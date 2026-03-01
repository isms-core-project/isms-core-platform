<!-- ISMS-CORE:IMP:ISMS-IMP-A.7.8-9-S2-UG:framework:UG:a.7.8-9-s2 -->
**ISMS-IMP-A.7.8-9-S2-UG - Off-Premises Asset Security Assessment**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.7.9: Security of Assets Off-Premises

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Off-Premises Asset Security |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.7.8-9-S2-UG |
| **Related Policy** | ISMS-POL-A.7.8-9-S2 (Equipment Location Security) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.7.9 (Security of Assets Off-Premises) |
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

- ISMS-POL-A.7.8-9-S2 (Equipment Location Security)
- ISMS-IMP-A.7.8-9-S1 (Equipment Siting Assessment)

---

### Document Structure

This is the **User Completion Guide**. The companion Technical Specification is documented in ISMS-IMP-A.7.8-9-S2-TG.

---

## Workbook at a Glance

| # | Sheet Name | Purpose |
|---|-----------|---------|
| 1 | Instructions & Legend | How to use this workbook and understand the colour coding |
| 2 | Equipment Inventory | Catalogue all equipment approved for off-premises use |
| 3 | Authorisation | Track authorisation for equipment taken off-premises |
| 4 | Protection Measures | Assess security controls applied to off-premises equipment |
| 5 | Remote Working | Evaluate security of equipment used at remote work locations |
| 6 | Permanent Off-Site | Manage permanently off-site equipment deployments |
| 7 | Incidents | Record and track off-premises security incidents |
| 8 | Evidence Register | Store and reference evidence supporting assessments |
| 9 | Summary Dashboard | Compliance status and key metrics overview |
| 10 | Approval Sign-Off | Management review sign-off and certification |

---

## Assessment Overview

### Purpose & Scope

**Assessment Name:** ISMS-IMP-A.7.8-9-S2 - Off-Premises Asset Security Assessment

#### What This Assessment Covers

This assessment documents the SECURITY of organisation assets when used or stored off-premises. This is the "HOW are assets protected when outside our facilities?" assessment that answers:

- What equipment is authorised for removal from premises? (laptops, mobile devices, storage media)
- How is equipment removal authorised and tracked? (approval workflows, asset tracking)
- What protection measures are required for off-premises equipment? (encryption, physical security)
- How are remote working environments secured? (home offices, public spaces)
- What permanently off-site equipment exists? (ATMs, remote sensors, edge devices)
- What incidents have occurred with off-premises equipment? (loss, theft, compromise)

#### Key Principle

This assessment is **completely vendor-agnostic and device-independent**. You document YOUR specific off-premises equipment (whatever you have - laptops, tablets, mobile devices, edge devices), and verify protection measures against generic policy requirements from ISMS-POL-A.7.8-9, Section 2.2.

#### What You'll Document

**Authorisation and Tracking:**

- Equipment removal authorisation processes
- Asset tracking and chain of custody records
- Return verification procedures
- Overdue equipment tracking

**Off-Premises Protection Requirements:**

- Physical security measures (locks, unmarked bags)
- Environmental protection (temperature, moisture)
- Theft prevention (GPS tracking, remote wipe capability)
- Encryption and data protection

**Remote Working Security:**

- Home office requirements
- Public space protections (privacy screens, VPN)
- Network security (encrypted WiFi, VPN)
- Physical access controls at home

**Permanently Off-Site Equipment:**

- Fixed installations (ATMs, sensors, edge devices)
- Tamper detection and physical security
- Environmental monitoring
- Remote management capabilities

**Incident Tracking:**

- Equipment loss and theft incidents
- Compromise or damage events
- Response times and recovery actions
- Lessons learned and improvements

#### How This Relates to Other A.7.8-9 Assessments

| Assessment            | Focus                  | Relationship to A.7.8-9-S2      |
|-----------------------|------------------------|---------------------------------|
| ISMS-IMP-A.7.8-9-S1 | Equipment Siting | Equipment located ON premises |
| **ISMS-IMP-A.7.8-9-S2** | **Off-Premises Assets** | **Equipment used or stored OFF premises** |

