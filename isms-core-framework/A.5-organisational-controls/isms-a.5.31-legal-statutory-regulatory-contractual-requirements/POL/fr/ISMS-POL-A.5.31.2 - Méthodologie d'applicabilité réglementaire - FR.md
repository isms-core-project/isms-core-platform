<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.31.2-FR:framework:POL:a.5.31.2 -->
**ISMS-POL-A.5.31.2 — Méthodologie d'applicabilité réglementaire**
**Exigences légales, statutaires, réglementaires et contractuelles**

**Contrôle documentaire**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Exigences légales, statutaires, réglementaires et contractuelles : Méthodologie d'applicabilité réglementaire |
| **Type de document** | Politique |
| **Identifiant du document** | ISMS-POL-A.5.31.2 |
| **Créateur du document** | Responsable de la sécurité des systèmes d'information (RSSI) |
| **Propriétaire du document** | Directeur général (DG) |
| **Approuvé par** | Direction générale |
| **Date de création** | [Date] |
| **Version** | 1.0 |
| **Date de version** | [À déterminer] |
| **Classification** | Interne |
| **Statut** | Brouillon |

**Historique des versions** :

| Version | Date | Auteur | Modifications |
|---------|------|--------|---------------|
| 1.0 | [Date] | RSSI/RSI | Cadre de politique initial pour la première certification ISO 27001:2022 |

---

# Introduction et contexte du cadre

## Objectif de cette section de politique

Cette section de politique établit la méthodologie systématique par laquelle [Organisation] identifie, évalue et catégorise les exigences légales, statutaires, réglementaires et contractuelles applicables à son programme de sécurité de l'information.

La méthodologie définie ici transforme la conformité réglementaire d'une activité réactive et ponctuelle en un processus systématique et reproductible qui produit des déterminations d'applicabilité réglementaire cohérentes et défendables.

## Relation avec le cadre de conformité

ISMS-POL-A.5.31.1 (Résumé exécutif et alignement des contrôles) a établi le cadre global de conformité réglementaire et la structure de gouvernance. Cette section de politique (5.31.2) fournit la **première méthodologie opérationnelle** dans ce cadre : le processus pour déterminer **quelles réglementations s'appliquent** à [Organisation].

Les résultats de cette méthodologie alimentent et maintiennent directement **ISMS-POL-00 (Cadre d'applicabilité réglementaire)** — le registre officiel des réglementations applicables.

**Flux du cadre :**
```
Contrôle ISO 27001:2022 A.5.31
         ↓
POL-5.31.1 : Foundation & Gouvernance du cadre
         ↓
POL-5.31.2 : Méthodologie d'applicabilité ← VOUS ÊTES ICI
         ↓ (produit des entrées pour)
ISMS-POL-00 : Registre réglementaire
         ↓ (alimente)
POL-5.31.3 : Extraction des exigences & Cartographie des contrôles
         ↓
POL-5.31.4 : Gestion des changements & Preuves
```

## L'approche systématique vs. ponctuelle

**Approche ponctuelle traditionnelle :**

- « Nous opérons dans le Pays X, donc nous devons probablement nous conformer à la loi sur la protection des données du Pays X »
- « Le Client Y a mentionné la réglementation Z dans son appel d'offres, je suppose donc qu'elle s'applique »
- « J'ai entendu lors d'une conférence que la réglementation ABC est importante »
- Pas de justification documentée des décisions
- Critères appliqués de manière incohérente selon les réglementations
- Pas de processus de révision systématique

**Approche systématique de ce cadre :**

- Des événements déclencheurs définis lancent les évaluations d'applicabilité
- Plusieurs sources systématiquement analysées pour identifier les réglementations potentiellement applicables
- Évaluation structurée utilisant des critères tridimensionnels cohérents
- Justification documentée avec preuves à l'appui
- Flux d'approbation formel
- Révision et validation périodiques
- Piste d'audit complète

L'approche systématique garantit que :

- Différents évaluateurs parviennent aux mêmes conclusions (reproductibilité)
- Les décisions sont défendables devant les auditeurs et régulateurs
- Les déterminations d'applicabilité sont traçables et réversibles
- Les changements de circonstances déclenchent une réévaluation
- Rien ne passe à travers les mailles du filet

## Intégration avec ISMS-POL-00

ISMS-POL-00 sert de **registre réglementaire officiel** pour [Organisation]. Cette politique définit les **processus par lesquels les réglementations entrent, sont catégorisées et sortent de POL-00**.

**Relation clé :**

- **Cette politique (POL-5.31.2)** définit la méthodologie d'évaluation de l'applicabilité
- **POL-00** contient les résultats de l'application de cette méthodologie (la liste des réglementations applicables)
- **IMP-5.31.1** (Processus d'évaluation de l'applicabilité) fournit des procédures opérationnelles étape par étape pour exécuter cette méthodologie
- **Classeur d'évaluation 2** (Matrice d'applicabilité) fournit des outils structurés de documentation

## Périmètre du document

Cette section de politique couvre :

- **Événements déclencheurs** lançant les évaluations d'applicabilité (Section 2.1)
- **Sources** pour identifier les réglementations potentiellement applicables (Section 2.2)
- **Filtrage initial** pour sélectionner les candidats (Section 2.3)
- Méthodologie d'**évaluation d'applicabilité tridimensionnelle** (Section 3)
- Cadre de **catégorisation à trois niveaux** (Section 4)
- Exigences de **documentation et d'approbation** (Section 5)
- **Fréquence de révision et déclencheurs** de réévaluation (Section 6)

Cette politique ne couvre PAS :

- L'extraction des exigences des réglementations applicables (couverte dans POL-5.31.3)
- La cartographie des exigences aux contrôles (couverte dans POL-5.31.3)
- La surveillance des changements réglementaires (couverte dans POL-5.31.4)
- La gestion des preuves (couverte dans POL-5.31.4)

---

# Processus d'identification réglementaire

## Événements déclencheurs pour l'identification réglementaire

[Organisation] doit lancer l'identification réglementaire et les évaluations d'applicabilité lors des événements déclencheurs suivants :

### Déclencheurs de révision périodique

**Révision complète annuelle** (Obligatoire) :

- Analyse complète du paysage réglementaire
- Révision de toutes les entrées dans ISMS-POL-00 pour confirmer l'applicabilité continue
- Validation qu'aucune réglementation applicable n'a été manquée
- Réalisée au T4 de chaque année civile (ou selon le calendrier SMSI défini)
- Responsabilité : Responsable de la conformité en coordination avec la Fonction juridique

**Analyse trimestrielle de l'environnement** (Recommandée) :

- Analyse ciblée des développements réglementaires dans les juridictions clés
- Révision des alertes de surveillance réglementaire accumulées pendant le trimestre
- Identification des réglementations nouvelles ou proposées nécessitant attention
- Réalisée à la fin de chaque trimestre
- Responsabilité : Responsable de la conformité

### Déclencheurs d'expansion

Une évaluation d'applicabilité doit être lancée lorsque [Organisation] :

**Entre sur un nouveau marché géographique :**

- Établit une entité juridique dans une nouvelle juridiction
- Ouvre un bureau ou une installation opérationnelle dans un nouvel emplacement
- Commence à commercialiser ou vendre des services dans un nouveau pays ou région
- Traite des données de personnes dans une nouvelle juridiction

**Offre de nouveaux services ou produits :**

- Lance une nouvelle offre de services (ex. services cloud, sécurité managée, conseil)
- Entre dans un nouveau marché vertical (ex. santé, services financiers, gouvernement)
- Commence à traiter de nouvelles catégories de données (ex. données de santé, financières, biométriques)
- Adopte de nouvelles technologies avec des implications réglementaires (ex. IA, blockchain)

**Acquiert des clients dans des secteurs réglementés :**

- Signe des contrats avec un client dans un secteur hautement réglementé (finance, santé, énergie, etc.)
- La relation implique l'accès aux données ou systèmes réglementés du client
- Le client opère dans une juridiction nouvelle pour [Organisation]

**Fusions et acquisitions :**

- [Organisation] acquiert une autre entité (hérite de ses obligations réglementaires)
- [Organisation] est acquise (peut déclencher de nouvelles obligations de la société mère)
- Déclenche une révision complète du paysage réglementaire combiné

### Déclencheurs contractuels

**Nouveaux contrats clients :**

- Le contrat client inclut des exigences de conformité spécifiques
- Le client mène un questionnaire de diligence raisonnable en matière de conformité
- L'appel d'offres inclut des exigences réglementaires ou de certification
- Le contrat-cadre de services inclut des clauses de conformité réglementaire

**Nouveaux accords fournisseurs :**

- L'accord fournisseur crée des obligations de conformité répercutées
- [Organisation] est désignée comme sous-traitant ou prestataire avec des obligations héritées
- Les certifications du fournisseur exigent que [Organisation] respecte des normes spécifiques

