# ISMS-REF-A.8.32 – Change Management Reference
## Implementation Tools & Templates (Non-ISMS Technical Reference)

---

## Document Control

| Field | Value |
|-------|-------|
| **Document Title** | Change Management Reference |
| **Document Type** | Internal - Technical Reference (Not ISMS) |
| **Document ID** | ISMS-REF-A.8.32 |
| **Document Creator** | Change Manager |
| **Document Owner** | Chief Information Security Officer (CISO) |
| **Approved By** | Change Manager (Technical Reference - No Executive Approval Required) |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Version Date** | [To Be Determined] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Change Manager / IT Operations | Initial technical reference for ISO 27001:2022 first certification |

**Review Cycle**: As needed (technology and tool evolution)  
**Next Review Date**: [Date + 12 months]  
**Approvers**: Change Manager / IT Operations Manager (technical reference, no ISMS approval required)

**Distribution**: Change Manager, CAB members, IT Operations, Change Implementers (for technical implementation awareness)

---

⚠️ **IMPORTANT – NON-ISMS TECHNICAL SUPPORT DOCUMENT**

This document is provided for informational and awareness purposes only.

- This document is NOT part of the Information Security Management System (ISMS).
- This document does NOT define mandatory change management controls or requirements.
- This document does NOT establish binding requirements, deadlines, KPIs, or SLAs.
- This document does NOT mandate the use, prohibition, or configuration of specific change management tools, vendors, or platforms.
- This document does NOT override or extend any ISMS policy.

All binding change management requirements, obligations, and governance decisions are defined exclusively in **ISMS-POL-A.8.32 (Change Management Policy)** and other approved ISMS documentation.

This document serves solely as a technical reference to:
- Describe change management tool capabilities and requirements
- Provide templates and forms for change management activities
- Track risk assessment methodologies and decision matrices
- Support change management implementation planning
- Provide quick reference guides for practitioners
- **This document must not be used as audit evidence of implementation**

Use of this document does not imply implementation, compliance, or operational maturity.

**Critical Positioning Statement**:
This document intentionally provides technical detail and implementation guidance beyond what is required for ISO/IEC 27001 policy documentation. Its purpose is technical awareness and practitioner support only. No auditor conclusions shall be drawn from the presence, absence, or classification of any tool, template, or methodology listed herein.

---

## 1. Document Purpose and Scope

### 1.1 Purpose

This document provides technical reference material for change management implementation, consolidating:

- Tool capability requirements (formerly ISMS-POL-A.8.32-S5.A)
- Change request form templates (formerly ISMS-POL-A.8.32-S5.B)
- Risk assessment methodology (formerly ISMS-POL-A.8.32-S5.C)
- Quick reference guide (formerly ISMS-POL-A.8.32-S5.D)

### 1.2 What This Document Is NOT

This document does NOT:
- Define [Organization]'s binding change management requirements (see ISMS-POL-A.8.32)
- Establish mandatory tool requirements
- Create compliance obligations or audit criteria
- Replace ISMS-POL-A.8.32 policy requirements
- Mandate specific tool selection or vendor relationships
- Establish approval workflows or authorities

### 1.3 Relationship to ISMS

This document is a **non-binding technical reference**. All change management requirements are defined exclusively in ISMS-POL-A.8.32 (Change Management Policy).

Implementation decisions are documented through ISMS-IMP-A.8.32 assessment workbooks based on risk assessment, operational context, and organizational requirements.

### 1.4 Content Organization

This reference organizes content into four sections:

1. **Section 2**: Tool Capability Requirements - Minimum capabilities for change management systems
2. **Section 3**: Change Request Form Template - Standard template ensuring consistent information capture
3. **Section 4**: Risk Assessment Methodology - Detailed impact/likelihood assessment and risk matrix
4. **Section 5**: Quick Reference Guide - One-page practitioner guide for common scenarios

---

## 2. Tool Capability Requirements

### 2.1 Purpose

Define minimum capabilities required from change management systems (ITSM tools, ticketing systems, workflow platforms). Organizations may use any system(s) meeting these capability requirements.

**Important:** This document specifies CAPABILITIES, not specific products or vendors.

### 2.2 Core Change Management Capabilities

#### CAP-001: Change Request Management

