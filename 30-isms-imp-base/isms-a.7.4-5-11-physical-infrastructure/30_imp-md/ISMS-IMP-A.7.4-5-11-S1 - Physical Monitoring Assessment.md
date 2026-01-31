**ISMS-IMP-A.7.4-5-11-S1: Physical Monitoring Assessment**
**Assessment Specification with User Completion Guide**
### ISO/IEC 27001:2022 Control A.7.4: Physical Security Monitoring

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.7.4-5-11-S1 |
| **Version** | 1.0 |
| **Assessment Area** | Physical Security Monitoring - Access Control, CCTV, Intrusion Detection |
| **Related Policy** | ISMS-POL-A.7.4-5-11, Section 2 (Physical Security Monitoring) |
| **Purpose** | Document deployed physical security monitoring systems, assess capabilities against policy requirements, and identify gaps |
| **Target Audience** | Security Operations, Facilities Management, IT Operations, Security Engineers, Compliance Officers, Auditors |
| **Assessment Type** | Technical & Operational |
| **Review Cycle** | Quarterly or After Major Infrastructure Changes |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Physical Monitoring assessment workbook | ISMS Implementation Team |

### Document Structure

This document consists of two parts:

- **PART I: USER COMPLETION GUIDE**
  - Assessment Overview
  - Prerequisites
  - Workflow
  - Completing Each Sheet
  - Evidence Collection
  - Common Pitfalls
  - Quality Checklist
  - Review & Approval

- **PART II: TECHNICAL SPECIFICATION**
  - Excel Workbook Structure
  - Sheet-by-Sheet Specifications
  - Cell Styling Reference
  - Integration Points


---

# PART I: USER COMPLETION GUIDE

## Assessment Overview

### Purpose & Scope

**Assessment Name:** ISMS-IMP-A.7.4-5-11-S1 - Physical Monitoring Assessment

#### What This Assessment Covers

This assessment documents the physical security MONITORING systems deployed in your facilities. This is the "WHAT monitoring systems do we have?" assessment that answers:

- What access control systems are deployed? (badge readers, access control panels, integration)
- What CCTV systems are deployed? (cameras, NVRs, coverage areas, recording capabilities)
- What intrusion detection systems are deployed? (sensors, alarm panels, monitoring)
- What security personnel and operations are in place? (guards, patrols, SOC)
- How are physical security systems integrated? (SIEM, dashboards, alerting)
- What incidents have occurred? (unauthorized access, intrusions, system failures)


#### Key Principle

This assessment is **completely vendor-agnostic and technology-independent**. You document YOUR specific systems (whatever you use - HID, Lenel, AMAG, Verkada, Milestone, Genetec, Honeywell, DSC, whatever), and verify capabilities against generic policy requirements from ISMS-POL-A.7.4-5-11, Section 2.

#### What You'll Document

**Access Control Systems:**

- Every access control system and controller in your environment
- Badge reader count and locations
- Access control panel configurations
- User count and access level definitions
- Integration with HR systems and SIEM


**CCTV Systems:**

- Every NVR/VMS and camera deployment
- Camera count, types, and coverage areas
- Recording capabilities and retention periods
- Storage capacity and backup configurations


**Intrusion Detection Systems:**

- Every alarm panel and sensor deployment
- Sensor types (motion, door/window, glass break)
- Arming zones and schedules
- Monitoring service or self-monitoring configuration


**Security Personnel:**

- Security guard schedules and duties
- Patrol routes and frequencies
- Daily security log practices
- Incident response capabilities


**System Integration:**

- SIEM integration status (log forwarding, event correlation)
- Dashboard deployments (real-time monitoring)
- Alerting configurations (email, SMS, alarm panel)


**Incidents and Performance:**

- Physical security incidents (unauthorized access, intrusions)
- System failures and downtime events
- False alarm rates and trends
- Response time metrics


#### How This Relates to Other A.7.4-5-11 Assessments

| Assessment            | Focus                  | Relationship to A.7.4-5-11-S1      |
|-----------------------|------------------------|------------------------------------|
| **ISMS-IMP-A.7.4-5-11-S1** | **Physical Monitoring** | **WHAT monitoring systems exist** |
| ISMS-IMP-A.7.4-5-11-S2 | Environmental Protection | Fire, flood, temperature protection systems |
| ISMS-IMP-A.7.4-5-11-S3 | Utility Resilience      | UPS, generators, HVAC, ISP systems |
| ISMS-IMP-A.7.4-5-11-S4 | Compliance Dashboard    | Consolidated view across all physical infrastructure |

This assessment (A.7.4-5-11-S1) focuses specifically on Control A.7.4 (Physical Security Monitoring). It complements assessments for A.7.5 (Environmental Protection) and A.7.11 (Utility Resilience).

### Who Should Complete This Assessment

#### Primary Stakeholders

1. **Security Operations Manager** - Overall physical security systems ownership
2. **Facilities Manager** - Physical infrastructure and vendor management
3. **IT Operations** - Network infrastructure for security systems, SIEM integration
4. **Security Engineers** - System architecture and technical configuration
5. **Compliance Officers** - Audit requirements and evidence collection

#### Required Skills

- Understanding of access control systems (badge readers, panels, software)
- Familiarity with CCTV systems (cameras, NVRs, recording configurations)
- Knowledge of intrusion detection systems (sensors, alarm panels)
- Understanding of facility criticality tiers (Tier 1 vs. Tier 2 requirements)
- Access to physical security system admin consoles


#### Time Commitment

- **Initial assessment:** 10-15 hours (comprehensive review of all systems across facilities)
- **Quarterly updates:** 2-4 hours (update incidents, performance metrics, minor configuration changes)


### Expected Outputs

Upon completion, you will have:

1. ✅ **Complete system inventory** - Every access control, CCTV, and intrusion detection system documented
2. ✅ **Coverage analysis** - Entry/exit point coverage, camera placement, sensor locations
3. ✅ **Capability assessment** - What each system can and cannot do
4. ✅ **Integration status** - SIEM integration, dashboard deployments, alerting configurations
5. ✅ **Incident tracking** - Physical security incidents and system failures documented
6. ✅ **Performance metrics** - Response times, false alarm rates, system uptime
7. ✅ **Gap analysis** - Identified gaps between deployed systems and policy requirements
8. ✅ **Evidence register** - Supporting documentation for audit
9. ✅ **Approved assessment** - Four-level approval workflow completed

---

## Prerequisites

### Information You'll Need

Before starting this assessment, gather:

#### 1. System Access

- Administrator access to all access control systems (panels, cloud portals)
- Administrator access to all CCTV systems (NVRs, VMSs)
- Administrator access to all intrusion detection systems (alarm panels)
- Access to security personnel schedules and daily logs
- Access to incident management system (physical security incidents)


#### 2. Documentation

- Facility floor plans with security system layouts
- Access control system configuration documentation
- CCTV camera placement maps
- Intrusion detection sensor placement maps
- Network diagrams (security system network topology)
- Integration documentation (HR system integration, SIEM integration)


#### 3. Historical Data

- Access control logs (last 90 days minimum)
- CCTV storage utilization reports
- Intrusion detection alarm logs (last 90 days minimum)
- Physical security incident reports (last 12 months)
- System maintenance records
- Security guard logs (if applicable)


#### 4. Policy Requirements

- ISMS-POL-A.7.4-5-11, Section 2 (Physical Security Monitoring Requirements)
  - Section 2.1: Access Control and Monitoring
  - Section 2.2: Physical Intrusion Detection
  - Section 2.3: Video Surveillance (CCTV)
  - Section 2.4: Security Personnel and Operations
  - Section 2.5: Integration with Security Operations


### Required Tools

- Microsoft Excel (2016 or later) for workbook completion
- Access to access control admin consoles (HID, Lenel, Verkada, etc.)
- Access to CCTV admin consoles (Milestone, Genetec, Verkada, etc.)
- Access to intrusion detection admin consoles (Honeywell, DSC, Bosch, etc.)
- Network monitoring tools (verify SIEM integration)
- Screen capture tools (for evidence screenshots)


### Dependencies

This assessment has NO dependencies on other assessments - it can be completed independently.

However, outputs from this assessment are INPUT to:

- ISMS-IMP-A.7.4-5-11-S4 (Compliance Dashboard) - Consolidates physical monitoring with environmental and utility assessments
- SIEM integration assessment (if separate SIEM assessment exists)


---

## Workflow

### High-Level Process

```
1. PREPARE
   ↓
2. INVENTORY SYSTEMS (Sheet 2: Access Control, Sheet 3: CCTV, Sheet 4: Intrusion Detection)
   ↓
3. ASSESS COVERAGE (Entry/exit points, camera placements, sensor locations)
   ↓
4. DOCUMENT INTEGRATION (SIEM, dashboards, alerting)
   ↓
5. REVIEW INCIDENTS (Sheet 5: Incidents - last 12 months)
   ↓
6. COLLECT EVIDENCE (Sheet 7: Evidence Register)
   ↓
7. REVIEW SUMMARY (Sheet 6: Summary Dashboard - automated scoring)
   ↓
8. QUALITY CHECK (Self-assessment against checklist)
   ↓
9. OBTAIN APPROVALS (Sheet 8: Approval Sign-Off)
   ↓
10. SUBMIT FOR AUDIT
```

### Detailed Step-by-Step

**Step 1: Preparation (Day 1 - 2 hours)**

- Read this Part I User Guide completely
- Review ISMS-POL-A.7.4-5-11, Section 2 requirements
- Gather all prerequisites (system access, documentation, historical data)
- Schedule time with Security Operations Manager and Facilities Manager
- Download or generate assessment workbook (Excel file)


**Step 2: System Inventory (Day 1-2 - 4-6 hours)**

