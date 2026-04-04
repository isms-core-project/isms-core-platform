<!-- ISMS-CORE:REF:ISMS-REF-A.8.31-cicd-pipeline-integration-DE:framework:REF:a.8.31 -->
**ISMS-REF-A.8.31 — CI/CD-Pipeline-Integrations-Referenz**
**Technische Referenz für die Implementierung von Deployment-Pipelines**

---

**Dokumentenkontrolle**

| Feld | Wert |
|------|------|
| **Dokumententitel** | CI/CD-Pipeline-Integrations-Referenz |
| **Dokumententyp** | Referenzdokument (Nicht-ISMS-Technische Referenz) |
| **Dokument-ID** | ISMS-REF-A.8.31-CICD |
| **Ersteller** | DevOps Lead / IT Operations Manager |
| **Dokumenteneigentümer** | Informationssicherheitsbeauftragter (ISB) |
| **Genehmigt von** | DevOps Lead (Technische Referenz — keine Geschäftsleitungsgenehmigung erforderlich) |
| **Erstellungsdatum** | [Datum] ||
| **Version** | 1.0 |
| **Versionsdatum** | [Noch festzulegen] |
| **Klassifikation** | Intern |
| **Status** | Entwurf |

**Versionshistorie**:

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | [Datum] | DevOps / IT Operations | Erstveröffentlichung technische Referenz für CI/CD-Pipeline-Integration |

**Überprüfungszyklus**: Bei Bedarf (Technologie- und Tool-Entwicklung)
**Nächstes Überprüfungsdatum**: [Date + 12 months]
**Genehmiger**: DevOps Lead / IT Operations Manager (technische Referenz, keine ISMS-Genehmigung erforderlich)

**Verteiler**: DevOps-Ingenieure, Entwicklungsteams, IT Operations (zur technischen Implementierungssensibilisierung)

---

⚠️ **WICHTIG — NICHT-ISMS-TECHNISCHES SUPPORTDOKUMENT**

Dieses Dokument dient ausschliesslich zu Informations- und Sensibilisierungszwecken.

- Dieses Dokument ist NICHT Bestandteil des Informationssicherheits-Managementsystems (ISMS).
- Dieses Dokument definiert KEINE verbindlichen CI/CD-Pipeline-Kontrollen oder -Anforderungen.
- Dieses Dokument begründet KEINE verbindlichen Anforderungen, Fristen, KPIs oder SLAs.
- Dieses Dokument schreibt die Verwendung, das Verbot oder die Konfiguration spezifischer CI/CD-Plattformen, Tools oder Konfigurationen weder vor noch untersagt es diese.
- Dieses Dokument überschreibt oder erweitert KEINE ISMS-Richtlinie.

Alle verbindlichen Anforderungen an die Umgebungstrennung, Verpflichtungen und Governance-Entscheidungen sind ausschliesslich in **ISMS-POL-A.8.31 (Umgebungstrennungsrichtlinie)** und anderen genehmigten ISMS-Dokumenten festgelegt.

Dieses Dokument dient ausschliesslich als technische Referenz für:

- Beschreibung häufig verwendeter CI/CD-Pipeline-Muster
- Bereitstellung plattformspezifischer Konfigurationsbeispiele
- Unterstützung der Implementierung von Deployment-Automatisierung
- Information über technische Diskussionen und zukünftige Implementierungsplanung
- **Dieses Dokument darf NICHT als Revisions-Nachweis der Implementierung verwendet werden**

Die Verwendung dieses Dokuments impliziert keine Implementierung, Konformität oder operative Reife.

**Kritische Positionierungsaussage**:
Dieses Dokument enthält absichtlich technische Details, die über den Umfang der ISO/IEC-27001-Richtliniendokumentation hinausgehen. Sein Zweck ist ausschliesslich die technische Sensibilisierung. Aus dem Vorhandensein, Fehlen oder der Klassifizierung von Pipeline-Mustern, Plattformen oder Konfigurationen in diesem Dokument dürfen keine Revisionschlüsse gezogen werden.

