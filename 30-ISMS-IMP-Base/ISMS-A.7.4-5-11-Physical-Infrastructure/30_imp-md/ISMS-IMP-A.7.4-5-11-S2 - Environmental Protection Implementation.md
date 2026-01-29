# ISMS-IMP-A.7.4-5-11-S2: Environmental Protection Assessment
## Assessment Specification with User Completion Guide
### ISO/IEC 27001:2022 Control A.7.5: Protecting Against Physical and Environmental Threats

---

## Document Control

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.7.4-5-11-S2 |
| **Version** | 1.0 |
| **Assessment Area** | Environmental Protection - Fire Detection/Suppression, Water Detection, Temperature/Humidity Monitoring |
| **Related Policy** | ISMS-POL-A.7.4-5-11, Section 3 (Environmental Protection Requirements) |
| **Purpose** | Document deployed environmental protection systems, assess capabilities against policy requirements, and identify gaps |
| **Target Audience** | Facilities Management, Fire/Life Safety Technicians, HVAC Technicians, Security Operations, Compliance Officers, Auditors |
| **Assessment Type** | Technical & Operational |
| **Review Cycle** | Quarterly or After Major Infrastructure Changes |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Environmental Protection assessment workbook | ISMS Implementation Team |

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

**Assessment Name:** ISMS-IMP-A.7.4-5-11-S2 - Environmental Protection Assessment

#### What This Assessment Covers

This assessment documents the environmental PROTECTION systems deployed in your facilities. This is the "WHAT environmental protection do we have?" assessment that answers:

- What fire detection systems are deployed? (smoke detectors, heat detectors, alarm panels)
- What fire suppression systems are deployed? (sprinklers, gas suppression, pre-action systems)
- What water damage protection systems are deployed? (water detection sensors, drainage, waterproofing)
- What temperature and humidity monitoring systems are deployed? (environmental sensors, HVAC monitoring, alerts)
- How are environmental systems integrated? (BMS, security dashboards, alerting)
- What environmental incidents have occurred? (fire alarms, water damage, temperature excursions)

#### Key Principle

This assessment is **completely vendor-agnostic and technology-independent**. You document YOUR specific systems (whatever you use - Simplex, Notifier, Edwards for fire alarms; Honeywell, Siemens for environmental sensors; etc.), and verify capabilities against generic policy requirements from ISMS-POL-A.7.4-5-11, Section 3.

#### What You'll Document

**Fire Detection Systems:**
- Every fire alarm panel and detector deployment
- Smoke detector count and locations (ceiling, under-floor, in-rack)
- Heat detector count and locations
- Notification devices (horns, strobes)
- Monitoring service or self-monitoring configuration

**Fire Suppression Systems:**
- Sprinkler systems (wet pipe, dry pipe, pre-action)
- Gas suppression systems (FM-200, Novec, Inergen for datacenters)
- Suppression zone coverage
- Testing and inspection records

**Water Detection Systems:**
- Water detection sensors and locations
- Coverage areas (server rooms, below-grade, under raised floors)
- Alert configurations (email, SMS, alarm panel)
- Response procedures

**Temperature and Humidity Monitoring:**
- Environmental sensor deployments
- Sensor locations (intake, exhaust, return air)
- Temperature and humidity thresholds
- Alert configurations and escalation
- Historical excursion data

**Environmental Integration:**
- BMS integration status (if applicable)
- Security dashboard integration (environmental events visible to SOC)
- Alerting configurations (email, SMS, dashboards)

**Environmental Incidents:**
- Fire alarm events (actual fires, false alarms)
- Water damage incidents
- Temperature/humidity excursions
- System failures and downtime
- Response times and resolution status

#### How This Relates to Other A.7.4-5-11 Assessments

| Assessment            | Focus                  | Relationship to A.7.4-5-11-S2      |
|-----------------------|------------------------|------------------------------------|
| ISMS-IMP-A.7.4-5-11-S1 | Physical Monitoring | Access control, CCTV, intrusion detection systems |
| **ISMS-IMP-A.7.4-5-11-S2** | **Environmental Protection** | **Fire, water, temperature protection systems** |
| ISMS-IMP-A.7.4-5-11-S3 | Utility Resilience      | UPS, generators, HVAC, ISP systems |
| ISMS-IMP-A.7.4-5-11-S4 | Compliance Dashboard    | Consolidated view across all physical infrastructure |

This assessment (A.7.4-5-11-S2) focuses specifically on Control A.7.5 (Protecting Against Physical and Environmental Threats). It complements assessments for A.7.4 (Physical Monitoring) and A.7.11 (Utility Resilience).

### Who Should Complete This Assessment

#### Primary Stakeholders

1. **Facilities Manager** - Overall environmental systems ownership
2. **Fire/Life Safety Technician** - Fire detection/suppression systems expertise
3. **HVAC Technician** - Temperature/humidity monitoring and HVAC systems
4. **Security Operations** - Environmental monitoring integration with security systems
5. **Compliance Officers** - Audit requirements and evidence collection

#### Required Skills

- Understanding of fire alarm systems (detectors, panels, notification devices)
- Familiarity with fire suppression systems (sprinklers, gas suppression, pre-action)
- Knowledge of environmental monitoring (temperature/humidity sensors, BMS)
- Understanding of facility criticality tiers (Tier 1 vs. Tier 2 requirements)
- Access to environmental system admin consoles and maintenance records

#### Time Commitment

- **Initial assessment:** 8-12 hours (comprehensive review of all environmental systems across facilities)
- **Quarterly updates:** 2-3 hours (update incidents, performance metrics, minor configuration changes)

### Expected Outputs

Upon completion, you will have:

1. ✅ **Complete system inventory** - Every fire detection, suppression, water detection, and temperature monitoring system documented
2. ✅ **Coverage analysis** - Fire detector coverage, sprinkler coverage, water sensor placement, temperature sensor locations
3. ✅ **Capability assessment** - What each system can and cannot do
4. ✅ **Integration status** - BMS integration, security dashboard integration, alerting configurations
5. ✅ **Incident tracking** - Environmental incidents and system failures documented
6. ✅ **Performance metrics** - Response times, false alarm rates, temperature excursions, system uptime
7. ✅ **Gap analysis** - Identified gaps between deployed systems and policy requirements
8. ✅ **Evidence register** - Supporting documentation for audit
9. ✅ **Approved assessment** - Four-level approval workflow completed

---

## Prerequisites

### Information You'll Need

Before starting this assessment, gather:

#### 1. System Access

- Administrator access to all fire alarm panels (on-site or remote access)
- Access to fire suppression system documentation and inspection reports
- Administrator access to water detection systems (alarm panels, cloud portals)
- Administrator access to environmental monitoring platforms (temperature/humidity sensors)
- Access to Building Management System (BMS) if applicable
- Access to environmental incident reports and maintenance records

#### 2. Documentation

- Facility floor plans with fire detector placements
- Fire suppression system design drawings (sprinkler layouts, gas suppression zones)
- Water detection sensor placement maps
- Environmental sensor placement maps (temperature/humidity)
- Fire alarm as-built documentation
- Fire marshal inspection reports (annual inspections)
- Fire suppression testing records (sprinkler flow tests, gas system tests)
- Environmental monitoring system configuration documentation

#### 3. Historical Data

- Fire alarm logs (last 90 days minimum - all alarms, including false alarms)
- Water detection alarm logs (last 90 days minimum)
- Temperature/humidity excursion logs (last 90 days minimum)
- Environmental incident reports (last 12 months)
- System maintenance records (fire alarm testing, sprinkler inspections, sensor calibrations)
- Fire marshal inspection reports (most recent annual inspection)

#### 4. Policy Requirements

- ISMS-POL-A.7.4-5-11, Section 3 (Environmental Protection Requirements)
  - Section 3.1: Environmental Threat Assessment
  - Section 3.2: Fire Detection and Suppression
  - Section 3.3: Flood and Water Damage Protection
  - Section 3.4: Temperature and Humidity Control
  - Section 3.5: Structural Protection
  - Section 3.6: Environmental Protection Plan

### Required Tools

- Microsoft Excel (2016 or later) for workbook completion
- Access to fire alarm panel admin consoles (on-site or remote)
- Access to environmental monitoring platforms (Ubiquiti UniFi, Monnit, SensorPush, BMS)
- Temperature/humidity calibration device (handheld thermometer/hygrometer - if verifying sensor accuracy)
- Screen capture tools (for evidence screenshots)

### Dependencies

This assessment has NO dependencies on other assessments - it can be completed independently.

However, outputs from this assessment are INPUT to:
- ISMS-IMP-A.7.4-5-11-S4 (Compliance Dashboard) - Consolidates environmental protection with physical monitoring and utility assessments
- ISMS-IMP-A.7.4-5-11-S3 (Utility Resilience) - HVAC systems documented in both (environmental monitoring here, HVAC resilience there)

