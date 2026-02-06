**ISMS-IMP-A.8.17-S3-UG - Exception Management**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.17: Clock Synchronization

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.17-S3-UG |
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

This is the **User Completion Guide**. The companion Technical Specification is documented in ISMS-IMP-A.8.17-S3-TG.

---

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

**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
