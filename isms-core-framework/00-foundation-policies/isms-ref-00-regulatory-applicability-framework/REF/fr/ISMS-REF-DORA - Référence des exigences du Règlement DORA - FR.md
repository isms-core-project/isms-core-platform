<!-- ISMS-CORE:REF:ISMS-REF-DORA-FR-digital-operational-resilience-act-requirements:framework:REF:dora -->
**ISMS-REF-DORA — Référence des exigences du Règlement sur la résilience opérationnelle numérique (DORA)**
**Exigences de résilience numérique pour le secteur financier de l'UE (Référence technique non-SMSI)**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Référence des exigences DORA |
| **Type de document** | Interne — Référence technique (Non-SMSI) |
| **Identifiant du document** | ISMS-REF-DORA |
| **Créateur du document** | Responsable de la Sécurité des Systèmes d'Information (RSSI) |
| **Propriétaire du document** | Directeur Général (PDG) |
| **Approuvé par** | RSSI (Référence technique — Aucune approbation de la Direction générale requise) |
| **Date de création** | [Date] |
| **Version** | 1.0 |
| **Date de version** | [À déterminer] |
| **Classification** | Interne |
| **Statut** | Brouillon |

**Historique des versions** :

| Version | Date | Auteur | Modifications |
|---------|------|--------|---------------|
| 1.0 | [Date] | RSSI / Juridique/Conformité | Référence technique initiale pour les entités financières de l'UE |

**Cycle de révision** : Annuel (ou lors de mises à jour des normes techniques de réglementation DORA)
**Prochaine date de révision** : [Date + 12 mois]
**Approbateurs** : Juridique/Conformité / RSSI (référence technique, aucune approbation SMSI requise)

**Distribution** : Équipe de conformité, RSSI, Conseil juridique (pour les organisations soumises à DORA)

---

⚠️ **IMPORTANT — DOCUMENT DE SUPPORT TECHNIQUE NON-SMSI**

Ce document est fourni à des fins d'information et de sensibilisation uniquement.

- Ce document ne fait PAS partie du Système de Management de la Sécurité de l'Information (SMSI).
- Ce document ne définit PAS d'exigences obligatoires à moins que [Organisation] ne soit une entité réglementée par DORA.
- Ce document n'établit PAS d'exigences contraignantes, de délais, de KPI ou de SLA pour les entités non réglementées.
- Ce document n'impose PAS l'adoption des exigences DORA aux organisations non soumises à DORA.
- Ce document ne remplace ni n'étend aucune politique du SMSI.

**Détermination de l'applicabilité** :
Les exigences DORA s'appliquent UNIQUEMENT SI [Organisation] :

- Est une entité financière opérant dans l'UE (banques, établissements de paiement, entreprises d'investissement, prestataires de services sur crypto-actifs, assurances, etc.)
- Est désignée comme prestataire tiers de services TIC critique ou important pour des entités financières de l'UE
- A des obligations contractuelles de respecter les exigences DORA

Pour toutes les autres organisations, ce document sert uniquement de :

- Référence technique pour les exigences DORA potentielles
- Contexte pour les relations de prestataires de services avec des entités financières de l'UE
- Sensibilisation aux normes de résilience numérique du secteur financier européen
- **Ce document ne doit pas être utilisé comme preuve d'audit à moins que [Organisation] ne soit réglementée par DORA**

L'utilisation de ce document n'implique pas l'applicabilité de DORA, des obligations de conformité ou un statut réglementaire.

**Déclaration de positionnement critique** :
Ce document fournit intentionnellement des détails réglementaires au-delà de ce qui s'applique à la plupart des organisations. Son objectif est la sensibilisation uniquement pour les organisations susceptibles de devenir soumises à DORA, ou qui fournissent des services TIC à des entités financières réglementées par DORA. Aucune conclusion d'audit ne doit être tirée de la présence, de l'absence ou du statut de mise en œuvre de toute exigence DORA énumérée ici, à moins que [Organisation] ne soit explicitement réglementée par DORA.

---

# Objet et périmètre du document

## Objet

Ce document fournit une vue d'ensemble technique des exigences du Règlement sur la résilience opérationnelle numérique (Règlement (UE) 2022/2554) pour les entités du secteur financier de l'UE. Il vise à soutenir :