---

## Workflow

### High-Level Process

```
1. PREPARE
   ↓
2. INVENTORY SYSTEMS (Sheet 2: Fire Detection, Sheet 3: Water Detection, Sheet 4: Temperature/Humidity)
   ↓
3. ASSESS COVERAGE (Fire detector placement, sprinkler coverage, water sensor locations, temperature sensor placements)
   ↓
4. DOCUMENT INTEGRATION (BMS, security dashboards, alerting)
   ↓
5. REVIEW ENVIRONMENTAL INCIDENTS (fire alarms, water damage, temperature excursions)
   ↓
6. COLLECT EVIDENCE (Sheet 6: Evidence Register)
   ↓
7. REVIEW SUMMARY (Sheet 5: Summary Dashboard - automated scoring)
   ↓
8. QUALITY CHECK (Self-assessment against checklist)
   ↓
9. OBTAIN APPROVALS (Sheet 7: Approval Sign-Off)
   ↓
10. SUBMIT FOR AUDIT
```

### Detailed Step-by-Step

**Step 1: Preparation (Day 1 - 2 hours)**
- Read this Part I User Guide completely
- Review ISMS-POL-A.7.4-5-11, Section 3 requirements
- Gather all prerequisites (system access, documentation, historical data)
- Schedule time with Facilities Manager, Fire/Life Safety Technician, HVAC Technician
- Download or generate assessment workbook (Excel file)

**Step 2: System Inventory (Day 1-3 - 4-6 hours)**
- Open assessment workbook
- Complete Sheet 1 (Instructions & Legend) - organization info, assessment date
- Complete Sheet 2 (Fire Detection) - inventory all fire alarm panels, detectors, notification devices
- Complete Sheet 3 (Water Detection) - inventory all water detection sensors and coverage areas
- Complete Sheet 4 (Temperature/Humidity) - inventory all environmental sensors and monitoring platforms
- Document integration status (BMS, security dashboard, alerting)

**Step 3: Coverage Analysis (Day 3-4 - 3-4 hours)**
- Verify fire detector coverage (100% of facility area per fire code)
- Verify fire suppression coverage (sprinklers or gas suppression in critical areas)
- Verify water detection coverage (below-grade areas, server rooms, under raised floors, near plumbing)
- Verify temperature sensor coverage (server rooms, datacenters, telecom closets)
- Identify blind spots (areas without coverage)
- Document gaps in Sheet 2, 3, 4 notes

**Step 4: Integration Assessment (Day 4 - 2-3 hours)**
- Verify BMS integration (if applicable - environmental systems visible in BMS)
- Verify security dashboard integration (environmental events visible to SOC)
- Verify alerting configurations (email, SMS, alarm panel notifications)
- Test sample integration (trigger fire alarm, verify SOC receives event)
- Document integration status in respective sheets

**Step 5: Environmental Incident Review (Day 5 - 2 hours)**
- Query incident management system or maintenance logs for environmental incidents (last 12 months)
- Review fire alarm logs (actual fires, false alarms)
- Review water detection alarm logs (actual water damage, false alarms)
- Review temperature/humidity excursion logs (HVAC failures, critical thresholds exceeded)
- Document key incidents (not all false alarms, but representative sample and all actual events)
- Classify incidents (Critical, High, Medium, Low per ISMS-POL-A.7.4-5-11, Section 5.4)
- Identify trends (repeat incident types, common causes)

**Step 6: Evidence Collection (Day 5-6 - 2-3 hours)**
- Take screenshots of fire alarm panel configurations (detector count, zones, monitoring)
- Take screenshots of water detection system configurations (sensor count, alert settings)
- Take screenshots of environmental monitoring platforms (temperature/humidity dashboards, thresholds)
- Export sample fire alarm logs (last 30 days)
- Export sample water detection logs (last 30 days)
- Export sample temperature/humidity data (last 30 days with excursions highlighted)
- Take photos of fire suppression systems (sprinkler heads, gas suppression panels - if accessible)
- Document evidence in Sheet 6 (Evidence Register)
- Store evidence files in secure location

**Step 7: Summary Review (Day 6 - 1 hour)**
- Review Sheet 5 (Summary Dashboard) - formulas automatically calculate compliance scores
- Verify compliance scores accurate (cross-check against detailed sheets)
- Identify areas below threshold (red or amber status)
- Prepare gap remediation plan for non-compliant areas

**Step 8: Quality Check (Day 6 - 1 hour)**
- Complete self-assessment using Quality Checklist (see section below)
- Verify all required fields completed
- Verify evidence register complete
- Verify formulas calculating correctly

**Step 9: Obtain Approvals (Day 7-12 - asynchronous)**
- Complete Sheet 7 (Approval Sign-Off) - Level 1: Assessor (you)
- Submit to Level 2: Facilities Manager for review and approval
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

### Sheet 2: Fire Detection

**Purpose:** Document all fire detection systems, fire alarm panels, detectors, and notification devices

**Structure:** 100 data rows for documenting multiple facilities/systems

**What to Document (Per Facility or Fire Alarm Panel):**

**Column A - Facility/System Name:**
- Example: "Building A - Main Campus", "Datacenter 1", "Branch Office - Denver"

**Column B - Fire Alarm Panel:**
- Vendor and model: "Simplex 4100ES", "Notifier NFS2-640", "Edwards EST3", "Honeywell Fire-Lite MS-9200UDLS"
- If multiple panels, create separate rows per panel

**Column C - Panel Type:**
- Dropdown: "Addressable", "Conventional", "Hybrid"
- Note: Addressable preferred (identifies specific detector that triggered)

**Column D - Smoke Detector Count:**
- Total number of smoke detectors on this panel: 15, 50, 200, etc.

**Column E - Heat Detector Count:**
- Total number of heat detectors on this panel: 5, 10, 20, etc.
- Note: Heat detectors used in areas where smoke detectors inappropriate (kitchens, mechanical rooms)

**Column F - Detector Technology:**
- Detector types deployed: "Photoelectric", "Ionization", "Dual-sensor", "Aspirating (ASD)"
- Example: "Photoelectric (standard), ASD (server room)"

**Column G - Notification Devices:**
- Horn/strobe count: "20 horn/strobes", "15 horns + 15 strobes (separate)", "30 combination units"

**Column H - Coverage Percentage:**
- Percentage of facility area covered by smoke/heat detection: 100%, 95%, 75%, etc.
- Policy requirement: 100% coverage
- If <100%, explain in Notes (e.g., "95% - warehouse area no detection yet")

**Column I - Monitoring Service:**
- Dropdown: "Yes - Professional", "Yes - Self (BMS/SOC)", "No"
- Note: Monitoring service required (professional or self-monitoring acceptable)

**Column J - Backup Communication:**
- Dropdown: "Yes - Cellular", "Yes - Dual path", "No"
- Note: Backup communication recommended for critical facilities

**Column K - Last Testing Date:**
- Date of last annual fire alarm test (full system test): "15.11.2025", etc.
- Policy requirement: Annual testing by certified technician

**Column L - Last Fire Marshal Inspection:**
- Date of last fire marshal inspection and approval: "01.12.2025", etc.
- Note: Annual inspection typically required by local fire code

**Column M - Compliance Status:**
- Formula auto-calculates based on requirements:
  - Green (✅): 100% coverage, monitoring service active, testing current, fire marshal inspection current
  - Amber (⚠️): Minor gaps (e.g., 95% coverage, testing slightly overdue)
  - Red (❌): Major gaps (no monitoring, testing >12 months overdue, <90% coverage)

**Column N - Notes:**
- Any additional context: "Server room has aspirating detection", "Testing scheduled for Q1 2026", "Fire marshal inspection passed with no issues"

**Common Entries:**
- One row per fire alarm panel deployment
- Multiple rows if facility has multiple disparate fire alarm systems (e.g., main building panel, datacenter panel)
- Document any coverage gaps honestly (blind spots, areas without detection)

**Time Required:** 45-60 minutes for comprehensive fire detection inventory across all facilities

### Sheet 3: Water Detection

**Purpose:** Document all water detection systems, sensors, coverage areas, and alert configurations

**Structure:** 100 data rows for documenting water detection sensor deployments

**What to Document (Per Facility or Water Detection System):**

**Column A - Facility/System Name:**
- Example: "Building A - Main Campus", "Datacenter 1 - Basement", "Server Room B"

**Column B - Water Detection System:**
- Vendor and model: "Honeywell 5800FLOOD", "D-Link DCH-S160 Wi-Fi", "Wired leak detection system", "BMS-integrated"
- If multiple disparate systems, create separate rows

**Column C - Sensor Count:**
- Total number of water detection sensors: 5, 10, 20, etc.

**Column D - Sensor Type:**
- Sensor technology: "Spot sensor (individual)", "Cable sensor (continuous)", "Wireless IoT", "Wired to BMS"
- Example: "10 spot sensors + 2 cable sensors (under raised floor)"

