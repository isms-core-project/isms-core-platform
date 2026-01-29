# ISMS-POL-A.8.32-S2.1
## Change Management - Change Process Requirements

**Document ID**: ISMS-POL-A.8.32-S2.1  
**Title**: Change Management - Change Process Requirements  
**Version**: 1.0  
**Date**: [Date] 
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date]| Change Manager / Information Security Manager | Initial requirements document |

**Review Cycle**: Annual (aligned with master policy review)  
**Next Review Date**: [Approval Date + 12 months]  
**Approvers**: 
- Primary: Change Manager
- Security Review: Chief Information Security Officer (CISO)
- Operational Review: IT Operations Manager

**Distribution**: Change Manager, CAB members, IT operations staff, system owners, implementers  
**Related Documents**: ISMS-POL-A.8.32 (Master), ISMS-POL-A.8.32-S2 (Requirements Overview)

---

## 2.1.1 Purpose

This document defines the core change management process requirements covering the complete change lifecycle from initiation through closure. These requirements implement ISO/IEC 27002:2022 Control 8.32 elements (a), (b), (c), (e), (g), (h), and (i).

**Scope of this section:**
- Change request submission and documentation
- Planning and impact assessment
- Authorization and approval workflows
- Communication to stakeholders
- Implementation execution
- Record keeping and audit trail
- Documentation updates
- Continuity plan updates
- Post-implementation review

---

## 2.1.2 Change Request Requirements

### REQ-PROCESS-001: Change Request Submission

**Requirement:**
All in-scope changes SHALL be submitted as formal change requests in the organization's change management system.

**Rationale:**
Formal change requests provide a single source of truth for change tracking, enable proper planning and assessment, create audit trail, and prevent undocumented "shadow changes".

**Implementation Guidance:**
Organizations should implement change management system (ITSM tool, ticketing system, or structured workflow) capable of:
- Creating change request records with unique identifiers
- Capturing required information per REQ-PROCESS-002
- Tracking change state through lifecycle
- Maintaining complete audit history
- Supporting approval workflows

**Assessment Criteria:**
- Change management system is documented in ISMS-IMP-A.8.32.1
- Sample change requests demonstrate required information captured
- Evidence shows no unauthorized changes (changes without tickets)

**Exceptions:**
Pre-approved standard changes may use simplified submission (e.g., self-service portal) but SHALL still create change request record.

---

### REQ-PROCESS-002: Minimum Change Request Information

**Requirement:**
Change requests SHALL include minimum required information:

a) **Change description:** Clear description of what will be changed  
b) **Business justification:** Why the change is needed  
c) **Affected systems/components:** Configuration items (CIs) impacted  
d) **Change category:** Standard / Normal / Emergency classification  
e) **Requester information:** Name, contact, organizational unit  
f) **Requested implementation date/time:** Preferred change window  
g) **Priority:** Based on business need and urgency  
h) **Initial risk assessment:** Preliminary impact and likelihood estimation

**Rationale:**
Insufficient information prevents proper impact assessment, risk evaluation, and informed decision-making.

**Implementation Guidance:**
Change management system should enforce required fields (mandatory fields in ticket form). Organizations may add additional fields based on their needs (e.g., cost estimate, resource requirements, dependencies).

Template provided in: ISMS-POL-A.8.32-S5.B (Change Request Form Template)

**Assessment Criteria:**
Sample change requests demonstrate completeness of information. Change management system configuration shows required field validation.

**Exceptions:**
Emergency changes may have abbreviated initial information but SHALL be completed retrospectively during post-implementation review.

---

## 2.1.3 Planning and Impact Assessment Requirements (ISO 27002 Element a)

### REQ-PROCESS-003: Impact Assessment

**Requirement:**
All normal and emergency changes SHALL undergo impact assessment addressing:

a) **Technical impact:** Systems, applications, infrastructure affected  
b) **Business impact:** Users, processes, services affected  
c) **Security impact:** Confidentiality, integrity, availability implications  
d) **Dependencies:** Other systems, services, or changes that may be affected or affect this change  
e) **Resource requirements:** Personnel, time, tools, licenses needed  
f) **Timing considerations:** Optimal change window, conflicts with other activities

**Rationale:**
Understanding full scope of impact prevents unintended consequences, identifies risks, and enables informed decision-making.

**Implementation Guidance:**
Organizations should develop impact assessment templates or checklists. Configuration Management Database (CMDB) helps identify dependencies. Security team should be consulted for changes with potential security implications.

**Assessment Criteria:**
Change requests demonstrate documented impact assessment. High-risk changes show comprehensive analysis. Evidence of dependency analysis (e.g., CMDB queries, architecture diagrams).

**Exceptions:**
Standard changes have impact assessment completed once during standard change catalog approval. Individual instances do not require re-assessment unless change scope differs.

---

### REQ-PROCESS-004: Risk Assessment

**Requirement:**
All normal and emergency changes SHALL undergo risk assessment determining:

a) **Impact level:** Low / Medium / High / Critical (scope of consequences if change fails)  
b) **Likelihood level:** Low / Medium / High (probability of failure or issues)  
c) **Overall risk:** Calculated using risk matrix (Impact × Likelihood)  
d) **Risk mitigation:** Steps to reduce risk (testing, rollback plan, phased deployment)

**Rationale:**
Risk-based approach ensures change management rigor is proportional to risk. High-risk changes receive additional scrutiny; low-risk changes can be streamlined.

Risk matrix provided in: ISMS-POL-A.8.32-S5.C (Risk Assessment Matrix)

**Implementation Guidance:**
Organizations should use consistent risk matrix across all changes. Risk assessment should consider both likelihood of failure and impact if failure occurs. Risk level determines approval authority (see REQ-PROCESS-006).

**Assessment Criteria:**
Change requests demonstrate documented risk assessment using organization's risk matrix. Risk levels are consistent with approval authorities exercised.

**Exceptions:**
Standard changes are assigned risk level during catalog approval. Emergency changes receive accelerated risk assessment but SHALL still document risk level.

---

### REQ-PROCESS-005: Implementation Planning

**Requirement:**
Normal changes with Medium risk or higher SHALL have documented implementation plan including:

a) **Step-by-step procedure:** Detailed implementation steps  
b) **Timeline:** Start time, duration, key milestones  
c) **Personnel:** Who will implement, who will verify  
d) **Prerequisites:** What must be completed before implementation  
e) **Verification steps:** How to confirm success  
f) **Rollback plan:** How to revert if problems occur (see REQ-VALIDATION-005)

**Rationale:**
Detailed implementation plans reduce errors, enable effective communication, and provide clear guidance to implementers.

**Implementation Guidance:**
Implementation plans may be documented in change ticket, attached documents, or runbooks. Complexity of plan should be proportional to change complexity and risk.

**Assessment Criteria:**
Medium and high-risk change requests demonstrate documented implementation plans. Implementers confirm plans are followed during execution.

**Exceptions:**
Low-risk normal changes and standard changes may have simplified implementation guidance. Emergency changes may document plan during implementation but SHALL update documentation post-implementation.

---

## 2.1.4 Authorization Requirements (ISO 27002 Element b)

### REQ-PROCESS-006: Approval Authority

**Requirement:**
Changes SHALL be approved by authority level appropriate to change risk:

| Risk Level | Approval Authority |
|------------|-------------------|
| **Low** (Standard changes) | Change Manager or designee |
| **Medium** | Change Advisory Board (CAB) |
| **High** | CAB + Senior IT Management |
| **Critical** | CAB + CISO + Executive Management |
| **Emergency** | Emergency CAB (E-CAB) - see S2.4 |

**Rationale:**
Risk-based approval authority ensures appropriate oversight without creating bottlenecks for low-risk changes.

