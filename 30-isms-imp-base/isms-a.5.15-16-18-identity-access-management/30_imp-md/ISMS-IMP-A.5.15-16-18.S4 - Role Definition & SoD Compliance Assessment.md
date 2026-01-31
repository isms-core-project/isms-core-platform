# ISMS-IMP-A.5.15-16-18.S4 - Role Definition & SoD Compliance Assessment
## Part I: User Completion Guide
### ISO/IEC 27001:2022 Controls A.5.15, A.5.18: Access Control, Access Rights

---

## Document Control

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.15-16-18.S4 |
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

# PART I: USER COMPLETION GUIDE

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
   - Identity system exports (AD groups, Azure AD roles, Okta groups)
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
   - Azure AD: Portal → Users → Group memberships
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
   - Role assignment exports (AD, Azure AD, Okta)
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

### Sheet 4: Direct Access Users
- [ ] All users accounted for
- [ ] Business justifications documented
- [ ] Justifications legitimate
- [ ] Approvals obtained
- [ ] Quarterly review frequency
- [ ] Unauthorized access flagged
- [ ] Direct access < 20%

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

### Sheet 7: RBAC Metrics
- [ ] Metrics calculated accurately
- [ ] RBAC adoption calculated
- [ ] SoD compliance calculated
- [ ] Role review compliance calculated
- [ ] Maturity score calculated
- [ ] Benchmarks applied
- [ ] Conditional formatting works

### Sheet 8: Gap Analysis
- [ ] All gaps identified
- [ ] Prioritized by risk
- [ ] Owners assigned
- [ ] Remediation plans specific
- [ ] Target dates realistic
- [ ] Critical gaps 30 days
- [ ] Status tracked

### Sheet 9: Evidence Register
- [ ] Evidence for all findings
- [ ] Evidence recent
- [ ] Storage locations accessible
- [ ] Audit-ready format
- [ ] Retention documented
- [ ] Critical evidence collected

### Sheet 10: Approval
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

**END OF PART I: USER COMPLETION GUIDE**

---

# PART II: TECHNICAL SPECIFICATION

## Workbook Structure

### Workbook Metadata

| Attribute | Value |
|-----------|-------|
| **Filename** | ISMS-IMP-A.5.15-16-18.S4_RoleCompliance_YYYY-MM.xlsx |
| **Total Sheets** | 10 |
| **File Format** | Excel Workbook (.xlsx) |
| **Excel Version** | Excel 2016 or later |
| **Macros** | None (formulas only) |
| **External Links** | None (self-contained) |

### Sheet Overview

| Sheet # | Sheet Name | Purpose | Rows (Est.) |
|---------|-----------|---------|-------------|
| 1 | Instructions_and_Legend | Document control, how to use, legends | 50 |
| 2 | Role_Catalog | Complete role inventory | 32-52 (30-50 roles) |
| 3 | Role_Assignments | User-to-role mappings | 82-202 (80-200 assignments) |
| 4 | Direct_Access_Users | Users without role assignments | 22-42 (20-40 users) |
| 5 | SoD_Matrix | Defined conflicting role pairs | 8-14 (6-12 conflicts) |
| 6 | SoD_Violations | Users with conflicting roles | 7-17 (5-15 violations) |
| 7 | RBAC_Metrics | RBAC maturity metrics | 30-40 |
| 8 | Gap_Analysis | Identified gaps and remediation | 12-22 (10-20 gaps) |
| 9 | Evidence_Register | Supporting documentation | 22-32 (20-30 evidence items) |
| 10 | Approval_and_Sign_Off | Three-level approval workflow | 30 |

---

## Sheet-by-Sheet Specifications

### Sheet 1: Instructions_and_Legend

**Purpose**: Document control, navigation guide, status/risk legends

**Layout**:
- **Rows 1-15**: Document Control
- **Rows 17-30**: Assessment Overview
- **Rows 32-45**: How to Use This Workbook
- **Rows 47-60**: Status Legends
- **Rows 62-75**: Risk Level Legends
- **Rows 77-90**: Conditional Formatting Guide
- **Rows 92-105**: Sheet Navigation Links

#### Document Control Section (Rows 1-15)

| Cell | Label | Value | Format |
|------|-------|-------|--------|
| A1 | Title | "ISMS-IMP-A.5.15-16-18.S4 - Role Definition & SoD Compliance Assessment" | Bold, 14pt, Navy |
| A3 | Document ID | "ISMS-IMP-A.5.15-16-18.S4" | Normal |
| A4 | Version | "1.0" | Normal |
| A5 | Assessment Period | "[Start Date] to [End Date]" | Normal, Date format |
| A6 | Prepared By | "[Name, Title]" | Normal |
| A7 | Preparation Date | [Date] | Date format |
| A8 | Review Date | [Date] | Date format |
| A9 | Next Review | [Date] (Quarterly/Semi-Annual/Annual) | Date format |
| A10 | Status | Dropdown: Draft, In Review, Approved | Conditional format |

#### Status Legend (Rows 47-60)

| Status | Description | Color Code |
|--------|-------------|------------|
| Active | Role or assignment currently active | Green background |
| Under Review | Role definition being updated | Yellow background |
| Obsolete | Role no longer used, should be deactivated | Orange background |
| Expired | Time-bounded role past expiration | Red background |
| Remediated | SoD violation resolved | Green background |
| Justified with Controls | SoD violation approved with mitigations | Yellow background |
| Open | SoD violation unresolved | Red background |

#### Risk Level Legend (Rows 62-75)

| Risk Level | Description | Color Code |
|------------|-------------|------------|
| Critical | Unresolved SoD violation with fraud risk | Red text, Red background |
| High | Low RBAC adoption, missing SoD approvals | Red text |
| Medium | Outdated roles, obsolete roles active | Orange text |
| Low | Minor process improvements | Black text |

#### Conditional Formatting Guide (Rows 77-90)

| Metric | Green | Yellow | Red |
|--------|-------|--------|-----|
| RBAC Adoption | >= 80% | 60-79% | < 60% |
| SoD Violations (Unresolved) | 0 | N/A | > 0 |
| Role Review Compliance | >= 95% | 80-94% | < 80% |
| Direct Access % | < 20% | 20-30% | > 30% |
| Overall Maturity Score | >= 80 | 60-79 | < 60 |

---

### Sheet 2: Role_Catalog

**Purpose**: Document all standard roles

**Column Structure**:

| Column | Header | Data Type | Width | Formula/Validation | Conditional Formatting |
|--------|--------|-----------|-------|-------------------|----------------------|
| A | Role_ID | Text | 12 | Manual entry (ROLE-001, ROLE-002, etc.) | None |
| B | Role_Name | Text | 25 | Manual entry | None |
| C | Role_Description | Text | 40 | Manual entry | None |
| D | Business_Owner | Text | 20 | Manual entry | None |
| E | Systems_Included | Text | 30 | Manual entry (comma-separated list) | None |
| F | Access_Level_Summary | Text | 30 | Manual entry | None |
| G | Users_Assigned | Number | 12 | `=COUNTIF(Role_Assignments!C:C, B2)` | Green if > 0, Red if = 0 and Status = "Active" |
| H | Last_Review_Date | Date | 15 | Manual entry | Green if < 365 days, Yellow if 365-545, Red if > 545 |
| I | Next_Review_Date | Date | 15 | `=H2+365` | Yellow if < TODAY()+30 (review due soon) |
| J | Status | Dropdown | 15 | Dropdown: Active, Under Review, Obsolete | Green = Active, Yellow = Under Review, Orange = Obsolete |

**Data Validation**:
- **Column A (Role_ID)**: Unique values (no duplicates)
- **Column J (Status)**: Dropdown list = Active, Under Review, Obsolete

**Conditional Formatting Rules**:

1. **Column G (Users_Assigned)**:
   ```
   Rule 1: =AND(G2>0, J2="Active")
   Format: Green background
   
   Rule 2: =AND(G2=0, J2="Active")
   Format: Red background (obsolete role still marked active)
   ```

2. **Column H (Last_Review_Date)**:
   ```
   Rule 1: =TODAY()-H2<365
   Format: Green background
   
   Rule 2: =AND(TODAY()-H2>=365, TODAY()-H2<=545)
   Format: Yellow background
   
   Rule 3: =TODAY()-H2>545
   Format: Red background
   ```

3. **Column I (Next_Review_Date)**:
   ```
   Rule 1: =I2<TODAY()+30
   Format: Yellow background (review due soon)
   ```

4. **Column J (Status)**:
   ```
   Rule 1: =J2="Active"
   Format: Green background
   
   Rule 2: =J2="Under Review"
   Format: Yellow background
   
   Rule 3: =J2="Obsolete"
   Format: Orange background
   ```

**Header Row Styling**:
- **Row 1**: Bold, White text, Navy background, 14pt
- **Freeze Panes**: Row 2 (header row always visible)

**Sample Data** (Rows 2-4):

| Role_ID | Role_Name | Role_Description | Business_Owner | Systems | Access | Users | Last_Review | Next_Review | Status |
|---------|-----------|------------------|----------------|---------|--------|-------|-------------|-------------|--------|
| ROLE-001 | Financial Analyst | Manages financial reporting, budget analysis | Finance Director | ERP, Budget, Files | ERP: Read, Budget: R/W | 15 | 2025-09-15 | 2026-09-15 | Active |
| ROLE-002 | HR Administrator | Employee lifecycle, HR systems | HR Manager | HRIS, Payroll, Identity | HRIS: Full, Payroll: Read | 8 | 2025-10-01 | 2026-10-01 | Active |
| ROLE-003 | Developer | Development environments, code repositories | Engineering Mgr | GitHub, Dev Servers, Test | GitHub: R/W Dev, Dev: Full | 25 | 2025-08-20 | 2026-08-20 | Active |

**Summary Metrics** (Bottom of sheet, below data):

| Metric | Formula | Location |
|--------|---------|----------|
| Total Roles | `=COUNTA(A2:A51)-COUNTIF(A2:A51,"")` | Cell A53 |
| Active Roles | `=COUNTIF(J2:J51,"Active")` | Cell A54 |
| Obsolete Roles | `=COUNTIF(J2:J51,"Obsolete")` | Cell A55 |
| Roles Needing Review | `=COUNTIF(I2:I51,"<"&TODAY()+30)` | Cell A56 |
| Roles Reviewed Last 12 Months | `=COUNTIF(H2:H51,">"&TODAY()-365)` | Cell A57 |
| Role Review Compliance % | `=(A57/A53)*100` | Cell A58 |

---

### Sheet 3: Role_Assignments

**Purpose**: Document user-to-role mappings

**Column Structure**:

| Column | Header | Data Type | Width | Formula/Validation | Conditional Formatting |
|--------|--------|-----------|-------|-------------------|----------------------|
| A | User_ID | Text | 15 | Manual entry | None |
| B | User_Name | Text | 25 | Manual entry | None |
| C | Role_Name | Text | 25 | Dropdown from Role_Catalog!B:B | None |
| D | Assignment_Date | Date | 15 | Manual entry | None |
| E | Assignment_Approver | Text | 20 | Manual entry | None |
| F | Expiration_Date | Date | 15 | Manual entry (optional, for contractors) | Yellow if within 30 days, Red if past |
| G | Status | Dropdown | 15 | Dropdown: Active, Expired, Removed | Green = Active, Red = Expired |

**Data Validation**:
- **Column C (Role_Name)**: Dropdown list from Role_Catalog!B:B (role names)
- **Column G (Status)**: Dropdown list = Active, Expired, Removed

**Conditional Formatting Rules**:

1. **Column F (Expiration_Date)**:
   ```
   Rule 1: =AND(F2<>"", F2<TODAY()+30, F2>=TODAY())
   Format: Yellow background (expiring within 30 days)
   
   Rule 2: =AND(F2<>"", F2<TODAY())
   Format: Red background (expired)
   ```

2. **Column G (Status)**:
   ```
   Rule 1: =AND(G2="Active", F2<>"", F2<TODAY())
   Format: Red background (status = Active but expired)
   
   Rule 2: =G2="Active"
   Format: Green background
   
   Rule 3: =G2="Expired"
   Format: Red background
   ```

**Header Row Styling**:
- **Row 1**: Bold, White text, Navy background, 14pt
- **Freeze Panes**: Row 2

**Sample Data** (Rows 2-4):

| User_ID | User_Name | Role_Name | Assignment_Date | Approver | Expiration | Status |
|---------|-----------|-----------|----------------|----------|------------|--------|
| U00123 | John Doe | Financial Analyst | 2024-06-15 | Finance Manager | (blank) | Active |
| U00124 | Jane Smith | HR Administrator | 2024-03-01 | HR Manager | (blank) | Active |
| U00125 | Bob Johnson | Developer | 2024-08-10 | Engineering Mgr | 2025-12-31 | Active |

**Summary Metrics** (Bottom of sheet):

| Metric | Formula | Location |
|--------|---------|----------|
| Total Role Assignments | `=COUNTA(A2:A201)-COUNTIF(A2:A201,"")` | Cell A203 |
| Active Assignments | `=COUNTIF(G2:G201,"Active")` | Cell A204 |
| Expired Assignments | `=COUNTIF(G2:G201,"Expired")` | Cell A205 |
| Assignments Expiring <30 Days | `=COUNTIFS(F2:F201,"<"&TODAY()+30, F2:F201,">="&TODAY())` | Cell A206 |
| Unique Users with Roles | `=SUMPRODUCT(1/COUNTIF(A2:A201,A2:A201&""))` | Cell A207 |

---

### Sheet 4: Direct_Access_Users

**Purpose**: Document users without role assignments (exceptions to RBAC)

