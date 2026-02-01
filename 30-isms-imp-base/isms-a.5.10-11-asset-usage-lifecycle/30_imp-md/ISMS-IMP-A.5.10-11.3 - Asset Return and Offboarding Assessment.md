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

## PART I: USER COMPLETION GUIDE

### Assessment Overview

**Purpose**

This workbook evaluates and tracks the organisation's asset return processes during employment termination, contract completion, or role changes. It ensures complete and verified return of organisational assets per ISO 27001:2022 Control A.5.11.

**Scope**

This assessment covers:
- Return process completeness assessment
- Standard asset return checklists
- Individual offboarding tracking
- Access revocation verification
- Return compliance monitoring

**What This Assessment Covers**

| Domain | Assessment Focus |
|--------|------------------|
| Process Assessment | Return procedures completeness |
| Asset Checklist | What must be returned |
| Offboarding Tracking | Individual departure tracking |
| Access Revocation | System access removal verification |

**Control Requirement**

ISO 27001:2022 A.5.11 states:

> "Personnel and other interested parties as appropriate should return all the organisation's assets in their possession upon change or termination of their employment, contract or agreement."

### Prerequisites

Before completing this assessment:

- [ ] Documented offboarding procedure
- [ ] Asset inventory linked to personnel records
- [ ] Access to HR termination notifications
- [ ] IT access revocation process documentation
- [ ] Historical offboarding records for review

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

Complete assessment metadata including review period.

**Step 2: Return Process Assessment (Return_Process Sheet)**

Evaluate each process requirement:

1. **Requirement_ID** - Pre-populated requirement reference
2. **Process_Requirement** - What the process should include
3. **Implemented** - Yes/Partial/No status
4. **Documented** - Whether procedure is documented
5. **Responsible_Role** - Who owns the process step
6. **SLA_Days** - Target completion timeframe
7. **Automated** - Whether process is automated

**Key Process Requirements**:

- Formal offboarding procedure documented
- Asset inventory linked to employee records
- Return checklist defined for each asset type
- IT notified upon termination notice
- Access revocation within 24 hours of last day
- Data wiping procedure for returned devices
- Knowledge transfer process defined
- Return completion sign-off obtained

**Step 3: Asset Checklist (Asset_Checklist Sheet)**

Define what must be returned for each asset type:

1. **Asset_Type** - Category of asset
2. **Return_Required** - Yes/No/Optional
3. **Verification_Method** - How return is verified
4. **Responsible_Team** - Who receives the asset
5. **SLA_Days** - Return deadline
6. **Data_Wipe_Required** - Whether data erasure needed

**Asset Categories**:

| Physical Assets | Digital Assets |
|-----------------|----------------|
| Laptop/Desktop | Network credentials |
| Mobile devices | Email account |
| Tokens/smart cards | Application accounts |
| Keys/badges | VPN certificates |
| Documents | Cloud service access |

**Step 4: Offboarding Tracking (Offboarding_Tracking Sheet)**

Track each individual departure:

1. **Employee_Name** - Person departing
2. **Department** - Their department
3. **Employee_Type** - Employee/Contractor/Consultant
4. **Last_Working_Day** - Final day
5. **Offboard_Reason** - Resignation/Termination/Contract End/etc.
6. **Assets_Assigned** - Count of assigned assets
7. **Assets_Returned** - Count of returned assets
8. **Return_Status** - Complete/In Progress/Pending/Overdue
9. **Access_Revoked** - Yes/No/Partial
10. **Sign_Off_Date** - Completion date

**Step 5: Access Revocation (Access_Revocation Sheet)**

Verify access removal for each system:

1. **Employee_Ref** - Link to offboarding record
2. **Access_Type** - Network/VPN/Email/Application/etc.
3. **System_Application** - Specific system name
4. **Last_Working_Day** - Reference date
5. **Revocation_Date** - When access was removed
6. **SLA_Met** - Yes/No (was it timely?)
7. **Verification_Method** - How removal was verified

**Verification Methods**:
- AD Query - Check Active Directory
- System Log - Review access logs
- Login Attempt - Verify login fails
- Screenshot - Capture disabled status
- Attestation - System owner confirmation

**Step 6: Evidence and Approval**

Complete evidence register and obtain sign-offs.

### Evidence Collection

**Required Evidence**:

| Evidence Type | Description | Storage Location |
|---------------|-------------|------------------|
| Offboarding Procedure | Documented process | ISMS Evidence Library |
| Return Forms | Signed asset return forms | ISMS Evidence Library |
| AD Exports | Access revocation verification | ISMS Evidence Library |
| Sign-off Records | Completion confirmations | ISMS Evidence Library |
| Exception Documentation | Any incomplete returns | ISMS Evidence Library |

### Common Pitfalls

❌ **MISTAKE**: Not tracking contractors and consultants separately
✅ **CORRECT**: Track all personnel types with appropriate processes

❌ **MISTAKE**: Only tracking physical assets, ignoring digital access
✅ **CORRECT**: Digital access revocation is equally critical

❌ **MISTAKE**: Waiting until after last day to start revocation
✅ **CORRECT**: Prepare revocation in advance; execute on/before last day

❌ **MISTAKE**: Not verifying data wipe for returned devices
✅ **CORRECT**: Confirm data erasure before device reissue

❌ **MISTAKE**: Missing remote worker return coordination
✅ **CORRECT**: Have shipping process for remote asset returns

