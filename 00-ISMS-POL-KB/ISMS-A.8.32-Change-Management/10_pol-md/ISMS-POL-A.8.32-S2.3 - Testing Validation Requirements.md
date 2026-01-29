# ISMS-POL-A.8.32-S2.3
## Change Management - Testing & Validation Requirements

**Document ID**: ISMS-POL-A.8.32-S2.3  
**Title**: Change Management - Testing & Validation Requirements  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Information Security Manager / IT Operations Manager | Initial requirements document |

**Review Cycle**: Annual  
**Next Review Date**: [Approval Date + 12 months]  
**Approvers**: CISO, IT Operations Manager, Change Manager  
**Distribution**: Development teams, QA teams, operations, system owners  
**Related Documents**: ISMS-POL-A.8.32-S2.1 (Change Process), Controls 8.29 (Security Testing), 8.31 (Environment Separation), 8.33 (Test Information)

---

## 2.3.1 Purpose

This document defines requirements for testing and validating changes before production deployment, including environment separation requirements and acceptance criteria. Implements ISO/IEC 27002:2022 Control 8.32 element (d) - Testing and Acceptance.

---

## 2.3.2 Environment Separation Requirements (Integration with Control 8.31)

### REQ-TESTING-001: Three-Environment Minimum

**Requirement:**
Organizations SHALL maintain separated environments for change development and testing:

**Development Environment (Dev):**
- Purpose: Code development, initial unit testing, experimentation
- Access: Developers, authorized development staff
- Data: NO production data (synthetic/anonymized test data only)
- Change control: Minimal (developers can make changes freely)

**Test/QA Environment (Test):**
- Purpose: Integration testing, QA testing, UAT, security testing
- Access: QA team, selected business users, security team
- Data: Production-like data (anonymized per Control 8.33)
- Change control: Controlled promotion from Dev

**Production Environment (Prod):**
- Purpose: Live operational systems serving business/customers
- Access: Strictly controlled, change-authorized personnel only
- Data: Real production data with full protection
- Change control: Full change management per this policy

**Optional: Staging/Pre-Production Environment**
Organizations MAY implement staging environment mirroring production for final validation.

**Cross-reference:** ISO/IEC 27001:2022 Control 8.31 (Separation of Development, Test, Production Environments)

**Rationale:**
Environment separation prevents unauthorized production changes, enables safe testing, protects production data confidentiality.

**Implementation Guidance:**
Separation may be logical (network segmentation, access controls) or physical (separate infrastructure). Cloud environments should use separate accounts/subscriptions per environment.

**Assessment Criteria:**
ISMS-IMP-A.8.32.3 documents environment architecture. Evidence of access controls preventing unauthorized cross-environment access. Network diagrams show separation.

---

### REQ-TESTING-002: Environment Access Controls

**Requirement:**
Access to each environment SHALL be controlled:

**Development:** 
- Developers have broad access for development activities
- NO access to production systems/data

**Test:**
- QA team, UAT participants have testing access
- Developers may have read-only access for troubleshooting
- NO production database connections

**Production:**
- Strict least privilege access
- Changes only via approved change management process
- All access logged and monitored

**Requirement:** Production database credentials SHALL NOT be stored in development or test environments.

**Rationale:**
Prevents accidental production modifications during development/testing. Protects production data confidentiality.

**Assessment Criteria:**
Access control matrices document who has what access to which environments. IAM configurations demonstrate enforcement. Audit logs verify no unauthorized access.

---

### REQ-TESTING-003: Production Data in Non-Production (Integration with Control 8.33)

**Requirement:**
Production data in test environments SHALL be:
- Anonymized (personally identifiable information removed/masked)
- Pseudonymized (real data replaced with realistic fake data)
- Synthesized (artificially generated test data)

**Production data SHALL NOT be used in development environments.**

**Specific protections required:**
- Personal data: Anonymize per FADP/GDPR requirements
- Financial data: Mask account numbers, amounts
- Health data: Remove/mask per applicable regulations
- Credentials: Never use production passwords in test

**Cross-reference:** ISO/IEC 27001:2022 Control 8.33 (Test Information)

**Rationale:**
Production data contains sensitive information requiring protection. Test data breaches have regulatory and reputational consequences.

**Implementation Guidance:**
Data masking tools, test data generation tools, or manual procedures for data sanitization. Document data protection procedures for test environments.

**Assessment Criteria:**
ISMS-IMP-A.8.32.3 documents test data protection procedures. Evidence of data masking/anonymization. Audit of test databases shows no unprotected production data.

---

## 2.3.3 Change Promotion Requirements

### REQ-TESTING-004: Promotion Workflow

**Requirement:**
Changes SHALL follow documented promotion workflow:

```
Development → Testing → Production
    ↓            ↓          ↓
Unit Tests   Integration   Production
  Pass       Tests Pass    Validation
              ↓
          Security Tests
            Pass
              ↓
           UAT Sign-Off
              ↓
         CAB Approval
```

**Mandatory gates:**
- **Dev → Test:** Unit tests pass, code review complete
- **Test → Prod:** Integration/UAT/security tests pass, CAB approval

**Emergency bypass:** Allowed only for emergency changes with documented justification and mandatory post-review.

**Rationale:**
Structured promotion ensures changes are validated before production deployment.

**Assessment Criteria:**
Change tickets demonstrate promotion workflow followed. Evidence of testing at each stage. No unauthorized direct-to-production changes.

---

### REQ-TESTING-005: Promotion Authorization

**Requirement:**
Environment promotions SHALL require authorization:

**Dev → Test:**
- Authorization by: Development team lead or designated authority
- Evidence: Code review approval, unit test results

**Test → Prod:**
- Authorization by: CAB (per change classification and risk level)
- Evidence: Test results, UAT sign-off, security test clearance

**Rationale:**
Authorization gates prevent premature or inadequately tested changes from reaching production.

**Assessment Criteria:**
Promotion records show required authorizations obtained. CI/CD pipelines enforce authorization gates.

---

## 2.3.4 Testing Requirements

### REQ-TESTING-006: Testing Types

**Requirement:**
Normal changes SHALL undergo appropriate testing based on change scope and risk:

**Unit Testing (Development environment):**
- Individual component testing
- Developer-performed
- Required for: All code changes

**Integration Testing (Test environment):**
- Component interaction testing
- QA-performed
- Required for: Medium+ risk changes

**User Acceptance Testing / UAT (Test environment):**
- Business validation
- Business user-performed
- Required for: Changes affecting user workflows

**Regression Testing (Test environment):**
- Verify no adverse impact on existing functionality
- QA-performed
- Required for: High+ risk changes

**Security Testing (Test environment):**
- Security vulnerability testing
- Security team-performed
- Required for: All changes (risk-based depth)
- Cross-reference: Control 8.29 (Security Testing in Development)

**Performance Testing (Test/Staging environment):**
- Load, stress, scalability testing
- Technical team-performed
- Required for: Infrastructure changes, high-volume applications

**Rationale:**
Comprehensive testing catches issues before production deployment. Testing type and depth should match change risk.

**Assessment Criteria:**
ISMS-IMP-A.8.32.4 documents testing procedures. Change tickets demonstrate appropriate testing performed. Test results documented and attached.

---

### REQ-TESTING-007: Security Testing Integration (Control 8.29)

**Requirement:**
All changes SHALL undergo security testing appropriate to change risk:

**Low risk:** Automated security scans (SAST, DAST, dependency checks)  
**Medium risk:** Automated scans + manual security review  
**High/Critical risk:** Comprehensive security testing + penetration testing where appropriate

**Security testing SHALL identify:**
- Introduced vulnerabilities
- Security control bypasses
- Data exposure risks
- Authentication/authorization issues

**Security team SHALL approve security test results before production promotion.**

**Cross-reference:** ISO/IEC 27001:2022 Control 8.29 (Security Testing in Development)

**Rationale:**
Changes can introduce security vulnerabilities. Security testing before production prevents exploitable weaknesses from reaching live systems.

**Implementation Guidance:**
Integrate security testing into CI/CD pipelines where possible. Security team defines testing requirements for each risk level.

**Assessment Criteria:**
Evidence of security testing for all changes. Security team sign-off documented. Identified vulnerabilities remediated before production deployment.

---

### REQ-TESTING-008: Test Documentation

**Requirement:**
Testing SHALL be documented including:
- Test plan (what will be tested, how, by whom)
- Test cases (specific tests to be executed)
- Test results (pass/fail, evidence, issues found)
- Test sign-off (who verified results, when)

**Test documentation SHALL be attached to change request.**

**Rationale:**
Documented testing provides evidence of due diligence, enables audit verification, supports troubleshooting if issues occur post-deployment.

**Assessment Criteria:**
Change tickets include test documentation. High-risk changes show comprehensive test evidence.

---

## 2.3.5 Acceptance Criteria Requirements

### REQ-TESTING-009: Acceptance Criteria Definition

**Requirement:**
Changes SHALL have defined acceptance criteria specifying:
- Success criteria (what "successful change" means)
- Performance criteria (acceptable performance metrics)
- Functional criteria (features work as intended)
- Security criteria (no security regressions)
- User criteria (user acceptance requirements)

**Acceptance criteria SHALL be defined before testing begins.**

