**ISMS-IMP-A.7.6-7-14-S2-UG - Clear Desk and Clear Screen Compliance Assessment**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.7.7: Clear Desk and Clear Screen

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.7.6-7-14-S2-UG |
| **Version** | 1.0 |
| **Assessment Area** | Clear Desk and Clear Screen - Workspace Information Protection |
| **Related Policy** | ISMS-POL-A.7.6-7-14, Section 2.2 (Clear Desk and Clear Screen) |
| **Purpose** | Document clear desk/screen requirements, assess workspace compliance, track audit results and enforcement |
| **Target Audience** | Facilities Management, IT Operations, Line Managers, Compliance Officers, Auditors |
| **Assessment Type** | Operational & Procedural |
| **Review Cycle** | Monthly (Audits) / Quarterly (Full Assessment) |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Clear Desk/Screen Compliance assessment workbook | ISMS Implementation Team |

### Document Structure

This is the **User Completion Guide**. The companion Technical Specification is documented in ISMS-IMP-A.7.6-7-14-S2-TG.

---

## Assessment Overview

### Purpose & Scope

**Assessment Name:** ISMS-IMP-A.7.6-7-14-S2 - Clear Desk and Clear Screen Compliance Assessment

#### What This Assessment Covers

This assessment documents the clear desk and clear screen requirements and evaluates workplace compliance. It answers:

- What clear desk requirements are defined for different classification levels?
- What screen lock configurations are deployed across the organisation?
- How is compliance monitored and enforced?
- What are the audit results from clear desk checks?
- What non-compliance incidents have occurred?
- What gaps exist between current practices and policy requirements?

#### ISO 27001:2022 Control Reference

> *Clear desk rules for papers and removable storage media and clear screen rules for information processing facilities should be defined and appropriately enforced.*
>
> — ISO/IEC 27001:2022 Annex A, Control A.7.7

**Control Objective:** Reduce risk of unauthorised access, loss of, or damage to information during and outside normal working hours.

#### Key Principle

This assessment covers BOTH physical workspace (clear desk) and digital workspace (clear screen) protection measures. It evaluates technical controls (screen lock timeouts) and procedural controls (desk audits, awareness training).

#### What You'll Document

**Clear Desk Requirements:**

- Classification-specific storage requirements (CONFIDENTIAL, INTERNAL, PUBLIC)
- Lockable storage availability and allocation
- Removable media handling requirements
- Printer security measures

**Clear Screen Implementation:**

- Screen lock timeout configurations by classification level
- Manual lock shortcut awareness and usage
- Privacy screen deployment in high-risk areas
- End-of-day procedures

**Compliance Monitoring:**

- Audit frequency and methodology
- Audit results and trends
- Non-compliance reporting and escalation
- Training and awareness programmes

**Workspace Assessment:**

- Office area compliance by location
- Remote working compliance
- Meeting room compliance
- Shared space compliance

#### How This Relates to Other A.7.6-7-14 Assessments

| Assessment | Focus | Relationship to S2 |
|------------|-------|-------------------|
| ISMS-IMP-A.7.6-7-14-S1 | Secure Areas Working | Clean desk requirements in secure areas feed into S1 |
| **ISMS-IMP-A.7.6-7-14-S2** | **Clear Desk/Screen Compliance** | **WHAT rules exist, HOW are they enforced** |
| ISMS-IMP-A.7.6-7-14-S3 | Equipment Disposal Assessment | Removable media disposal links to S3 |
| ISMS-IMP-A.7.6-7-14-S4 | Compliance Dashboard | Consolidated view across all controls |

### Who Should Complete This Assessment

#### Primary Stakeholders

1. **Facilities Manager** - Clear desk audit execution, storage provision
2. **IT Operations** - Screen lock configuration, endpoint management
3. **Line Managers** - Team compliance oversight
4. **Compliance Officers** - Policy enforcement and audit coordination

#### Required Skills

- Understanding of information classification levels
- Familiarity with endpoint management tools (screen lock configuration)
- Knowledge of workplace audit procedures
- Access to audit results and compliance records

#### Time Commitment

- **Initial assessment:** 6-10 hours
- **Monthly updates (audit results):** 1-2 hours
- **Quarterly full assessment:** 3-4 hours

