**ISMS-IMP-A.7.12-13.S1: Cabling Security Assessment**
**Assessment Specification with User Completion Guide**
### ISO/IEC 27001:2022 Control A.7.12: Cabling Security

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.7.12-13.S1 |
| **Version** | 1.0 |
| **Assessment Area** | Cabling Security - Power and Data Cable Protection, Segregation, Documentation |
| **Related Policy** | ISMS-POL-A.7.12-13, Section 2.1 (Cabling Security) |
| **Purpose** | Document cabling infrastructure, assess protection measures against policy requirements, and identify gaps |
| **Target Audience** | Facilities Management, Network Engineers, IT Operations, Data Centre Managers, Compliance Officers, Auditors |
| **Assessment Type** | Technical & Operational |
| **Review Cycle** | Annual or After Major Infrastructure Changes |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Cabling Security assessment workbook | ISMS Implementation Team |

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

**Assessment Name:** ISMS-IMP-A.7.12-13.S1 - Cabling Security Assessment

#### What This Assessment Covers

This assessment documents the cabling SECURITY measures deployed in your facilities. This is the "HOW are our cables protected?" assessment that answers:

- What cable pathways are deployed? (conduits, cable trays, raised floors, underground routes)
- What physical protection measures are in place? (armouring, electromagnetic shielding, cable segregation)
- What access controls protect cabling infrastructure? (locked cabinets, wiring closets, manholes)
- How is cabling documented? (cable schedules, labelling, network diagrams)
- What change control processes govern cabling? (approval workflows, documentation updates)
- What audits and inspections are performed? (annual reviews, visual inspections, authorised additions)


#### Key Principle

This assessment is **completely vendor-agnostic and technology-independent**. You document YOUR specific cabling infrastructure (whatever you have - copper, fibre optic, power cables, network cables), and verify protection measures against generic policy requirements from ISMS-POL-A.7.12-13, Section 2.1.

#### What You'll Document

**Cable Pathways:**

- Every cable pathway type (conduits, trays, raised floors, underground)
- Location and coverage area
- Cable types routed through each pathway
- Protection level (enclosed, open, armoured)


**Physical Protection:**

- Electromagnetic interference (EMI) shielding measures
- Physical protection against damage (armoured conduits, concrete encasement)
- Environmental protection (water, heat, physical impact)
- Cable route security (avoiding high-risk areas)


**Access Controls:**

- Wiring closet security (locks, access cards, monitoring)
- Patch panel and distribution frame access
- Manhole and duct access controls
- Cable infrastructure access logging


**Cable Documentation:**

- Cable schedules and inventories
- Network topology diagrams
- Labelling standards and compliance
- Documentation currency (last update date)


**Change Control:**

- Cable change approval process
- Documentation update procedures
- Unused cable management
- Audit trail of changes


**Audits and Inspections:**

- Annual cabling infrastructure audits
- Visual inspection schedules
- Unauthorised addition detection
- Remediation tracking


#### How This Relates to Other A.7.12-13 Assessments

| Assessment            | Focus                  | Relationship to A.7.12-13.S1      |
|-----------------------|------------------------|------------------------------------|
| **ISMS-IMP-A.7.12-13.S1** | **Cabling Security** | **Cable protection and documentation** |
| ISMS-IMP-A.7.12-13.S2 | Equipment Maintenance | Equipment servicing and maintenance records |
| ISMS-IMP-A.7.12-13.S3 | Maintenance Schedule | Preventive maintenance planning and tracking |
| ISMS-IMP-A.7.12-13.S4 | Compliance Dashboard | Consolidated view across cabling and maintenance |

This assessment (A.7.12-13.S1) focuses specifically on Control A.7.12 (Cabling Security). It complements assessments for A.7.13 (Equipment Maintenance).

### Who Should Complete This Assessment

#### Primary Stakeholders

1. **Facilities Manager** - Overall cabling infrastructure ownership
2. **Network Engineers** - Data cabling expertise and documentation
3. **Data Centre Manager** - Critical infrastructure cabling
4. **IT Operations** - Day-to-day cable management
5. **Compliance Officers** - Audit requirements and evidence collection

#### Required Skills

