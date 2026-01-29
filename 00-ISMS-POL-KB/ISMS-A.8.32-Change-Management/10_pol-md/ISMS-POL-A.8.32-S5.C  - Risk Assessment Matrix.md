# ISMS-POL-A.8.32-S5.C
## Risk Assessment Matrix

**Document ID**: ISMS-POL-A.8.32-S5.C  
**Title**: Change Management - Risk Assessment Matrix (Annex C)  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO / Change Manager | Initial risk matrix |

**Review Cycle**: Annual  
**Approvers**: CISO, Change Manager  
**Related Documents**: ISMS-POL-A.8.32-S2.1 (REQ-PROCESS-004), S2.2 (REQ-CLASSIFY-006, 007, 008)

---

## C.1 Purpose

This annex provides detailed methodology for assessing change risk based on impact and likelihood, determining appropriate approval authority, and identifying risk mitigation strategies.

---

## C.2 Impact Assessment

### C.2.1 Impact Level Definitions

**Impact measures the scope and severity of consequences if the change fails or causes issues.**

| Impact Level | Definition | Scope |
|--------------|------------|-------|
| **Low** | Minimal impact, easily reversible | Single user, single non-critical system, <15 min recovery |
| **Medium** | Moderate impact, rollback feasible | Team/multiple users, non-critical systems, <2 hour recovery |
| **High** | Significant impact, complex rollback | Department, major system, business process disruption, <8 hour recovery |
| **Critical** | Severe impact, difficult recovery | Organization-wide, mission-critical system, customer-facing, >8 hour recovery or irreversible |

### C.2.2 Impact Assessment Dimensions

Assess impact across multiple dimensions:

**Users Affected:**
- Low: <10 users
- Medium: 10-100 users
- High: 100-1000 users
- Critical: >1000 users or all users

**Business Processes:**
- Low: Optional/non-essential process
- Medium: Important but not critical process
- High: Critical business process with workarounds available
- Critical: Mission-critical process, no workarounds

**Financial Impact (if change fails):**
- Low: <$10K
- Medium: $10K-$100K
- High: $100K-$1M
- Critical: >$1M

**Regulatory/Compliance:**
- Low: No regulatory implications
- Medium: Compliance reporting affected
- High: Regulatory deadline risk
- Critical: Regulatory violation potential

**Reputation:**
- Low: Internal only, no external visibility
- Medium: Customer inconvenience, limited visibility
- High: Customer impact, public visibility
- Critical: Major customer impact, significant public visibility

**Recovery Complexity:**
- Low: Simple rollback, <15 minutes
- Medium: Standard rollback, <2 hours
- High: Complex rollback, multiple teams, <8 hours
- Critical: Very complex or irreversible

**Overall Impact:** Highest level across all dimensions (most conservative assessment).

### C.2.3 Impact Examples

**Low Impact Examples:**
- Add printer to individual workstation
- Update individual user's desktop software
- Change non-critical test environment configuration
- Update internal wiki documentation

**Medium Impact Examples:**
- Update department file server storage
- Modify team collaboration tool settings
- Upgrade non-critical application to new version
- Change network configuration in branch office

**High Impact Examples:**
- Upgrade production database to new major version
- Modify firewall rules affecting multiple departments
- Deploy new release of critical business application
- Migrate email system to new platform

**Critical Impact Examples:**
- Data center migration
- Core network infrastructure replacement
- Mission-critical application major version upgrade
- Customer-facing e-commerce platform changes
- Changes affecting patient safety (healthcare) or financial transactions (banking)

---

## C.3 Likelihood Assessment

### C.3.1 Likelihood Level Definitions

**Likelihood measures the probability that the change will fail, cause issues, or have unintended consequences.**

| Likelihood | Probability | Characteristics |
|------------|-------------|-----------------|
| **Low** | <10% failure risk | Simple change, well-tested, experienced team, stable environment, proven procedure |
| **Medium** | 10-30% failure risk | Moderate complexity, adequate testing, some unknowns, typical implementation |
| **High** | >30% failure risk | Complex change, many dependencies, limited testing, new technology, inexperienced team |

### C.3.2 Likelihood Assessment Factors

**Change Complexity:**
- Low: Single component, well-defined, straightforward
- Medium: Multiple components, moderate complexity
- High: Many components, complex interactions, many dependencies

**Testing Adequacy:**
- Low risk: Comprehensive testing in prod-like environment
- Medium risk: Standard testing, some scenarios untested
- High risk: Limited testing, environment doesn't match production

**Implementation Team Experience:**
- Low risk: Team highly experienced with this type of change
- Medium risk: Team has moderate experience
- High risk: Team new to this technology/process

**Environment Stability:**
- Low risk: Stable, mature environment
- Medium risk: Occasional issues, moderate maturity
- High risk: Unstable environment, frequent issues

**Change Frequency:**
- Low risk: Routine change, performed regularly
- Medium risk: Occasional change, some experience
- High risk: First-time or rare change

**Dependencies:**
- Low risk: Few or well-understood dependencies
- Medium risk: Multiple dependencies, mostly understood
- High risk: Many dependencies, some unknown

**Documentation Quality:**
- Low risk: Excellent documentation, detailed procedures
- Medium risk: Adequate documentation, some gaps
- High risk: Poor or missing documentation

**Vendor/Third-Party Involvement:**
- Low risk: Internal team only, full control
- Medium risk: Some vendor dependency, good relationship
- High risk: Heavy vendor dependency, new vendor

### C.3.3 Likelihood Examples

**Low Likelihood Examples:**
- Routine monthly security patches (established procedure)
- Standard workstation software installation from catalog
- Well-tested application update deployed 100+ times before
- Simple configuration change by experienced admin

