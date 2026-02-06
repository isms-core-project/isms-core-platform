**ISMS-IMP-A.5.4.4-TG - Security Culture Survey**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.5.4: Management Responsibilities

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.4.4-TG |
| **Version** | 1.0 |
| **Control Reference** | ISO/IEC 27001:2022 - A.5.4 Management Responsibilities |
| **Parent Policy** | ISMS-POL-A.5.4 - Management Responsibilities |
| **Owner** | CISO |
| **Classification** | Internal |
| **Last Updated** | [Date to be set] |

---

# Technical Specification

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

<!-- QA_VERIFIED: 2026-02-06 -->
