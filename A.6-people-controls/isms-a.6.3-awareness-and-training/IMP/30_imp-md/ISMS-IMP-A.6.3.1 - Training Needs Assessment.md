**ISMS-IMP-A.6.3.1 - Training Needs Assessment**
**Assessment Specification with User Completion Guide**
### ISO/IEC 27001:2022 Control A.6.3: Information Security Awareness, Education and Training

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.6.3.1 |
| **Version** | 1.0 |
| **Assessment Area** | Training Needs Analysis and Audience Classification |
| **Related Policy** | ISMS-POL-A.6.3, Section 2.2 (Training Audience Classification) |
| **Purpose** | Assess training needs by role classification, identify training gaps, and determine appropriate training requirements for all personnel |
| **Target Audience** | HR Training Coordinators, Information Security Officers, Department Managers, Compliance Officers, Auditors |
| **Assessment Type** | Process & Organizational Assessment |
| **Review Cycle** | Annual (minimum) + upon significant organizational changes |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | Initial | Initial specification for Training Needs Assessment workbook | ISMS Implementation Team |

---

# PART I: USER COMPLETION GUIDE
**Audience:** HR Training Coordinators, Department Managers, Information Security Officers

---

# Assessment Overview

## What This Assessment Measures

This assessment evaluates [Organization]'s training needs to ensure all personnel receive appropriate information security awareness, education, and training in compliance with ISO/IEC 27001:2022 Control A.6.3 and related regulatory requirements.

**Scope:** 4 assessment domains covering complete training needs analysis:
1. **Role Inventory** - Complete inventory of roles requiring security training
2. **Training Audience Classification** - Categorization of roles into training tiers (Tier 1-7)
3. **Training Requirement Mapping** - Requirements mapped to each role/tier
4. **Gap Analysis** - Current state vs. required training identification

**Assessment Output:** Excel workbook with sheets documenting:

- Complete role inventory with classifications
- Training tier assignments with justification
- Training requirement mapping by tier
- Gap analysis showing training deficits
- Prioritized remediation plan
- Evidence register for audit trail
- Approval sign-off workflow

## Why This Matters

**ISO 27001:2022 Control A.6.3 Requirement:**
> *"Personnel of the organisation and relevant interested parties should receive appropriate information security awareness, education and training and regular updates of the organisation's information security policy, topic-specific policies and procedures, as relevant for their job function."*

**ISO 27001:2022 Clause 7.2 - Competence:**
> The organization shall determine the necessary competence of person(s) doing work under its control that affects its information security performance.

**Regulatory Context:**

- **Swiss nDSG (Art. 8):** Requires appropriate organizational measures including staff competency
- **EU GDPR (Art. 29, 32):** Personnel processing personal data must act under appropriate instruction/training
- **NIS2 Directive:** Cybersecurity practices must include staff training (Art. 21)
- **DORA (Financial Services):** Digital operational resilience training required (Art. 13)
- **PCI DSS v4.0 (Req. 12.6):** Security awareness program for all personnel

**Business Impact:**

- **Regulatory Compliance:** Training requirements are audited in virtually all compliance frameworks
- **Human Factor Risk:** ~80% of security incidents involve human factors; training reduces this
- **Audit Readiness:** Documented training needs analysis demonstrates systematic approach
- **Resource Optimization:** Targeted training based on role reduces unnecessary training burden
- **Incident Reduction:** Role-appropriate training addresses actual risk exposures

## Who Should Complete This Assessment

**Primary Responsibility:** HR Training Coordinator (or equivalent)

**Required Stakeholders:**

1. **HR Training Coordinator** - Primary owner, maintains assessment
   - Maintains role inventory
   - Coordinates with department managers on classifications
   - Documents training requirements and gaps

2. **Information Security Officer** - Security expertise
   - Defines training tier criteria
   - Validates classification decisions
   - Identifies security-relevant requirements
   - Approves final classifications

3. **Department Managers** - Operational knowledge
   - Provide role descriptions and responsibilities
   - Confirm data/system access levels
   - Validate training audience assignments
   - Identify role-specific training needs

4. **HR Business Partners** - HR perspective
   - Provide organization structure information
   - Clarify employment types and relationships
   - Support onboarding/role change integration

**Support Roles:**

- **IT/System Administrators:** Confirm technical access levels
- **Data Protection Officer:** Privacy-specific training needs
- **Compliance Officer:** Regulatory training requirements

**Required Skills:**

- Understanding of organizational structure and roles
- Familiarity with ISMS-POL-A.6.3 training requirements
- Access to role descriptions and job specifications
- Knowledge of system/data access patterns
- Basic risk assessment understanding

## Time Estimate

**Initial Assessment:** 16-24 hours (first-time completion)

| Activity | Time Estimate |
|----------|---------------|
| Role inventory compilation | 4-6 hours |
| Stakeholder consultation | 4-6 hours |
| Training tier classification | 3-4 hours |
| Requirement mapping | 2-3 hours |
| Gap analysis | 2-3 hours |
| Documentation and sign-off | 2-4 hours |

**Annual Review:** 6-10 hours (incremental updates)

**Pro Tips:**

- **Start with existing data:** Use HR systems, org charts, job descriptions
- **Classify by role, not individual:** Reduces complexity and maintenance
- **Leverage system access data:** IT can provide access level reports
- **Prioritize high-risk roles first:** Privileged users, data handlers
- **Align with HR processes:** Integrate with job family/grade structures

## Connection to Policy

This assessment implements **ISMS-POL-A.6.3, Section 2.2 (Training Audience Classification)** which defines:

**Training Audience Tiers:**
- **Tier 1:** All Personnel - Baseline security awareness
- **Tier 2:** Standard Users - Application security, data handling
- **Tier 3:** Data Handlers - Data protection, privacy, classification
- **Tier 4:** Technical Staff - Secure development, system security
- **Tier 5:** Privileged Users - Privileged access, incident response
- **Tier 6:** Security Roles - Specialized security training
- **Tier 7:** Management - Governance, risk, compliance