---

# Dokumentzweck und Geltungsbereich

## Zweck

Dieses Dokument stellt technische Referenzmuster für die Integration von Umgebungstrennungskontrollen in CI/CD-Pipelines bereit. Es dient zur Unterstützung von:

- Technischer Sensibilisierung für Pipeline-Sicherheitsmuster
- Verständnis umgebungsspezifischer Deployment-Workflows
- Kontext für die Auswahl und Konfiguration von CI/CD-Plattformen
- Diskussionen zur künftigen Implementierungsplanung
- Evaluierungskriterien für Tools und Plattformen

## Was dieses Dokument NICHT ist

Dieses Dokument:

- Definiert NICHT die erforderlichen oder verbotenen CI/CD-Plattformen von [Organisation]
- Begründet KEINE verbindlichen Pipeline-Konfigurationen
- Schafft KEINE Compliance-Verpflichtungen oder Revisionskriterien
- Ersetzt NICHT die Richtlinienanforderungen von ISMS-POL-A.8.31
- Schreibt KEINE spezifischen Tools oder Hersteller vor
- Ersetzt NICHT Anbieterdokumentation oder Best Practices

## Beziehung zur ISMS-Richtlinie

**Verbindliche Anforderungen**: ISMS-POL-A.8.31 legt fest, **WAS** an Umgebungsbeförderungskontrollen erforderlich ist (kontrollierter Beförderungspfad, Genehmigungsgates usw.)

**Dieses Dokument**: Erklärt **WIE** diese Anforderungen in CI/CD-Plattformen implementiert werden können (Jenkins, GitLab CI, GitHub Actions usw.)

Organisationen wählen CI/CD-Plattformen und -Konfigurationen entsprechend ihren Anforderungen. Die Anforderung ist kontrollierte Beförderung; die Implementierung variiert.

---

# CI/CD-Pipeline-Architektur für Umgebungstrennung

## Pipeline-Struktur

**Umgebungsbewusste Pipeline-Gestaltung**:

```
┌─────────────────────────────────────────────────────────┐
│              QUELLCODE-REPOSITORY                        │
│             (Git, GitHub, GitLab usw.)                   │
└──────────────────────┬──────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────┐
│         CI/CD-ORCHESTRIERUNGSPLATTFORM                   │
│     (Jenkins, GitLab CI, GitHub Actions usw.)            │
└──────────────────────┬──────────────────────────────────┘
                       │
       ┌───────────────┼───────────────┬─────────────────┐
       │               │               │                 │
       ▼               ▼               ▼                 ▼
  ┌────────┐     ┌────────┐     ┌────────┐     ┌────────┐
  │  DEV   │     │  TEST  │     │STAGING │     │  PROD  │
  │PIPELINE│     │PIPELINE│     │PIPELINE│     │PIPELINE│
  └────┬───┘     └────┬───┘     └────┬───┘     └────┬───┘
       │              │              │              │
       │   AUTOMATISCH│   AUTOMATISCH│    MANUELL   │
       │     ↓        │     ↓        │     ↓        │
       ▼              ▼              ▼              ▼
  ┌────────┐     ┌────────┐     ┌────────┐     ┌────────┐
  │  DEV   │     │  TEST  │     │STAGING │     │  PROD  │
  │  ENV   │     │  ENV   │     │  ENV   │     │  ENV   │
  └────────┘     └────────┘     └────────┘     └────────┘
```

**Schlüsselprinzipien**:

- Separate Pipeline-Jobs/-Phasen pro Umgebung
- Automatische Beförderung von Dev → Test → Staging
- Manuelles Genehmigungsgate vor Produktionsbereitstellung
- Umgebungsvalidierung in jeder Phase
- Zugangsdaten getrennt pro Umgebung

## Deployment-Gates und Genehmigungen