This assessment (A.7.8-9-S2) focuses specifically on Control A.7.9 (Security of Assets Off-Premises). It complements the equipment siting assessment (A.7.8) in A.7.8-9-S1.

### Who Should Complete This Assessment

#### Primary Stakeholders

1. **IT Operations** - Endpoint device management and MDM
2. **Security Operations** - Security monitoring and incident response
3. **Line Managers** - Equipment removal authorisations
4. **HR** - Remote working policy and employee off-boarding
5. **Compliance Officers** - Audit requirements and evidence collection

#### Required Skills

- Understanding of mobile device management (MDM) platforms
- Familiarity with endpoint security technologies (encryption, remote wipe)
- Knowledge of remote working security best practices
- Understanding of asset tracking and chain of custody processes
- Access to asset management and MDM systems

#### Time Commitment

- **Initial assessment:** 6-10 hours (comprehensive review of off-premises equipment and policies)
- **Semi-annual updates:** 2-3 hours (update incidents, verify controls, review policy compliance)

### Expected Outputs

Upon completion, you will have:

1. **Off-premises equipment inventory** - All equipment authorised for off-premises use
2. **Authorisation process review** - Verification of removal and tracking procedures
3. **Protection measures assessment** - Security controls for off-premises equipment
4. **Remote working evaluation** - Home office and public space security
5. **Permanent installation review** - Fixed off-site equipment security
6. **Incident tracking** - Loss, theft, and compromise events documented
7. **Gap analysis** - Identified gaps between current state and policy requirements
8. **Evidence register** - Supporting documentation for audit
9. **Approved assessment** - Four-level approval workflow completed

---

## Prerequisites

### Information You'll Need

Before starting this assessment, gather:

#### 1. System Access

- Access to asset management system (equipment inventory)
- Access to Mobile Device Management (MDM) platform
- Access to equipment removal authorisation records
- Access to incident management system (loss/theft reports)
- Access to HR records (remote working agreements)

#### 2. Documentation

- Equipment removal policy and authorisation forms
- Remote working policy documentation
- MDM configuration and compliance reports
- Encryption policy and deployment records
- Permanently off-site equipment inventory
- Incident response procedures for lost/stolen equipment

#### 3. Historical Data

- Equipment removal authorisation records (last 12 months)
- MDM compliance reports (encryption, remote wipe capability)
- Equipment loss and theft incidents (last 12 months)
- Remote working security audit results
- Equipment return and recovery records

#### 4. Policy Requirements

- ISMS-POL-A.7.8-9, Section 2.2 (Security of Assets Off-Premises)
  - Section 2.2.1: Authorisation and Tracking
  - Section 2.2.2: Off-Premises Protection Requirements
  - Section 2.2.3: Working Remotely
  - Section 2.2.4: Permanently Off-Site Equipment

### Required Tools

- Microsoft Excel (2016 or later) for workbook completion
- Access to MDM console (Microsoft Intune, Jamf, VMware Workspace ONE, etc.)
- Access to asset management system
- Screen capture tools (for evidence screenshots)

### Dependencies

This assessment has NO dependencies on other assessments - it can be completed independently.

However, outputs from this assessment are INPUT to:

- ISMS-IMP-A.6.7 (Remote Working) - Related remote working controls

---

## Workflow

### High-Level Process

```
1. PREPARE
   |
2. INVENTORY OFF-PREMISES EQUIPMENT (Sheet 2: Equipment Inventory)
   |
3. REVIEW AUTHORISATION PROCESSES (Sheet 3: Authorisation & Tracking)
   |
4. ASSESS PROTECTION MEASURES (Sheet 4: Protection Measures)
   |
5. EVALUATE REMOTE WORKING SECURITY (Sheet 5: Remote Working)
   |
6. REVIEW PERMANENT INSTALLATIONS (Sheet 6: Permanent Off-Site)
   |
7. DOCUMENT INCIDENTS (Sheet 7: Incidents)
   |
8. COLLECT EVIDENCE (Sheet 8: Evidence Register)
   |
9. REVIEW SUMMARY (Sheet 9: Summary Dashboard)
   |
10. QUALITY CHECK (Self-assessment against checklist)
    |
11. OBTAIN APPROVALS (Sheet 10: Approval Sign-Off)
    |
12. SUBMIT FOR AUDIT
```

