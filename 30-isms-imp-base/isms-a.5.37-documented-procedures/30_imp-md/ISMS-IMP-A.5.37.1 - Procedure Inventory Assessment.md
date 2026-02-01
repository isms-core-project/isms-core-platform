# ISMS-IMP-A.5.37.1 - Procedure Inventory Assessment

## Document Information

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.37.1 |
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

This workbook enables systematic inventory and assessment of all documented operating procedures across [Organisation]'s information processing facilities. It captures the complete catalogue of procedures, their ownership, accessibility, and currency status.

## 2. Scope

### In Scope
- All documented operating procedures for information processing
- Physical facility operational procedures (HVAC, access controls, alarms)
- IT system operational procedures (backup, recovery, maintenance)
- Security-specific operational procedures
- Emergency and incident response procedures
- Change management procedures

### Out of Scope
- Policy documents (covered by A.5.1)
- Project-specific documentation
- End-user application guides (unless security-relevant)

## 3. Assessment Approach

### 3.1 Procedure Categories

| Category | Description | Examples |
|----------|-------------|----------|
| **System Operations** | Core IT system procedures | Backup, restart, monitoring |
| **Security Operations** | Security-specific procedures | Incident response, access review |
| **Facility Operations** | Physical facility procedures | HVAC, fire suppression, entry |
| **Change Management** | Change control procedures | CAB process, emergency change |
| **Recovery Operations** | Business continuity procedures | DR activation, failover |
| **User Management** | Identity lifecycle procedures | Onboarding, offboarding |

### 3.2 Assessment Criteria

Each procedure is assessed against:

| Criterion | Weight | Description |
|-----------|:------:|-------------|
| **Documented** | 20% | Written procedure exists |
| **Accessible** | 20% | Available to personnel who need it |
| **Current** | 20% | Reviewed within review cycle |
| **Complete** | 20% | Covers all necessary steps |
| **Approved** | 20% | Formally approved by management |

## 4. Using This Workbook

### Step 1: Inventory Discovery
- Identify all process owners across departments
- Collect existing procedure documentation
- Map procedures to ISO 27001 controls

### Step 2: Completeness Assessment
- Review each procedure against assessment criteria
- Identify gaps (undocumented critical processes)
- Document procedure locations

### Step 3: Gap Analysis
- Compare against required procedure catalogue
- Prioritise procedures needing creation/update
- Assign ownership for remediation

---

# PART II: TECHNICAL SPECIFICATION

## 5. Workbook Structure

### Sheet 1: Procedure_Inventory
**Purpose:** Master catalogue of all documented procedures

| Column | Header | Data Type | Validation | Description |
|:------:|--------|-----------|------------|-------------|
| A | Procedure_ID | Text | Required | Unique identifier (e.g., SOP-IT-001) |
| B | Procedure_Name | Text | Required | Descriptive name |
| C | Category | List | Dropdown | System/Security/Facility/Change/Recovery/User |
| D | Process_Owner | Text | Required | Responsible person/role |
| E | Department | Text | Required | Owning department |
| F | Document_Location | Text | Required | Repository path/URL |
| G | Last_Review_Date | Date | DD.MM.YYYY | Most recent review date |
| H | Next_Review_Due | Date | Formula | =G+Review_Cycle |
| I | Review_Cycle_Days | Number | Default=365 | Days between reviews |
| J | Version | Text | Format X.Y | Current version number |
| K | Approval_Status | List | Dropdown | Draft/Pending/Approved/Expired |
| L | Approver | Text | Conditional | Required if Approved |
| M | Approval_Date | Date | Conditional | Required if Approved |
| N | Related_Controls | Text | Multi-value | ISO 27001 control references |
| O | Criticality | List | Dropdown | Critical/High/Medium/Low |
| P | Notes | Text | Optional | Additional information |

**Dropdown Values:**

- **Category:** System Operations, Security Operations, Facility Operations, Change Management, Recovery Operations, User Management, Other
- **Approval_Status:** Draft, Pending Approval, Approved, Expired, Under Review
- **Criticality:** Critical, High, Medium, Low

### Sheet 2: Required_Procedures
**Purpose:** Reference list of procedures required for ISO 27001 compliance

| Column | Header | Data Type | Description |
|:------:|--------|-----------|-------------|
| A | Reference_ID | Text | Standard reference identifier |
| B | Required_Procedure | Text | Procedure name/description |
| C | ISO_Control | Text | Related ISO 27001 control |
| D | Category | List | Procedure category |
| E | Priority | List | Implementation priority |
| F | Current_Status | List | Exists/Partial/Missing |
| G | Mapped_Procedure_ID | Text | Link to Procedure_Inventory |
| H | Gap_Notes | Text | Gap description if missing |

