# ISMS-IMP-A.5.15-16-18-S5: IAM Assessment Procedures
## Implementation Guide for IAM Compliance Measurement

**Document ID**: ISMS-IMP-A.5.15-16-18-S5  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Security Manager / IAM Manager  
**Status**: Active

---

## Document Purpose

This implementation guide provides **step-by-step procedures** for assessing IAM control effectiveness and generating compliance evidence in accordance with ISO/IEC 27001:2022 Controls A.5.15, A.5.16, and A.5.18.

**Target Audience**: Security team, IAM team, internal audit, external auditors

**Prerequisites**:
- All IMP guides implemented (S1-S4)
- Assessment scripts ready (generate_iam_*.py)
- Data sources accessible (identity systems, HR system, access review results)

---

## 1. Assessment Overview

### 1.1 IAM Assessment Framework

**Assessment Structure** (6 workbooks + 1 dashboard):

```
IAM ASSESSMENT FRAMEWORK
├── Workbook 1: User Inventory & Lifecycle Compliance (A.5.16)
├── Workbook 2: Access Rights Matrix (A.5.18)
├── Workbook 3: Access Review Results (A.5.15 + A.5.18)
├── Workbook 4: Role Compliance & SoD (A.5.15 + A.5.18)
├── Workbook 5: Lifecycle Compliance Detailed (A.5.16)
└── Dashboard: IAM Governance Overview (All controls)
```

**Assessment Purpose**:
- Demonstrate IAM control effectiveness
- Identify compliance gaps
- Support audit evidence collection
- Enable continuous monitoring

---

### 1.2 Data Sources

**Required Data**:

| Data Source | Purpose | Examples |
|-------------|---------|----------|
| **Identity Systems** | User inventory, group memberships | Active Directory, Azure AD, Okta |
| **HR System** | Employee lifecycle events | Workday, SAP SuccessFactors, ADP |
| **Access Review Platform** | Review results, findings | GRC tool, spreadsheets, ServiceNow |
| **Ticketing System** | Access requests, approvals | ServiceNow, Jira |
| **Audit Logs** | Access provisioning/deprovisioning events | SIEM, identity system logs |

---

### 1.3 Assessment Frequency

| Assessment Type | Frequency | Purpose |
|----------------|-----------|---------|
| **Monthly** | User inventory updates, orphaned account scans | Operational monitoring |
| **Quarterly** | Access review compliance, role compliance | Tactical monitoring |
| **Annual** | Comprehensive IAM assessment (all 6 workbooks) | Strategic review, audit preparation |

---

## 2. Workbook 1: User Inventory & Lifecycle Compliance

### 2.1 Data Collection

**Objective**: Generate complete user inventory with lifecycle compliance metrics.

**Step 1: Extract User Data from Identity Systems**

**Active Directory Example**:
```powershell
# Export all users
Get-ADUser -Filter * -Properties * | 
  Select-Object SamAccountName, Name, EmailAddress, Department, Title, Manager, 
    Created, Enabled, LastLogonDate, DistinguishedName | 
  Export-Csv "user_inventory_AD.csv" -NoTypeInformation
```

**Azure AD Example**:
```powershell
# Connect and export
Connect-AzureAD
Get-AzureADUser -All $true | 
  Select-Object UserPrincipalName, DisplayName, Department, JobTitle, 
    UserType, AccountEnabled, LastSignInDateTime |
  Export-Csv "user_inventory_AzureAD.csv" -NoTypeInformation
```

**Output**: User inventory CSV files

---

**Step 2: Extract Lifecycle Events from HR System**

**Required Fields**:
- Employee ID
- Hire Date
- Termination Date (if applicable)
- Job Title
- Department
- Manager
- Status (Active, Terminated, On Leave)

**Sample CSV Format**:
```csv
employee_id,name,email,hire_date,termination_date,department,manager,status
12345,Alice Smith,alice.smith@company.com,2025-06-01,,Sales,Jane Doe,Active
67890,Bob Jones,bob.jones@company.com,2023-01-15,2026-01-10,IT,John Smith,Terminated
```

---

**Step 3: Run Assessment Script**

```bash
python3 generate_iam_1_user_inventory.py \
  --identity-export user_inventory_AD.csv \
  --hr-export hr_employees.csv \
  --output User_Inventory_Assessment.xlsx
```

