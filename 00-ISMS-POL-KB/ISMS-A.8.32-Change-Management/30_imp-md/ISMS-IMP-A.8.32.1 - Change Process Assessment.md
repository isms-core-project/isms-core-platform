# ISMS-IMP-A.8.32.1 - Change Process Assessment
## Excel Workbook Layout Specification
### ISO/IEC 27001:2022 Control A.8.32: Change Management

---

## Document Overview

**Document ID:** ISMS-IMP-A.8.32.1  
**Assessment Area:** Change Process Workflow & Management Procedures  
**Related Policy:** ISMS-POL-A.8.32-S2.1 (Change Process Requirements)  
**Purpose:** Document change management processes, assess procedural capabilities against policy requirements, and identify gaps in a technology-agnostic manner

**Key Principle:** This assessment is **technology-independent**. Organizations document THEIR specific change management approach (tools, workflows, procedures) and verify capabilities against generic requirements.

---

## Workbook Structure

### Sheet 1: Instructions & Legend

#### Header Section
- **Title:** "ISMS-IMP-A.8.32.1 – Change Process Assessment"
- **Subtitle:** "ISO/IEC 27001:2022 - Control A.8.32: Change Management"
- **Styling:** Dark blue header (003366), white text, centered, 40px height

#### Document Information Block
```
Document ID:           ISMS-IMP-A.8.32.1
Assessment Area:       Change Process Workflow & Management
Related Policy:        ISMS-POL-A.8.32-S2.1
Version:               1.0
Assessment Date:       [USER INPUT - yellow cell]
Completed By:          [USER INPUT - yellow cell]
Organization:          [Organization]
Review Cycle:          Quarterly
```

#### How to Use This Workbook
1. Document YOUR organization's change management process in the Change_Process_Workflow sheet
2. Complete the Approval_Authority_Matrix with YOUR specific roles and thresholds
3. Fill in YOUR communication procedures and stakeholder notification methods
4. Document YOUR documentation requirements and record-keeping practices
5. Inventory YOUR change management tools (whatever platforms/systems you use)
6. Review the Summary_Dashboard for compliance metrics
7. Maintain the Evidence Register for audit traceability
8. Obtain final approval and sign-off

#### Status Legend
| Symbol | Status | Description | Color Code |
|--------|--------|-------------|------------|
| ✅ | Implemented | Process implemented and operational | Green (C6EFCE) |
| ⚠️ | Partial | Partial implementation or limited coverage | Yellow (FFEB9C) |
| ❌ | Not Implemented | Process not implemented | Red (FFC7CE) |
| 📋 | Planned | Implementation planned with target date | Blue (B4C7E7) |
| N/A | Not Applicable | Not applicable to this environment | Gray |

#### Compliance Levels
| Level | Percentage | Description |
|-------|------------|-------------|
| Fully Compliant | 90-100% | All requirements met, evidence documented |
| Substantially Compliant | 70-89% | Most requirements met, minor gaps |
| Partially Compliant | 50-69% | Significant gaps, remediation required |
| Non-Compliant | <50% | Major deficiencies, immediate action required |

#### Acceptable Evidence (Examples)
- ✓ Change management policy documents
- ✓ Process flowcharts/diagrams
- ✓ Change request form templates
- ✓ Change Advisory Board (CAB) meeting minutes
- ✓ Approval workflow documentation
- ✓ Communication templates (notification emails, status updates)
- ✓ Change management tool screenshots (redacted if needed)
- ✓ Change calendar/schedule examples
- ✓ Post-Implementation Review (PIR) templates
- ✓ Change failure metrics/reports
- ✓ Emergency change procedure documentation
- ✓ Training materials for change requesters/approvers

---

## Sheet 2: Change_Process_Workflow

### Purpose
Document the end-to-end change management process from request initiation through post-implementation review.

### Header Section
**Row 1:** "CHANGE MANAGEMENT PROCESS WORKFLOW"  
**Row 2:** "Document the complete change lifecycle in your organization"

### Process Stage Mapping Section (Rows 4-25)

