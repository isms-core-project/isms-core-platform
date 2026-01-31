# ISMS-IMP-A.8.32.2 - Change Types & Categories Assessment
## Excel Workbook Layout Specification
### ISO/IEC 27001:2022 Control A.8.32: Change Management

---

## Document Overview

**Document ID:** ISMS-IMP-A.8.32.2  
**Assessment Area:** Change Types, Categories & Risk Classification  
**Related Policy:** ISMS-POL-A.8.32-S2.2 (Change Classification Requirements)  
**Purpose:** Document standard/normal/emergency change types, assess classification procedures, and evaluate risk-based categorization in a technology-agnostic manner

**Key Principle:** This assessment is **technology-independent**. Organizations document THEIR specific change classification approach and verify procedures against generic requirements.

---

## Workbook Structure

### Sheet 1: Instructions & Legend

#### Header Section
- **Title:** "ISMS-IMP-A.8.32.2 – Change Types & Categories Assessment"
- **Subtitle:** "ISO/IEC 27001:2022 - Control A.8.32: Change Management"
- **Styling:** Dark blue header (003366), white text, centered, 40px height

#### Document Information Block
```
Document ID:           ISMS-IMP-A.8.32.2
Assessment Area:       Change Types & Categories
Related Policy:        ISMS-POL-A.8.32-S2.2
Version:               1.0
Assessment Date:       [USER INPUT - yellow cell]
Completed By:          [USER INPUT - yellow cell]
Organization:          [Organization]
Review Cycle:          Quarterly
```

#### How to Use This Workbook
1. Complete the Standard_Changes_Catalog with YOUR pre-approved changes
2. Document YOUR normal change assessment criteria
3. Define YOUR emergency change triggers and procedures
4. Configure YOUR change risk classification matrix
5. Document YOUR change calendar management approach
6. Review the Summary_Dashboard for compliance metrics
7. Maintain the Evidence Register for audit traceability
8. Obtain final approval and sign-off

#### Status Legend
| Symbol | Status | Description | Color Code |
|--------|--------|-------------|------------|
| ✅ | Defined | Criteria/process clearly defined and documented | Green (C6EFCE) |
| ⚠️ | Partial | Partially defined or inconsistent application | Yellow (FFEB9C) |
| ❌ | Not Defined | Not defined or not documented | Red (FFC7CE) |
| 📋 | Planned | Definition planned with target date | Blue (B4C7E7) |
| N/A | Not Applicable | Not applicable to this environment | Gray |

#### Change Type Decision Tree
```
Is this change:
├─ Pre-approved, low-risk, well-documented? → STANDARD CHANGE
├─ Requires assessment and approval? → NORMAL CHANGE
│   ├─ Low Risk + Low Impact → Expedited Normal Change
│   ├─ Medium Risk/Impact → Standard Normal Change
│   └─ High/Critical Risk/Impact → High-Priority Normal Change
└─ Urgent, meets emergency criteria? → EMERGENCY CHANGE
    ├─ Critical system outage?
    ├─ Security incident?
    ├─ Data loss prevention?
    └─ Regulatory deadline?
```

#### Acceptable Evidence (Examples)
- ✓ Standard changes catalog/library
- ✓ Change classification decision trees
- ✓ Risk assessment matrices
- ✓ Emergency change criteria documentation
- ✓ Change calendar procedures
- ✓ CAB meeting records (classification decisions)
- ✓ Change metrics (by type and category)
- ✓ Training materials on change classification
- ✓ Audit reports on classification accuracy
- ✓ Exception/deviation records
- ✓ Change type definitions document
- ✓ Historical change data (by type)

---

## Sheet 2: Standard_Changes_Catalog

### Purpose
Document all pre-approved standard changes that can be executed without CAB approval.

### Header Section
**Row 1:** "STANDARD CHANGES CATALOG"  
**Row 2:** "Pre-approved, low-risk changes with documented procedures"

### Standard Change Register (Rows 4-53, 50 entries)

| Change ID | Change Title | Description | Category | Frequency | Pre-requisites | Procedure Location | Owner | Approval Date | Review Date | Risk Level | Status | Evidence |
|-----------|--------------|-------------|----------|-----------|----------------|-------------------|-------|---------------|-------------|------------|--------|----------|
| STD-001 | [User defines] | Text | Dropdown: Infrastructure/Application/Security/Data/Network/Other | Dropdown: Daily/Weekly/Monthly/Quarterly/On-Demand | Text | Text (URL/path) | Text | Date | Date | Dropdown: Low/Medium | Dropdown: ✅ Active/⚠️ Under Review/❌ Retired/📋 Proposed | Text |

**Column Specifications:**

#### Column: Change ID
- **Data Type:** Text (auto-suggest STD-NNN format)
- **Required:** Yes
- **Width:** 12
- **Description:** Unique identifier for standard change
- **Example:** STD-001, STD-002, etc.

#### Column: Change Title
- **Data Type:** Text
- **Required:** Yes
- **Width:** 30
- **Description:** Short, descriptive title
- **Example:** "Password Reset - End User", "Patch Deployment - Workstations"

