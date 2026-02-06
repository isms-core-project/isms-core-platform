**ISMS-IMP-A.8.32.1-TG - Change Process Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.32: Change Management

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.32.1-TG |
| **Version** | 1.0 |
| **Assessment Area** | Change Process Workflow & Management Procedures |
| **Related Policy** | ISMS-POL-A.8.32, Section 2.1 (Change Process Requirements) |
| **Purpose** | Document change management processes, assess procedural capabilities against policy requirements, and identify gaps in a technology-agnostic manner |
| **Target Audience** | Change Manager, CAB Members, IT Operations, System Owners, Compliance Officers, Auditors, Workbook Developers |
| **Assessment Type** | Process & Procedural |
| **Review Cycle** | Quarterly or After Major Process Changes |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial assessment specification for Change Process workbook | ISMS Implementation Team |

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.8.32.1-UG.

---

# Technical Specification

**Audience:** Workbook developers, Python script maintainers, Technical reviewers

**Note:** This section provides technical specifications for the Excel assessment workbook generation and maintenance. Users completing the assessment should refer to Part I above.

---

## Document Overview

**Document ID:** ISMS-IMP-A.8.32.1-TG  
**Assessment Area:** Change Process Workflow & Management Procedures  
**Related Policy:** ISMS-POL-A.8.32, Section 2.1 (Change Process Requirements)  
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
Related Policy:        ISMS-POL-A.8.32, Section 2.1
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
| 7 | Approval Decision | Obtain required approvals | Text | Text | Text | Dropdown | Text |
| 8 | Implementation Planning | Detailed execution planning | Text | Text | Text | Dropdown | Text |
| 9 | Stakeholder Communication | Notify affected parties | Text | Text | Text | Dropdown | Text |
| 10 | Change Implementation | Execute change | Text | Text | Text | Dropdown | Text |
| 11 | Verification & Validation | Confirm success | Text | Text | Text | Dropdown | Text |
| 12 | Rollback (if needed) | Revert to previous state | Text | Text | Text | Dropdown | Text |
| 13 | Documentation Update | Update system docs | Text | Text | Text | Dropdown | Text |
| 14 | Continuity Plan Update | Update DR/BC plans if needed | Text | Text | Text | Dropdown | Text |
| 15 | Post-Implementation Review | Lessons learned | Text | Text | Text | Dropdown | Text |
| 16 | Change Closure | Close change record | Text | Text | Text | Dropdown | Text |

**Column Widths:**

- A: 8, B: 30, C: 35, D: 20, E: 18, F: 25, G: 12, H: 30

### Process Requirements Assessment (Rows 27-50)

**Section Header:** "CHANGE PROCESS REQUIREMENTS ASSESSMENT"

| Requirement ID | Requirement | Implemented | How Implemented | Tool/System | Status | Evidence |
|----------------|-------------|-------------|-----------------|-------------|--------|----------|
| REQ-PROCESS-001 | Change request procedures | Dropdown: Yes/No/Partial | Text (editable) | Text | Dropdown: ✅/⚠️/❌/📋 | Text |
| REQ-PROCESS-002 | Risk assessment | Dropdown | Text | Text | Dropdown | Text |
| REQ-PROCESS-003 | Impact assessment | Dropdown | Text | Text | Dropdown | Text |
| REQ-PROCESS-004 | Change classification | Dropdown | Text | Text | Dropdown | Text |
| REQ-PROCESS-005 | Approval workflows | Dropdown | Text | Text | Dropdown | Text |
| REQ-PROCESS-006 | CAB operation | Dropdown | Text | Text | Dropdown | Text |
| REQ-PROCESS-007 | Emergency procedures | Dropdown | Text | Text | Dropdown | Text |
| REQ-PROCESS-008 | Communication | Dropdown | Text | Text | Dropdown | Text |
| REQ-PROCESS-009 | Implementation planning | Dropdown | Text | Text | Dropdown | Text |
| REQ-PROCESS-010 | Testing requirements | Dropdown | Text | Text | Dropdown | Text |
| REQ-PROCESS-011 | Rollback plans | Dropdown | Text | Text | Dropdown | Text |
| REQ-PROCESS-012 | Documentation | Dropdown | Text | Text | Dropdown | Text |
| REQ-PROCESS-013 | PIR mandatory | Dropdown | Text | Text | Dropdown | Text |
| REQ-PROCESS-014 | Continuous improvement | Dropdown | Text | Text | Dropdown | Text |
| REQ-PROCESS-015 | Record retention | Dropdown | Text | Text | Dropdown | Text |
| REQ-PROCESS-016 | Tool capabilities | Dropdown | Text | Text | Dropdown | Text |
| REQ-PROCESS-017 | Integration | Dropdown | Text | Text | Dropdown | Text |
| REQ-PROCESS-018 | Metrics/KPIs | Dropdown | Text | Text | Dropdown | Text |
| REQ-PROCESS-019 | Training | Dropdown | Text | Text | Dropdown | Text |
| REQ-PROCESS-020 | Governance | Dropdown | Text | Text | Dropdown | Text |

