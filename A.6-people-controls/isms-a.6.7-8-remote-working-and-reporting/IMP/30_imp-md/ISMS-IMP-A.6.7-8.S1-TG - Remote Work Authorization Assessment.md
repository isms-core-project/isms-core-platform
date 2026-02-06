**ISMS-IMP-A.6.7-8.S1-TG - Remote Work Authorization Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Controls A.6.7 (Remote Working) & A.6.8 (Information Security Event Reporting)

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.6.7-8.S1-TG |
| **Version** | 1.0 |
| **Assessment Area** | Remote Work Authorization, Policy Framework, and Governance |
| **Related Policy** | ISMS-POL-A.6.7-8, Section 2.1 (Remote Work Authorization) |
| **Purpose** | Guide users through systematic assessment of remote work authorization processes |
| **Target Audience** | IT Security Team, HR Representatives, Line Managers, Auditors |
| **Assessment Type** | Policy & Operational |
| **Review Cycle** | Annual |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial specification for remote work authorization assessment | ISMS Implementation Team |

---

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.6.7-8.S1-UG.

---

# Technical Specification

### 9. Workbook Architecture

#### 9.1 Sheet Structure

| Sheet Name | Purpose | Sheet Type |
|------------|---------|------------|
| Instructions | User guidance | Static |
| Policy_Framework | Policy documentation assessment | Assessment |
| Authorization_Process | Workflow assessment | Assessment |
| Authorization_Criteria | Criteria definition assessment | Assessment |
| Sample_Testing | Sample authorization testing | Assessment |
| Periodic_Review | Review cycle assessment | Assessment |
| Gap_Analysis | Consolidated gaps | Analysis |
| Evidence_Register | Evidence catalog | Register |
| Dashboard | Executive summary | Calculated |
| Approval_Sign_Off | Formal approvals | Governance |

#### 9.2 Sheet Dependencies

```
Policy_Framework ─────┐
Authorization_Process ─┼──→ Gap_Analysis ──→ Dashboard
Authorization_Criteria ┤
Sample_Testing ────────┤
Periodic_Review ───────┘

All Sheets ──→ Evidence_Register
```

### 10. Column Specifications

#### 10.1 Policy_Framework Sheet

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Policy Element | 30 | Text | Pre-populated |
| B | Requirement | 50 | Text | Pre-populated |
| C | Status | 15 | Dropdown | Exists/Partial/Missing |
| D | Evidence Reference | 30 | Text | Free text |
| E | Gap Description | 40 | Text | Free text |
| F | Remediation | 40 | Text | Free text |
| G | Priority | 12 | Dropdown | High/Medium/Low |

