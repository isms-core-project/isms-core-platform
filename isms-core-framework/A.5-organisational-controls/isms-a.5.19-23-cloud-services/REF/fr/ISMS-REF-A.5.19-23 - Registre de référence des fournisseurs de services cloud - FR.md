<!-- ISMS-CORE:REF:ISMS-REF-A.5.19-23-FR-cloud-service-provider-registry:framework:REF:a.5.19-23 -->
**ISMS-REF-A.5.19-23 — Registre de référence des fournisseurs de services cloud**
**Référence officielle pour l'évaluation des fournisseurs cloud et SaaS tiers**

---

**Contrôle documentaire**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Registre de référence des fournisseurs de services cloud |
| **Type de document** | Interne — Référence technique (hors SMSI) |
| **Identifiant du document** | ISMS-REF-A.5.19-23 |
| **Créateur du document** | Responsable de la Sécurité des Systèmes d'Information (RSSI) |
| **Propriétaire du document** | Directeur général (DG) |
| **Approuvé par** | RSSI (Référence technique — aucune approbation de la Direction générale requise) |
| **Date de création** | [Date] |
| **Version** | 1.0 |
| **Date de version** | [À déterminer] |
| **Classification** | Interne |
| **Statut** | Brouillon |

**Historique des versions** :

| Version | Date | Auteur | Modifications |
|---------|------|--------|---------------|
| 1.0 | [Date] | RSSI / Opérations informatiques | Création initiale du registre |

