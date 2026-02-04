**ISMS-IMP-A.7.1-2-3-S1: Perimeter Security Assessment**
**Assessment Specification with User Completion Guide**
### ISO/IEC 27001:2022 Control A.7.1: Physical Security Perimeters

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.7.1-2-3-S1 |
| **Version** | 1.0 |
| **Assessment Area** | Physical Security Perimeters - Zone Definition, Building Perimeter, Internal Perimeters |
| **Related Policy** | ISMS-POL-A.7.1-2-3, Section 2.1 (Physical Security Perimeters) |
| **Purpose** | Document security perimeter definitions, assess construction quality, verify monitoring coverage, and identify gaps |
| **Target Audience** | Facilities Management, Physical Security, Building Services, Compliance Officers, Auditors |
| **Assessment Type** | Technical & Operational |
| **Review Cycle** | Annual or After Major Facility Changes |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Perimeter Security assessment workbook | ISMS Implementation Team |

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

**Assessment Name:** ISMS-IMP-A.7.1-2-3-S1 - Perimeter Security Assessment

#### What This Assessment Covers

This assessment documents the physical security PERIMETERS protecting your facilities. This is the "WHAT security boundaries do we have?" assessment that answers:

- What security zones are defined? (Public, Controlled, Restricted, High-Security)
- How are building perimeters constructed? (walls, roofs, floors, windows, doors)
- What internal perimeters separate security zones?
- How are perimeters monitored? (CCTV, intrusion detection, alarms)
- Are there gaps or weaknesses in perimeter construction?
- Do perimeters extend floor-to-ceiling (including above suspended ceilings)?

#### ISO 27001:2022 Control Reference

> *"Security perimeters should be defined and used to protect areas that contain information and other associated assets."*
>
> --- ISO/IEC 27001:2022, Annex A Control 7.1

**Control Objective:** Prevent unauthorised physical access, damage, and interference to the organisation's information and assets.

#### Key Principle

This assessment is **facility-agnostic**. You document YOUR specific security zones and perimeters (whatever your building type - office, datacenter, warehouse, mixed-use), and verify construction and monitoring against policy requirements from ISMS-POL-A.7.1-2-3.

#### What You'll Document

**Security Zones:**

- Every defined security zone in your facilities
- Zone classification (Public, Controlled, Restricted, High-Security)
- Access requirements for each zone
- Perimeter definition status

**Building Perimeters:**

- External walls, roofs, and floors
- External doors and windows
- Emergency exits and loading areas
- Construction type and solid construction verification
- Gap and breach point identification

**Internal Perimeters:**

- Partitions between security zones
- Floor-to-ceiling barrier verification
- Above-ceiling and below-floor continuity
- Access control at zone transitions

**Perimeter Monitoring:**

- CCTV coverage at entry points
- Intrusion detection at perimeter
- Alert and response mechanisms
- Testing and inspection records

#### How This Relates to Other A.7.1-2-3 Assessments

| Assessment            | Focus                  | Relationship to A.7.1-2-3-S1      |
|-----------------------|------------------------|------------------------------------|
| **ISMS-IMP-A.7.1-2-3-S1** | **Perimeter Security** | **WHERE are the security boundaries?** |
| ISMS-IMP-A.7.1-2-3-S2 | Entry Control          | HOW do people enter secure areas? |
| ISMS-IMP-A.7.1-2-3-S3 | Secure Areas           | WHAT happens inside secure areas? |
| ISMS-IMP-A.7.1-2-3-S4 | Compliance Dashboard   | Overall physical access control posture |

This assessment (A.7.1-2-3-S1) establishes the foundation by defining WHERE security zones are and their perimeters. Entry Control (S2) builds on this by documenting HOW access is controlled at these perimeters.

### Who Should Complete This Assessment

#### Primary Stakeholders

1. **Facilities Manager** - Building infrastructure and perimeter ownership
2. **Physical Security Manager** - Security zone definitions and monitoring
3. **Building Services** - Construction and maintenance of perimeters
4. **Property/Estates** - Multi-site perimeter coordination
5. **Compliance Officers** - Audit requirements and evidence collection

