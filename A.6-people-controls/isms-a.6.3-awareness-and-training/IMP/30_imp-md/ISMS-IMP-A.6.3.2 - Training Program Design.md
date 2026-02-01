**ISMS-IMP-A.6.3.2 - Training Program Design**
**Assessment Specification with User Completion Guide**
### ISO/IEC 27001:2022 Control A.6.3: Information Security Awareness, Education and Training

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.6.3.2 |
| **Version** | 1.0 |
| **Assessment Area** | Training Curriculum Framework and Content Management |
| **Related Policy** | ISMS-POL-A.6.3, Section 2.3-2.4 (Training Requirements), Section 2.5 (Delivery Requirements) |
| **Purpose** | Define training curriculum, content requirements, delivery methods, and quality standards for security awareness program |
| **Target Audience** | Training Program Managers, Instructional Designers, Information Security Officers, HR Learning & Development |
| **Assessment Type** | Program Design & Content Management |
| **Review Cycle** | Annual (minimum) + upon significant policy or threat changes |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | Initial | Initial specification for Training Program Design workbook | ISMS Implementation Team |

---

# PART I: USER COMPLETION GUIDE
**Audience:** Training Program Managers, L&D Specialists, Information Security Officers

---

# Assessment Overview

## What This Assessment Measures

This assessment documents [Organization]'s security training curriculum design, content specifications, and delivery standards to ensure training programs meet policy requirements and effectively build security competencies.

**Scope:** 5 assessment domains covering training program design:
1. **Curriculum Framework** - Overall training architecture and structure
2. **Content Specifications** - Detailed requirements for each training module
3. **Delivery Standards** - Methods, platforms, and delivery quality requirements
4. **Assessment Design** - Knowledge verification and competency assessment
5. **Content Lifecycle** - Version control, updates, and maintenance procedures

**Assessment Output:** Excel workbook documenting:
- Complete training curriculum catalog
- Content specifications by module
- Delivery method assignments
- Assessment design standards
- Content review and update schedule
- Quality assurance checklists

## Why This Matters

**ISO 27002:2022 Guidance for A.6.3:**
Training programs should be designed to cover organizational policies, procedures, and guidance relevant to job functions. Content should be practical, regularly updated, and include real-world examples.

**Business Impact:**
- **Training Effectiveness:** Well-designed programs achieve better behavioral outcomes
- **Resource Efficiency:** Structured curriculum avoids duplication and gaps
- **Regulatory Compliance:** Documented program design demonstrates due diligence
- **Audit Readiness:** Clear specifications support audit evidence requirements
- **Scalability:** Standardized design enables consistent delivery across organization

## Who Should Complete This Assessment

**Primary Responsibility:** Training Program Manager / L&D Lead

**Required Stakeholders:**
1. **Training Program Manager** - Curriculum architecture, delivery planning
2. **Information Security Officer** - Content accuracy, security requirements
3. **Instructional Designer** - Learning design, assessment methodology
4. **HR Learning & Development** - Platform capabilities, delivery logistics
5. **Subject Matter Experts** - Technical content validation

## Time Estimate

**Initial Design:** 24-40 hours
**Annual Review:** 8-12 hours

## Connection to Policy

This assessment implements **ISMS-POL-A.6.3, Sections 2.3-2.5** which establish:
- Baseline awareness topics (Section 2.3)
- Role-based training requirements (Section 2.4)
- Training delivery requirements (Section 2.5)

**Policy Authority:** Chief Information Security Officer (CISO)

---

# Prerequisites

## Access Required

- [ ] ISMS-POL-A.6.3 (current version)
- [ ] ISMS-IMP-A.6.3.1 outputs (Training Needs Assessment)
- [ ] Current training content inventory
- [ ] Learning Management System (LMS) capabilities documentation
- [ ] Vendor training catalogs (if using third-party content)
- [ ] Regulatory training requirements checklist

---

# Workbook Structure Overview

## Sheet 1: Instructions
Assessment guidance and completion workflow

## Sheet 2: Curriculum_Catalog
**Purpose:** Master catalog of all training modules

**Columns:**
- Module_ID
- Module_Title
- Training_Tier
- Category
- Mandatory_Optional
- Duration_Minutes
- Delivery_Method
- Assessment_Type
- Frequency
- Policy_Reference
- Content_Owner
- Last_Updated
- Next_Review
- Status

## Sheet 3: Content_Specifications
**Purpose:** Detailed specifications for each module

