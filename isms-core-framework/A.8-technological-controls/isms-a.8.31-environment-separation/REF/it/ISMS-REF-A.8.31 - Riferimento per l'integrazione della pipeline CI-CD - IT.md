<!-- ISMS-CORE:REF:ISMS-REF-A.8.31-IT-cicd-pipeline-integration:framework:REF:a.8.31 -->
**ISMS-REF-A.8.31 — Riferimento per l'integrazione della pipeline CI/CD**
**Riferimento tecnico per l'implementazione della pipeline di distribuzione**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Riferimento per l'integrazione della pipeline CI/CD |
| **Tipo di documento** | Documento di riferimento (Riferimento tecnico non-SGSI) |
| **Identificativo del documento** | ISMS-REF-A.8.31-CICD |
| **Autore del documento** | Responsabile DevOps / Responsabile delle operazioni IT |
| **Proprietario del documento** | Responsabile della Sicurezza dei Sistemi Informativi (RSSI) |
| **Approvato da** | Responsabile DevOps (Riferimento tecnico — nessuna approvazione esecutiva richiesta) |
| **Data di creazione** | [Data] |
| **Versione** | 1.0 |
| **Data di versione** | [Da definire] |
| **Classificazione** | Interno |
| **Stato** | Bozza |

**Cronologia delle versioni**:

| Versione | Data | Autore | Modifiche |
|----------|------|--------|-----------|
| 1.0 | [Data] | DevOps / Operazioni IT | Riferimento tecnico iniziale per l'integrazione della pipeline CI/CD |

**Ciclo di revisione**: In base alle esigenze (evoluzione della tecnologia e degli strumenti)  
**Prossima data di revisione**: [Data + 12 mesi]

