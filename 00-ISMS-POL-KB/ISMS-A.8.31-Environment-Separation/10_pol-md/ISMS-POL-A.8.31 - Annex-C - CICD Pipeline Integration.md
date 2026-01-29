# ISMS-POL-A.8.31-Annex-C
## Environment Separation - CI/CD Pipeline Integration

**Document ID**: ISMS-POL-A.8.31-Annex-C  
**Title**: CI/CD Pipeline Integration for Environment Separation  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | DevOps Lead / Information Security Manager | Initial CI/CD integration guidance |

**Review Cycle**: Annual (or upon CI/CD platform changes)  
**Approvers**: DevOps Lead, Information Security Manager, CISO

---

## C.1 Purpose

This annex provides **technology-agnostic guidance** for integrating environment separation controls into Continuous Integration / Continuous Deployment (CI/CD) pipelines. Properly configured CI/CD pipelines enforce environment boundaries and prevent unauthorized deployments.

**Scope**: All CI/CD platforms and deployment automation tools used by [Organization].

---

## C.2 CI/CD Pipeline Architecture for Environment Separation

### C.2.1 Pipeline Structure

**Environment-Aware Pipeline Design**:

```
┌─────────────────────────────────────────────────────────────┐
│                    SOURCE CODE REPOSITORY                    │
│                  (Git, GitHub, GitLab, etc.)                 │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│              CI/CD ORCHESTRATION PLATFORM                    │
│        (Jenkins, GitLab CI, GitHub Actions, etc.)            │
└────────────────────┬────────────────────────────────────────┘
                     │
         ┌───────────┼───────────┬───────────┐
         │           │           │           │
         ▼           ▼           ▼           ▼
    ┌────────┐  ┌────────┐  ┌────────┐  ┌────────┐
    │  DEV   │  │  TEST  │  │ STAGING│  │  PROD  │
    │PIPELINE│  │PIPELINE│  │PIPELINE│  │PIPELINE│
    └────┬───┘  └────┬───┘  └────┬───┘  └────┬───┘
         │           │           │           │
         │     AUTO  │     AUTO  │    MANUAL │
         │     ↓     │     ↓     │     ↓     │
         ▼           ▼           ▼           ▼
    ┌────────┐  ┌────────┐  ┌────────┐  ┌────────┐
    │  DEV   │  │  TEST  │  │ STAGING│  │  PROD  │
    │  ENV   │  │  ENV   │  │  ENV   │  │  ENV   │
    └────────┘  └────────┘  └────────┘  └────────┘
```

**Key Principles**:
- **Separate pipeline jobs** per environment
- **Automated promotion** from dev → test → staging
- **Manual approval gate** before production deployment
- **Environment validation** at each stage

### C.2.2 Deployment Gates and Approvals

**Approval Requirements by Environment**:

| From → To | Approval Type | Who Approves | Additional Checks |
|-----------|---------------|--------------|-------------------|
| Dev → Test | Automatic | None (on successful build) | Unit tests pass |
| Test → Staging | Automatic | QA Lead (optional) | Integration tests pass |
| Staging → Production | **MANUAL** | Change Advisory Board | All tests pass, CAB approval, deployment window |

**Production Deployment Gate**:
- Requires explicit approval from authorized personnel (operations team, change manager)
- Deployment only during approved change windows (not 24/7 deployment)
- Rollback plan documented and available
- Smoke tests defined and ready for post-deployment validation

---

## C.3 Environment-Specific Pipeline Configuration

### C.3.1 Environment Variables and Secrets

**Separation of Secrets by Environment**:

**Jenkins Example**:
```groovy
pipeline {
    agent any
    environment {
        // Environment determined by branch or parameter
        ENV_NAME = "${params.TARGET_ENV}"
    }
    stages {
        stage('Deploy') {
            steps {
                script {
                    // Load environment-specific credentials
                    withCredentials([
                        string(credentialsId: "${ENV_NAME}-db-password", variable: 'DB_PASS'),
                        string(credentialsId: "${ENV_NAME}-api-key", variable: 'API_KEY')
                    ]) {
                        sh "deploy.sh --env ${ENV_NAME} --db-pass ${DB_PASS}"
                    }
                }
            }
        }
    }
}
```

