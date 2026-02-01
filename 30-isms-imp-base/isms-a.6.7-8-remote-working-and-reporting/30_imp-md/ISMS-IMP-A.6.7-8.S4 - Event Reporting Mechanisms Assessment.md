**ISMS-IMP-A.6.7-8.S4 - Event Reporting Mechanisms Assessment**
**Assessment Specification with User Completion Guide**
### ISO/IEC 27001:2022 Controls A.6.7 (Remote Working) & A.6.8 (Information Security Event Reporting)

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.6.7-8.S4 |
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

This document consists of two parts:

- **PART I: USER COMPLETION GUIDE**
  - Assessment Overview
  - Prerequisites
  - Assessment Workflow
  - Sheet-by-Sheet Guidance
  - Evidence Collection
  - Common Pitfalls
  - Quality Checklist
  - Review & Approval

- **PART II: TECHNICAL SPECIFICATION**
  - Workbook Structure
  - Sheet-by-Sheet Specifications
  - Formula Specifications
  - Styling Reference

**Target Audiences:**

- **Part I:** Assessment users (IT Security Team, Security Operations, Help Desk)
- **Part II:** Workbook developers (Python/Excel script maintainers)

---

# PART I: USER COMPLETION GUIDE

**Audience:** IT Security Team, Security Operations, Help Desk, Compliance Officers

---

## 1. Assessment Overview

### 1.1 Purpose

This assessment workbook evaluates [Organization]'s security event reporting mechanisms, ensuring that:
- Multiple accessible reporting channels exist
- Personnel understand what to report and how
- Reports are acknowledged and processed timely
- Non-blame culture is fostered
- Reporting mechanisms are accessible from remote locations
- Event reporting integrates with incident management

### 1.2 Scope

This assessment covers:
- Reporting channel inventory and accessibility
- Reporting procedures and documentation
- Event classification and examples
- Personnel awareness of reporting obligations
- Response timeliness and acknowledgment
- Non-blame culture implementation
- Integration with incident management (A.5.24-28)
- Remote accessibility of reporting channels

### 1.3 Target Audience

- **Primary Assessors**: IT Security Team, Security Operations
- **Data Contributors**: Help Desk, HR, Communications
- **Reviewers**: IT Security Manager, CISO
- **Approvers**: CISO

### 1.4 Assessment Frequency

| Trigger | Frequency |
|---------|-----------|
| Initial Assessment | Once (ISMS implementation) |
| Periodic Review | Semi-Annual |
| Triggered Review | After significant security events, reporting failures |

## 2. Prerequisites

Before starting this assessment, ensure:

| Prerequisite | Status | Notes |
|--------------|--------|-------|
| Access to event reporting system/ticketing | ☐ | To review actual reports |
| Reporting channel documentation | ☐ | Published contact info |
| Security awareness training materials | ☐ | Event reporting content |
| Sample of recent event reports | ☐ | For process verification |
| Response time metrics (if available) | ☐ | SLA compliance data |