**Classification Criteria (POL-A.6.3, Section 2.2):**
- System Access Level
- Data Handling (classification levels)
- Role Function
- External Exposure
- Technical Depth
- Regulatory Scope

**Policy Authority:** Chief Information Security Officer (CISO)
**Compliance Status:** Mandatory annual assessment

---

# Prerequisites

## Access Required

Before starting this assessment, ensure you have access to:

**Organizational Information:**
- [ ] Complete organization chart with all departments
- [ ] Role/job descriptions for all positions
- [ ] Employment type classifications (permanent, contractor, temp)
- [ ] Third-party personnel inventory (contractors with system access)

**System and Data Access Information:**
- [ ] User access reports (systems each role accesses)
- [ ] Privileged account list (admin, elevated access)
- [ ] Data classification mapping (who handles what data levels)
- [ ] Application access matrix

**Policy Documents:**
- [ ] ISMS-POL-A.6.3 (Information Security Awareness and Training)
- [ ] ISMS-POL-A.5.15-16-18 (Identity Access Management) - for access levels
- [ ] Data Classification Policy - for data handling roles
- [ ] Current training curriculum - to identify gaps

**HR Systems:**
- [ ] Access to HR information system for role data
- [ ] Current training completion records
- [ ] Job grade/family structures (if applicable)

## Knowledge Required

**Essential Understanding:**

1. **Organizational Structure:**
   - Department and team organization
   - Reporting relationships
   - Role responsibilities and scopes

2. **ISMS-POL-A.6.3 Training Tier Definitions:**
   - Tier criteria and requirements
   - Training topics by tier
   - Frequency requirements

3. **Access and Data Handling:**
   - System access levels (standard, elevated, privileged)
   - Data classification scheme
   - Which roles handle sensitive data

4. **Regulatory Requirements:**
   - Industry-specific training requirements
   - Compliance-mandated training (PCI, HIPAA, etc.)

---

# Workbook Structure Overview

## Sheet 1: Instructions
- Assessment overview and completion guidance
- Definitions and terminology
- Completion workflow

## Sheet 2: Role_Inventory
**Purpose:** Complete inventory of all roles requiring security training

**Columns:**
- Role ID (unique identifier)
- Role Title
- Department
- Employment Type (Employee/Contractor/Temp/Third-Party)
- Number of Personnel (in this role)
- Brief Description
- Primary System Access
- Highest Data Classification Handled
- External-Facing (Yes/No)
- Technical Role (Yes/No)
- Management Role (Yes/No)

## Sheet 3: Tier_Classification
**Purpose:** Assign training tiers to each role

**Columns:**
- Role ID (from Role_Inventory)
- Role Title
- System Access Score (1-5)
- Data Handling Score (1-5)
- Technical Depth Score (1-5)
- External Exposure Score (1-5)
- Regulatory Scope Score (1-5)
- Total Score
- Assigned Tier (1-7)
- Classification Justification
- Approved By
- Approval Date

**Scoring Guide:**
- 1 = Minimal/None
- 2 = Low
- 3 = Moderate
- 4 = High
- 5 = Very High/Critical

**Tier Assignment Matrix:**
| Total Score | Assigned Tier |
|-------------|---------------|
| 5-7 | Tier 1 (All Personnel) |
| 8-11 | Tier 2 (Standard Users) |
| 12-15 | Tier 3 (Data Handlers) |
| 16-19 | Tier 4 (Technical Staff) |
| 20-22 | Tier 5 (Privileged Users) |
| 23-25 | Tier 6 (Security Roles) |
| Management=Yes + Score≥12 | Tier 7 (Management) |

## Sheet 4: Training_Requirements
**Purpose:** Map required training to each tier

**Columns:**
- Tier
- Training Topic
- Mandatory (Y/N)
- Frequency
- Delivery Method Requirement
- Assessment Required (Y/N)
- Regulatory Driver
- Related Policy Reference

**Pre-Populated with POL-A.6.3 requirements by tier**

## Sheet 5: Gap_Analysis
**Purpose:** Compare current training state to requirements

**Columns:**
- Role ID
- Role Title
- Assigned Tier
- Required Training Topic
- Current Status (Completed/Partial/Not Started/Not Available)
- Gap Description
- Priority (Critical/High/Medium/Low)
- Remediation Action
- Target Date
- Owner

## Sheet 6: Evidence_Register
**Purpose:** Document evidence supporting assessment

**Columns:**
- Evidence ID
- Category
- Description
- Source Document/System
- Date Obtained
- Location/Reference
- Notes

## Sheet 7: Dashboard
**Purpose:** Summary metrics and compliance status

**Metrics:**
- Total Roles Assessed
- Roles by Tier (distribution)
- Personnel by Tier (headcount)
- Gap Count by Priority
- Training Coverage Status
- Compliance Score

## Sheet 8: Approval_Sign_Off
**Purpose:** Formal approval workflow

**Approvers:**
- Assessor
- HR Director
- Information Security Officer
- CISO (final approval)

---

# Completion Walkthrough

## Step 1: Build Role Inventory (Sheet 2)

**Objective:** Create complete inventory of all roles requiring security training.

**Process:**

1. **Export organizational data:**
   - Pull role/job title list from HR system
   - Include all employment types (employees, contractors, temps)
   - Add third-party personnel with system access