**Capability:** System SHALL enable creation and management of change requests.

**Requirements:**
- Create change requests with unique identifiers
- Capture all required fields per Section 3 (Form Template)
- Support rich text descriptions and file attachments
- Link related changes, incidents, problems
- Tag/categorize changes (by type, affected systems, priority)

**Assessment:** Can users submit complete change requests? Are all required fields captured?

---

#### CAP-002: Change State Management

**Capability:** System SHALL track change state through defined lifecycle.

**Required states (minimum):**
- Requested / Draft
- Assessing / Review
- Scheduled / Approved
- Implementing
- Review (PIR)
- Closed
- Rejected
- Cancelled

**Requirements:**
- State transitions tracked with timestamp and user
- State-based workflows (certain actions only available in certain states)
- State history visible in change record

---

#### CAP-003: Approval Workflow

**Capability:** System SHALL support configurable approval workflows.

**Requirements:**
- Multi-level approvals (Change Manager, CAB, E-CAB, Management)
- Role-based approval routing
- Approval notifications to approvers
- Approval deadline tracking
- Approval with comments/conditions
- Approval history with approver identity and timestamp
- Email integration for approval notifications

---

#### CAP-004: Change Calendar

**Capability:** System SHALL provide change calendar showing scheduled changes.

**Requirements:**
- Visual calendar view (daily, weekly, monthly)
- Highlight conflicts between changes
- Identify change freeze periods and blackout windows
- Filter by system, change type, risk level, team
- Export to iCalendar format

---

#### CAP-005: Reporting and Analytics

**Capability:** System SHALL provide reporting capabilities for metrics tracking.

**Required reports:**
- Change volume (by type, time period, risk level)
- Change success rate
- Emergency change percentage
- Average change duration
- Change-related incidents
- PIR completion rate
- Standard change utilization
- Trend analysis

---

#### CAP-006: Audit Trail

**Capability:** System SHALL maintain complete audit trail.

**Requirements:**
- All field changes logged (who, what, when)
- State transitions logged
- Approvals logged with timestamp
- System access logged
- Immutable audit log (cannot be altered after creation)
- Audit log retention aligned with policy requirements

---

#### CAP-007: Integration

**Capability:** System SHOULD integrate with related systems.

**Integration Points:**
- Configuration Management Database (CMDB) - link changes to CIs
- Incident Management - link changes to incidents
- Problem Management - link changes to problems
- Service Catalog - standard changes as catalog items
- Notification systems - email, Slack, MS Teams
- API availability for automation

---

### 2.3 Tool Evaluation Checklist

Organizations evaluating change management tools can use this checklist:

- [ ] CAP-001: Change request management capabilities present
- [ ] CAP-002: State management with lifecycle tracking
- [ ] CAP-003: Configurable approval workflows
- [ ] CAP-004: Change calendar with conflict detection
- [ ] CAP-005: Reporting and analytics capabilities
- [ ] CAP-006: Complete audit trail capabilities
- [ ] CAP-007: Integration capabilities with CMDB/Incident/Problem systems
- [ ] User-friendly interface for change requesters
- [ ] Mobile access capability
- [ ] Standard Change Catalog management
- [ ] Bulk change operations supported
- [ ] Role-based access control
- [ ] Customizable fields and workflows
- [ ] Multi-tenant support (if needed)
- [ ] Cloud-based or on-premises deployment (as per requirements)

---

## 3. Change Request Form Template

### 3.1 Purpose

Provide standard template for change requests ensuring consistent information capture. Use this template to configure ITSM tool forms or as standalone change request document.

### 3.2 Change Request Form

**Section 1: Basic Information**

- **Change Request ID:** [Auto-generated by system]
- **Submission Date:** [Auto-populated]
- **Requested by:** [Name, Email, Department]
- **Contact Phone:** [For implementation coordination]

**Section 2: Change Classification**

- **Change Type:** [Dropdown: Standard / Normal / Emergency]
- **If Standard Change - Standard Change Catalog Entry:** [Dropdown: Select from catalog]
- **If Emergency Change - Emergency Justification:** [Text: Why emergency classification applies]
- **Priority:** [Dropdown: Critical / High / Medium / Low]
- **Risk Level:** [Auto-calculated or manual: Critical / High / Medium / Low]

