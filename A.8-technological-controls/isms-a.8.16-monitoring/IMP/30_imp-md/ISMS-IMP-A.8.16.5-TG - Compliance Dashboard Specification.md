**ISMS-IMP-A.8.16.5-TG - Compliance Dashboard Specification**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.16: Monitoring Activities

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.16.5-TG |
| **Version** | 1.0 |
| **Assessment Area** | Compliance Dashboard, Metrics Consolidation, Executive Reporting |
| **Related Policy** | ISMS-POL-A.8.16, All Sections |
| **Purpose** | Consolidate metrics from A.8.16.1-4 assessments into executive dashboard with compliance scoring |
| **Target Audience** | Security Management, CISO, Compliance Officers, Executive Leadership, Auditors |
| **Assessment Type** | Data Consolidation & Reporting |
| **Review Cycle** | Monthly (dashboard updates), Quarterly (full review) |
| **Date** | 22.01.2026 |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Original] | Initial technical specification | ISMS Implementation Team |

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.8.16.5-UG.

---

# Technical Specification

# ISMS-IMP-A.8.16.5 - Compliance Dashboard Specification
# Excel Workbook Layout Specification
## ISO/IEC 27001:2022 Control A.8.16: Monitoring Activities

---

# Document Overview

**Document ID:** ISMS-IMP-A.8.16.5-TG  
**Assessment Area:** Overall Compliance Dashboard & Master Metrics  
**Related Policy:** All ISMS-POL-A.8.16 sections  
**Purpose:** Consolidated compliance dashboard aggregating all monitoring activity assessments  
**Generator Script:** `generate_a816_5_compliance_dashboard.py`  
**Output Filename:** `ISMS-IMP-A.8.16.5_Compliance_Dashboard_YYYYMMDD.xlsx`

---

# Workbook Structure

**Total Sheets:** 7
1. Instructions & Legend
2. Executive Summary
3. Detailed Compliance Matrix
4. Key Performance Indicators (KPIs)
5. Gap Analysis & Remediation Tracker
6. Trend Analysis
7. Evidence Register & Approvals

---

# Sheet 2: Executive Summary

## Header
**Title:** "MONITORING ACTIVITIES - EXECUTIVE SUMMARY"  
**Subtitle:** "ISO/IEC 27001:2022 Control A.8.16 Compliance Status"

## Section 1: Overall Compliance Score (Rows 3-12)

**Visual Compliance Gauge:**
```
Overall Compliance:  [XX%] â– â– â– â– â– â– â– â– â–¡â–¡ 
Status:              [✅ Compliant / ⚠️ Partial / ❌ Non-Compliant]
Assessment Date:     DD.MM.YYYY
Next Review:         DD.MM.YYYY
```

**Compliance by Assessment Area:**
| Assessment | Domain | Compliance % | Status | Trend |
|------------|--------|--------------|--------|-------|
| IMP-A.8.16.1 | Infrastructure | Formula | Formula | ↑/→/↓ |
| IMP-A.8.16.2 | Baseline & Detection | Formula | Formula | ↑/→/↓ |
| IMP-A.8.16.3 | Coverage | Formula | Formula | ↑/→/↓ |
| IMP-A.8.16.4 | Alert Management | Formula | Formula | ↑/→/↓ |
| **OVERALL** | **All Domains** | **Formula** | **Formula** | **↑/→/↓** |

## Section 2: Critical Metrics Summary (Rows 16-30)

| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| **Coverage Metrics** |
| Critical Systems Monitored | Formula | 100% | Formula |
| Overall System Coverage | Formula | >80% | Formula |
| Network Segment Coverage | Formula | 100% | Formula |
| **Detection Metrics** |
| Baseline Coverage (Critical) | Formula | 100% | Formula |
| Detection Rate | Formula | >90% | Formula |
| False Positive Rate | Formula | <25% | Formula |
| **Response Metrics** |
| MTTD (Critical Alerts) | Formula | <5 min | Formula |
| MTTR (Critical Incidents) | Formula | <8 hrs | Formula |
| SLA Compliance | Formula | >95% | Formula |
| **Operational Metrics** |
| Log Sources Integrated | Formula | Target | Formula |
| Active Detection Rules | Formula | Target | Formula |
| SOC Analyst Coverage | Formula | 24/7 | Formula |

