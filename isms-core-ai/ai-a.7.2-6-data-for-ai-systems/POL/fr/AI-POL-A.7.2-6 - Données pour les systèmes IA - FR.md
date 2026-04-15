<!-- ISMS-CORE:POLICY:AI-POL-A.7.2-6-FR:ai:POL:a.7.2-6 -->
**AI-POL-A.7.2-6 — Données pour les systèmes IA**

---

## Contrôle du document

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Données pour les systèmes IA |
| **Type de document** | Politique |
| **ID du document** | AI-POL-A.7.2-6 |
| **Auteur du document** | Responsable de la Gouvernance IA (RGIA) / Responsable de la gouvernance des données |
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
| 1.0 | [Date à définir] | RGIA / Responsable de la gouvernance des données | Politique initiale pour la première certification ISO/IEC 42001:2023 |

**Cycle de révision** : Annuel (ou en cas de changement significatif des pratiques de données IA ou des réglementations applicables)
**Date de prochaine révision** : [Date d'entrée en vigueur + 12 mois]

**Chaîne d'approbation** :

- Primaire : Responsable de la Gouvernance IA (RGIA)
- Secondaire : Responsable de la gouvernance des données / Directeur des Données
- Conformité : Juridique / Délégué à la Protection des Données (DPD)
- Autorité finale : Direction générale

**Documents connexes** :

- AI-POL-00 (Cadre d'applicabilité réglementaire IA)
- AI-POL-A.4.2-6 (Ressources des systèmes IA — documentation des ressources de données)
- AI-POL-A.6.2 (Cycle de vie des systèmes IA — données utilisées dans le développement et l'exploitation)
- AI-IMP-A.7.2-6-UG (Données pour les systèmes IA — Guide utilisateur)
- AI-IMP-A.7.2-6-TG (Données pour les systèmes IA — Guide technique)
- PRIV-POL-00 (Applicabilité réglementaire en matière de protection de la vie privée — pour les données IA contenant des données à caractère personnel)
- ISO/IEC 42001:2023 Contrôles A.7.2, A.7.3, A.7.4, A.7.5, A.7.6
- ISO/IEC 42001:2023 Annexe B.7 (Orientations de mise en œuvre — Données pour les systèmes IA)

---

## Synthèse exécutive

La présente politique établit les exigences de l'[organisation] pour la gestion des données tout au long du cycle de vie des systèmes IA — couvrant les processus de gestion des données, l'acquisition et la sélection des données, la qualité des données, la provenance des données et la préparation des données — conformément aux Contrôles A.7.2 à A.7.6 d'ISO/IEC 42001:2023.

**Périmètre** : Toutes les données utilisées dans le développement, l'entraînement, la validation, les tests et l'exploitation des systèmes IA dans le périmètre AIMS.

**Note sur la protection de la vie privée** : Lorsque les données IA contiennent ou sont dérivées de données à caractère personnel, la présente politique s'applique conjointement avec PRIV-POL-00 et la suite de contrôles PIMS. Le RGPD Article 5 (minimisation des données, limitation des finalités pour les données d'entraînement IA contenant des données à caractère personnel) et l'Article 25 (protection des données dès la conception) s'appliquent en sus des exigences de la présente politique.

**Objectif** : Définir QUELLES exigences de gouvernance des données s'appliquent aux systèmes IA, QUI est responsable et QUAND les processus de gouvernance des données doivent être appliqués. La mise en œuvre est dans AI-IMP-A.7.2-6-UG et AI-IMP-A.7.2-6-TG.

**Justification combinée des contrôles** : A.7.2 à A.7.6 forment le cadre de gouvernance des données pour l'IA. La gestion des données (A.7.2) établit les exigences de processus globales ; l'acquisition (A.7.3) régit la façon dont les données entrent dans le pipeline IA ; la qualité (A.7.4) fixe les standards que les données doivent satisfaire ; la provenance (A.7.5) garantit que l'origine et les droits sur les données sont suivis ; la préparation (A.7.6) régit la transformation des données brutes en forme exploitable par le modèle.

---

## Périmètre et applicabilité

### Énoncés des contrôles ISO/IEC 42001:2023

**Contrôle A.7.2 — Données pour le développement et l'amélioration du système IA**
L'organisation doit définir, documenter et mettre en œuvre des processus de gestion des données liés au développement des systèmes IA.

**Contrôle A.7.3 — Acquisition de données**
L'organisation doit déterminer et documenter les détails relatifs à l'acquisition et à la sélection des données utilisées dans les systèmes IA.

**Contrôle A.7.4 — Qualité des données pour les systèmes IA**
L'organisation doit définir et documenter les exigences de qualité des données et s'assurer que les données utilisées pour développer et exploiter le système IA satisfont ces exigences.

**Contrôle A.7.5 — Provenance des données**
L'organisation doit définir et documenter un processus d'enregistrement de la provenance des données utilisées dans ses systèmes IA tout au long des cycles de vie des données et du système IA.

**Contrôle A.7.6 — Préparation des données**
L'organisation doit définir et documenter ses critères de sélection des approches de préparation des données et les méthodes de préparation des données à utiliser.

### Cadre réglementaire

**Niveau 1 : Conformité obligatoire** (per AI-POL-00) :

- **Règlement IA de l'UE (Règlement 2024/1689)** : Article 10 — exigences de gouvernance des données pour les données d'entraînement IA à haut risque (critères de qualité, représentativité, absence d'erreurs et de biais, pratiques de gouvernance des données) ; Article 11 — la documentation technique doit inclure une description des données d'entraînement
- **RGPD** : Article 5 (limitation des finalités, minimisation des données pour les données d'entraînement IA contenant des données à caractère personnel) ; Article 25 (protection des données dès la conception) ; Article 35 (AIPD lorsque le traitement de données IA présente un risque élevé)

**Niveau 2 : Conditionnel** (per AI-POL-00) :

- **ISO/IEC 42001:2023** : Contrôles A.7.2–A.7.6 — applicable si la certification AIMS est dans le périmètre ou contractuellement requise

---

## Déclarations de politique : Processus de gestion des données (A.7.2)

### Exigence de cadre de gestion des données

L'[organisation] DOIT définir, documenter et mettre en œuvre des processus de gestion des données régissant toutes les données utilisées dans le développement et l'amélioration des systèmes IA. Ces processus doivent être intégrés dans le cycle de vie du développement IA (AI-POL-A.6.2) et doivent traiter l'intégralité du cycle de vie des données, de l'acquisition jusqu'à la suppression.

### Gouvernance du cycle de vie des données IA

Les processus de gestion des données doivent couvrir chaque étape du cycle de vie des données :

| Étape | Exigence de gouvernance |
|-------|------------------------|
| **Acquisition** | Critères d'acquisition documentés et processus d'approbation (A.7.3) |
| **Ingestion** | Intake versionné avec enregistrement de la provenance (A.7.5) |
| **Évaluation de la qualité** | Critères de qualité appliqués avant utilisation (A.7.4) |
| **Préparation** | Méthodologie de préparation documentée (A.7.6) |
| **Stockage** | Contrôles d'accès, chiffrement, sauvegarde per ISMS |
| **Utilisation en entraînement / validation / exploitation** | Liaison de versions — quel version du jeu de données a été utilisée dans quelle version du modèle |
| **Mise à jour / ré-entraînement** | Critères de déclenchement pour les mises à jour du jeu de données et le ré-entraînement |
| **Archivage** | Ce qu'il faut conserver, pour combien de temps et dans quel format |
| **Suppression** | Critères et processus de suppression sécurisée ; lien vers PRIV-POL-00 lorsque des données à caractère personnel sont impliquées |

---

## Déclarations de politique : Acquisition et sélection des données (A.7.3)

### Exigence d'acquisition des données

L'[organisation] DOIT déterminer et documenter les détails de l'acquisition et de la sélection des données pour chaque système IA. Aucune donnée ne peut entrer dans le pipeline de développement IA sans approbation documentée d'acquisition.

### Documentation d'acquisition des données

Pour chaque jeu de données acquis à des fins IA :

| Champ | Contenu requis |
|-------|---------------|
| Identifiant du jeu de données | Nom unique et version |
| Source | Origine des données (système interne, jeu de données public, jeu de données sous licence, collecte commandée, web scraping, autre) |
| Méthode d'acquisition | Comment les données ont été obtenues |
| Base juridique / licence | Licence sous laquelle les données sont utilisées ; confirmation de propriété ; pour les données à caractère personnel : base juridique au titre du RGPD |
| Usage prévu | Quel(s) système(s) IA et quelle(s) étape(s) du cycle de vie les données sont destinées |
| Périmètre et couverture | Ce que les données représentent ; ce qu'elles ne représentent pas |
| Date d'acquisition | Quand les données ont été obtenues |
| Approbateur responsable | Approbation du Responsable de la gouvernance des données pour l'acquisition |

### Sources de données interdites

Les éléments suivants NE DOIVENT PAS être utilisés comme données d'entraînement ou opérationnelles IA sans approbation documentée explicite du RGIA et du Juridique :

- Données obtenues par web scraping lorsque les conditions d'utilisation du site web interdisent un tel usage
- Données contenant des données à caractère personnel sans base juridique documentée au titre du RGPD
- Données synthétiques où la méthode de génération introduit des biais systématiques sans mesure d'atténuation documentée
- Données dont les droits de propriété intellectuelle sont incertains ou litigieux
- Données dont la provenance ne peut être établie

---

## Déclarations de politique : Qualité des données (A.7.4)

### Exigence de qualité des données

L'[organisation] DOIT définir et documenter les exigences de qualité des données pour chaque système IA et vérifier que les données satisfont ces exigences avant leur utilisation en entraînement, validation ou exploitation.

### Dimensions de la qualité des données

Les critères de qualité doivent être définis selon les dimensions suivantes pour chaque jeu de données :

| Dimension | Définition | Méthode d'évaluation |
|-----------|-----------|----------------------|
| **Complétude** | Quelle proportion de champs ou d'enregistrements requis est présente | Contrôle statistique de complétude |
| **Exactitude** | Degré auquel les données représentent correctement l'entité réelle qu'elles décrivent | Échantillonnage et validation par rapport à la vérité terrain |
| **Représentativité** | Degré auquel les données représentent la population de déploiement selon les dimensions démographiques pertinentes | Analyse de distribution ; évaluation de la couverture démographique |
| **Actualité** | Les données sont suffisamment récentes pour le cas d'usage ; la dérive temporelle est évaluée | Analyse de la distribution temporelle |
| **Cohérence** | Les données sont cohérentes entre les sources et dans le temps | Validation croisée inter-sources ; contrôles de cohérence |
| **Absence de biais préjudiciables** | Les données ne contiennent pas de biais systématiques qui produiraient des sorties IA inéquitables | Analyse des biais sur les caractéristiques protégées |
| **Qualité des étiquettes** (pour l'apprentissage supervisé) | Les étiquettes sont exactes, cohérentes et produites par des annotateurs qualifiés | Accord inter-annotateurs ; audit des étiquettes |

### Gate de qualité

Chaque jeu de données doit être évalué par rapport à ses critères de qualité définis avant utilisation. Les jeux de données ne satisfaisant pas aux seuils de qualité minimaux doivent :

1. Être rejetés pour utilisation, OU
2. Être remédié (collecte de données supplémentaires, nettoyage, augmentation) avec la remédiation documentée, OU
3. Être utilisés avec une acceptation de risque documentée du Responsable des risques IA, avec les limitations de qualité connues notées dans la fiche modèle

Aucun jeu de données ne peut être utilisé dans un système IA sans résultats documentés d'évaluation de la qualité.

---

## Déclarations de politique : Provenance des données (A.7.5)

### Exigence de provenance des données

L'[organisation] DOIT définir et mettre en œuvre un processus d'enregistrement et de maintenance de la provenance de toutes les données utilisées dans les systèmes IA tout au long des cycles de vie des données et du système IA.

### Exigences relatives aux enregistrements de provenance

Un enregistrement de provenance des données doit être maintenu pour chaque jeu de données, en suivant :

| Élément | Contenu |
|---------|---------|
| Identifiant et version du jeu de données | Référence unique |
| Source originale | D'où proviennent les données (avec référence à l'enregistrement d'acquisition) |
| Historique des transformations | Tous les nettoyages, normalisations, augmentations ou autres transformations appliqués — avec dates et partie responsable |
| Jeux de données dérivés | Si ce jeu de données est dérivé d'un autre, lien vers l'enregistrement de provenance parent |
| Systèmes IA utilisant ce jeu de données | Quels systèmes IA (et versions de modèle) ont utilisé ce jeu de données |
| Journal de conservation et suppression | Quand les données ont été archivées ou supprimées, et sous quelle autorité |

### Liaison de versions

Le système de provenance doit permettre la traçabilité : pour toute version de modèle IA déployée, il doit être possible d'identifier la ou les versions exactes du jeu de données utilisées en entraînement et validation. Cette traçabilité est requise pour :

- Les preuves d'audit et de certification
- L'investigation des incidents (déterminer si un problème de données a contribué à un incident IA)
- La conformité réglementaire (documentation technique Article 11 du Règlement IA UE)
- La conformité au droit à l'effacement (RGPD Article 17 — identifier quels modèles ont été entraînés sur des données faisant l'objet d'une demande d'effacement)

### RGPD Article 17 — Droit à l'effacement pour les données d'entraînement IA

Lorsqu'une personne concernée soumet une demande d'effacement valide au titre du RGPD Article 17, l'[organisation] DOIT :

1. **Supprimer immédiatement l'enregistrement des données d'entraînement source** — supprimer les données de la personne de tous les jeux de données d'entraînement, ensembles de validation et espaces de stockage associés sans délai injustifié.
2. **Évaluer le risque résiduel dans les poids du modèle** — en utilisant la traçabilité de provenance, identifier toutes les versions de modèles IA entraînées sur les données. Documenter une évaluation technique pour savoir si les données de la personne sont récupérables ou attribuables aux poids du modèle entraîné. Pour les architectures de réseaux de neurones standard, l'effacement complet des poids est généralement techniquement infaisable ; cette infaisabilité doit être documentée.
3. **Répondre à la personne concernée** — accuser réception de la demande d'effacement, confirmer la suppression des données source et, lorsque l'effacement complet des poids du modèle est techniquement infaisable, documenter cette limitation et l'évaluation du risque résiduel conformément aux orientations de l'ATD applicable.
4. **Déclencher le ré-entraînement ou la mise hors service du modèle** — lorsque l'évaluation du risque résiduel identifie une probabilité significative d'identification de la personne à partir des sorties du modèle (par exemple, le modèle a été entraîné sur un petit jeu de données, ou la personne est un point de données distinctif), le Propriétaire du système IA doit évaluer si un ré-entraînement ou une mise hors service du modèle est nécessaire. Le DPD doit conseiller sur le seuil de risque pour cette détermination.
5. **Journaliser toutes les actions d'effacement** — enregistrer la demande, la confirmation de suppression des données source, l'évaluation du modèle et toute décision de ré-entraînement dans le Registre de gouvernance des données IA. Conserver les enregistrements pendant 5 ans.

Lorsque l'[organisation] utilise des techniques de confidentialité différentielle lors de l'entraînement, cela doit être documenté dans l'ÉISIA et référencé dans les réponses aux effacements comme mesure d'atténuation du risque.

---

## Déclarations de politique : Préparation des données (A.7.6)

### Exigence de préparation des données

L'[organisation] DOIT définir et documenter les critères de sélection des approches de préparation des données et les méthodes à utiliser. Les décisions de préparation des données doivent être documentées et reproductibles.

### Gouvernance de la préparation des données

La préparation des données — le processus de transformation des données brutes en une forme adaptée à l'entraînement ou à l'exploitation du modèle IA — doit être :

**Documentée** : Chaque pipeline de préparation doit être documenté incluant :
- Étapes de pré-traitement appliquées (normalisation, encodage, imputation, tokenisation, etc.)
- Décisions de feature engineering avec justification
- Critères de filtrage (enregistrements exclus et pourquoi)
- Méthodes d'augmentation appliquées (et leurs paramètres)
- Stratégie d'échantillonnage lorsque les volumes de données nécessitent un échantillonnage

**Sous contrôle de version** : Les scripts et pipelines de préparation des données doivent être versionnés parallèlement au code du modèle, permettant la reproduction du jeu de données préparé exact à partir de la source brute.

**Consciente des biais** : Les décisions de préparation des données doivent être examinées pour leur potentiel à introduire ou amplifier des biais. Les étapes pouvant affecter de manière disproportionnée les groupes sous-représentés (p. ex., sous-échantillonnage, stratégies d'imputation) doivent être documentées avec justification et évaluation de l'impact sur les biais.

**Gouvernance des annotateurs** (pour les données étiquetées) :

- Les directives d'annotation doivent être documentées
- Les qualifications des annotateurs documentées
- L'accord inter-annotateurs mesuré et documenté
- La qualité des étiquettes en dessous des seuils acceptables déclenche une ré-annotation

---

## Rôles et responsabilités

| Rôle | Responsabilités |
|------|----------------|
| **RGIA** | Posséder la politique de gouvernance des données IA ; approuver l'acquisition de jeux de données à haute sensibilité ; réviser les problèmes de qualité des données escaladés par le Responsable de la gouvernance des données |
| **Responsable de la gouvernance des données** | Posséder et opérer les processus A.7.x au quotidien ; approuver les acquisitions de données standard ; maintenir les enregistrements de provenance ; présider les gates de qualité des données |
| **DPD / Responsable de la protection de la vie privée** | Réviser les données IA impliquant des données à caractère personnel ; assurer la conformité RGPD pour les données d'entraînement ; conseiller sur les implications du droit à l'effacement |
| **Data Scientists / Ingénieurs ML** | Conduire les évaluations de la qualité des données ; documenter les pipelines de préparation ; signaler les problèmes de qualité au Responsable de la gouvernance des données |
| **Propriétaire du système IA** | S'assurer que les enregistrements de gouvernance des données sont à jour pour les systèmes IA dont il est responsable |

---

## Exigences de preuves

| Preuve | Description | Conservation |
|-------|-------------|-------------|
| Enregistrements d'acquisition des données | Documentation d'acquisition par jeu de données avec base juridique et approbation | Durée d'utilisation du jeu de données + 5 ans |
| Enregistrements d'évaluation de la qualité des données | Résultats d'évaluation de la qualité par jeu de données par rapport aux critères définis | Durée d'utilisation du jeu de données + 3 ans |
| Enregistrements de provenance des données | Historique des transformations et enregistrements de liaison de versions | Durée du système IA + 5 ans après mise hors service |
| Documentation de préparation des données | Documentation du pipeline avec référence au code versionné | Durée du système IA + 3 ans |
| Résultats des gates de qualité | Enregistrements des décisions de passage/échec aux gates de qualité avec approbation | Durée du système IA + 3 ans |

---

## Considérations pour l'audit

Les auditeurs vérifiant la conformité avec A.7.2–A.7.6 doivent s'attendre à trouver :

- Des processus de gestion des données documentés couvrant l'intégralité du cycle de vie des données
- Des enregistrements d'acquisition pour tous les jeux de données utilisés dans les systèmes IA dans le périmètre
- Des critères de qualité des données définis par système IA et des enregistrements d'évaluation de la qualité confirmant que les critères sont satisfaits
- Des enregistrements de provenance des données permettant la traçabilité du modèle déployé au jeu de données d'entraînement
- Des pipelines de préparation des données documentés et versionnés
- Des preuves que les gates de qualité des données sont appliquées avant que les jeux de données entrent en production

---

<!-- QA_VERIFIED: [2026-04-15] -->
