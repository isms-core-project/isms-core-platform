**ISMS-IMP-A.8.12.5 - Compliance Dashboard**
**Assessment Specification with User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.12: Data Leakage Prevention

# PART I: USER COMPLETION GUIDE

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.12.5 |
| **Version** | 1.0 |
| **Assessment Area** | DLP Compliance Dashboard and Consolidated Reporting |
| **Related Policy** | ISMS-POL-A.8.12 (Data Leakage Prevention Policy) - All Sections |
| **Purpose** | Consolidate data from all DLP assessments (Infrastructure, Classification, Channel Coverage, Monitoring & Response) into unified executive dashboard for CISO reporting and audit readiness verification |
| **Target Audience** | CISO, DPO, Compliance Officers, Internal Audit, Executive Management, External Auditors |
| **Assessment Type** | Consolidation & Executive Reporting |
| **Review Cycle** | Quarterly (after all source assessments completed) |
| **Date** | 21.01.2026 |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial specification for Compliance Dashboard | ISMS Implementation Team |

---

# PART I: USER COMPLETION GUIDE
**Audience:** CISO, Compliance Officers, DLP Program Managers, Internal Audit

---

# Assessment Overview

## What This Assessment Measures

This assessment **consolidates and visualizes** compliance data from all four DLP assessments to provide executive-level visibility and audit readiness verification.

**Scope:** Consolidation of 4 source assessments:
1. **A.8.12.1 - DLP Infrastructure Assessment** → Technology deployment and capabilities
2. **A.8.12.2 - Data Classification Assessment** → Classification scheme and pattern accuracy
3. **A.8.12.3 - Channel Coverage Assessment** → Channel protection and bypass prevention
4. **A.8.12.4 - Monitoring & Response Assessment** → SOC integration and incident response

**Assessment Output:** Executive dashboard workbook with:

- Overall DLP compliance score (weighted across all domains)
- Compliance by assessment area (4 source assessments)
- Critical gaps requiring executive attention
- Audit readiness status
- Trend analysis (quarter-over-quarter comparison)
- Evidence completeness verification
- Executive summary for board reporting

## Why This Matters

**ISO 27001:2022 Control A.8.12 Requirement:**
> *"Data leakage prevention measures should be applied to systems, networks and any other devices that process, store or transmit sensitive information."*

**Executive Need:** CISO and Executive Management require consolidated view of DLP program effectiveness, not individual technical assessments.

**Audit Requirement:** External auditors (ISO 27001, SOC 2, etc.) need evidence that DLP controls are:
1. **Deployed** (Infrastructure)
2. **Configured correctly** (Classification, Channel Coverage)
3. **Operationally effective** (Monitoring & Response)
4. **Documented and evidenced** (All assessments)

**Regulatory Context:**

- **Swiss nDSG (Art. 8):** Requires demonstration of appropriate technical measures
- **EU GDPR (Art. 32):** Requires ability to demonstrate compliance with technical measures
- **Industry Standards:** PCI DSS, HIPAA, SOC 2 all require consolidated security control reporting

**Business Impact:**

- **Executive Decision-Making:** Resource allocation, budget approval, risk acceptance based on consolidated view
- **Audit Efficiency:** Single dashboard showing all DLP compliance status accelerates audit process
- **Gap Prioritization:** Consolidated critical gaps enable focused remediation efforts
- **Board Reporting:** Executive summary suitable for board cybersecurity reporting

**Why Dashboard Consolidation Matters:**

- **Single Source of Truth:** One definitive view of DLP compliance status
- **Trend Analysis:** Quarter-over-quarter comparison shows improvement/degradation
- **Evidence Verification:** Confirms all required evidence collected across all assessments
- **Audit Readiness:** Pre-audit verification that DLP controls are documented and compliant

## Who Should Complete This Assessment

**Primary Responsibility:** DLP Program Manager, CISO Office, Compliance Team

**Required Knowledge:**

- Completion status of all 4 source assessments (must be completed first)
- Location of source assessment workbooks (file paths)
- Excel external workbook linking (how to create and update links)
- Executive reporting requirements (what CISO/board needs to see)

**Support Roles:**

- **DLP Administrators:** Provide technical context for consolidated findings
- **Internal Audit:** Verify audit readiness status
- **Compliance Officers:** Review regulatory alignment
- **CISO/Security Leadership:** Review executive summary and approve risk acceptances

**CRITICAL PREREQUISITE:** All 4 source assessments MUST be completed before dashboard consolidation:

- [ ] A.8.12.1 - Infrastructure Assessment completed
- [ ] A.8.12.2 - Classification Assessment completed
- [ ] A.8.12.3 - Channel Coverage Assessment completed
- [ ] A.8.12.4 - Monitoring & Response Assessment completed

## Time Estimate

**Total Time:** 2-3 hours (assuming all source assessments already completed)

**Breakdown:**

- **Source File Preparation:** 30 minutes (collect all 4 source workbooks, verify completion)
- **Dashboard Setup:** 30 minutes (configure external workbook links, verify formulas calculate)
- **Consolidation Verification:** 30-60 minutes (verify data pulls correctly from source workbooks)
- **Critical Gaps Review:** 30 minutes (consolidate gaps from all 4 assessments, prioritize)
- **Executive Summary Generation:** 30 minutes (write summary for CISO/board)
- **Evidence Verification:** 15 minutes (confirm all evidence present across all assessments)
- **Quality Review:** 15 minutes (self-check using Section 7 quality checklist)

**IMPORTANT:** If source assessments are incomplete or have data quality issues, dashboard consolidation will take longer (4-6 hours) to identify and resolve data issues.

## Connection to Policy

This assessment implements **ISMS-POL-A.8.12 (Data Leakage Prevention Policy)** All Sections by providing consolidated compliance verification:

**Policy Requirements Verified:**

- **Section 2.1 - Data Classification:** Via A.8.12.2 assessment consolidation
- **Section 2.2 - Channel Protection:** Via A.8.12.3 assessment consolidation
- **Section 2.3 - Monitoring & Detection:** Via A.8.12.4 assessment consolidation
- **Section 3.2 - Assessment & Verification:** THIS dashboard is the quarterly verification deliverable
- **Section 4.1 - Roles & Responsibilities:** CISO accountability verified through approval workflow
- **Section 4.2 - Implementation Resources:** Evidence completeness verified
- **Section 5.1 - Review Cycle:** Quarterly dashboard updates per policy requirement

**Policy Authority:** Chief Information Security Officer (CISO)  
**Compliance Status:** Mandatory quarterly deliverable to Executive Management

**Relationship to Other Assessments:**

- **A.8.12.1-4:** Source assessments → THIS dashboard consolidates all
- **Executive Reporting:** THIS dashboard provides board-ready summary
- **Audit Process:** THIS dashboard is primary artifact for ISO 27001/SOC 2 auditors

## Critical: Consolidation Methodology

**⚠️ IMPORTANT - Dashboard Quality Depends on Source Assessment Quality:**

This dashboard consolidates data via **external workbook links** from 4 source assessment workbooks. Data quality issues in source assessments will propagate to dashboard.

**Consolidation Architecture:**

```
Source Workbooks (4 files):
├── ISMS-IMP-A.8.12.1_Infrastructure_YYYYMMDD.xlsx
├── ISMS-IMP-A.8.12.2_Classification_YYYYMMDD.xlsx
├── ISMS-IMP-A.8.12.3_Channel_Coverage_YYYYMMDD.xlsx
└── ISMS-IMP-A.8.12.4_Monitoring_Response_YYYYMMDD.xlsx

Dashboard Workbook (this file):
└── ISMS-IMP-A.8.12.5_Compliance_Dashboard_YYYYMMDD.xlsx
    ├── Links to Summary_Dashboard sheet in each source workbook
    ├── Consolidates compliance percentages
    ├── Aggregates critical gaps
    └── Generates executive summary
```

**Data Flow:**
1. **Source assessments completed** → Data entered by assessment owners
2. **Source workbooks saved** → Final approved versions
3. **Dashboard created** → External links established to source workbooks
4. **Data auto-updates** → Dashboard pulls latest data from source files
5. **Executive summary generated** → Based on consolidated metrics

**External Workbook Linking Requirements:**

- All 4 source workbooks must be in **same directory** as dashboard workbook
- Filenames must follow naming convention: `ISMS-IMP-A.8.12.X_[Name]_YYYYMMDD.xlsx`
- Source workbooks must be **closed** when updating dashboard links (Excel limitation)
- When source data changes, dashboard formulas auto-update (if links valid)

