<!-- ISMS-CORE:REF:ISMS-REF-A.8.31-IT-cicd-pipeline-integration:framework:REF:a.8.31 -->
**ISMS-REF-A.8.31 — Riferimento per l'integrazione CI/CD**
**Riferimento tecnico per l'implementazione del pipeline di distribuzione**

---

**Controllo del documento**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Riferimento per l'integrazione CI/CD |
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
| 1.0 | [Data] | DevOps / Operazioni IT | Riferimento tecnico iniziale per l'integrazione dei pipeline CI/CD |

**Ciclo di revisione**: In base alle esigenze (evoluzione delle tecnologie e degli strumenti)  
**Prossima data di revisione**: [Data + 12 mesi]

**Distribuzione**: Ingegneri DevOps, Team di sviluppo, Operazioni IT

---

⚠️ **IMPORTANTE — DOCUMENTO DI SUPPORTO TECNICO NON-SGSI**

Questo documento è fornito esclusivamente a scopo informativo e di sensibilizzazione. NON fa parte del SGSI, NON stabilisce requisiti vincolanti e NON sostituisce ISMS-POL-A.8.31.

---

# Scopo e ambito del documento

## Scopo

Questo documento fornisce modelli di riferimento tecnico per l'integrazione dei controlli di separazione degli ambienti nei pipeline CI/CD. È inteso a supportare:

- La consapevolezza tecnica dei modelli di sicurezza dei pipeline
- La comprensione dei flussi di distribuzione specifici per ambiente
- La selezione e configurazione delle piattaforme CI/CD
- La pianificazione futura dell'implementazione

## Relazione con la politica SGSI

**Requisiti vincolanti**: ISMS-POL-A.8.31 definisce COSA è richiesto (percorso di promozione controllato, porte di approvazione, ecc.)

**Questo documento**: Fornisce COME tali requisiti possono essere implementati sulle piattaforme CI/CD (Jenkins, GitLab CI, GitHub Actions, ecc.)

---

# Architettura del pipeline CI/CD per la separazione degli ambienti

## Struttura del pipeline

**Progettazione del pipeline adattata agli ambienti**:

```
┌─────────────────────────────────────────────────────────┐
│              REPOSITORY DEL CODICE SORGENTE              │
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
       │    AUTO      │    AUTO      │  MANUALE      │
       ▼              ▼              ▼              ▼
  ┌────────┐     ┌────────┐     ┌────────┐     ┌────────┐
  │  AMB   │     │  AMB   │     │  AMB   │     │  AMB   │
  │  DEV   │     │  TEST  │     │STAGING │     │  PROD  │
  └────────┘     └────────┘     └────────┘     └────────┘
```

**Principi chiave**:

- Job/fasi del pipeline separati per ambiente
- Promozione automatizzata da dev → test → staging
- Porta di approvazione manuale prima della distribuzione in produzione
- Validazione dell'ambiente in ogni fase
- Credenziali separate per ambiente

## Porte e approvazioni di distribuzione

**Requisiti di approvazione per ambiente**:

| Da → A | Tipo di approvazione | Chi approva | Controlli aggiuntivi |
|--------|---------------------|-------------|----------------------|
| Dev → Test | Automatico | Nessuno (dopo build riuscita) | Test unitari superati (100%) |
| Test → Staging | Automatico o semi-auto | Responsabile QA (opzionale) | Test di integrazione superati |
| Staging → Produzione | **MANUALE** | Comitato consultivo per le modifiche (CAB) | Tutti i test superati, approvazione CAB, verifica finestra di distribuzione |

**Requisiti della porta di distribuzione in produzione**:

- Approvazione manuale esplicita richiesta
- Approvazione del solo personale autorizzato (team delle operazioni, gestore delle modifiche)
- Distribuzione limitata alle finestre di modifica approvate
- Piano di rollback documentato e accessibile
- Test di fumo definiti per la validazione post-distribuzione
- Dashboard di monitoraggio verificati prima dell'approvazione

## Validazione dell'ambiente

**Lista di controllo di validazione pre-distribuzione**:

```yaml
# Pseudo-codice per la validazione dell'ambiente
valida_ambiente:
  - verifica_che_lambiente_di_destinazione_sia_corretto
  - conferma_che_le_credenziali_corrispondano_allambiente_di_destinazione
  - conferma_nessuna_credenziale_prod_in_non_prod
  - valida_connettivita_di_rete_verso_destinazione
  - verifica_disponibilita_risorse (CPU, memoria, disco)
  - verifica_che_la_finestra_di_distribuzione_sia_aperta (per produzione)
```

---

# Esempi specifici per piattaforma

## Jenkins Pipeline

**Jenkinsfile con separazione degli ambienti**:

```groovy
pipeline {
    agent any
    
    parameters {
        choice(name: 'AMBIENTE',
               choices: ['dev', 'test', 'staging', 'production'],
               description: 'Ambiente di destinazione per la distribuzione')
    }
    
    stages {
        stage('Build') {
            steps { sh 'mvn clean package' }
        }
        
        stage('Test unitari') {
            steps {
                sh 'mvn test'
                junit 'target/surefire-reports/*.xml'
            }
        }
        
        stage('Distribuire in Dev') {
            when { expression { params.AMBIENTE == 'dev' } }
            steps { distribuireVersAmbiente('dev') }
        }
        
        stage('Test di integrazione') {
            when {
                expression { params.AMBIENTE in ['test', 'staging', 'production'] }
            }
            steps { sh 'mvn verify -Pintegration-tests' }
        }
        
        stage('Distribuire in Test') {
            when { expression { params.AMBIENTE == 'test' } }
            steps { distribuireVersAmbiente('test') }
        }
        
        stage('Distribuire in Staging') {
            when { expression { params.AMBIENTE == 'staging' } }
            steps {
                input message: 'Approvare la distribuzione in Staging?',
                      submitter: 'qa-team'
                distribuireVersAmbiente('staging')
            }
        }
        
        stage('Porta di approvazione produzione') {
            when { expression { params.AMBIENTE == 'production' } }
            steps {
                script {
                    def oraCorrente = new Date().getHours()
                    if (oraCorrente < 9 || oraCorrente > 17) {
                        error("Distribuzione produzione consentita solo dalle 9:00 alle 17:00")
                    }
                }
                input message: 'Approvazione CAB richiesta per la PRODUZIONE',
                      submitter: 'change-advisory-board,operations-team',
                      parameters: [
                          string(name: 'TICKET_CAB', description: 'Numero ticket di approvazione CAB'),
                          text(name: 'PIANO_ROLLBACK', description: 'Descrivere la procedura di rollback')
                      ]
            }
        }
        
        stage('Distribuire in Produzione') {
            when { expression { params.AMBIENTE == 'production' } }
            steps {
                distribuireVersAmbiente('production')
                sh './scripts/smoke-tests.sh production'
            }
        }
    }
    
    post {
        success { echo "Distribuzione in ${params.AMBIENTE} riuscita!" }
        failure { echo "Distribuzione in ${params.AMBIENTE} FALLITA!" }
    }
}

def distribuireVersAmbiente(ambiente) {
    withCredentials([
        string(credentialsId: "${ambiente}-api-key", variable: 'API_KEY'),
        usernamePassword(credentialsId: "${ambiente}-db-creds",
                         usernameVariable: 'DB_USER',
                         passwordVariable: 'DB_PASS')
    ]) {
        sh """
            ./deploy.sh \\
                --environment ${ambiente} \\
                --artifact ${ARTIFACT_PATH} \\
                --api-key \$API_KEY
        """
    }
}
```

**Caratteristiche chiave**:

- Credenziali separate per ambiente (Jenkins Credentials Plugin)
- Porta di approvazione produzione con requisito CAB
- Applicazione della finestra di distribuzione (produzione solo durante l'orario lavorativo)
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

build:
  stage: build
  image: maven:3.8-openjdk-17
  script:
    - mvn clean package
  artifacts:
    paths:
      - target/app.jar
    expire_in: 1 week

test-unitari:
  stage: test
  script:
    - mvn test
  artifacts:
    reports:
      junit: target/surefire-reports/TEST-*.xml

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

deploy-test:
  stage: deploy-test
  environment:
    name: testing
    url: https://test.example.com
  script:
    - gcloud auth activate-service-account --key-file=$GCP_TEST_KEY
    - gcloud app deploy --project=test-project
  only:
    - main

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

**Caratteristiche chiave**:

- Account di servizio distinti per ambiente (GCP_DEV_KEY, GCP_TEST_KEY, ecc.)
- Approvazione manuale per staging e produzione (`when: manual`)
- Protezione del branch (solo il branch main può distribuire in produzione)
- Test di fumo post-distribuzione per la produzione

**Ambienti protetti GitLab** (configurare nell'interfaccia GitLab):

Impostazioni → CI/CD → Ambienti protetti

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
      - name: Configurare JDK 17
        uses: actions/setup-java@v3
        with:
          java-version: '17'
          distribution: 'temurin'
      - name: Build con Maven
        run: mvn clean package
      - name: Caricare artefatto
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
      - name: Distribuire in Dev (AWS)
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

  deploy-staging:
    runs-on: ubuntu-latest
    needs: deploy-test
    if: github.ref == 'refs/heads/main'
    environment:
      name: staging
      url: https://staging.example.com
    steps:
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
      - name: Distribuire in Produzione
        env:
          AWS_ACCESS_KEY_ID: ${{ secrets.AWS_PROD_ACCESS_KEY }}
          AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_PROD_SECRET_KEY }}
        run: |
          aws lambda update-function-code \
            --function-name prod-webapp \
            --s3-bucket prod-deployment-bucket \
            --s3-key app.jar
      - name: Test di fumo
        run: ./scripts/smoke-tests.sh production
```

**Regole di protezione degli ambienti GitHub** (configurare in GitHub):

Repository → Impostazioni → Ambienti

**Ambiente Produzione**:

- Revisori richiesti: gruppo `operations-team` (almeno 2 approvazioni)
- Branch di distribuzione: Solo branch `main`
- Timer di attesa: 5 minuti (periodo di raffreddamento)
- Segreti dell'ambiente: `AWS_PROD_ACCESS_KEY`, `AWS_PROD_SECRET_KEY`

**Ambiente Staging**:

- Revisori richiesti: gruppo `qa-team` (almeno 1 approvazione)
- Branch di distribuzione: Solo branch `main`

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
    - task: PublishBuildArtifacts@1
      inputs:
        PathtoPublish: 'target/app.jar'
        ArtifactName: 'app'

- stage: DistribuireInDev
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

- stage: DistribuireInStaging
  dependsOn: DistribuireInTest
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

- stage: DistribuireInProduzione
  dependsOn: DistribuireInStaging
  condition: eq(variables['Build.SourceBranch'], 'refs/heads/main')
  jobs:
  - deployment: DeployProductionJob
    environment: 'Production'
    strategy:
      runOnce:
        deploy:
          steps:
          - task: AzureWebApp@1
            inputs:
              azureSubscription: 'Azure-Prod-ServiceConnection'
              appName: 'webapp-prod'
          - script: ./scripts/smoke-tests.sh production
            displayName: 'Test di fumo produzione'
```

**Approvazioni e verifiche Azure DevOps** (configurare in Azure DevOps):

Pipeline → Ambienti → Produzione

- Approvatori richiesti: `Operations Team`, minimo 2 approvazioni
- Timeout: 30 giorni
- Porte per le ore lavorative: Distribuzioni consentite solo dalle 9:00 alle 17:00
- Controllo del branch: Solo branch `main`

---

# Integrazione dell'Infrastructure as Code (IaC)

## Modelli Terraform per ambiente

**Struttura della directory**:

```
terraform/
├── environments/
│   ├── dev/
│   │   ├── main.tf
│   │   └── terraform.tfvars
│   ├── test/
│   │   ├── main.tf
│   │   └── terraform.tfvars
│   ├── staging/
│   │   ├── main.tf
│   │   └── terraform.tfvars
│   └── prod/
│       ├── main.tf
│       └── terraform.tfvars
└── modules/
    └── webapp/
```

**Configurazione specifica per ambiente**:

**dev/terraform.tfvars**:
```hcl
ambiente = "dev"
tipo_istanza = "t3.small"
dimensione_minima = 1
dimensione_massima = 3
abilita_protezione_eliminazione = false
giorni_retention_backup = 7
```

