**ISMS-IMP-A.5.9.4 - Owner Accountability Assessment**
**Assessment Specification with User Completion Guide**
### ISO/IEC 27001:2022 Control A.5.9: Inventory of Information and Other Associated Assets

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.9.4 |
| **Version** | 1.0 |
| **Assessment Area** | Asset Ownership Assignment & Accountability Verification |
| **Related Policy** | ISMS-POL-A.5.9, Section 2.4 (Ownership and Accountability), Section 4 (Roles and Responsibilities) |
| **Purpose** | Verify asset ownership is assigned, acknowledged, and understood; validate owner accountability and performance |
| **Target Audience** | Security Team, Asset Owners, Management, HR, Compliance Officers |
| **Assessment Type** | Ownership Verification & Accountability Audit |
| **Review Cycle** | Quarterly or After Significant Ownership Changes |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|--------|--------|
| 1.0 | [Date] | Initial assessment specification following consolidated policy structure | ISMS Implementation Team |

### Document Structure

This document consists of two parts:

- **PART I: USER COMPLETION GUIDE** (This Document)
  - Assessment Overview
  - Prerequisites
  - Assessment Workflow
  - Completing Each Sheet
  - Evidence Collection
  - Common Pitfalls
  - Quality Checklist
  - Review & Approval

- **PART II: TECHNICAL SPECIFICATION** (Separate Document)
  - Excel Workbook Structure
  - Sheet-by-Sheet Specifications
  - Formula Definitions
  - Python Script Implementation


**Target Audiences:**

- **Part I:** Assessment users (Security Team, Asset Owners, Management)
- **Part II:** Workbook developers (Python/Excel script maintainers)


---

# PART I: USER COMPLETION GUIDE

**Audience:** Security Team, Asset Owners, Management, HR

---

## Assessment Overview

### What This Assessment Evaluates

This assessment verifies that asset ownership is not just assigned, but that owners UNDERSTAND and ACCEPT their responsibilities. Ownership without accountability is ineffective.

**Key Questions This Assessment Answers**:

- Is EVERY asset assigned to an owner? (100% coverage)
- Do owners ACKNOWLEDGE and ACCEPT ownership? (signed attestations)
- Do owners UNDERSTAND their responsibilities? (awareness verification)
- Are owners CONTACTABLE and AVAILABLE? (valid contact information)
- Are owners PERFORMING their duties? (review compliance, update timeliness)
- Are ownership changes TRACKED and MANAGED? (transfer procedures)


**Assessment Philosophy**: Ownership is accountability. Without acknowledged, understood, and exercised ownership, the inventory becomes an orphaned data set.

### Why This Matters

This assessment verifies [Organization]'s compliance with:

- **ISO/IEC 27001:2022 Control A.5.9**: "**Ownership** of assets should be assigned"
- **ISMS-POL-A.5.9, Requirement A.5.9-R4**: [Organization] SHALL assign ownership to all inventoried assets (100% coverage)
- **ISMS-POL-A.5.9, Section 2.4**: Ownership and accountability requirements (owner responsibilities, acknowledgment, performance)
- **ISMS-POL-A.5.9, Section 4.2**: Asset owner role definition and responsibilities


**From Implementer Perspective**: Ensures owners are engaged, aware, and accountable for their assets.

**From Auditor Perspective**: Provides objective evidence that ownership is not just documented but actively acknowledged and exercised.

### Assessment Domains

This assessment covers **4 ownership accountability domains**:

| Domain | Focus | What You'll Document |
|--------|-------|---------------------|
| **1. Ownership Assignment** | Is every asset owned? | 100% coverage, valid owners, no placeholders/departed employees |
| **2. Owner Acknowledgment** | Do owners accept ownership? | Signed attestations, acknowledgment records, acceptance dates |
| **3. Owner Awareness** | Do owners understand responsibilities? | Training completion, awareness verification, responsibility documentation |
| **4. Owner Performance** | Are owners performing duties? | Review compliance, update responsiveness, engagement metrics |

### Assessment Outputs

**Generated Workbook**: `ISMS_A_5_9_Owner_Accountability_Assessment_YYYYMMDD.xlsx`

**Sheets** (7 total):
1. **Instructions**: How to complete this assessment
2. **Ownership Coverage**: Verify 100% assignment, identify unowned/invalid owners
3. **Owner Acknowledgment**: Track attestations, acceptance records, signatures
4. **Owner Awareness**: Verify understanding of responsibilities, training status
5. **Owner Performance**: Measure review compliance, responsiveness, engagement
6. **Accountability Metrics**: Aggregate ownership quality scores
7. **Evidence Register**: Attestations, training records, performance data

**Compliance Metrics Generated**:

- Ownership coverage (% assets with valid owner)
- Acknowledgment rate (% owners who have signed attestations)
- Awareness rate (% owners who completed training/awareness)
- Performance score (% owners meeting performance standards)
- Overall accountability score (weighted average)


---

## Prerequisites

### What You Need Before Starting

**1. Completed Assessments**:

- **ISMS-IMP-A.5.9.1**: Asset Discovery (know what assets exist)
- **ISMS-IMP-A.5.9.2**: Inventory Maintenance (know where ownership data is stored)


**2. Access to Systems**:

- Inventory system(s) (for owner assignments)
- HR system (to validate owners are current employees)
- Training/LMS system (to check training completion)
- Email system (for attestation tracking)


**3. Personnel**:

- **Security Team**: Leads assessment, tracks attestations
- **HR**: Validates employee status, assists with contact information
- **Asset Owners**: Provide attestations, complete awareness activities
- **Management**: Reviews owner performance, approves ownership changes


**4. Documentation**:

- Current inventory with owner assignments
- Owner responsibility documentation (from policy Section 4.2)
- Previous attestation records (if exist)
- Ownership change logs
- Training materials for asset owners


**5. Tools**:

- Email distribution lists (for attestation campaigns)
- Electronic signature platform (optional, for attestations)
- Tracking spreadsheet/database (for attestation status)


**6. Time Allocation**:

- **Initial Assessment**: 10-15 hours (plus owner attestation collection time)
- **Quarterly Updates**: 4-6 hours
- **Evidence Collection**: 2-4 hours per quarter
- **Owner Attestation Campaign**: 2-4 weeks (for owner responses)


---

## Assessment Workflow

### Step-by-Step Process

```
Phase 1: Ownership Coverage Verification (Day 1-2)
├─ Export full inventory with owners
├─ Identify unowned assets (NULL/empty owner field)
├─ Identify invalid owners (departed employees, placeholders)
├─ Cross-reference owners with HR system
└─ Prioritize ownership assignment gaps

Phase 2: Owner Acknowledgment Campaign (Day 3 - Week 4)
├─ Generate list of current owners
├─ Send attestation requests (email campaign)
├─ Track attestation responses
├─ Send reminders (Week 2, Week 3)
├─ Escalate non-responders to management (Week 4)
└─ Document attestation status

Phase 3: Owner Awareness Verification (Day 5-7)
├─ Check training system for owner training completion
├─ Identify owners without training
├─ Verify owner understanding (quiz, interview, or review)
└─ Document awareness gaps

Phase 4: Owner Performance Assessment (Day 8-10)
├─ Check last review date for each owned asset
├─ Calculate review compliance rate per owner
├─ Check update responsiveness (staleness of owned assets)
├─ Identify high-performing and low-performing owners
└─ Document performance data

Phase 5: Metrics & Reporting (Day 11-12)
├─ Calculate accountability metrics
├─ Identify remediation priorities
├─ Generate executive summary
└─ Document evidence register

Phase 6: Review & Approval (Day 13-14)
├─ Quality check against checklist
├─ Security Team review
├─ Management review (owner performance)
├─ CISO approval
└─ Submit to compliance dashboard
```

**Timeline**: 14 working days + up to 4 weeks for owner attestation collection (can overlap with other phases)

---

## Completing Each Sheet

### Sheet 1: Instructions

**Purpose**: Provides overview and guidance for completing this workbook.

**What to Do**:

- Read the instructions completely before starting
- Understand the 4 accountability domains
- Review the attestation process
- Note the scoring criteria


**No data entry required** - informational only.

---

### Sheet 2: Ownership Coverage

**Purpose**: Verify 100% ownership assignment and identify gaps.

**What This Sheet Captures**:

- Total assets by category
- Assets with owner assigned
- Assets without owner (gaps)
- Assets with invalid owner (departed employees, placeholders)
- Ownership coverage percentage by category


**Column Definitions**:

| Column | Purpose | How to Complete |
|--------|---------|-----------------|
| **Asset Category** | Type of asset | Dropdown: Information, IT, Applications, Physical, Personnel |
| **Total Assets** | Count in category | From inventory query |
| **Assets with Owner** | Count with owner assigned | From inventory query (owner field NOT NULL) |
| **Unowned Assets** | Missing owner | Formula: Total - Owned |
| **Assets with Invalid Owner** | Departed employees, placeholders | From cross-reference with HR |
| **Valid Ownership %** | Percentage valid | Formula: (Owned - Invalid) / Total × 100% |
| **Compliance Status** | Met target or not | Auto-calculated: Pass = 100%, Fail < 100% |
| **Top Unowned Assets** | Examples of unowned | List asset IDs/names |
| **Top Invalid Owners** | Departed employee names | List for remediation |
| **Remediation Plan** | How to fix | Free text: Action plan |
| **Target Date** | When to fix by | Date field |
| **Responsible Party** | Who will fix | Free text: Team/role |
| **Notes** | Additional context | Free text |