#### Column: Description
- **Data Type:** Text (long)
- **Required:** Yes
- **Width:** 40
- **Description:** Full description of the change
- **Example:** "Reset end user password in Active Directory following identity verification"

#### Column: Category
- **Data Type:** Dropdown
- **Required:** Yes
- **Width:** 18
- **Validation:** Infrastructure, Application, Security, Data, Network, Cloud, User Access, Configuration, Other
- **Description:** Type of change for classification purposes

#### Column: Frequency
- **Data Type:** Dropdown
- **Required:** Yes
- **Width:** 15
- **Validation:** Daily, Weekly, Monthly, Quarterly, Annual, On-Demand, Rare
- **Description:** How often this change typically occurs

#### Column: Pre-requisites
- **Data Type:** Text
- **Required:** No
- **Width:** 30
- **Description:** Conditions that must be met before executing
- **Example:** "User identity verified via two-factor authentication"

#### Column: Procedure Location
- **Data Type:** Text
- **Required:** Yes
- **Width:** 30
- **Description:** Where detailed procedure is documented
- **Example:** "Wiki: /IT/Procedures/Password-Reset", "ServiceNow KB12345"

#### Column: Owner
- **Data Type:** Text
- **Required:** Yes
- **Width:** 20
- **Description:** Role or person responsible for this standard change
- **Example:** "Service Desk Team", "Network Operations"

#### Column: Approval Date
- **Data Type:** Date (DD.MM.YYYY)
- **Required:** Yes
- **Width:** 15
- **Description:** When this change was approved as standard

#### Column: Review Date
- **Data Type:** Date (DD.MM.YYYY)
- **Required:** Yes
- **Width:** 15
- **Description:** Next scheduled review (typically annually)

#### Column: Risk Level
- **Data Type:** Dropdown
- **Required:** Yes
- **Width:** 15
- **Validation:** Low, Medium (requires justification)
- **Description:** Only Low and Medium risk changes qualify as Standard
- **Note:** High/Critical changes CANNOT be Standard Changes per policy

#### Column: Status
- **Data Type:** Dropdown
- **Required:** Yes
- **Width:** 18
- **Validation:** ✅ Active, ⚠️ Under Review, ❌ Retired, 📋 Proposed
- **Description:** Current status of this standard change

#### Column: Evidence
- **Data Type:** Text
- **Required:** No
- **Width:** 25
- **Description:** Reference to evidence (procedure docs, approvals, etc.)

### Standard Change Summary Metrics (Rows 55-62)

| Metric | Value | Notes |
|--------|-------|-------|
| Total Standard Changes Defined | [Formula: COUNT] | [Text - editable] |
| Active Standard Changes | [Formula: COUNTIF Status=Active] | [Text] |
| Standard Changes Under Review | [Formula: COUNTIF Status=Review] | [Text] |
| Standard Changes Requiring Annual Review | [Formula: COUNT where Review Date < TODAY] | [Text] |
| Most Common Category | [Formula: MODE of Category] | [Text] |
| Average Age of Standard Changes | [Formula: Average of (TODAY - Approval Date)] | [Text] |

---

## Sheet 3: Normal_Changes_Assessment

### Purpose
Document criteria and procedures for normal (non-standard, non-emergency) changes.

### Header Section
**Row 1:** "NORMAL CHANGES ASSESSMENT"  
**Row 2:** "Changes requiring risk assessment, approval, and CAB review"

### Normal Change Criteria (Rows 4-20)

| Criterion | Defined | Documentation Reference | Assessment Method | Responsible Role | Compliance | Evidence |
|-----------|---------|------------------------|-------------------|------------------|------------|----------|
| Change does not meet Standard criteria | Dropdown: ✅/⚠️/❌/📋 | Text | Text | Text | Dropdown: ✅ Yes/⚠️ Partial/❌ No | Text |
| Change is not an emergency | Dropdown | Text | Text | Text | Dropdown | Text |
| Risk assessment required | Dropdown | Text | Text | Text | Dropdown | Text |
| Impact assessment required | Dropdown | Text | Text | Text | Dropdown | Text |
| CAB review required (based on risk) | Dropdown | Text | Text | Text | Dropdown | Text |
| Business justification required | Dropdown | Text | Text | Text | Dropdown | Text |
| Implementation plan required | Dropdown | Text | Text | Text | Dropdown | Text |
| Test plan required | Dropdown | Text | Text | Text | Dropdown | Text |
| Rollback plan required | Dropdown | Text | Text | Text | Dropdown | Text |
| Communication plan required | Dropdown | Text | Text | Text | Dropdown | Text |
| PIR (Post-Implementation Review) required | Dropdown | Text | Text | Text | Dropdown | Text |
| Change window scheduling required | Dropdown | Text | Text | Text | Dropdown | Text |

[15 rows total for normal change criteria]

### Risk-Based Approval Paths (Rows 22-35)

