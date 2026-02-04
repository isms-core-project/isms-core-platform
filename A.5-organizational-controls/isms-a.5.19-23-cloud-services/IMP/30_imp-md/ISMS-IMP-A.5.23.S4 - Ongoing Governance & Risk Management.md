**ISMS-IMP-A.5.23.S4 - Ongoing Governance & Risk Management**
**Assessment Specification with User Completion Guide**
### ISO/IEC 27001:2022 Control A.5.23: Information Security for Use of Cloud Services

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.23.S4 |
| **Version** | 1.0 |
| **Assessment Area** | Ongoing Governance & Risk Management |
| **Related Policy** | ISMS-POL-A.5.19-23-S4 (Supplier Monitoring & Change Management), ISMS-POL-A.5.19-23-S5 (Cloud Services Security - Section 6) |
| **Purpose** | Assess ongoing governance, access reviews, change management, incident response, business continuity, and vendor risk monitoring for all cloud services |
| **Target Audience** | IT Operations, Risk Management, Compliance Officers, Business Continuity Planners, Vendor Managers, Security Teams |
| **Assessment Type** | Operational Governance & Continuous Monitoring |
| **Review Cycle** | Quarterly (with continuous monitoring) |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial Excel workbook specification (Part II only) | ISMS Implementation Team |

### Document Structure

This document consists of two parts:

- **PART I: USER COMPLETION GUIDE**
  - Assessment Overview
  - Prerequisites & Preparation
  - Understanding the Assessment Sheets
  - Completing Each Sheet (Detailed Guidance)
  - Evidence Collection Guide
  - Common Pitfalls & How to Avoid Them
  - Quality Checklist
  - Review & Approval Process
  - Integration & Maintenance
  - Appendices & References

- **PART II: TECHNICAL SPECIFICATION**
  - Excel Workbook Structure (11 Sheets)
  - Sheet-by-Sheet Column Specifications
  - Validation Rules & Formulas
  - Cell Styling Reference
  - Integration Points

---

# PART I: USER COMPLETION GUIDE

## Section 1: Assessment Overview

### 1.1 Purpose & Scope

**Assessment Name:** ISMS-IMP-A.5.23.S4 - Ongoing Governance & Risk Management

#### What This Assessment Covers

This assessment evaluates the **operational governance and continuous monitoring** of ALL cloud services identified in your inventory (ISMS-IMP-A.5.23.S1). While previous assessments focused on initial selection, configuration, and vendor evaluation, this assessment answers the critical question:

**"Are we maintaining security and compliance over time?"**

Cloud security is NOT a one-time implementation—it requires ongoing vigilance. Services that were secure at deployment can drift, vendors can change ownership, incidents can occur, and business continuity plans can become outdated. This assessment ensures you're actively managing these operational risks.

**Core Principle:**

**"Security is a process, not a state. What was secure yesterday may not be secure today without continuous governance."**

#### Key Governance Areas Assessed

**1. Access Review & Recertification (Sheet 2)**

- Quarterly access reviews for all cloud services
- Orphan account detection and remediation
- Privileged access recertification
- Service account ownership verification

**2. Change Management (Sheet 3)**

- Provider-initiated changes (service updates, acquisitions, policy changes)
- Organization-initiated changes (configuration updates, integrations)
- Emergency change tracking
- Change impact assessment and rollback capability

**3. Incident Management (Sheet 4)**

- Security incident detection and response
- Vendor breach notification procedures
- Incident lessons learned and remediation
- Post-incident security improvements

**4. Business Continuity & Disaster Recovery (Sheet 5)**

- BC/DR plan existence and testing
- Recovery Time Objective (RTO) / Recovery Point Objective (RPO) validation
- Failover testing for critical services
- Annual BC/DR plan review

**5. Vendor Risk Monitoring (Sheet 6)**

- Ongoing vendor security posture assessment
- Certification expiry tracking (ISO 27001, SOC 2)
- Vendor security incidents and breach notifications
- Financial health monitoring for critical vendors
- Sub-processor change tracking

**6. Exit Strategy Review (Sheet 7)**

- Annual exit plan validation
- Proof-of-concept (PoC) migration testing for critical services
- Alternative provider viability assessment
- Exit trigger condition monitoring

**7. Jurisdictional Risk Assessment (Sheet 8)**

- Ongoing monitoring of US CLOUD Act exposure
- Transfer mechanism validity (SCCs, BCRs, TIAs)
- Vendor jurisdiction changes (acquisitions, data center moves)
- Regulatory landscape changes

---

### 1.2 What Makes This Different from Other Assessments

**Integration with the A.5.19-23 Framework:**
```
┌──────────────────────────────────────────────────────────────────┐
│                   A.5.19-23 FRAMEWORK OVERVIEW                   │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌──────────────┐   ┌──────────────┐   ┌──────────────┐          │
│  │ IMP-5.23.1   │ → │ IMP-5.23.2   │ → │ IMP-5.23.3   │          │
│  │ INVENTORY    │   │ VENDOR DD    │   │ CONFIG       │          │
│  │ "What?"      │   │ "Who?"       │   │ "How?"       │          │
│  └──────┬───────┘   └──────┬───────┘   └──────┬───────┘          │
│         │                  │                  │                  │
│         └──────────────────┼──────────────────┘                  │
│                            ▼                                     │
│                  ┌──────────────────┐                            │
│                  │  IMP-5.23.4      │ ◄── YOU ARE HERE           │
│                  │  THIS DOCUMENT   │                            │
│                  │  GOVERNANCE      │                            │
│                  │  "Ongoing?"      │                            │
│                  └────────┬─────────┘                            │
│                           │                                      │
│                           ▼                                      │
│                  ┌──────────────────┐                            │
│                  │  IMP-5.23.5      │                            │
│                  │  COMPLIANCE      │                            │
│                  │  DASHBOARD       │                            │
│                  └──────────────────┘                            │
└──────────────────────────────────────────────────────────────────┘
```

**How This Fits:**

| Assessment | Focus | Frequency | Dependency on 5.23.4 |
|------------|-------|-----------|----------------------|
| **5.23.1 (Inventory)** | What services exist | Quarterly | Feeds service list to governance |
| **5.23.2 (Vendor DD)** | Who provides them, contract terms | Annual + new vendors | Governance monitors contract compliance |
| **5.23.3 (Config)** | How they're configured | Quarterly | Governance detects config drift |
| **5.23.4 (THIS DOC)** | Are we maintaining security | Quarterly + continuous | Provides operational metrics |
| **5.23.5 (Dashboard)** | Overall compliance posture | Quarterly | Aggregates governance data |

---

### 1.3 Who Needs to Complete This Assessment

**Primary Stakeholders:**

| Role | Responsibility | Typical Time Commitment |
|------|----------------|------------------------|
| **IT Operations Manager** | Overall coordination, change management tracking | 8-12 hours per quarter |
| **Access Control Administrator** | Quarterly access reviews, orphan account remediation | 4-6 hours per quarter |
| **Incident Response Coordinator** | Security incident tracking, lessons learned | 2-4 hours per quarter |
| **Business Continuity Planner** | BC/DR plan validation, testing coordination | 4-6 hours per quarter |
| **Vendor Manager / Procurement** | Vendor performance monitoring, contract compliance | 3-5 hours per quarter |
| **Risk Manager** | Vendor risk assessment, risk register updates | 3-5 hours per quarter |
| **DPO (Data Protection Officer)** | Jurisdictional risk monitoring | 2-3 hours per quarter |
| **Compliance Officer** | Regulatory requirement tracking, audit coordination | 2-4 hours per quarter |

**Approval Chain:**
```
IT Operations Manager → Compliance Officer → CISO
```

**Implementer Perspective:**
*"This assessment requires coordination across multiple teams. Start early, assign clear ownership for each sheet, and schedule a kick-off meeting to align stakeholders."*

**Auditor Perspective:**
*"I'll verify that governance activities actually occurred (not just documented as required). Show me evidence: access review reports with dates, incident tickets with resolutions, BC/DR test results with screenshots."*

---

### 1.4 What You'll Deliver

**Quarterly Deliverables:**

**1. Completed Assessment Workbook (ISMS-IMP-A.5.23.S4_Governance_YYYYMMDD.xlsx):**

- All 6 governance assessment sheets complete (Sheets 2-7)
- Jurisdictional risk sheet updated (Sheet 8)
- Evidence register populated with audit trails (Sheet 10)
- Approval sign-offs from IT Ops, Compliance, CISO (Sheet 11)

**2. Governance Metrics Summary:**

- Access review completion rate (target: 100%)
- Orphan accounts remediated (target: <24 hours)
- Change success rate (target: >95%)
- BC/DR tests completed (target: 100% for critical services)
- Vendor risk escalations (flagged for CISO review)

**3. Gap Remediation Plan:**

- Overdue access reviews → Target completion dates
- Untested BC/DR plans → Test scheduling
- High-risk vendor concerns → Mitigation actions or vendor replacement plan
- Jurisdictional risks → TIA completion or risk acceptance

**4. Continuous Monitoring Evidence:**

- Access review reports (quarterly)
- Change management tickets (ongoing)
- Incident response tickets (as needed)
- BC/DR test reports (annual minimum, quarterly for critical)
- Vendor performance scorecards (quarterly)

---

### 1.5 Success Criteria

**What "Good" Looks Like:**

**Implementer Perspective:**

- ✅ 100% of services have completed quarterly access reviews
- ✅ Zero orphan accounts older than 24 hours
- ✅ All critical services have tested BC/DR plans (annual minimum)
- ✅ All high-risk vendor issues escalated to CISO within 5 business days
- ✅ All changes documented with impact assessment and rollback plan
- ✅ Evidence is current (<90 days old for quarterly items)

**Auditor Perspective:**

- ✅ Timestamps on evidence match claimed dates (not backdated)
- ✅ Access review sign-offs from actual managers (not admin on their behalf)
- ✅ BC/DR test results show actual testing (not just "plan reviewed")
- ✅ Incident lessons learned show actionable improvements (not "no issues found")
- ✅ Vendor risk assessments reference objective evidence (certifications, breach notifications, not just "vendor is good")
- ✅ Jurisdictional risk assessments updated when vendor circumstances change

---

### 1.6 Time Commitment & Resources

**Quarterly Assessment Cycle:**

| Phase | Duration | Activities |
|-------|----------|------------|
| **Week 1: Preparation** | 2-3 days | Gather previous quarter's data, schedule stakeholder meetings, assign sheet ownership |
| **Week 2-3: Data Collection** | 7-10 days | Complete access reviews, update change logs, review incidents, validate BC/DR status |
| **Week 3: Evidence Gathering** | 2-3 days | Collect screenshots, reports, tickets, test results |
| **Week 4: Review & Approval** | 3-5 days | Internal QA, stakeholder reviews, approval workflow |
| **Total** | 3-4 weeks | From kickoff to CISO sign-off |

**Resource Requirements:**

- **Personnel:** 6-8 stakeholders (see Section 1.3)
- **Tools:** Access to cloud admin consoles, ITSM system, SIEM, vendor portals
- **Budget:** Minimal (staff time only, unless BC/DR testing requires vendor support)

---

### 1.7 Key Concepts & Terminology

**Governance vs. Initial Assessment:**

| Concept | Definition | This Assessment's Role |
|---------|------------|------------------------|
| **Governance** | Ongoing oversight and control of cloud services | This document: quarterly validation |
| **Access Review** | Periodic verification that access rights remain appropriate | Sheet 2: quarterly recertification |
| **Change Management** | Controlled process for implementing changes | Sheet 3: tracking provider and org changes |
| **Incident Management** | Detecting, responding to, and learning from security incidents | Sheet 4: incident tracking and lessons learned |
| **Business Continuity** | Ensuring critical services can recover from disruptions | Sheet 5: BC/DR plan validation and testing |
| **Vendor Risk Monitoring** | Continuous assessment of vendor security posture | Sheet 6: certification tracking, breach monitoring |
| **Orphan Account** | User account with no active owner (terminated employee, changed role) | Sheet 2: detection and 24-hour remediation |

---

## Section 2: Prerequisites & Preparation

### 2.1 Prerequisites - What You MUST Have Before Starting

**❌ DO NOT start this assessment until you have:**

**1. Completed Upstream Assessments:**
```
☐ ISMS-IMP-A.5.23.S1 (Inventory) is current (within 90 days)
   Why: You need the authoritative service list to govern
   
☐ ISMS-IMP-A.5.23.S2 (Vendor DD) has baseline vendor risk ratings
   Why: Ongoing monitoring tracks changes from baseline
   
☐ ISMS-IMP-A.5.23.S3 (Config) has baseline configurations documented
   Why: Change management tracks drift from baseline
```

**Without these, you're assessing "something" but not the right "something."**

**2. Access to Required Systems:**
```
☐ Cloud service admin consoles (for access reviews)
☐ Identity & Access Management (IAM) system (for user lists, orphan detection)
☐ Change Management system (ServiceNow, Jira, etc.)
☐ Incident Management system (ticketing system)
☐ SIEM or logging system (for incident detection evidence)
☐ Vendor portals (for certification downloads, status pages)
☐ Contract management system (for SLA tracking)
```

**3. Previous Quarter's Assessment (if not first cycle):**
```
☐ Last quarter's ISMS-IMP-A.5.23.S4 workbook
   Why: Track progress on remediation items
   
☐ Open findings from previous quarter
   Why: Verify closure or escalate overdue items
```

**4. Stakeholder Availability:**
```
☐ IT Operations: Available for weekly sync meetings
☐ Access Control Admin: Dedicated time for quarterly reviews
☐ BC Planner: Available for test coordination
☐ Vendor Manager: Vendor performance data ready
```

---

### 2.2 Preparation Checklist (Week Before Assessment Starts)

**For Assessment Coordinator:**
```
WEEK BEFORE QUARTERLY ASSESSMENT KICKOFF

☐ Schedule Kickoff Meeting
  When: First Monday of assessment quarter
  Who: All stakeholders (IT Ops, Access Admin, BC Planner, Vendor Mgr, etc.)
  Duration: 60 minutes
  Agenda: Review previous quarter, assign sheet ownership, set deadlines

☐ Retrieve Previous Quarter's Data
  ☐ Last quarter's ISMS-IMP-A.5.23.S4 workbook
  ☐ Open remediation items with current status
  ☐ Vendor incidents from last quarter (from SIEM/tickets)

☐ Prepare Service List
  ☐ Export current services from ISMS-IMP-A.5.23.S1
  ☐ Identify new services added since last quarter
  ☐ Identify decommissioned services (archive, don't delete rows)

☐ Notify Stakeholders
  Email template:
  ---
  Subject: Q[X] Cloud Governance Assessment - Action Required
  
  Team,
  
  It's time for our quarterly cloud governance assessment (ISMS-IMP-A.5.23.S4).
  
  KICKOFF: [Date/Time] - [Location/Teams Link]
  DEADLINE: [4 weeks from kickoff]
  
  Your assigned responsibilities:

  - [Role]: [Sheet Name] - [Key deliverables]
  
  Prerequisites:

  - Review last quarter's findings (attached)
  - Ensure access to [relevant systems]
  - Block [X hours] over next 3 weeks
  
  Questions? Reply to this email.
  
  Thanks,
  [Assessment Coordinator]
  ---

☐ Validate Tool Access
  ☐ All stakeholders have admin access to their assigned cloud services
  ☐ Incident system access for IR Coordinator
  ☐ Vendor portal access for Vendor Manager
  ☐ IAM system access for Access Control Admin

☐ Prepare Evidence Storage
  ☐ Create folder: /evidence/governance/Q[X]_[YYYY]/
  ☐ Subfolders: /access_reviews, /changes, /incidents, /bcdr, /vendor
  ☐ Set permissions (read: Assessment team, write: Coordinators only)
```

---

### 2.3 Understanding the Assessment Workflow

**Quarterly Governance Cycle:**
```
┌─────────────────────────────────────────────────────────────────┐
│                    QUARTERLY GOVERNANCE CYCLE                    │
└─────────────────────────────────────────────────────────────────┘
          │
    WEEK 1: KICKOFF & PLANNING
          │
          ├─▶ Kickoff Meeting
          │   - Review previous quarter
          │   - Assign sheet ownership
          │   - Set deadlines
          │
          ├─▶ Prepare Service List
          │   - Import from IMP-5.23.1
          │   - Add new services
          │   - Archive decommissioned
          │
          ▼
    WEEK 2-3: DATA COLLECTION & EVIDENCE GATHERING
          │
          ├─▶ Sheet 2: Access Reviews
          │   - Run access reports
          │   - Identify orphans
          │   - Manager sign-offs
          │
          ├─▶ Sheet 3: Changes
          │   - Export change tickets
          │   - Document provider changes
          │   - Impact assessments
          │
          ├─▶ Sheet 4: Incidents
          │   - Pull incident tickets
          │   - Lessons learned docs
          │   - Remediation evidence
          │
          ├─▶ Sheet 5: BC/DR
          │   - BC plan reviews
          │   - Test reports (if scheduled)
          │   - RTO/RPO validation
          │
          ├─▶ Sheet 6: Vendor Risk
          │   - Check cert expiry dates
          │   - Review vendor incidents
          │   - Financial health (critical vendors)
          │
          ├─▶ Sheet 7: Exit Strategy
          │   - Annual plan review
          │   - PoC test results (if applicable)
          │   - Alternative validation
          │
          ├─▶ Sheet 8: Jurisdictional Risk
          │   - Monitor vendor acquisitions
          │   - TIA validity
          │   - Regulatory changes
          │
          ▼
    WEEK 3: INTERNAL QUALITY ASSURANCE
          │
          ├─▶ Coordinator Reviews
          │   - Completeness check
          │   - Evidence validation
          │   - Gap identification
          │
          ▼
    WEEK 4: APPROVAL WORKFLOW
          │
          ├─▶ IT Operations Review
          │   - Technical accuracy
          │   - Operational feasibility
          │
          ├─▶ Compliance Review
          │   - Regulatory alignment
          │   - Audit readiness
          │
          ├─▶ CISO Approval
          │   - Risk acceptance
          │   - Executive sign-off
          │
          ▼
    COMPLETION: ARCHIVE & EXPORT
          │
          ├─▶ Archive quarterly snapshot
          ├─▶ Export metrics to IMP-5.23.5
          └─▶ Schedule next quarter
```

---

### 2.4 Data Sources & Integration Points

**Where Data Comes From:**

| Sheet | Primary Data Source | Secondary Sources | Refresh Frequency |
|-------|---------------------|-------------------|-------------------|
| **2. Access Review** | IAM system (user lists, last login) | Manager attestations | Quarterly |
| **3. Change Management** | ITSM tickets, vendor emails | Cloud provider release notes | Continuous |
| **4. Incident Management** | Incident tickets, SIEM alerts | Post-incident reports | Continuous |
| **5. Business Continuity** | BC plan documents, test reports | Vendor SLA docs | Annual + quarterly validation |
| **6. Vendor Risk Monitoring** | Vendor portals, SecurityScorecard | Financial databases (D&B) | Quarterly |
| **7. Exit Strategy Review** | Exit plan docs, PoC test results | Alternative vendor assessments | Annual |
| **8. Jurisdictional Risk** | Vendor announcements, DPA updates | Legal/DPO assessments | Quarterly |

**Integration with Other Systems:**
```
ISMS-IMP-A.5.23.S4 (This Assessment)
     │
     ├─▶ INPUT FROM:
     │    ├─ ISMS-IMP-A.5.23.S1 (Service list)
     │    ├─ ISMS-IMP-A.5.23.S2 (Vendor baseline risk)
     │    ├─ ISMS-IMP-A.5.23.S3 (Config baseline)
     │    ├─ IAM System (Access data)
     │    ├─ ITSM (Change tickets)
     │    ├─ Incident System (Security incidents)
     │    ├─ Vendor Portals (Certifications)
     │    └─ Contract System (SLA data)
     │
     └─▶ OUTPUT TO:
          ├─ ISMS-IMP-A.5.23.S5 (Dashboard - governance metrics)
          ├─ Risk Register (Vendor risks)
          └─ Audit Evidence (Quarterly governance proof)
```

---

### 2.5 Common Mistakes to Avoid (Before You Even Start)

**❌ Pitfall 1: Starting Without Previous Quarter's Data**
```
Problem: "We'll just start fresh each quarter"
Result: No trend tracking, can't measure improvement, auditors ask "where's the history?"
Fix: Always load previous quarter's workbook, compare changes, track progress
```

**❌ Pitfall 2: Assigning to People Without System Access**
```
Problem: "Jane will do access reviews" but Jane doesn't have IAM admin rights
Result: 2 weeks wasted on access requests, delayed assessment
Fix: Validate system access BEFORE kickoff meeting, get emergency access if needed
```

**❌ Pitfall 3: Assuming "No News = Good News"**
```
Problem: "We didn't have any incidents this quarter" (but didn't check SIEM)
Result: Incidents occurred but weren't documented, auditor finds them, credibility lost
Fix: Actively query systems (don't rely on memory), search SIEM/tickets with date filters
```

**❌ Pitfall 4: Copying Last Quarter's Answers**
```
Problem: "This service was compliant last quarter, still is" (without checking)
Result: Config drifted, vendor changed, compliance now false
Fix: Re-validate each quarter, especially for critical services
```

**❌ Pitfall 5: Treating This as IT-Only Work**
```
Problem: IT Ops tries to complete entire assessment alone
Result: Missing business context (BC/DR), incomplete vendor data, no legal input
Fix: Multi-stakeholder collaboration (see Section 1.3), clear ownership per sheet
```

---

## Section 3: Understanding the Assessment Sheets

### 3.1 Workbook Architecture Overview

**The 11-Sheet Structure:**

