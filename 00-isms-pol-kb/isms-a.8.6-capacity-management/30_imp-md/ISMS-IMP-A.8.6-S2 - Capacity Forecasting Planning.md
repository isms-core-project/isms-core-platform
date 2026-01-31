# ISMS-IMP-A.8.6-S2
## Capacity Forecasting and Planning Implementation Guide

**Document ID**: ISMS-IMP-A.8.6-S2  
**Title**: Capacity Forecasting and Planning Implementation Guide  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Capacity Planning Manager / Infrastructure Manager  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Capacity Planning Team | Initial implementation guidance |

**Review Cycle**: Annual (or upon methodology changes)  
**Next Review Date**: [Approval Date + 12 months]  
**Approvers**: 
- Primary: Capacity Planning Manager / Infrastructure Manager
- Financial Review: Chief Financial Officer (CFO)
- Security Review: Chief Information Security Officer (CISO)
- Technical Review: IT Operations Manager

**Distribution**: Capacity planning team, IT management, finance, senior leadership  
**Related Documents**: ISMS-POL-A.8.6-S2 (Capacity Management Policy), ISMS-IMP-A.8.6-S1 (Monitoring Implementation)

---

## 1. Purpose and Scope

### 1.1 Implementation Guide Purpose

This document provides **step-by-step technical guidance** for implementing capacity forecasting and planning processes to satisfy requirements defined in ISMS-POL-A.8.6-S2 (Capacity Management Policy).

**Target Audience**: Capacity planning team, infrastructure managers, IT operations managers, financial planners

**Prerequisites**: 
- Capacity monitoring infrastructure operational (per ISMS-IMP-A.8.6-S1)
- Historical utilization data available (minimum 6 months, preferably 12-24 months)
- Capacity management policy approved (ISMS-POL-A.8.6-S2)
- Capacity planning team identified and trained

### 1.2 Implementation Scope

This guide covers implementation of:

1. **Historical Data Collection** - Gathering utilization data for trend analysis
2. **Trend Analysis Methodology** - Statistical methods for identifying growth patterns
3. **Capacity Forecasting** - Projecting future capacity requirements (6, 12, 24 months)
4. **Capacity Planning Process** - Structured planning cycles (monthly, quarterly, annual)
5. **Capacity Expansion Planning** - Determining when and how much capacity to add
6. **Forecast Accuracy Validation** - Measuring and improving forecast quality
7. **Capacity Reporting** - Monthly, quarterly, and annual capacity reports
8. **Assessment Tool** - Using the capacity forecasting assessment Excel generator

**Out of Scope**: Day-to-day capacity monitoring (covered in ISMS-IMP-A.8.6-S1)

### 1.3 Implementation Approach

**Phased Implementation**:
- **Phase 1** (Month 1): Establish historical data collection and basic trend analysis
- **Phase 2** (Months 2-3): Implement forecasting methodology and initial forecasts
- **Phase 3** (Months 3-6): Establish capacity planning cycles and reporting
- **Ongoing**: Continuous improvement of forecast accuracy

**Success Criteria**:
- Forecasts developed for all critical resources within 3 months
- Forecast accuracy within ±15% by month 6
- 90% of capacity expansions are proactive (planned) vs. reactive (emergency)
- Monthly capacity reports delivered on schedule

---

## 2. Historical Data Collection

### 2.1 Data Requirements

**Minimum Historical Data**:
- **Duration**: 6 months minimum, 12-24 months recommended
- **Granularity**: Daily or weekly aggregates (hourly for short-term trending)
- **Metrics**: All capacity metrics from ISMS-IMP-A.8.6-S1 (CPU, memory, disk, network, application)
- **Quality**: Complete data with minimal gaps (<5% missing data points)

**Data Sources**:
- Monitoring tool databases (Prometheus, Datadog, CloudWatch, etc.)
- Infrastructure management systems (VMware vCenter, AWS Cost Explorer)
- CMDB historical records
- Previous capacity assessment workbooks

### 2.2 Data Export Procedures

#### 2.2.1 Prometheus Data Export

**Query Historical Data** (PromQL):
```promql
# CPU utilization - 90 days of daily averages
avg_over_time(
  (100 - (avg(irate(node_cpu_seconds_total{mode="idle"}[5m])) * 100))
  [1d:1h]
)[90d:1d]

# Disk utilization - 90 days of daily averages
avg_over_time(
  (node_filesystem_avail_bytes{mountpoint="/"} / 
   node_filesystem_size_bytes{mountpoint="/"} * 100)
  [1d:1h]
)[90d:1d]
```

**Export to CSV**:
```bash
# Using Prometheus HTTP API
curl -G 'http://prometheus:9090/api/v1/query_range' \
  --data-urlencode 'query=avg_over_time((100-(avg(irate(node_cpu_seconds_total{mode="idle"}[5m]))*100))[1d:1h])[90d:1d]' \
  --data-urlencode 'start=2025-10-01T00:00:00Z' \
  --data-urlencode 'end=2026-01-01T00:00:00Z' \
  --data-urlencode 'step=1d' \
  | jq -r '.data.result[] | [.metric.instance, .values[][0], .values[][1]] | @csv' \
  > cpu_utilization_90d.csv
```

#### 2.2.2 Datadog Data Export

