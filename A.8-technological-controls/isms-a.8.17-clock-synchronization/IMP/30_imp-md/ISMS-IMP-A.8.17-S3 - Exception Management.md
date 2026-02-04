**ISMS-IMP-A.8.17-S3 — Exception Management**
**Assessment Specification with User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.17: Clock Synchronization

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.17-S3 |
| **Version** | 1.0 |
| **Assessment Area** | Clock Synchronization Exception Management |
| **Related Policy** | ISMS-POL-A.8.17 (Clock Synchronization Policy - Section 3.3) |
| **Purpose** | Document and manage systems that cannot meet clock synchronization requirements, including air-gapped systems, legacy equipment, and special use cases |
| **Target Audience** | System Administrators, Network Engineers, Security Engineers, ISMS Officers, Risk Managers, Auditors |
| **Assessment Type** | Operational & Risk Management |
| **Review Cycle** | Quarterly or When Exceptions Change |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Original Date] | Initial technical specification for exception management | ISMS Officer |

### Document Structure

This document consists of two parts:

- **PART I: USER COMPLETION GUIDE** (Sections 1-8)
  - How to complete the Exception Management workbook
  - Prerequisites, workflow, field-by-field guidance
  - Evidence collection, quality checks, and approval process

- **PART II: TECHNICAL SPECIFICATION** (Sections 9-onwards)
  - Section A: Implementation Guidance (exception categories, risk assessment, compensating controls)
  - Section B: Assessment Workbook Specification (Excel workbook structure, formulas, validation rules)

---

# PART I: USER COMPLETION GUIDE

**Audience:** System Administrators, ISMS Officers, Risk Managers completing the Exception Management Assessment

---

# Assessment Overview

## Purpose & Scope

**Assessment Name:** ISMS-IMP-A.8.17-S3 - Exception Management Assessment

**What This Assessment Covers:**

This assessment documents and manages systems that cannot meet the standard clock synchronization requirements defined in ISMS-POL-A.8.17. Think of this as the formal process for tracking "legitimate exceptions" to the clock sync policy. This assessment answers critical questions:

- **Which systems cannot meet sync requirements?** (Air-gapped, legacy, vendor-locked)
- **Why can't they comply?** (Technical limitation, business requirement, vendor constraint)
- **What compensating controls are in place?** (Manual sync, local GPS, isolated logging)
- **Who approved the exception?** (Risk acceptance authority)
- **When does the exception expire?** (Time-limited, permanent, or until remediated)

**Key Principle:** "No system escapes accountability." Every system either meets clock synchronization requirements OR has a documented, approved exception with compensating controls. This assessment ensures no systems fall through the cracks.

Think of this as the "exception register" for time synchronization - similar to how a firewall rule exception requires approval and documentation, systems that cannot synchronize properly require formal exception management.

## What You'll Document

**Workbook Sheets You'll Complete:**

1. **Instructions** - Guidance for completing the exception management workbook

   - Navigation instructions
   - Sheet descriptions
   - Status legend and dropdown definitions

2. **Exception_Requests** - New exception request workflow

   - System identification and justification
   - Risk assessment and compensating controls
   - Approval workflow tracking
   - Request status (Pending, Approved, Rejected)

3. **Active_Exceptions** - Currently approved exceptions

   - Approved exception details
   - Expiration dates and renewal requirements
   - Compensating control verification
   - Responsible parties and review schedule

4. **Expired_Exceptions** - Historical expired exceptions

   - Archive of previously approved exceptions
   - Expiration reason (Remediated, Decommissioned, Renewed)
   - Lessons learned and pattern analysis

5. **Summary_Dashboard** - Exception metrics overview

   - Count of active vs. expired exceptions
   - Exception categories breakdown
   - Upcoming expirations requiring action
   - Compliance gap summary

## How This Relates to Other A.8.17 Assessments

| Assessment | Focus | Relationship to A.8.17-S3 |
|------------|-------|---------------------------|
| ISMS-IMP-A.8.17-S1 | Time Source Infrastructure | S1 documents WHAT sources exist; S3 tracks systems that CAN'T use those sources |
| ISMS-IMP-A.8.17-S2 | System Synchronization Verification | S2 identifies non-compliant systems; S3 manages their exceptions |
| **ISMS-IMP-A.8.17-S3** | **Exception Management** | **THIS assessment - documents WHY systems can't comply and HOW we mitigate** |
| ISMS-IMP-A.8.17-S4 | Compliance Dashboard | S4 aggregates S1-S3 findings into executive view |

**Assessment Flow:**
1. **A.8.17-S2 (PREVIOUS):** "System XYZ is not synchronized to approved time sources"
2. **A.8.17-S3 (THIS):** "System XYZ is an air-gapped OT system; approved exception with local GPS compensating control"
3. **A.8.17-S4 (NEXT):** "2 active exceptions out of 1,234 systems; 99.8% overall compliance"

You SHOULD complete S1 and S2 first - exception management (S3) handles systems identified as non-compliant in S2.

## Who Should Complete This Assessment

**Primary Stakeholders:**

1. **System Administrators** - Know which systems have synchronization challenges
2. **Network Engineers** - Understand technical constraints preventing NTP connectivity
3. **OT/ICS Engineers** - Manage air-gapped and legacy industrial systems
4. **ISMS Officer** - Conducts risk assessment and manages exception process
5. **Risk Manager** - Approves exceptions based on risk evaluation
6. **CISO** - Final approval authority for high-risk exceptions

**Required Skills:**

- **System Architecture Knowledge** - Understand why systems cannot meet requirements
- **Risk Assessment Basics** - Can evaluate impact of non-synchronized time
- **Compensating Control Design** - Know alternatives to standard NTP synchronization
- **Documentation Skills** - Can clearly articulate justifications and controls

**You DON'T need to be a risk management expert!** The assessment provides guidance on exception categories, standard compensating controls, and approval criteria.

## Time Commitment

- **Initial assessment (first time):** 4-8 hours
  - 1-2 hours: Review S2 findings to identify exception candidates
  - 1-2 hours: Document exception requests with justifications
  - 1-2 hours: Define compensating controls for each exception
  - 1 hour: Risk assessment and impact analysis
  - 1 hour: Obtain approvals from risk owner/CISO

- **Quarterly updates:** 1-2 hours
  - 30 minutes: Review expiring exceptions
  - 30 minutes: Verify compensating controls still effective
  - 30 minutes: Update status of pending requests
  - 30 minutes: Archive expired exceptions and document lessons learned

**Pro Tip:** Most exceptions are predictable categories (air-gapped OT, legacy systems, vendor appliances). Creating templates for common scenarios speeds future requests significantly.

## Expected Outputs

Upon completion, you will have:

1. **Exception request pipeline** - All pending requests documented with justifications
2. **Active exception register** - All approved exceptions with compensating controls
3. **Expiration tracking** - Clear visibility into upcoming exception renewals
4. **Historical archive** - Record of past exceptions for pattern analysis
5. **Compliance metrics** - Exception count, categories, and trends
6. **Risk acceptance documentation** - Formal approval records for audit
7. **Compensating control verification** - Evidence that alternatives are effective
8. **Audit-ready documentation** - Complete exception lifecycle tracking

**What This Looks Like for Audit:**

When an auditor asks: *"How do you handle systems that cannot meet clock synchronization requirements?"*

You hand them this assessment and say:

> "We have a formal exception management process. Currently, we have 3 active exceptions: 2 air-gapped OT systems with local GPS receivers, and 1 legacy vendor appliance pending replacement. Each has documented compensating controls and CISO approval. All exceptions are reviewed quarterly."

**Auditor reaction:** "This demonstrates mature risk management with appropriate oversight. Excellent."

---

# Prerequisites

## Required Information

