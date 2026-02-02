# ISMS-IMP-A.5.4.4 - Security Culture Survey

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.4.4 |
| **Version** | 1.0 |
| **Control Reference** | ISO/IEC 27001:2022 - A.5.4 Management Responsibilities |
| **Parent Policy** | ISMS-POL-A.5.4 - Management Responsibilities |
| **Owner** | CISO |
| **Classification** | Internal |
| **Last Updated** | [Date to be set] |

---

## PART I: USER COMPLETION GUIDE

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

## PART II: TECHNICAL SPECIFICATION

### 14. Workbook Technical Details

#### 14.1 File Information

| Property | Value |
|----------|-------|
| Filename | `ISMS-IMP-A.5.4.4_Security_Culture_Survey_YYYYMMDD.xlsx` |
| Generator | `generate_a54_4_security_culture_survey.py` |
| Sheets | 6 |
| Protected | No |

#### 14.2 Sheet Specifications

**Sheet 1: Instructions**
- Purpose: Guidance, workflow, scoring methodology
- Rows: ~30
- No data entry required

**Sheet 2: Survey Questions**

| Column | Header | Width | Type |
|:------:|--------|:-----:|------|
| A | Question_ID | 12 | Text (Q01-Q20) |
| B | Category | 22 | Text |
| C | Question_Text | 55 | Text |
| D | Response_Scale | 40 | Text (fixed) |

**Pre-populated Questions (20 total):**

| Category | Questions |
|----------|-----------|
| Leadership Commitment | Q01-Q04 |
| Policy Awareness | Q05-Q08 |
| Training Effectiveness | Q09-Q12 |
| Reporting Culture | Q13-Q16 |
| Personal Responsibility | Q17-Q20 |

**Sheet 3: Response Data**

| Column | Header | Width | Type |
|:------:|--------|:-----:|------|
| A | Department | 15 | Text |
| B | Respondents | 12 | Number |
| C | Response_Rate | 14 | Percentage |
| D | Leadership_Commitment_Avg | 20 | Number (1-5) |
| E | Policy_Awareness_Avg | 20 | Number (1-5) |
| F | Training_Effectiveness_Avg | 20 | Number (1-5) |
| G | Reporting_Culture_Avg | 20 | Number (1-5) |
| H | Personal_Responsibility_Avg | 20 | Number (1-5) |
| I | Overall_Avg | 12 | Number (1-5) |

**Pre-populated Departments:**
Executive, Finance, IT, Operations, HR, Legal, Sales, Marketing, Engineering, Support, TOTAL

**Sheet 4: YoY Trend Analysis**

| Column | Header | Width | Type |
|:------:|--------|:-----:|------|
| A | Category | 25 | Text |
| B | Year-3 | 10 | Number |
| C | Year-2 | 10 | Number |
| D | Year-1 | 10 | Number |
| E | Current | 10 | Number |
| F | YoY_Change | 12 | Formula |
| G | Trend | 12 | List |

**YoY_Change Formula**: `=IF(AND(D{row}>0,E{row}>0),E{row}-D{row},"-")`

**Trend Values**: Improving, Stable, Declining

**Sheet 5: Action Plan**

| Column | Header | Width | Type |
|:------:|--------|:-----:|------|
| A | Action_ID | 12 | Text (SCS-NN) |
| B | Category | 22 | Text |
| C | Current_Score | 14 | Number |
| D | Gap | 8 | Formula |
| E | Action_Required | 40 | Text |
| F | Owner | 18 | Text |
| G | Due_Date | 12 | Date |
| H | Status | 12 | List |

**Gap Formula**: `=IF(C{row}>0,3.5-C{row},"-")`

**Status Values**: Not Started, In Progress, Completed, Deferred

**Sheet 6: Executive Summary**

| Section | Content |
|---------|---------|
| Title | Security Culture Survey - Executive Summary |
| Survey Period | [Year] |
| Report Date | Generated date |
| KEY METRICS | Table with Metric, Value, Benchmark |
| CATEGORY SCORES | Table with Category, Score, Status, Priority Action |