### Sheet 3: Accessibility_Matrix
**Purpose:** Map procedures to roles that need access

| Column | Header | Data Type | Description |
|:------:|--------|-----------|-------------|
| A | Procedure_ID | Text | Reference to inventory |
| B | Role_1 | Boolean | IT Operations access |
| C | Role_2 | Boolean | Security Team access |
| D | Role_3 | Boolean | Facilities access |
| E | Role_4 | Boolean | Help Desk access |
| F | Role_5 | Boolean | Management access |
| G | Access_Method | Text | How access is provided |
| H | Verified_Date | Date | Last access verification |

### Sheet 4: Gap_Analysis
**Purpose:** Track procedure gaps and remediation

| Column | Header | Data Type | Description |
|:------:|--------|-----------|-------------|
| A | Gap_ID | Text | Unique gap identifier |
| B | Gap_Type | List | Missing/Incomplete/Outdated/Unapproved |
| C | Procedure_Reference | Text | Procedure ID or description |
| D | Severity | List | Critical/High/Medium/Low |
| E | Identified_Date | Date | When gap was identified |
| F | Remediation_Owner | Text | Responsible party |
| G | Target_Date | Date | Remediation deadline |
| H | Status | List | Open/In Progress/Closed |
| I | Completion_Date | Date | When resolved |
| J | Evidence | Text | Remediation evidence reference |

### Sheet 5: Evidence_Register
**Purpose:** Link to supporting evidence

| Column | Header | Data Type | Description |
|:------:|--------|-----------|-------------|
| A | Evidence_ID | Text | Unique evidence identifier |
| B | Evidence_Type | List | Document/Screenshot/Export/Attestation |
| C | Description | Text | Evidence description |
| D | Related_Procedure | Text | Procedure ID reference |
| E | Collection_Date | Date | When evidence collected |
| F | Location | Text | Evidence storage location |
| G | Collected_By | Text | Person who collected |
| H | Valid_Until | Date | Evidence expiry |

### Sheet 6: Instructions
**Purpose:** User guidance and reference information

Static content including:
- Assessment methodology
- Category definitions
- Scoring criteria
- Contact information

## 6. Formulas and Calculations

### Review Status Calculation
```excel
=IF(H2<TODAY(),"OVERDUE",IF(H2<TODAY()+30,"DUE SOON","CURRENT"))
```

### Compliance Score per Category
```excel
=COUNTIFS(Procedure_Inventory!C:C,A2,Procedure_Inventory!K:K,"Approved")/
 COUNTIF(Procedure_Inventory!C:C,A2)*100
```

### Gap Count by Severity
```excel
=COUNTIFS(Gap_Analysis!D:D,"Critical",Gap_Analysis!H:H,"Open")
```

## 7. Conditional Formatting Rules

| Range | Condition | Format |
|-------|-----------|--------|
| Review Status | "OVERDUE" | Red fill, white text |
| Review Status | "DUE SOON" | Yellow fill |
| Approval Status | "Expired" | Red fill |
| Gap Status | "Open" + "Critical" | Red fill, bold |
| Compliance % | <70% | Red fill |
| Compliance % | 70-90% | Yellow fill |
| Compliance % | >90% | Green fill |

## 8. Data Validation

### Procedure_ID Format
- Pattern: `[A-Z]{3}-[A-Z]{2,4}-[0-9]{3}`
- Example: SOP-IT-001, SOP-SEC-012

### Date Validation
- Format: DD.MM.YYYY
- Range: 01.01.2020 to 31.12.2030

### Cross-Reference Validation
- Mapped_Procedure_ID must exist in Procedure_Inventory
- Related_Procedure must exist in Procedure_Inventory

## 9. Integration Points

### Upstream Dependencies
- Organisational structure (departments, roles)
- Document management system inventory
- ISO 27001 control mapping

### Downstream Consumers
- A.5.37.2 Procedure Quality Assessment
- A.5.37.4 Compliance Dashboard
- Audit evidence packages

## 10. Output Metrics

| Metric | Formula | Target |
|--------|---------|--------|
| Total Procedures Documented | COUNT(Procedure_Inventory) | - |
| Procedures Current | COUNTIF(Status="CURRENT") | >90% |
| Procedures Approved | COUNTIF(Approval="Approved") | 100% |
| Critical Gaps Open | COUNTIF(Critical+Open) | 0 |
| Coverage by Category | Per-category calculation | 100% |

---

**END OF SPECIFICATION**

---

*"The difference between a good organisation and a great one is often found in the quality of their documented procedures."*
— W. Edwards Deming

*Where bamboo antennas actually work.* 🎋

<!-- QA_VERIFIED: 2026-02-01 -->