## Section 3: Top 5 Strengths (Rows 34-42)
| Rank | Strength | Evidence |
|------|----------|----------|
| 1 | [Auto-populated from assessments] | [Link to evidence] |
| 2 | ... | ... |

## Section 4: Top 5 Gaps (Rows 45-53)
| Priority | Gap | Risk | Remediation Target |
|----------|-----|------|-------------------|
| Critical | [Auto-populated] | High | DD.MM.YYYY |

## Section 5: Management Recommendations (Rows 56-68)

- Investment priorities
- Resource needs
- Strategic improvements
- Compliance actions

---

# Sheet 3: Detailed Compliance Matrix

## Header
**Title:** "DETAILED COMPLIANCE MATRIX"

## Matrix Structure (Rows 3-150)

**Column Headers:**
| Col | Header | Width |
|-----|--------|-------|
| A | Policy Reference | 25 |
| B | Requirement | 40 |
| C | Control Type | 18 |
| D | Assessment Sheet | 22 |
| E | Evidence Location | 30 |
| F | Implementation Status | 20 |
| G | Compliance Status | 20 |
| H | Gap Description | 35 |
| I | Risk Level | 15 |
| J | Remediation Owner | 20 |
| K | Target Date | 14 |
| L | Notes | 25 |

**Requirements Mapped:**

- All requirements from S2.1 (Infrastructure) - ~25 requirements
- All requirements from S2.2 (Baseline & Detection) - ~30 requirements
- All requirements from S2.3 (Alert Management) - ~25 requirements
- All requirements from S2.4 (Retention) - ~15 requirements
- All requirements from S3 (Roles) - ~10 requirements
- **Total: ~105 requirement rows**

**Auto-Population from Assessment Workbooks:**

- Import compliance status from IMP-A.8.16.1 through IMP-A.8.16.4
- Aggregate to policy requirement level
- Flag gaps and non-compliance

## Compliance Scoring (Formula-driven)
```
Compliant Count: =COUNTIF(G:G,"✅ Compliant")
Partial Count: =COUNTIF(G:G,"⚠️ Partial")
Non-Compliant Count: =COUNTIF(G:G,"❌ Non-Compliant")
Overall %: =Compliant/(Compliant+Partial+Non-Compliant)*100
```

---

# Sheet 4: Key Performance Indicators (KPIs)

## Section 1: Coverage KPIs (Rows 3-20)

| KPI | Current | Target | Baseline | Trend (3mo) | Status |
|-----|---------|--------|----------|-------------|--------|
| **Asset Coverage** |
| Critical Systems Monitored % | [Input] | 100% | [Historical] | Chart | Status |
| High Priority Systems % | [Input] | >80% | [Historical] | Chart | Status |
| Overall Asset Coverage % | [Input] | >80% | [Historical] | Chart | Status |
| Network Segments Covered % | [Input] | 100% | [Historical] | Chart | Status |
| **Log Source Integration** |
| Log Sources Integrated (Count) | [Input] | Target | [Historical] | Chart | Status |
| Log Volume (GB/day) | [Input] | Capacity | [Historical] | Chart | Status |
| Log Collection Reliability % | [Input] | >99% | [Historical] | Chart | Status |

## Section 2: Detection KPIs (Rows 23-42)

