<!-- ISMS-CORE:POLICY:CLD-POL-A.9-FR:cloud:POL:a.9 -->
**CLD-POL-A.9 — Participation individuelle et accès**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Sous-traitant de DCP en cloud public — Participation individuelle et accès |
| **Type de document** | Politique |
| **Identifiant du document** | CLD-POL-A.9 |
| **Auteur du document** | Délégué à la Protection des Données (DPD) |
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
| 1.0 | [Date] | DPD | Politique initiale pour la mise en œuvre d'ISO/IEC 27018:2025 Éd. 3 |

**Cycle de révision** : Annuel (ou lors d'un changement significatif des capacités du service)
**Prochaine date de révision** : [Date d'entrée en vigueur + 12 mois]

**Chaîne d'approbation** :
- Principale : Délégué à la Protection des Données (DPD)
- Secondaire : RSSI / Responsable Sécurité Cloud
- Autorité finale : Direction générale

**Documents connexes** :
- PRIV-POL-00 (Cadre d'applicabilité réglementaire en matière de protection des données)
- ISMS-POL-A.5.34 (Protection des données et protection des DCP)
- CLD-POL-A.2 (Consentement et choix — A.2.1 coopération pour les droits)
- CLD-POL-A.7 (Exactitude et qualité — capacité de rectification)
- ISO/IEC 27018:2025 Annex A, Section A.9 (Participation individuelle et accès — principe)
- ISO/IEC 27701:2025 Contrôle A.2.3.2 (sous-traitant — conformité aux obligations envers les personnes concernées, incluant le soutien aux droits)
- RGPD Articles 15–22 (droits des personnes concernées) ; Article 28(3)(e)
- LPD suisse Articles 25–32 (droits des personnes concernées) ; Article 9(2)(c)

---

## Résumé exécutif

Cette politique établit les exigences de [Organisation] en tant que sous-traitant de DCP en cloud public en matière de participation individuelle et d'accès — spécifiquement l'obligation de fournir aux responsables du traitement des DCP des mécanismes techniques et un soutien opérationnel pour permettre la satisfaction des demandes de droits des personnes concernées dans les délais légaux — conformément à ISO/IEC 27018:2025 Annex A, Section A.9.

**Périmètre** : Tous les services cloud fournis par [Organisation] qui stockent ou traitent des DCP pour le compte de responsables du traitement des DCP.

**Clarification des rôles** : [Organisation] ne répond pas directement aux personnes concernées. Les personnes concernées adressent leurs demandes de droits au responsable du traitement des DCP. L'obligation de [Organisation] est de fournir au responsable du traitement les outils et la coopération nécessaires pour satisfaire ces demandes dans les délais. L'obligation de coopération au titre de A.9 est le pendant de A.2.1 à un niveau supérieur.

**Note sur le principe** : ISO/IEC 27018:2025 Annex A, Section A.9 est une section de niveau de principe sans sous-contrôles additionnels au-delà du corps principal de la norme. Le mécanisme opérationnel de coopération pour les droits des personnes concernées est traité dans CLD-POL-A.2.1.

---

# Périmètre et applicabilité

## ISO/IEC 27018:2025 — Section A.9

**Section A.9 — Participation individuelle et accès (principe)**

La Section A.9 établit le principe qu'un sous-traitant de DCP en cloud public doit fournir aux responsables du traitement des DCP des mécanismes pour soutenir la satisfaction des demandes d'accès des personnes concernées et d'autres droits, veiller à ce que ces capacités soient testées et documentées, et aider les responsables du traitement à respecter leurs obligations légales de réponse.

## Ce que cette politique ne couvre PAS

- Les capacités techniques spécifiques pour les droits individuels (export, suppression, limitation, portabilité) — détaillées dans CLD-POL-A.2.1
- Les mécanismes de correction et de mise à jour — traités dans CLD-POL-A.7

## Cadre réglementaire

**Niveau 1 : Conformité obligatoire** (per PRIV-POL-00) :

- **RGPD UE** : Articles 15–22 (droits des personnes concernées : accès, rectification, effacement, limitation, portabilité, opposition, droits relatifs aux décisions automatisées) ; Article 28(3)(e) (le sous-traitant assiste le responsable du traitement pour les obligations relatives aux droits des personnes concernées)
- **LPD suisse** : Articles 25–32 (droits des personnes concernées) ; Article 9(2)(c) (coopération du sous-traitant avec le responsable du traitement sur les demandes de droits)
- **ISO/IEC 27018:2025** : Principe Section A.9

---

# Dispositions de la politique : Participation individuelle et accès (A.9)

## Obligation de soutien du sous-traitant

[Organisation] DOIT fournir aux responsables du traitement des DCP des capacités techniques et des procédures opérationnelles qui permettent aux responsables du traitement de satisfaire aux demandes de droits des personnes concernées en vertu du droit applicable. L'obligation de soutien de [Organisation] couvre les droits suivants :

| Droit | Obligation de soutien de [Organisation] |
|-------|----------------------------------------|
| **Accès (Art. 15 RGPD)** | Fournir la capacité d'exporter toutes les DCP associées à une personne concernée dans un format structuré et lisible |
| **Rectification (Art. 16)** | Fournir la capacité de mettre à jour ou corriger les enregistrements de DCP incluant la propagation vers les répliques |
| **Effacement (Art. 17)** | Fournir la suppression des DCP de tous les stockages actifs dans les 5 jours ouvrables ; purge des copies de sauvegarde et répliquées dans les 15 jours ouvrables |
| **Limitation (Art. 18)** | Isoler les DCP du traitement actif dans le délai d'1 jour ouvrable (« limitation fonctionnelle ») ; propagation complète aux entrepôts de données répliqués dans les 5 jours ouvrables |
| **Portabilité (Art. 20)** | Fournir l'export des DCP dans un format lisible par machine et couramment utilisé (JSON, CSV) |
| **Opposition (Art. 21)** | Fournir la capacité de suspendre ou limiter le traitement d'enregistrements DCP spécifiques sur instruction du responsable du traitement |

## Test des capacités

[Organisation] DOIT tester les capacités de satisfaction des droits des personnes concernées au moins **annuellement** et lors de tout changement matériel de l'architecture du service — incluant les changements à l'infrastructure de stockage des données, à l'architecture de sauvegarde, à la topologie de réplication ou aux interfaces API utilisées pour la satisfaction des droits. Les tests DOIVENT :

- Couvrir chaque droit listé dans le tableau ci-dessus pour chaque catégorie de service
- Vérifier que les opérations d'export, de suppression et de limitation des données se complètent dans le délai de réponse défini
- Confirmer que les suppressions se propagent correctement aux copies de sauvegarde et aux entrepôts de données répliqués
- Être documentés avec les résultats conservés à des fins d'audit

Les lacunes matérielles identifiées lors des tests DOIVENT être suivies comme éléments de remédiation et signalées aux responsables du traitement des DCP affectés si la capacité est réduite en dessous des niveaux de service contractuels.

## Délais de réponse

Les capacités de service de [Organisation] DOIVENT soutenir la satisfaction par le responsable du traitement des réponses aux DSAR dans les délais suivants :

- **Accuser réception** de la demande liée aux DSAR du responsable du traitement : dans le délai d'1 jour ouvrable
- **Compléter** les exports d'accès aux données et les demandes de rectification : dans les 5 jours ouvrables
- **Compléter** les demandes d'effacement (incluant la propagation vers les sauvegardes) : dans les 15 jours ouvrables
- **Compléter** les demandes de limitation : dans le délai d'1 jour ouvrable (fonctionnelle — DCP isolées du traitement actif) ; propagation complète aux entrepôts de données répliqués dans les 5 jours ouvrables

Lorsqu'un accord de service spécifique définit des délais plus courts, ces délais prévalent.

## Documentation pour le responsable du traitement

[Organisation] DOIT fournir aux responsables du traitement des DCP une documentation décrivant les capacités relatives aux droits des personnes concernées disponibles dans chaque service cloud, incluant :

- Comment initier chaque opération de satisfaction des droits via l'interface du service ou l'API
- Les délais de complétion attendus et les mécanismes de confirmation
- Toute limitation sur la satisfaction des droits (ex. délais de suppression des sauvegardes)
- Le chemin d'escalade pour demander l'assistance de [Organisation] lorsque le libre-service est insuffisant

Cette documentation DOIT être maintenue à jour et mise à jour dans les 30 jours suivant tout changement matériel de capacité — incluant les changements à l'infrastructure de stockage des données, à l'architecture de sauvegarde, à la topologie de réplication ou aux interfaces API. Lorsqu'une capacité de droits des personnes concernées est temporairement indisponible, [Organisation] DOIT notifier les responsables du traitement affectés de l'indisponibilité et du délai de rétablissement prévu, et DOIT fournir une assistance manuelle (ex. export assisté par le personnel) lorsqu'un responsable du traitement fait face à un délai légal pendant la période d'indisponibilité. Les procédures de repli manuelles sont documentées dans le plan de réponse aux incidents de [Organisation].

---

# Rôles et responsabilités

| Rôle | Responsabilités |
|------|----------------|
| **Délégué à la Protection des Données (DPD)** | Surveille la satisfaction des responsables du traitement avec les capacités de satisfaction des droits ; examine les résultats annuels des tests de capacité ; conseille sur les obligations émergentes en matière de droits |
| **RSSI / Responsable Sécurité Cloud** | Propriétaire de la conception et de la maintenance des capacités de droits ; gère le programme annuel de tests des capacités ; signale les lacunes au DPD |
| **Ingénierie Cloud** | Met en œuvre et maintient les mécanismes de satisfaction des droits ; résout les lacunes techniques de capacité ; confirme la propagation des opérations de droits aux copies de sauvegarde et répliquées |
| **Prestation de services cloud** | Assiste les responsables du traitement dans l'exercice des capacités de droits ; escalade les demandes complexes à l'Ingénierie Cloud |

---

# Exigences en matière de preuves

| Preuve | Description | Conservation |
|-------|-------------|-------------|
| Documentation des capacités de droits | Documentation par service des capacités relatives aux droits des personnes concernées et des instructions d'utilisation | En cours + versions précédentes pendant 3 ans |
| Résultats des tests annuels de capacité | Résultats documentés des tests pour tous les types de droits par service | 3 ans |
| Enregistrements de suivi de remédiation | Éléments suivis pour les lacunes de capacité identifiées lors des tests | Jusqu'à résolution + 3 ans |
| Enregistrements d'assistance au responsable du traitement | Journal des demandes liées aux DSAR reçues des responsables du traitement et résultats de résolution | Durée du contrat + 3 ans |

---

# Considérations d'audit

Les auditeurs vérifiant la conformité à CLD-POL-A.9 doivent s'attendre à trouver :

- Une documentation à jour des capacités relatives aux droits des personnes concernées par service cloud
- Des enregistrements de tests annuels de capacité couvrant tous les types de droits avec les résultats et toute remédiation
- Aucune lacune matérielle non résolue pour la satisfaction des droits des personnes concernées
- Des enregistrements des demandes d'assistance liées aux DSAR des responsables du traitement et leur résolution dans les délais

---

<!-- QA_VERIFIED: 2026-04-04 -->