**Metrics Query** (Datadog API):
```python
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.metrics_api import MetricsApi
from datetime import datetime, timedelta

configuration = Configuration()
configuration.api_key['apiKeyAuth'] = 'YOUR_API_KEY'
configuration.api_key['appKeyAuth'] = 'YOUR_APP_KEY'

with ApiClient(configuration) as api_client:
    api_instance = MetricsApi(api_client)
    
    # Query CPU utilization for last 90 days
    from_time = int((datetime.now() - timedelta(days=90)).timestamp())
    to_time = int(datetime.now().timestamp())
    
    response = api_instance.query_metrics(
        from_time=from_time,
        to_time=to_time,
        query="avg:system.cpu.user{*} by {host}"
    )
    
    # Export to CSV
    import csv
    with open('cpu_utilization_90d.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Timestamp', 'Host', 'CPU_Utilization'])
        for series in response.series:
            host = series.scope
            for point in series.pointlist:
                timestamp, value = point
                writer.writerow([datetime.fromtimestamp(timestamp/1000), host, value])
```

#### 2.2.3 AWS CloudWatch Data Export

**Export Metrics** (AWS CLI):
```bash
# Get EC2 CPU utilization for last 90 days
aws cloudwatch get-metric-statistics \
  --namespace AWS/EC2 \
  --metric-name CPUUtilization \
  --dimensions Name=InstanceId,Value=i-1234567890abcdef0 \
  --statistics Average \
  --start-time 2025-10-01T00:00:00Z \
  --end-time 2026-01-01T00:00:00Z \
  --period 86400 \
  --output json \
  | jq -r '.Datapoints | sort_by(.Timestamp) | .[] | [.Timestamp, .Average] | @csv' \
  > cpu_utilization_90d.csv
```

**Python Boto3**:
```python
import boto3
import csv
from datetime import datetime, timedelta

cloudwatch = boto3.client('cloudwatch')

# Get CPU utilization for last 90 days
response = cloudwatch.get_metric_statistics(
    Namespace='AWS/EC2',
    MetricName='CPUUtilization',
    Dimensions=[{'Name': 'InstanceId', 'Value': 'i-1234567890abcdef0'}],
    StartTime=datetime.now() - timedelta(days=90),
    EndTime=datetime.now(),
    Period=86400,  # Daily aggregates
    Statistics=['Average', 'Maximum']
)

# Export to CSV
with open('cpu_utilization_90d.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Timestamp', 'Average', 'Maximum'])
    for datapoint in sorted(response['Datapoints'], key=lambda x: x['Timestamp']):
        writer.writerow([
            datapoint['Timestamp'].strftime('%Y-%m-%d'),
            datapoint['Average'],
            datapoint['Maximum']
        ])
```

### 2.3 Data Quality Validation

**Check for Data Completeness**:
```python
import pandas as pd

# Load historical data
df = pd.read_csv('cpu_utilization_90d.csv', parse_dates=['Timestamp'])
df = df.sort_values('Timestamp')

# Check for gaps
date_range = pd.date_range(start=df['Timestamp'].min(), end=df['Timestamp'].max(), freq='D')
missing_dates = date_range.difference(df['Timestamp'])

print(f"Total expected data points: {len(date_range)}")
print(f"Actual data points: {len(df)}")
print(f"Missing data points: {len(missing_dates)} ({len(missing_dates)/len(date_range)*100:.1f}%)")

if len(missing_dates) > 0:
    print(f"\nMissing dates: {missing_dates.tolist()[:10]}...")  # Show first 10
```

**Handle Missing Data**:
- **Interpolation**: Fill small gaps (<3 days) with linear interpolation
- **Forward Fill**: Carry forward last known value for short gaps
- **Exclude**: Exclude resources with >10% missing data from forecasting
- **Manual Collection**: Collect missing data manually if critical

```python
# Fill small gaps with interpolation
df['CPU_Utilization'] = df['CPU_Utilization'].interpolate(method='linear', limit=3)

# Fill remaining gaps with forward fill
df['CPU_Utilization'] = df['CPU_Utilization'].fillna(method='ffill')
```

---

## 3. Trend Analysis Methodology

### 3.1 Statistical Methods

#### 3.1.1 Linear Regression

**Purpose**: Identify linear growth trends and calculate growth rate

**Method**:
```python
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Load historical data
df = pd.read_csv('cpu_utilization_90d.csv', parse_dates=['Timestamp'])
df = df.sort_values('Timestamp')

# Prepare data for linear regression
df['Days'] = (df['Timestamp'] - df['Timestamp'].min()).dt.days
X = df[['Days']].values
y = df['CPU_Utilization'].values

# Fit linear regression model
model = LinearRegression()
model.fit(X, y)

# Calculate trend line
df['Trend'] = model.predict(X)

# Calculate growth rate (% per day)
growth_rate_per_day = model.coef_[0]
growth_rate_per_month = growth_rate_per_day * 30

print(f"Current utilization: {y[-1]:.1f}%")
print(f"Growth rate: {growth_rate_per_day:.3f}% per day")
print(f"Growth rate: {growth_rate_per_month:.2f}% per month")
print(f"R-squared: {model.score(X, y):.3f}")
```

**Interpretation**:
- **Positive growth rate**: Resource utilization increasing over time (capacity expansion likely needed)
- **Negative growth rate**: Resource utilization decreasing (potential for right-sizing)
- **R-squared > 0.7**: Strong linear trend (forecasting reliable)
- **R-squared < 0.3**: Weak linear trend (consider other methods or seasonal analysis)

#### 3.1.2 Exponential Growth

**Purpose**: Model resources growing exponentially (e.g., user base, data storage)

