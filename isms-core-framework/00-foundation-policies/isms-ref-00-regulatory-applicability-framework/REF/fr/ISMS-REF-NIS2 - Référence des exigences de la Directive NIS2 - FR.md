<!-- ISMS-CORE:REF:ISMS-REF-NIS2-FR-nis2-directive-requirements-reference:framework:REF:nis2 -->
**ISMS-REF-NIS2 — Référence des exigences de la Directive sur la Sécurité des Réseaux et des Systèmes d'Information 2 (NIS2)**
**Exigences de cybersécurité de l'UE pour les entités essentielles et importantes (Référence technique non-SMSI)**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Référence des exigences NIS2 |
| **Type de document** | Interne — Référence technique (Non-SMSI) |
| **Identifiant du document** | ISMS-REF-NIS2 |
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
| 1.0 | [Date] | RSSI / Juridique/Conformité | Référence technique initiale pour les entités de l'UE |

**Cycle de révision** : Annuel (ou lors de mises à jour des lois nationales de transposition)
**Prochaine date de révision** : [Date + 12 mois]
**Approbateurs** : Juridique/Conformité / RSSI (référence technique, aucune approbation SMSI requise)

**Distribution** : Équipe de conformité, RSSI, Conseil juridique (pour les organisations soumises à NIS2)

---

⚠️ **IMPORTANT — DOCUMENT DE SUPPORT TECHNIQUE NON-SMSI**

Ce document est fourni à des fins d'information et de sensibilisation uniquement.

- Ce document ne fait PAS partie du Système de Management de la Sécurité de l'Information (SMSI).
- Ce document ne définit PAS d'exigences obligatoires à moins que [Organisation] ne soit une entité réglementée par NIS2.
- Ce document n'établit PAS d'exigences contraignantes, de délais, de KPI ou de SLA pour les entités non réglementées.
- Ce document n'impose PAS l'adoption des exigences NIS2 aux organisations non soumises à NIS2.
- Ce document ne remplace ni n'étend aucune politique du SMSI.

**Détermination de l'applicabilité** :
Les exigences NIS2 s'appliquent UNIQUEMENT SI [Organisation] :

- Est une entité essentielle ou importante opérant dans l'UE dans les secteurs couverts
- Entre dans les seuils de taille (entreprises moyennes/grandes en général)
- Fournit des services catégorisés sous l'Annexe I (essentielle) ou l'Annexe II (importante) de NIS2
- Opère dans un État membre de l'UE ayant transposé NIS2 en droit national

Pour toutes les autres organisations, ce document sert uniquement de :

- Référence technique pour les exigences NIS2 potentielles
- Contexte pour le développement commercial vers des secteurs réglementés de l'UE
- Sensibilisation aux normes de cybersécurité européennes
- **Ce document ne doit pas être utilisé comme preuve d'audit à moins que [Organisation] ne soit réglementée par NIS2**

L'utilisation de ce document n'implique pas l'applicabilité de NIS2, des obligations de conformité ou un statut réglementaire.

**Déclaration de positionnement critique** :
Ce document fournit intentionnellement des détails réglementaires au-delà de ce qui s'applique à la plupart des organisations. Son objectif est la sensibilisation uniquement pour les organisations susceptibles de devenir soumises à NIS2 lors de l'expansion de leurs opérations, ou qui fournissent des services à des entités réglementées par NIS2. Aucune conclusion d'audit ne doit être tirée de la présence, de l'absence ou du statut de mise en œuvre de toute exigence NIS2 énumérée ici, à moins que [Organisation] ne soit explicitement réglementée par NIS2.

---

# Objet et périmètre du document

## Objet

Ce document fournit une vue d'ensemble technique des exigences de la Directive sur la Sécurité des Réseaux et des Systèmes d'Information 2 (Directive (UE) 2022/2555) pour les entités essentielles et importantes de l'UE. Il vise à soutenir :

- La sensibilisation aux exigences NIS2 pour les secteurs couverts de l'UE
- La compréhension du cadre de gestion des risques de cybersécurité de NIS2
- Le contexte pour les organisations se développant dans des secteurs réglementés par NIS2
- L'évaluation d'une applicabilité future potentielle
- La mise en correspondance des exigences NIS2 avec les contrôles ISO 27001:2022

## Ce que ce document n'est PAS

Ce document ne :