Before starting, gather the following:

**Non-Compliant System Inventory:**

- [ ] **List of systems identified as non-compliant** from S2 assessment
- [ ] **System ownership information** (who is responsible for each system)
- [ ] **System criticality classification** (critical, high, medium, low)

**Technical Constraint Documentation:**

- [ ] **Reason for non-compliance** for each system (air-gapped, legacy, vendor-locked)
- [ ] **Technical assessment** of why standard NTP cannot be implemented
- [ ] **Vendor documentation** (if vendor limitation prevents compliance)

**Compensating Control Options:**

- [ ] **Available alternatives** (local GPS, manual sync, isolated time source)
- [ ] **Implementation feasibility** for each compensating control
- [ ] **Effectiveness assessment** of proposed alternatives

**Approval Information:**

- [ ] **Risk owner identification** for each system/business area
- [ ] **CISO availability** for exception approvals
- [ ] **Approval criteria** from ISMS-POL-A.8.17 Section 3.3

## Required Tools

**For Documentation:**

- Access to S2 assessment results (non-compliant system list)
- Asset management system (CMDB) for system details
- This exception management workbook

**For Risk Assessment:**

- Organization's risk assessment methodology
- Business impact classification criteria
- Compensating control effectiveness evaluation

**For Approvals:**

- Access to risk owner for system-level exceptions
- Access to CISO for high-risk exceptions
- Email or workflow system for formal approvals

## Policy Requirements to Review

Before starting, familiarize yourself with key policy requirements from **ISMS-POL-A.8.17**:

**From Section 3.3 (Exception Management):**

- **REQ-817-017**: Formal exception process required for non-compliant systems
- **REQ-817-018**: All exceptions require documented justification
- **REQ-817-019**: Compensating controls required for all exceptions
- **REQ-817-020**: Risk acceptance required from appropriate authority (Risk Owner or CISO)
- **REQ-817-021**: Exception review minimum quarterly
- **REQ-817-022**: Maximum exception duration 12 months (must be renewed)
- **REQ-817-023**: Permanent exceptions require CISO and Executive approval

You'll be verifying compliance with these requirements in the assessment.

---

# Assessment Workflow

## Recommended Completion Order

**STEP 1:** Review S2 findings for exception candidates

- Export list of non-compliant systems from S2 assessment
- Categorize by reason for non-compliance
- Prioritize by system criticality

**STEP 2:** Research technical constraints

- For each system, document why standard NTP cannot be implemented
- Gather vendor documentation if applicable
- Confirm air-gap requirements if claimed

**STEP 3:** Design compensating controls

- For each exception candidate, identify viable alternatives
- Assess effectiveness of each compensating control
- Document implementation requirements

**STEP 4:** Complete Exception_Requests sheet

- Fill one row per exception request
- Document justification, risk assessment, compensating controls
- Mark required fields as mandatory

**STEP 5:** Obtain approvals

- Route requests to risk owner for initial approval
- Escalate to CISO for high-risk or permanent exceptions
- Document approval in workbook

**STEP 6:** Move approved exceptions to Active_Exceptions

- Transfer approved requests with approval details
- Set expiration dates (maximum 12 months)
- Assign responsible party for ongoing verification

**STEP 7:** Review expired exceptions

- Check Active_Exceptions for upcoming expirations
- Initiate renewal process or confirm remediation
- Archive expired exceptions in Expired_Exceptions sheet

**STEP 8:** Update Summary_Dashboard

- Verify metrics are accurate
- Document trends and patterns
- Flag upcoming expirations requiring action

**STEP 9:** Collect evidence

- Save approval emails/records
- Document compensating control verification
- Screenshot monitoring dashboards

**STEP 10:** Internal review and approval

- Peer review for completeness
- ISMS Officer sign-off on exception register

## Data Sources

**Where to find information for this assessment:**

**Non-Compliant Systems:**

- S2 assessment results (primary source)
- Monitoring system alerts for sync failures
- Security operations incident reports

**System Details:**

- Asset management system (CMDB)
- Network diagrams
- System documentation

**Approval Records:**

- Email archives
- Workflow/ticketing system
- ISMS document repository

---

# Sheet-by-Sheet Completion Guidance

## Sheet: Instructions

**Purpose:** Provide workbook usage instructions, navigation guidance, and status legends.

**THIS SHEET IS PRE-POPULATED** - No user input required.

**Content Includes:**

- Purpose statement for exception management
- Sheet descriptions and navigation
- Status dropdown definitions
- Approval workflow guidance
- Link to ISMS-POL-A.8.17 Section 3.3

---

## Sheet: Exception_Requests (New Exception Request Workflow)

**Purpose:** Document pending exception requests requiring approval.

**Column-by-Column Guidance:**

| Column | Field Name | Required? | Guidance | Where to Find This |
|--------|------------|-----------|----------|-------------------|
| A | **Request ID [*]** | REQUIRED | Unique identifier for tracking | Auto-generate: EXC-YYYYMMDD-NNN |
| | | | Example: `EXC-20260116-001`, `EXC-20260116-002` | Sequential numbering |
| B | **System Name [*]** | REQUIRED | Hostname or system identifier | S2 assessment, CMDB |
| | | | Example: `ot-plc-line1`, `legacy-erp-01`, `vendor-appliance-dc1` | Asset inventory |
| C | **System Type [*]** | REQUIRED | Select from dropdown | Identify based on system |
| | | | **Dropdown options:** OT/ICS System, Legacy System, Vendor Appliance, Air-Gapped System, Embedded Device, Test/Lab System, Other | |
| D | **Business Owner [*]** | REQUIRED | Person accountable for the system | CMDB, organizational chart |
| | | | Example: `Jane Smith (OT Manager)`, `IT Operations` | |
| E | **Exception Category [*]** | REQUIRED | Select from dropdown | Based on technical constraint |
| | | | **Dropdown options:** Air-Gapped (No Network), Legacy (No NTP Support), Vendor Restriction, Regulatory Requirement, Business Requirement, Other | |
| F | **Justification [*]** | REQUIRED | Detailed explanation why exception is needed | Technical assessment |
| | | | Example: `Air-gapped OT system controlling manufacturing line. Network connectivity prohibited by safety standards.` | Documentation review |
| | | | **Must be specific** - not just "cannot comply" | |
| G | **Risk Assessment [*]** | REQUIRED | Impact of non-synchronized time | Risk analysis |
| | | | Example: `Low - isolated system, logs not correlated with IT systems. Local timestamps sufficient for operational troubleshooting.` | |
| H | **Compensating Controls [*]** | REQUIRED | Alternative measures to mitigate risk | Control design |
| | | | Example: `Local GPS receiver for independent time source. Manual clock verification monthly.` | |
| | | | **Must address the risk identified** | |
| I | **Requested Duration [*]** | REQUIRED | How long exception is needed | Business requirement |
| | | | **Options:** 3 months, 6 months, 12 months, Permanent | |
| | | | **Note:** Permanent requires CISO + Executive approval | |
| J | **Request Date [*]** | REQUIRED | Date request submitted | Today's date |
| | | | **Format:** YYYY-MM-DD | Example: `2026-01-16` |
| K | **Requested By [*]** | REQUIRED | Person submitting request | Your name |
| L | **Risk Owner Approval** | Optional | Risk owner decision | Approval workflow |
| | | | **Dropdown:** Pending, Approved, Rejected | |
| M | **Risk Owner Date** | Optional | Date of risk owner decision | Approval date |
| N | **CISO Approval** | Optional | CISO decision (if required) | Approval workflow |
| | | | **Required for:** High-risk, Permanent, or Executive-escalated exceptions | |
| | | | **Dropdown:** Not Required, Pending, Approved, Rejected | |
| O | **CISO Date** | Optional | Date of CISO decision | Approval date |
| P | **Request Status [*]** | REQUIRED | Current status of request | Update as workflow progresses |
| | | | **Dropdown:** Draft, Submitted, Risk Owner Review, CISO Review, Approved, Rejected, Withdrawn | |
| Q | **Notes** | Optional | Additional context | Free text |