**How to Complete**:

**Step 1: Query Inventory for Ownership Data**

```sql
-- Example SQL query (adapt to your inventory system)
SELECT 
    AssetCategory,
    COUNT(*) AS TotalAssets,
    COUNT(Owner) AS AssetsWithOwner,
    COUNT(*) - COUNT(Owner) AS UnownedAssets
FROM Inventory
GROUP BY AssetCategory
```

**Step 2: Cross-Reference Owners with HR**

```sql
-- Identify owners not in HR system
SELECT DISTINCT Owner
FROM Inventory
WHERE Owner NOT IN (SELECT EmployeeID FROM HR_System)
```

**Example 1: Information Assets - Good Coverage**

- **Asset Category**: Information Assets
- **Total Assets**: 400
- **Assets with Owner**: 398
- **Unowned Assets**: 2 (formula auto-calculates)
- **Assets with Invalid Owner**: 3 (owners: "John Smith" departed 6 months ago, "Jane Doe" transferred to different company, "TBD" placeholder)
- **Valid Ownership %**: 98.75% (formula: (398-3)/400 × 100%)
- **Compliance Status**: Fail (target is 100%)
- **Top Unowned Assets**: DB-00456 (Customer Database - legacy, unclear owner), DOC-00789 (Old project documentation)
- **Top Invalid Owners**: John Smith (3 assets), TBD (1 asset)
- **Remediation Plan**: "Reassign John Smith's 3 assets to current Database Administrator. Assign ownership for 2 unowned assets. Eliminate TBD placeholder."
- **Target Date**: 05.02.2026 (2 weeks)
- **Responsible Party**: Information Security Manager


**Example 2: IT Infrastructure - Perfect Coverage**

- **Asset Category**: IT Infrastructure
- **Total Assets**: 600
- **Assets with Owner**: 600
- **Unowned Assets**: 0
- **Assets with Invalid Owner**: 0
- **Valid Ownership %**: 100% ✅
- **Compliance Status**: Pass
- **Remediation Plan**: N/A (maintain compliance)


**Example 3: Personnel Assets - Invalid Owner Issue**

- **Asset Category**: Personnel Assets
- **Total Assets**: 50
- **Assets with Owner**: 50
- **Unowned Assets**: 0
- **Assets with Invalid Owner**: 5 (owner: "HR Department" - department, not person)
- **Valid Ownership %**: 90%
- **Compliance Status**: Fail
- **Top Invalid Owners**: "HR Department" (5 assets - need individual assignment)
- **Remediation Plan**: "Assign individual HR manager as owner for each competency area rather than generic 'HR Department'"
- **Target Date**: 12.02.2026


**Targets (from policy)**:

- Ownership coverage: 100%
- Invalid owners: 0%


**Common Pitfalls**:

- ❌ Accepting department names as owners ("IT Department", "Finance Team")
- ✅ Owners must be individuals, not departments (accountability requires a person)
- ❌ Not cross-referencing with HR (missing departed employees)
- ✅ Monthly cross-reference to catch employee departures
- ❌ Allowing "TBD", "Unknown", "To Be Assigned" placeholders
- ✅ These count as unowned - must assign actual person


---

### Sheet 3: Owner Acknowledgment

**Purpose**: Track owner attestations and acceptance of ownership.

**What This Sheet Captures**:

- List of all asset owners
- Attestation status (signed, pending, not started)
- Attestation dates
- Attestation method (email, e-signature, physical)
- Assets owned per person
- Acknowledgment rate


**Column Definitions**:

| Column | Purpose | How to Complete |
|--------|---------|-----------------|
| **Owner Name** | Asset owner | From inventory (unique list of owners) |
| **Owner Email** | Contact email | From HR or inventory |
| **Owner Department** | Organizational unit | From HR |
| **Assets Owned - Count** | Number of assets | From inventory (COUNT by owner) |
| **Asset Categories** | Types of assets owned | From inventory (Info, IT, App, etc.) |
| **Attestation Status** | Current status | Dropdown: ✅ Signed / 📧 Sent, Pending / ❌ Not Sent / 🔴 Overdue |
| **Attestation Method** | How acknowledged | Dropdown: Email Confirmation / E-Signature (DocuSign, etc.) / Physical Signature / Verbal (Meeting) |
| **Attestation Date** | When signed | Date field |
| **Days Since Request** | Elapsed time | Formula: TODAY() - Request Date |
| **Reminder Count** | Reminders sent | Numeric: Count of reminder emails |
| **Last Reminder Date** | When last reminded | Date field |
| **Escalation Required** | Needs management follow-up | Dropdown: Yes / No |
| **Evidence Reference** | Link to signed attestation | Reference to Evidence Register |
| **Notes** | Additional context | Free text |

**How to Complete**:

**Step 1: Generate Unique List of Owners**

```sql
SELECT DISTINCT Owner, COUNT(*) AS AssetCount
FROM Inventory
WHERE Owner IS NOT NULL
GROUP BY Owner
ORDER BY AssetCount DESC
```

**Step 2: Launch Attestation Campaign**

**Attestation Email Template**:
```
Subject: Action Required: Asset Ownership Attestation for [Quarter/Year]

Dear [Owner Name],

You are listed as the owner of [N] assets in our Information Asset Inventory. 
As an asset owner, you have specific responsibilities per ISMS-POL-A.5.9:

1. Ensure asset information is accurate and current
2. Review asset details at least [frequency] per policy
3. Approve access requests for your assets
4. Report security incidents involving your assets
5. Participate in asset decommissioning decisions

Please confirm your acceptance of ownership by replying to this email with:
"I, [Your Name], acknowledge and accept ownership of the [N] assets assigned 
to me and understand my responsibilities as documented in ISMS-POL-A.5.9."

Your assets:
[Asset List]

Questions? Contact: [Security Team Email]

Deadline: [2 weeks from today]

Thank you,
[Organization] Information Security Team
```

**Step 3: Track Responses**

**Example 1: Attestation Complete**

- **Owner Name**: Alice Johnson
- **Owner Email**: alice.johnson@company.com
- **Owner Department**: Engineering
- **Assets Owned - Count**: 45
- **Asset Categories**: IT Infrastructure (servers), Applications (engineering tools)
- **Attestation Status**: ✅ Signed
- **Attestation Method**: Email Confirmation
- **Attestation Date**: 08.01.2026
- **Days Since Request**: 7 days (responded quickly)
- **Reminder Count**: 0 (responded before first reminder)
- **Escalation Required**: No
- **Evidence Reference**: ACCT-001 (email confirmation saved)


**Example 2: Pending Response**

- **Owner Name**: Bob Williams
- **Owner Email**: bob.williams@company.com
- **Owner Department**: Finance
- **Assets Owned - Count**: 12
- **Asset Categories**: Information Assets (financial reports)
- **Attestation Status**: 📧 Sent, Pending
- **Attestation Method**: Email Confirmation (requested, awaiting)
- **Attestation Date**: [blank - not yet received]
- **Days Since Request**: 10 days
- **Reminder Count**: 1 (first reminder sent at day 7)
- **Last Reminder Date**: 18.01.2026
- **Escalation Required**: No (not yet - escalate at 21 days)


**Example 3: Overdue**

- **Owner Name**: Carol Martinez
- **Owner Email**: carol.martinez@company.com
- **Owner Department**: Marketing
- **Assets Owned - Count**: 8
- **Asset Categories**: Information Assets (marketing databases)
- **Attestation Status**: 🔴 Overdue
- **Attestation Method**: Email Confirmation (requested, no response)
- **Attestation Date**: [blank]
- **Days Since Request**: 25 days
- **Reminder Count**: 3 (reminders at day 7, 14, 21)
- **Last Reminder Date**: 17.01.2026
- **Escalation Required**: Yes (escalate to Marketing Director)
- **Notes**: "No response to 3 email attempts. Escalated to Marketing Director on 22.01.2026."


**Step 4: Calculate Acknowledgment Rate**

Sheet auto-calculates:

- Total owners: COUNT(all rows)
- Owners with attestation: COUNT(status = "Signed")
- Acknowledgment rate: (Signed / Total) × 100%


**Target**: 95% acknowledgment rate (minimum), 100% ideal

**Attestation Timeline**:

- Day 0: Send initial attestation request
- Day 7: First reminder to non-responders
- Day 14: Second reminder
- Day 21: Third reminder + escalation warning
- Day 28: Escalate to management


**Common Pitfalls**:

- ❌ One-time attestation campaign, never repeated
- ✅ Annual attestation (minimum), quarterly for critical assets
- ❌ Accepting verbal acknowledgment without documentation
- ✅ Email confirmation minimum, e-signature preferred (audit trail)
- ❌ Not following up on non-responders
- ✅ Systematic reminder and escalation process


---

### Sheet 4: Owner Awareness