- Open assessment workbook
- Complete Sheet 1 (Instructions & Legend) - organization info, assessment date
- Complete Sheet 2 (Access Control) - inventory all badge readers, panels, users
- Complete Sheet 3 (CCTV) - inventory all cameras, NVRs, coverage areas
- Complete Sheet 4 (Intrusion Detection) - inventory all sensors, alarm panels, zones
- Document integration status (HR system, SIEM, dashboards)


**Step 3: Coverage Analysis (Day 2-3 - 3-4 hours)**

- Verify entry/exit point coverage (access control + CCTV at all entrances)
- Verify server room coverage (access control + CCTV + intrusion detection)
- Verify restricted area coverage (access levels properly configured)
- Identify blind spots (areas without monitoring)
- Document gaps in Sheet 2, 3, 4 notes


**Step 4: Integration Assessment (Day 3 - 2-3 hours)**

- Verify SIEM integration (log forwarding active, events visible in SIEM)
- Verify dashboard deployments (real-time monitoring available)
- Verify alerting configurations (email, SMS, alarm panel notifications)
- Test sample integration (trigger alarm, verify SIEM receives event)
- Document integration status in respective sheets


**Step 5: Incident Review (Day 4 - 2 hours)**

- Query incident management system for physical security incidents (last 12 months)
- Complete Sheet 5 (Incidents) for each incident
- Classify incidents (Critical, High, Medium, Low per ISMS-POL-A.7.4-5-11, Section 5.4)
- Document response times and resolution status
- Identify trends (repeat incident types, common causes)


**Step 6: Evidence Collection (Day 4-5 - 2-3 hours)**

- Take screenshots of system configurations (access control, CCTV, intrusion detection)
- Export sample access logs (last 7 days)
- Export sample CCTV footage (verify recording and retention)
- Export sample intrusion detection alarm logs (last 30 days)
- Document evidence in Sheet 7 (Evidence Register)
- Store evidence files in secure location


**Step 7: Summary Review (Day 5 - 1 hour)**

- Review Sheet 6 (Summary Dashboard) - formulas automatically calculate compliance scores
- Verify compliance scores accurate (cross-check against detailed sheets)
- Identify areas below threshold (red or amber status)
- Prepare gap remediation plan for non-compliant areas


**Step 8: Quality Check (Day 5 - 1 hour)**

- Complete self-assessment using Quality Checklist (see section below)
- Verify all required fields completed
- Verify evidence register complete
- Verify formulas calculating correctly


**Step 9: Obtain Approvals (Day 6-10 - asynchronous)**

- Complete Sheet 8 (Approval Sign-Off) - Level 1: Assessor (you)
- Submit to Level 2: Security Operations Manager for review and approval
- After Level 2 approval, submit to Level 3: CISO for review and approval
- After Level 3 approval, submit to Level 4: Compliance Officer for final sign-off
- Document approval dates and any feedback


**Step 10: Submit for Audit (Post-Approval)**

- Assessment workbook is now audit-ready
- Provide to Internal Audit or External Auditors
- Evidence register provides traceability to supporting documentation


---

## Completing Each Sheet

### Sheet 1: Instructions & Legend

**Purpose:** Assessment metadata and legend for status indicators

**What to Complete:**

- **Document Information** (Rows 4-11):
  - Assessment Date: Date you started this assessment
  - Completed By: Your name and role
  - Organization: [Organization] name
  - Leave other fields as-is (Document ID, Version, etc.)

- **Status Legend** (Rows 14-17):
  - Read-only reference - understand color coding:
    - Green (✅ Compliant): Meets all policy requirements
    - Amber (⚠️ Partial): Meets some requirements, gaps identified
    - Red (❌ Non-Compliant): Does not meet requirements, immediate action needed


**Time Required:** 5 minutes

### Sheet 2: Access Control

**Purpose:** Document all access control systems, badge readers, access levels, and integration

**Structure:** 100 data rows for documenting multiple facilities/systems

**What to Document (Per Facility or System):**

**Column A - Facility/System Name:**

- Example: "Building A - Main Campus", "Datacenter 1", "Branch Office - Denver"


**Column B - Access Control System:**

- Vendor and model: "HID VertX V2000", "Lenel OnGuard", "Verkada Cloud Access"
- If multiple systems, create separate rows per system


**Column C - Controller Count:**

- Number of access control panels/controllers: 1, 2, 5, etc.


**Column D - Reader Count:**

- Total number of badge readers (doors with access control): 10, 25, 50, etc.


**Column E - Badge Technology:**

- Reader type: "HID Prox 125kHz", "HID iCLASS SE", "Mobile (Bluetooth)", "Biometric", etc.


**Column F - User Count:**

- Total number of users in system (employees, contractors with badges): 50, 200, 1000, etc.


**Column G - Access Levels Defined:**

- Number of access levels configured: "4 (Public, Office, Restricted, Highly Sensitive)"


**Column H - HR Integration:**

- Dropdown: "Yes - Automated" (badge auto-provisioned/revoked on hire/term), "Partial - Manual sync", "No"


**Column I - SIEM Integration:**

- Dropdown: "Yes - Real-time" (log forwarding active), "Partial - Batch", "No"


**Column J - Anti-Passback:**

- Dropdown: "Yes", "No", "N/A"
- Note: Required for critical facilities (Tier 1)


**Column K - Access Log Retention (Days):**

- Days of access logs retained: 365 (Tier 1), 90 (Tier 2), etc.
- Policy requirement: 365 days (Tier 1), 90 days (Tier 2) minimum


**Column L - Last Access Review:**

- Date of last quarterly access review (verify user access rights)


**Column M - Compliance Status:**

- Formula auto-calculates based on requirements:
  - Green (✅): Meets all requirements (HR integration, SIEM integration, retention, access review)
  - Amber (⚠️): Meets most requirements, minor gaps
  - Red (❌): Major gaps, non-compliant


**Column N - Notes:**

- Any additional context: "Upgrading to iCLASS SE Q2 2026", "SIEM integration pending network upgrade"


**Common Entries:**

- One row per facility if single access control system
- Multiple rows if multiple disparate systems (e.g., Building A has HID, Building B has Lenel)
- Colocation facilities: Note shared responsibility (provider manages building access, you manage cage access)


**Time Required:** 30-60 minutes for comprehensive inventory across all facilities

### Sheet 3: CCTV

**Purpose:** Document all CCTV systems, cameras, coverage areas, recording capabilities, and retention

**Structure:** 100 data rows for documenting multiple NVR/VMS deployments and camera groups

**What to Document (Per NVR/VMS or Camera Group):**

**Column A - Facility/System Name:**

- Example: "Building A - Main Campus", "Datacenter 1 - Perimeter Cameras", "Branch Office - Denver"


**Column B - NVR/VMS System:**

- Vendor and model: "Milestone XProtect Corporate", "Genetec Security Center", "Verkada Cloud", "Hanwha Wave"


**Column C - Camera Count:**

- Total number of cameras on this NVR/VMS: 10, 50, 200, etc.


**Column D - Camera Types:**

- Mix of camera types: "Fixed (20), PTZ (5), Fisheye (2)", "All Fixed IP", etc.


**Column E - Resolution:**

- Predominant resolution: "1080p (2MP)", "4K (8MP)", "Mix 720p/1080p"
- Policy requirement: Minimum 1080p for critical areas


**Column F - Recording Mode:**

- Dropdown: "Continuous 24/7", "Motion-triggered", "Scheduled", "Mix"
- Note: Continuous required for critical areas (entrances, server rooms)


**Column G - Retention Period (Days):**

- Days of footage retained: 90 (Tier 1), 30 (Tier 2), etc.
- Policy requirement: 90 days (Tier 1), 30 days (Tier 2) minimum


**Column H - Storage Capacity (TB):**

- Total storage capacity for this NVR/VMS: 2 TB, 10 TB, 50 TB, etc.


**Column I - Storage Utilization (%):**

- Current storage usage: 60%, 85%, etc.
- Alert if >90% (insufficient capacity for retention)


**Column J - Coverage Areas:**

- Areas covered by cameras: "All entrances, server room, parking", "Perimeter, loading dock", etc.


**Column K - Blind Spots:**

- Areas NOT covered but should be: "Rear exit blind spot", "Server room no coverage", "None identified"


**Column L - Low-Light Capable:**

- Dropdown: "Yes - IR illumination", "Yes - Low-light sensor", "No"
- Note: Required for 24/7 monitoring


**Column M - Redundant Storage:**

- Dropdown: "Yes - RAID", "Yes - Cloud backup", "No"
- Note: Recommended for critical facilities


**Column N - Compliance Status:**

- Formula auto-calculates based on requirements:
  - Green (✅): Meets coverage, resolution, retention, storage requirements
  - Amber (⚠️): Minor gaps (e.g., some blind spots identified)
  - Red (❌): Major gaps (insufficient retention, critical area no coverage)


**Column O - Notes:**

- Any additional context: "Upgrading to 4K cameras Q3 2026", "Blind spot remediation planned"


**Common Entries:**

- One row per NVR/VMS deployment
- For large facilities, may have multiple rows (e.g., "Datacenter 1 - Interior Cameras", "Datacenter 1 - Perimeter Cameras")
- Document all coverage gaps identified during facility walk-through


**Time Required:** 45-75 minutes for comprehensive CCTV inventory and coverage analysis

### Sheet 4: Intrusion Detection

**Purpose:** Document all intrusion detection systems, sensors, alarm panels, arming zones, and monitoring

**Structure:** 100 data rows for documenting multiple alarm panels and sensor deployments

**What to Document (Per Facility or Alarm Panel):**

**Column A - Facility/System Name:**

- Example: "Building A - Main Campus", "Datacenter 1", "Branch Office - Denver"


**Column B - Alarm Panel System:**

