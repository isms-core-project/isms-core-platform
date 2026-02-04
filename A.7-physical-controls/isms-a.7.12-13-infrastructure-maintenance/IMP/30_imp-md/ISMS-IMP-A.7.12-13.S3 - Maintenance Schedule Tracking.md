**ISMS-IMP-A.7.12-13.S3: Maintenance Schedule Tracking**
**Assessment Specification with User Completion Guide**
### ISO/IEC 27001:2022 Control A.7.13: Equipment Maintenance

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.7.12-13.S3 |
| **Version** | 1.0 |
| **Assessment Area** | Maintenance Schedule Tracking - Preventive Maintenance Planning, Schedule Compliance, Overdue Tracking |
| **Related Policy** | ISMS-POL-A.7.12-13, Section 2.2.1 (Maintenance Programme) |
| **Purpose** | Track preventive maintenance schedules, monitor compliance, identify overdue items, and ensure equipment reliability |
| **Target Audience** | IT Operations, Facilities Management, System Administrators, Asset Managers, Compliance Officers |
| **Assessment Type** | Operational Tracking |
| **Review Cycle** | Monthly Review, Quarterly Full Assessment |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Maintenance Schedule Tracking workbook | ISMS Implementation Team |

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
  - Formula Reference
  - Validation Rules
  - Conditional Formatting Logic

---

# PART I: USER COMPLETION GUIDE

## Assessment Overview

### Purpose & Scope

**Assessment Name:** ISMS-IMP-A.7.12-13.S3 - Maintenance Schedule Tracking

#### What This Assessment Covers

This workbook provides operational TRACKING of equipment maintenance schedules. This is the "ARE we maintaining equipment on schedule?" workbook that enables:

- Tracking of preventive maintenance schedules by equipment type
- Monitoring of maintenance completion against schedules
- Identification of overdue maintenance items
- Trend analysis of maintenance compliance over time
- Early warning of upcoming maintenance requirements
- Resource planning for maintenance activities
- Vendor coordination and scheduling
- Regulatory compliance tracking for inspected equipment

#### Key Principle

This workbook is an **operational tool** used on an ongoing basis, not a one-time assessment. It should be updated regularly (monthly at minimum) to reflect:
- Completed maintenance activities
- Upcoming maintenance due dates
- Overdue items requiring attention
- Schedule changes
- New equipment additions
- Equipment decommissioning

#### What You'll Track

**Maintenance Schedules:**

- All equipment in preventive maintenance programme
- Scheduled maintenance dates (per manufacturer recommendations)
- Maintenance type (firmware, cleaning, inspection, calibration, battery check, etc.)
- Responsible party (internal, vendor)
- Warranty status and expiration dates
- Service level agreements (SLAs) with vendors

**Completion Tracking:**

- Actual completion dates
- Completion status (Completed, In Progress, Overdue, Scheduled)
- Variance from schedule
- Maintenance record reference
- Technician/vendor who performed work
- Issues discovered during maintenance

**Overdue Items:**

- Equipment with overdue maintenance
- Days overdue
- Escalation status
- Root cause for delay
- Compensating controls implemented
- Risk assessment of delay

**Upcoming Maintenance:**

- Next 30/60/90 day maintenance requirements
- Resource planning
- Vendor scheduling
- Parts and materials requirements
- Maintenance window coordination
- Change management alignment

**Historical Analysis:**

- Maintenance completion rates over time
- Recurring issues by equipment type
- Vendor performance metrics
- Cost tracking per equipment category

#### How This Relates to Other A.7.12-13 Assessments

| Assessment            | Focus                  | Relationship to A.7.12-13.S3      |
|-----------------------|------------------------|------------------------------------|
| ISMS-IMP-A.7.12-13.S1 | Cabling Security | Cable protection (separate tracking) |
| ISMS-IMP-A.7.12-13.S2 | Equipment Maintenance | Overall maintenance programme assessment |
| **ISMS-IMP-A.7.12-13.S3** | **Maintenance Schedule** | **Detailed schedule tracking tool** |
| ISMS-IMP-A.7.12-13.S4 | Compliance Dashboard | Pulls schedule compliance metrics from S3 |

This workbook (A.7.12-13.S3) is an **operational tracking tool** that supports the programme assessment in S2 and provides data to the compliance dashboard in S4.

### Who Should Use This Workbook

#### Primary Users

1. **IT Operations** - Day-to-day maintenance tracking
2. **Facilities Management** - Infrastructure equipment tracking
3. **Asset Manager** - Overall maintenance programme oversight
4. **Compliance Officers** - Schedule compliance monitoring
5. **Service Desk** - Maintenance ticket correlation
6. **Vendor Management** - External maintenance coordination

#### Secondary Users

1. **CISO** - Security equipment maintenance oversight
2. **IT Management** - Resource allocation and planning
3. **Finance** - Maintenance budget tracking
4. **Internal Audit** - Compliance verification

#### Use Frequency

- **Daily/Weekly:** Check for upcoming and overdue items
- **Monthly:** Full update of completion status, add new equipment
- **Quarterly:** Trend analysis, schedule optimisation
- **Annually:** Full programme review, vendor contract alignment

### Expected Outputs

Using this workbook provides:

1. **Current maintenance status** - Real-time view of maintenance compliance
2. **Overdue visibility** - Immediate identification of overdue items
3. **Forward planning** - Upcoming maintenance visibility (30/60/90 days)
4. **Compliance metrics** - % on-schedule, average days overdue
5. **Trend analysis** - Month-over-month compliance trends
6. **Audit evidence** - Schedule compliance documentation
7. **Resource planning** - Workload forecasting
8. **Vendor performance** - Service delivery tracking
9. **Risk indicators** - Equipment at risk due to missed maintenance
10. **Budget input** - Maintenance cost forecasting

---

## Prerequisites

### Information You'll Need

#### 1. Equipment Data

- Complete equipment inventory with asset IDs
- Manufacturer maintenance recommendations per equipment type
- Equipment criticality classifications
- Current maintenance schedule from CMMS/ITSM
- Equipment warranty information and expiration dates
- Service contract details and coverage
- Equipment age and expected lifecycle
- Location and accessibility information

#### 2. Maintenance Records

- Historical maintenance completion records
- Outstanding maintenance tickets
- Vendor maintenance schedules
- Previous maintenance findings and actions
- Recurring issue history
- Parts replacement records

#### 3. Documentation

- Maintenance procedures per equipment type
- Vendor contract maintenance schedules
- Manufacturer recommendation documents
- Regulatory inspection requirements
- Change management procedures
- Escalation procedures

#### 4. Contacts and Resources

- Internal maintenance team contact list
- Vendor contact information and escalation paths
- Emergency maintenance procedures
- After-hours support arrangements

### Required Tools

- Microsoft Excel (2016 or later)
- Access to CMMS/ITSM for maintenance records
- Access to vendor maintenance portals
- Asset management system access
- Change management system access

### System Integrations

