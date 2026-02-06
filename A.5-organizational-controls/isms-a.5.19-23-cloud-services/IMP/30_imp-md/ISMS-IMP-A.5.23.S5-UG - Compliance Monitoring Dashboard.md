**ISMS-IMP-A.5.23.S5-UG - Compliance Monitoring Dashboard**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.5.23: Information Security for Use of Cloud Services

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.23.S5-UG |
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


**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
