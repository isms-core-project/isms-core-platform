**ISMS-IMP-A.7.12-13.S2-UG - Equipment Maintenance Assessment**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.7.13: Equipment Maintenance

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.7.12-13.S2-UG |
| **Version** | 1.0 |
| **Assessment Area** | Equipment Maintenance - Maintenance Programme, Personnel, Security During Maintenance, Remote Maintenance, Records |
| **Related Policy** | ISMS-POL-A.7.12-13, Section 2.2 (Equipment Maintenance) |
| **Purpose** | Document equipment maintenance practices, assess compliance against policy requirements, and identify gaps |
| **Target Audience** | IT Operations, Facilities Management, System Administrators, Vendor Managers, Compliance Officers, Auditors |
| **Assessment Type** | Technical & Operational |
| **Review Cycle** | Quarterly or After Major Maintenance Events |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Equipment Maintenance assessment workbook | ISMS Implementation Team |

### Document Structure

This is the **User Completion Guide**. The companion Technical Specification is documented in ISMS-IMP-A.7.12-13.S2-TG.

---

## Assessment Overview

### Purpose & Scope

**Assessment Name:** ISMS-IMP-A.7.12-13.S2 - Equipment Maintenance Assessment

#### What This Assessment Covers

This assessment documents the equipment MAINTENANCE practices across your organisation. This is the "HOW do we maintain our equipment?" assessment that answers:

- What equipment is included in the maintenance programme? (servers, network devices, UPS, HVAC, security systems)
- Are maintenance schedules aligned with manufacturer recommendations?
- Who performs maintenance? (internal staff, third-party vendors)
- How is security maintained during maintenance activities?
- How is remote maintenance controlled and monitored?
- How are maintenance records documented and retained?
- What happens when equipment must be removed for off-site maintenance?

#### Key Principle

This assessment is **completely vendor-agnostic and technology-independent**. You document YOUR specific maintenance practices (whatever equipment you have - Dell, HP, Cisco, Schneider, whatever vendors), and verify practices against generic policy requirements from ISMS-POL-A.7.12-13, Section 2.2.

#### What You'll Document

**Equipment Inventory:**

- All equipment types included in maintenance programme
- Manufacturer maintenance recommendations
- Criticality classification (Tier 1, Tier 2)
- Current maintenance status

**Maintenance Programme:**

- Preventive maintenance schedules
- Manufacturer recommendation compliance
- Critical equipment prioritisation
- Maintenance record keeping

**Maintenance Personnel:**

- Authorised internal personnel
- Approved third-party maintenance providers
- Personnel verification procedures
- Supervision requirements

**Security During Maintenance:**

- Data protection during maintenance
- Access controls during maintenance
- Tool and equipment accountability
- Physical inspection after maintenance

**Remote Maintenance:**

- Remote maintenance authorisation
- Secure connection requirements
- Session logging and monitoring
- Access control (enable/disable)

**Equipment Removal:**

- Authorisation for off-site maintenance
- Data erasure requirements
- Chain of custody documentation
- Return inspection procedures

**Maintenance Records:**

- Record completeness requirements
- Retention periods
- Audit accessibility

#### How This Relates to Other A.7.12-13 Assessments

| Assessment            | Focus                  | Relationship to A.7.12-13.S2      |
|-----------------------|------------------------|------------------------------------|
| ISMS-IMP-A.7.12-13.S1 | Cabling Security | Cable protection and documentation |
| **ISMS-IMP-A.7.12-13.S2** | **Equipment Maintenance** | **Maintenance practices and records** |
| ISMS-IMP-A.7.12-13.S3 | Maintenance Schedule | Preventive maintenance planning and tracking |
| ISMS-IMP-A.7.12-13.S4 | Compliance Dashboard | Consolidated view across cabling and maintenance |

This assessment (A.7.12-13.S2) focuses specifically on Control A.7.13 (Equipment Maintenance). It complements assessments for A.7.12 (Cabling Security) and the detailed schedule tracking in S3.

### Who Should Complete This Assessment

#### Primary Stakeholders

1. **IT Operations Manager** - Overall equipment maintenance ownership
2. **System Administrators** - Server and network equipment maintenance
3. **Facilities Manager** - Infrastructure equipment (UPS, HVAC, security)
4. **Vendor Manager** - Third-party maintenance contracts
5. **Compliance Officers** - Audit requirements and evidence collection

#### Required Skills

- Understanding of equipment maintenance requirements
- Familiarity with vendor maintenance recommendations
- Knowledge of data protection during maintenance
- Understanding of remote access security
- Access to maintenance records and vendor contracts

