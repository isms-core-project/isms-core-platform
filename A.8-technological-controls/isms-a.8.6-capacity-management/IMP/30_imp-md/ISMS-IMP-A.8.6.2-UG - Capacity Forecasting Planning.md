**ISMS-IMP-A.8.6.2-UG - Capacity Forecasting & Planning**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.6: Capacity Management

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.6.2-UG |
| **Version** | 1.0 |
| **Assessment Area** | Capacity Forecasting, Trend Analysis & Expansion Planning |
| **Related Policy** | ISMS-POL-A.8.6 (Capacity Management Policy) |
| **Prerequisite** | ISMS-IMP-A.8.6.1 (Capacity Utilization Assessment) - MUST be completed first |
| **Purpose** | Analyze capacity trends, forecast future requirements, plan capacity expansions, and validate forecast accuracy |
| **Target Audience** | Capacity Planning Team, Infrastructure Managers, IT Operations, Finance (Budget Planning), Auditors |
| **Assessment Type** | Analytical & Planning |
| **Review Cycle** | Quarterly (with annual deep forecasting) |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Capacity Forecasting & Planning assessment workbook | ISMS Implementation Team |

### Document Structure

This is the **User Completion Guide**. The companion Technical Specification is documented in ISMS-IMP-A.8.6.2-TG.

---

## Assessment Overview

### Purpose & Scope

**Assessment Name:** ISMS-IMP-A.8.6.2 - Capacity Forecasting & Planning

#### What This Assessment Covers

This assessment uses historical utilization data (from A.8.6.1) to forecast future capacity needs and plan expansions. This is the "WHERE will we be?" assessment that answers:

- What are the capacity usage trends? (growth, decline, stable)
- What is the growth rate? (GB/month, %/month, users/month)
- When will capacity be exhausted? (forecasted dates)
- What capacity expansions are needed? (how much, when)
- How accurate are our forecasts? (actual vs. predicted)
- What is the capacity planning budget? (cost projections)

#### Key Principle

This assessment is **data-driven and forward-looking**. You analyze historical trends to make informed predictions about future capacity needs, enabling **proactive** (planned) capacity management instead of **reactive** (emergency) capacity firefighting.

#### What You'll Document

- Historical utilization trends (3-12 months of data)
- Growth rate calculations (linear, exponential, seasonal)
- Capacity exhaustion forecasts (dates when resources hit 100%)
- Planned capacity expansions (what, when, how much, cost)
- Forecast accuracy validation (comparing previous forecasts to actual outcomes)
- Capacity planning budget (capital and operational expenses)
- Supporting evidence (trend graphs, forecast models, expansion plans)

#### How This Relates to Other A.8.6 Assessments

| Assessment            | Focus                  | Relationship to A.8.6.2           |
|-----------------------|------------------------|------------------------------------|
| ISMS-IMP-A.8.6.1     | Current Utilization     | **INPUT** - Provides historical utilization data |
| **ISMS-IMP-A.8.6.2** | **Forecasting & Planning** | **ANALYZES A.8.6.1 data to predict future needs** |
| ISMS-IMP-A.8.6.3     | Compliance Dashboard   | **OUTPUT** - Consolidates current + future view |

This assessment (A.8.6.2) **requires A.8.6.1 to be completed first** - you can't forecast without historical data!

### Who Should Complete This Assessment

#### Primary Stakeholders

1. **Capacity Planning Team** - Trend analysis, forecasting, planning
2. **Infrastructure Managers** - Resource allocation, expansion decisions
3. **IT Operations** - Operational perspective on growth patterns
4. **Finance/Procurement** - Budget planning, cost analysis
5. **Business Units** - Business growth plans that drive capacity needs

#### Required Skills

- Understanding of capacity trends and growth patterns
- Basic forecasting skills (linear regression, trend analysis)
- Excel proficiency (charts, formulas, trend lines)
- Understanding of infrastructure procurement and provisioning timelines
- Cost estimation and budgeting skills

#### Time Commitment

- **Initial assessment:** 10-15 hours (for comprehensive forecasting across all resources)
- **Quarterly updates:** 4-6 hours (update forecasts, review accuracy)
- **Annual deep forecasting:** 12-20 hours (12-month forward planning, budget cycle)