### Detailed Step-by-Step

**Step 1: Preparation (Day 1 - 2 hours)**

- Read this Part I User Guide completely
- Review ISMS-POL-A.7.8-9, Section 2.2 requirements
- Gather all prerequisites (MDM access, asset inventory, incident records)
- Schedule time with IT Operations and Security
- Download or generate assessment workbook (Excel file)

**Step 2: Equipment Inventory (Day 1-2 - 2-3 hours)**

- Complete Sheet 1 (Instructions & Legend) - organisation info, assessment date
- Complete Sheet 2 (Equipment Inventory) - inventory all equipment categories authorised for off-premises use
- Document equipment types, quantities, and primary use cases
- Verify inventory against MDM and asset management systems

**Step 3: Authorisation Review (Day 2 - 2 hours)**

- Complete Sheet 3 (Authorisation & Tracking) - review removal authorisation processes
- Document approval workflows and tracking mechanisms
- Verify chain of custody records maintained
- Assess return verification procedures

**Step 4: Protection Measures Assessment (Day 2-3 - 2-3 hours)**

- Complete Sheet 4 (Protection Measures) for each equipment category
- Verify encryption status across all mobile devices
- Confirm remote wipe capability enabled
- Review physical security requirements and compliance

**Step 5: Remote Working Evaluation (Day 3-4 - 2-3 hours)**

- Complete Sheet 5 (Remote Working) for remote work scenarios
- Document home office security requirements
- Assess public space protections (privacy screens, VPN)
- Review network security controls

**Step 6: Permanent Installation Review (Day 4 - 1-2 hours)**

- Complete Sheet 6 (Permanent Off-Site) for fixed installations
- Document tamper detection and physical security
- Review environmental monitoring
- Verify remote management capabilities

**Step 7: Incident Documentation (Day 4-5 - 1-2 hours)**

- Complete Sheet 7 (Incidents) for loss, theft, and compromise events
- Document all equipment security incidents (last 12 months)
- Record response times and recovery actions
- Identify trends and lessons learned

**Step 8: Evidence Collection (Day 5 - 2 hours)**

- Export equipment removal authorisation records
- Document remote wipe test results
- Record evidence in Sheet 8 (Evidence Register)

**Step 9: Summary Review (Day 5 - 1 hour)**

- Review Sheet 9 (Summary Dashboard) - auto-calculated compliance scores
- Verify scores appear correct
- Identify areas below threshold
- Prepare gap remediation plan

**Step 10: Quality Check (Day 5-6 - 1 hour)**

- Complete self-assessment using Quality Checklist
- Verify all required fields completed
- Verify evidence register complete

**Step 11: Obtain Approvals (Day 6-12 - asynchronous)**

- Complete Sheet 10 (Approval Sign-Off) - Level 1: Assessor
- Submit through approval workflow

**Step 12: Submit for Audit (Post-Approval)**

- Assessment workbook is audit-ready
- Provide to auditors with evidence files

---

## Completing Each Sheet

### Sheet 1: Instructions & Legend

**Purpose:** Assessment metadata and legend for status indicators

**What to Complete:**

- Assessment Date: Date you started this assessment
- Completed By: Your name and role
- Organisation: [Organisation] name

**Time Required:** 5 minutes

### Sheet 2: Equipment Inventory

**Purpose:** Document all equipment categories authorised for off-premises use

**Structure:** 50 data rows for equipment categories (not individual devices)

**What to Document (Per Equipment Category):**

**Column A - Category ID:**

- Unique identifier: "CAT-001", "CAT-002", etc.

**Column B - Equipment Category:**

- Category name: "Corporate Laptops", "Mobile Phones", "Tablets", "USB Storage", "External Hard Drives"

**Column C - Equipment Type:**

- Dropdown: "Laptop", "Mobile Phone", "Tablet", "Storage Media", "Edge Device", "Other"

**Column D - Total Count:**

- Total devices in this category: 150, 200, 50, etc.

**Column E - Off-Premises Count:**

- Devices regularly used off-premises: 120, 180, 30, etc.

**Column F - Primary Use Case:**