**Script Actions**:
1. Load identity system data
2. Load HR system data
3. Cross-reference (identify orphaned accounts)
4. Calculate lifecycle compliance metrics (provisioning/deprovisioning timeliness)
5. Generate Excel workbook with 9 sheets

---

### 2.2 Workbook Structure

**Sheet 1: Instructions & Legend**
- How to use workbook
- Color codes (green/yellow/red)
- Data sources and collection dates

**Sheet 2: User_Inventory** (100 sample users)
- Complete user list with attributes
- User type classification
- Status (active/disabled)

**Sheet 3: Employee_Lifecycle** (50 employees)
- Provisioning compliance (access by start date)
- Deprovisioning compliance (access removed by termination date)

**Sheet 4: Contractor_Lifecycle** (30 contractors)
- Contract-based lifecycle
- Time-bound access compliance

**Sheet 5: Service_Accounts** (20 accounts)
- Non-human account inventory
- Ownership assignment

**Sheet 6: Orphaned_Accounts** (detection results)
- Accounts without valid owners
- Remediation tracking

**Sheet 7: Lifecycle_Metrics** (summary)
- On-time provisioning rate
- On-time deprovisioning rate
- Average delays

**Sheet 8: Gap_Analysis**
- Late provisioning instances
- Late deprovisioning instances
- Orphaned accounts list

**Sheet 9: Evidence_Register** (50 items)
- Evidence catalog for A.5.16

**Sheet 10: Approval_Sign_Off**
- 3-level approval workflow

---

### 2.3 Key Metrics

**Lifecycle Timeliness**:
- **Provisioning On-Time** = (Provision Date ≤ Start Date) → Green
- **Deprovisioning On-Time** = (Disable Date ≤ Termination Date + 1 day) → Green

**Orphaned Accounts**:
- **Orphaned** = User not in HR system OR Last login > 90 days

**Compliance Scoring**:
- **A.5.16 Score** = (Provisioning Timeliness + Deprovisioning Timeliness + Orphaned Account Remediation) / 3

---

## 3. Workbook 2: Access Rights Matrix

### 3.1 Data Collection

**Objective**: Map users to systems to access levels.

**Step 1: Export Access Data**

**From Identity Systems** (group memberships, role assignments)
**From Applications** (application-specific access)
**From Ticketing System** (access request approvals, justifications)

**Sample Data Format**:
```csv
user_id,user_name,system_name,access_level,granted_date,granted_by,justification,last_review_date
alice.smith,Alice Smith,CRM,Read/Write,2025-06-15,Manager,Sales rep role,2026-01-10
bob.jones,Bob Jones,Finance,Admin,2023-01-20,CFO,Finance manager,2025-12-15
```

---

**Step 2: Run Assessment Script**

```bash
python3 generate_iam_2_access_rights_matrix.py \
  --access-export access_data.csv \
  --role-export role_assignments.csv \
  --output Access_Rights_Matrix.xlsx
```

---

### 3.2 Workbook Structure

**9 sheets**:
1. Instructions & Legend
2. Access_Matrix (user × system mapping)
3. Role_Assignments (RBAC assignments)
4. Group_Memberships (detailed group data)
5. Privileged_Access (admin/elevated access tracking)
6. Access_Documentation (justification completeness)
7. Coverage_Analysis (system-level statistics)
8. Gap_Analysis (missing documentation, excessive access)
9. Evidence_Register
10. Approval_Sign_Off

---

### 3.3 Key Metrics

**Documentation Completeness**:
- % Access with business justification
- % Access with approval record

**Privileged Access**:
- Count of admin-level access
- Privileged users list

**Compliance Scoring**:
- **A.5.18 Score** = (Documentation Completeness + RBAC Adoption + Privileged Access Controls) / 3

---

## 4. Workbook 3: Access Review Results

### 4.1 Data Collection

**Objective**: Track access review completion and findings.

**Step 1: Collect Review Data**

**From Review Tool** (GRC, spreadsheets):
- Review schedule
- Review completion status
- Review findings (confirm/remove/change)

**Sample Data**:
```csv
review_id,system_name,review_period,reviewer,due_date,completion_date,users_reviewed,access_confirmed,access_removed
REV-001,Finance System,Q1 2026,CFO,2026-01-31,2026-01-28,30,27,3
REV-002,CRM,Q1 2026,VP Sales,2026-02-15,2026-02-12,100,95,5
```

---

**Step 2: Run Assessment Script**

```bash
python3 generate_iam_3_access_review_results.py \
  --review-schedule review_schedule.csv \
  --review-results review_results.csv \
  --output Access_Review_Results.xlsx
```

