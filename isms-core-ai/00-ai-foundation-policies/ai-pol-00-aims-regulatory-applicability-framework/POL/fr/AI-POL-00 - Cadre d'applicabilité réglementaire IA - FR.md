<!-- ISMS-CORE:POLICY:AI-POL-00-FR:ai:POL:00 -->
**AI-POL-00 — Cadre d'applicabilité réglementaire IA**
**Référence faisant autorité pour les obligations de conformité du Système de Management de l'IA**

---

## Contrôle du document

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Cadre d'applicabilité réglementaire IA |
| **Type de document** | Politique |
| **Identifiant du document** | AI-POL-00 |
| **Auteur du document** | Responsable de la Gouvernance IA (RGIA) / Responsable de la Sécurité des Systèmes d'Information (RSSI) |
| **Propriétaire du document** | Directeur Général (DG) |
| **Approuvé par** | Direction générale |
| **Date de création** | [Date] |
| **Version** | 1.0 |
| **Date de version** | [À définir] |
| **Classification** | Interne |
| **Statut** | Brouillon |
| **Version du produit AIMS** | 1.0 |

**Historique des versions** :

| Version | Date | Auteur | Modifications |
|---------|------|--------|---------------|
| 0.1 | [Date - 8 sem.] | RGIA | Brouillon initial — cadre à trois niveaux, périmètre Règlement IA + ISO 42001 |
| 0.2 | [Date - 6 sem.] | RGIA + Juridique | Ajout des obligations sectorielles, positionnement ISO 42005:2025 |
| 0.3 | [Date - 4 sem.] | RSSI | Alignement avec la méthodologie ISMS-POL-00 ; contexte de la stratégie suisse IA |
| 0.4 | [Date - 2 sem.] | RGIA / Juridique / RSSI | Intégration des retours des parties prenantes ; section de veille réglementaire ajoutée |
| 1.0 | [Date] | RGIA / Juridique / RSSI | Première version approuvée |