**Column Structure**:

| Column | Header | Data Type | Width | Formula/Validation | Conditional Formatting |
|--------|--------|-----------|-------|-------------------|----------------------|
| A | User_ID | Text | 15 | Manual entry | None |
| B | User_Name | Text | 25 | Manual entry | None |
| C | Systems_Accessed | Text | 30 | Manual entry (comma-separated) | None |
| D | Reason_No_Role | Text | 30 | Manual entry | Red if blank (missing justification) |
| E | Business_Justification | Text | 40 | Manual entry | Red if blank (missing justification) |
| F | Approved_By | Text | 20 | Manual entry | Red if blank (missing approval) |
| G | Review_Frequency | Dropdown | 15 | Dropdown: Quarterly, Semi-Annual | Yellow if not Quarterly |
| H | Last_Review_Date | Date | 15 | Manual entry | Green if < 90 days, Yellow if 90-120, Red if > 120 |

**Data Validation**:
- **Column G (Review_Frequency)**: Dropdown list = Quarterly, Semi-Annual, Annual

**Conditional Formatting Rules**:

1. **Column D (Reason_No_Role)**:
   ```
   Rule 1: =D2=""
   Format: Red background (missing justification)
   ```

2. **Column E (Business_Justification)**:
   ```
   Rule 1: =E2=""
   Format: Red background (missing justification)
   ```

3. **Column F (Approved_By)**:
   ```
   Rule 1: =F2=""
   Format: Red background (missing approval)
   ```

4. **Column G (Review_Frequency)**:
   ```
   Rule 1: =G2<>"Quarterly"
   Format: Yellow background (should be Quarterly for direct access)
   ```

5. **Column H (Last_Review_Date)**:
   ```
   Rule 1: =TODAY()-H2<90
   Format: Green background
   
   Rule 2: =AND(TODAY()-H2>=90, TODAY()-H2<=120)
   Format: Yellow background
   
   Rule 3: =TODAY()-H2>120
   Format: Red background (overdue review)
   ```

**Header Row Styling**:
- **Row 1**: Bold, White text, Navy background, 14pt
- **Freeze Panes**: Row 2

**Sample Data** (Rows 2-4):

| User_ID | User_Name | Systems | Reason | Justification | Approved By | Frequency | Last Review |
|---------|-----------|---------|--------|---------------|-------------|-----------|-------------|
| U00456 | Alice Brown | Custom DB, Legacy App | Unique job function | Executive oversight requires access to all systems | CISO | Quarterly | 2025-09-01 |
| U00457 | Charlie Davis | Special Tool | Temporary project | 6-month project access | Security Manager | Quarterly | 2025-08-15 |
| U00458 | Dana Evans | Restricted System | No equivalent role | Consultant role doesn't fit standard roles | CISO | Quarterly | 2025-10-05 |

**Summary Metrics** (Bottom of sheet):

| Metric | Formula | Location |
|--------|---------|----------|
| Total Direct Access Users | `=COUNTA(A2:A41)-COUNTIF(A2:A41,"")` | Cell A43 |
| Missing Justifications | `=COUNTIF(E2:E41,"")` | Cell A44 |
| Missing Approvals | `=COUNTIF(F2:F41,"")` | Cell A45 |
| Reviews Overdue (>120 days) | `=COUNTIF(H2:H41,"<"&TODAY()-120)` | Cell A46 |
| Direct Access % | `=A43/(Role_Assignments!A207+A43)*100` | Cell A47 |

---

### Sheet 5: SoD_Matrix

**Purpose**: Define conflicting role combinations (segregation of duties policy)

**Column Structure**:

| Column | Header | Data Type | Width | Formula/Validation | Conditional Formatting |
|--------|--------|-----------|-------|-------------------|----------------------|
| A | Conflict_ID | Text | 12 | Manual entry (SOD-001, SOD-002, etc.) | None |
| B | Role_A | Text | 25 | Dropdown from Role_Catalog!B:B | None |
| C | Role_B | Text | 25 | Dropdown from Role_Catalog!B:B | None |
| D | Conflict_Type | Text | 30 | Manual entry | None |
| E | Risk_Level | Dropdown | 12 | Dropdown: High, Medium, Low | Red = High, Yellow = Medium, Green = Low |
| F | Mitigation | Text | 40 | Manual entry | None |

**Data Validation**:
- **Column B, C (Role_A, Role_B)**: Dropdown list from Role_Catalog!B:B
- **Column E (Risk_Level)**: Dropdown list = High, Medium, Low

**Conditional Formatting Rules**:

1. **Column E (Risk_Level)**:
   ```
   Rule 1: =E2="High"
   Format: Red text, Red background
   
   Rule 2: =E2="Medium"
   Format: Orange text, Yellow background
   
   Rule 3: =E2="Low"
   Format: Green text
   ```

**Header Row Styling**:
- **Row 1**: Bold, White text, Navy background, 14pt
- **Freeze Panes**: Row 2

**Sample Data** (Rows 2-7):

| Conflict_ID | Role_A | Role_B | Conflict_Type | Risk | Mitigation |
|-------------|--------|--------|---------------|------|------------|
| SOD-001 | Expense Submitter | Expense Approver | Request + Approve | High | Manager review, quarterly audit |
| SOD-002 | Developer | Production Admin | Dev + Prod | High | Change control, peer review, logging |
| SOD-003 | Finance Manager | Payroll Processor | Finance + Payroll | High | Dual approval, segregated accounts |
| SOD-004 | Procurement Officer | Accounts Payable Clerk | Procurement + AP | Medium | Purchase order matching, manager review |
| SOD-005 | Database Admin | Application Owner | DB Admin + App Owner | Medium | Change logging, separation of duties |
| SOD-006 | HR Administrator | Payroll Processor | HR + Payroll | High | Segregated systems, quarterly audit |

**Summary Metrics** (Bottom of sheet):

| Metric | Formula | Location |
|--------|---------|----------|
| Total SoD Conflicts Defined | `=COUNTA(A2:A13)-COUNTIF(A2:A13,"")` | Cell A15 |
| High Risk Conflicts | `=COUNTIF(E2:E13,"High")` | Cell A16 |
| Medium Risk Conflicts | `=COUNTIF(E2:E13,"Medium")` | Cell A17 |
| Low Risk Conflicts | `=COUNTIF(E2:E13,"Low")` | Cell A18 |

---

### Sheet 6: SoD_Violations

**Purpose**: Detect users with conflicting role assignments

**Column Structure**:

| Column | Header | Data Type | Width | Formula/Validation | Conditional Formatting |
|--------|--------|-----------|-------|-------------------|----------------------|
| A | User_ID | Text | 15 | Manual entry | None |
| B | User_Name | Text | 25 | Manual entry | None |
| C | Conflicting_Roles | Text | 30 | Manual entry (Role A + Role B) | None |
| D | Conflict_Type | Text | 30 | Lookup from SoD_Matrix!D:D | None |
| E | Risk_Level | Dropdown | 12 | Lookup from SoD_Matrix!E:E | Red = High, Yellow = Medium |
| F | Detection_Date | Date | 15 | Manual entry | None |
| G | Business_Justification | Text | 40 | Manual entry | Red if blank and Status = Open |
| H | Compensating_Controls | Text | 40 | Manual entry | Red if blank and Status = Justified |
| I | Approved_By | Text | 20 | Manual entry | Red if blank and Status = Justified |
| J | Remediation_Plan | Text | 40 | Manual entry | Red if blank and Status = Open |
| K | Remediation_Date | Date | 15 | Manual entry | Red if past and Status = Open |
| L | Status | Dropdown | 20 | Dropdown: Open, Justified with Controls, Remediated | Red = Open, Yellow = Justified, Green = Remediated |

**Data Validation**:
- **Column E (Risk_Level)**: Dropdown list = High, Medium, Low
- **Column L (Status)**: Dropdown list = Open, Justified with Controls, Remediated

**Conditional Formatting Rules**:

1. **Column E (Risk_Level)**:
   ```
   Rule 1: =E2="High"
   Format: Red text, Red background
   
   Rule 2: =E2="Medium"
   Format: Orange text, Yellow background
   ```

2. **Column G (Business_Justification)**:
   ```
   Rule 1: =AND(G2="", L2="Open")
   Format: Red background (missing justification for open violation)
   ```

3. **Column H (Compensating_Controls)**:
   ```
   Rule 1: =AND(H2="", L2="Justified with Controls")
   Format: Red background (missing controls for justified violation)
   ```

4. **Column I (Approved_By)**:
   ```
   Rule 1: =AND(I2="", L2="Justified with Controls")
   Format: Red background (missing approval for justified violation)
   ```

5. **Column J (Remediation_Plan)**:
   ```
   Rule 1: =AND(J2="", L2="Open")
   Format: Red background (missing plan for open violation)
   ```

6. **Column K (Remediation_Date)**:
   ```
   Rule 1: =AND(K2<TODAY(), L2="Open")
   Format: Red background (remediation overdue)
   ```

7. **Column L (Status)**:
   ```
   Rule 1: =L2="Open"
   Format: Red background
   
   Rule 2: =L2="Justified with Controls"
   Format: Yellow background
   
   Rule 3: =L2="Remediated"
   Format: Green background
   ```

**Header Row Styling**:
- **Row 1**: Bold, White text, Navy background, 12pt (smaller due to more columns)
- **Freeze Panes**: Row 2

**Sample Data** (Rows 2-4):

| User_ID | Name | Conflicting Roles | Conflict Type | Risk | Detection | Justification | Controls | Approved By | Plan | Target Date | Status |
|---------|------|-------------------|---------------|------|-----------|---------------|----------|-------------|------|-------------|--------|
| U00789 | Bob Johnson | Developer + Production Admin | Dev + Prod | High | 2025-10-15 | Small team, only person with skills | Change control, peer review, enhanced logging | CISO | (blank) | (blank) | Justified with Controls |
| U00790 | Carol White | Expense Submitter + Expense Approver | Request + Approve | High | 2025-10-18 | (blank) | (blank) | (blank) | Remove Expense Approver role | 2025-11-15 | Open |
| U00791 | Dave Green | Finance Manager + Payroll Processor | Finance + Payroll | High | 2025-10-20 | (blank) | (blank) | (blank) | Remove Payroll role, assign to HR team | 2025-11-30 | Open |

**Summary Metrics** (Bottom of sheet):

| Metric | Formula | Location |
|--------|---------|----------|
| Total SoD Violations Detected | `=COUNTA(A2:A16)-COUNTIF(A2:A16,"")` | Cell A18 |
| Open (Unresolved) | `=COUNTIF(L2:L16,"Open")` | Cell A19 |
| Justified with Controls | `=COUNTIF(L2:L16,"Justified with Controls")` | Cell A20 |
| Remediated | `=COUNTIF(L2:L16,"Remediated")` | Cell A21 |
| High Risk Violations | `=COUNTIF(E2:E16,"High")` | Cell A22 |
| Remediation Overdue | `=COUNTIFS(K2:K16,"<"&TODAY(), L2:L16,"Open")` | Cell A23 |

---

### Sheet 7: RBAC_Metrics

**Purpose**: Calculate RBAC maturity metrics and overall compliance score

**Layout**:
- **Rows 1-25**: RBAC Adoption Metrics
- **Rows 27-40**: Role Usage Metrics
- **Rows 42-55**: SoD Compliance Metrics
- **Rows 57-70**: Role Review Metrics
- **Rows 72-85**: Overall RBAC Maturity Score
- **Rows 87-100**: Benchmark Comparisons

#### RBAC Adoption Metrics (Rows 1-25)

| Row | Metric | Formula | Target | Format |
|-----|--------|---------|--------|--------|
| 2 | **RBAC Adoption Metrics** | (header) | | Bold, Navy, 12pt |
| 4 | Total Users | `=Role_Assignments!A207+Direct_Access_Users!A43` | N/A | Number |
| 5 | Users with Roles | `=Role_Assignments!A207` | N/A | Number |
| 6 | Users with Direct Access | `=Direct_Access_Users!A43` | N/A | Number |
| 7 | RBAC Adoption Rate (%) | `=(B5/B4)*100` | >= 80% | Percent, CF: Green >= 80, Yellow 60-79, Red < 60 |
| 9 | Role Coverage (%) | `=(B5/B4)*100` | >= 80% | Percent, CF: Green >= 80, Yellow 60-79, Red < 60 |
| 10 | Direct Access (%) | `=(B6/B4)*100` | < 20% | Percent, CF: Green < 20, Yellow 20-30, Red > 30 |

**Conditional Formatting** (Column B):
```
Rule 1: =AND(B7>=80, B2="RBAC Adoption Rate (%)")
Format: Green background

Rule 2: =AND(B7>=60, B7<80, B2="RBAC Adoption Rate (%)")
Format: Yellow background

Rule 3: =AND(B7<60, B2="RBAC Adoption Rate (%)")
Format: Red background
```

#### Role Usage Metrics (Rows 27-40)

| Row | Metric | Formula | Target | Format |
|-----|--------|---------|--------|--------|
| 28 | **Role Usage Metrics** | (header) | | Bold, Navy, 12pt |
| 30 | Total Role Assignments | `=Role_Assignments!A203` | N/A | Number |
| 31 | Average Roles per User | `=B30/B5` | 1-3 | Number, 2 decimals, CF: Green 1-3, Yellow 3-5, Red > 5 |
| 33 | Active Roles | `=Role_Catalog!A54` | N/A | Number |
| 34 | Obsolete Roles | `=Role_Catalog!A55` | 0 | Number, CF: Green = 0, Red > 0 |
| 35 | Unused Roles (Active with 0 users) | `=COUNTIFS(Role_Catalog!G:G,0,Role_Catalog!J:J,"Active")` | 0 | Number, CF: Green = 0, Red > 0 |