- Vendor and model: "Honeywell Vista 128BPT", "DSC PowerSeries Neo", "Bosch B Series", "2GIG GC3"


**Column C - Sensor Count:**

- Total number of sensors (motion, door/window, glass break): 25, 50, 100, etc.


**Column D - Sensor Types:**

- Breakdown by type: "Motion (15), Door/Window (30), Glass Break (5)", "All Motion PIR", etc.


**Column E - Zone Count:**

- Number of arming zones configured: 3 (Perimeter, Server Room, Office), 5, etc.
- Note: Zones allow partial arming (arm perimeter while office occupied)


**Column F - Coverage Areas:**

- Areas protected by intrusion detection: "All perimeter doors, ground floor windows, server room", "Perimeter only"


**Column G - Arming Schedule:**

- When system is armed: "24/7 (perimeter + server room)", "After hours 6PM-7AM", "Manual only"
- Policy requirement: 24/7 for critical facilities


**Column H - Monitoring Service:**

- Dropdown: "Yes - Professional monitoring center", "Yes - Self-monitoring (SOC)", "No"
- Note: Professional or self-monitoring required, "No" is non-compliant


**Column I - Backup Communication:**

- Dropdown: "Yes - Cellular", "Yes - Dual path (Ethernet + Cellular)", "No - Ethernet only"
- Note: Backup communication recommended for critical facilities


**Column J - False Alarm Rate (per month):**

- Average false alarms per month: 2, 5, 10, etc.
- Policy requirement: <5 false alarms per month target


**Column K - Last Testing Date:**

- Date of last monthly sensor testing (walk test): "15.12.2025", etc.
- Policy requirement: Monthly testing


**Column L - Compliance Status:**

- Formula auto-calculates based on requirements:
  - Green (✅): Meets coverage, arming schedule, monitoring, testing requirements
  - Amber (⚠️): Minor gaps (e.g., false alarm rate slightly above target)
  - Red (❌): Major gaps (no monitoring, testing overdue, critical areas not covered)


**Column M - Notes:**

- Any additional context: "Upgrading to wireless sensors Q1 2026", "False alarms due to HVAC (remediation planned)"


**Common Entries:**

- One row per alarm panel deployment
- Separate rows if multiple alarm panels in single facility (e.g., main building alarm panel, server room alarm panel)
- Document excessive false alarms and root cause if known


**Time Required:** 30-45 minutes for intrusion detection inventory and testing verification

### Sheet 5: Incidents

**Purpose:** Document all physical security incidents from last 12 months for trend analysis

**Structure:** 100 data rows for incident logging

**What to Document (Per Incident):**

**Column A - Incident ID:**

- Unique incident identifier from incident management system: "INC-2025-0042", "PS-2025-12-15-001"


**Column B - Incident Date:**

- Date incident occurred: "15.12.2025"


**Column C - Incident Type:**

- Dropdown: "Unauthorized Access", "Intrusion Alarm", "Tailgating", "Lost/Stolen Badge", "System Failure", "Other"


**Column D - Facility/Location:**

- Where incident occurred: "Building A - Main Entrance", "Datacenter 1 - Server Room", etc.


**Column E - Severity:**

- Dropdown: "Critical", "High", "Medium", "Low"
- Use ISMS-POL-A.7.4-5-11, Section 5.4 classification criteria


**Column F - Description:**

- Brief description: "Unauthorized access attempt to server room, badge denied, person tailgated authorized employee"


**Column G - Detection Method:**

- How incident was detected: "Access control alarm", "CCTV review", "Security guard patrol", "Employee report"


**Column H - Response Time (Minutes):**

- Minutes from detection to security personnel on-site: 5, 10, 15, etc.
- Policy target: <5 min (Tier 1), <15 min (Tier 2)


**Column I - Resolution Status:**

- Dropdown: "Resolved", "In Progress", "Escalated"


**Column J - Root Cause:**

- Identified cause: "Employee forgot badge, tailgated", "System malfunction - door sensor failed", "False alarm - HVAC airflow"


**Column K - Corrective Action:**

- Actions taken: "Employee training on tailgating policy", "Replaced door sensor", "Adjusted motion sensor sensitivity"


**Column L - Notes:**

- Any additional context


**Common Entries:**

- One row per incident
- Include both genuine incidents AND significant false alarms (for trend analysis)
- Focus on last 12 months (365 days)
- Extract from incident management system or security guard daily logs


**Time Required:** 1-2 hours depending on incident volume (if 20-50 incidents in last year)

**Analysis:**

- After completing all incidents, review trends:
  - Most common incident types (tailgating, false alarms, system failures)
  - Facilities with highest incident count
  - Response time performance (meeting targets?)
  - Common root causes requiring systemic fixes


### Sheet 6: Summary Dashboard

**Purpose:** Automated compliance scoring and overall physical monitoring health

**Structure:** Dashboard with formulas auto-calculating from Sheets 2-5

**What to Review (Auto-Calculated - Read-Only):**

**Overall Compliance Score:**

- Formula aggregates compliance from Access Control, CCTV, Intrusion Detection
- Displayed as percentage: 92%, 78%, etc.
- Thresholds: >90% (Green - Excellent), 75-89% (Amber - Good), 60-74% (Amber - Acceptable), <60% (Red - Non-Compliant)


**Access Control Score:**

- Percentage of facilities meeting all access control requirements
- Based on: HR integration, SIEM integration, retention compliance, access review current


**CCTV Score:**

- Percentage of facilities meeting all CCTV requirements
- Based on: Coverage compliance, resolution adequate, retention compliance, storage sufficient


**Intrusion Detection Score:**

- Percentage of facilities meeting all intrusion detection requirements
- Based on: Coverage compliant, arming schedule correct, monitoring active, testing current


**Incident Metrics:**

- Total incidents (last 12 months)
- Critical/High incident count
- Average response time
- Response time compliance (% meeting target)


**Key Trends:**

- Charts showing monthly incident trends
- False alarm rate trends
- System availability/uptime


**Gap Summary:**

- Auto-generated list of non-compliant items requiring remediation
- Prioritized by severity (Critical → High → Medium → Low)


**What YOU Do:**

- Review dashboard after completing Sheets 2-5
- Verify auto-calculations appear correct
- Investigate any unexpected red/amber status
- Prepare remediation plan for gaps identified
- NO manual data entry in this sheet (formulas auto-populate from other sheets)


**Time Required:** 15-30 minutes for review and interpretation

### Sheet 7: Evidence Register

**Purpose:** Document all supporting evidence for audit traceability

**Structure:** Evidence log with links to actual evidence files

**What to Document (Per Evidence Item):**

**Column A - Evidence ID:**

- Unique identifier: "EVID-001", "EVID-002", etc.


**Column B - Evidence Type:**

- Dropdown: "Screenshot", "Configuration Export", "Log Sample", "Report", "Document", "Photo"


**Column C - Description:**

- What evidence shows: "Access control system configuration - Building A", "Sample access logs 01-07.01.2026"


**Column D - Related Sheet/Item:**

- Links evidence to assessment: "Sheet 2, Row 5 (Building A Access Control)", "Sheet 5, Incident INC-2025-0042"


**Column E - File Name:**

- Evidence filename: "BuildingA_AccessControl_Config_20260115.png", "AccessLogs_Sample_20260101-07.csv"


**Column F - File Location:**

- Where evidence stored: "SharePoint > ISMS > Assessments > A.7.4.1 > Evidence", "Network Drive \\server\share\evidence"


**Column G - Collection Date:**

- When evidence collected: "15.01.2026"


**Column H - Collected By:**

- Who collected evidence: "John Smith - Security Operations"


**Column I - Retention Period:**

- How long to retain: "3 years", "Permanent", "Until next assessment"


**Column J - Notes:**

- Any additional context


**Common Evidence to Collect:**

1. **Access Control System:**

   - Screenshot of system dashboard (show system name, version, controller count)
   - Screenshot of access level configuration
   - Screenshot of HR system integration settings
   - Screenshot of SIEM log forwarding configuration
   - Sample access log export (CSV, 7 days of data)


2. **CCTV System:**

   - Screenshot of NVR/VMS dashboard (show camera count, storage capacity)
   - Facility map with camera placements marked
   - Screenshot of retention settings
   - Sample video clip (verify recording quality and retention)


3. **Intrusion Detection:**

   - Screenshot of alarm panel configuration (zones, arming schedule)
   - Facility map with sensor placements marked
   - Screenshot of monitoring service configuration
   - Sample alarm log export (30 days of data)


4. **Incidents:**

   - Incident reports from incident management system
   - CCTV footage of incident (if applicable)
   - Security guard logs mentioning incident


5. **Integration:**

   - Screenshot of SIEM showing physical security events
   - Screenshot of physical security dashboard
   - Configuration documents for integration


**Time Required:** 2-3 hours for comprehensive evidence collection and documentation

**Storage Best Practices:**

- Use consistent file naming: [Facility]_[System]_[Type]_[Date].ext
- Organize in folders by sheet: Evidence/Sheet2_AccessControl/, Evidence/Sheet3_CCTV/, etc.
- Encrypt sensitive evidence (access logs contain user data)
- Backup evidence to secure location (required for audit)


### Sheet 8: Approval Sign-Off

**Purpose:** Four-level approval workflow for assessment completion

**Structure:** Approval table with dates and signatures

**Approval Levels:**

**Level 1: Assessor (You)**

- Role: Assessment Completed By
- Name: [Your name]
- Date: Date you completed quality check and ready for submission
- Signature/Confirmation: Your initials or digital signature


**Level 2: Security Operations Manager**

- Role: Technical Review and Approval
- Name: [Security Operations Manager name]
- Date: Date Security Operations Manager reviewed and approved
- Comments: Any feedback or required corrections


**Level 3: CISO**

