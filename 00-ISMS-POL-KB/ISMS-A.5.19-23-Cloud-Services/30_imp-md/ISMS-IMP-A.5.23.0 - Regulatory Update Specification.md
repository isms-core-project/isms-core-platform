# ISMS-IMP-A.5.23.0 - Regulatory Update Specification
## DORA, NIS2, AI Act, CLOUD Act Enhancements

---

## Document Purpose

This document provides precise instructions for updating the existing ISMS-IMP-A.5.23 workbook generators and validators to incorporate regulatory requirements for:

- **DORA** (Digital Operational Resilience Act) — EU financial sector
- **NIS2** (Network and Information Security Directive 2) — EU essential/important entities
- **EU AI Act** — AI system providers and deployers
- **US CLOUD Act** — Jurisdictional data access risks

**Principle:** Changes are ADDITIVE. Existing structure remains intact.

---

## 1. Global Changes (All Workbooks)

### 1.1 New Dropdown Lists (Add to all generators)

```python
# Add to dropdown definitions section of each generator

REGULATORY_SCOPE = [
    "Not Applicable",
    "DORA (Financial Sector)",
    "NIS2 (Essential Entity)",
    "NIS2 (Important Entity)",
    "AI Act (Provider)",
    "AI Act (Deployer)",
    "Multiple Regulations"
]

PROVIDER_HQ_JURISDICTION = [
    "Switzerland",
    "EU/EEA",
    "United Kingdom",
    "United States",
    "Other Adequate Country",
    "Non-Adequate Country"
]

CLOUD_ACT_EXPOSURE = [
    "No Exposure",
    "Potential Exposure (US HQ)",
    "Mitigated (EU Data Boundary)",
    "Mitigated (Encryption + Key Control)",
    "Accepted Risk (Documented)",
    "Under Assessment"
]

AI_RISK_CLASSIFICATION = [
    "Not Applicable",
    "Minimal Risk",
    "Limited Risk (Transparency)",
    "High Risk",
    "Unacceptable Risk (Prohibited)"
]

CONCENTRATION_RISK_LEVEL = [
    "Low (Multiple alternatives)",
    "Medium (Limited alternatives)",
    "High (Few alternatives)",
    "Critical (Single provider dependency)"
]
```

### 1.2 New Instructions Sheet Content

Add to Instructions sheet in ALL workbooks:

```
REGULATORY APPLICABILITY

This workbook includes fields for regulatory frameworks that may or may not apply
to your organization. Complete the following based on your regulatory scope:

| If You Are... | Complete These Fields |
|---------------|----------------------|
| EU Financial Entity | All DORA fields (mandatory) |
| EU Essential/Important Entity | All NIS2 fields (mandatory) |
| Using AI Systems | All AI Act fields |
| Using US-HQ Providers | All CLOUD Act/Jurisdiction fields |
| None of the Above | Mark as "Not Applicable" |

CONCENTRATION RISK

DORA and NIS2 require assessment of concentration risk for critical ICT providers.
Complete concentration risk fields for all Level 1 and Level 2 suppliers.
```

---

## 2. Workbook 5.23.1 — Cloud Service Inventory & Classification

### 2.1 Spec Updates (ISMS-IMP-A.5.23.1)

**Add to Section: Sheet Specifications → Cloud_Service_Inventory**

New columns (insert after existing columns, before Notes):

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| NEW-1 | Provider_HQ_Jurisdiction | 20 | Dropdown | PROVIDER_HQ_JURISDICTION |
| NEW-2 | CLOUD_Act_Exposure | 22 | Dropdown | CLOUD_ACT_EXPOSURE |
| NEW-3 | Data_Processing_Locations | 25 | Text | Free text (list countries) |
| NEW-4 | EU_Data_Boundary_Commitment | 15 | Dropdown | Yes/No/Partial/Unknown |
| NEW-5 | DORA_In_Scope | 12 | Dropdown | Yes/No/Not Determined |
| NEW-6 | NIS2_In_Scope | 12 | Dropdown | Yes/No/Not Determined |
| NEW-7 | AI_System_Classification | 18 | Dropdown | AI_RISK_CLASSIFICATION |
| NEW-8 | Concentration_Risk_Level | 18 | Dropdown | CONCENTRATION_RISK_LEVEL |
| NEW-9 | Alternative_Providers_Identified | 15 | Dropdown | Yes/No/Partial |

