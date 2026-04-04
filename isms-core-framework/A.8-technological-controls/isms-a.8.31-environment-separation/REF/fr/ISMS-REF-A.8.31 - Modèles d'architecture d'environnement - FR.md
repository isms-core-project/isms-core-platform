<!-- ISMS-CORE:REF:ISMS-REF-A.8.31-FR-environment-architecture-patterns:framework:REF:a.8.31 -->
**ISMS-REF-A.8.31 — Modèles d'architecture d'environnement**
**Référence technique pour l'implémentation des infrastructures**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Modèles d'architecture d'environnement |
| **Type de document** | Document de référence (Référence technique non-SMSI) |
| **Identifiant du document** | ISMS-REF-A.8.31 |
| **Créateur du document** | Responsable des opérations IT / Architecte cloud |
| **Propriétaire du document** | RSSI |
| **Approuvé par** | Responsable des opérations IT (Référence technique — aucune approbation exécutive requise) |
| **Date de création** | [Date] |
| **Version** | 1.0 |
| **Classification** | Interne |
| **Statut** | Brouillon |

**Distribution** : Opérations IT, Architecture cloud, DevOps, Propriétaires de systèmes

---

⚠️ **IMPORTANT — DOCUMENT DE SUPPORT TECHNIQUE NON-SMSI**

Ce document est fourni à des fins d'information et de sensibilisation uniquement. Il ne fait PAS partie du SMSI, n'établit PAS d'exigences contraignantes et ne remplace PAS ISMS-POL-A.8.31.

---

# Objectif et portée du document

## Objectif

Ce document fournit des modèles de référence technique pour l'implémentation de la séparation des environnements sur les plateformes d'infrastructure courantes. Il est destiné à soutenir :

- La sensibilisation technique aux approches de séparation spécifiques aux plateformes
- La compréhension des modèles de comptes/abonnements des fournisseurs cloud
- Les décisions d'architecture d'infrastructure
- La planification de l'implémentation

## Relation avec la politique SMSI