**Accords de partenariat et de revendeur :**

- Offre conjointe nécessitant la conformité aux obligations du partenaire
- Le partenaire technologique exige une posture de conformité spécifique
- L'accord de revendeur inclut des engagements de conformité

### Déclencheurs de certification et d'accréditation

**Poursuite de nouvelles certifications :**

- Décision de poursuivre ISO 27001, SOC 2, PCI DSS v4.0.1 ou autre certification
- L'organisme de certification spécifie des exigences réglementaires dans le cadre de la certification
- Accréditations sectorielles avec composantes de conformité

**Maintenance des certifications :**

- L'audit de surveillance identifie de nouvelles exigences réglementaires
- La norme de certification est mise à jour avec de nouvelles références réglementaires
- L'organisme de certification publie de nouvelles orientations sur les attentes réglementaires

### Déclencheurs internes

**Initiatives stratégiques :**

- La stratégie d'affaires prévoit d'entrer sur des marchés réglementés
- L'initiative de transformation numérique implique des technologies réglementées
- Le développement de nouveaux produits avec des implications réglementaires

**Résultats de l'évaluation des risques :**

- L'évaluation des risques de sécurité de l'information identifie une exposition réglementaire
- L'analyse d'impact sur la protection des données révèle une applicabilité réglementaire potentielle
- Les renseignements sur les menaces indiquent une application réglementaire dans le domaine de [Organisation]

**Identification d'écarts de conformité :**

- L'audit interne identifie une réglementation potentiellement applicable non incluse dans POL-00
- Un employé signale une réglementation potentiellement applicable
- L'auto-évaluation de conformité révèle une lacune de connaissance

### Déclencheurs externes

**Adoption de réglementations :**

- Nouvelle loi ou réglementation adoptée dans une juridiction où [Organisation] opère
- L'autorité réglementaire publie de nouvelles règles ou orientations
- Traité ou accord international avec des implications de conformité

**Développements sectoriels :**

- Une association sectorielle publie de nouvelles normes ou orientations
- Des organisations comparables reçoivent des mesures d'application réglementaire
- Un groupe de travail sectoriel recommande l'adoption d'un cadre spécifique

**Demande réglementaire :**

- Une autorité réglementaire contacte directement [Organisation]
- Enquête sectorielle d'un organisme réglementaire
- Enquête ou mesure d'application réglementaire dans le secteur de [Organisation]

## Sources de veille réglementaire

[Organisation] doit utiliser les sources suivantes pour identifier les réglementations potentiellement applicables :

### Bases de données juridiques et services de recherche

**Plateformes commerciales de recherche juridique :**

- Services à abonnement (ex. LexisNexis, Westlaw, Bloomberg Law)
- Accès aux statuts, réglementations, codes administratifs dans plusieurs juridictions
- Fonctionnalité d'alerte pour les changements réglementaires
- Recherche par juridiction, sujet, secteur, date d'entrée en vigueur

**Bases de données juridiques gouvernementales :**