**Rationale:**
Clear acceptance criteria prevent subjective "it looks good" assessments. Objective criteria enable consistent evaluation.

**Assessment Criteria:**
Change requests include defined acceptance criteria. Test results map to acceptance criteria.

---

### REQ-TESTING-010: UAT Sign-Off

**Requirement:**
Changes affecting business users SHALL obtain User Acceptance Testing (UAT) sign-off from:
- Business process owner
- Representative users
- Service owner

**UAT sign-off SHALL confirm:**
- Change meets business requirements
- Functionality works as expected
- User documentation is adequate
- Training needs identified

**Rationale:**
Business validation ensures changes deliver intended value and don't disrupt business operations.

**Assessment Criteria:**
Medium+ risk changes affecting users demonstrate UAT sign-off. Sign-off documented with approver names and dates.

---

## 2.3.6 Rollback Requirements

### REQ-TESTING-011: Rollback Procedure

**Requirement:**
All normal changes SHALL have documented rollback procedure specifying:
- How to revert change (step-by-step)
- Time required for rollback
- Data implications (data loss, data recovery needs)
- Rollback decision criteria (when to rollback)
- Rollback authorization (who can authorize rollback)

**Rollback procedures SHALL be tested where feasible.**

**Rationale:**
Rollback capability enables rapid recovery if change fails. Untested rollback procedures may fail when needed most.

**Implementation Guidance:**
Low-risk changes may have simple rollback (restore previous version). High-risk changes should test rollback in test environment. Database changes require special attention to data consistency.

**Assessment Criteria:**
Change requests include rollback procedures. High-risk changes show evidence of rollback testing. Failed changes demonstrate rollback executed successfully.

---

### REQ-TESTING-012: Rollback Decision Criteria

**Requirement:**
Changes SHALL define rollback triggers:
- Critical functionality not working
- Severe performance degradation
- Security vulnerability introduced
- Widespread user impact
- Data integrity issues

**Authority to authorize rollback:**
- Change Implementer: Can recommend rollback
- Change Manager or CAB: Authorizes rollback
- Incident Manager: Can authorize emergency rollback during incidents

**Rationale:**
Pre-defined rollback criteria enable faster decision-making during stressful situations.

**Assessment Criteria:**
Changes document rollback criteria. Failed changes demonstrate timely rollback decisions.

---

## 2.3.7 Production Validation Requirements

### REQ-TESTING-013: Production Validation Testing

**Requirement:**
After production deployment, changes SHALL undergo production validation testing (smoke testing) including:
- Core functionality verification
- Performance monitoring
- Error log review
- User feedback collection
- Security control verification

**Production validation SHALL be completed before change closure.**

**Rationale:**
Test environment validation doesn't guarantee production success. Production validation confirms change works in real environment.

**Implementation Guidance:**
Production validation should be brief but thorough. Monitor for configurable period (e.g., 24-48 hours) based on change risk. Automated monitoring alerts expedite issue detection.

**Assessment Criteria:**
Change tickets document production validation results. Monitoring dashboards show post-change health checks.

---

## 2.3.8 Documentation Updates Post-Testing

### REQ-TESTING-014: Documentation Updates

**Requirement:**
Successfully tested changes SHALL trigger documentation updates:
- System documentation (architecture, configurations)
- Operating procedures (runbooks, SOPs)
- User documentation (user guides, help docs)
- Training materials (if user-facing changes)

**Documentation SHALL be updated before change closure.**

**Cross-reference:** Control 5.37 (Documented Operating Procedures)

**Rationale:**
Current documentation enables operational effectiveness and knowledge transfer.

**Assessment Criteria:**
Change closure checklist includes documentation update verification. Document version history shows updates after changes.

---

## 2.3.9 Continuous Improvement

### REQ-TESTING-015: Testing Effectiveness Review

**Requirement:**
Change Manager SHALL review testing effectiveness quarterly:
- Failed changes: What testing would have caught the issue?
- Production incidents: Were test procedures adequate?
- Testing bypasses: Why were tests skipped? (address root cause)
- Test environment adequacy: Does test environment sufficiently mirror production?

**Metrics:**
- Percentage of changes with documented test results (target: 100%)
- Post-deployment defects (target: trend downward)
- Test environment availability (target: >95%)

**Rationale:**
Testing procedures should evolve based on lessons learned.

**Assessment Criteria:**
Quarterly testing effectiveness reviews documented. Test procedures updated based on findings.

---

**END OF SECTION 2.3**

*"Test it in test, not production. This should not be controversial."  
— Every operations engineer ever*

*If your test environment doesn't catch issues before production, you don't have a test environment—you have a second production environment with lower expectations.* 🧪
