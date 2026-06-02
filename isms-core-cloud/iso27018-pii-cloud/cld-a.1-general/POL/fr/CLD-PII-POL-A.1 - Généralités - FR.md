<!-- ISMS-CORE:POLICY:CLD-PII-POL-A.1-FR:cloud:POL:a.1 -->
**CLD-PII-POL-A.1 — Généralités**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Sous-traitant de DCP en cloud public — Applicabilité générale et obligations |
| **Type de document** | Politique |
| **Identifiant du document** | CLD-PII-POL-A.1 |
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

**Cycle de révision** : Annuel (ou lors d'un changement réglementaire ou de modèle de service significatif)
**Prochaine date de révision** : [Date d'entrée en vigueur + 12 mois]

**Chaîne d'approbation** :
- Principale : RSSI / Responsable Sécurité Cloud
- Secondaire : Délégué à la Protection des Données (DPD)
- Autorité finale : Direction générale

**Documents connexes** :
- PRIV-POL-00 (Cadre d'applicabilité réglementaire en matière de protection des données)
- ISMS-POL-A.5.34 (Protection des données et protection des DCP — politique SGSI parente)
- CLD-PII-POL-A.2 (Consentement et choix)
- CLD-PII-POL-A.3 (Légitimité et spécification des finalités)
- CLD-PII-POL-A.10 (Responsabilité)
- CLD-PII-POL-A.11 (Sécurité de l'information)
- CLD-PII-POL-A.12 (Conformité en matière de protection des données)
- ISO/IEC 27018:2025 Annex A, Section A.1 (Généralités)
- ISO/IEC 27701:2025 (Système de management des informations relatives à la protection des données)
- ISO/IEC 27002:2022 (Contrôles de sécurité de l'information)
- RGPD Article 28 (Obligations du sous-traitant)
- LPD suisse Article 9 (Engagements de sous-traitance)

---

## Résumé exécutif

Cette politique établit le périmètre, l'applicabilité et les obligations générales de [Organisation] agissant en tant que **sous-traitant de DCP en cloud public** conformément à ISO/IEC 27018:2025 Annex A, Section A.1.

**Périmètre** : Tous les services cloud fournis par [Organisation] dans le cadre desquels [Organisation] traite des données à caractère personnel (DCP) pour le compte et sous les instructions d'un responsable du traitement des DCP. Cela s'applique quel que soit le modèle de service cloud (IaaS, PaaS, SaaS) ou le modèle de déploiement (public, hybride). Les déploiements hybrides sont dans le périmètre dans la mesure où la composante cloud public implique le traitement de DCP pour le compte d'un responsable du traitement.

**Clarification des rôles** : ISO/IEC 27018:2025 s'applique à [Organisation] en sa qualité de **sous-traitant de DCP** — une entité qui traite des DCP pour le compte et sous l'autorité d'un responsable du traitement des DCP. [Organisation] ne détermine pas les finalités et les moyens d'un tel traitement ; cette responsabilité incombe au responsable du traitement des DCP.

**Note sur les contrôles étendus** : Les contrôles de l'Annex A d'ISO/IEC 27018:2025 sont informatifs. [Organisation] les met en œuvre dans le cadre de sa pratique de protection des données en cloud, indépendamment de leur statut normatif au titre de la norme.

---

# Périmètre et applicabilité

## ISO/IEC 27018:2025 — Section A.1

**Section A.1 — Généralités**

La Section A.1 de l'Annex A d'ISO/IEC 27018:2025 établit l'applicabilité générale du jeu de contrôles, définissant le rôle du sous-traitant de DCP en cloud public et les obligations fondamentales qui sous-tendent tous les contrôles suivants du jeu de contrôles étendu de l'Annex A.

## Applicabilité

Cette politique et la suite de politiques CLD-PII-POL-A.X s'appliquent à :

- Tous les services cloud public de [Organisation] qui traitent des DCP pour le compte de clients (responsables du traitement des DCP)
- Tout le personnel, les systèmes, les processus et les sous-traitants ultérieurs impliqués dans ce traitement des DCP
- Toutes les juridictions dans lesquelles [Organisation] fournit des services cloud où des DCP de personnes concernées sont traitées

## Cadre réglementaire

**Niveau 1 : Conformité obligatoire** (per PRIV-POL-00) :

- **RGPD UE** : Article 28 (obligations du sous-traitant — contrat écrit, traitement sur instruction uniquement, sécurité, sous-traitants ultérieurs, assistance, retour/suppression, droits d'audit) ; Article 32 (sécurité du traitement)
- **LPD suisse** : Article 9 (conditions d'engagement du sous-traitant et obligations de sécurité des données associées)
- **ISO/IEC 27018:2025** : Jeu de contrôles étendu de l'Annex A — mis en œuvre comme engagement organisationnel

---

# Dispositions de la politique : Applicabilité générale (A.1)

## Rôle de sous-traitant de DCP

[Organisation] DOIT agir uniquement en tant que sous-traitant de DCP — en traitant les DCP exclusivement selon les instructions documentées des responsables du traitement des DCP. [Organisation] NE DOIT PAS :

- Déterminer les finalités ou les moyens du traitement des DCP au-delà de la prestation technique du service
- Traiter des DCP pour ses propres finalités commerciales, analytiques ou opérationnelles sans autorisation explicite du responsable du traitement
- Transférer, vendre ou exploiter de quelque manière que ce soit les DCP traitées pour le compte d'un responsable du traitement

## Exigence contractuelle

[Organisation] DOIT traiter des DCP uniquement lorsqu'un contrat écrit avec le responsable du traitement des DCP est en place. Ce contrat DOIT couvrir, au minimum, le périmètre du traitement, les obligations de sécurité, la notification des violations, les dispositions relatives aux sous-traitants ultérieurs, le retour/la suppression des données et les droits d'audit — conformément à CLD-PII-POL-A.11 (§11.11 — Exigences contractuelles).

## Documentation des contrôles

[Organisation] DOIT documenter la manière dont chaque contrôle applicable de l'Annex A d'ISO/IEC 27018:2025 est mis en œuvre dans ses services. Cette documentation DOIT être mise à la disposition des responsables du traitement des DCP sur demande et intégrée dans les accords de service lorsque cela est contractuellement requis.

## Traitement sur instruction

[Organisation] DOIT traiter les DCP uniquement conformément aux instructions documentées et actuelles du responsable du traitement des DCP. Lorsque [Organisation] est légalement tenue par le droit applicable de traiter des DCP au-delà des instructions du responsable du traitement, [Organisation] DOIT informer le responsable du traitement des DCP de cette obligation avant le traitement, à moins qu'il ne lui soit légalement interdit de le faire.

## Gestion des sous-traitants ultérieurs

[Organisation] DOIT engager des sous-traitants ultérieurs uniquement avec le consentement écrit préalable du responsable du traitement des DCP. Tous les sous-traitants ultérieurs DOIVENT être liés par des obligations de protection des données équivalentes. [Organisation] demeure responsable envers le responsable du traitement de la conformité des sous-traitants ultérieurs. Les dispositions relatives aux sous-traitants ultérieurs sont régies en détail par CLD-PII-POL-A.11 (§11.12 — Obligations des sous-traitants ultérieurs).

---

# Rôles et responsabilités

| Rôle | Responsabilités |
|------|----------------|
| **RSSI / Responsable Sécurité Cloud** | Maintient la suite de politiques CLD-PII-POL-A.X ; veille à ce que les contrôles techniques répondent aux exigences de l'Annex A d'ISO 27018:2025 ; rend compte de la conformité du sous-traitant de DCP en cloud |
| **Délégué à la Protection des Données (DPD)** | Conseille sur la conformité réglementaire des activités du sous-traitant ; examine les accords de sous-traitance ; coordonne les questions DCP avec les responsables du traitement |
| **Responsable Juridique/Conformité** | Examine les conditions des accords de sous-traitance ; conseille sur les obligations légales applicables ; évalue les changements réglementaires affectant les obligations du sous-traitant |
| **Prestation de services cloud** | Exploite les services conformément aux instructions documentées des responsables du traitement ; escalade les demandes hors périmètre au RSSI et au DPD |
| **Tout le personnel** | Traite les DCP uniquement comme autorisé ; signale immédiatement les violations suspectées de la politique au RSSI et au DPD |

---

# Exigences en matière de preuves

| Preuve | Description | Conservation |
|-------|-------------|-------------|
| Registre des accords de sous-traitance | Liste de tous les accords actifs avec les responsables du traitement des DCP avec périmètre, statut et date de révision | En cours + 3 ans à compter de la fin du contrat |
| Documentation de mise en œuvre des contrôles | Documentation de la manière dont chaque contrôle CLD-PII-POL-A.X est mis en œuvre par service | Version actuelle + versions précédentes pendant 3 ans à compter de la supersession |
| Registre des sous-traitants ultérieurs | Liste des sous-traitants ultérieurs approuvés avec enregistrements du consentement des responsables du traitement | En cours + 3 ans à compter de la fin de l'engagement |
| Enregistrements des instructions | Enregistrements des instructions de traitement documentées des responsables du traitement et de tout écart | Durée du contrat + 3 ans |

> **Base de conservation** : Les périodes de 3 ans s'alignent sur les délais de prescription applicables en vertu du droit de l'UE et suisse pour les litiges relatifs aux accords de sous-traitance. Des périodes plus longues peuvent s'appliquer lorsque les exigences d'audit réglementaire ou les conditions contractuelles le précisent.

---

# Considérations d'audit

Les auditeurs vérifiant la conformité à CLD-PII-POL-A.1 doivent s'attendre à trouver :

- Un registre des accords de sous-traitance démontrant des contrats écrits avec tous les responsables du traitement des DCP
- Une documentation établissant le lien entre chaque contrôle de l'Annex A d'ISO/IEC 27018:2025 et la mise en œuvre du service
- Un registre des sous-traitants ultérieurs avec des enregistrements du consentement des responsables du traitement pour chaque sous-traitant ultérieur
- Des preuves que le traitement est effectué uniquement conformément aux instructions documentées des responsables du traitement

---

<!-- QA_VERIFIED: 2026-04-04 -->