- Role: Executive Review and Approval
- Name: [CISO name]
- Date: Date CISO reviewed and approved
- Comments: Strategic feedback or resource allocation needs


**Level 4: Compliance Officer**

- Role: Final Audit Readiness Sign-Off
- Name: [Compliance Officer name]
- Date: Date Compliance Officer certified assessment audit-ready
- Comments: Audit preparation feedback


**What YOU Do:**

- Complete Level 1 (Assessor) - date and sign
- Submit assessment workbook to Level 2 (Security Operations Manager)
- After Level 2 approval, flows to Level 3 (CISO)
- After Level 3 approval, flows to Level 4 (Compliance Officer)
- Track approval workflow progress


**Time Required:** 5 minutes for Level 1 completion, then asynchronous for Levels 2-4

**Approval Timeline:**

- Target: 5-10 business days for all four levels
- If corrections required at any level, assessor addresses and resubmits


---

## Evidence Collection

### What Evidence to Collect

**Purpose:** Provide audit trail and verification of assessment accuracy

**Evidence Categories:**

**1. System Configuration Evidence**

- Access control system configuration (access levels, user count, integration settings)
- CCTV system configuration (camera count, retention settings, storage capacity)
- Intrusion detection system configuration (zones, arming schedules, monitoring)
- Screenshot format preferred (shows system interface, date/time, your login)


**2. Log Samples**

- Access control logs (7-30 days sample showing typical activity)
- CCTV storage reports (verify retention compliance)
- Intrusion detection alarm logs (30 days sample)
- CSV or PDF export format acceptable


**3. Coverage Maps**

- Facility floor plans with access control readers marked
- Facility floor plans with CCTV cameras marked (with coverage cones)
- Facility floor plans with intrusion detection sensors marked
- PDF or image format


**4. Incident Documentation**

- Incident reports from incident management system
- CCTV footage of incidents (if applicable and available)
- Security guard daily logs showing incident response
- Root cause analysis documents
- Corrective action tracking


**5. Integration Verification**

- SIEM screenshots showing physical security events
- Dashboard screenshots showing real-time monitoring
- Integration architecture diagrams
- Configuration files (syslog forwarding, API integration)


**6. Testing Records**

- Monthly intrusion detection testing logs
- Quarterly access control testing logs
- Annual comprehensive testing reports
- Professional inspection reports (fire alarm, intrusion detection)


### How to Collect Evidence

**Best Practices:**

**Screenshots:**

- Use full-screen capture (shows complete system interface)
- Include date/time in screenshot (system clock visible or OS taskbar)
- Include your login/username (proves you have access and when captured)
- Annotate if needed (highlight specific settings, add text boxes)
- Save as PNG or JPEG
- File naming: [Facility]_[System]_[Description]_[Date].png


**Log Exports:**