**Columns:**
- Module_ID
- Learning_Objectives (numbered list)
- Topics_Covered
- Prerequisites
- Target_Audience
- Accessibility_Requirements
- Language_Versions
- Format_Requirements
- Assessment_Questions_Count
- Pass_Threshold
- Remediation_Path
- Regulatory_Mapping

## Sheet 4: Delivery_Standards
**Purpose:** Standards for each delivery method

**Columns:**
- Delivery_Method
- Description
- Use_Cases
- Technical_Requirements
- Instructor_Requirements
- Completion_Tracking
- Assessment_Integration
- Accessibility_Standard
- Quality_Criteria

## Sheet 5: Assessment_Design
**Purpose:** Assessment methodology standards

**Columns:**
- Assessment_Type
- Purpose
- Question_Types
- Minimum_Questions
- Pass_Threshold
- Attempt_Limits
- Feedback_Approach
- Remediation_Requirements
- Record_Retention

## Sheet 6: Content_Lifecycle
**Purpose:** Version control and update schedule

**Columns:**
- Module_ID
- Current_Version
- Version_Date
- Change_Summary
- Review_Cycle
- Next_Review_Date
- Trigger_Events
- Update_Owner
- Approval_Required

## Sheet 7: Gap_Analysis
**Purpose:** Identify curriculum gaps vs. policy requirements

**Columns:**
- Policy_Requirement
- Policy_Reference
- Current_Module (if exists)
- Gap_Description
- Priority
- Remediation_Plan
- Target_Date
- Owner

## Sheet 8: Evidence_Register
Supporting documentation

## Sheet 9: Dashboard
Summary metrics and status

## Sheet 10: Approval_Sign_Off
Formal approval workflow

---

# Completion Walkthrough

## Step 1: Define Curriculum Architecture (Sheet 2)

**Objective:** Create master catalog of all training modules required by the organization.

**Process:**

1. **Start with Policy Requirements:**
   - Reference POL-A.6.3 Sections 2.3-2.4 for required training topics
   - Map each policy requirement to at least one training module
   - Ensure all tiers have appropriate coverage

2. **For Each Module, Define:**
   - **Module_ID:** Unique identifier (e.g., MOD-T1-001)
   - **Module_Title:** Clear, descriptive name
   - **Training_Tier:** Which audience tier this serves (from ISMS-IMP-A.6.3.1)
   - **Category:** Grouping for curriculum organization
   - **Mandatory/Optional:** Is completion required or elective?
   - **Duration:** Estimated time to complete (minutes)
   - **Delivery_Method:** How content will be delivered
   - **Assessment_Type:** How learning will be verified
   - **Frequency:** How often training must be completed
   - **Policy_Reference:** Source requirement from POL-A.6.3

3. **Validate Coverage:**
   - Each policy requirement has at least one module
   - Each tier has appropriate mandatory modules
   - No gaps in required competencies

**Pre-Populated Starting Point:**
The workbook includes baseline modules from POL-A.6.3. Review, modify, and supplement as needed.

## Step 2: Specify Content Requirements (Sheet 3)

**Objective:** Define detailed specifications for each module to guide content development.

**Process:**

1. **For Each Module:**

   **Learning Objectives:**
   - Write 3-5 measurable objectives per module
   - Use action verbs: "identify," "demonstrate," "apply," "analyze"
   - Align with policy intent and risk reduction goals

   **Topics Covered:**
   - List specific topics/subtopics
   - Ensure completeness against policy requirements
   - Include practical examples and scenarios

   **Prerequisites:**
   - What must learners complete first?
   - What knowledge is assumed?

   **Target Audience:**
   - Specific roles or tier(s) this serves
   - Any exclusions or special considerations

   **Accessibility Requirements:**
   - WCAG 2.1 AA compliance
   - Language options needed
   - Alternative format requirements

2. **Assessment Specifications:**
   - Number of questions required
   - Pass threshold (align with Assessment_Design standards)
   - Remediation path if learner fails

## Step 3: Establish Delivery Standards (Sheet 4)

**Objective:** Define quality standards for each delivery method used.

**Process:**

1. **Review Pre-Populated Standards:**
   - eLearning, Instructor-Led, Workshop, Simulation, Briefing, Microlearning
   - Modify to match organizational capabilities

