<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.8.32-FR:operational:OP-POL:a.8.32 -->
**ISMS-OP-POL-A.8.32 — Gestion des changements**

---

**Contrôle documentaire**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Gestion des changements |
| **Type de document** | Politique opérationnelle |
| **Identifiant du document** | ISMS-OP-POL-A.8.32 |
| **Créateur du document** | Responsable de la sécurité de l'information (RSSI) |
| **Propriétaire du document** | Directeur général (PDG) |
| **Approuvé par** | Direction générale |
| **Date de création** | [Date] |
| **Version** | 1.0 |
| **Date de version** | [À déterminer] |
| **Classification** | Usage interne |
| **Statut** | Brouillon |

**Historique des versions** :

| Version | Date | Auteur | Modifications |
|---------|------|--------|---------------|
| 1.0 | [Date] | RSSI | Politique opérationnelle initiale pour ISO 27001:2022 |

**Cycle de révision** : Annuel
**Prochaine révision** : [Date d'entrée en vigueur + 12 mois]

**Approuvé par** : [RSSI / Direction générale]

**Documents connexes** :

- ISO/IEC 27001:2022 Contrôle A.8.32 — Gestion des changements

**Contrôles Annexe A connexes** :

| Contrôle | Relation avec la gestion des changements |
|----------|------------------------------------------|
| A.5.9 Inventaire des informations et autres actifs associés | L'inventaire des actifs définit le périmètre des changements et l'évaluation des impacts |
| A.5.24–28 Gestion des incidents | Les changements échoués peuvent déclencher la réponse aux incidents |
| A.5.37 Procédures d'exploitation documentées | Les procédures sont mises à jour suite aux modifications des systèmes |
| A.8.8 Gestion des vulnérabilités techniques | Le déploiement des correctifs suit le processus de gestion des changements |
| A.8.9 Gestion de la configuration | Les référentiels de configuration sont mis à jour après les changements |
| A.8.19 Installation de logiciels sur les systèmes en production | Les installations de logiciels suivent la gestion des changements |
| A.8.25–29 Cycle de développement sécurisé | Les changements de développement suivent la gestion des changements |
| A.8.31 Séparation des environnements | La promotion entre environnements est contrôlée via le processus de changement |
| A.8.33 Informations de test | Les données de test sont protégées durant les tests de changement |

**Politiques internes connexes** :

- Politique de gestion des actifs
- Politique de gestion des incidents
- Politique de procédures d'exploitation documentées
- Politique de sécurité des postes de travail (gestion des correctifs)
- Politique de sécurité réseau

---

# Politique de gestion des changements

## Objectif

La présente politique a pour objectif de gérer le risque posé par les modifications apportées aux systèmes de traitement de l'information, aux applications, aux infrastructures et aux technologies de support, en veillant à ce que les changements soient planifiés, évalués, approuvés, testés, mis en œuvre et documentés de manière contrôlée.

Cette politique soutient la nLPD suisse (revLPD) et l'Ordonnance sur la protection des données (OPDo) en mettant en œuvre des mesures techniques et organisationnelles proportionnées au risque, garantissant que les changements apportés aux systèmes traitant des données personnelles ne compromettent pas les garanties de protection des données. Lorsque l'organisation traite des données de personnes résidant dans l'UE/EEE, les exigences du RGPD s'appliquent également.

## Champ d'application

Tous les employés et utilisateurs tiers.

Tous les changements apportés aux systèmes de traitement de l'information, aux applications, aux infrastructures, aux équipements réseau, aux services cloud et aux systèmes de support, quel que soit le modèle de déploiement (sur site, cloud, hybride).

Cela inclut les changements matériels, les changements logiciels, les changements de configuration, les changements d'infrastructure, les changements de schéma de base de données et les changements des systèmes de sécurité.

**Hors champ d'application** : Mises à jour du contenu de sites web (textes, images), actions en libre-service des utilisateurs (réinitialisations de mots de passe via le portail approuvé), opérations automatisées de routine (sauvegardes planifiées, rotation des journaux), et changements gérés entièrement par les fournisseurs SaaS en dehors du contrôle client.

## Principe

Tous les changements apportés aux systèmes de traitement de l'information doivent être soumis à des procédures formelles de gestion des changements. Les changements doivent être planifiés, évalués pour leur impact et leur risque, autorisés, testés, communiqués, mis en œuvre de manière contrôlée et documentés. Les changements d'urgence doivent suivre des procédures accélérées tout en maintenant le contrôle et la supervision.

---

## Définitions

| Terme | Définition |
|-------|------------|
| **Changement** | Toute addition, modification ou suppression de composants d'un système d'information (matériel, logiciel, configuration, données) pouvant affecter la sécurité de l'information ou la disponibilité du système |
| **Changement standard** | Changement pré-approuvé, à faible risque et de routine, suivant une procédure documentée du Catalogue des changements standards |
| **Changement normal** | Changement nécessitant une évaluation complète, une révision par le CAB et un workflow d'approbation standard |
| **Changement d'urgence** | Changement nécessitant une mise en œuvre accélérée pour résoudre un incident critique, une vulnérabilité active ou prévenir un impact métier significatif |
| **Comité consultatif des changements (CAB)** | Groupe multidisciplinaire assurant la révision experte, l'évaluation des impacts et les recommandations pour les changements |
| **Revue post-implémentation (RPI)** | Revue structurée après la mise en œuvre d'un changement, vérifiant que les objectifs ont été atteints et capitalisant les enseignements |
| **Changement échoué** | Changement qui est annulé en raison d'un échec à atteindre les objectifs, d'une dégradation de performance inacceptable, de l'introduction d'une vulnérabilité de sécurité, ou d'une atteinte à des fonctions métier critiques. Un changement nécessitant des correctifs post-implémentation n'est pas nécessairement « échoué » si le changement initial n'a pas été annulé |

---

## Classification des changements

Tous les changements doivent être classifiés dans l'une des trois catégories suivantes :

| Type | Niveau de risque | Approbation | Révision CAB | Tests |
|------|-----------------|-------------|--------------|-------|
| **Standard** | Faible | Pré-approuvé (catalogue) | Non requise | Selon la procédure du catalogue |
| **Normal** | Moyen–Élevé | Propriétaire du service / CAB / RSSI (selon le risque) | Requise pour les risques élevés | Tests hors production requis |
| **Urgence** | Critique | RSSI ou Responsable des opérations informatiques | Rétrospective (dans les 48 heures) | Proportionné au risque (peut être abrégé) |

Les changements relevant de zones grises doivent être escaladés au Responsable des changements pour classification.

---

## Processus de demande de changement

### Soumission de la demande de changement

Tous les changements dans le périmètre doivent être soumis comme demandes de changement formelles dans le système de gestion des changements : **[Préciser : ServiceNow, Jira Service Management, Azure DevOps, ou « En cours de sélection ; en attendant : système de tickets/tableur »]**.

**Accès au système** : La soumission de changements est ouverte à tout le personnel informatique ; l'approbation des changements et la coordination du CAB sont réservées au personnel autorisé.

**Format de l'identifiant de changement** : [Préciser : CHG-AAAAMMJJ-### ou généré automatiquement par le système].

Chaque demande de changement doit inclure, au minimum :

| Champ | Description |
|-------|-------------|
| Identifiant du changement | Identifiant unique attribué par le système |
| Description | Ce qui est modifié et pourquoi |
| Justification métier | Raison du changement |
| Systèmes affectés | Actifs, services et dépendances impactés |
| Classification du risque | Faible / Moyen / Élevé / Critique |
| Plan de mise en œuvre | Procédure étape par étape |
| Fenêtre de mise en œuvre | Date, heure et durée proposées |
| Plan de retour arrière | Comment annuler le changement en cas d'échec |
| Approche de test | Quels tests seront effectués |
| Demandeur et responsable de mise en œuvre | Qui a demandé et qui exécutera |
| Plan de communication | Qui doit être informé |

### Évaluation de l'impact et du risque

Tous les changements doivent être évalués pour leur impact avant mise en œuvre :

- **Impact technique** : Systèmes affectés, dépendances, points d'intégration.
- **Impact métier** : Services affectés, impact sur les utilisateurs, perturbation des opérations métier.
- **Impact sécurité** : Risques de confidentialité, d'intégrité et de disponibilité. Les changements affectant des systèmes traitant des données personnelles doivent inclure une évaluation de l'impact sur la protection des données.
- **Impact conformité** : Obligations réglementaires, contrôles d'audit.
- **Niveau de risque** : Combinaison de la probabilité d'échec et de l'ampleur de l'impact.

### Workflow d'approbation

L'autorité d'approbation est déterminée par le niveau de risque du changement :

| Niveau de risque | Autorité d'approbation |
|-----------------|------------------------|
| **Faible** (changement standard) | Pré-approuvé via le Catalogue des changements standards |
| **Moyen** | Propriétaire du service ou Responsable d'équipe |
| **Élevé** | Responsable des opérations informatiques et RSSI |
| **Critique** | Direction générale |

---

## Comité consultatif des changements (CAB)

L'organisation doit établir un Comité consultatif des changements pour la révision des changements normaux et d'urgence.

### Composition du CAB

| Rôle | Responsabilité |
|------|----------------|
| **Responsable des changements** (Président) | Propriété du processus, planification, métriques, amélioration continue |
| **Représentant des opérations informatiques** | Faisabilité technique, impact sur l'infrastructure |
| **Représentant sécurité** | Évaluation des risques de sécurité, impact conformité |
| **Propriétaires d'applications métier** | Évaluation de l'impact métier (pour les changements pertinents) |
| **Experts thématiques** | Expertise technique selon les besoins |

### Fonctionnement du CAB

- **Réunions régulières** : **[Préciser : Chaque semaine le [jour] à [heure] CET]** (ou selon le volume de changements).
- **Format des réunions** : [En présentiel / virtuel / hybride].
- **Ordre du jour publié** : 24 heures avant la réunion (demandes de changement soumises avant le [jour précédent] 17h00 pour le CAB du [jour de réunion]).
- **CAB d'urgence** : Convoqué selon les besoins pour les changements urgents via [e-mail/Teams/Slack] ; peut procéder avec un quorum réduit (Responsable des changements + un membre supplémentaire), avec une réunion CAB rétrospective complète dans les **48 heures**.
- **Quorum** : Responsable des changements, représentant des opérations informatiques, représentant sécurité, et au moins un membre supplémentaire.
- **Comptes rendus** : Des procès-verbaux doivent être tenus pour toutes les réunions du CAB, documentant la date, les participants, les changements examinés, les décisions, les justifications et les actions à entreprendre. Les procès-verbaux sont conservés **3 ans**.

---

## Catalogue des changements standards

L'organisation doit maintenir un Catalogue des changements standards contenant les changements pré-approuvés, à faible risque et de routine.

### Exigences du catalogue

Chaque entrée du catalogue doit inclure :

- Description et périmètre du changement.
- Conditions préalables et prérequis.
- Procédure étape par étape.
- Durée estimée.
- Procédure de retour arrière (le cas échéant).
- Évaluation du risque (effectuée une seule fois lors de l'approbation au catalogue).

### Gouvernance du catalogue

- Catalogue révisé **trimestriellement** par le Responsable des changements avec la contribution du CAB.
- Nouvelles entrées ajoutées à partir de changements normaux réussis qui sont répétables et à faible risque.
- Entrées supprimées ou reclassifiées après tout échec d'un changement standard.
- Taux de réussite cible : **> 95 %** pour les changements standards.

Les changements standards doivent toujours être journalisés dans le système de gestion des changements pour la piste d'audit et la corrélation des incidents, même si la révision CAB n'est pas requise.

### Exemples du Catalogue des changements standards

Les changements standards pré-approuvés typiques incluent :

| Changement | Référence de procédure | Durée estimée | Prérequis |
|------------|------------------------|---------------|-----------|
| Ajout d'un utilisateur à un groupe Active Directory | IT-SOP-001 | 5 minutes | Ticket de demande d'accès approuvé |
| Redémarrage d'un serveur applicatif (hors production) | IT-SOP-015 | 10 minutes | Notification au propriétaire du service |
| Renouvellement de certificat SSL | IT-SOP-023 | 30 minutes | Nouveau certificat obtenu, sauvegarde de l'ancien cert |
| Ajout d'un enregistrement DNS (domaine interne) | IT-SOP-031 | 10 minutes | Formulaire de demande de modification DNS complété |
| Règle de pare-feu pour une application approuvée | IT-SOP-045 | 15 minutes | Pré-approbation de l'équipe sécurité, règle documentée |

**Ne constituent pas des changements standards** : modifications du schéma de base de données, mises à niveau du système d'exploitation, modifications de la topologie réseau, nouvelles installations logicielles, modifications de la configuration de sécurité affectant la production.

---

## Tests et validation

### Exigences de test

Les changements doivent être testés avant le déploiement en production :

| Risque du changement | Tests requis |
|---------------------|-------------|
| **Faible** (Standard) | Selon la procédure du catalogue ; vérification par le responsable de mise en œuvre |
| **Moyen** | Tests fonctionnels et tests d'intégration en environnement hors production |
| **Élevé** | Tests fonctionnels, d'intégration, de performance et d'acceptation utilisateur |
| **Critique** | Suite de tests complète incluant tests de sécurité et validation de la reprise après sinistre |

### Séparation des environnements

- Les changements doivent être testés dans des environnements hors production (développement, test/AQ, staging) avant le déploiement en production.
- Les environnements hors production doivent être logiquement ou physiquement séparés de la production, avec des identifiants et des contrôles d'accès distincts.
- Les données de production ne doivent pas être utilisées dans les environnements de test sans masquage ou anonymisation conformément à la Politique de classification et de traitement des données.
- La promotion du test vers la production nécessite une validation formelle et des résultats de test vérifiés.

### Protection de l'environnement de production

Les changements en production ne doivent être exécutés que par du personnel autorisé, avec les contrôles suivants :

- **Séparation des tâches** : Les développeurs ne doivent pas déployer leurs propres changements en production sans révision indépendante et approbation d'un responsable de mise en production désigné, d'un membre de l'équipe des opérations ou du CAB.
- **Révision par les pairs** : Les changements de code nécessitent une révision et une approbation par les pairs avant le déploiement en production (via une demande de fusion ou mécanisme équivalent).
- L'**authentification multifacteur (AMF)** doit être requise pour l'accès à la production.
- **Gestion des accès privilégiés** : Les comptes de déploiement en production doivent être distincts des comptes de développement.
- **Tous les changements en production doivent être journalisés** avec l'identité de l'utilisateur, l'horodatage et le contenu du changement.

**Exception** : Dans les organisations de moins de 5 membres du personnel informatique où la séparation complète n'est pas réalisable, les contrôles compensatoires doivent inclure une journalisation renforcée, une révision mensuelle par le RSSI de tous les changements en production, et une révision par les pairs post-implémentation.

---

## Mise en œuvre et retour arrière

### Mise en œuvre contrôlée

Les changements doivent être mis en œuvre conformément au plan de mise en œuvre approuvé, avec :

- Vérification des prérequis et dépendances avant le démarrage.
- Exécution des étapes documentées.
- Surveillance en temps réel lors de la mise en œuvre.
- Tests de vérification post-implémentation.
- Documentation des étapes réellement effectuées et de tout écart.

### Fenêtres de maintenance

L'organisation doit établir des fenêtres de changement préférentielles pour minimiser les perturbations métier :

**Fenêtres de changement préférentielles** :
- **Fenêtre standard** : [Préciser : ex. mardis et jeudis de 20h00 à 23h00 CET]
- **Fenêtre étendue** : [Préciser : ex. samedi de 08h00 à 16h00 CET]
- **Urgence** : À tout moment avec approbation du RSSI

**Périodes restreintes** (aucun changement non urgent) :
- [Propre à l'activité : ex. « Première semaine de chaque mois (clôture financière) », « 15 décembre–5 janvier (gel de fin d'année) »]
- Jours fériés : jours fériés fédéraux suisses
- Événements métier majeurs : documentés dans le calendrier des changements 90 jours à l'avance

Les changements en dehors des fenêtres préférentielles nécessitent l'autorité d'approbation pour les risques **élevés** (Responsable des opérations informatiques + RSSI), quel que soit le niveau de risque technique.

### Retour arrière

Une procédure de retour arrière doit être convenue avant la mise en œuvre de changements dans les systèmes de production. Le retour arrière doit être exécuté lorsque :

- Le changement n'atteint pas ses objectifs.
- Une dégradation de performance inacceptable survient.
- Une vulnérabilité de sécurité est introduite.
- Des fonctions métier critiques sont compromises.

Autorité de décision pour le retour arrière : même autorité d'approbation que pour le changement initial (ou niveau supérieur pour le retour arrière d'urgence).

