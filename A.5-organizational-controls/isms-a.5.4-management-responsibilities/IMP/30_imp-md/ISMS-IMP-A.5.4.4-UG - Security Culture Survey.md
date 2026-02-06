**ISMS-IMP-A.5.4.4-UG - Security Culture Survey**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.5.4: Management Responsibilities

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.4.4-UG |
| **Version** | 1.0 |
| **Control Reference** | ISO/IEC 27001:2022 - A.5.4 Management Responsibilities |
| **Parent Policy** | ISMS-POL-A.5.4 - Management Responsibilities |
| **Owner** | CISO |
| **Classification** | Internal |
| **Last Updated** | [Date to be set] |

---

### 1. Assessment Overview

#### 1.1 Purpose

This workbook supports annual employee security culture assessments, measuring how personnel perceive management's commitment to security, policy awareness, training effectiveness, and their own security responsibilities. Results drive targeted improvement actions.

#### 1.2 Scope

Survey covers all personnel:
- Full-time employees
- Part-time employees
- Long-term contractors (>6 months)

Excludes: Short-term contractors, temporary staff

#### 1.3 Control Requirement

Per ISO/IEC 27001:2022 Control A.5.4, management must ensure personnel apply information security appropriately. This survey measures whether management's efforts are perceived as effective by the workforce.

#### 1.4 Why This Matters

**The Perception Gap**: Management may believe their security program is effective, but employees may perceive it differently. This gap creates blind spots:
- Policies that seem clear to management may be confusing to staff
- Training that management considers sufficient may feel irrelevant to employees
- Reporting channels that management trusts may seem intimidating to personnel

**This survey closes that gap** by measuring the employee experience of security culture. It answers the question: "Do our people actually feel supported in doing security right?"

**Real-World Impact**:
- Organisations with strong security culture have 70% fewer security incidents
- Employees who feel comfortable reporting issues catch 80% of threats before they escalate
- Security training perceived as relevant achieves 3x better knowledge retention

**The ISMS Copilot Connection**: During Stage 2 audits, auditors will ask for evidence that the security program reaches and resonates with the workforce. This survey provides:
- Quantitative data on perceived management commitment
- Evidence that training is perceived as effective
- Metrics on psychological safety for incident reporting
- Year-over-year trends showing improvement efforts

**Survey Categories Explained**:

| Category | What It Measures | Why It Matters |
|----------|------------------|----------------|
| **Leadership Commitment** | Whether employees see management actively supporting security | Sets tone from top; correlates with employee compliance |
| **Policy Awareness** | Whether employees understand security policies | Awareness is prerequisite to compliance |
| **Training Effectiveness** | Whether training is perceived as useful and relevant | Poor training perception predicts poor knowledge retention |
| **Reporting Culture** | Whether employees feel safe reporting issues | Critical for early threat detection |
| **Personal Responsibility** | Whether employees feel ownership of security | Engaged employees are first line of defence |

#### 1.5 Assessment Frequency

| Activity | Frequency | Timing |
|----------|-----------|--------|
| Full survey deployment | Annually | Q4 |
| Pulse surveys (optional) | Quarterly | Q1-Q3 |
| Results analysis | Within 30 days of survey close | |
| Action plan development | Within 60 days of survey close | |

### 2. Prerequisites

Before deploying the survey, ensure:

- [ ] Survey tool configured (e.g., Microsoft Forms, SurveyMonkey)
- [ ] Employee distribution list current
- [ ] Executive sponsor communication drafted
- [ ] Prior year results available (for comparison)
- [ ] Analysis resources allocated

### 3. Workbook Structure

| Sheet | Purpose | When to Complete |
|-------|---------|------------------|
| **Instructions** | Guidance and scoring methodology | Reference |
| **Survey Questions** | Standard 20-question survey template | Survey design |
| **Response Data** | Aggregated responses by department | Post-survey |
| **YoY Trend Analysis** | Year-over-year comparison | Post-survey |
| **Action Plan** | Improvement actions for low-scoring areas | Post-analysis |
| **Executive Summary** | High-level results for leadership | Reporting |

