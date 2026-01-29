# ISMS-POL-A.8.32-S2.2
## Change Management - Change Classification Requirements

**Document ID**: ISMS-POL-A.8.32-S2.2  
**Title**: Change Management - Change Classification Requirements  
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
**Approvers**: Change Manager, CISO, IT Operations Manager  
**Distribution**: CAB members, IT operations, system owners  
**Related Documents**: ISMS-POL-A.8.32-S2 (Requirements Overview), S2.1 (Change Process), S2.4 (Emergency Changes)

---

## 2.2.1 Purpose

This document defines requirements for classifying changes into three categories: Standard, Normal, and Emergency. Classification determines approval workflow, testing requirements, and documentation rigor.

---

## 2.2.2 Standard Change Requirements

### REQ-CLASSIFY-001: Standard Change Catalog

**Requirement:**
Organizations SHALL maintain Standard Change Catalog containing pre-approved, low-risk changes that:
- Have well-understood impacts and outcomes
- Follow documented, repeatable procedures
- Have low risk of failure
- Have defined rollback procedures (if needed)

**Standard Change Catalog SHALL include:**
a) Change description and scope
b) Pre-conditions and prerequisites
c) Step-by-step procedure
d) Estimated duration
e) Rollback procedure
f) Risk assessment (completed once during catalog approval)

**Rationale:**
Standard changes streamline low-risk activities, reduce CAB burden, enable faster implementation while maintaining control.

**Implementation Guidance:**
Standard Change Catalog should be reviewed quarterly and updated based on successful normal changes that become routine. Examples: password resets, standard software installations, certificate renewals, routine patches.

**Assessment Criteria:**
ISMS-IMP-A.8.32.2 documents Standard Change Catalog. Evidence shows catalog is actively used and maintained.

---

### REQ-CLASSIFY-002: Standard Change Execution

**Requirement:**
Standard changes SHALL:
- Be logged in change management system (no CAB approval required)
- Follow documented procedure from Standard Change Catalog
- Be executed by authorized personnel
- Include post-execution verification

Standard changes MAY be self-service where appropriate (e.g., password resets via approved portal).

**Rationale:**
Even pre-approved changes need tracking for audit trail and incident correlation.

**Assessment Criteria:**
Change tickets demonstrate standard changes are logged. Execution follows catalog procedures.

---

### REQ-CLASSIFY-003: Standard Change Review

**Requirement:**
Standard Change Catalog SHALL be reviewed:
- Quarterly: Verify changes remain appropriate for standard classification
- After failures: Any failed standard change triggers review of catalog entry
- Annually: Comprehensive catalog review

Changes that develop higher risk profiles SHALL be reclassified as normal changes.

**Rationale:**
Risk profiles change over time. Yesterday's routine change may be tomorrow's high-risk change.

**Assessment Criteria:**
Evidence of quarterly catalog reviews. Failed standard changes demonstrate catalog updates.

---

## 2.2.3 Normal Change Requirements

### REQ-CLASSIFY-004: Normal Change Definition

**Requirement:**
Normal changes are changes that:
- Are NOT in Standard Change Catalog
- Are NOT emergency situations
- Require CAB review and approval
- Have sufficient time for proper planning and testing

**Normal changes SHALL follow full change management process per S2.1.**

**Rationale:**
Normal changes represent majority of significant changes and warrant comprehensive review.

**Implementation Guidance:**
When in doubt whether change is standard or normal, classify as normal (safer).

**Assessment Criteria:**
Change tickets demonstrate appropriate classification. Normal changes show CAB approval.

---

### REQ-CLASSIFY-005: Normal Change CAB Review

**Requirement:**
Normal changes SHALL be reviewed by CAB addressing:
- Business justification
- Technical feasibility
- Risk assessment
- Resource availability
- Dependencies and conflicts
- Testing adequacy
- Rollback plan

**CAB decision options:**
- **Approve:** Change proceeds as planned
- **Approve with conditions:** Change approved with modifications or additional requirements
- **Defer:** More information or preparation needed
- **Reject:** Change not approved (with documented rationale)

**Rationale:**
Multi-perspective CAB review catches issues that individual requesters might miss.

**Assessment Criteria:**
CAB meeting minutes document review discussions and decisions. Change tickets reflect CAB decisions.

---

## 2.2.4 Risk-Based Categorization Requirements

### REQ-CLASSIFY-006: Impact Classification

**Requirement:**
All normal and emergency changes SHALL be assigned impact level:

| Impact Level | Scope of Consequences if Change Fails |
|--------------|--------------------------------------|
| **Low** | Single user/system, easily reversible, minimal business impact |
| **Medium** | Multiple users/team/non-critical system, moderate impact, rollback feasible |
| **High** | Department/major system, significant business impact, complex rollback |
| **Critical** | Organization-wide/critical system, severe business/security impact, difficult recovery |