2. **For Each Delivery Method, Confirm:**
   - **Use Cases:** When this method is appropriate
   - **Technical Requirements:** Platform, equipment, connectivity
   - **Instructor Requirements:** Qualifications, certifications
   - **Completion Tracking:** How completion is recorded
   - **Quality Criteria:** Metrics for success

3. **Add Organization-Specific Methods:**
   - Blended approaches
   - Mentoring/coaching programs
   - On-the-job training elements

## Step 4: Define Assessment Standards (Sheet 5)

**Objective:** Establish consistent assessment methodology across training program.

**Process:**

1. **Review Pre-Populated Standards:**
   - Quiz, Practical, Simulation, Scenario, Tabletop
   - Ensure alignment with organizational policies

2. **Customize Thresholds:**
   - Pass thresholds appropriate for risk level
   - Attempt limits reasonable for learner experience
   - Remediation paths practical and effective

3. **Confirm Record Retention:**
   - Retention periods meet regulatory requirements
   - Integration with LMS reporting capabilities

## Step 5: Plan Content Lifecycle (Sheet 6)

**Objective:** Establish version control and update schedule for all content.

**Process:**

1. **For Each Module:**
   - Document current version and date
   - Set review cycle (annual minimum per POL-A.6.3)
   - Define trigger events requiring immediate update

2. **Trigger Events Include:**
   - Policy changes (POL-A.6.3 updates)
   - Significant security incidents
   - Regulatory changes
   - New threat landscape (emerging attack vectors)
   - Organizational changes (new systems, processes)

3. **Assign Ownership:**
   - Content owner responsible for updates
   - Approval required before deployment

## Step 6: Perform Gap Analysis (Sheet 7)

**Objective:** Identify where curriculum doesn't meet policy requirements.

**Process:**

1. **Map Policy to Curriculum:**
   - List each requirement from POL-A.6.3
   - Identify corresponding module (if exists)
   - Document gaps

2. **For Each Gap:**
   - Describe what's missing
   - Assess priority (Critical/High/Medium/Low)
   - Define remediation (develop content, acquire vendor content)
   - Assign owner and target date

## Step 7: Complete Evidence Register and Approvals (Sheets 8-10)

**Objective:** Document supporting evidence and obtain formal approvals.

**Process:**

1. **Evidence Collection:**
   - Policy documents referenced
   - Vendor training specifications (if applicable)
   - Platform capability documentation
   - SME input records

2. **Dashboard Review:**
   - Verify curriculum coverage metrics
   - Confirm tier coverage complete
   - Review gap status

3. **Approval Workflow:**
   - Training Program Manager sign-off
   - Information Security Officer review (accuracy)
   - CISO approval (alignment with ISMS)

---

# Evidence Collection

## General Evidence Guidelines

**Purpose:** Support curriculum design decisions and demonstrate due diligence.

**Evidence Quality Criteria:**
- **Authoritative:** From official sources (policies, standards, vendors)
- **Current:** Dated within validity period
- **Complete:** Covers all curriculum decisions
- **Accessible:** Stored in designated location

**Storage Location:** ISMS Evidence Library / A.6.3 Training / Program_Design / [Year] /

## Evidence Types by Assessment Area

### Curriculum Framework Evidence

| Evidence Type | Description | Source |
|---------------|-------------|--------|
| Policy Requirements Extract | Training requirements from POL-A.6.3 | ISMS |
| Regulatory Training Matrix | Industry-specific requirements | Compliance |
| Vendor Training Catalog | Third-party content options | Vendors |
| Competency Framework | Role competencies mapped to training | HR/ISMS |

### Content Specifications Evidence

| Evidence Type | Description | Source |
|---------------|-------------|--------|
| Learning Objective Templates | Standard objective formats | L&D |
| Accessibility Standards | WCAG 2.1 AA requirements | Accessibility team |
| Content Review Records | SME validation documentation | SME sign-off |

### Delivery Standards Evidence

| Evidence Type | Description | Source |
|---------------|-------------|--------|
| LMS Capabilities Document | Platform features and limitations | IT/Vendor |
| Instructor Certification Records | Trainer qualifications | HR |
| Facility Specifications | Classroom/lab capabilities | Facilities |

### Assessment Design Evidence

| Evidence Type | Description | Source |
|---------------|-------------|--------|
| Assessment Item Bank | Question bank documentation | L&D |
| Psychometric Standards | Validity/reliability standards | L&D |
| Remediation Procedures | Failure pathway documentation | L&D |

---

# Common Pitfalls