| Risk Category | Impact Category | Approval Authority | CAB Review | Typical Timeline | Success Rate | Documented | Evidence |
|---------------|----------------|-------------------|------------|------------------|-------------|------------|----------|
| Low | Low | Dropdown: Change Manager/CAB/Service Owner/CISO/Other | Dropdown: Mandatory/Recommended/Optional/Not Required | Text (e.g., "2-3 days") | Text (e.g., "95%") | Dropdown: ✅/⚠️/❌/📋 | Text |
| Low | Medium | Dropdown | Dropdown | Text | Text | Dropdown | Text |
| Low | High | Dropdown | Dropdown | Text | Text | Dropdown | Text |
| Medium | Low | Dropdown | Dropdown | Text | Text | Dropdown | Text |
| Medium | Medium | Dropdown | Dropdown | Text | Text | Dropdown | Text |
| Medium | High | Dropdown | Dropdown | Text | Text | Dropdown | Text |
| High | Low | Dropdown | Dropdown | Text | Text | Dropdown | Text |
| High | Medium | Dropdown | Dropdown | Text | Text | Dropdown | Text |
| High | High | Dropdown | Dropdown: Mandatory (always) | Text | Text | Dropdown | Text |
| Critical | Any | Dropdown: Multiple approvers required | Dropdown: Mandatory | Text | Text | Dropdown | Text |

### Normal Change Workflow Stages (Rows 37-50)

| Stage | Stage Name | Required for All Normal Changes | Exceptions Allowed | Exception Approval | Documented | Evidence |
|-------|------------|-------------------------------|-------------------|-------------------|------------|----------|
| 1 | Change Request Submission | Dropdown: ✅ Yes/❌ No | Dropdown: ✅ Yes/❌ No | Text (who can approve exception) | Dropdown: ✅/⚠️/❌/📋 | Text |
| 2 | Risk Assessment | Dropdown | Dropdown | Text | Dropdown | Text |
| 3 | Impact Assessment | Dropdown | Dropdown | Text | Dropdown | Text |
| 4 | Change Classification | Dropdown | Dropdown | Text | Dropdown | Text |
| 5 | CAB Scheduling | Dropdown | Dropdown | Text | Dropdown | Text |
| 6 | CAB Review | Dropdown | Dropdown | Text | Dropdown | Text |
| 7 | Formal Approval | Dropdown | Dropdown | Text | Dropdown | Text |
| 8 | Implementation Planning | Dropdown | Dropdown | Text | Dropdown | Text |
| 9 | Testing (pre-implementation) | Dropdown | Dropdown | Text | Dropdown | Text |
| 10 | Stakeholder Notification | Dropdown | Dropdown | Text | Dropdown | Text |
| 11 | Implementation | Dropdown | Dropdown | Text | Dropdown | Text |
| 12 | Verification | Dropdown | Dropdown | Text | Dropdown | Text |
| 13 | Post-Implementation Review | Dropdown | Dropdown | Text | Dropdown | Text |

---

## Sheet 4: Emergency_Changes

### Purpose
Document emergency change criteria, procedures, and governance.

### Header Section
**Row 1:** "EMERGENCY CHANGES"  
**Row 2:** "Urgent changes meeting specific emergency criteria with E-CAB approval"

### Emergency Criteria Definition (Rows 4-15)

| Emergency Criterion | Defined | Specific Triggers | Escalation Path | Response Time SLA | Documented | Evidence |
|--------------------|---------|-------------------|-----------------|-------------------|------------|----------|
| System Outage (Critical Services) | Dropdown: ✅ Clearly Defined/⚠️ Partially/❌ Not Defined | Text (e.g., "Complete loss of email service >1000 users") | Text (e.g., "NOC → IT Ops Manager → CIO") | Text (e.g., "E-CAB within 30 min") | Dropdown: ✅/⚠️/❌/📋 | Text |
| Security Incident Response | Dropdown | Text | Text | Text | Dropdown | Text |
| Data Loss Prevention | Dropdown | Text | Text | Text | Dropdown | Text |
| Regulatory Compliance Deadline | Dropdown | Text | Text | Text | Dropdown | Text |
| Health & Safety Risk | Dropdown | Text | Text | Text | Dropdown | Text |
| Business Continuity Threat | Dropdown | Text | Text | Text | Dropdown | Text |
| [Custom Criterion 1] | Dropdown | Text | Text | Text | Dropdown | Text |
| [Custom Criterion 2] | Dropdown | Text | Text | Text | Dropdown | Text |

### Emergency Change Process Requirements (Rows 17-30)

