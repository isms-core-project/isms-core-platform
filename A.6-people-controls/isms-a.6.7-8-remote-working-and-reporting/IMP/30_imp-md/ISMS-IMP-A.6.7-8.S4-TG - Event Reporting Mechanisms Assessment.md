**ISMS-IMP-A.6.7-8.S4-TG - Event Reporting Mechanisms Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Controls A.6.7 (Remote Working) & A.6.8 (Information Security Event Reporting)

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.6.7-8.S4-TG |
| **Version** | 1.0 |
| **Assessment Area** | Security Event Reporting Channels, Procedures, and Effectiveness |
| **Related Policy** | ISMS-POL-A.6.7-8, Section 3 (Security Event Reporting Requirements) |
| **Purpose** | Guide users through assessment of security event reporting mechanisms and their effectiveness |
| **Target Audience** | IT Security Team, Security Operations, Help Desk, Auditors |
| **Assessment Type** | Operational |
| **Review Cycle** | Semi-Annual |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial specification for event reporting assessment | ISMS Implementation Team |

---

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.6.7-8.S4-UG.

---

# Technical Specification

**Audience:** Workbook Developers (Python/Excel Script Maintainers)

---

## 8. Workbook Architecture

### 8.1 Sheet Structure

| Sheet Name | Purpose | Sheet Type |
|------------|---------|------------|
| Instructions | User guidance | Static |
| Reporting_Channels | Channel inventory | Inventory |
| Channel_Accessibility | Accessibility testing | Assessment |
| Reporting_Procedures | Procedure documentation | Assessment |
| Event_Categories | Category definitions | Assessment |
| Awareness_Assessment | Awareness verification | Assessment |
| Response_Sampling | Report sampling | Sample Testing |
| NonBlame_Culture | Culture assessment | Assessment |
| Integration_Assessment | A.5.24-28 integration | Assessment |
| Gap_Analysis | Consolidated gaps | Analysis |
| Evidence_Register | Evidence catalog | Register |
| Dashboard | Executive summary | Calculated |
| Approval_Sign_Off | Formal approvals | Governance |

## 9. Column Specifications

### 9.1 Reporting_Channels Sheet

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Channel ID | 12 | Text | Auto (CH-###) |
| B | Channel Name | 25 | Text | Free text |
| C | Channel Type | 15 | Dropdown | Email/Phone/Web Form/Chat/Ticketing/Other |
| D | Contact Details | 30 | Text | Free text |
| E | Availability | 15 | Dropdown | 24/7/Business Hours |
| F | Remote Accessible | 12 | Dropdown | Yes/No |
| G | Primary Use | 30 | Text | Free text |
| H | Owner | 20 | Text | Free text |
| I | Published | 12 | Dropdown | Yes/No |
| J | Status | 12 | Dropdown | Active/Inactive |

### 9.2 Response_Sampling Sheet

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Sample ID | 12 | Text | Auto (EVT-###) |
| B | Report Date | 12 | Date | Date format |
| C | Event Category | 20 | Dropdown | Category list |
| D | Reported Via | 15 | Reference | Channel ID |
| E | Reporter Location | 12 | Dropdown | Office/Remote/Travel |
| F | Acknowledged | 10 | Dropdown | Yes/No |
| G | Ack Time | 15 | Text | Free text |
| H | Ack SLA Met | 12 | Dropdown | Yes/No |
| I | Feedback Provided | 12 | Dropdown | Yes/No |
| J | Escalated | 12 | Dropdown | Yes/No/N/A |
| K | Documented | 12 | Dropdown | Yes/No |
| L | Compliant | 12 | Formula | =AND(F="Yes",H="Yes",K="Yes") |
| M | Notes | 40 | Text | Free text |

## 10. Formula Specifications

### 10.1 Dashboard Calculations

**Channel Compliance Rate**:
```
=COUNTIF(Reporting_Channels!F:F,"Yes")/COUNTA(Reporting_Channels!F2:F50)
```

**Response SLA Compliance**:
```
=COUNTIF(Response_Sampling!H:H,"Yes")/COUNTA(Response_Sampling!H2:H100)
```

**Awareness Coverage**:
```
=COUNTIF(Awareness_Assessment!B:B,"Yes")/COUNTA(Awareness_Assessment!B2:B20)
```

## 11. Pre-Populated Content

### 11.1 Procedure Elements

| Element | Requirement |
|---------|-------------|
| Event Definition | Clear definition of what constitutes a security event |
| Event Categories | Categories of reportable events with examples |
| Reporting Channels | How to reach each reporting channel |
| Report Content | What information to include in reports |
| Timeliness | When to report (timeframes by severity) |
| Prohibitions | What NOT to do (don't test, don't investigate) |
| Acknowledgment | What response to expect |
| Feedback | How and when feedback will be provided |
| Anonymity | Options for anonymous reporting |
| Escalation | When and how events escalate |

### 11.2 Event Categories

| Category | Example Events |
|----------|----------------|
| Phishing/Social Engineering | Suspicious emails, SMS, calls requesting credentials |
| Malware/System Compromise | Unexpected behavior, ransomware notes, suspicious processes |
| Unauthorized Access | Unknown logins, unexpected privilege changes |
| Data Breach/Exposure | Misdirected emails, exposed data, unauthorized sharing |
| Lost/Stolen Devices | Missing laptops, phones, USB drives |
| Physical Security | Tailgating, unauthorized visitors, missing equipment |
| Policy Violations | Observed security policy violations |
| System Changes | Unauthorized changes outside change control |
| Suspicious Activity | Unusual behavior, potential insider threat |
| Remote Work Security | VPN issues, home network concerns, public space risks |

### 11.3 Non-Blame Culture Elements

| Element | Requirement |
|---------|-------------|
| Policy Statement | Non-blame/no-retaliation stated in policy |
| Good Faith Protection | Reporters protected for good faith reports |
| Constructive Handling | Honest mistakes handled constructively |
| Confidentiality | Reporter identity protected |
| Recognition | Positive recognition for reporting |
| Management Support | Visible management support for reporting |
| No Negative Examples | No evidence of blame for reporting |

---

## END OF SPECIFICATION

---

*"The first step toward security is recognizing that there's a problem."*
— Security Maxim

<!-- QA_VERIFIED: 2026-02-06 -->
