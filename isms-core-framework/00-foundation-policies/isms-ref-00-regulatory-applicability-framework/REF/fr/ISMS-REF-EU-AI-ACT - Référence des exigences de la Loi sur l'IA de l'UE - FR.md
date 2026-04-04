<!-- ISMS-CORE:REF:ISMS-REF-EU-AI-ACT-FR-eu-ai-act-requirements-reference:framework:REF:eu-ai-act -->
**ISMS-REF-EU-AI-ACT — Référence des exigences de la Loi sur l'IA de l'UE**
**Exigences de gestion des risques et de conformité des systèmes d'IA de l'UE (Référence technique non-SMSI)**

---

**Contrôle documentaire**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Référence des exigences de la Loi sur l'IA de l'UE |
| **Type de document** | Interne — Référence technique (hors SMSI) |
| **Identifiant du document** | ISMS-REF-EU-AI-ACT |
| **Créateur du document** | Responsable de la Sécurité des Systèmes d'Information (RSSI) |
| **Propriétaire du document** | Président-Directeur Général (PDG) |
| **Approuvé par** | RSSI (Référence technique — aucune approbation de la direction requise) |
| **Date de création** | [Date] |
| **Version** | 1.0 |
| **Date de version** | [À déterminer] |
| **Classification** | Interne |
| **Statut** | Brouillon |

**Historique des versions** :

| Version | Date | Auteur | Modifications |
|---------|------|--------|--------------|
| 1.0 | [Date] | RSSI / Équipe de gouvernance IA | Référence technique initiale pour la Loi sur l'IA de l'UE (Règlement 2024/1689) |

**Cycle de révision** : Semestriel (mise en œuvre du Règlement IA en évolution rapide)
**Prochaine date de révision** : [Date + 6 mois]
**Approbateurs** : RSSI / Juridique/Conformité / Délégué à la Protection des Données (référence technique, aucune approbation SMSI requise)

