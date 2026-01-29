# ISMS-IMP-A.8.6-S3
## Capacity Management Assessment Methodology Implementation Guide

**Document ID**: ISMS-IMP-A.8.6-S3  
**Title**: Capacity Management Assessment Methodology Implementation Guide  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Internal Audit / Capacity Planning Manager  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Internal Audit / Capacity Planning Team | Initial implementation guidance |

**Review Cycle**: Annual (or upon assessment methodology changes)  
**Next Review Date**: [Approval Date + 12 months]  
**Approvers**: 
- Primary: Internal Audit Manager
- Technical Review: Capacity Planning Manager
- Security Review: Chief Information Security Officer (CISO)
- Management Review: IT Director / CIO

**Distribution**: Internal audit, capacity planning team, IT management, external auditors  
**Related Documents**: ISMS-POL-A.8.6-S3 (Assessment Framework), ISMS-IMP-A.8.6-S1 (Monitoring), ISMS-IMP-A.8.6-S2 (Forecasting)

---

## 1. Purpose and Scope

### 1.1 Implementation Guide Purpose

This document provides **step-by-step guidance** for conducting capacity management assessments to verify compliance with ISMS-POL-A.8.6 and demonstrate effective implementation of ISO/IEC 27001:2022 Control A.8.6.

**Target Audience**: Internal auditors, external auditors, capacity planning team, compliance managers, IT management

**Prerequisites**: 
- Capacity monitoring operational (ISMS-IMP-A.8.6-S1)
- Capacity forecasting and planning processes established (ISMS-IMP-A.8.6-S2)
- Assessment workbooks completed (Assessment 1 and 2)
- Evidence collected and organized

### 1.2 Implementation Scope

This guide covers:

1. **Assessment Execution** - Conducting capacity utilization and forecasting assessments
2. **Evidence Collection** - Gathering and organizing supporting documentation
3. **Compliance Scoring** - Evaluating capacity management effectiveness
4. **Dashboard Generation** - Creating executive capacity management dashboard
5. **Audit Preparation** - Preparing for internal and external audits
6. **Continuous Improvement** - Using assessment results for process improvement

**Assessment Types Covered**:
- **Assessment 1**: Capacity Utilization Analysis (Monthly)
- **Assessment 2**: Capacity Forecasts and Planning (Quarterly)
- **Dashboard**: Capacity Management Overview (Monthly)

---

## 2. Assessment Execution Process

### 2.1 Assessment 1: Capacity Utilization Analysis

**Frequency**: Monthly  
**Duration**: 2-4 hours (data collection) + 2-4 hours (analysis)  
**Owner**: Capacity Planning Team

#### 2.1.1 Preparation Phase

**Week Before Assessment**:
1. **Schedule Assessment**:
   - Block time for data collection
   - Notify infrastructure teams
   - Identify any infrastructure changes since last assessment

2. **Prepare Tools**:
   - Generate blank Assessment 1 workbook: `python3 generate_assessment_1_capacity_utilization.py`
   - Verify monitoring tool access
   - Prepare data export templates

3. **Review Previous Assessment**:
   - Identify resources added/removed
   - Review action items from previous month
   - Update resource inventory if needed

#### 2.1.2 Data Collection Phase

**Step 1: Export Monitoring Data**

Export current utilization data from monitoring tools:

**Prometheus Example**:
```bash
# Export current CPU utilization
curl -G 'http://prometheus:9090/api/v1/query' \
  --data-urlencode 'query=100-(avg(irate(node_cpu_seconds_total{mode="idle"}[5m]))*100)' \
  | jq -r '.data.result[] | [.metric.instance, .value[1]] | @csv' \
  > cpu_current.csv

# Export peak CPU (last 30 days)
curl -G 'http://prometheus:9090/api/v1/query' \
  --data-urlencode 'query=max_over_time((100-(avg(irate(node_cpu_seconds_total{mode="idle"}[5m]))*100))[30d:])' \
  | jq -r '.data.result[] | [.metric.instance, .value[1]] | @csv' \
  > cpu_peak_30d.csv
```

