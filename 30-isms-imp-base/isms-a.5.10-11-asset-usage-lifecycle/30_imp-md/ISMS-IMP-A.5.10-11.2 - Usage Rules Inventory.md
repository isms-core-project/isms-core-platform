# ISMS-IMP-A.5.10-11.2 — Usage Rules Inventory

---

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.10-11.2 |
| **Title** | Usage Rules Inventory |
| **Control Reference** | ISO/IEC 27001:2022 A.5.10 |
| **Control Name** | Acceptable Use of Information and Other Associated Assets |
| **Document Type** | Implementation Guide |
| **Version** | 1.0 |
| **Last Updated** | [Date to be set] |
| **Owner** | Information Security Manager |
| **Classification** | Internal |

---

## PART I: USER COMPLETION GUIDE

### Assessment Overview

**Purpose**

This workbook documents specific usage rules by asset category, providing a detailed inventory of permitted activities, prohibited activities, and handling requirements that support the Acceptable Use Policy.

**Scope**

This assessment covers:
- Usage rules inventory by asset category
- Permitted activities with conditions
- Prohibited activities with risk classifications
- Handling requirements by data classification
- Rule enforcement and monitoring requirements

**What This Assessment Covers**

| Domain | Assessment Focus |
|--------|------------------|
| Usage Rules | Rules for each asset category |
| Permitted Activities | What users may do and under what conditions |
| Prohibited Activities | What users must not do and consequences |
| Handling Requirements | How to handle assets by classification |

**Control Requirement**

ISO 27001:2022 A.5.10 states:

> "Rules for the acceptable use of information and other associated assets should be identified, documented and implemented."

This workbook documents the specific rules referenced by the Acceptable Use Policy.

### Prerequisites

Before completing this assessment:

- [ ] Approved Acceptable Use Policy (ISMS-POL-A.5.10-11)
- [ ] Asset inventory per ISMS-POL-A.5.9
- [ ] Data classification scheme
- [ ] Input from asset owners and operational teams
- [ ] Legal/HR review for employment-related rules

### Workbook Structure

| Sheet | Purpose | Key Actions |
|-------|---------|-------------|
| Instructions | Guidance and metadata | Complete document information |
| Usage_Rules | Master inventory of rules | Document all usage rules |
| Permitted_Activities | Permitted use details | Document allowed activities |
| Prohibited_Activities | Prohibited actions | Document forbidden activities |
| Handling_Requirements | Asset handling specs | Define handling by classification |
| Evidence_Register | Audit evidence linking | Document evidence locations |
| Approval_SignOff | Assessment approval | Obtain required signatures |

### Completion Walkthrough

**Step 1: Document Information (Instructions Sheet)**

Complete all metadata fields including assessment date, assessor, and organisation.

**Step 2: Usage Rules Inventory (Usage_Rules Sheet)**

For each usage rule:

1. **Rule_ID** - Auto-generated unique identifier
2. **Asset_Category** - Select applicable asset type
3. **Rule_Description** - Clear, specific rule statement
4. **Classification** - Permitted/Permitted with Conditions/Prohibited
5. **Applies_To** - Who the rule applies to
6. **Enforcement_Method** - How the rule is enforced
7. **Monitoring_Required** - Whether usage is monitored

**Rule Writing Guidelines**:

| Good Rule | Poor Rule |
|-----------|-----------|
| "Email may be used for business communications; personal use limited to breaks" | "Be careful with email" |
| "USB drives prohibited unless encrypted and approved" | "Don't use USB drives" |

**Step 3: Permitted Activities (Permitted_Activities Sheet)**

Document what users ARE allowed to do:

1. **Asset_Category** - Which assets
2. **Permitted_Activity** - Specific allowed action
3. **Conditions** - Any restrictions or requirements
4. **Approval_Required** - Whether prior approval needed
5. **Time_Restrictions** - When activity is permitted
6. **Documentation_Required** - What records to keep

**Step 4: Prohibited Activities (Prohibited_Activities Sheet)**

Document what users MUST NOT do:

1. **Asset_Category** - Which assets
2. **Prohibited_Activity** - Specific forbidden action
3. **Reason** - Why it's prohibited (risk basis)
4. **Risk_Level** - Critical/High/Medium/Low
5. **Detection_Method** - How violations are detected
6. **Consequence** - What happens if violated
7. **Exception_Possible** - Whether exceptions can be granted

**Step 5: Handling Requirements (Handling_Requirements Sheet)**

Define how to handle assets by classification:

1. **Asset_Category** - Asset type
2. **Data_Classification** - Public/Internal/Confidential/Restricted
3. **Storage_Requirement** - Where/how to store
4. **Transmission_Requirement** - How to send/share
5. **Disposal_Requirement** - How to dispose
6. **Encryption_Required** - Whether encryption needed

**Step 6: Evidence and Approval**

Complete Evidence_Register linking to supporting documents, then obtain required approvals.

### Evidence Collection

**Required Evidence**:

| Evidence Type | Description | Storage Location |
|---------------|-------------|------------------|
| Asset Inventory | Categories covered by rules | ISMS Evidence Library |
| AUP Document | Policy these rules support | ISMS Evidence Library |
| Legal Review | Compliance verification | ISMS Evidence Library |
| Stakeholder Sign-off | Asset owner approvals | ISMS Evidence Library |

### Common Pitfalls

❌ **MISTAKE**: Writing vague rules like "use responsibly"
✅ **CORRECT**: Write specific, actionable rules with clear boundaries