#### Required Skills

- Understanding of building construction and security zones
- Familiarity with physical security monitoring systems
- Knowledge of facility floor plans and layouts
- Understanding of security classification levels
- Access to building plans and construction documentation

#### Time Commitment

- **Initial assessment:** 8-12 hours (comprehensive review of all facility perimeters)
- **Annual updates:** 2-4 hours (update inspections, changes, new facilities)

### Expected Outputs

Upon completion, you will have:

1. **Complete zone inventory** - Every security zone defined and classified
2. **Perimeter assessment** - Building and internal perimeter evaluation
3. **Gap identification** - Weaknesses in perimeter construction or monitoring
4. **Monitoring verification** - CCTV and intrusion detection coverage confirmed
5. **Inspection records** - Evidence of perimeter inspections
6. **Evidence register** - Supporting documentation for audit
7. **Approved assessment** - Four-level approval workflow completed

---

## Prerequisites

### Information You'll Need

Before starting this assessment, gather:

#### 1. Documentation

- Facility floor plans (all levels including basements)
- Building construction specifications
- Security zone maps/diagrams
- Perimeter inspection reports
- Building lease agreements (for shared buildings)
- Fire safety plans (showing walls, exits, zones)

#### 2. System Access

- Access to building management systems
- Access to CCTV system (for coverage verification)
- Access to intrusion detection system
- Access to access control system (for zone definitions)

#### 3. Historical Data

- Previous perimeter inspection reports
- Security incident reports involving perimeter breaches
- Maintenance records for perimeter elements
- Alarm system logs (perimeter intrusion alerts)

#### 4. Policy Requirements

- ISMS-POL-A.7.1-2-3, Section 2.1 (Physical Security Perimeters)
  - Section 2.1.1: Perimeter Definition
  - Section 2.1.2: Perimeter Construction
  - Section 2.1.3: Perimeter Monitoring

### Required Tools

- Microsoft Excel (2016 or later) for workbook completion
- Floor plan viewing software (PDF or CAD)
- Camera/phone for evidence photographs
- Measuring tape (for gap measurements if needed)
- Torch/flashlight (for ceiling void inspections)

### Dependencies

This assessment has NO dependencies on other assessments - it can be completed independently.

However, outputs from this assessment are INPUT to:

- ISMS-IMP-A.7.1-2-3-S2 (Entry Control Assessment) - Uses zone definitions
- ISMS-IMP-A.7.1-2-3-S4 (Compliance Dashboard) - Consolidates with other assessments

---

## Workflow

### High-Level Process

```
1. PREPARE
   |
2. DEFINE SECURITY ZONES (Sheet 2: Security Zones)
   |
3. ASSESS BUILDING PERIMETER (Sheet 3: Building Perimeter)
   |
4. ASSESS INTERNAL PERIMETERS (Sheet 4: Internal Perimeters)
   |
5. VERIFY MONITORING (Sheet 5: Perimeter Monitoring)
   |
6. COLLECT EVIDENCE (Sheet 7: Evidence Register)
   |
7. REVIEW SUMMARY (Sheet 6: Summary Dashboard - automated scoring)
   |
8. QUALITY CHECK (Self-assessment against checklist)
   |
9. OBTAIN APPROVALS (Sheet 8: Approval Sign-Off)
   |
10. SUBMIT FOR AUDIT
```

### Detailed Step-by-Step

**Step 1: Preparation (Day 1 - 2 hours)**

- Read this Part I User Guide completely
- Review ISMS-POL-A.7.1-2-3 perimeter requirements
- Gather all prerequisites (floor plans, documentation)
- Schedule facility walk-through with Facilities Manager
- Download or generate assessment workbook (Excel file)

**Step 2: Security Zone Definition (Day 1-2 - 2-3 hours)**

- Open assessment workbook
- Complete Sheet 1 (Instructions & Legend) - organisation info, assessment date
- Complete Sheet 2 (Security Zones) - define all zones across all facilities
- Ensure each zone has clear classification and access requirements
- Verify perimeter is defined for each zone

