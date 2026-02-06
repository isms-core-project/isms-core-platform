**ISMS-IMP-A.6.7-8.S5-TG - Remote Working and Event Reporting Compliance Dashboard**
**Technical Specification**
### ISO/IEC 27001:2022 Controls A.6.7 (Remote Working) & A.6.8 (Information Security Event Reporting)

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.6.7-8.S5-TG |
| **Version** | 1.0 |
| **Assessment Area** | Consolidated Compliance Metrics and Executive Reporting |
| **Related Policy** | ISMS-POL-A.6.7-8 (All Sections) |
| **Purpose** | Consolidate compliance data from S1-S4 assessments into executive dashboard |
| **Target Audience** | CISO, IT Security Manager, Executive Management, Auditors |
| **Assessment Type** | Consolidation Dashboard |
| **Review Cycle** | Quarterly (or as S1-S4 are updated) |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial specification for compliance dashboard | ISMS Implementation Team |

---

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.6.7-8.S5-UG.

---

# Technical Specification

**Audience:** Workbook Developers (Python/Excel Script Maintainers)

---

## 8. Workbook Architecture

### 8.1 Sheet Structure

| Sheet Name | Purpose | Sheet Type |
|------------|---------|------------|
| Instructions | User guidance | Static |
| Executive_Summary | Executive overview | Summary |
| Metrics_Import | Data import from S1-S4 | Import |
| Control_Compliance | Detailed compliance | Analysis |
| Gap_Consolidation | Consolidated gaps | Analysis |
| Trend_Analysis | Trend tracking | Analysis |
| Risk_Assessment | Risk-based view | Analysis |
| SoA_Integration | SoA mapping | Integration |
| Audit_Summary | Audit support | Summary |
| Evidence_Index | Evidence master list | Register |
| Dashboard | Visual dashboard | Calculated |
| Approval_Sign_Off | Formal approvals | Governance |

### 8.2 Data Dependencies

```
S1 Workbook ──┐
S2 Workbook ──┼──→ Metrics_Import ──→ Control_Compliance
S3 Workbook ──┤                   └──→ Dashboard
S4 Workbook ──┘                   └──→ Executive_Summary

S1 Gap_Analysis ──┐
S2 Gap_Analysis ──┼──→ Gap_Consolidation ──→ Risk_Assessment
S3 Gap_Analysis ──┤
S4 Gap_Analysis ──┘

Historical Data ──→ Trend_Analysis
```

## 9. Column Specifications

### 9.1 Metrics_Import Sheet

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Source Workbook | 12 | Dropdown | S1/S2/S3/S4 |
| B | Metric Name | 40 | Text | Free text |
| C | Metric Value | 15 | Number | Percentage or number |
| D | Target Value | 15 | Number | Percentage or number |
| E | Compliant | 12 | Formula | =C>=D |
| F | Assessment Date | 15 | Date | Date format |
| G | Source Cell | 15 | Text | Cell reference |
| H | Notes | 40 | Text | Free text |

### 9.2 Gap_Consolidation Sheet

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Gap ID | 15 | Text | From source |
| B | Source | 8 | Dropdown | S1/S2/S3/S4 |
| C | Gap Description | 50 | Text | Free text |
| D | Risk Level | 12 | Dropdown | High/Medium/Low |
| E | Remediation Action | 50 | Text | Free text |
| F | Owner | 20 | Text | Free text |
| G | Target Date | 12 | Date | Date format |
| H | Status | 15 | Dropdown | Open/In Progress/Closed |
| I | Days Open | 12 | Formula | =TODAY()-[Created Date] |
| J | Overdue | 10 | Formula | =AND(G<TODAY(),H<>"Closed") |

## 10. Formula Specifications

### 10.1 Overall Compliance Calculation

**Weighted Average**:
```
Overall = (S1_Compliance * 0.20) + (S2_Compliance * 0.30) +
          (S3_Compliance * 0.30) + (S4_Compliance * 0.20)
```

Weights reflect relative importance:
- S1 (Authorization): 20%
- S2 (Technical): 30%
- S3 (Endpoint/Physical): 30%
- S4 (Event Reporting): 20%

### 10.2 Control-Level Compliance

**A.6.7 Compliance**:
```
= AVERAGE(S1_Compliance, S2_Compliance, S3_Compliance)
```

**A.6.8 Compliance**:
```
= S4_Compliance
```

### 10.3 Gap Metrics

**Open Gaps by Severity**:
```
High: =COUNTIFS(Gap_Consolidation!D:D,"High",Gap_Consolidation!H:H,"<>Closed")
Medium: =COUNTIFS(Gap_Consolidation!D:D,"Medium",Gap_Consolidation!H:H,"<>Closed")
Low: =COUNTIFS(Gap_Consolidation!D:D,"Low",Gap_Consolidation!H:H,"<>Closed")
```

**Overdue Gaps**:
```
=COUNTIF(Gap_Consolidation!J:J,TRUE)
```

## 11. Visualization Specifications

### 11.1 Gauge Charts

**Compliance Gauges**:
- Red zone: 0-79%
- Yellow zone: 80-94%
- Green zone: 95-100%
- Needle position based on current value

### 11.2 Trend Chart

**Line Chart Configuration**:
- X-axis: Assessment periods
- Y-axis: Compliance percentage (0-100%)
- Series: Overall, S1, S2, S3, S4
- Target line at 95%

### 11.3 Gap Distribution

**Pie Chart**:
- Segments: High, Medium, Low (by count)
- Colors: Red, Yellow, Green

## 12. Pre-Populated Content

### 12.1 Metrics to Import

| Source | Metric | Target |
|--------|--------|--------|
| S1 | Authorization Compliance Rate | ≥95% |
| S1 | Policy Framework Score | ≥90% |
| S2 | VPN Compliance Score | 100% |
| S2 | MFA Coverage | 100% |
| S2 | MFA Enforcement Rate | ≥98% |
| S2 | Encryption Compliance | 100% |
| S3 | Encryption Status | 100% |
| S3 | Endpoint Protection Coverage | ≥98% |
| S3 | Patch Compliance Rate | ≥95% |
| S3 | Physical Security Compliance | ≥90% |
| S4 | Channel Accessibility | 100% |
| S4 | Response SLA Compliance | ≥90% |
| S4 | Awareness Coverage | ≥95% |

### 12.2 SoA Mapping

| Control | Name | Assessment Source |
|---------|------|-------------------|
| A.6.7 | Remote Working | S1, S2, S3 |
| A.6.8 | Information Security Event Reporting | S4 |

---

## END OF SPECIFICATION

---

*"What gets measured gets managed."*
— Peter Drucker

<!-- QA_VERIFIED: 2026-02-06 -->
