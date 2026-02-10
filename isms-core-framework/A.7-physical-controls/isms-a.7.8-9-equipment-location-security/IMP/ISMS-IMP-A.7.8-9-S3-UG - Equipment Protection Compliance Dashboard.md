<!-- ISMS-CORE:IMP:ISMS-IMP-A.7.8-9-S3-UG:framework:UG:a.7.8-9-s3 -->
**ISMS-IMP-A.7.8-9-S3-UG - Equipment Protection Compliance Dashboard**
**User Completion Guide**
### ISO/IEC 27001:2022 Controls A.7.8 & A.7.9: Equipment Siting and Protection

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.7.8-9-S3-UG |
| **Version** | 1.0 |
| **Assessment Area** | Consolidated Compliance Dashboard - Equipment Siting (A.7.8) and Off-Premises Security (A.7.9) |
| **Related Policy** | ISMS-POL-A.7.8-9 (Equipment Siting and Protection) |
| **Purpose** | Provide consolidated compliance view across equipment siting and off-premises security, track gaps, and monitor remediation |
| **Target Audience** | CISO, Compliance Officers, Security Management, Internal Audit, Executive Management |
| **Assessment Type** | Management Dashboard |
| **Review Cycle** | Quarterly |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial dashboard specification for Equipment Protection compliance | ISMS Implementation Team |

### Document Structure

This is the **User Completion Guide**. The companion Technical Specification is documented in ISMS-IMP-A.7.8-9-S3-TG.

---

## Dashboard Overview

### Purpose & Scope

**Dashboard Name:** ISMS-IMP-A.7.8-9-S3 - Equipment Protection Compliance Dashboard

#### What This Dashboard Provides

This dashboard consolidates compliance data from the Equipment Siting (A.7.8-9-S1) and Off-Premises Asset Security (A.7.8-9-S2) assessments into a single executive view. It answers:

- What is our overall equipment protection compliance score?
- Which areas have the highest compliance gaps?
- What remediation actions are required?
- How are we trending over time?
- Are we audit-ready?

#### Key Principle

This dashboard **aggregates data from source assessments** - it does not replace detailed assessments. Use S1 (Equipment Siting) and S2 (Off-Premises Assets) for detailed findings; use this dashboard for executive reporting and strategic planning.

#### What the Dashboard Shows

**Overall Compliance Score:**

- Combined score for A.7.8 and A.7.9 compliance
- Colour-coded status (Green >90%, Amber 75-89%, Red <75%)
- Trend over last 4 quarters

**Control Area Scores:**

- Equipment Siting (A.7.8) - locations, environment, security, power
- Off-Premises Security (A.7.9) - authorisation, protection, remote work, permanent installations

**Gap Summary:**

- Critical and high priority gaps requiring attention
- Gap aging (how long gaps have been open)
- Remediation status and target dates

**Incident Metrics:**

- Equipment security incidents (loss, theft, damage)
- Incident trends over time
- Recovery rates

**Audit Readiness:**

- Documentation completeness
- Evidence availability
- Assessment currency

### Who Should Use This Dashboard

#### Primary Users

1. **CISO** - Strategic oversight and resource allocation
2. **Compliance Officers** - Audit preparation and regulatory reporting
3. **Security Management** - Operational monitoring and remediation tracking
4. **Internal Audit** - Control effectiveness assessment
5. **Executive Management** - Risk awareness and governance

#### Use Cases

- **Quarterly Management Review** - Present overall compliance status
- **Audit Preparation** - Identify and close gaps before audit
- **Board Reporting** - High-level security posture reporting
- **Budget Justification** - Support remediation investment requests
- **Trend Analysis** - Track improvement over time

---

## Prerequisites

### Source Assessments Required

This dashboard requires completed assessments:

1. **ISMS-IMP-A.7.8-9-S1** (Equipment Siting Assessment)
   - Equipment location inventory
   - Environmental assessment
   - Physical security evaluation
   - Power infrastructure review
   - Workstation security assessment

2. **ISMS-IMP-A.7.8-9-S2** (Off-Premises Asset Security Assessment)
   - Equipment inventory for off-premises use
   - Authorisation and tracking processes
   - Protection measures assessment
   - Remote working evaluation
   - Permanent installation review
   - Incident documentation

### Data Integration Options

**Option 1: Manual Data Entry**

- Enter summary data from S1 and S2 assessments manually
- Suitable for initial setup or low-volume updates
- Time required: 30-45 minutes per update

**Option 2: External Workbook Links**

- Link to S1 and S2 workbook files
- Automatic data refresh when source files updated
- Requires files in same directory or accessible network location
- Time required: 5-10 minutes per update (verify links)

**Option 3: Automated Data Collection**

- Python script consolidates data from source assessments
- Scheduled execution for regular updates
- Time required: Configuration only, then automatic

---

## Using the Dashboard

### Dashboard Navigation

**Sheet 1: Executive Summary**

- Overall compliance score and trend
- Key metrics at a glance
- Critical alerts and actions required

**Sheet 2: Control Area Details**

- Breakdown by control area (Equipment Siting, Off-Premises)
- Sub-domain scores (Environment, Security, Power, etc.)
- Comparison against targets

**Sheet 3: Gap Register**

- All identified compliance gaps
- Priority, owner, due date, status
- Gap aging and escalation indicators

**Sheet 4: Incident Tracker**

- Equipment security incidents
- Trend analysis
- Lessons learned

**Sheet 5: Remediation Plan**