### Test du retour arrière

Pour les changements à risque **élevé** et **critique**, les procédures de retour arrière doivent être :

- Documentées et approuvées dans le cadre de la demande de changement.
- **Testées hors production** avant la mise en œuvre en production (dans la mesure du possible).
- Vérifiées comme exécutables dans la fenêtre de retour arrière définie.

Le test du retour arrière doit vérifier :

- Les étapes de la procédure de retour arrière sont exactes et complètes.
- Le retour arrière peut être effectué dans la fenêtre de changement.
- L'intégrité des données est maintenue lors du retour arrière.
- La restauration du service est confirmée.

Lorsque le test du retour arrière n'est pas réalisable (migrations à sens unique, changements destructifs), un plan de **correction en avant** doit être documenté comme alternative au retour arrière.

---

## Communication

### Notification des parties prenantes

Les parties prenantes affectées doivent être notifiées des changements, incluant :

- Le calendrier et la programmation du changement.
- L'impact attendu sur le service (durée, portée).
- Les actions requises des utilisateurs (le cas échéant).
- Les coordonnées du support pendant le changement.

**Changements planifiés** : Notification préalable minimale selon les exigences organisationnelles (recommandé : 5 jours ouvrables pour les impacts élevés, 2 jours ouvrables pour les impacts moyens).