### 2.2 Generator Updates (generate_a523_1_inventory.py)

**Location:** After existing column definitions

```python
# ADD: Regulatory columns
regulatory_columns = [
    ("Provider_HQ_Jurisdiction", 20, PROVIDER_HQ_JURISDICTION),
    ("CLOUD_Act_Exposure", 22, CLOUD_ACT_EXPOSURE),
    ("Data_Processing_Locations", 25, None),  # Free text
    ("EU_Data_Boundary_Commitment", 15, ["Yes", "No", "Partial", "Unknown"]),
    ("DORA_In_Scope", 12, ["Yes", "No", "Not Determined"]),
    ("NIS2_In_Scope", 12, ["Yes", "No", "Not Determined"]),
    ("AI_System_Classification", 18, AI_RISK_CLASSIFICATION),
    ("Concentration_Risk_Level", 18, CONCENTRATION_RISK_LEVEL),
    ("Alternative_Providers_Identified", 15, ["Yes", "No", "Partial"]),
]
```

**Location:** Dashboard sheet formulas

```python
# ADD: Regulatory summary metrics
regulatory_metrics = [
    ("CLOUD Act Exposure (Potential)", '=COUNTIF(Cloud_Service_Inventory!XX:XX,"Potential Exposure*")'),
    ("DORA In-Scope Services", '=COUNTIF(Cloud_Service_Inventory!XX:XX,"Yes")'),
    ("NIS2 In-Scope Services", '=COUNTIF(Cloud_Service_Inventory!XX:XX,"Yes")'),
    ("High-Risk AI Systems", '=COUNTIF(Cloud_Service_Inventory!XX:XX,"High Risk")'),
    ("Critical Concentration Risk", '=COUNTIF(Cloud_Service_Inventory!XX:XX,"Critical*")'),
]
```

### 2.3 Validator Updates

Add to validation spec for 5.23.1:

```python
REGULATORY_COLUMNS_523_1 = [
    "Provider_HQ_Jurisdiction",
    "CLOUD_Act_Exposure", 
    "Data_Processing_Locations",
    "EU_Data_Boundary_Commitment",
    "DORA_In_Scope",
    "NIS2_In_Scope",
    "AI_System_Classification",
    "Concentration_Risk_Level",
    "Alternative_Providers_Identified"
]
```

---

## 3. Workbook 5.23.2 — Vendor Due Diligence & Contracts

### 3.1 Spec Updates (ISMS-IMP-A.5.23.2)

**Add new sheet: Jurisdictional_Risk_Assessment**

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Assessment_ID | 15 | Text | Auto: JRA-001 |
| B | Cloud_Service_Name | 25 | Dropdown | From Inventory |
| C | Provider_Name | 25 | Text | |
| D | Provider_HQ_Country | 20 | Dropdown | Country list |
| E | Provider_HQ_Jurisdiction | 20 | Dropdown | PROVIDER_HQ_JURISDICTION |
| F | US_Parent_Company | 15 | Dropdown | Yes/No/Unknown |
| G | CLOUD_Act_Applicability | 20 | Dropdown | CLOUD_ACT_EXPOSURE |
| H | Data_Locations | 25 | Text | |
| I | EU_Data_Boundary_Available | 15 | Dropdown | Yes/No/Planned |
| J | Customer_Managed_Keys | 15 | Dropdown | Yes/No/Optional |
| K | Provider_Legal_Challenge_Commitment | 15 | Dropdown | Yes/No/Partial/Unknown |
| L | Adequacy_Decision_Status | 20 | Text | |
| M | Transfer_Mechanism | 20 | Dropdown | SCCs/BCRs/Adequacy/None |
| N | Risk_Level | 15 | Dropdown | Low/Medium/High/Critical |
| O | Risk_Accepted_By | 20 | Text | |
| P | Risk_Acceptance_Date | 15 | Date | |
| Q | Compensating_Controls | 30 | Text | |
| R | Review_Date | 15 | Date | |
| S | Evidence_Reference | 25 | Text | EV-JRA-XXX |
| T | Notes | 30 | Text | |

