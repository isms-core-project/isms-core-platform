# ISMS-IMP-A.8.31-S2
## Environment Access Control Implementation & Assessment

**Document ID**: ISMS-IMP-A.8.31-S2  
**Title**: Environment Access Control Implementation & Assessment  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | IAM Administrator / Information Security Manager | Initial implementation guide |

**Review Cycle**: Quarterly (or upon access control changes)  
**Approvers**: CISO, IT Operations Manager, IAM Administrator  
**Related Policy**: ISMS-POL-A.8.31-S2.2 (Environment Access Control Requirements)

---

## 1. Purpose and Scope

### 1.1 Overview

This implementation guide provides **step-by-step procedures** for implementing and assessing environment-specific access controls in compliance with ISO/IEC 27001:2022 Control A.8.31.

**Objectives**:
- Implement environment-specific access controls (dev, test, staging, production)
- Enforce production access restrictions (operations-only)
- Configure break-glass emergency access procedures
- Assess compliance with access control requirements
- Document evidence for audit purposes

**Critical Requirement**: **ZERO developer access to production** (except via documented break-glass procedure for emergencies).

### 1.2 Target Audience

- **IAM Administrators**: Implementing access control policies
- **IT Operations Teams**: Managing production access
- **Security Team**: Assessing access compliance
- **Developers/DevOps**: Understanding access restrictions
- **Auditors**: Verifying access control implementation

---

## 2. Access Control Principles

### 2.1 Core Principles

**Principle 1: Least Privilege**
- Users have minimum access required for their role in each environment
- Access granted per environment, not globally

**Principle 2: Separation of Duties**
- Developers write code (dev/test environments)
- Operations deploy to production
- NO single person has both development and production deployment rights

**Principle 3: Need-to-Know**
- Production access restricted to operational necessity only
- Developers do NOT need production access for normal work

**Principle 4: Just-in-Time Access**
- Production access granted temporarily for specific incidents
- Break-glass access time-limited (hours, not days)
- Post-incident review mandatory

### 2.2 Access Control Matrix

**Standard Access Matrix**:

| Role | Development | Testing | Staging | Production |
|------|-------------|---------|---------|------------|
| **Developer** | Full (CRUD) | Read/Write (limited) | Read-only | ❌ NO ACCESS |
| **QA Engineer** | Read-only | Full (CRUD) | Read-only | ❌ NO ACCESS |
| **Senior Developer** | Full (CRUD) | Full (CRUD) | Read-only | ❌ NO ACCESS (break-glass only) |
| **DevOps Engineer** | Full (CRUD) | Full (CRUD) | Read/Write | Read-only (monitoring) |
| **Operations Engineer** | Read-only (support) | Read-only (support) | Full (CRUD) | Full (CRUD) via PAM |
| **Security Analyst** | Read-only | Read-only | Read-only | Read-only (monitoring, logs) |
| **Auditor** | Read-only | Read-only | Read-only | Read-only (audit logs) |

**Key Observations**:
- ❌ Developers have ZERO production access (normal operations)
- ✅ Operations team exclusive production admin access
- ✅ All production access via PAM vault
- ✅ Break-glass available for emergencies (tracked and reviewed)

---

## 3. Access Control Implementation

### 3.1 On-Premises / Active Directory

**Step 1: Create Security Groups Per Environment**

```powershell
# Development environment groups
New-ADGroup -Name "DEV-App-Admins" -GroupScope Global -GroupCategory Security
New-ADGroup -Name "DEV-App-Users" -GroupScope Global -GroupCategory Security

# Testing environment groups
New-ADGroup -Name "TEST-App-Admins" -GroupScope Global -GroupCategory Security
New-ADGroup -Name "TEST-App-Users" -GroupScope Global -GroupCategory Security

# Production environment groups
New-ADGroup -Name "PROD-Ops-Admins" -GroupScope Global -GroupCategory Security
New-ADGroup -Name "PROD-Monitoring" -GroupScope Global -GroupCategory Security
New-ADGroup -Name "PROD-BreakGlass" -GroupScope Global -GroupCategory Security
```

**Step 2: Assign Users to Groups**

```powershell
# Developers - dev and test access only
Add-ADGroupMember -Identity "DEV-App-Admins" -Members "dev_user1", "dev_user2"
Add-ADGroupMember -Identity "TEST-App-Users" -Members "dev_user1", "dev_user2"

# Operations team - production access
Add-ADGroupMember -Identity "PROD-Ops-Admins" -Members "ops_user1", "ops_user2"

# NO developers in production groups (enforce separation)
# Break-glass group empty by default (activated only during incidents)
```

