<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.16.3-TG:framework:TG:a.8.16.3 -->
**ISMS-IMP-A.8.16.3-TG - Coverage Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.16: Monitoring Activities

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Coverage Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.16.3-TG |
| **Related Policy** | ISMS-POL-A.8.16 (Monitoring) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.8.16 (Monitoring Activities) |
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

- ISMS-POL-A.8.16 (Monitoring)
- ISMS-IMP-A.8.16.1 (Monitoring Infrastructure Assessment)
- ISMS-IMP-A.8.16.2 (Baseline & Detection Assessment)
- ISMS-IMP-A.8.16.4 (Alert Management & Response Assessment)

---

# Technical Specification
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

---

## Generator Alignment Reference

> Auto-generated from `generate_a816_3_coverage_assessment.py` — DO NOT EDIT MANUALLY.
> Re-generate with: `python3 align_tg_to_scr.py --apply`

**Document ID:** `ISMS-IMP-A.8.16.3`

**Output Filename Pattern:** `{DOCUMENT_ID}_{WORKBOOK_NAME.replace(`

### Sheet Structure

| # | Sheet Name |
|---|-----------|
| 1 | Instructions & Legend |
| 2 | 1. Asset Coverage |
| 3 | 2. Network Coverage |
| 4 | 3. User Identity Coverage |
| 5 | 4. Application Coverage |
| 6 | 5. Gap Analysis |
| 7 | Evidence Register |
| 8 | Summary Dashboard |
| 9 | Approval Sign-Off |

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
| 1 | Asset ID |
| 2 | Asset Name |
| 3 | Asset Type |
| 4 | Operating System |
| 5 | Location |
| 6 | Business Unit |
| 7 | Asset Owner |
| 8 | Data Classification |
| 9 | Criticality |
| 10 | Regulatory Scope |
| 11 | Monitoring Required |
| 12 | Currently Monitored |
| 13 | Log Types Collected |
| 14 | Monitoring Platform |
| 15 | Baseline Established |
| 16 | Detection Rules Active |
| 17 | Last Log Verified |
| 18 | Coverage Status |
| 19 | Gap Reason |
| 20 | Exception Approved |
| 21 | Target Coverage Date |
| 22 | Responsible Party |
| 23 | Notes |
| 24 | Network Segment/Zone |
| 25 | Segment Type |
| 26 | IP Range/CIDR |
| 27 | VLAN ID |
| 28 | Number of Assets |
| 29 | Perimeter Monitoring |
| 30 | Flow Monitoring |
| 31 | DNS Monitoring |
| 32 | Endpoint Monitoring |
| 33 | Log Collection Active |
| 34 | Network Tap/SPAN |
| 35 | Isolation Status |
| 36 | Gaps Identified |
| 37 | Target Date |
| 38 | Identity System |
| 39 | System Type |
| 40 | User Count |
| 41 | Privileged Account Count |
| 42 | Service Account Count |
| 43 | Authentication Logs Collected |
| 44 | Authorisation Logs Collected |
| 45 | Password Change Logs |
| 46 | Privilege Escalation Logs |
| 47 | MFA Events Logged |
| 48 | SSO Events Logged |
| 49 | Failed Login Monitoring |
| 50 | After-Hours Access Monitoring |
| 51 | Geographic Anomaly Detection |
| 52 | User Behaviour Analytics |
| 53 | Privileged Access Monitoring |
| 54 | Gaps/Issues |
| 55 | Priority |
| 56 | Application/Service Name |
| 57 | Application Type |
| 58 | Application Owner |
| 59 | User Base |
| 60 | Application Logs Collected |
| 61 | API Logs Collected |
| 62 | Database Logs Collected |
| 63 | Error/Exception Logging |
| 64 | Transaction Logging |
| 65 | Access Control Logs |
| 66 | Data Export Monitoring |
| 67 | Performance Monitoring |
| 68 | WAF Integration |
| 69 | APM Integration |
| 70 | Gaps |
| 71 | Gap ID |
| 72 | Gap Category |
| 73 | Affected Asset/System |
| 74 | Gap Description |
| 75 | Business Impact |
| 76 | Risk Level |
| 77 | Root Cause |
| 78 | Exception ID |
| 79 | Compensating Controls |
| 80 | Remediation Plan |
| 81 | Remediation Owner |
| 82 | Budget Required |
| 83 | Status |
| 84 | Status Date |
| 85 | Verification Method |
| 86 | Mandatory Monitoring Not Done |
| 87 | Assessment Area |
| 88 | Total Items |
| 89 | Compliant |
| 90 | Partial |
| 91 | Non-Compliant |
| 92 | N/A |
| 93 | Compliance % |
| 94 | Evidence ID |
| 95 | Evidence Type |
| 96 | Description |
| 97 | Location/Path |
| 98 | Date Collected |
| 99 | Collected By |
| 100 | Verification Status |

### Data Validation Values

All dropdown/list values used across sheets:

```
Yes, No, N/A, Partial, Server, Network Device, Security Device, Endpoint
Cloud Resource, Database, Application, Container, IoT Device, Other
Confidential, Internal, Public, Critical, High, Medium, Low, PCI-DSS, HIPAA
GDPR, SOX, Multiple, None, Mandatory, Recommended, Optional
\u2705 Full Coverage, \u26A0\uFE0F Partial Coverage, \u274C No Coverage
Production, DMZ, Management, Guest, Partner, Development, Test, Cloud VPC
Firewall, IDS/IPS, Both, Isolated, Semi-Isolated, Open, Active Directory
Microsoft Entra ID (formerly Azure AD), LDAP, SAML IdP, OAuth Provider
Database Auth, Application-Specific, Web Application, API, Microservice, SaaS
Mobile App, Desktop App, Asset Not Monitored, Log Source Missing
Network Segment Gap, User/Identity Gap, Application Gap, Detection Gap
In Progress, Resolved, Deferred, Accepted, \u2705 Compliant
\u26A0\uFE0F Partial, \u274C Non-Compliant, Yes (EDR), Planned, \u2705 Full
\u274C None, Yes (UEBA), Yes (PAM integrated), Unknown, Pending
Configuration file, Screenshot, Log Export, Documentation, Report
Network scan, Audit log, Compliance report, Verified, Pending verification
Not verified, Requires update, Approved, Approved with Conditions, Rejected
```

**Extracted:** 9 sheets, 100 columns, 96 validation values, 10 colors

---

**END OF SPECIFICATION**


---

*"Mathematical reasoning may be regarded rather schematically as the exercise of a combination of two facilities, which we may call intuition and ingenuity."*
— Alan Turing

<!-- QA_VERIFIED: 2026-02-06 -->