**Genehmigungsanforderungen nach Umgebung**:

| Von → Nach | Genehmigungstyp | Wer genehmigt | Zusätzliche Prüfungen |
|------------|-----------------|---------------|----------------------|
| Dev → Test | Automatisch | Keine (bei erfolgreichem Build) | Unit-Tests bestanden (100%) |
| Test → Staging | Automatisch oder halb-automatisch | QA Lead (optional) | Integrationstests bestanden |
| Staging → Produktion | **MANUELL** | Change Advisory Board (CAB) | Alle Tests bestanden, CAB-Genehmigung, Prüfung des Deployment-Fensters |

**Anforderungen an das Produktions-Deployment-Gate**:

- Explizite manuelle Genehmigung erforderlich
- Genehmigung nur durch autorisiertes Personal (Operations-Team, Change Manager)
- Deployment auf genehmigte Änderungsfenster beschränkt
- Rollback-Plan dokumentiert und zugänglich
- Smoke-Tests für die Validierung nach dem Deployment definiert
- Überwachungs-Dashboards vor der Genehmigung geprüft

## Umgebungsvalidierung

**Vordeployment-Validierungs-Checkliste**:

```yaml
# Pseudo-Code für die Umgebungsvalidierung
validate_environment:

  - check_target_environment_is_correct
  - verify_credentials_match_target_environment
  - confirm_no_production_credentials_in_non_prod
  - validate_network_connectivity_to_target
  - check_resource_availability (CPU, Speicher, Festplatte)
  - verify_deployment_window_is_open (für Produktion)

```

---

# Plattformspezifische Beispiele

## Jenkins-Pipeline

**Jenkinsfile mit Umgebungstrennung**:

```groovy
pipeline {
    agent any

    parameters {
        choice(name: 'ENVIRONMENT',
               choices: ['dev', 'test', 'staging', 'production'],
               description: 'Zielumgebung für Deployment')
    }

    environment {
        APP_NAME = 'webapp'
        ARTIFACT_PATH = "${WORKSPACE}/build/app.jar"
    }

    stages {
        stage('Build') {
            steps {
                echo "Anwendung wird gebaut..."
                sh 'mvn clean package'
            }
        }

        stage('Unit-Tests') {
            steps {
                sh 'mvn test'
                junit 'target/surefire-reports/*.xml'
            }
        }

        stage('Deploy nach Dev') {
            when {
                expression { params.ENVIRONMENT == 'dev' }
            }
            steps {
                deployToEnvironment('dev')
            }
        }

        stage('Integrationstests') {
            when {
                expression { params.ENVIRONMENT in ['test', 'staging', 'production'] }
            }
            steps {
                sh 'mvn verify -Pintegration-tests'
            }
        }

        stage('Deploy nach Test') {
            when {
                expression { params.ENVIRONMENT == 'test' }
            }
            steps {
                deployToEnvironment('test')
            }
        }

        stage('Deploy nach Staging') {
            when {
                expression { params.ENVIRONMENT == 'staging' }
            }
            steps {
                input message: 'Deployment nach Staging genehmigen?',
                      submitter: 'qa-team'
                deployToEnvironment('staging')
            }
        }

        stage('Produktions-Genehmigungsgate') {
            when {
                expression { params.ENVIRONMENT == 'production' }
            }
            steps {
                script {
                    // Prüfen, ob Deployment-Fenster offen ist
                    def currentHour = new Date().getHours()
                    if (currentHour < 9 || currentHour > 17) {
                        error("Produktionsdeployment nur 9–17 Uhr erlaubt")
                    }
                }

                // CAB-Genehmigung erforderlich
                input message: 'CAB-Genehmigung erforderlich für PRODUKTION',
                      submitter: 'change-advisory-board,operations-team',
                      parameters: [
                          string(name: 'CAB_TICKET', description: 'CAB-Genehmigungsticket-Nummer'),
                          text(name: 'ROLLBACK_PLAN', description: 'Rollback-Verfahren beschreiben')
                      ]
            }
        }

        stage('Deploy nach Produktion') {
            when {
                expression { params.ENVIRONMENT == 'production' }
            }
            steps {
                deployToEnvironment('production')

                // Post-Deployment-Smoke-Tests
                sh './scripts/smoke-tests.sh production'
            }
        }

        stage('Post-Deployment-Validierung') {
            steps {
                echo "Post-Deployment-Validierung läuft..."
                sh "./scripts/validate-deployment.sh ${params.ENVIRONMENT}"
            }
        }
    }

    post {
        success {
            echo "Deployment nach ${params.ENVIRONMENT} erfolgreich!"
            // Benachrichtigung via Slack, E-Mail usw.
        }
        failure {
            echo "Deployment nach ${params.ENVIRONMENT} FEHLGESCHLAGEN!"
            // Operations-Team benachrichtigen
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
        echo "Deploying nach ${environment}..."
        sh """
            ./deploy.sh \\
                --environment ${environment} \\
                --artifact ${ARTIFACT_PATH} \\
                --api-key \$API_KEY
        """
    }
}
```