**Common Linking Issues:**

- **#REF! errors:** Source workbook moved or renamed → Update links via Edit Links dialog
- **Stale data:** Source workbook updated but dashboard not refreshed → Click "Update Values" in Edit Links
- **Circular reference:** Dashboard references itself → Review formula references
- **File path too long:** Windows 260-character path limit → Shorten directory path

**Quality Dependency:**

- If source assessment has ❌ Non-Compliant items → Dashboard shows ❌
- If source assessment missing evidence → Dashboard shows evidence gap
- If source assessment formulas broken → Dashboard shows #REF! or #VALUE!

**Best Practice:**
1. Complete ALL source assessments to high quality standard BEFORE creating dashboard
2. Have source assessment owners review and approve BEFORE consolidation
3. Store all 5 workbooks in single dedicated directory (e.g., `ISMS/A.8.12_DLP/Q1_2026/`)
4. Create dashboard, verify links, test formulas
5. Freeze source workbooks (mark as "FINAL APPROVED" version)
6. Update dashboard quarterly when source assessments refreshed

---

# Prerequisites

## Access Required

**Source Assessment Workbooks (4 files):**

- [ ] `ISMS-IMP-A.8.12.1_Infrastructure_YYYYMMDD.xlsx` - Completed and approved
- [ ] `ISMS-IMP-A.8.12.2_Classification_YYYYMMDD.xlsx` - Completed and approved
- [ ] `ISMS-IMP-A.8.12.3_Channel_Coverage_YYYYMMDD.xlsx` - Completed and approved
- [ ] `ISMS-IMP-A.8.12.4_Monitoring_Response_YYYYMMDD.xlsx` - Completed and approved

**All Source Workbooks Requirements:**

- Summary_Dashboard sheet completed (formulas calculated, no errors)
- Gap_Analysis sheet completed (all critical gaps documented)
- Evidence_Register populated (evidence IDs assigned)
- Approval_Sign-Off completed (signed by appropriate authorities)

**Policy Documentation:**

- [ ] ISMS-POL-A.8.12 Data Leakage Prevention Policy (current approved version)
- [ ] Previous quarter dashboard (if exists, for trend comparison)

## Knowledge Required

**Essential Understanding:**

- Excel external workbook references (how to create and maintain links)
- DLP assessment framework (what each source assessment measures)
- Executive reporting requirements (what CISO/board needs)
- Risk prioritization (Critical vs High vs Medium gaps)

**Technical Skills:**

- Excel formula auditing (trace precedents, evaluate formulas)
- Excel link management (Edit Links dialog, update links, break links)
- Data validation (verify consolidated data matches source)
- Conditional formatting (understand color coding rules)

**NOT Required:**

- Deep DLP technical expertise (source assessments have details)
- Advanced Excel VBA/macros
- Business intelligence tool expertise

## Tools Needed

**Required:**

- **Microsoft Excel** (2016 or later) or **LibreOffice Calc** (6.0 or later)
- **File system access** to directory containing all 5 workbooks
- **Read/write permissions** on all workbook files

**Optional but Recommended:**

- **Excel Formula Auditing toolbar** (for link troubleshooting)
- **PDF export capability** (for executive summary distribution)

## Estimated Time Commitment

**Phase 1: Source File Preparation (30 minutes)**

- Collect all 4 source assessment workbooks
- Verify each is completed (no missing data, formulas calculate)
- Place all files in single directory
- Note exact filenames for linking

**Phase 2: Dashboard Creation (30 minutes)**

