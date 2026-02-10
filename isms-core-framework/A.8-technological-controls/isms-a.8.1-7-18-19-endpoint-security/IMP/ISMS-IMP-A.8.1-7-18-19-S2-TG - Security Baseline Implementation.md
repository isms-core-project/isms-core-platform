<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.1-7-18-19-S2-TG:framework:TG:a.8.1-7-18-19-s2 -->
**ISMS-IMP-A.8.1-7-18-19-S2-TG - Security Baseline Implementation**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.1: User Endpoint Devices

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.1-7-18-19-S2-TG |
| **Version** | 1.0 |
| **Assessment Area** | Security Baseline Compliance and Enforcement |
| **Related Policy** | ISMS-POL-A.8.1-7-18-19, Section 2.1.3 (Security Baselines), Section 2.1.4 (Encryption), Section 2.1.5 (Endpoint Management) |
| **Purpose** | Document security baseline configurations per endpoint type, assess baseline compliance, verify encryption status, and identify configuration drift to support endpoint device security requirements |
| **Target Audience** | Endpoint Administrators, Security Engineers, IT Operations, Compliance Officers, Configuration Managers, Auditors |
| **Assessment Type** | Technical & Operational |
| **Review Cycle** | Weekly (automated compliance scans), Monthly (manual review) |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial implementation guide for security baseline assessment | ISMS Implementation Team |


---
# Technical Specification