- Primary reason for off-premises use: "Remote working", "Business travel", "Field service", "Customer demos"

**Column G - MDM Managed:**

- Dropdown: "Yes - All devices", "Partial", "No"
- Policy requirement: All mobile devices should be MDM managed

**Column H - Encryption Enabled:**

- Dropdown: "Yes - 100%", "Partial (>80%)", "Low (<80%)", "No"
- Policy requirement: 100% encryption for devices leaving premises

**Column I - Remote Wipe Capable:**

- Dropdown: "Yes - Tested", "Yes - Not tested", "No"
- Policy requirement: Remote wipe capability required and tested

**Column J - GPS Tracking:**

- Dropdown: "Yes - Enabled", "Available - Not enabled", "Not available"

**Column K - Last Compliance Check:**

- Date of last MDM compliance verification: "15.01.2026"

**Column L - Compliance Status:**

- Formula auto-calculates based on requirements

**Column M - Notes:**

- Additional context: "BYOD devices excluded from count", "Encryption rollout Q1 2026"

**Time Required:** 30-45 minutes for equipment category inventory

### Sheet 3: Authorisation & Tracking

**Purpose:** Document equipment removal authorisation and tracking processes

**Structure:** Assessment of authorisation controls per equipment category

**What to Document:**

**Column A - Category ID:**

- Link to Sheet 2: "CAT-001", etc.

**Column B - Equipment Category:**

- From Sheet 2

**Column C - Authorisation Required:**

- Dropdown: "Yes - Manager approval", "Yes - IT approval", "Yes - Auto-approved", "No approval required"

**Column D - Authorisation Method:**

- How authorisation is obtained: "ServiceNow ticket", "Email to manager", "Self-service portal", "Asset tag checkout"

**Column E - Tracking System:**

- System tracking equipment location: "CMDB", "MDM", "Spreadsheet", "None"

**Column F - Chain of Custody:**

- Dropdown: "Yes - Full tracking", "Partial", "No"
- Policy requirement: Chain of custody for high-value equipment

**Column G - Return Verification:**

- Dropdown: "Yes - Physical check", "Yes - System check", "No verification"

**Column H - Overdue Alert:**

- Dropdown: "Yes - Automated", "Yes - Manual review", "No"
- Alerts when equipment not returned by expected date

**Column I - Current Overdue Count:**

- Number of currently overdue items: 0, 5, 10, etc.

**Column J - Last Process Review:**

- Date of last authorisation process review: "01.12.2025"

**Column K - Compliance Status:**

- Formula auto-calculates

**Column L - Notes:**

- Additional context: "New tracking system implemented Q4 2025"

**Time Required:** 30 minutes for authorisation process review

### Sheet 4: Protection Measures

**Purpose:** Document protection measures for off-premises equipment

**Structure:** Protection requirements per equipment category

**What to Document:**

**Column A - Category ID:**

- Link to Sheet 2

**Column B - Equipment Category:**

- From Sheet 2

**Column C - Physical Security:**

- Dropdown: "Cable lock required", "Secure bag required", "No requirement"

**Column D - Transport Guidelines:**

- Dropdown: "Yes - Documented", "Partial", "No guidelines"
- Guidelines for secure transport

**Column E - Public Place Rules:**

- Dropdown: "Yes - Never unattended", "Yes - Partial rules", "No rules"

**Column F - Storage When Not In Use:**

- Dropdown: "Locked storage required", "Secure location recommended", "No requirement"

**Column G - Environmental Protection:**

- Dropdown: "Yes - Guidelines provided", "Partial", "No guidelines"
- Temperature, moisture protection during transport

**Column H - Privacy Screen Required:**

- Dropdown: "Yes - Always", "Yes - For sensitive data", "No"

**Column I - VPN Required:**

- Dropdown: "Yes - All connections", "Yes - Untrusted networks", "No requirement"

**Column J - Screen Lock Timeout:**

- Screen lock timeout configured: "5 min", "10 min", "15 min", "Not configured"

**Column K - Compliance Status:**

- Formula auto-calculates

**Column L - Notes:**

- Additional context

**Time Required:** 30-45 minutes for protection measures assessment

### Sheet 5: Remote Working