**Recommended Integrations:**

| System | Purpose | Integration Type |
|--------|---------|------------------|
| CMMS/ITSM | Ticket synchronisation | Export/Import |
| Asset Management | Equipment inventory | API or Export |
| Vendor Portals | Schedule synchronisation | Manual or API |
| Change Management | Maintenance window alignment | Manual |
| Monitoring Systems | Alert correlation | Manual |

---

## Workflow

### Initial Setup (One-Time)

```
1. Export equipment inventory from CMMS/Asset Management
   ↓
2. Validate equipment list completeness against physical inventory
   ↓
3. Populate Sheet 2 (Equipment Schedule) with all equipment
   ↓
4. Obtain manufacturer maintenance recommendations
   ↓
5. Enter manufacturer-recommended maintenance frequencies
   ↓
6. Set scheduled dates based on frequencies
   ↓
7. Import historical completion data from CMMS
   ↓
8. Verify status calculations are correct
   ↓
9. Configure alert thresholds (Sheet 1)
   ↓
10. Train team on workbook usage and update procedures
```

### Ongoing Operation (Monthly)

```
1. Update completion status for past month
   ↓
2. Record actual completion dates
   ↓
3. Document maintenance findings and issues
   ↓
4. Identify overdue items
   ↓
5. Update Sheet 3 (Overdue Tracking) for any overdue
   ↓
6. Document escalation and compensating controls
   ↓
7. Review upcoming maintenance (next 30 days)
   ↓
8. Coordinate vendor scheduling
   ↓
9. Review Dashboard (Sheet 5) for compliance metrics
   ↓
10. Generate monthly compliance report
   ↓
11. Submit for management review
```

### Quarterly Review Process

```
1. Complete all monthly update steps
   ↓
2. Analyse 3-month compliance trend
   ↓
3. Review recurring overdue patterns
   ↓
4. Assess vendor performance
   ↓
5. Identify schedule optimisation opportunities
   ↓
6. Update maintenance frequencies if needed
   ↓
7. Review new equipment additions
   ↓
8. Verify decommissioned equipment removed
   ↓
9. Prepare quarterly compliance report for S4 dashboard
   ↓
10. Management review and sign-off
```

### Annual Review Process

```
1. Complete quarterly review steps
   ↓
2. Full equipment inventory reconciliation
   ↓
3. Manufacturer recommendation review
   ↓
4. Vendor contract renewal alignment
   ↓
5. Historical trend analysis (12 months)
   ↓
6. Budget planning for next year
   ↓
7. Procedure updates if needed
   ↓
8. Staff training refresh
   ↓
9. ISMS audit preparation
   ↓
10. Document lessons learned
```

---

## Completing Each Sheet

### Sheet 1: Instructions & Configuration

**Purpose:** Workbook configuration and instructions

**What to Complete:**

- Organisation name
- Workbook start date
- Responsible department
- Update frequency (Monthly recommended)
- Primary contact for maintenance coordination
- CMMS/ITSM system reference
- Version control information

**Configuration Settings:**

- Days before due to flag as "Upcoming": 30 (default)
- Days overdue to escalate: 14 (default)
- Critical equipment overdue escalation: 7 (default)
- Warning threshold for "Due Soon": 30 days
- Critical threshold for immediate alert: 7 days

**Alert Configuration:**

| Alert Type | Default Threshold | Customisable |
|------------|-------------------|--------------|
| Upcoming Warning | 30 days | Yes |
| Due Soon Alert | 14 days | Yes |
| Overdue Alert | 1 day | No |
| Critical Escalation | 7 days overdue | Yes |
| Tier 1 Equipment | 3 days overdue | Yes |

**Time Required:** 15-30 minutes for initial configuration

### Sheet 2: Equipment Schedule

**Purpose:** Master maintenance schedule for all equipment

**Structure:** 200 data rows for equipment tracking

**What to Document (Per Equipment):**

**Column A - Equipment ID:**

- Asset tag: "SRV-001", "UPS-DC1-01"
- Must be unique
- Match with CMMS/Asset Management system
- Use consistent naming convention

**Column B - Equipment Type:**

- Dropdown: "Server", "Network Device", "Storage", "UPS", "HVAC", "Generator", "Security System", "Fire Suppression", "Access Control", "CCTV", "Environmental Sensors", "PDU", "Cable Infrastructure", "Other"

**Column C - Equipment Description:**

- Model/description: "Dell PowerEdge R740"
- Include manufacturer and model number
- Include capacity/specification if relevant

**Column D - Location:**

- Where located: "Datacenter 1 - Rack A1"
- Use consistent location naming
- Include room, rack, position if applicable

**Column E - Criticality:**

- Dropdown: "Tier 1 - Critical", "Tier 2 - Standard", "Tier 3 - Low"
- Based on business impact assessment
- Aligns with asset classification

**Column F - Maintenance Type:**

- Type of maintenance: "Firmware Update", "Inspection", "Battery Check", "Filter Replacement", "Calibration", "Full Service", "Cleaning", "Testing", "Component Replacement"
- Multiple maintenance types may apply (create separate rows)

**Column G - Frequency:**

- Dropdown: "Weekly", "Monthly", "Quarterly", "Semi-annually", "Annually", "Bi-annually"
- Based on manufacturer recommendations
- May be adjusted based on environment/usage

**Column H - Responsible Party:**

- Dropdown: "Internal - IT", "Internal - Facilities", "Vendor", "Manufacturer", "Contractor"
- Clear accountability assignment

**Column I - Last Completed:**

- Date of last maintenance: "15.12.2025"
- Swiss date format (DD.MM.YYYY)
- Required for status calculation

**Column J - Next Due:**

- Formula: Calculates based on last completed + frequency
- Automatically updated when Last Completed changes

**Column K - Status:**

- Formula auto-calculates:
  - "Current" (next due > today + 30 days)
  - "Due Soon" (next due within 30 days)
  - "Overdue" (next due < today)

**Column L - Days Until Due / Overdue:**

- Formula: Calculates days until or since due date
- Positive = days until due
- Negative = days overdue

**Column M - Maintenance Record Ref:**

- Reference to maintenance record: "TKT-2025-1234"
- Links to CMMS/ITSM ticket
- Required for audit trail

**Column N - Warranty Status:**

- Dropdown: "In Warranty", "Out of Warranty", "Extended Warranty", "N/A"
- Impacts vendor responsibility

**Column O - Contract Reference:**

- Service contract number if applicable
- Vendor contract reference

**Column P - Notes:**

- Any additional context
- Special requirements
- Known issues

**Time Required:** Initial setup 2-3 hours, monthly updates 30-60 minutes

### Sheet 3: Overdue Tracking

**Purpose:** Detailed tracking of overdue maintenance items

**Structure:** Filtered view of overdue items with escalation tracking

**What to Document (Per Overdue Item):**

**Column A - Equipment ID:**

- Pulled from Sheet 2
- Unique identifier

**Column B - Equipment Description:**

