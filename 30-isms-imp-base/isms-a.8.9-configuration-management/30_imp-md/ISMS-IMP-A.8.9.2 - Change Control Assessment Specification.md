**ISMS-IMP-A.8.9.2**
**Assessment Specification with User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.9: Configuration Management

**Document ID**: ISMS-IMP-A.8.9.2  
**Title**: Change Control Assessment Specification  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Configuration Manager  
**Status**: Draft  

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.9.2 |
| **Version** | 1.0 |
| **Assessment Area** | Change Control and Configuration Updates - Change Classification, CAB Operations, Approval Workflows, Testing, Rollback |
| **Related Policy** | ISMS-POL-A.8.9, Section 2.3 (Change Control & Configuration Updates) |
| **Purpose** | Assess change control processes, CAB operations, approval workflows, testing procedures, and rollback capabilities for configuration changes to ensure controlled and authorized modifications |
| **Target Audience** | Configuration Manager, CAB Members, Change Coordinators, System Administrators, IT Operations, Service Owners, Compliance Officers, Auditors |
| **Assessment Type** | Technical & Operational |
| **Review Cycle** | Quarterly or After Major Infrastructure Changes |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Change Control assessment workbook | ISMS Implementation Team |

### Approvers

- Primary: Configuration Manager
- Technical Review: Security Architect
- Security Review: Chief Information Security Officer (CISO)


### Distribution

Configuration management team, system administrators, IT operations, security engineers, auditors

### Related Documents

- ISMS-POL-A.8.9: Configuration Management Policy (Consolidated)
- ISMS-CTX-A.8.9: Configuration Management Reference (NOT ISMS)

# Assessment Purpose

## Objective

This assessment evaluates the effectiveness of configuration change management processes across [Organization]'s information assets. The assessment verifies that all configuration changes follow controlled procedures including impact assessment, approval workflows, testing validation, and rollback capability. This provides objective evidence of compliance with ISO 27001:2022 Control A.8.9 change control requirements.

**Implementer Perspective**: This workbook provides a systematic framework for tracking configuration changes from request through implementation, documenting the approval chain, validating testing procedures, and measuring change success rates. It enables [Organization] to demonstrate disciplined change management practices.

**Auditor Perspective**: This assessment generates quantitative metrics (change success rate, approval compliance, testing coverage, emergency change ratio) that demonstrate [Organization]'s capability to manage configuration changes in a controlled manner. Evidence collected supports verification that unauthorized or inadequately tested changes are prevented.

## Assessment Scope

This assessment addresses the change control domain of Control A.8.9, specifically:

**In Scope**:

- Configuration change request documentation and tracking
- Multi-tier approval workflows and authorization chains
- Impact and risk assessment for proposed changes
- Pre-deployment testing and validation procedures
- Change implementation execution and verification
- Rollback capability and procedures
- Emergency change management (expedited process with post-facto review)
- Change success metrics and failure analysis
- Integration with baseline management (ISMS-IMP-A.8.9.1)


**Out of Scope** (covered in other assessments):

- Configuration baseline definition and documentation (see ISMS-IMP-A.8.9.1)
- Configuration drift detection and monitoring (see ISMS-IMP-A.8.9.3)
- Security hardening standards compliance (see ISMS-IMP-A.8.9.4)
- Business continuity and disaster recovery (separate control)


## Control Alignment

This assessment implements requirements from:

- **ISMS-POL-A.8.9, Section 2.3**: Change Control Requirements (complete section)
- **ISMS-CTX-A.8.9, Part 2**: Change Request Form Template (reference annex)
- **ISO 27001:2022 A.8.9**: Configuration management control requirements
- **Related Controls**: A.5.37 (Documented Operating Procedures), A.8.16 (Monitoring Activities)


---

# PART I: USER COMPLETION GUIDE
**Audience:** Security assessors, Control owners, Compliance officers

---

# Assessment Scope Definition

## Change Types

This assessment tracks four primary change types, each with different approval requirements and urgency:

**Standard Changes**:

- Pre-approved, low-risk changes with documented procedures
- Examples: Monthly security patching, routine configuration updates, scheduled maintenance
- Approval: Pre-authorized by Change Advisory Board (CAB)
- Timeline: Executed according to pre-defined schedule
- Testing: Standard validation procedures apply


**Normal Changes**:

- Planned changes requiring individual assessment and approval
- Examples: Application upgrades, infrastructure modifications, new feature deployments
- Approval: CAB review and approval required
- Timeline: 7-14 days minimum from request to implementation
- Testing: Comprehensive testing in non-production environment required


**Emergency Changes**:

- Urgent changes required to resolve critical incidents or vulnerabilities
- Examples: Critical security patches, incident remediation, system recovery
- Approval: Emergency CAB (ECAB) with limited membership, post-implementation review required
- Timeline: Expedited (hours to 1-2 days)
- Testing: Abbreviated testing acceptable if fully documented


**Hot Fixes**:

- Immediate changes to restore service availability or security
- Examples: Fixing active security exploit, restoring failed critical service
- Approval: CIO/CISO approval, immediate CAB notification, full retrospective review
- Timeline: Immediate (minutes to hours)
- Testing: Minimal or post-implementation testing, comprehensive rollback plan mandatory


## Change Priorities

Changes are prioritized based on urgency and business impact:

| Priority | Definition | Response Time | Typical Change Type |
|----------|------------|---------------|---------------------|
| **P1 - Critical** | Immediate action required; critical system down or severe security threat | <4 hours | Hot Fix, Emergency |
| **P2 - High** | Urgent change needed; significant impact on operations | <24 hours | Emergency, Normal |
| **P3 - Medium** | Important but not urgent; scheduled implementation acceptable | <7 days | Normal, Standard |
| **P4 - Low** | Minor change; can be bundled with other changes | <30 days | Standard, Normal |

## Approval Tiers

[Organization] implements a risk-based approval framework:

**Single-Tier Approval** (Low Risk):

- Standard changes (pre-approved category)
- Changes to non-production environments
- Cosmetic changes with no functional impact
- Approver: Change Coordinator or Team Lead


**Two-Tier Approval** (Medium Risk):

- Normal changes to production systems (non-critical)
- Changes affecting single application or system
- Minor infrastructure modifications
- Approvers: (1) Technical Lead, (2) Service Owner


**Three-Tier Approval** (High Risk):

- Changes to critical systems or infrastructure
- Changes with cross-functional impact
- Major architectural modifications
- Security-sensitive changes
- Approvers: (1) Technical Lead, (2) Service Owner, (3) CAB Chair or CIO/CISO


**Emergency Approval** (Special Process):

- Emergency and Hot Fix changes
- Verbal approval acceptable (documented immediately)
- Approvers: Minimum 2 of: CIO, CISO, IT Manager
- Post-Implementation Review: Full CAB review within 5 business days


---

# Assessment Methodology

## Assessment Workflow

**Three-Tier Assessment Process**:

1. **Preparer** (Change Coordinator, System Administrators):

   - Document all configuration changes in Change Request Register
   - Complete impact assessment and risk analysis
   - Document testing validation results
   - Track implementation execution
   - Record emergency changes and post-facto justification
   - Timeline: Ongoing (continuous change tracking)


2. **Reviewer** (Configuration Manager, CAB Chair):

   - Verify completeness of change documentation
   - Validate approval workflows were followed
   - Review testing adequacy
   - Assess emergency change justifications
   - Analyze change success/failure trends
   - Identify process improvement opportunities
   - Timeline: Monthly or quarterly review


3. **Approver** (IT Manager, CISO):

   - Review overall change management effectiveness
   - Approve change process compliance metrics
   - Authorize remediation for process gaps
   - Sign off on assessment completion
   - Timeline: Quarterly or semi-annual approval


## Data Collection Approach

**Change Request Register**: Primary source of truth for all configuration changes. Each change receives unique ID, is tracked through complete lifecycle (request → approval → testing → implementation → verification), and outcome is recorded (successful, failed, rolled back).

**Change Approval Workflow**: Tracks approval chain for each change. Documents who approved at each tier, when approval was granted, and method (CAB meeting, email, emergency verbal approval). Critical for audit trail.

**Impact Assessment**: Risk and impact analysis performed for each change. Documents affected systems, potential risks, mitigation strategies, and business impact if change fails. Required before approval.

**Testing Validation**: Evidence that changes were tested before production deployment. Records test environment, test results, identified issues, and go/no-go decision. Exception: Emergency changes may have abbreviated testing (documented).

**Implementation Log**: Execution record for each change. Documents implementation date/time, implementer, actual steps performed, verification that change achieved intended result, and any deviations from plan.

**Rollback Capability**: Verification that rollback procedures exist and have been tested. Documents rollback trigger criteria, rollback steps, estimated rollback time, and rollback testing results.

**Emergency Changes**: Special tracking for expedited changes. Ensures emergency process is not abused (should be <10% of total changes), post-facto documentation is completed, and CAB retrospective review occurs.

## Assessment Frequency

**Initial Assessment**: Complete change control assessment within 90 days of ISMS implementation for A.8.9.

**Ongoing Assessment**: 

- **Monthly metrics review**: Change success rate, emergency change ratio, approval compliance
- **Quarterly comprehensive assessment**: Full review of all sheets, trend analysis, gap identification
- **Ad-hoc assessment**: After major incidents involving configuration changes, after significant process changes


**Continuous Updates**: Change Request Register updated in real-time as changes are requested, approved, implemented. Assessment provides periodic consolidation and analysis of this continuous data.

---

# Workbook Structure Overview

**Generated Workbook Name**: `ISMS_A_8_9_2_Change_Control_Assessment_YYYYMMDD.xlsx`

**Total Sheets**: 12

| Sheet # | Sheet Name | Purpose | Row Count |
|---------|------------|---------|-----------|
| 1 | Instructions | Usage guidance, roles, workflow, legend | N/A |
| 2 | Change_Request_Register | All configuration changes tracking | 100 data rows |
| 3 | Change_Approval_Workflow | Approval chain tracking | 100 data rows |
| 4 | Impact_Assessment | Risk and impact analysis per change | 100 data rows |
| 5 | Testing_Validation | Pre-deployment testing records | 100 data rows |
| 6 | Implementation_Log | Deployment execution records | 100 data rows |
| 7 | Rollback_Capability | Rollback procedures and testing | 100 data rows |
| 8 | Emergency_Changes | Emergency change tracking | 50 data rows |
| 9 | Change_Success_Metrics | Auto-calculated success rates, trends | N/A (formulas) |
| 10 | Compliance_Dashboard | Process adherence metrics | N/A (formulas) |
| 11 | Evidence_Register | Supporting evidence and documentation | 100 data rows |
| 12 | Approval_Sign_Off | Three-tier approval signatures | N/A (3 rows) |

**Sheet Relationship Flow**:
```
Change_Request_Register → (change list) → Change_Approval_Workflow
                                                  ↓
Impact_Assessment → (risk analysis) → Testing_Validation
                                              ↓
Implementation_Log → (execution) → Rollback_Capability
                                              ↓
Emergency_Changes → (expedited tracking) → Change_Success_Metrics
                                                      ↓
Compliance_Dashboard → (process metrics) → Evidence_Register
                                                      ↓
Approval_Sign_Off
```

---

# Detailed Sheet Specifications

## Sheet 1: Instructions

**Purpose**: Provides comprehensive guidance on using the assessment workbook, defines change types and priorities, explains approval workflows, and includes a legend for status values.

**Content Structure** (not row-based):

- Assessment overview and objectives
- Change types and priorities definitions
- Approval tier requirements by risk level
- Step-by-step completion instructions
- Three-tier assessment workflow diagram
- Status value definitions and color legend
- Integration with other assessments (baseline, monitoring)
- Common questions and troubleshooting
- Contact information for Change Advisory Board


**Formatting**:

- Title section: Bold, 16pt, dark blue background (003366)
- Section headers: Bold, 14pt, light blue background (4472C4)
- Body text: Regular, 11pt Calibri
- Color legend showing: Green (Approved/Successful), Yellow (Pending/In Progress), Red (Rejected/Failed), Gray (Cancelled/N/A)


**No Data Entry**: This is a read-only informational sheet.

---

## Sheet 2: Change_Request_Register

**Purpose**: Primary register of all configuration changes. Each change receives unique ID and is tracked through complete lifecycle from request to post-implementation review.

**Column Structure**:

| Column | Header | Data Type | Validation | Description |
|--------|--------|-----------|------------|-------------|
| A | Change ID | Text | Free text | Unique identifier (e.g., "CHG-2026-001") |
| B | Change Title | Text | Free text | Brief descriptive title of change |
| C | Change Type | Text | Dropdown | Standard, Normal, Emergency, Hot Fix |
| D | Priority | Text | Dropdown | P1-Critical, P2-High, P3-Medium, P4-Low |
| E | Affected Systems/Assets | Text | Free text | Systems impacted by change (comma-separated) |
| F | Requestor Name | Text | Free text | Person requesting the change |
| G | Requestor Contact | Text | Free text | Email or phone |
| H | Request Date | Date | Date format | Date change was requested |
| I | Required Implementation Date | Date | Date format | Target date for implementation |
| J | Change Status | Text | Dropdown | Draft, Submitted, Approved, In Testing, Scheduled, Implementing, Completed, Failed, Rolled Back, Cancelled |
| K | Current Phase | Text | Formula | Auto-calculated based on Change Status |
| L | Days in Current Phase | Number | Formula | Days since last status change |
| M | Overall Status Indicator | Text | Formula | On Track, At Risk, Delayed, Complete |
| N | Notes | Text | Free text | Additional context or updates |

**Row Allocation**: 100 data rows (Row 3 to Row 102)

**Freeze Panes**: B3 (Column headers and Change ID always visible)

**Data Validations**:

- Column C (Change Type): Dropdown list
  - Values: "Standard, Normal, Emergency, Hot Fix"
  - Allow blank: No (required field)
  - Error alert: "Please select a valid change type"

- Column D (Priority): Dropdown list
  - Values: "P1-Critical, P2-High, P3-Medium, P4-Low"
  - Allow blank: No (required field)
  - Error alert: "Please select priority level"

- Column J (Change Status): Dropdown list
  - Values: "Draft, Submitted, Approved, In Testing, Scheduled, Implementing, Completed, Failed, Rolled Back, Cancelled"
  - Allow blank: No (required field)
  - Error alert: "Please select change status"

- Column H (Request Date), Column I (Required Implementation Date): Date format DD.MM.YYYY


**Formulas**:

- Column K (Current Phase): 

```
  =IF(J3="Draft","Planning",IF(J3="Submitted","Approval",IF(J3="Approved","Testing",IF(J3="In Testing","Testing",IF(J3="Scheduled","Pre-Implementation",IF(J3="Implementing","Implementation",IF(OR(J3="Completed",J3="Failed",J3="Rolled Back",J3="Cancelled"),"Closed","Unknown")))))))
```

  - Explanation: Maps status to lifecycle phase

- Column L (Days in Current Phase): 

```
  =IF(H3="","",TODAY()-H3)
```

  - Explanation: Days since request (simplified - in practice would track status change dates)
  - Note: Real implementation might add hidden column for "Last Status Change Date"

- Column M (Overall Status Indicator):

```
  =IF(OR(J3="Completed",J3="Cancelled"),"Complete",IF(L3>30,"Delayed",IF(L3>14,"At Risk","On Track")))
```

  - Explanation: Status health indicator based on time in phase


**Conditional Formatting**:

- Column C (Change Type):
  - "Emergency" → Orange text (highlights emergency changes)
  - "Hot Fix" → Red text, bold (highlights urgent changes)

- Column D (Priority):
  - "P1-Critical" → Red fill (FFC7CE), bold
  - "P2-High" → Yellow fill (FFEB9C)