**Method**:
```python
import numpy as np
from scipy.optimize import curve_fit

# Exponential function: y = a * exp(b * x)
def exponential(x, a, b):
    return a * np.exp(b * x)

# Fit exponential curve
params, covariance = curve_fit(exponential, df['Days'].values, df['CPU_Utilization'].values)

# Calculate trend line
df['Trend_Exponential'] = exponential(df['Days'].values, *params)

# Calculate doubling time
doubling_time = np.log(2) / params[1]
print(f"Exponential growth rate: {params[1]:.5f} per day")
print(f"Doubling time: {doubling_time:.0f} days")
```

#### 3.1.3 Seasonal Decomposition

**Purpose**: Identify recurring patterns (daily, weekly, monthly, quarterly)

**Method**:
```python
from statsmodels.tsa.seasonal import seasonal_decompose

# Ensure data has consistent frequency
df = df.set_index('Timestamp')
df = df.asfreq('D')  # Daily frequency

# Decompose time series
decomposition = seasonal_decompose(df['CPU_Utilization'], model='additive', period=7)  # Weekly seasonality

# Extract components
trend = decomposition.trend
seasonal = decomposition.seasonal
residual = decomposition.resid

# Plot components
import matplotlib.pyplot as plt
fig, axes = plt.subplots(4, 1, figsize=(12, 10))
df['CPU_Utilization'].plot(ax=axes[0], title='Original')
trend.plot(ax=axes[1], title='Trend')
seasonal.plot(ax=axes[2], title='Seasonal')
residual.plot(ax=axes[3], title='Residual')
plt.tight_layout()
plt.savefig('seasonal_decomposition.png')
```

**Seasonal Patterns to Look For**:
- **Daily**: Business hours vs. overnight (batch processing)
- **Weekly**: Weekday vs. weekend patterns
- **Monthly**: Month-end processing, billing cycles
- **Quarterly**: Quarter-end reporting, financial close
- **Annual**: Holiday seasons, fiscal year-end

### 3.2 Growth Rate Calculation

**Simple Growth Rate** (linear):
```
Growth Rate (%) = ((Latest Value - Oldest Value) / Oldest Value) / Number of Periods * 100
```

Example:
```
90 days ago: 45% utilization
Today: 72% utilization
Growth Rate = ((72 - 45) / 45) / 3 months * 100 = 20% per month
```

**Compound Annual Growth Rate (CAGR)**:
```
CAGR = ((Ending Value / Beginning Value) ^ (1 / Number of Years)) - 1
```

**Python Implementation**:
```python
def calculate_growth_rate(df, column, period_days=30):
    """
    Calculate growth rate over specified period.
    
    Args:
        df: DataFrame with historical data
        column: Column name to analyze
        period_days: Period for growth rate calculation (default 30 days)
    
    Returns:
        float: Growth rate as percentage per period
    """
    latest = df[column].iloc[-1]
    oldest = df[column].iloc[0]
    num_periods = len(df) / period_days
    
    if oldest == 0:
        return None  # Avoid division by zero
    
    growth_rate = ((latest - oldest) / oldest) / num_periods * 100
    return growth_rate

# Calculate monthly growth rate
monthly_growth = calculate_growth_rate(df, 'CPU_Utilization', period_days=30)
print(f"Monthly growth rate: {monthly_growth:.2f}%")
```

### 3.3 Anomaly Detection and Filtering

**Purpose**: Remove one-time events that distort trend analysis

**Common Anomalies**:
- **Spikes**: One-time events (batch job failure, security incident, data migration)
- **Drops**: Planned maintenance, system outages, data collection gaps
- **Step Changes**: Application deployments, infrastructure changes

**Statistical Anomaly Detection** (Z-score method):
```python
from scipy import stats

# Calculate Z-scores
z_scores = stats.zscore(df['CPU_Utilization'])

# Identify outliers (|Z| > 3)
outliers = np.abs(z_scores) > 3

print(f"Outliers detected: {outliers.sum()} ({outliers.sum()/len(df)*100:.1f}%)")
print(f"Outlier dates: {df[outliers]['Timestamp'].tolist()}")

# Option 1: Remove outliers
df_clean = df[~outliers]

# Option 2: Replace outliers with median
df['CPU_Utilization_Clean'] = df['CPU_Utilization'].copy()
df.loc[outliers, 'CPU_Utilization_Clean'] = df['CPU_Utilization'].median()
```

**Manual Review**: Always manually review detected anomalies before removal
- Verify anomaly is truly one-time event
- Document reason for exclusion
- Consider if anomaly represents future normal behavior (e.g., new workload pattern)

---

## 4. Capacity Forecasting

### 4.1 Forecasting Methodology

#### 4.1.1 Linear Forecast (Trend-Based)

**Use When**: Growth is relatively steady, R-squared > 0.5

**Method**:
```python
def forecast_linear(df, days_ahead=180):
    """
    Generate linear forecast based on historical trend.
    
    Args:
        df: DataFrame with historical data and 'Days' column
        days_ahead: Number of days to forecast (default 180 = 6 months)
    
    Returns:
        DataFrame: Forecast with dates and predicted values
    """
    from sklearn.linear_model import LinearRegression
    
    # Fit model on historical data
    X = df[['Days']].values
    y = df['CPU_Utilization'].values
    model = LinearRegression()
    model.fit(X, y)
    
    # Generate future dates
    last_day = df['Days'].max()
    future_days = np.arange(last_day + 1, last_day + days_ahead + 1)
    
    # Predict
    predictions = model.predict(future_days.reshape(-1, 1))
    
    # Create forecast DataFrame
    last_date = df['Timestamp'].max()
    future_dates = pd.date_range(start=last_date + pd.Timedelta(days=1), periods=days_ahead, freq='D')
    
    forecast_df = pd.DataFrame({
        'Date': future_dates,
        'Forecasted_Utilization': predictions,
        'Growth_Rate_Per_Day': model.coef_[0]
    })
    
    return forecast_df

# Generate 6-month forecast
forecast_6m = forecast_linear(df, days_ahead=180)
print(forecast_6m.head())
```