| Requirement | Implemented | Process Description | Responsible Role | Exceptions Allowed | Compliance | Evidence |
|-------------|-------------|---------------------|------------------|-------------------|------------|----------|
| Emergency criteria must be met | Dropdown: ✅ Yes/⚠️ Partial/❌ No | Text | Text | Dropdown: ✅ Yes/❌ No/N/A | Dropdown: ✅/⚠️/❌ | Text |
| E-CAB convened | Dropdown | Text (how E-CAB is convened) | Text | Dropdown | Dropdown | Text |
| Minimum E-CAB members defined | Dropdown | Text (who must participate) | Text | Dropdown | Dropdown | Text |
| Emergency approval documented | Dropdown | Text | Text | Dropdown | Dropdown | Text |
| Risk acceptance explicit | Dropdown | Text | Text | Dropdown | Dropdown | Text |
| Communication immediate | Dropdown | Text | Text | Dropdown | Dropdown | Text |
| Implementation window immediate | Dropdown | Text | Text | Dropdown | Dropdown | Text |
| Rollback plan prepared (where feasible) | Dropdown | Text | Text | Dropdown | Dropdown | Text |
| Incident ticket linked | Dropdown | Text | Text | Dropdown | Dropdown | Text |
| Mandatory PIR within 2 business days | Dropdown | Text | Text | Dropdown: ❌ No Exceptions | Dropdown | Text |
| Retrospective CAB review | Dropdown | Text | Text | Dropdown | Dropdown | Text |
| Emergency change metrics tracked | Dropdown | Text | Text | Dropdown | Dropdown | Text |

### Emergency Change Metrics (Rows 32-42)

| Metric | Target | Current (Last Quarter) | Status | Notes |
|--------|--------|----------------------|--------|-------|
| Emergency changes as % of total changes | Text (e.g., "<5%") | Text (formula: [emergency count / total changes]) | Formula: Green/Yellow/Red based on target | Text (editable) |
| Average E-CAB response time | Text (e.g., "<30 minutes") | Text | Formula | Text |
| Emergency changes with PIR completed | Text (e.g., "100%") | Text (formula) | Formula | Text |
| Emergency changes leading to incidents | Text (e.g., "<10%") | Text | Formula | Text |
| Retrospective CAB review completion | Text (e.g., "100%") | Text | Formula | Text |
| False emergency declarations | Text (e.g., "<5%") | Text | Formula | Text |
| Emergency change success rate | Text (e.g., ">90%") | Text | Formula | Text |

### E-CAB (Emergency Change Advisory Board) (Rows 44-55)

| E-CAB Aspect | Configuration | Details | Documented | Evidence |
|-------------|--------------|---------|------------|----------|
| E-CAB Member Roles | Text (list of roles) | Text (names if applicable, or "per on-call rotation") | Dropdown: ✅/⚠️/❌/📋 | Text |
| Minimum quorum | Number | Text (e.g., "3 of 5 members") | Dropdown | Text |
| Convening method | Dropdown: Conference Call/Video/IM Group/Emergency Hotline/Other | Text | Dropdown | Text |
| Availability requirement | Text (e.g., "24/7 on-call rotation") | Text | Dropdown | Text |
| Decision authority | Text (e.g., "IT Ops Manager has final say") | Text | Dropdown | Text |
| Documentation requirements | Text | Text | Dropdown | Text |
| Escalation if E-CAB unavailable | Text | Text | Dropdown | Text |

---

## Sheet 5: Change_Risk_Classification

### Purpose
Document the risk classification matrix and assessment methodology.

### Header Section
**Row 1:** "CHANGE RISK CLASSIFICATION MATRIX"  
**Row 2:** "Risk = Impact × Likelihood methodology"

### Impact Level Definitions (Rows 4-12)

| Impact Level | User Count Affected | Service Downtime Potential | Recovery Time | Data Loss Risk | Financial Impact | Documented | Evidence |
|--------------|-------------------|-------------------------|---------------|----------------|------------------|------------|----------|
| Low | Dropdown: <10 users/10-50/50-100/Other | Dropdown: <15 min/15-60 min/1-2 hours/Other | Text (e.g., "<15 min") | Dropdown: None/Minimal/Moderate/High | Text (e.g., "<€1,000") | Dropdown: ✅/⚠️/❌/📋 | Text |
| Medium | Dropdown | Dropdown | Text | Dropdown | Text | Dropdown | Text |
| High | Dropdown | Dropdown | Text | Dropdown | Text | Dropdown | Text |
| Critical | Dropdown: >1000 users/All users/Business-critical/Other | Dropdown: >8 hours/Irreversible/Business-critical/Other | Text (e.g., ">8 hours or permanent") | Dropdown | Text (e.g., ">€100,000") | Dropdown | Text |

### Likelihood Level Definitions (Rows 14-20)

| Likelihood Level | Failure Probability | Complexity | Dependencies | Testing Maturity | Historical Success Rate | Documented | Evidence |
|-----------------|-------------------|------------|--------------|-----------------|----------------------|------------|----------|
| Low | Text (e.g., "<10%") | Dropdown: Simple/Moderate/Complex/Very Complex | Text (e.g., "Single system, no external dependencies") | Dropdown: Extensively Tested/Well Tested/Limited Testing/Untested | Text (e.g., ">95%") | Dropdown: ✅/⚠️/❌/📋 | Text |
| Medium | Text (e.g., "10-30%") | Dropdown | Text | Dropdown | Text | Dropdown | Text |
| High | Text (e.g., ">30%") | Dropdown | Text | Dropdown | Text | Dropdown | Text |

