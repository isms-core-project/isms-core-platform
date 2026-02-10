<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.20-21-22.S4-TG:framework:TG:a.8.20-21-22 -->
**ISMS-IMP-A.8.20-21-22.S4-TG - Network Services Security Process**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.20: Networks Security

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.20-21-22-S4-TG |
| **Version** | 1.0 |
| **Assessment Area** | Network Services Security Implementation |
| **Related Policy** | ISMS-POL-A.8.20-21-22, Section 2.2 (Network Services Security - A.8.21), Section 2.1 (Network Infrastructure Security - A.8.20) |
| **Purpose** | Provide service-specific security implementation guidance for critical network services (DNS, DHCP, NTP, proxy, load balancers, authentication services) including hardening, monitoring, and redundancy |
| **Target Audience** | Network Administrators, System Administrators, Security Engineers, IT Operations, Service Owners, Auditors |
| **Assessment Type** | Service Security Configuration & Availability Assessment |
| **Review Cycle** | Quarterly or After Service Configuration Changes |
| **Total Sheets** | 11 |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial implementation guidance for network services security | ISMS Implementation Team |

---
# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers


> Auto-generated from `generate_a820_4_segmentation_matrix.py`
> Re-generate with: `python3 generate_tg_from_scr.py --apply`

## Workbook Overview

| Property | Value |
|----------|-------|
| **Document ID** | `ISMS-IMP-A.8.20-21-22.S4` |
| **Output Filename** | `ISMS-IMP-A.8.20-21-22.S4_Network_Segmentation_Matrix_YYYYMMDD.xlsx` |
| **Workbook Title** | Network Segmentation Matrix & Assessment |
| **Total Sheets** | 12 (12 visible) |
| **Control Reference** | ISO/IEC 27001:2022 - Controls A.8.20, A.8.21, A.8.22: Network Security |

## Color Palette

| Hex Code | Style Name | Description |
|----------|-----------|-------------|
| #002060 | 002060 | Custom |
| #003366 | 003366 | Dark Blue (Headers) |
| #006100 | 006100 | Dark Green (Pass) |
| #4472C4 | 4472C4 | Medium Blue (Sub-headers) |
| #92D050 | 92D050 | Green (Complete) |
| #9C0006 | 9C0006 | Dark Red (Error) |
| #C6EFCE | C6EFCE | Light Green (Compliant/Pass) |
| #D9D9D9 | D9D9D9 | Light Gray (Column Headers) |
| #E7E6E6 | E7E6E6 | Light Gray (Example Rows) |
| #FF0000 | FF0000 | Red (Critical/Alert) |
| #FFC000 | FFC000 | Custom |
| #FFC7CE | FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFFF00 | FFFF00 | Yellow (Warning) |
| #FFFFCC | FFFFCC | Light Yellow (User Input) |

## Sheet 1: Data_Validations

---

## Sheet 2: Instructions & Guide

---

## Sheet 3: Security_Zones_Inventory

**Data Rows:** 11 (rows 2–12) | **Frozen Panes:** A4

### Columns

| Col | Header |
|-----|--------|
| A | Zone ID |
| B | Zone Name |
| C | Purpose |
| D | Trust Level |
| E | Networks/Subnets |
| F | VLANs |
| G | Segmentation Type |
| H | Devices Count |
| I | Critical Assets |
| J | Internet Access |
| K | Owner |
| L | Notes |

---

## Sheet 4: Segmentation_Matrix

**Data Rows:** 10 (rows 2–11) | **Frozen Panes:** A5

### Columns

| Col | Header |
|-----|--------|
| A | Rule ID |
| B | Source Zone |
| C | Destination Zone |
| D | Traffic Action |
| E | Protocols/Ports |
| F | Justification |
| G | Firewall Enforced |
| H | ACL Enforced |
| I | Monitoring |
| J | Last Reviewed |
| K | Notes |

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| DN:DN | equal  |  |
| DN:DN | equal  |  |

---

## Sheet 5: VLAN_Inventory

**Data Rows:** 10 (rows 1–10) | **Frozen Panes:** A4

### Columns

| Col | Header |
|-----|--------|
| A | VLAN ID |
| B | VLAN Name |
| C | Security Zone |
| D | IP Subnet |
| E | Purpose |
| F | Devices/Ports |
| G | Trunk Allowed |
| H | Native VLAN |
| I | Last Reviewed |
| J | Notes |

---

## Sheet 6: Firewall_Rules_Assessment

**Data Rows:** 12 (rows 2–13) | **Frozen Panes:** A4

### Columns

| Col | Header |
|-----|--------|
| A | Rule ID |
| B | Firewall |
| C | Rule Number |
| D | Source Zone |
| E | Destination Zone |
| F | Source IP/Network |
| G | Destination IP/Network |
| H | Service/Port |
| I | Action |
| J | Review Status |
| K | Last Modified |
| L | Reviewed By |
| M | Notes |

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| IN:IN | equal  |  |
| IN:IN | equal  |  |

---

## Sheet 7: ACL_Assessment

**Data Rows:** 11 (rows 2–12) | **Frozen Panes:** A4

### Columns

| Col | Header |
|-----|--------|
| A | ACL ID |
| B | Device |
| C | ACL Name/Number |
| D | Interface |
| E | Direction |
| F | Purpose |
| G | Zones Protected |
| H | Review Status |
| I | Effectiveness |
| J | Last Modified |
| K | Reviewed By |
| L | Notes |

---

## Sheet 8: Segmentation_Testing

**Data Rows:** 10 (rows 2–11) | **Frozen Panes:** A4

### Columns

| Col | Header |
|-----|--------|
| A | Test ID |
| B | Test Name |
| C | Source Zone |
| D | Destination Zone |
| E | Expected Result |
| F | Actual Result |
| G | Test Result |
| H | Test Method |
| I | Test Date |
| J | Tested By |
| K | Notes |

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| GN:GN | equal  |  |
| GN:GN | equal  |  |

---

## Sheet 9: Gap_Analysis

**Data Rows:** 9 (rows 2–10) | **Frozen Panes:** A4

### Columns

| Col | Header |
|-----|--------|
| A | Gap ID |
| B | Gap Type |
| C | Location/Zone |
| D | Description |
| E | Risk |
| F | Severity |
| G | Remediation Plan |
| H | Owner |
| I | Status |
| J | Target Date |

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| FN:FN | equal  |  |
| FN:FN | equal  |  |
| FN:FN | equal  |  |
| FN:FN | equal  |  |

---

## Sheet 10: Compliance_Summary

---

## Sheet 11: Segmentation Test Results

---

## Sheet 12: Remediation_Roadmap

**Data Rows:** 7 (rows 2–8) | **Frozen Panes:** A4

### Columns

| Col | Header |
|-----|--------|
| A | Priority |
| B | Severity |
| C | Improvement |
| D | Affected Zones |
| E | Remediation Action |
| F | Owner |
| G | Target Date |
| H | Status |

### Conditional Formatting

| Range | Condition | Format |
|-------|-----------|--------|
| BN:BN | equal  |  |
| BN:BN | equal  |  |
| BN:BN | equal  |  |

---

## Data Validation Dropdown Lists

All dropdown value lists defined in the generator:

| Variable | Values |
|----------|--------|
| `COMMON_ZONES` | Internet/DMZ, Internal, Management, Datacenter, Guest, Branch, Cloud |

---

**END OF SPECIFICATION**

---

*"People are always selling the idea that people with mental illness are suffering. I think madness can be an escape."*
— John Nash

<!-- QA_VERIFIED: 2026-02-06 -->