**GitLab CI Example**:
```yaml
deploy_to_dev:
  stage: deploy
  environment: development
  variables:
    ENV_NAME: "dev"
  script:
    - deploy.sh --env $ENV_NAME
  only:
    - develop

deploy_to_prod:
  stage: deploy
  environment: production
  variables:
    ENV_NAME: "prod"
  script:
    - deploy.sh --env $ENV_NAME
  when: manual  # Requires manual trigger
  only:
    - main
```

**GitHub Actions Example**:
```yaml
name: Deploy Pipeline

on:
  push:
    branches:
      - main
      - develop

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Determine Environment
        id: set-env
        run: |
          if [[ "${{ github.ref }}" == "refs/heads/main" ]]; then
            echo "env_name=production" >> $GITHUB_OUTPUT
          elif [[ "${{ github.ref }}" == "refs/heads/develop" ]]; then
            echo "env_name=development" >> $GITHUB_OUTPUT
          fi
      
      - name: Deploy
        env:
          DB_PASSWORD: ${{ secrets[format('{0}_DB_PASSWORD', steps.set-env.outputs.env_name)] }}
        run: |
          ./deploy.sh --env ${{ steps.set-env.outputs.env_name }}
```

**Key Practices**:
- **Never hardcode** production credentials in pipeline definitions
- Use **CI/CD secret management** (Jenkins Credentials, GitLab CI/CD variables, GitHub Secrets)
- Scope secrets **per environment** (dev-db-password, prod-db-password)
- **Rotate secrets** regularly (automated rotation preferred)

### C.3.2 Infrastructure as Code (IaC) Integration

**Terraform Example**:
```hcl
# Backend configuration per environment
terraform {
  backend "s3" {
    bucket = "myorg-terraform-state-${var.environment}"
    key    = "infrastructure/terraform.tfstate"
    region = "us-east-1"
  }
}

# Environment-specific variables
variable "environment" {
  description = "Target environment (dev, test, staging, prod)"
  type        = string
}

# Resource naming includes environment
resource "aws_instance" "app_server" {
  ami           = var.ami_id
  instance_type = var.environment == "prod" ? "t3.large" : "t3.micro"
  
  tags = {
    Name        = "app-server-${var.environment}"
    Environment = var.environment
  }
}
```

**Pipeline Integration**:
```bash
#!/bin/bash
# Pipeline deployment script

ENV=$1  # dev, test, staging, prod

# Validate environment
if [[ ! "$ENV" =~ ^(dev|test|staging|prod)$ ]]; then
    echo "ERROR: Invalid environment. Must be dev, test, staging, or prod."
    exit 1
fi

# Apply Terraform with environment-specific vars
terraform init -backend-config="backend-${ENV}.hcl"
terraform plan -var-file="${ENV}.tfvars" -out="${ENV}.plan"

# Production requires manual approval
if [ "$ENV" == "prod" ]; then
    echo "Production deployment requires manual approval."
    echo "Review plan and run: terraform apply ${ENV}.plan"
    exit 0
else
    terraform apply "${ENV}.plan"
fi
```

---

## C.4 Access Control in CI/CD Pipelines

### C.4.1 Pipeline Execution Permissions

**Who Can Trigger Pipelines**:

| Environment | Who Can Deploy | Mechanism |
|-------------|----------------|-----------|
| Development | Developers | Automatic on git push to develop branch |
| Testing | Developers, QA | Automatic on merge to test branch |
| Staging | Senior Developers, Operations | Semi-automatic (merge triggers, but can be paused) |
| Production | Operations Team ONLY | Manual trigger + approval required |

**Implementation Examples**:

**Jenkins (Role-Based Access)**:
- Developers: Can trigger dev/test pipelines
- Operations: Can trigger all pipelines including production
- Production pipeline job requires "Deploy to Production" permission

**GitLab CI (Protected Environments)**:
```yaml
deploy_to_production:
  stage: deploy
  environment:
    name: production
  script:
    - ./deploy.sh --env production
  only:
    - main
  when: manual
  # Only users with "Maintainer" role can trigger
```

**GitHub Actions (Environment Protection Rules)**:
- Environment "production" requires reviewers (operations team members)
- Required approvals: 2 reviewers before deployment proceeds
- Deployment branches restricted to "main" only

### C.4.2 Service Account Separation

**CI/CD Service Accounts per Environment**:

- **Development Pipeline**: Uses dev-cicd-service-account
  - Permissions: Deploy to dev environment only
  - Cannot access test, staging, or production credentials
  