**Add to existing Evaluation_Criteria sheet:**

New rows for evaluation checklist:

| Criteria_ID | Category | Requirement |
|-------------|----------|-------------|
| EVAL-REG-01 | Regulatory | Provider discloses HQ jurisdiction and legal entity structure |
| EVAL-REG-02 | Regulatory | Provider discloses all data processing locations |
| EVAL-REG-03 | Regulatory | Provider offers EU Data Boundary or regional commitment |
| EVAL-REG-04 | Regulatory | Provider supports customer-managed encryption keys |
| EVAL-REG-05 | Regulatory | Provider commits to challenge government data requests |
| EVAL-REG-06 | Regulatory | Provider discloses sub-processor jurisdictions |
| EVAL-AI-01 | AI Act | AI system risk classification documented |
| EVAL-AI-02 | AI Act | High-risk AI system has conformity assessment |
| EVAL-AI-03 | AI Act | AI transparency requirements met |

**Add to existing Contract_Review sheet:**

New rows for DORA/NIS2 contract clauses:

| Clause_ID | Category | Requirement | DORA_Mandatory | NIS2_Mandatory |
|-----------|----------|-------------|----------------|----------------|
| CON-DORA-01 | DORA Art.30 | Clear service descriptions | Yes | No |
| CON-DORA-02 | DORA Art.30 | Data processing locations specified | Yes | Yes |
| CON-DORA-03 | DORA Art.30 | Subcontracting conditions | Yes | Yes |
| CON-DORA-04 | DORA Art.30 | Full access and audit rights | Yes | No |
| CON-DORA-05 | DORA Art.30 | Cooperation with regulators | Yes | Yes |
| CON-DORA-06 | DORA Art.30 | Exit strategy provisions | Yes | No |
| CON-DORA-07 | DORA Art.30 | Termination rights | Yes | No |
| CON-NIS2-01 | NIS2 | Supply chain security requirements | No | Yes |
| CON-NIS2-02 | NIS2 | Incident notification ≤24h | No | Yes |
| CON-NIS2-03 | NIS2 | Vulnerability handling | No | Yes |

### 3.2 Generator Updates (generate_a523_2_vendor_dd.py)

**ADD:** New sheet function `create_jurisdictional_risk_sheet()`

**ADD:** New dropdown lists (as per Section 1.1)

**MODIFY:** `create_evaluation_criteria_sheet()` — add EVAL-REG and EVAL-AI rows

**MODIFY:** `create_contract_review_sheet()` — add DORA/NIS2 clause rows

### 3.3 Validator Updates

Add to validation spec for 5.23.2:

```python
REQUIRED_SHEETS_523_2 = [
    # ... existing sheets ...
    "Jurisdictional_Risk_Assessment"  # NEW
]

REGULATORY_EVAL_IDS = [
    "EVAL-REG-01", "EVAL-REG-02", "EVAL-REG-03", 
    "EVAL-REG-04", "EVAL-REG-05", "EVAL-REG-06",
    "EVAL-AI-01", "EVAL-AI-02", "EVAL-AI-03"
]

DORA_CONTRACT_CLAUSES = [
    "CON-DORA-01", "CON-DORA-02", "CON-DORA-03", "CON-DORA-04",
    "CON-DORA-05", "CON-DORA-06", "CON-DORA-07"
]

NIS2_CONTRACT_CLAUSES = [
    "CON-NIS2-01", "CON-NIS2-02", "CON-NIS2-03"
]
```

---

## 4. Workbook 5.23.3 — Secure Configuration & Deployment

### 4.1 Spec Updates (ISMS-IMP-A.5.23.3)

**Minimal changes — add to existing Configuration_Checklist sheet:**

New rows:

| Config_ID | Category | Requirement |
|-----------|----------|-------------|
| CFG-DATA-LOC-01 | Data Residency | Data-at-rest location verified and documented |
| CFG-DATA-LOC-02 | Data Residency | Data-in-transit routing verified (no unexpected countries) |
| CFG-DATA-LOC-03 | Data Residency | Backup/DR location verified and documented |
| CFG-KEY-01 | Key Management | Customer-managed keys implemented (if required) |
| CFG-KEY-02 | Key Management | Key storage location verified (jurisdiction) |

### 4.2 Generator Updates (generate_a523_3_secure_config.py)

**MODIFY:** `create_configuration_checklist_sheet()` — add 5 new rows

### 4.3 Validator Updates

Add to validation spec for 5.23.3:

```python
DATA_RESIDENCY_CONFIG_IDS = [
    "CFG-DATA-LOC-01", "CFG-DATA-LOC-02", "CFG-DATA-LOC-03",
    "CFG-KEY-01", "CFG-KEY-02"
]
```

---

## 5. Workbook 5.23.4 — Ongoing Governance & Risk Management

### 5.1 Spec Updates (ISMS-IMP-A.5.23.4)

**MODIFY: Incident_Register sheet — update Notification_Deadline column validation:**

```python
INCIDENT_NOTIFICATION_DEADLINES = [
    "Immediate (within 1 hour)",
    "Within 24 hours (NIS2 early warning)",
    "Within 24 hours (standard)",
    "Within 48 hours",
    "Within 72 hours (GDPR)",
    "Per Contract SLA",
    "Not Applicable"
]
```

**Add explanatory row in Instructions:**

```
NIS2 INCIDENT NOTIFICATION REQUIREMENTS

If your organization is subject to NIS2:
- Early warning to CSIRT: Within 24 hours of becoming aware
- Incident notification: Within 72 hours with assessment
- Final report: Within 1 month

Select "Within 24 hours (NIS2 early warning)" for initial notification requirement.
```

**MODIFY: Change_Register sheet — add DORA change notification field:**

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| NEW-1 | DORA_Notification_Required | 15 | Dropdown | Yes/No/N/A |
| NEW-2 | DORA_Notification_Date | 15 | Date | |
| NEW-3 | DORA_30_Day_Compliance | 15 | Dropdown | Compliant/Non-Compliant/N/A |

**Add explanatory row in Instructions:**

```
DORA CHANGE NOTIFICATION REQUIREMENTS

If using critical ICT third-party providers under DORA:
- Provider must notify of planned changes affecting security
- Minimum 30 days advance notice required
- Track compliance in DORA_30_Day_Compliance column
```

**ADD: New sheet Concentration_Risk_Assessment**

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Assessment_ID | 15 | Text | Auto: CRA-001 |
| B | Assessment_Date | 15 | Date | |
| C | Provider_Name | 25 | Text | |
| D | Services_Count | 10 | Number | |
| E | Critical_Services_Count | 10 | Number | |
| F | Data_Volume_Percentage | 15 | Percentage | |
| G | Business_Process_Dependency | 20 | Dropdown | Low/Medium/High/Critical |
| H | Alternative_Providers_Exist | 15 | Dropdown | Yes/Limited/No |
| I | Migration_Feasibility | 15 | Dropdown | Easy/Moderate/Difficult/Impractical |
| J | Migration_Timeframe_Estimate | 15 | Dropdown | <1 month/1-3 months/3-6 months/6-12 months/>12 months |
| K | Concentration_Risk_Level | 18 | Dropdown | CONCENTRATION_RISK_LEVEL |
| L | Risk_Mitigation_Strategy | 30 | Text | |
| M | DORA_Compliant | 15 | Dropdown | Yes/No/N/A |
| N | Review_Frequency | 15 | Dropdown | Quarterly/Semi-Annual/Annual |
| O | Next_Review_Date | 15 | Date | |
| P | Evidence_Reference | 25 | Text | EV-CRA-XXX |
| Q | Notes | 30 | Text | |

### 5.2 Generator Updates (generate_a523_4_governance.py)

**ADD:** New function `create_concentration_risk_sheet()`

**MODIFY:** `create_incident_register_sheet()` — update deadline dropdown