## ❌ MISTAKE #1: Designing Training Without Needs Assessment Input

**The Problem:** Creating curriculum without reference to ISMS-IMP-A.6.3.1 (Training Needs Assessment) results in misaligned content.

**Why It Matters:** Curriculum won't serve actual organizational needs. Resources wasted on unnecessary content. Required competencies may be missed.

**The Fix:**
- Always start with completed Training Needs Assessment
- Map curriculum to identified tier requirements
- Validate coverage against needs assessment gaps

## ❌ MISTAKE #2: One-Size-Fits-All Content

**The Problem:** Using identical content for all audiences regardless of role, tier, or technical level.

**Why It Matters:** Technical staff bored by basic content. Non-technical staff confused by advanced topics. Engagement and retention suffer.

**The Fix:**
- Design tier-specific modules
- Create role-relevant scenarios and examples
- Use audience-appropriate language and depth

## ❌ MISTAKE #3: Neglecting Assessment Design

**The Problem:** Training without knowledge verification, or using trivial assessments that don't measure learning.

**Why It Matters:** Can't demonstrate competency. Compliance claims unsupported. No feedback loop for content improvement.

**The Fix:**
- Every mandatory module has meaningful assessment
- Questions test understanding, not just recall
- Pass thresholds reflect actual competency needs

## ❌ MISTAKE #4: Static Content with No Update Plan

**The Problem:** Content created once and never updated despite changing threats, policies, and technology.

**Why It Matters:** Outdated training provides false confidence. New risks not addressed. Compliance gaps emerge.

**The Fix:**
- Establish review cycle for each module
- Define trigger events for immediate updates
- Assign content owners with accountability

## ❌ MISTAKE #5: Ignoring Accessibility Requirements

**The Problem:** Content designed without consideration for users with disabilities.

**Why It Matters:** Excludes portion of workforce. Potential legal/regulatory issues. Incomplete training coverage.

**The Fix:**
- Design to WCAG 2.1 AA standards
- Provide captioning, transcripts, alternative text
- Test with assistive technology
- Include in content specifications

## ❌ MISTAKE #6: Duration Mismatch with Reality

**The Problem:** Module durations listed don't reflect actual time required, or are so long they're never completed.

**Why It Matters:** Scheduling becomes impossible. Learner frustration. Incomplete training recorded as complete.

**The Fix:**
- Pilot test all durations with target audience
- Break long content into digestible modules
- Use microlearning for reinforcement

## ❌ MISTAKE #7: Delivery Method Not Matched to Learning Objective

**The Problem:** Using eLearning for topics requiring hands-on practice, or instructor-led for simple awareness topics.

**Why It Matters:** Learning objectives not achieved. Resources misallocated. Poor training outcomes.

**The Fix:**
- Match delivery to objective type:
  - Awareness → eLearning/Microlearning
  - Skills → Workshop/Practical
  - Behavior change → Simulation
  - Complex judgment → Instructor-led/Scenario

## ❌ MISTAKE #8: No Clear Content Ownership

**The Problem:** Content has no designated owner; updates fall through the cracks.

**Why It Matters:** Content becomes stale. No accountability for quality. Version control chaos.

**The Fix:**
- Every module has named content owner
- Owner responsible for reviews and updates
- Ownership documented in curriculum catalog

## ❌ MISTAKE #9: Not Validating Regulatory Mapping

**The Problem:** Assuming content meets regulatory requirements without verification.

**Why It Matters:** False compliance claims. Audit findings. Potential regulatory penalties.

**The Fix:**
- Document regulatory driver for each module
- Have compliance/legal review regulatory mappings
- Maintain mapping documentation as evidence

## ❌ MISTAKE #10: Designing in Isolation

**The Problem:** Training program designed without input from security, IT, HR, and business stakeholders.

**Why It Matters:** Content may be inaccurate, impractical, or misaligned with business reality.

**The Fix:**
- Include ISO in all content decisions
- Get SME review for technical accuracy
- HR validates delivery feasibility
- Business validates scenario relevance

---

# Quality Checklist

## Completeness Checks

**Curriculum Coverage:**
- [ ] ALL policy requirements from POL-A.6.3 have corresponding module(s)
- [ ] ALL training tiers (1-7) have mandatory modules assigned
- [ ] ALL mandatory modules have assessment defined
- [ ] ALL delivery methods in use have standards documented