**Exigences contraignantes** : ISMS-POL-A.8.31 définit CE QUI est requis (isolation réseau, séparation d'infrastructure, séparation des identifiants, etc.)

**Ce document** : Fournit COMMENT ces exigences peuvent être implémentées sur des plateformes spécifiques (multi-compte AWS, abonnements Azure, espaces de noms Kubernetes, etc.)

---

# Modèle multi-compte AWS

## Vue d'ensemble de l'architecture

**Structure des Organisations AWS** :

Structure recommandée utilisant des Unités Organisationnelles (OU) pour regrouper les comptes par environnement :

```
Organisation racine
├── OU Sécurité
│   ├── Compte Audit (journaux CloudTrail, rapports de conformité)
│   └── Compte Outils de sécurité (GuardDuty, SecurityHub, Inspector)
├── OU Développement
│   ├── Compte Dev 1 (Équipe A — Développement)
│   ├── Compte Dev 2 (Équipe B — Développement)
│   └── Compte Services Dev Partagés (outils DevOps, référentiels d'artefacts)
├── OU Test
│   ├── Compte Test 1 (Équipe A — Test)
│   └── Compte Services Test Partagés (outils d'automatisation QA)
├── OU Staging
│   ├── Compte Staging 1 (Équipe A — Pré-production)
│   └── Compte Staging 2 (Équipe B — Pré-production)
└── OU Production
    ├── Compte Production 1 (Équipe A — Production)
    ├── Compte Production 2 (Équipe B — Production)
    └── Services Partagés Production (surveillance, sauvegarde, reprise après sinistre)
```

**Pourquoi le multi-compte** :

- **Frontière IAM** : Les politiques IAM ne peuvent pas franchir les limites des comptes (empêche l'accès dev → prod)
- **Rayon d'impact** : La compromission du compte dev n'affecte pas la production
- **Attribution des coûts** : Facturation séparée par environnement
- **Limites de service** : Quotas de service séparés par compte
- **Piste d'audit** : Journaux CloudTrail séparés par compte

## Séparation réseau

**VPC (Virtual Private Cloud) par environnement** :

Blocs CIDR recommandés (espace d'adressage privé RFC 1918) :

- VPC Développement : 10.1.0.0/16 (65 536 IPs)
- VPC Test : 10.2.0.0/16 (65 536 IPs)
- VPC Staging : 10.3.0.0/16 (65 536 IPs)
- VPC Production : 10.4.0.0/16 (65 536 IPs)

**Configuration d'appairage VPC** :

Appairage contrôlé entre environnements adjacents uniquement :

- ✅ Appairage Dev ↔ Test : Autorisé (pipelines de déploiement)
- ✅ Appairage Test ↔ Staging : Autorisé (flux de promotion)
- ✅ Appairage Staging ↔ Production : Autorisé (automatisation de déploiement)
- ❌ Appairage Dev ↔ Production : **INTERDIT** (connexion directe viole la séparation)

**Groupes de sécurité** :

- Refus par défaut (pas de trafic entrant sauf si explicitement autorisé)
- Groupes de sécurité séparés par environnement
- Groupes de sécurité production : gérés via Terraform/CloudFormation uniquement
- Dénomination : `{environnement}-{service}-{direction}` (ex. `prod-web-entrant`)

## Contrôle d'accès (IAM)

**Modèle d'accès basé sur les rôles** :

**Rôles IAM Développeurs** (dans le compte Dev uniquement) :
```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Action": ["ec2:*", "s3:*", "rds:*"],
    "Resource": "*",
    "Condition": {
      "StringEquals": {"aws:RequestedRegion": "eu-central-1"}
    }
  }]
}
```

**Rôles IAM Opérations** (dans le compte Production) :

- Exiger MFA pour l'accès console
- Durée de session : 4 heures maximum
- Workflow d'approbation requis avant AssumeRole

**AssumeRole inter-comptes** (pipeline de déploiement) :
```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Principal": {"AWS": "arn:aws:iam::ID-COMPTE-DEV:root"},
    "Action": "sts:AssumeRole",
    "Resource": "arn:aws:iam::ID-COMPTE-TEST:role/DeploymentRole",
    "Condition": {
      "StringEquals": {"sts:ExternalId": "id-externe-unique-de-deploiement"}
    }
  }]
}
```

**Rôle d'urgence (Break-Glass)** (Production) :

- MFA obligatoire
- Approbation requise
- Durée de session : 4 heures
- Journalisation : toutes les actions enregistrées dans CloudTrail + alerte SNS

## Séparation des données

**Buckets S3** (par environnement) :

- Dénomination : `{environnement}-{app}-{usage}-{id-compte}`
- Exemples : `dev-webapp-data-123456789012`, `prod-webapp-data-345678901234`

**Politiques de bucket S3** (production — empêcher l'accès inter-comptes) :
```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Deny",
    "Principal": "*",
    "Action": "s3:*",
    "Resource": "arn:aws:s3:::prod-webapp-data-*/*",
    "Condition": {
      "StringNotEquals": {"aws:PrincipalAccount": "ID-COMPTE-PROD"}
    }
  }]
}
```

**Bases de données RDS** :

- Instances RDS séparées par environnement
- Production RDS : chiffrement au repos (clé gérée par le client AWS KMS), sauvegardes automatiques (7-35 jours), déploiement Multi-AZ, surveillance avancée
- Dev/Test RDS : types d'instances plus petits acceptables, Single-AZ acceptable

**AWS Secrets Manager** :

- Secrets séparés par environnement
- Convention de dénomination : `{environnement}/{service}/{secret}` (ex. `prod/webapp/db-password`)
- Secrets de production : rotation automatique activée (30-90 jours)

---

# Modèle multi-abonnement Azure

## Vue d'ensemble de l'architecture

**Hiérarchie des groupes de gestion Azure** :

```
Groupe racine du tenant
├── Groupe de gestion Sécurité
│   ├── Abonnement Audit (journaux Azure Monitor, Log Analytics)
│   └── Abonnement Outils de sécurité (Microsoft Defender, Sentinel)
├── Groupe de gestion Développement
│   ├── Abonnement Dev — Équipe A
│   └── Abonnement Dev — Équipe B
├── Groupe de gestion Test
│   └── Abonnements Test
├── Groupe de gestion Staging
│   └── Abonnements Staging
└── Groupe de gestion Production
    ├── Abonnement Production — Équipe A
    └── Abonnement Production — Équipe B
```

**Pourquoi le multi-abonnement** :

- **Application des politiques Azure** : Les politiques au niveau du groupe de gestion se propagent aux abonnements
- **Frontière RBAC** : Azure RBAC ne franchit pas les limites d'abonnement
- **Gestion des coûts** : Facturation et budgets séparés par abonnement
- **Confinement du rayon d'impact** : La compromission d'un abonnement dev est isolée de la production

## Séparation réseau

**Réseaux virtuels (VNets)** par abonnement :

- VNet Développement : 10.10.0.0/16
- VNet Test : 10.20.0.0/16
- VNet Staging : 10.30.0.0/16
- VNet Production : 10.40.0.0/16

**Groupes de sécurité réseau (NSG)** :

- Refus de tout trafic entrant par défaut
- Règles d'autorisation explicites pour le trafic requis
- NSG Production : géré via Azure Policy (empêcher la substitution manuelle)

**Appairage VNet** :

- Topologie hub-and-spoke (VNet hub central pour les services partagés)
- VNets spoke (Dev, Test, Staging, Prod) appairent uniquement avec le Hub
- Routage transitif désactivé (Dev ne peut pas atteindre Prod via Hub)

## Contrôle d'accès (Azure RBAC)

**Attributions de rôles par environnement** :

**Développeurs** (Abonnement Dev) :

- Rôle : Contributeur (peut créer/modifier des ressources)
- Portée : Groupes de ressources dans l'abonnement Dev
- Ne peut pas accéder aux abonnements Test/Staging/Prod

**Équipe QA** (Abonnement Test) :

- Rôle : Lecteur + accès spécifique à l'application
- Portée : Groupes de ressources de l'abonnement Test

**Opérations** (Abonnement Production) :

- Rôle : Contributeur (via Privileged Identity Management — PIM)
- Exigences : Activation JIT (Just-in-Time) + MFA + approbation
- Session : 4 heures maximum
- Audit : toutes les actions journalisées dans Log Analytics

**Accès conditionnel Azure AD** :

L'accès à la production requiert :

- Appareil géré (conformité Intune)
- Authentification multi-facteurs (AMF)
- Emplacement réseau approuvé
- Politiques basées sur les risques (Azure AD Identity Protection)

## Séparation des données

**Comptes de stockage Azure** :

- Dénomination : `{env}{app}{usage}{idunique}` (max 24 caractères)
- Exemples : `devwebappdata001abc`, `prodwebappdata003pqr`

**Azure SQL Database** :

- Serveurs Azure SQL séparés par environnement
- Production SQL : TDE activé, sauvegardes automatiques (7-35 jours), géo-réplication pour la reprise après sinistre, Advanced Threat Protection
- Dev/Test SQL : niveaux de performance inférieurs acceptables

**Azure Key Vault** :

- Coffres-forts séparés par environnement
- Dénomination : `{environnement}-{app}-kv` (ex. `prod-webapp-kv`)
- Key Vault Production : suppression réversible activée (90 jours), protection de purge activée, point de terminaison privé, règles de pare-feu

## Application des politiques Azure

**Politiques du groupe de gestion** :

**Groupe de gestion Production** (appliqué à tous les abonnements production) :
```json
{
  "policyRule": {
    "if": {
      "allOf": [
        {"field": "type", "equals": "Microsoft.Storage/storageAccounts"},
        {"field": "Microsoft.Storage/storageAccounts/encryption.keySource",
         "notEquals": "Microsoft.KeyVault"}
      ]
    },
    "then": {"effect": "deny"}
  }
}
```
Traduction : Les comptes de stockage production DOIVENT utiliser des clés de chiffrement gérées par le client.

---

# Modèle multi-projet GCP

## Vue d'ensemble de l'architecture

**Hiérarchie d'organisation GCP** :

```
Organisation (example.com)
├── Dossier Sécurité
│   └── Projet Outils de sécurité (Security Command Center)
├── Dossier Développement
│   ├── Projet Dev — Équipe A
│   └── Projet Dev — Équipe B
├── Dossier Test
├── Dossier Staging
└── Dossier Production
    ├── Projet Production — Équipe A
    └── Projet Production — Équipe B
```

**Pourquoi le multi-projet** :

- **Frontière IAM** : Politiques IAM limitées aux projets
- **Facturation** : Comptes de facturation séparés par projet
- **Quotas** : Quotas de ressources séparés par projet
- **Audit** : Cloud Audit Logs séparés par projet

## Séparation réseau

**Réseaux VPC** (par projet) :

- Développement VPC : 10.100.0.0/16
- Test VPC : 10.110.0.0/16
- Staging VPC : 10.120.0.0/16
- Production VPC : 10.130.0.0/16

**Règles de pare-feu** :

- Refus de tout trafic entrant par défaut
- Règles d'autorisation explicites requises
- Règles de pare-feu production : gérées via Terraform

## Contrôle d'accès (Cloud IAM)

**Rôles IAM par environnement** :

**Développeurs** (Projet Dev) :

- Rôle : `roles/editor` (peut créer/modifier des ressources)
- Portée : Projet dev uniquement

**Opérations** (Projet Production) :

- Rôles de portée limitée (compute.admin, storage.admin)
- Accès contextuel + MFA requis
- Limité dans le temps (4 heures via identifiants temporaires)

**Comptes de service d'application** :

- Comptes de service séparés par environnement
- Dénomination : `{env}-{app}-sa@{id-projet}.iam.gserviceaccount.com`
- Comptes de service production : rotation des clés appliquée (90 jours)

## Séparation des données

**Buckets Cloud Storage** :

- Production : versioning activé, politique de rétention (30 jours minimum), clés de chiffrement gérées par le client (Cloud KMS)

**Cloud SQL** :

- Instances Cloud SQL séparées par projet
- Production : sauvegardes automatiques, haute disponibilité (régionale), IP privée uniquement, chiffrement Cloud KMS

**Secret Manager** :

- Secrets séparés par projet
- Dénomination : `{environnement}_{service}_{secret}` (ex. `prod_webapp_db_password`)
- Production : rotation automatique

---

# Séparation des environnements Kubernetes

## Options d'architecture

**Option 1 : Séparation par espace de noms** (cluster unique) :
```
Cluster Kubernetes (partagé)
├── espace de noms dev
├── espace de noms test
├── espace de noms staging
└── espace de noms production
```

**Avantages** : Efficacité des ressources, gestion plus simple  
**Inconvénients** : Isolation plus faible (la production partage le plan de contrôle avec dev)  
**Cas d'usage** : Petites organisations, applications à faible risque

**Option 2 : Séparation par cluster** (clusters distincts) :
```
Cluster Développement
Cluster Test
Cluster Staging
Cluster Production (séparé)
```

**Avantages** : Isolation forte (plan de contrôle de production séparé)  
**Inconvénients** : Surcharge opérationnelle plus élevée, coût plus élevé  
**Cas d'usage** : Grandes organisations, applications à risque élevé

**Recommandé** : Séparation par cluster pour la production, par espace de noms pour dev/test/staging.

## Séparation par espace de noms

**Configuration de l'espace de noms** :

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: production
  labels:
    environment: production
---
apiVersion: v1
kind: ResourceQuota
metadata:
  name: prod-quota
  namespace: production
spec:
  hard:
    requests.cpu: "100"
    requests.memory: 200Gi
    persistentvolumeclaims: "10"
```

**Politiques réseau** (isoler les espaces de noms) :

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: deny-from-other-namespaces
  namespace: production
spec:
  podSelector: {}
  policyTypes:
  - Ingress
  ingress:
  - from:
    - namespaceSelector:
        matchLabels:
          environment: production
```

**RBAC** :

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: developers
  namespace: dev
subjects:
- kind: Group
  name: developers
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: ClusterRole
  name: edit
  apiGroup: rbac.authorization.k8s.io
```

## Séparation par cluster

**Clusters EKS/AKS/GKE distincts** :

**Cluster Développement** :

- Nombre de nœuds : Auto-scaling 2-10
- Taille des nœuds : Petits types d'instances (optimisation des coûts)
- Surveillance : Basique (Prometheus)

**Cluster Production** :

- Nombre de nœuds : Auto-scaling 5-50
- Taille des nœuds : Instances haute performance
- Surveillance : Observabilité complète (Prometheus, Grafana, traçage Jaeger)
- Haute disponibilité : Pools de nœuds Multi-AZ

**Normes de sécurité des pods** :

- Production : `restricted` (sécurité maximale)
- Staging : `restricted`
- Test : `baseline`
- Dev : `privileged` (les développeurs ont besoin de flexibilité)

---

# Infrastructure sur site / Traditionnelle

## Séparation basée sur les VLAN

**Segmentation réseau** :

```
Réseau principal (192.168.0.0/16)
├── VLAN 10 : Développement (192.168.10.0/24)
├── VLAN 20 : Test (192.168.20.0/24)
├── VLAN 30 : Staging (192.168.30.0/24)
└── VLAN 40 : Production (192.168.40.0/24)
```

**Règles de pare-feu entre VLAN** :

- Refus de tout trafic par défaut
- ACL permettant le trafic de déploiement (dev → test → staging → prod)
- VLAN Production : aucun trafic entrant depuis les VLAN dev/test

---

# Infrastructure hybride

## Cloud + sur site

**Architecture** :

- Développement/Test : basé sur le cloud (AWS/Azure/GCP)
- Production : centre de données sur site (exigence réglementaire)

**Connectivité** :

- VPN ou Direct Connect / ExpressRoute / Cloud Interconnect

**Cas d'usage** : Organisations en migration vers le cloud (maintien de la production sur site pendant la transition)

---

# Cadre de décision

## Choisir l'approche de séparation

| Facteur | Par espace de noms | Par compte/abonnement | Séparation physique |
|---------|-------------------|----------------------|---------------------|
| **Coût** | Faible (ressources partagées) | Moyen (comptes séparés) | Élevé (infrastructure dupliquée) |
| **Isolation** | Moyen (logique uniquement) | Élevé (limites du compte) | Maximum (physique) |
| **Conformité** | Risque faible-moyen | Risque élevé acceptable | Maximum (finance, santé) |
| **Complexité** | Faible | Moyen | Élevé |
| **Recommandé pour** | Petites org., faible risque | La plupart des organisations | Industries réglementées |

## Chemin de migration

**Phase 1** : Commencer par la séparation par espace de noms (rapide à implémenter)  
**Phase 2** : Migrer vers la séparation par compte/abonnement (isolation plus forte)  
**Phase 3** : Envisager la séparation physique pour la production uniquement (si exigence réglementaire)

---

**FIN DU DOCUMENT DE RÉFÉRENCE**

---

*Cette référence technique soutient ISMS-POL-A.8.31. Les décisions d'implémentation doivent être basées sur l'évaluation des risques organisationnels et approuvées par le RSSI.*

<!-- QA_VERIFIED: 2026-04-04 -->
