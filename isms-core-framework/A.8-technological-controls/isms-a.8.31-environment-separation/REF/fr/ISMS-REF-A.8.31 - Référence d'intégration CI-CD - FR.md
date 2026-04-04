<!-- ISMS-CORE:REF:ISMS-REF-A.8.31-FR-cicd-pipeline-integration:framework:REF:a.8.31 -->
**ISMS-REF-A.8.31 — Référence d'intégration CI/CD**
**Référence technique pour l'implémentation du pipeline de déploiement**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Référence d'intégration CI/CD |
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
| 1.0 | [Date] | DevOps / Opérations IT | Référence technique initiale pour l'intégration de pipelines CI/CD |

**Cycle de révision** : Selon les besoins (évolution des technologies et des outils)  
**Prochaine date de révision** : [Date + 12 mois]

**Distribution** : Ingénieurs DevOps, Équipes de développement, Opérations IT

---

⚠️ **IMPORTANT — DOCUMENT DE SUPPORT TECHNIQUE NON-SMSI**

Ce document est fourni à des fins d'information et de sensibilisation uniquement. Il ne fait PAS partie du SMSI, n'établit PAS d'exigences contraignantes et ne remplace PAS ISMS-POL-A.8.31.

---

# Objectif et portée du document

## Objectif

Ce document fournit des modèles de référence technique pour l'intégration des contrôles de séparation des environnements dans les pipelines CI/CD. Il est destiné à soutenir :

- La sensibilisation technique aux modèles de sécurité des pipelines
- La compréhension des flux de déploiement spécifiques aux environnements
- La sélection et configuration des plateformes CI/CD
- La planification future de l'implémentation

## Relation avec la politique SMSI