### Critical Findings (Rows 52-57)

| Finding Type | Count | Description |
|--------------|-------|-------------|
| Critical Gaps | Formula (count ❌ from all sheets) | Text area (auto-populate key gaps) |
| High-Priority Items | Formula (count ⚠️) | Text area |
| Planned Improvements | Formula (count 📋) | Text area |

### Audit Readiness Assessment (Rows 59-65)

| Criterion | Status | Notes |
|-----------|--------|-------|
| All processes documented | Formula: ✅/⚠️/❌ | Text |
| Evidence available for key controls | Formula | Text |
| Roles and responsibilities defined | Formula | Text |
| Tool capabilities verified | Formula | Text |
| Compliance ≥70% | Formula | Text |
| **OVERALL AUDIT READINESS** | Formula | Text |

---

## Sheet 3: Approval_Authority_Matrix

### Purpose
Document approval authorities for different change types and risk levels.

### Header Section
**Row 1:** "APPROVAL AUTHORITY MATRIX"  
**Row 2:** "Define who approves changes at different risk levels"

### Approval Authority by Risk Level (Rows 4-12)

| Risk Level | Change Type | Primary Approver | Secondary Approver | Emergency Approver | Documented | Enforced | Evidence |
|------------|-------------|------------------|--------------------|--------------------|------------|----------|----------|
| Low | Standard Change | Text (role/title) | Text or N/A | Text | Dropdown: Yes/No | Dropdown: ✅/⚠️/❌ | Text |
| Medium | Normal Change | Text | Text | Text | Dropdown | Dropdown | Text |
| High | Normal Change | Text | Text | Text | Dropdown | Dropdown | Text |
| Critical | Normal Change | Text | Text | Text | Dropdown | Dropdown | Text |
| Emergency | Emergency Change | Text | Text | N/A | Dropdown | Dropdown | Text |

**Column Widths:**

- A: 15, B: 20, C: 25, D: 25, E: 25, F: 15, G: 12, H: 30

### Approval Requirements Assessment (Rows 14-30)

| Requirement | Implemented | Details | Status | Evidence |
|-------------|-------------|---------|--------|----------|
| Approval authority documented | Dropdown: Yes/No/Partial | Text | Dropdown: ✅/⚠️/❌ | Text |
| Risk-based approval levels | Dropdown | Text | Dropdown | Text |
| Separation of duties (requester ≠ approver) | Dropdown | Text | Dropdown | Text |
| Delegation procedures defined | Dropdown | Text | Dropdown | Text |
| Emergency approval procedures | Dropdown | Text | Dropdown | Text |
| Escalation paths documented | Dropdown | Text | Dropdown | Text |
| Approval timeframes defined | Dropdown | Text | Dropdown | Text |
| Approval tracked in system | Dropdown | Text | Dropdown | Text |
| Approval history auditable | Dropdown | Text | Dropdown | Text |
| Non-compliance consequences defined | Dropdown | Text | Dropdown | Text |

---

## Sheet 4: CAB_Operations

### Purpose
Assess Change Advisory Board (CAB) operations and effectiveness.

