**ISMS-IMP-A.8.9.1**
**Assessment Specification with User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.9: Configuration Management

**Document ID**: ISMS-IMP-A.8.9.1  
**Title**: Baseline Configuration Assessment Specification  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Configuration Manager  
**Status**: Draft  

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.9.1 |
| **Version** | 1.0 |
| **Assessment Area** | Baseline Configuration Management - Asset Inventory, Baseline Documentation, Golden Images, Approvals |
| **Related Policy** | ISMS-POL-A.8.9, Section 2.2 (Baseline Configuration Management) |
| **Purpose** | Assess establishment, documentation, approval, and maintenance of configuration baselines across all asset types to demonstrate ISO 27001:2022 Control A.8.9 compliance |
| **Target Audience** | Configuration Manager, System Administrators, Asset Managers, Security Engineers, IT Operations, Compliance Officers, Auditors |
| **Assessment Type** | Technical & Operational |
| **Review Cycle** | Quarterly or After Major Infrastructure Changes |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Baseline Configuration assessment workbook | ISMS Implementation Team |

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

This assessment evaluates the establishment, documentation, approval, and maintenance of configuration baselines across [Organization]'s information assets. The assessment provides objective evidence of compliance with ISO 27001:2022 Control A.8.9 baseline configuration requirements and supports audit verification of configuration management maturity.

**Implementer Perspective**: This workbook provides a systematic framework for documenting which assets have defined baselines, tracking baseline approval status, assessing documentation quality, and identifying coverage gaps requiring remediation.

**Auditor Perspective**: This assessment generates quantitative metrics (baseline coverage percentage, approval compliance rates, documentation quality scores) that demonstrate [Organization]'s capability to establish and maintain configuration baselines. Evidence collected supports verification of control implementation effectiveness.

## Assessment Scope

This assessment addresses the baseline configuration domain of Control A.8.9, specifically:

**In Scope**:

- Asset inventory completeness and accuracy (foundation for baseline management)
- Configuration baseline definition and documentation for all asset types
- Baseline approval and authorization workflows
- Baseline repository management and version control
- Documentation quality assessment (completeness, accuracy, maintainability)
- Authorized deviations from baselines (with business justification)
- Coverage analysis by asset type and criticality level


**Out of Scope** (covered in other assessments):

- Configuration change management processes (see ISMS-IMP-A.8.9.2)
- Configuration drift detection and monitoring (see ISMS-IMP-A.8.9.3)
- Security hardening compliance verification (see ISMS-IMP-A.8.9.4)
- Operational changes to configurations (change control domain)


## Control Alignment

This assessment implements requirements from:

- **ISMS-POL-A.8.9, Section 2.2**: Baseline Configuration Requirements (complete section)
- **ISMS-CTX-A.8.9, Part 1**: Configuration Standards by Asset Type (reference annexes)
- **ISO 27001:2022 A.8.9**: Configuration management control requirements
- **Related Controls**: A.5.9 (Inventory of Information and Other Associated Assets), A.8.19 (Installation of Software on Operational Systems)


---

# PART I: USER COMPLETION GUIDE
**Audience:** Security assessors, Control owners, Compliance officers

---

# Assessment Scope Definition

## Asset Types Covered

This assessment applies to all asset types within [Organization]'s asset inventory that require configuration management. The 43-type asset taxonomy organizes assets into six major categories:

**Infrastructure Assets** (12 types):

- Physical Servers, Virtual Machines (VMs), Hypervisors
- Network Switches, Routers, Firewalls, Load Balancers
- Storage Arrays (SAN/NAS), Backup Appliances
- UPS/Power Distribution, Environmental Controls (HVAC)
- Physical Security Systems


**Endpoint Assets** (6 types):

- Desktop Computers, Laptop Computers
- Mobile Phones, Tablets
- Thin Clients, Kiosks/Point-of-Sale


**Network Services** (7 types):

- DNS Servers, DHCP Servers, NTP Servers
- Proxy Servers, VPN Gateways
- Wireless Access Points, Network Management Systems


**Application Assets** (8 types):

- Enterprise Applications, Web Applications, Database Systems
- Middleware, APIs/Web Services
- Custom Developed Applications, Commercial Off-the-Shelf (COTS)
- Open Source Software


**Cloud Assets** (5 types):

- IaaS Resources (VMs, Storage), PaaS Services, SaaS Applications
- Cloud-Native Applications, Serverless Functions


**IoT/OT Assets** (5 types):

- IoT Devices, Industrial Control Systems (ICS), SCADA Systems
- Building Management Systems (BMS), Medical Devices


## Criticality Levels

Assets are classified by criticality to prioritize baseline implementation:

| Criticality | Definition | Baseline Requirement | Target Coverage |
|-------------|------------|---------------------|-----------------|
| **Critical** | Supports critical business processes; failure causes severe impact | Mandatory, comprehensive baseline required | ≥95% |
| **High** | Supports important functions; failure causes significant impact | Mandatory, detailed baseline required | ≥90% |
| **Medium** | Supports standard operations; failure causes moderate impact | Recommended, standard baseline | ≥80% |
| **Low** | Supports non-critical functions; failure causes minimal impact | Optional, basic baseline | ≥60% |

**Note**: Criticality is determined during asset classification (see A.5.9 Inventory control) and reflects business impact of asset unavailability or compromise.

## Exclusions and Exceptions

The following asset scenarios may be excluded from baseline requirements with appropriate justification:

**Valid Exclusions**:

- Assets scheduled for decommissioning within 90 days (document decommission date)
- Development/test environments with no production data (document environment classification)
- Temporary assets (duration <30 days) with no access to sensitive information
- Assets with vendor-managed configurations where baseline access is contractually restricted


**Important**: All exclusions must be documented in the Deviation Register sheet with business justification and approval. Exclusions are reviewed during assessment refresh cycles.

---

# Assessment Methodology

## Assessment Workflow

**Three-Tier Approval Process**:

1. **Preparer** (System Administrators, Asset Owners):

   - Complete asset inventory
   - Document baseline status for assigned assets
   - Assess documentation quality
   - Collect supporting evidence
   - Timeline: 2-3 weeks depending on asset count


2. **Reviewer** (Configuration Manager, Team Leads):

   - Verify completeness of documented information
   - Validate baseline repository references
   - Review documentation quality assessments
   - Identify gaps and recommend remediation
   - Timeline: 1 week


3. **Approver** (IT Manager, CISO):

   - Review overall compliance metrics
   - Approve assessment findings
   - Authorize remediation priorities
   - Sign off on assessment completion
   - Timeline: 3-5 business days


## Data Collection Approach

**Asset Inventory Sheet**: Populated from existing asset inventory (A.5.9) or manually compiled if no CMDB exists. Each asset requires unique identifier, type classification, and criticality assignment.

**Baseline Repository Sheet**: Documents each distinct configuration baseline maintained by [Organization]. A baseline may apply to multiple assets (e.g., "Windows Server 2022 Standard Build" applies to all Windows 2022 servers).

**Coverage Matrix Sheet**: Auto-calculates coverage statistics by asset type. Used to identify which asset categories have insufficient baseline coverage.

**Approval Tracking Sheet**: Records baseline approval status through governance workflow. Links to specific approval artifacts (meeting minutes, email approvals, change requests).

**Documentation Assessment Sheet**: Evaluates quality of baseline documentation against criteria: completeness (all configuration elements documented), accuracy (documentation matches actual configuration), maintainability (documentation is updateable and accessible).

**Version Control Sheet**: Tracks baseline versions over time. When baselines are updated through change control (see ISMS-IMP-A.8.9.2), new versions are recorded here.

**Deviation Register Sheet**: Documents authorized deviations from standard baselines. Example: Server X requires non-standard configuration due to legacy application compatibility (approved deviation with business justification).

## Assessment Frequency

**Initial Assessment**: Complete baseline configuration assessment within 90 days of ISMS implementation for A.8.9.

**Ongoing Assessment**: 

- **Quarterly refresh** for Critical and High assets (every 3 months)
- **Semi-annual refresh** for Medium and Low assets (every 6 months)
- **Ad-hoc assessment** when significant infrastructure changes occur (data center migration, cloud transformation, major application deployment)


**Continuous Updates**: Asset inventory and baseline repository should be updated in real-time as changes occur through change control processes. Formal assessment consolidates and validates this continuous data.

---

# Workbook Structure Overview

**Generated Workbook Name**: `ISMS_A_8_9_1_Baseline_Configuration_Assessment_YYYYMMDD.xlsx`

**Total Sheets**: 11

| Sheet # | Sheet Name | Purpose | Row Count |
|---------|------------|---------|-----------|
| 1 | Instructions | Usage guidance, roles, workflow, legend | N/A |
| 2 | Asset_Inventory | All assets requiring baseline management | 100 data rows |
| 3 | Baseline_Repository | Documented configuration baselines | 50 data rows |
| 4 | Baseline_Coverage_Matrix | Coverage analysis by asset type | 43 data rows (one per asset type) |
| 5 | Approval_Tracking | Baseline approval status and workflow | 50 data rows |
| 6 | Documentation_Assessment | Quality evaluation of baseline docs | 30 data rows |
| 7 | Version_Control | Baseline version history | 50 data rows |
| 8 | Deviation_Register | Authorized deviations from baselines | 50 data rows |
| 9 | Metrics_Summary | Auto-calculated compliance metrics | N/A (formulas) |
| 10 | Evidence_Register | Supporting evidence and documentation links | 100 data rows |
| 11 | Approval_Sign_Off | Three-tier approval signatures | N/A (3 rows) |

**Sheet Relationship Flow**:
```
Asset_Inventory → (asset list) → Baseline_Coverage_Matrix
                                        ↓
Baseline_Repository → (baseline definitions) → Approval_Tracking
                                                       ↓
Documentation_Assessment → (quality scores) → Metrics_Summary
                                                       ↓
Version_Control → (history tracking) ← Deviation_Register
                                                       ↓
Evidence_Register → (audit trail) → Approval_Sign_Off
```

---

# Detailed Sheet Specifications

## Sheet 1: Instructions

**Purpose**: Provides comprehensive guidance on how to use the assessment workbook, defines roles and responsibilities, explains the approval workflow, and includes a legend for status values and color coding.

**Content Structure** (not row-based):

- Assessment overview and objectives
- Who should complete each sheet
- Step-by-step completion instructions
- Three-tier approval workflow diagram
- Status value definitions and color legend
- Common questions and troubleshooting
- Contact information for Configuration Manager


**Formatting**:

- Title section: Bold, 16pt, dark blue background (003366)
- Section headers: Bold, 14pt, light blue background (4472C4)
- Body text: Regular, 11pt Calibri
- Color legend showing: Green (Compliant), Yellow (Partial/In Progress), Red (Non-Compliant/Not Started), Gray (N/A)


**No Data Entry**: This is a read-only informational sheet.

---

## Sheet 2: Asset_Inventory

**Purpose**: Comprehensive list of all information assets within assessment scope that require configuration baseline management.

**Column Structure**:

| Column | Header | Data Type | Validation | Description |
|--------|--------|-----------|------------|-------------|
| A | Asset ID | Text | Free text | Unique asset identifier from CMDB or local tracking system |
| B | Asset Name | Text | Free text | Descriptive name of asset (e.g., "WebServer-Prod-01") |
| C | Asset Type | Text | Dropdown (43 types) | Classification from 43-type taxonomy (see Section 2.1) |
| D | Asset Category | Text | Auto-filled formula | Major category derived from Asset Type (Infrastructure/Endpoint/Network/App/Cloud/IoT) |
| E | Criticality | Text | Dropdown | Critical, High, Medium, Low |
| F | Owner | Text | Free text | Name of person/team responsible for asset |
| G | Location | Text | Free text | Physical location, data center, cloud region, or "Virtual" |
| H | Baseline Status | Text | Dropdown | Defined, In Progress, Not Started, N/A |
| I | Baseline Reference | Text | Free text | Link or reference to baseline in Baseline_Repository sheet |
| J | Last Reviewed Date | Date | Date format | Date baseline was last reviewed or updated |
| K | Next Review Due | Date | Formula | Auto-calculated based on criticality (Critical: +90 days, High: +90 days, Medium: +180 days, Low: +180 days) |
| L | Compliance Status | Text | Formula | Auto: "Compliant" if Baseline Status="Defined", else "Non-Compliant" |
| M | Notes | Text | Free text | Additional context, special considerations, or issues |

**Row Allocation**: 100 data rows (Row 3 to Row 102)

**Freeze Panes**: B3 (Column headers and Asset ID always visible during horizontal/vertical scrolling)

**Data Validations**:

- Column C (Asset Type): Dropdown list with all 43 asset types from taxonomy
  - List source: `{43-type list - too long for inline, stored in hidden sheet "Lookup_Tables"}`
  - Allow blank: No (required field)
  - Error alert: "Please select a valid asset type from the dropdown"

- Column E (Criticality): Dropdown list
  - Values: "Critical, High, Medium, Low"
  - Allow blank: No (required field)
  - Error alert: "Please select criticality level"

- Column H (Baseline Status): Dropdown list
  - Values: "Defined, In Progress, Not Started, N/A"
  - Allow blank: No (required field)
  - Error alert: "Please select baseline status"

- Column J (Last Reviewed Date): Date format DD.MM.YYYY
  - Allow blank: Yes (may be blank if never reviewed)


**Formulas**:

- Column D (Asset Category): `=IF(C3="","",VLOOKUP(C3,Lookup_Tables!$A$2:$B$44,2,FALSE))`
  - Explanation: Auto-populates major category based on Asset Type selection

- Column K (Next Review Due): 

```
  =IF(J3="","",IF(E3="Critical",J3+90,IF(E3="High",J3+90,IF(E3="Medium",J3+180,J3+180))))
```

  - Explanation: Calculates next review date based on criticality (Critical/High: 90 days, Medium/Low: 180 days)

- Column L (Compliance Status):

```
  =IF(H3="Defined","Compliant",IF(H3="N/A","Excluded","Non-Compliant"))
```

  - Explanation: Auto-determines compliance based on baseline status


**Conditional Formatting**:

- Column H (Baseline Status):
  - "Defined" → Green fill (C6EFCE)
  - "In Progress" → Yellow fill (FFEB9C)
  - "Not Started" → Red fill (FFC7CE)
  - "N/A" → Gray fill (D9D9D9)

- Column L (Compliance Status):
  - "Compliant" → Green fill (C6EFCE), bold text
  - "Non-Compliant" → Red fill (FFC7CE), bold text
  - "Excluded" → Gray fill (D9D9D9)

- Column K (Next Review Due):
  - If date < TODAY() AND Baseline Status ≠ "N/A" → Red fill (overdue review)
  - If date between TODAY() and TODAY()+30 → Yellow fill (due soon)


**Special Features**:

- Row 2: Column headers with light gray background (D9D9D9), bold text, centered alignment
- Row 1: Title "Asset Inventory - Baseline Configuration Assessment" spanning A1:M1, merged, dark blue background
- Protected cells: Columns D, K, L (formula cells) are locked to prevent accidental modification
- Hidden sheet: "Lookup_Tables" contains 43-type asset taxonomy for dropdown validation


**Usage Notes**:

- Preparer: Complete columns A-C, E-G, H-J, M for each asset
- Auto-populated: Columns D, K, L calculate automatically
- Start with Critical assets, then High, then Medium/Low
- If "N/A" in Baseline Status, explain in Notes column (M) why baseline is not applicable


---

## Sheet 3: Baseline_Repository

**Purpose**: Catalog of all configuration baselines maintained by [Organization]. Each row represents a distinct baseline that may apply to one or multiple assets.

**Column Structure**:

| Column | Header | Data Type | Validation | Description |
|--------|--------|-----------|------------|-------------|
| A | Baseline ID | Text | Free text | Unique identifier for baseline (e.g., "BL-WIN2022-STD-001") |
| B | Baseline Name | Text | Free text | Descriptive name (e.g., "Windows Server 2022 Standard Build") |
| C | Baseline Version | Text | Free text | Version number (e.g., "2.1", "2024.Q4") |
| D | Applicable Asset Types | Text | Free text | Which asset types use this baseline (comma-separated if multiple) |
| E | Description | Text | Free text | Summary of what this baseline configures |
| F | Approval Status | Text | Dropdown | Approved, Pending Review, Rejected, Draft |
| G | Approved By | Text | Free text | Name/role of person who approved baseline |
| H | Approval Date | Date | Date format | Date baseline was approved |
| I | Last Updated | Date | Date format | Date baseline was last modified |
| J | Documentation Location | Text | Free text | File path, URL, or document management system reference |
| K | Configuration Elements Count | Number | Number (0-999) | Number of configuration items defined in baseline |
| L | Applied to Assets Count | Number | Formula (optional) | Count of assets using this baseline (link to Asset_Inventory) |
| M | Notes | Text | Free text | Additional information, change history summary |

**Row Allocation**: 50 data rows (Row 3 to Row 52)

**Freeze Panes**: B3

**Data Validations**:

- Column F (Approval Status): Dropdown list
  - Values: "Approved, Pending Review, Rejected, Draft"
  - Allow blank: No
  - Error alert: "Please select approval status"

- Column H (Approval Date): Date format DD.MM.YYYY
  - Allow blank: Yes (blank if not yet approved)

- Column I (Last Updated): Date format DD.MM.YYYY
  - Allow blank: No (required field)

- Column K (Configuration Elements Count): Number
  - Whole numbers only, range 0-999
  - Allow blank: Yes


**Formulas**:

- Column L (Applied to Assets Count): *Optional - requires complex COUNTIF across sheets*

```
  =COUNTIF(Asset_Inventory!$I$3:$I$102,A3)
```

  - Explanation: Counts how many assets reference this baseline ID in Asset_Inventory sheet column I
  - Note: This formula may not work if users don't use exact Baseline ID matching


**Conditional Formatting**:

- Column F (Approval Status):
  - "Approved" → Green fill (C6EFCE)
  - "Pending Review" → Yellow fill (FFEB9C)
  - "Rejected" → Red fill (FFC7CE)
  - "Draft" → Light yellow fill (FFFFCC)

- Column H (Approval Date):
  - If blank AND Approval Status = "Approved" → Red fill (data inconsistency)

- Column I (Last Updated):
  - If date > 365 days old → Yellow fill (baseline may need review)


**Special Features**:

- Row 2: Column headers with light gray background, bold, centered
- Row 1: Title "Baseline Repository" spanning A1:M1, merged, dark blue background
- Protected cells: Column L (formula cell) locked if formula is implemented
- Link: Column J could contain hyperlinks to documentation (users can manually add)


**Usage Notes**:

- Preparer: Each distinct configuration baseline gets one row
- A baseline is "approved" when it passes through governance workflow
- Documentation location (Column J) should point to detailed configuration specs
- Configuration Elements Count (Column K) reflects how comprehensive the baseline is (example: Windows baseline with 150 configured items vs. basic baseline with 20 items)


---

## Sheet 4: Baseline_Coverage_Matrix

**Purpose**: Provides statistical analysis of baseline coverage by asset type. Auto-calculates coverage percentages to identify gaps requiring attention. This is a primarily formula-driven sheet.

**Column Structure**:

| Column | Header | Data Type | Validation | Description |
|--------|--------|-----------|------------|-------------|
| A | Asset Type | Text | Pre-filled | All 43 asset types from taxonomy (one row per type) |
| B | Asset Category | Text | Pre-filled | Major category (Infrastructure/Endpoint/Network/App/Cloud/IoT) |
| C | Total Assets | Number | Formula | Count of assets of this type from Asset_Inventory |
| D | Assets with Baselines | Number | Formula | Count of assets where Baseline Status = "Defined" |
| E | Assets In Progress | Number | Formula | Count where Baseline Status = "In Progress" |
| F | Assets Not Started | Number | Formula | Count where Baseline Status = "Not Started" |
| G | Assets N/A | Number | Formula | Count where Baseline Status = "N/A" |
| H | Coverage % | Percentage | Formula | (Assets with Baselines / (Total Assets - Assets N/A)) × 100 |
| I | Critical Assets Count | Number | Formula | Count of Critical assets of this type |
| J | Critical Coverage % | Percentage | Formula | Coverage % for Critical assets only |
| K | Status | Text | Formula | "Compliant", "Partial", "Non-Compliant" based on coverage % |
| L | Gap Analysis | Text | Formula | Descriptive gap statement |

**Row Allocation**: 43 data rows (Row 3 to Row 45) - one row per asset type from taxonomy

**Freeze Panes**: B3

**Pre-filled Data**:

- Column A: All 43 asset types (pre-populated, users do not edit)
- Column B: Corresponding category for each asset type (pre-populated)


**Formulas** (Examples - actual formulas depend on implementation):

- Column C (Total Assets):

```
  =COUNTIF(Asset_Inventory!$C$3:$C$102,A3)
```

  - Explanation: Counts how many assets in Asset_Inventory match this Asset Type

- Column D (Assets with Baselines):

```
  =COUNTIFS(Asset_Inventory!$C$3:$C$102,A3,Asset_Inventory!$H$3:$H$102,"Defined")
```

  - Explanation: Counts assets of this type where Baseline Status = "Defined"

- Column E (Assets In Progress):

```
  =COUNTIFS(Asset_Inventory!$C$3:$C$102,A3,Asset_Inventory!$H$3:$H$102,"In Progress")
```

- Column F (Assets Not Started):

```
  =COUNTIFS(Asset_Inventory!$C$3:$C$102,A3,Asset_Inventory!$H$3:$H$102,"Not Started")
```

- Column G (Assets N/A):

```
  =COUNTIFS(Asset_Inventory!$C$3:$C$102,A3,Asset_Inventory!$H$3:$H$102,"N/A")
```

- Column H (Coverage %):

```
  =IF((C3-G3)=0,0,D3/(C3-G3)*100)
```

  - Explanation: Percentage of non-excluded assets with defined baselines
  - Handles division by zero if no assets or all excluded

- Column I (Critical Assets Count):

```
  =COUNTIFS(Asset_Inventory!$C$3:$C$102,A3,Asset_Inventory!$E$3:$E$102,"Critical")
```

- Column J (Critical Coverage %):

```
  =IF(I3=0,0,COUNTIFS(Asset_Inventory!$C$3:$C$102,A3,Asset_Inventory!$E$3:$E$102,"Critical",Asset_Inventory!$H$3:$H$102,"Defined")/I3*100)
```

  - Explanation: Coverage % specifically for Critical assets

- Column K (Status):

```
  =IF(H3>=90,"Compliant",IF(H3>=60,"Partial","Non-Compliant"))
```

  - Explanation: Status based on coverage thresholds (≥90% = Compliant, 60-89% = Partial, <60% = Non-Compliant)

- Column L (Gap Analysis):

```
  =IF(K3="Compliant","Coverage target met",IF(F3>0,F3&" assets need baselines started","Review in-progress baselines"))
```

  - Explanation: Dynamic text describing the gap


**Conditional Formatting**:

- Column H (Coverage %):
  - ≥90% → Green fill (C6EFCE)
  - 60-89% → Yellow fill (FFEB9C)
  - <60% → Red fill (FFC7CE)

- Column J (Critical Coverage %):
  - ≥95% → Green fill (target for Critical assets)
  - 80-94% → Yellow fill
  - <80% → Red fill

- Column K (Status):
  - "Compliant" → Green text, bold
  - "Partial" → Yellow/orange text, bold
  - "Non-Compliant" → Red text, bold


**Special Features**:

- Row 2: Column headers with light gray background
- Row 1: Title "Baseline Coverage Matrix by Asset Type" spanning A1:L1
- All cells protected (formula-driven sheet, no user input)
- Summary row at bottom (Row 46): Totals across all asset types
  - Column C: =SUM(C3:C45)
  - Column D: =SUM(D3:D45)
  - Column H: =IF(C46-G46=0,0,D46/(C46-G46)*100) [overall coverage]


**Usage Notes**:

- This sheet auto-updates as Asset_Inventory is filled in
- No manual data entry required
- Use this to identify which asset types have poorest baseline coverage
- Focus remediation efforts on rows with "Non-Compliant" status


---

## Sheet 5: Approval_Tracking

**Purpose**: Track the approval workflow status for each configuration baseline through the governance process.

**Column Structure**:

| Column | Header | Data Type | Validation | Description |
|--------|--------|-----------|------------|-------------|
| A | Baseline ID | Text | Free text | Reference to baseline from Baseline_Repository (Column A) |
| B | Baseline Name | Text | Free text | Descriptive name for easy reference |
| C | Submission Date | Date | Date format | Date baseline was submitted for approval |
| D | Approver Name | Text | Free text | Person responsible for approval (role or name) |
| E | Approval Status | Text | Dropdown | Pending Submission, Submitted, Under Review, Approved, Rejected, Revisions Requested |
| F | Approval Date | Date | Date format | Date approval was granted (blank if not yet approved) |
| G | Approval Method | Text | Dropdown | Change Advisory Board, Email Approval, Manager Sign-Off, Governance Committee |
| H | Approval Reference | Text | Free text | Meeting minutes reference, email thread ID, ticket number |
| I | Business Justification | Text | Free text | Why this baseline is needed |
| J | Risk Assessment | Text | Dropdown | Low, Medium, High |
| K | Days Pending | Number | Formula | Days between submission and current date or approval date |
| L | SLA Status | Text | Formula | "Within SLA" (<14 days), "Approaching SLA" (14-21 days), "SLA Breach" (>21 days) |
| M | Next Action | Text | Free text | Required follow-up actions |
| N | Notes | Text | Free text | Additional context |

**Row Allocation**: 50 data rows (Row 3 to Row 52)

**Freeze Panes**: B3

**Data Validations**:

- Column E (Approval Status): Dropdown list
  - Values: "Pending Submission, Submitted, Under Review, Approved, Rejected, Revisions Requested"
  - Allow blank: No

- Column G (Approval Method): Dropdown list
  - Values: "Change Advisory Board, Email Approval, Manager Sign-Off, Governance Committee, Automated Process"
  - Allow blank: Yes (blank until submitted)

- Column J (Risk Assessment): Dropdown list
  - Values: "Low, Medium, High"
  - Allow blank: Yes

- Column C (Submission Date), Column F (Approval Date): Date format DD.MM.YYYY


**Formulas**:

- Column K (Days Pending):

```
  =IF(C3="","",IF(F3="",TODAY()-C3,F3-C3))
```

  - Explanation: If submitted but not approved, calculates days from submission to today. If approved, calculates days from submission to approval.

- Column L (SLA Status):

```
  =IF(K3="","",IF(K3<=14,"Within SLA",IF(K3<=21,"Approaching SLA","SLA Breach")))
```

  - Explanation: Approval SLA is 14 days (customize for [Organization]). Warns if approaching or exceeding SLA.


**Conditional Formatting**:

- Column E (Approval Status):
  - "Approved" → Green fill (C6EFCE)
  - "Under Review" → Yellow fill (FFEB9C)
  - "Rejected" → Red fill (FFC7CE)
  - "Revisions Requested" → Orange fill (FFA500)

- Column L (SLA Status):
  - "Within SLA" → Green text
  - "Approaching SLA" → Yellow/orange text, bold
  - "SLA Breach" → Red text, bold

- Column K (Days Pending):
  - >21 days → Red fill (significant delay)


**Special Features**:

- Row 2: Column headers with light gray background
- Row 1: Title "Baseline Approval Tracking" spanning A1:N1
- Protected cells: Columns K and L (formula cells) locked
- Link to Baseline_Repository: Column A should match Baseline IDs


**Usage Notes**:

- Preparer: Create entry when baseline is submitted for approval
- Update Column E as baseline progresses through approval workflow
- Column H (Approval Reference) is critical for audit trail - document where approval decision is recorded
- If "Revisions Requested", document required changes in Column M (Next Action)
- SLA of 14 days is example; customize for [Organization]'s governance cycle


---

## Sheet 6: Documentation_Assessment

**Purpose**: Evaluate the quality of configuration baseline documentation against defined criteria. This assessment ensures baselines are not just defined, but properly documented for long-term maintainability and audit verification.

**Column Structure**:

| Column | Header | Data Type | Validation | Description |
|--------|--------|-----------|------------|-------------|
| A | Baseline ID | Text | Free text | Reference to baseline from Baseline_Repository |
| B | Baseline Name | Text | Free text | Descriptive name for reference |
| C | Documentation Completeness | Text | Dropdown | Comprehensive, Adequate, Insufficient, Missing |
| D | Completeness Score | Number | Formula | Numeric score: Comprehensive=100, Adequate=75, Insufficient=40, Missing=0 |
| E | Documentation Accuracy | Text | Dropdown | Verified Accurate, Mostly Accurate, Contains Errors, Not Verified |
| F | Accuracy Score | Number | Formula | Numeric score: Verified=100, Mostly=75, Errors=40, Not Verified=0 |
| G | Maintainability | Text | Dropdown | Easy to Update, Moderate Effort, Difficult, Not Maintainable |
| H | Maintainability Score | Number | Formula | Numeric score: Easy=100, Moderate=75, Difficult=40, Not Maintainable=0 |
| I | Accessibility | Text | Dropdown | Highly Accessible, Accessible, Limited Access, Not Accessible |
| J | Accessibility Score | Number | Formula | Numeric score: Highly=100, Accessible=75, Limited=40, Not=0 |
| K | Overall Quality Score | Number | Formula | Average of scores in columns D, F, H, J |
| L | Quality Rating | Text | Formula | Excellent (≥90), Good (75-89), Fair (50-74), Poor (<50) |
| M | Gaps Identified | Text | Free text | Specific documentation gaps or improvement areas |
| N | Remediation Priority | Text | Dropdown | Critical, High, Medium, Low |
| O | Target Completion Date | Date | Date format | When documentation improvements should be completed |

**Row Allocation**: 30 data rows (Row 3 to Row 32)

**Freeze Panes**: B3

**Data Validations**:

- Column C (Documentation Completeness): Dropdown list
  - Values: "Comprehensive, Adequate, Insufficient, Missing"
  - Allow blank: No
  - Comprehensive = All configuration elements documented with detailed specifications
  - Adequate = Core elements documented, minor gaps acceptable
  - Insufficient = Significant gaps in documentation
  - Missing = No meaningful documentation exists

- Column E (Documentation Accuracy): Dropdown list
  - Values: "Verified Accurate, Mostly Accurate, Contains Errors, Not Verified"
  - Allow blank: No

- Column G (Maintainability): Dropdown list
  - Values: "Easy to Update, Moderate Effort, Difficult, Not Maintainable"
  - Allow blank: No

- Column I (Accessibility): Dropdown list
  - Values: "Highly Accessible, Accessible, Limited Access, Not Accessible"
  - Allow blank: No
  - Highly Accessible = Available in central repository, searchable, version controlled
  - Accessible = Available but may require specific access request
  - Limited Access = Only few people can access
  - Not Accessible = Documentation location unknown or access severely restricted

- Column N (Remediation Priority): Dropdown list
  - Values: "Critical, High, Medium, Low"
  - Allow blank: Yes

- Column O (Target Completion Date): Date format DD.MM.YYYY


**Formulas**:

- Column D (Completeness Score):

```
  =IF(C3="Comprehensive",100,IF(C3="Adequate",75,IF(C3="Insufficient",40,0)))
```

- Column F (Accuracy Score):

```
  =IF(E3="Verified Accurate",100,IF(E3="Mostly Accurate",75,IF(E3="Contains Errors",40,0)))
```

- Column H (Maintainability Score):

```
  =IF(G3="Easy to Update",100,IF(G3="Moderate Effort",75,IF(G3="Difficult",40,0)))
```

- Column J (Accessibility Score):

```
  =IF(I3="Highly Accessible",100,IF(I3="Accessible",75,IF(I3="Limited Access",40,0)))
```

- Column K (Overall Quality Score):

```
  =(D3+F3+H3+J3)/4
```

  - Explanation: Average of four quality dimensions

- Column L (Quality Rating):

```
  =IF(K3>=90,"Excellent",IF(K3>=75,"Good",IF(K3>=50,"Fair","Poor")))
```

**Conditional Formatting**:

- Column K (Overall Quality Score):
  - ≥90 → Green fill (C6EFCE)
  - 75-89 → Light green fill
  - 50-74 → Yellow fill (FFEB9C)
  - <50 → Red fill (FFC7CE)

- Column L (Quality Rating):
  - "Excellent" → Dark green text, bold
  - "Good" → Green text
  - "Fair" → Orange text
  - "Poor" → Red text, bold

- Column O (Target Completion Date):
  - If date < TODAY() and Quality Rating = "Poor" or "Fair" → Red fill (overdue)


**Special Features**:

- Row 2: Column headers with light gray background
- Row 1: Title "Baseline Documentation Quality Assessment" spanning A1:O1
- Protected cells: Columns D, F, H, J, K, L (formula cells) locked
- Scoring rubric: Include reference note that explains scoring methodology


**Usage Notes**:

- Reviewer typically completes this assessment (Configuration Manager or designee)
- Quality assessment performed by reviewing actual baseline documentation
- "Verified Accurate" means documentation was compared against actual configured systems and matches
- Remediation Priority should be "Critical" for baselines with Poor quality that apply to Critical assets
- This assessment drives documentation improvement initiatives


---

## Sheet 7: Version_Control

**Purpose**: Track version history of configuration baselines over time. When baselines are updated through change control processes, new versions are recorded here to maintain audit trail and support rollback if needed.

**Column Structure**:

| Column | Header | Data Type | Validation | Description |
|--------|--------|-----------|------------|-------------|
| A | Baseline ID | Text | Free text | Reference to baseline from Baseline_Repository |
| B | Baseline Name | Text | Free text | Descriptive name |
| C | Version Number | Text | Free text | Version identifier (e.g., "1.0", "2.3", "2024.Q1") |
| D | Version Date | Date | Date format | Date this version was created/approved |
| E | Previous Version | Text | Free text | Version number this replaced (blank for initial version) |
| F | Change Type | Text | Dropdown | Initial Release, Minor Update, Major Update, Security Patch, Emergency Change |
| G | Change Summary | Text | Free text | Brief description of what changed in this version |
| H | Change Request Reference | Text | Free text | Reference to change control record (see ISMS-IMP-A.8.9.2) |
| I | Changed By | Text | Free text | Person/team who made the change |
| J | Approved By | Text | Free text | Person who approved this version |
| K | Superseded Date | Date | Date format | Date this version was replaced by newer version (blank if current) |
| L | Status | Text | Formula | "Current" if Superseded Date is blank, "Superseded" if date present |
| M | Assets Affected Count | Number | Free text/Formula | Number of assets using this baseline version |
| N | Documentation Location | Text | Free text | Where this specific version's documentation is stored |

**Row Allocation**: 50 data rows (Row 3 to Row 52)

**Freeze Panes**: B3

**Data Validations**:

- Column F (Change Type): Dropdown list
  - Values: "Initial Release, Minor Update, Major Update, Security Patch, Emergency Change, Rollback"
  - Allow blank: No
  - Initial Release = First version of baseline
  - Minor Update = Small changes, non-breaking (e.g., parameter adjustment)
  - Major Update = Significant changes, may require testing (e.g., new OS version)
  - Security Patch = Security-driven update (urgent)
  - Emergency Change = Unplanned change due to incident
  - Rollback = Reverting to previous version

- Column D (Version Date), Column K (Superseded Date): Date format DD.MM.YYYY


**Formulas**:

- Column L (Status):

```
  =IF(K3="","Current","Superseded")
```

  - Explanation: If Superseded Date is blank, version is still current; otherwise it's been replaced


**Conditional Formatting**:

- Column L (Status):
  - "Current" → Green fill (C6EFCE), bold
  - "Superseded" → Gray fill (D9D9D9)

- Column K (Superseded Date):
  - If blank → Light green background (indicates current version)

- Column F (Change Type):
  - "Emergency Change" → Red text (highlights urgent changes)
  - "Security Patch" → Orange text (security-related)


**Special Features**:

- Row 2: Column headers with light gray background
- Row 1: Title "Baseline Version Control History" spanning A1:N1
- Protected cells: Column L (formula cell) locked
- Sort: Should be sorted by Baseline ID (A) then Version Date (D) descending to show most recent first
- Filter: Enable auto-filter on header row to allow filtering by Baseline ID, Status, Change Type


**Usage Notes**:

- Every time a baseline is updated, a new row is added to this sheet
- Previous version's Superseded Date (Column K) is filled when new version is created
- Change Request Reference (Column H) links to formal change control (see ISMS-IMP-A.8.9.2 assessment)
- For audit purposes, maintain history for at least 3 years
- "Current" versions should match the version in Baseline_Repository sheet
- Multiple baselines can have multiple versions tracked in this sheet (one row per version)