**Distribuzione**: Ingegneri DevOps, team di sviluppo, operazioni IT (per la consapevolezza tecnica dell'implementazione)

---

⚠️ **IMPORTANTE — DOCUMENTO DI SUPPORTO TECNICO NON-SGSI**

Questo documento è fornito esclusivamente a scopo informativo e di sensibilizzazione.

- Questo documento NON fa parte del Sistema di Gestione della Sicurezza delle Informazioni (SGSI).
- Questo documento NON definisce controlli o requisiti obbligatori per la pipeline CI/CD.
- Questo documento NON stabilisce requisiti vincolanti, scadenze, ICP o SLA.
- Questo documento NON impone l'uso, il divieto o la configurazione di piattaforme, strumenti o configurazioni CI/CD specifici.
- Questo documento NON sostituisce né estende alcuna politica SGSI.

Tutti i requisiti di separazione degli ambienti vincolanti, gli obblighi e le decisioni di governance sono definiti esclusivamente in **ISMS-POL-A.8.31 (Politica di separazione degli ambienti)** e in altri documenti SGSI approvati.

---

# Scopo e ambito del documento

## Scopo

Questo documento fornisce pattern di riferimento tecnici per integrare i controlli di separazione degli ambienti nelle pipeline CI/CD. È inteso a supportare:

- La consapevolezza tecnica dei pattern di sicurezza delle pipeline
- La comprensione dei flussi di lavoro di distribuzione specifici per l'ambiente
- Il contesto per la selezione e la configurazione delle piattaforme CI/CD
- La pianificazione futura delle discussioni di implementazione

## Relazione con la politica SGSI

**Requisiti vincolanti**: ISMS-POL-A.8.31 definisce **COSA** è richiesto come controlli di promozione degli ambienti (percorso di promozione controllato, porte di approvazione, ecc.)

**Questo documento**: Fornisce **COME** questi requisiti possono essere implementati nelle piattaforme CI/CD (Jenkins, GitLab CI, GitHub Actions, ecc.)

---

# Architettura della pipeline CI/CD per la separazione degli ambienti

## Struttura della pipeline

**Progettazione della pipeline con consapevolezza dell'ambiente**:

```
┌─────────────────────────────────────────────────────────┐
│           REPOSITORY DEL CODICE SORGENTE                 │
│             (Git, GitHub, GitLab, ecc.)                  │
└──────────────────────┬──────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────┐
│       PIATTAFORMA DI ORCHESTRAZIONE CI/CD                │
│     (Jenkins, GitLab CI, GitHub Actions, ecc.)           │
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
       │     AUTO     │     AUTO     │   MANUALE    │
       ▼              ▼              ▼              ▼
  ┌────────┐     ┌────────┐     ┌────────┐     ┌────────┐
  │  ENV   │     │  ENV   │     │  ENV   │     │  ENV   │
  │  DEV   │     │  TEST  │     │STAGING │     │  PROD  │
  └────────┘     └────────┘     └────────┘     └────────┘
```

**Principi chiave**:

- Job/fasi della pipeline separati per ambiente
- Promozione automatizzata da dev → test → staging
- Porta di approvazione manuale prima della distribuzione in produzione
- Validazione dell'ambiente in ogni fase
- Credenziali separate per ambiente

## Porte di distribuzione e approvazioni

**Requisiti di approvazione per ambiente**:

| Da → A | Tipo di approvazione | Chi approva | Verifiche aggiuntive |
|--------|---------------------|-------------|----------------------|
| Dev → Test | Automatica | Nessuno (su build riuscito) | Test unitari superati (100%) |
| Test → Staging | Automatica o semi-automatica | Responsabile QA (opzionale) | Test di integrazione superati |
| Staging → Produzione | **MANUALE** | Comitato consultivo per i cambiamenti (CAB) | Tutti i test superati, approvazione CAB, verifica della finestra di distribuzione |

**Requisiti della porta di distribuzione in produzione**:

- Approvazione manuale esplicita richiesta
- Approvazione solo da parte del personale autorizzato (team operativo, responsabile dei cambiamenti)
- Distribuzione limitata alle finestre di cambiamento approvate
- Piano di rollback documentato e accessibile
- Test di fumo definiti per la validazione post-distribuzione
- Dashboard di monitoraggio esaminati prima dell'approvazione

---

# Esempi specifici per piattaforma

## Pipeline Jenkins

**Jenkinsfile con separazione degli ambienti**:

```groovy
pipeline {
    agent any
    
    parameters {
        choice(name: 'ENVIRONMENT', 
               choices: ['dev', 'test', 'staging', 'production'], 
               description: 'Ambiente di destinazione per la distribuzione')
    }
    
    environment {
        APP_NAME = 'webapp'
        ARTIFACT_PATH = "${WORKSPACE}/build/app.jar"
    }
    
    stages {
        stage('Build') {
            steps {
                echo "Costruzione dell'applicazione..."
                sh 'mvn clean package'
            }
        }
        
        stage('Test unitari') {
            steps {
                sh 'mvn test'
                junit 'target/surefire-reports/*.xml'
            }
        }
        
        stage('Distribuire in Dev') {
            when {
                expression { params.ENVIRONMENT == 'dev' }
            }
            steps {
                deployToEnvironment('dev')
            }
        }
        
        stage('Test di integrazione') {
            when {
                expression { params.ENVIRONMENT in ['test', 'staging', 'production'] }
            }
            steps {
                sh 'mvn verify -Pintegration-tests'
            }
        }
        
        stage('Distribuire in Test') {
            when {
                expression { params.ENVIRONMENT == 'test' }
            }
            steps {
                deployToEnvironment('test')
            }
        }
        
        stage('Distribuire in Staging') {
            when {
                expression { params.ENVIRONMENT == 'staging' }
            }
            steps {
                input message: 'Approvare la distribuzione in Staging?', 
                      submitter: 'qa-team'
                deployToEnvironment('staging')
            }
        }
        
        stage('Porta di approvazione Produzione') {
            when {
                expression { params.ENVIRONMENT == 'production' }
            }
            steps {
                script {
                    // Verificare se la finestra di distribuzione è aperta
                    def currentHour = new Date().getHours()
                    if (currentHour < 9 || currentHour > 17) {
                        error("Distribuzione in produzione consentita solo dalle 9:00 alle 17:00")
                    }
                }
                
                // Approvazione CAB richiesta
                input message: 'Approvazione CAB richiesta per la PRODUZIONE', 
                      submitter: 'change-advisory-board,operations-team',
                      parameters: [
                          string(name: 'CAB_TICKET', description: 'Numero del ticket di approvazione CAB'),
                          text(name: 'ROLLBACK_PLAN', description: 'Descrivere la procedura di rollback')
                      ]
            }
        }
        
        stage('Distribuire in Produzione') {
            when {
                expression { params.ENVIRONMENT == 'production' }
            }
            steps {
                deployToEnvironment('production')
                sh './scripts/smoke-tests.sh production'
            }
        }
        
        stage('Validazione post-distribuzione') {
            steps {
                echo "Esecuzione della validazione post-distribuzione..."
                sh "./scripts/validate-deployment.sh ${params.ENVIRONMENT}"
            }
        }
    }
    
    post {
        success {
            echo "Distribuzione in ${params.ENVIRONMENT} riuscita!"
        }
        failure {
            echo "Distribuzione in ${params.ENVIRONMENT} FALLITA!"
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
        echo "Distribuzione in ${environment}..."
        sh """
            ./deploy.sh \\
                --environment ${environment} \\
                --artifact ${ARTIFACT_PATH} \\
                --api-key \$API_KEY
        """
    }
}
```

**Funzionalità chiave**:

- Validazione del parametro dell'ambiente
- Credenziali separate per ambiente (Plugin Jenkins Credentials)
- Porta di approvazione della produzione con requisito CAB
- Applicazione delle finestre di distribuzione (produzione solo durante l'orario lavorativo)
- Test di fumo post-distribuzione
- Documentazione del piano di rollback richiesta

## GitLab CI/CD

**.gitlab-ci.yml con separazione degli ambienti**:

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
  script:
    - mvn test

deploy-dev:
  stage: deploy-dev
  environment:
    name: development
    url: https://dev.example.com
  script:
    - gcloud auth activate-service-account --key-file=$GCP_DEV_KEY
    - gcloud app deploy --project=dev-project
  only:
    - develop

deploy-staging:
  stage: deploy-staging
  environment:
    name: staging
    url: https://staging.example.com
  script:
    - gcloud auth activate-service-account --key-file=$GCP_STAGING_KEY
    - gcloud app deploy --project=staging-project
  when: manual
  only:
    - main

deploy-production:
  stage: deploy-production
  environment:
    name: production
    url: https://example.com
  script:
    - gcloud auth activate-service-account --key-file=$GCP_PROD_KEY
    - gcloud app deploy --project=prod-project
    - ./scripts/smoke-tests.sh production
  when: manual
  only:
    - main
  allow_failure: false
```

**Funzionalità chiave**:

- Fasi separate per ambiente
- Account di servizio specifici per l'ambiente (GCP_DEV_KEY, GCP_STAGING_KEY, ecc.)
- Approvazione manuale per staging e produzione (`when: manual`)
- Protezione dei branch (solo il branch main può distribuire in produzione)
- Test di fumo post-distribuzione in produzione

**Ambienti protetti GitLab**:

Configurare nell'interfaccia GitLab:

- Impostazioni → CI/CD → Ambienti protetti
- Produzione: Solo il gruppo `operations-team` può distribuire
- Staging: Solo `qa-team` e `operations-team` possono distribuire

## GitHub Actions

**.github/workflows/deploy.yml con separazione degli ambienti**:

```yaml
name: Distribuire negli ambienti

on:
  push:
    branches:
      - develop
      - main

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Costruire con Maven
        run: mvn clean package
      - name: Caricare l'artefatto
        uses: actions/upload-artifact@v3
        with:
          name: app-jar
          path: target/app.jar

  deploy-dev:
    runs-on: ubuntu-latest
    needs: [build]
    if: github.ref == 'refs/heads/develop'
    environment:
      name: development
      url: https://dev.example.com
    steps:
      - uses: actions/checkout@v3
      - name: Distribuire in Dev (AWS)
        env:
          AWS_ACCESS_KEY_ID: ${{ secrets.AWS_DEV_ACCESS_KEY }}
          AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_DEV_SECRET_KEY }}
        run: |
          aws lambda update-function-code \
            --function-name dev-webapp \
            --s3-bucket dev-deployment-bucket \
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
      - name: Distribuire in Staging
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
      - name: Distribuire in Produzione
        env:
          AWS_ACCESS_KEY_ID: ${{ secrets.AWS_PROD_ACCESS_KEY }}
          AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_PROD_SECRET_KEY }}
        run: |
          aws lambda update-function-code \
            --function-name prod-webapp \
            --s3-bucket prod-deployment-bucket \
            --s3-key app.jar
      - name: Eseguire test di fumo
        run: ./scripts/smoke-tests.sh production