### Header Section
**Row 1:** "CHANGE ADVISORY BOARD (CAB) OPERATIONS"  
**Row 2:** "Document CAB composition, operation, and effectiveness"

### CAB Composition (Rows 4-15)

| Role | Name/Position | Attendance Rate | Decision Authority | Status | Notes |
|------|---------------|-----------------|--------------------| -------|-------|
| CAB Chair | Text | Text (e.g., "85%") | Text | Dropdown: ✅/⚠️/❌ | Text |
| Change Manager | Text | Text | Text | Dropdown | Text |
| Security Representative | Text | Text | Text | Dropdown | Text |
| IT Operations Rep | Text | Text | Text | Dropdown | Text |
| Application Owner Rep | Text | Text | Text | Dropdown | Text |
| Business Representative | Text | Text | Text | Dropdown | Text |
| [Additional Members] | Text | Text | Text | Dropdown | Text |

### CAB Operations Assessment (Rows 17-35)

| Requirement | Implemented | Details | Frequency/SLA | Status | Evidence |
|-------------|-------------|---------|---------------|--------|----------|
| CAB charter exists | Dropdown: Yes/No | Text | N/A | Dropdown: ✅/⚠️/❌ | Text |
| Regular meeting schedule | Dropdown | Text | Text (e.g., "Weekly") | Dropdown | Text |
| Meeting attendance tracked | Dropdown | Text | N/A | Dropdown | Text |
| Quorum requirements | Dropdown | Text | Text | Dropdown | Text |
| Meeting agenda distributed | Dropdown | Text | Text (e.g., "48h advance") | Dropdown | Text |
| Meeting minutes recorded | Dropdown | Text | N/A | Dropdown | Text |
| Decision criteria defined | Dropdown | Text | N/A | Dropdown | Text |
| Conflict resolution process | Dropdown | Text | N/A | Dropdown | Text |
| Emergency CAB procedures | Dropdown | Text | Text (e.g., "<4 hours") | Dropdown | Text |
| Virtual CAB option available | Dropdown | Text | N/A | Dropdown | Text |
| CAB effectiveness reviewed | Dropdown | Text | Text (e.g., "Annually") | Dropdown | Text |

### CAB Metrics (Rows 37-45)

| Metric | Last Quarter Value | Target | Status | Notes |
|--------|-------------------|--------|--------|-------|
| CAB meeting frequency | Text (e.g., "12 meetings") | Text | Formula: Green/Yellow/Red | Text |
| Average attendance rate | Text (e.g., "82%") | Text (e.g., ">80%") | Formula | Text |
| Changes reviewed by CAB | Text | Text | Formula | Text |
| CAB decisions overturned | Text | Text (e.g., "<5%") | Formula | Text |
| Average review duration | Text | Text | Formula | Text |

---

## Sheet 5: Communication_Stakeholder_Mgmt

### Purpose
Assess stakeholder communication procedures and effectiveness.

### Header Section
**Row 1:** "COMMUNICATION & STAKEHOLDER MANAGEMENT"  
**Row 2:** "Document how changes are communicated to affected stakeholders"

### Communication Procedures (Rows 4-20)

| Communication Type | Documented | Method | Timing | Template Exists | Status | Evidence |
|--------------------|------------|--------|--------|-----------------|--------|----------|
| Pre-change notification (users) | Dropdown: Yes/No | Text (e.g., "Email") | Text (e.g., "48h advance") | Dropdown: Yes/No | Dropdown: ✅/⚠️/❌ | Text |
| Pre-change notification (technical teams) | Dropdown | Text | Text | Dropdown | Dropdown | Text |
| Change approval notification | Dropdown | Text | Text | Dropdown | Dropdown | Text |
| Change schedule updates | Dropdown | Text | Text | Dropdown | Dropdown | Text |
| Implementation start notification | Dropdown | Text | Text | Dropdown | Dropdown | Text |
| Progress updates during change | Dropdown | Text | Text | Dropdown | Dropdown | Text |
| Change completion notification | Dropdown | Text | Text | Dropdown | Dropdown | Text |
| Rollback notification | Dropdown | Text | Text | Dropdown | Dropdown | Text |
| Post-implementation summary | Dropdown | Text | Text | Dropdown | Dropdown | Text |
| Incident/issue alerts | Dropdown | Text | Text | Dropdown | Dropdown | Text |