**Changements d'urgence** : Communication dès que possible en toute sécurité.

**Achèvement du changement** : Confirmation envoyée aux parties prenantes à la fin du changement.

---

## Changements d'urgence

### Critères de classification en urgence

Les changements ne doivent être classifiés comme urgence que lorsque :

- Résolution d'un incident de sécurité actif ou d'une vulnérabilité activement exploitée.
- Restauration d'une panne de service critique.
- Prévention d'une défaillance imminente du système.
- Réponse à une exigence réglementaire urgente.
- Atténuation d'une violation de données active.

La classification en urgence **ne doit pas** être utilisée par commodité, en raison d'une mauvaise planification, pour du travail de routine ou des fonctionnalités souhaitées.

### Processus de changement d'urgence

1. Justification de l'urgence documentée (même brièvement).
2. Approbation du RSSI ou du Responsable des opérations informatiques (au minimum).
3. Tests proportionnés au risque (cas de test abrégés, ou acceptation documentée du risque si les tests ne sont pas réalisables).
4. Mise en œuvre avec surveillance renforcée.
5. Plan de retour arrière en place avant l'exécution.
6. Révision rétrospective par le CAB dans les **48 heures**.
7. Revue post-implémentation obligatoire dans les **5 jours ouvrables**.

### Surveillance des changements d'urgence