### Risk Matrix (Impact × Likelihood) (Rows 22-28)

|  | **Low Impact** | **Medium Impact** | **High Impact** | **Critical Impact** |
|--|----------------|-------------------|----------------|-------------------|
| **Low Likelihood** | LOW RISK (Green) | LOW RISK (Green) | MEDIUM RISK (Yellow) | HIGH RISK (Orange) |
| **Medium Likelihood** | LOW RISK (Green) | MEDIUM RISK (Yellow) | HIGH RISK (Orange) | CRITICAL RISK (Red) |
| **High Likelihood** | MEDIUM RISK (Yellow) | HIGH RISK (Orange) | CRITICAL RISK (Red) | CRITICAL RISK (Red) |

**Color Coding:**
- Green (C6EFCE): LOW RISK - Expedited approval possible
- Yellow (FFEB9C): MEDIUM RISK - Standard CAB review
- Orange (FFD966): HIGH RISK - Enhanced scrutiny, senior approval
- Red (FFC7CE): CRITICAL RISK - CISO/CIO approval required

### Risk Assessment Process (Rows 30-42)

| Process Step | Implemented | Process Description | Tool/Method | Responsible Role | Compliance | Evidence |
|-------------|-------------|---------------------|------------|------------------|------------|----------|
| Impact assessment performed | Dropdown: ✅ Always/⚠️ Sometimes/❌ Never | Text | Text (e.g., "Change request form, section 3") | Text | Dropdown: ✅/⚠️/❌ | Text |
| Likelihood assessment performed | Dropdown | Text | Text | Text | Dropdown | Text |
| Risk score calculated | Dropdown | Text (formula/method) | Text | Text | Dropdown | Text |
| Risk score documented | Dropdown | Text | Text | Text | Dropdown | Text |
| Risk mitigation identified | Dropdown | Text | Text | Text | Dropdown | Text |
| Residual risk assessed | Dropdown | Text | Text | Text | Dropdown | Text |
| Risk acceptance documented | Dropdown | Text | Text | Text | Dropdown | Text |
| Risk review at PIR | Dropdown | Text | Text | Text | Dropdown | Text |

### Risk Trends (Rows 44-52)

| Metric | Last Quarter | Current Quarter | Trend | Target | Status |
|--------|--------------|----------------|-------|--------|--------|
| % Low Risk Changes | Text (editable) | Text (editable) | Formula (↑/↓/→) | Text | Formula (Green/Yellow/Red) |
| % Medium Risk Changes | Text | Text | Formula | Text | Formula |
| % High Risk Changes | Text | Text | Formula | Text | Formula |
| % Critical Risk Changes | Text | Text | Formula | Text | Formula |
| Risk Assessment Accuracy | Text (e.g., "85%") | Text | Formula | Text (e.g., ">90%") | Formula |
| Changes failing due to risk | Text | Text | Formula | Text (e.g., "<5%") | Formula |

---

## Sheet 6: Change_Calendar_Management

### Purpose
Document change calendar management, blackout windows, and scheduling procedures.

### Header Section
**Row 1:** "CHANGE CALENDAR MANAGEMENT"  
**Row 2:** "Scheduling, blackout windows, and conflict detection"

### Change Window Definitions (Rows 4-15)

| Change Window | Days/Times | Applicable Change Types | Approval Required | Advance Notice | Documented | Evidence |
|--------------|------------|------------------------|-------------------|----------------|------------|----------|
| Standard Maintenance Window | Text (e.g., "Saturday 02:00-06:00 CET") | Dropdown: All/Standard Only/Normal Only/Emergency Only/Custom | Dropdown: Yes/No | Text (e.g., "5 business days") | Dropdown: ✅/⚠️/❌/📋 | Text |
| Business Hours (Restricted) | Text (e.g., "Monday-Friday 08:00-18:00 CET") | Dropdown | Dropdown | Text | Dropdown | Text |
| After-Hours Window | Text | Dropdown | Dropdown | Text | Dropdown | Text |
| Emergency Window | Text (e.g., "Anytime - as needed") | Dropdown: Emergency Only | Dropdown | Text (e.g., "Immediate") | Dropdown | Text |
| [Custom Window 1] | Text | Dropdown | Dropdown | Text | Dropdown | Text |
| [Custom Window 2] | Text | Dropdown | Dropdown | Text | Dropdown | Text |

### Blackout Periods (Rows 17-30)

| Blackout Period | Start Date | End Date | Reason | Affected Systems/Services | Exceptions Allowed | Exception Approver | Documented | Evidence |
|----------------|-----------|----------|--------|--------------------------|-------------------|-------------------|------------|----------|
| Year-End Freeze | Date (DD.MM.YYYY) | Date (DD.MM.YYYY) | Dropdown: Financial Close/Holiday Period/Peak Business/Audit/Other | Text | Dropdown: Yes/No/Emergency Only | Text (role) | Dropdown: ✅/⚠️/❌/📋 | Text |
| [Recurring - specify] | Date | Date | Dropdown | Text | Dropdown | Text | Dropdown | Text |