#### 4.1.2 Excel-Based Forecasting (FORECAST.LINEAR)

**For Non-Technical Users**:
```
# In Excel:
# Column A: Historical dates
# Column B: Historical utilization
# Column C: Future dates (extend beyond last historical date)
# Column D: Forecast formula

=FORECAST.LINEAR(C2, $B$2:$B$100, $A$2:$A$100)
```

**Forecast Growth with TREND**:
```
=TREND($B$2:$B$100, $A$2:$A$100, C2)
```

#### 4.1.3 Seasonal Forecast (with Seasonality)

**Use When**: Clear seasonal patterns identified

**Method** (Prophet library):
```python
from prophet import Prophet

# Prepare data for Prophet (requires 'ds' and 'y' columns)
prophet_df = df[['Timestamp', 'CPU_Utilization']].copy()
prophet_df.columns = ['ds', 'y']

# Create and fit model
model = Prophet(
    daily_seasonality=False,
    weekly_seasonality=True,
    yearly_seasonality=True
)
model.fit(prophet_df)

# Generate future dataframe
future = model.make_future_dataframe(periods=180)  # 180 days ahead

# Predict
forecast = model.predict(future)

# Extract forecast components
forecast_6m = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(180)
forecast_6m.columns = ['Date', 'Forecast', 'Lower_Bound', 'Upper_Bound']
print(forecast_6m.head())
```

### 4.2 Forecasting Horizons

**Short-Term Forecast (3-6 months)**:
- **Purpose**: Tactical capacity planning, immediate procurement decisions
- **Update Frequency**: Monthly
- **Confidence**: High (historical patterns likely to continue)
- **Use**: Trigger capacity expansions, budget approvals

**Medium-Term Forecast (12 months)**:
- **Purpose**: Annual budget planning, strategic capacity investments
- **Update Frequency**: Quarterly
- **Confidence**: Medium (business changes may impact)
- **Use**: Annual capacity budget, procurement planning

**Long-Term Forecast (24-36 months)**:
- **Purpose**: Strategic planning, datacenter expansion, major platform changes
- **Update Frequency**: Annually
- **Confidence**: Low (high uncertainty over long periods)
- **Use**: Long-term strategy, datacenter planning, technology refresh

### 4.3 Incorporating Business Growth Assumptions

**Adjust Forecasts for Known Business Changes**:

```python
def adjust_forecast_for_growth(forecast_df, business_growth_rate):
    """
    Adjust technical forecast with business growth assumptions.
    
    Args:
        forecast_df: DataFrame with forecasted utilization
        business_growth_rate: Expected business growth rate (e.g., 0.15 for 15% growth)
    
    Returns:
        DataFrame: Adjusted forecast
    """
    # Apply business growth multiplier
    forecast_df['Adjusted_Forecast'] = forecast_df['Forecasted_Utilization'] * (1 + business_growth_rate)
    
    return forecast_df

# Example: Company expects 20% user growth
forecast_6m = adjust_forecast_for_growth(forecast_6m, business_growth_rate=0.20)
```

**Document Business Assumptions**:
- User growth projections (new customers, market expansion)
- New product launches (additional workload, traffic)
- Seasonal events (holiday season for retail, tax season for financial services)
- Marketing campaigns (expected traffic spikes)
- Acquisitions or divestitures (workload changes)

---

## 5. Capacity Exhaustion Projection

### 5.1 Calculate Capacity Exhaustion Date

**Method**:
```python
def calculate_exhaustion_date(current_util, growth_rate_per_month, threshold=85):
    """
    Calculate when capacity will reach threshold.
    
    Args:
        current_util: Current utilization percentage
        growth_rate_per_month: Growth rate (percentage points per month)
        threshold: Capacity threshold (default 85%)
    
    Returns:
        float: Months until exhaustion (None if no exhaustion projected)
    """
    if growth_rate_per_month <= 0:
        return None  # No exhaustion if not growing
    
    headroom = threshold - current_util
    if headroom <= 0:
        return 0  # Already at/above threshold
    
    months_until_exhaustion = headroom / growth_rate_per_month
    return months_until_exhaustion

# Example
current_cpu = 68  # 68% current utilization
growth = 3.5  # 3.5% growth per month
months = calculate_exhaustion_date(current_cpu, growth, threshold=85)
print(f"Months until 85% threshold: {months:.1f} months")

# Calculate exhaustion date
from datetime import datetime, timedelta
exhaustion_date = datetime.now() + timedelta(days=months*30)
print(f"Projected exhaustion date: {exhaustion_date.strftime('%Y-%m-%d')}")
```

### 5.2 Urgency Classification

**Classify Resources by Time to Exhaustion**:

| Urgency | Time to Exhaustion | Action Required |
|---------|-------------------|-----------------|
| **Immediate** | 0-3 months | Urgent capacity expansion, emergency procurement |
| **Short-Term** | 3-6 months | Begin capacity planning now, include in current quarter |
| **Medium-Term** | 6-12 months | Include in quarterly/annual planning |
| **Long-Term** | >12 months | Monitor in strategic planning |
| **No Risk** | Not projected to exhaust | Continue monitoring |