2. **For each role, document:**
   - Role ID: Create unique identifier (e.g., "FIN-001", "IT-005")
   - Role Title: Official job title
   - Department: Department/team affiliation
   - Employment Type: Employee/Contractor/Temp/Third-Party
   - Number of Personnel: Current headcount in this role
   - Brief Description: 1-2 sentence role summary
   - Primary System Access: Main systems this role uses
   - Highest Data Classification: Public/Internal/Confidential/Restricted
   - External-Facing: Does role interact with external parties?
   - Technical Role: Is this an IT/Development/Engineering role?
   - Management Role: Is this a people manager/executive role?

3. **Verification:**
   - Cross-reference with department managers
   - Ensure all departments are represented
   - Include remote workers and international roles

**Example Entries:**

| Role ID | Role Title | Dept | Type | Count | Data Class | External | Technical | Mgmt |
|---------|-----------|------|------|-------|------------|----------|-----------|------|
| FIN-001 | Financial Analyst | Finance | Employee | 8 | Confidential | No | No | No |
| IT-003 | System Administrator | IT Ops | Employee | 3 | Restricted | No | Yes | No |
| HR-002 | HR Business Partner | HR | Employee | 4 | Restricted | No | No | No |
| EXT-001 | IT Contractor | IT | Contractor | 5 | Confidential | No | Yes | No |
| EXEC-001 | Department Director | Various | Employee | 6 | Confidential | Yes | No | Yes |

## Step 2: Classify Training Tiers (Sheet 3)

**Objective:** Assign appropriate training tier to each role based on scoring criteria.

**Process:**

1. **For each role from Sheet 2, score each criterion (1-5):**

   **System Access Score:**
   - 1: No system access (physical-only roles)
   - 2: Basic read-only access to limited systems
   - 3: Standard business application access
   - 4: Elevated access (sensitive systems, multiple environments)
   - 5: Privileged/Administrative access

   **Data Handling Score:**
   - 1: Public data only
   - 2: Internal data
   - 3: Confidential data occasionally
   - 4: Confidential data regularly
   - 5: Restricted data or high-volume sensitive data

   **Technical Depth Score:**
   - 1: No technical requirements
   - 2: Basic IT literacy
   - 3: Power user/advanced applications
   - 4: Technical role (IT support, development)
   - 5: Security/infrastructure specialist

   **External Exposure Score:**
   - 1: Internal-only role
   - 2: Occasional external contact
   - 3: Regular external contact (customers, vendors)
   - 4: Primary external interface role
   - 5: High-profile external role (executive, spokesperson)

   **Regulatory Scope Score:**
   - 1: No specific regulatory requirements
   - 2: General compliance awareness
   - 3: Role-specific compliance (one framework)
   - 4: Multi-regulation compliance role
   - 5: Compliance/audit-focused role

2. **Calculate total score and assign tier per matrix**

3. **Document justification for each assignment**

4. **Special considerations:**
   - Management roles: Assign Tier 7 if Total Score ≥12
   - Security roles: Always Tier 6 regardless of score
   - Override with justification if scoring doesn't fit

## Step 3: Map Training Requirements (Sheet 4)

**Objective:** Document required training for each tier.

**This sheet is pre-populated based on POL-A.6.3 Section 2.3-2.4.**

**Review and customize:**

1. **Verify pre-populated requirements align with current policy**

2. **Add organization-specific training:**
   - Industry-specific security topics
   - Regulatory training (PCI, HIPAA, GDPR as applicable)
   - Organization-specific systems/procedures

3. **Document delivery method requirements:**
   - Some regulations mandate specific methods (e.g., annual classroom for PCI)
   - Note where flexibility exists

4. **Identify regulatory drivers:**
   - Link each requirement to driving regulation/policy
   - Helps prioritization and audit response

## Step 4: Perform Gap Analysis (Sheet 5)

**Objective:** Identify gaps between current training state and requirements.

**Process:**

1. **For each role-tier combination:**
   - List all required training topics (from Sheet 4)
   - Check current training records for completion status
   - Document gaps

2. **Status Categories:**
   - **Completed:** Training completed and current
   - **Partial:** Some training done, not complete
   - **Not Started:** Required training not begun
   - **Not Available:** Training content doesn't exist yet

3. **Priority Assignment:**
   - **Critical:** Regulatory requirement, no compliance
   - **High:** Core security training, significant gap
   - **Medium:** Role-specific training, moderate risk
   - **Low:** Supplemental training, lower urgency

4. **Remediation Planning:**
   - Specific action to close gap
   - Target date (realistic)
   - Owner (who will ensure completion)

## Step 5: Complete Evidence Register (Sheet 6)

**Objective:** Document all evidence supporting the assessment.

**Required Evidence:**

| Category | Evidence Examples |
|----------|-------------------|
| Organizational | Org charts, role descriptions, employment data |
| System Access | Access reports, privilege lists, application matrices |
| Training Records | LMS reports, completion certificates, attendance records |
| Policy | POL-A.6.3, related policies referenced |
| Approvals | Email approvals, meeting minutes, sign-off records |

## Step 6: Review Dashboard and Obtain Approvals (Sheets 7-8)

**Objective:** Verify metrics, gain formal approval.

1. **Review Dashboard metrics:**
   - Verify calculations are correct
   - Identify any concerning patterns
   - Prepare summary for approvers

2. **Approval Workflow:**
   - Assessor self-review and sign
   - HR Director review (organizational accuracy)
   - Information Security Officer (classification accuracy)
   - CISO final approval

---

# Evidence Collection

## General Evidence Guidelines

**Purpose:** Evidence substantiates assessment findings and provides audit trail.

**Evidence Quality Criteria:**
- **Current:** Dated within assessment period (typically last 12 months)
- **Complete:** Covers all assessed roles and classifications
- **Verifiable:** Can be independently validated
- **Consistent:** Aligns with assessment findings

**Storage Location:** ISMS Evidence Library / A.6.3 Training / Assessments / [Year] / Needs_Assessment /

## Evidence Types by Assessment Area

### Role Inventory Evidence