```

**Regole di protezione degli ambienti GitHub** (configurare nell'interfaccia GitHub):

**Ambiente Produzione**:

- Revisori richiesti: gruppo `operations-team` (almeno 2 approvazioni)
- Branch di distribuzione: solo il branch `main`
- Timer di attesa: 5 minuti (periodo di raffreddamento)
- Segreti dell'ambiente: `AWS_PROD_ACCESS_KEY`, `AWS_PROD_SECRET_KEY`

**Ambiente Staging**:

- Revisori richiesti: gruppo `qa-team` (almeno 1 approvazione)
- Branch di distribuzione: solo il branch `main`

## Azure DevOps Pipelines

**azure-pipelines.yml con separazione degli ambienti**:

```yaml
trigger:
  branches:
    include:
      - develop
      - main

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

- stage: DeployProduction
  dependsOn: DeployStaging
  condition: eq(variables['Build.SourceBranch'], 'refs/heads/main')
  jobs:
  - deployment: DeployProductionJob
    environment: 'Production'  # Richiede approvazione manuale in Azure DevOps
    strategy:
      runOnce:
        deploy:
          steps:
          - task: AzureWebApp@1
            inputs:
              azureSubscription: 'Azure-Prod-ServiceConnection'
              appName: 'webapp-prod'
          - script: ./scripts/smoke-tests.sh production
            displayName: 'Eseguire test di fumo della produzione'