**Cycle de révision** : Semestriel (ou lors de modifications significatives du paysage fournisseurs)
**Prochaine date de révision** : [Date d'approbation + 6 mois]
**Approbateurs** :

- Responsable de la Sécurité des Systèmes d'Information (RSSI)
- Responsable des opérations informatiques
- Achats / Gestion des fournisseurs

**Distribution** : Parties prenantes du SMSI, propriétaires de systèmes, achats, gestion des fournisseurs
**Référencé par** : ISMS-POL-A.5.19 à A.5.23, ISMS-POL-A.8.10, évaluations fournisseurs

---

**Objet**

Ce document constitue le **registre de référence officiel** des fournisseurs de services cloud et des plateformes SaaS couramment rencontrés dans les environnements informatiques organisationnels.

**Utilisation :**

- Prépopuler les classeurs d'évaluation (A.5.23, A.8.10, etc.)
- Standardiser la catégorisation des fournisseurs au sein du SMSI
- Permettre une évaluation cohérente des risques fournisseurs
- Soutenir la conformité en matière de suppression et de conservation des données (A.8.10)

**Principe fondamental :** Ce registre est **neutre vis-à-vis des fournisseurs à des fins politiques** — il répertorie les fournisseurs à des fins d'évaluation, non d'approbation. Les organisations documentent LEUR utilisation et leurs configurations spécifiques.

---

# Cadre de classification des fournisseurs

**Catégories de modèles de service**

| Code | Modèle | Description |
|------|--------|-------------|
| **IaaS** | Infrastructure as a Service | Machines virtuelles, stockage, réseau |
| **PaaS** | Platform as a Service | Plateformes de développement, environnements d'exécution gérés |
| **SaaS** | Software as a Service | Applications destinées aux utilisateurs finaux |
| **DBaaS** | Database as a Service | Services de bases de données gérés |
| **BaaS** | Backup as a Service | Services de sauvegarde et récupération gérés |
| **SECaaS** | Security as a Service | Services de sécurité gérés |
| **IDaaS** | Identity as a Service | Gestion des identités et des accès |
| **CDN** | Content Delivery Network | Mise en cache et distribution par point de présence |

## Niveaux de priorité d'évaluation

| Niveau | Priorité | Critères | Fréquence d'évaluation |
|--------|----------|----------|------------------------|
| **Niveau 1** | Critique | Hyperscalers, infrastructure centrale | Trimestrielle |
| **Niveau 2** | Critique | Principales plateformes d'entreprise | Trimestrielle |
| **Niveau 3** | Élevée | Fournisseurs d'infrastructure & sécurité | Semestrielle |
| **Niveau 4** | Élevée | Spécialistes sauvegarde & stockage | Semestrielle |
| **Niveau 5** | Élevée | Communication & collaboration | Semestrielle |
| **Niveau 6** | Moyenne | Plateformes DevOps & développement | Annuelle |
| **Niveau 7** | Moyenne | Bases de données & analytique gérées | Annuelle |
| **Niveau 8** | Élevée | Sécurité & identité (sensibles) | Semestrielle |
| **Niveau 9** | Élevée | RH & Finance (forte teneur en DCP) | Semestrielle |
| **Niveau 10** | Régionale | Fournisseurs régionaux suisses/UE | Semestrielle |

## Indicateurs de sensibilité des données

| Indicateur | Description | Priorité de suppression |
|------------|-------------|-------------------------|
| 🔴 **DCP** | Données à Caractère Personnel | Critique (Art. 17 RGPD) |
| 🟠 **PCI** | Données de l'industrie des cartes de paiement | Critique (PCI DSS) |
| 🟡 **CONF** | Données d'affaires confidentielles | Élevée |
| 🟢 **INT** | Données internes | Moyenne |
| ⚪ **PUB** | Données publiques | Faible |

---

# Registre des fournisseurs

## Niveau 1 : Hyperscalers (Critique)

Fournisseurs d'infrastructure cloud centrale avec présence mondiale.

| Fournisseur | Modèle de service | Siège social | Services clés | Sensibilité des données | Pertinence SMSI |
|-------------|-------------------|--------------|---------------|-------------------------|-----------------|
| **Microsoft Azure** | IaaS, PaaS | États-Unis (régions UE) | Calcul, Stockage, Bases de données, IA | 🔴🟡 | A.5.23, A.8.10, A.8.24 |
| **Microsoft 365** | SaaS | États-Unis (régions UE) | Exchange, SharePoint, OneDrive, Teams | 🔴🟡 | A.5.23, A.8.10, A.8.24 |
| **Amazon Web Services (AWS)** | IaaS, PaaS | États-Unis (régions UE) | EC2, S3, RDS, Glacier | 🔴🟡 | A.5.23, A.8.10, A.8.24 |
| **Google Cloud Platform (GCP)** | IaaS, PaaS | États-Unis (régions UE) | Calcul, Stockage, BigQuery | 🔴🟡 | A.5.23, A.8.10, A.8.24 |
| **Google Workspace** | SaaS | États-Unis (régions UE) | Gmail, Drive, Docs, Meet | 🔴🟡 | A.5.23, A.8.10 |

**Notes d'évaluation :**

- Tous les fournisseurs de Niveau 1 proposent des options de résidence des données dans l'UE
- Requièrent des Accords de traitement des données (ATD) avec des Clauses Contractuelles Types (CCT)
- Capacités de suppression bien documentées — vérifier la conservation dans les sauvegardes
- Effacement cryptographique généralement disponible

---

## Niveau 2 : Principaux fournisseurs d'entreprise (Critique)

Plateformes de niveau entreprise pour les opérations métier.

| Fournisseur | Modèle de service | Siège social | Services clés | Sensibilité des données | Pertinence SMSI |
|-------------|-------------------|--------------|---------------|-------------------------|-----------------|
| **Oracle Cloud (OCI)** | IaaS, PaaS, SaaS | États-Unis (régions UE) | Base de données, Calcul, ERP, HCM | 🔴🟡 | A.5.23, A.8.10 |
| **IBM Cloud** | IaaS, PaaS | États-Unis (régions UE) | Stockage, IA, Bases de données | 🟡 | A.5.23, A.8.10 |
| **SAP** | SaaS, PaaS | Allemagne | S/4HANA, SuccessFactors, BTP | 🔴🟡 | A.5.23, A.8.10 |
| **Salesforce** | SaaS | États-Unis (régions UE) | CRM, Marketing, Service Cloud | 🔴🟡 | A.5.23, A.8.10 |
| **ServiceNow** | SaaS | États-Unis (régions UE) | ITSM, Workflows, CMDB | 🟡 | A.5.23, A.8.10 |

**Notes d'évaluation :**

- SAP dont le siège est dans l'UE (Allemagne) — favorable pour le RGPD
- Oracle et Salesforce nécessitent un examen attentif des ATD
- La CMDB ServiceNow peut contenir des secrets d'infrastructure

---

## Niveau 3 : Fournisseurs d'infrastructure & sécurité (Élevé)

Fournisseurs CDN, sécurité de périmètre et IaaS alternatifs.

| Fournisseur | Modèle de service | Siège social | Services clés | Sensibilité des données | Pertinence SMSI |
|-------------|-------------------|--------------|---------------|-------------------------|-----------------|
| **Cloudflare** | CDN, Sécurité, IaaS | États-Unis | CDN, WAF, R2 Storage, Workers | 🟡 | A.5.23, A.8.10, A.8.23 |
| **Akamai** | CDN, Sécurité | États-Unis | CDN, WAF, Sécurité de périmètre | 🟡 | A.5.23, A.8.23 |
| **Fastly** | CDN | États-Unis | Calcul de périmètre, CDN | 🟡 | A.5.23 |
| **DigitalOcean** | IaaS | États-Unis | Droplets, Spaces, Bases de données | 🟡 | A.5.23, A.8.10 |
| **Linode (Akamai)** | IaaS | États-Unis | VMs, Stockage, Kubernetes | 🟡 | A.5.23, A.8.10 |
| **OVHcloud** | IaaS | France | Hébergement, Stockage, Cloud | 🟡 | A.5.23, A.8.10 |
| **Hetzner** | IaaS | Allemagne | Hébergement, Stockage, Cloud | 🟡 | A.5.23, A.8.10 |
| **Vultr** | IaaS | États-Unis | VMs, Stockage, Kubernetes | 🟡 | A.5.23, A.8.10 |

**Notes d'évaluation :**

- OVHcloud et Hetzner ont leur siège dans l'UE (favorable au RGPD)
- Les fournisseurs CDN mettent en cache des données au point de présence — la propagation de la suppression est importante
- Cloudflare R2 est compatible S3 — vérifier les mécanismes de suppression

---

## Niveau 4 : Spécialistes sauvegarde & stockage (Élevé)

Fournisseurs dédiés à la sauvegarde, l'archivage et le stockage objet.

| Fournisseur | Modèle de service | Siège social | Services clés | Sensibilité des données | Pertinence SMSI |
|-------------|-------------------|--------------|---------------|-------------------------|-----------------|
| **Veeam Cloud Connect** | BaaS | États-Unis/Suisse | Référentiels de sauvegarde | 🔴🟡 | A.5.23, A.8.10 |
| **Commvault** | BaaS | États-Unis | Sauvegarde, Archivage, Récupération | 🔴🟡 | A.5.23, A.8.10 |
| **Rubrik** | BaaS | États-Unis | Sauvegarde, Récupération après ransomware | 🔴🟡 | A.5.23, A.8.10 |
| **Cohesity** | BaaS | États-Unis | Sauvegarde, Gestion des données | 🔴🟡 | A.5.23, A.8.10 |
| **Wasabi** | Stockage | États-Unis | Stockage chaud compatible S3 | 🟡 | A.5.23, A.8.10 |
| **Backblaze B2** | Stockage | États-Unis | Stockage compatible S3 | 🟡 | A.5.23, A.8.10 |
| **Dropbox Business** | SaaS | États-Unis | Synchronisation de fichiers, Collaboration | 🔴🟡 | A.5.23, A.8.10 |
| **Box** | SaaS | États-Unis | Gestion de contenu | 🔴🟡 | A.5.23, A.8.10 |

**Notes d'évaluation :**

- Les fournisseurs de sauvegarde sont CRITIQUES pour A.8.10 — les données persistent dans les sauvegardes après la suppression primaire
- Vérifier que les durées de conservation des sauvegardes sont alignées sur les exigences de suppression
- Les fonctionnalités de sauvegarde immuable peuvent entrer en conflit avec les obligations de suppression
- Veeam a une présence en Suisse (favorable pour les organisations suisses)

---

## Niveau 5 : Communication & Collaboration (Élevé)

Plateformes de messagerie, vidéoconférence et collaboration d'équipe.

| Fournisseur | Modèle de service | Siège social | Services clés | Sensibilité des données | Pertinence SMSI |
|-------------|-------------------|--------------|---------------|-------------------------|-----------------|
| **Slack** | SaaS | États-Unis | Messagerie, Fichiers, Intégrations | 🔴🟡 | A.5.23, A.8.10 |
| **Zoom** | SaaS | États-Unis | Vidéo, Enregistrements, Chat | 🔴🟡 | A.5.23, A.8.10 |
| **Cisco Webex** | SaaS | États-Unis | Vidéo, Messagerie, Réunions | 🔴🟡 | A.5.23, A.8.10 |
| **Atlassian Cloud** | SaaS | Australie | Jira, Confluence, Bitbucket | 🟡 | A.5.23, A.8.10 |
| **Notion** | SaaS | États-Unis | Espaces de travail, Documentation | 🟡 | A.5.23, A.8.10 |
| **Asana** | SaaS | États-Unis | Projets, Tâches | 🟡 | A.5.23, A.8.10 |
| **Monday.com** | SaaS | Israël | Projets, Workflows | 🟡 | A.5.23, A.8.10 |

**Notes d'évaluation :**

- Les plateformes collaboratives accumulent d'importantes DCP au fil du temps
- Les enregistrements de réunions nécessitent des politiques de suppression explicites
- La conservation des messages Slack/Teams entre souvent en conflit avec les exigences de suppression
- Atlassian a son siège en Australie — vérifier la résidence des données

---

## Niveau 6 : Plateformes DevOps & Développement (Moyen)

Plateformes de code source, CI/CD et conteneurs.

| Fournisseur | Modèle de service | Siège social | Services clés | Sensibilité des données | Pertinence SMSI |
|-------------|-------------------|--------------|---------------|-------------------------|-----------------|
| **GitHub** | SaaS | États-Unis (Microsoft) | Dépôts, Actions, Packages | 🟡 | A.5.23, A.8.10 |
| **GitLab** | SaaS/Auto-hébergé | États-Unis/Pays-Bas | Dépôts, CI/CD, Registre | 🟡 | A.5.23, A.8.10 |
| **Bitbucket** | SaaS | Australie (Atlassian) | Dépôts, Pipelines | 🟡 | A.5.23, A.8.10 |
| **Docker Hub** | SaaS | États-Unis | Images de conteneurs | 🟡 | A.5.23, A.8.10 |
| **JFrog** | SaaS | États-Unis/Israël | Artéfacts, Registre de conteneurs | 🟡 | A.5.23, A.8.10 |
| **Terraform Cloud** | SaaS | États-Unis (HashiCorp) | Fichiers d'état, Espaces de travail | 🟡🔴 | A.5.23, A.8.10 |

**Notes d'évaluation :**

- Les dépôts de code source peuvent contenir des secrets (clés API, identifiants)
- Les fichiers d'état Terraform contiennent souvent des détails d'infrastructure sensibles
- Les images de conteneurs peuvent embarquer des secrets — la suppression doit couvrir toutes les couches
- GitLab dispose d'une entité dans l'UE (Pays-Bas) — vérifier l'emplacement du traitement des données

---

## Niveau 7 : Bases de données & Analytique (Moyen)

Plateformes de bases de données gérées et d'analytique des données.

| Fournisseur | Modèle de service | Siège social | Services clés | Sensibilité des données | Pertinence SMSI |
|-------------|-------------------|--------------|---------------|-------------------------|-----------------|
| **MongoDB Atlas** | DBaaS | États-Unis | Bases de données documentaires | 🔴🟡 | A.5.23, A.8.10 |
| **Snowflake** | SaaS | États-Unis | Entrepôt de données | 🔴🟡 | A.5.23, A.8.10 |
| **Databricks** | SaaS | États-Unis | Analytique, Lakehouse | 🔴🟡 | A.5.23, A.8.10 |
| **Elastic Cloud** | SaaS | États-Unis/Pays-Bas | Elasticsearch, Journaux | 🔴🟡 | A.5.23, A.8.10, A.8.16 |
| **Redis Cloud** | DBaaS | États-Unis | Cache, Bases de données | 🟡 | A.5.23, A.8.10 |
| **PlanetScale** | DBaaS | États-Unis | Compatible MySQL | 🔴🟡 | A.5.23, A.8.10 |
| **Supabase** | DBaaS | États-Unis | PostgreSQL, Stockage | 🔴🟡 | A.5.23, A.8.10 |

**Notes d'évaluation :**

- Les entrepôts de données (Snowflake, Databricks) agrègent souvent des DCP de sources multiples
- Les index Elasticsearch utilisés pour la journalisation peuvent contenir des DCP — vérifier la conservation
- Les sauvegardes de bases de données et la récupération ponctuelle complexifient la suppression
- Elastic dispose d'une présence dans l'UE (Pays-Bas)

---

## Niveau 8 : Sécurité & Identité (Élevé — Sensibles)

Plateformes d'opérations de sécurité et de gestion des identités.

| Fournisseur | Modèle de service | Siège social | Services clés | Sensibilité des données | Pertinence SMSI |
|-------------|-------------------|--------------|---------------|-------------------------|-----------------|
| **Okta** | IDaaS | États-Unis | Identité, SSO, AMF | 🔴 | A.5.23, A.8.10, A.5.15 |
| **Auth0** | IDaaS | États-Unis (Okta) | Identité, Gestion des utilisateurs | 🔴 | A.5.23, A.8.10, A.5.15 |
| **CrowdStrike** | SECaaS | États-Unis | EDR, Threat Intelligence | 🟡 | A.5.23, A.8.10 |
| **SentinelOne** | SECaaS | États-Unis/Israël | EDR, XDR | 🟡 | A.5.23, A.8.10 |
| **Splunk Cloud** | SaaS | États-Unis (Cisco) | Agrégation de journaux, SIEM | 🔴🟡 | A.5.23, A.8.10, A.8.16 |
| **Datadog** | SaaS | États-Unis | Surveillance, Journaux, APM | 🟡 | A.5.23, A.8.10, A.8.16 |
| **New Relic** | SaaS | États-Unis | APM, Journaux, Surveillance | 🟡 | A.5.23, A.8.10 |

**Notes d'évaluation :**

- Les fournisseurs d'identité (Okta, Auth0) stockent des DCP d'utilisateurs — critique pour la suppression RGPD
- Les plateformes SIEM/journaux agrègent les données de l'ensemble de l'infrastructure
- La télémétrie EDR peut contenir des données sensibles des terminaux
- Les politiques de conservation des journaux doivent être alignées sur les exigences de suppression

---

## Niveau 9 : RH & Finance (Élevé — Forte teneur en DCP)

Plateformes de gestion des ressources humaines et financières.

| Fournisseur | Modèle de service | Siège social | Services clés | Sensibilité des données | Pertinence SMSI |
|-------------|-------------------|--------------|---------------|-------------------------|-----------------|
| **Workday** | SaaS | États-Unis | RH, Finance, Planification | 🔴 | A.5.23, A.8.10 |
| **ADP** | SaaS | États-Unis | Paie, RH | 🔴 | A.5.23, A.8.10 |
| **BambooHR** | SaaS | États-Unis | Gestion RH | 🔴 | A.5.23, A.8.10 |
| **Personio** | SaaS | Allemagne | RH (orienté UE) | 🔴 | A.5.23, A.8.10 |
| **Xero** | SaaS | Nouvelle-Zélande | Comptabilité | 🔴🟠 | A.5.23, A.8.10 |
| **QuickBooks Online** | SaaS | États-Unis (Intuit) | Comptabilité | 🔴🟠 | A.5.23, A.8.10 |
| **Stripe** | SaaS | États-Unis/Irlande | Paiements | 🔴🟠 | A.5.23, A.8.10 |
| **PayPal** | SaaS | États-Unis | Paiements | 🔴🟠 | A.5.23, A.8.10 |

**Notes d'évaluation :**

- Les systèmes RH contiennent des DCP étendues des employés — les droits de suppression RGPD s'appliquent
- Personio a son siège dans l'UE (Allemagne) — favorable pour le RGPD
- Les processeurs de paiement (Stripe, PayPal) ont des exigences de conservation PCI DSS
- Les systèmes financiers ont des obligations légales de conservation qui peuvent primer sur la suppression
- Stripe dispose d'une entité dans l'UE (Irlande)

---

## Niveau 10 : Fournisseurs régionaux suisses/UE (Régional)

Fournisseurs dont le siège social ou les centres de données sont en Suisse ou dans l'UE.

| Fournisseur | Modèle de service | Siège social | Services clés | Sensibilité des données | Pertinence SMSI |
|-------------|-------------------|--------------|---------------|-------------------------|-----------------|
| **Exoscale** | IaaS | Suisse | Calcul, Stockage, Kubernetes | 🟡 | A.5.23, A.8.10 |
| **Infomaniak** | IaaS, SaaS | Suisse | Hébergement, kDrive, Messagerie | 🔴🟡 | A.5.23, A.8.10 |
| **Proton (ProtonMail/Drive)** | SaaS | Suisse | Messagerie chiffrée, Stockage | 🔴🟡 | A.5.23, A.8.10, A.8.24 |
| **Tresorit** | SaaS | Suisse | Stockage chiffré | 🔴🟡 | A.5.23, A.8.10, A.8.24 |
| **STACKIT** | IaaS | Allemagne | Cloud (Groupe Schwarz) | 🟡 | A.5.23, A.8.10 |
| **IONOS** | IaaS | Allemagne | Hébergement, Cloud | 🟡 | A.5.23, A.8.10 |
| **Scaleway** | IaaS | France | Cloud, Stockage | 🟡 | A.5.23, A.8.10 |

**Notes d'évaluation :**

- Les fournisseurs suisses (Exoscale, Infomaniak, Proton, Tresorit) sont soumis à la nLPD suisse
- Pas d'exposition à la loi CLOUD Act des États-Unis pour les fournisseurs exclusivement suisses
- Proton et Tresorit utilisent le chiffrement de bout en bout — vérifier la suppression des données chiffrées
- Les fournisseurs allemands/français sont soumis au RGPD de l'UE (favorable)
- STACKIT est filiale du Groupe Schwarz (Lidl/Kaufland) — cloud allemand de niveau entreprise

---

# Résumé du registre

## Nombre de fournisseurs par niveau

| Niveau | Catégorie | Nombre | Priorité |
|--------|-----------|--------|----------|
| 1 | Hyperscalers | 5 | Critique |
| 2 | Fournisseurs d'entreprise | 5 | Critique |
| 3 | Infrastructure & Sécurité | 8 | Élevée |
| 4 | Sauvegarde & Stockage | 8 | Élevée |
| 5 | Collaboration | 7 | Élevée |
| 6 | DevOps | 6 | Moyenne |
| 7 | Base de données & Analytique | 7 | Moyenne |
| 8 | Sécurité & Identité | 7 | Élevée |
| 9 | RH & Finance | 8 | Élevée |
| 10 | Régional Suisse/UE | 7 | Régionale |
| **TOTAL** | | **68** | |

## Nombre de fournisseurs par région de siège social

| Région | Nombre | Notes |
|--------|--------|-------|
| États-Unis | 48 | La plupart nécessitent un ATD avec des CCT pour les données UE/CH |
| UE (Allemagne, France, Pays-Bas, Irlande) | 10 | Natifs RGPD |
| Suisse | 4 | Natifs nLPD, pas de loi CLOUD Act |
| Autres (Israël, Australie, Nouvelle-Zélande) | 6 | Vérifier les décisions d'adéquation |

## Nombre de fournisseurs par sensibilité des données

| Sensibilité | Nombre | Priorité de suppression |
|-------------|--------|-------------------------|
| 🔴 DCP (Données personnelles) | 42 | Critique |
| 🟠 PCI (Données de paiement) | 6 | Critique |
| 🟡 Confidentiel | 58 | Élevée |
| 🟢 Interne | 68 | Moyenne |

---

# Intégration avec les évaluations

## Contrôles SMSI associés

| Contrôle | Point d'intégration |
|----------|---------------------|
| **A.5.19** | Sécurité de l'information dans les relations avec les fournisseurs |
| **A.5.20** | Prise en compte de la sécurité de l'information dans les accords fournisseurs |
| **A.5.21** | Gestion de la sécurité de l'information dans la chaîne d'approvisionnement TIC |
| **A.5.22** | Surveillance, révision et gestion des changements des services fournisseurs |
| **A.5.23** | Sécurité de l'information pour l'utilisation des services cloud |
| **A.8.10** | Suppression de l'information |
| **A.8.24** | Utilisation de la cryptographie |

## Prépopulation des classeurs Excel

Ce registre DOIT être utilisé pour prépopuler :

1. **ISMS-IMP-A.5.19-23.x** — Classeurs d'évaluation des services cloud
2. **ISMS-IMP-A.8.10.3** — Évaluation de la suppression tiers & cloud
3. **Registre des risques fournisseurs** — Évaluations des risques fournisseurs
4. **Registre des activités de traitement** — Enregistrements Article 30 RGPD

## Configuration des listes déroulantes

**Liste déroulante Nom du fournisseur** (68 entrées + personnalisé) :
```
Microsoft Azure
Microsoft 365
Amazon Web Services (AWS)
Google Cloud Platform (GCP)
Google Workspace
Oracle Cloud (OCI)
[... tous les 68 fournisseurs ...]
[Personnalisé - préciser dans les notes]
```

**Liste déroulante Modèle de service** :
```
IaaS - Infrastructure as a Service
PaaS - Platform as a Service
SaaS - Software as a Service
DBaaS - Database as a Service
BaaS - Backup as a Service
SECaaS - Security as a Service
IDaaS - Identity as a Service
CDN - Content Delivery Network
Hybride/Multiple
```

**Liste déroulante Niveau** :
```
Niveau 1 - Hyperscaler (Critique)
Niveau 2 - Entreprise (Critique)
Niveau 3 - Infrastructure (Élevé)
Niveau 4 - Sauvegarde/Stockage (Élevé)
Niveau 5 - Collaboration (Élevé)
Niveau 6 - DevOps (Moyen)
Niveau 7 - Base de données (Moyen)
Niveau 8 - Sécurité (Élevé)
Niveau 9 - RH/Finance (Élevé)
Niveau 10 - Régional (Régional)
Personnalisé
```

---

# Maintenance

## Déclencheurs de mise à jour

Ce registre DOIT être mis à jour lorsque :

- Un nouveau fournisseur cloud est adopté par l'organisation
- Un fournisseur subit un changement significatif (acquisition, modification de politique)
- De nouvelles exigences réglementaires affectent l'évaluation des fournisseurs
- Lors du cycle de révision semestriel

**Journal des modifications**

| Date | Modification | Auteur |
|------|-------------|--------|
| [Date] | Création initiale du registre | [Auteur] |

---

# Annexe A : Carte de référence rapide

```
┌─────────────────────────────────────────────────────────────────────┐
│           RÉFÉRENCE RAPIDE D'ÉVALUATION DES FOURNISSEURS CLOUD      │
├─────────────────────────────────────────────────────────────────────┤
│  CRITIQUE (Évaluation trimestrielle)                                │
│  • Niveau 1 : Azure, M365, AWS, GCP, Google Workspace               │
│  • Niveau 2 : Oracle, IBM, SAP, Salesforce, ServiceNow              │
│                                                                     │
│  PRIORITÉ ÉLEVÉE (Évaluation semestrielle)                          │
│  • Niveau 3 : Cloudflare, Akamai, OVH, Hetzner                      │
│  • Niveau 4 : Veeam, Rubrik, Wasabi, Dropbox, Box                   │
│  • Niveau 5 : Slack, Zoom, Atlassian, Teams                         │
│  • Niveau 8 : Okta, CrowdStrike, Splunk, Datadog                    │
│  • Niveau 9 : Workday, Personio, Stripe                             │
│                                                                     │
│  PRIORITÉ MOYENNE (Évaluation annuelle)                             │
│  • Niveau 6 : GitHub, GitLab, Docker Hub                            │
│  • Niveau 7 : MongoDB, Snowflake, Elastic                           │
│                                                                     │
│  PRÉFÉRÉS SUISSES/UE                                                │
│  • CH : Exoscale, Infomaniak, Proton, Tresorit                      │
│  • DE : SAP, Hetzner, STACKIT, IONOS                                │
│  • FR : OVHcloud, Scaleway                                          │
│  • NL : GitLab, Elastic                                             │
│  • IE : Stripe                                                       │
├─────────────────────────────────────────────────────────────────────┤
│  🔴 DCP = Droits de suppression Art. 17 RGPD applicables            │
│  🟠 PCI = Exigences de conservation des cartes de paiement          │
│  🟡 CONF = Suppression standard selon la politique de conservation   │
└─────────────────────────────────────────────────────────────────────┘
```

---

> *« Pour qu'une technologie soit un succès, la réalité doit primer sur les relations publiques, car la nature ne peut être trompée. »*
*— Richard Feynman*

**Traduction pour le SMSI :** Le marketing de votre fournisseur cloud dit « nous prenons la sécurité au sérieux ». Ce registre vous aide à vérifier ce que cela signifie concrètement pour VOS données.

---

**FIN DU DOCUMENT**

<!-- QA_VERIFIED: 2026-03-30 -->