**Step 3: Building Perimeter Assessment (Day 2-3 - 3-4 hours)**

- Walk the building perimeter physically
- Complete Sheet 3 (Building Perimeter) - walls, roof, floor, doors, windows
- Check each perimeter element for solid construction
- Identify any gaps or breach points
- Note security controls at each entry point

**Step 4: Internal Perimeter Assessment (Day 3-4 - 2-3 hours)**

- Walk internal zone boundaries
- Complete Sheet 4 (Internal Perimeters) - partitions between zones
- Verify floor-to-ceiling construction
- Check above suspended ceilings
- Check below raised floors (if applicable)

**Step 5: Monitoring Verification (Day 4 - 2 hours)**

- Complete Sheet 5 (Perimeter Monitoring) - CCTV and intrusion detection
- Verify CCTV coverage at all entry points
- Verify intrusion detection at perimeter
- Check alert response procedures
- Review testing records

**Step 6: Evidence Collection (Day 4-5 - 2 hours)**

- Take photographs of perimeter construction
- Capture screenshots of monitoring coverage
- Collect inspection reports
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
- After Level 2, submit to Level 3: Security Manager
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

- **Status Legend** (Rows 14-17):
  - Read-only reference - understand colour coding

**Time Required:** 5 minutes

### Sheet 2: Security Zones

**Purpose:** Define and classify all security zones across all facilities

**What to Document (Per Zone):**

**Column A - Zone ID:**

- Unique identifier: "ZN-001", "ZN-002", etc.

**Column B - Zone Name:**

- Descriptive name: "Main Reception", "Server Room A", "Executive Floor"

**Column C - Zone Type:**

- Dropdown: "Public Zone", "Controlled Zone", "Restricted Zone", "High-Security Zone"
- Use classification from ISMS-POL-A.7.1-2-3

**Column D - Location/Building:**

- Where zone is located: "Building A - Ground Floor", "Datacenter 1"

**Column E - Classification:**

- Data classification: "Tier 1 - Critical", "Tier 2 - Important", "Tier 3 - Standard"

**Column F - Access Requirements:**

- What's needed to access: "Badge only", "Badge + PIN", "Biometric + escort"

**Column G - Perimeter Defined:**

- Is the perimeter clearly documented? "Yes", "Partial", "No"

**Column H - Status:**

- Dropdown: Compliant, Partial, Non-Compliant, N/A

**Column I - Notes:**

- Any additional context

**Time Required:** 30-60 minutes

### Sheet 3: Building Perimeter

**Purpose:** Assess external building perimeter construction

**What to Document (Per Perimeter Element):**

**Column A - Building/Facility:**

- Building name: "Building A - Main Campus"

**Column B - Perimeter Element:**

- Dropdown: "External Wall", "Roof", "Floor", "Window", "External Door", "Emergency Exit", "Loading Dock", "Other"

**Column C - Construction Type:**

- Description: "Brick/masonry", "Metal cladding", "Glass curtain wall", etc.

**Column D - Solid Construction:**

- Is construction solid (no easy breach)? "Yes", "No", "Partial"

**Column E - Gap/Breach Points:**

- Any identified gaps: "None", "Ventilation duct - secured", "Ceiling gap"

**Column F - Security Controls:**

- Controls at this element: "Alarmed door", "Locked window", "CCTV coverage"

**Column G - Last Inspection:**

- Date of last inspection: "15.01.2026"

**Column H - Inspector:**

- Who inspected: "John Smith - Facilities"

**Column I - Status:**

- Dropdown: Compliant, Partial, Non-Compliant, N/A

**Column J - Notes:**

- Any additional context

**Time Required:** 1-2 hours

### Sheet 4: Internal Perimeters

**Purpose:** Assess internal zone boundary construction

**What to Document (Per Boundary):**

**Column A - From Zone:**

- Zone on one side: "Controlled Zone - Office Area"

**Column B - To Zone:**

- Zone on other side: "Restricted Zone - Server Room"