- La sensibilisation aux exigences DORA pour les entités financières de l'UE
- La compréhension des cinq piliers de DORA (gestion des risques TIC, notification des incidents, tests, risques liés aux tiers, partage d'informations)
- Le contexte pour les prestataires de services TIC auprès d'entités financières de l'UE
- L'évaluation d'une applicabilité future potentielle
- La mise en correspondance des exigences DORA avec les contrôles ISO 27001:2022

## Ce que ce document n'est PAS

Ce document ne :

- N'établit PAS d'exigences obligatoires pour les organisations non réglementées par DORA
- Ne définit PAS les obligations de conformité de [Organisation] (voir POL-00 pour l'applicabilité réglementaire)
- Ne crée PAS de critères d'audit à moins que [Organisation] ne soit réglementée par DORA
- Ne remplace PAS l'interprétation du conseil juridique ou de conformité
- Ne constitue PAS un avis juridique sur la conformité à DORA
- N'établit PAS de procédures de mise en œuvre ou de processus de vérification
- Ne couvre PAS les Normes Techniques de Réglementation (NTR) de manière exhaustive

## Relation avec le SMSI

Ce document est une **référence technique non contraignante** SAUF si [Organisation] est soumise à DORA (telle que déterminée dans ISMS-POL-00 Section 3.2).

**Si [Organisation] EST réglementée par DORA :**

- Les exigences DORA deviennent Niveau 1 (Conformité obligatoire) selon POL-00
- Ce document fournit des orientations de mise en œuvre
- Les contrôles du SMSI doivent démontrer la conformité DORA
- Une attestation de conformité est requise (rapports de surveillance)

**Si [Organisation] N'EST PAS réglementée par DORA :**

- DORA reste Niveau 3 (Référence informative) selon POL-00
- Ce document est fourni à titre de sensibilisation uniquement
- Aucune obligation de conformité DORA n'existe
- Les contrôles du SMSI suivent uniquement ISO 27001:2022

**Si [Organisation] fournit des services TIC à des entités financières DORA :**

- Peut être désignée comme prestataire tiers de services TIC critique ou important
- Le cadre de surveillance DORA peut s'appliquer (Chapitre V, Section II)
- Les exigences contractuelles référenceront probablement les normes DORA
- À considérer comme Niveau 2 (Conditionnel) en attente de désignation

## Organisation du contenu

Cette référence organise les exigences DORA par :

- Structure en cinq piliers (Chapitres II à VI de DORA)
- Cadre de gestion des risques TIC (Chapitre II)
- Notification des incidents (Chapitre III)
- Tests de résilience opérationnelle numérique (Chapitre IV)
- Gestion des risques liés aux tiers (Chapitre V)
- Arrangements de partage d'informations (Chapitre VI)
- Mise en correspondance avec les contrôles de l'Annexe A de l'ISO 27001:2022

---

# Aperçu et applicabilité de DORA

## Qu'est-ce que DORA ?

Le **Règlement (UE) 2022/2554** sur la résilience opérationnelle numérique du secteur financier est entré en vigueur le 16 janvier 2023 avec application à compter du **17 janvier 2025**.

**Objectif** : Établir des exigences uniformes de résilience opérationnelle numérique dans l'ensemble du secteur financier de l'UE, en traitant :

- Les approches nationales fragmentées en matière de risque TIC
- Les cybermenaces et perturbations TIC croissantes
- Le risque de concentration auprès des prestataires tiers de services TIC
- Le besoin d'une notification harmonisée des incidents
- L'importance du partage de renseignements sur les menaces

**Base juridique** : Règlement de l'UE (directement applicable dans tous les États membres, aucune transposition nationale requise)

**Autorité de surveillance** : Autorités européennes de surveillance (AES) :

- Autorité bancaire européenne (ABE / EBA)
- Autorité européenne des marchés financiers (AEMF / ESMA)
- Autorité européenne des assurances et des pensions professionnelles (AEAPP / EIOPA)
- Plus les autorités nationales compétentes

## Qui doit se conformer à DORA ?

**Entités financières** (Article 2) :

| Catégorie | Exemples | Autorité de surveillance |
|-----------|----------|--------------------------|
| **Établissements de crédit** | Banques | EBA + Autorité nationale |
| **Établissements de paiement** | Prestataires de services de paiement | EBA + Autorité nationale |
| **Établissements de monnaie électronique** | Émetteurs de monnaie électronique | EBA + Autorité nationale |
| **Entreprises d'investissement** | Courtiers, gestionnaires de portefeuille | ESMA + Autorité nationale |
| **Prestataires de services sur crypto-actifs** | Plateformes crypto, dépositaires | ESMA + Autorité nationale |
| **Dépositaires centraux de titres** | DCT | ESMA + Autorité nationale |
| **Plates-formes de négociation** | Bourses, MTF | ESMA + Autorité nationale |
| **Référentiels centraux** | Rapportage des transactions | ESMA + Autorité nationale |
| **Gestionnaires de fonds d'investissement alternatifs** | Fonds spéculatifs, fonds de PE | ESMA + Autorité nationale |
| **Sociétés de gestion** | Gestionnaires d'OPCVM | ESMA + Autorité nationale |
| **Fournisseurs de services de communication de données** | Dispositifs de publication agréés | ESMA + Autorité nationale |
| **Entreprises d'assurance et de réassurance** | Assureurs, réassureurs | EIOPA + Autorité nationale |
| **Intermédiaires d'assurance** | Courtiers en assurance | EIOPA + Autorité nationale |
| **Institutions de retraite professionnelle** | Fonds de pension | EIOPA + Autorité nationale |
| **Agences de notation de crédit** | Agences de notation | ESMA |
| **Administrateurs d'indices de référence critiques** | Fournisseurs d'indices | ESMA |
| **Prestataires de services de financement participatif** | Plateformes de crowdfunding | ESMA + Autorité nationale |
| **Référentiels de titrisation** | Rapportage titrisation | ESMA + Autorité nationale |

**Prestataires tiers de services TIC** (Chapitre V, Section II) :

- Fournisseurs de services d'informatique en nuage
- Fournisseurs de logiciels
- Fournisseurs d'analyses de données
- Fournisseurs de services de centres de données
- **Si désignés comme « critiques »** : Soumis au cadre de surveillance DORA
- **Si désignés comme « importants »** : Exigences contractuelles renforcées

## Détermination de l'applicabilité

**DORA s'applique à [Organisation] SI** :

| Critère | Statut | Preuve |
|---------|--------|--------|
| Entité financière opérant dans l'UE | ⬜ Oui ⬜ Non | [Type de licence / Pays] |
| Banque ou établissement de crédit UE | ⬜ Oui ⬜ Non | [Licence bancaire] |
| Établissement de paiement ou de monnaie électronique UE | ⬜ Oui ⬜ Non | [Licence de paiement] |
| Entreprise d'investissement UE | ⬜ Oui ⬜ Non | [Licence d'investissement] |
| Prestataire de services sur crypto-actifs UE | ⬜ Oui ⬜ Non | [Licence MiCAR] |
| Entreprise d'assurance ou de réassurance UE | ⬜ Oui ⬜ Non | [Licence d'assurance] |
| Autre entité financière selon l'Article 2 | ⬜ Oui ⬜ Non | [Préciser le type] |
| Prestataire tiers de services TIC critique | ⬜ Oui ⬜ Non ⬜ En attente | [Lettre de désignation] |

**Si UN « Oui » quelconque** : Les exigences DORA sont **Niveau 1 (Conformité obligatoire)** selon POL-00 Section 3.2

**Si TOUS « Non »** : Les exigences DORA restent **Niveau 3 (Référence informative)** selon POL-00

**Évaluation des prestataires de services TIC** :
Si [Organisation] fournit des services TIC à des entités financières de l'UE :

- Surveiller la désignation potentielle comme prestataire tiers de services TIC critique
- Examiner les contrats clients pour les exigences référencées à DORA
- Évaluer si les services constituent des « fonctions critiques ou importantes » selon l'Article 3(31)–(32) de DORA
- La désignation critique déclenche le cadre de surveillance DORA (Articles 31–44)

---

# Aperçu des cinq piliers de DORA

## Structure des piliers

DORA organise les exigences en cinq piliers :

```
┌─────────────────────────────────────────────────────────────────┐
│                  CINQ PILIERS DE DORA                           │
├─────────────────────────────────────────────────────────────────┤
│  CHAPITRE II :  Cadre de gestion des risques TIC                │
│                 Articles 5–16                                    │
│                 - Gouvernance et stratégie                       │
│                 - Identification, protection, détection TIC      │
│                 - Réponse et reprise                             │
│                 - Apprentissage et évolution                     │
│                 - Communication                                  │
├─────────────────────────────────────────────────────────────────┤
│  CHAPITRE III : Gestion et notification des incidents TIC        │
│                 Articles 17–23                                   │
│                 - Détection et classification des incidents      │
│                 - Procédures de réponse aux incidents            │
│                 - Notification aux autorités compétentes         │
├─────────────────────────────────────────────────────────────────┤
│  CHAPITRE IV :  Tests de résilience opérationnelle numérique     │
│                 Articles 24–27                                   │
│                 - Programmes de tests                            │
│                 - Tests avancés (TLPT)                           │
│                 - Principe de proportionnalité                   │
├─────────────────────────────────────────────────────────────────┤
│  CHAPITRE V :   Gestion des risques TIC liés aux tiers          │
│                 Articles 28–44                                   │
│                 - Cadre de gestion des risques tiers             │
│                 - Exigences contractuelles                       │
│                 - Surveillance des prestataires critiques        │
├─────────────────────────────────────────────────────────────────┤
│  CHAPITRE VI :  Arrangements de partage d'informations          │
│                 Article 45                                       │
│                 - Partage de renseignements sur les cybermenaces │
└─────────────────────────────────────────────────────────────────┘
```

## Principe de proportionnalité

DORA applique la proportionnalité (Article 4) :