**Implementation Guidance:**
Organizations may adjust approval authority levels based on their risk tolerance and organizational structure. Authority levels SHALL be documented and consistently applied.

**Assessment Criteria:**
Change requests demonstrate approval by appropriate authority level based on documented risk. Evidence of approver authorization (e.g., CAB meeting minutes, approval workflows).

**Exceptions:**
None. Approval authority requirements apply to all changes including emergency changes (expedited approval process).

---

### REQ-PROCESS-007: Change Advisory Board (CAB)

**Requirement:**
Organizations SHALL establish Change Advisory Board (CAB) responsible for reviewing and approving normal changes (Medium risk and above).

**CAB composition SHOULD include:**
- Change Manager (chair)
- Technical representatives (infrastructure, applications, security)
- Business representatives (service owners)
- Other stakeholders as appropriate to change portfolio

**Rationale:**
CAB provides multi-perspective review ensuring changes consider technical feasibility, business impact, security implications, and operational considerations.

**Implementation Guidance:**
CAB should meet regularly (e.g., weekly) with additional meetings as needed. CAB membership may vary based on changes under review (core members + relevant stakeholders). Virtual meetings are acceptable if properly documented.

**Assessment Criteria:**
CAB charter or equivalent document defines membership and responsibilities. Meeting schedule documented. CAB meeting minutes demonstrate regular meetings and decision documentation.

**Exceptions:**
Small organizations may use simplified approval process (e.g., email approval from key stakeholders) if properly documented and auditable.

---

### REQ-PROCESS-008: Approval Documentation

**Requirement:**
Change approvals SHALL be documented with:

a) **Approver identity:** Who approved the change  
b) **Approval date/time:** When approval was granted  
c) **Approval conditions:** Any conditions or constraints attached to approval  
d) **Approval rationale:** Why change was approved (especially for high-risk changes)

**Rationale:**
Documented approvals provide audit trail, accountability, and justification for change decisions.

**Implementation Guidance:**
Change management system should capture approval information automatically. CAB meeting minutes should document approval decisions. Email approvals should be attached to change tickets.

**Assessment Criteria:**
Change tickets demonstrate clear approval documentation. CAB meeting minutes show approval decisions. Audit trail shows who approved what and when.

**Exceptions:**
None. Even emergency changes require documented approval (may be retrospective).

---

## 2.1.5 Communication Requirements (ISO 27002 Element c)

### REQ-PROCESS-009: Stakeholder Communication

**Requirement:**
Changes SHALL be communicated to affected stakeholders with sufficient advance notice:

**Communication SHALL include:**
a) **What is changing:** Clear description of the change  
b) **When change occurs:** Date, time, duration  
c) **Who is affected:** Users, systems, services impacted  
d) **Expected impact:** Service interruptions, functionality changes  
e) **Contact information:** Who to contact with questions or issues

**Communication timing:**
- Standard changes: Communication as needed (may be minimal)
- Normal changes: Minimum 48 hours advance notice (more for high-impact)
- Emergency changes: Communication as soon as feasible during implementation

**Rationale:**
Advance communication allows stakeholders to plan, reduces surprise, enables user preparation, and sets expectations for service availability.

**Implementation Guidance:**
Organizations should establish communication channels (email, service portal, chat, status page). Communication templates help ensure consistency. High-impact changes may require multiple communication touchpoints (announcement, reminder, implementation update, completion notice).

**Assessment Criteria:**
Evidence of stakeholder communication (sent emails, posted announcements, chat messages). Stakeholder surveys or feedback confirms adequate communication. Communication timing meets minimum requirements.

**Exceptions:**
Emergency changes may require shortened communication timeline but SHALL communicate during or immediately after implementation.

---

### REQ-PROCESS-010: Change Calendar