### Expected Outputs

Upon completion, you will have:

1. ✅ **Historical trend analysis** - Visualization of capacity consumption over time
2. ✅ **Growth rate calculations** - Quantified growth (GB/month, %/month)
3. ✅ **Capacity exhaustion forecasts** - Predicted dates when resources hit limits
4. ✅ **Capacity expansion plans** - What to expand, when, how much
5. ✅ **Forecast accuracy metrics** - How accurate past forecasts were
6. ✅ **Capacity planning budget** - Cost projections for expansions
7. ✅ **Proactive vs. reactive ratio** - Measure of planning effectiveness
8. ✅ **Evidence register** - Supporting documentation for audit
9. ✅ **Approved forecast** - Three-level approval workflow completed

---

## Prerequisites

### Information You'll Need

Before starting this assessment, gather:

#### 1. Completed A.8.6.1 Assessment (REQUIRED)

- **Sheet 2: Compute Capacity** - Historical CPU/memory utilization
- **Sheet 3: Storage Capacity** - Historical disk utilization and growth rates
- **Sheet 4: Network Capacity** - Historical bandwidth utilization
- **Sheet 5: Application Capacity** - Historical user/transaction counts
- **Minimum data requirement:** 90 days of historical data (180+ days preferred)

**CRITICAL:** A.8.6.2 **cannot be completed** without A.8.6.1 historical data. If A.8.6.1 is incomplete or lacks historical data, complete A.8.6.1 first.

#### 2. Extended Historical Data (If Available)

- **12+ months preferred** for annual trend analysis
- **24+ months ideal** for seasonal pattern detection
- **36+ months excellent** for long-term trend validation

Sources:

- Monitoring system historical data (Prometheus, Datadog, CloudWatch retention)
- Previous capacity assessments (if available)
- Infrastructure change logs (expansions, migrations)

#### 3. Business Growth Plans

- **Sales projections** - Expected customer/user growth
- **Product roadmap** - New features, services, applications
- **Marketing campaigns** - Seasonal or promotional events that drive usage
- **Merger/acquisition plans** - Sudden capacity demand changes
- **Geographic expansion** - New regions, datacenters

#### 4. Infrastructure Procurement Information

- **Lead times** - How long to procure/provision capacity
  - Physical hardware: 4-12 weeks typical
  - Cloud resources: Minutes to hours (but budget approval may take weeks)
  - SAN/NAS expansion: 2-4 weeks
  - Network upgrades: 4-8 weeks (ISP circuits can be longer)
- **Vendor quotes** - Cost estimates for capacity expansions
- **Budget constraints** - Available capital and operational budgets

#### 5. Policy Requirements

- ISMS-POL-A.8.6, Section 5 (Capacity Forecasting)
- ISMS-POL-A.8.6, Section 6 (Capacity Planning)
- Organizational forecasting methodology (if defined)
- Forecast accuracy targets (e.g., ±15% accuracy required)

### Required Tools

- **Microsoft Excel** (2016 or later) with Analysis ToolPak enabled
- **Historical utilization data** from A.8.6.1
- **Charting/graphing tools** (Excel built-in or Tableau, Power BI)
- **Forecasting tools** (optional):
  - Python with pandas, scikit-learn (for advanced forecasting)
  - R with forecast package
  - Excel built-in forecasting functions (FORECAST.LINEAR, TREND)

### Dependencies

**CRITICAL DEPENDENCY:**

- ✅ **A.8.6.1 (Capacity Utilization Assessment) MUST be completed first**
  - Cannot forecast without historical data
  - Minimum 90 days of data required
  - 180+ days preferred

**Soft Dependencies:**

- Business growth plans (helpful but not blocking)
- Previous capacity assessments (helpful for trend validation)
- Budget information (needed for cost planning, can be added later)

---

## Workflow

### High-Level Process

