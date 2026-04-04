<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.24-28-FR:framework:POL:a.5.24-28 -->
**ISMS-POL-A.5.24-28 — Cycle de vie de la gestion des incidents**

---

**Contrôle documentaire**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Cycle de vie de la gestion des incidents |
| **Type de document** | Politique |
| **Identifiant du document** | ISMS-POL-A.5.24-28 |
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
| 1.0 | [Date] | RSSI | Politique initiale pour la première certification ISO 27001:2022 |

**Cycle de révision** : Annuel
**Prochaine révision** : [Date d'entrée en vigueur + 12 mois]

**Chaîne d'approbation** :

- Primaire : Responsable de la sécurité des systèmes d'information (RSSI)
- Secondaire : Directeur des systèmes d'information (DSI)
- Technique : Responsable de la réponse aux incidents / Responsable CSIRT
- Juridique : Responsable juridique/conformité
- Autorité finale : Direction générale

**Documents connexes** :

- ISMS-POL-00 (Cadre d'applicabilité réglementaire)
- ISMS-REF-A.5.24-28 (Guide de référence de réponse aux incidents)
- ISMS-IMP-A.5.24-28.-UG/TGS1 à S5 (Évaluations de mise en œuvre)
- ISO/IEC 27001:2022 Contrôles A.5.24, A.5.25, A.5.26, A.5.27, A.5.28
- ISMS-POL-A.8.15 (Journalisation)
- ISMS-POL-A.8.16 (Activités de surveillance)
- ISMS-POL-A.6.8 (Signalement des événements de sécurité de l'information)
- ISMS-POL-A.5.29-30 (Continuité d'activité et reprise après sinistre)
- ISMS-POL-A.5.31 (Exigences légales, réglementaires et contractuelles)

---

# Résumé exécutif

La présente politique établit les exigences de l'[Organisation] en matière de gestion des incidents de sécurité de l'information tout au long de leur cycle de vie complet, conformément aux contrôles ISO/IEC 27001:2022 A.5.24 à A.5.28.

**Objet** : Définir les exigences organisationnelles pour la mise en œuvre et la gouvernance des contrôles de gestion des incidents. Cette politique établit QUELLES capacités de gestion des incidents sont requises, QUI est responsable et QUAND les actions doivent avoir lieu. Les procédures de mise en œuvre (COMMENT exécuter la réponse aux incidents) sont documentées séparément dans les Guides de mise en œuvre ISMS-IMP-A.5.24-28 (variantes UG/TG).

**Périmètre** : Cette politique s'applique à tous les événements et incidents de sécurité de l'information affectant les actifs informationnels, systèmes, réseaux et services de l'[Organisation], quelle que soit leur source (interne, externe, tiers) ou le modèle de déploiement (sur site, nuage, hybride).

**Approche de contrôle combinée** : Ces cinq contrôles sont mis en œuvre dans le cadre d'un cycle de vie unifié :

1. **Planification et préparation (A.5.24)** — Établir les capacités avant que les incidents ne surviennent
2. **Évaluation et décision (A.5.25)** — Déterminer si un événement constitue un incident nécessitant une réponse
3. **Opérations de réponse (A.5.26)** — Contenir, éradiquer, récupérer après les incidents
4. **Collecte de preuves (A.5.28)** — Préserver les preuves forensiques (en parallèle de la réponse)
5. **Apprentissage et amélioration (A.5.27)** — Tirer des enseignements, améliorer les contrôles

Malgré une mise en œuvre unifiée, chaque contrôle maintient des exigences distinctes aux fins de la Déclaration d'applicabilité (DdA).

---

# Périmètre et applicabilité

## Dans le périmètre

**Incidents de sécurité de l'information** affectant :

- Les systèmes informatiques, applications et bases de données
- Les données et actifs informationnels (toutes classifications)
- L'infrastructure réseau (sur site, nuage, hybride)
- Les utilisateurs et systèmes d'authentification
- Les systèmes tiers interfacés avec l'[Organisation]
- Les incidents de sécurité physique affectant les actifs informationnels

**Catégories d'incidents** couvertes :

- Maliciels et rançongiciels
- Accès non autorisés et escalades de privilèges
- Violations et exfiltrations de données
- Déni de service (DoS/DDoS)
- Ingénierie sociale et hameçonnage
- Menaces internes (malveillantes, négligentes)
- Incidents de sécurité physique affectant l'informatique
- Incidents de la chaîne d'approvisionnement et de tiers
- Erreurs de configuration ayant un impact sur la sécurité

## Hors périmètre

Les éléments suivants nécessitent l'approbation de la Direction générale et une acceptation documentée du risque :

- Incidents n'affectant que des informations Publiques (non classifiées) sans impact métier
- Incidents gérés par des cadres distincts (ex. incidents de sécurité des personnes, violations RH sans composante sécurité)
- Incidents de tiers avec délégation contractuelle de la gestion des incidents

## Applicabilité aux tiers

Les prestataires de services tiers, sous-traitants et partenaires accédant aux systèmes de l'[Organisation] ou traitant des données de l'[Organisation] DOIVENT :

- Signaler les événements et incidents de sécurité conformément aux exigences de notification de l'[Organisation]
- Coopérer aux activités de réponse aux incidents de l'[Organisation]
- Se conformer aux exigences de préservation des preuves
- Participer aux revues post-incident lorsque leurs actions ont contribué à l'incident

## Applicabilité réglementaire

La présente politique traite des exigences de conformité obligatoires conformément à ISMS-POL-00 (Cadre d'applicabilité réglementaire) :

**Niveau 1 : Conformité obligatoire**

- **nLPD suisse (FADP)** : Art. 24 — Notification d'une violation de données au PFPDT « dès que possible » en cas de risque élevé
- **RGPD UE** : Art. 33-34 — Notification d'une violation à l'autorité de contrôle dans les 72 heures
- **ISO/IEC 27001:2022** : Contrôles A.5.24, A.5.25, A.5.26, A.5.27, A.5.28

**Niveau 2 : Applicabilité conditionnelle**

- PCI DSS v4.0.1, FINMA, DORA, NIS2, HIPAA — S'appliquent lorsque les activités de l'[Organisation] déclenchent leur applicabilité conformément à ISMS-POL-00

---

# Déclarations de politique

## Planification et préparation de la gestion des incidents (A.5.24)

L'[Organisation] DOIT établir des capacités de gestion des incidents AVANT que ceux-ci ne surviennent.

**PS-3.1.1 Capacité organisationnelle** : L'[Organisation] DOIT établir une capacité de réponse aux incidents via des fonctions CSIRT (équipe de réponse aux incidents de sécurité informatique) et/ou SOC (centre des opérations de sécurité) désignées, disposant d'une autorité et de ressources définies.

**PS-3.1.2 Procédures documentées** : L'[Organisation] DOIT documenter et maintenir des procédures de réponse aux incidents couvrant le cycle de vie complet des incidents. Les procédures DOIVENT être sous contrôle de version et révisées annuellement.

**PS-3.1.3 Cadre de classification** : L'[Organisation] DOIT établir un cadre de classification des incidents définissant les niveaux de gravité et les catégories d'incidents. Ce cadre DOIT permettre une priorisation et une escalade cohérentes des incidents.

**PS-3.1.4 Exigences de formation** : Le personnel de réponse aux incidents DOIT être formé et démontrer ses compétences avant de prendre en charge des fonctions de réponse aux incidents. La compétence DOIT être évaluée par des exercices de simulation pratiques et la vérification par un responsable de la connaissance des procédures de réponse. Les normes de compétence minimales sont définies dans ISMS-IMP-A.5.24-28.S1. La formation DOIT être renouvelée annuellement (intervalle maximal de 12 mois depuis la dernière complétion).

**PS-3.1.5 Exigences d'exercices** : L'[Organisation] DOIT mener des exercices de simulation de réponse aux incidents au minimum deux fois par an, couvrant les principaux scénarios d'incidents. Les résultats des exercices DOIVENT être documentés, priorisés par risque et suivis comme actions d'amélioration conformément à PS-3.5.3 (Apprentissage et amélioration). Les lacunes critiques de capacité nécessitent une correction immédiate avec escalade à la direction générale.

**PS-3.1.6 Outils et technologie** : L'[Organisation] DOIT fournir aux équipes de réponse aux incidents des outils appropriés incluant : (1) un système de gestion des incidents avec suivi des flux de travail, (2) une capacité d'acquisition forensique, (3) un canal de communication sécurisé (chiffré), (4) l'accès aux systèmes de surveillance/journalisation conformément à A.8.15/A.8.16. L'adéquation des outils est évaluée annuellement dans ISMS-IMP-A.5.24-28.S1.

**Vérification** : Les procédures documentées, les enregistrements de formation, les rapports d'exercices et les capacités des outils sont vérifiés par l'évaluation ISMS-IMP-A.5.24-28.S1.

## Évaluation des événements et décision (A.5.25)

L'[Organisation] DOIT évaluer systématiquement tous les événements de sécurité afin de déterminer s'ils constituent des incidents nécessitant une réponse.

**PS-3.2.1 Exigence d'évaluation** : Tous les événements de sécurité détectés par la surveillance ou signalés par des utilisateurs DOIVENT être évalués pour déterminer s'ils constituent des incidents nécessitant une réponse. Les événements DOIVENT être priorisés pour évaluation sur la base : (1) des indicateurs de gravité automatisés issus des systèmes de surveillance (A.8.16), (2) de la criticité du système affecté conformément au registre des actifs (A.5.9), (3) de la source de l'événement (les alertes SOC sont prioritaires sur les signalements d'utilisateurs pour les événements en double). La méthodologie de priorisation des événements est détaillée dans ISMS-IMP-A.5.24-28.S2.

**PS-3.2.2 Classification de la gravité** : Tous les incidents confirmés DOIVENT se voir attribuer un niveau de gravité basé sur l'impact sur la confidentialité, l'intégrité et la disponibilité (CIA) en utilisant la Matrice de notation d'impact CIA définie dans ISMS-REF-A.5.24-28 Section 1. La notation tient compte de : le volume de données affectées, la criticité des systèmes (conformément au registre des actifs A.5.9), l'impact sur les processus métier, les seuils de notification réglementaire. Les incidents de gravité Critique et Élevée DOIVENT être notés indépendamment par deux analystes pour assurer la cohérence. La gravité d'un incident PEUT être reclassifiée si de nouvelles informations modifient l'évaluation de l'impact ; la reclassification vers Élevé/Critique nécessite l'approbation du Responsable de la réponse aux incidents, avec notifications rétroactives à la direction conformément à la Section 5.2.

**PS-3.2.3 Classification par catégorie** : Tous les incidents DOIVENT être catégorisés par type en utilisant la taxonomie organisationnelle des incidents, afin de permettre des procédures de réponse appropriées et une analyse des tendances.

**PS-3.2.4 Exigences d'escalade** : Les incidents DOIVENT être escaladés aux niveaux de management appropriés en fonction de leur gravité. Les incidents Critiques nécessitent une notification immédiate à la Direction générale.

**PS-3.2.5 Documentation** : Toutes les évaluations d'événements DOIVENT être documentées dans le système de gestion des incidents avec les champs obligatoires : (1) source de l'événement et horodatage de détection, (2) analyse de l'impact CIA avec notation, (3) niveau de gravité et justification de l'attribution, (4) catégorie d'incident conformément à la taxonomie, (5) actions d'escalade prises avec notifications envoyées, (6) nom et horodatage d'approbation de l'approbateur. Le système de gestion des incidents DOIT imposer la complétion des champs obligatoires avant que l'évaluation puisse être marquée comme terminée.

**Vérification** : L'exactitude des évaluations, la cohérence des classifications et la conformité aux escalades sont vérifiées par l'évaluation ISMS-IMP-A.5.24-28.S2.

## Opérations de réponse aux incidents (A.5.26)

L'[Organisation] DOIT répondre aux incidents confirmés conformément aux procédures documentées.

**PS-3.3.1 Exécution de la réponse** : Tous les incidents confirmés DOIVENT faire l'objet d'une réponse selon les procédures documentées appropriées à la gravité et à la catégorie de l'incident. Les procédures de réponse sont sélectionnées en fonction de la catégorie d'incident (PS-3.2.3), le niveau de gravité (PS-3.2.2) déterminant l'allocation des ressources et l'escalade. Les playbooks de réponse aux incidents sont maintenus dans ISMS-REF-A.5.24-28 Section 3 pour chaque catégorie principale :

- **Maliciel/Rançongiciel** : Isolation, imagerie forensique, analyse du maliciel, vérification de l'éradication
- **Accès non autorisé** : Révocation des identifiants, clôture des sessions, révision des journaux d'accès, évaluation de l'escalade de privilèges
- **Violation de données** : Évaluation du périmètre, analyse de notification réglementaire (RGPD/nLPD), identification des personnes affectées, préservation des preuves
- **Déni de service** : Analyse du trafic, activation des mesures d'atténuation (limitation du débit, filtrage en amont), priorisation de la restauration du service
- **Ingénierie sociale** : Notification des utilisateurs, réinitialisation des identifiants, renforcement de la sensibilisation, prévention d'attaques similaires
- **Menace interne** : Préservation des preuves (conservation légale), coordination RH, suspension des accès, détermination du périmètre de l'enquête
- **Sécurité physique** : Récupération des actifs, vérification du contrôle d'accès, révision de la surveillance, correction des contrôles physiques
- **Chaîne d'approvisionnement** : Notification du fournisseur, évaluation des dépendances, activation des mesures compensatoires, révision du contrat

Pour les incidents couvrant plusieurs catégories, la catégorie principale est déterminée par l'impact le plus significatif (la violation de données a la priorité sur le vecteur d'accès initial). La sélection du playbook est documentée dans le dossier d'incident avec justification. Les incidents hybrides ou inédits sans playbook existant suivent par défaut la procédure générale de réponse aux incidents avec les conseils du Responsable de la réponse aux incidents.

**PS-3.3.2 Confinement** : La réponse aux incidents DOIT prioriser le confinement pour limiter la portée et prévenir tout dommage supplémentaire. L'approche de confinement varie selon la gravité, avec un confinement agressif pour les incidents Critiques/Élevés. L'efficacité du confinement DOIT être vérifiée avant de passer à la phase d'éradication : (1) Aucun système supplémentaire ne présente d'indicateurs de compromission, (2) Le vecteur d'attaque est identifié et bloqué, (3) L'accès de l'acteur malveillant est résilié (révocation des identifiants, clôture de session confirmée), (4) La surveillance confirme l'absence de déplacement latéral pendant au minimum 1 heure (Critique/Élevé) ou 4 heures (Moyen). Pour les attaques sophistiquées en cours, le confinement peut être itératif avec l'approbation du Responsable de la réponse aux incidents pour continuer.

**PS-3.3.3 Éradication** : La cause racine des incidents DOIT être éliminée avant que les systèmes ne soient remis en production. Les actions d'éradication DOIVENT être vérifiées avant de procéder à la récupération.

**PS-3.3.4 Récupération** : Les systèmes et services affectés DOIVENT être restaurés aux opérations normales après vérification de sécurité. La récupération DOIT suivre les priorités de criticité métier alignées sur les exigences PCA/PRA. La priorité de récupération des systèmes est déterminée par les niveaux de criticité métier du registre des actifs (A.5.9) et les Objectifs de temps de récupération (RTO) des plans PCA/PRA (A.5.29-30). Niveaux de priorité : (1) Systèmes critiques (RTO < 4 heures) — récupération immédiate, (2) Haute priorité (RTO 4-24 heures) — le jour même, (3) Priorité moyenne (RTO 1-3 jours) — le jour ouvré suivant, (4) Priorité faible (RTO > 3 jours) — restauration planifiée. Le séquençage de la récupération tient compte des dépendances (restaurer l'infrastructure de support avant les applications dépendantes). Les priorités de récupération peuvent être remplacées par le Responsable de la réponse aux incidents avec l'approbation de la Direction générale lorsque le contexte de l'incident nécessite une dérogation.

**PS-3.3.5 Communication** : Les communications liées aux incidents DOIVENT suivre des protocoles documentés pour les parties prenantes internes, la direction, les utilisateurs et les parties externes (régulateurs, clients, forces de l'ordre) selon les besoins. Les protocoles de communication DOIVENT préciser :

- **Parties prenantes internes** : Équipe de réponse aux incidents (toutes gravités), propriétaires de l'unité métier affectée (Moyen+), Opérations IT (toutes gravités), Direction InfoSec (Élevé+), Direction générale (Critique)
- **Escalades à la direction** : Conformément à la matrice d'escalade de la Section 5.2 avec contenu défini (synthèse de l'incident, évaluation de l'impact, statut du confinement, délai de résolution estimé)
- **Communications aux utilisateurs** : Les utilisateurs affectés sont informés des impacts de service (Moyen+), avec mises à jour selon les intervalles SLA pour les incidents en cours
- **Parties externes** :
  - Régulateurs (notification de violation RGPD/nLPD conformément à l'art. 33/art. 24) — Juridique et DPD coordonnent
  - Clients (si leurs données sont affectées) — L'équipe de communication rédige, la Direction générale approuve
  - Forces de l'ordre (si activité criminelle suspectée) — Le conseil juridique décide et coordonne la remise
  - Tiers (si un incident fournisseur impacte l'[Organisation]) — La Gestion des fournisseurs coordonne conformément à A.5.22

Les modèles de communication pour chaque niveau de gravité et type de partie prenante sont maintenus dans ISMS-REF-A.5.24-28 Section 2 et dans le système de gestion des incidents. Toutes les communications liées aux incidents Critiques/Élevés nécessitent l'approbation du Responsable de la réponse aux incidents avant envoi.

**PS-3.3.6 Normes de temps de réponse** : L'[Organisation] DOIT définir et maintenir des normes de temps de réponse (SLA) par niveau de gravité conformément à la Section 5.1.1. La conformité aux SLA DOIT être mesurée mensuellement et rapportée dans les synthèses exécutives trimestrielles. Les SLA non respectés nécessitent une analyse des causes racines conformément à PS-3.5.2 (Revue post-incident) pour identifier les problèmes systémiques nécessitant correction.

**Vérification** : L'exécution de la réponse, la conformité aux SLA et l'efficacité des communications sont vérifiées par l'évaluation ISMS-IMP-A.5.24-28.S3.

## Collecte et préservation des preuves forensiques (A.5.28)

L'[Organisation] DOIT établir des procédures pour l'identification, la collecte, l'acquisition et la préservation des preuves forensiques.

**PS-3.4.1 Exigence de collecte des preuves** : Les preuves forensiques DOIVENT être collectées pour tous les incidents de gravité Critique et les incidents de gravité Élevée présentant des implications légales ou réglementaires potentielles.

**PS-3.4.2 Calendrier de collecte** : La collecte des preuves commence immédiatement lors de la détection de l'incident et s'effectue en parallèle des opérations de réponse. La préservation des preuves NE DOIT PAS être sacrifiée sauf lorsque le confinement des menaces actives est prioritaire.

**PS-3.4.3 Méthodes forensiquement saines** : Les preuves DOIVENT être collectées selon des méthodes forensiquement saines qui maintiennent leur intégrité et permettent leur potentielle admissibilité légale.

**PS-3.4.4 Chaîne de custody** : Toutes les preuves DOIVENT avoir une chaîne de custody documentée, depuis la collecte jusqu'à la destruction, incluant les transferts de custody, les lieux de stockage et les enregistrements d'accès.

**PS-3.4.5 Préservation des preuves** : Les preuves DOIVENT être préservées de manière sécurisée avec des contrôles d'accès, un chiffrement et une vérification de l'intégrité. Les durées de conservation DOIVENT être conformes aux exigences réglementaires et aux politiques de conservation de l'[Organisation].

**PS-3.4.6 Conservation légale** : L'[Organisation] DOIT mettre en œuvre des procédures de conservation légale lorsqu'une procédure judiciaire est engagée ou raisonnablement anticipée, suspendant les processus de suppression normaux pour les preuves pertinentes.

**Vérification** : Les procédures relatives aux preuves, la documentation de la chaîne de custody et les contrôles de préservation sont vérifiés par l'évaluation ISMS-IMP-A.5.24-28.S4.

## Apprentissage et amélioration post-incident (A.5.27)

L'[Organisation] DOIT tirer des enseignements des incidents et les traduire en améliorations des contrôles.

**PS-3.5.1 Exigence de revue post-incident** : Des revues post-incident (RPI) DOIVENT être conduites pour tous les incidents de gravité Critique et Élevée dans les délais définis. Les incidents de gravité Moyenne nécessitent une RPI lorsqu'ils révèlent de nouvelles techniques d'attaque ou des défaillances significatives de contrôle.

**PS-3.5.2 Analyse des causes racines** : Une analyse des causes racines DOIT être menée pour identifier les problèmes systémiques sous-jacents, et non uniquement les causes directes. Les résultats DOIVENT alimenter les mesures préventives.

**PS-3.5.3 Mise en œuvre des améliorations** : Les enseignements tirés DOIVENT être traduits en améliorations concrètes avec des responsables désignés et des dates cibles de réalisation. Les actions d'amélioration DOIVENT être suivies jusqu'à leur réalisation.

**PS-3.5.4 Gestion des connaissances** : L'[Organisation] DOIT maintenir un référentiel de retours d'expérience accessible au personnel de réponse aux incidents. Les playbooks de réponse DOIVENT être mis à jour sur la base des enseignements tirés.

**PS-3.5.5 Métriques et analyse tendancielle** : L'[Organisation] DOIT suivre les métriques des incidents (volume, gravité, temps de réponse, conformité aux SLA) et conduire une analyse trimestrielle des tendances pour identifier les problèmes systémiques.

**PS-3.5.6 Revue annuelle du programme** : Le programme de gestion des incidents DOIT faire l'objet d'une revue annuelle pour évaluer son efficacité, comparer ses résultats aux standards et mettre à jour les procédures, la formation et les outils.

**Vérification** : L'achèvement des RPI, le suivi des améliorations et le reporting des métriques sont vérifiés par l'évaluation ISMS-IMP-A.5.24-28.S5.

---

# Rôles et responsabilités

## Direction générale

- **Responsable** de l'efficacité globale du programme de gestion des incidents
- **Approuve** la politique de gestion des incidents et les modifications majeures des procédures
- **Décide** des actions critiques pour l'activité (arrêt de service, divulgation publique, engagement des forces de l'ordre)
- **Reçoit** les mises à jour de statut des incidents Critiques, les métriques trimestrielles, la revue annuelle du programme

## Responsable de la sécurité des systèmes d'information (RSSI)

- **Responsable** de la conformité à la politique de gestion des incidents et de la maturité du programme
- **Approuve** les procédures, accepte le risque résiduel, alloue le budget et les ressources
- **Décide** des escalades de réponse aux incidents Élevés/Critiques et de l'engagement externe
- **Reçoit** tous les rapports d'incidents, les rapports de RPI, les métriques hebdomadaires

## Responsable de la réponse aux incidents / Responsable CSIRT

- **Responsable** des opérations quotidiennes de réponse aux incidents et de la conformité aux SLA
- **Gère** l'évaluation des incidents, la coordination de la réponse, l'allocation des ressources, les communications, la formation
- **Approuve** la clôture des incidents, la planification des RPI, les mises à jour des procédures
- **Rend compte** au RSSI sur le statut des incidents, les métriques et la santé du programme

## Intervenants incidents / Analystes SOC

- **Responsables** du triage, de l'investigation, du confinement, de l'éradication, de la récupération et de la documentation des incidents
- **Exécutent** les procédures de réponse en fonction de la gravité et de la catégorie
- **Escaladent** les incidents conformément à la matrice d'escalade
- **Documentent** toutes les activités liées aux incidents dans le système de gestion des incidents

## Spécialistes forensiques

- **Responsables** de l'intégrité de la collecte des preuves et de la chaîne de custody
- **Exécutent** l'analyse forensique et la préservation des preuves
- **Coordonnent** avec le Juridique sur l'admissibilité des preuves et la conservation légale
- **Documentent** toutes les collectes de preuves et les transferts de custody

## Opérations IT

- **Responsables** de l'exécution des actions de confinement/éradication/récupération sur les systèmes
- **Coordonnent** la restauration des services avec l'équipe de réponse aux incidents
- **Fournissent** le support technique et l'accès aux systèmes pour l'investigation des incidents
- **Mettent en œuvre** les améliorations techniques des contrôles issues des recommandations des RPI

## Conseil juridique

- **Responsable** de l'atténuation des risques légaux et de la conformité réglementaire
- **Conseille** sur les implications légales, les exigences de notification réglementaire, la préservation des preuves
- **Coordonne** les notifications aux autorités réglementaires avec le DPD
- **Gère** les procédures de conservation légale et la liaison avec les forces de l'ordre

## Délégué à la protection des données (DPD)

- **Responsable** de la conformité à la protection de la vie privée et de l'évaluation des obligations de notification des violations
- **Évalue** les incidents au regard des exigences de notification de violation RGPD/nLPD
- **Coordonne** les notifications aux personnes concernées lorsque nécessaire
- **Conseille** sur les implications des incidents en matière de données personnelles

## Équipe de communication

- **Responsable** des communications externes et de la gestion de la réputation
- **Rédige** les communications destinées aux utilisateurs, clients et médias
- **Coordonne** la communication avec le Juridique et la Direction générale
- **Exécute** les communications externes approuvées

## Ensemble du personnel

- **Responsable** du signalement des incidents de sécurité suspectés conformément à ISMS-POL-A.6.8
- **Coopère** aux activités de réponse aux incidents sur demande
- **Complète** la formation à la sensibilisation à la sécurité incluant le signalement des incidents

---

# Cadre de gouvernance

## Cadre de gravité des incidents

L'[Organisation] DOIT définir des niveaux de gravité avec les exigences de réponse associées :

| Gravité | Définition | Exigence de réponse |
|---------|------------|---------------------|
| **Critique** | Impact métier significatif ; violation à grande échelle, rançongiciel affectant la production, compromission d'infrastructure critique, notification réglementaire déclenchée | Réponse immédiate, confinement agressif, notification de la Direction générale, RPI obligatoire |
| **Élevé** | Impact métier modéré ; attaque ciblée, accès aux données confirmé, compromission de système sensible, dégradation de service | Réponse urgente, notification du RSSI, RPI obligatoire |
| **Moyen** | Impact métier limité ; infection isolée, attaque infructueuse, violation mineure de politique | Réponse standard, supervision du chef d'équipe, RPI conditionnelle |
| **Faible** | Impact métier minimal ; attaque bloquée, anomalie mineure, événement informatif | Traitement standard, traitement par lots acceptable, aucune RPI requise |

## Normes de temps de réponse (SLA)

L'[Organisation] définit les normes de temps de réponse suivantes par niveau de gravité :

| Gravité | Réponse initiale | Cible de confinement | Cible de résolution | Mises à jour direction |
|---------|-----------------|---------------------|---------------------|------------------------|
| **Critique** | 15 minutes | 1 heure | 24 heures | En temps réel (toutes les heures) |
| **Élevé** | 1 heure | 4 heures | 72 heures | Quotidienne |
| **Moyen** | 4 heures | 24 heures | 5 jours ouvrés | Hebdomadaire (si en cours) |
| **Faible** | 8 heures | 48 heures | 10 jours ouvrés | Reporting par lots |

**Réponse initiale** : Délai depuis la confirmation de l'incident (évaluation PS-3.2.1 terminée) jusqu'à l'affectation de l'équipe de réponse et le déclenchement des actions de confinement.

**Cible de confinement** : Délai pour limiter la portée de l'incident et prévenir tout dommage supplémentaire. La cible est un objectif, non une garantie — les incidents complexes peuvent dépasser les cibles avec une justification documentée.

**Cible de résolution** : Délai pour terminer l'éradication et la récupération, avec retour aux opérations normales. Le compteur s'arrête lorsque l'incident est clôturé par le Responsable de la réponse aux incidents.

**Mises à jour direction** : Fréquence du reporting de statut à la direction conformément à la Section 5.3.

La conformité aux SLA est mesurée mensuellement et rapportée dans les synthèses exécutives trimestrielles. Les SLA non respectés nécessitent une analyse des causes racines conformément à PS-3.5.2 (Revue post-incident). Les cibles SLA sont révisées annuellement lors de la revue du programme (PS-3.5.6) et ajustées en fonction de la réalité opérationnelle et des benchmarks sectoriels.

Les procédures de mesure détaillées des SLA sont définies dans ISMS-IMP-A.5.24-28.S3.

## Exigences d'escalade

**Incidents Critiques** : Escalade immédiate au RSSI et à la Direction générale
**Incidents Élevés** : Escalade au Responsable de la réponse aux incidents (immédiate), au RSSI (dans le délai défini)
**Incidents Moyens/Faibles** : Supervision du chef d'équipe ; escalader si la gravité augmente ou si la résolution est bloquée

La fréquence des notifications à la direction et les exigences de contenu sont définies dans ISMS-IMP-A.5.24-28.S3.

## Exigences de reporting

**Reporting opérationnel** :

- Incidents Critiques : Mises à jour de statut en temps réel à la Direction générale
- Incidents Élevés : Mises à jour quotidiennes au RSSI
- Tous les incidents : Synthèse hebdomadaire au RSSI

**Reporting exécutif** :

- Synthèse trimestrielle des incidents à la Direction générale (volume, tendances, métriques, enseignements)
- Revue annuelle du programme de gestion des incidents à la Direction générale

## Intégration avec les contrôles connexes

La présente politique s'intègre avec :

| Contrôle | Point d'intégration |
|----------|---------------------|
| **A.8.16 (Surveillance)** | La surveillance détecte les événements qui alimentent l'évaluation des incidents |
| **A.8.15 (Journalisation)** | Les journaux fournissent des preuves pour l'investigation et la forensique |
| **A.6.8 (Signalement d'événements)** | Les signalements des utilisateurs alimentent le processus d'évaluation des incidents |
| **A.5.29-30 (PCA/PRA)** | Les incidents majeurs peuvent déclencher l'activation du PCA/PRA |
| **A.5.31 (Légal/Réglementaire)** | Les exigences de notification réglementaire sont intégrées |
| **A.5.19-23 (Tiers)** | Les incidents de tiers sont signalés et coordonnés |

## Révision de la politique

- **Fréquence** : Annuelle au minimum
- **Déclencheurs** : Incident majeur révélant une lacune de politique, changements réglementaires, résultats d'audit, changements organisationnels
- **Réviseurs** : RSSI (propriétaire), Responsable de la réponse aux incidents (contributeur), Juridique (conformité)
- **Approbation** : RSSI (technique), Direction générale (stratégique)

Les procédures de mise en œuvre et les documents de référence peuvent être mis à jour sans révision de la politique lorsque les changements n'affectent pas les déclarations de politique.

---

# Conformité et exceptions

## Exigences de conformité

Tout le personnel DOIT se conformer à la présente politique. La conformité est surveillée par :

- Les enregistrements et métriques du système de gestion des incidents
- Le suivi de la complétion des formations
- Les taux d'achèvement des RPI
- La participation aux exercices
- L'achèvement des actions d'amélioration

## Gestion des exceptions

Les exceptions à la présente politique nécessitent :

- Une demande d'exception écrite avec justification métier
- Une évaluation des risques de l'exception
- Des mesures compensatoires (le cas échéant)
- L'approbation du RSSI (minimum) ; approbation de la Direction générale pour les exceptions aux contrôles Critiques
- Une durée limitée (maximum 12 mois, renouvellement requis)
- Une documentation dans le registre des exceptions SMSI

Les exceptions sont révisées annuellement pour vérifier leur validité continue.

## Non-conformité

La non-conformité à la présente politique peut entraîner :

- Une escalade à la direction
- Une surveillance accrue lors des audits
- Des mesures disciplinaires conformément aux politiques RH
- Des constats réglementaires lors des audits de certification

---

# Documents connexes

## Guides de mise en œuvre

| Document | Objet |
|----------|-------|
| **ISMS-IMP-A.5.24-28.S1-UG/TG** | Évaluation du cadre de gestion des incidents (gouvernance, structure, procédures, formation, outils) |
| **ISMS-IMP-A.5.24-28.S2-UG/TG** | Évaluation de la détection et classification des événements (procédures d'évaluation, exactitude des classifications, escalade) |
| **ISMS-IMP-A.5.24-28.S3-UG/TG** | Évaluation des capacités de réponse aux incidents (procédures, SLA, playbooks, communications) |
| **ISMS-IMP-A.5.24-28.S4-UG/TG** | Évaluation de la gestion des preuves forensiques (procédures, chaîne de custody, préservation) |
| **ISMS-IMP-A.5.24-28.S5-UG/TG** | Évaluation de l'apprentissage et de l'amélioration continue (RPI, analyse des causes racines, suivi des améliorations, métriques) |

## Documents de référence

| Document | Objet |
|----------|-------|
| **ISMS-REF-A.5.24-28 Section 1** | Taxonomie de classification des incidents (catégories, sous-catégories, indicateurs de gravité) |
| **ISMS-REF-A.5.24-28 Section 2** | Référence rapide des notifications réglementaires (RGPD, nLPD, exigences sectorielles) |
| **ISMS-REF-A.5.24-28 Section 3** | Bibliothèque des techniques de collecte forensique (procédures techniques, outils, modèles) |

## Politiques connexes

- ISMS-POL-00 (Cadre d'applicabilité réglementaire)
- ISMS-POL-A.8.15 (Journalisation)
- ISMS-POL-A.8.16 (Activités de surveillance)
- ISMS-POL-A.6.8 (Signalement des événements de sécurité de l'information)
- ISMS-POL-A.5.29-30 (Continuité d'activité et reprise après sinistre)
- ISMS-POL-A.5.31 (Exigences légales, réglementaires et contractuelles)
- ISMS-POL-A.5.19-23 (Gestion des tiers)

## Normes externes

- ISO/IEC 27001:2022 — Contrôles A.5.24, A.5.25, A.5.26, A.5.27, A.5.28
- ISO/IEC 27002:2022 — Lignes directrices de mise en œuvre pour les contrôles de gestion des incidents
- NIST SP 800-61 Rév. 2 — Guide de gestion des incidents de sécurité informatique
- ISO/IEC 27035 — Gestion des incidents de sécurité de l'information

---

# Définitions

**Événement de sécurité de l'information** : Occurrence identifiée indiquant une possible violation de la politique de sécurité de l'information ou une défaillance des mesures de protection. Les événements peuvent ou non devenir des incidents après évaluation.

**Incident de sécurité de l'information** : Événement de sécurité de l'information indésirable ou inattendu, présentant une probabilité significative de compromettre les opérations métier et de menacer la sécurité de l'information. Les incidents nécessitent des actions de réponse.

**CSIRT (équipe de réponse aux incidents de sécurité informatique)** : Équipe organisationnelle chargée de recevoir, réviser et répondre aux incidents de sécurité de l'information.

**SOC (centre des opérations de sécurité)** : Équipe ou fonction responsable de la surveillance, de la détection, de l'analyse et de la réponse aux événements et incidents de sécurité.

**Revue post-incident (RPI)** : Révision structurée conduite après la clôture d'un incident pour documenter la chronologie, évaluer l'efficacité de la réponse, identifier les enseignements et recommander des améliorations.

**Analyse des causes racines (ACR)** : Investigation systématique pour identifier la ou les cause(s) fondamentale(s) ayant permis à l'incident de se produire.

**Chaîne de custody** : Piste documentée indiquant qui a collecté les preuves, quand, où, comment et chaque transfert de preuves entre parties.

**Conservation légale** : Directive de préserver toutes les preuves potentiellement pertinentes liées à des procédures judiciaires engagées ou raisonnablement anticipées.

---

# Preuves pour cette politique

**Preuves de l'Étape 1 (Revue documentaire) :**

Preuves requises pour démontrer que cette politique est adéquatement documentée et approuvée :

- ✅ Ce document de politique (ISMS-POL-A.5.24-28 v1.0)
- ✅ Signatures d'approbation du RSSI, du DSI, de la Direction générale
- ✅ Exigences de capacité de gestion des incidents définies (Section 3.1 — PS-3.1.1 à PS-3.1.6)
- ✅ Cadre d'évaluation et de classification des événements documenté (Section 3.2 — PS-3.2.1 à PS-3.2.5)
- ✅ Procédures d'opérations de réponse aux incidents spécifiées (Section 3.3 — PS-3.3.1 à PS-3.3.6)
- ✅ Exigences relatives aux preuves forensiques documentées (Section 3.4 — PS-3.4.1 à PS-3.4.6)
- ✅ Exigences d'apprentissage post-incident spécifiées (Section 3.5 — PS-3.5.1 à PS-3.5.6)
- ✅ Cadre de gravité des incidents défini (Section 5.1)
- ✅ Exigences d'escalade documentées (Section 5.2)
- ✅ Rôles et responsabilités assignés (Section 4)
- ✅ Gouvernance et procédures d'exception définies (Section 6)
- ✅ Intégration avec les contrôles connexes documentée (Section 5.4)

**Preuves de l'Étape 2 (Efficacité opérationnelle) :**

Preuves requises pour démontrer que cette politique est opérationnellement efficace :

- Registre des incidents montrant tous les incidents enregistrés avec classification (gravité, catégorie)
- Chronologies de réponse aux incidents démontrant la conformité aux SLA (détection → confinement → résolution)
- Enregistrements d'escalade montrant les notifications appropriées à la direction par gravité
- Enregistrements de personnel CSIRT/SOC et vérification des compétences
- Enregistrements de complétion des formations pour le personnel de réponse aux incidents
- Rapports d'exercices de simulation (au minimum deux fois par an)
- Rapports de revue post-incident (RPI) pour tous les incidents Critiques/Élevés
- Documentation d'analyse des causes racines avec recommandations d'amélioration
- Mises à jour du référentiel de retours d'expérience
- Suivi des actions d'amélioration jusqu'à réalisation
- Documentation de la chaîne de custody des preuves forensiques
- Enregistrements de préservation et de vérification d'intégrité des preuves
- Enregistrements de notifications réglementaires (72 heures RGPD, « dès que possible » nLPD)
- Tableaux de bord des métriques d'incidents (volume, gravité, MTTR, conformité SLA)
- Rapports d'analyse trimestrielle des tendances
- Documentation de la revue annuelle du programme
- Sorties des classeurs d'évaluation ISMS-IMP-A.5.24-28.S1-S5

**Lieux de stockage des preuves** :

| Type de preuve | Lieu de stockage |
|----------------|-----------------|
| Enregistrements de formation | Système d'information RH / Système de gestion de l'apprentissage |
| Rapports d'exercices | Système de gestion des incidents / Référentiel documentaire |
| Inventaire des outils | Base de données de gestion de la configuration (CMDB) |
| Procédures | Système de gestion documentaire |
| Évaluations de compétences | Dossiers responsables dans le SIRH |
| Enregistrements d'incidents | Système de gestion des incidents |
| Rapports RPI | Système de gestion des incidents / SharePoint |
| Rapports de conformité SLA | Tableau de bord décisionnel |

## Précision sur les preuves de conformité

La présente politique établit le cadre de gouvernance de la gestion des incidents (exigences de planification, d'évaluation, de réponse, de preuves, d'apprentissage). Elle N'ÉTABLIT PAS :

- **Les contrôles techniques de détection** (traités dans A.8.16 Activités de surveillance — la surveillance fournit des flux d'événements à l'évaluation des incidents)
- **Les exigences d'infrastructure de journalisation** (traitées dans A.8.15 Journalisation — les journaux fournissent des preuves pour les investigations)
- **Les procédures de continuité d'activité** (traitées dans A.5.29-30 PCA/PRA — les incidents majeurs peuvent déclencher l'activation du PCA/PRA)
- **Les procédures de signalement d'événements par les utilisateurs** (traitées dans A.6.8 Signalement des événements de sécurité — les signalements alimentent l'évaluation)
- **Les playbooks spécifiques de réponse aux incidents** (détails opérationnels dans ISMS-IMP-A.5.24-28 et ISMS-REF-A.5.24-28)

La délimitation est la suivante : POL-A.5.24-28 définit QUELLES capacités de gestion des incidents sont requises et QUAND les actions doivent avoir lieu → ISMS-IMP-A.5.24-28.S1-S5 décrit COMMENT évaluer la maturité des capacités → ISMS-REF-A.5.24-28 fournit les matériaux de référence techniques → Les contrôles connexes (A.8.15, A.8.16, A.6.8, A.5.29-30) fournissent les capacités de support.

---

# Enregistrement des approbations

| Rôle | Nom | Date | Signature |
|------|-----|------|-----------|
| **Propriétaire du document (RSSI)** | [Nom] | [Date] | [Signature] |
| **Revue technique (Responsable de la réponse aux incidents)** | [Nom] | [Date] | [Signature] |
| **Revue technique (DSI)** | [Nom] | [Date] | [Signature] |
| **Revue juridique (Conseil juridique)** | [Nom] | [Date] | [Signature] |
| **Revue vie privée (DPD)** | [Nom] | [Date] | [Signature] |
| **Approbation finale (Direction générale)** | [Nom] | [Date] | [Signature] |

---

**FIN DU DOCUMENT DE POLITIQUE**

---

*La présente politique établit les exigences de gestion des incidents de sécurité de l'information couvrant le cycle de vie complet (A.5.24-28). Les procédures de mise en œuvre sont documentées dans ISMS-IMP-A.5.24-28 (UG/TG).S1 à S5.*
<!-- QA_VERIFIED: 2026-03-30 -->