- Exigences adaptées en fonction de :
  - La taille de l'entité financière
  - La nature, l'étendue et la complexité des activités
  - Le profil de risque global
- **Petites entreprises d'investissement non interconnectées** : Régime simplifié
- **Microentreprises** : Simplifications supplémentaires lorsque justifiées
- **Toutes les entités financières** : Les exigences fondamentales s'appliquent néanmoins

---

# Chapitre II — Cadre de gestion des risques TIC

## Aperçu (Articles 5–16)

Les entités financières doivent établir, maintenir et réviser un cadre de gestion des risques TIC garantissant la résilience, la continuité et la sécurité des systèmes TIC.

**Article 5 : Gouvernance et organisation**

**Exigences** :

- L'organe de direction assume la responsabilité ultime du risque TIC
- Approbation du cadre de gestion des risques TIC
- Attribution de rôles et responsabilités clairs
- Ressources suffisantes pour la gestion des risques TIC
- Lignes de reporting internes vers l'organe de direction

**Rôles clés** :

- Organe de direction (responsabilité au niveau du conseil d'administration)
- Fonction de gestion des risques TIC (responsabilité opérationnelle)
- Fonctions de contrôle (surveillance indépendante)

**Correspondance ISO 27001:2022** :

- Clause 5.1 : Leadership et engagement
- Clause 5.3 : Rôles, responsabilités et autorités organisationnels
- A.5.1 : Politiques de sécurité de l'information
- A.5.2 : Rôles et responsabilités en matière de sécurité de l'information

---

**Article 6 : Cadre de gestion des risques TIC**

**Exigences** :
Cadre complet couvrant :

- **Stratégies, politiques, procédures** : Approche documentée de la gestion des risques TIC
- **Systèmes et outils TIC** : Inventaire et évaluation des risques
- **Politiques de sécurité TIC** : Mesures de protection
- **Politiques de continuité TIC** : Continuité des activités et reprise après sinistre
- **Plans de réponse et de reprise TIC** : Gestion des incidents
- **Tests TIC** : Validation des contrôles
- **Audit TIC** : Assurance indépendante
- **Risque TIC lié aux tiers** : Gestion des fournisseurs

**Correspondance ISO 27001:2022** :

- Clauses 4–10 : Ensemble du cadre SMSI
- A.5.1 : Politiques de sécurité de l'information
- A.5.8 : Sécurité de l'information dans la gestion de projet
- A.5.9 : Inventaire de l'information et des autres actifs associés
- A.8.13 : Sauvegarde de l'information
- A.5.29–5.30 : Continuité des activités

---

**Article 8 : Identification**

**Exigences** :

- Inventaire complet des actifs TIC et des actifs informationnels
- Identification de toutes les sources de risque TIC (internes et externes)
- Méthodologie d'évaluation des risques alignée sur la criticité métier
- Documentation des emplacements de traitement de l'information et des flux de données
- Identification des systèmes TIC anciens et évaluation des risques associés

**Correspondance ISO 27001:2022** :

- A.5.9 : Inventaire de l'information et des autres actifs associés
- A.5.12 : Classification de l'information
- Clause 6.1.2 : Évaluation des risques liés à la sécurité de l'information

**Exigences spécifiques à DORA** :

- **Systèmes anciens** : Identification explicite et contrôles compensatoires
- **Interdépendances** : Cartographie des dépendances entre systèmes
- **Cartographie des données** : Emplacements de traitement et flux transfrontaliers
- **Services critiques** : Classification par impact métier

---

**Article 9 : Protection et prévention**

**Exigences** :
Protection des systèmes TIC par :

- **Politiques, procédures, protocoles** : Niveaux de référence de sécurité
- **Outils de sécurité TIC** : Technologies de détection et de prévention
- **Chiffrement** : Protection des données au repos et en transit
- **Segmentation du réseau** : Isolation des fonctions critiques
- **Contrôle des accès** : Gestion des identités et des accès
- **Sécurité physique** : Protection des centres de données et des infrastructures
- **Gestion des changements** : Modifications contrôlées des systèmes

**Correspondance ISO 27001:2022** :

- A.8.1 : Terminaux des utilisateurs
- A.8.2–8.5 : Contrôle des accès
- A.8.7 : Protection contre les logiciels malveillants
- A.8.9 : Gestion des configurations
- A.8.18 : Utilisation de programmes utilitaires à privilèges
- A.8.19 : Installation de logiciels sur des systèmes en exploitation
- A.8.20 : Sécurité des réseaux
- A.8.21 : Sécurité des services réseau
- A.8.22 : Cloisonnement des réseaux
- A.8.23 : Filtrage Web
- A.8.24 : Utilisation de la cryptographie
- A.7.4 : Surveillance de la sécurité physique

**Accent DORA** :

- La **segmentation du réseau** est explicitement requise (non optionnelle)
- Le **chiffrement** est obligatoire pour les données sensibles
- L'**authentification multi-facteurs (AMF)** est attendue pour l'accès à privilèges
- La **gestion des correctifs et des vulnérabilités** constitue une exigence critique

---

**Article 10 : Détection**

**Exigences** :

- Mécanismes de surveillance continue
- Détection des activités anormales
- Capacités d'alertes en temps réel
- Corrélation des événements de sécurité
- Intégration des renseignements sur les menaces

**Correspondance ISO 27001:2022** :

- A.8.15 : Journalisation
- A.8.16 : Activités de surveillance
- A.5.24–5.25 : Planification de la gestion des incidents
- A.5.7 : Renseignements sur les menaces

**Exemples technologiques** :

- SIEM (Security Information and Event Management)
- EDR (Endpoint Detection and Response)
- Analyse du trafic réseau (NTA)
- Analyse comportementale des utilisateurs et des entités (UEBA)
- Plateformes de renseignements sur les menaces (TIP)

---

**Article 11 : Réponse et reprise**

**Exigences** :

- Plans de réponse aux incidents TIC
- Procédures de gestion de crise
- Plans de communication (internes et externes)
- Plans de continuité des activités (PCA)
- Plans de reprise d'activité (PRA)
- Objectifs de délai de reprise (ODR)
- Objectifs de point de reprise (OPR)

**Correspondance ISO 27001:2022** :

- A.5.24–5.28 : Gestion des incidents (cycle complet)
- A.5.29 : Sécurité de l'information lors d'une perturbation
- A.5.30 : Préparation des TIC à la continuité des activités
- A.8.13 : Sauvegarde de l'information
- A.8.14 : Redondance des installations de traitement de l'information

**Attentes DORA** :

- **ODR pour les fonctions critiques** : Généralement 2–4 heures
- **OPR pour les données critiques** : Quasi-zéro (réplication continue préférée)
- **Communication de crise** : Parties prenantes internes et externes
- **Retours d'expérience** : Revue post-incident obligatoire

---

**Article 12 : Apprentissage et évolution**

**Exigences** :

- Revues post-incident
- Analyse des causes profondes
- Mise en œuvre d'actions correctives
- Intégration des retours d'expérience
- Amélioration continue du cadre de gestion des risques TIC
- Surveillance de l'évolution du paysage des risques TIC

**Correspondance ISO 27001:2022** :

- A.5.27 : Apprentissage tiré des incidents liés à la sécurité de l'information
- Clause 10.1–10.2 : Amélioration continue

---

**Article 13 : Communication**

**Exigences** :

- Canaux de communication pour signaler les problèmes TIC
- Procédures d'escalade vers la direction
- Partage d'informations avec les parties prenantes
- Coordination avec les prestataires tiers de services TIC
- Communication externe lors des incidents

**Correspondance ISO 27001:2022** :

- A.5.5 : Contact avec les autorités
- A.5.6 : Contact avec des groupes d'intérêt spécifiques
- A.6.8 : Signalement des événements liés à la sécurité de l'information

---

**Article 15 : Sensibilisation et formation à la sécurité TIC**

**Exigences** :

- Programmes réguliers de sensibilisation à la sécurité TIC
- Formation spécifique au rôle pour le personnel TIC
- Simulations de hameçonnage et tests
- Mesure de l'efficacité des formations
- Sensibilisation aux menaces d'ingénierie sociale

**Correspondance ISO 27001:2022** :

- A.6.3 : Sensibilisation, éducation et formation à la sécurité de l'information

**Accent DORA** :

- Les programmes de formation doivent être documentés et mesurables
- Formation obligatoire annuelle au minimum
- Formation spécialisée pour les utilisateurs à privilèges
- Les tests de hameçonnage sont considérés comme une pratique standard

---

**Article 16 : Politiques liées aux TIC**

**Exigences** :
Les entités financières doivent établir des politiques TIC couvrant :

- La sécurité TIC
- La continuité TIC
- La gestion des changements TIC
- Les opérations TIC
- La gestion de projets TIC
- La sécurité des réseaux
- Le chiffrement et la gestion des clés

**Révision des politiques** : Annuelle au minimum, ou lors de changements significatifs

**Correspondance ISO 27001:2022** :

- A.5.1 : Politiques de sécurité de l'information
- A.5.36 : Conformité aux politiques, règles et normes pour la sécurité de l'information

---

# Chapitre III — Gestion et notification des incidents TIC

## Aperçu (Articles 17–23)

Les entités financières doivent disposer de processus pour détecter, gérer, notifier et rapporter les incidents TIC.

**Article 17 : Processus de gestion des incidents TIC**

**Exigences** :

- Indicateurs d'alerte précoce
- Procédures de détection des incidents
- Critères de classification des incidents (majeurs vs. non majeurs)
- Procédures de réponse aux incidents et de reprise
- Analyse des causes profondes
- Procédures d'escalade
- Plans de communication

**Classification des incidents** (Article 18) :
Les entités financières doivent classer les incidents en fonction de :

- **Criticité** : Impact sur les opérations métier
- **Durée** : Durée de l'interruption de service
- **Perte de données** : Volume et sensibilité des données affectées
- **Portée géographique** : Nombre de pays/clients affectés
- **Impact réputationnel** : Perception publique et confiance

**Indicateurs d'incident majeur** :

- Perturbation significative des fonctions critiques
- Indisponibilité du service dépassant un seuil (p. ex. 2 heures)
- Violation de données affectant un grand nombre de clients
- Perte financière significative
- Risque systémique potentiel pour la stabilité financière

**Correspondance ISO 27001:2022** :

- A.5.24 : Planification et préparation de la gestion des incidents liés à la sécurité de l'information
- A.5.25 : Évaluation des événements liés à la sécurité de l'information et décisions
- A.5.26 : Réponse aux incidents liés à la sécurité de l'information

---

**Article 19 : Notification initiale et rapports intermédiaires**

**Exigence** : Les entités financières doivent notifier les autorités compétentes des **incidents TIC majeurs** selon des délais définis.

**Calendrier de notification** :

| Phase | Délai | Contenu |
|-------|-------|---------|
| **Notification initiale** | Dès que possible, au plus tard dans les heures spécifiées (généralement 4 heures après la détection) | Description de l'incident, heure de détection, statut, impact préliminaire |
| **Rapport intermédiaire** | Sur demande ou en cas de changement significatif de statut | Évaluation mise à jour, actions prises, réponse en cours |
| **Rapport final** | Après résolution de l'incident (p. ex. dans le mois suivant) | Cause profonde, évaluation de l'impact, remédiation, retours d'expérience |

**Canaux de notification** :

- Portail de l'autorité nationale compétente
- Modèles de notification standardisés (selon les NTR)
- Canaux de communication sécurisés

**Correspondance ISO 27001:2022** :

- A.5.5 : Contact avec les autorités
- A.5.26 : Réponse aux incidents liés à la sécurité de l'information

**Notifications croisées** :
Les exigences de notification DORA peuvent se recouper avec :

- Les notifications de violation de données personnelles du RGPD (Articles 33–34)
- La notification d'incidents NIS2 (si l'entité est également soumise à NIS2)
- Les exigences nationales de notification des incidents