**Exigences contraignantes** : ISMS-POL-A.8.31 définit CE QUI est requis (chemin de promotion contrôlé, portes d'approbation, etc.)

**Ce document** : Fournit COMMENT ces exigences peuvent être implémentées sur des plateformes CI/CD (Jenkins, GitLab CI, GitHub Actions, etc.)

---

# Architecture de pipeline CI/CD pour la séparation des environnements

## Structure du pipeline

**Conception de pipeline adaptée aux environnements** :

```
┌─────────────────────────────────────────────────────────┐
│              DÉPÔT DE CODE SOURCE                        │
│             (Git, GitHub, GitLab, etc.)                  │
└──────────────────────┬──────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────┐
│       PLATEFORME D'ORCHESTRATION CI/CD                   │
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
       │     AUTO     │     AUTO     │   MANUEL      │
       ▼              ▼              ▼              ▼
  ┌────────┐     ┌────────┐     ┌────────┐     ┌────────┐
  │  ENV   │     │  ENV   │     │  ENV   │     │  ENV   │
  │  DEV   │     │  TEST  │     │STAGING │     │  PROD  │
  └────────┘     └────────┘     └────────┘     └────────┘
```

**Principes clés** :

- Jobs/étapes de pipeline distincts par environnement
- Promotion automatisée de dev → test → staging
- Porte d'approbation manuelle avant le déploiement en production
- Validation de l'environnement à chaque étape
- Identifiants séparés par environnement

## Portes et approbations de déploiement

**Exigences d'approbation par environnement** :

| De → À | Type d'approbation | Qui approuve | Contrôles supplémentaires |
|--------|-------------------|--------------|--------------------------|
| Dev → Test | Automatique | Aucun (après build réussi) | Tests unitaires réussis (100 %) |
| Test → Staging | Automatique ou semi-auto | Responsable QA (optionnel) | Tests d'intégration réussis |
| Staging → Production | **MANUEL** | Comité consultatif sur les changements (CAB) | Tous les tests réussis, approbation CAB, vérification de la fenêtre de déploiement |

**Exigences de la porte de déploiement production** :

- Approbation manuelle explicite requise
- Approbation du personnel autorisé uniquement (équipe des opérations, gestionnaire des changements)
- Déploiement limité aux fenêtres de changement approuvées
- Plan de retour arrière documenté et accessible
- Tests de fumée définis pour la validation post-déploiement
- Tableaux de bord de surveillance vérifiés avant approbation

## Validation de l'environnement

**Liste de contrôle de validation pré-déploiement** :

```yaml
# Pseudo-code pour la validation de l'environnement
valider_environnement:
  - verifier_que_lenvironnement_cible_est_correct
  - confirmer_que_les_credentials_correspondent_a_lenvironnement_cible
  - confirmer_aucun_credentials_production_en_non_prod
  - valider_la_connectivite_reseau_vers_la_cible
  - verifier_disponibilite_ressources (CPU, mémoire, disque)
  - verifier_que_la_fenetre_de_deploiement_est_ouverte (pour production)
```

---

# Exemples spécifiques aux plateformes

## Jenkins Pipeline

**Jenkinsfile avec séparation des environnements** :

```groovy
pipeline {
    agent any
    
    parameters {
        choice(name: 'ENVIRONMENT', 
               choices: ['dev', 'test', 'staging', 'production'], 
               description: 'Environnement cible pour le déploiement')
    }
    
    stages {
        stage('Build') {
            steps {
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
            when { expression { params.ENVIRONMENT == 'dev' } }
            steps { deployerVersEnvironnement('dev') }
        }
        
        stage('Tests d\'intégration') {
            when {
                expression { params.ENVIRONMENT in ['test', 'staging', 'production'] }
            }
            steps { sh 'mvn verify -Pintegration-tests' }
        }
        
        stage('Déployer en Test') {
            when { expression { params.ENVIRONMENT == 'test' } }
            steps { deployerVersEnvironnement('test') }
        }
        
        stage('Déployer en Staging') {
            when { expression { params.ENVIRONMENT == 'staging' } }
            steps {
                input message: 'Approuver le déploiement en Staging ?',
                      submitter: 'qa-team'
                deployerVersEnvironnement('staging')
            }
        }
        
        stage('Porte d\'approbation production') {
            when { expression { params.ENVIRONMENT == 'production' } }
            steps {
                script {
                    def heureActuelle = new Date().getHours()
                    if (heureActuelle < 9 || heureActuelle > 17) {
                        error("Déploiement production autorisé uniquement de 9h à 17h")
                    }
                }
                input message: 'Approbation CAB requise pour la PRODUCTION',
                      submitter: 'change-advisory-board,operations-team',
                      parameters: [
                          string(name: 'TICKET_CAB', description: 'Numéro de ticket d\'approbation CAB'),
                          text(name: 'PLAN_RETOUR', description: 'Décrire la procédure de retour arrière')
                      ]
            }
        }
        
        stage('Déployer en Production') {
            when { expression { params.ENVIRONMENT == 'production' } }
            steps {
                deployerVersEnvironnement('production')
                sh './scripts/smoke-tests.sh production'
            }
        }
    }
    
    post {
        success { echo "Déploiement vers ${params.ENVIRONMENT} réussi !" }
        failure { echo "Déploiement vers ${params.ENVIRONMENT} ÉCHOUÉ !" }
    }
}

def deployerVersEnvironnement(environnement) {
    withCredentials([
        string(credentialsId: "${environnement}-api-key", variable: 'API_KEY'),
        usernamePassword(credentialsId: "${environnement}-db-creds",
                         usernameVariable: 'DB_USER',
                         passwordVariable: 'DB_PASS')
    ]) {
        sh """
            ./deploy.sh \\
                --environment ${environnement} \\
                --artifact ${ARTIFACT_PATH} \\
                --api-key \$API_KEY
        """
    }
}
```

**Caractéristiques clés** :

- Identifiants séparés par environnement (Jenkins Credentials Plugin)
- Porte d'approbation production avec exigence CAB
- Enforcement de la fenêtre de déploiement (production uniquement pendant les heures ouvrables)
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

build:
  stage: build
  image: maven:3.8-openjdk-17
  script:
    - mvn clean package
  artifacts:
    paths:
      - target/app.jar
    expire_in: 1 week

tests-unitaires:
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

**Caractéristiques clés** :

- Comptes de service distincts par environnement (GCP_DEV_KEY, GCP_TEST_KEY, etc.)
- Approbation manuelle pour staging et production (`when: manual`)
- Protection de branche (seule la branche main peut déployer en production)
- Tests de fumée post-déploiement pour la production

**Environnements protégés GitLab** (configurer dans l'interface GitLab) :

Paramètres → CI/CD → Environnements protégés

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
      - name: Configurer JDK 17
        uses: actions/setup-java@v3
        with:
          java-version: '17'
          distribution: 'temurin'
      - name: Build avec Maven
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
      - name: Déployer en Production
        env:
          AWS_ACCESS_KEY_ID: ${{ secrets.AWS_PROD_ACCESS_KEY }}
          AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_PROD_SECRET_KEY }}
        run: |
          aws lambda update-function-code \
            --function-name prod-webapp \
            --s3-bucket prod-deployment-bucket \
            --s3-key app.jar
      - name: Tests de fumée
        run: ./scripts/smoke-tests.sh production
```

**Règles de protection des environnements GitHub** (configurer dans GitHub) :

Dépôt → Paramètres → Environnements

**Environnement Production** :

- Réviseurs requis : groupe `operations-team` (au moins 2 approbations)
- Branches de déploiement : Uniquement la branche `main`
- Minuterie d'attente : 5 minutes (période de refroidissement)
- Secrets d'environnement : `AWS_PROD_ACCESS_KEY`, `AWS_PROD_SECRET_KEY`

**Environnement Staging** :

- Réviseurs requis : groupe `qa-team` (au moins 1 approbation)
- Branches de déploiement : Uniquement la branche `main`

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

- stage: DeployProduction
  dependsOn: DeployStaging
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
            displayName: 'Tests de fumée production'
```