| Evidence Type | Description | Source | Format |
|---------------|-------------|--------|--------|
| Organization Chart | Current org structure | HR System | PDF/PNG export |
| Role Catalog | Complete job descriptions | HR System | Excel/PDF |
| Headcount Report | Personnel count by role | HR System | Excel export |
| Contractor Register | Third-party personnel list | Vendor Management | Excel |
| Access Matrix | System access by role | IT/IAM | Excel export |

**Collection Tools:**
```
HR System Exports:
- Workday: Reports > Custom > Export Role Catalog
- SAP SuccessFactors: Admin Center > Position Management > Export
- BambooHR: Reports > Employee Directory > Export CSV

Access Management:
- Active Directory: Get-ADGroupMember for group membership reports
- Azure AD: Export user access from Enterprise Applications
- IAM platforms: Role-based access reports
```

### Tier Classification Evidence

| Evidence Type | Description | Source | Format |
|---------------|-------------|--------|--------|
| Scoring Worksheets | Individual role scores | Assessment | Excel (this workbook) |
| Classification Decisions | Justification records | Meetings | Meeting minutes |
| Override Approvals | Non-standard tier assignments | Email/Tickets | PDF/Screenshot |
| Policy Reference | Tier criteria from POL-A.6.3 | ISMS | PDF |

### Training Requirements Evidence

| Evidence Type | Description | Source | Format |
|---------------|-------------|--------|--------|
| Policy Extract | Training requirements from POL-A.6.3 | ISMS | PDF |
| Regulatory Mapping | Training requirements by regulation | Compliance | Excel |
| LMS Curriculum | Current available training | LMS | Export/Screenshot |
| Training Calendar | Scheduled training sessions | HR/LMS | Calendar export |

### Gap Analysis Evidence

| Evidence Type | Description | Source | Format |
|---------------|-------------|--------|--------|
| Training Completion Reports | Current completion by employee | LMS | Excel export |
| Compliance Reports | Training compliance status | LMS | PDF/Excel |
| Exception Requests | Approved training deferrals | ServiceNow/Email | PDF |
| Remediation Plans | Documented improvement actions | Project Tool | Export |

## Evidence Sanitization

**Before storing evidence, remove:**
- Personal identifiable information (unless required for audit)
- Social security numbers, national IDs
- Personal contact information
- Salary/compensation data (not relevant to security training)

**Retain:**
- Employee IDs (anonymized if possible)
- Role classifications
- Department affiliations
- Training completion status

---

# Common Pitfalls

## ❌ MISTAKE #1: Using Job Titles Instead of Roles

**The Problem:** Classifying by job title (e.g., "Senior Analyst" vs "Analyst") instead of functional role creates inconsistent training requirements for people doing the same work.

**Why It Matters:** Job titles vary across departments and are often based on experience/compensation rather than function. Security training needs are driven by what people DO, not their title.

**The Fix:**
- Group by functional role (what they do)
- Use job title as reference only
- Document role-to-title mapping

**Example:**
```
Wrong: "Senior Financial Analyst" → Tier 4, "Financial Analyst" → Tier 2
Right: "Financial Analysis Role" → Tier 3 (both titles, same training needs)
```

## ❌ MISTAKE #2: Ignoring Contractors and Third Parties

**The Problem:** Assessment covers only employees, missing contractors, consultants, and third-party personnel who access systems.

**Why It Matters:** Third parties often have the same or greater access than employees but receive less training oversight. They're frequently involved in security incidents.

**The Fix:**
- Include ALL personnel with system access
- Document employment type for each role
- Ensure contractor agreements include training requirements
- Track third-party training completion separately

## ❌ MISTAKE #3: Over-Classifying to "Be Safe"

**The Problem:** Assigning higher tiers than warranted to "err on the side of caution" creates training burden and reduces effectiveness.

**Why It Matters:** Training overload causes fatigue and reduces engagement. Resources are wasted on unnecessary training. People ignore training that isn't relevant to their work.

**The Fix:**
- Score objectively using criteria
- Justify all tier assignments
- Review with department managers for reality check
- Accept that some roles genuinely need minimal training

## ❌ MISTAKE #4: Static Assessment (One and Done)

**The Problem:** Completing assessment once and not updating when organization changes.

**Why It Matters:** Role changes, new hires, reorganizations, and new systems all affect training needs. Stale assessments lead to compliance gaps and untrained personnel.

**The Fix:**
- Review quarterly (minimum annually)
- Trigger reassessment on:
  - New roles created
  - Significant headcount changes (>20%)
  - New systems/data types introduced
  - Organizational restructuring
  - Regulatory changes

## ❌ MISTAKE #5: No Gap Remediation Ownership

**The Problem:** Identifying gaps without assigning owners or realistic timelines.

**Why It Matters:** Gaps without ownership don't get closed. Assessment becomes documentation exercise with no improvement.

**The Fix:**
- Every gap needs: Owner + Target Date + Specific Action
- Escalate gaps without resolution plan
- Track remediation in regular meetings
- Report overdue remediation to CISO

## ❌ MISTAKE #6: Confusing Training Availability with Completion

**The Problem:** Marking training as "available" when requirement is "completed."

**Why It Matters:** Training content existing doesn't mean people have taken it. Compliance requires actual completion, not just availability.

**The Fix:**
- Status categories:
  - Available = content exists
  - Assigned = enrolled/scheduled
  - Completed = finished with passing score
  - Current = completed within validity period
- Track completion status, not availability

## ❌ MISTAKE #7: Ignoring Management Tier Requirements

**The Problem:** Classifying managers based only on their technical scores, missing governance responsibilities.

**Why It Matters:** Managers have security governance responsibilities beyond their technical role. They approve access, handle incidents, and set culture.

**The Fix:**
- Management roles ALWAYS consider Tier 7
- Apply rule: Management=Yes AND Score≥12 → Tier 7
- Include governance, risk, and compliance topics for all managers
- Document management-specific training requirements

