<!-- ISMS-CORE:IMP:ISMS-IMP-A.7.1-3.S2-UG:framework:UG:a.7.1-3 -->
**ISMS-IMP-A.7.1-3.S2-UG - Entry Control Assessment**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.7.2: Physical Entry

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Entry Control Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.7.1-3.S2-UG |
| **Related Policy** | ISMS-POL-A.7.1-3-S2 (Physical Access Control) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.7.2 (Physical Entry) |
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

- ISMS-POL-A.7.1-3-S2 (Physical Access Control)
- ISMS-IMP-A.7.1-3-S1 (Perimeter Security Assessment)
- ISMS-IMP-A.7.1-3-S3 (Secure Areas Assessment)

---

### Document Structure

This is the **User Completion Guide**. The companion Technical Specification is documented in ISMS-IMP-A.7.1-3.S2-TG.

---

## Workbook at a Glance

| # | Sheet Name | Purpose |
|---|-----------|---------|
| 1 | Instructions & Legend | How to use this workbook and understand the colour coding |
| 2 | Access Control Systems | Assess physical access control systems and technologies |
| 3 | Visitor Management | Evaluate visitor registration and escort procedures |
| 4 | Contractor Access | Assess access management for contractors and third parties |
| 5 | After-Hours Access | Evaluate out-of-hours access controls and monitoring |
| 6 | Evidence Register | Store and reference evidence supporting assessments |
| 7 | Summary Dashboard | Compliance status and key metrics overview |
| 8 | Approval Sign-Off | Management review sign-off and certification |

---

## Assessment Overview

### Purpose & Scope

**Assessment Name:** ISMS-IMP-A.7.1-3-S2 - Entry Control Assessment

#### What This Assessment Covers

This assessment documents the physical entry CONTROLS at your secure areas. This is the "HOW do people enter?" assessment that answers:

- What access control systems are deployed? (badge readers, PIN pads, biometrics)
- What authentication is required at each entry point by security zone?
- How are visitors managed? (sign-in, ID verification, badges, escorts)
- How are contractors and maintenance personnel controlled?
- What happens for after-hours access?
- Are tailgating/piggybacking prevention measures in place?

#### ISO 27001:2022 Control Reference

> *"Secure areas should be protected by appropriate entry controls and access points."*
>
> --- ISO/IEC 27001:2022, Annex A Control 7.2

**Control Objective:** Ensure only authorised physical access to the organisation's information and other associated assets occurs.

#### Key Principle

Entry controls are the ACTIVE security measures that verify and log who enters secure areas. While perimeters (A.7.1) define WHERE boundaries are, entry controls define HOW access is granted or denied at those boundaries.

#### What You'll Document

**Access Control Systems:**

- Every entry point with electronic access control
- Authentication methods by security zone
- Anti-tailgating measures
- Access log retention and review practices
- System health and maintenance status

**Visitor Management:**

- Sign-in procedures at reception
- ID verification requirements
- Visitor badge issuance and return
- Escort requirements in restricted zones
- Visitor log retention and review
- Emergency evacuation procedures for visitors

**Contractor Access:**

- Pre-authorisation procedures
- Time-limited access controls
- Supervision requirements
- Access logging and review
- Credential management and return

**After-Hours Access:**

- Enhanced authentication for after-hours
- Alarm integration
- Security response procedures
- Access logging
- Lone worker safety considerations

#### How This Relates to Other A.7.1-3 Assessments

| Assessment            | Focus                  | Relationship to A.7.1-3-S2      |
|-----------------------|------------------------|------------------------------------|
| ISMS-IMP-A.7.1-3-S1 | Perimeter Security     | WHERE are the boundaries?          |
| **ISMS-IMP-A.7.1-3-S2** | **Entry Control**  | **HOW is access controlled?**      |
| ISMS-IMP-A.7.1-3-S3 | Secure Areas           | WHAT happens inside secure areas?  |

This assessment builds on Zone definitions from S1 to document HOW access is controlled at each entry point.

### Who Should Complete This Assessment

#### Primary Stakeholders

1. **Physical Security Manager** - Access control systems ownership
2. **Facilities Manager** - Entry point infrastructure
3. **Reception Manager** - Visitor management procedures
4. **IT Operations** - Access control system integration
5. **Compliance Officers** - Audit requirements

#### Required Skills

