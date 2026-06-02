<!-- ISMS-CORE:POLICY:CLD-PII-POL-A.5-FR:cloud:POL:a.5 -->
**CLD-PII-POL-A.5 — Minimisation des données**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Sous-traitant de DCP en cloud public — Minimisation des données |
| **Type de document** | Politique |
| **Identifiant du document** | CLD-PII-POL-A.5 |
| **Auteur du document** | RSSI / Responsable Sécurité Cloud |
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
| 1.0 | [Date] | RSSI / Responsable Sécurité Cloud | Politique initiale pour la mise en œuvre d'ISO/IEC 27018:2025 Éd. 3 |

**Cycle de révision** : Annuel (ou lors d'un changement significatif de l'architecture du service)
**Prochaine date de révision** : [Date d'entrée en vigueur + 12 mois]

**Chaîne d'approbation** :
- Principale : RSSI / Responsable Sécurité Cloud
- Secondaire : Délégué à la Protection des Données (DPD)
- Autorité finale : Direction générale

**Documents connexes** :
- PRIV-POL-00 (Cadre d'applicabilité réglementaire en matière de protection des données)
- ISMS-POL-A.5.34 (Protection des données et protection des DCP)
- ISMS-POL-A.8.10 (Suppression des informations)
- CLD-PII-POL-A.4 (Limitation de la collecte)
- CLD-PII-POL-A.6 (Limitation de l'utilisation, de la conservation et de la divulgation)
- CLD-PII-POL-A.11 (Sécurité de l'information — supports portables, chiffrement, élimination)
- ISO/IEC 27018:2025 Annex A, Section A.5 et Contrôle A.5.1
- ISO/IEC 27701:2025 Contrôles A.2.4.2 (sous-traitant — fichiers temporaires) et A.2.4.3 (sous-traitant — retour, transfert ou élimination des DCP)
- RGPD Article 5(1)(c) (minimisation des données) ; Article 5(1)(e) (limitation de la conservation)
- LPD suisse Article 6(2) (proportionnalité)

---

## Résumé exécutif

Cette politique établit les exigences de [Organisation] en tant que sous-traitant de DCP en cloud public en matière de minimisation des données — spécifiquement l'effacement sécurisé des fichiers temporaires contenant des DCP générés lors des opérations de traitement cloud — conformément à ISO/IEC 27018:2025 Annex A, Section A.5 et Contrôle A.5.1.

**Périmètre** : Tous les stockages éphémères, temporaires et de travail créés par les services cloud de [Organisation] lors du traitement des DCP, incluant le cache, la mémoire virtuelle, les fichiers de travail et les journaux.

**Justification des contrôles combinés** : La Section A.5 établit le principe que l'identification complète est inutile lorsque le traitement peut être effectué sur des données anonymisées ou pseudonymisées. Le Contrôle A.5.1 traite le risque spécifique au cloud de persistance des DCP dans le stockage temporaire après la fin du traitement — un risque particulièrement significatif dans les environnements cloud multi-locataires où le stockage peut être réalloué.

---

# Périmètre et applicabilité

## Énoncés des contrôles ISO/IEC 27018:2025

**Section A.5 — Minimisation des données (principe)**

La Section A.5 établit le principe que l'identification complète des personnes concernées doit être évitée lorsque le traitement peut être effectué à l'aide de données anonymisées, pseudonymisées ou agrégées, et que les techniques utilisées doivent être documentées et examinées.

**Contrôle A.5.1 — Effacement sécurisé des fichiers temporaires**

Le Contrôle A.5.1 traite le risque spécifique de persistance des DCP dans le stockage temporaire après la fin du traitement. Il exige que le sous-traitant mette en œuvre l'effacement sécurisé des fichiers temporaires — incluant le cache, la mémoire virtuelle, les fichiers de travail et les journaux — en utilisant des méthodes empêchant la récupération, couvrant à la fois le stockage persistant et éphémère.

## Ce que cette politique ne couvre PAS

- Les périodes de conservation des entrepôts principaux de DCP au repos — traitées dans CLD-PII-POL-A.6
- L'élimination sécurisée des supports de stockage physiques — traitée dans CLD-PII-POL-A.11

## Cadre réglementaire

**Niveau 1 : Conformité obligatoire** (per PRIV-POL-00) :

- **RGPD UE** : Article 5(1)(c) (minimisation des données) ; Article 5(1)(e) (limitation de la conservation — pas plus longtemps que nécessaire) ; Article 32(1)(a) (pseudonymisation et chiffrement comme mesures de sécurité appropriées)
- **LPD suisse** : Article 6(2) (proportionnalité) ; Article 9 (obligations du sous-traitant — mesures techniques appropriées)
- **ISO/IEC 27018:2025** : Contrôles A.5 (principe) et A.5.1

---

# Dispositions de la politique : Principe de minimisation des données (A.5)

## Pseudonymisation et anonymisation

Lorsque la finalité du traitement peut être accomplie sans identification directe des personnes concernées, [Organisation] DOIT mettre en œuvre la pseudonymisation ou l'anonymisation dans le cadre de la conception du service. Plus précisément :

- Les fonctions d'analyse et de rapport DOIVENT utiliser des données pseudonymisées ou agrégées lorsque cela est techniquement faisable
- Les systèmes de journalisation et de télémétrie DOIVENT minimiser la capture de DCP au minimum opérationnellement nécessaire
- Les environnements de test et de développement DOIVENT utiliser des données synthétiques ou des jeux de données anonymisés dans la mesure du possible

Les techniques d'anonymisation appliquées aux DCP du responsable du traitement DOIVENT être documentées et soumises à la revue du DPD avant mise en œuvre pour confirmer que le résultat est véritablement et irréversiblement anonymisé. L'évaluation du DPD DOIT être conduite conformément aux orientations applicables des autorités de contrôle (y compris l'Avis 05/2014 du CEPD sur les techniques d'anonymisation, ou son successeur).

---

# Dispositions de la politique : Effacement sécurisé des fichiers temporaires (A.5.1)

## Types de fichiers temporaires dans le périmètre

Les services cloud de [Organisation] génèrent les catégories de stockage temporaire suivantes pouvant contenir des DCP et soumises à cette politique :

- **Fichiers cache** : Données stockées temporairement par les couches applicatives lors du traitement actif
- **Fichiers d'échange / fichiers de pagination** : Débordement de mémoire du système d'exploitation stocké sur disque
- **Fichiers de travail / espace de travail temporaire** : Fichiers de traitement intermédiaires créés lors d'opérations par lots ou en flux
- **Fichiers journaux d'application** : Journaux de service générés lors du traitement pouvant capturer des DCP dans les charges utiles, les traces d'erreurs ou les sorties de débogage
- **Stockage de calcul éphémère** : Stockage en blocs attaché aux instances de calcul lors de l'exécution des tâches

## Exigence d'effacement

[Organisation] DOIT mettre en œuvre l'effacement sécurisé de toutes les catégories de stockage temporaire listées ci-dessus une fois que l'opération de traitement pour laquelle elles ont été créées est terminée. L'effacement DOIT être effectué en utilisant des méthodes empêchant la récupération des données, conformément à NIST SP 800-88 (Guidelines for Media Sanitization) ou équivalent, incluant :

- L'effacement cryptographique (suppression de clé de chiffrement pour les volumes chiffrés) — uniquement efficace lorsque les données ont été chiffrées avec une clé dédiée non répliquée ou sauvegardée en dehors du périmètre de suppression
- L'écrasement multipassage pour le stockage persistant lorsque l'effacement cryptographique n'est pas applicable
- La mise à zéro sécurisée de la mémoire pour les DCP en mémoire après utilisation

Le mécanisme d'effacement DOIT être automatisé dans le pipeline de service chaque fois que cela est techniquement faisable afin d'éliminer le recours à des procédures manuelles.

## Minimisation des journaux

Les journaux d'application et d'infrastructure capturant des DCP DOIVENT être soumis à :

- **Capture minimale** : Les configurations de journaux DOIVENT être examinées pour s'assurer que les DCP dans les charges utiles, les en-têtes ou les paramètres sont masquées ou exclues sauf si opérationnellement essentielles
- **Limites de conservation** : Les journaux contenant des DCP DOIVENT être conservés pendant la période opérationnelle requise, et en tout état de cause pas plus de 30 jours sauf justification opérationnelle documentée — ou le maximum défini dans les accords de service avec le responsable du traitement des DCP si celui-ci est plus court
- **Suppression automatisée** : Les politiques de conservation des journaux DOIVENT être mises en œuvre comme règles de suppression automatisées, et non comme processus manuels

## Isolation du stockage multi-locataires

Dans les environnements multi-locataires, [Organisation] DOIT veiller à ce que le stockage temporaire alloué au traitement d'un responsable du traitement des DCP soit :

- Isolé des autres locataires pendant le traitement actif
- Effacé de manière sécurisée avant réallocation à tout autre locataire ou charge de travail
- Auditable — les événements de réallocation DOIVENT être journalisés et disponibles pour inspection

Cette question est traitée en détail dans CLD-PII-POL-A.11 (§11.13 — Accès aux données sur l'espace de stockage préalablement utilisé). Des tests d'isolation multi-locataires DOIVENT être effectués au minimum annuellement et après tout changement matériel à l'infrastructure de stockage.

## Couverture des procédures

Les procédures d'effacement des fichiers temporaires DOIVENT couvrir explicitement :

- Le stockage persistant (SSD, HDD, NVMe) et le stockage éphémère (stockage d'instance, éphémère de conteneur)
- Toutes les couches de calcul : bare metal, machine virtuelle, conteneur, fonction serverless (les considérations d'effacement spécifiques au serverless, y compris le stockage /tmp et la mise en cache des couches, sont traitées dans les procédures d'effacement au niveau des services)
- Toutes les régions géographiques dans lesquelles [Organisation] exploite une infrastructure cloud

---

# Rôles et responsabilités

| Rôle | Responsabilités |
|------|----------------|
| **RSSI / Responsable Sécurité Cloud** | Propriétaire des normes d'effacement des fichiers temporaires ; examine la mise en œuvre annuellement ; escalade les lacunes non résolues au DPD et à la Direction générale |
| **Ingénierie Cloud** | Met en œuvre des mécanismes d'effacement automatisés dans les pipelines de service ; veille à ce que les configurations de minimisation des journaux soient appliquées ; teste l'efficacité de l'effacement |
| **Délégué à la Protection des Données (DPD)** | Examine les évaluations d'anonymisation/pseudonymisation ; confirme que les configurations de minimisation des journaux sont adéquates ; conseille sur les obligations de limitation de la conservation |
| **Opérations de sécurité** | Surveille les événements anormaux de rémanence des données ; répond aux incidents où des DCP pourraient avoir persisté dans le stockage temporaire |

---

# Exigences en matière de preuves

| Preuve | Description | Conservation |
|-------|-------------|-------------|
| Procédures d'effacement des fichiers temporaires | Procédures documentées par service et type de stockage, avec méthode d'effacement précisée | En cours + versions précédentes pendant 3 ans |
| Enregistrements de configuration d'effacement automatisé | Enregistrements de configuration technique démontrant la mise en œuvre de l'effacement automatisé | En cours + 3 ans |
| Enregistrements de configuration de minimisation des journaux | Configurations de journaux documentées confirmant la minimisation de la capture de DCP | En cours + versions précédentes pendant 3 ans |
| Enregistrements de tests d'isolation multi-locataires | Résultats des tests périodiques confirmant l'absence de rémanence de données entre locataires | 3 ans |
| Revues d'anonymisation du DPD | Évaluations DPD signées des techniques d'anonymisation appliquées aux DCP du responsable du traitement | Durée d'utilisation + 3 ans |

---

# Considérations d'audit

Les auditeurs vérifiant la conformité à CLD-PII-POL-A.5 doivent s'attendre à trouver :

- Des procédures d'effacement des fichiers temporaires documentées couvrant tous les types de stockage et couches de calcul pertinents
- Des preuves techniques que l'effacement est automatisé dans les pipelines de service plutôt que dépendant d'étapes manuelles
- Des configurations de minimisation des journaux examinées et confirmées comme excluant les DCP inutiles
- Des résultats de tests confirmant que le stockage réalloué entre locataires ne contient aucune DCP résiduelle du traitement du locataire précédent

---

<!-- QA_VERIFIED: 2026-04-04 -->