```python
def classify_urgency(months_to_exhaustion):
    """Classify capacity urgency based on time to exhaustion."""
    if months_to_exhaustion is None:
        return "No Risk"
    elif months_to_exhaustion <= 0:
        return "CRITICAL - Already Exceeded"
    elif months_to_exhaustion <= 3:
        return "Immediate (0-3 months)"
    elif months_to_exhaustion <= 6:
        return "Short-Term (3-6 months)"
    elif months_to_exhaustion <= 12:
        return "Medium-Term (6-12 months)"
    else:
        return "Long-Term (>12 months)"

urgency = classify_urgency(months)
print(f"Urgency classification: {urgency}")
```

---

## 6. Capacity Planning Process

### 6.1 Monthly Capacity Review

**Attendees**: Capacity planning team, infrastructure team leads

**Agenda** (1-2 hours):
1. Review current utilization status (Assessment 1 data)
2. Review resources at warning/critical thresholds
3. Review short-term forecasts (3-6 months)
4. Identify resources requiring immediate action
5. Update capacity expansion tracker
6. Assign action items

**Outputs**:
- Updated capacity status report
- List of resources requiring expansion (with timelines)
- Action items with ownership

**Meeting Template**:
```
MONTHLY CAPACITY REVIEW - [Month Year]

1. UTILIZATION STATUS
   - Total resources monitored: [X]
   - Resources at OK status: [Y] ([%])
   - Resources at Warning: [Z] ([%])
   - Resources at Critical: [W] ([%])
   - Capacity health score: [Score]%

2. RESOURCES REQUIRING ACTION
   [Resource Name] | Current: [X]% | Forecast (3mo): [Y]% | Action: [Expand/Optimize]
   
3. CAPACITY EXPANSIONS IN PROGRESS
   [Resource] | Expansion Amount | Target Date | Status | Owner
   
4. FORECAST UPDATES
   - Key forecast changes since last review
   - Business assumptions updated
   
5. ACTION ITEMS
   [Action] | Owner | Due Date | Status
```

### 6.2 Quarterly Capacity Planning

**Attendees**: Capacity planning team, infrastructure managers, IT operations, IT Director

**Agenda** (Half-day workshop):
1. Comprehensive forecast review (12-month outlook)
2. Capacity expansion planning (next quarter)
3. Budget impact analysis
4. Risk assessment (capacity risks)
5. Forecast accuracy validation (previous quarter)
6. Process improvements

**Outputs**:
- Quarterly capacity forecast report
- Capacity expansion plan for next 12 months
- Budget request for capacity expansions
- Capacity management dashboard

**Quarterly Planning Timeline**:
```
Week 1: Data collection and analysis
  - Export historical data
  - Update trend analysis
  - Generate forecasts

Week 2: Forecast review and validation
  - Review forecasts with infrastructure teams
  - Validate business assumptions
  - Calculate capacity exhaustion dates

Week 3: Capacity planning workshop
  - Identify expansion requirements
  - Develop expansion plans
  - Calculate budget impact

Week 4: Report generation and approval
  - Generate quarterly capacity report
  - Present to IT leadership
  - Obtain budget approvals
```

### 6.3 Annual Capacity Planning

**Attendees**: IT leadership (CIO, CISO, IT Director), finance (CFO, controller), executive management, capacity planning team

**Agenda** (Full-day or multi-day session):
1. Long-term capacity forecast (24-36 months)
2. Strategic capacity investments (datacenter, major platforms)
3. Multi-year budget planning
4. Technology refresh planning
5. Cloud migration capacity planning
6. Business growth alignment
7. Capacity management maturity assessment

**Outputs**:
- Annual strategic capacity plan
- Multi-year capacity budget (CapEx and OpEx)
- Datacenter capacity roadmap
- Technology refresh schedule
- Executive presentation

**Annual Planning Process**:
```
Month 1 (August): Initial forecasting
  - Gather business growth projections
  - Develop 24-month capacity forecasts
  - Identify strategic capacity needs

Month 2 (September): Planning workshop
  - Full-day planning session
  - Scenario planning (best case, worst case, most likely)
  - Technology options evaluation
  - Multi-year budget development

Month 3 (October): Executive approval
  - Executive presentation
  - Board-level briefing (if required)
  - Budget approval
  - Strategic plan finalization
```

---

## 7. Capacity Expansion Planning

### 7.1 Expansion Trigger Points

**When to Plan Capacity Expansion**:

1. **Forecast-Driven**: Forecast projects threshold breach within lead time window
2. **Threshold-Driven**: Resource currently at warning threshold
3. **Business-Driven**: Planned business initiative requires additional capacity
4. **SLA-Driven**: Required to meet contractual service level agreements

**Lead Time Consideration**:
```python
def calculate_expansion_trigger_date(exhaustion_date, lead_time_days):
    """
    Calculate when to trigger capacity expansion based on lead time.
    
    Args:
        exhaustion_date: Projected capacity exhaustion date
        lead_time_days: Lead time required for capacity expansion
    
    Returns:
        datetime: Date to trigger expansion
    """
    trigger_date = exhaustion_date - timedelta(days=lead_time_days)
    return trigger_date

# Example
exhaustion = datetime(2026, 8, 15)
lead_time = 90  # 90 days for physical server procurement

trigger = calculate_expansion_trigger_date(exhaustion, lead_time)
print(f"Expansion trigger date: {trigger.strftime('%Y-%m-%d')}")
print(f"Action required in: {(trigger - datetime.now()).days} days")
```

### 7.2 Expansion Sizing

**Determine How Much Capacity to Add**:

**Minimum Expansion**: Sufficient to avoid exhaustion for one planning cycle
```
Minimum Expansion = (Growth Rate per Month × Planning Cycle Months) + Safety Buffer
```

**Recommended Expansion**: Sufficient for 12-18 months
```
Recommended Expansion = (Growth Rate per Month × 12-18 months)
```