**Column E - Coverage Areas:**
- Areas protected by water detection: "Server room perimeter, under raised floor, near HVAC", "Basement, below-grade storage"

**Column F - High-Risk Areas Covered:**
- Dropdown: "Yes - All covered", "Partial - Some gaps", "No - Missing coverage"
- High-risk areas: Below-grade facilities, server rooms, under raised floors, near plumbing/HVAC
- Policy requirement: 100% of high-risk areas covered

**Column G - Alert Method:**
- How alerts are sent: "Email + SMS", "BMS alarm", "Alarm panel + email", "Local audible only"

**Column H - Alert Recipients:**
- Who receives alerts: "Facilities Manager, IT Ops, Security", "BMS monitoring center"

**Column I - Response Procedure Documented:**
- Dropdown: "Yes", "No"
- Note: Response procedure should document: Who responds, how to shut off water source, equipment protection steps

**Column J - Last Testing Date:**
- Date of last monthly water sensor test: "15.01.2026", etc.
- Policy requirement: Monthly testing (pour water on sensor, verify alarm)

**Column K - Compliance Status:**
- Formula auto-calculates based on requirements:
  - Green (✅): All high-risk areas covered, alert method configured, response procedure documented, testing current
  - Amber (⚠️): Minor gaps (e.g., partial coverage, testing slightly overdue)
  - Red (❌): Major gaps (no coverage in high-risk areas, no alerts, testing >60 days overdue)

**Column L - Notes:**
- Any additional context: "Cable sensors under entire raised floor", "Alert testing scheduled weekly", "Basement flood risk high (near river)"

**Common Entries:**
- One row per facility or water detection zone
- Separate rows for different areas if using different systems (e.g., server room wireless sensors, basement wired sensors)
- Document coverage gaps (areas without sensors but at risk for water damage)

**Time Required:** 30-45 minutes for water detection inventory and coverage assessment

### Sheet 4: Temperature_Humidity

**Purpose:** Document all temperature and humidity monitoring systems, sensors, platforms, and alert configurations

**Structure:** 100 data rows for documenting environmental sensor deployments

**What to Document (Per Facility or Monitoring Zone):**

**Column A - Facility/System Name:**
- Example: "Datacenter 1 - Server Room", "Building A - Network Closet", "Colocation Cage - Phoenix"

**Column B - Monitoring Platform:**
- Platform/vendor: "Ubiquiti UniFi Environmental Sensors", "Monnit iMonnit", "Honeywell BMS", "SensorPush Cloud", "Custom Grafana+InfluxDB"

**Column C - Sensor Count:**
- Total number of temperature/humidity sensors in this area: 2, 5, 10, etc.

**Column D - Sensor Locations:**
- Where sensors are placed: "Intake (cold aisle), exhaust (hot aisle), return air", "Equipment rack intake level"
- Note: Sensors should be at equipment intake level, not ceiling level

**Column E - Temperature Thresholds (°C):**
- Warning and critical temperature thresholds: "Warning: 28°C high / 16°C low, Critical: 30°C high / 15°C low"
- Policy recommendation: Warning 28°C high / 16°C low, Critical 30°C high / 15°C low

**Column F - Humidity Thresholds (%RH):**
- Warning and critical humidity thresholds: "Warning: 25% / 70%, Critical: 20% / 80%"
- Policy recommendation: Warning 25%/70%, Critical 20%/80%

**Column G - Alert Method:**
- How alerts are sent: "Email + SMS (critical only)", "BMS alarm + email", "Dashboard alert + email"

**Column H - Alert Recipients:**
- Who receives alerts: "Facilities Manager, HVAC Technician, IT Operations"

**Column I - Data Retention (Months):**
- How long environmental data is retained: 12, 24, 36, etc.
- Policy requirement: 12 months minimum (raw data 5-min intervals), 3 years (aggregated hourly)

**Column J - Sensor Accuracy Verified:**
- Dropdown: "Yes - Within 6 months", "Yes - Within 12 months", "No / Unknown"
- Note: Sensor accuracy should be verified annually with calibrated handheld device

**Column K - Excursions Last 90 Days:**
- Number of temperature/humidity excursions in last 90 days: 0, 2, 5, 15, etc.
- Note: Frequent excursions indicate HVAC issues

**Column L - Compliance Status:**
- Formula auto-calculates based on requirements:
  - Green (✅): Sensors deployed, thresholds configured, alerts working, data retention compliant, low excursions (<5 in 90 days)
  - Amber (⚠️): Minor gaps (e.g., moderate excursions 5-10, sensor accuracy verification overdue)
  - Red (❌): Major gaps (no sensors, no alerts, high excursions >10, sensor accuracy unknown)

**Column M - Notes:**
- Any additional context: "Hot aisle containment deployed", "HVAC upgrade planned Q2 2026 to reduce excursions", "Sensors show accurate +/-0.3°C"

**Common Entries:**
- One row per server room / network closet / datacenter zone
- Multiple rows if large datacenter with multiple zones (e.g., "Datacenter 1 - Zone A", "Datacenter 1 - Zone B")
- Document excursion trends and root causes in notes

**Time Required:** 45-60 minutes for temperature/humidity monitoring inventory and excursion review

### Sheet 5: Summary Dashboard

**Purpose:** Automated compliance scoring and overall environmental protection health

**Structure:** Dashboard with formulas auto-calculating from Sheets 2-4

**What to Review (Auto-Calculated - Read-Only):**

**Overall Compliance Score:**
- Formula aggregates compliance from Fire Detection, Water Detection, Temperature/Humidity
- Displayed as percentage: 94%, 81%, etc.
- Thresholds: >90% (Green - Excellent), 75-89% (Amber - Good), 60-74% (Amber - Acceptable), <60% (Red - Non-Compliant)

**Fire Detection Score:**
- Percentage of facilities meeting all fire detection requirements
- Based on: 100% coverage, monitoring service active, testing current, fire marshal inspection current

**Water Detection Score:**
- Percentage of facilities meeting all water detection requirements
- Based on: High-risk areas covered, alert method configured, response procedure documented, testing current

**Temperature/Humidity Score:**
- Percentage of facilities meeting all temperature/humidity monitoring requirements
- Based on: Sensors deployed, thresholds configured, alerts working, data retention compliant, low excursions

**Environmental Incident Metrics:**
- Fire alarm events (last 12 months - actual fires, false alarms)
- Water damage incidents (last 12 months)
- Temperature excursions (last 90 days)
- Average response time to critical environmental events

**Key Trends:**
- Charts showing monthly environmental incident trends
- False alarm rate trends (fire alarms, water detection)
- Temperature excursion frequency over time

**Gap Summary:**
- Auto-generated list of non-compliant items requiring remediation
- Prioritized by severity (Critical → High → Medium → Low)

**What YOU Do:**
- Review dashboard after completing Sheets 2-4
- Verify auto-calculations appear correct
- Investigate any unexpected red/amber status
- Prepare remediation plan for gaps identified
- NO manual data entry in this sheet (formulas auto-populate from other sheets)

**Time Required:** 15-30 minutes for review and interpretation

### Sheet 6: Evidence Register

**Purpose:** Document all supporting evidence for audit traceability

**Structure:** Evidence log with links to actual evidence files

**What to Document (Per Evidence Item):**

**Column A - Evidence ID:**
- Unique identifier: "EVID-001", "EVID-002", etc.

**Column B - Evidence Type:**
- Dropdown: "Screenshot", "Configuration Export", "Log Sample", "Report", "Document", "Photo"

**Column C - Description:**
- What evidence shows: "Fire alarm panel configuration - Building A", "Sample fire alarm logs 01-30.01.2026", "Water sensor placement map - Datacenter 1"

**Column D - Related Sheet/Item:**
- Links evidence to assessment: "Sheet 2, Row 5 (Building A Fire Detection)", "Sheet 4, Row 3 (Datacenter 1 Temperature Monitoring)"

**Column E - File Name:**
- Evidence filename: "BuildingA_FireAlarm_Config_20260115.png", "FireAlarmLogs_Sample_20260101-30.csv", "DC1_WaterSensors_Map.pdf"

**Column F - File Location:**
- Where evidence stored: "SharePoint > ISMS > Assessments > A.7.4.2 > Evidence", "Network Drive \\server\share\evidence"

**Column G - Collection Date:**
- When evidence collected: "15.01.2026"

**Column H - Collected By:**
- Who collected evidence: "Jane Doe - Facilities Manager"

**Column I - Retention Period:**
- How long to retain: "3 years", "Permanent", "Until next assessment"

**Column J - Notes:**
- Any additional context

**Common Evidence to Collect:**

1. **Fire Detection System:**
   - Screenshot of fire alarm panel (detector count, zones, monitoring status)
   - Facility map with fire detector placements marked
   - Fire marshal inspection report (most recent annual)
   - Sample fire alarm log (30 days showing all alarms including false alarms)
   - Fire alarm testing report (most recent annual test)