**Datadog Example**:
```python
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.metrics_api import MetricsApi
from datetime import datetime

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MetricsApi(api_client)
    
    # Query current CPU utilization
    response = api_instance.query_metrics(
        from_time=int((datetime.now() - timedelta(hours=1)).timestamp()),
        to_time=int(datetime.now().timestamp()),
        query="avg:system.cpu.user{*} by {host}"
    )
    
    # Export to CSV
    with open('cpu_current.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['Host', 'CPU_Utilization'])
        for series in response.series:
            host = series.scope
            value = series.pointlist[-1][1]  # Latest value
            writer.writerow([host, value])
```

**CloudWatch Example**:
```python
import boto3
import csv
from datetime import datetime, timedelta

cloudwatch = boto3.client('cloudwatch')

# Get list of EC2 instances
ec2 = boto3.client('ec2')
instances = ec2.describe_instances()

with open('cpu_current.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Instance', 'CPU_Utilization_Avg', 'CPU_Utilization_Max'])
    
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            
            # Get CPU metrics
            response = cloudwatch.get_metric_statistics(
                Namespace='AWS/EC2',
                MetricName='CPUUtilization',
                Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}],
                StartTime=datetime.now() - timedelta(days=30),
                EndTime=datetime.now(),
                Period=86400,
                Statistics=['Average', 'Maximum']
            )
            
            if response['Datapoints']:
                latest = response['Datapoints'][-1]
                writer.writerow([instance_id, latest['Average'], latest['Maximum']])
```

**Step 2: Populate Assessment Workbook**

1. Open generated Assessment 1 workbook
2. Populate each resource sheet:
   - **Compute_Resources**: Import CPU/memory data
   - **Storage_Resources**: Import disk/database capacity
   - **Network_Resources**: Import bandwidth utilization
   - **Application_Resources**: Import user sessions, transactions
   - **Cloud_Resources**: Import cloud quotas, usage
3. Verify auto-calculations:
   - Utilization percentages
   - Threshold status (OK/Warning/Critical)
4. Review **Threshold_Summary** dashboard
5. Complete **Coverage_Analysis** (identify monitoring gaps)

#### 2.1.3 Analysis Phase

**Review Threshold Status**:
1. Identify resources at Warning threshold (70-85%)
   - → Begin capacity planning
   - → Forecast when critical threshold will be reached
2. Identify resources at Critical threshold (>85%)
   - → Immediate capacity expansion required
   - → Escalate to IT management
3. Document action items for each warning/critical resource

**Review Monitoring Coverage**:
1. Calculate coverage percentage:
   - Production systems: Target 100%
   - Non-production systems: Target 90%
2. Identify resources not yet monitored
3. Document plan to close monitoring gaps

**Quality Checks**:
- [ ] All resource types documented
- [ ] Utilization data is current (within last 7 days)
- [ ] Peak utilization data available (30-day window)
- [ ] Threshold status correctly calculated
- [ ] Coverage gaps identified and documented

#### 2.1.4 Evidence Collection

Document evidence in **Evidence_Register** sheet:

| Evidence Type | Examples | Storage Location |
|---------------|----------|------------------|
| Monitoring Dashboards | Screenshots showing current utilization | `/evidence/A86/2026-01/dashboard_screenshots/` |
| Monitoring Data Exports | CSV/JSON exports from Prometheus/Datadog/CloudWatch | `/evidence/A86/2026-01/data_exports/` |
| Threshold Configuration | Alert configuration backups | `/evidence/A86/2026-01/alert_configs/` |
| Alert History | Capacity alert logs (30 days) | `/evidence/A86/2026-01/alert_history/` |

**Evidence Naming Convention**:
```
ISMS-A86-[Type]-[YYYY-MM]-[Description].[ext]

Examples:
ISMS-A86-MON-2026-01-Prometheus-Dashboard.png
ISMS-A86-DATA-2026-01-CPU-Utilization-Export.csv
ISMS-A86-CONFIG-2026-01-Alert-Thresholds.json
```

#### 2.1.5 Approval and Distribution

1. **Internal Review**: Capacity planning team reviews completeness
2. **Management Review**: Infrastructure Manager reviews findings
3. **Approval**: IT Operations Manager approves monthly assessment
4. **Distribution**:
   - Email monthly capacity report to IT management
   - File assessment workbook in capacity management repository
   - Update dashboard (see Section 4)

