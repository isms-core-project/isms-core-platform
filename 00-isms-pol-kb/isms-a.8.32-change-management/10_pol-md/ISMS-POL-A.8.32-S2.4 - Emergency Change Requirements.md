# ISMS-POL-A.8.32-S2.4
## Change Management - Emergency Change Requirements

**Document ID**: ISMS-POL-A.8.32-S2.4  
**Title**: Change Management - Emergency Change Requirements  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Change Manager / Information Security Manager | Initial requirements document |

**Review Cycle**: Annual  
**Next Review Date**: [Approval Date + 12 months]  
**Approvers**: CISO, Change Manager, IT Operations Manager  
**Distribution**: E-CAB members, incident response team, IT operations, system owners  
**Related Documents**: ISMS-POL-A.8.32-S2.1 (Change Process), S2.2 (Change Classification)

---

## 2.4.1 Purpose

This document defines requirements for emergency changes—urgent modifications required to resolve critical incidents, security vulnerabilities, or business disruptions. Implements ISO/IEC 27002:2022 Control 8.32 element (f) - Emergency Change Procedures and Contingency.

**Critical principle:** Emergency classification is NOT an excuse to bypass change management—it's an alternate path with different timelines but equivalent controls.

---

## 2.4.2 Emergency Change Criteria

### REQ-EMERGENCY-001: Emergency Change Definition

**Requirement:**
Emergency changes are changes that meet ALL of the following criteria:

**a) Urgency:** Immediate action required (cannot wait for normal CAB cycle)

**b) Critical justification (at least ONE of):**
- Resolving critical incident causing business disruption
- Fixing security vulnerability under active exploitation
- Preventing imminent system failure
- Restoring critical business functionality
- Addressing regulatory compliance deadline (with documented justification)

**c) Risk acceptance:** Accelerated process accepted due to greater risk of inaction

**"Urgent" is NOT sufficient for emergency classification.** Business pressure, deadlines, or poor planning do NOT justify emergency classification.

**Rationale:**
Emergency classification grants expedited approval but carries risk. Criteria prevent abuse of emergency process.

**Implementation Guidance:**
When requesters claim "emergency," Change Manager verifies against criteria. False emergencies are rejected (convert to normal change with expedited scheduling if truly urgent).

**Assessment Criteria:**
Emergency change tickets demonstrate clear justification against criteria. Evidence shows emergency classification is not abused (target: <5% of all changes).

---

### REQ-EMERGENCY-002: Emergency vs. Urgent Clarification

**Requirement:**
Organizations SHALL distinguish "Emergency" from "Urgent":

**Emergency Change:** Meets REQ-EMERGENCY-001 criteria, follows emergency process  
**Urgent Normal Change:** Important but can follow normal process with expedited CAB review (special CAB meeting called if needed)

**Examples:**
- ❌ "CEO wants feature launched tomorrow" → Urgent normal change (poor planning)
- ✅ "Zero-day vulnerability under active exploitation" → Emergency change
- ❌ "We promised client by Friday" → Urgent normal change (business pressure)
- ✅ "Production database failure, data corruption imminent" → Emergency change
- ❌ "Marketing wants Black Friday updates live" → Urgent normal change (scheduled event)
- ✅ "Security breach, need to block attacker access" → Emergency change

**Rationale:**
Prevents "emergency fatigue" where everything becomes emergency, degrading process effectiveness.

**Assessment Criteria:**
Evidence that Change Manager challenges inappropriate emergency requests. Trend analysis shows consistent application of criteria.

---

## 2.4.3 Emergency CAB (E-CAB) Requirements

### REQ-EMERGENCY-003: E-CAB Composition

**Requirement:**
Organizations SHALL establish Emergency CAB (E-CAB) consisting of:

**Core members (must be available 24/7 via on-call rotation):**
- Change Manager or delegate
- Senior Technical Authority (infrastructure/applications as relevant)
- Information Security representative

**Additional members (called as needed):**
- System Owner
- Application Owner
- Business Representative
- CISO (for security-related emergencies)

**E-CAB members SHALL have authority to make immediate decisions without full CAB assembly.**

**Rationale:**
Smaller E-CAB enables faster decisions while maintaining oversight. 24/7 availability enables response to incidents occurring outside business hours.