**Medium Likelihood Examples:**
- Quarterly application upgrade (some risk of compatibility issues)
- Database schema change (tested but production data complex)
- Infrastructure change in moderately complex environment
- Change using new procedure (but experienced team)

**High Likelihood Examples:**
- First deployment of new major application version
- Complex infrastructure migration to new platform
- Change in environment with recent stability issues
- Implementation by vendor with limited knowledge of environment
- Urgent change without adequate testing time
- Change with many unknown dependencies

---

## C.4 Risk Matrix

### C.4.1 Risk Calculation

**Overall Risk = Impact × Likelihood**

| Impact ↓ / Likelihood → | Low | Medium | High |
|-------------------------|-----|--------|------|
| **Low** | Low | Low | Medium |
| **Medium** | Low | Medium | High |
| **High** | Medium | High | Critical |
| **Critical** | High | Critical | Critical |

### C.4.2 Risk Level Descriptions

**Low Risk:**
- Minimal oversight needed
- Standard approval process
- Basic documentation
- Minimal testing acceptable

**Medium Risk:**
- CAB review and approval
- Standard documentation
- Standard testing required
- Rollback plan required

**High Risk:**
- Enhanced CAB review with senior management
- Comprehensive documentation
- Comprehensive testing required
- Tested rollback plan required
- Communication plan required
- Phased deployment recommended

**Critical Risk:**
- Executive management approval
- Comprehensive risk assessment documented
- Extensive testing across all scenarios
- Tested rollback plan mandatory
- Comprehensive communication plan
- Phased deployment with rollback checkpoints
- 24/7 support during implementation
- Incident management team on standby

---

## C.5 Approval Authority by Risk Level

| Risk Level | Approval Authority | Additional Requirements |
|------------|-------------------|------------------------|
| **Low** | Change Manager or delegate | Basic change request, standard process |
| **Medium** | Change Advisory Board (CAB) | Impact assessment, testing evidence, rollback plan |
| **High** | CAB + Senior IT Management (CIO or IT Ops Manager) | Comprehensive assessment, extensive testing, detailed implementation plan |
| **Critical** | CAB + CISO + Executive Management | Executive briefing, comprehensive risk mitigation, go/no-go checkpoints |

---

## C.6 Risk Mitigation Strategies

### C.6.1 By Risk Level

**Low Risk:**
- Standard procedures
- Basic verification
- Minimal stakeholder notification

**Medium Risk:**
- Detailed implementation plan
- Standard testing
- Rollback plan
- Stakeholder notification
- Monitoring during implementation

**High Risk:**
- Comprehensive implementation plan
- Extensive testing including edge cases
- Tested rollback plan
- Phased deployment if feasible
- Enhanced monitoring
- Communication plan with regular updates
- Post-implementation review mandatory

**Critical Risk:**
- All high-risk mitigations PLUS:
- Pilot or canary deployment
- Go/no-go decision checkpoints
- Executive oversight
- Incident management team on standby
- 24/7 support coverage
- Immediate rollback capability
- Customer communication plan
- Business continuity plan review

### C.6.2 Specific Mitigation Techniques

**Phased Deployment:**
- Deploy to subset of users/systems first
- Validate success before full deployment
- Reduce blast radius of potential issues

**Canary Deployment:**
- Deploy to small percentage (e.g., 5%)
- Monitor for issues
- Gradually increase percentage

**Blue/Green Deployment:**
- Maintain two identical environments
- Deploy to inactive environment
- Switch traffic after validation
- Easy rollback by switching back

**Feature Flags:**
- Deploy code with features disabled
- Enable features gradually
- Disable instantly if issues

**Rollback Checkpoints:**
- Define specific points where rollback decision is made
- Go/no-go decision at each checkpoint
- Clear criteria for proceeding vs. rollback

---

## C.7 Risk Reassessment

**Risk assessment SHALL be updated if:**
- Change scope increases
- Additional systems affected
- Dependencies change
- Testing reveals higher complexity
- Implementation team changes
- Environmental factors change

**Reassessment triggers approval review:**
- If risk level increases, change may require higher approval authority
- Change Manager shall coordinate reassessment with CAB

---

## C.8 Risk Assessment Documentation

**All normal and emergency changes SHALL document:**
- Impact level with justification
- Likelihood level with justification
- Overall risk calculation
- Risk mitigation measures
- Approval authority determination

**Documentation template provided in: ISMS-POL-A.8.32-S5.B (Change Request Form), Section 5**

---

## C.9 Examples

**Example 1: Low Risk**
- Change: Install standard office software on 5 workstations
- Impact: Low (5 users, non-critical, easily reversible)
- Likelihood: Low (standard procedure, experienced team)
- Risk: Low
- Approval: Change Manager

**Example 2: Medium Risk**
- Change: Upgrade department file server to new version
- Impact: Medium (50 users, important but not critical)
- Likelihood: Medium (tested upgrade, some compatibility unknowns)
- Risk: Medium
- Approval: CAB

**Example 3: High Risk**
- Change: Migrate production database to new platform
- Impact: High (critical business system, complex rollback)
- Likelihood: Medium (tested but complex migration)
- Risk: High
- Approval: CAB + Senior IT Management

**Example 4: Critical Risk**
- Change: Replace core network infrastructure during business hours
- Impact: Critical (organization-wide, customer-facing, difficult recovery)
- Likelihood: Medium (complex change, adequate planning)
- Risk: Critical
- Approval: CAB + CISO + Executive Management

---

**END OF ANNEX C**

*"Risk assessment is not about eliminating risk—it's about understanding risk well enough to make informed decisions about accepting it."* ⚖️

*Feynman's principle applies: If you can't explain why a change is low/medium/high risk, you haven't done the risk assessment—you've just filled out a form.* 🎯