**Approbations et vérifications Azure DevOps** (configurer dans Azure DevOps) :

Pipelines → Environnements → Production

- Approbateurs requis : `Operations Team`, minimum 2 approbations
- Délai d'expiration : 30 jours
- Porte des heures ouvrables : Déploiements autorisés uniquement 9h-17h
- Contrôle de branche : Uniquement la branche `main`

---

# Intégration de l'Infrastructure en tant que Code (IaC)

## Modèles Terraform par environnement

**Structure de répertoires** :

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

**Configuration spécifique à l'environnement** :

**dev/terraform.tfvars** :
```hcl
environnement = "dev"
type_instance = "t3.small"
taille_min = 1
taille_max = 3
activer_protection_suppression = false
jours_retention_backup = 7
```

**prod/terraform.tfvars** :
```hcl
environnement = "prod"
type_instance = "t3.large"
taille_min = 3
taille_max = 10
activer_protection_suppression = true
jours_retention_backup = 30
```

---

# Contrôles de sécurité dans les pipelines

## Séparation des comptes de service

**Bonne pratique** : Comptes de service/identifiants séparés par environnement

**Exemple AWS** :

- Pipeline Dev : utilise le rôle IAM `dev-deployment-role`
- Pipeline Test : utilise le rôle IAM `test-deployment-role`
- Pipeline Production : utilise le rôle IAM `prod-deployment-role`

**Pourquoi** : Si le pipeline dev est compromis, l'attaquant ne peut pas déployer en production.

## Gestion des secrets par environnement

**Intégration HashiCorp Vault** :

```groovy
pipeline {
    agent any
    stages {
        stage('Déployer') {
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

**Chemins Vault par environnement** :

- `dev/database/password`
- `test/database/password`
- `prod/database/password`

## Surveillance et alertes post-déploiement

**Validation post-déploiement** :

```bash
#!/bin/bash
# smoke-tests.sh

ENVIRONMENT=$1
APP_URL="https://${ENVIRONMENT}.example.com"

# Vérification de l'état de santé
if curl -f "${APP_URL}/health" > /dev/null 2>&1; then
    echo "✅ Vérification de santé réussie"
else
    echo "❌ Vérification de santé ÉCHOUÉE"
    exit 1
fi

# Connectivité base de données
if curl -f "${APP_URL}/db-check" > /dev/null 2>&1; then
    echo "✅ Connectivité base de données OK"
else
    echo "❌ Connectivité base de données ÉCHOUÉE"
    exit 1
fi

# Vérification des performances (temps de réponse < 2 secondes)
TEMPS_REPONSE=$(curl -o /dev/null -s -w '%{time_total}' "${APP_URL}")
if (( $(echo "$TEMPS_REPONSE < 2.0" | bc -l) )); then
    echo "✅ Temps de réponse OK (${TEMPS_REPONSE}s)"
else
    echo "❌ Temps de réponse trop lent (${TEMPS_REPONSE}s)"
    exit 1
fi

echo "Tous les tests de fumée réussis !"
```

---

# Écueils courants et meilleures pratiques

## Ce qu'il NE FAUT PAS faire

❌ **Identifiants partagés entre les environnements** : Production et dev utilisant le même rôle IAM AWS → Risque de sécurité

❌ **Pas de porte d'approbation pour la production** : Déploiement automatique en production → Changements non testés atteignent les clients

❌ **Secrets de production dans le code** : `DATABASE_PASSWORD=prod_secret_123` codé en dur → Exposé dans les journaux

❌ **Déploiement direct en production** : Le pipeline contourne le staging → Aucune validation avant la production

❌ **Pas de plan de retour arrière** : Le déploiement échoue → Aucune procédure de récupération documentée

## Meilleures pratiques

✅ Identifiants séparés par environnement  
✅ Porte d'approbation manuelle pour la production  
✅ Secrets stockés dans un coffre-fort (HashiCorp Vault, AWS Secrets Manager)  
✅ Chemin de promotion obligatoire (dev → test → staging → prod)  
✅ Retour arrière automatisé en cas d'échec  
✅ Tests de fumée post-déploiement  
✅ Surveillance du déploiement (Datadog, New Relic)  
✅ Journalisation d'audit (qui a déployé quoi, quand)  
✅ Protection de branche (seule la branche main → production)  
✅ Enforcement des fenêtres de changement (production uniquement pendant les heures approuvées)

---

**FIN DU DOCUMENT DE RÉFÉRENCE**

---

*Cette référence technique soutient ISMS-POL-A.8.31. Les configurations de pipelines CI/CD doivent être revues et approuvées par le Responsable DevOps et le RSSI.*

<!-- QA_VERIFIED: 2026-04-04 -->