**Purpose**: Verify owners understand their responsibilities.

**What This Sheet Captures**:

- Owner training completion status
- Awareness verification method
- Understanding assessment results
- Knowledge gaps identified
- Training/awareness improvement plans


**Column Definitions**:

| Column | Purpose | How to Complete |
|--------|---------|-----------------|
| **Owner Name** | Asset owner | From Sheet 3 (unique owners) |
| **Training Required** | Is training mandatory? | Dropdown: Yes / No (Yes for owners of Critical/High assets) |
| **Training Completed** | Has owner completed training? | Dropdown: ✅ Yes / ❌ No / 🕒 In Progress |
| **Training Date** | When completed | Date field |
| **Training Method** | How trained | Dropdown: E-Learning (LMS) / Instructor-Led / Self-Study / Not Yet Trained |
| **Training Score** | If assessed | Numeric: Percentage (0-100) or N/A |
| **Awareness Verification** | How understanding verified | Dropdown: Quiz / Interview / Document Review / Attestation Only |
| **Verification Date** | When verified | Date field |
| **Understanding Level** | Assessment result | Dropdown: Excellent / Good / Fair / Poor / Not Assessed |
| **Knowledge Gaps** | What owner doesn't understand | Free text: Specific gaps |
| **Remediation Plan** | How to close gaps | Free text: Additional training, coaching |
| **Target Date** | When to remediate | Date field |
| **Evidence Reference** | Link to training record | Reference to Evidence Register |
| **Notes** | Additional context | Free text |

**How to Complete**:

**Step 1: Query Training System**

Check LMS or training records for "Asset Owner Training" completion:

- Who completed
- Completion date
- Assessment score (if applicable)


**Step 2: Verify Understanding**

**Awareness Verification Methods**:

**Option A: Knowledge Quiz** (preferred for large owner population)

- 5-10 questions on owner responsibilities
- 80% passing score
- Automatic via LMS
- Example questions:
  - "How often must you review your assets per policy?" (Answer: Annually minimum)
  - "What should you do if you're no longer responsible for an asset?" (Answer: Request ownership transfer)
  - "Who approves access requests to your assets?" (Answer: You, the asset owner)


**Option B: Interview** (for small owner population or critical asset owners)

- 15-minute discussion with Security Team
- Discuss owner responsibilities
- Ask scenario questions
- Document understanding level


**Option C: Document Review** (lightweight, combine with attestation)

- Owner reviews responsibility document
- Signs acknowledgment that they've read and understood
- No formal assessment


**Example 1: Training Complete, Good Understanding**

- **Owner Name**: Alice Johnson
- **Training Required**: Yes (owns critical servers)
- **Training Completed**: ✅ Yes
- **Training Date**: 10.12.2025
- **Training Method**: E-Learning (LMS)
- **Training Score**: 95%
- **Awareness Verification**: Quiz
- **Verification Date**: 10.12.2025 (same day as training)
- **Understanding Level**: Excellent
- **Knowledge Gaps**: None identified
- **Evidence Reference**: ACCT-010 (LMS completion certificate)


**Example 2: No Training, Assessment Pending**

- **Owner Name**: Bob Williams
- **Training Required**: Yes (owns confidential financial data)
- **Training Completed**: ❌ No
- **Training Date**: [blank]
- **Training Method**: Not Yet Trained
- **Awareness Verification**: Not Assessed
- **Understanding Level**: Not Assessed
- **Knowledge Gaps**: Unknown (training not completed)
- **Remediation Plan**: "Enroll Bob in next Asset Owner training session (scheduled 05.02.2026). Follow up to ensure completion within 30 days."
- **Target Date**: 05.03.2026


**Example 3: Training Complete, Poor Understanding**

- **Owner Name**: David Chen
- **Training Required**: Yes
- **Training Completed**: ✅ Yes
- **Training Date**: 15.01.2026
- **Training Method**: E-Learning (LMS)
- **Training Score**: 65% (below 80% passing)
- **Awareness Verification**: Quiz
- **Verification Date**: 15.01.2026
- **Understanding Level**: Poor
- **Knowledge Gaps**: "Unclear on review frequency requirements, confused about ownership transfer process"
- **Remediation Plan**: "1-on-1 coaching session with Security Team to clarify responsibilities. Retake quiz after coaching."
- **Target Date**: 29.01.2026
- **Notes**: "David is new to organization, needs additional support"


**Step 3: Calculate Awareness Rate**

Sheet auto-calculates:

- Total owners requiring training
- Owners with training complete AND understanding verified
- Awareness rate: (Trained & Verified / Total Required) × 100%


**Target**: 100% for owners of Critical/High assets, 80% for Standard/Low

**Common Pitfalls**:

- ❌ Assuming attestation = understanding (it doesn't!)
- ✅ Verify understanding through quiz, interview, or review
- ❌ One-time training, never refreshed
- ✅ Annual refresher training (minimum)
- ❌ Generic InfoSec training without asset owner specifics
- ✅ Targeted training on owner responsibilities per ISMS-POL-A.5.9


---

### Sheet 5: Owner Performance

**Purpose**: Measure whether owners are actually performing their duties.

**What This Sheet Captures**:

- Review compliance (are owners reviewing their assets on schedule?)
- Update responsiveness (do owners keep asset info current?)
- Engagement level (do owners respond to requests?)
- Performance scoring
- High/low performer identification


**Column Definitions**:

| Column | Purpose | How to Complete |
|--------|---------|-----------------|
| **Owner Name** | Asset owner | From Sheet 3 |
| **Assets Owned - Count** | Number of assets | From inventory |
| **Critical/High Assets** | Count of high-value assets | From inventory (criticality filter) |
| **Last Review Date - Avg** | Average last review across owned assets | From inventory (average LastReviewDate) |
| **Days Since Avg Review** | Staleness | Formula: TODAY() - Last Review Date Avg |
| **Review Compliance %** | % of assets reviewed on time | From inventory: (Assets reviewed within period / Total assets) × 100% |
| **Update Responsiveness** | Do owners update when notified? | Dropdown: Excellent / Good / Fair / Poor |
| **Response Time - Avg** | Average days to respond to update requests | From tracking data |
| **Engagement Score** | Overall engagement metric | Formula: Weighted average of compliance, responsiveness |
| **Performance Rating** | Overall performance | Auto-calculated: High Performer / Meets Expectations / Needs Improvement / Poor |
| **Assets at Risk** | Count of stale/incomplete assets | From inventory (owned assets exceeding staleness threshold) |
| **Action Required** | What owner needs to do | Free text: Specific actions |
| **Evidence Reference** | Link to performance data | Reference to Evidence Register |
| **Notes** | Additional context | Free text |

**How to Complete**:

**Step 1: Calculate Review Compliance**

For each owner, query inventory:
```sql
SELECT Owner,
       COUNT(*) AS TotalAssets,
       SUM(CASE WHEN LastReviewDate >= (TODAY() - 365) THEN 1 ELSE 0 END) AS ReviewedWithinYear,
       (ReviewedWithinYear / TotalAssets * 100) AS ReviewCompliance
FROM Inventory
WHERE Owner IS NOT NULL
GROUP BY Owner
```

**Step 2: Assess Update Responsiveness**

Track owner response to update requests:

- When notified of stale data, how quickly do they update?
- Excellent: <3 days
- Good: 3-7 days
- Fair: 7-14 days
- Poor: >14 days or no response


**Step 3: Calculate Engagement Score**

```
Engagement Score = (Review Compliance × 60%) + (Responsiveness × 40%)

Where Responsiveness = 
  Excellent: 100%
  Good: 80%
  Fair: 60%
  Poor: 20%
```

**Example 1: High Performer**

- **Owner Name**: Alice Johnson
- **Assets Owned - Count**: 45
- **Critical/High Assets**: 15
- **Last Review Date - Avg**: 45 days ago
- **Days Since Avg Review**: 45
- **Review Compliance %**: 98% (44 of 45 assets reviewed within year)
- **Update Responsiveness**: Excellent (responds within 24 hours)
- **Response Time - Avg**: 1.2 days
- **Engagement Score**: 98.8% (formula: 98% × 60% + 100% × 40%)
- **Performance Rating**: High Performer ⭐
- **Assets at Risk**: 0
- **Action Required**: None (maintain excellent performance)
- **Notes**: "Model asset owner, consistently engaged"


**Example 2: Meets Expectations**

- **Owner Name**: Bob Williams
- **Assets Owned - Count**: 12
- **Critical/High Assets**: 3
- **Last Review Date - Avg**: 180 days ago
- **Review Compliance %**: 75% (9 of 12 reviewed within year, 3 overdue)
- **Update Responsiveness**: Good (responds within 5 days)
- **Response Time - Avg**: 4.8 days
- **Engagement Score**: 77% (formula: 75% × 60% + 80% × 40%)
- **Performance Rating**: Meets Expectations
- **Assets at Risk**: 3 (overdue for review)
- **Action Required**: "Review 3 overdue assets within 2 weeks"


**Example 3: Needs Improvement**

- **Owner Name**: Carol Martinez
- **Assets Owned - Count**: 8
- **Critical/High Assets**: 0
- **Last Review Date - Avg**: 400 days ago
- **Review Compliance %**: 25% (2 of 8 reviewed, 6 overdue)
- **Update Responsiveness**: Poor (slow or no response)
- **Response Time - Avg**: 18 days
- **Engagement Score**: 23% (formula: 25% × 60% + 20% × 40%)
- **Performance Rating**: Needs Improvement ⚠️
- **Assets at Risk**: 6
- **Action Required**: "Urgent: Review all 6 overdue assets within 1 week. Escalate to manager if no action."
- **Notes**: "Multiple reminder emails sent, minimal engagement. Potential ownership reassignment if no improvement."


**Example 4: Poor Performance - Ownership Transfer Recommended**

- **Owner Name**: David Chen
- **Assets Owned - Count**: 20
- **Critical/High Assets**: 5
- **Last Review Date - Avg**: 730 days ago (2 years!)
- **Review Compliance %**: 0% (no reviews in past year)
- **Update Responsiveness**: Poor (no response)
- **Response Time - Avg**: N/A (doesn't respond)
- **Engagement Score**: 8% (formula: 0% × 60% + 20% × 40%)
- **Performance Rating**: Poor ❌
- **Assets at Risk**: 20 (all assets)
- **Action Required**: "Immediate escalation to management. Recommend ownership transfer to engaged owner. Critical assets at risk."
- **Notes**: "David has not engaged with asset ownership responsibilities for 2 years. Urgent action required."


**Performance Thresholds**:

- **High Performer**: Engagement ≥90%
- **Meets Expectations**: Engagement 70-89%
- **Needs Improvement**: Engagement 50-69%
- **Poor**: Engagement <50%


**Common Pitfalls**:

- ❌ Not measuring owner performance (assume owners are engaged)
- ✅ Track review compliance, responsiveness, engagement
- ❌ Tolerating poor performance indefinitely
- ✅ Escalate poor performers, reassign ownership if no improvement
- ❌ No recognition for high performers
- ✅ Highlight and thank high-performing owners, share best practices


---

### Sheet 6: Accountability Metrics

**Purpose**: Aggregate ownership accountability scores.

**What This Sheet Captures**:

- Accountability dimensions (Coverage, Acknowledgment, Awareness, Performance)
- Scores for each dimension
- Weighted overall accountability score
- Trending vs. previous quarter


**This sheet is MOSTLY auto-populated** from other sheets.

**Column Definitions**:

| Column | Purpose | How to Complete |
|--------|---------|-----------------|
| **Accountability Dimension** | Dimension name | Fixed: Coverage / Acknowledgment / Awareness / Performance |
| **Weight** | Importance weighting | Fixed: 30% / 25% / 20% / 25% |
| **Target Score** | Policy requirement | Fixed: 100% / 95% / 100% / 80% |
| **Actual Score** | Current achievement | Auto-calculated from sheets 2-5 |
| **Gap vs. Target** | Shortfall | Formula: Actual - Target |
| **Compliance Status** | Met target or not | Auto-calculated: ✅ / ⚠️ / ❌ |
| **Trend vs. Last Quarter** | Improving or degrading | Dropdown: Improved / Stable / Degraded / N/A |
| **Key Issues** | Top problems | Free text summary |
| **Remediation Actions** | What to fix | Free text |
| **Notes** | Additional context | Free text |

**Accountability Dimensions**:

**1. Ownership Coverage (Weight: 30%)**

- Target: 100% (all assets have valid owner)
- Actual: From Sheet 2 (average Valid Ownership % across categories)


**2. Owner Acknowledgment (Weight: 25%)**

- Target: 95% (minimum acceptable)
- Actual: From Sheet 3 (Acknowledgment Rate %)


**3. Owner Awareness (Weight: 20%)**

- Target: 100% (all required owners trained and verified)
- Actual: From Sheet 4 (Awareness Rate %)


**4. Owner Performance (Weight: 25%)**

- Target: 80% (average Engagement Score ≥80%)
- Actual: From Sheet 5 (average Engagement Score across all owners)


**Overall Accountability Score**:
```
Overall = (Coverage × 30%) + (Acknowledgment × 25%) + 
          (Awareness × 20%) + (Performance × 25%)
```

**Scoring Interpretation**:

- **95-100%**: Excellent (strong accountability culture)
- **85-94%**: Good (acceptable, minor gaps)
- **75-84%**: Fair (significant improvements needed)
- **<75%**: Poor (major accountability issues)


**Example Scorecard**:

| Dimension | Weight | Target | Actual | Gap | Status | Trend |
|-----------|--------|--------|--------|-----|--------|-------|
| Coverage | 30% | 100% | 98% | -2% | ⚠️ | Improved |
| Acknowledgment | 25% | 95% | 89% | -6% | ⚠️ | Stable |
| Awareness | 20% | 100% | 85% | -15% | ❌ | Improved |
| Performance | 25% | 80% | 76% | -4% | ⚠️ | Stable |
| **Overall** | **100%** | **94%** | **88.1%** | **-5.9%** | ⚠️ | **Improved** |

Interpretation: Good accountability (88%), approaching target. Main gaps: Awareness (need more training) and Acknowledgment (need better attestation follow-up).

---

### Sheet 7: Evidence Register

**Purpose**: Document all evidence related to owner accountability.

**Column Definitions**: Same as previous assessments with adjusted Related Domain:

**Related Domain** dropdown:

- Ownership Coverage
- Owner Acknowledgment
- Owner Awareness
- Owner Performance
- Accountability Metrics
- All Domains


**Evidence ID format**: `ACCT-NNN` (e.g., ACCT-001, ACCT-002, etc.)

**Example Evidence Items**:

1. **ACCT-001**: Owner attestation - Alice Johnson (email confirmation)
2. **ACCT-010**: LMS training completion certificate - Alice Johnson
3. **ACCT-020**: Ownership coverage query results (unowned assets list)
4. **ACCT-030**: HR cross-reference report (invalid owners)
5. **ACCT-040**: Performance tracking data (review compliance by owner)

---

## Evidence Collection

### What Evidence to Collect

**Ownership Coverage Evidence**:

- Inventory export with owner assignments
- HR system cross-reference report (valid employees)
- Unowned asset list
- Invalid owner list (departed employees, placeholders)


**Owner Acknowledgment Evidence**:

- Signed attestations (email confirmations, e-signatures)
- Attestation campaign tracking (sent date, response date)
- Reminder emails
- Escalation correspondence


**Owner Awareness Evidence**:

- Training completion certificates (LMS exports)
- Quiz results (if applicable)
- Interview notes (if applicable)
- Awareness verification documentation


**Owner Performance Evidence**:

- Review compliance reports (by owner)
- Update responsiveness tracking data
- Engagement score calculations
- Performance rating assignments


### Evidence Organization

```
/evidence/
├── 2026-Q1/
│   ├── ownership-coverage/
│   │   ├── inventory-export-with-owners.xlsx
│   │   ├── hr-cross-reference.xlsx
│   │   └── invalid-owners-list.pdf
│   ├── owner-acknowledgment/
│   │   ├── attestations/
│   │   │   ├── alice-johnson-attestation.pdf
│   │   │   ├── bob-williams-attestation.pdf
│   │   │   └── [other attestations]
│   │   └── attestation-tracking.xlsx
│   ├── owner-awareness/
│   │   ├── training-certificates/
│   │   ├── quiz-results.xlsx
│   │   └── awareness-verification.pdf
│   ├── owner-performance/
│   │   ├── review-compliance-report.xlsx
│   │   ├── responsiveness-tracking.xlsx
│   │   └── engagement-scores.xlsx
│   └── accountability-metrics/
│       └── accountability-scorecard.xlsx
└── 2026-Q2/
    └── [same structure]
```

---

## Common Pitfalls

### Pitfall 1: Ownership Without Accountability

**Problem**: Assigning owners but never verifying they understand or perform responsibilities.

**Why It Fails**: Owners become "owners in name only", don't actually manage assets.

**Solution**: Require attestation, verify awareness, measure performance.

### Pitfall 2: Accepting Department Names as Owners

**Problem**: "IT Department", "Finance Team" listed as owners.

**Why It Fails**: No individual accountability, unclear who to contact.

**Solution**: Owners must be individuals. If multiple people share responsibility, assign primary owner + delegates.

### Pitfall 3: One-Time Attestation, Never Repeated

**Problem**: Collecting attestations once, never asking again.

**Why It Fails**: Ownership changes, people forget responsibilities, attestations become stale.

**Solution**: Annual attestation (minimum), quarterly for critical assets.

### Pitfall 4: Not Tracking Owner Performance

**Problem**: Assuming owners are engaged without measuring.

**Why It Fails**: Poor performers go unnoticed, assets become orphaned over time.

**Solution**: Track review compliance, responsiveness, engagement. Escalate poor performers.

### Pitfall 5: No Consequences for Non-Acknowledgment

**Problem**: Sending attestation requests but not following up on non-responders.

**Why It Fails**: Owners learn they can ignore requests without consequence.

**Solution**: Systematic reminder and escalation process. Escalate to management, consider reassignment.

### Pitfall 6: Generic Training, No Owner Specifics

**Problem**: Generic InfoSec awareness training without asset owner responsibilities.

**Why It Fails**: Owners don't understand their specific duties.

**Solution**: Targeted asset owner training on responsibilities per ISMS-POL-A.5.9.

### Pitfall 7: Tolerating Invalid Owners Indefinitely

**Problem**: Knowing departed employees are still listed as owners, not fixing it.

**Why It Fails**: Assets become truly orphaned, no one accountable.

**Solution**: Monthly HR cross-reference, immediate reassignment on employee departure.

---

## Quality Checklist

Before submitting this assessment, verify:

### Coverage Checks

- [ ] 100% ownership coverage verified (or gaps documented with remediation plan)
- [ ] Cross-reference with HR completed (no departed employees as owners)
- [ ] No placeholder owners ("TBD", "Unknown", etc.)
- [ ] Department names replaced with individual owners
- [ ] Unowned assets prioritized by criticality


### Acknowledgment Checks

- [ ] Attestation campaign launched (all current owners contacted)
- [ ] Attestation responses tracked (signed, pending, overdue)
- [ ] Reminders sent per schedule (Day 7, 14, 21)
- [ ] Non-responders escalated to management
- [ ] Attestation evidence collected and stored
- [ ] Acknowledgment rate calculated


### Awareness Checks

- [ ] Training requirements defined (who needs training)
- [ ] Training completion verified (LMS query or records check)
- [ ] Understanding verified (quiz, interview, or review)
- [ ] Knowledge gaps identified
- [ ] Remediation plans for poor understanding
- [ ] Awareness rate calculated


### Performance Checks

- [ ] Review compliance calculated per owner
- [ ] Update responsiveness tracked
- [ ] Engagement scores calculated
- [ ] Performance ratings assigned
- [ ] High/low performers identified
- [ ] Action plans for poor performers
- [ ] Average performance score calculated


### Metrics Checks

- [ ] All 4 dimensions calculated
- [ ] Overall accountability score computed
- [ ] Trending vs. previous quarter documented
- [ ] Remediation priorities identified
- [ ] Executive summary prepared


### Evidence Checks

- [ ] All attestations saved
- [ ] Training records exported
- [ ] Performance data documented
- [ ] Evidence metadata complete
- [ ] Evidence stored securely per retention policy


---

## Review & Approval

### Review Process

**Step 1: Self-Review** (Assessment Preparer)

- Complete quality checklist above
- Verify calculations
- Check evidence completeness


**Step 2: HR Review** (Optional but Recommended)

- Validate employee status cross-reference
- Confirm departed employee handling
- Review ownership transfer process


**Step 3: Management Review**

- Review owner performance ratings
- Approve escalations for poor performers
- Approve ownership reassignments if needed


**Step 4: Security Review** (Information Security Manager)

- Review accountability scores vs. targets
- Assess gap severity and priorities
- Verify policy compliance
- Review remediation timeline


**Step 5: CISO Approval**

- Review executive summary (accountability scorecard)
- Assess overall accountability culture
- Approve remediation plans
- Escalate critical gaps to Executive Management
- Sign approval


**Step 6: Submission to Compliance Dashboard**

- Export metrics to dashboard consolidation
- Update ISMS-IMP-A.5.9.5 (Compliance Dashboard)
- Archive assessment workbook
- Store evidence per retention policy


### Approval Criteria

**Approve** if:

- ✅ Overall accountability score ≥85%
- ✅ Ownership coverage ≥95% (100% ideal)
- ✅ No critical assets with invalid/missing owners
- ✅ Remediation plans exist for all gaps


**Conditional Approval** (with immediate remediation) if:

- ⚠️ Overall accountability score 75-84%
- ⚠️ Ownership coverage 90-94%
- ⚠️ Some critical assets with ownership gaps (but remediation in progress)


**Reject** if:

- ❌ Overall accountability score <75%
- ❌ Ownership coverage <90%
- ❌ Critical assets with no owner and no remediation plan
- ❌ Systemic non-engagement (most owners not responding)


---

**END OF ISMS-IMP-A.5.9.4 PART I - USER COMPLETION GUIDE**

# PART II: TECHNICAL SPECIFICATION

**Audience:** Workbook developers (Python/Excel script maintainers)

---

## Document Overview

### Purpose of Technical Specification

This section provides complete technical specifications for developers creating or maintaining the Python script that generates the Owner Accountability Assessment workbook.

**Python Script**: `generate_a59_4_owner_accountability.py`

**Generated Workbook**: `ISMS_A_5_9_Owner_Accountability_Assessment_YYYYMMDD.xlsx`

**Key Design Principles**:
1. **Accountability Focus**: Measure not just assignment, but engagement and performance
2. **Tracking Capability**: Support multi-week attestation campaigns
3. **Performance Metrics**: Objective owner performance measurement
4. **Evidence Collection**: Structured attestation and training record tracking
5. **Trending**: Support quarter-over-quarter accountability improvement

---

## Excel Workbook Structure

### Workbook Metadata

**Workbook Properties**:

- **Title**: ISMS A.5.9 Owner Accountability Assessment
- **Subject**: ISO/IEC 27001:2022 Control A.5.9 - Asset Ownership Verification
- **Author**: [Organization] ISMS Implementation Team
- **Company**: [Organization]
- **Created**: [Generation Date]
- **Version**: 1.0


### Sheet Summary

| Sheet # | Sheet Name | Purpose | User Input | Formulas | Protection |
|---------|-----------|---------|------------|----------|-----------|
| 1 | Instructions | User guide | None (read-only) | None | Full |
| 2 | Ownership Coverage | Verify 100% assignment | Yes | Coverage % calcs | Partial |
| 3 | Owner Acknowledgment | Track attestations | Yes | Acknowledgment % | Partial |
| 4 | Owner Awareness | Verify training/understanding | Yes | Awareness % | Partial |
| 5 | Owner Performance | Measure engagement | Yes | Performance scores | Partial |
| 6 | Accountability Metrics | Aggregate scores | Auto-populated | All metrics | Partial |
| 7 | Evidence Register | Evidence tracking | Yes | None | Partial |

---

## Global Styling Standards

Same as IMP-A.5.9-1/2/3 (refer to those documents for detailed color palette and styling).

---

## Sheet 2: Ownership Coverage - Complete Specification

### Purpose

Verify 100% ownership assignment, identify gaps.

### Column Structure

**Total Columns: 13 (A through M)**

| Col | Header | Width | Type | Validation | Formula | Lock |
|-----|--------|-------|------|------------|---------|------|
| A | Asset Category | 20 | List | Dropdown | None | No |
| B | Total Assets | 12 | Number | Integer ≥0 | None | No |
| C | Assets with Owner | 12 | Number | Integer ≥0 | None | No |
| D | Unowned Assets | 12 | Number | None | Formula | Yes |
| E | Assets with Invalid Owner | 12 | Number | Integer ≥0 | None | No |
| F | Valid Ownership % | 12 | Number | None | Formula | Yes |
| G | Compliance Status | 15 | Text | None | Formula | Yes |
| H | Top Unowned Assets | 40 | Text | None | None | No |
| I | Top Invalid Owners | 30 | Text | None | None | No |
| J | Remediation Plan | 40 | Text | None | None | No |
| K | Target Date | 15 | Date | Date validation | None | No |
| L | Responsible Party | 25 | Text | None | None | No |
| M | Notes | 30 | Text | None | None | No |

### Data Validation

**Column A: Asset Category**

```python
asset_categories = [
    "Information Assets",
    "IT Infrastructure",
    "Applications",
    "Physical Assets",
    "Personnel Assets"
]

dv_asset_cat = DataValidation(
    type="list",
    formula1=f'"{",".join(asset_categories)}"',
    allow_blank=False
)
dv_asset_cat.add('A3:A10')
ws.add_data_validation(dv_asset_cat)
```

### Formulas

**Column D: Unowned Assets**

```python
for row in range(3, 11):
    ws[f'D{row}'] = f'=B{row}-C{row}'
    ws[f'D{row}'].protection = Protection(locked=True)
```

**Column F: Valid Ownership %**

```python
for row in range(3, 11):
    ws[f'F{row}'] = f'=IFERROR((C{row}-E{row})/B{row}*100,0)'
    ws[f'F{row}'].number_format = '0.0"%"'
    ws[f'F{row}'].protection = Protection(locked=True)
```

**Column G: Compliance Status**

```python
for row in range(3, 11):
    formula = f'=IF(F{row}=100,"✅ Pass","❌ Fail")'
    ws[f'G{row}'] = formula
    ws[f'G{row}'].alignment = Alignment(horizontal='center')
    ws[f'G{row}'].protection = Protection(locked=True)
```

### Conditional Formatting

**Column F: Valid Ownership % - Traffic Light**

```python
# Green: 100%
complete_rule = CellIsRule(
    operator='equal',
    formula=['100'],
    fill=PatternFill(start_color='C6EFCE', fill_type='solid'),
    font=Font(color='006100', bold=True)
)
ws.conditional_formatting.add('F3:F10', complete_rule)

# Yellow: 95-99%
near_complete_rule = CellIsRule(
    operator='between',
    formula=['95', '99'],
    fill=PatternFill(start_color='FFEB9C', fill_type='solid'),
    font=Font(color='9C5700', bold=True)
)
ws.conditional_formatting.add('F3:F10', near_complete_rule)

# Red: < 95%
incomplete_rule = CellIsRule(
    operator='lessThan',
    formula=['95'],
    fill=PatternFill(start_color='FFC7CE', fill_type='solid'),
    font=Font(color='9C0006', bold=True)
)
ws.conditional_formatting.add('F3:F10', incomplete_rule)
```

### Summary Section

**Location**: Rows 13-16

```python
# Overall Ownership Coverage
ws['A13'] = "Overall Ownership Coverage %"
ws['B13'] = '=IFERROR(AVERAGE(F3:F10),0)'
ws['B13'].number_format = '0.0"%"'
ws['B13'].font = Font(bold=True, size=12)

ws['A14'] = "Total Assets Across All Categories"
ws['B14'] = '=SUM(B3:B10)'

ws['A15'] = "Total Unowned Assets"
ws['B15'] = '=SUM(D3:D10)'

ws['A16'] = "Total Invalid Owners"
ws['B16'] = '=SUM(E3:E10)'
```

---

## Sheet 3: Owner Acknowledgment - Complete Specification

### Purpose

Track attestations and acceptance of ownership.

### Column Structure

**Total Columns: 14 (A through N)**

| Col | Header | Width | Type | Validation | Formula | Lock |
|-----|--------|-------|------|------------|---------|------|
| A | Owner Name | 25 | Text | None | None | No |
| B | Owner Email | 30 | Text | Email validation | None | No |
| C | Owner Department | 20 | Text | None | None | No |
| D | Assets Owned - Count | 12 | Number | Integer ≥0 | None | No |
| E | Asset Categories | 30 | Text | None | None | No |
| F | Attestation Status | 20 | List | Dropdown | None | No |
| G | Attestation Method | 25 | List | Dropdown | None | No |
| H | Attestation Date | 15 | Date | Date validation | None | No |
| I | Days Since Request | 12 | Number | None | Formula | Yes |
| J | Reminder Count | 12 | Number | Integer ≥0 | None | No |
| K | Last Reminder Date | 15 | Date | Date validation | None | No |
| L | Escalation Required | 15 | List | Dropdown | None | No |
| M | Evidence Reference | 20 | Text | None | None | No |
| N | Notes | 30 | Text | None | None | No |

### Data Validation

**Column B: Owner Email - Email Validation**

```python
dv_email = DataValidation(
    type="custom",
    formula1='=AND(LEN(B3)>0,ISNUMBER(FIND("@",B3)))',
    allow_blank=True,
    showErrorMessage=True,
    errorTitle="Invalid Email",
    error="Please enter a valid email address"
)
dv_email.add('B3:B100')
ws.add_data_validation(dv_email)
```

**Column F: Attestation Status**

```python
attestation_statuses = [
    "✅ Signed",
    "📧 Sent, Pending",
    "❌ Not Sent",
    "🔴 Overdue"
]

dv_attestation = DataValidation(
    type="list",
    formula1=f'"{",".join(attestation_statuses)}"',
    allow_blank=False
)
dv_attestation.add('F3:F100')
ws.add_data_validation(dv_attestation)
```

**Column G: Attestation Method**

```python
attestation_methods = [
    "Email Confirmation",
    "E-Signature (DocuSign, etc.)",
    "Physical Signature",
    "Verbal (Meeting)",
    "Not Yet Attested"
]

dv_method = DataValidation(
    type="list",
    formula1=f'"{",".join(attestation_methods)}"',
    allow_blank=True
)
dv_method.add('G3:G100')
ws.add_data_validation(dv_method)
```

**Column L: Escalation Required**

```python
escalation_options = [
    "Yes",
    "No"
]

dv_escalation = DataValidation(
    type="list",
    formula1=f'"{",".join(escalation_options)}"',
    allow_blank=False
)
dv_escalation.add('L3:L100')
ws.add_data_validation(dv_escalation)
```

### Formulas

**Column I: Days Since Request**

```python
# Assuming attestation request sent on assessment start date (in Instructions sheet, or user-defined)
# For simplicity, calculate from today to attestation date (if signed) or today (if pending)

for row in range(3, 101):
    # If attestation signed, days from request to signature
    # If pending, days since request (ongoing)
    # This requires a "Request Date" - add hidden column or use fixed date
    # For sample: Days since today if not signed
    ws[f'I{row}'] = f'=IF(F{row}="✅ Signed",H{row}-$C$1,TODAY()-$C$1)'
    # Where C1 is "Assessment Start Date" in Instructions sheet
    ws[f'I{row}'].protection = Protection(locked=True)
```

**Simpler approach for template**:

```python
for row in range(3, 101):
    # Days since attestation (if signed) or blank
    ws[f'I{row}'] = f'=IF(H{row}<>"",TODAY()-H{row},"")'
    ws[f'I{row}'].protection = Protection(locked=True)
```

### Conditional Formatting

**Column F: Attestation Status - Color Coding**

```python
# Green: Signed
signed_rule = ContainsText(
    text='✅',
    fill=PatternFill(start_color='C6EFCE', fill_type='solid')
)
ws.conditional_formatting.add('F3:F100', signed_rule)

# Yellow: Pending
pending_rule = ContainsText(
    text='📧',
    fill=PatternFill(start_color='FFEB9C', fill_type='solid')
)
ws.conditional_formatting.add('F3:F100', pending_rule)

# Red: Overdue
overdue_rule = ContainsText(
    text='🔴',
    fill=PatternFill(start_color='FFC7CE', fill_type='solid')
)
ws.conditional_formatting.add('F3:F100', overdue_rule)
```

### Summary Section

**Location**: Rows 105-110

```python
# Acknowledgment Metrics
ws['A105'] = "Total Owners"
ws['B105'] = '=COUNTA(A3:A100)'

ws['A106'] = "Owners with Attestation"
ws['B106'] = '=COUNTIF(F3:F100,"✅ Signed")'

ws['A107'] = "Acknowledgment Rate %"
ws['B107'] = '=IFERROR(B106/B105*100,0)'
ws['B107'].number_format = '0.0"%"'
ws['B107'].font = Font(bold=True, size=12)

ws['A108'] = "Pending Attestations"
ws['B108'] = '=COUNTIF(F3:F100,"📧 Sent, Pending")'

ws['A109'] = "Overdue Attestations"
ws['B109'] = '=COUNTIF(F3:F100,"🔴 Overdue")'

ws['A110'] = "Not Yet Sent"
ws['B110'] = '=COUNTIF(F3:F100,"❌ Not Sent")'
```

---

## Sheet 4: Owner Awareness - Complete Specification

### Purpose

Verify owner training and understanding.

### Column Structure

**Total Columns: 14 (A through N)**

| Col | Header | Width | Type | Validation | Formula | Lock |
|-----|--------|-------|------|------------|---------|------|
| A | Owner Name | 25 | Text | None | None | No |
| B | Training Required | 15 | List | Dropdown | None | No |
| C | Training Completed | 15 | List | Dropdown | None | No |
| D | Training Date | 15 | Date | Date validation | None | No |
| E | Training Method | 25 | List | Dropdown | None | No |
| F | Training Score | 12 | Number | 0-100 or N/A | None | No |
| G | Awareness Verification | 25 | List | Dropdown | None | No |
| H | Verification Date | 15 | Date | Date validation | None | No |
| I | Understanding Level | 15 | List | Dropdown | None | No |
| J | Knowledge Gaps | 35 | Text | None | None | No |
| K | Remediation Plan | 40 | Text | None | None | No |
| L | Target Date | 15 | Date | Date validation | None | No |
| M | Evidence Reference | 20 | Text | None | None | No |
| N | Notes | 30 | Text | None | None | No |

### Data Validation

**Column B: Training Required**

```python
training_required = [
    "Yes",
    "No"
]

dv_training_req = DataValidation(
    type="list",
    formula1=f'"{",".join(training_required)}"',
    allow_blank=False
)
dv_training_req.add('B3:B100')
ws.add_data_validation(dv_training_req)
```

**Column C: Training Completed**

```python
training_completed = [
    "✅ Yes",
    "❌ No",
    "🕒 In Progress"
]

dv_training_comp = DataValidation(
    type="list",
    formula1=f'"{",".join(training_completed)}"',
    allow_blank=False
)
dv_training_comp.add('C3:C100')
ws.add_data_validation(dv_training_comp)
```

**Column E: Training Method**

```python
training_methods = [
    "E-Learning (LMS)",
    "Instructor-Led",
    "Self-Study",
    "Not Yet Trained"
]

dv_training_method = DataValidation(
    type="list",
    formula1=f'"{",".join(training_methods)}"',
    allow_blank=True
)
dv_training_method.add('E3:E100')
ws.add_data_validation(dv_training_method)
```

**Column G: Awareness Verification**

```python
verification_methods = [
    "Quiz",
    "Interview",
    "Document Review",
    "Attestation Only",
    "Not Assessed"
]

dv_verification = DataValidation(
    type="list",
    formula1=f'"{",".join(verification_methods)}"',
    allow_blank=False
)
dv_verification.add('G3:G100')
ws.add_data_validation(dv_verification)
```

**Column I: Understanding Level**

```python
understanding_levels = [
    "Excellent",
    "Good",
    "Fair",
    "Poor",
    "Not Assessed"
]

dv_understanding = DataValidation(
    type="list",
    formula1=f'"{",".join(understanding_levels)}"',
    allow_blank=False
)
dv_understanding.add('I3:I100')
ws.add_data_validation(dv_understanding)
```

### Conditional Formatting

**Column C: Training Completed - Color Coding**

```python
# Green: Yes
yes_rule = ContainsText(text='✅', fill=PatternFill(start_color='C6EFCE', fill_type='solid'))
ws.conditional_formatting.add('C3:C100', yes_rule)

# Red: No
no_rule = ContainsText(text='❌', fill=PatternFill(start_color='FFC7CE', fill_type='solid'))
ws.conditional_formatting.add('C3:C100', no_rule)

# Yellow: In Progress
progress_rule = ContainsText(text='🕒', fill=PatternFill(start_color='FFEB9C', fill_type='solid'))
ws.conditional_formatting.add('C3:C100', progress_rule)
```

**Column I: Understanding Level - Color Coding**

```python
# Green: Excellent/Good
excellent_rule = ContainsText(text='Excellent', fill=PatternFill(start_color='C6EFCE', fill_type='solid'))
ws.conditional_formatting.add('I3:I100', excellent_rule)

good_rule = ContainsText(text='Good', fill=PatternFill(start_color='C6EFCE', fill_type='solid'))
ws.conditional_formatting.add('I3:I100', good_rule)

# Yellow: Fair
fair_rule = ContainsText(text='Fair', fill=PatternFill(start_color='FFEB9C', fill_type='solid'))
ws.conditional_formatting.add('I3:I100', fair_rule)

# Red: Poor
poor_rule = ContainsText(text='Poor', fill=PatternFill(start_color='FFC7CE', fill_type='solid'))
ws.conditional_formatting.add('I3:I100', poor_rule)
```

### Summary Section

```python
# Awareness Metrics
ws['A105'] = "Total Owners Requiring Training"
ws['B105'] = '=COUNTIF(B3:B100,"Yes")'

ws['A106'] = "Owners with Training Complete"
ws['B106'] = '=COUNTIFS(B3:B100,"Yes",C3:C100,"✅ Yes")'

ws['A107'] = "Awareness Rate %"
ws['B107'] = '=IFERROR(B106/B105*100,0)'
ws['B107'].number_format = '0.0"%"'
ws['B107'].font = Font(bold=True, size=12)

ws['A108'] = "Owners with Good/Excellent Understanding"
ws['B108'] = '=COUNTIFS(I3:I100,"Excellent")+COUNTIFS(I3:I100,"Good")'
```

---

## Sheet 5: Owner Performance - Complete Specification

### Purpose

Measure owner engagement and performance.

### Column Structure

**Total Columns: 14 (A through N)**

| Col | Header | Width | Type | Validation | Formula | Lock |
|-----|--------|-------|------|------------|---------|------|
| A | Owner Name | 25 | Text | None | None | No |
| B | Assets Owned - Count | 12 | Number | Integer ≥0 | None | No |
| C | Critical/High Assets | 12 | Number | Integer ≥0 | None | No |
| D | Last Review Date - Avg | 15 | Date | Date | None | No |
| E | Days Since Avg Review | 12 | Number | None | Formula | Yes |
| F | Review Compliance % | 12 | Number | 0-100 | None | No |
| G | Update Responsiveness | 20 | List | Dropdown | None | No |
| H | Response Time - Avg (days) | 12 | Number | ≥0 | None | No |
| I | Engagement Score | 12 | Number | None | Formula | Yes |
| J | Performance Rating | 20 | Text | None | Formula | Yes |
| K | Assets at Risk | 12 | Number | Integer ≥0 | None | No |
| L | Action Required | 40 | Text | None | None | No |
| M | Evidence Reference | 20 | Text | None | None | No |
| N | Notes | 30 | Text | None | None | No |

### Data Validation

**Column G: Update Responsiveness**

```python
responsiveness_levels = [
    "Excellent",
    "Good",
    "Fair",
    "Poor"
]

dv_responsiveness = DataValidation(
    type="list",
    formula1=f'"{",".join(responsiveness_levels)}"',
    allow_blank=False
)
dv_responsiveness.add('G3:G100')
ws.add_data_validation(dv_responsiveness)
```

### Formulas

**Column E: Days Since Avg Review**

```python
for row in range(3, 101):
    ws[f'E{row}'] = f'=IF(D{row}<>"",TODAY()-D{row},"")'
    ws[f'E{row}'].protection = Protection(locked=True)
```

**Column I: Engagement Score**

```python
# Engagement = (Review Compliance × 60%) + (Responsiveness Score × 40%)
# Responsiveness Score: Excellent=100%, Good=80%, Fair=60%, Poor=20%

for row in range(3, 101):
    formula = (
        f'=F{row}*0.6+'
        f'IF(G{row}="Excellent",100,IF(G{row}="Good",80,IF(G{row}="Fair",60,20)))*0.4'
    )
    ws[f'I{row}'] = formula
    ws[f'I{row}'].number_format = '0.0"%"'
    ws[f'I{row}'].protection = Protection(locked=True)
```

**Column J: Performance Rating**

```python
for row in range(3, 101):
    formula = (
        f'=IF(I{row}>=90,"⭐ High Performer",'
        f'IF(I{row}>=70,"Meets Expectations",'
        f'IF(I{row}>=50,"⚠️ Needs Improvement",'
        f'"❌ Poor")))'
    )
    ws[f'J{row}'] = formula
    ws[f'J{row}'].alignment = Alignment(horizontal='center')
    ws[f'J{row}'].protection = Protection(locked=True)
```

### Conditional Formatting

**Column I: Engagement Score - Traffic Light**

```python
# Green: ≥ 90%
high_performer = CellIsRule(
    operator='greaterThanOrEqual',
    formula=['90'],
    fill=PatternFill(start_color='C6EFCE', fill_type='solid'),
    font=Font(color='006100', bold=True)
)
ws.conditional_formatting.add('I3:I100', high_performer)

# Yellow: 70-89%
meets_expectations = CellIsRule(
    operator='between',
    formula=['70', '89'],
    fill=PatternFill(start_color='FFEB9C', fill_type='solid'),
    font=Font(color='9C5700', bold=True)
)
ws.conditional_formatting.add('I3:I100', meets_expectations)

# Red: < 70%
poor_performer = CellIsRule(
    operator='lessThan',
    formula=['70'],
    fill=PatternFill(start_color='FFC7CE', fill_type='solid'),
    font=Font(color='9C0006', bold=True)
)
ws.conditional_formatting.add('I3:I100', poor_performer)
```

**Column J: Performance Rating - Color Coding**

Same emoji-based color coding as other sheets.

### Summary Section

```python
# Performance Metrics
ws['A105'] = "Total Owners"
ws['B105'] = '=COUNTA(A3:A100)'

ws['A106'] = "Average Engagement Score"
ws['B106'] = '=AVERAGE(I3:I100)'
ws['B106'].number_format = '0.0"%"'
ws['B106'].font = Font(bold=True, size=12)

ws['A107'] = "High Performers"
ws['B107'] = '=COUNTIF(J3:J100,"*High Performer*")'

ws['A108'] = "Needs Improvement"
ws['B108'] = '=COUNTIF(J3:J100,"*Needs Improvement*")'

ws['A109'] = "Poor Performers"
ws['B109'] = '=COUNTIF(J3:J100,"*Poor*")'
```

---

## Sheet 6: Accountability Metrics - Complete Specification

### Purpose

Aggregate accountability scores across 4 dimensions.

### Column Structure

**Total Columns: 10 (A through J)**

| Col | Header | Width | Type | Validation | Formula | Lock |
|-----|--------|-------|------|------------|---------|------|
| A | Accountability Dimension | 25 | Text | None | Fixed values | Yes |
| B | Weight | 10 | Number | None | Fixed values | Yes |
| C | Target Score | 10 | Number | None | Fixed values | Yes |
| D | Actual Score | 10 | Number | None | Formula | Yes |
| E | Gap vs. Target | 10 | Number | None | Formula | Yes |
| F | Compliance Status | 15 | Text | None | Formula | Yes |
| G | Trend vs. Last Quarter | 20 | List | Dropdown | None | No |
| H | Key Issues | 40 | Text | None | None | No |
| I | Remediation Actions | 40 | Text | None | None | No |
| J | Notes | 30 | Text | None | None | No |

### Pre-Populated Dimensions

```python
dimensions = [
    ("Coverage", 30, 100),
    ("Acknowledgment", 25, 95),
    ("Awareness", 20, 100),
    ("Performance", 25, 80)
]

# Populate columns A-C (rows 3-6)
for row_num, (dimension, weight, target) in enumerate(dimensions, start=3):
    ws[f'A{row_num}'] = dimension
    ws[f'B{row_num}'] = weight
    ws[f'C{row_num}'] = target
    ws[f'A{row_num}'].protection = Protection(locked=True)
    ws[f'B{row_num}'].protection = Protection(locked=True)
    ws[f'C{row_num}'].protection = Protection(locked=True)

# Format
for row in range(3, 7):
    ws[f'B{row}'].number_format = '0"%"'
    ws[f'C{row}'].number_format = '0"%"'
```

### Formulas

**Column D: Actual Score**

```python
# Row 3: Coverage (from Sheet 2)
ws['D3'] = "='Ownership Coverage'!B13"  # Overall Ownership Coverage %
ws['D3'].number_format = '0.0"%"'

# Row 4: Acknowledgment (from Sheet 3)
ws['D4'] = "='Owner Acknowledgment'!B107"  # Acknowledgment Rate %
ws['D4'].number_format = '0.0"%"'

# Row 5: Awareness (from Sheet 4)
ws['D5'] = "='Owner Awareness'!B107"  # Awareness Rate %
ws['D5'].number_format = '0.0"%"'

# Row 6: Performance (from Sheet 5)
ws['D6'] = "='Owner Performance'!B106"  # Average Engagement Score
ws['D6'].number_format = '0.0"%"'

# Lock all
for row in range(3, 7):
    ws[f'D{row}'].protection = Protection(locked=True)
```

**Column E: Gap vs. Target**

```python
for row in range(3, 7):
    ws[f'E{row}'] = f'=D{row}-C{row}'
    ws[f'E{row}'].number_format = '0.0"%"'
    ws[f'E{row}'].protection = Protection(locked=True)
```

**Column F: Compliance Status**

```python
for row in range(3, 7):
    formula = (
        f'=IF(D{row}>=C{row},"✅ Met",'
        f'IF(D{row}>=C{row}-10,"⚠️ At Risk",'
        f'"❌ Not Met"))'
    )
    ws[f'F{row}'] = formula
    ws[f'F{row}'].alignment = Alignment(horizontal='center')
    ws[f'F{row}'].protection = Protection(locked=True)
```

### Data Validation

**Column G: Trend**

```python
trends = [
    "Improved",
    "Stable",
    "Degraded",
    "N/A (first assessment)"
]

dv_trend = DataValidation(
    type="list",
    formula1=f'"{",".join(trends)}"',
    allow_blank=True
)
dv_trend.add('G3:G6')
ws.add_data_validation(dv_trend)
```

### Overall Accountability Score

**Location**: Rows 10-15

```python
# Overall Accountability Score (weighted average)
ws['A10'] = "Overall Accountability Score"
ws['A10'].font = Font(bold=True, size=14, color='003366')

ws['B10'] = '=(D3*B3/100)+(D4*B4/100)+(D5*B5/100)+(D6*B6/100)'
ws['B10'].number_format = '0.0"%"'
ws['B10'].font = Font(bold=True, size=14)
ws['B10'].fill = PatternFill(start_color='FFEB9C', fill_type='solid')

# Interpretation
ws['A12'] = "Score Interpretation:"
ws['B12'] = '=IF(B10>=95,"Excellent",IF(B10>=85,"Good",IF(B10>=75,"Fair","Poor")))'
ws['B12'].font = Font(bold=True, size=12)

# Target vs. Actual
ws['A13'] = "Target Overall Score"
ws['B13'] = "94%"  # Policy target
ws['B13'].font = Font(bold=True)

ws['A14'] = "Actual Overall Score"
ws['B14'] = '=B10'
ws['B14'].number_format = '0.0"%"'
ws['B14'].font = Font(bold=True)

ws['A15'] = "Gap vs. Target"
ws['B15'] = '=B14-VALUE(LEFT(B13,LEN(B13)-1))'
ws['B15'].number_format = '0.0"%"'
ws['B15'].font = Font(bold=True)
```

### Conditional Formatting

Same pattern as IMP-A.5.9-3 Quality Metrics (Green/Yellow/Red based on compliance status and overall score).

---

## Sheet 7: Evidence Register - Complete Specification

Same structure as previous assessments with adjusted Related Domain:

**Related Domain** dropdown:

- Ownership Coverage
- Owner Acknowledgment
- Owner Awareness
- Owner Performance
- Accountability Metrics
- All Domains


**Evidence ID format**: `ACCT-NNN`

---

## Python Script Template

```python
"""
SAMPLE SCRIPT - REQUIRES CUSTOMIZATION FOR CONTROL A.5.9-4

Owner Accountability Assessment Workbook Generator
ISO/IEC 27001:2022 Control A.5.9

This script generates the Excel workbook specified in ISMS-IMP-A.5.9.4.

IMPORTANT: This is a SAMPLE script. Customize for your organization:
1. Attestation workflow (adjust to your attestation process)
2. Training requirements (which owners require training)
3. Performance thresholds (adjust engagement score calculation)
4. Weighting of dimensions (adjust to your priorities)

DO NOT use this script without reviewing and adapting all sections marked
with "# CUSTOMIZE:" comments.

Author: ISMS Implementation Team
Date: [Date]
Version: 1.0
"""

import openpyxl
from openpyxl.styles import Font, PatternFill, Border, Side, Alignment, Protection
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import CellIsRule, ContainsText
from datetime import datetime
import os

# CUSTOMIZE: Configuration
CONFIG = {
    'output_dir': './output/',
    'workbook_name': f'ISMS_A_5_9_Owner_Accountability_Assessment_{datetime.now().strftime("%Y%m%d")}.xlsx',
    'author': '[Organization] ISMS Implementation Team',
    'company': '[Organization]',
    
    # Same color scheme as IMP-A.5.9-1/2/3
    'colors': {
        'header_bg': '003366',
        'header_text': 'FFFFFF',
        # ... (full color scheme)
    },
    
    'sheets': [
        'Instructions',
        'Ownership Coverage',
        'Owner Acknowledgment',
        'Owner Awareness',
        'Owner Performance',
        'Accountability Metrics',
        'Evidence Register'
    ]
}

# CUSTOMIZE: Accountability dimension weights (must sum to 100%)
ACCOUNTABILITY_WEIGHTS = {
    'Coverage': 30,
    'Acknowledgment': 25,
    'Awareness': 20,
    'Performance': 25
}

# CUSTOMIZE: Target scores
ACCOUNTABILITY_TARGETS = {
    'Coverage': 100,
    'Acknowledgment': 95,
    'Awareness': 100,
    'Performance': 80
}

def create_workbook():
    """Main function to create the assessment workbook"""
    
    print("=" * 60)
    print("ISMS A.5.9 Owner Accountability Assessment Generator")
    print("=" * 60)
    print()
    
    wb = openpyxl.Workbook()
    
    # Set properties
    wb.properties.title = "ISMS A.5.9 Owner Accountability Assessment"
    wb.properties.subject = "ISO/IEC 27001:2022 Control A.5.9 - Ownership Verification"
    wb.properties.creator = CONFIG['author']
    wb.properties.company = CONFIG['company']
    wb.properties.created = datetime.now()
    
    wb.remove(wb.active)
    
    # Create sheets
    print("Creating sheets...")
    for sheet_name in CONFIG['sheets']:
        wb.create_sheet(title=sheet_name)
        print(f"  ✓ {sheet_name}")
    
    print()
    print("Populating sheets...")
    
    create_instructions_sheet(wb['Instructions'])
    create_ownership_coverage_sheet(wb['Ownership Coverage'])
    create_acknowledgment_sheet(wb['Owner Acknowledgment'])
    create_awareness_sheet(wb['Owner Awareness'])
    create_performance_sheet(wb['Owner Performance'])
    create_accountability_metrics_sheet(wb['Accountability Metrics'])
    create_evidence_sheet(wb['Evidence Register'])
    
    # Save
    output_path = os.path.join(CONFIG['output_dir'], CONFIG['workbook_name'])
    os.makedirs(CONFIG['output_dir'], exist_ok=True)
    wb.save(output_path)
    
    print()
    print("=" * 60)
    print(f"✓ Workbook generated successfully!")
    print(f"  Location: {output_path}")
    print("=" * 60)
    
    return wb


# ... (sheet creation functions per specifications above)

if __name__ == '__main__':
    workbook = create_workbook()
```

---

## Integration with Dashboard

**CSV Export from Sheet 6 (Accountability Metrics)**:

Required columns:

- Accountability Dimension
- Actual Score
- Compliance Status
- Trend


**Export procedure**:
1. Select rows 3-6 in Accountability Metrics sheet
2. Export to CSV: `A59_4_Accountability_Metrics_YYYYMMDD.csv`
3. UTF-8 encoding
4. Include headers

**File format**:
```csv
Accountability Dimension,Actual Score,Compliance Status,Trend
Coverage,98%,⚠️ At Risk,Improved
Acknowledgment,89%,⚠️ At Risk,Stable
Awareness,85%,⚠️ At Risk,Improved
Performance,76%,⚠️ At Risk,Stable
Overall Accountability Score,88.1%,⚠️ At Risk,Improved
```

**Export filename**: `A59_4_Accountability_Metrics_YYYYMMDD.csv`

---

**END OF SPECIFICATION**

---

*"We are all agreed that your theory is crazy. The question which divides us is whether it is crazy enough."*
— Niels Bohr
*Where bamboo antennas actually work.* 🎋