- Understanding of access control technologies (cards, biometrics, PINs)
- Familiarity with visitor management procedures
- Access to access control system admin consoles
- Knowledge of security zone classifications
- Experience with physical security incident management

#### Time Commitment

- **Initial assessment:** 8-10 hours
- **Quarterly updates:** 2-3 hours

### Expected Outputs

Upon completion, you will have:

1. **Access control inventory** - Every entry point documented with controls
2. **Authentication requirements** - Verified against policy
3. **Visitor procedures** - Documented and verified
4. **Contractor controls** - Documented and verified
5. **After-hours controls** - Documented and verified
6. **Evidence register** - Supporting documentation
7. **Approved assessment** - Four-level approval completed

---

## Prerequisites

### Information You'll Need

Before starting this assessment, gather:

#### 1. System Access

- Administrator access to access control system
- Access to visitor management system
- Access to contractor management records
- Access to access log reports
- Access to CCTV system (for verification)

#### 2. Documentation

- Access control system configuration
- Visitor management procedures
- Contractor access procedures
- After-hours access policy
- Access review records
- Emergency response procedures
- Badge replacement procedures

#### 3. Historical Data

- Access logs (last 90 days)
- Visitor logs (last 12 months)
- Failed access attempt reports
- Security incident reports
- Tailgating incident reports
- Badge loss/theft reports

#### 4. Policy Requirements

- ISMS-POL-A.7.1-3, Section 2.2 (Physical Entry Controls)
  - Section 2.2.1: Entry Point Security
  - Section 2.2.2: Access Control Systems
  - Section 2.2.3: Visitor Management
  - Section 2.2.4: Contractor Access
  - Section 2.2.5: After-Hours Access

### Required Tools

- Microsoft Excel (2016 or later) for workbook completion
- Access to physical access control system admin console
- Camera/phone for evidence photographs
- Access to visitor management system

### Dependencies

This assessment has DEPENDENCIES on:

- ISMS-IMP-A.7.1-3-S1 (Perimeter Security) - Use zone definitions from S1

Outputs from this assessment are INPUT to:


---

## Workflow

### High-Level Process

```
1. PREPARE
   |
2. DOCUMENT ACCESS CONTROL SYSTEMS (Sheet 2)
   |
3. ASSESS VISITOR MANAGEMENT (Sheet 3)
   |
4. ASSESS CONTRACTOR ACCESS (Sheet 4)
   |
5. ASSESS AFTER-HOURS ACCESS (Sheet 5)
   |
6. COLLECT EVIDENCE (Sheet 7)
   |
7. REVIEW SUMMARY (Sheet 6 - automated)
   |
8. QUALITY CHECK
   |
9. OBTAIN APPROVALS (Sheet 8)
```

### Detailed Step-by-Step

**Step 1: Preparation (Day 1 - 2 hours)**

- Read this Part I User Guide completely
- Review ISMS-POL-A.7.1-3 entry control requirements
- Gather all prerequisites (system access, documentation)
- Retrieve zone definitions from S1 (Perimeter Security)
- Schedule facility walk-through with Physical Security Manager
- Download or generate assessment workbook (Excel file)

**Step 2: Access Control Systems Assessment (Day 1-2 - 3-4 hours)**

- Open assessment workbook
- Complete Sheet 1 (Instructions & Legend) - organisation info, assessment date
- Complete Sheet 2 (Access Control Systems) - document all entry points
- Verify authentication methods at each entry point
- Test anti-tailgating measures at critical entry points
- Review access log retention settings
- Document access review schedules and last review dates

**Step 3: Visitor Management Assessment (Day 2-3 - 2-3 hours)**

- Walk through visitor arrival experience
- Complete Sheet 3 (Visitor Management) - all visitor procedures
- Sample visitor logs for completeness
- Verify ID verification processes
- Check visitor badge issuance and return procedures
- Document escort requirements and compliance

**Step 4: Contractor Access Assessment (Day 3-4 - 2 hours)**

- Review contractor management procedures
- Complete Sheet 4 (Contractor Access) - all contractor types
- Verify pre-authorisation processes
- Check access logging for contractors
- Document supervision requirements by area

**Step 5: After-Hours Access Assessment (Day 4 - 2 hours)**

- Review after-hours access policy
- Complete Sheet 5 (After-Hours Access) - all facilities
- Verify enhanced authentication requirements
- Check alarm integration
- Document security response procedures