---

### 4.2 Workbook Structure

**9 sheets**:
1. Instructions & Legend
2. Review_Schedule (annual calendar, 80 reviews)
3. Review_Completion (execution tracking)
4. Review_Findings (60 findings)
5. Overdue_Reviews (past due)
6. Reviewer_Performance (responsiveness)
7. Review_Metrics (completion rate, removal rate)
8. Gap_Analysis (incomplete reviews, unaddressed findings)
9. Evidence_Register
10. Approval_Sign_Off

---

### 4.3 Key Metrics

**Review Completion**:
- Completion Rate = (Completed / Total) × 100
- On-Time Rate = (Completed On-Time / Total) × 100

**Review Effectiveness**:
- Access Removal Rate = (Access Removed / Users Reviewed) × 100
- Typical range: 5-15% (healthy finding rate)

---

## 5. Workbook 4: Role Compliance & SoD

### 5.1 Data Collection

**Objective**: Assess RBAC adoption and SoD compliance.

**Step 1: Export Role Data**

```csv
# Role catalog
role_id,role_name,description,owner,users_assigned,last_review_date
ROLE-001,Sales Representative,Manages customers,VP Sales,15,2026-01-01

# SoD matrix
conflict_id,role_a,role_b,risk_level,exception_allowed
SOD-001,Developer,Production Admin,Critical,No
SOD-002,IT Admin,Security Admin,High,Yes

# User role assignments
user_id,user_name,role_name,assignment_date
alice.smith,Alice Smith,Sales Representative,2025-06-01
```

---

**Step 2: Run Assessment Script**

```bash
python3 generate_iam_4_role_compliance.py \
  --role-catalog roles.csv \
  --sod-matrix sod_matrix.csv \
  --user-roles user_roles.csv \
  --output Role_Compliance.xlsx
```

---

### 5.2 Workbook Structure

**9 sheets**:
1. Instructions & Legend
2. Role_Catalog (30 roles)
3. Role_Assignments (80 users with roles)
4. Direct_Access_Users (20 users without roles)
5. SoD_Matrix (6 conflict pairs)
6. SoD_Violations (5 violations)
7. RBAC_Metrics (adoption rate, coverage)
8. Gap_Analysis (low adoption, unresolved violations)
9. Evidence_Register
10. Approval_Sign_Off

---

### 5.3 Key Metrics

**RBAC Adoption**:
- RBAC Adoption Rate = (Users with Roles / Total Users) × 100
- Target: 80%+

**SoD Compliance**:
- SoD Violation Count (unapproved)
- Target: 0

---

## 6. Workbook 5: Lifecycle Compliance Detailed

### 6.1 Data Collection

**Objective**: Detailed joiner/mover/leaver compliance assessment.

**Step 1: Export Lifecycle Events**

```csv
# Joiner events
user_id,name,hire_date,provision_date,days_to_provision,compliance
E12345,Alice Smith,2025-06-01,2025-05-30,-1,Compliant

# Leaver events
user_id,name,termination_date,disable_date,days_to_disable,compliance
E67890,Bob Jones,2026-01-10,2026-01-10,0,Compliant
```

---

**Step 2: Run Assessment Script**

```bash
python3 generate_iam_5_lifecycle_compliance.py \
  --joiner-data joiners.csv \
  --mover-data movers.csv \
  --leaver-data leavers.csv \
  --output Lifecycle_Compliance_Detailed.xlsx
```

---

### 6.2 Workbook Structure

**10 sheets**:
1. Instructions & Legend
2. Joiner_Compliance (40 new hires)
3. Mover_Compliance (20 role changes)
4. Leaver_Compliance (30 terminations)
5. Contractor_Lifecycle (25 contractors)
6. Orphaned_Account_Remediation (15 accounts)
7. Process_Timeliness_Metrics (summary)
8. HR_Integration_Status (sync health)
9. Gap_Analysis (late events, failures)
10. Evidence_Register
11. Approval_Sign_Off

---

### 6.3 Key Metrics

**Joiner/Mover/Leaver Timeliness**:
- On-Time Provisioning Rate
- On-Time Deprovisioning Rate
- Average delay (days)

**Targets**:
- Provisioning: ≥95% on-time
- Deprovisioning: ≥98% on-time (higher bar for security)

---

## 7. Dashboard: IAM Governance Overview

### 7.1 Dashboard Purpose