---

## Sheet 8: Deviation_Register

**Purpose**: Document and track authorized deviations from standard configuration baselines. Deviations require business justification and approval, and are regularly reviewed to ensure they remain valid.

**Column Structure**:

| Column | Header | Data Type | Validation | Description |
|--------|--------|-----------|------------|-------------|
| A | Deviation ID | Text | Free text | Unique identifier for deviation (e.g., "DEV-2024-001") |
| B | Asset ID | Text | Free text | Reference to specific asset with deviation |
| C | Asset Name | Text | Free text | Descriptive name of asset |
| D | Baseline ID | Text | Free text | Which baseline this deviates from |
| E | Deviation Type | Text | Dropdown | Configuration Exception, Exclusion from Baseline, Temporary Deviation, Permanent Exception |
| F | Configuration Element | Text | Free text | Specific configuration item that deviates (e.g., "Firewall Rule 502") |
| G | Standard Value | Text | Free text | What the baseline specifies |
| H | Actual Value | Text | Free text | What is actually configured on this asset |
| I | Business Justification | Text | Free text | Why this deviation is necessary |
| J | Risk Assessment | Text | Dropdown | Low, Medium, High, Critical |
| K | Compensating Controls | Text | Free text | Security controls in place to mitigate deviation risk |
| L | Approved By | Text | Free text | Name/role of approver |
| M | Approval Date | Date | Date format | Date deviation was approved |
| N | Review Frequency | Text | Dropdown | Monthly, Quarterly, Semi-Annual, Annual |
| O | Next Review Date | Date | Formula | Auto-calculated based on Approval Date + Review Frequency |
| P | Deviation Status | Text | Dropdown | Active, Under Review, Expired, Revoked, No Longer Needed |
| Q | Expiration Date | Date | Date format | Date deviation authorization expires (if temporary) |
| R | Notes | Text | Free text | Additional context |

**Row Allocation**: 50 data rows (Row 3 to Row 52)

**Freeze Panes**: B3

**Data Validations**:

- Column E (Deviation Type): Dropdown list
  - Values: "Configuration Exception, Exclusion from Baseline, Temporary Deviation, Permanent Exception"
  - Allow blank: No
  - Configuration Exception = Specific config item differs from baseline
  - Exclusion from Baseline = Entire asset excluded from baseline application
  - Temporary Deviation = Short-term deviation (has expiration date)
  - Permanent Exception = Long-term deviation (no expiration, but regularly reviewed)

- Column J (Risk Assessment): Dropdown list
  - Values: "Low, Medium, High, Critical"
  - Allow blank: No

- Column N (Review Frequency): Dropdown list
  - Values: "Monthly, Quarterly, Semi-Annual, Annual"
  - Allow blank: No
  - High/Critical risk deviations should use Monthly or Quarterly

- Column P (Deviation Status): Dropdown list
  - Values: "Active, Under Review, Expired, Revoked, No Longer Needed"
  - Allow blank: No

- Column M (Approval Date), Column Q (Expiration Date): Date format DD.MM.YYYY


**Formulas**:

- Column O (Next Review Date):

```
  =IF(M3="","",IF(N3="Monthly",M3+30,IF(N3="Quarterly",M3+90,IF(N3="Semi-Annual",M3+180,M3+365))))
```

  - Explanation: Calculates next review based on approval date + review frequency


**Conditional Formatting**:

- Column J (Risk Assessment):
  - "Critical" → Dark red fill (C00000), white text, bold
  - "High" → Red fill (FFC7CE)
  - "Medium" → Yellow fill (FFEB9C)
  - "Low" → Light green fill (E2EFDA)

- Column P (Deviation Status):
  - "Active" → Green fill (C6EFCE)
  - "Expired" → Red fill (FFC7CE), bold
  - "Under Review" → Yellow fill (FFEB9C)
  - "Revoked" → Gray fill (D9D9D9)

- Column O (Next Review Date):
  - If date < TODAY() and Status = "Active" → Red fill (overdue review)
  - If date between TODAY() and TODAY()+30 → Yellow fill (review due soon)

- Column Q (Expiration Date):
  - If date < TODAY() and Status = "Active" → Red fill, bold (expired deviation still active - must update status)


**Special Features**:

- Row 2: Column headers with light gray background
- Row 1: Title "Configuration Baseline Deviation Register" spanning A1:R1
- Protected cells: Column O (formula cell) locked
- High-risk deviations (Critical/High) should be highlighted in summary metrics


**Usage Notes**:

- Every deviation from a standard baseline MUST be documented here
- Business Justification (Column I) is critical - auditors will review this
- Compensating Controls (Column K) are mandatory for High/Critical risk deviations
- Temporary Deviations (Column E) must have Expiration Date (Column Q)
- When deviation is no longer needed, update Status to "No Longer Needed" and document in Notes
- Regular review of this register is part of Configuration Manager responsibilities
- Policy reference: ISMS-CTX-A.8.9, Part 3 (Configuration Deviation Procedures)


---

## Sheet 9: Metrics_Summary

**Purpose**: Auto-calculate key compliance metrics and provide executive summary of baseline configuration assessment results. This sheet is formula-driven and requires no manual data entry.

**Content Structure** (Not tabular - dashboard layout):

**Section A: Overall Compliance Metrics** (Rows 3-10)

| Metric | Formula/Value | Target | Status |
|--------|---------------|--------|--------|
| Total Assets in Scope | =COUNTA(Asset_Inventory!A3:A102)-COUNTBLANK(Asset_Inventory!A3:A102) | N/A | [Calculated] |
| Assets with Defined Baselines | =COUNTIF(Asset_Inventory!H3:H102,"Defined") | N/A | [Calculated] |
| Overall Baseline Coverage % | =(Assets with Baselines / Total Assets) × 100 | ≥85% | [Green/Yellow/Red] |
| Critical Asset Coverage % | =COUNTIFS(Asset_Inventory!E3:E102,"Critical",Asset_Inventory!H3:H102,"Defined")/COUNTIF(Asset_Inventory!E3:E102,"Critical")*100 | ≥95% | [Status] |
| High Asset Coverage % | Similar formula for High criticality | ≥90% | [Status] |
| Baselines Pending Approval | =COUNTIF(Approval_Tracking!E3:E52,"Submitted")+COUNTIF(Approval_Tracking!E3:E52,"Under Review") | 0 | [Status] |
| Documentation Quality - Excellent | =COUNTIF(Documentation_Assessment!L3:L32,"Excellent") | Maximize | [Count] |
| Documentation Quality - Poor | =COUNTIF(Documentation_Assessment!L3:L32,"Poor") | 0 | [Count] |
| Active Deviations - High Risk | =COUNTIFS(Deviation_Register!J3:J52,"High",Deviation_Register!P3:P52,"Active")+COUNTIFS(Deviation_Register!J3:J52,"Critical",Deviation_Register!P3:P52,"Active") | <5 | [Status] |

**Section B: Coverage by Asset Category** (Rows 12-20)

| Category | Total Assets | Assets with Baselines | Coverage % | Status |
|----------|--------------|----------------------|------------|--------|
| Infrastructure | =Formula from Coverage_Matrix | =Formula | =Formula | [Status] |
| Endpoint | =Formula | =Formula | =Formula | [Status] |
| Network Services | =Formula | =Formula | =Formula | [Status] |
| Applications | =Formula | =Formula | =Formula | [Status] |
| Cloud | =Formula | =Formula | =Formula | [Status] |
| IoT/OT | =Formula | =Formula | =Formula | [Status] |

**Section C: Top Gaps Requiring Attention** (Rows 22-32)

| Priority | Gap Description | Assets Affected | Remediation Owner | Target Date |
|----------|----------------|-----------------|-------------------|-------------|
| 1 | [Auto-generated from analysis] | [Count] | [TBD] | [TBD] |
| 2 | [Auto-generated] | [Count] | [TBD] | [TBD] |
| ... | ... | ... | ... | ... |

**Section D: Approval Process Health** (Rows 34-40)

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| Average Approval Time (Days) | =AVERAGE(Approval_Tracking!K3:K52) | <14 days | [Status] |
| Baselines Exceeding SLA | =COUNTIF(Approval_Tracking!L3:L52,"SLA Breach") | 0 | [Status] |
| Approval Success Rate | =(Approved / (Approved + Rejected)) × 100 | >90% | [Status] |

**Formatting**:

- Section headers: Bold, 14pt, dark blue background (003366), white text
- Metric labels: Bold, 11pt
- Values: 12pt, conditionally formatted based on status
- Target column: Gray background (D9D9D9)
- Status column: Conditional formatting (Green/Yellow/Red)


**Conditional Formatting**:

- Overall Coverage %:
  - ≥85% → Green fill
  - 70-84% → Yellow fill
  - <70% → Red fill

- Critical/High Asset Coverage:
  - Meets or exceeds target → Green
  - Within 5% of target → Yellow
  - Below target by >5% → Red

- Documentation Quality counts:
  - "Excellent" count → Green text
  - "Poor" count → Red text if >0


**Special Features**:

- All cells protected (formula-driven, no user input)
- Print area defined (fits on 2 pages for executive reporting)
- Page breaks set logically between sections
- Chart/graph area reserved (Rows 42-60) for visual representation if organization wants to add charts


**Usage Notes**:

- This sheet updates automatically as other sheets are populated
- Review this sheet LAST after all other sheets are complete
- Use this sheet for executive reporting and governance meetings
- Red/Yellow status items should be discussed in Approval Sign-Off section
- This feeds into overall compliance dashboard (ISMS-IMP-A.8.9.5)


---

## Sheet 10: Evidence_Register

**Purpose**: Central register of all supporting evidence and documentation that demonstrates baseline configuration implementation. Critical for audit verification and traceability.

**Column Structure**:

| Column | Header | Data Type | Validation | Description |
|--------|--------|-----------|------------|-------------|
| A | Evidence ID | Text | Free text | Unique identifier (e.g., "EVID-A89-001") |
| B | Evidence Type | Text | Dropdown | Screenshot, Configuration File, Scan Report, Approval Record, Meeting Minutes, Email, Document, System Export |
| C | Evidence Description | Text | Free text | Brief description of what this evidence shows |
| D | Related Asset(s) | Text | Free text | Asset ID(s) this evidence relates to (comma-separated if multiple) |
| E | Related Baseline(s) | Text | Free text | Baseline ID(s) this evidence supports |
| F | Evidence Date | Date | Date format | Date evidence was created/captured |
| G | Evidence Location | Text | Free text | File path, URL, document management system reference, physical location |
| H | Evidence Owner | Text | Free text | Person/team responsible for this evidence |
| I | Evidence Classification | Text | Dropdown | Public, Internal, Confidential, Restricted |
| J | Retention Period | Text | Dropdown | 1 Year, 3 Years, 5 Years, 7 Years, Indefinite |
| K | Last Verified Date | Date | Date format | Date evidence was last verified as still valid/accessible |
| L | Verification Status | Text | Dropdown | Verified, Needs Verification, Missing, Outdated |
| M | Linked Control Requirement | Text | Free text | Which POL section this evidence supports (e.g., "POL-S2.1-2.1.2") |
| N | Notes | Text | Free text | Additional context |

**Row Allocation**: 100 data rows (Row 3 to Row 102)

**Freeze Panes**: B3

**Data Validations**:

- Column B (Evidence Type): Dropdown list
  - Values: "Screenshot, Configuration File, Scan Report, Approval Record, Meeting Minutes, Email, Document, System Export, Video Recording, Audit Log, Other"
  - Allow blank: No

- Column I (Evidence Classification): Dropdown list
  - Values: "Public, Internal, Confidential, Restricted"
  - Allow blank: No
  - Classification should match [Organization]'s information classification policy

- Column J (Retention Period): Dropdown list
  - Values: "1 Year, 3 Years, 5 Years, 7 Years, Indefinite"
  - Allow blank: No
  - ISO 27001 typically requires 3+ years for compliance evidence

- Column L (Verification Status): Dropdown list
  - Values: "Verified, Needs Verification, Missing, Outdated"
  - Allow blank: No

- Column F (Evidence Date), Column K (Last Verified Date): Date format DD.MM.YYYY


**Conditional Formatting**:

- Column L (Verification Status):
  - "Verified" → Green fill (C6EFCE)
  - "Needs Verification" → Yellow fill (FFEB9C)
  - "Missing" → Red fill (FFC7CE), bold
  - "Outdated" → Orange fill

- Column K (Last Verified Date):
  - If date > 180 days old and Status = "Verified" → Yellow fill (needs re-verification)
  - If blank → Red fill (never verified)

- Column I (Evidence Classification):
  - "Restricted" → Red text (high sensitivity)
  - "Confidential" → Orange text


**Special Features**:

- Row 2: Column headers with light gray background
- Row 1: Title "Evidence Register - Baseline Configuration Assessment" spanning A1:N1
- Hyperlinks: Column G (Evidence Location) should contain clickable hyperlinks where applicable
- Filter: Enable auto-filter to filter by Evidence Type, Related Asset, Verification Status


**Usage Notes**:

- Every claim in assessment should have supporting evidence documented here
- Evidence ID should be referenced in other sheets (e.g., in Notes columns) to create traceability
- For audits, auditor will sample evidence from this register to verify claims
- "Verified" status means evidence was checked and is valid/accessible
- Evidence verification should be performed at least semi-annually
- Missing or Outdated evidence is a compliance gap that must be remediated
- Retention Period based on [Organization]'s retention policy and regulatory requirements


---

## Sheet 11: Approval_Sign_Off

**Purpose**: Formal three-tier approval of the baseline configuration assessment. Documents who prepared, reviewed, and approved the assessment, establishing accountability.

**Structure** (Not tabular - signature block format):

**Section A: Document Information** (Rows 3-8)

| Attribute | Value |
|-------|-------|
| Assessment Title | Baseline Configuration Assessment - Control A.8.9 |
| Assessment Period | [DD.MM.YYYY] to [DD.MM.YYYY] |
| Document ID | ISMS-IMP-A.8.9.1 |
| Version | 1.0 |
| Assessment Date | [Auto-filled with TODAY() when sheet created] |

**Section B: Preparer Sign-Off** (Rows 10-16)

| Attribute | Value |
|-------|-------|
| Preparer Name | [Free text entry] |
| Preparer Role | [Free text entry, e.g., "System Administrator"] |
| Preparer Signature | [Free text entry or "Electronically signed"] |
| Date Prepared | [Date field - DD.MM.YYYY] |
| Completeness Attestation | "I attest that the information in this assessment has been compiled accurately to the best of my knowledge and all required evidence has been collected." |

**Section C: Reviewer Sign-Off** (Rows 18-25)

| Attribute | Value |
|-------|-------|
| Reviewer Name | [Free text entry] |
| Reviewer Role | [Free text entry, e.g., "Configuration Manager"] |
| Reviewer Signature | [Free text entry] |
| Date Reviewed | [Date field] |
| Review Findings | [Free text entry - summary of review findings] |
| Gaps Identified | [Free text entry - list of gaps requiring remediation] |
| Review Attestation | "I have reviewed this assessment and verify that it accurately represents [Organization]'s baseline configuration status. Identified gaps have been documented for remediation." |

**Section D: Approver Sign-Off** (Rows 27-35)

| Attribute | Value |
|-------|-------|
| Approver Name | [Free text entry] |
| Approver Role | [Free text entry, e.g., "IT Manager" or "CISO"] |
| Approver Signature | [Free text entry] |
| Date Approved | [Date field] |
| Approval Decision | [Dropdown: "Approved", "Approved with Conditions", "Not Approved - Revisions Required"] |
| Conditions/Comments | [Free text entry - any conditions or required actions] |
| Next Assessment Due | [Date field - typically +90 or +180 days based on criticality] |
| Approver Attestation | "I approve this baseline configuration assessment and authorize any documented remediation activities to proceed. This assessment will be used for compliance reporting and audit purposes." |

**Formatting**:

- Section headers (A, B, C, D): Bold, 14pt, dark blue background (003366), white text
- Field labels: Bold, 11pt, light gray background (D9D9D9)
- Value cells: 11pt, white background (user entry area)
- Attestation text: Italic, 10pt, light blue background (E7E6E6)


**Data Validations**:

- Date fields: DD.MM.YYYY format
- Approval Decision: Dropdown ("Approved", "Approved with Conditions", "Not Approved - Revisions Required")


**Conditional Formatting**:

- Approval Decision:
  - "Approved" → Green fill (C6EFCE)
  - "Approved with Conditions" → Yellow fill (FFEB9C)
  - "Not Approved - Revisions Required" → Red fill (FFC7CE)


**Special Features**:

- All value cells (for names, dates, signatures, comments) are UNLOCKED for user entry
- All other cells (labels, attestations) are PROTECTED to prevent modification
- Print area defined to fit on single page for formal signature printing if required
- Digital signature support: If [Organization] uses digital signatures, this section can be modified to reference digital signature validation


**Usage Notes**:

- Complete this sheet LAST after all other sheets are finalized
- Preparer completes Section B after finishing data entry in all assessment sheets
- Reviewer completes Section C after verifying completeness and accuracy
- Approver completes Section D after reviewing summary metrics and deciding on approval
- If "Not Approved", document required revisions in Conditions/Comments and repeat cycle
- Signed copy (digital or printed) should be retained as part of evidence (reference in Evidence_Register)
- This sign-off demonstrates governance oversight of configuration management


---

# Data Validation Rules Summary

## Dropdown Lists

**Asset_Inventory Sheet**:

- Asset Type: 43-type taxonomy (stored in hidden "Lookup_Tables" sheet)
- Criticality: Critical, High, Medium, Low
- Baseline Status: Defined, In Progress, Not Started, N/A


**Baseline_Repository Sheet**:

- Approval Status: Approved, Pending Review, Rejected, Draft


**Approval_Tracking Sheet**:

- Approval Status: Pending Submission, Submitted, Under Review, Approved, Rejected, Revisions Requested
- Approval Method: Change Advisory Board, Email Approval, Manager Sign-Off, Governance Committee, Automated Process
- Risk Assessment: Low, Medium, High


**Documentation_Assessment Sheet**:

- Documentation Completeness: Comprehensive, Adequate, Insufficient, Missing
- Documentation Accuracy: Verified Accurate, Mostly Accurate, Contains Errors, Not Verified
- Maintainability: Easy to Update, Moderate Effort, Difficult, Not Maintainable
- Accessibility: Highly Accessible, Accessible, Limited Access, Not Accessible
- Remediation Priority: Critical, High, Medium, Low


**Version_Control Sheet**:

- Change Type: Initial Release, Minor Update, Major Update, Security Patch, Emergency Change, Rollback


**Deviation_Register Sheet**:

- Deviation Type: Configuration Exception, Exclusion from Baseline, Temporary Deviation, Permanent Exception
- Risk Assessment: Low, Medium, High, Critical
- Review Frequency: Monthly, Quarterly, Semi-Annual, Annual
- Deviation Status: Active, Under Review, Expired, Revoked, No Longer Needed


**Evidence_Register Sheet**:

- Evidence Type: Screenshot, Configuration File, Scan Report, Approval Record, Meeting Minutes, Email, Document, System Export, Video Recording, Audit Log, Other
- Evidence Classification: Public, Internal, Confidential, Restricted
- Retention Period: 1 Year, 3 Years, 5 Years, 7 Years, Indefinite
- Verification Status: Verified, Needs Verification, Missing, Outdated


**Approval_Sign_Off Sheet**:

- Approval Decision: Approved, Approved with Conditions, Not Approved - Revisions Required


## Date Format

All date fields use **DD.MM.YYYY** format (European standard, as requested).

Date fields include:

- Last Reviewed Date, Next Review Due (Asset_Inventory)
- Approval Date, Last Updated (Baseline_Repository)
- Submission Date, Approval Date (Approval_Tracking)
- Version Date, Superseded Date (Version_Control)
- Approval Date, Review Date, Expiration Date (Deviation_Register)
- Evidence Date, Last Verified Date (Evidence_Register)
- Date Prepared, Date Reviewed, Date Approved, Next Assessment Due (Approval_Sign_Off)


## Number Validations

- Configuration Elements Count (Baseline_Repository): Whole numbers, 0-999
- Days Pending (Approval_Tracking): Calculated field, no manual entry
- All Score fields (Documentation_Assessment): Calculated, 0-100 range
- Assets Affected Count (Version_Control): Whole numbers


## Required vs Optional Fields

**Required Fields** (Allow Blank = No):

- Asset ID, Asset Type, Criticality, Baseline Status (Asset_Inventory)
- Baseline ID, Baseline Name, Approval Status (Baseline_Repository)
- All dropdown fields in Documentation_Assessment
- Deviation Type, Risk Assessment, Review Frequency, Status (Deviation_Register)
- Evidence Type, Classification, Retention Period, Verification Status (Evidence_Register)


**Optional Fields** (Allow Blank = Yes):

- Notes columns across all sheets
- Approval Date (until approved)
- Expiration Date (if not temporary deviation)


---

# Compliance Scoring Methodology

## Overall Baseline Coverage Calculation
```
Overall Coverage % = (Assets with Defined Baselines / Total In-Scope Assets) × 100

Where:

- Assets with Defined Baselines = COUNT(Asset_Inventory.Baseline_Status = "Defined")
- Total In-Scope Assets = COUNT(All Assets) - COUNT(Asset_Inventory.Baseline_Status = "N/A")
- Excluded assets (Baseline Status = "N/A") do not count against coverage


Target: ≥85% overall coverage
```

## Criticality-Based Coverage Targets

| Criticality Level | Target Coverage | Compliance Threshold |
|-------------------|----------------|---------------------|
| Critical | ≥95% | Red if <90%, Yellow if 90-94%, Green if ≥95% |
| High | ≥90% | Red if <85%, Yellow if 85-89%, Green if ≥90% |
| Medium | ≥80% | Red if <70%, Yellow if 70-79%, Green if ≥80% |
| Low | ≥60% | Red if <50%, Yellow if 50-59%, Green if ≥60% |

**Rationale**: 

- Critical assets pose highest business risk if misconfigured → highest baseline requirement
- Low criticality assets have flexibility but still need basic configuration management
- These thresholds align with industry best practices (CIS, NIST guidelines)


## Documentation Quality Scoring

**Four Quality Dimensions** (each scored 0-100):

1. **Completeness** (Weight: 25%)

   - Comprehensive = 100 (all config elements documented in detail)
   - Adequate = 75 (core elements documented, minor gaps)
   - Insufficient = 40 (significant gaps)
   - Missing = 0 (no documentation)


2. **Accuracy** (Weight: 25%)

   - Verified Accurate = 100 (documentation matches actual config)
   - Mostly Accurate = 75 (minor discrepancies)
   - Contains Errors = 40 (significant inaccuracies)
   - Not Verified = 0 (accuracy unknown)


3. **Maintainability** (Weight: 25%)

   - Easy to Update = 100 (well-structured, version controlled)
   - Moderate Effort = 75 (updateable but requires effort)
   - Difficult = 40 (hard to update, risk of errors)
   - Not Maintainable = 0 (cannot be updated)


4. **Accessibility** (Weight: 25%)

   - Highly Accessible = 100 (central repository, searchable)
   - Accessible = 75 (available but may need access request)
   - Limited Access = 40 (only few can access)
   - Not Accessible = 0 (location unknown or severely restricted)


**Overall Quality Score**:
```
Quality Score = (Completeness + Accuracy + Maintainability + Accessibility) / 4

Rating:

- Excellent: ≥90
- Good: 75-89
- Fair: 50-74
- Poor: <50


Target: ≥75% of baselines should have "Good" or "Excellent" rating
```

## Approval Process Health Metrics

**Average Approval Time**:
```
Average = SUM(Days from Submission to Approval) / COUNT(Approved Baselines)

Target: <14 days (2 weeks)
Status:

- Green if <14 days
- Yellow if 14-21 days
- Red if >21 days

```

**SLA Compliance**:
```
SLA Compliance % = (Baselines Approved Within SLA / Total Baselines Submitted) × 100

SLA = 14 days from submission to approval decision

Target: ≥90% SLA compliance
```

**Approval Success Rate**:
```
Success Rate = (Approved Baselines / (Approved + Rejected Baselines)) × 100

Target: >90%

Note: High rejection rate may indicate:

- Poor baseline quality during initial submission
- Insufficient preparation before submission
- Unrealistic approval criteria (may need adjustment)

```

## Deviation Risk Assessment

**Risk-Weighted Deviation Count**:
```
Risk Score = (Critical Deviations × 4) + (High Deviations × 3) + (Medium Deviations × 2) + (Low Deviations × 1)

Thresholds:

- Green: Risk Score <20
- Yellow: Risk Score 20-50
- Red: Risk Score >50


Target: Minimize high/critical risk deviations; ensure compensating controls in place
```

**Deviation Coverage**:
```
Deviation Rate % = (Assets with Active Deviations / Total Assets with Baselines) × 100

Target: <10%

High deviation rate may indicate:

- Baselines are not practical/realistic (need revision)
- Significant technical debt
- Poor change control discipline

```

## Compliance Status Determination

**Control A.8.9 Baseline Configuration Compliance**:
```
IF Critical Coverage ≥95% AND High Coverage ≥90% AND Overall Coverage ≥85%:
    Status = "COMPLIANT"
ELSE IF Critical Coverage ≥90% AND High Coverage ≥85% AND Overall Coverage ≥75%:
    Status = "PARTIALLY COMPLIANT"
ELSE:
    Status = "NON-COMPLIANT"

Additional Factors:

- Documentation quality: ≥60% of baselines should have "Good" or better rating
- Active High/Critical risk deviations: <5
- Approval process: No SLA breaches >30 days


Final Assessment:

- Compliant = All criteria met → Green status
- Partially Compliant = Minor gaps, remediation plan exists → Yellow status
- Non-Compliant = Significant gaps, immediate action required → Red status

```

---

# Usage Instructions

## Step-by-Step Completion Guide

**Phase 1: Preparation** (Day 1)
1. Configuration Manager assigns assessment to team
2. Review Instructions sheet
3. Identify all team members who will complete sections
4. Set timeline: typically 2-3 weeks for initial assessment

**Phase 2: Asset Inventory** (Days 2-5)
1. Export asset list from CMDB if available, or compile manually
2. Populate Asset_Inventory sheet (columns A-C, E-G)
3. For each asset, determine if baseline is Defined, In Progress, Not Started, or N/A
4. Document Baseline Reference (Column I) if baseline exists
5. Update Last Reviewed Date for existing baselines

**Phase 3: Baseline Documentation** (Days 6-10)
1. Populate Baseline_Repository sheet with all configuration baselines
2. For each baseline, document:

   - Version, applicable asset types, approval status
   - Documentation location (critical for audit)
   - Configuration elements count (how comprehensive is baseline)

3. Cross-reference Baseline IDs between Asset_Inventory and Baseline_Repository

**Phase 4: Approval and Quality Assessment** (Days 11-14)
1. Complete Approval_Tracking sheet for baselines in approval process
2. Configuration Manager completes Documentation_Assessment sheet

   - Review actual documentation
   - Score on four quality dimensions
   - Identify gaps for remediation

3. Update Version_Control sheet with baseline version history
4. Document any deviations in Deviation_Register

**Phase 5: Evidence Collection** (Days 15-18)
1. Compile all supporting evidence
2. Document each piece of evidence in Evidence_Register
3. Ensure evidence is accessible for audit
4. Verify evidence classification and retention periods

**Phase 6: Review and Approval** (Days 19-21)
1. Review Metrics_Summary sheet - identify gaps
2. Preparer completes Approval_Sign_Off (Section B)
3. Reviewer (Configuration Manager) verifies assessment (Section C)
4. Approver (IT Manager/CISO) reviews and approves (Section D)
5. If "Not Approved", revise and repeat

## Roles and Responsibilities

**Preparer (System Administrators, Asset Owners)**:

- Complete Asset_Inventory sheet for assigned assets
- Gather baseline documentation
- Collect evidence
- Populate Evidence_Register
- Complete Preparer sign-off


**Reviewer (Configuration Manager, Team Leads)**:

- Verify completeness of Asset_Inventory
- Complete Documentation_Assessment (quality scoring)
- Review Approval_Tracking status
- Validate Deviation_Register entries
- Identify remediation priorities
- Complete Reviewer sign-off


**Approver (IT Manager, CISO, Governance Committee)**:

- Review Metrics_Summary for overall compliance status
- Assess remediation plans for identified gaps
- Approve assessment or request revisions
- Authorize remediation activities
- Complete Approver sign-off


## Common Questions and Troubleshooting

**Q: What if we don't have a CMDB - how do we populate Asset_Inventory?**
A: Manually compile asset list from:

- Network scanning tools (Nmap, network inventory tools)
- Server/endpoint management consoles
- Cloud provider consoles (AWS, Azure, GCP)
- Application inventory from IT Service Management system
- Physical asset inventory records


**Q: How detailed should baselines be?**
A: Baselines should document:

- All security-relevant configuration parameters
- Service configurations (enabled/disabled services)
- User accounts and access controls
- Network settings (IP, firewall rules, ports)
- Installed software and versions
- Security hardening settings

Detail level depends on asset criticality - Critical assets need comprehensive baselines.

**Q: What if a baseline was approved verbally - how do we document?**
A: Verbal approvals should be:

- Documented in meeting minutes (add to Evidence_Register)
- Followed up with email confirmation (add to Evidence_Register)
- Retroactively formalized through proper approval workflow

Verbal-only approvals are not sufficient for audit purposes.

**Q: Can we have one baseline apply to multiple asset types?**
A: Yes, example: "Linux Server Standard Build" can apply to multiple Linux distributions.
Document in Baseline_Repository Column D (Applicable Asset Types): "Physical Server, Virtual Machine"

**Q: What if an asset needs multiple baselines?**
A: Some assets may need layered baselines:

- OS baseline (Windows Server 2022 Standard)
- Application baseline (IIS Web Server Configuration)
- Security baseline (CIS Benchmark Level 1)

Document all applicable baselines in Asset_Inventory Column I (comma-separated) or create separate rows.

**Q: How often should baselines be reviewed?**
A: Review frequency based on criticality:

- Critical/High assets: Quarterly (every 90 days)
- Medium/Low assets: Semi-annually (every 180 days)
- Also review when: major OS updates, security vulnerabilities discovered, significant config drift detected


**Q: What constitutes a valid deviation?**
A: Valid deviations require:

- Clear business justification (technical requirement, vendor limitation, legacy compatibility)
- Risk assessment (understand security impact)
- Compensating controls (if high/critical risk)
- Appropriate approval (manager/CISO depending on risk)
- Regular review (to determine if still needed)


## Integration with Other Processes

**Integration with Change Control (ISMS-IMP-A.8.9.2)**:

- When baseline is updated, create change request
- After change is approved and implemented, update Version_Control sheet
- New baseline version triggers re-assessment of affected assets


**Integration with Configuration Monitoring (ISMS-IMP-A.8.9.3)**:

- Baselines define "expected state" for drift detection
- Drift alerts trigger review of Asset_Inventory and Deviation_Register
- Frequent drift on same asset may indicate baseline needs revision


**Integration with Security Hardening (ISMS-IMP-A.8.9.4)**:

- Hardening standards are incorporated into baselines
- Hardening assessment results inform baseline updates
- Non-compliance with hardening standards may require deviation documentation


**Integration with Asset Inventory (A.5.9)**:

- Asset_Inventory sheet should align with organization's asset register
- Asset criticality classification comes from asset inventory process
- Baseline status feeds back into asset inventory as attribute


---

# Integration Points with Other Assessments

## Cross-Assessment Dependencies

| This Assessment | Integrates With | Integration Mechanism | Data Flow |
|----------------|----------------|----------------------|-----------|
| Asset_Inventory sheet | ISMS-IMP-A.8.9.2 (Change Control) | Changes to baselines trigger version updates | Bidirectional: Asset list → Change requests for baseline updates |
| Baseline_Repository | ISMS-IMP-A.8.9.3 (Config Monitoring) | Baselines define expected state for drift detection | Unidirectional: Baselines → Monitoring tools |
| Deviation_Register | ISMS-IMP-A.8.9.4 (Security Hardening) | Deviations may be security hardening exceptions | Bidirectional: Hardening gaps ↔ Approved deviations |
| Documentation_Assessment | ISMS-IMP-A.8.9.5 (Compliance Dashboard) | Quality scores feed into overall compliance | Unidirectional: Quality metrics → Dashboard |
| All sheets | A.5.9 (Asset Inventory) | Asset list must align with organizational asset register | Bidirectional: Asset data synchronized |

## Data Export Requirements

For integration with ISMS-IMP-A.8.9.5 (Compliance Dashboard), the following data must be extractable:

**Key Metrics to Export**:

- Overall Baseline Coverage % (from Metrics_Summary)
- Critical Asset Coverage % (from Metrics_Summary)
- High Asset Coverage % (from Metrics_Summary)
- Count of assets with baselines vs. total (from Asset_Inventory)
- Count of baselines pending approval (from Approval_Tracking)
- Count of High/Critical risk deviations (from Deviation_Register)
- Average documentation quality score (from Documentation_Assessment)
- Approval process health (average days, SLA compliance) (from Approval_Tracking)


**Export Format**: 

- Dashboard script will read this workbook directly using openpyxl
- Key cells referenced by name (e.g., Metrics_Summary!B5 for Overall Coverage %)
- Alternatively, create hidden "Export_Data" sheet with pre-calculated values for dashboard extraction


## CMDB Integration (if applicable)

If [Organization] maintains a Configuration Management Database (CMDB):

**Import from CMDB**:

- Asset inventory (Asset ID, Name, Type, Location, Owner)
- Asset criticality classifications
- Current baseline references (if tracked in CMDB)


**Export to CMDB**:

- Baseline status (Defined/In Progress/Not Started)
- Last reviewed dates
- Deviation status (for assets with active deviations)


**Synchronization Approach**:

- Initial assessment: Import asset list from CMDB
- Ongoing: Periodic sync (weekly/monthly) to keep aligned
- Trigger: Configuration changes in CMDB trigger update to this assessment


---

# Evidence Collection Guidelines

## Required Evidence Types

For audit verification, the following evidence types should be collected:

**1. Asset Inventory Evidence**:

- CMDB export or network scan results (proves asset list is complete)
- Asset classification documentation (proves criticality assignments)
- Asset ownership assignments (proves accountability)


**2. Baseline Documentation Evidence**:

- Configuration baseline documents (detailed config specifications)
- Configuration templates or scripts (for automated deployment)
- Baseline approval records (meeting minutes, email approvals, change tickets)


**3. Approval Workflow Evidence**:

- Change Advisory Board meeting minutes
- Email approval threads
- Governance committee decisions
- Change request tickets with approval history


**4. Quality Assessment Evidence**:

- Screenshots of actual configurations vs. baseline documentation (proves accuracy)
- Baseline review reports (proves regular review)
- Documentation audit findings (internal quality checks)


**5. Deviation Evidence**:

- Deviation request forms with business justification
- Risk assessment documentation for deviations
- Compensating control documentation (for high-risk deviations)
- Deviation review meeting minutes


**6. Version Control Evidence**:

- Baseline version history logs
- Change request records for baseline updates
- Before/after configuration comparisons


## Evidence Quality Standards

**Good Evidence Characteristics**:

- **Timestamped**: Clear date/time of when evidence was created
- **Attributable**: Shows who created/approved (names, signatures)
- **Authentic**: Original or verified copy, not easily fabricated
- **Accessible**: Stored in retrievable location, properly indexed
- **Retained**: Kept for required retention period (typically 3+ years for ISO 27001)


**Poor Evidence Examples**:

- Undated screenshots (no way to verify when captured)
- Verbal approvals with no documentation (not verifiable)
- Evidence stored on individual laptops (not accessible for audit)
- Evidence in personal email only (may be deleted, not formally retained)


## Evidence Repository Structure

