<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.28.5-UG:framework:UG:a.8.28.5 -->
**ISMS-IMP-A.8.28.5-UG - Compliance Dashboard (Master Aggregator) Specification**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.28: Secure Coding

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.28.5-UG |
| **Version** | 1.0 |
| **Assessment Area** | Compliance Dashboard & Master Aggregator |
| **Related Policy** | ISMS-POL-A.8.28 (All Sections) - Control A.8.28 Master Policy |
| **Purpose** | Aggregate compliance data from all four operational assessments (SDLC, Tools, Review/Testing, Supply Chain) to provide executive-level visibility and unified compliance tracking |
| **Target Audience** | CISO, CTO, Board of Directors, Audit Committee, Application Security Leadership, Risk Management, Auditors |
| **Assessment Type** | Consolidation & Reporting |
| **Review Cycle** | Quarterly (Aligned with Board Reporting Cycles) |
| **Date** | [Date]|

**Version History**:

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | [Date] | Initial dashboard specification |

**Approvers**:

- Application Security Lead (Technical Review)
- Chief Information Security Officer (Executive Approval)
- Chief Technology Officer (Stakeholder Review)

**Related Documents**:

- ISMS-POL-A.8.28 - Secure Coding Policy (Master Policy)
- ISMS-IMP-A.8.28.1 - SDLC Assessment
- ISMS-IMP-A.8.28.2 - Standards & Tools Assessment
- ISMS-IMP-A.8.28.3 - Code Review & Testing Assessment
- ISMS-IMP-A.8.28.4 - Third-Party & OSS Assessment

---

# Dashboard Overview

## What This Dashboard Does

This is the **master compliance dashboard** for ISO/IEC 27001:2022 Control A.8.28 (Secure Coding). It consolidates and aggregates data from all four operational assessments to provide:

- **Executive-level visibility** into overall secure coding maturity
- **Cross-cutting gap analysis** across all assessment domains
- **Prioritized remediation roadmap** for organizational improvement
- **Compliance metrics** for board reporting and audit readiness
- **Trend analysis** for continuous improvement tracking

**Core Philosophy**: As Feynman said, *"If you cannot measure it, you cannot improve it."*

This dashboard transforms individual assessment data into actionable intelligence for decision-makers.

**Critical Difference**: Unlike Assessments 1-4 which are standalone, this dashboard **AGGREGATES and REFERENCES** data from those workbooks, providing a unified compliance view.

**Anti-Cargo-Cult Principle**: This dashboard shows the TRUTH about your secure coding posture. It aggregates real data from actual assessments, not aspirational policy statements.

## Who Should Use This Dashboard

**Primary Users**:

- **CISO**: Strategic decision-making, resource allocation
- **CTO**: Technical program oversight, remediation prioritization
- **Board / Audit Committee**: Governance and risk oversight
- **Application Security Leadership**: Program management and improvement

**Supporting Users**:

- Engineering leadership (remediation planning)
- Compliance team (audit readiness)
- Risk management (risk appetite alignment)
- External auditors (compliance verification)

**Not for**: Individual developers (use source assessment workbooks instead)

## When to Generate/Update Dashboard

**Initial Creation**: After completion of ALL FOUR assessments (IMP 1-4)

**Regular Updates**:

- **Quarterly**: Refresh data from source assessments for board reporting
- **After Each Assessment Cycle**: Update when any assessment workbook is refreshed
- **Before Audits**: Ensure current compliance posture is documented
- **After Major Incidents**: Reflect updated risk posture

**Historical Tracking**:

- Archive previous dashboard versions for trend analysis
- Maintain historical data for year-over-year comparison

## Prerequisites

**CRITICAL**: This dashboard REQUIRES completed source assessments:

✅ **Must Have FIRST**:
1. **ISMS-IMP-A.8.28.1** - SDLC Assessment (completed)
2. **ISMS-IMP-A.8.28.2** - Standards & Tools Assessment (completed)
3. **ISMS-IMP-A.8.28.3** - Code Review & Testing Assessment (completed)
4. **ISMS-IMP-A.8.28.4** - Third-Party & OSS Assessment (completed)

**Without these four source assessments, this dashboard CANNOT be generated.**

The dashboard pulls data via Excel formulas (external links) from these source workbooks.

## Dashboard Output

**Generated Workbook**: `ISMS-IMP-A.8.28.5_Compliance_Dashboard_YYYYMMDD.xlsx`  
**Python Generator**: `generate_a828_5_compliance_dashboard.py`

**Contains**:

- 9 sheets providing comprehensive compliance overview
- Executive one-page summary
- Cross-cutting gap analysis
- Prioritized remediation roadmap
- Historical trend tracking
- CISO approval sign-off

---

# Dashboard Workflow (Step-by-Step)

## Step 1: Complete All Four Source Assessments

**Before you can create the dashboard, you MUST complete**:

1. **IMP-A.8.28.1 (SDLC)** → Saved as `ISMS-IMP-A.8.28.1_SDLC_Assessment_YYYYMMDD.xlsx`
2. **IMP-A.8.28.2 (Tools)** → Saved as `ISMS-IMP-A.8.28.2_Standards_Tools_Assessment_YYYYMMDD.xlsx`
3. **IMP-A.8.28.3 (Review/Testing)** → Saved as `ISMS-IMP-A.8.28.3_Code_Review_Testing_Assessment_YYYYMMDD.xlsx`
4. **IMP-A.8.28.4 (Supply Chain)** → Saved as `ISMS-IMP-A.8.28.4_Third_Party_OSS_Assessment_YYYYMMDD.xlsx`

**File Organization**:
```
/assessments/A.8.28/
  ├── ISMS-IMP-A.8.28.1_SDLC_Assessment_20260125.xlsx
  ├── ISMS-IMP-A.8.28.2_Standards_Tools_Assessment_20260125.xlsx
  ├── ISMS-IMP-A.8.28.3_Code_Review_Testing_Assessment_20260125.xlsx
  ├── ISMS-IMP-A.8.28.4_Third_Party_OSS_Assessment_20260125.xlsx
  └── ISMS-IMP-A.8.28.5_Compliance_Dashboard_20260125.xlsx  ← This file
```

**Keep all files in the same directory** for Excel external links to work.

## Step 2: Normalize Source Assessment Files (Optional)

If your source assessment files have different naming or are in different folders, run the normalization script:

```bash
# Optional: Normalize file names and locations
python3 normalize_assessment_files_a828.py
```

This script:

- Standardizes file names
- Moves files to common directory
- Validates all required sheets exist

## Step 3: Generate Dashboard Workbook

```bash
# Generate dashboard workbook
python3 generate_a828_5_compliance_dashboard.py

# Output: ISMS-IMP-A.8.28.5_Compliance_Dashboard_20260125.xlsx
```

**What This Creates**:

- Empty dashboard workbook with all sheets
- Excel formulas linking to source assessments
- Pre-configured charts and visualizations
- Template for manual data entry (historical trends, etc.)

## Step 4: Open Dashboard and Update Links

**Open the generated workbook**:
1. Open `ISMS-IMP-A.8.28.5_Compliance_Dashboard_YYYYMMDD.xlsx`
2. Excel will prompt: "Update links to other workbooks?"
3. Click **"Update"** (this pulls data from source assessments)

**If links are broken**:

- Go to: Data → Edit Links → Update Values
- Or: Data → Edit Links → Change Source (point to correct files)

**Formulas will auto-populate** data from source assessments into dashboard.

## Step 5: Review Executive Dashboard Sheet

**Sheet**: `Executive Dashboard`  
**Auto-Populated from Source Assessments**

**What You'll See**:

**Section 1: Overall Compliance Summary**

- Overall Control A.8.28 Compliance: XX%
- Total Requirements Assessed: 360 (90 per assessment × 4)
- Implemented: XX
- Partial: XX
- Not Implemented: XX
- N/A: XX

**Section 2: Domain-by-Domain Breakdown**
| Domain | Compliance % | Status | Critical Gaps |
|--------|--------------|--------|---------------|
| 1. SDLC Security | XX% | 🟢/🟡/🔴 | X |
| 2. Tools & Standards | XX% | 🟢/🟡/🔴 | X |
| 3. Review & Testing | XX% | 🟢/🟡/🔴 | X |
| 4. Supply Chain Security | XX% | 🟢/🟡/🔴 | X |

**Status Indicators**:

- 🟢 Green (≥80%): Excellent
- 🟡 Yellow (60-79%): Needs attention
- 🔴 Red (<60%): Critical gaps

**Section 3: Key Findings** (auto-summarized):

- Highest compliance domain
- Lowest compliance domain
- Total critical gaps across all domains
- Total high-priority gaps
- Recommended focus areas

**Section 4: Compliance Trend** (if historical data available):

- Quarter-over-quarter compliance trajectory
- Improvement velocity (gaps closed per quarter)
- Areas of consistent weakness

## Step 6: Review Gap Analysis

**Sheet**: `Gap Analysis`  
**Consolidates gaps from all four assessments**

**Columns**:

- Gap ID (consolidated numbering)
- Source Assessment (IMP 1/2/3/4)
- Domain (which assessment domain)
- Gap Description
- Priority (Critical/High/Medium/Low)
- Owner
- Target Date
- Status

**Critical Analysis**:

- How many critical gaps across all domains?
- Are critical gaps distributed or concentrated?
- Are there cross-cutting themes (e.g., "lack of automation")?
- Are target dates realistic and committed?

**Cross-Cutting Pattern Detection**:
Look for common themes:

- "Automation gaps" appearing in multiple assessments?
- "Training needs" across multiple domains?
- "Tool effectiveness" issues in Tools + Review/Testing?

## Step 7: Review Risk Register

**Sheet**: `Risk Register`  
**Consolidates high-risk items from all assessments**

**Risk Categories**:

- SDLC Process Risks (from IMP-A.8.28.1)
- Tool Effectiveness Risks (from IMP-A.8.28.2)
- Review/Testing Coverage Risks (from IMP-A.8.28.3)
- Supply Chain Risks (from IMP-A.8.28.4)

**For Each Risk**:

- Risk description
- Likelihood (Low/Medium/High)
- Impact (Low/Medium/High)
- Risk score (calculated)
- Mitigation status
- Owner

## Step 8: Review Remediation Roadmap

**Sheet**: `Remediation Roadmap`  
**Prioritized action plan across all domains**

**Roadmap Structure**:

**Phase 1: Critical Gaps (0-30 days)**

- List of all critical-priority gaps
- Assigned owners
- Target completion dates
- Dependencies

**Phase 2: High-Priority Gaps (31-90 days)**

- High-priority items
- Resource requirements
- Dependencies on Phase 1

**Phase 3: Medium-Priority Gaps (91-180 days)**

- Medium-priority improvements
- Process changes
- Training initiatives

**Phase 4: Low-Priority / Continuous Improvement (181+ days)**

- Long-term improvements
- Optimization initiatives
- Nice-to-have enhancements

**Resource Requirements**:

- FTE estimate for remediation
- Budget requirements (tools, training, consulting)
- Timeline dependencies

## Step 9: Review KPIs & Metrics

**Sheet**: `KPIs & Metrics`  
**Track key performance indicators across all domains**

**Metrics Categories**:

**SDLC Metrics** (from IMP-A.8.28.1):

- Security requirements coverage (% projects with security reqs)
- Threat modeling coverage (% projects with threat models)
- Security sign-off compliance

**Tool Metrics** (from IMP-A.8.28.2):

- SAST/DAST/SCA coverage (% applications scanned)
- Tool effectiveness (vulnerabilities found vs. false positives)
- Developer adoption rate

**Review/Testing Metrics** (from IMP-A.8.28.3):

- Code review coverage (% code reviewed)
- Security test coverage (% security tests executed)
- Vulnerabilities caught in review vs. production

**Supply Chain Metrics** (from IMP-A.8.28.4):

- SBOM coverage (% applications with current SBOM)
- Vulnerability remediation MTTR (mean time to remediate)
- License compliance rate (% dependencies compliant)

**Overall Maturity Score**:

- Calculated based on all metrics
- Trend analysis (improving/declining)

## Step 10: Update Evidence Register

**Sheet**: `Evidence_Register`  
**Consolidates evidence from all four assessments**

**Purpose**: Single source of truth for audit evidence

**For Each Evidence Item**:

- Evidence ID (consolidated from source assessments)
- Source Assessment (IMP 1/2/3/4)
- Requirement ID
- Evidence type
- Description
- Location/link
- Last verified date
- Verification status

**Audit Readiness Check**:

- Are all "Implemented" claims backed by evidence?
- Is evidence current (verified within last quarter)?
- Are evidence links accessible?

## Step 11: Update Action Items & Follow-up

**Sheet**: `Action Items & Follow-up`  
**Track actions arising from dashboard review**

**Action Item Types**:

- Gap remediation tasks
- Evidence collection tasks
- Process improvement initiatives
- Training needs
- Tool procurement/configuration
- Policy updates

**For Each Action**:

- Action description
- Owner
- Due date
- Status (Not Started/In Progress/Complete/Blocked)
- Blockers (if any)
- Completion date (when done)

## Step 12: Update Audit & Compliance Log

**Sheet**: `Audit & Compliance Log`  
**Track audits and compliance reviews**

**Log Entries**:

- Audit date
- Audit type (Internal/External/Certification)
- Auditor
- Findings count (Critical/High/Medium/Low)
- Findings remediated
- Next audit date
- Compliance status

**Historical Tracking**:

- Trend in audit findings (improving?)
- Recurring findings (not being fixed?)
- Compliance trajectory

## Step 13: Obtain CISO Approval

**Sheet**: `Approval Sign-Off`  
**Executive approval of compliance posture**

**Required Approvers**:
1. **Dashboard Compiler**: Application Security Analyst
2. **Application Security Lead**: Technical accuracy review
3. **CTO**: Resource commitment and prioritization
4. **CISO**: Executive approval and risk acceptance

**Approval Criteria**:

- All four source assessments complete and current
- Gap analysis accurate and complete
- Remediation roadmap has committed owners and dates
- Risk register reflects current risk posture
- CISO acknowledges compliance status and accepts residual risk

**Approval Statement**:
"I acknowledge the current Control A.8.28 compliance status as reflected in this dashboard. I approve the remediation roadmap and commit organizational resources to address identified gaps in accordance with the proposed timeline."

---

# Understanding Your Dashboard Results

## Overall Compliance Interpretation

**Overall Compliance** = (Total Implemented + 0.5×Total Partial) / (Total Requirements - Total N/A) × 100%

**Compliance Levels**:

- **≥85%**: Excellent - Control A.8.28 is well-implemented
- **70-84%**: Good - Minor gaps exist, targeted improvements needed
- **55-69%**: Adequate - Significant gaps, remediation plan required
- **40-54%**: Needs Improvement - Major compliance gaps, high risk
- **<40%**: Critical - Fundamental security controls missing

**Reality Check**:

- Don't celebrate 85% if critical gaps exist
- Focus on gap severity, not just percentage
- Look for cross-cutting weaknesses (same issue across multiple domains)

## Domain Analysis

**Which domain needs most attention?**

Look for:

- Lowest compliance percentage
- Highest count of critical gaps
- Declining trend (getting worse, not better)

**Common Patterns**:

**If SDLC (IMP-1) is weakest**:

- Problems: Security not integrated early enough
- Impact: Security defects introduced in requirements/design
- Fix: Invest in security requirements, threat modeling, secure design

**If Tools (IMP-2) is weakest**:

- Problems: Tools not deployed or not effective
- Impact: Vulnerabilities not detected automatically
- Fix: Deploy/configure SAST/DAST/SCA, improve effectiveness

**If Review/Testing (IMP-3) is weakest**:

- Problems: Manual verification insufficient
- Impact: Vulnerabilities slip through to production
- Fix: Improve code review, expand security testing, Security Champions

**If Supply Chain (IMP-4) is weakest**:

- Problems: Third-party risk not managed
- Impact: Supply chain attacks, unpatched dependencies
- Fix: Deploy SCA, maintain SBOM, vendor security assessments

## Gap Prioritization

**Critical Gaps (Fix Immediately)**:

- No SBOM (supply chain blind spot)
- No SCA tool (dependency vulnerabilities undetected)
- No code review for production code (basic control missing)
- Critical vulnerabilities >30 days unpatched
- GPL license contamination

**High-Priority Gaps (Fix Within Quarter)**:

- Incomplete SBOM (missing transitive deps)
- SAST/DAST not integrated in CI/CD
- Security testing gaps (API testing, auth testing)
- Vendor security assessments overdue

**Medium-Priority Gaps (Fix Within 6 Months)**:

- OSS approval process gaps
- Tool effectiveness issues (high false positive rate)
- Security Champion program immature
- Training needs

**Low-Priority Gaps (Continuous Improvement)**:

- Process documentation improvements
- Tool optimization
- Efficiency enhancements

## Trend Analysis (If Historical Data Available)

**Positive Trends** (Good News):

- Compliance percentage increasing quarter-over-quarter
- Critical gap count decreasing
- Remediation velocity improving (gaps closed faster)
- Tool effectiveness improving (more real issues, fewer false positives)

**Negative Trends** (Warning Signs):

- Compliance percentage declining
- Same gaps appearing repeatedly (not being fixed)
- Remediation velocity slowing
- New gap introduction rate exceeds closure rate

**Stagnant (Neither Improving nor Declining)**:

- Compliance percentage flat
- Gaps shuffling (closing old, opening new)
- Resource constraints preventing progress

---

# Common Dashboard Pitfalls

## "Garbage In, Garbage Out"

**Problem**: Dashboard is only as good as source assessments

❌ **Anti-Pattern**:

- Source assessments inflated ("everything is Implemented")
- Evidence lacking or superficial
- Assessments not refreshed (stale data)
- Cherry-picking good results

✅ **Good Practice**:

- Source assessments are honest and evidence-based
- Regular assessment refresh (quarterly minimum)
- Evidence verified by auditors
- Trends reflect reality, not wishful thinking

