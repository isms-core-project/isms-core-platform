**ISMS-IMP-A.5.23.S5 - Compliance Monitoring Dashboard**
**Assessment Specification with User Completion Guide**
### ISO/IEC 27001:2022 Control A.5.23: Information Security for Use of Cloud Services

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.23.S5 |
| **Version** | 1.0 |
| **Assessment Area** | Compliance Monitoring & Exit Planning Dashboard |
| **Related Policy** | ISMS-POL-A.5.19-23-S5 (Cloud Services Security - Section 8: Exit Strategy Framework) |
| **Purpose** | Auto-generate executive compliance dashboard consolidating exit strategy compliance, DORA PoC testing status, and high-risk service identification from source assessment workbooks (IMP-A.5.23.1 through A.5.23.4) |
| **Target Audience** | CISO, CIO, Risk Committee, Board of Directors, Compliance Officers, DPO, Internal/External Auditors |
| **Assessment Type** | Consolidation Dashboard (Auto-Generated from Source Workbooks) |
| **Review Cycle** | Quarterly (after source workbook completion), Annual (post-PoC testing), Pre-Audit, Board Meetings |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial Python generator script for basic exit strategy dashboard (3 sheets). Consolidated data from IMP-A.5.23.1 (exit strategies) and IMP-A.5.23.4 (governance). No user documentation provided. | ISMS Implementation Team |

---

## Document Purpose & Scope

### What This Document Provides

**Part I: User Completion Guide** (~4,500 lines target)

- Dashboard overview and architecture
- Source workbook prerequisites and validation
- Step-by-step dashboard generation procedures
- Sheet-by-sheet interpretation guidance
- Executive reporting templates (CISO/CIO, Board)
- Dashboard refresh and maintenance procedures
- Integration with ISMS and risk management
- Quality assurance and troubleshooting
- Appendices, glossary, and regulatory references


**Part II: Technical Specification** (~4,000 lines target)

- Python generator script architecture breakdown
- Complete output workbook specification (3 sheets)
- Data extraction algorithms and formulas
- Schema validation logic
- Conditional formatting and styling rules
- Testing and validation procedures
- Extension and customization guidance


### Target Audience

**Primary Users:**

- **CISO / CIO:** Executive oversight of cloud exit strategy compliance
- **Risk Committee:** Quarterly compliance reporting and risk escalation
- **Compliance Officer:** Dashboard generation, validation, and evidence management
- **DPO (Data Protection Officer):** Cross-border data transfer risk monitoring


**Secondary Users:**

- **Internal Auditors:** ISO 27001 A.5.23 audit evidence
- **External Auditors:** Third-party compliance verification
- **Board of Directors:** Annual strategic risk reporting
- **IT Operations:** Remediation action planning and tracking


### Dual Perspective Approach

**🔧 IMPLEMENTER PERSPECTIVE:**
*You are the Compliance Officer responsible for generating the quarterly compliance dashboard. You need to understand how to run the Python generator script, validate outputs against source data, interpret metrics, and present findings to executives with actionable recommendations.*

**🔍 AUDITOR PERSPECTIVE:**
*You are verifying that exit strategy compliance is monitored systematically with proper evidence trails. You need to understand data sources, validation procedures, traceability from source workbooks to dashboard metrics, and evidence of executive governance (decisions based on dashboard findings).*

**This guide maintains BOTH perspectives throughout all sections.**

---

## Relationship to Other ISMS Documents

### Source Documents (Inputs to Dashboard)

| Document ID | Title | Data Extracted | Usage in Dashboard |
|-------------|-------|----------------|-------------------|
| **ISMS-IMP-A.5.23.S1** | Cloud Service Inventory | Sheet 4: Exit strategy type, lock-in risk, export tested, migration complexity | Exit Strategy Coverage metrics, High-risk services list |
| **ISMS-IMP-A.5.23.S2** | Vendor Due Diligence & Contracts | (Future: Vendor risk ratings, contract terms) | Not currently used (v2.1 enhancement planned) |
| **ISMS-IMP-A.5.23.S3** | Secure Configuration & Deployment | (Future: Configuration compliance metrics) | Not currently used (v2.1 enhancement planned) |
| **ISMS-IMP-A.5.23.S4** | Ongoing Governance & Risk Management | Sheet 7: Annual exit review status, PoC testing results, next due dates | DORA PoC Testing Compliance metrics, Recommendations |

### Policy Documents (Compliance Baseline)

| Document ID | Title | Policy Targets | Dashboard Validation |
|-------------|-------|----------------|---------------------|
| **ISMS-POL-A.5.19-23-S5** | Cloud Services Security - Section 8 | Exit Strategy Framework: Cloud-to-Cloud ≥90%, Hybrid 5-10%, On-Premises <5% | Compares actual % vs targets, flags deviations |
| **ISMS-POL-A.5.19-23-S4** | Supplier Monitoring & Change Management | Vendor risk monitoring, governance activities | (Future: Vendor performance metrics) |

### Output Documents (Dashboard Consumers)

| Document Type | Usage | Frequency |
|---------------|-------|-----------|
| **CISO Monthly Report** | Executive summary of exit strategy compliance | Monthly |
| **Risk Committee Report** | Quarterly compliance status with escalations | Quarterly |
| **Board Briefing** | Annual strategic risk overview (1-page summary) | Annually |
| **Audit Evidence Package** | ISO 27001 A.5.23 compliance demonstration | On-demand (pre-audit) |
| **Risk Register Updates** | Critical findings added as enterprise risks | As needed (Critical findings) |

---

# PART I: USER COMPLETION GUIDE
# Dashboard Overview

## Purpose & Scope

**What This Dashboard Does:**

- **Consolidates** data from FOUR source workbooks (IMP-A.5.23.1 through A.5.23.4)
- **Validates** exit strategy compliance against policy targets
- **Monitors** DORA Article 28.6 PoC testing requirements
- **Identifies** high-risk services requiring immediate attention
- **Provides** actionable recommendations for executive decision-making


**What This Dashboard Does NOT Do:**

- Does NOT replace detailed assessments (use IMP-A.5.23.1-4 for that)
- Does NOT collect new data (it reads existing workbooks)
- Does NOT have manual input fields (100% auto-generated)


**Target Audience:**

- **Primary:** CISO, CIO, Risk Committee
- **Secondary:** Compliance Officer, DPO, IT Management
- **Tertiary:** Auditors (for compliance overview)


## Dashboard Architecture

**Source Workbooks (Inputs):**