**Key Metrics:**
- Overall Culture Score ([Score]/5.0)
- Survey Response Rate
- Categories Meeting Target ([X]/5)
- YoY Improvement

**Category Status Values**: Exceeds Target, Meets Target, Below Target, Critical

#### 14.3 Survey Question Bank

| ID | Category | Question |
|:--:|----------|----------|
| Q01 | Leadership Commitment | Management demonstrates commitment to information security |
| Q02 | Leadership Commitment | Security is a visible priority at the executive level |
| Q03 | Leadership Commitment | Leaders allocate adequate resources for security initiatives |
| Q04 | Leadership Commitment | Management responds appropriately to security incidents |
| Q05 | Policy Awareness | I understand the organisation's security policies |
| Q06 | Policy Awareness | Security policies are clearly communicated |
| Q07 | Policy Awareness | I know where to find security policies and procedures |
| Q08 | Policy Awareness | Policy updates are communicated effectively |
| Q09 | Training Effectiveness | Security training is relevant to my role |
| Q10 | Training Effectiveness | I feel confident handling security situations after training |
| Q11 | Training Effectiveness | Training materials are engaging and useful |
| Q12 | Training Effectiveness | Refresher training helps maintain awareness |
| Q13 | Reporting Culture | I feel comfortable reporting security concerns |
| Q14 | Reporting Culture | Reported issues are addressed in a timely manner |
| Q15 | Reporting Culture | There is no fear of blame when reporting incidents |
| Q16 | Reporting Culture | I know how and where to report security issues |
| Q17 | Personal Responsibility | I understand my personal security responsibilities |
| Q18 | Personal Responsibility | Security is part of my daily work routine |
| Q19 | Personal Responsibility | I actively look for security risks in my work |
| Q20 | Personal Responsibility | I take ownership of protecting company information |

#### 14.4 Styling

