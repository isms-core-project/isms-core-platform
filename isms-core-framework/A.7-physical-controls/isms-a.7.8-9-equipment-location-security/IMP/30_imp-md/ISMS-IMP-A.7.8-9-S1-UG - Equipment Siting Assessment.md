**ISMS-IMP-A.7.8-9-S1-UG - Equipment Siting Assessment**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.7.8: Equipment Siting and Protection

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.7.8-9-S1-UG |
| **Version** | 1.0 |
| **Assessment Area** | Equipment Siting - Location Assessment, Environmental Protection, Security Measures |
| **Related Policy** | ISMS-POL-A.7.8-9, Section 2.1 (Equipment Siting Requirements) |
| **Purpose** | Document equipment siting locations, assess environmental risks, evaluate physical security measures, and identify gaps |
| **Target Audience** | Facilities Management, IT Operations, Security Operations, Data Centre Managers, Compliance Officers, Auditors |
| **Assessment Type** | Technical & Operational |
| **Review Cycle** | Annual or After Major Infrastructure Changes |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Equipment Siting assessment workbook | ISMS Implementation Team |

### Document Structure

This is the **User Completion Guide**. The companion Technical Specification is documented in ISMS-IMP-A.7.8-9-S1-TG.

---

## Assessment Overview

### Purpose & Scope

**Assessment Name:** ISMS-IMP-A.7.8-9-S1 - Equipment Siting Assessment

#### What This Assessment Covers

This assessment documents the SITING of information processing equipment within your facilities. This is the "WHERE is equipment located and HOW is it protected?" assessment that answers:

- Where is information processing equipment physically located? (server rooms, network closets, office areas)
- What environmental risks exist at each location? (temperature, humidity, flood, fire, dust)
- What physical security measures protect each location? (access control, CCTV, locks)
- What power and cabling protection is in place? (UPS, surge protection, cable management)
- How are screens and workstations positioned? (shoulder surfing prevention, privacy screens)
- What segregation exists between organisation-owned and third-party equipment?

#### Key Principle

This assessment is **completely vendor-agnostic and facility-independent**. You document YOUR specific equipment locations (whatever you have - data centres, server rooms, network closets, co-location cages), and verify siting decisions against generic policy requirements from ISMS-POL-A.7.8-9, Section 2.1.

#### What You'll Document

**Equipment Location Inventory:**

- Every location where information processing equipment is sited
- Equipment type at each location (servers, network, storage, workstations)
- Environmental conditions at each location
- Access control measures protecting each location
- Criticality classification (Tier 1 critical, Tier 2 standard)

**Environmental Risk Assessment:**

- Temperature and humidity exposure
- Flood and water damage risk
- Fire risk and suppression systems
- Dust, vibration, and contamination exposure
- Electromagnetic interference exposure

**Physical Security Measures:**

- Access control systems (badge readers, biometrics, keys)
- CCTV coverage and monitoring
- Equipment locking and securing mechanisms
- Cable protection and routing
- Asset labelling and segregation

**Power and Infrastructure Protection:**

- UPS and backup power systems
- Surge and lightning protection
- Cable management and protection
- Emergency power-off (EPO) switches

**Screen and Workstation Positioning:**

- Privacy screen usage for sensitive displays
- Workstation positioning relative to windows and traffic
- Clear desk policy compliance
- Shoulder surfing prevention measures

#### How This Relates to Other A.7.8-9 Assessments

| Assessment            | Focus                  | Relationship to A.7.8-9-S1      |
|-----------------------|------------------------|---------------------------------|
| **ISMS-IMP-A.7.8-9-S1** | **Equipment Siting** | **WHERE equipment is located and protected** |
| ISMS-IMP-A.7.8-9-S2 | Off-Premises Assets | Equipment removed from premises or permanently off-site |
| ISMS-IMP-A.7.8-9-S3 | Compliance Dashboard | Consolidated view across all equipment siting and protection |

This assessment (A.7.8-9-S1) focuses specifically on Control A.7.8 (Equipment Siting and Protection). It complements the off-premises asset security assessment (A.7.9) in A.7.8-9-S2.

### Who Should Complete This Assessment

#### Primary Stakeholders

1. **Facilities Manager** - Overall facility and equipment siting ownership
2. **Data Centre Manager** - Server room and data centre equipment siting
3. **IT Operations** - Network and infrastructure equipment locations
4. **Security Operations** - Physical security measures and monitoring
5. **Compliance Officers** - Audit requirements and evidence collection

#### Required Skills

