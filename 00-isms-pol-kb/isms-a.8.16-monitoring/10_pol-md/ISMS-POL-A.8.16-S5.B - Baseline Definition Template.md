# ISMS-POL-A.8.16-S5.B
## Baseline Definition Template

**Document ID**: ISMS-POL-A.8.16-S5.B
**Title**: Baseline Definition Template  
**Version**: 1.0  
**Date**: [Date]   
**Classification**: Internal  
**Owner**: SOC Lead  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date]  | SOC Lead / Security Engineering | Initial baseline methodology and template |

**Review Cycle**: Semi-annual (or when baseline methodology improves)  
**Next Review Date**: [Approval Date + 6 months]  
**Approvers**: 
- Primary: SOC Lead
- Technical Review: Security Engineering Manager
- Operational Input: SOC Tier 2/3 Analysts

**Distribution**: SOC, Security Engineering, System Owners  
**Related Documents**: ISMS-POL-A.8.16-S2.2 (Baseline & Anomaly Detection Requirements)

---

## 1. Purpose and Scope

### 1.1 Purpose

This template provides **step-by-step methodology** for establishing, documenting, and maintaining security monitoring baselines. Baselines are **documented normal behavior** used to detect anomalies and derive alert thresholds.

**Why Baselines Matter**: Without baselines, alerts are arbitrary ("failed logins >10" - why 10?). With baselines, alerts are data-driven ("failed logins >95th percentile × 1.2 multiplier").

**Target Audience**: SOC Tier 2/3 Analysts, Security Engineering, System Owners

### 1.2 Scope

This template applies to:

- **Systems**: Servers, workstations, network devices, applications
- **Metrics**: Authentication events, network traffic, resource usage, application activity
- **Use Cases**: New system monitoring, baseline reviews, threshold tuning, anomaly investigation

**Out of Scope**: Business metrics (sales volume, transaction counts) unless directly related to security.

### 1.3 Anti-Cargo-Cult Principle

**Cargo Cult Baseline**: "We documented a baseline because policy requires it. We wrote down some numbers. Mission accomplished!"

**Real Baseline**: "We measured actual behavior over 30-90 days, excluded anomalies, calculated statistics, derived thresholds with rationale, tested alerts, got approval, and scheduled quarterly reviews."

*"The first principle is that you must not fool yourself - and you are the easiest person to fool."* - Richard Feynman

**This template prevents self-fooling.**

---

## 2. Baseline Establishment Methodology

### 2.1 Step 1: Identify System

**What to Document**:
```
System Name: [Exact hostname or application name]
System Type: [Server / Workstation / Network Device / Application / Service]
Criticality: [Critical / High / Medium / Low]
System Owner: [Name / Team - who is accountable for this system?]
Business Function: [What does this system do? Why does it exist?]
Operating Hours: [24×7 / Business Hours Only / Batch Processing / Varies]
```

**Example**:
```
System Name: PROD-DC-01
System Type: Server (Domain Controller)
Criticality: Critical
System Owner: Windows Infrastructure Team (Contact: John Smith)
Business Function: Active Directory authentication for entire organization
Operating Hours: 24×7
```

**Why This Matters**: Context determines baseline expectations. Domain controller at 3 AM has different normal than web server at 3 AM.

---

### 2.2 Step 2: Define Metrics

**What to Baseline**: Choose metrics that indicate security-relevant behavior changes.

**Common Metric Categories**:

**Authentication Metrics**:
- Successful login events (per hour/day)
- Failed login events (per hour/day)
- Account lockouts (per day)
- Privilege escalation events (per day)

**Network Metrics**:
- Inbound connections (per hour)
- Outbound connections (per hour)
- Data transferred (MB per hour)
- DNS queries (per hour)

**Resource Usage Metrics**:
- CPU utilization (%)
- Memory utilization (%)
- Disk I/O (MB/s)
- Process count

**Application Metrics**:
- Queries per hour (databases)
- Transactions per hour (applications)
- Error rates (per hour)
- API calls per hour

**Guideline**: Start with 3-5 key metrics per system. Too many baselines = maintenance burden. Too few = blind spots.

**Example for Domain Controller**:
```
Metrics to Baseline:
1. Successful authentication events (per hour)
2. Failed authentication events (per hour)
3. Account lockout events (per day)
4. Kerberos ticket requests (per hour)
5. LDAP query volume (per hour)
```

**Rationale**: These metrics detect brute force attacks, credential stuffing, reconnaissance, and infrastructure issues.