| Element | Style |
|---------|-------|
| Title | Bold 14pt, centered |
| Headers | White text (#FFFFFF), Blue fill (#2F5496), Bold |
| Input cells | Yellow fill (#FFFFCC) |
| Locked/Formula cells | Grey fill (#F2F2F2) |
| Positive indicators | Green fill (#C6EFCE) |
| Negative indicators | Red fill (#FFC7CE) |
| All data cells | Thin black border |

### 15. Integration Points

| System | Integration | Data Flow |
|--------|-------------|-----------|
| Survey Tool | Question deployment, response collection | Survey tool → Response Data sheet |
| HR System | Employee roster, department mapping | HR → Department structure, employee count |
| LMS | Training completion correlation | LMS → Training effectiveness analysis |
| Email | Survey invitations, reminders | Email → Participation tracking |
| SharePoint | Results storage, evidence archive | Results → Evidence Library |
| A.5.4.2 | Training data correlation | Compare training scores with training completion |
| A.5.4.3 | Dashboard integration | Culture Survey score → Leadership Dashboard |

#### 15.1 Survey Tool Integration

**Recommended Survey Tools**:
| Tool | Suitability | Notes |
|------|-------------|-------|
| Microsoft Forms | Good | Part of M365, easy distribution, limited analysis |
| SurveyMonkey | Excellent | Robust analysis, anonymity features, reporting |
| Qualtrics | Enterprise | Advanced analysis, benchmarking, expensive |
| Google Forms | Basic | Free, simple, limited anonymity options |
| Typeform | Good | User-friendly interface, moderate analysis |

**Survey Tool Configuration Requirements**:
1. **Anonymity**: Disable IP tracking, email address collection
2. **Scale**: Configure 5-point Likert scale (1-5)
3. **Progress**: Show completion percentage
4. **Required**: Make all 20 questions mandatory
5. **Export**: Ensure CSV/Excel export capability

#### 15.2 HR System Integration

**Required HR Data**:
| Data Element | Purpose | Update Frequency |
|--------------|---------|------------------|
| Employee count by department | Calculate response rates | Monthly |
| Manager hierarchy | Correlate with A.5.4.1 data | Monthly |
| Employment status | Include/exclude criteria | Real-time |
| Tenure bands | Tenure-based analysis (optional) | Annual |
| Location | Site-based analysis (optional) | As needed |

**Data Privacy Considerations**:
- Do not merge individual survey responses with HR data
- Aggregate data only (department level minimum)
- Ensure minimum 5 respondents per group for reporting
- Groups <5 respondents: combine with larger group or exclude

#### 15.3 Correlation Analysis with Other A.5.4 Assessments

**Cross-Reference Matrix**:

| Culture Survey Finding | Cross-Reference with | Expected Correlation |
|-----------------------|---------------------|---------------------|
| Low Leadership Commitment score | A.5.4.1 Management Commitment | Commitment Assessment scores should align |
| Low Training Effectiveness score | A.5.4.2 Training Oversight | Check training completion rates |
| Low Reporting Culture score | A.5.4.2 Policy Violations | May see underreporting of violations |
| Department-specific low scores | A.5.4.1 by department | May indicate specific manager issues |

**Investigation Triggers**:
- If Culture Survey says "Training ineffective" but A.5.4.2 shows 100% completion → Training content issue
- If Culture Survey says "Leadership uncommitted" but A.5.4.1 shows high scores → Perception vs reality gap
- If Culture Survey Reporting Culture low but violation count also low → Fear of reporting (underreporting)

### 16. Pulse Survey Option

For organisations wanting more frequent feedback (quarterly) without survey fatigue:

**Pulse Survey Design**:
- 5 questions maximum (1 per category)
- 2-minute completion time
- Rotating questions each quarter
- No action plan requirement (trending only)

**Sample Pulse Questions** (rotate each quarter):
| Quarter | Question | Category |
|---------|----------|----------|
| Q1 | "I believe management prioritises security" | Leadership |
| Q2 | "I know where to find security policies when needed" | Policy |
| Q3 | "Security training helps me do my job safely" | Training |
| Q4 | "I would feel comfortable reporting a security issue" | Reporting |

**Pulse Survey vs Full Survey**:
| Aspect | Full Survey | Pulse Survey |
|--------|-------------|--------------|
| Frequency | Annual | Quarterly (optional) |
| Questions | 20 | 5 |
| Time | 10 minutes | 2 minutes |
| Analysis depth | Comprehensive | Trending only |
| Action plan | Required | Not required |
| Response rate target | 80% | 60% |

### 17. Version Control

**Workbook Naming Convention**:
```
ISMS-IMP-A.5.4.4_Security_Culture_Survey_[YYYY].xlsx
```

Example: `ISMS-IMP-A.5.4.4_Security_Culture_Survey_2026.xlsx`

**Question Version Control**:
- Any change to question wording requires new version
- Changed questions invalidate year-over-year comparison
- Document question changes in Instructions sheet

**Retention Requirements**:
| Document Type | Retention | Location |
|--------------|-----------|----------|
| Survey workbooks | 5 years | Evidence Library |
| Raw response data (anonymised) | 3 years | Secure storage |
| Action plan evidence | 5 years | Evidence Library |
| Executive presentations | 5 years | Evidence Library |

### 18. Related Documents

| Document ID | Title | Relationship |
|-------------|-------|--------------|
| ISMS-POL-A.5.4 | Management Responsibilities | Parent policy |
| ISMS-IMP-A.5.4.1 | Management Commitment Assessment | Complementary (management view) |
| ISMS-IMP-A.5.4.2 | Compliance Oversight Tracker | Training data correlation |
| ISMS-IMP-A.5.4.3 | Leadership Dashboard | Consolidation target |
| ISMS-IMP-A.6.3 | Awareness and Training | Training effectiveness correlation |

---

**END OF SPECIFICATION**

---

*"Culture eats strategy for breakfast."*
— Peter Drucker

<!-- QA_VERIFIED: 2026-02-02 -->