| Stage | Stage Name | Description | Process Owner | Standard Duration | Tool/System Used | Status | Evidence Location |
|-------|------------|-------------|---------------|-------------------|------------------|--------|-------------------|
| 1 | Change Request Initiation | How changes are requested | Text | Text (e.g., "1 day") | Text | Dropdown: ✅/⚠️/❌/📋/N/A | Text |
| 2 | Initial Assessment & Screening | Validation and categorization | Text | Text | Text | Dropdown | Text |
| 3 | Risk & Impact Assessment | Evaluate change risks | Text | Text | Text | Dropdown | Text |
| 4 | Change Categorization | Standard/Normal/Emergency | Text | Text | Text | Dropdown | Text |
| 5 | CAB Scheduling (if required) | Schedule review meeting | Text | Text | Text | Dropdown | Text |
| 6 | CAB Review & Discussion | Formal review process | Text | Text | Text | Dropdown | Text |
| 7 | Change Authorization | Approval decision | Text | Text | Text | Dropdown | Text |
| 8 | Implementation Planning | Schedule and resource allocation | Text | Text | Text | Dropdown | Text |
| 9 | Stakeholder Communication | Notification procedures | Text | Text | Text | Dropdown | Text |
| 10 | Pre-Implementation Testing | Testing in non-production | Text | Text | Text | Dropdown | Text |
| 11 | Change Implementation | Actual execution | Text | Text | Text | Dropdown | Text |
| 12 | Implementation Verification | Verify success | Text | Text | Text | Dropdown | Text |
| 13 | Stakeholder Notification | Completion notification | Text | Text | Text | Dropdown | Text |
| 14 | Post-Implementation Review | Lessons learned | Text | Text | Text | Dropdown | Text |
| 15 | Change Record Closure | Documentation completion | Text | Text | Text | Dropdown | Text |

### Process Documentation Requirements (Rows 27-38)

| Requirement | Implemented | Documentation Type | Template Available | Location | Responsible Role |
|-------------|-------------|-------------------|-------------------|----------|------------------|
| Change request form/template | Dropdown: Yes/No/Partial | Text | Dropdown: Yes/No | Text | Text |
| Risk assessment template | Dropdown: Yes/No/Partial | Text | Dropdown: Yes/No | Text | Text |
| Impact assessment template | Dropdown: Yes/No/Partial | Text | Dropdown: Yes/No | Text | Text |
| CAB agenda template | Dropdown: Yes/No/Partial | Text | Dropdown: Yes/No | Text | Text |
| Implementation plan template | Dropdown: Yes/No/Partial | Text | Dropdown: Yes/No | Text | Text |
| Rollback plan template | Dropdown: Yes/No/Partial | Text | Dropdown: Yes/No | Text | Text |
| PIR template | Dropdown: Yes/No/Partial | Text | Dropdown: Yes/No | Text | Text |
| Communication templates | Dropdown: Yes/No/Partial | Text | Dropdown: Yes/No | Text | Text |
| Change closure checklist | Dropdown: Yes/No/Partial | Text | Dropdown: Yes/No | Text | Text |

### Workflow Automation Assessment (Rows 40-50)

| Capability | Automated | Semi-Automated | Manual | Tool/System | Notes |
|------------|-----------|----------------|--------|-------------|-------|
| Change request submission | Checkbox | Checkbox | Checkbox | Text | Text |
| Request routing/assignment | Checkbox | Checkbox | Checkbox | Text | Text |
| Approval workflow | Checkbox | Checkbox | Checkbox | Text | Text |
| Notification distribution | Checkbox | Checkbox | Checkbox | Text | Text |
| Change calendar updates | Checkbox | Checkbox | Checkbox | Text | Text |
| Status tracking | Checkbox | Checkbox | Checkbox | Text | Text |
| Reporting/dashboards | Checkbox | Checkbox | Checkbox | Text | Text |
| PIR reminders | Checkbox | Checkbox | Checkbox | Text | Text |

---

## Sheet 3: Approval_Authority_Matrix

### Purpose
Define who can approve what types of changes based on risk level and change type.

### Header Section
**Row 1:** "CHANGE APPROVAL AUTHORITY MATRIX"  
**Row 2:** "Define approval authorities by change type and risk level"

### Standard Changes Approval (Rows 4-20)

| Standard Change Type | Pre-Approved | Self-Service Allowed | Approver (if required) | Approval SLA | Implemented | Evidence |
|---------------------|--------------|---------------------|----------------------|--------------|-------------|----------|
| [Describe standard change] | Dropdown: Yes/No | Dropdown: Yes/No/N/A | Text | Text | Dropdown: ✅/⚠️/❌/📋 | Text |

[15 rows for standard change documentation]

### Normal Changes Approval Matrix (Rows 22-35)