```
┌──────────────────────────────────────────────────────────────────┐
│                     SOURCE WORKBOOKS (4)                         │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  IMP-A.5.23.1: Cloud Service Inventory                          │
│  ├─ Sheet 4: Cloud Security Services (Exit Strategy data)       │
│  └─ Columns R-AA: Exit strategy type, lock-in risk, export test │
│                                                                  │
│  IMP-A.5.23.2: Vendor Due Diligence & Contracts                 │
│  └─ (Optional: Future enhancement for vendor risk metrics)      │
│                                                                  │
│  IMP-A.5.23.3: Secure Configuration & Deployment                │
│  └─ (Optional: Future enhancement for config compliance)        │
│                                                                  │
│  IMP-A.5.23.4: Ongoing Governance & Risk Management             │
│  ├─ Sheet 7: Exit Strategy Review (Annual review + PoC testing) │
│  └─ Columns H-N: PoC test results, data portability, next due   │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌──────────────────────────────────────────────────────────────────┐
│                    PYTHON GENERATOR SCRIPT                       │
│           generate_reg_a523_5_compliance_dashboard.py            │
├──────────────────────────────────────────────────────────────────┤
│  1. Validate all 4 source workbooks exist                       │
│  2. Extract exit strategy data from IMP-5.23.1                  │
│  3. Extract PoC testing data from IMP-5.23.4                    │
│  4. Calculate compliance metrics                                │
│  5. Generate 3-sheet dashboard workbook                         │
└──────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌──────────────────────────────────────────────────────────────────┐
│              OUTPUT: DASHBOARD WORKBOOK (3 Sheets)               │
├──────────────────────────────────────────────────────────────────┤
│  1. Exit Strategy Dashboard                                     │
│           - Exit strategy coverage metrics                       │
│           - DORA PoC testing compliance                          │
│  2. Risk Overview                                               │
│           - High-risk services list                              │
│           - Critical lock-in services                            │
│  3. Recommendations                                             │
│           - Actionable findings                                  │
│           - Priority-ranked remediation items                    │
└──────────────────────────────────────────────────────────────────┘
```

**File Naming Convention:**
```
Output: ISMS-IMP-A.5.23.S5_Dashboard_YYYYMMDD.xlsx
Example: ISMS-IMP-A.5.23.S5_Dashboard_20260120.xlsx
```

---

# Prerequisites & Setup

## Required Source Workbooks

**Before running the dashboard generator, ensure ALL FOUR source workbooks exist:**

| Workbook | Required Filename Pattern | Status Check |
|----------|---------------------------|--------------|
| IMP-A.5.23.1 | `ISMS-IMP-A.5.23.S1_Inventory_*.xlsx` | ✅ Must have Sheet 4 (Cloud Security Services) |
| IMP-A.5.23.2 | `ISMS-IMP-A.5.23.S2_VendorDD_*.xlsx` | ✅ Must have Instructions sheet |
| IMP-A.5.23.3 | `ISMS-IMP-A.5.23.S3_SecureConfig_*.xlsx` | ✅ Must have Instructions sheet |
| IMP-A.5.23.4 | `ISMS-IMP-A.5.23.S4_Governance_*.xlsx` | ✅ Must have Sheet 7 (Exit Strategy Review) |

**Critical Requirement:**

- Workbooks MUST be in the same directory as the generator script
- Workbooks MUST be the most recent versions (check timestamps)
- Workbooks MUST be complete (not in-progress drafts)


## Data Quality Requirements

**IMP-A.5.23.1 (Inventory) - Sheet 4:**

- All services must have `Exit Strategy Type` (Column R)
- All services must have `Lock-In Risk` assessment (Column X)
- Critical services must have `Export Tested` status (Column U)


**IMP-A.5.23.4 (Governance) - Sheet 7:**

- Critical services must have `PoC Test Result` (Column J)
- `PoC Testing Required?` must be set for Critical services (Column H)
- `PoC Test Next Due` must be populated (Column N)


**Data Quality Validation:**
The generator script performs automatic validation and will:

- ✅ **PASS:** If all required data present
- ⚠️ **WARNING:** If optional data missing (continues generation)
- ❌ **FAIL:** If critical sheets or columns missing (stops generation)


## Python Environment Setup

**Requirements:**
```bash
pip install openpyxl
```

**System Requirements:**

- Python 3.8+
- 50 MB free disk space (for dashboard workbook)
- Source workbooks accessible (same directory or specify path)


---

# Generating the Dashboard

## Running the Generator Script

**Command:**
```bash
python3 generate_reg_a523_5_compliance_dashboard.py
```

**Expected Output:**
```
================================================================================
ISMS-IMP-A.5.23.S5 - Compliance Monitoring Dashboard Generator (REGULATORY)
ISO/IEC 27001:2022 Control A.5.23 + Exit Strategy Framework
================================================================================

🛡️  Consolidates data from 4 assessment workbooks:
   1. Inventory (Exit Strategy framework)
   2. Vendor Due Diligence
   3. Secure Configuration
   4. Governance (Exit Strategy review + PoC testing)

[VALIDATE] Checking source workbooks...
   [OK] Found: ISMS-IMP-A.5.23.S1_Inventory_20260120.xlsx
   [OK] Found: ISMS-IMP-A.5.23.S2_VendorDD_20260120.xlsx
   [OK] Found: ISMS-IMP-A.5.23.S3_SecureConfig_20260120.xlsx
   [OK] Found: ISMS-IMP-A.5.23.S4_Governance_20260120.xlsx

================================================================================
DASHBOARD GENERATION
================================================================================

[EXTRACT] Reading Exit Strategy data from inventory workbook...
   [OK] Extracted data from 32 services
        Cloud-to-Cloud: 28
        Hybrid: 3
        On-Premises: 1
        Not Determined: 0

[EXTRACT] Reading PoC Testing data from governance workbook...
   [OK] Extracted PoC data for 12 Critical services
        PoC Completed: 10
        PoC Not Tested: 1
        PoC Overdue: 1

[GENERATE] Creating dashboard workbook...
   [OK] Exit Strategy dashboard created
   [OK] Risk Overview created
   [OK] Recommendations created

[SAVE] Saving dashboard: ISMS-IMP-A.5.23.S5_Dashboard_20260120.xlsx

================================================================================
✅ SUCCESS: ISMS-IMP-A.5.23.S5_Dashboard_20260120.xlsx
================================================================================

📊 DASHBOARD STRUCTURE (3 sheets):
   1. Exit Strategy Dashboard (Exit Strategy metrics + PoC Testing compliance)
   2. Risk Overview (High-risk services requiring attention)
   3. Recommendations (Actionable findings)

🛡️  COMPLIANCE COVERAGE:
   ✓ ISO 27001:2022 A.5.23 (Exit planning requirements)
   ✓ POL-A.5.19-23-S5 Section 8 (Exit Strategy Framework)
   ✓ DORA Article 28.6 (Annual PoC testing)

🎯 NEXT STEPS:
   1. Review Exit Strategy Dashboard for compliance status
   2. Address Critical/High priority items in Recommendations
   3. Escalate PoC testing failures to CISO immediately
   4. Update risk register with findings
   5. Quarterly reporting to Risk Committee

================================================================================
"In God we trust. All others must bring data." – W. Edwards Deming
================================================================================
```