**Step 3: Configure Server Access (NTFS/Share Permissions)**

```
Production Servers:
\\prod-app01\c$
  - PROD-Ops-Admins: Full Control
  - PROD-Monitoring: Read-only
  - DEV-App-Admins: DENIED (explicit deny)
  
Development Servers:
\\dev-app01\c$
  - DEV-App-Admins: Full Control
  - PROD-Ops-Admins: Read-only (for support)
```

**Verification**:

```powershell
# Test access from developer account to production
Test-Path \\prod-app01\c$ -ErrorAction SilentlyContinue
# Should return: False (access denied)

# Test access from operations account to production
Test-Path \\prod-app01\c$ -ErrorAction SilentlyContinue
# Should return: True (access granted)
```

### 3.2 AWS IAM

**Step 1: Multi-Account Setup with IAM Roles**

```
Development Account (111111111111):
  - Role: DevFullAccess
  - Assume by: Developers group
  - Permissions: EC2, RDS, S3 (dev account only)

Production Account (444444444444):
  - Role: ProdOpsAccess
  - Assume by: Operations group ONLY
  - Permissions: EC2, RDS, S3 (prod account only)
  - MFA: REQUIRED
```

**Step 2: IAM Policy - Development Account**

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ec2:*",
        "rds:*",
        "s3:*",
        "cloudwatch:*"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:RequestedRegion": "us-east-1"
        }
      }
    },
    {
      "Effect": "Deny",
      "Action": "sts:AssumeRole",
      "Resource": "arn:aws:iam::444444444444:role/*"
    }
  ]
}
```

**Step 3: IAM Policy - Production Account**

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ec2:Describe*",
        "rds:Describe*",
        "s3:ListBucket",
        "cloudwatch:GetMetricStatistics"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Deny",
      "NotAction": [
        "ec2:Describe*",
        "rds:Describe*",
        "s3:ListBucket",
        "cloudwatch:GetMetricStatistics"
      ],
      "Resource": "*",
      "Condition": {
        "StringNotLike": {
          "aws:userid": "AIDAI*:ops-*"
        }
      }
    }
  ]
}
```

**Step 4: Enforce MFA for Production**

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Deny",
      "Action": "*",
      "Resource": "*",
      "Condition": {
        "BoolIfExists": {
          "aws:MultiFactorAuthPresent": "false"
        }
      }
    }
  ]
}
```

**Verification**:

```bash
# Developer tries to assume production role (should FAIL)
aws sts assume-role --role-arn arn:aws:iam::444444444444:role/ProdOpsAccess \
  --role-session-name test --profile dev-user

# Expected error: User is not authorized to perform: sts:AssumeRole

# Operations user assumes production role (should SUCCEED with MFA)
aws sts assume-role --role-arn arn:aws:iam::444444444444:role/ProdOpsAccess \
  --role-session-name ops-session --serial-number arn:aws:iam::444444444444:mfa/ops-user \
  --token-code 123456 --profile ops-user

# Should return temporary credentials
```

### 3.3 Azure RBAC

**Step 1: Create Custom Roles Per Environment**

```json
{
  "Name": "Development Environment Contributor",
  "Id": null,
  "IsCustom": true,
  "Description": "Full access to development subscription resources",
  "Actions": [
    "Microsoft.Compute/*",
    "Microsoft.Storage/*",
    "Microsoft.Network/*",
    "Microsoft.Sql/*"
  ],
  "NotActions": [],
  "AssignableScopes": [
    "/subscriptions/dev-subscription-id"
  ]
}
```

```json
{
  "Name": "Production Operations Admin",
  "Id": null,
  "IsCustom": true,
  "Description": "Full access to production subscription - Operations team only",
  "Actions": [
    "Microsoft.Compute/*",
    "Microsoft.Storage/*",
    "Microsoft.Network/*",
    "Microsoft.Sql/*"
  ],
  "NotActions": [],
  "AssignableScopes": [
    "/subscriptions/prod-subscription-id"
  ]
}
```

**Step 2: Assign Roles to Users/Groups**

```bash
# Developers - development subscription
az role assignment create \
  --assignee-object-id <developer-group-id> \
  --role "Development Environment Contributor" \
  --scope /subscriptions/dev-subscription-id