**Step 6: Evidence Collection (Day 4-5 - 2 hours)**

- Capture screenshots of access control configuration
- Collect sample access logs
- Sample visitor logs
- Collect contractor authorisation forms
- Document evidence in Sheet 7 (Evidence Register)
- Store evidence files in secure location

**Step 7: Summary Review (Day 5 - 1 hour)**

- Review Sheet 6 (Summary Dashboard) - automated compliance scores
- Verify scores appear accurate
- Identify areas below threshold
- Prepare gap remediation plan

**Step 8: Quality Check (Day 5 - 1 hour)**

- Complete self-assessment using Quality Checklist (see section below)
- Verify all required fields completed
- Verify evidence register complete

**Step 9: Obtain Approvals (Day 6-10 - asynchronous)**

- Complete Sheet 8 (Approval Sign-Off) - Level 1: Assessor (you)
- Submit to Level 2: Facilities Manager
- After Level 2, submit to Level 3: Physical Security Manager
- After Level 3, submit to Level 4: CISO

---

## Completing Each Sheet

### Sheet 1: Instructions & Legend

**Purpose:** Assessment metadata and legend for status indicators

**What to Complete:**

- **Document Information** (Rows 4-11):
  - Assessment Date: Date you started this assessment
  - Completed By: Your name and role
  - Organisation: [Organisation] name
  - Assessment Period: Quarter and year

- **Status Legend** (Rows 14-17):
  - Read-only reference - understand colour coding

**Time Required:** 5 minutes

### Sheet 2: Access Control Systems

**Purpose:** Document all electronic access control points

**What to Document (Per Entry Point):**

**Column A - Entry Point ID:**

- Unique identifier: "EP-001", "EP-002", etc.
- Use consistent numbering across all facilities

**Column B - Location:**

- Descriptive location: "Main Entrance - Building A", "Side Door - East Wing"
- Include building name and specific location

**Column C - Security Zone:**

- Dropdown: "Controlled Zone", "Restricted Zone", "High-Security Zone"
- Must match zone definitions from S1

**Column D - Access System Type:**

- Dropdown: "Card", "PIN", "Biometric", "Card+PIN", "Multi-Factor"
- Document the actual system deployed

**Column E - Authentication Method:**

- Dropdown: "Badge Only", "Badge+PIN", "Badge+Biometric", "Dual-Person"
- This is what's required to gain entry

**Column F - Anti-Tailgating:**

- Dropdown: "Yes", "No", "Partial"
- Document measures like mantraps, turnstiles, security guards

**Column G - Log Retention (Days):**

- Number of days access logs are retained
- Verify against policy requirements

**Column H - Last Review Date:**

- Date of last access rights review
- Should be within quarterly requirement

**Column I - Status:**

- Dropdown: "Compliant", "Partial", "Non-Compliant", "N/A"

**Column J - Notes:**

- Any additional context or identified gaps

**Time Required:** 1-2 hours

### Sheet 3: Visitor Management

**Purpose:** Assess visitor management procedures

**What to Document (Per Procedure Element):**

**Column A - Procedure Element:**

- Dropdown: "Sign-In", "ID Check", "Badge", "Escort", "Sign-Out", "After-Hours"

**Column B - Location/Facility:**

- Where this procedure applies: "All Facilities", "HQ Reception", "Branch Office A"

**Column C - Implemented:**

- Dropdown: "Yes", "No", "Partial", "N/A"
- Is the procedure in place?

**Column D - Sign-In Process:**

- Is visitor sign-in required? "Yes", "No", "Partial", "N/A"

**Column E - ID Verification:**

- Is government-issued ID checked? "Yes", "No", "Partial", "N/A"

**Column F - Badge Issued:**

- Is a visitor badge issued? "Yes", "No", "Partial", "N/A"

**Column G - Escort Required:**

- Is escort required in secure areas? "Yes", "No", "Partial", "N/A"

**Column H - Status:**

- Dropdown: "Compliant", "Partial", "Non-Compliant", "N/A"

**Column I - Notes:**

- Any additional context

**Time Required:** 45-60 minutes

### Sheet 4: Contractor Access

**Purpose:** Assess contractor and maintenance access controls

**What to Document (Per Contractor Type):**

**Column A - Contractor Type:**

- Dropdown: "IT", "Cleaning", "Security", "HVAC", "Delivery", "Construction", "Other"