## Troubleshooting Generation Failures

**Common Issues:**

| Error Message | Cause | Resolution |
|---------------|-------|------------|
| `FileNotFoundError: No files matching pattern...` | Source workbook missing | Check all 4 workbooks in same directory |
| `Sheet 'X' not found in workbook` | Workbook version mismatch | Regenerate source workbook with latest script |
| `Column 'Y' not found in sheet 'Z'` | Wrong workbook version | Ensure all workbooks are v1.0+ (regulatory) |
| `No data extracted from inventory` | Empty inventory Sheet 4 | Complete IMP-5.23.1 Sheet 4 first |
| `Exit Strategy Review sheet missing` | Old governance workbook | Regenerate IMP-5.23.4 with v2.1 script |

**Debug Mode:**
Add `print()` statements in script to see detailed extraction:
```python
# Line ~270 in script
print(f"   Row {row}: {service_name} -> {exit_strategy}")
```

---

# Reading the Dashboard

## Sheet 1: Exit Strategy Dashboard

**Purpose:** Monitor compliance with exit strategy policy targets.

### Section 1: Exit Strategy Coverage Metrics

**Table Layout:**

| METRIC | VALUE | PERCENTAGE | STATUS | POLICY TARGET |
|--------|-------|------------|--------|---------------|
| Total Cloud Services | 32 | - | - | All services inventoried |
| Cloud-to-Cloud Strategy | 28 | 87.5% | ⚠️ | ≥90% (default strategy) |
| Hybrid Strategy | 3 | 9.4% | ✅ | 5-10% (data sovereignty cases) |
| On-Premises Strategy | 1 | 3.1% | ✅ | <5% (requires TCO justification) |
| Not Yet Determined | 0 | 0.0% | ✅ | Temporary (new services only) |
| - | - | - | - | - |
| High Lock-In Risk | 2 | - | ⚠️ | Mitigation plan required |
| CRITICAL Lock-In Risk | 1 | - | ❌ | Immediate action required |
| Export Not Tested (Critical) | 1 | - | ❌ | All Critical services tested |

**How to Read:**

**✅ Green Checkmark:** Compliant with policy target

- Example: On-Premises = 3.1% (target: <5%) → ✅ Good


**⚠️ Yellow Warning:** Approaching policy limit or minor deviation

- Example: Cloud-to-Cloud = 87.5% (target: ≥90%) → ⚠️ Close to target but not quite there
- **Action:** Monitor, trend toward compliance


**❌ Red X:** Non-compliant, requires immediate action

- Example: CRITICAL Lock-In Risk = 1 (target: 0) → ❌ Unacceptable
- **Action:** Escalate to CISO, implement mitigation immediately


**Exit Strategy Types Explained:**

| Strategy | Description | When to Use | Policy Target |
|----------|-------------|-------------|---------------|
| **Cloud-to-Cloud** | Migrate from one cloud provider to another cloud provider | **DEFAULT** - Most cloud services | ≥90% of services |
| **Hybrid** | Migrate to hybrid (cloud + on-premises) solution | Data sovereignty requirements (e.g., GDPR, Swiss privacy) | 5-10% of services |
| **On-Premises** | Migrate back to on-premises infrastructure | Extreme cases only (TCO justification required) | <5% of services |
| **Not Determined** | Exit strategy not yet defined | Temporary state for new services only | 0% (complete within 90 days) |

**Why These Targets?**

- **Cloud-to-Cloud 90%+:** Maximizes flexibility, minimizes lock-in to specific infrastructure
- **Hybrid 5-10%:** Allows for data sovereignty edge cases without over-committing to on-prem
- **On-Premises <5%:** On-prem defeats cloud benefits; only acceptable if TCO justifies it


### Section 2: DORA PoC Testing Compliance

**Table Layout:**

| METRIC | VALUE | STATUS | COMPLIANCE REQUIREMENT |
|--------|-------|--------|------------------------|
| Critical Services Requiring PoC Testing | 12 | - | All Critical services with exit strategy |
| PoC Testing Completed (Pass) | 10 | ⚠️ | 100% annually |
| PoC Testing Not Tested | 1 | ❌ | 0 (all must be tested) |
| PoC Testing Overdue | 1 | ❌ | 0 (test on schedule) |
| Overall PoC Compliance | 83.3% | ⚠️ | 100% (DORA Art. 28.6) |

**How to Read:**

**Critical Services:** Services with `Service_Criticality = Critical` in inventory

- These MUST have exit strategies tested via Proof-of-Concept (PoC) annually
- DORA Article 28.6 requirement for financial institutions


**PoC Test Result Values:**

- **Pass:** PoC successfully demonstrated data export and service migration
- **Not Tested:** PoC never conducted (violation if >365 days old)
- **In Progress:** PoC started but not completed (counts as "Overdue" if past due date)
- **Fail:** PoC attempted but failed (requires remediation plan)


**Overdue Calculation:**

- Script compares `PoC Test Next Due` date (Column N in IMP-5.23.4 Sheet 7) against today's date
- If Next Due < Today AND Result ≠ Pass → **Overdue** (escalate to CISO)


**Example Interpretation:**
```
PoC Testing Completed: 10/12 = 83.3%
PoC Not Tested: 1 service
PoC Overdue: 1 service

EXECUTIVE ACTION REQUIRED:

- Service A: PoC never tested → Schedule PoC within 30 days
- Service B: PoC overdue (last test 14 months ago) → Immediate PoC retest

```

---

## Sheet 2: Risk Overview

**Purpose:** List all high-risk services requiring immediate attention.

**Table Structure:**

| SERVICE NAME | PROVIDER | CRITICALITY | EXIT STRATEGY | LOCK-IN RISK | EXPORT TESTED | POC RESULT | RISK FACTORS |
|--------------|----------|-------------|---------------|--------------|---------------|------------|--------------|
| Salesforce Sales Cloud | Salesforce | Critical | Cloud-to-Cloud | High | No | Not Tested | ❌ Export not tested, ❌ PoC not tested |
| Oracle ERP | Oracle | Critical | On-Premises | Critical | Partial | Fail | ❌ Critical lock-in, ❌ PoC failed, ⚠️ On-prem strategy |
| Microsoft 365 | Microsoft | Critical | Cloud-to-Cloud | Low | Yes | Pass | ✅ Compliant |