- Understanding of structured cabling systems (TIA/EIA standards)
- Familiarity with cable protection methods (conduits, trays, shielding)
- Knowledge of power and data cable segregation requirements
- Understanding of facility security zones
- Access to cable documentation and network diagrams


#### Time Commitment

- **Initial assessment:** 8-12 hours (comprehensive review of all cabling infrastructure)
- **Annual updates:** 2-4 hours (update based on infrastructure changes, audit findings)


### Expected Outputs

Upon completion, you will have:

1. ✅ **Complete pathway inventory** - Every cable pathway documented with protection status
2. ✅ **Protection assessment** - Physical, electromagnetic, and environmental protection verified
3. ✅ **Access control verification** - Wiring closet and infrastructure access controls documented
4. ✅ **Documentation audit** - Cable schedules, diagrams, and labelling compliance verified
5. ✅ **Change control review** - Cable change processes assessed
6. ✅ **Gap analysis** - Identified gaps between deployed measures and policy requirements
7. ✅ **Evidence register** - Supporting documentation for audit
8. ✅ **Approved assessment** - Four-level approval workflow completed

---

## Prerequisites

### Information You'll Need

Before starting this assessment, gather:

#### 1. System Access

- Access to cable documentation systems (cable management databases, spreadsheets)
- Access to network documentation (topology diagrams, rack elevations)
- Access to wiring closets and distribution rooms
- Access to data centre cable infrastructure
- Access to facilities documentation (floor plans, cable routing)


#### 2. Documentation

- Current cable schedules (power and data)
- Network topology diagrams (logical and physical)
- Facility floor plans with cable routes marked
- Wiring closet and patch panel documentation
- Cable labelling standards and procedures
- Change control procedures for cabling


#### 3. Historical Data

- Previous cabling audit reports
- Change requests for cabling modifications (last 12 months)
- Incident reports related to cable damage or failure
- Access logs for wiring closets (if available)
- Maintenance records for cabling infrastructure


#### 4. Policy Requirements

- ISMS-POL-A.7.12-13, Section 2.1 (Cabling Security Requirements)
  - Section 2.1.1: Cable Protection
  - Section 2.1.2: Access Control
  - Section 2.1.3: Segregation Requirements
  - Section 2.1.4: Cable Documentation and Management
  - Section 2.1.5: Inspection and Maintenance


### Required Tools

- Microsoft Excel (2016 or later) for workbook completion
- Access to cable documentation systems
- Facility access for physical inspection
- Measuring tape or laser distance meter (for pathway measurements if needed)
- Torch/flashlight (for inspecting cable routes)
- Camera (for evidence photos)


### Dependencies

This assessment has NO dependencies on other assessments - it can be completed independently.

However, outputs from this assessment are INPUT to:

- ISMS-IMP-A.7.12-13.S4 (Compliance Dashboard) - Consolidates cabling security with equipment maintenance
- Network security assessments (physical network infrastructure verification)


---

## Workflow

### High-Level Process