- Référentiels gouvernementaux officiels (ex. EUR-Lex pour l'UE, Registre fédéral pour les États-Unis)
- Bases de données législatives nationales
- Sites web des autorités réglementaires
- Gratuits mais peuvent manquer de recherche avancée et d'alertes

**Plateformes de technologie réglementaire (RegTech) :**

- Services spécialisés de surveillance de la conformité (ex. Compliance.ai, RegHub)
- Détection des changements réglementaires assistée par l'IA
- Suivi réglementaire spécifique au secteur
- Comprend souvent l'interprétation et l'analyse d'impact

**Lignes directrices d'utilisation :**

- Maintenir des abonnements à jour aux plateformes principales de recherche juridique
- Configurer des alertes pour les juridictions et sujets clés
- Formation régulière du personnel de conformité à l'utilisation efficace des bases de données
- Documenter les requêtes de recherche et résultats pour la piste d'audit

### Associations sectorielles et organismes de normalisation

**Associations sectorielles :**

- Associations commerciales sectorielles dans les secteurs que [Organisation] sert
- Les associations publient des mises à jour réglementaires, des guides de conformité et des meilleures pratiques
- Exemples : associations de services financiers, groupes du secteur de la santé, consortiums technologiques

**Organisations intersectorielles :**

- Associations professionnelles de sécurité de l'information et de protection de la vie privée (ex. IAPP, (ISC)², ISACA)
- Organisations de qualité et de conformité (ex. organes nationaux ISO)
- Organisations d'affaires régionales

**Organismes de développement de normes :**

- ISO (Organisation internationale de normalisation)
- NIST (National Institute of Standards and Technology)
- CIS (Center for Internet Security)
- Organismes de normalisation spécifiques au secteur

**Lignes directrices d'utilisation :**

- Maintenir des adhésions dans les associations pertinentes
- S'abonner aux bulletins d'information et alertes sur les mises à jour réglementaires
- Participer aux groupes de travail sectoriels sur les sujets réglementaires
- Assister aux conférences et webinaires sur les développements réglementaires

### Conseil juridique

**Équipe juridique interne :**

- Source principale d'interprétation juridique des réglementations
- Surveille les développements juridiques pertinents pour [Organisation]
- Fournit des conseils juridiques continus sur les questions de conformité
- Coordonne avec le conseil externe si nécessaire

**Conseillers juridiques externes :**

- Conseil spécialisé par juridiction (pour les opérations internationales)
- Conseil réglementaire spécialisé (ex. protection des données, réglementation financière)
- Engagé pour des questions spécifiques ou une surveillance réglementaire continue

**Conseil réglementaire spécialisé :**

- Expertise approfondie dans des domaines réglementaires spécifiques
- Retenu pour les questions de conformité complexes
- Fournit des avis sur l'applicabilité et l'interprétation réglementaires

**Lignes directrices d'utilisation :**

- Réunions juridiques régulières (au moins trimestrielles) sur le paysage réglementaire
- Point permanent à l'ordre du jour des réunions Juridique/Conformité
- Révision juridique de toutes les déterminations d'applicabilité de Niveau 1
- Conseil externe engagé pour les juridictions où [Organisation] manque d'expertise interne

### Réseaux de pairs et communautés professionnelles

**Forums sectoriels :**

- Forums de conformité et juridiques au sein du secteur
- Centres de partage et d'analyse de l'information (ISAC)
- Groupes de discussion entre pairs sur les sujets réglementaires

**Associations professionnelles :**

- Réseaux de responsables de la conformité
- Communautés de délégués à la protection des données
- Groupes professionnels de la sécurité de l'information

**Communautés de pratique en conformité :**

- Collaboration de conformité entre entreprises
- Comparaison et partage de meilleures pratiques
- Discussions sur l'interprétation réglementaire

**Lignes directrices d'utilisation :**

- Participation active dans au moins un réseau de pairs pertinent
- Les représentants désignés assistent aux réunions régulières
- Partager les apprentissages dans le respect de la confidentialité
- Vérifier les informations des pairs auprès de sources officielles avant d'agir

### Cabinets de services professionnels

**Cabinets d'audit :**

- Les Big 4 et les cabinets d'audit régionaux publient des mises à jour réglementaires
- Alertes réglementaires spécifiques au secteur
- Services de conseil en conformité
- Fournissent souvent des briefings réglementaires gratuits aux clients

**Consultants en conformité :**

- Conseil réglementaire spécialisé en conformité
- Évaluations des programmes de conformité réglementaire
- Services d'analyse des écarts de conformité

**Services de surveillance réglementaire :**

- Surveillance des changements réglementaires par des tiers
- Alertes et résumés sélectionnés
- Évaluations d'impact et recommandations

**Lignes directrices d'utilisation :**

- S'abonner aux services de mise à jour réglementaire du cabinet d'audit ou du consultant
- Assister aux briefings clients et webinaires
- Utiliser les prestataires de services professionnels pour les évaluations complexes
- Maintenir des relations pour les consultations ponctuelles

### Canaux clients et fournisseurs

**Exigences clients :**

- Clauses de conformité dans les contrats-cadres de services
- Questionnaires de sécurité et de conformité (ex. SIG, CAIQ)
- Exigences de conformité dans les appels d'offres
- Audits et évaluations de conformité clients

**Obligations fournisseurs :**

- Accords de traitement des données (ATD) avec obligations héritées
- Accords de sous-traitants
- Exigences de conformité de la chaîne d'approvisionnement
- Questionnaires d'évaluation des fournisseurs

**Lignes directrices d'utilisation :**

- Révision systématique de tous les contrats clients pour les clauses de conformité
- Révision juridique des accords fournisseurs pour les obligations répercutées
- Maintenir une base de données des exigences de conformité contractuelles
- Intégrer les exigences contractuelles dans le processus d'évaluation de l'applicabilité

## Critères de filtrage initial

Avant de mener une évaluation complète de l'applicabilité, [Organisation] doit appliquer un filtrage initial pour réduire l'univers des réglementations à un ensemble de candidats gérable :

### Filtrage par pertinence

**Question** : Cette réglementation est-elle relative à la sécurité de l'information, la protection des données, les services informatiques ou les actifs informationnels de [Organisation] ?

**Appliquer à** :

- Réglementations régissant la protection des données, la confidentialité, la cybersécurité
- Réglementations régissant les services informatiques, cloud, managés
- Réglementations régissant des types spécifiques de données que [Organisation] traite
- Réglementations régissant les systèmes d'information et l'infrastructure technologique
- Réglementations avec des dispositions de sécurité de l'information (même si le périmètre est plus large)

**Exclure** :

- Réglementations purement opérationnelles sans rapport avec l'information/les TI (ex. sécurité au travail, environnemental)
- Réglementations de rapport financier sans composantes de sécurité de l'information
- Réglementations de sécurité des produits pour des produits physiques que [Organisation] ne produit pas
- Réglementations clairement hors du domaine de [Organisation]

**Résultat** : Si la réglementation n'est PAS pertinente pour la sécurité de l'information ou les TI, **ARRÊTER** — ne pas procéder à l'évaluation complète. Documenter la justification et classer dans « Filtré — Non pertinent ».

### Filtrage juridictionnel

**Question** : [Organisation] a-t-elle un lien quelconque avec la juridiction où cette réglementation s'applique ?

**Les liens incluent** :

- Présence physique (bureau, installation, employés) dans la juridiction
- Entité juridique enregistrée dans la juridiction
- Clients ou personnes concernées situés dans la juridiction
- Prestation de services dans la juridiction (même sans présence physique)
- Traitement de données soumises aux lois de la juridiction
- La réglementation revendique une portée extraterritoriale affectant [Organisation]

**Résultat** : Si [Organisation] n'a AUCUN lien avec la juridiction et que la réglementation ne fait AUCUNE revendication extraterritoriale, probablement non applicable. Toutefois, procéder à l'évaluation complète si :

- Incertitude sur la portée extraterritoriale
- Expansion potentielle future vers la juridiction
- Lien indirect via des clients ou fournisseurs

### Filtrage opérationnel

**Question** : Les opérations actuelles ou prévues de [Organisation] relèvent-elles du périmètre de cette réglementation ?

**Vérifier** :

- Types de services fournis par [Organisation] vs. périmètre de la réglementation
- Secteurs que [Organisation] sert vs. critères d'applicabilité de la réglementation
- Types de données que [Organisation] traite vs. périmètre de la réglementation
- Taille, revenus ou autres seuils de [Organisation] vs. critères d'applicabilité de la réglementation

**Résultat** : Si la réglementation ne s'applique clairement PAS aux opérations de [Organisation] (ex. réglementation de la santé lorsque [Organisation] ne sert pas le secteur de la santé et ne traite pas de données de santé), probablement non applicable. Procéder à l'évaluation complète si :

- Incertitude sur le périmètre
- Des opérations futures potentielles pourraient déclencher l'applicabilité
- Chevauchement partiel avec les opérations actuelles

### Matrice de décision de filtrage

| Pertinence | Juridiction | Opérations | Décision |
|------------|-------------|------------|----------|
| NON pertinente | Quelconque | Quelconque | **ARRÊTER** — Filtré |
| Pertinente | AUCUN lien | NON applicable | **ARRÊTER** — Probablement non applicable (documenter) |
| Pertinente | AUCUN lien | Potentiellement applicable | **PROCÉDER** — Évaluation complète (futur potentiel) |
| Pertinente | Lien | NON applicable | **PROCÉDER** — Évaluation complète (vérifier non applicable) |
| Pertinente | Lien | Potentiellement applicable | **PROCÉDER** — Évaluation complète |
| Pertinente | Lien | Clairement applicable | **PROCÉDER** — Évaluation complète (probablement applicable) |

### Documentation du filtrage

Pour chaque réglementation filtrée :

- Documenter le nom de la réglementation, la juridiction, une brève description
- Enregistrer la décision de filtrage (Procéder à l'évaluation complète / Filtré)
- Fournir la justification de la décision
- Référencer la source où elle a été identifiée
- Date et nom de l'évaluateur

Les réglementations filtrées doivent être conservées dans un fichier « Examinées mais non applicables » pour référence future potentielle si les circonstances changent.

---

# Cadre des critères d'applicabilité

Pour les réglementations qui passent le filtrage initial, [Organisation] doit mener une évaluation d'applicabilité structurée utilisant un **cadre tridimensionnel** :

1. **Périmètre géographique** : Applicabilité basée sur OÙ [Organisation] opère
2. **Périmètre opérationnel** : Applicabilité basée sur CE QUE [Organisation] fait
3. **Périmètre contractuel** : Applicabilité basée sur les ACCORDS que [Organisation] a conclus

Chaque dimension est évaluée indépendamment, puis combinée pour une détermination globale de l'applicabilité.

## Évaluation du périmètre géographique

### Critères d'applicabilité géographique

**Critère G1 : Opérations dans la juridiction**

Question : [Organisation] mène-t-elle des opérations dans la juridiction où cette réglementation s'applique ?

Considérer :

- Bureaux, installations ou centres de données physiques dans la juridiction
- Employés travaillant depuis la juridiction
- Entités juridiques constituées ou enregistrées dans la juridiction
- Licences commerciales ou permis dans la juridiction

Preuves : Registres d'entreprise, baux de bureaux, dossiers d'emploi, enregistrements de licences commerciales

**Critère G2 : Clients ou personnes concernées dans la juridiction**

Question : [Organisation] sert-elle des clients physiquement situés dans la juridiction, ou traite-t-elle des données de personnes dans la juridiction ?

Considérer :

- Contrats clients avec des parties situées dans la juridiction
- Utilisateurs finaux accédant aux services de [Organisation] depuis la juridiction
- Personnes concernées dont les données personnelles sont protégées par les lois de la juridiction
- Activités de marketing ou de vente ciblant la juridiction

Preuves : Contrats clients, registres de ventes, analyses de trafic web, registres de traitement des données

**Critère G3 : Ciblage de la juridiction**

Question : [Organisation] cible-t-elle activement des personnes ou entités dans la juridiction ?

Considérer :

- Site web disponible dans la/les langue(s) de la juridiction
- Prix affichés dans la devise de la juridiction
- Campagnes marketing dirigées vers la juridiction
- Modes de paiement locaux acceptés
- Conformité aux lois de protection des consommateurs de la juridiction

Preuves : Contenu du site web, matériaux marketing, configurations de passerelle de paiement

**Critère G4 : Traitement des données dans la juridiction**

Question : [Organisation] traite-t-elle des données dans la juridiction, même si [Organisation] n'y a aucune autre présence ?

Considérer :

- Serveurs ou infrastructure situés dans la juridiction
- Prestataires de services tiers dans la juridiction traitant des données au nom de [Organisation]
- Données en transit via la juridiction
- Sites de sauvegarde ou de reprise après sinistre dans la juridiction

Preuves : Schémas d'infrastructure, accords fournisseurs, documentation des flux de données

**Critère G5 : Application extraterritoriale**

Question : La réglementation revendique-t-elle explicitement de s'appliquer au-delà des frontières de sa juridiction ?

Considérer :

- La réglementation s'applique aux organisations hors juridiction si elles servent des résidents
- La réglementation s'applique selon l'emplacement de la personne concernée quel que soit l'emplacement de l'organisation
- Exemples : RGPD (UE), CCPA (Californie), LGPD (Brésil) ont toutes des dispositions extraterritoriales

Preuves : Texte réglementaire, analyse juridique des dispositions extraterritoriales

### Notation du périmètre géographique

Pour chaque critère G1 à G5 :

- **OUI** = 1 point
- **NON** = 0 point
- **INCERTAIN** = 0,5 point (déclenche une révision juridique)

**Score d'applicabilité géographique** = Somme de G1 à G5 (plage : 0 à 5)

**Interprétation** :

- 0 à 1 point : Faible applicabilité géographique
- 2 à 3 points : Applicabilité géographique modérée
- 4 à 5 points : Forte applicabilité géographique

Un score élevé indique un lien géographique fort suggérant l'applicabilité. Cependant, le score seul ne détermine PAS l'applicabilité finale — il faut considérer les trois dimensions.

## Évaluation du périmètre opérationnel

### Critères d'applicabilité opérationnelle

**Critère O1 : Alignement du type de service**

Question : [Organisation] fournit-elle des types de services qui relèvent du périmètre de la réglementation ?

Considérer :

- Services cloud, hébergement, SaaS (peut déclencher les réglementations cloud/services informatiques)
- Traitement des paiements (peut déclencher les réglementations des services financiers)
- Services de santé ou traitement de données de santé (peut déclencher les réglementations de la santé)
- Services de télécommunication (peut déclencher les réglementations télécom)
- Services d'infrastructure critique (peut déclencher les réglementations de protection des IC)

Preuves : Catalogue de services, descriptions de services, déclarations de travaux, matériaux marketing

**Critère O2 : Alignement du secteur industriel**

Question : [Organisation] sert-elle des secteurs industriels réglementés par cette réglementation ?

Considérer :

- Secteur des services financiers (banques, sociétés d'investissement, assurances)
- Secteur de la santé (prestataires, payeurs, technologie de la santé)
- Secteur gouvernemental (secteur public, défense)
- Secteurs d'infrastructure critique (énergie, eau, transport)
- La réglementation peut s'appliquer aux prestataires de services À ces secteurs même si non dans le secteur directement

Preuves : Liste des clients, analyse des marchés verticaux, contrats spécifiques au secteur

**Critère O3 : Alignement du type de données**

Question : [Organisation] traite-t-elle des types de données qui sont protégées ou réglementées par cette réglementation ?

Considérer :

- Données personnelles / Données à caractère personnel (DCP)
- Catégories spéciales de données personnelles (santé, biométriques, génétiques, race/ethnie, etc.)
- Données financières (données de carte de paiement, données bancaires, informations de compte financier)
- Données gouvernementales (classifiées, non classifiées contrôlées, données des forces de l'ordre)
- Secrets commerciaux ou informations commerciales confidentielles
- Données d'enfants

Preuves : Inventaire des données, registre de classification des données, schémas de flux de données, registres de traitement des données

**Critère O4 : Caractéristiques organisationnelles**

Question : [Organisation] satisfait-elle aux seuils d'applicabilité de la réglementation basés sur la taille, les revenus ou d'autres caractéristiques ?

Considérer :

- Nombre d'employés (certaines réglementations s'appliquent uniquement au-delà d'un seuil)
- Chiffre d'affaires annuel (seuils financiers)
- Volume de données traitées (ex. nombre de personnes concernées)
- Entité publique vs. privée
- À but lucratif vs. sans but lucratif
- Structure organisationnelle (filiale d'une société mère réglementée)

Preuves : États financiers, rapports sur les effectifs, métriques de volume de traitement des données, documents de structure d'entreprise

**Critère O5 : Opérations spécifiques couvertes**

Question : [Organisation] effectue-t-elle des opérations ou activités spécifiques explicitement couvertes par la réglementation ?

Considérer :

- Opérations de commerce électronique (peut déclencher les réglementations de protection des consommateurs/e-commerce)
- Transferts de données transfrontaliers (peut déclencher les réglementations de transfert de données)
- Prise de décision automatisée ou profilage (peut déclencher les réglementations IA/algorithmiques)
- Marketing/publicité utilisant des données personnelles (peut déclencher les réglementations marketing)
- Authentification/identification biométrique (peut déclencher les réglementations biométriques)

Preuves : Documentation opérationnelle, documentation technologique, descriptions de processus

### Notation du périmètre opérationnel

Pour chaque critère O1 à O5 :

- **OUI** = 1 point
- **NON** = 0 point
- **INCERTAIN** = 0,5 point (déclenche une analyse supplémentaire)

**Score d'applicabilité opérationnelle** = Somme de O1 à O5 (plage : 0 à 5)

**Interprétation** :

- 0 à 1 point : Faible applicabilité opérationnelle
- 2 à 3 points : Applicabilité opérationnelle modérée
- 4 à 5 points : Forte applicabilité opérationnelle

## Évaluation du périmètre contractuel

### Critères d'applicabilité contractuelle

**Critère C1 : Exigences contractuelles clients**

Question : Les contrats clients de [Organisation] exigent-ils explicitement la conformité à cette réglementation ?

Considérer :

- Contrats-cadres de services avec des clauses de conformité
- Accords de traitement des données exigeant la conformité du responsable du traitement
- Déclarations de travaux avec des exigences réglementaires spécifiques
- Questionnaires de conformité client attendant la conformité
- Clauses de droit d'audit couvrant la conformité réglementaire

Preuves : Contrats clients exécutés, matrices d'exigences de conformité, rapports d'audit clients

**Critère C2 : Obligations contractuelles fournisseurs répercutées**

Question : Les accords de [Organisation] avec les fournisseurs créent-ils des obligations pour [Organisation] de se conformer à cette réglementation ?

Considérer :

- [Organisation] comme sous-traitant avec des obligations du responsable de traitement principal
- Exigences de conformité de la chaîne d'approvisionnement
- Fournisseur exigeant que [Organisation] respecte les normes que le fournisseur doit respecter
- Clauses de répercussion des contrats principaux

Preuves : Accords fournisseurs, accords de sous-traitants, contrats de chaîne d'approvisionnement

**Critère C3 : Exigences de certification**

Question : La conformité à cette réglementation est-elle requise pour les certifications que [Organisation] détient ou poursuit ?

Considérer :

- ISO 27001 peut référencer des exigences réglementaires spécifiques
- SOC 2 Type II peut inclure la conformité réglementaire dans les critères
- Certifications sectorielles exigeant la conformité réglementaire
- L'organisme de certification exige explicitement la conformité à la réglementation

Preuves : Normes de certification, exigences de l'organisme de certification, rapports d'audit, orientations de l'évaluateur

**Critère C4 : Engagements volontaires**

Question : [Organisation] a-t-elle pris des engagements publics ou des pledges volontaires pour se conformer à cette réglementation ou cadre ?

Considérer :

- Politiques de confidentialité déclarant la conformité à des réglementations spécifiques
- Matériaux marketing revendiquant des certifications ou la conformité
- Engagements publics envers des cadres (ex. Privacy Shield — exemple historique)
- Codes de conduite ou engagements sectoriels

Preuves : Politiques de confidentialité publiées, déclarations sur le site web, matériaux marketing, communiqués de presse

### Notation du périmètre contractuel

Pour chaque critère C1 à C4 :

- **OUI** = 1 point
- **NON** = 0 point
- **INCERTAIN** = 0,5 point

**Score d'applicabilité contractuelle** = Somme de C1 à C4 (plage : 0 à 4)

**Interprétation** :

- 0 point : Aucune applicabilité contractuelle
- 1 à 2 points : Applicabilité contractuelle modérée
- 3 à 4 points : Forte applicabilité contractuelle

## Détermination globale de l'applicabilité

### Pondération des dimensions

Les trois dimensions ont le même poids dans la détermination. Une réglementation peut être applicable sur la base d'un score élevé dans une dimension OU d'un score modéré dans plusieurs dimensions.

### Logique de décision d'applicabilité

**APPLICABLE** (Ajouter à ISMS-POL-00) :

- Score élevé (4-5) dans N'IMPORTE QUELLE dimension, OU
- Scores modérés (2-3) dans DEUX DIMENSIONS OU PLUS, OU
- Exigence contractuelle explicite (C1 ou C2 = OUI), OU
- L'avis juridique confirme l'applicabilité

**CONDITIONNELLEMENT APPLICABLE** (Ajouter à ISMS-POL-00 en Niveau 2) :

- Score modéré (2-3) dans UNE SEULE dimension
- Applicabilité future potentielle (plans d'expansion)
- Adoption volontaire pour un avantage concurrentiel

**NON APPLICABLE** (Ne pas ajouter à ISMS-POL-00) :

- Scores faibles (0-1) dans TOUTES les dimensions
- La réglementation exclut explicitement les opérations de [Organisation]
- L'avis juridique confirme la non-applicabilité

### Cas particuliers

**Déterminations incertaines :**
Si l'applicabilité est incertaine après évaluation :

- Escalader au conseil juridique pour interprétation
- Envisager d'engager un conseil réglementaire externe
- Documenter l'incertitude et la décision d'inclure/exclure
- Recourir par défaut à « Conditionnellement applicable » (Niveau 2) si le doute persiste

**Indicateurs contradictoires :**
Si certains critères suggèrent applicable et d'autres non :

- Le conseil juridique prend la détermination finale
- Le poids est donné aux exigences contractuelles (C1, C2) car elles créent des obligations indépendamment de l'applicabilité légale
- Documenter le conflit et la justification de la décision finale

---

# Cadre de catégorisation à trois niveaux

Les réglementations déterminées comme applicables doivent être catégorisées dans l'un des trois niveaux au sein de ISMS-POL-00 :

## Niveau 1 : Conformité obligatoire

### Définition

Les réglementations de Niveau 1 sont celles avec une **OBLIGATION LÉGALE** ou une **EXIGENCE CONTRACTUELLE OPPOSABLE**.

La non-conformité entraîne des conséquences légales ou contractuelles concrètes : amendes réglementaires, sanctions, révocation de licence, pénalités contractuelles ou perte de relations commerciales.

### Critères d'attribution

Une réglementation DOIT être classée en Niveau 1 si elle répond à L'UN des critères suivants :

**Obligation légale :**

- Statut, loi ou réglementation légalement contraignant pour [Organisation] dans les juridictions où [Organisation] opère
- Score d'applicabilité géographique élevé (4-5) ET la réglementation contient des exigences obligatoires (« doit », « est tenu de »)
- L'autorité réglementaire a compétence sur [Organisation] et pouvoir d'application
- La non-conformité peut entraîner des amendes, sanctions ou autres pénalités légales

**Opposabilité contractuelle :**

- Le contrat client exige explicitement la conformité et inclut des mécanismes d'application (pénalités, droits de résiliation)
- L'accord fournisseur crée une obligation répercutée opposable
- Engagement contractuel avec des conséquences financières ou commerciales matérielles en cas de violation

**Exigence de certification :**

- La conformité est requise pour la certification que [Organisation] détient (ex. ISO 27001, SOC 2)
- L'organisme de certification audite la conformité à la réglementation
- La perte de certification aurait un impact commercial matériel

### Traitement des réglementations de Niveau 1

Les réglementations de Niveau 1 reçoivent la priorité la plus élevée :

- **Conformité totale requise** — aucune exception sans acceptation documentée du risque
- **Approbation de la Direction générale requise** pour l'inclusion au Niveau 1 (engagement de ressources)
- **Extraction obligatoire des exigences** (POL-5.31.3, IMP-5.31.2)
- **Cartographie obligatoire des contrôles** (POL-5.31.3, IMP-5.31.3)
- **Remédiation des écarts haute priorité** — les écarts doivent être traités ou formellement acceptés
- **Audits de conformité réguliers** (internes et potentiellement externes)
- **Collecte et maintenance continues des preuves**
- **Révision annuelle minimum** — plus fréquente si la réglementation évolue activement

### Exemples de classifications de Niveau 1 (génériques)

- Loi sur la protection des données dans la juridiction où [Organisation] a des opérations et traite des données personnelles
- Réglementation des services financiers où [Organisation] fournit des services informatiques aux institutions financières et est désignée comme prestataire de services
- Contrat client avec un grand compte exigeant la conformité SOC 2 avec des pénalités contractuelles en cas de non-conformité
- Norme ISO 27001 (si [Organisation] est certifiée)

## Niveau 2 : Applicabilité conditionnelle

### Définition

Les réglementations de Niveau 2 sont celles qui **PEUVENT DEVENIR APPLICABLES** à l'avenir ou qui sont **ADOPTÉES VOLONTAIREMENT** pour des raisons stratégiques.

Celles-ci ne sont pas actuellement légalement contraignantes, mais [Organisation] les surveille en raison de leur applicabilité future potentielle ou parce que l'adoption volontaire offre un avantage concurrentiel ou stratégique.

### Critères d'attribution

Une réglementation DOIT être classée en Niveau 2 si elle répond à L'UN des critères suivants :

**Applicabilité future potentielle :**

- [Organisation] envisage de s'étendre dans une juridiction où la réglementation s'applique
- [Organisation] prévoit d'offrir des services qui déclencheraient l'applicabilité
- [Organisation] peut entrer dans un secteur industriel couvert par la réglementation
- Réglementation proposée ou en projet susceptible d'être adoptée et d'affecter [Organisation]
- Seuils pas encore atteints mais pouvant l'être avec la croissance

**Adoption volontaire :**

- Cadre de meilleures pratiques sectorielles que [Organisation] choisit d'adopter
- Différenciateur concurrentiel (la conformité dépasse les exigences)
- Attentes des clients ou exigences du marché (même sans obligation contractuelle)
- Sphère de sécurité réglementaire ou approche préférée
- Positionnement stratégique pour des opportunités futures

**Incertitude réglementaire :**

- L'évaluation de l'applicabilité est incertaine (scores modérés, périmètre peu clair)
- La portée extraterritoriale est ambiguë
- En attente de clarification juridique ou d'orientation réglementaire
- Recours par défaut au Niveau 2 en attendant la clarification

### Traitement des réglementations de Niveau 2

Les réglementations de Niveau 2 reçoivent une priorité modérée :

- **Surveillance et préparation** — rester informé des changements
- **Analyse des écarts** pour comprendre l'effort de conformité si/lorsque déclenché
- **Mise en œuvre partielle** peut survenir si stratégiquement utile
- **Extraction des exigences** optionnelle (recommandée pour l'applicabilité future à forte probabilité)
- **Révision annuelle ou bisannuelle** — évaluer si les circonstances ont changé déclenchant un passage au Niveau 1
- **Documenter la justification stratégique** pour l'adoption volontaire le cas échéant

### Exemples de classifications de Niveau 2 (génériques)

- Réglementation de protection des données dans une juridiction vers laquelle [Organisation] envisage de s'étendre
- Réglementation spécifique à un secteur pour un marché vertical que [Organisation] pourrait pénétrer
- Réglementation émergente (en projet/proposée) susceptible d'affecter [Organisation] une fois adoptée
- NIST Cybersecurity Framework (CSF) 2.0 adopté volontairement pour l'évaluation de la maturité

## Niveau 3 : Référence informative

### Définition

Les réglementations et cadres de Niveau 3 sont utilisés pour l'**ORIENTATION**, le **RÉFÉRENCEMENT** ou les **MEILLEURES PRATIQUES** uniquement.

Il n'y a AUCUNE obligation de conformité (légale ou contractuelle), mais ces cadres informent la conception des contrôles de [Organisation] et fournissent des points de référence pour l'évaluation de la maturité.

### Critères d'attribution

Une réglementation ou cadre DOIT être classifié en Niveau 3 si :

**Aucune obligation de conformité :**

- Scores d'applicabilité faibles dans les trois dimensions
- Aucune exigence légale de conformité
- Aucune exigence contractuelle de conformité
- Non requis pour aucune certification que [Organisation] détient

**Valeur de référence :**

- Meilleures pratiques reconnues par le secteur
- Utilisé par les pairs pour le référencement
- Fournit des orientations utiles pour la conception des contrôles
- Référencé par d'autres réglementations applicables
- Soutient les efforts d'évaluation et d'amélioration de la maturité

### Traitement des réglementations de Niveau 3

Les réglementations de Niveau 3 reçoivent un traitement formel minimal :

- **Référence pour la conception des contrôles** — consulté lors de la mise en œuvre ou de l'amélioration des contrôles
- **Référencement** par rapport aux normes sectorielles
- **Aucune exigence de preuves** — aucune obligation de démontrer la conformité
- **Révision périodique** (bisannuelle ou selon les besoins) — évaluer si toujours utile comme référence
- **Peut informer mais non exiger** — les contrôles peuvent être inspirés des cadres de Niveau 3 mais sans obligation

### Exemples de classifications de Niveau 3 (génériques)

- CIS Controls (Center for Internet Security Critical Security Controls)
- NIST Cybersecurity Framework (si non adopté volontairement per Niveau 2)
- OWASP (Open Web Application Security Project)
- Guides de meilleures pratiques sectorielles sans force réglementaire

## Arbre de décision pour l'attribution de niveau

```
DÉBUT : Réglementation a passé le filtrage initial
    ↓
Existe-t-il une OBLIGATION LÉGALE ?
(La réglementation est une loi dans la juridiction où [Org] opère
 ET s'applique aux opérations de [Org])
    ├─ OUI → NIVEAU 1 (Conformité obligatoire)
    └─ NON → Continuer
        ↓
Existe-t-il une EXIGENCE CONTRACTUELLE OPPOSABLE ?
(Le contrat client/fournisseur exige la conformité
 AVEC mécanisme d'application)
    ├─ OUI → NIVEAU 1 (Conformité obligatoire)
    └─ NON → Continuer
        ↓
La conformité est-elle REQUISE pour une certification que [Org] détient ?
(ISO 27001, SOC 2, etc. l'exige)
    ├─ OUI → NIVEAU 1 (Conformité obligatoire)
    └─ NON → Continuer
        ↓
Existe-t-il une APPLICABILITÉ FUTURE POTENTIELLE ?
(Plans d'expansion, trajectoire de croissance, réglementation proposée)
    ├─ OUI → NIVEAU 2 (Applicabilité conditionnelle)
    └─ NON → Continuer
        ↓
[Org] l'adopte-t-elle VOLONTAIREMENT pour des raisons stratégiques ?
(Avantage concurrentiel, attentes des clients)
    ├─ OUI → NIVEAU 2 (Applicabilité conditionnelle)
    └─ NON → Continuer
        ↓
Est-ce utile comme ORIENTATION/RÉFÉRENCEMENT ?
(Meilleures pratiques sectorielles, référence de maturité)
    ├─ OUI → NIVEAU 3 (Référence informative)
    └─ NON → NE PAS AJOUTER À POL-00
              (Non applicable, classer dans « Filtré »)
```

## Mobilité entre niveaux

Les réglementations peuvent passer d'un niveau à l'autre au fil des changements de circonstances :

**Niveau 2 → Niveau 1 :**

- [Organisation] s'étend dans la juridiction (le potentiel devient réel)
- La réglementation proposée est adoptée
- Un contrat client ajouté exigeant la conformité
- [Organisation] atteint le seuil déclenchant l'applicabilité

**Niveau 1 → Niveau 2 :**

- [Organisation] quitte la juridiction ou cesse les opérations pertinentes
- La réglementation est abrogée ou substantiellement amendée pour exclure [Organisation]
- Le contrat expire sans renouvellement

**Niveau 3 → Niveau 2 :**

- [Organisation] décide d'adopter volontairement le cadre pour des raisons stratégiques

**Tout niveau → Suppression :**

- La réglementation est entièrement abrogée
- [Organisation] détermine définitivement la non-applicabilité après la classification initiale
- Le cadre est remplacé ou n'est plus utile

Les changements de niveau nécessitent une réévaluation utilisant la méthodologie complète d'applicabilité et l'approbation appropriée (voir Section 5).

---

# Exigences de documentation et d'approbation

## Documentation de l'évaluation d'applicabilité

Pour chaque réglementation évaluée (qu'elle soit déterminée applicable ou non), [Organisation] doit créer et maintenir une documentation complète :

### Éléments de documentation requis

**Identification de la réglementation :**

- Nom complet de la réglementation et abréviation courante
- Juridiction (pays, état/province, multijuridictionnel)
- Autorité émettrice (organe législatif, agence réglementaire)
- Date d'entrée en vigueur et éventuelles périodes de transition
- Source où identifiée (base de données, conseil, client, etc.)

**Résumé de l'évaluation :**

- **Évaluation du périmètre géographique :**
  - Réponse à chaque critère G1 à G5 (Oui/Non/Incertain)
  - Score d'applicabilité géographique
  - Justification et preuves à l'appui
- **Évaluation du périmètre opérationnel :**
  - Réponse à chaque critère O1 à O5 (Oui/Non/Incertain)
  - Score d'applicabilité opérationnelle
  - Justification et preuves à l'appui
- **Évaluation du périmètre contractuel :**
  - Réponse à chaque critère C1 à C4 (Oui/Non/Incertain)
  - Score d'applicabilité contractuelle
  - Justification et preuves à l'appui

**Détermination globale :**

- Conclusion d'applicabilité (Applicable / Conditionnellement applicable / Non applicable)
- Attribution de niveau (1, 2, 3 ou N/A)
- Justification détaillée synthétisant l'évaluation tridimensionnelle
- Toute considération spéciale ou cas limite
- Opinions divergentes ou domaines d'incertitude

**Preuves à l'appui :**

- Liens vers ou copies du texte réglementaire
- Avis ou mémorandums juridiques
- Extraits de contrats (si pilotés contractuellement)
- Analyse juridictionnelle
- Précédents de réglementations similaires ou d'organisations comparables

**Métadonnées de l'évaluation :**

- Nom et rôle de l'évaluateur
- Date de l'évaluation
- Nom et rôle du réviseur (si révision par les pairs)
- Approbateur(s) et date(s) d'approbation
- Prochaine date de révision

### Modèles de documentation

Le **Classeur d'évaluation 2 : Matrice d'applicabilité** fournit un modèle standardisé de documentation. Toutes les évaluations doivent être documentées à l'aide de ce modèle pour assurer la cohérence.

Le modèle inclut :

- Formulaire structuré pour l'évaluation tridimensionnelle
- Formules de notation
- Arbre de décision pour l'attribution de niveau
- Blocs de signature d'approbation
- Contrôle de version

### Rétention des preuves

Les preuves à l'appui doivent être jointes ou référencées dans la documentation d'évaluation de l'applicabilité et conservées conformément à la politique de conservation des registres (minimum : durée de l'applicabilité + 7 ans, ou selon les exigences de la réglementation).

## Flux d'approbation

### Étapes d'évaluation et de révision

**Étape 1 : Évaluation initiale**

- Réalisée par : Responsable de la conformité ou personnel juridique/conformité désigné
- Activités : Mener l'évaluation tridimensionnelle, rédiger la détermination
- Résultat : Document d'évaluation d'applicabilité préliminaire
- Délai : Dans les 10 jours ouvrables suivant l'événement déclencheur (ou selon le calendrier IMP-5.31.1)

**Étape 2 : Révision par les pairs** (Recommandée pour tous ; Obligatoire pour Niveau 1)

- Réalisée par : Deuxième professionnel Conformité/Juridique
- Activités : Examiner l'évaluation pour l'exhaustivité, la logique, la qualité des preuves
- Résultat : Commentaires de révision par les pairs, recommandation de procéder ou de réviser
- Délai : Dans les 5 jours ouvrables suivant l'évaluation initiale

**Étape 3 : Révision juridique** (Obligatoire pour Niveau 1 ; Optionnelle pour Niveaux 2/3)

- Réalisée par : Conseil juridique interne (ou conseil externe pour les juridictions sans expertise interne)
- Activités : Valider l'interprétation juridique, confirmer la détermination d'applicabilité
- Résultat : Approbation juridique ou demande de révision, peut inclure un avis juridique
- Délai : Dans les 10 jours ouvrables suivant la révision par les pairs

**Étape 4 : Révision par le Responsable SMSI** (Tous les niveaux)

- Réalisée par : Responsable SMSI
- Activités : Examiner les implications SMSI, considérer l'intégration avec le cadre existant
- Résultat : Approbation du Responsable SMSI ou préoccupations
- Délai : Dans les 5 jours ouvrables suivant la révision juridique (ou Étape 2 si pas de révision juridique)

**Étape 5 : Approbation de la Direction générale** (Obligatoire pour Niveau 1 ; Non requise pour Niveaux 2/3)

- Réalisée par : Direction générale (telle que définie dans les rôles POL-5.31.1)
- Activités : Reconnaître l'obligation de conformité, engager des ressources, approuver l'inclusion au Niveau 1
- Résultat : Signature d'approbation de la Direction générale
- Délai : Dans les 10 jours ouvrables suivant la révision par le Responsable SMSI
- Note : L'approbation de la Direction générale signifie l'engagement organisationnel à se conformer

### Matrice d'autorité d'approbation

| Niveau | Responsable conformité | Conseil juridique | Responsable SMSI | Direction générale |
|--------|------------------------|-------------------|------------------|--------------------|
| **Niveau 1** | Évalue (R) | Révise & Approuve (A) | Révise & Approuve (A) | **Approuve** (A) |
| **Niveau 2** | Évalue (R) | Révise (C) | **Approuve** (A) | Informée (I) |
| **Niveau 3** | Évalue (R) | Optionnel (C) | **Approuve** (A) | Informée (I) |

R=Responsable, A=Redevable/Approuve, C=Consulté, I=Informé

### Processus d'approbation accélérée

Dans les situations urgentes (ex. contrat client en attente d'engagement de conformité, délai réglementaire imminent), un processus d'approbation accéléré peut être utilisé :

- Comprimer les délais à 2 à 3 jours ouvrables par étape
- Étapes de révision simultanées lorsque possible
- Les approbations verbales sont acceptables avec signatures de suivi documentées dans les 5 jours ouvrables
- Escalade vers l'autorité disponible la plus élevée si l'approbateur désigné est indisponible
- **Toutes les approbations accélérées soumises à un audit post-approbation** dans les 30 jours pour valider l'intégrité du processus

Le processus accéléré nécessite l'autorisation du Responsable SMSI et la documentation de la justification de l'urgence.

### Déterminations contestées

Si les évaluateurs, réviseurs ou approbateurs sont en désaccord sur l'applicabilité ou le niveau :

**Résolution interne :**

- Le Responsable de la conformité et le Responsable SMSI discutent, tentent le consensus
- Le Conseil juridique fournit l'interprétation définitive sur les questions juridiques
- Si le consensus ne peut être atteint en interne, escalader à la Direction générale

**Résolution externe :**

- Pour les questions juridiques complexes : Engager un conseil juridique externe pour un avis
- Pour l'interprétation réglementaire : Envisager une demande directe à l'autorité réglementaire (avec les conseils du Conseil juridique)
- Documenter le litige, le processus de résolution et la décision finale avec la justification à l'appui

**Position par défaut :**

- Si le doute persiste après les efforts de résolution : Recourir à « Applicable » et au niveau supérieur (Niveau 1 sur Niveau 2, Niveau 2 sur Niveau 3)
- Justification : L'approche conservatrice réduit le risque de non-conformité
- Réévaluer lorsque des clarifications supplémentaires deviennent disponibles

## Ajout à ISMS-POL-00

Après l'approbation finale de la détermination d'applicabilité :

### Entrée POL-00

Le Responsable SMSI doit ajouter la réglementation à ISMS-POL-00 (Cadre d'applicabilité réglementaire) dans la section de niveau appropriée avec les informations suivantes :

- ID de réglementation (attribué systématiquement, ex. REG-001, REG-002)
- Nom de la réglementation
- Juridiction
- Autorité émettrice
- Date d'entrée en vigueur
- Niveau (1, 2 ou 3)
- Statut d'applicabilité (Applicable, Conditionnellement applicable)
- Brève justification de l'applicabilité (1 à 2 phrases)
- Lien vers la documentation d'évaluation d'applicabilité complète
- Dernière date de révision
- Prochaine date de révision (annuelle pour Niveau 1, bisannuelle pour Niveaux 2/3, ou selon détermination)
- Partie responsable (typiquement Responsable de la conformité)

### Contrôle de version

- Incrémenter le numéro de version de POL-00
- Mettre à jour le tableau d'historique des versions avec la date, l'auteur et le résumé du changement (« Ajout de REG-XXX [Nom de la réglementation] au Niveau [X] »)
- Distribuer le POL-00 mis à jour aux parties prenantes conformément à la liste de distribution

### Communication

Le Responsable de la conformité ou le Responsable SMSI doit notifier les parties prenantes concernées :

**Pour les ajouts de Niveau 1 :**

- Direction générale (notification formelle)
- Tous les Propriétaires de contrôles (sensibilisation générale)
- Unités commerciales concernées (si la réglementation affecte des opérations spécifiques)
- Audit interne (pour la planification des audits)
- Équipes en contact avec les clients (si exigence pilotée par le client)

**Pour les ajouts de Niveaux 2/3 :**

- Responsable SMSI
- Propriétaires de contrôles concernés (notification ciblée)
- Équipe de conformité

**Contenu de la communication :**

- Réglementation ajoutée et niveau
- Implications de haut niveau
- Prochaines étapes (ex. extraction des exigences planifiée)
- Point de contact pour les questions

### Déclenchement des processus en aval

L'ajout d'une réglementation à POL-00 Niveau 1 ou 2 déclenche :

- **Extraction des exigences** (POL-5.31.3, IMP-5.31.2) : Planifier l'extraction des exigences spécifiques de la réglementation
- **Cartographie des contrôles** (POL-5.31.3, IMP-5.31.3) : Suite à l'extraction des exigences, cartographier aux contrôles
- **Analyse des écarts** : Identifier tout écart de conformité
- **Planification des preuves** (POL-5.31.4, IMP-5.31.5) : Déterminer les exigences de preuves

Le Responsable SMSI coordonne ces activités en aval.

---

# Fréquence de révision et déclencheurs de mise à jour

Les déterminations d'applicabilité ne sont pas statiques. [Organisation] doit réviser et, le cas échéant, mettre à jour les évaluations d'applicabilité selon le calendrier et les déclencheurs suivants :

## Calendrier de révision périodique

### Révision complète annuelle (Obligatoire)

**Périmètre** : TOUTES les réglementations dans ISMS-POL-00 (Niveaux 1, 2 et 3)

**Calendrier** : T4 de chaque année civile (ou calendrier alternatif défini dans le cycle de révision de management SMSI)

**Processus** :
1. Le Responsable de la conformité examine chaque réglementation dans POL-00
2. Confirmer que les circonstances de [Organisation] n'ont pas changé affectant l'applicabilité
3. Confirmer que la réglementation elle-même n'a pas été amendée d'une manière affectant l'applicabilité
4. Valider que l'attribution de niveau reste appropriée
5. Documenter la date de révision et le résultat (« Aucun changement », « Niveau modifié », « Supprimé », etc.)
6. Mettre à jour les champs « Dernière date de révision » et « Prochaine date de révision » dans POL-00

**Documentation** : Rapport de résumé de révision annuelle documentant le périmètre, les résultats et tout changement

**Approbation** : Approbation du Responsable SMSI du résumé de révision annuelle

### Fréquence de révision spécifique au niveau

**Réglementations de Niveau 1** :

- Minimum : Révision annuelle (per 6.1.1)
- Recommandé : Révision semestrielle pour les réglementations évoluant rapidement
- Obligatoire : La révision pilotée par les événements (Section 6.2) prend le dessus sur les révisions planifiées

**Réglementations de Niveau 2** :

- Minimum : Révision annuelle (per 6.1.1)
- Alternative : Révision bisannuelle acceptable pour les cadres stables avec faible probabilité de changement

**Réglementations de Niveau 3** :

- Minimum : Révision bisannuelle
- Peut réviser « selon les besoins » en fonction de l'utilisation du cadre comme référence par [Organisation]

## Déclencheurs de révision pilotée par les événements

L'évaluation de l'applicabilité doit être revisitée (en dehors des révisions planifiées) lorsque déclenchée par :

### Changements organisationnels

**Expansion ou contraction géographique :**

- [Organisation] entre dans une nouvelle juridiction → Réviser les réglementations dans cette juridiction
- [Organisation] quitte une juridiction → Réviser les réglementations dépendant de la présence là-bas
- Déclencheur : Dans les 30 jours suivant la décision ou l'événement d'expansion/contraction

**Changements opérationnels :**

- Nouvelles offres de services → Réviser les réglementations couvrant ces services
- Entrée dans un nouveau marché vertical → Réviser les réglementations sectorielles spécifiques
- Nouveaux types de données traités → Réviser les réglementations spécifiques aux données
- Abandon de services → Réviser si les réglementations restent applicables
- Déclencheur : Pendant la phase de planification (avant le lancement) et dans les 30 jours suivant le changement opérationnel

**Restructuration organisationnelle :**

- Fusion ou acquisition → Révision complète des obligations de l'entité combinée
- Cession → Réviser si les obligations subsistent après la cession
- Changement de société mère → Réviser si de nouvelles obligations se répercutent
- Déclencheur : Dans le cadre de la diligence raisonnable de fusion/acquisition ; dans les 60 jours suivant la clôture de la transaction

**Changements de seuils :**

- [Organisation] franchit un seuil réglementaire (ex. nombre d'employés, revenus, volume de données)
- Déclencheur : Surveillance continue ; révision formelle lorsque le seuil est franchi

### Changements réglementaires

**Réglementation amendée :**

- Les amendements peuvent changer le périmètre, les critères d'applicabilité ou les exigences
- Déclencheur : Le processus de surveillance des changements réglementaires (POL-5.31.4, IMP-5.31.4) détecte l'amendement
- Action : L'évaluation d'impact inclut une réévaluation de l'applicabilité si le périmètre a changé

**Nouvelle réglementation adoptée :**

- Déjà couverte par le processus d'identification (Section 2)
- Déclencheur : Sources multiples (per Section 2.2)

**Réglementation abrogée ou remplacée :**

- La réglementation dans POL-00 est abrogée, annulée ou remplacée par une réglementation plus récente
- Déclencheur : Surveillance des changements réglementaires
- Action : Marquer comme « Remplacée » dans POL-00, mener une évaluation d'applicabilité pour la réglementation de remplacement

**Orientation ou interprétation réglementaire publiée :**

- L'autorité réglementaire publie des orientations clarifiant le périmètre ou l'applicabilité
- Une décision de justice interprète la réglementation d'une manière affectant l'applicabilité
- Déclencheur : Surveillance réglementaire ou alerte du Conseil juridique
- Action : Réviser la détermination d'applicabilité à la lumière de la nouvelle interprétation

### Changements contractuels

**Nouveau contrat client :**

- Le contrat inclut des exigences de conformité → Évaluation d'applicabilité pour ces exigences
- Déclencheur : Signature du contrat ou lors de la diligence raisonnable pré-contrat
- Action : Évaluer les réglementations exigées contractuellement (peut être Niveau 1 si opposable)

**Renouvellement ou amendement de contrat :**

- Le client ajoute des exigences de conformité lors du renouvellement
- Les obligations de conformité sont modifiées
- Déclencheur : Processus de renouvellement du contrat
- Action : Réviser l'applicabilité sur la base des termes contractuels mis à jour

**Expiration du contrat :**

- Un contrat client majeur expire sans renouvellement
- Le contrat était le seul facteur de l'applicabilité (Critère C1)
- Déclencheur : Date d'expiration du contrat
- Action : Évaluer si la réglementation reste applicable sans le contrat (peut passer du Niveau 1 au Niveau 2 ou être supprimée)

**Nouvel accord fournisseur :**

- L'accord crée des obligations répercutées
- Déclencheur : Signature du contrat fournisseur
- Action : Évaluation de l'applicabilité pour les exigences répercutées

### Changements de certification

**Nouvelle certification poursuivie :**

- [Organisation] décide de poursuivre une nouvelle certification (ex. SOC 2, PCI DSS v4.0.1)
- Déclencheur : Décision de certification
- Action : Réviser les exigences de certification pour les réglementations applicables

**Norme de certification mise à jour :**

- La norme révisée avec de nouvelles références réglementaires
- Déclencheur : Notification de l'organisme de certification ou publication de l'organisme de normalisation
- Action : Réviser la norme mise à jour pour la nouvelle applicabilité

## Escalade pour les litiges d'applicabilité

Si la détermination d'applicabilité est contestée (désaccord interne ou défi externe) :

### Litiges internes

**Scénarios typiques :**

- Une unité commerciale affirme que la réglementation ne s'applique pas ; la Conformité affirme qu'elle s'applique
- Un propriétaire de contrôle conteste l'attribution de niveau (ex. demande Niveau 2 plutôt que Niveau 1 en raison de la charge de mise en œuvre)
- Le Juridique et la Conformité sont en désaccord sur l'interprétation

**Processus de résolution :**
1. **Discussion** : Les parties en litige se réunissent pour comprendre les positions et les preuves
2. **Décision du Responsable de la conformité** : Si le litige est au niveau opérationnel, le Responsable de la conformité prend la décision
3. **Révision du Conseil juridique** : Pour les litiges d'interprétation juridique, le Conseil juridique a le dernier mot sur les questions juridiques
4. **Escalade à la Direction générale** : Pour les litiges impliquant des engagements de ressources ou l'acceptation de risques, escalader à la Direction générale
5. **Conseil externe** : Pour les questions juridiques complexes, engager un conseil externe pour un avis indépendant

**Documentation** : Le litige doit être documenté incluant les positions, les preuves, le processus de résolution et la décision finale avec justification

**Délai** : Les litiges doivent être résolus dans les 30 jours suivant l'identification ; la position intermédiaire « Applicable » est maintenue jusqu'à résolution

### Défis externes

**Scénarios :**

- Une autorité réglementaire affirme que la réglementation s'applique ; [Organisation] estime qu'elle ne s'applique pas
- Un client conteste la position de [Organisation] sur l'applicabilité
- Un auditeur remet en question la détermination d'applicabilité

**Réponse :**
1. **Rassembler les preuves** : Compiler la documentation d'évaluation de l'applicabilité et les preuves à l'appui
2. **Révision du Conseil juridique** : Engager le Conseil juridique pour examiner la position et l'assertion externe
3. **Avis juridique externe** : Envisager d'obtenir un avis juridique indépendant
4. **Demande réglementaire directe** : Avec les conseils du Conseil juridique, envisager une demande directe à l'autorité réglementaire
5. **Résoudre** : Sur la base de l'analyse et des conseils juridiques, confirmer ou réviser la détermination
6. **Documenter** : Documenter soigneusement le défi externe et la résolution

**Position intermédiaire** : Pendant la résolution du litige, sauf si le Conseil juridique conseille autrement, maintenir la détermination originale ou adopter la position plus conservatrice (traiter comme applicable) pour réduire le risque de conformité.

## Documentation des révisions

Toutes les révisions (périodiques et pilotées par les événements) doivent être documentées :

**Registre de révision :**

- Réglementation examinée
- Type de révision (Annuelle, Pilotée par les événements, Résolution de litige)
- Date de révision
- Nom du réviseur
- Résultat (Aucun changement, Niveau modifié, Supprimé de POL-00, Ajouté à POL-00)
- Justification du résultat (si modifié)
- Approbateur et date (si la détermination a changé)

**Journal de révision** : Maintenir un journal de révision centralisé enregistrant toutes les révisions. Soutient la démonstration d'une gestion diligente et continue du paysage réglementaire.

---

# Contrôle documentaire et documents connexes

## Informations sur le document

| Attribut | Valeur |
|----------|--------|
| **Identifiant du document** | ISMS-POL-A.5.31.2 |
| **Titre du document** | Exigences légales, statutaires, réglementaires et contractuelles : Méthodologie d'applicabilité réglementaire |
| **Version** | 1.0 |
| **Statut** | Brouillon |
| **Classification** | Usage interne |
| **Propriétaire** | Responsable de la conformité |
| **Auteur** | [Nom] |
| **Date d'entrée en vigueur** | [À déterminer lors de l'approbation] |
| **Fréquence de révision** | Annuellement, ou lors d'un changement significatif de la méthodologie ou du cadre d'applicabilité |
| **Prochaine date de révision** | [12 mois à partir de la date d'entrée en vigueur] |

## Approbation

Cette politique nécessite l'approbation des rôles suivants :

| Rôle | Nom | Signature | Date |
|------|-----|-----------|------|
| **Responsable de la conformité** | [Nom] | ___________________ | __________ |
| **Conseil juridique** | [Nom] | ___________________ | __________ |
| **Responsable SMSI** | [Nom] | ___________________ | __________ |
| **Direction générale** | [Nom] | ___________________ | __________ |

## Historique des versions

| Version | Date | Auteur | Modifications |
|---------|------|--------|---------------|
| 0.1 | [Date] | [Nom] | Brouillon initial pour révision |
| 1.0 | [Date] | [Nom] | Version approuvée initiale |

## Documents connexes

**Documents prérequis :**

- **ISMS-POL-A.5.31.1** : Résumé exécutif et alignement des contrôles (base du cadre)

**Documents de coordination :**

- **ISMS-POL-00** : Cadre d'applicabilité réglementaire (registre réglementaire maintenu à l'aide de cette méthodologie)

**Documents en aval :**

- **ISMS-POL-A.5.31.3** : Cadre d'extraction des exigences et de cartographie des contrôles (phase suivante après détermination de l'applicabilité)
- **ISMS-POL-A.5.31.4** : Cadre de gestion des changements et des preuves (gestion continue incluant la surveillance des changements réglementaires)

**Guides de mise en œuvre :**

- **ISMS-IMP-A.5.31.2-UG/TG** : Processus d'évaluation de l'applicabilité réglementaire (procédures étape par étape pour exécuter cette méthodologie)

**Outils d'évaluation :**

- **Classeur d'évaluation 1** : Inventaire réglementaire (liste complète des réglementations)
- **Classeur d'évaluation 2** : Matrice d'applicabilité (modèle d'évaluation structuré)

**Normes :**

- ISO/IEC 27001:2022 — Systèmes de management de la sécurité de l'information — Exigences (Contrôle A.5.31)
- ISO/IEC 27002:2022 — Mesures de sécurité de l'information (Section 5.31)

## Distribution et accès

**Liste de distribution :**

- Direction générale
- Responsable de la conformité / Fonction juridique
- Responsable SMSI
- Développement commercial (pour les nouveaux contrats/clients)
- Direction des opérations (pour les changements opérationnels déclenchant des révisions)
- Équipe d'audit interne

**Niveau d'accès** : Usage interne

**Emplacement du document** : Système de gestion documentaire de [Organisation] : [Chemin/URL]

---

# Définitions

**Applicabilité** : Détermination qu'une réglementation s'applique à [Organisation] sur la base de critères géographiques, opérationnels ou contractuels.

**Obligation contractuelle** : Exigence imposée par contrat (client, fournisseur, partenaire) créant une obligation de conformité opposable.

**Périmètre géographique** : Applicabilité basée sur l'endroit où [Organisation] opère, où se trouvent les clients, ou les dispositions extraterritoriales.

**Obligation légale** : Exigence imposée par statut, loi ou réglementation qui est légalement contraignante et opposable.

**Périmètre opérationnel** : Applicabilité basée sur les services que [Organisation] fournit, les données qu'elle traite ou les opérations qu'elle mène.

**Réglementation** : Terme général englobant les lois, statuts, réglementations, directives, exigences contractuelles et normes (exigences réglementaires).

**Cadre à trois niveaux** : Système de catégorisation classifiant les réglementations comme Niveau 1 (Obligatoire), Niveau 2 (Conditionnel) ou Niveau 3 (Informationnel).

**Événement déclencheur** : Circonstance initiant l'identification réglementaire ou la réévaluation de l'applicabilité.

---

**FIN DU DOCUMENT**

---

*Cette politique établit la méthodologie systématique de [Organisation] pour la détermination de l'applicabilité réglementaire, alimentant ISMS-POL-00 et permettant l'extraction des exigences et la cartographie des contrôles en aval.*

<!-- QA_VERIFIED: 2026-03-30 -->