---

### 2.3 Step 3: Collect Data

#### 2.3.1 Observation Period

**Minimum Duration**: 30 days  
**Recommended Duration**: 60-90 days  
**Rationale**: 30 days captures weekly patterns. 90 days captures monthly patterns (e.g., month-end processing). Shorter periods = incomplete picture.

**What to Include**:
- ✅ Normal operations
- ✅ Business cycles (month-end, quarter-end if within observation window)
- ✅ Typical user behavior

**What to Exclude**:
- ❌ Known incidents (security events, outages)
- ❌ Major system changes (migrations, upgrades during observation period)
- ❌ Scheduled maintenance windows (unless baseline is for maintenance activity)
- ❌ Obvious anomalies (e.g., one-time mass password reset)

**Example**:
```
Observation Period: 01.10.2025 - 30.12.2025 (90 days)
Exclusions:
- 15.11.2025: Phishing incident (excluded failed login spike)
- 20.12.2025 - 22.12.2025: Planned AD maintenance (excluded DC downtime)
- 25.12.2025: Christmas Day (minimal activity, but KEPT IN DATA as normal)
```

**Why Exclude Incidents?**: Incidents are by definition not normal. Including them inflates baselines (e.g., brute force spike makes "normal" failed logins look higher).

#### 2.3.2 Data Collection

**Source**: SIEM, log aggregation platform, monitoring tools  
**Granularity**: Hourly is recommended (daily too coarse, per-minute too granular)  
**Storage**: Export to CSV/Excel for analysis (or use SIEM statistical functions if available)

**Example Query** (pseudo-SIEM):
```
index=windows source=domain_controller EventCode=4624 (successful logon)
| bucket _time span=1h
| stats count by _time, host
| where host="PROD-DC-01"
```

Export result: Timestamp, Event_Count for entire observation period.

---

### 2.4 Step 4: Calculate Statistics

**Mandatory Statistics** (calculate for EACH metric):

1. **Mean (Average)**: Sum of all values ÷ number of observations
2. **Median**: Middle value when sorted (50th percentile)
3. **Standard Deviation**: Measure of variability around mean
4. **Min / Max**: Lowest and highest observed values
5. **95th Percentile**: Value below which 95% of observations fall

**Why These Statistics?**:

- **Mean**: Typical "average" behavior (but sensitive to outliers)
- **Median**: True "middle" behavior (robust to outliers)
- **Std Dev**: How much variation is normal? Low std dev = stable system. High std dev = variable system.
- **Min/Max**: Absolute bounds (but often include outliers)
- **95th Percentile**: High-end normal (excludes outliers, good for threshold derivation)

**Example Calculation** (successful logins on PROD-DC-01):
```
Observation period: 90 days × 24 hours = 2,160 hourly observations

Raw data: [120, 135, 118, 140, 128, ... , 122, 131]

Statistics:
Mean: 127.3 events/hour
Median: 125.0 events/hour
Std Dev: 14.2 events/hour
Min: 45 events/hour (overnight, weekend)
Max: 310 events/hour (outlier: Monday morning after long weekend)
95th Percentile: 155.0 events/hour
```

**Interpretation**: Typical login volume is ~125-130/hour. Variation is ±14/hour. 95% of time, logins are ≤155/hour.

**Tools**: Excel (AVERAGE, MEDIAN, STDEV.S, PERCENTILE.INC), Python (pandas .describe()), SIEM statistical functions.

---

### 2.5 Step 5: Create Time-Aware Baselines

**Why Time-Aware?**: Systems behave differently based on time of day, day of week. Single baseline = excessive false positives.

**Recommended Baseline Segments**:

1. **Business Hours** (Mon-Fri, 08:00-18:00): Peak activity
2. **Off-Hours** (Mon-Fri, 18:00-08:00): Reduced activity, some batch jobs
3. **Weekends** (Sat-Sun, all hours): Minimal activity (unless 24×7 business)

**Optional Segments** (for complex environments):
- **Lunch hours** (11:00-13:00): Reduced activity
- **Month-end** (last 3 days of month): Elevated activity for financial systems
- **Shift changes**: Manufacturing, healthcare with clear shift patterns

