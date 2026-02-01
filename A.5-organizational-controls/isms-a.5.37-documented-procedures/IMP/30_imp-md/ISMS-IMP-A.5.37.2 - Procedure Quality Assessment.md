# ISMS-IMP-A.5.37.2 - Procedure Quality Assessment

## Document Information

| Field | Value |
|-------|-------|
| **Document ID** | ISMS-IMP-A.5.37.2 |
| **Control Reference** | ISO/IEC 27001:2022 - Control A.5.37: Documented Operating Procedures |
| **Version** | 1.0 |
| **Classification** | Internal Use |
| **Owner** | Information Security Manager |
| **Last Review** | [Date to be set] |

---

## Control Requirement

> "Operating procedures for information processing facilities should be documented and made available to personnel who need them."
>
> — ISO/IEC 27001:2022, Annex A Control 5.37

---

# PART I: USER GUIDE

## 1. Purpose

This workbook assesses the quality and completeness of documented operating procedures. While A.5.37.1 inventories procedures, this assessment evaluates whether each procedure meets quality standards for clarity, completeness, and usability.

## 2. Quality Framework

### 2.1 Quality Dimensions

| Dimension | Weight | Description |
|-----------|:------:|-------------|
| **Clarity** | 20% | Can be understood by target audience |
| **Completeness** | 20% | Covers all necessary steps and scenarios |
| **Accuracy** | 20% | Reflects current systems and processes |
| **Usability** | 20% | Practical to follow in operations |
| **Maintainability** | 20% | Easy to update when changes occur |

### 2.2 Quality Scoring

| Score | Rating | Description |
|:-----:|--------|-------------|
| 5 | Excellent | Fully meets all criteria, best practice |
| 4 | Good | Meets criteria with minor improvements needed |
| 3 | Adequate | Meets minimum requirements |
| 2 | Needs Improvement | Significant gaps exist |
| 1 | Poor | Major deficiencies, high risk |
| 0 | Missing | Element not present |

### 2.3 Quality Elements Checklist

#### Document Structure
- [ ] Title and document ID clearly stated
- [ ] Version number and date present
- [ ] Owner and approver identified
- [ ] Scope and applicability defined
- [ ] Prerequisites listed

#### Content Quality
- [ ] Step-by-step instructions provided
- [ ] Decision points clearly marked
- [ ] Error handling procedures included
- [ ] Escalation paths defined
- [ ] Contact information current

#### Operational Elements
- [ ] Recovery procedures documented
- [ ] Rollback instructions included
- [ ] Verification steps specified
- [ ] Expected outcomes stated
- [ ] Time estimates provided (where applicable)

## 3. Assessment Process

### Step 1: Select Procedures for Review
- Prioritise critical and high-risk procedures
- Include recently created or modified procedures
- Sample across all categories

### Step 2: Conduct Quality Review
- Apply quality checklist to each procedure
- Score each dimension (1-5)
- Document specific findings

### Step 3: Calculate Quality Score
- Weight dimension scores
- Generate overall quality rating
- Identify improvement priorities

### Step 4: Remediation Planning
- Create improvement actions for low-scoring items
- Assign owners and deadlines
- Track to completion

---

# PART II: TECHNICAL SPECIFICATION

## 4. Workbook Structure

### Sheet 1: Quality_Assessment
**Purpose:** Detailed quality scoring for each procedure

| Column | Header | Data Type | Validation | Description |
|:------:|--------|-----------|------------|-------------|
| A | Procedure_ID | Text | From Inventory | Reference to A.5.37.1 |
| B | Procedure_Name | Text | Lookup | Auto-populated |
| C | Assessment_Date | Date | Required | Date of quality review |
| D | Assessor | Text | Required | Person conducting review |
| E | Clarity_Score | Number | 0-5 | Clarity dimension score |
| F | Completeness_Score | Number | 0-5 | Completeness dimension score |
| G | Accuracy_Score | Number | 0-5 | Accuracy dimension score |
| H | Usability_Score | Number | 0-5 | Usability dimension score |
| I | Maintainability_Score | Number | 0-5 | Maintainability dimension score |
| J | Overall_Score | Number | Formula | Weighted average |
| K | Quality_Rating | Text | Formula | Excellent/Good/Adequate/Poor |
| L | Priority_Improvements | Text | Multi-value | Key improvement areas |
| M | Findings | Text | Optional | Detailed findings |
| N | Next_Review | Date | Formula | Based on rating |

**Rating Thresholds:**
- Excellent: ≥4.5
- Good: 3.5-4.49
- Adequate: 2.5-3.49
- Needs Improvement: 1.5-2.49
- Poor: <1.5

### Sheet 2: Quality_Checklist
**Purpose:** Detailed checklist items for thorough assessment

| Column | Header | Data Type | Description |
|:------:|--------|-----------|-------------|
| A | Procedure_ID | Text | Reference to procedure |
| B | Check_Category | Text | Structure/Content/Operations |
| C | Check_Item | Text | Specific check description |
| D | Status | List | Pass/Partial/Fail/N/A |
| E | Finding | Text | Specific observation |
| F | Recommendation | Text | Improvement suggestion |

**Checklist Items (Pre-populated):**

*Document Structure:*
1. Document ID and title present
2. Version control information
3. Owner and approver identified
4. Last review date documented
5. Scope clearly defined
6. Prerequisites listed
7. Related documents referenced