**Column B - Facility/Area:**

- Where contractors of this type access: "All Areas", "Server Room", "Office Floors"

**Column C - Pre-Authorisation:**

- Is pre-authorisation required? "Yes", "No", "Partial", "N/A"

**Column D - Time-Limited Access:**

- Is access time-limited? "Yes", "No", "Partial", "N/A"

**Column E - Access Logged:**

- Is access logged? "Yes", "No", "Partial", "N/A"

**Column F - Escort Required:**

- Is escort required? "Yes", "No", "Partial", "N/A"

**Column G - Supervision Level:**

- Dropdown: "Full Escort", "Spot Checks", "Self-Supervised", "Not Required"

**Column H - Status:**

- Dropdown: "Compliant", "Partial", "Non-Compliant", "N/A"

**Column I - Notes:**

- Any additional context

**Time Required:** 30-45 minutes

### Sheet 5: After-Hours Access

**Purpose:** Assess enhanced controls for after-hours access

**What to Document (Per Facility/Entry Point):**

**Column A - Facility/Entry Point:**

- Location: "HQ - Main Entrance", "Datacenter - Primary Entry"

**Column B - Security Zone:**

- Dropdown: "Controlled", "Restricted", "High-Security"

**Column C - After-Hours Period:**

- Definition: "18:00-07:00 weekdays, all day weekends/holidays"

**Column D - Enhanced Auth:**

- Is enhanced authentication required? "Yes", "No", "Partial", "N/A"

**Column E - Alarm Integration:**

- Is entry linked to alarm system? "Yes", "No", "Partial", "N/A"

**Column F - Security Response:**

- What security response exists: "SOC Monitoring", "Guard Patrol", "Automated Alert"

**Column G - Access Logged:**

- Is after-hours access logged? "Yes", "No", "Partial", "N/A"

**Column H - Status:**

- Dropdown: "Compliant", "Partial", "Non-Compliant", "N/A"

**Column I - Notes:**

- Any additional context

**Time Required:** 30-45 minutes

### Sheet 6: Summary Dashboard

**Purpose:** Automated compliance scoring

**What to Review (Auto-Calculated - Read-Only):**

- Overall Entry Control Compliance Score
- Access Control Systems Score
- Visitor Management Score
- Contractor Access Score
- After-Hours Access Score

**NO manual data entry in this sheet**

**Time Required:** 15-30 minutes for review

### Sheet 7: Evidence Register

**Purpose:** Document all supporting evidence

**What to Document (Per Evidence Item):**

**Column A - Evidence ID:**

- Unique identifier: "E-001", "E-002", etc.

**Column B - Evidence Type:**

- Type of evidence: "Configuration Screenshot", "Access Log", "Visitor Log", "Procedure Document"

**Column C - Description:**

- What the evidence shows

**Column D - Collection Date:**

- Date evidence was collected

**Column E - Collector:**

- Who collected the evidence

**Column F - Location/Link:**

- Where evidence is stored: SharePoint path, file server location

**Column G - Status:**

- Dropdown: "Collected", "Pending", "Missing"

**Time Required:** 1-2 hours

### Sheet 8: Approval Sign-Off

**Purpose:** Four-level approval workflow

**Approval Levels:**

- Level 1: Assessor (you)
- Level 2: Facilities Manager
- Level 3: Physical Security Manager
- Level 4: CISO Approver

**Time Required:** 5 minutes for Level 1 completion

---

## Evidence Collection

### What Evidence to Collect

**1. Access Control System:**

- System configuration screenshots
- Access level definitions
- Sample access logs (7-day period)
- Access review records
- Maintenance logs
- System health reports

**2. Visitor Management:**

- Visitor log samples (1 month)
- Visitor badge examples (photograph)
- Reception procedures document
- Escort sign-in sheets
- Visitor log retention verification

**3. Contractor Access:**

- Contractor pre-authorisation forms
- Contractor badge examples
- Supervision records
- Time-limited access configuration
- Contractor access logs

**4. After-Hours:**

- After-hours access logs
- Alarm integration configuration
- Security response procedures
- Enhanced authentication configuration
- Incident reports (after-hours)

**5. System Integration:**

- Integration with HR systems (termination workflow)
- Badge deactivation logs
- Emergency access procedures

### Evidence Storage