**Column C - Barrier Type:**

- Dropdown: "Solid Wall", "Glass Partition", "Demountable Partition", "Security Cage", "Other"

**Column D - Floor-to-Ceiling:**

- Does barrier extend floor-to-ceiling? "Yes", "No", "N/A"

**Column E - Above Ceiling Check:**

- Has space above suspended ceiling been checked? "Yes", "No", "N/A"

**Column F - Below Floor Check:**

- Has space below raised floor been checked? "Yes", "No", "N/A"

**Column G - Access Control:**

- Access control at transition: "Badge reader", "Keypad", "Biometric", "Manual lock"

**Column H - Status:**

- Dropdown: Compliant, Partial, Non-Compliant, N/A

**Column I - Notes:**

- Any additional context

**Time Required:** 45-60 minutes

### Sheet 5: Perimeter Monitoring

**Purpose:** Verify monitoring coverage at all perimeter entry points

**What to Document (Per Entry Point):**

**Column A - Entry Point ID:**

- Unique identifier: "EP-001", "EP-002", etc.

**Column B - Location:**

- Entry point location: "Main Entrance - Building A"

**Column C - Entry Type:**

- Dropdown: "Main Entrance", "Side Door", "Emergency Exit", "Window", "Loading Dock", "Roof Access", "Vent/Service Point"

**Column D - CCTV Coverage:**

- Is entry point covered by CCTV? "Yes", "No", "Partial"

**Column E - Intrusion Detection:**

- Is entry point monitored by intrusion detection? "Yes", "No", "Partial"

**Column F - Alert Response:**

- What happens on alert: "Security patrol", "Alarm to SOC", "Local alarm only"

**Column G - Last Tested:**

- Date of last test: "15.01.2026"

**Column H - Status:**

- Dropdown: Compliant, Partial, Non-Compliant, N/A

**Column I - Notes:**

- Any additional context

**Time Required:** 45-60 minutes

### Sheet 6: Summary Dashboard

**Purpose:** Automated compliance scoring

**What to Review (Auto-Calculated - Read-Only):**

- Overall Compliance Score
- Security Zones Score
- Building Perimeter Score
- Internal Perimeters Score
- Perimeter Monitoring Score

**NO manual data entry in this sheet**

**Time Required:** 15-30 minutes for review

### Sheet 7: Evidence Register

**Purpose:** Document all supporting evidence

**Common Evidence to Collect:**

1. Floor plans showing security zones
2. Photographs of perimeter construction
3. Inspection reports from Facilities
4. CCTV coverage maps
5. Intrusion detection sensor placement diagrams
6. Test reports for alarm systems

**Time Required:** 1-2 hours

### Sheet 8: Approval Sign-Off

**Purpose:** Four-level approval workflow

**Approval Levels:**

- Level 1: Assessor (you)
- Level 2: Facilities Manager
- Level 3: Security Manager
- Level 4: CISO Approver

**Time Required:** 5 minutes for Level 1 completion

---

## Evidence Collection

### What Evidence to Collect

**1. Zone Documentation**

- Floor plans with security zones marked
- Zone classification documentation
- Access requirement definitions

**2. Perimeter Construction**

- Photographs of perimeter walls, doors, windows
- Construction specifications
- Inspection reports
- Gap identification documentation

**3. Monitoring Coverage**

- CCTV coverage maps
- Intrusion detection sensor placement
- Alarm system configuration
- Test reports

**4. Inspections**

- Annual perimeter inspection reports
- Walk-through checklists
- Remediation records for identified issues

### Evidence Storage

- **Location:** SharePoint > ISMS > Assessments > A.7.1 > Evidence
- **Retention:** 3 years minimum
- **Access:** CISO, Facilities Manager, Compliance Officer, Internal Audit

---

## Common Pitfalls

### Pitfall 1: Missing Above-Ceiling Check

**Problem:** Documenting internal perimeters as "floor-to-ceiling" without checking above suspended ceilings

**Impact:** Audit finding - perimeter bypass possible through ceiling void

**How to Avoid:**