## ❌ MISTAKE #8: Incomplete Evidence Trail

**The Problem:** Assessment completed but evidence not collected or stored properly.

**Why It Matters:** Auditors require evidence. Without it, assessment findings cannot be verified. Compliance status is unsubstantiated.

**The Fix:**
- Collect evidence AS you assess (not after)
- Store in designated ISMS evidence location
- Cross-reference evidence in assessment workbook
- Verify evidence accessibility before sign-off

## ❌ MISTAKE #9: No Baseline for Comparison

**The Problem:** First assessment establishes no baseline; subsequent assessments can't show improvement.

**Why It Matters:** Continuous improvement requires measuring progress. Without baseline, you can't demonstrate training program effectiveness.

**The Fix:**
- Snapshot metrics at each assessment
- Track over time:
  - Roles assessed
  - Gap count and severity
  - Time to close gaps
  - Coverage percentage
- Include trend analysis in dashboard

## ❌ MISTAKE #10: Assessment in Isolation

**The Problem:** Training needs assessment not integrated with other ISMS processes.

**Why It Matters:** Training needs connect to access management, incident response, and overall risk posture. Isolated assessments miss important context.

**The Fix:**
- Cross-reference with:
  - Access reviews (A.5.15-18) - are training levels aligned with access levels?
  - Incident reports (A.5.24-28) - do incidents indicate training gaps?
  - Risk assessments (A.5.7) - are high-risk roles getting appropriate training?
- Coordinate with IAM and Security Operations teams

---

# Quality Checklist

## Completeness Checks

Before submitting for review, verify:

**Role Inventory:**
- [ ] ALL departments represented in role inventory
- [ ] ALL employment types included (employee, contractor, temp, third-party)
- [ ] Role count matches HR headcount report (±5% variance acceptable)
- [ ] No duplicate role entries
- [ ] All required fields populated for each role

**Tier Classification:**
- [ ] ALL roles from inventory have tier assignments
- [ ] ALL scores documented (no blanks)
- [ ] ALL assignments have justification text
- [ ] Override assignments have explicit approval documented

**Training Requirements:**
- [ ] ALL tiers have training requirements mapped
- [ ] Regulatory-mandated training included with compliance reference
- [ ] Delivery method and frequency specified for each requirement

**Gap Analysis:**
- [ ] ALL role-requirement combinations evaluated
- [ ] ALL gaps have priority assigned
- [ ] ALL gaps have remediation action, owner, and target date
- [ ] No "TBD" or placeholder entries

## Accuracy Checks

- [ ] Scoring criteria applied consistently across all roles
- [ ] Tier assignments follow matrix (or justified override)
- [ ] Gap status reflects current LMS/training records
- [ ] Evidence references are accurate and accessible
- [ ] Dashboard metrics calculate correctly

## Policy Alignment Checks

- [ ] Training tiers match POL-A.6.3 Section 2.2 definitions
- [ ] Training requirements align with POL-A.6.3 Section 2.3-2.4
- [ ] Approval workflow follows organizational governance
- [ ] Frequency requirements match policy minimums

## Audit Readiness Checks

- [ ] Evidence register complete with all supporting documents
- [ ] All evidence accessible in designated storage location
- [ ] Assessment dated and version-controlled
- [ ] Approver signatures obtained (or digital equivalent)
- [ ] Clear audit trail from role → tier → requirements → gaps

## Red Flags to Address Before Submission

| Red Flag | Resolution |
|----------|------------|
| >10% of roles unclassified | Complete classification |
| Critical gaps without owner | Assign ownership |
| Remediation dates >6 months out | Justify or accelerate |
| Missing evidence for major findings | Collect before submission |
| Dashboard shows <80% coverage | Investigate and document |

---

# Review & Approval

## Review Workflow

**Step 1: Self-Review** (Assessment Owner)

Before submitting for review:
- Run through Quality Checklist above
- Verify all calculations are correct
- Ensure evidence is collected and accessible
- Prepare summary of key findings for reviewers
- Set assessment status to "Draft - Ready for Review"

**Step 2: HR Director Review**

**Reviewer:** HR Director or HR Business Partner Lead
**Focus:** Organizational accuracy

**Review Points:**
- Role inventory completeness and accuracy
- Personnel counts match HR records
- Employment type classifications correct
- Department coverage complete
- Role descriptions accurate

**Duration:** 2-3 business days

**Outcomes:**
- Approved: No organizational concerns
- Revisions Required: Specific corrections noted

**Step 3: Information Security Officer Review**

**Reviewer:** Information Security Officer (ISO)
**Focus:** Security classification accuracy

**Review Points:**
- Tier assignment methodology applied correctly
- Scoring criteria interpreted appropriately
- Training requirements comprehensive
- Gap prioritization reasonable
- Remediation plans realistic

**Duration:** 3-5 business days

**Outcomes:**
- Approved: Classifications and gaps validated
- Revisions Required: Classification or gap concerns noted

**Step 4: CISO Final Approval**

**Reviewer:** Chief Information Security Officer
**Focus:** Overall assessment quality and strategic alignment

**Review Points:**
- Assessment completeness
- Material gaps identified and addressed
- Remediation timelines appropriate
- Resource requirements reasonable
- Risk posture implications

**Duration:** 1-2 business days

**Outcomes:**
- Approved: Assessment complete, remediation authorized
- Approved with Conditions: Specific follow-up required
- Rejected: Significant issues, reassessment needed

## Approval Timeline

**Typical Timeline:**

| Phase | Duration | Cumulative |
|-------|----------|------------|
| Assessment completion | 3-5 days | Day 5 |
| Self-review | 1 day | Day 6 |
| HR Director review | 2-3 days | Day 9 |
| ISO review | 3-5 days | Day 14 |
| CISO approval | 1-2 days | Day 16 |
| **Total** | **~3 weeks** | |