**MODIFY:** `create_change_register_sheet()` — add DORA columns

**ADD:** Dashboard metrics for concentration risk

### 5.3 Validator Updates

Add to validation spec for 5.23.4:

```python
REQUIRED_SHEETS_523_4 = [
    # ... existing sheets ...
    "Concentration_Risk_Assessment"  # NEW
]

DORA_CHANGE_COLUMNS = [
    "DORA_Notification_Required",
    "DORA_Notification_Date",
    "DORA_30_Day_Compliance"
]

NIS2_INCIDENT_DEADLINES = [
    "Within 24 hours (NIS2 early warning)"
]
```

---

## 6. Workbook 5.23.5 — Compliance Monitoring & Exit Planning

### 6.1 Spec Updates (ISMS-IMP-A.5.23.5)

**MODIFY: Exit_Strategy sheet — add DORA-specific fields:**

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| NEW-1 | DORA_Exit_Plan_Required | 15 | Dropdown | Yes/No |
| NEW-2 | DORA_Exit_Plan_Documented | 15 | Dropdown | Yes/No/In Progress |
| NEW-3 | DORA_Exit_Plan_Tested | 15 | Dropdown | Yes/No/Planned |
| NEW-4 | DORA_Exit_Test_Date | 15 | Date | |
| NEW-5 | Transition_Period_Adequate | 15 | Dropdown | Yes/No/Under Review |

**Add to Instructions:**

```
DORA EXIT STRATEGY REQUIREMENTS

Financial entities under DORA must have documented exit strategies for critical
ICT third-party providers including:
- Exit plans that are comprehensive and documented
- Tested periodically to ensure feasibility
- Adequate transition periods to alternative solutions
- No undue dependence on single providers

Complete DORA fields for all critical/important cloud services.
```

**ADD: New sheet Regulatory_Compliance_Matrix**

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Cloud_Service_Name | 25 | Dropdown | From Inventory |
| B | DORA_Applicable | 12 | Dropdown | Yes/No |
| C | DORA_Art30_Compliant | 15 | Dropdown | Yes/No/Partial/N/A |
| D | DORA_Exit_Strategy | 15 | Dropdown | Yes/No/In Progress/N/A |
| E | DORA_Concentration_Assessed | 15 | Dropdown | Yes/No/N/A |
| F | NIS2_Applicable | 12 | Dropdown | Yes/No |
| G | NIS2_Supply_Chain_Compliant | 15 | Dropdown | Yes/No/Partial/N/A |
| H | NIS2_Incident_Process | 15 | Dropdown | Yes/No/N/A |
| I | AI_Act_Applicable | 12 | Dropdown | Yes/No |
| J | AI_Risk_Classification | 18 | Dropdown | AI_RISK_CLASSIFICATION |
| K | AI_Conformity_Status | 15 | Dropdown | Compliant/Non-Compliant/In Progress/N/A |
| L | CLOUD_Act_Assessed | 15 | Dropdown | Yes/No |
| M | CLOUD_Act_Risk_Level | 15 | Dropdown | Low/Medium/High/N/A |
| N | Overall_Regulatory_Status | 15 | Dropdown | Compliant/Gaps Identified/Non-Compliant |
| O | Gap_Summary | 30 | Text | |
| P | Remediation_Plan | 30 | Text | |
| Q | Target_Compliance_Date | 15 | Date | |
| R | Evidence_Reference | 25 | Text | EV-REG-XXX |

### 6.2 Generator Updates (generate_a523_5_compliance.py)

**ADD:** New function `create_regulatory_compliance_matrix_sheet()`

**MODIFY:** `create_exit_strategy_sheet()` — add DORA columns

**ADD:** Dashboard metrics:

```python
regulatory_dashboard_metrics = [
    ("Services with DORA gaps", '=COUNTIF(Regulatory_Compliance_Matrix!C:C,"No")+COUNTIF(Regulatory_Compliance_Matrix!C:C,"Partial")'),
    ("Services with NIS2 gaps", '=COUNTIF(Regulatory_Compliance_Matrix!G:G,"No")+COUNTIF(Regulatory_Compliance_Matrix!G:G,"Partial")'),
    ("High-Risk AI Systems", '=COUNTIF(Regulatory_Compliance_Matrix!J:J,"High Risk")'),
    ("CLOUD Act High Exposure", '=COUNTIF(Regulatory_Compliance_Matrix!M:M,"High")'),
    ("Overall Gaps Identified", '=COUNTIF(Regulatory_Compliance_Matrix!N:N,"Gaps Identified")'),
]
```