**Recommended Folder Structure**:
```
Evidence/
├── ISMS-A.8.9-Baseline-Configuration/
│   ├── Asset-Inventory/
│   │   ├── CMDB-Export-YYYYMMDD.xlsx
│   │   ├── Network-Scan-Results-YYYYMMDD.pdf
│   │   └── Asset-Criticality-Classifications.pdf
│   ├── Baseline-Documentation/
│   │   ├── BL-WIN2022-STD-001-v2.1.docx
│   │   ├── BL-RHEL9-SEC-001-v1.3.pdf
│   │   └── ...
│   ├── Approval-Records/
│   │   ├── CAB-Meeting-Minutes-YYYYMMDD.pdf
│   │   ├── Email-Approval-Baseline-XYZ.pdf
│   │   └── ...
│   ├── Configuration-Snapshots/
│   │   ├── Server-Config-WebServer01-YYYYMMDD.txt
│   │   ├── Firewall-Rules-Export-YYYYMMDD.xml
│   │   └── ...
│   ├── Deviation-Documentation/
│   │   ├── Deviation-Request-DEV-2024-001.pdf
│   │   ├── Risk-Assessment-DEV-2024-001.pdf
│   │   └── ...
│   └── Assessment-Reports/
│       ├── Baseline-Assessment-YYYYMMDD.xlsx (this workbook)
│       ├── Assessment-Summary-Presentation.pptx
│       └── Evidence-Register-Index.pdf
```

## Evidence Sampling for Audits

**Auditor Will Typically Sample**:

- 5-10 Critical assets: Verify baseline exists, is documented, is applied
- 3-5 baselines: Review documentation quality, approval records
- 2-3 deviations: Verify justification, risk assessment, compensating controls
- 1-2 recent baseline updates: Trace through change control to version control
- Approval process: Review 2-3 approval records for completeness


**Preparation for Audit**:

- Ensure Evidence_Register is complete and up-to-date
- Verify all evidence links are accessible
- Pre-pull commonly requested evidence (saves time during audit)
- Review evidence for completeness (no missing signatures, dates, etc.)


## Evidence Verification Process

**Semi-Annual Evidence Verification** (recommended):
1. Review all entries in Evidence_Register
2. For each piece of evidence:

   - Verify file/document still exists and is accessible
   - Check if evidence is still valid (not outdated)
   - Update "Last Verified Date" column
   - Update "Verification Status" if issues found

3. For "Missing" or "Outdated" evidence:

   - Attempt to locate or recreate evidence
   - If cannot be recreated, document gap and remediation plan
   - Update Asset_Inventory or other sheets if baseline status changes due to missing evidence


**Continuous Evidence Management**:

- When new evidence is collected, immediately add to Evidence_Register
- When baseline is updated, archive old evidence and link new evidence
- When evidence reaches retention period end, review before destruction (some may need extension for ongoing issues)


---

# Document Maintenance and Updates

## Update Triggers

This assessment workbook should be updated when:

- **Quarterly**: Regular refresh for Critical/High assets
- **Semi-Annually**: Regular refresh for Medium/Low assets
- **Ad-Hoc**: Significant infrastructure changes (data center migration, cloud transformation, major application deployment)
- **Post-Incident**: After security incidents involving configuration issues
- **Audit Preparation**: Prior to internal or external audits
- **Policy Updates**: When ISMS-POL-A.8.9 is revised


## Version Control

**Workbook Versioning**:

- File naming convention: `ISMS_A_8_9_1_Baseline_Configuration_Assessment_YYYYMMDD.xlsx`
- Date in filename = Assessment completion date
- Retain previous versions for at least 3 years (audit trail)
- Store in version-controlled repository if available (SharePoint, Git, document management system)


**Change Log** (maintain in Instructions sheet or separate tab):
| Version | Date | Changes Made | Changed By |
|---------|------|--------------|------------|
| 1.0 | DD.MM.YYYY | Initial baseline assessment | [Name] |
| 1.1 | DD.MM.YYYY | Added 15 new cloud assets | [Name] |
| 2.0 | DD.MM.YYYY | Quarterly refresh, updated all sheets | [Name] |

## Annual Review Process

**Configuration Manager Responsibilities** (Annual):
1. Review all baselines for continued relevance
2. Verify documentation quality standards are still appropriate
3. Update asset taxonomy if new asset types introduced
4. Review deviation register - determine if long-standing deviations should become new baseline variants
5. Assess whether target coverage percentages need adjustment based on organizational maturity
6. Update evidence retention periods if regulatory requirements change
7. Brief management on annual trends (improving or declining baseline coverage)

---

# Specification Approval

**Document Owner**: Configuration Manager  
---

# PART II: TECHNICAL SPECIFICATION
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

**Note:** This section provides technical specifications for the assessment workbook generation and maintenance. Users completing the assessment should refer to Part I above.

---

# Workbook Structure Overview

**Generated Workbook Name**: `ISMS_A_8_9_1_Baseline_Configuration_Assessment_YYYYMMDD.xlsx`

**Total Sheets**: 11

| Sheet # | Sheet Name | Purpose | Row Count |
|---------|------------|---------|-----------|
| 1 | Instructions | Usage guidance, roles, workflow, legend | N/A |
| 2 | Asset_Inventory | All assets requiring baseline management | 100 data rows |
| 3 | Baseline_Repository | Documented configuration baselines | 50 data rows |
| 4 | Baseline_Coverage_Matrix | Coverage analysis by asset type | 43 data rows (one per asset type) |
| 5 | Approval_Tracking | Baseline approval status and workflow | 50 data rows |
| 6 | Documentation_Assessment | Quality evaluation of baseline docs | 30 data rows |
| 7 | Version_Control | Baseline version history | 50 data rows |
| 8 | Deviation_Register | Authorized deviations from baselines | 50 data rows |
| 9 | Metrics_Summary | Auto-calculated compliance metrics | N/A (formulas) |
| 10 | Evidence_Register | Supporting evidence and documentation links | 100 data rows |
| 11 | Approval_Sign_Off | Three-tier approval signatures | N/A (3 rows) |

**Sheet Relationship Flow**:
```
Asset_Inventory → (asset list) → Baseline_Coverage_Matrix
                                        ↓
Baseline_Repository → (baseline definitions) → Approval_Tracking
                                                       ↓
Documentation_Assessment → (quality scores) → Metrics_Summary
                                                       ↓
Version_Control → (history tracking) ← Deviation_Register
                                                       ↓
Evidence_Register → (audit trail) → Approval_Sign_Off
```

---

# Detailed Sheet Specifications

## Sheet 1: Instructions

**Purpose**: Provides comprehensive guidance on how to use the assessment workbook, defines roles and responsibilities, explains the approval workflow, and includes a legend for status values and color coding.

**Content Structure** (not row-based):

- Assessment overview and objectives
- Who should complete each sheet
- Step-by-step completion instructions
- Three-tier approval workflow diagram
- Status value definitions and color legend
- Common questions and troubleshooting
- Contact information for Configuration Manager


**Formatting**:

- Title section: Bold, 16pt, dark blue background (003366)
- Section headers: Bold, 14pt, light blue background (4472C4)
- Body text: Regular, 11pt Calibri
- Color legend showing: Green (Compliant), Yellow (Partial/In Progress), Red (Non-Compliant/Not Started), Gray (N/A)


**No Data Entry**: This is a read-only informational sheet.

---

## Sheet 2: Asset_Inventory

**Purpose**: Comprehensive list of all information assets within assessment scope that require configuration baseline management.

**Column Structure**:

| Column | Header | Data Type | Validation | Description |
|--------|--------|-----------|------------|-------------|
| A | Asset ID | Text | Free text | Unique asset identifier from CMDB or local tracking system |
| B | Asset Name | Text | Free text | Descriptive name of asset (e.g., "WebServer-Prod-01") |
| C | Asset Type | Text | Dropdown (43 types) | Classification from 43-type taxonomy (see Section 2.1) |
| D | Asset Category | Text | Auto-filled formula | Major category derived from Asset Type (Infrastructure/Endpoint/Network/App/Cloud/IoT) |
| E | Criticality | Text | Dropdown | Critical, High, Medium, Low |
| F | Owner | Text | Free text | Name of person/team responsible for asset |
| G | Location | Text | Free text | Physical location, data center, cloud region, or "Virtual" |
| H | Baseline Status | Text | Dropdown | Defined, In Progress, Not Started, N/A |
| I | Baseline Reference | Text | Free text | Link or reference to baseline in Baseline_Repository sheet |
| J | Last Reviewed Date | Date | Date format | Date baseline was last reviewed or updated |
| K | Next Review Due | Date | Formula | Auto-calculated based on criticality (Critical: +90 days, High: +90 days, Medium: +180 days, Low: +180 days) |
| L | Compliance Status | Text | Formula | Auto: "Compliant" if Baseline Status="Defined", else "Non-Compliant" |
| M | Notes | Text | Free text | Additional context, special considerations, or issues |

**Row Allocation**: 100 data rows (Row 3 to Row 102)

**Freeze Panes**: B3 (Column headers and Asset ID always visible during horizontal/vertical scrolling)

**Data Validations**:

- Column C (Asset Type): Dropdown list with all 43 asset types from taxonomy
  - List source: `{43-type list - too long for inline, stored in hidden sheet "Lookup_Tables"}`
  - Allow blank: No (required field)
  - Error alert: "Please select a valid asset type from the dropdown"

- Column E (Criticality): Dropdown list
  - Values: "Critical, High, Medium, Low"
  - Allow blank: No (required field)
  - Error alert: "Please select criticality level"

- Column H (Baseline Status): Dropdown list
  - Values: "Defined, In Progress, Not Started, N/A"
  - Allow blank: No (required field)
  - Error alert: "Please select baseline status"

- Column J (Last Reviewed Date): Date format DD.MM.YYYY
  - Allow blank: Yes (may be blank if never reviewed)


**Formulas**:

- Column D (Asset Category): `=IF(C3="","",VLOOKUP(C3,Lookup_Tables!$A$2:$B$44,2,FALSE))`
  - Explanation: Auto-populates major category based on Asset Type selection

- Column K (Next Review Due): 

```
  =IF(J3="","",IF(E3="Critical",J3+90,IF(E3="High",J3+90,IF(E3="Medium",J3+180,J3+180))))
```

  - Explanation: Calculates next review date based on criticality (Critical/High: 90 days, Medium/Low: 180 days)

- Column L (Compliance Status):

```
  =IF(H3="Defined","Compliant",IF(H3="N/A","Excluded","Non-Compliant"))
```

  - Explanation: Auto-determines compliance based on baseline status


**Conditional Formatting**:

- Column H (Baseline Status):
  - "Defined" → Green fill (C6EFCE)
  - "In Progress" → Yellow fill (FFEB9C)
  - "Not Started" → Red fill (FFC7CE)
  - "N/A" → Gray fill (D9D9D9)

- Column L (Compliance Status):
  - "Compliant" → Green fill (C6EFCE), bold text
  - "Non-Compliant" → Red fill (FFC7CE), bold text
  - "Excluded" → Gray fill (D9D9D9)

- Column K (Next Review Due):
  - If date < TODAY() AND Baseline Status ≠ "N/A" → Red fill (overdue review)
  - If date between TODAY() and TODAY()+30 → Yellow fill (due soon)


**Special Features**:

- Row 2: Column headers with light gray background (D9D9D9), bold text, centered alignment
- Row 1: Title "Asset Inventory - Baseline Configuration Assessment" spanning A1:M1, merged, dark blue background
- Protected cells: Columns D, K, L (formula cells) are locked to prevent accidental modification
- Hidden sheet: "Lookup_Tables" contains 43-type asset taxonomy for dropdown validation


**Usage Notes**:

- Preparer: Complete columns A-C, E-G, H-J, M for each asset
- Auto-populated: Columns D, K, L calculate automatically
- Start with Critical assets, then High, then Medium/Low
- If "N/A" in Baseline Status, explain in Notes column (M) why baseline is not applicable


---

## Sheet 3: Baseline_Repository

**Purpose**: Catalog of all configuration baselines maintained by [Organization]. Each row represents a distinct baseline that may apply to one or multiple assets.

**Column Structure**:

| Column | Header | Data Type | Validation | Description |
|--------|--------|-----------|------------|-------------|
| A | Baseline ID | Text | Free text | Unique identifier for baseline (e.g., "BL-WIN2022-STD-001") |
| B | Baseline Name | Text | Free text | Descriptive name (e.g., "Windows Server 2022 Standard Build") |
| C | Baseline Version | Text | Free text | Version number (e.g., "2.1", "2024.Q4") |
| D | Applicable Asset Types | Text | Free text | Which asset types use this baseline (comma-separated if multiple) |
| E | Description | Text | Free text | Summary of what this baseline configures |
| F | Approval Status | Text | Dropdown | Approved, Pending Review, Rejected, Draft |
| G | Approved By | Text | Free text | Name/role of person who approved baseline |
| H | Approval Date | Date | Date format | Date baseline was approved |
| I | Last Updated | Date | Date format | Date baseline was last modified |
| J | Documentation Location | Text | Free text | File path, URL, or document management system reference |
| K | Configuration Elements Count | Number | Number (0-999) | Number of configuration items defined in baseline |
| L | Applied to Assets Count | Number | Formula (optional) | Count of assets using this baseline (link to Asset_Inventory) |
| M | Notes | Text | Free text | Additional information, change history summary |

**Row Allocation**: 50 data rows (Row 3 to Row 52)

**Freeze Panes**: B3

**Data Validations**:

- Column F (Approval Status): Dropdown list
  - Values: "Approved, Pending Review, Rejected, Draft"
  - Allow blank: No
  - Error alert: "Please select approval status"

- Column H (Approval Date): Date format DD.MM.YYYY
  - Allow blank: Yes (blank if not yet approved)

- Column I (Last Updated): Date format DD.MM.YYYY
  - Allow blank: No (required field)

- Column K (Configuration Elements Count): Number
  - Whole numbers only, range 0-999
  - Allow blank: Yes


**Formulas**:

- Column L (Applied to Assets Count): *Optional - requires complex COUNTIF across sheets*

```
  =COUNTIF(Asset_Inventory!$I$3:$I$102,A3)
```

  - Explanation: Counts how many assets reference this baseline ID in Asset_Inventory sheet column I
  - Note: This formula may not work if users don't use exact Baseline ID matching


**Conditional Formatting**:

- Column F (Approval Status):
  - "Approved" → Green fill (C6EFCE)
  - "Pending Review" → Yellow fill (FFEB9C)
  - "Rejected" → Red fill (FFC7CE)
  - "Draft" → Light yellow fill (FFFFCC)

- Column H (Approval Date):
  - If blank AND Approval Status = "Approved" → Red fill (data inconsistency)

- Column I (Last Updated):
  - If date > 365 days old → Yellow fill (baseline may need review)


**Special Features**:

- Row 2: Column headers with light gray background, bold, centered
- Row 1: Title "Baseline Repository" spanning A1:M1, merged, dark blue background
- Protected cells: Column L (formula cell) locked if formula is implemented
- Link: Column J could contain hyperlinks to documentation (users can manually add)


**Usage Notes**:

- Preparer: Each distinct configuration baseline gets one row
- A baseline is "approved" when it passes through governance workflow
- Documentation location (Column J) should point to detailed configuration specs
- Configuration Elements Count (Column K) reflects how comprehensive the baseline is (example: Windows baseline with 150 configured items vs. basic baseline with 20 items)


---

## Sheet 4: Baseline_Coverage_Matrix

**Purpose**: Provides statistical analysis of baseline coverage by asset type. Auto-calculates coverage percentages to identify gaps requiring attention. This is a primarily formula-driven sheet.

**Column Structure**:

| Column | Header | Data Type | Validation | Description |
|--------|--------|-----------|------------|-------------|
| A | Asset Type | Text | Pre-filled | All 43 asset types from taxonomy (one row per type) |
| B | Asset Category | Text | Pre-filled | Major category (Infrastructure/Endpoint/Network/App/Cloud/IoT) |
| C | Total Assets | Number | Formula | Count of assets of this type from Asset_Inventory |
| D | Assets with Baselines | Number | Formula | Count of assets where Baseline Status = "Defined" |
| E | Assets In Progress | Number | Formula | Count where Baseline Status = "In Progress" |
| F | Assets Not Started | Number | Formula | Count where Baseline Status = "Not Started" |
| G | Assets N/A | Number | Formula | Count where Baseline Status = "N/A" |
| H | Coverage % | Percentage | Formula | (Assets with Baselines / (Total Assets - Assets N/A)) × 100 |
| I | Critical Assets Count | Number | Formula | Count of Critical assets of this type |
| J | Critical Coverage % | Percentage | Formula | Coverage % for Critical assets only |
| K | Status | Text | Formula | "Compliant", "Partial", "Non-Compliant" based on coverage % |
| L | Gap Analysis | Text | Formula | Descriptive gap statement |

**Row Allocation**: 43 data rows (Row 3 to Row 45) - one row per asset type from taxonomy

**Freeze Panes**: B3

**Pre-filled Data**:

- Column A: All 43 asset types (pre-populated, users do not edit)
- Column B: Corresponding category for each asset type (pre-populated)


**Formulas** (Examples - actual formulas depend on implementation):

- Column C (Total Assets):

```
  =COUNTIF(Asset_Inventory!$C$3:$C$102,A3)
```

  - Explanation: Counts how many assets in Asset_Inventory match this Asset Type

- Column D (Assets with Baselines):

```
  =COUNTIFS(Asset_Inventory!$C$3:$C$102,A3,Asset_Inventory!$H$3:$H$102,"Defined")
```

  - Explanation: Counts assets of this type where Baseline Status = "Defined"

- Column E (Assets In Progress):

```
  =COUNTIFS(Asset_Inventory!$C$3:$C$102,A3,Asset_Inventory!$H$3:$H$102,"In Progress")
```

- Column F (Assets Not Started):

```
  =COUNTIFS(Asset_Inventory!$C$3:$C$102,A3,Asset_Inventory!$H$3:$H$102,"Not Started")
```

- Column G (Assets N/A):

```
  =COUNTIFS(Asset_Inventory!$C$3:$C$102,A3,Asset_Inventory!$H$3:$H$102,"N/A")
```

- Column H (Coverage %):

```
  =IF((C3-G3)=0,0,D3/(C3-G3)*100)
```

  - Explanation: Percentage of non-excluded assets with defined baselines
  - Handles division by zero if no assets or all excluded

- Column I (Critical Assets Count):

```
  =COUNTIFS(Asset_Inventory!$C$3:$C$102,A3,Asset_Inventory!$E$3:$E$102,"Critical")
```

- Column J (Critical Coverage %):

```
  =IF(I3=0,0,COUNTIFS(Asset_Inventory!$C$3:$C$102,A3,Asset_Inventory!$E$3:$E$102,"Critical",Asset_Inventory!$H$3:$H$102,"Defined")/I3*100)
```

  - Explanation: Coverage % specifically for Critical assets

