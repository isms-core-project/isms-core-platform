# ISMS-IMP-A.5.37.3 - Procedure Review and Update Tracking

## Document Information

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.37.3 |
| **Control Reference** | ISO/IEC 27001:2022 - Control A.5.37: Documented Operating Procedures |
| **Version** | 1.0 |
| **Classification** | Internal Use |
| **Owner** | Information Security Manager |
| **Last Review** | [Date to be set] |

---

## Control Requirement

> "Operating procedures for information processing facilities should be documented and made available to personnel who need them."
>
> — ISO/IEC 27001:2022, Annex A Control 5.37

---

# PART I: USER GUIDE

## 1. Purpose

This workbook tracks the review cycle and change management for documented operating procedures. It ensures procedures remain current, accurate, and aligned with actual systems and processes. Procedures must be treated as living documents requiring regular review and updates when systems change.

## 2. Review Requirements

### 2.1 Mandatory Review Triggers

| Trigger | Review Type | Timeframe |
|---------|-------------|-----------|
| **Scheduled Review** | Full review | Per review cycle (annual default) |
| **System Change** | Targeted review | Within 30 days of change |
| **Incident Related** | Targeted review | Within 14 days of incident |
| **Regulatory Change** | Compliance review | Within 60 days of effective date |
| **Audit Finding** | Corrective review | Per CAR timeline |
| **Personnel Change** | Owner verification | Within 30 days |

### 2.2 Review Cycle by Criticality

| Criticality | Review Cycle | Rationale |
|-------------|:------------:|-----------|
| **Critical** | 6 months | High-impact procedures require frequent validation |
| **High** | 12 months | Standard annual review |
| **Medium** | 12 months | Standard annual review |
| **Low** | 24 months | Extended cycle for stable procedures |

### 2.3 Review Outcomes

| Outcome | Action Required |
|---------|-----------------|
| **Current - No Changes** | Document review, update review date |
| **Minor Updates** | Apply changes, increment version (X.Y+1) |
| **Major Updates** | Full rewrite, increment version (X+1.0), re-approval |
| **Obsolete** | Archive procedure, remove from active use |
| **Superseded** | Replace with new procedure, archive old |

## 3. Change Management Process

### 3.1 Change Categories

| Category | Description | Approval |
|----------|-------------|----------|
| **Administrative** | Typos, formatting, contact updates | Procedure Owner |
| **Minor** | Clarifications, step refinements | Procedure Owner + Reviewer |
| **Major** | Process changes, new steps | Management Approval |
| **Emergency** | Urgent operational changes | Expedited approval + retrospective |

### 3.2 Change Workflow

1. **Initiate Change Request** - Document reason and proposed changes
2. **Impact Assessment** - Evaluate training, system, and compliance impacts
3. **Draft Updates** - Prepare revised procedure
4. **Review & Approve** - Per approval matrix
5. **Publish & Communicate** - Update repository, notify affected personnel
6. **Verify Access** - Confirm updated version accessible
7. **Training (if required)** - Update personnel on changes

## 4. Using This Workbook

### Step 1: Review Schedule Management
- Monitor upcoming reviews via dashboard
- Assign reviewers 30 days before due date
- Track overdue reviews for escalation

### Step 2: Change Request Processing
- Log all change requests
- Track through approval workflow
- Document implementation evidence

### Step 3: Communication Tracking
- Record notification distribution
- Confirm acknowledgement where required
- Track training completion

---

# PART II: TECHNICAL SPECIFICATION

## 4. Workbook Structure

### Sheet 1: Review_Schedule
**Purpose:** Track scheduled and completed reviews

| Column | Header | Data Type | Validation | Description |
|:------:|--------|-----------|------------|-------------|
| A | Procedure_ID | Text | From Inventory | Reference to A.5.37.1 |
| B | Procedure_Name | Text | Lookup | Auto-populated |
| C | Criticality | Text | Lookup | From inventory |
| D | Review_Cycle_Days | Number | Lookup | Based on criticality |
| E | Last_Review_Date | Date | Required | Most recent review |
| F | Next_Review_Due | Date | Formula | E + D |
| G | Days_Until_Due | Number | Formula | F - TODAY() |
| H | Review_Status | Text | Formula | Overdue/Due Soon/Current |
| I | Assigned_Reviewer | Text | Required | Person assigned |
| J | Review_Started | Date | Optional | When review began |
| K | Review_Completed | Date | Optional | When review completed |
| L | Review_Outcome | List | Dropdown | Current/Minor/Major/Obsolete |
| M | New_Version | Text | Conditional | Version after update |
| N | Notes | Text | Optional | Review notes |

### Sheet 2: Change_Requests
**Purpose:** Log and track procedure change requests

| Column | Header | Data Type | Validation | Description |
|:------:|--------|-----------|------------|-------------|
| A | CR_ID | Text | Auto | Change request ID (CR-YYYYMM-NNN) |
| B | Procedure_ID | Text | From Inventory | Affected procedure |
| C | Request_Date | Date | Required | When submitted |
| D | Requestor | Text | Required | Person requesting change |
| E | Change_Category | List | Dropdown | Administrative/Minor/Major/Emergency |
| F | Trigger | List | Dropdown | Scheduled/System/Incident/Regulatory/Audit |
| G | Description | Text | Required | Change description |
| H | Justification | Text | Required | Reason for change |
| I | Impact_Assessment | Text | Required | Training/System/Compliance impacts |
| J | Status | List | Dropdown | Submitted/Under Review/Approved/Rejected/Implemented |
| K | Approver | Text | Conditional | Who approved |
| L | Approval_Date | Date | Conditional | When approved |
| M | Implementation_Date | Date | Conditional | When implemented |
| N | Verification | Text | Optional | Implementation verification |

