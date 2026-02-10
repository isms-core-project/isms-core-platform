<!-- ISMS-CORE:REF:ISMS-REF-A.8.31-cicd-pipeline-integration:framework:REF:a.8.31 -->
**ISMS-REF-A.8.31 – CI/CD Pipeline Integration Reference**
**Technical Reference for Deployment Pipeline Implementation**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | CI/CD Pipeline Integration Reference |
| **Document Type** | Reference Document (Non-ISMS Technical Reference) |
| **Document ID** | ISMS-REF-A.8.31-CICD |
| **Document Creator** | DevOps Lead / IT Operations Manager |
| **Document Owner** | Chief Information Security Officer (CISO) |
| **Approved By** | DevOps Lead (Technical Reference - No Executive Approval Required) |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Version Date** | [To Be Determined] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | DevOps / IT Operations | Initial technical reference for CI/CD pipeline integration |

**Review Cycle**: As needed (technology and tool evolution)  
**Next Review Date**: [Date + 12 months]  
**Approvers**: DevOps Lead / IT Operations Manager (technical reference, no ISMS approval required)

**Distribution**: DevOps Engineers, Development Teams, IT Operations (for technical implementation awareness)

---

⚠️ **IMPORTANT – NON-ISMS TECHNICAL SUPPORT DOCUMENT**

This document is provided for informational and awareness purposes only.

- This document is NOT part of the Information Security Management System (ISMS).
- This document does NOT define mandatory CI/CD pipeline controls or requirements.
- This document does NOT establish binding requirements, deadlines, KPIs, or SLAs.
- This document does NOT mandate the use, prohibition, or configuration of specific CI/CD platforms, tools, or configurations.
- This document does NOT override or extend any ISMS policy.

All binding environment separation requirements, obligations, and governance decisions are defined exclusively in **ISMS-POL-A.8.31 (Environment Separation Policy)** and other approved ISMS documentation.

This document serves solely as a technical reference to:

- Describe commonly used CI/CD pipeline patterns
- Provide platform-specific configuration examples
- Support deployment automation implementation
- Inform technical discussions and future implementation planning
- **This document must not be used as audit evidence of implementation**

Use of this document does not imply implementation, compliance, or operational maturity.

**Critical Positioning Statement**:
This document intentionally provides technical detail beyond what is required for ISO/IEC 27001 policy documentation. Its purpose is technical awareness only. No auditor conclusions shall be drawn from the presence, absence, or classification of any pipeline pattern, platform, or configuration listed herein.

---

# Document Purpose and Scope

## Purpose

This document provides technical reference patterns for integrating environment separation controls into CI/CD pipelines. It is intended to support:

- Technical awareness of pipeline security patterns
- Understanding of environment-specific deployment workflows
- Context for CI/CD platform selection and configuration
- Future implementation planning discussions
- Tool and platform evaluation criteria

## What This Document Is NOT

This document does NOT:

- Define [Organization]'s required or prohibited CI/CD platforms
- Establish mandatory pipeline configurations
- Create compliance obligations or audit criteria
- Replace ISMS-POL-A.8.31 policy requirements
- Mandate specific tools or vendors
- Replace vendor documentation or best practices

## Relationship to ISMS Policy

**Binding Requirements**: ISMS-POL-A.8.31 defines **WHAT** environment promotion controls are required (controlled promotion path, approval gates, etc.)

**This Document**: Provides **HOW** those requirements can be implemented in CI/CD platforms (Jenkins, GitLab CI, GitHub Actions, etc.)

Organizations choose CI/CD platforms and configurations appropriate to their needs. The requirement is controlled promotion; the implementation varies.

---

# CI/CD Pipeline Architecture for Environment Separation

## Pipeline Structure

**Environment-Aware Pipeline Design**:

```
┌─────────────────────────────────────────────────────────┐
│              SOURCE CODE REPOSITORY                      │
│             (Git, GitHub, GitLab, etc.)                  │
└──────────────────────┬──────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────┐
│         CI/CD ORCHESTRATION PLATFORM                     │
│     (Jenkins, GitLab CI, GitHub Actions, etc.)           │
└──────────────────────┬──────────────────────────────────┘
                       │
       ┌───────────────┼───────────────┬─────────────────┐
       │               │               │                 │
       ▼               ▼               ▼                 ▼
  ┌────────┐     ┌────────┐     ┌────────┐     ┌────────┐
  │  DEV   │     │  TEST  │     │ STAGING│     │  PROD  │
  │PIPELINE│     │PIPELINE│     │PIPELINE│     │PIPELINE│
  └────┬───┘     └────┬───┘     └────┬───┘     └────┬───┘
       │              │              │              │
       │     AUTO     │     AUTO     │    MANUAL    │
       │     ↓        │     ↓        │     ↓        │
       ▼              ▼              ▼              ▼
  ┌────────┐     ┌────────┐     ┌────────┐     ┌────────┐
  │  DEV   │     │  TEST  │     │ STAGING│     │  PROD  │
  │  ENV   │     │  ENV   │     │  ENV   │     │  ENV   │
  └────────┘     └────────┘     └────────┘     └────────┘
```

**Key Principles**:

- Separate pipeline jobs/stages per environment
- Automated promotion from dev → test → staging
- Manual approval gate before production deployment
- Environment validation at each stage
- Credentials separated per environment

## Deployment Gates and Approvals

**Approval Requirements by Environment**:

| From → To | Approval Type | Who Approves | Additional Checks |
|-----------|---------------|--------------|-------------------|
| Dev → Test | Automatic | None (on successful build) | Unit tests pass (100%) |
| Test → Staging | Automatic or Semi-Auto | QA Lead (optional) | Integration tests pass |
| Staging → Production | **MANUAL** | Change Advisory Board (CAB) | All tests pass, CAB approval, deployment window check |

**Production Deployment Gate Requirements**:

- Explicit manual approval required
- Approval from authorized personnel only (operations team, change manager)
- Deployment restricted to approved change windows
- Rollback plan documented and accessible
- Smoke tests defined for post-deployment validation
- Monitoring dashboards reviewed before approval

## Environment Validation

**Pre-Deployment Validation Checklist**:

```yaml
# Pseudo-code for environment validation
validate_environment:

  - check_target_environment_is_correct
  - verify_credentials_match_target_environment
  - confirm_no_production_credentials_in_non_prod
  - validate_network_connectivity_to_target
  - check_resource_availability (CPU, memory, disk)
  - verify_deployment_window_is_open (for production)

```

---

# Platform-Specific Examples

## Jenkins Pipeline

**Jenkinsfile with Environment Separation**:

```groovy
pipeline {
    agent any
    
    parameters {
        choice(name: 'ENVIRONMENT', 
               choices: ['dev', 'test', 'staging', 'production'], 
               description: 'Target environment for deployment')
    }
    
    environment {
        APP_NAME = 'webapp'
        ARTIFACT_PATH = "${WORKSPACE}/build/app.jar"
    }
    
    stages {
        stage('Build') {
            steps {
                echo "Building application..."
                sh 'mvn clean package'
            }
        }
        
        stage('Unit Tests') {
            steps {
                sh 'mvn test'
                junit 'target/surefire-reports/*.xml'
            }
        }
        
        stage('Deploy to Dev') {
            when {
                expression { params.ENVIRONMENT == 'dev' }
            }
            steps {
                deployToEnvironment('dev')
            }
        }
        
        stage('Integration Tests') {
            when {
                expression { params.ENVIRONMENT in ['test', 'staging', 'production'] }
            }
            steps {
                sh 'mvn verify -Pintegration-tests'
            }
        }
        
        stage('Deploy to Test') {
            when {
                expression { params.ENVIRONMENT == 'test' }
            }
            steps {
                deployToEnvironment('test')
            }
        }
        
        stage('Deploy to Staging') {
            when {
                expression { params.ENVIRONMENT == 'staging' }
            }
            steps {
                input message: 'Approve deployment to Staging?', 
                      submitter: 'qa-team'
                deployToEnvironment('staging')
            }
        }
        
        stage('Production Approval Gate') {
            when {
                expression { params.ENVIRONMENT == 'production' }
            }
            steps {
                script {
                    // Check if deployment window is open
                    def currentHour = new Date().getHours()
                    if (currentHour < 9 || currentHour > 17) {
                        error("Production deployment only allowed 9am-5pm")
                    }
                }
                
                // Require CAB approval
                input message: 'CAB Approval Required for PRODUCTION', 
                      submitter: 'change-advisory-board,operations-team',
                      parameters: [
                          string(name: 'CAB_TICKET', description: 'CAB approval ticket number'),
                          text(name: 'ROLLBACK_PLAN', description: 'Describe rollback procedure')
                      ]
            }
        }
        
        stage('Deploy to Production') {
            when {
                expression { params.ENVIRONMENT == 'production' }
            }
            steps {
                deployToEnvironment('production')
                
                // Post-deployment smoke tests
                sh './scripts/smoke-tests.sh production'
            }
        }
        
        stage('Post-Deployment Validation') {
            steps {
                echo "Running post-deployment validation..."
                sh "./scripts/validate-deployment.sh ${params.ENVIRONMENT}"
            }
        }
    }
    
    post {
        success {
            echo "Deployment to ${params.ENVIRONMENT} successful!"
            // Notify via Slack, email, etc.
        }
        failure {
            echo "Deployment to ${params.ENVIRONMENT} FAILED!"
            // Alert operations team
        }
    }
}

def deployToEnvironment(environment) {
    withCredentials([
        string(credentialsId: "${environment}-api-key", variable: 'API_KEY'),
        usernamePassword(credentialsId: "${environment}-db-creds", 
                         usernameVariable: 'DB_USER', 
                         passwordVariable: 'DB_PASS')
    ]) {
        echo "Deploying to ${environment}..."
        sh """
            ./deploy.sh \\
                --environment ${environment} \\
                --artifact ${ARTIFACT_PATH} \\
                --api-key \$API_KEY
        """
    }
}
```

**Key Features**:

- Environment parameter validation
- Separate credentials per environment (Jenkins Credentials Plugin)
- Production approval gate with CAB requirement
- Deployment window enforcement (production only during business hours)
- Post-deployment smoke tests
- Rollback plan documentation required

## GitLab CI/CD

**.gitlab-ci.yml with Environment Separation**:

```yaml
stages:

  - build
  - test
  - deploy-dev
  - deploy-test
  - deploy-staging
  - deploy-production

variables:
  APP_NAME: "webapp"

build:
  stage: build
  image: maven:3.8-openjdk-17
  script:

    - mvn clean package

  artifacts:
    paths:

      - target/app.jar

    expire_in: 1 week

unit-tests:
  stage: test
  image: maven:3.8-openjdk-17
  script:

    - mvn test

  artifacts:
    reports:
      junit: target/surefire-reports/TEST-*.xml

deploy-dev:
  stage: deploy-dev
  image: google/cloud-sdk:alpine
  environment:
    name: development
    url: https://dev.example.com
  script:

    - gcloud auth activate-service-account --key-file=$GCP_DEV_KEY
    - gcloud app deploy --project=dev-project

  only:

    - develop

  variables:
    ENVIRONMENT: "dev"

integration-tests:
  stage: test
  image: maven:3.8-openjdk-17
  script:

    - mvn verify -Pintegration-tests

  only:

    - develop
    - main

deploy-test:
  stage: deploy-test
  image: google/cloud-sdk:alpine
  environment:
    name: testing
    url: https://test.example.com
  script:

    - gcloud auth activate-service-account --key-file=$GCP_TEST_KEY
    - gcloud app deploy --project=test-project

  only:

    - main

  variables:
    ENVIRONMENT: "test"

deploy-staging:
  stage: deploy-staging
  image: google/cloud-sdk:alpine
  environment:
    name: staging
    url: https://staging.example.com
  script:

    - gcloud auth activate-service-account --key-file=$GCP_STAGING_KEY
    - gcloud app deploy --project=staging-project

  when: manual  # Require manual trigger
  only:

    - main

  variables:
    ENVIRONMENT: "staging"

deploy-production:
  stage: deploy-production
  image: google/cloud-sdk:alpine
  environment:
    name: production
    url: https://example.com
  script:
    # Production deployment with validation

    - echo "Deploying to PRODUCTION..."
    - gcloud auth activate-service-account --key-file=$GCP_PROD_KEY
    - gcloud app deploy --project=prod-project
    
    # Post-deployment smoke tests

    - ./scripts/smoke-tests.sh production

  when: manual  # MANUAL approval required
  only:

    - main  # Only from main branch

  allow_failure: false  # Deployment failure stops pipeline
  variables:
    ENVIRONMENT: "production"
  # Production deployment restricted to specific users
  rules:

    - if: '$CI_COMMIT_BRANCH == "main"'

      when: manual
      allow_failure: false
```