| Risk Level | Impact Level | Required Approvers | CAB Review Required | Approval Threshold | Typical SLA | Implemented |
|------------|--------------|-------------------|--------------------|--------------------|-------------|-------------|
| Low | Low | Text (e.g., "Change Manager") | Dropdown: Yes/No | Text (e.g., "1 approver") | Text | Dropdown |
| Low | Medium | Text | Dropdown: Yes/No | Text | Text | Dropdown |
| Low | High | Text | Dropdown: Yes/No | Text | Text | Dropdown |
| Medium | Low | Text | Dropdown: Yes/No | Text | Text | Dropdown |
| Medium | Medium | Text (e.g., "CAB + Service Owner") | Dropdown: Yes/No | Text (e.g., "2 approvers") | Text | Dropdown |
| Medium | High | Text | Dropdown: Yes/No | Text | Text | Dropdown |
| High | Low | Text | Dropdown: Yes/No | Text | Text | Dropdown |
| High | Medium | Text | Dropdown: Yes/No | Text | Text | Dropdown |
| High | High | Text (e.g., "CAB + CISO") | Dropdown: Yes/No | Text (e.g., "3+ approvers") | Text | Dropdown |
| Critical | Any | Text (e.g., "CAB + CISO + CIO") | Dropdown: Yes (Mandatory) | Text | Text | Dropdown |

### Emergency Changes Approval (Rows 37-43)

| Emergency Criteria | E-CAB Members | Minimum Approvers | Approval Method | Documented | Evidence |
|-------------------|--------------|-------------------|-----------------|------------|----------|
| System outage affecting critical services | Text | Number | Dropdown: Virtual Meeting/Phone/Email Chain/Instant Messaging | Dropdown: ✅/⚠️/❌ | Text |
| Security incident response | Text | Number | Dropdown | Dropdown | Text |
| Regulatory compliance deadline | Text | Number | Dropdown | Dropdown | Text |
| Data loss prevention | Text | Number | Dropdown | Dropdown | Text |
| [Other - specify] | Text | Number | Dropdown | Dropdown | Text |

### Approval Process Metrics (Rows 45-52)

| Metric | Target | Current | Status |
|--------|--------|---------|--------|
| Average approval time (Standard) | Text | Text | Formula: Green/Yellow/Red |
| Average approval time (Normal - Low Risk) | Text | Text | Formula |
| Average approval time (Normal - High Risk) | Text | Text | Formula |
| Average approval time (Emergency) | Text | Text | Formula |
| Approval backlog (pending >SLA) | Text | Number | Formula |
| Approval rejection rate | Text (e.g., "<5%") | Text (e.g., "3%") | Formula |

---

## Sheet 4: Communication_Procedures

### Purpose
Document how changes are communicated to stakeholders throughout the change lifecycle.

### Header Section
**Row 1:** "CHANGE COMMUNICATION PROCEDURES"  
**Row 2:** "Document stakeholder notification and communication methods"

### Stakeholder Identification (Rows 4-20)

| Stakeholder Group | Role/Description | Notification Trigger | Communication Method | Responsible Party | Template Available | Status |
|-------------------|------------------|---------------------|---------------------|-------------------|--------------------|--------|
| End Users | All affected users | Dropdown: Submission/Approval/24h Before/At Implementation/Completion | Dropdown: Email/Portal/IM/SMS/All | Text | Dropdown: Yes/No | Dropdown: ✅/⚠️/❌/📋 |
| Service Owners | Business service owners | Dropdown | Dropdown | Text | Dropdown | Dropdown |
| IT Operations Team | Implementation team | Dropdown | Dropdown | Text | Dropdown | Dropdown |
| Security Team | InfoSec team | Dropdown | Dropdown | Text | Dropdown | Dropdown |
| Management | IT leadership | Dropdown | Dropdown | Text | Dropdown | Dropdown |
| CAB Members | Change Advisory Board | Dropdown | Dropdown | Text | Dropdown | Dropdown |
| External Vendors | Third-party providers | Dropdown | Dropdown | Text | Dropdown | Dropdown |

[13 rows for stakeholder documentation]

### Communication Templates (Rows 22-32)

