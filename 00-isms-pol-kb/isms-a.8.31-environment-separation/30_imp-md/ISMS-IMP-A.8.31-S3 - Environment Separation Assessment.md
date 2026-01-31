# ISMS-IMP-A.8.31-S3
## Environment Separation Assessment & Compliance Dashboard

**Document ID**: ISMS-IMP-A.8.31-S3  
**Title**: Environment Separation Assessment & Compliance Dashboard  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Information Security Manager | Initial assessment & dashboard guide |

**Review Cycle**: Quarterly (aligned with assessment schedule)  
**Approvers**: CISO, IT Operations Manager, Information Security Manager  
**Related Policy**: ISMS-POL-A.8.31-S3 (Assessment & Evidence Framework)

---

## 1. Purpose and Scope

### 1.1 Overview

This implementation guide provides **step-by-step procedures** for conducting comprehensive environment separation assessments and generating executive compliance dashboards in support of ISO/IEC 27001:2022 Control A.8.31.

**Objectives**:
- Conduct systematic environment separation assessments
- Aggregate assessment data from multiple sources
- Generate executive-level compliance dashboards
- Track remediation progress over time
- Prepare evidence packages for audits

**Assessment Components**:
1. **Architecture Assessment** (ISMS-IMP-A.8.31.1) - Network, infrastructure, data, credential separation
2. **Access Control Assessment** (ISMS-IMP-A.8.31.2) - User permissions, production access, break-glass
3. **Compliance Dashboard** (ISMS-IMP-A.8.31.3) - Executive summary and trend analysis

### 1.2 Target Audience

- **CISO / Executive Management**: Strategic oversight and compliance status
- **Information Security Team**: Tactical assessment execution
- **IT Operations**: Remediation implementation
- **Auditors**: Compliance verification
- **Risk Management**: Risk treatment tracking

---

## 2. Assessment Methodology

### 2.1 Assessment Lifecycle

**Quarterly Assessment Cycle**:

```
Week 1: Planning & Preparation
  ↓
Week 2-3: Data Collection
  ├─ Architecture Assessment (ISMS-IMP-A.8.31.1)
  ├─ Access Control Assessment (ISMS-IMP-A.8.31.2)
  └─ Evidence Gathering
  ↓
Week 4: Analysis & Dashboard Generation
  ├─ Gap identification
  ├─ Compliance scoring
  ├─ Dashboard generation (ISMS-IMP-A.8.31.3)
  └─ Trend analysis
  ↓
Week 5: Reporting & Remediation Planning
  ├─ Executive briefing
  ├─ Remediation prioritization
  └─ Action plan approval
  ↓
Weeks 6-12: Remediation Execution
  └─ Continuous monitoring
```

### 2.2 Assessment Phases

**Phase 1: Planning**
- Schedule assessment activities
- Assign assessment team roles
- Identify systems in scope
- Prepare assessment tools (workbooks)

**Phase 2: Architecture Assessment**
- Complete ISMS-IMP-A.8.31.1 workbook
- Review network diagrams and firewall rules
- Verify infrastructure separation (cloud accounts, databases)
- Validate data separation (no prod data in dev/test)
- Audit credential separation (production in PAM vault)
- Test network isolation (penetration testing)

**Phase 3: Access Control Assessment**
- Complete ISMS-IMP-A.8.31.2 workbook
- Document user-environment access matrix
- **CRITICAL**: Verify ZERO developer production access
- Audit production credential usage
- Review break-glass access logs
- Verify MFA enforcement for production

**Phase 4: Dashboard Generation**
- Aggregate data from Phases 2 and 3
- Calculate compliance scores
- Generate executive dashboard (ISMS-IMP-A.8.31.3)
- Perform trend analysis (if historical data available)
- Identify top gaps and risks

**Phase 5: Reporting & Action Planning**
- Present dashboard to CISO and executive management
- Prioritize remediation actions (risk-based)
- Assign owners and target dates
- Track remediation progress

---

## 3. Data Collection Procedures

### 3.1 Architecture Data Collection

**Network Configuration Data**:
```bash
# On-premises firewall rules
iptables -L -n > firewall_rules_$(date +%Y%m%d).txt

# AWS security groups
aws ec2 describe-security-groups --profile prod > aws_sg_prod.json
aws ec2 describe-security-groups --profile dev > aws_sg_dev.json

# Azure network security groups
az network nsg list --subscription prod-sub > azure_nsg_prod.json
az network nsg list --subscription dev-sub > azure_nsg_dev.json

# GCP firewall rules
gcloud compute firewall-rules list --project=prod-project > gcp_fw_prod.txt
gcloud compute firewall-rules list --project=dev-project > gcp_fw_dev.txt
```