- Planned remediation actions
- Resource requirements
- Timeline and milestones

**Sheet 6: Audit Readiness**

- Documentation checklist
- Evidence availability
- Assessment currency

**Sheet 7: Trend Analysis**

- Historical compliance scores
- Quarter-over-quarter comparison
- Improvement trajectory

**Sheet 8: Data Input**

- Manual data entry for source assessment results
- OR external workbook link configuration

### Updating the Dashboard

**Quarterly Update Process:**

1. Ensure S1 and S2 assessments are current
2. Update data in Sheet 8 (manual or verify links)
3. Review Sheet 1 for overall score
4. Update gap status in Sheet 3
5. Update incident data in Sheet 4
6. Adjust remediation plan in Sheet 5 as needed
7. Generate reports for management review

---

## Interpreting Metrics

### Overall Compliance Score

**Score Calculation:**

```
Overall Score = (A.7.8 Score x 50%) + (A.7.9 Score x 50%)
```

**Thresholds:**

| Score | Status | Interpretation |
|-------|--------|----------------|
| >90% | Green - Compliant | Meets all requirements, minor improvements only |
| 75-89% | Amber - Partial | Most requirements met, remediation needed |
| 60-74% | Amber - Attention | Significant gaps, prioritised remediation required |
| <60% | Red - Non-Compliant | Major gaps, immediate action required |

### Control Area Scores

**A.7.8 Equipment Siting Score Components:**

| Component | Weight | Source |
|-----------|--------|--------|
| Equipment Locations | 25% | S1 Sheet 2 |
| Environmental Assessment | 25% | S1 Sheet 3 |
| Physical Security | 25% | S1 Sheet 4 |
| Power Infrastructure | 15% | S1 Sheet 5 |
| Workstation Security | 10% | S1 Sheet 6 |

**A.7.9 Off-Premises Security Score Components:**

| Component | Weight | Source |
|-----------|--------|--------|
| Equipment Inventory | 20% | S2 Sheet 2 |
| Authorisation & Tracking | 20% | S2 Sheet 3 |
| Protection Measures | 25% | S2 Sheet 4 |
| Remote Working | 20% | S2 Sheet 5 |
| Permanent Installations | 15% | S2 Sheet 6 |

### Gap Priority Levels

| Priority | Definition | Target Remediation |
|----------|------------|-------------------|
| Critical | Significant risk of data breach or regulatory non-compliance | 30 days |
| High | Material gap that could impact audit outcome | 60 days |
| Medium | Process improvement opportunity | 90 days |
| Low | Minor enhancement or documentation improvement | 180 days |

### Incident Metrics

**Key Metrics:**

- **Loss Rate**: Equipment losses per 1,000 devices per year
- **Recovery Rate**: Percentage of lost devices recovered
- **Mean Time to Report**: Average hours from incident to report
- **Remote Wipe Success Rate**: Percentage of successful remote wipes

---

## Gap Management

### Gap Identification

Gaps are identified from:

1. Non-compliant items in S1 and S2 assessments (Red status)
2. Partial compliance items requiring attention (Amber status)
3. Audit findings and recommendations
4. Incident root cause analysis
5. Policy changes requiring implementation

### Gap Register Fields

| Field | Description |
|-------|-------------|
| Gap ID | Unique identifier (GAP-001, GAP-002) |
| Control Area | A.7.8 or A.7.9 |
| Sub-domain | Specific area (Environment, Security, Remote Work, etc.) |
| Description | Clear description of the gap |
| Risk Impact | Business impact if gap not addressed |
| Priority | Critical, High, Medium, Low |
| Owner | Person responsible for remediation |
| Target Date | Planned completion date |
| Status | Open, In Progress, Completed, Deferred |
| Evidence | Documentation that gap has been closed |

### Gap Remediation Workflow

```
1. GAP IDENTIFIED
   |
2. PRIORITY ASSIGNED (based on risk)
   |
3. OWNER ASSIGNED
   |
4. REMEDIATION PLAN DEVELOPED
   |
5. IMPLEMENTATION
   |
6. VERIFICATION
   |
7. GAP CLOSED
   |
8. EVIDENCE DOCUMENTED
```

### Gap Escalation

**Escalation Triggers:**

- Gap past target date by >30 days
- Critical gap open >60 days
- High gap open >90 days
- Resource constraints blocking remediation

**Escalation Path:**

- Day 30 overdue: Notify gap owner and their manager
- Day 60 overdue: Escalate to CISO
- Day 90 overdue: Escalate to Executive Management

---

## Reporting

### Standard Reports

**1. Executive Summary Report**

- Audience: Executive Management, Board
- Frequency: Quarterly
- Content: Overall score, key metrics, critical gaps, remediation progress

**2. Compliance Status Report**

- Audience: CISO, Compliance Officers
- Frequency: Monthly
- Content: Detailed scores by control area, gap status, incident summary

**3. Gap Remediation Report**

- Audience: Security Management, IT Operations
- Frequency: Weekly/Monthly
- Content: Open gaps, status updates, resource requirements

**4. Audit Readiness Report**

- Audience: Compliance Officers, Internal Audit
- Frequency: Pre-audit
- Content: Documentation completeness, evidence availability, gap closure status

### Report Generation

**From Dashboard:**

1. Navigate to relevant sheet
2. Apply filters if needed
3. Print or export to PDF

**Automated Reports:**

- Configure Python script for scheduled report generation
- Email distribution to stakeholders

---

**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