| Template Type | Purpose | Content Includes | Approval Required | Format | Location | Maintained |
|---------------|---------|------------------|-------------------|--------|----------|------------|
| Change Request Acknowledgment | Confirm receipt | Change ID, requestor, next steps | Dropdown: Yes/No | Dropdown: Email/Portal/Both | Text | Dropdown: ✅/⚠️/❌ |
| Change Scheduled Notification | Inform of approval & schedule | Change details, date/time, impact | Dropdown | Dropdown | Text | Dropdown |
| Change Reminder (24h) | Pre-implementation reminder | Time, expected duration, contacts | Dropdown | Dropdown | Text | Dropdown |
| Change In Progress | During implementation | Status, progress, issues | Dropdown | Dropdown | Text | Dropdown |
| Change Completed Successfully | Successful completion | Completion time, verification | Dropdown | Dropdown | Text | Dropdown |
| Change Failed/Rolled Back | Failure notification | Issue, rollback status, next steps | Dropdown | Dropdown | Text | Dropdown |
| Change Postponed | Schedule change | Reason, new date, next steps | Dropdown | Dropdown | Text | Dropdown |
| Emergency Change Notice | Urgent notification | Reason, approval, impact | Dropdown | Dropdown | Text | Dropdown |

### Communication Channels Assessment (Rows 34-43)

| Channel | Available | Primary Use | Audience Reach | Reliability | Documented |
|---------|-----------|-------------|----------------|-------------|------------|
| Email | Dropdown: Yes/No | Text | Dropdown: All Users/IT Staff/Management/Selective | Dropdown: High/Medium/Low | Dropdown: ✅/⚠️/❌ |
| Internal Portal/Intranet | Dropdown: Yes/No | Text | Dropdown | Dropdown | Dropdown |
| Change Management System | Dropdown: Yes/No | Text | Dropdown | Dropdown | Dropdown |
| Instant Messaging (Teams/Slack/etc) | Dropdown: Yes/No | Text | Dropdown | Dropdown | Dropdown |
| SMS/Text Messages | Dropdown: Yes/No | Text | Dropdown | Dropdown | Dropdown |
| Status Dashboard | Dropdown: Yes/No | Text | Dropdown | Dropdown | Dropdown |
| Scheduled Announcements | Dropdown: Yes/No | Text | Dropdown | Dropdown | Dropdown |

---

## Sheet 5: Documentation_Requirements

### Purpose
Define what documentation is required for each change type and how records are maintained.

### Header Section
**Row 1:** "CHANGE DOCUMENTATION REQUIREMENTS"  
**Row 2:** "Define record-keeping requirements by change type"

### Standard Change Documentation (Rows 4-15)

| Documentation Item | Required | Format | Retention Period | Storage Location | Responsible Role | Compliant |
|--------------------|----------|--------|------------------|------------------|------------------|-----------|
| Change request (basic) | Dropdown: Mandatory/Optional/N/A | Dropdown: Electronic/Paper/Both | Text (e.g., "1 year") | Text | Text | Dropdown: ✅/⚠️/❌ |
| Requestor identification | Dropdown | Dropdown | Text | Text | Text | Dropdown |
| Change description | Dropdown | Dropdown | Text | Text | Text | Dropdown |
| Service/system affected | Dropdown | Dropdown | Text | Text | Text | Dropdown |
| Implementation date/time | Dropdown | Dropdown | Text | Text | Text | Dropdown |
| Implementation result | Dropdown | Dropdown | Text | Text | Text | Dropdown |

[10 rows for standard change documentation]

### Normal Change Documentation (Rows 17-35)

| Documentation Item | Required | Format | Retention Period | Storage Location | Responsible Role | Compliant |
|--------------------|----------|--------|------------------|------------------|------------------|-----------|
| Complete change request | Dropdown: Mandatory/Optional | Dropdown: Electronic/Paper/Both | Text (e.g., "3 years") | Text | Text | Dropdown: ✅/⚠️/❌ |
| Risk assessment | Dropdown | Dropdown | Text | Text | Text | Dropdown |
| Impact assessment | Dropdown | Dropdown | Text | Text | Text | Dropdown |
| Business justification | Dropdown | Dropdown | Text | Text | Text | Dropdown |
| Technical implementation plan | Dropdown | Dropdown | Text | Text | Text | Dropdown |
| Test plan/results | Dropdown | Dropdown | Text | Text | Text | Dropdown |
| Rollback plan | Dropdown | Dropdown | Text | Text | Text | Dropdown |
| CAB review record | Dropdown | Dropdown | Text | Text | Text | Dropdown |
| Approval record (all approvers) | Dropdown | Dropdown | Text | Text | Text | Dropdown |
| Communication records | Dropdown | Dropdown | Text | Text | Text | Dropdown |
| Implementation log/notes | Dropdown | Dropdown | Text | Text | Text | Dropdown |
| Verification evidence | Dropdown | Dropdown | Text | Text | Text | Dropdown |
| Post-Implementation Review | Dropdown | Dropdown | Text | Text | Text | Dropdown |

