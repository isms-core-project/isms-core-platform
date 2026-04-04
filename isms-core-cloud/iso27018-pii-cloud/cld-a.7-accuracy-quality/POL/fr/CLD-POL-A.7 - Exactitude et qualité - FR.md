<!-- ISMS-CORE:POLICY:CLD-POL-A.7-FR:cloud:POL:a.7 -->
**CLD-POL-A.7 — Exactitude et qualité**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Sous-traitant de DCP en cloud public — Exactitude et qualité |
| **Type de document** | Politique |
| **Identifiant du document** | CLD-POL-A.7 |
| **Auteur du document** | RSSI / Délégué à la Protection des Données (DPD) |
| **Propriétaire du document** | Directeur Général (DG) |
| **Approuvé par** | Direction générale |
| **Date de création** | [Date] |
| **Version** | 1.0 |
| **Date de version** | [Date à définir] |
| **Classification** | Interne |
| **Statut** | Brouillon |
| **Version du produit Cloud** | 1.0 |

**Historique des versions** :

| Version | Date | Auteur | Modifications |
|---------|------|--------|---------------|
| 1.0 | [Date] | RSSI / DPD | Politique initiale pour la mise en œuvre d'ISO/IEC 27018:2025 Éd. 3 |

**Cycle de révision** : Annuel (ou lors d'un changement significatif de l'architecture du service)
**Prochaine date de révision** : [Date d'entrée en vigueur + 12 mois]

**Chaîne d'approbation** :
- Principale : RSSI / Responsable Sécurité Cloud
- Secondaire : Délégué à la Protection des Données (DPD)
- Autorité finale : Direction générale

**Documents connexes** :
- PRIV-POL-00 (Cadre d'applicabilité réglementaire en matière de protection des données)
- ISMS-POL-A.5.34 (Protection des données et protection des DCP)
- CLD-POL-A.2 (Consentement et choix — coopération pour les droits des personnes concernées)
- CLD-POL-A.6 (Limitation de l'utilisation, de la conservation et de la divulgation)
- CLD-POL-A.9 (Participation individuelle et accès)
- ISO/IEC 27018:2025 Annex A, Section A.7 (Exactitude et qualité — principe)
- ISO/IEC 27701:2025 Contrôle A.2.3.2 (sous-traitant — conformité aux obligations envers les personnes concernées, incluant le soutien à la rectification)
- RGPD Article 5(1)(d) (principe d'exactitude) ; Article 16 (droit à la rectification) ; Article 28(3)(e)
- LPD suisse Article 6(4) (exactitude et correction) ; Article 9(2)(c)

---

## Résumé exécutif

Cette politique établit les exigences de [Organisation] en tant que sous-traitant de DCP en cloud public en matière d'exactitude et de qualité — spécifiquement l'obligation de maintenir l'intégrité des DCP stockées dans les systèmes cloud, de fournir des mécanismes permettant aux responsables du traitement des DCP de corriger, mettre à jour ou supprimer des DCP inexactes, et d'éviter d'introduire une dégradation de la qualité des données par les opérations de traitement — conformément à ISO/IEC 27018:2025 Annex A, Section A.7.

**Périmètre** : Toutes les DCP stockées ou traitées par [Organisation] pour le compte de responsables du traitement des DCP.

**Note sur le principe** : ISO/IEC 27018:2025 Annex A, Section A.7 est une section de niveau de principe sans sous-contrôles additionnels au-delà du corps principal de la norme. Cette politique met en œuvre le principe comme engagement opérationnel. La responsabilité principale de l'exactitude des DCP incombe au responsable du traitement des DCP ; le rôle de [Organisation] est de préserver et de ne pas dégrader l'exactitude, et de fournir des outils permettant au responsable du traitement de la maintenir.

---

# Périmètre et applicabilité

## ISO/IEC 27018:2025 — Section A.7

**Section A.7 — Exactitude et qualité (principe)**

La Section A.7 établit le principe qu'un sous-traitant de DCP en cloud public doit mettre en œuvre des contrôles pour maintenir l'exactitude et l'exhaustivité des DCP qu'il traite pour le compte des responsables du traitement, fournir des mécanismes permettant au responsable du traitement de corriger ou de mettre à jour des DCP inexactes, et éviter d'introduire une dégradation de la qualité par ses opérations de traitement.

## Ce que cette politique ne couvre PAS

- Vérifier l'exactitude des DCP fournies à [Organisation] par le responsable du traitement des DCP — l'exactitude des données source est la responsabilité du responsable du traitement
- Les normes de qualité des données pour le traitement propre du responsable du traitement — ce sont les obligations du responsable du traitement en vertu de l'Article 5(1)(d) du RGPD

## Cadre réglementaire

**Niveau 1 : Conformité obligatoire** (per PRIV-POL-00) :

- **RGPD UE** : Article 5(1)(d) (exactitude — les DCP doivent être exactes et, si nécessaire, tenues à jour ; les DCP inexactes doivent être effacées ou rectifiées sans délai) ; Article 16 (droit à la rectification — le responsable du traitement doit pouvoir exercer ce droit, nécessitant la coopération du sous-traitant) ; Article 28(3)(e)
- **LPD suisse** : Article 6(4) (exactitude et obligations de correction) ; Article 9(2)(c)
- **ISO/IEC 27018:2025** : Principe Section A.7

---

# Dispositions de la politique : Exactitude et qualité (A.7)

## Préservation de l'intégrité des données

[Organisation] DOIT mettre en œuvre des contrôles techniques garantissant que les DCP stockées dans les systèmes cloud ne sont pas dégradées, corrompues ou altérées par les opérations de traitement, sauf autorisation du responsable du traitement des DCP. Plus précisément :

- Les systèmes de stockage DOIVENT mettre en œuvre des vérifications d'intégrité (ex. sommes de contrôle, hachages cryptographiques) pour les entrepôts de DCP afin de détecter toute modification non autorisée ou accidentelle
- Les opérations de transformation effectuées sur les DCP lors du traitement DOIVENT être réversibles lorsque cela est techniquement faisable ; lorsqu'elles sont irréversibles, l'état original des DCP DOIT être préservé dans un enregistrement séparé ou une sauvegarde avant la transformation
- Les opérations de sauvegarde et de réplication DOIVENT préserver l'exactitude et l'exhaustivité des DCP sans perte de données

## Mécanismes de correction par le responsable du traitement

[Organisation] DOIT fournir aux responsables du traitement des DCP des capacités techniques pour corriger, mettre à jour et supprimer des DCP dans le stockage cloud. Ces mécanismes DOIVENT :

- Permettre la correction au niveau des champs ou la mise à jour complète des enregistrements pour les entrepôts de DCP structurées
- Propager les corrections aux répliques actives et en lecture seule dans les 24 heures, et aux copies de sauvegarde dans les 72 heures suivant l'application de la correction — et en tout état de cause dans le délai requis pour que le responsable du traitement remplisse ses obligations relatives aux droits des personnes concernées
- Générer un enregistrement de confirmation lorsque les corrections sont complètes, incluant les enregistrements modifiés et l'horodatage

## Contrôles de qualité

[Organisation] DOIT mettre en œuvre les contrôles de qualité suivants pour les entrepôts de DCP :

- **Contrôles d'exhaustivité des données** : Identifier et signaler les enregistrements avec des champs obligatoires manquants pouvant indiquer une corruption des données ou un transfert incomplet
- **Contrôles de cohérence des données** : Vérifier la cohérence des DCP dans les entrepôts de données répliqués ou distribués afin de détecter les erreurs de réplication
- **Vérification de l'intégrité des sauvegardes** : Restaurer et vérifier les données DCP de sauvegarde au minimum trimestriellement pour les entrepôts de DCP critiques, afin de confirmer l'intégrité des sauvegardes

Les résultats des contrôles de qualité DOIVENT être journalisés et examinés trimestriellement par l'équipe Cloud Engineering. Un résumé des résultats trimestriels des contrôles de qualité DOIT également être fourni au DPD. Les problèmes matériels de qualité des données — définis comme des problèmes affectant plus de 1 % des enregistrements dans un entrepôt de données, ou tout problème ayant pu affecter une décision relative aux droits des personnes concernées ou ayant causé la divulgation de DCP inexactes à un tiers — DOIVENT être signalés au responsable du traitement des DCP dans les 3 jours ouvrables suivant l'identification. Lorsqu'une défaillance d'intégrité des données est détectée, l'incident DOIT être escaladé conformément à CLD-POL-A.11 (Sécurité de l'information).

## Inexactitude induite par le traitement

Lorsque [Organisation] effectue des opérations de transformation, d'enrichissement ou de traitement de données sur des DCP pour le compte d'un responsable du traitement, [Organisation] DOIT :

- Documenter la logique de transformation et son effet sur l'exactitude des DCP
- Obtenir l'autorisation du responsable du traitement pour toute transformation qui modifie les attributs des DCP et n'est pas déjà couverte par l'accord de service ou la description du traitement documentée
- Alerter le responsable du traitement si une opération de traitement produit des résultats indiquant une possible inexactitude dans les données source

---

# Rôles et responsabilités

| Rôle | Responsabilités |
|------|----------------|
| **RSSI / Responsable Sécurité Cloud** | Propriétaire des contrôles d'intégrité pour les entrepôts de DCP ; veille à ce que les mécanismes de correction soient fonctionnels ; supervise le programme de contrôle de qualité |
| **Ingénierie Cloud** | Met en œuvre les vérifications d'intégrité, les mécanismes de correction et les processus de contrôle de qualité ; enquête sur les problèmes de qualité des données et les résout |
| **Délégué à la Protection des Données (DPD)** | Conseille sur les obligations d'exactitude en vertu du RGPD et de la LPD ; examine la documentation des capacités face aux responsables du traitement ; surveille les escalades d'incidents de qualité des données |
| **Prestation de services cloud** | Communique les problèmes d'exactitude signalés par les responsables du traitement à l'Ingénierie Cloud ; suit la résolution et confirme la completion au responsable du traitement |

---

# Exigences en matière de preuves

| Preuve | Description | Conservation |
|-------|-------------|-------------|
| Enregistrements de configuration des vérifications d'intégrité | Documentation technique des mécanismes de vérification d'intégrité par entrepôt de données | En cours + 3 ans |
| Documentation des mécanismes de correction | Description des outils de correction, mise à jour et suppression des DCP disponibles pour les responsables du traitement par service | En cours + versions précédentes pendant 3 ans |
| Journaux de contrôle de qualité | Résultats trimestriels des contrôles de qualité incluant exhaustivité, cohérence et vérification des sauvegardes | 3 ans |
| Enregistrements d'incidents de qualité des données | Enregistrements des problèmes matériels de qualité des données, notifications aux responsables du traitement et résolution | Durée du contrat + 3 ans |

---

# Considérations d'audit

Les auditeurs vérifiant la conformité à CLD-POL-A.7 doivent s'attendre à trouver :

- Une documentation technique confirmant la mise en œuvre des vérifications d'intégrité pour les entrepôts de DCP
- Des preuves que les responsables du traitement des DCP ont accès à des mécanismes de correction, mise à jour et suppression dans les services cloud
- Des journaux de contrôle de qualité couvrant la période d'audit avec examen documenté
- Tout incident de qualité des données signalé aux responsables du traitement avec preuves de résolution

---

<!-- QA_VERIFIED: 2026-04-04 -->