Le pourcentage de changements d'urgence doit être suivi mensuellement. Cible : **< 5 %** de l'ensemble des changements.

Lorsque les changements d'urgence dépassent 5 % pendant deux mois consécutifs :

1. Analyse des causes racines effectuée par le Responsable des changements dans les **14 jours**.
2. Résultats présentés au CAB et au RSSI.
3. Actions correctives mises en œuvre dans les **30 jours**, pouvant inclure : formation supplémentaire sur la classification des changements, améliorations de processus (ex. : workflows d'approbation plus rapides pour les changements urgents mais non d'urgence), ajustements des ressources, ou mesures disciplinaires en cas d'abus de la classification d'urgence.
4. Revue de suivi après **60 jours** pour vérifier l'efficacité.

**Abus de la classification d'urgence** : L'utilisation inappropriée de la classification d'urgence (commodité, mauvaise planification) constitue une violation de la politique et doit être escaladée au RSSI.

---

## Revue post-implémentation (RPI)

Des revues post-implémentation doivent être conduites pour :

- **Tous les changements d'urgence** (obligatoire).
- **Tous les changements échoués** (obligatoire).
- **Les changements normaux classifiés à risque élevé ou critique**.

### Contenu de la RPI

- Objectifs atteints vs. résultats planifiés.
- Problèmes rencontrés lors de la mise en œuvre.
- Efficacité de la planification et des tests.
- Retour des utilisateurs et impact sur le service.
- Enseignements tirés et opportunités d'amélioration.
- Si le changement doit être ajouté au Catalogue des changements standards.

