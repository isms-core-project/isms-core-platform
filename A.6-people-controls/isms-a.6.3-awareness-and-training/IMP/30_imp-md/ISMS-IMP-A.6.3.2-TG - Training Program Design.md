**ISMS-IMP-A.6.3.2-TG - Training Program Design**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.6.3: Information Security Awareness, Education and Training

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.6.3.2-TG |
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

# Technical Specification
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

<!-- QA_VERIFIED: 2026-02-06 -->