- Pulled from Sheet 2
- For quick identification

**Column C - Criticality:**

- Tier 1, Tier 2, or Tier 3
- Impacts escalation timeline

**Column D - Maintenance Type:**

- What maintenance is overdue
- From Sheet 2

**Column E - Original Due Date:**

- When it was due
- From Sheet 2

**Column F - Days Overdue:**

- Formula: Today - Due Date
- Automatically calculated

**Column G - Reason for Delay:**

- Dropdown: "Parts on Order", "Vendor Scheduling", "Resource Unavailable", "Budget Hold", "Awaiting Change Window", "Equipment Access Issue", "Dependency on Other Work", "Other"
- Required for all overdue items

**Column H - Detailed Explanation:**

- Free text explanation
- Why the delay occurred
- What is being done to resolve

**Column I - Estimated Completion:**

- Revised completion date
- When maintenance is now expected

**Column J - Escalated:**

- Dropdown: "Yes", "No"
- Required if overdue > threshold

**Column K - Escalated To:**

- Who it was escalated to: "IT Manager", "CISO", "Vendor Manager"
- Required if Escalated = Yes

**Column L - Escalation Date:**

- When escalation occurred
- For tracking response time

**Column M - Compensating Control:**

- Any interim measures: "Increased monitoring", "Backup system in place", "Manual checks implemented", "Redundancy active"
- Required for critical equipment

**Column N - Risk Assessment:**

- Impact of delay: "Low", "Medium", "High", "Critical"
- Based on equipment criticality and delay duration

**Column O - Resolution Notes:**

- Update when resolved
- Document actions taken

**Column P - Actual Completion Date:**

- When finally completed
- For variance analysis

**Time Required:** 15-30 minutes per overdue item

### Sheet 4: Upcoming Maintenance

**Purpose:** Forward-looking view of maintenance due in next 90 days

**Structure:** Auto-filtered list from Sheet 2

**Categories:**

- Next 7 Days (immediate scheduling required)
- 8-14 Days (schedule this week)
- 15-30 Days (schedule this month)
- 31-60 Days (plan scheduling)
- 61-90 Days (advance notice)

**Planning Fields:**

- Scheduled Date (planned completion)
- Assigned To (technician/vendor)
- Parts/Resources Required
- Estimated Duration
- Vendor Booked (Yes/No)
- Change Request Number (if required)
- Maintenance Window (date/time)
- Pre-requisites (dependencies)
- Post-maintenance Testing Required

**Coordination Notes:**

- System dependencies
- User notifications required
- Rollback plan needed (Yes/No)

### Sheet 5: Dashboard

**Purpose:** Summary metrics and compliance status

**Key Metrics (Auto-Calculated):**

**Overall Compliance:**

- Total equipment in programme
- Equipment current (%)
- Equipment due soon (%)
- Equipment overdue (%)
- Compliance trend (vs. previous month)

**Compliance by Type:**

- Servers: X% current
- Network: X% current
- Storage: X% current
- UPS: X% current
- HVAC: X% current
- Security Systems: X% current
- Other: X% current

**Compliance by Criticality:**

- Tier 1 (Critical): X% current
- Tier 2 (Standard): X% current
- Tier 3 (Low): X% current

**Overdue Summary:**

- Total overdue items
- Average days overdue
- Longest overdue item
- Critical equipment overdue (count)
- Items escalated (count)
- Items with compensating controls (count)

**Trend (Rolling 6 Months):**

- Compliance % by month
- Overdue count by month
- Average resolution time

**Upcoming Workload:**

- Next 7 days: X items
- 8-14 days: X items
- 15-30 days: X items
- 31-60 days: X items
- 61-90 days: X items

**Vendor Workload:**

- Internal IT: X items this month
- Internal Facilities: X items this month
- Vendor (by vendor): X items this month

### Sheet 6: Maintenance Log

**Purpose:** Historical record of completed maintenance

**What to Document (Per Completion):**

- Equipment ID
- Equipment Description
- Maintenance Type
- Scheduled Date
- Actual Completion Date
- Variance (days early/late)
- Performed By (name/vendor)
- Maintenance Record Reference
- Findings/Notes
- Parts Replaced
- Cost (if tracked)
- Follow-up Required (Yes/No)
- Follow-up Action (if required)
- Next Scheduled Date

### Sheet 7: Evidence Register

**Purpose:** Link to supporting evidence

**Evidence Types:**

- Maintenance tickets/records
- Vendor service reports
- Test reports
- Inspection certificates
- Calibration certificates
- Firmware update confirmations
- Photographs (before/after)
- Sign-off documentation

**Evidence Fields:**

| Field | Description |
|-------|-------------|
| Evidence ID | Unique identifier |
| Equipment ID | Related equipment |
| Maintenance Date | When performed |
| Evidence Type | Category of evidence |
| Document Reference | File name/ticket number |
| Storage Location | Where stored (SharePoint, CMMS, etc.) |
| Retention Period | How long to keep |
| Last Verified | When evidence last confirmed accessible |

---

## Evidence Collection

### What Evidence to Collect

**Mandatory Evidence:**

1. **Maintenance Tickets** - CMMS/ITSM records for each maintenance activity
2. **Completion Confirmations** - Sign-off from technician/vendor
3. **Test Reports** - Post-maintenance testing results
4. **Vendor Service Reports** - For contracted maintenance

**Recommended Evidence:**

5. **Photographs** - Before/after for physical maintenance
6. **Screenshots** - Firmware versions, system logs
7. **Calibration Certificates** - For measuring equipment
8. **Inspection Reports** - For regulatory equipment

### Evidence Storage Location

**Primary Storage:** ISMS Evidence Library (SharePoint or equivalent)

**Folder Structure:**
```
/ISMS-Evidence/
  /A.7.13-Equipment-Maintenance/
    /Maintenance-Records/
      /2026/
        /01-January/
        /02-February/
        ...
    /Vendor-Reports/
    /Certificates/
    /Test-Results/
```

### Retention Requirements

| Evidence Type | Retention Period | Basis |
|---------------|------------------|-------|
| Maintenance Records | 5 years | ISO 27001 |
| Vendor Reports | Contract term + 3 years | Contractual |
| Calibration Certs | Calibration interval + 1 year | Regulatory |
| Test Results | 3 years | Operational |

---

## Common Pitfalls

### Pitfall 1: Not Updating Completion Status

**MISTAKE:** Maintenance completed but workbook not updated

**Impact:** Dashboard shows false overdue items, compliance metrics incorrect

**How to Avoid:**
- Update workbook as part of maintenance closure process
- Monthly reconciliation against CMMS
- Include workbook update in maintenance procedure checklist

### Pitfall 2: Missing Equipment

**MISTAKE:** New equipment not added to schedule

**Impact:** Equipment lacks maintenance, potential failure, audit finding

**How to Avoid:**
- Integrate with asset management process
- Quarterly audit of equipment vs. schedule
- Include in equipment commissioning checklist