### Calendrier de la RPI

- Changements d'urgence : dans les **5 jours ouvrables**.
- Changements échoués : dans les **5 jours ouvrables**.
- Changements normaux à risque élevé : dans les **14 jours ouvrables**.

---

## Périodes de gel des changements

À des moments critiques de l'année, l'organisation peut imposer une période de gel des changements pendant laquelle seuls les changements d'urgence sont autorisés.

Les périodes de gel des changements doivent être :

- Approuvées par la direction générale ou le RSSI.
- Communiquées à toutes les parties prenantes à l'avance (minimum 2 semaines).
- Documentées dans le calendrier des changements.
- Exemples : clôture financière de fin d'année, lancements majeurs de produits, périodes d'activité intense, périodes de soumission réglementaire.

---

## Gestion des enregistrements et documentation

### Enregistrements des changements

Des enregistrements complets des changements doivent être tenus, incluant :

- Toutes les informations de la demande de changement.
- Enregistrements d'approbation avec horodatages et approbateurs.
- Notes de révision CAB et recommandations.
- Journaux de mise en œuvre et résultats de vérification.
- Enregistrements de communication.
- Problèmes ou incidents durant la mise en œuvre.
- Décisions de retour arrière et exécution (le cas échéant).
- Résultats de la revue post-implémentation.