```

**Approvazioni ed ispezioni dell'ambiente Azure DevOps** (configurare nell'interfaccia):

- Approvatori richiesti: Team Operations, minimo 2 approvazioni
- Timeout: 30 giorni
- Porta dell'orario lavorativo: Consentire le distribuzioni solo dalle 9:00 alle 17:00
- Controllo del branch: Solo il branch `main`

---

# Infrastructure as Code (IaC) — Integrazione

## Pattern Terraform per ambiente

**Struttura delle directory**:

```
terraform/
├── environments/
│   ├── dev/terraform.tfvars
│   ├── test/terraform.tfvars
│   ├── staging/terraform.tfvars
│   └── prod/terraform.tfvars
└── modules/webapp/
```

**Configurazione specifica per l'ambiente**:

**dev/terraform.tfvars**:
```hcl
environment = "dev"
instance_type = "t3.small"
enable_deletion_protection = false
backup_retention_days = 7
```

**prod/terraform.tfvars**:
```hcl
environment = "prod"
instance_type = "t3.large"
enable_deletion_protection = true
backup_retention_days = 30
```

**Integrazione pipeline**:

```yaml
terraform-prod:
  stage: deploy-production
  image: hashicorp/terraform:latest
  script:
    - cd terraform/environments/prod
    - terraform init
    - terraform plan -out=tfplan
    - terraform apply tfplan
  when: manual
  only:
    - main