### 4. Survey Categories and Questions

The survey covers 5 categories with 4 questions each (20 questions total):

| Category | Weight | Focus |
|----------|:------:|-------|
| Leadership Commitment | 20% | Visible management support for security |
| Policy Awareness | 20% | Understanding of security policies |
| Training Effectiveness | 20% | Quality and relevance of training |
| Reporting Culture | 20% | Comfort reporting security issues |
| Personal Responsibility | 20% | Individual security ownership |

**Response Scale**: 1 (Strongly Disagree) to 5 (Strongly Agree)

### 5. Completion Walkthrough

#### Step 1: Deploy Survey

1. Export questions from **Survey Questions** sheet
2. Configure survey tool with 1-5 scale
3. Draft executive sponsor announcement
4. Deploy to all in-scope personnel
5. Send reminders at Day 7 and Day 14
6. Close survey after 3 weeks

**Target Response Rate**: ≥80%

#### Step 2: Aggregate Response Data

After survey closes:
1. Export raw responses from survey tool
2. Calculate average score per question
3. Calculate average score per category
4. Aggregate by department in **Response Data** sheet
5. Calculate **Overall_Avg** for each department
6. Calculate **TOTAL** row for organisation-wide averages

#### Step 3: Complete YoY Trend Analysis

Compare current results with prior years:
1. Enter current year category averages
2. Enter prior year data (Year-1, Year-2, Year-3)
3. Calculate **YoY_Change** (Current - Year-1)
4. Set **Trend**: Improving (+0.2 or more), Stable (±0.2), Declining (-0.2 or more)
5. Review **OVERALL** row for organisation trend

#### Step 4: Develop Action Plan

For any category scoring below 3.5/5.0 (70%):
1. Generate **Action_ID** (format: SCS-NN)
2. Record **Current_Score**
3. Calculate **Gap** (3.5 - Current_Score)
4. Define **Action_Required** (specific improvement)
5. Assign **Owner**
6. Set **Due_Date** (within 12 months)
7. Track **Status**

**Prioritisation**: Address largest gaps first

#### Step 5: Prepare Executive Summary

Compile results for leadership:
1. Calculate **Overall Culture Score** (average of all categories)
2. Record **Survey Response Rate**
3. Count **Categories Meeting Target** (≥3.5/5.0)
4. Calculate **YoY Improvement** (vs prior year)
5. Summarise each category with score and priority action
6. Set **Status**: Exceeds Target, Meets Target, Below Target, Critical

### 6. Worked Examples

#### Example A: Strong Security Culture Results

**Response Data Summary**:
| Department | Respondents | Rate | Leadership | Policy | Training | Reporting | Personal | Overall |
|------------|:-----------:|:----:|:----------:|:------:|:--------:|:---------:|:--------:|:-------:|
| Engineering | 45/50 | 90% | 4.2 | 4.0 | 3.9 | 4.5 | 4.3 | 4.2 |
| Finance | 28/30 | 93% | 4.1 | 4.3 | 4.0 | 4.2 | 4.0 | 4.1 |
| IT | 38/40 | 95% | 4.4 | 4.2 | 4.1 | 4.6 | 4.4 | 4.3 |
| Sales | 42/55 | 76% | 3.4 | 3.2 | 3.0 | 3.5 | 3.3 | 3.3 |
| **TOTAL** | **253/300** | **84%** | **4.0** | **3.9** | **3.8** | **4.2** | **3.9** | **4.0** |

**Analysis**:
- Overall score 4.0/5.0 = **Exceeds Target** ✅
- Response rate 84% = Above 80% threshold ✅
- 4/5 categories meet target
- **Sales department** significantly below average across all categories → Requires targeted intervention
- **Reporting Culture** highest score (4.2) → Employees feel safe reporting issues
- **Training Effectiveness** lowest score (3.8) → Training content review recommended

**Action Plan Generated**:
| Action_ID | Category | Current | Gap | Action | Owner |
|-----------|----------|:-------:|:---:|--------|-------|
| SCS-01 | Training Effectiveness | 3.8 | -0.3 | Review training content for role relevance | L&D Manager |
| SCS-02 | Sales (All Categories) | 3.3 | -0.2 | Department-specific culture initiative | Sales VP + CISO |