- Column K (Status):

```
  =IF(H3>=90,"Compliant",IF(H3>=60,"Partial","Non-Compliant"))
```

  - Explanation: Status based on coverage thresholds (≥90% = Compliant, 60-89% = Partial, <60% = Non-Compliant)

- Column L (Gap Analysis):

```
  =IF(K3="Compliant","Coverage target met",IF(F3>0,F3&" assets need baselines started","Review in-progress baselines"))
```

  - Explanation: Dynamic text describing the gap


**Conditional Formatting**:

- Column H (Coverage %):
  - ≥90% → Green fill (C6EFCE)
  - 60-89% → Yellow fill (FFEB9C)
  - <60% → Red fill (FFC7CE)

- Column J (Critical Coverage %):
  - ≥95% → Green fill (target for Critical assets)
  - 80-94% → Yellow fill
  - <80% → Red fill

- Column K (Status):
  - "Compliant" → Green text, bold
  - "Partial" → Yellow/orange text, bold
  - "Non-Compliant" → Red text, bold


**Special Features**:

- Row 2: Column headers with light gray background
- Row 1: Title "Baseline Coverage Matrix by Asset Type" spanning A1:L1
- All cells protected (formula-driven sheet, no user input)
- Summary row at bottom (Row 46): Totals across all asset types
  - Column C: =SUM(C3:C45)
  - Column D: =SUM(D3:D45)
  - Column H: =IF(C46-G46=0,0,D46/(C46-G46)*100) [overall coverage]


**Usage Notes**:

- This sheet auto-updates as Asset_Inventory is filled in
- No manual data entry required
- Use this to identify which asset types have poorest baseline coverage
- Focus remediation efforts on rows with "Non-Compliant" status


---

## Sheet 5: Approval_Tracking

**Purpose**: Track the approval workflow status for each configuration baseline through the governance process.

**Column Structure**:

| Column | Header | Data Type | Validation | Description |
|--------|--------|-----------|------------|-------------|
| A | Baseline ID | Text | Free text | Reference to baseline from Baseline_Repository (Column A) |
| B | Baseline Name | Text | Free text | Descriptive name for easy reference |
| C | Submission Date | Date | Date format | Date baseline was submitted for approval |
| D | Approver Name | Text | Free text | Person responsible for approval (role or name) |
| E | Approval Status | Text | Dropdown | Pending Submission, Submitted, Under Review, Approved, Rejected, Revisions Requested |
| F | Approval Date | Date | Date format | Date approval was granted (blank if not yet approved) |
| G | Approval Method | Text | Dropdown | Change Advisory Board, Email Approval, Manager Sign-Off, Governance Committee |
| H | Approval Reference | Text | Free text | Meeting minutes reference, email thread ID, ticket number |
| I | Business Justification | Text | Free text | Why this baseline is needed |
| J | Risk Assessment | Text | Dropdown | Low, Medium, High |
| K | Days Pending | Number | Formula | Days between submission and current date or approval date |
| L | SLA Status | Text | Formula | "Within SLA" (<14 days), "Approaching SLA" (14-21 days), "SLA Breach" (>21 days) |
| M | Next Action | Text | Free text | Required follow-up actions |
| N | Notes | Text | Free text | Additional context |

**Row Allocation**: 50 data rows (Row 3 to Row 52)

**Freeze Panes**: B3

**Data Validations**:

- Column E (Approval Status): Dropdown list
  - Values: "Pending Submission, Submitted, Under Review, Approved, Rejected, Revisions Requested"
  - Allow blank: No

- Column G (Approval Method): Dropdown list
  - Values: "Change Advisory Board, Email Approval, Manager Sign-Off, Governance Committee, Automated Process"
  - Allow blank: Yes (blank until submitted)

- Column J (Risk Assessment): Dropdown list
  - Values: "Low, Medium, High"
  - Allow blank: Yes

- Column C (Submission Date), Column F (Approval Date): Date format DD.MM.YYYY


**Formulas**:

- Column K (Days Pending):

```
  =IF(C3="","",IF(F3="",TODAY()-C3,F3-C3))
```

  - Explanation: If submitted but not approved, calculates days from submission to today. If approved, calculates days from submission to approval.

- Column L (SLA Status):

```
  =IF(K3="","",IF(K3<=14,"Within SLA",IF(K3<=21,"Approaching SLA","SLA Breach")))
```

  - Explanation: Approval SLA is 14 days (customize for [Organization]). Warns if approaching or exceeding SLA.


**Conditional Formatting**:

- Column E (Approval Status):
  - "Approved" → Green fill (C6EFCE)
  - "Under Review" → Yellow fill (FFEB9C)
  - "Rejected" → Red fill (FFC7CE)
  - "Revisions Requested" → Orange fill (FFA500)

- Column L (SLA Status):
  - "Within SLA" → Green text
  - "Approaching SLA" → Yellow/orange text, bold
  - "SLA Breach" → Red text, bold

- Column K (Days Pending):
  - >21 days → Red fill (significant delay)


**Special Features**:

- Row 2: Column headers with light gray background
- Row 1: Title "Baseline Approval Tracking" spanning A1:N1
- Protected cells: Columns K and L (formula cells) locked
- Link to Baseline_Repository: Column A should match Baseline IDs


**Usage Notes**:

- Preparer: Create entry when baseline is submitted for approval
- Update Column E as baseline progresses through approval workflow
- Column H (Approval Reference) is critical for audit trail - document where approval decision is recorded
- If "Revisions Requested", document required changes in Column M (Next Action)
- SLA of 14 days is example; customize for [Organization]'s governance cycle


---

## Sheet 6: Documentation_Assessment

**Purpose**: Evaluate the quality of configuration baseline documentation against defined criteria. This assessment ensures baselines are not just defined, but properly documented for long-term maintainability and audit verification.

**Column Structure**:

| Column | Header | Data Type | Validation | Description |
|--------|--------|-----------|------------|-------------|
| A | Baseline ID | Text | Free text | Reference to baseline from Baseline_Repository |
| B | Baseline Name | Text | Free text | Descriptive name for reference |
| C | Documentation Completeness | Text | Dropdown | Comprehensive, Adequate, Insufficient, Missing |
| D | Completeness Score | Number | Formula | Numeric score: Comprehensive=100, Adequate=75, Insufficient=40, Missing=0 |
| E | Documentation Accuracy | Text | Dropdown | Verified Accurate, Mostly Accurate, Contains Errors, Not Verified |
| F | Accuracy Score | Number | Formula | Numeric score: Verified=100, Mostly=75, Errors=40, Not Verified=0 |
| G | Maintainability | Text | Dropdown | Easy to Update, Moderate Effort, Difficult, Not Maintainable |
| H | Maintainability Score | Number | Formula | Numeric score: Easy=100, Moderate=75, Difficult=40, Not Maintainable=0 |
| I | Accessibility | Text | Dropdown | Highly Accessible, Accessible, Limited Access, Not Accessible |
| J | Accessibility Score | Number | Formula | Numeric score: Highly=100, Accessible=75, Limited=40, Not=0 |
| K | Overall Quality Score | Number | Formula | Average of scores in columns D, F, H, J |
| L | Quality Rating | Text | Formula | Excellent (≥90), Good (75-89), Fair (50-74), Poor (<50) |
| M | Gaps Identified | Text | Free text | Specific documentation gaps or improvement areas |
| N | Remediation Priority | Text | Dropdown | Critical, High, Medium, Low |
| O | Target Completion Date | Date | Date format | When documentation improvements should be completed |

**Row Allocation**: 30 data rows (Row 3 to Row 32)

**Freeze Panes**: B3

**Data Validations**:

- Column C (Documentation Completeness): Dropdown list
  - Values: "Comprehensive, Adequate, Insufficient, Missing"
  - Allow blank: No
  - Comprehensive = All configuration elements documented with detailed specifications
  - Adequate = Core elements documented, minor gaps acceptable
  - Insufficient = Significant gaps in documentation
  - Missing = No meaningful documentation exists

- Column E (Documentation Accuracy): Dropdown list
  - Values: "Verified Accurate, Mostly Accurate, Contains Errors, Not Verified"
  - Allow blank: No

- Column G (Maintainability): Dropdown list
  - Values: "Easy to Update, Moderate Effort, Difficult, Not Maintainable"
  - Allow blank: No

- Column I (Accessibility): Dropdown list
  - Values: "Highly Accessible, Accessible, Limited Access, Not Accessible"
  - Allow blank: No
  - Highly Accessible = Available in central repository, searchable, version controlled
  - Accessible = Available but may require specific access request
  - Limited Access = Only few people can access
  - Not Accessible = Documentation location unknown or access severely restricted

- Column N (Remediation Priority): Dropdown list
  - Values: "Critical, High, Medium, Low"
  - Allow blank: Yes

- Column O (Target Completion Date): Date format DD.MM.YYYY


**Formulas**:

- Column D (Completeness Score):

```
  =IF(C3="Comprehensive",100,IF(C3="Adequate",75,IF(C3="Insufficient",40,0)))
```

- Column F (Accuracy Score):

```
  =IF(E3="Verified Accurate",100,IF(E3="Mostly Accurate",75,IF(E3="Contains Errors",40,0)))
```

- Column H (Maintainability Score):

```
  =IF(G3="Easy to Update",100,IF(G3="Moderate Effort",75,IF(G3="Difficult",40,0)))
```

- Column J (Accessibility Score):

```
  =IF(I3="Highly Accessible",100,IF(I3="Accessible",75,IF(I3="Limited Access",40,0)))
```

- Column K (Overall Quality Score):

```
  =(D3+F3+H3+J3)/4
```

  - Explanation: Average of four quality dimensions

- Column L (Quality Rating):

```
  =IF(K3>=90,"Excellent",IF(K3>=75,"Good",IF(K3>=50,"Fair","Poor")))
```

**Conditional Formatting**:

- Column K (Overall Quality Score):
  - ≥90 → Green fill (C6EFCE)
  - 75-89 → Light green fill
  - 50-74 → Yellow fill (FFEB9C)
  - <50 → Red fill (FFC7CE)

- Column L (Quality Rating):
  - "Excellent" → Dark green text, bold
  - "Good" → Green text
  - "Fair" → Orange text
  - "Poor" → Red text, bold

- Column O (Target Completion Date):
  - If date < TODAY() and Quality Rating = "Poor" or "Fair" → Red fill (overdue)


**Special Features**:

- Row 2: Column headers with light gray background
- Row 1: Title "Baseline Documentation Quality Assessment" spanning A1:O1
- Protected cells: Columns D, F, H, J, K, L (formula cells) locked
- Scoring rubric: Include reference note that explains scoring methodology


**Usage Notes**:

- Reviewer typically completes this assessment (Configuration Manager or designee)
- Quality assessment performed by reviewing actual baseline documentation
- "Verified Accurate" means documentation was compared against actual configured systems and matches
- Remediation Priority should be "Critical" for baselines with Poor quality that apply to Critical assets
- This assessment drives documentation improvement initiatives


---

## Sheet 7: Version_Control

**Purpose**: Track version history of configuration baselines over time. When baselines are updated through change control processes, new versions are recorded here to maintain audit trail and support rollback if needed.

**Column Structure**:

| Column | Header | Data Type | Validation | Description |
|--------|--------|-----------|------------|-------------|
| A | Baseline ID | Text | Free text | Reference to baseline from Baseline_Repository |
| B | Baseline Name | Text | Free text | Descriptive name |
| C | Version Number | Text | Free text | Version identifier (e.g., "1.0", "2.3", "2024.Q1") |
| D | Version Date | Date | Date format | Date this version was created/approved |
| E | Previous Version | Text | Free text | Version number this replaced (blank for initial version) |
| F | Change Type | Text | Dropdown | Initial Release, Minor Update, Major Update, Security Patch, Emergency Change |
| G | Change Summary | Text | Free text | Brief description of what changed in this version |
| H | Change Request Reference | Text | Free text | Reference to change control record (see ISMS-IMP-A.8.9.2) |
| I | Changed By | Text | Free text | Person/team who made the change |
| J | Approved By | Text | Free text | Person who approved this version |
| K | Superseded Date | Date | Date format | Date this version was replaced by newer version (blank if current) |
| L | Status | Text | Formula | "Current" if Superseded Date is blank, "Superseded" if date present |
| M | Assets Affected Count | Number | Free text/Formula | Number of assets using this baseline version |
| N | Documentation Location | Text | Free text | Where this specific version's documentation is stored |

**Row Allocation**: 50 data rows (Row 3 to Row 52)

**Freeze Panes**: B3

**Data Validations**:

- Column F (Change Type): Dropdown list
  - Values: "Initial Release, Minor Update, Major Update, Security Patch, Emergency Change, Rollback"
  - Allow blank: No
  - Initial Release = First version of baseline
  - Minor Update = Small changes, non-breaking (e.g., parameter adjustment)
  - Major Update = Significant changes, may require testing (e.g., new OS version)
  - Security Patch = Security-driven update (urgent)
  - Emergency Change = Unplanned change due to incident
  - Rollback = Reverting to previous version

- Column D (Version Date), Column K (Superseded Date): Date format DD.MM.YYYY


**Formulas**:

- Column L (Status):

```
  =IF(K3="","Current","Superseded")
```

  - Explanation: If Superseded Date is blank, version is still current; otherwise it's been replaced


**Conditional Formatting**:

- Column L (Status):
  - "Current" → Green fill (C6EFCE), bold
  - "Superseded" → Gray fill (D9D9D9)

- Column K (Superseded Date):
  - If blank → Light green background (indicates current version)

- Column F (Change Type):
  - "Emergency Change" → Red text (highlights urgent changes)
  - "Security Patch" → Orange text (security-related)


**Special Features**:

- Row 2: Column headers with light gray background
- Row 1: Title "Baseline Version Control History" spanning A1:N1
- Protected cells: Column L (formula cell) locked
- Sort: Should be sorted by Baseline ID (A) then Version Date (D) descending to show most recent first
- Filter: Enable auto-filter on header row to allow filtering by Baseline ID, Status, Change Type


**Usage Notes**:

- Every time a baseline is updated, a new row is added to this sheet
- Previous version's Superseded Date (Column K) is filled when new version is created
- Change Request Reference (Column H) links to formal change control (see ISMS-IMP-A.8.9.2 assessment)
- For audit purposes, maintain history for at least 3 years
- "Current" versions should match the version in Baseline_Repository sheet
- Multiple baselines can have multiple versions tracked in this sheet (one row per version)


---

## Sheet 8: Deviation_Register

**Purpose**: Document and track authorized deviations from standard configuration baselines. Deviations require business justification and approval, and are regularly reviewed to ensure they remain valid.

**Column Structure**:

| Column | Header | Data Type | Validation | Description |
|--------|--------|-----------|------------|-------------|
| A | Deviation ID | Text | Free text | Unique identifier for deviation (e.g., "DEV-2024-001") |
| B | Asset ID | Text | Free text | Reference to specific asset with deviation |
| C | Asset Name | Text | Free text | Descriptive name of asset |
| D | Baseline ID | Text | Free text | Which baseline this deviates from |
| E | Deviation Type | Text | Dropdown | Configuration Exception, Exclusion from Baseline, Temporary Deviation, Permanent Exception |
| F | Configuration Element | Text | Free text | Specific configuration item that deviates (e.g., "Firewall Rule 502") |
| G | Standard Value | Text | Free text | What the baseline specifies |
| H | Actual Value | Text | Free text | What is actually configured on this asset |
| I | Business Justification | Text | Free text | Why this deviation is necessary |
| J | Risk Assessment | Text | Dropdown | Low, Medium, High, Critical |
| K | Compensating Controls | Text | Free text | Security controls in place to mitigate deviation risk |
| L | Approved By | Text | Free text | Name/role of approver |
| M | Approval Date | Date | Date format | Date deviation was approved |
| N | Review Frequency | Text | Dropdown | Monthly, Quarterly, Semi-Annual, Annual |
| O | Next Review Date | Date | Formula | Auto-calculated based on Approval Date + Review Frequency |
| P | Deviation Status | Text | Dropdown | Active, Under Review, Expired, Revoked, No Longer Needed |
| Q | Expiration Date | Date | Date format | Date deviation authorization expires (if temporary) |
| R | Notes | Text | Free text | Additional context |

**Row Allocation**: 50 data rows (Row 3 to Row 52)

**Freeze Panes**: B3

**Data Validations**:

- Column E (Deviation Type): Dropdown list
  - Values: "Configuration Exception, Exclusion from Baseline, Temporary Deviation, Permanent Exception"
  - Allow blank: No
  - Configuration Exception = Specific config item differs from baseline
  - Exclusion from Baseline = Entire asset excluded from baseline application
  - Temporary Deviation = Short-term deviation (has expiration date)
  - Permanent Exception = Long-term deviation (no expiration, but regularly reviewed)

- Column J (Risk Assessment): Dropdown list
  - Values: "Low, Medium, High, Critical"
  - Allow blank: No

- Column N (Review Frequency): Dropdown list
  - Values: "Monthly, Quarterly, Semi-Annual, Annual"
  - Allow blank: No
  - High/Critical risk deviations should use Monthly or Quarterly

- Column P (Deviation Status): Dropdown list
  - Values: "Active, Under Review, Expired, Revoked, No Longer Needed"
  - Allow blank: No

- Column M (Approval Date), Column Q (Expiration Date): Date format DD.MM.YYYY


**Formulas**:

- Column O (Next Review Date):

```
  =IF(M3="","",IF(N3="Monthly",M3+30,IF(N3="Quarterly",M3+90,IF(N3="Semi-Annual",M3+180,M3+365))))
```

  - Explanation: Calculates next review based on approval date + review frequency


**Conditional Formatting**:

- Column J (Risk Assessment):
  - "Critical" → Dark red fill (C00000), white text, bold
  - "High" → Red fill (FFC7CE)
  - "Medium" → Yellow fill (FFEB9C)
  - "Low" → Light green fill (E2EFDA)

- Column P (Deviation Status):
  - "Active" → Green fill (C6EFCE)
  - "Expired" → Red fill (FFC7CE), bold
  - "Under Review" → Yellow fill (FFEB9C)
  - "Revoked" → Gray fill (D9D9D9)

- Column O (Next Review Date):
  - If date < TODAY() and Status = "Active" → Red fill (overdue review)
  - If date between TODAY() and TODAY()+30 → Yellow fill (review due soon)