❌ **MISTAKE**: Not specifying enforcement method
✅ **CORRECT**: Every rule should explain how compliance is verified

❌ **MISTAKE**: Missing risk justification for prohibitions
✅ **CORRECT**: Document WHY each activity is prohibited

❌ **MISTAKE**: Inconsistent handling requirements across categories
✅ **CORRECT**: Ensure handling requirements follow data classification consistently

❌ **MISTAKE**: Not considering all user types (employees, contractors, guests)
✅ **CORRECT**: Specify which rules apply to which personnel categories

❌ **MISTAKE**: Rules that conflict with operational needs
✅ **CORRECT**: Validate rules with operational teams before finalising

❌ **MISTAKE**: No exception process for prohibited activities
✅ **CORRECT**: Document whether and how exceptions can be requested

❌ **MISTAKE**: Failing to link rules to consequences
✅ **CORRECT**: Each prohibition should reference the consequence

### Quality Checklist

Before submitting:

- [ ] All asset categories have defined rules
- [ ] Each rule is specific and actionable
- [ ] Permitted activities have clear conditions
- [ ] Prohibited activities have risk classifications
- [ ] Handling requirements align with data classification
- [ ] Evidence linked for all documented rules
- [ ] Approvals obtained from stakeholders

### Review & Approval

**Review Workflow**:

1. Assessor documents all rules
2. Asset owners review applicable rules
3. Legal/HR review employment implications
4. CISO approves final inventory

---

## PART II: TECHNICAL SPECIFICATION

### Workbook Architecture

**File Details**:

- Filename: `ISMS-IMP-A.5.10-11.2_Usage_Rules_Inventory_YYYYMMDD.xlsx`
- Format: Microsoft Excel (.xlsx)
- Sheets: 7

### Sheet Specifications

#### Usage_Rules Sheet

**Columns**:

| Column | Header | Width | Content |
|--------|--------|-------|---------|
| A | Rule_ID | 14 | Auto-generated (UR-001, etc.) |
| B | Asset_Category | 25 | User selection |
| C | Rule_Description | 50 | User input |
| D | Classification | 20 | Data validation |
| E | Applies_To | 22 | User input |
| F | Enforcement_Method | 22 | User input |
| G | Monitoring_Required | 16 | Data validation: Yes/No |
| H | Exception_Process | 18 | User input |
| I | Policy_Reference | 20 | AUP section reference |
| J | Last_Updated | 14 | Date field |
| K | Owner | 22 | User input |
| L | Notes | 30 | User input |

**Pre-populated Rules**: 15 common usage rules with colour-coded classifications

#### Permitted_Activities Sheet

**Columns**:

| Column | Header | Width | Content |
|--------|--------|-------|---------|
| A | Activity_ID | 14 | Auto-generated (PA-001, etc.) |
| B | Asset_Category | 22 | User selection |
| C | Permitted_Activity | 45 | User input |
| D | Conditions | 35 | User input |
| E | Approval_Required | 16 | Data validation: Yes/No |
| F | Approver_Role | 22 | User input |
| G | Time_Restrictions | 20 | User input |
| H | Location_Restrictions | 22 | User input |
| I | Documentation_Required | 20 | Data validation: Yes/No |
| J | Notes | 30 | User input |

#### Prohibited_Activities Sheet

**Columns**:

| Column | Header | Width | Content |
|--------|--------|-------|---------|
| A | Prohibition_ID | 14 | Auto-generated (PH-001, etc.) |
| B | Asset_Category | 22 | User selection |
| C | Prohibited_Activity | 45 | User input |
| D | Reason | 35 | User input |
| E | Risk_Level | 14 | Data validation |
| F | Detection_Method | 25 | User input |
| G | Consequence | 25 | User input |
| H | Exception_Possible | 16 | Data validation: Yes/No |
| I | Related_Control | 18 | ISO control reference |
| J | Notes | 30 | User input |

**Pre-populated Prohibitions**: 8 common critical prohibitions

#### Handling_Requirements Sheet

**Columns**:

| Column | Header | Width | Content |
|--------|--------|-------|---------|
| A | Handling_ID | 14 | Auto-generated (HR-001, etc.) |
| B | Asset_Category | 22 | User selection |
| C | Data_Classification | 18 | Data validation |
| D | Storage_Requirement | 30 | User input |
| E | Transmission_Requirement | 30 | User input |
| F | Disposal_Requirement | 30 | User input |
| G | Access_Restriction | 25 | User input |
| H | Labelling_Required | 16 | Data validation: Yes/No |
| I | Encryption_Required | 16 | Data validation: Yes/No |
| J | Retention_Period | 18 | User input |
| K | Notes | 30 | User input |

### Data Validations

| Field | Validation List |
|-------|-----------------|
| Classification | Permitted, Permitted with Conditions, Prohibited, Not Applicable |
| Risk_Level | Critical, High, Medium, Low |
| Data_Classification | Public, Internal, Confidential, Restricted |
| Yes/No fields | Yes, No |

### Generator Reference

**Script**: `generate_a510_11_2_usage_rules_inventory.py`

**Location**: `10-isms-scr-base/isms-a.5.10-11-asset-usage-lifecycle/10_generator-master/`

---

**END OF SPECIFICATION**

---

*"The best security policy is the one that people actually follow."*
— Unknown

<!-- QA_VERIFIED: 2026-02-01 -->