[12 rows for blackout periods - covering annual cycle]

### Change Calendar Procedures (Rows 32-45)

| Procedure | Implemented | Process Description | Tool/System | Responsible Role | Compliance | Evidence |
|-----------|-------------|---------------------|------------|------------------|------------|----------|
| Change calendar maintained | Dropdown: ✅ Yes/⚠️ Partial/❌ No | Text | Text (tool name) | Text | Dropdown: ✅/⚠️/❌ | Text |
| Changes scheduled in calendar | Dropdown | Text | Text | Text | Dropdown | Text |
| Conflict detection automated | Dropdown | Text | Text | Text | Dropdown | Text |
| Blackout periods enforced | Dropdown | Text | Text | Text | Dropdown | Text |
| Calendar visible to stakeholders | Dropdown | Text | Text | Text | Dropdown | Text |
| Calendar synchronization (if multiple systems) | Dropdown | Text | Text | Text | Dropdown | Text |
| Change window utilization tracked | Dropdown | Text | Text | Text | Dropdown | Text |
| Scheduling conflicts escalated | Dropdown | Text | Text | Text | Dropdown | Text |

### Conflict Detection & Resolution (Rows 47-58)

| Conflict Type | Detection Method | Resolution Process | Escalation Path | Documented | Evidence |
|--------------|------------------|-------------------|-----------------|------------|----------|
| Overlapping change windows | Dropdown: Automated/Manual/None | Text | Text | Dropdown: ✅/⚠️/❌/📋 | Text |
| Resource conflicts (same team) | Dropdown | Text | Text | Dropdown | Text |
| Dependency conflicts | Dropdown | Text | Text | Dropdown | Text |
| Blackout period violations | Dropdown | Text | Text | Dropdown | Text |
| Same system multiple changes | Dropdown | Text | Text | Dropdown | Text |

### Change Calendar Metrics (Rows 60-68)

| Metric | Target | Current | Status | Notes |
|--------|--------|---------|--------|-------|
| Changes scheduled in advance (>5 days) | Text (e.g., ">80%") | Text | Formula | Text |
| Blackout period violations | Text (e.g., "<2%") | Text | Formula | Text |
| Emergency changes bypassing schedule | Text (e.g., "<5%") | Text | Formula | Text |
| Change window utilization | Text (e.g., "60-80%") | Text | Formula | Text |
| Conflicts detected and resolved | Text (e.g., "100%") | Text | Formula | Text |

---

## Sheet 7: Summary_Dashboard

### Purpose
Aggregate compliance metrics and identify gaps across all change type assessments.

### Header Section
**Row 1:** "CHANGE TYPES & CATEGORIES - SUMMARY DASHBOARD"  
**Row 2:** "Overall compliance status and key findings"

### Overall Compliance Summary (Rows 4-12)

| Assessment Area | Total Criteria | Defined | Partial | Not Defined | Compliance % | Status |
|-----------------|---------------|---------|---------|-------------|--------------|--------|
| Standard Changes Catalog | Formula | Formula | Formula | Formula | Formula | Formula: Green/Yellow/Red |
| Normal Changes Criteria | Formula | Formula | Formula | Formula | Formula | Formula |
| Emergency Change Procedures | Formula | Formula | Formula | Formula | Formula | Formula |
| Risk Classification Matrix | Formula | Formula | Formula | Formula | Formula | Formula |
| Change Calendar Management | Formula | Formula | Formula | Formula | Formula | Formula |
| **OVERALL TOTAL** | Formula | Formula | Formula | Formula | Formula | Formula |

### Policy Requirement Mapping (Rows 14-28)

| Policy Req ID | Requirement Summary | Status | Evidence Sheet | Evidence Row | Auditor Notes |
|--------------|---------------------|--------|----------------|--------------|---------------|
| REQ-CLASSIFY-001 | Standard changes catalog maintained | Formula: ✅/⚠️/❌ | Text | Text | Text (editable) |
| REQ-CLASSIFY-002 | Standard change pre-approval | Formula | Text | Text | Text |
| REQ-CLASSIFY-003 | Normal change assessment criteria | Formula | Text | Text | Text |
| REQ-CLASSIFY-004 | Emergency criteria defined | Formula | Text | Text | Text |
| REQ-CLASSIFY-005 | Risk-based categorization | Formula | Text | Text | Text |
| REQ-CLASSIFY-006 | Impact assessment methodology | Formula | Text | Text | Text |
| REQ-CLASSIFY-007 | Likelihood assessment methodology | Formula | Text | Text | Text |
| REQ-CLASSIFY-008 | Risk matrix documented | Formula | Text | Text | Text |
| REQ-CLASSIFY-009 | Change calendar management | Formula | Text | Text | Text |
| REQ-CLASSIFY-010 | Blackout periods defined | Formula | Text | Text | Text |
| REQ-CLASSIFY-011 | E-CAB procedures | Formula | Text | Text | Text |
| REQ-CLASSIFY-012 | Classification metrics tracked | Formula | Text | Text | Text |