- **Testing Pipeline**: Uses test-cicd-service-account
  - Permissions: Deploy to test environment only
  
- **Production Pipeline**: Uses prod-cicd-service-account
  - Permissions: Deploy to staging and production environments
  - Highly restricted (only operations team can use)
  - All actions logged and audited

**AWS IAM Example**:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ec2:*",
        "s3:*",
        "rds:*"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:RequestedRegion": "us-east-1",
          "ec2:ResourceTag/Environment": "production"
        }
      }
    }
  ]
}
```

---

## C.5 Environment Validation in Pipelines

### C.5.1 Pre-Deployment Validation

**Validation Checks Before Deployment**:

```bash
#!/bin/bash
# validate_deployment.sh

TARGET_ENV=$1
ARTIFACT=$2

# 1. Validate environment name
if [[ ! "$TARGET_ENV" =~ ^(dev|test|staging|prod)$ ]]; then
    echo "ERROR: Invalid target environment: $TARGET_ENV"
    exit 1
fi

# 2. Validate artifact is tagged for this environment
ARTIFACT_ENV=$(docker inspect --format='{{index .Config.Labels "environment"}}' $ARTIFACT)
if [ "$ARTIFACT_ENV" != "$TARGET_ENV" ]; then
    echo "ERROR: Artifact is tagged for $ARTIFACT_ENV but deploying to $TARGET_ENV"
    exit 1
fi

# 3. Check if production deployment window is active
if [ "$TARGET_ENV" == "prod" ]; then
    CURRENT_HOUR=$(date +%H)
    # Production deployments only 02:00-06:00 UTC
    if [ $CURRENT_HOUR -lt 2 ] || [ $CURRENT_HOUR -gt 6 ]; then
        echo "ERROR: Production deployments only allowed 02:00-06:00 UTC"
        exit 1
    fi
fi

# 4. Verify all tests passed
if ! check_test_results "$ARTIFACT"; then
    echo "ERROR: Not all tests passed for this artifact"
    exit 1
fi

echo "✅ Deployment validation passed for $TARGET_ENV"
exit 0
```

### C.5.2 Post-Deployment Validation

**Smoke Tests After Deployment**:

```yaml
# GitLab CI smoke test example
deploy_to_production:
  stage: deploy
  environment: production
  script:
    - ./deploy.sh --env production
    - ./smoke_tests.sh --env production
  only:
    - main
  when: manual

# smoke_tests.sh
#!/bin/bash
ENV=$1

# Check application is responding
if ! curl -f https://app-${ENV}.example.com/health; then
    echo "ERROR: Application health check failed"
    ./rollback.sh --env $ENV
    exit 1
fi

# Check database connectivity
if ! ./check_db.sh --env $ENV; then
    echo "ERROR: Database connectivity check failed"
    ./rollback.sh --env $ENV
    exit 1
fi

echo "✅ Smoke tests passed for $ENV"
```

---

## C.6 Audit Logging and Monitoring

### C.6.1 Pipeline Audit Requirements

**What Must Be Logged**:
- Who triggered the deployment
- Target environment
- Artifact/version deployed
- Timestamp (start and end)
- Success or failure
- Approval chain (for production)
- Rollback events (if occurred)

**Log Retention**:
- Development/Test: 90 days
- Staging: 6 months
- Production: 7 years (regulatory compliance)

**Example Log Entry**:
```json
{
  "timestamp": "2026-01-11T14:32:00Z",
  "event": "deployment",
  "environment": "production",
  "triggered_by": "ops-user@example.com",
  "artifact": "myapp:v2.3.1",
  "approvers": ["change-manager@example.com", "senior-ops@example.com"],
  "pipeline_id": "pipeline-12345",
  "result": "success",
  "duration_seconds": 187,
  "rollback": false
}
```

### C.6.2 Alerting for Policy Violations

**Alert Conditions**:
- Deployment to production without approval
- Deployment outside approved change window
- Failed environment validation (wrong artifact → wrong environment)
- Service account misuse (dev account trying to deploy to prod)
- Deployment to production by non-operations personnel

**Example Alert Configuration** (Prometheus/Alertmanager):
```yaml
groups:
  - name: deployment_violations
    rules:
      - alert: UnauthorizedProductionDeployment
        expr: |
          deployment_events{environment="production", authorized="false"} > 0
        for: 1m
        labels:
          severity: critical
        annotations:
          summary: "Unauthorized production deployment detected"
          description: "Deployment to production without proper authorization"