[18 rows total for normal change documentation]

### Emergency Change Documentation (Rows 37-48)

| Documentation Item | Required | Special Requirements | Retention Period | Storage Location | Responsible Role | Compliant |
|--------------------|----------|---------------------|------------------|------------------|------------------|-----------|
| Emergency change justification | Dropdown: Mandatory/Optional | Text (e.g., "Document within 2 hours") | Text (e.g., "5 years") | Text | Text | Dropdown: ✅/⚠️/❌ |
| E-CAB approval record | Dropdown | Text | Text | Text | Text | Dropdown |
| Emergency criteria met | Dropdown | Text | Text | Text | Text | Dropdown |
| Incident ticket reference | Dropdown | Text | Text | Text | Text | Dropdown |
| Risk accepted by | Dropdown | Text | Text | Text | Text | Dropdown |
| Implementation record | Dropdown | Text | Text | Text | Text | Dropdown |
| Mandatory PIR | Dropdown: Mandatory (always) | Text (e.g., "Within 2 business days") | Text | Text | Text | Dropdown |
| Retrospective CAB review | Dropdown | Text | Text | Text | Text | Dropdown |

### Record Retention & Disposal (Rows 50-58)

| Record Type | Retention Period | Disposal Method | Regulatory Requirement | Implemented | Evidence |
|-------------|------------------|-----------------|----------------------|-------------|----------|
| Standard changes | Text | Dropdown: Secure Delete/Archive/Destruction | Text (e.g., "ISO 27001") | Dropdown: ✅/⚠️/❌ | Text |
| Normal changes (successful) | Text | Dropdown | Text | Dropdown | Text |
| Failed changes | Text | Dropdown | Text | Dropdown | Text |
| Emergency changes | Text | Dropdown | Text | Dropdown | Text |
| CAB meeting minutes | Text | Dropdown | Text | Dropdown | Text |
| Approval records | Text | Dropdown | Text | Dropdown | Text |

---

## Sheet 6: Change_Management_Tools

### Purpose
Inventory all tools, systems, and platforms used to support change management processes.

### Header Section
**Row 1:** "CHANGE MANAGEMENT TOOLS & SYSTEMS INVENTORY"  
**Row 2:** "Document all platforms and tools supporting change management"

### Primary Change Management System (Rows 4-25)

| Attribute | Value | Evidence Location |
|-----------|-------|-------------------|
| **System Identification** | | |
| Tool/Platform Name | Text (e.g., "ServiceNow Change Management") | Text |
| Vendor/Provider | Text | Text |
| Version/Release | Text | Text |
| Deployment Type | Dropdown: Cloud SaaS/On-Premises/Hybrid/Self-Hosted | Text |
| Primary Use | Dropdown: Change Management/ITSM Suite/Ticketing/Custom Development | Text |
| **Capabilities** | | |
| Change request submission | Dropdown: ✅ Full/⚠️ Partial/❌ No | Text |
| Workflow automation | Dropdown | Text |
| Approval routing | Dropdown | Text |
| Risk/Impact assessment forms | Dropdown | Text |
| Change calendar | Dropdown | Text |
| Conflict detection | Dropdown | Text |
| Notification engine | Dropdown | Text |
| Reporting/dashboards | Dropdown | Text |
| Integration with monitoring | Dropdown | Text |
| Integration with CMDB | Dropdown | Text |
| API availability | Dropdown: ✅ Yes/❌ No/⚠️ Limited | Text |
| **Administration** | | |
| System administrators | Text (number or names) | Text |
| User training provided | Dropdown: ✅ Yes/⚠️ Limited/❌ No | Text |
| Documentation available | Dropdown | Text |
| Support availability | Dropdown: 24/7/Business Hours/Community/None | Text |
| License status | Dropdown: Active/Expiring Soon/Expired | Text |
| License expiration date | Date | Text |

### Supporting Tools & Systems (Rows 27-45)

| Tool/System | Purpose | Integration with Primary System | Status | User Count | Evidence |
|-------------|---------|--------------------------------|--------|------------|----------|
| [Tool name - user fills in] | Dropdown: Testing/Deployment/Monitoring/Collaboration/Documentation/Other | Dropdown: ✅ Integrated/⚠️ Partial/❌ Standalone | Dropdown: ✅/⚠️/❌/📋 | Number | Text |