- Column Q (Expiration Date):
  - If date < TODAY() and Status = "Active" → Red fill, bold (expired deviation still active - must update status)


**Special Features**:

- Row 2: Column headers with light gray background
- Row 1: Title "Configuration Baseline Deviation Register" spanning A1:R1
- Protected cells: Column O (formula cell) locked
- High-risk deviations (Critical/High) should be highlighted in summary metrics


**Usage Notes**:

- Every deviation from a standard baseline MUST be documented here
- Business Justification (Column I) is critical - auditors will review this
- Compensating Controls (Column K) are mandatory for High/Critical risk deviations
- Temporary Deviations (Column E) must have Expiration Date (Column Q)
- When deviation is no longer needed, update Status to "No Longer Needed" and document in Notes
- Regular review of this register is part of Configuration Manager responsibilities
- Policy reference: ISMS-POL-A.8.9-S5.C (Configuration Deviation Procedures)


---

## Sheet 9: Metrics_Summary

**Purpose**: Auto-calculate key compliance metrics and provide executive summary of baseline configuration assessment results. This sheet is formula-driven and requires no manual data entry.

**Content Structure** (Not tabular - dashboard layout):

**Section A: Overall Compliance Metrics** (Rows 3-10)

| Metric | Formula/Value | Target | Status |
|--------|---------------|--------|--------|
| Total Assets in Scope | =COUNTA(Asset_Inventory!A3:A102)-COUNTBLANK(Asset_Inventory!A3:A102) | N/A | [Calculated] |
| Assets with Defined Baselines | =COUNTIF(Asset_Inventory!H3:H102,"Defined") | N/A | [Calculated] |
| Overall Baseline Coverage % | =(Assets with Baselines / Total Assets) × 100 | ≥85% | [Green/Yellow/Red] |
| Critical Asset Coverage % | =COUNTIFS(Asset_Inventory!E3:E102,"Critical",Asset_Inventory!H3:H102,"Defined")/COUNTIF(Asset_Inventory!E3:E102,"Critical")*100 | ≥95% | [Status] |
| High Asset Coverage % | Similar formula for High criticality | ≥90% | [Status] |
| Baselines Pending Approval | =COUNTIF(Approval_Tracking!E3:E52,"Submitted")+COUNTIF(Approval_Tracking!E3:E52,"Under Review") | 0 | [Status] |
| Documentation Quality - Excellent | =COUNTIF(Documentation_Assessment!L3:L32,"Excellent") | Maximize | [Count] |
| Documentation Quality - Poor | =COUNTIF(Documentation_Assessment!L3:L32,"Poor") | 0 | [Count] |
| Active Deviations - High Risk | =COUNTIFS(Deviation_Register!J3:J52,"High",Deviation_Register!P3:P52,"Active")+COUNTIFS(Deviation_Register!J3:J52,"Critical",Deviation_Register!P3:P52,"Active") | <5 | [Status] |

**Section B: Coverage by Asset Category** (Rows 12-20)

| Category | Total Assets | Assets with Baselines | Coverage % | Status |
|----------|--------------|----------------------|------------|--------|
| Infrastructure | =Formula from Coverage_Matrix | =Formula | =Formula | [Status] |
| Endpoint | =Formula | =Formula | =Formula | [Status] |
| Network Services | =Formula | =Formula | =Formula | [Status] |
| Applications | =Formula | =Formula | =Formula | [Status] |
| Cloud | =Formula | =Formula | =Formula | [Status] |
| IoT/OT | =Formula | =Formula | =Formula | [Status] |

**Section C: Top Gaps Requiring Attention** (Rows 22-32)

| Priority | Gap Description | Assets Affected | Remediation Owner | Target Date |
|----------|----------------|-----------------|-------------------|-------------|
| 1 | [Auto-generated from analysis] | [Count] | [TBD] | [TBD] |
| 2 | [Auto-generated] | [Count] | [TBD] | [TBD] |
| ... | ... | ... | ... | ... |

**Section D: Approval Process Health** (Rows 34-40)

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| Average Approval Time (Days) | =AVERAGE(Approval_Tracking!K3:K52) | <14 days | [Status] |
| Baselines Exceeding SLA | =COUNTIF(Approval_Tracking!L3:L52,"SLA Breach") | 0 | [Status] |
| Approval Success Rate | =(Approved / (Approved + Rejected)) × 100 | >90% | [Status] |

**Formatting**:

- Section headers: Bold, 14pt, dark blue background (003366), white text
- Metric labels: Bold, 11pt
- Values: 12pt, conditionally formatted based on status
- Target column: Gray background (D9D9D9)
- Status column: Conditional formatting (Green/Yellow/Red)


**Conditional Formatting**:

- Overall Coverage %:
  - ≥85% → Green fill
  - 70-84% → Yellow fill
  - <70% → Red fill

- Critical/High Asset Coverage:
  - Meets or exceeds target → Green
  - Within 5% of target → Yellow
  - Below target by >5% → Red

- Documentation Quality counts:
  - "Excellent" count → Green text
  - "Poor" count → Red text if >0


**Special Features**:

- All cells protected (formula-driven, no user input)
- Print area defined (fits on 2 pages for executive reporting)
- Page breaks set logically between sections
- Chart/graph area reserved (Rows 42-60) for visual representation if organization wants to add charts


**Usage Notes**:

- This sheet updates automatically as other sheets are populated
- Review this sheet LAST after all other sheets are complete
- Use this sheet for executive reporting and governance meetings
- Red/Yellow status items should be discussed in Approval Sign-Off section
- This feeds into overall compliance dashboard (ISMS-IMP-A.8.9.5)


---

## Sheet 10: Evidence_Register

**Purpose**: Central register of all supporting evidence and documentation that demonstrates baseline configuration implementation. Critical for audit verification and traceability.

**Column Structure**:

| Column | Header | Data Type | Validation | Description |
|--------|--------|-----------|------------|-------------|
| A | Evidence ID | Text | Free text | Unique identifier (e.g., "EVID-A89-001") |
| B | Evidence Type | Text | Dropdown | Screenshot, Configuration File, Scan Report, Approval Record, Meeting Minutes, Email, Document, System Export |
| C | Evidence Description | Text | Free text | Brief description of what this evidence shows |
| D | Related Asset(s) | Text | Free text | Asset ID(s) this evidence relates to (comma-separated if multiple) |
| E | Related Baseline(s) | Text | Free text | Baseline ID(s) this evidence supports |
| F | Evidence Date | Date | Date format | Date evidence was created/captured |
| G | Evidence Location | Text | Free text | File path, URL, document management system reference, physical location |
| H | Evidence Owner | Text | Free text | Person/team responsible for this evidence |
| I | Evidence Classification | Text | Dropdown | Public, Internal, Confidential, Restricted |
| J | Retention Period | Text | Dropdown | 1 Year, 3 Years, 5 Years, 7 Years, Indefinite |
| K | Last Verified Date | Date | Date format | Date evidence was last verified as still valid/accessible |
| L | Verification Status | Text | Dropdown | Verified, Needs Verification, Missing, Outdated |
| M | Linked Control Requirement | Text | Free text | Which POL section this evidence supports (e.g., "POL-S2.1-2.1.2") |
| N | Notes | Text | Free text | Additional context |

**Row Allocation**: 100 data rows (Row 3 to Row 102)

**Freeze Panes**: B3

**Data Validations**:

- Column B (Evidence Type): Dropdown list
  - Values: "Screenshot, Configuration File, Scan Report, Approval Record, Meeting Minutes, Email, Document, System Export, Video Recording, Audit Log, Other"
  - Allow blank: No

- Column I (Evidence Classification): Dropdown list
  - Values: "Public, Internal, Confidential, Restricted"
  - Allow blank: No
  - Classification should match [Organization]'s information classification policy

- Column J (Retention Period): Dropdown list
  - Values: "1 Year, 3 Years, 5 Years, 7 Years, Indefinite"
  - Allow blank: No
  - ISO 27001 typically requires 3+ years for compliance evidence

- Column L (Verification Status): Dropdown list
  - Values: "Verified, Needs Verification, Missing, Outdated"
  - Allow blank: No

- Column F (Evidence Date), Column K (Last Verified Date): Date format DD.MM.YYYY


**Conditional Formatting**:

- Column L (Verification Status):
  - "Verified" → Green fill (C6EFCE)
  - "Needs Verification" → Yellow fill (FFEB9C)
  - "Missing" → Red fill (FFC7CE), bold
  - "Outdated" → Orange fill

- Column K (Last Verified Date):
  - If date > 180 days old and Status = "Verified" → Yellow fill (needs re-verification)
  - If blank → Red fill (never verified)

- Column I (Evidence Classification):
  - "Restricted" → Red text (high sensitivity)
  - "Confidential" → Orange text


**Special Features**:

- Row 2: Column headers with light gray background
- Row 1: Title "Evidence Register - Baseline Configuration Assessment" spanning A1:N1
- Hyperlinks: Column G (Evidence Location) should contain clickable hyperlinks where applicable
- Filter: Enable auto-filter to filter by Evidence Type, Related Asset, Verification Status


**Usage Notes**:

- Every claim in assessment should have supporting evidence documented here
- Evidence ID should be referenced in other sheets (e.g., in Notes columns) to create traceability
- For audits, auditor will sample evidence from this register to verify claims
- "Verified" status means evidence was checked and is valid/accessible
- Evidence verification should be performed at least semi-annually
- Missing or Outdated evidence is a compliance gap that must be remediated
- Retention Period based on [Organization]'s retention policy and regulatory requirements


---

## Sheet 11: Approval_Sign_Off

**Purpose**: Formal three-tier approval of the baseline configuration assessment. Documents who prepared, reviewed, and approved the assessment, establishing accountability.

**Structure** (Not tabular - signature block format):

**Section A: Document Information** (Rows 3-8)

| Field | Value |
|-------|-------|
| Assessment Title | Baseline Configuration Assessment - Control A.8.9 |
| Assessment Period | [DD.MM.YYYY] to [DD.MM.YYYY] |
| Document ID | ISMS-IMP-A.8.9.1 |
| Version | 1.0 |
| Assessment Date | [Auto-filled with TODAY() when sheet created] |

**Section B: Preparer Sign-Off** (Rows 10-16)

| Field | Value |
|-------|-------|
| Preparer Name | [Free text entry] |
| Preparer Role | [Free text entry, e.g., "System Administrator"] |
| Preparer Signature | [Free text entry or "Electronically signed"] |
| Date Prepared | [Date field - DD.MM.YYYY] |
| Completeness Attestation | "I attest that the information in this assessment has been compiled accurately to the best of my knowledge and all required evidence has been collected." |

**Section C: Reviewer Sign-Off** (Rows 18-25)

| Field | Value |
|-------|-------|
| Reviewer Name | [Free text entry] |
| Reviewer Role | [Free text entry, e.g., "Configuration Manager"] |
| Reviewer Signature | [Free text entry] |
| Date Reviewed | [Date field] |
| Review Findings | [Free text entry - summary of review findings] |
| Gaps Identified | [Free text entry - list of gaps requiring remediation] |
| Review Attestation | "I have reviewed this assessment and verify that it accurately represents [Organization]'s baseline configuration status. Identified gaps have been documented for remediation." |

**Section D: Approver Sign-Off** (Rows 27-35)

| Field | Value |
|-------|-------|
| Approver Name | [Free text entry] |
| Approver Role | [Free text entry, e.g., "IT Manager" or "CISO"] |
| Approver Signature | [Free text entry] |
| Date Approved | [Date field] |
| Approval Decision | [Dropdown: "Approved", "Approved with Conditions", "Not Approved - Revisions Required"] |
| Conditions/Comments | [Free text entry - any conditions or required actions] |
| Next Assessment Due | [Date field - typically +90 or +180 days based on criticality] |
| Approver Attestation | "I approve this baseline configuration assessment and authorize any documented remediation activities to proceed. This assessment will be used for compliance reporting and audit purposes." |

**Formatting**:

- Section headers (A, B, C, D): Bold, 14pt, dark blue background (003366), white text
- Field labels: Bold, 11pt, light gray background (D9D9D9)
- Value cells: 11pt, white background (user entry area)
- Attestation text: Italic, 10pt, light blue background (E7E6E6)


**Data Validations**:

- Date fields: DD.MM.YYYY format
- Approval Decision: Dropdown ("Approved", "Approved with Conditions", "Not Approved - Revisions Required")


**Conditional Formatting**:

- Approval Decision:
  - "Approved" → Green fill (C6EFCE)
  - "Approved with Conditions" → Yellow fill (FFEB9C)
  - "Not Approved - Revisions Required" → Red fill (FFC7CE)


**Special Features**:

- All value cells (for names, dates, signatures, comments) are UNLOCKED for user entry
- All other cells (labels, attestations) are PROTECTED to prevent modification
- Print area defined to fit on single page for formal signature printing if required
- Digital signature support: If [Organization] uses digital signatures, this section can be modified to reference digital signature validation


**Usage Notes**:

- Complete this sheet LAST after all other sheets are finalized
- Preparer completes Section B after finishing data entry in all assessment sheets
- Reviewer completes Section C after verifying completeness and accuracy
- Approver completes Section D after reviewing summary metrics and deciding on approval
- If "Not Approved", document required revisions in Conditions/Comments and repeat cycle
- Signed copy (digital or printed) should be retained as part of evidence (reference in Evidence_Register)
- This sign-off demonstrates governance oversight of configuration management


---

# Data Validation Rules Summary

## Dropdown Lists

**Asset_Inventory Sheet**:

- Asset Type: 43-type taxonomy (stored in hidden "Lookup_Tables" sheet)
- Criticality: Critical, High, Medium, Low
- Baseline Status: Defined, In Progress, Not Started, N/A


**Baseline_Repository Sheet**:

- Approval Status: Approved, Pending Review, Rejected, Draft


**Approval_Tracking Sheet**:

- Approval Status: Pending Submission, Submitted, Under Review, Approved, Rejected, Revisions Requested
- Approval Method: Change Advisory Board, Email Approval, Manager Sign-Off, Governance Committee, Automated Process
- Risk Assessment: Low, Medium, High


**Documentation_Assessment Sheet**:

- Documentation Completeness: Comprehensive, Adequate, Insufficient, Missing
- Documentation Accuracy: Verified Accurate, Mostly Accurate, Contains Errors, Not Verified
- Maintainability: Easy to Update, Moderate Effort, Difficult, Not Maintainable
- Accessibility: Highly Accessible, Accessible, Limited Access, Not Accessible
- Remediation Priority: Critical, High, Medium, Low


**Version_Control Sheet**:

- Change Type: Initial Release, Minor Update, Major Update, Security Patch, Emergency Change, Rollback


**Deviation_Register Sheet**:

- Deviation Type: Configuration Exception, Exclusion from Baseline, Temporary Deviation, Permanent Exception
- Risk Assessment: Low, Medium, High, Critical
- Review Frequency: Monthly, Quarterly, Semi-Annual, Annual
- Deviation Status: Active, Under Review, Expired, Revoked, No Longer Needed


**Evidence_Register Sheet**:

- Evidence Type: Screenshot, Configuration File, Scan Report, Approval Record, Meeting Minutes, Email, Document, System Export, Video Recording, Audit Log, Other
- Evidence Classification: Public, Internal, Confidential, Restricted
- Retention Period: 1 Year, 3 Years, 5 Years, 7 Years, Indefinite
- Verification Status: Verified, Needs Verification, Missing, Outdated


**Approval_Sign_Off Sheet**:

- Approval Decision: Approved, Approved with Conditions, Not Approved - Revisions Required


## Date Format

All date fields use **DD.MM.YYYY** format (European standard, as requested).

Date fields include:

- Last Reviewed Date, Next Review Due (Asset_Inventory)
- Approval Date, Last Updated (Baseline_Repository)
- Submission Date, Approval Date (Approval_Tracking)
- Version Date, Superseded Date (Version_Control)
- Approval Date, Review Date, Expiration Date (Deviation_Register)
- Evidence Date, Last Verified Date (Evidence_Register)
- Date Prepared, Date Reviewed, Date Approved, Next Assessment Due (Approval_Sign_Off)


## Number Validations

- Configuration Elements Count (Baseline_Repository): Whole numbers, 0-999
- Days Pending (Approval_Tracking): Calculated field, no manual entry
- All Score fields (Documentation_Assessment): Calculated, 0-100 range
- Assets Affected Count (Version_Control): Whole numbers


## Required vs Optional Fields

**Required Fields** (Allow Blank = No):

- Asset ID, Asset Type, Criticality, Baseline Status (Asset_Inventory)
- Baseline ID, Baseline Name, Approval Status (Baseline_Repository)
- All dropdown fields in Documentation_Assessment
- Deviation Type, Risk Assessment, Review Frequency, Status (Deviation_Register)
- Evidence Type, Classification, Retention Period, Verification Status (Evidence_Register)


**Optional Fields** (Allow Blank = Yes):

- Notes columns across all sheets
- Approval Date (until approved)
- Expiration Date (if not temporary deviation)


---

# Compliance Scoring Methodology

## Overall Baseline Coverage Calculation
```
Overall Coverage % = (Assets with Defined Baselines / Total In-Scope Assets) × 100

Where:

- Assets with Defined Baselines = COUNT(Asset_Inventory.Baseline_Status = "Defined")
- Total In-Scope Assets = COUNT(All Assets) - COUNT(Asset_Inventory.Baseline_Status = "N/A")
- Excluded assets (Baseline Status = "N/A") do not count against coverage


Target: ≥85% overall coverage
```

## Criticality-Based Coverage Targets

| Criticality Level | Target Coverage | Compliance Threshold |
|-------------------|----------------|---------------------|
| Critical | ≥95% | Red if <90%, Yellow if 90-94%, Green if ≥95% |
| High | ≥90% | Red if <85%, Yellow if 85-89%, Green if ≥90% |
| Medium | ≥80% | Red if <70%, Yellow if 70-79%, Green if ≥80% |
| Low | ≥60% | Red if <50%, Yellow if 50-59%, Green if ≥60% |

**Rationale**: 

- Critical assets pose highest business risk if misconfigured → highest baseline requirement
- Low criticality assets have flexibility but still need basic configuration management
- These thresholds align with industry best practices (CIS, NIST guidelines)


## Documentation Quality Scoring

