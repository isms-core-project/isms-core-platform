# ISMS-IMP-A.5.10-11.1 — Acceptable Use Policy Assessment

---

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.10-11.1 |
| **Title** | Acceptable Use Policy Assessment |
| **Control Reference** | ISO/IEC 27001:2022 A.5.10 |
| **Control Name** | Acceptable Use of Information and Other Associated Assets |
| **Document Type** | Implementation Guide |
| **Version** | 1.0 |
| **Last Updated** | [Date to be set] |
| **Owner** | Information Security Manager |
| **Classification** | Internal |

---

## PART I: USER COMPLETION GUIDE

### Assessment Overview

**Purpose**

This assessment workbook evaluates the completeness and effectiveness of your organisation's Acceptable Use Policy (AUP) framework. It verifies that rules for acceptable use of information and other associated assets are identified, documented, and implemented per ISO 27001:2022 Control A.5.10.

**Scope**

This assessment covers:
- AUP content completeness against ISO 27001 requirements
- Asset category coverage
- User awareness and acknowledgment tracking
- Policy communication effectiveness
- Gap identification and remediation planning

**What This Assessment Covers**

| Domain | Assessment Focus |
|--------|------------------|
| Policy Framework | AUP exists, approved, complete |
| Content Requirements | All required topics addressed |
| Asset Coverage | All asset categories included |
| User Awareness | Acknowledgment tracked and enforced |
| Communication | Dissemination effectiveness |

**Control Requirement**

ISO 27001:2022 A.5.10 states:

> "Rules for the acceptable use of information and other associated assets should be identified, documented and implemented."

The control ensures personnel understand their responsibilities when using organisational assets.

### Prerequisites

Before completing this assessment:

- [ ] Obtain current version of the Acceptable Use Policy
- [ ] Access to user acknowledgment records (LMS or HR system)
- [ ] List of all asset categories in scope
- [ ] Communication records for policy dissemination
- [ ] Access to ISMS Evidence Library for evidence storage

### Workbook Structure

| Sheet | Purpose | Key Actions |
|-------|---------|-------------|
| Instructions | Guidance and metadata | Complete document information |
| Policy_Assessment | AUP completeness evaluation | Assess each requirement |
| Asset_Coverage | Coverage by asset category | Verify all categories addressed |
| Awareness_Tracking | User acknowledgment tracking | Record acknowledgment status |
| Communication_Matrix | Dissemination assessment | Evaluate communication effectiveness |
| Evidence_Register | Audit evidence linking | Document evidence locations |
| Approval_SignOff | Assessment approval | Obtain required signatures |

### Completion Walkthrough

**Step 1: Document Information (Instructions Sheet)**

Complete all metadata fields:
- Assessment date
- Assessor name and role
- Organisation name
- Review period covered

**Step 2: Policy Assessment (Policy_Assessment Sheet)**

For each policy requirement:

1. **Addressed** - Select whether the requirement is addressed (Yes/Partial/No/N/A)
2. **Policy Section** - Reference the AUP section containing the requirement
3. **Clarity Rating** - Assess how clearly the requirement is stated
4. **Gap Status** - Identify any compliance gaps
5. **Remediation Notes** - Document required improvements

**Scoring Guidance**:

| Rating | Criteria |
|--------|----------|
| Yes | Fully addressed with clear, actionable language |
| Partial | Addressed but vague or incomplete |
| No | Not addressed in current policy |
| N/A | Not applicable to organisation |

**Step 3: Asset Coverage (Asset_Coverage Sheet)**

For each asset category:

1. Verify category is mentioned in AUP
2. Check usage rules are defined
3. Check handling requirements are documented
4. Note any gaps requiring remediation

**Step 4: Awareness Tracking (Awareness_Tracking Sheet)**

For each department:

1. Enter total user count
2. Enter acknowledged count
3. Formula calculates percentage
4. Document campaign method and dates
5. Track escalation status for non-compliance

**Target**: 100% acknowledgment within 30 days

**Step 5: Communication Matrix (Communication_Matrix Sheet)**

For each communication channel:

1. Record last communication date
2. Schedule next communication
3. Rate effectiveness based on feedback/metrics
4. Document improvement actions

**Step 6: Evidence Register (Evidence_Register Sheet)**

Link supporting evidence:

- Policy documents and approval records
- Acknowledgment exports
- Training completion records
- Communication distribution records

**Evidence Storage**: Store all evidence in ISMS Evidence Library with clear naming convention.

**Step 7: Approval Sign-Off (Approval_SignOff Sheet)**

1. Review summary metrics (auto-calculated)
2. Complete assessor information
3. Obtain Information Security Manager review
4. Obtain CISO approval

### Evidence Collection

**Required Evidence**:

| Evidence Type | Description | Storage Location |
|---------------|-------------|------------------|
| Policy Document | Current approved AUP | ISMS Evidence Library |
| Acknowledgment Records | LMS/HR export showing sign-offs | ISMS Evidence Library |
| Communication Records | Email distributions, intranet postings | ISMS Evidence Library |
| Training Records | AUP training completion | ISMS Evidence Library |
| Exception Register | Any approved exceptions | ISMS Evidence Library |

### Common Pitfalls

Avoid these frequent mistakes:

❌ **MISTAKE**: Assessing against an outdated version of the AUP
✅ **CORRECT**: Always verify you have the current approved version before assessment

❌ **MISTAKE**: Accepting "implied" coverage without explicit policy language
✅ **CORRECT**: Requirements should be explicitly stated, not assumed

❌ **MISTAKE**: Counting unsigned acknowledgments as complete
✅ **CORRECT**: Only count fully signed, dated acknowledgments

❌ **MISTAKE**: Not verifying acknowledgment dates are within required timeframe
✅ **CORRECT**: Check acknowledgments are current (within 12 months)

❌ **MISTAKE**: Marking coverage as "Yes" when only partially addressed
✅ **CORRECT**: Use "Partial" for incomplete coverage; "Yes" only for full coverage

❌ **MISTAKE**: Not documenting evidence locations
✅ **CORRECT**: Every claim should link to retrievable evidence

❌ **MISTAKE**: Skipping asset categories as "not applicable" without justification
✅ **CORRECT**: Document rationale for any N/A designations

❌ **MISTAKE**: Failing to track escalation status for non-compliant users
✅ **CORRECT**: Document escalation actions taken for acknowledgment non-compliance

### Quality Checklist

Before submitting the assessment:

- [ ] All metadata fields completed
- [ ] Every policy requirement assessed with valid status
- [ ] All asset categories evaluated
- [ ] Acknowledgment data is current (within 30 days)
- [ ] Communication effectiveness rated for all channels
- [ ] Evidence linked for all "Yes" ratings
- [ ] Gap notes documented for all "Partial" or "No" ratings
- [ ] Summary metrics reviewed for accuracy
- [ ] Assessor section completed and signed
- [ ] Review signatures obtained

### Review & Approval

**Review Workflow**:

1. Assessor completes all sheets
2. Information Security Manager reviews for accuracy
3. CISO approves final assessment
4. Assessment archived in ISMS Evidence Library

**Approval Authority**:

| Role | Responsibility |
|------|---------------|
| Assessor | Complete assessment accurately |
| ISM | Verify assessment quality and completeness |
| CISO | Final approval; escalate critical gaps |

---

## PART II: TECHNICAL SPECIFICATION

### Workbook Architecture

**File Details**:

- Filename: `ISMS-IMP-A.5.10-11.1_Acceptable_Use_Policy_Assessment_YYYYMMDD.xlsx`
- Format: Microsoft Excel (.xlsx)
- Sheets: 7

### Sheet Specifications

#### Instructions Sheet

| Row | Column A | Column B |
|-----|----------|----------|
| 1 | Header (merged A:G) | Document title and control reference |
| 3 | "Document Information" | Section header |
| 4-11 | Metadata labels | Input fields |