```
1. PREPARE (Gather A.8.6.1 data)
   ↓
2. ANALYZE TRENDS (Sheet 1)
   ↓
3. CALCULATE GROWTH RATES (Sheet 2)
   ↓
4. FORECAST CAPACITY EXHAUSTION (Sheet 3)
   ↓
5. PLAN CAPACITY EXPANSIONS (Sheet 4)
   ↓
6. VALIDATE FORECAST ACCURACY (Sheet 5)
   ↓
7. PLAN BUDGET (Sheet 6)
   ↓
8. REGISTER EVIDENCE (Sheet 7)
   ↓
9. REVIEW & APPROVE
```

### Detailed Workflow

#### Phase 1: Preparation (2-3 hours)

**Objective:** Gather and validate historical data from A.8.6.1

**Steps:**
1. Open completed A.8.6.1 assessment workbook
2. Verify historical data availability:

   - Check that 30-day and 90-day utilization data exists
   - Verify peak and average metrics are populated
   - Confirm data is recent (< 30 days old)

3. Export A.8.6.1 data for analysis:

   - Sheet 2 (Compute): Export CPU/memory utilization time series
   - Sheet 3 (Storage): Export disk utilization and growth rates
   - Sheet 4 (Network): Export bandwidth utilization
   - Sheet 5 (Application): Export user/transaction counts

4. Gather extended historical data (if available):

   - Query monitoring system for 180+ days of data
   - Collect previous capacity assessments

5. Read this entire User Guide
6. Schedule time with capacity planning team and finance

**Deliverable:** Validated historical dataset ready for trend analysis

**Quality Check:**

- ✓ A.8.6.1 assessment is complete and approved
- ✓ Minimum 90 days of historical data available
- ✓ Data quality verified (no major gaps or anomalies)
- ✓ Business growth plans obtained

#### Phase 2: Historical Trend Analysis (3-4 hours)

**Objective:** Complete Sheet 1 - Historical Trends

**Steps:**
1. For each resource from A.8.6.1:

   - Plot utilization over time (line chart)
   - Identify trend pattern (linear growth, exponential, seasonal, stable)
   - Calculate correlation coefficient (R²) for trend line
   - Document trend confidence (high, medium, low)

2. Look for patterns:

   - **Linear growth:** Steady increase at constant rate
   - **Exponential growth:** Accelerating increase
   - **Seasonal patterns:** Regular peaks (month-end, quarter-end, holidays)
   - **Step changes:** Sudden jumps (new application, migration)
   - **Stable/flat:** No significant change

3. Document trend observations
4. Create trend visualizations (charts/graphs)

**Deliverable:** Complete Sheet 1 with trend analysis for all resources

**Quality Check:**

- ✓ All resources from A.8.6.1 analyzed
- ✓ Trend patterns identified and documented
- ✓ Visualizations created (charts)
- ✓ Trend confidence assessed

#### Phase 3: Growth Rate Calculation (2-3 hours)

**Objective:** Complete Sheet 2 - Growth Rate Calculations

**Steps:**
1. For each resource with growing utilization:

   - Calculate absolute growth rate (GB/month, users/month)
   - Calculate percentage growth rate (%/month)
   - Calculate compound monthly growth rate (CMGR) if exponential
   - Extrapolate annual growth rate

2. Compare growth rates:

   - Actual vs. business plan (if available)
   - Current period vs. previous period
   - Resource-to-resource (which is growing fastest?)

3. Document growth drivers:

   - Business growth (new customers, users)
   - New applications or features
   - Data accumulation (logs, databases)
   - Seasonal factors

4. Flag anomalies:

   - Negative growth (declining utilization - optimization, migration?)
   - Sudden acceleration
   - Unexpected patterns

**Deliverable:** Complete Sheet 2 with growth rates for all growing resources

**Quality Check:**

- ✓ Growth rates calculated for all applicable resources
- ✓ Both absolute and percentage growth documented
- ✓ Growth drivers identified
- ✓ Anomalies flagged and explained

#### Phase 4: Capacity Exhaustion Forecasting (3-4 hours)

**Objective:** Complete Sheet 3 - Capacity Exhaustion Forecasts

**Steps:**
1. For each resource with positive growth:

   - Calculate "months until warning threshold"
   - Calculate "months until critical threshold"
   - Calculate "months until 100% exhaustion"
   - Forecast exhaustion date (calendar date)