- Understanding of physical security principles (access control, CCTV, environmental monitoring)
- Familiarity with data centre best practices (hot/cold aisle, power distribution)
- Knowledge of environmental risks (temperature, humidity, water, fire)
- Understanding of equipment criticality classifications
- Access to facility floor plans and equipment inventories

#### Time Commitment

- **Initial assessment:** 8-12 hours (comprehensive review of all equipment locations)
- **Annual updates:** 3-4 hours (update changes, verify current state)

### Expected Outputs

Upon completion, you will have:

1. **Complete location inventory** - Every location where information processing equipment is sited
2. **Environmental risk assessment** - Identified risks at each location
3. **Physical security evaluation** - Security measures protecting each location
4. **Power protection assessment** - UPS, surge, and backup power coverage
5. **Screen positioning review** - Privacy and shoulder surfing prevention
6. **Gap analysis** - Identified gaps between current siting and policy requirements
7. **Evidence register** - Supporting documentation for audit
8. **Approved assessment** - Four-level approval workflow completed

---

## Prerequisites

### Information You'll Need

Before starting this assessment, gather:

#### 1. System Access

- Access to facility floor plans and building documentation
- Access to equipment inventory system (asset management)
- Access to physical security systems (access control logs, CCTV)
- Access to environmental monitoring systems (temperature, humidity)
- Access to power infrastructure documentation (UPS, PDU, generator)

#### 2. Documentation

- Facility floor plans with equipment locations marked
- Equipment inventory with criticality classifications
- Environmental monitoring data (last 90 days)
- Physical security incident reports (last 12 months)
- Power infrastructure diagrams (UPS zones, PDU locations)
- Access control zone definitions
- CCTV camera coverage maps

#### 3. Historical Data

- Environmental excursion logs (temperature, humidity out of range)
- Physical security incidents (unauthorised access attempts, tailgating)
- Power incidents (outages, UPS failures, generator tests)
- Equipment failures related to environmental conditions
- Near-miss events or security concerns

#### 4. Policy Requirements

- ISMS-POL-A.7.8-9, Section 2.1 (Equipment Siting Requirements)
  - Section 2.1.1: Location Selection
  - Section 2.1.2: Environmental Considerations
  - Section 2.1.3: Security Measures
  - Section 2.1.4: Power and Cabling Protection

### Required Tools

- Microsoft Excel (2016 or later) for workbook completion
- Access to facility floor plans (digital or physical)
- Camera/smartphone for evidence photographs
- Thermometer/hygrometer for environmental verification (optional)
- Screen capture tools (for evidence screenshots)

### Dependencies

This assessment has NO dependencies on other assessments - it can be completed independently.

However, outputs from this assessment are INPUT to:

- ISMS-IMP-A.7.8-9-S3 (Compliance Dashboard) - Consolidates equipment siting with off-premises asset security
- ISMS-IMP-A.7.4-5-11 (Physical Infrastructure) - Related environmental protection controls

---

## Workflow

### High-Level Process

```
1. PREPARE
   |
2. INVENTORY LOCATIONS (Sheet 2: Equipment Locations)
   |
3. ASSESS ENVIRONMENTAL RISKS (Sheet 3: Environmental Assessment)
   |
4. EVALUATE SECURITY MEASURES (Sheet 4: Physical Security)
   |
5. REVIEW POWER PROTECTION (Sheet 5: Power Infrastructure)
   |
6. ASSESS SCREEN POSITIONING (Sheet 6: Workstation Security)
   |
7. COLLECT EVIDENCE (Sheet 7: Evidence Register)
   |
8. REVIEW SUMMARY (Sheet 8: Summary Dashboard - automated scoring)
   |
9. QUALITY CHECK (Self-assessment against checklist)
   |
10. OBTAIN APPROVALS (Sheet 9: Approval Sign-Off)
    |
11. SUBMIT FOR AUDIT
```

### Detailed Step-by-Step

**Step 1: Preparation (Day 1 - 2 hours)**

- Read this Part I User Guide completely
- Review ISMS-POL-A.7.8-9, Section 2.1 requirements
- Gather all prerequisites (floor plans, equipment inventory, access logs)
- Schedule time with Facilities Manager and IT Operations
- Download or generate assessment workbook (Excel file)

**Step 2: Location Inventory (Day 1-2 - 3-4 hours)**

- Open assessment workbook
- Complete Sheet 1 (Instructions & Legend) - organisation info, assessment date
- Complete Sheet 2 (Equipment Locations) - inventory all locations with equipment
- Document equipment types, criticality, and access control at each location
- Physically walk through each location to verify accuracy

**Step 3: Environmental Risk Assessment (Day 2-3 - 2-3 hours)**