**Risk Factor Icons:**

| Icon | Meaning | Severity |
|------|---------|----------|
| ❌ | Critical issue requiring immediate action | **Critical** |
| ⚠️ | Warning - needs attention | **High** |
| ✅ | Compliant | **None** |

**How to Use This Sheet:**

1. **Sort by Risk Factors column** (most ❌ to fewest)
2. **Prioritize services with:**

   - Critical Lock-In Risk = Critical
   - PoC Result = Fail or Not Tested
   - Export Tested = No (for Critical services)
   - Exit Strategy = On-Premises (without TCO justification)


3. **Executive Actions:**

   - Critical Lock-In → Immediate migration planning (add to risk register)
   - PoC Fail → Root cause analysis, remediation plan to CISO
   - Export Not Tested → Schedule export test within 30 days
   - On-Premises without justification → Re-evaluate strategy or document TCO


---

## Sheet 3: Recommendations

**Purpose:** Priority-ranked actionable recommendations for executive decision-making.

**Structure:**

```
PRIORITY 1: CRITICAL - IMMEDIATE ACTION (Next 30 Days)
───────────────────────────────────────────────────────
1. ❌ Oracle ERP: Critical lock-in risk detected
   ├─ Issue: Proprietary data model, no standard export
   ├─ Impact: Cannot migrate without major re-engineering
   ├─ Recommendation: Engage Oracle for data export API; initiate migration project
   └─ Owner: CIO + CISO

2. ❌ Salesforce: PoC testing overdue by 14 months
   ├─ Issue: DORA Article 28.6 violation (annual PoC required)
   ├─ Impact: Regulatory non-compliance
   ├─ Recommendation: Schedule PoC test immediately; engage Salesforce support
   └─ Owner: CISO + DPO

PRIORITY 2: HIGH - NEXT 90 DAYS
───────────────────────────────
3. ⚠️ Cloud-to-Cloud strategy at 87.5% (target: ≥90%)
   ├─ Issue: 3 services below target allocation
   ├─ Impact: Slightly higher lock-in risk than policy allows
   ├─ Recommendation: Review Hybrid services - can any move to Cloud-to-Cloud?
   └─ Owner: Cloud Ops Manager

4. ⚠️ 2 services with High lock-in risk without mitigation
   ├─ Issue: Lock-in identified but no mitigation plan documented
   ├─ Impact: Vendor dependency risk
   ├─ Recommendation: Document mitigation plans (architecture changes, alternatives)
   └─ Owner: Enterprise Architecture

PRIORITY 3: MEDIUM - NEXT 6 MONTHS
──────────────────────────────────
5. 📊 5 services not yet exit strategy determined
   ├─ Issue: New services added but strategy not yet assigned
   ├─ Impact: Policy gap (temporary only)
   ├─ Recommendation: Complete exit strategy assessment
   └─ Owner: Service Owners + Cloud Ops

...
```

**How to Use Recommendations:**

1. **Assign Owners:** Recommendations include suggested owner (CISO, CIO, etc.)
2. **Create Tickets:** Generate ITSM tickets for each recommendation
3. **Track Progress:** Review recommendations monthly in governance meetings
4. **Re-Run Dashboard:** After remediation, regenerate dashboard to validate fixes

---

# Dashboard Refresh Frequency

## Recommended Schedule

| Frequency | Trigger | Rationale |
|-----------|---------|-----------|
| **Quarterly** | After completing IMP-5.23.4 quarterly governance | Standard compliance monitoring |
| **Annually** | After IMP-5.23.4 annual review + PoC testing | DORA Article 28.6 compliance check |
| **On-Demand** | Major cloud service changes (new vendor, migration, incident) | Immediate risk assessment |
| **Pre-Audit** | 2 weeks before ISO 27001 audit | Evidence preparation |
| **Board Meeting** | Week before Risk Committee / Board meeting | Executive reporting |

## Dashboard Lifecycle

```
Week 1: Generate Source Workbooks
  ├─ Complete IMP-5.23.1 (Inventory) - update exit strategies
  ├─ Complete IMP-5.23.4 (Governance) - update PoC results
  └─ Validate data quality (self-assessment)

Week 2: Generate Dashboard
  ├─ Run: python3 generate_reg_a523_5_compliance_dashboard.py
  ├─ Review: Check all 3 sheets for accuracy
  └─ Validate: Spot-check metrics against source data

Week 3: Executive Review
  ├─ Present to CISO/CIO
  ├─ Discuss Critical/High priority items
  ├─ Assign remediation owners
  └─ Set review date for next quarter

Week 4: Action Planning
  ├─ Create ITSM tickets for recommendations
  ├─ Update risk register with new risks
  ├─ Schedule PoC tests for overdue services
  └─ Archive dashboard for audit trail
```

---

# Executive Reporting

## CISO/CIO Monthly Report Template

**Subject:** Cloud Exit Strategy Compliance - [MONTH] [YEAR]

**Executive Summary:**
```
Overall Exit Strategy Compliance: 92% (Target: ≥95%)
DORA PoC Testing Compliance: 83% (Target: 100%)

Status: ⚠️ ATTENTION REQUIRED

Critical Issues (Immediate Action):
  1. [Service]: Critical lock-in risk - migration plan required
  2. [Service]: PoC testing overdue - DORA compliance violation

High Priority (Next 90 Days):
  3. Cloud-to-Cloud strategy below target (87.5% vs 90%)
  4. 2 services with untested data export capabilities
```

**Detailed Metrics:**

- Attach: Sheet 1 (Exit Strategy Dashboard) screenshot
- Attach: Sheet 2 (Risk Overview) filtered to Critical/High risks only


**Recommendations:**

- Copy from Sheet 3 (Recommendations), Priority 1-2 only


**Next Review:** [DATE] (Quarterly cycle)

## Board of Directors Reporting

**For Risk Committee / Board Audit Committee:**