**Implementation Guidance:**
E-CAB members should be documented with contact information. On-call schedules should be maintained. E-CAB authority levels should be clearly defined.

**Assessment Criteria:**
E-CAB membership documented. Evidence of 24/7 availability (on-call schedules). E-CAB decisions demonstrate appropriate authority exercised.

---

### REQ-EMERGENCY-004: E-CAB Approval Process

**Requirement:**
Emergency changes SHALL obtain E-CAB approval via:

**Real-time approval (preferred):**
- E-CAB members contacted immediately
- Emergency change discussed via conference call/chat
- Approval decision documented in real-time
- Minimum 2 E-CAB members approve (Change Manager + one technical/security authority)

**Retrospective approval (when real-time not feasible):**
- Change implementer proceeds with verbal approval from incident commander
- Full E-CAB approval obtained within 4 business hours
- Comprehensive justification documented
- Post-implementation review mandatory within 2 business days

**Rationale:**
Balance speed with oversight. Real-time approval prevents completely uncontrolled changes. Retrospective approval allows life-safety or critical security responses.

**Assessment Criteria:**
Emergency change tickets show E-CAB approval timestamp. Retrospective approvals demonstrate rapid follow-up documentation.

---

## 2.4.4 Emergency Change Process

### REQ-EMERGENCY-005: Abbreviated Change Request

**Requirement:**
Emergency changes SHALL create change request with minimum information:
- Emergency justification (why emergency classification applies)
- Critical business/security impact if not implemented
- Affected systems/components
- Implementation approach
- Rollback plan (even if abbreviated)
- Implementer and approver contact information

**Full change documentation SHALL be completed retrospectively within 24 hours of implementation.**

**Rationale:**
Minimum information enables informed decision while not delaying critical response. Retrospective completion ensures audit trail.

**Assessment Criteria:**
Emergency change tickets demonstrate initial minimum information captured. Full documentation completed within 24-hour timeframe.

---

### REQ-EMERGENCY-006: Accelerated Risk Assessment

**Requirement:**
Emergency changes SHALL undergo accelerated risk assessment considering:
- **Risk of action:** Potential issues from implementing change
- **Risk of inaction:** Consequences if change not implemented
- **Net risk:** Comparison justifying emergency action

**Risk assessment may be performed verbally during E-CAB review but SHALL be documented retrospectively.**

**Rationale:**
Even emergency changes need risk consideration. Risk of inaction often justifies accepting risk of action.

**Assessment Criteria:**
Emergency change tickets document risk assessment. Justification demonstrates reasoned decision-making.

---

### REQ-EMERGENCY-007: Testing Requirements for Emergencies

**Requirement:**
Emergency changes SHOULD undergo testing where feasible:

**When testing is feasible:**
- Test in development/test environment if time permits
- Use staging environment if available
- Perform limited production validation before full deployment

**When testing is not feasible:**
- Document justification for testing bypass
- Implement monitoring to detect issues rapidly
- Have rollback plan ready for immediate execution
- Document testing that WILL be performed post-implementation

**Testing requirements SHALL NOT delay critical security or life-safety responses.**

**Rationale:**
Test when possible, but don't let perfect be the enemy of good during emergencies.

**Assessment Criteria:**
Emergency changes show testing performed where feasible. Testing bypasses have documented justification.

---

### REQ-EMERGENCY-008: Emergency Communication

**Requirement:**
Emergency changes SHALL communicate to affected stakeholders:

**During implementation:**
- Incident updates (if emergency change is part of incident response)
- Status page updates
- Key stakeholder notifications

**After implementation:**
- Completion notice
- Impact summary
- Follow-up actions needed

**Communication timing:**
- Cannot delay critical response
- Communicate as soon as feasible during/after implementation

**Rationale:**
Stakeholders need awareness even if advance notice is not possible.

**Assessment Criteria:**
Evidence of stakeholder communication during/after emergency changes. Communication demonstrates urgency and impact.

---

## 2.4.5 Post-Implementation Review Requirements

### REQ-EMERGENCY-009: Mandatory Post-Implementation Review

**Requirement:**
ALL emergency changes SHALL undergo Post-Implementation Review (PIR) within 2 business days addressing:

**a) Emergency justification validation:**
- Was emergency classification appropriate?
- Could change have followed normal process?

**b) Implementation review:**
- Did change achieve objectives?
- Were there issues during implementation?
- Was rollback plan adequate?