**Schlüsselfunktionen**:

- Umgebungsparameter-Validierung
- Separate Zugangsdaten pro Umgebung (Jenkins Credentials Plugin)
- Produktions-Genehmigungsgate mit CAB-Anforderung
- Durchsetzung des Deployment-Fensters (Produktion nur während Geschäftszeiten)
- Post-Deployment-Smoke-Tests
- Rollback-Plan-Dokumentation erforderlich

## GitLab CI/CD

**.gitlab-ci.yml mit Umgebungstrennung**:

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

  when: manual  # Manuelle Auslösung erforderlich
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
    # Produktions-Deployment mit Validierung

    - echo "Deployment nach PRODUKTION..."
    - gcloud auth activate-service-account --key-file=$GCP_PROD_KEY
    - gcloud app deploy --project=prod-project

    # Post-Deployment-Smoke-Tests

    - ./scripts/smoke-tests.sh production

  when: manual  # MANUELLE Genehmigung erforderlich
  only:

    - main  # Nur von main-Branch

  allow_failure: false  # Deployment-Fehler stoppt Pipeline
  variables:
    ENVIRONMENT: "production"
  rules:

    - if: '$CI_COMMIT_BRANCH == "main"'

      when: manual
      allow_failure: false
```

**Schlüsselfunktionen**:

- Separate Phasen pro Umgebung
- Umgebungsspezifische Service Accounts (GCP_DEV_KEY, GCP_TEST_KEY usw.)
- Manuelle Genehmigung für Staging und Produktion (`when: manual`)
- Branch-Schutz (nur main-Branch kann in Produktion deployen)
- Post-Deployment-Smoke-Tests für Produktion
- Umgebungs-URLs verfolgt (dev.example.com, test.example.com usw.)

**GitLab Protected Environments** (in GitLab-UI konfigurieren):

Einstellungen → CI/CD → Geschützte Umgebungen

- Produktion: Nur Gruppe `operations-team` darf deployen
- Staging: Nur `qa-team` und `operations-team` dürfen deployen

## GitHub Actions

**.github/workflows/deploy.yml mit Umgebungstrennung**:

```yaml
name: In Umgebungen deployen

on:
  push:
    branches:

      - develop  # Löst Dev-Deployment aus
      - main    # Löst Test-/Staging-/Prod-Workflows aus