**Cycle de révision** : Annuel (ou en cas de changements réglementaires significatifs en matière d'IA, de nouvelles publications normatives, ou de modifications du périmètre de certification)
**Prochaine date de révision** : [Date d'entrée en vigueur + 12 mois]

**Chaîne d'approbation** :

- Principale : Responsable de la Gouvernance IA (ou RSSI désigné en l'absence d'un rôle dédié de gouvernance IA)
- Secondaire : Responsable de la Sécurité des Systèmes d'Information (RSSI)
- Conformité : Responsable Juridique / Responsable de la Conformité
- Autorité finale : Direction générale

**Documents connexes** :

- AI-POL-01 — Cadre de gouvernance et de prise de décisions IA
- ISMS-POL-00 — Cadre d'applicabilité réglementaire (base SMSI — co-référence obligatoire)
- ISO/IEC 42001:2023 Clause 4.2 (Compréhension des besoins et attentes des parties intéressées)
- ISO/IEC 42001:2023 Clause 4.3 (Détermination du périmètre du Système de Management de l'IA)
- Tous les documents de politique AIMS (référence obligatoire)

**Distribution** : Tous les parties prenantes AIMS, responsables de la gouvernance IA, auteurs de politiques, propriétaires de systèmes IA, Juridique/Conformité, auditeurs
**Référencé par** : Tous les documents de politique AIMS (AI-POL-01, toutes les politiques de groupes de contrôle AI-POL-A.x.x)

**Stratégie linguistique** : Lorsque des termes techniques ou réglementaires sont établis à l'échelle internationale (ex. Règlement IA de l'UE, GPAI, ISO/IEC, AISIA, NIST AI RMF), la terminologie anglaise est conservée afin de préserver la précision et de faciliter les références réglementaires transfrontalières.

---

## Résumé exécutif

Ce document constitue la **référence faisant autorité** pour interpréter l'applicabilité des réglementations et cadres relatifs à l'IA dans l'ensemble du Système de Management de l'IA (AIMS).

**Objet** : Éliminer l'ambiguïté et les incohérences dans les références aux lois, réglementations et normes en matière d'IA dans l'ensemble de la documentation AIMS.

**Périmètre** : Toutes les références aux lois sur l'IA, réglementations sur l'IA et cadres de gouvernance IA dans la documentation AIMS.

**Relation avec le SMSI** : Cette politique est le complément spécifique à l'IA de **ISMS-POL-00** (Cadre d'applicabilité réglementaire). ISMS-POL-00 régit les obligations de sécurité de l'information. AI-POL-00 régit les obligations de management et de gouvernance de l'IA. Lorsque des obligations se chevauchent (ex. RGPD Article 22 — prise de décision automatisée, ou les exigences de sécurité du Règlement IA pour les systèmes IA à haut risque), ISMS-POL-00 prévaut pour la dimension sécurité de l'information ; AI-POL-00 régit la dimension gouvernance IA. Les obligations en matière de protection des données découlant du traitement de données personnelles par l'IA sont traitées conjointement avec PRIV-POL-00.

**Principe clé** : **L'applicabilité réglementaire en matière d'IA doit être explicite, non supposée.** Les références aux réglementations et cadres IA se répartissent en trois catégories :

1. **Conformité obligatoire** — Obligations légales applicables à l'organisation
2. **Applicabilité conditionnelle** — Exigences s'appliquant uniquement dans des circonstances spécifiques
3. **Référence informative** — Meilleures pratiques et orientations techniques

**Utilisation** : Toutes les politiques AIMS DOIVENT inclure une section « Cadre réglementaire » référençant ce document, identifiant à quel niveau appartient chaque réglementation ou norme citée.

**Termes clés** : Les définitions des termes utilisés dans cette politique sont fournies dans le **Glossaire** à la fin de ce document.

---

## Autorité et périmètre de la politique

### Objet et périmètre de cette politique

Cette politique définit **l'identification et l'applicabilité** des exigences légales, réglementaires et contractuelles applicables au Système de Management de l'IA de l'organisation.

**Cette politique établit :**

- Quelles lois et normes IA s'appliquent à l'organisation
- La catégorisation des obligations IA (Obligatoire, Conditionnel, Informatif)
- La méthodologie d'évaluation de l'applicabilité en fonction du rôle IA de l'organisation
- Les processus de révision et de mise à jour face aux évolutions du paysage réglementaire IA

**Cette politique n'établit PAS :**

- Les décisions de traitement des risques IA (traitées dans la gestion des risques AIMS)
- Les exigences d'implémentation des contrôles (traitées dans les politiques de groupes de contrôle et les IMP)
- Le statut de conformité ou de vérification (traité dans les processus de suivi de la conformité)
- Les obligations de sécurité de l'information (traitées dans ISMS-POL-00)
- Les obligations de protection des données pour le traitement IA de données personnelles (traitées dans PRIV-POL-00)

**Principe de délimitation** : Cette politique établit l'applicabilité réglementaire IA. La mise en œuvre, l'application et la vérification sont assurées par des processus AIMS distincts et les politiques de groupes de contrôle.

**Intégration avec ISO/IEC 42001:2023 :**

- **Clause 4.2 (Parties intéressées)** : Les exigences réglementaires en matière d'IA constituent les principales obligations envers les parties intéressées. Cette politique les identifie explicitement.
- **Clause 4.3 (Périmètre)** : La détermination du périmètre est conditionnée par les obligations de Niveau 1 applicables et le rôle IA de l'organisation (fournisseur, déployeur, ou les deux).
- **Clause 6 (Évaluation des risques)** : Les obligations réglementaires alimentent le registre des risques IA. Niveau 1 = priorité élevée, Niveau 2 conditionnel = priorité moyenne, Niveau 3 = contribution informative.

**Intégration avec ISMS-POL-00 et PRIV-POL-00 :**

Cette politique opère aux côtés de ISMS-POL-00 et PRIV-POL-00. Lorsqu'une réglementation IA a des dimensions de sécurité de l'information (ex. Règlement IA Article 15 — exactitude, robustesse et cybersécurité), ISMS-POL-00 régit l'interprétation sécurité. Lorsqu'une réglementation IA a des dimensions relatives à la vie privée (ex. RGPD Article 22 — prise de décision individuelle automatisée), PRIV-POL-00 régit l'interprétation protection des données. AI-POL-00 régit l'interprétation management et gouvernance IA.

---

## Détermination du rôle IA de l'organisation

**Cette étape doit être réalisée avant d'appliquer le cadre réglementaire.** Les obligations réglementaires en matière d'IA diffèrent significativement selon le rôle de l'organisation dans la chaîne de valeur IA.

### Rôles définis par le Règlement IA de l'UE (Règlement 2024/1689)

| Rôle | Définition | Obligations |
|------|-----------|-------------|
| **Fournisseur d'IA** | Développe un système d'IA ou un modèle d'IA à usage général avec intention de le mettre sur le marché ou de le mettre en service sous son propre nom ou marque, y compris par téléchargement | Niveau d'obligation le plus élevé — évaluation de la conformité, documentation technique, surveillance post-commercialisation |
| **Déployeur d'IA** | Utilise un système d'IA sous sa propre autorité à des fins professionnelles | Mettre en œuvre les instructions du fournisseur, réaliser une EIDF pour les systèmes IA à haut risque, conserver les journaux, assurer la surveillance humaine |
| **Importateur d'IA** | Met sur le marché de l'UE un système d'IA portant le nom d'une entité établie hors de l'UE | Vérifier la conformité, conserver la documentation, notifier aux autorités |
| **Distributeur d'IA** | Met à disposition sur le marché de l'UE un système d'IA, autrement que comme fournisseur ou importateur | Vérifier le marquage CE, la documentation, l'enregistrement |

### Rôles définis par ISO/IEC 42001:2023

| Rôle | Définition |
|------|-----------|
| **Fournisseur d'IA** | Développe, entraîne, déploie ou maintient des systèmes IA (pour usage interne ou externe) |
| **Utilisateur / Déployeur d'IA** | Intègre ou utilise des systèmes IA développés par des tiers |
| **Les deux** | La plupart des organisations — développe certaines capacités IA en interne tout en utilisant des outils IA tiers |

**Action requise** : L'organisation DOIT documenter son ou ses rôle(s) dans l'inventaire des systèmes IA (AI-POL-01) pour chaque système IA dans le périmètre. Les rôles peuvent différer selon le système IA.

---

## Catégories d'applicabilité réglementaire

**Conformité obligatoire**
Obligations légales ou contractuelles en matière d'IA auxquelles l'organisation DOIT se conformer. Le non-respect entraîne une responsabilité juridique, des amendes réglementaires, des enquêtes des autorités de surveillance, ou la perte de certification.

**Caractéristiques** :

- Exécutoire par une autorité réglementaire ou un tribunal
- Le non-respect entraîne des conséquences légales ou financières (amendes, injonctions, restrictions d'accès au marché)
- Requiert des preuves documentées de conformité (évaluations de conformité, documentation technique, registres d'incidents)
- Soumis aux audits, inspections et pouvoirs des autorités de surveillance réglementaires

**Applicabilité conditionnelle**
Exigences IA s'appliquant uniquement lorsque des conditions spécifiques sont remplies (ex. types de systèmes IA, exposition géographique au marché, certification recherchée, contrats clients, secteurs réglementés).

**Caractéristiques** :

- L'applicabilité dépend des caractéristiques du système IA, du contexte de déploiement ou de la géographie du marché
- Peut devenir obligatoire en fonction des activités commerciales ou des exigences contractuelles
- Requiert une réévaluation périodique à mesure que les activités et les systèmes IA évoluent

**Référence informative / Alignement sur les meilleures pratiques**
Cadres et normes utilisés pour des orientations techniques et organisationnelles, l'étalonnage ou l'alignement volontaire. Ils informent les pratiques de gouvernance IA mais ne constituent pas des exigences de conformité obligatoires.

**Caractéristiques** :

- Adoption volontaire pour les meilleures pratiques
- Aucun mécanisme d'application directe
- Utilisé pour des orientations d'implémentation IA responsable
- Peut devenir obligatoire si référencé dans des contrats ou des exigences de certification

---

## Hiérarchie de conformité

```
┌─────────────────────────────────────────────────────────────────────┐
│              HIÉRARCHIE DE CONFORMITÉ IA                            │
├─────────────────────────────────────────────────────────────────────┤
│  NIVEAU 1 : OBLIGATOIRE (Légal / Contractuel)                       │
│  • Règlement IA de l'UE (2024/1689) — lors de la mise sur le marché │
│    de l'UE ou de la mise en service de l'IA dans l'UE               │
│  • Obligations IA sectorielles (DORA, MiFID II, MDR, etc.)          │
│  • RGPD Article 22 — lorsque l'IA prend des décisions automatisées  │
│    sur des personnes avec des effets légaux ou significatifs         │
│                                                                     │
│  NIVEAU 2 : CONDITIONNEL (Dépendant du contexte)                    │
│  • ISO/IEC 42001:2023 — lorsque la certification est recherchée ou  │
│    contractuellement requise                                         │
│  • ISO/IEC 42005:2025 — méthodologie ÉISIA (complément à 42001,     │
│    applicable lorsque la certification 42001 est dans le périmètre) │
│  • Obligations d'évaluation de conformité pour les systèmes IA      │
│    à haut risque (lorsque classifiés sous l'Annexe III du Règl. IA) │
│  • Lois nationales sur l'IA dans les marchés où l'organisation opère│
│                                                                     │
│  NIVEAU 3 : INFORMATIF (Meilleures pratiques / Orientations)        │
│  • NIST AI Risk Management Framework 1.0 (NIST AI RMF)             │
│  • ISO/IEC 23894:2023 (Orientations sur la gestion des risques IA) │
│  • ISO/IEC 38507:2022 (Gouvernance de l'IA)                         │
│  • Principes de l'OCDE sur l'IA (2019, révisés 2024)               │
│  • Recommandation de l'UNESCO sur l'éthique de l'IA (2021)          │
│  • Stratégie IA du Conseil fédéral suisse (2023)                    │
│                                                                     │
│  À VENIR (Surveiller — Adopter dès publication / entrée en vigueur) │
│  • Législation nationale suisse sur l'IA (anticipée)                │
│  • ISO/IEC 42006 — orientations d'audit interne AIMS (en dév.)      │
│  • Directive UE sur la responsabilité civile IA (en dév.)           │
└─────────────────────────────────────────────────────────────────────┘
```

> *Si les caractères de dessin de cadre ne s'affichent pas correctement, référez-vous aux sections ci-dessous pour les définitions des niveaux.*

---

# Conformité obligatoire (Niveau 1)

> **Note sur la classification ISO/IEC 42001:2023** : ISO/IEC 42001:2023 est classifiée **Niveau 2 (Conditionnel)** dans ce cadre. Ce n'est pas une réglementation légalement exécutoire. Elle devient obligatoire pour [L'organisation] lorsque la certification est activement recherchée ou lorsqu'un contrat client requiert explicitement la conformité AIMS. Lorsqu'aucune de ces conditions n'est remplie, elle fonctionne comme un cadre de meilleures pratiques volontaire. Voir la section ISO/IEC 42001:2023 sous le Niveau 2 pour les détails complets.

## Règlement sur l'Intelligence Artificielle de l'UE (Règlement 2024/1689)

**Applicabilité** : Lors de la mise sur le marché de l'UE d'un système d'IA, de la mise en service d'un système d'IA dans l'UE, ou lorsque les résultats d'un système d'IA sont utilisés dans l'UE — indépendamment du lieu d'établissement de l'organisation. S'applique intégralement à partir du 2 août 2026 (avec les dispositions relatives aux pratiques d'IA interdites en vigueur depuis le 2 février 2025, les dispositions GPAI depuis le 2 août 2025).

**Cadre de classification des risques** :

Le Règlement IA de l'UE applique une approche basée sur les risques. Chaque système d'IA doit être classifié :

| Niveau de risque | Définition | Obligations |
|----------------|-----------|-------------|
| **Risque inacceptable** (Interdit) | Systèmes d'IA présentant une menace manifeste pour les droits fondamentaux ou la sécurité | Interdiction absolue — ne peut être mis sur le marché. Exemples : manipulation subliminale, notation sociale, identification biométrique à distance en temps réel dans les espaces publics (sauf exceptions étroites pour les forces de l'ordre), exploitation des vulnérabilités liées à l'âge ou au handicap |
| **Haut risque** (Annexe III) | Systèmes d'IA dans des secteurs réglementés ou ayant un impact significatif sur les droits fondamentaux | Obligations de conformité complètes — voir ci-dessous |
| **Risque limité** | Systèmes d'IA avec des obligations de transparence spécifiques | Informer les utilisateurs de l'interaction avec l'IA (chatbots, hypertrucages) |
| **Risque minimal** | Tous les autres systèmes d'IA | Pas d'exigences obligatoires ; codes de conduite volontaires |
| **IA à usage général (GPAI)** | Modèles d'IA aux capacités générales (ex. GML) | Transparence, conformité au droit d'auteur ; les modèles à risque systémique ont des obligations supplémentaires |

**Catégories de systèmes d'IA à haut risque (Annexe III)** :

- Identification biométrique et catégorisation
- Gestion et exploitation des infrastructures critiques
- Éducation et formation professionnelle (accès, évaluation)
- Emploi, gestion des travailleurs et accès au travail indépendant
- Accès et bénéfice des services privés et publics essentiels
- Application de la loi
- Gestion des migrations, de l'asile et du contrôle aux frontières
- Administration de la justice et processus démocratiques

**Exigences clés pour les fournisseurs d'IA à haut risque** :

- Article 9 : Système de management de la qualité (SMQ) incluant la gestion des risques
- Article 10 : Exigences relatives aux données d'entraînement, de validation et de test
- Article 11 : Documentation technique (avant mise sur le marché)
- Article 12 : Tenue de registres (journalisation pendant toute la durée de vie opérationnelle)
- Article 13 : Transparence et fourniture d'informations aux déployeurs
- Article 14 : Mesures de surveillance humaine
- Article 15 : Exigences d'exactitude, de robustesse et de cybersécurité
- Article 16 : Obligations des fournisseurs (enregistrement, marquage CE, surveillance post-commercialisation)
- Article 26 : Obligations des déployeurs (évaluation d'impact sur les droits fondamentaux pour les organismes publics et certains déployeurs privés)

**Exigences clés pour les fournisseurs de modèles GPAI** :

- Article 53 : Transparence et conformité au droit d'auteur (documentation technique, résumé des données d'entraînement)
- Article 55 : Modèles à risque systémique (tests adversariaux, signalement d'incidents, mesures de cybersécurité)

**Impact sur l'AIMS** :

- L'inventaire des systèmes IA doit classer chaque système selon la catégorie de risque du Règlement IA de l'UE
- Les systèmes à haut risque requièrent une évaluation de conformité avant la mise sur le marché de l'UE
- La documentation technique est maintenue conformément aux exigences de l'Article 11
- L'ÉISIA (A.5.2–A.5.5) est alignée avec l'Évaluation d'Impact sur les Droits Fondamentaux (EIDF) pour les systèmes IA à haut risque
- A.6.2.6 (opération et surveillance) doit traiter les obligations de surveillance post-commercialisation
- A.8.4 (communication des incidents) doit traiter les délais de signalement des incidents graves du Règlement IA de l'UE

**Autorité de surveillance** : Autorité nationale de surveillance du marché de chaque État membre de l'UE ; Bureau européen de l'IA (Commission européenne) pour les modèles GPAI

**Référence** : Règlement (UE) 2024/1689, Journal officiel de l'UE, 12 juillet 2024. Dates d'application : pratiques d'IA interdites depuis le 2 février 2025 ; dispositions GPAI depuis le 2 août 2025 ; application complète depuis le 2 août 2026.

---

## RGPD Article 22 — Prise de décision automatisée

**Applicabilité** : Lorsque l'organisation utilise des systèmes d'IA pour prendre des **décisions entièrement automatisées** qui produisent des **effets juridiques** ou **affectent significativement** des personnes (ex. scoring de crédit automatisé, présélection de recrutement automatisée, éligibilité automatisée aux prestations, détection de fraude automatisée entraînant un blocage de compte).

**Exigences clés** :

- Droit de ne pas faire l'objet de décisions entièrement automatisées ayant des effets juridiques ou significatifs (Article 22(1))
- Exceptions : consentement explicite, nécessité contractuelle, ou autorisé par le droit de l'Union ou d'un État membre — toutes requièrent des garanties
- Lorsque des exceptions s'appliquent : informer les personnes, mettre en œuvre une surveillance humaine significative, prévoir le droit de contester la décision et d'obtenir un réexamen humain
- AIPD requises pour les traitements automatisés systématiques susceptibles d'engendrer un risque élevé (Article 35)

**Impact sur l'AIMS** :

- Les systèmes IA prenant des décisions automatisées importantes doivent être identifiés dans l'inventaire des systèmes IA
- Contrôles de surveillance humaine obligatoires (A.6.2.6) pour les décisions pilotées par l'IA affectant des personnes
- Les divulgations de transparence (A.8.2, A.8.5) doivent traiter les obligations d'information de l'Article 22 du RGPD
- Lien vers PRIV-POL-00 et PRIV-POL-A.1.3.11 (Prise de décision automatisée) pour les obligations complètes de protection des données

**Autorité de surveillance** : Autorité de protection des données (APD) compétente de l'UE/EEE

**Référence** : Règlement (UE) 2016/679 Article 22 ; Lignes directrices 05/2020 sur la prise de décision automatisée et le profilage (EDPB)

---

## Obligations IA sectorielles

Certains secteurs réglementés imposent des obligations spécifiques à l'IA en complément du Règlement IA de l'UE. L'applicabilité dépend du secteur et des activités de l'organisation.

**Services financiers — DORA (Règlement 2022/2554)** :

- Articles 28–30 : La gestion des risques liés aux tiers en matière de TIC s'applique aux outils IA et aux fournisseurs de services IA
- DORA classe les outils IA utilisés dans des fonctions critiques comme des dépendances TIC tierces soumises aux obligations complètes de TPRM
- Les systèmes IA utilisés dans le trading, la gestion des risques ou les services clients entrent dans le périmètre de signalement des incidents TIC
- **Déclencheur d'applicabilité** : L'organisation est une entité réglementée par DORA (établissement financier, entreprise d'investissement, entreprise d'assurance, prestataire de services sur crypto-actifs, etc.)

**Dispositifs médicaux — MDR (Règlement 2017/745) et IVDR (Règlement 2017/746)** :

- Les dispositifs médicaux et dispositifs médicaux de diagnostic in vitro alimentés par l'IA sont soumis à l'évaluation de conformité MDR/IVDR
- Les logiciels de dispositifs médicaux IA (SaMD) peuvent être classifiés à haut risque à la fois sous le MDR et le Règlement IA — une double évaluation de conformité peut s'appliquer
- **Déclencheur d'applicabilité** : L'organisation développe ou met sur le marché des dispositifs médicaux ou des logiciels de diagnostic alimentés par l'IA

**Aviation, Automobile, Ferroviaire, Maritime (régimes de marquage CE)** :

- Les systèmes d'IA intégrés dans des produits à sécurité critique réglementés en vertu de la législation existante sur la sécurité des produits peuvent nécessiter une double conformité au titre du Règlement IA et de la réglementation sectorielle spécifique
- **Déclencheur d'applicabilité** : L'organisation développe des systèmes IA intégrés dans des produits à sécurité critique dans ces secteurs

**Action requise** : Juridique/Conformité DOIT évaluer annuellement les obligations IA sectorielles et documenter les conclusions d'applicabilité dans le registre réglementaire.

---

# Applicabilité conditionnelle (Niveau 2)

Ces réglementations et normes s'appliquent **uniquement lorsque des conditions spécifiques sont remplies**.

## ISO/IEC 42001:2023 — Système de Management de l'IA

**Norme** : ISO/IEC 42001:2023 (Première édition) — Technologies de l'information — Intelligence artificielle — Système de management

**Déclencheurs d'applicabilité** :

- L'organisation **recherche la certification ISO/IEC 42001:2023** (seule ou combinée avec la certification ISO 27001)
- Un contrat client **requiert explicitement** la conformité AIMS à cette norme
- L'organisation **adopte volontairement** ISO 42001 comme cadre de gouvernance IA (auquel cas traiter comme opérationnellement contraignant)

**Note de classification** : ISO/IEC 42001:2023 est classifiée Niveau 2 (Conditionnel) dans ce cadre. Ce n'est pas une réglementation légalement exécutoire. Elle ne devient pas obligatoire simplement parce que l'organisation développe ou utilise des systèmes IA — le Règlement IA de l'UE remplit ce rôle pour l'exposition au marché de l'UE. Lorsque la certification est recherchée ou contractuellement requise, elle est traitée comme un engagement opérationnel contraignant équivalent au Niveau 1 pour la durée de la certification.

**Exigences clés** :

- Clause 4 : Contexte de l'organisation (compréhension du contexte, parties intéressées, périmètre AIMS)
- Clause 5 : Leadership (politique IA, rôles et responsabilités, engagement de la direction)
- Clause 6 : Planification (évaluation des risques IA, évaluation d'impact des systèmes IA, objectifs IA)
- Clause 7 : Support (ressources, compétences, sensibilisation, communication, informations documentées)
- Clause 8 : Opérations (planification opérationnelle, exécution de l'évaluation des risques IA, traitement des risques, exécution de l'ÉISIA)
- Clause 9 : Évaluation des performances (surveillance, audit interne, revue de direction)
- Clause 10 : Amélioration (non-conformité, action corrective, amélioration continue)
- Annexe A (normative) : 36 contrôles dans 9 domaines (A.2–A.10)
- Annexe B (normative) : Orientations de mise en œuvre pour tous les contrôles de l'Annexe A

**Déploiement AIMS** : L'ensemble des contrôles de l'Annexe A d'ISO 42001 est déployé à travers les politiques de groupes de contrôle AI-POL-A.x.x dans `53-isms-core-ai/`. La Déclaration d'applicabilité (DDA) de l'organisation DOIT référencer ces politiques.

**Intégration avec ISO 27001** : ISO 42001 utilise la même structure de haut niveau (HLS/Annexe SL) qu'ISO 27001:2022. Les organisations certifiées ISO 27001 peuvent intégrer ou combiner les processus AIMS et SMSI dans un système de management partagé. Les domaines de clause partagés (7, 9, 10) peuvent réutiliser l'infrastructure SMSI existante.

**Référence** : ISO/IEC 42001:2023, Technologies de l'information — Intelligence artificielle — Système de management, décembre 2023

---

## ISO/IEC 42005:2025 — Évaluation d'impact des systèmes d'IA

**Norme** : ISO/IEC 42005:2025 (Première édition) — Technologies de l'information — Intelligence artificielle — Évaluation d'impact des systèmes d'IA

**Déclencheurs d'applicabilité** :

- ISO/IEC 42001:2023 est dans le périmètre (le déclencheur de Niveau 2 ci-dessus s'applique) — ISO 42005:2025 fournit la méthodologie pour la Clause 6.1.4 d'ISO 42001 (évaluation d'impact des systèmes IA) et les contrôles A.5.2–A.5.5 de l'Annexe A
- L'organisation adopte formellement l'ÉISIA dans le cadre de son programme de gouvernance IA
- Des contrats clients ou des obligations réglementaires (ex. exigences EIDF du Règlement IA de l'UE) requièrent une méthodologie documentée d'évaluation d'impact IA

**Ce que couvre ISO 42005:2025** :

- Clause 5 : Développement et mise en œuvre du processus ÉISIA (périmètre, seuils, usages sensibles, usages restreints, échelles d'impact, responsabilités, approbation, surveillance et révision)
- Clause 6 : Documentation de l'évaluation d'impact des systèmes IA (description du système IA, fonctionnalités et capacités, usage prévu, informations sur les données et qualité, informations sur les algorithmes et modèles, environnement de déploiement, parties intéressées, impacts réels et raisonnablement prévisibles, bénéfices et préjudices, mesures pour traiter les préjudices)
- Annexe A (informative) : Orientations pour l'utilisation avec ISO/IEC 42001
- Annexe B (informative) : Orientations pour l'utilisation avec ISO/IEC 23894 (gestion des risques IA)

**Impact sur l'AIMS** :

- Tous les modèles ÉISIA dans `53-isms-core-ai/` DOIVENT être construits conformément aux exigences de documentation de la Clause 6 d'ISO 42005:2025
- La méthodologie ÉISIA dans les documents AIMS doit référencer ISO 42005:2025, non des orientations génériques
- L'ÉISIA d'ISO 42005:2025 est alignée avec l'Évaluation d'Impact sur les Droits Fondamentaux (EIDF) du Règlement IA de l'UE — les organisations soumises aux deux DOIVENT documenter la cross-référence

**Référence** : ISO/IEC 42005:2025, Technologies de l'information — Intelligence artificielle — Évaluation d'impact des systèmes d'IA, mai 2025

---

## Évaluation de conformité des systèmes IA à haut risque (Règlement IA de l'UE)

**Déclencheur d'applicabilité** : L'organisation agit en tant que fournisseur ou déployeur d'IA pour un système d'IA classifié **à haut risque** en vertu de l'Annexe III du Règlement IA de l'UE.

**Obligations supplémentaires déclenchées** :

- Procédure d'évaluation de conformité (Article 43) — soit contrôle interne, soit évaluation tierce (organisme notifié) selon la catégorie du système IA
- Enregistrement dans la base de données du Règlement IA de l'UE (Article 49) avant la mise sur le marché
- Marquage CE et déclaration de conformité
- Système de surveillance post-commercialisation (Article 72)
- Signalement des incidents graves à l'autorité nationale (Article 73) dans les délais définis

**Action requise** : Pour chaque système IA dans le périmètre du marché de l'UE, classifier selon les catégories de risque du Règlement IA et documenter dans l'inventaire des systèmes IA. La classification à haut risque déclenche la planification de l'évaluation de conformité.

---

# Référence informative (Niveau 3)

Ces cadres informent les pratiques de gouvernance IA mais ne constituent pas des exigences de conformité obligatoires. Ils sont utilisés pour l'orientation, l'étalonnage et la mise en œuvre des meilleures pratiques.

## NIST AI Risk Management Framework 1.0 (NIST AI RMF)

**Publié** : Janvier 2023 — National Institute of Standards and Technology (États-Unis)

**Pertinence** : Fournit un cadre volontaire pour la gestion des risques IA selon quatre fonctions principales : GOUVERNER (GOVERN), CARTOGRAPHIER (MAP), MESURER (MEASURE), GÉRER (MANAGE). Reconnu internationalement comme référence pratique de gestion des risques IA, y compris hors des États-Unis.

**Utilisation dans l'AIMS** :

- La structure du registre des risques IA est informée par la taxonomie des risques NIST AI RMF (GOVERN, MAP, MEASURE, MANAGE)
- Le concept de profil NIST AI RMF soutient la priorisation des risques IA spécifique à l'organisation
- La correspondance NIST AI RMF ↔ ISO 42001 assiste les organisations utilisant les deux cadres

**Référence** : NIST AI RMF 1.0, NIST AI 100-1, janvier 2023

---

## ISO/IEC 23894:2023 — Gestion des risques IA

**Publié** : Février 2023

**Pertinence** : Fournit des orientations sur la façon dont les organisations peuvent gérer les risques liés spécifiquement à l'IA. Étend ISO 31000 (gestion des risques) avec des considérations spécifiques à l'IA. Référencé par l'Annexe B d'ISO 42001 et l'Annexe B d'ISO 42005.

**Utilisation dans l'AIMS** :

- La méthodologie d'évaluation des risques IA est informée par les orientations d'identification et d'analyse des risques d'ISO 23894
- La taxonomie des risques IA est informée par les catégories d'ISO 23894 (technique, opérationnel, sociétal)

**Référence** : ISO/IEC 23894:2023, Technologies de l'information — Intelligence artificielle — Orientations sur la gestion des risques

---

## ISO/IEC 38507:2022 — Gouvernance de l'IA pour les organisations

**Publié** : Avril 2022

**Pertinence** : Fournit des orientations sur les implications de gouvernance de l'utilisation de l'IA par les organisations. Aborde la manière dont les membres des organes de gouvernance peuvent permettre, étendre et faire évoluer la gouvernance IA. Référencé dans l'Annexe B.2.3 d'ISO 42001.

**Utilisation dans l'AIMS** :

- La structure de gouvernance pour l'IA (A.3.2) est informée par les orientations de gouvernance IA au niveau du conseil d'administration d'ISO 38507
- Le cadre de responsabilisation de la direction est aligné avec les principes d'ISO 38507

**Référence** : ISO/IEC 38507:2022, Technologies de l'information — Intelligence artificielle — Implications de gouvernance de l'utilisation de l'IA par les organisations

---

## Principes de l'OCDE sur l'IA (2019, révisés 2024)

**Publiés** : Mai 2019 (révisés en juin 2024) — Organisation de Coopération et de Développement Économiques

**Pertinence** : Référence internationale pour une IA responsable. Adoptés par le G20. Largement référencés dans la législation nationale sur l'IA, y compris le Règlement IA de l'UE. Cinq principes : croissance inclusive et bien-être ; valeurs centrées sur l'humain et équité ; transparence et explicabilité ; robustesse et sécurité ; responsabilité.

**Utilisation dans l'AIMS** :

- Les principes d'IA responsable d'AI-POL-01 sont alignés avec les Principes de l'OCDE sur l'IA
- Les considérants du Règlement IA de l'UE référencent les Principes de l'OCDE — l'alignement réduit les lacunes d'interprétation

**Référence** : Principes de l'OCDE sur l'IA, OECD/LEGAL/0449, adoptés le 22 mai 2019, révisés en 2024

---

## Stratégie IA du Conseil fédéral suisse (2023)

**Publiée** : Décembre 2023 — Conseil fédéral suisse

**Pertinence** : La stratégie IA gouvernementale de la Suisse expose les principes d'IA responsable pour l'administration publique et indique la direction pour la future législation suisse sur l'IA. Non contraignante pour le secteur privé en date d'avril 2026.

**Contexte suisse** : La Suisse n'a pas adopté de loi nationale autonome sur l'IA en date d'avril 2026. La gouvernance IA pour les organisations du secteur privé est principalement traitée par :

- nDSG suisse (Loi fédérale sur la protection des données, RS 235.1) — s'applique au traitement IA de données personnelles
- ISG suisse (Loi fédérale sur la sécurité de l'information, RS 128) — s'applique aux systèmes IA dans les infrastructures critiques nationales
- Stratégie IA du Conseil fédéral suisse — principes volontaires
- Règlement IA de l'UE — s'applique aux organisations suisses mettant des systèmes IA sur le marché de l'UE

**Surveiller** : La législation nationale suisse sur l'IA est anticipée en suivant le cadre du Règlement IA de l'UE. Attribuer la responsabilité de la veille à Juridique/Conformité.

---

# À venir (Surveiller — Adopter dès publication ou entrée en vigueur)

Ces instruments sont en cours d'élaboration ou anticipés. [L'organisation] DOIT surveiller et adopter lors de leur publication ou entrée en vigueur.

| Instrument | Statut | Impact attendu |
|-----------|--------|----------------|
| **Législation nationale suisse sur l'IA** | Anticipée — aucun projet publié en avril 2026 | Susceptible de s'aligner sur le Règlement IA de l'UE pour les systèmes IA du marché suisse ; l'AIMS est déjà aligné |
| **ISO/IEC 42006** — Exigences pour l'audit des systèmes de management de l'IA | En cours d'élaboration (ISO/IEC JTC 1/SC 42) | Définira les exigences d'audit AIMS interne/externe — mettre à jour le programme d'audit AIMS lors de la publication |
| **Directive UE sur la responsabilité civile IA** | En cours d'élaboration | Peut imposer une responsabilité civile pour les préjudices causés par les systèmes IA ; déclenche des mises à jour du registre des risques AIMS |
| **Actes délégués du Règlement IA de l'UE** | Attendus 2025–2026 | Détails techniques pour l'évaluation de conformité, mandats de normalisation, seuils pour les modèles GPAI |
| **NIST AI RMF 2.0 / profils sectoriels** | Attendus périodiquement | Mettre à jour la référence NIST AI RMF Niveau 3 lors de la publication |

**Responsabilité de surveillance** : Responsable Juridique/Conformité, avec le soutien du Responsable de la Gouvernance IA (RGIA). Cycle de révision : veille trimestrielle, mise à jour annuelle de la politique si nécessaire.

---

# Processus d'évaluation et de révision

## Détermination de l'applicabilité

Pour chaque nouveau système d'IA développé ou acquis, et à chaque cycle de révision annuel, le Responsable de la Gouvernance IA (RGIA) et Juridique/Conformité DOIVENT :

1. **Identifier le rôle IA de l'organisation** pour le système (fournisseur, déployeur, les deux) selon les définitions de rôles ci-dessus
2. **Évaluer l'applicabilité du Niveau 1** — classification des risques selon le Règlement IA de l'UE ; déclencheur de l'Article 22 du RGPD ; déclencheurs sectoriels
3. **Évaluer les déclencheurs du Niveau 2** — La certification ISO 42001 est-elle recherchée ou contractuellement requise ? Le système est-il à haut risque selon le Règlement IA de l'UE, requérant une évaluation de conformité ?
4. **Examiner la pertinence du Niveau 3** — Documenter quels cadres informatifs informent la mise en œuvre pour le système
5. **Mettre à jour l'inventaire des systèmes IA** (AI-POL-01) avec les conclusions de classification réglementaire
6. **Mettre à jour la DDA AIMS** si de nouvelles obligations affectent la sélection des contrôles

## Révision annuelle

Cette politique DOIT être révisée annuellement par le Responsable de la Gouvernance IA et Juridique/Conformité. Déclencheurs pour une révision hors cycle :

- Nouvelle réglementation IA adoptée dans une juridiction où l'organisation opère
- Nouvelle norme IA publiée affectant le cadre de contrôle AIMS
- Changement significatif dans le portefeuille IA de l'organisation (nouveau système IA dans une catégorie à haut risque)
- Action d'application réglementaire contre une organisation similaire révélant une nouvelle interprétation des obligations

---

# Glossaire

| Terme | Définition |
|-------|-----------|
| **Règlement IA** | Règlement sur l'Intelligence Artificielle de l'UE — Règlement (UE) 2024/1689 sur l'intelligence artificielle |
| **Déployeur d'IA** | Personne physique ou morale utilisant un système d'IA sous sa propre autorité à des fins professionnelles (définition du Règlement IA de l'UE) |
| **Fournisseur d'IA** | Personne ou entité développant un système d'IA ou un modèle GPAI avec intention de le mettre sur le marché de l'UE (définition du Règlement IA de l'UE) |
| **Système d'IA** | Système basé sur la machine conçu pour fonctionner avec des niveaux variables d'autonomie, susceptible de faire preuve d'adaptabilité, et qui — pour des objectifs explicites ou implicites — déduit, à partir des données reçues, comment générer des sorties telles que des prédictions, du contenu, des recommandations ou des décisions (définition ISO/IEC 42001:2023, alignée avec l'Article 3 du Règlement IA de l'UE) |
| **AIMS** | Système de Management de l'IA — système de management pour le développement, le déploiement et l'utilisation responsables des systèmes d'IA |
| **ÉISIA** | Évaluation d'Impact du Système d'IA — évaluation formelle des conséquences potentielles d'un système d'IA pour les individus et les sociétés (ISO/IEC 42001:2023 Clause 6.1.4 ; détaillée dans ISO/IEC 42005:2025) |
| **EIDF** | Évaluation d'Impact sur les Droits Fondamentaux — requise en vertu de l'Article 26 du Règlement IA de l'UE pour les déployeurs de certains systèmes IA à haut risque affectant des personnes physiques |
| **GPAI** | IA à usage général — modèle d'IA entraîné sur de vastes données, capable de servir plusieurs tâches (ex. grands modèles de langage) ; soumis à des obligations spécifiques en vertu du Titre V du Règlement IA de l'UE |
| **IA à haut risque** | Système d'IA relevant des catégories de l'Annexe III du Règlement IA de l'UE, soumis aux obligations complètes de conformité avant la mise sur le marché de l'UE |
| **Obligatoire** | Niveau 1 — obligation légalement ou contractuellement exécutoire avec des conséquences en cas de non-conformité |
| **Conditionnel** | Niveau 2 — obligation devenant applicable lorsque des déclencheurs spécifiques sont remplis |
| **Informatif** | Niveau 3 — cadre de meilleures pratiques volontaire informant la mise en œuvre de l'AIMS sans application directe |
| **DDA** | Déclaration d'applicabilité — document listant les 36 contrôles de l'Annexe A d'ISO 42001 avec les décisions d'applicabilité et les justifications |
| **Risque systémique** | Risque associé aux modèles GPAI avec une très haute puissance de calcul d'entraînement (≥10^25 FLOPs) présentant des effets néfastes à l'échelle de l'UE |

---

<!-- QA_VERIFIED: 2026-04-15 -->