### Pitfall 3: Incorrect Frequencies

**MISTAKE:** Maintenance frequency doesn't match manufacturer recommendations

**Impact:** Over-maintenance (wasted resources) or under-maintenance (equipment failure)

**How to Avoid:**
- Verify against manufacturer documentation
- Review during S2 assessment
- Document source of frequency determination

### Pitfall 4: No Overdue Escalation

**MISTAKE:** Items remain overdue without escalation or compensating controls

**Impact:** Security risk, audit finding, potential equipment failure

**How to Avoid:**
- Weekly review of overdue items
- Escalation after defined period (14 days standard, 7 days critical)
- Document compensating controls for all overdue critical equipment

### Pitfall 5: Stale Upcoming View

**MISTAKE:** Upcoming maintenance not scheduled until last minute

**Impact:** Rushed scheduling, missed windows, quality issues

**How to Avoid:**
- Weekly review of next 30 days
- Pre-schedule vendor maintenance 60 days out
- Coordinate with change management calendar

### Pitfall 6: Inconsistent Equipment IDs

**MISTAKE:** Using different IDs in workbook vs. CMMS/Asset Management

**Impact:** Cannot correlate records, audit trail broken

**How to Avoid:**
- Use CMMS asset IDs as primary identifier
- Cross-reference in Notes field if needed
- Annual reconciliation with asset register

### Pitfall 7: Missing Maintenance Types

**MISTAKE:** Only tracking one maintenance type per equipment

**Impact:** Other maintenance types missed, incomplete coverage

**How to Avoid:**
- Create separate row for each maintenance type per equipment
- Review manufacturer recommendations for all maintenance types
- Include firmware, inspection, cleaning, calibration as separate items

### Pitfall 8: No Variance Analysis

**MISTAKE:** Not tracking actual vs. scheduled completion variance

**Impact:** Cannot identify systemic scheduling issues

**How to Avoid:**
- Record both scheduled and actual dates
- Calculate variance in Maintenance Log
- Monthly review of average variance by type/vendor

### Pitfall 9: Incomplete Evidence References

**MISTAKE:** Maintenance marked complete without ticket/evidence reference

**Impact:** Cannot prove maintenance occurred, audit finding

**How to Avoid:**
- Require ticket reference before marking complete
- Verify evidence exists in CMMS
- Quarterly evidence verification sample

### Pitfall 10: Ignoring Warranty Status

**MISTAKE:** Performing vendor maintenance on equipment still under warranty

**Impact:** May void warranty, unnecessary cost

**How to Avoid:**
- Track warranty status (Column N)
- Review warranty before scheduling internal maintenance
- Coordinate with vendor for warranty equipment

### Pitfall 11: No Compensating Controls for Overdue Critical Equipment

**MISTAKE:** Critical equipment overdue without interim risk mitigation

**Impact:** Security exposure, potential for undetected failure

**How to Avoid:**
- Mandatory compensating control field for Tier 1 equipment
- Weekly review of overdue critical items
- Escalation to CISO for critical overdue >7 days

### Pitfall 12: Decommissioned Equipment Still in Schedule

**MISTAKE:** Equipment removed from service but still tracked for maintenance

**Impact:** False overdue items, skewed compliance metrics

**How to Avoid:**
- Process to mark equipment as decommissioned
- Remove from active schedule (move to archive)
- Monthly check against asset status

### Pitfall 13: No Vendor Performance Tracking

**MISTAKE:** Not tracking vendor maintenance delivery against SLA

**Impact:** Cannot hold vendors accountable, ongoing service issues

**How to Avoid:**
- Track responsible party (Column H)
- Monitor completion variance by vendor
- Quarterly vendor performance review

### Pitfall 14: Formula Errors Not Detected

**MISTAKE:** Status formulas broken, showing incorrect status

**Impact:** False compliance view, missed overdue items

**How to Avoid:**
- Test formulas after any structural changes
- Include formula validation in monthly review
- Sanity check: manual count vs. formula count

### Pitfall 15: No Backup of Workbook

**MISTAKE:** Single copy of workbook, no version control

**Impact:** Data loss if file corrupted, no audit trail of changes

**How to Avoid:**
- Store in SharePoint/OneDrive with version history
- Monthly backup to secure location
- Document last known good date

### Pitfall 16: Incomplete Location Information

**MISTAKE:** Equipment location too vague to find equipment

**Impact:** Maintenance delayed while locating equipment

**How to Avoid:**
- Include building, room, rack, position
- Use consistent location naming convention
- Verify locations during annual review

### Pitfall 17: No Change Management Alignment

**MISTAKE:** Maintenance scheduled without change window approval

**Impact:** Maintenance blocked, potential for uncontrolled changes

**How to Avoid:**
- Check change calendar before scheduling
- Include change request reference for system changes
- Coordinate with CAB for production systems

### Pitfall 18: Missing Post-Maintenance Testing

**MISTAKE:** Maintenance marked complete without verifying system functionality

**Impact:** Issues not discovered until production impact

**How to Avoid:**
- Include testing in maintenance procedure
- Document test results
- Require test sign-off before completion

---

## Quality Checklist

### Sheet 1: Instructions & Configuration

- [ ] Organisation name entered correctly
- [ ] Responsible department identified
- [ ] Update frequency documented (Monthly recommended)
- [ ] Primary contact specified
- [ ] Alert thresholds configured appropriately
- [ ] All configuration fields completed
- [ ] Version control information current

### Sheet 2: Equipment Schedule

- [ ] ALL equipment in maintenance programme included
- [ ] No duplicate equipment IDs
- [ ] Manufacturer frequencies documented for all equipment
- [ ] Frequencies verified against manufacturer documentation
- [ ] All criticality levels assigned
- [ ] Last completed dates accurate (verified against CMMS)
- [ ] Status formulas working correctly (spot check 5 items)
- [ ] Days Until/Overdue calculating correctly
- [ ] All maintenance types captured (multiple rows if needed)
- [ ] Responsible party assigned for all items
- [ ] Warranty status documented
- [ ] Service contract references included where applicable
- [ ] Locations specific enough to find equipment
- [ ] No blank required fields

### Sheet 3: Overdue Tracking

- [ ] ALL overdue items from Sheet 2 captured
- [ ] Reasons documented for all overdue items
- [ ] Estimated completion dates provided
- [ ] Escalation tracked (Yes/No) for items over threshold
- [ ] Escalation recipient documented when escalated
- [ ] Compensating controls documented for Tier 1 equipment
- [ ] Risk assessment completed for all overdue
- [ ] No items overdue > 30 days without CISO awareness

### Sheet 4: Upcoming Maintenance

- [ ] All items due in next 90 days visible
- [ ] Items in next 7 days have scheduled dates
- [ ] Vendor items have booking confirmation
- [ ] Parts/resources identified for upcoming work
- [ ] Change windows aligned for system maintenance
- [ ] No scheduling conflicts identified