### Expected Outputs

Upon completion, you will have:

1. **Complete requirements documentation** - Clear desk/screen rules by classification
2. **Technical configuration assessment** - Screen lock settings verified
3. **Audit programme documentation** - Methodology, frequency, results
4. **Workspace compliance analysis** - By location/area
5. **Incident tracking** - Non-compliance events and resolution
6. **Gap analysis** - Identified gaps requiring remediation
7. **Evidence register** - Supporting documentation for audit
8. **Approved assessment** - Four-level approval workflow completed

---

## Prerequisites

### Information You'll Need

Before starting this assessment, gather:

#### 1. Policy Documentation

- Clear desk and clear screen policy
- Information classification policy (CONFIDENTIAL, INTERNAL, PUBLIC definitions)
- Remote working policy (if applicable)

#### 2. Technical Configuration Data

- Endpoint management reports (screen lock timeout settings)
- Group Policy or MDM configuration for screen lock
- Privacy screen inventory (if deployed)

#### 3. Audit Records

- Clear desk audit checklists and results (last 12 months)
- Audit methodology documentation
- Non-compliance reports and follow-up actions

#### 4. Workspace Information

- Office floor plans with workspace types
- Lockable storage inventory and allocation
- Shredder/confidential waste bin locations
- Meeting room list and security equipment

#### 5. Training Records

- Clear desk/screen awareness training completion rates
- Training materials used

### Required Tools

- Microsoft Excel (2016 or later) for workbook completion
- Access to endpoint management console
- Clear desk audit checklist templates
- Screen capture tools (for evidence)

### Dependencies

This assessment has NO dependencies on other assessments - it can be completed independently.

Outputs feed into:
- ISMS-IMP-A.7.6-7-14-S4 (Compliance Dashboard)

---

## Workflow

### High-Level Process

```
1. PREPARE
   |
2. DOCUMENT REQUIREMENTS (Sheet 2: Requirements Matrix)
   |
3. ASSESS TECHNICAL CONTROLS (Sheet 3: Screen Lock Configuration)
   |
4. REVIEW AUDIT RESULTS (Sheet 4: Audit Results)
   |
5. ASSESS WORKSPACES (Sheet 5: Workspace Assessment)
   |
6. COLLECT EVIDENCE (Sheet 7: Evidence Register)
   |
7. REVIEW SUMMARY (Sheet 6: Summary Dashboard)
   |
8. QUALITY CHECK
   |
9. OBTAIN APPROVALS (Sheet 8: Approval Sign-Off)
   |
10. SUBMIT FOR AUDIT
```

---

## Completing Each Sheet

### Sheet 1: Instructions & Legend

**Purpose:** Assessment metadata and legend for status indicators

**What to Complete:**

- Assessment Date, Completed By, Organisation
- Review status legend for colour coding

**Time Required:** 5 minutes

### Sheet 2: Requirements Matrix

**Purpose:** Document clear desk/screen requirements by classification level

**What to Document:**

**Clear Desk Requirements Table:**

| Classification | During Work Hours | End of Day | Storage Required |
|----------------|-------------------|------------|------------------|
| CONFIDENTIAL | Locked when unattended | Mandatory locked storage | Lockable drawer/cabinet |
| INTERNAL | Locked at end of day | Recommended locked storage | Lockable drawer/cabinet |
| PUBLIC | Best practice | Not mandatory | Open storage acceptable |

**Clear Screen Requirements Table:**

| Classification | Auto-Lock Timeout | Manual Lock Required | Privacy Screen |
|----------------|-------------------|---------------------|----------------|
| CONFIDENTIAL | 5 minutes | Yes | Required in open areas |
| INTERNAL | 10 minutes | Yes | Recommended |
| PUBLIC | 15 minutes | Best practice | Not required |

**Column Structure:**

| Col | Field | Description |
|-----|-------|-------------|
| A | Classification Level | CONFIDENTIAL / INTERNAL / PUBLIC |
| B | Clear Desk - Work Hours | Requirement during work |
| C | Clear Desk - End of Day | End of day requirement |
| D | Storage Requirement | Type of storage required |
| E | Screen Lock Timeout | Maximum auto-lock timeout |
| F | Privacy Screen Required | Yes / Recommended / No |
| G | Implementation Status | Implemented / Partial / Not Implemented |
| H | Notes | Additional context |