#### 10.2 Sample_Testing Sheet

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Sample ID | 12 | Text | Auto-generated (RWA-###) |
| B | Employee ID | 15 | Text | Free text |
| C | Department | 20 | Text | Free text |
| D | Role | 25 | Text | Free text |
| E | Authorization Date | 15 | Date | Date format |
| F | Approval Obtained | 12 | Dropdown | Yes/No |
| G | Approved By | 20 | Text | Free text |
| H | Documentation Complete | 15 | Dropdown | Yes/No/Partial |
| I | Risk Assessment Done | 15 | Dropdown | Yes/No/N/A |
| J | Acknowledgment Signed | 15 | Dropdown | Yes/No |
| K | Compliant | 12 | Formula | =AND(F="Yes",H="Yes",J="Yes") |
| L | Notes | 40 | Text | Free text |

#### 10.3 Gap_Analysis Sheet

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Gap ID | 15 | Text | GAP-RWA-### format |
| B | Source Sheet | 20 | Text | Sheet name |
| C | Gap Description | 50 | Text | Free text |
| D | Control Reference | 25 | Text | Policy section |
| E | Risk Level | 12 | Dropdown | High/Medium/Low |
| F | Remediation Action | 50 | Text | Free text |
| G | Owner | 20 | Text | Free text |
| H | Target Date | 15 | Date | Date format |
| I | Status | 15 | Dropdown | Open/In Progress/Closed |

### 11. Formula Specifications

#### 11.1 Dashboard Calculations

**Overall Compliance %**:
```
=COUNTIF(Sample_Testing!K:K,"TRUE")/COUNTA(Sample_Testing!K2:K100)
```

**Gaps by Severity**:
```
High: =COUNTIF(Gap_Analysis!E:E,"High")
Medium: =COUNTIF(Gap_Analysis!E:E,"Medium")
Low: =COUNTIF(Gap_Analysis!E:E,"Low")
```

**Policy Framework Score**:
```
=COUNTIF(Policy_Framework!C:C,"Exists")/(COUNTIF(Policy_Framework!C:C,"Exists")+COUNTIF(Policy_Framework!C:C,"Partial")+COUNTIF(Policy_Framework!C:C,"Missing"))
```

### 12. Styling Specifications

#### 12.1 Color Coding

| Element | Fill Color | Font Color | Use |
|---------|------------|------------|-----|
| Header Row | #003366 (Navy) | #FFFFFF (White) | Column headers |
| Input Cell | #FFFF00 (Yellow) | #000000 (Black) | User input |
| Calculated Cell | #DCE6F1 (Light Blue) | #000000 (Black) | Formulas |
| Label Cell | #D9D9D9 (Gray) | #000000 (Black) | Row labels |
| Compliant | #C6EFCE (Light Green) | #006100 (Dark Green) | Pass status |
| Non-Compliant | #FFC7CE (Light Red) | #9C0006 (Dark Red) | Fail status |
| Partial | #FFEB9C (Light Yellow) | #9C5700 (Dark Yellow) | Partial status |

#### 12.2 Conditional Formatting

**Status Column (Policy_Framework)**:
- "Exists" → Green fill
- "Partial" → Yellow fill
- "Missing" → Red fill

**Compliant Column (Sample_Testing)**:
- TRUE → Green fill
- FALSE → Red fill

**Risk Level (Gap_Analysis)**:
- "High" → Red fill
- "Medium" → Yellow fill
- "Low" → Green fill

### 13. Data Validation Lists

#### 13.1 Dropdown Options

| Field | Options |
|-------|---------|
| Status (Policy) | Exists, Partial, Missing |
| Implemented | Yes, No, Partial |
| Priority | High, Medium, Low |
| Risk Level | High, Medium, Low |
| Gap Status | Open, In Progress, Closed, Deferred |
| Evidence Type | Document, Screenshot, Interview, System Export, Email |
| Yes/No | Yes, No |
| Yes/No/Partial | Yes, No, Partial |
| Yes/No/N/A | Yes, No, N/A |

### 14. Pre-Populated Content

#### 14.1 Policy Framework Elements

| Policy Element | Requirement |
|----------------|-------------|
| Remote Work Policy | Formal policy document approved and published |
| Authorization Procedure | Documented process for requesting/approving remote work |
| Security Requirements | Technical and physical security requirements defined |
| Eligibility Criteria | Criteria for remote work eligibility documented |
| Data Handling Rules | Data classification handling for remote work |
| Device Requirements | Corporate and BYOD device requirements |
| Termination Procedure | Process for revoking remote work authorization |
| Review Cycle | Periodic review requirements defined |

#### 14.2 Authorization Process Steps

| Step | Description |
|------|-------------|
| Request Initiation | Employee/manager initiates remote work request |
| Eligibility Check | HR/Manager verifies role eligibility |
| Risk Assessment | Security assesses risk for sensitive roles |
| Technical Approval | IT confirms technical capability |
| Manager Approval | Line manager approves arrangement |
| Security Acknowledgment | Employee signs security requirements |
| Access Provisioning | IT provisions remote access |
| Documentation | Records filed in HR system |
| Periodic Review | Authorization reviewed per schedule |

---

## END OF SPECIFICATION

---

*"The only truly secure system is one that is powered off, cast in a block of concrete, and sealed in a lead-lined room with armed guards."*
— Gene Spafford

<!-- QA_VERIFIED: 2026-02-06 -->