## 3. Assessment Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│  PHASE 1: Reporting Channel Inventory                          │
│  - Identify all reporting channels                              │
│  - Verify accessibility and availability                        │
│  - Check remote access capability                               │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│  PHASE 2: Procedure Assessment                                  │
│  - Review reporting procedures                                  │
│  - Verify event classification guidance                         │
│  - Check documentation completeness                             │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│  PHASE 3: Awareness Assessment                                  │
│  - Verify training includes event reporting                     │
│  - Check awareness of reporting channels                        │
│  - Assess understanding of reportable events                    │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│  PHASE 4: Response Effectiveness                                │
│  - Sample recent event reports                                  │
│  - Verify acknowledgment timeliness                             │
│  - Check feedback to reporters                                  │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│  PHASE 5: Gap Analysis & Evidence Collection                    │
│  - Document gaps identified                                     │
│  - Collect evidence                                             │
│  - Prepare remediation recommendations                          │
└─────────────────────────────────────────────────────────────────┘
```

## 4. Sheet-by-Sheet Completion Guide

### 4.1 Instructions Sheet

**Purpose**: Provides guidance for workbook users.

### 4.2 Reporting_Channels Sheet

**Purpose**: Inventory all security event reporting channels.

**Column Definitions**:

| Column | Description | Input Type |
|--------|-------------|------------|
| Channel ID | Unique identifier | Auto-generated |
| Channel Name | Name of reporting channel | Free text |
| Channel Type | Email/Phone/Web Form/Chat/Other | Dropdown |
| Contact Details | How to reach this channel | Free text |
| Availability | 24/7 or business hours | Dropdown |
| Remote Accessible | Can be used from remote locations | Yes/No |
| Primary Use | Main purpose of this channel | Free text |
| Owner | Team/person managing channel | Free text |
| Published | Is this channel publicly documented | Yes/No |
| Status | Active/Inactive | Dropdown |

**Minimum Channels Expected**:
- At least 2 distinct channels
- At least 1 available 24/7 for critical events
- All channels accessible from remote locations

### 4.3 Channel_Accessibility Sheet

**Purpose**: Verify that reporting channels are accessible and functional.

**Column Definitions**:

| Column | Description | Input Type |
|--------|-------------|------------|
| Channel ID | Reference to Reporting_Channels | Reference |
| Test Date | When accessibility was tested | Date |
| Test Type | Functional/Availability/Remote | Dropdown |
| Test Method | How the test was conducted | Free text |
| Result | Pass/Fail/Partial | Dropdown |
| Response Received | Did test generate response | Yes/No |
| Response Time | Time to acknowledgment | Free text |
| Issues Found | Any issues during testing | Free text |
| Evidence | Test evidence reference | Free text |

### 4.4 Reporting_Procedures Sheet

**Purpose**: Assess documentation of reporting procedures.

**Column Definitions**:

| Column | Description | Input Type |
|--------|-------------|------------|
| Procedure Element | Component of reporting procedure | Pre-populated |
| Requirement | What should be documented | Pre-populated |
| Documented | Is this documented | Yes/No/Partial |
| Location | Where is this documented | Free text |
| Current | Is documentation current | Yes/No |
| Accessible | Can personnel access this | Yes/No |
| Evidence | Documentation reference | Free text |
| Gap | If not compliant, describe gap | Free text |

**Procedure Elements**:
- What to report (event categories with examples)
- How to report (channel-specific instructions)
- When to report (timeliness expectations)
- What information to include
- What NOT to do (e.g., don't investigate yourself)
- Response expectations (acknowledgment timeframes)
- Escalation paths
- Anonymity options

### 4.5 Event_Categories Sheet

**Purpose**: Verify that reportable event categories are defined with examples.

**Column Definitions**:

| Column | Description | Input Type |
|--------|-------------|------------|
| Category | Event category | Pre-populated |
| Defined | Is this category defined | Yes/No |
| Examples Provided | Are examples given | Yes/No |
| Priority Level | Associated priority (Critical/High/Medium/Low) | Dropdown |
| Reporting Timeframe | Expected reporting timeframe | Free text |
| Documentation | Where is this documented | Free text |
| Compliant | Meets requirements | Formula |

**Event Categories (per ISO 27002:2022)**:
- Phishing/Social engineering
- Malware/Suspected infection
- Unauthorized access attempts
- Data breach/exposure
- Lost or stolen devices
- Physical security breaches
- Policy violations
- System alterations outside change control (NEW)
- Suspicious activity
- Remote work specific events

### 4.6 Awareness_Assessment Sheet

**Purpose**: Assess whether personnel are aware of reporting obligations.

**Column Definitions**:

| Column | Description | Input Type |
|--------|-------------|------------|
| Awareness Element | What personnel should know | Pre-populated |
| Training Included | Is this in security training | Yes/No |
| Onboarding Included | Is this in onboarding | Yes/No |
| Refresher Frequency | How often is this reinforced | Free text |
| Last Communication | Last awareness communication | Date |
| Verification Method | How is awareness verified | Free text |
| Compliant | Meets requirements | Formula |
| Evidence | Training materials, etc. | Free text |

### 4.7 Response_Sampling Sheet

**Purpose**: Sample actual event reports to verify process effectiveness.

**Sample Selection**:
- Minimum 20 reports from last 12 months (or all if fewer)
- Include mix of categories and priorities
- Include reports from remote workers

**Column Definitions**:

| Column | Description | Input Type |
|--------|-------------|------------|
| Sample ID | Unique identifier | Auto-generated |
| Report Date | When event was reported | Date |
| Event Category | Type of event | Dropdown |
| Reported Via | Channel used | Reference |
| Reporter Location | Office/Remote | Dropdown |
| Acknowledged | Was report acknowledged | Yes/No |
| Ack Time | Time to acknowledgment | Free text |
| Ack SLA Met | Within required timeframe | Yes/No |
| Feedback Provided | Was reporter given feedback | Yes/No |
| Escalated | Was event escalated to incident | Yes/No/N/A |
| Documented | Proper documentation maintained | Yes/No |
| Compliant | Overall process compliance | Formula |
| Notes | Observations | Free text |

### 4.8 NonBlame_Culture Sheet

**Purpose**: Assess implementation of non-blame reporting culture.

**Column Definitions**:

| Column | Description | Input Type |
|--------|-------------|------------|
| Culture Element | Aspect of non-blame culture | Pre-populated |
| Policy Stated | Is this in policy | Yes/No |
| Communicated | Has this been communicated | Yes/No |
| Evidence of Practice | Evidence this is practiced | Free text |
| Contrary Evidence | Any evidence of blame culture | Free text |
| Compliant | Meets requirements | Formula |
| Notes | Observations | Free text |

**Culture Elements**:
- Good faith protection stated in policy
- Non-retaliation clause
- Constructive handling of honest mistakes
- Recognition for exemplary reporting
- Confidentiality of reporter identity
- Management endorsement of reporting
- No negative examples (blame incidents)

### 4.9 Integration_Assessment Sheet

**Purpose**: Assess integration with incident management.

**Column Definitions**:

| Column | Description | Input Type |
|--------|-------------|------------|
| Integration Point | Connection with incident management | Pre-populated |
| Implemented | Is this in place | Yes/No/Partial |
| Documentation | Where is this documented | Free text |
| Evidence | Evidence of integration | Free text |
| Gap | If not compliant, describe | Free text |

**Integration Points**:
- Clear escalation criteria (event → incident)
- Handoff procedure to incident response team
- Event feeds into incident classification
- Closed-loop feedback from incidents to events
- Metrics shared between event and incident management
- Common ticketing/tracking system (if applicable)

### 4.10 Gap_Analysis Sheet

**Purpose**: Consolidate all event reporting gaps.

**Column Definitions**:

| Column | Description | Input Type |
|--------|-------------|------------|
| Gap ID | Unique identifier (GAP-EVT-###) | Auto-generated |
| Source Sheet | Which sheet identified gap | Reference |
| Gap Description | Clear description | Free text |
| Control Reference | Related policy section | Free text |
| Impact | Impact if not addressed | Dropdown |
| Remediation Action | Recommended fix | Free text |
| Owner | Who will remediate | Free text |
| Target Date | Remediation deadline | Date |
| Status | Current status | Dropdown |

### 4.11 Evidence_Register Sheet

**Purpose**: Catalog all evidence collected.

### 4.12 Dashboard Sheet

**Purpose**: Provide executive summary.

**Metrics Displayed**:
- Number of reporting channels
- Channel accessibility compliance
- Procedure documentation completeness
- Awareness coverage
- Response SLA compliance rate
- Non-blame culture score
- Gap count by severity

### 4.13 Approval_Sign_Off Sheet

**Purpose**: Document formal review and approval.

## 5. Evidence Collection Guidelines

### 5.1 Required Evidence Types

| Evidence Category | Examples |
|-------------------|----------|
| Channel Documentation | Published contact information, intranet pages |
| Procedures | Reporting procedures, quick reference guides |
| Training Materials | Awareness content covering event reporting |
| Sample Reports | Anonymized event reports (with consent) |
| Response Logs | Acknowledgment records, ticket history |
| Communications | Awareness communications, policy announcements |

## 6. Common Pitfalls

#### ❌ MISTAKE #1: Only Testing Primary Reporting Channel

**The Problem:** Testing main security email or portal but not backup/alternative channels.

**Why It Matters:** Primary channel may fail. Users may not know it. Backup channels may be misconfigured.

**The Fix:**
- Test ALL documented reporting channels
- Include phone, email, web, chat options
- Verify backup channels actually work

#### ❌ MISTAKE #2: Not Testing From Remote Locations

**The Problem:** Testing channels from office network, not remote worker perspective.

**Why It Matters:** Remote users may have different access. VPN requirements may affect accessibility. Critical for remote worker event reporting.

**The Fix:**
- Test channels from outside corporate network
- Verify mobile accessibility
- Check VPN impact on channel access

#### ❌ MISTAKE #3: Missing Informal Reporting Paths

**The Problem:** Only assessing formal channels, missing how events actually get reported.

**Why It Matters:** Staff may report via Slack, email to manager, etc. Informal reports may not reach security team. Incomplete event capture.

**The Fix:**
- Survey staff on how they'd report events
- Interview managers about informal reports received
- Document all reporting paths, formal and informal

#### ❌ MISTAKE #4: Assuming Training Equals Awareness

**The Problem:** Confirming event reporting is in training but not verifying staff actually know what to do.

**Why It Matters:** Training completion doesn't equal retention. Staff may not recognize events. May not know how to report.

**The Fix:**
- Include awareness questions in surveys
- Test with simulated events (phishing, etc.)
- Check if staff can locate reporting information

#### ❌ MISTAKE #5: Not Testing Anonymous Reporting

**The Problem:** Documenting anonymous reporting exists but not verifying it works.

**Why It Matters:** Anonymity may be compromised technically. Important for whistleblower protection. May affect willingness to report.

**The Fix:**
- Test anonymous submission process
- Verify IP/identity not logged
- Check anonymous report tracking

#### ❌ MISTAKE #6: Ignoring Response Effectiveness

**The Problem:** Assessing reporting process but not what happens after reports received.

**Why It Matters:** Slow/no response discourages reporting. Staff need feedback. Response quality affects culture.

**The Fix:**
- Sample actual reports and check response times
- Verify feedback provided to reporters
- Check resolution tracking

#### ❌ MISTAKE #7: Not Verifying Non-Blame Culture

**The Problem:** Policy says non-blame but not checking if practice matches.

**Why It Matters:** Fear of blame prevents reporting. Critical for security culture. Policy must be practiced.

**The Fix:**
- Look for evidence of punitive responses
- Survey staff on perception of blame
- Check for positive recognition of reporters

#### ❌ MISTAKE #8: Missing Incident Management Integration

**The Problem:** Assessing event reporting in isolation from incident management (A.5.24-28).

**Why It Matters:** Events should flow to incident process. Integration gaps mean lost events. Incomplete audit trail.

**The Fix:**
- Trace sample events to incident tickets
- Verify handoff process documented
- Check classification triggers incident escalation

---

## 7. Quality Checklist

#### Completeness Checks

- [ ] ALL reporting channels inventoried
- [ ] Channel accessibility tested (including from remote)
- [ ] Procedures documented and current
- [ ] Event categories defined with examples
- [ ] Awareness included in training program
- [ ] Response sampling completed (actual reports)
- [ ] Non-blame culture assessed (policy and practice)
- [ ] Integration with incident management verified
- [ ] All gaps documented with remediation

#### Accuracy Checks

- [ ] Channels actually work as documented
- [ ] Contact information current
- [ ] Response times match SLAs
- [ ] Categories align with incident taxonomy

#### Evidence Quality Checks

- [ ] Channel tests documented
- [ ] Sample reports anonymized appropriately
- [ ] Response time evidence captured
- [ ] Survey results documented

---

## 8. Review and Approval Process

### 8.1 Review Workflow

**Step 1: Self-Review** (Assessor) - Complete Quality Checklist
**Step 2: Technical Review** (Security Operations) - 2-3 days
**Step 3: Management Approval** (CISO) - 1-2 days

### 8.2 After Approval

1. **Store Assessment:** `ISMS/Controls/A.6.7-8/Event_Reporting/`
2. **Distribute:** Security Operations, Help Desk, Communications
3. **Initiate Remediation:** Fix channel issues, update procedures
4. **Schedule Follow-Up:** Annual reassessment, quarterly channel tests

---

# PART II: TECHNICAL SPECIFICATION

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

<!-- QA_VERIFIED: 2026-01-31 -->