┌──────────────────────────────────────────────────────────────────┐
│           ISMS-IMP-A.5.23.S4 WORKBOOK ARCHITECTURE                │
├──────────────────────────────────────────────────────────────────┤
│                                                                   │
│  LAYER 1: ORIENTATION                                            │
│  ┌────────────────────────────────────────────────────────────┐  │
│  │ Sheet 1: Instructions & Legend                             │  │
│  │          How to use workbook, status symbols, dropdowns    │  │
│  └────────────────────────────────────────────────────────────┘  │
│                                                                   │
│  LAYER 2: OPERATIONAL GOVERNANCE ASSESSMENTS (Core)              │
│  ┌────────────────────────────────────────────────────────────┐  │
│  │ Sheet 2: Access Review & Recertification                   │  │
│  │          Quarterly access reviews, orphan accounts, PAM    │  │
│  ├────────────────────────────────────────────────────────────┤  │
│  │ Sheet 3: Change Management                                 │  │
│  │          Provider changes, org changes, impact assessment  │  │
│  ├────────────────────────────────────────────────────────────┤  │
│  │ Sheet 4: Incident Management                               │  │
│  │          Security incidents, response, lessons learned     │  │
│  ├────────────────────────────────────────────────────────────┤  │
│  │ Sheet 5: Business Continuity & DR                          │  │
│  │          BC/DR plans, RTO/RPO, testing, failover           │  │
│  ├────────────────────────────────────────────────────────────┤  │
│  │ Sheet 6: Vendor Risk Monitoring                            │  │
│  │          Cert tracking, vendor incidents, financial health │  │
│  ├────────────────────────────────────────────────────────────┤  │
│  │ Sheet 7: Exit Strategy Review                   │  │
│  │          Annual plan validation, PoC testing, alternatives │  │
│  └────────────────────────────────────────────────────────────┘  │
│                                                                   │
│  LAYER 3: REGULATORY COMPLIANCE                       │
│  ┌────────────────────────────────────────────────────────────┐  │
│  │ Sheet 8: Jurisdictional Risk Assessment                    │  │
│  │          CLOUD Act, transfer mechanisms, TIAs, DPO review  │  │
│  └────────────────────────────────────────────────────────────┘  │
│                                                                   │
│  LAYER 4: REPORTING & EVIDENCE                                   │
│  ┌────────────────────────────────────────────────────────────┐  │
│  │ Sheet 9: Summary Dashboard                                 │  │
│  │          Auto-calculated metrics, compliance %, gaps       │  │
│  ├────────────────────────────────────────────────────────────┤  │
│  │ Sheet 10: Evidence Register                                │  │
│  │          Audit trail (EV-GOV-###), evidence tracking       │  │
│  └────────────────────────────────────────────────────────────┘  │
│                                                                   │
│  LAYER 5: APPROVAL WORKFLOW                                      │
│  ┌────────────────────────────────────────────────────────────┐  │
│  │ Sheet 11: Approval Sign-Off                                │  │
│  │          IT Ops → Compliance → CISO approval chain         │  │
│  └────────────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────────────┘

---

### 3.2 Sheet-by-Sheet Purpose Summary

**Quick Reference:**

| Sheet | What It Assesses | Who Owns It | Update Frequency | Critical for Audit? |
|-------|------------------|-------------|------------------|---------------------|
| **Instructions & Legend** | How to use workbook | Coordinator | Once (at start) | No |
| **2. Access Review** | Access still appropriate? | Access Control Admin | Quarterly | ✅ YES |
| **3. Change Management** | Changes controlled? | IT Operations | Continuous + quarterly summary | ✅ YES |
| **4. Incident Management** | Incidents managed? | IR Coordinator | Continuous + quarterly summary | ✅ YES |
| **5. Business Continuity** | Recovery capability validated? | BC Planner | Annual + quarterly check | ✅ YES |
| **6. Vendor Risk Monitoring** | Vendor posture maintained? | Vendor Manager / Risk Mgr | Quarterly | ✅ YES |
| **7. Exit Strategy Review** | Exit plan viable? | IT Ops / Architect | Annual | ⚠️ MEDIUM |
| **8. Jurisdictional Risk** | Transfer mechanisms valid? | DPO / Legal | Quarterly | ✅ YES |
| **9. Summary Dashboard** | Overall compliance? | Auto-calculated | Real-time | ✅ YES |
| **10. Evidence Register** | Proof available? | All contributors | Continuous | ✅ YES |
| **11. Approval Sign-Of** | Sign-offs obtained? | Coordinator | End of quarter | ✅ YES |

---

### 3.3 Column Structure - Standard Across All Assessment Sheets

**Base Columns (A-Q) - Present on ALL Assessment Sheets (2-8):**

| Col | Header | Type | Purpose | Implementer View | Auditor View |
|-----|--------|------|---------|------------------|--------------|
| **A** | Cloud Service Name | Text | Service identifier | "What service am I governing?" | "Is this in the inventory?" |
| **B** | Vendor Name | Text | Provider | "Who do I contact for issues?" | "Does vendor match IMP-5.23.2?" |
| **C** | Service Type | Dropdown | SaaS/IaaS/PaaS | "What kind of service?" | "Classification correct?" |
| **D** | Review Period | Dropdown | Q1/Q2/Q3/Q4 | "When was this assessed?" | "Is this current quarter?" |
| **E** | Service Criticality | Dropdown | Critical/High/Medium/Low | "How important is this?" | "Matches IMP-5.23.1?" |
| **F** | Data Classification | Dropdown | Restricted/Confidential/etc. | "What data sensitivity?" | "Matches IMP-5.23.1?" |
| **G** | *[Sheet-Specific]* | Varies | Domain-specific field | See individual sheets | See individual sheets |
| **H** | Status | Dropdown | ✅/⚠️/❌/N/A | "Am I compliant?" | "Evidence supports status?" |
| **I** | Evidence Location | Text | Path to proof | "Where's my evidence?" | "Can I access and verify?" |
| **J** | Gap Description | Text | What's wrong | "What needs fixing?" | "Clear and specific?" |
| **K** | Remediation Needed | Dropdown | Yes/No | "Action required?" | "Matches status?" |
| **L** | Exception ID | Text | Link to exception register | "Approved deviation?" | "Exception current and signed?" |
| **M** | Risk ID | Text | Link to risk register | "Risk documented?" | "Risk treatment adequate?" |
| **N** | Compensating Controls | Text | Alternative mitigations | "How am I mitigating?" | "Controls effective?" |
| **O** | Responsible Team/Owner | Dropdown | Who owns remediation | "Who fixes this?" | "Owner has authority?" |
| **P** | Target Remediation Date | Date | When will it be fixed | "My deadline?" | "Realistic and tracked?" |
| **Q** | Last Review Date | Date | When last checked | "How current is this?" | "Evidence is fresh?" |

**Extended Columns (R-X) - Sheet-Specific:**

Each assessment sheet (2-8) has 7 additional columns (R-X) tailored to that governance domain. These will be explained in Section 4 (Sheet-by-Sheet Guide).

---

### 3.4 Status Symbols & Color Coding

**Universal Status Legend (Column H on all sheets):**

| Symbol | Status | Color | Meaning | When to Use |
|--------|--------|-------|---------|-------------|
| ✅ | **Compliant** | Green | Fully meets governance requirements | All criteria met, evidence available |
| ⚠️ | **Partial** | Yellow | Partially compliant, gaps exist | Some criteria met, action needed |
| ❌ | **Non-Compliant** | Red | Does not meet requirements | Significant gaps, urgent action |
| N/A | **Not Applicable** | Gray | Control doesn't apply | Service type doesn't require this |

**Examples by Sheet:**

**Sheet 2 (Access Review):**

- ✅ Compliant: Access review completed on-time, no orphans found, manager sign-off obtained
- ⚠️ Partial: Review completed but 3 orphan accounts found, remediation in progress
- ❌ Non-Compliant: Review overdue by 45 days, no action taken
- N/A: Service doesn't have user access (API-only integration)

**Sheet 4 (Incidents):**

- ✅ Compliant: Incident detected, responded to within SLA, lessons learned documented
- ⚠️ Partial: Incident responded to but lessons learned not yet documented
- ❌ Non-Compliant: Incident occurred but no formal response, no ticket created
- N/A: No incidents this quarter

**Implementer Perspective:**
*"Don't mark something compliant just because you want it to be. If evidence is missing, it's Partial at best. Auditors will check."*

**Auditor Perspective:**
*"I will randomly sample 20% of 'Compliant' items and verify evidence. If evidence doesn't support the status, the entire assessment loses credibility."*

---

### 3.5 Evidence Requirements - What "Counts"

**General Evidence Principles:**

**✅ Good Evidence:**

- **Timestamped:** Evidence shows when activity occurred
- **Objective:** Third-party report, system screenshot, signed document (not just "we did it")
- **Specific:** Links to exact service, exact date, exact finding
- **Recent:** <90 days old for quarterly items, <365 days for annual
- **Retrievable:** Stored in accessible location, not on someone's laptop

**❌ Poor Evidence:**

- "Trust me, we do access reviews" (no documentation)
- Screenshot with no timestamp or context
- "We have a BC plan" (but can't produce it or show it was tested)
- Vendor marketing material claiming "99.99% uptime" (without actual SLA report)

**Evidence by Sheet:**

| Sheet | Required Evidence Type | Example |
|-------|------------------------|---------|
| **2. Access Review** | Access review report with manager sign-off | PDF export from IAM system showing users reviewed, orphans found, manager signature |
| **3. Change Management** | Change ticket with approval and outcome | ServiceNow ticket #CHG-12345 showing approval chain, implementation, validation |
| **4. Incident Management** | Incident ticket + post-incident report | Jira ticket SEC-2024-089 + lessons learned doc with action items |
| **5. Business Continuity** | BC plan document + test report | BC Plan v2.3 (dated) + Test Report showing RTO achieved (screenshots) |
| **6. Vendor Risk Monitoring** | Vendor certification + validity check | ISO 27001 cert (PDF) + screenshot from cert authority showing validity |
| **7. Exit Strategy Review** | Exit plan + PoC test results | Exit plan doc v1.2 + migration PoC report (data extracted successfully) |
| **8. Jurisdictional Risk** | DPA + TIA (if US vendor) + legal review | Signed DPA with SCC annexes + TIA signed by Legal/DPO |

---

**END OF SECTIONS 1-3 (~1,000 lines)**

This first delivery covers:

- ✅ Document Control
- ✅ Section 1: Assessment Overview
- ✅ Section 2: Prerequisites & Preparation
- ✅ Section 3: Understanding the Assessment Sheets

**Next delivery will cover:**

- Section 4: Completing Each Sheet (Detailed Guidance) - Sheets 2-8
- Section 5: Evidence Collection Guide

**Ready for next part?** 🚀

---

## Section 4: Completing Each Sheet (Detailed Guidance)

### 4.1 Sheet 2: Access Review & Recertification

**Purpose:** Validate that user access to cloud services remains appropriate and authorized. Detect and remediate orphan accounts within 24 hours.

**Policy Reference:** "Access to cloud services MUST be reviewed quarterly. Orphan accounts MUST be disabled within 24 hours of detection." (ISMS-POL-A.5.19-23-S5 Section 6.1)

**Owner:** Access Control Administrator / IAM Team

**Time Commitment:** 4-6 hours per quarter (for ~40-50 services)

---

#### Column-by-Column Guidance (Sheet 2)

**Standard Columns (A-Q):** See Section 3.3

**Extended Columns (R-X) - Access Review Specific:**

| Column | Header | Type | How to Complete | Implementer Tip | Auditor Check |
|--------|--------|------|-----------------|-----------------|---------------|
| **R** | Last Review Date | Date | Date of most recent access review | Export from IAM system | Verify timestamp matches evidence |
| **S** | Review Outcome | Dropdown | Passed/Issues Found/Overdue | "Passed" only if zero issues | Check if "Issues" documented in Col J |
| **T** | Total Accounts Reviewed | Number | Count of user accounts checked | Get from IAM report | Spot-check against system |
| **U** | Orphan Accounts Found | Number | Accounts with no active owner | Run orphan detection script | Verify remediation evidence |
| **V** | Excessive Privileges Found | Number | Users with more access than needed | Compare role vs. actual access | Check downgrade evidence |
| **W** | Accounts Remediated | Number | Issues fixed this quarter | Should equal U + V if all resolved | Match to tickets |
| **X** | Next Review Due | Date | Last Review Date + 90 days | Auto-calculate or set reminder | Flag if overdue |

---

#### Step-by-Step: Completing an Access Review Entry

**Example Service: Microsoft 365**

**Step 1: Prepare for Review**
```
1. Log into Entra ID admin center
2. Export user list: Users → All Users → Download users
3. Export last sign-in report: Users → Sign-in logs → Last 90 days
4. Run orphan detection query (Microsoft Graph PowerShell):
   Connect-MgGraph -Scopes "User.Read.All"
   Get-MgUser -All -Filter "accountEnabled eq true" |
   Where-Object {$_.UserPrincipalName -like "*#EXT#*" -or $_.OnPremisesSecurityIdentifier -eq $null}
```

**Step 2: Fill Base Columns**
```
A: Microsoft 365
B: Microsoft
C: SaaS
D: Q1 (current quarter)
E: Critical
F: Confidential
G: Full Recertification (review type)
```

**Step 3: Conduct Review**
```
1. Review all 245 active accounts
2. Find 3 orphan accounts (terminated employees)
3. Find 5 accounts with excessive privileges (former managers)
4. Generate manager attestation requests
5. Collect manager sign-offs
```

**Step 4: Fill Extended Columns**
```
R: 2026-01-15 (review completed date)
S: Issues Found (because orphans + excessive privileges detected)
T: 245 (total accounts)
U: 3 (orphans)
V: 5 (excessive privileges)
W: 8 (all remediated within 24 hours)
X: 2026-04-15 (next review due in 90 days)
```

**Step 5: Status & Evidence**
```
H: ✅ Compliant (all issues remediated within SLA)
I: /evidence/access_reviews/Q1_2026/M365_access_review.pdf
J: (blank - no outstanding gaps)
K: No
L-N: (blank - no exceptions needed)
O: IAM Team
P: (blank - no remediation needed)
Q: 2026-01-15
```

**Evidence to Collect:**

- IAM system export (user list with last login dates)
- Orphan account detection report
- Manager attestation emails (signed)
- Remediation tickets (account disablement proof)

**Common Pitfalls:**

- ❌ Marking "Passed" when orphans were found (even if remediated—that's "Issues Found")
- ❌ Not documenting orphan remediation (auditors will ask for disable timestamps)
- ❌ Manager attestations collected but not dated (need timestamps)

---

#### Access Review Checklist (15 Items)

**For each cloud service, verify:**
```
☐ Quarterly access review schedule documented
☐ Review covers all user types (employees, contractors, service accounts)
☐ Privileged access reviewed separately with enhanced scrutiny
☐ Review includes comparison against job role/least privilege
☐ Orphan account detection automated or scheduled
☐ Orphan accounts disabled within 24 hours of detection
☐ Terminated user access revoked within SLA (24 hours)
☐ Service account ownership verified and documented
☐ Shared accounts minimized and justified
☐ MFA status verified during access review
☐ External/guest access reviewed and time-limited
☐ Access review findings documented with evidence
☐ Non-compliance escalated to service owner
☐ Review completion rates tracked and reported
☐ Access review process covers all cloud services in inventory
```

---

### 4.2 Sheet 3: Change Management

**Purpose:** Track and validate that all changes to cloud services (provider-initiated or org-initiated) follow change management procedures.

**Policy Reference:** "All cloud service changes MUST follow change management process. Emergency changes require post-implementation review within 48 hours." (ISMS-POL-A.5.19-23-S5 Section 6.2)

**Owner:** IT Operations Manager / Change Manager

**Time Commitment:** 2-3 hours per quarter (reviewing change log)

---

#### Column-by-Column Guidance (Sheet 3)

**Extended Columns (R-X) - Change Management Specific:**

| Column | Header | Type | How to Complete | Implementer Tip | Auditor Check |
|--------|--------|------|-----------------|-----------------|---------------|
| **R** | Change Count (Quarter) | Number | Total changes this quarter | Count from ITSM tickets | Verify against ticket system |
| **S** | Change Criticality | Dropdown | Low/Medium/High/Emergency | Based on impact assessment | Match to CAB approval level |
| **T** | CAB Approval Status | Dropdown | Approved/Rejected/Emergency Override | From change ticket | Emergency requires post-review |
| **U** | Rollback Plan Documented | Dropdown | Yes/No/N/A | Must be "Yes" for High/Critical | Check plan actually exists |
| **V** | Rollback Tested | Dropdown | Yes/No/N/A | Tested before implementation | Review test evidence |
| **W** | Change Success Rate | Percentage | Successful / Total changes | Calculate from quarter's changes | Failed changes documented? |
| **X** | Last Change Date | Date | Most recent change to service | From change log | Check if recent major changes |

---

#### Step-by-Step: Documenting Changes

**Example Service: AWS Production Account**

**Scenario:** 3 changes this quarter
1. Provider change: AWS announced new region availability (Medium)
2. Org change: Updated security group rules for new application (High)
3. Emergency change: Patched zero-day vulnerability (Emergency)

**Step 1: Gather Change Data**
```
1. Export change tickets from ServiceNow for Q1 2026
2. Filter for "AWS" and "Production"
3. Found 3 changes: CHG-10234, CHG-10567, CHG-10899
4. Review each ticket for approval, outcome, rollback status
```

**Step 2: Fill Base Columns**
```
A: AWS Production Account
B: Amazon Web Services
C: IaaS
D: Q1
E: Critical
F: Restricted
G: Mixed (Provider + Org Changes)
```

**Step 3: Assess Change Management Compliance**
```
R: 3 (changes this quarter)
S: High (worst case from 3 changes: Emergency > High > Medium)
T: 2 Approved + 1 Emergency Override
U: Yes (all 3 had rollback plans documented)
V: Partial (CHG-10234 and CHG-10567 tested, emergency CHG-10899 not tested due to urgency)
W: 100% (all 3 successful, no rollbacks needed)
X: 2026-01-18 (most recent emergency change)
```

**Step 4: Status & Evidence**
```
H: ⚠️ Partial (emergency change didn't have tested rollback—acceptable but needs post-review)
I: /evidence/changes/Q1_2026/AWS_changes_CHG-10234_10567_10899.pdf
J: Emergency change CHG-10899 bypassed rollback testing (acceptable per policy but requires 48hr post-review)
K: Yes (post-implementation review needed)
L: (blank)
M: (blank)
N: Compensating control: Emergency change had vendor support on standby for rollback if needed
O: IT Operations
P: 2026-01-20 (48 hours from emergency change for post-review)
Q: 2026-01-18
```

**Evidence to Collect:**

- Change tickets (all 3) with CAB approval timestamps
- Rollback plans (documented in tickets)
- Rollback test results (for CHG-10234, CHG-10567)
- Post-implementation review notes (for emergency CHG-10899)

**Common Pitfalls:**

- ❌ Not tracking provider-initiated changes (AWS announces new features—still needs documentation)
- ❌ Emergency changes marked "Compliant" (always Partial if testing bypassed, even if acceptable)
- ❌ No evidence of post-implementation review for emergency changes

---

### 4.3 Sheet 4: Incident Management

**Purpose:** Track security incidents involving cloud services and verify proper incident response procedures were followed.

**Policy Reference:** "Security incidents MUST be logged, responded to within SLA, and result in documented lessons learned." (ISMS-POL-A.5.19-23-S5 Section 6.3)

**Owner:** Incident Response Coordinator / SOC Manager

**Time Commitment:** 2-4 hours per quarter (depending on incident count)

---

#### Column-by-Column Guidance (Sheet 4)

**Extended Columns (R-X) - Incident Management Specific:**

| Column | Header | Type | How to Complete | Implementer Tip | Auditor Check |
|--------|--------|------|-----------------|-----------------|---------------|
| **R** | Incident Count (Quarter) | Number | Total incidents this quarter | Query incident system by date + service | Verify against SIEM/tickets |
| **S** | Incident Severity | Dropdown | P1/P2/P3/P4 (Critical/High/Medium/Low) | Highest severity if multiple | Match to incident ticket classification |
| **T** | Detection Method | Dropdown | SIEM Alert/User Report/Vendor Notification/Audit Finding | How was incident discovered | Validate detection capability |
| **U** | Response Time (Hours) | Number | Time from detection to response start | Calculate from timestamps | Check against SLA (P1: 1hr, P2: 4hr, P3: 24hr) |
| **V** | Resolution Time (Hours) | Number | Time from detection to closure | From incident ticket | Check against SLA |
| **W** | Lessons Learned Documented | Dropdown | Yes/No/Pending | Post-incident report exists | Review report for actionable items |
| **X** | Remediation Actions Completed | Dropdown | Yes/No/In Progress | From lessons learned action items | Check completion evidence |

---

#### Step-by-Step: Documenting an Incident

**Example Service: Salesforce**

**Scenario:** Phishing email led to compromised Salesforce credentials (1 incident, P2 severity)

**Step 1: Gather Incident Data**
```
1. Incident Ticket: SEC-2026-042
2. Detection: User reported suspicious email (User Report)
3. Response started: 2026-01-10 14:30
4. Incident detected: 2026-01-10 14:00
5. Incident closed: 2026-01-11 09:00
6. Lessons learned meeting: 2026-01-12
```

**Step 2: Fill Base Columns**
```
A: Salesforce
B: Salesforce (vendor)
C: SaaS
D: Q1
E: High
F: Confidential
G: Credential Compromise (incident type)
```

**Step 3: Calculate Incident Metrics**
```
R: 1 (incident this quarter)
S: P2 (High severity - credentials compromised but no data exfiltration)
T: User Report (employee reported phishing)
U: 0.5 (30 minutes from detection to response - within P2 SLA of 4 hours)
V: 18.5 (from 14:00 to 09:00 next day)
W: Yes (post-incident review completed 2026-01-12)
X: In Progress (2 of 3 action items complete: MFA enforced, user retrained; pending: phishing simulation rollout)
```

**Step 4: Status & Evidence**
```
H: ⚠️ Partial (incident handled well but remediation actions not fully complete)
I: /evidence/incidents/Q1_2026/SEC-2026-042_Salesforce_phishing.pdf
J: Remediation action pending: Deploy phishing simulation training org-wide (target: 2026-02-28)
K: Yes
L: (blank)
M: RSK-2026-015 (risk of phishing attacks on cloud services)
N: Compensating control: MFA enforced on all Salesforce accounts (prevents future credential compromise impact)
O: Security Team
P: 2026-02-28
Q: 2026-01-12 (lessons learned meeting date)
```

**Evidence to Collect:**

- Incident ticket (SEC-2026-042) with full timeline
- Post-incident report with lessons learned
- Action item tracker (showing 2/3 complete)
- MFA enforcement evidence (screenshots of Salesforce admin console)

**Special Case: No Incidents This Quarter**
```
If NO incidents occurred:
A: [Service Name]
B-F: [Standard info]
G: No Incidents
H: ✅ Compliant (no incidents is good!)
I: /evidence/incidents/Q1_2026/SIEM_query_no_alerts_[service].pdf
J: (blank)
K: No
L-P: (blank)
Q: 2026-01-31 (date SIEM queried)
R: 0
S-X: N/A
```

**Implementer Perspective:**
*"Document even 'near misses' (incidents detected before impact). They show your detection works and provide learning opportunities."*

**Auditor Perspective:**
*"I'll check if 'No Incidents' is backed by evidence (SIEM query showing zero alerts) or just memory. Zero incidents without proof is suspicious."*

---

### 4.4 Sheet 5: Business Continuity & Disaster Recovery

**Purpose:** Validate that BC/DR plans exist, are current, and have been tested for critical cloud services.

**Policy Reference:** "BC/DR plans MUST exist for Critical/High services and be tested annually minimum." (ISMS-POL-A.5.19-23-S5 Section 6.4)

**Owner:** Business Continuity Planner / Resilience Manager

**Time Commitment:** 4-6 hours per quarter (annual for testing, quarterly for validation)

---

#### Column-by-Column Guidance (Sheet 5)

**Extended Columns (R-X) - BC/DR Specific:**

| Column | Header | Type | How to Complete | Implementer Tip | Auditor Check |
|--------|--------|------|-----------------|-----------------|---------------|
| **R** | BC/DR Plan Exists | Dropdown | Yes/No/In Development | Document must be current (<12 months) | Check plan document date |
| **S** | Last Plan Review Date | Date | When plan was last reviewed | Annual minimum for Critical/High | Flag if >12 months old |
| **T** | RTO (Hours) | Number | Recovery Time Objective | From BC plan | Verify against business requirements |
| **U** | RPO (Hours) | Number | Recovery Point Objective | From BC plan | Check backup frequency matches |
| **V** | Last Test Date | Date | When recovery was last tested | Annual minimum for Critical | Evidence of actual test, not just review |
| **W** | Test Outcome | Dropdown | Successful/Failed/Partial/Not Tested | From test report | Failed tests require remediation |
| **X** | Next Test Due | Date | Last Test + 365 days | Set reminder | Overdue tests are non-compliant |

---

#### Step-by-Step: BC/DR Assessment

**Example Service: Critical Database (AWS RDS)**

**Scenario:** Annual BC/DR test conducted, RTO target met

**Step 1: Review BC Plan**
```
1. Locate BC plan: /BC_plans/AWS_RDS_production_BC_plan_v3.2.pdf
2. Plan last updated: 2025-11-15 (within 12 months)
3. RTO: 4 hours (from failure to restored service)
4. RPO: 1 hour (max data loss acceptable)
```

**Step 2: Review Test Results**
```
1. Last test conducted: 2025-12-05
2. Test scenario: Simulated primary region failure, failover to DR region
3. Actual RTO achieved: 3.5 hours (better than 4-hour target)
4. Actual RPO: 45 minutes (better than 1-hour target)
5. Test outcome: Successful
6. Issues found: None (failover procedure worked as documented)
```

**Step 3: Fill Columns**
```
Base Columns:
A: AWS RDS Production Database
B: Amazon Web Services
C: IaaS
D: Q1
E: Critical
F: Restricted
G: Annual BC/DR Test Completed

Extended Columns:
R: Yes (plan exists and current)
S: 2025-11-15 (plan review date)
T: 4 (RTO target in hours)
U: 1 (RPO target in hours)
V: 2025-12-05 (last test date)
W: Successful (RTO/RPO both achieved)
X: 2026-12-05 (next test due in 12 months)

Status & Evidence:
H: ✅ Compliant (plan current, tested annually, successful)
I: /evidence/bcdr/2025_AWS_RDS_failover_test_report.pdf
J: (blank - no gaps)
K: No
L-P: (blank)
Q: 2025-12-05
```

**Evidence to Collect:**

- BC/DR plan document (dated, version-controlled)
- Test report with:
  - Test scenario description
  - Actual RTO/RPO achieved (with timestamps)
  - Screenshots of failover process
  - Issues found and resolutions
  - Sign-off from BC team and service owner

**Special Case: Service Without BC Plan (Medium/Low Criticality)**
```
For non-critical services where BC plan may not be required:
R: No (BC plan not required for Medium criticality)
S: N/A
T: N/A
U: N/A
V: N/A
W: Not Tested
X: N/A

H: ✅ Compliant (no BC plan required per policy)
I: /evidence/bcdr/BC_exemption_memo_[service].pdf
J: BC plan waived per policy (Medium criticality, non-essential service)
```

**Implementer Perspective:**
*"Don't confuse 'BC plan exists' with 'BC plan tested.' Auditors want evidence that recovery actually works, not just a plan document."*

**Auditor Perspective:**
*"I'll check test report timestamps—tests older than 12 months for Critical services mean the plan is untested (environment has changed)."*

---

### 4.5 Sheet 6: Vendor Risk Monitoring

**Purpose:** Continuously monitor vendor security posture, certifications, incidents, and financial health.

**Policy Reference:** "Vendor security posture MUST be monitored quarterly. Certification expiry MUST be tracked and renewals verified." (ISMS-POL-A.5.19-23-S5 Section 6.5)

**Owner:** Vendor Manager / Risk Manager / Procurement

**Time Commitment:** 3-5 hours per quarter

---

#### Column-by-Column Guidance (Sheet 6)

**Extended Columns (R-X) - Vendor Risk Monitoring Specific:**

| Column | Header | Type | How to Complete | Implementer Tip | Auditor Check |
|--------|--------|------|-----------------|-----------------|---------------|
| **R** | ISO 27001 Cert Status | Dropdown | Valid/Expiring Soon/Expired/Not Certified | Check cert portal | "Expiring Soon" = <90 days |
| **S** | SOC 2 Report Date | Date | Date of most recent SOC 2 report | Type II preferred | Report <12 months old |
| **T** | Vendor Incidents (Quarter) | Number | Security incidents reported by vendor | From vendor notifications | Check vendor status pages |
| **U** | Financial Health | Dropdown | Stable/Concern/At Risk/Unknown | D&B rating or public filings | Critical vendors only |
| **V** | Sub-processor Changes | Dropdown | Yes/No/Unknown | From vendor notifications | Changes require re-assessment |
| **W** | Last Vendor Meeting | Date | Date of last QBR or security review | Quarterly for Critical vendors | Check meeting notes |
| **X** | Vendor Risk Rating | Dropdown | Low/Medium/High/Critical | From risk assessment | Change from baseline triggers review |

---

#### Step-by-Step: Vendor Risk Monitoring

**Example Service: Slack (Communication Platform)**

**Scenario:** Quarterly vendor risk check, cert renewal detected

**Step 1: Check Certifications**
```
1. Visit Slack Trust Portal: https://slack.com/trust
2. ISO 27001 cert: Valid until 2026-08-15 (7 months away - not "Expiring Soon" yet)
3. SOC 2 Type II report: 2025-12-01 (2 months old - current)
4. Download cert copies for evidence
```

**Step 2: Check Vendor Incidents**
```
1. Review Slack Status Page (https://status.slack.com)
2. Search vendor security notifications email folder
3. Found 1 minor incident Q1: Brief API latency (5 min), no security impact
```

**Step 3: Check Sub-processors**
```
1. Review Slack DPA Annex (sub-processor list)
2. Compare to last quarter's list
3. No changes detected
```

**Step 4: Vendor Meeting (if scheduled)**
```
1. Last QBR: 2025-11-20 (3 months ago for quarterly cadence)
2. Next QBR: Scheduled 2026-02-15
3. No urgent security concerns raised
```

**Step 5: Fill Columns**
```
Base Columns:
A: Slack
B: Slack Technologies
C: SaaS
D: Q1
E: High (business-critical communication)
F: Confidential
G: Quarterly Vendor Review

Extended Columns:
R: Valid (ISO 27001 expires 2026-08-15, >90 days)
S: 2025-12-01 (SOC 2 Type II report date)
T: 1 (minor incident, no security impact)
U: Stable (publicly traded, strong financials)
V: No (no sub-processor changes)
W: 2025-11-20 (last QBR)
X: Medium (up from Low last quarter due to 1 incident, but still acceptable)

Status & Evidence:
H: ✅ Compliant (all checks passed, vendor risk acceptable)
I: /evidence/vendor/Q1_2026/Slack_certs_SOC2_incident_log.pdf
J: (blank - no gaps)
K: No
L-P: (blank)
Q: 2026-01-20 (quarterly check date)
```

**Evidence to Collect:**

- ISO 27001 certificate (PDF from trust portal)
- SOC 2 Type II report (request from vendor if not public)
- Vendor incident log (screenshots of status page + emails)
- Sub-processor list (from DPA)
- QBR meeting notes (if applicable)

**Common Pitfalls:**

- ❌ Trusting vendor claims without verifying (download certs, don't just check website)
- ❌ Not tracking cert expiry dates (certification lapses can occur between reviews)
- ❌ Ignoring vendor "minor" incidents (patterns matter—5 minor incidents = problem)

---

### 4.6 Sheet 7: Exit Strategy Review

**Purpose:** Validate that exit plans remain viable and test feasibility annually for critical services.

**Policy Reference:** "Exit strategies MUST be reviewed annually. PoC migration testing SHOULD be conducted for Critical services." (ISMS-POL-A.5.19-23-S5 Section 8.3)

**Owner:** IT Operations / Cloud Architect / Service Owner

**Time Commitment:** 6-8 hours per year (annual activity, quarterly validation)

---

#### Column-by-Column Guidance (Sheet 7)

**Extended Columns (R-X) - Exit Strategy Specific:**

| Column | Header | Type | How to Complete | Implementer Tip | Auditor Check |
|--------|--------|------|-----------------|-----------------|---------------|
| **R** | Exit Plan Documented | Dropdown | Yes/No/In Development | Must be current (<12 months) | Check plan document exists |
| **S** | Last Plan Review | Date | When exit plan was last reviewed | Annual minimum | Flag if >12 months |
| **T** | Alternative Provider Identified | Dropdown | Yes/No/Multiple Options | Documented in exit plan | Check alternatives are viable |
| **U** | Migration Complexity | Dropdown | Low/Medium/High/Very High | Technical assessment | Justify rating |
| **V** | PoC Test Conducted | Dropdown | Yes/No/Planned/N/A | For Critical services only | Evidence of actual data migration test |
| **W** | PoC Test Outcome | Dropdown | Successful/Failed/Partial/N/A | From test report | Failed = update exit plan |
| **X** | Exit Trigger Monitoring | Dropdown | Yes/No | Are exit triggers being monitored? | Check monitoring process |

---

#### Step-by-Step: Exit Strategy Review

**Example Service: GitHub Enterprise (Critical)**

**Scenario:** Annual exit plan review + PoC migration test conducted

**Step 1: Review Exit Plan**
```
1. Locate exit plan: /exit_plans/GitHub_Enterprise_exit_plan_v2.1.pdf
2. Plan last updated: 2025-09-01 (4 months ago - current)
3. Alternative identified: GitLab Ultimate (primary), Bitbucket Premium (secondary)
4. Migration complexity: Medium (repos exportable, CI/CD requires reconfiguration)
```

**Step 2: Conduct PoC Test (Annual)**
```
1. Test date: 2025-10-15
2. Test scope: Migrate 5 sample repositories to GitLab test instance
3. Test results:

   - Repository migration: Successful (all commits, branches, tags preserved)
   - CI/CD migration: Partial (70% of pipelines migrated, 30% require manual adjustment)
   - Secrets management: Manual migration required

4. Test outcome: Partial success (migration viable but requires effort)
```

**Step 3: Monitor Exit Triggers**
```
Exit triggers defined in plan:
1. GitHub security incident (monitor vendor notifications)
2. Price increase >30% (monitor contract renewal)
3. End-of-life announcement (monitor vendor roadmap)

Monitoring status: Active (vendor notifications forwarded to IT Ops)
```

**Step 4: Fill Columns**
```
Base Columns:
A: GitHub Enterprise
B: GitHub (Microsoft)
C: SaaS
D: Q1 (annual review in Q4 2025, quarterly validation in Q1 2026)
E: Critical
F: Confidential
G: Annual Exit Plan Review + PoC

Extended Columns:
R: Yes (plan exists, current)
S: 2025-09-01 (plan review date)
T: Yes (GitLab primary, Bitbucket secondary)
U: Medium (repos portable, CI/CD requires work)
V: Yes (PoC conducted 2025-10-15)
W: Partial (migration viable but CI/CD needs manual work)
X: Yes (exit triggers monitored via vendor notifications)

Status & Evidence:
H: ✅ Compliant (plan current, alternatives viable, PoC tested)
I: /evidence/exit/2025_GitHub_PoC_migration_test_report.pdf
J: PoC identified CI/CD migration complexity (30% pipelines need manual adjustment)
K: No (not a gap, just documented complexity)
L-P: (blank)
Q: 2025-10-15 (PoC test date)
```

**Evidence to Collect:**

- Exit plan document (version-controlled, dated)
- Alternative provider assessments (GitLab/Bitbucket capability comparison)
- PoC test report:
  - Test scope and methodology
  - Migration success rates
  - Issues encountered
  - Effort estimates
  - Screenshots of migrated repositories
- Exit trigger monitoring process (email forwarding rules, status page subscriptions)

**Special Case: Low/Medium Criticality Services (PoC Not Required)**
```
For services where PoC testing is not required:
R: Yes (plan exists)
S: 2025-11-01
T: Yes (alternative identified)
U: Low (standard SaaS, easy export)
V: N/A (PoC not required for Medium criticality)
W: N/A
X: Yes (basic trigger monitoring)

H: ✅ Compliant (plan adequate for Medium criticality service)
```

**Implementer Perspective:**
*"PoC testing is effort-intensive. Prioritize Critical services. For others, verify export capability works (download data, check format)."*

**Auditor Perspective:**
*"I'll check if PoC test actually migrated data (not just reviewed export documentation). Test reports should have screenshots and metrics."*

---

### 4.7 Sheet 8: Jurisdictional Risk Assessment

**Purpose:** Monitor ongoing jurisdictional risks (CLOUD Act exposure, transfer mechanisms, vendor jurisdiction changes).

**Policy Reference:** "Jurisdictional risks MUST be reassessed quarterly. TIAs MUST be reviewed annually." (Regulatory requirement: DORA, NIS2, GDPR)

**Owner:** Data Protection Officer (DPO) / Legal / Compliance

**Time Commitment:** 2-3 hours per quarter

---

#### Column-by-Column Guidance (Sheet 8)

**Extended Columns (R-X) - Jurisdictional Risk Specific:**

| Column | Header | Type | How to Complete | Implementer Tip | Auditor Check |
|--------|--------|------|-----------------|-----------------|---------------|
| **R** | Provider HQ Jurisdiction | Dropdown | US/EU/UK/Switzerland/Other | May change if vendor acquired | Monitor M&A announcements |
| **S** | Data Processing Location | Dropdown | EU-Only/EU+US/US-Only/Multi-Region | From DPA | Verify against vendor docs |
| **T** | CLOUD Act Exposure | Dropdown | No Exposure/Potential/Mitigated/Accepted | US-nexus = exposure | DPO assessment required |
| **U** | Transfer Mechanism | Dropdown | SCCs/BCRs/Adequacy/TIA/None | From DPA | SCCs must be current template |
| **V** | TIA Status | Dropdown | N/A/Required/In Progress/Complete | For US providers if required | TIA signed by Legal/DPO |
| **W** | Customer-Managed Keys | Dropdown | Yes/No/Planned/N/A | CMK reduces CLOUD Act risk | Verify CMK actually deployed |
| **X** | Risk Acceptance | Dropdown | N/A/Accepted/Requires Mitigation | For residual risks | CISO/DPO sign-off required |

---

#### Step-by-Step: Jurisdictional Risk Monitoring

**Example Service: Salesforce (US-based vendor, EU data residency)**

**Scenario:** Quarterly jurisdictional risk check, TIA validity verification

**Step 1: Verify Current Jurisdiction Status**
```
1. Provider HQ: United States (Salesforce.com, Inc. - San Francisco)
2. Data processing: EU-only (via Hyperforce EU instance)
3. Check for any vendor M&A or jurisdiction changes: None this quarter
```

**Step 2: Review Transfer Mechanisms**
```
1. DPA in place: Yes (Salesforce Data Processing Addendum v4.0)
2. Transfer mechanism: SCCs (Standard Contractual Clauses - EU Commission template)
3. TIA status: Complete (Transfer Impact Assessment conducted 2025-06-15 by Legal + DPO)
4. TIA valid until: 2026-06-15 (annual review)
```

**Step 3: Check Mitigations**
```
1. Customer-managed keys: No (Salesforce Shield Encryption uses Salesforce-managed keys)
2. Compensating controls:

   - Data residency: EU-only Hyperforce instance
   - SCC: Current EU template
   - TIA: Documented risk acceptance

```

**Step 4: Fill Columns**

Base Columns:
A: Salesforce
B: Salesforce (US)
C: SaaS
D: Q1
E: High
F: Confidential
G: Quarterly Jurisdictional Review
Extended Columns:
R: US (Salesforce HQ)
S: EU-Only (Hyperforce EU instance)
T: Mitigated (US-nexus but EU data residency + SCCs + TIA)
U: SCCs (current EU template)
V: Complete (TIA signed 2025-06-15, valid 12 months)
W: No (Shield uses Salesforce-managed keys, not CMK)
X: Accepted (residual CLOUD Act risk accepted by DPO/CISO given mitigations)
Status & Evidence:
H: ✅ Compliant (all transfer mechanisms valid, TIA current, risk accepted)
I: /evidence/jurisdictional/Q1_2026/Salesforce_DPA_TIA_risk_acceptance.pdf
J: (blank - no gaps)
K: No
L-P: (blank)
Q: 2026-01-18 (quarterly review date)

**Evidence to Collect:**

- DPA with SCCs (signed document)
- TIA (Transfer Impact Assessment signed by Legal + DPO)
- Risk acceptance memo (CISO/DPO signature)
- Data residency verification (Salesforce Hyperforce instance configuration screenshot)

**Common Pitfalls:**

- ❌ Assuming US vendor = automatic CLOUD Act violation (EU data residency + mitigations can be acceptable)
- ❌ Using outdated SCC template (Schrems II invalidated old templates)
- ❌ TIA not renewed annually (risk landscape changes)
- ❌ No risk acceptance documentation (DPO/CISO must formally accept residual risk)

---

**END OF SECTION 4 (~1,000 lines)**

This delivery covers:

- ✅ Section 4: Completing Each Sheet (Detailed Guidance) - All 7 sheets (2-8)

**Next delivery will cover:**

- Section 5: Evidence Collection Guide
- Section 6: Common Pitfalls & How to Avoid Them
- Section 7: Quality Checklist

**Ready for next part?** 🚀

---

## Section 5: Evidence Collection Guide

### 5.1 Evidence Collection Strategy

**Core Principle:** Evidence must be **objective, timestamped, retrievable, and verifiable**. "We did it" is not evidence—a dated report showing what was done is evidence.

---

#### 5.1.1 Evidence Hierarchy (What Auditors Trust)

**Tier 1 - Strongest Evidence (System-Generated, Immutable):**
```
✅ SIEM logs with timestamps
✅ IAM system exports (access lists, last login dates)
✅ Change management tickets with approval workflows
✅ Incident tickets with resolution timestamps
✅ Vendor certification PDFs (from official cert authority)
✅ Cloud provider audit logs (AWS CloudTrail, Azure Monitor, GCP Cloud Logging)
```

**Tier 2 - Good Evidence (Documented Processes with Sign-Offs):**
```
✅ BC/DR test reports with manager sign-off
✅ Access review reports with manager attestations
✅ Vendor QBR meeting minutes with attendee list
✅ Exit plan documents (version-controlled, dated)
✅ Risk assessments with DPO/CISO signatures
```

**Tier 3 - Acceptable Evidence (Screenshots, Exports with Context):**
```
⚠️ Screenshots of cloud admin consoles (with timestamp, service name visible)
⚠️ Email confirmations from vendors (with full headers)
⚠️ Exported CSV/Excel from systems (with export date)
⚠️ PDF downloads from vendor portals (with URL, download date)
```

**Tier 4 - Weak Evidence (Avoid if Possible):**
```
❌ Verbal confirmations ("vendor said it's secure")
❌ Undated documents ("we have a BC plan" - when was it last updated?)
❌ Personal notes without corroboration ("I reviewed access on Monday")
❌ Marketing materials as proof ("vendor brochure says 99.99% uptime")
```

**Implementer Perspective:**
*"Aim for Tier 1-2 evidence. If you must use Tier 3, add context (who took screenshot, when, why). Never use Tier 4 alone."*

**Auditor Perspective:**
*"I can verify Tier 1 evidence independently (query SIEM myself). Tier 2 requires trust verification (signatures genuine?). Tier 3 is circumstantial. Tier 4 gets rejected."*

---

#### 5.1.2 Evidence Folder Structure

**Recommended Organization:**
```
/evidence/governance/
├── Q1_2026/
│   ├── access_reviews/
│   │   ├── AWS_access_review_Q1_2026.pdf
│   │   ├── M365_access_review_Q1_2026.pdf
│   │   ├── Salesforce_access_review_Q1_2026.pdf
│   │   └── orphan_accounts_remediation_tickets.pdf
│   ├── changes/
│   │   ├── AWS_changes_Q1_2026_CHG-10234_to_10899.pdf
│   │   ├── emergency_change_post_review_CHG-10899.pdf
│   │   └── change_success_rate_Q1_2026.xlsx
│   ├── incidents/
│   │   ├── SEC-2026-042_Salesforce_phishing_ticket.pdf
│   │   ├── SEC-2026-042_lessons_learned_report.pdf
│   │   └── SIEM_query_no_incidents_Q1_2026.pdf
│   ├── bcdr/
│   │   ├── AWS_RDS_failover_test_2025-12-05.pdf
│   │   ├── BC_plan_reviews_Q1_2026.xlsx
│   │   └── RTO_RPO_validation_summary.pdf
│   ├── vendor/
│   │   ├── Slack_ISO27001_cert_valid_until_2026-08-15.pdf
│   │   ├── Slack_SOC2_Type_II_2025-12-01.pdf
│   │   ├── vendor_incident_log_Q1_2026.xlsx
│   │   └── QBR_meeting_notes/
│   ├── exit/
│   │   ├── GitHub_exit_plan_v2.1.pdf
│   │   ├── GitHub_PoC_migration_test_2025-10-15.pdf
│   │   └── alternative_providers_assessment.xlsx
│   └── jurisdictional/
│       ├── Salesforce_DPA_with_SCCs.pdf
│       ├── Salesforce_TIA_2025-06-15_signed.pdf
│       ├── risk_acceptance_memo_US_vendors.pdf
│       └── data_residency_verification_screenshots/
├── Q2_2026/
│   └── [same structure]
└── manifests/
    ├── Q1_2026_evidence_manifest.txt
    └── Q2_2026_evidence_manifest.txt
```

---

#### 5.1.3 Evidence Naming Conventions

**Template:** `[ServiceName]_[EvidenceType]_[Date]_[Optional-Details].pdf`

**Good Examples:**
```
✅ AWS_access_review_2026-01-15_245_accounts.pdf
✅ Salesforce_incident_SEC-2026-042_phishing.pdf
✅ GitHub_PoC_migration_test_2025-10-15.pdf
✅ Slack_ISO27001_cert_expires_2026-08-15.pdf
```

**Bad Examples:**
```
❌ access_review.pdf (which service? which date?)
❌ incident.pdf (no context)
❌ document1.pdf (meaningless)
❌ final_FINAL_v3_really_final.pdf (unprofessional)
```

---

### 5.2 Evidence Collection by Sheet

#### Sheet 2: Access Review Evidence

**Required Evidence:**

**1. Access Review Report (Primary Evidence)**
```
Content Must Include:
☐ Service name (e.g., "Microsoft 365")
☐ Review date (e.g., "2026-01-15")
☐ Total accounts reviewed (e.g., "245")
☐ Account breakdown by type (users, admins, service accounts, guests)
☐ Orphan accounts identified (e.g., "3 terminated employees")
☐ Excessive privileges identified (e.g., "5 former managers")
☐ Remediation actions taken (e.g., "8 accounts disabled/downgraded")
☐ Manager attestations (e.g., "Department heads confirmed access appropriate")
☐ Review completion sign-off (name, title, date)

Format: PDF export from IAM system OR structured report template
Example: /evidence/access_reviews/Q1_2026/M365_access_review_2026-01-15.pdf
```

**2. Orphan Account Remediation Tickets (Supporting Evidence)**
```
If orphans found, provide:
☐ Ticket IDs (e.g., "INC-2026-1234, INC-2026-1235, INC-2026-1236")
☐ Account names (redacted if sensitive)
☐ Discovery date
☐ Remediation date (must be <24 hours from discovery)
☐ Remediation action (disabled, deleted, reassigned)

Format: Ticket export or screenshot
Example: /evidence/access_reviews/Q1_2026/orphan_remediation_INC-2026-1234_to_1236.pdf
```

**3. Manager Attestation Emails (Supporting Evidence)**
```
For each department/team:
☐ Manager name and title
☐ Attestation statement ("I confirm access is appropriate for these users")
☐ Email date (within review period)
☐ List of users attested

Format: Email thread PDF or attestation form
Example: /evidence/access_reviews/Q1_2026/manager_attestations/IT_dept_attestation.pdf
```

**Quick Collect Method (Microsoft Graph PowerShell):**
```powershell
# Entra ID example
Connect-MgGraph -Scopes "User.Read.All", "AuditLog.Read.All"

# 1. Export user list:
Get-MgUser -All | Select-Object UserPrincipalName, DisplayName, AccountEnabled,
   SignInActivity | Export-Csv "M365_users_2026-01-15.csv" -NoTypeInformation

# 2. Run orphan detection:
Get-MgUser -All -Filter "accountEnabled eq true" |
   Where-Object {$_.SignInActivity.LastSignInDateTime -lt (Get-Date).AddDays(-90)} |
   Export-Csv "M365_orphans_2026-01-15.csv" -NoTypeInformation

# 3. Generate report, save as PDF with screenshot of admin console
# 4. Collect manager email confirmations
# 5. Archive all in /evidence/access_reviews/Q1_2026/
```

---

#### Sheet 3: Change Management Evidence

**Required Evidence:**

**1. Change Tickets (Primary Evidence)**
```
For each change, provide ticket with:
☐ Change ID (e.g., "CHG-10234")
☐ Service affected (e.g., "AWS Production")
☐ Change type (Provider/Org/Emergency)
☐ Change description (what's changing)
☐ Impact assessment (who/what affected)
☐ Rollback plan (documented steps)
☐ CAB approval (or emergency override justification)
☐ Implementation date/time
☐ Outcome (successful/failed/rolled back)
☐ Post-implementation validation

Format: Ticket export from ITSM system
Example: /evidence/changes/Q1_2026/CHG-10234_AWS_security_group_update.pdf
```

**2. Rollback Test Results (Supporting Evidence, for High/Critical changes)**
```
☐ Rollback procedure (step-by-step)
☐ Test date (before change implementation)
☐ Test environment (staging/dev)
☐ Test outcome (successful restoration)
☐ Screenshots of rollback execution

Format: Test report or ticket attachment
Example: /evidence/changes/Q1_2026/CHG-10234_rollback_test_2025-12-20.pdf
```

**3. Emergency Change Post-Review (Required for Emergency changes)**
```
Within 48 hours of emergency change:
☐ Change justification (why emergency process used)
☐ Impact assessment (was there a better option?)
☐ Lessons learned (how to prevent future emergencies)
☐ Process improvement (update CAB process if needed)
☐ Sign-off from IT Ops Manager + CISO

Format: Post-review meeting notes or report
Example: /evidence/changes/Q1_2026/CHG-10899_emergency_post_review_2026-01-20.pdf
```

---

#### Sheet 4: Incident Management Evidence

**Required Evidence:**

**1. Incident Ticket (Primary Evidence)**
```
☐ Incident ID (e.g., "SEC-2026-042")
☐ Service affected (e.g., "Salesforce")
☐ Severity (P1/P2/P3/P4)
☐ Detection method (SIEM/User Report/Vendor/Audit)
☐ Detection timestamp (when first observed)
☐ Response start timestamp (when team engaged)
☐ Resolution timestamp (when incident closed)
☐ Root cause (what happened)
☐ Impact (data accessed? systems compromised?)
☐ Remediation actions (what was done)

Format: Incident ticket export
Example: /evidence/incidents/Q1_2026/SEC-2026-042_Salesforce_phishing.pdf
```

**2. Post-Incident Report / Lessons Learned (Required for P1/P2)**
```
☐ Incident summary (high-level overview)
☐ Timeline (detailed chronology of events)
☐ Root cause analysis (5 Whys or Fishbone)
☐ What went well (detection, response, communication)
☐ What went poorly (gaps, delays, failures)
☐ Action items (with owners and due dates)
☐ Follow-up verification (action items completed)
☐ Sign-off (IR lead + CISO)

Format: Structured report (template-based)
Example: /evidence/incidents/Q1_2026/SEC-2026-042_lessons_learned_2026-01-12.pdf
```

**3. SIEM Query Results (For "No Incidents" claims)**
```
If claiming zero incidents:
☐ SIEM query showing date range (quarter start to end)
☐ Filter criteria (e.g., "severity:HIGH OR severity:CRITICAL, source:cloud_services")
☐ Result count (should be zero)
☐ Query timestamp (when checked)
☐ Analyst name (who verified)

Format: SIEM export or screenshot
Example: /evidence/incidents/Q1_2026/SIEM_no_incidents_AWS_Q1_2026.pdf
```

---

#### Sheet 5: BC/DR Evidence

**Required Evidence:**

**1. BC/DR Plan Document (Primary Evidence)**
```
☐ Service name
☐ Document version (e.g., "v3.2")
☐ Last review date (annual minimum)
☐ RTO target (hours to recovery)
☐ RPO target (max data loss in hours)
☐ Recovery procedures (step-by-step)
☐ Escalation contacts (names, roles, phone numbers)
☐ Dependencies (what else needs to work for recovery)
☐ Alternative providers (if primary fails completely)

Format: Version-controlled document (PDF)
Example: /evidence/bcdr/AWS_RDS_BC_plan_v3.2_reviewed_2025-11-15.pdf
```

**2. BC/DR Test Report (Required annually for Critical/High)**
```
☐ Test date
☐ Test scenario (what was simulated)
☐ Test scope (full DR region failover vs. partial)
☐ RTO achieved (actual hours to recovery)
☐ RPO achieved (actual data loss)
☐ Issues encountered (problems during test)
☐ Resolutions (how issues were fixed)
☐ Lessons learned (what to improve)
☐ Next test date (schedule next annual test)
☐ Sign-off (BC Planner + Service Owner)

Format: Test report with screenshots
Example: /evidence/bcdr/AWS_RDS_failover_test_2025-12-05.pdf
```

**3. Backup Validation (Quarterly for Critical)**
```
☐ Backup schedule verification (frequency matches RPO)
☐ Recent backup restore test (sample data restored successfully)
☐ Backup storage location (geographic redundancy)
☐ Encryption status (backups encrypted at rest)

Format: Backup report or restore test results
Example: /evidence/bcdr/AWS_RDS_backup_validation_Q1_2026.pdf
```

---

#### Sheet 6: Vendor Risk Monitoring Evidence

**Required Evidence:**

**1. Vendor Certifications (Primary Evidence)**
```
For ISO 27001:
☐ Certificate PDF (from accredited body)
☐ Scope of certification (what's covered)
☐ Validity period (issue date to expiry date)
☐ Certificate number (for verification)
☐ Accreditation body (UKAS, ANAB, etc.)

Format: PDF from vendor trust portal or cert authority
Example: /evidence/vendor/Q1_2026/Slack_ISO27001_cert_valid_until_2026-08-15.pdf

For SOC 2:
☐ Type II report (Type I is insufficient for high-trust)
☐ Report date (should be <12 months old)
☐ Audit period covered (typically 6-12 months)
☐ Opinion (unqualified/qualified)
☐ Exceptions noted (if any)

Format: PDF from vendor (under NDA typically)
Example: /evidence/vendor/Q1_2026/Slack_SOC2_Type_II_2025-12-01.pdf
```

**2. Vendor Incident Log (Quarterly)**
```
☐ Vendor name
☐ Quarter covered (e.g., "Q1 2026")
☐ Incidents reported (from vendor notifications, status pages)
☐ Incident severity (vendor's classification)
☐ Impact to [Organization] (did it affect us?)
☐ Vendor response (how quickly resolved)

Format: Tracking spreadsheet + incident notification emails
Example: /evidence/vendor/Q1_2026/vendor_incident_log_Q1_2026.xlsx
```

**3. Vendor QBR Meeting Notes (Quarterly for Critical vendors)**
```
☐ Meeting date
☐ Attendees (vendor and [Organization] representatives)
☐ Agenda (topics discussed)
☐ Security topics covered (incidents, roadmap, certifications)
☐ Performance review (SLA compliance, issues)
☐ Action items (with owners and due dates)

Format: Meeting minutes (PDF)
Example: /evidence/vendor/Q1_2026/Slack_QBR_2025-11-20_meeting_notes.pdf
```

---

#### Sheet 7: Exit Strategy Evidence

**Required Evidence:**

**1. Exit Plan Document (Annual review)**
```
☐ Service name
☐ Document version and date
☐ Exit triggers (conditions that would prompt exit)
☐ Alternative providers (minimum 1, preferably 2)
☐ Migration approach (cloud-to-cloud, hybrid, on-prem)
☐ Data extraction procedure (APIs, exports, manual)
☐ Migration effort estimate (person-hours, calendar time)
☐ Migration cost estimate (vendor costs, internal labor)
☐ Communication plan (stakeholder notifications)
☐ Rollback plan (if migration fails mid-way)

Format: Structured document (PDF)
Example: /evidence/exit/GitHub_exit_plan_v2.1_reviewed_2025-09-01.pdf
```

**2. PoC Migration Test Report (Annual for Critical, optional for others)**
```
☐ Test date
☐ Test scope (how much data migrated)
☐ Test environment (production-like staging)
☐ Migration method (API, export/import, third-party tool)
☐ Success rate (% of data successfully migrated)
☐ Issues encountered (data format conversions, API limits)
☐ Effort actual vs. estimate (was estimate accurate?)
☐ Lessons learned (what would we do differently in real exit)
☐ Recommendation (exit plan viable? needs update?)

Format: Test report with screenshots
Example: /evidence/exit/GitHub_PoC_migration_test_2025-10-15.pdf
```

**3. Alternative Provider Assessment (When exit plan updated)**
```
For each alternative:
☐ Provider name
☐ Service offering (equivalent capabilities)
☐ Security certifications (ISO 27001, SOC 2)
☐ Data residency options (EU, US, multi-region)
☐ Pricing comparison (vs. current provider)
☐ Migration compatibility (import formats supported)
☐ Feature gaps (what would we lose/gain)

Format: Comparison spreadsheet
Example: /evidence/exit/alternative_providers_GitLab_vs_Bitbucket.xlsx
```

---

#### Sheet 8: Jurisdictional Risk Evidence

**Required Evidence:**

**1. Data Processing Agreement (DPA) with SCCs (Required for all EU data)**
```
☐ Signed DPA between [Organization] and vendor
☐ Standard Contractual Clauses (current EU template)
☐ Annexes (data categories, security measures, sub-processors)
☐ Signing date (both parties)
☐ Validity check (no amendments that weaken SCCs)

Format: Signed PDF
Example: /evidence/jurisdictional/Q1_2026/Salesforce_DPA_with_SCCs_signed_2024-05-10.pdf
```

**2. Transfer Impact Assessment (TIA) (Required for US-nexus vendors processing EU data)**
```
☐ Vendor name and jurisdiction
☐ Assessment date (annual review required)
☐ CLOUD Act exposure analysis (can US govt access data?)
☐ Mitigating measures (data residency, encryption, CMK)
☐ Residual risk assessment (what risk remains)
☐ Risk acceptance or further mitigation decision
☐ DPO sign-off (confirming GDPR compliance)
☐ Legal sign-off (confirming legal sufficiency)

Format: Structured assessment report
Example: /evidence/jurisdictional/Q1_2026/Salesforce_TIA_2025-06-15_signed_DPO_Legal.pdf
```

**3. Risk Acceptance Memo (If residual jurisdictional risk exists)**
```
☐ Service name
☐ Jurisdictional risk summary (e.g., "US CLOUD Act exposure")
☐ Mitigations in place (SCCs, EU data residency, TIA)
☐ Residual risk (what remains despite mitigations)
☐ Business justification (why accepting risk)
☐ CISO sign-off (accepting residual risk)
☐ DPO sign-off (confirming GDPR compliance despite risk)

Format: Memo or risk acceptance form
Example: /evidence/jurisdictional/Q1_2026/risk_acceptance_Salesforce_CLOUD_Act.pdf
```

**4. Data Residency Verification (For vendors claiming EU-only processing)**
```
☐ Vendor documentation (where data is processed/stored)
☐ Screenshot from admin console (showing region selection)
☐ Configuration verification (data residency settings)
☐ Sub-processor list (verify no US sub-processors for EU data)

Format: Screenshots + vendor docs
Example: /evidence/jurisdictional/Q1_2026/Salesforce_Hyperforce_EU_data_residency.pdf
```

---

### 5.3 Evidence Register (Sheet 10) - How to Use

**Purpose:** Centralized audit trail linking every assessment finding to its evidence.

**How to Complete:**
```
For each piece of evidence collected:

Column A (Evidence ID): Auto-generated (EV-GOV-001, EV-GOV-002, ...)
Column B (Assessment Area): Which sheet? (Access Review, Change Mgmt, Incidents, etc.)
Column C (Cloud Service): Which service? (Microsoft 365, AWS, etc.)
Column D (Evidence Type): What kind? (Access Review Report, Incident Ticket, BC Test Report, etc.)
Column E (Description): Brief summary (e.g., "Q1 2026 access review for M365, 245 accounts, 3 orphans")
Column F (Location/Path): Where stored? (/evidence/access_reviews/Q1_2026/M365_access_review.pdf)
Column G (Date Collected): When obtained? (2026-01-15)
Column H (Collected By): Who gathered it? (Jane Smith - IAM Admin)
Column I (Verification Status): Has auditor reviewed? (Pending/Verified/Rejected)
```

**Example Entries:**

| ID | Area | Service | Type | Description | Location | Date | By | Status |
|----|------|---------|------|-------------|----------|------|-------|--------|
| EV-GOV-001 | Access Review | Microsoft 365 | Access Review Report | Q1 2026 review, 245 accounts, 3 orphans remediated | /evidence/access_reviews/Q1_2026/M365_review.pdf | 2026-01-15 | J. Smith | Verified |
| EV-GOV-002 | Change Mgmt | AWS Prod | Change Ticket | CHG-10234: Security group update, approved, successful | /evidence/changes/Q1_2026/CHG-10234.pdf | 2026-01-10 | M. Jones | Pending |
| EV-GOV-003 | Incidents | Salesforce | Incident Ticket + Report | SEC-2026-042: Phishing, P2, lessons learned completed | /evidence/incidents/Q1_2026/SEC-2026-042.pdf | 2026-01-12 | A. Lee | Verified |

**Implementer Perspective:**
*"Populate evidence register AS YOU COLLECT evidence (don't wait until end). This prevents missing evidence and makes audit prep effortless."*

**Auditor Perspective:**
*"I'll spot-check 20% of evidence register entries by requesting the files. If paths are wrong or files missing, credibility drops for entire assessment."*

---

## Section 6: Common Pitfalls & How to Avoid Them

### 6.1 Top 10 Governance Assessment Mistakes

#### Pitfall 1: Waiting Until Week 4 to Start

**Problem:**
```
Coordinator schedules kickoff meeting for Week 1
Team says "we have 4 weeks, plenty of time"
Weeks 1-3: Nothing happens
Week 4: Panic, incomplete assessment, missing evidence, delayed approval
```

**Impact:**

- Rushed assessment (errors, missed items)
- No time for remediation
- Approval delays (CISO unavailable at deadline)

**Fix:**
```
Week 1: Kickoff + assign ownership + start data collection
Week 2-3: Complete assessments + collect evidence
Week 4: Internal QA + approval workflow
Contingency: 5-day buffer for unexpected issues
```

---

#### Pitfall 2: Copy-Paste from Last Quarter Without Re-Validation

**Problem:**
```
"AWS was compliant last quarter, I'll just copy the row"
Reality: Configuration drifted, new security group added (misconfigured), now non-compliant
Auditor checks current state: Finds gap, questions all "Compliant" statuses
```

**Impact:**

- False compliance claims
- Audit findings
- Loss of credibility

**Fix:**
```
☐ ALWAYS re-validate each quarter
☐ For Critical services: Check current state actively (don't assume)
☐ For High/Medium: Spot-check 50% minimum
☐ For Low: Spot-check 20% minimum
☐ Document validation method (e.g., "Verified via AWS Console on 2026-01-15")
```

---

#### Pitfall 3: Treating "No Incidents" as Automatic Compliance

**Problem:**
```
Assessor: "We didn't have any incidents this quarter"
Auditor: "How do you know?"
Assessor: "Nobody told me about any"
Auditor: "Did you check SIEM? Incident system? Vendor notifications?"
Assessor: "Uh..."
Auditor: *Marks as Non-Compliant due to unverified claim*
```

**Impact:**

- Failed audit check
- Undetected incidents (security gaps)

**Fix:**
```
For "No Incidents" claims, provide evidence:
☐ SIEM query results (date range, filter criteria, zero results)
☐ Incident system query (no open/closed security tickets for service)
☐ Vendor status page check (no security incidents reported)
☐ Screenshot with timestamp
```

---

#### Pitfall 4: Orphan Accounts Left in "Issues Found" Status

**Problem:**
```
Access review completed: 5 orphan accounts found
Assessor marks status: "⚠️ Partial" 
Evidence: Access review report showing orphans
Gap description: "5 orphans identified"

3 months later: Same 5 orphans still active (forgotten)

```

**Impact:**

- Security vulnerability (terminated employee access)
- Repeated quarterly findings
- Compliance failure

**Fix:**
```
☐ Orphan detection MUST trigger immediate remediation (same day)
☐ Policy requires: <24 hours to disable
☐ Don't close assessment until remediation complete
☐ Evidence MUST show both detection AND remediation:

   - Access review report (orphans found)
   - Remediation tickets (accounts disabled)
   - Verification screenshot (accounts now disabled in IAM system)

```

---

#### Pitfall 5: Emergency Changes Without Post-Implementation Review

**Problem:**
```
Emergency change executed (zero-day patch applied urgently)
CAB approval bypassed (acceptable per policy)
Change successful, service restored
Post-implementation review skipped (team busy)
Next quarter: Auditor asks for 48-hour post-review
Team: "We were busy, forgot"
Auditor: "Emergency process requires post-review within 48 hours - Non-Compliant"
```

**Impact:**

- Policy violation
- Missed lessons learned
- Audit finding

**Fix:**
```
☐ Set calendar reminder: Emergency change date + 48 hours
☐ Block 1 hour for post-review meeting
☐ Document even if outcome is "everything went well"
☐ Template questions:

   - Was emergency process necessary? (Could we have used normal CAB?)
   - What went well?
   - What went poorly?
   - How can we prevent similar emergencies?
   - Process improvements needed?

```

---

#### Pitfall 6: BC/DR Plan "Tested" = Plan Reviewed

**Problem:**
```
Assessor: "BC plan tested annually ✅"
Evidence: Meeting notes "Reviewed BC plan on 2026-01-10, looks good"
Auditor: "Was recovery actually performed?"
Assessor: "No, we just reviewed the document"
Auditor: "That's not a test, that's a review. Did you fail over to DR?"
Assessor: "No..."
Auditor: *Marks Non-Compliant*
```

**Impact:**

- BC plan may not work when actually needed
- Audit failure
- Unproven RTO/RPO

**Fix:**
```
BC/DR "Test" MUST include:
☐ Actual recovery procedure execution (even if partial)
☐ Simulated failure scenario
☐ Measured RTO/RPO
☐ Issues encountered and resolved
☐ Screenshots or system logs proving recovery occurred

Acceptable test levels:

- Full DR region failover (best)
- Partial failover (test environment)
- Backup restore to test environment (minimum)

NOT acceptable:

- Reading the plan document
- Discussion of "what we would do"

```

---

#### Pitfall 7: Vendor Certifications Expired (Not Monitored)

**Problem:**
```
Q1: Vendor ISO 27001 valid until 2026-03-15 (✅ Compliant)
Q2: Assessor copies Q1 data, doesn't check expiry
Reality: Cert expired 2026-03-15, vendor hasn't renewed
Q3: Auditor checks cert authority: "Expired, not renewed"
Assessor: "I didn't know!"
Auditor: "You're required to monitor quarterly"
```

**Impact:**

- Vendor using expired certification (marketing fraud)
- Compliance violation
- Vendor risk not managed

**Fix:**
```
☐ Track cert expiry dates in vendor tracking spreadsheet
☐ Set reminders: 90 days before expiry
☐ Quarterly validation process:
   1. Check vendor trust portal
   2. Download current cert (don't trust cached copy)
   3. Verify with cert authority if suspicious
   4. Note expiry date in assessment
☐ If cert expired: Escalate to vendor manager, demand renewal proof or switch vendors
```

---

#### Pitfall 8: Jurisdictional Risk "Accepted" Without Documentation

**Problem:**
```
DPO verbally says: "Salesforce US CLOUD Act risk is acceptable given mitigations"
Assessor marks: "Risk Acceptance: Accepted"

6 months later: Data breach investigation

Regulator: "Show us documented risk acceptance for US data transfer"
[Organization]: "It was verbal..."
Regulator: *GDPR Article 32 violation fine*
```

**Impact:**

- Regulatory violation
- No legal defense
- Potential fines

**Fix:**
```
Risk acceptance MUST be documented:
☐ Written memo or risk acceptance form
☐ Service name and jurisdictional risk summary
☐ Mitigations in place
☐ Residual risk statement
☐ Business justification
☐ DPO signature and date
☐ CISO signature and date
☐ Legal review (for cross-border transfers)
☐ Filed in evidence folder
```

---

#### Pitfall 9: Exit Plan for Critical Service = "We'd figure it out"

**Problem:**
```
Auditor: "Show me exit plan for GitHub Enterprise (Critical service)"
Assessor: "We have a plan"
Auditor: "Can I see it?"
Assessor: "Well, it's not written down, but we know we'd migrate to GitLab"
Auditor: "How long would migration take?"
Assessor: "Uh... a few weeks?"
Auditor: "Have you tested data export?"
Assessor: "No..."
Auditor: *Non-Compliant*
```

**Impact:**

- Vendor lock-in (no viable exit path)
- Cannot respond to vendor issues (price hikes, security incidents, acquisition)
- Policy violation

**Fix:**
```
Exit plan MUST be documented:
☐ Written plan with version/date
☐ Alternative providers identified and assessed
☐ Migration effort estimated (person-hours, calendar time, cost)
☐ Data extraction tested (at least PoC for Critical services)
☐ Reviewed annually
☐ Updated when service changes materially
```

---

#### Pitfall 10: Assessment Completed But Not Approved

**Problem:**
```
Week 1-3: Assessment completed, evidence collected
Week 4: Sent to IT Ops for review
Week 5: IT Ops approved, sent to Compliance
Week 6: Compliance approved, sent to CISO
Week 7: CISO on vacation, returns Week 8
Week 8: CISO has questions, sends back for clarification
Week 9: Clarifications provided
Week 10: CISO approves

Assessment marked "complete" in Week 3
Actually approved: Week 10 (7 weeks delay)
```

**Impact:**

- Assessment data stale (6+ weeks old at approval)
- Audit cycle broken (Q2 starts before Q1 approved)

**Fix:**
```
☐ Build approval time into schedule (4-week assessment + 2-week approval = 6 weeks total)
☐ Pre-brief approvers (Week 3: "Assessment coming next week, please reserve time")
☐ Approval escalation process: If approver unavailable, escalate to deputy
☐ Assessment not "complete" until final sign-off obtained
☐ Set hard deadline: "CISO sign-off required by [date] or assessment delayed to next quarter"
```

---

### 6.2 Red Flags That Signal Cargo Cult Compliance

**Watch for these warning signs:**
```
🚩 All services marked "✅ Compliant" (statistically improbable - some gaps always exist)
🚩 Same status quarter over quarter (no change = not actually re-validating)
🚩 Evidence all from same date (bulk collection, not ongoing monitoring)
🚩 Generic gap descriptions ("needs improvement" - not specific)
🚩 No remediation target dates (gaps exist but no plan to fix)
🚩 Evidence register empty or incomplete (assessment without proof)
🚩 Approvals all signed same day (no actual review time)
🚩 No incidents for 4 quarters (either very lucky or not monitoring)
🚩 BC/DR plans "tested" but no RTO/RPO measurements
🚩 Vendor certifications never verified (just copied from vendor website)
```

**Implementer Perspective:**
*"If your assessment looks 'too perfect,' auditors will dig deeper. Honest disclosure of gaps with remediation plans is more credible than claiming perfection."*

**Auditor Perspective:**
*"Assessments with some 'Partial' or 'Non-Compliant' findings are more trustworthy than all-green assessments. Reality has gaps—mature programs acknowledge and address them."*

---

## Section 7: Quality Checklist

### 7.1 Pre-Submission Quality Review

**Before submitting assessment for approval, verify:**

---

#### 7.1.1 Completeness Checks
```
ASSESSMENT STRUCTURE
☐ All 11 sheets present and named correctly
☐ Sheet 1 (Instructions) completed with org name, assessment date, coordinator
☐ Sheets 2-8 (Assessments) have at least 1 entry per service in inventory
☐ Sheet 9 (Dashboard) formulas calculate correctly (no #REF!, #DIV/0! errors)
☐ Sheet 10 (Evidence Register) has entry for every piece of evidence
☐ Sheet 11 (Approval) has placeholder for approver names (ready to sign)

DATA QUALITY
☐ All yellow cells (user input) completed (no blanks where data required)
☐ All dropdown cells use dropdown options (no manual text entry)
☐ All date cells in DD.MM.YYYY format (consistent)
☐ Status column (H) reflects evidence (✅ only if fully compliant)
☐ Evidence location column (I) has path for all non-N/A entries
☐ Gap description column (J) completed for all ⚠️ Partial and ❌ Non-Compliant entries
☐ Remediation date column (P) completed for all gaps requiring action

EVIDENCE COMPLETENESS
☐ Evidence register matches evidence folder (all files referenced exist)
☐ Evidence files follow naming conventions (service_type_date.pdf)
☐ Evidence is current (<90 days for quarterly items, <365 for annual)
☐ Screenshots include timestamps and service names
☐ Signed documents have actual signatures (not placeholder)
```

---

#### 7.1.2 Accuracy Checks
```
CROSS-WORKBOOK VALIDATION
☐ Service names match IMP-5.23.1 (Inventory) exactly (spelling, capitalization)
☐ Vendor names match IMP-5.23.2 (Vendor DD) exactly
☐ Service criticality matches IMP-5.23.1 (no discrepancies)
☐ Data classification matches IMP-5.23.1
☐ Services in governance assessment exist in inventory (no orphan services)
☐ New services added to inventory also added to governance assessment

FORMULA VALIDATION
☐ Dashboard compliance % calculates correctly (manual spot-check)
☐ Evidence count in register matches actual evidence files
☐ Totals in dashboard match sum of assessment sheets
☐ Conditional formatting applies correctly (green/yellow/red)

LOGICAL CONSISTENCY
☐ "No incidents" claims have SIEM query evidence (not just blank)
☐ "Compliant" access reviews have completion dates within quarter
☐ BC/DR "tested" entries have test reports (not just plan reviews)
☐ Vendor certifications marked "Valid" have expiry dates in future
☐ Exit plans marked "Yes" have actual plan documents (not placeholder)
```

---

#### 7.1.3 Policy Compliance Checks
```
ACCESS REVIEW (Sheet 2)
☐ All services have access review within 90 days
☐ Orphan accounts (if found) remediated within 24 hours (evidence exists)
☐ Manager attestations dated within review period

CHANGE MANAGEMENT (Sheet 3)
☐ Emergency changes have post-implementation review within 48 hours
☐ High/Critical changes have documented rollback plans
☐ CAB approval documented for non-emergency changes

INCIDENT MANAGEMENT (Sheet 4)
☐ P1 incidents responded to within 1 hour
☐ P2 incidents responded to within 4 hours
☐ All P1/P2 incidents have lessons learned documentation

BC/DR (Sheet 5)
☐ Critical services have BC/DR plan (<12 months old)
☐ Critical services have BC/DR test (annual minimum)
☐ RTO/RPO measured during tests (not estimated)

VENDOR RISK (Sheet 6)
☐ Critical vendors have quarterly meetings (last 90 days)
☐ Certifications verified (not just copied from vendor website)
☐ Vendor incidents documented (from vendor notifications)

EXIT STRATEGY (Sheet 7)
☐ Critical/High services have documented exit plans (<12 months old)
☐ Critical services have PoC migration testing (annual)

JURISDICTIONAL RISK (Sheet 8)
☐ EU data transfers have valid SCCs
☐ US-nexus vendors have TIA (<12 months old)
☐ Residual risks have CISO/DPO sign-off
```

---

#### 7.1.4 Evidence Quality Checks
```
TIER 1 EVIDENCE (System-Generated)
☐ SIEM logs have timestamps
☐ IAM exports have export date
☐ Change tickets have approval workflow
☐ Incident tickets have resolution timestamps

TIER 2 EVIDENCE (Documented with Sign-Offs)
☐ BC test reports have manager signatures
☐ Access reviews have manager attestations
☐ Risk acceptances have DPO/CISO signatures
☐ Meeting notes have attendee lists

TIER 3 EVIDENCE (Screenshots)
☐ Screenshots include timestamp/date
☐ Screenshots show service name
☐ Screenshots show relevant data (not cropped critical info)
☐ Screenshots are readable (not blurry or low-res)

EVIDENCE STORAGE
☐ All evidence in correct quarter folder
☐ Folder structure consistent (subfolders for each sheet)
☐ File permissions set correctly (read-only for evidence, write for admins)
☐ Backup of evidence folder exists (don't lose quarter's work)
```

---

### 7.2 Approval Readiness Checklist

**Before sending to IT Operations Manager:**
```
INTERNAL QA COMPLETE
☐ Assessment coordinator has reviewed entire workbook
☐ All stakeholder sections reviewed by section owners
☐ Quality checklist (Section 7.1) completed
☐ Known gaps documented with remediation plans
☐ Evidence register cross-checked against evidence folder

STAKEHOLDER COMMUNICATION
☐ Pre-brief email sent to approvers (summary of findings)
☐ Remediation plans attached (for any gaps)
☐ Evidence folder access granted to approvers
☐ Approval deadline communicated (2 weeks for review)

APPROVAL PACKAGE CONTENTS
☐ ISMS-IMP-A.5.23.S4_Governance_Q[X]_YYYY.xlsx (main workbook)
☐ Executive summary (1-page, key findings + metrics)
☐ Gap remediation plan (if applicable)
☐ Evidence folder path (or archive if emailing)
☐ Approval workflow instructions (who signs, when, sequence)
```

---

## Section 8: Review & Approval Process

### 8.1 Approval Workflow Overview

**Three-Stage Sequential Approval:**
```
┌─────────────────────────────────────────────────────────────────┐
│                     APPROVAL WORKFLOW                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  STAGE 1: IT OPERATIONS MANAGER REVIEW (3-5 business days)       │
│  ┌────────────────────────────────────────────────────────────┐  │
│  │ Focus: Technical accuracy, operational feasibility         │  │
│  │ Checks:                                                    │  │
│  │  ☐ Access reviews completed correctly                     │  │
│  │  ☐ Change management process followed                     │  │
│  │  ☐ BC/DR tests actually performed                         │  │
│  │  ☐ Remediation plans are realistic                        │  │
│  │                                                            │  │
│  │ Outcomes:                                                  │  │
│  │  ✅ Approved → Forward to Compliance                       │  │
│  │  ⚠️ Approved with Conditions → Document conditions        │  │
│  │  ❌ Rejected → Return for remediation                     │  │
│  └────────────────────────────────────────────────────────────┘  │
│                            ↓                                     │
│  STAGE 2: COMPLIANCE OFFICER REVIEW (3-5 business days)          │
│  ┌────────────────────────────────────────────────────────────┐  │
│  │ Focus: Regulatory alignment, audit readiness               │  │
│  │ Checks:                                                    │  │
│  │  ☐ Evidence sufficient for audit                          │  │
│  │  ☐ Policy requirements met                                │  │
│  │  ☐ Jurisdictional risks properly assessed                 │  │
│  │  ☐ Vendor risks documented                                │  │
│  │                                                            │  │
│  │ Outcomes:                                                  │  │
│  │  ✅ Approved → Forward to CISO                             │  │
│  │  ⚠️ Approved with Conditions → Document conditions        │  │
│  │  ❌ Rejected → Return for remediation                     │  │
│  └────────────────────────────────────────────────────────────┘  │
│                            ↓                                     │
│  STAGE 3: CISO APPROVAL (3-5 business days)                      │
│  ┌────────────────────────────────────────────────────────────┐  │
│  │ Focus: Risk acceptance, strategic alignment                │  │
│  │ Checks:                                                    │  │
│  │  ☐ Overall governance health acceptable                   │  │
│  │  ☐ High-risk vendor issues addressed                      │  │
│  │  ☐ Jurisdictional risks properly accepted                 │  │
│  │  ☐ Resource allocation for remediation                    │  │
│  │                                                            │  │
│  │ Outcomes:                                                  │  │
│  │  ✅ Final Approval → Assessment complete                   │  │
│  │  ⚠️ Approved with Conditions → Document exec conditions   │  │
│  │  ❌ Rejected → Return for significant remediation         │  │
│  └────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

**Total Timeline:** 9-15 business days (best case 9, realistic 12-15)

---

### 8.2 Stage 1: IT Operations Manager Review

**Review Focus:** Operational feasibility and technical accuracy

**Detailed Checklist (IT Operations Manager):**
```
TECHNICAL ACCURACY (8 items)
☐ Access review completion dates match IAM system exports
☐ Change tickets referenced actually exist in ITSM
☐ Incident response times match ticket timestamps
☐ BC/DR test RTOs/RPOs match test reports
☐ Vendor certifications verified against cert authorities
☐ Exit plan technical assessments are accurate
☐ Service names/configurations match actual deployments
☐ Technical gaps are correctly identified (not false positives)

OPERATIONAL FEASIBILITY (7 items)
☐ Remediation timelines are realistic (not overly optimistic)
☐ Resource requirements identified for gap remediation
☐ Access review procedures can be sustained quarterly
☐ Change management process is actually being followed
☐ BC/DR test frequency is achievable (annual for all Critical)
☐ Vendor monitoring can be maintained with current staffing
☐ Exit strategies are technically viable (PoC results support claims)

EVIDENCE QUALITY (5 items)
☐ Evidence is from actual systems (not placeholder documents)
☐ Screenshots show timestamps and context
☐ Test reports show actual execution (not just plans)
☐ Access reviews have manager sign-offs (not just IT attestation)
☐ Evidence is current (within acceptable age limits)

INTEGRATION VERIFICATION (3 items)
☐ Assessment data matches upstream sources (IMP-5.23.1, 5.23.2, 5.23.3)
☐ No orphan services (services in assessment exist in inventory)
☐ Dashboard metrics match assessment sheet totals
```

**Approval Outcomes:**

**✅ Approved:**
```
All checks passed, no concerns.

IT Ops Manager signs and forwards to Compliance Officer.
```

**⚠️ Approved with Conditions:**
```
Example conditions:

- "Approved provided that orphan account remediation completed by [date]"
- "Approved contingent on BC/DR test for AWS RDS scheduled by [date]"
- "Approved with condition: Emergency change post-review completed within 5 days"

Conditions documented in Column J (Gap Description) and tracked separately.
```

**❌ Rejected:**
```
Example rejection reasons:

- "Access review evidence is placeholder document (not actual IAM export)"
- "BC/DR test claimed but no test report provided"
- "Change tickets referenced don't exist in ServiceNow"
- "Remediation timelines unrealistic (300-hour project scheduled for 2 days)"

Return to Assessment Coordinator with specific items to fix.
Do not proceed to Compliance review until issues resolved.
```

---

### 8.3 Stage 2: Compliance Officer Review

**Review Focus:** Regulatory alignment and audit readiness

**Detailed Checklist (Compliance Officer):**
```
POLICY COMPLIANCE (10 items)
☐ All policy requirements met (access reviews quarterly, BC tests annual, etc.)
☐ No policy violations documented (orphan accounts >24hrs, etc.)
☐ Exceptions properly documented (Exception ID linked to register)
☐ Risk acceptances have proper sign-offs (CISO/DPO)
☐ SLA compliance tracked for vendor performance
☐ Regulatory requirements addressed (DORA, NIS2, GDPR)
☐ Data protection requirements met (DPAs, SCCs, TIAs)
☐ Vendor monitoring procedures followed
☐ Exit planning requirements met for Critical/High services
☐ Evidence retention adequate for audit (7-year minimum)

AUDIT READINESS (8 items)
☐ Evidence is objective and verifiable (auditor can independently verify)
☐ Evidence register is complete (all claims have supporting evidence)
☐ Timestamps on evidence are credible (not backdated)
☐ Sign-offs are genuine (actual signatories, not proxies)
☐ Gaps are honestly disclosed (not hidden or minimized)
☐ Remediation plans exist for all gaps
☐ Assessment tells a coherent story (no contradictions)
☐ Previous audit findings addressed (if applicable)

REGULATORY COMPLIANCE (9 items)
☐ GDPR Article 32 compliance (security of processing)
☐ DORA Article 28 compliance (ICT risk management for financial entities)
☐ NIS2 Article 21 compliance (cybersecurity measures for essential entities)
☐ CLOUD Act risks assessed and documented
☐ Data residency requirements met (or documented deviations)
☐ Transfer mechanisms valid (SCCs current template)
☐ TIAs completed and signed (annual review)
☐ DPO review documented for jurisdictional risks
☐ Vendor concentration risk assessed (if multiple services from one vendor)

RISK MANAGEMENT (6 items)
☐ High-risk vendor issues escalated appropriately
☐ Residual risks clearly stated (not just implied)
☐ Risk acceptance documented (not verbal)
☐ Compensating controls justified (actually compensate for risk)
☐ Risk ratings consistent with evidence
☐ Risk treatment aligned with organization risk appetite
```

**Approval Outcomes:**

**✅ Approved:**
```
Regulatory and audit requirements met.

Compliance Officer signs and forwards to CISO.
```

**⚠️ Approved with Conditions:**
```
Example conditions:

- "Approved provided DPO signs jurisdictional risk acceptance by [date]"
- "Approved contingent on TIA renewal for Salesforce completed by [date]"
- "Approved with condition: DORA exit plan testing completed within 90 days"

Conditions tracked in separate tracking sheet (not just in comments).
```

**❌ Rejected:**
```
Example rejection reasons:

- "TIA for US vendor is expired (GDPR compliance risk)"
- "DORA exit testing requirement not met for Critical financial services"
- "Risk acceptance for jurisdictional risk lacks DPO signature"
- "Evidence insufficient for audit (screenshots without timestamps)"

Return to Assessment Coordinator with compliance gaps to address.
```

---

### 8.4 Stage 3: CISO Approval

**Review Focus:** Executive risk acceptance and strategic alignment

**Detailed Checklist (CISO):**
```
STRATEGIC ALIGNMENT (7 items)
☐ Cloud governance supports business objectives
☐ Vendor strategy aligns with IT strategy
☐ Exit plans support vendor diversity goals
☐ Resource allocation reasonable for identified gaps
☐ Remediation priorities aligned with business criticality
☐ Regulatory compliance posture acceptable
☐ No surprises (major issues were escalated earlier)

RISK POSTURE (8 items)
☐ Overall compliance rate acceptable (target: ≥85%)
☐ Critical service gaps identified and prioritized
☐ High-risk vendor issues have mitigation plans
☐ Jurisdictional risks properly accepted (DPO concurrence)
☐ BC/DR coverage adequate for business continuity
☐ Incident response effectiveness demonstrated
☐ Access control hygiene maintained (orphan accounts managed)
☐ Vendor concentration risk understood and accepted

RESOURCE & BUDGET (5 items)
☐ Remediation budget requirements identified
☐ Staffing adequate for ongoing governance (quarterly cycle sustainable)
☐ Tool/system gaps identified (if automation needed)
☐ Training needs documented (if skills gap exists)
☐ Third-party support requirements clear (if needed)

ACCOUNTABILITY (3 items)
☐ Ownership assigned for all gap remediation
☐ Escalation paths clear for issues requiring executive decision
☐ Quarterly governance cycle sustainable with current team
```

**Approval Outcomes:**

**✅ Final Approval:**
```
Assessment complete. CISO signature authorizes:

- Current risk posture acceptance
- Remediation budget allocation
- Continuation of quarterly governance cycle

File assessment as official quarterly record.
Export metrics to IMP-5.23.5 (Dashboard).
```

**⚠️ Approved with Executive Conditions:**
```
Example conditions:

- "Approved with condition: High-risk vendor [X] to be replaced by Q3"
- "Approved contingent on hiring additional IAM admin for sustainable access reviews"
- "Approved with requirement: DORA exit testing to be budgeted in Q2"

Executive conditions trigger separate project planning (not just task tracking).
```

**❌ Rejected (Rare):**
```
CISO rejection indicates significant concerns, typically:

- Risk posture unacceptable (too many critical gaps)
- Remediation plans lack credibility
- Major regulatory compliance issue not addressed
- Resource requirements exceed available budget significantly

Requires executive discussion before resubmission.
```

---

### 8.5 Handling Rejections & Resubmissions

**If Assessment Rejected at Any Stage:**

**Step 1: Acknowledge & Understand (Within 24 hours)**
```
☐ Acknowledge receipt of rejection
☐ Schedule meeting with rejecting approver
☐ Understand specific issues (not just "insufficient evidence" - which evidence?)
☐ Document rejection reasons in detail
```

**Step 2: Root Cause Analysis (2-3 days)**
```
☐ Why did issues occur? (inadequate preparation, wrong interpretation, missing process)
☐ Were similar issues in previous quarter? (pattern or one-off)
☐ Systemic problem or isolated error?
```

**Step 3: Remediation Planning (2-3 days)**
```
☐ Address each rejection reason specifically
☐ Collect missing evidence
☐ Correct errors
☐ Update procedures to prevent recurrence
```

**Step 4: Execute Remediation (5-10 days, depends on issues)**
```
☐ Gather missing evidence
☐ Conduct additional testing if needed
☐ Obtain missing sign-offs
☐ Update assessment with corrections
```

**Step 5: Internal Pre-Review (2 days)**
```
☐ Have uninvolved party review remediation
☐ Verify all rejection reasons addressed
☐ Quality check (Section 7) before resubmitting
```

**Step 6: Formal Resubmission (1 day)**
```
☐ Cover letter explaining what was fixed
☐ Highlight changes (track changes or summary of updates)
☐ Request expedited review if timeline critical
```

**Step 7: Learn & Improve (After approval)**

☐ Document lessons learned
☐ Update procedures/templates
☐ Train team on gaps
☐ Prevent recurrence next quarter

---

## Section 9: Integration & Maintenance

### 9.1 Integration with Other ISMS Assessments

**Critical Context:** This assessment (ISMS-IMP-A.5.23.S4) is ONE component of the comprehensive A.5.19-23 supplier/cloud security framework. It does not operate in isolation.

**The Five-Workbook Ecosystem:**

```
┌────────────────────────────────────────────────────────────────────┐
│  ISMS Control A.5.19-23: Information Security for Cloud Services   │
└────────────────────────────────────────────────────────────────────┘
                              │
              ┌───────────────┼───────────────┐
              │               │               │
         ┌────▼────┐     ┌────▼────┐    ┌────▼────┐
         │ 5.23.1  │────▶│ 5.23.2  │───▶│ 5.23.3  │
         │Inventory│     │Vendor DD│    │ Config  │
         └────┬────┘     └────┬────┘    └────┬────┘
              │               │               │
              └───────────────┼───────────────┘
                              │
              ┌───────────────┼───────────────┐
              │               │               │
         ┌────▼────┐     ┌────▼────┐
         │ 5.23.4  │◀────│ 5.23.5  │
         │Governanc│     │Complianc│
         │  (YOU)  │     │   e     │
         └─────────┘     └─────────┘
```

**Integration Requirements:**

| Workbook | Relationship to 5.23.4 | Integration Point |
|----------|------------------------|-------------------|
| **5.23.1 (Inventory)** | AUTHORITATIVE SOURCE | Cloud service list; any service in 5.23.4 MUST exist in 5.23.1 |
| **5.23.2 (Vendor DD)** | UPSTREAM DEPENDENCY | Vendor security certs/contracts inform governance frequency |
| **5.23.3 (Config)** | UPSTREAM DEPENDENCY | Secure configurations are monitored for drift in governance |
| **5.23.5 (Compliance)** | DOWNSTREAM CONSUMER | Compliance monitoring uses 5.23.4 governance metrics as evidence |

**Implementer Perspective:**
*"Governance is the 'continuous operation' phase after initial deployment. You can't govern services you haven't inventoried (5.23.1), vetted (5.23.2), or configured securely (5.23.3). Do those first."*

**Auditor Perspective:**
*"I'll check that every service in 5.23.4 governance tracking exists in 5.23.1 inventory, and that access reviews (Sheet 2) reference the access controls documented in 5.23.3. Missing linkages indicate incomplete governance."*

---

### 9.2 Integration with Organizational Systems

**Cloud governance assessment should NOT be a standalone spreadsheet.** To avoid creating "shadow IT governance," integrate with existing organizational systems:

**Priority 1: Configuration Management Database (CMDB)**

**What to Integrate:**

- Column B (Cloud_Service_Name) → CMDB CI (Configuration Item)
- Column C (Vendor_Name) → CMDB Supplier entity
- Column F (Service_Criticality) → CMDB Business Impact rating
- Sheet 2 (Access Review) → CMDB Service Owner field
- Sheet 6 (Vendor Risk) → CMDB Vendor Risk Score

**Integration Method:**

- **Manual:** Weekly export from this workbook → import to CMDB (error-prone)
- **Automated (Preferred):** Python script reads Excel, updates CMDB via API
- **Bidirectional:** CMDB is source of truth, this workbook for governance details

**Example API Integration (Python):**

```python
import openpyxl
import requests

# Load governance workbook
wb = openpyxl.load_workbook("ISMS-IMP-A.5.23.S4.xlsx", data_only=True)
ws_access_review = wb["2. Access Review"]

# Extract access review dates for CMDB update
for row in range(7, 31):  # Data rows 7-30
    service_name = ws_access_review.cell(row=row, column=2).value
    last_review_date = ws_access_review.cell(row=row, column=18).value  # Column R
    
    if service_name and last_review_date:
        # Update CMDB via API
        cmdb_api_url = "https://cmdb.example.com/api/v1/ci/update"
        payload = {
            "ci_name": service_name,
            "last_access_review": last_review_date.strftime("%Y-%m-%d"),
            "compliance_status": "Governance Reviewed"
        }
        response = requests.post(cmdb_api_url, json=payload, headers={"Authorization": "Bearer TOKEN"})
        print(f"✅ Updated CMDB for {service_name}: {response.status_code}")
```

---

**Priority 2: IT Service Management (ITSM) / Ticketing System**

**What to Integrate:**

- Sheet 3 (Change Management) → ITSM Change Records
- Sheet 4 (Incident Management) → ITSM Incident Records
- Column M (Exception_ID) → ITSM Exception/Risk Ticket

**Integration Method:**

- **Automated ticket creation:** Python script reads non-compliant items → creates ITSM tickets
- **Bidirectional sync:** ITSM ticket status updates Excel "Status" column
- **Governance triggers:** ITSM change/incident events trigger governance assessment updates

**Example ITSM Integration (ServiceNow):**

```python
# Create ITSM ticket for overdue access review
import openpyxl
from servicenow import ServiceNowClient

wb = openpyxl.load_workbook("ISMS-IMP-A.5.23.S4.xlsx", data_only=True)
ws_access = wb["2. Access Review"]

sn_client = ServiceNowClient(instance="yourinstance.service-now.com", username="api_user", password="api_pass")

for row in range(7, 31):
    service = ws_access.cell(row=row, column=2).value
    status = ws_access.cell(row=row, column=9).value  # Column I
    last_review = ws_access.cell(row=row, column=18).value  # Column R
    
    # If access review overdue (>90 days), create ITSM ticket
    if status == "❌ Non-Compliant" and last_review:
        days_overdue = (datetime.now() - last_review).days - 90
        if days_overdue > 0:
            ticket = sn_client.create_incident({
                "short_description": f"OVERDUE: Access review for {service} ({days_overdue} days past due)",
                "assignment_group": "Cloud Operations",
                "priority": "2 - High",
                "category": "Compliance",
                "subcategory": "Access Review"
            })
            print(f"🎫 Created ITSM ticket {ticket['number']} for {service}")
```

---

**Priority 3: Risk Management System**

**What to Integrate:**

- Sheet 6 (Vendor Risk) → Risk Register entries
- Column N (Risk_ID) → Risk Management System risk ID
- Column O (Compensating_Controls) → Risk mitigation controls

**Integration Method:**

- Export vendor risk ratings → import to enterprise risk register
- Link governance gaps to operational risks
- Trigger risk reassessment when vendor risk rating changes

---

**Priority 4: Vendor Management Portal**

**What to Integrate:**

- Sheet 6 (Vendor Risk) → Vendor Management System vendor profiles
- Sheet 3 (Change Management) → Vendor Change Notifications
- Column W (Last_Assessment_Date) → Vendor reassessment schedule

**Integration Method:**

- Automated vendor risk score sync
- Vendor certification expiry alerts from vendor portal → update Sheet 6 Column U
- Vendor security incident feeds → auto-populate Sheet 4 Column R

---

### 9.3 Quarterly Maintenance Procedures

**Cloud governance is NOT "set and forget."** Quarterly reviews keep governance current as services evolve.

**Quarterly Maintenance Checklist (Every 3 Months):**

```
QUARTERLY GOVERNANCE MAINTENANCE - ISMS-IMP-5.23.4
Review Quarter: Q[X] [YYYY]
Review Date: [DD.MM.YYYY]
Coordinator: [Name]

☐ STEP 1: Reconcile with Inventory (5.23.1)
  ☐ Compare 5.23.4 service list against current 5.23.1
  ☐ Add rows for NEW services deployed this quarter
  ☐ Mark DECOMMISSIONED services (archive, don't delete)
  ☐ Update service criticality if changed in 5.23.1
  ☐ Verify vendor names match 5.23.2

☐ STEP 2: Execute Quarterly Governance Activities
  ☐ Sheet 2 (Access Review): Conduct quarterly access reviews
    ├─ Review user accounts for all services
    ├─ Recertify admin/privileged access
    ├─ Disable inactive accounts
    └─ Document review date in Column R
  ☐ Sheet 3 (Change Management): Review changes this quarter
    ├─ Verify all changes properly authorized
    ├─ Check emergency change documentation
    └─ Update change risk assessment if needed
  ☐ Sheet 4 (Incident Management): Review incidents this quarter
    ├─ Update incident counts (Column R)
    ├─ Check MTTR metrics (Column S)
    ├─ Verify lessons learned captured (Column X)
    └─ Update playbooks based on new incident types
  ☐ Sheet 5 (Business Continuity): Test BC/DR plans
    ├─ Test failover for Tier 1 services (quarterly)
    ├─ Verify RTO/RPO achievement (Columns T-W)
    ├─ Document test results (Column S)
    └─ Schedule next test (Column X)
  ☐ Sheet 6 (Vendor Risk): Reassess vendor risk
    ├─ Check vendor security incidents (Column S)
    ├─ Update certification expiry tracking (Column T-U)
    ├─ Assess financial health if critical vendor (Column V)
    ├─ Update risk rating if changes detected (Column G)
    └─ Document reassessment date (Column W)

☐ STEP 3: Refresh Evidence
  ☐ Review "Evidence_Location" (Column J) on all sheets
  ☐ Re-capture screenshots for configs older than 90 days
  ☐ Update access review reports
  ☐ Collect incident management reports
  ☐ Archive BC/DR test results
  ☐ Collect vendor security bulletins

☐ STEP 4: Validate Current State
  ☐ Spot-check 20% of "Compliant" items (avoid false positives)
  ☐ Re-assess any "Partial" items (have they been remediated?)
  ☐ Check remediation progress on "Non-Compliant" items
  ☐ Verify compensating controls still in place

☐ STEP 5: Update Dashboard (Sheet 9 - was Sheet 8 in v1.0)
  ☐ Verify all formulas calculating correctly
  ☐ Review compliance percentage trends (improving or degrading?)
  ☐ Check key metrics (overdue reviews, open incidents, etc.)
  ☐ Update executive summary if needed

☐ STEP 6: Review Exceptions and Risk Acceptance
  ☐ Check exception expiration dates (Column M)
  ☐ Verify risk acceptance still valid (Column N risk ID active?)
  ☐ Renew exceptions if needed (requires CISO approval)
  ☐ Close expired exceptions or remediate gaps

☐ STEP 7: Check Integration Points
  ☐ Verify CMDB sync working (if automated)
  ☐ Check ITSM ticket status for governance gaps
  ☐ Reconcile vendor risk scores with vendor management system
  ☐ Update risk register with current vendor risks

☐ STEP 8: Prepare for Approval
  ☐ Run quality checklist (Section 7)
  ☐ Self-assessment score ≥80/100
  ☐ Evidence register complete (Sheet 10 - was Sheet 9)
  ☐ Submit for IT Ops → Compliance → CISO approval (Sheet 11)

SIGN-OFF:
Completed By: _________________
Date: _________________
Quarterly Review Status: ☐ Complete  ☐ In Progress  ☐ Overdue
```

---

### 9.4 Annual Comprehensive Review

**In addition to quarterly maintenance, conduct a thorough annual review.**

**Annual Review Checklist (Once Per Year):**

```
ANNUAL GOVERNANCE REVIEW - ISMS-IMP-5.23.4
Review Year: [YYYY]
Review Start: [DD.MM.YYYY]
Review Complete: [DD.MM.YYYY]
Coordinator: [Name]

☐ PHASE 1: Strategic Assessment (Weeks 1-2)
  ☐ Review governance framework effectiveness
  ☐ Analyze governance metrics trends (year-over-year)
  ☐ Assess staffing adequacy for governance activities
  ☐ Review governance tool effectiveness (Excel, automation scripts)
  ☐ Benchmark against industry standards (ISO 27001, CIS Controls)
  ☐ Identify governance maturity gaps

☐ PHASE 2: Vendor Landscape Review (Weeks 3-4)
  ☐ Conduct comprehensive vendor due diligence refresh (5.23.2)
  ☐ Reassess all vendor risk ratings (not just high-risk)
  ☐ Review vendor concentration risk (too many services with one vendor?)
  ☐ Evaluate vendor M&A activity (acquisitions, divestitures)
  ☐ Check for vendor end-of-life announcements
  ☐ Assess geopolitical risks affecting vendors

☐ PHASE 3: Configuration Drift Analysis (Weeks 5-6)
  ☐ Full configuration baseline refresh (5.23.3)
  ☐ Compare current configs against last year's baseline
  ☐ Identify systematic drift patterns (not just individual services)
  ☐ Assess whether config standards need updating
  ☐ Review security best practice evolution (CIS benchmarks updated?)

☐ PHASE 4: Incident & Change Trend Analysis (Week 7)
  ☐ Aggregate incident data for the year (Sheet 4)
  ☐ Identify top 5 incident root causes
  ☐ Assess MTTR trends (improving or degrading?)
  ☐ Review change management effectiveness (Sheet 3)
  ☐ Analyze emergency change frequency (should be decreasing)

☐ PHASE 5: Business Continuity Validation (Week 8)
  ☐ Full BC/DR test for ALL Tier 1 services (Sheet 5)
  ☐ Validate RTO/RPO assumptions still valid
  ☐ Test multi-vendor failover scenarios
  ☐ Review BC plan with business stakeholders
  ☐ Update BC documentation based on test results

☐ PHASE 6: Access Control Hygiene (Week 9)
  ☐ Deep-dive access review for ALL services (Sheet 2)
  ☐ Identify orphaned accounts (users no longer with org)
  ☐ Review admin access grants (are all still justified?)
  ☐ Assess privilege creep (users with more access than needed)
  ☐ Recertify service accounts

☐ PHASE 7: Compliance Gap Analysis (Week 10)
  ☐ Review changes in regulatory landscape (DORA, NIS2, etc.)
  ☐ Assess new compliance requirements applicability
  ☐ Gap analysis against new standards
  ☐ Update governance framework if needed
  ☐ Document compliance roadmap for next year

☐ PHASE 8: Continuous Improvement (Week 11)
  ☐ Collect feedback from stakeholders (IT Ops, Security, Compliance, CISO)
  ☐ Identify process bottlenecks
  ☐ Propose automation opportunities
  ☐ Update governance procedures/templates
  ☐ Define governance improvement initiatives for next year

☐ PHASE 9: Executive Reporting (Week 12)
  ☐ Prepare annual governance report for CISO/CIO
  ☐ Include: Compliance trends, key metrics, major incidents, vendor risks
  ☐ Highlight governance improvements achieved this year
  ☐ Propose governance priorities for next year
  ☐ Obtain executive approval for annual report

ANNUAL REVIEW SIGN-OFF:
Completed By: _________________
CISO Approval: _________________
Date: _________________
```

---

### 9.5 Continuous Improvement Methodology

**Governance should improve over time, not stagnate.**

**Quarterly Improvement Cycle:**

```
Q1: ASSESS
  ├─ What governance activities are time-consuming?
  ├─ Which activities provide low value?
  ├─ Where are we finding recurring gaps?
  └─ What feedback have we received?

Q2: PLAN
  ├─ Prioritize improvement initiatives
  ├─ Develop automation/process improvements
  ├─ Allocate resources (time, budget, tools)
  └─ Set measurable improvement goals

Q3: IMPLEMENT
  ├─ Roll out improvements
  ├─ Train stakeholders on new processes
  ├─ Monitor adoption and effectiveness
  └─ Adjust based on early feedback

Q4: MEASURE
  ├─ Did improvements achieve intended outcomes?
  ├─ Quantify time/effort savings
  ├─ Assess stakeholder satisfaction
  └─ Document lessons learned for next cycle
```

**Example Improvement Initiative:**

```
IMPROVEMENT INITIATIVE: Automate Access Review Reminders

Current State (Manual):

- Coordinator manually emails service owners quarterly
- 40% of reminders ignored, requiring follow-up
- Average 2 weeks to complete all access reviews
- High coordinator overhead

Proposed State (Automated):

- Python script reads Sheet 2, checks last review dates
- Auto-generates reminder emails to service owners
- Tracks responses and sends escalation emails if overdue
- Updates Excel when reviews submitted
- Dashboard shows real-time completion status

ROI Analysis:

- Development time: 8 hours (one-time)
- Time saved per quarter: 6 hours (coordinator time)
- Improved completion rate: 40% → 80%
- Payback period: < 2 quarters

Approval Status: ✅ APPROVED (CISO 01.02.2026)
Implementation: Q2 2026
```

---

### 9.6 Change Management: When Vendors/Services Evolve

**Cloud services don't stay static. The governance framework must adapt.**

**Common Change Scenarios:**

#### Scenario 1: Vendor Merger/Acquisition

*Example: Vendor A (your cloud provider) acquired by Vendor B*

**Governance Impact Assessment:**
1. **Immediate:** Flag all services using Vendor A in Sheet 6 (Vendor Risk)
2. **Week 1:** Reassess vendor risk rating (may increase if Vendor B less secure)
3. **Week 2:** Review contracts (do they transfer? need renegotiation?)
4. **Week 3:** Update CMDB, risk register, contracts database
5. **Month 1:** Conduct due diligence on Vendor B (treat as new vendor)
6. **Month 2:** Assess whether to migrate away (if risk too high)
7. **Ongoing:** Monitor integration progress, watch for service degradation

---

#### Scenario 2: Vendor Security Incident

*Example: Major breach at cloud provider*

**Governance Response:**
1. **Hour 0:** Activate incident response (Sheet 4)
2. **Hour 1:** Document incident in Column R (Incident Count)
3. **Hour 4:** Assess customer data impact (was YOUR data compromised?)
4. **Day 1:** Notify internal stakeholders (Security, CISO, Legal, DPO)
5. **Day 2:** Update vendor risk rating (Sheet 6 Column G → "Critical")
6. **Week 1:** Reassess compensating controls (Column O)
7. **Week 2:** Request vendor post-incident report (PIR)
8. **Month 1:** Update playbooks (Column U) based on lessons learned
9. **Quarter 1:** Conduct "should we stay with this vendor?" assessment

---

#### Scenario 3: Service End-of-Life Announcement

*Example: Vendor sunsetting a legacy service you use*

**Governance Migration Plan:**
1. **Announcement Day:** Flag service in Sheet 6 (Vendor Risk) with note
2. **Week 1:** Assess migration options (vendor's replacement? alternative vendor?)
3. **Week 2:** Update business continuity plan (Sheet 5) - accelerated migration timeline
4. **Week 3:** Conduct due diligence on replacement service (5.23.2)
5. **Month 1:** Plan migration (data transfer, config baseline, testing)
6. **Month 2:** Execute migration with fallback plan
7. **Month 3:** Decommission old service, update governance tracking

---

### 9.7 Workbook Versioning & Archive Strategy

**As governance assessments evolve, maintain historical record for audit trail.**

**Versioning Strategy:**

```
WORKBOOK NAMING CONVENTION:
ISMS-IMP-A.5.23.S4_Governance_[YYYY-MM-DD].xlsx

Examples:

- ISMS-IMP-A.5.23.S4_Governance_2026-01-20.xlsx (Q1 2026 assessment)
- ISMS-IMP-A.5.23.S4_Governance_2026-04-20.xlsx (Q2 2026 assessment)
- ISMS-IMP-A.5.23.S4_Governance_2026-07-20.xlsx (Q3 2026 assessment)
- ISMS-IMP-A.5.23.S4_Governance_2026-10-20.xlsx (Q4 2026 assessment)

```

**Archive Location:**

```
\\fileserver\ISMS\Assessments\5.23.4-Governance\Archive\
  ├─ 2025\
  │  ├─ ISMS-IMP-A.5.23.S4_Governance_2025-04-15.xlsx
  │  ├─ ISMS-IMP-A.5.23.S4_Governance_2025-07-15.xlsx
  │  ├─ ISMS-IMP-A.5.23.S4_Governance_2025-10-15.xlsx
  │  └─ ISMS-IMP-A.5.23.S4_Governance_2026-01-15.xlsx
  ├─ 2026\
  │  ├─ ISMS-IMP-A.5.23.S4_Governance_2026-04-20.xlsx (Q1)
  │  └─ ISMS-IMP-A.5.23.S4_Governance_2026-07-20.xlsx (Q2) [CURRENT]
  └─ README.md (archive policy documentation)
```

**Retention Policy:**

- **Current + 2 years:** Full workbooks retained
- **3-5 years:** Archive (compress to ZIP, store evidence separately)
- **>5 years:** Dispose per retention schedule (retain only approved/signed PDFs)

---

**END OF SECTION 9: INTEGRATION & MAINTENANCE**

*Next: Section 10 - Appendices & Glossary (FINAL)*

---

## Section 10: Appendices & Glossary

### 10.1 Glossary of Terms

**Comprehensive terminology reference for ongoing governance and risk management.**

| Term | Definition | Context in This Assessment |
|------|------------|---------------------------|
| **Access Recertification** | Periodic review and validation of user access rights to confirm continued business need | Sheet 2 (Access Review) quarterly activity - admin access must be recertified by business owner |
| **BC/DR (Business Continuity / Disaster Recovery)** | Plans and procedures to maintain or restore critical business functions after disruption | Sheet 5 tracks BC/DR plans, test results, RTO/RPO achievement for all cloud services |
| **Change Advisory Board (CAB)** | Group responsible for reviewing and approving proposed changes to IT services | Sheet 3 (Change Management) tracks CAB approvals for cloud service changes |
| **Compensating Control** | Alternative security measure when primary control cannot be implemented | Column O: Document alternative controls (e.g., enhanced monitoring if MFA not feasible) |
| **DORA (Digital Operational Resilience Act)** | EU regulation requiring financial entities to ensure ICT operational resilience | Applies to EU financial institutions - requires quarterly ICT risk monitoring (Sheet 6 Column Y) |
| **Failover** | Automatic switching to redundant system/service when primary fails | Sheet 5 (Business Continuity) tracks failover test results for critical services |
| **Governance** | Framework of policies, processes, and controls to manage and monitor cloud services | This entire assessment (ISMS-IMP-5.23.4) constitutes ongoing governance activities |
| **Incident** | Unplanned interruption or degradation of IT service quality | Sheet 4 tracks security/availability incidents, MTTR, root cause, lessons learned |
| **Lock-In Risk** | Risk that vendor-specific dependencies make migration difficult or costly | Sheet 6 assesses vendor concentration risk and lock-in factors |
| **Lock-Out Risk** | Risk that vendor business failure or relationship termination prevents access to data/services | Sheet 6 evaluates vendor financial health, exit strategies for continuity |
| **MTTR (Mean Time To Repair)** | Average time to restore service after incident | Sheet 4 Column S - target is service-specific based on criticality |
| **NIS2 (Network and Information Security Directive 2)** | EU directive requiring essential/important entities to implement cybersecurity measures | Mandates significant incident notification within 24 hours (Sheet 4 Column Z tracks) |
| **Privilege Creep** | Gradual accumulation of excess access rights as user roles change over time | Sheet 2 (Access Review) identifies and remediates via quarterly recertification |
| **RTO (Recovery Time Objective)** | Maximum acceptable downtime for service after disruption | Sheet 5 Column T - defined per service criticality (e.g., Tier 1 = <4 hours) |
| **RPO (Recovery Point Objective)** | Maximum acceptable data loss measured in time | Sheet 5 Column V - data loss tolerance (e.g., financial data = 0 minutes) |
| **Service Owner** | Individual accountable for service's business outcomes and responsible for access decisions | Sheet 2 - Service Owner approves quarterly access reviews for their service |
| **SLA (Service Level Agreement)** | Vendor commitment to specific service performance metrics (availability, response time, etc.) | Sheet 6 tracks vendor SLA compliance; breaches may increase risk rating |
| **Vendor Concentration Risk** | Risk from over-dependency on single vendor (if vendor fails, multiple services affected) | Sheet 6 assesses whether too many critical services use same vendor |

---

### 10.2 Acronyms & Abbreviations

| Acronym | Full Form | Usage Context |
|---------|-----------|---------------|
| **CAB** | Change Advisory Board | Sheet 3 - Reviews/approves changes |
| **CI** | Configuration Item | CMDB integration reference |
| **CMDB** | Configuration Management Database | Integration target for service inventory |
| **DPO** | Data Protection Officer | Approval stage for data protection compliance |
| **ITSM** | IT Service Management | Ticketing system integration |
| **JIT** | Just-In-Time (Access) | Temporary elevated access (Sheet 2 Column U) |
| **KPI** | Key Performance Indicator | Dashboard metrics (Sheet 9) |
| **MAU** | Monthly Active Users | Access review scope metric (Sheet 2) |
| **MTTR** | Mean Time To Repair | Incident resolution metric (Sheet 4 Column S) |
| **PAM** | Privileged Access Management | Admin access control (Sheet 2) |
| **PIR** | Post-Incident Review | Sheet 4 - Lessons learned after incidents |
| **QBR** | Quarterly Business Review | Vendor performance review cadence (Sheet 6) |
| **RBAC** | Role-Based Access Control | Access control model (Sheet 2) |
| **RPO** | Recovery Point Objective | Data loss tolerance (Sheet 5 Column V) |
| **RTO** | Recovery Time Objective | Downtime tolerance (Sheet 5 Column T) |
| **SLA** | Service Level Agreement | Vendor performance targets (Sheet 6) |

---

### 10.3 Related ISMS Documents

**Policy Layer:**

- ISMS-POL-A.5.19-23: Supplier & Cloud Services Security Policy (Master)
- ISMS-POL-A.5.19-23-S4: Supplier Monitoring & Change Management
- ISMS-POL-A.5.19-23-S5: Cloud Services Security (Section 6: Operational Management)
- ISMS-POL-A.5.19-23-S6: Assessment Methodology & Automation

**Assessment Layer (Upstream Dependencies):**

- ISMS-IMP-A.5.23.S1: Cloud Service Inventory & Classification
- ISMS-IMP-A.5.23.S2: Vendor Due Diligence & Contracts
- ISMS-IMP-A.5.23.S3: Secure Configuration & Deployment

**Assessment Layer (Downstream Consumers):**

- ISMS-IMP-A.5.23.S5: Compliance Monitoring & Exit Planning

**Related Controls:**

- ISMS-POL-A.5.24-28: Information Security Incident Management
- ISMS-POL-A.5.30: ICT Readiness for Business Continuity
- ISMS-POL-A.8.8: Management of Technical Vulnerabilities

**Procedures:**

- ISMS Incident Management Procedure
- ISMS Change Management Procedure
- ISMS Access Review Procedure
- ISMS Business Continuity Plan

---

### 10.4 External Standards & Regulations

**International Standards:**

- ISO/IEC 27001:2022 - Information Security Management Systems (Control A.5.23)
- ISO/IEC 27002:2022 - Information Security Controls (Guidance for A.5.23)
- ISO/IEC 27005:2022 - Information Security Risk Management
- ISO 22301:2019 - Business Continuity Management Systems

**Regulatory Frameworks:**

- **DORA (Digital Operational Resilience Act):** EU Regulation 2022/2554 - Applies to financial entities
  - Article 15: ICT risk management framework
  - Article 16: ICT-related incident management
  - Article 28: Exit strategies for ICT service providers
- **NIS2 (Network and Information Security Directive 2):** EU Directive 2022/2555 - Applies to essential/important entities
  - Article 21: Cybersecurity risk management measures
  - Article 23: Incident notification (significant incidents ≤24 hours)
- **EU AI Act:** Regulation 2024/1689 - Applies to high-risk AI systems
  - Article 9: Risk management system for high-risk AI
  - Article 72: Post-market monitoring obligations
- **US CLOUD Act:** Clarifying Lawful Overseas Use of Data Act (2018)
  - Allows US government to compel US companies to produce data stored anywhere
  - Addressed in Sheet 7 (Jurisdictional Risk Assessment)

**Compliance Frameworks:**

- CIS Controls v8 - Center for Internet Security benchmarks
- NIST Cybersecurity Framework (CSF)
- SOC 2 Type II - Service Organization Control audit reports
- PCI DSS 4.0 - Payment Card Industry Data Security Standard

---

### 10.5 Regulatory Applicability Decision Matrix

**Quick reference to determine which regulatory columns apply to your organization.**

| If Your Organization Is... | Complete These Sheets/Columns | Justification |
|----------------------------|------------------------------|---------------|
| **EU Financial Entity** (bank, insurance, investment firm) | Sheet 6: Columns Y-AA (DORA), Sheet 7 (if US vendor) | DORA mandates ICT risk management for financial entities |
| **EU Essential/Important Entity** (energy, transport, health, digital infra) | Sheet 4: Column Z (NIS2), Sheet 6: Column Z (NIS2) | NIS2 requires cybersecurity measures for critical sectors |
| **Using High-Risk AI Systems** (biometrics, critical infra, law enforcement) | Sheet 6: Column AA (AI Act) | EU AI Act requires ongoing monitoring of high-risk AI |
| **Using US-Headquartered Providers** (Microsoft, AWS, Google, Oracle, Salesforce) | Sheet 7: ALL columns (Jurisdictional Risk) | CLOUD Act exposure requires data sovereignty assessment |
| **None of the Above** | Mark all regulatory columns as "N/A" | Standard governance only, no enhanced regulatory requirements |

---

### 10.6 Governance Maturity Model

**Assess your organization's governance maturity level:**

**Level 1: Initial (Ad Hoc)**

- Governance activities are reactive, not systematic
- Access reviews happen only when someone complains
- No centralized tracking of changes or incidents
- Vendor risk assessments done at onboarding only
- **Improvement Target:** Implement quarterly access reviews, basic change tracking

**Level 2: Repeatable (Documented)**

- Governance activities follow documented procedures
- Quarterly access reviews conducted for critical services
- Changes tracked in spreadsheet or ticketing system
- Vendor risk monitored annually
- **Improvement Target:** Automate reminders, integrate with CMDB/ITSM

**Level 3: Defined (Standardized)**

- Governance framework standardized across all cloud services
- Automated reminders for access reviews, BC tests
- Integration with CMDB, ITSM, risk management systems
- Vendor risk scoring methodology consistent
- **Improvement Target:** Metrics-driven improvement, predictive analytics

**Level 4: Managed (Measured)**

- Governance KPIs tracked and reported to management
- Continuous improvement based on metrics
- Vendor risk scoring incorporates external threat intel
- BC/DR testing includes multi-vendor failover scenarios
- **Improvement Target:** Full automation, AI-assisted risk assessment

**Level 5: Optimized (Continuous Improvement)**

- Governance is fully automated with human oversight
- Predictive analytics identify risks before they materialize
- Industry-leading governance practices
- Governance framework continuously evolves
- **Maintain excellence, share best practices**

---

### 10.7 Common Governance Metrics (KPIs)

**Track these KPIs quarterly to measure governance effectiveness:**

| Metric | Target | Source | Trend Indicator |
|--------|--------|--------|----------------|
| **Access Review Completion Rate** | ≥95% within 15 days | Sheet 2 | ↑ Good, ↓ Bad |
| **Overdue Access Reviews** | 0 | Sheet 2, Column R | ↑ Bad, ↓ Good |
| **Admin Account Recertification Rate** | 100% quarterly | Sheet 2, Column T | = 100% always |
| **Unapproved Changes** | 0 | Sheet 3 | ↑ Bad, ↓ Good |
| **Emergency Changes (% of total)** | <5% | Sheet 3 | ↑ Bad (lack of planning), ↓ Good |
| **Open Incidents (P1/P2)** | 0 | Sheet 4 | ↑ Bad, ↓ Good |
| **Mean Time To Repair (MTTR)** | Service-specific | Sheet 4, Column S | ↑ Bad, ↓ Good |
| **BC/DR Test Pass Rate** | 100% | Sheet 5, Column S | = 100% always |
| **Overdue BC/DR Tests** | 0 | Sheet 5 | ↑ Bad, ↓ Good |
| **High-Risk Vendors** | <10% of portfolio | Sheet 6, Column G | ↑ Bad, ↓ Good |
| **Vendors with Expired Certifications** | 0 | Sheet 6, Column T-U | ↑ Bad, ↓ Good |
| **Overall Governance Compliance** | ≥90% | Sheet 9 (Dashboard) | ↑ Good, ↓ Bad |

**Dashboard Example:**

```
QUARTERLY GOVERNANCE KPIs - Q2 2026

Access Management:
  Access Review Completion: 92% (Target: ≥95%)        [↓ vs Q1: 96%]
  Overdue Reviews: 3                                  [↑ vs Q1: 1]
  Admin Recertification: 100%                         [= Q1: 100%]

Change Management:
  Unapproved Changes: 0                               [= Q1: 0]
  Emergency Changes: 3.2%                             [↓ vs Q1: 4.1%]

Incident Management:
  Open P1/P2 Incidents: 1 (AWS outage)                [↑ vs Q1: 0]
  MTTR (Average): 4.2 hours                           [↑ vs Q1: 3.1h]

Business Continuity:
  BC/DR Test Pass Rate: 100%                          [= Q1: 100%]
  Overdue Tests: 0                                    [= Q1: 0]

Vendor Risk:
  High-Risk Vendors: 2 (8% of portfolio)              [= Q1: 2]
  Expired Certifications: 0                           [= Q1: 0]

OVERALL GOVERNANCE HEALTH: 88%                        [↓ vs Q1: 91%]

ACTION ITEMS:
1. Address overdue access reviews (target: 0 by end of Q3)
2. Investigate MTTR increase (AWS incident postmortem)
3. Accelerate access review completion (consider automation)
```

---

### 10.8 Troubleshooting Guide

**Common issues and resolutions when completing this assessment.**

| Problem | Possible Cause | Resolution |
|---------|---------------|------------|
| **"Dashboard formulas showing #REF! error"** | Sheet references broken after copying workbook | Verify sheet names match exactly (case-sensitive). Check formula references point to correct sheets. |
| **"Cannot select dropdown values"** | Data validation removed or corrupted | Reapply data validation using instructions sheet dropdown definitions. |
| **"Evidence files not accessible"** | File paths changed or permissions issue | Update Column J (Evidence_Location) with current paths. Verify network share permissions. |
| **"Integration script fails"** | CMDB/ITSM API credentials expired | Regenerate API tokens, update script credentials. |
| **"Services missing from 5.23.4 that exist in 5.23.1"** | Inventory not synchronized | Run reconciliation (Section 9.3 Step 1). Copy services from 5.23.1 inventory. |
| **"Approval workflow stuck"** | Approver on leave or unresponsive | Escalate to backup approver per ISMS escalation procedure. |
| **"Quarterly review overdue"** | Coordinator missed calendar reminder | Set recurring calendar invites. Consider automated reminder script (Section 9.5). |

---

### 10.9 Contact Information & Escalation Path

**Template - Customize for [Organization].**

```
GOVERNANCE ASSESSMENT SUPPORT CONTACTS

GENERAL QUESTIONS:
  Cloud Operations Team
  Email: cloud-ops@[organization].com
  Teams: Cloud Operations Channel
  Response Time: 1 business day

ACCESS REVIEW QUESTIONS (Sheet 2):
  Identity & Access Management (IAM) Team
  Email: iam@[organization].com
  Phone: +XX XXX XXX XXXX
  Response Time: 2 business days
  Escalation: IAM Manager

CHANGE MANAGEMENT QUESTIONS (Sheet 3):
  Change Advisory Board (CAB)
  Email: cab@[organization].com
  Meeting: Weekly Thursdays 10:00 AM
  Response Time: Next CAB meeting
  Escalation: CIO

INCIDENT MANAGEMENT QUESTIONS (Sheet 4):
  Security Operations Center (SOC)
  Email: soc@[organization].com
  Phone: +XX XXX XXX XXXX (24/7 hotline)
  Response Time: Immediate (P1/P2), 4 hours (P3/P4)
  Escalation: Incident Commander → CISO

BUSINESS CONTINUITY QUESTIONS (Sheet 5):
  Business Continuity Planning Team
  Email: bcdr@[organization].com
  Phone: +XX XXX XXX XXXX
  Response Time: 2 business days
  Escalation: Business Continuity Manager

VENDOR RISK QUESTIONS (Sheet 6):
  Vendor Management Office
  Email: vendor-risk@[organization].com
  Response Time: 3 business days
  Escalation: Chief Risk Officer (CRO)

COMPLIANCE/REGULATORY QUESTIONS:
  Compliance Officer
  Email: compliance@[organization].com
  Phone: +XX XXX XXX XXXX
  Response Time: 3 business days
  Escalation: General Counsel

APPROVAL WORKFLOW (Sheet 11):
  ISMS Coordinator
  Email: isms-coordinator@[organization].com
  Response Time: 1 business day
  Escalation: CISO

TOOL/WORKBOOK TECHNICAL ISSUES:
  ISMS Implementation Team
  Email: isms-admin@[organization].com
  Response Time: 1 business day
  Escalation: ISMS Program Manager
```

---

### 10.10 Document Revision History

**Tracking changes to this IMP document.**

| Version | Date | Section(s) Modified | Changes Summary | Author |
|---------|------|---------------------|-----------------|--------|
| 1.0 | [Date] | All | Initial release (Part II only - technical spec) | ISMS Implementation Team |

**Future Version Planning:**

| Planned Version | Target Date | Planned Changes |
|----------------|-------------|-----------------|
| 2.1 | Q2 2026 | Add automation examples (Python scripts for ITSM/CMDB integration) |
| 2.2 | Q3 2026 | Expand troubleshooting guide based on user feedback |
| 3.0 | Q1 2027 | Major update if regulatory landscape changes significantly (e.g., new DORA technical standards) |

---

**END OF SECTION 10: APPENDICES & GLOSSARY**

**END OF PART I: USER COMPLETION GUIDE**

---

# ISMS-IMP-A.5.23.S4 - Ongoing Governance & Risk Management
# PART II: TECHNICAL SPECIFICATION - Section 1 of 4

---

**Document:** ISMS-IMP-A.5.23.S4 - Ongoing Governance & Risk Management  
**Part:** II - Technical Specification  
**Section:** 1 of 4 (Workbook Overview + Sheets 1-2)  
**Version:** 1.0 
**Date:** [Date]

---

## Table of Contents - Section 1

1. **Workbook Structure Overview**
2. **Cell Styling Reference**
3. **Base Column Definitions (A-Q)**
4. **Sheet 1: Instructions & Legend**
5. **Sheet 2: Access Review & Recertification**

---

# Workbook Structure Overview

## Sheet Architecture (11 Sheets)

```
┌─────────────────────────────────────────────────────────────────────┐
│              ISMS-IMP-A.5.23.S4 WORKBOOK STRUCTURE.                 │
│              (Ongoing Governance & Risk Management)                 │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  LAYER 1: ORIENTATION                                               │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │ Sheet 1: Instructions & Legend                                │  │
│  │          Assessment purpose, regulatory guidance, legend      │  │
│  └───────────────────────────────────────────────────────────────┘  │
│                                                                     │
│  LAYER 2: GOVERNANCE ACTIVITIES (Quarterly/Ongoing)                 │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │ Sheet 2: Access Review & Recertification                      │  │
│  │          24 columns (A-X): Quarterly access reviews, admin    │  │
│  ├───────────────────────────────────────────────────────────────┤  │
│  │ Sheet 3: Change Management                                    │  │
│  │          24 columns (A-X): Provider changes, config changes   │  │
│  ├───────────────────────────────────────────────────────────────┤  │
│  │ Sheet 4: Incident Management                                  │  │
│  │          24 columns (A-X): Detection, response, lessons       │  │
│  ├───────────────────────────────────────────────────────────────┤  │
│  │ Sheet 5: Business Continuity                                  │  │
│  │          24 columns (A-X): BC/DR testing, RTO/RPO validation  │  │
│  ├───────────────────────────────────────────────────────────────┤  │
│  │ Sheet 6: Vendor Risk Monitoring                               │  │
│  │          24 columns (A-X): Ongoing vendor assessment          │  │
│  └───────────────────────────────────────────────────────────────┘  │
│                                                                     │
│  LAYER 3: ANNUAL REVIEWS (NEW v2.1 - DORA Article 28.6)             │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │ Sheet 7: Exit Strategy Review & PoC Testing                   │  │
│  │          14 columns (A-N): Annual exit plan review + testing  │  │
│  └───────────────────────────────────────────────────────────────┘  │
│                                                                     │
│  LAYER 4: REGULATORY COMPLIANCE                                     │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │ Sheet 8: Jurisdictional Risk Assessment                       │  │
│  │          20 columns (A-T): CLOUD Act, data sovereignty        │  │
│  └───────────────────────────────────────────────────────────────┘  │
│                                                                     │
│  LAYER 5: CONSOLIDATION & APPROVAL                                  │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │ Sheet 9: Summary Dashboard                                    │  │
│  │          3 tables: Governance + Jurisdictional + Regulatory   │  │
│  ├───────────────────────────────────────────────────────────────┤  │
│  │ Sheet 10: Evidence Register                                   │  │
│  │          Centralized evidence tracking (all sheets)           │  │
│  ├───────────────────────────────────────────────────────────────┤  │
│  │ Sheet 11: Approval Sign-Off                                   │  │
│  │          5-stage: IT Ops → Compliance → DPO → CRO → CISO      │  │
│  └───────────────────────────────────────────────────────────────┘  │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

## Version Control

| Version | Date | Changes | Sheets Affected |
|---------|------|---------|-----------------|
| **1.0** | [Date] | Initial release (10 sheets) | All (original) |

**Key v2.1 Enhancements:**

- **NEW Sheet 7:** Exit Strategy Annual Review + PoC Testing (DORA Art. 28.6 requirement)
- **Sheet 8:** Jurisdictional Risk
- **Sheet 9:** Dashboard +1 table for exit strategy readiness
- **Sheet 11:** +DPO and CRO approval sections

## Regulatory Compliance Coverage

| Regulation | Affected Sheets | Key Requirements |
|------------|----------------|------------------|
| **DORA (Digital Operational Resilience Act)** | Sheets 4, 6, 7, 9, 11 | Incident management, ICT risk monitoring, exit strategy testing (Art. 28.6) |
| **NIS2 (Network and Information Security Directive 2)** | Sheets 4, 9, 11 | Significant incident notification (≤24h), cybersecurity measures |
| **EU AI Act** | Sheets 6, 9, 11 | High-risk AI system monitoring, post-market surveillance |
| **US CLOUD Act** | Sheet 8 | Jurisdictional risk assessment, cross-border data access exposure |

---

# Cell Styling Reference

## Style Definitions

All styles use **NEW object creation per cell** to avoid Excel "shared object" repair warnings.

| Style Name | Font | Fill Color | Alignment | Usage |
|------------|------|------------|-----------|-------|
| **header** | Calibri 14, Bold, White | Dark Blue (003366) | Center, Wrap | Section headers (Row 1) |
| **subheader** | Calibri 11, Bold, White | Medium Blue (4472C4) | Center, Wrap | Policy references (Row 2) |
| **column_header** | Calibri 10, Bold, Black | Light Gray (D9D9D9) | Center, Wrap | Column headers (Row 4) |
| **input_cell** | Calibri 10, Black | Light Yellow (FFFFCC) | Left, Wrap | Editable data cells (Rows 5-30) |
| **warning** | Calibri 10, Bold, Red | Light Orange (FFEB9C) | Left, Wrap | Warning messages |

## Border Standards

- **All cells:** Thin borders (1px solid) on all sides
- **Merged cells:** Apply border to entire merged range
- **Data rows:** Consistent thin borders for professional appearance

## Row Heights

| Row Type | Height (points) | Rationale |
|----------|-----------------|-----------|
| Section Header (Row 1) | 50 | Accommodate 2-line title + subtitle |
| Policy Reference (Row 2) | 30 | Clear policy requirement visibility |
| Spacer (Row 3) | 15 (default) | Visual separation |
| Column Headers (Row 4) | 15 (default) | Standard header height |
| Data Rows (5-30) | 15 (default) | Auto-adjust based on content |

## Column Widths

**Base columns (A-Q)** - Standard across all governance sheets (Sheets 2-6):

- Column A (Assessment_ID): 14
- Column B (Cloud_Service_Name): 28
- Column C (Vendor_Name): 22
- Column D (Service_Type): 20
- Column E (Environment): 18
- Column F (Service_Criticality): 18
- Column G (Governance_Area_Specific): 18-20 (varies by sheet)
- Column H (Configuration_Item): 30
- Column I (Status): 15
- Column J (Evidence_Location): 30
- Column K (Gap_Description): 35
- Column L (Remediation_Needed): 16
- Column M (Exception_ID): 14
- Column N (Risk_ID): 14
- Column O (Compensating_Controls): 30
- Column P (Responsible_Team): 20
- Column Q (Target_Remediation_Date): 18

**Extended columns (R-X)** - Vary by sheet (see individual sheet specs)

---

# Base Column Definitions (A-Q)

## Standard Columns for ALL Governance Assessment Sheets

These 17 columns (A-Q) are **identical** across Sheets 2-6 to enable dashboard consolidation.

| Column | Field Name | Width | Data Type | Validation | Formula | Description |
|--------|-----------|-------|-----------|------------|---------|-------------|
| **A** | Assessment_ID | 14 | Formula | - | `=CONCATENATE("GOV-",TEXT(ROW()-4,"000"))` | Auto-generated unique ID (GOV-001, GOV-002, etc.) |
| **B** | Cloud_Service_Name | 28 | Text | - | - | Service name (import from IMP-5.23.1 Sheet 2 Column B) |
| **C** | Vendor_Name | 22 | Text | - | - | Vendor/provider name (import from IMP-5.23.1 Sheet 2 Column C) |
| **D** | Service_Type | 20 | Dropdown | SaaS, IaaS, PaaS, Security Service, Storage Service | - | Cloud service category |
| **E** | Environment | 18 | Dropdown | Production, Staging, Development, Test, All Environments | - | Where this service is deployed |
| **F** | Service_Criticality | 18 | Dropdown | Critical, High, Medium, Low | - | Business impact if unavailable (from IMP-5.23.1) |
| **G** | Governance_Area | 18-20 | Dropdown | **VARIES BY SHEET** (see sheet-specific specs) | - | Sheet-specific governance dimension |
| **H** | Configuration_Item | 30 | Text | - | - | Specific governance item being assessed |
| **I** | Status | 15 | Dropdown | ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant, N/A | - | Governance compliance status |
| **J** | Evidence_Location | 30 | Text | - | - | Path/URL to evidence file |
| **K** | Gap_Description | 35 | Text | - | - | If not Compliant: describe the gap |
| **L** | Remediation_Needed | 16 | Dropdown | Yes, No, N/A | - | Does this gap require remediation? |
| **M** | Exception_ID | 14 | Text | - | - | If exception approved: reference exception document ID |
| **N** | Risk_ID | 14 | Text | - | - | If risk accepted: reference risk register entry |
| **O** | Compensating_Controls | 30 | Text | - | - | Alternative controls if governance item not fully compliant |
| **P** | Responsible_Team | 20 | Dropdown | IT Operations, Cloud Ops, Security, Compliance, Risk Management | - | Team responsible for remediation |
| **Q** | Target_Remediation_Date | 18 | Date | - | - | Target date to close gap (if remediation needed) |

## Data Validation Rules (Base Columns)

**Dropdowns implemented via `openpyxl.worksheet.datavalidation.DataValidation`:**

```python
# Service Type (Column D)
service_type_dv = DataValidation(
    type="list",
    formula1='"SaaS,IaaS,PaaS,Security Service,Storage Service"',
    allow_blank=False
)
ws.add_data_validation(service_type_dv)
service_type_dv.add("D5:D30")

# Environment (Column E)
environment_dv = DataValidation(
    type="list",
    formula1='"Production,Staging,Development,Test,All Environments"',
    allow_blank=False
)
ws.add_data_validation(environment_dv)
environment_dv.add("E5:E30")

# Service Criticality (Column F)
criticality_dv = DataValidation(
    type="list",
    formula1='"Critical,High,Medium,Low"',
    allow_blank=False
)
ws.add_data_validation(criticality_dv)
criticality_dv.add("F5:F30")

# Status (Column I) - with UTF-8 symbols
status_dv = DataValidation(
    type="list",
    formula1=f'"{CHECK} Compliant,{WARNING} Partial,{XMARK} Non-Compliant,N/A"',
    allow_blank=False
)
ws.add_data_validation(status_dv)
status_dv.add("I5:I30")

# Remediation Needed (Column L)
yes_no_dv = DataValidation(
    type="list",
    formula1='"Yes,No,N/A"',
    allow_blank=False
)
ws.add_data_validation(yes_no_dv)
yes_no_dv.add("L5:L30")

# Responsible Team (Column P)
responsible_team_dv = DataValidation(
    type="list",
    formula1='"IT Operations,Cloud Ops,Security,Compliance,Risk Management"',
    allow_blank=False
)
ws.add_data_validation(responsible_team_dv)
responsible_team_dv.add("P5:P30")
```

## UTF-8 Symbol Encoding

**Status symbols used in dropdowns:**

```python
CHECK = '\u2705'      # ✅ Green checkmark (Compliant)
WARNING = '\u26A0'    # ⚠️ Warning sign (Partial)
XMARK = '\u274C'      # ❌ Red X (Non-Compliant)
```

---

# Sheet 1: Instructions & Legend

## Purpose & Layout

**Sheet Name:** `Instructions & Legend`

**Purpose:** Provide user orientation, governance assessment context, status legend, evidence requirements, and regulatory applicability guidance.

**Layout:** Free-form text layout with merged cells, no data validation (read-only reference).

## Sheet Structure

```
┌───────────────────────────────────────────────────────────────┐
│ Row 1:  ISMS-IMP-A.5.23.S4 – Ongoing Governance v2.1          │
│         (Header, merged A1:C1)                                │
├───────────────────────────────────────────────────────────────┤
│ Row 2:  ISO/IEC 27001:2022 - Control A.5.23                   │
│         (Subheader, merged A2:C2)                             │
├───────────────────────────────────────────────────────────────┤
│ Row 4+: DOCUMENT INFORMATION                                  │
│         - Document ID: ISMS-IMP-A.5.23.S4                     │
│         - Assessment Area: Ongoing Governance & Risk Mgmt     │
│         - Related Policy: ISMS-POL-A.5.19-23-S5 Section 6     │
│         - Version: 2.1 (DORA Exit Strategy Update)            │
│         - Assessment Date: [Input field]                      │
│         - Completed By: [Input field]                         │
│         - Organization: [Input field]                         │
│         - Review Cycle: Quarterly (+ Annual Exit Review)      │
├───────────────────────────────────────────────────────────────┤
│ HOW TO USE THIS WORKBOOK (Step-by-step instructions)          │
├───────────────────────────────────────────────────────────────┤
│ SHEET NAVIGATION GUIDE (11 sheets explained)                  │
├───────────────────────────────────────────────────────────────┤
│ STATUS LEGEND (✅ ⚠️ ❌ N/A definitions)                      │
├───────────────────────────────────────────────────────────────┤
│ EVIDENCE REQUIREMENTS (logs, reports, test results)           │
├───────────────────────────────────────────────────────────────┤
│ REGULATORY APPLICABILITY GUIDE (DORA/NIS2/AI Act/CLOUD Act)   │
├───────────────────────────────────────────────────────────────┤
│ VERSION HISTORY (1.0 → 2.0 → 2.1 updates)                     │
├───────────────────────────────────────────────────────────────┤
│ CONTACT INFORMATION (coordinator, IT ops, compliance, CISO)   │
└───────────────────────────────────────────────────────────────┘
```

## Key Content Sections

### Document Information

| Attribute | Value | Notes |
|-------|-------|-------|
| Document ID | ISMS-IMP-A.5.23.S4 | Fixed |
| Assessment Area | Ongoing Governance & Risk Management | Fixed |
| Related Policy | ISMS-POL-A.5.19-23-S5 Section 6 | Fixed |
| Version | 2.1 (DORA Exit Strategy Update) | Fixed |
| Assessment Date | [Input field] | Yellow fill, user-editable |
| Completed By | [Input field] | Yellow fill, user-editable |
| Organization | [Input field] | Yellow fill, user-editable |
| Review Cycle | Quarterly (+ Annual Exit Review) | Fixed |

### How to Use This Workbook

**Instructions (summary):**
1. Reference ISMS-IMP-A.5.23.S1 (Inventory) for service list
2. Complete Sheets 2-6 for quarterly governance activities
3. Complete Sheet 7 annually for exit strategy review (DORA requirement)
4. Complete Sheet 8 for jurisdictional risk (US-nexus providers only)
5. Use dropdown menus for standardized entries
6. Provide evidence links for all governance claims
7. Dashboard formulas automatically calculate compliance
8. Review evidence register for completeness
9. Obtain sequential approvals (IT Ops → Compliance → DPO → CRO → CISO)

### Sheet Navigation Guide

**11-Sheet Overview:**

| Sheet # | Sheet Name | Purpose | Review Frequency |
|---------|------------|---------|------------------|
| 1 | Instructions & Legend | Orientation | Read first |
| 2 | 2. Access Review | Quarterly access recertification | Quarterly |
| 3 | 3. Change Management | Provider/config change tracking | Quarterly + ongoing |
| 4 | 4. Incident Management | Security/availability incidents | Quarterly + ongoing |
| 5 | 5. Business Continuity | BC/DR testing, RTO/RPO validation | Quarterly + annual full test |
| 6 | 6. Vendor Risk Monitoring | Ongoing vendor assessment | Quarterly + triggered |
| 7 | 7. Exit Strategy Review | Annual exit plan + PoC testing (DORA) | **Annually** |
| 8 | 8. Jurisdictional Risk | CLOUD Act exposure (US vendors) | Quarterly + triggered |
| 9 | 9. Summary Dashboard | Compliance metrics, gaps | Auto-calculated |
| 10 | 10. Evidence Register | Evidence tracking | As evidence collected |
| 11 | 11. Approval Sign-Of | 5-stage approval workflow | After assessment complete |

### Status Legend

| Symbol | Status | Definition | Usage |
|--------|--------|------------|-------|
| ✅ | Compliant | Governance activity completed per requirements, evidence provided | Use when governance item verified compliant |
| ⚠️ | Partial | Governance activity partially compliant, minor gaps exist | Use when mostly compliant but improvements needed |
| ❌ | Non-Compliant | Governance activity fails requirements, remediation required | Use when governance item is missing/inadequate |
| N/A | Not Applicable | Governance item not relevant to this service/environment | Use when governance item doesn't apply |

### Evidence Requirements

**Acceptable Evidence Types by Governance Area:**

| Governance Area | Evidence Type | Example |
|--------------------|---------------|---------|
| Access Review | Access review report export | Quarterly access review report (CSV/PDF) from IAM system |
| Change Management | Change ticket log | ServiceNow change ticket screenshots/export |
| Incident Management | Incident management report | Incident log from SIEM, MTTR metrics report |
| Business Continuity | BC/DR test report | Annual BC test results, RTO/RPO achievement |
| Vendor Risk | Vendor risk assessment | Vendor risk scorecard, security incident notifications |
| Exit Strategy | Exit plan document + PoC test report | Exit strategy document + annual PoC test results (DORA) |
| Jurisdictional Risk | Legal assessment memo | DPO/Legal opinion on CLOUD Act exposure |

**Evidence Location Format:**

- **File share:** `\\fileserver\ISMS\Evidence\A.5.23.4\[Service_Name]\[Governance_Area]\[Filename]`
- **SharePoint:** `https://[org].sharepoint.com/sites/ISMS/Evidence/A.5.23.4/[Service]/[File]`
- **ITSM:** Ticket IDs (INC-###, CHG-###, RITM-###)

### Regulatory Applicability Guide (v2.1 UPDATE)

**When to Complete Regulatory Sheets/Columns:**

| Regulation | Applies If... | Required Sheets | Required Columns |
|------------|---------------|-----------------|------------------|
| **DORA** | [Organization] is EU financial institution or critical ICT provider | Sheet 4 (Incident Mgmt), Sheet 7 (Exit Strategy) | Sheet 7: ALL columns (A-N) - Annual exit plan review |
| **NIS2** | [Organization] is Essential/Important Entity under NIS2 | Sheet 4 (Incident Mgmt) | Sheet 4: Enhanced incident notification tracking |
| **EU AI Act** | Cloud service includes high-risk AI components | Sheet 6 (Vendor Risk) | Sheet 6: AI system monitoring requirements |
| **US CLOUD Act** | Cloud provider has US nexus (HQ, subsidiary, operations in US) | Sheet 8 (Jurisdictional Risk) | Sheet 8: ALL columns (A-T) |

**NEW in v2.1 - DORA Article 28.6 Exit Strategy Requirement:**

```
If [Organization] is subject to DORA (EU financial institutions):
  ├─ Complete Sheet 7 (Exit Strategy Annual Review) ANNUALLY
  ├─ Conduct Proof-of-Concept (PoC) testing of exit strategies ANNUALLY
  ├─ Document PoC test results (Column J-N)
  └─ Report results to management and supervisory authorities

Otherwise:
  └─ Sheet 7 is OPTIONAL (but recommended as best practice)
```

### Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | [Date] | Initial release (10 sheets, no regulatory) |

---

# Sheet 2: Access Review & Recertification

## Purpose & Layout

**Sheet Name:** `2. Access Review`

**Purpose:** Assess quarterly access reviews and admin access recertification for all cloud services.

**Policy Reference:** ISMS-POL-A.5.19-23-S5, Section 6.1 (Access Management)

**Assessment Question:** "Are access reviews conducted quarterly with admin/privileged access recertified and documented?"

## Column Structure (A-X, 24 columns)

**Base Columns (A-Q):** Standard 17 columns (see Section 3)

**Column G Specialization:** `Review_Period` (Dropdown: Q1, Q2, Q3, Q4, Annual)

**Extended Columns (R-X):** Access review-specific

| Column | Field Name | Width | Data Type | Validation | Description |
|--------|-----------|-------|-----------|------------|-------------|
| **R** | Last_Review_Date | 18 | Date | - | Date of last access review |
| **S** | Admin_Count | 14 | Integer | Positive integer | Number of admin/privileged accounts |
| **T** | Admin_Recertified | 18 | Dropdown | Yes, No, Pending | Were admin accounts recertified by business owner? |
| **U** | Inactive_Accounts_Disabled | 20 | Dropdown | Yes, No, Partial | Were inactive accounts (>90 days) disabled? |
| **V** | Orphaned_Accounts_Removed | 20 | Dropdown | Yes, No, Partial | Were orphaned accounts (user left org) removed? |
| **W** | JIT_Access_Used | 16 | Dropdown | Yes, No, N/A | Is Just-In-Time (JIT) access used for admin privileges? |
| **X** | Next_Review_Due | 18 | Date | Formula: `=R+90` | Next quarterly review date (90 days from last) |

## Data Validation Rules (Extended Columns)

```python
# Admin Count (Column S)
admin_count_dv = DataValidation(
    type="whole",
    operator="greaterThanOrEqual",
    formula1="0",
    allow_blank=True
)
ws.add_data_validation(admin_count_dv)
admin_count_dv.add("S5:S30")

# Admin Recertified (Column T)
admin_recertified_dv = DataValidation(
    type="list",
    formula1='"Yes,No,Pending"',
    allow_blank=False
)
ws.add_data_validation(admin_recertified_dv)
admin_recertified_dv.add("T5:T30")

# Inactive Accounts Disabled (Column U)
inactive_accounts_dv = DataValidation(
    type="list",
    formula1='"Yes,No,Partial"',
    allow_blank=False
)
ws.add_data_validation(inactive_accounts_dv)
inactive_accounts_dv.add("U5:U30")

# Orphaned Accounts Removed (Column V)
orphaned_accounts_dv = DataValidation(
    type="list",
    formula1='"Yes,No,Partial"',
    allow_blank=False
)
ws.add_data_validation(orphaned_accounts_dv)
orphaned_accounts_dv.add("V5:V30")

# JIT Access Used (Column W)
jit_access_dv = DataValidation(
    type="list",
    formula1='"Yes,No,N/A"',
    allow_blank=False
)
ws.add_data_validation(jit_access_dv)
jit_access_dv.add("W5:W30")
```

## Section Headers

```
Row 1 (merged A1:X1):
  "ACCESS REVIEW & RECERTIFICATION ASSESSMENT
   ISMS-POL-A.5.19-23-S5, Section 6.1: Quarterly Access Reviews"

Row 2 (merged A2:X2):
  "Assessment Question: Are access reviews conducted quarterly with 
   admin/privileged access recertified and documented?"
```

## Compliance Checklist (Rows 33+)

**Checklist Items (15 items):**

| # | Requirement | Evidence Type |
|---|-------------|---------------|
| 1 | Access reviews conducted quarterly for ALL cloud services | Access review schedule/calendar |
| 2 | Admin/privileged accounts recertified by business owner | Admin recertification report |
| 3 | Inactive accounts (>90 days) disabled automatically | IAM lifecycle policy config |
| 4 | Orphaned accounts (user left org) removed within 24 hours | Offboarding process doc |
| 5 | Service accounts inventoried and reviewed | Service account inventory |
| 6 | Access rights aligned with current job roles | Access review delta report |
| 7 | Just-In-Time (JIT) access implemented for admin privileges | PAM tool configuration |
| 8 | Access review results documented with approvals | Signed review report |
| 9 | Privilege creep identified and remediated | Access rightsizing report |
| 10 | Emergency access (break-glass) accounts reviewed | Break-glass account log |
| 11 | MFA enforced for all admin accounts (minimum) | MFA enforcement report |
| 12 | Access review deviations escalated to management | Exception log |
| 13 | Federated identity used (no local cloud accounts) | IdP integration validation |
| 14 | Access review metrics reported to CISO quarterly | Access metrics dashboard |
| 15 | Automated reminders sent to service owners before due date | Reminder email logs |

## Example Data Row

**Row 7 (Example - AWS Production Account):**

| Col | Value | Notes |
|-----|-------|-------|
| A | GOV-003 | Auto-generated |
| B | AWS Production Account | Service name |
| C | Amazon Web Services | Vendor |
| D | IaaS | Service type |
| E | Production | Environment |
| F | Critical | Criticality |
| G | Q1 | Review period |
| H | IAM User Access Review | Config item |
| I | ✅ Compliant | Status |
| J | `s3://isms-evidence/A.5.23.4/AWS/Q1_Access_Review.pdf` | Evidence path |
| K | - | No gap |
| L | No | No remediation |
| M | - | No exception |
| N | - | No risk ID |
| O | - | No compensating controls |
| P | IT Operations | Responsible team |
| Q | - | No target date |
| R | 15.01.2026 | Last review date |
| S | 8 | Admin count |
| T | Yes | Admin recertified |
| U | Yes | Inactive accounts disabled (automated) |
| V | Yes | Orphaned accounts removed (HR integration) |
| W | Yes | JIT via AWS IAM Identity Center |
| X | 15.04.2026 | Next review due (90 days) |

## Integration Points

**Exports to Sheet 9 (Dashboard):**

- Column I (Status): Access review compliance metrics
- Column R (Last_Review_Date): Overdue review tracking
- Column T (Admin_Recertified): Admin recertification compliance

**Exports to Sheet 10 (Evidence Register):**

- Column J (Evidence_Location): Access review evidence tracking

---

**END OF SECTION 1**

*Next Section: Sheets 3-6 (Change Management, Incident Management, Business Continuity, Vendor Risk)*

---

# ISMS-IMP-A.5.23.S4 - Ongoing Governance & Risk Management
# PART II: TECHNICAL SPECIFICATION - Sections 2-4 of 4

---

**Document:** ISMS-IMP-A.5.23.S4 - Ongoing Governance & Risk Management  
**Part:** II - Technical Specification  
**Sections:** 2-4 (Complete remaining sheets + integration)  
**Version:** 1.0  
**Date:** [Date]

---

# SECTION 2: SHEETS 3-6 (GOVERNANCE ACTIVITIES)

## Sheet 3: Change Management

### Purpose & Layout

**Sheet Name:** `3. Change Management`

**Purpose:** Track all changes to cloud services (provider changes, configuration changes, integrations) and ensure proper approval/review.

**Policy Reference:** ISMS-POL-A.5.19-23-S5, Section 6.2 (Change Management)

**Assessment Question:** "Are all cloud service changes following change management process with proper approvals?"

### Column Structure (A-X, 24 columns)

**Base Columns (A-Q):** Standard 17 columns

**Column G Specialization:** `Change_Type` (Dropdown: Provider Change, Config Change, Integration Change, Emergency Change, Scheduled Maintenance)

**Extended Columns (R-X):**

| Column | Field Name | Width | Type | Validation |
|--------|-----------|-------|-----------|------------|
| **R** | Change_Count_Period | 18 | Integer | ≥0 |
| **S** | Impact_Level | 16 | Dropdown | Critical, High, Medium, Low |
| **T** | Approval_Status | 18 | Dropdown | Approved, Pending, Rejected, Emergency |
| **U** | Rollback_Plan_Documented | 20 | Dropdown | Yes, No, N/A |
| **V** | Rollback_Tested | 16 | Dropdown | Yes, No, N/A |
| **W** | Post_Change_Review_Done | 20 | Dropdown | Yes, No, Pending |
| **X** | Security_Impact_Assessed | 20 | Dropdown | Yes, No, N/A |

### Compliance Checklist (15 items)

```
☐ Change management process documented for cloud services
☐ Provider change notifications monitored and assessed
☐ Configuration changes require security review before approval
☐ Integration changes assessed for data flow impact
☐ Emergency change process defined with post-review requirement
☐ Emergency changes reviewed within 48 hours
☐ Rollback procedures documented for critical changes
☐ Rollback procedures tested before go-live (critical changes)
☐ Change calendar maintained and communicated
☐ Change conflicts identified and resolved
☐ Security impact assessment required for all changes
☐ Change audit trail maintained in ticketing system
☐ Failed changes documented with root cause
☐ Change success metrics tracked (success rate, rollback rate)
☐ Provider maintenance windows tracked and planned for
```

---

## Sheet 4: Incident Management

### Purpose & Layout

**Sheet Name:** `4. Incident Management`

**Purpose:** Track cloud service incidents (security, availability, performance) and lessons learned.

**Policy Reference:** ISMS-POL-A.5.19-23-S5, Section 6.3 (Incident Management)

**Assessment Question:** "Are cloud service incidents detected, responded to, and documented per incident management procedures?"

### Column Structure (A-X, 24 columns)

**Base Columns (A-Q):** Standard 17 columns

**Column G Specialization:** `Incident_Severity` (Dropdown: P1-Critical, P2-High, P3-Medium, P4-Low)

**Extended Columns (R-X):**

| Column | Field Name | Width | Type | Validation |
|--------|-----------|-------|-----------|------------|
| **R** | Incident_Count_Period | 18 | Integer | ≥0 |
| **S** | MTTR_Hours | 14 | Decimal | ≥0 |
| **T** | Root_Cause_Documented | 20 | Dropdown | Yes, No, Pending |
| **U** | Playbook_Updated | 16 | Dropdown | Yes, No, N/A |
| **V** | Vendor_Notified | 16 | Dropdown | Yes, No, N/A |
| **W** | Customer_Impact | 18 | Dropdown | Yes, No, Unknown |
| **X** | Lessons_Learned_Captured | 20 | Dropdown | Yes, No, Pending |

### Compliance Checklist (30 items - REGULATORY ENHANCED)

**Base Items (15):**
```
☐ Incident detection mechanisms in place for cloud services
☐ Alerting thresholds defined and tuned
☐ Incident classification aligned with org severity matrix
☐ Escalation paths defined for cloud service incidents
☐ Vendor notification procedures documented
☐ Vendor incident response SLAs tracked
☐ Internal incident response playbooks exist per service
☐ Playbooks reviewed/updated after incidents
☐ Root cause analysis performed for P1/P2 incidents
☐ Lessons learned documented and shared
☐ Problem management process identifies recurring issues
☐ Known error database maintained for cloud services
☐ Incident metrics reported to management
☐ MTTR/MTTD tracked per service
☐ Post-incident reviews conducted within defined timeframe
```

**DORA Items (+8):**
```
☐ ICT-related incidents classified per DORA Article 17
☐ Major incidents reported to senior management immediately
☐ Incident impact on critical operations documented
☐ Incident root cause traced to ICT dependency (vendor/config)
☐ Third-party incident monitoring activated
☐ Incident severity escalation to authorities (if major)
☐ ICT incident register maintained and reviewed quarterly
☐ Lessons learned integrated into ICT risk management
```

**NIS2 Items (+5):**
```
☐ Significant cybersecurity incidents identified per NIS2
☐ Incident notification to authorities within 24h (significant)
☐ Incident intermediate report within 72h (if applicable)
☐ Final incident report prepared within 1 month
☐ Cross-border incident coordination with other MS authorities
```

**AI Act Items (+6):**
```
☐ High-risk AI system incidents categorized separately
☐ AI system failure incidents logged with input/output data
☐ AI safety incident impact on human rights documented
☐ Post-market monitoring incident review conducted
☐ Serious AI incidents reported to market surveillance authority
☐ AI incident corrective actions implemented and verified
```

---

## Sheet 5: Business Continuity

### Purpose & Layout

**Sheet Name:** `5. Business Continuity`

**Purpose:** Track BC/DR testing, RTO/RPO validation, and failover capabilities for cloud services.

**Policy Reference:** ISMS-POL-A.5.19-23-S5, Section 6.4 (Business Continuity)

**Assessment Question:** "Are BC/DR plans tested annually with RTO/RPO achievement verified?"

### Column Structure (A-X, 24 columns)

**Base Columns (A-Q):** Standard 17 columns

**Column G Specialization:** `BC_Tier` (Dropdown: Tier 1 (<4hr), Tier 2 (<24hr), Tier 3 (<72hr), Tier 4 (Best Effort))

**Extended Columns (R-X):**

| Column | Field Name | Width | Type | Validation |
|--------|-----------|-------|-----------|------------|
| **R** | Last_Test_Date | 16 | Date | - |
| **S** | Test_Result | 16 | Dropdown | Passed, Failed, Partial, Not Tested |
| **T** | RTO_Target_Hours | 16 | Decimal | ≥0 |
| **U** | RTO_Achieved_Hours | 18 | Decimal | ≥0 |
| **V** | RPO_Target_Hours | 16 | Decimal | ≥0 |
| **W** | RPO_Achieved_Hours | 18 | Decimal | ≥0 |
| **X** | Next_Test_Due | 16 | Date | Formula: `=R5+365` |

### Compliance Checklist (15 items)

```
☐ BC/DR plan documented for Critical/High services
☐ Vendor BC/DR capabilities verified and documented
☐ RTO requirements defined per service criticality
☐ RPO requirements defined per data classification
☐ Failover procedures documented and accessible
☐ Failover tested annually (minimum)
☐ Test results documented with evidence
☐ RTO achievement verified during tests
☐ RPO achievement verified during tests
☐ Data backup restoration tested
☐ Multi-region/availability zone strategy documented
☐ Single points of failure identified and mitigated
☐ Communication plan exists for BC events
☐ Vendor dependency chain mapped for BC planning
☐ BC plan reviewed after significant changes
```

---

## Sheet 6: Vendor Risk Monitoring

### Purpose & Layout

**Sheet Name:** `6. Vendor Risk Monitoring`

**Purpose:** Ongoing monitoring of vendor security posture, certification expiry, incidents, financial health.

**Policy Reference:** ISMS-POL-A.5.19-23-S5, Section 6.5 (Vendor Risk Management)

**Assessment Question:** "Is cloud vendor risk monitored continuously with reassessment triggered by changes?"

### Column Structure (A-X, 24 columns)

**Base Columns (A-Q):** Standard 17 columns

**Column G Specialization:** `Risk_Rating` (Dropdown: Critical, High, Medium, Low, Minimal)

**Extended Columns (R-X):**

| Column | Field Name | Width | Type | Validation |
|--------|-----------|-------|-----------|------------|
| **R** | Risk_Score_Trend | 18 | Dropdown | Improving, Stable, Degrading, Unknown |
| **S** | Security_Incidents_YTD | 20 | Integer | ≥0 |
| **T** | Cert_Expiry_Tracked | 18 | Dropdown | Yes, No, N/A |
| **U** | Next_Cert_Expiry | 16 | Date | - |
| **V** | Financial_Health | 18 | Dropdown | Strong, Stable, Concerning, Unknown |
| **W** | Last_Assessment_Date | 18 | Date | - |
| **X** | Reassessment_Trigger_Met | 20 | Dropdown | Yes, No |

### Compliance Checklist (15 items)

```
☐ Vendor risk assessment performed at onboarding
☐ Annual vendor risk reassessment scheduled
☐ Risk scoring methodology documented and consistent
☐ Security certifications tracked (ISO 27001, SOC 2, etc.)
☐ Certification expiry dates monitored with alerts
☐ Vendor security incidents monitored via news/feeds
☐ Vendor breach notification process documented
☐ Financial health indicators monitored for critical vendors
☐ Vendor concentration risk assessed
☐ Sub-processor changes tracked and assessed
☐ Geopolitical risk factors considered
☐ Vendor security questionnaire refreshed periodically
☐ Risk rating changes trigger stakeholder notification
☐ High-risk vendors subject to enhanced monitoring
☐ Vendor risk dashboard available to stakeholders
```

---

# SECTION 3: SHEETS 7-9 (ANNUAL REVIEWS + DASHBOARD)

## Sheet 7: Exit Strategy Annual Review & PoC Testing (NEW v2.1)

### Purpose & Layout

**Sheet Name:** `7. Exit Strategy Review`

**Purpose:** Annual review of exit strategies + Proof-of-Concept (PoC) testing per DORA Article 28.6.

**Regulatory Driver:** DORA Article 28.6 requires financial institutions to annually review and test exit strategies for ICT services.

**Policy Reference:** ISMS-POL-A.5.19-23-S5, Section 8 (Exit Strategy)

**Assessment Question:** "Is the exit strategy reviewed annually with PoC testing demonstrating feasibility?"

### Column Structure (A-N, 14 columns)

| Column | Field Name | Width | Type | Validation | Description |
|--------|-----------|-------|-----------|------------|-------------|
| **A** | Review_ID | 14 | Formula | - | `=CONCATENATE("EXIT-",TEXT(ROW()-4,"000"))` |
| **B** | Cloud_Service_Name | 28 | Text | - | Service name |
| **C** | Vendor_Name | 22 | Text | - | Vendor/provider |
| **D** | Exit_Strategy_Documented | 20 | Dropdown | Yes, No, Partial | Exit plan exists? |
| **E** | Last_Annual_Review_Date | 18 | Date | - | Last review date |
| **F** | Next_Review_Due | 18 | Date | Formula: `=E5+365` | Next annual review |
| **G** | Review_Outcome | 16 | Dropdown | Adequate, Needs Update, Critical Gaps | Review result |
| **H** | PoC_Test_Conducted | 18 | Dropdown | Yes, No, Planned | PoC test done? |
| **I** | PoC_Test_Date | 16 | Date | - | When PoC tested |
| **J** | PoC_Test_Result | 16 | Dropdown | Successful, Partial, Failed, Not Tested | PoC outcome |
| **K** | Data_Portability_Verified | 20 | Dropdown | Yes, No, Partial | Can export data? |
| **L** | Alternative_Provider_Identified | 22 | Dropdown | Yes, No, In Progress | Backup vendor? |
| **M** | Responsible_Team | 20 | Dropdown | IT Operations, Cloud Ops, Business Continuity | Who owns exit plan |
| **N** | Next_PoC_Test_Due | 18 | Date | Formula: `=I5+365` | Next PoC test |

### Compliance Checklist (12 items - DORA-specific)

```
☐ Exit strategy documented for all cloud services (DORA Art. 28.6)
☐ Exit plan includes data extraction procedures
☐ Exit plan includes service migration steps
☐ Exit plan includes contract termination process
☐ Annual review conducted by business and technical teams
☐ Proof-of-Concept (PoC) test conducted annually
☐ PoC test validates data portability (complete extraction)
☐ PoC test validates alternative provider feasibility
☐ PoC test results documented with evidence
☐ PoC failures documented with remediation plan
☐ Exit strategy reviewed after vendor M&A or major changes
☐ Exit readiness status reported to senior management/board
```

### Example Data Row

**Row 5 (Example - Salesforce CRM):**

| Col | Value | Notes |
|-----|-------|-------|
| A | EXIT-001 | Auto-generated |
| B | Salesforce Sales Cloud | Service name |
| C | Salesforce Inc. | Vendor |
| D | Yes | Exit strategy documented |
| E | 01.02.2026 | Last annual review |
| F | 01.02.2027 | Next review due |
| G | Adequate | Review outcome |
| H | Yes | PoC test conducted |
| I | 15.02.2026 | PoC test date |
| J | Successful | PoC test result (full data export via API successful) |
| K | Yes | Data portability verified (CRM data exported to CSV) |
| L | Yes | Alternative provider identified (HubSpot, Dynamics 365) |
| M | Business Continuity | Responsible team |
| N | 15.02.2027 | Next PoC test due |

---

## Sheet 8: Jurisdictional Risk Assessment (CLOUD Act)

### Purpose & Layout

**Sheet Name:** `8. Jurisdictional Risk`

**Purpose:** Assess CLOUD Act exposure for US-headquartered cloud providers and cross-border data access risks.

**Regulatory Driver:** US CLOUD Act allows US government to compel US companies to produce data stored anywhere.

**Policy Reference:** ISMS-POL-A.5.19-23-S5, Section 7 (Data Sovereignty & Jurisdictional Risk)

**Assessment Question:** "For US-nexus providers, what is the jurisdictional risk and what mitigations are in place?"

### Column Structure (A-T, 20 columns)

| Column | Field Name | Width | Type | Validation | Description |
|--------|-----------|-------|-----------|------------|-------------|
| **A** | Assessment_ID | 14 | Formula | - | `=CONCATENATE("JUR-",TEXT(ROW()-4,"000"))` |
| **B** | Cloud_Service_Name | 28 | Text | - | Service name |
| **C** | Vendor_Name | 22 | Text | - | Vendor/provider |
| **D** | Provider_HQ_Jurisdiction | 20 | Dropdown | Switzerland, EU/EEA, UK, US, Other Adequate, Non-Adequate | Where HQ located |
| **E** | US_Parent_Company | 18 | Dropdown | Yes, No, Unknown | Is parent company US-based? |
| **F** | CLOUD_Act_Exposure | 18 | Dropdown | No Exposure, Potential (US HQ), Mitigated (EU Boundary), Mitigated (Encryption+Keys), Accepted Risk, Under Assessment | CLOUD Act risk |
| **G** | Data_Processing_Locations | 22 | Text | - | Where data stored/processed |
| **H** | EU_Data_Boundary_Available | 20 | Dropdown | Yes, No, Unknown | Vendor offers EU boundary? |
| **I** | EU_Data_Boundary_Enabled | 20 | Dropdown | Yes, No, N/A | Is EU boundary configured? |
| **J** | Customer_Managed_Keys | 18 | Dropdown | Yes, No, Partial | Customer controls encryption keys? |
| **K** | Legal_Challenge_Commitment | 20 | Dropdown | Yes, No, Unknown | Vendor commits to challenge requests? |
| **L** | Transfer_Mechanism | 18 | Dropdown | SCCs, BCRs, Adequacy Decision, None | Legal basis for data transfer |
| **M** | SCCs_In_DPA | 16 | Dropdown | Yes, No, N/A | SCCs included in DPA? |
| **N** | Residual_Risk_Level | 16 | Dropdown | Low, Medium, High, Critical | After mitigations, what's risk? |
| **O** | Risk_Owner | 18 | Dropdown | DPO, Legal, CISO, Business Unit | Who owns this risk? |
| **P** | Risk_Acceptance_Date | 18 | Date | - | When risk accepted |
| **Q** | Compensating_Controls | 30 | Text | - | Additional controls |
| **R** | Next_Review_Date | 18 | Date | Formula: `=P5+90` | Next quarterly review |
| **S** | Evidence_ID | 14 | Text | - | Link to evidence register |
| **T** | Notes | 35 | Text | - | Additional context |

### Applicability

**Complete this sheet ONLY IF:**

- Cloud provider has US nexus (HQ, subsidiary, or significant US operations)

**Examples of US-nexus providers:**

- Microsoft, AWS, Google Cloud, Oracle Cloud, Salesforce, Adobe, Snowflake, ServiceNow, Workday, Okta, Zoom, Slack, Box, Dropbox, etc.

**Skip this sheet if:**

- Provider is EU/EEA-only (OVH, Hetzner, IONOS)
- Provider is Swiss (Proton, Infomaniak)
- Provider is UK-only with no US parent

### Example Data Row

**Row 5 (Example - Microsoft 365 with EU Data Boundary):**

| Col | Value |
|-----|-------|
| A | JUR-001 |
| B | Microsoft 365 |
| C | Microsoft Corporation |
| D | US |
| E | Yes (Microsoft Corp is US-based) |
| F | Mitigated (EU Boundary) |
| G | EU Data Boundary: Germany, France, Netherlands |
| H | Yes |
| I | Yes (EU Data Boundary enabled for tenant) |
| J | Partial (Customer-managed keys for email, not SharePoint) |
| K | Yes (Microsoft committed to legal challenge in MS Cloud Act transparency report) |
| L | SCCs |
| M | Yes (EU SCCs in DPA) |
| N | Medium (residual risk due to CMK partial coverage) |
| O | DPO |
| P | 15.01.2026 |
| Q | Vendor commitment to legal challenge + Enhanced monitoring |
| R | 15.04.2026 |
| S | EV-GOV-045 |
| T | DPO reviewed, acceptable with compensating controls |

---

## Sheet 9: Summary Dashboard

### Purpose & Layout

**Sheet Name:** `9. Summary Dashboard`

**Purpose:** Auto-calculated compliance metrics, governance health score, jurisdictional risk summary, regulatory compliance status.

**Layout:** Read-only formulas, no user input (except references to other sheets).

### Dashboard Structure (3 Main Tables)

**TABLE 1: Governance Compliance Summary (Rows 4-10)**

| Assessment Area | Total Items | Compliant | Partial | Non-Compliant | N/A | Compliance % |
|-----------------|-------------|-----------|---------|---------------|-----|--------------|
| 2. Access Review | `=COUNTA('2. Access Review'!I5:I30)` | `=COUNTIF('2. Access Review'!I5:I30,CHECK&" Compliant")` | `=COUNTIF('2. Access Review'!I5:I30,WARNING&" Partial")` | `=COUNTIF('2. Access Review'!I5:I30,XMARK&" Non-Compliant")` | `=COUNTIF('2. Access Review'!I5:I30,"N/A")` | `=IF(B5>0,ROUND((C5/B5)*100,0),"N/A")` |
| 3. Change Mgmt | ... | ... | ... | ... | ... | ... |
| 4. Incident Mgmt | ... | ... | ... | ... | ... | ... |
| 5. Business Continuity | ... | ... | ... | ... | ... | ... |
| 6. Vendor Risk | ... | ... | ... | ... | ... | ... |
| **TOTAL** | `=SUM(B5:B9)` | `=SUM(C5:C9)` | `=SUM(D5:D9)` | `=SUM(E5:E9)` | `=SUM(F5:F9)` | `=ROUND(AVERAGE(G5:G9),0)` |

**TABLE 2: Key Governance Metrics (Rows 13-20)**

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| Total Cloud Services Assessed | `=COUNTA('2. Access Review'!B5:B30)` | - | Info |
| Services Requiring Remediation | `=COUNTIF('2. Access Review'!L5:L30,"Yes")` | 0 | `=IF(B14>0,"❌ Action","✅ OK")` |
| Overdue Access Reviews | `=COUNTIFS('2. Access Review'!R5:R30,"<"&TODAY()-90,'2. Access Review'!I5:I30,"<>N/A")` | 0 | `=IF(B15>0,"❌ Action","✅ OK")` |
| Open P1/P2 Incidents | `=COUNTIF('4. Incident Management'!G5:G30,"P1*")+COUNTIF('4. Incident Management'!G5:G30,"P2*")` | 0 | `=IF(B16>0,"⚠️ Review","✅ OK")` |
| BC Tests Overdue | `=COUNTIFS('5. Business Continuity'!R5:R30,"<"&TODAY()-365,'5. Business Continuity'!I5:I30,"<>N/A")` | 0 | `=IF(B17>0,"❌ Action","✅ OK")` |
| High-Risk Vendors | `=COUNTIF('6. Vendor Risk Monitoring'!G5:G30,"High")+COUNTIF('6. Vendor Risk Monitoring'!G5:G30,"Critical")` | <3 | `=IF(B18>3,"⚠️ Review","✅ OK")` |
| Exit Strategies Not Reviewed (Annual) | `=COUNTIFS('7. Exit Strategy Review'!E5:E30,"<"&TODAY()-365,'7. Exit Strategy Review'!D5:D30,"Yes")` | 0 | `=IF(B19>0,"❌ Action","✅ OK")` |
| Jurisdictional Risks (High/Critical) | `=COUNTIF('8. Jurisdictional Risk'!N5:N30,"High")+COUNTIF('8. Jurisdictional Risk'!N5:N30,"Critical")` | 0 | `=IF(B20>0,"⚠️ Review","✅ OK")` |

**TABLE 3: Regulatory Compliance Status (NEW - Rows 23-30)**

| Regulation | Metric | Value | Status |
|------------|--------|-------|--------|
| **DORA** | Exit Strategies Not PoC Tested (Annual) | `=COUNTIFS('7. Exit Strategy Review'!I5:I30,"<"&TODAY()-365,'7. Exit Strategy Review'!D5:D30,"Yes")` | `=IF(C24>0,"❌ Action","✅ OK")` |
| **DORA** | ICT Incidents Not Monitored | `=COUNTIF('4. Incident Management'!I5:I30,"❌ Non-Compliant")` | `=IF(C25>0,"❌ Action","✅ OK")` |
| **NIS2** | Significant Incidents (Require ≤24h notification) | `=COUNTIF('4. Incident Management'!G5:G30,"P1*")` | `=IF(C26>0,"⚠️ Review","✅ OK")` |
| **AI Act** | AI Systems Requiring Active Monitoring | `=COUNTIF('6. Vendor Risk Monitoring'!I5:I30,"<>N/A")` | Info |
| **CLOUD Act** | US-Nexus Providers (High/Critical Risk) | `=COUNTIF('8. Jurisdictional Risk'!N5:N30,"High")+COUNTIF('8. Jurisdictional Risk'!N5:N30,"Critical")` | `=IF(C28>0,"⚠️ Review","✅ OK")` |

### Overall Governance Health Score

**Row 33 (Weighted Score):**
```
OVERALL GOVERNANCE HEALTH SCORE: =ROUND(G10,0)%

Legend:
  ≥95%: ✅ Excellent
  80-94%: ⚠️ Good
  60-79%: ❌ Needs Improvement
  <60%: ❌ Critical - Immediate Action Required
```

---

# SECTION 4: SHEETS 10-11 + INTEGRATION

## Sheet 10: Evidence Register

### Purpose & Layout

**Sheet Name:** `10. Evidence Register`

**Purpose:** Centralized tracking of all governance evidence across all assessment sheets.

**Evidence ID Prefix:** `EV-GOV-###`

### Column Structure (A-M, 13 columns)

| Column | Field Name | Width | Type | Validation | Description |
|--------|-----------|-------|-----------|------------|-------------|
| **A** | Evidence_ID | 15 | Formula | - | `=CONCATENATE("EV-GOV-",TEXT(ROW()-4,"000"))` |
| **B** | Source_Sheet | 22 | Dropdown | 2. Access Review, 3. Change Mgmt, 4. Incident Mgmt, 5. Business Continuity, 6. Vendor Risk, 7. Exit Strategy, 8. Jurisdictional Risk | Which sheet is this evidence for? |
| **C** | Source_Row | 12 | Integer | 5-30 | Row number in source sheet |
| **D** | Service_Name | 28 | Text | - | Cloud service name |
| **E** | Governance_Item | 30 | Text | - | What governance activity is being evidenced |
| **F** | Evidence_Type | 22 | Dropdown | Access Review Report, Change Ticket, Incident Report, BC Test Result, Vendor Assessment, Exit Plan Document, PoC Test Results, DPO Opinion | Type of evidence |
| **G** | File_Location | 45 | Text | - | Full path or URL to evidence file |
| **H** | File_Format | 16 | Dropdown | PDF, DOCX, XLSX, CSV, PNG/JPG, Email (MSG/EML), ITSM Ticket | File type |
| **I** | Collection_Date | 16 | Date | - | When evidence collected |
| **J** | Collected_By | 20 | Text | - | Who collected evidence |
| **K** | Retention_Until | 16 | Date | Formula: `=I5+2555` | 7 years retention |
| **L** | Verification_Status | 20 | Dropdown | Verified, Pending, Invalid, Missing | Evidence quality status |
| **M** | Notes | 35 | Text | - | Additional context |

### Conditional Formatting

**Verification Status (Column L):**

- "Verified" → Green fill (C6EFCE)
- "Pending" → Yellow fill (FFEB9C)
- "Invalid" → Orange fill (FFC7CE)
- "Missing" → Red fill (FF0000), white text

### Data Rows

**Rows:** 5-124 (120 evidence entries capacity)

---

## Sheet 11: Approval Sign-Off

### Purpose & Layout

**Sheet Name:** `11. Approval Sign-Of`  *(Note: typo in sheet name matches Python generator)*

**Purpose:** 5-stage sequential approval workflow.

**Approval Stages:**
1. IT Operations Review (technical accuracy)
2. Compliance Officer Review (governance adequacy)
3. Data Protection Officer (DPO) Review
4. Chief Risk Officer (CRO) Review
5. CISO Approval (final authorization)

### Approval Workflow Structure

**Assessment Summary (Rows 4-12):**

- Document ID: ISMS-IMP-A.5.23.S4
- Assessment Period: [Input]
- Overall Compliance Rate: `='9. Summary Dashboard'!G10`
- Services Assessed: `='9. Summary Dashboard'!B13`
- Services Requiring Remediation: `='9. Summary Dashboard'!B14`
- Overdue Access Reviews: `='9. Summary Dashboard'!B15`
- Jurisdictional Risks Identified: `='9. Summary Dashboard'!B20`
- Exit Strategies Not Tested: `='9. Summary Dashboard'!B19` (NEW v2.1)
- Assessment Status: [Dropdown: Draft, Ready for Review, In Approval, Approved, Requires Remediation]

**Approval Sections (Rows 14+):**

**1. IT OPERATIONS REVIEW (Rows 14-22)**

- Reviewed By (IT Ops Manager): [Input]
- Review Date: [Date]
- Technical Accuracy: [Dropdown: Verified, Issues Found, Incomplete]
- Governance Activities Completed: [Dropdown: Yes, Partially, No]
- Evidence Adequate: [Dropdown: Yes, Partially, No]
- IT Ops Comments: [Long text]
- IT Ops Approval: [Dropdown: Approved, Approved with Conditions, Rejected]

**2. COMPLIANCE OFFICER REVIEW (Rows 24-32)**

- Reviewed By (Compliance Officer): [Input]
- Review Date: [Date]
- Governance Framework Compliance: [Dropdown: Compliant, Partially, Non-Compliant]
- Policy Alignment: [Dropdown: Yes, Needs Update, Gaps Identified]
- Remediation Plans Adequate: [Dropdown: Yes, No, N/A]
- Compliance Comments: [Long text]
- Compliance Approval: [Dropdown: Approved, Approved with Conditions, Rejected]

**3. DPO REVIEW (Rows 34-42)**

- Reviewed By (DPO): [Input]
- Review Date: [Date]
- Data Protection Compliance: [Dropdown: Compliant, Partially Compliant, Non-Compliant]
- Cross-Border Transfer Status: [Dropdown: Approved, Approved with SCCs, Requires TIA, Rejected]
- Jurisdictional Risk Acceptable: [Dropdown: Yes, With Mitigations, No]
- DPO Comments: [Long text]
- DPO Approval: [Dropdown: Approved, Approved with Conditions, Rejected]

**4. CRO REVIEW (Rows 44-52)**

- Reviewed By (CRO): [Input]
- Review Date: [Date]
- Enterprise Risk Acceptance: [Dropdown: Approved, Conditionally Approved, Rejected]
- Regulatory Risk Status: [Dropdown: Acceptable, Requires Mitigation, Unacceptable]
- Vendor Concentration Risk: [Dropdown: Acceptable, Requires Diversification, Critical]
- CRO Comments: [Long text]
- CRO Approval: [Dropdown: Approved, Approved with Conditions, Rejected]

**5. CISO APPROVAL (Rows 54-62)**

- Reviewed By (CISO): [Input]
- Review Date: [Date]
- Overall Security Posture: [Dropdown: Strong, Acceptable, Needs Improvement, Unacceptable]
- Cloud Governance Adequate: [Dropdown: Yes, With Improvements, No]
- Risk Appetite Alignment: [Dropdown: Yes, Partially, No]
- CISO Comments: [Long text]
- **FINAL DECISION**: [Dropdown: **Approved, Approved with Conditions, Rejected - Remediation Required, Deferred**]

**Next Review Details (Rows 64-68):**

- Next Review Date: `=B57+90` (90 days after CISO approval)
- Next Review Type: [Dropdown: Quarterly, Annual, Triggered]
- Review Owner: [Input]
- Calendar Invite Sent: [Dropdown: Yes, No]

---

## Integration Points

### Integration with Other ISMS Assessments

**Imports FROM:**

| Source | Data Element | Usage |
|--------|--------------|-------|
| IMP-A.5.23.1 (Inventory) | Cloud service list (Column B) | Populate service names in Sheets 2-6 |
| IMP-A.5.23.1 (Inventory) | Service criticality (Column F) | Determine governance frequency (Critical = quarterly, Low = annual) |
| IMP-A.5.23.2 (Vendor DD) | Vendor certifications | Inform vendor risk monitoring (Sheet 6) |
| IMP-A.5.23.3 (Secure Config) | Access control baseline | Reference for access reviews (Sheet 2) |

**Exports TO:**

| Target | Data Element | Usage |
|--------|--------------|-------|
| IMP-A.5.23.5 (Compliance) | Overall compliance % (Dashboard) | Executive compliance reporting |
| IMP-A.5.23.5 (Compliance) | Incident counts (Sheet 4) | Security incident trends |
| IMP-A.5.23.5 (Compliance) | High-risk vendors (Sheet 6) | Risk heatmap generation |
| IMP-A.5.23.5 (Compliance) | Exit strategy readiness (Sheet 7) | Exit planning dashboard |

### Integration with Organizational Systems

**CMDB (Configuration Management Database):**

- Export: Cloud service governance status → CMDB compliance field
- Import: Service owner changes → Update Sheet 2 responsible teams

**ITSM (IT Service Management):**

- Export: Non-compliant items → Auto-create ITSM remediation tickets
- Import: Change ticket IDs → Populate Sheet 3 change references
- Import: Incident ticket IDs → Populate Sheet 4 incident references

**Risk Management System:**

- Export: Vendor risk ratings (Sheet 6) → Enterprise risk register
- Export: Jurisdictional risks (Sheet 8) → Operational risk register
- Import: Risk IDs → Column N (Risk_ID) across all sheets

**IAM (Identity & Access Management):**

- Import: Access review reports → Evidence for Sheet 2
- Import: Admin account counts → Sheet 2 Column S

**Vendor Management Portal:**

- Import: Vendor cert expiry dates → Sheet 6 Column U
- Import: Vendor security incidents → Sheet 6 Column S
- Export: Vendor risk ratings → Vendor portal dashboards

---

## Quality Assurance Procedures

### Pre-Distribution QA Checklist

```
☐ Generator Script Validation
  ├─ Run generate_reg_a523_4_governance.py
  ├─ Verify 11 sheets created (correct names)
  ├─ Check all formulas calculate correctly (no #REF! errors)
  └─ Validate dropdown lists populated

☐ Data Validation Testing
  ├─ Test Status dropdown (✅ ⚠️ ❌ N/A) on each sheet
  ├─ Test sheet-specific dropdowns (Column G variations)
  ├─ Test date validations (no future dates allowed)
  └─ Test integer validations (no negative numbers)

☐ Formula Validation
  ├─ Sheet 2 Column X (Next_Review_Due = Last_Review + 90 days)
  ├─ Sheet 5 Column X (Next_Test_Due = Last_Test + 365 days)
  ├─ Sheet 7 Column F (Next_Review_Due = Last_Review + 365 days)
  ├─ Sheet 7 Column N (Next_PoC_Test = Last_PoC + 365 days)
  ├─ Sheet 8 Column R (Next_Review = Risk_Acceptance + 90 days)
  ├─ Sheet 9: ALL dashboard formulas (compliance %, metrics)
  └─ Sheet 10 Column K (Retention_Until = Collection + 2555 days)

☐ Dashboard Formula Testing
  ├─ Manually enter test data in Sheet 2
  ├─ Verify Dashboard Table 1 updates correctly
  ├─ Verify Dashboard Table 2 metrics calculate
  ├─ Verify Dashboard Table 3 regulatory metrics
  └─ Test with 0 entries (should show "N/A" not errors)

☐ Integration Testing
  ├─ Export sample data from IMP-5.23.1
  ├─ Import into IMP-5.23.4 Sheets 2-6 Column B
  ├─ Verify Dashboard consolidates data correctly
  ├─ Test CMDB/ITSM integration scripts (if automated)
  └─ Validate evidence register linkages

☐ Accessibility & Usability
  ├─ Column widths appropriate (no truncated headers)
  ├─ Row heights adequate (wrapped text visible)
  ├─ Print settings: Landscape, A4, fit-to-width
  ├─ Freeze panes: Row 5 frozen on assessment sheets
  ├─ Instructions sheet comprehensive and clear
  └─ Legend/help text accurate
```

### Post-Completion QA

**Before approval submission:**
```
☐ Completeness Check
  ├─ All 11 sheets populated (no empty sheets)
  ├─ All yellow input cells filled (no "[INPUT]" placeholders)
  ├─ All dropdowns selected (no empty validation cells)
  ├─ Evidence locations provided (Column J on all sheets)
  └─ Evidence register populated (Sheet 10)

☐ Accuracy Verification
  ├─ Spot-check 20% of "Compliant" entries (verify evidence)
  ├─ Verify Status-Evidence alignment (Compliant = evidence exists)
  ├─ Check remediation dates realistic (Column Q)
  ├─ Validate cross-sheet consistency (service names match)
  └─ Review Dashboard metrics (do they make sense?)

☐ Regulatory Compliance
  ├─ If DORA: Sheet 7 complete (exit strategy + PoC)
  ├─ If NIS2: Sheet 4 incidents classified correctly
  ├─ If AI Act: Sheet 6 AI monitoring documented
  ├─ If US vendors: Sheet 8 jurisdictional risk assessed
  └─ DPO/CRO approval sections complete (if applicable)

☐ Approval Readiness
  ├─ Self-assessment score ≥80/100 (Part I Section 7)
  ├─ All gaps documented with remediation plans
  ├─ Critical findings escalated to CISO
  ├─ Stakeholders pre-briefed (no surprises)
  └─ README.md created (for auditors)
```

---

## Workbook-Level Specifications

**File Naming Convention:**
```
ISMS-IMP-A.5.23.S4_Governance_YYYYMMDD.xlsx

Example: ISMS-IMP-A.5.23.S4_Governance_20260120.xlsx
```

**Metadata Properties (via `openpyxl.workbook.properties`):**
```python
wb.properties.title = "ISMS-IMP-A.5.23.S4 - Ongoing Governance & Risk Management"
wb.properties.subject = "ISO/IEC 27001:2022 Control A.5.23 Governance Assessment"
wb.properties.creator = "[Organization] ISMS Team"
wb.properties.description = "Quarterly governance assessment for cloud services (v2.1 with DORA exit strategy)"
wb.properties.keywords = "ISMS, ISO27001, A.5.23, Cloud, Governance, Risk, DORA, NIS2, CLOUD Act"
wb.properties.category = "Information Security Management"
wb.properties.version = "2.1"
```

**Sheet Protection:**

- **Protected Sheets:** 2-8 (assessment sheets), 9 (dashboard), 10 (evidence register)
- **Locked Cells:** Column A (Assessment_ID formulas), Dashboard formulas
- **Unlocked Cells:** All yellow input cells, Column J (Evidence_Location)
- **Allow:** Select unlocked cells, Select locked cells, Format cells

**Print Settings (All Assessment Sheets):**

- Page orientation: Landscape
- Paper size: A4
- Scaling: Fit to 1 page wide × auto tall
- Repeat rows: 1:4 (headers)
- Print gridlines: Yes
- Print quality: High

**Freeze Panes:**

- **Assessment Sheets (2-8):** Row 5 frozen (headers rows 1-4 visible when scrolling)
- **Dashboard (9):** Row 4 frozen (table headers visible)
- **Evidence Register (10):** Row 5 frozen
- **Approval (11):** No freeze

**Expected File Size:**

- Empty workbook: ~200-250 KB
- Fully populated: ~1.5-2.5 MB (depends on evidence volume)
- With images: Up to 10 MB (if screenshots embedded)

---

**END OF SECTION 4**

**END OF PART II: TECHNICAL SPECIFICATION**

---

**END OF SPECIFICATION**

---

*"Nature uses only the longest threads to weave her patterns, so that each small piece of her fabric reveals the organization of the entire tapestry."*
— Richard Feynman

<!-- QA_VERIFIED: 2026-01-31 -->