```

---

## C.7 Technology-Specific Examples

### C.7.1 Jenkins Pipeline

**Jenkinsfile for Environment Separation**:
```groovy
pipeline {
    agent any
    
    parameters {
        choice(
            name: 'TARGET_ENV',
            choices: ['dev', 'test', 'staging', 'prod'],
            description: 'Target deployment environment'
        )
    }
    
    stages {
        stage('Validate') {
            steps {
                script {
                    // Validate target environment
                    if (params.TARGET_ENV == 'prod' && !isAuthorized()) {
                        error("User ${env.USER} not authorized for production deployment")
                    }
                }
            }
        }
        
        stage('Build') {
            steps {
                sh './build.sh'
            }
        }
        
        stage('Test') {
            steps {
                sh './run_tests.sh'
            }
        }
        
        stage('Deploy') {
            when {
                expression {
                    // Auto-deploy to dev/test, manual for staging/prod
                    params.TARGET_ENV in ['dev', 'test'] || 
                    currentBuild.rawBuild.getCause(hudson.model.Cause$UserIdCause) != null
                }
            }
            steps {
                script {
                    // Production requires additional approval
                    if (params.TARGET_ENV == 'prod') {
                        input message: 'Deploy to Production?', 
                              ok: 'Deploy',
                              submitter: 'operations-team'
                    }
                    
                    // Load environment-specific credentials
                    withCredentials([
                        string(credentialsId: "${params.TARGET_ENV}-deploy-key", variable: 'DEPLOY_KEY')
                    ]) {
                        sh "./deploy.sh --env ${params.TARGET_ENV} --key ${DEPLOY_KEY}"
                    }
                }
            }
        }
        
        stage('Smoke Test') {
            steps {
                sh "./smoke_test.sh --env ${params.TARGET_ENV}"
            }
        }
    }
    
    post {
        always {
            // Log deployment event
            script {
                sh """
                echo '{
                    "timestamp": "${new Date()}",
                    "environment": "${params.TARGET_ENV}",
                    "user": "${env.USER}",
                    "build": "${env.BUILD_NUMBER}",
                    "result": "${currentBuild.currentResult}"
                }' | tee -a /var/log/deployments.json
                """
            }
        }
        failure {
            // Alert on production deployment failure
            script {
                if (params.TARGET_ENV == 'prod') {
                    mail to: 'ops-team@example.com',
                         subject: "ALERT: Production deployment failed",
                         body: "Build ${env.BUILD_NUMBER} failed"
                }
            }
        }
    }
}
```

### C.7.2 GitLab CI/CD

**. gitlab-ci.yml for Environment Separation**:
```yaml
stages:
  - build
  - test
  - deploy_dev
  - deploy_test
  - deploy_staging
  - deploy_prod

variables:
  DOCKER_REGISTRY: "registry.example.com"

build:
  stage: build
  script:
    - docker build -t ${DOCKER_REGISTRY}/myapp:${CI_COMMIT_SHA} .
    - docker push ${DOCKER_REGISTRY}/myapp:${CI_COMMIT_SHA}
  only:
    - branches

test:
  stage: test
  script:
    - ./run_unit_tests.sh
    - ./run_integration_tests.sh

deploy_to_dev:
  stage: deploy_dev
  environment:
    name: development
  script:
    - ./deploy.sh --env dev --version ${CI_COMMIT_SHA}
  only:
    - develop

deploy_to_test:
  stage: deploy_test
  environment:
    name: testing
  script:
    - ./deploy.sh --env test --version ${CI_COMMIT_SHA}
  only:
    - develop
  when: on_success

deploy_to_staging:
  stage: deploy_staging
  environment:
    name: staging
  script:
    - ./deploy.sh --env staging --version ${CI_COMMIT_SHA}
  only:
    - main
  when: manual

deploy_to_production:
  stage: deploy_prod
  environment:
    name: production
    on_stop: rollback_production
  script:
    - ./deploy.sh --env prod --version ${CI_COMMIT_SHA}
    - ./smoke_test.sh --env prod
  only:
    - main
  when: manual
  allow_failure: false

rollback_production:
  stage: deploy_prod
  environment:
    name: production
    action: stop
  script:
    - ./rollback.sh --env prod
  when: manual
  only:
    - main