**Example** (Domain Controller successful logins):
```
Business Hours Baseline (Mon-Fri 08:00-18:00):
- Mean: 145.2 events/hour
- Median: 142.0 events/hour
- Std Dev: 18.3 events/hour
- 95th Percentile: 175.0 events/hour

Off-Hours Baseline (Mon-Fri 18:00-08:00):
- Mean: 45.3 events/hour
- Median: 42.0 events/hour
- Std Dev: 12.1 events/hour
- 95th Percentile: 65.0 events/hour

Weekend Baseline (Sat-Sun, all hours):
- Mean: 28.7 events/hour
- Median: 25.0 events/hour
- Std Dev: 9.2 events/hour
- 95th Percentile: 45.0 events/hour
```

**Alert Logic**:
- Business hours: Alert if >175 events/hour
- Off-hours: Alert if >65 events/hour
- Weekends: Alert if >45 events/hour

**Result**: Fewer false positives (Monday morning spike won't alert), better sensitivity (50 logins on Saturday WILL alert).

---

### 2.6 Step 6: Document Baseline

Use template in Section 3 below. **Fill out completely** - incomplete baselines are cargo cult.

**Required Fields**:
- System identification (name, type, owner, criticality)
- Metric definition (what is being measured)
- Observation period and exclusions
- Statistics for each time segment
- Derived thresholds (see Step 7)
- Approvals and review dates

**Storage**: ISMS document repository, shared drive, or dedicated baseline tracking system (Excel workbook recommended for small orgs).

---

### 2.7 Step 7: Derive Thresholds

**Threshold = When to Alert**

**Formula Options**:

**Option 1: Percentile-Based** (Recommended)
```
Threshold = 95th Percentile × Multiplier
Multiplier = 1.1 to 1.5 depending on risk tolerance
```

**Example**:
```
95th Percentile = 175 events/hour
Multiplier = 1.2 (moderate tolerance)
Threshold = 175 × 1.2 = 210 events/hour
```

**Option 2: Standard Deviation-Based**
```
Threshold = Mean + (N × Std Dev)
N = 2 to 3 standard deviations
```

**Example**:
```
Mean = 145.2 events/hour
Std Dev = 18.3 events/hour
N = 2 (moderate tolerance)
Threshold = 145.2 + (2 × 18.3) = 181.8 ≈ 182 events/hour
```

**Which to Use?**:
- **Percentile-based**: Better for skewed distributions, easier to explain to non-statisticians
- **Std Dev-based**: Better for normal distributions, mathematically rigorous

**Risk Tolerance**:
- **Low tolerance (sensitive)**: Lower multiplier (1.1) or N=2 → More alerts, fewer missed threats, more false positives
- **High tolerance (specific)**: Higher multiplier (1.5) or N=3 → Fewer alerts, more missed threats, fewer false positives

**Recommendation**: Start with moderate tolerance (1.2 multiplier or N=2.5), tune based on alert volume.

**Warning Thresholds** (Optional):
```
Warning = 95th Percentile × 1.1 (lower threshold, informational alert)
Critical = 95th Percentile × 1.3 (higher threshold, immediate response)
```

Allows tiered response (warnings logged, criticals paged).

---

### 2.8 Step 8: Approve Baseline

**Required Approvals**:
1. **System Owner**: Confirms baseline reflects expected system behavior
2. **SOC Lead**: Confirms baseline methodology followed, thresholds reasonable

**Approval Process**:
1. SOC analyst prepares baseline document
2. System owner reviews: "Yes, 145 logins/hour during business hours is normal for our environment"
3. SOC lead reviews: "Statistics calculated correctly, thresholds appropriate, approved"
4. Baseline marked as "Approved", effective date set
5. Alert rules updated with new thresholds

**What if System Owner Disagrees?**:
- Investigate discrepancy (data collection error? system changed during observation?)
- Extend observation period if needed
- Document disagreement and resolution in baseline document

**Approval Timeframe**: Complete within 5 business days of baseline preparation.

---

### 2.9 Baseline Review and Update

**Review Frequency**:
- **Critical systems**: Quarterly (every 3 months)
- **High criticality**: Semi-annually (every 6 months)
- **Medium/Low criticality**: Annually

**Trigger for Unscheduled Review**:
- System undergoes major change (migration, upgrade, architecture change)
- Alert volume excessive (too many false positives = threshold too low)
- Alert volume insufficient (missed incidents = threshold too high)
- Business function changes (e.g., user population doubles)

**Review Process**:
1. Re-run statistics for recent period (last 30-90 days)
2. Compare to existing baseline
3. If significant change (>20% shift in mean or median), update baseline
4. Document reason for change
5. Re-approve per Step 8

**Example**:
```
Original Baseline (Q1 2025): Mean 145.2 events/hour
Current Data (Q4 2025): Mean 198.7 events/hour
Change: +37% (company grew, more users)
Action: Update baseline, re-approve, adjust thresholds
```

---

## 3. Baseline Documentation Template

**Copy this template for each baseline:**
```
═══════════════════════════════════════════════════════════════
SECURITY MONITORING BASELINE DOCUMENT
═══════════════════════════════════════════════════════════════

SYSTEM INFORMATION
──────────────────────────────────────────────────────────────
System Name:             [Exact hostname / application name]
System Type:             [Server / Workstation / Network Device / Application]
Criticality:             [Critical / High / Medium / Low]
System Owner:            [Name / Team]
Owner Contact:           [Email / Phone]
Business Function:       [What does this system do?]
Operating Hours:         [24×7 / Business Hours Only / Varies]

METRIC DEFINITION
──────────────────────────────────────────────────────────────
Metric Name:             [Specific metric, e.g., "Successful Authentication Events"]
Metric Source:           [SIEM index, log source, monitoring tool]
Metric Type:             [Count / Volume / Rate / Percentage]
Unit of Measure:         [Events per hour / MB per hour / Percentage]
Security Relevance:      [Why are we monitoring this? What attacks does it detect?]

OBSERVATION PERIOD
──────────────────────────────────────────────────────────────
Start Date:              [DD.MM.YYYY]
End Date:                [DD.MM.YYYY]
Duration:                [X days]
Data Points Collected:   [Number of hourly/daily observations]

Exclusions:              [List dates/times excluded and why]
- [DD.MM.YYYY - DD.MM.YYYY]: [Reason for exclusion]
- [DD.MM.YYYY - DD.MM.YYYY]: [Reason for exclusion]

BUSINESS HOURS BASELINE (Mon-Fri 08:00-18:00)
──────────────────────────────────────────────────────────────
Mean:                    [X.X events/hour]
Median:                  [X.X events/hour]
Standard Deviation:      [X.X events/hour]
Minimum Observed:        [X.X events/hour]
Maximum Observed:        [X.X events/hour]
95th Percentile:         [X.X events/hour]
Data Points:             [N observations]

OFF-HOURS BASELINE (Mon-Fri 18:00-08:00)
──────────────────────────────────────────────────────────────
Mean:                    [X.X events/hour]
Median:                  [X.X events/hour]
Standard Deviation:      [X.X events/hour]
95th Percentile:         [X.X events/hour]
Data Points:             [N observations]

WEEKEND BASELINE (Sat-Sun, all hours)
──────────────────────────────────────────────────────────────
Mean:                    [X.X events/hour]
Median:                  [X.X events/hour]
Standard Deviation:      [X.X events/hour]
95th Percentile:         [X.X events/hour]
Data Points:             [N observations]

ALERT THRESHOLDS (DERIVED FROM BASELINE)
──────────────────────────────────────────────────────────────
Business Hours:          [X.X events/hour]
  Derivation:            [95th Percentile × 1.2 = X.X × 1.2 = X.X]
  
Off-Hours:               [X.X events/hour]
  Derivation:            [95th Percentile × 1.2 = X.X × 1.2 = X.X]
  
Weekends:                [X.X events/hour]
  Derivation:            [95th Percentile × 1.2 = X.X × 1.2 = X.X]

Risk Tolerance:          [Moderate / Sensitive / Specific]
Multiplier Rationale:    [Why 1.2? Balance between false positives and detection]

Warning Threshold:       [Optional - lower threshold for informational alerts]
Critical Threshold:      [Optional - higher threshold for immediate escalation]

BASELINE METADATA
──────────────────────────────────────────────────────────────
Established By:          [Analyst Name]
Established Date:        [DD.MM.YYYY]
Approved By (Owner):     [System Owner Name]
Approved By (SOC):       [SOC Lead Name]
Approval Date:           [DD.MM.YYYY]
Effective Date:          [DD.MM.YYYY]

Next Scheduled Review:   [DD.MM.YYYY]
Review Frequency:        [Quarterly / Semi-annually / Annually]

NOTES / COMMENTS
──────────────────────────────────────────────────────────────
[Any additional context, known seasonal patterns, planned changes, etc.]

REVISION HISTORY
──────────────────────────────────────────────────────────────
Version | Date       | Changed By      | Changes Made
--------|------------|-----------------|--------------------------------
1.0     | DD.MM.YYYY | [Analyst]       | Initial baseline
1.1     | DD.MM.YYYY | [Analyst]       | Updated after Q2 review (+15% user growth)

═══════════════════════════════════════════════════════════════
```

---

## 4. Example Baselines

### 4.1 Example 1: Domain Controller - Successful Authentication
```
═══════════════════════════════════════════════════════════════
BASELINE: Domain Controller Successful Authentication
═══════════════════════════════════════════════════════════════

SYSTEM INFORMATION
System Name:             PROD-DC-01.company.local
System Type:             Server (Windows Domain Controller)
Criticality:             Critical
System Owner:            Windows Infrastructure Team (John Smith)
Owner Contact:           jsmith@company.com
Business Function:       Active Directory authentication for 2,500 users
Operating Hours:         24×7

METRIC DEFINITION
Metric Name:             Successful Authentication Events (Kerberos + NTLM)
Metric Source:           SIEM index=windows EventCode=4624
Metric Type:             Count
Unit of Measure:         Events per hour
Security Relevance:      Detect unauthorized access, lateral movement, credential theft

OBSERVATION PERIOD
Start Date:              01.10.2025
End Date:                30.12.2025
Duration:                90 days (2,160 hourly observations)
Exclusions:              15.11.2025 10:00-12:00 (phishing incident - 500 failed logins spike)

BUSINESS HOURS BASELINE (Mon-Fri 08:00-18:00)
Mean:                    145.2 events/hour
Median:                  142.0 events/hour
Standard Deviation:      18.3 events/hour
Minimum Observed:        95 events/hour (light day before holiday)
Maximum Observed:        210 events/hour (Monday morning)
95th Percentile:         175.0 events/hour
Data Points:             450 observations

OFF-HOURS BASELINE (Mon-Fri 18:00-08:00)
Mean:                    45.3 events/hour
Median:                  42.0 events/hour
Standard Deviation:      12.1 events/hour
95th Percentile:         65.0 events/hour
Data Points:             630 observations

WEEKEND BASELINE (Sat-Sun, all hours)
Mean:                    28.7 events/hour
Median:                  25.0 events/hour
Standard Deviation:      9.2 events/hour
95th Percentile:         45.0 events/hour
Data Points:             480 observations

ALERT THRESHOLDS
Business Hours:          210 events/hour (175 × 1.2)
Off-Hours:               78 events/hour (65 × 1.2)
Weekends:                54 events/hour (45 × 1.2)
Risk Tolerance:          Moderate (multiplier 1.2)
Multiplier Rationale:    Balance sensitivity vs. operational overhead

BASELINE METADATA
Established By:          Jane Analyst (SOC Tier 2)
Established Date:        05.01.2026
Approved By (Owner):     John Smith (Windows Infra Team)
Approved By (SOC):       Mike Johnson (SOC Lead)
Approval Date:           [Approval Date]
Effective Date:          07.01.2026
Next Scheduled Review:   07.04.2026 (Quarterly - Critical System)

NOTES
- Monday mornings typically +20% above mean (weekend email catch-up)
- Overnight backups authenticate every hour (~5 events/hour baseline component)
- Annual user onboarding in September may require baseline review
═══════════════════════════════════════════════════════════════
```

### 4.2 Example 2: Database Server - Query Volume
```
═══════════════════════════════════════════════════════════════
BASELINE: Database Server Query Volume
═══════════════════════════════════════════════════════════════

SYSTEM INFORMATION
System Name:             PROD-SQL-03
System Type:             Server (MS SQL Database)
Criticality:             High
System Owner:            Database Team (Maria Lopez)
Business Function:       Customer order processing database
Operating Hours:         24×7 (web store never closes)

METRIC DEFINITION
Metric Name:             SQL Query Count (SELECT, INSERT, UPDATE, DELETE)
Metric Source:           SQL Server logs via SIEM (index=mssql)
Unit of Measure:         Queries per hour
Security Relevance:      Detect SQL injection, data exfiltration, unauthorized access

OBSERVATION PERIOD
Start Date:              01.11.2025
End Date:                30.01.2026
Duration:                90 days
Exclusions:              25.12.2025 - 26.12.2025 (Christmas - store offline for maintenance)

BUSINESS HOURS BASELINE (Mon-Fri 08:00-18:00)
Mean:                    12,450 queries/hour
Median:                  12,200 queries/hour
Standard Deviation:      1,840 queries/hour
95th Percentile:         15,800 queries/hour
Data Points:             450 observations

OFF-HOURS BASELINE (Mon-Fri 18:00-08:00)
Mean:                    8,320 queries/hour
Median:                  8,100 queries/hour
Standard Deviation:      1,220 queries/hour
95th Percentile:         10,500 queries/hour
Data Points:             630 observations

WEEKEND BASELINE (Sat-Sun, all hours)
Mean:                    9,100 queries/hour (higher than weekday off-hours - online shopping!)
95th Percentile:         11,200 queries/hour

ALERT THRESHOLDS
Business Hours:          18,960 queries/hour (15,800 × 1.2)
Off-Hours:               12,600 queries/hour (10,500 × 1.2)
Weekends:                13,440 queries/hour (11,200 × 1.2)

NOTES
- Black Friday (29.11.2025) excluded from baseline (10× normal volume)
- Month-end processing (last 3 days) shows +15% query volume - within baseline
═══════════════════════════════════════════════════════════════
```

### 4.3 Example 3: Firewall - Outbound Connections
```
═══════════════════════════════════════════════════════════════
BASELINE: Firewall Outbound Connection Attempts
═══════════════════════════════════════════════════════════════

SYSTEM INFORMATION
System Name:             FW-PERIMETER-01
System Type:             Network Device (Firewall)
Criticality:             Critical
System Owner:            Network Security Team
Business Function:       Perimeter security for corporate network
Operating Hours:         24×7

METRIC DEFINITION
Metric Name:             Outbound Connection Attempts (New Connections)
Metric Source:           Firewall logs via Syslog (index=firewall action=new)
Unit of Measure:         Connections per hour
Security Relevance:      Detect C2 beaconing, data exfiltration, unauthorized tunnels

OBSERVATION PERIOD
Start Date:              01.09.2025
End Date:                30.11.2025
Duration:                90 days

BUSINESS HOURS BASELINE (Mon-Fri 08:00-18:00)
Mean:                    45,200 connections/hour
Median:                  44,800 connections/hour
95th Percentile:         52,000 connections/hour

OFF-HOURS BASELINE (Mon-Fri 18:00-08:00)
Mean:                    18,500 connections/hour
95th Percentile:         22,000 connections/hour

WEEKEND BASELINE
Mean:                    15,200 connections/hour
95th Percentile:         18,000 connections/hour

ALERT THRESHOLDS
Business Hours:          62,400 connections/hour (52,000 × 1.2)
Off-Hours:               26,400 connections/hour (22,000 × 1.2)
Weekends:                21,600 connections/hour (18,000 × 1.2)

NOTES
- Patch Tuesday (2nd Tuesday) shows +10% connections (Windows updates)
- Baseline includes normal software updates, cloud sync, SaaS traffic
═══════════════════════════════════════════════════════════════
```

---

## 5. Common Pitfalls and How to Avoid Them

**Pitfall 1: "One-Size-Fits-All Baseline"**  
❌ Single threshold for all times → False positives during business hours, missed threats overnight  
✅ Time-aware baselines (business hours, off-hours, weekends)

**Pitfall 2: "Garbage In, Garbage Out"**  
❌ Include incident data in baseline → Inflated thresholds miss future attacks  
✅ Exclude known anomalies, document exclusions

**Pitfall 3: "Set and Forget"**  
❌ Baseline from 2 years ago → Business changed, baseline obsolete  
✅ Quarterly reviews for critical systems, update as needed

**Pitfall 4: "Arbitrary Thresholds"**  
❌ "Alert if >100 failed logins because 100 is a nice round number"  
✅ Data-driven thresholds (95th percentile × multiplier)

**Pitfall 5: "Baseline Without Approval"**  
❌ SOC creates baseline, never consults system owner → Owner disputes alerts  
✅ System owner reviews and approves baseline

**Pitfall 6: "Insufficient Observation Period"**  
❌ 7 days observation → Miss weekly patterns (Monday busy, Friday light)  
✅ 30-90 days observation minimum

**Pitfall 7: "Baseline Without Context"**  
❌ Document numbers without explanation → Future analysts don't understand why  
✅ Document business function, security relevance, rationale

---

**END OF DOCUMENT**

---

*"A baseline without statistics is just a guess with extra steps."* - Anonymous SOC Analyst

*"If your baseline can't distinguish Monday morning from Saturday at 3 AM, you have a problem."* - Probably Feynman

*"The cargo cult approach: We have baselines! (Do they work?) Well, they exist..."* - Every ISMS Auditor's Nightmare