**Key Features**:

- Separate stages per environment
- Environment-specific service accounts (GCP_DEV_KEY, GCP_TEST_KEY, etc.)
- Manual approval for staging and production (`when: manual`)
- Branch protection (only main branch can deploy to production)
- Post-deployment smoke tests for production
- Environment URLs tracked (dev.example.com, test.example.com, etc.)

**GitLab Protected Environments**:

Configure in GitLab UI:

- Settings → CI/CD → Protected Environments
- Production: Only `operations-team` group can deploy
- Staging: Only `qa-team` and `operations-team` can deploy

## GitHub Actions

**.github/workflows/deploy.yml with Environment Separation**:

```yaml
name: Deploy to Environments

on:
  push:
    branches:

      - develop  # Triggers dev deployment
      - main    # Triggers test/staging/prod workflows

jobs:
  build:
    runs-on: ubuntu-latest
    steps:

      - uses: actions/checkout@v3
      
      - name: Set up JDK 17

        uses: actions/setup-java@v3
        with:
          java-version: '17'
          distribution: 'temurin'
      
      - name: Build with Maven

        run: mvn clean package
      
      - name: Upload artifact

        uses: actions/upload-artifact@v3
        with:
          name: app-jar
          path: target/app.jar

  unit-tests:
    runs-on: ubuntu-latest
    needs: build
    steps:

      - uses: actions/checkout@v3
      - name: Run unit tests

        run: mvn test

  deploy-dev:
    runs-on: ubuntu-latest
    needs: [build, unit-tests]
    if: github.ref == 'refs/heads/develop'
    environment:
      name: development
      url: https://dev.example.com
    steps:

      - uses: actions/checkout@v3
      
      - name: Download artifact

        uses: actions/download-artifact@v3
        with:
          name: app-jar
      
      - name: Deploy to Dev (AWS)

        env:
          AWS_ACCESS_KEY_ID: ${{ secrets.AWS_DEV_ACCESS_KEY }}
          AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_DEV_SECRET_KEY }}
          AWS_REGION: eu-central-1
        run: |
          aws s3 cp app.jar s3://dev-deployment-bucket/
          aws lambda update-function-code \
            --function-name dev-webapp \
            --s3-bucket dev-deployment-bucket \
            --s3-key app.jar

  integration-tests:
    runs-on: ubuntu-latest
    needs: deploy-dev
    if: github.ref == 'refs/heads/main' || github.ref == 'refs/heads/develop'
    steps:

      - uses: actions/checkout@v3
      - name: Run integration tests

        run: mvn verify -Pintegration-tests

  deploy-test:
    runs-on: ubuntu-latest
    needs: [build, integration-tests]
    if: github.ref == 'refs/heads/main'
    environment:
      name: testing
      url: https://test.example.com
    steps:

      - uses: actions/checkout@v3
      - name: Deploy to Test

        env:
          AWS_ACCESS_KEY_ID: ${{ secrets.AWS_TEST_ACCESS_KEY }}
          AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_TEST_SECRET_KEY }}
        run: |
          aws lambda update-function-code \
            --function-name test-webapp \
            --s3-bucket test-deployment-bucket \
            --s3-key app.jar

  deploy-staging:
    runs-on: ubuntu-latest
    needs: deploy-test
    if: github.ref == 'refs/heads/main'
    environment:
      name: staging
      url: https://staging.example.com
    steps:

      - uses: actions/checkout@v3
      - name: Deploy to Staging

        env:
          AWS_ACCESS_KEY_ID: ${{ secrets.AWS_STAGING_ACCESS_KEY }}
          AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_STAGING_SECRET_KEY }}
        run: |
          aws lambda update-function-code \
            --function-name staging-webapp \
            --s3-bucket staging-deployment-bucket \
            --s3-key app.jar

  deploy-production:
    runs-on: ubuntu-latest
    needs: deploy-staging
    if: github.ref == 'refs/heads/main'
    environment:
      name: production
      url: https://example.com
    steps:

      - uses: actions/checkout@v3
      
      - name: Download artifact

        uses: actions/download-artifact@v3
        with:
          name: app-jar
      
      - name: Deploy to Production

        env:
          AWS_ACCESS_KEY_ID: ${{ secrets.AWS_PROD_ACCESS_KEY }}
          AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_PROD_SECRET_KEY }}
        run: |
          echo "Deploying to PRODUCTION..."
          aws lambda update-function-code \
            --function-name prod-webapp \
            --s3-bucket prod-deployment-bucket \
            --s3-key app.jar
      
      - name: Run smoke tests

        run: |
          ./scripts/smoke-tests.sh production
      
      - name: Notify deployment success

        run: |
          echo "Production deployment successful!"
          # Send Slack notification, PagerDuty event, etc.
```