2. Apply forecasting methodology:

   - **Linear forecast:** If growth is steady
   - **Exponential forecast:** If growth is accelerating
   - **Seasonal adjustment:** If seasonal patterns exist

3. Document forecast confidence:

   - **High confidence:** R² > 0.9, linear trend, 180+ days data
   - **Medium confidence:** R² 0.7-0.9, some variability
   - **Low confidence:** R² < 0.7, high variability, limited data

4. Prioritize by urgency:

   - **Critical (< 3 months):** Immediate action required
   - **High (3-6 months):** Planning required now
   - **Medium (6-12 months):** Include in budget cycle
   - **Low (> 12 months):** Monitor quarterly

**Deliverable:** Complete Sheet 3 with capacity exhaustion forecasts

**Quality Check:**

- ✓ Exhaustion dates calculated for all growing resources
- ✓ Forecast methodology documented
- ✓ Forecast confidence assessed
- ✓ Resources prioritized by urgency

#### Phase 5: Capacity Expansion Planning (4-6 hours)

**Objective:** Complete Sheet 4 - Capacity Expansion Plans

**Steps:**
1. For each resource approaching exhaustion:

   - Determine expansion approach (vertical scale, horizontal scale, optimization)
   - Calculate required capacity addition
   - Document expansion timeline (considering lead times)
   - Estimate costs (capital and operational)
   - Assign ownership
   - Set target completion date

2. Validate expansion plans:

   - Does expansion provide adequate headroom? (12-18 months recommended)
   - Is timeline realistic? (accounts for procurement, testing, deployment)
   - Is budget available?

3. Create expansion schedule:

   - Q1, Q2, Q3, Q4 expansions
   - Dependencies between expansions
   - Resource allocation

4. Document alternatives:

   - Option A, B, C for each expansion
   - Cost-benefit analysis
   - Recommended option

**Deliverable:** Complete Sheet 4 with capacity expansion plans

**Quality Check:**

- ✓ All at-risk resources have expansion plans
- ✓ Expansion sizing provides adequate headroom
- ✓ Timelines account for procurement lead times
- ✓ Costs estimated
- ✓ Owners assigned

#### Phase 6: Forecast Accuracy Validation (2-3 hours)

**Objective:** Complete Sheet 5 - Forecast Accuracy Validation

**Steps:**
1. Retrieve previous forecasts (if available):

   - Last quarter's A.8.6.2 assessment
   - Last year's capacity plan

2. For each previous forecast:

   - Document predicted utilization
   - Document actual utilization
   - Calculate forecast error (% difference)
   - Classify accuracy (within ±15% = accurate)

3. Analyze forecast errors:

   - Consistent over-forecasting? (wasteful capacity additions)
   - Consistent under-forecasting? (reactive capacity additions)
   - What caused errors? (business changes, new applications, etc.)

4. Improve forecasting:

   - Adjust methodology based on error analysis
   - Incorporate lessons learned
   - Document methodology changes

**Deliverable:** Complete Sheet 5 with forecast accuracy metrics

**Quality Check:**

- ✓ Previous forecasts compared to actuals
- ✓ Forecast errors calculated and analyzed
- ✓ Root causes of errors identified
- ✓ Methodology improvements documented

**Note:** If this is the **first** A.8.6.2 assessment, Sheet 5 will be empty. Document "Baseline - no previous forecasts available" and use this assessment to establish baseline for future validation.

#### Phase 7: Budget Planning (2-3 hours)

**Objective:** Complete Sheet 6 - Capacity Planning Budget

**Steps:**
1. Consolidate all planned expansions from Sheet 4
2. Categorize costs:

   - **Capital Expenditure (CapEx):** Hardware purchases, one-time costs
   - **Operational Expenditure (OpEx):** Cloud costs, licensing, ongoing

3. Create quarterly budget forecast:

   - Q1, Q2, Q3, Q4 expenditures
   - Cumulative annual spend

4. Document budget status:

   - Budget requested
   - Budget approved
   - Budget allocated
   - Budget spent

5. Flag budget gaps:

   - Required vs. available budget
   - Prioritization if budget constrained

**Deliverable:** Complete Sheet 6 with capacity planning budget