[18 rows for additional tool documentation]

### Integration Architecture (Rows 47-58)

| Integration Point | Source System | Target System | Integration Type | Automated | Data Exchanged | Status |
|-------------------|---------------|---------------|------------------|-----------|----------------|--------|
| [e.g., "Change → Monitoring"] | Text | Text | Dropdown: API/File Transfer/Manual/Webhook/Other | Dropdown: Yes/No/Partial | Text | Dropdown: ✅/⚠️/❌ |

[12 rows for integration documentation]

### Tool Access & Security (Rows 60-68)

| Security Control | Implemented | Details | Evidence |
|------------------|-------------|---------|----------|
| Multi-factor authentication | Dropdown: ✅ Yes/❌ No/⚠️ Partial | Text | Text |
| Role-based access control | Dropdown | Text | Text |
| Audit logging enabled | Dropdown | Text | Text |
| Data encryption (at rest) | Dropdown | Text | Text |
| Data encryption (in transit) | Dropdown | Text | Text |
| Backup/recovery tested | Dropdown | Text | Text |
| Disaster recovery plan | Dropdown | Text | Text |

---

## Sheet 7: Summary_Dashboard

### Purpose
Aggregate compliance metrics and identify gaps across all process areas.

### Header Section
**Row 1:** "CHANGE PROCESS ASSESSMENT - SUMMARY DASHBOARD"  
**Row 2:** "Overall compliance status and key findings"

### Overall Compliance Summary (Rows 4-12)

| Assessment Area | Total Requirements | Implemented | Partial | Not Implemented | Compliance % | Status |
|-----------------|-------------------|-------------|---------|----------------|--------------|--------|
| Change Process Workflow | Formula (count from Sheet 2) | Formula | Formula | Formula | Formula | Formula: Green/Yellow/Red |
| Approval Authority | Formula (from Sheet 3) | Formula | Formula | Formula | Formula | Formula |
| Communication Procedures | Formula (from Sheet 4) | Formula | Formula | Formula | Formula | Formula |
| Documentation Requirements | Formula (from Sheet 5) | Formula | Formula | Formula | Formula | Formula |
| Change Management Tools | Formula (from Sheet 6) | Formula | Formula | Formula | Formula | Formula |
| **OVERALL TOTAL** | Formula | Formula | Formula | Formula | Formula | Formula |

### Policy Requirement Mapping (Rows 14-35)

| Policy Req ID | Requirement Summary | Status | Evidence Sheet | Evidence Row | Auditor Notes |
|--------------|---------------------|--------|----------------|--------------|---------------|
| REQ-PROCESS-001 | Change request procedures | Formula: ✅/⚠️/❌ | Text | Text | Text (editable) |
| REQ-PROCESS-002 | Risk assessment | Formula | Text | Text | Text |
| REQ-PROCESS-003 | Impact assessment | Formula | Text | Text | Text |
| REQ-PROCESS-004 | Change classification | Formula | Text | Text | Text |
| REQ-PROCESS-005 | Approval workflows | Formula | Text | Text | Text |
| REQ-PROCESS-006 | CAB operation | Formula | Text | Text | Text |
| REQ-PROCESS-007 | Emergency procedures | Formula | Text | Text | Text |
| REQ-PROCESS-008 | Communication | Formula | Text | Text | Text |
| REQ-PROCESS-009 | Implementation planning | Formula | Text | Text | Text |
| REQ-PROCESS-010 | Testing requirements | Formula | Text | Text | Text |
| REQ-PROCESS-011 | Rollback plans | Formula | Text | Text | Text |
| REQ-PROCESS-012 | Documentation | Formula | Text | Text | Text |
| REQ-PROCESS-013 | PIR mandatory | Formula | Text | Text | Text |
| REQ-PROCESS-014 | Continuous improvement | Formula | Text | Text | Text |
| REQ-PROCESS-015 | Record retention | Formula | Text | Text | Text |
| REQ-PROCESS-016 | Tool capabilities | Formula | Text | Text | Text |
| REQ-PROCESS-017 | Integration | Formula | Text | Text | Text |
| REQ-PROCESS-018 | Metrics/KPIs | Formula | Text | Text | Text |
| REQ-PROCESS-019 | Training | Formula | Text | Text | Text |
| REQ-PROCESS-020 | Governance | Formula | Text | Text | Text |