### Sheet 5: Dashboard

- [ ] Total equipment count matches Sheet 2
- [ ] Metrics calculating correctly (spot check)
- [ ] Compliance percentages sum correctly
- [ ] Trends showing meaningful data (not flat/zero)
- [ ] No formula errors (#REF!, #DIV/0!, etc.)
- [ ] All equipment types represented
- [ ] Critical equipment metrics accurate
- [ ] Overdue summary matches Sheet 3

### Sheet 6: Maintenance Log

- [ ] All completed maintenance in past quarter logged
- [ ] Ticket references provided for all entries
- [ ] Variance calculated (actual vs. scheduled)
- [ ] Findings documented where applicable
- [ ] Follow-up items tracked

### Sheet 7: Evidence Register

- [ ] Evidence referenced for all completed maintenance
- [ ] Storage locations accessible and verified
- [ ] Evidence types correctly categorised
- [ ] Retention periods documented
- [ ] Sample of evidence verified accessible (quarterly)

### Overall Workbook Quality

- [ ] Workbook opens without errors
- [ ] All sheets accessible and formatted correctly
- [ ] Conditional formatting working (status colours)
- [ ] Dropdowns functioning on all data entry fields
- [ ] No unprotected formula cells
- [ ] Version date updated
- [ ] Backup copy exists

### Cross-Reference Verification

- [ ] Equipment IDs match asset management system exactly
- [ ] Criticality tiers align with business impact assessment
- [ ] Vendor contract references verified current
- [ ] Warranty expiration dates confirmed accurate
- [ ] Service level agreements documented and current
- [ ] Escalation contacts verified and reachable
- [ ] CMMS ticket references valid and accessible
- [ ] Evidence storage locations confirmed accessible
- [ ] Maintenance procedures referenced exist and are current
- [ ] Integration with S4 Dashboard tested and working

### Data Integrity Checks

- [ ] No orphaned records (equipment removed but log entries remain)
- [ ] Date sequences logical (last completed before next due)
- [ ] No future dates in Last Completed column
- [ ] Frequency values match manufacturer recommendations
- [ ] Status formulas calculate correctly for edge cases
- [ ] Days overdue values reasonable (no extreme outliers unexplained)
- [ ] Trend data consistent with historical records
- [ ] Backup verification completed this period

---

## Review & Approval

### Monthly Review Process

**Reviewer:** IT Operations Manager or Facilities Manager

**Review Steps:**

1. Open workbook and verify no errors
2. Check Sheet 5 Dashboard for current compliance status
3. Review all overdue items on Sheet 3
4. Verify escalations are current
5. Review upcoming maintenance (next 30 days)
6. Sample check 5 items for accuracy
7. Sign off monthly review

**Evidence:** Documented review notes, signature

### Quarterly Review Process

**Reviewer:** Asset Manager or Compliance Officer

**Review Steps:**

1. Complete monthly review
2. Analyse 3-month compliance trend
3. Review vendor performance
4. Verify evidence sample (10%)
5. Check for recurring issues
6. Update S4 Compliance Dashboard
7. Present to IT Management
8. Document improvement actions

**Evidence:** Quarterly compliance report, meeting minutes

### Annual Review Process

**Reviewer:** CISO or IT Director

**Review Steps:**

1. Complete quarterly review
2. Full equipment reconciliation with asset register
3. Manufacturer recommendation review
4. Contract/vendor review
5. 12-month trend analysis
6. Budget planning input
7. Procedure update if needed
8. Staff training review
9. Document lessons learned
10. Sign off annual review

**Evidence:** Annual compliance report, improvement plan

---

# PART II: TECHNICAL SPECIFICATION

## Excel Workbook Structure

### Workbook Overview

**File Name:** ISMS-IMP-A.7.12-13.S3_Maintenance_Schedule_YYYYMMDD.xlsx

**Generation:** Automated via Python script (generate_a712_3_maintenance_schedule.py)

**Sheet Count:** 7 worksheets

**Styling:** Navy blue headers, yellow input cells, conditional formatting for status

**Protection:** Formula cells protected, input cells unlocked

### Sheet Organisation

| Sheet # | Sheet Name | Purpose | Type | Row Count |
|---------|------------|---------|------|-----------|
| 1 | Instructions | Configuration and instructions | Reference | ~50 rows |
| 2 | Equipment Schedule | Master maintenance schedule | Data Entry | 200 rows |
| 3 | Overdue Tracking | Overdue item management | Data Entry | 50 rows |
| 4 | Upcoming Maintenance | Forward planning | Formula-driven | ~100 rows |
| 5 | Dashboard | Compliance metrics | Formula-driven | ~60 rows |
| 6 | Maintenance Log | Completion history | Data Entry | 500 rows |
| 7 | Evidence Register | Supporting evidence | Data Entry | 100 rows |

---

## Sheet-by-Sheet Specifications

### Sheet 1: Instructions & Configuration

**Purpose:** Workbook configuration, thresholds, and user instructions

**Structure:**

| Row Range | Content | Type |
|-----------|---------|------|
| 1-3 | Title and version | Static |
| 5-15 | Configuration fields | Input |
| 17-25 | Alert thresholds | Input |
| 27-50 | User instructions | Static |

**Configuration Fields:**

| Cell | Field | Type | Default |
|------|-------|------|---------|
| B5 | Organisation Name | Text | [Enter] |
| B6 | Department | Text | IT Operations |
| B7 | Start Date | Date | [Today] |
| B8 | Update Frequency | Dropdown | Monthly |
| B9 | Primary Contact | Text | [Enter] |
| B10 | CMMS System | Text | ServiceNow |

**Alert Threshold Fields:**

| Cell | Field | Type | Default |
|------|-------|------|---------|
| B17 | Upcoming Warning (days) | Number | 30 |
| B18 | Due Soon Alert (days) | Number | 14 |
| B19 | Critical Escalation (days overdue) | Number | 7 |
| B20 | Tier 1 Escalation (days overdue) | Number | 3 |

### Sheet 2: Equipment Schedule

**Columns:**

| Col | Field Name | Type | Width | Validation |
|-----|------------|------|-------|------------|
| A | Equipment ID | Text | 15 | None |
| B | Equipment Type | Dropdown | 18 | Server, Network Device, Storage, UPS, HVAC, Generator, Security System, Fire Suppression, Access Control, CCTV, Environmental Sensors, PDU, Cable Infrastructure, Other |
| C | Equipment Description | Text | 35 | None |
| D | Location | Text | 25 | None |
| E | Criticality | Dropdown | 18 | Tier 1 - Critical, Tier 2 - Standard, Tier 3 - Low |
| F | Maintenance Type | Dropdown | 20 | Firmware Update, Inspection, Battery Check, Filter Replacement, Calibration, Full Service, Cleaning, Testing, Component Replacement |
| G | Frequency | Dropdown | 15 | Weekly, Monthly, Quarterly, Semi-annually, Annually, Bi-annually |
| H | Responsible Party | Dropdown | 20 | Internal - IT, Internal - Facilities, Vendor, Manufacturer, Contractor |
| I | Last Completed | Date | 15 | Date |
| J | Next Due | Formula | 15 | =I2+VLOOKUP(G2,FrequencyTable,2,FALSE) |
| K | Status | Formula | 15 | See formula below |
| L | Days Until/Overdue | Formula | 15 | =J2-TODAY() |
| M | Maintenance Record Ref | Text | 20 | None |
| N | Warranty Status | Dropdown | 18 | In Warranty, Out of Warranty, Extended Warranty, N/A |
| O | Contract Reference | Text | 15 | None |
| P | Notes | Text | 40 | None |

**Frequency Lookup Table (Named Range: FrequencyTable):**

| Frequency | Days |
|-----------|------|
| Weekly | 7 |
| Monthly | 30 |
| Quarterly | 90 |
| Semi-annually | 180 |
| Annually | 365 |
| Bi-annually | 730 |

**Status Formula (Column K):**

```excel
=IF(J2="","",IF(J2>TODAY()+$B$17,"Current",IF(J2>TODAY(),"Due Soon","Overdue")))
```

**Where $B$17 is the Upcoming Warning threshold from Sheet 1**

**Conditional Formatting Rules (Column K):**

| Value | Background | Font |
|-------|------------|------|
| Current | #C6EFCE (Green) | Black |
| Due Soon | #FFEB9C (Amber) | Black |
| Overdue | #FFC7CE (Red) | Dark Red |

### Sheet 3: Overdue Tracking

**Columns:**

| Col | Field Name | Type | Width | Validation |
|-----|------------|------|-------|------------|
| A | Equipment ID | Text | 15 | None |
| B | Equipment Description | Text | 30 | None |
| C | Criticality | Dropdown | 18 | Tier 1 - Critical, Tier 2 - Standard, Tier 3 - Low |
| D | Maintenance Type | Text | 20 | None |
| E | Original Due Date | Date | 15 | Date |
| F | Days Overdue | Formula | 12 | =TODAY()-E2 |
| G | Reason for Delay | Dropdown | 22 | Parts on Order, Vendor Scheduling, Resource Unavailable, Budget Hold, Awaiting Change Window, Equipment Access Issue, Dependency on Other Work, Other |
| H | Detailed Explanation | Text | 40 | None |
| I | Estimated Completion | Date | 15 | Date |
| J | Escalated | Dropdown | 10 | Yes, No |
| K | Escalated To | Text | 20 | None |
| L | Escalation Date | Date | 15 | Date |
| M | Compensating Control | Text | 35 | None |
| N | Risk Assessment | Dropdown | 12 | Low, Medium, High, Critical |
| O | Resolution Notes | Text | 40 | None |
| P | Actual Completion Date | Date | 15 | Date |

**Conditional Formatting (Column F - Days Overdue):**

| Days | Background |
|------|------------|
| 1-7 | #FFE4B5 (Light Orange) |
| 8-14 | #FFA500 (Orange) |
| 15-30 | #FFC7CE (Light Red) |
| >30 | #FF0000 (Red) |

**Conditional Formatting (Row - if Criticality = "Tier 1 - Critical" AND Escalated = "No" AND Days Overdue > 3):**
- Red border around entire row

### Sheet 4: Upcoming Maintenance

**Columns:**

| Col | Field Name | Type | Width | Validation |
|-----|------------|------|-------|------------|
| A | Equipment ID | Text | 15 | None |
| B | Equipment Description | Text | 30 | None |
| C | Criticality | Text | 18 | None |
| D | Maintenance Type | Text | 20 | None |
| E | Due Date | Date | 15 | None |
| F | Days Until Due | Formula | 12 | =E2-TODAY() |
| G | Time Category | Formula | 15 | See formula |
| H | Scheduled Date | Date | 15 | Date |
| I | Assigned To | Text | 20 | None |
| J | Parts Required | Text | 30 | None |
| K | Vendor Booked | Dropdown | 12 | Yes, No, N/A |
| L | Change Request | Text | 15 | None |
| M | Maintenance Window | Text | 20 | None |
| N | Notes | Text | 35 | None |

**Time Category Formula (Column G):**

```excel
=IF(F2<=7,"1-Next 7 Days",IF(F2<=14,"2-8-14 Days",IF(F2<=30,"3-15-30 Days",IF(F2<=60,"4-31-60 Days","5-61-90 Days"))))
```

**Conditional Formatting (Column G):**

| Category | Background |
|----------|------------|
| 1-Next 7 Days | #FFC7CE (Light Red) |
| 2-8-14 Days | #FFE4B5 (Light Orange) |
| 3-15-30 Days | #FFEB9C (Light Amber) |
| 4-31-60 Days | #FFFFCC (Light Yellow) |
| 5-61-90 Days | #C6EFCE (Light Green) |

### Sheet 5: Dashboard

**Purpose:** Summary metrics and compliance status

**Layout:**

| Row Range | Content |
|-----------|---------|
| 1-5 | Title and report period |
| 7-18 | Overall compliance metrics |
| 20-35 | Compliance by type |
| 37-45 | Compliance by criticality |
| 47-60 | Overdue summary |
| 62-75 | Trend data (6 months) |
| 77-90 | Upcoming workload |

**Metrics Formulas:**

**Total Equipment:**
```excel
=COUNTA('Equipment Schedule'!A:A)-1
```

**Equipment Current (%):**
```excel
=COUNTIF('Equipment Schedule'!K:K,"Current")/B8*100
```

**Equipment Due Soon (%):**
```excel
=COUNTIF('Equipment Schedule'!K:K,"Due Soon")/B8*100
```

**Equipment Overdue:**
```excel
=COUNTIF('Equipment Schedule'!K:K,"Overdue")
```

**Critical Equipment Overdue:**
```excel
=COUNTIFS('Equipment Schedule'!K:K,"Overdue",'Equipment Schedule'!E:E,"Tier 1 - Critical")
```

**Average Days Overdue (for overdue items):**
```excel
=AVERAGEIF('Equipment Schedule'!K:K,"Overdue",'Equipment Schedule'!L:L)*-1
```

**Longest Overdue (days):**
```excel
=MIN('Equipment Schedule'!L:L)*-1
```

**Compliance by Type formulas:**

```excel
=COUNTIFS('Equipment Schedule'!B:B,"Server",'Equipment Schedule'!K:K,"Current")/COUNTIF('Equipment Schedule'!B:B,"Server")*100
```

**Compliance by Criticality formulas:**

```excel
=COUNTIFS('Equipment Schedule'!E:E,"Tier 1 - Critical",'Equipment Schedule'!K:K,"Current")/COUNTIF('Equipment Schedule'!E:E,"Tier 1 - Critical")*100
```

### Sheet 6: Maintenance Log

**Columns:**

| Col | Field Name | Type | Width |
|-----|------------|------|-------|
| A | Log ID | Auto-increment | 10 |
| B | Equipment ID | Text | 15 |
| C | Equipment Description | Text | 30 |
| D | Maintenance Type | Text | 20 |
| E | Scheduled Date | Date | 15 |
| F | Actual Completion Date | Date | 15 |
| G | Variance (Days) | Formula | 12 |
| H | Performed By | Text | 20 |
| I | Ticket Reference | Text | 15 |
| J | Findings/Notes | Text | 40 |
| K | Parts Replaced | Text | 25 |
| L | Cost (CHF) | Number | 12 |
| M | Follow-up Required | Dropdown | 12 |
| N | Follow-up Action | Text | 35 |
| O | Next Scheduled | Date | 15 |

**Variance Formula (Column G):**
```excel
=F2-E2
```

**Conditional Formatting (Column G - Variance):**

| Variance | Background |
|----------|------------|
| <0 (Early) | #C6EFCE (Light Green) |
| 0 (On Time) | White |
| 1-7 (Late) | #FFEB9C (Light Amber) |
| >7 (Very Late) | #FFC7CE (Light Red) |

### Sheet 7: Evidence Register

**Columns:**

| Col | Field Name | Type | Width |
|-----|------------|------|-------|
| A | Evidence ID | Text | 12 |
| B | Equipment ID | Text | 15 |
| C | Maintenance Date | Date | 15 |
| D | Evidence Type | Dropdown | 20 |
| E | Document Reference | Text | 30 |
| F | Storage Location | Text | 35 |
| G | File Path/URL | Text | 50 |
| H | Retention Period | Dropdown | 15 |
| I | Expiry Date | Formula | 15 |
| J | Last Verified | Date | 15 |
| K | Verified By | Text | 20 |
| L | Status | Dropdown | 12 |
| M | Notes | Text | 30 |

**Evidence Type Dropdown:**
- Maintenance Ticket
- Vendor Service Report
- Test Report
- Inspection Certificate
- Calibration Certificate
- Firmware Confirmation
- Photograph
- Sign-off Form
- Other

**Retention Period Dropdown:**
- 1 Year
- 3 Years
- 5 Years
- 7 Years
- Contract Term +3

**Expiry Date Formula:**
```excel
=IF(H2="1 Year",C2+365,IF(H2="3 Years",C2+1095,IF(H2="5 Years",C2+1825,IF(H2="7 Years",C2+2555,""))))
```

**Status Dropdown:**
- Active
- Archived
- Expired
- Missing

---

## Cell Styling Reference

### Colour Palette

- Primary Header: #003366 (Navy blue)
- Section Header: #4472C4 (Medium blue)
- Column Header: #D9D9D9 (Light grey)
- Input Cell: #FFFFCC (Light yellow)
- Formula Cell: #E6E6E6 (Very light grey)

### Status Colours

- Current: #C6EFCE (Light green)
- Due Soon: #FFEB9C (Light amber)
- Overdue: #FFC7CE (Light red)

### Priority Colours

- Critical: #FFC7CE (Light red)
- High: #FFE4B5 (Light orange)
- Medium: #FFEB9C (Light amber)
- Low: #FFFFCC (Light yellow)

### Font Standards

- Title: Calibri 16pt Bold
- Section Header: Calibri 14pt Bold
- Column Header: Calibri 11pt Bold
- Data: Calibri 11pt Regular
- Notes: Calibri 10pt Regular

---

## Formula Reference

### Named Ranges

| Name | Range | Purpose |
|------|-------|---------|
| FrequencyTable | Lookup!A2:B8 | Frequency to days conversion |
| UpcomingThreshold | Instructions!B17 | Days for upcoming warning |
| CriticalThreshold | Instructions!B20 | Days for Tier 1 escalation |
| EquipmentList | 'Equipment Schedule'!A:A | Equipment IDs |
| StatusList | 'Equipment Schedule'!K:K | Status values |

### Key Formulas

**Next Due Date:**
```excel
=IF(I2="","",I2+VLOOKUP(G2,FrequencyTable,2,FALSE))
```

**Status Determination:**
```excel
=IF(J2="","",IF(J2>TODAY()+UpcomingThreshold,"Current",IF(J2>TODAY(),"Due Soon","Overdue")))
```

**Days Calculation:**
```excel
=IF(J2="","",J2-TODAY())
```

**Compliance Percentage:**
```excel
=IFERROR(COUNTIF(StatusList,"Current")/COUNTA(EquipmentList)*100,0)
```

---

## Validation Rules

### Data Validation Settings

**Equipment ID (Column A):**
- No duplicates allowed
- Text length: 5-20 characters

**Date Fields:**
- Format: DD.MM.YYYY (Swiss)
- Future dates allowed for scheduled/estimated
- Past dates required for completed

**Dropdown Fields:**
- Source: Named range or list
- Error alert: Show error on invalid entry

### Error Handling

**Blank Dependencies:**
- If Last Completed blank, Next Due shows blank
- If Status blank, Days Until/Overdue shows blank

**Division Errors:**
- Dashboard percentages use IFERROR to handle division by zero

---

## Integration Points

### Integration with S2 (Equipment Maintenance)

- Equipment list should align with S2 equipment inventory
- Manufacturer frequencies from S2 populate S3 schedules
- S2 assessment informs maintenance programme scope

### Integration with S4 (Dashboard)

- S4 pulls compliance metrics from S3 Dashboard
- Overall maintenance compliance score feeds S4
- Overdue counts and critical items link to S4

### Integration with CMMS/ITSM

- Export equipment from CMMS for initial population
- Reconcile completion status with maintenance tickets
- Link maintenance records to ticket references
- Sync scheduled dates with CMMS calendar

### Integration with Change Management

- Maintenance windows align with change calendar
- Change requests required for system-impacting maintenance
- Change closure triggers maintenance completion

---

## Conditional Formatting Logic

### Status Column Formatting (Column K)

**Rule Configuration:**

| Rule Order | Condition | Format Applied |
|------------|-----------|----------------|
| 1 | Cell value = "Overdue" | Background: #FFC7CE (Light red), Font: #9C0006 (Dark red) |
| 2 | Cell value = "Due Soon" | Background: #FFEB9C (Light amber), Font: #9C6500 (Dark amber) |
| 3 | Cell value = "Current" | Background: #C6EFCE (Light green), Font: #006100 (Dark green) |

**Application Range:** K2:K201 (all data rows)

### Days Until/Overdue Formatting (Column L)

**Rule Configuration:**

| Rule Order | Condition | Format Applied |
|------------|-----------|----------------|
| 1 | Cell value < -14 | Background: #FF0000 (Red), Font: White, Bold |
| 2 | Cell value < -7 | Background: #FFC7CE (Light red), Font: Dark red |
| 3 | Cell value < 0 | Background: #FFE4B5 (Light orange), Font: Black |
| 4 | Cell value <= 7 | Background: #FFEB9C (Light amber), Font: Black |
| 5 | Cell value <= 30 | Background: #FFFFCC (Light yellow), Font: Black |
| 6 | Cell value > 30 | Background: #C6EFCE (Light green), Font: Black |

**Application Range:** L2:L201

### Criticality Row Highlighting

**Rule for Tier 1 Critical Equipment:**

```
Formula: =AND($E2="Tier 1 - Critical",$K2="Overdue")
Format: Bold font, Red border around row
```

**Rule for Tier 1 Overdue Without Escalation (Sheet 3):**

```
Formula: =AND($C2="Tier 1 - Critical",$J2="No",$F2>3)
Format: Red border, Bold text, Background: #FFC7CE
```

### Overdue Tracking Conditional Formats (Sheet 3)

**Days Overdue Column (F):**

| Days | Background Colour |
|------|-------------------|
| 1-3 | #FFFFCC (Light yellow) |
| 4-7 | #FFE4B5 (Light orange) |
| 8-14 | #FFA500 (Orange) |
| 15-30 | #FFC7CE (Light red) |
| >30 | #FF0000 (Red) with white text |

### Upcoming Maintenance Time Category (Sheet 4, Column G)

| Category | Background |
|----------|------------|
| 1-Next 7 Days | #FFC7CE (Light red) |
| 2-8-14 Days | #FFE4B5 (Light orange) |
| 3-15-30 Days | #FFEB9C (Light amber) |
| 4-31-60 Days | #FFFFCC (Light yellow) |
| 5-61-90 Days | #C6EFCE (Light green) |

---

## Validation Rule Details

### Equipment ID Validation (Column A)

**Validation Settings:**

```
Type: Custom
Formula: =AND(LEN(A2)>=5,LEN(A2)<=25,COUNTIF($A$2:$A$201,A2)=1)
Error Title: Invalid Equipment ID
Error Message: Equipment ID must be 5-25 characters and unique within the workbook.
```

### Date Field Validation

**Last Completed (Column I):**

```
Type: Date
Operator: Less than or equal to
Formula: =TODAY()
Error Title: Invalid Date
Error Message: Last Completed date cannot be in the future.
```

**Next Due (Column J):**

```
Type: Date
Operator: Greater than
Formula: =I2
Error Title: Invalid Date
Error Message: Next Due date must be after Last Completed date.
```

### Dropdown Validation Sources

**Equipment Type (Column B):**

```
Source: "Server,Network Device,Storage,UPS,HVAC,Generator,Security System,Fire Suppression,Access Control,CCTV,Environmental Sensors,PDU,Cable Infrastructure,Other"
Allow blank: No
Show input message: Yes
Input message: Select the equipment category from the list.
```

**Criticality (Column E):**

```
Source: "Tier 1 - Critical,Tier 2 - Standard,Tier 3 - Low"
Allow blank: No
Show input message: Yes
Input message: Select criticality based on business impact assessment.
```

**Frequency (Column G):**

```
Source: "Weekly,Monthly,Quarterly,Semi-annually,Annually,Bi-annually"
Allow blank: No
Show input message: Yes
Input message: Select maintenance frequency per manufacturer recommendation.
```

---

## Advanced Formula Reference

### Compliance Percentage Calculations (Dashboard)

**Overall Schedule Compliance:**

```excel
=IFERROR(COUNTIF('Equipment Schedule'!K:K,"Current")/(COUNTA('Equipment Schedule'!A:A)-1)*100,0)
```

**Compliance by Equipment Type:**

```excel
=IFERROR(COUNTIFS('Equipment Schedule'!B:B,"Server",'Equipment Schedule'!K:K,"Current")/COUNTIF('Equipment Schedule'!B:B,"Server")*100,0)
```

**Compliance by Criticality:**

```excel
=IFERROR(COUNTIFS('Equipment Schedule'!E:E,"Tier 1 - Critical",'Equipment Schedule'!K:K,"Current")/COUNTIF('Equipment Schedule'!E:E,"Tier 1 - Critical")*100,0)
```

### Overdue Analysis Formulas

**Total Overdue Count:**

```excel
=COUNTIF('Equipment Schedule'!K:K,"Overdue")
```

**Critical Equipment Overdue:**

```excel
=COUNTIFS('Equipment Schedule'!E:E,"Tier 1 - Critical",'Equipment Schedule'!K:K,"Overdue")
```

**Average Days Overdue:**

```excel
=IFERROR(ABS(AVERAGEIF('Equipment Schedule'!L:L,"<0",'Equipment Schedule'!L:L)),0)
```

**Maximum Days Overdue:**

```excel
=IFERROR(ABS(MIN('Equipment Schedule'!L:L)),0)
```

### Upcoming Workload Formulas

**Next 7 Days:**

```excel
=COUNTIFS('Equipment Schedule'!L:L,">=0",'Equipment Schedule'!L:L,"<=7")
```

**8-14 Days:**

```excel
=COUNTIFS('Equipment Schedule'!L:L,">7",'Equipment Schedule'!L:L,"<=14")
```

**15-30 Days:**

```excel
=COUNTIFS('Equipment Schedule'!L:L,">14",'Equipment Schedule'!L:L,"<=30")
```

### Trend Calculation Formulas

**Month-over-Month Change:**

```excel
=B3-B2
```
Where B3 is current month compliance and B2 is previous month.

**Rolling Average (3-month):**

```excel
=AVERAGE(B2:B4)
```

**Compliance Trend Direction:**

```excel
=IF(B3>B2,"↑ Improving",IF(B3<B2,"↓ Declining","→ Stable"))
```

---

## Error Handling and Edge Cases

### Handling Blank Cells

**Next Due Date Calculation:**

```excel
=IF(OR(I2="",G2=""),"",I2+VLOOKUP(G2,FrequencyTable,2,FALSE))
```
Returns blank if either Last Completed or Frequency is empty.

**Status Determination:**

```excel
=IF(J2="","",IF(J2>TODAY()+UpcomingThreshold,"Current",IF(J2>TODAY(),"Due Soon","Overdue")))
```
Returns blank if Next Due is empty.

### Division by Zero Prevention

**Percentage Calculations:**

```excel
=IFERROR(COUNTIF(range,"Current")/COUNTA(range)*100,0)
```
Returns 0 if division would fail.

### Circular Reference Prevention

Avoid referencing cells that reference back:
- Status (K) should not reference Dashboard metrics
- Days Until (L) references only Next Due (J) and TODAY()
- Compliance percentages calculated independently of source data formulas

### Large Dataset Performance

**For workbooks exceeding 500 equipment items:**

1. Consider splitting into multiple workbooks by location/type
2. Use SUMPRODUCT instead of COUNTIFS for large ranges
3. Disable automatic calculation during bulk updates
4. Use helper columns to pre-calculate intermediate values

---

**END OF SPECIFICATION**

---

*"An ounce of prevention is worth a pound of cure."*
— Benjamin Franklin

<!-- QA_VERIFIED: 2026-02-03 -->