#### Time Commitment

- **Initial assessment:** 8-12 hours (comprehensive review of maintenance programme)
- **Quarterly updates:** 2-4 hours (review recent maintenance activities, update records)

### Expected Outputs

Upon completion, you will have:

1. ✅ **Equipment maintenance inventory** - All equipment in maintenance programme documented
2. ✅ **Schedule compliance assessment** - Verification against manufacturer recommendations
3. ✅ **Personnel verification** - Authorised personnel and vendors documented
4. ✅ **Security assessment** - Data protection and access controls verified
5. ✅ **Remote maintenance review** - Remote access controls documented
6. ✅ **Record keeping audit** - Maintenance records completeness verified
7. ✅ **Gap analysis** - Identified gaps between practices and policy requirements
8. ✅ **Approved assessment** - Four-level approval workflow completed

---

## Prerequisites

### Information You'll Need

Before starting this assessment, gather:

#### 1. System Access

- Access to CMDB or asset management system
- Access to ITSM/ticketing system (maintenance records)
- Access to vendor maintenance portals
- Access to remote access systems (VPN, remote management)

#### 2. Documentation

- Equipment inventory with maintenance requirements
- Manufacturer maintenance recommendations (per equipment type)
- Maintenance contracts with third-party vendors
- Maintenance procedures and checklists
- Remote maintenance access procedures
- Equipment removal authorisation procedures

#### 3. Historical Data

- Maintenance records (last 12 months)
- Vendor maintenance reports
- Remote maintenance session logs (last 90 days)
- Equipment removal logs (last 12 months)
- Maintenance-related incidents

#### 4. Policy Requirements

- ISMS-POL-A.7.12-13, Section 2.2 (Equipment Maintenance Requirements)
  - Section 2.2.1: Maintenance Programme
  - Section 2.2.2: Maintenance Personnel
  - Section 2.2.3: Security During Maintenance
  - Section 2.2.4: Remote Maintenance
  - Section 2.2.5: Equipment Removal for Maintenance
  - Section 2.2.6: Maintenance Records

### Required Tools

- Microsoft Excel (2016 or later) for workbook completion
- Access to asset management/CMDB systems
- Access to maintenance ticketing system
- Access to vendor contracts/portals
- Screen capture tools (for evidence screenshots)

### Dependencies

This assessment has NO dependencies on other assessments - it can be completed independently.

However, outputs from this assessment are INPUT to:

- ISMS-IMP-A.7.12-13.S3 (Maintenance Schedule Tracking) - Detailed schedule compliance
- ISMS-IMP-A.7.12-13.S4 (Compliance Dashboard) - Consolidated compliance view

---

## Workflow

### High-Level Process

```
1. PREPARE
   ↓
2. INVENTORY EQUIPMENT (Sheet 2: Equipment Inventory)
   ↓
3. ASSESS MAINTENANCE PROGRAMME (Sheet 3: Maintenance Programme)
   ↓
4. VERIFY PERSONNEL (Sheet 4: Personnel & Vendors)
   ↓
5. REVIEW SECURITY CONTROLS (Sheet 5: Security During Maintenance)
   ↓
6. AUDIT REMOTE MAINTENANCE (Sheet 6: Remote Maintenance)
   ↓
7. COLLECT EVIDENCE (Sheet 8: Evidence Register)
   ↓
8. REVIEW SUMMARY (Sheet 7: Summary Dashboard)
   ↓
9. QUALITY CHECK
   ↓
10. OBTAIN APPROVALS (Sheet 9: Approval Sign-Off)
```

### Detailed Step-by-Step

**Step 1: Preparation (Day 1 - 2 hours)**

- Read this Part I User Guide completely
- Review ISMS-POL-A.7.12-13, Section 2.2 requirements
- Gather all prerequisites (documentation, access, historical data)
- Schedule time with IT Operations Manager and Facilities Manager
- Download or generate assessment workbook (Excel file)

**Step 2: Equipment Inventory (Day 1-2 - 2-3 hours)**

- Open assessment workbook
- Complete Sheet 1 (Instructions & Legend)
- Complete Sheet 2 (Equipment Inventory) - document all equipment in maintenance programme
- Classify equipment by criticality (Tier 1, Tier 2)
- Document manufacturer maintenance requirements

**Step 3: Maintenance Programme Assessment (Day 2-3 - 2-3 hours)**

- Complete Sheet 3 (Maintenance Programme)
- Compare scheduled maintenance vs. manufacturer recommendations
- Verify preventive maintenance is occurring on schedule
- Identify any overdue maintenance