**Infrastructure Inventory Data**:
```bash
# AWS resources per account
aws ec2 describe-instances --profile prod --query 'Reservations[*].Instances[*].[InstanceId,Tags]' > aws_ec2_prod.json
aws rds describe-db-instances --profile prod > aws_rds_prod.json
aws s3api list-buckets --profile prod > aws_s3_prod.json

# Azure resources per subscription
az vm list --subscription prod-sub > azure_vm_prod.json
az sql server list --subscription prod-sub > azure_sql_prod.json
az storage account list --subscription prod-sub > azure_storage_prod.json

# GCP resources per project
gcloud compute instances list --project=prod-project --format=json > gcp_vm_prod.json
gcloud sql instances list --project=prod-project --format=json > gcp_sql_prod.json
gcloud storage buckets list --project=prod-project --format=json > gcp_storage_prod.json
```

**Credential Audit Data**:
```bash
# List users with access to PAM vault (example: CyberArk)
# Export from PAM system (vendor-specific)

# AWS IAM users per account
aws iam list-users --profile prod > aws_iam_users_prod.json
aws iam list-users --profile dev > aws_iam_users_dev.json

# Azure AD users with subscription access
az role assignment list --subscription prod-sub --query "[].principalName" > azure_users_prod.txt
az role assignment list --subscription dev-sub --query "[].principalName" > azure_users_dev.txt
```

### 3.2 Access Control Data Collection

**User-Environment Access Matrix**:
```bash
# Export from IAM system (Active Directory, Okta, etc.)
# Example: LDAP query for group memberships
ldapsearch -x -H ldap://dc.example.com -D "CN=admin,DC=example,DC=com" \
  -b "OU=Groups,DC=example,DC=com" "(objectClass=group)" member > ad_groups.ldif

# AWS IAM role assignments
for account in dev test staging prod; do
  aws organizations list-accounts-for-parent \
    --parent-id ou-${account} > aws_accounts_${account}.json
done

# Azure RBAC assignments
for sub in dev-sub test-sub prod-sub; do
  az role assignment list --subscription $sub > azure_rbac_${sub}.json
done
```

**Production Access Logs**:
```bash
# AWS CloudTrail logs (production account)
aws cloudtrail lookup-events \
  --profile prod \
  --start-time $(date -u -d '30 days ago' +%Y-%m-%dT%H:%M:%S) \
  --max-items 1000 > cloudtrail_prod_30days.json

# Azure Activity Logs (production subscription)
az monitor activity-log list \
  --subscription prod-sub \
  --start-time $(date -u -d '30 days ago' +%Y-%m-%dT%H:%M:%S) \
  --max-events 1000 > azure_activity_prod_30days.json

# Filter for developer access to production (should be ZERO)
cat cloudtrail_prod_30days.json | jq '.Events[] | select(.Username | contains("developer"))' > dev_prod_access.json
```

**Break-Glass Access Logs**:
```bash
# Extract from break-glass activation/revocation logs
cat /var/log/breakglass.log | grep "$(date +%Y)" > breakglass_usage_2026.log

# Parse structured data
cat breakglass_usage_2026.log | \
  awk '/ACTIVATED/{print $1, $2, $6, $9}' > breakglass_summary.txt
```

### 3.3 Evidence Collection Checklist

**Required Evidence**:
- [ ] Network diagrams (all environments)
- [ ] Firewall rule exports (showing default deny)
- [ ] Cloud account/subscription inventory
- [ ] Infrastructure inventory (compute, database, storage)
- [ ] User-environment access matrix (current)
- [ ] Production access logs (past 90 days minimum)
- [ ] Break-glass access logs (past 12 months)
- [ ] MFA enforcement policies (screenshots or exports)
- [ ] PAM vault credential list (production)
- [ ] Penetration test results (network isolation)
- [ ] Configuration drift reports (staging vs production)
- [ ] Access review sign-offs (monthly/quarterly)

---

## 4. Compliance Scoring Methodology

### 4.1 Scoring Criteria

**Overall Compliance Score** = Weighted average of:

| Component | Weight | Description |
|-----------|--------|-------------|
| Network Separation | 25% | VLANs/VPCs, firewall rules, network isolation |
| Infrastructure Separation | 20% | Separate servers, cloud accounts, databases |
| Data Separation | 30% | **CRITICAL** - No prod data in dev/test |
| Credential Separation | 15% | Separate credentials, production in PAM |
| Access Control | 10% | User permissions, production access restrictions |

**Scoring Scale**:
- **100%**: Fully compliant, no gaps identified
- **90-99%**: Substantially compliant, minor gaps
- **70-89%**: Partially compliant, moderate gaps requiring remediation
- **50-69%**: Significant gaps, major remediation required
- **<50%**: Non-compliant, critical gaps requiring immediate action

### 4.2 Component Scoring

**Network Separation Score**:
```
Score = (Environments with proper network isolation / Total environments) × 100%

Criteria:
✅ Separate VLAN/VPC per environment
✅ Firewall rules prevent cross-environment traffic (except authorized)
✅ Penetration test confirms isolation
✅ No VPC peering between dev/test and production
```

**Infrastructure Separation Score**:
```
Score = (Environments with separate infrastructure / Total environments) × 100%

Criteria:
✅ Separate cloud accounts/subscriptions
✅ Separate database instances
✅ Separate storage buckets
✅ No shared compute resources between prod and non-prod
```

**Data Separation Score** (CRITICAL):
```
Score = 100% if ZERO production data in dev/test, otherwise 0%

Criteria:
❌ ANY production data in dev/test = CRITICAL VIOLATION = 0%
✅ Synthetic/anonymized data only in dev/test = 100%
```

**Credential Separation Score**:
```
Score = (Unique credentials per environment / Total credentials) × 100%

Criteria:
✅ Production credentials in PAM vault
✅ No shared passwords across environments
✅ Credential rotation schedule followed
```

**Access Control Score**:
```
Score = (Compliant access controls / Total access controls) × 100%

Criteria:
✅ ZERO developer production access (except break-glass)
✅ MFA enabled for all production accounts
✅ Access reviews completed on time
✅ Break-glass procedures documented and followed
```

### 4.3 Compliance Status Thresholds

**Compliance Status Determination**:
- **✅ Compliant**: Overall score ≥ 90%
- **⚠️ Partially Compliant**: Overall score 70-89%
- **❌ Non-Compliant**: Overall score < 70%
- **🔴 Critical Violation**: ANY production data in dev/test OR ANY unauthorized developer production access

---

## 5. Dashboard Generation

### 5.1 Executive Dashboard Components

Use the provided dashboard generator: **generate_dashboard_environment_separation.py**

**Dashboard Sections**:

1. **Executive Summary** (Single-page overview)
   - Overall compliance score (gauge/progress bar)
   - Compliance status (✅ ⚠️ ❌ 🔴)
   - Critical findings count
   - Top 5 gaps requiring attention

2. **Environment Separation Status**
   - Compliance by component (network, infrastructure, data, credentials, access)
   - Per-environment status (dev, test, staging, production)
   - Trend over time (if historical data available)

3. **Access Control Summary**
   - Developers with production access (should be ZERO)
   - Production users with MFA (should be 100%)
   - Break-glass usage (past quarter)
   - Cross-environment access attempts (blocked)

4. **Gap Analysis & Remediation**
   - Gap inventory by severity (Critical, High, Medium, Low)
   - Remediation status (Open, In Progress, Resolved)
   - Aging analysis (gaps open > 30 days)
   - Owner assignment

5. **Risk Register**
   - Identified risks from gaps
   - Risk severity and likelihood
   - Risk treatment status
   - Residual risk

6. **Evidence Summary**
   - Evidence collected for audit
   - Evidence completeness (%)
   - Missing evidence items

7. **Trend Analysis** (Quarterly)
   - Compliance score over time
   - Gap closure rate
   - New gaps identified
   - Remediation velocity

### 5.2 Dashboard Generation Process

**Step 1: Normalize Assessment Files**

```bash
# Use normalization script to prepare source data
python3 normalize_assessment_files_a831.py

# This creates:
# - ISMS-IMP-A.8.31.1.xlsx (architecture assessment)
# - ISMS-IMP-A.8.31.2.xlsx (access control assessment)
```

**Step 2: Generate Dashboard**