#### SoD Compliance Metrics (Rows 42-55)

| Row | Metric | Formula | Target | Format |
|-----|--------|---------|--------|--------|
| 43 | **SoD Compliance Metrics** | (header) | | Bold, Navy, 12pt |
| 45 | SoD Violations Detected | `=SoD_Violations!A18` | N/A | Number |
| 46 | SoD Violations Unresolved | `=SoD_Violations!A19` | 0 | Number, CF: Green = 0, Red > 0 |
| 47 | SoD Violations Justified | `=SoD_Violations!A20` | Minimal | Number |
| 48 | SoD Violations Remediated | `=SoD_Violations!A21` | N/A | Number |
| 50 | SoD Compliance Rate (%) | `=((B4-B46)/B4)*100` | 100% | Percent, CF: Green = 100, Yellow >= 95, Red < 95 |

#### Role Review Metrics (Rows 57-70)

| Row | Metric | Formula | Target | Format |
|-----|--------|---------|--------|--------|
| 58 | **Role Review Metrics** | (header) | | Bold, Navy, 12pt |
| 60 | Total Roles | `=Role_Catalog!A53` | N/A | Number |
| 61 | Roles Reviewed Last 12 Months | `=Role_Catalog!A57` | N/A | Number |
| 62 | Role Review Compliance (%) | `=(B61/B60)*100` | >= 95% | Percent, CF: Green >= 95, Yellow 80-94, Red < 80 |
| 64 | Roles Needing Review (<30 days) | `=Role_Catalog!A56` | N/A | Number |

#### Overall RBAC Maturity Score (Rows 72-85)

| Row | Metric | Formula | Weight | Format |
|-----|--------|---------|--------|--------|
| 73 | **Overall RBAC Maturity Score** | (header) | | Bold, Navy, 14pt |
| 75 | RBAC Adoption Component | `=B7*0.40` | 40% | Number, 2 decimals |
| 76 | SoD Compliance Component | `=B50*0.30` | 30% | Number, 2 decimals |
| 77 | Role Review Component | `=B62*0.20` | 20% | Number, 2 decimals |
| 78 | Direct Access Justification Component | `=((Direct_Access_Users!A43-Direct_Access_Users!A44-Direct_Access_Users!A45)/Direct_Access_Users!A43)*100*0.10` | 10% | Number, 2 decimals |
| 80 | **Overall RBAC Maturity Score** | `=B75+B76+B77+B78` | | Number, 1 decimal, Bold, 16pt |
| 81 | | (blank) | | |
| 82 | Maturity Rating | `=IF(B80>=90,"Excellent",IF(B80>=80,"Very Good",IF(B80>=70,"Good",IF(B80>=60,"Fair","Poor"))))` | | Text, CF based on rating |

**Conditional Formatting** (Row 82, Column B):
```
Rule 1: =B82="Excellent"
Format: Dark Green text, Green background

Rule 2: =B82="Very Good"
Format: Green text, Light Green background

Rule 3: =B82="Good"
Format: Black text, Yellow background

Rule 4: =B82="Fair"
Format: Orange text, Light Orange background

Rule 5: =B82="Poor"
Format: Red text, Red background
```

#### Benchmark Comparisons (Rows 87-100)

| Row | Metric | Excellent | Very Good | Good | Fair | Poor | Actual |
|-----|--------|-----------|-----------|------|------|------|--------|
| 88 | **Benchmark Comparisons** | (header) | | | | | |
| 90 | RBAC Adoption | >= 90% | 80-89% | 70-79% | 60-69% | < 60% | `=B7` (CF based on value) |
| 91 | SoD Unresolved | 0 | 0 | 1-2 | 3-5 | > 5 | `=B46` (CF based on value) |
| 92 | Role Review | >= 95% | 85-94% | 70-84% | 60-69% | < 60% | `=B62` (CF based on value) |
| 93 | Overall Maturity | >= 90 | 80-89 | 70-79 | 60-69 | < 60 | `=B80` (CF based on value) |

**Conditional Formatting** (Column G, Rows 90-93):
```
Rule 1: =AND(G90>=90, $A90="RBAC Adoption")
Format: Dark Green background

Rule 2: =AND(G90>=80, G90<90, $A90="RBAC Adoption")
Format: Light Green background

Rule 3: =AND(G90>=70, G90<80, $A90="RBAC Adoption")
Format: Yellow background

Rule 4: =AND(G90>=60, G90<70, $A90="RBAC Adoption")
Format: Orange background

Rule 5: =AND(G90<60, $A90="RBAC Adoption")
Format: Red background
```

(Similar rules for rows 91-93 adjusted for their respective thresholds)

---

### Sheet 8: Gap_Analysis

**Purpose**: Identify RBAC and SoD gaps with remediation plans

**Column Structure**:

| Column | Header | Data Type | Width | Formula/Validation | Conditional Formatting |
|--------|--------|-----------|-------|-------------------|----------------------|
| A | Gap_ID | Text | 12 | Manual entry (RBC-GAP-001, etc.) | None |
| B | Gap_Type | Dropdown | 25 | Dropdown: Low RBAC Adoption, Unresolved SoD, etc. | None |
| C | Severity | Dropdown | 12 | Dropdown: Critical, High, Medium, Low | Red = Critical/High, Orange = Medium, Green = Low |
| D | Description | Text | 40 | Manual entry | None |
| E | Current_State | Text | 25 | Manual entry | None |
| F | Target_State | Text | 25 | Manual entry | None |
| G | Owner | Text | 20 | Manual entry | Red if blank |
| H | Remediation_Plan | Text | 40 | Manual entry | Red if blank |
| I | Target_Date | Date | 15 | Manual entry | Red if past and Status = Open |
| J | Status | Dropdown | 15 | Dropdown: Open, In Progress, Closed | Red = Open, Yellow = In Progress, Green = Closed |
| K | Audit_Impact | Dropdown | 15 | Dropdown: Finding, Observation, No Impact | Red = Finding, Yellow = Observation |

**Data Validation**:
- **Column B (Gap_Type)**: Dropdown list = Low RBAC Adoption, High Direct Access, Unauthorized Direct Access, Unresolved SoD Violations, Outdated Role Definitions, Obsolete Roles Not Deactivated, Missing SoD Exception Approvals, Missing Compensating Controls
- **Column C (Severity)**: Dropdown list = Critical, High, Medium, Low
- **Column J (Status)**: Dropdown list = Open, In Progress, Closed
- **Column K (Audit_Impact)**: Dropdown list = Finding, Observation, No Impact

**Conditional Formatting Rules**:

1. **Column C (Severity)**:
   ```
   Rule 1: =OR(C2="Critical", C2="High")
   Format: Red text, Red background
   
   Rule 2: =C2="Medium"
   Format: Orange text, Yellow background
   
   Rule 3: =C2="Low"
   Format: Black text
   ```