**Rationale:**
Impact classification drives approval authority and change management rigor.

**Assessment Criteria:**
Change tickets demonstrate documented impact classification. High/critical changes show enhanced oversight.

---

### REQ-CLASSIFY-007: Likelihood Classification

**Requirement:**
All normal and emergency changes SHALL be assigned likelihood level:

| Likelihood | Probability of Failure or Issues |
|------------|--------------------------------|
| **Low** | Simple, well-tested, experienced team, stable environment |
| **Medium** | Moderate complexity, some unknowns, adequate testing |
| **High** | Complex, many dependencies, limited testing, new technology |

**Rationale:**
Likelihood combined with impact determines overall risk.

**Assessment Criteria:**
Change tickets demonstrate likelihood assessment with rationale.

---

### REQ-CLASSIFY-008: Risk Matrix

**Requirement:**
Overall change risk SHALL be calculated using Risk Matrix (Impact × Likelihood):

| Impact ↓ / Likelihood → | Low | Medium | High |
|-------------------------|-----|--------|------|
| **Low** | Low | Low | Medium |
| **Medium** | Low | Medium | High |
| **High** | Medium | High | Critical |
| **Critical** | High | Critical | Critical |

**Risk level determines approval authority:**
- **Low:** Change Manager
- **Medium:** CAB
- **High:** CAB + Senior IT Management
- **Critical:** CAB + CISO + Executive Management

*Detailed risk matrix: ISMS-POL-A.8.32-S5.C*

**Rationale:**
Risk-based approach ensures oversight is proportional to risk.

**Assessment Criteria:**
Change tickets show risk calculation. Approval authorities match risk levels.

---

## 2.2.5 Change Calendar and Scheduling Requirements

### REQ-CLASSIFY-009: Change Calendar Management

**Requirement:**
Organizations SHALL manage change calendar including:
- Scheduled change windows
- Change freeze periods
- Blackout windows (no changes except emergencies)
- Major business events requiring restricted changes

**Change conflicts SHALL be identified and resolved before approval.**

**Rationale:**
Change calendar prevents collisions, reduces risk of concurrent changes, aligns with business needs.

**Implementation Guidance:**
Freeze periods typically align with: financial close periods, peak business seasons, major releases, audit periods, holiday periods.

**Assessment Criteria:**
Change calendar documented in ISMS-IMP-A.8.32.2. Evidence of conflict identification and resolution.

---

### REQ-CLASSIFY-010: Change Scheduling Priorities

**Requirement:**
When multiple changes compete for same change window, prioritization SHALL consider:
- Business priority and urgency
- Risk level (higher risk gets dedicated window)
- Dependencies (prerequisite changes go first)
- Resource availability
- Service impact

**Change Manager has authority to prioritize and reschedule changes.**

**Rationale:**
Structured prioritization prevents chaotic scheduling and optimizes change windows.

**Assessment Criteria:**
Evidence of change prioritization decisions. Scheduling conflicts resolved before implementation.

---

## 2.2.6 Change Classification Boundaries

### REQ-CLASSIFY-011: Classification Edge Cases

**Requirement:**
When change classification is unclear:
- Default to higher classification (standard → normal, normal → emergency requires justification)
- Escalate to Change Manager for classification decision
- Document classification rationale in change ticket

**Common edge cases:**
- "Urgent" vs. "Emergency": Urgency alone doesn't justify emergency classification
- Standard change with modifications: Becomes normal change if deviating from catalog procedure
- Bundled changes: Classify at highest risk level of any component change

**Rationale:**
Conservative classification reduces risk of inadequate oversight.

**Assessment Criteria:**
Change Manager maintains log of classification decisions for edge cases. Patterns inform catalog updates.

---

## 2.2.7 Continuous Improvement

### REQ-CLASSIFY-012: Classification Effectiveness Review

**Requirement:**
Change Manager SHALL quarterly review:
- Failed standard changes (should they remain in catalog?)
- Successful normal changes (candidates for standard change catalog?)
- Emergency change patterns (can we prevent emergencies?)
- Classification accuracy (were changes appropriately classified?)

**Metrics to track:**
- Standard change success rate
- Normal changes that fail classification review
- Emergency changes that could have been normal changes

**Rationale:**
Classification system should evolve based on experience and changing risk landscape.

**Assessment Criteria:**
Quarterly review documentation. Standard Change Catalog updates based on reviews.

---

**END OF SECTION 2.2**

*Standard changes are pre-approved because they're boring and reliable. The moment a "standard" change becomes interesting, it's no longer standard.* 🎯
