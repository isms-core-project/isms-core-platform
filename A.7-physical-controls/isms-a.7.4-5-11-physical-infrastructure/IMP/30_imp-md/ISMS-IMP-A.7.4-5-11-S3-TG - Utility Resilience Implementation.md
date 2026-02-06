**ISMS-IMP-A.7.4-5-11-S3-TG - Utility Resilience Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.7.4: Physical Security Monitoring

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.7.4-5-11-S3-TG |
| **Version** | 1.0 |
| **Assessment Area** | Utility Resilience - Power (UPS/Generators), HVAC, Telecommunications (ISP) |
| **Related Policy** | ISMS-POL-A.7.4-5-11, Section 4 (Utility Resilience Requirements) |
| **Purpose** | Document deployed utility resilience infrastructure, assess capabilities against policy requirements, and identify gaps |
| **Target Audience** | Facilities Management, Electricians, HVAC Technicians, IT Operations, Network Engineers, Compliance Officers, Auditors |
| **Assessment Type** | Technical & Operational |
| **Review Cycle** | Quarterly or After Major Infrastructure Changes |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Utility Resilience assessment workbook | ISMS Implementation Team |

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.7.4-5-11-S3-UG.

---

# Technical Specification

## Excel Workbook Structure

### Workbook Overview

**File Name:** ISMS-IMP-A.7.4.3_Utility_Resilience_YYYYMMDD.xlsx

**Generation:** Automated via Python script (generate_a74_3_utility_resilience.py)

**Sheet Count:** 7 worksheets

**Data Capacity:** 100 data rows per assessment sheet (Sheets 2-4)

**Styling:** Navy blue headers, yellow input cells, conditional formatting (green/amber/red)

### Sheet Organization

| Sheet # | Sheet Name | Purpose | Type | Row Count |
|---------|------------|---------|------|-----------|
| 1 | Instructions & Legend | Assessment metadata and status legend | Read-only | ~30 rows |
| 2 | Power Infrastructure | UPS, generators, power redundancy inventory | Data Entry | 100 data rows |
| 3 | HVAC | HVAC units, cooling capacity, redundancy assessment | Data Entry | 100 data rows |
| 4 | Telecommunications | ISP circuits, bandwidth, diverse paths, failover | Data Entry | 100 data rows |
| 5 | Summary Dashboard | Automated compliance scoring and metrics | Formula-driven | ~40 rows |
| 6 | Evidence Register | Supporting evidence documentation | Data Entry | 100 data rows |
| 7 | Approval Sign-Off | Four-level approval workflow | Data Entry | ~20 rows |

---

## Sheet-by-Sheet Specifications

### Sheet 2: Power Infrastructure

**Columns:**

| Col | Field Name | Type | Width | Validation | Formula | Description |
|-----|------------|------|-------|------------|---------|-------------|
| A | Facility/System Name | Text | 25 | None | No | Facility or building name |
| B | UPS Vendor/Model | Text | 30 | None | No | UPS make and model |
| C | UPS Capacity (kVA) | Number | 15 | Float >0 | No | UPS nameplate capacity |
| D | UPS Runtime (Minutes) | Number | 15 | Integer >0 | No | Runtime at current/full load |
| E | UPS Redundancy | Dropdown | 15 | List | No | N / N+1 / 2N / None |
| F | Backup Generator | Dropdown | 15 | List | No | Yes / No / N/A |
| G | Generator Capacity (kW) | Number | 15 | Float >0 | No | Generator capacity (if Yes) |
| H | Generator Runtime (Hours) | Number | 15 | Integer >0 | No | Hours of runtime at full load |
| I | Generator Fuel Type | Dropdown | 15 | List | No | Diesel / Natural Gas / Propane / N/A |
| J | Last UPS Test Date | Date | 15 | Date | No | Last quarterly UPS load test |
| K | Last Generator Test Date | Date | 18 | Date | No | Last monthly generator exercise |
| L | Power Monitoring | Dropdown | 18 | List | No | Yes - Real-time / Partial / No |
| M | Compliance Status | Formula | 18 | None | Yes | ✅ / ⚠️ / ❌ |
| N | Notes | Text | 50 | None | No | Additional context |