**Section 3: Change Description**

- **Change Title:** [Brief, descriptive title - 80 characters max]
- **Change Description:** [What is being changed? What is the scope? What are the specific modifications?]
- **Business Justification:** [Why is this change needed? Business driver, expected benefits, consequences if not implemented]

**Section 4: Impact Assessment**

- **Affected Systems/Components:** [List configuration items from CMDB]
- **Affected Users/Stakeholders:** [User groups, approximate number, geographic locations]
- **Service Impact:** [Dropdown: No Impact / Limited / Partial Outage / Full Outage]
- **Downtime Required:** [Yes / No] **If Yes, Duration:** [Estimated minutes/hours]

**Section 5: Risk Assessment**

- **Impact Level:** [Dropdown: Low / Medium / High / Critical] + Justification
- **Likelihood Level:** [Dropdown: Low / Medium / High] + Justification
- **Overall Risk:** [Auto-calculated from Impact × Likelihood matrix]
- **Risk Mitigation Measures:** [How will risks be reduced?]

**Section 6: Dependencies and Prerequisites**

- **Dependencies:** [Other changes, systems, or activities this change depends on]
- **Prerequisites:** [What must be completed before this change - technical, business, approval]
- **Conflicts:** [Any known conflicts with other changes or activities?]

**Section 7: Implementation Plan**

- **Proposed Implementation Date/Time:** [Date picker, Time picker - include timezone]
- **Implementation Window:** [Duration estimate]
- **Implementation Steps:** [High-level procedure numbered list]
- **Implementation Team:** [Lead Implementer, Additional Implementers, Verification Personnel]
- **Resource Requirements:** [Personnel, Tools/Software, Budget]

**Section 8: Testing and Validation**

- **Testing Environment:** [Where will change be tested?]
- **Testing Performed:** [Unit testing, Integration testing, Security testing, UAT - Y/N and results]
- **Test Results:** [Attach test documentation]
- **Acceptance Criteria:** [How will success be measured?]

**Section 9: Rollback Plan**

- **Rollback Procedure:** [Step-by-step rollback if change fails]
- **Rollback Duration:** [Time required to rollback]
- **Rollback Decision Criteria:** [When should rollback be initiated?]
- **Data Considerations:** [Will rollback cause data loss? How mitigated?]

**Section 10: Communication Plan**

- **Stakeholder Notification Required:** [Yes / No]
- **If Yes:** Who needs to be notified, notification method, timing, communication owner
- **User Communication:** [Will end users need advance notice?]

**Section 11: Documentation**

- **Documentation Updates Required:** [Yes / No]
- **If Yes:** System documentation, Operating procedures, User guides, Network diagrams, Other
- **Documentation Owner:** [Who will update documentation?]

**Section 12: Post-Implementation**

- **PIR Required:** [Auto-determined based on change type/risk]
- **Success Criteria:** [How will change success be measured?]
- **Monitoring Duration:** [How long will change be monitored post-implementation?]

---

## 4. Risk Assessment Methodology

### 4.1 Purpose

Provide detailed methodology for assessing change risk based on impact and likelihood, determining appropriate approval authority, and identifying risk mitigation strategies.

### 4.2 Impact Assessment

#### 4.2.1 Impact Level Definitions

| Impact Level | Definition | Scope |
|--------------|------------|-------|
| **Low** | Minimal impact, easily reversible | Single user, single non-critical system, <15 min recovery |
| **Medium** | Moderate impact, rollback feasible | Team/multiple users, non-critical systems, <2 hour recovery |
| **High** | Significant impact, complex rollback | Department, major system, business process disruption, <8 hour recovery |
| **Critical** | Severe impact, difficult recovery | Organization-wide, mission-critical system, customer-facing, >8 hour recovery or irreversible |

#### 4.2.2 Impact Assessment Dimensions

**Users Affected:** Low: <10 / Medium: 10-100 / High: 100-1000 / Critical: >1000

**Business Processes:** Low: Optional / Medium: Important / High: Critical with workarounds / Critical: Mission-critical

**Financial Impact:** Low: <$10K / Medium: $10K-$100K / High: $100K-$1M / Critical: >$1M

**Regulatory/Compliance:** Low: None / Medium: Reporting affected / High: Deadline risk / Critical: Violation potential