Les entités devraient coordonner les notifications pour éviter les doublons et les incohérences.

---

**Article 20 : Notification centralisée**

Les entités financières notifient un point de contact unique (autorité nationale compétente), qui coordonne avec :

- Les Autorités européennes de surveillance (AES)
- La Banque centrale européenne (BCE) pour l'évaluation du risque systémique
- Le Conseil de résolution unique (CRU) le cas échéant
- D'autres autorités de l'UE selon les besoins

**Objectif** : Assurer une visibilité à l'échelle de l'UE sur les incidents TIC à impact systémique potentiel.

---

**Article 23 : Notification volontaire de cybermenaces significatives**

Les entités financières peuvent notifier volontairement les autorités compétentes de cybermenaces significatives même sans incident réel, afin de soutenir la sensibilisation et la prévention à l'échelle du secteur.

**Exemples** :

- Détection de menace persistante avancée (APT)
- Découverte de vulnérabilité zero-day
- Campagne de rançongiciel ciblant le secteur financier
- Attaques de credential stuffing à grande échelle

---

# Chapitre IV — Tests de résilience opérationnelle numérique

## Aperçu (Articles 24–27)

Les entités financières doivent établir, maintenir et réviser un programme solide de tests de résilience opérationnelle numérique.

**Article 24 : Exigences générales en matière de tests**

**Composantes du programme de tests** :

- Éventail d'évaluations et de tests appropriés aux risques TIC de l'entité
- Évaluations et analyses des vulnérabilités
- Analyse des sources ouvertes
- Évaluations de la sécurité des réseaux
- Analyses des écarts
- Revues de sécurité physique
- Tests basés sur des scénarios
- Tests de compatibilité
- Tests de performance
- Tests de bout en bout

**Fréquence des tests** :

- Tests de base : Au moins annuellement
- Systèmes critiques : Tests plus fréquents
- Après des changements significatifs : Tests déclenchés

**Correspondance ISO 27001:2022** :

- A.5.30 : Préparation des TIC à la continuité des activités (exigence de tests)
- A.8.8 : Gestion des vulnérabilités techniques
- A.8.34 : Protection des systèmes d'information lors des tests d'audit

---

**Article 25 : Tests des outils, systèmes et processus TIC**

Les entités financières doivent mettre en œuvre des méthodologies de tests comprenant :

**1. Évaluations des vulnérabilités** :