2. **Water Detection System:**
   - Screenshot of water detection system configuration (sensor count, alert settings)
   - Facility map with water sensor placements marked
   - Screenshot of alert configuration (email/SMS recipients)
   - Sample water detection log (30 days)
   - Response procedure document (water damage response)

3. **Temperature/Humidity Monitoring:**
   - Screenshot of environmental monitoring dashboard (current temperature, humidity, all sensors)
   - Screenshot of threshold configuration (warning and critical thresholds)
   - Sample environmental data export (30 days with excursions highlighted)
   - Sensor accuracy verification report (if performed recently)
   - Excursion investigation reports (for significant events)

4. **Fire Suppression:**
   - Sprinkler system inspection report (annual inspection)
   - Gas suppression system test report (if applicable)
   - Photo of sprinkler heads (verify coverage)
   - Photo of gas suppression panel and cylinders (if accessible)

5. **Integration:**
   - Screenshot of BMS showing environmental systems (if BMS integrated)
   - Screenshot of security dashboard showing environmental events
   - Integration architecture diagram

**Time Required:** 2-3 hours for comprehensive evidence collection and documentation

**Storage Best Practices:**
- Use consistent file naming: [Facility]_[System]_[Type]_[Date].ext
- Organize in folders by sheet: Evidence/Sheet2_FireDetection/, Evidence/Sheet3_WaterDetection/, etc.
- Encrypt sensitive evidence if contains proprietary facility layouts
- Backup evidence to secure location (required for audit)

### Sheet 7: Approval Sign-Off

**Purpose:** Four-level approval workflow for assessment completion

**Structure:** Approval table with dates and signatures

**Approval Levels:**

**Level 1: Assessor (You)**
- Role: Assessment Completed By
- Name: [Your name]
- Date: Date you completed quality check and ready for submission
- Signature/Confirmation: Your initials or digital signature

**Level 2: Facilities Manager**
- Role: Technical Review and Approval
- Name: [Facilities Manager name]
- Date: Date Facilities Manager reviewed and approved
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
- Submit assessment workbook to Level 2 (Facilities Manager)
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
- Fire alarm panel configuration (detector count, zones, monitoring, notification devices)
- Water detection system configuration (sensor count, alert settings, coverage areas)
- Environmental monitoring platform configuration (sensor count, thresholds, data retention)
- Screenshot format preferred (shows system interface, date/time, your login)

**2. Testing and Inspection Records**
- Fire alarm testing reports (annual full system test by certified technician)
- Fire marshal inspection reports (annual inspection and approval)
- Sprinkler inspection reports (annual flow test)
- Gas suppression test reports (if applicable - annual test)
- Water detection sensor testing logs (monthly tests)
- Environmental sensor accuracy verification (annual calibration check)

**3. Log Samples**
- Fire alarm logs (30-90 days sample showing all alarms including false alarms)
- Water detection alarm logs (30-90 days sample)
- Temperature/humidity excursion logs (30-90 days with excursions highlighted)
- CSV or PDF export format acceptable

**4. Coverage Maps**
- Facility floor plans with fire detector placements marked (smoke, heat, notification devices)
- Facility floor plans with fire suppression coverage (sprinkler heads, gas suppression zones)
- Facility floor plans with water detection sensor placements marked
- Facility floor plans with temperature/humidity sensor placements marked
- PDF or image format

**5. Incident Documentation**
- Fire alarm incident reports (actual fires, significant false alarm investigations)
- Water damage incident reports (leaks, floods, near-misses)
- Temperature excursion incident reports (HVAC failures, critical threshold exceeded)
- Root cause analysis documents
- Corrective action tracking

**6. Integration Verification**
- BMS screenshots showing environmental systems integration (if applicable)
- Security dashboard screenshots showing environmental events
- Integration architecture diagrams
- Alert test results (email/SMS alert examples)

### How to Collect Evidence

**Best Practices:**

**Screenshots:**
- Use full-screen capture (shows complete system interface)
- Include date/time in screenshot (system clock visible)
- Include your login/username (proves you have access and when captured)
- Annotate if needed (highlight detector count, threshold settings)
- Save as PNG or JPEG
- File naming: [Facility]_[System]_[Description]_[Date].png

**Testing Records:**
- Export from maintenance management system or scan paper reports
- Fire alarm testing: Annual test report from certified technician
- Fire marshal inspection: Official inspection report with stamp/signature
- Sprinkler testing: Annual flow test results
- Save as PDF (preserves formatting and signatures)
- File naming: [System]_[TestType]_[Date].pdf