---

#### Example B: Concerning Security Culture Results

**Response Data Summary**:
| Department | Respondents | Rate | Leadership | Policy | Training | Reporting | Personal | Overall |
|------------|:-----------:|:----:|:----------:|:------:|:--------:|:---------:|:--------:|:-------:|
| Engineering | 25/50 | 50% | 3.0 | 2.8 | 2.5 | 2.9 | 3.1 | 2.9 |
| Finance | 20/30 | 67% | 3.2 | 3.0 | 2.8 | 2.7 | 3.0 | 2.9 |
| IT | 30/40 | 75% | 3.1 | 2.9 | 2.6 | 3.0 | 3.2 | 2.9 |
| Operations | 40/60 | 67% | 2.8 | 2.6 | 2.4 | 2.5 | 2.8 | 2.6 |
| **TOTAL** | **180/270** | **67%** | **3.0** | **2.8** | **2.6** | **2.8** | **3.0** | **2.8** |

**Analysis**:
- Overall score 2.8/5.0 = **Critical** ⚠️ (below 3.0 threshold)
- Response rate 67% = Below 80% threshold ⚠️
- 0/5 categories meet target
- Low response rate itself indicates engagement problem
- **Training Effectiveness** lowest score (2.6) → Critical intervention needed
- **Reporting Culture** concerning (2.8) → Employees may not feel safe reporting

**Immediate Escalation Required**:
1. Executive briefing to CEO within 48 hours
2. All-hands communication acknowledging results
3. Commitment to specific improvements
4. Follow-up pulse survey in 3 months

**Action Plan Generated**:
| Action_ID | Category | Current | Gap | Action | Owner | Due |
|-----------|----------|:-------:|:---:|--------|-------|-----|
| SCS-01 | All | 2.8 | -0.7 | Executive commitment communication | CEO | 2 weeks |
| SCS-02 | Training | 2.6 | -0.9 | Complete training overhaul | L&D + CISO | Q2 |
| SCS-03 | Reporting | 2.8 | -0.7 | Anonymous reporting channel launch | Security Team | 1 month |
| SCS-04 | Leadership | 3.0 | -0.5 | Manager security training | HR + CISO | Q2 |
| SCS-05 | Response Rate | 67% | -13% | Engagement campaign for next survey | HR + Comms | Next survey |

---

#### Example C: Interpreting Year-over-Year Trends

**YoY Trend Analysis**:
| Category | 2023 | 2024 | 2025 | Change | Trend |
|----------|:----:|:----:|:----:|:------:|:-----:|
| Leadership Commitment | 3.2 | 3.5 | 4.0 | +0.8 | ↑ Improving |
| Policy Awareness | 3.0 | 3.3 | 3.9 | +0.9 | ↑ Improving |
| Training Effectiveness | 2.8 | 3.2 | 3.8 | +1.0 | ↑ Improving |
| Reporting Culture | 3.5 | 3.8 | 4.2 | +0.7 | ↑ Improving |
| Personal Responsibility | 3.3 | 3.6 | 3.9 | +0.6 | ↑ Improving |
| **OVERALL** | **3.2** | **3.5** | **4.0** | **+0.8** | **↑ Improving** |

**Executive Narrative**: "Our security culture program has achieved consistent year-over-year improvement across all categories. The 3-year trend shows overall culture score improving from 3.2 (Below Target) to 4.0 (Exceeds Target). Key drivers:
- Executive visibility initiatives (Leadership +0.8)
- Training redesign with role-specific content (Training +1.0)
- Anonymous reporting channel implementation (Reporting +0.7)

Recommended: Maintain current programs, focus on sustaining gains."

---

#### Example D: Department Comparison for Root Cause Analysis

When one department consistently underperforms, investigate:

| Question to Ask | Data Source | Action if Concerning |
|-----------------|-------------|---------------------|
| Is it a management issue? | Compare Leadership score vs other depts | Manager coaching |
| Is it a training issue? | Compare Training score vs other depts | Targeted training |
| Is turnover high? | HR data | Focus on onboarding |
| Are policies unclear for this function? | Compare Policy score + interviews | Policy revision |
| Is there fear of reporting? | Compare Reporting score + exit interviews | Culture intervention |

### 7. Survey Administration Best Practices

#### Pre-Survey Communication

**What to Communicate** (from Executive Sponsor):
1. Purpose of survey (improving security support for employees)
2. Anonymity assurance (specific technical measures taken)
3. How results will be used (improvement actions, not punishment)
4. Timeline (survey open period, when results shared)
5. Importance of honest feedback

**Sample Executive Announcement**:

> *Subject: Your Voice Matters - Annual Security Culture Survey*
>
> Dear Colleagues,
>
> Next week we launch our annual Security Culture Survey. This survey helps us understand how well we're supporting you in keeping our organisation secure.
>
> **What you need to know:**
> - The survey is anonymous - we cannot trace responses to individuals
> - It takes approximately 10 minutes
> - Your honest feedback drives real improvements
> - Results will be shared with all staff, along with our action plan
>
> Last year's survey led to [specific improvement]. Your feedback makes a difference.
>
> Please complete the survey by [date]. Thank you for helping us build a stronger security culture.
>
> [CEO/CISO Name]

#### During Survey Period

**Reminder Schedule**:
| Day | Action | Message Focus |
|-----|--------|---------------|
| 1 | Survey launch | Full details, anonymity assurance |
| 7 | First reminder | "50% complete, your voice matters" |
| 14 | Second reminder | "Final week, don't miss your chance" |
| 18 | Final reminder | "Closes tomorrow, last opportunity" |
| 21 | Survey closes | Thank you message |

**Tracking Completion** (without identifying individuals):
- Monitor response rate by department
- If department below 70% at Day 14, ask department head to encourage participation
- Note: Encourage, don't mandate - coerced responses are less honest

#### Post-Survey Actions

**Closing the Loop** (Critical for Trust):
1. **Within 30 days**: Share high-level results with all staff
2. **Within 60 days**: Publish action plan for improvement
3. **Quarterly**: Update on progress against action plan
4. **Next survey**: Reference prior actions and outcomes

**What NOT to Do**:
- ❌ Share only positive results
- ❌ Ignore low scores
- ❌ Punish managers for department scores
- ❌ Promise actions you can't deliver
- ❌ Skip the follow-up communication

### 8. Scoring Thresholds

| Score Range | Status | Action Required |
|:-----------:|--------|-----------------|
| 4.0-5.0 | Exceeds Target | Maintain; share best practices |
| 3.5-3.9 | Meets Target | Monitor; incremental improvements |
| 3.0-3.4 | Below Target | Action plan required |
| <3.0 | Critical | Immediate intervention; executive escalation |

### 7. Evidence Collection

| Evidence Type | Description | Retention |
|---------------|-------------|-----------|
| Raw survey responses | Anonymised response data | 3 years |
| Survey tool export | Full dataset with timestamps | 3 years |
| Analysis workbook | This completed workbook | 3 years |
| Action plan artifacts | Improvement documentation | 3 years |
| Executive presentation | Summary deck | 3 years |

**Evidence Storage**: `[SharePoint/Evidence Library]/A.5.4/Security-Culture-Survey/[Year]/`

### 8. Common Pitfalls

❌ **MISTAKE**: Deploying survey without executive sponsorship
✅ **CORRECT**: Have CEO/CISO send announcement emphasising importance

❌ **MISTAKE**: Making survey responses identifiable
✅ **CORRECT**: Ensure anonymity to get honest feedback

❌ **MISTAKE**: Analysing only organisation-wide averages
✅ **CORRECT**: Break down by department to identify specific issues

❌ **MISTAKE**: Ignoring low response rates
✅ **CORRECT**: Target ≥80%; low rates indicate engagement issues

❌ **MISTAKE**: Developing generic improvement actions
✅ **CORRECT**: Create specific, measurable actions tied to findings