**Monthly Report Email Template**:
```
Subject: Monthly Capacity Report - [Month Year]

Capacity Health Score: [X]% ([Y] of [Z] resources at OK status)

KEY FINDINGS:
- [N] resources at Warning threshold (require capacity planning)
- [M] resources at Critical threshold (immediate action required)

TOP CAPACITY CONCERNS:
1. [Resource] - [X]% utilization - Action: [Plan]
2. [Resource] - [X]% utilization - Action: [Plan]

ACTIONS COMPLETED THIS MONTH:
- [Action]

PLANNED ACTIONS NEXT MONTH:
- [Action]

Full Assessment: [Link to Assessment 1 workbook]
Dashboard: [Link to Capacity Management Dashboard]

Questions? Contact: [Capacity Planning Team]
```

### 2.2 Assessment 2: Capacity Forecasts and Planning

**Frequency**: Quarterly  
**Duration**: 1-2 days (data analysis) + Half-day workshop  
**Owner**: Capacity Planning Team

#### 2.2.1 Preparation Phase

**2 Weeks Before Assessment**:
1. **Collect Historical Data**:
   - Export 12-24 months of utilization data
   - Prepare data for trend analysis
   - Identify any data quality issues

2. **Schedule Planning Workshop**:
   - Book half-day session with stakeholders
   - Attendees: Capacity team, infrastructure managers, IT Director, finance
   - Prepare workshop materials

3. **Review Business Assumptions**:
   - Contact business units for growth projections
   - Review planned initiatives (product launches, marketing campaigns)
   - Document any major changes since last forecast

#### 2.2.2 Data Analysis Phase

**Step 1: Historical Utilization Analysis**

Generate blank Assessment 2 workbook:
```bash
python3 generate_assessment_2_capacity_forecasts.py
```

Populate **Historical_Utilization** sheet with 12-month data:

```python
# Example: Load historical data from CSV exports
import pandas as pd
import openpyxl

# Load historical data
df = pd.read_csv('historical_cpu_12months.csv', parse_dates=['Date'])

# Load assessment workbook
wb = openpyxl.load_workbook('ISMS-IMP-A.8.6.2_Capacity_Forecasts_Planning_20260111.xlsx')
ws = wb['Historical_Utilization']

# Populate sheet
row = 4
for _, data in df.iterrows():
    ws[f'A{row}'] = data['Date']
    ws[f'B{row}'] = data['Resource']
    ws[f'C{row}'] = data['Utilization']
    ws[f'D{row}'] = data['Peak']
    row += 1

wb.save('ISMS-IMP-A.8.6.2_Capacity_Forecasts_Planning_20260111.xlsx')
```

**Step 2: Trend Analysis**

Perform statistical trend analysis (per ISMS-IMP-A.8.6-S2, Section 3):

```python
from sklearn.linear_model import LinearRegression
import numpy as np

# Prepare data
df['Days'] = (df['Date'] - df['Date'].min()).dt.days
X = df[['Days']].values
y = df['Utilization'].values

# Fit linear regression
model = LinearRegression()
model.fit(X, y)

# Calculate growth rate
growth_rate_per_day = model.coef_[0]
growth_rate_per_month = growth_rate_per_day * 30

# Calculate R-squared
r_squared = model.score(X, y)

print(f"Growth Rate: {growth_rate_per_month:.2f}% per month")
print(f"R-squared: {r_squared:.3f}")
```

Populate **Trend_Analysis** sheet:
- Growth rate (% per month)
- R-squared value
- Trend method used (linear regression, exponential, seasonal)
- Seasonal patterns identified (if any)

**Step 3: Capacity Forecasting**

Generate forecasts using trend data:

```python
def forecast_linear(current_util, growth_rate_per_month, months_ahead):
    """Generate linear forecast."""
    forecast = current_util + (growth_rate_per_month * months_ahead)
    return forecast

# Generate forecasts
current = 68  # Current 68% utilization
growth = 2.5  # 2.5% growth per month

forecast_6m = forecast_linear(current, growth, 6)
forecast_12m = forecast_linear(current, growth, 12)
forecast_24m = forecast_linear(current, growth, 24)

print(f"Current: {current}%")
print(f"6-month forecast: {forecast_6m:.1f}%")
print(f"12-month forecast: {forecast_12m:.1f}%")
print(f"24-month forecast: {forecast_24m:.1f}%")
```

Populate **Capacity_Forecasts** sheet with projections.

**Step 4: Capacity Exhaustion Projection**

Calculate when resources will reach thresholds:

```python
def calculate_exhaustion(current, growth_rate, threshold=85):
    """Calculate months until capacity exhaustion."""
    if growth_rate <= 0:
        return None
    headroom = threshold - current
    if headroom <= 0:
        return 0
    months = headroom / growth_rate
    return months

months_to_critical = calculate_exhaustion(current, growth, threshold=85)
exhaustion_date = datetime.now() + timedelta(days=months_to_critical*30)

print(f"Months to 85% threshold: {months_to_critical:.1f}")
print(f"Exhaustion date: {exhaustion_date.strftime('%Y-%m-%d')}")

# Classify urgency
if months_to_critical <= 3:
    urgency = "Immediate (0-3 months)"
elif months_to_critical <= 6:
    urgency = "Short-term (3-6 months)"
elif months_to_critical <= 12:
    urgency = "Medium-term (6-12 months)"
else:
    urgency = "Long-term (>12 months)"

print(f"Urgency: {urgency}")
```

Populate **Capacity_Exhaustion** sheet.

#### 2.2.3 Capacity Planning Workshop

**Workshop Agenda** (4 hours):

**Hour 1: Forecast Review**
- Present capacity forecasts for all critical resources
- Review capacity exhaustion timeline
- Discuss business growth assumptions
- Identify high-risk resources (exhaustion within 6 months)

**Hour 2: Capacity Expansion Planning**
- For each high-risk resource:
  - Determine expansion sizing (how much capacity to add)
  - Evaluate expansion options (cloud vs. on-premises, timing)
  - Estimate costs (CapEx, OpEx)
  - Assign ownership
- Document expansion plans in **Planned_Expansions** sheet

**Hour 3: Budget Impact Analysis**
- Calculate total budget impact (CapEx and OpEx)
- Develop quarterly spending plan
- Identify budget approval requirements
- Populate **Budget_Planning** sheet

**Hour 4: Forecast Accuracy Review & Action Planning**
- Compare previous quarter's forecasts to actual
- Calculate forecast accuracy (MAPE)
- Identify forecast methodology improvements
- Define action items and ownership
- Populate **Forecast_Accuracy** sheet

**Workshop Outputs**:
- Completed Assessment 2 workbook
- Quarterly capacity expansion plan
- Budget request documentation
- Action item register

#### 2.2.4 Forecast Accuracy Validation

Compare previous forecasts to actual utilization:

```python
# Load previous forecast (from 3 months ago)
previous_forecast = [55, 58, 61, 64]  # Forecasted for months 1-4

# Load actual observed values
actual_observed = [52, 57, 59, 62]  # Actual for months 1-4

# Calculate MAPE
def calculate_mape(forecast, actual):
    forecast = np.array(forecast)
    actual = np.array(actual)
    mape = np.mean(np.abs((actual - forecast) / actual)) * 100
    return mape

mape = calculate_mape(previous_forecast, actual_observed)
print(f"Forecast Accuracy (MAPE): {mape:.1f}%")

if mape <= 5:
    rating = "Excellent"
elif mape <= 10:
    rating = "Good"
elif mape <= 15:
    rating = "Acceptable"
else:
    rating = "Poor - Requires Methodology Review"

print(f"Accuracy Rating: {rating}")
```

Document results in **Forecast_Accuracy** sheet.

**If Accuracy is Poor** (MAPE > 15%):
1. Review trend analysis methodology
2. Check for business changes not reflected in forecast
3. Consider seasonal or exponential models
4. Shorten forecast horizon
5. Document lessons learned

#### 2.2.5 Approval and Distribution

1. **Technical Review**: Capacity planning team validates completeness
2. **Budget Review**: CFO reviews budget impact
3. **Management Approval**: IT Director/CIO approves capacity plan
4. **Distribution**:
   - Email quarterly capacity planning report to IT leadership and finance
   - Present to executive management (if budget > threshold)
   - File assessment workbook in repository
   - Update dashboard

---

## 3. Evidence Collection Best Practices

### 3.1 Evidence Organization

