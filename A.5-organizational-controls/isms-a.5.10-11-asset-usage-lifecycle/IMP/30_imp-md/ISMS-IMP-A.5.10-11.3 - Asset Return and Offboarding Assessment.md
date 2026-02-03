# ISMS-IMP-A.5.10-11.3 — Asset Return and Offboarding Assessment

---

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.10-11.3 |
| **Title** | Asset Return and Offboarding Assessment |
| **Control Reference** | ISO/IEC 27001:2022 A.5.11 |
| **Control Name** | Return of Assets |
| **Document Type** | Implementation Guide |
| **Version** | 1.0 |
| **Last Updated** | [Date to be set] |
| **Owner** | Information Security Manager |
| **Classification** | Internal |

---

## Table of Contents

**PART I: USER COMPLETION GUIDE**
1. [Assessment Overview](#assessment-overview)
2. [Control Requirement](#control-requirement)
3. [Prerequisites](#prerequisites)
4. [Key Terminology](#key-terminology)
5. [Return Process Framework](#return-process-framework)
6. [Asset Return Requirements](#asset-return-requirements)
7. [Workbook Structure](#workbook-structure)
8. [Completion Walkthrough](#completion-walkthrough)
9. [Access Revocation Framework](#access-revocation-framework)
10. [Offboarding Scenarios](#offboarding-scenarios)
11. [Evidence Collection](#evidence-collection)
12. [Common Pitfalls](#common-pitfalls)
13. [Quality Checklist](#quality-checklist)
14. [Review & Approval](#review-approval)

**PART II: TECHNICAL SPECIFICATION**
1. [Workbook Architecture](#workbook-architecture)
2. [Sheet Specifications](#sheet-specifications)
3. [Data Validations](#data-validations)
4. [Conditional Formatting Rules](#conditional-formatting-rules)
5. [Formula Specifications](#formula-specifications)
6. [Generator Reference](#generator-reference)

---

## PART I: USER COMPLETION GUIDE

### Assessment Overview

**Purpose**

This workbook evaluates and tracks the organisation's asset return processes during employment termination, contract completion, or role changes. It ensures complete and verified return of organisational assets per ISO 27001:2022 Control A.5.11. The assessment provides a structured methodology for documenting return processes, tracking individual offboardings, and verifying access revocation.

**Scope**

This assessment covers:
- Return process completeness assessment
- Standard asset return checklists by asset type
- Individual offboarding tracking and monitoring
- Access revocation verification and timing
- Return compliance monitoring and metrics
- Knowledge transfer requirements
- Data sanitisation verification
- Remote worker return coordination
- Contractor and third-party offboarding

**What This Assessment Covers**

| Domain | Assessment Focus |
|--------|------------------|
| Process Assessment | Return procedure completeness and documentation |
| Asset Checklist | What must be returned by category |
| Offboarding Tracking | Individual departure tracking |
| Access Revocation | System access removal verification |
| SLA Compliance | Timeliness of return and revocation |
| Knowledge Transfer | Critical information handover |
| Data Security | Data wipe and sanitisation verification |

**Assessment Frequency**

- Full process assessment: Annual
- Offboarding tracking: Continuous (per departure)
- Access revocation verification: Per departure
- Metrics review: Monthly

### Control Requirement

ISO 27001:2022 A.5.11 states:

> "Personnel and other interested parties as appropriate should return all the organisation's assets in their possession upon change or termination of their employment, contract or agreement."

**ISO 27002:2022 Implementation Guidance**

The return process should address:

| Guidance Area | Implementation Requirement |
|---------------|---------------------------|
| **Formal Process** | Documented offboarding procedure including asset return |
| **Asset Identification** | List of assets assigned to each individual |
| **Physical Assets** | Laptops, mobile devices, tokens, keys, documents |
| **Digital Assets** | Access credentials, stored data, cloud accounts |
| **Timing** | Prompt return upon termination or role change |
| **Verification** | Confirmation that all assets have been returned |
| **Data Handling** | Secure handling of information on returned assets |
| **Personal Data** | Separation of personal from organisational data |
| **Knowledge Transfer** | Ensuring critical knowledge is captured |

**Regulatory Considerations**

| Regulation | Relevant Requirement |
|------------|----------------------|
| Swiss FADP/nDSG | Protection of personal data during offboarding |
| EU GDPR | Right to erasure; data processing termination |
| Employment Law | Return of employer property obligations |
| IP Regulations | Return of confidential/proprietary materials |

### Prerequisites

Before completing this assessment, ensure:

**Process Prerequisites**

- [ ] Documented offboarding procedure exists
- [ ] HR termination notification process defined
- [ ] IT access revocation process documented
- [ ] Asset inventory linked to personnel records
- [ ] Data wiping procedure documented
- [ ] Remote worker return procedure exists

**Access Prerequisites**

- [ ] Access to HR termination notifications
- [ ] Access to asset management system
- [ ] Access to Active Directory/IAM system
- [ ] Access to application owner contacts
- [ ] Access to historical offboarding records

**Data Prerequisites**

- [ ] List of recent departures (12 months)
- [ ] Asset inventory export per employee
- [ ] Access revocation logs
- [ ] Return forms and sign-off records

**Stakeholder Engagement**

- [ ] HR Manager available for process review
- [ ] IT Manager available for access verification
- [ ] Facilities Manager for physical asset coordination
- [ ] Department managers for knowledge transfer review

### Key Terminology

| Term | Definition |
|------|------------|
| **Offboarding** | The formal process of managing employee/contractor departure |
| **Asset Return** | Physical or digital handover of organisational property |
| **Access Revocation** | Removal of system and physical access rights |
| **Last Working Day (LWD)** | Final day of employment or contract |
| **SLA** | Service Level Agreement for action completion timing |
| **Data Wipe** | Secure erasure of data from returned devices |
| **Knowledge Transfer** | Handover of role-specific information to successor |
| **Exit Interview** | Final meeting to complete offboarding tasks |
| **Return Verification** | Confirmation that asset has been received |
| **Leaver Type** | Category of departure (resignation, termination, etc.) |

### Return Process Framework

**Process Overview**

The asset return process follows a structured workflow from departure notification to final sign-off:

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   Notification  │────▶│   Preparation   │────▶│    Execution    │
│   HR notifies   │     │  Asset list     │     │  Asset return   │
│   IT/Security   │     │  Access review  │     │  Access revoke  │
└─────────────────┘     └─────────────────┘     └─────────────────┘
                                                        │
                                                        ▼
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│    Sign-Off     │◀────│   Verification  │◀────│   Data Wipe     │
│  Final closure  │     │  All returned?  │     │  Device secure  │
│  HR confirmed   │     │  Access gone?   │     │  Data erased    │
└─────────────────┘     └─────────────────┘     └─────────────────┘
```

**Process Stages**

| Stage | Description | Responsible | Timeline |
|-------|-------------|-------------|----------|
| **1. Notification** | HR notifies IT/Security of upcoming departure | HR Manager | Upon resignation/termination decision |
| **2. Asset Inventory** | Generate list of assets assigned to leaver | IT Asset Manager | Within 24 hours of notification |
| **3. Access Review** | Identify all system/physical access to revoke | IT Security | Within 24 hours of notification |
| **4. Knowledge Transfer** | Ensure critical knowledge is documented/transferred | Department Manager | Before LWD |
| **5. Asset Collection** | Physical return of equipment and materials | IT/Facilities | On or before LWD |
| **6. Access Revocation** | Remove all system and physical access | IT Security | By end of LWD |
| **7. Data Wipe** | Secure erasure of returned devices | IT Operations | Within 5 days of return |
| **8. Verification** | Confirm all assets returned, access removed | IT Security | Within 3 days of LWD |
| **9. Sign-Off** | Final offboarding closure with HR confirmation | HR/IT Security | Within 5 days of LWD |

**SLA Requirements**

| Action | Standard SLA | Immediate Termination SLA |
|--------|--------------|---------------------------|
| IT Notification | Within 24 hours of HR notification | Immediately |
| Asset List Generation | Within 24 hours | Within 2 hours |
| Physical Asset Return | By LWD | Same day |
| Network Access Revocation | By end of LWD | Immediately |
| Email Access Revocation | By end of LWD | Immediately |
| Application Access Revocation | Within 24 hours of LWD | Within 4 hours |
| VPN Revocation | By end of LWD | Immediately |
| Badge Deactivation | By end of LWD | Immediately |
| Data Wipe Completion | Within 5 business days | Within 24 hours |
| Final Sign-Off | Within 5 business days | Within 3 business days |

### Asset Return Requirements

**Physical Asset Categories**

| Category | Asset Types | Return Method | Verification |
|----------|-------------|---------------|--------------|
| **Computing Devices** | Laptops, desktops, tablets | In-person handover | Serial number match |
| **Mobile Devices** | Phones, smartphones | In-person handover | IMEI verification |
| **Peripherals** | Monitors, keyboards, mice | In-person handover | Asset tag match |
| **Storage Media** | USB drives, external HDDs, CDs | In-person handover | Visual inspection |
| **Authentication** | Smart cards, tokens, fobs | In-person handover | Serial/ID match |
| **Physical Access** | Keys, access badges | In-person handover | Badge ID verification |
| **Printed Materials** | Confidential documents, manuals | In-person handover | Destruction/return |
| **Company Cards** | Credit cards, fuel cards | In-person handover | Card number match |
| **Uniforms/Equipment** | Safety gear, branded items | In-person handover | Visual inspection |

**Digital Access Categories**

| Category | Access Types | Revocation Method | Verification |
|----------|--------------|-------------------|--------------|
| **Network** | AD account, Wi-Fi | AD disable/delete | Login attempt fails |
| **Email** | Exchange/O365, aliases | Account disable | Mailbox inaccessible |
| **VPN** | Remote access | Certificate revoke | Connection fails |
| **Applications** | Business systems | Account disable | Login fails |
| **Cloud Services** | SaaS applications | Account remove | Access denied |
| **Databases** | Direct DB access | Credential revoke | Query fails |
| **Admin Access** | Privileged accounts | Account disable | Elevated access gone |
| **Shared Resources** | File shares, SharePoint | Permission remove | Access denied |

**Remote Worker Return Process**

For employees working remotely:

| Step | Action | Responsibility |
|------|--------|----------------|
| 1 | Provide prepaid shipping materials | IT Operations |
| 2 | Arrange courier pickup or drop-off location | IT Operations |
| 3 | Track shipment in transit | IT Operations |
| 4 | Confirm receipt and condition | IT Asset Manager |
| 5 | Process return in asset system | IT Asset Manager |
| 6 | Initiate data wipe | IT Operations |

**International Considerations**

| Region | Special Considerations |
|--------|------------------------|
| EU/EEA | GDPR requirements for personal data separation |
| Switzerland | FADP requirements; cross-border data handling |
| USA | State-specific wage/final pay requirements |
| APAC | Various labour law requirements |

### Workbook Structure

| Sheet | Purpose | Key Actions |
|-------|---------|-------------|
| Instructions | Guidance and metadata | Complete document information |
| Return_Process | Process assessment | Evaluate procedure completeness |
| Asset_Checklist | Standard return checklist | Define returnable asset types |
| Offboarding_Tracking | Individual tracking | Track each departure |
| Access_Revocation | Access removal verification | Verify access termination |
| Evidence_Register | Audit evidence linking | Document evidence locations |
| Approval_SignOff | Assessment approval | Obtain required signatures |

### Completion Walkthrough

**Step 1: Document Information (Instructions Sheet)**

Complete assessment metadata:

| Field | Input Required |
|-------|----------------|
| Assessment Title | Pre-populated |
| Document ID | Pre-populated (ISMS-IMP-A.5.10-11.3) |
| Control Reference | Pre-populated (A.5.11) |
| Assessment Period | Start and end dates for review |
| Assessor Name | Person conducting assessment |
| Department | Assessor's department |
| Review Date | Date of current assessment |
| Version | Assessment version number |

**Step 2: Return Process Assessment (Return_Process Sheet)**

Evaluate each process requirement:

1. **Requirement_ID** - Pre-populated requirement reference (PR-001, etc.)
2. **Process_Requirement** - What the process should include
3. **Category** - Process category
4. **Implemented** - Yes/Partial/No status
5. **Documented** - Whether procedure is documented
6. **Responsible_Role** - Who owns the process step
7. **SLA_Days** - Target completion timeframe
8. **Automated** - Whether process is automated
9. **Gap_Status** - Gap/Compliant/Risk Accepted
10. **Remediation_Notes** - Actions needed
11. **Evidence_Ref** - Link to supporting evidence

**Process Requirement Categories**:

| Category | Requirements Covered |
|----------|---------------------|
| Notification Process | HR-to-IT notification, timing, channels |
| Asset Tracking | Inventory linkage, assignment records |
| Physical Return | Collection process, verification |
| Access Revocation | System access removal procedures |
| Data Security | Data wipe, device sanitisation |
| Knowledge Transfer | Handover documentation |
| Verification | Completion confirmation |
| Escalation | Incomplete return handling |
| Documentation | Record keeping requirements |

**Assessment Scoring**:

| Status | Score | Criteria |
|--------|-------|----------|
| Implemented: Yes | 1.0 | Process fully implemented and documented |
| Implemented: Partial | 0.5 | Process exists but incomplete or informal |
| Implemented: No | 0.0 | Process not implemented |

**Step 3: Asset Checklist (Asset_Checklist Sheet)**

Define what must be returned for each asset type:

1. **Asset_Type** - Category of asset
2. **Description** - Detailed description
3. **Category** - Hardware/Authentication/Digital/Document/Other
4. **Return_Required** - Yes/No/Optional
5. **Verification_Method** - How return is verified
6. **Responsible_Team** - Who receives the asset
7. **SLA_Days** - Return deadline from LWD
8. **Data_Wipe_Required** - Yes/No/N/A
9. **Disposal_If_Not_Returned** - Action if unreturned
10. **Notes** - Additional requirements

**Asset Type Coverage Checklist**:

| Physical Assets | Digital Assets | Documentation |
|-----------------|----------------|---------------|
| Laptop | Network credentials | Confidential documents |
| Desktop | Email account | Project files |
| Mobile phone | Application accounts | Customer data |
| Tablet | VPN certificate | Intellectual property |
| Token/Smart card | Cloud service access | Access codes/passwords |
| Keys | Database access | Procedures/manuals |
| Badge | Admin credentials | Training materials |
| Company vehicle | Shared drive access | - |

**Step 4: Offboarding Tracking (Offboarding_Tracking Sheet)**

Track each individual departure:

1. **Offboard_ID** - Auto-generated identifier (OFF-001, etc.)
2. **Employee_Name** - Person departing
3. **Employee_ID** - Employee/contractor ID
4. **Department** - Their department
5. **Employee_Type** - Employee/Contractor/Consultant/Intern/Temp
6. **Manager** - Reporting manager
7. **Last_Working_Day** - Final working day
8. **Offboard_Reason** - Resignation/Termination/Contract End/Transfer/Retirement/Other
9. **Notice_Date** - Date HR notified IT
10. **Assets_Assigned** - Count of assigned assets
11. **Assets_Returned** - Count of returned assets
12. **Return_Status** - Complete/In Progress/Pending/Overdue
13. **Access_Revoked** - Yes/No/Partial
14. **Data_Wiped** - Yes/No/Pending/N/A
15. **Knowledge_Transfer** - Complete/Partial/N/A
16. **Sign_Off_Date** - Completion date
17. **HR_Confirmed** - Yes/No
18. **Notes** - Additional comments

**Return Status Definitions**:

| Status | Definition |
|--------|------------|
| Complete | All assets returned and verified |
| In Progress | Return process underway |
| Pending | Not yet started (future LWD) |
| Overdue | Past LWD with outstanding items |

**Step 5: Access Revocation (Access_Revocation Sheet)**

Verify access removal for each system:

1. **Revocation_ID** - Auto-generated identifier (REV-001, etc.)
2. **Employee_Ref** - Link to Offboarding_Tracking (Offboard_ID)
3. **Employee_Name** - For reference
4. **Access_Type** - Network/VPN/Email/Application/Database/Cloud/Physical/Admin
5. **System_Application** - Specific system name
6. **Access_Level** - User/Power User/Admin/etc.
7. **Last_Working_Day** - Reference date
8. **Target_Revocation** - When revocation should occur
9. **Revocation_Date** - When access was actually removed
10. **SLA_Met** - Yes/No (was it within SLA?)
11. **Revoked_By** - Person who performed revocation
12. **Verification_Method** - How removal was verified
13. **Verified_By** - Person who verified
14. **Verification_Date** - Date of verification
15. **Notes** - Additional comments

**Verification Methods**:

| Method | Description | Applicable To |
|--------|-------------|---------------|
| AD Query | Check Active Directory for disabled/deleted account | Network, Email |
| System Log | Review system logs for account status | All systems |
| Login Attempt | Verify login fails with old credentials | All systems |
| Screenshot | Capture showing disabled/removed status | All systems |
| Attestation | System owner written confirmation | Applications |
| Certificate Check | Verify certificate revoked | VPN |
| Badge Scan | Attempt badge scan fails | Physical access |

**Step 6: Evidence Register (Evidence_Register Sheet)**

Document evidence for audit purposes:

1. **Evidence_ID** - Unique identifier
2. **Evidence_Type** - Document/Screenshot/Log/Form/Report
3. **Description** - What the evidence shows
4. **Related_Requirement** - Links to Return_Process
5. **Related_Offboard** - Links to Offboarding_Tracking
6. **File_Reference** - Evidence file name/location
7. **Date_Collected** - When evidence was gathered
8. **Collected_By** - Who gathered the evidence
9. **Storage_Location** - Where evidence is stored

**Step 7: Approval and Sign-Off (Approval_SignOff Sheet)**

Complete approval section with required signatures:

| Approval Level | Role | Scope of Approval |
|----------------|------|-------------------|
| Assessment Completion | Assessor | Assessment accuracy |
| IT Verification | IT Manager | Technical accuracy |
| HR Confirmation | HR Manager | Process compliance |
| Final Approval | CISO | Overall assessment |

### Access Revocation Framework

**Revocation Priority Levels**

| Priority | Access Type | Timing | Rationale |
|----------|-------------|--------|-----------|
| **P1 - Immediate** | Network, VPN, Email, Admin | End of LWD or immediately for termination | Core access vectors |
| **P2 - Same Day** | Physical access (badge, keys) | End of LWD | Physical security |
| **P3 - 24 Hours** | Applications, Cloud services | Within 24 hours of LWD | Business system access |
| **P4 - 48 Hours** | Shared resources, Databases | Within 48 hours of LWD | Secondary access |

**Revocation Checklist by Access Type**

**Network/Active Directory**
- [ ] Disable AD account
- [ ] Remove from security groups
- [ ] Revoke VPN certificate
- [ ] Remove from Wi-Fi allowlist
- [ ] Update DNS/DHCP reservations

**Email/Communication**
- [ ] Disable mailbox
- [ ] Set up forwarding/auto-reply (if approved)
- [ ] Remove from distribution lists
- [ ] Revoke Teams/Slack access
- [ ] Remove calendar delegates

**Applications**
- [ ] Disable each application account
- [ ] Remove SSO access
- [ ] Revoke API keys/tokens
- [ ] Transfer ownership of resources
- [ ] Remove from application groups

**Physical Access**
- [ ] Deactivate badge
- [ ] Collect keys
- [ ] Update visitor lists
- [ ] Remove parking access
- [ ] Update building security

### Offboarding Scenarios

**Scenario 1: Standard Resignation**

| Timeline | Action | Responsible |
|----------|--------|-------------|
| Day -14 (resignation) | HR notifies IT of resignation | HR Manager |
| Day -14 | Asset list generated | IT Asset Manager |
| Day -13 to -1 | Knowledge transfer completed | Department Manager |
| Day 0 (LWD) | Assets collected, access revoked | IT Operations |
| Day +1 to +5 | Data wipe, final verification | IT Operations |
| Day +5 | Sign-off complete | HR/IT Manager |

**Scenario 2: Immediate Termination**

| Timeline | Action | Responsible |
|----------|--------|-------------|
| Hour 0 | Decision communicated to IT Security | HR Manager |
| Hour 0 | All access revoked immediately | IT Security |
| Hour 0 | Badge deactivated | Facilities |
| Hour 0-1 | Assets collected from desk/person | IT/Security |
| Hour 1-2 | Escorted from premises | Security |
| Day +1 | Data wipe, verification | IT Operations |
| Day +3 | Sign-off complete | HR/IT/Legal |

**Scenario 3: Remote Worker**

| Timeline | Action | Responsible |
|----------|--------|-------------|
| Day -14 | HR notifies IT; shipping arranged | HR/IT Operations |
| Day -10 | Return shipping materials sent | IT Operations |
| Day -1 | Knowledge transfer confirmed | Department Manager |
| Day 0 (LWD) | Access revoked | IT Security |
| Day +1 to +7 | Assets returned via courier | Employee |
| Day +7 | Receipt confirmed, data wipe | IT Operations |
| Day +10 | Sign-off complete | HR/IT Manager |

**Scenario 4: Contractor End**

| Timeline | Action | Responsible |
|----------|--------|-------------|
| Day -30 | Contract end date notification | Procurement |
| Day -7 | IT notified, asset list generated | Vendor Manager |
| Day -5 | Access scope confirmed | IT Security |
| Day 0 (Contract End) | All access revoked | IT Security |
| Day 0 | Assets collected | IT Operations |
| Day +3 | Verification, sign-off | IT Manager |

**Scenario 5: Internal Transfer**

| Timeline | Action | Responsible |
|----------|--------|-------------|
| Day -7 | Transfer notification to IT | HR/Manager |
| Day -5 | Current access reviewed | IT Security |
| Day -5 | New role access requirements | New Manager |
| Day 0 (Transfer) | Old role access removed | IT Security |
| Day 0 | New role access granted | IT Security |
| Day +1 | Verification complete | IT Security |

### Evidence Collection

**Required Evidence**

| Evidence Type | Description | Storage Location |
|---------------|-------------|------------------|
| Offboarding Procedure | Documented process document | ISMS Evidence Library |
| HR Notification | Email/ticket showing IT was notified | ISMS Evidence Library |
| Asset Assignment Records | Screenshot of assets per employee | ISMS Evidence Library |
| Return Forms | Signed asset return acknowledgements | ISMS Evidence Library |
| AD Exports | Screenshot/export showing account disabled | ISMS Evidence Library |
| Access Logs | Logs showing failed login attempts post-LWD | ISMS Evidence Library |
| Wipe Certificates | Data destruction certificates | ISMS Evidence Library |
| Sign-off Records | Completed offboarding forms | ISMS Evidence Library |
| Exception Documentation | Any incomplete returns with justification | ISMS Evidence Library |

**Evidence Storage Requirements**

| Requirement | Specification |
|-------------|---------------|
| Retention Period | 7 years minimum |
| Access Control | Restricted to HR, IT Security, Auditors |
| Naming Convention | `[Offboard_ID]_[Evidence_Type]_[Date].[ext]` |
| Format | PDF preferred for documents; native for exports |

### Common Pitfalls

❌ **MISTAKE**: Not tracking contractors and consultants separately from employees
✅ **CORRECT**: Track all personnel types with appropriate processes; contractors may have different asset assignments and shorter notice periods

❌ **MISTAKE**: Only tracking physical assets and ignoring digital access revocation
✅ **CORRECT**: Digital access revocation is equally critical and often more urgent for security

❌ **MISTAKE**: Waiting until after the last working day to start access revocation
✅ **CORRECT**: Prepare revocation in advance; execute on or before last working day

❌ **MISTAKE**: Not verifying data wipe for returned devices before reissue
✅ **CORRECT**: Confirm data erasure with documented evidence before device reissue

❌ **MISTAKE**: Missing remote worker return coordination entirely
✅ **CORRECT**: Have documented shipping process for remote asset returns with tracking

❌ **MISTAKE**: No escalation process for incomplete or delayed returns
✅ **CORRECT**: Define and execute escalation for outstanding items (Manager → HR → Legal)

❌ **MISTAKE**: Treating all terminations the same regardless of circumstances
✅ **CORRECT**: Immediate revocation for dismissals and security concerns; planned process for resignations

❌ **MISTAKE**: No knowledge transfer tracking or requirements
✅ **CORRECT**: Verify critical knowledge is transferred before departure; document handover

❌ **MISTAKE**: Relying solely on manual processes without verification
✅ **CORRECT**: Implement automated notifications and verification steps where possible

❌ **MISTAKE**: Not documenting exceptions or incomplete returns
✅ **CORRECT**: All exceptions must be documented with justification and risk acceptance

❌ **MISTAKE**: Assuming HR will notify IT automatically
✅ **CORRECT**: Formalise notification process with defined SLAs and confirmation

❌ **MISTAKE**: Not checking privileged/admin access separately
✅ **CORRECT**: Admin accounts require special attention and immediate revocation

❌ **MISTAKE**: Forgetting about shared accounts or generic credentials
✅ **CORRECT**: Review and rotate shared credentials when users with access depart

❌ **MISTAKE**: No verification that revocation was successful
✅ **CORRECT**: Verify each revocation with appropriate method (login test, log review, etc.)

❌ **MISTAKE**: Allowing "grace periods" for access after last working day
✅ **CORRECT**: Access ends on last working day; no exceptions without documented approval

❌ **MISTAKE**: Not tracking SLA compliance for revocations
✅ **CORRECT**: Measure and report on revocation timing; investigate breaches

### Quality Checklist

Before submitting this assessment:

**Process Assessment**
- [ ] All 18 process requirements assessed
- [ ] Implementation status documented for each requirement
- [ ] Responsible roles identified
- [ ] SLAs defined for each process step
- [ ] Gaps identified with remediation notes

**Asset Checklist**
- [ ] All asset types from organisation inventory covered
- [ ] Return requirements defined (Yes/No/Optional)
- [ ] Verification methods specified
- [ ] Data wipe requirements identified
- [ ] Responsible teams assigned

**Offboarding Tracking**
- [ ] Sample of recent offboardings included (minimum 12 months)
- [ ] All employee types represented (employees, contractors, etc.)
- [ ] Return status tracked for each departure
- [ ] Outstanding items identified and escalated

**Access Revocation**
- [ ] All access types covered per departure
- [ ] Revocation dates documented
- [ ] SLA compliance calculated
- [ ] Verification evidence collected
- [ ] Failed verifications investigated

**Evidence and Documentation**
- [ ] Evidence linked for all completed offboardings
- [ ] Exception documentation complete
- [ ] Storage location confirmed
- [ ] Retention requirements met

**Approvals**
- [ ] IT Manager verification obtained
- [ ] HR Manager confirmation obtained
- [ ] CISO final approval obtained

### Review & Approval

**Review Workflow**

1. **Assessment Completion** - Assessor completes process assessment and tracking
2. **IT Manager Review** - Verifies technical accuracy of access revocation data
3. **HR Manager Review** - Confirms offboarding process compliance
4. **CISO Approval** - Final approval for overall assessment

**Review Frequency**

| Review Type | Frequency | Scope |
|-------------|-----------|-------|
| Process Assessment | Annual | Full process review |
| Offboarding Tracking | Continuous | Each departure |
| SLA Compliance Report | Monthly | Timing metrics |
| Trend Analysis | Quarterly | Compliance trends |

**Escalation Path**

| Issue | Escalate To | Timeline |
|-------|-------------|----------|
| Incomplete return after LWD | Department Manager | Day +1 |
| No response after 3 days | HR Manager | Day +4 |
| Assets not returned after 7 days | CISO/Legal | Day +8 |
| Access not revoked by LWD | IT Security Manager | Immediately |

---

## PART II: TECHNICAL SPECIFICATION

### Workbook Architecture

**File Details**

| Attribute | Value |
|-----------|-------|
| Filename | `ISMS-IMP-A.5.10-11.3_Asset_Return_and_Offboarding_Assessment_YYYYMMDD.xlsx` |
| Format | Microsoft Excel (.xlsx) |
| Total Sheets | 7 |
| Target Rows | Process: 18; Assets: 22; Offboarding: 50+; Revocation: 200+ |

**Sheet Overview**

| Sheet Name | Purpose | Row Count |
|------------|---------|-----------|
| Instructions | Guidance and metadata | 35 |
| Return_Process | Process requirements assessment | 18 requirements |
| Asset_Checklist | Asset return definitions | 22 asset types |
| Offboarding_Tracking | Individual departure tracking | Dynamic (50+ recommended) |
| Access_Revocation | Access removal records | Dynamic (5+ per offboarding) |
| Evidence_Register | Evidence documentation | Dynamic |
| Approval_SignOff | Assessment approvals | 10 |

### Sheet Specifications

#### Instructions Sheet

**Metadata Section (Rows 1-20)**

| Row | Content |
|-----|---------|
| 1 | Document title (merged A1:F1) |
| 3-15 | Metadata table (Field/Value pairs) |
| 17-20 | Instructions text |

**Metadata Fields**

| Field | Cell | Content |
|-------|------|---------|
| Assessment Title | B3 | Asset Return and Offboarding Assessment |
| Document ID | B4 | ISMS-IMP-A.5.10-11.3 |
| Control Reference | B5 | A.5.11 |
| Assessment Period Start | B6 | Date (user input) |
| Assessment Period End | B7 | Date (user input) |
| Assessor Name | B8 | Text (user input) |
| Department | B9 | Text (user input) |
| Review Date | B10 | Date (user input) |
| Version | B11 | 1.0 |

#### Return_Process Sheet

**Columns**

| Column | Header | Width | Content |
|--------|--------|-------|---------|
| A | Requirement_ID | 14 | Pre-populated (PR-001 to PR-018) |
| B | Process_Requirement | 45 | Pre-populated requirements |
| C | Category | 22 | Pre-populated categories |
| D | Implemented | 14 | Data validation: Yes/Partial/No |
| E | Documented | 14 | Data validation: Yes/No |
| F | Responsible_Role | 22 | User input |
| G | SLA_Days | 12 | User input (numeric) |
| H | Automated | 14 | Data validation: Yes/No |
| I | Gap_Status | 16 | Data validation |
| J | Remediation_Notes | 35 | User input |
| K | Evidence_Ref | 18 | Evidence reference |

**Pre-populated Requirements (18)**

| ID | Requirement | Category |
|----|-------------|----------|
| PR-001 | Formal offboarding procedure documented | Documentation |
| PR-002 | HR-to-IT notification process defined | Notification |
| PR-003 | Notification SLA established (24 hours) | Notification |
| PR-004 | Asset inventory linked to personnel records | Asset Tracking |
| PR-005 | Asset list generated upon notification | Asset Tracking |
| PR-006 | Return checklist defined per asset type | Asset Return |
| PR-007 | Physical asset collection process | Asset Return |
| PR-008 | Remote worker return shipping process | Asset Return |
| PR-009 | Network access revocation procedure | Access Revocation |
| PR-010 | Application access revocation procedure | Access Revocation |
| PR-011 | Physical access revocation procedure | Access Revocation |
| PR-012 | Access revocation SLA (end of LWD) | Access Revocation |
| PR-013 | Data wipe procedure for returned devices | Data Security |
| PR-014 | Data wipe verification and certification | Data Security |
| PR-015 | Knowledge transfer requirements defined | Knowledge Transfer |
| PR-016 | Return completion sign-off process | Verification |
| PR-017 | Escalation process for incomplete returns | Escalation |
| PR-018 | Exception documentation requirements | Documentation |

**Summary Row (Row 21)**

- Compliance Score: `=SUMPRODUCT((D2:D19="Yes")*1+(D2:D19="Partial")*0.5)/18*100`
- Documentation Score: `=COUNTIF(E2:E19,"Yes")/COUNTA(E2:E19)*100`

#### Asset_Checklist Sheet

**Columns**

| Column | Header | Width | Content |
|--------|--------|-------|---------|
| A | Asset_Type | 25 | Pre-populated types |
| B | Description | 40 | Pre-populated descriptions |
| C | Category | 18 | Pre-populated categories |
| D | Return_Required | 16 | Data validation: Yes/No/Optional |
| E | Verification_Method | 25 | User input |
| F | Responsible_Team | 20 | User input |
| G | SLA_Days | 12 | User input (numeric) |
| H | Data_Wipe_Required | 16 | Data validation: Yes/No/N/A |
| I | Disposal_If_Not_Returned | 25 | User input |
| J | Notes | 30 | User input |

**Pre-populated Asset Types (22)**

| Category | Asset Types |
|----------|-------------|
| Hardware | Laptop, Desktop, Monitor, Keyboard/Mouse, Tablet |
| Mobile | Mobile Phone, Smartphone, SIM Card |
| Storage | USB Drive, External HDD, SD Card |
| Authentication | Smart Card, Hardware Token, Security Key |
| Physical Access | Access Badge, Keys, Parking Pass |
| Documents | Confidential Documents, Company Manuals, Training Materials |
| Other | Company Credit Card, Fuel Card, Company Vehicle |

#### Offboarding_Tracking Sheet

**Columns**

| Column | Header | Width | Content |
|--------|--------|-------|---------|
| A | Offboard_ID | 14 | Auto-generated (OFF-001) |
| B | Employee_Name | 25 | User input |
| C | Employee_ID | 14 | User input |
| D | Department | 20 | User input |
| E | Employee_Type | 16 | Data validation |
| F | Manager | 22 | User input |
| G | Last_Working_Day | 16 | Date field |
| H | Offboard_Reason | 18 | Data validation |
| I | Notice_Date | 14 | Date field |
| J | Assets_Assigned | 14 | User input (numeric) |
| K | Assets_Returned | 14 | User input (numeric) |
| L | Return_Status | 16 | Data validation |
| M | Access_Revoked | 14 | Data validation |
| N | Data_Wiped | 14 | Data validation |
| O | Knowledge_Transfer | 16 | Data validation |
| P | Sign_Off_Date | 14 | Date field |
| Q | HR_Confirmed | 14 | Data validation |
| R | Notes | 30 | User input |

**Summary Metrics (Bottom section)**

| Metric | Formula |
|--------|---------|
| Total Offboardings | `=COUNTA(A2:A[last])` |
| Complete Returns | `=COUNTIF(L:L,"Complete")` |
| Overdue Returns | `=COUNTIF(L:L,"Overdue")` |
| Completion Rate | `=Complete/Total*100` |

#### Access_Revocation Sheet

**Columns**

| Column | Header | Width | Content |
|--------|--------|-------|---------|
| A | Revocation_ID | 14 | Auto-generated (REV-001) |
| B | Employee_Ref | 14 | Link to Offboarding_Tracking |
| C | Employee_Name | 22 | User input |
| D | Access_Type | 18 | Data validation |
| E | System_Application | 28 | User input |
| F | Access_Level | 16 | User input |
| G | Last_Working_Day | 16 | Date field |
| H | Target_Revocation | 16 | Date field |
| I | Revocation_Date | 16 | Date field |
| J | SLA_Met | 12 | Formula: Yes/No |
| K | Revoked_By | 20 | User input |
| L | Verification_Method | 22 | Data validation |
| M | Verified_By | 20 | User input |
| N | Verification_Date | 16 | Date field |
| O | Notes | 30 | User input |

**SLA_Met Formula**

```
=IF(I2="","",IF(I2<=H2,"Yes","No"))
```

**Summary Metrics**

| Metric | Formula |
|--------|---------|
| Total Revocations | `=COUNTA(A2:A[last])` |
| SLA Met | `=COUNTIF(J:J,"Yes")` |
| SLA Missed | `=COUNTIF(J:J,"No")` |
| SLA Compliance % | `=SLA Met/Total*100` |

#### Evidence_Register Sheet

**Columns**

| Column | Header | Width | Content |
|--------|--------|-------|---------|
| A | Evidence_ID | 14 | Auto-generated (EVD-001) |
| B | Evidence_Type | 18 | Data validation |
| C | Description | 40 | User input |
| D | Related_Requirement | 16 | Link to Return_Process |
| E | Related_Offboard | 16 | Link to Offboarding_Tracking |
| F | File_Reference | 30 | User input |
| G | Date_Collected | 14 | Date field |
| H | Collected_By | 20 | User input |
| I | Storage_Location | 25 | User input |

#### Approval_SignOff Sheet

**Approval Table**

| Row | Role | Name | Signature | Date | Comments |
|-----|------|------|-----------|------|----------|
| 2 | Assessor | | | | |
| 3 | IT Manager | | | | |
| 4 | HR Manager | | | | |
| 5 | CISO | | | | |

### Data Validations

| Field | Validation List |
|-------|-----------------|
| Implemented | Yes, Partial, No |
| Documented | Yes, No |
| Automated | Yes, No |
| Gap_Status | Gap, Compliant, Risk Accepted |
| Return_Required | Yes, No, Optional |
| Data_Wipe_Required | Yes, No, N/A |
| Employee_Type | Employee, Contractor, Consultant, Intern, Temp |
| Offboard_Reason | Resignation, Termination, Contract End, Transfer, Retirement, Other |
| Return_Status | Complete, In Progress, Pending, Overdue |
| Access_Revoked | Yes, No, Partial, N/A |
| Data_Wiped | Yes, No, Pending, N/A |
| Knowledge_Transfer | Complete, Partial, N/A |
| HR_Confirmed | Yes, No |
| Access_Type | Network, VPN, Email, Application, Database, Cloud, Physical, Admin |
| Verification_Method | AD Query, System Log, Login Attempt, Screenshot, Attestation, Certificate Check, Badge Scan |
| Evidence_Type | Document, Screenshot, Log, Form, Report, Certificate |

### Conditional Formatting Rules

**Return_Process Sheet**

| Condition | Format | Columns |
|-----------|--------|---------|
| Implemented = "No" | Red fill | D |
| Implemented = "Partial" | Yellow fill | D |
| Implemented = "Yes" | Green fill | D |
| Documented = "No" | Red text | E |
| Gap_Status = "Gap" | Red fill | I |

**Offboarding_Tracking Sheet**

| Condition | Format | Columns |
|-----------|--------|---------|
| Return_Status = "Overdue" | Red fill | L |
| Return_Status = "Complete" | Green fill | L |
| Access_Revoked = "No" | Red fill | M |
| Last_Working_Day < Today AND Return_Status <> "Complete" | Red border | Row |

**Access_Revocation Sheet**

| Condition | Format | Columns |
|-----------|--------|---------|
| SLA_Met = "No" | Red fill | J |
| SLA_Met = "Yes" | Green fill | J |
| Revocation_Date blank AND Last_Working_Day < Today | Red fill | I |

### Formula Specifications

**Return_Process Compliance Score**

```
=ROUND(SUMPRODUCT((D2:D19="Yes")*1,(D2:D19="Partial")*0.5)/18*100,1)
```

**Offboarding Completion Rate**

```
=ROUND(COUNTIF(L:L,"Complete")/COUNTA(A2:A1000)*100,1)
```

**Access Revocation SLA Compliance**

```
=ROUND(COUNTIF(J:J,"Yes")/COUNTA(J2:J1000)*100,1)
```

**Days Since Last Working Day**

```
=IF(G2="","",TODAY()-G2)
```

**Return Delta**

```
=J2-K2
```
(Assets Assigned - Assets Returned)

### Generator Reference

**Script**: `generate_a510_11_3_asset_return_offboarding.py`

**Location**: `10-isms-scr-base/isms-a.5.10-11-asset-usage-lifecycle/10_generator-master/`

**Dependencies**:
- openpyxl
- datetime
- logging

**Output**: `../90_workbooks/ISMS-IMP-A.5.10-11.3_Asset_Return_and_Offboarding_Assessment_YYYYMMDD.xlsx`

---

**END OF SPECIFICATION**

---

*"Trust, but verify."*
— Ronald Reagan

<!-- QA_VERIFIED: 2026-02-03 -->