# Operations - production subscription
az role assignment create \
  --assignee-object-id <operations-group-id> \
  --role "Production Operations Admin" \
  --scope /subscriptions/prod-subscription-id

# Developers explicitly DENIED on production subscription
az role assignment create \
  --assignee-object-id <developer-group-id> \
  --role "Deny Assignment" \
  --scope /subscriptions/prod-subscription-id
```

**Step 3: Conditional Access - MFA Required for Production**

```json
{
  "displayName": "Require MFA for Production Access",
  "state": "enabled",
  "conditions": {
    "applications": {
      "includeApplications": ["All"]
    },
    "users": {
      "includeGroups": ["Operations-Team"]
    },
    "locations": {
      "includeLocations": ["All"]
    }
  },
  "grantControls": {
    "operator": "AND",
    "builtInControls": ["mfa"]
  },
  "sessionControls": {
    "signInFrequency": {
      "value": 8,
      "type": "hours"
    }
  }
}
```

**Verification**:

```bash
# Developer tries to list production resources (should FAIL)
az vm list --subscription prod-subscription-id
# Error: The client does not have authorization to perform action

# Operations user lists production resources (should SUCCEED with MFA)
az vm list --subscription prod-subscription-id
# Prompts for MFA, then returns VM list
```

### 3.4 GCP IAM

**Step 1: Create Custom Roles Per Environment**

```yaml
title: "Development Environment Admin"
description: "Full access to development project resources"
stage: "GA"
includedPermissions:
- compute.instances.*
- storage.buckets.*
- cloudsql.instances.*
- monitoring.timeSeries.list
```

```yaml
title: "Production Operations Admin"
description: "Full access to production project - Operations only"
stage: "GA"
includedPermissions:
- compute.instances.*
- storage.buckets.*
- cloudsql.instances.*
- monitoring.timeSeries.list
```

**Step 2: Assign Roles to Users**

```bash
# Developers - development project
gcloud projects add-iam-policy-binding dev-project-123456 \
  --member='group:developers@example.com' \
  --role='projects/dev-project-123456/roles/DevelopmentEnvironmentAdmin'

# Operations - production project
gcloud projects add-iam-policy-binding prod-project-456789 \
  --member='group:operations@example.com' \
  --role='projects/prod-project-456789/roles/ProductionOperationsAdmin'

# Developers explicitly DENIED on production
gcloud projects add-iam-policy-binding prod-project-456789 \
  --member='group:developers@example.com' \
  --role='roles/iam.denyAll'
```

**Verification**:

```bash
# Developer tries to list production VMs (should FAIL)
gcloud compute instances list --project=prod-project-456789
# Error: Permission denied

# Operations user lists production VMs (should SUCCEED)
gcloud compute instances list --project=prod-project-456789
# Returns VM list
```

### 3.5 Kubernetes RBAC

**Step 1: Create Namespaces with RBAC**

```yaml
# Development namespace
apiVersion: v1
kind: Namespace
metadata:
  name: dev
---
# Development role - full access to dev namespace
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  namespace: dev
  name: dev-full-access
rules:
- apiGroups: ["*"]
  resources: ["*"]
  verbs: ["*"]
---
# Bind developers to dev role
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: dev-users-binding
  namespace: dev
subjects:
- kind: Group
  name: developers
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: Role
  name: dev-full-access
  apiGroup: rbac.authorization.k8s.io
```

```yaml
# Production namespace
apiVersion: v1
kind: Namespace
metadata:
  name: prod
---
# Production role - full access ONLY for operations
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  namespace: prod
  name: prod-ops-access
rules:
- apiGroups: ["*"]
  resources: ["*"]
  verbs: ["*"]
---
# Bind operations team to prod role
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: ops-users-binding
  namespace: prod
subjects:
- kind: Group
  name: operations
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: Role
  name: prod-ops-access
  apiGroup: rbac.authorization.k8s.io
---
# Production read-only for monitoring
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  namespace: prod
  name: prod-monitoring
rules:
- apiGroups: ["*"]
  resources: ["pods", "deployments", "services"]
  verbs: ["get", "list", "watch"]
---
# Bind monitoring to prod read-only
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: monitoring-binding
  namespace: prod
subjects:
- kind: Group
  name: monitoring
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: Role
  name: prod-monitoring
  apiGroup: rbac.authorization.k8s.io