**Objective**: Consolidate all 5 workbooks into executive summary.

**Audience**: CISO, Executive Team, Board

**Dashboard Sections**:
1. Executive Summary (high-level KPIs)
2. Compliance Scores (A.5.15, A.5.16, A.5.18)
3. Summary from each workbook (WB1-WB5)
4. Gap Consolidation (all gaps from WB1-WB5)
5. Action Plan (prioritized remediation)
6. Approval Sign-Off

---

### 7.2 Data Consolidation

**Prerequisites**:
- All 5 workbooks generated and normalized
- Files named: User_Inventory.xlsx, Access_Matrix.xlsx, Review_Results.xlsx, Role_Compliance.xlsx, Lifecycle_Compliance.xlsx

**Run Dashboard Script**:
```bash
python3 generate_iam_dashboard.py \
  --workbooks-dir /path/to/workbooks/ \
  --output IAM_Governance_Dashboard.xlsx
```

**Script Actions**:
1. Load all 5 workbooks
2. Extract key metrics from each
3. Calculate overall IAM maturity score
4. Consolidate gaps
5. Prioritize actions
6. Generate executive dashboard

---

### 7.3 Dashboard Structure

**11 sheets**:
1. Instructions
2. Executive_Summary (KPIs, maturity score)
3. Compliance_Scores (A.5.15/16/18 scores)
4. WB1_User_Inventory_Summary
5. WB2_Access_Matrix_Summary
6. WB3_Review_Summary
7. WB4_Role_Summary
8. WB5_Lifecycle_Summary
9. Gap_Consolidation (60 gaps from all workbooks)
10. Action_Plan (30 prioritized actions)
11. Approval_Sign_Off

---

### 7.4 Overall IAM Maturity Score

**Calculation**:
```
Overall IAM Maturity = (A.5.15 Score + A.5.16 Score + A.5.18 Score) / 3

Where:
- A.5.15 Score = Access control policy compliance (SoD, exceptions, reviews)
- A.5.16 Score = Lifecycle compliance (joiner/mover/leaver timeliness)
- A.5.18 Score = Access rights compliance (RBAC adoption, review completion)
```

**Maturity Levels**:
- **90-100**: Optimizing (best-in-class)
- **80-89**: Defined (strong)
- **70-79**: Managed (adequate)
- **60-69**: Repeatable (needs improvement)
- **<60**: Initial (significant gaps)

---

## 8. Assessment Execution Procedures

### 8.1 Monthly Assessment (Operational)

**Objective**: Monitor operational metrics.

**Activities**:
1. Update user inventory (new hires, terminations)
2. Scan for orphaned accounts (automated script)
3. Review deprovisioning timeliness (terminations from last 30 days)
4. Generate brief summary report (1 page)

**Deliverable**: Monthly operational dashboard (distributed to IAM team)

**Timeline**: 1st week of each month

---

### 8.2 Quarterly Assessment (Tactical)

**Objective**: Assess quarterly metrics and trends.

**Activities**:
1. Run WB3: Access Review Results (review completion for quarter)
2. Run WB4: Role Compliance (RBAC adoption trends)
3. Privilege creep scan (detect excessive access)
4. Generate quarterly report (5-10 pages)

**Deliverable**: Quarterly IAM report (distributed to Security Manager, CISO)

**Timeline**: 2nd week after quarter end

---

### 8.3 Annual Assessment (Strategic)

**Objective**: Comprehensive IAM assessment for audit and strategic planning.

**Activities**:
1. Run all 5 workbooks (WB1-WB5)
2. Normalize workbook files (standardize filenames)
3. Run dashboard consolidation script
4. Generate annual report (20-30 pages)
5. Present to CISO and Executive Team

**Deliverable**:
- 6 Excel workbooks (WB1-WB5 + Dashboard)
- Annual IAM assessment report (PDF)
- Presentation deck (PowerPoint) for executives

**Timeline**: 4 weeks (1 week per workbook, 1 week for dashboard and reporting)

---

## 9. Evidence Collection for Audits

### 9.1 Audit Evidence Mapping

**A.5.15 (Access Control) Evidence**:
- Access control policy document (POL-S2)
- SoD matrix and violation reports (WB4)
- Exception approval records (WB3)
- Access review results (WB3)

**A.5.16 (Identity Management) Evidence**:
- User inventory (WB1)
- Provisioning/deprovisioning timeliness reports (WB1, WB5)
- Orphaned account detection and remediation (WB1)
- HR integration documentation (IMP-S2)