**Directory Structure**:
```
/capacity-management-evidence/
├── 2026-01/
│   ├── assessments/
│   │   ├── ISMS-IMP-A.8.6.1_Capacity_Utilization_20260111.xlsx
│   │   └── ISMS-IMP-A.8.6.2_Capacity_Forecasts_Planning_20260111.xlsx
│   ├── monitoring-data/
│   │   ├── prometheus_cpu_export_2026-01.csv
│   │   ├── cloudwatch_disk_export_2026-01.csv
│   │   └── datadog_network_export_2026-01.json
│   ├── dashboards/
│   │   ├── capacity_dashboard_2026-01-11.png
│   │   └── grafana_capacity_overview_2026-01.png
│   ├── configurations/
│   │   ├── prometheus_alerts_2026-01.yml
│   │   └── threshold_config_2026-01.json
│   ├── reports/
│   │   ├── Monthly_Capacity_Report_2026-01.pdf
│   │   └── capacity_planning_presentation_2026-01.pptx
│   └── evidence_index.xlsx
├── 2026-02/
...
```

### 3.2 Evidence Index

Maintain master evidence index (Excel spreadsheet):

| Evidence ID | Date | Type | Description | File Path | Related Assessment | Retention Date |
|-------------|------|------|-------------|-----------|-------------------|----------------|
| A86-001 | 2026-01-11 | Monitoring Data | CPU utilization export | .../monitoring-data/prometheus_cpu_export_2026-01.csv | Assessment 1 | 2029-01-11 |
| A86-002 | 2026-01-11 | Dashboard | Capacity dashboard screenshot | .../dashboards/capacity_dashboard_2026-01-11.png | Assessment 1 | 2029-01-11 |
| A86-003 | 2026-01-15 | Report | Monthly capacity report | .../reports/Monthly_Capacity_Report_2026-01.pdf | Assessment 1 | 2029-01-15 |

**Retention Policy**:
- Assessment workbooks: 3 years
- Monitoring data exports: 3 years
- Dashboard screenshots: 3 years
- Monthly reports: 3 years
- Quarterly plans: 5 years (for audit trail)
- Annual strategic plans: 7 years (for strategic review)

### 3.3 Evidence Quality Checklist

For each piece of evidence:
- [ ] **Authentic**: Traceable to source system
- [ ] **Complete**: Contains all necessary information
- [ ] **Timely**: From appropriate time period
- [ ] **Accurate**: Data validated for correctness
- [ ] **Relevant**: Directly supports capacity management requirement

---

## 4. Dashboard Generation and Maintenance

### 4.1 Dashboard Purpose

The **Capacity Management Dashboard** provides executive-level consolidated view integrating data from:
- Assessment 1 (Capacity Utilization)
- Assessment 2 (Capacity Forecasts and Planning)

**Dashboard Output**: Excel workbook with charts, metrics, and trends

### 4.2 Dashboard Generation Process

**Step 1: Normalize Assessment Files**

Before generating dashboard, normalize assessment workbooks:

```bash
# Run normalization script
python3 normalize_assessment_files_a86.py

# Prompts for:
# - Source directory (where Assessment 1 and 2 are located)
# - Output directory (default: Dashboard_Sources/)

# Creates normalized copies:
# - ISMS-IMP-A.8.6.1.xlsx (from Assessment 1 with date stamp)
# - ISMS-IMP-A.8.6.2.xlsx (from Assessment 2 with date stamp)
```

**Normalization ensures**:
- Stable filenames for dashboard formulas
- External workbook links work correctly
- Audit trail maintained (manifest created)

**Step 2: Generate Dashboard**

```bash
# Generate capacity management dashboard
python3 generate_dashboard_capacity_management.py

# Output: ISMS-A.8.6_Capacity_Management_Dashboard_YYYYMMDD.xlsx
```

**Step 3: Link Dashboard to Normalized Files**

1. Move dashboard to same directory as normalized files
2. Open dashboard in Excel
3. If prompted "Update Links?", click "Update"
4. Dashboard auto-populates with current data

**Dashboard File Locations**:
```
Dashboard_Sources/
├── ISMS-IMP-A.8.6.1.xlsx (normalized Assessment 1)
├── ISMS-IMP-A.8.6.2.xlsx (normalized Assessment 2)
├── ISMS-A.8.6_Capacity_Management_Dashboard_20260111.xlsx
└── normalization_manifest.txt
```

### 4.3 Dashboard Metrics

**Executive Dashboard Sheet** (one-page summary):
- **Capacity Health Score**: % of resources at OK status (target: ≥95%)
- **Resources at Risk**: Count of resources at warning/critical
- **Forecast Risk**: Resources with exhaustion projected within 3/6/12 months
- **Planning Effectiveness**: % proactive expansions (target: ≥90%)
- **Forecast Accuracy**: Average MAPE across all forecasts (target: ≤15%)
- **Budget Status**: Capacity expansion budget utilized vs. planned