**Requirement:**
Organizations SHOULD maintain change calendar showing:
- Scheduled changes with implementation date/time
- Change conflicts (multiple changes to same system)
- Freeze periods (restricted change windows)
- Major business events (requiring change restrictions)

**Rationale:**
Change calendar provides visibility into planned changes, prevents change collisions, and enables coordination across teams.

**Implementation Guidance:**
Change calendar may be maintained in change management system, shared calendar platform, or specialized tool. Calendar should be accessible to all change stakeholders. Automated conflict detection is beneficial.

**Assessment Criteria:**
Change calendar exists and is actively maintained. Evidence of change conflict identification and resolution.

**Exceptions:**
Small organizations with few changes may use simplified tracking (e.g., spreadsheet).

---

## 2.1.6 Implementation Requirements (ISO 27002 Element e)

### REQ-PROCESS-011: Implementation Execution

**Requirement:**
Changes SHALL be implemented according to approved implementation plan including:

a) **Timing:** Implementation occurs during approved change window  
b) **Personnel:** Authorized and trained personnel perform implementation  
c) **Procedures:** Implementation follows documented procedure  
d) **Verification:** Success verification performed per plan  
e) **Documentation:** Implementation actions documented in change ticket

**Rationale:**
Disciplined implementation execution prevents errors, enables troubleshooting if issues occur, and creates audit trail.

**Implementation Guidance:**
Implementers should document implementation progress in change ticket (start time, completion time, issues encountered, actions taken). Screen captures or logs may be attached as evidence.

**Assessment Criteria:**
Change tickets show implementation documentation (start/end times, actions taken, results). Implementation occurs during approved change windows.

**Exceptions:**
Emergency changes may deviate from approved timing but SHALL document timing justification.

---

### REQ-PROCESS-012: Implementation Monitoring

**Requirement:**
During change implementation, systems SHALL be monitored for:
- Performance degradation
- Error messages or failures
- Security alerts
- User impact

**Rationale:**
Real-time monitoring enables early detection of issues, allows for rapid response, and supports rollback decisions.

**Implementation Guidance:**
Leverage existing monitoring tools (SIEM, APM, infrastructure monitoring). Key personnel should be available during implementation window. Communication channels should be established for issue reporting.

**Assessment Criteria:**
Evidence of monitoring during change implementation (monitoring dashboards, alerts reviewed, logs examined). Incident response procedures for change-related issues.

**Exceptions:**
Low-risk standard changes may have reduced monitoring if impacts are well-understood.

---

## 2.1.7 Record Keeping Requirements (ISO 27002 Element g)

### REQ-PROCESS-013: Change Records

**Requirement:**
Organizations SHALL maintain complete change records including:

a) **Change request information:** All required fields per REQ-PROCESS-002  
b) **Assessment documentation:** Impact assessment, risk assessment  
c) **Approval documentation:** Approvals with approver identity and timing  
d) **Communication records:** Stakeholder notifications  
e) **Implementation documentation:** Implementation steps, timing, results  
f) **Verification results:** Success verification, testing outcomes  
g) **Post-implementation review:** PIR outcomes and lessons learned  
h) **Change history:** All state transitions and updates

**Rationale:**
Complete change records provide audit trail, enable troubleshooting, support continuous improvement analysis, and demonstrate compliance.

**Implementation Guidance:**
Change management system should maintain all information automatically. Attachments (test results, approvals, evidence) should be linked to change tickets. Records should be immutable after change closure (prevent tampering).

**Assessment Criteria:**
Sample change tickets demonstrate completeness of information. Change management system provides audit history of changes to tickets. Records retention meets organizational/regulatory requirements.

**Exceptions:**
None. Record keeping is mandatory for all changes.

---

### REQ-PROCESS-014: Change Audit Trail

**Requirement:**
Change management system SHALL maintain audit trail recording:
- Who created/modified the change request
- What information was changed
- When changes occurred
- All state transitions (Requested → Scheduled → Implementing → Closed)