- Column J (Change Status):
  - "Completed" → Green fill (C6EFCE)
  - "Failed" → Red fill (FFC7CE)
  - "Rolled Back" → Orange fill
  - "Approved", "Scheduled" → Light green fill (E2EFDA)
  - "Draft", "Submitted" → Light yellow fill (FFFFCC)

- Column M (Overall Status Indicator):
  - "Complete" → Green text, bold
  - "On Track" → Black text
  - "At Risk" → Orange text, bold
  - "Delayed" → Red text, bold


**Special Features**:

- Row 2: Column headers with light gray background (D9D9D9), bold text, centered alignment
- Row 1: Title "Change Request Register - Configuration Change Tracking" spanning A1:N1, merged, dark blue background
- Protected cells: Columns K, L, M (formula cells) locked
- Filter: Enable auto-filter on header row to filter by Change Type, Priority, Status


**Usage Notes**:

- Preparer: Create new row for each configuration change request
- Change ID should follow organizational convention (e.g., CHG-YYYY-NNN)
- Update Change Status as change progresses through lifecycle
- Reference this Change ID in all other sheets for traceability


---

## Sheet 3: Change_Approval_Workflow

**Purpose**: Track approval chain for each change. Documents who approved at each tier, approval timestamps, and approval method. Critical for audit trail and compliance verification.

**Column Structure**:

| Column | Header | Data Type | Validation | Description |
|--------|--------|-----------|------------|-------------|
| A | Change ID | Text | Free text | Reference to Change_Request_Register |
| B | Change Title | Text | Free text | Brief title for reference |
| C | Approval Tier Required | Text | Dropdown | Single-Tier, Two-Tier, Three-Tier, Emergency |
| D | Tier 1 Approver Name | Text | Free text | First approver (Technical Lead) |
| E | Tier 1 Approval Status | Text | Dropdown | Pending, Approved, Rejected, N/A |
| F | Tier 1 Approval Date | Date | Date format | Date Tier 1 approved |
| G | Tier 2 Approver Name | Text | Free text | Second approver (Service Owner) |
| H | Tier 2 Approval Status | Text | Dropdown | Pending, Approved, Rejected, N/A |
| I | Tier 2 Approval Date | Date | Date format | Date Tier 2 approved |
| J | Tier 3 Approver Name | Text | Free text | Third approver (CAB Chair/CIO/CISO) |
| K | Tier 3 Approval Status | Text | Dropdown | Pending, Approved, Rejected, N/A |
| L | Tier 3 Approval Date | Date | Date format | Date Tier 3 approved |
| M | Approval Method | Text | Dropdown | CAB Meeting, Email Approval, Emergency Verbal, Automated (Standard) |
| N | Approval Reference | Text | Free text | Meeting minutes, email thread, ticket number |
| O | Overall Approval Status | Text | Formula | Approved, Partially Approved, Rejected, Pending |
| P | Days to Full Approval | Number | Formula | Days from request to final approval |
| Q | Notes | Text | Free text | Approval conditions, reasons for rejection |

**Row Allocation**: 100 data rows (Row 3 to Row 102)

**Freeze Panes**: B3

**Data Validations**:

- Column C (Approval Tier Required): Dropdown list
  - Values: "Single-Tier, Two-Tier, Three-Tier, Emergency"
  - Allow blank: No

- Column E, H, K (Approval Status): Dropdown list
  - Values: "Pending, Approved, Rejected, N/A"
  - Allow blank: Yes
  - N/A = This tier not required for this change

- Column M (Approval Method): Dropdown list
  - Values: "CAB Meeting, Email Approval, Emergency Verbal, Automated (Standard), Not Applicable"
  - Allow blank: Yes

- Date columns (F, I, L): Date format DD.MM.YYYY


**Formulas**:

- Column O (Overall Approval Status):

```
  =IF(C3="Single-Tier",IF(E3="Approved","Approved",IF(E3="Rejected","Rejected","Pending")),
     IF(C3="Two-Tier",IF(AND(E3="Approved",H3="Approved"),"Approved",IF(OR(E3="Rejected",H3="Rejected"),"Rejected",IF(AND(E3="Approved",H3="Pending"),"Partially Approved","Pending"))),
     IF(C3="Three-Tier",IF(AND(E3="Approved",H3="Approved",K3="Approved"),"Approved",IF(OR(E3="Rejected",H3="Rejected",K3="Rejected"),"Rejected",IF(AND(E3="Approved",H3="Approved",K3="Pending"),"Partially Approved","Pending"))),
     "Unknown")))
```

  - Explanation: Complex logic to determine overall status based on required tiers and individual approvals

- Column P (Days to Full Approval):

```
  =IF(O3="Approved",IF(C3="Single-Tier",F3-VLOOKUP(A3,Change_Request_Register!$A$3:$H$102,8,FALSE),
     IF(C3="Two-Tier",I3-VLOOKUP(A3,Change_Request_Register!$A$3:$H$102,8,FALSE),
     L3-VLOOKUP(A3,Change_Request_Register!$A$3:$H$102,8,FALSE))),"")
```

  - Explanation: Calculates days from request date to final approval date
  - Note: VLOOKUP fetches request date from Change_Request_Register


**Conditional Formatting**:

- Columns E, H, K (Approval Status):
  - "Approved" → Green fill (C6EFCE)
  - "Rejected" → Red fill (FFC7CE)
  - "Pending" → Yellow fill (FFEB9C)
  - "N/A" → Gray fill (D9D9D9)

- Column O (Overall Approval Status):
  - "Approved" → Green fill, bold text
  - "Rejected" → Red fill, bold text
  - "Partially Approved" → Yellow fill
  - "Pending" → Light yellow fill

- Column P (Days to Full Approval):
  - >14 days → Red fill (approval took too long)
  - 8-14 days → Yellow fill (approaching SLA)
  - <8 days → Green fill (fast approval)


**Special Features**:

- Row 2: Column headers with light gray background
- Row 1: Title "Change Approval Workflow Tracking" spanning A1:Q1
- Protected cells: Columns O and P (formula cells) locked
- Approval tier logic: If Tier 2 or Tier 3 not required (N/A), they don't block overall approval


**Usage Notes**:

- Preparer: Create entry when change is submitted for approval
- Update each tier's approval status as approvals are granted
- For Emergency changes, document verbal approval immediately and get written confirmation within 24 hours
- Approval Reference (Column N) is critical for audit - must link to verifiable record
- Standard changes (pre-approved) should show "Automated (Standard)" as approval method


---

## Sheet 4: Impact_Assessment

**Purpose**: Document risk and impact analysis for each change. Required before change approval to ensure informed decision-making.

**Column Structure**:

| Column | Header | Data Type | Validation | Description |
|--------|--------|-----------|------------|-------------|
| A | Change ID | Text | Free text | Reference to Change_Request_Register |
| B | Change Title | Text | Free text | Brief title |
| C | Affected Systems Count | Number | Number | How many systems/assets impacted |
| D | Affected Systems Detail | Text | Free text | List of affected systems/assets |
| E | User Impact | Text | Dropdown | None, Minimal, Moderate, Significant, Severe |
| F | User Count Affected | Number | Number | Estimated number of users impacted |
| G | Service Downtime Required | Text | Dropdown | None, <1 hour, 1-4 hours, 4-8 hours, >8 hours |
| H | Risk Level | Text | Dropdown | Low, Medium, High, Critical |
| I | Risk Description | Text | Free text | What could go wrong |
| J | Mitigation Strategies | Text | Free text | How risks will be mitigated |
| K | Rollback Required | Text | Dropdown | Yes, No |
| L | Estimated Rollback Time | Text | Free text | Time to rollback if needed (e.g., "30 minutes") |
| M | Dependencies | Text | Free text | Other systems/changes this depends on |
| N | Business Justification | Text | Free text | Why this change is necessary |
| O | Risk Score | Number | Formula | Calculated risk score based on impact and likelihood |
| P | Assessment Completed By | Text | Free text | Name of person who performed assessment |
| Q | Assessment Date | Date | Date format | Date assessment was completed |

**Row Allocation**: 100 data rows (Row 3 to Row 102)

**Freeze Panes**: B3

**Data Validations**:

- Column E (User Impact): Dropdown list
  - Values: "None, Minimal, Moderate, Significant, Severe"
  - Allow blank: No

- Column G (Service Downtime Required): Dropdown list
  - Values: "None, <1 hour, 1-4 hours, 4-8 hours, >8 hours"
  - Allow blank: No

- Column H (Risk Level): Dropdown list
  - Values: "Low, Medium, High, Critical"
  - Allow blank: No

- Column K (Rollback Required): Dropdown list
  - Values: "Yes, No"
  - Allow blank: No


**Formulas**:

- Column O (Risk Score):

```
  =IF(H3="Low",1,IF(H3="Medium",2,IF(H3="High",3,IF(H3="Critical",4,0))))*
   IF(E3="None",1,IF(E3="Minimal",2,IF(E3="Moderate",3,IF(E3="Significant",4,IF(E3="Severe",5,0)))))
```

  - Explanation: Risk Score = Risk Level (1-4) × User Impact (1-5)
  - Range: 1 (lowest) to 20 (highest)


**Conditional Formatting**:

- Column H (Risk Level):
  - "Critical" → Dark red fill (C00000), white bold text
  - "High" → Red fill (FFC7CE)
  - "Medium" → Yellow fill (FFEB9C)
  - "Low" → Light green fill (E2EFDA)

- Column O (Risk Score):
  - ≥12 → Red fill (high risk)
  - 6-11 → Yellow fill (medium risk)
  - <6 → Green fill (low risk)

- Column K (Rollback Required):
  - "Yes" → Yellow fill (indicates rollback plan needed)
  - "No" → Gray fill


**Special Features**:

- Row 2: Column headers with light gray background
- Row 1: Title "Impact Assessment - Risk Analysis per Change" spanning A1:Q1
- Protected cells: Column O (formula cell) locked
- Risk-based approval: High/Critical risk changes should trigger Three-Tier approval


**Usage Notes**:

- Preparer: Complete impact assessment BEFORE submitting change for approval
- All Normal, Emergency, and Hot Fix changes require impact assessment
- Standard changes may have templated impact assessment (minimal)
- Risk Level (Column H) should match Priority in Change_Request_Register (P1/P2 = High/Critical risk)
- If Rollback Required = Yes, must complete Rollback_Capability sheet
- Assessment Completed By (Column P) provides accountability


---

## Sheet 5: Testing_Validation

**Purpose**: Evidence that changes were tested before production deployment. Records test environment, test results, identified issues, and go/no-go decision.

**Column Structure**:

| Column | Header | Data Type | Validation | Description |
|--------|--------|-----------|------------|-------------|
| A | Change ID | Text | Free text | Reference to Change_Request_Register |
| B | Change Title | Text | Free text | Brief title |
| C | Testing Required | Text | Dropdown | Yes, No, N/A (Emergency) |
| D | Test Environment | Text | Dropdown | Dev, Test, Staging, UAT, Production (Non-Critical), None |
| E | Test Start Date | Date | Date format | When testing began |
| F | Test End Date | Date | Date format | When testing completed |
| G | Test Duration (Days) | Number | Formula | Days between start and end |
| H | Test Plan Reference | Text | Free text | Link to test plan document |
| I | Test Cases Executed | Number | Number | Number of test cases run |
| J | Test Cases Passed | Number | Number | Number of test cases that passed |
| K | Test Cases Failed | Number | Number | Number of test cases that failed |
| L | Test Pass Rate % | Number | Formula | (Passed / Executed) × 100 |
| M | Critical Issues Found | Number | Number | Number of critical defects identified |
| N | Issues Resolved Before Deployment | Number | Number | Defects fixed before go-live |
| O | Testing Status | Text | Dropdown | Not Started, In Progress, Completed, Failed, Abbreviated (Emergency) |
| P | Go/No-Go Decision | Text | Dropdown | Go, No-Go, Go with Conditions, N/A |
| Q | Decision Maker | Text | Free text | Person who made go/no-go decision |
| R | Decision Date | Date | Date format | Date of go/no-go decision |
| S | Notes | Text | Free text | Test findings, conditions, issues |

**Row Allocation**: 100 data rows (Row 3 to Row 102)

**Freeze Panes**: B3

**Data Validations**:

- Column C (Testing Required): Dropdown list
  - Values: "Yes, No, N/A (Emergency)"
  - Allow blank: No

- Column D (Test Environment): Dropdown list
  - Values: "Dev, Test, Staging, UAT, Production (Non-Critical), None"
  - Allow blank: Yes

- Column O (Testing Status): Dropdown list
  - Values: "Not Started, In Progress, Completed, Failed, Abbreviated (Emergency)"
  - Allow blank: No

- Column P (Go/No-Go Decision): Dropdown list
  - Values: "Go, No-Go, Go with Conditions, N/A"
  - Allow blank: Yes


**Formulas**:

- Column G (Test Duration Days):

```
  =IF(OR(E3="",F3=""),"",F3-E3)
```

- Column L (Test Pass Rate %):

```
  =IF(I3=0,"",J3/I3*100)
```

  - Format as percentage with 1 decimal place


**Conditional Formatting**:

- Column L (Test Pass Rate %):
  - ≥95% → Green fill (C6EFCE)
  - 80-94% → Yellow fill (FFEB9C)
  - <80% → Red fill (FFC7CE)

- Column P (Go/No-Go Decision):
  - "Go" → Green fill, bold
  - "No-Go" → Red fill, bold
  - "Go with Conditions" → Yellow fill

- Column O (Testing Status):
  - "Completed" → Green fill
  - "Failed" → Red fill
  - "Abbreviated (Emergency)" → Orange fill (flag abbreviated testing)


**Special Features**:

- Row 2: Column headers with light gray background
- Row 1: Title "Testing Validation Records" spanning A1:S1
- Protected cells: Columns G and L (formula cells) locked
- Testing adequacy: Changes with Test Pass Rate <80% or Critical Issues >0 should be flagged for review


**Usage Notes**:

- Preparer: Document testing for each change
- Normal changes: Comprehensive testing required (Test Pass Rate target ≥95%)
- Standard changes: May use abbreviated testing if low risk
- Emergency changes: Abbreviated testing acceptable if documented
- Hot Fix changes: May proceed with minimal testing if critical (document in Notes)
- "Go with Conditions" requires documenting conditions in Notes column
- Test Plan Reference (Column H) should link to detailed test documentation


---

## Sheet 6: Implementation_Log

**Purpose**: Execution record for each change. Documents implementation date/time, implementer, actual steps performed, verification that change achieved intended result, and any deviations from plan.

**Column Structure**:

| Column | Header | Data Type | Validation | Description |
|--------|--------|-----------|------------|-------------|
| A | Change ID | Text | Free text | Reference to Change_Request_Register |
| B | Change Title | Text | Free text | Brief title |
| C | Scheduled Implementation Date/Time | DateTime | DateTime format | Planned implementation date and time |
| D | Actual Implementation Date/Time | DateTime | DateTime format | Actual start of implementation |
| E | Implementation Completed Date/Time | DateTime | DateTime format | When implementation finished |
| F | Implementation Duration (Hours) | Number | Formula | Hours between start and completion |
| G | Implementer Name | Text | Free text | Person who performed implementation |
| H | Implementation Method | Text | Dropdown | Manual, Automated Script, Semi-Automated, Assisted (Vendor) |
| I | Implementation Steps Performed | Text | Free text | Summary of steps executed |
| J | Deviations from Plan | Text | Free text | Any differences from planned procedure |
| K | Post-Implementation Verification | Text | Dropdown | Successful, Partial Success, Failed, Not Verified |
| L | Verification Method | Text | Free text | How success was verified (tests, monitoring, user confirmation) |
| M | Issues Encountered | Text | Free text | Problems during implementation |
| N | Issues Resolved | Text | Dropdown | Yes, No, Partially, N/A |
| O | Implementation Status | Text | Dropdown | Successful, Failed, Rolled Back, In Progress |
| P | Change Outcome | Text | Formula | Success, Partial Success, Failure, Rollback Required |
| Q | Rollback Triggered | Text | Dropdown | Yes, No |
| R | Rollback Completion Time | Text | Free text | If rolled back, time to complete rollback |
| S | Notes | Text | Free text | Additional context, lessons learned |