**Utilization Summary Sheet**: Breakdown by resource type (compute, storage, network, application, cloud)

**Forecast Summary Sheet**: Capacity exhaustion timeline (immediate, short-term, medium-term)

**Maturity Assessment Sheet**: Capacity management maturity scorecard (levels 1-5)

### 4.4 Dashboard Distribution

**Monthly** (after Assessment 1):
- Email dashboard to IT management
- Post to management portal (SharePoint, Confluence)
- Present in monthly IT operations meeting

**Quarterly** (after Assessment 2):
- Present dashboard to IT leadership
- Include in quarterly business review
- Distribute to finance for budget tracking

**Dashboard Security**:
- Internal distribution only (contains capacity details)
- Mark as "Internal - Confidential"
- Do not share externally without redaction

---

## 5. Compliance Scoring Methodology

### 5.1 Compliance Dimensions

Capacity management compliance assessed across 5 dimensions (per ISMS-POL-A.8.6-S3):

#### 5.1.1 Monitoring Compliance

**Assessment Criteria**:
- Monitoring coverage: Production systems (target 100%), non-production (target 90%)
- Monitoring data quality: Completeness, accuracy, timeliness
- Threshold configuration: Warning/critical thresholds defined
- Alerting: Alerts triggering appropriately
- Data retention: Meeting policy requirements (12+ months historical)

**Scoring**:
```
Score = (
    (Monitoring Coverage % × 0.4) +
    (Data Quality % × 0.2) +
    (Threshold Config Completeness % × 0.2) +
    (Alerting Functionality % × 0.1) +
    (Data Retention Compliance % × 0.1)
)
```

**Example**:
```
Monitoring Coverage: 95% (production) = 0.95
Data Quality: 98% complete = 0.98
Thresholds: 100% configured = 1.00
Alerting: 90% functional = 0.90
Retention: 100% compliant = 1.00

Score = (0.95×0.4) + (0.98×0.2) + (1.00×0.2) + (0.90×0.1) + (1.00×0.1)
      = 0.38 + 0.196 + 0.20 + 0.09 + 0.10
      = 96.6% (Fully Compliant)
```

#### 5.1.2 Forecasting Compliance

**Assessment Criteria**:
- Forecasts developed for all in-scope resources
- Forecasting methodology documented
- Forecast accuracy (MAPE ≤ 15%)
- Update frequency (quarterly minimum)
- Business assumptions documented

**Scoring**: Same weighted approach

#### 5.1.3 Planning Compliance

**Assessment Criteria**:
- Planning cycles executed (monthly, quarterly, annual)
- Expansion plans documented
- Proactive expansion ratio (≥90%)
- Lead time management
- Budget integration

**Scoring**: Same weighted approach

#### 5.1.4 Reporting Compliance

**Assessment Criteria**:
- Monthly reports produced and distributed
- Quarterly planning reports produced
- Annual strategic plan produced
- Management review documented
- Incident reporting (capacity-related events)

**Scoring**: Same weighted approach

#### 5.1.5 Optimization Compliance

**Assessment Criteria**:
- Optimization activities performed (quarterly)
- Over-provisioning identified and remediated
- Cost optimization (cloud spend)
- Performance tuning documented
- Results measured

**Scoring**: Same weighted approach

### 5.2 Overall Compliance Score

**Calculation**:
```
Overall Score = (Monitoring + Forecasting + Planning + Reporting + Optimization) / 5
```

**Compliance Levels**:
- **Fully Compliant** (≥95%): Comprehensive capacity management
- **Substantially Compliant** (85-94%): Strong implementation, minor gaps
- **Partially Compliant** (70-84%): Functional but significant gaps
- **Non-Compliant** (<70%): Major gaps requiring remediation

**Dashboard Integration**: Overall compliance score displayed on executive dashboard

### 5.3 Gap Remediation

For each non-compliant dimension:
1. Identify specific gaps (what requirements not met)
2. Document root cause (why not met)
3. Develop remediation plan (how to close gap)
4. Assign ownership (who will close gap)
5. Set target date (when gap will be closed)
6. Track progress (monthly review of open gaps)