**prod/terraform.tfvars**:
```hcl
ambiente = "prod"
tipo_istanza = "t3.large"
dimensione_minima = 3
dimensione_massima = 10
abilita_protezione_eliminazione = true
giorni_retention_backup = 30
```

---

# Controlli di sicurezza nei pipeline

## Separazione degli account di servizio

**Buona pratica**: Account di servizio/credenziali separati per ambiente

**Esempio AWS**:

- Pipeline Dev: utilizza il ruolo IAM `dev-deployment-role`
- Pipeline Test: utilizza il ruolo IAM `test-deployment-role`
- Pipeline Produzione: utilizza il ruolo IAM `prod-deployment-role`

**Perché**: Se il pipeline dev è compromesso, l'attaccante non può distribuire in produzione.

## Gestione dei segreti per ambiente

**Integrazione HashiCorp Vault**:

```groovy
pipeline {
    agent any
    stages {
        stage('Distribuire') {
            steps {
                script {
                    def secrets = [
                        [path: "${AMBIENTE}/database",
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

**Percorsi Vault per ambiente**:

- `dev/database/password`
- `test/database/password`
- `prod/database/password`

## Monitoraggio e avvisi post-distribuzione

**Validazione post-distribuzione**:

```bash
#!/bin/bash
# smoke-tests.sh

AMBIENTE=$1
APP_URL="https://${AMBIENTE}.example.com"

# Verifica dello stato di salute
if curl -f "${APP_URL}/health" > /dev/null 2>&1; then
    echo "✅ Verifica di salute superata"
else
    echo "❌ Verifica di salute FALLITA"
    exit 1
fi

# Connettività del database
if curl -f "${APP_URL}/db-check" > /dev/null 2>&1; then
    echo "✅ Connettività database OK"
else
    echo "❌ Connettività database FALLITA"
    exit 1
fi

# Verifica delle prestazioni (tempo di risposta < 2 secondi)
TEMPO_RISPOSTA=$(curl -o /dev/null -s -w '%{time_total}' "${APP_URL}")
if (( $(echo "$TEMPO_RISPOSTA < 2.0" | bc -l) )); then
    echo "✅ Tempo di risposta OK (${TEMPO_RISPOSTA}s)"
else
    echo "❌ Tempo di risposta troppo lento (${TEMPO_RISPOSTA}s)"
    exit 1
fi

echo "Tutti i test di fumo superati!"
```

---

# Errori comuni e migliori pratiche

## Cosa NON fare

❌ **Credenziali condivise tra gli ambienti**: Produzione e dev che utilizzano lo stesso ruolo IAM AWS → Rischio di sicurezza

❌ **Nessuna porta di approvazione per la produzione**: Distribuzione automatica in produzione → Modifiche non testate raggiungono i clienti

❌ **Segreti di produzione nel codice**: `DATABASE_PASSWORD=prod_secret_123` codificato → Esposto nei registri

❌ **Distribuzione diretta in produzione**: Il pipeline aggira lo staging → Nessuna validazione prima della produzione

❌ **Nessun piano di rollback**: La distribuzione fallisce → Nessuna procedura di recupero documentata

## Migliori pratiche

✅ Credenziali separate per ambiente  
✅ Porta di approvazione manuale per la produzione  
✅ Segreti archiviati in un vault (HashiCorp Vault, AWS Secrets Manager)  
✅ Percorso di promozione obbligatorio (dev → test → staging → prod)  
✅ Rollback automatizzato in caso di errore  
✅ Test di fumo post-distribuzione  
✅ Monitoraggio della distribuzione (Datadog, New Relic)  
✅ Registrazione degli audit (chi ha distribuito cosa, quando)  
✅ Protezione del branch (solo il branch main → produzione)  
✅ Applicazione delle finestre di modifica (produzione solo durante le ore approvate)

---

**FINE DEL DOCUMENTO DI RIFERIMENTO**

---

*Questo riferimento tecnico supporta ISMS-POL-A.8.31. Le configurazioni dei pipeline CI/CD devono essere riviste e approvate dal Responsabile DevOps e dal RSSI.*

<!-- QA_VERIFIED: 2026-04-04 -->