| KPI | Current | Target | Baseline | Trend | Status |
|-----|---------|--------|----------|-------|--------|
| **Baseline Metrics** |
| Tier 1 Systems with Baselines % | [Input] | 100% | [Historical] | Chart | Status |
| Tier 2 Systems with Baselines % | [Input] | >80% | [Historical] | Chart | Status |
| Baseline Staleness (Avg Days Since Review) | [Input] | <90 | [Historical] | Chart | Status |
| **Detection Rule Health** |
| Active Detection Rules (Count) | [Input] | Target | [Historical] | Chart | Status |
| MITRE ATT&CK Coverage % | [Input] | >60% | [Historical] | Chart | Status |
| Detection Rate (Testing) % | [Input] | >90% | [Historical] | Chart | Status |
| False Positive Rate % | [Input] | <25% | [Historical] | Chart | Status |
| Rules Requiring Tuning (Count) | [Input] | <10 | [Historical] | Chart | Status |

## Section 3: Response KPIs (Rows 45-65)

| KPI | Current | Target | Baseline | Trend | Status |
|-----|---------|--------|----------|-------|--------|
| **Alert Metrics** |
| Total Alerts (30d) | [Input] | Target | [Historical] | Chart | Status |
| Alerts by Severity (Critical/High/Med/Low) | [Input] | Profile | [Historical] | Chart | Status |
| True Positive Rate % | [Input] | >20% | [Historical] | Chart | Status |
| Alert-to-Incident Ratio | [Input] | Target | [Historical] | Chart | Status |
| **Response Time Metrics** |
| MTTA - Critical (minutes) | [Input] | <15 | [Historical] | Chart | Status |
| MTTT - Critical (minutes) | [Input] | <60 | [Historical] | Chart | Status |
| MTTI - Critical (hours) | [Input] | <4 | [Historical] | Chart | Status |
| MTTR - Critical (hours) | [Input] | <8 | [Historical] | Chart | Status |
| SLA Compliance Rate % | [Input] | >95% | [Historical] | Chart | Status |
| **Escalation Metrics** |
| Escalation Rate % | [Input] | Target | [Historical] | Chart | Status |
| False Escalation Rate % | [Input] | <10% | [Historical] | Chart | Status |

## Section 4: Operational KPIs (Rows 68-85)

| KPI | Current | Target | Baseline | Trend | Status |
|-----|---------|--------|----------|-------|--------|
| **SOC Operations** |
| SOC Analyst Count | [Input] | Target | [Historical] | Chart | Status |
| Alerts per Analyst per Shift | [Input] | <50 | [Historical] | Chart | Status |
| SOC Coverage Model | [Input] | 24/7 | N/A | N/A | Status |
| Training Completion % | [Input] | 100% | [Historical] | Chart | Status |
| **Infrastructure Health** |
| SIEM Availability % | [Input] | >99.5% | [Historical] | Chart | Status |
| Search Performance (seconds) | [Input] | <10 | [Historical] | Chart | Status |
| Storage Utilization % | [Input] | <80% | [Historical] | Chart | Status |
| Indexing Lag (minutes) | [Input] | <5 | [Historical] | Chart | Status |

---

# Sheet 5: Gap Analysis & Remediation Tracker

## Section 1: Gap Inventory (Rows 3-60)

| Gap ID | Source Assessment | Gap Category | Description | Risk | Impact | Remediation Plan | Owner | Target Date | Budget | Status | % Complete | Last Updated |
|--------|-------------------|--------------|-------------|------|--------|------------------|-------|-------------|--------|--------|------------|--------------|
| [Auto-populated from IMP-A.8.16.1-4] | | | | | | | | | | | | |

**Gap Categories:**

- Infrastructure Gap
- Baseline Gap
- Coverage Gap
- Detection Gap
- Alert Management Gap
- Process Gap
- Resource Gap

