<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.15-16-18.S4-UG:framework:UG:a.5.15-16-18 -->
**ISMS-IMP-A.5.15-16-18.S4-UG - Role Definition & SoD Compliance Assessment**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.5.15: Access Control

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.15-16-18.S4-UG |
| **Version** | 1.0 |
| **Assessment Area** | Role-Based Access Control (RBAC) Maturity & Segregation of Duties (SoD) Compliance |
| **Related Policy** | ISMS-POL-A.5.15-16-18, Section 2.3 (Role Definition & RBAC - A.5.18), Section 2.1.4 (Segregation of Duties - A.5.15) |
| **Purpose** | Assess RBAC adoption, verify role-based access implementation, detect segregation of duties violations, and identify role governance gaps |
| **Target Audience** | IAM Team, Security Operations, Access Control Administrators, Internal Audit, Compliance Officers |
| **Assessment Type** | Operational & Compliance |
| **Review Cycle** | Quarterly (Critical Roles), Semi-Annual (All Roles), Annual (Comprehensive Role Governance Review) |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial specification for Role Definition & SoD Compliance assessment workbook | ISMS Implementation Team |

---

## Assessment Overview

### Purpose & Scope

This assessment evaluates Role-Based Access Control (RBAC) maturity and Segregation of Duties (SoD) compliance. It answers:

- **RBAC Maturity**: What percentage of users are assigned to roles vs. direct access grants?
- **Role Definition Quality**: Are roles well-defined, maintained, and accurately mapped to access?
- **SoD Compliance**: Are users assigned to conflicting role combinations?
- **Role Governance**: Are roles reviewed regularly and obsolete roles deactivated?

### Key Outputs

Upon completion, you will have:

1. ✅ Complete role catalog (30+ standard roles)
2. ✅ Role assignment data (all users mapped to roles or direct access)
3. ✅ RBAC maturity metrics (adoption rate, coverage, accuracy)
4. ✅ SoD matrix (defined conflicting role pairs)
5. ✅ SoD violation detection (users with conflicting roles)
6. ✅ Direct access justifications (exceptions to RBAC)
7. ✅ Role accuracy assessment (definitions match actual access)
8. ✅ Gap analysis (low RBAC adoption, unresolved SoD violations)
9. ✅ Evidence register (supporting documentation)
10. ✅ Three-level approval (Completer → IAM Lead → CISO)

---

##Prerequisites

### Information Required

1. **Role Documentation**:

   - Current role catalog (or work with HR/business units to create)
   - Role definitions (description, business owner, access rights)
   - Role hierarchy (if applicable)

2. **Role Assignment Data**:

   - Identity system exports (AD groups, Entra ID roles, Okta groups)
   - User-to-role mapping
   - Direct access users (no role assignments)

3. **SoD Matrix**:

   - Defined conflicting role pairs (or create with security team)
   - SoD exception approvals (CISO-approved violations)
   - SoD policy (ISMS-POL-A.5.15-16-18, Section 2.1.4)

4. **Supporting Data**:

   - User inventory (from ISMS-IMP-A.5.15-16-18.S1)
   - Access rights data (from ISMS-IMP-A.5.15-16-18.S2)
   - Access review results (from ISMS-IMP-A.5.15-16-18.S3)

### Time Commitment

- **Initial assessment**: 12-20 hours
- **Quarterly updates**: 3-5 hours
- **Annual comprehensive review**: 8-12 hours

---

## Workflow

### Assessment Flow

```
1. PREPARE (Gather role catalog, SoD matrix, assignment data)
   ↓
2. DOCUMENT ROLE CATALOG (Sheet 2)
   ↓
3. DOCUMENT ROLE ASSIGNMENTS (Sheet 3)
   ↓
4. IDENTIFY DIRECT ACCESS USERS (Sheet 4)
   ↓
5. DEFINE SOD MATRIX (Sheet 5)
   ↓
6. DETECT SOD VIOLATIONS (Sheet 6)
   ↓
7. CALCULATE RBAC METRICS (Sheet 7)
   ↓
8. ANALYZE GAPS (Sheet 8)
   ↓
9. REGISTER EVIDENCE (Sheet 9)
   ↓
10. REVIEW & APPROVE (Sheet 10)
```

### Phase 1: Preparation (2-4 hours)