**Log Exports:**
- Export from native system (don't re-type into Excel)
- Fire alarm logs: Include timestamp, detector, event type (alarm, trouble, clear)
- Environmental logs: Include timestamp, sensor, temperature, humidity, threshold status
- 30-90 day sample sufficient
- Save as CSV or PDF
- File naming: [System]_[LogType]_[StartDate]-[EndDate].csv

**Maps and Diagrams:**
- Use existing facility floor plans if available
- Mark detector/sensor/sprinkler locations clearly with symbols
- Use legend (different symbols for smoke detector, heat detector, sprinkler head, water sensor, temperature sensor)
- Include coverage radius/zones if applicable
- Identify blind spots or coverage gaps
- Save as PDF or high-resolution image
- File naming: [Facility]_[SystemType]_Coverage_Map_[Date].pdf

**Photos:**
- Take photos of physical systems (fire alarm panels, gas suppression panels, sprinkler heads)
- Include context (show entire panel, not just close-up)
- Ensure photo quality sufficient (readable labels, clear view)
- Date-stamp photos if possible
- Save as JPEG
- File naming: [Facility]_[System]_Photo_[Date].jpg

### Evidence Storage

**Storage Location:**
- **Secure network share:** \\server\ISMS\Assessments\A.7.4.2_Environmental_Protection\Evidence
- **SharePoint/Cloud:** SharePoint > ISMS > Assessments > A.7.4.2 > Evidence folder
- **Organized by sheet:** Evidence/Sheet2_FireDetection/, Evidence/Sheet3_WaterDetection/, Evidence/Sheet4_TempHumidity/

**Access Control:**
- Evidence folder permissions: CISO, Facilities Manager, Compliance Officer, Internal Audit (read-only)
- Encrypt facility maps if they contain sensitive security information

**Retention:**
- Minimum: 3 years (typical audit requirement)
- Permanent: If evidence of significant incidents or major findings
- Delete after retention period (data minimization)

**Backup:**
- Evidence backed up with regular network backups
- Critical evidence: Additional copy to offline storage (external drive, tape)

---

## Common Pitfalls

### Pitfall 1: Incomplete System Inventory

**Problem:** Only documenting primary facility, missing branch offices, remote locations, or network closets

**Impact:** Audit finding - incomplete assessment scope

**How to Avoid:**
- Create master facility list BEFORE starting assessment
- Include ALL locations where [Organization] has server rooms, network closets, datacenters
- Don't forget: Network closets in branch offices, small server rooms, below-grade storage areas
- For colocation: Document customer-managed environmental systems (temperature monitoring in cage)

### Pitfall 2: Confusing Fire Code Compliance with Policy Compliance

**Problem:** Assuming "passed fire marshal inspection" = "compliant with ISMS policy"

**Example:** Fire code requires smoke detectors, but ISMS policy also requires monitoring service and BMS integration

**How to Avoid:**
- Fire code compliance is MINIMUM (life safety)
- ISMS policy requirements are ADDITIONAL (information asset protection)
- Policy may require: Monitoring service, BMS integration, environmental sensors in server rooms beyond basic code
- Assess against policy requirements (ISMS-POL-A.7.4-5-11, Section 3), not just fire code

### Pitfall 3: Assuming "Installed" Means "Working"

**Problem:** Documenting that water detection sensors exist but not verifying they work

**Example:** "We have 10 water sensors" (but 3 have dead batteries, alerts not configured)

**How to Avoid:**
- TEST systems during assessment (trigger water sensor, verify alert sent)
- Check last testing date (monthly testing required for water sensors)
- Verify alerts actually deliver (check email inbox, SMS, alarm panel)
- Status formula flags systems with testing overdue (red/amber)

### Pitfall 4: Ignoring False Alarms

**Problem:** Not documenting false alarm frequency and root causes

**Example:** Fire alarm triggers 15 false alarms per month (dust, cooking smoke) - not documented

**How to Avoid:**
- False alarm rate is KEY metric (indicates system reliability)
- Review fire alarm logs for last 90 days (count false alarms)
- If excessive false alarms (>5 per month), document in Notes
- Root cause important: Dust (clean detectors), cooking smoke (relocate detector), aging detectors (replace)

### Pitfall 5: Temperature Sensor Placement Errors

**Problem:** Documenting sensor exists but it's in wrong location (ceiling vs. equipment intake)

**Example:** "Temperature sensor installed" (but it's on ceiling - reads 5°C cooler than actual equipment intake temperature)

**How to Avoid:**
- Verify sensor placement during facility walk-through
- Sensors should be at equipment intake level (where equipment breathes), NOT ceiling
- If sensor on ceiling, note in assessment (placement suboptimal, recommend relocation)
- Compliance status = Partial if sensor placement incorrect

### Pitfall 6: Not Documenting Coverage Gaps

**Problem:** Claiming "100% coverage" without verifying blind spots

**Example:** Server room has smoke detector but no under-floor detector (smoke could smolder under floor undetected)

**How to Avoid:**
- Physical facility walk-through REQUIRED
- Check EVERY critical area: Server rooms (ceiling + under floor + in-rack for very early detection), telecom closets, below-grade storage
- Document gaps honestly (fire detector on ceiling only, missing under-floor detector)
- Gaps identified = opportunity for remediation, hidden gaps = audit finding

### Pitfall 7: Missing Environmental Excursion Analysis

**Problem:** Documenting temperature monitoring exists but not analyzing excursion frequency

**Example:** "We have temperature sensors" (but 25 excursions in last 90 days indicates HVAC chronic issues)

**How to Avoid:**
- Review excursion logs from last 90 days (count how many times thresholds exceeded)
- <5 excursions = Good, 5-10 = Acceptable (investigate trends), >10 = Problem (HVAC issues, inadequate capacity)
- Document excursion frequency in Sheet 4, Column K
- High excursions = Amber or Red compliance status, HVAC remediation required

### Pitfall 8: Stale Inspection Reports

**Problem:** Using fire marshal inspection report from 18 months ago

**Impact:** Evidence doesn't reflect current state, audit finding

**How to Avoid:**
- Fire marshal inspections are ANNUAL (12 months maximum)
- If inspection >12 months old, document as overdue in assessment
- Compliance status = Amber or Red if inspection overdue
- Schedule inspection immediately if overdue

### Pitfall 9: Forgetting Colocation Shared Responsibility

**Problem:** Assuming colocation provider handles 100% of environmental protection

**Example:** "We're in colocation, N/A" (but you're responsible for in-cage temperature monitoring, equipment-level UPS - documented in Utility Resilience, not here, but awareness needed)

**How to Avoid:**
- Colocation: Building-level systems (fire alarm, sprinklers) are provider responsibility
- Customer responsibility: In-cage environmental monitoring (temperature sensors inside cage to ensure provider HVAC adequate)
- Document responsibility split clearly
- Verify provider systems through audit reports (fire marshal inspection of building, sprinkler testing)

### Pitfall 10: Formula Corruption

**Problem:** Accidentally overwriting formula cells, breaking auto-calculations

**Example:** Compliance Status formula deleted, now shows blank instead of green/amber/red

**How to Avoid:**
- Summary Dashboard (Sheet 5) and Compliance Status columns are FORMULA CELLS - do not edit
- If formula appears broken, refer to Part II Technical Specification for correct formula
- If you must edit formula, save backup copy of workbook first
- Test formula after any changes (verify green/amber/red colors appear correctly)

---

## Quality Checklist

Before submitting for Level 2 approval (Facilities Manager), complete this self-assessment:

### Sheet 1: Instructions & Legend

- [ ] Assessment Date completed
- [ ] Completed By (your name and role)
- [ ] Organization name filled in
- [ ] All document information reviewed

### Sheet 2: Fire Detection

- [ ] ALL facilities with fire alarm systems documented (not just primary facility)
- [ ] Fire alarm panel vendor and model specified for each system
- [ ] Panel type (addressable/conventional) documented
- [ ] Smoke detector count accurate (verified against panel or physical count)
- [ ] Heat detector count accurate
- [ ] Detector technology specified (photoelectric, dual-sensor, aspirating, etc.)
- [ ] Notification device count documented (horns, strobes)
- [ ] Coverage percentage calculated and documented (100% policy requirement)
- [ ] Monitoring service status verified (professional monitoring center name, self-monitoring via BMS/SOC)
- [ ] Backup communication verified (cellular, dual path)
- [ ] Last testing date within 12 months (or documented if overdue)
- [ ] Last fire marshal inspection within 12 months (or documented if overdue)
- [ ] Compliance status column showing green/amber/red (formulas working)
- [ ] Notes column completed for any amber/red status (explain gap)
- [ ] At least one fire alarm system documented (or explicitly state "No fire alarm systems" if truly none - unlikely)

### Sheet 3: Water Detection

- [ ] ALL facilities with water detection systems documented
- [ ] Water detection system vendor and model specified
- [ ] Sensor count accurate for each system
- [ ] Sensor type specified (spot, cable, wireless, wired to BMS)
- [ ] Coverage areas listed (server rooms, basement, below-grade, under raised floors, near HVAC/plumbing)
- [ ] High-risk areas coverage assessed (all covered, partial, no coverage)
- [ ] Alert method verified (email, SMS, BMS alarm, alarm panel)
- [ ] Alert recipients documented (who gets alerts)
- [ ] Response procedure documented (yes/no - procedure exists for water damage response)
- [ ] Last testing date within 30 days (or documented if overdue)
- [ ] Compliance status column showing green/amber/red (formulas working)
- [ ] Notes column completed for any amber/red status (explain gap)
- [ ] At least one water detection system documented (or explicitly state "No water detection systems" if none)

### Sheet 4: Temperature_Humidity

- [ ] ALL facilities with temperature/humidity monitoring documented
- [ ] Monitoring platform vendor and model specified
- [ ] Sensor count accurate for each area
- [ ] Sensor locations documented (intake, exhaust, return air)
- [ ] Temperature thresholds configured (warning and critical)
- [ ] Humidity thresholds configured (warning and critical)
- [ ] Alert method verified (email, SMS, BMS alarm, dashboard)
- [ ] Alert recipients documented (who gets alerts)
- [ ] Data retention documented (12 months minimum policy requirement)
- [ ] Sensor accuracy verified within 12 months (or documented if not verified)
- [ ] Excursions last 90 days documented (count of threshold exceedances)
- [ ] Compliance status column showing green/amber/red (formulas working)
- [ ] Notes column completed for any amber/red status (explain gap, especially high excursions)
- [ ] At least one temperature/humidity monitoring system documented (or explicitly state "No environmental monitoring" if none)

### Sheet 5: Summary Dashboard

- [ ] Overall Compliance Score displays (not blank, not error)
- [ ] Fire Detection Score displays
- [ ] Water Detection Score displays
- [ ] Temperature/Humidity Score displays
- [ ] Environmental incident metrics display (fire alarms, water damage, temp excursions)
- [ ] Gap summary auto-populates (lists non-compliant items)
- [ ] Review dashboard and verify scores appear reasonable
- [ ] Investigate any unexpected red status
- [ ] NO manual data entry in dashboard (formulas auto-populate from Sheets 2-4)

### Sheet 6: Evidence Register

- [ ] At least 10 evidence items documented (comprehensive evidence collection)
- [ ] Evidence types appropriate (screenshots, logs, maps, inspection reports, photos)
- [ ] Descriptions clear
- [ ] Evidence linked to specific sheets/items
- [ ] File names match actual files
- [ ] File locations accurate (evidence actually stored there)
- [ ] Collection dates recent (during assessment period, not stale)
- [ ] Collected by documented
- [ ] Retention periods assigned
- [ ] ALL evidence files actually exist in documented location (not just documented but not collected)

**Evidence Minimum Requirements:**
- [ ] Fire alarm panel configuration screenshot(s)
- [ ] Fire marshal inspection report (most recent)
- [ ] Sample fire alarm log
- [ ] Water detection system configuration screenshot(s)
- [ ] Facility map(s) with sensor placements (fire, water, temperature)
- [ ] Temperature/humidity monitoring dashboard screenshot(s)
- [ ] Sample environmental data export (with excursions)
- [ ] At least one testing report (fire alarm annual test, sprinkler inspection, etc.)

### Sheet 7: Approval Sign-Off

- [ ] Level 1 (Assessor) completed (your name, date, signature)
- [ ] Assessment ready for submission to Level 2 (Facilities Manager)
- [ ] Assessment workbook saved with final data
- [ ] Evidence folder organized and complete

### Overall Quality

- [ ] No blank required fields (all yellow input cells completed or marked N/A if truly not applicable)
- [ ] No formula errors (#REF, #VALUE, #DIV/0 in any cell)
- [ ] Consistent facility naming across sheets (e.g., "Building A" not "Bldg A" or "Building 1")
- [ ] Dates in DD.MM.YYYY format consistently
- [ ] Compliance status colors working (green/amber/red visible)
- [ ] Notes columns used appropriately (explain gaps, not repeat data)
- [ ] Assessment tells complete story (auditor could understand environmental protection without asking you questions)

### Final Checks Before Submission

- [ ] Spell check completed
- [ ] Grammar check completed
- [ ] Data accuracy spot-checked (sample rows cross-referenced against actual systems)
- [ ] Evidence files spot-checked (open 3-5 random evidence files, verify they contain what Evidence Register says)
- [ ] Second person review requested (have colleague spot-check for obvious errors)
- [ ] Assessment workbook saved in final location
- [ ] Evidence folder backed up

**If ALL checkboxes checked:** Assessment is ready for Level 2 approval (Facilities Manager)  
**If ANY checkboxes unchecked:** Address gaps before submission

---

## Review & Approval

### Four-Level Approval Workflow

**Purpose:** Ensure assessment accuracy, completeness, and audit readiness through progressive review

**Approval Sequence:** Assessor → Facilities Manager → CISO → Compliance Officer

### Level 1: Assessor (You)

**Role:** Assessment Completion and Initial Quality Check

**Responsibilities:**
- Complete all assessment sheets (Sheets 2-4)
- Collect all required evidence (Sheet 6)
- Perform self-assessment using Quality Checklist (above)
- Address any gaps identified in self-assessment
- Complete Level 1 approval in Sheet 7 (name, date, signature)

**Approval Criteria:**
- All required fields completed (no blank yellow cells unless truly N/A)
- Evidence collected and documented
- Quality checklist 100% checked
- Assessment tells complete story

**Timeline:** Complete before submitting to Level 2

### Level 2: Facilities Manager

**Role:** Technical Review and Validation

**Responsibilities:**
- Review all system inventories for completeness (Sheets 2-4)
- Verify system counts accurate (compare to known deployments and maintenance records)
- Verify testing and inspection dates current (fire alarm testing, fire marshal inspection, water sensor testing)
- Review environmental incident documentation (fire alarms, water damage, temperature excursions)
- Spot-check evidence (open 5-10 evidence files, verify accurate - especially fire marshal inspection reports)
- Review Summary Dashboard for reasonableness
- Provide feedback to Assessor if corrections needed
- Complete Level 2 approval in Sheet 7 (name, date, signature, comments)

**Approval Criteria:**
- Technical accuracy verified (detector counts, sensor counts, inspection dates)
- Testing and inspection compliance confirmed (fire alarm testing annual, fire marshal inspection annual)
- Environmental incidents documented appropriately
- Evidence supports assessment conclusions (fire marshal report exists, testing records exist)
- No major gaps requiring immediate correction

**Timeline:** 2-5 business days after receipt from Assessor

**If Corrections Required:**
- Document required corrections in Sheet 7 Comments
- Return to Assessor for corrections
- Assessor addresses feedback, resubmits for Level 2 re-review

### Level 3: CISO

**Role:** Executive Review and Resource Allocation

**Responsibilities:**
- Review Summary Dashboard (overall compliance score)
- Review gap summary (non-compliant items requiring remediation)
- Assess remediation resource requirements (fire system upgrades, water sensor installations, HVAC improvements)
- Prioritize gaps for remediation (critical gaps first - e.g., missing fire detection in server room)
- Approve remediation plan (or request revised plan)
- Complete Level 3 approval in Sheet 7 (name, date, signature, comments)

**Approval Criteria:**
- Overall compliance score acceptable (>60% minimum, prefer >75%)
- Critical gaps have remediation plans (e.g., missing fire detection, no water sensors in below-grade area)
- Resource requirements reasonable (budget for fire system upgrades, HVAC improvements)
- Assessment aligns with organizational risk tolerance
- No strategic concerns requiring escalation

**Timeline:** 2-5 business days after Level 2 approval

**If Strategic Concerns:**
- Document concerns in Sheet 7 Comments
- May request additional analysis or revised remediation plan (e.g., cost-benefit analysis for aspirating smoke detection)
- May escalate to Executive Management if risk unacceptable (e.g., datacenter no fire suppression)

### Level 4: Compliance Officer

**Role:** Final Audit Readiness Certification

**Responsibilities:**
- Review assessment for audit readiness
- Verify evidence completeness (Evidence Register complete, files exist, fire marshal inspection reports present)
- Verify approval workflow complete (Levels 1-3 signed)
- Verify assessment format professional (no typos, consistent formatting)
- Confirm assessment meets ISO 27001:2022 Control A.7.5 requirements
- Certify assessment ready for internal/external audit
- Complete Level 4 approval in Sheet 7 (name, date, signature, comments)

**Approval Criteria:**
- Evidence complete and audit-ready (fire marshal reports, testing records, logs)
- Assessment professionally formatted
- All approval levels completed
- Assessment demonstrates compliance with policy requirements
- Assessment defensible in audit (auditor questions anticipated and addressed)

**Timeline:** 1-3 business days after Level 3 approval

**Post-Approval:**
- Assessment workbook finalized (no further edits without re-approval)
- Assessment stored in audit repository
- Assessment available to Internal Audit and External Auditors
- Assessment forms basis for Control A.7.5 compliance evidence

### Approval Workflow Best Practices

**Communication:**
- Email notification at each level transition
- Include assessment workbook as attachment
- Include evidence folder link
- Request estimated timeline for review

**Version Control:**
- File naming: ISMS-IMP-A.7.4.2_Environmental_Protection_YYYY-MM-DD_vX.xlsx
- Increment version after corrections: v1, v2, v3
- Final approved version: ISMS-IMP-A.7.4.2_Environmental_Protection_YYYY-MM-DD_FINAL.xlsx

**Tracking:**
- Use Sheet 7 Approval Sign-Off table to track progress
- Update approval dates as levels complete
- Document feedback in Comments column

**Corrections:**
- If corrections required at any level, return to Assessor
- Assessor makes corrections, increments version number
- Resubmit through workflow (start at level where corrections requested)
- Document what changed in version history

**Timeline Management:**
- Total approval timeline: 5-15 business days typical
- If urgent (e.g., imminent audit, fire marshal inspection coming), request expedited review
- Coordinate approval schedules with approvers in advance

**Audit Submission:**
- After Level 4 approval, assessment is FINAL
- Provide to Internal Audit or External Auditors as requested
- Auditor questions routed to Assessor and Facilities Manager
- Evidence files provided to auditors for verification (fire marshal reports, testing records)

---

# PART II: TECHNICAL SPECIFICATION

## Excel Workbook Structure

### Workbook Overview

**File Name:** ISMS-IMP-A.7.4.2_Environmental_Protection_YYYYMMDD.xlsx

**Generation:** Automated via Python script (generate_a74_2_environmental_protection.py)

**Sheet Count:** 7 worksheets

**Data Capacity:** 100 data rows per assessment sheet (Sheets 2-4)

**Styling:** Navy blue headers, yellow input cells, conditional formatting for compliance status (green/amber/red)

### Sheet Organization

| Sheet # | Sheet Name | Purpose | Type | Row Count |
|---------|------------|---------|------|-----------|
| 1 | Instructions & Legend | Assessment metadata and status legend | Read-only Reference | ~30 rows |
| 2 | Fire Detection | Fire alarm systems, detectors, notification devices inventory | Data Entry | 100 data rows |
| 3 | Water Detection | Water detection systems, sensors, coverage assessment | Data Entry | 100 data rows |
| 4 | Temperature_Humidity | Environmental sensors, thresholds, excursion tracking | Data Entry | 100 data rows |
| 5 | Summary Dashboard | Automated compliance scoring and metrics | Formula-driven | ~40 rows |
| 6 | Evidence Register | Supporting evidence documentation | Data Entry | 100 data rows |
| 7 | Approval Sign-Off | Four-level approval workflow | Data Entry | ~20 rows |

### Workbook Features

**Data Validation:**
- Dropdown lists for standardized input (Panel Type, Monitoring Service, Alert Method, etc.)
- Date validation (valid date format)
- Numeric validation (detector count, sensor count, excursion count)
- Percentage validation (coverage percentage 0-100%)

**Conditional Formatting:**
- Compliance Status columns: Green fill (✅ Compliant), Amber fill (⚠️ Partial), Red fill (❌ Non-Compliant)
- Summary Dashboard scores: Color-coded thresholds (>90% green, 75-89% amber, 60-74% amber, <60% red)
- Overdue dates highlighted (testing overdue, inspection overdue)
- High excursion counts highlighted (>10 excursions in 90 days)

**Formulas:**
- Summary Dashboard auto-calculates from Sheets 2-4
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
- Text: "ISMS-IMP-A.7.4.2 - Physical Environmental Protection Assessment\nISO/IEC 27001:2022 - Control A.7.5: Protecting Against Physical and Environmental Threats"
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

### Sheet 2: Fire Detection

**Purpose:** Document all fire alarm systems, detectors, notification devices, and assess compliance against policy requirements

**Header Row (Row 3):**
- Style: Gray background, bold text, center-aligned, freeze panes

**Columns:**

| Col | Field Name | Type | Width | Validation | Formula | Description |
|-----|------------|------|-------|------------|---------|-------------|
| A | Facility/System Name | Text | 25 | None | No | Facility or building name |
| B | Fire Alarm Panel | Text | 30 | None | No | Vendor and model (Simplex, Notifier, Edwards, etc.) |
| C | Panel Type | Dropdown | 15 | List | No | Addressable / Conventional / Hybrid |
| D | Smoke Detector Count | Number | 15 | Integer >0 | No | Total smoke detectors |
| E | Heat Detector Count | Number | 15 | Integer ≥0 | No | Total heat detectors (0 if none) |
| F | Detector Technology | Text | 25 | None | No | Photoelectric, Ionization, Dual-sensor, Aspirating |
| G | Notification Devices | Text | 25 | None | No | Horn/strobe count and type |
| H | Coverage Percentage | Number | 15 | Integer 0-100 | No | % of facility area covered |
| I | Monitoring Service | Dropdown | 25 | List | No | Yes - Professional / Yes - Self (BMS/SOC) / No |
| J | Backup Communication | Dropdown | 20 | List | No | Yes - Cellular / Yes - Dual path / No |
| K | Last Testing Date | Date | 15 | Date | No | Last annual fire alarm test date |
| L | Last Fire Marshal Inspection | Date | 18 | Date | No | Last fire marshal inspection date |
| M | Compliance Status | Formula | 18 | None | Yes | ✅ Compliant / ⚠️ Partial / ❌ Non-Compliant |
| N | Notes | Text | 50 | None | No | Additional context, gaps, remediation plans |

**Compliance Status Formula (Column M):**
```excel
=IF(AND(H2=100, I2<>"No", (TODAY()-K2)<=365, (TODAY()-L2)<=365), "✅ Compliant",
   IF(OR(H2<90, I2="No", (TODAY()-K2)>547, (TODAY()-L2)>547), "❌ Non-Compliant",
   "⚠️ Partial"))
```

**Logic:**
- ✅ Compliant IF: 100% coverage AND monitoring service active AND testing within 365 days AND fire marshal inspection within 365 days
- ❌ Non-Compliant IF: Coverage <90% OR no monitoring service OR testing >18 months overdue OR fire marshal inspection >18 months overdue
- ⚠️ Partial: Everything else (e.g., 95% coverage, testing slightly overdue)

**Conditional Formatting:**
- Column M: Green background if "✅ Compliant", Amber if "⚠️ Partial", Red if "❌ Non-Compliant"
- Column K: Red background if (TODAY()-K2)>365 (testing overdue)
- Column L: Red background if (TODAY()-L2)>365 (inspection overdue)

**Data Rows:** Rows 4-103 (100 data rows)

**Freeze Panes:** Row 3 (header) and Column A (facility name)

### Sheet 3: Water Detection

**Purpose:** Document all water detection systems, sensors, coverage areas, and assess compliance

**Header Row (Row 3):**
- Style: Gray background, bold text, center-aligned, freeze panes

**Columns:**

| Col | Field Name | Type | Width | Validation | Formula | Description |
|-----|------------|------|-------|------------|---------|-------------|
| A | Facility/System Name | Text | 25 | None | No | Facility or area name |
| B | Water Detection System | Text | 30 | None | No | Vendor and model |
| C | Sensor Count | Number | 12 | Integer >0 | No | Total water sensors |
| D | Sensor Type | Text | 25 | None | No | Spot, Cable, Wireless, Wired to BMS |
| E | Coverage Areas | Text | 30 | None | No | Areas protected |
| F | High-Risk Areas Covered | Dropdown | 20 | List | No | Yes - All covered / Partial - Some gaps / No - Missing coverage |
| G | Alert Method | Text | 25 | None | No | Email, SMS, BMS alarm, Alarm panel |
| H | Alert Recipients | Text | 30 | None | No | Who receives alerts |
| I | Response Procedure Documented | Dropdown | 20 | List | No | Yes / No |
| J | Last Testing Date | Date | 15 | Date | No | Last monthly water sensor test |
| K | Compliance Status | Formula | 18 | None | Yes | ✅ Compliant / ⚠️ Partial / ❌ Non-Compliant |
| L | Notes | Text | 50 | None | No | Additional context, gaps, remediation plans |

**Compliance Status Formula (Column K):**
```excel
=IF(AND(F2="Yes - All covered", G2<>"", I2="Yes", (TODAY()-J2)<=31), "✅ Compliant",
   IF(OR(F2="No - Missing coverage", G2="", I2="No", (TODAY()-J2)>60), "❌ Non-Compliant",
   "⚠️ Partial"))
```

**Logic:**
- ✅ Compliant IF: All high-risk areas covered AND alert method configured AND response procedure documented AND testing within 31 days
- ❌ Non-Compliant IF: No coverage in high-risk areas OR no alert method OR no response procedure OR testing >60 days overdue
- ⚠️ Partial: Everything else

**Conditional Formatting:**
- Column K: Green background if "✅ Compliant", Amber if "⚠️ Partial", Red if "❌ Non-Compliant"
- Column J: Red background if (TODAY()-J2)>31 (testing overdue)

**Data Rows:** Rows 4-103 (100 data rows)

**Freeze Panes:** Row 3 (header) and Column A (facility name)

### Sheet 4: Temperature_Humidity

**Purpose:** Document all temperature/humidity monitoring systems, sensors, thresholds, and assess compliance

**Header Row (Row 3):**
- Style: Gray background, bold text, center-aligned, freeze panes

**Columns:**

| Col | Field Name | Type | Width | Validation | Formula | Description |
|-----|------------|------|-------|------------|---------|-------------|
| A | Facility/System Name | Text | 25 | None | No | Facility or monitoring zone |
| B | Monitoring Platform | Text | 30 | None | No | Vendor and model |
| C | Sensor Count | Number | 12 | Integer >0 | No | Total environmental sensors |
| D | Sensor Locations | Text | 30 | None | No | Intake, exhaust, return air |
| E | Temperature Thresholds (°C) | Text | 25 | None | No | Warning and critical thresholds |
| F | Humidity Thresholds (%RH) | Text | 25 | None | No | Warning and critical thresholds |
| G | Alert Method | Text | 25 | None | No | Email, SMS, BMS alarm, Dashboard |
| H | Alert Recipients | Text | 30 | None | No | Who receives alerts |
| I | Data Retention (Months) | Number | 15 | Integer >0 | No | Months of data retained |
| J | Sensor Accuracy Verified | Dropdown | 20 | List | No | Yes - Within 6 months / Yes - Within 12 months / No / Unknown |
| K | Excursions Last 90 Days | Number | 18 | Integer ≥0 | No | Count of threshold exceedances |
| L | Compliance Status | Formula | 18 | None | Yes | ✅ Compliant / ⚠️ Partial / ❌ Non-Compliant |
| M | Notes | Text | 50 | None | No | Additional context, gaps, remediation plans |

**Compliance Status Formula (Column L):**
```excel
=IF(AND(E2<>"", F2<>"", G2<>"", I2>=12, K2<5), "✅ Compliant",
   IF(OR(E2="", G2="", I2<6, K2>10), "❌ Non-Compliant",
   "⚠️ Partial"))
```

**Logic:**
- ✅ Compliant IF: Temperature thresholds configured AND humidity thresholds configured AND alert method configured AND data retention ≥12 months AND excursions <5 in 90 days
- ❌ Non-Compliant IF: No temperature thresholds OR no alert method OR data retention <6 months OR excursions >10 in 90 days
- ⚠️ Partial: Everything else (e.g., moderate excursions 5-10, data retention 6-11 months)

**Conditional Formatting:**
- Column L: Green background if "✅ Compliant", Amber if "⚠️ Partial", Red if "❌ Non-Compliant"
- Column K: Red background if >10 (high excursions indicate HVAC issues)

**Data Rows:** Rows 4-103 (100 data rows)

**Freeze Panes:** Row 3 (header) and Column A (facility name)

### Sheet 5: Summary Dashboard

**Purpose:** Automated compliance scoring and key performance indicators

**Structure:** Dashboard layout with metrics and charts

**Row 1:** Header
- Merged cells A1:H1
- Text: "Environmental Protection - Summary Dashboard"
- Style: Navy blue background, white bold text, 14pt, center-aligned

**Rows 3-10:** Overall Compliance Score
- Row 3: "Overall Compliance Score" label
- Row 4: Formula calculating aggregate score from Sheets 2-4
- Row 5: Color-coded status (Green >90%, Amber 75-89%, Amber 60-74%, Red <60%)

**Overall Compliance Score Formula:**
```excel
=(COUNTIF('Fire Detection'!M:M,"✅ Compliant")/COUNTA('Fire Detection'!M:M)*0.4 +
  COUNTIF('Water Detection'!K:K,"✅ Compliant")/COUNTA('Water Detection'!K:K)*0.3 +
  COUNTIF(Temperature_Humidity!L:L,"✅ Compliant")/COUNTA(Temperature_Humidity!L:L)*0.3)*100
```

**Weighting:** Fire Detection 40%, Water Detection 30%, Temperature/Humidity 30%

**Rows 12-20:** Domain Scores
- Fire Detection Compliance Score (%)
- Water Detection Compliance Score (%)
- Temperature/Humidity Compliance Score (%)
- Each with formula, percentage display, color-coding

**Rows 22-30:** Environmental Incident Metrics
- Fire Alarm Events (last 12 months): Count of fire alarms (actual + false)
- Water Damage Incidents (last 12 months): Count of water detection events
- Temperature Excursions (last 90 days): Sum of excursions from Sheet 4
- Average Excursions per Facility: Average of Sheet 4, Column K

**Rows 32-50:** Gap Summary
- Auto-generated list of non-compliant items
- Formula scans Sheets 2-4 for "❌ Non-Compliant" status
- Lists facility name, system type, gap description
- Prioritized by severity

**Gap Summary Formula (example for row 32):**
```excel
=IF(COUNTIF('Fire Detection'!M:M,"❌ Non-Compliant")>0,
   INDEX('Fire Detection'!A:A, MATCH("❌ Non-Compliant",'Fire Detection'!M:M,0)) & " - Fire Detection Gap",
   IF(COUNTIF('Water Detection'!K:K,"❌ Non-Compliant")>0,
      INDEX('Water Detection'!A:A, MATCH("❌ Non-Compliant",'Water Detection'!K:K,0)) & " - Water Detection Gap",
      "No Critical Gaps Identified"))
```

**Charts:**
- Chart 1: Overall Compliance Score (gauge chart)
- Chart 2: Domain Scores (bar chart - Fire Detection, Water Detection, Temperature/Humidity)
- Chart 3: Temperature Excursion Trend (line chart - if historical data available)
- Chart 4: Gap Distribution (pie chart - compliant vs. partial vs. non-compliant)

**Conditional Formatting:**
- Compliance scores: Green >90%, Amber 75-89%, Red <60%
- Gap summary: Red highlight for critical gaps, amber for partial compliance

### Sheet 6: Evidence Register

**Purpose:** Document all supporting evidence with audit traceability

**Header Row (Row 3):**
- Style: Gray background, bold text, center-aligned, freeze panes

**Columns:**

| Col | Field Name | Type | Width | Validation | Formula | Description |
|-----|------------|------|-------|------------|---------|-------------|
| A | Evidence ID | Text | 12 | None | No | Unique identifier (EVID-001, EVID-002, etc.) |
| B | Evidence Type | Dropdown | 18 | List | No | Screenshot / Config Export / Log Sample / Report / Document / Photo |
| C | Description | Text | 40 | None | No | What evidence shows |
| D | Related Sheet/Item | Text | 25 | None | No | Links to specific assessment row |
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

### Sheet 7: Approval Sign-Off

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
| Level 2 | Facilities Manager | [Input] | [Input] | [Input] | [Input] |
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
- Applied to: All data table cells (Sheets 2-4, 6)

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
- Summary Dashboard (Sheet 5): All cells except approval override
- Compliance Status columns (Sheets 2-4): Formula-protected
- Header rows (Row 1-3 all sheets): Protected

**Unlocked Cells (Input cells):**
- All yellow background cells (user input required)
- Evidence Register (Sheet 6): All data cells
- Approval Sign-Off (Sheet 7): Name, Date, Signature, Comments cells

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
| Section 3.1: Environmental Threat Assessment | ISMS-POL-A.7.4-5-11, §3.1 | All Sheets | Geographic threats inform coverage requirements |
| Section 3.2: Fire Detection and Suppression | ISMS-POL-A.7.4-5-11, §3.2 | Sheet 2: Fire Detection | Fire alarm panels, detectors, notification devices, monitoring |
| Section 3.3: Flood and Water Damage Protection | ISMS-POL-A.7.4-5-11, §3.3 | Sheet 3: Water Detection | Water sensors, coverage, alerts, response procedures |
| Section 3.4: Temperature and Humidity Control | ISMS-POL-A.7.4-5-11, §3.4 | Sheet 4: Temperature_Humidity | Environmental sensors, thresholds, HVAC monitoring, excursions |
| Section 3.5: Structural Protection | ISMS-POL-A.7.4-5-11, §3.5 | Sheet 2 Notes | Structural protection noted where relevant (seismic, wind) |
| Section 3.6: Environmental Protection Plan | ISMS-POL-A.7.4-5-11, §3.6 | Sheet 3: Response Procedure | Response procedures documented |

**Assessment validates policy compliance by comparing deployed systems against policy requirements:**
- Policy states "100% coverage by smoke/heat detection" → Assessment verifies 100% in Sheet 2, Column H
- Policy states "Monthly water sensor testing" → Assessment verifies testing within 31 days in Sheet 3, Column J
- Policy states "Temperature monitoring with alerts" → Assessment verifies thresholds and alerts in Sheet 4, Columns E/F/G

### Integration with Other Assessments

**Feeds into:**
- ISMS-IMP-A.7.4-5-11-S4 (Compliance Dashboard): Overall compliance score, gap summary, environmental incident metrics
- ISMS-IMP-A.7.4-5-11-S3 (Utility Resilience): HVAC systems documented in both (environmental monitoring here, HVAC resilience in S3)

**Dependencies from:**
- Facility inventory: List of all facilities requiring assessment (if master facility list exists)
- Fire marshal inspection schedule: Annual inspections inform Sheet 2, Column L

**Shared evidence with:**
- Fire marshal inspection reports: Evidence for both environmental protection and facility compliance
- HVAC system documentation: Shared with utility resilience assessment (S3)

### Integration with Evidence Collection

**Evidence Register (Sheet 6) cross-references Assessment Sheets:**
- Evidence ID "EVID-003" → Related Sheet/Item: "Sheet 2, Row 4 (Building A Fire Detection)"
- File Name: "BuildingA_FireAlarm_Panel_Config_20260115.png"
- Assessment Sheet 2, Row 4, Column N (Notes): "Evidence: EVID-003"

**Evidence Traceability:**
```
Assessment Finding (Sheet 2, Row 4) ← Evidence (EVID-003) ← Evidence File (BuildingA_FireAlarm_Panel_Config_20260115.png)
```

**Audit Flow:**
1. Auditor reviews Sheet 2 (Fire Detection), identifies non-compliant item
2. Auditor checks Sheet 6 (Evidence Register) for supporting evidence ID
3. Auditor requests evidence file from File Location
4. Evidence file verifies or refutes assessment finding (fire marshal inspection report shows compliance)

### Integration with Audit Process

**Audit Deliverables:**
1. **Assessment Workbook:** ISMS-IMP-A.7.4.2_Environmental_Protection_YYYYMMDD_FINAL.xlsx (all sheets)
2. **Evidence Folder:** All files listed in Sheet 6 Evidence Register
3. **Approval Documentation:** Sheet 7 showing four-level approval workflow complete
4. **Gap Remediation Plan:** Derived from Sheet 5 Gap Summary (separate document or embedded in workbook)

**Auditor Review Process:**
1. Review Summary Dashboard (Sheet 5) for overall compliance score
2. Identify non-compliant areas (red status) in Sheets 2-4
3. Review Evidence Register (Sheet 6) for supporting evidence (especially fire marshal inspection reports)
4. Sample evidence files (verify 10-20% of evidence items, prioritize fire marshal reports and testing records)
5. Interview Facilities Manager (validate assessment accuracy, discuss remediation plans)
6. Physical facility inspection (spot-check fire detectors exist, water sensors placed correctly, temperature sensors functional)
7. Issue audit findings (if gaps identified) or confirm compliance

**Audit Questions Anticipated (Part I guides assessor to address proactively):**
- "How do you know fire detector count is accurate?" → Evidence: Fire alarm panel screenshot showing detector list
- "Is fire marshal inspection current?" → Evidence: Fire marshal inspection report within 12 months
- "Are water sensors tested monthly?" → Evidence: Testing logs showing monthly tests
- "What is temperature excursion frequency?" → Sheet 4, Column K documents excursion count, trend shown in Sheet 5
- "Are all high-risk areas covered by water detection?" → Sheet 3, Column F documents coverage status, facility maps show sensor placements

---

**END OF ISMS-IMP-A.7.4-5-11-S2 - PART II TECHNICAL SPECIFICATION**

---

**END OF ISMS-IMP-A.7.4-5-11-S2: Environmental Protection Assessment**

---

*"Assessment is not just checking off boxes for fire alarms and sensors. It's systematic evaluation—understanding what environmental protection is deployed, verifying coverage and compliance, collecting evidence, identifying gaps, and creating a defensible audit trail that demonstrates genuine protection against fire, water, and temperature threats to information assets."*