- **Location:** SharePoint > ISMS > Assessments > A.7.2 > Evidence
- **Retention:** 3 years minimum
- **Access:** CISO, Facilities Manager, Physical Security Manager, Compliance Officer, Internal Audit
- **Naming Convention:** ISMS-A.7.2-[EvidenceType]-[Date].[ext]

---

## Common Pitfalls

### Pitfall 1: Incomplete Entry Point Coverage

- **Problem:** Only documenting main entrance, missing side doors, emergency exits, loading docks

- **Impact:** Audit finding - incomplete assessment leaves security gaps undocumented

- **How to Avoid:**
  - Use perimeter assessment (S1) to identify ALL entry points
  - Walk the entire facility perimeter
  - Include emergency exits, loading docks, basement entries
  - Document roof access points if applicable

- **Example:**
  - ❌ MISTAKE: Only listing "Main Entrance - Building A" when building has 8 entry points
  - ✅ CORRECT: Documenting all 8 entry points including emergency exits and loading dock

### Pitfall 2: Not Testing Anti-Tailgating

- **Problem:** Assuming anti-tailgating measures work without verification

- **Impact:** Tailgating remains possible despite documented controls

- **How to Avoid:**
  - Observe actual entry during busy periods
  - Check for mantrap effectiveness
  - Review tailgating incident reports
  - Interview security personnel about observed behaviours

- **Example:**
  - ❌ MISTAKE: Marking "Anti-Tailgating: Yes" because mantrap is installed but never testing it
  - ✅ CORRECT: Observing mantrap operation, reviewing incident reports, confirming effectiveness

### Pitfall 3: Visitor Log Gaps

- **Problem:** Visitor logs not consistently completed

- **Impact:** Cannot verify who visited facility, audit trail incomplete

- **How to Avoid:**
  - Sample visitor logs for last month
  - Verify sign-in/sign-out completion rates
  - Check ID verification compliance
  - Interview reception staff about challenges

- **Example:**
  - ❌ MISTAKE: Accepting visitor management as "Compliant" without sampling logs
  - ✅ CORRECT: Sampling 50 visitor entries, finding 90% complete sign-in but only 60% sign-out

### Pitfall 4: Contractor Access Untracked

- **Problem:** Contractors accessing facilities without proper pre-authorisation or logging

- **Impact:** Unknown individuals in secure areas, accountability gap

- **How to Avoid:**
  - Review contractor access records for last quarter
  - Verify pre-authorisation process is followed
  - Check supervision records
  - Interview facilities staff about contractor management

- **Example:**
  - ❌ MISTAKE: Documenting contractor controls as "Compliant" without verification
  - ✅ CORRECT: Reviewing 20 contractor visits, finding 3 without pre-authorisation

### Pitfall 5: After-Hours Controls Not Enhanced

- **Problem:** Same access controls after-hours as during business hours

- **Impact:** Reduced security when fewer people present to observe

- **How to Avoid:**
  - Verify enhanced authentication after-hours (e.g., badge + PIN vs badge only)
  - Check alarm integration
  - Verify security response procedures
  - Review after-hours access logs for patterns

- **Example:**
  - ❌ MISTAKE: Assuming after-hours access requires additional authentication
  - ✅ CORRECT: Testing entry at 22:00, confirming badge-only still works (gap identified)

### Pitfall 6: Access Reviews Not Current

- **Problem:** Quarterly access reviews not completed or overdue

- **Impact:** Stale access rights, terminated employees may still have access

- **How to Avoid:**
  - Check access review records and dates
  - Verify dates are within quarterly requirement
  - Document overdue reviews as gaps
  - Check review completion percentage

- **Example:**
  - ❌ MISTAKE: Documenting "Last Review: Q2 2025" in Q1 2026 without flagging as overdue
  - ✅ CORRECT: Flagging review as 6+ months overdue, documenting as Non-Compliant

### Pitfall 7: Badge Revocation Delays

- **Problem:** Terminated employees retaining badge access

- **Impact:** Former employees can access facilities after termination

- **How to Avoid:**
  - Sample terminated employee list against access control system
  - Verify revocation SLA (e.g., same day)
  - Check integration with HR system
  - Review badge return process

- **Example:**
  - ❌ MISTAKE: Assuming badges are revoked on termination because policy says so
  - ✅ CORRECT: Checking 10 terminations from last month, finding 2 with badges still active after 48 hours

### Pitfall 8: Escort Policy Not Enforced