### Stakeholder Management Assessment (Rows 22-35)

| Requirement | Implemented | Details | Status | Evidence |
|-------------|-------------|---------|--------|----------|
| Stakeholder identification process | Dropdown: Yes/No/Partial | Text | Dropdown: ✅/⚠️/❌ | Text |
| Communication plan template | Dropdown | Text | Dropdown | Text |
| Communication channels defined | Dropdown | Text | Dropdown | Text |
| Advance notice requirements | Dropdown | Text | Dropdown | Text |
| Feedback mechanisms | Dropdown | Text | Dropdown | Text |
| Communication effectiveness measured | Dropdown | Text | Dropdown | Text |
| Communication failures tracked | Dropdown | Text | Dropdown | Text |

---

## Sheet 6: Documentation_Record_Keeping

### Purpose
Assess documentation and record-keeping practices for changes.

### Header Section
**Row 1:** "DOCUMENTATION & RECORD KEEPING"  
**Row 2:** "Document what information is captured and retained for changes"

### Change Record Documentation (Rows 4-30)

| Information Element | Captured | System/Location | Retention Period | Status | Evidence |
|---------------------|----------|-----------------|------------------|--------|----------|
| Change request ID | Dropdown: Yes/No | Text | Text | Dropdown: ✅/⚠️/❌ | Text |
| Requestor information | Dropdown | Text | Text | Dropdown | Text |
| Change description | Dropdown | Text | Text | Dropdown | Text |
| Business justification | Dropdown | Text | Text | Dropdown | Text |
| Systems affected | Dropdown | Text | Text | Dropdown | Text |
| Risk assessment | Dropdown | Text | Text | Dropdown | Text |
| Impact assessment | Dropdown | Text | Text | Dropdown | Text |
| Change classification | Dropdown | Text | Text | Dropdown | Text |
| Approval records | Dropdown | Text | Text | Dropdown | Text |
| CAB review notes | Dropdown | Text | Text | Dropdown | Text |
| Implementation plan | Dropdown | Text | Text | Dropdown | Text |
| Test results | Dropdown | Text | Text | Dropdown | Text |
| Rollback plan | Dropdown | Text | Text | Dropdown | Text |
| Communication records | Dropdown | Text | Text | Dropdown | Text |
| Implementation logs | Dropdown | Text | Text | Dropdown | Text |
| Verification results | Dropdown | Text | Text | Dropdown | Text |
| PIR results | Dropdown | Text | Text | Dropdown | Text |
| Lessons learned | Dropdown | Text | Text | Dropdown | Text |
| Change closure date | Dropdown | Text | Text | Dropdown | Text |

### Documentation Update Requirements (Rows 32-45)

| Documentation Type | Updated After Changes | Update Timeframe | Verified | Status | Evidence |
|--------------------|----------------------|------------------|----------|--------|----------|
| System configuration docs | Dropdown: Yes/No/Sometimes | Text (e.g., "5 days") | Dropdown: Yes/No | Dropdown: ✅/⚠️/❌ | Text |
| Network diagrams | Dropdown | Text | Dropdown | Dropdown | Text |
| Application architecture | Dropdown | Text | Dropdown | Dropdown | Text |
| Operational procedures | Dropdown | Text | Dropdown | Dropdown | Text |
| Runbooks | Dropdown | Text | Dropdown | Dropdown | Text |
| Troubleshooting guides | Dropdown | Text | Dropdown | Dropdown | Text |
| User documentation | Dropdown | Text | Dropdown | Dropdown | Text |
| Continuity/DR plans | Dropdown | Text | Dropdown | Dropdown | Text |

### Record Retention Assessment (Rows 47-55)

