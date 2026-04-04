<!-- ISMS-CORE:REF:ISMS-REF-A.8.31-FR-cicd-pipeline-integration:framework:REF:a.8.31 -->
**ISMS-REF-A.8.31 — Intégration du pipeline CI/CD**
**Référence technique pour l'implémentation du pipeline de déploiement**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Référence d'intégration du pipeline CI/CD |
| **Type de document** | Document de référence (Référence technique non-SMSI) |
| **Identifiant du document** | ISMS-REF-A.8.31-CICD |
| **Créateur du document** | Responsable DevOps / Responsable des opérations IT |
| **Propriétaire du document** | Responsable de la sécurité des systèmes d'information (RSSI) |
| **Approuvé par** | Responsable DevOps (Référence technique — aucune approbation exécutive requise) |
| **Date de création** | [Date] |
| **Version** | 1.0 |
| **Date de version** | [À déterminer] |
| **Classification** | Interne |
| **Statut** | Brouillon |

**Historique des versions** :

| Version | Date | Auteur | Modifications |
|---------|------|--------|---------------|
| 1.0 | [Date] | DevOps / Opérations IT | Référence technique initiale pour l'intégration du pipeline CI/CD |

**Cycle de révision** : Selon les besoins (évolution des technologies et des outils)  
**Prochaine date de révision** : [Date + 12 mois]