- **Problem:** Visitors in restricted zones without escorts

- **Impact:** Uncontrolled access to sensitive areas

- **How to Avoid:**
  - Observe actual practice during facility walk-through
  - Interview security personnel
  - Review incident reports for escort violations
  - Check visitor badge design (visible "ESCORT REQUIRED"?)

- **Example:**
  - ❌ MISTAKE: Documenting escort policy as "Compliant" based on policy document alone
  - ✅ CORRECT: Observing visitor in server room corridor without escort, documenting as Partial compliance

### Pitfall 9: Authentication Not Zone-Appropriate

- **Problem:** High-security zones accessible with badge-only (no PIN/biometric)

- **Impact:** Authentication doesn't match zone risk level

- **How to Avoid:**
  - Verify authentication requirements against policy by zone
  - Test access points in each zone
  - Document mismatches as gaps

- **Example:**
  - ❌ MISTAKE: Documenting server room access as "Badge+PIN" without testing
  - ✅ CORRECT: Testing server room entry, confirming badge-only works (gap identified)

### Pitfall 10: Insufficient Log Retention

- **Problem:** Access logs not retained for required period

- **Impact:** Cannot investigate historical access patterns, compliance violation

- **How to Avoid:**
  - Verify log retention settings in access control system
  - Test retrieval of historical logs (e.g., 90 days ago)
  - Document retention period in assessment

- **Example:**
  - ❌ MISTAKE: Accepting "90 days" verbally without verification
  - ✅ CORRECT: Attempting to retrieve logs from 85 days ago, confirming successful retrieval

### Pitfall 11: Visitor Badge Return Not Tracked

- **Problem:** Visitor badges not returned at end of visit

- **Impact:** Lost badges could be used for unauthorised access

- **How to Avoid:**
  - Check visitor badge return rate
  - Review process for lost/unreturned badges
  - Verify badge deactivation for unreturned badges
  - Check badge reuse procedures

- **Example:**
  - ❌ MISTAKE: Assuming all visitor badges are returned
  - ✅ CORRECT: Reviewing badge return log, finding 15% unreturned without deactivation

### Pitfall 12: Emergency Exit Alarming Not Verified

- **Problem:** Emergency exits not alarmed or alarms not monitored

- **Impact:** Unauthorised entry/exit through emergency doors undetected

- **How to Avoid:**
  - Test emergency exit alarms
  - Verify alarm monitoring and response
  - Check for propped-open doors
  - Review emergency exit alarm logs

- **Example:**
  - ❌ MISTAKE: Assuming emergency exits are alarmed because policy requires it
  - ✅ CORRECT: Testing 3 emergency exits, finding 1 alarm not functioning

### Pitfall 13: Access Control System Maintenance Gaps

- **Problem:** Access control system not regularly maintained or tested

- **Impact:** System failures could compromise security

- **How to Avoid:**
  - Review maintenance schedule and records
  - Check battery backup testing
  - Verify fail-secure/fail-safe configuration
  - Document maintenance gaps

- **Example:**
  - ❌ MISTAKE: Not assessing system maintenance status
  - ✅ CORRECT: Reviewing maintenance log, finding no battery test for 18 months

### Pitfall 14: Dual-Person Access Not Implemented

- **Problem:** High-security zones don't require dual-person authentication

- **Impact:** Single compromised credential provides full access

- **How to Avoid:**
  - Verify dual-person requirements against policy
  - Test dual-person access at applicable entry points
  - Document implementation status

- **Example:**
  - ❌ MISTAKE: Documenting datacenter as requiring dual-person without testing
  - ✅ CORRECT: Testing datacenter entry, finding single-person access possible

### Pitfall 15: Visitor Pre-Registration Not Utilised

- **Problem:** Visitors arriving without pre-registration, slowing check-in

- **Impact:** Reception overwhelmed, security checks rushed

- **How to Avoid:**
  - Review pre-registration usage statistics
  - Check pre-registration process effectiveness
  - Document usage rates

- **Example:**
  - ❌ MISTAKE: Assuming pre-registration system is being used
  - ✅ CORRECT: Checking statistics showing only 30% of visitors pre-registered

### Pitfall 16: Lost Badge Reporting Delays

- **Problem:** Lost/stolen badges not reported promptly

- **Impact:** Lost badges remain active, can be used for unauthorised access