**Step 4: Personnel Verification (Day 3 - 2 hours)**

- Complete Sheet 4 (Personnel & Vendors)
- Document authorised internal maintenance personnel
- List approved third-party maintenance providers
- Verify supervision requirements are met

**Step 5: Security Controls Review (Day 3-4 - 2 hours)**

- Complete Sheet 5 (Security During Maintenance)
- Verify data protection measures during maintenance
- Check access controls during maintenance activities
- Review equipment accountability procedures

**Step 6: Remote Maintenance Audit (Day 4 - 2 hours)**

- Complete Sheet 6 (Remote Maintenance)
- Review remote access authorisation process
- Verify secure connection requirements
- Check session logging and monitoring
- Verify access enable/disable controls

**Step 7: Evidence Collection (Day 4-5 - 2-3 hours)**

- Collect maintenance records samples
- Screenshot maintenance systems and logs
- Collect vendor contract excerpts
- Document in Sheet 8 (Evidence Register)

**Step 8: Summary Review (Day 5 - 1 hour)**

- Review Sheet 7 (Summary Dashboard)
- Verify compliance scores accurate
- Identify gaps requiring remediation

**Step 9: Quality Check (Day 5 - 1 hour)**

- Complete self-assessment using Quality Checklist
- Verify all required fields completed

**Step 10: Obtain Approvals (Day 6-10 - asynchronous)**

- Complete Sheet 9 (Approval Sign-Off)
- Follow four-level approval workflow

---

## Completing Each Sheet

### Sheet 1: Instructions & Legend

**Purpose:** Assessment metadata and legend for status indicators

**What to Complete:**

- Assessment Date
- Completed By (your name and role)
- Organisation name

**Time Required:** 5 minutes

### Sheet 2: Equipment Inventory

**Purpose:** Document all equipment included in maintenance programme

**Structure:** 100 data rows for documenting equipment

**What to Document (Per Equipment Type or System):**

**Column A - Equipment ID:**

- Asset tag or unique identifier: "SRV-001", "UPS-DC1-01", "SW-CORE-01"

**Column B - Equipment Type:**

- Dropdown: "Server", "Network Device", "Storage", "UPS", "HVAC", "Security System", "Other"

**Column C - Equipment Description:**

- Specific model/description: "Dell PowerEdge R740", "Cisco Catalyst 9300", "Schneider Smart-UPS"

**Column D - Location:**

- Where equipment is located: "Datacenter 1", "Server Room A", "IDF Floor 2"

**Column E - Criticality:**

- Dropdown: "Tier 1 - Critical", "Tier 2 - Standard"

**Column F - Manufacturer:**

- Equipment manufacturer: "Dell", "Cisco", "HP", "Schneider"

**Column G - Manufacturer Maintenance Requirement:**

- What manufacturer recommends: "Annual firmware + inspection", "Quarterly battery check", "Semi-annual filter replacement"

**Column H - Maintenance Frequency:**

- Actual scheduled frequency: "Annually", "Semi-annually", "Quarterly", "Monthly"

**Column I - Frequency Compliant:**

- Dropdown: "Yes", "No"
- Does scheduled frequency meet or exceed manufacturer requirement?

**Column J - In Maintenance Programme:**

- Dropdown: "Yes", "No", "Partial"

**Column K - Last Maintenance:**

- Date of last maintenance: "15.01.2026"

**Column L - Next Scheduled:**

- Date of next scheduled maintenance: "15.07.2026"

**Column M - Compliance Status:**

- Formula auto-calculates

**Column N - Notes:**

- Any additional context

**Time Required:** 45-60 minutes for comprehensive equipment inventory

### Sheet 3: Maintenance Programme

**Purpose:** Assess maintenance programme compliance

**What to Document:**

**Programme Elements:**

- All equipment types covered: Yes/No
- Manufacturer recommendations followed: Yes/Partial/No
- Critical equipment prioritised: Yes/No
- Maintenance records maintained: Yes/Partial/No

**Schedule Compliance:**

- Preventive maintenance on schedule: % compliant
- Overdue maintenance items: Count
- Average days overdue (if any)

**Record Keeping:**

- Records include required fields: Yes/Partial/No
- Retention period met: Yes/No
- Records accessible for audit: Yes/No

**Time Required:** 30-45 minutes

### Sheet 4: Personnel & Vendors

**Purpose:** Document authorised maintenance personnel and vendors

**What to Document (Per Person or Vendor):**

**Column A - Personnel/Vendor ID:**