```
1. PREPARE
   ↓
2. INVENTORY PATHWAYS (Sheet 2: Cable Pathways)
   ↓
3. ASSESS PROTECTION (Sheet 3: Physical Protection)
   ↓
4. VERIFY ACCESS CONTROLS (Sheet 4: Access Controls)
   ↓
5. AUDIT DOCUMENTATION (Sheet 5: Documentation)
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
- Review ISMS-POL-A.7.12-13, Section 2.1 requirements
- Gather all prerequisites (documentation, access, historical data)
- Schedule time with Facilities Manager and Network Engineers
- Download or generate assessment workbook (Excel file)


**Step 2: Pathway Inventory (Day 1-2 - 3-4 hours)**

- Open assessment workbook
- Complete Sheet 1 (Instructions & Legend) - organisation info, assessment date
- Complete Sheet 2 (Cable Pathways) - inventory all pathways by type and location
- Document cable types routed through each pathway
- Note protection level for each pathway


**Step 3: Protection Assessment (Day 2-3 - 2-3 hours)**

- Complete Sheet 3 (Physical Protection)
- Verify EMI shielding measures
- Check physical protection against damage
- Verify environmental protection
- Identify any high-risk routing areas


**Step 4: Access Control Verification (Day 3 - 2-3 hours)**

- Complete Sheet 4 (Access Controls)
- Verify wiring closet security
- Check patch panel and distribution frame access
- Verify manhole and duct access controls
- Review access logging mechanisms


**Step 5: Documentation Audit (Day 4 - 2-3 hours)**

- Complete Sheet 5 (Documentation)
- Review cable schedules for accuracy and currency
- Verify network diagrams are current
- Check labelling compliance against standards
- Verify change control process compliance


**Step 6: Evidence Collection (Day 4-5 - 2-3 hours)**

- Take photographs of cable pathways and protection measures
- Take screenshots of cable documentation systems
- Collect sample cable schedules and diagrams
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
  - Organisation: [Organisation] name
  - Leave other fields as-is (Document ID, Version, etc.)

- **Status Legend** (Rows 14-17):
  - Read-only reference - understand colour coding:
    - Green (✅ Compliant): Meets all policy requirements
    - Amber (⚠️ Partial): Meets some requirements, gaps identified
    - Red (❌ Non-Compliant): Does not meet requirements, immediate action needed


**Time Required:** 5 minutes

### Sheet 2: Cable Pathways

**Purpose:** Document all cable pathways and their protection status

**Structure:** 100 data rows for documenting multiple pathway segments

**What to Document (Per Pathway Segment):**

**Column A - Pathway ID:**

- Unique identifier: "CP-001", "CP-002", etc.


**Column B - Facility/Building:**

- Location: "Building A - Main Campus", "Datacenter 1", "Branch Office"


**Column C - Pathway Type:**

- Dropdown: "Conduit", "Cable Tray", "Raised Floor", "Underground", "Ceiling Void", "Wall Chase"


**Column D - Start Location:**

- Where pathway begins: "MDF Room A", "Server Room", "Building Entry Point"


**Column E - End Location:**

- Where pathway terminates: "IDF Room 2", "Workstation Area", "External Comms Room"


**Column F - Cable Types:**

- Cables routed through pathway: "Fibre + Cat6", "Power only", "Data only", "Mixed power/data"


**Column G - Protection Type:**

- Dropdown: "Enclosed - Metal", "Enclosed - Plastic", "Open Tray", "Armoured", "None"


**Column H - Length (metres):**

- Approximate length of pathway segment: 10, 50, 200, etc.


**Column I - Segregation Compliant:**

- Dropdown: "Yes", "No", "N/A"
- Note: Power and data cables should be segregated


**Column J - Documentation Current:**

- Dropdown: "Yes", "Partial", "No"
- Is this pathway documented in cable schedules?


**Column K - Last Inspection:**

- Date of last visual inspection: "15.01.2026"


**Column L - Compliance Status:**

- Formula auto-calculates based on requirements:
  - Green (✅): Protected pathway, segregation compliant, documentation current
  - Amber (⚠️): Minor gaps (e.g., documentation slightly outdated)
  - Red (❌): Major gaps (no protection, segregation non-compliant)


**Column M - Notes:**

- Any additional context: "Upgrade planned Q2 2026", "Legacy installation"


**Time Required:** 45-60 minutes for comprehensive pathway inventory

### Sheet 3: Physical Protection

**Purpose:** Assess physical and environmental protection measures for cabling

**Structure:** 100 data rows for documenting protection assessments

**What to Document (Per Facility Area):**

**Column A - Area ID:**

- Unique identifier: "PA-001", "PA-002", etc.


**Column B - Facility/Building:**

- Location: "Building A", "Datacenter 1"


**Column C - Area Name:**

- Specific area: "Server Room", "IDF Closet Floor 2", "Underground Entry"


**Column D - EMI Protection:**

- Dropdown: "Yes - Shielded", "Partial", "No", "N/A"


**Column E - Physical Damage Protection:**

- Dropdown: "Yes - Armoured", "Yes - Enclosed", "Partial", "No"


**Column F - Water Protection:**

- Dropdown: "Yes", "Partial", "No", "N/A"


**Column G - Heat Protection:**

- Dropdown: "Yes", "Partial", "No", "N/A"


**Column H - Cable Route Risk Level:**

- Dropdown: "Low", "Medium", "High"
- High = near water sources, heat sources, public areas


**Column I - Fibre Used for High Security:**

- Dropdown: "Yes", "No", "N/A"
- Note: Fibre optic should be used where interception risk exists


**Column J - Compliance Status:**

- Formula auto-calculates based on requirements


**Column K - Notes:**

- Any additional context, remediation plans


**Time Required:** 30-45 minutes for protection assessment

### Sheet 4: Access Controls

**Purpose:** Document access controls for cabling infrastructure

**Structure:** 100 data rows for documenting access-controlled areas

**What to Document (Per Access Point):**

**Column A - Location ID:**

- Unique identifier: "AC-001", "AC-002", etc.


**Column B - Facility/Building:**

- Location: "Building A", "Datacenter 1"


**Column C - Infrastructure Type:**

- Dropdown: "Wiring Closet", "Patch Panel", "Distribution Frame", "Manhole", "Duct Access"


**Column D - Location Description:**

- Specific location: "Floor 2 IDF", "Basement MDF", "External manhole #3"


**Column E - Lock Type:**

- Dropdown: "Electronic Access Card", "Keyed Lock", "Combination Lock", "No Lock", "Cage/Enclosure"


**Column F - Access Restricted:**

- Dropdown: "Yes - IT Only", "Yes - Facilities Only", "Yes - Authorised Personnel", "No"


**Column G - Access Logged:**

- Dropdown: "Yes - Electronic", "Yes - Manual", "No"


**Column H - Occupied Monitoring:**

- Dropdown: "Yes - CCTV", "Yes - Guards", "No"
- Note: Unoccupied spaces should be secured


**Column I - Last Access Review:**

- Date of last review of who has access: "15.01.2026"


**Column J - Compliance Status:**

- Formula auto-calculates based on requirements


**Column K - Notes:**

- Any additional context


**Time Required:** 30-45 minutes for access control documentation

### Sheet 5: Documentation

**Purpose:** Audit cable documentation compliance

**Structure:** Documentation compliance checklist

**What to Document:**

**Column A - Document Type:**

- Cable schedule, Network diagram, Labelling standard, Change log, etc.


**Column B - Document Name:**

- Specific document name: "Network Topology v2.3", "Cable Schedule Building A"


**Column C - Document Location:**

- Where stored: "SharePoint/IT/Network", "CMDB", "Facilities shared drive"


**Column D - Owner:**

- Person responsible: "Network Manager", "Facilities Manager"


**Column E - Last Updated:**

- Date of last update: "15.01.2026"


**Column F - Review Cycle:**

- Expected review frequency: "Annual", "Quarterly", "On change"


**Column G - Current:**

- Dropdown: "Yes", "No"
- Is document current (updated within review cycle)?


**Column H - Accessible:**

- Dropdown: "Yes - Online", "Yes - Restricted", "No"


**Column I - Compliance Status:**

- Formula auto-calculates


**Column J - Notes:**

- Any additional context


**Labelling Compliance Section:**

- Cables labelled at both ends: Yes/No
- Labels legible: Yes/No
- Labels match documentation: Yes/No
- Patch panels labelled: Yes/No


**Time Required:** 20-30 minutes for documentation audit

### Sheet 6: Summary Dashboard

**Purpose:** Automated compliance scoring and overall cabling security health

**Structure:** Dashboard with formulas auto-calculating from Sheets 2-5

**What to Review (Auto-Calculated - Read-Only):**

**Overall Compliance Score:**

- Formula aggregates compliance from all sheets
- Displayed as percentage: 92%, 78%, etc.
- Thresholds: >90% (Green), 75-89% (Amber), <75% (Red)


**Domain Scores:**

- Cable Pathways Compliance Score (%)
- Physical Protection Score (%)
- Access Controls Score (%)
- Documentation Score (%)


**Gap Summary:**

- Auto-generated list of non-compliant items
- Prioritised by severity


**What YOU Do:**

- Review dashboard after completing Sheets 2-5
- Verify auto-calculations appear correct
- Investigate any unexpected red/amber status
- Prepare remediation plan for gaps identified
- NO manual data entry in this sheet


**Time Required:** 15-30 minutes for review and interpretation

### Sheet 7: Evidence Register

**Purpose:** Document all supporting evidence for audit traceability

**Structure:** Evidence log with links to actual evidence files

**What to Document (Per Evidence Item):**

- Evidence ID (EVID-001, etc.)
- Evidence Type (Screenshot, Photo, Document, Export)
- Description
- Related Sheet/Item
- File Name
- File Location
- Collection Date
- Collected By
- Retention Period


**Common Evidence to Collect:**

1. **Cable Pathways:**
   - Photos of cable trays, conduits, raised floor
   - Cable route diagrams

2. **Physical Protection:**
   - Photos of shielding, armoured conduits
   - EMI test reports if available

3. **Access Controls:**
   - Photos of locked wiring closets
   - Access control system configuration screenshots
   - Access logs samples

4. **Documentation:**
   - Cable schedules (sample pages)
   - Network diagrams (current version)
   - Labelling photos


**Time Required:** 2-3 hours for comprehensive evidence collection

### Sheet 8: Approval Sign-Off

**Purpose:** Four-level approval workflow documentation

**Approval Levels:**

- Level 1: Assessor (You)
- Level 2: Facilities Manager
- Level 3: CISO
- Level 4: Compliance Officer


**Time Required:** 5 minutes for Level 1, then asynchronous for Levels 2-4

---

## Evidence Collection

### What Evidence to Collect

**Evidence Categories:**

**1. Cable Pathway Evidence**

- Photos of cable trays and conduits
- Photos of raised floor cable management
- Photos of underground cable entry points
- Cable route diagrams


**2. Protection Measure Evidence**

- Photos of armoured conduits
- Photos of EMI shielding (if visible)
- Photos of cable segregation (power vs. data)
- Environmental protection measures


**3. Access Control Evidence**

- Photos of locked wiring closets
- Access control system configuration
- Access logs (sample export)
- CCTV coverage of infrastructure areas


**4. Documentation Evidence**

- Current cable schedule (sample pages or full document)
- Network topology diagram (current version)
- Labelling standard document
- Change control procedure document
- Sample change requests


**5. Audit/Inspection Evidence**

- Previous audit reports
- Inspection checklists
- Remediation tracking records


### Evidence Storage

**Storage Location:**

- Secure network share or SharePoint
- Organised by sheet: Evidence/Sheet2_Pathways/, Evidence/Sheet3_Protection/, etc.

**Retention:**

- Minimum: 3 years
- Encrypt sensitive evidence


---

## Common Pitfalls

### Pitfall 1: Incomplete Pathway Inventory

❌ **MISTAKE:** Only documenting main cable routes, missing secondary pathways or branch circuits

**How to Avoid:**
- Walk through entire facility with network diagrams
- Include ALL pathway types: conduits, trays, underground, ceiling voids
- Don't forget inter-building connections


### Pitfall 2: Assuming Segregation Compliance

❌ **MISTAKE:** Assuming power and data are segregated without physical verification

**How to Avoid:**
- Physically inspect cable routes
- Check for mixed cables in same conduit/tray
- Verify minimum separation distances per local electrical codes


### Pitfall 3: Outdated Documentation

❌ **MISTAKE:** Referencing cable schedules that haven't been updated after changes

**How to Avoid:**
- Check document last updated date
- Cross-reference documentation with physical reality
- Sample-check 10% of documented cables against physical labels


### Pitfall 4: Missing Underground/External Routes

❌ **MISTAKE:** Only assessing internal cabling, ignoring external and underground routes

**How to Avoid:**
- Include all building entry points
- Document underground ducts and manholes
- Assess inter-building connections


### Pitfall 5: Access Control Gaps

❌ **MISTAKE:** Documenting that wiring closets are "locked" without verifying who has access

**How to Avoid:**
- Review access list for each wiring closet
- Verify access is appropriate (IT/Facilities only)
- Check if access review has been conducted recently


### Pitfall 6: Labelling Non-Compliance

❌ **MISTAKE:** Assuming cables are labelled because the standard exists

**How to Avoid:**
- Physically verify labelling at sample locations
- Check both ends of cables are labelled
- Verify labels match documentation


### Pitfall 7: Change Control Bypass

❌ **MISTAKE:** Not checking for unauthorised cable additions

**How to Avoid:**
- Compare physical cables to documentation
- Look for cables without labels (potential unauthorised additions)
- Review change log for completeness


### Pitfall 8: Stale Evidence

❌ **MISTAKE:** Using photos or documents from previous assessments

**How to Avoid:**
- Collect evidence during current assessment
- Date-stamp all photos
- Verify documents are current versions


### Pitfall 9: Ignoring Fibre for High-Security

❌ **MISTAKE:** Not verifying fibre optic use for high-security network segments

**How to Avoid:**
- Identify high-security network zones
- Verify fibre optic cables used for sensitive traffic
- Document where copper is used and justify


### Pitfall 10: Incomplete Risk Assessment

❌ **MISTAKE:** Not identifying high-risk cable routes (near water, heat, public areas)

**How to Avoid:**
- Map cable routes against facility risks
- Identify routes near water pipes, HVAC, kitchens
- Document mitigation measures for high-risk routes


---

## Quality Checklist

Before submitting for Level 2 approval, complete this self-assessment:

### Sheet 1: Instructions & Legend

- [ ] Assessment Date completed
- [ ] Completed By (your name and role)
- [ ] Organisation name filled in

### Sheet 2: Cable Pathways

- [ ] ALL pathway segments documented (not just main routes)
- [ ] Pathway types correctly identified
- [ ] Cable types documented for each pathway
- [ ] Protection type verified (not assumed)
- [ ] Segregation compliance physically verified
- [ ] Documentation currency checked
- [ ] Last inspection dates recorded
- [ ] Compliance status formulas working

### Sheet 3: Physical Protection

- [ ] ALL facility areas with cabling assessed
- [ ] EMI protection verified where applicable
- [ ] Physical damage protection assessed
- [ ] Water and heat protection assessed
- [ ] Cable route risk levels identified
- [ ] Fibre usage for high-security verified

### Sheet 4: Access Controls

- [ ] ALL wiring closets/infrastructure access points documented
- [ ] Lock types verified (not assumed)
- [ ] Access restriction levels documented
- [ ] Access logging verified
- [ ] Last access review dates recorded

### Sheet 5: Documentation

- [ ] ALL cable documentation types listed
- [ ] Document currency verified
- [ ] Labelling compliance physically checked
- [ ] Change control process documented

### Sheet 6: Summary Dashboard

- [ ] Compliance scores display correctly
- [ ] Gap summary auto-populates
- [ ] Scores reviewed and verified reasonable

### Sheet 7: Evidence Register

- [ ] At least 10 evidence items documented
- [ ] Evidence files actually exist at documented locations
- [ ] Collection dates are during assessment period

### Sheet 8: Approval Sign-Off

- [ ] Level 1 (Assessor) completed

### Overall Quality

- [ ] No blank required fields
- [ ] No formula errors
- [ ] Consistent facility naming across sheets
- [ ] British spelling used throughout


---

## Review & Approval

### Four-Level Approval Workflow

**Level 1: Assessor (You)**
- Complete assessment and evidence collection
- Self-review using Quality Checklist

**Level 2: Facilities Manager**
- Technical review of cabling infrastructure assessment
- Verify accuracy against known infrastructure

**Level 3: CISO**
- Executive review and gap prioritisation
- Resource allocation for remediation

**Level 4: Compliance Officer**
- Final audit readiness certification
- Verify evidence completeness


---

# PART II: TECHNICAL SPECIFICATION

## Excel Workbook Structure

### Workbook Overview

**File Name:** ISMS-IMP-A.7.12-13.S1_Cabling_Security_YYYYMMDD.xlsx

**Generation:** Automated via Python script (generate_a712_1_cabling_security.py)

**Sheet Count:** 8 worksheets

**Data Capacity:** 100 data rows per assessment sheet

**Styling:** Navy blue headers, yellow input cells, conditional formatting for compliance status

### Sheet Organisation

| Sheet # | Sheet Name | Purpose | Type | Row Count |
|---------|------------|---------|------|-----------|
| 1 | Instructions & Legend | Assessment metadata and status legend | Read-only Reference | ~30 rows |
| 2 | Cable Pathways | Cable pathway inventory and compliance | Data Entry | 100 data rows |
| 3 | Physical Protection | Physical and environmental protection | Data Entry | 100 data rows |
| 4 | Access Controls | Infrastructure access control assessment | Data Entry | 100 data rows |
| 5 | Documentation | Cable documentation compliance | Data Entry | 50 data rows |
| 6 | Summary Dashboard | Automated compliance scoring | Formula-driven | ~40 rows |
| 7 | Evidence Register | Supporting evidence documentation | Data Entry | 100 data rows |
| 8 | Approval Sign-Off | Four-level approval workflow | Data Entry | ~20 rows |

---

## Sheet-by-Sheet Specifications

### Sheet 1: Instructions & Legend

**Purpose:** Assessment metadata and status legend

**Structure:**

**Row 1:** Header
- Merged cells A1:G1
- Text: "ISMS-IMP-A.7.12-13.S1 - Cabling Security Assessment\nISO/IEC 27001:2022 - Control A.7.12: Cabling Security"
- Style: Navy blue background (#003366), white bold text, 14pt

**Rows 3-11:** Document Information Table
- Labels in Column A, Values in Column B
- User input fields (yellow): Assessment Date, Completed By, Organisation

**Rows 13-17:** Status Legend
- Colour-coded status definitions

### Sheet 2: Cable Pathways

**Purpose:** Document all cable pathways and assess protection status

**Columns:**

| Col | Field Name | Type | Width | Validation |
|-----|------------|------|-------|------------|
| A | Pathway ID | Text | 12 | None |
| B | Facility/Building | Text | 25 | None |
| C | Pathway Type | Dropdown | 18 | List: Conduit, Cable Tray, Raised Floor, Underground, Ceiling Void, Wall Chase |
| D | Start Location | Text | 25 | None |
| E | End Location | Text | 25 | None |
| F | Cable Types | Text | 20 | None |
| G | Protection Type | Dropdown | 18 | List: Enclosed - Metal, Enclosed - Plastic, Open Tray, Armoured, None |
| H | Length (metres) | Number | 12 | Integer >0 |
| I | Segregation Compliant | Dropdown | 15 | List: Yes, No, N/A |
| J | Documentation Current | Dropdown | 15 | List: Yes, Partial, No |
| K | Last Inspection | Date | 15 | Date format |
| L | Compliance Status | Formula | 18 | Auto-calculated |
| M | Notes | Text | 40 | None |

**Compliance Status Formula:**
```excel
=IF(AND(G2<>"None", I2<>"No", J2<>"No"), "✅ Compliant",
   IF(OR(G2="None", I2="No"), "❌ Non-Compliant",
   "⚠️ Partial"))