### 6.3 Validator Updates

Add to validation spec for 5.23.5:

```python
REQUIRED_SHEETS_523_5 = [
    # ... existing sheets ...
    "Regulatory_Compliance_Matrix"  # NEW
]

DORA_EXIT_COLUMNS = [
    "DORA_Exit_Plan_Required",
    "DORA_Exit_Plan_Documented",
    "DORA_Exit_Plan_Tested",
    "DORA_Exit_Test_Date",
    "Transition_Period_Adequate"
]

REGULATORY_MATRIX_COLUMNS = [
    "DORA_Applicable", "DORA_Art30_Compliant", "DORA_Exit_Strategy",
    "NIS2_Applicable", "NIS2_Supply_Chain_Compliant",
    "AI_Act_Applicable", "AI_Risk_Classification",
    "CLOUD_Act_Assessed", "CLOUD_Act_Risk_Level",
    "Overall_Regulatory_Status"
]
```

---

## 7. Merged Validator Updates (excel_sanity_check_a523.py)

### 7.1 New Validation Functions

```python
def validate_regulatory_dropdowns(ws, workbook_type):
    """Validate regulatory-specific dropdown values"""
    # Check PROVIDER_HQ_JURISDICTION values
    # Check CLOUD_ACT_EXPOSURE values
    # Check AI_RISK_CLASSIFICATION values
    # Check CONCENTRATION_RISK_LEVEL values

def validate_dora_compliance(ws, workbook_type):
    """For DORA in-scope services, verify required fields completed"""
    # If DORA_In_Scope == "Yes", check DORA-specific fields populated

def validate_nis2_compliance(ws, workbook_type):
    """For NIS2 in-scope services, verify incident notification setup"""
    # If NIS2_In_Scope == "Yes", check incident deadlines appropriate

def validate_concentration_risk(ws):
    """Validate concentration risk assessment completeness"""
    # Check Critical services have concentration assessment
```

### 7.2 Updated Workbook Specs

```python
WORKBOOK_SPECS = {
    "5.23.1": {
        "required_sheets": [..., "Cloud_Service_Inventory"],
        "regulatory_columns": REGULATORY_COLUMNS_523_1,  # NEW
    },
    "5.23.2": {
        "required_sheets": [..., "Jurisdictional_Risk_Assessment"],  # NEW SHEET
        "regulatory_eval_ids": REGULATORY_EVAL_IDS,  # NEW
    },
    # ... etc
}
```

---

## 8. Execution Checklist

### Phase 1: Update Specs (Markdown)
- [ ] Update ISMS-IMP-A.5.23.1 spec
- [ ] Update ISMS-IMP-A.5.23.2 spec
- [ ] Update ISMS-IMP-A.5.23.3 spec
- [ ] Update ISMS-IMP-A.5.23.4 spec
- [ ] Update ISMS-IMP-A.5.23.5 spec

### Phase 2: Update Generators (Python)
- [ ] Add global dropdown lists to all generators
- [ ] Update generate_a523_1_inventory.py
- [ ] Update generate_a523_2_vendor_dd.py
- [ ] Update generate_a523_3_secure_config.py
- [ ] Update generate_a523_4_governance.py
- [ ] Update generate_a523_5_compliance.py

### Phase 3: Update Validator
- [ ] Add new validation functions
- [ ] Update workbook specs
- [ ] Test against sample workbooks

### Phase 4: Version Control
- [ ] Mark all outputs as v1.1
- [ ] Update version history in each spec
- [ ] Document changes in changelog

---

## 9. Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author Name] | Initial regulatory update specification |

---

**END OF SPECIFICATION**

*"Measure twice, cut once — especially when updating 5 generators."*