**GitHub Environment Protection Rules** (Configure in GitHub UI):

Repository → Settings → Environments

**Production Environment**:

- Required reviewers: `operations-team` (at least 2 approvals)
- Deployment branches: Only `main` branch
- Wait timer: 5 minutes (cooling-off period)
- Environment secrets: `AWS_PROD_ACCESS_KEY`, `AWS_PROD_SECRET_KEY`

**Staging Environment**:

- Required reviewers: `qa-team` (at least 1 approval)
- Deployment branches: Only `main` branch

## Azure DevOps Pipelines

**azure-pipelines.yml with Environment Separation**:

```yaml
trigger:
  branches:
    include:

      - develop
      - main

pool:
  vmImage: 'ubuntu-latest'

variables:
  buildConfiguration: 'Release'

stages:

- stage: Build

  jobs:

  - job: BuildJob

    steps:

    - task: Maven@3

      inputs:
        mavenPomFile: 'pom.xml'
        goals: 'clean package'
        publishJUnitResults: true
        testResultsFiles: '**/surefire-reports/TEST-*.xml'
    
    - task: PublishBuildArtifacts@1

      inputs:
        PathtoPublish: 'target/app.jar'
        ArtifactName: 'app'

- stage: DeployDev

  dependsOn: Build
  condition: eq(variables['Build.SourceBranch'], 'refs/heads/develop')
  jobs:

  - deployment: DeployDevJob

    environment: 'Development'
    strategy:
      runOnce:
        deploy:
          steps:

          - task: AzureWebApp@1

            inputs:
              azureSubscription: 'Azure-Dev-ServiceConnection'
              appName: 'webapp-dev'
              package: '$(Pipeline.Workspace)/app/app.jar'

- stage: DeployTest

  dependsOn: Build
  condition: eq(variables['Build.SourceBranch'], 'refs/heads/main')
  jobs:

  - deployment: DeployTestJob

    environment: 'Testing'
    strategy:
      runOnce:
        deploy:
          steps:

          - task: AzureWebApp@1

            inputs:
              azureSubscription: 'Azure-Test-ServiceConnection'
              appName: 'webapp-test'
              package: '$(Pipeline.Workspace)/app/app.jar'

- stage: DeployStaging

  dependsOn: DeployTest
  condition: eq(variables['Build.SourceBranch'], 'refs/heads/main')
  jobs:

  - deployment: DeployStagingJob

    environment: 'Staging'
    strategy:
      runOnce:
        deploy:
          steps:

          - task: AzureWebApp@1

            inputs:
              azureSubscription: 'Azure-Staging-ServiceConnection'
              appName: 'webapp-staging'
              package: '$(Pipeline.Workspace)/app/app.jar'

- stage: DeployProduction

  dependsOn: DeployStaging
  condition: eq(variables['Build.SourceBranch'], 'refs/heads/main')
  jobs:

  - deployment: DeployProductionJob

    environment: 'Production'  # Requires manual approval in Azure DevOps
    strategy:
      runOnce:
        deploy:
          steps:

          - task: AzureWebApp@1

            inputs:
              azureSubscription: 'Azure-Prod-ServiceConnection'
              appName: 'webapp-prod'
              package: '$(Pipeline.Workspace)/app/app.jar'
          
          - script: |

              ./scripts/smoke-tests.sh production
            displayName: 'Run production smoke tests'
```