> Auto-generated from `generate_a81-7-18-19_2_protection_coverage.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.8.1-7-18-19.2` |
| **Total Sheets** | 27 (27 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Controls A.8.1, A.8.7, A.8.18, A.8.19: Endpoint Security |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #C00000 | C00000 | Dark Red (Blocked) |
| #C6EFCE | C6EFCE | Light Green (Compliant/Pass) |
| #D9D9D9 | D9D9D9 | Light Gray (Column Headers) |
| #E26B0A | E26B0A | Custom |
| #E7E6E6 | E7E6E6 | Light Gray (Example Rows) |
| #FF6666 | FF6666 | Custom |
| #FFC7CE | FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFF2CC | FFF2CC | Cream (Input Alt) |
| #FFFFCC | FFFFCC | Light Yellow (User Input) |

## Sheet 1: Instructions & Legend

---

## Sheet 2: Coverage_Analysis

---

## Sheet 3: Agent_Status

---

## Sheet 4: Scan_Compliance

---

## Sheet 5: Detection_Metrics

---

## Sheet 6: Incident_Response

---

## Sheet 7: User_Awareness

---

## Sheet 8: Performance_Metrics

---

## Sheet 9: Licensing_Support

---

## Sheet 10: Capability_Requirements

---

## Sheet 11: Evidence_Register

---

## Sheet 12: Gap_Analysis

---

## Sheet 13: Approval_Sign_Off

---

## Sheet 14: Base_Validations

---

## Sheet 15: Instructions

**Data Rows:** 3 (rows 1–3)

### Columns

| Col | Header |
|-----|--------|
| A | Sheet Name |
| B | Description |
| A | Status/Severity |
| B | Meaning |
| C | Color |
| A | Metric |
| B | Target |

---

## Sheet 16: Coverage_Analysis

**Data Rows:** 50 (rows 5–54)

### Columns

| Col | Header |
|-----|--------|
| A | Device ID |
| B | Hostname |
| C | Device Type |
| D | Protection Product |
| E | Agent Version |
| F | Agent Status |
| G | Signature Version |
| H | Signature Date |
| I | Signatures Current |
| J | Last Full Scan |
| K | Last Quick Scan |
| L | Protection Status |
| M | Notes |

---

## Sheet 17: Agent_Status

**Data Rows:** 50 (rows 5–54)

### Columns

| Col | Header |
|-----|--------|
| A | Device ID |
| B | Hostname |
| C | Agent Installed |
| D | Agent Version |
| E | Latest Version |
| F | Agent Outdated |
| G | Last Check-In |
| H | Communication Status |
| I | Deployment Gap Reason |
| J | Notes |

---

## Sheet 18: Scan_Compliance

**Data Rows:** 50 (rows 5–54)

### Columns

| Col | Header |
|-----|--------|
| A | Device ID |
| B | Hostname |
| C | Last Full Scan Date |
| D | Full Scan Status |
| E | Days Since Full Scan |
| F | Full Scan Compliant |
| G | Last Quick Scan Date |
| H | Quick Scan Status |
| I | Days Since Quick Scan |
| J | Quick Scan Compliant |
| K | Notes |

---

## Sheet 19: Detection_Metrics

**Data Rows:** 100 (rows 5–104)

### Columns

| Col | Header |
|-----|--------|
| A | Detection ID |
| B | Detection Date |
| C | Device ID |
| D | Hostname |
| E | Detection Type |
| F | Threat Name |
| G | Severity |
| H | Remediation Status |
| I | Remediation Date |
| J | Remediation Time (Hours) |
| K | Re-Infection |
| L | Notes |

---

## Sheet 20: Incident_Response

**Data Rows:** 50 (rows 5–54)

### Columns

| Col | Header |
|-----|--------|
| A | Incident ID |
| B | Incident Date |
| C | Severity |
| D | Affected Devices |
| E | Incident Type |
| F | Investigation Time (H) |
| G | Investigation SLA |
| H | Containment Time (H) |
| I | Containment SLA |
| J | Remediation Time (H) |
| K | Remediation SLA |
| L | Incident Status |
| M | Post-Incident Review |

---

## Sheet 21: User_Awareness

### Columns

| Col | Header |
|-----|--------|
| A | User |
| B | Department |
| C | Training Assigned |
| D | Training Completed |
| E | Training Status |
| F | Completion Date |
| G | Score |
| H | Notes |
| A | Simulation ID |
| B | Quarter |
| C | Users Targeted |
| D | Emails Delivered |
| E | Links Clicked |
| F | Credentials Submitted |
| G | Reported Phishing |
| H | Click Rate (%) |

---

## Sheet 22: Performance_Metrics

### Columns

| Col | Header |
|-----|--------|
| A | Month |
| B | False Positives |
| C | False Negatives |
| D | FP Rate (%) |
| E | Avg Scan Time (min) |
| F | Performance Complaints |

---

## Sheet 23: Licensing_Support

### Columns

| Col | Header |
|-----|--------|
| A | Product Name |
| B | Vendor |
| C | License Type |
| D | License Count |
| E | Deployed Count |
| F | Support Status |
| G | Support Expiration |
| H | Days Until Expiration |
| I | Annual Cost |
| J | Notes |

---

## Sheet 24: Capability_Requirements

**Data Rows:** 6 (rows 1–6)

### Columns

| Col | Header |
|-----|--------|
| A | Req ID |
| B | Policy Requirement |
| C | Implemented |
| D | Evidence Reference |
| E | Notes |
| F | Status |

---

## Sheet 25: Evidence_Register

**Data Rows:** 100 (rows 5–104)

### Columns

| Col | Header |
|-----|--------|
| A | Evidence ID |
| B | Evidence Type |
| C | Description |
| D | Related Requirement |
| E | Related Worksheet/Device |
| F | File Location |
| G | Collection Date |
| H | Collected By |
| I | Verification Status |
| J | Notes |

---

## Sheet 26: Gap_Analysis

**Data Rows:** 40 (rows 5–44)

### Columns

| Col | Header |
|-----|--------|
| A | Gap ID |
| B | Gap Description |
| C | Affected Devices/Count |
| D | Related Requirement |
| E | Severity |
| F | Risk |
| G | Root Cause |
| H | Remediation Plan |
| I | Owner |
| J | Due Date |
| K | Status |
| L | Budget Required |
| M | Notes |

---

## Sheet 27: Approval_Signoff

---

**END OF SPECIFICATION**

---

*"Any man whose errors take ten years to correct is quite a man."*
— J. Robert Oppenheimer

<!-- QA_VERIFIED: 2026-02-06 -->