```

### C.7.3 GitHub Actions

**.github/workflows/deploy.yml**:
```yaml
name: Deploy Pipeline

on:
  push:
    branches:
      - main
      - develop

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Build
        run: |
          docker build -t myapp:${{ github.sha }} .
      
      - name: Test
        run: |
          ./run_tests.sh
  
  deploy_dev:
    needs: build
    if: github.ref == 'refs/heads/develop'
    runs-on: ubuntu-latest
    environment: development
    steps:
      - uses: actions/checkout@v3
      
      - name: Deploy to Dev
        env:
          DEPLOY_KEY: ${{ secrets.DEV_DEPLOY_KEY }}
        run: |
          ./deploy.sh --env dev --key $DEPLOY_KEY
  
  deploy_test:
    needs: deploy_dev
    if: github.ref == 'refs/heads/develop'
    runs-on: ubuntu-latest
    environment: testing
    steps:
      - uses: actions/checkout@v3
      
      - name: Deploy to Test
        env:
          DEPLOY_KEY: ${{ secrets.TEST_DEPLOY_KEY }}
        run: |
          ./deploy.sh --env test --key $DEPLOY_KEY
  
  deploy_staging:
    needs: build
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    environment: staging
    steps:
      - uses: actions/checkout@v3
      
      - name: Deploy to Staging
        env:
          DEPLOY_KEY: ${{ secrets.STAGING_DEPLOY_KEY }}
        run: |
          ./deploy.sh --env staging --key $DEPLOY_KEY
  
  deploy_production:
    needs: deploy_staging
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    environment:
      name: production
      # Requires approval from "production-deployers" team
    steps:
      - uses: actions/checkout@v3
      
      - name: Deploy to Production
        env:
          DEPLOY_KEY: ${{ secrets.PROD_DEPLOY_KEY }}
        run: |
          ./deploy.sh --env prod --key $DEPLOY_KEY
          ./smoke_test.sh --env prod
```

---

## C.8 Rollback Procedures

### C.8.1 Automated Rollback

**Rollback Triggers**:
- Smoke test failure post-deployment
- Health check failures exceeding threshold
- Critical errors in application logs
- Manual rollback request (emergency)

**Rollback Script Example**:
```bash
#!/bin/bash
# rollback.sh

ENV=$1
PREVIOUS_VERSION=$2

echo "Rolling back $ENV to version $PREVIOUS_VERSION"

# Re-deploy previous version
./deploy.sh --env $ENV --version $PREVIOUS_VERSION

# Verify rollback success
if ./smoke_test.sh --env $ENV; then
    echo "✅ Rollback successful"
    # Log rollback event
    log_event "rollback" "$ENV" "$PREVIOUS_VERSION" "success"
else
    echo "❌ Rollback failed - manual intervention required"
    alert_operations "Rollback failed for $ENV"
    exit 1
fi
```

### C.8.2 Rollback Testing

**Requirements**:
- Rollback procedures tested quarterly in staging
- Rollback from production tested annually (planned maintenance window)
- Rollback time measured and documented (RTO metric)

---

## C.9 Compliance and Audit

### C.9.1 Pipeline Audit Checklist

For audit purposes, [Organization] must demonstrate:

- ✅ Separate pipeline configurations per environment
- ✅ Production deployments require manual approval
- ✅ Deployment audit logs retained per policy (7 years for production)
- ✅ Service accounts separate per environment
- ✅ Secrets separated per environment (no shared credentials)
- ✅ Environment validation implemented (prevent wrong artifact → wrong env)
- ✅ Smoke tests run post-deployment
- ✅ Rollback procedures documented and tested
- ✅ Alerting configured for policy violations
- ✅ Access controls enforce "operations-only" production deployment

### C.9.2 Continuous Compliance Monitoring

**Automated Checks**:
- Weekly: Scan pipeline configurations for policy violations
- Monthly: Review deployment logs for unauthorized deployments
- Quarterly: Test rollback procedures
- Annual: Full pipeline security audit

---

**Document Approval**:

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Policy Owner (CISO) | [Name] | ________________ | [Date] |
| DevOps Lead | [Name] | ________________ | [Date] |
| IT Operations Manager | [Name] | ________________ | [Date] |
| Information Security Manager | [Name] | ________________ | [Date] |

---

*End of Annex C - ISMS-POL-A.8.31-Annex-C*
