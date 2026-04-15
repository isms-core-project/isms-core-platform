<!-- ISMS-CORE:POLICY:AI-POL-A.6.1-FR:ai:POL:a.6.1 -->
**AI-POL-A.6.1 — Gouvernance du développement IA**

---

## Contrôle du document

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Gouvernance du développement IA |
| **Type de document** | Politique |
| **ID du document** | AI-POL-A.6.1 |
| **Auteur du document** | Responsable de la Gouvernance IA (RGIA) / Directeur Technique (DT) |
| **Propriétaire du document** | Directeur Général (DG) |
| **Approuvé par** | Direction générale |
| **Date de création** | [Date à définir] |
| **Version** | 1.0 |
| **Date de version** | [Date à définir] |
| **Classification** | Interne |
| **Statut** | Brouillon |
| **Version du produit AIMS** | 1.0 |

**Historique des versions** :

| Version | Date | Auteur | Modifications |
|---------|------|--------|--------------|
| 1.0 | [Date à définir] | RGIA / DT | Politique initiale pour la première certification ISO/IEC 42001:2023 |

**Cycle de révision** : Annuel (ou en cas de changement significatif de la méthodologie de développement IA ou des normes d'IA responsable)
**Date de prochaine révision** : [Date d'entrée en vigueur + 12 mois]

**Chaîne d'approbation** :

- Primaire : Responsable de la Gouvernance IA (RGIA)
- Secondaire : Directeur Technique (DT) / Responsable IA Engineering
- Conformité : Responsable de la Sécurité des Systèmes d'Information (RSSI)
- Autorité finale : Direction générale

**Documents connexes** :

- AI-POL-00 (Cadre d'applicabilité réglementaire IA)
- AI-POL-01 (Cadre de gouvernance et de prise de décisions AIMS)
- AI-POL-A.5.2-5 (Évaluation d'impact des systèmes IA — l'ÉISIA guide la sélection des contrôles)
- AI-POL-A.6.2 (Cycle de vie des systèmes IA — contrôles du cycle de vie opérationnel)
- AI-IMP-A.6.1-UG (Gouvernance du développement IA — Guide utilisateur)
- AI-IMP-A.6.1-TG (Gouvernance du développement IA — Guide technique)
- ISO/IEC 42001:2023 Contrôles A.6.1.2, A.6.1.3
- ISO/IEC 42001:2023 Annexe B.6.1 (Orientations de mise en œuvre — Gouvernance du développement de systèmes IA)

---

## Synthèse exécutive

La présente politique établit les exigences de l'[organisation] pour identifier et intégrer des objectifs de développement responsable, et pour définir et documenter les processus par lesquels les systèmes IA sont conçus et développés de manière responsable — conformément aux Contrôles A.6.1.2 et A.6.1.3 d'ISO/IEC 42001:2023.

**Périmètre** : Tous les systèmes IA développés par l'[organisation] (rôle de fournisseur IA) ; les objectifs, processus et pratiques de gouvernance guidant le cycle de vie du développement de la conception jusqu'à la remise pour déploiement.

**Note d'applicabilité** : Les contrôles A.6.1 s'appliquent principalement aux organisations agissant en tant que **fournisseurs IA** — celles qui développent, entraînent ou créent autrement des systèmes IA. Les organisations agissant uniquement en tant que déployeurs IA (utilisant une IA tierce sans modification) doivent le documenter dans la DDA AIMS et appliquer A.6.1 là où elles exercent une influence significative sur la conception ou la configuration du système IA.

**Objectif** : Définir QUELS objectifs de développement responsable doivent être établis et documentés (A.6.1.2), et QUELS processus de conception et développement responsables doivent être définis (A.6.1.3). La mise en œuvre est dans AI-IMP-A.6.1-UG et AI-IMP-A.6.1-TG.

**Justification combinée des contrôles** : A.6.1.2 et A.6.1.3 forment la couche de gouvernance stratégique et de processus pour le développement IA. Les objectifs (A.6.1.2) établissent les principes d'IA responsable qui doivent être intégrés dans le cycle de développement ; les processus (A.6.1.3) définissent COMMENT ces principes sont mis en œuvre opérationnellement. Les deux contrôles doivent être appliqués ensemble pour assurer une gouvernance du développement efficace.

---

## Périmètre et applicabilité

### Énoncés des contrôles ISO/IEC 42001:2023

**Contrôle A.6.1.2 — Objectifs pour le développement responsable du système IA**
L'organisation doit identifier et documenter des objectifs pour guider le développement responsable des systèmes IA, et tenir compte de ces objectifs et intégrer des mesures pour les atteindre dans le cycle de vie du développement.

**Contrôle A.6.1.3 — Processus pour la conception et le développement responsables du système IA**
L'organisation doit définir et documenter les processus spécifiques pour la conception et le développement responsables du système IA.

### Ce que couvre la présente politique

- Objectifs de développement IA responsable à établir par système IA
- Exigences de processus pour la conception et le développement IA responsables
- Intégration des résultats de l'ÉISIA dans la gouvernance du développement
- Points de contrôle d'IA responsable tout au long du cycle de vie du développement

### Ce que la présente politique ne couvre PAS

- Contrôles du cycle de vie opérationnel (exigences, V&V, déploiement, monitoring — traités dans AI-POL-A.6.2)
- Processus de gestion des données (traités dans AI-POL-A.7.2-6)
- Procédures d'évaluation de la conformité au Règlement IA UE (traitées dans AI-POL-A.8.2-5 et AI-POL-00)

### Cadre réglementaire

**Niveau 1 : Conformité obligatoire** (per AI-POL-00) :

- **Règlement IA de l'UE (Règlement 2024/1689)** : Article 9 — les fournisseurs d'IA à haut risque doivent établir un système de management de la qualité traitant les objectifs d'IA responsable ; Article 9(1)(b) — méthodologie de conception et développement ; Article 10 — exigences d'entraînement, validation et test pour un développement responsable

**Niveau 2 : Conditionnel** (per AI-POL-00) :

- **ISO/IEC 42001:2023** : Contrôles A.6.1.2, A.6.1.3 — applicable si la certification AIMS est dans le périmètre ou contractuellement requise

**Niveau 3 : Informatif** (per AI-POL-00) :

- NIST AI RMF : GOVERN 4.x — pratiques de développement IA organisationnelles ; MAP 2.x — identification de l'impact dans le développement
- ISO/IEC 23894:2023 : Considérations de management des risques lors du développement IA

---

## Déclarations de politique : Objectifs de développement responsable (A.6.1.2)

### Exigence d'objectifs de développement responsable

L'[organisation] DOIT identifier et documenter des objectifs pour le développement responsable de chaque système IA. Ces objectifs doivent :

- Être établis avant le début du développement (non rétrospectivement)
- Refléter les principes d'IA responsable dans la Politique IA (AI-POL-A.2.2-4)
- Être éclairés par les résultats de l'ÉISIA pour le système IA (AI-POL-A.5.2-5)
- Être intégrés dans le cycle de vie du développement en tant que critères de conception mesurables, et non déclarations aspirationnelles
- Être approuvés par le RGIA avant le début du développement

### Objectifs fondamentaux de développement responsable

Les propriétés d'IA responsable suivantes doivent être considérées comme des objectifs pour chaque système IA développé par l'[organisation]. L'applicabilité et le niveau de mise en œuvre sont déterminés par la classification d'impact de l'ÉISIA (Faible / Moyen / Élevé) :

**Équité et non-discrimination**

Le système IA doit traiter les individus et les groupes de manière équitable. Les objectifs doivent préciser :

- Les groupes démographiques ou caractéristiques protégées pertinents pour l'évaluation de l'équité
- Les métriques d'équité appropriées pour le cas d'usage (p. ex., parité démographique, equalised odds, parité prédictive)
- Les seuils acceptables pour les métriques d'équité avant déploiement — les seuils sont définis par le RGIA en concertation avec le DT et l'expertise sectorielle concernée, documentés dans l'ÉISIA et approuvés avant le début de la V&V
- Le processus de monitoring de l'équité en production (A.6.2.6)

**Transparence et explicabilité**

Les sorties du système IA doivent être interprétables dans la mesure nécessaire pour la supervision humaine et la communication avec les personnes concernées. Les objectifs doivent préciser :

- Le niveau d'explicabilité requis (importance des variables, justification des décisions, explications locales) selon le cas d'usage et la classification d'impact
- Le public cible des explications (opérateurs internes, personnes concernées, régulateurs)
- La documentation des limites du modèle et des conditions dans lesquelles les sorties peuvent ne pas être fiables

**Robustesse et sécurité**

Le système IA doit fonctionner de manière fiable dans ses conditions opérationnelles documentées et défaillir en sécurité lorsque les conditions sortent du périmètre opérationnel défini. Les objectifs doivent préciser :

- Les conditions opérationnelles définies et les exigences de détection hors distribution
- Les exigences de robustesse adversariale (lorsque le système IA pourrait être une cible)
- Les modes de défaillance acceptables et le comportement de sécurité par défaut
- La couverture de test pour les cas limites et les entrées adversariales

**Protection de la vie privée dès la conception**

Le système IA doit traiter les données à caractère personnel de manière minimale et par conception, non en ajout après coup. Les objectifs doivent préciser :

- Les exigences de minimisation des données pour les données d'entraînement et opérationnelles
- Les exigences d'anonymisation ou de pseudonymisation
- Les exigences du RGPD Article 25 (protection des données dès la conception et par défaut) le cas échéant
- Le renvoi aux obligations PRIV-POL-00

**Supervision humaine**

La conception du système IA doit soutenir, et non compromettre, une supervision humaine significative. Les objectifs doivent préciser :

- Les points de contrôle de la supervision humaine requis avant que les décisions pilotées par l'IA n'affectent les personnes
- Les mécanismes de dérogation — capacité pour les humains de surpasser les sorties IA
- Les exigences de journalisation et de piste d'audit pour soutenir la supervision humaine
- Les mécanismes d'alerte pour le comportement anormal du système IA

**Responsabilité**

Une responsabilité humaine claire pour le comportement du système IA doit être maintenue. Les objectifs doivent préciser :

- Le Responsable des risques IA nommé et responsable du système IA (AI-POL-A.3.2-3)
- Le chemin d'escalade pour les incidents IA
- Les exigences de piste d'audit reliant les sorties IA à la version du système qui les a produites

### Documenter les objectifs de développement responsable

Les objectifs de développement responsable doivent être documentés dans un **Dossier d'objectifs de développement du système IA** pour chaque système IA, signé par :

- Le RGIA (approbation de la gouvernance IA responsable)
- Le Responsable des risques IA (acceptation des risques)
- Le DT / Responsable IA Engineering (confirmation de la faisabilité technique)

Le dossier doit être mis à jour si le résultat de l'ÉISIA change de manière significative.

---

## Déclarations de politique : Processus de conception et développement IA responsables (A.6.1.3)

### Exigence de définition des processus

L'[organisation] DOIT définir et documenter les processus spécifiques pour la conception et le développement responsables de chaque système IA. Ces processus doivent opérationnaliser les objectifs de développement responsable définis dans A.6.1.2.

### Processus de développement responsable requis

**1. Revue de conception IA responsable**

Avant le début du développement, un processus de revue de conception doit valider que :

- L'architecture proposée du système IA soutient les objectifs d'IA responsable documentés
- Les considérations d'équité, d'explicabilité et de protection de la vie privée sont intégrées dans la conception, et non ajoutées après coup
- L'usage prévu est clairement spécifié et les contrôles limitant le périmètre sont conçus dès le départ

La revue de conception doit être documentée, avec approbation du RGIA.

**2. Processus d'évaluation des biais et de l'équité**

Pour les systèmes IA avec une classification d'impact Moyen ou Élevé (per AI-POL-A.5.2-5), le processus de développement doit inclure :

- Pré-développement : Évaluation de la représentativité du jeu de données — les données d'entraînement représentent-elles la population de déploiement ?
- Développement : Sélection et entraînement du modèle avec prise en compte de l'équité — quelles contraintes ou objectifs d'équité sont intégrés ?
- Pré-déploiement : Évaluation de l'équité par rapport aux métriques et seuils approuvés
- Post-déploiement : Monitoring continu de l'équité (A.6.2.6)

Le processus d'évaluation des biais doit être documenté par système IA avec conservation des preuves.

**3. Points de contrôle du développement IA responsable**

Le processus de développement doit inclure des points de contrôle définis auxquels les critères d'IA responsable sont évalués avant de passer à l'étape suivante :

| Point de contrôle | Étape | Ce qui est vérifié |
|-------------------|-------|-------------------|
| Approbation de la conception | Avant le début du développement | Objectifs d'IA responsable documentés ; ÉISIA complétée ; sources de données approuvées |
| Gate de qualité des données | Avant l'entraînement du modèle | Représentativité des données, critères de qualité satisfaits ; provenance documentée |
| Revue de développement | En cours de développement actif | Contrôles d'équité, d'explicabilité et de protection de la vie privée mis en œuvre comme prévu |
| Revue pré-validation | Avant V&V (A.6.2.4) | Documentation du modèle complète ; critères de test définis incluant les critères d'IA responsable |
| Approbation pré-déploiement | Avant déploiement (A.6.2.5) | Tous les objectifs d'IA responsable évalués ; ÉISIA à jour ; mécanismes de supervision humaine mis en œuvre |

Chaque point de contrôle doit produire un résultat documenté. Un système ne passant pas un point de contrôle d'IA responsable ne peut pas progresser à l'étape suivante jusqu'à résolution des problèmes.

**4. Processus de documentation IA responsable**

Tout au long du développement, la documentation suivante doit être maintenue :

- **Fiche modèle** : Usage prévu, description des données d'entraînement, résultats d'évaluation incluant les métriques d'équité, limites connues, usages hors périmètre
- **Fiche données** : Description du jeu de données, méthodologie de collecte, évaluation de la représentativité, analyse des biais
- **Dossier de critères d'IA responsable** : Comment chaque objectif d'IA responsable a été adressé dans la conception et le développement

---

## Rôles et responsabilités

| Rôle | Responsabilités |
|------|----------------|
| **RGIA** | Approuver les objectifs de développement responsable ; approuver la revue de conception ; conduire ou mandater les revues de points de contrôle d'IA responsable ; maintenir les dossiers d'objectifs |
| **DT / Responsable IA Engineering** | Diriger les revues de conception IA responsable ; s'assurer que le processus de développement inclut les points de contrôle ; s'assurer que les équipes d'engineering sont formées aux pratiques d'IA responsable |
| **Propriétaire du système IA** | Maintenir le dossier d'objectifs de développement responsable ; s'assurer que la documentation des points de contrôle est complète |
| **Data Scientists / Ingénieurs ML** | Appliquer les techniques tenant compte de l'équité ; réaliser les évaluations de représentativité des données ; documenter les fiches modèles et fiches données |
| **Responsable des risques IA** | Accepter le risque d'IA responsable résiduel ; escalader lorsque les objectifs ne peuvent être atteints |

---

## Exigences de preuves

| Preuve | Description | Conservation |
|-------|-------------|-------------|
| Dossier d'objectifs de développement responsable | Document par système IA des objectifs d'IA responsable avec approbation | Durée du système + 3 ans |
| Dossiers de revue de conception | Documentation des revues de conception IA responsable avec résultats | Durée du système + 3 ans |
| Dossiers de points de contrôle | Preuves de chaque point de contrôle d'IA responsable avec résultat validé/refusé | Durée du système + 3 ans |
| Fiches modèles | Documentation du modèle incluant l'évaluation de l'équité et les limites | Durée du système + 3 ans |
| Fiches données | Documentation du jeu de données incluant la représentativité et l'analyse des biais | Durée d'utilisation des données + 3 ans |

---

## Considérations pour l'audit

Les auditeurs vérifiant la conformité avec A.6.1.2–A.6.1.3 doivent s'attendre à trouver :

- Des objectifs de développement responsable documentés par système IA, antérieurs au développement
- Des preuves que les objectifs ont été éclairés par les résultats de l'ÉISIA
- Un processus de développement défini avec des points de contrôle d'IA responsable
- Des dossiers de points de contrôle démontrant que les critères d'IA responsable ont été évalués avant les transitions d'étapes
- Des fiches modèles et fiches données comme artefacts de sortie du processus de développement

---

<!-- QA_VERIFIED: [YYYY-MM-DD] -->