**Row Allocation**: 100 data rows (Row 3 to Row 102)

**Freeze Panes**: B3

**Data Validations**:

- Column H (Implementation Method): Dropdown list
  - Values: "Manual, Automated Script, Semi-Automated, Assisted (Vendor)"
  - Allow blank: No

- Column K (Post-Implementation Verification): Dropdown list
  - Values: "Successful, Partial Success, Failed, Not Verified"
  - Allow blank: No

- Column N (Issues Resolved): Dropdown list
  - Values: "Yes, No, Partially, N/A"
  - Allow blank: Yes

- Column O (Implementation Status): Dropdown list
  - Values: "Successful, Failed, Rolled Back, In Progress"
  - Allow blank: No

- Column Q (Rollback Triggered): Dropdown list
  - Values: "Yes, No"
  - Allow blank: No


**Formulas**:

- Column F (Implementation Duration Hours):

```
  =IF(OR(D3="",E3=""),"",ROUND((E3-D3)*24,2))
```

  - Explanation: Calculates hours between start and end (Excel date arithmetic, multiply by 24 for hours)

- Column P (Change Outcome):

```
  =IF(O3="Successful","Success",IF(O3="Failed","Failure",IF(O3="Rolled Back","Rollback Required",IF(K3="Partial Success","Partial Success","Unknown"))))
```

**Conditional Formatting**:

- Column O (Implementation Status):
  - "Successful" → Green fill (C6EFCE), bold
  - "Failed" → Red fill (FFC7CE), bold
  - "Rolled Back" → Orange fill
  - "In Progress" → Yellow fill (FFEB9C)

- Column K (Post-Implementation Verification):
  - "Successful" → Green fill
  - "Failed" → Red fill
  - "Partial Success" → Yellow fill
  - "Not Verified" → Light red fill (verification is required!)

- Column Q (Rollback Triggered):
  - "Yes" → Red fill (indicates change failed and was reversed)


**Special Features**:

- Row 2: Column headers with light gray background
- Row 1: Title "Implementation Log - Change Execution Records" spanning A1:S1
- Protected cells: Columns F and P (formula cells) locked
- DateTime fields: Use format DD.MM.YYYY HH:MM for precise tracking


**Usage Notes**:

- Preparer: Complete during/immediately after change implementation
- Record actual implementation time (not scheduled time) in Column D
- Document ANY deviations from plan (Column J) - critical for learning
- Post-Implementation Verification (Column K) must be "Successful" for change to be considered complete
- If Issues Encountered (Column M) is not empty, must document resolution in Column N
- Rollback timing (Column R) feeds into Rollback_Capability assessment


---

## Sheet 7: Rollback_Capability

**Purpose**: Verification that rollback procedures exist and have been tested. Documents rollback trigger criteria, rollback steps, estimated rollback time, and rollback testing results.

**Column Structure**:

| Column | Header | Data Type | Validation | Description |
|--------|--------|-----------|------------|-------------|
| A | Change ID | Text | Free text | Reference to Change_Request_Register |
| B | Change Title | Text | Free text | Brief title |
| C | Rollback Required | Text | Dropdown | Yes, No |
| D | Rollback Procedure Documented | Text | Dropdown | Yes, No, N/A |
| E | Rollback Document Location | Text | Free text | Link to rollback procedure document |
| F | Rollback Trigger Criteria | Text | Free text | Conditions that would trigger rollback |
| G | Estimated Rollback Time | Text | Free text | Expected time to complete rollback (e.g., "45 minutes") |
| H | Rollback Tested | Text | Dropdown | Yes, No, Partially, N/A |
| I | Rollback Test Date | Date | Date format | Date rollback procedure was tested |
| J | Rollback Test Results | Text | Dropdown | Successful, Failed, Partially Successful, Not Tested |
| K | Rollback Dependencies | Text | Free text | What must be in place to rollback (backups, snapshots, etc.) |
| L | Data Loss Risk on Rollback | Text | Dropdown | None, Minimal, Moderate, Significant |
| M | Data Backup Verified | Text | Dropdown | Yes, No, N/A |
| N | Rollback Approval Required | Text | Dropdown | Yes (same as forward), Yes (expedited), No (automatic) |
| O | Rollback Owner | Text | Free text | Person responsible for executing rollback if needed |
| P | Rollback Readiness | Text | Formula | Ready, Not Ready, Partially Ready, N/A |
| Q | Notes | Text | Free text | Special considerations, limitations |

**Row Allocation**: 100 data rows (Row 3 to Row 102)

**Freeze Panes**: B3

**Data Validations**:

- Column C (Rollback Required): Dropdown list
  - Values: "Yes, No"
  - Allow blank: No

- Column D (Rollback Procedure Documented): Dropdown list
  - Values: "Yes, No, N/A"
  - Allow blank: No

- Column H (Rollback Tested): Dropdown list
  - Values: "Yes, No, Partially, N/A"
  - Allow blank: No

- Column J (Rollback Test Results): Dropdown list
  - Values: "Successful, Failed, Partially Successful, Not Tested"
  - Allow blank: Yes

- Column L (Data Loss Risk on Rollback): Dropdown list
  - Values: "None, Minimal, Moderate, Significant"
  - Allow blank: Yes

- Column M (Data Backup Verified): Dropdown list
  - Values: "Yes, No, N/A"
  - Allow blank: No

- Column N (Rollback Approval Required): Dropdown list
  - Values: "Yes (same as forward), Yes (expedited), No (automatic)"
  - Allow blank: Yes


**Formulas**:

- Column P (Rollback Readiness):

```
  =IF(C3="No","N/A",IF(AND(D3="Yes",H3="Yes",J3="Successful",M3="Yes"),"Ready",IF(AND(D3="Yes",OR(H3="No",J3="Not Tested")),"Not Ready","Partially Ready")))
```

  - Explanation: 
    - N/A if rollback not required
    - Ready if documented + tested successfully + backup verified
    - Not Ready if documented but not tested
    - Partially Ready for other combinations


**Conditional Formatting**:

- Column P (Rollback Readiness):
  - "Ready" → Green fill (C6EFCE), bold
  - "Not Ready" → Red fill (FFC7CE), bold
  - "Partially Ready" → Yellow fill (FFEB9C)
  - "N/A" → Gray fill (D9D9D9)

- Column J (Rollback Test Results):
  - "Successful" → Green fill
  - "Failed" → Red fill
  - "Not Tested" → Red fill (testing is critical!)

- Column L (Data Loss Risk on Rollback):
  - "None" → Green fill
  - "Minimal" → Light green
  - "Moderate" → Yellow fill
  - "Significant" → Red fill (high risk!)


**Special Features**:

- Row 2: Column headers with light gray background
- Row 1: Title "Rollback Capability Assessment" spanning A1:Q1
- Protected cells: Column P (formula cell) locked
- Critical requirement: High-risk changes MUST have "Ready" rollback capability before approval


**Usage Notes**:

- Preparer: Complete before change approval (especially for high-risk changes)
- Rollback procedures should be tested in non-production environment where possible
- For changes where rollback is impossible or impractical (e.g., database schema changes), document mitigation in Notes
- Data Backup Verified (Column M) is mandatory for changes involving data
- If Rollback Readiness = "Not Ready" or "Partially Ready", should be resolved before production implementation
- Actual rollback events should be documented in Implementation_Log sheet


---

## Sheet 8: Emergency_Changes

**Purpose**: Special tracking for expedited changes. Ensures emergency process is not abused, post-facto documentation is completed, and CAB retrospective review occurs.

**Column Structure**:

| Column | Header | Data Type | Validation | Description |
|--------|--------|-----------|------------|-------------|
| A | Change ID | Text | Free text | Reference to Change_Request_Register (must be Emergency or Hot Fix type) |
| B | Change Title | Text | Free text | Brief title |
| C | Emergency Type | Text | Dropdown | Security Incident, Service Outage, Critical Bug, Vulnerability Remediation, Other |
| D | Business Impact if Not Implemented | Text | Free text | Consequence of delaying change |
| E | Emergency Declared By | Text | Free text | Person who authorized emergency process |
| F | Emergency Declaration Time | DateTime | DateTime format | When emergency was declared |
| G | Implementation Time | DateTime | DateTime format | When change was implemented |
| H | Time to Implement (Hours) | Number | Formula | Hours from declaration to implementation |
| I | Emergency Approval Method | Text | Dropdown | Verbal (CIO/CISO), Email (Expedited), CAB Chair Authorization |
| J | Emergency Approvers | Text | Free text | Names of approvers (minimum 2) |
| K | Post-Implementation Documentation Completed | Text | Dropdown | Yes, No, In Progress |
| L | CAB Retrospective Review Date | Date | Date format | Date emergency change was reviewed by full CAB |
| M | CAB Review Outcome | Text | Dropdown | Approved, Approved with Remediation, Disapproved (requires reversal), Not Yet Reviewed |
| N | Justification Valid | Text | Dropdown | Yes, No, Questionable |
| O | Process Abuse Indicator | Text | Formula | Legitimate, Questionable, Likely Abuse |
| P | Lessons Learned | Text | Free text | What can be improved for future emergencies |
| Q | Remediation Actions | Text | Free text | Actions required based on CAB review |
| R | Notes | Text | Free text | Additional context |

**Row Allocation**: 50 data rows (Row 3 to Row 52)

**Freeze Panes**: B3

**Data Validations**:

- Column C (Emergency Type): Dropdown list
  - Values: "Security Incident, Service Outage, Critical Bug, Vulnerability Remediation, Other"
  - Allow blank: No

- Column I (Emergency Approval Method): Dropdown list
  - Values: "Verbal (CIO/CISO), Email (Expedited), CAB Chair Authorization"
  - Allow blank: No

- Column K (Post-Implementation Documentation Completed): Dropdown list
  - Values: "Yes, No, In Progress"
  - Allow blank: No

- Column M (CAB Review Outcome): Dropdown list
  - Values: "Approved, Approved with Remediation, Disapproved (requires reversal), Not Yet Reviewed"
  - Allow blank: No

- Column N (Justification Valid): Dropdown list
  - Values: "Yes, No, Questionable"
  - Allow blank: Yes


**Formulas**:

- Column H (Time to Implement Hours):

```
  =IF(OR(F3="",G3=""),"",ROUND((G3-F3)*24,2))
```

- Column O (Process Abuse Indicator):

```
  =IF(AND(H3>48,N3="Questionable"),"Likely Abuse",IF(OR(H3>72,N3="No"),"Questionable","Legitimate"))
```

  - Explanation: Flags potential abuse if took >48 hours to implement (not truly emergency) or justification questionable


**Conditional Formatting**:

- Column M (CAB Review Outcome):
  - "Approved" → Green fill (C6EFCE)
  - "Disapproved (requires reversal)" → Red fill (FFC7CE), bold
  - "Not Yet Reviewed" → Yellow fill (FFEB9C)

- Column O (Process Abuse Indicator):
  - "Legitimate" → Green text
  - "Questionable" → Orange text, bold
  - "Likely Abuse" → Red text, bold

- Column K (Post-Implementation Documentation Completed):
  - "No" → Red fill (documentation is required!)
  - "In Progress" → Yellow fill
  - "Yes" → Green fill


**Special Features**:

- Row 2: Column headers with light gray background
- Row 1: Title "Emergency Changes - Expedited Process Tracking" spanning A1:R1
- Protected cells: Columns H and O (formula cells) locked
- Emergency ratio monitoring: Should be <10% of total changes


**Usage Notes**:

- Preparer: Document emergency change immediately after implementation
- Emergency process should only be used for true emergencies (service down, active security threat)
- Post-Implementation Documentation (Column K) must be completed within 24 hours
- CAB Retrospective Review (Column L) must occur within 5 business days
- If CAB Review Outcome = "Disapproved", change must be reversed unless exceptional circumstances
- Process Abuse Indicator helps identify when emergency process is misused for non-urgent changes
- Target: <10% of total changes should be Emergency/Hot Fix type


---

## Sheet 9: Change_Success_Metrics

**Purpose**: Auto-calculate change success rates, failure analysis, and trends. Formula-driven dashboard for change management effectiveness.

**Content Structure** (Not tabular - dashboard layout):

**Section A: Overall Change Metrics** (Rows 3-12)

| Metric | Formula/Value | Target | Status |
|--------|---------------|--------|--------|
| Total Changes (All Types) | =COUNTA(Change_Request_Register!A3:A102)-COUNTBLANK(Change_Request_Register!A3:A102) | N/A | [Calculated] |
| Completed Changes | =COUNTIF(Change_Request_Register!J3:J102,"Completed") | N/A | [Calculated] |
| Failed Changes | =COUNTIF(Change_Request_Register!J3:J102,"Failed") | <5% | [Status] |
| Rolled Back Changes | =COUNTIF(Change_Request_Register!J3:J102,"Rolled Back") | <3% | [Status] |
| Changes in Progress | =COUNTIF(Change_Request_Register!J3:J102,"Implementing")+COUNTIF(Change_Request_Register!J3:J102,"Scheduled") | N/A | [Count] |
| Overall Success Rate % | =(Completed / (Completed + Failed + Rolled Back)) × 100 | ≥95% | [Green/Yellow/Red] |

**Section B: Change Type Distribution** (Rows 14-20)

| Change Type | Count | Percentage | Target % |
|-------------|-------|------------|----------|
| Standard | =COUNTIF(Change_Request_Register!C3:C102,"Standard") | =Formula | 40-50% |
| Normal | =COUNTIF(Change_Request_Register!C3:C102,"Normal") | =Formula | 40-50% |
| Emergency | =COUNTIF(Change_Request_Register!C3:C102,"Emergency") | =Formula | <8% |
| Hot Fix | =COUNTIF(Change_Request_Register!C3:C102,"Hot Fix") | =Formula | <2% |

**Section C: Success Rate by Change Type** (Rows 22-28)

| Change Type | Total | Successful | Failed | Success Rate % |
|-------------|-------|------------|--------|----------------|
| Standard | =Formula | =Formula | =Formula | =Formula |
| Normal | =Formula | =Formula | =Formula | =Formula |
| Emergency | =Formula | =Formula | =Formula | =Formula |
| Hot Fix | =Formula | =Formula | =Formula | =Formula |

**Section D: Approval Process Metrics** (Rows 30-36)

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| Average Approval Time (Days) | =AVERAGE(Change_Approval_Workflow!P3:P102) | <7 days (Normal), <2 days (Emergency) | [Status] |
| Changes Rejected | =COUNTIF(Change_Approval_Workflow!O3:O102,"Rejected") | <10% | [Status] |
| Rejection Rate % | =(Rejected / Total Submitted) × 100 | <10% | [Status] |

**Section E: Testing Adequacy** (Rows 38-44)

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| Changes with Testing | =COUNTIF(Testing_Validation!C3:C102,"Yes") | 100% (Normal), >80% (Emergency) | [Status] |
| Average Test Pass Rate % | =AVERAGE(Testing_Validation!L3:L102) | ≥95% | [Status] |
| Changes with <80% Pass Rate | =COUNTIF(Testing_Validation!L3:L102,"<80") | 0 | [Status] |

