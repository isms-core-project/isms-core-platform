**ISMS-IMP-A.7.1-2-3-S3-UG - Secure Areas Assessment**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.7.3: Securing Offices, Rooms and Facilities

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.7.1-2-3-S3-UG |
| **Version** | 1.0 |
| **Assessment Area** | Securing Offices, Rooms and Facilities - Office Security, Server Rooms, Meeting Rooms |
| **Related Policy** | ISMS-POL-A.7.1-2-3, Section 2.3 (Securing Offices, Rooms and Facilities) |
| **Purpose** | Document secure area controls, assess office security, verify server room protection, evaluate meeting room procedures |
| **Target Audience** | Facilities Management, IT Operations, Physical Security, Compliance Officers, Auditors |
| **Assessment Type** | Technical & Operational |
| **Review Cycle** | Annual or After Facility Changes |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Secure Areas assessment workbook | ISMS Implementation Team |

### Document Structure

This is the **User Completion Guide**. The companion Technical Specification is documented in ISMS-IMP-A.7.1-2-3-S3-TG.

---

## Assessment Overview

### Purpose & Scope

**Assessment Name:** ISMS-IMP-A.7.1-2-3-S3 - Secure Areas Assessment

#### What This Assessment Covers

This assessment documents the security WITHIN offices, rooms, and facilities. This is the "WHAT happens inside secure areas?" assessment that answers:

- Are offices locked when unoccupied?
- Is the clean desk policy enforced?
- Are screens positioned to prevent shoulder surfing?
- Are server rooms adequately protected (MFA, no windows, CCTV)?
- Are meeting rooms checked for recording devices before sensitive discussions?
- For shared buildings, is the organisation's perimeter clearly defined?

#### ISO 27001:2022 Control Reference

> *"Physical security for offices, rooms and facilities should be designed and implemented."*
>
> --- ISO/IEC 27001:2022, Annex A Control 7.3

**Control Objective:** Prevent unauthorised physical access, damage and interference to the organisation's information and other associated assets in offices, rooms and facilities.

#### Key Principle

While perimeters (A.7.1) define boundaries and entry controls (A.7.2) manage who enters, secure area controls ensure appropriate security measures are in place INSIDE those spaces. This includes both physical controls (locks, CCTV) and procedural controls (clean desk, screen privacy).

#### What You'll Document

**Office Security:**

- Locking policy when unoccupied
- Clean desk policy enforcement
- Screen privacy measures
- Secure storage availability
- Information classification handling
- Visitor supervision in office areas
- CCTV coverage in office spaces

**Server Rooms and Datacenters:**

- Multi-factor access requirements
- No external windows
- Reinforced construction
- CCTV coverage
- Environmental monitoring
- Access logging
- Visitor supervision requirements
- Equipment security

**Meeting Rooms:**

- Recording device checks before sensitive meetings
- Whiteboard clearing procedures
- Document clearing procedures
- Video conferencing equipment security
- Room booking and access controls
- Sensitive meeting designation

**Shared Facilities:**

- Perimeter definition in shared buildings
- Building management access controls
- Shared infrastructure risks
- Key management coordination
- Visitor control at shared entry points
- Emergency response coordination

#### How This Relates to Other A.7.1-2-3 Assessments

| Assessment            | Focus                  | Relationship to A.7.1-2-3-S3      |
|-----------------------|------------------------|------------------------------------|
| ISMS-IMP-A.7.1-2-3-S1 | Perimeter Security     | WHERE are the boundaries?          |
| ISMS-IMP-A.7.1-2-3-S2 | Entry Control          | HOW is access controlled?          |
| **ISMS-IMP-A.7.1-2-3-S3** | **Secure Areas**   | **WHAT controls inside areas?**    |
| ISMS-IMP-A.7.1-2-3-S4 | Compliance Dashboard   | Overall physical access control    |

This assessment documents controls WITHIN secure areas, building on the perimeter (S1) and entry (S2) assessments.

### Who Should Complete This Assessment

#### Primary Stakeholders

1. **Facilities Manager** - Office and building security
2. **IT Operations Manager** - Server room and datacenter security
3. **Physical Security Manager** - Overall secure area controls
4. **Property/Estates** - Shared facility arrangements
5. **Compliance Officers** - Audit requirements