**How to Detect**:

- If overall compliance >90% but production incidents reveal gaps
- If no critical gaps but obvious security issues exist
- If compliance has been "85%" for 2 years straight (no improvement)

## Dashboard Theater

**Problem**: Dashboard looks good but doesn't reflect reality

❌ **Anti-Pattern**:

- Dashboard generated for audit, then ignored
- Remediation roadmap never executed
- Gaps marked "Complete" without verification
- CISO approval without reading dashboard

✅ **Good Practice**:

- Dashboard reviewed quarterly by CISO/CTO
- Remediation roadmap actively tracked
- Gap closure verified with evidence
- Dashboard drives actual security improvements

## "Aggregate and Forget"

**Problem**: Dashboard consolidates data but no one acts on it

❌ **Anti-Pattern**:

- Dashboard presented to board, no follow-up
- Critical gaps identified, no action taken
- Remediation roadmap exists, no owners assigned
- Same dashboard findings quarter after quarter

✅ **Good Practice**:

- Board expects quarterly progress updates
- Critical gaps have committed owners and dates
- Remediation progress tracked and reported
- Dashboard drives accountability

## Missing the Forest for the Trees

**Problem**: Focusing on overall percentage, missing critical gaps

❌ **Anti-Pattern**:

- "We're at 85%, we're good!"
- Ignoring that 15% includes critical gaps like "no SBOM"
- Celebrating improvement in low-priority areas while critical gaps persist

✅ **Good Practice**:

- Critical gaps addressed first, regardless of percentage
- Cross-cutting themes identified and addressed
- Focus on risk reduction, not just compliance percentage

---

# Dashboard Maintenance

## Quarterly Update Process

**Every Quarter**:

1. **Refresh Source Assessments** (IMP 1-4):

   - Regenerate assessment workbooks
   - Update evidence (last 3 months data)
   - Re-assess all requirements
   - Obtain fresh approvals

2. **Update Dashboard**:

   - Open dashboard workbook
   - Click "Update Links" (pulls fresh data from source assessments)
   - Review auto-populated metrics
   - Add new historical trend data point

3. **Review with CISO/CTO**:

   - Present updated dashboard
   - Highlight changes from last quarter
   - Discuss remediation progress
   - Identify new priorities

4. **Update Remediation Roadmap**:

   - Mark completed gaps as "Complete"
   - Add new gaps identified
   - Re-prioritize based on current risk
   - Assign owners for new gaps

5. **Archive Previous Version**:

   - Save previous dashboard with date suffix
   - Maintain historical record for trend analysis

## Annual Deep Dive

**Once Per Year**:

- Comprehensive re-assessment across all four domains
- External audit/penetration test findings incorporated
- Benchmark against industry standards (BSIMM, OWASP SAMM)
- Board presentation on secure coding maturity
- Budget planning for next year's improvements

## Event-Driven Updates

**Update Dashboard After**:

- Major security incident (post-incident review findings)
- Significant process changes (new tools, new SDLC)
- Audit findings requiring remediation
- Regulatory changes affecting compliance

---

# Quality Checklist

**Dashboard Completeness**:

- [ ] All four source assessments completed and current
- [ ] All Excel links updated and working
- [ ] All metrics auto-populated from source assessments
- [ ] Historical trend data added (if available)
- [ ] Gap analysis includes all gaps from source assessments
- [ ] Remediation roadmap has owners and dates
- [ ] Evidence register consolidated from source assessments

**Data Accuracy**:

- [ ] Overall compliance calculation verified manually
- [ ] Domain breakdowns match source assessment summaries
- [ ] Critical gap count matches source assessments
- [ ] Metrics are current (not stale)
- [ ] Trend data is accurate (matches archived dashboards)

**Stakeholder Engagement**:

- [ ] CISO reviewed and approved dashboard
- [ ] CTO committed to remediation roadmap
- [ ] Board/Audit Committee received executive summary
- [ ] Engineering leadership engaged on remediation

**Actionability**:

- [ ] Critical gaps have immediate action plans
- [ ] Remediation roadmap is resourced and committed
- [ ] Owners assigned for all gaps
- [ ] Progress tracking mechanism established
- [ ] Next review date scheduled

**Anti-Cargo-Cult Check**:

- [ ] Dashboard reflects reality (not aspirations)
- [ ] Source assessments are honest and evidence-based
- [ ] Remediation commitments are realistic
- [ ] Trends show actual progress (or lack thereof)
- [ ] Dashboard drives actual improvements (not just reporting)

---

**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