- Open dashboard template (or generate via Python script)
- Establish external links to 4 source workbooks
- Verify formulas calculate correctly (no #REF! errors)
- Test link updates (modify source data, verify dashboard updates)

**Phase 3: Consolidation Verification (30-60 minutes)**

- Verify Overall Compliance % matches source calculations
- Check each domain compliance % pulls correctly
- Verify critical gaps consolidated from all sources
- Confirm evidence count matches sources

**Phase 4: Critical Gaps Review & Prioritization (30 minutes)**

- Review all critical gaps from 4 source assessments
- Prioritize for executive attention (top 5-10 gaps)
- Verify remediation plans exist and are realistic
- Check owners and target dates assigned

**Phase 5: Executive Summary Generation (30 minutes)**

- Write 1-2 page executive summary
- Highlight overall compliance score
- List top critical gaps
- Provide trend analysis (vs. previous quarter)
- Recommend executive actions (budget, risk acceptance, remediation)

**Phase 6: Quality Assurance (15 minutes)**

- Self-check using quality checklist (Section 7)
- Verify all external links active
- Check for formula errors
- Confirm evidence completeness

**Total:** 2-3 hours

---

# Assessment Workflow

## Recommended Completion Sequence

**STEP 1: Pre-Assessment Verification (15 minutes)**
1. Verify all 4 source assessments completed:

   - [ ] A.8.12.1 Infrastructure - Status: ✅ Complete
   - [ ] A.8.12.2 Classification - Status: ✅ Complete
   - [ ] A.8.12.3 Channel Coverage - Status: ✅ Complete
   - [ ] A.8.12.4 Monitoring & Response - Status: ✅ Complete

2. Verify each source workbook has:

   - [ ] Summary_Dashboard sheet (with calculated metrics)
   - [ ] Gap_Analysis sheet (critical gaps documented)
   - [ ] Evidence_Register sheet (evidence collected)
   - [ ] Approval_Sign-Off sheet (signed and dated)

3. If any source incomplete → STOP, complete source assessment first

**STEP 2: File Organization (10 minutes)**
1. Create dedicated directory: `ISMS/A.8.12_DLP/Q1_2026/` (adjust quarter as appropriate)
2. Copy all 4 source assessment workbooks to this directory
3. Ensure filenames follow convention:

   - `ISMS-IMP-A.8.12.1_Infrastructure_20260121.xlsx`
   - `ISMS-IMP-A.8.12.2_Classification_20260121.xlsx`
   - `ISMS-IMP-A.8.12.3_Channel_Coverage_20260121.xlsx`
   - `ISMS-IMP-A.8.12.4_Monitoring_Response_20260121.xlsx`

4. Generate dashboard workbook, save to same directory:

   - `ISMS-IMP-A.8.12.5_Compliance_Dashboard_20260121.xlsx`

**STEP 3: Dashboard Setup (30 minutes)**
1. Open dashboard workbook: `ISMS-IMP-A.8.12.5_Compliance_Dashboard_20260121.xlsx`
2. Navigate to Instructions_Legend sheet
3. Complete Organization Metadata (yellow cells)
4. Navigate to Consolidated_Metrics sheet
5. Verify external link formulas reference correct source files:

   - Example formula: `=[ISMS-IMP-A.8.12.1_Infrastructure_20260121.xlsx]Summary_Dashboard!$B$7`

6. If formulas show #REF! → Update links via Data → Edit Links
7. Verify all formulas calculate (no errors)

**STEP 4: Overall Compliance Calculation (15 minutes)**
1. Navigate to Executive_Summary sheet
2. Verify "Overall DLP Compliance %" calculated correctly:

   - Formula pulls from each source workbook's Summary_Dashboard
   - Weighted average: Infrastructure 25%, Classification 25%, Coverage 25%, Monitoring 25%

3. Check status color coding:

   - ≥90% = Green (Compliant)
   - 80-89% = Yellow (Partial)
   - <80% = Red (Non-Compliant)

4. Review compliance by domain (4 source assessments)
5. Verify trend vs. previous quarter (if applicable)

**STEP 5: Critical Gaps Consolidation (30 minutes)**
1. Navigate to Critical_Gaps_Consolidated sheet
2. Verify critical gaps pulled from all 4 source workbooks:

   - A.8.12.1 Gap_Analysis → Filter Risk Level = "Critical"
   - A.8.12.2 Gap_Analysis → Filter Risk Level = "Critical"
   - A.8.12.3 Gap_Analysis → Filter Risk Level = "Critical"
   - A.8.12.4 Gap_Analysis → Filter Risk Level = "Critical"

3. Total critical gaps count (target: 0)
4. For each critical gap:

   - Verify remediation action defined
   - Check owner assigned
   - Confirm target date realistic
   - Review regulatory impact

5. Prioritize top 5-10 gaps for executive attention

**STEP 6: Evidence Verification (15 minutes)**
1. Navigate to Evidence_Summary sheet
2. Verify evidence count from each source:

   - A.8.12.1 Infrastructure: Expected ~15 evidence items
   - A.8.12.2 Classification: Expected ~15 evidence items
   - A.8.12.3 Channel Coverage: Expected ~15 evidence items
   - A.8.12.4 Monitoring & Response: Expected ~10 evidence items
   - **Total expected: ~55 evidence items**

3. Flag any source with insufficient evidence
4. Verify evidence types:

   - Policy documents (classification policy, SOC playbooks)
   - Configuration screenshots (DLP rules, SIEM integration)
   - Test results (bypass testing, SIEM end-to-end tests)
   - Metrics (alert volume, MTTR, FP rate)

**STEP 7: Executive Summary Generation (30 minutes)**
1. Navigate to Executive_Summary sheet
2. Write executive summary (1-2 pages):

   - **Overall Status:** Compliance score, color-coded status
   - **Key Highlights:** What's working well (compliant domains)
   - **Critical Gaps:** Top 5-10 issues requiring executive attention
   - **Trend Analysis:** Improvement/degradation vs. previous quarter
   - **Resource Needs:** Budget, staffing, tools required for remediation
   - **Risk Acceptance Recommendations:** Which gaps to accept vs. remediate
   - **Audit Readiness:** Is DLP program audit-ready? (Yes/No with justification)

3. Format for board presentation (concise, executive language, no jargon)

**STEP 8: Trend Analysis (if previous quarter exists) (15 minutes)**
1. Navigate to Trend_Analysis sheet
2. Compare current quarter vs. previous quarter:

   - Overall compliance % (improving/stable/degrading?)
   - Critical gaps count (reducing/stable/increasing?)
   - Evidence completeness (improving?)

3. Document reasons for changes:

   - Example: "Compliance improved from 75% to 85% due to SIEM integration completion"
   - Example: "Critical gaps increased from 2 to 5 due to new regulatory requirements"

**STEP 9: Quality Assurance (15 minutes)**
1. Complete quality checklist (Section 7)
2. Verify all external links functional:

   - Excel: Data → Edit Links → Status should show "OK" for all links
   - If "Error" → Fix file paths, update links

3. Test link updates:

   - Modify value in source workbook
   - Verify dashboard updates automatically

4. Check for formula errors (#REF!, #VALUE!, #DIV/0!)
5. Verify conditional formatting working (colors correct)

**STEP 10: Approval & Distribution (15 minutes)**
1. Navigate to Approval_Sign-Off sheet
2. Complete approval workflow:

   - Completed By: DLP Program Manager
   - Reviewed By: Compliance Officer
   - Approved By: CISO

3. Export Executive Summary to PDF for board distribution
4. Save final dashboard workbook
5. Distribute to stakeholders (CISO, Executive Management, Internal Audit)

---

# Sheet-by-Sheet Guidance

## Sheet: Executive_Summary

**Assessment Question:** *"What is the overall DLP compliance status and what are the top executive-level concerns?"*

**Understanding the Requirement:**

This sheet provides board-ready executive summary suitable for CISO reporting to Executive Management.

**Field Guidance:**

| Field | How to Complete | Examples | Where to Find |
|-------|-----------------|----------|---------------|
| **Overall DLP Compliance %** | Auto-calculated from sources | 85% (Yellow) | Formula references 4 source dashboards |
| **Status** | Auto-determined by % | ✅ / ⚠️ / ❌ | Conditional formatting |
| **Infrastructure Compliance %** | From A.8.12.1 | 90% (Green) | External link to A.8.12.1 Summary_Dashboard |
| **Classification Compliance %** | From A.8.12.2 | 75% (Yellow) | External link to A.8.12.2 Summary_Dashboard |
| **Channel Coverage Compliance %** | From A.8.12.3 | 88% (Yellow) | External link to A.8.12.3 Summary_Dashboard |
| **Monitoring Compliance %** | From A.8.12.4 | 87% (Yellow) | External link to A.8.12.4 Summary_Dashboard |
| **Total Critical Gaps** | Count from all sources | 7 (Red flag) | Consolidated from 4 Gap_Analysis sheets |
| **Total Evidence Items** | Count from all sources | 58 (Adequate) | Consolidated from 4 Evidence_Register sheets |
| **Audit Readiness** | Assessment judgment | Ready / Not Ready / Partially Ready | Based on compliance % + gaps + evidence |
| **Trend vs. Previous Quarter** | Comparison | +10% (Improving) | Compare to previous dashboard |

**Status Determination:**

**✅ Audit-Ready (Green):**

- Overall compliance ≥90%
- All domains ≥85%
- Critical gaps = 0
- Total evidence ≥50 items
- All approvals signed

**⚠️ Partially Ready (Yellow):**

- Overall compliance 80-89%
- Some domains <85% but all >75%
- Critical gaps 1-5
- Evidence ≥40 items
- Minor documentation gaps

**❌ Not Audit-Ready (Red):**

- Overall compliance <80%
- Any domain <75%
- Critical gaps >5
- Evidence <40 items
- Major gaps requiring immediate remediation

**Executive Summary Template:**

```
EXECUTIVE SUMMARY - DLP COMPLIANCE STATUS
Quarter: Q1 2026
Prepared For: Executive Management / Board of Directors
Prepared By: CISO

OVERALL STATUS: [85%] ⚠️ PARTIALLY COMPLIANT

KEY HIGHLIGHTS:
✅ DLP infrastructure fully deployed across all channels
✅ SIEM integration complete, 24/7 SOC monitoring operational
✅ Pattern accuracy >90%, false positive rate reduced to 12%

CRITICAL GAPS REQUIRING EXECUTIVE ATTENTION:
1. [Gap description] - Impact: [regulatory/business] - Target: [date] - Owner: [name]
2. [Gap description] - Impact: [regulatory/business] - Target: [date] - Owner: [name]
[List top 5-10]

TREND ANALYSIS:
Previous Quarter: 75% → Current: 85% (+10% improvement)

- Improvement drivers: SIEM integration, SOC playbook deployment
- Remaining challenges: Data classification scheme incomplete, mobile DLP gaps

RESOURCE REQUIREMENTS:

- Budget: CHF [amount] for [purpose]
- Staffing: [FTE] additional SOC analysts for alert management
- Tools: [tool name] for [capability gap]

RISK ACCEPTANCE RECOMMENDATIONS:

- Accept: [Gap X] - Low risk, high cost to remediate, compensating controls in place
- Remediate: [Gap Y] - High regulatory risk (GDPR), must fix before audit

AUDIT READINESS: PARTIALLY READY

- Recommendation: Complete [specific gaps] before ISO 27001 audit in [month]
- Timeline: [weeks] to achieve full audit readiness

```

---

# Evidence Collection

## General Evidence Guidelines

**Evidence for Dashboard:**

- Consolidated dashboard workbook itself (primary evidence)
- Executive summary (PDF export)
- Board presentation (if created)
- All 4 source assessment workbooks (linked evidence)

**Evidence Naming Convention:**
```
EV-DASH-[Date]-[Description].[ext]
```

**Examples:**

- `EV-DASH-20260121-Consolidated-Dashboard.xlsx`
- `EV-DASH-20260121-Executive-Summary.pdf`
- `EV-DASH-20260121-Board-Presentation.pptx`
- `EV-DASH-20260121-Trend-Analysis-Q4-2025-vs-Q1-2026.xlsx`

**Storage:** `ISMS/Controls/A.8.12_DLP/Dashboards/Q1_2026/`  
**Retention:** 3 years (audit cycle + 1 year)  
**Sensitivity:** Confidential (contains compliance gaps, may reference incidents)

## Evidence Types

**Dashboard Evidence:**

- Consolidated dashboard workbook (all sheets)
- Executive summary (PDF for board)
- Trend analysis (quarter-over-quarter)

**Source Assessment Evidence:**

- All 4 source workbooks (linked as evidence)
- ~55 total evidence items across all assessments

**Approval Evidence:**

- CISO approval signature on dashboard
- Board meeting minutes showing DLP status review
- Risk acceptance decisions documented

**Minimum Evidence:** Dashboard + Executive Summary + 4 Source Workbooks = **6 items**

---

# Common Pitfalls and How to Avoid Them

## "Source assessments incomplete, tried to create dashboard anyway"

**Problem:** Dashboard shows #REF! errors, missing data, invalid calculations

**Solution:**

- Verify ALL 4 source assessments 100% complete before dashboard creation
- Check each source has Summary_Dashboard, Gap_Analysis, Evidence_Register completed
- Review source workbook approvals (signed and dated)

## "External links broken after moving files"

**Problem:** Dashboard shows #REF! errors after file path changes

**Solution:**

- Keep all 5 workbooks in same directory (never move separately)
- Use relative paths if possible (Excel limitation: external links usually absolute)
- If must move: Data → Edit Links → Change Source → Browse to new location for each link

## "Dashboard shows stale data from old source assessments"

**Problem:** Source assessments updated but dashboard not refreshed

**Solution:**

- Excel: Data → Edit Links → Update Values (refreshes all external links)
- LibreOffice: Edit → Links → Update (refresh all links)
- Enable automatic link updates: File → Options → Advanced → Update automatic links

## "Compliance % calculation doesn't match manual review"

**Problem:** Formula errors, weighting incorrect, source data wrong

**Solution:**

- Verify weighting: Each domain should be 25% (Infrastructure, Classification, Coverage, Monitoring)
- Check formula references correct cells in source Summary_Dashboard sheets
- Manually calculate 1-2 domains to verify formula logic
- Trace precedents: Excel Formula Auditing → Trace Precedents

## "Executive summary too technical for board"

**Problem:** Board doesn't understand technical jargon, loses interest

**Solution:**

- Use business language, not technical terms
- Focus on risk and business impact, not technical details
- Use traffic light colors (Green/Yellow/Red) for visual clarity
- Limit to 1-2 pages maximum
- Highlight "So what?" for each item (why board should care)

## "Critical gaps not prioritized, everything marked Critical"

**Problem:** 20+ "critical" gaps → executive overwhelmed, nothing gets addressed

**Solution:**

- True Critical = Regulatory violation risk OR severe business impact
- Limit Critical to 5-10 maximum (force prioritization)
- Downgrade some to High (important but not immediate regulatory risk)
- For each Critical gap: Justify why it's truly critical
- Focus executive attention on top 5 Critical gaps only

---

# Quality Checklist (Self-Review Before Submission)

**Source Assessment Completeness:**

- [ ] All 4 source assessments 100% complete
- [ ] Each source has Summary_Dashboard calculated (no formula errors)
- [ ] Each source has Gap_Analysis completed (critical gaps documented)
- [ ] Each source has Evidence_Register populated (evidence IDs assigned)
- [ ] Each source has Approval_Sign-Off signed and dated

**Dashboard Technical Quality:**

- [ ] All external links functional (no #REF! errors)
- [ ] All formulas calculate correctly (no #VALUE!, #DIV/0!)
- [ ] Overall compliance % matches manual calculation
- [ ] Conditional formatting working (colors correct)
- [ ] Link update test passed (modified source, verified dashboard updated)

**Data Accuracy:**

- [ ] Compliance % by domain matches source workbooks exactly
- [ ] Critical gaps count matches sum across all sources
- [ ] Evidence count matches sum across all sources
- [ ] Trend analysis (if applicable) uses correct previous quarter data

**Executive Summary Quality:**

- [ ] Written in business language (not technical jargon)
- [ ] Length appropriate (1-2 pages maximum)
- [ ] Top 5-10 critical gaps highlighted with justification
- [ ] Trend analysis included (vs. previous quarter)
- [ ] Resource requirements specified (budget, staffing, tools)
- [ ] Risk acceptance recommendations provided
- [ ] Audit readiness assessment included

**Evidence Completeness:**

- [ ] Dashboard workbook saved in approved directory
- [ ] Executive summary exported to PDF
- [ ] All 4 source workbooks saved with dashboard
- [ ] File naming convention followed
- [ ] Evidence stored per retention policy (3 years)

**Approval Workflow:**

- [ ] Completed By: DLP Program Manager signed
- [ ] Reviewed By: Compliance Officer signed
- [ ] Approved By: CISO signed
- [ ] Distribution list completed

**Final Checks:**

- [ ] Filename: `ISMS-IMP-A.8.12.5_Compliance_Dashboard_20260121.xlsx`
- [ ] All sheets present and populated
- [ ] No placeholder text ([TBD], [FILL IN], etc.)
- [ ] Ready for board presentation

---

# Review & Approval Process

## Assessment Metadata

**Consolidation Period:** Q1 2026 (Adjust as appropriate)  
**Dashboard Date:** 21.01.2026  
**Source Assessments Included:**

- [ ] A.8.12.1 Infrastructure (Date: _______)
- [ ] A.8.12.2 Classification (Date: _______)
- [ ] A.8.12.3 Channel Coverage (Date: _______)
- [ ] A.8.12.4 Monitoring & Response (Date: _______)

## Completed By (DLP Program Manager)

**Name:** _______________________  
**Role:** _______________________  
**Email:** _______________________  
**Date:** _______________________  
**Signature:** _______________________

**Declaration:**
I confirm:

- All 4 source assessments reviewed and verified complete
- External workbook links functional and tested
- Compliance calculations verified accurate
- Critical gaps consolidated and prioritized
- Executive summary suitable for board presentation

## Reviewed By (Compliance Officer / Internal Audit)

**Name:** _______________________  
**Date:** _______________________  
**Signature:** _______________________

**Review Focus:**

- Audit readiness status accurate
- Regulatory compliance risks identified
- Evidence completeness verified
- Gap remediation plans realistic

**Review Outcome:**

- [ ] Approved - Ready for CISO presentation
- [ ] Approved with minor corrections: _______
- [ ] Requires revision: _______

## Approved By (CISO)

**Name:** _______________________  
**Date:** _______________________  
**Signature:** _______________________

**Decision:**

- [ ] Approved - Ready for Executive Management / Board presentation
- [ ] Approved with conditions - Address [gaps] before audit
- [ ] Rejected - Insufficient compliance, remediation required before approval

**Risk Acceptance Decisions:**
For critical gaps documented:

- [ ] Accept residual risk (specify which gaps): _______
- [ ] Remediate (budget approved, timeline agreed): _______
- [ ] Escalate to Board (gaps exceed CISO authority to accept): _______

**Board Presentation:**

- [ ] Schedule board presentation for: _______
- [ ] Provide executive summary to board on: _______

## Next Review Date

**Next Dashboard Update:** _______________________ (Quarterly)

**Review Cycle:**

- **Quarterly:** Regular dashboard update
- **Ad-hoc:** When major changes occur (new DLP deployment, incident, audit, regulatory change)

**Source Assessment Update Triggers:**

- Network changes → Update A.8.12.3 Channel Coverage
- DLP tuning → Update A.8.12.2 Classification, A.8.12.4 Monitoring
- SOC changes → Update A.8.12.4 Monitoring
- New DLP technology → Update A.8.12.1 Infrastructure

## Distribution List

This dashboard shall be distributed to:

- [ ] CISO
- [ ] Executive Management Team (CEO, CFO, COO)
- [ ] Board of Directors (Executive Summary only)
- [ ] Data Protection Officer (DPO)
- [ ] Legal / General Counsel
- [ ] Compliance Officer
- [ ] Internal Audit
- [ ] External Auditors (upon request)

**Storage Location:**
`ISMS/Controls/A.8.12_DLP/Dashboards/Q1_2026/ISMS-IMP-A.8.12.5_Compliance_Dashboard_20260121_APPROVED.xlsx`

---

**END OF PART I: USER COMPLETION GUIDE**

---

# PART II: TECHNICAL SPECIFICATION
**Audience:** Python Developers, Excel Workbook Developers, Quality Assurance, ISMS Implementation Team

---

# Workbook Structure Overview

## Sheet List

**Total Sheets:** 12

| # | Sheet Name | Rows (approx) | Purpose | User Input |
|---|------------|---------------|---------|------------|
| 1 | Instructions_Legend | 45 | User guidance, metadata | Metadata only |
| 2 | Executive_Summary | 50 | Board-ready summary, overall compliance | Manual summary text |
| 3 | Domain_Rollup_Summary | 40 | Compliance % by domain, KPIs | No (formulas) |
| 4 | Consolidated_Gap_Analysis | 60 | All critical gaps from 4 sources | No (formulas) |
| 5 | Risk_Register | 40 | DLP-related risk tracking | Yes (risk details) |
| 6 | Remediation_Roadmap | 45 | Remediation planning and tracking | Yes (roadmap items) |
| 7 | Evidence_Master_Index | 35 | Evidence count verification and index | No (formulas) |
| 8 | Trend_Analysis | 40 | Quarter-over-quarter comparison | Manual analysis |
| 9 | KPI_Dashboard | 35 | Key performance indicators dashboard | No (formulas) |
| 10 | Budget_Planning | 30 | DLP budget and resource planning | Yes (budget items) |
| 11 | CISO_DPO_Approval | 25 | Multi-level approval workflow | Yes (signatures) |
| 12 | Summary_Dashboard | 40 | Overall summary and status | No (formulas) |

**Total:** ~485 rows + external link formulas

---

# Detailed Sheet Specifications

## Sheet: Instructions_Legend

**Purpose:** User guidance and dashboard metadata

**Layout:**

- Rows 1-5: Document header
- Rows 7-14: Organization metadata (yellow cells)
- Rows 16-30: How to use dashboard
- Rows 32-40: External link troubleshooting guide
- Rows 42-45: Color coding legend

**Organization Metadata:**

| Row | Field | Type | Example |
|-----|-------|------|---------|
| 7 | Dashboard Period | Text | Q1 2026 |
| 8 | Dashboard Date | Date | 21.01.2026 |
| 9 | Prepared By | Text | Jane Doe |
| 10 | Role | Text | DLP Program Manager |
| 11 | Organization | Text | [Organization] |
| 12 | CISO | Text | John Smith |
| 13 | Next Review | Date | 21.04.2026 |
| 14 | Audit Date (if scheduled) | Date | 15.05.2026 |

---

## Sheet: Executive_Summary

**Purpose:** Board-ready executive summary with overall compliance status

**Column Structure:**

| Col | Header | Type | Width | Validation | Notes |
|-----|--------|------|-------|------------|-------|
| A | Metric | Text | 35 | None | Pre-populated |
| B | Value | Various | 20 | None | External link formula or manual |
| C | Target | Text | 15 | None | Policy target |
| D | Status | Dropdown | 12 | ✅/⚠️/❌ | Auto or manual |
| E | Trend | Text | 15 | None | +/- vs. previous quarter |
| F | Notes | Text (wrap) | 50 | None | Executive commentary |

**Pre-Populated Metrics (Rows 6-50):**

| Section | Metrics |
|---------|---------|
| **Overall Status** | Overall DLP Compliance %, Status, Trend vs. Q4 2025 |
| **Domain Compliance** | Infrastructure %, Classification %, Channel Coverage %, Monitoring & Response % |
| **Critical Metrics** | Total Critical Gaps, Total Evidence Items, Audit Readiness Status |
| **Key Findings** | DLP Infrastructure Status, Data Classification Maturity, Channel Coverage %, MTTR - Critical Alerts, False Positive Rate, SIEM Integration Status |
| **Executive Concerns** | Top 5 Critical Gaps (auto-populated from consolidated gaps) |
| **Resource Requirements** | Budget Needs, Staffing Needs, Tool Requirements |
| **Risk Acceptance** | Gaps Accepted, Gaps Remediation Required, Board Escalation Required |
| **Executive Summary Text** | Free-form summary (manual entry, 1-2 paragraphs) |

**Key External Link Formulas:**

```excel
# Overall DLP Compliance % (Cell B6)
=ROUND(
  ([ISMS-IMP-A.8.12.1_Infrastructure_YYYYMMDD.xlsx]Summary_Dashboard!$B$7 * 0.25) +
  ([ISMS-IMP-A.8.12.2_Classification_YYYYMMDD.xlsx]Summary_Dashboard!$B$7 * 0.25) +
  ([ISMS-IMP-A.8.12.3_Channel_Coverage_YYYYMMDD.xlsx]Summary_Dashboard!$B$7 * 0.25) +
  ([ISMS-IMP-A.8.12.4_Monitoring_Response_YYYYMMDD.xlsx]Summary_Dashboard!$B$7 * 0.25),
  0
)

# Infrastructure Compliance % (Cell B10)
=[ISMS-IMP-A.8.12.1_Infrastructure_YYYYMMDD.xlsx]Summary_Dashboard!$B$7

# Classification Compliance % (Cell B11)
=[ISMS-IMP-A.8.12.2_Classification_YYYYMMDD.xlsx]Summary_Dashboard!$B$7

# Channel Coverage Compliance % (Cell B12)
=[ISMS-IMP-A.8.12.3_Channel_Coverage_YYYYMMDD.xlsx]Summary_Dashboard!$B$7

# Monitoring & Response Compliance % (Cell B13)
=[ISMS-IMP-A.8.12.4_Monitoring_Response_YYYYMMDD.xlsx]Summary_Dashboard!$B$7

# Total Critical Gaps (Cell B16)
=[ISMS-IMP-A.8.12.1_Infrastructure_YYYYMMDD.xlsx]Gap_Analysis!$F$6:$F$45 (COUNTIF "Critical") +
=[ISMS-IMP-A.8.12.2_Classification_YYYYMMDD.xlsx]Gap_Analysis!$F$6:$F$45 (COUNTIF "Critical") +
=[ISMS-IMP-A.8.12.3_Channel_Coverage_YYYYMMDD.xlsx]Gap_Analysis!$F$6:$F$45 (COUNTIF "Critical") +
=[ISMS-IMP-A.8.12.4_Monitoring_Response_YYYYMMDD.xlsx]Gap_Analysis!$F$6:$F$45 (COUNTIF "Critical")
```

**Conditional Formatting:**

```python
# Overall Compliance % (Cell B6)
compliance_format = {
    'green': ('>=', 90),   # Audit-ready
    'yellow': ('and', [('>=', 80), ('<', 90)]),  # Partially ready
    'red': ('<', 80)       # Not audit-ready
}

# Status (Column D)
status_format = {
    '✅ Compliant': 'green',
    '⚠️ Partial': 'yellow',
    '❌ Non-Compliant': 'red'
}
```

---

## Sheet: Consolidated_Metrics

**Purpose:** Detailed metrics consolidated from all 4 source assessments

**Column Structure:**

| Col | Header | Type | Width | Validation | Notes |
|-----|--------|------|-------|------------|-------|
| A | Metric Category | Text | 25 | None | Domain grouping |
| B | Metric Name | Text | 35 | None | Specific metric |
| C | Source | Text | 30 | None | Which assessment |
| D | Value | Various | 20 | None | External link formula |
| E | Target | Text | 15 | None | Policy target |
| F | Status | Auto | 12 | ✅/⚠️/❌ | Formula-driven |
| G | Notes | Text (wrap) | 40 | None | Context |

**Pre-Populated Metrics (Rows 6-40):**

**From A.8.12.1 Infrastructure:**

- DLP Technology Inventory Completeness (%)
- Network DLP Coverage (%)
- Endpoint DLP Coverage (%)
- Email DLP Coverage (%)
- Cloud DLP Coverage (%)

**From A.8.12.2 Classification:**

- Data Classification Scheme Maturity Level
- Sensitive Data Categories Inventoried (#)
- DLP Pattern Accuracy (%)
- False Positive Rate (%)

**From A.8.12.3 Channel Coverage:**

- Channels Fully Covered (#/7)
- Bypass Tests Passed (%)
- Shadow IT Channels Identified (#)
- Unprotected Restricted Data Channels (#)

**From A.8.12.4 Monitoring & Response:**

- Alert Backlog (#)
- MTTR - Critical Alerts (hours)
- SIEM Integration Status
- SOC Playbooks Documented (Yes/No)
- GDPR 72-Hour Compliance (%)

**External Link Formula Pattern:**

```excel
# Generic pattern for pulling metrics from source workbooks
=[SourceWorkbookName.xlsx]SheetName!$CellReference

# Example: DLP Pattern Accuracy from A.8.12.2
=[ISMS-IMP-A.8.12.2_Classification_YYYYMMDD.xlsx]Summary_Dashboard!$B$15

# Example: MTTR Critical from A.8.12.4
=[ISMS-IMP-A.8.12.4_Monitoring_Response_YYYYMMDD.xlsx]Summary_Dashboard!$B$12
```

---

## Sheet: Critical_Gaps_Consolidated

**Purpose:** Consolidate all critical gaps from 4 source Gap_Analysis sheets

**Column Structure:**

| Col | Header | Type | Width | Notes |
|-----|--------|------|-------|-------|
| A | Gap ID | Text | 15 | From source (e.g., GAP-001) |
| B | Source Assessment | Text | 25 | Infrastructure/Classification/Coverage/Monitoring |
| C | Gap Description | Text (wrap) | 45 | From source Gap_Analysis |
| D | Current State | Text (wrap) | 30 | From source |
| E | Required State | Text (wrap) | 30 | From source |
| F | Risk Level | Text | 12 | Should all be "Critical" |
| G | Regulatory Impact | Text | 25 | GDPR, nDSG, etc. |
| H | Remediation Action | Text (wrap) | 40 | From source |
| I | Owner | Text | 20 | From source |
| J | Target Date | Date | 15 | From source |
| K | Status | Text | 15 | From source (Open/In Progress) |
| L | Priority Rank | Number | 10 | 1-10 (manual prioritization) |

**Data Population Method:**

**CRITICAL NOTE:** This sheet CANNOT use simple external link formulas because:

- Each source workbook has variable number of critical gaps
- Gap_Analysis rows are user-populated (not pre-defined structure)
- Need to filter for Risk Level = "Critical" only

**Two Implementation Options:**

**Option A: Manual Consolidation (Recommended for initial dashboard)**
1. Open each source workbook
2. Filter Gap_Analysis sheet for Risk Level = "Critical"
3. Copy critical gap rows
4. Paste into Consolidated_Gaps_Dashboard
5. Add "Source Assessment" column manually
6. Sort by Target Date or Priority Rank

**Option B: Power Query / Automated (Advanced, requires Excel Power Query)**
1. Use Power Query to connect to 4 source workbooks
2. Query each Gap_Analysis sheet
3. Filter for Risk Level = "Critical"
4. Append all queries
5. Add calculated column for "Source Assessment"
6. Refresh query to update dashboard

**For Python Script Generation:**

- Include commented-out Power Query code
- Provide manual consolidation instructions as default
- Note that full automation requires VBA or Power Query

**Data Rows:** 60 total (accommodate up to 15 critical gaps per source × 4 sources)

---

## Sheet: Evidence_Summary

**Purpose:** Verify evidence completeness across all assessments

**Column Structure:**

| Col | Header | Type | Width | Validation | Notes |
|-----|--------|------|-------|------------|-------|
| A | Source Assessment | Text | 30 | None | Pre-populated |
| B | Evidence Count | Number | 15 | None | External link formula |
| C | Expected Count | Number | 15 | None | Target (e.g., 15) |
| D | Status | Auto | 12 | ✅/⚠️/❌ | Formula-driven |
| E | Evidence Types | Text (wrap) | 50 | None | Summary of types |
| F | Gaps | Text (wrap) | 40 | None | Missing evidence |

**Pre-Populated Assessments (Rows 6-10):**

| Assessment | Expected Count | Status Criteria |
|------------|----------------|-----------------|
| A.8.12.1 Infrastructure | 15 | ✅ if ≥15, ⚠️ if 10-14, ❌ if <10 |
| A.8.12.2 Classification | 15 | ✅ if ≥15, ⚠️ if 10-14, ❌ if <10 |
| A.8.12.3 Channel Coverage | 15 | ✅ if ≥15, ⚠️ if 10-14, ❌ if <10 |
| A.8.12.4 Monitoring & Response | 10 | ✅ if ≥10, ⚠️ if 7-9, ❌ if <7 |
| **TOTAL** | **55** | ✅ if ≥55, ⚠️ if 40-54, ❌ if <40 |

**External Link Formula for Evidence Count:**

```excel
# Count evidence items in source Evidence_Register
# Evidence IDs are in column A, starting row 6

# A.8.12.1 Infrastructure Evidence Count (Cell B6)
=COUNTA([ISMS-IMP-A.8.12.1_Infrastructure_YYYYMMDD.xlsx]Evidence_Register!$A$6:$A$105)

# A.8.12.2 Classification Evidence Count (Cell B7)
=COUNTA([ISMS-IMP-A.8.12.2_Classification_YYYYMMDD.xlsx]Evidence_Register!$A$6:$A$105)

# Total Evidence Count (Cell B10)
=SUM(B6:B9)
```

**Conditional Formatting:**

```python
# Evidence Count Status (Column D)
status_formula = {
    '✅': '=B6>=C6',           # Meets or exceeds target
    '⚠️': '=AND(B6>=C6*0.7, B6<C6)',  # 70-99% of target
    '❌': '=B6<C6*0.7'         # <70% of target
}
```

---

## Sheet: Trend_Analysis

**Purpose:** Quarter-over-quarter trend comparison

**Column Structure:**

| Col | Header | Type | Width | Notes |
|-----|--------|------|-------|-------|
| A | Metric | Text | 35 | Pre-populated |
| B | Previous Quarter (Q4 2025) | Number/Text | 20 | Manual entry from previous dashboard |
| C | Current Quarter (Q1 2026) | Number/Text | 20 | External link formula |
| D | Change | Number | 12 | =C-B (for percentages/counts) |
| E | Trend | Auto | 12 | ⬆️ / ➡️ / ⬇️ (improving/stable/degrading) |
| F | Analysis | Text (wrap) | 50 | Manual commentary |

**Pre-Populated Metrics for Trending (Rows 6-40):**

| Category | Metrics |
|----------|---------|
| **Overall** | Overall Compliance %, Total Critical Gaps |
| **By Domain** | Infrastructure %, Classification %, Coverage %, Monitoring % |
| **Infrastructure** | DLP Technologies Deployed, Channel Coverage Count |
| **Classification** | Pattern Accuracy %, False Positive Rate % |
| **Coverage** | Bypass Tests Passed %, Shadow IT Channels |
| **Monitoring** | Alert Backlog, MTTR Critical (hours), SOC 24/7 Coverage |

**Trend Determination Formula:**

```excel
# Trend indicator (Column E)
# For compliance % (higher is better)
=IF(D6>5, "⬆️ Improving", IF(D6<-5, "⬇️ Degrading", "➡️ Stable"))

# For gap counts (lower is better)
=IF(D6<-2, "⬆️ Improving", IF(D6>2, "⬇️ Degrading", "➡️ Stable"))

# For MTTR (lower is better)
=IF(D6<-1, "⬆️ Improving", IF(D6>1, "⬇️ Degrading", "➡️ Stable"))
```

**Conditional Formatting:**

- ⬆️ Improving = Green
- ➡️ Stable = Yellow
- ⬇️ Degrading = Red

---

## Sheet: Approval_Sign-Off

**Purpose:** Multi-level approval workflow for dashboard

*(Same structure as previous IMP documents)*

**Approval Levels:**
1. Completed By: DLP Program Manager
2. Reviewed By: Compliance Officer / Internal Audit
3. Approved By: CISO
4. Presented To: Executive Management / Board (optional signature)

---

## Sheet: Link_Management

**Purpose:** External link status monitoring and troubleshooting reference

**Column Structure:**

| Col | Header | Type | Width | Notes |
|-----|--------|------|-------|-------|
| A | Source Workbook | Text | 40 | Filename |
| B | File Path | Text | 60 | Full path |
| C | Link Status | Auto | 15 | OK / Error / Unknown |
| D | Last Updated | Auto | 20 | Timestamp |
| E | Sheet Referenced | Text | 25 | Which sheets linked |
| F | Formula Count | Number | 15 | How many formulas reference this workbook |
| G | Notes | Text (wrap) | 40 | Troubleshooting notes |

**Pre-Populated Source Workbooks (Rows 6-9):**

| Source Workbook | Sheets Referenced | Typical Formula Count |
|-----------------|-------------------|------------------------|
| ISMS-IMP-A.8.12.1_Infrastructure_YYYYMMDD.xlsx | Summary_Dashboard, Gap_Analysis, Evidence_Register | ~10 formulas |
| ISMS-IMP-A.8.12.2_Classification_YYYYMMDD.xlsx | Summary_Dashboard, Gap_Analysis, Evidence_Register | ~10 formulas |
| ISMS-IMP-A.8.12.3_Channel_Coverage_YYYYMMDD.xlsx | Summary_Dashboard, Gap_Analysis, Evidence_Register | ~10 formulas |
| ISMS-IMP-A.8.12.4_Monitoring_Response_YYYYMMDD.xlsx | Summary_Dashboard, Gap_Analysis, Evidence_Register | ~10 formulas |

**Link Status Check:**

Excel: Data → Edit Links → Shows status for each external workbook
LibreOffice: Edit → Links → Shows status

**Status Values:**

- **OK:** Link functional, data updating
- **Error:** File not found, moved, or renamed
- **Unknown:** Excel can't determine status (may need manual update)

**Troubleshooting Guide (Rows 15-30):**

| Issue | Cause | Solution |
|-------|-------|----------|
| #REF! Error | Source workbook moved/renamed | Data → Edit Links → Change Source |
| Stale Data | Source updated but dashboard not refreshed | Data → Edit Links → Update Values |
| "Links Disabled" Warning | Excel security setting | File → Options → Trust Center → Enable automatic link updates |
| Circular Reference | Dashboard formula references itself | Check formula, ensure references external workbook only |
| Slow Performance | Too many external links | Consider consolidating formulas, use fewer references |

---

# External Link Formula Patterns

## Standard External Link Syntax

**Excel External Link Format:**
```excel
=[WorkbookName.xlsx]SheetName!CellReference

# Example:
=[ISMS-IMP-A.8.12.1_Infrastructure_20260121.xlsx]Summary_Dashboard!$B$7
```

**Components:**

- `[WorkbookName.xlsx]` - Source workbook filename in brackets
- `SheetName` - Sheet name in source workbook
- `!` - Separator
- `CellReference` - Cell address (use $ for absolute reference)

**Full Path External Link (when workbooks in different directories):**
```excel
='C:\Path\To\File\[WorkbookName.xlsx]SheetName'!CellReference

# Example:
='C:\ISMS\A.8.12_DLP\Q1_2026\[ISMS-IMP-A.8.12.1_Infrastructure_20260121.xlsx]Summary_Dashboard'!$B$7
```

## Common Formula Patterns

**Pattern 1: Direct Value Reference**
```excel
# Pull single value from source Summary_Dashboard
=[SourceWorkbook.xlsx]Summary_Dashboard!$B$7
```

**Pattern 2: COUNT / COUNTIF Across External Range**
```excel
# Count critical gaps in source Gap_Analysis
=COUNTIF([SourceWorkbook.xlsx]Gap_Analysis!$F$6:$F$45,"Critical")
```

**Pattern 3: Weighted Average Across Multiple Sources**
```excel
# Overall compliance from 4 sources (25% weight each)
=ROUND(
  ([Source1.xlsx]Summary_Dashboard!$B$7 * 0.25) +
  ([Source2.xlsx]Summary_Dashboard!$B$7 * 0.25) +
  ([Source3.xlsx]Summary_Dashboard!$B$7 * 0.25) +
  ([Source4.xlsx]Summary_Dashboard!$B$7 * 0.25),
  0
)
```

**Pattern 4: SUM Across Multiple External Sources**
```excel
# Total critical gaps from all sources
=COUNTIF([Source1.xlsx]Gap_Analysis!$F$6:$F$45,"Critical") +
 COUNTIF([Source2.xlsx]Gap_Analysis!$F$6:$F$45,"Critical") +
 COUNTIF([Source3.xlsx]Gap_Analysis!$F$6:$F$45,"Critical") +
 COUNTIF([Source4.xlsx]Gap_Analysis!$F$6:$F$45,"Critical")
```

**Pattern 5: Conditional Status Based on External Value**
```excel
# Status based on compliance %
=IF([Source.xlsx]Summary_Dashboard!$B$7>=90, "✅ Compliant",
    IF([Source.xlsx]Summary_Dashboard!$B$7>=80, "⚠️ Partial",
       "❌ Non-Compliant"))
```

## Link Update and Maintenance

**Manual Link Update:**
1. Excel: Data → Edit Links
2. Select link to update
3. Click "Update Values" (refresh data from source)
4. Click "Change Source" (if file moved/renamed)

**Automatic Link Update:**

- File → Options → Advanced → General → "Update automatic links at open"
- Warning: May slow workbook opening if many links

**Breaking Links (Converting to Values):**

- Data → Edit Links → Select link → Break Link
- Converts formulas to static values (loses connection to source)
- Use when archiving historical dashboards

---

# Data Validation Rules

## Executive Summary Sheet

**Manual Entry Fields:**

- Executive Summary Text (rows 40-50): Free-form text, no validation
- Resource Requirements: Free-form text
- Risk Acceptance Decisions: Free-form text

**Dropdown Validations:**
```python
# Status fields (where not auto-calculated)
validation_status = {
    'type': 'list',
    'formula1': '"✅ Compliant,⚠️ Partial,❌ Non-Compliant,N/A"',
    'allow_blank': False
}

# Audit Readiness
validation_audit = {
    'type': 'list',
    'formula1': '"Ready,Partially Ready,Not Ready"',
    'allow_blank': False
}
```

## Trend Analysis Sheet

**Previous Quarter Values:**

- Manual entry (copied from previous quarter dashboard)
- Numeric validation for percentages (0-100)
- Date validation for timestamps

---

# Conditional Formatting Rules

## Compliance Percentage Formatting

**Applied to:** All compliance % cells across all sheets

```python
compliance_format = {
    'dark_green': ('>=', 90),   # 90-100%: Audit-ready
    'light_green': ('and', [('>=', 85), ('<', 90)]),  # 85-89%: Nearly compliant
    'yellow': ('and', [('>=', 80), ('<', 85)]),       # 80-84%: Partially compliant
    'orange': ('and', [('>=', 70), ('<', 80)]),       # 70-79%: Needs improvement
    'red': ('<', 70)            # <70%: Non-compliant
}
```

## Gap Count Formatting

**Applied to:** Critical gaps count cells

```python
gap_count_format = {
    'green': ('=', 0),          # Zero critical gaps = excellent
    'yellow': ('and', [('>', 0), ('<=', 5)]),   # 1-5 gaps = acceptable
    'red': ('>', 5)             # >5 gaps = too many
}
```

## Evidence Count Formatting

**Applied to:** Evidence completeness cells

```python
evidence_format = {
    'green': ('>=', 'target'),      # Meets or exceeds target
    'yellow': ('>=', 'target*0.7'), # 70-99% of target
    'red': ('<', 'target*0.7')      # <70% of target
}
```

---

# Cell Protection

**Protected Cells (Formula Cells):**

- All external link formulas (prevent accidental editing)
- All calculated status cells
- All auto-generated IDs
- Pre-populated metric names

**Unprotected Cells (User Input):**

- Organization metadata (yellow cells)
- Executive summary text (manual commentary)
- Trend analysis commentary
- Risk acceptance decisions
- Approval signatures and dates

**Sheet Protection:**

- Enable protection on all sheets
- Allow: Format cells, Sort, Filter
- Disallow: Delete rows, Modify formulas, Unprotect sheet

---

# Dashboard Summary Formulas (Consolidated)

## Overall DLP Compliance %

```excel
# Executive_Summary!B6
=ROUND(
  ([ISMS-IMP-A.8.12.1_Infrastructure_YYYYMMDD.xlsx]Summary_Dashboard!$B$7 * 0.25) +
  ([ISMS-IMP-A.8.12.2_Classification_YYYYMMDD.xlsx]Summary_Dashboard!$B$7 * 0.25) +
  ([ISMS-IMP-A.8.12.3_Channel_Coverage_YYYYMMDD.xlsx]Summary_Dashboard!$B$7 * 0.25) +
  ([ISMS-IMP-A.8.12.4_Monitoring_Response_YYYYMMDD.xlsx]Summary_Dashboard!$B$7 * 0.25),
  0
)
```

## Total Critical Gaps

```excel
# Executive_Summary!B16
=COUNTIF([ISMS-IMP-A.8.12.1_Infrastructure_YYYYMMDD.xlsx]Gap_Analysis!$F$6:$F$45,"Critical") +
 COUNTIF([ISMS-IMP-A.8.12.2_Classification_YYYYMMDD.xlsx]Gap_Analysis!$F$6:$F$45,"Critical") +
 COUNTIF([ISMS-IMP-A.8.12.3_Channel_Coverage_YYYYMMDD.xlsx]Gap_Analysis!$F$6:$F$45,"Critical") +
 COUNTIF([ISMS-IMP-A.8.12.4_Monitoring_Response_YYYYMMDD.xlsx]Gap_Analysis!$F$6:$F$45,"Critical")
```

## Total Evidence Items

```excel
# Evidence_Summary!B10
=COUNTA([ISMS-IMP-A.8.12.1_Infrastructure_YYYYMMDD.xlsx]Evidence_Register!$A$6:$A$105) +
 COUNTA([ISMS-IMP-A.8.12.2_Classification_YYYYMMDD.xlsx]Evidence_Register!$A$6:$A$105) +
 COUNTA([ISMS-IMP-A.8.12.3_Channel_Coverage_YYYYMMDD.xlsx]Evidence_Register!$A$6:$A$105) +
 COUNTA([ISMS-IMP-A.8.12.4_Monitoring_Response_YYYYMMDD.xlsx]Evidence_Register!$A$6:$A$105)
```

## Audit Readiness Status

```excel
# Executive_Summary!B18
=IF(AND(B6>=90, B16=0, B17>=55), "✅ Ready",
    IF(AND(B6>=80, B16<=5, B17>=40), "⚠️ Partially Ready",
       "❌ Not Ready"))

# Where:
# B6 = Overall Compliance %
# B16 = Total Critical Gaps
# B17 = Total Evidence Items
```

---

# APPENDIX: Technical Notes for Python Developers

## A.1 Python Script Integration

**Script Name:** `generate_a812_5_compliance_dashboard.py`

**CRITICAL CUSTOMIZATION REQUIRED:**

This script MUST be customized for each implementation because:
1. Source workbook filenames contain organization-specific dates (YYYYMMDD)
2. File paths are environment-specific
3. External link formulas require exact filenames

**Script Structure:**

```python
import openpyxl
from openpyxl import Workbook
from openpyxl.utils import get_column_letter
from datetime import datetime

# ============================================
# CONFIGURATION - CUSTOMIZE FOR YOUR DEPLOYMENT
# ============================================

# Assessment date (used in filenames)
ASSESSMENT_DATE = "20260121"  # Format: YYYYMMDD

# Source workbook filenames (MUST match actual files)
SOURCE_FILES = {
    'infrastructure': f'ISMS-IMP-A.8.12.1_Infrastructure_{ASSESSMENT_DATE}.xlsx',
    'classification': f'ISMS-IMP-A.8.12.2_Classification_{ASSESSMENT_DATE}.xlsx',
    'coverage': f'ISMS-IMP-A.8.12.3_Channel_Coverage_{ASSESSMENT_DATE}.xlsx',
    'monitoring': f'ISMS-IMP-A.8.12.4_Monitoring_Response_{ASSESSMENT_DATE}.xlsx'
}

# Dashboard workbook filename
DASHBOARD_FILE = f'ISMS-IMP-A.8.12.5_Compliance_Dashboard_{ASSESSMENT_DATE}.xlsx'

# Directory containing all workbooks (use relative path or absolute)
WORKBOOK_DIR = './'  # Current directory, or '/path/to/workbooks/'

# ============================================
# EXTERNAL LINK FORMULA TEMPLATES
# ============================================

def create_external_link_formula(source_file, sheet, cell):
    """
    Create Excel external link formula
    
    Args:
        source_file: Source workbook filename
        sheet: Sheet name in source workbook
        cell: Cell reference (e.g., "$B$7")
    
    Returns:
        Formula string (e.g., "=[SourceFile.xlsx]SheetName!$B$7")
    """
    return f"=[{source_file}]{sheet}!{cell}"

def create_overall_compliance_formula(source_files):
    """
    Create weighted average formula for overall compliance
    
    Returns formula: (Infra*0.25 + Class*0.25 + Coverage*0.25 + Monitor*0.25)
    """
    formulas = []
    for key in ['infrastructure', 'classification', 'coverage', 'monitoring']:
        link = create_external_link_formula(
            source_files[key],
            'Summary_Dashboard',
            '$B$7'
        )
        formulas.append(f"({link} * 0.25)")
    
    return f"=ROUND({' + '.join(formulas)}, 0)"

def create_critical_gaps_formula(source_files):
    """
    Create SUM formula for total critical gaps across all sources
    
    Returns formula: COUNTIF(Source1...) + COUNTIF(Source2...) + ...
    """
    countifs = []
    for key in ['infrastructure', 'classification', 'coverage', 'monitoring']:
        link_range = create_external_link_formula(
            source_files[key],
            'Gap_Analysis',
            '$F$6:$F$45'
        )
        countifs.append(f'COUNTIF({link_range},"Critical")')
    
    return f"={' + '.join(countifs)}"

# ============================================
# WORKBOOK GENERATION
# ============================================

def create_dashboard_workbook():
    """Main function to create dashboard workbook"""
    wb = Workbook()
    
    # Create sheets
    sheets = [
        'Instructions_Legend',
        'Executive_Summary',
        'Consolidated_Metrics',
        'Critical_Gaps_Consolidated',
        'Evidence_Summary',
        'Trend_Analysis',
        'Approval_Sign-Off',
        'Link_Management'
    ]
    
    # Implementation continues...
    # (See full script in separate file)
    
    return wb

if __name__ == "__main__":
    # Generate dashboard workbook
    wb = create_dashboard_workbook()
    wb.save(DASHBOARD_FILE)
    print(f"Dashboard created: {DASHBOARD_FILE}")
    print("IMPORTANT: Update source file paths if workbooks in different directory")
```

## A.2 Deployment Instructions

**Step 1: Prepare Environment**
```bash
# Ensure all 4 source assessments completed and saved
ls -la ISMS-IMP-A.8.12.*_YYYYMMDD.xlsx

# Expected output:
# ISMS-IMP-A.8.12.1_Infrastructure_20260121.xlsx
# ISMS-IMP-A.8.12.2_Classification_20260121.xlsx
# ISMS-IMP-A.8.12.3_Channel_Coverage_20260121.xlsx
# ISMS-IMP-A.8.12.4_Monitoring_Response_20260121.xlsx
```

**Step 2: Customize Python Script**
```python
# Edit generate_a812_5_compliance_dashboard.py
# Update ASSESSMENT_DATE to match your files
ASSESSMENT_DATE = "20260121"  # Change to your date
```

**Step 3: Generate Dashboard**
```bash
python3 generate_a812_5_compliance_dashboard.py

# Output: ISMS-IMP-A.8.12.5_Compliance_Dashboard_20260121.xlsx
```

**Step 4: Verify External Links**
```bash
# Open in Excel
# Data → Edit Links → Verify all 4 source workbooks show "OK" status
# If "Error" → Check file paths, ensure all workbooks in same directory
```

**Step 5: Test Link Updates**
```bash
# Modify value in source workbook (e.g., change compliance % in A.8.12.1)
# Save source workbook
# Refresh dashboard: Data → Edit Links → Update Values
# Verify dashboard reflects change
```

## A.3 Quality Assurance

**Validation Script:** `excel_sanity_check_a812_5.py`

```python
def validate_dashboard(workbook_path):
    """Comprehensive dashboard validation"""
    checks = [
        check_all_sheets_exist(),
        check_external_links_functional(),
        check_formulas_no_errors(),
        check_compliance_calculation(),
        check_critical_gaps_sum(),
        check_evidence_count(),
        check_approval_workflow()
    ]
    return all(checks)

def check_external_links_functional():
    """Verify all external links return values (not #REF!)"""
    # Open workbook
    # For each external link formula:
    #   - Check formula doesn't contain #REF!
    #   - Verify cell value is numeric or text (not error)
    pass

def check_compliance_calculation():
    """Verify overall compliance % matches manual calculation"""
    # Extract 4 domain compliance %
    # Calculate: (sum of 4) / 4
    # Compare to dashboard Overall Compliance %
    # Assert difference <0.1% (rounding tolerance)
    pass
```

## A.4 Troubleshooting Guide

**Issue: #REF! Errors in Dashboard**

*Cause:* Source workbook file not found or moved

*Solution:*
1. Data → Edit Links
2. Select broken link
3. Change Source → Browse to correct file
4. Update Values

**Issue: Formulas Not Auto-Updating**

*Cause:* Automatic link updates disabled

*Solution:*
1. File → Options → Advanced → General
2. Enable "Update automatic links at open"
3. Close and reopen workbook

**Issue: Circular Reference Warning**

*Cause:* Dashboard formula accidentally references itself

*Solution:*
1. Formulas → Error Checking → Circular References
2. Review formula, ensure references external workbook only
3. Fix formula to point to correct source

---

**END OF PART II: TECHNICAL SPECIFICATION**

**Status:** Complete  
**Next Action:** Implement Python generator, deploy dashboard, verify external links

---

**Final Note for Implementers:**

This dashboard is the CONSOLIDATION LAYER. Its value depends entirely on the quality of the 4 source assessments. Invest time in high-quality source assessments before creating dashboard.

**Maintenance:**

- Quarterly: Update dashboard when source assessments refreshed
- After major DLP changes: Update relevant source assessment, dashboard auto-reflects change
- Before audit: Verify all links functional, evidence complete, gaps documented

**Archive Strategy:**

- Keep historical dashboards (one per quarter) for trend analysis
- Break links in archived dashboards (convert formulas to values) to prevent link errors when source files archived

---

**END OF SPECIFICATION**

---

*"Imagination is more important than knowledge. Knowledge is limited. Imagination encircles the world."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-01-31 -->