**How Many Rows to Complete:**

- **One row per exception request**
- Typical organizations: 1-10 pending requests
- High: >10 requests suggests systemic compliance issues

**Example Completed Rows:**

| Request ID | System Name | System Type | Business Owner | Category | Justification | Risk Assessment | Compensating Controls | Duration | Request Date | Requested By | RO Approval | RO Date | CISO Approval | CISO Date | Status | Notes |
|------------|-------------|-------------|----------------|----------|---------------|-----------------|----------------------|----------|--------------|--------------|-------------|---------|---------------|-----------|--------|-------|
| EXC-20260116-001 | ot-plc-line1 | OT/ICS System | Jane Smith (OT Manager) | Air-Gapped (No Network) | Air-gapped PLC controlling manufacturing line. Network connectivity prohibited by IEC 62443 safety requirements. | Low - Isolated OT system. Logs not correlated with IT. Local timestamps sufficient for safety analysis. | Local GPS receiver installed. Manual clock verification monthly with documented results. | 12 months | 2026-01-16 | John Doe | Pending | | Not Required | | Submitted | High-priority for Q1 approval |
| EXC-20260116-002 | legacy-erp-01 | Legacy System | Bob Wilson (Finance) | Legacy (No NTP Support) | Legacy ERP system (vendor XYZ v3.2, 2008). No NTP client support. Vendor EOL, replacement planned Q3 2026. | Medium - Financial transaction timestamps used in reports. Manual reconciliation required for audit. | Manual time sync quarterly using admin console. Replacement project funded and scheduled. | 12 months | 2026-01-16 | John Doe | Pending | | Not Required | | Submitted | Tied to ERP replacement project |

**Policy Compliance Check:**

- [ ] All requests have unique Request ID?
- [ ] All requests have documented justification (not generic)?
- [ ] All requests have risk assessment?
- [ ] All requests have compensating controls that address the risk?
- [ ] Permanent requests flagged for CISO + Executive approval?
- [ ] Request status accurately reflects workflow position?

**Common Mistakes to Avoid:**

- **Generic justification** - "System cannot comply" is insufficient; explain WHY
- **Missing compensating controls** - Every exception needs mitigation
- **Skipping risk assessment** - Must document impact of non-compliance
- **Permanent without escalation** - Permanent exceptions require CISO + Executive
- **Stale requests** - Review and update pending requests monthly

---

## Sheet: Active_Exceptions (Currently Approved Exceptions)

**Purpose:** Document all currently approved and active exceptions.

**Column-by-Column Guidance:**

| Column | Field Name | Required? | Guidance | Where to Find This |
|--------|------------|-----------|----------|-------------------|
| A | **Exception ID [*]** | REQUIRED | Unique identifier (from approved request) | Exception_Requests sheet |
| | | | Example: `EXC-20260116-001` | Same as Request ID |
| B | **System Name [*]** | REQUIRED | Hostname or system identifier | Exception_Requests sheet |
| C | **System Type [*]** | REQUIRED | System category | Exception_Requests sheet |
| D | **Business Owner [*]** | REQUIRED | Person accountable | Exception_Requests sheet |
| E | **Exception Category [*]** | REQUIRED | Reason category | Exception_Requests sheet |
| F | **Approved Justification [*]** | REQUIRED | Final approved justification | May be modified during approval |
| G | **Compensating Controls [*]** | REQUIRED | Approved compensating controls | May be modified during approval |
| H | **Approval Date [*]** | REQUIRED | Date exception was approved | Approval workflow |
| I | **Approved By [*]** | REQUIRED | Approving authority | Risk Owner and/or CISO |
| | | | Example: `Risk Owner: Jane Smith; CISO: Bob Johnson` | |
| J | **Expiration Date [*]** | REQUIRED | Date exception expires | Approval date + duration |
| | | | **Maximum:** 12 months from approval (or Permanent if approved) | |
| K | **Review Schedule [*]** | REQUIRED | How often to verify compensating controls | Based on risk level |
| | | | **Options:** Monthly, Quarterly, Semi-annually | |
| L | **Last Review Date** | Optional | Date of last compensating control review | Review records |
| M | **Review Status** | Optional | Status of last review | Review findings |
| | | | **Dropdown:** Current, Overdue, Review Scheduled | |
| N | **Responsible Party [*]** | REQUIRED | Person responsible for ongoing compliance | System owner or delegate |
| O | **Renewal Status** | Optional | Status of renewal process (if expiring soon) | Renewal workflow |
| | | | **Dropdown:** Not Due, In Progress, Renewed, Expiring Soon | |
| P | **Notes** | Optional | Additional context | Free text |

**How Many Rows to Complete:**

- **One row per active exception**
- Move from Exception_Requests when approved
- Remove when expired (move to Expired_Exceptions)

**Example Completed Rows:**

| Exception ID | System Name | System Type | Business Owner | Category | Justification | Compensating Controls | Approval Date | Approved By | Expiration Date | Review Schedule | Last Review | Review Status | Responsible | Renewal Status | Notes |
|--------------|-------------|-------------|----------------|----------|---------------|----------------------|---------------|-------------|-----------------|-----------------|-------------|---------------|-------------|----------------|-------|
| EXC-20251020-003 | ot-scada-hmi | OT/ICS System | Jane Smith (OT Manager) | Air-Gapped (No Network) | Air-gapped SCADA HMI in manufacturing control room. No network connectivity per safety requirements. | Local GPS receiver (Meinberg M300) provides Stratum 1 time. Monthly manual verification documented. | 2025-10-20 | Risk Owner: Jane Smith; CISO: Bob Johnson | 2026-10-20 | Quarterly | 2026-01-15 | Current | Mike Brown (OT Engineer) | Not Due | GPS receiver maintenance scheduled Q2 |
| EXC-20251115-007 | vendor-fw-dc1 | Vendor Appliance | IT Operations | Vendor Restriction | Vendor firewall appliance (Vendor XYZ) does not expose NTP configuration. Vendor confirmed no plans to add feature. | Appliance syncs internally to vendor cloud service. Vendor SLA guarantees <1 second accuracy. Monitoring configured for drift alerts. | 2025-11-15 | Risk Owner: Tom Davis | 2026-11-15 | Semi-annually | 2025-11-15 | Current | Susan Lee (Network Ops) | Not Due | Vendor escalation ticket #12345 for feature request |

**Policy Compliance Check:**

- [ ] All active exceptions have approval documentation?
- [ ] All exceptions have expiration date within 12 months (unless Permanent)?
- [ ] All exceptions have compensating controls documented?
- [ ] Review schedule appropriate for risk level?
- [ ] Last review within review schedule period?
- [ ] Expiring exceptions have renewal status tracked?

**Common Mistakes to Avoid:**

- **Missing approval documentation** - Every exception needs formal approval record
- **Expired exceptions not archived** - Move to Expired_Exceptions when expired
- **Overdue reviews not flagged** - Review Status should show "Overdue" if past due
- **No responsible party** - Someone must own ongoing compliance
- **Permanent exceptions without proper approval** - Requires CISO + Executive

---

## Sheet: Expired_Exceptions (Historical Expired Exceptions)

**Purpose:** Archive previously approved exceptions for historical tracking and pattern analysis.

**Column-by-Column Guidance:**