- Complete Sheet 3 (Environmental Assessment) for each location
- Document temperature and humidity conditions
- Assess flood, fire, dust, and vibration risks
- Review environmental monitoring coverage
- Identify environmental gaps

**Step 4: Physical Security Evaluation (Day 3-4 - 2-3 hours)**

- Complete Sheet 4 (Physical Security) for each location
- Document access control systems and CCTV coverage
- Assess equipment locking and cable protection
- Review asset labelling and segregation
- Identify security gaps

**Step 5: Power Protection Review (Day 4 - 2 hours)**

- Complete Sheet 5 (Power Infrastructure) for each location
- Document UPS and backup power coverage
- Assess surge and lightning protection
- Review emergency power-off locations
- Identify power protection gaps

**Step 6: Screen Positioning Assessment (Day 4-5 - 2 hours)**

- Complete Sheet 6 (Workstation Security) for high-traffic areas
- Document privacy screen usage
- Assess shoulder surfing risks
- Review screen positioning relative to windows and traffic
- Identify positioning gaps

**Step 7: Evidence Collection (Day 5-6 - 2-3 hours)**

- Take photographs of equipment locations and security measures
- Screenshot environmental monitoring dashboards
- Export access control reports
- Document evidence in Sheet 7 (Evidence Register)
- Store evidence files in secure location

**Step 8: Summary Review (Day 6 - 1 hour)**

- Review Sheet 8 (Summary Dashboard) - formulas auto-calculate compliance scores
- Verify compliance scores appear correct
- Identify areas below threshold (red or amber status)
- Prepare gap remediation plan for non-compliant areas

**Step 9: Quality Check (Day 6 - 1 hour)**

- Complete self-assessment using Quality Checklist (see section below)
- Verify all required fields completed
- Verify evidence register complete
- Verify formulas calculating correctly

**Step 10: Obtain Approvals (Day 7-12 - asynchronous)**

- Complete Sheet 9 (Approval Sign-Off) - Level 1: Assessor (you)
- Submit to Level 2: Facilities Manager for review and approval
- After Level 2 approval, submit to Level 3: CISO for review and approval
- After Level 3 approval, submit to Level 4: Compliance Officer for final sign-off
- Document approval dates and any feedback

**Step 11: Submit for Audit (Post-Approval)**

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
  - Organisation: [Organisation] name
  - Leave other fields as-is (Document ID, Version, etc.)

- **Status Legend** (Rows 14-17):
  - Read-only reference - understand colour coding:
    - Green (Compliant): Meets all policy requirements
    - Amber (Partial): Meets some requirements, gaps identified
    - Red (Non-Compliant): Does not meet requirements, immediate action needed

**Time Required:** 5 minutes

### Sheet 2: Equipment Locations

**Purpose:** Document all locations where information processing equipment is sited

**Structure:** 100 data rows for documenting multiple locations

**What to Document (Per Location):**

**Column A - Location ID:**

- Unique identifier for each location: "LOC-001", "LOC-002", etc.

**Column B - Location Name:**

- Descriptive name: "Main Data Centre", "Server Room B", "Network Closet Floor 3", "Branch Office Denver"

**Column C - Location Type:**

- Dropdown: "Data Centre", "Server Room", "Network Closet", "Office Area", "Co-location", "Remote Office", "Other"

**Column D - Building/Address:**

- Physical building and address: "Building A - 123 Main Street", "Co-lo Provider XYZ - Phoenix"

**Column E - Equipment Types:**

- What equipment is sited: "Servers, Storage, Network", "Network switches, Patch panels", "Workstations"

**Column F - Criticality Tier:**

- Dropdown: "Tier 1 - Critical", "Tier 2 - Standard", "Tier 3 - Non-Critical"
- Tier 1: Primary data centres, critical infrastructure
- Tier 2: Secondary facilities, standard operations
- Tier 3: Non-critical, general office equipment

**Column G - Access Control Type:**

- Dropdown: "Biometric + Badge", "Badge Only", "Key Lock", "Combination Lock", "No Access Control"
- Policy requirement: Tier 1 requires Biometric + Badge, Tier 2 requires Badge minimum

**Column H - Environmental Monitoring:**

- Dropdown: "Yes - Real-time alerts", "Yes - Periodic checks", "No monitoring"

**Column I - CCTV Coverage:**

- Dropdown: "Yes - 24/7 recording", "Yes - Motion triggered", "No CCTV"

**Column J - UPS Protected:**

- Dropdown: "Yes - Full coverage", "Partial coverage", "No UPS"