#### Required Skills

- Understanding of office security requirements
- Familiarity with datacenter security standards
- Knowledge of clean desk and screen privacy policies
- Access to server room and datacenter facilities
- Understanding of shared building arrangements

#### Time Commitment

- **Initial assessment:** 6-10 hours
- **Annual updates:** 2-3 hours

### Expected Outputs

Upon completion, you will have:

1. **Office security inventory** - All office areas with security controls
2. **Server room assessment** - Technical controls verified
3. **Meeting room procedures** - Documented and verified
4. **Shared facility arrangements** - Documented and assessed
5. **Evidence register** - Supporting documentation
6. **Approved assessment** - Four-level approval completed

---

## Prerequisites

### Information You'll Need

#### 1. Documentation

- Office security policy
- Clean desk policy
- Server room/datacenter security standards
- Meeting room procedures
- Shared building lease agreements
- Floor plans with room designations
- Environmental monitoring specifications

#### 2. System Access

- Access to server rooms for inspection
- Access to access control system for server room logs
- Access to CCTV system for server room coverage
- Access to environmental monitoring dashboards
- Access to building management system

#### 3. Historical Data

- Clean desk audit results
- Server room access logs
- Security incident reports
- Environmental monitoring alerts
- Meeting room usage logs
- Key management records

#### 4. Policy Requirements

- ISMS-POL-A.7.1-2-3, Section 2.3 (Securing Offices, Rooms and Facilities)
  - Section 2.3.1: General Offices
  - Section 2.3.2: Sensitive Areas
  - Section 2.3.3: Server Rooms
  - Section 2.3.4: Meeting Rooms
  - Section 2.3.5: Shared Facilities

### Required Tools

- Microsoft Excel (2016 or later) for workbook completion
- Camera/phone for evidence photographs
- Access to building management systems
- Floor plan viewing software (PDF or CAD)
- Torch/flashlight (for server room inspections)

### Dependencies

This assessment has DEPENDENCIES on:

- ISMS-IMP-A.7.1-2-3-S1 (Perimeter Security) - Zone inventory
- ISMS-IMP-A.7.1-2-3-S2 (Entry Control) - Access control configuration

Outputs from this assessment are INPUT to:

- ISMS-IMP-A.7.1-2-3-S4 (Compliance Dashboard) - Secure areas compliance score

---

## Workflow

### High-Level Process