| Requirement | Implemented | Details | Status | Evidence |
|-------------|-------------|---------|--------|----------|
| Retention policy defined | Dropdown: Yes/No | Text (period) | Dropdown: ✅/⚠️/❌ | Text |
| Retention enforced | Dropdown | Text | Dropdown | Text |
| Records immutable | Dropdown | Text | Dropdown | Text |
| Audit trail complete | Dropdown | Text | Dropdown | Text |
| Records accessible for audit | Dropdown | Text | Dropdown | Text |

---

## Sheet 7: Tool_Capabilities

### Purpose
Inventory change management tools and assess capabilities.

### Header Section
**Row 1:** "CHANGE MANAGEMENT TOOL CAPABILITIES"  
**Row 2:** "Document tools used and their capabilities"

### Tool Inventory (Rows 4-15)

| Tool/System | Vendor/Type | Version | Purpose | User Count | License Status | Status | Notes |
|-------------|-------------|---------|---------|------------|----------------|--------|-------|
| Text (e.g., "ServiceNow") | Text | Text | Text | Text | Text (e.g., "Current") | Dropdown: ✅/⚠️/❌ | Text |
| [Additional tools] | Text | Text | Text | Text | Text | Dropdown | Text |

### Tool Capability Assessment (Rows 17-45)

| Capability | Required | Implemented | Tool/System | Effectiveness | Status | Gap/Notes |
|------------|----------|-------------|-------------|---------------|--------|-----------|
| Change request creation | Dropdown: Yes | Dropdown: Yes/No/Partial | Text | Dropdown: High/Medium/Low | Dropdown: ✅/⚠️/❌ | Text |
| Unique change ID generation | Dropdown | Dropdown | Text | Dropdown | Dropdown | Text |
| Workflow automation | Dropdown | Dropdown | Text | Dropdown | Dropdown | Text |
| Approval routing | Dropdown | Dropdown | Text | Dropdown | Dropdown | Text |
| CAB scheduling | Dropdown | Dropdown | Text | Dropdown | Dropdown | Text |
| Change calendar | Dropdown | Dropdown | Text | Dropdown | Dropdown | Text |
| Communication/notifications | Dropdown | Dropdown | Text | Dropdown | Dropdown | Text |
| Documentation attachment | Dropdown | Dropdown | Text | Dropdown | Dropdown | Text |
| Audit trail/logging | Dropdown | Dropdown | Text | Dropdown | Dropdown | Text |
| Reporting/analytics | Dropdown | Dropdown | Text | Dropdown | Dropdown | Text |
| Integration with CMDB | Dropdown | Dropdown | Text | Dropdown | Dropdown | Text |
| Integration with incident mgmt | Dropdown | Dropdown | Text | Dropdown | Dropdown | Text |
| Mobile access | Recommended | Dropdown | Text | Dropdown | Dropdown | Text |
| API availability | Recommended | Dropdown | Text | Dropdown | Dropdown | Text |

### Tool Gaps & Limitations (Rows 47-55)

| Gap/Limitation | Impact | Workaround | Remediation Plan | Target Date | Status |
|----------------|--------|------------|------------------|-------------|--------|
| Text | Dropdown: High/Medium/Low | Text | Text | Date DD.MM.YYYY | Dropdown: ✅/⚠️/❌/📋 |

---

## Sheet 8: Metrics_KPIs

### Purpose
Document change management metrics and performance indicators.

### Header Section
**Row 1:** "CHANGE MANAGEMENT METRICS & KPIs"  
**Row 2:** "Track change process performance and effectiveness"

### Tracked Metrics (Rows 4-25)