**Quality Check:**

- ✓ All expansion costs included
- ✓ CapEx vs. OpEx categorized
- ✓ Quarterly breakdown provided
- ✓ Budget status documented
- ✓ Gaps flagged

#### Phase 8: Evidence Registry (30-60 minutes)

**Objective:** Complete Sheet 7 - Evidence Registry

**Steps:**
1. List all evidence collected:

   - Trend charts and graphs
   - Growth rate calculations
   - Forecast models (Excel files, scripts)
   - Expansion plan documents
   - Budget approval emails
   - Vendor quotes

2. Organize by category
3. Document storage locations
4. Verify accessibility
5. Tag for audit readiness

**Deliverable:** Complete Sheet 7 with evidence register

**Quality Check:**

- ✓ All evidence listed
- ✓ Storage locations accessible
- ✓ Evidence is organized
- ✓ Audit-ready format

#### Phase 9: Review & Approval (2-3 hours)

**Objective:** Three-level approval process

**Steps:**
1. **Self-review** (completer)

   - Check completeness
   - Verify calculations (growth rates, forecasts)
   - Validate evidence quality
   - Run quality checklist
   
2. **Technical review** (capacity planning manager / infrastructure manager)

   - Review trend analysis
   - Validate growth rate calculations
   - Check forecast methodology
   - Verify expansion plans are realistic
   - Approve or request changes
   
3. **Management review** (CIO/IT Director + CFO/Finance)

   - Review capacity risks (imminent exhaustion)
   - Review expansion plans and budget requirements
   - Approve budget allocations
   - Set priorities if budget constrained
   - Final approval

**Deliverable:** Approved forecast ready for budget allocation and implementation

**Quality Check:**

- ✓ All sections complete
- ✓ All reviewers have approved
- ✓ Budget approved (or prioritization decisions made)
- ✓ Evidence is audit-ready

---

## Completing Each Sheet

This section provides detailed guidance for completing each sheet in the workbook.

### Sheet 1: Historical Trends

#### Purpose

Visualize and analyze capacity utilization trends over time to understand historical patterns and identify growth trajectories.

#### What to Document

For EACH resource from A.8.6.1:

- **Resource ID** and Name
- **Time Period Analyzed** (e.g., 90 days, 180 days, 12 months)
- **Trend Pattern** (Linear Growth, Exponential Growth, Seasonal, Stable, Declining)
- **Trend Line Equation** (y = mx + b for linear)
- **R² (Correlation Coefficient)** (measure of trend fit, 0.0-1.0)
- **Trend Confidence** (High/Medium/Low based on R²)
- **Observations** (notes on pattern, anomalies, inflection points)
- **Visualization** (chart showing utilization over time with trend line)

#### Common Mistakes to Avoid

❌ **Not enough data points** - 30 days is too short for reliable trends  
❌ **Ignoring seasonal patterns** - Month-end spikes appear as random noise  
❌ **Over-fitting** - Complex polynomial trends where linear would suffice  
❌ **Not accounting for capacity changes** - Infrastructure expansion mid-period skews trend  
❌ **Cherry-picking time periods** - Selecting periods that show desired trend  

#### How to Complete

**Step 1: Gather Historical Data**

From A.8.6.1 assessment:

- Minimum: 90 days (3 months) of utilization data
- Preferred: 180 days (6 months)
- Ideal: 365+ days (12+ months) for seasonal pattern detection

Data points needed:

- Date/time stamps
- Utilization percentage or absolute values
- Peak, average, or both (peak recommended for capacity planning)

**Step 2: Create Trend Visualization**

Using Excel or similar tool:
1. Create scatter plot or line chart
2. X-axis: Time (dates)
3. Y-axis: Utilization (% or absolute)
4. Add trend line:

   - Linear (most common for capacity planning)
   - Polynomial (if clear acceleration/deceleration)
   - Moving average (to smooth out noise)

5. Display R² value on chart
6. Format professionally (title, axis labels, legend)

**Step 3: Calculate Trend Statistics**

**For Linear Trends:**

- Slope (m): Rate of change per day/month
- Intercept (b): Starting point
- R²: Correlation coefficient (goodness of fit)