| Column | Field Name | Required? | Guidance | Where to Find This |
|--------|------------|-----------|----------|-------------------|
| A | **Exception ID [*]** | REQUIRED | Original exception identifier | Active_Exceptions sheet |
| B | **System Name [*]** | REQUIRED | Hostname or system identifier | Active_Exceptions sheet |
| C | **System Type [*]** | REQUIRED | System category | Active_Exceptions sheet |
| D | **Exception Category [*]** | REQUIRED | Reason category | Active_Exceptions sheet |
| E | **Original Approval Date [*]** | REQUIRED | Date originally approved | Active_Exceptions sheet |
| F | **Expiration Date [*]** | REQUIRED | Date exception expired | Active_Exceptions sheet |
| G | **Expiration Reason [*]** | REQUIRED | Why exception ended | Determine from outcome |
| | | | **Dropdown:** Remediated (Now Compliant), Renewed (New Exception), System Decommissioned, Rejected on Renewal, Risk Accepted Permanently | |
| H | **Final Compensating Controls** | Optional | What controls were in place at expiration | Active_Exceptions sheet |
| I | **Successor Exception ID** | Optional | New exception ID if renewed | New exception request |
| | | | Leave blank if not renewed | |
| J | **Lessons Learned** | Optional | Insights for future exception management | Post-expiration review |
| | | | Example: `Renewal process started too late. Recommend 60-day advance notice for future.` | |
| K | **Archived By [*]** | REQUIRED | Person who archived the exception | Your name |
| L | **Archive Date [*]** | REQUIRED | Date moved to archive | Today's date |
| M | **Notes** | Optional | Additional context | Free text |

**How Many Rows to Complete:**

- **One row per expired exception**
- Move from Active_Exceptions when expired
- Retain for minimum 3 years for audit trail

**Example Completed Rows:**

| Exception ID | System Name | System Type | Category | Original Approval | Expiration Date | Expiration Reason | Final Controls | Successor | Lessons Learned | Archived By | Archive Date | Notes |
|--------------|-------------|-------------|----------|-------------------|-----------------|-------------------|----------------|-----------|-----------------|-------------|--------------|-------|
| EXC-20250115-001 | legacy-app-01 | Legacy System | Legacy (No NTP Support) | 2025-01-15 | 2026-01-15 | Remediated (Now Compliant) | Manual quarterly sync | N/A | Application upgraded to v5.0 with NTP support. 6-month remediation project successful. | John Doe | 2026-01-16 | Closed successfully |
| EXC-20250301-002 | test-lab-vm-01 | Test/Lab System | Business Requirement | 2025-03-01 | 2026-01-01 | System Decommissioned | Isolated network time source | N/A | Lab environment rebuilt. Old VMs decommissioned. | Jane Smith | 2026-01-02 | Part of lab refresh project |

**Policy Compliance Check:**

- [ ] All expired exceptions properly archived?
- [ ] Expiration reason documented for each?
- [ ] Successor exception linked if renewed?
- [ ] Lessons learned captured for significant exceptions?

---

## Sheet: Summary_Dashboard (Exception Metrics Overview)

**Purpose:** Provide management overview of exception status and trends.

**THIS SHEET HAS BOTH AUTO-CALCULATED AND MANUAL SECTIONS**

**Section 1: Exception Counts (Auto-Calculated)**

| Metric | Formula | Description |
|--------|---------|-------------|
| **Total Active Exceptions** | =COUNTA(Active_Exceptions!A2:A100) | Count of currently active exceptions |
| **Pending Requests** | =COUNTIF(Exception_Requests!P2:P100,"Submitted")+COUNTIF(Exception_Requests!P2:P100,"Risk Owner Review")+COUNTIF(Exception_Requests!P2:P100,"CISO Review") | Requests awaiting approval |
| **Expired This Quarter** | =COUNTIFS(...) | Exceptions expired in current quarter |
| **Expiring Next 30 Days** | =COUNTIFS(Active_Exceptions!J2:J100,"<="&TODAY()+30,Active_Exceptions!J2:J100,">="&TODAY()) | Upcoming expirations requiring action |
| **Expiring Next 90 Days** | =COUNTIFS(Active_Exceptions!J2:J100,"<="&TODAY()+90,Active_Exceptions!J2:J100,">="&TODAY()) | Exceptions to review for renewal |

**Section 2: Exception Categories Breakdown (Auto-Calculated)**

| Category | Count | Percentage |
|----------|-------|------------|
| Air-Gapped (No Network) | =COUNTIF(Active_Exceptions!E2:E100,"Air-Gapped (No Network)") | [%] |
| Legacy (No NTP Support) | =COUNTIF(Active_Exceptions!E2:E100,"Legacy (No NTP Support)") | [%] |
| Vendor Restriction | =COUNTIF(Active_Exceptions!E2:E100,"Vendor Restriction") | [%] |
| Regulatory Requirement | =COUNTIF(Active_Exceptions!E2:E100,"Regulatory Requirement") | [%] |
| Business Requirement | =COUNTIF(Active_Exceptions!E2:E100,"Business Requirement") | [%] |
| Other | =COUNTIF(Active_Exceptions!E2:E100,"Other") | [%] |

**Section 3: Exception System Types Breakdown (Auto-Calculated)**

| System Type | Count | Percentage |
|-------------|-------|------------|
| OT/ICS System | =COUNTIF(Active_Exceptions!C2:C100,"OT/ICS System") | [%] |
| Legacy System | =COUNTIF(Active_Exceptions!C2:C100,"Legacy System") | [%] |
| Vendor Appliance | =COUNTIF(Active_Exceptions!C2:C100,"Vendor Appliance") | [%] |
| Air-Gapped System | =COUNTIF(Active_Exceptions!C2:C100,"Air-Gapped System") | [%] |
| Embedded Device | =COUNTIF(Active_Exceptions!C2:C100,"Embedded Device") | [%] |
| Test/Lab System | =COUNTIF(Active_Exceptions!C2:C100,"Test/Lab System") | [%] |
| Other | =COUNTIF(Active_Exceptions!C2:C100,"Other") | [%] |

**Section 4: Review Status Summary (Auto-Calculated)**

| Review Status | Count | Action Required |
|---------------|-------|-----------------|
| Current | =COUNTIF(Active_Exceptions!M2:M100,"Current") | None |
| Overdue | =COUNTIF(Active_Exceptions!M2:M100,"Overdue") | Immediate review required |
| Review Scheduled | =COUNTIF(Active_Exceptions!M2:M100,"Review Scheduled") | Per schedule |

**Section 5: Upcoming Expirations (Auto-Calculated List)**

Lists active exceptions expiring in next 90 days:

| Exception ID | System Name | Expiration Date | Days Remaining | Renewal Status |
|--------------|-------------|-----------------|----------------|----------------|
| [Auto-filtered from Active_Exceptions] | | | =Expiration - TODAY() | |

**Section 6: Trend Analysis (Manual Entry)**

| Quarter | Active Exceptions | New Requests | Approved | Rejected | Remediated |
|---------|-------------------|--------------|----------|----------|------------|
| Q1 2026 | [Current count] | [Count new] | [Count approved] | [Count rejected] | [Count remediated] |
| Q4 2025 | | | | | |
| Q3 2025 | | | | | |

**Section 7: Key Observations (Manual Entry)**

Document notable patterns, trends, or concerns:

- Trend in exception categories
- Departments with most exceptions
- Remediation progress
- Risk areas requiring attention

---

# Evidence Collection

## Required Evidence Types

**Approval Evidence:**

- [ ] **Approval emails** - Email trails showing risk owner and/or CISO approval
- [ ] **Workflow records** - Ticketing system approval records
- [ ] **Meeting minutes** - If approved in risk committee

**Compensating Control Evidence:**

- [ ] **Implementation documentation** - Proof controls are in place
- [ ] **Verification records** - Results of compensating control reviews
- [ ] **Monitoring screenshots** - If compensating control includes monitoring