### Change Distribution Analysis (Rows 30-38)

| Metric | Current | Target | Status | Notes |
|--------|---------|--------|--------|-------|
| Standard Changes (%) | Formula from Sheet 2 | Text (e.g., "40-60%") | Formula | Text |
| Normal Changes (%) | Formula | Text (e.g., "35-55%") | Formula | Text |
| Emergency Changes (%) | Formula | Text (e.g., "<5%") | Formula | Text |
| Total Active Standard Changes | Formula | Text | Formula | Text |
| Standard Changes Requiring Review | Formula | Text | Formula | Text |
| Classification Accuracy | Text (e.g., "Current: 92%") | Text (e.g., ">90%") | Formula | Text |

### Critical Findings (Rows 40-45)

| Finding Type | Count | Description |
|--------------|-------|-------------|
| Critical Gaps | Formula (count ❌) | Text area (auto-populate key gaps) |
| High-Priority Items | Formula (count ⚠️) | Text area |
| Planned Improvements | Formula (count 📋) | Text area |

### Audit Readiness Assessment (Rows 47-54)

| Criterion | Status | Notes |
|-----------|--------|-------|
| All change types clearly defined | Formula: ✅/⚠️/❌ | Text |
| Standard changes catalog complete | Formula | Text |
| Risk classification methodology documented | Formula | Text |
| Emergency procedures documented | Formula | Text |
| Evidence available for all criteria | Formula | Text |
| Compliance ≥70% | Formula | Text |
| **OVERALL AUDIT READINESS** | Formula | Text |

---

## Sheet 8: Evidence_Register

### Purpose
Centralized evidence repository linking to all supporting documentation.

### Header Section
**Row 1:** "EVIDENCE REGISTER"  
**Row 2:** "Document all evidence supporting this assessment"

### Evidence Inventory (Rows 4-103, 100 rows)

| Evidence ID | Evidence Type | Description | Related Sheet/Requirement | Location/Path | Date Collected | Collected By | Verification Status | Auditor Notes |
|-------------|---------------|-------------|--------------------------|---------------|----------------|--------------|-------------------|---------------|
| EV-001 | Dropdown: Catalog/Procedure/Criteria Doc/Risk Matrix/Calendar/Meeting Minutes/Metrics Report/Approval Record/Training Material/Other | Text | Dropdown: (all sheets + REQ-IDs) | Text | Date (DD.MM.YYYY) | Text | Dropdown: ✅ Verified/⚠️ Pending/❌ Not Verified | Text |

[100 rows for evidence tracking with alternating row colors for readability]

**Column Widths:**
- Evidence ID: 12
- Evidence Type: 18
- Description: 40
- Related Sheet/Requirement: 25
- Location/Path: 30
- Date Collected: 15
- Collected By: 20
- Verification Status: 18
- Auditor Notes: 30

---

## Sheet 9: Approval_Sign_Off

### Purpose
Formal approval workflow for completed assessment.

### Assessment Summary Section (Rows 3-10)
```
Assessment Document:        ISMS-IMP-A.8.32.2 - Change Types & Categories Assessment
Assessment Period:          [USER INPUT - date range]
Assessment Scope:           [USER INPUT - text]
Overall Compliance Rate:    [Formula from Summary_Dashboard]
Critical Gaps:              [Formula from Summary_Dashboard]
Audit Readiness:            [Formula from Summary_Dashboard]
Assessment Status:          [Dropdown: ✅ Final/⚠️ Requires Remediation/📋 Draft/❌ Re-assessment Required]
```

### Assessment Completed By (Rows 12-20)
```
Name:               [USER INPUT]
Role/Title:         [USER INPUT]
Department:         [USER INPUT]
Email:              [USER INPUT]
Phone:              [USER INPUT]
Date Completed:     [USER INPUT - date picker, format DD.MM.YYYY]
Signature:          [USER INPUT]
```

### Reviewed By - Change Manager (Rows 22-30)
```
Name:                   [USER INPUT]
Role/Title:             [USER INPUT]
Review Date:            [USER INPUT - date picker, format DD.MM.YYYY]
Review Notes:           [Text area - merged cells]
Recommendation:         [Dropdown: ✅ Approve/⚠️ Approve with Conditions/❌ Reject/📋 Require Rework]
Conditions (if any):    [Text area]
Signature:              [USER INPUT]
```

### Approved By - CISO or IT Operations Manager (Rows 32-40)
```
Name:                   [USER INPUT]
Role/Title:             [USER INPUT]
Approval Date:          [USER INPUT - date picker, format DD.MM.YYYY]
Approval Decision:      [Dropdown: ✅ Approved/⚠️ Approved with Conditions/❌ Rejected]
Conditions/Notes:       [Text area]
Signature:              [USER INPUT]
```

### Next Review Details (Rows 42-48)
```
Next Review Date:               [Date - auto-calculate +3 months from Approval Date]
Review Responsible:             [USER INPUT]
Special Considerations:         [Text area]
Regulatory Review Required:     [Dropdown: Yes/No/To Be Determined]
External Audit Scheduled:       [Date]
```