Excel formula: `=LINEST(utilization_range, time_range, TRUE, TRUE)`

**For Growth Rate:**

- Daily growth rate: Slope value
- Monthly growth rate: Slope × 30.4 days
- Annual growth rate: Slope × 365 days

**Step 4: Assess Trend Confidence**

| R² Value | Trend Confidence | Interpretation |
|----------|------------------|----------------|
| **0.90-1.00** | **High** | Strong linear relationship, reliable forecast |
| **0.70-0.89** | **Medium** | Moderate relationship, forecast with caution |
| **0.50-0.69** | **Low** | Weak relationship, high uncertainty |
| **< 0.50** | **Very Low** | No clear trend, do not forecast |

**Step 5: Document Pattern Type**

**Linear Growth:**

- Steady, constant rate of increase
- Example: Database growing 50 GB/month consistently
- Forecast method: Linear extrapolation

**Exponential Growth:**

- Accelerating increase
- Example: User count doubling every quarter
- Forecast method: Exponential model or compound growth rate

**Seasonal Pattern:**

- Regular peaks and valleys
- Example: Month-end processing spikes, holiday traffic
- Forecast method: Seasonal adjustment + trend

**Stable/Flat:**

- No significant change over time
- Example: Well-optimized application with stable user base
- Forecast method: None needed (but monitor for changes)

**Declining:**

- Decreasing utilization
- Example: Application being phased out, data archived
- Forecast method: None (capacity not at risk)

**Step 6: Document Observations**

Note anything interesting or unusual:

- Inflection points (where trend changed)
- Anomalies (sudden spikes or drops)
- Capacity expansions (step-up in available capacity)
- Application migrations
- Seasonal events
- Business events (product launches, marketing campaigns)

#### Real-World Examples

**Example 1: Database Storage - Strong Linear Growth**
| Attribute | Value |
|-------|-------|
| Resource ID | db-prod-01-data |
| Time Period | 180 days (Jan-Jun 2026) |
| Starting Utilization | 650 GB |
| Ending Utilization | 950 GB |
| Trend Pattern | Linear Growth |
| Trend Equation | y = 1.67x + 650 |
| Slope | 1.67 GB/day |
| R² | 0.94 |
| Trend Confidence | High |
| Monthly Growth Rate | 50 GB/month (1.67 × 30) |
| Annual Growth Rate | 600 GB/year (1.67 × 365) |
| Observations | Steady growth, no anomalies, high confidence for forecasting |

**Analysis:** Excellent candidate for forecasting. R² of 0.94 indicates strong linear relationship. Growth is predictable at ~50 GB/month.

**Example 2: Web Server CPU - Seasonal Pattern**
| Attribute | Value |
|-------|-------|
| Resource ID | web-prod-cluster |
| Time Period | 365 days |
| Trend Pattern | Linear Growth + Seasonal |
| Base Trend | y = 0.05x + 40 |
| R² (base trend) | 0.72 |
| Seasonal Pattern | Monthly spikes (month-end +15-20%) |
| Trend Confidence | Medium |
| Observations | Underlying linear growth (~0.05%/day = 1.5%/month) PLUS regular month-end processing spikes |

**Analysis:** Medium confidence due to seasonal noise. Need to use seasonal-adjusted forecasting or plan for peak capacity including seasonal spikes.

**Example 3: Development Environment - Stable**
| Attribute | Value |
|-------|-------|
| Resource ID | dev-environment-01 |
| Time Period | 180 days |
| Trend Pattern | Stable/Flat |
| Average Utilization | 45% |
| Std Deviation | 3% |
| R² (trend line) | 0.12 |
| Trend Confidence | Very Low (no trend) |
| Observations | Consistent ~45% utilization, minor fluctuations, no growth trend |

**Analysis:** No forecasting needed. Resource is stable and not at risk of exhaustion. Continue quarterly monitoring.

#### Evidence to Collect

- **Trend charts** (with trend lines and R² values)
- **Historical data exports** (CSV/Excel with dates and utilization)
- **Trend analysis calculations** (Excel formulas or scripts)
- **Pattern documentation** (explanations of seasonal patterns, anomalies)