**Section F: Emergency Change Analysis** (Rows 46-52)

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| Total Emergency Changes | =COUNTA(Emergency_Changes!A3:A52) | <10% of total | [Status] |
| Emergency Changes % | =(Emergency Total / All Changes) × 100 | <10% | [Status] |
| Emergency Changes Not Reviewed | =COUNTIF(Emergency_Changes!M3:M52,"Not Yet Reviewed") | 0 (after 5 days) | [Status] |
| Process Abuse Flagged | =COUNTIF(Emergency_Changes!O3:O52,"Likely Abuse") | 0 | [Status] |

**Formatting**:

- Section headers: Bold, 14pt, dark blue background (003366), white text
- Metric labels: Bold, 11pt
- Values: 12pt, conditionally formatted
- Target column: Gray background (D9D9D9)
- Status column: Conditional formatting (Green/Yellow/Red)


**Conditional Formatting**:

- Success Rate %:
  - ≥95% → Green
  - 90-94% → Yellow
  - <90% → Red

- Emergency Change %:
  - <8% → Green
  - 8-10% → Yellow
  - >10% → Red


**Special Features**:

- All cells protected (formula-driven sheet, no user input)
- Print area defined (fits on 2 pages)
- Chart area reserved (Rows 54-70) for trend graphs if needed


**Usage Notes**:

- This sheet updates automatically as other sheets are populated
- Review monthly to identify trends
- Rising failure rate or emergency change % indicates process issues
- Use for CAB reporting and management dashboards


---

## Sheet 10: Compliance_Dashboard

**Purpose**: Process adherence metrics showing compliance with change control procedures. Formula-driven assessment of whether required steps are being followed.

**Content Structure** (Dashboard layout):

**Section A: Approval Compliance** (Rows 3-10)

| Compliance Check | Compliant Count | Non-Compliant Count | Compliance % | Target |
|-----------------|-----------------|---------------------|--------------|--------|
| All Changes Have Approval Records | =Formula | =Formula | =Formula | 100% |
| Three-Tier Approval Followed (High Risk) | =Formula | =Formula | =Formula | 100% |
| Emergency Changes Have Post-Facto Review | =Formula | =Formula | =Formula | 100% |

**Section B: Testing Compliance** (Rows 12-18)

| Compliance Check | Compliant | Non-Compliant | Compliance % | Target |
|-----------------|-----------|----------------|--------------|--------|
| Normal Changes Have Testing | =Formula | =Formula | =Formula | 100% |
| Test Pass Rate ≥95% | =Formula | =Formula | =Formula | 95% |
| Go/No-Go Decision Documented | =Formula | =Formula | =Formula | 100% |

**Section C: Rollback Compliance** (Rows 20-26)

| Compliance Check | Compliant | Non-Compliant | Compliance % | Target |
|-----------------|-----------|----------------|--------------|--------|
| High-Risk Changes Have Rollback Plan | =Formula | =Formula | =Formula | 100% |
| Rollback Procedures Tested | =Formula | =Formula | =Formula | 100% |
| Data Backups Verified | =Formula | =Formula | =Formula | 100% |

**Section D: Documentation Compliance** (Rows 28-34)

| Compliance Check | Compliant | Non-Compliant | Compliance % | Target |
|-----------------|-----------|----------------|--------------|--------|
| All Changes Have Impact Assessment | =Formula | =Formula | =Formula | 100% |
| Implementation Documented | =Formula | =Formula | =Formula | 100% |
| Post-Implementation Verification | =Formula | =Formula | =Formula | 100% |

**Section E: Overall Compliance Summary** (Rows 36-42)

| Category | Compliance % | Status |
|----------|--------------|--------|
| Approval Process | =Average of Section A | [Status] |
| Testing Process | =Average of Section B | [Status] |
| Rollback Readiness | =Average of Section C | [Status] |
| Documentation | =Average of Section D | [Status] |
| **Overall Compliance** | **=Average of all categories** | **[Status]** |

**Conditional Formatting**:

- Compliance %:
  - 100% → Dark green
  - 95-99% → Green
  - 90-94% → Yellow
  - <90% → Red


**Special Features**:

- All cells protected (formula-driven)
- Traffic light indicators for visual status
- Print-friendly format for reporting


**Usage Notes**:

- Review quarterly to ensure process compliance
- Non-compliant items require remediation
- Target: ≥95% overall compliance
- Use for internal audit preparation


---

## Sheet 11: Evidence_Register

**Purpose**: Central register of supporting evidence for change control process.

**Column Structure**:

| Column | Header | Data Type | Validation | Description |
|--------|--------|-----------|------------|-------------|
| A | Evidence ID | Text | Free text | Unique identifier (e.g., "EVID-CHG-001") |
| B | Evidence Type | Text | Dropdown | Approval Record, Test Results, Implementation Log, Rollback Test, CAB Minutes, Email Approval, Change Request, Other |
| C | Evidence Description | Text | Free text | What this evidence shows |
| D | Related Change ID(s) | Text | Free text | Change IDs this evidence supports |
| E | Evidence Date | Date | Date format | Date evidence created |
| F | Evidence Location | Text | Free text | File path, URL, document reference |
| G | Evidence Owner | Text | Free text | Person responsible |
| H | Evidence Classification | Text | Dropdown | Public, Internal, Confidential, Restricted |
| I | Retention Period | Text | Dropdown | 1 Year, 3 Years, 5 Years, 7 Years, Indefinite |
| J | Last Verified Date | Date | Date format | Date evidence was verified accessible |
| K | Verification Status | Text | Dropdown | Verified, Needs Verification, Missing, Outdated |
| L | Linked Control Requirement | Text | Free text | POL section this supports (e.g., "POL-S2.2-2.2.3") |
| M | Notes | Text | Free text | Additional context |

**Row Allocation**: 100 data rows (Row 3 to Row 102)

**Freeze Panes**: B3

**Data Validations**:

- Column B: Dropdown with 8 evidence types
- Column H: Dropdown with 4 classification levels
- Column I: Dropdown with 5 retention periods
- Column K: Dropdown with 4 verification statuses


**Conditional Formatting**:

- Same as ISMS-IMP-A.8.9.1 Evidence Register


**Usage Notes**:

- Every change should have supporting evidence documented
- CAB meeting minutes are critical evidence
- Test results should be retained as evidence
- Approval records must be accessible for audit


---

## Sheet 12: Approval_Sign_Off

**Purpose**: Three-tier approval of change control assessment.

**Structure** (Signature block format):

**Section A: Document Information** (Rows 3-8)

- Assessment Title, Period, Document ID, Version, Assessment Date


**Section B: Preparer Sign-Off** (Rows 10-16)

- Preparer Name, Role, Signature, Date
- Attestation: "I attest that all configuration changes have been documented accurately and change control procedures have been followed."


**Section C: Reviewer Sign-Off** (Rows 18-25)

- Reviewer Name, Role, Signature, Date
- Review Findings, Gaps Identified
- Attestation: "I have reviewed this assessment and verified change control process compliance. Process improvement opportunities have been identified."


**Section D: Approver Sign-Off** (Rows 27-35)

- Approver Name, Role, Signature, Date
- Approval Decision (dropdown: Approved, Approved with Conditions, Not Approved)
- Conditions/Comments
- Next Assessment Due
- Attestation: "I approve this change control assessment and authorize remediation activities for identified gaps."


**Conditional Formatting**:

- Approval Decision: Green (Approved), Yellow (Conditions), Red (Not Approved)


---

# Data Validation Rules Summary

## Dropdown Lists

**Change_Request_Register**:

- Change Type: Standard, Normal, Emergency, Hot Fix
- Priority: P1-Critical, P2-High, P3-Medium, P4-Low
- Change Status: Draft, Submitted, Approved, In Testing, Scheduled, Implementing, Completed, Failed, Rolled Back, Cancelled


**Change_Approval_Workflow**:

- Approval Tier Required: Single-Tier, Two-Tier, Three-Tier, Emergency
- Approval Status (Tiers 1-3): Pending, Approved, Rejected, N/A
- Approval Method: CAB Meeting, Email Approval, Emergency Verbal, Automated (Standard), Not Applicable


**Impact_Assessment**:

- User Impact: None, Minimal, Moderate, Significant, Severe
- Service Downtime Required: None, <1 hour, 1-4 hours, 4-8 hours, >8 hours
- Risk Level: Low, Medium, High, Critical
- Rollback Required: Yes, No


**Testing_Validation**:

- Testing Required: Yes, No, N/A (Emergency)
- Test Environment: Dev, Test, Staging, UAT, Production (Non-Critical), None
- Testing Status: Not Started, In Progress, Completed, Failed, Abbreviated (Emergency)
- Go/No-Go Decision: Go, No-Go, Go with Conditions, N/A


**Implementation_Log**:

- Implementation Method: Manual, Automated Script, Semi-Automated, Assisted (Vendor)
- Post-Implementation Verification: Successful, Partial Success, Failed, Not Verified
- Issues Resolved: Yes, No, Partially, N/A
- Implementation Status: Successful, Failed, Rolled Back, In Progress
- Rollback Triggered: Yes, No


**Rollback_Capability**:

- Rollback Required: Yes, No
- Rollback Procedure Documented: Yes, No, N/A
- Rollback Tested: Yes, No, Partially, N/A
- Rollback Test Results: Successful, Failed, Partially Successful, Not Tested
- Data Loss Risk on Rollback: None, Minimal, Moderate, Significant
- Data Backup Verified: Yes, No, N/A
- Rollback Approval Required: Yes (same as forward), Yes (expedited), No (automatic)


**Emergency_Changes**:

- Emergency Type: Security Incident, Service Outage, Critical Bug, Vulnerability Remediation, Other
- Emergency Approval Method: Verbal (CIO/CISO), Email (Expedited), CAB Chair Authorization
- Post-Implementation Documentation Completed: Yes, No, In Progress
- CAB Review Outcome: Approved, Approved with Remediation, Disapproved (requires reversal), Not Yet Reviewed
- Justification Valid: Yes, No, Questionable


**Evidence_Register**:

- Evidence Type: Approval Record, Test Results, Implementation Log, Rollback Test, CAB Minutes, Email Approval, Change Request, Other
- Evidence Classification: Public, Internal, Confidential, Restricted
- Retention Period: 1 Year, 3 Years, 5 Years, 7 Years, Indefinite
- Verification Status: Verified, Needs Verification, Missing, Outdated


**Approval_Sign_Off**:

- Approval Decision: Approved, Approved with Conditions, Not Approved - Revisions Required


## Date Format

All date fields use **DD.MM.YYYY** format. DateTime fields use **DD.MM.YYYY HH:MM** format.

## Number Validations

- Test Cases Executed/Passed/Failed: Whole numbers, 0-9999
- Implementation Duration Hours: Decimal, calculated
- Risk Score: Calculated, 1-20 range


---

# Compliance Scoring Methodology

## Change Success Rate Calculation
```
Success Rate % = (Completed Changes / (Completed + Failed + Rolled Back)) × 100

Where:

- Completed = Changes with status "Completed" and verification "Successful"
- Failed = Changes with status "Failed"
- Rolled Back = Changes with status "Rolled Back"


Target: ≥95% overall success rate
```

## Emergency Change Ratio
```
Emergency Ratio % = ((Emergency + Hot Fix) / Total Changes) × 100

Target: <10%
Acceptable: <8%
Concern: 10-15%
Critical: >15% (indicates process problems or inadequate planning)
```

## Approval Compliance
```
Approval Compliance % = (Changes with Proper Approval / Total Changes) × 100

Proper Approval means:

- Approval tier matches risk level (High Risk = Three-Tier)
- All required approvers signed off
- Emergency changes have post-facto CAB review


Target: 100%
```

## Testing Coverage
```
Testing Coverage % = (Changes with Testing / Changes Requiring Testing) × 100

Changes Requiring Testing:

- All Normal changes: 100%
- Standard changes: May use templated testing
- Emergency changes: Abbreviated acceptable if documented


Target: 100% for Normal, 80% for Emergency
```

## Rollback Readiness
```
Rollback Readiness % = (High-Risk Changes with Ready Rollback / Total High-Risk Changes) × 100

Ready Rollback means:

- Rollback procedure documented
- Rollback tested successfully
- Data backup verified (if applicable)


Target: 100% for Critical/High risk changes
```

## Overall Change Control Compliance
```
Overall Compliance = 
  (Approval Compliance × 30%) +
  (Testing Coverage × 25%) +
  (Success Rate × 25%) +
  (Rollback Readiness × 20%)

Target: ≥95%

Status:

- Compliant: ≥95%
- Partially Compliant: 90-94%
- Non-Compliant: <90%

```

---

# Usage Instructions

## Step-by-Step Completion Guide

**Phase 1: Setup and Training** (Week 1)
1. Configuration Manager distributes workbook to Change Coordinator
2. Train change coordinators on workbook usage
3. Establish Change ID numbering convention (e.g., CHG-2026-NNN)
4. Set up integration with existing ticketing system if applicable

**Phase 2: Ongoing Change Tracking** (Continuous)
1. For each configuration change:

   - Create entry in Change_Request_Register (assign Change ID)
   - Complete Impact_Assessment before submission for approval
   - Document approval in Change_Approval_Workflow
   - Record testing in Testing_Validation
   - Document rollback plan in Rollback_Capability (if required)
   - Log implementation in Implementation_Log
   - Update Change_Request_Register status as change progresses

2. For emergency changes:

   - Follow expedited process
   - Create entry in Emergency_Changes immediately after implementation
   - Ensure CAB review within 5 business days


**Phase 3: Monthly Review** (Days 1-5 of each month)
1. Change Coordinator reviews previous month's changes
2. Verify all changes have complete documentation
3. Identify any incomplete records and follow up
4. Review Change_Success_Metrics for trends
5. Document gaps or issues in preparation for quarterly assessment

**Phase 4: Quarterly Assessment** (Last week of quarter)
1. Configuration Manager performs comprehensive review
2. Analyze Compliance_Dashboard metrics
3. Review emergency change ratio and justifications
4. Identify process improvement opportunities
5. Compile evidence in Evidence_Register
6. Complete Reviewer Sign-Off

**Phase 5: Annual Approval** (Quarterly or Semi-Annual)
1. IT Manager/CISO reviews assessment
2. Evaluate overall change management effectiveness
3. Approve remediation plans for identified gaps
4. Complete Approver Sign-Off

## Roles and Responsibilities

**Change Coordinator (Preparer)**:

- Document all changes in Change_Request_Register
- Complete Impact_Assessment for each change
- Track changes through approval and implementation
- Maintain Evidence_Register
- Monthly review of change records


**Configuration Manager (Reviewer)**:

- Quarterly comprehensive assessment
- Verify process compliance
- Analyze success metrics and trends
- Identify improvement opportunities
- Complete Reviewer Sign-Off


**IT Manager / CISO (Approver)**:

- Review overall change management effectiveness
- Approve assessment and remediation plans
- Complete Approver Sign-Off
- Authorize process improvements


**Change Advisory Board (CAB)**:

- Review and approve high-risk changes
- Retrospective review of emergency changes
- Provide governance oversight
- Approve process changes


## Common Questions

**Q: How do Standard changes (pre-approved) fit into this process?**
A: Standard changes still need tracking in Change_Request_Register, but approval workflow is simplified. Document "Automated (Standard)" as approval method. Testing may be templated. Focus on tracking execution and outcomes.

**Q: What if a change doesn't fit cleanly into Normal/Emergency/etc?**
A: Use risk-based judgment. If in doubt, classify as Normal (requires full process). It's better to over-document than under-document. CAB can adjust classification during review.

**Q: How do we handle changes that span multiple systems/teams?**
A: Create single Change ID for coordinated change. Document all affected systems in Impact_Assessment. Ensure all teams document their implementation in Implementation_Log with notes indicating coordination.