**Risk Assessment Evidence:**

- [ ] **Risk assessment document** - Formal risk analysis for high-risk exceptions
- [ ] **Impact analysis** - Documentation of potential impact if time unsynchronized

**System Documentation:**

- [ ] **Vendor documentation** - Confirming vendor limitations (if applicable)
- [ ] **Technical assessment** - Confirming why NTP cannot be implemented
- [ ] **Network diagrams** - Showing air-gap or isolation (if applicable)

## Evidence Naming Convention

```
Evidence Type: EXC-[EXCEPTION_ID]-[EVIDENCE_TYPE]-[DATE].ext

Examples:
EXC-20260116-001-Approval-Email-20260120.pdf     (Approval documentation)
EXC-20260116-001-GPS-Install-Photos-20260125.pdf (Compensating control evidence)
EXC-20260116-001-Vendor-Doc-NoNTP-20260116.pdf   (Vendor limitation)
EXC-20260116-001-Risk-Assessment-20260118.pdf    (Risk analysis)
```

## Where to Store Evidence

**Options:**
1. **ISMS document repository** - Centralized ISMS file storage
2. **Network share** - `\\fileserver\ISMS\Evidence\A.8.17\S3\Exceptions\`
3. **Document management** - SharePoint, Confluence, etc.
4. **Reference in workbook** - Put file paths in Notes columns

**Recommendation:** Store centrally with exception ID as folder name, reference paths in workbook.

---

# Common Pitfalls & How to Avoid Them

## Generic Justifications

**MISTAKE:**
Writing "System cannot meet NTP requirements" as justification.

**WHY IT'S WRONG:**
Auditors and approvers need to understand WHY the system cannot comply to assess risk.

**HOW TO AVOID:**
Be specific: "Air-gapped OT system per IEC 62443. Network connectivity would create safety risk."

## Missing Compensating Controls

**MISTAKE:**
Documenting exception without any compensating controls.

**WHY IT'S WRONG:**
Policy requires compensating controls for all exceptions. No controls = no approval.

**HOW TO AVOID:**
Every exception needs at least one compensating control. Examples:
- Local GPS receiver
- Manual time synchronization with documented procedure
- Isolated time source within air-gapped network
- Vendor-managed time synchronization

## Expired Exceptions Not Tracked

**MISTAKE:**
Letting exceptions expire without renewal process or archiving.

**WHY IT'S WRONG:**
Creates compliance gap - system neither compliant nor has valid exception.

**HOW TO AVOID:**
- Set calendar reminders 60 days before expiration
- Review Summary_Dashboard weekly for upcoming expirations
- Initiate renewal process early

## Permanent Exceptions Without Proper Approval

**MISTAKE:**
Approving permanent exceptions with only risk owner sign-off.

**WHY IT'S WRONG:**
Policy requires CISO AND Executive approval for permanent exceptions.

**HOW TO AVOID:**
- Route permanent requests through full approval chain
- Document Executive approval explicitly
- Consider if "permanent" is truly necessary vs. annual renewal

## Compensating Controls Not Verified

**MISTAKE:**
Documenting compensating controls but never verifying they work.

**WHY IT'S WRONG:**
Unverified controls may not actually mitigate risk.

**HOW TO AVOID:**
- Set review schedule appropriate to risk level
- Actually verify controls during review (not just check the box)
- Document verification results

---

# Quality Checklist

Before submitting for approval, verify:

**Data Completeness:**

- [ ] All required fields completed in Exception_Requests
- [ ] All approved exceptions moved to Active_Exceptions
- [ ] All expired exceptions moved to Expired_Exceptions
- [ ] Summary_Dashboard reflects current state

**Data Accuracy:**

- [ ] Exception IDs are unique and consistent
- [ ] Dates are in YYYY-MM-DD format
- [ ] Dropdown selections used (not free text)
- [ ] Expiration dates calculated correctly (approval + duration)

**Policy Compliance:**

- [ ] All exceptions have documented justification?
- [ ] All exceptions have compensating controls?
- [ ] All exceptions have appropriate approval?
- [ ] Permanent exceptions have CISO + Executive approval?
- [ ] No exceptions exceed 12-month duration without renewal?
- [ ] Review schedules appropriate for risk level?

**Approval Documentation:**

- [ ] Approval emails/records collected for all active exceptions?
- [ ] Approver names documented in Active_Exceptions?
- [ ] Approval dates documented?

**Evidence:**

- [ ] Compensating control evidence collected?
- [ ] Vendor documentation collected (if applicable)?
- [ ] Risk assessments documented for high-risk exceptions?

**Professional Presentation:**

- [ ] No spelling errors or typos
- [ ] Consistent formatting throughout
- [ ] Notes provide useful context (not just "N/A")

---

# Review & Approval Process

## Internal Review (Before Submission)

**Step 1: Self-Review**

- Use Quality Checklist above
- Verify exception counts match between sheets
- Confirm all pending requests have current status

**Step 2: Peer Review** (Recommended)

- Have another team member review for completeness
- Focus on: Are justifications clear? Are compensating controls adequate?

**Step 3: ISMS Officer Review** (Required)

- ISMS Officer checks policy compliance
- Verifies: All exceptions approved? Controls documented? Reviews current?

## Formal Approval Workflow

**For Individual Exceptions:**

1. **Risk Owner** - Approves system-level exceptions (standard risk)
2. **CISO** - Approves high-risk or permanent exceptions
3. **Executive Management** - Co-approves permanent exceptions

**For Exception Register (This Assessment):**

**Level 1: ISMS Officer**

- **Reviews:** Completeness, policy compliance, evidence collection
- **Approves:** Assessment ready for management review

**Level 2: CISO**

- **Reviews:** Overall exception posture, risk acceptance appropriateness
- **Approves:** Exception management process is effective

## Approval Criteria

**Assessment will be APPROVED if:**

- All active exceptions have documented approvals
- All exceptions have compensating controls
- Review schedules are followed (no overdue reviews)
- Expiring exceptions have renewal plan
- Evidence is collected and accessible

**Assessment will be REJECTED if:**

- Active exceptions missing approval documentation
- Exceptions without compensating controls
- Multiple overdue reviews without remediation plan
- No evidence collected
- Permanent exceptions without proper approval chain

## Post-Approval

**After approval:**
1. **File final version** in ISMS document repository
2. **Update ISMS tracking** (S3 assessment completed date)
3. **Schedule next quarterly assessment** (set calendar reminder)
4. **Set expiration reminders** (60 days before each exception expires)
5. **Provide to S4 assessment** (S4 needs S3 results for compliance dashboard)
6. **Provide to auditors** when requested

**Quarterly Updates:**

- Review all active exceptions for continued validity
- Verify compensating controls still effective
- Process any pending requests
- Archive expired exceptions
- Update Summary_Dashboard metrics
- Document any patterns or trends

---

**END OF PART I: USER COMPLETION GUIDE**

---

# PART II: TECHNICAL SPECIFICATION

**Audience:** Workbook developers, Python script maintainers, technical implementers

**Note:** This section provides technical specifications for exception management workbook structure. Users completing the assessment should refer to Part I above.

---

# Implementation Requirement Mapping

**This section maps policy requirements (REQ-817-xxx codes) to ISMS-POL-A.8.17 sections for traceability.**

## S3 Requirements (REQ-817-017 through REQ-817-023)

| Requirement ID | Policy Section | Requirement Summary |
|---------------|----------------|---------------------|
| REQ-817-017 | Section 3.3 | Formal exception process required for non-compliant systems |
| REQ-817-018 | Section 3.3 | All exceptions require documented justification |
| REQ-817-019 | Section 3.3 | Compensating controls required for all exceptions |
| REQ-817-020 | Section 3.3 | Risk acceptance required from appropriate authority |
| REQ-817-021 | Section 3.3 | Exception review minimum quarterly |
| REQ-817-022 | Section 3.3 | Maximum exception duration 12 months |
| REQ-817-023 | Section 3.3 | Permanent exceptions require CISO and Executive approval |

---

# SECTION A: Implementation Guidance

## Introduction

This section provides technical guidance for managing clock synchronization exceptions, including categorization, risk assessment, and compensating control design.

**Purpose:** Enable ISMS Officers and System Administrators to implement a robust exception management process that maintains accountability while accommodating legitimate technical constraints.

**Scope:** Systems that cannot meet standard NTP synchronization requirements due to air-gap, legacy, vendor, or business constraints.

**Related Documents:**

- ISMS-POL-A.8.17 (Clock Synchronization Policy)
- ISMS-IMP-A.8.17-S1 (Time Source Configuration)
- ISMS-IMP-A.8.17-S2 (Synchronization Verification)
- ISMS-IMP-A.8.17-S4 (Compliance Dashboard)

---

## Exception Categories

### Air-Gapped Systems (No Network)

**Definition:** Systems intentionally isolated from network connectivity for security or safety reasons.

**Common Examples:**

- OT/ICS systems (PLCs, SCADA, HMIs) in manufacturing
- High-security classified systems
- Research systems with sensitive data
- Safety-critical systems per IEC 62443

**Typical Justification:**

> "System is air-gapped per [safety standard/security requirement]. Network connectivity would violate [standard] and create [safety/security] risk."

**Recommended Compensating Controls:**

1. **Local GPS Receiver** - Install dedicated GPS time receiver within air-gapped network
   - Stratum 0/1 accuracy
   - Independent of external network
   - Example: Meinberg, EndRun, Symmetricom appliances

2. **Manual Time Synchronization** - Periodic manual clock setting
   - Monthly or quarterly depending on drift tolerance
   - Documented procedure with verification
   - Audit trail of sync events

3. **Local Atomic Clock** - For highest accuracy requirements
   - Expensive but provides ultimate independence
   - Typically only for critical infrastructure

---

### Legacy Systems (No NTP Support)

**Definition:** Older systems that do not support NTP protocol or configuration.

**Common Examples:**

- Legacy ERP systems (pre-2010)
- Old mainframe applications
- Embedded systems with fixed firmware
- Proprietary industrial controllers

**Typical Justification:**

> "System is [Vendor] [Product] version [X.Y] from [Year]. Vendor confirmed no NTP support in this version. System is scheduled for replacement in [Quarter/Year]."

**Recommended Compensating Controls:**

1. **Manual Time Synchronization** - Documented manual sync procedure
   - Frequency based on system drift rate
   - Admin console or hardware clock access
   - Verification after each sync

2. **Planned Remediation** - Document replacement timeline
   - Link to project/budget approval
   - Track progress toward compliant replacement
   - Exception tied to remediation completion

3. **Log Correlation Adjustment** - If logs must be correlated
   - Document time offset from reference
   - Apply offset in SIEM during correlation
   - Accept reduced accuracy for forensics

---

### Vendor Restrictions

**Definition:** Systems where vendor configuration does not permit NTP customization.

**Common Examples:**

- SaaS appliances with locked-down OS
- Security appliances with vendor-managed time
- Cloud services with provider time sync
- Proprietary network devices

**Typical Justification:**

> "System is [Vendor] [Product]. Vendor does not expose NTP configuration per support case #[Number]. System uses vendor-managed time synchronization to [Vendor Cloud Service]."

**Recommended Compensating Controls:**

1. **Vendor-Managed Sync** - Accept vendor time source
   - Document vendor SLA for time accuracy
   - Monitor for drift using external validation
   - Retain vendor support case as evidence

2. **Drift Monitoring** - External validation of vendor sync
   - Compare system time against reference
   - Alert if drift exceeds threshold
   - Document acceptable variance

3. **Vendor Escalation** - Request feature enhancement
   - Document escalation request
   - Track vendor roadmap for NTP support
   - Re-evaluate at exception renewal

---

### Regulatory Requirements

**Definition:** Systems where regulations require specific time source or prohibit standard NTP.

**Common Examples:**

- Financial trading systems (MiFID II timestamp requirements)
- Healthcare systems (specific time source requirements)
- Government systems (certified time sources only)

**Typical Justification:**

> "System must use [Specific Time Source] per [Regulation] Article [X]. Standard organizational NTP infrastructure does not meet regulatory requirements for [accuracy/auditability/certification]."

**Recommended Compensating Controls:**

1. **Regulatory-Compliant Time Source** - Use required time source
   - Document regulatory requirement
   - Implement compliant time infrastructure
   - May require dedicated NTP path

2. **Audit Trail** - Enhanced logging for regulated systems
   - Capture time source information in logs
   - Retain for regulatory retention period
   - Support audit inquiries

---

### Business Requirements

**Definition:** Systems where business need prevents standard NTP implementation.

**Common Examples:**

- Test/lab environments requiring time manipulation
- Development systems with clock testing requirements
- Demonstration systems with specific time scenarios

**Typical Justification:**

> "System is [purpose] requiring [time manipulation/specific time/isolated operation]. Standard NTP would [interfere with testing/break functionality]."

**Recommended Compensating Controls:**

1. **Isolated Time Management** - Controlled time within environment
   - Document purpose and scope
   - Limit exception to specific systems
   - Prevent cross-contamination with production

2. **Periodic Resync** - Reset to accurate time periodically
   - After testing cycles
   - Before production deployment
   - Documented procedure

---

## Risk Assessment Guidance

### Risk Factors to Consider

**Impact of Unsynchronized Time:**

1. **Log Correlation** - Can logs be correlated with other systems?
   - Critical: Forensic investigation capability
   - High: SIEM correlation, incident response
   - Medium: Operational troubleshooting
   - Low: Isolated systems with local-only logs

2. **Authentication** - Does time affect authentication?
   - Critical: Kerberos (5-minute tolerance)
   - High: Certificate validation
   - Medium: Token expiration
   - Low: No time-dependent authentication

3. **Compliance** - Does non-compliance create regulatory risk?
   - Critical: Financial/healthcare regulations
   - High: Audit findings
   - Medium: Policy variance
   - Low: Internal guidance only

4. **Operations** - Does time affect operations?
   - Critical: Scheduling, batch processing
   - High: Reporting accuracy
   - Medium: User convenience
   - Low: No operational impact

### Risk Rating Matrix

| Impact | Compensating Control Effectiveness | Risk Rating |
|--------|-------------------------------------|-------------|
| Critical | Strong (GPS, atomic) | High - CISO approval |
| Critical | Moderate (manual sync) | Critical - May not be acceptable |
| High | Strong | Medium - Risk owner approval |
| High | Moderate | High - CISO approval |
| Medium | Any | Low-Medium - Risk owner approval |
| Low | Any | Low - Standard exception |

### Documentation Requirements by Risk Level

**Low Risk:**

- Basic justification
- Compensating control description
- Risk owner approval

**Medium Risk:**

- Detailed justification with technical assessment
- Compensating control implementation evidence
- Risk owner approval
- Quarterly review

**High Risk:**

- Formal risk assessment document
- Compensating control effectiveness validation
- Risk owner AND CISO approval
- Monthly review

**Critical Risk:**

- Full risk analysis with executive summary
- Compensating control proof of effectiveness
- Risk owner, CISO, AND Executive approval
- Or: Do not approve exception

---

## Compensating Control Implementation

### Local GPS Receiver Installation

**Purpose:** Provide Stratum 0/1 time source for air-gapped networks.

**Hardware Options:**

| Product | Stratum | Typical Cost | Notes |
|---------|---------|--------------|-------|
| Meinberg LANTIME M300 | 1 | €3,000-5,000 | Enterprise grade |
| EndRun Meridian II | 1 | $2,000-4,000 | Good accuracy |
| Microsemi/Symmetricom | 1 | $3,000-8,000 | High precision |
| Budget GPS (ublox-based) | 1 | €200-500 | Hobbyist, less reliable |

**Installation Requirements:**

1. GPS antenna with clear sky view (roof mount typically)
2. Lightning protection for outdoor antenna
3. Network connectivity within air-gapped zone
4. Power with UPS backup

**Configuration:**

- Configure as NTP server for air-gapped network
- Air-gapped systems point to local GPS NTP
- Monitor GPS signal lock status

**Verification:**

```bash
# On GPS NTP appliance
chronyc tracking   # Should show refid = GPS or PPS
chronyc sources    # Should show GPS source selected