- Export from native system (don't re-type into Excel)
- Include all relevant fields (user, door, timestamp, result for access logs)
- 7-30 day sample sufficient (don't export years of data)
- Save as CSV or PDF
- File naming: [System]_[LogType]_[StartDate]-[EndDate].csv


**Maps and Diagrams:**

- Use existing facility floor plans if available
- Mark access control readers, cameras, sensors clearly
- Use legend (different symbols for different device types)
- Include coverage cones for cameras (show field of view)
- Identify blind spots if any
- Save as PDF or high-resolution image
- File naming: [Facility]_[SystemType]_Coverage_Map_[Date].pdf


**Documents:**

- Incident reports: Export from incident management system or scan paper logs
- Testing records: Export from maintenance system or scan technician reports
- Save as PDF (preserves formatting)
- File naming: [DocumentType]_[Description]_[Date].pdf


### Evidence Storage

**Storage Location:**

- **Secure network share:** \\server\ISMS\Assessments\A.7.4.1_Physical_Monitoring\Evidence
- **SharePoint/Cloud:** SharePoint > ISMS > Assessments > A.7.4.1 > Evidence folder
- **Organized by sheet:** Evidence/Sheet2_AccessControl/, Evidence/Sheet3_CCTV/, Evidence/Sheet4_IntrusionDetection/, Evidence/Sheet5_Incidents/


**Access Control:**

- Evidence folder permissions: CISO, Security Operations Manager, Compliance Officer, Internal Audit (read-only)
- Encrypt sensitive evidence (access logs contain personal data)


**Retention:**

- Minimum: 3 years (typical audit requirement)
- Permanent: If evidence of significant incidents or major findings
- Delete after retention period (GDPR/data minimization)


**Backup:**

- Evidence backed up with regular network backups
- Critical evidence: Additional copy to offline storage (external drive, tape)


---

## Common Pitfalls

### Pitfall 1: Incomplete System Inventory

**Problem:** Only documenting primary facility, missing branch offices, colocation spaces, or temporary locations

**Impact:** Audit finding - incomplete assessment scope

**How to Avoid:**

- Create master facility list BEFORE starting assessment
- Include ALL locations where [Organization] has equipment or personnel
- For colocation: Document customer-managed controls (cage access control, equipment-level monitoring)
- For cloud-only organizations: Explicitly state "N/A - No on-premises infrastructure" in assessment


### Pitfall 2: Vendor-Specific Language

**Problem:** Using vendor product names instead of generic capabilities

**Example:** "We use HID VertX" vs. "Access control system with badge readers, cloud-based management"

**How to Avoid:**

- Focus on WHAT the system does, not just what product it is
- Assessor must understand policy requirements (generic) and map deployed systems to those requirements
- Document vendor/model for inventory, but assess against generic policy requirements


### Pitfall 3: Confusing "Deployed" vs. "Configured Correctly"

**Problem:** Documenting that system exists but not verifying it meets policy requirements

**Example:** "We have CCTV cameras" (but retention is 14 days, policy requires 30 days minimum)

**How to Avoid:**

- Read policy requirements FIRST (ISMS-POL-A.7.4-5-11, Section 2)
- For each system, check: Does this meet the requirement? (Yes/Partial/No)
- Document gaps in Notes column
- Status formula auto-flags non-compliance (red/amber), but YOU must verify requirements


### Pitfall 4: Stale Evidence

**Problem:** Using old screenshots or documents from 6-12 months ago

**Impact:** Evidence doesn't reflect current state, audit finding

**How to Avoid:**

- Collect evidence DURING assessment (not before, not long after)
- Date all evidence clearly (screenshot includes date, file name includes date)
- If assessment spans multiple weeks, collect evidence as you go (not all at once at end)
- Evidence Collection Date in Evidence Register must match screenshot date/file date


### Pitfall 5: Missing Coverage Gaps

**Problem:** Not performing physical walk-through, missing blind spots or uncovered areas

**Example:** Claiming "100% coverage" but rear exit has no camera, no access control

**How to Avoid:**

- Physical facility walk-through REQUIRED (don't just rely on documentation)
- Check every entrance/exit point against policy requirements (access control + CCTV required)
- Check every restricted area (server rooms, storage) for access control + intrusion detection
- Document blind spots honestly (gaps identified = opportunity for remediation, hidden gaps = audit finding)


### Pitfall 6: Ignoring Integration Failures

**Problem:** Documenting "SIEM integration configured" but not testing if it works

**Example:** Syslog forwarding enabled but SIEM not receiving events (firewall block, configuration error)

**How to Avoid:**

- TEST integration, don't just document configuration
- Trigger test event (badge swipe, alarm), verify event appears in SIEM within minutes
- If integration not working, status = "Partial" or "No", document issue in Notes
- Integration "configured" but not working = non-compliant


### Pitfall 7: Insufficient Incident Documentation

**Problem:** Only documenting Critical incidents, missing Medium/Low or false alarms

**Impact:** Incomplete trend analysis, missing systemic issues

**How to Avoid:**

- Document ALL physical security incidents from last 12 months (not just Critical/High)
- Include significant false alarms (e.g., weekly false alarms indicating system issue)
- False alarm rate is KEY metric (policy target: <5 per month)
- If no incidents in 12 months, explicitly state "Zero incidents in assessment period" (not just blank sheet)


### Pitfall 8: Copy-Paste Errors

**Problem:** Copying rows in Excel, forgetting to update facility name or specific data

**Example:** Row 5 says "Building A" but data is actually for "Building B"

**How to Avoid:**

- Enter data methodically, one facility at a time
- Cross-check facility name against system name in each row
- If using copy-paste for similar facilities, immediately update ALL fields in new row
- Have second person spot-check (Security Operations Manager review)


### Pitfall 9: Formula Corruption

**Problem:** Accidentally overwriting formula cells, breaking auto-calculations

**Example:** Compliance Status formula deleted, now shows blank instead of green/amber/red

**How to Avoid:**

- Summary Dashboard (Sheet 6) and Compliance Status columns are FORMULA CELLS - do not edit
- If formula appears broken, refer to Part II Technical Specification for correct formula
- If you must edit formula, save backup copy of workbook first
- Test formula after any changes (verify green/amber/red colors appear correctly)


### Pitfall 10: Approval Workflow Shortcuts

**Problem:** Skipping approval levels or obtaining approvals out of sequence

**Example:** Going straight to CISO without Security Operations Manager review

**How to Avoid:**

- Follow four-level approval workflow in order: Assessor → Security Ops Mgr → CISO → Compliance Officer
- Each level reviews AND signs (date + name)
- If corrections required, go back to assessor, fix, resubmit through workflow
- Incomplete approvals = assessment not audit-ready


---

## Quality Checklist

Before submitting for Level 2 approval (Security Operations Manager), complete this self-assessment:

### Sheet 1: Instructions & Legend

- [ ] Assessment Date completed
- [ ] Completed By (your name and role)
- [ ] Organization name filled in
- [ ] All document information reviewed


### Sheet 2: Access Control

- [ ] ALL facilities with access control systems documented (not just primary facility)
- [ ] Controller count and reader count accurate
- [ ] Badge technology specified for each system
- [ ] User count current (verified against system)
- [ ] Access levels defined and documented
- [ ] HR integration status accurate (verified, not assumed)
- [ ] SIEM integration status accurate (tested, not just configured)
- [ ] Access log retention verified (actual retention, not policy target)
- [ ] Last access review date within 90 days (or documented if overdue)
- [ ] Compliance status column showing green/amber/red (formulas working)
- [ ] Notes column completed for any amber/red status (explain gap)
- [ ] At least one facility documented (or explicitly state "No access control systems" if truly none)


### Sheet 3: CCTV

- [ ] ALL NVR/VMS systems documented (not just primary system)
- [ ] Camera count accurate for each system
- [ ] Camera types specified (Fixed, PTZ, Fisheye, etc.)
- [ ] Resolution verified (not assumed - check camera specs)
- [ ] Recording mode verified (continuous, motion, scheduled)
- [ ] Retention period verified (actual retention, check NVR settings)
- [ ] Storage capacity and utilization accurate (check NVR storage report)
- [ ] Coverage areas listed (entrances, server rooms, parking, etc.)
- [ ] Blind spots documented honestly (if any exist)
- [ ] Low-light capability verified (IR illumination present?)
- [ ] Redundant storage status accurate (RAID configured? Cloud backup?)
- [ ] Compliance status column showing green/amber/red (formulas working)
- [ ] Notes column completed for any amber/red status (explain gap)
- [ ] At least one NVR/VMS documented (or explicitly state "No CCTV systems" if truly none)


### Sheet 4: Intrusion Detection

- [ ] ALL alarm panels documented (not just primary panel)
- [ ] Sensor count accurate for each panel
- [ ] Sensor types specified (motion, door/window, glass break)
- [ ] Zone count accurate
- [ ] Coverage areas listed (perimeter, server rooms, restricted areas)
- [ ] Arming schedule verified (24/7, after-hours, manual)
- [ ] Monitoring service verified (professional monitoring center name, self-monitoring via SOC)
- [ ] Backup communication verified (cellular backup present?)
- [ ] False alarm rate calculated (average per month from last 90 days)
- [ ] Last testing date within 30 days (or documented if overdue)
- [ ] Compliance status column showing green/amber/red (formulas working)
- [ ] Notes column completed for any amber/red status (explain gap)
- [ ] At least one alarm panel documented (or explicitly state "No intrusion detection" if truly none)


### Sheet 5: Incidents

- [ ] ALL physical security incidents from last 12 months documented (not just Critical/High)
- [ ] Incident IDs match incident management system
- [ ] Incident dates accurate
- [ ] Incident types classified correctly
- [ ] Severities assigned per policy (Critical/High/Medium/Low)
- [ ] Descriptions clear and concise
- [ ] Detection methods documented
- [ ] Response times documented (minutes from detection to response)
- [ ] Resolution status current (Resolved, In Progress, Escalated)
- [ ] Root causes identified (not just "unknown")
- [ ] Corrective actions documented (what was done to prevent recurrence)
- [ ] If zero incidents: Explicitly documented "Zero physical security incidents in assessment period 01.01.2025-31.12.2025"


### Sheet 6: Summary Dashboard

- [ ] Overall Compliance Score displays (not blank, not error)
- [ ] Access Control Score displays
- [ ] CCTV Score displays
- [ ] Intrusion Detection Score displays
- [ ] Incident metrics display (total incidents, Critical/High count)
- [ ] Average response time calculated
- [ ] Gap summary auto-populates (lists non-compliant items)
- [ ] Review dashboard and verify scores appear reasonable
- [ ] Investigate any unexpected red status
- [ ] NO manual data entry in dashboard (formulas auto-populate from Sheets 2-5)


### Sheet 7: Evidence Register

- [ ] At least 10 evidence items documented (comprehensive evidence collection)
- [ ] Evidence types appropriate (screenshots, logs, maps, documents)
- [ ] Descriptions clear
- [ ] Evidence linked to specific sheets/items
- [ ] File names match actual files
- [ ] File locations accurate (evidence actually stored there)
- [ ] Collection dates recent (during assessment period, not stale)
- [ ] Collected by documented
- [ ] Retention periods assigned
- [ ] ALL evidence files actually exist in documented location (not just documented but not collected)


**Evidence Minimum Requirements:**

- [ ] Access control system configuration screenshot(s)
- [ ] Sample access log export
- [ ] CCTV system configuration screenshot(s)
- [ ] Facility map with camera placements
- [ ] Intrusion detection system configuration screenshot(s)
- [ ] Sample alarm log export
- [ ] At least one incident report (if any incidents occurred)
- [ ] SIEM integration screenshot (if integrated)


### Sheet 8: Approval Sign-Off

- [ ] Level 1 (Assessor) completed (your name, date, signature)
- [ ] Assessment ready for submission to Level 2 (Security Operations Manager)
- [ ] Assessment workbook saved with final data
- [ ] Evidence folder organized and complete


### Overall Quality

- [ ] No blank required fields (all yellow input cells completed or marked N/A if truly not applicable)
- [ ] No formula errors (#REF, #VALUE, #DIV/0 in any cell)
- [ ] Consistent facility naming across sheets (e.g., "Building A" not "Bldg A" or "Building 1")
- [ ] Dates in DD.MM.YYYY format consistently
- [ ] Compliance status colors working (green/amber/red visible)
- [ ] Notes columns used appropriately (explain gaps, not repeat data)
- [ ] Assessment tells complete story (auditor could understand physical monitoring without asking you questions)


### Final Checks Before Submission

- [ ] Spell check completed
- [ ] Grammar check completed
- [ ] Data accuracy spot-checked (sample rows cross-referenced against actual systems)
- [ ] Evidence files spot-checked (open 3-5 random evidence files, verify they contain what Evidence Register says)
- [ ] Second person review requested (have colleague spot-check for obvious errors)
- [ ] Assessment workbook saved in final location
- [ ] Evidence folder backed up


**If ALL checkboxes checked:** Assessment is ready for Level 2 approval (Security Operations Manager)  
**If ANY checkboxes unchecked:** Address gaps before submission

---

## Review & Approval

### Four-Level Approval Workflow

**Purpose:** Ensure assessment accuracy, completeness, and audit readiness through progressive review

**Approval Sequence:** Assessor → Security Operations Manager → CISO → Compliance Officer

### Level 1: Assessor (You)

**Role:** Assessment Completion and Initial Quality Check

**Responsibilities:**

- Complete all assessment sheets (Sheets 2-5)
- Collect all required evidence (Sheet 7)
- Perform self-assessment using Quality Checklist (above)
- Address any gaps identified in self-assessment
- Complete Level 1 approval in Sheet 8 (name, date, signature)


**Approval Criteria:**

- All required fields completed (no blank yellow cells unless truly N/A)
- Evidence collected and documented
- Quality checklist 100% checked
- Assessment tells complete story


**Timeline:** Complete before submitting to Level 2

### Level 2: Security Operations Manager

**Role:** Technical Review and Validation

**Responsibilities:**

- Review all system inventories for completeness (Sheets 2-4)
- Verify system counts accurate (compare to known deployments)
- Verify integration status accurate (SIEM integration working, dashboards deployed)
- Review incident documentation for completeness (Sheet 5)
- Spot-check evidence (open 5-10 evidence files, verify accurate)
- Review Summary Dashboard for reasonableness
- Provide feedback to Assessor if corrections needed
- Complete Level 2 approval in Sheet 8 (name, date, signature, comments)


**Approval Criteria:**

- Technical accuracy verified (system counts, configurations)
- Integration status confirmed (tested, not just assumed)
- Incidents documented appropriately
- Evidence supports assessment conclusions
- No major gaps requiring immediate correction


**Timeline:** 2-5 business days after receipt from Assessor

**If Corrections Required:**

- Document required corrections in Sheet 8 Comments
- Return to Assessor for corrections
- Assessor addresses feedback, resubmits for Level 2 re-review


### Level 3: CISO

**Role:** Executive Review and Resource Allocation

**Responsibilities:**

- Review Summary Dashboard (overall compliance score)
- Review gap summary (non-compliant items requiring remediation)
- Assess remediation resource requirements (budget, personnel, timeline)
- Prioritize gaps for remediation (critical gaps first)
- Approve remediation plan (or request revised plan)
- Complete Level 3 approval in Sheet 8 (name, date, signature, comments)


**Approval Criteria:**

- Overall compliance score acceptable (>60% minimum, prefer >75%)
- Critical gaps have remediation plans
- Resource requirements reasonable
- Assessment aligns with organizational risk tolerance
- No strategic concerns requiring escalation


**Timeline:** 2-5 business days after Level 2 approval

**If Strategic Concerns:**

- Document concerns in Sheet 8 Comments
- May request additional analysis or revised remediation plan
- May escalate to Executive Management if risk unacceptable


### Level 4: Compliance Officer

**Role:** Final Audit Readiness Certification

**Responsibilities:**

- Review assessment for audit readiness
- Verify evidence completeness (Evidence Register complete, files exist)
- Verify approval workflow complete (Levels 1-3 signed)
- Verify assessment format professional (no typos, consistent formatting)
- Confirm assessment meets ISO 27001:2022 Control A.7.4 requirements
- Certify assessment ready for internal/external audit
- Complete Level 4 approval in Sheet 8 (name, date, signature, comments)


**Approval Criteria:**

- Evidence complete and audit-ready
- Assessment professionally formatted
- All approval levels completed
- Assessment demonstrates compliance with policy requirements
- Assessment defensible in audit (auditor questions anticipated and addressed)


**Timeline:** 1-3 business days after Level 3 approval

**Post-Approval:**

- Assessment workbook finalized (no further edits without re-approval)
- Assessment stored in audit repository
- Assessment available to Internal Audit and External Auditors
- Assessment forms basis for Control A.7.4 compliance evidence


### Approval Workflow Best Practices

**Communication:**

- Email notification at each level transition
- Include assessment workbook as attachment
- Include evidence folder link
- Request estimated timeline for review


**Version Control:**

- File naming: ISMS-IMP-A.7.4.1_Access_Monitoring_YYYY-MM-DD_vX.xlsx
- Increment version after corrections: v1, v2, v3
- Final approved version: ISMS-IMP-A.7.4.1_Access_Monitoring_YYYY-MM-DD_FINAL.xlsx


**Tracking:**

- Use Sheet 8 Approval Sign-Off table to track progress
- Update approval dates as levels complete
- Document feedback in Comments column


**Corrections:**

- If corrections required at any level, return to Assessor
- Assessor makes corrections, increments version number
- Resubmit through workflow (start at level where corrections requested)
- Document what changed in version history


**Timeline Management:**

- Total approval timeline: 5-15 business days typical
- If urgent (e.g., imminent audit), request expedited review
- Coordinate approval schedules with approvers in advance


**Audit Submission:**

- After Level 4 approval, assessment is FINAL
- Provide to Internal Audit or External Auditors as requested
- Auditor questions routed to Assessor and Security Operations Manager
- Evidence files provided to auditors for verification


---

# PART II: TECHNICAL SPECIFICATION

## Excel Workbook Structure

### Workbook Overview

**File Name:** ISMS-IMP-A.7.4.1_Access_Monitoring_YYYYMMDD.xlsx

**Generation:** Automated via Python script (generate_a74_1_access_monitoring.py)

**Sheet Count:** 8 worksheets

**Data Capacity:** 100 data rows per assessment sheet (Sheets 2-5)

**Styling:** Navy blue headers, yellow input cells, conditional formatting for compliance status (green/amber/red)

### Sheet Organization

| Sheet # | Sheet Name | Purpose | Type | Row Count |
|---------|------------|---------|------|-----------|
| 1 | Instructions & Legend | Assessment metadata and status legend | Read-only Reference | ~30 rows |
| 2 | Access Control | Access control system inventory and compliance | Data Entry | 100 data rows |
| 3 | CCTV | CCTV system inventory and coverage assessment | Data Entry | 100 data rows |
| 4 | Intrusion Detection | Intrusion detection system inventory and testing | Data Entry | 100 data rows |
| 5 | Incidents | Physical security incident log (last 12 months) | Data Entry | 100 data rows |
| 6 | Summary Dashboard | Automated compliance scoring and metrics | Formula-driven | ~40 rows |
| 7 | Evidence Register | Supporting evidence documentation | Data Entry | 100 data rows |
| 8 | Approval Sign-Off | Four-level approval workflow | Data Entry | ~20 rows |

### Workbook Features

**Data Validation:**

- Dropdown lists for standardized input (Yes/No, Compliant/Partial/Non-Compliant, etc.)
- Date validation (valid date format)
- Numeric validation (retention days, camera count, etc.)


**Conditional Formatting:**

- Compliance Status columns: Green fill (✅ Compliant), Amber fill (⚠️ Partial), Red fill (❌ Non-Compliant)
- Summary Dashboard scores: Color-coded thresholds (>90% green, 75-89% amber, 60-74% amber, <60% red)
- Overdue dates highlighted (testing overdue, access review overdue)


**Formulas:**

- Summary Dashboard auto-calculates from Sheets 2-5
- Compliance Status formulas evaluate multiple criteria per row
- Aggregate metrics (totals, averages, percentages)


**Freeze Panes:**

- Row 1-3 frozen (header rows always visible)
- Column A frozen (facility name always visible when scrolling right)


**Column Widths:**

- Optimized for readability (facility names 25 chars, descriptions 40 chars, notes 50 chars)


**Print Settings:**

- Page orientation: Landscape
- Fit to page: 1 page wide (scroll height)
- Print titles: Header rows repeat on each page


---

## Sheet-by-Sheet Specifications

### Sheet 1: Instructions & Legend

**Purpose:** Assessment metadata, status legend, and completion instructions

**Structure:**

**Row 1:** Header

- Merged cells A1:G1
- Text: "ISMS-IMP-A.7.4.1 - Physical Access Monitoring Assessment\nISO/IEC 27001:2022 - Control A.7.4: Physical Security Monitoring"
- Style: Navy blue background, white bold text, 14pt, center-aligned


**Rows 3-11:** Document Information Table

- Column A: Labels (Document ID, Assessment Area, Related Policy, Version, Assessment Date, Completed By, Organization, Review Cycle)
- Column B: Values (pre-filled for read-only fields, blank yellow for user input)
- User input fields (yellow): Assessment Date, Completed By, Organization


**Rows 13-17:** Status Legend

- Column A: Status labels (✅ Compliant, ⚠️ Partial Compliance, ❌ Non-Compliant)
- Column B: Definitions
- Style: Color-coded backgrounds matching compliance colors (green, amber, red)


**Rows 19-30:** Completion Instructions

- Brief workflow summary
- Reference to Part I User Guide for detailed instructions
- Contact information for assessment support


**Cell Styling:**

- Headers: Navy blue background (#003366), white bold text
- Labels: Bold text, gray background (#D9D9D9)
- Input cells: Yellow background (#FFFFCC)
- Read-only cells: White background


### Sheet 2: Access Control

**Purpose:** Document all access control systems and assess compliance against policy requirements

**Header Row (Row 3):**

- Style: Gray background, bold text, center-aligned, freeze panes


**Columns:**

| Col | Field Name | Type | Width | Validation | Formula | Description |
|-----|------------|------|-------|------------|---------|-------------|
| A | Facility/System Name | Text | 25 | None | No | Facility or building name |
| B | Access Control System | Text | 30 | None | No | Vendor and model (HID, Lenel, Verkada, etc.) |
| C | Controller Count | Number | 12 | Integer >0 | No | Number of access control panels/controllers |
| D | Reader Count | Number | 12 | Integer >0 | No | Number of badge readers (doors) |
| E | Badge Technology | Text | 25 | None | No | Reader technology (HID Prox, iCLASS, Mobile, Biometric) |
| F | User Count | Number | 12 | Integer >0 | No | Total users in system |
| G | Access Levels Defined | Number | 12 | Integer >0 | No | Number of access levels configured |
| H | HR Integration | Dropdown | 18 | List | No | Yes - Automated / Partial - Manual / No |
| I | SIEM Integration | Dropdown | 18 | List | No | Yes - Real-time / Partial - Batch / No |
| J | Anti-Passback | Dropdown | 15 | List | No | Yes / No / N/A |
| K | Access Log Retention (Days) | Number | 15 | Integer >0 | No | Days of logs retained |
| L | Last Access Review | Date | 15 | Date | No | Date of last quarterly access review |
| M | Compliance Status | Formula | 18 | None | Yes | ✅ Compliant / ⚠️ Partial / ❌ Non-Compliant |
| N | Notes | Text | 50 | None | No | Additional context, gaps, remediation plans |

**Compliance Status Formula (Column M):**
```excel
=IF(AND(H2="Yes - Automated", I2="Yes - Real-time", K2>=90, (TODAY()-L2)<=90), "✅ Compliant",
   IF(OR(H2="No", I2="No", K2<30, (TODAY()-L2)>180), "❌ Non-Compliant",
   "⚠️ Partial"))
```

**Logic:**

- ✅ Compliant IF: HR integration automated AND SIEM integration real-time AND retention ≥90 days AND access review within 90 days
- ❌ Non-Compliant IF: HR integration "No" OR SIEM integration "No" OR retention <30 days OR access review >180 days overdue
- ⚠️ Partial: Everything else (meets some but not all requirements)


**Conditional Formatting:**

- Column M: Green background if "✅ Compliant", Amber if "⚠️ Partial", Red if "❌ Non-Compliant"


**Data Rows:** Rows 4-103 (100 data rows)

**Freeze Panes:** Row 3 (header) and Column A (facility name)

### Sheet 3: CCTV

**Purpose:** Document all CCTV systems and assess coverage and retention compliance

**Header Row (Row 3):**

- Style: Gray background, bold text, center-aligned, freeze panes


**Columns:**

| Col | Field Name | Type | Width | Validation | Formula | Description |
|-----|------------|------|-------|------------|---------|-------------|
| A | Facility/System Name | Text | 25 | None | No | Facility or NVR/VMS name |
| B | NVR/VMS System | Text | 30 | None | No | Vendor and model (Milestone, Genetec, Verkada, etc.) |
| C | Camera Count | Number | 12 | Integer >0 | No | Total cameras on this NVR/VMS |
| D | Camera Types | Text | 25 | None | No | Fixed, PTZ, Fisheye, Mix |
| E | Resolution | Text | 15 | None | No | 720p, 1080p, 4K, Mix |
| F | Recording Mode | Dropdown | 18 | List | No | Continuous 24/7 / Motion-triggered / Scheduled / Mix |
| G | Retention Period (Days) | Number | 15 | Integer >0 | No | Days of footage retained |
| H | Storage Capacity (TB) | Number | 15 | Float >0 | No | Total storage capacity |
| I | Storage Utilization (%) | Number | 15 | Integer 0-100 | No | Current storage usage percentage |
| J | Coverage Areas | Text | 30 | None | No | Areas covered (entrances, server rooms, parking, etc.) |
| K | Blind Spots | Text | 30 | None | No | Areas not covered but should be |
| L | Low-Light Capable | Dropdown | 18 | List | No | Yes - IR / Yes - Low-light sensor / No |
| M | Redundant Storage | Dropdown | 18 | List | No | Yes - RAID / Yes - Cloud backup / No |
| N | Compliance Status | Formula | 18 | None | Yes | ✅ Compliant / ⚠️ Partial / ❌ Non-Compliant |
| O | Notes | Text | 50 | None | No | Additional context, gaps, remediation plans |

**Compliance Status Formula (Column N):**
```excel
=IF(AND(G2>=30, I2<90, K2="None identified", L2<>"No"), "✅ Compliant",
   IF(OR(G2<14, I2>95, ISNUMBER(SEARCH("no coverage",K2))), "❌ Non-Compliant",
   "⚠️ Partial"))
```

**Logic:**

- ✅ Compliant IF: Retention ≥30 days AND storage utilization <90% AND no blind spots AND low-light capable
- ❌ Non-Compliant IF: Retention <14 days OR storage utilization >95% OR critical area no coverage
- ⚠️ Partial: Everything else


**Conditional Formatting:**

- Column N: Green background if "✅ Compliant", Amber if "⚠️ Partial", Red if "❌ Non-Compliant"
- Column I: Red background if >90% (storage critically full)


**Data Rows:** Rows 4-103 (100 data rows)

**Freeze Panes:** Row 3 (header) and Column A (facility name)

### Sheet 4: Intrusion Detection

**Purpose:** Document all intrusion detection systems and assess coverage, arming, and testing compliance

**Header Row (Row 3):**

- Style: Gray background, bold text, center-aligned, freeze panes


**Columns:**

| Col | Field Name | Type | Width | Validation | Formula | Description |
|-----|------------|------|-------|------------|---------|-------------|
| A | Facility/System Name | Text | 25 | None | No | Facility or alarm panel name |
| B | Alarm Panel System | Text | 30 | None | No | Vendor and model (Honeywell, DSC, Bosch, etc.) |
| C | Sensor Count | Number | 12 | Integer >0 | No | Total sensors (motion, door/window, glass break) |
| D | Sensor Types | Text | 30 | None | No | Breakdown by type (Motion: 15, Door/Window: 30, etc.) |
| E | Zone Count | Number | 12 | Integer >0 | No | Number of arming zones |
| F | Coverage Areas | Text | 30 | None | No | Areas protected (perimeter, server rooms, etc.) |
| G | Arming Schedule | Text | 25 | None | No | 24/7, After hours, Manual |
| H | Monitoring Service | Dropdown | 25 | List | No | Yes - Professional / Yes - Self (SOC) / No |
| I | Backup Communication | Dropdown | 20 | List | No | Yes - Cellular / Yes - Dual path / No |
| J | False Alarm Rate (/month) | Number | 15 | Integer ≥0 | No | Average false alarms per month |
| K | Last Testing Date | Date | 15 | Date | No | Date of last monthly testing |
| L | Compliance Status | Formula | 18 | None | Yes | ✅ Compliant / ⚠️ Partial / ❌ Non-Compliant |
| M | Notes | Text | 50 | None | No | Additional context, gaps, remediation plans |

**Compliance Status Formula (Column L):**
```excel
=IF(AND(H2<>"No", J2<=5, (TODAY()-K2)<=31), "✅ Compliant",
   IF(OR(H2="No", J2>10, (TODAY()-K2)>60), "❌ Non-Compliant",
   "⚠️ Partial"))
```

**Logic:**

- ✅ Compliant IF: Monitoring service active AND false alarm rate ≤5/month AND testing within 31 days
- ❌ Non-Compliant IF: No monitoring service OR false alarm rate >10/month OR testing >60 days overdue
- ⚠️ Partial: Everything else


**Conditional Formatting:**

- Column L: Green background if "✅ Compliant", Amber if "⚠️ Partial", Red if "❌ Non-Compliant"
- Column J: Red background if >10 (excessive false alarms)
- Column K: Red background if (TODAY()-K2)>31 (testing overdue)


**Data Rows:** Rows 4-103 (100 data rows)

**Freeze Panes:** Row 3 (header) and Column A (facility name)

### Sheet 5: Incidents

**Purpose:** Log all physical security incidents from last 12 months for trend analysis and response time tracking

**Header Row (Row 3):**

- Style: Gray background, bold text, center-aligned, freeze panes


**Columns:**

| Col | Field Name | Type | Width | Validation | Formula | Description |
|-----|------------|------|-------|------------|---------|-------------|
| A | Incident ID | Text | 18 | None | No | Unique incident identifier |
| B | Incident Date | Date | 15 | Date | No | Date incident occurred |
| C | Incident Type | Dropdown | 20 | List | No | Unauthorized Access / Intrusion Alarm / Tailgating / Lost Badge / System Failure / Other |
| D | Facility/Location | Text | 25 | None | No | Where incident occurred |
| E | Severity | Dropdown | 12 | List | No | Critical / High / Medium / Low |
| F | Description | Text | 40 | None | No | Brief incident description |
| G | Detection Method | Text | 25 | None | No | How detected (Access control alarm, CCTV, Guard patrol, etc.) |
| H | Response Time (Min) | Number | 15 | Integer ≥0 | No | Minutes from detection to response |
| I | Resolution Status | Dropdown | 15 | List | No | Resolved / In Progress / Escalated |
| J | Root Cause | Text | 30 | None | No | Identified cause |
| K | Corrective Action | Text | 40 | None | No | Actions taken to prevent recurrence |
| L | Notes | Text | 50 | None | No | Additional context |

**Conditional Formatting:**

- Column E: Red background if "Critical", Orange if "High", Yellow if "Medium", White if "Low"
- Column H: Red background if >15 minutes (response time target exceeded for standard facilities)


**Data Rows:** Rows 4-103 (100 data rows)

**Freeze Panes:** Row 3 (header) and Column A (incident ID)

**Summary Metrics (Auto-calculated in Sheet 6):**

- Total incidents (last 12 months)
- Critical/High incident count
- Average response time
- Most common incident types
- Facilities with highest incident count


### Sheet 6: Summary Dashboard

**Purpose:** Automated compliance scoring and key performance indicators

**Structure:** Dashboard layout with metrics and charts

**Row 1:** Header

- Merged cells A1:H1
- Text: "Physical Security Monitoring - Summary Dashboard"
- Style: Navy blue background, white bold text, 14pt, center-aligned


**Rows 3-10:** Overall Compliance Score

- Row 3: "Overall Compliance Score" label
- Row 4: Formula calculating aggregate score from Sheets 2-4
- Row 5: Color-coded status (Green >90%, Amber 75-89%, Amber 60-74%, Red <60%)


**Overall Compliance Score Formula:**
```excel
=(COUNTIF('Access Control'!M:M,"✅ Compliant")/COUNTA('Access Control'!M:M)*0.4 +
  COUNTIF(CCTV!N:N,"✅ Compliant")/COUNTA(CCTV!N:N)*0.3 +
  COUNTIF('Intrusion Detection'!L:L,"✅ Compliant")/COUNTA('Intrusion Detection'!L:L)*0.3)*100
```

**Weighting:** Access Control 40%, CCTV 30%, Intrusion Detection 30%

**Rows 12-20:** Domain Scores

- Access Control Compliance Score (%)
- CCTV Compliance Score (%)
- Intrusion Detection Compliance Score (%)
- Each with formula, percentage display, color-coding


**Rows 22-30:** Incident Metrics

- Total Incidents (last 12 months): `=COUNTA(Incidents!A:A)-1`
- Critical/High Incidents: `=COUNTIF(Incidents!E:E,"Critical")+COUNTIF(Incidents!E:E,"High")`
- Average Response Time (min): `=AVERAGE(Incidents!H:H)`
- Response Time Compliance (%): `=COUNTIF(Incidents!H:H,"<=15")/COUNTA(Incidents!H:H)*100`


**Rows 32-50:** Gap Summary

- Auto-generated list of non-compliant items
- Formula scans Sheets 2-4 for "❌ Non-Compliant" status
- Lists facility name, system type, gap description
- Prioritized by severity (Critical → High → Medium → Low)


**Gap Summary Formula (example for row 32):**
```excel
=IF(COUNTIF('Access Control'!M:M,"❌ Non-Compliant")>0,
   INDEX('Access Control'!A:A, MATCH("❌ Non-Compliant",'Access Control'!M:M,0)) & " - Access Control Gap",
   IF(COUNTIF(CCTV!N:N,"❌ Non-Compliant")>0,
      INDEX(CCTV!A:A, MATCH("❌ Non-Compliant",CCTV!N:N,0)) & " - CCTV Gap",
      "No Critical Gaps Identified"))
```

**Charts:**

- Chart 1: Overall Compliance Score (gauge chart)
- Chart 2: Domain Scores (bar chart - Access Control, CCTV, Intrusion Detection)
- Chart 3: Incident Trend (line chart - incidents per month, last 12 months)
- Chart 4: Incident Severity Distribution (pie chart - Critical, High, Medium, Low)


**Conditional Formatting:**

- Compliance scores: Green >90%, Amber 75-89%, Red <60%
- Gap summary: Red highlight for critical gaps, amber for high/medium gaps


### Sheet 7: Evidence Register

**Purpose:** Document all supporting evidence with audit traceability

**Header Row (Row 3):**

- Style: Gray background, bold text, center-aligned, freeze panes


**Columns:**

| Col | Field Name | Type | Width | Validation | Formula | Description |
|-----|------------|------|-------|------------|---------|-------------|
| A | Evidence ID | Text | 12 | None | No | Unique identifier (EVID-001, EVID-002, etc.) |
| B | Evidence Type | Dropdown | 18 | List | No | Screenshot / Config Export / Log Sample / Report / Document / Photo |
| C | Description | Text | 40 | None | No | What evidence shows |
| D | Related Sheet/Item | Text | 25 | None | No | Links to specific assessment row (Sheet 2, Row 5) |
| E | File Name | Text | 35 | None | No | Evidence filename |
| F | File Location | Text | 50 | None | No | Path to evidence file |
| G | Collection Date | Date | 15 | Date | No | When evidence collected |
| H | Collected By | Text | 25 | None | No | Who collected evidence |
| I | Retention Period | Text | 18 | None | No | 3 years, Permanent, etc. |
| J | Notes | Text | 50 | None | No | Additional context |

**Data Rows:** Rows 4-103 (100 data rows)

**Freeze Panes:** Row 3 (header) and Column A (evidence ID)

**Conditional Formatting:**

- Column G: Red background if >30 days old (stale evidence warning)


### Sheet 8: Approval Sign-Off

**Purpose:** Four-level approval workflow documentation

**Structure:**

**Row 1:** Header

- Merged cells A1:E1
- Text: "Assessment Approval Workflow"
- Style: Navy blue background, white bold text, 14pt, center-aligned


**Rows 3-20:** Approval Table

| Approval Level | Role | Name | Date | Signature/Confirmation | Comments |
|----------------|------|------|------|------------------------|----------|
| Level 1 | Assessor | [Input] | [Input] | [Input] | |
| Level 2 | Security Operations Manager | [Input] | [Input] | [Input] | [Input] |
| Level 3 | CISO | [Input] | [Input] | [Input] | [Input] |
| Level 4 | Compliance Officer | [Input] | [Input] | [Input] | [Input] |

**Cell Styling:**

- Level labels: Bold text, gray background
- Input cells: Yellow background (Name, Date, Signature, Comments)
- Instructions below table (rows 10-20): Workflow sequence, timeline expectations


---

## Cell Styling Reference

### Color Palette

**Headers:**

- Primary Header (Sheet titles, Row 1): #003366 (Navy blue background), #FFFFFF (White text)
- Subheader (Section titles): #4472C4 (Medium blue background), #FFFFFF (White text)
- Column Header (Row 3): #D9D9D9 (Light gray background), #000000 (Black text)


**Data Cells:**

- Input Cell (Yellow): #FFFFCC (Light yellow background) - indicates user should enter data
- Formula Cell (White): #FFFFFF (White background) - read-only, auto-calculated
- Read-Only Cell (Light gray): #F2F2F2 (Very light gray background) - pre-filled, do not edit


**Compliance Status:**

- Compliant: #C6EFCE (Light green background)
- Partial Compliance: #FFEB9C (Light amber/yellow background)
- Non-Compliant: #FFC7CE (Light red background)


**Alerts:**

- Warning (Amber): #FFEB9C (Light amber background)
- Critical (Red): #FFC7CE (Light red background)
- Success (Green): #C6EFCE (Light green background)


### Font Specifications

**Headers:**

- Font: Calibri
- Size: 14pt (primary header), 11pt (subheader), 10pt (column header)
- Weight: Bold
- Color: #FFFFFF (white) for primary/subheader, #000000 (black) for column header


**Data Cells:**

- Font: Calibri
- Size: 10pt
- Weight: Normal (regular for data, bold for labels)
- Color: #000000 (black)


**Status Text:**

- Font: Calibri
- Size: 10pt
- Weight: Bold
- Uses Unicode symbols: ✅ (U+2705), ⚠️ (U+26A0), ❌ (U+274C)


### Border Styles

**Table Borders:**

- Style: Thin solid line
- Color: #000000 (black)
- Applied to: All data table cells (Sheets 2-5, 7)


**Header Borders:**

- Style: Medium solid line (bottom border only)
- Color: #000000 (black)
- Applied to: Column header row (Row 3)


### Alignment

**Headers:**

- Horizontal: Center
- Vertical: Center
- Wrap text: Yes (for long header labels)


**Data Cells:**

- Text fields: Left-aligned, top-aligned
- Numeric fields: Right-aligned, top-aligned
- Date fields: Left-aligned, top-aligned
- Formula fields: Center-aligned (status indicators)


### Cell Protection

**Protected Cells (Formula cells):**

- Summary Dashboard (Sheet 6): All cells except approval override
- Compliance Status columns (Sheets 2-5): Formula-protected
- Header rows (Row 1-3 all sheets): Protected


**Unlocked Cells (Input cells):**

- All yellow background cells (user input required)
- Evidence Register (Sheet 7): All data cells
- Approval Sign-Off (Sheet 8): Name, Date, Signature, Comments cells


**Sheet Protection:**

- Password: [Organization-specific]
- Allow: Select unlocked cells, format cells (unlocked cells only)
- Disallow: Insert/delete rows, modify formulas, edit locked cells


---

## Integration Points

### Integration with Policy (ISMS-POL-A.7.4-5-11)

**Policy Section → Assessment Sheet Mapping:**

| Policy Section | Policy Reference | Assessment Sheet | Assessment Focus |
|----------------|------------------|------------------|------------------|
| Section 2.1: Access Control and Monitoring | ISMS-POL-A.7.4-5-11, §2.1 | Sheet 2: Access Control | Badge readers, access levels, HR/SIEM integration, log retention, access review |
| Section 2.3: Video Surveillance (CCTV) | ISMS-POL-A.7.4-5-11, §2.3 | Sheet 3: CCTV | Camera coverage, recording capabilities, retention, storage capacity, blind spots |
| Section 2.2: Physical Intrusion Detection | ISMS-POL-A.7.4-5-11, §2.2 | Sheet 4: Intrusion Detection | Sensors, alarm panels, arming schedules, monitoring service, false alarms, testing |
| Section 2.4: Security Personnel | ISMS-POL-A.7.4-5-11, §2.4 | Sheet 5: Incidents | Security guard logs reflected in incident documentation |
| Section 2.5: Integration | ISMS-POL-A.7.4-5-11, §2.5 | Sheets 2-4: Integration columns | SIEM integration, dashboard deployments, alerting configurations |
| Section 5.4: Incident Response | ISMS-POL-A.7.4-5-11, §5.4 | Sheet 5: Incidents | Incident classification, response times, resolution status |

**Assessment validates policy compliance by comparing deployed systems against policy requirements:**

- Policy states "SIEM integration SHALL be implemented" → Assessment verifies "Yes - Real-time" in Sheet 2, Column I
- Policy states "Retention 90 days minimum (Tier 1)" → Assessment verifies ≥90 days in Sheet 2, Column K
- Policy states "Response time <5 min (Tier 1)" → Assessment tracks actual response times in Sheet 5, Column H


### Integration with Other Assessments

**Feeds into:**

- ISMS-IMP-A.7.4-5-11-S4 (Compliance Dashboard): Overall compliance score, gap summary, incident metrics
- SIEM assessment (if separate): Physical security log integration status verified
- BC/DR assessment: Physical security incident data informs business continuity scenarios


**Dependencies from:**

- Facility inventory: List of all facilities requiring assessment (if master facility list exists)
- Network inventory: Network infrastructure supporting physical security systems (access control network, CCTV network)
- HR system inventory: Confirms HR system integration feasibility


**Shared evidence with:**

- Access Control assessment (if separate from physical monitoring): Badge reader deployments, access control logs
- Network security assessment: Network diagrams showing security system VLANs
- Incident management assessment: Physical security incidents cross-referenced


### Integration with Evidence Collection

**Evidence Register (Sheet 7) cross-references Assessment Sheets:**

- Evidence ID "EVID-005" → Related Sheet/Item: "Sheet 2, Row 5 (Building A Access Control)"
- File Name: "BuildingA_AccessControl_Config_20260115.png"
- Assessment Sheet 2, Row 5, Column N (Notes): "Evidence: EVID-005"


**Evidence Traceability:**
```
Assessment Finding (Sheet 2, Row 5) ← Evidence (EVID-005) ← Evidence File (BuildingA_AccessControl_Config_20260115.png)
```

**Audit Flow:**
1. Auditor reviews Sheet 2 (Access Control), identifies non-compliant item
2. Auditor checks Sheet 7 (Evidence Register) for supporting evidence ID
3. Auditor requests evidence file from File Location
4. Evidence file verifies or refutes assessment finding

### Integration with Audit Process

**Audit Deliverables:**
1. **Assessment Workbook:** ISMS-IMP-A.7.4.1_Access_Monitoring_YYYYMMDD_FINAL.xlsx (all sheets)
2. **Evidence Folder:** All files listed in Sheet 7 Evidence Register
3. **Approval Documentation:** Sheet 8 showing four-level approval workflow complete
4. **Gap Remediation Plan:** Derived from Sheet 6 Gap Summary (separate document or embedded in workbook)

**Auditor Review Process:**
1. Review Summary Dashboard (Sheet 6) for overall compliance score
2. Identify non-compliant areas (red status) in Sheets 2-4
3. Review Evidence Register (Sheet 7) for supporting evidence
4. Sample evidence files (verify 10-20% of evidence items)
5. Interview Security Operations Manager and Facilities Manager (validate assessment accuracy)
6. Test integration (trigger access control event, verify appears in SIEM)
7. Review physical facility (spot-check badge readers, cameras, sensors exist as documented)
8. Issue audit findings (if gaps identified) or confirm compliance

**Audit Questions Anticipated (Part I guides assessor to address proactively):**

- "How do you know camera count is accurate?" → Evidence: NVR screenshot showing camera list
- "How do you verify SIEM integration works?" → Evidence: SIEM screenshot showing access control events
- "What is your false alarm rate trend?" → Sheet 5 incidents include false alarms, trend shown in Sheet 6
- "Are all facilities documented?" → Sheet 2/3/4 comprehensive, or explicit "N/A" if facility truly has no systems


---

**END OF SPECIFICATION**

---

*"There must be no barriers to freedom of inquiry. There is no place for dogma in science."*
— J. Robert Oppenheimer
*Where bamboo antennas actually work.* 🎋