Les enregistrements des changements doivent être conservés pendant un minimum de **3 ans** pour la référence opérationnelle et **7 ans** pour les preuves d'audit.

### Mises à jour de la documentation

À la suite de changements système, la documentation suivante doit être mise à jour dans les **5 jours ouvrables** :

- Documentation de la configuration des systèmes.
- Diagrammes réseau et topologie.
- Procédures d'exploitation et runbooks.
- Procédures de reprise après sinistre (lorsque le changement affecte des systèmes critiques ou les RTO/RPO).

---

## Intégration avec la gestion de la configuration

La gestion des changements et la gestion de la configuration sont des disciplines complémentaires :

- La **gestion des changements** contrôle *comment* les changements sont effectués (approbation, tests, mise en œuvre).
- La **gestion de la configuration** contrôle *quel* est l'état actuel (référentiels, versions, éléments de configuration).

**Points d'intégration** :

- Les référentiels de configuration doivent être mis à jour à la suite de changements approuvés.
- La détection de dérive de configuration (état réel vs. référentiel) doit déclencher une investigation et une demande de changement correctif.
- La base de données de gestion de la configuration (CMDB) ou l'inventaire équivalent doit être la source faisant autorité pour l'évaluation des impacts (quels systèmes sont affectés).

Voir la **Politique de gestion de la configuration (A.8.9)** pour les exigences détaillées sur les référentiels et le contrôle des versions.

---

## Changements non autorisés

Les changements non autorisés — changements effectués sans suivre le processus de gestion des changements — doivent être :

- Détectés via la surveillance, la journalisation d'audit et les outils de gestion de la configuration.
- Investigués pour déterminer la cause racine et l'impact.
- Signalés au RSSI et escaladés à l'Équipe de revue de direction.
- Soumis à des actions correctives, pouvant inclure des mesures disciplinaires conformément au processus disciplinaire de l'organisation.

---

## Corrélation changements-incidents

