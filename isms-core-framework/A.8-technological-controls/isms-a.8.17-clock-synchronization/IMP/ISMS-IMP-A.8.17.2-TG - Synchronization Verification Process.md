<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.17.2-TG:framework:TG:a.8.17-s2 -->
**ISMS-IMP-A.8.17.2-TG - Synchronization Verification Process & Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.17: Clock Synchronization

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Synchronization Verification Process |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.17.2-TG |
| **Related Policy** | ISMS-POL-A.8.17 (Clock Synchronization) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.8.17 (Clock Synchronization) |
| **Document Creator** | Chief Information Security Officer (CISO) |
| **Document Owner** | CISO |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO | Initial implementation specification |

**Review Cycle**: Quarterly  
**Next Review Date**: [Effective Date + 90 days]

**Related Documents**:

- ISMS-POL-A.8.17 (Clock Synchronization)
- ISMS-IMP-A.8.17.1 (Time Source Configuration)
- ISMS-IMP-A.8.17.3 (Exception Management)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a817_2_sync_status.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.8.17.2`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | System Inventory |
| 3 | Drift Analysis |
| 4 | Gap Analysis |
| 5 | Summary Dashboard |
| 6 | Evidence Register |
| 7 | Approval Sign-Off |

### Color Palette

| Hex Code | Color Name |
|----------|------------|
| #003366 | Dark Blue (Headers) |
| #4472C4 | Medium Blue (Sub-headers) |
| #808080 | Gray (Disabled) |
| #C00000 | Dark Red (Blocked) |
| #C6EFCE | Light Green (Compliant/Pass) |
| #D9D9D9 | Light Gray (Column Headers) |
| #F2F2F2 | Very Light Gray (Alternating Rows) |
| #FFC7CE | Light Red (Non-Compliant/Fail) |
| #FFEB9C | Light Yellow/Amber (Partial) |
| #FFFFCC | Light Yellow (User Input) |

### Column Headers (All Sheets)

| # | Column Header |
|---|--------------|
| 1 | SYSTEM INVENTORY |
| 2 | TIME DRIFT STATISTICAL ANALYSIS |
| 3 | TOTAL Non-Compliant Critical/High |
| 4 | EVIDENCE REGISTER |
| 5 | Assessment Area |
| 6 | Total Items |
| 7 | Compliant |
| 8 | Partial |
| 9 | Non-Compliant |
| 10 | N/A |
| 11 | Compliance % |
| 12 | System Name |
| 13 | Criticality |
| 14 | Sync Status |
| 15 | Drift (ms) |
| 16 | Compliance |
| 17 | Notes |
| 18 | Evidence ID |
| 19 | Evidence Type |
| 20 | Description |
| 21 | Location/Path |
| 22 | Date Collected |
| 23 | Collected By |
| 24 | Verification Status |

### Data Validation Values

All dropdown/list values used across sheets:

```
Server-Physical, Server-Virtual, Server-Cloud, Network Device
Security Appliance, Workstation, Container Host, IoT Device, Other, Critical
High, Medium, Low, NTP Not Configured, NTP Server Unreachable
Excessive Drift (Critical), Excessive Drift (General), Sync Failure
Unknown Status, Excluded System, Draft, Final, Requires remediation
Re-assessment required, Approved, Approved with Conditions, Rejected, Deferred
```

**Extracted:** 7 sheets, 24 columns, 28 validation values, 10 colors

---

**END OF SPECIFICATION**


---

*"The only reason for time is so that everything doesn't happen at once."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