**Purpose:** Document security requirements for remote working scenarios

**Structure:** Assessment of remote working controls

**What to Document (Per Work Scenario):**

**Column A - Scenario ID:**

- Unique identifier: "RW-001", "RW-002", etc.

**Column B - Work Scenario:**

- Scenario name: "Home Office - Regular", "Home Office - Sensitive Data", "Public Space - Coffee Shop", "Travel - Hotel", "Travel - Client Site"

**Column C - Data Sensitivity:**

- Dropdown: "High (PII, Financial)", "Medium (Internal)", "Low (Public)"

**Column D - VPN Requirement:**

- Dropdown: "Required - Always", "Required - Sensitive only", "Recommended", "Not required"

**Column E - Privacy Screen:**

- Dropdown: "Required", "Recommended", "Not required"

**Column F - WiFi Security:**

- Dropdown: "Encrypted only", "VPN for public WiFi", "No requirement"

**Column G - Physical Security:**

- Dropdown: "Locked when away", "Not visible to others", "No requirement"

**Column H - Visitor Access:**

- Dropdown: "No access allowed", "Supervised access only", "N/A"

**Column I - Bluetooth/Wireless:**

- Dropdown: "Disable when not needed", "No requirement"

**Column J - Worker Count:**

- Approximate workers in this scenario: 50, 100, 200, etc.

**Column K - Last Review:**

- Date of last scenario review: "15.01.2026"

**Column L - Compliance Status:**

- Formula auto-calculates based on data sensitivity and controls

**Column M - Notes:**

- Additional context: "New policy issued Jan 2026"

**Time Required:** 30-45 minutes for remote working assessment

### Sheet 6: Permanent Off-Site

**Purpose:** Document security for permanently installed off-site equipment

**Structure:** Assessment of fixed off-premises installations

**What to Document (Per Installation):**

**Column A - Installation ID:**

- Unique identifier: "PERM-001", "PERM-002", etc.

**Column B - Installation Name:**

- Descriptive name: "ATM Network", "Remote Sensor Array", "Edge Computing Nodes", "Digital Signage"

**Column C - Installation Type:**

- Dropdown: "ATM/Kiosk", "Sensor/IoT", "Edge Computing", "Signage", "Antenna/Telecom", "Other"

**Column D - Location Count:**

- Number of installations: 10, 50, 100, etc.

**Column E - Physical Security:**

- Dropdown: "Tamper detection", "Locked enclosure", "Public exposure"

**Column F - Environmental Monitoring:**

- Dropdown: "Yes - Continuous", "Yes - Periodic", "No"

**Column G - Remote Management:**

- Dropdown: "Yes - Full control", "Partial", "No"

**Column H - Inspection Schedule:**

- Inspection frequency: "Monthly", "Quarterly", "Annual", "None"

**Column I - Last Inspection:**

- Date of last physical inspection: "01.01.2026"

**Column J - Incident Response:**

- Dropdown: "Yes - Documented", "Partial", "No procedure"
- Procedure for incidents at remote locations

**Column K - Compliance Status:**

- Formula auto-calculates

**Column L - Notes:**

- Additional context: "New tamper detection installed Q4 2025"

**Time Required:** 20-30 minutes for permanent installation review

### Sheet 7: Incidents

**Purpose:** Document equipment security incidents (loss, theft, compromise)

**Structure:** 100 data rows for incident logging

**What to Document (Per Incident):**

**Column A - Incident ID:**

- Unique identifier: "INC-001", "INC-002", etc.

**Column B - Incident Date:**

- Date of incident: "15.12.2025"

**Column C - Equipment Category:**

- Link to Sheet 2: "Corporate Laptop", "Mobile Phone", etc.

**Column D - Incident Type:**

- Dropdown: "Lost", "Stolen", "Damaged", "Compromised", "Near Miss"

**Column E - Location:**

- Where incident occurred: "Public transport", "Hotel", "Home", "Client site", "Office"

**Column F - Data at Risk:**

- Dropdown: "High (PII, Financial)", "Medium (Internal)", "Low (Public)", "None (encrypted)"

**Column G - Remote Wipe Executed:**