```

**Verification**:

```bash
# Developer tries to list production pods (should FAIL)
kubectl get pods -n prod --as=developer
# Error: User "developer" cannot list resource "pods" in namespace "prod"

# Operations user lists production pods (should SUCCEED)
kubectl get pods -n prod --as=ops-user
# Returns pod list
```

---

## 4. Break-Glass Emergency Access

### 4.1 Break-Glass Procedure

**When to Use Break-Glass**:
- Critical production incident requiring developer expertise
- Production system down, operations team needs developer assistance
- Security incident requiring immediate developer forensics
- Data recovery requiring developer knowledge

**When NOT to Use Break-Glass**:
- Regular debugging (use logs, monitoring)
- Feature development or testing
- Performance optimization (non-emergency)
- Curiosity or convenience

**Process Flow**:

```
1. INCIDENT DECLARED
   ↓
2. INCIDENT COMMANDER approves break-glass
   ↓
3. DEVELOPER requests break-glass access
   ↓
4. SECURITY TEAM activates temporary credentials
   ↓
5. DEVELOPER troubleshoots production (TIME-LIMITED)
   ↓
6. INCIDENT RESOLVED
   ↓
7. BREAK-GLASS ACCESS REVOKED
   ↓
8. POST-INCIDENT REVIEW (mandatory)
```

### 4.2 Break-Glass Implementation

**AWS - Break-Glass Role**:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::444444444444:user/emergency-access"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "IpAddress": {
          "aws:SourceIp": "203.0.113.0/24"
        },
        "DateGreaterThan": {
          "aws:CurrentTime": "2026-01-11T09:00:00Z"
        },
        "DateLessThan": {
          "aws:CurrentTime": "2026-01-11T17:00:00Z"
        }
      }
    }
  ]
}
```

**Break-Glass Activation Script**:

```bash
#!/bin/bash
# break_glass_activate.sh

DEVELOPER_EMAIL=$1
INCIDENT_ID=$2
DURATION_HOURS=$3

echo "🚨 BREAK-GLASS ACCESS REQUEST 🚨"
echo "Developer: $DEVELOPER_EMAIL"
echo "Incident: $INCIDENT_ID"
echo "Duration: $DURATION_HOURS hours"
echo ""
read -p "Approve? (YES/no): " APPROVAL

if [ "$APPROVAL" != "YES" ]; then
    echo "❌ Break-glass access DENIED"
    exit 1
fi

# Generate temporary credentials
EXPIRY=$(date -u -d "+$DURATION_HOURS hours" +"%Y-%m-%dT%H:%M:%SZ")

# Add developer to break-glass group
aws iam add-user-to-group \
    --user-name $DEVELOPER_EMAIL \
    --group-name BreakGlassAccess

# Log activation
echo "$(date): BREAK-GLASS activated for $DEVELOPER_EMAIL (Incident: $INCIDENT_ID, Expires: $EXPIRY)" \
    >> /var/log/breakglass.log

# Send notification
mail -s "🚨 BREAK-GLASS ACTIVATED: $DEVELOPER_EMAIL" security-team@example.com <<EOF
Break-glass access activated:

Developer: $DEVELOPER_EMAIL
Incident ID: $INCIDENT_ID
Activated: $(date)
Expires: $EXPIRY
Approved by: $(whoami)

All actions will be logged and audited.
EOF

echo "✅ Break-glass access ACTIVATED"
echo "Expires: $EXPIRY"
echo "⚠️  All actions are logged and will be reviewed."
```

**Break-Glass Revocation Script**:

```bash
#!/bin/bash
# break_glass_revoke.sh

DEVELOPER_EMAIL=$1

# Remove from break-glass group
aws iam remove-user-from-group \
    --user-name $DEVELOPER_EMAIL \
    --group-name BreakGlassAccess

# Log revocation
echo "$(date): BREAK-GLASS revoked for $DEVELOPER_EMAIL" \
    >> /var/log/breakglass.log

echo "✅ Break-glass access REVOKED for $DEVELOPER_EMAIL"
```

### 4.3 Break-Glass Monitoring

**CloudWatch Alarm - Break-Glass Usage**:

```json
{
  "AlarmName": "BreakGlassAccessUsed",
  "AlarmDescription": "Alert when break-glass credentials are used",
  "MetricName": "AssumeRoleCount",
  "Namespace": "AWS/IAM",
  "Statistic": "Sum",
  "Period": 300,
  "EvaluationPeriods": 1,
  "Threshold": 1,
  "ComparisonOperator": "GreaterThanThreshold",
  "Dimensions": [
    {
      "Name": "RoleName",
      "Value": "BreakGlassRole"
    }
  ],
  "AlarmActions": [
    "arn:aws:sns:us-east-1:444444444444:security-alerts"
  ]
}
```

---

## 5. Access Monitoring and Logging

### 5.1 Access Log Requirements

**What Must Be Logged**:
- Who accessed which environment
- When (timestamp)
- What actions were performed
- Source IP address
- Success or failure
- MFA status (for production)

**Log Retention**:
- Development: 90 days
- Testing: 6 months
- Staging: 1 year
- Production: 7 years (regulatory compliance)

### 5.2 SIEM Integration

**Example Splunk Query - Production Access by Developers**:

```spl
index=aws_cloudtrail 
eventName=AssumeRole 
requestParameters.roleArn="*prod*" 
userIdentity.principalId="*developer*"
| stats count by userIdentity.principalId, eventTime
| sort - eventTime
```

**Alert Rule**:
```
Alert: Developer Production Access
Trigger: ANY developer assumes production role
Action: Send to security-alerts@example.com, create Jira ticket
Severity: HIGH
```

### 5.3 Access Review Procedures

**Monthly Access Review**:
1. Export user-to-environment access matrix
2. Review production access list (should be operations-only)
3. Check for dormant accounts (no activity in 90 days)
4. Verify MFA enabled for all production accounts
5. Document findings and remediation actions

**Quarterly Certification**:
1. Operations manager certifies production access list
2. Development manager certifies dev/test access list
3. CISO approves exceptions (if any)

---

## 6. Assessment Methodology

### 6.1 Access Control Assessment

Use the provided Excel assessment workbook: **ISMS-IMP-A.8.31.2.xlsx**

**Assessment Process**:

1. **User-Environment Access Matrix**
   - Document who has access to which environment
   - Verify developers have NO production access

2. **Production Access Audit**
   - List all users with production access
   - Verify all are operations team members
   - Check MFA enabled

3. **Break-Glass Procedures**
   - Document break-glass activation process
   - Review break-glass access log (past 12 months)
   - Verify post-incident reviews conducted

4. **Access Monitoring**
   - Check SIEM alerts configured
   - Review access logs for anomalies
   - Verify log retention per policy

5. **Compliance Scoring**
   - Calculate compliance percentage
   - Identify gaps
   - Document remediation plan

### 6.2 Evidence Collection

Required evidence for audit:

- **User-Environment Access Matrix** (export from IAM system)
- **Production Access List** (with justification for each user)
- **MFA Enforcement Evidence** (conditional access policies, IAM policies)
- **Break-Glass Access Log** (past 12 months)
- **Post-Incident Reviews** (break-glass usage)
- **Access Review Reports** (monthly/quarterly)
- **SIEM Alert Configuration** (screenshots or exports)

---

## 7. Common Implementation Scenarios

### 7.1 Small Organization (Single Sign-On)

**Pattern**: Active Directory with SSO to cloud services

```
Active Directory:
  - Group: DEV-Users → Dev environment access
  - Group: OPS-Users → Production environment access
  
Azure AD Connect:
  - Sync AD groups to Azure AD
  - Conditional Access enforces MFA for production
  
AWS SSO:
  - DEV-Users → DevFullAccess role (dev account)
  - OPS-Users → ProdOpsAccess role (prod account)
```

### 7.2 Medium Organization (Multi-Cloud)

**Pattern**: Centralized IAM with federation

```
Okta (Identity Provider):
  - Developers group → AWS dev account, Azure dev subscription
  - Operations group → AWS prod account, Azure prod subscription
  
SAML Federation:
  - Okta → AWS (SAML trust)
  - Okta → Azure (SAML trust)
  - Okta → GCP (SAML trust)
  
MFA:
  - Okta enforces MFA for production access
```

### 7.3 Large Organization (Centralized IAM)

**Pattern**: PAM + Just-in-Time Access

```
CyberArk PAM:
  - Production credentials stored in vault
  - Just-in-time access provisioning
  - Session recording for production access
  
ServiceNow Integration:
  - Access requests via ServiceNow tickets
  - Approval workflow (manager → CISO)
  - Automated provisioning after approval
  - Automatic de-provisioning after expiry
```