❌ **MISTAKE**: No escalation for incomplete returns
✅ **CORRECT**: Define and execute escalation for outstanding items

❌ **MISTAKE**: Treating all terminations the same
✅ **CORRECT**: Immediate revocation for dismissals; planned for resignations

❌ **MISTAKE**: No knowledge transfer tracking
✅ **CORRECT**: Verify critical knowledge is transferred before departure

### Quality Checklist

Before submitting:

- [ ] All process requirements assessed
- [ ] Asset checklist covers all asset types
- [ ] Recent offboardings tracked (last 12 months sample)
- [ ] Access revocation verified with evidence
- [ ] SLA compliance calculated
- [ ] Outstanding items escalated appropriately
- [ ] Evidence linked for all completions
- [ ] Approvals obtained

### Review & Approval

**Review Workflow**:

1. Assessor completes process assessment
2. IT Manager verifies access revocation accuracy
3. HR Manager confirms offboarding compliance
4. CISO approves overall assessment

---

## PART II: TECHNICAL SPECIFICATION

### Workbook Architecture

**File Details**:

- Filename: `ISMS-IMP-A.5.10-11.3_Asset_Return_and_Offboarding_Assessment_YYYYMMDD.xlsx`
- Format: Microsoft Excel (.xlsx)
- Sheets: 7

### Sheet Specifications

#### Return_Process Sheet

**Columns**:

| Column | Header | Width | Content |
|--------|--------|-------|---------|
| A | Requirement_ID | 14 | Pre-populated (PR-001, etc.) |
| B | Process_Requirement | 45 | Pre-populated requirements |
| C | Category | 22 | Requirement category |
| D | Implemented | 14 | Data validation: Yes/Partial/No |
| E | Documented | 14 | Data validation: Yes/No |
| F | Responsible_Role | 22 | User input |
| G | SLA_Days | 12 | User input (numeric) |
| H | Automated | 14 | Data validation: Yes/No |
| I | Gap_Status | 16 | Data validation |
| J | Remediation_Notes | 35 | User input |
| K | Evidence_Ref | 18 | Evidence reference |

**Pre-populated Requirements**: 18 process requirements

#### Asset_Checklist Sheet

**Columns**:

| Column | Header | Width | Content |
|--------|--------|-------|---------|
| A | Asset_Type | 25 | Pre-populated types |
| B | Description | 40 | Asset description |
| C | Category | 18 | Hardware/Authentication/Digital/etc. |
| D | Return_Required | 16 | Data validation: Yes/No/Optional |
| E | Verification_Method | 25 | User input |
| F | Responsible_Team | 20 | User input |
| G | SLA_Days | 12 | User input |
| H | Data_Wipe_Required | 16 | Data validation: Yes/No/N/A |
| I | Disposal_If_Not_Returned | 25 | User input |
| J | Notes | 30 | User input |

**Pre-populated Asset Types**: 22 common asset types

#### Offboarding_Tracking Sheet

**Columns**:

| Column | Header | Width | Content |
|--------|--------|-------|---------|
| A | Offboard_ID | 14 | Auto-generated (OFF-001, etc.) |
| B | Employee_Name | 25 | User input |
| C | Department | 20 | User input |
| D | Employee_Type | 16 | Data validation |
| E | Last_Working_Day | 16 | Date field |
| F | Offboard_Reason | 18 | Data validation |
| G | Assets_Assigned | 14 | User input (numeric) |
| H | Assets_Returned | 14 | User input (numeric) |
| I | Return_Status | 16 | Data validation |
| J | Access_Revoked | 14 | Data validation |
| K | Data_Wiped | 14 | Data validation |
| L | Sign_Off_Date | 14 | Date field |
| M | HR_Confirmed | 14 | Data validation |
| N | Notes | 30 | User input |

#### Access_Revocation Sheet

**Columns**:

| Column | Header | Width | Content |
|--------|--------|-------|---------|
| A | Revocation_ID | 14 | Auto-generated (REV-001, etc.) |
| B | Employee_Ref | 18 | Link to Offboarding_Tracking |
| C | Access_Type | 22 | Data validation |
| D | System_Application | 28 | User input |
| E | Last_Working_Day | 16 | Date field |
| F | Revocation_Date | 16 | Date field |
| G | SLA_Met | 12 | Data validation: Yes/No |
| H | Revoked_By | 22 | User input |
| I | Verification_Method | 22 | Data validation |
| J | Verified_By | 22 | User input |
| K | Verification_Date | 16 | Date field |
| L | Notes | 30 | User input |

### Data Validations

| Field | Validation List |
|-------|-----------------|
| Employee_Type | Employee, Contractor, Consultant, Intern, Temp |
| Offboard_Reason | Resignation, Termination, Contract End, Transfer, Retirement, Other |
| Return_Status | Complete, In Progress, Pending, Overdue |
| Access_Revoked | Yes, No, Partial, N/A |
| Access_Type | Network, VPN, Email, Application, Database, Cloud, Physical, Admin |
| Verification_Method | AD Query, System Log, Login Attempt, Screenshot, Attestation |

### Generator Reference

**Script**: `generate_a510_11_3_asset_return_offboarding.py`

**Location**: `10-isms-scr-base/isms-a.5.10-11-asset-usage-lifecycle/10_generator-master/`

---

**END OF SPECIFICATION**

---

*"Trust, but verify."*
— Ronald Reagan

<!-- QA_VERIFIED: 2026-02-01 -->