**c) Process compliance:**
- Was E-CAB approval obtained?
- Was communication adequate?
- Was documentation completed?

**d) Lessons learned:**
- How to prevent similar emergencies?
- Process improvements needed?
- Training needs identified?

**e) Follow-up actions:**
- Permanent fix needed? (emergency change often temporary)
- Documentation updates required?
- Security review needed?

**PIR is MANDATORY. No exceptions.**

**Rationale:**
PIR prevents emergency process abuse, captures lessons, identifies improvements, and validates emergency response effectiveness.

**Implementation Guidance:**
Schedule PIR immediately after emergency change closure. Include E-CAB members, implementers, and system owners. Document findings in change ticket.

**Assessment Criteria:**
100% of emergency changes demonstrate PIR completion within 2 business days. PIR documentation shows thorough analysis.

---

### REQ-EMERGENCY-010: Emergency Pattern Analysis

**Requirement:**
Change Manager SHALL analyze emergency changes quarterly identifying:
- **Preventable emergencies:** Could proper planning have avoided emergency?
- **Recurring patterns:** Same systems repeatedly requiring emergency changes
- **Root causes:** Why are emergencies occurring?
- **Process improvements:** How to reduce emergency change frequency

**Goal:** Reduce emergency change ratio to <5% of total changes.

**Rationale:**
High emergency change rate indicates poor planning, inadequate monitoring, or systemic issues requiring correction.

**Implementation Guidance:**
Quarterly reports to CAB and management. Action plans to address root causes. Metrics tracking emergency change trends.

**Assessment Criteria:**
Quarterly emergency change analysis documented. Trends show decreasing emergency change ratio over time. Root causes addressed.

---

## 2.4.6 Emergency Change Constraints

### REQ-EMERGENCY-011: Prohibited Emergency Changes

**Requirement:**
The following changes SHALL NOT use emergency process regardless of urgency:

a) **Project deliverables:** Planned projects with deadline pressure  
b) **Scope expansion:** Adding features or capabilities beyond incident resolution  
c) **Deferred maintenance:** Routine maintenance postponed until urgent  
d) **Business convenience:** Changes for business convenience, not technical necessity  
e) **Repeated emergencies:** Third emergency change to same system within 30 days requires root cause analysis before proceeding

**Exception:** Life-safety or active security breach situations may override these constraints with CISO approval.

**Rationale:**
Emergency process exists for genuine emergencies, not poor planning or scope creep.

**Assessment Criteria:**
Change Manager demonstrates enforcement of prohibited emergency changes. Rejected emergency requests documented with rationale.

---

### REQ-EMERGENCY-012: Emergency Change Freeze Periods

**Requirement:**
During critical business periods (financial close, peak business season, audit periods), emergency changes SHALL:
- Require enhanced justification
- Require CISO approval (in addition to E-CAB)
- Be escalated to executive management if business-impacting

**Exception:** Security incidents and life-safety issues proceed regardless of freeze periods.

**Rationale:**
Emergency changes during critical periods carry amplified business risk and require enhanced oversight.

**Assessment Criteria:**
Critical business periods documented. Emergency changes during freeze periods demonstrate enhanced approval and justification.

---

## 2.4.7 Continuous Improvement

### REQ-EMERGENCY-013: Emergency Process Effectiveness

**Requirement:**
Organizations SHALL measure emergency change process effectiveness:

**Metrics:**
- Emergency change percentage (<5% target)
- Average emergency change resolution time
- Emergency changes requiring rollback
- Emergency changes validated as appropriate (vs. should have been normal)
- Post-implementation review completion rate (100% target)

**Review frequency:** Quarterly analysis with annual comprehensive review.

**Rationale:**
Emergency process should be effective when needed but not abused.

**Assessment Criteria:**
Quarterly emergency change metrics reviewed. Process improvements implemented based on findings.

---

**END OF SECTION 2.4**

*"An emergency on your part does not constitute an emergency on my part."  
— Unknown operations engineer*

*But when it's a real emergency—security breach, system failure, data at risk—that's when you discover if your change management process helps or hinders. Emergency procedures should enable rapid response while maintaining enough control to prevent making things worse.* 🚨

*Feynman's corollary: If everything is an emergency, nothing is an emergency.* 🎯