**Distribution** : Ingénieurs DevOps, équipes de développement, opérations IT (pour la sensibilisation technique à l'implémentation)

---

⚠️ **IMPORTANT — DOCUMENT DE SUPPORT TECHNIQUE NON-SMSI**

Ce document est fourni à des fins d'information et de sensibilisation uniquement.

- Ce document NE fait PAS partie du Système de management de la sécurité de l'information (SMSI).
- Ce document NE définit PAS de contrôles ou d'exigences de pipeline CI/CD obligatoires.
- Ce document N'établit PAS d'exigences contraignantes, de délais, d'ICP ou de SLA.
- Ce document N'impose PAS l'utilisation, l'interdiction ou la configuration de plateformes, d'outils ou de configurations CI/CD spécifiques.
- Ce document NE remplace NI n'étend aucune politique SMSI.

Toutes les exigences de séparation des environnements contraignantes, obligations et décisions de gouvernance sont définies exclusivement dans **ISMS-POL-A.8.31 (Politique de séparation des environnements)** et autres documentations SMSI approuvées.

---

# Objectif et portée du document

## Objectif

Ce document fournit des patterns de référence techniques pour intégrer les contrôles de séparation des environnements dans les pipelines CI/CD. Il vise à soutenir :

- La sensibilisation technique aux patterns de sécurité des pipelines
- La compréhension des flux de déploiement spécifiques aux environnements
- Le contexte pour la sélection et la configuration de plateformes CI/CD
- La planification future des discussions d'implémentation

## Relation avec la politique SMSI

**Exigences contraignantes** : ISMS-POL-A.8.31 définit **CE QUI** est requis comme contrôles de promotion des environnements (chemin de promotion contrôlé, portes d'approbation, etc.)

**Ce document** : Fournit **COMMENT** ces exigences peuvent être implémentées dans les plateformes CI/CD (Jenkins, GitLab CI, GitHub Actions, etc.)

---

# Architecture du pipeline CI/CD pour la séparation des environnements

## Structure du pipeline

**Conception du pipeline par environnement** :

```
┌─────────────────────────────────────────────────────────┐
│           DÉPÔT DE CODE SOURCE                           │
│             (Git, GitHub, GitLab, etc.)                  │
└──────────────────────┬──────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────┐
│         PLATEFORME D'ORCHESTRATION CI/CD                 │
│     (Jenkins, GitLab CI, GitHub Actions, etc.)           │
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
       │     AUTO     │     AUTO     │   MANUEL     │
       ▼              ▼              ▼              ▼
  ┌────────┐     ┌────────┐     ┌────────┐     ┌────────┐
  │  ENV   │     │  ENV   │     │  ENV   │     │  ENV   │
  │  DEV   │     │  TEST  │     │STAGING │     │  PROD  │
  └────────┘     └────────┘     └────────┘     └────────┘
```

**Principes clés** :

- Jobs/étapes de pipeline séparés par environnement
- Promotion automatisée de dev → test → staging
- Porte d'approbation manuelle avant le déploiement en production
- Validation de l'environnement à chaque étape
- Identifiants séparés par environnement

## Portes de déploiement et approbations

**Exigences d'approbation par environnement** :

| De → Vers | Type d'approbation | Qui approuve | Vérifications supplémentaires |
|-----------|-------------------|--------------|-------------------------------|
| Dev → Test | Automatique | Aucun (sur build réussi) | Tests unitaires réussis (100%) |
| Test → Staging | Automatique ou semi-automatique | Responsable QA (optionnel) | Tests d'intégration réussis |
| Staging → Production | **MANUEL** | Comité consultatif des changements (CAB) | Tous les tests réussis, approbation CAB, vérification de la fenêtre de déploiement |

**Exigences de la porte de déploiement en production** :

- Approbation manuelle explicite requise
- Approbation du personnel autorisé uniquement (équipe opérations, gestionnaire des changements)
- Déploiement limité aux fenêtres de changement approuvées
- Plan de retour arrière documenté et accessible
- Tests de fumée définis pour la validation post-déploiement
- Tableaux de bord de monitoring examinés avant l'approbation

---

# Exemples spécifiques aux plateformes

## Pipeline Jenkins

**Jenkinsfile avec séparation des environnements** :

```groovy
pipeline {
    agent any
    
    parameters {
        choice(name: 'ENVIRONMENT', 
               choices: ['dev', 'test', 'staging', 'production'], 
               description: "Environnement cible pour le déploiement")
    }
    
    environment {
        APP_NAME = 'webapp'
        ARTIFACT_PATH = "${WORKSPACE}/build/app.jar"
    }
    
    stages {
        stage('Build') {
            steps {
                echo "Construction de l'application..."
                sh 'mvn clean package'
            }
        }
        
        stage('Tests unitaires') {
            steps {
                sh 'mvn test'
                junit 'target/surefire-reports/*.xml'
            }
        }
        
        stage('Déployer en Dev') {
            when {
                expression { params.ENVIRONMENT == 'dev' }
            }
            steps {
                deployToEnvironment('dev')
            }
        }
        
        stage('Tests d\'intégration') {
            when {
                expression { params.ENVIRONMENT in ['test', 'staging', 'production'] }
            }
            steps {
                sh 'mvn verify -Pintegration-tests'
            }
        }
        
        stage('Déployer en Test') {
            when {
                expression { params.ENVIRONMENT == 'test' }
            }
            steps {
                deployToEnvironment('test')
            }
        }
        
        stage('Déployer en Staging') {
            when {
                expression { params.ENVIRONMENT == 'staging' }
            }
            steps {
                input message: 'Approuver le déploiement en Staging ?', 
                      submitter: 'qa-team'
                deployToEnvironment('staging')
            }
        }
        
        stage('Porte d\'approbation Production') {
            when {
                expression { params.ENVIRONMENT == 'production' }
            }
            steps {
                script {
                    // Vérifier si la fenêtre de déploiement est ouverte
                    def currentHour = new Date().getHours()
                    if (currentHour < 9 || currentHour > 17) {
                        error("Déploiement en production uniquement autorisé 9h-17h")
                    }
                }
                
                // Approbation CAB requise
                input message: 'Approbation CAB requise pour la PRODUCTION', 
                      submitter: 'change-advisory-board,operations-team',
                      parameters: [
                          string(name: 'CAB_TICKET', description: 'Numéro du ticket d\'approbation CAB'),
                          text(name: 'ROLLBACK_PLAN', description: 'Décrire la procédure de retour arrière')
                      ]
            }
        }
        
        stage('Déployer en Production') {
            when {
                expression { params.ENVIRONMENT == 'production' }
            }
            steps {
                deployToEnvironment('production')
                // Tests de fumée post-déploiement
                sh './scripts/smoke-tests.sh production'
            }
        }
        
        stage('Validation post-déploiement') {
            steps {
                echo "Exécution de la validation post-déploiement..."
                sh "./scripts/validate-deployment.sh ${params.ENVIRONMENT}"
            }
        }
    }
    
    post {
        success {
            echo "Déploiement vers ${params.ENVIRONMENT} réussi !"
        }
        failure {
            echo "Déploiement vers ${params.ENVIRONMENT} ÉCHOUÉ !"
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
        echo "Déploiement vers ${environment}..."
        sh """
            ./deploy.sh \\
                --environment ${environment} \\
                --artifact ${ARTIFACT_PATH} \\
                --api-key \$API_KEY
        """
    }
}
```

**Fonctionnalités clés** :

- Validation du paramètre d'environnement
- Identifiants séparés par environnement (Plugin Jenkins Credentials)
- Porte d'approbation production avec exigence CAB
- Application des fenêtres de déploiement (production uniquement pendant les heures ouvrables)
- Tests de fumée post-déploiement
- Documentation du plan de retour arrière requise

## GitLab CI/CD

**.gitlab-ci.yml avec séparation des environnements** :

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

**Fonctionnalités clés** :

- Étapes séparées par environnement
- Comptes de service spécifiques à l'environnement
- Approbation manuelle pour staging et production (`when: manual`)
- Protection des branches (seule la branche main peut déployer en production)
- Tests de fumée post-déploiement en production

**Environnements protégés GitLab** :

Configurer dans l'interface GitLab :

- Paramètres → CI/CD → Environnements protégés
- Production : Seul le groupe `operations-team` peut déployer
- Staging : Seuls `qa-team` et `operations-team` peuvent déployer

## GitHub Actions

**.github/workflows/deploy.yml avec séparation des environnements** :

```yaml
name: Déployer dans les environnements

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
      - name: Construire avec Maven
        run: mvn clean package
      - name: Téléverser l'artefact
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
      - name: Déployer en Dev (AWS)
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
      - name: Déployer en Staging
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
      - name: Déployer en Production
        env:
          AWS_ACCESS_KEY_ID: ${{ secrets.AWS_PROD_ACCESS_KEY }}
          AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_PROD_SECRET_KEY }}
        run: |
          aws lambda update-function-code \
            --function-name prod-webapp \
            --s3-bucket prod-deployment-bucket \
            --s3-key app.jar
      - name: Exécuter les tests de fumée
        run: ./scripts/smoke-tests.sh production
```

**Règles de protection d'environnement GitHub** (configurer dans l'interface GitHub) :

**Environnement Production** :

- Réviseurs requis : groupe `operations-team` (au moins 2 approbations)
- Branches de déploiement : uniquement la branche `main`
- Minuterie d'attente : 5 minutes (période de refroidissement)
- Secrets d'environnement : `AWS_PROD_ACCESS_KEY`, `AWS_PROD_SECRET_KEY`

**Environnement Staging** :

- Réviseurs requis : groupe `qa-team` (au moins 1 approbation)
- Branches de déploiement : uniquement la branche `main`

## Azure DevOps Pipelines

**azure-pipelines.yml avec séparation des environnements** :

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
    environment: 'Production'  # Requiert une approbation manuelle dans Azure DevOps
    strategy:
      runOnce:
        deploy:
          steps:
          - task: AzureWebApp@1
            inputs:
              azureSubscription: 'Azure-Prod-ServiceConnection'
              appName: 'webapp-prod'
          - script: ./scripts/smoke-tests.sh production
            displayName: 'Exécuter les tests de fumée de production'
```

**Approbations et vérifications d'environnement Azure DevOps** (configurer dans l'interface) :

- Approbateurs requis : Équipe Operations, minimum 2 approbations
- Délai d'expiration : 30 jours
- Porte des heures ouvrables : Autoriser les déploiements uniquement 9h-17h
- Contrôle de branche : Uniquement la branche `main`

---

# Infrastructure as Code (IaC) — Intégration

## Patterns Terraform par environnement

**Structure de répertoires** :

```
terraform/
├── environments/
│   ├── dev/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   └── terraform.tfvars
│   ├── test/
│   ├── staging/
│   └── prod/
│       ├── main.tf
│       ├── variables.tf
│       └── terraform.tfvars
└── modules/
    └── webapp/
```

**Configuration spécifique à l'environnement** :

**dev/terraform.tfvars** :
```hcl
environment = "dev"
instance_type = "t3.small"
min_size = 1
max_size = 3
enable_deletion_protection = false
backup_retention_days = 7
```

**prod/terraform.tfvars** :
```hcl
environment = "prod"
instance_type = "t3.large"
min_size = 3
max_size = 10
enable_deletion_protection = true
backup_retention_days = 30
```

**Intégration pipeline (GitLab CI)** :

```yaml
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

## Variables d'environnement Ansible

**Structure d'inventaire** :

```
ansible/
├── inventories/
│   ├── dev/group_vars/all.yml
│   ├── test/group_vars/all.yml
│   └── prod/group_vars/all.yml
└── playbooks/deploy.yml
```

**Variables spécifiques à l'environnement** :

**prod/group_vars/all.yml** :
```yaml
environment: prod
app_version: "1.5.2"  # Version spécifique
database_host: prod-db.internal
enable_debug_mode: false
```

---

# Contrôles de sécurité dans les pipelines

## Séparation des comptes de service

**Bonne pratique** : Comptes de service/identifiants séparés par environnement

**Exemple AWS** :

- Pipeline Dev : Utilise le rôle IAM `dev-deployment-role`
- Pipeline Test : Utilise le rôle IAM `test-deployment-role`
- Pipeline Production : Utilise le rôle IAM `prod-deployment-role`

**Pourquoi** : Si le pipeline dev est compromis, l'attaquant ne peut pas déployer en production.

## Gestion des secrets par environnement

**Intégration HashiCorp Vault** :

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

**Chemins Vault par environnement** :

- `dev/database/password`
- `test/database/password`
- `prod/database/password`

## Surveillance et alertes post-déploiement

**Script de validation post-déploiement** :

```bash
#!/bin/bash
ENVIRONMENT=$1
APP_URL="https://${ENVIRONMENT}.example.com"

# Vérification de santé
if curl -f "${APP_URL}/health" > /dev/null 2>&1; then
    echo "✅ Vérification de santé réussie"
else
    echo "❌ Vérification de santé ÉCHOUÉE"
    exit 1
fi

# Vérification de la connectivité de la base de données
if curl -f "${APP_URL}/db-check" > /dev/null 2>&1; then
    echo "✅ Connectivité de la base de données OK"
else
    echo "❌ Connectivité de la base de données ÉCHOUÉE"
    exit 1
fi

# Vérification des performances (temps de réponse < 2 secondes)
RESPONSE_TIME=$(curl -o /dev/null -s -w '%{time_total}' "${APP_URL}")
if (( $(echo "$RESPONSE_TIME < 2.0" | bc -l) )); then
    echo "✅ Temps de réponse OK (${RESPONSE_TIME}s)"
else
    echo "❌ Temps de réponse trop lent (${RESPONSE_TIME}s)"
    exit 1
fi

echo "Tous les tests de fumée réussis !"
```

---

# Erreurs courantes et bonnes pratiques

## Ce qu'il NE FAUT PAS faire

❌ **Identifiants partagés entre environnements** : Production et dev utilisant le même rôle IAM AWS → Risque de sécurité

❌ **Pas de porte d'approbation pour la production** : Déploiement automatique en production → Des changements non testés atteignent les clients

❌ **Secrets de production dans le code** : `DATABASE_PASSWORD=prod_secret_123` codé en dur dans le pipeline → Exposé dans les journaux

❌ **Déploiement direct en production** : Le pipeline contourne le staging → Pas de validation avant la production

❌ **Pas de plan de retour arrière** : Le déploiement échoue → Pas de procédure de récupération documentée

## Bonnes pratiques

✅ Identifiants séparés par environnement  
✅ Porte d'approbation manuelle pour la production  
✅ Secrets stockés dans un coffre (HashiCorp Vault, AWS Secrets Manager)  
✅ Chemin de promotion obligatoire (dev → test → staging → prod)  
✅ Retour arrière automatisé en cas d'échec  
✅ Tests de fumée post-déploiement  
✅ Surveillance du déploiement (Datadog, New Relic)  
✅ Journalisation d'audit (qui a déployé quoi, quand)  
✅ Protection des branches (seule la branche main → production)  
✅ Application des fenêtres de changement (production uniquement pendant les heures approuvées)

---

**FIN DU DOCUMENT DE RÉFÉRENCE**

---

*Cette référence technique soutient ISMS-POL-A.8.31. Les configurations de pipeline CI/CD doivent être revues et approuvées par le Responsable DevOps et le RSSI.*
<!-- QA_VERIFIED: 2026-04-04 -->