- Unique identifier: "INT-001" (internal), "VEN-001" (vendor)

**Column B - Name:**

- Person name or vendor company name

**Column C - Type:**

- Dropdown: "Internal Staff", "Third-Party Vendor", "Contractor"

**Column D - Equipment Types Authorised:**

- What equipment they can maintain: "Servers", "Network", "UPS", "All"

**Column E - Verification Required:**

- Dropdown: "Yes - Badge/ID", "Yes - Escort", "No"

**Column F - Supervision Required:**

- Dropdown: "Yes - Always", "Yes - Sensitive Equipment", "No"

**Column G - Contract/Agreement:**

- Contract reference: "MSA-2025-001", "Employment contract"

**Column H - NDA in Place:**

- Dropdown: "Yes", "No", "N/A"

**Column I - Background Check:**

- Dropdown: "Yes", "No", "N/A"

**Column J - Last Verified:**

- Date authorisation last verified: "15.01.2026"

**Column K - Compliance Status:**

- Formula auto-calculates

**Column L - Notes:**

- Any additional context

**Time Required:** 30-45 minutes

### Sheet 5: Security During Maintenance

**Purpose:** Assess security controls during maintenance activities

**What to Document:**

**Data Protection:**

- Sensitive data protected during maintenance: Yes/Partial/No
- Equipment containing data kept on-premises: Yes/Partial/No
- Data erased before off-site maintenance: Yes/Partial/No/N/A
- Maintenance personnel data access restricted: Yes/No

**Access Controls:**

- Maintenance access time-limited: Yes/No
- Access logged (who, what, when, why): Yes/Partial/No
- Tools and equipment accounted for: Yes/No
- Physical inspection after maintenance: Yes/Partial/No

**Equipment Removal:**

- Removal authorisation required: Yes/No
- Chain of custody documented: Yes/Partial/No
- Equipment inspected on return: Yes/No
- Return logged in asset management: Yes/No

**Time Required:** 30-45 minutes

### Sheet 6: Remote Maintenance

**Purpose:** Audit remote maintenance controls

**What to Document (Per Remote Access Method or Vendor):**

**Column A - Access ID:**

- Unique identifier: "RM-001", "RM-002"

**Column B - Access Type:**

- Dropdown: "Vendor Remote Support", "Internal Remote Management", "Cloud Management Portal"

**Column C - Provider/System:**

- Who or what provides access: "Dell ProSupport", "TeamViewer", "Azure Portal"

**Column D - Equipment Types:**

- What equipment can be accessed: "Dell Servers", "Network Devices", "All"

**Column E - Authorised:**

- Dropdown: "Yes - Pre-approved", "Yes - On-demand", "No"

**Column F - Secure Connection:**

- Dropdown: "Yes - VPN", "Yes - Encrypted", "No"

**Column G - Session Logged:**

- Dropdown: "Yes - Automated", "Yes - Manual", "No"

**Column H - Session Monitored:**

- Dropdown: "Yes - Real-time", "Yes - Recorded", "No"

**Column I - Access Disabled When Not Required:**

- Dropdown: "Yes - Always", "Yes - Usually", "No"

**Column J - Last Access Review:**

- Date of last review: "15.01.2026"

**Column K - Compliance Status:**

- Formula auto-calculates

**Column L - Notes:**

- Any additional context

**Time Required:** 30-45 minutes

### Sheet 7: Summary Dashboard

**Purpose:** Automated compliance scoring

**What to Review (Auto-Calculated):**

- Overall Compliance Score
- Equipment Inventory Coverage
- Maintenance Programme Compliance
- Personnel Verification Status
- Security Controls Status
- Remote Maintenance Compliance
- Gap Summary

**Time Required:** 15-30 minutes for review

### Sheet 8: Evidence Register

**Purpose:** Document supporting evidence

**Common Evidence:**

1. Equipment inventory export from CMDB
2. Maintenance records (sample)
3. Vendor contracts (excerpts)
4. Remote access logs (sample)
5. Equipment removal authorisation forms
6. Maintenance checklists/procedures

**Time Required:** 2-3 hours for evidence collection

### Sheet 9: Approval Sign-Off

**Purpose:** Four-level approval workflow

---

## Evidence Collection

### What Evidence to Collect

**Equipment Inventory:**

- CMDB or asset inventory export
- Equipment criticality classification

**Maintenance Programme:**

- Maintenance schedule documentation
- Manufacturer recommendation documents
- Sample maintenance tickets/records

**Personnel & Vendors:**