**Steps**:
1. Read this guide
2. Review access control policy (ISMS-POL-A.5.15-16-18)
3. Locate/create role catalog
4. Identify/create SoD matrix
5. Gather role assignment data from identity systems
6. Schedule stakeholder meetings

**Deliverable**: Role catalog, SoD matrix, assignment data

### Phase 2: Role Catalog Documentation (3-5 hours)

**Steps**:
1. List all standard roles (30+ typical)
2. For each role:

   - Role name (job-based: Financial Analyst, HR Administrator)
   - Description (job function, responsibilities)
   - Business owner (department manager)
   - Systems included (ERP, CRM, file shares)
   - Access level summary (Read, Write, Admin per system)
   - Users assigned (count from identity system)
   - Last review date
   - Status (Active, Under Review, Obsolete)

3. Validate with role owners
4. Identify obsolete roles (zero users, outdated)

**Deliverable**: Complete Sheet 2 with all standard roles

**Quality Check**:

- ✓ All standard roles documented (30+ typical)
- ✓ Role descriptions clear and job-function based
- ✓ Business owners identified (not "IT Team")
- ✓ Systems and access levels documented
- ✓ Review dates recent (< 12 months)
- ✓ Obsolete roles flagged

### Phase 3: Role Assignment Documentation (2-4 hours)

**Steps**:
1. Export role/group assignments from identity systems:

   - AD: `Get-ADPrincipalGroupMembership`
   - Entra ID: Portal → Users → Group memberships
   - Okta: Admin → Users → Group assignments

2. Map users to roles
3. Document: User ID, Name, Role, Assignment Date, Approver, Expiration, Status
4. Cross-reference with user inventory
5. Identify users NOT in role catalog (direct access)

**Deliverable**: Complete Sheet 3 with all role assignments

**Quality Check**:

- ✓ All active users accounted for
- ✓ Role names match Sheet 2 catalog
- ✓ Assignment dates documented
- ✓ Approvers documented
- ✓ Expired roles flagged
- ✓ Cross-referenced with user inventory

### Phase 4: Direct Access User Identification (2-3 hours)

**Steps**:
1. Identify users WITHOUT role assignments
2. For each direct access user:

   - Systems accessed
   - Reason no role (unique job function, temporary, executive)
   - Business justification
   - Security/CISO approval
   - Review frequency (Quarterly recommended)
   - Last review date

3. Contact managers for justifications
4. Flag unauthorized direct access (gap)

**Deliverable**: Complete Sheet 4 with all direct access users

**Quality Check**:

- ✓ Every user accounted for (roles OR direct access)
- ✓ Business justifications documented
- ✓ Justifications legitimate (not "forgot to assign role")
- ✓ Approvals obtained (security/CISO)
- ✓ Quarterly review frequency
- ✓ Unauthorized direct access flagged

**Target**: Direct access < 20% of total users

### Phase 5: SoD Matrix Definition (2-4 hours)

**Steps**:
1. Review SoD policy (ISMS-POL-A.5.15-16-18, Section 2.1.4)
2. Identify conflicting role pairs:

   - Request + Approve (fraud risk)
   - Developer + Production Admin (error/fraud risk)
   - Finance + Payroll (fraud risk)
   - Expense Submitter + Expense Approver (fraud risk)
   - Procurement + Accounts Payable (fraud risk)

3. For each conflict:

   - Conflict ID, Role A, Role B
   - Conflict type (description)
   - Risk level (High, Medium, Low)
   - Mitigation (compensating controls)

4. Validate with security team and internal audit

**Deliverable**: Complete Sheet 5 with SoD matrix (6-12 conflicts typical)

**Quality Check**:

- ✓ All high-risk conflicts identified
- ✓ Conflict types clearly described
- ✓ Risk levels assigned
- ✓ Mitigation controls documented
- ✓ Validated by security team

### Phase 6: SoD Violation Detection (3-5 hours)

**Steps**:
1. Cross-reference role assignments (Sheet 3) against SoD matrix (Sheet 5):
   ```
   FOR EACH User:
     FOR EACH Conflict Pair in SoD Matrix:
       IF User has Role_A AND User has Role_B:
         FLAG as SoD Violation
   ```