- Dropdown: "Yes - Successful", "Yes - Failed", "No - Not needed", "No - Not possible"

**Column H - Time to Report (hours):**

- Hours from incident to report: 1, 4, 24, etc.

**Column I - Recovery Status:**

- Dropdown: "Recovered", "Not recovered", "Insurance claim", "Replaced"

**Column J - Root Cause:**

- Identified cause: "Left unattended", "Vehicle break-in", "Dropped/damaged", "Unknown"

**Column K - Corrective Action:**

- Action taken: "Policy reminder issued", "Training required", "Equipment upgrade", "No action needed"

**Column L - Notes:**

- Additional context

**Time Required:** 30-60 minutes for incident documentation (depending on incident volume)

### Sheet 8: Evidence Register

**Purpose:** Document all supporting evidence for audit traceability

**Structure:** Standard evidence register format

**Common Evidence to Collect:**

1. **Equipment Inventory Evidence:**
   - MDM device inventory export
   - Asset management system report

2. **Authorisation Evidence:**
   - Equipment removal policy document
   - Sample authorisation forms/tickets
   - Tracking system screenshots

3. **Protection Measures Evidence:**
   - MDM configuration screenshots
   - Remote wipe test results
   - Physical security guidelines document

4. **Remote Working Evidence:**
   - Remote working policy document
   - VPN configuration evidence
   - Privacy screen deployment records

5. **Incident Evidence:**
   - Incident reports
   - Remote wipe execution logs
   - Recovery documentation

**Time Required:** 2 hours for evidence collection

### Sheet 9: Summary Dashboard

**Purpose:** Automated compliance scoring

**What to Review:**

- Overall Off-Premises Security Score
- Equipment Inventory Compliance
- Authorisation Process Compliance
- Protection Measures Compliance
- Remote Working Compliance
- Permanent Installation Compliance
- Incident Metrics (loss rate, recovery rate)
- Gap Summary

**Time Required:** 15-30 minutes for review

### Sheet 10: Approval Sign-Off

**Purpose:** Four-level approval workflow

**Approval Levels:**

- Level 1: Assessor (You)
- Level 2: IT Operations Manager
- Level 3: CISO
- Level 4: Compliance Officer

**Time Required:** 5 minutes for Level 1, then asynchronous

---

## Evidence Collection

### What Evidence to Collect

**1. Equipment and MDM Evidence**

- Device encryption status reports
- Remote wipe capability verification
- Asset inventory exports

**2. Authorisation Evidence**

- Equipment removal policy document
- Sample authorisation records
- Tracking system configuration
- Overdue equipment reports

**3. Protection Measures Evidence**

- Physical security guidelines
- Transport and storage requirements
- Privacy screen deployment records
- VPN configuration evidence

**4. Remote Working Evidence**

- Remote working policy
- Home office security checklist
- VPN usage reports
- Security awareness training records

**5. Incident Evidence**

- Incident reports and investigations
- Remote wipe execution logs
- Recovery and replacement records
- Trend analysis reports

### Evidence Storage

**Storage Location:**

- SharePoint > ISMS > Assessments > A.7.9 > Evidence

**Retention:**

- Minimum: 3 years

---

## Common Pitfalls

### Pitfall 1: Confusing Device Count with Category Assessment

**Problem:** Trying to document every individual device instead of equipment categories

**How to Avoid:**

- Assess at category level (laptops, mobile phones, tablets)
- Use MDM and asset management for individual device tracking
- Focus on controls that apply to the category, not device-by-device

### Pitfall 2: Ignoring BYOD Devices

**Problem:** Only assessing corporate-owned devices, missing BYOD

**How to Avoid:**

- Include BYOD as a separate category if applicable
- Document BYOD policy and controls
- Verify BYOD devices meet security requirements

### Pitfall 3: Assuming MDM = Compliant

**Problem:** Documenting "MDM enrolled" without verifying actual compliance

**Example:** Device enrolled but encryption disabled, remote wipe not tested

**How to Avoid:**

- Verify actual compliance status in MDM console
- Check encryption percentage, not just enrollment
- Test remote wipe capability periodically

### Pitfall 4: Not Testing Remote Wipe

**Problem:** Claiming remote wipe capability without ever testing it