- Identification des faiblesses dans les systèmes
- Outils d'analyse automatisés
- Revue manuelle le cas échéant
- Notation des risques basée sur la gravité

**2. Tests basés sur des scénarios** :

- Tests de continuité des activités et de reprise après sinistre
- Exercices de gestion de crise
- Validation du basculement et de la redondance
- Validation du plan de communication

**3. Tests de compatibilité** :

- Tests d'intégration de nouveaux systèmes
- Tests de mise à niveau et de migration
- Compatibilité multiplateforme

**4. Tests de performance** :

- Tests de capacité et de charge
- Tests de résistance dans des conditions défavorables
- Validation de la scalabilité

**Documentation** :

- Plans et procédures de tests
- Résultats et constatations des tests
- Plans de remédiation et délais
- Validation de la remédiation

---

**Article 26 : Tests avancés des outils, systèmes et processus TIC (TLPT)**

**Tests de pénétration guidés par la menace (TLPT)** :
Les entités financières sélectionnées doivent réaliser des tests avancés basés sur les **Tests de pénétration guidés par la menace** au moins tous les **3 ans**.

**Applicabilité du TLPT** :

- Désignées par les autorités compétentes
- Généralement les grandes entités financières interconnectées
- Institutions à fort impact pour la stabilité financière
- Critères : taille, importance systémique, interconnexion