2. For each violation:

   - Document user, conflicting roles, conflict type, risk level
   - Contact manager: Is violation justified?
   - **If justified**: Document reason, compensating controls, obtain CISO approval
   - **If not justified**: Create remediation plan (remove role, reassign duties)

3. Track remediation progress

**Deliverable**: Complete Sheet 6 with all SoD violations

**Quality Check**:

- ✓ All violations detected
- ✓ Each violation analyzed (justified or remediate)
- ✓ Justified violations have compensating controls
- ✓ Justified violations have CISO approval
- ✓ Unjustified violations have remediation plans
- ✓ High-risk violations prioritized (30 days)

**Target**: Zero unresolved SoD violations

### Phase 7: RBAC Metrics Calculation (1-2 hours)

**Steps**:
1. Calculate RBAC adoption metrics:

   - Total users
   - Users with roles
   - Users with direct access only
   - RBAC adoption rate = (Users with roles / Total users) × 100

2. Calculate role usage metrics:

   - Average roles per user
   - Active roles, Obsolete roles

3. Calculate SoD compliance metrics:

   - Violations detected, remediated, justified, unresolved
   - SoD compliance rate = ((Total users - Unresolved) / Total users) × 100

4. Calculate role review metrics:

   - Roles reviewed in last 12 months
   - Role review compliance %

5. Calculate overall RBAC maturity score:

   - = (RBAC Adoption × 40%) + ((100 - SoD %) × 30%) + (Role Review % × 20%) + (Direct Access Justification % × 10%)

**Deliverable**: Complete Sheet 7 with RBAC metrics

**Quality Check**:

- ✓ Metrics calculated accurately
- ✓ RBAC adoption >= 80% (target)
- ✓ SoD violations unresolved = 0 (target)
- ✓ Role review >= 95% (target)
- ✓ Maturity score >= 80 (Excellent), >= 60 (Good)

**Benchmark Maturity**:

- **90-100**: Excellent
- **80-89**: Very Good
- **70-79**: Good
- **60-69**: Fair
- **<60**: Poor

### Phase 8: Gap Analysis (2-3 hours)

**Steps**:
1. Identify gaps:

   - Low RBAC adoption (< 80%)
   - High direct access (> 20%)
   - Unauthorized direct access
   - Unresolved SoD violations
   - Outdated role definitions (> 12 months)
   - Obsolete roles not deactivated
   - Missing SoD exception approvals

2. For each gap:

   - Gap ID, Type, Severity (Critical/High/Medium/Low)
   - Description, Current State, Target State
   - Owner, Remediation Plan, Target Date, Status

3. Prioritize:

   - **Critical**: Unresolved SoD violations, unauthorized direct access
   - **High**: Low RBAC adoption, missing SoD approvals, outdated roles
   - **Medium**: Obsolete roles active, roles not reviewed annually
   - **Low**: Minor improvements

**Deliverable**: Complete Sheet 8 with prioritized gaps

**Quality Check**:

- ✓ All gaps identified
- ✓ Prioritized by risk
- ✓ Owners assigned
- ✓ Remediation plans specific (not vague)
- ✓ Target dates realistic (30/60/90 days)
- ✓ Critical gaps within 30 days

### Phase 9: Evidence Collection (2-3 hours)

**Steps**:
1. Collect evidence:

   - Role catalog documentation
   - Role assignment exports (AD, Entra ID, Okta)
   - SoD matrix documentation
   - SoD exception approvals (CISO sign-off)
   - Role review meeting minutes
   - Direct access justifications
   - RBAC metrics and trends

2. For each evidence item:

   - Evidence ID, Type, Description
   - Source, Date Collected
   - Storage Location, Retention Period (3 years)
   - Audit Relevance (A.5.15, A.5.18)

3. Organize by category
4. Verify accessibility

**Deliverable**: Complete Sheet 9 with evidence register

**Quality Check**:

- ✓ Evidence for all key findings
- ✓ Evidence recent (assessment period)
- ✓ Storage locations accessible
- ✓ Audit-ready format
- ✓ Retention period documented

### Phase 10: Review & Approval (1-2 hours)

**Steps**:
1. **Self-Review** (Assessment Completer):

   - Review all sheets for completeness
   - Verify formulas, conditional formatting
   - Run quality checklist
   - Document self-review