---

## 8. Troubleshooting Common Issues

### 8.1 Developer Cannot Access Development

**Problem**: Developer gets "Access Denied" in dev environment

**Root Cause**: User not in development access group

**Solution**:
```bash
# Check group membership
aws iam get-group --group-name DevelopersGroup

# Add user to group
aws iam add-user-to-group --user-name dev_user1 --group-name DevelopersGroup
```

### 8.2 Operations User Cannot Access Production

**Problem**: Operations user gets "MFA required" error

**Root Cause**: MFA not configured or token expired

**Solution**:
```bash
# Enable MFA device
aws iam enable-mfa-device \
    --user-name ops_user1 \
    --serial-number arn:aws:iam::444444444444:mfa/ops_user1 \
    --authentication-code1 123456 \
    --authentication-code2 789012

# Test MFA
aws sts get-session-token \
    --serial-number arn:aws:iam::444444444444:mfa/ops_user1 \
    --token-code 123456
```

### 8.3 Break-Glass Access Not Working

**Problem**: Break-glass credentials expired or invalid

**Root Cause**: Time-based condition in IAM policy expired

**Solution**:
```bash
# Update IAM policy with new time window
aws iam update-assume-role-policy \
    --role-name BreakGlassRole \
    --policy-document file://breakglass-policy-updated.json
```

---

## 9. Continuous Compliance Monitoring

### 9.1 Automated Access Scanning

**AWS Config Rule - No Developer Production Access**:

```json
{
  "ConfigRuleName": "no-developer-production-access",
  "Description": "Ensure no developers have production account access",
  "Source": {
    "Owner": "CUSTOM_LAMBDA",
    "SourceIdentifier": "arn:aws:lambda:us-east-1:444444444444:function:CheckDevProdAccess"
  },
  "Scope": {
    "ComplianceResourceTypes": ["AWS::IAM::User", "AWS::IAM::Group"]
  }
}
```

**Lambda Function** (pseudo-code):

```python
def check_dev_prod_access(event):
    """Check if any developer has production access."""
    
    # Get all IAM users in production account
    prod_users = iam.list_users(AccountId='444444444444')
    
    # Get developer group members from dev account
    dev_users = iam.list_group_members(GroupName='DevelopersGroup', AccountId='111111111111')
    
    # Check for overlap
    violations = set(prod_users) & set(dev_users)
    
    if violations:
        return {
            'compliance_type': 'NON_COMPLIANT',
            'annotation': f'Developers have production access: {violations}'
        }
    else:
        return {
            'compliance_type': 'COMPLIANT'
        }
```

### 9.2 Compliance Dashboard

Monitor key metrics:
- **Developers with production access**: **0** (target)
- **Production accounts with MFA**: **100%** (target)
- **Break-glass usage (past month)**: Document each instance
- **Access reviews completed on time**: **100%** (target)
- **Dormant accounts (90+ days inactive)**: **0** (target)

---

## 10. Audit Preparation

### 10.1 Evidence Package

Prepare for auditors:

1. **Access Control Documentation**
   - User-environment access matrix
   - Production access list with justifications

2. **Access Logs**
   - Production access logs (past 12 months)
   - Break-glass access logs (past 12 months)
   - Failed access attempts (anomalies)

3. **Break-Glass Evidence**
   - Break-glass procedure document
   - Post-incident review reports (all break-glass usage)
   - Break-glass access approval records

4. **Access Review Evidence**
   - Monthly access review reports
   - Quarterly certification sign-offs
   - Remediation actions for identified issues

5. **Technical Controls**
   - IAM policy exports (AWS, Azure, GCP)
   - Conditional access policies (MFA enforcement)
   - SIEM alert configurations

### 10.2 Interview Preparation

Be prepared to answer:

- How many developers have production access? (Answer: ZERO)
- What is the break-glass procedure?
- How do you detect unauthorized production access?
- How often do you review production access?
- What happens if a developer tries to access production?

---

**Document Approval**:

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Implementation Lead | [Name] | ________________ | [Date] |
| CISO | [Name] | ________________ | [Date] |
| IAM Administrator | [Name] | ________________ | [Date] |
| IT Operations Manager | [Name] | ________________ | [Date] |

---

*End of Document ISMS-IMP-A.8.31-S2*