**Compliance Status Formula (Column M):**
```excel
=IF(AND(D2>=15, F2="Yes", E2<>"N", (TODAY()-J2)<=90, (TODAY()-K2)<=30), "✅ Compliant",
   IF(OR(D2<5, E2="None", (TODAY()-J2)>180, (TODAY()-K2)>60), "❌ Non-Compliant",
   "⚠️ Partial"))
```

**Logic:**

- ✅ Compliant IF: Runtime ≥15 min AND generator present AND redundancy configured AND UPS test within 90 days AND generator test within 30 days
- ❌ Non-Compliant IF: Runtime <5 min OR no redundancy OR testing >180/60 days overdue
- ⚠️ Partial: Everything else

**Conditional Formatting:**

- Column M: Green/Amber/Red based on status
- Column D: Red if <5 minutes (insufficient runtime)
- Column J: Red if (TODAY()-J2)>90 (UPS test overdue)
- Column K: Red if (TODAY()-K2)>30 (generator test overdue)

### Sheet 3: HVAC

**Columns:**

| Col | Field Name | Type | Width | Validation | Formula | Description |
|-----|------------|------|-------|------------|---------|-------------|
| A | Facility/System Name | Text | 25 | None | No | Facility or zone name |
| B | HVAC Vendor/Model | Text | 30 | None | No | HVAC make and model |
| C | HVAC Unit Count | Number | 12 | Integer >0 | No | Number of HVAC units |
| D | Cooling Capacity (kW) | Number | 15 | Float >0 | No | Total cooling capacity |
| E | Current Heat Load (kW) | Number | 15 | Float >0 | No | Actual heat load (IT equipment) |
| F | Capacity Margin (%) | Formula | 15 | None | Yes | (Capacity - Load) / Load × 100 |
| G | HVAC Redundancy | Dropdown | 15 | List | No | N / N+1 / 2N / None |
| H | Temperature Monitoring | Dropdown | 18 | List | No | Yes - Real-time / Partial / No |
| I | HVAC Monitoring | Dropdown | 15 | List | No | Yes - BMS / Yes - Manual / No |
| J | Last HVAC Maintenance | Date | 18 | Date | No | Last maintenance date |
| K | Compliance Status | Formula | 18 | None | Yes | ✅ / ⚠️ / ❌ |
| L | Notes | Text | 50 | None | No | Additional context |

**Capacity Margin Formula (Column F):**
```excel
=IF(AND(D2>0, E2>0), (D2-E2)/E2*100, "")
```

**Compliance Status Formula (Column K):**
```excel
=IF(AND(F2>=20, G2<>"None", H2="Yes - Real-time", (TODAY()-J2)<=365), "✅ Compliant",
   IF(OR(F2<10, G2="None", H2="No", (TODAY()-J2)>547), "❌ Non-Compliant",
   "⚠️ Partial"))
```

**Logic:**

- ✅ Compliant IF: Margin ≥20% AND redundancy configured AND real-time monitoring AND maintenance within 365 days
- ❌ Non-Compliant IF: Margin <10% OR no redundancy OR no monitoring OR maintenance >18 months overdue
- ⚠️ Partial: Everything else

### Sheet 4: Telecommunications

**Columns:**

| Col | Field Name | Type | Width | Validation | Formula | Description |
|-----|------------|------|-------|------------|---------|-------------|
| A | Facility/System Name | Text | 25 | None | No | Facility name |
| B | Primary ISP | Text | 30 | None | No | ISP name and circuit type |
| C | Primary Bandwidth (Mbps) | Number | 15 | Integer >0 | No | Contracted bandwidth |
| D | Secondary ISP | Text | 30 | None | No | ISP name or "None" |
| E | Secondary Bandwidth (Mbps) | Number | 15 | Integer ≥0 | No | Bandwidth (0 if none) |
| F | Diverse Path Verified | Dropdown | 25 | List | No | Yes - Different carriers + paths / Partial / No / N/A |
| G | Failover Configuration | Dropdown | 20 | List | No | Automatic - BGP / Manual / None / N/A |
| H | Last Failover Test | Date | 18 | Date | No | Last quarterly failover test |
| I | ISP Monitoring | Dropdown | 18 | List | No | Yes - Real-time / Partial / No |
| J | Compliance Status | Formula | 18 | None | Yes | ✅ / ⚠️ / ❌ |
| K | Notes | Text | 50 | None | No | Additional context |