**How to Avoid:**

- Document last remote wipe test date
- Include test devices in regular testing schedule
- Verify wipe actually removes data, not just factory reset

### Pitfall 5: Missing Permanent Installations

**Problem:** Only assessing portable devices, forgetting fixed installations

**Example:** ATMs, remote sensors, edge devices not included

**How to Avoid:**

- Create inventory of ALL off-premises equipment
- Include fixed installations that never return to premises
- Assess physical security and tamper detection

### Pitfall 6: Underreporting Incidents

**Problem:** Only documenting major incidents, missing near-misses and minor events

**How to Avoid:**

- Document ALL equipment security events
- Include near-misses (left unattended but recovered)
- Track trends to identify systemic issues

### Pitfall 7: Outdated Remote Working Assessment

**Problem:** Using pre-pandemic remote working assessment, not reflecting current state

**How to Avoid:**

- Review remote working policies and actual practices
- Verify controls still match current work patterns
- Include hybrid working scenarios

### Pitfall 8: Insufficient Authorisation Tracking

**Problem:** Equipment removal authorised but no tracking of actual removals

**How to Avoid:**

- Verify tracking system captures actual movements
- Check for equipment never returned
- Reconcile asset inventory with tracking records

### Pitfall 9: Formula Corruption

**Problem:** Accidentally overwriting formula cells

**How to Avoid:**

- Dashboard and Compliance Status columns are formulas
- Do not edit formula cells
- Save backup before making changes

### Pitfall 10: Approval Workflow Shortcuts

**Problem:** Skipping approval levels

**How to Avoid:**

- Follow four-level workflow in order
- Each level reviews and signs
- Corrections return to assessor

---

## Quality Checklist

Before submitting for Level 2 approval, complete this self-assessment:

### Sheet 2: Equipment Inventory

- [ ] All equipment categories documented
- [ ] Total counts accurate
- [ ] MDM status verified
- [ ] Encryption compliance verified
- [ ] Remote wipe capability documented
- [ ] Last compliance check current

### Sheet 3: Authorisation & Tracking

- [ ] Authorisation process documented for each category
- [ ] Tracking mechanisms identified
- [ ] Chain of custody requirements documented
- [ ] Return verification process assessed
- [ ] Overdue counts current

### Sheet 4: Protection Measures

- [ ] Physical security requirements documented
- [ ] Transport guidelines assessed
- [ ] Public place rules documented
- [ ] Privacy screen requirements clear
- [ ] VPN requirements documented

### Sheet 5: Remote Working

- [ ] All work scenarios documented
- [ ] Data sensitivity assessed
- [ ] Security controls match sensitivity
- [ ] Worker counts estimated
- [ ] Recent review completed

### Sheet 6: Permanent Off-Site

- [ ] All permanent installations documented
- [ ] Physical security assessed
- [ ] Remote management capability verified
- [ ] Inspection schedule documented
- [ ] Incident response procedures assessed

### Sheet 7: Incidents

- [ ] All incidents from last 12 months documented
- [ ] Incident types classified
- [ ] Root causes identified
- [ ] Corrective actions documented
- [ ] Recovery status updated

### Sheet 8: Evidence Register

- [ ] At least 10 evidence items documented
- [ ] Evidence files exist at documented locations
- [ ] Collection dates recent

### Overall

- [ ] All compliance status formulas working
- [ ] No blank required fields
- [ ] Ready for Level 2 approval

---

## Review & Approval

### Four-Level Approval Workflow

**Approval Sequence:** Assessor -> IT Operations Manager -> CISO -> Compliance Officer

### Level 1: Assessor

- Complete all sheets
- Collect evidence
- Complete quality checklist

### Level 2: IT Operations Manager

- Verify MDM and asset data accuracy
- Review protection measures
- Confirm incident documentation

### Level 3: CISO

- Review overall compliance score
- Assess remediation priorities
- Approve resource allocation

### Level 4: Compliance Officer

- Verify audit readiness
- Confirm evidence completeness
- Final sign-off

---

**END OF USER GUIDE**

---

*"A device off-site is not off the policy."*
— Anon

<!-- QA_VERIFIED: 2026-03-01 -->