**Azure DevOps Environment Approvals** (Configure in Azure DevOps UI):

Pipelines → Environments → Production

**Approvals and Checks**:

- Required approvers: Add `Operations Team`, minimum 2 approvals
- Timeout: 30 days (pipeline waits for approval)
- Business hours gate: Only allow deployments 9am-5pm
- Branch control: Only `main` branch

---

# Infrastructure as Code (IaC) Integration

## Terraform Environment Patterns

**Directory Structure**:

```
terraform/
├── environments/
│   ├── dev/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   └── terraform.tfvars
│   ├── test/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   └── terraform.tfvars
│   ├── staging/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   └── terraform.tfvars
│   └── prod/
│       ├── main.tf
│       ├── variables.tf
│       └── terraform.tfvars
└── modules/
    └── webapp/
        ├── main.tf
        ├── variables.tf
        └── outputs.tf
```

**Environment-Specific Configuration (terraform.tfvars)**:

**dev/terraform.tfvars**:
```hcl
environment = "dev"
instance_type = "t3.small"
min_size = 1
max_size = 3
enable_deletion_protection = false
backup_retention_days = 7
```

**prod/terraform.tfvars**:
```hcl
environment = "prod"
instance_type = "t3.large"
min_size = 3
max_size = 10
enable_deletion_protection = true
backup_retention_days = 30
```

**Pipeline Integration (GitLab CI)**:

```yaml
terraform-dev:
  stage: deploy-dev
  image: hashicorp/terraform:latest
  script:

    - cd terraform/environments/dev
    - terraform init -backend-config="key=dev/terraform.tfstate"
    - terraform plan
    - terraform apply -auto-approve

  only:

    - develop

terraform-prod:
  stage: deploy-production
  image: hashicorp/terraform:latest
  script:

    - cd terraform/environments/prod
    - terraform init -backend-config="key=prod/terraform.tfstate"
    - terraform plan -out=tfplan
    - terraform apply tfplan

  when: manual
  only:

    - main

```

## Ansible Environment Variables

**Inventory Structure**:

```
ansible/
├── inventories/
│   ├── dev/
│   │   ├── hosts
│   │   └── group_vars/
│   │       └── all.yml
│   ├── test/
│   │   ├── hosts
│   │   └── group_vars/
│   │       └── all.yml
│   └── prod/
│       ├── hosts
│       └── group_vars/
│           └── all.yml
└── playbooks/
    └── deploy.yml
```

**Environment-Specific Variables**:

**dev/group_vars/all.yml**:
```yaml
environment: dev
app_version: latest
database_host: dev-db.internal
enable_debug_mode: true
```

**prod/group_vars/all.yml**:
```yaml
environment: prod
app_version: "1.5.2"  # Specific version
database_host: prod-db.internal
enable_debug_mode: false
```