```bash
# Run dashboard generator
python3 generate_dashboard_environment_separation.py

# This creates:
# - ISMS-IMP-A.8.31.3_Environment_Separation_Dashboard_YYYYMMDD.xlsx
```

**Step 3: Review and Customize**

- Review auto-calculated compliance scores
- Add narrative context to findings
- Customize trend analysis (if historical data available)
- Add executive commentary

**Step 4: Distribute**

- Present to CISO and executive management
- Distribute to IT operations for remediation planning
- Share with auditors for compliance verification
- Archive for historical trend analysis

---

## 6. Trend Analysis

### 6.1 Historical Data Collection

**Quarterly Snapshots**:
- Save completed dashboard after each quarterly assessment
- Track compliance scores over time
- Monitor gap closure rate
- Measure remediation effectiveness

**Metrics to Track**:
- Overall compliance score (trend over 4+ quarters)
- Compliance by component (network, infrastructure, data, credentials, access)
- Gap count (total, by severity)
- Mean time to remediation (MTTR)
- New gaps introduced vs. gaps closed

### 6.2 Trend Visualization

**Compliance Score Trend**:
```
Q1 2025: 75% (⚠️ Partial)
Q2 2025: 82% (⚠️ Partial) ↑ 7%
Q3 2025: 88% (⚠️ Partial) ↑ 6%
Q4 2025: 93% (✅ Compliant) ↑ 5%
Q1 2026: 95% (✅ Compliant) ↑ 2%

Trend: ✅ Improving (consistent upward trajectory)
Target: Maintain ≥90% compliance
```

**Gap Closure Analysis**:
```
Q4 2025:
  Opened: 3 new gaps
  Closed: 8 gaps
  Net: -5 gaps (improvement)
  
Q1 2026:
  Opened: 2 new gaps
  Closed: 4 gaps
  Net: -2 gaps (continued improvement)

Average Time to Close:
  Critical: 15 days
  High: 30 days
  Medium: 60 days
  Low: 90 days
```

---

## 7. Remediation Planning

### 7.1 Gap Prioritization

**Prioritization Matrix**:

| Severity | Impact | Effort | Priority |
|----------|--------|--------|----------|
| 🔴 Critical | High | Any | **P0** - Immediate (24-48 hours) |
| 🟠 High | High | Low | **P1** - Urgent (1 week) |
| 🟠 High | High | High | **P2** - High (2 weeks) |
| 🟡 Medium | Medium | Low | **P3** - Medium (1 month) |
| 🟡 Medium | Medium | High | **P4** - Medium (2 months) |
| 🟢 Low | Low | Any | **P5** - Low (3 months) |

**Example Gaps with Prioritization**:

1. **CRITICAL (P0)**: Developer has production access
   - Impact: Security violation, audit failure
   - Effort: Low (revoke access immediately)
   - Action: Remove from production IAM group, enable alerting
   - Owner: IAM Administrator
   - Target: 24 hours

2. **HIGH (P1)**: VPC peering exists between dev and staging
   - Impact: Network isolation violation
   - Effort: Low (remove peering connection)
   - Action: Delete VPC peering, verify traffic blocked
   - Owner: Cloud Architect
   - Target: 1 week

3. **MEDIUM (P3)**: Production credentials not in PAM vault
   - Impact: Credential management gap
   - Effort: Medium (migrate credentials to vault)
   - Action: Move credentials to CyberArk, update documentation
   - Owner: Security Team
   - Target: 1 month

### 7.2 Remediation Tracking

**Remediation Status Categories**:
- **Open**: Gap identified, not yet assigned or started
- **Assigned**: Owner assigned, awaiting start
- **In Progress**: Active remediation work
- **Pending Verification**: Remediation complete, awaiting validation
- **Resolved**: Gap closed and verified
- **Accepted Risk**: Gap acknowledged, risk accepted by CISO
- **False Positive**: Gap determined to be invalid

**Tracking Template**:

| Gap ID | Severity | Description | Owner | Target Date | Status | % Complete |
|--------|----------|-------------|-------|-------------|--------|------------|
| GAP-001 | 🔴 Critical | Dev access to prod | IAM Admin | 2026-01-12 | Resolved | 100% |
| GAP-002 | 🟠 High | VPC peering dev→staging | Cloud Arch | 2026-01-18 | In Progress | 75% |
| GAP-003 | 🟡 Medium | Prod creds not in vault | Security | 2026-02-15 | Assigned | 0% |