❌ **MISTAKE**: Not communicating results back to employees
✅ **CORRECT**: Share summary and planned actions to close the loop

❌ **MISTAKE**: Conducting survey but not following up on actions
✅ **CORRECT**: Track actions to completion; report progress quarterly

❌ **MISTAKE**: Comparing results across very different time periods
✅ **CORRECT**: Compare year-over-year at consistent survey timing

❌ **MISTAKE**: Using only organisation-wide averages for action planning
✅ **CORRECT**: Drill down to department level to identify specific intervention targets

❌ **MISTAKE**: Surveying too frequently (quarterly full surveys cause fatigue)
✅ **CORRECT**: Annual full survey with optional quarterly pulse surveys (5 questions max)

### 10. Trend Analysis Methodology

#### Calculating Meaningful Trends

**Minimum Data Requirements**:
- 2 years of data required for any trend claims
- 3 years recommended for reliable trend assessment
- Consistent survey timing (same quarter each year)
- Consistent question wording (changes invalidate comparisons)

**Trend Classification**:
| YoY Change | Trend Category | Interpretation |
|:----------:|----------------|----------------|
| ≥+0.3 points | **Improving** | Initiatives having positive impact |
| ±0.2 points | **Stable** | Maintaining current position |
| ≤-0.3 points | **Declining** | Attention required, investigate cause |

**Statistical Significance Note**:
With typical survey sample sizes (200-500 responses), a change of ±0.2 may be within normal variation. Changes of ±0.3 or greater are more likely to represent real shifts.

#### Correlation Analysis

Look for correlations between categories:

| Correlation | Possible Interpretation |
|-------------|-------------------------|
| Low Leadership + Low Training | Management not prioritising security education |
| Low Policy + Low Personal | Unclear policies lead to disengagement |
| Low Reporting + Low Leadership | Fear of blame culture from management |
| High Training + Low Personal | Training isn't translating to behaviour |
| High Leadership + High Everything | Strong tone from top lifts all categories |

#### Benchmarking Considerations

**Internal Benchmarks** (Recommended):
- Compare current year to prior years
- Compare departments within organisation
- Track improvement against own baseline

**External Benchmarks** (Use with Caution):
- Industry benchmarks vary widely by survey methodology
- Different question wording invalidates comparisons
- Focus on internal improvement rather than external comparison

### 11. Quality Checklist

Before presenting results to leadership:

- [ ] Survey achieved ≥80% response rate
- [ ] All departments represented in Response Data
- [ ] Category averages calculated correctly
- [ ] YoY Trend Analysis populated with historical data
- [ ] Action Plan created for all categories below 3.5
- [ ] All actions have assigned owners and due dates
- [ ] Executive Summary accurately reflects findings
- [ ] Workbook saved with correct naming convention
- [ ] Presentation prepared for management review

### 12. Review and Approval

| Role | Responsibility | Timing |
|------|----------------|--------|
| HR/Communications | Survey deployment support | Survey period |
| Security Analyst | Data aggregation and analysis | +15 days |
| Security Manager | Review analysis; draft actions | +25 days |
| CISO | Approve action plan and summary | +30 days |
| Executive Management | Review in management meeting | Per calendar |

### 13. Audit Preparation

#### Stage 2 Audit Evidence Requirements

When auditors review security culture, prepare:

**Documentation Evidence**:
- Current survey workbook plus 2 prior years (if available)
- Survey questions exported from survey tool
- Executive sponsor announcement emails
- Action plan documentation from prior surveys

**Demonstration Requests** (be prepared to show):
1. How survey is administered (anonymity measures)
2. How response data is aggregated
3. How action plans are developed from results
4. How results are communicated back to employees

**Common Audit Questions**:

| Question | Evidence to Provide |
|----------|---------------------|
| "How do you measure security culture?" | Survey methodology, question bank, scoring |
| "What was your response rate?" | Response Data sheet showing participation |
| "What actions did you take based on results?" | Action Plan sheet with specific items |
| "How do you ensure anonymity?" | Survey tool configuration, data handling procedures |
| "Can you show improvement over time?" | YoY Trend Analysis with 2+ years of data |

---


**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
