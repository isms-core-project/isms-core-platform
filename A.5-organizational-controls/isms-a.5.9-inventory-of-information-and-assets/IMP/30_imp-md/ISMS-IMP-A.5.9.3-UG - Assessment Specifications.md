**ISMS-IMP-A.5.9.3-UG - Quality & Compliance Assessment**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.5.9: Inventory of Information and Other Associated Assets

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.9.3-UG |
| **Version** | 1.0 |
| **Assessment Area** | Inventory Quality & Policy Compliance Verification |
| **Related Policy** | ISMS-POL-A.5.9, Section 2.3 (Mandatory Attributes), Section 2.5 (Quality Standards), Section 3 (Assessment Methodology) |
| **Purpose** | Verify inventory data quality (accuracy, completeness, currency) and compliance with policy requirements |
| **Target Audience** | Security Team, Quality Assurance, CMDB Administrators, Auditors |
| **Assessment Type** | Quality Verification & Compliance Audit |
| **Review Cycle** | Quarterly |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|--------|--------|
| 1.0 | [Date] | Initial assessment specification following consolidated policy structure | ISMS Implementation Team |

### Document Structure

This is the **User Completion Guide**. The companion Technical Specification is documented in ISMS-IMP-A.5.9.3-TG.

---

**Audience:** Security Team, Quality Assurance, CMDB Administrators, Auditors

---

## Assessment Overview

### What This Assessment Evaluates

This assessment verifies that the asset inventory meets quality standards and policy compliance requirements. Unlike IMP-A.5.9-1 (Discovery) and IMP-A.5.9-2 (Maintenance), this assessment focuses on VERIFICATION:

**Key Questions This Assessment Answers**:

- Is the inventory data ACCURATE? (matches reality)
- Is the inventory data COMPLETE? (all required fields populated)
- Is the inventory data CURRENT? (not stale)
- Does the inventory COMPLY with policy requirements?
- Where are the quality GAPS? (what needs improvement)

**Assessment Philosophy**: Trust, but verify. Don't assume inventory is accurate just because it exists. Sample and validate.

### Why This Matters

This assessment verifies [Organization]'s compliance with:

- **ISO/IEC 27001:2022 Control A.5.9**: "Rules related to **acceptable use** and return of assets should be identified and **implemented**"
- **ISMS-POL-A.5.9, Section 2.5**: Quality standards (accuracy ≥95% for information assets, ≥98% for IT infrastructure)
- **ISMS-POL-A.5.9, Section 2.5.3**: Currency standards (maximum staleness by criticality)
- **ISMS-POL-A.5.9, Section 3.2**: Assessment methodology requirements

**From Implementer Perspective**: Identifies data quality issues requiring remediation.

**From Auditor Perspective**: Provides objective evidence that inventory meets quality standards and policy requirements.

### Assessment Domains

This assessment covers **5 quality dimensions**:

| Dimension | Focus | Policy Requirement |
|-----------|-------|-------------------|
| **1. Accuracy** | Does inventory match reality? | ≥95% (Info Assets), ≥98% (IT Infrastructure), ≥90% (Physical), 100% (Personnel) |
| **2. Completeness** | Are mandatory attributes populated? | 100% mandatory attributes populated |
| **3. Currency** | Is data up-to-date (not stale)? | Per criticality: Critical daily, High 3 days, Standard 7 days, Low 30 days |
| **4. Consistency** | Is data internally consistent? | No contradictions (e.g., status=Retired but still in production) |
| **5. Policy Compliance** | Does inventory meet all policy requirements? | 100% compliance with SHALL requirements |

### Assessment Outputs

**Generated Workbook**: `ISMS_A_5_9_Quality_Compliance_Assessment_YYYYMMDD.xlsx`

**Sheets** (8 total):
1. **Instructions**: How to complete this assessment
2. **Accuracy Sampling**: Sample assets and verify accuracy
3. **Completeness Assessment**: Check mandatory attribute population
4. **Currency Assessment**: Check staleness against policy thresholds
5. **Consistency Checks**: Identify contradictions and anomalies
6. **Policy Compliance Matrix**: Verify against all SHALL requirements
7. **Quality Metrics & Scoring**: Aggregate quality scores and compliance status
8. **Evidence Register**: Sample records, verification evidence, test results

**Compliance Metrics Generated**:

- Overall quality score (weighted average of 5 dimensions)
- Accuracy rate by asset category
- Completeness percentage (mandatory attributes)
- Currency compliance (% within staleness thresholds)
- Policy compliance percentage (% of SHALL requirements met)

---

## Prerequisites

### What You Need Before Starting

**1. Completed Assessments**:

- **ISMS-IMP-A.5.9.1**: Asset Discovery (know what's supposed to be inventoried)
- **ISMS-IMP-A.5.9.2**: Inventory Maintenance (know where inventory data lives)

**2. Access to Inventory and Source Systems**:

- Read access to inventory system(s)
- Access to source systems for verification (CMDB, HR, procurement)
- Access to physical assets (for physical verification if applicable)
- Network access for IT infrastructure validation

**3. Personnel**:

- **Security Team**: Leads assessment, performs sampling
- **CMDB Administrator**: Assists with data queries
- **System Owners**: Validates accuracy of sampled assets
- **QA/Audit Team**: Provides independent verification (if available)

**4. Tools**:

- Inventory system query/export capability
- Random sampling tool (Excel RAND(), Python random.sample, or statistical software)
- Verification tools (network scanners, asset discovery tools)
- Comparison tools (for consistency checks)

**5. Documentation**:

- ISMS-POL-A.5.9 (reference for requirements)
- Inventory data model/schema (from IMP-A.5.9-2)
- Previous quality assessment (if exists - for trending)

**6. Time Allocation**:

- **Initial Assessment**: 20-30 hours (extensive sampling)
- **Quarterly Updates**: 8-12 hours (smaller sample, focused checks)
- **Evidence Collection**: 4-6 hours per quarter

---

## Assessment Workflow

### Step-by-Step Process

```
Phase 1: Preparation & Sampling (Day 1-2)
├─ Define sample size and stratification
├─ Generate random sample for accuracy testing
├─ Export inventory data for analysis
└─ Prepare verification procedures

Phase 2: Accuracy Assessment (Day 3-6)
├─ Verify sampled assets against reality
├─ Document discrepancies
├─ Calculate accuracy rates by category
└─ Identify patterns in errors

Phase 3: Completeness Assessment (Day 7-8)
├─ Check mandatory attribute population
├─ Identify missing fields
├─ Calculate completeness percentage
└─ Categorize gaps (systemic vs. isolated)

Phase 4: Currency Assessment (Day 9-10)
├─ Check LastUpdated dates against policy thresholds
├─ Identify stale records by criticality
├─ Calculate currency compliance percentage
└─ Prioritize refresh actions

Phase 5: Consistency Checks (Day 11-12)
├─ Run automated consistency checks
├─ Identify contradictions and anomalies
├─ Investigate root causes
└─ Document inconsistencies

Phase 6: Policy Compliance Verification (Day 13-15)
├─ Verify against each SHALL requirement
├─ Document evidence of compliance
├─ Identify non-compliance gaps
└─ Categorize severity (Critical, High, Medium, Low)

Phase 7: Metrics & Reporting (Day 16-18)
├─ Calculate quality scores
├─ Generate compliance summary
├─ Identify remediation priorities
├─ Document evidence register
└─ Prepare executive summary

Phase 8: Review & Approval (Day 19-20)
├─ Quality check against checklist
├─ Security Team review
├─ CISO approval
└─ Submit to compliance dashboard
```

**Timeline**: 20 working days for initial assessment, 8-12 days for quarterly updates

---

## Completing Each Sheet

### Sheet 1: Instructions

**Purpose**: Provides overview and guidance for completing this workbook.

**What to Do**:

- Read the instructions completely before starting
- Understand the 5 quality dimensions being assessed
- Review the sampling methodology
- Note the scoring criteria

**No data entry required** - informational only.

---

### Sheet 2: Accuracy Sampling

**Purpose**: Sample inventory records and verify accuracy against reality.

**What This Sheet Captures**:

- Random sample of inventory records
- Verification results (accurate vs. inaccurate)
- Specific discrepancies found
- Root cause analysis
- Accuracy rates by asset category

**Sampling Methodology**:

**Sample Size Calculation**:

- Use statistical sampling (95% confidence, ±5% margin of error)
- **CRITICAL: Minimum 30 samples PER CATEGORY for statistical validity**
  - This is a hard minimum - smaller samples cannot make valid statistical claims about category accuracy
  - If a category has fewer than 30 assets, sample 100% of that category
- Overall minimum sample sizes (across all categories):
  - Small inventory (<100 assets total): All records (100% sampling)
  - Medium inventory (100-500 assets): 100-150 records
  - Large inventory (>500 assets): 150-250 records
- Stratify by asset category (with n=30 minimum floor per category)

**Stratification Example** (with n=30 minimum per category):
```
Total Inventory: 1,500 assets
├─ Information Assets: 400 (27%) → Sample 40 (proportional)
├─ IT Infrastructure: 600 (40%) → Sample 60 (proportional)
├─ Applications: 300 (20%) → Sample 30 (minimum met)
├─ Physical Assets: 150 (10%) → Sample 30 (minimum floor applied, not 15)
└─ Personnel Assets: 50 (3%) → Sample 30 (minimum floor applied, not 5)
                                 ─────────
Total Sample: 190 assets (not 150, due to minimum floors)
```

**Note**: The n=30 minimum per category ensures statistically valid accuracy statements can be made for EACH asset category individually. Without this minimum, accuracy rates per category are unreliable.

**Random Selection**:

- Use Excel `=RAND()` function or Python `random.sample()`
- No cherry-picking! True random selection required for statistical validity
- Generate random sample within each category stratum separately

**Column Definitions**:

| Column | Purpose | How to Complete |
|--------|---------|-----------------|
| **Sample ID** | Unique identifier for sample | Format: QA-NNN (QA-001, QA-002, etc.) |
| **Asset Category** | Type of asset | From inventory (Info, IT, App, Physical, Personnel) |
| **Asset ID** | Inventory asset identifier | From inventory |
| **Asset Name** | Asset name from inventory | From inventory |
| **Attribute to Verify** | Which attribute being checked | Free text: e.g., "Owner", "Location", "Status", "Classification" |
| **Inventory Value** | Value in inventory system | Copy from inventory |
| **Actual Value** | Value from verification | Result of verification (reality check) |
| **Match?** | Do they match? | Dropdown: Yes (Accurate) / No (Inaccurate) / Cannot Verify |
| **Discrepancy Type** | If no match, what's wrong? | Dropdown: Wrong Value / Outdated / Missing / Duplicate / Other |
| **Impact** | Severity of discrepancy | Dropdown: Critical / High / Medium / Low / Informational |
| **Root Cause** | Why discrepancy exists | Free text: Analysis of cause |
| **Verification Method** | How verified | Free text: e.g., "Network scan", "Owner confirmation", "Physical inspection" |
| **Verification Date** | When verified | Date field |
| **Verified By** | Who verified | Free text: Name/role |
| **Notes** | Additional context | Free text |

**How to Complete**:

**Step 1: Generate Sample**

1. Export full inventory to Excel/CSV
2. Assign random numbers to each record
3. Sort by random number
4. Select top N records per category (stratified sample)
5. Document sample in this sheet (rows 3+)

**Step 2: Verify Each Sample Record**

**Example 1: IT Infrastructure - Server**

- **Sample ID**: QA-001
- **Asset Category**: IT Infrastructure
- **Asset ID**: SRV-12345
- **Asset Name**: prod-db-01.company.com
- **Attribute to Verify**: Status
- **Inventory Value**: Active - Production
- **Actual Value**: Retired (server decommissioned 2 months ago per change ticket CHG-98765)
- **Match?**: No (Inaccurate)
- **Discrepancy Type**: Outdated
- **Impact**: High (retired server still shown as production, security risk if access not revoked)
- **Root Cause**: Decommission procedure doesn't include inventory update step
- **Verification Method**: Network scan (server not responding), change management ticket review
- **Verification Date**: [Date]
- **Verified By**: Security Team

**Example 2: Information Asset - Database**

- **Sample ID**: QA-002
- **Asset Category**: Information Assets
- **Asset ID**: DB-00456
- **Asset Name**: Customer Database (CRM)
- **Attribute to Verify**: Owner
- **Inventory Value**: John Smith
- **Actual Value**: Jane Doe (John transferred to different department 6 months ago, Jane is current owner)
- **Match?**: No (Inaccurate)
- **Discrepancy Type**: Outdated
- **Impact**: Medium (owner is contactable but incorrect, affects accountability)
- **Root Cause**: Owner transfer process didn't update inventory
- **Verification Method**: Email confirmation from Jane Doe
- **Verification Date**: 22.01.2026
- **Verified By**: Information Security Manager

**Example 3: Application - SaaS**

- **Sample ID**: QA-003
- **Asset Category**: Applications
- **Asset ID**: APP-00789
- **Asset Name**: Salesforce CRM
- **Attribute to Verify**: License Count
- **Inventory Value**: 250 licenses
- **Actual Value**: 250 licenses (verified via Salesforce admin console)
- **Match?**: Yes (Accurate)
- **Discrepancy Type**: N/A
- **Impact**: N/A
- **Root Cause**: N/A
- **Verification Method**: Salesforce admin console screenshot
- **Verification Date**: 22.01.2026
- **Verified By**: IT Operations

**Example 4: Physical Asset - Cannot Verify**

- **Sample ID**: QA-004
- **Asset Category**: Physical Assets
- **Asset ID**: MEDIA-00123
- **Asset Name**: Backup Tape LTO-8 #0123
- **Attribute to Verify**: Location
- **Inventory Value**: Offsite Storage - Iron Mountain Vault A
- **Actual Value**: Cannot verify (offsite vault, no immediate access)
- **Match?**: Cannot Verify
- **Discrepancy Type**: N/A
- **Impact**: N/A
- **Root Cause**: N/A
- **Verification Method**: Requested verification from Iron Mountain (pending response)
- **Verification Date**: 22.01.2026
- **Verified By**: Security Team
- **Notes**: Follow up with Iron Mountain, escalate if no response within 1 week

**Step 3: Calculate Accuracy Rates**

Sheet will auto-calculate:

- Overall accuracy rate: (Accurate / Total Verifiable) × 100%
- Accuracy rate per category
- Discrepancy breakdown by type
- Impact distribution

**Accuracy Targets (from policy)**:

- Information Assets: ≥95%
- IT Infrastructure: ≥98%
- Applications: ≥90%
- Physical Assets: ≥90%
- Personnel Assets: 100%

**Common Pitfalls**:

- ❌ Sampling only "easy to verify" assets (introduces bias)
- ✅ True random sampling, verify whatever the sample selects
- ❌ Marking "Cannot Verify" as inaccurate (skews results)
- ✅ Exclude "Cannot Verify" from accuracy calculation (separate category)
- ❌ Not documenting verification method
- ✅ Clear documentation of HOW each sample was verified (audit trail)

---

### Sheet 3: Completeness Assessment

**Purpose**: Verify that mandatory attributes are populated per policy requirements.

**What This Sheet Captures**:

- Mandatory attributes per asset category (from policy Section 2.3)
- Population rate for each attribute
- Missing data counts
- Completeness percentage by category

**Column Definitions**:

| Column | Purpose | How to Complete |
|--------|---------|-----------------|
| **Asset Category** | Type of asset | Dropdown: Info, IT, App, Physical, Personnel, All |
| **Mandatory Attribute** | Required field name | From policy Section 2.3 |
| **Policy Requirement** | Requirement code | Reference to policy (e.g., "A.5.9-R3") |
| **Total Records** | Count of assets in category | Auto-calculated or manual entry |
| **Records with Attribute** | Count with field populated | Auto-calculated or manual entry |
| **Missing Count** | Records missing this attribute | Formula: Total - Populated |
| **Completeness %** | Percentage populated | Formula: (Populated / Total) × 100% |
| **Compliance Status** | Met target or not | Auto-calculated: Pass ≥100%, Fail <100% |
| **Gap Severity** | If missing, how bad? | Dropdown: Critical / High / Medium / Low |
| **Root Cause** | Why missing? | Free text: Analysis |
| **Remediation Plan** | How to fix | Free text: Action plan |
| **Target Date** | When to fix by | Date field |
| **Responsible Party** | Who will fix | Free text: Team/role |
| **Evidence Reference** | Link to evidence | Reference to Evidence Register |
| **Notes** | Additional context | Free text |

**How to Complete**:

**Step 1: List Mandatory Attributes**

From ISMS-POL-A.5.9 Section 2.3, mandatory attributes include:

**All Asset Categories**:

- Asset ID (unique identifier)
- Asset Name
- Asset Type/Category
- Owner (responsible person/role)
- Custodian (if different from owner)
- Description
- Location (physical or logical)
- Status (Active, Inactive, Retired, etc.)
- Business Criticality (Critical, High, Standard, Low)
- Created Date
- Last Updated Date
- Last Reviewed Date
- Next Review Date

**Information Assets (additional)**:

- Data Classification (Public, Internal, Confidential, Restricted)
- Data Format (structured/unstructured)
- Storage Location (system/repository)
- Retention Period

**IT Infrastructure (additional)**:

- IP Address (if network-connected)
- Operating System (if applicable)
- Physical/Virtual designation
- Serial Number / Asset Tag

**Applications (additional)**:

- Vendor/Developer
- Version
- License Type (perpetual, subscription, open-source)
- License Count

**Physical Assets (additional)**:

- Asset Tag / Serial Number
- Purchase Date
- Condition (New, Good, Fair, Poor)

**Personnel Assets (additional)**:

- Competency Category
- Current Capacity (headcount)
- Required Capacity
- Succession Plan Status

**Step 2: Query Inventory for Population Rates**

**Example 1: Information Assets - Data Classification**

- **Asset Category**: Information Assets
- **Mandatory Attribute**: Data Classification
- **Policy Requirement**: A.5.9-R3 (All information assets SHALL be classified)
- **Total Records**: 400 (total information assets in inventory)
- **Records with Attribute**: 376 (have classification assigned)
- **Missing Count**: 24 (formula auto-calculates)
- **Completeness %**: 94% (formula auto-calculates)
- **Compliance Status**: Fail (target is 100%)
- **Gap Severity**: High (classification is critical for access control)
- **Root Cause**: Legacy data migrated from old system without classification, owners not prompted to classify
- **Remediation Plan**: Email campaign to owners of 24 unclassified assets, request classification within 30 days
- **Target Date**: 22.02.2026
- **Responsible Party**: Information Security Manager
- **Evidence Reference**: QUAL-010 (query results showing 24 missing)

**Example 2: IT Infrastructure - IP Address**

- **Asset Category**: IT Infrastructure
- **Mandatory Attribute**: IP Address
- **Policy Requirement**: A.5.9-R3 (Network-connected devices SHALL have IP documented)
- **Total Records**: 600 IT infrastructure assets
- **Records with Attribute**: 520 (IP documented)
- **Missing Count**: 80
- **Completeness %**: 87%
- **Compliance Status**: Fail
- **Gap Severity**: Medium
- **Root Cause**: Devices with dynamic DHCP not tracked, offline devices have no current IP
- **Remediation Plan**: "Discovery scan to capture current IPs, update CMDB. Mark offline devices as 'N/A - Offline'"
- **Target Date**: 15.02.2026
- **Responsible Party**: IT Operations

**Example 3: Applications - License Count (Pass)**

- **Asset Category**: Applications
- **Mandatory Attribute**: License Count
- **Policy Requirement**: A.5.9-R3
- **Total Records**: 300
- **Records with Attribute**: 300
- **Missing Count**: 0
- **Completeness %**: 100%
- **Compliance Status**: Pass ✅
- **Gap Severity**: N/A
- **Root Cause**: N/A
- **Remediation Plan**: N/A (maintain compliance)

**Step 3: Calculate Overall Completeness**

Sheet auto-calculates:

- Overall completeness (average across all mandatory attributes)
- Completeness by asset category
- Top 10 missing attributes (prioritize remediation)

**Target**: 100% mandatory attribute completeness (policy requirement)

**Common Pitfalls**:

- ❌ Counting NULL vs. empty string differently (inconsistent)
- ✅ Define "populated" clearly: NOT NULL, NOT empty string, NOT "Unknown"
- ❌ Accepting "Unknown" or "TBD" as populated
- ✅ "Unknown" = missing data, requires remediation
- ❌ Not distinguishing "N/A" from missing
- ✅ "N/A" is valid for some fields (e.g., IP address for offline device), document rationale

---

### Sheet 4: Currency Assessment

**Purpose**: Verify inventory data is current (not stale) per policy thresholds.

**What This Sheet Captures**:

- Last Updated dates for each asset
- Staleness (days since last update)
- Compliance with policy thresholds by criticality
- Currency compliance percentage

**Column Definitions**:

| Column | Purpose | How to Complete |
|--------|---------|-----------------|
| **Asset Category** | Type of asset | Auto-populated from inventory |
| **Criticality** | Business criticality | Auto-populated from inventory |
| **Total Assets** | Count in this criticality band | Auto-calculated |
| **Policy Threshold** | Max staleness allowed | From policy Section 2.5.3 |
| **Assets Within Threshold** | Count current | Auto-calculated |
| **Assets Exceeding Threshold** | Count stale | Auto-calculated |
| **Currency Compliance %** | Percentage current | Formula: (Within / Total) × 100% |
| **Avg Days Since Update** | Average staleness | Auto-calculated |
| **Max Days Since Update** | Worst staleness | Auto-calculated |
| **Compliance Status** | Met target or not | Auto-calculated: Pass/Fail |
| **Remediation Plan** | How to refresh stale data | Free text |
| **Target Date** | When to refresh by | Date field |
| **Responsible Party** | Who will refresh | Free text |
| **Notes** | Additional context | Free text |

**Policy Thresholds (from Section 2.5.3)**:

- **Critical assets**: Daily updates (max 1 day staleness)
- **High criticality**: 3 days max staleness
- **Standard criticality**: 7 days max staleness
- **Low criticality**: 30 days max staleness

**How to Complete**:

**Step 1: Export Inventory with Last Updated Dates**

Query inventory for:

- Asset ID, Name, Category, Criticality
- Last Updated Date (when record last modified)
- Calculate Staleness = TODAY() - Last Updated Date

**Step 2: Group by Category and Criticality**

**Example 1: Information Assets - Critical**

- **Asset Category**: Information Assets
- **Criticality**: Critical
- **Total Assets**: 45 (critical information assets)
- **Policy Threshold**: 1 day (daily updates required)
- **Assets Within Threshold**: 42 (updated within 24 hours)
- **Assets Exceeding Threshold**: 3 (stale >1 day)
- **Currency Compliance %**: 93% (42/45 × 100%)
- **Avg Days Since Update**: 0.8 days
- **Max Days Since Update**: 14 days (one severely stale record)
- **Compliance Status**: Fail (target is 100% for critical assets)
- **Remediation Plan**: "Contact owners of 3 stale records, request immediate review and update. Investigate 14-day stale record - may be error."
- **Target Date**: 23.01.2026 (immediate - critical assets)
- **Responsible Party**: Information Security Manager

**Example 2: IT Infrastructure - Standard**

- **Asset Category**: IT Infrastructure
- **Criticality**: Standard
- **Total Assets**: 320
- **Policy Threshold**: 7 days
- **Assets Within Threshold**: 305
- **Assets Exceeding Threshold**: 15
- **Currency Compliance %**: 95%
- **Avg Days Since Update**: 4.2 days
- **Max Days Since Update**: 45 days
- **Compliance Status**: Pass (95% ≥ target, but should aim for 100%)
- **Remediation Plan**: "Run discovery scan to refresh 15 stale records"
- **Target Date**: 29.01.2026
- **Responsible Party**: IT Operations

**Example 3: Personnel Assets - All Criticalities**

- **Asset Category**: Personnel Assets
- **Criticality**: All (personnel competencies are all high criticality)
- **Total Assets**: 50
- **Policy Threshold**: 3 days
- **Assets Within Threshold**: 50
- **Assets Exceeding Threshold**: 0
- **Currency Compliance %**: 100% ✅
- **Compliance Status**: Pass
- **Notes**: "Weekly HR system sync keeps personnel assets current"

**Step 3: Identify Stale Records**

Create list of stale records (exceeding threshold):

- Asset ID, Name, Criticality, Days Stale
- Prioritize by criticality (Critical → High → Standard → Low)
- Assign to owners for refresh

**Common Pitfalls**:

- ❌ Using "Created Date" instead of "Last Updated Date"
- ✅ Last Updated = when record was last modified (any field change counts)
- ❌ Not accounting for weekends/holidays in staleness calculation
- ✅ Calendar days, not business days (policy specifies calendar days)
- ❌ Refreshing only high-profile assets
- ✅ Systematic refresh process for all stale records regardless of visibility

---

### Sheet 5: Consistency Checks

**Purpose**: Identify contradictions and anomalies in inventory data.

**What This Sheet Captures**:

- Automated consistency checks
- Logical contradictions (e.g., retired asset still in production)
- Cross-field validation failures
- Duplicate detection

**Column Definitions**:

| Column | Purpose | How to Complete |
|--------|---------|-----------------|
| **Check ID** | Unique identifier | Format: CHK-NNN |
| **Check Type** | Category of check | Dropdown: Status Contradiction / Date Inconsistency / Duplicate / Cross-Reference Error / Other |
| **Check Description** | What's being verified | Free text: e.g., "Retired assets should not have Active status" |
| **Check Logic** | Rule being applied | Free text: SQL/formula/logic |
| **Total Records Checked** | How many tested | Numeric |
| **Failures Found** | Count of inconsistencies | Numeric |
| **Failure Rate %** | Percentage failed | Formula: (Failures / Total) × 100% |
| **Example Failures** | Sample of failures | Free text: List 2-3 examples |
| **Impact** | Severity | Dropdown: Critical / High / Medium / Low |
| **Root Cause** | Why inconsistencies exist | Free text: Analysis |
| **Remediation Plan** | How to fix | Free text: Action plan |
| **Responsible Party** | Who will fix | Free text |
| **Evidence Reference** | Link to full results | Reference to Evidence Register |
| **Notes** | Additional context | Free text |

**How to Complete**:

**Common Consistency Checks**:

**Check 1: Status-Date Contradiction**

- **Check ID**: CHK-001
- **Check Type**: Status Contradiction
- **Check Description**: "Assets with Status='Retired' should have RetiredDate populated"
- **Check Logic**: `SELECT * FROM Inventory WHERE Status='Retired' AND RetiredDate IS NULL`
- **Total Records Checked**: 78 retired assets
- **Failures Found**: 12 (retired assets with no retired date)
- **Failure Rate %**: 15%
- **Example Failures**: "SRV-99887 (retired but no date), APP-00445 (retired but no date)"
- **Impact**: Medium (affects audit trail, unclear when retirement occurred)
- **Root Cause**: Retirement workflow doesn't enforce date entry
- **Remediation Plan**: "Contact asset owners, request retirement date. Update workflow to make RetiredDate mandatory when Status=Retired"
- **Responsible Party**: CMDB Administrator
- **Evidence Reference**: QUAL-020 (full query results)

**Check 2: Active Retired Assets**

- **Check ID**: CHK-002
- **Check Type**: Status Contradiction
- **Check Description**: "Assets marked Retired should not be in Active production use"
- **Check Logic**: "Cross-reference: CMDB Status=Retired but Discovery scan shows device responding on network"
- **Total Records Checked**: 78 retired assets
- **Failures Found**: 3 (retired assets still active on network)
- **Failure Rate %**: 4%
- **Example Failures**: "SRV-12345 (retired 2 months ago but still pingable), RTR-00678 (retired but still routing traffic)"
- **Impact**: Critical (security risk - retired assets may not be patched, access may not be revoked)
- **Root Cause**: Retirement process incomplete - asset marked retired in CMDB but not actually decommissioned
- **Remediation Plan**: "Immediate investigation - verify if assets should be un-retired or if decommission wasn't completed. Escalate to IT Operations manager."
- **Responsible Party**: IT Operations
- **Evidence Reference**: QUAL-021 (network scan vs. CMDB comparison)

**Check 3: Future Dates**

- **Check ID**: CHK-003
- **Check Type**: Date Inconsistency
- **Check Description**: "Created Date should not be in the future"
- **Check Logic**: `SELECT * FROM Inventory WHERE CreatedDate > TODAY()`
- **Total Records Checked**: 1,500 (all assets)
- **Failures Found**: 2
- **Failure Rate %**: 0.1%
- **Example Failures**: "APP-00999 (CreatedDate = 2027-01-01), DB-00555 (CreatedDate = 2026-12-31)"
- **Impact**: Low (likely data entry error, doesn't affect asset validity)
- **Root Cause**: Manual data entry error or timezone issue
- **Remediation Plan**: "Correct dates to actual creation date, add data validation to prevent future dates"
- **Responsible Party**: CMDB Administrator

**Check 4: Duplicate Detection**

- **Check ID**: CHK-004
- **Check Type**: Duplicate
- **Check Description**: "Assets with identical name, type, and location may be duplicates"
- **Check Logic**: `SELECT Name, Type, Location, COUNT(*) FROM Inventory GROUP BY Name, Type, Location HAVING COUNT(*) > 1`
- **Total Records Checked**: 1,500
- **Failures Found**: 8 potential duplicates (4 pairs)
- **Failure Rate %**: 0.5%
- **Example Failures**: "Laptop-Dell-Latitude-7400 appears twice with same serial number (likely data entry error), Customer-Database appears twice (may be dev vs. prod instances)"
- **Impact**: Medium (affects accuracy of counts, may lead to double-counting)
- **Root Cause**: Lack of uniqueness constraint, manual data entry
- **Remediation Plan**: "Investigate each pair - merge if true duplicate, rename if distinct assets. Add unique constraint on (Name + AssetTag)"
- **Responsible Party**: CMDB Administrator

**Check 5: Owner Exists**

- **Check ID**: CHK-005
- **Check Type**: Cross-Reference Error
- **Check Description**: "Asset owners should exist in HR system (valid employees)"
- **Check Logic**: "Cross-reference: Inventory.Owner NOT IN (SELECT EmployeeID FROM HR_System)"
- **Total Records Checked**: 1,500
- **Failures Found**: 23 (owners not in HR system)
- **Failure Rate %**: 1.5%
- **Example Failures**: "Assets owned by 'John Smith' who left company 6 months ago, assets owned by 'TBD' (placeholder)"
- **Impact**: High (ownership unclear, accountability missing)
- **Root Cause**: Owner changes not tracked, placeholder values used
- **Remediation Plan**: "Reassign assets with departed owners to current staff, eliminate 'TBD' placeholders"
- **Responsible Party**: Information Security Manager

**Check 6: Logical Capacity**

- **Check ID**: CHK-006
- **Check Type**: Date Inconsistency
- **Check Description**: "LastUpdated date should not be earlier than CreatedDate"
- **Check Logic**: `SELECT * FROM Inventory WHERE LastUpdated < CreatedDate`
- **Total Records Checked**: 1,500
- **Failures Found**: 5
- **Failure Rate %**: 0.3%
- **Example Failures**: "SRV-00111 (created 2025-01-01, last updated 2024-12-15 - impossible)"
- **Impact**: Low (data quality issue but doesn't affect asset validity)
- **Root Cause**: Data migration error from legacy system
- **Remediation Plan**: "Correct LastUpdated to match CreatedDate or later actual update"

**Common Pitfalls**:

- ❌ Running checks once and never repeating
- ✅ Automate checks, run monthly (or integrate into data quality dashboards)
- ❌ Ignoring low-impact inconsistencies
- ✅ Fix ALL inconsistencies (even low-impact) - they indicate process gaps
- ❌ Manual inconsistency hunting
- ✅ Automated SQL queries, scheduled reports

---

### Sheet 6: Policy Compliance Matrix

**Purpose**: Verify compliance with all SHALL requirements from ISMS-POL-A.5.9.

**What This Sheet Captures**:

- Each SHALL requirement from policy
- Evidence of compliance
- Compliance status (Met / Partially Met / Not Met)
- Gap analysis for non-compliance

**Column Definitions**:

| Column | Purpose | How to Complete |
|--------|---------|-----------------|
| **Requirement ID** | Policy requirement code | From policy (A.5.9-R1 through A.5.9-R9) |
| **Requirement Text** | Full requirement statement | Copy from policy |
| **Compliance Criterion** | How to verify compliance | Free text: What constitutes compliance |
| **Verification Method** | How verified | Free text: e.g., "Inventory query", "Sample testing", "Document review" |
| **Evidence Collected** | What evidence gathered | Free text: Description |
| **Evidence Reference** | Link to evidence | Reference to Evidence Register |
| **Compliance Status** | Met requirement or not | Dropdown: ✅ Met / ⚠️ Partially Met / ❌ Not Met |
| **Compliance %** | If quantifiable | Numeric (0-100%) or "N/A" |
| **Gap Description** | If not met, what's missing | Free text |
| **Gap Severity** | Criticality of gap | Dropdown: Critical / High / Medium / Low / N/A |
| **Remediation Plan** | How to close gap | Free text |
| **Target Date** | When to close gap | Date field |
| **Responsible Party** | Who will close gap | Free text |
| **Notes** | Additional context | Free text |

**How to Complete**:

**Step 1: List All SHALL Requirements**

From ISMS-POL-A.5.9, the SHALL requirements are:

- **A.5.9-R1**: [Organization] SHALL maintain an inventory of information and associated assets
- **A.5.9-R2**: [Organization] SHALL categorize assets per defined taxonomy
- **A.5.9-R3**: [Organization] SHALL document mandatory attributes for each inventoried asset
- **A.5.9-R4**: [Organization] SHALL assign ownership to all inventoried assets
- **A.5.9-R5**: [Organization] SHALL review and update the inventory on a defined schedule
- **A.5.9-R6**: [Organization] SHALL integrate asset inventory with other ISMS processes
- **A.5.9-R7**: [Organization] SHALL protect inventory data with appropriate access controls
- **A.5.9-R8**: [Organization] SHALL conduct periodic assessments of inventory quality
- **A.5.9-R9**: [Organization] SHALL report inventory metrics to management

**Step 2: Verify Each Requirement**

**Example 1: A.5.9-R1 (Inventory Exists)**

- **Requirement ID**: A.5.9-R1
- **Requirement Text**: "[Organization] SHALL maintain an inventory of information and associated assets"
- **Compliance Criterion**: "Inventory system exists, contains records for all 5 asset categories"
- **Verification Method**: "Review IMP-A.5.9-2 (Inventory Structure sheet), confirm inventory systems documented"
- **Evidence Collected**: "ServiceNow CMDB (IT Infrastructure, Applications), Asset Inventory spreadsheet (Information, Physical, Personnel)"
- **Evidence Reference**: QUAL-030 (screenshots of inventory systems)
- **Compliance Status**: ✅ Met
- **Compliance %**: 100%
- **Gap Description**: N/A
- **Gap Severity**: N/A

**Example 2: A.5.9-R3 (Mandatory Attributes) - Partially Met**

- **Requirement ID**: A.5.9-R3
- **Requirement Text**: "[Organization] SHALL document mandatory attributes for each inventoried asset"
- **Compliance Criterion**: "100% of assets have all mandatory attributes populated per policy Section 2.3"
- **Verification Method**: "Sheet 3 (Completeness Assessment) analysis"
- **Evidence Collected**: "Completeness Assessment shows 94% average completeness across all mandatory attributes"
- **Evidence Reference**: QUAL-031 (Sheet 3 results)
- **Compliance Status**: ⚠️ Partially Met
- **Compliance %**: 94%
- **Gap Description**: "24 information assets missing Data Classification, 80 IT assets missing IP Address, etc. (see Sheet 3 for full breakdown)"
- **Gap Severity**: High (mandatory attributes are required)
- **Remediation Plan**: "Execute remediation plans from Sheet 3 - email campaigns to owners, discovery scans to populate missing IPs, enforce mandatory fields in CMDB"
- **Target Date**: 22.02.2026 (30 days)
- **Responsible Party**: Information Security Manager, CMDB Administrator

**Example 3: A.5.9-R4 (Ownership Assignment)**

- **Requirement ID**: A.5.9-R4
- **Requirement Text**: "[Organization] SHALL assign ownership to all inventoried assets"
- **Compliance Criterion**: "100% of assets have Owner field populated with valid employee"
- **Verification Method**: "Query inventory for NULL/empty Owner field, cross-reference owners with HR system"
- **Evidence Collected**: "Owner field populated for 1,477 of 1,500 assets (98%). Cross-reference found 23 owners not in HR (departed employees)"
- **Evidence Reference**: QUAL-032 (owner query results, HR cross-reference)
- **Compliance Status**: ⚠️ Partially Met
- **Compliance %**: 98% (population), but 1.5% invalid
- **Gap Description**: "23 assets missing owner, 23 assets have departed employee as owner"
- **Gap Severity**: High (ownership is critical for accountability)
- **Remediation Plan**: "Assign missing owners, reassign assets from departed employees to current staff"
- **Target Date**: 05.02.2026 (2 weeks)
- **Responsible Party**: Information Security Manager

**Example 4: A.5.9-R8 (Periodic Assessments) - Met**

- **Requirement ID**: A.5.9-R8
- **Requirement Text**: "[Organization] SHALL conduct periodic assessments of inventory quality"
- **Compliance Criterion**: "Quality assessment conducted quarterly, documented, reviewed by CISO"
- **Verification Method**: "This assessment workbook is evidence of compliance, previous assessments on file"
- **Evidence Collected**: "Q4 2025 quality assessment (this workbook), Q3 2025 assessment archived"
- **Evidence Reference**: QUAL-033 (this workbook, Q3 archive)
- **Compliance Status**: ✅ Met
- **Compliance %**: 100%
- **Gap Description**: N/A

**Step 3: Calculate Overall Policy Compliance**

Sheet auto-calculates:

- Overall compliance percentage (% of requirements fully met)
- Breakdown: Met / Partially Met / Not Met
- Weighted compliance score (accounting for partial compliance)

**Target**: 100% compliance with all SHALL requirements

**Common Pitfalls**:

- ❌ Claiming compliance without evidence
- ✅ Each "Met" status requires documented evidence
- ❌ Vague gap descriptions ("some assets missing data")
- ✅ Specific, quantified gaps ("24 assets missing classification, list provided in Evidence Register")
- ❌ Unrealistic remediation timelines
- ✅ Achievable target dates with assigned responsibilities

---

### Sheet 7: Quality Metrics & Scoring

**Purpose**: Aggregate all quality dimensions into overall quality score.

**What This Sheet Captures**:

- Quality scores for each of 5 dimensions
- Weighted overall quality score
- Compliance status summary
- Trending vs. previous assessments

**This sheet is MOSTLY auto-populated** from other sheets.

**Column Definitions**:

| Column | Purpose | How to Complete |
|--------|---------|-----------------|
| **Quality Dimension** | Dimension name | Fixed: Accuracy / Completeness / Currency / Consistency / Policy Compliance |
| **Weight** | Importance weighting | Policy-defined or organization-specific |
| **Target Score** | Policy requirement | From policy Section 2.5 |
| **Actual Score** | Current achievement | Auto-calculated from sheets 2-6 |
| **Gap vs. Target** | Shortfall | Formula: Actual - Target |
| **Compliance Status** | Met target or not | Auto-calculated: ✅ / ⚠️ / ❌ |
| **Trend vs. Last Quarter** | Improving or degrading | Dropdown: Improved / Stable / Degraded / N/A |
| **Key Issues** | Top problems | Free text summary |
| **Remediation Priority** | What to fix first | Free text |
| **Notes** | Additional context | Free text |

**Quality Dimension Details**:

**1. Accuracy (Weight: 30%)**

- Target: ≥95% (Info), ≥98% (IT), ≥90% (Physical/App), 100% (Personnel)
- Actual: Weighted average from Sheet 2 (Accuracy Sampling)
- Formula: `=(Info_Accuracy*0.3 + IT_Accuracy*0.4 + App_Accuracy*0.2 + Physical_Accuracy*0.1) / 1.0`

**2. Completeness (Weight: 25%)**

- Target: 100% mandatory attributes populated
- Actual: Average completeness from Sheet 3
- Formula: `=AVERAGE(Sheet3!Completeness_Percentages)`

**3. Currency (Weight: 20%)**

- Target: 100% within staleness thresholds
- Actual: Weighted average from Sheet 4
- Formula: `=AVERAGE(Sheet4!Currency_Compliance_Percentages)`

**4. Consistency (Weight: 15%)**

- Target: 0% inconsistencies (or <1% acceptable)
- Actual: `= 100% - Average(Failure Rates from Sheet 5)`
- Formula: `=100 - AVERAGE(Sheet5!Failure_Rates)`

**5. Policy Compliance (Weight: 10%)**

- Target: 100% SHALL requirements met
- Actual: Percentage from Sheet 6
- Formula: `=COUNTIF(Sheet6!Compliance_Status,"✅ Met") / COUNTA(Sheet6!Compliance_Status) * 100`

**Overall Quality Score**:
```
Overall = (Accuracy × 30%) + (Completeness × 25%) + (Currency × 20%) + 
          (Consistency × 15%) + (Policy Compliance × 10%)
```

**Scoring Interpretation**:

- **90-100%**: Excellent (world-class data quality)
- **80-89%**: Good (acceptable, minor improvements needed)
- **70-79%**: Fair (significant improvements required)
- **<70%**: Poor (major quality issues, immediate action required)

**Example Quality Scorecard**:

| Dimension | Weight | Target | Actual | Gap | Status | Trend |
|-----------|--------|--------|--------|-----|--------|-------|
| Accuracy | 30% | 95% | 96% | +1% | ✅ | Improved |
| Completeness | 25% | 100% | 94% | -6% | ⚠️ | Stable |
| Currency | 20% | 100% | 92% | -8% | ⚠️ | Improved |
| Consistency | 15% | 99% | 98.5% | -0.5% | ✅ | Stable |
| Policy Compliance | 10% | 100% | 89% | -11% | ⚠️ | Improved |
| **Overall Score** | **100%** | **97%** | **94.2%** | **-2.8%** | ⚠️ | **Improved** |

Interpretation: Good quality (94.2%), close to target. Main gaps: Completeness (mandatory attributes) and Policy Compliance. Action required.

---

### Sheet 8: Evidence Register

**Purpose**: Document all evidence collected during quality assessment.

**Column Definitions**: Same as IMP-A.5.9-1/2 Evidence Registers with adjusted Related Domain:

**Related Domain** dropdown:

- Accuracy Sampling
- Completeness Assessment
- Currency Assessment
- Consistency Checks
- Policy Compliance
- Quality Metrics
- All Domains

**Evidence ID format**: `QUAL-NNN` (e.g., QUAL-001, QUAL-002, etc.)

**Example Evidence Items**:

1. **QUAL-001**: Random sample selection results (150 assets)
2. **QUAL-002**: Accuracy verification screenshots (network scans, owner confirmations)
3. **QUAL-010**: Completeness query results (missing Data Classification)
4. **QUAL-020**: Consistency check CHK-001 full results
5. **QUAL-021**: Retired assets network scan comparison
6. **QUAL-030**: Inventory system screenshots (compliance evidence)
7. **QUAL-040**: Quality metrics calculation workbook

---

## Evidence Collection

### What Evidence to Collect

**Accuracy Sampling Evidence**:

- Random sample selection documentation (method, seed, stratification)
- Verification screenshots/records for each sample
- Owner confirmation emails
- Network scan results
- Physical inspection checklists

**Completeness Evidence**:

- SQL queries or reports showing missing attributes
- Inventory exports with NULL/empty field counts
- Remediation tracking logs

**Currency Evidence**:

- Staleness reports (LastUpdated date queries)
- Owner notification emails for stale records
- Refresh activity logs

**Consistency Evidence**:

- Automated check scripts (SQL, Python)
- Full result sets from consistency checks
- Duplicate investigation results
- Cross-reference reports (inventory vs. HR, inventory vs. discovery)

**Policy Compliance Evidence**:

- Policy document (ISMS-POL-A.5.9) with requirement mapping
- Compliance verification reports
- Gap analysis documentation
- Remediation plans and tracking

### Evidence Organization

```
/evidence/
├── 2026-Q1/
│   ├── accuracy-sampling/
│   │   ├── sample-selection/
│   │   │   ├── random-sample-list.xlsx
│   │   │   └── stratification-methodology.pdf
│   │   ├── verification-results/
│   │   │   ├── network-scans/
│   │   │   ├── owner-confirmations/
│   │   │   └── physical-inspections/
│   │   └── accuracy-summary-report.xlsx
│   ├── completeness/
│   │   ├── missing-attributes-queries.sql
│   │   ├── completeness-reports/
│   │   └── remediation-tracking.xlsx
│   ├── currency/
│   │   ├── staleness-reports/
│   │   └── refresh-activity-logs/
│   ├── consistency/
│   │   ├── automated-checks/
│   │   │   ├── check-scripts.sql
│   │   │   └── check-results/
│   │   └── cross-reference-reports/
│   ├── policy-compliance/
│   │   ├── requirement-mapping.xlsx
│   │   ├── compliance-verification/
│   │   └── gap-analysis/
│   └── quality-metrics/
│       ├── quality-scorecard.xlsx
│       └── trend-analysis/
└── 2026-Q2/
    └── [same structure]
```

---

## Common Pitfalls

### Pitfall 1: Non-Random Sampling (Selection Bias)

**Problem**: Choosing "easy to verify" or "known good" assets for sampling.

**Why It Fails**: Biased sample doesn't represent true quality, inflates accuracy scores.

**Solution**: True random selection, verify WHATEVER the random sample selects (even difficult cases).

### Pitfall 2: Small Sample Size (Statistical Insignificance)

**Problem**: Sampling 10-20 assets from inventory of 1,000+ (insufficient).

**Why It Fails**: Results not statistically valid, can't extrapolate to full inventory.

**Solution**: Calculate proper sample size for 95% confidence, ±5% margin of error (typically 100-200 for large inventories).

### Pitfall 3: Accepting "Unknown" as Valid Data

**Problem**: Treating "Unknown", "TBD", "N/A" as populated fields.

**Why It Fails**: These are placeholders, not actual data, should count as missing.

**Solution**: Define "populated" as: NOT NULL, NOT empty, NOT placeholder value.

### Pitfall 4: One-Time Assessment (No Trending)

**Problem**: Assessing quality once, never repeating, no trend analysis.

**Why It Fails**: Can't measure improvement, can't demonstrate continuous quality management.

**Solution**: Quarterly assessments (minimum), track trends, demonstrate improvement over time.

### Pitfall 5: Ignoring Root Causes

**Problem**: Documenting gaps without analyzing WHY they exist.

**Why It Fails**: Surface-level fixes don't prevent recurrence, gaps reappear.

**Solution**: Root cause analysis for every gap, fix processes not just data.

### Pitfall 6: Vague Remediation Plans

**Problem**: "We'll improve data quality" (no specific actions, no timeline, no accountability).

**Why It Fails**: Nothing actually gets fixed, same gaps in next assessment.

**Solution**: Specific actions, assigned responsibilities, target dates, track completion.

### Pitfall 7: Cherry-Picking Compliance Evidence

**Problem**: Only showing evidence of compliance, hiding non-compliance.

**Why It Fails**: Dishonest, auditors will find gaps, damages credibility.

**Solution**: Document ACTUAL compliance status (including gaps), honest assessment drives improvement.

---

## Quality Checklist

Before submitting this assessment, verify:

### Sampling Checks

- [ ] Sample size statistically valid (95% confidence, ±5% margin)
- [ ] Sample is truly random (no selection bias)
- [ ] Sample is stratified by asset category
- [ ] All sampled assets verified (no skipping "hard to verify" assets)
- [ ] Verification methods documented for each sample
- [ ] "Cannot Verify" properly excluded from accuracy calculation

### Completeness Checks

- [ ] All mandatory attributes from policy listed
- [ ] Population rates calculated for each attribute
- [ ] "Populated" defined clearly (excludes NULL, empty, placeholders)
- [ ] Missing data counts accurate
- [ ] Remediation plans specific and actionable

### Currency Checks

- [ ] Staleness calculated correctly (TODAY - LastUpdated)
- [ ] Policy thresholds applied by criticality
- [ ] Stale records identified and prioritized
- [ ] Remediation assigned to responsible parties

### Consistency Checks

- [ ] Automated checks documented (logic, results)
- [ ] All major contradiction types checked
- [ ] Root causes analyzed
- [ ] Remediation plans developed

### Policy Compliance Checks

- [ ] All SHALL requirements listed
- [ ] Compliance verified with evidence
- [ ] Evidence references provided
- [ ] Gaps documented honestly
- [ ] Remediation plans realistic

### Metrics Checks

- [ ] Quality scores calculated correctly
- [ ] Weighting appropriate (totals 100%)
- [ ] Overall score computed
- [ ] Trending vs. previous quarter documented
- [ ] Scorecard interpretation provided

### Evidence Checks

- [ ] All evidence items documented in register
- [ ] Evidence metadata complete (date, collector, location)
- [ ] Evidence quality assessed
- [ ] Evidence stored securely per retention policy

---

## Review & Approval

### Review Process

**Step 1: Self-Review** (Assessment Preparer)

- Complete quality checklist above
- Verify calculations and formulas
- Check evidence completeness

**Step 2: Statistical Review** (QA/Audit Team if available)

- Validate sampling methodology
- Verify sample size and stratification
- Check statistical calculations
- Review extrapolation from sample to population

**Step 3: Technical Review** (CMDB Administrator, IT Operations)

- Validate consistency check results
- Confirm remediation plans are feasible
- Review resource requirements

**Step 4: Security Review** (Information Security Manager)

- Review quality scores vs. targets
- Assess gap severity and priorities
- Verify policy compliance verification
- Review remediation timeline

**Step 5: CISO Approval**

- Review executive summary (quality scorecard)
- Assess compliance status
- Approve remediation plans and resource allocation
- Escalate critical gaps to Executive Management
- Sign approval

**Step 6: Submission to Compliance Dashboard**

- Export metrics to dashboard consolidation
- Update ISMS-IMP-A.5.9.5 (Compliance Dashboard)
- Archive assessment workbook
- Store evidence per retention policy

### Approval Criteria

**Approve** if:

- ✅ Overall quality score ≥80%
- ✅ No critical gaps (Critical severity gaps must be remediated before approval)
- ✅ Remediation plans exist for all gaps
- ✅ Evidence quality rated "Complete" or "Partial"
- ✅ Sampling methodology valid

**Conditional Approval** (with immediate remediation) if:

- ⚠️ Overall quality score 70-79%
- ⚠️ Some high-severity gaps (but remediation in progress)
- ⚠️ Evidence quality "Partial" (sufficient for now, needs improvement)

**Reject** if:

- ❌ Overall quality score <70%
- ❌ Critical gaps with no remediation plan
- ❌ Sampling methodology invalid (biased, insufficient size)
- ❌ Evidence insufficient

---

**END OF ISMS-IMP-A.5.9.3 PART I - USER COMPLETION GUIDE**


**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