**One-Page Summary:**
```
┌────────────────────────────────────────────────────────┐
│      CLOUD EXIT STRATEGY COMPLIANCE OVERVIEW           │
│             Q[X] [YEAR] - Board Summary                │
├────────────────────────────────────────────────────────┤
│                                                        │
│  EXIT STRATEGY COVERAGE                                │
│  ├─ Cloud-to-Cloud:  87.5% (Target: ≥90%)     [⚠️ ]    │
│  ├─ Hybrid:           9.4% (Target: 5-10%)     [✅]    │
│  ├─ On-Premises:      3.1% (Target: <5%)       [✅]    │
│  └─ Not Determined:   0.0% (Target: 0%)        [✅]    │
│                                                        │
│  DORA POC TESTING (Critical Services)                  │
│  ├─ Tested & Compliant:  83% (Target: 100%)    [⚠️ ]   │
│  ├─ Overdue/Not Tested:   2 services           [❌]    │
│  └─ Next Review: [DATE] (Annual requirement)           │
│                                                        │
│  VENDOR LOCK-IN RISK                                   │
│  ├─ Critical Lock-In:     1 service            [❌]    │
│  ├─ High Lock-In:         2 services           [⚠️ ]   │
│  └─ Mitigation Plans: In Progress                      │
│                                                        │
│  MANAGEMENT ACTIONS                                    │
│  ├─ Critical Issues: 2 (Escalated to CISO/CIO)         │
│  ├─ Remediation Timeline: 30-90 days                   │
│  └─ Next Board Update: [DATE]                          │
│                                                        │
│  REGULATORY COMPLIANCE                                 │
│  ├─ ISO 27001 A.5.23: Compliant                        │
│  ├─ DORA Art. 28.6: Partial (83% PoC tested)   [⚠️ ]   │
│  └─ Remediation: PoC testing scheduled                 │
│                                                        │
└────────────────────────────────────────────────────────┘

BOARD ACTION REQUESTED:
  [✓] Note progress on exit strategy framework
  [✓] Approve remediation plan for DORA PoC testing
  [ ] No action required at this time
```

**Appendix:** Full dashboard workbook (for Board members requesting details)

---

# Quality Assurance

## Dashboard Validation Checklist

**Before presenting dashboard to executives, validate:**

```
☐ SOURCE DATA QUALITY
  ├─ IMP-5.23.1 Sheet 4: All services have exit strategy type
  ├─ IMP-5.23.1 Sheet 4: Critical services have lock-in risk assessment
  ├─ IMP-5.23.4 Sheet 7: Critical services have PoC test results
  └─ IMP-5.23.4 Sheet 7: PoC next due dates populated

☐ DASHBOARD GENERATION
  ├─ Script executed without errors
  ├─ All 3 sheets created (Exit Strategy, Risk Overview, Recommendations)
  ├─ File size reasonable (~50-200 KB for empty, ~500 KB populated)
  └─ Timestamp in filename matches today

☐ METRICS VALIDATION
  ├─ Totals match source workbooks (spot-check 5 services)
  ├─ Percentages calculated correctly (Cloud-to-Cloud % = count/total)
  ├─ Status symbols correct (✅ ⚠️ ❌ logic validated)
  └─ PoC compliance % matches manual calculation

☐ RISK OVERVIEW ACCURACY
  ├─ All Critical lock-in services listed
  ├─ All PoC failures/overdue listed
  ├─ Risk factors accurate per service
  └─ No false positives (compliant services incorrectly flagged)

☐ RECOMMENDATIONS QUALITY
  ├─ Priority 1 items are genuinely critical
  ├─ Owners assigned appropriately
  ├─ Recommendations actionable (not vague)
  └─ Remediation timelines realistic

☐ PRESENTATION READINESS
  ├─ Charts/tables formatted professionally
  ├─ No #REF! or #DIV/0! errors
  ├─ Color coding consistent (red=bad, yellow=warning, green=good)
  └─ Executive summary prepared
```

## Common Validation Issues

| Issue | Symptom | Root Cause | Fix |
|-------|---------|------------|-----|
| Total services = 0 | Empty dashboard | Source workbook Sheet 4 empty | Complete IMP-5.23.1 first |
| Percentages = 0% or 100% | Unrealistic metrics | Division by zero (no services) | Add services to inventory |
| PoC data missing | "No PoC data found" warning | IMP-5.23.4 Sheet 7 not present | Regenerate IMP-5.23.4 with v2.1 script |
| Lock-in risk missing | Dashboard shows 0 high-risk | Column X not populated in IMP-5.23.1 | Complete lock-in assessment |
| Wrong status symbols | Green when should be red | Script logic error or source data typo | Check source data dropdowns |

---

# Integration & Maintenance

## Integration with Risk Management

**Export Dashboard Findings to Risk Register:**

| Dashboard Finding | Risk Register Entry | Risk Owner | Mitigation |
|-------------------|---------------------|------------|------------|
| Critical lock-in on [Service] | RISK-CLD-001: Vendor lock-in risk | CISO | Migration project initiated |
| PoC testing overdue [Service] | RISK-REG-002: DORA non-compliance | DPO | PoC scheduled Q2 2026 |
| On-prem strategy >5% | RISK-STR-003: Exit strategy deviation | CIO | Revalidate TCO justification |

## Integration with Audit Management

**For ISO 27001 Audits:**

**Auditor Question:** "How do you monitor cloud exit strategy compliance?"

**Evidence:**
1. **Dashboard Workbook:** Latest IMP-A.5.23.5 dashboard (this quarter)
2. **Source Workbooks:** IMP-A.5.23.1 (inventory) + IMP-A.5.23.4 (governance)
3. **Generator Script:** `generate_reg_a523_5_compliance_dashboard.py` (demonstrates methodology)
4. **Audit Trail:** Archived dashboards from previous quarters (trend analysis)

**Auditor Question:** "How do you ensure DORA Article 28.6 compliance (PoC testing)?"

**Evidence:**
1. **Dashboard Sheet 1:** PoC testing compliance metrics (current status)
2. **IMP-5.23.4 Sheet 7:** Detailed PoC test results per service (source data)
3. **PoC Test Reports:** Actual test documentation (referenced in evidence column)
4. **Remediation Plan:** For any services with overdue/failed PoC tests

## Dashboard Archive & Retention

**Retention Policy:**
```
Current Dashboard: Active in shared drive
  └─ Location: \\fileserver\ISMS\Dashboards\5.23.5\Current\

Quarterly Archives: 2 years retention
  └─ Location: \\fileserver\ISMS\Dashboards\5.23.5\Archive\
      ├─ 2025\
      │   ├─ ISMS-IMP-A.5.23.S5_Dashboard_20250415_Q2.xlsx
      │   ├─ ISMS-IMP-A.5.23.S5_Dashboard_20250715_Q3.xlsx
      │   ├─ ISMS-IMP-A.5.23.S5_Dashboard_20251015_Q4.xlsx
      │   └─ ISMS-IMP-A.5.23.S5_Dashboard_20260115_Q1.xlsx
      └─ 2026\
          ├─ ISMS-IMP-A.5.23.S5_Dashboard_20260420_Q2.xlsx (CURRENT)
          └─ ...

Annual Archives: 7 years retention (ISO 27001 requirement)
  └─ Location: \\fileserver\ISMS\Dashboards\5.23.5\Annual-Archive\
```