**Example**:
```
Current: 70% CPU utilization
Growth Rate: 2.5% per month
Planning Cycle: 3 months (quarterly)

Minimum Expansion = 2.5% × 3 + 5% buffer = 12.5% additional capacity
Recommended Expansion = 2.5% × 12 = 30% additional capacity
```

**Practical Sizing Constraints**:
- **Physical Infrastructure**: Add in increments (servers, racks)
  - Can't add 12.5% of a server → Round up to whole servers
  - Consider cluster balancing (add even number for load distribution)
  
- **Cloud Infrastructure**: Can scale precisely
  - Add exact capacity needed
  - Consider reserved instance blocks for cost optimization

### 7.3 Expansion Options Evaluation

**Compare Expansion Alternatives**:

| Option | Capacity Added | Cost | Lead Time | Pros | Cons |
|--------|---------------|------|-----------|------|------|
| **Cloud Scale-Up** | +30% | $500/month | 1 hour | Fast, flexible | Ongoing OpEx |
| **Physical Servers** | +50% | $15,000 (CapEx) | 6 weeks | Cost-effective long-term | Long lead time |
| **Optimization** | +15% (reclaimed) | $0 | 2 weeks | No cost | Limited capacity |
| **Hybrid** | +30% (cloud) +20% (physical) | $300/mo + $10K | 6 weeks | Balanced | Complex management |

**Decision Criteria**:
- **Urgency**: How soon is capacity needed?
- **Duration**: Is this temporary or permanent need?
- **Cost**: CapEx vs. OpEx, 3-year TCO
- **Scalability**: Future growth expectations
- **Risk**: Capacity risk vs. cost risk

### 7.4 Budget Impact Analysis

**Calculate Total Cost of Ownership (3 years)**:

```python
def calculate_tco(capex, opex_per_month, years=3):
    """
    Calculate 3-year total cost of ownership.
    
    Args:
        capex: Capital expenditure (one-time)
        opex_per_month: Operating expenditure per month
        years: Period for TCO calculation (default 3)
    
    Returns:
        float: Total cost of ownership
    """
    total_opex = opex_per_month * 12 * years
    tco = capex + total_opex
    return tco

# Example: Compare cloud vs. on-premises
cloud_tco = calculate_tco(capex=0, opex_per_month=500, years=3)
onprem_tco = calculate_tco(capex=15000, opex_per_month=100, years=3)  # Maintenance, power

print(f"Cloud 3-year TCO: ${cloud_tco:,.0f}")
print(f"On-premises 3-year TCO: ${onprem_tco:,.0f}")
print(f"Difference: ${cloud_tco - onprem_tco:,.0f}")
```

**Budget Request Template**:
```
CAPACITY EXPANSION REQUEST

Resource: [Name]
Current Capacity: [X GB/cores/users]
Current Utilization: [Y%]
Projected Exhaustion: [Date] (in [Z] months)

Expansion Option: [Selected Option]
Capacity to Add: [Amount]
New Total Capacity: [New Total]
Headroom After Expansion: [Months of capacity]

COST ANALYSIS
  Capital Expenditure (CapEx): $[Amount]
  Operating Expenditure (OpEx): $[Amount]/month
  3-Year Total Cost: $[Amount]
  
PROCUREMENT
  Vendor: [Name]
  Lead Time: [Weeks]
  Target Deployment Date: [Date]
  
APPROVALS REQUIRED
  [ ] IT Operations Manager (<$25K)
  [ ] IT Director/CIO ($25K-$100K)
  [ ] CFO + Executive Management (>$100K)
```

---

## 8. Forecast Accuracy Validation

### 8.1 Accuracy Measurement

**Compare Previous Forecasts to Actual**:

```python
def calculate_forecast_accuracy(forecast, actual):
    """
    Calculate forecast accuracy metrics.
    
    Args:
        forecast: Forecasted values (list or array)
        actual: Actual observed values (list or array)
    
    Returns:
        dict: Accuracy metrics (MAPE, MAE, RMSE, Bias)
    """
    forecast = np.array(forecast)
    actual = np.array(actual)
    
    # Mean Absolute Percentage Error
    mape = np.mean(np.abs((actual - forecast) / actual)) * 100
    
    # Mean Absolute Error
    mae = np.mean(np.abs(actual - forecast))
    
    # Root Mean Squared Error
    rmse = np.sqrt(np.mean((actual - forecast) ** 2))
    
    # Bias (average forecast error)
    bias = np.mean(forecast - actual)
    
    return {
        'MAPE': mape,
        'MAE': mae,
        'RMSE': rmse,
        'Bias': bias,
        'Bias_Direction': 'Over-forecasting' if bias > 0 else 'Under-forecasting'
    }

# Example: Validate 3-month-old forecast
forecast_3m_ago = [55, 58, 61, 64]  # Forecasted for months 1-4
actual_observed = [52, 57, 59, 62]  # Actual values for months 1-4

accuracy = calculate_forecast_accuracy(forecast_3m_ago, actual_observed)
print(f"MAPE: {accuracy['MAPE']:.1f}%")
print(f"Bias: {accuracy['Bias']:.1f}% ({accuracy['Bias_Direction']})")
```

**Accuracy Targets** (per ISMS-POL-A.8.6-S2):
- **Excellent**: MAPE ≤ 5%
- **Good**: MAPE ≤ 10%
- **Acceptable**: MAPE ≤ 15%
- **Poor**: MAPE > 15% (requires methodology review)

### 8.2 Continuous Improvement

**When Forecast Accuracy is Poor**:

1. **Review Methodology**: Is linear regression appropriate? Consider seasonal or exponential models
2. **Check Data Quality**: Are there data collection gaps or anomalies?
3. **Update Business Assumptions**: Have business conditions changed significantly?
4. **Shorten Horizon**: Reduce forecast horizon if long-term forecasts are unreliable
5. **Increase Granularity**: Forecast by application/workload instead of aggregate

**Forecast Tuning**:
```python
def tune_forecast_with_actual(forecast_df, actual_value, forecast_date):
    """
    Adjust forecast based on actual observed value.
    
    Args:
        forecast_df: DataFrame with forecast
        actual_value: Actual observed value
        forecast_date: Date of actual observation
    
    Returns:
        DataFrame: Adjusted forecast
    """
    # Calculate forecast error
    forecast_for_date = forecast_df[forecast_df['Date'] == forecast_date]['Forecasted_Utilization'].values[0]
    error = actual_value - forecast_for_date
    
    # Adjust future forecasts by error amount (simple adjustment)
    forecast_df.loc[forecast_df['Date'] > forecast_date, 'Forecasted_Utilization'] += error
    
    return forecast_df
```

---

## 9. Capacity Reporting

### 9.1 Monthly Capacity Report

**Template**:
```
MONTHLY CAPACITY REPORT
[Month Year]

EXECUTIVE SUMMARY
- Capacity Health Score: [X]% ([Y] of [Z] resources at OK status)
- Resources Requiring Action: [N] resources at warning/critical thresholds
- Capacity Expansions Completed: [N] expansions deployed this month
- Capacity Incidents: [N] capacity-related incidents

UTILIZATION STATUS
Resource Category | Total | OK | Warning | Critical | Not Monitored
Compute          |  [X]  | [Y]|   [Z]   |   [W]    |     [V]
Storage          |  [X]  | [Y]|   [Z]   |   [W]    |     [V]
Network          |  [X]  | [Y]|   [Z]   |   [W]    |     [V]
Application      |  [X]  | [Y]|   [Z]   |   [W]    |     [V]
Cloud            |  [X]  | [Y]|   [Z]   |   [W]    |     [V]

TOP CAPACITY CONCERNS (Resources at Warning/Critical)
1. [Resource Name] - [Current Util]% - Action: [Plan]
2. [Resource Name] - [Current Util]% - Action: [Plan]
...

FORECAST HIGHLIGHTS
- [Resource] projected to reach 85% in [X] months
- [Resource] growth accelerating ([Rate]% per month)

CAPACITY ACTIONS COMPLETED
- [Action] completed on [Date]

NEXT MONTH PLANNED ACTIONS
- [Action] scheduled for [Date]

APPENDIX
- Detailed utilization data (Assessment 1 workbook)
- Evidence register
```

### 9.2 Quarterly Capacity Planning Report

**Template**:
```
QUARTERLY CAPACITY PLANNING REPORT
[Quarter Year]

EXECUTIVE SUMMARY
- 12-Month Capacity Forecast: [Summary of key findings]
- Projected Capacity Exhaustion: [X] resources within 12 months
- Recommended Capacity Expansions: [Y] expansions, Total Cost: $[Z]
- Forecast Accuracy: [MAPE]% (vs. target ≤15%)

12-MONTH CAPACITY FORECAST
Resource Category | Current | 6-Month Forecast | 12-Month Forecast | Exhaustion Risk
Compute          |   [X]%  |      [Y]%       |       [Z]%       |   [N] resources
Storage          |   [X]%  |      [Y]%       |       [Z]%       |   [N] resources
Network          |   [X]%  |      [Y]%       |       [Z]%       |   [N] resources

CAPACITY EXPANSION PLAN (Next 12 Months)
Resource | Expansion Amount | Target Quarter | Estimated Cost | Approval Status
[Name]   |     [Amount]     |     [Q1]      |    $[Cost]    |   [Approved]
[Name]   |     [Amount]     |     [Q2]      |    $[Cost]    |   [Pending]

BUDGET IMPACT
  Q1: $[Amount]
  Q2: $[Amount]
  Q3: $[Amount]
  Q4: $[Amount]
  Total: $[Amount]

FORECAST ACCURACY VALIDATION
- Previous Quarter Forecast vs. Actual
- MAPE: [X]%
- Bias: [Over/Under-forecasting by Y%]
- Improvement Actions: [List]

CAPACITY OPTIMIZATION
- Right-sizing candidates: [N] resources
- Potential savings: $[Amount]/month

RISKS AND MITIGATION
- [Risk description] - Mitigation: [Plan]

RECOMMENDATIONS
1. [Recommendation]
2. [Recommendation]
```

### 9.3 Annual Strategic Capacity Plan

**Template**:
```
ANNUAL STRATEGIC CAPACITY PLAN
[Fiscal Year]

EXECUTIVE SUMMARY
- 24-Month Capacity Outlook: [Summary]
- Strategic Capacity Investments: $[Total Budget]
- Major Initiatives: [Cloud migration, Datacenter expansion, etc.]
- Business Enablement: Capacity to support [X]% business growth

LONG-TERM CAPACITY FORECAST (24 Months)
[Charts and graphs showing capacity trends]

STRATEGIC CAPACITY INITIATIVES
Initiative             | Timeline | Investment | Business Impact
Cloud Migration        | [Dates] | $[Amount] | [Impact]
Datacenter Expansion   | [Dates] | $[Amount] | [Impact]
Technology Refresh     | [Dates] | $[Amount] | [Impact]

MULTI-YEAR BUDGET
              Year 1    | Year 2    | Total
CapEx        $[Amount] | $[Amount] | $[Amount]
OpEx         $[Amount] | $[Amount] | $[Amount]
Total        $[Amount] | $[Amount] | $[Amount]

CAPACITY MANAGEMENT MATURITY
Current Maturity Level: [Level 1-5]
Target Maturity Level: [Level]
Improvement Roadmap: [Summary]

RISK ASSESSMENT
Strategic Risk | Impact | Probability | Mitigation
[Risk]         | [High] | [Medium]    | [Plan]

EXECUTIVE RECOMMENDATIONS
1. [Recommendation for board/executive approval]
2. [Recommendation]
```