*Content Quality:*
8. Purpose statement clear
9. Step-by-step instructions
10. Decision trees/flowcharts where needed
11. Screenshots/diagrams included
12. Error handling documented
13. Escalation procedures defined
14. Contact information current
15. Glossary of terms (if needed)

*Operational Elements:*
16. Pre-execution checks defined
17. Execution steps numbered
18. Verification steps included
19. Expected outcomes stated
20. Rollback procedures documented
21. Recovery steps included
22. Time estimates provided
23. Resource requirements listed

### Sheet 3: Improvement_Actions
**Purpose:** Track quality improvement actions

| Column | Header | Data Type | Description |
|:------:|--------|-----------|-------------|
| A | Action_ID | Text | Unique identifier |
| B | Procedure_ID | Text | Related procedure |
| C | Dimension | List | Quality dimension affected |
| D | Issue_Description | Text | What needs improvement |
| E | Action_Required | Text | Specific action to take |
| F | Owner | Text | Responsible person |
| G | Priority | List | Critical/High/Medium/Low |
| H | Target_Date | Date | Completion deadline |
| I | Status | List | Open/In Progress/Completed/Cancelled |
| J | Completion_Date | Date | When completed |
| K | Verification | Text | How completion verified |

### Sheet 4: Trend_Analysis
**Purpose:** Track quality improvements over time

| Column | Header | Data Type | Description |
|:------:|--------|-----------|-------------|
| A | Period | Text | Assessment period (e.g., Q1 2026) |
| B | Procedures_Assessed | Number | Count assessed |
| C | Avg_Clarity | Number | Average clarity score |
| D | Avg_Completeness | Number | Average completeness score |
| E | Avg_Accuracy | Number | Average accuracy score |
| F | Avg_Usability | Number | Average usability score |
| G | Avg_Maintainability | Number | Average maintainability score |
| H | Overall_Avg | Number | Overall average |
| I | Excellent_Count | Number | Procedures rated Excellent |
| J | Poor_Count | Number | Procedures rated Poor |
| K | Improvement_% | Number | Change from previous period |

### Sheet 5: Evidence_Register
**Purpose:** Link to assessment evidence

| Column | Header | Data Type | Description |
|:------:|--------|-----------|-------------|
| A | Evidence_ID | Text | Unique identifier |
| B | Evidence_Type | List | Assessment/Screenshot/Document |
| C | Procedure_ID | Text | Related procedure |
| D | Description | Text | Evidence description |
| E | Collection_Date | Date | When collected |
| F | Location | Text | Storage location |
| G | Collected_By | Text | Assessor name |

### Sheet 6: Instructions
**Purpose:** User guidance for quality assessment

Static content including:
- Assessment methodology
- Scoring guidance
- Checklist explanations
- Best practice examples

## 5. Formulas and Calculations

### Overall Quality Score
```excel
=(E2*0.2)+(F2*0.2)+(G2*0.2)+(H2*0.2)+(I2*0.2)
```

### Quality Rating
```excel
=IF(J2>=4.5,"Excellent",IF(J2>=3.5,"Good",IF(J2>=2.5,"Adequate",IF(J2>=1.5,"Needs Improvement","Poor"))))
```

### Next Review Date (Based on Rating)
```excel
=IF(K2="Excellent",C2+365,IF(K2="Good",C2+180,IF(K2="Adequate",C2+90,C2+30)))
```

### Checklist Pass Rate
```excel
=COUNTIF(D:D,"Pass")/(COUNTIF(D:D,"Pass")+COUNTIF(D:D,"Partial")+COUNTIF(D:D,"Fail"))*100
```

### Improvement Action Completion Rate
```excel
=COUNTIF(I:I,"Completed")/COUNTA(A:A)*100
```

## 6. Conditional Formatting Rules

| Range | Condition | Format |
|-------|-----------|--------|
| Quality Score | <2.5 | Red fill |
| Quality Score | 2.5-3.49 | Yellow fill |
| Quality Score | ≥3.5 | Green fill |
| Quality Rating | "Poor" | Red fill, bold |
| Action Status | "Open" + Past Due | Red fill |
| Checklist Status | "Fail" | Red fill |

## 7. Data Validation

### Score Validation
- Range: 0-5
- Decimal places: 1

### Status Values
- Pass, Partial, Fail, N/A

### Priority Values
- Critical, High, Medium, Low

## 8. Integration Points

### Upstream Dependencies
- A.5.37.1 Procedure Inventory (Procedure_ID lookup)
- Procedure document repository

### Downstream Consumers
- A.5.37.4 Compliance Dashboard
- Management reporting
- Audit evidence packages

## 9. Output Metrics

| Metric | Formula | Target |
|--------|---------|--------|
| Average Quality Score | AVERAGE(J:J) | ≥4.0 |
| Procedures Excellent/Good | COUNT(K="Excellent" or "Good") | >80% |
| Open Improvement Actions | COUNTIF(Status="Open") | Decreasing |
| Checklist Pass Rate | Formula above | >90% |
| Period-over-Period Improvement | Current-Previous | Positive |

---

**END OF SPECIFICATION**

---

*"Quality is not an act, it is a habit."*
— Aristotle

*Where bamboo antennas actually work.* 🎋

<!-- QA_VERIFIED: 2026-02-01 -->