**A.5.18 (Access Rights) Evidence**:
- Access rights matrix (WB2)
- Role catalog and assignments (WB4)
- Access review completion reports (WB3)
- Access removal audit logs (WB5)

---

### 9.2 Audit Preparation Checklist

**4 Weeks Before Audit**:
- [ ] Run annual comprehensive assessment (all 5 workbooks + dashboard)
- [ ] Review all evidence for completeness
- [ ] Identify and remediate any critical gaps
- [ ] Prepare audit evidence package

**2 Weeks Before Audit**:
- [ ] Conduct internal audit dry run (spot-check evidence)
- [ ] Update any outdated documentation
- [ ] Prepare audit response team (CISO, Security Manager, IAM Manager)

**During Audit**:
- [ ] Provide evidence package to auditors
- [ ] Answer auditor questions
- [ ] Track any audit findings
- [ ] Commit to remediation timelines

**Post-Audit**:
- [ ] Address audit findings (within agreed timeline)
- [ ] Update assessment procedures based on lessons learned

---

## 10. Continuous Monitoring

### 10.1 Automated Monitoring

**Objective**: Detect issues proactively, not reactively.

**Automated Alerts** (daily/weekly):

| Alert | Trigger | Recipient | Action |
|-------|---------|-----------|--------|
| **Orphaned Account Detected** | User not in HR system | IAM Team | Investigate, disable account |
| **Deprovisioning Overdue** | Termination >24h ago, account still active | IAM Team | Investigate, disable immediately |
| **SoD Violation Detected** | User assigned conflicting roles | Security Team | Investigate, escalate to CISO |
| **Privileged Access Added** | User granted admin access | Security Team | Verify approval, document |
| **Inactive Account** | No login in 90 days | Manager | Review, remove if not needed |

**Implementation**:
- Scheduled scripts (cron jobs, Windows Task Scheduler)
- Integration with SIEM (alerts for critical events)
- Email notifications to responsible teams

---

### 10.2 Dashboard Refresh

**Objective**: Keep dashboard current.

**Refresh Schedule**:
- **Monthly**: User inventory metrics
- **Quarterly**: Access review metrics, role compliance
- **Annual**: Full assessment refresh

**Automated Refresh** (optional):
- Set up automated scripts to refresh dashboard monthly
- Distribute updated dashboard to CISO
- Highlight changes from previous month (trend analysis)

---

## 11. Success Criteria

**How to Know IAM Assessment is Working**:

✅ **Assessment Operational**:
- All 5 workbooks generate successfully
- Dashboard consolidates data correctly
- Metrics calculated accurately

✅ **Evidence Available**:
- Audit evidence readily available (no scrambling)
- Evidence up-to-date (≤30 days old)
- Evidence complete (all controls covered)

✅ **Gaps Identified & Remediated**:
- Monthly orphaned account scans detect 0 orphaned accounts
- Quarterly reviews detect and remediate privilege creep
- Annual assessment shows improving maturity score (year-over-year)

✅ **Compliance Demonstrated**:
- No audit findings on IAM controls
- Regulatory requirements met (FADP, GDPR, FINMA)
- Executive confidence in IAM program

---

## 12. Next Steps

### 12.1 After Implementing IAM Assessment

1. ✅ **IAM assessment procedures established** (this implementation guide completed)
   
2. ➡️ **Next**: Generate assessment scripts
   - Create 8 Python scripts (generate_iam_*.py)
   - Test scripts with sample data
   - Validate workbook output (formulas, conditional formatting, UTF-8)
   
3. ➡️ **Then**: Execute first assessment
   - Run all 5 workbook scripts
   - Generate dashboard
   - Present results to CISO
   - Identify and prioritize gaps

4. ➡️ **Finally**: Continuous improvement
   - Monthly operational monitoring
   - Quarterly tactical assessments
   - Annual strategic reviews
   - Evolve assessment based on lessons learned

---

## Document Approval

**Prepared By**: [Name], [Title] - [Date]  
**Reviewed By**: [Name], [Title] - [Date]  
**Approved By**: [Name], CISO - [Date]

**Next Review Date**: [Date + 12 months]

**Version History**:
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial implementation guide for IAM assessment |

---

**END OF IMPLEMENTATION GUIDE S5 - IAM ASSESSMENT PROCEDURES**

**Next Documents**: Assessment Scripts (generate_iam_*.py - 8 scripts)