**Content Specifications:**
- [ ] ALL modules have learning objectives defined
- [ ] ALL modules have topics covered listed
- [ ] ALL modules have accessibility requirements addressed
- [ ] ALL modules have content owner assigned

**Lifecycle Management:**
- [ ] ALL modules have review date scheduled
- [ ] ALL modules have version documented
- [ ] ALL trigger events defined for content updates

## Accuracy Checks

- [ ] Learning objectives are measurable (action verbs)
- [ ] Durations are realistic (pilot tested)
- [ ] Policy references are accurate and current
- [ ] Regulatory mappings verified by compliance

## Policy Alignment Checks

- [ ] Curriculum aligns with POL-A.6.3 Sections 2.3-2.5
- [ ] Assessment standards meet policy requirements
- [ ] Frequency requirements match policy minimums
- [ ] Delivery methods approved per policy guidance

## Audit Readiness Checks

- [ ] Evidence register complete
- [ ] SME review documented
- [ ] Approval signatures obtained
- [ ] Version history maintained

---

# Review & Approval

## Review Workflow

**Step 1: Self-Review** (Training Program Manager)
- Quality checklist complete
- All gaps documented with remediation plans
- Evidence collected

**Step 2: ISO Review** (Information Security Officer)
- Content accuracy and completeness
- Policy alignment verified
- Regulatory mappings validated
- Duration: 3-5 business days

**Step 3: L&D Review** (HR Learning & Development)
- Instructional design quality
- Delivery feasibility
- Platform capabilities confirmed
- Duration: 2-3 business days

**Step 4: CISO Approval**
- Strategic alignment
- Resource requirements acceptable
- Risk reduction adequate
- Duration: 1-2 business days

## After Approval

1. **Store Assessment:**
   - Location: `ISMS/Controls/A.6.3_Training/Program_Design/`
   - Filename: `ISMS-IMP-A.6.3.2_Program_Design_[DATE]_APPROVED.xlsx`

2. **Distribute Results:**
   - L&D Team: For content development prioritization
   - Vendor Management: For procurement planning
   - IT: For LMS configuration requirements

3. **Initiate Development:**
   - Create tickets for content development
   - Procure vendor content where identified
   - Schedule content reviews

4. **Schedule Follow-Up:**
   - Annual curriculum review
   - Quarterly gap remediation check
   - Content update triggers monitoring

---

# PART II: TECHNICAL SPECIFICATION
**Audience:** Generator Script Developers

---

# Excel Workbook Technical Specification

## Workbook Metadata

```python
DOCUMENT_ID = "ISMS-IMP-A.6.3.2"
WORKBOOK_NAME = "Training_Program_Design"
CONTROL_ID = "A.6.3"
CONTROL_NAME = "Information Security Awareness, Education and Training"
```

## Pre-Populated Data

### Curriculum Catalog (Sample Entries)

Based on POL-A.6.3 requirements, pre-populate baseline modules:

```python
CURRICULUM_CATALOG = [
    # Tier 1 - Baseline Awareness
    ("MOD-T1-001", "Information Security Fundamentals", "Tier 1", "Baseline Awareness", "Mandatory", 30, "eLearning", "Quiz", "Onboarding", "POL-A.6.3 §2.3.1"),
    ("MOD-T1-002", "Acceptable Use Policy", "Tier 1", "Baseline Awareness", "Mandatory", 20, "eLearning", "Quiz", "Annual", "POL-A.6.3 §2.3.2"),
    ("MOD-T1-003", "Data Classification and Handling", "Tier 1", "Baseline Awareness", "Mandatory", 25, "eLearning", "Quiz", "Annual", "POL-A.6.3 §2.3.3"),
    ("MOD-T1-004", "Password Security and Authentication", "Tier 1", "Baseline Awareness", "Mandatory", 20, "eLearning", "Quiz", "Annual", "POL-A.6.3 §2.3.4"),
    ("MOD-T1-005", "Phishing and Social Engineering", "Tier 1", "Baseline Awareness", "Mandatory", 30, "eLearning + Simulation", "Quiz + Simulation", "Annual", "POL-A.6.3 §2.3.5"),
    ("MOD-T1-006", "Security Incident Reporting", "Tier 1", "Baseline Awareness", "Mandatory", 15, "eLearning", "Quiz", "Onboarding", "POL-A.6.3 §2.3.6"),
    ("MOD-T1-007", "Physical Security Awareness", "Tier 1", "Baseline Awareness", "Mandatory", 15, "eLearning", "Quiz", "Annual", "POL-A.6.3 §2.3.7"),
    ("MOD-T1-008", "Remote Working Security", "Tier 1", "Baseline Awareness", "Mandatory", 20, "eLearning", "Quiz", "Annual", "POL-A.6.3 §2.3.8"),

    # Tier 3 - Data Handlers
    ("MOD-T3-001", "Privacy and Data Protection Fundamentals", "Tier 3", "Data Protection", "Mandatory", 45, "eLearning", "Quiz", "Annual", "POL-A.6.3 §2.4.1"),
    ("MOD-T3-002", "Data Subject Rights and Obligations", "Tier 3", "Data Protection", "Mandatory", 30, "eLearning", "Quiz", "Annual", "POL-A.6.3 §2.4.1"),
    ("MOD-T3-003", "Data Retention and Secure Deletion", "Tier 3", "Data Protection", "Mandatory", 25, "eLearning", "Quiz", "Annual", "POL-A.6.3 §2.4.1"),

    # Tier 4 - Technical Staff
    ("MOD-T4-001", "Secure Coding Practices", "Tier 4", "Technical Security", "Mandatory", 60, "eLearning + Workshop", "Quiz + Practical", "Annual", "POL-A.6.3 §2.4.2"),
    ("MOD-T4-002", "OWASP Top 10 Vulnerabilities", "Tier 4", "Technical Security", "Mandatory", 45, "eLearning", "Quiz", "Annual", "POL-A.6.3 §2.4.2"),
    ("MOD-T4-003", "Secure Configuration Management", "Tier 4", "Technical Security", "Mandatory", 30, "eLearning", "Quiz", "Annual", "POL-A.6.3 §2.4.2"),

    # Tier 5 - Privileged Users
    ("MOD-T5-001", "Privileged Access Management", "Tier 5", "Privileged Access", "Mandatory", 45, "Instructor-Led", "Quiz + Scenario", "Annual", "POL-A.6.3 §2.4.3"),
    ("MOD-T5-002", "Incident Response for System Admins", "Tier 5", "Privileged Access", "Mandatory", 60, "Workshop", "Practical", "Annual", "POL-A.6.3 §2.4.3"),

    # Tier 6 - Security Roles
    ("MOD-T6-001", "Risk Assessment Methodology", "Tier 6", "Specialized", "Mandatory", 120, "Instructor-Led", "Practical", "Annual", "POL-A.6.3 §2.4.4"),
    ("MOD-T6-002", "Incident Response and Forensics", "Tier 6", "Specialized", "Mandatory", 240, "Workshop", "Tabletop + Practical", "Annual", "POL-A.6.3 §2.4.4"),

    # Tier 7 - Management
    ("MOD-T7-001", "Information Security Governance", "Tier 7", "Governance", "Mandatory", 45, "eLearning + Briefing", "N/A", "Annual", "POL-A.6.3 §2.4.5"),
    ("MOD-T7-002", "Executive Cyber Risk Briefing", "Tier 7", "Governance", "Mandatory", 30, "Briefing", "N/A", "Quarterly", "POL-A.6.3 §2.4.5"),
]
```

### Delivery Standards (Pre-Populated)

```python
DELIVERY_STANDARDS = [
    ("eLearning", "Self-paced online modules", "Baseline awareness, refresher training, geographically dispersed", "LMS access, modern browser, mobile-responsive", "N/A", "Automatic via LMS", "Integrated quiz at completion", "WCAG 2.1 AA", "Completion rate ≥95%, Avg score ≥80%"),
    ("Instructor-Led", "Facilitated classroom or virtual training", "Complex topics, discussion-based, specialized roles", "Classroom/VC platform, presentation equipment", "Certified instructor, subject matter expertise", "Attendance record, completion certificate", "Post-session assessment", "Accessible venue, captioning for virtual", "Participant satisfaction ≥4/5, Learning objectives achieved"),
    ("Workshop", "Hands-on practical exercises", "Technical skills, incident response, simulations", "Lab environment, scenario tools", "Technical SME, facilitation experience", "Participation record, exercise completion", "Practical assessment during workshop", "Adjustable workstations, assistive tech compatible", "Skills demonstration, scenario completion"),
    ("Simulation", "Realistic scenario exercises", "Phishing awareness, social engineering, incident drills", "Simulation platform, realistic scenarios", "Campaign design expertise", "Engagement tracking, response metrics", "Behavioral measurement (click rate, report rate)", "Text alternatives for visual elements", "Click rate ≤5%, Report rate ≥70%"),
    ("Briefing", "Executive-level information sessions", "Leadership updates, strategic awareness", "Executive meeting space, concise materials", "Senior security leadership", "Attendance record", "N/A (awareness-focused)", "Standard meeting accessibility", "Attendance, engagement feedback"),
    ("Microlearning", "Brief focused modules (2-5 min)", "Reinforcement, emerging threats, quick updates", "Mobile-friendly delivery, push notifications", "N/A", "View tracking", "Optional quick check", "Mobile accessible", "Completion rate, engagement metrics"),
]
```