2. **Column G (Owner)**:
   ```
   Rule 1: =G2=""
   Format: Red background
   ```

3. **Column H (Remediation_Plan)**:
   ```
   Rule 1: =H2=""
   Format: Red background
   ```

4. **Column I (Target_Date)**:
   ```
   Rule 1: =AND(I2<TODAY(), J2<>"Closed")
   Format: Red background (remediation overdue)
   ```

5. **Column J (Status)**:
   ```
   Rule 1: =J2="Open"
   Format: Red background
   
   Rule 2: =J2="In Progress"
   Format: Yellow background
   
   Rule 3: =J2="Closed"
   Format: Green background
   ```

6. **Column K (Audit_Impact)**:
   ```
   Rule 1: =K2="Finding"
   Format: Red text
   
   Rule 2: =K2="Observation"
   Format: Orange text
   ```

**Header Row Styling**:
- **Row 1**: Bold, White text, Navy background, 12pt
- **Freeze Panes**: Row 2

**Sample Data** (Rows 2-5):

| Gap_ID | Gap_Type | Severity | Description | Current | Target | Owner | Plan | Target Date | Status | Audit Impact |
|--------|----------|----------|-------------|---------|--------|-------|------|-------------|--------|--------------|
| RBC-GAP-001 | Unresolved SoD Violation | Critical | 3 users with Dev+ProdAdmin roles | SoD violations = 3 | Zero unresolved violations | IAM Team | Remove ProdAdmin role, migrate duties to ops team | 2025-11-15 | Open | Finding |
| RBC-GAP-002 | Low RBAC Adoption | High | RBAC adoption = 65% | RBAC adoption = 65% | >= 80% adoption | IAM Team | Create 5 new roles, migrate 30 users from direct access | 2026-01-31 | In Progress | Observation |
| RBC-GAP-003 | Outdated Role Definitions | High | 40% roles not reviewed 12+ months | 40% roles outdated | >= 95% roles reviewed | Role Owners | Schedule role review meetings with all owners | 2025-12-15 | In Progress | Observation |
| RBC-GAP-004 | Obsolete Roles Active | Medium | 8 obsolete roles still marked "Active" | 8 obsolete roles | 0 obsolete roles | IAM Team | Deactivate obsolete roles, verify zero users | 2025-12-31 | Open | No Impact |

**Summary Metrics** (Bottom of sheet):

| Metric | Formula | Location |
|--------|---------|----------|
| Total Gaps | `=COUNTA(A2:A21)-COUNTIF(A2:A21,"")` | Cell A23 |
| Critical Gaps | `=COUNTIF(C2:C21,"Critical")` | Cell A24 |
| High Gaps | `=COUNTIF(C2:C21,"High")` | Cell A25 |
| Open Gaps | `=COUNTIF(J2:J21,"Open")` | Cell A26 |
| Overdue Gaps | `=COUNTIFS(I2:I21,"<"&TODAY(), J2:J21,"<>Closed")` | Cell A27 |
| Audit Findings | `=COUNTIF(K2:K21,"Finding")` | Cell A28 |

---

### Sheet 9: Evidence_Register

**Purpose**: Document supporting evidence for audit

**Column Structure**:

| Column | Header | Data Type | Width | Formula/Validation | Conditional Formatting |
|--------|--------|-----------|-------|-------------------|----------------------|
| A | Evidence_ID | Text | 15 | Manual entry (RBC-EV-001, etc.) | None |
| B | Evidence_Type | Dropdown | 15 | Dropdown: Document, Export, Screenshot, Email, Approval, Meeting Minutes | None |
| C | Description | Text | 40 | Manual entry | None |
| D | Source | Text | 25 | Manual entry | None |
| E | Date_Collected | Date | 15 | Manual entry | Green if within assessment period, Red if outside |
| F | Storage_Location | Text | 30 | Manual entry | Red if blank |
| G | Retention_Period | Text | 15 | Manual entry (typically "3 years") | None |
| H | Audit_Relevance | Text | 15 | Manual entry (A.5.15, A.5.18, or both) | None |

**Data Validation**:
- **Column B (Evidence_Type)**: Dropdown list = Document, Export, Screenshot, Email, Approval, Meeting Minutes

**Conditional Formatting Rules**:

1. **Column E (Date_Collected)**:
   ```
   Rule 1: =AND(E2>=Instructions_and_Legend!$B$5, E2<=Instructions_and_Legend!$B$5+365)
   Format: Green background (within assessment period)
   
   Rule 2: =OR(E2<Instructions_and_Legend!$B$5, E2>Instructions_and_Legend!$B$5+365)
   Format: Red background (outside assessment period)
   ```

2. **Column F (Storage_Location)**:
   ```
   Rule 1: =F2=""
   Format: Red background (missing storage location)
   ```

**Header Row Styling**:
- **Row 1**: Bold, White text, Navy background, 14pt
- **Freeze Panes**: Row 2

**Sample Data** (Rows 2-6):

| Evidence_ID | Type | Description | Source | Date_Collected | Storage | Retention | Audit |
|-------------|------|-------------|--------|----------------|---------|-----------|-------|
| RBC-EV-001 | Document | Role catalog with business owner approvals | IAM Team | 2025-10-15 | SharePoint/Evidence/IAM/Role_Catalog.xlsx | 3 years | A.5.18 |
| RBC-EV-002 | Export | AD group memberships export | Active Directory | 2025-10-15 | SharePoint/Evidence/IAM/AD_Groups.csv | 3 years | A.5.18 |
| RBC-EV-003 | Document | SoD policy document | Security Team | 2025-10-15 | SharePoint/Evidence/IAM/SoD_Policy.pdf | 3 years | A.5.15 |
| RBC-EV-004 | Email | CISO approval for SoD exception User123 | CISO | 2025-10-18 | SharePoint/Evidence/IAM/SoD_Approval_User123.pdf | 3 years | A.5.15 |
| RBC-EV-005 | Meeting Minutes | Role review meeting Finance roles | Finance Director | 2025-09-15 | SharePoint/Evidence/IAM/Role_Review_Finance_Q3.pdf | 3 years | A.5.18 |

**Summary Metrics** (Bottom of sheet):

| Metric | Formula | Location |
|--------|---------|----------|
| Total Evidence Items | `=COUNTA(A2:A31)-COUNTIF(A2:A31,"")` | Cell A33 |
| Documents | `=COUNTIF(B2:B31,"Document")` | Cell A34 |
| Exports | `=COUNTIF(B2:B31,"Export")` | Cell A35 |
| Approvals | `=COUNTIF(B2:B31,"Approval")` | Cell A36 |
| Missing Storage Locations | `=COUNTIF(F2:F31,"")` | Cell A37 |

---

### Sheet 10: Approval_and_Sign_Off

**Purpose**: Three-level approval workflow