### Sheet 3: Version_History
**Purpose:** Track version history for each procedure

| Column | Header | Data Type | Description |
|:------:|--------|-----------|-------------|
| A | Procedure_ID | Text | Reference to procedure |
| B | Version | Text | Version number |
| C | Effective_Date | Date | When version became active |
| D | Supersedes | Text | Previous version |
| E | Change_Summary | Text | Summary of changes |
| F | CR_Reference | Text | Related change request |
| G | Approved_By | Text | Approver name |
| H | Status | List | Active/Superseded/Archived |

### Sheet 4: Communication_Log
**Purpose:** Track procedure update communications

| Column | Header | Data Type | Description |
|:------:|--------|-----------|-------------|
| A | Comm_ID | Text | Communication identifier |
| B | Procedure_ID | Text | Related procedure |
| C | Version | Text | Version communicated |
| D | Communication_Date | Date | When sent |
| E | Communication_Method | List | Email/Intranet/Meeting/Training |
| F | Audience | Text | Who was notified |
| G | Acknowledgement_Required | Boolean | Yes/No |
| H | Acknowledgement_Rate | Number | % acknowledged |
| I | Training_Required | Boolean | Yes/No |
| J | Training_Completion | Number | % completed training |

### Sheet 5: Overdue_Escalation
**Purpose:** Track escalations for overdue reviews

| Column | Header | Data Type | Description |
|:------:|--------|-----------|-------------|
| A | Procedure_ID | Text | Overdue procedure |
| B | Days_Overdue | Number | Days past due date |
| C | Escalation_Level | List | L1/L2/L3 |
| D | Escalated_To | Text | Escalation recipient |
| E | Escalation_Date | Date | When escalated |
| F | Response_Required_By | Date | Response deadline |
| G | Status | List | Open/Acknowledged/Resolved |
| H | Resolution | Text | How resolved |

**Escalation Matrix:**
- L1 (1-14 days overdue): Procedure Owner + Line Manager
- L2 (15-30 days overdue): Department Head + ISM
- L3 (>30 days overdue): CISO + Executive Management

### Sheet 6: Evidence_Register
**Purpose:** Link to review and change evidence

| Column | Header | Data Type | Description |
|:------:|--------|-----------|-------------|
| A | Evidence_ID | Text | Unique identifier |
| B | Evidence_Type | List | Review Record/Approval/Communication/Training |
| C | Related_CR | Text | Change request reference |
| D | Related_Procedure | Text | Procedure ID |
| E | Description | Text | Evidence description |
| F | Collection_Date | Date | When collected |
| G | Location | Text | Storage location |

### Sheet 7: Instructions
**Purpose:** User guidance for review and change management

Static content including:
- Review process workflow
- Change category definitions
- Escalation procedures
- Communication templates

## 5. Formulas and Calculations

### Days Until Due
```excel
=F2-TODAY()
```

### Review Status
```excel
=IF(G2<0,"OVERDUE",IF(G2<=30,"DUE SOON","CURRENT"))
```

### Overdue Count by Criticality
```excel
=COUNTIFS(C:C,"Critical",H:H,"OVERDUE")
```

### Average Days to Complete Review
```excel
=AVERAGE(K:K-J:J)
```

### Change Request Cycle Time
```excel
=AVERAGE(Change_Requests!M:M-Change_Requests!C:C)
```

### Communication Acknowledgement Rate
```excel
=AVERAGE(Communication_Log!H:H)
```

## 6. Conditional Formatting Rules

| Range | Condition | Format |
|-------|-----------|--------|
| Review Status | "OVERDUE" | Red fill, white bold text |
| Review Status | "DUE SOON" | Yellow fill |
| Days Overdue | >30 | Red fill |
| Days Overdue | 15-30 | Orange fill |
| CR Status | "Rejected" | Grey strikethrough |
| Acknowledgement Rate | <80% | Yellow fill |
| Acknowledgement Rate | <50% | Red fill |

## 7. Data Validation

### Change Category
- Administrative, Minor, Major, Emergency

### Trigger Values
- Scheduled Review, System Change, Incident Related, Regulatory Change, Audit Finding, Personnel Change

### Review Outcome
- Current - No Changes, Minor Updates, Major Updates, Obsolete, Superseded

## 8. Integration Points

### Upstream Dependencies
- A.5.37.1 Procedure Inventory
- Change management system
- Incident management (for incident-triggered reviews)

### Downstream Consumers
- A.5.37.4 Compliance Dashboard
- Audit trail reports
- Management reviews

## 9. Output Metrics

| Metric | Formula | Target |
|--------|---------|--------|
| Reviews On-Time | On-time/Total | >95% |
| Overdue Reviews | COUNTIF(OVERDUE) | 0 |
| Avg Review Cycle Time | Days from start to complete | <14 days |
| Change Request Approval Rate | Approved/Total | Track trend |
| Communication Acknowledgement | Average rate | >90% |

---

**END OF SPECIFICATION**

---

*"Change is inevitable. Growth is optional."*
— John C. Maxwell

*Where bamboo antennas actually work.* 🎋

<!-- QA_VERIFIED: 2026-02-01 -->