**Gap Register Template**:
| Gap ID | Dimension | Gap Description | Root Cause | Remediation Plan | Owner | Target Date | Status |
|--------|-----------|----------------|------------|------------------|-------|-------------|--------|
| G-001 | Monitoring | 15% of production systems not monitored | Legacy systems, no agent support | Deploy agentless monitoring (SNMP) | Infrastructure Team | 2026-03-31 | In Progress |

---

## 6. Audit Preparation

### 6.1 Internal Audit Preparation

**2 Weeks Before Audit**:
1. **Review Compliance Score**: Ensure ≥85% across all dimensions
2. **Organize Evidence**: Update evidence index, verify all evidence accessible
3. **Test Dashboard Links**: Verify dashboard formulas working correctly
4. **Prepare Presentations**: Create audit walkthrough presentation

**1 Week Before Audit**:
1. **Dry Run**: Conduct internal dry-run with capacity team
2. **Evidence Package**: Prepare evidence package for auditors
3. **Interview Prep**: Brief capacity team on audit questions
4. **System Access**: Arrange monitoring system access for auditors

**Evidence Package Contents**:
- Assessment 1 and 2 workbooks (latest quarter)
- Capacity management dashboard
- Evidence index
- Monthly capacity reports (last 3 months)
- Quarterly capacity planning report (latest)
- Policy documents (ISMS-POL-A.8.6 series)
- Process documentation (ISMS-IMP-A.8.6 series)

### 6.2 External Audit / ISO 27001 Certification

**1 Month Before Audit**:
1. **Pre-Audit Assessment**: Conduct internal assessment using audit checklist
2. **Gap Remediation**: Close any compliance gaps identified
3. **Management Review**: Present capacity management status to CISO/CIO
4. **Auditor Communication**: Confirm audit scope and schedule

**External Auditor Evidence**:
- All evidence from internal audit package
- Demonstration of monitoring systems
- Demonstration of forecasting methodology
- Capacity incident reports (if any)
- Capacity planning meeting minutes

**Audit Sampling**: Auditors typically sample:
- 10-20% of monitored resources (verify monitoring operational)
- 3-5 resources with forecasts (verify forecast methodology)
- 2-3 capacity expansions (verify planning process)

**Auditor Interviews**: Prepare capacity team for questions:
- "How do you monitor capacity?"
- "How do you forecast capacity requirements?"
- "How do you plan capacity expansions?"
- "How do you measure forecast accuracy?"
- "How do you handle capacity incidents?"

### 6.3 Audit Findings Management

**If Audit Finding Raised**:
1. **Acknowledge**: Confirm understanding of finding
2. **Root Cause**: Determine why gap exists
3. **Remediation Plan**: Develop corrective action plan
4. **Timeline**: Commit to remediation date
5. **Verification**: Plan for auditor to verify closure

**Common Findings**:
- **Monitoring Coverage Gaps**: Not all resources monitored
  - Remediation: Implement monitoring for gap resources
- **Forecast Accuracy Poor**: MAPE > 15%
  - Remediation: Review and improve forecasting methodology
- **Proactive Planning Low**: <90% proactive expansions
  - Remediation: Improve forecast lead time, earlier planning
- **Evidence Gaps**: Missing supporting documentation
  - Remediation: Improve evidence collection process

---

## 7. Continuous Improvement

### 7.1 Metrics for Improvement

Track capacity management effectiveness over time:

**Operational Metrics**:
- Capacity health score (monthly trend)
- Monitoring coverage percentage (monthly)
- Forecast accuracy (MAPE) (quarterly)
- Proactive expansion ratio (quarterly)
- Capacity-related incidents (monthly)

**Efficiency Metrics**:
- Time to add capacity (from request to deployment)
- Capacity utilization efficiency (% of resources optimally sized)
- Cost per unit capacity ($/GB, $/core, $/user)

**Maturity Metrics**:
- Capacity management maturity level (annual assessment)
- Process automation percentage
- Staff capability (training completion)

### 7.2 Lessons Learned Process

**After Each Capacity Incident**:
1. Conduct post-mortem (within 1 week)
2. Document:
   - What happened (timeline)
   - Root cause (why it happened)
   - Impact (business/user impact)
   - Detection (how/when discovered)
   - Response (actions taken)
   - Prevention (how to prevent recurrence)
3. Update processes/procedures
4. Share lessons learned with team