- **How to Avoid:**
  - Review lost badge reporting statistics
  - Check time from loss to deactivation
  - Document average response time

- **Example:**
  - ❌ MISTAKE: Not assessing lost badge response process
  - ✅ CORRECT: Reviewing 5 lost badge incidents, finding average 72-hour deactivation time

---

## Quality Checklist

Before submitting for Level 2 approval, complete this self-assessment:

### Sheet 1: Instructions & Legend

- [ ] Assessment Date completed
- [ ] Completed By (your name and role)
- [ ] Organisation name filled in
- [ ] Assessment period specified

### Sheet 2: Access Control Systems

- [ ] ALL entry points documented (not just main entrances)
- [ ] Entry points match zone inventory from S1
- [ ] Authentication method verified against zone requirements
- [ ] Anti-tailgating measures documented for each entry point
- [ ] Anti-tailgating measures tested (not just documented)
- [ ] Log retention meets policy requirements (verified, not assumed)
- [ ] Recent access review documented (within quarterly requirement)
- [ ] Access review completion percentage documented
- [ ] System health/maintenance status documented
- [ ] Fail-secure/fail-safe configuration documented

### Sheet 3: Visitor Management

- [ ] All visitor procedures documented
- [ ] Sign-in compliance verified (sample reviewed)
- [ ] Sign-out compliance verified (sample reviewed)
- [ ] ID verification compliance verified (sample reviewed)
- [ ] Visitor badge issuance documented
- [ ] Visitor badge return tracked
- [ ] Escort policy compliance verified (observed, not assumed)
- [ ] Log retention meets policy (12 months minimum)
- [ ] Pre-registration process documented
- [ ] Emergency procedures for visitors documented

### Sheet 4: Contractor Access

- [ ] All contractor types documented
- [ ] Pre-authorisation process verified (sample reviewed)
- [ ] Time-limited access verified (configuration checked)
- [ ] Access logging verified (sample reviewed)
- [ ] Supervision requirements verified (observed)
- [ ] Badge/credential management documented
- [ ] Contractor training requirements documented

### Sheet 5: After-Hours Access

- [ ] After-hours period defined for each facility
- [ ] Enhanced authentication verified (tested, not assumed)
- [ ] Alarm integration verified (configuration checked)
- [ ] Security response documented and verified
- [ ] After-hours access logging verified
- [ ] Lone worker procedures documented

### Sheet 6: Summary Dashboard

- [ ] Dashboard displays scores (not blank, not error)
- [ ] Scores appear reasonable based on assessment findings
- [ ] No formula errors (#REF, #VALUE, etc.)

### Sheet 7: Evidence Register

- [ ] At least 10 evidence items documented
- [ ] Access logs collected (7-day sample)
- [ ] Visitor logs sampled (1 month)
- [ ] Configuration screenshots captured
- [ ] Contractor authorisation forms collected
- [ ] Access review records collected
- [ ] All evidence stored in approved location
- [ ] Evidence naming convention followed

### Sheet 8: Approval Sign-Off

- [ ] Level 1 (Assessor) completed

### Final Checks

- [ ] Facility walk-through completed (not desk-based only)
- [ ] All yellow input cells completed or marked N/A
- [ ] No formula errors (#REF, #VALUE, etc.)
- [ ] Consistent naming across sheets
- [ ] Zone references match S1 assessment
- [ ] Gaps documented with severity rating

---

## Review & Approval

### Four-Level Approval Workflow

**Level 1: Assessor (You)**

- Complete assessment and quality check
- Date and sign Level 1
- Document any assumptions or limitations

**Level 2: Facilities Manager**

- Review entry point accuracy
- Verify physical infrastructure details
- Confirm maintenance records
- Date and sign Level 2

**Level 3: Physical Security Manager**

- Review access control configuration
- Verify visitor and contractor procedures
- Confirm security response procedures
- Date and sign Level 3

**Level 4: CISO Approver**

- Executive review and approval
- Resource allocation for gaps
- Date and sign Level 4

**Timeline:** 5-10 business days for all four levels

### Escalation Procedures

If approval is delayed beyond 10 business days:

1. Send reminder to current approver
2. Escalate to approver's manager after 5 additional days
3. Document delays in assessment notes

---

**END OF USER GUIDE**

---

*"Access is a privilege, not a right."*
— Anon

<!-- QA_VERIFIED: 2026-03-01 -->