**Rationale:**
Audit trail provides accountability, prevents unauthorized modifications to change records, and enables forensic analysis if needed.

**Implementation Guidance:**
Modern ITSM tools typically provide audit trail functionality. Audit trail should be tamper-proof (write-only, no deletion allowed).

**Assessment Criteria:**
Change management system demonstrates audit trail capabilities. Sample change tickets show complete history of modifications.

**Exceptions:**
None. Audit trail is critical control.

---

### REQ-PROCESS-015: Change Records Retention

**Requirement:**
Change records SHALL be retained for minimum:
- Standard changes: 1 year
- Normal changes: 3 years
- Failed changes: 5 years (for incident analysis)
- Changes affecting compliance systems: Per regulatory requirements

**Rationale:**
Adequate retention supports audit requirements, enables trend analysis, and maintains organizational knowledge.

**Implementation Guidance:**
Retention policies should be automated in change management system. Closed change tickets may be archived but must remain accessible.

**Assessment Criteria:**
Retention policy documented. Historical change records available per retention requirements.

**Exceptions:**
Longer retention may be required by industry regulations (financial services, healthcare, etc.).

---

## 2.1.8 Documentation Update Requirements (ISO 27002 Element h)

### REQ-PROCESS-016: Operational Documentation Updates

**Requirement:**
Changes affecting operational procedures SHALL trigger updates to:

a) **System documentation:** Architecture diagrams, configuration documents  
b) **Operating procedures:** Runbooks, standard operating procedures (SOPs)  
c) **User documentation:** User guides, help documentation  
d) **Network diagrams:** Topology maps, IP address schemes  
e) **Configuration baselines:** Documented configurations for systems

**Cross-reference:** ISO/IEC 27001:2022 Control 5.37 (Documented Operating Procedures)

**Rationale:**
Current documentation enables operational effectiveness, troubleshooting, knowledge transfer, and onboarding. Outdated documentation leads to errors and knowledge loss.

**Implementation Guidance:**
Documentation updates should be part of change closure criteria (change cannot be closed until documentation is updated). Documentation repository should be easily accessible. Version control for documentation is strongly recommended.

**Assessment Criteria:**
Evidence that documentation is updated after changes (version history, updated documents). Sample changes demonstrate documentation update as part of closure checklist.

**Exceptions:**
Standard changes that don't materially change operating procedures may not require documentation updates.

---

## 2.1.9 Continuity Plan Update Requirements (ISO 27002 Element i)

### REQ-PROCESS-017: ICT Continuity Plan Updates

**Requirement:**
Changes affecting ICT continuity capabilities SHALL trigger review and update of:

a) **ICT continuity plans:** Disaster recovery plans, business continuity plans  
b) **Recovery procedures:** System recovery runbooks, failover procedures  
c) **Recovery time objectives (RTO):** If change affects recovery capabilities  
d) **Recovery point objectives (RPO):** If change affects backup/recovery  
e) **Contact information:** If change affects key personnel or vendors  
f) **Dependencies:** If change affects system dependencies documented in continuity plans

**Cross-reference:** ISO/IEC 27001:2022 Control 5.30 (ICT Readiness for Business Continuity)

**Rationale:**
ICT continuity plans must reflect current infrastructure and recovery procedures. Outdated continuity plans fail during actual disasters.

**Implementation Guidance:**
Business continuity coordinator should be involved in CAB review of infrastructure changes. Changes affecting critical systems should trigger mandatory continuity plan review. Annual testing of continuity plans helps identify outdated documentation.

**Assessment Criteria:**
Evidence that continuity plans are reviewed after infrastructure changes. Continuity plan version history shows updates after relevant changes.

**Exceptions:**
Changes with no continuity impact (e.g., non-critical system updates) do not require continuity plan updates.

---

## 2.1.10 Post-Implementation Review Requirements

### REQ-PROCESS-018: Post-Implementation Review (PIR)