## Section 2: Gap Summary by Category (Rows 63-75)
| Category | Total | Critical | High | Medium | Low | Open | In Progress | Resolved |
|----------|-------|----------|------|--------|-----|------|-------------|----------|
| Infrastructure | Formula | Formula | Formula | Formula | Formula | Formula | Formula | Formula |
| Baseline & Detection | Formula | Formula | Formula | Formula | Formula | Formula | Formula | Formula |
| Coverage | Formula | Formula | Formula | Formula | Formula | Formula | Formula | Formula |
| Alert Management | Formula | Formula | Formula | Formula | Formula | Formula | Formula | Formula |
| **TOTAL** | Formula | Formula | Formula | Formula | Formula | Formula | Formula | Formula |

## Section 3: Remediation Timeline (Rows 78-95)

- Gantt chart style timeline
- Gaps by month
- Critical path items highlighted
- Resource allocation

## Section 4: Risk Heat Map (Rows 98-110)
```
                Impact
            Low  Med  High
Likelihood:
High        [Count gaps by quadrant]
Med         
Low         
```

---

# Sheet 6: Trend Analysis

## Section 1: Compliance Trend (Rows 3-18)
**Monthly compliance % over 12 months**
| Month | Overall % | Infrastructure % | Baseline % | Coverage % | Alert Mgmt % |
|-------|-----------|------------------|------------|-----------|--------------|
| Jan 2025 | [Historical] | ... | ... | ... | ... |
| ... | | | | | |
| Dec 2025 | [Current] | ... | ... | ... | ... |

**Line chart showing trends**

## Section 2: KPI Trends (Rows 21-45)
**Key metrics over time (12 months):**

- Critical system coverage %
- Detection rate %
- False positive rate %
- MTTD (Critical)
- MTTR (Critical)
- SLA compliance %

## Section 3: Gap Closure Rate (Rows 48-60)
**Monthly gap remediation tracking:**
| Month | New Gaps | Closed Gaps | Net Change | Total Open |
|-------|----------|-------------|------------|------------|
| ... | | | | |

## Section 4: Incident Detection Effectiveness (Rows 63-75)
**Quarterly analysis:**
| Quarter | Incidents Detected by Monitoring | Incidents Missed | Detection Rate % | Lessons Learned |
|---------|----------------------------------|------------------|------------------|-----------------|
| ... | | | | |

---

# Sheet 7: Evidence Register & Approvals

## Section 1: Evidence Register (Rows 3-102)
**100 rows for evidence tracking**

| Evidence ID | Evidence Type | Description | Related Requirement | Source Assessment | Date Collected | Collected By | Location/Link | Verification Status | Verified By | Verification Date | Notes |
|-------------|---------------|-------------|-------------------|-------------------|----------------|--------------|---------------|-------------------|-------------|------------------|-------|

## Section 2: Approval Workflow (Rows 105-130)

**Assessment Prepared By:**

- Name: [Input]
- Title: [Input]
- Date: [Input]
- Signature: [Space for signature]

**Reviewed By (SOC Lead):**

- Name: [Input]
- Title: [Input]
- Review Comments: [Multi-line text]
- Date: [Input]
- Signature: [Space]

**Reviewed By (Security Engineering):**

- Name: [Input]
- Title: [Input]
- Review Comments: [Multi-line text]
- Date: [Input]
- Signature: [Space]

**Approved By (CISO):**

- Name: [Input]
- Title: [Input]
- Approval Decision: [Dropdown: Approved, Approved with Conditions, Rejected]
- Conditions/Comments: [Multi-line text]
- Date: [Input]
- Signature: [Space]

**Executive Acknowledgment (Optional):**

- Name: [Input]
- Title: [Input]
- Date: [Input]
- Signature: [Space]

---

# Data Import Instructions

**This workbook is designed to aggregate data from:**

- ISMS-IMP-A.8.16.1_Monitoring_Infrastructure_YYYYMMDD.xlsx
- ISMS-IMP-A.8.16.2_Baseline_Detection_YYYYMMDD.xlsx
- ISMS-IMP-A.8.16.3_Coverage_Assessment_YYYYMMDD.xlsx
- ISMS-IMP-A.8.16.4_Alert_Management_YYYYMMDD.xlsx