**Column K - Last Physical Inspection:**

- Date of last physical inspection: "15.01.2026", etc.
- Policy requirement: Annual inspection minimum

**Column L - Compliance Status:**

- Formula auto-calculates based on tier requirements:
  - Green (Compliant): Meets all tier requirements
  - Amber (Partial): Meets some requirements, gaps identified
  - Red (Non-Compliant): Major gaps, does not meet tier requirements

**Column M - Notes:**

- Any additional context: "Planned upgrade to biometric Q2 2026", "Shared with tenant, segregation pending"

**Common Entries:**

- One row per physical location with equipment
- Include all locations: data centres, server rooms, network closets, co-locations
- Don't forget remote offices and branch locations

**Time Required:** 45-60 minutes for comprehensive location inventory

### Sheet 3: Environmental Assessment

**Purpose:** Document environmental risks and protection at each equipment location

**Structure:** 100 data rows linked to locations from Sheet 2

**What to Document (Per Location):**

**Column A - Location ID:**

- Link to Sheet 2: "LOC-001", "LOC-002", etc.

**Column B - Location Name:**

- From Sheet 2 for reference

**Column C - Temperature Range (C):**

- Operating temperature range: "18-24C", "20-26C", etc.
- Policy requirement: 18-27C acceptable range

**Column D - Humidity Range (%RH):**

- Operating humidity range: "40-60%", "30-70%", etc.
- Policy requirement: 30-70% acceptable range

**Column E - Temperature Monitoring:**

- Dropdown: "Yes - Real-time alerts", "Yes - Daily checks", "No monitoring"

**Column F - Flood Risk:**

- Dropdown: "High (below grade)", "Medium (ground floor)", "Low (upper floor)", "Protected (raised floor)"

**Column G - Fire Suppression:**

- Dropdown: "Gas suppression", "Pre-action sprinkler", "Wet sprinkler", "Extinguishers only", "None"

**Column H - Dust/Contamination:**

- Dropdown: "Clean room", "Filtered HVAC", "Standard office", "Industrial/Dusty"

**Column I - Vibration Exposure:**

- Dropdown: "Low (isolated)", "Medium (standard building)", "High (near machinery)"

**Column J - Food/Drink Prohibited:**

- Dropdown: "Yes - Enforced", "Yes - Policy only", "No restriction"

**Column K - Environmental Incidents (12 months):**

- Number of environmental incidents: 0, 1, 5, etc.
- Include temperature excursions, water leaks, etc.

**Column L - Compliance Status:**

- Formula auto-calculates based on environmental requirements

**Column M - Notes:**

- Any additional context: "HVAC upgrade planned", "Flood sensor installed last month"

**Time Required:** 30-45 minutes for environmental assessment across all locations

### Sheet 4: Physical Security

**Purpose:** Document physical security measures at each equipment location

**Structure:** 100 data rows linked to locations from Sheet 2

**What to Document (Per Location):**

**Column A - Location ID:**

- Link to Sheet 2: "LOC-001", etc.

**Column B - Location Name:**

- From Sheet 2 for reference

**Column C - Access Control System:**

- Vendor and model: "HID iCLASS", "Lenel OnGuard", "Key lock", etc.

**Column D - Access Levels Defined:**

- Number of access levels: "3 (Admin, Ops, Vendor)", "1 (All or nothing)"

**Column E - Access Log Retention (Days):**

- Days of access logs retained: 90, 365, etc.
- Policy requirement: 90 days minimum

**Column F - CCTV System:**

- System details: "Verkada 4K", "Milestone VMS", "None"

**Column G - CCTV Retention (Days):**

- Days of footage retained: 30, 90, etc.
- Policy requirement: 30 days minimum for Tier 1

**Column H - Equipment Locking:**

- Dropdown: "Rack locks + Cable locks", "Rack locks only", "Cable locks only", "None"

**Column I - Cable Protection:**

- Dropdown: "Enclosed conduit", "Cable trays", "Exposed cabling"

**Column J - Asset Labels:**

- Dropdown: "Yes - All labelled", "Partial", "No labels"

**Column K - Segregation:**

- Dropdown: "Yes - Physical separation", "Partial - Logical only", "No - Shared space"
- Note: Organisation equipment should be segregated from third-party equipment

**Column L - Last Security Review:**

- Date of last security review: "15.12.2025", etc.

**Column M - Compliance Status:**

- Formula auto-calculates based on physical security requirements

**Column N - Notes:**

- Any additional context: "CCTV upgrade planned Q1 2026", "Shared rack with provider"

**Time Required:** 30-45 minutes for physical security assessment