**Layout**:
- **Rows 1-20**: Self-Review (Assessment Completer)
- **Rows 22-40**: IAM Team Lead Review
- **Rows 42-60**: CISO Review & Approval

#### Self-Review Section (Rows 1-20)

| Row | Field | Value | Format |
|-----|-------|-------|--------|
| 1 | **Self-Review (Assessment Completer)** | (header) | Bold, 14pt, Navy |
| 3 | Completer Name | [Manual entry] | Normal |
| 4 | Completer Title | [Manual entry] | Normal |
| 5 | Review Date | [Date] | Date format |
| 7 | Quality Checklist Completed? | Dropdown: Yes, No | CF: Green = Yes, Red = No |
| 8 | Completeness Confirmed? | Dropdown: Yes, No | CF: Green = Yes, Red = No |
| 9 | Formulas Verified? | Dropdown: Yes, No | CF: Green = Yes, Red = No |
| 10 | Conditional Formatting Verified? | Dropdown: Yes, No | CF: Green = Yes, Red = No |
| 11 | Evidence Collected? | Dropdown: Yes, No | CF: Green = Yes, Red = No |
| 13 | Comments/Notes | [Manual entry] | Text, Wrap text |
| 17 | Signature/Approval | [Manual entry] | Normal |
| 18 | Approval Date | [Date] | Date format |

**Conditional Formatting** (Column B, Rows 7-11):
```
Rule 1: =B7="Yes"
Format: Green background

Rule 2: =B7="No"
Format: Red background
```

#### IAM Team Lead Review Section (Rows 22-40)

| Row | Field | Value | Format |
|-----|-------|-------|--------|
| 22 | **IAM Team Lead Review** | (header) | Bold, 14pt, Navy |
| 24 | Reviewer Name | [Manual entry] | Normal |
| 25 | Reviewer Title | [Manual entry] | Normal |
| 26 | Review Date | [Date] | Date format |
| 28 | Technical Validation Completed? | Dropdown: Yes, No | CF: Green = Yes, Red = No |
| 29 | Role Catalog Accuracy Verified? | Dropdown: Yes, No | CF: Green = Yes, Red = No |
| 30 | SoD Matrix Completeness Confirmed? | Dropdown: Yes, No | CF: Green = Yes, Red = No |
| 31 | RBAC Metrics Validated? | Dropdown: Yes, No | CF: Green = Yes, Red = No |
| 33 | Feedback/Comments | [Manual entry] | Text, Wrap text |
| 35 | Approval Status | Dropdown: Approved, Revisions Required | CF: Green = Approved, Red = Revisions |
| 37 | Signature/Approval | [Manual entry] | Normal |
| 38 | Approval Date | [Date] | Date format |

**Conditional Formatting** (Column B, Rows 28-31, 35):
```
Rule 1: =B28="Yes"
Format: Green background

Rule 2: =B28="No"
Format: Red background

Rule 3: =B35="Approved"
Format: Green background

Rule 4: =B35="Revisions Required"
Format: Red background
```

#### CISO Review Section (Rows 42-60)

| Row | Field | Value | Format |
|-----|-------|-------|--------|
| 42 | **CISO Review & Approval** | (header) | Bold, 14pt, Navy |
| 44 | Reviewer Name | [Manual entry] | Normal |
| 45 | Reviewer Title | [Manual entry] | Normal |
| 46 | Review Date | [Date] | Date format |
| 48 | Overall RBAC Maturity Acceptable? | Dropdown: Yes, No | CF: Green = Yes, Red = No |
| 49 | SoD Compliance Acceptable? | Dropdown: Yes, No | CF: Green = Yes, Red = No |
| 50 | Critical Gaps Reviewed? | Dropdown: Yes, No | CF: Green = Yes, Red = No |
| 51 | SoD Exception Approvals Validated? | Dropdown: Yes, No | CF: Green = Yes, Red = No |
| 53 | Final Approval Status | Dropdown: Approved, Revisions Required | CF: Green = Approved, Red = Revisions |
| 55 | Comments/Recommendations | [Manual entry] | Text, Wrap text |
| 57 | Next Review Date | [Date] (Quarterly/Semi-Annual/Annual) | Date format |
| 59 | Signature/Approval | [Manual entry] | Normal |
| 60 | Approval Date | [Date] | Date format |

**Conditional Formatting** (Column B, Rows 48-51, 53):
```
Rule 1: =B48="Yes"
Format: Green background

Rule 2: =B48="No"
Format: Red background

Rule 3: =B53="Approved"
Format: Green background

Rule 4: =B53="Revisions Required"
Format: Red background
```

---

## Cell Styling Reference

### Color Palette

| Element | Background Color | Text Color | Font Size |
|---------|-----------------|------------|-----------|
| Sheet Tab (Active) | Navy (RGB: 31, 73, 125) | White | N/A |
| Header Row | Navy (RGB: 31, 73, 125) | White | 14pt |
| Subheader | Light Blue (RGB: 180, 198, 231) | Black | 12pt |
| Good/Compliant | Light Green (RGB: 198, 224, 180) | Dark Green (RGB: 70, 120, 70) | Normal |
| Warning/Review | Light Yellow (RGB: 255, 235, 156) | Dark Orange (RGB: 204, 102, 0) | Normal |
| Critical/Non-Compliant | Light Red (RGB: 255, 199, 206) | Dark Red (RGB: 192, 0, 0) | Normal |
| Neutral | White (RGB: 255, 255, 255) | Black (RGB: 0, 0, 0) | Normal |

### Font Standards

| Element | Font Family | Font Size | Bold | Italic |
|---------|-------------|-----------|------|--------|
| Main Title (Sheet 1) | Calibri | 14pt | Yes | No |
| Section Header | Calibri | 12pt | Yes | No |
| Column Header | Calibri | 11pt | Yes | No |
| Data Cell | Calibri | 11pt | No | No |
| Metric Label | Calibri | 11pt | Yes | No |
| Metric Value | Calibri | 11pt | No | No |
| Comments/Notes | Calibri | 10pt | No | No |

### Number Formats

| Data Type | Format Code | Example |
|-----------|-------------|---------|
| Percentage | `0.0%` | 85.5% |
| Percentage (No Decimal) | `0%` | 85% |
| Integer | `#,##0` | 1,234 |
| Decimal (2 places) | `#,##0.00` | 1,234.56 |
| Date | `yyyy-mm-dd` | 2025-10-15 |
| Currency | `$#,##0.00` | $1,234.56 |

---

## Freeze Panes Configuration

**All Data Sheets (Sheets 2-9)**:
- Freeze Panes: Row 2 (header row always visible when scrolling)
- Selection before freezing: Cell A2

**How to Apply**:
1. Select cell A2
2. View → Freeze Panes → Freeze Panes
3. Result: Row 1 (header) remains visible when scrolling down

---

## File Naming Convention

**Format**: `ISMS-IMP-A.5.15-16-18.S4_RoleCompliance_YYYY-MM.xlsx`