| Metric | Tracked | Frequency | Last Period Value | Target | Status | Tool/Method |
|--------|---------|-----------|-------------------|--------|--------|-------------|
| Total changes (all types) | Dropdown: Yes/No | Text (e.g., "Monthly") | Text | Text | Formula: Green/Yellow/Red | Text |
| Standard changes | Dropdown | Text | Text | Text | Formula | Text |
| Normal changes | Dropdown | Text | Text | Text | Formula | Text |
| Emergency changes | Dropdown | Text | Text | Text | Formula | Text |
| Emergency change % | Dropdown | Text | Text (e.g., "8%") | Text (e.g., "<5%") | Formula | Text |
| Change success rate | Dropdown | Text | Text (e.g., "94%") | Text (e.g., ">95%") | Formula | Text |
| Change failure rate | Dropdown | Text | Text | Text | Formula | Text |
| Failed changes causing incidents | Dropdown | Text | Text | Text | Formula | Text |
| Average change duration | Dropdown | Text | Text | Text | Formula | Text |
| Changes exceeding window | Dropdown | Text | Text | Text | Formula | Text |
| Rollback rate | Dropdown | Text | Text | Text | Formula | Text |
| PIR completion rate | Dropdown | Text | Text (e.g., "78%") | Text (e.g., ">90%") | Formula | Text |
| CAB attendance rate | Dropdown | Text | Text | Text | Formula | Text |
| Changes per system/app | Dropdown | Text | Text | Text | Formula | Text |
| Change backlog | Dropdown | Text | Text | Text | Formula | Text |
| Unauthorized changes detected | Dropdown | Text | Text | Text | Formula | Text |

### KPI Reporting (Rows 27-35)

| Report | Frequency | Recipients | Reviewed By | Action Taken | Status | Evidence |
|--------|-----------|------------|-------------|--------------|--------|----------|
| Change volume report | Text | Text | Text | Text | Dropdown: ✅/⚠️/❌ | Text |
| Change success/failure report | Text | Text | Text | Text | Dropdown | Text |
| Emergency change analysis | Text | Text | Text | Text | Dropdown | Text |
| Trend analysis | Text | Text | Text | Text | Dropdown | Text |
| Executive dashboard | Text | Text | Text | Text | Dropdown | Text |

---

## Sheet 9: Evidence_Register

### Purpose
Centralized evidence repository linking to all supporting documentation.

### Header Section
**Row 1:** "EVIDENCE REGISTER"  
**Row 2:** "Document evidence location for all assessed requirements"

### Evidence Inventory (Rows 4-100)

| Requirement ID | Requirement Description | Evidence Type | Evidence Location | Last Verified | Accessible To | Status | Notes |
|----------------|------------------------|---------------|-------------------|---------------|---------------|--------|-------|
| REQ-PROCESS-001 | Change request procedures | Text (e.g., "Policy Document") | Text (path/URL) | Date DD.MM.YYYY | Text (role) | Dropdown: ✅/⚠️/❌ | Text |
| REQ-PROCESS-002 | Risk assessment | Text | Text | Date | Text | Dropdown | Text |
| [Continue for all requirements] | Text | Text | Text | Date | Text | Dropdown | Text |

**Column Widths:**

- A: 18, B: 35, C: 20, D: 35, E: 15, F: 20, G: 12, H: 25

---

## Sheet 10: Summary_Dashboard

### Purpose
Executive summary with compliance scoring and audit readiness.

### Header Section
**Row 1:** "CHANGE PROCESS ASSESSMENT - SUMMARY DASHBOARD"  
**Row 2:** "Overall compliance status and key findings"  
**Row 3:** Date and organization info (formulas from Instructions sheet)

### Overall Compliance (Rows 5-12)

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| **Overall Compliance %** | Formula: AVG(all status columns) | 90% | Formula: Color-coded cell |
| Requirements Assessed | Formula: COUNT | N/A | Auto |
| Fully Compliant (✅) | Formula: COUNTIF | N/A | Auto |
| Partially Compliant (⚠️) | Formula: COUNTIF | N/A | Auto |
| Non-Compliant (❌) | Formula: COUNTIF | N/A | Auto |
| Planned (📋) | Formula: COUNTIF | N/A | Auto |

### Compliance by Domain (Rows 14-24)

| Domain | Requirements | Compliant | Partial | Non-Compliant | Compliance % | Status |
|--------|--------------|-----------|---------|---------------|--------------|--------|
| Change Process Workflow | Formula: COUNT | Formula | Formula | Formula | Formula | Color cell |
| Approval Authority | Formula | Formula | Formula | Formula | Formula | Color cell |
| CAB Operations | Formula | Formula | Formula | Formula | Formula | Color cell |
| Communication | Formula | Formula | Formula | Formula | Formula | Color cell |
| Documentation | Formula | Formula | Formula | Formula | Formula | Color cell |
| Tool Capabilities | Formula | Formula | Formula | Formula | Formula | Color cell |
| Metrics & KPIs | Formula | Formula | Formula | Formula | Formula | Color cell |