**Requirement:**
All normal changes and emergency changes SHALL undergo Post-Implementation Review (PIR) including:

a) **Success verification:** Did change achieve intended objectives?  
b) **Issues encountered:** Problems during implementation, how resolved  
c) **Actual vs. planned:** Compare actual implementation to plan (timing, resources)  
d) **Stakeholder feedback:** Input from users, business owners, operations  
e) **Lessons learned:** What went well, what could be improved  
f) **Recommendations:** Process improvements, documentation needs, training needs

**PIR timing:**
- Normal changes: Within 5 business days of implementation
- Emergency changes: Within 2 business days of implementation (mandatory)

**Rationale:**
PIR enables continuous improvement, captures lessons while fresh, identifies training needs, and validates change success.

**Implementation Guidance:**
PIR may be brief for successful low-risk changes (checklist completion). High-risk changes or failed changes warrant more detailed PIR (formal review meeting). PIR findings should inform process improvements and future change planning.

**Assessment Criteria:**
Change tickets demonstrate PIR completion within required timeframe. PIR documentation shows thoughtful analysis. Evidence of process improvements based on PIR findings.

**Exceptions:**
Standard changes typically do not require individual PIR (standard change catalog reviewed periodically). However, failed standard changes SHALL undergo PIR to determine if change should remain in standard catalog.

---

### REQ-PROCESS-019: Failed Change Analysis

**Requirement:**
Failed changes (changes that were rolled back or caused incidents) SHALL undergo detailed root cause analysis including:

a) **Failure description:** What went wrong  
b) **Root cause:** Why failure occurred (technical, process, human factors)  
c) **Contributing factors:** Other factors that contributed to failure  
d) **Prevention measures:** How to prevent similar failures  
e) **Process improvements:** Changes to change management process  
f) **Training needs:** Knowledge gaps identified

**Rationale:**
Failed changes represent learning opportunities. Understanding failure patterns prevents recurrence and improves change management maturity.

**Implementation Guidance:**
Root cause analysis should involve all relevant stakeholders (implementer, approver, system owner, security team). Blameless post-mortems encourage honest analysis. Focus should be on system and process improvement, not individual blame.

**Assessment Criteria:**
Failed change records demonstrate thorough root cause analysis. Evidence of corrective actions implemented. Trend analysis shows reduced failure rate over time.

**Exceptions:**
None. Failed change analysis is critical for continuous improvement.

---

### REQ-PROCESS-020: Continuous Improvement

**Requirement:**
Organizations SHALL use change management metrics and PIR findings to continuously improve change management processes.

**Key metrics to track:**
- Change success rate (target: >95%)
- Emergency change percentage (target: <5%)
- Average change implementation time
- Failed change percentage (target: <5%)
- Changes with proper approvals (target: 100%)
- PIR completion rate (target: 100%)

**Improvement activities:**
- Quarterly review of change management metrics
- Annual comprehensive change management process review
- Update standard change catalog based on successful normal changes
- Update change procedures based on lessons learned
- Training programs based on identified knowledge gaps

**Rationale:**
Continuous improvement prevents change management from becoming stagnant bureaucracy. Data-driven improvement focuses efforts where most beneficial.

**Implementation Guidance:**
Change Manager owns continuous improvement program. ISMS-IMP-A.8.32.5 (Compliance Dashboard) supports metrics analysis. Improvement initiatives should be treated as changes (following change management process).

**Assessment Criteria:**
Evidence of regular metrics review. Documentation of process improvements over time. Metrics show improvement trends.

**Exceptions:**
None. Continuous improvement is core philosophy of this framework.

---

**END OF SECTION 2.1**

*"The thing that doesn't fit is the most interesting."  
— Richard Feynman*

*When a change fails, don't sweep it under the rug. That failure is your best teacher. Analyze it, learn from it, prevent it from happening again. That's real engineering.* 🔧