**Examples**:
- `ISMS-IMP-A.5.15-16-18.S4_RoleCompliance_2025-10.xlsx` (October 2025 assessment)
- `ISMS-IMP-A.5.15-16-18.S4_RoleCompliance_2026-01.xlsx` (January 2026 assessment)

**Versioning**:
- Monthly assessments: YYYY-MM
- Quarterly assessments: YYYY-Q1, YYYY-Q2, etc.
- Annual assessments: YYYY-Annual

---

## Monthly/Quarterly Review Cycles

### Quarterly Update Procedures

**Steps**:
1. **Update Role Assignments** (Sheet 3):
   - Export current role/group memberships from identity systems
   - Add new role assignments (rows)
   - Update Status for expired/removed assignments
   - Recalculate Users_Assigned in Sheet 2 Role_Catalog (formula auto-updates)

2. **Detect New SoD Violations** (Sheet 6):
   - Cross-reference updated Sheet 3 against Sheet 5 SoD_Matrix
   - Add new violations (users who gained conflicting roles)
   - Update Status for remediated violations
   - Remediate or justify new violations

3. **Update Direct Access Users** (Sheet 4):
   - Identify new direct access users (not in Sheet 3 roles)
   - Obtain business justifications
   - Update Last_Review_Date for quarterly reviews
   - Target: Migrate direct access users to roles

4. **Recalculate RBAC Metrics** (Sheet 7):
   - Formulas auto-update based on Sheet 2, 3, 4, 6 changes
   - Compare to previous quarter (trending?)
   - Update gap analysis if new gaps identified

5. **Update Gap Analysis** (Sheet 8):
   - Review existing gaps: Status (Open → In Progress → Closed)
   - Add new gaps identified during quarterly review
   - Verify Target_Date for overdue gaps
   - Update remediation progress

**Time Required**: 3-5 hours

---

### Semi-Annual Comprehensive Review

**Steps**:
1. **Role Catalog Review** (Sheet 2):
   - Review all roles: Still needed? Definition accurate?
   - Deactivate obsolete roles (zero users, outdated job functions)
   - Create new roles (emerging job functions)
   - Update Last_Review_Date for reviewed roles

2. **Role Owner Validation**:
   - Contact all role owners (email or meeting)
   - Confirm role definitions still accurate
   - Update role descriptions if job functions changed
   - Document role owner sign-off (evidence)

3. **Comprehensive SoD Review** (Sheet 6):
   - Review all SoD violations (Sheet 6)
   - Verify justified violations still justified (business reason valid?)
   - Verify compensating controls still in place (logging, audits)
   - Remediate violations where justification expired

4. **Role Accuracy Assessment**:
   - Sample 10-20 users per role
   - Compare Sheet 2 Role_Catalog (role definition) vs. actual access (from Sheet 2 of A.5.15-16-18.2)
   - Identify role drift (users have more/less access than role defines)
   - Remediate discrepancies (update role definitions or fix access)

5. **RBAC Adoption Improvement Plan** (Sheet 8):
   - If RBAC Adoption < 80%: Create plan to improve
   - Identify 3-5 new roles to create (common direct access patterns)
   - Target 20-30 users to migrate from direct access to roles
   - Document improvement plan in Gap Analysis

**Time Required**: 5-8 hours

---

### Annual Strategic Review

**Steps**:
1. **Comprehensive Role Catalog Review** (Sheet 2):
   - Review ALL roles (30-60 minute meetings with each role owner)
   - Validate role definitions, access mappings, business need
   - Deactivate obsolete roles, create new roles
   - Update role hierarchy if needed (junior → senior)
   - Document Last_Review_Date for all roles

2. **Complete Role Accuracy Assessment**:
   - For EVERY role: Sample 10-20 users
   - Compare role definition vs. actual access
   - Calculate role accuracy score: (Correct access / Sampled) × 100
   - Target: >= 95% role accuracy
   - Remediate all role drift

3. **SoD Matrix Review** (Sheet 5):
   - Review SoD matrix with security team and internal audit
   - Identify new conflicts (business changes, new systems)
   - Update risk levels (fraud risk changed?)
   - Document new mitigation controls
   - Validate with regulatory requirements (FINMA, SOX, etc.)

4. **RBAC Maturity Strategic Plan**:
   - Review RBAC Maturity trend (Sheet 7): Improving? Stagnant?
   - If Maturity < 80: Create 12-month improvement plan
   - Target: RBAC adoption >= 90%, SoD violations = 0, Role Review = 100%
   - Identify technology investments (IAM platforms, role mining)
   - Document strategic plan in Gap Analysis

5. **Audit Preparation**:
   - Ensure all evidence collected (Sheet 9)
   - Verify evidence accessible (SharePoint, not laptops)
   - Confirm approvals up to date (CISO sign-off)
   - Prepare executive summary (one-page RBAC maturity overview)

**Time Required**: 8-12 hours

---

## Integration Points

### Data Dependencies

**Inputs from Other Assessments**:
1. **From ISMS-IMP-A.5.15-16-18.S1 (User Inventory)**:
   - Total user count (for RBAC adoption denominator)
   - User status (active/inactive)
   - User type (employee/contractor)

2. **From ISMS-IMP-A.5.15-16-18.S2 (Access Rights Matrix)**:
   - Actual user access (for role accuracy validation)
   - System-level access (Read/Write/Admin)
   - Direct access identification

3. **From ISMS-IMP-A.5.15-16-18.S3 (Access Review Results)**:
   - Role review dates (when roles last validated)
   - Review findings (role accuracy)
   - Role owner sign-offs

**Outputs to Other Assessments**:
1. **To ISMS-IMP-A.5.15-16-18.S5 (IAM Governance Dashboard)**:
   - RBAC Adoption Rate (%)
   - SoD Violation Count (Unresolved, Justified, Remediated)
   - Role Review Compliance (%)
   - Overall RBAC Maturity Score (0-100)
   - Critical Gaps (Unresolved SoD, Low RBAC Adoption)

2. **To ISMS-IMP-A.5.15-16-18.S3 (Access Review Results)**:
   - Role definitions (baseline for role-based reviews)
   - Role owners (who reviews role assignments)
   - Role-based review scope (review by role vs. individual users)

### Cross-Reference Formulas

**Example: Role Catalog Sheet 2 references Role Assignments Sheet 3**:
```
=COUNTIF(Role_Assignments!C:C, B2)
```
This formula in Sheet 2, Column G (Users_Assigned) counts how many times the role name (B2) appears in Sheet 3, Column C (Role_Name).

**Example: RBAC Metrics Sheet 7 references multiple sheets**:
```
Total Users = Role_Assignments!A207 + Direct_Access_Users!A43
```
This formula combines user counts from Sheet 3 (Role Assignments) and Sheet 4 (Direct Access Users).

---

**END OF PART II: TECHNICAL SPECIFICATION**