**Q: What constitutes "adequate" testing for approval?**
A: Depends on risk. Normal changes: Test pass rate ≥95%. Emergency changes: Testing may be abbreviated but must be documented. Hot Fix: Minimal testing acceptable if critical and rollback plan exists.

**Q: How strictly should we enforce the 10% emergency change limit?**
A: This is a health indicator, not absolute rule. If emergency ratio >10%, investigate why:

- Are truly emergencies, or is planning inadequate?
- Is emergency process being abused for convenience?
- Are there systemic issues (infrastructure instability, poor monitoring)?

Use as trigger for process improvement, not punitive measure.

**Q: What if rollback is impossible (e.g., irreversible database migration)?**
A: Document in Rollback_Capability why rollback is not possible. Provide mitigation strategy (extensive testing, phased approach, manual data recovery procedure). Requires explicit approval acknowledgment of risk.

---

# Integration Points with Other Assessments

## Cross-Assessment Dependencies

| This Assessment | Integrates With | Integration Mechanism | Data Flow |
|----------------|----------------|----------------------|-----------|
| Change_Request_Register | ISMS-IMP-A.8.9.1 (Baseline) | Changes update baselines → version control | Changes → New baseline versions |
| Implementation_Log | ISMS-IMP-A.8.9.3 (Monitoring) | Changes trigger monitoring of new config state | Change completion → Monitoring baseline update |
| Testing_Validation | ISMS-IMP-A.8.9.4 (Hardening) | Testing includes security hardening validation | Test results → Hardening compliance evidence |
| Emergency_Changes | A.6.8 (Incident Management) | Incidents may trigger emergency changes | Incidents → Emergency changes → Post-incident review |

## Process Integration

**Change → Baseline Update Flow**:
1. Change completed (Implementation_Log: status = Successful)
2. If baseline affected, update Version_Control in ISMS-IMP-A.8.9.1
3. Record new baseline version with Change ID as reference
4. Update affected assets in Asset_Inventory with new baseline reference

**Change → Monitoring Integration**:
1. Change implementation updates expected configuration state
2. Monitoring system (ISMS-IMP-A.8.9.3) updated with new baseline
3. Configuration drift detection validates change was applied correctly
4. Monitoring alerts if configuration reverts unexpectedly

---

# Evidence Collection Guidelines

## Required Evidence Types

**Approval Evidence**:

- CAB meeting minutes (with attendance, decisions, voting records)
- Email approval chains (with timestamps, full headers)
- Emergency verbal approval documentation (who, when, what, confirmation method)


**Testing Evidence**:

- Test plans and test cases
- Test execution results (pass/fail per test case)
- Screenshots of test environments
- Test data summaries
- Go/No-Go decision records


**Implementation Evidence**:

- Before/after configuration snapshots
- Implementation checklists (completed)
- Verification screenshots showing change applied
- Monitoring dashboards showing successful change
- Backup verification records (pre-change backups)


**Rollback Evidence**:

- Rollback procedure documents
- Rollback test results (in non-production)
- Backup/snapshot verification
- Rollback trigger criteria documentation


**Emergency Change Evidence**:

- Emergency declaration notification
- Incident records triggering emergency change
- Post-facto CAB review minutes
- Justification documentation


## Evidence Quality Standards

**Good Evidence**:

- Timestamped with date/time visible
- Attributable (shows who made decision/performed action)
- Authentic (original or certified copy)
- Complete (full context, not excerpts)
- Retained per retention policy


**Poor Evidence**:

- Undated screenshots
- "Approvals" without verifiable record
- Verbal agreements not documented
- Partial records (missing context)
- Evidence on personal storage only


---

# Document Maintenance

## Update Frequency

- **Real-time**: Change_Request_Register updated as changes occur
- **Daily**: High-priority change status updates
- **Weekly**: Review pending approvals, testing in progress
- **Monthly**: Metrics review, gap identification
- **Quarterly**: Comprehensive assessment, formal review
- **Annual**: Process improvement review, metrics trends analysis


## Workbook Versioning

File naming: `ISMS_A_8_9_2_Change_Control_Assessment_YYYYMMDD.xlsx`

Retain versions:

- Monthly snapshots (for trend analysis)
- Quarterly assessments (formal records)
- All versions for minimum 3 years (audit trail)


---

# Specification Approval

**Document Owner**: Configuration Manager  
**Technical Review**: Change Advisory Board, ISMS Implementation Team  
**Approval**: CISO / IT Management  

**This specification defines the structure and content of the Change Control Assessment workbook. The Python script `generate_a89_2_change_control.py` will implement this specification to create the actual Excel workbook.**

---

**END OF SPECIFICATION - ISMS-IMP-A.8.9.2**

---

# PART II: TECHNICAL SPECIFICATION
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

**Note:** This section provides technical specifications for the assessment workbook generation and maintenance. Users completing the assessment should refer to Part I above.

---

# Workbook Structure Overview

**Generated Workbook Name**: `ISMS_A_8_9_2_Change_Control_Assessment_YYYYMMDD.xlsx`

**Total Sheets**: 12

| Sheet # | Sheet Name | Purpose | Row Count |
|---------|------------|---------|-----------|
| 1 | Instructions | Usage guidance, roles, workflow, legend | N/A |
| 2 | Change_Request_Register | All configuration changes tracking | 100 data rows |
| 3 | Change_Approval_Workflow | Approval chain tracking | 100 data rows |
| 4 | Impact_Assessment | Risk and impact analysis per change | 100 data rows |
| 5 | Testing_Validation | Pre-deployment testing records | 100 data rows |
| 6 | Implementation_Log | Deployment execution records | 100 data rows |
| 7 | Rollback_Capability | Rollback procedures and testing | 100 data rows |
| 8 | Emergency_Changes | Emergency change tracking | 50 data rows |
| 9 | Change_Success_Metrics | Auto-calculated success rates, trends | N/A (formulas) |
| 10 | Compliance_Dashboard | Process adherence metrics | N/A (formulas) |
| 11 | Evidence_Register | Supporting evidence and documentation | 100 data rows |
| 12 | Approval_Sign_Off | Three-tier approval signatures | N/A (3 rows) |

**Sheet Relationship Flow**:
```
Change_Request_Register → (change list) → Change_Approval_Workflow
                                                  ↓
Impact_Assessment → (risk analysis) → Testing_Validation
                                              ↓
Implementation_Log → (execution) → Rollback_Capability
                                              ↓
Emergency_Changes → (expedited tracking) → Change_Success_Metrics
                                                      ↓
Compliance_Dashboard → (process metrics) → Evidence_Register
                                                      ↓
Approval_Sign_Off
```

---

# Detailed Sheet Specifications

## Sheet 1: Instructions

**Purpose**: Provides comprehensive guidance on using the assessment workbook, defines change types and priorities, explains approval workflows, and includes a legend for status values.

**Content Structure** (not row-based):

- Assessment overview and objectives
- Change types and priorities definitions
- Approval tier requirements by risk level
- Step-by-step completion instructions
- Three-tier assessment workflow diagram
- Status value definitions and color legend
- Integration with other assessments (baseline, monitoring)
- Common questions and troubleshooting
- Contact information for Change Advisory Board


**Formatting**:

- Title section: Bold, 16pt, dark blue background (003366)
- Section headers: Bold, 14pt, light blue background (4472C4)
- Body text: Regular, 11pt Calibri
- Color legend showing: Green (Approved/Successful), Yellow (Pending/In Progress), Red (Rejected/Failed), Gray (Cancelled/N/A)


**No Data Entry**: This is a read-only informational sheet.

---

## Sheet 2: Change_Request_Register

**Purpose**: Primary register of all configuration changes. Each change receives unique ID and is tracked through complete lifecycle from request to post-implementation review.

**Column Structure**:

| Column | Header | Data Type | Validation | Description |
|--------|--------|-----------|------------|-------------|
| A | Change ID | Text | Free text | Unique identifier (e.g., "CHG-2026-001") |
| B | Change Title | Text | Free text | Brief descriptive title of change |
| C | Change Type | Text | Dropdown | Standard, Normal, Emergency, Hot Fix |
| D | Priority | Text | Dropdown | P1-Critical, P2-High, P3-Medium, P4-Low |
| E | Affected Systems/Assets | Text | Free text | Systems impacted by change (comma-separated) |
| F | Requestor Name | Text | Free text | Person requesting the change |
| G | Requestor Contact | Text | Free text | Email or phone |
| H | Request Date | Date | Date format | Date change was requested |
| I | Required Implementation Date | Date | Date format | Target date for implementation |
| J | Change Status | Text | Dropdown | Draft, Submitted, Approved, In Testing, Scheduled, Implementing, Completed, Failed, Rolled Back, Cancelled |
| K | Current Phase | Text | Formula | Auto-calculated based on Change Status |
| L | Days in Current Phase | Number | Formula | Days since last status change |
| M | Overall Status Indicator | Text | Formula | On Track, At Risk, Delayed, Complete |
| N | Notes | Text | Free text | Additional context or updates |

**Row Allocation**: 100 data rows (Row 3 to Row 102)

**Freeze Panes**: B3 (Column headers and Change ID always visible)

**Data Validations**:

- Column C (Change Type): Dropdown list
  - Values: "Standard, Normal, Emergency, Hot Fix"
  - Allow blank: No (required field)
  - Error alert: "Please select a valid change type"

- Column D (Priority): Dropdown list
  - Values: "P1-Critical, P2-High, P3-Medium, P4-Low"
  - Allow blank: No (required field)
  - Error alert: "Please select priority level"

- Column J (Change Status): Dropdown list
  - Values: "Draft, Submitted, Approved, In Testing, Scheduled, Implementing, Completed, Failed, Rolled Back, Cancelled"
  - Allow blank: No (required field)
  - Error alert: "Please select change status"

- Column H (Request Date), Column I (Required Implementation Date): Date format DD.MM.YYYY


**Formulas**:

- Column K (Current Phase): 

```
  =IF(J3="Draft","Planning",IF(J3="Submitted","Approval",IF(J3="Approved","Testing",IF(J3="In Testing","Testing",IF(J3="Scheduled","Pre-Implementation",IF(J3="Implementing","Implementation",IF(OR(J3="Completed",J3="Failed",J3="Rolled Back",J3="Cancelled"),"Closed","Unknown")))))))
```

  - Explanation: Maps status to lifecycle phase

- Column L (Days in Current Phase): 

```
  =IF(H3="","",TODAY()-H3)
```

  - Explanation: Days since request (simplified - in practice would track status change dates)
  - Note: Real implementation might add hidden column for "Last Status Change Date"

- Column M (Overall Status Indicator):

```
  =IF(OR(J3="Completed",J3="Cancelled"),"Complete",IF(L3>30,"Delayed",IF(L3>14,"At Risk","On Track")))
```

  - Explanation: Status health indicator based on time in phase


**Conditional Formatting**:

- Column C (Change Type):
  - "Emergency" → Orange text (highlights emergency changes)
  - "Hot Fix" → Red text, bold (highlights urgent changes)

- Column D (Priority):
  - "P1-Critical" → Red fill (FFC7CE), bold
  - "P2-High" → Yellow fill (FFEB9C)

- Column J (Change Status):
  - "Completed" → Green fill (C6EFCE)
  - "Failed" → Red fill (FFC7CE)
  - "Rolled Back" → Orange fill
  - "Approved", "Scheduled" → Light green fill (E2EFDA)
  - "Draft", "Submitted" → Light yellow fill (FFFFCC)

- Column M (Overall Status Indicator):
  - "Complete" → Green text, bold
  - "On Track" → Black text
  - "At Risk" → Orange text, bold
  - "Delayed" → Red text, bold


**Special Features**:

- Row 2: Column headers with light gray background (D9D9D9), bold text, centered alignment
- Row 1: Title "Change Request Register - Configuration Change Tracking" spanning A1:N1, merged, dark blue background
- Protected cells: Columns K, L, M (formula cells) locked
- Filter: Enable auto-filter on header row to filter by Change Type, Priority, Status


**Usage Notes**:

- Preparer: Create new row for each configuration change request
- Change ID should follow organizational convention (e.g., CHG-YYYY-NNN)
- Update Change Status as change progresses through lifecycle
- Reference this Change ID in all other sheets for traceability


---

## Sheet 3: Change_Approval_Workflow

**Purpose**: Track approval chain for each change. Documents who approved at each tier, approval timestamps, and approval method. Critical for audit trail and compliance verification.

**Column Structure**:

| Column | Header | Data Type | Validation | Description |
|--------|--------|-----------|------------|-------------|
| A | Change ID | Text | Free text | Reference to Change_Request_Register |
| B | Change Title | Text | Free text | Brief title for reference |
| C | Approval Tier Required | Text | Dropdown | Single-Tier, Two-Tier, Three-Tier, Emergency |
| D | Tier 1 Approver Name | Text | Free text | First approver (Technical Lead) |
| E | Tier 1 Approval Status | Text | Dropdown | Pending, Approved, Rejected, N/A |
| F | Tier 1 Approval Date | Date | Date format | Date Tier 1 approved |
| G | Tier 2 Approver Name | Text | Free text | Second approver (Service Owner) |
| H | Tier 2 Approval Status | Text | Dropdown | Pending, Approved, Rejected, N/A |
| I | Tier 2 Approval Date | Date | Date format | Date Tier 2 approved |
| J | Tier 3 Approver Name | Text | Free text | Third approver (CAB Chair/CIO/CISO) |
| K | Tier 3 Approval Status | Text | Dropdown | Pending, Approved, Rejected, N/A |
| L | Tier 3 Approval Date | Date | Date format | Date Tier 3 approved |
| M | Approval Method | Text | Dropdown | CAB Meeting, Email Approval, Emergency Verbal, Automated (Standard) |
| N | Approval Reference | Text | Free text | Meeting minutes, email thread, ticket number |
| O | Overall Approval Status | Text | Formula | Approved, Partially Approved, Rejected, Pending |
| P | Days to Full Approval | Number | Formula | Days from request to final approval |
| Q | Notes | Text | Free text | Approval conditions, reasons for rejection |

**Row Allocation**: 100 data rows (Row 3 to Row 102)

**Freeze Panes**: B3

**Data Validations**:

- Column C (Approval Tier Required): Dropdown list
  - Values: "Single-Tier, Two-Tier, Three-Tier, Emergency"
  - Allow blank: No

- Column E, H, K (Approval Status): Dropdown list
  - Values: "Pending, Approved, Rejected, N/A"
  - Allow blank: Yes
  - N/A = This tier not required for this change

- Column M (Approval Method): Dropdown list
  - Values: "CAB Meeting, Email Approval, Emergency Verbal, Automated (Standard), Not Applicable"
  - Allow blank: Yes

- Date columns (F, I, L): Date format DD.MM.YYYY


**Formulas**:

- Column O (Overall Approval Status):

```
  =IF(C3="Single-Tier",IF(E3="Approved","Approved",IF(E3="Rejected","Rejected","Pending")),
     IF(C3="Two-Tier",IF(AND(E3="Approved",H3="Approved"),"Approved",IF(OR(E3="Rejected",H3="Rejected"),"Rejected",IF(AND(E3="Approved",H3="Pending"),"Partially Approved","Pending"))),
     IF(C3="Three-Tier",IF(AND(E3="Approved",H3="Approved",K3="Approved"),"Approved",IF(OR(E3="Rejected",H3="Rejected",K3="Rejected"),"Rejected",IF(AND(E3="Approved",H3="Approved",K3="Pending"),"Partially Approved","Pending"))),
     "Unknown")))
```

  - Explanation: Complex logic to determine overall status based on required tiers and individual approvals

- Column P (Days to Full Approval):