**Quarterly Lessons Learned Review**:
1. Review all capacity incidents (quarter)
2. Identify common themes
3. Update forecasting methodology
4. Update threshold configurations
5. Improve monitoring coverage
6. Enhance planning processes

### 7.3 Process Improvement Initiatives

**Annual Review** (part of annual capacity planning):
1. Benchmark against industry standards (ITIL, NIST)
2. Identify process improvement opportunities
3. Prioritize improvements (impact vs. effort)
4. Develop improvement roadmap
5. Allocate resources for improvement
6. Track improvement implementation

**Example Improvements**:
- Automate forecast generation (reduce manual effort)
- Implement ML-based anomaly detection (improve accuracy)
- Integrate capacity planning with ITSM (improve workflow)
- Deploy auto-scaling (reduce manual expansions)
- Implement predictive monitoring (detect issues earlier)

---

## 8. Implementation Checklist

### 8.1 Assessment Process Setup

- [ ] Assessment 1 (Utilization) scheduled monthly
- [ ] Assessment 2 (Forecasting) scheduled quarterly
- [ ] Assessment workbook generation scripts tested
- [ ] Data export procedures documented
- [ ] Evidence collection process established
- [ ] Evidence repository created

### 8.2 Dashboard Implementation

- [ ] Normalization script tested
- [ ] Dashboard generation script tested
- [ ] Dashboard distribution process defined
- [ ] Executive training on dashboard interpretation

### 8.3 Compliance Scoring

- [ ] Compliance scoring methodology documented
- [ ] Gap remediation process defined
- [ ] Compliance tracking integrated into dashboard

### 8.4 Audit Readiness

- [ ] Internal audit schedule defined
- [ ] Evidence package template created
- [ ] Auditor interview preparation materials developed
- [ ] System access procedures for auditors documented

### 8.5 Continuous Improvement

- [ ] Metrics dashboard established
- [ ] Lessons learned process defined
- [ ] Annual improvement review scheduled
- [ ] Improvement tracking process established

---

## Appendix A: Assessment Execution Timeline

**Monthly Cycle** (Assessment 1):
```
Week 1: Data collection (Mon-Wed)
Week 1: Assessment completion (Thu-Fri)
Week 2: Evidence collection (Mon-Tue)
Week 2: Review and approval (Wed-Thu)
Week 2: Distribution and dashboard update (Fri)
```

**Quarterly Cycle** (Assessment 2):
```
Week 1-2: Historical data analysis and trend analysis
Week 3: Forecasting and capacity planning workshop
Week 4: Report finalization, budget approval, distribution
```

**Annual Cycle**:
```
Month 1: Long-term forecasting and strategic planning
Month 2: Annual capacity plan development
Month 3: Executive approval and communication
```

---

## Appendix B: Audit Checklist

**Monitoring Compliance**:
- [ ] Monitoring tool deployed and operational
- [ ] ≥95% production systems monitored
- [ ] ≥90% non-production systems monitored
- [ ] Thresholds configured (warning, critical)
- [ ] Alerting functional and tested
- [ ] Historical data retained (12+ months)

**Forecasting Compliance**:
- [ ] Forecasts developed quarterly
- [ ] Forecasting methodology documented
- [ ] Forecast accuracy ≤15% MAPE
- [ ] Business assumptions documented
- [ ] Previous forecasts validated

**Planning Compliance**:
- [ ] Monthly capacity reviews conducted
- [ ] Quarterly capacity planning workshops held
- [ ] Annual capacity plan developed
- [ ] ≥90% proactive expansions
- [ ] Budget planning integrated

**Reporting Compliance**:
- [ ] Monthly capacity reports distributed
- [ ] Quarterly planning reports produced
- [ ] Annual strategic plan approved
- [ ] Management review documented
- [ ] Capacity incidents reported

**Optimization Compliance**:
- [ ] Quarterly optimization reviews conducted
- [ ] Over-provisioning identified and remediated
- [ ] Cost optimization measured
- [ ] Performance tuning documented
- [ ] Results tracked

---

**End of Document ISMS-IMP-A.8.6-S3**

---

**Document Status**: DRAFT - Pending Approval  
**Next Steps**: 
1. Review by internal audit and capacity planning team
2. Approval by Internal Audit Manager, Capacity Manager, CISO
3. Training on assessment methodology
4. First assessment execution (Assessment 1 and 2)
5. Dashboard generation and distribution
6. Prepare for first internal audit