```

---

# Controlli di sicurezza nelle pipeline

## Separazione degli account di servizio

**Migliore pratica**: Account di servizio/credenziali separati per ambiente

**Esempio AWS**:

- Pipeline Dev: Utilizza il ruolo IAM `dev-deployment-role`
- Pipeline Test: Utilizza il ruolo IAM `test-deployment-role`
- Pipeline Produzione: Utilizza il ruolo IAM `prod-deployment-role`

**Perché**: Se la pipeline dev viene compromessa, l'attaccante non può distribuire in produzione.

## Gestione dei segreti per ambiente

**Integrazione HashiCorp Vault**:

```groovy
def secrets = [
    [path: "${ENVIRONMENT}/database", 
     secretValues: [
         [envVar: 'DB_PASSWORD', vaultKey: 'password']
     ]]
]

withVault([vaultSecrets: secrets]) {
    sh "./deploy.sh --db-password ${DB_PASSWORD}"
}
```

**Percorsi Vault per ambiente**:

- `dev/database/password`
- `test/database/password`
- `prod/database/password`

## Monitoraggio e avvisi post-distribuzione

**Script di validazione post-distribuzione**:

```bash
#!/bin/bash
ENVIRONMENT=$1
APP_URL="https://${ENVIRONMENT}.example.com"

# Verifica dello stato di salute
if curl -f "${APP_URL}/health" > /dev/null 2>&1; then
    echo "✅ Verifica dello stato di salute superata"
else
    echo "❌ Verifica dello stato di salute FALLITA"
    exit 1
fi

# Verifica della connettività al database
if curl -f "${APP_URL}/db-check" > /dev/null 2>&1; then
    echo "✅ Connettività al database OK"
else
    echo "❌ Connettività al database FALLITA"
    exit 1
fi

# Verifica delle prestazioni (tempo di risposta < 2 secondi)
RESPONSE_TIME=$(curl -o /dev/null -s -w '%{time_total}' "${APP_URL}")
if (( $(echo "$RESPONSE_TIME < 2.0" | bc -l) )); then
    echo "✅ Tempo di risposta OK (${RESPONSE_TIME}s)"
else
    echo "❌ Tempo di risposta troppo lento (${RESPONSE_TIME}s)"
    exit 1
fi

echo "Tutti i test di fumo superati!"
```

---

# Errori comuni e migliori pratiche

## Cosa NON fare

❌ **Credenziali condivise tra ambienti**: Produzione e dev che utilizzano lo stesso ruolo IAM AWS → Rischio di sicurezza

❌ **Nessuna porta di approvazione per la produzione**: Distribuzione automatica in produzione → Modifiche non testate raggiungono i clienti

❌ **Segreti di produzione nel codice**: `DATABASE_PASSWORD=prod_secret_123` hardcoded nella pipeline → Esposto nei log

❌ **Distribuzione diretta in produzione**: La pipeline bypassa lo staging → Nessuna validazione prima della produzione

❌ **Nessun piano di rollback**: La distribuzione fallisce → Nessuna procedura di recupero documentata

## Migliori pratiche

✅ Credenziali separate per ambiente  
✅ Porta di approvazione manuale per la produzione  
✅ Segreti archiviati nel vault (HashiCorp Vault, AWS Secrets Manager)  
✅ Percorso di promozione obbligatorio (dev → test → staging → prod)  
✅ Rollback automatizzato in caso di errore  
✅ Test di fumo post-distribuzione  
✅ Monitoraggio delle distribuzioni (Datadog, New Relic)  
✅ Registrazione di audit (chi ha distribuito cosa, quando)  
✅ Protezione dei branch (solo il branch main → produzione)  
✅ Applicazione delle finestre di cambiamento (produzione solo durante le ore approvate)

---

**FINE DEL DOCUMENTO DI RIFERIMENTO**

---

*Questo riferimento tecnico supporta ISMS-POL-A.8.31. Le configurazioni della pipeline CI/CD devono essere esaminate e approvate dal Responsabile DevOps e dal RSSI.*
<!-- QA_VERIFIED: 2026-04-04 -->