**Time Required:** 1-2 hours

### Sheet 3: Screen Lock Configuration

**Purpose:** Document and verify screen lock settings across device types

**What to Document (Per Device Type/Policy):**

**Column A - Device Type:**

- "Windows Workstations", "MacOS Devices", "Mobile Devices (iOS)", "Mobile Devices (Android)"

**Column B - Policy Name:**

- Group Policy or MDM policy name: "GPO-ScreenLock-Standard", "Intune-MDM-Mobile"

**Column C - Configured Timeout (minutes):**

- Actual timeout configured: 5, 10, 15

**Column D - Required Timeout (per policy):**

- Required per clear screen policy

**Column E - Compliant:**

- Formula: Yes if Configured <= Required

**Column F - Enforcement Method:**

- "Group Policy", "Intune MDM", "JAMF", "Manual"

**Column G - Device Count:**

- Number of devices covered

**Column H - Last Verified:**

- Date configuration was verified

**Column I - Evidence:**

- Screenshot reference or configuration export

**Column J - Notes:**

- Exceptions, remediation plans

**Time Required:** 1-2 hours

### Sheet 4: Audit Results

**Purpose:** Track clear desk audit results over time

**What to Document (Per Audit):**

**Column A - Audit Date:**

- Date of audit: "15.01.2026"

**Column B - Audit Type:**

- "Scheduled Monthly", "Random Spot Check", "Post-Incident"

**Column C - Location/Area:**

- "Building A - Floor 2", "Remote Workers", "Executive Suite"

**Column D - Workstations Audited:**

- Number audited: 25, 50, etc.

**Column E - Compliant:**

- Number passing audit

**Column F - Non-Compliant:**

- Number failing audit

**Column G - Compliance Rate:**

- Formula: E/(E+F) * 100%

**Column H - Common Issues Found:**

- "Sensitive documents on desk", "USB drives left out", "Unlocked screens"

**Column I - Follow-Up Actions:**

- "Line managers notified", "Training scheduled", "Repeat audit planned"

**Column J - Auditor:**

- Name of auditor

**Time Required:** 1-2 hours (capturing historical audits)

### Sheet 5: Workspace Assessment

**Purpose:** Assess compliance infrastructure by workspace area

**What to Document (Per Area):**

**Column A - Area ID:**

- "WS-001", "WS-002", etc.

**Column B - Location:**

- "Building A - Floor 2 Open Plan"

**Column C - Workspace Type:**

- Dropdown: "Open Plan Office", "Private Office", "Meeting Room", "Shared Space", "Home Office"

**Column D - Workstation Count:**

- Number of workstations

**Column E - Lockable Storage Available:**

- "Yes - All", "Yes - Partial", "No"

**Column F - Shredder Access:**

- "Yes - On Floor", "Yes - Central", "No"

**Column G - Confidential Waste Bins:**

- "Yes", "No"

**Column H - Privacy Screens Deployed:**

- "Yes - All", "Yes - Partial", "No", "N/A"

**Column I - Average Audit Compliance:**

- Average compliance rate from audits: "95%", "87%"

**Column J - Compliance Status:**

- Formula auto-calculates

**Column K - Notes:**

- Remediation plans, equipment requests

**Time Required:** 2-3 hours

### Sheet 6: Summary Dashboard

**Purpose:** Automated compliance scoring and metrics

**What to Review:**

- Overall Compliance Score
- Screen Lock Configuration Compliance
- Audit Results Summary (trend chart)
- Workspace Infrastructure Compliance
- Gap Summary

**Time Required:** 15-30 minutes for review

### Sheet 7: Evidence Register

**Purpose:** Document all supporting evidence for audit traceability

**Common Evidence to Collect:**

1. Clear desk/screen policy document
2. Screen lock GPO/MDM configuration screenshots
3. Sample audit checklists (completed)
4. Audit results summary reports
5. Non-compliance incident reports
6. Training completion records
7. Storage allocation records
8. Privacy screen deployment records

**Time Required:** 2-3 hours

### Sheet 8: Approval Sign-Off

**Purpose:** Four-level approval workflow

**Approval Levels:**

