<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.9-FR:framework:POL:a.5.9 -->
**ISMS-POL-A.5.9 — Inventaire des informations et des actifs**

---

**Contrôle documentaire**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Inventaire des informations et des actifs |
| **Type de document** | Politique |
| **Identifiant du document** | ISMS-POL-A.5.9 |
| **Créateur du document** | Responsable de la sécurité des systèmes d'information (RSSI) |
| **Propriétaire du document** | Directeur général (DG) |
| **Approuvé par** | Direction générale |
| **Date de création** | [Date] |
| **Version** | 1.0 |
| **Date de version** | [Date à définir] |
| **Classification** | Interne |
| **Statut** | Brouillon |

**Historique des versions** :

| Version | Date | Auteur | Modifications |
|---------|------|--------|---------------|
| 1.0 | [Date] | RSSI | Politique initiale suivie dans les tableaux de bord de synthèse pour la première certification ISO 27001:2022 |

**Cycle de révision** : Annuel
**Prochaine date de révision** : [Date d'entrée en vigueur + 12 mois]

**Chaîne d'approbation** :

- Primaire : Responsable de la sécurité des systèmes d'information (RSSI)
- Secondaire : Directeur des systèmes d'information (DSI)
- Conformité : Responsable juridique/conformité
- Autorité finale : Direction générale

**Documents connexes** :

- ISMS-POL-00 (Cadre d'applicabilité réglementaire)
- ISMS-POL-A.5.10 à A.5.18 (Contrôles de gestion des actifs)
- ISMS-POL-A.8.x (Contrôles techniques)
- ISMS-IMP-A.5.9.1-UG/TG (Identification et découverte des actifs)
- ISMS-IMP-A.5.9.2-UG/TG (Structure et maintenance de l'inventaire)
- ISMS-IMP-A.5.9.3-UG/TG (Spécifications d'évaluation)
- ISMS-IMP-A.5.9.4-UG/TG (Évaluation de la responsabilité des propriétaires)
- ISO/IEC 27001:2022 Contrôle A.5.9

---

## Résumé exécutif

La présente politique établit les exigences de [Organisation] pour la tenue d'un inventaire des informations et des actifs associés, conformément au contrôle A.5.9 de l'ISO/IEC 27001:2022.

**Le principe fondamental** : On ne peut pas protéger ce que l'on ne sait pas qu'on possède. L'inventaire des actifs est le fondement sur lequel reposent tous les autres contrôles de sécurité — évaluation des risques, contrôle d'accès, classification, gestion des vulnérabilités, réponse aux incidents et planification de la continuité des activités.

**Périmètre** : Cette politique s'applique à tous les actifs informationnels (données, contenus, propriété intellectuelle) et aux actifs associés (infrastructure informatique, applications, installations physiques, compétences du personnel) relevant du périmètre de management de la sécurité de l'information de [Organisation]. La politique établit CE QUI doit être inventorié, QUI en est responsable et COMMENT la conformité est vérifiée.

**Objet** : Définir les exigences organisationnelles pour la création, la maintenance et la gouvernance de l'inventaire des actifs. Cette politique établit le cadre de gouvernance (CE QUOI et POURQUOI). Les procédures de mise en œuvre (COMMENT) sont documentées séparément dans la suite ISMS-IMP-A.5.9 (variantes UG/TG).

**Alignement réglementaire** : Cette politique répond aux exigences de conformité obligatoires définies dans ISMS-POL-00 (Cadre d'applicabilité réglementaire), notamment le nLPD suisse, le RGPD de l'UE et l'ISO/IEC 27001:2022. Des exigences sectorielles conditionnelles (PCI DSS v4.0.1, FINMA, DORA, NIS2, HIPAA) s'appliquent lorsque les activités de [Organisation] déclenchent leur applicabilité.

---

# Alignement des contrôles et périmètre

## Contrôle ISO/IEC 27001:2022 A.5.9

**Annexe A.5.9 de l'ISO/IEC 27001:2022 — Inventaire des informations et autres actifs associés**

> *Un inventaire des informations et des autres actifs associés, incluant les propriétaires, devrait être créé et maintenu.*

**Objectif du contrôle (ISO/IEC 27002:2022)** : Identifier les informations et autres actifs associés de l'organisation afin de maintenir leur sécurité de l'information et d'attribuer les responsabilités appropriées.

**Type de contrôle** : Organisationnel
**Propriétés de sécurité de l'information** : Confidentialité, Intégrité, Disponibilité
**Concepts de cybersécurité** : Identifier
**Capacités opérationnelles** : Gestion des actifs
**Domaines de sécurité** : Gouvernance et écosystème

**Cette politique porte sur** :

- Exigences d'identification et de classification des actifs informationnels
- Exigences d'inventaire des actifs associés (informatiques, physiques, personnel)
- Cadre d'attribution et de responsabilité des propriétaires d'actifs
- Normes d'exactitude, de complétude et d'actualité de l'inventaire
- Rôles et responsabilités organisationnels pour la gestion des actifs
- Intégration avec d'autres contrôles du SMSI et systèmes organisationnels
- Méthodologie d'évaluation et vérification de la conformité

## Ce que fait cette politique

Cette politique :

- **Définit** ce qui constitue un actif informationnel et un actif associé nécessitant un inventaire
- **Établit** les attributs obligatoires pour les enregistrements d'inventaire (propriétaire, classification, localisation, etc.)
- **Précise** les exigences d'attribution de propriété et la responsabilité des propriétaires
- **Fixe** des normes d'exactitude, de complétude et d'actualité pour la maintenance de l'inventaire
- **Identifie** les rôles et responsabilités organisationnels pour l'inventaire des actifs
- **Référence** les exigences réglementaires applicables conformément à ISMS-POL-00

## Ce que cette politique ne fait PAS

Cette politique NE :

- **Précise pas les détails techniques de mise en œuvre** (voir les guides de mise en œuvre ISMS-IMP-A.5.9)
- **Définit pas la sélection des outils d'inventaire** (décisions technologiques fondées sur les besoins de [Organisation])
- **Fournit pas de procédures de découverte détaillées** (voir ISMS-IMP-A.5.9-1 Identification des actifs)
- **Décrit pas les flux de travail de maintenance** (voir ISMS-IMP-A.5.9-2 Maintenance de l'inventaire)
- **Se substitue pas à l'évaluation des risques** (l'inventaire fournit des données d'entrée au processus d'évaluation)

**Justification** : La séparation des exigences politiques et du guide de mise en œuvre permet :

- La stabilité de la politique malgré les changements organisationnels
- L'agilité technique pour les mises à jour d'outils et de processus sans révision de la politique
- Une distinction claire entre la gouvernance (politique) et l'exécution (mise en œuvre)
- L'adaptabilité à différents contextes organisationnels et profils de risque

## Périmètre

**Cette politique s'applique à** :

- Tous les actifs informationnels dans le périmètre du SMSI de [Organisation] (bases de données, documents, enregistrements, PI, données de configuration)
- Toute l'infrastructure informatique supportant le traitement de l'information (serveurs, stockage, réseau, postes de travail)
- Toutes les applications et logiciels (applications métier, services SaaS, outils de développement)
- Tous les actifs physiques supportant la sécurité de l'information (installations, supports, équipements)
- Tous les actifs de personnel critiques aux opérations (rôles clés, compétences spécialisées)
- Tous les services tiers traitant les informations de [Organisation]

**Catégories d'actifs dans le périmètre** :

1. **Actifs informationnels** : Toutes données, contenus ou connaissances ayant de la valeur pour [Organisation]

   - Données structurées (bases de données, entrepôts de données)
   - Documents non structurés (fichiers, courriels, rapports)
   - Enregistrements et archives (conservation réglementaire)
   - Propriété intellectuelle (secrets commerciaux, brevets, conceptions)
   - Configuration et paramètres (configurations système)
   - Matériaux d'authentification et cryptographiques (clés, certificats, identifiants)

2. **Actifs associés — Infrastructure informatique** : Systèmes traitant, stockant ou transmettant des informations

   - Serveurs physiques et machines virtuelles
   - Systèmes de stockage et infrastructures de sauvegarde
   - Infrastructure réseau (routeurs, commutateurs, pare-feu, équilibreurs de charge)
   - Postes de travail (stations de travail, ordinateurs portables, appareils mobiles)
   - Infrastructures et services cloud

3. **Actifs associés — Applications** : Logiciels traitant des informations

   - Applications métier (ERP, CRM, systèmes financiers)
   - Services SaaS et cloud
   - Applications développées en interne
   - Outils de développement et pipelines CI/CD
   - API et plateformes d'intégration

4. **Actifs associés — Physiques** : Ressources tangibles supportant les opérations

   - Installations et datacentres
   - Supports amovibles (clés USB, bandes de sauvegarde, disques portables)
   - Équipements de sécurité physique (contrôle d'accès, surveillance)
   - Documents papier et imprimés

5. **Actifs associés — Personnel** : Ressources humaines et compétences

   - Rôles de personnel clés (critiques aux opérations)
   - Compétences spécialisées (compétences uniques, certifications)
   - PAS les dossiers individuels (conformité à la vie privée)

**Hors périmètre** :

- Les actifs appartenant à des tiers (sauf s'ils traitent les informations de [Organisation])
- Les appareils personnels non utilisés pour le travail de [Organisation] (sauf si la politique BYOD s'applique)
- Les informations publiques sans exigences de confidentialité, d'intégrité ou de disponibilité
- Les fournitures de bureau courantes sans impact sur la sécurité

## Applicabilité réglementaire

Les exigences réglementaires sont catégorisées conformément à **ISMS-POL-00 (Cadre d'applicabilité réglementaire)**.

**Niveau 1 : Conformité obligatoire** (s'applique à toutes les opérations de [Organisation]) :

- **nLPD suisse (art. 8)** : La sécurité des données personnelles exige de savoir quelles données existent et où
- **RGPD UE (art. 5, 32)** : La protection des données dès la conception exige un inventaire documenté
- **ISO/IEC 27001:2022 (Contrôle A.5.9)** : Exigence de contrôle explicite pour la certification

**Niveau 2 : Applicabilité conditionnelle** (déclenchée par des activités métier spécifiques) :

- **PCI DSS v4.0.1 (Req. 2.4, 12.5)** : Inventaire des composants système dans l'environnement des données de titulaires de cartes
- **HIPAA (164.310(d)(1))** : Inventaire et contrôles des actifs pour les systèmes d'information de santé
- **FINMA** : Exigences d'inventaire des actifs fondées sur les risques pour les institutions financières suisses
- **DORA/NIS2** : Inventaire des actifs TIC pour les infrastructures critiques et entités financières
- **SOX** : Les contrôles généraux informatiques exigent un inventaire documenté des systèmes pour le reporting financier
- **Réglementations sectorielles** : Peuvent exiger une catégorisation spécialisée des actifs

**Niveau 3 : Référence informative** (bonnes pratiques, non juridiquement contraignantes) :

- **ISO/IEC 19770-1** : Exigences des systèmes de gestion des actifs informatiques
- **ISO 55001** : Gestion des actifs — Exigences des systèmes de management
- **NIST SP 800-53 (CM-8, PM-5)** : Contrôles d'inventaire des composants système
- **CIS Controls (1, 2)** : Inventaire et contrôle des actifs d'entreprise et des logiciels
- **COBIT 2019 (BAI09)** : Cadre de gestion des actifs

**Exigences fédérales américaines** : Les références aux cadres fédéraux américains (FISMA, FIPS, FedRAMP, exigences cybersécurité NIST) s'appliquent uniquement lorsque [Organisation] a des obligations contractuelles fédérales américaines explicites, telles que définies dans ISMS-POL-00.

---

# Cadre des exigences

## Création de l'inventaire des actifs

**Exigence A.5.9-R1** : [Organisation] DOIT tenir un inventaire des informations et des actifs associés.

**Couverture obligatoire** :

- Tous les actifs informationnels dans le périmètre du SMSI (bases de données, documents, PI, configurations)
- Toute l'infrastructure informatique traitant des informations (serveurs, stockage, réseau, postes)
- Toutes les applications et services (applications métier, SaaS, API, outils de développement)
- Tous les actifs physiques supportant la sécurité (installations, supports, équipements)
- Tous les actifs de personnel critiques aux opérations (rôles clés, compétences)

**Approche de mise en œuvre** : [Organisation] détermine la structure d'inventaire appropriée fondée sur l'évaluation des risques. L'inventaire peut consister en plusieurs inventaires spécialisés (CMDB pour l'informatique, SIRH pour le personnel, référentiels documentaires) à condition qu'ils satisfassent collectivement aux exigences du contrôle.

**Méthode de vérification** : Évaluation de la complétude conformément à ISMS-IMP-A.5.9-3 (Évaluation de la qualité et de la conformité).

## Catégorisation des actifs

**Exigence A.5.9-R2** : [Organisation] DOIT catégoriser les actifs pour permettre l'application appropriée des contrôles de sécurité.

**Dimensions de catégorisation** :

1. **Par type d'actif** (catégorisation primaire) :

   - Actifs informationnels (ce qui nécessite protection)
   - Infrastructure informatique (systèmes traitant les informations)
   - Applications (logiciels traitant les informations)
   - Actifs physiques (ressources tangibles)
   - Actifs de personnel (compétences et rôles)

2. **Par criticité** (pour un traitement fondé sur les risques) :

   - Critique : La perte entraînerait un impact grave sur l'activité (perturbation opérationnelle, violation réglementaire)
   - Élevé : La perte entraînerait un impact significatif sur l'activité (pertes financières, atteinte à la réputation)
   - Moyen : La perte entraînerait un impact modéré (réduction de l'efficacité, inconvénient client)
   - Faible : La perte entraînerait un impact minimal (inconvénient mineur, facilement remplaçable)

3. **Par état du cycle de vie** (pour la planification de la maintenance) :

   - Actif : En production
   - En développement : En cours de développement ou de test
   - En maintenance : Prévu pour des mises à jour ou des correctifs
   - Retraité : Prévu pour mise hors service
   - Archivé : Conservé pour conformité mais non activement utilisé

**Aide à la décision** : L'annexe A fournit le cadre de décision pour la catégorisation et des exemples.

**Méthode de vérification** : Attribution des catégories révisée lors du processus d'accusé de réception des propriétaires conformément à ISMS-IMP-A.5.9-4 (Évaluation de la responsabilité des propriétaires).

## Attributs obligatoires de l'inventaire

**Exigence A.5.9-R3** : [Organisation] DOIT documenter les attributs obligatoires pour chaque actif inventorié.

**Attributs de base** (requis pour tous les actifs) :

| Attribut | Description | Objet | Vérification |
|----------|-------------|-------|--------------|
| **Identifiant de l'actif** | Identifiant unique | Traçabilité entre systèmes | Automatique (généré par le système) |
| **Nom de l'actif** | Nom lisible | Communication et reporting | Vérification par le propriétaire |
| **Type d'actif** | Catégorie conformément à 2.2 | Applicabilité du contrôle | Validation de la catégorie |
| **Propriétaire** | Individu responsable (pour les actifs informationnels, il s'agit du « Propriétaire des données » au sens RGPD — la partie métier responsable) | Attribution des responsabilités | Accusé de réception du propriétaire |
| **Gardien** | Gestionnaire au quotidien (peut différer du propriétaire) — partie technique gérant l'infrastructure/les systèmes | Responsabilité opérationnelle | Accusé de réception du gardien |
| **Description** | Objet et fonction | Compréhension et contexte | Vérification par le propriétaire |
| **Localisation** | Emplacement physique ou logique | Suivi des actifs, résidence des données | Vérification physique |
| **Statut** | État du cycle de vie conformément à 2.2 | Planification de la maintenance | Flux de travail du statut |
| **Criticité** | Impact métier conformément à 2.2 | Priorisation des risques | Alignement avec l'évaluation des risques |
| **Date de création** | Date d'acquisition/création | Suivi de l'ancienneté | Vérification documentaire |
| **Dernière mise à jour** | Dernière modification de l'enregistrement | Suivi de l'actualité | Horodatage automatique |
| **Dernière révision** | Dernière révision par le propriétaire | Assurance d'exactitude | Attestation du propriétaire |
| **Prochaine date de révision** | Révision planifiée | Maintenance proactive | Calendrier de révision |

**Attributs spécifiques aux actifs informationnels** :

| Attribut | Description | Objet |
|----------|-------------|-------|
| **Classification des données** | Niveau de confidentialité/intégrité/disponibilité conformément à A.5.12 | Sélection des contrôles |
| **Format des données** | Format de fichier, schéma, structure | Compatibilité technique |
| **Emplacement(s) de stockage** | Où les données résident physiquement | Conformité à la résidence des données |
| **Durée de conservation** | Exigence de conservation légale/métier | Conformité, planification du stockage |
| **Exigences légales/réglementaires** | Réglementations applicables | Suivi de la conformité |
| **Systèmes connexes** | Systèmes accédant à ces informations | Analyse des dépendances |
| **Statut de chiffrement** | Au repos, en transit, ou les deux | Vérification de la protection cryptographique |

**Attributs spécifiques à l'infrastructure informatique** :

| Attribut | Description | Objet |
|----------|-------------|-------|
| **Fabricant/Fournisseur** | Producteur de l'actif | Contrats de support, compatibilité |
| **Modèle/Version** | Version spécifique du produit | Gestion des correctifs, suivi de fin de vie |
| **Numéro de série/Étiquette d'actif** | Identifiant physique | Vérification physique de l'actif |
| **Adresse IP/Nom d'hôte** | Identifiant réseau | Gestion réseau |
| **Référence de configuration** | Référence de configuration standard | Gestion de la configuration (A.8.9) |
| **Dépendances** | Actifs requis pour le fonctionnement | Évaluation d'impact |
| **Informations supportées** | Actifs informationnels traités | Héritage de classification |

**Attributs optionnels** : [Organisation] peut étendre l'inventaire avec des attributs supplémentaires selon les besoins opérationnels (coût d'achat, dates de garantie, consommation énergétique, certifications de conformité) à condition qu'ils ne créent pas une charge de maintenance excessive.

**Méthode de vérification** : Complétude des attributs vérifiée conformément à ISMS-IMP-A.5.9-3 (Évaluation de la qualité et de la conformité).

## Propriété des actifs

**Exigence A.5.9-R4** : [Organisation] DOIT attribuer un propriétaire à chaque actif inventorié.

**Principes de propriété** :

- **Attribution universelle** : Chaque actif DOIT avoir un propriétaire attribué (aucune exception)
- **Responsabilité** : Le propriétaire est responsable de l'actif tout au long de son cycle de vie
- **Délégation autorisée** : Le propriétaire peut déléguer les responsabilités de gardien mais conserve sa responsabilité
- **Accusé de réception requis** : Les propriétaires doivent accuser réception de la propriété et des responsabilités
- **Gestion des changements** : Les changements de propriété déclenchent une mise à jour de l'inventaire

**Responsabilités du propriétaire** :

- Classifier l'actif selon sa valeur métier et son risque
- S'assurer que les contrôles de sécurité appropriés sont appliqués
- Réviser l'exactitude de l'enregistrement d'inventaire au moins annuellement
- Approuver les demandes d'accès aux actifs dont il est propriétaire
- Signaler les incidents de sécurité affectant les actifs dont il est propriétaire
- Participer aux décisions du cycle de vie des actifs (mise hors service, archivage)
- Maintenir la connaissance des exigences réglementaires affectant les actifs dont il est propriétaire

**Lorsque la propriété est incertaine** :

1. Escalader au niveau de gestion approprié dans les 5 jours ouvrables suivant la découverte de l'actif
2. Documenter l'attribution d'un gardien temporaire (responsabilité opérationnelle pendant la période de détermination)
3. Fixer une échéance pour la détermination du propriétaire permanent :
   - **Échéance initiale** : 30 jours calendaires
   - **Prolongation autorisée** : Jusqu'à 90 jours calendaires avec approbation du RSSI si la propriété nécessite une résolution interfonctionnelle (documenter la justification et les contrôles compensatoires : le gardien attribué surveille l'actif, les incidents de sécurité sont immédiatement escaladés)
4. Les actifs sans propriétaire au-delà de 90 jours nécessitent une approbation de la direction générale en tant que dérogation formelle (Section 3.4)

Les escalades d'actifs sans propriétaire sont suivies dans le registre des dérogations. Objectif : ≥ 95 % des actifs avec propriétaires permanents attribués dans les 30 jours, 100 % dans les 90 jours.

**Méthode de vérification** : Complétude de l'attribution des propriétaires (objectif 100 %) vérifiée conformément à ISMS-IMP-A.5.9-4 (Évaluation de la responsabilité des propriétaires).

## Normes de qualité de l'inventaire

**Exigence A.5.9-R5** : [Organisation] DOIT maintenir la qualité de l'inventaire par des normes d'exactitude, de complétude et d'actualité.

### Complétude

**Norme** : L'inventaire doit inclure tous les actifs dans le périmètre.

**Approche de vérification** :

- Analyses de découverte périodiques et réconciliation
- Validation croisée avec d'autres systèmes (CMDB, achats, RH)
- Tests par échantillonnage pour les actifs manquants
- Attestation de gestion

**Granularité acceptable** : Déterminée par la criticité et le risque de l'actif. Les actifs à haute valeur/haut risque nécessitent des enregistrements individuels détaillés. Les actifs courants à faible risque peuvent être regroupés (p. ex. « ordinateurs portables standard des employés — quantité 50 » contre des numéros de série individuels).

**Objectif initial de certification** : 85 % de complétude pour les actifs critiques, 80 % pour les actifs standards, évalué dans les 90 jours suivant l'approbation de la politique via l'évaluation de l'inventaire de référence (ISMS-IMP-A.5.9-1).

**Objectif à maturité** (atteint dans les 12 mois après la certification) : 95 % de complétude pour les actifs critiques, 90 % pour les actifs standards. Progression intermédiaire suivie trimestriellement via le tableau de bord de synthèse.

### Exactitude

**Norme** : Les données d'inventaire doivent refléter correctement l'état réel des actifs.

**Approche de vérification** :

- Révisions régulières par les propriétaires d'actifs (au moins annuellement)
- Échantillonnage statistique pour la validation de l'exactitude des données
- Validation automatisée là où techniquement réalisable
- Vérification déclenchée par incident (l'inventaire est vérifié lors d'incidents)

**Objectifs d'exactitude initiaux** (référence + 90 jours) :

- Actifs informationnels : 85 %
- Infrastructure informatique : 90 %
- Actifs physiques : 80 %
- Actifs de personnel : 95 %

**Objectifs d'exactitude à maturité** (dans les 12 mois après la certification) :

- Actifs informationnels : 95 %
- Infrastructure informatique : 98 %
- Actifs physiques : 90 %
- Actifs de personnel : 100 %

Amélioration de l'exactitude suivie trimestriellement. Méthodologie d'échantillonnage définie dans ISMS-IMP-A.5.9-3.

### Actualité

**Norme** : L'inventaire doit refléter l'état actuel, non l'état historique.

**Déclencheurs de mise à jour** :

- Création d'actif (nouvelle acquisition, développement)
- Modification d'actif (changement de configuration, déplacement)
- Cession d'actif (mise hors service, suppression)
- Changement de propriétaire
- Changement de classification
- Révision périodique planifiée

**Ancienneté maximale** (délais de mise à jour après un événement de changement) :

- Actifs critiques : Mises à jour en temps réel ou quotidiennes
- Actifs à haut risque : Mises à jour dans les 3 jours ouvrables
- Actifs standards : Mises à jour dans la semaine
- Actifs à faible risque : Mises à jour dans le mois
- Tous les actifs : Révisés annuellement au minimum

**Précision** : L'ancienneté maximale se réfère aux **déclencheurs de mise à jour** (délai de mise à jour après un événement de changement). Le calendrier de vérification ci-dessous se réfère à la **révision proactive par le propriétaire** (attestation périodique). Les actifs critiques nécessitent des mises à jour rapides lors de changements (quotidiennement) ET une révision planifiée par le propriétaire pour détecter les écarts non remarqués.

**Exigence d'intégration** : L'inventaire des actifs DOIT s'intégrer aux processus de gestion des changements (les changements déclenchent des mises à jour d'inventaire automatiquement là où techniquement réalisable).

### Calendrier de vérification

| Catégorie d'actifs | Fréquence de révision | Rôle responsable | Méthode de vérification |
|--------------------|-----------------------|------------------|-------------------------|
| Information critique | Trimestrielle | Propriétaire de l'information | Attestation du propriétaire + échantillonnage |
| Infrastructure informatique à haut risque | Trimestrielle | Propriétaire du système | Analyse automatisée + vérification manuelle |
| Actifs standards | Semestrielle | Propriétaire de l'actif | Révision propriétaire + contrôles ponctuels |
| Actifs à faible risque | Annuelle | Propriétaire de l'actif | Attestation du propriétaire |
| Tous les actifs de personnel | Trimestrielle | RH + responsables de département | Réconciliation avec le système RH |

**Méthode de vérification** : Métriques d'actualité et d'exactitude suivies conformément à ISMS-IMP-A.5.9-3 (Évaluation de la qualité et de la conformité).

## Exigences d'intégration

**Exigence A.5.9-R6** : [Organisation] DOIT intégrer l'inventaire des actifs avec les autres processus du SMSI et systèmes organisationnels.

**Points d'intégration obligatoires** :

| Contrôle/Processus SMSI | Exigence d'intégration | Objet |
|------------------------|------------------------|-------|
| **A.5.12 (Classification de l'information)** | Classification attribuée aux actifs informationnels | Sélection des contrôles |
| **A.5.13 (Étiquetage)** | Les étiquettes référencent la classification de l'inventaire | Marquage de sécurité visible |
| **A.5.15 (Contrôle d'accès)** | Règles d'accès fondées sur la propriété et la classification | Décisions d'autorisation |
| **A.5.18 (Droits d'accès)** | Droits d'accès approuvés par les propriétaires | Application de la responsabilité |
| **A.8.x (Contrôles techniques)** | Les contrôles techniques protègent les actifs inventoriés | Cartographie contrôle-actif |
| **Gestion des risques (Clause 6)** | L'inventaire fournit des données d'entrée pour l'évaluation | Identification menace-actif-vulnérabilité |
| **Gestion des changements** | Les changements déclenchent des mises à jour | Maintenance de l'actualité |
| **Gestion des incidents** | Les incidents référencent les actifs affectés | Évaluation d'impact |
| **Continuité des activités** | Identification des actifs critiques pour le PCA/PRA | Priorisation |

**Intégration avec les systèmes organisationnels** :

| Système | Objet de l'intégration | Synchronisation |
|---------|------------------------|-----------------|
| **CMDB (Base de données de gestion des configurations)** | Source de l'inventaire des actifs informatiques | Bidirectionnelle (là où techniquement réalisable) |
| **Achats/Finance** | Suivi des acquisitions d'actifs | Entrante (achats → inventaire) |
| **Système RH** | Validation des actifs de personnel | Entrante (RH → inventaire pour rôles/compétences) |
| **Système de gestion des actifs** | Suivi des actifs physiques | Bidirectionnelle |
| **Gestion documentaire** | Référentiel des actifs informationnels | Entrante (GED → métadonnées inventaire) |

**Approche de maturité de l'intégration** : Les exigences d'intégration sont **phasées** selon la maturité des systèmes organisationnels :

**Phase 1 — Certification initiale** (intégration minimale viable) :

- CMDB : Si une CMDB existe, export/réconciliation manuel trimestriel. Si pas de CMDB, l'infrastructure informatique est suivie dans une base de données dédiée avec validation trimestrielle contre les enregistrements d'achats et les analyses de découverte réseau.
- SIRH : Réconciliation manuelle trimestrielle des actifs de personnel (rôles/compétences critiques) contre les enregistrements RH.
- Achats : Révision annuelle des enregistrements d'achats pour les nouvelles acquisitions d'actifs ; nouveaux actifs ajoutés à l'inventaire dans les 30 jours suivant l'approbation d'achat.
- Gestion documentaire : Actifs informationnels identifiés via les exports de métadonnées du référentiel (trimestriel).

**Phase 2 — État de maturité** (dans les 18 mois post-certification) :

- Synchronisation automatisée bidirectionnelle là où techniquement réalisable (CMDB ↔ inventaire, SIRH → inventaire).
- Intégration achats en temps réel (nouveaux enregistrements d'actifs auto-créés à partir des bons de commande approuvés).
- Analyses de découverte automatisées (hebdomadaires) avec alertes de réconciliation.

Progression des phases documentée dans ISMS-IMP-A.5.9-2 Maintenance de l'inventaire. Phase actuelle évaluée trimestriellement via le tableau de bord de synthèse.

**Méthode de vérification** : Efficacité de l'intégration évaluée conformément à ISMS-IMP-A.5.9-2 et ISMS-IMP-A.5.9-3.

---

# Gouvernance et conformité

## Rôles et responsabilités

**3.1.1 Direction générale**

**Responsabilité stratégique** :

- Approuver la politique d'inventaire des actifs et les changements majeurs
- Allouer des ressources pour la mise en œuvre et la maintenance de l'inventaire
- Recevoir les rapports annuels de conformité à l'inventaire
- Assurer une culture organisationnelle supportant la responsabilité des actifs

**Responsabilités spécifiques** :

- Approuver la matrice RACI pour la gouvernance de l'inventaire
- Résoudre les litiges de propriété escaladés depuis les unités métier
- Approuver les dérogations aux exigences d'inventaire (rares, documentées)

**3.1.2 Responsable de la sécurité des systèmes d'information (RSSI)**

**Responsabilité opérationnelle** :

- Posséder la politique et le cadre d'inventaire des actifs
- Définir les exigences et normes de qualité de l'inventaire
- Surveiller la conformité aux exigences d'inventaire
- Rendre compte du statut de conformité à la direction générale
- Coordonner avec d'autres propriétaires de contrôles (Classification A.5.12, Contrôle d'accès A.5.15)

**Responsabilités spécifiques** :

- Approuver le cadre de catégorisation de l'inventaire
- Définir les objectifs d'exactitude, de complétude et d'actualité
- Réviser et approuver les résultats d'évaluation
- Escalader les lacunes significatives à la direction générale
- Maintenir la connaissance des changements réglementaires affectant l'inventaire

**3.1.3 Responsable de la sécurité de l'information**

**Mise en œuvre tactique** :

- Mettre en œuvre le cadre d'inventaire des actifs
- Mener des évaluations périodiques de l'inventaire
- Fournir des orientations aux propriétaires et gardiens d'actifs
- Suivre et reporter les métriques (complétude, exactitude, attribution de propriétaires)
- Coordonner les activités de révision et de validation périodiques

**Responsabilités spécifiques** :

- Générer les classeurs d'évaluation
- Faciliter le processus d'accusé de réception des propriétaires
- Mener des activités d'échantillonnage et de validation
- Maintenir les éléments de preuve d'évaluation
- Préparer les rapports de conformité pour le RSSI

**3.1.4 Opérations informatiques / Équipes d'infrastructure**

**Gestion des actifs informatiques** :

- Maintenir l'inventaire des infrastructures informatiques (serveurs, stockage, réseau, postes)
- Intégrer l'inventaire avec la CMDB
- Mener des analyses de découverte automatisées
- Mettre à jour l'inventaire pour les événements du cycle de vie des actifs informatiques
- Soutenir la validation et la réconciliation de l'inventaire

**3.1.5 Propriétaires d'applications / Propriétaires de systèmes**

**Gestion des actifs applicatifs** :

- Maintenir l'inventaire des applications et systèmes
- Documenter les dépendances des applications et les flux d'information
- Classifier les applications selon le cadre de criticité
- Mettre à jour l'inventaire pour les changements applicatifs (versions, configurations, mises hors service)
- S'assurer que les relations application-actif informationnel sont documentées

**3.1.6 Propriétaires d'informations / Propriétaires de données**

**Propriété des actifs informationnels** :

- Posséder les actifs informationnels attribués tout au long de leur cycle de vie
- Classifier les informations conformément à A.5.12 (Classification de l'information)
- Réviser les enregistrements d'inventaire des actifs informationnels au moins annuellement
- Approuver l'accès aux informations dont ils sont propriétaires
- Participer aux évaluations des risques informationnels
- Prendre les décisions de conservation et d'élimination conformément à A.8.10

**3.1.7 Gardiens d'actifs**

**Gestion opérationnelle des actifs** :

- Exécuter les tâches opérationnelles déléguées par le propriétaire
- Maintenir la disponibilité et l'intégrité des actifs
- Mettre à jour les enregistrements d'inventaire pour les changements courants
- Signaler les problèmes au propriétaire
- Mettre en œuvre les contrôles de sécurité selon les instructions du propriétaire

**Distinction** : Les gardiens ont la responsabilité opérationnelle mais la responsabilité reste avec le propriétaire.

**3.1.8 Tout le personnel**

**Responsabilités des utilisateurs** :

- Signaler immédiatement les actifs perdus, volés ou endommagés
- Se conformer aux politiques d'utilisation acceptable pour les actifs assignés
- Notifier les opérations informatiques des changements d'actifs (matériel, logiciel)
- Restituer les actifs lors d'un départ ou d'un changement de rôle
- Participer à la vérification périodique des actifs lorsque demandé

**3.1.9 Audit interne / Conformité**

**Vérification indépendante** :

- Mener des audits indépendants de l'inventaire
- Vérifier la conformité aux exigences de la politique
- Tester l'efficacité des contrôles (exactitude, complétude, attribution de propriétaires)
- Rendre compte des résultats à la direction générale et au RSSI
- Recommander des améliorations au cadre d'inventaire

## Matrice RACI

**Gouvernance de l'inventaire des actifs** :

| Activité | Dir. gén. | RSSI | Resp. séc. | Ops IT | Prop. app. | Prop. info. | Gardiens | Tout pers. | Audit |
|----------|-----------|------|------------|--------|------------|-------------|----------|------------|-------|
| **Approbation de la politique** | A | R | C | I | I | I | I | I | C |
| **Conception du cadre** | I | A | R | C | C | C | I | I | C |
| **Identification des actifs** | I | I | C | R | R | R | C | I | I |
| **Attribution des propriétaires** | I | A | C | C | C | R | I | I | I |
| **Création des enregistrements** | I | I | C | R | R | C | C | I | I |
| **Maintenance des enregistrements** | I | I | C | R | R | R | R | I | I |
| **Révision de l'exactitude** | I | I | C | C | R | R | C | I | I |
| **Évaluation de la conformité** | I | A | R | C | C | C | I | I | C |
| **Remédiation des écarts** | C | A | R | R | R | R | C | I | I |
| **Reporting** | I | A | R | C | C | I | I | I | C |
| **Audit indépendant** | I | I | C | I | I | I | I | I | A/R |
| **Approbation des dérogations** | A | R | C | I | C | C | I | I | C |

**Légende** : R = Responsable (fait le travail), A = Autorité (décision finale), C = Consulté (contributions), I = Informé (tenu au courant)

## Évaluation et vérification

**Exigence A.5.9-R7** : [Organisation] DOIT mener des évaluations périodiques pour vérifier la conformité de l'inventaire.

**Cadre d'évaluation** (5 domaines) :

| Domaine d'évaluation | Identifiant | Focus de l'évaluation | Fréquence |
|---------------------|-------------|----------------------|-----------|
| **Identification et découverte des actifs** | ISMS-IMP-A.5.9-1 | Procédures de découverte, complétude | Trimestrielle |
| **Maintenance de l'inventaire** | ISMS-IMP-A.5.9-2 | Structure, procédures de mise à jour, intégration | Trimestrielle |
| **Qualité et conformité** | ISMS-IMP-A.5.9-3 | Exactitude, complétude, vérification de l'actualité | Trimestrielle |
| **Responsabilité des propriétaires** | ISMS-IMP-A.5.9-4 | Attribution, accusé de réception, formation | Trimestrielle |

**Métriques de conformité** :

| Métrique | Objectif | Méthode de mesure | Fréquence de reporting |
|----------|----------|-------------------|------------------------|
| **Complétude** | ≥ 95 % pour les actifs critiques, ≥ 90 % pour les standards | Réconciliation de découverte | Trimestrielle |
| **Exactitude** | ≥ 95 % information, ≥ 98 % IT | Échantillonnage statistique | Trimestrielle |
| **Actualité** | ≥ 98 % dans les seuils d'ancienneté | Analyse des dates de révision | Mensuelle |
| **Attribution de propriétaire** | 100 % | Vérification champ propriétaire vide | Mensuelle |
| **Accusé de réception** | ≥ 95 % dans les 30 jours | Suivi des accusés | Mensuelle |
| **Respect du calendrier de révision** | ≥ 90 % des révisions à temps | Conformité au calendrier | Trimestrielle |

## Gestion des dérogations

**Exigence A.5.9-R8** : [Organisation] DOIT établir un processus formel de dérogation pour les écarts aux exigences d'inventaire.

**Catégories de dérogations** :

1. **Dérogation de granularité** : L'actif nécessite un niveau de détail différent du standard
2. **Dérogation de fréquence de révision** : L'actif nécessite un calendrier de révision différent
3. **Dérogation de propriété** : L'actif a une propriété incertaine nécessitant un temps de résolution prolongé
4. **Dérogation technique** : Les contraintes techniques empêchent l'approche d'inventaire standard

**Processus de demande de dérogation** :

1. Le demandeur soumet une demande de dérogation avec justification métier
2. Le responsable de la sécurité de l'information effectue une évaluation des risques
3. Le RSSI approuve/refuse la dérogation
4. Les dérogations approuvées sont documentées avec :
   - Justification et évaluation des risques
   - Contrôles compensatoires (le cas échéant)
   - Date d'expiration (maximum 12 mois)
   - Critères de réévaluation
5. Les dérogations sont révisées lors des évaluations périodiques
6. Le registre des dérogations est maintenu comme élément de preuve

**Autorité de dérogation** :

- **Responsable de la sécurité de l'information** : Approuver les dérogations temporaires ≤ 30 jours (tactiques)
- **RSSI** : Approuver les dérogations ≤ 12 mois (stratégiques)
- **Direction générale** : Approuver les dérogations > 12 mois (rares, documentées au niveau du conseil)

**Durée maximale de dérogation** : 12 mois (doit être renouvelée ou remédiée)

## Réponse aux incidents

**Exigence A.5.9-R9** : [Organisation] DOIT utiliser l'inventaire des actifs pour soutenir les processus de réponse aux incidents.

**L'inventaire dans la réponse aux incidents** :

- **Identification des actifs** : Identifier rapidement les actifs affectés et leurs dépendances
- **Notification des propriétaires** : Contacter les propriétaires pour l'évaluation de l'impact métier
- **Évaluation de l'impact** : Déterminer la criticité en utilisant les métadonnées de l'inventaire
- **Confinement** : Utiliser les informations de dépendance pour isoler les systèmes affectés
- **Récupération** : Prioriser la récupération selon la classification de criticité
- **Analyse des causes profondes** : Recouper les configurations et relations des actifs

**Actions d'inventaire déclenchées par incident** :

- Vérifier que les enregistrements d'inventaire des actifs affectés sont à jour
- Mettre à jour le statut si l'actif est endommagé ou compromis
- Documenter l'incident dans l'historique de l'actif
- Réviser et mettre à jour la classification des risques si justifié
- Mener une validation post-incident de l'inventaire

## Gouvernance de la politique

**Fréquence de révision** : Annuelle au minimum, ou déclenchée par :

- Changements organisationnels significatifs (fusions, acquisitions, restructurations)
- Changements réglementaires majeurs affectant la gestion des actifs
- Conclusions d'audit nécessitant des mises à jour de la politique
- Évaluation des risques identifiant des lacunes de la politique
- Changements technologiques affectant l'approche d'inventaire

**Processus de révision** :

1. Le responsable de la sécurité propose des mises à jour de la politique
2. Le RSSI révise et approuve les changements
3. Le service juridique/conformité révise l'alignement réglementaire
4. Consultation des parties prenantes (opérations IT, propriétaires d'applications, propriétaires d'informations)
5. Approbation finale de la direction générale
6. Communication et formation sur les changements
7. Contrôle des versions et historique des changements maintenus

**Autorité d'approbation** : Direction générale (PDG ou autorité désignée)

**Contrôle des versions** : Toutes les versions de la politique conservées pour la piste d'audit (conservation minimale de 7 ans)

---

# Mise en œuvre et références

## Intégration avec le SMSI

**Évaluation des risques** (Clause 6.1 de l'ISO 27001) :

- L'inventaire des actifs constitue le fondement de l'identification des risques
- La criticité des actifs influence l'évaluation et la priorisation du traitement
- L'analyse menace-actif-vulnérabilité nécessite un inventaire complet
- Les plans de traitement des risques référencent les actifs inventoriés

**Déclaration d'applicabilité** (Clause 6.1.3 de l'ISO 27001) :

- Applicabilité du contrôle A.5.9 justifiée dans la DdA de [Organisation]
- Statut de mise en œuvre suivi et reporté
- L'inventaire des actifs permet la mise en œuvre des autres contrôles de l'Annexe A

**Contrôles connexes** :

| Contrôle | Relation | Point d'intégration |
|----------|----------|---------------------|
| **A.5.10 (Utilisation acceptable)** | Définit l'utilisation acceptable des actifs inventoriés | Les enregistrements référencent la politique |
| **A.5.11 (Restitution des actifs)** | Restitution suivie dans l'inventaire | Statut mis à jour à la restitution/cession |
| **A.5.12 (Classification)** | Classification appliquée aux actifs informationnels | Champ classification dans l'inventaire |
| **A.5.13 (Étiquetage)** | Étiquettes appliquées selon la classification | Génération d'étiquettes via données d'inventaire |
| **A.5.14 (Transfert)** | Contrôles de transfert fondés sur la classification | Journaux référencent l'inventaire |
| **A.5.15 (Contrôle d'accès)** | Règles d'accès protègent les actifs | Politiques de contrôle fondées sur les actifs |
| **A.5.16 (Gestion des identités)** | Identités liées aux actifs de personnel | Inventaire valide les identités |
| **A.5.17 (Authentification)** | Protège l'accès aux actifs | Systèmes nécessitant authentification inventoriés |
| **A.5.18 (Droits d'accès)** | Propriétaires approuvent les droits | Propriété dans l'inventaire active le flux d'approbation |
| **A.8.9 (Gestion des configurations)** | Références de configuration pour IT | Référence incluse dans l'inventaire |
| **A.8.10 (Suppression)** | La cession met à jour le statut | Déclencheurs d'inventaire à la suppression |
| **A.8.19 (Installation logicielle)** | Crée un enregistrement | Inventaire applicatif maintenu |

## Ressources de mise en œuvre

**Suite de mise en œuvre** (ISMS-IMP-A.5.9) :

| Identifiant | Titre | Objet | Public cible |
|-------------|-------|-------|--------------|
| **ISMS-IMP-A.5.9-1-UG/TG** | Identification et découverte des actifs | Procédures d'identification, méthodes de découverte, vérification de complétude | Équipe sécurité, opérations IT |
| **ISMS-IMP-A.5.9-2-UG/TG** | Maintenance de l'inventaire | Conception de la structure, procédures de mise à jour, méthodes d'intégration | Équipe sécurité, opérations IT, propriétaires |
| **ISMS-IMP-A.5.9-3-UG/TG** | Évaluation de la qualité et conformité | Échantillonnage d'exactitude, vérification d'actualité, analyse des écarts | Équipe sécurité, audit, conformité |
| **ISMS-IMP-A.5.9-4-UG/TG** | Évaluation de la responsabilité des propriétaires | Attribution, suivi des accusés, vérification des responsabilités | Équipe sécurité, direction, propriétaires |

## Cartographie réglementaire

| Catégorie d'exigence | nLPD suisse | RGPD UE | ISO 27001 | PCI DSS v4.0.1* | FINMA* | DORA/NIS2* | HIPAA* |
|---------------------|-------------|---------|-----------|-----------------|--------|------------|--------|
| Identification des actifs | Art. 8 | Art. 5, 30 | A.5.9 | Req. 2.4 | Fondé risques | Gestion actifs | 164.310(d)(1) |
| Attribution propriétaire | Art. 8 | Art. 5 | A.5.9 | Req. 12.5 | Fondé risques | Registre TIC | 164.308(a)(2) |
| Exactitude et actualité | Art. 8 | Art. 5 | A.5.9 | Req. 12.5.2 | Fondé risques | Inventaire actuel | 164.310(d)(1) |
| Classification | Art. 8 | Art. 32 | A.5.9, A.5.12 | Req. 2.2 | Fondé risques | Criticité | 164.308(a)(1) |

*Applicabilité conditionnelle conformément à ISMS-POL-00

## Formation et sensibilisation

**Sensibilisation à la sécurité** (Tout le personnel) :

- Module de formation annuel sur les responsabilités liées aux actifs
- Procédures de signalement des actifs perdus/endommagés
- Utilisation acceptable et manipulation des actifs
- Considérations de vie privée (notamment pour les actifs de personnel)

**Formation des propriétaires d'actifs** :

- Responsabilités de propriété et de responsabilité
- Procédures de révision de l'inventaire
- Flux de travail d'approbation des accès
- Orientations de classification conformément à A.5.12
- Processus de demande de dérogation

**Formation technique** (personnel IT/sécurité) :

- Configuration et fonctionnement des outils de découverte
- Administration du système d'inventaire
- Complétion des classeurs d'évaluation
- Intégration avec la CMDB et autres systèmes
- Collecte d'éléments de preuve pour les audits

**Formation des gardiens** :

- Responsabilités opérationnelles
- Procédures de mise à jour de l'inventaire
- Signalement des incidents
- Limites de délégation

---

# Définitions

**Actif** : Tout ce qui a de la valeur pour [Organisation] et nécessite une protection. Les actifs comprennent les informations, l'infrastructure informatique, les applications, les ressources physiques et les compétences du personnel.

**Actif informationnel** : Données, contenus ou connaissances sous toute forme (bases de données structurées, documents non structurés, propriété intellectuelle, configurations, identifiants) avec des exigences de confidentialité, d'intégrité ou de disponibilité.

**Actif associé** : Infrastructure, applications, installations ou personnel qui traitent, stockent, transmettent ou protègent des actifs informationnels. Ces actifs tirent leurs exigences de sécurité des informations qu'ils supportent.

**Propriétaire d'actif** : Individu responsable d'un actif tout au long de son cycle de vie. Le propriétaire est responsable de la classification, de l'approbation des accès, des décisions de protection et de la conformité aux exigences. La propriété est attribuée sur la base de la responsabilité métier, non de la garde technique.

**Gardien d'actif** : Individu ou équipe ayant la responsabilité opérationnelle quotidienne d'un actif. Le gardien met en œuvre les contrôles de sécurité selon les instructions du propriétaire mais la responsabilité reste avec le propriétaire.

**Inventaire des actifs** : Registre structuré des informations et des actifs associés, documentant les attributs obligatoires incluant le propriétaire, la classification, la localisation et le statut du cycle de vie.

**Complétude de l'inventaire** : Degré auquel l'inventaire inclut tous les actifs dans le périmètre. Mesuré en pourcentage des actifs découverts présents dans l'inventaire.

**Exactitude de l'inventaire** : Degré auquel les données d'inventaire reflètent correctement l'état réel des actifs. Mesuré par échantillonnage et validation par rapport aux sources faisant autorité.

**Actualité de l'inventaire** : Degré auquel l'inventaire reflète l'état actuel plutôt que l'état historique. Mesuré par les dates de révision et la rapidité de mise à jour.

**Criticité** : Évaluation de l'impact métier si l'actif est indisponible, compromis ou détruit. Utilisée pour prioriser le traitement des risques et la réponse aux incidents.

**État du cycle de vie** : Étape actuelle dans le cycle de vie de l'actif (actif, en développement, en maintenance, retraité, archivé). Détermine les contrôles et exigences de maintenance applicables.

**Découverte** : Processus automatisé ou manuel pour identifier les actifs dans l'environnement organisationnel. La découverte compare les résultats avec l'inventaire pour identifier les lacunes.

**CMDB (Base de données de gestion des configurations)** : Système organisationnel documentant les configurations des infrastructures informatiques. Source primaire de l'inventaire des actifs informatiques lorsque mis en œuvre.

**Actif de personnel** : Rôles organisationnels clés et compétences spécialisées (non des enregistrements individuels). Documentés de manière générique pour protéger la vie privée tout en permettant la planification de la continuité.

**Granularité** : Niveau de détail auquel les actifs sont inventoriés. Les actifs à haut risque nécessitent des enregistrements individuels ; les actifs à faible risque peuvent être regroupés (p. ex. « ordinateurs portables standard — quantité 50 »).

---

# Éléments de preuve pour cette politique

**Éléments de preuve pour l'Étape 1 (revue documentaire) :**

Éléments de preuve requis pour démontrer que cette politique est adéquatement documentée et approuvée :

- ✅ Ce document de politique (ISMS-POL-A.5.9 v1.0)
- ✅ Signatures d'approbation du RSSI, de la direction générale, du responsable juridique/conformité
- ✅ Exigences de création de l'inventaire définies (Section 2.1)
- ✅ Cadre de catégorisation des actifs documenté (Section 2.2, Annexe A)
- ✅ Attributs obligatoires de l'inventaire précisés (Section 2.3)
- ✅ Exigences de propriété des actifs définies (Section 2.4)
- ✅ Normes de qualité de l'inventaire établies (Section 2.5 — complétude, exactitude, actualité)
- ✅ Exigences d'intégration documentées (Section 2.6)
- ✅ Rôles et responsabilités attribués (Section 3)
- ✅ Procédures de gouvernance et de révision définies (Section 3.3)
- ✅ Intégration avec les contrôles connexes documentée (Section 4.1)

**Éléments de preuve pour l'Étape 2 (efficacité opérationnelle) :**

Éléments de preuve requis pour démontrer que cette politique est opérationnellement efficace :

- Évaluations d'identification et de découverte conformément à ISMS-IMP-A.5.9-1
- Évaluations de maintenance conformément à ISMS-IMP-A.5.9-2
- Évaluations de qualité et conformité conformément à ISMS-IMP-A.5.9-3
- Évaluations de responsabilité des propriétaires conformément à ISMS-IMP-A.5.9-4
- Enregistrements d'inventaire des actifs (tous types : informationnel, IT, applicatif, physique, personnel)
- Déterminations de catégorisation des actifs (type, criticité, état du cycle de vie)
- Attributions de propriété avec accusés de réception (objectif 100 %)
- Métriques de complétude (pourcentage d'actifs découverts vs inventoriés)
- Métriques d'exactitude (pourcentage d'enregistrements vérifiés comme exacts)
- Métriques d'actualité (pourcentage d'enregistrements mis à jour dans les délais)
- Enregistrements de révision par les propriétaires (attestations annuelles)
- Éléments de preuve d'intégration avec d'autres contrôles
- Enregistrements de synchronisation CMDB/RH/achats
- Documentation du cycle de vie des actifs (acquisition, changement, cession)
- Enregistrements d'escalade d'actifs sans propriétaire (résolution < 30 jours)
- Résultats d'audit et éléments de preuve de remédiation

**Référentiel et conservation des éléments de preuve** :

- **Emplacement principal** : Tous les éléments de preuve du contrôle A.5.9 maintenus dans [Plateforme GRC / Référentiel central d'éléments de preuve]. Base de données d'inventaire hébergée dans [Nom du système]. Classeurs d'évaluation archivés dans [Bibliothèque d'éléments de preuve SMSI].
- **Durée de conservation** : Minimum 3 ans conformément à la clause 7.5.3 de l'ISO 27001, alignée avec la politique générale de conservation de [Organisation]. Classeurs, accusés, registres des écarts et registre des dérogations conservés pendant la durée de la certification plus 3 ans.
- **Contrôle d'accès** : Accès au référentiel limité au responsable de la sécurité, à l'audit interne et au personnel autorisé conformément à la politique A.5.15. Accès en lecture seule accordé aux auditeurs externes pendant la période d'audit.
- **Sauvegarde** : Éléments de preuve sauvegardés conformément aux exigences A.8.13 ; testés trimestriellement.

---

# Annexe A : Matrice de décision pour la catégorisation des actifs

## Objet

Cette annexe fournit un cadre de décision pratique pour catégoriser les actifs dans l'inventaire. Ce sont des **exemples génériques** que [Organisation] adapte à son contexte spécifique lors de l'évaluation des risques.

## Catégorisation primaire : Information vs. Actif associé

**Question de décision** : S'agit-il d'une INFORMATION ou de QUELQUE CHOSE QUI TRAITE/STOCKE DES INFORMATIONS ?

```
┌─ INFORMATION (données, contenus, connaissances)
│  └─ Catégories d'actifs informationnels :
│     ├─ Données structurées (bases de données, tables, entrepôts)
│     ├─ Documents non structurés (fichiers, courriels, rapports)
│     ├─ Enregistrements et archives (conservés pour conformité)
│     ├─ Propriété intellectuelle (secrets, brevets, conceptions)
│     ├─ Configuration et paramètres (configs, paramètres)
│     ├─ Authentification et cryptographie (clés, certificats, identifiants)
│     ├─ Enregistrements de communication (courriels, chats, journaux)
│     └─ Intelligence métier (rapports, analyses, tableaux de bord)
│
└─ AUTRE CHOSE (système, équipement, installation, personne)
   └─ Catégories d'actifs associés :
      ├─ Infrastructure informatique (serveurs, stockage, réseau, postes)
      ├─ Applications (logiciels, SaaS, services, API)
      ├─ Actifs physiques (installations, supports, équipements)
      └─ Actifs de personnel (compétences, rôles clés)
```

## Cadre d'évaluation de la criticité

**Questions d'impact métier** (détermine la criticité) :

| Domaine d'impact | Critique | Élevé | Moyen | Faible |
|------------------|----------|-------|-------|--------|
| **Opérationnel** | Perturbation totale | Défaillance majeure | Dégradation | Inconvénient mineur |
| **Financier** | > 5 % du CA annuel | 1-5 % du CA | < 1 % du CA | Négligeable |
| **Réglementaire** | Notification obligatoire, amendes | Violation de conformité | Violation mineure | Sans impact |
| **Réputationnel** | Médias nationaux, fuite clients | Presse sectorielle, perte clients | Presse locale, plaintes | Aucune visibilité |
| **Temps de récupération** | Irremplaçable | > 1 mois | 1 semaine à 1 mois | < 1 semaine |

**Attribution de la criticité** : Utiliser le domaine d'impact le plus élevé pour la classification globale.

## Cadre de décision de granularité

**Question** : À quel niveau devons-nous inventorier cet actif ?

**Haute granularité** (enregistrements individuels) lorsque :

- L'actif est critique aux opérations
- L'actif traite des informations sensibles (classification Élevée/Très élevée conformément à A.5.12)
- Les exigences réglementaires imposent un suivi individuel
- L'actif est unique ou spécialisé
- La valeur de l'actif justifie la charge de suivi

**Faible granularité** (enregistrements groupés) lorsque :

- Les actifs sont courants/standardisés
- Les actifs sont à faible risque et facilement remplaçables
- Le suivi individuel crée une charge de maintenance excessive
- Les actifs sont homogènes (modèle, configuration, objet identiques)

**Exemples** :

| Type d'actif | Granularité | Justification |
|--------------|-------------|---------------|
| Serveur de base de données production | Individuel | Critique, unique, traite données sensibles |
| Ordinateur portable du PDG | Individuel | Utilisateur à haut risque, informations sensibles potentielles |
| Ordinateurs portables standards des employés (modèle identique) | Groupé (quantité : 100) | Courant, standardisé, faible risque individuel |
| Base de données DCP clients | Individuel | Exigence réglementaire, haute sensibilité |
| Points d'accès WiFi de bureau | Groupé par bâtiment | Standardisés, faible importance individuelle |
| Référentiels de code source | Individuel | Propriété intellectuelle, contrôle de version nécessaire |
| PDFs de brochures marketing | Groupé par campagne | Information publique, faible valeur individuelle |
| Comptes administrateur de domaine | Individuel | Hauts privilèges, suivi précis requis |
| Bandes de sauvegarde | Groupé par rotation | Suivi par lot, non individuellement |

## Exemples de catégorisation des actifs informationnels

**Données structurées** : Base de données clients (CRM), enregistrements de transactions financières, dossiers employés (SIRH), base de données de produits, entrepôt de données web analytics, archives de courriels, journaux d'audit

**Documents non structurés** : Contrats et accords, documentation de projet, politiques et procédures, manuels employés, supports marketing, enregistrements de réunions, spécifications de conception

**Propriété intellectuelle** : Référentiels de code source, demandes de brevet et brevets accordés, secrets commerciaux (formules, algorithmes, méthodes), conceptions et plans, actifs de marque (logos, marques déposées), données de recherche propriétaires

**Configuration et paramètres** : Fichiers de configuration système, paramètres d'application, configurations d'équipements réseau (règles routeurs, pare-feu), modèles Infrastructure-as-Code, schémas de bases de données et procédures stockées

## Exemples de catégorisation de l'infrastructure informatique

**Calcul** : Serveurs physiques (production, développement, test), machines virtuelles, conteneurs et plateformes d'orchestration, postes de travail, ordinateurs portables et appareils mobiles

**Stockage** : Systèmes SAN/NAS, infrastructures de sauvegarde, stockage d'archivage, buckets de stockage cloud, serveurs de fichiers

**Réseau** : Routeurs et commutateurs, pare-feu et équipements de sécurité, équilibreurs de charge, concentrateurs VPN, points d'accès sans fil, serveurs DNS/DHCP

## Exemples de catégorisation des applications

**Applications métier** : ERP, CRM, système de gestion financière, SIRH, outils de gestion de projet, plateformes de collaboration

**SaaS et services cloud** : Service de messagerie (Microsoft 365, Google Workspace), stockage cloud (Dropbox, OneDrive), outils de communication (Slack, Teams, Zoom), plateformes de développement (GitHub, GitLab, Jira)

**Applications développées en interne** : Portail client, applications de gestion internes, applications mobiles, API et services d'intégration

## Catégorisation des actifs de personnel

**Rôles critiques** (rôles, non individus) : Cadres dirigeants (PDG, DAF, DSI, RSSI), rôles techniques clés (architecte principal, administrateur de bases de données senior), rôles de conformité réglementaire (DPD, responsable conformité), rôles d'opérations de sécurité (responsable SOC, réponse aux incidents)

**Compétences spécialisées** : Expertise technique approfondie (technologies spécifiques, systèmes hérités), expertise réglementaire, relations fournisseurs, certifications, compétences linguistiques

**Note de vie privée** : Les actifs de personnel documentent des RÔLES et des COMPÉTENCES, jamais des enregistrements individuels. « Compétence administrateur de bases de données (3 personnes qualifiées) » NON « Jean Dupont — DBA ».

---

# Annexe B : Guide de référence rapide pour les propriétaires d'actifs

## Votre rôle en tant que propriétaire d'actif

**Vous êtes responsable** des informations ou des actifs associés qui vous ont été attribués. Ce guide résume vos responsabilités.

## Erreurs courantes à éviter

1. **Confondre « Propriétaire » et « Gardien »** : Vous êtes responsable même si l'informatique gère le système. Propriétaire = responsabilité métier, Gardien = gestion opérationnelle.
2. **Classifier tous les actifs comme « Critiques »** : Utilisez le cadre d'impact métier (Annexe A). Tout n'est pas critique — cela dilue le sens.
3. **Lister des personnes individuelles comme actifs de personnel** : Documentez les rôles/compétences, pas les noms. « Compétence administrateur de bases de données (3 personnes qualifiées) » NON « Jean Dupont — DBA ».
4. **Oublier de mettre à jour l'inventaire quand les actifs changent** : Configurez des rappels pour les actifs dont vous êtes propriétaire.
5. **Supposer que quelqu'un d'autre mettra à jour** : En tant que propriétaire, vous êtes responsable de l'exactitude des enregistrements même si le gardien effectue les mises à jour.

## Responsabilités principales

**1. Classifier vos actifs** (conformément à ISMS-POL-A.5.12)

- Déterminer les exigences de confidentialité, intégrité, disponibilité
- Considérer l'impact métier si l'actif est compromis
- Documenter la classification dans l'inventaire

**2. Réviser les enregistrements d'inventaire**

- **Fréquence** : Au moins annuellement, ou après des changements significatifs
- **Vérifier** : Description, localisation, classification, dépendances sont exactes
- **Mettre à jour** : Soumettre des mises à jour si les informations changent
- **Attester** : Confirmer l'exactitude en signant le relevé de révision

**3. Approuver les demandes d'accès**

- Examiner les demandes d'accès pour les actifs dont vous êtes propriétaire
- Vérifier le besoin métier et les privilèges appropriés
- Approuver/refuser selon le principe du moindre privilège
- Documenter la justification de la décision

**4. Signaler les incidents de sécurité**

- Signaler immédiatement les incidents affectant les actifs dont vous êtes propriétaire
- Participer aux investigations
- Approuver les procédures de récupération et de restauration
- Réviser la classification si l'incident révèle de nouveaux risques

**5. Gérer le cycle de vie des actifs**

- Participer aux décisions : conservation, archivage, cession
- Assurer une cession appropriée conformément à ISMS-POL-A.8.10
- Mettre à jour l'inventaire lors de la mise hors service ou de l'archivage
- Transférer la propriété lors d'un changement de rôle

## Lorsque vous avez besoin d'aide

**Questions d'inventaire** : Contacter le responsable de la sécurité de l'information
**Problèmes techniques** : Contacter les opérations IT ou le gardien du système
**Orientations de classification** : Contacter le RSSI ou le responsable de la sécurité
**Flux d'approbation des accès** : Contacter l'équipe de gestion des identités et des accès
**Signalement d'incidents** : Contacter le SOC ou le service d'assistance

## Listes de contrôle courantes

**Lors de la révision annuelle de l'inventaire** :

- [ ] Vérifier que la description de l'actif est exacte
- [ ] Confirmer que la localisation physique/logique est correcte
- [ ] Valider que la classification de criticité est toujours appropriée
- [ ] Vérifier que les dépendances sont documentées
- [ ] S'assurer que l'attribution du gardien est à jour
- [ ] Réviser la liste des accès (si disponible)
- [ ] Confirmer que la classification est appropriée (conformément à A.5.12)
- [ ] Signer le formulaire d'attestation
- [ ] Soumettre au responsable de la sécurité de l'information

**Lors de l'attribution en tant que propriétaire** :

- [ ] Recevoir la notification formelle d'attribution
- [ ] Réviser l'enregistrement d'inventaire de l'actif
- [ ] Lire ce guide de référence rapide
- [ ] Suivre la formation de propriétaire (si requise)
- [ ] Signer le formulaire d'accusé de réception
- [ ] Ajouter l'actif à votre calendrier de révision

**Lors d'un changement de rôle** :

- [ ] Générer la liste des actifs dont vous êtes propriétaire
- [ ] Identifier les successeurs (avec approbation du manager)
- [ ] Documenter la transition dans la gestion des changements
- [ ] Mener une réunion de passation avec le nouveau propriétaire
- [ ] Mettre à jour l'inventaire avec le nouveau propriétaire
- [ ] Confirmer la réception de l'accusé du nouveau propriétaire

## Références de politique clés

- **Politique complète** : ISMS-POL-A.5.9 (ce document)
- **Guides de mise en œuvre** : ISMS-IMP-A.5.9-1 à A.5.9-5
- **Politique de classification** : ISMS-POL-A.5.12
- **Politique de suppression** : ISMS-POL-A.8.10
- **Politique de contrôle d'accès** : ISMS-POL-A.5.15

## Questions ou dérogations ?

**Pour les questions** : Contacter le responsable de la sécurité de l'information
**Pour les dérogations** : Soumettre une demande conformément à la Section 3.4 de la politique complète
**Pour les urgences** : Contacter immédiatement le Centre des opérations de sécurité (SOC)

---

**FIN DU DOCUMENT DE POLITIQUE**

---

*Cette politique établit les exigences pour l'inventaire des informations et des actifs associés. Les procédures de mise en œuvre sont documentées dans ISMS-IMP-A.5.9-1 à A.5.9-5 (UG/TG).*

<!-- QA_VERIFIED: 2026-03-30 -->