jobs:
  build:
    runs-on: ubuntu-latest
    steps:

      - uses: actions/checkout@v3

      - name: JDK 17 einrichten

        uses: actions/setup-java@v3
        with:
          java-version: '17'
          distribution: 'temurin'

      - name: Mit Maven bauen

        run: mvn clean package

      - name: Artefakt hochladen

        uses: actions/upload-artifact@v3
        with:
          name: app-jar
          path: target/app.jar

  unit-tests:
    runs-on: ubuntu-latest
    needs: build
    steps:

      - uses: actions/checkout@v3
      - name: Unit-Tests ausführen

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

      - name: Artefakt herunterladen

        uses: actions/download-artifact@v3
        with:
          name: app-jar

      - name: Nach Dev deployen (AWS)

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
      - name: Integrationstests ausführen

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
      - name: Nach Test deployen

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
      - name: Nach Staging deployen

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

      - name: Artefakt herunterladen

        uses: actions/download-artifact@v3
        with:
          name: app-jar

      - name: Nach Produktion deployen

        env:
          AWS_ACCESS_KEY_ID: ${{ secrets.AWS_PROD_ACCESS_KEY }}
          AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_PROD_SECRET_KEY }}
        run: |
          echo "Deploying nach PRODUKTION..."
          aws lambda update-function-code \
            --function-name prod-webapp \
            --s3-bucket prod-deployment-bucket \
            --s3-key app.jar

      - name: Smoke-Tests ausführen

        run: |
          ./scripts/smoke-tests.sh production

      - name: Deployment-Erfolg melden

        run: |
          echo "Produktionsdeployment erfolgreich!"
          # Slack-Benachrichtigung, PagerDuty-Ereignis usw. senden
```

**GitHub Environment Protection Rules** (in GitHub-UI konfigurieren):

Repository → Einstellungen → Environments

**Produktionsumgebung**:

- Erforderliche Reviewer: `operations-team` (mindestens 2 Genehmigungen)
- Deployment-Branches: Nur `main`-Branch
- Wartezeit: 5 Minuten (Abkühlungsphase)
- Umgebungsgeheimnisse: `AWS_PROD_ACCESS_KEY`, `AWS_PROD_SECRET_KEY`

**Staging-Umgebung**:

- Erforderliche Reviewer: `qa-team` (mindestens 1 Genehmigung)
- Deployment-Branches: Nur `main`-Branch

## Azure DevOps Pipelines

**azure-pipelines.yml mit Umgebungstrennung**:

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

    environment: 'Production'  # Erfordert manuelle Genehmigung in Azure DevOps
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
            displayName: 'Produktions-Smoke-Tests ausführen'
```

**Azure DevOps Environment Approvals** (in Azure DevOps UI konfigurieren):

Pipelines → Environments → Production

**Genehmigungen und Prüfungen**:

- Erforderliche Genehmiger: `Operations Team` hinzufügen, mindestens 2 Genehmigungen
- Timeout: 30 Tage (Pipeline wartet auf Genehmigung)
- Geschäftszeiten-Gate: Deployments nur 9–17 Uhr erlauben
- Branch-Steuerung: Nur `main`-Branch

---

# Infrastructure as Code (IaC) Integration

## Terraform-Umgebungsmuster

**Verzeichnisstruktur**:

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

**Umgebungsspezifische Konfiguration (terraform.tfvars)**:

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

**Pipeline-Integration (GitLab CI)**:

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

## Ansible-Umgebungsvariablen

**Inventar-Struktur**:

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

**Umgebungsspezifische Variablen**:

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
app_version: "1.5.2"  # Spezifische Version
database_host: prod-db.internal
enable_debug_mode: false
```

**Pipeline-Integration**:

```bash
# Nach Dev deployen
ansible-playbook -i inventories/dev playbooks/deploy.yml

# Nach Produktion deployen (manuell)
ansible-playbook -i inventories/prod playbooks/deploy.yml
```

---

# Sicherheitskontrollen in Pipelines

## Trennung von Service Accounts

**Best Practice**: Separate Service Accounts/Zugangsdaten pro Umgebung

**AWS-Beispiel**:

- Dev-Pipeline: Verwendet IAM-Rolle `dev-deployment-role`
- Test-Pipeline: Verwendet IAM-Rolle `test-deployment-role`
- Produktions-Pipeline: Verwendet IAM-Rolle `prod-deployment-role`

**Azure-Beispiel**:

- Dev-Pipeline: Verwendet Service Principal `dev-sp`
- Produktions-Pipeline: Verwendet Service Principal `prod-sp`

**Begründung**: Bei Kompromittierung der Dev-Pipeline kann ein Angreifer nicht in Produktion deployen.

## Geheimnismanagement nach Umgebung

**HashiCorp-Vault-Integration**:

```groovy
// Jenkins-Pipeline mit Vault
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