**Compliance Status Formula (Column J):**
```excel
=IF(AND(D2<>"None", F2="Yes - Different carriers + paths", (TODAY()-H2)<=90), "✅ Compliant",
   IF(OR(D2="None", F2="No"), "❌ Non-Compliant",
   "⚠️ Partial"))
```

**Logic:**

- ✅ Compliant IF: Dual ISP AND diverse paths verified AND failover tested within 90 days
- ❌ Non-Compliant IF: Single ISP (for Tier 1 critical facilities) OR no diverse paths
- ⚠️ Partial: Everything else

### Sheet 5: Summary Dashboard

**Overall Compliance Score Formula:**
```excel
=(COUNTIF('Power Infrastructure'!M:M,"✅ Compliant")/COUNTA('Power Infrastructure'!M:M)*0.4 +
  COUNTIF(HVAC!K:K,"✅ Compliant")/COUNTA(HVAC!K:K)*0.3 +
  COUNTIF(Telecommunications!J:J,"✅ Compliant")/COUNTA(Telecommunications!J:J)*0.3)*100
```

**Weighting:** Power 40%, HVAC 30%, Telecom 30%

---

## Cell Styling Reference

### Color Palette

**Headers:** #003366 (Navy blue), #FFFFFF (White text)
**Input Cells:** #FFFFCC (Light yellow)
**Compliant:** #C6EFCE (Light green)
**Partial:** #FFEB9C (Light amber)
**Non-Compliant:** #FFC7CE (Light red)

### Font Specifications

**Headers:** Calibri 14pt Bold (primary), 11pt Bold (sub), 10pt Bold (column)
**Data:** Calibri 10pt Normal
**Status:** Calibri 10pt Bold with Unicode symbols (✅ U+2705, ⚠️ U+26A0, ❌ U+274C)

---

## Integration Points

### Integration with Policy (ISMS-POL-A.7.4-5-11)

| Policy Section | Assessment Sheet | Assessment Focus |
|----------------|------------------|------------------|
| Section 4.1: Power Supply Resilience | Sheet 2: Power Infrastructure | UPS, generators, redundancy, testing |
| Section 4.2: HVAC and Cooling | Sheet 3: HVAC | Cooling capacity, redundancy, monitoring, maintenance |
| Section 4.3: Telecommunications | Sheet 4: Telecommunications | ISP redundancy, diverse paths, failover, testing |
| Section 4.5: Utility Monitoring | All Sheets | Monitoring coverage, alerting, dashboards |
| Section 4.6: Utility Failure Testing | Sheets 2-4 | UPS testing, generator testing, ISP failover testing |

### Integration with Other Assessments

**Feeds into:**

- ISMS-IMP-A.7.4-5-11-S4 (Compliance Dashboard)

**Shared with:**

- ISMS-IMP-A.7.4-5-11-S2 (Environmental Protection) - HVAC systems documented in both

### Integration with Audit Process

**Audit Deliverables:**
1. Assessment Workbook (all sheets)
2. Evidence Folder (UPS screenshots, testing logs, ISP SLAs)
3. Approval Documentation (Sheet 7)
4. Gap Remediation Plan

**Auditor Review:**
1. Review Summary Dashboard
2. Verify UPS runtime calculations
3. Verify generator testing current
4. Verify ISP diverse paths
5. Spot-check evidence
6. Physical facility inspection (verify UPS/generator exist)

**Audit Questions Anticipated:**

- "How do you know UPS runtime is 15 minutes?" → Evidence: UPS web interface screenshot showing runtime
- "Is generator tested monthly?" → Evidence: Testing logs showing monthly exercise tests
- "Are ISP paths truly diverse?" → Evidence: ISP diverse path documentation from carriers
- "What was UPS performance during last power outage?" → Utility failure event documentation

---

**END OF SPECIFICATION**

---

*"The best way to send information is to wrap it up in a person."*
— J. Robert Oppenheimer

<!-- QA_VERIFIED: 2026-02-06 -->