---

## Cell Styling Reference

### Header Styles
- **Main Header (Row 1):** Font: Calibri 14pt bold white, Fill: 003366 (dark blue), Alignment: centered/wrapped, Height: 40px
- **Subheader (Row 2):** Font: Calibri 11pt bold white, Fill: 4472C4 (medium blue), Alignment: centered/wrapped, Height: 25px
- **Section Header:** Font: Calibri 11pt bold white, Fill: 4472C4 (light blue), Alignment: center, Height: 20px
- **Column Header:** Font: Calibri 10pt bold black, Fill: D9D9D9 (light gray), Alignment: centered/wrapped, Border: thin all sides

### Input Cell Styles
- **Editable (User Input):** Fill: FFFFCC (light yellow), Border: thin black, Alignment: left/wrap
- **Calculated/Formula:** Fill: E0E0E0 (light gray), Border: thin black, Protection: locked
- **Dropdown:** Fill: FFFFCC (light yellow), Border: thin black, Data validation applied

### Status Color Coding
- **✅ Defined/Compliant:** C6EFCE (light green)
- **⚠️ Partial/Requires Attention:** FFEB9C (light yellow)
- **❌ Not Defined/Non-Compliant:** FFC7CE (light red)
- **📋 Planned:** B4C7E7 (light blue)
- **N/A:** F2F2F2 (light gray)

### Risk Level Colors
- **LOW RISK:** C6EFCE (green)
- **MEDIUM RISK:** FFEB9C (yellow)
- **HIGH RISK:** FFD966 (orange)
- **CRITICAL RISK:** FFC7CE (red)

---

## Freeze Panes

- **All assessment sheets:** Freeze at row 4 (headers remain visible during scrolling)
- **Standard Changes Catalog:** Freeze at row 5 (includes column headers)
- **Evidence Register:** Freeze at row 5
- **Approval Sign-Off:** Freeze at row 3

---

## File Naming Convention

**Format:** `ISMS_A_8_32_2_Change_Types_Categories_Assessment_YYYYMMDD.xlsx`

**Examples:**
- `ISMS_A_8_32_2_Change_Types_Categories_Assessment_20260115.xlsx`
- `ISMS_A_8_32_2_Change_Types_Categories_Assessment_20260401_FINAL.xlsx`

---

## Quarterly Review Cycle

### Review Checklist
1. ☐ Review standard changes catalog (additions/retirements)
2. ☐ Verify normal change criteria remain appropriate
3. ☐ Review emergency change metrics (<5% target)
4. ☐ Validate risk classification methodology
5. ☐ Update change calendar and blackout periods
6. ☐ Recalculate compliance metrics
7. ☐ Add new evidence entries
8. ☐ Address any identified gaps
9. ☐ Update approval sign-off with quarterly review notes
10. ☐ Distribute updated assessment to stakeholders

### Triggers for Ad-Hoc Review
- Addition/retirement of standard changes
- Emergency change threshold exceeded (>5%)
- Change failure rate increase
- Risk assessment methodology changes
- Organizational restructuring affecting approvals
- Internal/external audit findings
- Regulatory requirement changes

---

## Integration Points

### Related ISMS Documents
- **ISMS-POL-A.8.32-S2.2:** Change Classification Requirements (12 requirements)
- **ISMS-POL-A.8.32-S5.C:** Risk Assessment Matrix
- **ISMS-IMP-A.8.32.1:** Change Process Assessment
- **ISMS-IMP-A.8.32.3:** Environment Separation Assessment
- **ISMS-IMP-A.8.32.4:** Testing & Validation Assessment
- **ISMS-IMP-A.8.32.5:** Compliance Dashboard (consolidates this data)

### Related ISO 27001:2022 Controls
- **Control 5.7:** Threat intelligence (risk assessment inputs)
- **Control 8.29:** Configuration management (change classification consistency)
- **Control 8.31:** Separation of environments (standard vs. normal change criteria)

### External Integrations
- **Risk Register:** Link change risk classifications to organizational risk register
- **Incident Management:** Track emergency changes triggered by incidents
- **Change Management System:** Standard changes catalog synchronized
- **Metrics Dashboard:** Change distribution and classification accuracy metrics
- **Training Register:** Track training on change classification

### Audit Trail Requirements
- All change types documented with approval dates
- Standard changes catalog with annual review dates
- Risk classification methodology documented and versioned
- Emergency change metrics tracked quarterly
- Classification accuracy measured and trended
- Evidence maintained for all classification decisions

---

**END OF SPECIFICATION**

*"The first principle is that you must not fool yourself — and you are the easiest person to fool."*  
— Richard Feynman

**Change Classification Maturity Indicator:** If your emergency changes consistently stay below 5% and your risk classifications accurately predict change outcomes, you've moved beyond checkbox compliance to operational excellence. ✅

---

**Document Control:**
- **Created:** [Date]
- **Version:** 1.0
- **Next Review:** [Date + 3 months]
- **Owner:** ISMS Implementation Team
- **Classification:** Internal Use