**Vault-Pfade nach Umgebung**:

- `dev/database/password`
- `test/database/password`
- `prod/database/password`

## Deployment-Überwachung und -Alarmierung

**Post-Deployment-Validierung**:

```bash
#!/bin/bash
# smoke-tests.sh

ENVIRONMENT=$1
APP_URL="https://${ENVIRONMENT}.example.com"

# Gesundheitsprüfung
if curl -f "${APP_URL}/health" > /dev/null 2>&1; then
    echo "✅ Gesundheitsprüfung bestanden"
else
    echo "❌ Gesundheitsprüfung FEHLGESCHLAGEN"
    exit 1
fi

# Datenbankkonnektivität
if curl -f "${APP_URL}/db-check" > /dev/null 2>&1; then
    echo "✅ Datenbankkonnektivität OK"
else
    echo "❌ Datenbankkonnektivität FEHLGESCHLAGEN"
    exit 1
fi

# Performance-Prüfung (Antwortzeit < 2 Sekunden)
RESPONSE_TIME=$(curl -o /dev/null -s -w '%{time_total}' "${APP_URL}")
if (( $(echo "$RESPONSE_TIME < 2.0" | bc -l) )); then
    echo "✅ Antwortzeit OK (${RESPONSE_TIME}s)"
else
    echo "❌ Antwortzeit zu langsam (${RESPONSE_TIME}s)"
    exit 1
fi

echo "Alle Smoke-Tests bestanden!"
```

---

# Häufige Fehler und Best Practices

## Was NICHT zu tun ist

❌ **Gemeinsame Zugangsdaten über Umgebungen hinweg**:

- Produktion und Dev nutzen dieselbe AWS-IAM-Rolle → Sicherheitsrisiko

❌ **Kein Genehmigungsgate für Produktion**:

- Automatisches Deployment in Produktion → Ungetestete Änderungen erreichen Kunden

❌ **Produktionsgeheimnisse im Code**:

- `DATABASE_PASSWORD=prod_geheimnis_123` hartcodiert in Pipeline → In Logs exponiert

❌ **Direktes Produktions-Deployment**:

- Pipeline umgeht Staging → Keine Validierung vor Produktion

❌ **Kein Rollback-Plan**:

- Deployment schlägt fehl → Kein dokumentiertes Wiederherstellungsverfahren

## Best Practices

✅ Separate Zugangsdaten pro Umgebung
✅ Manuelles Genehmigungsgate für Produktion
✅ Geheimnisse in Vault gespeichert (HashiCorp Vault, AWS Secrets Manager)
✅ Verbindlicher Beförderungspfad (Dev → Test → Staging → Prod)
✅ Automatischer Rollback bei Fehler
✅ Post-Deployment-Smoke-Tests
✅ Deployment-Überwachung (Datadog, New Relic)
✅ Audit-Protokollierung (wer was wann deployt hat)
✅ Branch-Schutz (nur main-Branch → Produktion)
✅ Durchsetzung des Änderungsfensters (Produktion nur während genehmigter Zeiten)

---

**ENDE DES REFERENZDOKUMENTS**

---

*Dieses technische Referenzdokument unterstützt ISMS-POL-A.8.31. CI/CD-Pipeline-Konfigurationen sollten vom DevOps Lead und vom ISB überprüft und genehmigt werden.*

**DIESES DOKUMENT IST NICHT BESTANDTEIL DES ISMS.**

<!-- QA_VERIFIED: 2026-03-29 -->