**Import Method:**
1. Manual copy-paste from Summary Dashboards
2. Excel Power Query (recommended for automation)
3. Python script to aggregate (advanced)

**Formula References:**

- Use INDIRECT() for dynamic workbook references
- Use INDEX/MATCH for lookups across workbooks
- Implement data validation to prevent manual errors

---

**END OF SPECIFICATION**

---

# Integration Testing Procedures

**Before deploying dashboard to production, test:**

## Test 1: Data Import Validation

**Procedure:**
1. Place all 4 source assessment workbooks in same directory
2. Run dashboard generation (script or manual)
3. Verify ALL metrics populated (no blank cells, no #REF! errors)
4. Spot-check 10 metrics against source data (manual verification)

**Pass Criteria:** 100% metrics match source, no errors

---

## Test 2: Formula Validation

**Procedure:**
1. Manually calculate overall compliance score from components
2. Compare to dashboard-calculated score
3. Test all 4 area scores (Infrastructure, Baselines, Coverage, Alert Mgmt)
4. Verify weighting (20% + 25% + 30% + 25% = 100%)

**Pass Criteria:** Manual calc matches dashboard calc (within 0.1%)

---

## Test 3: Trend Analysis Test

**Procedure:**
1. If historical data exists, verify quarter-over-quarter calculations
2. Check trend direction indicators (up/down/stable)
3. Validate charts display historical data correctly

**Pass Criteria:** Trend calculations correct, charts display properly

---

## Test 4: Hyperlink / Drill-Down Test

**Procedure:**
1. Click 10 random metrics on dashboard
2. Verify hyperlink navigates to correct source sheet
3. Validate source cell contains expected data

**Pass Criteria:** All tested hyperlinks work, point to correct data

---

## Test 5: Gap Consolidation Test

**Procedure:**
1. Count gaps in each source assessment:

   - A.8.16.1 gaps: ___
   - A.8.16.2 gaps: ___
   - A.8.16.3 gaps: ___
   - A.8.16.4 gaps: ___
   - Total: ___

2. Count gaps in dashboard consolidated gaps sheet: ___

3. Verify totals match (allowing for deduplication)

**Pass Criteria:** All gaps accounted for, no missing gaps

---

## Test 6: Update Procedure Test

**Procedure:**
1. Modify data in one source assessment (change a metric)
2. Re-run dashboard generation
3. Verify dashboard reflects changed data
4. Check update timestamp on dashboard

**Pass Criteria:** Dashboard updates correctly when source data changes

---

# Maintenance Procedures

## Monthly Maintenance (1-2 hours)

**Tasks:**
1. Update A.8.16.4 data (latest month alert management metrics)
2. Update gap remediation status (mark closed gaps, update target dates)
3. Refresh dashboard calculations
4. Review with CISO/Security Manager
5. Distribute to stakeholders

**Checklist:**

- [ ] Extract latest A.8.16.4, Sheet 6 (Alert Quality Metrics)
- [ ] Update gaps remediation status (Sheet 7)
- [ ] Recalculate compliance score
- [ ] Update trend charts (if monthly tracking)
- [ ] Review executive summary
- [ ] Distribute updated dashboard

---

## Quarterly Maintenance (8-12 hours)

**Tasks:**
1. Re-run all 4 source assessments (A.8.16.1-4)
2. Full dashboard regeneration
3. Quarter-over-quarter trend analysis
4. Management review meeting
5. Archive previous quarter dashboard

**Checklist:**

- [ ] Update A.8.16.1 (Infrastructure) - verify platforms, log sources
- [ ] Update A.8.16.2 (Baselines) - verify detection rules, MITRE coverage
- [ ] Update A.8.16.3 (Coverage) - verify asset/network/identity/app coverage
- [ ] Update A.8.16.4 (Alert Mgmt) - verify SLA compliance, investigation quality
- [ ] Regenerate dashboard with all new data
- [ ] Calculate quarter-over-quarter trends
- [ ] Create quarterly presentation for management
- [ ] Archive previous quarter dashboard for historical tracking

---

## Annual Maintenance (2-3 days)

**Tasks:**
1. Complete re-assessment of all areas (deep dive)
2. Review compliance scoring methodology (are weights still appropriate?)
3. Update dashboard structure if needed (new metrics, visualizations)
4. Validate against audit requirements
5. Executive review and planning for next year

**Checklist:**

- [ ] Deep-dive assessment of all 4 areas (not just refresh)
- [ ] Review scoring weights with CISO (adjust if needed)
- [ ] Update dashboard template if new requirements
- [ ] Validate against ISO 27001:2022 standard (any updates?)
- [ ] Executive presentation with annual trends
- [ ] Planning for next year improvements

---

# Automated Dashboard Generation

**For organizations preferring automation over manual Excel:**

Python scripts can automate dashboard generation by:
1. Reading data from source assessment Excel files
2. Calculating compliance scores
3. Generating dashboard workbook with charts
4. Creating trend analysis from historical data

**Advantages:**

- Consistent dashboard generation
- Faster updates (monthly/quarterly)
- Reduced manual errors
- Repeatable process

**Disadvantages:**

- Initial development time
- Maintenance required if source structure changes
- Requires Python expertise

Python automation code available as separate script: `generate_a816_5_compliance_dashboard.py`

---

# Document Change Log

**Version 2.0 (22.01.2026):**

- Added comprehensive Part I: User Guide (1,217 lines)
- Enhanced with dashboard implementation workflow
- Added compliance scoring framework with examples
- Added executive reporting templates (monthly and quarterly)
- Added trend analysis procedures
- Added 8 common pitfalls with solutions
- Enhanced quality validation checklist
- Added integration testing and maintenance procedures

**Version 1.0 (Original):**

- Technical specification only (353 lines)
- Sheet structures and column definitions
- Basic dashboard layout

---

# Appendix: Quick Reference

## Compliance Scoring Weights (Default)

| Area | Weight | Rationale |
|------|--------|-----------|
| Infrastructure | 20% | Foundation for monitoring |
| Baselines & Detection | 25% | Core detection capability |
| Coverage | 30% | Most critical - must monitor assets |
| Alert Management | 25% | Operational effectiveness |

**Customize weights based on organizational priorities.**

---

## Compliance Status Thresholds

| Score | Status | Action |
|-------|--------|--------|
| 90-100% | Fully Compliant | Maintain |
| 80-89% | Substantially Compliant | Address gaps per plan |
| 70-79% | Partially Compliant | Urgent remediation |
| 60-69% | Minimally Compliant | Immediate action |
| <60% | Non-Compliant | Escalate to executive |

---

## Update Frequency

| Update Type | Frequency | Effort | Tasks |
|-------------|-----------|--------|-------|
| **Monthly** | 1st week of month | 1-2 hours | A.8.16.4 update, gap status, trend refresh |
| **Quarterly** | After quarter end | 8-12 hours | All assessments, full dashboard, trend analysis |
| **Annual** | Once per year | 2-3 days | Deep-dive assessments, scoring review, planning |

---

## Key Dashboard Sheets

| Sheet | Purpose | Data Source |
|-------|---------|-------------|
| **Sheet 1** | Instructions & Legend | N/A |
| **Sheet 2** | Executive Summary | Calculated from Sheets 3-6 |
| **Sheet 3** | Compliance Matrix | A.8.16.1-4 |
| **Sheet 4** | KPIs | A.8.16.1-4 |
| **Sheet 5** | Gap Remediation Tracker | All A.8.16.1-4 |
| **Sheet 6** | Trend Analysis | Historical dashboards |
| **Sheet 7** | Evidence & Approvals | Source assessment files, Management approval |

---

**END OF SPECIFICATION**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