---

## 10. Assessment Tool Usage

### 10.1 Capacity Forecasting Assessment Workbook

**Purpose**: Document capacity forecasts, track expansion planning, validate forecast accuracy

**Generation**: Use Python script `generate_assessment_2_capacity_forecasts.py`

```bash
# Generate assessment workbook
python3 generate_assessment_2_capacity_forecasts.py

# Output: ISMS-IMP-A.8.6.2_Capacity_Forecasts_Planning_Assessment_YYYYMMDD.xlsx
```

### 10.2 Workbook Completion Process

**Step 1: Generate Workbook**
- Run Python script to create blank assessment workbook
- Workbook contains 10 sheets for forecasting and planning

**Step 2: Populate Historical Data**
- Export historical utilization data from monitoring tools
- Import into Historical_Utilization sheet
- Ensure data quality (complete, accurate, recent)

**Step 3: Perform Trend Analysis**
- Calculate growth rates (manually or using Excel formulas)
- Identify seasonal patterns
- Document trend analysis methodology

**Step 4: Develop Forecasts**
- Use Excel FORECAST.LINEAR or trend analysis results
- Project 6-month and 12-month capacity forecasts
- Document assumptions

**Step 5: Calculate Capacity Exhaustion**
- Determine when resources will reach thresholds
- Classify urgency (immediate, short-term, medium-term)

**Step 6: Plan Capacity Expansions**
- Identify resources requiring expansion
- Determine expansion sizing
- Calculate budget impact
- Document planned expansion dates

**Step 7: Validate Previous Forecasts**
- Compare forecasts made 3-6 months ago to actual utilization
- Calculate forecast accuracy (MAPE)
- Document lessons learned

**Step 8: Review and Approval**
- Capacity planning team reviews completeness
- IT Director and CFO approve budget impact
- Save final version with date stamp

---

## 11. Implementation Checklist

### 11.1 Pre-Implementation

- [ ] Capacity monitoring operational (ISMS-IMP-A.8.6-S1 complete)
- [ ] Historical utilization data available (6+ months)
- [ ] Capacity planning team identified and trained
- [ ] Forecasting tools selected (Excel, Python, or monitoring tool built-in)
- [ ] Capacity management policy approved (ISMS-POL-A.8.6-S2)

### 11.2 Forecasting Setup

- [ ] Historical data export procedures documented
- [ ] Data quality validation process established
- [ ] Trend analysis methodology selected and documented
- [ ] Forecast templates created (Excel or scripts)
- [ ] Business growth assumptions documented

### 11.3 Planning Process

- [ ] Monthly capacity review meetings scheduled
- [ ] Quarterly capacity planning workshops scheduled
- [ ] Annual capacity planning timeline defined
- [ ] Capacity expansion approval process documented
- [ ] Budget templates created

### 11.4 Reporting

- [ ] Monthly capacity report template created
- [ ] Quarterly capacity planning report template created
- [ ] Annual strategic capacity plan template created
- [ ] Report distribution list defined
- [ ] Executive dashboard configured

### 11.5 Validation and Improvement

- [ ] Forecast accuracy tracking implemented
- [ ] Continuous improvement process defined
- [ ] Lessons learned captured quarterly
- [ ] Forecasting methodology reviewed annually

---

## Appendix A: Forecasting Tools Comparison

| Tool | Complexity | Cost | Use Case | Pros | Cons |
|------|-----------|------|----------|------|------|
| **Excel** | Low | Free | Small-scale, manual forecasting | Easy to use, widely available | Manual, limited scalability |
| **Python (Pandas, Scikit-learn)** | Medium | Free | Medium to large scale, automated | Powerful, flexible, scalable | Requires programming skills |
| **Python (Prophet)** | Medium | Free | Seasonal forecasting | Handles seasonality well | Learning curve |
| **Monitoring Tool Built-in** | Low | Included | Integrated forecasting | Convenient, integrated | Limited customization |
| **Dedicated Capacity Tools** | High | $$$$ | Enterprise-scale | Comprehensive, automated | Expensive, complex |

---

## Appendix B: Forecast Accuracy Formulas

**Mean Absolute Percentage Error (MAPE)**:
```
MAPE = (1/n) × Σ|((Actual - Forecast) / Actual)| × 100%
```

**Mean Absolute Error (MAE)**:
```
MAE = (1/n) × Σ|Actual - Forecast|
```

**Root Mean Squared Error (RMSE)**:
```
RMSE = √((1/n) × Σ(Actual - Forecast)²)
```

**Forecast Bias**:
```
Bias = (1/n) × Σ(Forecast - Actual)
```

---

**End of Document ISMS-IMP-A.8.6-S2**

---

**Document Status**: DRAFT - Pending Approval  
**Next Steps**: 
1. Review by capacity planning team and finance
2. Approval by Infrastructure Manager, CFO, CISO
3. Training on forecasting methodology
4. Initial forecast development for critical resources
5. Establish capacity planning cycles
6. First quarterly capacity planning workshop