```

### Sheet 3: Physical Protection

**Purpose:** Assess physical and environmental protection measures

**Columns:**

| Col | Field Name | Type | Width | Validation |
|-----|------------|------|-------|------------|
| A | Area ID | Text | 12 | None |
| B | Facility/Building | Text | 25 | None |
| C | Area Name | Text | 25 | None |
| D | EMI Protection | Dropdown | 15 | List: Yes - Shielded, Partial, No, N/A |
| E | Physical Damage Protection | Dropdown | 20 | List: Yes - Armoured, Yes - Enclosed, Partial, No |
| F | Water Protection | Dropdown | 15 | List: Yes, Partial, No, N/A |
| G | Heat Protection | Dropdown | 15 | List: Yes, Partial, No, N/A |
| H | Cable Route Risk Level | Dropdown | 15 | List: Low, Medium, High |
| I | Fibre Used for High Security | Dropdown | 15 | List: Yes, No, N/A |
| J | Compliance Status | Formula | 18 | Auto-calculated |
| K | Notes | Text | 40 | None |

### Sheet 4: Access Controls

**Purpose:** Document access controls for cabling infrastructure

**Columns:**

| Col | Field Name | Type | Width | Validation |
|-----|------------|------|-------|------------|
| A | Location ID | Text | 12 | None |
| B | Facility/Building | Text | 25 | None |
| C | Infrastructure Type | Dropdown | 18 | List: Wiring Closet, Patch Panel, Distribution Frame, Manhole, Duct Access |
| D | Location Description | Text | 30 | None |
| E | Lock Type | Dropdown | 20 | List: Electronic Access Card, Keyed Lock, Combination Lock, No Lock, Cage/Enclosure |
| F | Access Restricted | Dropdown | 25 | List: Yes - IT Only, Yes - Facilities Only, Yes - Authorised Personnel, No |
| G | Access Logged | Dropdown | 15 | List: Yes - Electronic, Yes - Manual, No |
| H | Occupied Monitoring | Dropdown | 15 | List: Yes - CCTV, Yes - Guards, No |
| I | Last Access Review | Date | 15 | Date format |
| J | Compliance Status | Formula | 18 | Auto-calculated |
| K | Notes | Text | 40 | None |

### Sheet 5: Documentation

**Purpose:** Audit cable documentation compliance

**Columns:**

| Col | Field Name | Type | Width | Validation |
|-----|------------|------|-------|------------|
| A | Document Type | Dropdown | 20 | List: Cable Schedule, Network Diagram, Labelling Standard, Change Log, Audit Report |
| B | Document Name | Text | 35 | None |
| C | Document Location | Text | 40 | None |
| D | Owner | Text | 25 | None |
| E | Last Updated | Date | 15 | Date format |
| F | Review Cycle | Dropdown | 15 | List: Annual, Quarterly, On Change |
| G | Current | Dropdown | 10 | List: Yes, No |
| H | Accessible | Dropdown | 15 | List: Yes - Online, Yes - Restricted, No |
| I | Compliance Status | Formula | 18 | Auto-calculated |
| J | Notes | Text | 40 | None |

### Sheet 6: Summary Dashboard

**Purpose:** Automated compliance scoring and metrics

**Structure:**
- Overall Compliance Score (weighted average)
- Domain Scores (Pathways, Protection, Access, Documentation)
- Gap Summary (auto-generated from non-compliant items)

**Weighting:**
- Cable Pathways: 30%
- Physical Protection: 25%
- Access Controls: 25%
- Documentation: 20%

### Sheet 7: Evidence Register

**Purpose:** Document supporting evidence for audit

**Columns:**
- Evidence ID, Evidence Type, Description, Related Sheet/Item
- File Name, File Location, Collection Date, Collected By
- Retention Period, Notes

### Sheet 8: Approval Sign-Off

**Purpose:** Four-level approval workflow

**Structure:**
- Assessment summary section
- Approval table (Role, Name, Signature, Date, Comments)

---

## Cell Styling Reference

### Colour Palette

**Headers:**
- Primary Header: #003366 (Navy blue), white text
- Column Header: #D9D9D9 (Light grey), black text

**Data Cells:**
- Input Cell: #FFFFCC (Light yellow)
- Formula Cell: #FFFFFF (White)

**Compliance Status:**
- Compliant: #C6EFCE (Light green)
- Partial: #FFEB9C (Light amber)
- Non-Compliant: #FFC7CE (Light red)

### Font Specifications

- Headers: Calibri, 14pt (primary), 10pt (column), Bold
- Data Cells: Calibri, 10pt, Regular

---

## Integration Points

### Integration with Policy

**Policy Section → Assessment Sheet Mapping:**

| Policy Section | Assessment Sheet | Focus |
|----------------|------------------|-------|
| Section 2.1.1: Cable Protection | Sheet 2, Sheet 3 | Pathways and protection measures |
| Section 2.1.2: Access Control | Sheet 4 | Infrastructure access controls |
| Section 2.1.3: Segregation Requirements | Sheet 2, Sheet 3 | Power/data segregation, fibre for security |
| Section 2.1.4: Documentation | Sheet 5 | Cable schedules, diagrams, labelling |
| Section 2.1.5: Inspection and Maintenance | Sheet 2 | Last inspection dates |

### Integration with Other Assessments

**Feeds into:**
- ISMS-IMP-A.7.12-13.S4 (Compliance Dashboard)
- Network security assessments

**Dependencies from:**
- Facility inventory
- Network documentation

---

**END OF SPECIFICATION**

---

*"The strength of the chain is the strength of the weakest link."*
— Thomas Reid

<!-- QA_VERIFIED: 2026-02-03 -->
