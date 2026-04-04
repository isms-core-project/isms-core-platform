<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.19-23-FR:framework:POL:a.5.19-23 -->
**ISMS-POL-A.5.19-23 — Sécurité des fournisseurs et des services en nuage**
**Cadre de politique et de mise en œuvre complet**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Sécurité des fournisseurs et des services en nuage |
| **Type de document** | Politique |
| **Identifiant du document** | ISMS-POL-A.5.19-23 |
| **Créateur du document** | Responsable de la sécurité des systèmes d'information (RSSI) |
| **Propriétaire du document** | Directeur général (DG) |
| **Approuvé par** | Direction générale |
| **Date de création** | [Date] |
| **Version** | 1.0 |
| **Date de version** | [À définir] |
| **Classification** | Interne |
| **Statut** | Projet |

**Historique des versions** :

| Version | Date | Auteur | Modifications |
|---------|------|--------|---------------|
| 1.0 | [Date] | RSSI/ISO | Cadre de politique initial pour la première certification ISO 27001:2022 |

**Cycle de révision** : Annuel
**Prochaine date de révision** : [Date d'entrée en vigueur + 12 mois]

**Chaîne d'approbation** :

- Principal : Responsable de la sécurité des systèmes d'information (RSSI)
- Secondaire : Directeur des systèmes d'information (DSI)
- Conformité : Responsable juridique/conformité
- Achats : Directeur des achats
- Autorité finale : Direction générale

**Documents connexes** :

- ISMS-POL-00 (Cadre d'applicabilité réglementaire)
- ISMS-POL-A.5.19-23-S1 (Fondamentaux des relations fournisseurs)
- ISMS-POL-A.5.19-23-S2 (Exigences des accords fournisseurs)
- ISMS-POL-A.5.19-23-S3 (Sécurité de la chaîne d'approvisionnement TIC)
- ISMS-POL-A.5.19-23-S4 (Surveillance des fournisseurs et gestion des changements)
- ISMS-POL-A.5.19-23-S5 (Sécurité des services en nuage)
- ISMS-POL-A.5.19-23-S6 (Méthodologie d'évaluation et automatisation)
- ISMS-IMP-A.5.19-23.S1-UG/TG (Inventaire et classification des services en nuage)
- ISMS-IMP-A.5.19-23.S2-UG/TG (Diligence raisonnable et contrats fournisseurs)
- ISMS-IMP-A.5.19-23.S3-UG/TG (Configuration sécurisée et déploiement)
- ISMS-IMP-A.5.19-23.S4-UG/TG (Gouvernance continue et gestion des risques)
- ISMS-REF-A.5.23 (Registre des prestataires de services en nuage)
- ISO/IEC 27001:2022 Contrôles A.5.19-23
- ISO/IEC 27036 (Relations fournisseurs)
- ISO/IEC 27017 (Sécurité en nuage)
- ISO/IEC 27018 (Protection de la vie privée en nuage)

**Distribution** : Tous les employés, prestataires, équipes achats, équipe juridique, exploitation informatique, administrateurs de nuage

---

## Résumé exécutif

Le présent document constitue l'**index principal** du cadre de sécurité des fournisseurs et des services en nuage de [Organisation], mettant en œuvre les contrôles ISO/IEC 27001:2022 A.5.19 à A.5.23.

**Objet** : Établir des exigences obligatoires pour gérer les risques de sécurité de l'information associés aux fournisseurs externes, aux engagements contractuels, aux dépendances de la chaîne d'approvisionnement TIC, à la gestion continue des relations fournisseurs et au cycle de vie des services en nuage.

**Périmètre** : Toutes les relations fournisseurs impliquant un accès aux informations ou systèmes organisationnels, tous les services en nuage (IaaS, PaaS, SaaS, services de sécurité), tous les accords contractuels avec des prestataires de services externes et tous les produits TIC présentant des dépendances en matière de chaîne d'approvisionnement.

**Principe critique — « La confiance envers les fournisseurs doit être vérifiée, non présumée »** : Ce cadre exige une validation fondée sur des preuves de la posture de sécurité des fournisseurs via une diligence raisonnable systématique, des engagements contractuels avec des clauses exécutoires et une surveillance continue tout au long du cycle de vie de la relation. Les déclarations de fournisseurs sans attestation tierce (SOC 2, ISO 27001, certificats de conformité réglementaire), les contrats sans clauses de sécurité exécutoires et droits d'audit, et les relations sans revue périodique créent des risques inacceptables. La confiance mais la vérification par des preuves documentées est non négociable.

**Composants du cadre** :

- **Couche politique :** Documents de gouvernance définissant les exigences (7 documents de politique)
- **Couche d'évaluation :** Spécifications d'évaluation technique (documentation markdown)
- **Couche de mise en œuvre :** Cahiers Excel générés par Python (4 cahiers d'évaluation)
- **Couche de validation :** Scripts d'assurance qualité et de normalisation
- **Couche d'intégration :** Tableaux de bord récapitulatifs des cahiers individuels

**Approche** : Ce cadre emploie un **processus documenté et systématique** où les outils d'évaluation sont générés de manière programmatique à partir de spécifications contrôlées plutôt que créés manuellement. Cela garantit la cohérence, la reproductibilité et le contrôle des versions — si les exigences d'évaluation changent, la régénération des cahiers mis à jour suit des procédures documentées plutôt qu'une édition manuelle sujette aux erreurs.

**Alignement réglementaire** : La présente politique répond aux exigences de conformité obligatoires visées par ISMS-POL-00 (Cadre d'applicabilité réglementaire), notamment la nLPD suisse, le RGPD de l'UE (article 28 — accords avec les sous-traitants et exigences de sécurité), l'ISO/IEC 27001:2022, et les exigences conditionnelles pour DORA (registre des risques liés aux TIC tiers, évaluation du risque de concentration, stratégies de sortie conformément aux art. 28-31), NIS2 (mesures de sécurité de la chaîne d'approvisionnement, notification d'incident dans les 24 heures conformément aux art. 21-23), la loi européenne sur l'IA (exigences des fournisseurs de systèmes d'IA à haut risque) et les considérations juridictionnelles du CLOUD Act américain lorsque les activités commerciales de [Organisation] en déclenchent l'applicabilité.

---

## Alignement des contrôles

**ISO/IEC 27001:2022 Annexe A.5.19-23 — Sécurité des fournisseurs et des services en nuage**

Ce cadre de politique assure la gouvernance organisationnelle de cinq contrôles connexes couvrant le cycle de vie complet des fournisseurs et des services en nuage :

### A.5.19 — Sécurité de l'information dans les relations avec les fournisseurs

> *Des processus et procédures devraient être définis et convenus avec les fournisseurs pour gérer les risques de sécurité de l'information associés à l'utilisation des produits ou services du fournisseur.*

**Objectif du contrôle** : S'assurer que les risques de sécurité de l'information associés aux relations fournisseurs sont identifiés, évalués et gérés tout au long du cycle de vie de la relation.

**Synthèse des orientations ISO/IEC 27002:2022** :

- Les relations fournisseurs doivent être gérées via des processus définis couvrant le cycle de vie complet (sélection, intégration, exploitation, sortie)
- Les fournisseurs doivent être identifiés et classifiés selon le type d'accès, la sensibilité des données et la criticité du service
- Une diligence raisonnable doit être effectuée avant d'accorder l'accès des fournisseurs aux informations ou systèmes organisationnels
- Les exigences de sécurité des fournisseurs doivent être définies sur la base de la classification des risques et des données
- La performance et la posture de sécurité des fournisseurs doivent être surveillées tout au long de la relation
- Des procédures de sortie fournisseur doivent être établies pour assurer une résiliation sécurisée et le retour des données
- L'informatique fantôme (Shadow IT) et l'utilisation non autorisée de fournisseurs doivent être activement identifiées et gérées
- Les risques de dépendance et de concentration des fournisseurs doivent être évalués pour les services critiques

**Référence de politique** : Voir ISMS-POL-A.5.19-23-S1 (Fondamentaux des relations fournisseurs) pour les exigences détaillées.

### A.5.20 — Prise en compte de la sécurité de l'information dans les accords avec les fournisseurs

> *Des exigences de sécurité de l'information pertinentes devraient être établies et convenues avec chaque fournisseur susceptible d'accéder, de traiter, de stocker, de communiquer ou de fournir des composants d'infrastructure informatique pour les informations de l'organisation.*

**Objectif du contrôle** : S'assurer que les exigences de sécurité de l'information sont contractuellement contraignantes et exécutoires tout au long de la relation fournisseur.

**Synthèse des orientations ISO/IEC 27002:2022** :

- Les exigences de sécurité de l'information doivent figurer dans tous les contrats et accords fournisseurs
- Les exigences doivent traiter la confidentialité, l'intégrité et la disponibilité des informations organisationnelles
- Les contrats doivent définir les contrôles d'accès, les exigences d'authentification et les procédures d'autorisation
- Les obligations de protection des données et de la vie privée doivent être spécifiées conformément aux réglementations applicables (RGPD art. 28, nLPD)
- Les exigences de notification et de réponse aux incidents doivent être documentées avec des délais précis
- Les droits d'audit et les mécanismes de vérification de conformité doivent être établis
- Les accords de niveau de service (SLA) doivent inclure des indicateurs de sécurité
- Les procédures de résiliation et les obligations de retour/destruction des données doivent être définies contractuellement
- Le droit d'audit (sur site ou à distance) et la coopération réglementaire doivent être exécutoires

**Référence de politique** : Voir ISMS-POL-A.5.19-23-S2 (Exigences des accords fournisseurs) pour les exigences contractuelles détaillées.

### A.5.21 — Gestion de la sécurité de l'information dans la chaîne d'approvisionnement TIC

> *Des processus et procédures devraient être définis et convenus avec les fournisseurs pour gérer les risques de sécurité de l'information associés à la chaîne d'approvisionnement des services et produits de technologie de l'information et de la communication (TIC).*

**Objectif du contrôle** : Gérer les risques de sécurité de l'information au sein de la chaîne d'approvisionnement TIC, y compris les sous-fournisseurs, les composants et les dépendances logicielles.

**Synthèse des orientations ISO/IEC 27002:2022** :

- Les risques de la chaîne d'approvisionnement TIC doivent être identifiés et évalués de manière systématique
- Les exigences de sécurité pour les produits et services TIC doivent être spécifiées lors de la passation de marchés
- Les sous-fournisseurs des fournisseurs (transparence de la chaîne d'approvisionnement) doivent être évalués et divulgués
- La sécurité de la chaîne d'approvisionnement logicielle doit être traitée, notamment les dépendances, les bibliothèques et les composants open source
- La sécurité de la chaîne d'approvisionnement matérielle doit être prise en compte, notamment la détection de contrefaçons et la protection contre la falsification
- La continuité et la résilience de la chaîne d'approvisionnement doivent être planifiées pour les services TIC critiques
- Les changements et mises à jour des fournisseurs doivent être gérés via des processus de gestion des changements
- L'évaluation des risques de la chaîne d'approvisionnement doit inclure les dépendances géopolitiques, de concentration et à source unique

**Référence de politique** : Voir ISMS-POL-A.5.19-23-S3 (Sécurité de la chaîne d'approvisionnement TIC) pour les exigences détaillées.

### A.5.22 — Surveillance, révision et gestion des changements des services fournisseurs

> *L'organisation devrait régulièrement surveiller, réviser, évaluer et gérer les changements dans les pratiques de sécurité de l'information et la prestation de services des fournisseurs.*

**Objectif du contrôle** : Assurer la validation continue de la posture de sécurité des fournisseurs et la gestion contrôlée des changements apportés aux services fournisseurs.

**Synthèse des orientations ISO/IEC 27002:2022** :

- La performance des fournisseurs doit être surveillée en continu par rapport aux engagements contractuels
- Des revues périodiques des pratiques de sécurité des fournisseurs doivent être effectuées selon la classification des risques
- Les modifications des services fournisseurs doivent être gérées via des procédures formelles de gestion des changements
- La conformité des fournisseurs aux accords doit être vérifiée par des audits, des attestations ou des certifications
- Les incidents et événements de sécurité des fournisseurs doivent être suivis, analysés et traités de manière appropriée
- Des audits de fournisseurs ou des attestations tierces (SOC 2, ISO 27001) doivent être obtenus et révisés
- La relation avec les fournisseurs doit être maintenue via des communications et réunions régulières
- La dégradation des services fournisseurs ou la non-conformité doit déclencher des procédures d'escalade et de correction

**Référence de politique** : Voir ISMS-POL-A.5.19-23-S4 (Surveillance des fournisseurs et gestion des changements) pour les exigences de gouvernance détaillées.

### A.5.23 — Sécurité de l'information pour l'utilisation des services en nuage

> *Des processus d'acquisition, d'utilisation, de gestion et de sortie des services en nuage devraient être établis conformément aux exigences de sécurité de l'information de l'organisation.*

**Objectif du contrôle** : Gérer le cycle de vie des services en nuage de manière systématique, de la sélection jusqu'à la sortie sécurisée.

**Synthèse des orientations ISO/IEC 27002:2022** :

- L'acquisition de services en nuage doit suivre un processus de sélection basé sur les risques avec évaluation de la sécurité
- Les accords de services en nuage doivent traiter les exigences de sécurité et le modèle de responsabilité partagée
- Le modèle de responsabilité partagée doit être explicitement compris et documenté (contrôles du prestataire vs. du client)
- La configuration des services en nuage doit être sécurisée conformément aux référentiels du fournisseur et aux exigences organisationnelles
- Les exigences de résidence et de souveraineté des données en nuage doivent être appliquées conformément aux obligations réglementaires
- La surveillance et la journalisation des services en nuage doivent être mises en œuvre avec une conservation appropriée
- La stratégie de sortie des services en nuage doit être planifiée et testée, notamment l'export des données et la portabilité
- Les risques spécifiques au nuage (multilocation, commingling des données, juridiction) doivent être évalués et atténués
- Les certifications et la conformité du prestataire en nuage doivent être vérifiées (SOC 2, ISO 27017, CSA STAR)

**Référence de politique** : Voir ISMS-POL-A.5.19-23-S5 (Sécurité des services en nuage) pour les exigences spécifiques au nuage.

---

# Structure du cadre

## Objet

Établir des exigences obligatoires pour gérer les risques de sécurité de l'information associés à :

- Les fournisseurs externes proposant des produits ou services
- Les engagements contractuels avec les fournisseurs
- Les dépendances de la chaîne d'approvisionnement TIC
- La gestion continue des relations fournisseurs
- L'acquisition, l'exploitation et la sortie des services en nuage

## Périmètre

Ce cadre s'applique à :

- Toutes les relations fournisseurs impliquant un accès aux informations ou systèmes organisationnels
- Tous les services en nuage (modèles IaaS, PaaS, SaaS, XaaS incluant les services de sécurité, les plateformes de collaboration, le stockage)
- Tous les accords contractuels avec des prestataires de services externes
- Tous les produits et services TIC présentant des dépendances de chaîne d'approvisionnement
- Tous les employés, prestataires et tiers gérant des relations fournisseurs

## Exclusions

Ce cadre ne couvre pas :

- Les achats ponctuels sans relation de service continue ni accès aux données
- Les fournisseurs sans accès aux actifs informationnels organisationnels
- Les prestataires de services internes (couverts par les politiques RH/opérationnelles distinctes)

---

# Documents de politique

## Structure de la politique

Le cadre de politique de sécurité des fournisseurs et des services en nuage comprend les documents modulaires suivants :

| Identifiant du document | Titre | Contrôle(s) principal/aux | Objet |
|-------------------------|-------|--------------------------|-------|
| **ISMS-POL-A.5.19-23** | Index principal | Tous (5.19-23) | Présentation du cadre et navigation |
| **ISMS-POL-A.5.19-23-S1** | Fondamentaux des relations fournisseurs | A.5.19 | Classification des risques et diligence raisonnable |
| **ISMS-POL-A.5.19-23-S2** | Exigences des accords fournisseurs | A.5.20 | Clauses contractuelles et exigences SLA |
| **ISMS-POL-A.5.19-23-S3** | Sécurité de la chaîne d'approvisionnement TIC | A.5.21 | Sécurité des sous-fournisseurs et composants |
| **ISMS-POL-A.5.19-23-S4** | Surveillance des fournisseurs et gestion des changements | A.5.22 | Cycles de revue et procédures de changement |
| **ISMS-POL-A.5.19-23-S5** | Sécurité des services en nuage | A.5.23 | Gestion du cycle de vie en nuage |
| **ISMS-POL-A.5.19-23-S6** | Méthodologie d'évaluation et automatisation | Tous (5.19-23) | Génération programmatique de documentation |

**Philosophie de conception** : Chaque document est versionnable indépendamment pour permettre une gestion granulaire des changements, des revues ciblées par parties prenantes et des pistes d'audit claires.

## Hiérarchie des documents

```
ISMS-POL-A.5.19-23 (Index principal) ← Vous êtes ici
│
├── S1 : Fondamentaux des relations fournisseurs (A.5.19)
│   └── Définit : Catégories de risques, classification, diligence raisonnable
│
├── S2 : Exigences des accords fournisseurs (A.5.20)
│   └── Définit : Clauses contractuelles, exigences SLA, termes de sécurité
│
├── S3 : Sécurité de la chaîne d'approvisionnement TIC (A.5.21)
│   └── Définit : Exigences sous-fournisseurs, sécurité des composants
│
├── S4 : Surveillance des fournisseurs et gestion des changements (A.5.22)
│   └── Définit : Cycles de revue, droits d'audit, procédures de changement
│
├── S5 : Sécurité des services en nuage (A.5.23)
│   └── Définit : Cycle de vie nuage (sélection → mise en œuvre → sortie)
│
└── S6 : Méthodologie d'évaluation et automatisation (Tous contrôles)
    └── Définit : Cahiers Excel, scripts Python, validation

Couche de mise en œuvre (Documents séparés) :
├── ISMS-IMP-A.5.19-23.0 (Spécification de mise à jour réglementaire — DORA/NIS2/Loi IA/CLOUD Act)
├── ISMS-IMP-A.5.19-23.1 (Inventaire et classification des services en nuage)
├── ISMS-IMP-A.5.19-23.2 (Diligence raisonnable et contrats fournisseurs)
├── ISMS-IMP-A.5.19-23.3 (Configuration sécurisée et déploiement)
└── ISMS-IMP-A.5.19-23.4 (Gouvernance continue et gestion des risques)

Données de référence :
└── ISMS-REF-A.5.23 (Registre des prestataires de services en nuage)
```

---

# Documents d'évaluation et de mise en œuvre

## Spécifications d'évaluation (Markdown)

Le cadre comprend des spécifications d'évaluation complètes définissant la structure et les exigences pour la génération des cahiers Excel :

| Identifiant du document | Titre | Objet | Feuilles |
|-------------------------|-------|-------|----------|
| **ISMS-IMP-A.5.19-23.0** | Spécification de mise à jour réglementaire | Améliorations DORA, NIS2, Loi IA, CLOUD Act | S.O. (spec) |
| **ISMS-IMP-A.5.19-23.1** | Inventaire et classification des services en nuage | Inventaire faisant autorité avec classification des données et criticité | ~10 |
| **ISMS-IMP-A.5.19-23.2** | Diligence raisonnable et contrats fournisseurs | Critères de diligence raisonnable, clauses de sécurité contractuelles | ~8 |
| **ISMS-IMP-A.5.19-23.3** | Configuration sécurisée et déploiement | Référentiels de configuration de sécurité et déploiement | ~8 |
| **ISMS-IMP-A.5.19-23.4** | Gouvernance continue et gestion des risques | Surveillance, cycles de revue, gestion des incidents | ~8 |

**Note** : ISMS-IMP-A.5.19-23.0 est un document de spécification pour la mise à jour des cahiers 1-4 avec les améliorations réglementaires, et non un cahier autonome.

## Cahiers Excel générés

Lors de l'exécution des générateurs Python, ils produisent :

| Cahier | Feuilles | Utilisateurs principaux | Objet |
|--------|----------|------------------------|-------|
| **ISMS_REG_A523_1_Inventory_AAAAMMJJ.xlsx** | ~10 | Achats, Sécurité, Exploitation IT | Inventaire des services, classification des données, faisabilité de sortie |
| **ISMS_REG_A523_2_DueDiligence_AAAAMMJJ.xlsx** | ~8 | Achats, Juridique, Sécurité | Évaluation fournisseur, revue contractuelle, clauses de sécurité |
| **ISMS_REG_A523_3_Configuration_AAAAMMJJ.xlsx** | ~8 | Architectes nuage, Sécurité | Référentiels de configuration sécurisée, conformité du déploiement |
| **ISMS_REG_A523_4_Governance_AAAAMMJJ.xlsx** | ~8 | Exploitation IT, Sécurité | Surveillance continue, gestion des changements, suivi des incidents |

**Total des résultats d'évaluation :** ~34 feuilles réparties sur 4 cahiers

## Domaines d'évaluation expliqués

**Domaine 0 — Mises à jour réglementaires (Spécification)** :

- Quels cadres réglementaires s'appliquent ? (DORA, NIS2, Loi IA)
- Quels risques juridictionnels existent ? (exposition au CLOUD Act américain)
- Quels champs supplémentaires sont requis ? (risque de concentration, souveraineté des données)
- Comment les cahiers prennent-ils en charge la conformité conditionnelle ? (listes déroulantes de périmètre réglementaire)

**Domaine 1 — Inventaire et classification des services en nuage** :

- Quels services en nuage existent ? (inventaire complet : SaaS, IaaS, PaaS, services de sécurité)
- Quelles données sont traitées ? (classification : Public, Interne, Confidentiel, Restreint)
- Quelle est la criticité du service ? (évaluation de l'impact métier)
- Où se trouvent les données ? (résidence : Suisse, UE, USA, multi-région)
- Quelle est la faisabilité de sortie ? (portabilité, fournisseurs alternatifs, coût de transition)
- Quel périmètre réglementaire s'applique ? (applicabilité DORA, NIS2, Loi IA par service)

**Domaine 2 — Diligence raisonnable et contrats fournisseurs** :

- Quelle diligence raisonnable a été effectuée ? (certifications, rapports d'audit, questionnaires de sécurité)
- Quelles clauses de sécurité figurent dans les contrats ? (protection des données, notification d'incident, droits d'audit)
- Quels sont les engagements SLA ? (disponibilité, délai de support, délais de notification de violation)
- Quelle est la juridiction du prestataire ? (siège social, centres de données, sous-traitants)
- Quelle est l'exposition au CLOUD Act américain ? (prestataires basés aux États-Unis, stratégies d'atténuation)
- Quelles dispositions de sortie existent ? (export des données, assistance à la transition, clauses de résiliation)

**Domaine 3 — Configuration sécurisée et déploiement** :

- Quels référentiels de configuration s'appliquent ? (benchmarks CIS, guides de durcissement fournisseur)
- Quels contrôles de sécurité sont activés ? (chiffrement, AMF, segmentation réseau, journalisation)
- Comment l'accès est-il géré ? (moindre privilège, accès basé sur les rôles, surveillance des comptes privilégiés)
- Quelle surveillance est déployée ? (événements de sécurité, performance, dérive de conformité)
- Quelle est la division de la responsabilité partagée ? (contrôles de l'organisation vs. du prestataire)

**Domaine 4 — Gouvernance continue et gestion des risques** :

- Quel calendrier de revue s'applique ? (trimestriel pour les risques élevés, annuel pour les risques faibles)
- Quels indicateurs de performance existent ? (conformité SLA, fréquence des incidents, réactivité du support)
- Quels incidents se sont produits ? (événements de sécurité, interruptions de service, violations de données)
- Quels changements ont été approuvés ? (changements de configuration, avenants contractuels, migrations)
- Quels risques sont suivis ? (risque de concentration, enfermement fournisseur, lacunes de conformité)

**Domaine 5 — Tableau de bord de surveillance de la conformité** :

- Quel est l'état de conformité global ? (indicateurs de signalisation par domaine)
- Quels sont les indicateurs de performance clés ? (complétude de l'inventaire, couverture contractuelle, conformité de configuration)
- Quelles lacunes existent ? (contrats manquants, SLA faibles, dérive de configuration)
- Quelles preuves réglementaires existent ? (documentation DORA/NIS2/Loi IA)
- Quelle est la feuille de route de remédiation ? (actions prioritaires, besoins budgétaires)

---

# Scripts d'automatisation

## Scripts générateurs d'évaluation

| Script | Cahier de sortie | Objet |
|--------|-----------------|-------|
| `generate_reg_a523_1_inventory.py` | ISMS-IMP-A.5.19-23.1_Inventory_{AAAAMMJJ}.xlsx | Inventaire et classification des services en nuage |
| `generate_reg_a523_2_vendor_dd.py` | ISMS-IMP-A.5.19-23.2_VendorDD_{AAAAMMJJ}.xlsx | Évaluation fournisseur et revue contractuelle |
| `generate_reg_a523_3_secure_config.py` | ISMS-IMP-A.5.19-23.3_SecureConfig_{AAAAMMJJ}.xlsx | Configuration sécurisée et déploiement |
| `generate_reg_a523_4_governance.py` | ISMS-IMP-A.5.19-23.4_Governance_{AAAAMMJJ}.xlsx | Surveillance continue et gestion des risques |

**Amélioration réglementaire** : Tous les générateurs intègrent les champs de la spécification ISMS-IMP-A.5.19-23.0 pour les exigences de conformité DORA, NIS2, Loi IA et CLOUD Act.

---

# Rôles et responsabilités

## Rôles exécutifs

| Rôle | Responsabilités |
|------|-----------------|
| **RSSI** | Responsabilité globale, approbation de la politique, validation des exceptions, acceptation des risques, approbation budgétaire |
| **Direction générale** | Décisions stratégiques sur les fournisseurs, allocation budgétaire, gouvernance des risques |
| **Directeur des achats** | Sélection des fournisseurs, négociation des contrats, gestion des coûts |
| **Conseil juridique** | Revue des contrats, conformité réglementaire, termes des accords, résolution des litiges |

## Rôles opérationnels

| Rôle | Responsabilités |
|------|-----------------|
| **Responsable de la sécurité de l'information** | Propriété de la politique, application, surveillance de la conformité, évaluation des risques fournisseurs |
| **Équipe achats** | Sélection des fournisseurs, gestion des appels d'offres, gestion des relations fournisseurs, administration des contrats |
| **Exploitation informatique** | Mise en œuvre technique, configuration, surveillance, gestion des changements |
| **Architectes nuage** | Conception des services en nuage, configuration de la sécurité, revue de l'architecture |
| **Propriétaires de systèmes** | Relations fournisseurs dans leur domaine, justification commerciale, approbation budgétaire |

## Rôles de soutien

| Rôle | Responsabilités |
|------|-----------------|
| **Conformité et audit** | Interprétation réglementaire (DORA, NIS2, Loi IA), support d'audit, collecte des preuves |
| **Gestion des risques** | Évaluation des risques fournisseurs, analyse du risque de concentration, maintenance du registre des risques |
| **Délégué à la protection des données (DPD)** | Conformité RGPD article 28, accords de traitement des données, analyses d'impact sur la protection des données |
| **Sécurité de l'information** | Développement des outils d'évaluation, scripts générateurs, automatisation de la validation |
| **Finance** | Suivi budgétaire, analyse des coûts, évaluation du ROI |

## Responsabilités des utilisateurs

| Rôle | Responsabilités |
|------|-----------------|
| **Tous les employés** | Respect de la liste des services en nuage approuvés, interdiction de l'informatique fantôme, signalement des incidents |
| **Responsables hiérarchiques** | Approbation budgétaire des services fournisseurs, justification commerciale, gestion des accès utilisateurs |

## Exigences de compétence

Le personnel effectuant des activités d'évaluation de la sécurité des fournisseurs et du nuage DOIT satisfaire aux exigences de compétence suivantes, documentées dans la [Matrice de formation et de compétences SMSI de l'organisation] :

**Personnel achats :**

- Formation à l'évaluation des risques fournisseurs (interne ou équivalent)
- Compréhension des exigences de sécurité pour les services en nuage
- Actualisation annuelle sur les clauses de sécurité contractuelles

**Architectes nuage / Évaluateurs techniques :**

- Certification en sécurité nuage (CCSP, CCSK, ou spécifique au fournisseur : AWS Security, Azure Security, GCP Security)
- Compréhension des modèles de responsabilité partagée
- Expérience en revue de configuration de sécurité nuage

**Conseil juridique :**

- Formation au RGPD et à la protection des données
- Compréhension des accords avec les sous-traitants (RGPD article 28)
- Familiarité avec les exigences DORA/NIS2 (le cas échéant)

**Responsable de la sécurité de l'information :**

- Responsable principal de mise en œuvre ISO 27001 ou équivalent
- Formation à la méthodologie d'appréciation du risque
- Cadres de sécurité nuage (CSA CCM, ISO 27017/27018)

**Preuve :** Registres de formation, certifications et évaluations de compétences maintenus conformément aux exigences de la Clause 7.2 de l'ISO 27001.

---

# Méthodologie d'évaluation

## Approche documentaire programmatique

Ce cadre emploie une **évaluation quantitative fondée sur des preuves** plutôt qu'une évaluation subjective :

**Principe fondamental** : Ce qui peut être créé de manière systématique peut être maintenu de manière systématique et vérifié objectivement. Les outils d'évaluation sont générés de manière programmatique pour garantir :

- **Cohérence** : Structure identique entre les cycles d'évaluation
- **Reproductibilité** : Même méthodologie d'évaluation appliquée à tous les fournisseurs
- **Traçabilité** : Piste d'audit complète de la politique à la mise en œuvre jusqu'aux preuves
- **Maintenabilité** : Les mises à jour des exigences se propagent systématiquement par régénération
- **Objectivité** : Le calcul automatique de la conformité élimine la notation subjective

**Validation fondée sur des preuves** :

- Pas d'auto-évaluations « nous sommes conformes parce que nous l'affirmons »
- Chaque statut « Conforme » nécessite des preuves documentées (certificats, contrats, configurations)
- Chaque fournisseur nécessite une attestation tierce (SOC 2, ISO 27001) ou un audit équivalent
- Chaque contrat nécessite des clauses de sécurité exécutoires avec droits d'audit
- Chaque exception nécessite une acceptation du risque par le RSSI avec mitigation documentée

## Exigences de preuve

**Pour chaque service fournisseur** :

| Type de preuve | Documentation requise | Norme minimale |
|----------------|----------------------|----------------|
| **Certification** | SOC 2 Type II, ISO 27001, ISO 27017, CSA STAR | En cours (voir règles de validité ci-dessous) |
| **Contrat** | Accord signé avec clauses de sécurité | Conformité RGPD art. 28 minimum |
| **Configuration** | Documentation des paramètres de sécurité de base | Benchmark CIS ou guide de durcissement fournisseur |
| **Surveillance** | Données de performance SLA, journaux d'incidents | Trimestriel minimum |
| **Évaluation des risques** | Diligence raisonnable documentée et évaluation des risques | Approuvée par le RSSI |

**Règles de validité des certifications :**

| Certification | Période de validité | Vérification de la validité |
|---------------|--------------------|-----------------------------|
| **ISO 27001** | 3 ans (cycle de certification) | Audit de surveillance annuel confirmé dans les 12 mois |
| **SOC 2 Type II** | 1 an (période du rapport) | Date du rapport dans les 12 mois |
| **CSA STAR** | 2 ans (Niveau 2) | Recertification annuelle ou surveillance continue |
| **ISO 27017/27018** | 3 ans (aligné sur ISO 27001) | Audit de surveillance confirmé dans les 12 mois |

**Critères de rejet** :

- Auto-attestation du fournisseur sans validation tierce
- Certifications expirées (au-delà de la période de validité ci-dessus)
- Contrats sans clauses de sécurité ni droits d'audit
- Accord de traitement des données manquant (violation RGPD)
- Pas de stratégie de sortie ni de mécanisme de portabilité des données

## Classification des risques fournisseurs

Les fournisseurs sont classifiés selon une **notation quantitative** sur six dimensions :

| Dimension | Pondération | Critères de notation |
|-----------|-------------|---------------------|
| **Accès aux données** | 25 % | Restreint=100, Confidentiel=75, Interne=50, Public=25, Aucun=0 |
| **Criticité du service** | 25 % | Critique (Niveau 1)=100, Élevé (Niveau 2)=75, Moyen (Niveau 3)=50, Faible (Niveau 4)=25 |
| **Remplaçabilité** | 15 % | Source unique=100, Alternatives limitées=75, Alternatives multiples=50, Générique=25 |
| **Profondeur d'intégration** | 15 % | Intégration profonde=100, Modérée=75, Légère=50, Aucune=25 |
| **Impact réglementaire** | 10 % | DORA/NIS2 critique=100, Sous-traitant RGPD=75, Pertinent conformité=50, Aucun impact=25 |
| **Risque de concentration** | 10 % | >50 % budget=100, 25-50 %=75, 10-25 %=50, <10 %=25 |

> **Note :** Les pondérations des dimensions peuvent être ajustées selon le contexte organisationnel. Les institutions financières soumises à la FINMA, DORA ou des cadres de supervision équivalents peuvent augmenter la pondération de l'**Impact réglementaire** à 15-20 % pour refléter les attentes renforcées des superviseurs.

**Clarification du risque de concentration :** Le risque de concentration est calculé comme pourcentage du **budget total des services IT** alloué à un seul fournisseur. Par exemple, si le budget IT total est de CHF 1 M et que les dépenses AWS sont de CHF 400 K, le risque de concentration est de 40 % (score 75 points). Lorsqu'un fournisseur propose des services dans plusieurs catégories budgétaires, agréger les dépenses de toutes les catégories.

**Score total → Classification** :

- **Niveau 1 (Critique) :** 75-100 points → Revue trimestrielle, SOC 2 Type II ou ISO 27001 obligatoire, droits d'audit sur site
- **Niveau 2 (Élevé) :** 50-74 points → Revue semestrielle, attestation tierce requise, droits d'audit à distance
- **Niveau 3 (Moyen) :** 25-49 points → Revue annuelle, auto-évaluation acceptable avec validation par sondage
- **Niveau 4 (Faible) :** 0-24 points → Revue bisannuelle, auto-évaluation acceptable

## Notation de la conformité

**Statut de conformité global** (modèle à signalisation) :

| Statut | Critères | Action requise |
|--------|----------|----------------|
| **Vert (Conforme)** | Toutes les exigences satisfaites, preuves récentes (< 12 mois), aucune constatation ouverte | Surveillance de routine |
| **Jaune (Partiellement conforme)** | Lacunes mineures ou preuves vieillissantes (12-18 mois), constatations non critiques | Plan de remédiation dans les 90 jours |
| **Rouge (Non conforme)** | Lacunes majeures, preuves manquantes, certifications expirées (> 18 mois), constatations critiques | Remédiation immédiate ou suspension du service |

**Indicateurs du tableau de bord** :

- Pourcentage de conformité par contrôle (A.5.19-23)
- Distribution des risques fournisseurs (N1/N2/N3/N4)
- Couverture contractuelle (% des services avec accords signés)
- Statut des certifications (% en cours vs. expirées)
- Complétude des preuves (% des documents requis disponibles)

## Logique conditionnelle réglementaire

Les cahiers d'évaluation implémentent un **affichage conditionnel des champs** selon l'applicabilité réglementaire :

**Champs DORA** (affichés si : entité du secteur financier dans l'UE) :

- Entrée au registre des risques liés aux TIC tiers
- Évaluation du risque de concentration
- Documentation de la stratégie de sortie
- Statut d'approbation de la sous-traitance
- Clauses de coopération avec l'autorité compétente

**Champs NIS2** (affichés si : entité essentielle/importante dans l'UE) :

- Mesures de sécurité de la chaîne d'approvisionnement
- Capacité de signalement d'incident dans les 24 heures
- Documentation de la responsabilité de la direction
- Rapport annuel d'évaluation des risques de cybersécurité

**Champs Loi IA** (affichés si : fournisseur/déployeur de systèmes d'IA) :

- Classification des systèmes d'IA à haut risque
- Statut d'évaluation de la conformité
- Obligations de transparence
- Mécanismes de supervision humaine

**Champs CLOUD Act** (affichés si : prestataire basé aux États-Unis) :

- Évaluation du risque juridictionnel
- Engagements de contestation juridique
- Chiffrement et gestion des clés
- Mesures supplémentaires (CCT, évaluation d'impact sur le transfert)

---

# Matrice d'intégration des contrôles

## Comment les contrôles fonctionnent ensemble

Ce cadre couvre cinq contrôles connexes qui fonctionnent ensemble tout au long du cycle de vie des fournisseurs/services en nuage :

| Phase du cycle de vie | Contrôle principal | Contrôles de soutien | Activités clés |
|-----------------------|--------------------|-----------------------|----------------|
| **Identification** | A.5.19 (Relations fournisseurs) | — | Découverte des fournisseurs, identification du Shadow IT, création d'inventaire |
| **Évaluation des risques** | A.5.19 (Relations fournisseurs) | A.5.21 (Chaîne d'approvisionnement) | Classification des risques, évaluation de criticité, délimitation de la diligence raisonnable |
| **Sélection** | A.5.19 + A.5.23 (Spécificités nuage) | A.5.21 (Chaîne d'approvisionnement) | Évaluation des fournisseurs, questionnaires de sécurité, preuve de concept |
| **Contractualisation** | A.5.20 (Accords) | A.5.19, A.5.23 | Négociation contractuelle, clauses de sécurité, définition SLA, dispositions de sortie |
| **Mise en œuvre** | A.5.23 (Services en nuage) | A.5.20 | Déploiement du service, configuration, provisionnement des accès, tests d'intégration |
| **Exploitation** | A.5.22 (Surveillance) | A.5.19, A.5.23 | Surveillance des performances, gestion des incidents, contrôle des changements, revue de conformité |
| **Revue** | A.5.22 (Surveillance) | A.5.19, A.5.20, A.5.21 | Évaluations périodiques, exercice des droits d'audit, recertification, renouvellement contractuel |
| **Sortie** | A.5.23 (Sortie nuage) | A.5.20 | Extraction des données, sauvegarde de configuration, migration du service, résiliation du contrat |

## Modèle de responsabilité partagée

| Couche | IaaS (AWS EC2) | PaaS (Azure App Service) | SaaS (Microsoft 365) |
|--------|----------------|--------------------------|----------------------|
| **Données** | Organisation | Organisation | Organisation |
| **Application** | Organisation | Organisation | Prestataire |
| **Exécution** | Organisation | Prestataire | Prestataire |
| **Système d'exploitation** | Organisation | Prestataire | Prestataire |
| **Virtualisation** | Prestataire | Prestataire | Prestataire |
| **Serveurs** | Prestataire | Prestataire | Prestataire |
| **Stockage** | Prestataire | Prestataire | Prestataire |
| **Réseau** | Partagé | Prestataire | Prestataire |

---

# Gestion du cycle de vie

## Phases du cycle de vie fournisseur

**Phase 1 : Sélection et diligence raisonnable (A.5.19, A.5.21)**

- Définition des besoins métier
- Identification et présélection des fournisseurs
- Distribution des questionnaires de sécurité
- Évaluation et classification des risques
- Évaluation technique (POC/pilote)
- Revue de diligence raisonnable (certifications, références, stabilité financière)

**Phase 2 : Contractualisation (A.5.20)**

- Négociation contractuelle avec clauses de sécurité
- Accord de traitement des données (RGPD art. 28)
- Définition des accords de niveau de service (SLA)
- Établissement des droits d'audit
- Documentation de la stratégie de sortie
- Approbation juridique et achats

**Phase 3 : Intégration et configuration (A.5.23)**

- Configuration du référentiel de sécurité
- Provisionnement des accès (moindre privilège)
- Mise en place de la surveillance et journalisation
- Intégration avec les systèmes organisationnels
- Formation et documentation des utilisateurs
- Approbation de mise en production

**Phase 4 : Exploitation et surveillance (A.5.22)**

- Surveillance continue des performances
- Suivi de la conformité SLA
- Revues de sécurité périodiques
- Gestion des changements
- Réponse et résolution des incidents
- Gestion de la relation

**Phase 5 : Revue et optimisation (A.5.22)**

- Revue contractuelle annuelle
- Analyse coûts-avantages
- Optimisation du service
- Renégociation ou renouvellement
- Évaluation des alternatives

**Phase 6 : Sortie et transition (A.5.23)**

- Identification des déclencheurs de sortie
- Export et validation des données
- Migration ou remplacement du service
- Résiliation du contrat
- Vérification de la destruction des données
- Documentation des retours d'expérience

**Exigences de test des plans de sortie :**

- Les plans de sortie pour les fournisseurs de **Niveau 1 (Critique)** DOIVENT être testés annuellement (DORA art. 28.6 le cas échéant)
- Les plans de sortie pour les fournisseurs de **Niveau 2 (Élevé)** DOIVENT être testés tous les deux ans ou lors d'un changement majeur de service
- Le test des plans de sortie comprend : validation de l'export des données, simulation de migration du service, vérification de l'intégration PCA/PRA
- Les résultats des tests sont documentés dans ISMS-IMP-A.5.19-23.4 (Cahier de gouvernance) et rapportés au RSSI

## Cycles de revue

| Niveau fournisseur | Fréquence de revue | Périmètre de revue |
|--------------------|--------------------|-------------------|
| **Niveau 1 (Critique)** | Trimestrielle | Revue complète de conformité, performance SLA, réévaluation des risques, statut des certifications |
| **Niveau 2 (Élevé)** | Semestrielle | Contrôle ponctuel de conformité, performance SLA, revue des changements majeurs |
| **Niveau 3 (Moyen)** | Annuelle | Validation de conformité, évaluation du renouvellement contractuel |
| **Niveau 4 (Faible)** | Bisannuelle | Décision de renouvellement contractuel, besoin commercial continu |

**Événements déclencheurs pour une revue ad hoc** :

- Incident de sécurité impliquant un fournisseur
- Changement ou migration majeure du service
- Avenant ou renouvellement contractuel
- Fusion/acquisition du fournisseur
- Modification réglementaire affectant les obligations fournisseurs
- Constatation d'audit ou lacune de conformité

## Gestion des exceptions

**Processus de demande d'exception** :

1. **Dépôt de la demande** : Le demandeur documente l'exception avec justification commerciale
2. **Évaluation des risques** : L'équipe sécurité évalue le niveau de risque et l'impact potentiel
3. **Contrôles compensatoires** : Identification des mesures d'atténuation si l'exception est approuvée
4. **Décision d'approbation** :
   - Risque faible : Responsable de la sécurité de l'information
   - Risque moyen : RSSI
   - Risque élevé : RSSI + DSI
   - Risque critique : Direction générale
5. **Documentation** : Exception enregistrée avec approbation, durée et date de revue
6. **Surveillance** : Revue périodique (trimestrielle pour les exceptions temporaires, annuelle pour les permanentes)
7. **Remédiation** : Plan d'action pour la clôture de l'exception si temporaire

## Détection du Shadow IT

Le Shadow IT (services en nuage ou fournisseurs non autorisés utilisés sans approbation IT/Sécurité) DOIT être activement détecté via les méthodes suivantes :

**Méthodes de détection :**

- **Analyse des journaux de pare-feu/proxy** : Identifier les connexions à des services SaaS/nuage non enregistrés
- **Surveillance des requêtes DNS** : Détecter la résolution de domaines associés à des services en nuage absents du registre des fournisseurs approuvés
- **Courtier de sécurité d'accès au nuage (CASB)** : Découverte automatisée de l'utilisation des services en nuage (lorsque déployé)
- **Revue des notes de frais** : Identifier les abonnements à des services en nuage dans les relevés achats/finance
- **Auto-signalement des utilisateurs** : Encourager la divulgation volontaire via des campagnes de sensibilisation (politique sans reproche pour l'usage existant)

**Cadence de détection :**

- Des analyses trimestrielles du Shadow IT DOIVENT être effectuées par l'exploitation informatique
- Les résultats sont rapportés au RSSI avec des recommandations de remédiation
- Les services découverts sont évalués pour les risques et soit intégrés au registre approuvé, soit mis hors service

---

# Gestion des incidents

## Catégories d'incidents fournisseurs

| Type d'incident | Définition | Réponse |
|-----------------|------------|---------|
| **Violation de sécurité** | Accès non autorisé, violation de données, ransomware | Confinement immédiat, investigation forensique, notification (RGPD 72 h, NIS2 24 h) |
| **Interruption de service** | Indisponibilité non planifiée dépassant le SLA | Gestion des incidents, activation de la continuité d'activité, communication fournisseur |
| **Violation contractuelle** | Non-conformité du fournisseur à l'accord | Escalade juridique, mise en demeure de correction, résiliation potentielle |
| **Dégradation des performances** | Échecs des indicateurs SLA | Plan d'amélioration des performances, intensification de la surveillance |
| **Échec d'un changement** | Changement non autorisé ou échoué | Procédures de retour arrière, revue de la gestion des changements |

## Exigences de notification

**Notification interne** :

- Immédiat : RSSI, Propriétaire du système, Exploitation informatique
- Dans les 4 heures : Direction générale (pour les incidents critiques)
- Dans les 24 heures : DPD (si des données personnelles sont impliquées)

**Notification externe** :

- **RGPD** : Autorité de contrôle dans les 72 heures (art. 33)
- **NIS2** : Autorité compétente dans les 24 heures (alerte précoce), 72 heures (notification d'incident), 1 mois (rapport final)
- **DORA** : Autorité compétente selon le calendrier réglementaire
- **Contractuelle** : Notification client selon les termes du contrat

**Exigences de notification fournisseurs** :

| Gravité de l'incident | Délai de notification du fournisseur |
|-----------------------|--------------------------------------|
| **Critique** (violation de données, ransomware) | Immédiat (dans les 4 heures suivant la prise de connaissance) |
| **Élevé** (interruption de service, événement de sécurité) | Dans les 24 heures |
| **Moyen** (performance dégradée, changement de configuration) | Dans les 72 heures |
| **Faible** (maintenance, indisponibilité planifiée) | Préavis de 5 jours ouvrés |

- La notification doit inclure : description de l'incident, systèmes affectés, impact sur les données, mesures de confinement, délai de résolution estimé
- Les fournisseurs DOIVENT coopérer à l'investigation des incidents et aux analyses forensiques
- Les fournisseurs DOIVENT fournir un rapport post-incident dans le délai convenu
- Ces délais DOIVENT être intégrés dans les contrats fournisseurs (à utiliser comme langage contractuel par les achats/juridique)

---

# Conformité et audit

## Exigences obligatoires

Ce cadre de politique démontre la conformité avec :

**Normes principales :**

- ISO/IEC 27001:2022 Annexe A Contrôles 5.19-5.23
- ISO/IEC 27002:2022 Contrôles 5.19-5.23 (orientations de mise en œuvre)
- ISO/IEC 27036 (série) — Sécurité de l'information pour les relations fournisseurs

**Normes spécifiques au nuage :**

- ISO/IEC 27017:2015 — Contrôles de sécurité en nuage
- ISO/IEC 27018:2019 — Protection de la vie privée en nuage (protection des DCP)
- CSA CCM (Cloud Controls Matrix) — Alignement avec le cadre de contrôle nuage

**Alignement réglementaire :**

- **nLPD (Loi fédérale suisse sur la protection des données)** : Accords de traitement des données, obligations sous-traitant art. 9
- **RGPD de l'UE** : Accords sous-traitant article 28, divulgation des sous-traitants ultérieurs
- **DORA** (Règlement sur la résilience opérationnelle numérique) : Gestion des risques liés aux TIC tiers pour les entités financières de l'UE
- **NIS2** (Directive sur la sécurité des réseaux et des systèmes d'information 2) : Sécurité de la chaîne d'approvisionnement pour les entités essentielles/importantes dans l'UE
- **Loi européenne sur l'IA** : Obligations fournisseur/déployeur de systèmes d'IA le cas échéant
- **CLOUD Act américain** : Évaluation et atténuation du risque juridictionnel

## Approche d'audit

**Méthodologie d'audit recommandée :**

1. **Revue documentaire :** Vérifier la complétude de la politique, l'approbation, la distribution
2. **Évaluation technique :** Revue des cahiers générés, validation de la qualité des preuves
3. **Sondage :** Sélectionner les fournisseurs à risque élevé pour une revue détaillée (10-20 % de l'inventaire)
4. **Revue contractuelle :** Vérifier les clauses de sécurité dans les accords (échantillon de 5-10 contrats)
5. **Évaluation nuage :** Revue de la sélection, configuration et planification de sortie des services en nuage
6. **Vérification réglementaire :** Vérifier la conformité DORA/NIS2/Loi IA le cas échéant
7. **Entretiens :** Discussions avec Achats, Juridique, Exploitation IT, Architectes nuage, Sécurité
8. **Analyse des écarts :** Comparer les capacités réelles aux capacités requises
9. **Revue de remédiation :** Évaluer les plans de clôture des écarts, délais et allocation budgétaire

**Stratégie d'échantillonnage :**

- **Fournisseurs critiques** : Revue à 100 % (auditer tous les fournisseurs critiques)
- **Fournisseurs à risque élevé** : Échantillonnage à 50 %
- **Fournisseurs à risque moyen** : Échantillonnage à 25 %
- **Fournisseurs à faible risque** : Échantillonnage à 10 % ou sélection basée sur les risques

---

# Applicabilité réglementaire

## Niveau 1 : Conformité obligatoire

| Règlementation | Exigence | Applicabilité |
|----------------|----------|---------------|
| **nLPD suisse** | Mesures de sécurité du sous-traitant (art. 9), divulgation des sous-traitants ultérieurs | Tout traitement de données personnelles par [Organisation] |
| **RGPD UE** | Accords sous-traitant (art. 28), mesures de sécurité (art. 32), notification de violation (art. 33) | Lors du traitement de données personnelles de l'UE |
| **ISO/IEC 27001:2022** | Contrôles A.5.19-23 | Périmètre de certification |

## Niveau 2 : Applicabilité conditionnelle

| Règlementation | Exigence | Condition déclenchante |
|----------------|----------|------------------------|
| **Circulaire FINMA 2023/1** | Résilience opérationnelle, gouvernance des externalisations, registre des sous-externalisations, signalement d'incidents | Institution financière réglementée par la FINMA |
| **DORA** | Gestion des risques liés aux TIC tiers (art. 28-31) : registre des risques, évaluation de concentration, stratégies de sortie, dispositions contractuelles | Opérations de services financiers dans l'UE |
| **Directive NIS2** | Mesures de sécurité de la chaîne d'approvisionnement (art. 21), signalement d'incidents (art. 23) : alerte précoce 24 h, notification 72 h, rapport final | Désignation d'entité essentielle/importante |
| **Loi UE sur l'IA** | Exigences des systèmes d'IA à haut risque (art. 9-15) : évaluation de conformité, transparence, supervision humaine | Fourniture/déploiement de systèmes d'IA dans l'UE |
| **CLOUD Act américain** | Considérations d'accès aux données juridictionnel, transparence des procédures légales | Utilisation de prestataires en nuage basés aux États-Unis |

## Niveaux de risque et détermination de l'applicabilité

| Règlementation | Vous êtes soumis si... | À confirmer avec |
|----------------|------------------------|------------------|
| **DORA** | Votre entité est un établissement de crédit, établissement de paiement, établissement de monnaie électronique, entreprise d'assurance, entreprise d'investissement, prestataire de services sur crypto-actifs, ou autre entité financière réglementée par l'ABE, l'AEAPP ou l'AEMF en vertu du droit de l'UE | Juridique/Conformité — référence DORA article 2(2) |
| **NIS2** | Votre entité est classifiée comme essentielle ou importante en vertu de l'Annexe I/II de NIS2 (énergie, transport, eau, banque, santé, infrastructure numérique, etc.) dans un État membre de l'UE | Juridique/Conformité — référence NIS2 Annexes I/II et transposition nationale |
| **FINMA** | Votre entité est agréée par la FINMA en tant que banque, compagnie d'assurance, maison de titres ou organisme de placement collectif | Juridique/Conformité — référence Circulaire FINMA 2023/1 périmètre |
| **Loi UE sur l'IA** | Votre entité fournit, déploie ou utilise des systèmes d'IA classifiés comme à haut risque en vertu de l'Annexe III de la Loi UE sur l'IA sur le marché de l'UE | Juridique/Conformité — référence Loi UE sur l'IA article 6 et Annexe III |

## Exigences spécifiques DORA

Pour les entités financières de l'UE soumises à DORA, les exigences supplémentaires suivantes s'appliquent :

**Article 28 — Risques liés aux TIC tiers** :

- Maintenir un registre complet des risques liés aux TIC tiers
- Documenter l'évaluation des risques pour chaque prestataire de services TIC tiers
- Identifier le risque de concentration et les prestataires de services TIC tiers critiques
- Mettre en œuvre une stratégie de surveillance et de gestion des risques

**Article 29 — Dispositions contractuelles clés** :

- Coopération totale avec les autorités compétentes (accès, inspection, droits d'audit)
- Exigences et processus d'approbation de la sous-traitance
- Stratégies de sortie incluant la portabilité des données et l'assistance à la transition
- Accords de niveau de service avec indicateurs de sécurité
- Droits d'audit (sur site et à distance)
- Droits de résiliation en cas de non-conformité

**Article 30 — Sous-traitance en cascade** :

- Maintenir le registre des arrangements de sous-traitance en cascade
- Évaluer les risques de la sous-traitance en cascade
- S'assurer que les dispositions contractuelles s'appliquent aux sous-traitants
- Obtenir l'autorisation pour la sous-traitance critique en cascade

**Article 31 — Risque de concentration TIC** :

- Évaluer le risque de concentration lié aux prestataires TIC tiers individuels
- Documenter les dépendances envers les prestataires critiques
- Mettre en œuvre des stratégies d'atténuation du risque de concentration
- Signaler le risque de concentration aux autorités compétentes

## Souveraineté des données et considérations transfrontalières

| Cadre | Impact sur les services en nuage |
|-------|----------------------------------|
| **CLOUD Act américain** | Les prestataires basés aux États-Unis peuvent être contraints de divulguer des données quel que soit le lieu de stockage. Évaluer la juridiction du siège social du prestataire, évaluer les engagements de contestation juridique, mettre en œuvre des garanties techniques (chiffrement, clés gérées par le client). |
| **Initiatives de frontière des données UE** | Certains prestataires offrent des garanties de traitement de données exclusivement dans l'UE (AWS European Sovereign Cloud, Azure EU Data Boundary, régions UE de Google Cloud). Vérifier les engagements contractuels et la mise en œuvre technique. |
| **Cadre de protection des données Suisse-USA** | Mécanisme d'adéquation pour les transferts vers les États-Unis (remplace le Privacy Shield). Vérifier l'auto-certification du prestataire. |
| **Implications Schrems II** | Garanties supplémentaires requises pour les transferts vers des pays non adéquats : Évaluation d'impact sur le transfert (EIT), Clauses contractuelles types (CCT), mesures techniques supplémentaires (chiffrement, contrôles d'accès). |

---

# Définitions

| Terme | Définition |
|-------|------------|
| **Fournisseur** | Organisation externe proposant des produits ou services à [Organisation] pouvant accéder, traiter, stocker ou transmettre des informations organisationnelles |
| **Prestataire de services en nuage (PSN)** | Fournisseur proposant des services d'informatique en nuage (IaaS, PaaS, SaaS) via un réseau |
| **Prestataire de services TIC tiers** | Fournisseur proposant des produits ou services TIC critiques pour les opérations organisationnelles (terminologie DORA) |
| **Sous-traitant ultérieur** | Propres fournisseurs du fournisseur (sous-fournisseurs) pouvant accéder aux données organisationnelles |
| **Modèle de responsabilité partagée** | Répartition des responsabilités de sécurité entre le prestataire de services en nuage et le client |
| **Diligence raisonnable** | Évaluation systématique de la posture de sécurité d'un fournisseur avant engagement |
| **Risque de concentration** | Risque découlant de la dépendance envers un seul fournisseur ou un nombre limité de fournisseurs pour des services critiques |
| **Enfermement fournisseur** | Dépendance envers la technologie propriétaire d'un fournisseur rendant la migration coûteuse ou difficile |
| **Stratégie de sortie** | Plan de résiliation ordonnée de la relation fournisseur incluant l'export des données et la migration du service |
| **Résidence des données** | Emplacement géographique où les données sont physiquement stockées et traitées |
| **Souveraineté des données** | Exigence légale que les données soient soumises aux lois du pays où elles sont situées |
| **Évaluation d'impact sur le transfert (EIT)** | Évaluation de l'adéquation de la protection des données dans le pays de destination (exigence RGPD Schrems II) |
| **Clauses contractuelles types (CCT)** | Clauses contractuelles approuvées par la Commission de l'UE pour les transferts internationaux de données |
| **CLOUD Act américain** | Loi américaine de clarification sur l'utilisation légale des données à l'étranger — exigeant des entreprises américaines de fournir des données aux forces de l'ordre américaines indépendamment du lieu de stockage |
| **DORA** | Règlement sur la résilience opérationnelle numérique — réglementation de l'UE pour la gestion des risques TIC du secteur financier |
| **NIS2** | Directive sur la sécurité des réseaux et des systèmes d'information 2 — directive de l'UE sur la cybersécurité des entités essentielles/importantes |
| **Shadow IT / Informatique fantôme** | Services en nuage ou fournisseurs non autorisés utilisés sans approbation IT/Sécurité |

---

# Registre d'approbation

| Rôle | Nom | Date |
|------|-----|------|
| **Responsable de la sécurité des systèmes d'information (RSSI)** | [Nom] | [Date à définir] |
| **Directeur des systèmes d'information (DSI)** | [Nom] | [Date à définir] |
| **Directeur des achats** | [Nom] | [Date à définir] |
| **Responsable juridique/conformité** | [Nom] | [Date à définir] |
| **Direction générale** | [Nom] | [Date à définir] |

---

# Preuves pour ce cadre de politique

## Preuves d'étape 1 (revue de la documentation)

Preuves requises pour démontrer que ce cadre de politique est correctement documenté et approuvé :

- ✅ Ce document de politique principal (ISMS-POL-A.5.19-23 v1.0)
- ✅ Signatures d'approbation du RSSI, DSI, Directeur des achats, Responsable juridique/conformité, Direction générale (Registre d'approbation)
- ✅ Documents de sous-politique complets (S1-S6) :
  - S1 : Fondamentaux des relations fournisseurs (A.5.19)
  - S2 : Exigences des accords fournisseurs (A.5.20)
  - S3 : Sécurité de la chaîne d'approvisionnement TIC (A.5.21)
  - S4 : Surveillance des fournisseurs et gestion des changements (A.5.22)
  - S5 : Sécurité des services en nuage (A.5.23)
  - S6 : Méthodologie d'évaluation et automatisation
- ✅ Alignement des contrôles avec ISO/IEC 27001:2022 A.5.19-23 documenté
- ✅ Méthodologie de classification des risques fournisseurs définie
- ✅ Seuils de notation de la conformité établis
- ✅ Phases de gestion du cycle de vie documentées
- ✅ Catégories d'incidents et exigences de notification définies
- ✅ Rôles et responsabilités attribués avec exigences de compétence
- ✅ Cadre d'applicabilité réglementaire documenté
- ✅ Intégration avec les contrôles SMSI connexes documentée
- ✅ Intégration PCA/PRA pour les scénarios de sortie définie

## Preuves d'étape 2 (efficacité opérationnelle)

Preuves requises pour démontrer l'efficacité opérationnelle de ce cadre :

- **Inventaire des services en nuage** : Cahier ISMS-IMP-A.5.19-23.1 montrant l'inventaire complet avec classification des données, cotes de criticité, résidence et faisabilité de sortie
- **Dossiers de diligence raisonnable** : Cahier ISMS-IMP-A.5.19-23.2 documentant les évaluations, certifications révisées, réponses aux questionnaires de sécurité
- **Contrats signés avec clauses de sécurité** : Accords fournisseurs contenant les dispositions de sécurité requises (RGPD art. 28, droits d'audit, notification d'incident, dispositions de sortie)
- **Référentiels de configuration** : Cahier ISMS-IMP-A.5.19-23.3 montrant la conformité de configuration sécurisée par rapport aux benchmarks CIS
- **Comptes rendus des réunions de revue fournisseurs** : Documentation trimestrielle/semestrielle/annuelle montrant la performance SLA, le statut de conformité, le suivi des corrections
- **Dossiers de gouvernance continue** : Cahier ISMS-IMP-A.5.19-23.4 suivant les résultats de surveillance, la gestion des changements, l'historique des incidents, les évaluations des risques
- **Preuves de certification fournisseurs** : Certificats SOC 2 Type II, ISO 27001, CSA STAR en cours pour les fournisseurs critiques/à risque élevé (dans les 12 mois)
- **Rapports de performance SLA** : Rapports mensuels/trimestriels montrant la disponibilité, les délais de réponse du support, les indicateurs de résolution des incidents
- **Notifications d'incidents fournisseurs** : Incidents de sécurité documentés conformément aux exigences de notification contractuelles avec preuves de réponse
- **Dossiers de gestion des changements** : Changements de service approuvés, mises à jour de configuration, migrations et avenants contractuels
- **Résultats de tests des plans de sortie** : Validation annuelle de la stratégie de sortie démontrant la capacité d'export des données et la disponibilité pour la transition (DORA art. 28.6)
- **Évaluations du risque de concentration** : Analyse documentée des dépendances envers les fournisseurs critiques avec stratégies d'atténuation
- **Registre des exceptions** : Exceptions approuvées avec justification commerciale, contrôles compensatoires et validation du RSSI
- **Preuves réglementaires (le cas échéant)** :
  - DORA : Registre des risques liés aux TIC tiers, rapports du risque de concentration, dossiers de coopération avec l'autorité compétente
  - NIS2 : Rapports d'incidents 24 h/72 h/finaux au CSIRT, évaluation annuelle des risques de cybersécurité
  - Loi IA : Évaluations de conformité des systèmes d'IA à haut risque, documentation de transparence

---

**FIN DU DOCUMENT DE POLITIQUE**

---

*Cet index principal assure une gouvernance complète de la sécurité des fournisseurs et des services en nuage. Les exigences détaillées pour chaque contrôle sont documentées dans les sections S1-S6. Les outils d'évaluation et les orientations de mise en œuvre sont fournis dans la suite de documents ISMS-IMP-A.5.19-23.*

<!-- QA_VERIFIED: 2026-03-30 -->