```
1. PREPARE
   |
2. ASSESS OFFICE SECURITY (Sheet 2)
   |
3. ASSESS SERVER ROOMS (Sheet 3)
   |
4. ASSESS MEETING ROOMS (Sheet 4)
   |
5. ASSESS SHARED FACILITIES (Sheet 5)
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
- Review ISMS-POL-A.7.1-2-3 secure areas requirements
- Gather all prerequisites (documentation, system access)
- Retrieve zone inventory from S1 (Perimeter Security)
- Schedule facility walk-through with Facilities Manager
- Download or generate assessment workbook (Excel file)

**Step 2: Office Security Assessment (Day 1-2 - 2-3 hours)**

- Walk through all office areas
- Complete Sheet 2 (Office Security) - all office spaces
- Verify locking policies are implemented
- Check clean desk policy compliance
- Assess screen privacy measures
- Verify secure storage availability
- Document CCTV coverage in office areas

**Step 3: Server Room Assessment (Day 2-3 - 2-3 hours)**

- Conduct physical inspection of all server rooms
- Complete Sheet 3 (Server Rooms) - all technical spaces
- Verify MFA access requirements
- Check for external windows (should be none)
- Assess CCTV coverage
- Verify environmental monitoring
- Review access logs

**Step 4: Meeting Room Assessment (Day 3 - 1-2 hours)**

- Review meeting room procedures
- Complete Sheet 4 (Meeting Rooms) - all meeting spaces
- Verify recording check procedures
- Check whiteboard/document clearing compliance
- Assess video conferencing equipment security
- Review room booking controls

**Step 5: Shared Facilities Assessment (Day 3-4 - 1-2 hours)**

- Review shared building arrangements
- Complete Sheet 5 (Shared Facilities) - all shared spaces
- Verify perimeter definition within shared buildings
- Check building management access controls
- Document key management coordination

**Step 6: Evidence Collection (Day 4-5 - 2 hours)**

- Take photographs of server room controls
- Capture clean desk audit results
- Collect CCTV coverage maps
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
- After Level 2, submit to Level 3: IT Operations Manager
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
  - Assessment Period: Year

- **Status Legend** (Rows 14-17):
  - Read-only reference - understand colour coding

**Time Required:** 5 minutes

### Sheet 2: Office Security

**Purpose:** Assess security controls in general office areas

**What to Document (Per Office/Area):**

**Column A - Office/Area ID:**

- Unique identifier: "OFF-001", "OFF-002", etc.
- Include all office spaces, not just main floors

**Column B - Location:**

- Descriptive location: "Building A - Floor 3 - Finance", "HQ - Open Plan Area"

**Column C - Security Zone:**

- Dropdown: "Controlled", "Restricted", "High-Security"
- Must match zone definitions from S1

**Column D - Classification:**

- Dropdown: "Public", "Internal", "Confidential", "Highly Confidential"
- Information classification of typical data in this area

**Column E - Lock When Unoccupied:**

- Dropdown: "Yes", "No", "Partial", "N/A"
- Is the area locked when unoccupied?

**Column F - Clean Desk Enforced:**

- Dropdown: "Yes", "No", "Partial", "N/A"
- Is clean desk policy enforced?

**Column G - Screen Privacy:**

- Dropdown: "Yes", "No", "Partial", "N/A"
- Are screen privacy measures in place (filters, positioning)?

**Column H - Secure Storage:**

- Dropdown: "Yes", "No", "Partial", "N/A"
- Is secure storage available for classified documents?

**Column I - Status:**

- Dropdown: "Compliant", "Partial", "Non-Compliant", "N/A"

**Column J - Notes:**

- Any additional context or gaps identified

**Time Required:** 45-60 minutes

### Sheet 3: Server Rooms

**Purpose:** Assess server room and datacenter security

**What to Document (Per Room):**

**Column A - Room ID:**

- Unique identifier: "SR-001", "DC-001", etc.

**Column B - Location:**

- Descriptive location: "Building A - Basement - Main Server Room"

**Column C - Room Type:**

- Dropdown: "Server Room", "Datacenter", "Network Closet", "Comms Room", "UPS Room"

**Column D - MFA Access:**

- Dropdown: "Yes", "No", "Partial", "N/A"
- Is multi-factor access required?

**Column E - No Windows:**

- Dropdown: "Yes", "No", "Partial", "N/A"
- Confirmed no external windows?

**Column F - Reinforced Walls:**

- Dropdown: "Yes", "No", "Partial", "N/A"
- Are walls reinforced?

**Column G - CCTV Coverage:**

- Dropdown: "Yes", "No", "Partial", "N/A"
- Is the room covered by CCTV?

**Column H - Access Logging:**

- Dropdown: "Yes", "No", "Partial", "N/A"
- Is access logged?

**Column I - Env. Monitoring:**

- Dropdown: "Yes", "No", "Partial", "N/A"
- Is environmental monitoring in place (temperature, humidity, water)?

**Column J - Status:**

- Dropdown: "Compliant", "Partial", "Non-Compliant", "N/A"

**Column K - Notes:**

- Any additional context

**Time Required:** 1-2 hours

### Sheet 4: Meeting Rooms

**Purpose:** Assess meeting room security procedures

**What to Document (Per Room):**

**Column A - Room ID:**

- Unique identifier: "MR-001", "MR-002", etc.

**Column B - Location:**

- Descriptive location: "HQ - Floor 5 - Boardroom"

**Column C - Room Classification:**

- Dropdown: "Standard", "Boardroom", "Secure", "Interview"
- Classification based on typical use

**Column D - Recording Check:**

- Dropdown: "Yes", "No", "Partial", "N/A"
- Is recording device check performed before sensitive meetings?

**Column E - Whiteboard Clear:**

- Dropdown: "Yes", "No", "Partial", "N/A"
- Is whiteboard cleared after meetings?

**Column F - Document Clear:**

- Dropdown: "Yes", "No", "Partial", "N/A"
- Are documents cleared after meetings?

**Column G - VC Equipment Secured:**

- Dropdown: "Yes", "No", "Partial", "N/A"
- Is video conferencing equipment secured when not in use?

**Column H - Status:**

- Dropdown: "Compliant", "Partial", "Non-Compliant", "N/A"

**Column I - Notes:**

- Any additional context

**Time Required:** 30-45 minutes

### Sheet 5: Shared Facilities

**Purpose:** Assess security in shared building arrangements

**What to Document (Per Shared Facility):**

**Column A - Facility/Building:**

- Building name: "123 Main Street - Multi-Tenant Office"

**Column B - Sharing Arrangement:**

- Dropdown: "Multi-Tenant", "Co-Working", "Shared Floor", "Colocation", "Sole Occupant"

**Column C - Perimeter Defined:**

- Dropdown: "Yes", "No", "Partial", "N/A"
- Is organisation perimeter clearly defined within building?

**Column D - Own Access Control:**

- Dropdown: "Yes", "No", "Partial", "N/A"
- Does organisation control its own access system?

**Column E - Building Mgmt Access:**

- Dropdown: "Controlled and Logged", "Controlled Only", "Uncontrolled", "N/A"
- How is building management access handled?

**Column F - Shared Infrastructure:**

- Text description of shared infrastructure and risks

**Column G - Key Management:**

- Text description of key management coordination

**Column H - Status:**

- Dropdown: "Compliant", "Partial", "Non-Compliant", "N/A"

**Column I - Notes:**

- Any additional context

**Time Required:** 30-45 minutes

### Sheet 6: Summary Dashboard

**Purpose:** Automated compliance scoring

**What to Review (Auto-Calculated - Read-Only):**

- Overall Secure Areas Compliance Score
- Office Security Score
- Server Rooms Score
- Meeting Rooms Score
- Shared Facilities Score

**NO manual data entry in this sheet**

**Time Required:** 15-30 minutes for review

### Sheet 7: Evidence Register

**Purpose:** Document all supporting evidence

**What to Document (Per Evidence Item):**

**Column A - Evidence ID:**

- Unique identifier: "E-001", "E-002", etc.

**Column B - Evidence Type:**

- Type of evidence: "Photograph", "Audit Report", "Configuration", "Log Sample"

**Column C - Description:**

- What the evidence shows

**Column D - Collection Date:**

- Date evidence was collected

**Column E - Collector:**

- Who collected the evidence

**Column F - Location/Link:**

- Where evidence is stored

**Column G - Status:**

- Dropdown: "Collected", "Pending", "Missing"

**Time Required:** 1-2 hours

### Sheet 8: Approval Sign-Off

**Purpose:** Four-level approval workflow

**Approval Levels:**

- Level 1: Assessor (you)
- Level 2: Facilities Manager
- Level 3: IT Operations Manager
- Level 4: CISO Approver

**Time Required:** 5 minutes for Level 1 completion

---

## Evidence Collection

### What Evidence to Collect

**1. Office Security:**

- Clean desk audit results (recent, within 6 months)
- Screen privacy filter deployment records
- Locking policy document
- Secure storage inventory
- CCTV coverage map for office areas
- Photographs showing clean desk compliance

**2. Server Rooms:**

- Access control configuration (MFA verified)
- Photographs showing no windows
- Photographs of reinforced construction
- CCTV coverage map
- Access logs sample (7-day period)
- Environmental monitoring configuration
- Environmental monitoring alerts (last 12 months)
- Maintenance records

**3. Meeting Rooms:**

- Meeting room procedures document
- Recording check checklists (if used)
- VC equipment inventory
- Room booking system configuration
- Photographs of room clearing signage

**4. Shared Facilities:**

- Lease agreement excerpts (perimeter definition)
- Building management access log
- Key management procedures
- Shared infrastructure documentation
- Emergency response coordination documents

### Evidence Storage

- **Location:** SharePoint > ISMS > Assessments > A.7.3 > Evidence
- **Retention:** 3 years minimum
- **Access:** CISO, Facilities Manager, IT Operations Manager, Compliance Officer, Internal Audit
- **Naming Convention:** ISMS-A.7.3-[EvidenceType]-[Date].[ext]

---

## Common Pitfalls

### Pitfall 1: Clean Desk Not Verified

- **Problem:** Assuming clean desk policy is enforced without verification

- **Impact:** Sensitive documents left exposed, audit finding

- **How to Avoid:**
  - Conduct unannounced clean desk audits
  - Review audit results (should be within 6 months)
  - Document compliance rates with specific numbers
  - Interview facilities/security staff about observations

- **Example:**
  - ❌ MISTAKE: Marking "Clean Desk Enforced: Yes" because policy exists
  - ✅ CORRECT: Reviewing audit results showing 85% compliance, documenting as "Partial"

### Pitfall 2: Server Room Windows Present

- **Problem:** Server rooms with external windows (security and environmental risk)

- **Impact:** Visual access to equipment, potential environmental damage from sunlight/heat

- **How to Avoid:**
  - Physically inspect server rooms
  - Document any windows found
  - Require mitigation (blocking, alarming) if windows exist
  - Take photographs as evidence

- **Example:**
  - ❌ MISTAKE: Not physically checking server room for windows
  - ✅ CORRECT: Physical inspection reveals small window, documenting as "Non-Compliant" with remediation required

### Pitfall 3: Server Room Single-Factor Access

- **Problem:** Server rooms accessible with badge-only (no PIN or biometric)

- **Impact:** Single compromised credential provides access to critical infrastructure

- **How to Avoid:**
  - Test access control configuration at server room doors
  - Verify access control system settings
  - Document actual authentication required

- **Example:**
  - ❌ MISTAKE: Documenting "MFA Access: Yes" based on policy without testing
  - ✅ CORRECT: Testing door, finding badge-only works, documenting as "Non-Compliant"

### Pitfall 4: Meeting Room Information Left Behind

- **Problem:** Whiteboards not erased, documents left after meetings

- **Impact:** Sensitive information exposed to subsequent room users

- **How to Avoid:**
  - Observe meeting room clearing practices
  - Interview cleaning staff about what they find
  - Check for clearing signage/reminders
  - Sample check rooms after meetings

- **Example:**
  - ❌ MISTAKE: Documenting "Whiteboard Clear: Yes" without observation
  - ✅ CORRECT: Checking 5 meeting rooms after meetings, finding 2 with information on whiteboards

### Pitfall 5: Shared Building Perimeter Unclear

- **Problem:** In multi-tenant buildings, organisation perimeter not clearly defined

- **Impact:** Unclear security boundary, shared responsibility gaps

- **How to Avoid:**
  - Review lease agreement for perimeter definition
  - Walk the building to identify actual boundaries
  - Document any unclear areas
  - Verify access controls at perimeter points

- **Example:**
  - ❌ MISTAKE: Assuming building entrance is organisation perimeter
  - ✅ CORRECT: Reviewing lease, finding organisation controls floors 5-7 only, documenting actual perimeter

### Pitfall 6: Building Management Uncontrolled Access

- **Problem:** Building management can access organisation spaces without logging

- **Impact:** Unknown individuals accessing organisation areas

- **How to Avoid:**
  - Review building management access agreement
  - Verify logging of building management access
  - Document arrangements in assessment
  - Check key management procedures

- **Example:**
  - ❌ MISTAKE: Not assessing building management access arrangements
  - ✅ CORRECT: Reviewing lease, finding building management has master key with no logging requirement

### Pitfall 7: Server Room CCTV Coverage Gaps

- **Problem:** CCTV doesn't cover all server room areas

- **Impact:** Actions in blind spots unobserved

- **How to Avoid:**
  - Review CCTV coverage map
  - Walk server room checking camera positions
  - Identify and document blind spots
  - Verify recording retention

- **Example:**
  - ❌ MISTAKE: Documenting "CCTV Coverage: Yes" based on camera presence
  - ✅ CORRECT: Walking server room, finding rear rack aisle not covered, documenting as "Partial"

### Pitfall 8: VC Equipment Recording Risk

- **Problem:** Video conferencing equipment could be used for surveillance

- **Impact:** Unintended recording of meetings, privacy breach

- **How to Avoid:**
  - Verify VC equipment secured when not in use
  - Check for physical camera covers
  - Review equipment configuration
  - Check for always-on microphones

- **Example:**
  - ❌ MISTAKE: Not assessing VC equipment security
  - ✅ CORRECT: Checking VC equipment, finding cameras without physical covers, recommending covers

### Pitfall 9: Incomplete Office Coverage

- **Problem:** Only assessing main offices, missing satellite areas

- **Impact:** Gaps in security controls across organisation

- **How to Avoid:**
  - Use zone inventory from S1 to ensure ALL office areas covered
  - Include storage rooms, mail rooms, print rooms
  - Document all spaces regardless of size

- **Example:**
  - ❌ MISTAKE: Only documenting main open plan office
  - ✅ CORRECT: Documenting all 15 office areas including finance room, print room, storage areas

### Pitfall 10: Environmental Monitoring Not Verified

- **Problem:** Assuming server room environmental monitoring works without verification

- **Impact:** Environmental failures could damage equipment

- **How to Avoid:**
  - Review environmental monitoring configuration
  - Check alert recipients are valid
  - Verify testing records
  - Review historical alerts and responses

- **Example:**
  - ❌ MISTAKE: Documenting "Env. Monitoring: Yes" without verification
  - ✅ CORRECT: Checking configuration, finding alerts go to email address of person who left 2 years ago

### Pitfall 11: Secure Storage Inadequate

- **Problem:** Secure storage exists but is inadequate for needs

- **Impact:** Classified documents cannot be properly secured

- **How to Avoid:**
  - Assess secure storage capacity vs. needs
  - Verify storage meets classification requirements
  - Check storage is in appropriate locations
  - Document any gaps

- **Example:**
  - ❌ MISTAKE: Documenting "Secure Storage: Yes" because cabinets exist
  - ✅ CORRECT: Auditing storage, finding only 50% of desks have lockable drawers, documenting as "Partial"

### Pitfall 12: Screen Privacy Not Position-Based

- **Problem:** Screen privacy relies only on filters, not positioning

- **Impact:** Screens visible from public areas despite filters

- **How to Avoid:**
  - Assess screen positioning relative to public areas
  - Check visibility from windows, corridors, reception
  - Document both filters and positioning

- **Example:**
  - ❌ MISTAKE: Documenting screen privacy as "Yes" because filters deployed
  - ✅ CORRECT: Observing screens visible from public corridor, documenting positioning issue

### Pitfall 13: Network Closets Unsecured

- **Problem:** Network closets without same controls as server rooms

- **Impact:** Network infrastructure accessible with reduced security

- **How to Avoid:**
  - Include ALL technical spaces in assessment
  - Apply appropriate controls based on criticality
  - Document security measures for each closet

- **Example:**
  - ❌ MISTAKE: Only assessing main server room, ignoring 8 network closets
  - ✅ CORRECT: Assessing all network closets, finding 3 with key-only access (no logging)

### Pitfall 14: Meeting Room Booking Not Controlled

- **Problem:** Anyone can book any meeting room regardless of sensitivity

- **Impact:** Sensitive meetings in inappropriate rooms

- **How to Avoid:**
  - Review meeting room booking system configuration
  - Check access restrictions for secure rooms
  - Verify approval workflows for boardroom/secure rooms

- **Example:**
  - ❌ MISTAKE: Not assessing meeting room booking controls
  - ✅ CORRECT: Checking booking system, finding no restrictions on boardroom access

### Pitfall 15: Server Room Visitor Access Uncontrolled

- **Problem:** Vendors/visitors access server rooms without proper supervision

- **Impact:** Unsupervised access to critical infrastructure

- **How to Avoid:**
  - Review server room visitor procedures
  - Check visitor logs for supervision documentation
  - Interview IT staff about visitor handling

- **Example:**
  - ❌ MISTAKE: Assuming all visitors are supervised because policy requires it
  - ✅ CORRECT: Reviewing visitor log, finding 4 of 10 vendor visits without supervision documentation

### Pitfall 16: Environmental Monitoring Thresholds Inappropriate

- **Problem:** Temperature/humidity thresholds set incorrectly or not set

- **Impact:** Alerts not triggered before equipment damage occurs

- **How to Avoid:**
  - Review threshold settings against best practice
  - Verify thresholds for temperature, humidity, water
  - Check alert escalation procedures

- **Example:**
  - ❌ MISTAKE: Documenting environmental monitoring as compliant without checking thresholds
  - ✅ CORRECT: Checking settings, finding temperature alert set at 35C (too high for safe operation)

### Pitfall 17: Shared Infrastructure Risks Not Documented

- **Problem:** Shared building infrastructure creates undocumented risks

- **Impact:** Unknown attack vectors through shared systems

- **How to Avoid:**
  - Document all shared infrastructure (HVAC, electrical, fire suppression)
  - Assess security implications of each shared system
  - Document mitigation measures

- **Example:**
  - ❌ MISTAKE: Not assessing shared infrastructure security implications
  - ✅ CORRECT: Documenting shared HVAC system allowing air flow between tenants, recommending air gap review

### Pitfall 18: Key Management Not Coordinated

- **Problem:** Multiple key holders without central tracking

- **Impact:** Unknown individuals hold keys to secure areas

- **How to Avoid:**
  - Document all key holders
  - Verify key register is current
  - Check key return process
  - Audit key distribution annually

- **Example:**
  - ❌ MISTAKE: Not assessing key management in shared facilities
  - ✅ CORRECT: Reviewing key register, finding 5 keys issued but only 3 holders identifiable

---

## Quality Checklist

Before submitting for Level 2 approval, complete this self-assessment:

### Sheet 1: Instructions & Legend

- [ ] Assessment Date completed
- [ ] Completed By (your name and role)
- [ ] Organisation name filled in
- [ ] Assessment period specified

### Sheet 2: Office Security

- [ ] ALL office areas documented (not just main floor)
- [ ] Office areas match zone inventory from S1
- [ ] Locking policy verified (spot checks conducted)
- [ ] Clean desk compliance verified (audit results reviewed)
- [ ] Clean desk audit results within 6 months
- [ ] Screen privacy measures documented
- [ ] Screen positioning assessed (not just filters)
- [ ] Secure storage capacity vs. needs assessed
- [ ] CCTV coverage in office areas documented
- [ ] Information classification handling documented

### Sheet 3: Server Rooms

- [ ] ALL server rooms/datacenters documented
- [ ] ALL network closets documented
- [ ] MFA access verified (tested, not assumed)
- [ ] No windows verified (physical inspection)
- [ ] Reinforced construction verified
- [ ] CCTV coverage verified (coverage map reviewed)
- [ ] CCTV blind spots identified and documented
- [ ] Access logging verified
- [ ] Environmental monitoring verified (configuration checked)
- [ ] Environmental thresholds appropriate
- [ ] Alert recipients verified (current)
- [ ] Visitor supervision procedures verified

### Sheet 4: Meeting Rooms

- [ ] ALL meeting rooms documented
- [ ] Meeting room procedures documented
- [ ] Recording check procedures verified
- [ ] Whiteboard/document clearing verified (observed)
- [ ] VC equipment security verified
- [ ] Room booking controls documented
- [ ] Sensitive meeting designation process documented

### Sheet 5: Shared Facilities

- [ ] All shared building arrangements documented
- [ ] Perimeter definition verified (lease reviewed)
- [ ] Building management access documented
- [ ] Shared infrastructure risks documented
- [ ] Key management coordination documented
- [ ] Emergency response coordination documented

### Sheet 6: Summary Dashboard

- [ ] Dashboard displays scores (not blank, not error)
- [ ] Scores appear reasonable based on assessment findings
- [ ] No formula errors (#REF, #VALUE, etc.)

### Sheet 7: Evidence Register

- [ ] At least 8 evidence items documented
- [ ] Clean desk audit results collected
- [ ] Server room photographs collected
- [ ] CCTV coverage map collected
- [ ] Environmental monitoring configuration collected
- [ ] Lease agreement excerpts collected (if shared facility)
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

- Review office and meeting room accuracy
- Verify building-related controls
- Confirm shared facility arrangements
- Date and sign Level 2

**Level 3: IT Operations Manager**

- Review server room and datacenter accuracy
- Verify environmental monitoring
- Confirm access control configuration
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

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