- Authorised personnel list
- Vendor contracts with maintenance scope
- NDA and background check records

**Security During Maintenance:**

- Maintenance procedures showing data protection
- Access logging samples
- Equipment removal authorisation forms

**Remote Maintenance:**

- Remote access policies/procedures
- Session logs (sample)
- Access enable/disable procedures

---

## Common Pitfalls

### Pitfall 1: Incomplete Equipment Coverage

❌ **MISTAKE:** Only including IT equipment, missing facilities equipment (UPS, HVAC, security systems)

**How to Avoid:**
- Include ALL equipment supporting information processing
- Coordinate with Facilities Manager
- Include environmental control systems

### Pitfall 2: Missing Manufacturer Recommendations

❌ **MISTAKE:** Scheduling maintenance without reference to manufacturer requirements

**How to Avoid:**
- Document manufacturer recommendations per equipment type
- Compare scheduled frequency vs. recommended frequency
- Flag any gaps

### Pitfall 3: Vendor Contracts Not Reviewed

❌ **MISTAKE:** Assuming vendor contracts include appropriate security requirements

**How to Avoid:**
- Review vendor maintenance contracts
- Verify NDA and confidentiality clauses
- Check supervision requirements

### Pitfall 4: Remote Access Always Enabled

❌ **MISTAKE:** Leaving vendor remote access permanently enabled

**How to Avoid:**
- Verify remote access is disabled when not actively required
- Implement "just-in-time" access where possible
- Log access enable/disable actions

### Pitfall 5: Incomplete Maintenance Records

❌ **MISTAKE:** Maintenance performed but not documented

**How to Avoid:**
- Verify all maintenance is recorded
- Check records include required fields
- Audit sample of records for completeness

### Pitfall 6: No Supervision of Third Parties

❌ **MISTAKE:** Third-party technicians working unsupervised on sensitive equipment

**How to Avoid:**
- Document supervision requirements per equipment type
- Verify supervision actually occurs
- Log supervision in maintenance records

### Pitfall 7: Data Not Protected During Maintenance

❌ **MISTAKE:** Equipment sent for off-site maintenance with data intact

**How to Avoid:**
- Verify data erasure procedures for off-site maintenance
- Check if on-site maintenance is possible
- Document data protection measures

### Pitfall 8: No Return Inspection

❌ **MISTAKE:** Equipment returned from maintenance without inspection

**How to Avoid:**
- Verify inspection procedure exists
- Check for unauthorised modifications
- Update asset management on return

### Pitfall 9: Stale Personnel Lists

❌ **MISTAKE:** Authorised personnel list not updated when people leave

**How to Avoid:**
- Regular review of authorised personnel (quarterly minimum)
- Coordinate with HR for terminations
- Coordinate with Procurement for vendor changes

### Pitfall 10: No Overdue Tracking

❌ **MISTAKE:** Not tracking overdue preventive maintenance

**How to Avoid:**
- Implement overdue tracking in CMMS/ITSM
- Regular reporting on overdue items
- Escalation for critical equipment overdue

---

## Quality Checklist

### Sheet 2: Equipment Inventory

- [ ] ALL equipment types included (IT, facilities, security)
- [ ] Manufacturer maintenance requirements documented
- [ ] Criticality classification assigned
- [ ] Last maintenance dates recorded
- [ ] Next scheduled dates documented

### Sheet 3: Maintenance Programme

- [ ] Programme coverage verified
- [ ] Manufacturer recommendations followed
- [ ] Overdue items identified
- [ ] Record keeping assessed

### Sheet 4: Personnel & Vendors

- [ ] Internal personnel documented
- [ ] Third-party vendors documented
- [ ] Verification requirements documented
- [ ] Supervision requirements documented
- [ ] Contracts and NDAs verified

### Sheet 5: Security During Maintenance

- [ ] Data protection measures verified
- [ ] Access controls documented
- [ ] Equipment removal procedures verified
- [ ] Return inspection procedures verified

### Sheet 6: Remote Maintenance

- [ ] ALL remote access methods documented
- [ ] Secure connection requirements verified
- [ ] Session logging verified
- [ ] Access disable when not required verified

### Evidence Register

- [ ] At least 10 evidence items
- [ ] Evidence files exist at documented locations

---

## Review & Approval

### Four-Level Approval Workflow

**Level 1: Assessor**
- Complete assessment and evidence collection

**Level 2: IT Operations Manager**
- Technical review of maintenance assessment

**Level 3: CISO**
- Executive review and gap prioritisation

**Level 4: Compliance Officer**
- Final audit readiness certification

---

**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