2. **IAM Team Lead Review**:

   - Verify role catalog accuracy
   - Validate role assignment data
   - Confirm SoD matrix completeness
   - Review SoD violation detection
   - Assess RBAC metrics
   - Approve or request revisions

3. **CISO Review & Approval**:

   - Review RBAC maturity score
   - Assess SoD compliance
   - Review critical gaps
   - Validate SoD exception approvals
   - Approve assessment
   - Schedule next review

**Deliverable**: Complete Sheet 10 with three-level approval

---

## Common Pitfalls & Solutions

### Pitfall 1: No Formal Role Catalog

**Problem**: "We don't have a formal role catalog. We just create AD groups as needed."

**Solution**:
1. Create role catalog DURING this assessment
2. Work with HR to identify job titles
3. Map job titles to access patterns
4. Document as formal roles
5. Assign business owners
6. Migrate AD groups to formal role structure

### Pitfall 2: Low RBAC Adoption (High Direct Access)

**Problem**: "80% of users have direct access instead of roles."

**Solution**:
1. Analyze direct access: What job functions?
2. Create standard roles for common job functions
3. Migrate direct access users to roles
4. Target: RBAC adoption >= 80%
5. Direct access = exception, not norm

### Pitfall 3: Ignoring SoD Violations

**Problem**: "We detected SoD violations but haven't remediated them."

**Solution**:
1. Prioritize unresolved violations (Critical)
2. **Option 1**: Remediate (remove role, reassign duties)
3. **Option 2**: Justify (business reason, compensating controls, CISO approval)
4. High-risk violations: 30 days
5. Target: Zero unresolved violations

### Pitfall 4: Obsolete Roles Not Deactivated

**Problem**: "We have 50 roles, but 15 have zero users."

**Solution**:
1. Identify obsolete roles (zero users, outdated)
2. Confirm with business owners
3. Change Status to "Obsolete", deactivate
4. Quarterly cleanup process

### Pitfall 5: Roles Not Reviewed Annually

**Problem**: "Roles defined 5 years ago, never reviewed."

**Solution**:
1. Schedule role review meetings
2. For each role: Still accurate? Appropriate access? Legitimate users?
3. Document review results
4. Update role definitions
5. Annual review cycle (Q4 every year)

### Pitfall 6: SoD Violations Without Compensating Controls

**Problem**: "5 SoD violations justified, but no compensating controls."

**Solution**:
1. Define compensating controls:

   - Enhanced logging (all transactions logged, reviewed monthly)
   - Dual approval (second person approves)
   - Manager review (quarterly)
   - Quarterly audit

2. Implement controls
3. Document implementation
4. CISO approval required

### Pitfall 7: Role-to-Access Mapping Inaccurate

**Problem**: "Role definitions say 'read access', but users have write access."

**Solution**:
1. Role accuracy assessment:

   - Compare role definition vs. actual access
   - Sample 10-20 users per role

2. Identify discrepancies:

   - Users have MORE access (privilege creep)
   - Users have LESS access (provisioning error)

3. Remediate: Remove excess or grant missing
4. Role-based provisioning (automated)
5. Quarterly validation

---

## Quality Checklist

### Preparation Phase

- [ ] All prerequisites gathered
- [ ] Access control policy reviewed
- [ ] Stakeholders scheduled
- [ ] User inventory available
- [ ] Working folder created

### Sheet 2: Role Catalog

- [ ] All standard roles documented (30+)
- [ ] Role definitions clear, job-based
- [ ] Business owners identified
- [ ] Systems and access documented
- [ ] User counts accurate
- [ ] Review dates documented
- [ ] Obsolete roles flagged
- [ ] No "TBD" values

### Sheet 3: Role Assignments

- [ ] All users accounted for
- [ ] Role names match Sheet 2
- [ ] Assignment dates documented
- [ ] Approvers documented
- [ ] Expired roles flagged
- [ ] Cross-referenced with user inventory
- [ ] Identity exports collected

### Sheet 4: Role Access Mapping

- [ ] All roles mapped to system access rights
- [ ] Access levels documented (Read, Write, Admin)
- [ ] Business justifications documented
- [ ] Access rights reviewed and current
- [ ] Maps aligned with role definitions

### Sheet 5: SoD Matrix