# On air-gapped systems
chronyc tracking   # Should show local GPS NTP as source
```

---

### Manual Time Synchronization Procedure

**Purpose:** Periodic manual clock setting for systems without NTP.

**Procedure Template:**

1. **Preparation**
   - Access authoritative time reference (time.nist.gov, GPS receiver)
   - Document current system time before sync
   - Note offset for audit trail

2. **Synchronization**
   - Access system clock settings (admin console, BIOS, CLI)
   - Set time to match reference
   - Set date if required
   - Apply changes

3. **Verification**
   - Confirm system time matches reference (within tolerance)
   - Document post-sync time
   - Calculate and record sync offset

4. **Documentation**
   - Record sync event in exception log
   - Sign-off by authorized personnel
   - File evidence (screenshot, log entry)

**Frequency Guidance:**

| System Drift Rate | Sync Frequency |
|-------------------|----------------|
| <1 second/day | Monthly |
| 1-5 seconds/day | Weekly |
| >5 seconds/day | Daily (or remediate) |

---

### Drift Monitoring for Vendor-Managed Systems

**Purpose:** Validate vendor time synchronization is working.

**Monitoring Approach:**

1. **External Time Comparison**
   - Query vendor system time via API or log timestamp
   - Compare to authoritative reference
   - Alert if delta exceeds threshold

2. **Log Timestamp Analysis**
   - Monitor logs for timestamp anomalies
   - Compare log timestamps to correlated events
   - Flag significant discrepancies

3. **Periodic Manual Validation**
   - Monthly manual check of system time
   - Document comparison to reference
   - Escalate to vendor if drift exceeds SLA

**Alert Thresholds:**

| System Criticality | Alert Threshold | Action |
|--------------------|-----------------|--------|
| Critical | >100ms | Immediate investigation |
| High | >500ms | Same-day review |
| Medium | >1 second | Next business day |
| Low | >5 seconds | Weekly review |

---

# SECTION B: Assessment Workbook Specification

## Workbook Overview

**Filename:** ISMS-IMP-A.8.17-S3_Exception_Management_[YYYYMMDD].xlsx

**Generated By:** `generate_a817_s3_exception_management.py`

**Purpose:** Template for documenting and managing clock synchronization exceptions

**Sheets:**
1. **Instructions** - Workbook usage instructions and legend
2. **Exception_Requests** - New exception request workflow
3. **Active_Exceptions** - Currently approved exceptions
4. **Expired_Exceptions** - Historical expired exceptions
5. **Summary_Dashboard** - Exception metrics overview

**Total Sheets:** 5

---

## Common Styling Definitions

**Header Style:**

- Font: Bold, White (FFFFFF), Size 11
- Fill: Dark Blue (366092)
- Alignment: Center, Vertical Center, Wrap Text
- Border: Thin borders all sides

**Title Style:**

- Font: Bold, Size 14, Dark Blue (366092)
- Alignment: Left, Vertical Center

**Data Cell Style:**

- Alignment: Left, Vertical Center, Wrap Text
- Border: Thin borders all sides

**Center Style:**

- Alignment: Center, Vertical Center
- Border: Thin borders all sides

---

## Sheet 1: Instructions

**Purpose:** Provide workbook usage instructions, status legend, and navigation guidance.

**Layout:**

**Row 1-2:** Title Block

- A1: "ISMS A.8.17-S3 - Exception Management" (Font: Bold 16, Dark Blue, Merged A1:F1)
- A2: "Generated: [Timestamp]" (Font: Italic 10, Merged A2:F2)

**Row 4-5:** Document Metadata

- A4: "Document ID:" (Bold) | B4: "ISMS-IMP-A.8.17-S3" (Bold, Dark Blue)
- A5: "Title:" (Bold) | B5: "Clock Synchronization Exception Management"

**Row 7+:** Instructions Content

- Purpose statement
- Sheet descriptions
- Status legend (Exception_Requests, Active_Exceptions)
- Approval workflow summary
- Compensating control guidance
- Link to ISMS-POL-A.8.17 Section 3.3

**Column Widths:**

- A: 15
- B: 80
- C-F: 15 each

---

## Sheet 2: Exception_Requests

**Purpose:** Document pending exception requests requiring approval.

**Headers (Row 1):**

| Column | Header | Width | Required | Data Type | Dropdown/Validation |
|--------|--------|-------|----------|-----------|---------------------|
| A | Request ID [*] | 18 | Yes | Text | None |
| B | System Name [*] | 22 | Yes | Text | None |
| C | System Type [*] | 18 | Yes | Dropdown | OT/ICS System, Legacy System, Vendor Appliance, Air-Gapped System, Embedded Device, Test/Lab System, Other |
| D | Business Owner [*] | 20 | Yes | Text | None |
| E | Exception Category [*] | 22 | Yes | Dropdown | Air-Gapped (No Network), Legacy (No NTP Support), Vendor Restriction, Regulatory Requirement, Business Requirement, Other |
| F | Justification [*] | 40 | Yes | Text | None |
| G | Risk Assessment [*] | 35 | Yes | Text | None |
| H | Compensating Controls [*] | 40 | Yes | Text | None |
| I | Requested Duration [*] | 15 | Yes | Dropdown | 3 months, 6 months, 12 months, Permanent |
| J | Request Date [*] | 12 | Yes | Date | None |
| K | Requested By [*] | 18 | Yes | Text | None |
| L | Risk Owner Approval | 15 | No | Dropdown | Pending, Approved, Rejected |
| M | Risk Owner Date | 12 | No | Date | None |
| N | CISO Approval | 15 | No | Dropdown | Not Required, Pending, Approved, Rejected |
| O | CISO Date | 12 | No | Date | None |
| P | Request Status [*] | 18 | Yes | Dropdown | Draft, Submitted, Risk Owner Review, CISO Review, Approved, Rejected, Withdrawn |
| Q | Notes | 35 | No | Text | None |

**Data Validation:**

**Column C (System Type):**

- Type: List
- Formula: `"OT/ICS System,Legacy System,Vendor Appliance,Air-Gapped System,Embedded Device,Test/Lab System,Other"`
- Applies To: C2:C100

**Column E (Exception Category):**

- Type: List
- Formula: `"Air-Gapped (No Network),Legacy (No NTP Support),Vendor Restriction,Regulatory Requirement,Business Requirement,Other"`
- Applies To: E2:E100

**Column I (Requested Duration):**

- Type: List
- Formula: `"3 months,6 months,12 months,Permanent"`
- Applies To: I2:I100

**Column L (Risk Owner Approval):**

- Type: List
- Formula: `"Pending,Approved,Rejected"`
- Applies To: L2:L100

**Column N (CISO Approval):**

- Type: List
- Formula: `"Not Required,Pending,Approved,Rejected"`
- Applies To: N2:N100

**Column P (Request Status):**

- Type: List
- Formula: `"Draft,Submitted,Risk Owner Review,CISO Review,Approved,Rejected,Withdrawn"`
- Applies To: P2:P100

**Empty Template Rows:** Rows 2-20 (formatted with borders, no data)

**Freeze Panes:** A2 (freeze header row)

---

## Sheet 3: Active_Exceptions

**Purpose:** Document currently approved and active exceptions.

**Headers (Row 1):**

| Column | Header | Width | Required | Data Type | Dropdown/Validation |
|--------|--------|-------|----------|-----------|---------------------|
| A | Exception ID [*] | 18 | Yes | Text | None |
| B | System Name [*] | 22 | Yes | Text | None |
| C | System Type [*] | 18 | Yes | Dropdown | (same as Exception_Requests) |
| D | Business Owner [*] | 20 | Yes | Text | None |
| E | Exception Category [*] | 22 | Yes | Dropdown | (same as Exception_Requests) |
| F | Approved Justification [*] | 40 | Yes | Text | None |
| G | Compensating Controls [*] | 40 | Yes | Text | None |
| H | Approval Date [*] | 12 | Yes | Date | None |
| I | Approved By [*] | 25 | Yes | Text | None |
| J | Expiration Date [*] | 12 | Yes | Date | None |
| K | Review Schedule [*] | 15 | Yes | Dropdown | Monthly, Quarterly, Semi-annually |
| L | Last Review Date | 12 | No | Date | None |
| M | Review Status | 15 | No | Dropdown | Current, Overdue, Review Scheduled |
| N | Responsible Party [*] | 20 | Yes | Text | None |
| O | Renewal Status | 15 | No | Dropdown | Not Due, In Progress, Renewed, Expiring Soon |
| P | Notes | 35 | No | Text | None |

**Data Validation:**

**Column K (Review Schedule):**

- Type: List
- Formula: `"Monthly,Quarterly,Semi-annually"`
- Applies To: K2:K100

**Column M (Review Status):**

- Type: List
- Formula: `"Current,Overdue,Review Scheduled"`
- Applies To: M2:M100

**Column O (Renewal Status):**

- Type: List
- Formula: `"Not Due,In Progress,Renewed,Expiring Soon"`
- Applies To: O2:O100

**Conditional Formatting:**

- Expiration Date < TODAY(): Red fill (expired)
- Expiration Date < TODAY()+30: Yellow fill (expiring soon)
- Review Status = "Overdue": Red text

**Empty Template Rows:** Rows 2-20 (formatted with borders, no data)

**Freeze Panes:** A2 (freeze header row)

---

## Sheet 4: Expired_Exceptions

**Purpose:** Archive previously approved exceptions for historical tracking.

**Headers (Row 1):**

| Column | Header | Width | Required | Data Type | Dropdown/Validation |
|--------|--------|-------|----------|-----------|---------------------|
| A | Exception ID [*] | 18 | Yes | Text | None |
| B | System Name [*] | 22 | Yes | Text | None |
| C | System Type [*] | 18 | Yes | Text | None |
| D | Exception Category [*] | 22 | Yes | Text | None |
| E | Original Approval Date [*] | 15 | Yes | Date | None |
| F | Expiration Date [*] | 12 | Yes | Date | None |
| G | Expiration Reason [*] | 22 | Yes | Dropdown | Remediated (Now Compliant), Renewed (New Exception), System Decommissioned, Rejected on Renewal, Risk Accepted Permanently |
| H | Final Compensating Controls | 40 | No | Text | None |
| I | Successor Exception ID | 18 | No | Text | None |
| J | Lessons Learned | 40 | No | Text | None |
| K | Archived By [*] | 18 | Yes | Text | None |
| L | Archive Date [*] | 12 | Yes | Date | None |
| M | Notes | 35 | No | Text | None |

**Data Validation:**

**Column G (Expiration Reason):**

- Type: List
- Formula: `"Remediated (Now Compliant),Renewed (New Exception),System Decommissioned,Rejected on Renewal,Risk Accepted Permanently"`
- Applies To: G2:G100

**Empty Template Rows:** Rows 2-20 (formatted with borders, no data)

**Freeze Panes:** A2 (freeze header row)

---

## Sheet 5: Summary_Dashboard

**Purpose:** Provide management overview of exception status and trends.

**Layout:**

**Section 1: Exception Counts (Rows 1-8)**

| Row | Column A | Column B | Column C |
|-----|----------|----------|----------|
| 1 | "Exception Management Dashboard" (Title, merged A1:C1) | | |
| 2 | "Last Updated:" | [Date] | |
| 4 | "Metric" (Header) | "Count" (Header) | "Notes" (Header) |
| 5 | "Total Active Exceptions" | =COUNTA(Active_Exceptions!A2:A100) | |
| 6 | "Pending Requests" | =COUNTIF(Exception_Requests!P2:P100,"Submitted")+... | |
| 7 | "Expiring Next 30 Days" | =COUNTIFS(...) | Requires renewal action |
| 8 | "Expiring Next 90 Days" | =COUNTIFS(...) | Plan renewal process |

**Section 2: Exception Categories (Rows 10-18)**

| Row | Column A | Column B | Column C |
|-----|----------|----------|----------|
| 10 | "Exception Categories" (Header, merged) | | |
| 11 | "Category" (Header) | "Count" (Header) | "Percentage" (Header) |
| 12 | "Air-Gapped (No Network)" | =COUNTIF(Active_Exceptions!E:E,"Air-Gapped*") | =B12/B5 |
| 13 | "Legacy (No NTP Support)" | =COUNTIF(...) | =B13/B5 |
| ... | ... | ... | ... |

**Section 3: System Types (Rows 20-28)**

Similar structure to Section 2.

**Section 4: Review Status (Rows 30-35)**

| Row | Column A | Column B | Column C |
|-----|----------|----------|----------|
| 30 | "Review Status Summary" (Header, merged) | | |
| 31 | "Status" (Header) | "Count" (Header) | "Action Required" (Header) |
| 32 | "Current" | =COUNTIF(Active_Exceptions!M:M,"Current") | "None" |
| 33 | "Overdue" | =COUNTIF(Active_Exceptions!M:M,"Overdue") | "Immediate review required" |
| 34 | "Review Scheduled" | =COUNTIF(Active_Exceptions!M:M,"Review Scheduled") | "Per schedule" |

**Section 5: Upcoming Expirations (Rows 37-50)**

Auto-filtered list of exceptions expiring within 90 days.

**Section 6: Trend Analysis (Rows 52-60)**

Manual entry table for quarterly trends.

**Section 7: Key Observations (Rows 62+)**

Free-form text area for management comments.

---

## Python Script Reference

**Script File:** `generate_a817_s3_exception_management.py`

**Script Location:** `10-isms-scr-base/isms-a.8.17-clock-synchronization/10_generator-master/`

**Key Functions:**

- `create_styles()` - Defines all styling
- `create_instructions_sheet()` - Generates Instructions sheet
- `create_exception_requests_sheet()` - Generates Exception_Requests sheet
- `create_active_exceptions_sheet()` - Generates Active_Exceptions sheet
- `create_expired_exceptions_sheet()` - Generates Expired_Exceptions sheet
- `create_summary_dashboard_sheet()` - Generates Summary_Dashboard sheet
- `main()` - Orchestrates workbook generation

**To regenerate workbook:**

```bash
cd 10-isms-scr-base/isms-a.8.17-clock-synchronization/10_generator-master
python3 generate_a817_s3_exception_management.py
mv *.xlsx ../90_workbooks/
```

**Output:** Excel workbook ready for user completion per Part I User Guide.

---

**END OF SPECIFICATION**

---

*"Lost time is never found again."*
— Benjamin Franklin

<!-- QA_VERIFIED: 2026-02-01 -->