```
  =IF(O3="Approved",IF(C3="Single-Tier",F3-VLOOKUP(A3,Change_Request_Register!$A$3:$H$102,8,FALSE),
     IF(C3="Two-Tier",I3-VLOOKUP(A3,Change_Request_Register!$A$3:$H$102,8,FALSE),
     L3-VLOOKUP(A3,Change_Request_Register!$A$3:$H$102,8,FALSE))),"")
```

  - Explanation: Calculates days from request date to final approval date
  - Note: VLOOKUP fetches request date from Change_Request_Register


**Conditional Formatting**:

- Columns E, H, K (Approval Status):
  - "Approved" → Green fill (C6EFCE)
  - "Rejected" → Red fill (FFC7CE)
  - "Pending" → Yellow fill (FFEB9C)
  - "N/A" → Gray fill (D9D9D9)

- Column O (Overall Approval Status):
  - "Approved" → Green fill, bold text
  - "Rejected" → Red fill, bold text
  - "Partially Approved" → Yellow fill
  - "Pending" → Light yellow fill

- Column P (Days to Full Approval):
  - >14 days → Red fill (approval took too long)
  - 8-14 days → Yellow fill (approaching SLA)
  - <8 days → Green fill (fast approval)


**Special Features**:

- Row 2: Column headers with light gray background
- Row 1: Title "Change Approval Workflow Tracking" spanning A1:Q1
- Protected cells: Columns O and P (formula cells) locked
- Approval tier logic: If Tier 2 or Tier 3 not required (N/A), they don't block overall approval


**Usage Notes**:

- Preparer: Create entry when change is submitted for approval
- Update each tier's approval status as approvals are granted
- For Emergency changes, document verbal approval immediately and get written confirmation within 24 hours
- Approval Reference (Column N) is critical for audit - must link to verifiable record
- Standard changes (pre-approved) should show "Automated (Standard)" as approval method


---

## Sheet 4: Impact_Assessment

**Purpose**: Document risk and impact analysis for each change. Required before change approval to ensure informed decision-making.

**Column Structure**:

| Column | Header | Data Type | Validation | Description |
|--------|--------|-----------|------------|-------------|
| A | Change ID | Text | Free text | Reference to Change_Request_Register |
| B | Change Title | Text | Free text | Brief title |
| C | Affected Systems Count | Number | Number | How many systems/assets impacted |
| D | Affected Systems Detail | Text | Free text | List of affected systems/assets |
| E | User Impact | Text | Dropdown | None, Minimal, Moderate, Significant, Severe |
| F | User Count Affected | Number | Number | Estimated number of users impacted |
| G | Service Downtime Required | Text | Dropdown | None, <1 hour, 1-4 hours, 4-8 hours, >8 hours |
| H | Risk Level | Text | Dropdown | Low, Medium, High, Critical |
| I | Risk Description | Text | Free text | What could go wrong |
| J | Mitigation Strategies | Text | Free text | How risks will be mitigated |
| K | Rollback Required | Text | Dropdown | Yes, No |
| L | Estimated Rollback Time | Text | Free text | Time to rollback if needed (e.g., "30 minutes") |
| M | Dependencies | Text | Free text | Other systems/changes this depends on |
| N | Business Justification | Text | Free text | Why this change is necessary |
| O | Risk Score | Number | Formula | Calculated risk score based on impact and likelihood |
| P | Assessment Completed By | Text | Free text | Name of person who performed assessment |
| Q | Assessment Date | Date | Date format | Date assessment was completed |

**Row Allocation**: 100 data rows (Row 3 to Row 102)

**Freeze Panes**: B3

**Data Validations**:

- Column E (User Impact): Dropdown list
  - Values: "None, Minimal, Moderate, Significant, Severe"
  - Allow blank: No

- Column G (Service Downtime Required): Dropdown list
  - Values: "None, <1 hour, 1-4 hours, 4-8 hours, >8 hours"
  - Allow blank: No

- Column H (Risk Level): Dropdown list
  - Values: "Low, Medium, High, Critical"
  - Allow blank: No

- Column K (Rollback Required): Dropdown list
  - Values: "Yes, No"
  - Allow blank: No


**Formulas**:

- Column O (Risk Score):

```
  =IF(H3="Low",1,IF(H3="Medium",2,IF(H3="High",3,IF(H3="Critical",4,0))))*
   IF(E3="None",1,IF(E3="Minimal",2,IF(E3="Moderate",3,IF(E3="Significant",4,IF(E3="Severe",5,0)))))
```

  - Explanation: Risk Score = Risk Level (1-4) × User Impact (1-5)
  - Range: 1 (lowest) to 20 (highest)


**Conditional Formatting**:

- Column H (Risk Level):
  - "Critical" → Dark red fill (C00000), white bold text
  - "High" → Red fill (FFC7CE)
  - "Medium" → Yellow fill (FFEB9C)
  - "Low" → Light green fill (E2EFDA)

- Column O (Risk Score):
  - ≥12 → Red fill (high risk)
  - 6-11 → Yellow fill (medium risk)
  - <6 → Green fill (low risk)

- Column K (Rollback Required):
  - "Yes" → Yellow fill (indicates rollback plan needed)
  - "No" → Gray fill


**Special Features**:

- Row 2: Column headers with light gray background
- Row 1: Title "Impact Assessment - Risk Analysis per Change" spanning A1:Q1
- Protected cells: Column O (formula cell) locked
- Risk-based approval: High/Critical risk changes should trigger Three-Tier approval


**Usage Notes**:

- Preparer: Complete impact assessment BEFORE submitting change for approval
- All Normal, Emergency, and Hot Fix changes require impact assessment
- Standard changes may have templated impact assessment (minimal)
- Risk Level (Column H) should match Priority in Change_Request_Register (P1/P2 = High/Critical risk)
- If Rollback Required = Yes, must complete Rollback_Capability sheet
- Assessment Completed By (Column P) provides accountability


---

## Sheet 5: Testing_Validation

**Purpose**: Evidence that changes were tested before production deployment. Records test environment, test results, identified issues, and go/no-go decision.

**Column Structure**:

| Column | Header | Data Type | Validation | Description |
|--------|--------|-----------|------------|-------------|
| A | Change ID | Text | Free text | Reference to Change_Request_Register |
| B | Change Title | Text | Free text | Brief title |
| C | Testing Required | Text | Dropdown | Yes, No, N/A (Emergency) |
| D | Test Environment | Text | Dropdown | Dev, Test, Staging, UAT, Production (Non-Critical), None |
| E | Test Start Date | Date | Date format | When testing began |
| F | Test End Date | Date | Date format | When testing completed |
| G | Test Duration (Days) | Number | Formula | Days between start and end |
| H | Test Plan Reference | Text | Free text | Link to test plan document |
| I | Test Cases Executed | Number | Number | Number of test cases run |
| J | Test Cases Passed | Number | Number | Number of test cases that passed |
| K | Test Cases Failed | Number | Number | Number of test cases that failed |
| L | Test Pass Rate % | Number | Formula | (Passed / Executed) × 100 |
| M | Critical Issues Found | Number | Number | Number of critical defects identified |
| N | Issues Resolved Before Deployment | Number | Number | Defects fixed before go-live |
| O | Testing Status | Text | Dropdown | Not Started, In Progress, Completed, Failed, Abbreviated (Emergency) |
| P | Go/No-Go Decision | Text | Dropdown | Go, No-Go, Go with Conditions, N/A |
| Q | Decision Maker | Text | Free text | Person who made go/no-go decision |
| R | Decision Date | Date | Date format | Date of go/no-go decision |
| S | Notes | Text | Free text | Test findings, conditions, issues |

**Row Allocation**: 100 data rows (Row 3 to Row 102)

**Freeze Panes**: B3

**Data Validations**:

- Column C (Testing Required): Dropdown list
  - Values: "Yes, No, N/A (Emergency)"
  - Allow blank: No

- Column D (Test Environment): Dropdown list
  - Values: "Dev, Test, Staging, UAT, Production (Non-Critical), None"
  - Allow blank: Yes

- Column O (Testing Status): Dropdown list
  - Values: "Not Started, In Progress, Completed, Failed, Abbreviated (Emergency)"
  - Allow blank: No

- Column P (Go/No-Go Decision): Dropdown list
  - Values: "Go, No-Go, Go with Conditions, N/A"
  - Allow blank: Yes


**Formulas**:

- Column G (Test Duration Days):

```
  =IF(OR(E3="",F3=""),"",F3-E3)
```

- Column L (Test Pass Rate %):

```
  =IF(I3=0,"",J3/I3*100)
```

  - Format as percentage with 1 decimal place


**Conditional Formatting**:

- Column L (Test Pass Rate %):
  - ≥95% → Green fill (C6EFCE)
  - 80-94% → Yellow fill (FFEB9C)
  - <80% → Red fill (FFC7CE)

- Column P (Go/No-Go Decision):
  - "Go" → Green fill, bold
  - "No-Go" → Red fill, bold
  - "Go with Conditions" → Yellow fill

- Column O (Testing Status):
  - "Completed" → Green fill
  - "Failed" → Red fill
  - "Abbreviated (Emergency)" → Orange fill (flag abbreviated testing)


**Special Features**:

- Row 2: Column headers with light gray background
- Row 1: Title "Testing Validation Records" spanning A1:S1
- Protected cells: Columns G and L (formula cells) locked
- Testing adequacy: Changes with Test Pass Rate <80% or Critical Issues >0 should be flagged for review


**Usage Notes**:

- Preparer: Document testing for each change
- Normal changes: Comprehensive testing required (Test Pass Rate target ≥95%)
- Standard changes: May use abbreviated testing if low risk
- Emergency changes: Abbreviated testing acceptable if documented
- Hot Fix changes: May proceed with minimal testing if critical (document in Notes)
- "Go with Conditions" requires documenting conditions in Notes column
- Test Plan Reference (Column H) should link to detailed test documentation


---

## Sheet 6: Implementation_Log

**Purpose**: Execution record for each change. Documents implementation date/time, implementer, actual steps performed, verification that change achieved intended result, and any deviations from plan.

**Column Structure**:

| Column | Header | Data Type | Validation | Description |
|--------|--------|-----------|------------|-------------|
| A | Change ID | Text | Free text | Reference to Change_Request_Register |
| B | Change Title | Text | Free text | Brief title |
| C | Scheduled Implementation Date/Time | DateTime | DateTime format | Planned implementation date and time |
| D | Actual Implementation Date/Time | DateTime | DateTime format | Actual start of implementation |
| E | Implementation Completed Date/Time | DateTime | DateTime format | When implementation finished |
| F | Implementation Duration (Hours) | Number | Formula | Hours between start and completion |
| G | Implementer Name | Text | Free text | Person who performed implementation |
| H | Implementation Method | Text | Dropdown | Manual, Automated Script, Semi-Automated, Assisted (Vendor) |
| I | Implementation Steps Performed | Text | Free text | Summary of steps executed |
| J | Deviations from Plan | Text | Free text | Any differences from planned procedure |
| K | Post-Implementation Verification | Text | Dropdown | Successful, Partial Success, Failed, Not Verified |
| L | Verification Method | Text | Free text | How success was verified (tests, monitoring, user confirmation) |
| M | Issues Encountered | Text | Free text | Problems during implementation |
| N | Issues Resolved | Text | Dropdown | Yes, No, Partially, N/A |
| O | Implementation Status | Text | Dropdown | Successful, Failed, Rolled Back, In Progress |
| P | Change Outcome | Text | Formula | Success, Partial Success, Failure, Rollback Required |
| Q | Rollback Triggered | Text | Dropdown | Yes, No |
| R | Rollback Completion Time | Text | Free text | If rolled back, time to complete rollback |
| S | Notes | Text | Free text | Additional context, lessons learned |

**Row Allocation**: 100 data rows (Row 3 to Row 102)

**Freeze Panes**: B3

**Data Validations**:

- Column H (Implementation Method): Dropdown list
  - Values: "Manual, Automated Script, Semi-Automated, Assisted (Vendor)"
  - Allow blank: No

- Column K (Post-Implementation Verification): Dropdown list
  - Values: "Successful, Partial Success, Failed, Not Verified"
  - Allow blank: No

- Column N (Issues Resolved): Dropdown list
  - Values: "Yes, No, Partially, N/A"
  - Allow blank: Yes

- Column O (Implementation Status): Dropdown list
  - Values: "Successful, Failed, Rolled Back, In Progress"
  - Allow blank: No

- Column Q (Rollback Triggered): Dropdown list
  - Values: "Yes, No"
  - Allow blank: No


**Formulas**:

- Column F (Implementation Duration Hours):

```
  =IF(OR(D3="",E3=""),"",ROUND((E3-D3)*24,2))
```

  - Explanation: Calculates hours between start and end (Excel date arithmetic, multiply by 24 for hours)

- Column P (Change Outcome):

```
  =IF(O3="Successful","Success",IF(O3="Failed","Failure",IF(O3="Rolled Back","Rollback Required",IF(K3="Partial Success","Partial Success","Unknown"))))
```

**Conditional Formatting**:

- Column O (Implementation Status):
  - "Successful" → Green fill (C6EFCE), bold
  - "Failed" → Red fill (FFC7CE), bold
  - "Rolled Back" → Orange fill
  - "In Progress" → Yellow fill (FFEB9C)

- Column K (Post-Implementation Verification):
  - "Successful" → Green fill
  - "Failed" → Red fill
  - "Partial Success" → Yellow fill
  - "Not Verified" → Light red fill (verification is required!)

- Column Q (Rollback Triggered):
  - "Yes" → Red fill (indicates change failed and was reversed)


**Special Features**:

- Row 2: Column headers with light gray background
- Row 1: Title "Implementation Log - Change Execution Records" spanning A1:S1
- Protected cells: Columns F and P (formula cells) locked
- DateTime fields: Use format DD.MM.YYYY HH:MM for precise tracking


**Usage Notes**:

- Preparer: Complete during/immediately after change implementation
- Record actual implementation time (not scheduled time) in Column D
- Document ANY deviations from plan (Column J) - critical for learning
- Post-Implementation Verification (Column K) must be "Successful" for change to be considered complete
- If Issues Encountered (Column M) is not empty, must document resolution in Column N
- Rollback timing (Column R) feeds into Rollback_Capability assessment


---

## Sheet 7: Rollback_Capability

**Purpose**: Verification that rollback procedures exist and have been tested. Documents rollback trigger criteria, rollback steps, estimated rollback time, and rollback testing results.

**Column Structure**:

| Column | Header | Data Type | Validation | Description |
|--------|--------|-----------|------------|-------------|
| A | Change ID | Text | Free text | Reference to Change_Request_Register |
| B | Change Title | Text | Free text | Brief title |
| C | Rollback Required | Text | Dropdown | Yes, No |
| D | Rollback Procedure Documented | Text | Dropdown | Yes, No, N/A |
| E | Rollback Document Location | Text | Free text | Link to rollback procedure document |
| F | Rollback Trigger Criteria | Text | Free text | Conditions that would trigger rollback |
| G | Estimated Rollback Time | Text | Free text | Expected time to complete rollback (e.g., "45 minutes") |
| H | Rollback Tested | Text | Dropdown | Yes, No, Partially, N/A |
| I | Rollback Test Date | Date | Date format | Date rollback procedure was tested |
| J | Rollback Test Results | Text | Dropdown | Successful, Failed, Partially Successful, Not Tested |
| K | Rollback Dependencies | Text | Free text | What must be in place to rollback (backups, snapshots, etc.) |
| L | Data Loss Risk on Rollback | Text | Dropdown | None, Minimal, Moderate, Significant |
| M | Data Backup Verified | Text | Dropdown | Yes, No, N/A |
| N | Rollback Approval Required | Text | Dropdown | Yes (same as forward), Yes (expedited), No (automatic) |
| O | Rollback Owner | Text | Free text | Person responsible for executing rollback if needed |
| P | Rollback Readiness | Text | Formula | Ready, Not Ready, Partially Ready, N/A |
| Q | Notes | Text | Free text | Special considerations, limitations |