---

## 8. Audit Preparation

### 8.1 Evidence Package Assembly

**Required Documents**:
1. Assessment workbooks (completed)
   - ISMS-IMP-A.8.31.1 (Architecture Assessment)
   - ISMS-IMP-A.8.31.2 (Access Control Assessment)
   - ISMS-IMP-A.8.31.3 (Compliance Dashboard)

2. Supporting evidence (referenced in Evidence Registers)
   - Network diagrams
   - Firewall rule exports
   - Cloud configuration exports
   - Access logs
   - Break-glass logs
   - Penetration test reports

3. Remediation tracking
   - Gap analysis with remediation status
   - Risk register
   - Remediation plans with target dates

4. Approval documentation
   - Assessment sign-offs
   - Quarterly certification by managers
   - Exception approvals (if any)

5. Historical trend data
   - Previous quarter dashboards
   - Compliance score trends
   - Gap closure metrics

### 8.2 Auditor Interview Preparation

**Expected Questions and Answers**:

**Q: How do you ensure developers don't have production access?**
A: Multi-layered approach:
- Separate cloud accounts/subscriptions per environment
- IAM policies explicitly deny developer access to production
- Monitoring alerts on any developer production access attempts
- Quarterly access reviews verify ZERO developer production access
- Evidence: User-environment access matrix shows no developers in production

**Q: How do you prevent production data from being used in development/testing?**
A: Strict data separation controls:
- Policy prohibits production data in dev/test (ISMS-POL-A.8.31-S2.3)
- Synthetic data generation tools for testing
- Data anonymization when production-like data needed
- Regular scans of dev/test environments for production data
- Evidence: Data separation assessment shows 100% compliance

**Q: What happens if a developer needs emergency access to production?**
A: Break-glass procedure:
- Incident commander approves emergency access request
- Security team activates time-limited credentials (4-8 hours)
- All actions logged and recorded
- Mandatory post-incident review within 24 hours
- Evidence: Break-glass access log shows all instances with approvals and reviews

**Q: How often do you assess environment separation compliance?**
A: Quarterly formal assessments:
- Architecture assessment (network, infrastructure, data, credentials)
- Access control assessment (permissions, production access, MFA)
- Compliance dashboard generation with executive reporting
- Evidence: Past 4 quarters of dashboards showing trends

**Q: How do you track remediation of identified gaps?**
A: Structured remediation process:
- Gaps prioritized by severity (Critical, High, Medium, Low)
- Owners assigned with target dates
- Status tracked (Open, In Progress, Resolved)
- Monthly remediation review meetings
- Evidence: Gap analysis with remediation tracking

---

## 9. Continuous Monitoring

### 9.1 Automated Compliance Monitoring

**Between Quarterly Assessments**:

**Daily Automated Checks**:
```bash
#!/bin/bash
# daily_compliance_check.sh

# Check 1: Any developers in production IAM groups?
DEV_PROD_ACCESS=$(aws iam get-group --group-name ProductionAdmins --profile prod | \
  jq -r '.Users[].UserName' | grep -i developer | wc -l)

if [ $DEV_PROD_ACCESS -gt 0 ]; then
  echo "🔴 CRITICAL: Developers found in production group!"
  mail -s "CRITICAL: Developer Production Access" security-team@example.com
fi

# Check 2: Any VPC peering between dev and prod?
VPC_PEERING=$(aws ec2 describe-vpc-peering-connections --profile prod | \
  jq -r '.VpcPeeringConnections[] | select(.RequesterVpcInfo.OwnerId=="111111111111") | .VpcPeeringConnectionId' | wc -l)

if [ $VPC_PEERING -gt 0 ]; then
  echo "⚠️ WARNING: VPC peering exists between dev and prod"
  mail -s "WARNING: Dev-Prod VPC Peering" security-team@example.com
fi

# Check 3: MFA enabled for all production users?
PROD_USERS_NO_MFA=$(aws iam list-users --profile prod | \
  jq -r '.Users[] | select(.MfaDevices | length == 0) | .UserName' | wc -l)

if [ $PROD_USERS_NO_MFA -gt 0 ]; then
  echo "⚠️ WARNING: Production users without MFA"
  mail -s "WARNING: Production MFA Not Enabled" security-team@example.com
fi

echo "✅ Daily compliance check complete"
```