### Sheet 5: Power Infrastructure

**Purpose:** Document power protection at each equipment location

**Structure:** 100 data rows linked to locations from Sheet 2

**What to Document (Per Location):**

**Column A - Location ID:**

- Link to Sheet 2: "LOC-001", etc.

**Column B - Location Name:**

- From Sheet 2 for reference

**Column C - UPS Coverage:**

- Dropdown: "100% (all equipment)", "Partial (critical only)", "None"

**Column D - UPS Runtime (minutes):**

- Minutes of UPS runtime: 15, 30, 60, etc.
- Policy requirement: 15 minutes minimum for orderly shutdown

**Column E - Generator Backup:**

- Dropdown: "Yes - Auto-transfer", "Yes - Manual transfer", "No generator"

**Column F - Surge Protection:**

- Dropdown: "Yes - All circuits", "Partial", "None"

**Column G - Lightning Protection:**

- Dropdown: "Yes - Building grounded", "Unknown", "No"

**Column H - EPO Switch:**

- Dropdown: "Yes - Near room", "Yes - Remote only", "No EPO"
- EPO = Emergency Power Off

**Column I - Power Redundancy:**

- Dropdown: "Dual feed (A+B)", "Single feed + UPS", "Single feed only"

**Column J - Last UPS Test:**

- Date of last UPS load test: "15.11.2025", etc.
- Policy requirement: Quarterly UPS testing

**Column K - Last Generator Test:**

- Date of last generator test: "01.12.2025", etc.
- Policy requirement: Monthly generator testing

**Column L - Power Incidents (12 months):**

- Number of power-related incidents: 0, 1, 5, etc.

**Column M - Compliance Status:**

- Formula auto-calculates based on power protection requirements

**Column N - Notes:**

- Any additional context: "UPS battery replacement due Q2 2026"

**Time Required:** 30 minutes for power infrastructure assessment

### Sheet 6: Workstation Security

**Purpose:** Document screen positioning and workstation security in office areas

**Structure:** 100 data rows for documenting workstation areas

**What to Document (Per Area):**

**Column A - Area ID:**

- Unique identifier: "WS-001", "WS-002", etc.

**Column B - Area Name:**

- Descriptive name: "Finance Department", "Reception", "Call Centre", "Executive Suite"

**Column C - Workstation Count:**

- Number of workstations in area: 5, 20, 100, etc.

**Column D - Data Sensitivity:**

- Dropdown: "High (PII, Financial)", "Medium (Internal)", "Low (Public)"

**Column E - Screen Positioning:**

- Dropdown: "Optimal (away from windows/traffic)", "Acceptable", "At risk (visible to public)"

**Column F - Privacy Screens:**

- Dropdown: "Yes - All workstations", "Partial", "None"
- Policy requirement: High sensitivity areas require privacy screens

**Column G - Automatic Lock:**

- Dropdown: "Yes - <5 min timeout", "Yes - >5 min timeout", "Not configured"

**Column H - Clear Desk Policy:**

- Dropdown: "Yes - Enforced", "Yes - Policy only", "No policy"

**Column I - Visitor Access:**

- Dropdown: "Escorted only", "Badge required", "Open access"

**Column J - Shoulder Surfing Risk:**

- Dropdown: "Low", "Medium", "High"
- Consider traffic patterns, public access, window visibility

**Column K - Last Review:**

- Date of last workstation security review: "15.01.2026", etc.

**Column L - Compliance Status:**

- Formula auto-calculates based on data sensitivity and controls

**Column M - Notes:**

- Any additional context: "Privacy screens ordered", "Reception area exposed to public"

**Time Required:** 30-45 minutes for workstation security assessment

### Sheet 7: Evidence Register

**Purpose:** Document all supporting evidence for audit traceability

**Structure:** Evidence log with links to actual evidence files

**What to Document (Per Evidence Item):**

**Column A - Evidence ID:**

- Unique identifier: "EVID-001", "EVID-002", etc.

**Column B - Evidence Type:**

- Dropdown: "Screenshot", "Configuration Export", "Log Sample", "Report", "Document", "Photo"

**Column C - Description:**

- What evidence shows: "Data Centre floor plan with equipment layout", "Access control logs Jan 2026"

**Column D - Related Sheet/Item:**

- Links evidence to assessment: "Sheet 2, Row 5 (Main Data Centre)", "Sheet 4, Row 3 (Server Room B)"

**Column E - File Name:**

- Evidence filename: "DataCentre_FloorPlan_20260115.pdf", "AccessLogs_Jan2026.csv"

**Column F - File Location:**