**Distribution** : Équipes de développement IA/ML, Gestion des produits, Juridique, RSSI, DPD (pour les organisations développant ou déployant des systèmes d'IA)

---

⚠️ **IMPORTANT — DOCUMENT DE SUPPORT TECHNIQUE NON-SMSI**

Ce document est fourni à titre d'information et de sensibilisation uniquement.

- Ce document ne fait PAS partie du Système de Management de la Sécurité de l'Information (SMSI).
- Ce document ne définit PAS d'exigences obligatoires, sauf si [Organisation] développe ou déploie des systèmes d'IA affectant des personnes dans l'UE.
- Ce document n'établit PAS d'exigences contraignantes, de délais, de KPI ou de SLA pour les organisations non soumises au Règlement IA.
- Ce document n'impose PAS l'adoption des exigences de la Loi sur l'IA de l'UE pour les organisations non soumises au règlement.
- Ce document ne remplace ni n'étend aucune politique SMSI.

**Détermination de l'applicabilité** :
Les exigences de la Loi sur l'IA de l'UE s'appliquent UNIQUEMENT SI [Organisation] :

- Est un fournisseur (développe ou met sur le marché de l'UE des systèmes d'IA)
- Est un déployeur (utilise des systèmes d'IA sous sa propre autorité dans l'UE)
- Est un importateur ou distributeur de systèmes d'IA dans l'UE
- Développe/déploie des systèmes d'IA dont les résultats affectent des personnes situées dans l'UE (application extraterritoriale)

Pour toutes les autres organisations, ce document sert uniquement de :

- Référence technique sur les exigences potentielles du Règlement IA
- Contexte pour une expansion commerciale vers le développement/déploiement d'IA
- Sensibilisation au paysage réglementaire de l'IA dans l'UE
- **Ce document ne doit pas être utilisé comme preuve d'audit, sauf si [Organisation] est soumise au Règlement IA**

L'utilisation de ce document n'implique pas l'applicabilité du Règlement IA, d'obligations de conformité, ni un statut de développement/déploiement de systèmes d'IA.

**Déclaration de positionnement critique** :
Ce document fournit intentionnellement un niveau de détail réglementaire supérieur à ce qui s'applique à la plupart des organisations. Son objectif est uniquement de sensibiliser les organisations susceptibles de devenir soumises à la Loi sur l'IA de l'UE lors du développement ou du déploiement de systèmes d'IA, ou qui fournissent des services à des fournisseurs/déployeurs de systèmes d'IA. Aucune conclusion d'audit ne doit être tirée de la présence, de l'absence ou du statut de mise en œuvre de toute exigence du Règlement IA mentionnée ici, sauf si [Organisation] développe ou déploie explicitement des systèmes d'IA affectant des personnes dans l'UE.

---

# Objet et périmètre du document

## Objet

Ce document fournit une vue d'ensemble technique des exigences de la Loi sur l'IA de l'UE (Règlement (UE) 2024/1689). Il est destiné à soutenir :

- La sensibilisation aux exigences du Règlement IA pour les fournisseurs et déployeurs de systèmes d'IA
- La compréhension de la classification fondée sur les risques (Inacceptable, Haut risque, Risque limité, Risque minimal)
- Le contexte pour les organisations envisageant le développement ou le déploiement d'IA
- L'évaluation future potentielle de l'applicabilité
- La mise en correspondance des exigences du Règlement IA avec les contrôles ISO 27001:2022

## Ce que ce document n'est PAS

Ce document ne :

- N'établit pas d'exigences obligatoires pour les organisations non soumises à l'IA
- Ne définit pas les obligations de conformité de [Organisation] (voir POL-00 pour l'applicabilité réglementaire)
- Ne crée pas de critères d'audit, sauf si [Organisation] développe/déploie des systèmes d'IA
- Ne remplace pas l'interprétation de conseillers juridiques ou de conformité
- Ne constitue pas un conseil juridique sur la conformité au Règlement IA de l'UE
- Ne couvre pas tous les actes délégués et actes d'exécution (nombreux encore en cours d'élaboration)
- N'établit pas de procédures de développement ou de déploiement d'IA

## Relation avec le SMSI

Ce document est une **référence technique non contraignante**, SAUF si [Organisation] développe ou déploie des systèmes d'IA affectant des personnes dans l'UE (tel que déterminé dans ISMS-POL-00 Section 3.X — Loi sur l'IA de l'UE).

**Si [Organisation] développe/déploie des systèmes d'IA affectant l'UE :**

- Les exigences du Règlement IA deviennent de Niveau 1 (Conformité obligatoire) selon POL-00
- Ce document fournit des orientations de mise en œuvre
- Les contrôles SMSI doivent soutenir la conformité au Règlement IA (gestion des risques, gouvernance des données, journalisation, surveillance humaine)
- Une évaluation de la conformité est requise pour les systèmes d'IA à haut risque

**Si [Organisation] ne développe/déploie PAS de systèmes d'IA :**

- Le Règlement IA reste de Niveau 3 (Référence informative) selon POL-00
- Ce document est fourni à titre de sensibilisation uniquement
- Aucune obligation de conformité au Règlement IA n'existe
- Les contrôles SMSI suivent uniquement ISO 27001:2022

## Organisation du contenu

Cette référence organise les exigences du Règlement IA selon :

- Le système de classification fondée sur les risques (Inacceptable, Haut risque, Risque limité, Risque minimal)
- Les obligations des fournisseurs (développeurs, fabricants)
- Les obligations des déployeurs (utilisateurs de systèmes d'IA)
- Le calendrier de mise en œuvre par phases (2025–2027)
- Les exigences relatives aux modèles d'IA à usage général (MIAG)
- La mise en correspondance avec ISO 27001:2022 et les normes connexes
- Les exigences organisationnelles et de gouvernance

---

# Vue d'ensemble et applicabilité du Règlement IA de l'UE

## Qu'est-ce que la Loi sur l'IA de l'UE ?

**Règlement (UE) 2024/1689** établissant des règles harmonisées sur l'intelligence artificielle (Loi sur l'intelligence artificielle).

**Dates clés** :

- **Adoption** : 21 mai 2024 (Parlement européen)
- **Entrée en vigueur** : 1er août 2024 (20 jours après publication au Journal officiel)
- **Mise en œuvre par phases** : 2025–2027 (voir Section 2.6)

**Objet** :

- Établir des règles harmonisées pour le développement et le déploiement de l'IA dans l'UE
- Approche réglementaire fondée sur les risques (proportionnelle aux risques du système d'IA)
- Protéger les droits fondamentaux, la santé, la sécurité et la démocratie
- Favoriser l'innovation en IA digne de confiance
- Renforcer la position concurrentielle de l'UE dans le domaine de l'IA

**Base juridique** : Règlement de l'UE (directement applicable dans tous les États membres, aucune transposition nationale requise)

**Application extraterritoriale** : S'applique aux fournisseurs/déployeurs hors UE si les systèmes d'IA affectent des personnes dans l'UE.

## Définitions clés

**Système d'IA** (Article 3(1)) :
Système basé sur des machines, conçu pour fonctionner avec des niveaux variables d'autonomie et pouvant présenter une capacité d'adaptation après son déploiement, et qui, pour des objectifs explicites ou implicites, déduit, à partir des données en entrée qu'il reçoit, comment générer des résultats tels que des prédictions, du contenu, des recommandations ou des décisions susceptibles d'influencer des environnements physiques ou virtuels.

**Fournisseur** (Article 3(3)) :
Toute personne physique ou morale, toute autorité publique, tout organisme ou autre entité qui développe un système d'IA ou un modèle d'IA à usage général, ou qui fait développer un système d'IA ou un modèle d'IA à usage général et le commercialise ou le met en service sous son propre nom ou sa propre marque, à titre onéreux ou gratuit.

**Déployeur** (Article 3(4)) :
Toute personne physique ou morale, toute autorité publique, tout organisme ou autre entité utilisant un système d'IA sous sa propre autorité, à l'exception des cas où le système d'IA est utilisé dans le cadre d'une activité personnelle et non professionnelle.

**Modèle d'IA à usage général (MIAG)** (Article 3(44)) :
Modèle d'IA, notamment entraîné avec de grandes quantités de données par auto-supervision à grande échelle, qui présente une généralité significative et est capable d'exécuter de manière compétente un large éventail de tâches distinctes, indépendamment de la manière dont le modèle est mis sur le marché, et qui peut être intégré dans une variété de systèmes ou d'applications en aval, à l'exception des modèles d'IA utilisés pour des activités de recherche, de développement ou de prototypage avant leur mise sur le marché.

## Champ d'application (Article 2)

**Le Règlement IA s'applique à** :

| Acteur | Périmètre géographique | Conditions |
|--------|------------------------|------------|
| **Fournisseurs** | Mise sur le marché de l'UE OU mise en service dans l'UE | Indépendamment de la localisation du fournisseur |
| **Fournisseurs** | Localisés dans un pays tiers | Si les résultats du système d'IA sont utilisés dans l'UE |
| **Déployeurs** | Localisés dans l'UE | Utilisant des systèmes d'IA |
| **Déployeurs** | Localisés dans un pays tiers | Si les résultats du système d'IA sont utilisés dans l'UE |
| **Importateurs et distributeurs** | Dans l'UE | Distribuant des systèmes d'IA |
| **Fabricants de produits** | Dans l'UE | Mettant sur le marché des produits intégrant de l'IA |
| **Représentants autorisés** | Des fournisseurs hors UE | Agissant au nom de fournisseurs non établis dans l'UE |

**Exclusions** (Article 2(3)) :

- Systèmes d'IA développés ou utilisés exclusivement à des fins militaires, de défense ou de sécurité nationale
- Systèmes d'IA développés ou utilisés exclusivement pour des activités de recherche, de développement ou de prototypage avant la mise sur le marché
- Usage personnel et non professionnel

## Classification fondée sur les risques

Le Règlement IA adopte une **pyramide des risques à quatre niveaux** :

```
                   ┌──────────────────┐
                   │   INACCEPTABLE   │
                   │    INTERDIT      │
                   └──────────────────┘
                        (Article 5)

              ┌────────────────────────────┐
              │       HAUT RISQUE          │
              │  (Exigences strictes)      │
              └────────────────────────────┘
                   (Annexe III + Article 6)

        ┌────────────────────────────────────────┐
        │         RISQUE LIMITÉ                  │
        │   (Obligations de transparence)        │
        └────────────────────────────────────────┘
                     (Article 50)

   ┌──────────────────────────────────────────────────┐
   │              RISQUE MINIMAL                      │
   │    (Aucune obligation — Codes volontaires)       │
   └──────────────────────────────────────────────────┘
                     (La majorité des systèmes d'IA)
```

## Détermination de la classification des risques d'un système d'IA

**Étape 1** : Le système d'IA est-il interdit ? (Article 5 — Risque inacceptable)

**Étape 2** : Le système d'IA relève-t-il d'une catégorie à haut risque ?

- Est-il listé à l'Annexe III ? OU
- Est-il un composant de sécurité d'un produit couvert par la législation d'harmonisation de l'UE (Annexe I) ?

**Étape 3** : Le système d'IA est-il soumis à des exigences de transparence ? (Article 50 — Risque limité)

**Étape 4** : Si aucune des conditions ci-dessus n'est remplie, le risque est minimal (aucune exigence spécifique)

## Calendrier de mise en œuvre par phases

| Catégorie d'exigences | Date d'effet | Statut |
|-----------------------|-------------|--------|
| **Pratiques d'IA interdites** (Article 5) | 2 février 2025 | 6 mois après l'entrée en vigueur |
| **Modèles d'IA à usage général** (Chapitre V) | 2 août 2025 | 12 mois après l'entrée en vigueur |
| **Systèmes d'IA à haut risque** (Chapitre III, Section 2) | 2 août 2026 | 24 mois après l'entrée en vigueur |
| **IA à haut risque dans les produits réglementés** | 2 août 2027 | 36 mois après l'entrée en vigueur |
| **Bureau IA de l'UE, structure de gouvernance** | Immédiat | Août 2024 |

**Période de grâce pour les systèmes existants** :
Les systèmes d'IA déjà mis sur le marché ou mis en service avant le 2 août 2026 peuvent continuer à être utilisés jusqu'au 2 août 2030 sans mise en conformité (sauf en cas de modification substantielle).

---

# Pratiques d'IA à risque inacceptable (Article 5) — INTERDITES

## Vue d'ensemble

Certaines pratiques d'IA sont **interdites** en raison des risques inacceptables qu'elles font peser sur les droits fondamentaux, la sécurité ou la démocratie.

**Date d'effet** : 2 février 2025

**Sanction en cas de violation** : jusqu'à 35 millions d'euros ou 7 % du chiffre d'affaires annuel mondial (le montant le plus élevé étant retenu)

## Pratiques interdites

**Article 5(1)(a) : Manipulation subliminale**

- Systèmes d'IA déployant des techniques subliminales en dehors du champ de conscience de la personne
- Objectif : Altérer matériellement le comportement d'une manière causant ou susceptible de causer un préjudice significatif
- Exemples : Messages cachés, publicité subliminale ciblant des populations vulnérables

**Article 5(1)(b) : Exploitation des vulnérabilités**

- Systèmes d'IA exploitant les vulnérabilités de groupes spécifiques (âge, handicap, situation sociale/économique)
- Objectif : Altérer matériellement le comportement causant un préjudice significatif
- Exemples : Ciblage prédateur d'enfants, de personnes âgées ou de personnes en difficulté économique

**Article 5(1)(c) : Notation sociale**

- Systèmes d'IA évaluant ou classifiant des personnes physiques sur la base de leur comportement social ou de leurs caractéristiques personnelles/de personnalité
- Résultats : Traitement préjudiciable ou défavorable dans des contextes sans rapport avec la collecte initiale des données OU injustifié/disproportionné par rapport au comportement social
- Exemples : Systèmes de crédit social gouvernementaux, notation sociale généralisée par les employeurs

**Article 5(1)(d) : Évaluation du risque de délinquance**

- Systèmes d'IA évaluant ou prédisant le risque qu'une personne physique commette une infraction pénale
- Fondés uniquement sur le profilage ou les traits de personnalité
- Exception : Fondés sur des faits objectifs et vérifiables directement liés à une activité criminelle
- Exemples : Policing prédictif basé uniquement sur des données démographiques

**Article 5(1)(e) : Collecte massive d'images faciales**

- Collecte non ciblée d'images faciales sur Internet ou via des systèmes de vidéosurveillance (CCTV)
- Objectif : Créer ou enrichir des bases de données de reconnaissance faciale
- Exemples : Collecte massive de photos sur les réseaux sociaux

**Article 5(1)(f) : Reconnaissance des émotions sur le lieu de travail/dans l'enseignement**

- Systèmes d'IA inférant des émotions sur le lieu de travail ou dans des établissements d'enseignement
- Exception : Raisons médicales ou de sécurité
- Exemples : Surveillance de la productivité des employés via la détection des émotions (interdit sauf à des fins de sécurité/médicales)

**Article 5(1)(g) : Catégorisation biométrique**

- Systèmes d'IA de catégorisation biométrique inférant des attributs sensibles
- Attributs sensibles : Race, opinions politiques, appartenance syndicale, croyances religieuses/philosophiques, vie sexuelle, orientation sexuelle
- Exception : Étiquetage/filtrage de jeux de données biométriques acquis légalement (bases de données des forces de l'ordre)

**Article 5(1)(h) : Identification biométrique à distance en temps réel (IBD-TR) dans les espaces publics**

- Utilisation de systèmes IBD-TR dans des espaces accessibles au public à des fins répressives
- Exceptions (Article 5(2)) : Utilisations strictement nécessaires et proportionnées :
  - Recherche ciblée de personnes disparues spécifiques, victimes d'enlèvement
  - Prévention d'une menace spécifique, substantielle et imminente (attentat terroriste)
  - Localisation/identification d'une personne suspectée d'une infraction pénale grave (définie à l'Annexe II)
- Requiert une autorisation judiciaire ou administrative indépendante préalable (sauf urgence)

**Correspondance ISO 27001:2022** :

- Les interdictions de l'Article 5 concernent les politiques organisationnelles et l'utilisation éthique de l'IA
- Aucun contrôle ISO 27001 direct, mais éclairé par :
  - A.5.1 : Politiques de sécurité de l'information (politiques d'utilisation éthique)
  - A.5.31 : Exigences légales, réglementaires, statutaires et contractuelles
  - Clause 4.1 : Compréhension de l'organisme et de son contexte (attentes sociétales)

## Exigences de conformité

**Pour toutes les organisations** :
1. **Inventaire des systèmes d'IA** : Identifier tous les systèmes d'IA en développement ou en déploiement
2. **Évaluation Article 5** : Vérifier si des systèmes d'IA relèvent des pratiques interdites
3. **Cessation immédiate** : Arrêter le développement/déploiement de systèmes d'IA interdits avant le 2 février 2025
4. **Documentation** : Documenter l'évaluation et les décisions
5. **Formation** : Sensibiliser les équipes de développement/achats aux interdictions de l'Article 5

---

# Systèmes d'IA à haut risque (Chapitre III, Section 2)

## Vue d'ensemble

Les systèmes d'IA à haut risque sont soumis à des **exigences strictes** en raison des risques significatifs potentiels pour la santé, la sécurité ou les droits fondamentaux.

**Date d'effet** : 2 août 2026 (24 mois après l'entrée en vigueur)

**Sanction en cas de non-conformité** : jusqu'à 15 millions d'euros ou 3 % du chiffre d'affaires annuel mondial (le montant le plus élevé étant retenu)

## Catégories de systèmes d'IA à haut risque

**Cas d'usage à haut risque de l'Annexe III** :

| Catégorie | Cas d'usage | Exemples |
|-----------|-------------|----------|
| **1. Identification et catégorisation biométriques** | Identification biométrique à distance, catégorisation biométrique (exception attributs sensibles), reconnaissance des émotions | Contrôle d'accès par reconnaissance faciale, systèmes de catégorisation biométrique |
| **2. Infrastructures critiques** | Gestion et exploitation des infrastructures numériques critiques, gestion du trafic routier, alimentation en eau, gaz, chauffage, électricité | Gestion du trafic pilotée par l'IA, optimisation des réseaux électriques |
| **3. Éducation et formation professionnelle** | Détermination de l'accès/admission, évaluation des étudiants, détection de la triche aux examens | Admissions universitaires automatisées, IA de surveillance d'examens |
| **4. Emploi** | Recrutement, présélection, évaluation/promotion, affectation des tâches, surveillance/évaluation des performances professionnelles, licenciement | Tri de CV par IA, systèmes d'évaluation des performances |
| **5. Services privés/publics essentiels** | Notation de crédit, évaluation de l'éligibilité aux aides publiques, priorisation des interventions d'urgence | Algorithmes de décision de crédit, IA d'éligibilité aux prestations |
| **6. Forces de l'ordre** | Évaluation individuelle des risques (victimes, auteurs, récidive), polygraphes, reconnaissance des émotions, détection des hypertrucages, évaluation de la fiabilité des preuves | Prédiction de récidive, aide à l'interrogatoire par IA |
| **7. Migration, asile, contrôle aux frontières** | Examen des demandes, détection de documents frauduleux, évaluation des risques sécuritaires/sanitaires, polygraphe/détection de mensonges | Filtrage automatisé des visas, IA de vérification de documents |
| **8. Administration de la justice/processus démocratiques** | Assistance aux autorités judiciaires dans la recherche/interprétation juridiques, IA influençant les résultats électoraux | IA de recherche juridique, systèmes de prédiction électorale |

**Article 6(1)** : Systèmes d'IA constituant des composants de sécurité de produits couverts par la législation d'harmonisation de l'UE (Annexe I) si ces produits font l'objet d'une évaluation de la conformité par un tiers.

**Exemples tirés de l'Annexe I** :

- Dispositifs médicaux (Règlement 2017/745, 2017/746)
- Machines (Règlement 2023/1230)
- Jouets (Directive 2009/48/CE)
- Équipements radioélectriques (Directive 2014/53/UE)
- Aviation civile (Règlements 2018/1139, 2019/945, 2018/1139)

## Obligations des fournisseurs pour les systèmes d'IA à haut risque

**Article 9 : Système de gestion des risques**

Exigences :

- Établir, mettre en œuvre, documenter et maintenir un système de gestion des risques
- Processus itératif continu tout au long du cycle de vie du système d'IA
- Mises à jour systématiques régulières

**Processus de gestion des risques** :
1. **Identification et analyse** des risques connus et raisonnablement prévisibles
2. **Estimation et évaluation** des risques survenant lors de l'utilisation prévue et d'une utilisation abusive raisonnablement prévisible
3. **Évaluation d'autres risques** sur la base des données de surveillance post-commercialisation
4. **Adoption de mesures de gestion des risques adaptées** (Article 9(4))

**Mesures de gestion des risques** (Article 9(4)) :

- Élimination ou réduction des risques (protections dès la conception)
- Mesures d'atténuation et de contrôle adéquates (protections lors du déploiement)
- Information des déployeurs (instructions d'utilisation, avertissements)
- Formation appropriée des déployeurs

**Correspondance ISO 27001:2022** :

- Clause 6.1.2 : Appréciation des risques liés à la sécurité de l'information
- Clause 6.1.3 : Traitement des risques liés à la sécurité de l'information
- A.5.7 : Renseignement sur les menaces
- ISO/IEC 23894:2023 : Technologies de l'information — Intelligence artificielle — Gestion des risques (norme spécifique aux risques liés à l'IA)

---

**Article 10 : Données et gouvernance des données**

Exigences :

- Les jeux de données d'entraînement, de validation et de test satisfont aux **critères de qualité**
- Soumis à des pratiques de **gouvernance et de gestion des données**

**Critères de qualité des données** (Article 10(3)) :

- **Pertinents, suffisamment représentatifs et exempts d'erreurs**
- **Complets** pour l'objectif poursuivi
- **Propriétés statistiques appropriées** (ex. : équilibre, couverture)
- Prise en compte des caractéristiques/éléments du contexte géographique, contextuel et fonctionnel spécifique
- Documentation des choix de conception, des modalités de collecte des données et des opérations de préparation des données

**Pratiques de gouvernance des données** (Article 10(2)) :

- Choix de conception pertinents
- Processus de collecte de données
- Opérations de traitement et de préparation des données (annotation, étiquetage, nettoyage, enrichissement, agrégation)
- Hypothèses, notamment relatives à l'exhaustivité des informations
- Évaluation des biais dans les données et mesures d'atténuation appropriées
- Identification des lacunes ou insuffisances des données affectant l'utilisation prévue

**Catégories spéciales de données** (Article 10(5)) :
Lorsqu'un système d'IA traite des catégories sensibles de données à caractère personnel (Article 9 RGPD : origine raciale/ethnique, opinions politiques, croyances religieuses, données biométriques, données de santé, vie sexuelle/orientation) :

- Mesures appropriées pour détecter, prévenir et réduire les biais
- Formation aux droits fondamentaux et à la non-discrimination

**Correspondance ISO 27001:2022** :

- A.5.12 : Classification de l'information
- A.5.13 : Marquage de l'information
- A.5.14 : Transfert d'information (partage de jeux de données)
- A.8.11 : Masquage des données
- RGPD Article 5(1)(d) : Principe d'exactitude des données

---

**Article 11 : Documentation technique**

Exigences :

- Établir la documentation technique **avant la mise sur le marché**
- Maintenir la documentation technique **à jour**
- La mettre à disposition des autorités nationales compétentes sur demande

**Contenu de la documentation technique** (Annexe IV) :
1. Description générale du système d'IA (objectif, développeur, versions, dates de mise sur le marché)
2. Description détaillée des éléments du système et du processus de développement
3. Informations détaillées sur la surveillance, le fonctionnement et le contrôle
4. Description du système de gestion des risques (Article 9)
5. Description des modifications apportées tout au long du cycle de vie
6. Démonstration de la conformité aux exigences applicables aux systèmes à haut risque
7. Description détaillée de la procédure d'évaluation de la conformité
8. Copie de la déclaration UE de conformité
9. Description détaillée du système de surveillance post-commercialisation

**Correspondance ISO 27001:2022** :

- A.5.37 : Procédures d'exploitation documentées
- Clause 7.5 : Informations documentées (exigences de documentation SMSI)

---

**Article 12 : Conservation des enregistrements (journalisation)**

Exigences :

- Journaux générés automatiquement tout au long de la durée de vie du système d'IA
- Permettre la **traçabilité** du fonctionnement du système
- Adaptés à l'objectif prévu et au niveau de risque

**Exigences de journalisation** (Article 12(2)) :

- **Durée de journalisation** : Appropriée au risque du système
- **Horodatage** : Date et heure de chaque événement
- **Données en entrée** : Base de données/fichier déclenchant l'action
- **Personnes physiques impliquées** : Identification si techniquement faisable

**Objectif** : Permettre la surveillance, l'investigation, la surveillance post-commercialisation et la responsabilisation.

**Correspondance ISO 27001:2022** :

- A.8.15 : Journalisation
- A.8.16 : Activités de surveillance
- ISO/IEC 27018:2019 : Protection des données à caractère personnel dans les nuages publics (exigences de journalisation)

---

**Article 13 : Transparence et information des déployeurs**

Exigences :

- Concevoir le système d'IA de manière à assurer la **transparence** permettant aux déployeurs :
  - D'interpréter les résultats du système
  - D'utiliser le système de manière appropriée

**Instructions d'utilisation** (Annexe IV, Section 2) :

- Identité et coordonnées du fournisseur
- Caractéristiques, capacités et limites de performance
- Modifications apportées au système d'IA et à ses performances
- Mesures de surveillance humaine
- Ressources informatiques et matérielles nécessaires
- Durée de vie attendue et besoins de maintenance

**Correspondance ISO 27001:2022** :

- A.5.37 : Procédures d'exploitation documentées (documentation utilisateur)

---

**Article 14 : Surveillance humaine**

Exigences :

- Concevoir le système d'IA pour permettre une **surveillance effective par des personnes physiques**
- Prévenir ou minimiser les risques pour la santé, la sécurité et les droits fondamentaux

**Mesures de surveillance humaine** (Article 14(4)) :

- **Comprendre** les capacités et limites du système d'IA
- Rester **conscient** de la tendance au biais d'automatisation
- **Interpréter correctement** les résultats du système
- **Décider de ne pas utiliser** ou de passer outre les résultats
- **Intervenir ou interrompre** le fonctionnement du système (bouton d'arrêt)

**Désignation des responsables de la surveillance** (Article 14(5)) :

- Les personnes physiques désignées pour assurer la surveillance doivent disposer de :
  - La compétence, la formation et l'autorité nécessaires
  - Une compréhension adéquate du système d'IA à haut risque

**Correspondance ISO 27001:2022** :

- A.5.37 : Procédures d'exploitation documentées (procédures de surveillance humaine)
- A.6.3 : Sensibilisation, formation et éducation à la sécurité de l'information (formation à la surveillance)

---

**Article 15 : Exactitude, robustesse et cybersécurité**

Exigences :

- **Exactitude** : Niveau d'exactitude approprié tout au long du cycle de vie
- **Robustesse** : Mesures techniques et de cybersécurité adaptées aux risques
- **Résilience** : Contre les tentatives d'altération de l'utilisation/des performances par des tiers

**Mesures de robustesse** :

- Solutions techniques contre les attaques adversariales
- Attaques par empoisonnement de modèle
- Attaques par empoisonnement de données
- Attaques sur la vie privée (inversion de modèle, inférence d'appartenance)
- Attaques sur la confidentialité

**Correspondance ISO 27001:2022** :

- A.8.7 : Protection contre les logiciels malveillants
- A.8.8 : Gestion des vulnérabilités techniques
- A.8.16 : Activités de surveillance (détection des anomalies)
- A.8.24 : Utilisation de la cryptographie (protection des modèles)
- ISO/IEC 24029-1 : Intelligence artificielle — Évaluation de la robustesse des réseaux de neurones

---

**Article 16 : Système de management de la qualité**

Exigences :

- Mettre en place un système de management de la qualité (SMQ) garantissant :
  - La conformité au Règlement IA
  - La mise en œuvre des Articles 9 à 15
  - La surveillance post-commercialisation (Article 72)

**Contenu du système de management de la qualité** :

- Stratégie de conformité réglementaire (politiques, procédures)
- Techniques, procédures, actions systématiques (conception, contrôle de la conception, vérification, validation, tests)
- Procédures d'examen, de test et de validation avant, pendant et après le développement
- Spécifications techniques (normes de qualité, directives de codage)
- Systèmes et procédures de gestion des données
- Système de gestion des risques
- Système de surveillance post-commercialisation
- Signalement des incidents graves et dysfonctionnements
- Communication avec les autorités, les déployeurs
- Systèmes et procédures de conservation des enregistrements
- Gestion des ressources (compétences, plans de formation)
- Cadre de responsabilisation (rôles et responsabilités)

**Correspondance ISO 27001:2022** :

- L'ensemble du cadre SMSI Clauses 4 à 10
- ISO 9001:2015 Système de management de la qualité (norme complémentaire)

---

**Articles 43–51 : Évaluation de la conformité**

**Avant la mise sur le marché d'un système d'IA à haut risque**, le fournisseur doit procéder à une évaluation de la conformité.

**Options d'évaluation de la conformité** :

**Option 1 : Contrôle interne** (Article 43 + Annexe VI) :

- Évaluation propre du fournisseur (auto-évaluation)
- Applicable à la plupart des systèmes à haut risque de l'Annexe III

**Option 2 : Évaluation par un organisme notifié** (Article 43 + Annexe VII) :

- Évaluation par un tiers (organisme notifié)
- Requise pour :
  - Identification/catégorisation biométrique (Annexe III(1))
  - Certaines infrastructures critiques (si non auto-certifiées)

**Processus d'évaluation de la conformité** (Annexe VI) :
1. Préparation de la documentation technique (Article 11, Annexe IV)
2. Mise en œuvre du système de management de la qualité (Article 16)
3. Mise en œuvre du système de gestion des risques (Article 9)
4. Auto-évaluation ou évaluation par un tiers
5. Établissement de la déclaration UE de conformité (Annexe V)
6. Apposition du marquage CE (Article 48)

**Marquage CE** (Article 48) :

- Les systèmes d'IA à haut risque portent le marquage CE
- Indique la conformité au Règlement IA
- Apposé de manière visible, lisible et indélébile

**Correspondance ISO 27001:2022** :

- Clause 9.2 : Audit interne (similaire à l'auto-évaluation)
- Clause 9.3 : Revue de direction

---

**Article 72 : Surveillance post-commercialisation**

Exigences :

- Établir et documenter un système de surveillance post-commercialisation
- Collecter, documenter et analyser les données sur les performances tout au long de la durée de vie

**Plan de surveillance post-commercialisation** :

- Stratégie de collecte de données sur les performances en conditions réelles
- Méthodes d'analyse des incidents graves, dysfonctionnements et inexactitudes
- Mécanismes de signalement aux autorités
- Boucle de rétroaction vers le système de gestion des risques

**Correspondance ISO 27001:2022** :

- Clause 9.1 : Surveillance, mesure, analyse et évaluation
- A.8.16 : Activités de surveillance

---

## Obligations des déployeurs pour les systèmes d'IA à haut risque

**Article 26 : Obligations des déployeurs**

Les déployeurs (utilisateurs) de systèmes d'IA à haut risque doivent :

1. **Utiliser conformément aux instructions** (Article 26(1))
2. **Désigner une surveillance humaine** à des personnes physiques compétentes (Article 26(2))
3. **Surveiller le fonctionnement** sur la base des instructions d'utilisation (Article 26(3))
4. **Suspendre l'utilisation** en cas de suspicion d'incident grave ou de dysfonctionnement (Article 26(4))
5. **Conserver les journaux** générés automatiquement par le système (Article 26(5))
6. **Utiliser des données en entrée** pertinentes et représentatives pour l'objectif prévu (Article 26(6))
7. **Réaliser une évaluation de l'impact sur les droits fondamentaux** (EIDF) avant la mise en service (Article 27) — pour les déployeurs dans des secteurs ou usages spécifiques

**Évaluation de l'impact sur les droits fondamentaux (EIDF)** — Article 27 :
Requise pour les déployeurs qui sont :

- Des autorités publiques OU
- Des institutions/organes/organismes de l'UE OU
- Des déployeurs de systèmes d'IA à haut risque dans certains domaines sensibles (définis à l'Article 27(1))

**Contenu de l'EIDF** :

- Description des processus du déployeur dans lesquels l'IA sera utilisée
- Description de la période et de la fréquence d'utilisation
- Catégories de personnes physiques et de groupes susceptibles d'être concernés
- Risques spécifiques de préjudice susceptibles d'affecter les personnes concernées
- Description des mesures de surveillance humaine
- Mesures en cas de matérialisation des risques

**Correspondance ISO 27001:2022** :

- A.5.37 : Procédures d'exploitation documentées (procédures du déployeur)
- Clause 6.1.2 : Appréciation des risques (EIDF similaire à une appréciation des risques)
- RGPD Article 35 : Analyse d'impact relative à la protection des données (AIPD) (similaire à l'EIDF)

---

# Systèmes d'IA à risque limité (Article 50) — Obligations de transparence

## Vue d'ensemble

Certains systèmes d'IA présentent des **risques limités** mais nécessitent de la transparence pour permettre des décisions éclairées.

**Date d'effet** : 2 août 2026 (identique aux systèmes à haut risque)

**Sanction en cas de non-conformité** : jusqu'à 7,5 millions d'euros ou 1,5 % du chiffre d'affaires annuel mondial (le montant le plus élevé étant retenu)

## Exigences de transparence

**Article 50(1) : Systèmes d'IA interagissant avec des personnes physiques**

Lorsqu'un système d'IA est destiné à interagir directement avec des personnes physiques :

- **Informer les personnes physiques** qu'elles interagissent avec un système d'IA
- **Exceptions** :
  - L'évidence ressort des circonstances et du contexte
  - Autorisé par la loi à des fins répressives (détection, prévention, investigation d'infractions)

**Exemples** :

- Chatbots (obligation d'informer l'utilisateur qu'il interagit avec une IA)
- Assistants virtuels
- Systèmes téléphoniques automatisés

---

**Article 50(2) : Systèmes de reconnaissance des émotions et de catégorisation biométrique**

Lors de l'utilisation de systèmes de reconnaissance des émotions ou de catégorisation biométrique :

- **Informer les personnes physiques** exposées au système
- **Exception** : Autorisé par la loi à des fins répressives

**Exemples** :

- Reconnaissance des émotions dans le commerce de détail (obligation d'informer les clients)
- Outils d'analyse des émotions lors d'entretiens
- Catégorisation biométrique dans les aéroports

---

**Article 50(3) : Contenus générés par IA (hypertrucages)**

Lors de la génération ou de la manipulation de contenus d'image/audio/vidéo (hypertrucages) :

- **Divulguer** que le contenu est artificiellement généré ou manipulé

**Exigences de divulgation** :

- Format lisible par machine (normes techniques en cours d'élaboration)
- Divulgation lisible par l'homme destinée au grand public

**Exceptions** :

- Contenu nécessaire à l'exercice du droit à la liberté d'expression et à la liberté artistique/littéraire/satirique
- Autorisé par la loi à des fins répressives
- Nécessaire pour détecter/exposer des infractions

**Types spécifiques** :

**Article 50(4) : Textes générés par IA (systèmes similaires à ChatGPT)**

- Divulguer que les résultats sont artificiellement générés ou manipulés
- S'applique aux systèmes produisant du texte à des fins d'information du public
- **Exception** : Texte ayant fait l'objet d'une révision humaine ou d'un contrôle éditorial avec responsabilité éditoriale

---

**Correspondance ISO 27001:2022** :

- A.5.1 : Politiques de sécurité de l'information (politiques de transparence)
- A.5.9 : Inventaire de l'information et des autres actifs associés (inventaire des systèmes d'IA)

---

# Systèmes d'IA à risque minimal — Mesures volontaires

## Vue d'ensemble

La plupart des systèmes d'IA présentent un **risque minimal ou nul** et ne sont soumis à **aucune exigence obligatoire** au titre du Règlement IA.

**Exemples** :

- Filtres anti-spam
- Jeux vidéo avec IA
- Systèmes de gestion des stocks
- Moteurs de recommandation (commerce électronique)
- Analyses commerciales internes
- Outils de développement IA

## Codes de conduite volontaires (Article 95)

Les fournisseurs de systèmes d'IA à risque minimal sont **encouragés** à appliquer volontairement :

- Les exigences applicables aux systèmes d'IA à haut risque (Articles 9 à 15)
- Les exigences de transparence (Article 50)
- Les codes de conduite élaborés par l'industrie

**Avantages de la conformité volontaire** :

- Démontrer la fiabilité
- Avantage concurrentiel
- Préparation à une réglementation future potentielle
- Alignement avec les principes d'une IA éthique

---

# Modèles d'IA à usage général (MIAG) — Chapitre V

## Vue d'ensemble

Les **modèles d'IA à usage général** (MIAG) sont des modèles de fondation capables d'exécuter un large éventail de tâches.

**Exemples** :

- Grands modèles de langage (GPT-4, Claude, Gemini, LLaMA)
- Modèles multimodaux (GPT-4V, Gemini)
- Modèles de fondation pour la génération d'images (DALL-E, Stable Diffusion, Midjourney)

**Date d'effet** : 2 août 2025 (12 mois après l'entrée en vigueur)

## Obligations des fournisseurs de MIAG

**Article 53 : Obligations de tous les fournisseurs de MIAG**

Tous les fournisseurs de MIAG doivent :

1. **Documentation technique** (Article 53(1)(a) + Annexe XI) :

   - Description générale du modèle (capacités, limites)
   - Description des données utilisées pour l'entraînement (sources, sélection)
   - Informations sur les ressources de calcul (temps d'entraînement, matériel)
   - Description du processus d'évaluation et des résultats

2. **Information pour les fournisseurs en aval** (Article 53(1)(b)) :

   - Documentation permettant aux fournisseurs en aval (intégrant le MIAG dans leurs systèmes d'IA) de se conformer au Règlement IA
   - Instructions d'utilisation

3. **Politique en matière de droits d'auteur** (Article 53(1)(c)) :

   - Politique accessible au public pour identifier et respecter la Directive (UE) 2019/790 (Directive droit d'auteur)
   - Résumé des contenus protégés par le droit d'auteur utilisés pour l'entraînement (si disponible)

4. **Transparence** (Article 53(1)(d)) :

   - Résumé accessible au public des contenus utilisés pour l'entraînement
   - Modèle du Bureau IA de l'UE (en cours d'élaboration)

**Article 54 : Obligations supplémentaires pour les MIAG présentant un risque systémique**

Pour les MIAG présentant un **risque systémique** (voir Section 7.3) :

5. **Évaluation du modèle** (Article 54(1)(a)) :

   - Tests adversariaux (red teaming)
   - Évaluation et atténuation des risques systémiques

6. **Suivi des incidents graves** (Article 54(1)(b)) :

   - Suivre, documenter et signaler les incidents graves au Bureau IA de l'UE

7. **Cybersécurité** (Article 54(1)(c)) :

   - Assurer un niveau adéquat de protection de la cybersécurité
   - Protéger les poids et autres paramètres du modèle contre les accès non autorisés

8. **Efficacité énergétique** (Article 54(1)(d)) :

   - Rendre compte de la consommation énergétique lors de l'entraînement
   - Optimiser l'efficacité énergétique lorsque cela est faisable

## MIAG présentant un risque systémique

**Définition** (Article 51) :
Un MIAG présente un risque systémique si :

- Il a des capacités à fort impact (évaluées selon l'état de l'art) OU
- Son impact sur le marché de l'UE est significatif (évalué par la portée du modèle) OU
- La quantité cumulée de calcul utilisée ≥ 10^25 FLOPs (opérations à virgule flottante)

**Seuil de 10^25 FLOPs** (Article 51(1)(a)) :

- Risque systémique présumé si le calcul d'entraînement ≥ 10^25 FLOPs
- Exemple : GPT-4 estimé à ~2–5 × 10^25 FLOPs (serait qualifié)

**Désignation** :

- Le Bureau IA de l'UE peut désigner des modèles comme présentant un risque systémique
- Les fournisseurs peuvent demander une décision de la Commission si le calcul < 10^25 FLOPs

**Sanction en cas de non-conformité** : jusqu'à 15 millions d'euros ou 3 % du chiffre d'affaires annuel mondial (le montant le plus élevé étant retenu)

## Correspondance ISO 27001:2022 pour les MIAG

| Exigence du Règlement IA | Contrôle ISO 27001:2022 | Notes |
|--------------------------|-------------------------|-------|
| Documentation technique (Article 53) | A.5.37, Clause 7.5 | Pratiques de documentation |
| Politique droits d'auteur (Article 53(1)(c)) | A.5.31 Exigences légales | Conformité au droit d'auteur |
| Évaluation du modèle (Article 54(1)(a)) | A.8.8 Gestion des vulnérabilités | Tests adversariaux similaires aux tests de pénétration |
| Suivi des incidents graves (Article 54(1)(b)) | A.5.24–5.28 Gestion des incidents | Suivi et signalement des incidents |
| Cybersécurité (Article 54(1)(c)) | A.8.24 Cryptographie, A.8.3 Restriction d'accès | Protection des poids du modèle |

---

# Exigences organisationnelles et de gouvernance

## Culture de l'IA (Article 4)

**Exigence** : Les fournisseurs et déployeurs veillent à ce que le **personnel opérant des systèmes d'IA** dispose d'un niveau suffisant de culture de l'IA.

**Définition de la culture de l'IA** : Compétences et connaissances permettant de :

- Comprendre les capacités et les limites des systèmes d'IA
- Interpréter correctement les résultats des systèmes
- Prendre des décisions éclairées sur l'utilisation appropriée

**Mise en œuvre** :

- Programmes de formation pour les utilisateurs de systèmes d'IA
- Formation spécifique aux rôles (développeurs, déployeurs, responsables de la surveillance)
- Sensibilisation aux biais, à l'éthique et aux droits fondamentaux

**Correspondance ISO 27001:2022** :

- A.6.3 : Sensibilisation, formation et éducation à la sécurité de l'information

---

## Rôles et responsabilités

**Structure de gouvernance recommandée** :

| Rôle | Responsabilités |
|------|----------------|
| **Comité de gouvernance IA** | Supervision stratégique de l'IA, approbation des politiques, appétence pour le risque |
| **Directeur de l'IA (DAI)** ou équivalent | Pilotage du programme IA, coordination de la conformité |
| **RSSI** | Aspects cybersécurité des systèmes d'IA (Article 15) |
| **DPD** | Conformité RGPD pour le traitement de données à caractère personnel par l'IA |
| **Juridique/Conformité** | Conformité au Règlement IA, évaluations des risques, rapports externes |
| **Responsables produit** | Responsables des systèmes d'IA spécifiques (gestion des risques, documentation) |
| **Équipes de développement IA** | Mise en œuvre des exigences techniques (Articles 9 à 15) |
| **Responsables de la surveillance humaine** | Désignés conformément à l'Article 14 pour les systèmes à haut risque |

**Correspondance ISO 27001:2022** :

- Clause 5.3 : Rôles, responsabilités et autorités au sein de l'organisme
- A.5.2 : Rôles et responsabilités en matière de sécurité de l'information

---

## Inventaire des systèmes d'IA

**Exigence** : Maintenir un inventaire de tous les systèmes d'IA développés ou déployés.

**Contenu de l'inventaire** :

- Nom et version du système d'IA
- Fournisseur (développement interne ou externe)
- Objectif et cas d'usage prévus
- Classification des risques (Inacceptable, Haut risque, Risque limité, Risque minimal)
- Statut de déploiement (développement, test, production, retraité)
- Obligations réglementaires (statut d'évaluation de la conformité)
- Responsabilités du déployeur désignées

**Correspondance ISO 27001:2022** :

- A.5.9 : Inventaire de l'information et des autres actifs associés

---

# Correspondance ISO 27001:2022 / Règlement IA de l'UE

## Matrice de correspondance des contrôles

| Exigence du Règlement IA | Article | Contrôle ISO 27001:2022 | Analyse des écarts |
|--------------------------|---------|-------------------------|--------------------|
| Évaluation des pratiques interdites | Art. 5 | A.5.1, A.5.31 | Interdictions spécifiques au Règlement IA |
| Système de gestion des risques | Art. 9 | Clause 6.1.2–6.1.3 | Règlement IA : Processus de gestion des risques IA plus détaillé |
| Gouvernance des données | Art. 10 | A.5.12–5.14 | **Spécifique au Règlement IA** : qualité des données, atténuation des biais |
| Documentation technique | Art. 11 | A.5.37, Clause 7.5 | Règlement IA : Documentation étendue des systèmes d'IA |
| Journalisation (conservation) | Art. 12 | A.8.15–8.16 | Aligné |
| Transparence pour les déployeurs | Art. 13 | A.5.37 | Règlement IA : Instructions d'utilisation détaillées |
| Surveillance humaine | Art. 14 | A.5.37 | **Spécifique au Règlement IA** : Exigences d'intervention humaine |
| Exactitude, robustesse, cybersécurité | Art. 15 | A.8.7–8.8, A.8.16 | Règlement IA : Protection IA spécifique contre les attaques adversariales |
| Système de management de la qualité | Art. 16 | Clauses 4 à 10 (ensemble du SMSI) | Complémentaire : ISO 9001 + ISO 27001 |
| Évaluation de la conformité | Art. 43–51 | Clause 9.2–9.3 | **Spécifique au Règlement IA** : Marquage CE, organismes notifiés |
| Surveillance post-commercialisation | Art. 72 | Clause 9.1, A.8.16 | Règlement IA : Surveillance continue des performances réelles |
| Obligations des déployeurs | Art. 26 | A.5.37 | Règlement IA : Responsabilités spécifiques aux déployeurs |
| Transparence (risque limité) | Art. 50 | A.5.1 | **Spécifique au Règlement IA** : Exigences de divulgation à l'utilisateur |
| Culture de l'IA | Art. 4 | A.6.3 | Règlement IA : Formation spécifique à l'IA |

## Écarts clés entre ISO 27001:2022 et le Règlement IA de l'UE

**Écart 1 : Appréciation des risques spécifique à l'IA**

- ISO 27001 : Appréciation générale des risques liés à la sécurité de l'information
- Règlement IA : Gestion détaillée des risques des systèmes d'IA (biais, discrimination, sécurité, droits fondamentaux)

**Écart 2 : Gouvernance des données pour l'IA**

- ISO 27001 : Classification et protection des données
- Règlement IA : Qualité des données d'entraînement/validation/test, représentativité, atténuation des biais

**Écart 3 : Exigences de surveillance humaine**

- ISO 27001 : Aucune exigence spécifique de surveillance humaine
- Règlement IA : Surveillance humaine obligatoire pour les systèmes d'IA à haut risque (Article 14)

**Écart 4 : Évaluation de la conformité et marquage CE**

- ISO 27001 : Certification par un organisme accrédité
- Règlement IA : Évaluation de la conformité (auto-évaluation ou organisme notifié), marquage CE

**Écart 5 : Transparence et explicabilité**

- ISO 27001 : Aucune exigence d'explicabilité
- Règlement IA : Transparence envers les déployeurs (Article 13), transparence envers les utilisateurs finaux (Article 50)

**Écart 6 : Impact sur les droits fondamentaux**

- ISO 27001 : Aucune évaluation des droits fondamentaux
- Règlement IA : Évaluation de l'impact sur les droits fondamentaux (EIDF) pour certains déployeurs (Article 27)

**Écart 7 : Surveillance post-commercialisation spécifique à l'IA**

- ISO 27001 : Surveillance et mesure générales
- Règlement IA : Surveillance des performances des systèmes d'IA en conditions réelles, signalement des incidents

## Conformité au Règlement IA avec un socle ISO 27001

**Enseignement clé** :
ISO 27001:2022 fournit de solides contrôles fondamentaux pour la conformité au Règlement IA, notamment pour les aspects cybersécurité (Article 15). Toutefois, le Règlement IA introduit des **exigences spécifiques à l'IA** non couvertes par ISO 27001 :

**Normes complémentaires à prendre en compte** :

- **ISO/IEC 42001:2023** : Système de management de l'IA (SMIA) — spécifiquement conçu pour la gouvernance de l'IA
- **ISO/IEC 23894:2023** : Gestion des risques liés à l'IA
- **ISO/IEC 24029-1:2021** : Évaluation de la robustesse des réseaux de neurones
- **ISO/IEC TR 24028:2020** : Vue d'ensemble de la fiabilité en IA
- **ISO/IEC 38507:2022** : Gouvernance des TI — Implications de la gouvernance pour l'IA

Les organisations disposant d'ISO 27001 nécessitent généralement **40 à 60 % d'effort supplémentaire** pour atteindre la conformité au Règlement IA de l'UE pour les systèmes à haut risque, principalement dans les domaines suivants :

- Gestion des risques spécifique à l'IA
- Gouvernance des données pour les données d'entraînement/validation
- Procédures de surveillance humaine
- Évaluation de la conformité et marquage CE
- Considérations relatives aux droits fondamentaux

---

# Considérations de mise en œuvre

## Feuille de route de conformité au Règlement IA

**Si [Organisation] développe ou déploie des systèmes d'IA affectant l'UE** :

**Phase 1 : Inventaire et classification (Mois 1–3)**

- Identifier tous les systèmes d'IA (actuels et planifiés)
- Classifier chaque système d'IA (Inacceptable, Haut risque, Risque limité, Risque minimal)
- Évaluer les interdictions de l'Article 5 (action immédiate en cas de violations)
- Déterminer le rôle fournisseur vs. déployeur pour chaque système
- Identifier les MIAG (le cas échéant)

**Phase 2 : Évaluation des écarts (Mois 3–6)**

- Évaluer la gouvernance IA et la documentation actuelles
- Identifier les écarts par rapport aux exigences du Règlement IA
- Prioriser la remédiation (pratiques interdites en premier, puis haut risque)
- Estimer le budget et les ressources
- Consulter des conseils juridiques pour les décisions de classification complexes

**Phase 3 : Gouvernance et politiques (Mois 6–9)**

- Établir la structure de gouvernance IA (rôles, responsabilités)
- Développer le cadre de gestion des risques IA (Article 9)
- Créer des politiques de gouvernance des données (Article 10)
- Établir des procédures de surveillance humaine (Article 14)
- Programmes de formation à la culture de l'IA (Article 4)

**Phase 4 : Conformité des systèmes à haut risque (Mois 9–18)**

- Mettre en œuvre les exigences techniques (Articles 11 à 15)
- Préparer la documentation technique (Annexe IV)
- Mettre en œuvre le système de management de la qualité (Article 16)
- Préparer l'évaluation de la conformité
- Établir la surveillance post-commercialisation

**Phase 5 : Évaluation de la conformité (Mois 18–24)**

- Finaliser la documentation technique
- Mener l'auto-évaluation ou faire appel à un organisme notifié
- Traiter les non-conformités identifiées
- Préparer la déclaration UE de conformité
- Apposer le marquage CE (si système à haut risque)

**Phase 6 : Déploiement et surveillance (Mois 24+)**

- Déployer les systèmes d'IA à haut risque en conformité
- Mettre en œuvre la surveillance post-commercialisation (Article 72)
- Surveillance continue de la conformité
- Révision et mises à jour annuelles
- Procédures de signalement des incidents

**Notes sur le calendrier** :

- Pratiques interdites : Action immédiate requise (2 février 2025)
- MIAG : 2 août 2025
- Systèmes à haut risque : 2 août 2026
- Période de grâce pour les systèmes existants : Jusqu'au 2 août 2030 (sauf modification substantielle)

## Ressources nécessaires

**Personnel** :

- Directeur de l'IA ou équivalent
- Équipe de gouvernance IA (interfonctionnelle)
- Data scientists/ingénieurs ML (développement IA)
- Conseils juridiques avec expertise en Règlement IA
- Spécialistes de la gouvernance des données
- Personnel de surveillance humaine (pour chaque système à haut risque)
- Équipe conformité/audit

**Ressources externes** :

- Conseils juridiques (interprétation du Règlement IA)
- Organismes notifiés (si requis pour l'évaluation de la conformité)
- Consultants en éthique de l'IA
- Auditeurs externes (système de management de la qualité)

**Technologie** :

- Plateforme de documentation des systèmes d'IA
- Outils de gouvernance des modèles (MLOps, registre de modèles)
- Plateformes de gouvernance des données (qualité des données, traçabilité)
- Infrastructure de journalisation et de surveillance
- Outils de tests adversariaux (pour les MIAG à risque systémique)

## Implications financières

Les coûts de conformité au Règlement IA varient considérablement selon :

- Le nombre et le niveau de risque des systèmes d'IA
- Le rôle fournisseur vs. déployeur
- Le développement IA interne vs. IA de tiers

**Coûts de conformité estimés** :

**Système d'IA à haut risque (Fournisseur)** :

- Documentation technique et management de la qualité : 50 000 € – 200 000 €
- Évaluation de la conformité (organisme notifié si requis) : 10 000 € – 50 000 €
- Surveillance post-commercialisation annuelle : 20 000 € – 100 000 €
- Juridique et conseil : 30 000 € – 100 000 €
- **Coût initial total** : 110 000 € – 450 000 € par système à haut risque
- **Récurrent annuel** : 50 000 € – 150 000 € par système

**Système d'IA à haut risque (Déployeur)** :

- Évaluation de l'impact sur les droits fondamentaux : 10 000 € – 30 000 €
- Mise en œuvre de la surveillance humaine : 20 000 € – 50 000 €
- Formation et procédures : 10 000 € – 30 000 €
- **Coût initial total** : 40 000 € – 110 000 € par système
- **Récurrent annuel** : 20 000 € – 50 000 €

**MIAG à risque systémique** :

- Documentation technique : 100 000 € – 300 000 €
- Tests adversariaux (red teaming) : 50 000 € – 200 000 €
- Mesures de cybersécurité (protection des modèles) : 50 000 € – 150 000 €
- Rapport sur l'efficacité énergétique : 10 000 € – 30 000 €
- **Coût initial total** : 210 000 € – 680 000 €
- **Récurrent annuel** : 100 000 € – 300 000 €

**Sanctions en cas de non-conformité** :

- Pratiques interdites : jusqu'à 35 M€ ou 7 % du chiffre d'affaires
- Violations haut risque : jusqu'à 15 M€ ou 3 % du chiffre d'affaires
- Violations risque limité : jusqu'à 7,5 M€ ou 1,5 % du chiffre d'affaires
- Fourniture d'informations inexactes : jusqu'à 7,5 M€ ou 1,5 % du chiffre d'affaires

---

# Difficultés courantes et retours d'expérience

## Principaux défis de conformité au Règlement IA

**Défi 1 : Identification des systèmes d'IA**

- Les organisations sous-estiment le nombre de systèmes d'IA utilisés
- La définition de l'« IA » est large — inclut les systèmes à base de règles, les modèles statistiques
- L'IA intégrée dans des logiciels tiers est souvent négligée

**Défi 2 : Incertitude sur la classification des risques**

- La frontière entre haut risque et risque limité n'est pas toujours claire
- Le cas d'usage prime sur la technologie (même modèle, usage différent = risque différent)
- Les catégories de l'Annexe III sont sujettes à interprétation

**Défi 3 : Confusion entre rôle fournisseur et rôle déployeur**

- Une même organisation peut être à la fois fournisseur et déployeur
- La personnalisation d'une IA tierce peut faire de l'organisation un fournisseur
- La « modification substantielle » déclenche les obligations du fournisseur

**Défi 4 : Gouvernance des données pour l'IA**

- La qualité des données d'entraînement et l'atténuation des biais nécessitent un effort considérable
- Les systèmes d'IA anciens peuvent manquer de documentation sur la traçabilité des données
- La représentativité des données est difficile à évaluer et à valider

**Défi 5 : Mise en œuvre de la surveillance humaine**

- Identifier les responsables de surveillance compétents
- Équilibrer la surveillance et l'efficacité opérationnelle
- Le « bouton d'arrêt » n'est pas toujours techniquement faisable dans les systèmes en temps réel

**Défi 6 : Préparation à l'évaluation de la conformité**

- La documentation technique est étendue (Annexe IV)
- Le système de management de la qualité exige une maturité organisationnelle
- La capacité des organismes notifiés peut être initialement limitée

**Défi 7 : Obligations relatives aux MIAG**

- La conformité du droit d'auteur pour les données d'entraînement est difficile à vérifier
- Les résumés de transparence nécessitent des formats standardisés (encore en cours d'élaboration)
- Le seuil de risque systémique (10^25 FLOPs) peut concerner de nombreux modèles de fondation

## Bonnes pratiques

**Pratique 1** : Réaliser un inventaire complet des systèmes d'IA tôt (ne pas attendre les échéances)
**Pratique 2** : Consulter des conseils juridiques pour la classification des risques (décisions documentées)
**Pratique 3** : Mettre en place la structure de gouvernance IA avant les exigences techniques
**Pratique 4** : Utiliser conjointement ISO 27001 + ISO 42001 (Système de management de l'IA)
**Pratique 5** : Tout documenter (le Règlement IA met fortement l'accent sur la documentation)
**Pratique 6** : Établir la surveillance humaine dès la phase de conception du système d'IA (et non a posteriori)
**Pratique 7** : Pour les fournisseurs de MIAG, engager tôt le Bureau IA de l'UE (les orientations évoluent)
**Pratique 8** : Envisager la conformité volontaire pour les IA à risque minimal (anticipation réglementaire)
**Pratique 9** : Intégrer la conformité au Règlement IA dans le cycle de vie du développement logiciel (SDLC) et les processus d'achats
**Pratique 10** : Surveiller les actes délégués et les actes d'exécution du Règlement IA (nombreux encore en cours d'élaboration)

---

# Références et ressources

## Ressources officielles relatives au Règlement IA de l'UE

**Règlement primaire** :

- Règlement (UE) 2024/1689 (Loi sur l'IA) — Journal officiel de l'UE

**Bureau IA de l'UE** :

- Site web : https://digital-strategy.ec.europa.eu/en/policies/ai-office
- Documents d'orientation (en cours d'élaboration)
- Modèles pour la documentation technique et les résumés de transparence

**Commission européenne** :

- Pages dédiées au Règlement IA : https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai

## Normes et référentiels connexes

**Normes ISO sur l'IA** :

- **ISO/IEC 42001:2023** : Système de management de l'IA (SMIA) — recommandé pour la conformité au Règlement IA
- **ISO/IEC 23894:2023** : Gestion des risques liés à l'IA
- **ISO/IEC 24029-1:2021** : Évaluation de la robustesse des réseaux de neurones
- **ISO/IEC TR 24028:2020** : Vue d'ensemble de la fiabilité en IA
- **ISO/IEC 38507:2022** : Gouvernance des TI — Implications de la gouvernance pour l'IA
- **ISO/IEC 23053:2022** : Cadre pour les systèmes d'IA utilisant l'apprentissage automatique

**Normes de sécurité de l'information** :

- ISO/IEC 27001:2022 : Management de la sécurité de l'information
- ISO/IEC 27002:2022 : Contrôles de sécurité de l'information
- ISO/IEC 27701:2019 : Management des informations sur la vie privée

**Normes NIST sur l'IA** (référence informative) :

- NIST AI Risk Management Framework (AI RMF)
- NIST SP 1270 : Vers une norme d'identification et de gestion des biais dans l'IA

## Orientations et ressources sectorielles

**Alliance européenne pour l'IA** :

- Forum des parties prenantes pour la politique en matière d'IA
- Site web : https://futurium.ec.europa.eu/en/european-ai-alliance

**Centre de normalisation IA** :

- Activités de normalisation IA du CEN-CENELEC
- Site web : https://www.cencenelec.eu/areas-of-work/cen-cenelec-topics/artificial-intelligence/

**Ressources juridiques et de conseil** :

- Consulter des conseils juridiques avec expertise en Règlement IA de l'UE
- Consultants en éthique de l'IA pour les évaluations des droits fondamentaux
- Organismes notifiés (liste à publier par la Commission)

---

# Annexe A : Liste de contrôle d'auto-évaluation de la conformité au Règlement IA de l'UE

## Inventaire des systèmes d'IA

| Question | Statut | Notes |
|----------|--------|-------|
| Avons-nous identifié tous les systèmes d'IA utilisés ou en développement ? | ⬜ Oui ⬜ Non ⬜ En cours | [Lister les systèmes] |
| Avons-nous classifié le niveau de risque de chaque système d'IA ? | ⬜ Oui ⬜ Non ⬜ Partiel | [Documentation de classification] |
| Avons-nous déterminé le rôle fournisseur vs. déployeur pour chaque système ? | ⬜ Oui ⬜ Non ⬜ Partiel | [Documentation des rôles] |
| Développons-nous ou utilisons-nous des MIAG ? | ⬜ Oui ⬜ Non ⬜ Incertain | [Liste des MIAG le cas échéant] |

## Pratiques interdites (Article 5)

| Exigence | Statut | Preuve | Notes |
|----------|--------|--------|-------|
| Évaluation de tous les systèmes d'IA au regard des interdictions de l'Article 5 | ⬜ Oui ⬜ Non | | |
| Confirmation d'absence d'IA de manipulation subliminale | ⬜ Oui ⬜ Non ⬜ S/O | | |
| Confirmation d'absence d'IA de notation sociale | ⬜ Oui ⬜ Non ⬜ S/O | | |
| Confirmation d'absence d'IBD-TR en temps réel (sauf exception forces de l'ordre) | ⬜ Oui ⬜ Non ⬜ S/O | | |
| Confirmation d'absence de reconnaissance émotionnelle sur le lieu de travail/enseignement (sauf sécurité/médical) | ⬜ Oui ⬜ Non ⬜ S/O | | |
| Évaluation Article 5 documentée | ⬜ Oui ⬜ Non | | |

## Systèmes d'IA à haut risque — Obligations des fournisseurs

| Exigence | Statut | Preuve | Notes |
|----------|--------|--------|-------|
| Système de gestion des risques établi (Article 9) | ⬜ Oui ⬜ Non ⬜ S/O | | |
| Gouvernance et mesures de qualité des données (Article 10) | ⬜ Oui ⬜ Non ⬜ S/O | | |
| Documentation technique préparée (Article 11, Annexe IV) | ⬜ Oui ⬜ Non ⬜ S/O | | |
| Journalisation automatique mise en œuvre (Article 12) | ⬜ Oui ⬜ Non ⬜ S/O | | |
| Instructions d'utilisation fournies (Article 13) | ⬜ Oui ⬜ Non ⬜ S/O | | |
| Mesures de surveillance humaine conçues (Article 14) | ⬜ Oui ⬜ Non ⬜ S/O | | |
| Exactitude, robustesse, cybersécurité traitées (Article 15) | ⬜ Oui ⬜ Non ⬜ S/O | | |
| Système de management de la qualité mis en œuvre (Article 16) | ⬜ Oui ⬜ Non ⬜ S/O | | |
| Évaluation de la conformité réalisée | ⬜ Oui ⬜ Non ⬜ Planifié | | |
| Marquage CE apposé (le cas échéant) | ⬜ Oui ⬜ Non ⬜ S/O | | |
| Système de surveillance post-commercialisation établi (Article 72) | ⬜ Oui ⬜ Non ⬜ S/O | | |

## Systèmes d'IA à haut risque — Obligations des déployeurs

| Exigence | Statut | Preuve | Notes |
|----------|--------|--------|-------|
| Utilisation conforme aux instructions (Article 26(1)) | ⬜ Oui ⬜ Non ⬜ S/O | | |
| Surveillance humaine désignée (Article 26(2)) | ⬜ Oui ⬜ Non ⬜ S/O | | |
| Surveillance du fonctionnement selon les instructions (Article 26(3)) | ⬜ Oui ⬜ Non ⬜ S/O | | |
| Procédures de suspension en cas d'incident grave (Article 26(4)) | ⬜ Oui ⬜ Non ⬜ S/O | | |
| Journaux conservés (Article 26(5)) | ⬜ Oui ⬜ Non ⬜ S/O | | |
| Données en entrée pertinentes et représentatives (Article 26(6)) | ⬜ Oui ⬜ Non ⬜ S/O | | |
| EIDF réalisée (Article 27, le cas échéant) | ⬜ Oui ⬜ Non ⬜ S/O | | |

## Systèmes d'IA à risque limité

| Exigence | Statut | Preuve | Notes |
|----------|--------|--------|-------|
| Chatbot/assistant virtuel signale l'interaction avec l'IA (Article 50(1)) | ⬜ Oui ⬜ Non ⬜ S/O | | |
| Reconnaissance émotionnelle/catégorisation biométrique informe les utilisateurs (Article 50(2)) | ⬜ Oui ⬜ Non ⬜ S/O | | |
| Contenu hypertrucage divulgué (Article 50(3)) | ⬜ Oui ⬜ Non ⬜ S/O | | |
| Texte généré par IA divulgué (Article 50(4)) | ⬜ Oui ⬜ Non ⬜ S/O | | |

## Modèles d'IA à usage général (MIAG)

| Exigence | Statut | Preuve | Notes |
|----------|--------|--------|-------|
| Documentation technique préparée (Article 53, Annexe XI) | ⬜ Oui ⬜ Non ⬜ S/O | | |
| Information pour les fournisseurs en aval (Article 53(1)(b)) | ⬜ Oui ⬜ Non ⬜ S/O | | |
| Politique droits d'auteur documentée (Article 53(1)(c)) | ⬜ Oui ⬜ Non ⬜ S/O | | |
| Résumé du contenu d'entraînement publié (Article 53(1)(d)) | ⬜ Oui ⬜ Non ⬜ S/O | | |
| Évaluation du risque systémique (≥10^25 FLOPs ou autres critères) | ⬜ Oui ⬜ Non ⬜ S/O | | |
| **Si risque systémique** : Évaluation du modèle / red teaming (Article 54(1)(a)) | ⬜ Oui ⬜ Non ⬜ S/O | | |
| **Si risque systémique** : Suivi des incidents graves (Article 54(1)(b)) | ⬜ Oui ⬜ Non ⬜ S/O | | |
| **Si risque systémique** : Cybersécurité / protection du modèle (Article 54(1)(c)) | ⬜ Oui ⬜ Non ⬜ S/O | | |
| **Si risque systémique** : Rapport sur l'efficacité énergétique (Article 54(1)(d)) | ⬜ Oui ⬜ Non ⬜ S/O | | |

## Exigences organisationnelles

| Exigence | Statut | Preuve | Notes |
|----------|--------|--------|-------|
| Structure de gouvernance IA établie | ⬜ Oui ⬜ Non ⬜ En cours | | |
| Formation à la culture de l'IA pour le personnel (Article 4) | ⬜ Oui ⬜ Non ⬜ Planifié | | |
| Inventaire des systèmes d'IA maintenu | ⬜ Oui ⬜ Non ⬜ En cours | | |
| Rôles et responsabilités attribués | ⬜ Oui ⬜ Non ⬜ Partiel | | |

---

# Annexe B : Organigramme de classification des systèmes d'IA à haut risque

```
┌─────────────────────────────────────────┐
│   S'agit-il d'un système d'IA ?         │
│   (définition Article 3(1))             │
└──────────────┬──────────────────────────┘
               │ OUI
               ↓
┌─────────────────────────────────────────┐
│   Est-il interdit au titre de           │
│   l'Article 5 ?                         │
│   (Notation sociale, manipulation       │
│    subliminale, IBD-TR en public, etc.) │
└──────────────┬──────────────────────────┘
               │ NON (Si OUI → STOP, interdit)
               ↓
┌─────────────────────────────────────────┐
│   Est-il listé à l'Annexe III ?         │
│   (Identification biométrique, infra.   │
│    critiques, emploi, enseignement,     │
│    forces de l'ordre, notation de       │
│    crédit, etc.)                        │
└──────────────┬──────────────────────────┘
         OUI   │   NON
               ↓
┌─────────────────────────────────────────┐
│   OU : Est-il un composant de sécurité  │
│   d'un produit relevant de la           │
│   législation Annexe I ?                │
└──────────────┬──────────────────────────┘
         OUI   │   NON
               ↓
┌─────────────────────────────────────────┐
│   SYSTÈME D'IA À HAUT RISQUE            │
│                                         │
│   Exigences :                           │
│   - Gestion des risques (Art. 9)        │
│   - Gouvernance des données (Art. 10)   │
│   - Documentation technique (Art. 11)  │
│   - Journalisation (Art. 12)            │
│   - Transparence (Art. 13)              │
│   - Surveillance humaine (Art. 14)      │
│   - Exactitude/robustesse (Art. 15)     │
│   - SMQ (Art. 16)                       │
│   - Évaluation conformité (Art. 43–51) │
│   - Surveillance post-comm. (Art. 72)  │
└──────────────┬──────────────────────────┘
               │
          (Fin — Haut risque)

        (NON issu du contrôle Annexe III/I)
               ↓
┌─────────────────────────────────────────┐
│   Exige-t-il de la transparence ?       │
│   - Chatbot/interaction avec humains ?  │
│   - Reconnaissance émotions/catég.      │
│     biométrique ?                       │
│   - Génère des hypertrucages/contenus   │
│     synthétiques ?                      │
│   - Génère du texte à des fins          │
│     d'information publique ?            │
└──────────────┬──────────────────────────┘
         OUI   │   NON
               ↓
┌─────────────────────────────────────────┐
│   SYSTÈME D'IA À RISQUE LIMITÉ          │
│                                         │
│   Exigences :                           │
│   - Obligations de transparence         │
│     (Art. 50)                           │
│   - Divulguer l'interaction IA/contenu  │
└──────────────┬──────────────────────────┘
               │
          (Fin — Risque limité)

        (NON issu du contrôle transparence)
               ↓
┌─────────────────────────────────────────┐
│   SYSTÈME D'IA À RISQUE MINIMAL         │
│                                         │
│   Exigences :                           │
│   - Aucune obligatoire                  │
│   - Codes de conduite volontaires       │
│     (Art. 95)                           │
└─────────────────────────────────────────┘
```

---

**FIN DE LA RÉFÉRENCE TECHNIQUE**

---

*Cette référence technique soutient les exigences potentielles de conformité au Règlement IA de l'UE telles que déterminées dans ISMS-POL-00. Toutes les déterminations d'applicabilité réglementaire et exigences contraignantes sont définies dans ISMS-POL-00 et les documents de politique SMSI approuvés.*

*Pour les organisations ne développant pas ni ne déployant des systèmes d'IA affectant des personnes dans l'UE, ce document est fourni à titre de sensibilisation informative uniquement et ne crée aucune obligation de conformité.*

<!-- QA_VERIFIED: 2026-03-30 -->