### Critical Findings (Rows 26-35)

**Section Header (RED):** "CRITICAL GAPS REQUIRING IMMEDIATE ATTENTION"

| Domain | Finding | Severity | Assigned To | Target Date | Status |
|--------|---------|----------|-------------|-------------|--------|
| Auto-populate from sheets | Text | Critical/High/Medium | Text | Date DD.MM.YYYY | Dropdown: ✅/⚠️/❌/📋 |

### Audit Readiness (Rows 37-45)

| Criterion | Status | Notes |
|-----------|--------|-------|
| All processes documented | Formula | Text |
| Evidence complete | Formula | Text |
| Roles defined | Formula | Text |
| Tools adequate | Formula | Text |
| Metrics tracked | Formula | Text |
| Compliance ≥70% | Formula | Text |
| **OVERALL AUDIT READY** | Formula: Yes/No/Conditional | Text |

**Column Widths:**

- A: 35, B: 15, C: 25

---

## Sheet 11: Approval_Sign_Off

### Purpose
Final approval and sign-off for assessment.

### Header Section
**Row 1:** "ASSESSMENT APPROVAL & SIGN-OFF"  
**Row 2:** "Formal approval of completed assessment"

### Assessment Metadata (Rows 4-12)

| Attribute | Value |
|-------|-------|
| Assessment Completion Date | Date picker (yellow cell) |
| Overall Compliance | Formula from Summary_Dashboard |
| Critical Gaps Count | Formula from Summary_Dashboard |
| Assessment Status | Dropdown: Draft / Under Review / Final / Rejected |
| Next Review Date | Date picker (yellow cell) |

### Approvals (Rows 14-25)

| Role | Name | Signature/Approval | Date | Comments |
|------|------|-------------------|------|----------|
| Assessment Owner (Change Manager) | Text | Dropdown: Approved/Rejected | Date picker | Text |
| CAB Chair | Text | Dropdown | Date picker | Text |
| Compliance Officer | Text | Dropdown | Date picker | Text |
| CISO | Text | Dropdown | Date picker | Text |

### Conditional Approval (if applicable) (Rows 27-30)

| Condition | Responsibility | Target Date | Status |
|-----------|---------------|-------------|--------|
| Text | Text | Date | Dropdown: ✅/⚠️/❌/📋 |

---

## Appendix: Technical Notes for Developers

### Formula Patterns

**Status Column Formulas:**
```excel
=IF(C5="Yes","✅",IF(C5="Partial","⚠️",IF(C5="No","❌","N/A")))
```

**Compliance Percentage:**
```excel
=COUNTIF(StatusRange,"✅")/(COUNTA(StatusRange)-COUNTIF(StatusRange,"N/A"))*100
```

**Conditional Formatting Rules:**

- Green (C6EFCE): Cell value = "✅"
- Yellow (FFEB9C): Cell value = "⚠️"  
- Red (FFC7CE): Cell value = "❌"
- Blue (B4C7E7): Cell value = "📋"
- Gray: Cell value = "N/A"

### Data Validation

**Status Dropdowns:**
```
List: ✅,⚠️,❌,📋,N/A
```

**Yes/No/Partial Dropdowns:**
```
List: Yes,No,Partial,N/A
```

**Severity Levels:**
```
List: Critical,High,Medium,Low
```

### Cell Protection

- **Protected:** All formula cells, headers, instructions
- **Unprotected:** Yellow input cells, text entry areas, status dropdowns
- **Sheet Protection Password:** [Organization-defined]

---

**END OF SPECIFICATION**

---

*"The enemy knows the system. Security through obscurity is not security at all."*
— Adi Shamir

<!-- QA_VERIFIED: 2026-02-06 -->