**Row Allocation**: 100 data rows (Row 3 to Row 102)

**Freeze Panes**: B3

**Data Validations**:

- Column C (Rollback Required): Dropdown list
  - Values: "Yes, No"
  - Allow blank: No

- Column D (Rollback Procedure Documented): Dropdown list
  - Values: "Yes, No, N/A"
  - Allow blank: No

- Column H (Rollback Tested): Dropdown list
  - Values: "Yes, No, Partially, N/A"
  - Allow blank: No

- Column J (Rollback Test Results): Dropdown list
  - Values: "Successful, Failed, Partially Successful, Not Tested"
  - Allow blank: Yes

- Column L (Data Loss Risk on Rollback): Dropdown list
  - Values: "None, Minimal, Moderate, Significant"
  - Allow blank: Yes

- Column M (Data Backup Verified): Dropdown list
  - Values: "Yes, No, N/A"
  - Allow blank: No

- Column N (Rollback Approval Required): Dropdown list
  - Values: "Yes (same as forward), Yes (expedited), No (automatic)"
  - Allow blank: Yes


**Formulas**:

- Column P (Rollback Readiness):

```
  =IF(C3="No","N/A",IF(AND(D3="Yes",H3="Yes",J3="Successful",M3="Yes"),"Ready",IF(AND(D3="Yes",OR(H3="No",J3="Not Tested")),"Not Ready","Partially Ready")))
```

  - Explanation: 
    - N/A if rollback not required
    - Ready if documented + tested successfully + backup verified
    - Not Ready if documented but not tested
    - Partially Ready for other combinations


**Conditional Formatting**:

- Column P (Rollback Readiness):
  - "Ready" → Green fill (C6EFCE), bold
  - "Not Ready" → Red fill (FFC7CE), bold
  - "Partially Ready" → Yellow fill (FFEB9C)
  - "N/A" → Gray fill (D9D9D9)

- Column J (Rollback Test Results):
  - "Successful" → Green fill
  - "Failed" → Red fill
  - "Not Tested" → Red fill (testing is critical!)

- Column L (Data Loss Risk on Rollback):
  - "None" → Green fill
  - "Minimal" → Light green
  - "Moderate" → Yellow fill
  - "Significant" → Red fill (high risk!)


**Special Features**:

- Row 2: Column headers with light gray background
- Row 1: Title "Rollback Capability Assessment" spanning A1:Q1
- Protected cells: Column P (formula cell) locked
- Critical requirement: High-risk changes MUST have "Ready" rollback capability before approval


**Usage Notes**:

- Preparer: Complete before change approval (especially for high-risk changes)
- Rollback procedures should be tested in non-production environment where possible
- For changes where rollback is impossible or impractical (e.g., database schema changes), document mitigation in Notes
- Data Backup Verified (Column M) is mandatory for changes involving data
- If Rollback Readiness = "Not Ready" or "Partially Ready", should be resolved before production implementation
- Actual rollback events should be documented in Implementation_Log sheet


---

## Sheet 8: Emergency_Changes

**Purpose**: Special tracking for expedited changes. Ensures emergency process is not abused, post-facto documentation is completed, and CAB retrospective review occurs.

**Column Structure**:

| Column | Header | Data Type | Validation | Description |
|--------|--------|-----------|------------|-------------|
| A | Change ID | Text | Free text | Reference to Change_Request_Register (must be Emergency or Hot Fix type) |
| B | Change Title | Text | Free text | Brief title |
| C | Emergency Type | Text | Dropdown | Security Incident, Service Outage, Critical Bug, Vulnerability Remediation, Other |
| D | Business Impact if Not Implemented | Text | Free text | Consequence of delaying change |
| E | Emergency Declared By | Text | Free text | Person who authorized emergency process |
| F | Emergency Declaration Time | DateTime | DateTime format | When emergency was declared |
| G | Implementation Time | DateTime | DateTime format | When change was implemented |
| H | Time to Implement (Hours) | Number | Formula | Hours from declaration to implementation |
| I | Emergency Approval Method | Text | Dropdown | Verbal (CIO/CISO), Email (Expedited), CAB Chair Authorization |
| J | Emergency Approvers | Text | Free text | Names of approvers (minimum 2) |
| K | Post-Implementation Documentation Completed | Text | Dropdown | Yes, No, In Progress |
| L | CAB Retrospective Review Date | Date | Date format | Date emergency change was reviewed by full CAB |
| M | CAB Review Outcome | Text | Dropdown | Approved, Approved with Remediation, Disapproved (requires reversal), Not Yet Reviewed |
| N | Justification Valid | Text | Dropdown | Yes, No, Questionable |
| O | Process Abuse Indicator | Text | Formula | Legitimate, Questionable, Likely Abuse |
| P | Lessons Learned | Text | Free text | What can be improved for future emergencies |
| Q | Remediation Actions | Text | Free text | Actions required based on CAB review |
| R | Notes | Text | Free text | Additional context |

**Row Allocation**: 50 data rows (Row 3 to Row 52)

**Freeze Panes**: B3

**Data Validations**:

- Column C (Emergency Type): Dropdown list
  - Values: "Security Incident, Service Outage, Critical Bug, Vulnerability Remediation, Other"
  - Allow blank: No

- Column I (Emergency Approval Method): Dropdown list
  - Values: "Verbal (CIO/CISO), Email (Expedited), CAB Chair Authorization"
  - Allow blank: No

- Column K (Post-Implementation Documentation Completed): Dropdown list
  - Values: "Yes, No, In Progress"
  - Allow blank: No

- Column M (CAB Review Outcome): Dropdown list
  - Values: "Approved, Approved with Remediation, Disapproved (requires reversal), Not Yet Reviewed"
  - Allow blank: No

- Column N (Justification Valid): Dropdown list
  - Values: "Yes, No, Questionable"
  - Allow blank: Yes


**Formulas**:

- Column H (Time to Implement Hours):

```
  =IF(OR(F3="",G3=""),"",ROUND((G3-F3)*24,2))
```

- Column O (Process Abuse Indicator):

```
  =IF(AND(H3>48,N3="Questionable"),"Likely Abuse",IF(OR(H3>72,N3="No"),"Questionable","Legitimate"))
```

  - Explanation: Flags potential abuse if took >48 hours to implement (not truly emergency) or justification questionable


**Conditional Formatting**:

- Column M (CAB Review Outcome):
  - "Approved" → Green fill (C6EFCE)
  - "Disapproved (requires reversal)" → Red fill (FFC7CE), bold
  - "Not Yet Reviewed" → Yellow fill (FFEB9C)

- Column O (Process Abuse Indicator):
  - "Legitimate" → Green text
  - "Questionable" → Orange text, bold
  - "Likely Abuse" → Red text, bold

- Column K (Post-Implementation Documentation Completed):
  - "No" → Red fill (documentation is required!)
  - "In Progress" → Yellow fill
  - "Yes" → Green fill


**Special Features**:

- Row 2: Column headers with light gray background
- Row 1: Title "Emergency Changes - Expedited Process Tracking" spanning A1:R1
- Protected cells: Columns H and O (formula cells) locked
- Emergency ratio monitoring: Should be <10% of total changes


**Usage Notes**:

- Preparer: Document emergency change immediately after implementation
- Emergency process should only be used for true emergencies (service down, active security threat)
- Post-Implementation Documentation (Column K) must be completed within 24 hours
- CAB Retrospective Review (Column L) must occur within 5 business days
- If CAB Review Outcome = "Disapproved", change must be reversed unless exceptional circumstances
- Process Abuse Indicator helps identify when emergency process is misused for non-urgent changes
- Target: <10% of total changes should be Emergency/Hot Fix type


---

## Sheet 9: Change_Success_Metrics

**Purpose**: Auto-calculate change success rates, failure analysis, and trends. Formula-driven dashboard for change management effectiveness.

**Content Structure** (Not tabular - dashboard layout):

**Section A: Overall Change Metrics** (Rows 3-12)

| Metric | Formula/Value | Target | Status |
|--------|---------------|--------|--------|
| Total Changes (All Types) | =COUNTA(Change_Request_Register!A3:A102)-COUNTBLANK(Change_Request_Register!A3:A102) | N/A | [Calculated] |
| Completed Changes | =COUNTIF(Change_Request_Register!J3:J102,"Completed") | N/A | [Calculated] |
| Failed Changes | =COUNTIF(Change_Request_Register!J3:J102,"Failed") | <5% | [Status] |
| Rolled Back Changes | =COUNTIF(Change_Request_Register!J3:J102,"Rolled Back") | <3% | [Status] |
| Changes in Progress | =COUNTIF(Change_Request_Register!J3:J102,"Implementing")+COUNTIF(Change_Request_Register!J3:J102,"Scheduled") | N/A | [Count] |
| Overall Success Rate % | =(Completed / (Completed + Failed + Rolled Back)) × 100 | ≥95% | [Green/Yellow/Red] |

**Section B: Change Type Distribution** (Rows 14-20)

| Change Type | Count | Percentage | Target % |
|-------------|-------|------------|----------|
| Standard | =COUNTIF(Change_Request_Register!C3:C102,"Standard") | =Formula | 40-50% |
| Normal | =COUNTIF(Change_Request_Register!C3:C102,"Normal") | =Formula | 40-50% |
| Emergency | =COUNTIF(Change_Request_Register!C3:C102,"Emergency") | =Formula | <8% |
| Hot Fix | =COUNTIF(Change_Request_Register!C3:C102,"Hot Fix") | =Formula | <2% |

**Section C: Success Rate by Change Type** (Rows 22-28)

| Change Type | Total | Successful | Failed | Success Rate % |
|-------------|-------|------------|--------|----------------|
| Standard | =Formula | =Formula | =Formula | =Formula |
| Normal | =Formula | =Formula | =Formula | =Formula |
| Emergency | =Formula | =Formula | =Formula | =Formula |
| Hot Fix | =Formula | =Formula | =Formula | =Formula |

**Section D: Approval Process Metrics** (Rows 30-36)

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| Average Approval Time (Days) | =AVERAGE(Change_Approval_Workflow!P3:P102) | <7 days (Normal), <2 days (Emergency) | [Status] |
| Changes Rejected | =COUNTIF(Change_Approval_Workflow!O3:O102,"Rejected") | <10% | [Status] |
| Rejection Rate % | =(Rejected / Total Submitted) × 100 | <10% | [Status] |

**Section E: Testing Adequacy** (Rows 38-44)

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| Changes with Testing | =COUNTIF(Testing_Validation!C3:C102,"Yes") | 100% (Normal), >80% (Emergency) | [Status] |
| Average Test Pass Rate % | =AVERAGE(Testing_Validation!L3:L102) | ≥95% | [Status] |
| Changes with <80% Pass Rate | =COUNTIF(Testing_Validation!L3:L102,"<80") | 0 | [Status] |

**Section F: Emergency Change Analysis** (Rows 46-52)

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| Total Emergency Changes | =COUNTA(Emergency_Changes!A3:A52) | <10% of total | [Status] |
| Emergency Changes % | =(Emergency Total / All Changes) × 100 | <10% | [Status] |
| Emergency Changes Not Reviewed | =COUNTIF(Emergency_Changes!M3:M52,"Not Yet Reviewed") | 0 (after 5 days) | [Status] |
| Process Abuse Flagged | =COUNTIF(Emergency_Changes!O3:O52,"Likely Abuse") | 0 | [Status] |

**Formatting**:

- Section headers: Bold, 14pt, dark blue background (003366), white text
- Metric labels: Bold, 11pt
- Values: 12pt, conditionally formatted
- Target column: Gray background (D9D9D9)
- Status column: Conditional formatting (Green/Yellow/Red)


**Conditional Formatting**:

- Success Rate %:
  - ≥95% → Green
  - 90-94% → Yellow
  - <90% → Red

- Emergency Change %:
  - <8% → Green
  - 8-10% → Yellow
  - >10% → Red


**Special Features**:

- All cells protected (formula-driven sheet, no user input)
- Print area defined (fits on 2 pages)
- Chart area reserved (Rows 54-70) for trend graphs if needed


**Usage Notes**:

- This sheet updates automatically as other sheets are populated
- Review monthly to identify trends
- Rising failure rate or emergency change % indicates process issues
- Use for CAB reporting and management dashboards


---

## Sheet 10: Compliance_Dashboard

**Purpose**: Process adherence metrics showing compliance with change control procedures. Formula-driven assessment of whether required steps are being followed.

**Content Structure** (Dashboard layout):

**Section A: Approval Compliance** (Rows 3-10)

| Compliance Check | Compliant Count | Non-Compliant Count | Compliance % | Target |
|-----------------|-----------------|---------------------|--------------|--------|
| All Changes Have Approval Records | =Formula | =Formula | =Formula | 100% |
| Three-Tier Approval Followed (High Risk) | =Formula | =Formula | =Formula | 100% |
| Emergency Changes Have Post-Facto Review | =Formula | =Formula | =Formula | 100% |

**Section B: Testing Compliance** (Rows 12-18)

| Compliance Check | Compliant | Non-Compliant | Compliance % | Target |
|-----------------|-----------|----------------|--------------|--------|
| Normal Changes Have Testing | =Formula | =Formula | =Formula | 100% |
| Test Pass Rate ≥95% | =Formula | =Formula | =Formula | 95% |
| Go/No-Go Decision Documented | =Formula | =Formula | =Formula | 100% |

**Section C: Rollback Compliance** (Rows 20-26)

| Compliance Check | Compliant | Non-Compliant | Compliance % | Target |
|-----------------|-----------|----------------|--------------|--------|
| High-Risk Changes Have Rollback Plan | =Formula | =Formula | =Formula | 100% |
| Rollback Procedures Tested | =Formula | =Formula | =Formula | 100% |
| Data Backups Verified | =Formula | =Formula | =Formula | 100% |

**Section D: Documentation Compliance** (Rows 28-34)

| Compliance Check | Compliant | Non-Compliant | Compliance % | Target |
|-----------------|-----------|----------------|--------------|--------|
| All Changes Have Impact Assessment | =Formula | =Formula | =Formula | 100% |
| Implementation Documented | =Formula | =Formula | =Formula | 100% |
| Post-Implementation Verification | =Formula | =Formula | =Formula | 100% |

**Section E: Overall Compliance Summary** (Rows 36-42)

| Category | Compliance % | Status |
|----------|--------------|--------|
| Approval Process | =Average of Section A | [Status] |
| Testing Process | =Average of Section B | [Status] |
| Rollback Readiness | =Average of Section C | [Status] |
| Documentation | =Average of Section D | [Status] |
| **Overall Compliance** | **=Average of all categories** | **[Status]** |

**Conditional Formatting**:

- Compliance %:
  - 100% → Dark green
  - 95-99% → Green
  - 90-94% → Yellow
  - <90% → Red


**Special Features**:

- All cells protected (formula-driven)
- Traffic light indicators for visual status
- Print-friendly format for reporting


**Usage Notes**:

- Review quarterly to ensure process compliance
- Non-compliant items require remediation
- Target: ≥95% overall compliance
- Use for internal audit preparation


---

## Sheet 11: Evidence_Register

**Purpose**: Central register of supporting evidence for change control process.

**Column Structure**:

| Column | Header | Data Type | Validation | Description |
|--------|--------|-----------|------------|-------------|
| A | Evidence ID | Text | Free text | Unique identifier (e.g., "EVID-CHG-001") |
| B | Evidence Type | Text | Dropdown | Approval Record, Test Results, Implementation Log, Rollback Test, CAB Minutes, Email Approval, Change Request, Other |
| C | Evidence Description | Text | Free text | What this evidence shows |
| D | Related Change ID(s) | Text | Free text | Change IDs this evidence supports |
| E | Evidence Date | Date | Date format | Date evidence created |
| F | Evidence Location | Text | Free text | File path, URL, document reference |
| G | Evidence Owner | Text | Free text | Person responsible |
| H | Evidence Classification | Text | Dropdown | Public, Internal, Confidential, Restricted |
| I | Retention Period | Text | Dropdown | 1 Year, 3 Years, 5 Years, 7 Years, Indefinite |
| J | Last Verified Date | Date | Date format | Date evidence was verified accessible |
| K | Verification Status | Text | Dropdown | Verified, Needs Verification, Missing, Outdated |
| L | Linked Control Requirement | Text | Free text | POL section this supports (e.g., "POL-S2.2-2.2.3") |
| M | Notes | Text | Free text | Additional context |

**Row Allocation**: 100 data rows (Row 3 to Row 102)

**Freeze Panes**: B3

**Data Validations**:

- Column B: Dropdown with 8 evidence types
- Column H: Dropdown with 4 classification levels
- Column I: Dropdown with 5 retention periods
- Column K: Dropdown with 4 verification statuses


**Conditional Formatting**:

- Same as ISMS-IMP-A.8.9.1 Evidence Register


**Usage Notes**:

- Every change should have supporting evidence documented
- CAB meeting minutes are critical evidence
- Test results should be retained as evidence
- Approval records must be accessible for audit


---

## Sheet 12: Approval_Sign_Off

**Purpose**: Three-tier approval of change control assessment.

**Structure** (Signature block format):

**Section A: Document Information** (Rows 3-8)

- Assessment Title, Period, Document ID, Version, Assessment Date


**Section B: Preparer Sign-Off** (Rows 10-16)

- Preparer Name, Role, Signature, Date
- Attestation: "I attest that all configuration changes have been documented accurately and change control procedures have been followed."


**Section C: Reviewer Sign-Off** (Rows 18-25)

- Reviewer Name, Role, Signature, Date
- Review Findings, Gaps Identified
- Attestation: "I have reviewed this assessment and verified change control process compliance. Process improvement opportunities have been identified."


**Section D: Approver Sign-Off** (Rows 27-35)

- Approver Name, Role, Signature, Date
- Approval Decision (dropdown: Approved, Approved with Conditions, Not Approved)
- Conditions/Comments
- Next Assessment Due
- Attestation: "I approve this change control assessment and authorize remediation activities for identified gaps."


**Conditional Formatting**:

- Approval Decision: Green (Approved), Yellow (Conditions), Red (Not Approved)


---

# Data Validation Rules Summary

## Dropdown Lists

**Change_Request_Register**:

- Change Type: Standard, Normal, Emergency, Hot Fix
- Priority: P1-Critical, P2-High, P3-Medium, P4-Low
- Change Status: Draft, Submitted, Approved, In Testing, Scheduled, Implementing, Completed, Failed, Rolled Back, Cancelled


**Change_Approval_Workflow**:

- Approval Tier Required: Single-Tier, Two-Tier, Three-Tier, Emergency
- Approval Status (Tiers 1-3): Pending, Approved, Rejected, N/A
- Approval Method: CAB Meeting, Email Approval, Emergency Verbal, Automated (Standard), Not Applicable


**Impact_Assessment**:

- User Impact: None, Minimal, Moderate, Significant, Severe
- Service Downtime Required: None, <1 hour, 1-4 hours, 4-8 hours, >8 hours
- Risk Level: Low, Medium, High, Critical
- Rollback Required: Yes, No


**Testing_Validation**:

- Testing Required: Yes, No, N/A (Emergency)
- Test Environment: Dev, Test, Staging, UAT, Production (Non-Critical), None
- Testing Status: Not Started, In Progress, Completed, Failed, Abbreviated (Emergency)
- Go/No-Go Decision: Go, No-Go, Go with Conditions, N/A


**Implementation_Log**:

- Implementation Method: Manual, Automated Script, Semi-Automated, Assisted (Vendor)
- Post-Implementation Verification: Successful, Partial Success, Failed, Not Verified
- Issues Resolved: Yes, No, Partially, N/A
- Implementation Status: Successful, Failed, Rolled Back, In Progress
- Rollback Triggered: Yes, No


**Rollback_Capability**:

- Rollback Required: Yes, No
- Rollback Procedure Documented: Yes, No, N/A
- Rollback Tested: Yes, No, Partially, N/A
- Rollback Test Results: Successful, Failed, Partially Successful, Not Tested
- Data Loss Risk on Rollback: None, Minimal, Moderate, Significant
- Data Backup Verified: Yes, No, N/A
- Rollback Approval Required: Yes (same as forward), Yes (expedited), No (automatic)


**Emergency_Changes**:

- Emergency Type: Security Incident, Service Outage, Critical Bug, Vulnerability Remediation, Other
- Emergency Approval Method: Verbal (CIO/CISO), Email (Expedited), CAB Chair Authorization
- Post-Implementation Documentation Completed: Yes, No, In Progress
- CAB Review Outcome: Approved, Approved with Remediation, Disapproved (requires reversal), Not Yet Reviewed
- Justification Valid: Yes, No, Questionable


**Evidence_Register**:

- Evidence Type: Approval Record, Test Results, Implementation Log, Rollback Test, CAB Minutes, Email Approval, Change Request, Other
- Evidence Classification: Public, Internal, Confidential, Restricted
- Retention Period: 1 Year, 3 Years, 5 Years, 7 Years, Indefinite
- Verification Status: Verified, Needs Verification, Missing, Outdated


**Approval_Sign_Off**:

- Approval Decision: Approved, Approved with Conditions, Not Approved - Revisions Required


## Date Format

All date fields use **DD.MM.YYYY** format. DateTime fields use **DD.MM.YYYY HH:MM** format.

## Number Validations

- Test Cases Executed/Passed/Failed: Whole numbers, 0-9999
- Implementation Duration Hours: Decimal, calculated
- Risk Score: Calculated, 1-20 range


---

# Compliance Scoring Methodology

## Change Success Rate Calculation
```
Success Rate % = (Completed Changes / (Completed + Failed + Rolled Back)) × 100

Where:

- Completed = Changes with status "Completed" and verification "Successful"
- Failed = Changes with status "Failed"
- Rolled Back = Changes with status "Rolled Back"


Target: ≥95% overall success rate
```

## Emergency Change Ratio
```
Emergency Ratio % = ((Emergency + Hot Fix) / Total Changes) × 100

Target: <10%
Acceptable: <8%
Concern: 10-15%
Critical: >15% (indicates process problems or inadequate planning)
```

## Approval Compliance
```
Approval Compliance % = (Changes with Proper Approval / Total Changes) × 100

Proper Approval means:

- Approval tier matches risk level (High Risk = Three-Tier)
- All required approvers signed off
- Emergency changes have post-facto CAB review


Target: 100%
```

## Testing Coverage
```
Testing Coverage % = (Changes with Testing / Changes Requiring Testing) × 100

Changes Requiring Testing:

- All Normal changes: 100%
- Standard changes: May use templated testing
- Emergency changes: Abbreviated acceptable if documented


Target: 100% for Normal, 80% for Emergency
```

## Rollback Readiness
```
Rollback Readiness % = (High-Risk Changes with Ready Rollback / Total High-Risk Changes) × 100

Ready Rollback means:

- Rollback procedure documented
- Rollback tested successfully
- Data backup verified (if applicable)


Target: 100% for Critical/High risk changes
```

## Overall Change Control Compliance
```
Overall Compliance = 
  (Approval Compliance × 30%) +
  (Testing Coverage × 25%) +
  (Success Rate × 25%) +
  (Rollback Readiness × 20%)

Target: ≥95%

Status:

- Compliant: ≥95%
- Partially Compliant: 90-94%
- Non-Compliant: <90%

```

---

# Usage Instructions

## Step-by-Step Completion Guide

**Phase 1: Setup and Training** (Week 1)
1. Configuration Manager distributes workbook to Change Coordinator
2. Train change coordinators on workbook usage
3. Establish Change ID numbering convention (e.g., CHG-2026-NNN)
4. Set up integration with existing ticketing system if applicable

**Phase 2: Ongoing Change Tracking** (Continuous)
1. For each configuration change:

   - Create entry in Change_Request_Register (assign Change ID)
   - Complete Impact_Assessment before submission for approval
   - Document approval in Change_Approval_Workflow
   - Record testing in Testing_Validation
   - Document rollback plan in Rollback_Capability (if required)
   - Log implementation in Implementation_Log
   - Update Change_Request_Register status as change progresses

2. For emergency changes:

   - Follow expedited process
   - Create entry in Emergency_Changes immediately after implementation
   - Ensure CAB review within 5 business days


**Phase 3: Monthly Review** (Days 1-5 of each month)
1. Change Coordinator reviews previous month's changes
2. Verify all changes have complete documentation
3. Identify any incomplete records and follow up
4. Review Change_Success_Metrics for trends
5. Document gaps or issues in preparation for quarterly assessment

**Phase 4: Quarterly Assessment** (Last week of quarter)
1. Configuration Manager performs comprehensive review
2. Analyze Compliance_Dashboard metrics
3. Review emergency change ratio and justifications
4. Identify process improvement opportunities
5. Compile evidence in Evidence_Register
6. Complete Reviewer Sign-Off

**Phase 5: Annual Approval** (Quarterly or Semi-Annual)
1. IT Manager/CISO reviews assessment
2. Evaluate overall change management effectiveness
3. Approve remediation plans for identified gaps
4. Complete Approver Sign-Off

## Roles and Responsibilities

**Change Coordinator (Preparer)**:

- Document all changes in Change_Request_Register
- Complete Impact_Assessment for each change
- Track changes through approval and implementation
- Maintain Evidence_Register
- Monthly review of change records


**Configuration Manager (Reviewer)**:

- Quarterly comprehensive assessment
- Verify process compliance
- Analyze success metrics and trends
- Identify improvement opportunities
- Complete Reviewer Sign-Off


**IT Manager / CISO (Approver)**:

- Review overall change management effectiveness
- Approve assessment and remediation plans
- Complete Approver Sign-Off
- Authorize process improvements


**Change Advisory Board (CAB)**:

- Review and approve high-risk changes
- Retrospective review of emergency changes
- Provide governance oversight
- Approve process changes


## Common Questions

**Q: How do Standard changes (pre-approved) fit into this process?**
A: Standard changes still need tracking in Change_Request_Register, but approval workflow is simplified. Document "Automated (Standard)" as approval method. Testing may be templated. Focus on tracking execution and outcomes.

**Q: What if a change doesn't fit cleanly into Normal/Emergency/etc?**
A: Use risk-based judgment. If in doubt, classify as Normal (requires full process). It's better to over-document than under-document. CAB can adjust classification during review.

**Q: How do we handle changes that span multiple systems/teams?**
A: Create single Change ID for coordinated change. Document all affected systems in Impact_Assessment. Ensure all teams document their implementation in Implementation_Log with notes indicating coordination.

**Q: What constitutes "adequate" testing for approval?**
A: Depends on risk. Normal changes: Test pass rate ≥95%. Emergency changes: Testing may be abbreviated but must be documented. Hot Fix: Minimal testing acceptable if critical and rollback plan exists.

**Q: How strictly should we enforce the 10% emergency change limit?**
A: This is a health indicator, not absolute rule. If emergency ratio >10%, investigate why:

- Are truly emergencies, or is planning inadequate?
- Is emergency process being abused for convenience?
- Are there systemic issues (infrastructure instability, poor monitoring)?

Use as trigger for process improvement, not punitive measure.

**Q: What if rollback is impossible (e.g., irreversible database migration)?**
A: Document in Rollback_Capability why rollback is not possible. Provide mitigation strategy (extensive testing, phased approach, manual data recovery procedure). Requires explicit approval acknowledgment of risk.

---

# Integration Points with Other Assessments

## Cross-Assessment Dependencies

| This Assessment | Integrates With | Integration Mechanism | Data Flow |
|----------------|----------------|----------------------|-----------|
| Change_Request_Register | ISMS-IMP-A.8.9.1 (Baseline) | Changes update baselines → version control | Changes → New baseline versions |
| Implementation_Log | ISMS-IMP-A.8.9.3 (Monitoring) | Changes trigger monitoring of new config state | Change completion → Monitoring baseline update |
| Testing_Validation | ISMS-IMP-A.8.9.4 (Hardening) | Testing includes security hardening validation | Test results → Hardening compliance evidence |
| Emergency_Changes | A.6.8 (Incident Management) | Incidents may trigger emergency changes | Incidents → Emergency changes → Post-incident review |

## Process Integration

**Change → Baseline Update Flow**:
1. Change completed (Implementation_Log: status = Successful)
2. If baseline affected, update Version_Control in ISMS-IMP-A.8.9.1
3. Record new baseline version with Change ID as reference
4. Update affected assets in Asset_Inventory with new baseline reference

**Change → Monitoring Integration**:
1. Change implementation updates expected configuration state
2. Monitoring system (ISMS-IMP-A.8.9.3) updated with new baseline
3. Configuration drift detection validates change was applied correctly
4. Monitoring alerts if configuration reverts unexpectedly

---

# Evidence Collection Guidelines

## Required Evidence Types

**Approval Evidence**:

- CAB meeting minutes (with attendance, decisions, voting records)
- Email approval chains (with timestamps, full headers)
- Emergency verbal approval documentation (who, when, what, confirmation method)


**Testing Evidence**:

- Test plans and test cases
- Test execution results (pass/fail per test case)
- Screenshots of test environments
- Test data summaries
- Go/No-Go decision records


**Implementation Evidence**:

- Before/after configuration snapshots
- Implementation checklists (completed)
- Verification screenshots showing change applied
- Monitoring dashboards showing successful change
- Backup verification records (pre-change backups)


**Rollback Evidence**:

- Rollback procedure documents
- Rollback test results (in non-production)
- Backup/snapshot verification
- Rollback trigger criteria documentation


**Emergency Change Evidence**:

- Emergency declaration notification
- Incident records triggering emergency change
- Post-facto CAB review minutes
- Justification documentation


## Evidence Quality Standards

**Good Evidence**:

- Timestamped with date/time visible
- Attributable (shows who made decision/performed action)
- Authentic (original or certified copy)
- Complete (full context, not excerpts)
- Retained per retention policy


**Poor Evidence**:

- Undated screenshots
- "Approvals" without verifiable record
- Verbal agreements not documented
- Partial records (missing context)
- Evidence on personal storage only


---

# Document Maintenance

## Update Frequency

- **Real-time**: Change_Request_Register updated as changes occur
- **Daily**: High-priority change status updates
- **Weekly**: Review pending approvals, testing in progress
- **Monthly**: Metrics review, gap identification
- **Quarterly**: Comprehensive assessment, formal review
- **Annual**: Process improvement review, metrics trends analysis


## Workbook Versioning

File naming: `ISMS_A_8_9_2_Change_Control_Assessment_YYYYMMDD.xlsx`

Retain versions:

- Monthly snapshots (for trend analysis)
- Quarterly assessments (formal records)
- All versions for minimum 3 years (audit trail)


---

# Specification Approval

**Document Owner**: Configuration Manager  
**Technical Review**: Change Advisory Board, ISMS Implementation Team  
**Approval**: CISO / IT Management  

**This specification defines the structure and content of the Change Control Assessment workbook. The Python script `generate_a89_2_change_control.py` will implement this specification to create the actual Excel workbook.**

---

**END OF SPECIFICATION**

---

*"The process of analogy-making lies at the heart of intelligence."*
— Douglas Hofstadter

*Where bamboo antennas actually work.* 🎋