**Expedited Timeline:** 1 week (with pre-coordination and dedicated reviewer time)

## After Approval

**Immediate Actions:**

1. **Store Assessment:**
   - Location: `ISMS/Controls/A.6.3_Training/Assessments/[Year]/`
   - Filename: `ISMS-IMP-A.6.3.1_Training_Needs_Assessment_[DATE]_APPROVED.xlsx`

2. **Distribute Results:**
   - HR Training Team: For training program planning
   - Department Managers: For awareness of their team's requirements
   - Compliance Team: For audit evidence
   - Security Team: For risk tracking

3. **Initiate Remediation:**
   - Create tickets/tasks for each gap
   - Assign to documented owners
   - Set due dates per remediation plan
   - Schedule check-in meetings

4. **Schedule Follow-Up:**
   - Quarterly gap remediation review
   - Annual full reassessment
   - Trigger-based reassessment (reorg, new systems, etc.)

---

# PART II: TECHNICAL SPECIFICATION
**Audience:** Generator Script Developers

---

# Excel Workbook Technical Specification

## Workbook Metadata

```python
DOCUMENT_ID = "ISMS-IMP-A.6.3.1"
WORKBOOK_NAME = "Training Needs Assessment"
CONTROL_ID = "A.6.3"
CONTROL_NAME = "Information Security Awareness, Education and Training"
```

## Sheet Specifications

### Sheet 1: Instructions

**Purpose:** User guidance and assessment overview

**Content Sections:**
1. Assessment Purpose
2. Scope and Applicability
3. Completion Workflow
4. Key Definitions
5. Support Contacts

**Formatting:**
- Header: Bold, centered, larger font
- Sections: Clear headings with explanatory text
- Workflow: Numbered steps with descriptions
- Freeze top row

### Sheet 2: Role_Inventory

**Column Specification:**

| Column | Header | Width | Type | Validation | Required |
|--------|--------|-------|------|------------|----------|
| A | Role_ID | 12 | Text | Unique, format "XXX-000" | Yes |
| B | Role_Title | 30 | Text | None | Yes |
| C | Department | 20 | Text | None | Yes |
| D | Employment_Type | 15 | Dropdown | Employee, Contractor, Temp, Third-Party | Yes |
| E | Personnel_Count | 12 | Integer | ≥1 | Yes |
| F | Role_Description | 50 | Text | None | Yes |
| G | Primary_Systems | 40 | Text | None | Yes |
| H | Highest_Data_Classification | 15 | Dropdown | Public, Internal, Confidential, Restricted | Yes |
| I | External_Facing | 10 | Dropdown | Yes, No | Yes |
| J | Technical_Role | 10 | Dropdown | Yes, No | Yes |
| K | Management_Role | 10 | Dropdown | Yes, No | Yes |
| L | Notes | 40 | Text | None | No |

**Formatting:**
- Header row: Bold, frozen, filter-enabled
- Alternating row colors
- Data validation dropdowns where specified
- Conditional formatting: Restricted data = orange highlight

### Sheet 3: Tier_Classification

**Column Specification:**

| Column | Header | Width | Type | Validation | Required |
|--------|--------|-------|------|------------|----------|
| A | Role_ID | 12 | Reference | Must match Role_Inventory | Yes |
| B | Role_Title | 30 | Lookup | =VLOOKUP(A,Role_Inventory,2) | Auto |
| C | System_Access_Score | 18 | Integer | 1-5 | Yes |
| D | Data_Handling_Score | 18 | Integer | 1-5 | Yes |
| E | Technical_Depth_Score | 18 | Integer | 1-5 | Yes |
| F | External_Exposure_Score | 20 | Integer | 1-5 | Yes |
| G | Regulatory_Scope_Score | 18 | Integer | 1-5 | Yes |
| H | Total_Score | 12 | Formula | =SUM(C:G) | Auto |
| I | Assigned_Tier | 12 | Formula/Override | Tier 1-7 | Yes |
| J | Classification_Justification | 50 | Text | None | Yes |
| K | Approved_By | 25 | Text | None | Yes |
| L | Approval_Date | 12 | Date | None | Yes |

**Tier Assignment Formula (Column I):**
```excel
=IF(AND(Management_Role="Yes",H>=12),"Tier 7",
  IF(H<=7,"Tier 1",
    IF(H<=11,"Tier 2",
      IF(H<=15,"Tier 3",
        IF(H<=19,"Tier 4",
          IF(H<=22,"Tier 5","Tier 6"))))))
```

**Scoring Criteria (embedded in sheet or separate reference):**

### Sheet 4: Training_Requirements

**Column Specification:**

| Column | Header | Width | Type | Required |
|--------|--------|-------|------|----------|
| A | Tier | 10 | Dropdown | Yes |
| B | Training_Topic | 40 | Text | Yes |
| C | Topic_Category | 20 | Dropdown | Yes |
| D | Mandatory | 10 | Dropdown | Yes |
| E | Frequency | 15 | Dropdown | Yes |
| F | Delivery_Requirement | 20 | Dropdown | Yes |
| G | Assessment_Required | 15 | Dropdown | Yes |
| H | Regulatory_Driver | 30 | Text | No |
| I | Policy_Reference | 25 | Text | Yes |
| J | Notes | 40 | Text | No |

**Dropdown Values:**

- Tier: Tier 1, Tier 2, Tier 3, Tier 4, Tier 5, Tier 6, Tier 7
- Topic_Category: Baseline Awareness, Data Protection, Technical Security, Privileged Access, Specialized, Governance
- Mandatory: Yes, No
- Frequency: Onboarding, Annual, Bi-Annual, Quarterly, As Needed, Upon Change
- Delivery_Requirement: Any, eLearning, Instructor-Led, Workshop, Simulation
- Assessment_Required: Yes, No