- [ ] All high-risk conflicts identified
- [ ] Conflict types described
- [ ] Risk levels assigned
- [ ] Mitigation controls documented
- [ ] Validated by security team
- [ ] 6-12 conflict pairs defined

### Sheet 6: SoD Violations

- [ ] All violations detected
- [ ] Each violation analyzed
- [ ] Justified violations have controls
- [ ] Justified violations have CISO approval
- [ ] Unjustified violations have plans
- [ ] High-risk prioritized (30 days)
- [ ] Target: Zero unresolved

### Sheet 7: Compensating Controls

- [ ] All SoD violations with exceptions documented
- [ ] Compensating controls defined for each
- [ ] Control owners assigned
- [ ] Review frequency established
- [ ] Effectiveness tracked
- [ ] Controls verified and tested

### Sheet 8: RBAC Coverage

- [ ] All systems assessed for RBAC adoption
- [ ] Role-based vs direct access calculated
- [ ] RBAC adoption percentages accurate
- [ ] Target thresholds defined
- [ ] Non-compliant systems identified

### Sheet 9: Gap Analysis

- [ ] All gaps identified
- [ ] Prioritized by risk
- [ ] Owners assigned
- [ ] Remediation plans specific
- [ ] Target dates realistic
- [ ] Critical gaps 30 days
- [ ] Status tracked

### Sheet 10: Evidence Register

- [ ] Evidence for all findings
- [ ] Evidence recent
- [ ] Storage locations accessible
- [ ] Audit-ready format
- [ ] Retention documented
- [ ] Critical evidence collected

### Sheet 11: Approval Sign-Off

- [ ] Self-review completed
- [ ] Quality checklist passed
- [ ] IAM Lead review completed
- [ ] CISO approval obtained
- [ ] Feedback addressed
- [ ] Next review scheduled

---

## Continuous Improvement

### Quarterly Review (3-5 hours)
1. Update role assignments
2. Detect new SoD violations
3. Update direct access users
4. Recalculate RBAC metrics
5. Track remediation progress

### Semi-Annual Review (5-8 hours)
1. Role catalog review
2. Role owner validation
3. Comprehensive SoD review
4. Role accuracy assessment
5. RBAC adoption improvement plan

### Annual Review (8-12 hours)
1. Comprehensive role catalog review
2. Complete role accuracy assessment
3. SoD matrix review
4. RBAC maturity strategic plan
5. Audit preparation

---

## Regulatory Mapping

### ISO/IEC 27001:2022

**A.5.15 - Access Control**:

- SoD Matrix (Sheet 5): Access control restrictions
- SoD Violations (Sheet 6): Policy enforcement
- Gap Analysis (Sheet 8): Policy violations

**A.5.18 - Access Rights**:

- Role Catalog (Sheet 2): Standard access rights
- Role Assignments (Sheet 3): Role-based provisioning
- RBAC Metrics (Sheet 7): Maturity measurement
- Gap Analysis (Sheet 8): Governance gaps

### FINMA Circular 2023/1 (Swiss Financial)

**Margin 56 - User Administration**:

- Role Catalog (Sheet 2): Documented roles
- Role Assignments (Sheet 3): Role-based provisioning
- RBAC Metrics (Sheet 7): Maturity measurement

**Margin 58 - Segregation of Duties**:

- SoD Matrix (Sheet 5): Incompatible role combinations
- SoD Violations (Sheet 6): Detection and remediation
- SoD Exception Approvals: CISO approval with controls

### GDPR Article 32 (EU)

**Article 32(1)(b) - Confidentiality**:

- Role Catalog: Authorized access definition
- SoD Matrix: Segregation prevents unauthorized combinations
- RBAC Metrics: Access is role-based (not ad-hoc)

**Article 32(1)(d) - Regular Testing**:

- Quarterly/Semi-Annual/Annual review cycles
- Role accuracy assessment
- SoD violation detection
- Gap analysis and remediation

### NIS2 Article 21 (EU)

**Article 21(2)(d) - Access Control**:

- Role Catalog: Formalized access control
- SoD Matrix: Access control restrictions
- RBAC Maturity: Access control effectiveness

**Article 21(2)(f) - Identity and Access Management**:

- RBAC maturity assessment
- Role governance
- SoD compliance
- Continuous monitoring

---

**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