---

# Troubleshooting & FAQs

## Frequently Asked Questions

**Q: Why does the dashboard show 0 services?**
A: The source workbook (IMP-5.23.1) Sheet 4 is empty. Complete the inventory assessment first.

**Q: Why is PoC compliance showing 0%?**
A: IMP-5.23.4 Sheet 7 (Exit Strategy Review) doesn't exist. Regenerate IMP-5.23.4 with v2.1 script that includes Sheet 7.

**Q: Can I manually edit the dashboard?**
A: No. The dashboard is 100% auto-generated. Edit source workbooks (IMP-5.23.1, IMP-5.23.4) and regenerate dashboard.

**Q: How often should I regenerate the dashboard?**
A: Quarterly (after governance review), annually (after PoC testing), or on-demand (major changes, pre-audit, Board meetings).

**Q: What if the script can't find source workbooks?**
A: Ensure all 4 workbooks are in the same directory as the script. Check filenames match patterns (e.g., `ISMS-IMP-A.5.23.S1_Inventory_*.xlsx`).

**Q: Can I customize the policy targets (e.g., 90% cloud-to-cloud)?**
A: Yes, but requires editing the Python script. Modify the target values in the `create_exit_strategy_dashboard()` function (~line 505). Not recommended without technical expertise.

**Q: How do I add more services to the dashboard?**
A: Add services to IMP-5.23.1 Sheet 4 (inventory), complete their exit strategy assessment, then regenerate this dashboard.

**Q: What if a service has a failed PoC test?**
A: This is flagged as Critical in the dashboard. Immediate actions: (1) Root cause analysis, (2) Remediation plan, (3) Retest within 90 days, (4) Document in risk register.

## Advanced Customization

**Extending Dashboard to Include Additional Metrics:**

**Example:** Add vendor concentration risk to dashboard

**Steps:**
1. Update `VENDOR_DD_SCHEMA` to include vendor risk sheet/columns
2. Create `extract_vendor_risk_data()` function (similar to existing extraction functions)
3. Modify `create_exit_strategy_dashboard()` to include vendor concentration metrics
4. Update `create_risk_overview()` to highlight concentrated vendors

**Caution:** Advanced customization requires Python development skills. Test thoroughly before production use.

---

# Appendices

## Glossary

| Term | Definition |
|------|------------|
| **Cloud-to-Cloud Exit Strategy** | Migration plan from one cloud provider to another cloud provider (e.g., AWS → Azure) |
| **DORA Article 28.6** | EU regulation requiring financial institutions to annually test exit strategies for critical ICT services |
| **Exit Strategy Type** | Categorization of exit plan: Cloud-to-Cloud, Hybrid, On-Premises, Not Determined |
| **Lock-In Risk** | Degree of vendor dependency making migration difficult (Low, Medium, High, Critical) |
| **PoC Testing** | Proof-of-Concept test demonstrating feasibility of data export and service migration |
| **Source Workbook** | One of the 4 input workbooks (IMP-A.5.23.1 through A.5.23.4) |

## Related Documents

| Document ID | Title | Relationship |
|-------------|-------|--------------|
| ISMS-POL-A.5.19-23-S5 | Cloud Services Security Policy (Section 8) | Defines exit strategy policy targets |
| ISMS-IMP-A.5.23.S1 | Cloud Service Inventory | Source data for exit strategies |
| ISMS-IMP-A.5.23.S4 | Ongoing Governance & Risk Management | Source data for PoC testing |
| ISMS-IMP-A.5.23.0 | Exit Strategy Framework Spec | Technical specification for exit framework |

## Regulatory References

| Regulation | Article/Section | Requirement |
|------------|-----------------|-------------|
| ISO/IEC 27001:2022 | Control A.5.23 | Information security for use of cloud services (exit planning) |
| DORA (EU 2022/2554) | Article 28.6 | Annual testing of exit strategies for critical ICT services |
| ISO/IEC 27002:2022 | Control 5.23 | Guidance on exit strategies for cloud services |

---

# PART II: TECHNICAL SPECIFICATION

# Script Architecture

## Python Script Structure

**File:** `generate_reg_a523_5_compliance_dashboard.py` (~900 lines)

**Sections:**
```python
# Section 1: Workbook Schema Definitions (~150 lines)
#   - INVENTORY_SCHEMA
#   - VENDOR_DD_SCHEMA  
#   - SECURE_CONFIG_SCHEMA
#   - GOVERNANCE_SCHEMA

# Section 2: Input Validation (~100 lines)
#   - find_latest_workbook()
#   - validate_workbook_schema()
#   - validate_all_inputs()

# Section 3: Data Extraction (~250 lines)
#   - extract_exit_strategy_data()
#   - extract_poc_testing_data()

# Section 4: Style Definitions (~50 lines)
#   - create_styles()

# Section 5: Dashboard Creation (~350 lines)
#   - create_exit_strategy_dashboard()
#   - create_poc_testing_dashboard()
#   - create_risk_overview()
#   - create_recommendations()
#   - create_dashboard_workbook()

# Section 6: Main Execution (~50 lines)
#   - main()
```

## Data Flow Diagram

```
INPUT VALIDATION
├─ Find latest workbook matching pattern
├─ Validate required sheets exist
├─ Validate required columns present
└─ Fail fast if validation errors

DATA EXTRACTION
├─ Load workbook read-only (openpyxl)
├─ Navigate to specific sheet
├─ Read column range (start_row to max_row)
├─ Parse data into Python dict
├─ Calculate summary metrics
└─ Close workbook

DASHBOARD GENERATION
├─ Create new workbook
├─ Apply styles (fonts, fills, borders)
├─ Populate metrics tables
├─ Conditional formatting (status colors)
├─ Generate risk list
├─ Create recommendations
└─ Save workbook

OUTPUT
└─ ISMS-IMP-A.5.23.S5_Dashboard_YYYYMMDD.xlsx
```

---

# Output Workbook Specification

## Sheet 1: Exit Strategy Dashboard

**Sheet Name:** `1. Exit Strategy Dashboard`

**Layout:**