**Pre-populated Data (from POL-A.6.3 Sections 2.3-2.4):**

[Include 40-60 rows of pre-populated training requirements mapped to tiers]

### Sheet 5: Gap_Analysis

**Column Specification:**

| Column | Header | Width | Type | Required |
|--------|--------|-------|------|----------|
| A | Role_ID | 12 | Reference | Yes |
| B | Role_Title | 30 | Lookup | Auto |
| C | Assigned_Tier | 12 | Lookup | Auto |
| D | Training_Topic | 40 | Reference | Yes |
| E | Required_By | 15 | Lookup | Auto |
| F | Current_Status | 15 | Dropdown | Yes |
| G | Gap_Description | 50 | Text | If gap |
| H | Priority | 10 | Dropdown | Yes |
| I | Remediation_Action | 50 | Text | If gap |
| J | Target_Date | 12 | Date | If gap |
| K | Owner | 25 | Text | If gap |
| L | Status_Update | 30 | Text | No |

**Dropdown Values:**

- Current_Status: Completed, Partial, Not Started, Not Available
- Priority: Critical, High, Medium, Low

**Conditional Formatting:**
- Not Started + Critical: Red fill
- Not Started + High: Orange fill
- Partial: Yellow fill
- Completed: Green fill

### Sheet 6: Evidence_Register

**Column Specification:**

| Column | Header | Width | Type | Required |
|--------|--------|-------|------|----------|
| A | Evidence_ID | 12 | Text | Yes |
| B | Category | 20 | Dropdown | Yes |
| C | Description | 50 | Text | Yes |
| D | Source | 30 | Text | Yes |
| E | Date_Obtained | 12 | Date | Yes |
| F | Location_Reference | 40 | Text | Yes |
| G | Retention_Period | 15 | Text | No |
| H | Notes | 40 | Text | No |

**Dropdown Values:**

- Category: Organizational Data, System Access, Training Records, Policy Documents, Approvals, Other

### Sheet 7: Dashboard

**Metrics to Display:**

**Summary Section:**
- Assessment Date
- Assessor Name
- Review Period
- Next Review Date

**Role Metrics:**
- Total Roles Assessed
- Total Personnel Covered
- Roles by Tier (pie chart)
- Personnel by Tier (bar chart)

**Gap Metrics:**
- Total Gaps Identified
- Gaps by Priority (Critical/High/Medium/Low)
- Gap by Tier (heatmap)
- Remediation Progress (% complete)

**Compliance Score:**
- Formula: (Completed Requirements / Total Requirements) × 100
- Target: ≥90%

### Sheet 8: Approval_Sign_Off

**Layout:**

```
ASSESSMENT APPROVAL RECORD

Assessment Details:
- Document ID: ISMS-IMP-A.6.3.1
- Assessment Period: [Date Range]
- Total Roles Assessed: [Auto from Dashboard]
- Total Gaps Identified: [Auto from Dashboard]

Approval Chain:

1. Assessor
   Name: _______________
   Title: _______________
   Date: _______________
   Signature: _______________

2. HR Director
   Name: _______________
   Title: _______________
   Date: _______________
   Signature: _______________

3. Information Security Officer
   Name: _______________
   Title: _______________
   Date: _______________
   Signature: _______________

4. CISO (Final Approval)
   Name: _______________
   Title: _______________
   Date: _______________
   Signature: _______________

Approval Notes:
[Free text area]
```

---

## Generator Script Requirements

### Required Libraries

```python
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, PatternFill, Border
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl.chart import PieChart, BarChart, Reference
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import FormulaRule, ColorScaleRule
from datetime import datetime
import logging
```

### Generator Script Pattern

Follow standardized generator pattern per ISMS-Control-Implementation-Instructions v3.0:

```python
# =============================================================================
# DOCUMENT METADATA
# =============================================================================
DOCUMENT_ID = "ISMS-IMP-A.6.3.1"
WORKBOOK_NAME = "Training_Needs_Assessment"
CONTROL_ID = "A.6.3"
CONTROL_NAME = "Information Security Awareness, Education and Training"
CONTROL_REF = f"ISO/IEC 27001:2022 - Control {CONTROL_ID}: {CONTROL_NAME}"

GENERATED_DATE = datetime.now().strftime("%d.%m.%Y")
GENERATED_TIMESTAMP = datetime.now().strftime("%Y%m%d")

OUTPUT_FILENAME = f"{DOCUMENT_ID}_{WORKBOOK_NAME}_{GENERATED_TIMESTAMP}.xlsx"
```

### Pre-populated Training Requirements Data

Include reference data for Sheet 4 (Training_Requirements) based on POL-A.6.3:

```python
TRAINING_REQUIREMENTS = [
    # Tier 1 - All Personnel
    ("Tier 1", "Information Security Policy Overview", "Baseline Awareness", "Yes", "Onboarding", "Any", "Yes", "ISO 27001", "POL-A.6.3 §2.3.1"),
    ("Tier 1", "Acceptable Use Policy", "Baseline Awareness", "Yes", "Annual", "Any", "Yes", "ISO 27001", "POL-A.6.3 §2.3.2"),
    ("Tier 1", "Data Classification and Handling", "Baseline Awareness", "Yes", "Annual", "Any", "Yes", "GDPR Art.32", "POL-A.6.3 §2.3.3"),
    ("Tier 1", "Password and Authentication Security", "Baseline Awareness", "Yes", "Annual", "Any", "Yes", "ISO 27001", "POL-A.6.3 §2.3.4"),
    ("Tier 1", "Phishing and Social Engineering Awareness", "Baseline Awareness", "Yes", "Annual", "Any", "Yes", "ISO 27001", "POL-A.6.3 §2.3.5"),
    ("Tier 1", "Security Incident Reporting", "Baseline Awareness", "Yes", "Onboarding", "Any", "Yes", "ISO 27001", "POL-A.6.3 §2.3.6"),
    ("Tier 1", "Physical Security Awareness", "Baseline Awareness", "Yes", "Annual", "Any", "No", "ISO 27001", "POL-A.6.3 §2.3.7"),
    ("Tier 1", "Remote Working Security", "Baseline Awareness", "Yes", "Annual", "Any", "Yes", "ISO 27001", "POL-A.6.3 §2.3.8"),

    # Tier 3 - Data Handlers (includes Tier 1-2)
    ("Tier 3", "Privacy and Data Protection (GDPR/nDSG)", "Data Protection", "Yes", "Annual", "Any", "Yes", "GDPR Art.29", "POL-A.6.3 §2.4.1"),
    ("Tier 3", "Data Subject Rights", "Data Protection", "Yes", "Annual", "Any", "Yes", "GDPR", "POL-A.6.3 §2.4.1"),
    ("Tier 3", "Data Retention and Deletion", "Data Protection", "Yes", "Annual", "Any", "No", "GDPR Art.17", "POL-A.6.3 §2.4.1"),
    ("Tier 3", "Cross-Border Data Transfer", "Data Protection", "Yes", "Annual", "Any", "No", "GDPR Ch.V", "POL-A.6.3 §2.4.1"),

    # Tier 4 - Technical Staff
    ("Tier 4", "Secure Coding Practices", "Technical Security", "Yes", "Annual", "Any", "Yes", "OWASP", "POL-A.6.3 §2.4.2"),
    ("Tier 4", "OWASP Top 10", "Technical Security", "Yes", "Annual", "Any", "Yes", "OWASP", "POL-A.6.3 §2.4.2"),
    ("Tier 4", "Secure Configuration Management", "Technical Security", "Yes", "Annual", "Any", "No", "CIS", "POL-A.6.3 §2.4.2"),
    ("Tier 4", "Vulnerability Management", "Technical Security", "Yes", "Annual", "Any", "No", "ISO 27001", "POL-A.6.3 §2.4.2"),

    # Tier 5 - Privileged Users
    ("Tier 5", "Privileged Access Management", "Privileged Access", "Yes", "Annual", "Instructor-Led", "Yes", "ISO 27001", "POL-A.6.3 §2.4.3"),
    ("Tier 5", "Incident Response Procedures", "Privileged Access", "Yes", "Annual", "Workshop", "Yes", "ISO 27001", "POL-A.6.3 §2.4.3"),
    ("Tier 5", "Insider Threat Awareness", "Privileged Access", "Yes", "Annual", "Any", "No", "ISO 27001", "POL-A.6.3 §2.4.3"),

    # Tier 6 - Security Roles
    ("Tier 6", "Risk Assessment and Management", "Specialized", "Yes", "Annual", "Any", "Yes", "ISO 27005", "POL-A.6.3 §2.4.4"),
    ("Tier 6", "Security Operations", "Specialized", "Yes", "Annual", "Any", "Yes", "ISO 27001", "POL-A.6.3 §2.4.4"),
    ("Tier 6", "Incident Response and Forensics", "Specialized", "Yes", "Annual", "Workshop", "Yes", "ISO 27001", "POL-A.6.3 §2.4.4"),
    ("Tier 6", "Security Architecture", "Specialized", "Yes", "Annual", "Any", "No", "TOGAF", "POL-A.6.3 §2.4.4"),

    # Tier 7 - Management
    ("Tier 7", "Information Security Governance", "Governance", "Yes", "Annual", "Any", "No", "ISO 27001", "POL-A.6.3 §2.4.5"),
    ("Tier 7", "Risk Management for Executives", "Governance", "Yes", "Annual", "Any", "No", "ISO 31000", "POL-A.6.3 §2.4.5"),
    ("Tier 7", "Incident Management - Executive Role", "Governance", "Yes", "Annual", "Any", "No", "ISO 27001", "POL-A.6.3 §2.4.5"),
]
```

---

## Validation Rules Summary

| Sheet | Validation | Rule |
|-------|------------|------|
| Role_Inventory | Role_ID | Unique, non-empty |
| Role_Inventory | Personnel_Count | Integer ≥ 1 |
| Role_Inventory | Data_Classification | Dropdown only |
| Tier_Classification | Scores | Integer 1-5 |
| Tier_Classification | Assigned_Tier | Must match calculated or justified |
| Gap_Analysis | Current_Status | Dropdown only |
| Gap_Analysis | Remediation fields | Required if gap exists |
| Evidence_Register | Evidence_ID | Unique, non-empty |
| Approval_Sign_Off | All fields | Required for final approval |

---

## QA Checklist

Before generating workbook:

- [ ] All 8 sheets created with correct names
- [ ] Column widths set per specification
- [ ] Data validation dropdowns functional
- [ ] Formulas calculate correctly
- [ ] Conditional formatting applied
- [ ] Header rows frozen
- [ ] Filters enabled on data sheets
- [ ] Dashboard charts render correctly
- [ ] Pre-populated data included (Training_Requirements)
- [ ] Document control metadata accurate
- [ ] Print areas defined for approval sheet

---

# Document Control

**Document ID:** ISMS-IMP-A.6.3.1
**Version:** 1.0
**Classification:** Internal
**Status:** Draft

**Review and Approval:**

| Role | Responsibility |
|------|----------------|
| **Document Owner** | CISO |
| **Technical Review** | Information Security Officer |
| **Business Review** | HR Director |
| **Approval Authority** | CISO |

---

**END OF SPECIFICATION**

---

*"An equation for me has no meaning unless it expresses a thought of God."*
— Srinivasa Ramanujan

<!-- QA_VERIFIED: 2026-02-01 -->