- Level 1: Assessor
- Level 2: Facilities Manager
- Level 3: CISO
- Level 4: Compliance Officer

**Time Required:** 5 minutes for Level 1

---

## Evidence Collection

### What Evidence to Collect

**1. Policy Evidence**

- Clear desk and clear screen policy document
- Information classification policy
- Remote working policy

**2. Technical Configuration Evidence**

- Group Policy configuration (screen lock timeout)
- MDM configuration screenshots
- Endpoint management compliance reports

**3. Audit Evidence**

- Completed audit checklists (sample)
- Audit results summary reports
- Photo evidence of compliant/non-compliant workstations (anonymised)

**4. Infrastructure Evidence**

- Storage allocation records
- Privacy screen inventory
- Shredder/secure bin locations

**5. Training Evidence**

- Training completion reports
- Training materials

### Evidence Storage

**Location:** SharePoint > ISMS > Assessments > A.7.6-7-14 > S2_Clear_Desk_Screen > Evidence

**Retention:** 3 years minimum

---

## Common Pitfalls

### Pitfall 1: Screen Lock Configuration Not Verified

**Problem:** Assuming GPO/MDM configuration is deployed correctly without verification

**How to Avoid:**

- Export configuration from endpoint management console
- Spot-check random devices to verify actual timeout
- Document last verification date

### Pitfall 2: Audit Results Not Trended

**Problem:** Individual audit results documented but no trend analysis

**How to Avoid:**

- Document all audits (monthly minimum)
- Calculate compliance trend over time
- Identify persistent problem areas

### Pitfall 3: Remote Workers Excluded

**Problem:** Clear desk/screen assessment only covers office workers

**How to Avoid:**

- Include remote working in scope
- Document remote working policy requirements
- Consider remote audit mechanisms (self-certification, video check)

### Pitfall 4: Lockable Storage Insufficiency

**Problem:** Policy requires locked storage but insufficient provision

**How to Avoid:**

- Verify lockable storage availability vs. requirement
- Document allocation and any shortfalls
- Include remediation plan for gaps

### Pitfall 5: Privacy Screens Not Deployed Where Required

**Problem:** High-risk areas (open plan, public facing) lack privacy screens

**How to Avoid:**

- Identify areas requiring privacy screens
- Document current deployment
- Include procurement plan for gaps

### Pitfall 6: Non-Compliance Not Escalated

**Problem:** Repeat non-compliance not escalated to line managers/HR

**How to Avoid:**

- Document escalation process
- Track repeat offenders (anonymised)
- Evidence escalation actions taken

### Pitfall 7: Meeting Room Compliance Ignored

**Problem:** Focus on desks but meeting rooms have whiteboards, printouts left

**How to Avoid:**

- Include meeting rooms in audit scope
- Document whiteboard erasing requirements
- Check for post-meeting compliance

### Pitfall 8: Printer Security Not Addressed

**Problem:** Secure printing not implemented or not enforced

**How to Avoid:**

- Document printer locations and security features
- Verify secure print (authentication) deployment
- Include printer areas in audits

---

## Quality Checklist

### Sheet 2: Requirements Matrix

- [ ] All classification levels documented (CONFIDENTIAL, INTERNAL, PUBLIC)
- [ ] Clear desk requirements defined per classification
- [ ] Clear screen timeout requirements defined per classification
- [ ] Privacy screen requirements defined
- [ ] Implementation status accurate

### Sheet 3: Screen Lock Configuration

- [ ] All device types documented (Windows, Mac, Mobile)
- [ ] Configured timeout values accurate (verified)
- [ ] Compliance calculated correctly
- [ ] Evidence referenced for each configuration

### Sheet 4: Audit Results

- [ ] At least 12 months of audit results
- [ ] Compliance rates calculated
- [ ] Common issues documented
- [ ] Follow-up actions documented

### Sheet 5: Workspace Assessment

- [ ] All workspace areas documented
- [ ] Lockable storage availability accurate
- [ ] Privacy screen deployment documented
- [ ] Compliance infrastructure gaps identified

### Sheet 7: Evidence Register

- [ ] Policy documents referenced
- [ ] Configuration screenshots collected
- [ ] Audit checklists/results referenced
- [ ] All evidence files exist in documented location

---

**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