**Weekly Automated Reports**:
- Cross-environment access attempts (should all be blocked)
- Break-glass usage (if any)
- Dormant accounts (no activity in 90 days)
- Credential rotation status

### 9.2 Real-Time Alerting

**SIEM Alert Rules**:

1. **Developer Production Access** (CRITICAL)
   - Trigger: ANY developer assumes production IAM role
   - Action: Immediate alert to CISO, block access, create incident
   - Priority: P0

2. **Production Data Export** (HIGH)
   - Trigger: Large data export from production database
   - Action: Alert security team, investigate if authorized
   - Priority: P1

3. **Cross-Environment Network Traffic** (MEDIUM)
   - Trigger: Network traffic from dev to production (should be blocked)
   - Action: Alert network team, verify firewall rules
   - Priority: P2

4. **Break-Glass Activation** (INFORMATIONAL)
   - Trigger: Break-glass credentials activated
   - Action: Notify CISO, start incident tracking
   - Priority: P3 (expected during incidents)

---

## 10. Dashboard Maintenance

### 10.1 Dashboard Update Schedule

**Quarterly (Formal Assessment)**:
- Complete architecture assessment (ISMS-IMP-A.8.31.1)
- Complete access control assessment (ISMS-IMP-A.8.31.2)
- Generate new dashboard (ISMS-IMP-A.8.31.3)
- Update trend analysis with new data point
- Present to executive management

**Monthly (Light Touch)**:
- Review compliance metrics
- Update remediation status
- Check for new gaps
- Verify critical controls (developer prod access, data separation)

**Ad-Hoc (Triggered by Events)**:
- Major infrastructure changes (cloud migration, new environments)
- Security incidents (break-glass usage, policy violations)
- Audit requests (provide current compliance status)

### 10.2 Dashboard Archival

**Retention Requirements**:
- Keep all quarterly dashboards for 7 years (regulatory compliance)
- Archive supporting evidence with dashboards
- Maintain remediation tracking history
- Preserve trend analysis data

**Storage Location**:
- Primary: SharePoint/Document Management System
- Backup: Secure file share (encrypted, access-controlled)
- Audit Package: Separate evidence folder per quarter

---

## 11. Tool Reference

### 11.1 Assessment Workbooks

**ISMS-IMP-A.8.31.1**: Environment Architecture Assessment
- Generates: `ISMS-IMP-A.8.31.1_Environment_Architecture_Assessment_YYYYMMDD.xlsx`
- Usage: `python3 generate_assessment_1_environment_architecture.py`
- Sheets: 10 (Instructions, Inventory, Network, Infrastructure, Data, Credentials, Config, Gap, Evidence, Approval)

**ISMS-IMP-A.8.31.2**: Environment Access Control Assessment
- Generates: `ISMS-IMP-A.8.31.2_Environment_Access_Control_Assessment_YYYYMMDD.xlsx`
- Usage: `python3 generate_assessment_2_environment_access.py`
- Sheets: 10 (Instructions, Access Matrix, Developer Prod Access, Credentials, Cross-Env Log, Break-Glass, MFA, Scorecard, Evidence, Approval)

**ISMS-IMP-A.8.31.3**: Compliance Dashboard
- Generates: `ISMS-IMP-A.8.31.3_Environment_Separation_Dashboard_YYYYMMDD.xlsx`
- Usage: `python3 generate_dashboard_environment_separation.py`
- Sheets: 8 (Executive Summary, Environment Status, Access Summary, Gap Analysis, Risk Register, Evidence Summary, Trend Analysis, Approval)

### 11.2 Utility Scripts

**Normalization Script**:
```bash
python3 normalize_assessment_files_a831.py
# Prepares assessment files for dashboard consumption
# Creates normalized filenames (no dates/versions)
```

**Sanity Check Script**:
```bash
python3 excel_sanity_check_a831.py ISMS-IMP-A.8.31.1_*.xlsx
# Validates workbook integrity
# Checks for common Excel issues
```

**Dashboard Sanity Check**:
```bash
python3 sanity_check_a831_dashboard.py
# Pre-flight check before generating dashboard
# Validates all required functions exist
```

---

**Document Approval**:

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Implementation Lead | [Name] | ________________ | [Date] |
| CISO | [Name] | ________________ | [Date] |
| Information Security Manager | [Name] | ________________ | [Date] |
| IT Operations Manager | [Name] | ________________ | [Date] |

---

*End of Document ISMS-IMP-A.8.31-S3*