### Sheet 2: Growth Rate Calculations

#### Purpose

Quantify the rate of capacity consumption to enable accurate forecasting and budgeting.

#### What to Document

For EACH growing resource:

- **Resource ID** and Name
- **Measurement Period** (days/months analyzed)
- **Absolute Growth Rate** (GB/month, users/month, %bandwidth/month)
- **Percentage Growth Rate** (%/month relative to total capacity)
- **Compound Monthly Growth Rate** (for exponential growth)
- **Annual Extrapolation** (projected 12-month growth)
- **Growth Drivers** (business reasons for growth)
- **Growth Confidence** (based on trend R²)

#### How to Complete

**Calculate Absolute Growth Rate:**

Growth Rate = (Ending Value - Starting Value) / Time Period

Example:

- Storage: 950 GB (end) - 650 GB (start) / 6 months = 50 GB/month
- Users: 12,500 (end) - 10,000 (start) / 12 months = 208 users/month

**Calculate Percentage Growth Rate:**

% Growth Rate = (Growth Rate / Total Capacity) × 100

Example:

- Storage: 50 GB/month / 2000 GB capacity = 2.5%/month
- Users: 208 users/month / 15,000 user limit = 1.4%/month

**Calculate Compound Monthly Growth Rate (CMGR):**

For exponential growth:
CMGR = (Ending Value / Starting Value)^(1/months) - 1

Example:

- Users doubled in 12 months: (20,000 / 10,000)^(1/12) - 1 = 5.9%/month

**Extrapolate Annual Growth:**

Annual Growth = Monthly Growth × 12

Example:

- Storage: 50 GB/month × 12 = 600 GB/year
- Users: 208 users/month × 12 = 2,500 users/year

#### Real-World Examples

**Example 1: SAN Storage - Predictable Linear Growth**
| Attribute | Value |
|-------|-------|
| Resource ID | vol-data-prod-db-01 |
| Measurement Period | 6 months |
| Starting Value | 650 GB |
| Ending Value | 950 GB |
| Absolute Growth Rate | 50 GB/month |
| Total Capacity | 2000 GB |
| Percentage Growth Rate | 2.5%/month |
| Annual Extrapolation | 600 GB/year |
| Growth Drivers | Database: new customer records, transaction history |
| Growth Confidence | High (R² = 0.94) |

## Common Pitfalls

### Pitfall 1: Forecasting Without Sufficient Data

**Mistake:** Attempting to forecast trends with less than 90 days of data

**Why It Happens:**

- Urgency to produce forecast
- Monitoring recently implemented
- "Good enough" mindset

**How to Avoid:**

- Require minimum 90 days data (policy)
- If unavailable, document as "Insufficient data - monitoring period TBD"
- Use business estimates as interim (but flag as low confidence)

**Impact of Not Fixing:**

- Inaccurate forecasts
- Over-provisioning or under-provisioning
- Budget waste or capacity incidents

### Pitfall 2: Ignoring Seasonal Patterns

**Mistake:** Using linear trend without accounting for regular seasonal spikes

**Example:**

- Month-end processing causes 20% CPU spike every month
- Forecast uses average utilization
- Result: Under-forecasting peak capacity needs

**How to Avoid:**

- Analyze 12+ months of data to identify seasonal patterns
- Use seasonal-adjusted forecasting
- Plan for peak capacity, not average

### Pitfall 3: Extrapolating Recent Anomalies

**Mistake:** Treating one-time events as ongoing trends

**Example:**

- Data migration caused temporary 200 GB growth in one month
- Forecast assumes 200 GB/month ongoing
- Result: Massive over-forecasting

**How to Avoid:**

- Identify and exclude one-time events from trend calculations
- Document anomalies separately
- Use underlying trend, not anomaly-distorted data

### Pitfall 4: Not Validating Forecast Accuracy

**Mistake:** Never comparing forecasts to actual outcomes

**Why It Happens:**

- "Set and forget" forecasting
- No accountability for accuracy
- No feedback loop

**How to Avoid:**

- Maintain forecast accuracy tracking (Sheet 5)
- Review quarterly: forecast vs. actual
- Adjust methodology based on errors


**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