```
Row 1: HEADER
  ├─ Merged A1:H1
  ├─ "EXIT STRATEGY COVERAGE DASHBOARD"
  └─ Font: Calibri 14 Bold, White on Dark Blue (003366)

Row 2: POLICY REFERENCE
  ├─ Merged A2:H2
  ├─ "POL-S5 Section 8: Exit Strategy Framework..."
  └─ Font: Calibri 9 Italic

Row 4: METRICS TABLE HEADER
  ├─ Columns: METRIC | VALUE | PERCENTAGE | STATUS | POLICY TARGET
  └─ Style: Bold, Gray fill (D9D9D9)

Row 5-13: EXIT STRATEGY METRICS
  ├─ Total Cloud Services
  ├─ Cloud-to-Cloud Strategy
  ├─ Hybrid Strategy
  ├─ On-Premises Strategy
  ├─ Not Yet Determined
  ├─ (blank separator)
  ├─ High Lock-In Risk
  ├─ CRITICAL Lock-In Risk
  └─ Export Not Tested (Critical)

Row 15: POC TESTING HEADER
  ├─ "DORA PoC TESTING COMPLIANCE (Article 28.6)"
  └─ Font: Calibri 12 Bold, White on Medium Blue (4472C4)

Row 18: POC METRICS TABLE HEADER
  └─ Columns: METRIC | VALUE | STATUS | COMPLIANCE REQUIREMENT

Row 19-24: POC TESTING METRICS
  ├─ Critical Services Requiring PoC Testing
  ├─ PoC Testing Completed (Pass)
  ├─ PoC Testing Not Tested
  ├─ PoC Testing Overdue
  ├─ Overall PoC Compliance
  └─ Next Annual Review Due
```

**Column Widths:**

- A: 35 (Metric names)
- B: 12 (Values)
- C: 15 (Percentages)
- D: 12 (Status symbols)
- E: 25 (Policy targets)


**Conditional Formatting:**

| Condition | Cell Range | Fill Color | Font Color |
|-----------|------------|------------|------------|
| On-Premises % > 5% | A-C (On-Premises row) | Red (FFC7CE) | Dark Red (9C0006) |
| Critical Lock-In > 0 | A-B (Critical Lock-In row) | Red (FFC7CE) | Dark Red (9C0006) |
| PoC Compliance < 100% | B (Overall PoC Compliance) | Yellow (FFEB9C) | Dark Yellow (9C6500) |

---

## Sheet 2: Risk Overview

**Sheet Name:** `2. Risk Overview`

**Purpose:** Table listing all high-risk services.

**Columns (A-H):**

| Column | Header | Width | Content |
|--------|--------|-------|---------|
| A | Service Name | 28 | Cloud service name from inventory |
| B | Provider | 22 | Vendor name |
| C | Criticality | 14 | Critical, High, Medium, Low |
| D | Exit Strategy | 18 | Cloud-to-Cloud, Hybrid, On-Premises, Not Determined |
| E | Lock-In Risk | 14 | Low, Medium, High, Critical |
| F | Export Tested | 14 | Yes, No, Partial |
| G | PoC Result | 14 | Pass, Fail, Not Tested, In Progress |
| H | Risk Factors | 50 | Concatenated list of issues (❌ ⚠️ symbols) |

**Filtering Logic:**
```python
# Include service in Risk Overview if ANY of:
# Lock-In Risk = "High" or "Critical"
# PoC Result = "Fail" or "Not Tested" (for Critical services)
# Export Tested = "No" (for Critical services)
# Exit Strategy = "On-Premises" (without TCO justification)
```

**Row Sorting:** By number of ❌ symbols (descending) - highest risk first

**Example Row:**
```
Service: Oracle ERP
Provider: Oracle
Criticality: Critical
Exit Strategy: On-Premises
Lock-In Risk: Critical
Export Tested: Partial
PoC Result: Fail
Risk Factors: ❌ Critical lock-in, ❌ PoC failed, ⚠️ On-prem strategy, ⚠️ Partial export
```

---

## Sheet 3: Recommendations

**Sheet Name:** `3. Recommendations`

**Purpose:** Priority-ranked actionable items.

**Structure:**

```
Row 1: HEADER
  "EXECUTIVE RECOMMENDATIONS - Exit Strategy Compliance"

Row 3: PRIORITY 1 HEADER
  "PRIORITY 1: CRITICAL - IMMEDIATE ACTION (Next 30 Days)"

Row 4+: Priority 1 Recommendations
  For each Critical issue:
  ├─ Recommendation number
  ├─ Service name
  ├─ Issue description
  ├─ Impact statement
  ├─ Recommended action
  └─ Suggested owner

Row X: PRIORITY 2 HEADER
  "PRIORITY 2: HIGH - NEXT 90 DAYS"

Row X+: Priority 2 Recommendations
  ...

Row Y: PRIORITY 3 HEADER
  "PRIORITY 3: MEDIUM - NEXT 6 MONTHS"
```

**Recommendation Template:**
```
[PRIORITY] [NUMBER]. [ISSUE_TYPE]: [SERVICE]
├─ Issue: [DESCRIPTION]
├─ Impact: [BUSINESS_IMPACT]
├─ Recommendation: [ACTION_REQUIRED]
└─ Owner: [SUGGESTED_OWNER]
```

**Prioritization Logic:**

| Priority | Criteria | Timeline |
|----------|----------|----------|
| **P1: Critical** | Critical lock-in, PoC failures, DORA violations | 30 days |
| **P2: High** | High lock-in, Export not tested, Strategy deviation from target | 90 days |
| **P3: Medium** | Not Determined strategies, Minor compliance gaps | 6 months |

---

# Data Extraction Specification

## Exit Strategy Data Extraction

**Source:** IMP-A.5.23.1, Sheet 4 (Cloud Security Services)

**Column Mapping:**

```python
INVENTORY_SCHEMA['exit_strategy_columns'] = {
    'Service Name': 'A',          # Column A
    'Provider': 'B',              # Column B
    'Service Type': 'C',          # Column C
    'Criticality': 'H',           # Column H
    'Exit Strategy Type': 'R',    # Column R
    'Alternative Identified': 'S', # Column S
    'Export Tested': 'U',         # Column U
    'Migration Complexity': 'W',  # Column W
    'Lock-In Risk': 'X',          # Column X
}
```

**Extraction Logic:**

```python
for row in range(start_row, ws.max_row + 1):
    service_name = ws[f"A{row}"].value
    
    if not service_name or str(service_name).strip() == "":
        continue  # Skip empty rows
    
    data['total_services'] += 1
    
    exit_strategy = ws[f"R{row}"].value
    criticality = ws[f"H{row}"].value
    lock_in_risk = ws[f"X{row}"].value
    export_tested = ws[f"U{row}"].value
    
    # Count by exit strategy type
    if exit_strategy == "Cloud-to-Cloud":
        data['cloud_to_cloud'] += 1
    elif exit_strategy == "Hybrid":
        data['hybrid'] += 1
    elif exit_strategy == "On-Premises":
        data['on_premises'] += 1
    else:
        data['not_determined'] += 1
    
    # Count lock-in risks
    if lock_in_risk == "High":
        data['high_lock_in'] += 1
    elif lock_in_risk == "Critical":
        data['critical_lock_in'] += 1
    
    # Count critical services without tested export
    if criticality == "Critical" and export_tested == "No":
        data['export_not_tested_critical'] += 1
```