- Where evidence stored: "SharePoint > ISMS > Assessments > A.7.8-9 > Evidence"

**Column G - Collection Date:**

- When evidence collected: "15.01.2026"

**Column H - Collected By:**

- Who collected evidence: "John Smith - Facilities Manager"

**Column I - Retention Period:**

- How long to retain: "3 years", "Permanent"

**Column J - Notes:**

- Any additional context

**Common Evidence to Collect:**

1. **Location Documentation:**
   - Facility floor plans with equipment locations marked
   - Equipment inventory reports
   - Criticality classification documentation

2. **Environmental Evidence:**
   - Environmental monitoring dashboard screenshots
   - Temperature/humidity trend reports (30 days)
   - Environmental incident reports

3. **Physical Security Evidence:**
   - Access control system configuration screenshots
   - Access log samples (7 days)
   - CCTV coverage maps
   - Photos of equipment locking mechanisms

4. **Power Infrastructure Evidence:**
   - UPS configuration and capacity reports
   - UPS and generator test records
   - Power incident reports

5. **Workstation Security Evidence:**
   - Photos of workstation positioning
   - Privacy screen deployment records
   - Clear desk policy documentation

**Time Required:** 2-3 hours for comprehensive evidence collection

### Sheet 8: Summary Dashboard

**Purpose:** Automated compliance scoring and overall equipment siting health

**Structure:** Dashboard with formulas auto-calculating from Sheets 2-6

**What to Review (Auto-Calculated - Read-Only):**

**Overall Compliance Score:**

- Formula aggregates compliance from all assessment sheets
- Displayed as percentage: 92%, 78%, etc.
- Thresholds: >90% (Green), 75-89% (Amber), <75% (Red)

**Domain Scores:**

- Equipment Locations Compliance Score (%)
- Environmental Assessment Compliance Score (%)
- Physical Security Compliance Score (%)
- Power Infrastructure Compliance Score (%)
- Workstation Security Compliance Score (%)

**Gap Summary:**

- Auto-generated list of non-compliant items requiring remediation
- Prioritised by severity (Critical, High, Medium, Low)

**What YOU Do:**

- Review dashboard after completing Sheets 2-6
- Verify auto-calculations appear correct
- Investigate any unexpected red/amber status
- Prepare remediation plan for gaps identified
- NO manual data entry in this sheet (formulas auto-populate)

**Time Required:** 15-30 minutes for review and interpretation

### Sheet 9: Approval Sign-Off

**Purpose:** Four-level approval workflow for assessment completion

**Structure:** Approval table with dates and signatures

**Approval Levels:**

**Level 1: Assessor (You)**

- Role: Assessment Completed By
- Name: [Your name]
- Date: Date you completed quality check
- Signature/Confirmation: Your initials or digital signature

**Level 2: Facilities Manager**

- Role: Technical Review and Approval
- Name: [Facilities Manager name]
- Date: Date reviewed and approved
- Comments: Any feedback or required corrections

**Level 3: CISO**

- Role: Executive Review and Approval
- Name: [CISO name]
- Date: Date reviewed and approved
- Comments: Strategic feedback or resource allocation needs

**Level 4: Compliance Officer**

- Role: Final Audit Readiness Sign-Off
- Name: [Compliance Officer name]
- Date: Date certified assessment audit-ready
- Comments: Audit preparation feedback

**Time Required:** 5 minutes for Level 1 completion, then asynchronous for Levels 2-4

---

## Evidence Collection

### What Evidence to Collect

**Purpose:** Provide audit trail and verification of assessment accuracy

**Evidence Categories:**

**1. Location Documentation**

- Facility floor plans with equipment locations marked
- Equipment inventory from asset management system
- Criticality classification documentation
- Co-location agreements (if applicable)

**2. Environmental Evidence**

- Environmental monitoring platform screenshots
- Temperature/humidity trend data (30 days minimum)
- Environmental excursion reports
- HVAC configuration documentation
- Fire suppression system certification

**3. Physical Security Evidence**

- Access control system configuration screenshots
- Access log exports (7-30 days sample)
- CCTV system configuration and coverage maps
- Photos of equipment locking mechanisms
- Asset labelling photographs

**4. Power Infrastructure Evidence**

- UPS configuration and capacity documentation
- UPS load test reports (quarterly)
- Generator test reports (monthly)
- Power distribution diagrams
- Power incident reports

**5. Workstation Security Evidence**

- Office layout diagrams showing workstation positioning
- Privacy screen deployment records
- Screen lock policy configuration screenshots
- Clear desk policy documentation

### Evidence Storage

**Storage Location:**