**Styling**:
- Header: Navy (#003366), white text, 14pt bold
- Labels: Bold
- Input cells: Yellow fill (#FFFFCC)

#### Policy_Assessment Sheet

**Columns**:

| Column | Header | Width | Content |
|--------|--------|-------|---------|
| A | Requirement_ID | 15 | Auto-generated (REQ-001, etc.) |
| B | Policy_Requirement | 45 | Pre-populated requirements |
| C | Category | 20 | Requirement category |
| D | Addressed | 14 | Data validation: Yes/Partial/No/N/A |
| E | Policy_Section | 20 | User input |
| F | Clarity_Rating | 16 | Data validation: Clear/Needs Improvement/Unclear |
| G | Last_Updated | 16 | Date field |
| H | Owner | 22 | User input |
| I | Gap_Status | 16 | Data validation |
| J | Remediation_Notes | 35 | User input |
| K | Evidence_Ref | 18 | Evidence reference |

**Pre-populated Requirements**:

1. Policy scope defines applicable assets
2. Policy defines acceptable business use
3. Policy explicitly prohibits unauthorized activities
4. Personal use guidelines are documented
5. Monitoring and logging disclosure included
6. Consequences of violation are stated
7. Exception request process documented
8. Intellectual property rules defined
9. Data classification handling requirements
10. Mobile device acceptable use rules
11. Remote working asset use guidelines
12. Cloud service usage rules
13. Social media usage guidelines
14. Email and messaging acceptable use
15. Internet usage guidelines
16. Password and authentication requirements
17. Physical asset protection responsibilities
18. Incident reporting obligations
19. Third-party access provisions
20. Policy acknowledgment requirement

#### Asset_Coverage Sheet

**Columns**:

| Column | Header | Width | Content |
|--------|--------|-------|---------|
| A | Asset_Category | 25 | Pre-populated categories |
| B | Asset_Examples | 40 | Example assets |
| C | Covered_In_AUP | 16 | Data validation: Yes/Partial/No |
| D | Policy_Section | 20 | User input |
| E | Usage_Rules_Defined | 18 | Data validation: Yes/No/N/A |
| F | Handling_Rules_Defined | 18 | Data validation: Yes/No/N/A |
| G | Gap_Notes | 35 | User input |
| H | Remediation_Required | 18 | Data validation: Yes/No |
| I | Evidence_Ref | 18 | Evidence reference |

**Pre-populated Categories**:
- Information Assets
- Software Assets
- Hardware Assets
- Network Assets
- Cloud Services
- Communication Tools
- Physical Media
- Authentication Assets
- Development Environments
- Monitoring Systems
- Personal Devices (BYOD)
- IoT Devices

#### Awareness_Tracking Sheet

**Columns**:

| Column | Header | Width | Formula |
|--------|--------|-------|---------|
| A | Department | 22 | Pre-populated departments |
| B | Total_Users | 14 | User input |
| C | Acknowledged | 14 | User input |
| D | Pending | 14 | =B-C (formula) |
| E | Acknowledgment_% | 16 | =C/B*100 (formula) |
| F | Last_Campaign_Date | 18 | Date field |
| G | Next_Due_Date | 16 | User input |
| H | Campaign_Method | 22 | Data validation |
| I | Escalation_Status | 18 | Data validation |
| J | Notes | 35 | User input |

**Summary Row**: TOTAL row with SUM formulas

#### Communication_Matrix Sheet

**Columns**:

| Column | Header | Width | Content |
|--------|--------|-------|---------|
| A | Communication_Channel | 28 | Pre-populated channels |
| B | Audience | 25 | Target audience |
| C | Frequency | 18 | Data validation |
| D | Last_Communication | 18 | Date field |
| E | Next_Scheduled | 18 | Date field |
| F | Effectiveness_Rating | 18 | Data validation |
| G | Owner | 22 | User input |
| H | Improvement_Actions | 35 | User input |
| I | Evidence_Ref | 18 | Evidence reference |

#### Evidence_Register Sheet

**Columns**:

| Column | Header | Width | Content |
|--------|--------|-------|---------|
| A | Evidence_ID | 15 | Auto-generated (EV-001, etc.) |
| B | Evidence_Type | 22 | Data validation |
| C | Description | 45 | User input |
| D | Related_Requirement | 25 | User input |
| E | Collection_Date | 16 | Date field |
| F | Location | 40 | User input (URL or path) |
| G | Collected_By | 25 | User input |
| H | Valid_Until | 16 | Date field |

#### Approval_SignOff Sheet

**Structure**:
- Summary metrics (auto-calculated from other sheets)
- Assessor completion section
- Information Security Manager review section
- CISO approval section

**Summary Formulas**:
- Total Requirements Assessed: `=COUNTA(Policy_Assessment!A4:A33)-COUNTBLANK(Policy_Assessment!B4:B33)`
- Requirements Addressed: `=COUNTIF(Policy_Assessment!D4:D33,"Yes")`
- Gaps Identified: `=COUNTIF(Policy_Assessment!D4:D33,"No")`
- Acknowledgment %: Reference to Awareness_Tracking total row

### Data Validations

| Field | Validation List |
|-------|-----------------|
| Addressed | Yes, Partial, No, N/A |
| Clarity_Rating | Clear, Needs Improvement, Unclear |
| Gap_Status | Compliant, Gap Identified, Remediation In Progress |
| Covered_In_AUP | Yes, Partial, No |
| Usage/Handling Defined | Yes, No, N/A |
| Campaign_Method | Email, LMS, Intranet, In-Person, Onboarding |
| Escalation_Status | None Required, Reminder Sent, Manager Notified, HR Escalation |
| Frequency | Daily, Weekly, Monthly, Quarterly, Annual, Per hire, As needed, Always available |
| Effectiveness_Rating | Highly Effective, Effective, Needs Improvement, Ineffective |
| Evidence_Type | Policy Document, Acknowledgment Record, Training Record, Screenshot, Export, Attestation, Email, Meeting Minutes |
| Approval_Decision | Approved, Approved with conditions, Rejected |

### Generator Reference

**Script**: `generate_a510_11_1_acceptable_use_policy.py`

**Location**: `10-isms-scr-base/isms-a.5.10-11-asset-usage-lifecycle/10_generator-master/`

**Execution**:
```bash
python3 generate_a510_11_1_acceptable_use_policy.py
```

**Output**: Excel workbook in current directory

---

**END OF SPECIFICATION**

---

*"Security is not a product, but a process."*
— Bruce Schneier

<!-- QA_VERIFIED: 2026-02-01 -->