**Four Quality Dimensions** (each scored 0-100):

1. **Completeness** (Weight: 25%)

   - Comprehensive = 100 (all config elements documented in detail)
   - Adequate = 75 (core elements documented, minor gaps)
   - Insufficient = 40 (significant gaps)
   - Missing = 0 (no documentation)


2. **Accuracy** (Weight: 25%)

   - Verified Accurate = 100 (documentation matches actual config)
   - Mostly Accurate = 75 (minor discrepancies)
   - Contains Errors = 40 (significant inaccuracies)
   - Not Verified = 0 (accuracy unknown)


3. **Maintainability** (Weight: 25%)

   - Easy to Update = 100 (well-structured, version controlled)
   - Moderate Effort = 75 (updateable but requires effort)
   - Difficult = 40 (hard to update, risk of errors)
   - Not Maintainable = 0 (cannot be updated)


4. **Accessibility** (Weight: 25%)

   - Highly Accessible = 100 (central repository, searchable)
   - Accessible = 75 (available but may need access request)
   - Limited Access = 40 (only few can access)
   - Not Accessible = 0 (location unknown or severely restricted)


**Overall Quality Score**:
```
Quality Score = (Completeness + Accuracy + Maintainability + Accessibility) / 4

Rating:

- Excellent: ≥90
- Good: 75-89
- Fair: 50-74
- Poor: <50


Target: ≥75% of baselines should have "Good" or "Excellent" rating
```

## Approval Process Health Metrics

**Average Approval Time**:
```
Average = SUM(Days from Submission to Approval) / COUNT(Approved Baselines)

Target: <14 days (2 weeks)
Status:

- Green if <14 days
- Yellow if 14-21 days
- Red if >21 days

```

**SLA Compliance**:
```
SLA Compliance % = (Baselines Approved Within SLA / Total Baselines Submitted) × 100

SLA = 14 days from submission to approval decision

Target: ≥90% SLA compliance
```

**Approval Success Rate**:
```
Success Rate = (Approved Baselines / (Approved + Rejected Baselines)) × 100

Target: >90%

Note: High rejection rate may indicate:

- Poor baseline quality during initial submission
- Insufficient preparation before submission
- Unrealistic approval criteria (may need adjustment)

```

## Deviation Risk Assessment

**Risk-Weighted Deviation Count**:
```
Risk Score = (Critical Deviations × 4) + (High Deviations × 3) + (Medium Deviations × 2) + (Low Deviations × 1)

Thresholds:

- Green: Risk Score <20
- Yellow: Risk Score 20-50
- Red: Risk Score >50


Target: Minimize high/critical risk deviations; ensure compensating controls in place
```

**Deviation Coverage**:
```
Deviation Rate % = (Assets with Active Deviations / Total Assets with Baselines) × 100

Target: <10%

High deviation rate may indicate:

- Baselines are not practical/realistic (need revision)
- Significant technical debt
- Poor change control discipline

```

## Compliance Status Determination

**Control A.8.9 Baseline Configuration Compliance**:
```
IF Critical Coverage ≥95% AND High Coverage ≥90% AND Overall Coverage ≥85%:
    Status = "COMPLIANT"
ELSE IF Critical Coverage ≥90% AND High Coverage ≥85% AND Overall Coverage ≥75%:
    Status = "PARTIALLY COMPLIANT"
ELSE:
    Status = "NON-COMPLIANT"

Additional Factors:

- Documentation quality: ≥60% of baselines should have "Good" or better rating
- Active High/Critical risk deviations: <5
- Approval process: No SLA breaches >30 days


Final Assessment:

- Compliant = All criteria met → Green status
- Partially Compliant = Minor gaps, remediation plan exists → Yellow status
- Non-Compliant = Significant gaps, immediate action required → Red status

```

---

# Usage Instructions

## Step-by-Step Completion Guide

**Phase 1: Preparation** (Day 1)
1. Configuration Manager assigns assessment to team
2. Review Instructions sheet
3. Identify all team members who will complete sections
4. Set timeline: typically 2-3 weeks for initial assessment

**Phase 2: Asset Inventory** (Days 2-5)
1. Export asset list from CMDB if available, or compile manually
2. Populate Asset_Inventory sheet (columns A-C, E-G)
3. For each asset, determine if baseline is Defined, In Progress, Not Started, or N/A
4. Document Baseline Reference (Column I) if baseline exists
5. Update Last Reviewed Date for existing baselines

**Phase 3: Baseline Documentation** (Days 6-10)
1. Populate Baseline_Repository sheet with all configuration baselines
2. For each baseline, document:

   - Version, applicable asset types, approval status
   - Documentation location (critical for audit)
   - Configuration elements count (how comprehensive is baseline)

3. Cross-reference Baseline IDs between Asset_Inventory and Baseline_Repository

**Phase 4: Approval and Quality Assessment** (Days 11-14)
1. Complete Approval_Tracking sheet for baselines in approval process
2. Configuration Manager completes Documentation_Assessment sheet

   - Review actual documentation
   - Score on four quality dimensions
   - Identify gaps for remediation

3. Update Version_Control sheet with baseline version history
4. Document any deviations in Deviation_Register

**Phase 5: Evidence Collection** (Days 15-18)
1. Compile all supporting evidence
2. Document each piece of evidence in Evidence_Register
3. Ensure evidence is accessible for audit
4. Verify evidence classification and retention periods

**Phase 6: Review and Approval** (Days 19-21)
1. Review Metrics_Summary sheet - identify gaps
2. Preparer completes Approval_Sign_Off (Section B)
3. Reviewer (Configuration Manager) verifies assessment (Section C)
4. Approver (IT Manager/CISO) reviews and approves (Section D)
5. If "Not Approved", revise and repeat

## Roles and Responsibilities

**Preparer (System Administrators, Asset Owners)**:

- Complete Asset_Inventory sheet for assigned assets
- Gather baseline documentation
- Collect evidence
- Populate Evidence_Register
- Complete Preparer sign-off


**Reviewer (Configuration Manager, Team Leads)**:

- Verify completeness of Asset_Inventory
- Complete Documentation_Assessment (quality scoring)
- Review Approval_Tracking status
- Validate Deviation_Register entries
- Identify remediation priorities
- Complete Reviewer sign-off


**Approver (IT Manager, CISO, Governance Committee)**:

- Review Metrics_Summary for overall compliance status
- Assess remediation plans for identified gaps
- Approve assessment or request revisions
- Authorize remediation activities
- Complete Approver sign-off


## Common Questions and Troubleshooting

**Q: What if we don't have a CMDB - how do we populate Asset_Inventory?**
A: Manually compile asset list from:

- Network scanning tools (Nmap, network inventory tools)
- Server/endpoint management consoles
- Cloud provider consoles (AWS, Azure, GCP)
- Application inventory from IT Service Management system
- Physical asset inventory records


**Q: How detailed should baselines be?**
A: Baselines should document:

- All security-relevant configuration parameters
- Service configurations (enabled/disabled services)
- User accounts and access controls
- Network settings (IP, firewall rules, ports)
- Installed software and versions
- Security hardening settings

Detail level depends on asset criticality - Critical assets need comprehensive baselines.

**Q: What if a baseline was approved verbally - how do we document?**
A: Verbal approvals should be:

- Documented in meeting minutes (add to Evidence_Register)
- Followed up with email confirmation (add to Evidence_Register)
- Retroactively formalized through proper approval workflow

Verbal-only approvals are not sufficient for audit purposes.

**Q: Can we have one baseline apply to multiple asset types?**
A: Yes, example: "Linux Server Standard Build" can apply to multiple Linux distributions.
Document in Baseline_Repository Column D (Applicable Asset Types): "Physical Server, Virtual Machine"

**Q: What if an asset needs multiple baselines?**
A: Some assets may need layered baselines:

- OS baseline (Windows Server 2022 Standard)
- Application baseline (IIS Web Server Configuration)
- Security baseline (CIS Benchmark Level 1)

Document all applicable baselines in Asset_Inventory Column I (comma-separated) or create separate rows.

**Q: How often should baselines be reviewed?**
A: Review frequency based on criticality:

- Critical/High assets: Quarterly (every 90 days)
- Medium/Low assets: Semi-annually (every 180 days)
- Also review when: major OS updates, security vulnerabilities discovered, significant config drift detected


**Q: What constitutes a valid deviation?**
A: Valid deviations require:

- Clear business justification (technical requirement, vendor limitation, legacy compatibility)
- Risk assessment (understand security impact)
- Compensating controls (if high/critical risk)
- Appropriate approval (manager/CISO depending on risk)
- Regular review (to determine if still needed)


## Integration with Other Processes

**Integration with Change Control (ISMS-IMP-A.8.9.2)**:

- When baseline is updated, create change request
- After change is approved and implemented, update Version_Control sheet
- New baseline version triggers re-assessment of affected assets


**Integration with Configuration Monitoring (ISMS-IMP-A.8.9.3)**:

- Baselines define "expected state" for drift detection
- Drift alerts trigger review of Asset_Inventory and Deviation_Register
- Frequent drift on same asset may indicate baseline needs revision


**Integration with Security Hardening (ISMS-IMP-A.8.9.4)**:

- Hardening standards are incorporated into baselines
- Hardening assessment results inform baseline updates
- Non-compliance with hardening standards may require deviation documentation


**Integration with Asset Inventory (A.5.9)**:

- Asset_Inventory sheet should align with organization's asset register
- Asset criticality classification comes from asset inventory process
- Baseline status feeds back into asset inventory as attribute


---

# Integration Points with Other Assessments

## Cross-Assessment Dependencies

| This Assessment | Integrates With | Integration Mechanism | Data Flow |
|----------------|----------------|----------------------|-----------|
| Asset_Inventory sheet | ISMS-IMP-A.8.9.2 (Change Control) | Changes to baselines trigger version updates | Bidirectional: Asset list → Change requests for baseline updates |
| Baseline_Repository | ISMS-IMP-A.8.9.3 (Config Monitoring) | Baselines define expected state for drift detection | Unidirectional: Baselines → Monitoring tools |
| Deviation_Register | ISMS-IMP-A.8.9.4 (Security Hardening) | Deviations may be security hardening exceptions | Bidirectional: Hardening gaps ↔ Approved deviations |
| Documentation_Assessment | ISMS-IMP-A.8.9.5 (Compliance Dashboard) | Quality scores feed into overall compliance | Unidirectional: Quality metrics → Dashboard |
| All sheets | A.5.9 (Asset Inventory) | Asset list must align with organizational asset register | Bidirectional: Asset data synchronized |

## Data Export Requirements

For integration with ISMS-IMP-A.8.9.5 (Compliance Dashboard), the following data must be extractable:

**Key Metrics to Export**:

- Overall Baseline Coverage % (from Metrics_Summary)
- Critical Asset Coverage % (from Metrics_Summary)
- High Asset Coverage % (from Metrics_Summary)
- Count of assets with baselines vs. total (from Asset_Inventory)
- Count of baselines pending approval (from Approval_Tracking)
- Count of High/Critical risk deviations (from Deviation_Register)
- Average documentation quality score (from Documentation_Assessment)
- Approval process health (average days, SLA compliance) (from Approval_Tracking)


**Export Format**: 

- Dashboard script will read this workbook directly using openpyxl
- Key cells referenced by name (e.g., Metrics_Summary!B5 for Overall Coverage %)
- Alternatively, create hidden "Export_Data" sheet with pre-calculated values for dashboard extraction


## CMDB Integration (if applicable)

If [Organization] maintains a Configuration Management Database (CMDB):

**Import from CMDB**:

- Asset inventory (Asset ID, Name, Type, Location, Owner)
- Asset criticality classifications
- Current baseline references (if tracked in CMDB)


**Export to CMDB**:

- Baseline status (Defined/In Progress/Not Started)
- Last reviewed dates
- Deviation status (for assets with active deviations)


**Synchronization Approach**:

- Initial assessment: Import asset list from CMDB
- Ongoing: Periodic sync (weekly/monthly) to keep aligned
- Trigger: Configuration changes in CMDB trigger update to this assessment


---

# Evidence Collection Guidelines

## Required Evidence Types

For audit verification, the following evidence types should be collected:

**1. Asset Inventory Evidence**:

- CMDB export or network scan results (proves asset list is complete)
- Asset classification documentation (proves criticality assignments)
- Asset ownership assignments (proves accountability)


**2. Baseline Documentation Evidence**:

- Configuration baseline documents (detailed config specifications)
- Configuration templates or scripts (for automated deployment)
- Baseline approval records (meeting minutes, email approvals, change tickets)


**3. Approval Workflow Evidence**:

- Change Advisory Board meeting minutes
- Email approval threads
- Governance committee decisions
- Change request tickets with approval history


**4. Quality Assessment Evidence**:

- Screenshots of actual configurations vs. baseline documentation (proves accuracy)
- Baseline review reports (proves regular review)
- Documentation audit findings (internal quality checks)


**5. Deviation Evidence**:

- Deviation request forms with business justification
- Risk assessment documentation for deviations
- Compensating control documentation (for high-risk deviations)
- Deviation review meeting minutes


**6. Version Control Evidence**:

- Baseline version history logs
- Change request records for baseline updates
- Before/after configuration comparisons


## Evidence Quality Standards

**Good Evidence Characteristics**:

- **Timestamped**: Clear date/time of when evidence was created
- **Attributable**: Shows who created/approved (names, signatures)
- **Authentic**: Original or verified copy, not easily fabricated
- **Accessible**: Stored in retrievable location, properly indexed
- **Retained**: Kept for required retention period (typically 3+ years for ISO 27001)


**Poor Evidence Examples**:

- Undated screenshots (no way to verify when captured)
- Verbal approvals with no documentation (not verifiable)
- Evidence stored on individual laptops (not accessible for audit)
- Evidence in personal email only (may be deleted, not formally retained)


## Evidence Repository Structure

**Recommended Folder Structure**:
```
Evidence/
├── ISMS-A.8.9-Baseline-Configuration/
│   ├── Asset-Inventory/
│   │   ├── CMDB-Export-YYYYMMDD.xlsx
│   │   ├── Network-Scan-Results-YYYYMMDD.pdf
│   │   └── Asset-Criticality-Classifications.pdf
│   ├── Baseline-Documentation/
│   │   ├── BL-WIN2022-STD-001-v2.1.docx
│   │   ├── BL-RHEL9-SEC-001-v1.3.pdf
│   │   └── ...
│   ├── Approval-Records/
│   │   ├── CAB-Meeting-Minutes-YYYYMMDD.pdf
│   │   ├── Email-Approval-Baseline-XYZ.pdf
│   │   └── ...
│   ├── Configuration-Snapshots/
│   │   ├── Server-Config-WebServer01-YYYYMMDD.txt
│   │   ├── Firewall-Rules-Export-YYYYMMDD.xml
│   │   └── ...
│   ├── Deviation-Documentation/
│   │   ├── Deviation-Request-DEV-2024-001.pdf
│   │   ├── Risk-Assessment-DEV-2024-001.pdf
│   │   └── ...
│   └── Assessment-Reports/
│       ├── Baseline-Assessment-YYYYMMDD.xlsx (this workbook)
│       ├── Assessment-Summary-Presentation.pptx
│       └── Evidence-Register-Index.pdf
```

## Evidence Sampling for Audits

**Auditor Will Typically Sample**:

- 5-10 Critical assets: Verify baseline exists, is documented, is applied
- 3-5 baselines: Review documentation quality, approval records
- 2-3 deviations: Verify justification, risk assessment, compensating controls
- 1-2 recent baseline updates: Trace through change control to version control
- Approval process: Review 2-3 approval records for completeness


**Preparation for Audit**:

- Ensure Evidence_Register is complete and up-to-date
- Verify all evidence links are accessible
- Pre-pull commonly requested evidence (saves time during audit)
- Review evidence for completeness (no missing signatures, dates, etc.)


## Evidence Verification Process

**Semi-Annual Evidence Verification** (recommended):
1. Review all entries in Evidence_Register
2. For each piece of evidence:

   - Verify file/document still exists and is accessible
   - Check if evidence is still valid (not outdated)
   - Update "Last Verified Date" column
   - Update "Verification Status" if issues found

3. For "Missing" or "Outdated" evidence:

   - Attempt to locate or recreate evidence
   - If cannot be recreated, document gap and remediation plan
   - Update Asset_Inventory or other sheets if baseline status changes due to missing evidence


**Continuous Evidence Management**:

- When new evidence is collected, immediately add to Evidence_Register
- When baseline is updated, archive old evidence and link new evidence
- When evidence reaches retention period end, review before destruction (some may need extension for ongoing issues)


---

# Document Maintenance and Updates

## Update Triggers

This assessment workbook should be updated when:

- **Quarterly**: Regular refresh for Critical/High assets
- **Semi-Annually**: Regular refresh for Medium/Low assets
- **Ad-Hoc**: Significant infrastructure changes (data center migration, cloud transformation, major application deployment)
- **Post-Incident**: After security incidents involving configuration issues
- **Audit Preparation**: Prior to internal or external audits
- **Policy Updates**: When ISMS-POL-A.8.9 is revised


## Version Control

**Workbook Versioning**:

- File naming convention: `ISMS_A_8_9_1_Baseline_Configuration_Assessment_YYYYMMDD.xlsx`
- Date in filename = Assessment completion date
- Retain previous versions for at least 3 years (audit trail)
- Store in version-controlled repository if available (SharePoint, Git, document management system)


**Change Log** (maintain in Instructions sheet or separate tab):
| Version | Date | Changes Made | Changed By |
|---------|------|--------------|------------|
| 1.0 | DD.MM.YYYY | Initial baseline assessment | [Name] |
| 1.1 | DD.MM.YYYY | Added 15 new cloud assets | [Name] |
| 2.0 | DD.MM.YYYY | Quarterly refresh, updated all sheets | [Name] |

## Annual Review Process

**Configuration Manager Responsibilities** (Annual):
1. Review all baselines for continued relevance
2. Verify documentation quality standards are still appropriate
3. Update asset taxonomy if new asset types introduced
4. Review deviation register - determine if long-standing deviations should become new baseline variants
5. Assess whether target coverage percentages need adjustment based on organizational maturity
6. Update evidence retention periods if regulatory requirements change
7. Brief management on annual trends (improving or declining baseline coverage)

---

# Specification Approval

**Document Owner**: Configuration Manager  
---

*Where bamboo antennas actually work.* 🎋