**Reputation:** Low: Internal only / Medium: Customer inconvenience / High: Public visibility / Critical: Major impact

**Recovery Complexity:** Low: <15 min / Medium: <2 hours / High: <8 hours / Critical: Very complex or irreversible

**Overall Impact:** Highest level across all dimensions (most conservative assessment)

### 4.3 Likelihood Assessment

#### 4.3.1 Likelihood Level Definitions

| Likelihood | Definition | Typical Success Rate |
|------------|------------|----------------------|
| **Low** | Highly unlikely to fail | >95% success |
| **Medium** | Moderate chance of issues | 75-95% success |
| **High** | Significant chance of issues | <75% success |

#### 4.3.2 Likelihood Assessment Factors

**Change Complexity:** Low: Simple / Medium: Moderate / High: Complex

**Environment Stability:** Low: Stable / Medium: Occasional issues / High: Frequent issues

**Team Experience:** Low: Experienced / Medium: Some experience / High: New procedure/team

**Testing Completeness:** Low: Extensively tested / Medium: Wel tested / High: Limited/Untested

**Dependencies:** Low: None / Medium: Few / High: Many complex dependencies

### 4.4 Risk Matrix

**Overall Risk = Impact × Likelihood**

| Impact ↓ / Likelihood → | Low | Medium | High |
|-------------------------|-----|--------|------|
| **Low** | Low | Low | Medium |
| **Medium** | Low | Medium | High |
| **High** | Medium | High | Critical |
| **Critical** | High | Critical | Critical |

### 4.5 Approval Authority by Risk Level

| Risk Level | Approval Authority | Additional Requirements |
|------------|-------------------|-------------------------|
| **Low** | Change Manager | Standard documentation |
| **Medium** | CAB | Standard documentation |
| **High** | CAB + Senior IT Management | Comprehensive documentation |
| **Critical** | CAB + CISO + Executive Management | Comprehensive documentation + Executive briefing |
| **Emergency** | E-CAB (IT Ops Manager + CISO) | Retrospective CAB review within 48 hours |

---

## 5. Quick Reference Guide

### 5.1 Change Type Decision Tree

**START HERE → Is this change needed?**

```
├─ Is change already in Standard Change Catalog?
│   ├─ YES → Standard Change
│   │        ▼
│   │   • Submit change request (self-service OK)
│   │   • No CAB approval needed
│   │   • Follow catalog procedure
│   │   • Log in change system
│   │
│   └─ NO → Continue...
│
├─ Is this an emergency situation?
│   ├─ YES → Does it meet ALL emergency criteria?
│   │        • Immediate action required?
│   │        • Critical incident/security/failure?
│   │        • Risk of inaction > risk of action?
│   │        ▼
│   │   ├─ YES → Emergency Change
│   │   │        • Contact E-CAB immediately
│   │   │        • Document justification
│   │   │        • Accelerated approval
│   │   │        • PIR mandatory within 2 days
│   │   │
│   │   └─ NO → Urgent Normal Change
│   │            • Call special CAB meeting
│   │            • Expedite but follow full process
│   │
│   └─ NO → Normal Change
│            ▼
│       • Submit change request
│       • Risk assessment
│       • CAB review
│       • Full process
```

### 5.2 Approval Authority Quick Reference

| Risk Level | Who Approves | Typical Timeline |
|------------|--------------|------------------|
| **Low** (Standard) | Change Manager | Immediate - 1 day |
| **Medium** (Normal) | CAB | Weekly CAB meeting |
| **High** (Normal) | CAB + Senior IT Mgmt | 1-2 weeks |
| **Critical** (Normal) | CAB + CISO + Exec Mgmt | 2-4 weeks |
| **Emergency** | E-CAB | <4 hours |

### 5.3 Required Information Checklist