- N'établit PAS d'exigences obligatoires pour les organisations non réglementées par NIS2
- Ne définit PAS les obligations de conformité de [Organisation] (voir POL-00 pour l'applicabilité réglementaire)
- Ne crée PAS de critères d'audit à moins que [Organisation] ne soit réglementée par NIS2
- Ne remplace PAS l'interprétation du conseil juridique ou de conformité
- Ne constitue PAS un avis juridique sur la conformité à NIS2
- Ne couvre PAS toutes les variations nationales de transposition (NIS2 est une Directive nécessitant une mise en œuvre nationale)
- N'établit PAS de procédures de mise en œuvre ou de processus de vérification

## Relation avec le SMSI

Ce document est une **référence technique non contraignante** SAUF si [Organisation] est soumise à NIS2 (telle que déterminée dans ISMS-POL-00 Section 3.3).

**Si [Organisation] EST réglementée par NIS2 :**

- Les exigences NIS2 deviennent Niveau 1 (Conformité obligatoire) selon POL-00
- Ce document fournit des orientations de mise en œuvre
- Les contrôles du SMSI doivent démontrer la conformité NIS2
- La notification des incidents et la coordination avec le CSIRT national sont requises

**Si [Organisation] N'EST PAS réglementée par NIS2 :**

- NIS2 reste Niveau 3 (Référence informative) selon POL-00
- Ce document est fourni à titre de sensibilisation uniquement
- Aucune obligation de conformité NIS2 n'existe
- Les contrôles du SMSI suivent uniquement ISO 27001:2022

## Organisation du contenu

Cette référence organise les exigences NIS2 par :

- Périmètre et applicabilité (entités, secteurs, seuils de taille)
- Mesures de gestion des risques de cybersécurité (Article 21)
- Obligations de notification des incidents (Article 23)
- Sécurité de la chaîne d'approvisionnement (Article 21)
- Cadre de supervision et sanctions
- Mise en correspondance avec les contrôles de l'Annexe A de l'ISO 27001:2022

---

# Aperçu et applicabilité de NIS2

## Qu'est-ce que NIS2 ?

La **Directive (UE) 2022/2555** sur des mesures destinées à assurer un niveau élevé commun de cybersécurité dans l'ensemble de l'Union, remplaçant la Directive NIS originale (2016/1148).

**Dates clés** :

- **Entrée en vigueur** : 16 janvier 2023
- **Délai de transposition** : 17 octobre 2024 (les États membres de l'UE doivent la transposer en droit national)
- **Application** : Varie selon l'État membre (généralement 6 à 12 mois après la publication de la loi nationale)

**Objectif** :

- Renforcer la résilience en matière de cybersécurité dans les secteurs critiques de l'UE
- Harmoniser les exigences de cybersécurité entre les États membres
- Étendre le périmètre par rapport à la Directive NIS originale
- Établir un cadre de notification des incidents
- Introduire des mesures de surveillance et d'application

**Nature juridique** :

- Directive (pas un Règlement), donc les États membres doivent la transposer en droit national
- Des variations nationales peuvent exister dans les détails de mise en œuvre
- Les exigences fondamentales restent cohérentes dans toute l'UE

**Autorités de surveillance** :

- Autorités compétentes nationales (désignées par chaque État membre)
- Équipes de Réponse aux Incidents de Sécurité Informatique (CSIRT)
- Points de Contact Uniques (PCU)

## Périmètre et secteurs couverts

NIS2 établit deux catégories d'entités :

**Entités essentielles** (Annexe I — Impact élevé, exigences plus strictes) :

| Secteur | Sous-secteurs |
|---------|---------------|
| **Énergie** | Électricité, chauffage/refroidissement urbain, pétrole, gaz, hydrogène |
| **Transports** | Transports aérien, ferroviaire, maritime, routier |
| **Banque** | Établissements de crédit |
| **Infrastructures des marchés financiers** | Plates-formes de négociation, contreparties centrales, dépositaires centraux de titres |
| **Santé** | Prestataires de soins de santé, laboratoires de référence de l'UE, fabricants de médicaments critiques |
| **Eau potable** | Fournisseurs et distributeurs d'eau potable |
| **Eaux usées** | Gestion et collecte des eaux usées |
| **Infrastructure numérique** | Points d'échange Internet, fournisseurs de services DNS (à l'exclusion des serveurs de noms racines), registres de noms de domaine de premier niveau, fournisseurs de services d'informatique en nuage, fournisseurs de services de centres de données, réseaux de diffusion de contenu, prestataires de services de confiance, réseaux de communications électroniques publics, services de communications électroniques accessibles au public |
| **Gestion des services TIC** | Fournisseurs de services gérés, fournisseurs de services de sécurité gérés |
| **Administration publique** | Entités de l'administration centrale |
| **Espace** | Opérateurs d'infrastructure au sol soutenant les services spatiaux |

**Entités importantes** (Annexe II — Impact moyen, exigences proportionnées) :

| Secteur | Sous-secteurs |
|---------|---------------|
| **Services postaux et d'expédition** | Prestataires de services postaux et d'expédition |
| **Gestion des déchets** | Collecte, traitement et élimination des déchets |
| **Fabrication, production et distribution de produits chimiques** | Substances et mélanges chimiques |
| **Production, transformation et distribution de denrées alimentaires** | Opérateurs alimentaires (à grande échelle) |
| **Fabrication** | Dispositifs médicaux, produits informatiques/électroniques/optiques, équipements électriques, machines, véhicules automobiles/remorques, autres équipements de transport |
| **Fournisseurs numériques** | Places de marché en ligne, moteurs de recherche en ligne, plateformes de réseaux sociaux |
| **Recherche** | Organisations de recherche |

## Critères de taille et de périmètre

**Seuils de taille** (Article 2) :

| Taille de l'entreprise | Employés | Chiffre d'affaires annuel OU Bilan | Applicabilité NIS2 |
|------------------------|----------|-------------------------------------|-------------------|
| **Grande** | ≥ 250 | > 50 M€ CA OU > 43 M€ bilan | Dans le périmètre (si dans un secteur couvert) |
| **Moyenne** | 50–249 | ≤ 50 M€ CA ET ≤ 43 M€ bilan | Dans le périmètre (si dans un secteur couvert) |
| **Petite** | 10–49 | ≤ 10 M€ CA ET ≤ 10 M€ bilan | Généralement hors périmètre |
| **Micro** | < 10 | ≤ 2 M€ CA ET ≤ 2 M€ bilan | Hors périmètre |

**Exceptions** :

- **Fournisseurs uniques** : Même si petits, peuvent être dans le périmètre s'ils sont le seul fournisseur d'un service essentiel
- **Administration publique** : Les seuils de taille ne s'appliquent pas
- **Infrastructure critique** : Les États membres peuvent inclure des entités supplémentaires

## Détermination de l'applicabilité

**NIS2 s'applique à [Organisation] SI** :

| Critère | Statut | Preuve |
|---------|--------|--------|
| Opère dans un État membre de l'UE | ⬜ Oui ⬜ Non | [Pays] |
| Entre dans un secteur couvert (Annexe I ou II) | ⬜ Oui ⬜ Non | [Secteur] |
| Satisfait aux seuils de taille (moyen ou grand) | ⬜ Oui ⬜ Non | [Employés / Chiffre d'affaires] |
| Désigné par l'autorité nationale | ⬜ Oui ⬜ Non ⬜ Inconnu | [Lettre de désignation si applicable] |
| La loi nationale de transposition NIS2 est en vigueur | ⬜ Oui ⬜ Non ⬜ En attente | [Référence de la loi nationale] |

**Si les critères sont satisfaits** : Les exigences NIS2 sont **Niveau 1 (Conformité obligatoire)** selon POL-00 Section 3.3

**Si les critères ne sont pas satisfaits** : Les exigences NIS2 restent **Niveau 3 (Référence informative)** selon POL-00

**Note sur la transposition nationale** :
Chaque État membre de l'UE met en œuvre NIS2 par voie de législation nationale. Les organisations doivent consulter leur autorité nationale de cybersécurité pour les exigences spécifiques, car les détails de mise en œuvre peuvent varier.

---

# Article 21 — Mesures de gestion des risques de cybersécurité

## Aperçu

L'Article 21 établit des **mesures minimales de gestion des risques de cybersécurité** que les entités essentielles et importantes doivent mettre en œuvre.

**Obligation juridique** (Article 21(1)) :
Les États membres doivent veiller à ce que les entités prennent des mesures techniques, opérationnelles et organisationnelles « appropriées et proportionnées » pour gérer les risques de cybersécurité et minimiser l'impact des incidents.

**Principe de proportionnalité** :
Les mesures doivent être appropriées à :

- La nature et l'étendue des activités de l'entité
- La taille de l'entité
- La probabilité et la gravité des incidents
- L'état de l'art en matière de cybersécurité

## Dix mesures minimales (Article 21(2))

**1. Analyse des risques et politiques de sécurité des systèmes d'information**

**Exigence** :

- Politiques d'analyse des risques et de sécurité des systèmes d'information
- Méthodologie complète d'évaluation des risques
- Révisions et mises à jour régulières des risques
- Documentation des décisions de traitement des risques

**Correspondance ISO 27001:2022** :

- Clause 6.1.2 : Évaluation des risques liés à la sécurité de l'information
- Clause 6.1.3 : Traitement des risques liés à la sécurité de l'information
- A.5.1 : Politiques de sécurité de l'information

**Orientations de mise en œuvre** :

- Évaluation des risques annuelle au minimum
- Approche basée sur les risques alignée sur l'impact métier
- Rapport sur les risques au niveau du conseil d'administration
- Intégration dans la gestion des risques d'entreprise

---

**2. Gestion des incidents**

**Exigence** :

- Politiques et procédures de gestion des incidents
- Détection, classification, réponse et reprise après incident
- Plans de communication (internes et externes)
- Retours d'expérience et amélioration continue

**Correspondance ISO 27001:2022** :

- A.5.24 : Planification et préparation de la gestion des incidents liés à la sécurité de l'information
- A.5.25 : Évaluation des événements liés à la sécurité de l'information et décisions
- A.5.26 : Réponse aux incidents liés à la sécurité de l'information
- A.5.27 : Apprentissage tiré des incidents liés à la sécurité de l'information

**Spécificités NIS2** :

- Notification des incidents aux autorités nationales (Article 23)
- Coordination avec le CSIRT national
- Communication avec les clients et les parties prenantes

---

**3. Continuité des activités et gestion de crise**

**Exigence** :

- Plans de continuité des activités (PCA)
- Plans de reprise d'activité (PRA)
- Procédures de gestion de crise
- Capacités de sauvegarde et de récupération
- Tests et validation

**Correspondance ISO 27001:2022** :

- A.5.29 : Sécurité de l'information lors d'une perturbation
- A.5.30 : Préparation des TIC à la continuité des activités
- A.8.13 : Sauvegarde de l'information
- A.8.14 : Redondance des installations de traitement de l'information

**Accent NIS2** :

- Accent sur la continuité des services essentiels
- Objectifs de délai de reprise (ODR) pour les fonctions critiques
- Tests réguliers (au moins annuellement)

---

**4. Sécurité de la chaîne d'approvisionnement**

**Exigence** :

- Mesures pour sécuriser la chaîne d'approvisionnement
- Évaluation des pratiques de cybersécurité des fournisseurs
- Exigences contractuelles de sécurité
- Surveillance de la posture de sécurité des fournisseurs
- Approche basée sur les risques pour les relations avec les fournisseurs

**Correspondance ISO 27001:2022** :

- A.5.19 : Sécurité de l'information dans les relations avec les fournisseurs
- A.5.20 : Prise en compte de la sécurité de l'information dans les accords avec les fournisseurs
- A.5.21 : Gestion de la sécurité de l'information dans la chaîne d'approvisionnement TIC
- A.5.22 : Surveillance, révision et gestion des changements des services fournisseurs

**Spécificités NIS2** :

- Accent explicite sur les aspects de cybersécurité de la chaîne d'approvisionnement
- Inclut les fournisseurs directs et les dépendances dans la chaîne d'approvisionnement
- Divulgation des vulnérabilités et coordination avec les fournisseurs

---

**5. Sécurité dans l'acquisition, le développement et la maintenance des réseaux et systèmes d'information**

**Exigence** :

- Cycle de développement sécurisé
- Exigences de sécurité dans les achats
- Tests de sécurité avant déploiement
- Procédures de maintenance et de correctifs
- Contrôles de gestion des changements

**Correspondance ISO 27001:2022** :

- A.8.4 : Accès au code source
- A.8.8 : Gestion des vulnérabilités techniques
- A.8.9 : Gestion des configurations
- A.8.25 : Cycle de développement sécurisé
- A.8.26 : Exigences de sécurité des applications
- A.8.27 : Principes d'architecture et d'ingénierie des systèmes sécurisés
- A.8.28 : Codage sécurisé
- A.8.29 : Tests de sécurité dans le développement et l'acceptation
- A.8.30 : Développement externalisé

**Mise en œuvre** :

- Principes de sécurité dès la conception
- Programme de gestion des vulnérabilités
- Gestion des correctifs avec des SLA définis
- Configurations de référence sécurisées

---

**6. Politiques et procédures pour évaluer l'efficacité des mesures de gestion des risques de cybersécurité**

**Exigence** :

- Évaluation régulière de l'efficacité des contrôles de sécurité
- Audits internes
- Métriques et KPI de sécurité
- Surveillance continue et amélioration

**Correspondance ISO 27001:2022** :

- Clause 9.1 : Surveillance, mesure, analyse et évaluation
- Clause 9.2 : Audit interne
- Clause 9.3 : Revue de direction
- Clause 10.1–10.2 : Amélioration continue

**Méthodes d'évaluation** :

- Évaluations de sécurité internes
- Évaluations des vulnérabilités
- Tests d'intrusion
- Audits tiers
- Revues de conformité

---

**7. Pratiques de base d'hygiène cybernétique et formation à la cybersécurité**

**Exigence** :

- Programmes de sensibilisation et de formation des utilisateurs
- Mesures de base d'hygiène cybernétique
- Formation en sécurité spécifique au rôle
- Campagnes régulières de sensibilisation à la sécurité
- Mesure de l'efficacité des formations

**Correspondance ISO 27001:2022** :

- A.6.3 : Sensibilisation, éducation et formation à la sécurité de l'information
- A.6.4 : Processus disciplinaire (responsabilisation)

**Mesures d'hygiène cybernétique** :

- Politiques robustes de mots de passe
- Authentification multi-facteurs (AMF)
- Sensibilisation au hameçonnage et tests
- Orientations sur le télétravail sécurisé
- Sécurité BYOD et des appareils mobiles
- Sécurité de la messagerie et du web

**Exigences de formation** :

- Formation obligatoire annuelle pour tout le personnel
- Formation spécialisée pour le personnel informatique et de sécurité
- Tests de simulation de hameçonnage
- Suivi de la complétion des formations

---

**8. Cryptographie et chiffrement**

**Exigence** :

- Utilisation de la cryptographie pour protéger les données
- Chiffrement des données sensibles au repos et en transit
- Gestion des clés cryptographiques
- Alignement sur les standards de chiffrement actuels

**Correspondance ISO 27001:2022** :

- A.8.24 : Utilisation de la cryptographie

**Standards de mise en œuvre** :

- TLS 1.2 minimum (TLS 1.3 préféré) pour les données en transit
- AES-256 pour les données au repos
- PKI et gestion des certificats
- Aucun recours aux algorithmes obsolètes (DES, 3DES, MD5, SHA-1)
- Modules de Sécurité Matériels (HSM) pour les clés à haute valeur

---

**9. Sécurité des ressources humaines, politiques de contrôle des accès et gestion des actifs**

**Exigences** :

**Sécurité des ressources humaines** :

- Vérifications des antécédents pour les postes sensibles
- Responsabilités de sécurité dans les contrats de travail
- Procédures de départ (révocation des accès)

**Contrôle des accès** :

- Identification et authentification des utilisateurs
- Principe du moindre privilège
- Révisions régulières des accès
- Gestion des accès à privilèges

**Gestion des actifs** :

- Inventaire des actifs informationnels
- Classification et traitement des actifs
- Politiques d'utilisation acceptable
- Procédures d'élimination des actifs

**Correspondance ISO 27001:2022** :

- A.5.9 : Inventaire de l'information et des autres actifs associés
- A.5.10 : Utilisation acceptable de l'information et des autres actifs associés
- A.5.12 : Classification de l'information
- A.5.15 : Contrôle des accès
- A.5.16 : Gestion des identités
- A.5.17 : Informations d'authentification
- A.5.18 : Droits d'accès
- A.6.1 : Sélection des candidats
- A.6.2 : Conditions d'emploi
- A.6.4 : Processus disciplinaire
- A.6.5 : Responsabilités après la cessation ou la modification d'emploi
- A.8.2 : Droits d'accès à privilèges
- A.8.3 : Restriction de l'accès à l'information
- A.8.10 : Suppression de l'information

---

**10. Authentification multi-facteurs, communications vocales/vidéo/texte sécurisées et communication d'urgence**

**Exigences** :

**Authentification multi-facteurs (AMF)** :

- AMF pour l'accès distant
- AMF pour les comptes à privilèges
- AMF pour l'accès aux systèmes/données sensibles
- Authentification basée sur les risques le cas échéant

**Communications sécurisées** :

- Chiffrement pour les communications vocales, vidéo et texte
- Plateformes de collaboration sécurisées
- Chiffrement de bout en bout pour les communications sensibles
- VPN pour l'accès distant

**Systèmes de communication d'urgence** :

- Canaux de communication hors bande pour les incidents
- Listes de contacts d'urgence
- Méthodes de communication alternatives (SMS, téléphone, messagerie sécurisée)
- Procédures de communication de crise

**Correspondance ISO 27001:2022** :

- A.5.14 : Transfert de l'information
- A.8.5 : Authentification sécurisée
- A.8.20 : Sécurité des réseaux
- A.8.23 : Filtrage Web (sécurité des communications)

**Spécificités NIS2** :
Il s'agit de l'une des exigences les plus prescriptives de NIS2, imposant explicitement l'AMF et des communications sécurisées — plus spécifique que les mises en œuvre ISO 27001 typiques.

---

## Responsabilité de l'organe de direction (Article 21(3))

**Responsabilisation de la direction** :
Les États membres doivent veiller à ce que l'organe de direction :

- **Approuve** les mesures de gestion des risques de cybersécurité
- **Supervise** leur mise en œuvre
- Puisse être **tenu responsable** en cas de non-conformité

**Dispositions relatives à la responsabilité** (Article 21(5)) :

- L'organe de direction peut être tenu responsable des infractions
- Les États membres peuvent prévoir une responsabilité directe
- Une formation est requise pour les membres de l'organe de direction

**Correspondance ISO 27001:2022** :

- Clause 5.1 : Leadership et engagement
- Clause 5.2 : Politique
- Clause 9.3 : Revue de direction

**Spécificité NIS2** :
La responsabilité explicite de la direction est propre à NIS2 et n'est pas présente dans ISO 27001.

---

# Article 23 — Notification des incidents

## Aperçu

Les entités doivent notifier au CSIRT national ou à l'autorité compétente les incidents significatifs.

**Obligation juridique** :

- **Sans délai injustifié** : Notification initiale
- **Processus en trois étapes** : Alerte précoce, notification d'incident, rapport final

## Calendrier de notification

| Étape | Délai | Contenu |
|-------|-------|---------|
| **Alerte précoce** | Sans délai injustifié (≤ 24 heures après la prise de connaissance) | Prise de connaissance d'un incident significatif, indication initiale d'un possible impact transfrontalier |
| **Notification d'incident** | Sans délai injustifié (≤ 72 heures après la prise de connaissance) | Évaluation initiale (impact, gravité, indicateurs de compromission), détails techniques préliminaires |
| **Rapport final** | ≤ 1 mois après la notification d'incident | Description détaillée, gravité, impact, cause profonde, mesures d'atténuation appliquées/en cours |
| **Rapports intermédiaires** | À la demande du CSIRT/de l'autorité OU en cas de changement significatif dans la gestion | Statut mis à jour et informations |

## Critères d'incident significatif

Les incidents sont considérés comme **significatifs** si :

- Ils ont causé ou sont susceptibles de causer une perturbation opérationnelle grave
- Ils ont causé ou sont susceptibles de causer des pertes financières considérables
- Ils ont affecté ou sont susceptibles d'affecter d'autres personnes physiques/morales (clients, partenaires)

**Facteurs d'évaluation** (Annexe I de la Directive — Acte d'exécution) :

- Nombre d'utilisateurs/entités affectés
- Durée de l'incident
- Portée géographique
- Gravité de la perturbation des services
- Étendue de l'impact sur les activités économiques et sociétales

## Contenu du rapport

**Alerte précoce** (24 heures) :

- Indication qu'un incident significatif s'est produit
- Si l'incident est suspecté d'être le résultat d'un acte illicite/malveillant
- Si l'incident est susceptible d'avoir un impact transfrontalier

**Notification d'incident** (72 heures) :

- Description de l'incident (type, périmètre, chronologie)
- Indicateurs de compromission (IOC) si disponibles
- Évaluation initiale de la gravité et de l'impact
- Type de menace ou cause profonde (si connu)
- Mesures d'atténuation appliquées

**Rapport final** (1 mois) :

- Description détaillée de l'incident
- Type d'incident et analyse des causes profondes
- Évaluation de la gravité avec justification
- Impact sur la fourniture de services et les clients
- Mesures d'atténuation et de remédiation
- Évaluation de l'impact transfrontalier (le cas échéant)
- Retours d'expérience

## Exemptions de notification

Les entités **peuvent choisir de ne pas notifier** si :

- L'incident est couvert par d'autres notifications sectorielles spécifiques (p. ex. RGPD, DORA pour les entités financières)
- À condition que l'information parvienne au CSIRT ou à l'autorité compétente

**Coordination** :

- Les rapports d'incidents NIS2 peuvent se recouper avec la notification des violations de données personnelles du RGPD
- La notification DORA pour les entités financières peut satisfaire les exigences NIS2
- Les États membres peuvent établir un portail de notification unique

**Correspondance ISO 27001:2022** :

- A.5.26 : Réponse aux incidents liés à la sécurité de l'information (notification interne)
- A.5.5 : Contact avec les autorités (notification externe)

**NIS2 vs. ISO 27001** :
ISO 27001 n'impose pas de délais de notification réglementaire externe — cela est spécifique à NIS2.

---

# Sécurité de la chaîne d'approvisionnement (Article 21(2)(d) et considérants)

## Aperçu

NIS2 exige explicitement que les entités traitent les risques de cybersécurité dans leur chaîne d'approvisionnement.

**Exigence** :

- Mesures de sécurité pour remédier aux vulnérabilités spécifiques à chaque fournisseur direct
- Qualité globale des produits et services
- Pratiques de cybersécurité des fournisseurs

## Évaluation des fournisseurs

**Évaluation avant contrat** :

- Évaluation de la posture de cybersécurité du fournisseur
- Certifications de sécurité (ISO 27001, SOC 2, etc.)
- Historique des incidents et capacités de réponse
- Pratiques de traitement et de protection des données
- Évaluation des risques liés aux sous-traitants

**Surveillance continue** :

- Révisions de sécurité régulières (minimum annuel)
- Surveillance continue le cas échéant
- Exigences de notification des incidents
- Droits d'audit de sécurité
- Performance vis-à-vis des SLA de sécurité

## Exigences contractuelles

Les contrats avec les fournisseurs devraient inclure :

- Obligations et normes de sécurité
- Exigences de notification des incidents
- Droits d'audit et d'évaluation
- Protection des données et confidentialité
- Restrictions de sous-traitance
- Responsabilité et indemnisation
- Droits de résiliation en cas de violations de sécurité

**Correspondance ISO 27001:2022** :

- A.5.19 : Sécurité de l'information dans les relations avec les fournisseurs
- A.5.20 : Prise en compte de la sécurité de l'information dans les accords avec les fournisseurs
- A.5.21 : Gestion de la sécurité de l'information dans la chaîne d'approvisionnement TIC

## Gestion des risques de la chaîne d'approvisionnement

**Approche basée sur les risques** :

- Évaluation de la criticité (impact en cas de défaillance du fournisseur)
- Risque de concentration (dépendances envers un fournisseur unique)
- Risque géographique (localisation des fournisseurs/données)
- Substituabilité (disponibilité d'alternatives)

**Stratégies d'atténuation** :

- Diversification des fournisseurs
- Protections contractuelles
- Arrangements de séquestre pour les logiciels critiques
- Clauses de continuité des activités
- Stratégies de sortie

---

# Cadre de surveillance et d'application

## Autorités nationales compétentes

Chaque État membre désigne :

- **Autorité compétente** : Responsable de la surveillance NIS2
- **CSIRT (Computer Security Incident Response Team)** : Réponse technique aux incidents
- **Point de Contact Unique (PCU)** : Fonction de liaison pour la coopération transfrontalière

**Pouvoirs de surveillance** (Article 32) :

- Inspections sur site et à distance
- Audits de sécurité par des auditeurs qualifiés
- Demandes d'information
- Demandes de preuve de mise en œuvre
- Accès aux données, documents et installations

## Mesures d'application (Article 34)

**Sanctions administratives** :

- Instructions contraignantes
- Avertissements
- Ordres de mise en conformité
- Interdiction temporaire de membres de l'organe de direction
- **Amendes** (voir Section 6.3)
- Divulgation publique de la non-conformité

**Mesures d'urgence** :
En cas de risque grave et immédiat, les autorités peuvent :

- Ordonner la mise en œuvre immédiate de mesures de sécurité
- Restreindre ou interdire l'utilisation de systèmes compromis
- Suspendre temporairement des services

## Sanctions (Article 34)

**Entités essentielles** (Annexe I) :

- Jusqu'à **10 000 000 €** OU
- **2 % du chiffre d'affaires annuel mondial total** (le montant le plus élevé étant retenu)

**Entités importantes** (Annexe II) :

- Jusqu'à **7 000 000 €** OU
- **1,4 % du chiffre d'affaires annuel mondial total** (le montant le plus élevé étant retenu)

**Facteurs pris en compte** :

- Gravité et durée de l'infraction
- Caractère intentionnel ou négligent
- Actions prises pour atténuer les dommages
- Infractions antérieures
- Avantages financiers obtenus ou pertes évitées
- Coopération avec l'autorité

**Responsabilité de la direction** (Article 21(5)) :

- Les États membres peuvent tenir les membres de l'organe de direction personnellement responsables
- Interdiction temporaire d'exercer des fonctions de direction possible

---

# Mise en correspondance ISO 27001:2022 — NIS2

## Matrice de correspondance des contrôles

| Exigence NIS2 | Article NIS2 | Contrôle ISO 27001:2022 | Analyse des écarts |
|---------------|-------------|-------------------------|---------------------|
| Analyse des risques et politiques de sécurité | Art. 21(2)(a) | Clause 6.1.2–6.1.3, A.5.1 | Aligné |
| Gestion des incidents | Art. 21(2)(b) | A.5.24–5.27 | NIS2 : Ajoute la notification externe |
| Continuité des activités et gestion de crise | Art. 21(2)(c) | A.5.29–5.30, A.8.13–8.14 | Aligné |
| Sécurité de la chaîne d'approvisionnement | Art. 21(2)(d) | A.5.19–5.22 | NIS2 : Accent plus explicite |
| Acquisition, développement, maintenance sécurisés | Art. 21(2)(e) | A.8.4, A.8.8–8.9, A.8.25–8.30 | Aligné |
| Évaluation de l'efficacité | Art. 21(2)(f) | Clause 9.1–9.3, 10.1–10.2 | Aligné |
| Hygiène de base et formation | Art. 21(2)(g) | A.6.3 | Aligné |
| Cryptographie et chiffrement | Art. 21(2)(h) | A.8.24 | Aligné |
| Sécurité RH, contrôle d'accès, gestion des actifs | Art. 21(2)(i) | A.5.9–5.18, A.6.1–6.5, A.8.2–8.3 | Aligné |
| AMF et communications sécurisées | Art. 21(2)(j) | A.5.14, A.8.5, A.8.20 | **Spécifique NIS2** : Exigence AMF prescriptive |
| Notification des incidents aux autorités | Art. 23 | A.5.5, A.5.26 | **Spécifique NIS2** : Délais imposés |
| Responsabilité de l'organe de direction | Art. 21(3) | Clause 5.1–5.2 | **Spécifique NIS2** : Responsabilité personnelle |

## Écarts clés entre ISO 27001:2022 et NIS2

**Écart 1 : Notification réglementaire des incidents avec délais**

- ISO 27001 : Gestion interne des incidents, contact optionnel avec les autorités
- NIS2 : Notification obligatoire au CSIRT/à l'autorité nationale dans les 24/72 heures

**Écart 2 : Exigence AMF prescriptive**

- ISO 27001 : Authentification sécurisée (méthode flexible)
- NIS2 : Exigence explicite d'authentification multi-facteurs

**Écart 3 : Responsabilité de la direction**

- ISO 27001 : Aucune disposition de responsabilité légale
- NIS2 : L'organe de direction peut être tenu responsable, y compris des pénalités personnelles

**Écart 4 : Application et sanctions**

- ISO 27001 : Suspension/retrait de la certification
- NIS2 : Sanctions financières significatives (jusqu'à 10 M€ ou 2 % du CA)

## Conformité NIS2 avec une base ISO 27001

**Point clé** :
La certification ISO 27001:2022 fournit une base solide pour la conformité NIS2. Les principaux écarts sont :
1. Processus et délais de notification des incidents
2. Validation de la mise en œuvre de l'AMF
3. Cadre de supervision et de responsabilité de l'organe de direction
4. Enregistrement et surveillance nationaux

Les organisations dotées d'ISO 27001 nécessitent généralement **10 à 20 % d'effort supplémentaire** pour atteindre la conformité NIS2, principalement dans l'infrastructure de notification des incidents et la gouvernance de la direction.

---

# Considérations de mise en œuvre

## Calendrier de conformité NIS2

**Si [Organisation] est une entité réglementée par NIS2** :

**Avant l'application (avant l'entrée en vigueur de la loi nationale)** :

- Confirmer le statut d'applicabilité NIS2
- Évaluation des écarts par rapport aux mesures de l'Article 21
- Établissement du processus de notification des incidents
- Information et approbation de l'organe de direction

**0–6 mois (Période de conformité initiale)** :

- Mettre en œuvre les mesures de cybersécurité obligatoires
- Établir la capacité de notification des incidents
- S'enregistrer auprès de l'autorité nationale compétente (si requis)
- Évaluations de sécurité de la chaîne d'approvisionnement

**6–12 mois (Phase de maturité)** :

- Tests et validation de toutes les mesures
- Mécanismes de supervision de l'organe de direction
- Test du processus de notification des incidents
- Première révision annuelle et évaluation

**Continu** :

- Surveillance et amélioration continues
- Évaluation annuelle de l'efficacité
- Notification des incidents (selon les incidents)
- Revues de direction et rapports au conseil d'administration

## Ressources nécessaires

**Personnel** :

- Fonction de cybersécurité avec des responsabilités définies
- Équipe de réponse aux incidents
- Spécialistes en sécurité de la chaîne d'approvisionnement
- Fonction de conformité et de notification
- Engagement de l'organe de direction (formation et supervision)

**Technologie** :

- Infrastructure AMF (à l'échelle de l'entreprise)
- Outils de détection et de réponse aux incidents (SIEM, EDR)
- Infrastructure de sauvegarde et de reprise après sinistre
- Plateformes de communication chiffrées
- Outils de gestion des vulnérabilités

**Support externe** :

- Conseil juridique avec expertise NIS2 (spécifique à l'État membre)
- Auditeurs externes pour l'évaluation de l'efficacité
- Service de réponse aux incidents (services DFIR)
- Fournisseur de Services de Sécurité Gérés (MSSP) si nécessaire

## Implications financières

La conformité NIS2 nécessite généralement :

- Des contrôles techniques renforcés (AMF, chiffrement, surveillance)
- Une infrastructure de notification des incidents
- Un programme de sécurité de la chaîne d'approvisionnement
- Un cadre de supervision de la direction
- Des programmes de formation et de sensibilisation

Coût supplémentaire estimé : **augmentation de 10 à 25 %** par rapport à la conformité ISO 27001 de base pour les entités de taille moyenne.

**Risque de pénalités** :
Les pénalités de non-conformité peuvent être sévères (7 à 10 M€ ou 1,4 à 2 % du CA), ce qui rend l'investissement en conformité une mesure rentable de réduction des risques.

---

# Défis courants et retours d'expérience

## Défis courants en matière de conformité NIS2

**Défi 1 : Détermination de l'applicabilité**

- La classification des entités (essentielle vs. importante) peut être ambiguë
- Seuils de taille au niveau du groupe vs. de la filiale
- Variations nationales de transposition entre États membres
- Déterminations de fournisseur unique

**Défi 2 : Processus de notification des incidents**

- L'alerte précoce de 24 heures est un délai très serré
- Les critères de classification des incidents nécessitent un jugement
- Coordination avec les notifications existantes (RGPD, sectorielles spécifiques)
- Test du processus de notification avant les incidents réels

**Défi 3 : Engagement de l'organe de direction**

- Les membres du conseil d'administration peuvent manquer d'expertise en cybersécurité
- Les préoccupations relatives à la responsabilité nécessitent un cadre de gouvernance clair
- Formation et sensibilisation pour les cadres non techniques
- Équilibre entre supervision et délégation opérationnelle

**Défi 4 : Complexité de la chaîne d'approvisionnement**

- Grand nombre de fournisseurs à évaluer
- Levier limité auprès des fournisseurs majeurs (p. ex. fournisseurs cloud)
- Difficultés de visibilité sur les sous-traitants
- Équilibre entre sécurité et efficacité opérationnelle

**Défi 5 : Déploiement de l'AMF à grande échelle**

- Les systèmes anciens peuvent ne pas supporter l'AMF
- Défis d'expérience utilisateur et d'adoption
- Coût de l'infrastructure AMF pour tous les utilisateurs
- Exceptions et contrôles compensatoires pour les contraintes techniques

## Bonnes pratiques

**Pratique 1** : Prendre contact tôt avec l'autorité nationale compétente pour des orientations sur l'applicabilité
**Pratique 2** : Utiliser ISO 27001 comme base, compléter avec les exigences spécifiques à NIS2
**Pratique 3** : Établir une infrastructure de notification des incidents et tester trimestriellement
**Pratique 4** : Déployer l'AMF à l'échelle de l'entreprise (pas seulement pour la conformité NIS2)
**Pratique 5** : Intégrer NIS2 dans les programmes existants de GRE et de conformité
**Pratique 6** : Fournir une formation en cybersécurité au niveau du conseil d'administration et des rapports réguliers
**Pratique 7** : Documenter les justifications de proportionnalité pour les décisions basées sur les risques

---

# Références et ressources

## Textes juridiques NIS2

**Directive principale** :

- Directive (UE) 2022/2555 (Directive NIS2) — Journal officiel de l'UE

**Actes d'exécution et lignes directrices** :

- Règlement d'exécution de la Commission sur la notification des incidents (attendu 2024–2025)
- Lignes directrices ENISA sur la mise en œuvre de NIS2
- Lois nationales de transposition (varient selon l'État membre)

**Agences de l'UE** :

- **ENISA** (Agence de l'Union européenne pour la cybersécurité) : https://www.enisa.europa.eu/
- Pages dédiées à NIS2 et support à la mise en œuvre

## Autorités nationales compétentes

Les organisations doivent consulter leur **autorité nationale de cybersécurité** pour :

- Les spécificités de la loi nationale de transposition
- Les exigences d'enregistrement
- Les procédures de notification des incidents
- Les attentes de surveillance

**Exemples d'autorités nationales** :

- **Allemagne** : BSI (Bundesamt für Sicherheit in der Informationstechnik)
- **France** : ANSSI (Agence nationale de la sécurité des systèmes d'information)
- **Pays-Bas** : NCSC (National Cyber Security Centrum)
- **Italie** : ACN (Agenzia per la Cybersicurezza Nazionale)
- **Espagne** : CCN-CERT (Centro Criptológico Nacional)
- **Pologne** : NASK (Naukowa i Akademicka Sieć Komputerowa)

## Normes et cadres connexes

**Normes ISO** :

- ISO/IEC 27001:2022 : Systèmes de Management de la Sécurité de l'Information
- ISO/IEC 27002:2022 : Contrôles de sécurité de l'information
- ISO/IEC 27005:2022 : Gestion des risques liés à la sécurité de l'information
- ISO 22301:2019 : Gestion de la continuité des activités

**Publications NIST** (référence informative) :

- NIST Cybersecurity Framework (CSF)
- NIST SP 800-53 : Contrôles de sécurité et de confidentialité

**Orientations sectorielles** :

- Lignes directrices et meilleures pratiques ENISA NIS2
- Guides de gestion des incidents des CSIRT nationaux
- Orientations sectorielles spécifiques (selon le secteur)

## Ressources de conformité

Les organisations soumises à NIS2 devraient faire appel à :

- Un conseil juridique avec expertise en réglementation cybersécurité de l'UE
- Des auditeurs expérimentés en conformité NIS2
- Des consultants en cybersécurité familiers de la transposition nationale
- L'autorité compétente nationale pour des clarifications

---

# Annexe A : Liste de contrôle d'auto-évaluation de la conformité NIS2

## Détermination de l'applicabilité

| Critère | Statut | Notes |
|---------|--------|-------|
| L'entité opère dans un État membre de l'UE | ⬜ Oui ⬜ Non | [Préciser le/les pays] |
| L'entité entre dans les secteurs Annexe I ou II | ⬜ Oui (Annexe I) ⬜ Oui (Annexe II) ⬜ Non | [Préciser le secteur] |
| L'entité satisfait aux seuils de taille (≥ 50 employés) | ⬜ Oui ⬜ Non | [Employés : ___ / CA : ___] |
| L'entité est désignée par l'autorité nationale | ⬜ Oui ⬜ Non ⬜ Inconnu | |
| La loi nationale de transposition est en vigueur | ⬜ Oui ⬜ Non ⬜ En attente | [Référence de la loi nationale] |

**Applicabilité NIS2 globale** : ⬜ Entité essentielle ⬜ Entité importante ⬜ Non applicable

---

## Article 21(2) — Mesures de gestion des risques de cybersécurité

| Mesure | Statut | Emplacement de la preuve | Notes |
|--------|--------|--------------------------|-------|
| (a) Analyse des risques et politiques de sécurité | ⬜ Oui ⬜ Non ⬜ Partiel | | |
| (b) Procédures de gestion des incidents | ⬜ Oui ⬜ Non ⬜ Partiel | | |
| (c) Continuité des activités et gestion de crise | ⬜ Oui ⬜ Non ⬜ Partiel | | |
| (d) Mesures de sécurité de la chaîne d'approvisionnement | ⬜ Oui ⬜ Non ⬜ Partiel | | |
| (e) Sécurité dans l'acquisition, le développement, la maintenance | ⬜ Oui ⬜ Non ⬜ Partiel | | |
| (f) Procédures d'évaluation de l'efficacité | ⬜ Oui ⬜ Non ⬜ Partiel | | |
| (g) Hygiène cybernétique de base et formation | ⬜ Oui ⬜ Non ⬜ Partiel | | |
| (h) Cryptographie et chiffrement | ⬜ Oui ⬜ Non ⬜ Partiel | | |
| (i) Sécurité RH, contrôle d'accès, gestion des actifs | ⬜ Oui ⬜ Non ⬜ Partiel | | |
| (j) AMF, communications sécurisées, communications d'urgence | ⬜ Oui ⬜ Non ⬜ Partiel | | |

---

## Article 21(3) — Responsabilité de l'organe de direction

| Exigence | Statut | Emplacement de la preuve | Notes |
|----------|--------|--------------------------|-------|
| Approbation par l'organe de direction des mesures de gestion des risques | ⬜ Oui ⬜ Non | | |
| Supervision par l'organe de direction de la mise en œuvre | ⬜ Oui ⬜ Non ⬜ Partiel | | |
| Formation en cybersécurité pour l'organe de direction | ⬜ Oui ⬜ Non ⬜ Prévu | | |
| Rapport régulier en matière de cybersécurité à l'organe de direction | ⬜ Oui ⬜ Non | | |

---

## Article 23 — Notification des incidents

| Exigence | Statut | Emplacement de la preuve | Notes |
|----------|--------|--------------------------|-------|
| Critères de classification des incidents définis | ⬜ Oui ⬜ Non ⬜ Partiel | | |
| Processus de notification des incidents au CSIRT/à l'autorité | ⬜ Oui ⬜ Non | | |
| Capacité d'alerte précoce (24 heures) | ⬜ Oui ⬜ Non | | |
| Capacité de notification d'incident (72 heures) | ⬜ Oui ⬜ Non | | |
| Capacité de rapport final (1 mois) | ⬜ Oui ⬜ Non | | |
| Test du processus de notification des incidents réalisé | ⬜ Oui ⬜ Non ⬜ Prévu | | |
| Contact CSIRT/autorité établi | ⬜ Oui ⬜ Non | | |

---

## Enregistrement et surveillance

| Exigence | Statut | Emplacement de la preuve | Notes |
|----------|--------|--------------------------|-------|
| Enregistré auprès de l'autorité nationale compétente (si requis) | ⬜ Oui ⬜ Non ⬜ N/A | | |
| Point de contact désigné | ⬜ Oui ⬜ Non | | |
| Préparé pour les inspections de surveillance | ⬜ Oui ⬜ Non ⬜ Partiel | | |

---

# Annexe B : Modèle de notification d'incident NIS2

**Notification d'incident significatif NIS2**

**À** : [CSIRT national / Autorité compétente]
**De** : [Nom de l'entité]
**Contact** : [Nom du Responsable de la réponse aux incidents, téléphone, e-mail]
**Date/Heure** : [Format ISO 8601]
**Classification de l'entité** : ⬜ Essentielle (Annexe I) ⬜ Importante (Annexe II)
**Secteur** : [Préciser le secteur selon l'Annexe I ou II]
**Type de notification** : ⬜ Alerte précoce ⬜ Notification d'incident ⬜ Rapport final ⬜ Rapport intermédiaire

---

## SECTION 1 : RÉSUMÉ DE L'INCIDENT

**Identifiant de l'incident** : [Numéro de référence interne]
**Date/Heure de prise de connaissance** : [Quand l'entité en a eu connaissance — ISO 8601]
**Date/Heure de début de l'incident** (estimée) : [ISO 8601]
**Statut actuel** : ⬜ En cours ⬜ Contenu ⬜ Résolu

**Type d'incident** :
⬜ Cyberattaque (préciser : rançongiciel, DDoS, logiciel malveillant, hameçonnage, violation de données, etc.)
⬜ Défaillance de système (préciser : matériel, logiciel, réseau, alimentation électrique)
⬜ Problème de prestataire tiers
⬜ Catastrophe naturelle
⬜ Erreur humaine
⬜ Autre (préciser) : _____________

---

## SECTION 2 : ÉVALUATION DE LA SIGNIFICATIVITÉ

**Pourquoi cet incident est-il significatif ?** (Cochez tout ce qui s'applique) :
⬜ A causé/est susceptible de causer une perturbation opérationnelle grave du service essentiel
⬜ A causé/est susceptible de causer des pertes financières considérables
⬜ A affecté/est susceptible d'affecter d'autres personnes physiques ou morales (clients, partenaires, public)

**Impact sur le service** :

- **Durée de la perturbation** : [Heures/minutes]
- **Nombre d'utilisateurs/clients affectés** : [Estimation]
- **Portée géographique** : [Pays/régions affectés]
- **Services essentiels affectés** : [Liste]

---

## SECTION 3 : IMPACT TRANSFRONTALIER

**Un impact transfrontalier est-il suspecté ?**
⬜ Oui ⬜ Non ⬜ Inconnu

**Si Oui** :

- **Pays affectés** : [Liste]
- **Nature de l'impact transfrontalier** : [Description]

---

## SECTION 4 : ÉVALUATION DE L'ACTE MALVEILLANT

**L'incident est-il suspecté d'être le résultat d'un acte illicite ou malveillant ?**
⬜ Oui ⬜ Non ⬜ Inconnu

**Si Oui** :

- **Type de menace** : [p. ex. rançongiciel, APT, menace interne]
- **Indicateurs de compromission (IOC)** : [Liste si disponible]

---

## SECTION 5 : DÉTAILS TECHNIQUES (Pour la notification d'incident et le rapport final)

**Cause profonde** (si connue) :
[Description]

**Vecteur d'attaque** (le cas échéant) :
⬜ Hameçonnage/Ingénierie sociale
⬜ Exploitation de vulnérabilité
⬜ Force brute / Credential stuffing
⬜ Compromission de la chaîne d'approvisionnement
⬜ Menace interne
⬜ Autre : _____________

**Systèmes affectés** :

- [Système 1] : [Impact]
- [Système 2] : [Impact]

---

## SECTION 6 : ACTIONS DE RÉPONSE

**Mesures d'atténuation prises** :
1. [Action 1 — horodatage]
2. [Action 2 — horodatage]
3. [Action 3 — horodatage]

**Réponse en cours** :
[Description des activités de réponse actuelles]

**Délai de reprise estimé** : [Si connu]

---

## SECTION 7 : ÉVALUATION DE L'IMPACT (Pour le rapport final)

**Impact opérationnel** :

- **Temps d'arrêt du service** : [Nombre total d'heures]
- **Période de service dégradé** : [Heures]
- **Nombre d'utilisateurs affectés** : [Décompte final]

**Impact financier** :
⬜ Non encore quantifié
⬜ Estimé : [Montant et base de calcul]
⬜ Aucun impact financier significatif

**Impact sur les données** :
⬜ Aucune donnée affectée
⬜ Données potentiellement compromises : [Type, volume]
⬜ Données confirmées compromises : [Détails]

**Impact réputationnel** :
⬜ Faible ⬜ Moyen ⬜ Élevé
[Description]

---

## SECTION 8 : RETOURS D'EXPÉRIENCE (Pour le rapport final)

**Résumé de l'analyse des causes profondes** :
[Cause profonde détaillée]

**Facteurs contributifs** :
[Facteurs ayant permis ou aggravé l'incident]

**Actions correctives** :
1. [Action pour prévenir toute récurrence]
2. [Action pour améliorer la détection]
3. [Action pour renforcer la réponse]

**Calendrier de remédiation** : [Dates d'achèvement]

---

## SECTION 9 : COORDINATION EXTERNE

**Autres autorités notifiées** :
⬜ Autorité de protection des données (violation RGPD) : [Date]
⬜ Forces de l'ordre : [Quelle agence, date]
⬜ Autres autorités réglementaires : [Préciser]

**Communication publique** :
⬜ Oui ⬜ Non ⬜ Prévu
[Si oui, décrire le périmètre et le calendrier]

---

## SECTION 10 : PROCHAINES ÉTAPES

**Prochain type de rapport** : ⬜ Intermédiaire ⬜ Final ⬜ Aucun prévu
**Prochain rapport attendu** : [Date/heure le cas échéant]

---

**DÉCLARATION**

Je confirme que les informations fournies dans cette notification sont exactes au meilleur de ma connaissance à la date du [Date/Heure].

**Nom** : [Représentant autorisé]
**Titre** : [Titre]
**Signature** : [Signature numérique le cas échéant]

---

**FIN DE LA RÉFÉRENCE TECHNIQUE**

---

*Cette référence technique soutient les exigences potentielles de conformité NIS2 telles que déterminées dans ISMS-POL-00. Toutes les déterminations d'applicabilité réglementaire et les exigences contraignantes sont définies dans ISMS-POL-00 et les documents de politique SMSI approuvés.*

*Pour les organisations NON soumises à NIS2, ce document est fourni à titre de sensibilisation informative uniquement et ne crée PAS d'obligations de conformité.*

<!-- QA_VERIFIED: 2026-03-30 -->