- **Secure network share:** \\server\ISMS\Assessments\A.7.8.1_Equipment_Siting\Evidence
- **SharePoint/Cloud:** SharePoint > ISMS > Assessments > A.7.8.1 > Evidence folder

**Access Control:**

- Evidence folder permissions: CISO, Facilities Manager, Compliance Officer, Internal Audit (read-only)

**Retention:**

- Minimum: 3 years (typical audit requirement)
- Permanent: If evidence of significant incidents or major findings

---

## Common Pitfalls

### Pitfall 1: Incomplete Location Inventory

**Problem:** Only documenting main data centre, missing network closets, branch offices, co-locations

**Impact:** Audit finding - incomplete assessment scope

**How to Avoid:**

- Create master location list BEFORE starting assessment
- Include ALL locations with information processing equipment
- Don't forget: Network closets, wiring cupboards, co-location cages, remote offices
- Walk through facilities physically, don't just rely on documentation

### Pitfall 2: Assuming Co-location is "Someone Else's Problem"

**Problem:** Not assessing co-location facilities because provider "handles everything"

**Example:** "We're in co-lo, N/A" (but you're responsible for cage-level security, equipment locking)

**How to Avoid:**

- Document responsibility split clearly (provider vs. customer)
- Assess customer-controlled aspects: Cage locks, equipment locks, in-cage environmental monitoring
- Verify provider controls through audit reports (SOC 2, ISO 27001)
- Include co-location as a location in assessment

### Pitfall 3: Missing Workstation Areas

**Problem:** Only assessing server rooms, ignoring office workstations processing sensitive data

**Example:** Finance department workstations face windows with public visibility

**How to Avoid:**

- Assess ALL areas where sensitive data is processed or displayed
- Include reception areas, call centres, executive offices
- High sensitivity = higher protection requirements (privacy screens, positioning)

### Pitfall 4: Outdated Floor Plans

**Problem:** Using floor plans from 3 years ago that don't reflect current equipment layout

**Impact:** Evidence doesn't reflect current state, audit finding

**How to Avoid:**

- Verify floor plans match current state during physical walk-through
- Update or annotate floor plans with current equipment locations
- Date all floor plans (creation date and verification date)

### Pitfall 5: Not Testing Access Controls

**Problem:** Documenting "badge access required" without verifying it works

**Example:** Badge reader installed but not properly configured, door can be opened without badge

**How to Avoid:**

- TEST access controls during assessment (try to access without authorisation)
- Verify access logs show all access attempts
- Check for tailgating opportunities (door held open)

### Pitfall 6: Ignoring Environmental Monitoring Gaps

**Problem:** Documenting temperature monitoring exists but not verifying coverage

**Example:** "We have temperature sensors" (but they're on the ceiling, not at equipment intake)

**How to Avoid:**

- Verify sensor placement during physical inspection
- Check sensor readings against portable thermometer
- Confirm alerts actually trigger and reach appropriate personnel

### Pitfall 7: Power Protection Assumptions

**Problem:** Assuming all equipment is UPS protected without verification

**Example:** "UPS in data centre" (but only covers some racks, network closets unprotected)

**How to Avoid:**

- Trace power circuits from equipment to UPS
- Verify UPS capacity vs. actual load
- Check UPS test records (batteries can fail silently)

### Pitfall 8: Copy-Paste Errors

**Problem:** Copying rows in Excel, forgetting to update location-specific data

**Example:** Row 5 says "Data Centre A" but data is actually for "Server Room B"

**How to Avoid:**

- Enter data methodically, one location at a time
- Cross-check location ID against location name in each row
- Have second person spot-check (Facilities Manager review)

### Pitfall 9: Formula Corruption

**Problem:** Accidentally overwriting formula cells, breaking auto-calculations

**Example:** Compliance Status formula deleted, now shows blank instead of green/amber/red

**How to Avoid:**

- Summary Dashboard (Sheet 8) and Compliance Status columns are FORMULA CELLS - do not edit
- If formula appears broken, refer to Part II Technical Specification for correct formula
- Save backup copy before making any changes

### Pitfall 10: Approval Workflow Shortcuts

**Problem:** Skipping approval levels or obtaining approvals out of sequence

**Example:** Going straight to CISO without Facilities Manager review

**How to Avoid:**

- Follow four-level approval workflow in order
- Each level reviews AND signs (date + name)
- If corrections required, go back to assessor, fix, resubmit through workflow

---

## Quality Checklist

Before submitting for Level 2 approval (Facilities Manager), complete this self-assessment:

### Sheet 1: Instructions & Legend

- [ ] Assessment Date completed
- [ ] Completed By (your name and role)
- [ ] Organisation name filled in
- [ ] All document information reviewed

### Sheet 2: Equipment Locations

- [ ] ALL locations with equipment documented (not just main data centre)
- [ ] Location types correctly classified
- [ ] Criticality tiers assigned based on business impact
- [ ] Access control type accurately reflects current state
- [ ] Environmental monitoring status verified
- [ ] CCTV coverage status verified
- [ ] UPS protection status verified
- [ ] Last physical inspection date current
- [ ] Compliance status column showing green/amber/red
- [ ] Notes explain any amber/red status

### Sheet 3: Environmental Assessment

- [ ] All locations from Sheet 2 included
- [ ] Temperature and humidity ranges documented
- [ ] Flood risk assessed for each location
- [ ] Fire suppression type documented
- [ ] Dust/contamination risk assessed
- [ ] Environmental incidents documented
- [ ] Compliance status formulas working

### Sheet 4: Physical Security

- [ ] All locations from Sheet 2 included
- [ ] Access control systems documented
- [ ] Access log retention verified
- [ ] CCTV coverage and retention documented
- [ ] Equipment locking measures documented
- [ ] Cable protection assessed
- [ ] Asset labelling status documented
- [ ] Equipment segregation assessed
- [ ] Compliance status formulas working

### Sheet 5: Power Infrastructure

- [ ] All locations from Sheet 2 included
- [ ] UPS coverage documented
- [ ] UPS runtime sufficient for orderly shutdown
- [ ] Generator backup documented (if applicable)
- [ ] Surge and lightning protection assessed
- [ ] EPO switch locations documented
- [ ] Power redundancy assessed
- [ ] UPS and generator test dates current
- [ ] Power incidents documented
- [ ] Compliance status formulas working

### Sheet 6: Workstation Security

- [ ] All high-sensitivity workstation areas documented
- [ ] Screen positioning assessed
- [ ] Privacy screen usage documented
- [ ] Automatic screen lock configured
- [ ] Clear desk policy status documented
- [ ] Visitor access controls assessed
- [ ] Shoulder surfing risk assessed
- [ ] Compliance status formulas working

### Sheet 7: Evidence Register

- [ ] At least 10 evidence items documented
- [ ] Evidence types appropriate
- [ ] Descriptions clear
- [ ] Evidence linked to specific sheets/items
- [ ] File names match actual files
- [ ] File locations accurate
- [ ] Collection dates recent
- [ ] ALL evidence files actually exist in documented location

### Sheet 8: Summary Dashboard

- [ ] Overall Compliance Score displays
- [ ] All domain scores display
- [ ] Gap summary auto-populates
- [ ] Scores appear reasonable
- [ ] NO manual data entry in dashboard

### Sheet 9: Approval Sign-Off

- [ ] Level 1 (Assessor) completed
- [ ] Assessment ready for submission to Level 2

**If ALL checkboxes checked:** Assessment is ready for Level 2 approval
**If ANY checkboxes unchecked:** Address gaps before submission

---

## Review & Approval

### Four-Level Approval Workflow

**Purpose:** Ensure assessment accuracy, completeness, and audit readiness through progressive review

**Approval Sequence:** Assessor -> Facilities Manager -> CISO -> Compliance Officer

### Level 1: Assessor (You)

**Responsibilities:**

- Complete all assessment sheets (Sheets 2-6)
- Collect all required evidence (Sheet 7)
- Perform self-assessment using Quality Checklist
- Complete Level 1 approval in Sheet 9

**Timeline:** Complete before submitting to Level 2

### Level 2: Facilities Manager

**Responsibilities:**

- Review all location inventories for completeness
- Verify environmental and security assessments accurate
- Spot-check evidence files
- Provide feedback if corrections needed
- Complete Level 2 approval in Sheet 9

**Timeline:** 2-5 business days after receipt from Assessor

### Level 3: CISO

**Responsibilities:**

- Review Summary Dashboard for overall compliance
- Assess remediation resource requirements
- Prioritise gaps for remediation
- Complete Level 3 approval in Sheet 9

**Timeline:** 2-5 business days after Level 2 approval

### Level 4: Compliance Officer

**Responsibilities:**

- Review assessment for audit readiness
- Verify evidence completeness
- Certify assessment ready for audit
- Complete Level 4 approval in Sheet 9

**Timeline:** 1-3 business days after Level 3 approval

**Post-Approval:**

- Assessment workbook finalised
- Assessment stored in audit repository
- Assessment available to Internal Audit and External Auditors

---

**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