**Every change request needs:**
- [ ] Clear description (what's changing?)
- [ ] Business justification (why?)
- [ ] Risk assessment (impact + likelihood)
- [ ] Systems affected (from CMDB)
- [ ] Implementation plan (step-by-step)
- [ ] Testing completed (or plan if emergency)
- [ ] Rollback plan (how to undo)
- [ ] Communication plan (who to notify)

### 5.4 Emergency Change Checklist

**Before declaring emergency:**
- [ ] Critical incident or security vulnerability?
- [ ] Immediate action required to prevent significant impact?
- [ ] Risk of NOT changing > risk of changing?
- [ ] No time for normal CAB review?

**If YES to all above → Emergency Change:**
1. Contact E-CAB (IT Ops Manager + CISO)
2. Document emergency justification
3. Get accelerated approval
4. Implement with monitoring
5. Conduct PIR within 48 hours
6. Present to CAB retrospectively

### 5.5 Key Contacts

**Change Manager:** [Name, Email, Phone]  
**CAB Chair:** [Name, Email, Phone]  
**E-CAB (Emergency):** [Names, Emails, Phones]  
**IT Operations Manager:** [Name, Email, Phone]  
**CISO:** [Name, Email, Phone]

**Escalation Path:**
1. Change Manager
2. IT Operations Manager
3. CISO
4. CIO

### 5.6 Common Mistakes to Avoid

1. ❌ **Submitting incomplete change requests** → Missing approvals delayed
2. ❌ **Skipping testing "because urgent"** → Production incidents
3. ❌ **No rollback plan** → Extended outages when change fails
4. ❌ **Forgetting to communicate** → Angry users and executives
5. ❌ **Misclassifying as emergency** → Process erosion
6. ❌ **No documentation updates** → Operational confusion
7. ❌ **Skipping PIR** → Lessons not learned, mistakes repeated
8. ❌ **Implementing without approval** → Compliance violation, career limiting

### 5.7 Success Tips

✅ **Start change request early** - Don't wait until last minute  
✅ **Be thorough in risk assessment** - Better safe than sorry  
✅ **Test in non-production first** - Catch issues before production  
✅ **Have rollback plan ready** - Hope for best, prepare for worst  
✅ **Communicate proactively** - Stakeholders appreciate advance notice  
✅ **Document everything** - Future you will thank present you  
✅ **Learn from failures** - PIR is for improvement, not blame

---

## 6. Tool Selection Guidance

### 6.1 Evaluating ITSM Platforms

**Key Criteria:**
- Meets minimum capability requirements (Section 2)
- User-friendly for change requesters
- Integration with existing tools (CMDB, ticketing)
- Reporting and analytics capabilities
- Total cost of ownership (licensing, maintenance, training)
- Vendor stability and support quality
- Cloud vs on-premises deployment model

**Popular ITSM Platforms** (examples, not recommendations):
- ServiceNow
- Jira Service Management
- BMC Remedy
- Cherwell
- Freshservice
- ManageEngine
- Open-source options (OTRS, iTop, osTicket)

### 6.2 Configuration Best Practices

**When configuring change management tools:**
1. Start with out-of-box workflows, customize only when necessary
2. Implement required fields to enforce completeness
3. Configure approval workflows based on risk matrix
4. Set up email notifications for all stakeholders
5. Configure change calendar with freeze periods
6. Enable integration with CMDB for accurate impact assessment
7. Set up dashboards for Change Manager and CAB
8. Configure report templates for required metrics
9. Train users before go-live
10. Plan for ongoing maintenance and updates

---

## Appendix: Form Templates

### A.1 Change Request Form (Blank)

[Complete blank form matching Section 3.2 structure]

### A.2 Emergency Change Justification Template

**Emergency Change Request**

- **Change ID:** ___________
- **Submitted by:** ___________
- **Date/Time:** ___________

**Emergency Criteria Met:**
- [ ] Critical incident requiring immediate resolution
- [ ] Security vulnerability requiring immediate patching
- [ ] System failure requiring immediate restoration
- [ ] Imminent system failure prevention
- [ ] Urgent regulatory requirement

**Situation Description:**
[Describe the critical situation requiring emergency change]

**Impact if NOT Implemented Immediately:**
[Describe consequences of delay]

**Risk if Implemented Without Full Testing:**
[Acknowledge risks of expedited implementation]

**Mitigation Measures:**
[Describe how risks will be minimized despite urgency]

**E-CAB Approval:**
- IT Operations Manager: ___________ Date: ___________
- CISO: ___________ Date: ___________

---

**END OF TECHNICAL REFERENCE**

---

*This technical reference supports implementation of ISMS-POL-A.8.32. All binding requirements are defined in the policy document.*