Lorsqu'un incident de sécurité ou une panne de service survient, le Responsable des changements doit :

1. **Passer en revue les changements récents** dans les 48 heures précédant l'heure de début de l'incident.
2. **Corréler la chronologie de l'incident** avec les horodatages de mise en œuvre des changements.
3. **Identifier les changements potentiellement liés** (mêmes systèmes, dépendances, période).
4. **Escalader au CAB et au RSSI** si un changement est suspecté comme cause racine.

Lorsqu'un changement est confirmé comme cause racine d'un incident :

- **Revue post-implémentation obligatoire** dans les **3 jours ouvrables**.
- **Analyse des causes racines** pour identifier les lacunes du processus (tests insuffisants, évaluation d'impact manquée, approbation insuffisante).
- **Actions correctives** pour prévenir la récurrence.
- Si le changement figurait dans le Catalogue des changements standards, l'entrée du catalogue doit être révisée et potentiellement reclassifiée ou supprimée.

Le taux d'incidents liés aux changements est suivi comme métrique clé (cible : 0 par trimestre).

---

## Métriques de gestion des changements

L'équipe de gestion de la sécurité de l'information doit rapporter les métriques de gestion des changements au RSSI au moins trimestriellement :

| Métrique | Cible | Seuil critique |
|----------|--------|----------------|
| Taux de réussite des changements (changements réalisés sans retour arrière ni incident) | ≥ 95 % | < 85 % |
| Pourcentage de changements d'urgence | < 5 % | > 10 % |
| Taux de réalisation des RPI (pour les RPI obligatoires) | 100 % | < 80 % |
| Utilisation du Catalogue des changements standards | ≥ 30 % de l'ensemble des changements | < 15 % |
| Incidents liés aux changements | 0 | > 2 par trimestre |
| Changements en retard (après la mise en œuvre planifiée) | 0 | > 5 |
| Conformité des mises à jour documentaires (dans les 5 jours ouvrables) | ≥ 95 % | < 80 % |

Les métriques dépassant les seuils critiques doivent être escaladées au RSSI pour une attention immédiate et rapportées lors de la prochaine revue de direction.

---

## Rôles et responsabilités

| Rôle | Responsabilités |
|------|-----------------|
| **RSSI** | Propriété de la politique ; approbation des changements à risque élevé et d'urgence ; autorisation des exceptions ; révision des métriques |
| **Responsable des changements** | Propriété du processus ; présidence du CAB ; maintenance du Catalogue des changements standards ; suivi des métriques ; amélioration continue |
| **Responsable des opérations informatiques** | Approbation des changements à risque moyen/élevé ; présidence du CAB d'urgence ; coordination des fenêtres de changement |
| **Membres du CAB** | Révision des changements, évaluation des impacts, identification des risques, recommandations d'approbation |
| **Demandeurs de changement** | Soumettre des demandes de changement complètes avec justification métier et évaluation des impacts |
| **Responsables de mise en œuvre** | Exécuter les changements approuvés selon les procédures documentées ; effectuer les tests de vérification |
| **Propriétaires de systèmes** | Approuver les changements sur les systèmes dont ils sont responsables ; fournir l'évaluation des impacts ; responsables de la disponibilité du système |

---

## Preuves

Les preuves suivantes démontrent la conformité à la présente politique :

| # | Preuve | Responsable | Fréquence |
|---|--------|-------------|-----------|
| 1 | Enregistrements du **système de gestion des changements** (toutes les demandes de changement avec les champs requis) | Responsable des changements | *Par événement ; audité trimestriellement* |
| 2 | **Procès-verbaux du CAB** (participants, décisions, justifications, actions à entreprendre) | Responsable des changements | *Par réunion ; conservés 3 ans* |
| 3 | **Catalogue des changements standards** avec historique des versions et enregistrements de révision trimestrielle | Responsable des changements | *Révisé trimestriellement ; version contrôlée* |
| 4 | **Calendrier des changements** avec périodes de gel et changements planifiés | Responsable des changements | *Maintenu en continu ; révisé mensuellement* |
| 5 | Enregistrements de **revue post-implémentation** pour les changements d'urgence, échoués et à risque élevé | Responsable des changements | *Par changement éligible ; cible : 100 % de réalisation* |
| 6 | **Enregistrements d'approbation** avec horodatages montrant l'autorité appropriée par niveau de risque | Responsable des changements | *Par changement ; conservés 7 ans* |
| 7 | **Enregistrements de test** (plans de test, résultats, validations) pour les changements normaux et à risque élevé | Opérations informatiques | *Par changement ; conservés 3 ans* |
| 8 | **Justification des changements d'urgence** et enregistrements de révision CAB rétrospective | RSSI | *Par changement d'urgence ; révisé mensuellement* |
| 9 | Rapports de **métriques de gestion des changements** | Responsable des changements | *Trimestriel ; présenté lors de la revue de direction* |
| 10 | Enregistrements d'**investigation et d'actions correctives pour les changements non autorisés** | RSSI | *Par événement ; conservés 3 ans* |

---

# Conformité à la politique

## Mesure de la conformité

L'équipe de gestion de la sécurité de l'information vérifiera la conformité à la présente politique par diverses méthodes, incluant notamment les audits des enregistrements de changements, les revues des réunions CAB, le suivi de la réalisation des RPI, l'analyse des changements d'urgence, les audits internes et externes, et le retour d'information au propriétaire de la politique.

## Exceptions

Toute exception à la présente politique doit être approuvée et enregistrée à l'avance par le Responsable de la sécurité de l'information, avec acceptation documentée du risque, contrôles compensatoires et date de révision définie. Les exceptions doivent être rapportées à l'Équipe de revue de direction.

## Non-conformité

Tout employé reconnu coupable d'avoir violé la présente politique peut faire l'objet de mesures disciplinaires, pouvant aller jusqu'au licenciement.

## Amélioration continue

La présente politique est révisée et mise à jour dans le cadre du processus d'amélioration continue. Les révisions doivent prendre en compte les évolutions des normes de gestion des changements, les changements technologiques, les risques émergents, les changements réglementaires, les conclusions des RPI et les enseignements tirés des incidents liés aux changements.

---

# Zones de la norme ISO 27001 couvertes

Politique de gestion des changements — Correspondance avec les contrôles ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership et engagement | 5.1 Politiques de sécurité de l'information |
| Clause 5.2 Politique | 5.4 Responsabilités de la direction |
| Clause 6.2 Objectifs de sécurité de l'information | 5.36 Conformité aux politiques, règles et standards |
| Clause 6.3 Planification des changements | 5.37 Procédures d'exploitation documentées |
| Clause 7.3 Sensibilisation | 6.3 Sensibilisation, éducation et formation à la sécurité de l'information |
| Clause 8.1 Planification et contrôle opérationnels | 6.4 Processus disciplinaire |
| | **8.32 Gestion des changements** |
| | 8.9 Gestion de la configuration |
| | 8.19 Installation de logiciels sur les systèmes en production |

**Cadre réglementaire et légal** :

| Cadre | Pertinence |
|-------|-----------|
| nLPD suisse (revLPD) | Art. 8 — Mesures techniques et organisationnelles (la gestion des changements comme mesure organisationnelle protégeant les systèmes de traitement des données) |
| OPDo suisse (Ordonnance sur la protection des données) | Art. 1–3 — Exigences minimales en matière de sécurité des données |
| RGPD de l'UE (le cas échéant) | Art. 32 — Sécurité du traitement (la gestion des changements comme mesure appropriée) |
| ISO/IEC 27001:2022 | Contrôle Annexe A 8.32 — Gestion des changements |
| ISO/IEC 27002:2022 | Section 8.32 — Recommandations de mise en œuvre (9 éléments obligatoires) |
| NIST SP 800-53 Rév. 5 | CM-3 (Contrôle des changements de configuration), CM-4 (Analyses d'impact), CM-5 (Restrictions d'accès pour les changements) |
| CIS Controls v8 | Contrôle 2 (Inventaire et contrôle des actifs logiciels — Mesure 2.5 : Liste autorisée des logiciels autorisés) |

---

<!-- QA_VERIFIED: 2026-03-29 -->