### Assessment Design Standards (Pre-Populated)

```python
ASSESSMENT_STANDARDS = [
    ("Quiz", "Knowledge verification post-training", "Multiple choice, True/False, Matching", 10, "80%", 3, "Immediate, show correct answers", "Retake training if 3 fails", "5 years"),
    ("Practical", "Skills demonstration", "Hands-on exercises, scenario completion", 3, "Pass/Fail per task", 2, "Instructor feedback", "Additional coaching", "3 years"),
    ("Simulation", "Behavioral assessment", "Phishing response, social engineering resistance", 1, "Did not click + reported", "N/A", "Educational landing page if fail", "Targeted remedial training", "3 years"),
    ("Scenario", "Situational judgment", "Case studies, decision scenarios", 5, "80%", 2, "Explanation of optimal response", "Review with SME", "5 years"),
    ("Tabletop", "Group decision-making exercise", "Incident scenarios, team response", 1, "Participation + contribution", 1, "Facilitator debrief", "Individual follow-up if needed", "3 years"),
]
```

---

## Sheet Specifications

### Sheet 2: Curriculum_Catalog

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Module_ID | 15 | Text | Unique, format "MOD-TX-000" |
| B | Module_Title | 40 | Text | Required |
| C | Training_Tier | 10 | Dropdown | Tier 1-7 |
| D | Category | 20 | Dropdown | Baseline Awareness, Data Protection, Technical Security, Privileged Access, Specialized, Governance |
| E | Mandatory_Optional | 12 | Dropdown | Mandatory, Optional |
| F | Duration_Minutes | 15 | Integer | ≥5 |
| G | Delivery_Method | 25 | Dropdown | eLearning, Instructor-Led, Workshop, Simulation, Briefing, Microlearning, Blended |
| H | Assessment_Type | 20 | Dropdown | Quiz, Practical, Simulation, Scenario, Tabletop, N/A |
| I | Frequency | 15 | Dropdown | Onboarding, Annual, Bi-Annual, Quarterly, As Needed |
| J | Policy_Reference | 25 | Text | Required |
| K | Content_Owner | 25 | Text | Required |
| L | Last_Updated | 12 | Date | Required |
| M | Next_Review | 12 | Date | Required |
| N | Status | 12 | Dropdown | Active, Draft, Under Review, Retired |

### Sheet 3: Content_Specifications

| Column | Header | Width | Type |
|--------|--------|-------|------|
| A | Module_ID | 15 | Reference to Catalog |
| B | Learning_Objectives | 60 | Text (numbered list) |
| C | Topics_Covered | 60 | Text (list) |
| D | Prerequisites | 30 | Text |
| E | Target_Audience | 30 | Text |
| F | Accessibility_Requirements | 40 | Text |
| G | Language_Versions | 20 | Text |
| H | Format_Requirements | 40 | Text |
| I | Assessment_Questions_Count | 20 | Integer |
| J | Pass_Threshold | 15 | Percentage |
| K | Remediation_Path | 40 | Text |
| L | Regulatory_Mapping | 40 | Text |

---

## QA Checklist

- [ ] All 10 sheets created
- [ ] Pre-populated data included
- [ ] Dropdown validations functional
- [ ] Cross-references between sheets work
- [ ] Curriculum covers all POL-A.6.3 requirements
- [ ] Assessment standards align with policy

---

# Document Control

**Document ID:** ISMS-IMP-A.6.3.2
**Version:** 1.0
**Classification:** Internal
**Status:** Draft

---

**END OF SPECIFICATION**

---

*"The essence of mathematics is not to make simple things complicated, but to make complicated things simple."*
— Srinivasa Ramanujan

<!-- QA_VERIFIED: 2026-02-01 -->
