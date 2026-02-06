**ISMS-IMP-A.8.12.5-UG - Compliance Dashboard**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.12: Data Leakage Prevention

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.12.5-UG |
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

**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