**Exigences TLPT** (selon l'Article 26 et les NTR) :

**Renseignements sur les menaces** :

- Scénarios de menaces réels
- Simulation de menace persistante avancée (APT)
- Basé sur TIBER-EU ou cadres équivalents

**Tests de l'équipe rouge** :

- Attaques simulées sur les fonctions critiques
- Vecteurs d'attaque physiques et numériques
- Éléments d'ingénierie sociale
- Test des capacités de détection et de réponse

**Tests des contrôles** :

- Exercices d'équipe violette (collaboration équipe rouge + équipe bleue)
- Test de la surveillance, de la détection et de la réponse
- Validation des procédures de réponse aux incidents
- Test de la communication et de l'escalade

**Clôture et remédiation** :

- Rapport détaillé des constatations
- Plan de remédiation avec délais
- Rapport à la direction et au conseil d'administration
- Notification à l'autorité de surveillance

**Correspondance ISO 27001:2022** :

- Pas de correspondance directe avec ISO 27001 (le TLPT est une exigence avancée spécifique à DORA)
- Lié à : A.8.34 (tests d'audit), A.5.7 (renseignements sur les menaces)

**Références de cadres TLPT** :

- **TIBER-EU** : Cadre européen de test éthique par l'équipe rouge basé sur les renseignements sur les menaces
- **CBEST** (Royaume-Uni), **TIBER-NL** (Pays-Bas), **iCAST** (Irlande) : Cadres nationaux

---

**Article 27 : Exigences relatives aux testeurs pour le TLPT**

Le TLPT doit être réalisé par :

- Des testeurs externes indépendants
- Des testeurs internes avec des garanties d'indépendance
- Les autorités compétentes peuvent établir un groupe de testeurs agréés

**Qualifications des testeurs** :

- Expertise technique en renseignements sur les menaces et tests d'intrusion
- Compréhension des opérations du secteur financier
- Exigences de certification (p. ex. CREST, OSCP, OSCE ou équivalent)
- Accords de non-divulgation et de confidentialité

---

# Chapitre V — Gestion des risques TIC liés aux tiers

## Aperçu (Articles 28–44)

Les entités financières doivent gérer les risques TIC liés aux tiers via un cadre complet et une surveillance appropriée.

**Article 28 : Principes généraux**

**Cadre de gestion des risques liés aux tiers** :

- Stratégie, politiques et procédures
- Tenue d'un registre des prestataires tiers de services TIC
- Diligence raisonnable avant contrat
- Arrangements contractuels
- Surveillance et contrôle continus
- Stratégies de sortie

**Correspondance ISO 27001:2022** :

- A.5.19 : Sécurité de l'information dans les relations avec les fournisseurs
- A.5.20 : Prise en compte de la sécurité de l'information dans les accords avec les fournisseurs
- A.5.21 : Gestion de la sécurité de l'information dans la chaîne d'approvisionnement TIC
- A.5.22 : Surveillance, révision et gestion des changements des services fournisseurs
- A.5.23 : Sécurité de l'information pour l'utilisation des services cloud

---

**Article 29 : Évaluation préliminaire du risque de concentration TIC**

Les entités financières doivent :

- Identifier le risque de concentration auprès des prestataires tiers de services TIC
- Évaluer les points uniques de défaillance potentiels
- Envisager des prestataires alternatifs ou des stratégies d'atténuation
- Signaler les risques de concentration significatifs à l'autorité compétente

**Facteurs de risque de concentration** :

- Utilisation du même prestataire pour plusieurs fonctions critiques
- Prestataires alternatifs disponibles en nombre limité
- Concentration géographique (région/pays unique)
- Chaînes de dépendances (le prestataire dépend d'un sous-traitant)

**Spécificité DORA** :
Il s'agit d'une exigence explicite généralement non détaillée dans ISO 27001.

---

**Article 30 : Dispositions contractuelles clés**

**Éléments obligatoires du contrat** pour les services TIC soutenant des fonctions critiques ou importantes :

**1. Descriptions des services** :

- Définition claire des services fournis
- Accords de niveau de service (SLA)
- Emplacements du traitement des données
- Support aux obligations de conformité de l'entité financière

**2. Exigences de sécurité** :

- Mesures de protection des données et de confidentialité
- Délais de notification des incidents de sécurité
- Restrictions et approbations de sous-traitance
- Procédures de retour et de suppression des données

**3. Droits d'accès et d'audit** :

- Droit d'audit de l'entité financière
- Droit d'accès et d'audit de l'autorité compétente
- Droits d'inspection sur site
- Accès à l'information à des fins de surveillance

**4. Résiliation et sortie** :

- Stratégies de sortie avec période de transition suffisante
- Support à la portabilité et à la migration des données
- Continuité du service pendant la transition
- Retour ou suppression des données

**5. Juridiction et résolution des litiges** :

- Droit applicable (droit d'un État membre de l'UE)
- Mécanismes de résolution des litiges
- Obligations de coopération réglementaire

**Correspondance ISO 27001:2022** :

- A.5.20 : Prise en compte de la sécurité de l'information dans les accords avec les fournisseurs
- A.5.23 : Sécurité de l'information pour l'utilisation des services cloud (stratégies de sortie)

**Amélioration DORA** :
DORA fournit des exigences contractuelles beaucoup plus prescriptives qu'ISO 27001, notamment en ce qui concerne :

- Les droits d'accès et d'audit pour les autorités
- Les stratégies de sortie obligatoires
- La gouvernance de la sous-traitance
- La localisation et la portabilité des données

---

**Article 31 : Registre des prestataires tiers de services TIC**

Les entités financières doivent tenir et mettre à jour un registre de tous les prestataires tiers de services TIC, incluant :

- Identification du prestataire
- Services fournis
- Classification de la criticité (critique, important, non critique)
- Dates des contrats et renouvellements
- Pays d'établissement et emplacements de traitement des données
- Sous-traitants utilisés

**Notification** : Soumission annuelle à l'autorité compétente (ou plus fréquemment sur demande)

**Correspondance ISO 27001:2022** :

- A.5.19 (exige un registre des fournisseurs, bien que moins prescriptif que DORA)

---

**Articles 32–44 : Cadre de surveillance des prestataires tiers de services TIC critiques**

**Désignation de prestataire critique** :
Les Autorités européennes de surveillance (AES) peuvent désigner des prestataires tiers de services TIC comme « critiques » en fonction de :

- L'impact systémique sur la stabilité financière
- Le nombre et la nature des entités financières desservies
- La complexité et la criticité des services
- La substituabilité et le risque de concentration

**Processus de désignation** (Article 33) :

- Recommandation de l'AES aux entités financières clientes
- Évaluation des critères (facteurs de l'Article 31(1))
- Le prestataire TIC a la possibilité de fournir des informations
- Désignation d'une Autorité de surveillance principale (ASP)

**Activités de surveillance** (Articles 35–40) :

- Enquêtes générales et inspections sur site
- Demandes d'information et de documentation
- Recommandations de remédiation
- Pénalités en cas de non-conformité

**Obligations du prestataire TIC** (Articles 37–41) :

- Coopération avec l'Autorité de surveillance principale
- Fourniture d'informations et de documentation
- Facilitation des inspections
- Mise en œuvre des recommandations

**Unique à DORA** : ISO 27001 n'a pas de cadre réglementaire de surveillance équivalent pour les prestataires de services.

---

# Chapitre VI — Arrangements de partage d'informations

## Article 45 : Partage d'informations

Les entités financières peuvent participer à des arrangements de partage d'informations pour renforcer les renseignements sur les cybermenaces et les capacités défensives.

**Partage d'informations autorisé** :

- Informations et renseignements sur les cybermenaces
- Indicateurs de compromission (IOC)
- Tactiques, techniques et procédures (TTP)
- Vulnérabilités et avis de sécurité
- Bonnes pratiques de sécurité

**Conditions** :

- Participation volontaire
- Protection de la confidentialité et des informations sensibles
- Conformité au droit de la protection des données (RGPD)
- Aucun échange d'informations concurrentiellement sensibles
- Aucune restriction aux obligations de notification aux autorités

**Correspondance ISO 27001:2022** :

- A.5.7 : Renseignements sur les menaces

**Plateformes de partage d'informations** :

- Financial Services Information Sharing and Analysis Center (FS-ISAC)
- European Financial ISAC (EU FS-ISAC)
- CERT et CSIRT nationaux
- Groupes de partage sectoriels spécifiques

---

# Mise en correspondance ISO 27001:2022 — DORA

## Matrice de correspondance des contrôles

| Exigence DORA | Article DORA | Contrôle ISO 27001:2022 | Analyse des écarts |
|---------------|-------------|-------------------------|---------------------|
| Gouvernance des risques TIC | Art. 5 | Clause 5.1, 5.3, A.5.1, A.5.2 | DORA : Responsabilité explicite de l'organe de direction |
| Cadre de risque TIC | Art. 6 | Clause 4–10 (ensemble du SMSI) | DORA : Éléments du cadre plus prescriptifs |
| Identification des actifs | Art. 8 | A.5.9, A.5.12 | DORA : Systèmes anciens explicites, cartographie des données requise |
| Protection et prévention | Art. 9 | A.8.1–8.24, A.7.4 | DORA : Segmentation du réseau obligatoire |
| Détection | Art. 10 | A.8.15, A.8.16, A.5.7 | DORA : Surveillance en temps réel attendue |
| Réponse et reprise | Art. 11 | A.5.24–5.30, A.8.13–8.14 | DORA : ODR/OPR pour les fonctions critiques |
| Apprentissage et évolution | Art. 12 | A.5.27, Clause 10 | Aligné |
| Sensibilisation et formation | Art. 15 | A.6.3 | DORA : Programmes de formation mesurables |
| Classification des incidents | Art. 18 | A.5.25 | DORA : Critères de classification spécifiques (incident majeur) |
| Notification des incidents | Art. 19–20 | A.5.5, A.5.26 | **Spécifique DORA** : Délais de notification réglementaire |
| Programme de tests | Art. 24–25 | A.5.30, A.8.8 | DORA : Exigences de tests plus complètes |
| TLPT | Art. 26–27 | Pas d'équivalent | **Unique DORA** : Tests de pénétration guidés par la menace |
| Registre des tiers | Art. 31 | A.5.19 | DORA : Registre et notification prescriptifs |
| Contrats tiers | Art. 30 | A.5.20, A.5.23 | **Spécifique DORA** : Dispositions contractuelles obligatoires |
| Risque de concentration | Art. 29 | Pas de correspondance directe | **Unique DORA** : Évaluation et notification explicites du risque de concentration |
| Surveillance des prestataires critiques | Art. 32–44 | Pas d'équivalent | **Unique DORA** : Cadre réglementaire de surveillance |
| Partage d'informations | Art. 45 | A.5.7 | Aligné |

## Écarts clés entre ISO 27001:2022 et DORA

**Écart 1 : Notification réglementaire des incidents**

- ISO 27001 : Gestion interne des incidents
- DORA : Notification obligatoire aux autorités compétentes avec des délais

**Écart 2 : Tests de pénétration guidés par la menace (TLPT)**

- ISO 27001 : Pas d'équivalent
- DORA : Requis pour les entités financières désignées tous les 3 ans

**Écart 3 : Dispositions contractuelles avec les tiers**

- ISO 27001 : Orientations générales sur les accords avec les fournisseurs
- DORA : Clauses contractuelles obligatoires spécifiques

**Écart 4 : Surveillance des prestataires critiques**

- ISO 27001 : Pas de concept de surveillance réglementaire
- DORA : Cadre de surveillance AES pour les prestataires TIC critiques

**Écart 5 : Risque de concentration**

- ISO 27001 : Traité indirectement via l'évaluation des risques
- DORA : Exigence explicite d'évaluation et de notification

---

# Considérations de mise en œuvre

## Calendrier de conformité DORA

**Si [Organisation] est une entité financière réglementée par DORA** :

**Janvier 2025 (Date d'application)** :

- DORA devient applicable
- Les autorités compétentes peuvent procéder à des évaluations de surveillance

**Calendrier de préparation recommandé** :

**6–12 mois avant (Juil. 2024 – Déc. 2024)** :

- Évaluation des écarts par rapport aux exigences DORA
- Renforcement du cadre de gestion des risques TIC
- Établissement du processus de notification des incidents
- Révision de la gestion des risques liés aux tiers
- Renégociation des contrats avec les prestataires TIC critiques

**0–6 mois après (Jan. 2025 – Juin 2025)** :

- Test de la capacité de notification des incidents
- Lancement du programme de tests de résilience opérationnelle numérique
- Établissement du registre des tiers
- Participation au partage d'informations
- Mise en œuvre des Normes Techniques de Réglementation (NTR) au fur et à mesure de leur adoption

**Continu (Après juin 2025)** :

- Tests annuels et amélioration continue
- Notification trimestrielle des incidents (selon les incidents)
- Soumission annuelle du registre des tiers
- Cycle TLPT tous les 3 ans (si désigné)

## Ressources nécessaires

**Personnel** :

- Fonction de gestion des risques TIC (dédiée)
- Équipe de réponse aux incidents avec capacité 24h/24 7j/7
- Spécialistes en gestion des risques liés aux tiers
- Ressources de tests et d'audit (internes ou externes)
- Fonction de conformité et de notification réglementaire

**Technologie** :

- Capacités SIEM et SOC renforcées
- Outils de tests (scanners de vulnérabilités, plateformes de tests d'intrusion)
- Plateforme de gestion des risques liés aux tiers
- Intégration avec le portail de notification des incidents
- Infrastructure de sauvegarde et de reprise après sinistre

**Support externe** :

- Conseil juridique avec expertise DORA
- Auditeurs externes et testeurs d'intrusion
- Fournisseurs de Services de Sécurité Gérés (MSSP) si nécessaire
- Services de renseignements sur les menaces

## Implications financières

La conformité DORA nécessite généralement :

- Un cadre de gestion des risques TIC renforcé
- Des capacités de tests avancées (TLPT)
- Une surveillance élargie des tiers
- Une infrastructure de notification des incidents
- Des programmes de formation et de sensibilisation

Coût supplémentaire estimé : augmentation de 20 à 35 % par rapport à la conformité ISO 27001 de base pour les entités financières de taille moyenne.

---

# Défis courants et retours d'expérience

## Défis courants en matière de conformité DORA

**Défi 1 : Sous-estimer la complexité de la notification réglementaire**

- Les délais de notification des incidents sont serrés (rapport initial dans les heures qui suivent)
- Les critères de classification nécessitent un jugement et de la cohérence
- L'infrastructure de notification doit être testée avant les incidents

**Défi 2 : Renégociation des contrats avec les tiers**

- Les grands fournisseurs cloud peuvent résister aux clauses contractuelles spécifiques à DORA
- Les délais de négociation peuvent s'étendre sur 6 à 12 mois
- Certains prestataires peuvent ne pas accepter les droits d'audit pour les autorités

**Défi 3 : Préparation au TLPT**

- Les organisations peu habituées aux exercices de l'équipe rouge peuvent avoir des difficultés
- Nécessite des capacités de détection et de réponse matures
- La préparation de l'équipe bleue est critique pour des tests réalistes

**Défi 4 : Évaluation du risque de concentration**

- Difficile de quantifier le risque de concentration
- Prestataires alternatifs limités dans certaines catégories de services
- Les stratégies d'atténuation peuvent être coûteuses (multi-cloud, diversification des fournisseurs)

**Défi 5 : Défis des systèmes anciens**

- Les systèmes plus anciens peuvent manquer de journalisation et de surveillance
- Les correctifs et mises à niveau peuvent être irréalisables
- Des contrôles compensatoires sont requis mais peuvent ne pas atténuer pleinement le risque

## Bonnes pratiques

**Pratique 1** : Prendre contact tôt avec l'autorité compétente pour des orientations
**Pratique 2** : Utiliser ISO 27001 comme base, compléter avec les exigences spécifiques à DORA
**Pratique 3** : Établir un processus de notification des incidents et tester trimestriellement
**Pratique 4** : Prioriser les relations avec les prestataires de services TIC critiques
**Pratique 5** : Réaliser une préparation interne au TLPT même sans désignation formelle
**Pratique 6** : Participer aux arrangements de partage d'informations sectoriels

---

# Références et ressources

## Textes juridiques DORA

**Règlement principal** :

- Règlement (UE) 2022/2554 (DORA) — Journal officiel de l'UE

**Normes Techniques de Réglementation (NTR)** :

- Règlement délégué de la Commission sur la gestion des risques TIC (adoption attendue 2024)
- Règlement délégué de la Commission sur la notification des incidents (adoption attendue 2024)
- Règlement délégué de la Commission sur les tests de résilience opérationnelle numérique (adoption attendue 2024)
- Règlement délégué de la Commission sur la surveillance des risques tiers (adoption attendue 2024)

**Sites web des AES** :

- Autorité bancaire européenne (EBA) : https://www.eba.europa.eu/
- Autorité européenne des marchés financiers (ESMA) : https://www.esma.europa.eu/
- Autorité européenne des assurances et des pensions professionnelles (EIOPA) : https://www.eiopa.europa.eu/

## Normes et cadres connexes

**Normes ISO** :

- ISO/IEC 27001:2022 : Systèmes de Management de la Sécurité de l'Information
- ISO/IEC 27002:2022 : Contrôles de sécurité de l'information
- ISO/IEC 27005:2022 : Gestion des risques liés à la sécurité de l'information
- ISO 22301:2019 : Gestion de la continuité des activités

**Cadres TLPT** :

- **TIBER-EU** : Test éthique par l'équipe rouge basé sur les renseignements sur les menaces (cadre BCE)
- CBEST : Cadre de tests d'intrusion guidés par la menace au Royaume-Uni
- TIBER-NL : Cadre TLPT des Pays-Bas
- iCAST : Cadre TLPT d'Irlande

**Publications NIST** (référence informative) :

- NIST Cybersecurity Framework (CSF)
- NIST SP 800-53 : Contrôles de sécurité et de confidentialité
- NIST SP 800-61 : Guide de gestion des incidents de sécurité informatique

## Orientations sectorielles

**Secteur financier** :

- FS-ISAC : Financial Services Information Sharing and Analysis Center
- Programme de sécurité client SWIFT (CSP)
- PCI DSS : Norme de sécurité des données de l'industrie des cartes de paiement (le cas échéant)

**Conseil en conformité** :
Les organisations soumises à DORA devraient faire appel à :

- Un conseil juridique avec expertise en réglementation financière de l'UE
- Des auditeurs expérimentés en conformité DORA
- Des consultants en cybersécurité familiers de TIBER-EU et du TLPT

---

# Annexe A : Liste de contrôle d'auto-évaluation de la conformité DORA

## Cadre de gestion des risques TIC (Chapitre II)

| Exigence | Statut | Emplacement de la preuve | Notes |
|----------|--------|--------------------------|-------|
| Approbation par l'organe de direction du cadre de risque TIC | ⬜ Oui ⬜ Non ⬜ Partiel | | |
| Fonction de gestion des risques TIC établie | ⬜ Oui ⬜ Non | | |
| Inventaire complet des actifs TIC | ⬜ Oui ⬜ Non ⬜ Partiel | | |
| Systèmes anciens identifiés et évalués | ⬜ Oui ⬜ Non | | |
| Segmentation du réseau mise en œuvre | ⬜ Oui ⬜ Non ⬜ Partiel | | |
| Chiffrement des données sensibles (repos et transit) | ⬜ Oui ⬜ Non ⬜ Partiel | | |
| Surveillance et détection continues | ⬜ Oui ⬜ Non ⬜ Partiel | | |
| Plans de continuité des activités et de reprise après sinistre | ⬜ Oui ⬜ Non ⬜ Partiel | | |
| ODR/OPR définis pour les fonctions critiques | ⬜ Oui ⬜ Non | | |
| Revues post-incident et retours d'expérience | ⬜ Oui ⬜ Non | | |
| Formation annuelle de sensibilisation à la sécurité TIC | ⬜ Oui ⬜ Non | | |

## Gestion et notification des incidents (Chapitre III)

| Exigence | Statut | Emplacement de la preuve | Notes |
|----------|--------|--------------------------|-------|
| Critères de classification des incidents établis | ⬜ Oui ⬜ Non ⬜ Partiel | | |
| Définition d'un incident majeur documentée | ⬜ Oui ⬜ Non | | |
| Processus de notification des incidents à l'autorité compétente | ⬜ Oui ⬜ Non ⬜ N/A | | |
| Capacité de notification initiale (dans les heures) | ⬜ Oui ⬜ Non | | |
| Test du processus de notification des incidents réalisé | ⬜ Oui ⬜ Non | | |

## Tests de résilience opérationnelle numérique (Chapitre IV)

| Exigence | Statut | Emplacement de la preuve | Notes |
|----------|--------|--------------------------|-------|
| Programme de tests annuel établi | ⬜ Oui ⬜ Non ⬜ Partiel | | |
| Évaluations des vulnérabilités réalisées régulièrement | ⬜ Oui ⬜ Non | | |
| Tests PCA/PRA basés sur des scénarios | ⬜ Oui ⬜ Non | | |
| TLPT réalisé (si désigné) | ⬜ Oui ⬜ Non ⬜ N/A ⬜ En attente | | |
| Résultats des tests documentés et remédiés | ⬜ Oui ⬜ Non ⬜ Partiel | | |

## Gestion des risques liés aux tiers (Chapitre V)

| Exigence | Statut | Emplacement de la preuve | Notes |
|----------|--------|--------------------------|-------|
| Cadre de gestion des risques liés aux tiers | ⬜ Oui ⬜ Non ⬜ Partiel | | |
| Registre des prestataires tiers de services TIC | ⬜ Oui ⬜ Non ⬜ Partiel | | |
| Processus de diligence raisonnable avant contrat | ⬜ Oui ⬜ Non ⬜ Partiel | | |
| Contrats conformes à DORA pour les prestataires critiques | ⬜ Oui ⬜ Non ⬜ Partiel | | |
| Stratégies de sortie pour les services TIC critiques | ⬜ Oui ⬜ Non ⬜ Partiel | | |
| Évaluation du risque de concentration réalisée | ⬜ Oui ⬜ Non | | |
| Soumission annuelle du registre à l'autorité | ⬜ Oui ⬜ Non ⬜ N/A | | |

## Partage d'informations (Chapitre VI)

| Exigence | Statut | Emplacement de la preuve | Notes |
|----------|--------|--------------------------|-------|
| Participation au partage de renseignements sur les menaces | ⬜ Oui ⬜ Non ⬜ Prévu | | |
| Adhésion à FS-ISAC ou similaire | ⬜ Oui ⬜ Non ⬜ Prévu | | |

---

# Annexe B : Modèle de notification d'incident majeur DORA

**Incident TIC majeur DORA — Notification initiale**

**À** : [Autorité nationale compétente — Point de contact unique]
**De** : [Nom de l'entité financière]
**Contact** : [Nom du Responsable de la réponse aux incidents, téléphone, e-mail]
**Date/Heure** : [Format ISO 8601]
**IEJ (Identifiant d'entité juridique / LEI)** : [IEJ]
**Type de notification** : ⬜ Initiale ⬜ Intermédiaire ⬜ Finale

---

**SECTION 1 : RÉSUMÉ DE L'INCIDENT**

**Identifiant de l'incident** : [Numéro de référence interne]
**Date/Heure de détection** : [ISO 8601]
**Date/Heure de début de l'incident** (estimée) : [ISO 8601]
**Statut actuel** : ⬜ En cours ⬜ Contenu ⬜ Résolu

**Type d'incident** :
⬜ Cyberattaque (préciser : rançongiciel, DDoS, logiciel malveillant, hameçonnage, etc.)
⬜ Défaillance de système (préciser : matériel, logiciel, réseau)
⬜ Violation de données / Perte de données
⬜ Panne du prestataire tiers
⬜ Impact de catastrophe naturelle
⬜ Autre (préciser) : _____________

---

**SECTION 2 : ÉVALUATION DE L'IMPACT**

**Fonctions critiques ou importantes affectées** :

- [Fonction 1] : [Description de l'impact]
- [Fonction 2] : [Description de l'impact]

**Perturbation du service** :

- **Durée** : [Heures/minutes de perturbation]
- **Clients affectés** : [Nombre et type]
- **Portée géographique** : [Pays affectés]
- **Indisponibilité du service** : [Quels services sont en panne]

**Impact sur les données** :
⬜ Aucune donnée affectée
⬜ Données potentiellement compromises : [Type, volume, sensibilité]
⬜ Données confirmées compromises : [Détails]

**Impact financier** (préliminaire) :
⬜ Pas encore déterminé
⬜ Estimé : [Montant et base de calcul]

**Impact réputationnel** :
⬜ Faible ⬜ Moyen ⬜ Élevé
[Brève description]

---

**SECTION 3 : CAUSE PROFONDE** (préliminaire)

[Brève description de la cause profonde suspectée ou confirmée]

---

**SECTION 4 : ACTIONS DE RÉPONSE**

**Actions prises** :
1. [Action 1 — horodatage]
2. [Action 2 — horodatage]
3. [Action 3 — horodatage]

**Statut actuel de la réponse** :
[Brève description de la réponse en cours]

**Actions en cours** :

- [Action avec achèvement prévu]

---

**SECTION 5 : COORDINATION EXTERNE**

**Prestataires tiers impliqués** :

- [Prestataire 1] : [Implication]
- [Prestataire 2] : [Implication]

**Notifications externes** :

- **Clients** : ⬜ Oui ⬜ Non ⬜ Prévu [Date/heure]
- **Autorité de protection des données (RGPD)** : ⬜ Oui ⬜ Non ⬜ N/A
- **Autres autorités** : [Préciser]

---

**SECTION 6 : PROCHAINE MISE À JOUR**

**Prochain rapport attendu** : [Date/heure]
**Type de rapport** : ⬜ Intermédiaire ⬜ Final

---

**DÉCLARATION**

Je confirme que les informations fournies dans cette notification sont exactes au meilleur de ma connaissance à la date du [Date/Heure].

**Nom** : [Représentant de la direction]
**Titre** : [Titre]
**Signature** : [Signature numérique le cas échéant]

---

**FIN DE LA RÉFÉRENCE TECHNIQUE**

---

*Cette référence technique soutient les exigences potentielles de conformité DORA telles que déterminées dans ISMS-POL-00. Toutes les déterminations d'applicabilité réglementaire et les exigences contraignantes sont définies dans ISMS-POL-00 et les documents de politique SMSI approuvés.*

*Pour les organisations NON soumises à DORA, ce document est fourni à titre de sensibilisation informative uniquement et ne crée PAS d'obligations de conformité.*

<!-- QA_VERIFIED: 2026-03-30 -->