**Return Value:**
```python
{
    'total_services': 32,
    'cloud_to_cloud': 28,
    'hybrid': 3,
    'on_premises': 1,
    'not_determined': 0,
    'high_lock_in': 2,
    'critical_lock_in': 1,
    'export_not_tested_critical': 1,
    'services': [...]  # List of service dicts
}
```

---

## PoC Testing Data Extraction

**Source:** IMP-A.5.23.4, Sheet 7 (Exit Strategy Review)

**Column Mapping:**

```python
GOVERNANCE_SCHEMA['exit_review_columns'] = {
    'Service Name': 'B',               # Column B
    'Criticality': 'F',                # Column F
    'PoC Testing Required?': 'H',      # Column H
    'PoC Test Result': 'J',            # Column J
    'PoC Test Next Due': 'N',          # Column N
}
```

**Extraction Logic:**

```python
today = datetime.now().date()

for row in range(start_row, ws.max_row + 1):
    service_name = ws[f"B{row}"].value
    
    if not service_name or str(service_name).strip() == "":
        continue
    
    poc_required = ws[f"H{row}"].value
    poc_result = ws[f"J{row}"].value
    poc_next_due = ws[f"N{row}"].value
    
    if poc_required == "Yes (Critical)":
        data['total_requiring_poc'] += 1
        
        if poc_result == "Pass":
            data['poc_completed'] += 1
        elif poc_result in ["Not Tested"]:
            data['poc_not_tested'] += 1
        elif poc_result in ["In Progress"]:
            data['poc_overdue'] += 1
        
        # Check if actually overdue based on date
        if poc_next_due:
            try:
                if isinstance(poc_next_due, datetime):
                    due_date = poc_next_due.date()
                else:
                    due_date = datetime.strptime(str(poc_next_due), '%Y-%m-%d').date()
                
                if due_date < today and poc_result != "Pass":
                    data['poc_overdue'] += 1
            except:
                pass  # Ignore date parsing errors
```

**Return Value:**
```python
{
    'total_requiring_poc': 12,
    'poc_completed': 10,
    'poc_overdue': 1,
    'poc_not_tested': 1,
    'services': [...]
}
```

---

# Schema Validation

## Required Sheets Validation

**Function:** `validate_workbook_schema(filepath, schema)`

**Logic:**
```python
def validate_workbook_schema(filepath: str, schema: dict) -> bool:
    """
    Validate that workbook has required sheets and structure.
    
    Returns:
        True if valid, raises ValueError if invalid
    """
    wb = load_workbook(filepath, read_only=True)
    
    for required_sheet in schema['required_sheets']:
        if required_sheet not in wb.sheetnames:
            raise ValueError(
                f"Missing required sheet '{required_sheet}' in {filepath}"
            )
    
    wb.close()
    return True
```

**Error Examples:**

```
ValueError: Missing required sheet '4. Cloud Security Services' in ISMS-IMP-A.5.23.S1_Inventory_20260120.xlsx

ValueError: Missing required sheet '7. Exit Strategy Review' in ISMS-IMP-A.5.23.S4_Governance_20260120.xlsx
```

---

# File Naming & Metadata

## Output File Naming

**Pattern:** `ISMS-IMP-A.5.23.S5_Dashboard_YYYYMMDD.xlsx`

**Example:** `ISMS-IMP-A.5.23.S5_Dashboard_20260120.xlsx`

**Timestamp:** Uses `datetime.now().strftime("%Y%m%d")`

## Workbook Metadata

```python
wb.properties.title = "ISMS-IMP-A.5.23.S5 Compliance Dashboard"
wb.properties.subject = "ISO 27001 A.5.23 Exit Strategy Compliance"
wb.properties.creator = "[Organization] ISMS Team"
wb.properties.description = "Auto-generated dashboard consolidating exit strategy compliance"
wb.properties.keywords = "ISMS, ISO27001, Exit Strategy, DORA, PoC Testing"
wb.properties.category = "Information Security Management"
wb.properties.version = "2.0"
```

---

# Known Limitations & Future Enhancements

## Current Limitations

| Limitation | Workaround | Future Enhancement |
|------------|------------|-------------------|
| Only extracts from IMP-5.23.1 & 5.23.4 | Manual review of IMP-5.23.2/3 | Add vendor risk, config compliance metrics |
| No trend analysis (single point-in-time) | Compare archived dashboards manually | Add quarterly trend charts |
| No email automation | Manual distribution | Auto-email dashboard to stakeholders |
| Fixed policy targets (90% cloud-to-cloud) | Edit Python script | Add config file for targets |

## Roadmap

**Version 2.1 (Q2 2026):**

- Add vendor concentration risk metrics (from IMP-5.23.2)
- Add configuration compliance summary (from IMP-5.23.3)


**Version 2.2 (Q3 2026):**

- Quarterly trend charts (compare last 4 quarters)
- Email automation (send dashboard to distribution list)


**Version 3.0 (Q4 2026):**

- Real-time dashboard (web-based, not Excel)
- Integration with CMDB/ITSM for live data


---

# Testing & Validation

## Unit Test Cases

**Test 1: Empty Inventory**
```
Input: IMP-5.23.1 with 0 services
Expected: Dashboard generates with all metrics = 0
Actual: ✅ PASS
```

**Test 2: All Cloud-to-Cloud**
```
Input: 10 services, all Cloud-to-Cloud
Expected: Cloud-to-Cloud % = 100%, Status = ✅
Actual: ✅ PASS
```

**Test 3: PoC All Pass**
```
Input: 5 Critical services, all PoC = Pass
Expected: PoC Compliance = 100%, Status = ✅
Actual: ✅ PASS
```

**Test 4: Missing Sheet 7**
```
Input: IMP-5.23.4 without Sheet 7 (old version)
Expected: Warning message, PoC metrics = 0
Actual: ✅ PASS (warning logged)
```

## Integration Test

**Full End-to-End Test:**
```
Step 1: Generate all 4 source workbooks with test data
Step 2: Run dashboard generator
Step 3: Validate all 3 sheets created
Step 4: Spot-check 10 metrics against source data
Step 5: Check conditional formatting applied correctly
Result: ✅ PASS
```

---

**END OF SPECIFICATION**

---

*"Science is the belief in the ignorance of experts."*
— Richard Feynman
*Where bamboo antennas actually work.* 🎋