- Physically inspect above suspended ceilings at zone boundaries
- Check if partitions extend to structural ceiling or stop at suspended ceiling
- Document findings honestly including gaps

### Pitfall 2: Ignoring Raised Floor Voids

**Problem:** Not checking below raised floors in datacenters/server rooms

**Impact:** Perimeter bypass possible through floor void

**How to Avoid:**

- Check if partitions extend below raised floors
- Verify cable penetrations are sealed
- Document raised floor security controls

### Pitfall 3: Incomplete Zone Classification

**Problem:** Only documenting obvious zones (server rooms, reception) and missing others

**Impact:** Incomplete assessment, audit finding

**How to Avoid:**

- Use floor plans systematically - every area must be in a zone
- Include less obvious areas: storage rooms, utility closets, lift lobbies
- "Controlled Zone" is the default for office areas - document all

### Pitfall 4: Not Verifying Monitoring Coverage

**Problem:** Assuming CCTV covers all entry points without verification

**Impact:** Gaps in monitoring, audit finding

**How to Avoid:**

- Review CCTV camera placement maps
- Walk the perimeter and check camera positions
- Verify intrusion detection coverage independently

### Pitfall 5: Stale Inspection Records

**Problem:** Using inspection reports from 2+ years ago

**Impact:** Evidence doesn't reflect current state

**How to Avoid:**

- Conduct fresh perimeter walk-through during assessment
- Collect new photographs with current date visible
- Reference recent (within 12 months) inspection reports

### Pitfall 6: Shared Building Complexity

**Problem:** Not properly documenting shared building arrangements

**Impact:** Unclear responsibility boundaries, incomplete assessment

**How to Avoid:**

- Clearly document which perimeters are your responsibility
- Document building management access arrangements
- Identify shared infrastructure risks

### Pitfall 7: Emergency Exit Oversight

**Problem:** Focusing on main entrances but missing emergency exits

**Impact:** Security gap, audit finding

**How to Avoid:**

- Include ALL emergency exits in building perimeter assessment
- Verify alarmed status
- Check for propped-open or wedged doors

### Pitfall 8: Ventilation and Service Points

**Problem:** Missing ventilation ducts, cable routes, service access points

**Impact:** Perimeter bypass routes not secured

**How to Avoid:**

- Review building services drawings
- Include air handling units, cable risers, service tunnels
- Verify security controls on service access points

### Pitfall 9: Copy-Paste Zone Definitions

**Problem:** Using generic zone definitions that don't match your facility

**Impact:** Assessment doesn't reflect reality, unhelpful for security

**How to Avoid:**

- Define zones based on YOUR facility layout
- Walk the facility during definition, not just use floor plans
- Ensure access requirements match actual practice

### Pitfall 10: Incomplete Evidence Register

**Problem:** Documenting assessment but not collecting supporting evidence

**Impact:** Audit finding - assessment unsupported

**How to Avoid:**

- Collect evidence AS you complete each sheet
- Take photographs during walk-through
- Reference all evidence in Evidence Register

---

## Quality Checklist

Before submitting for Level 2 approval, complete this self-assessment:

### Sheet 1: Instructions & Legend

- [ ] Assessment Date completed
- [ ] Completed By (your name and role)
- [ ] Organisation name filled in

### Sheet 2: Security Zones

- [ ] ALL security zones documented (not just critical areas)
- [ ] Zone types correctly classified
- [ ] Perimeter defined status accurate
- [ ] At least one zone per facility documented

### Sheet 3: Building Perimeter

- [ ] ALL perimeter elements documented (walls, roof, floor, doors, windows)
- [ ] Solid construction verified (not assumed)
- [ ] Gap/breach points honestly documented
- [ ] Recent inspection date (within 12 months)

### Sheet 4: Internal Perimeters

- [ ] ALL zone boundaries documented
- [ ] Floor-to-ceiling status verified (not assumed)
- [ ] Above-ceiling checks completed
- [ ] Below-floor checks completed (where applicable)

### Sheet 5: Perimeter Monitoring