**Pipeline Integration**:

```bash
# Deploy to dev
ansible-playbook -i inventories/dev playbooks/deploy.yml

# Deploy to production (manual)
ansible-playbook -i inventories/prod playbooks/deploy.yml
```

---

# Security Controls in Pipelines

## Service Account Separation

**Best Practice**: Separate service accounts/credentials per environment

**AWS Example**:

- Dev pipeline: Uses IAM role `dev-deployment-role`
- Test pipeline: Uses IAM role `test-deployment-role`
- Production pipeline: Uses IAM role `prod-deployment-role`

**Azure Example**:

- Dev pipeline: Uses Service Principal `dev-sp`
- Production pipeline: Uses Service Principal `prod-sp`

**Why**: If dev pipeline compromised, attacker cannot deploy to production.

## Secrets Management by Environment

**HashiCorp Vault Integration**:

```groovy
// Jenkins pipeline with Vault
pipeline {
    agent any
    
    stages {
        stage('Deploy') {
            steps {
                script {
                    def secrets = [
                        [path: "${ENVIRONMENT}/database", 
                         secretValues: [
                             [envVar: 'DB_PASSWORD', vaultKey: 'password']
                         ]]
                    ]
                    
                    withVault([vaultSecrets: secrets]) {
                        sh "./deploy.sh --db-password ${DB_PASSWORD}"
                    }
                }
            }
        }
    }
}
```

**Vault Paths by Environment**:

- `dev/database/password`
- `test/database/password`
- `prod/database/password`

## Deployment Monitoring and Alerting

**Post-Deployment Validation**:

```bash
#!/bin/bash
# smoke-tests.sh

ENVIRONMENT=$1
APP_URL="https://${ENVIRONMENT}.example.com"

# Health check
if curl -f "${APP_URL}/health" > /dev/null 2>&1; then
    echo "✅ Health check passed"
else
    echo "❌ Health check FAILED"
    exit 1
fi

# Database connectivity
if curl -f "${APP_URL}/db-check" > /dev/null 2>&1; then
    echo "✅ Database connectivity OK"
else
    echo "❌ Database connectivity FAILED"
    exit 1
fi

# Performance check (response time < 2 seconds)
RESPONSE_TIME=$(curl -o /dev/null -s -w '%{time_total}' "${APP_URL}")
if (( $(echo "$RESPONSE_TIME < 2.0" | bc -l) )); then
    echo "✅ Response time OK (${RESPONSE_TIME}s)"
else
    echo "❌ Response time too slow (${RESPONSE_TIME}s)"
    exit 1
fi

echo "All smoke tests passed!"
```

---

# Common Pitfalls and Best Practices

## What NOT to Do

❌ **Shared Credentials Across Environments**:

- Production and dev using same AWS IAM role → Security risk

❌ **No Approval Gate for Production**:

- Automatic deployment to production → Untested changes reach customers

❌ **Production Secrets in Code**:

- `DATABASE_PASSWORD=prod_secret_123` hardcoded in pipeline → Exposed in logs

❌ **Direct Production Deployment**:

- Pipeline bypasses staging → No validation before production

❌ **No Rollback Plan**:

- Deployment fails → No documented recovery procedure

## Best Practices

✅ Separate credentials per environment  
✅ Manual approval gate for production  
✅ Secrets stored in vault (HashiCorp Vault, AWS Secrets Manager)  
✅ Mandatory promotion path (dev → test → staging → prod)  
✅ Automated rollback on failure  
✅ Post-deployment smoke tests  
✅ Deployment monitoring (Datadog, New Relic)  
✅ Audit logging (who deployed what, when)  
✅ Branch protection (only main branch → production)  
✅ Change window enforcement (production only during approved hours)

---

**END OF REFERENCE DOCUMENT**

---

*This technical reference supports ISMS-POL-A.8.31. CI/CD pipeline configurations should be reviewed and approved by DevOps Lead and CISO.*

<!-- QA_VERIFIED: 2026-02-01 -->