### Critical Findings (Rows 37-42)

| Finding Type | Count | Description |
|--------------|-------|-------------|
| Critical Gaps | Formula (count ❌ from all sheets) | Text area (auto-populate key gaps) |
| High-Priority Items | Formula (count ⚠️) | Text area |
| Planned Improvements | Formula (count 📋) | Text area |

### Audit Readiness Assessment (Rows 44-50)

| Criterion | Status | Notes |
|-----------|--------|-------|
| All processes documented | Formula: ✅/⚠️/❌ | Text |
| Evidence available for key controls | Formula | Text |
| Roles and responsibilities defined | Formula | Text |
| Tool capabilities verified | Formula | Text |
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
| EV-001 | Dropdown: Policy Doc/Procedure/Flowchart/Template/Screenshot/Meeting Minutes/Email/Report/Contract/Other | Text | Dropdown: (all sheets + REQ-IDs) | Text | Date | Text | Dropdown: ✅ Verified/⚠️ Pending/❌ Not Verified | Text |

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
Assessment Document:        ISMS-IMP-A.8.32.1 - Change Process Assessment
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

### Reviewed By - Process Owner / Change Manager (Rows 22-30)
```
Name:                   [USER INPUT]
Role/Title:             [USER INPUT]
Review Date:            [USER INPUT - date picker, format DD.MM.YYYY]
Review Notes:           [Text area - merged cells C24:F28]
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
Conditions/Notes:       [Text area - merged cells C36:F38]
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
- **Section Header:** Font: Calibri 11pt bold black, Fill: B4C7E7 (light blue), Alignment: left, Height: 20px
- **Column Header:** Font: Calibri 10pt bold black, Fill: D9D9D9 (light gray), Alignment: centered/wrapped, Border: thin all sides

### Input Cell Styles
- **Editable (User Input):** Fill: FFFFCC (light yellow), Border: thin black, Alignment: left/wrap
- **Calculated/Formula:** Fill: E0E0E0 (light gray), Border: thin black, Protection: locked
- **Dropdown:** Fill: FFFFCC (light yellow), Border: thin black, Data validation applied

### Status Color Coding
- **✅ Implemented/Compliant:** C6EFCE (light green)
- **⚠️ Partial/Requires Attention:** FFEB9C (light yellow)
- **❌ Not Implemented/Non-Compliant:** FFC7CE (light red)
- **📋 Planned:** B4C7E7 (light blue)
- **N/A:** F2F2F2 (light gray)

### Compliance Level Colors
- **90-100% (Fully Compliant):** C6EFCE (green)
- **70-89% (Substantially):** FFEB9C (yellow)
- **50-69% (Partially):** FFD966 (orange)
- **<50% (Non-Compliant):** FFC7CE (red)

---

## Freeze Panes

- **All assessment sheets:** Freeze at row 4 (headers remain visible during scrolling)
- **Evidence Register:** Freeze at row 5 (header + column headers)
- **Approval Sign-Off:** Freeze at row 3

---

## Column Width Guidelines

### Standard Widths (approximate pixels)
- **ID columns:** 12
- **Status dropdowns:** 15
- **Short text (names, roles):** 20
- **Descriptions:** 35-40
- **Notes/Comments:** 30-35
- **Dates:** 12-15
- **Evidence locations:** 30

### Auto-fit Exceptions
- Do NOT auto-fit merged cells (breaks layout)
- Do NOT auto-fit formula cells (use fixed width)

---

## Data Protection & Workbook Security

### Protection Settings
- **Instructions sheet:** Unprotected (read-only recommended)
- **Assessment sheets:** Protect formulas, unlock input cells (yellow)
- **Summary Dashboard:** Fully protected (formulas only)
- **Evidence Register:** Unlock all except Evidence ID (auto-generated)
- **Approval Sign-Off:** Unlock signature/approval fields only

### Password Protection
- **Recommended:** Use workbook password for distribution
- **Do NOT:** Protect individual sheets with different passwords
- **Note:** Password in organizational password manager

---

## File Naming Convention

**Format:** `ISMS_A_8_32_1_Change_Process_Assessment_YYYYMMDD.xlsx`

**Examples:**
- `ISMS_A_8_32_1_Change_Process_Assessment_20260115.xlsx`
- `ISMS_A_8_32_1_Change_Process_Assessment_20260401_FINAL.xlsx`

---

## Quarterly Review Cycle

### Review Checklist
1. ☐ Update process workflow for any changes (Sheet 2)
2. ☐ Verify approval authorities are current (Sheet 3)
3. ☐ Review communication procedures effectiveness (Sheet 4)
4. ☐ Validate documentation compliance (Sheet 5)
5. ☐ Update tool inventory and licenses (Sheet 6)
6. ☐ Recalculate compliance metrics (Sheet 7)
7. ☐ Add new evidence entries (Sheet 8)
8. ☐ Address any identified gaps
9. ☐ Update approval sign-off with quarterly review notes
10. ☐ Distribute updated assessment to stakeholders

### Triggers for Ad-Hoc Review
- Major change to change management process
- New change management tool implementation
- Significant change failure/incident
- Internal/external audit findings
- Regulatory requirement changes
- Organizational restructuring affecting approvals

---

## Integration Points

### Related ISMS Documents
- **ISMS-POL-A.8.32-S2.1:** Change Process Requirements (20 requirements)
- **ISMS-POL-A.8.32-S2.2:** Change Classification Requirements
- **ISMS-POL-A.8.32-S3:** Roles and Responsibilities (RACI matrix)
- **ISMS-POL-A.8.32-S5.B:** Change Request Form Template
- **ISMS-IMP-A.8.32.2:** Change Types & Categories Assessment
- **ISMS-IMP-A.8.32.3:** Environment Separation Assessment
- **ISMS-IMP-A.8.32.4:** Testing & Validation Assessment
- **ISMS-IMP-A.8.32.5:** Compliance Dashboard (consolidates this data)

### Related ISO 27001:2022 Controls
- **Control 5.30:** ICT readiness for business continuity (continuity plan updates)
- **Control 5.37:** Documented operating procedures (change procedures)
- **Control 8.29:** Configuration management (link change records to config items)
- **Control 8.31:** Separation of environments (test before prod deployment)
- **Control 8.33:** Test information (production data in test environments)

### External Integrations
- **Risk Register:** Link change risks to organizational risk register
- **Incident Management:** Reference incidents triggering emergency changes
- **Problem Management:** Link changes to problem resolutions
- **Configuration Management Database (CMDB):** Link changes to CIs
- **Asset Register:** Ensure change management tools are tracked as assets
- **Training Register:** Track change management training completion

### Audit Trail Requirements
- All process documentation referenced in Evidence Register
- Approval authorities documented with organizational chart evidence
- Communication templates stored in document management system
- Tool capabilities verified through screenshots/reports
- Compliance metrics calculated from source data (auditable formulas)
- Sign-off maintains complete approval chain

---

## Assessment Completion Checklist

### Before Submitting for Review
- [ ] All 9 sheets completed (no yellow cells empty unless N/A)
- [ ] Evidence Register has entries for all major claims
- [ ] Compliance percentages calculated correctly
- [ ] Critical gaps identified and documented
- [ ] Tool inventory current and complete
- [ ] Approval authorities reflect current org structure
- [ ] Communication procedures tested and verified
- [ ] Documentation requirements compliance verified
- [ ] All formulas working correctly (no #REF or #VALUE errors)
- [ ] File named correctly with current date

### Quality Checks
- [ ] No broken cross-references between sheets
- [ ] Dropdown values used consistently
- [ ] Date formats consistent (DD.MM.YYYY in cells)
- [ ] Evidence locations are specific and accessible
- [ ] Status indicators match actual implementation state
- [ ] Comments/notes provide sufficient detail
- [ ] No placeholder text remaining
- [ ] Spell check completed
- [ ] Print preview reviewed (if physical approval required)

### Sign-Off Preparation
- [ ] Assessment summary accurately reflects findings
- [ ] Preparer contact information complete
- [ ] Review notes section ready for reviewer input
- [ ] Approval section formatted for signature (physical or digital)
- [ ] Next review date calculated
- [ ] Distribution list identified

---

**END OF SPECIFICATION**

*"The first principle is that you must not fool yourself — and you are the easiest person to fool."*  
— Richard Feynman

**Change Management Maturity Indicator:** If you can describe your change management process WITHOUT mentioning specific tool brands in your policies, you understand the difference between implementing a process and installing software. ✅

---

**Document Control:**
- **Created:** [Date]
- **Version:** 1.0
- **Next Review:** [Date + 3 months]
- **Owner:** ISMS Implementation Team
- **Classification:** Internal Use