- [ ] ALL entry points documented
- [ ] CCTV coverage verified (walked the perimeter)
- [ ] Intrusion detection coverage verified
- [ ] Testing dates within policy requirements

### Sheet 6: Summary Dashboard

- [ ] Dashboard displays scores (not blank, not error)
- [ ] Scores appear reasonable

### Sheet 7: Evidence Register

- [ ] At least 5 evidence items documented
- [ ] Floor plans collected
- [ ] Photographs collected
- [ ] Inspection reports referenced

### Sheet 8: Approval Sign-Off

- [ ] Level 1 (Assessor) completed

### Final Checks

- [ ] Facility walk-through completed (not desk-based only)
- [ ] All yellow input cells completed or marked N/A
- [ ] No formula errors (#REF, #VALUE, etc.)
- [ ] Consistent naming across sheets

---

## Review & Approval

### Four-Level Approval Workflow

**Level 1: Assessor (You)**
- Complete assessment and quality check
- Date and sign Level 1

**Level 2: Facilities Manager**
- Review perimeter construction accuracy
- Verify inspection records
- Date and sign Level 2

**Level 3: Security Manager**
- Review zone definitions
- Verify monitoring coverage
- Date and sign Level 3

**Level 4: CISO Approver**
- Executive review and approval
- Date and sign Level 4

**Timeline:** 5-10 business days for all four levels

---

# PART II: TECHNICAL SPECIFICATION

## Excel Workbook Structure

### Workbook Overview

**File Name:** ISMS-IMP-A.7.1.1_Perimeter_Security_YYYYMMDD.xlsx

**Generation:** Automated via Python script (generate_a71_1_perimeter_security.py)

**Sheet Count:** 8 worksheets

**Data Capacity:** 100 data rows per assessment sheet (Sheets 2-5)

**Styling:** Navy blue headers, yellow input cells, conditional formatting for compliance status (green/amber/red)

### Sheet Organisation

| Sheet # | Sheet Name | Purpose | Type | Row Count |
|---------|------------|---------|------|-----------|
| 1 | Instructions & Legend | Assessment metadata and status legend | Read-only Reference | ~30 rows |
| 2 | Security Zones | Security zone inventory and classification | Data Entry | 100 data rows |
| 3 | Building Perimeter | External perimeter construction assessment | Data Entry | 100 data rows |
| 4 | Internal Perimeters | Internal zone boundary assessment | Data Entry | 100 data rows |
| 5 | Perimeter Monitoring | CCTV and intrusion detection coverage | Data Entry | 100 data rows |
| 6 | Summary Dashboard | Automated compliance scoring | Formula-driven | ~20 rows |
| 7 | Evidence Register | Supporting evidence documentation | Data Entry | 100 data rows |
| 8 | Approval Sign-Off | Four-level approval workflow | Data Entry | ~20 rows |

### Workbook Features

**Data Validation:**

- Dropdown lists for standardised input (Zone Types, Perimeter Elements, Status)
- Date validation (valid date format)

**Conditional Formatting:**

- Compliance Status columns: Green (Compliant), Amber (Partial), Red (Non-Compliant)
- Summary Dashboard scores: Colour-coded thresholds

**Formulas:**

- Summary Dashboard auto-calculates from Sheets 2-5
- Compliance Status derived from entry data

**Freeze Panes:**

- Header rows frozen
- First column frozen for horizontal scrolling

---

## Sheet-by-Sheet Specifications

### Sheet 2: Security Zones

**Columns:**

| Col | Field Name | Type | Width | Validation |
|-----|------------|------|-------|------------|
| A | Zone ID | Text | 12 | None |
| B | Zone Name | Text | 25 | None |
| C | Zone Type | Dropdown | 18 | Public/Controlled/Restricted/High-Security |
| D | Location/Building | Text | 25 | None |
| E | Classification | Dropdown | 18 | Tier 1/Tier 2/Tier 3 |
| F | Access Requirements | Text | 30 | None |
| G | Perimeter Defined | Dropdown | 15 | Yes/Partial/No |
| H | Status | Dropdown | 18 | Compliant/Partial/Non-Compliant/N/A |
| I | Notes | Text | 35 | None |

### Sheet 3: Building Perimeter

**Columns:**

| Col | Field Name | Type | Width | Validation |
|-----|------------|------|-------|------------|
| A | Building/Facility | Text | 25 | None |
| B | Perimeter Element | Dropdown | 20 | Wall/Roof/Floor/Window/Door/Exit/Dock/Other |
| C | Construction Type | Text | 20 | None |
| D | Solid Construction | Dropdown | 15 | Yes/No/Partial |
| E | Gap/Breach Points | Text | 20 | None |
| F | Security Controls | Text | 25 | None |
| G | Last Inspection | Date | 15 | Date format |
| H | Inspector | Text | 18 | None |
| I | Status | Dropdown | 18 | Compliant/Partial/Non-Compliant/N/A |
| J | Notes | Text | 35 | None |

### Sheet 4: Internal Perimeters

**Columns:**

| Col | Field Name | Type | Width | Validation |
|-----|------------|------|-------|------------|
| A | From Zone | Text | 20 | None |
| B | To Zone | Text | 20 | None |
| C | Barrier Type | Dropdown | 20 | Wall/Glass/Partition/Cage/Other |
| D | Floor-to-Ceiling | Dropdown | 15 | Yes/No/N/A |
| E | Above Ceiling Check | Dropdown | 18 | Yes/No/N/A |
| F | Below Floor Check | Dropdown | 18 | Yes/No/N/A |
| G | Access Control | Text | 20 | None |
| H | Status | Dropdown | 18 | Compliant/Partial/Non-Compliant/N/A |
| I | Notes | Text | 35 | None |

### Sheet 5: Perimeter Monitoring

**Columns:**

| Col | Field Name | Type | Width | Validation |
|-----|------------|------|-------|------------|
| A | Entry Point ID | Text | 15 | None |
| B | Location | Text | 25 | None |
| C | Entry Type | Dropdown | 20 | Entrance/Door/Exit/Window/Dock/Roof/Vent |
| D | CCTV Coverage | Dropdown | 15 | Yes/No/Partial |
| E | Intrusion Detection | Dropdown | 18 | Yes/No/Partial |
| F | Alert Response | Text | 20 | None |
| G | Last Tested | Date | 15 | Date format |
| H | Status | Dropdown | 18 | Compliant/Partial/Non-Compliant/N/A |
| I | Notes | Text | 35 | None |

---

## Cell Styling Reference

### Colour Palette

**Headers:**

- Primary Header: #003366 (Navy blue), White text
- Column Header: #D9D9D9 (Light grey), Black text

**Data Cells:**

- Input Cell: #FFFFCC (Light yellow)
- Read-Only: White

**Compliance Status:**

- Compliant: #C6EFCE (Light green)
- Partial: #FFEB9C (Light amber)
- Non-Compliant: #FFC7CE (Light red)

---

## Integration Points

### Integration with Policy (ISMS-POL-A.7.1-2-3)

| Policy Section | Assessment Sheet | Focus |
|----------------|------------------|-------|
| 2.1.1 Perimeter Definition | Sheet 2: Security Zones | Zone classification and definition |
| 2.1.2 Perimeter Construction | Sheet 3: Building Perimeter | External perimeter assessment |
| 2.1.2 Internal Perimeters | Sheet 4: Internal Perimeters | Zone boundary construction |
| 2.1.3 Perimeter Monitoring | Sheet 5: Perimeter Monitoring | CCTV and intrusion detection |

### Integration with Other Assessments

**Feeds into:**

- ISMS-IMP-A.7.1-2-3-S4 (Compliance Dashboard) - Perimeter compliance score

**Dependencies from:**

- None - this is the foundational assessment

---

**END OF SPECIFICATION**

---

*"The strength of a chain is determined by its weakest link; the security of a perimeter, by its least protected point."*
--- Bruce Schneier

<!-- QA_VERIFIED: 2026-02-03 -->
