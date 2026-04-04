<!-- ISMS-CORE:POLICY:ISMS-POL-A.8.32-FR:framework:POL:a.8.32 -->
**ISMS-POL-A.8.32 – Gestion des changements**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Gestion des changements |
| **Type de document** | Politique |
| **Identifiant du document** | ISMS-POL-A.8.32 |
| **Créateur du document** | Responsable de la Sécurité des Systèmes d'Information (RSSI) |
| **Propriétaire du document** | Directeur général (DG) |
| **Approuvé par** | Direction générale |
| **Date de création** | [Date] |
| **Version** | 1.0 |
| **Date de version** | [À définir] |
| **Classification** | Interne |
| **Statut** | Brouillon |

**Historique des versions** :

| Version | Date | Auteur | Modifications |
|---------|------|--------|---------------|
| 1.0 | [Date] | RSSI | Politique initiale consolidée pour la première certification ISO 27001:2022 |

**Cycle de révision** : Annuel
**Prochaine date de révision** : [Date d'entrée en vigueur + 12 mois]

**Chaîne d'approbation** :

- Principale : Responsable de la Sécurité des Systèmes d'Information (RSSI)
- Secondaire : Directeur des Systèmes d'Information (DSI) / Responsable des opérations IT
- Conformité : Responsable juridique/conformité
- Autorité finale : Direction générale (PDG)

**Documents connexes** :

- ISMS-POL-00 (Cadre d'applicabilité réglementaire)
- ISMS-IMP-A.8.32.1-UG/TG (Évaluation du processus de changement)
- ISMS-IMP-A.8.32.2-UG/TG (Évaluation des types et catégories de changements)
- ISMS-IMP-A.8.32.3-UG/TG (Évaluation de la séparation des environnements)
- ISMS-REF-A.8.32 (Référence de gestion des changements — Modèles, outils, guides rapides)
- ISO/IEC 27001:2022 Contrôle A.8.32

---

## Résumé exécutif

Cette politique établit les exigences de [Organisation] pour les contrôles de gestion des changements afin d'assurer des modifications sécurisées et contrôlées des systèmes d'information, conformément au Contrôle A.8.32 de la norme ISO/IEC 27001:2022.

**Périmètre** : Cette politique s'applique à tous les changements apportés aux systèmes de traitement de l'information, aux applications, à l'infrastructure, aux équipements réseau et aux systèmes de soutien, quel que soit le modèle de déploiement (sur site, cloud, hybride). Tous les types de changements (matériel, logiciel, configuration, infrastructure, données, processus, documentation) et tous les environnements (développement, test, préproduction, production, reprise après sinistre) sont couverts.

**Objet** : Définir les exigences organisationnelles pour la mise en œuvre et la gouvernance des contrôles de gestion des changements. Cette politique établit QUELLE gestion des changements est requise et QUI en est responsable. Les procédures de mise en œuvre (COMMENT les changements sont exécutés) sont documentées séparément dans les classeurs d'évaluation ISMS-IMP-A.8.32.

**Alignement réglementaire** : Cette politique traite des exigences de conformité obligatoires conformément à ISMS-POL-00, notamment le Contrôle A.8.32 de la norme ISO/IEC 27001:2022.

---

# Alignement sur les contrôles et périmètre

## Contrôle A.8.32 de la norme ISO/IEC 27001:2022

**Norme ISO/IEC 27001:2022 Annexe A.8.32 — Gestion des changements**

> *Les changements apportés aux installations de traitement de l'information et aux systèmes d'information devraient être soumis à des procédures de gestion des changements.*

**Neuf éléments obligatoires (ISO/IEC 27002:2022)** :

| Élément | Description | Section de référence |
|---------|-------------|---------------------|
| **(a) Planification et évaluation de l'impact** | Évaluer les impacts potentiels avant mise en œuvre | 2.1 |
| **(b) Autorisation** | Obtenir les approbations appropriées selon le risque/l'impact | 2.1 |
| **(c) Communication** | Informer les parties prenantes des changements et des impacts | 2.1 |
| **(d) Tests et acceptation** | Vérifier que les changements fonctionnent comme prévu | 2.3 |
| **(e) Mise en œuvre** | Exécuter les changements de manière contrôlée | 2.1 |
| **(f) Urgences et contingences** | Gérer les changements urgents avec des procédures accélérées | 2.4 |
| **(g) Tenue des dossiers** | Maintenir une piste d'audit de tous les changements | 2.1 |
| **(h) Mises à jour de la documentation** | Mettre à jour les procédures opérationnelles et les guides | 2.1 |
| **(i) Mises à jour des plans de continuité** | Mettre à jour les plans de continuité lors de changements d'infrastructure | 2.1 |

## Périmètre

**Cette politique s'applique à** :

**Systèmes d'information** (tous systèmes traitant, stockant ou transmettant des informations organisationnelles) :

- Systèmes de production (applications métier, bases de données, ERP, CRM, systèmes financiers)
- Systèmes d'infrastructure (serveurs, stockage, virtualisation, équipements réseau)
- Systèmes de sécurité (pare-feu, IDS/IPS, SIEM, systèmes d'authentification, systèmes de chiffrement)
- Services cloud (IaaS, PaaS, SaaS — configurations sous contrôle du client)
- Systèmes de communication (e-mail, plateformes collaboratives, téléphonie)
- Environnements de développement et de test (pipelines CI/CD inclus)
- Systèmes de bureautique (e-mail, collaboration, gestion documentaire)
- Sites web et applications web

**Types de changements** : Matériel, logiciel, configuration, infrastructure, données, processus, documentation.

**Tous les environnements** : Développement, Test/Assurance qualité, Préproduction, Production, Reprise après sinistre.

**Hors périmètre** :

- Changements organisationnels (sauf s'ils affectent des systèmes IT)
- Modifications du contenu des sites web, des documents ou des e-mails
- Opérations de routine (sauvegardes planifiées automatisées, rotation des journaux, archivage)
- Actions en libre-service des utilisateurs (réinitialisations de mots de passe via portail approuvé)
- Changements de fournisseurs de services externes entièrement gérés en coulisses

**Justification des exclusions** : Ces exclusions représentent des activités qui (1) n'affectent pas matériellement la sécurité de l'information, (2) sont gérées via des processus de gouvernance distincts, (3) sont entièrement automatisées avec des contrôles adéquats, ou (4) sont hors du contrôle de l'organisation.

## Définitions

| Terme | Définition |
|-------|------------|
| **Changement** | Toute addition, modification ou suppression de composants du système d'information pouvant affecter la sécurité ou la disponibilité |
| **Comité d'Approbation des Changements (CAC)** | Groupe multidisciplinaire fournissant une revue experte, une évaluation de l'impact et des recommandations pour les changements normaux et d'urgence |
| **Responsable des changements** | Personne responsable du processus de gestion des changements, de la coordination du CAC, du suivi des métriques et de l'amélioration continue |
| **Demande de changement** | Dossier formel documentant le changement proposé incluant description, justification, évaluation de l'impact, plan de mise en œuvre, approche de test et procédure de retour arrière |
| **Changement d'urgence** | Changement nécessitant une mise en œuvre accélérée pour résoudre un incident critique, une vulnérabilité de sécurité ou prévenir un impact métier significatif |
| **Changement normal** | Changement nécessitant une évaluation complète, une revue CAC et un flux d'approbation standard |
| **Revue post-mise en œuvre (RPMO)** | Revue structurée après la mise en œuvre d'un changement pour vérifier les objectifs, identifier les enseignements tirés et identifier les opportunités d'amélioration |
| **Retour arrière** | Procédure pour annuler un changement et remettre le système dans son état de fonctionnement précédent |
| **Changement standard** | Changement pré-approuvé, à faible risque et routinier suivant une procédure documentée du Catalogue des changements standard. Peut être mis en œuvre sans revue CAC |

---

# Exigences de gestion des changements

Ce section définit les exigences organisées en trois domaines :

1. **Exigences du processus de changement** (2.1) : Flux de travail de base
2. **Exigences de classification des changements** (2.2) : Types standard, normal et urgence
3. **Exigences de tests et validation** (2.3) : Tests avant déploiement en production

## Exigences du processus de changement

### Soumission des demandes de changement

**EXG-PROCESSUS-001 : Documentation des demandes de changement**

[Organisation] DOIT exiger que tous les changements dans le périmètre soient soumis comme demandes de changement formelles dans le système de gestion des changements.

**Informations minimales requises** :

- Identifiant unique du changement
- Description et périmètre du changement
- Justification métier
- Systèmes/composants affectés
- Date/fenêtre de mise en œuvre
- Identification du demandeur et de l'exécutant
- Évaluation de l'impact (disponibilité, confidentialité, intégrité)
- Classification des risques
- Procédure de retour arrière
- Approche de test
- Dépendances avec d'autres changements
- Plan de communication

**Exceptions** : Les changements standard pré-approuvés peuvent utiliser une soumission simplifiée mais DOIVENT quand même créer un dossier de demande de changement.

---

### Planification et évaluation de l'impact

**EXG-PROCESSUS-002 : Évaluation de l'impact**

[Organisation] DOIT exiger une évaluation de l'impact pour tous les changements évaluant :

- Impact technique (systèmes affectés, dépendances, points d'intégration)
- Impact métier (services affectés, impact utilisateurs, perturbation des opérations)
- Impact sécurité (risques de confidentialité, intégrité, disponibilité)
- Impact conformité (obligations réglementaires, contrôles d'audit)
- Niveau de risque (probabilité d'échec × magnitude de l'impact)

---

**EXG-PROCESSUS-003 : Planification de la mise en œuvre**

[Organisation] DOIT exiger des plans de mise en œuvre pour les changements normaux et d'urgence incluant :

- Procédure étape par étape
- Exigences en ressources (personnel, outils, accès)
- Calendrier de mise en œuvre
- Dépendances et prérequis
- Étapes de vérification
- Déclencheurs du retour arrière et procédure
- Points de contrôle de communication

---

### Autorisation et approbation

**EXG-PROCESSUS-004 : Flux d'approbation**

[Organisation] DOIT définir l'autorité d'approbation selon le niveau de risque du changement :

| Niveau de risque | Autorité d'approbation | Revue CAC | Niveau de documentation |
|-----------------|----------------------|-----------|------------------------|
| **Faible** | Changement standard (pré-approuvé) | Non requise | Catalogue des changements standard |
| **Moyen** | Propriétaire du service / Responsable d'équipe | Recommandée | Standard |
| **Élevé** | Responsable des opérations IT / RSSI | Requise | Complète |
| **Critique** | Direction générale | Requise | Complète + Acceptation des risques |

**Mise en œuvre** : La matrice d'autorité d'approbation est documentée dans ISMS-IMP-A.8.32.1 identifiant les rôles/postes spécifiques avec autorité d'approbation pour chaque niveau de risque. La matrice DOIT être révisée et approuvée par le RSSI annuellement et mise à jour dans les 30 jours suivant les changements organisationnels affectant les autorités d'approbation.

---

**EXG-PROCESSUS-005 : Comité d'Approbation des Changements (CAC)**

[Organisation] DOIT établir un Comité d'Approbation des Changements (CAC) pour la revue des changements normaux et d'urgence.

**Responsabilités du CAC** :

- Réviser les demandes de changement pour leur complétude et la précision de l'évaluation des risques
- Identifier les conflits potentiels entre les changements planifiés
- Évaluer l'impact sur les systèmes dépendants
- Recommander l'approbation, le report ou le refus
- Réviser les changements d'urgence (rétrospectivement pour les urgences critiques dans le temps)

**Composition du CAC** (minimum) :

- Responsable des changements (président)
- Représentant des opérations IT
- Représentant de la sécurité
- Propriétaires d'applications métier (pour les changements pertinents)
- Experts techniques supplémentaires (selon les besoins)

**Exigences de quorum** : Les réunions du CAC nécessitent la présence minimale de : (1) Responsable des changements (président), (2) Représentant des opérations IT, (3) Représentant de la sécurité, et (4) au moins un membre supplémentaire du CAC. Les réunions du CAC d'urgence PEUVENT se tenir avec un quorum réduit (Responsable des changements + un membre supplémentaire) si le temps est critique, avec une revue rétrospective complète du CAC requise dans les 48 heures.

**Preuves de fonctionnement** : Le fonctionnement du CAC est vérifié par : (1) procès-verbaux de réunion pour toutes les réunions planifiées et d'urgence avec date, participants, changements révisés, décisions, justification et actions, (2) dossiers de présence montrant les exigences de quorum satisfaites, (3) dossiers de demandes de changement montrant les notes et recommandations du CAC, (4) révision annuelle de la charte du CAC. Les procès-verbaux des réunions du CAC sont conservés pendant minimum 3 ans.

**Fréquence du CAC** :

- Réunions régulières (hebdomadaires recommandées pour les environnements de changement actifs)
- Réunions du CAC d'urgence (selon les besoins)
- Revue CAC virtuelle (pour les changements urgents entre réunions)

---

### Communication

**EXG-PROCESSUS-006 : Communication aux parties prenantes**

[Organisation] DOIT communiquer les changements aux parties prenantes concernées incluant :

- Calendrier et timing du changement
- Impact attendu sur le service (durée, périmètre)
- Actions requises des utilisateurs (le cas échéant)
- Coordonnées du support
- Décision de retour arrière et communication

**Timing de communication** :

- **Changements planifiés** : Notification minimale d'avance selon les exigences opérationnelles de [Organisation]
- **Changements d'urgence** : Communication dès que possible en toute sécurité
- **Complétion du changement** : Confirmation aux parties prenantes à la complétion

---

### Exécution de la mise en œuvre

**EXG-PROCESSUS-007 : Mise en œuvre contrôlée**

[Organisation] DOIT mettre en œuvre les changements selon le plan de mise en œuvre approuvé avec :

- Vérification des prérequis et des dépendances
- Exécution des étapes documentées
- Surveillance en temps réel pendant la mise en œuvre
- Tests de vérification post-mise en œuvre
- Documentation des étapes réellement effectuées

---

**EXG-PROCESSUS-008 : Exécution du retour arrière**

[Organisation] DOIT exécuter la procédure de retour arrière lorsque :

- Le changement n'atteint pas ses objectifs
- Une dégradation des performances inacceptable survient
- Une vulnérabilité de sécurité est introduite
- Une fonction métier critique est altérée
- Les déclencheurs du retour arrière (définis dans la demande de changement) sont atteints

**Autorité de décision du retour arrière** : Même autorité d'approbation que le changement original (ou supérieure pour le retour arrière d'urgence).

---

### Tenue des dossiers et piste d'audit

**EXG-PROCESSUS-009 : Dossiers de changement**

[Organisation] DOIT maintenir des dossiers de changement complets incluant :

- Toutes les informations de la demande de changement
- Dossiers d'approbation avec horodatages et approbateurs
- Notes et recommandations du CAC
- Journaux de mise en œuvre et résultats de vérification
- Dossiers de communication
- Incidents ou problèmes pendant la mise en œuvre
- Décisions et exécution du retour arrière (le cas échéant)
- Résultats de la revue post-mise en œuvre

**Conservation des dossiers** : Minimum de la période définie par [Organisation] (recommandé : 7 ans pour l'audit, 3 ans pour la référence opérationnelle).

---

### Mises à jour de la documentation

**EXG-PROCESSUS-010 : Mises à jour de la documentation opérationnelle**

[Organisation] DOIT mettre à jour la documentation opérationnelle suite aux changements :

- Documentation de la configuration des systèmes
- Schémas et topologie réseau
- Documents d'architecture applicative
- Procédures opérationnelles et guides de procédures
- Guides de dépannage
- Procédures de reprise après sinistre
- Documentation utilisateur (le cas échéant)

**Timing de mise à jour** : Dans le délai défini par [Organisation] (recommandé : 5 jours ouvrables pour les changements non urgents).

---

**EXG-PROCESSUS-011 : Mises à jour des plans de continuité**

[Organisation] DOIT réviser et mettre à jour les plans de continuité des activités lorsque les changements affectent :

- Systèmes ou applications métier critiques
- Infrastructure soutenant la continuité des activités
- Procédures de reprise après sinistre
- Objectifs de temps de récupération (RTO) ou de point de récupération (RPO)
- Procédures de sauvegarde et de restauration

---

### Revue post-mise en œuvre

**EXG-PROCESSUS-012 : Revue post-mise en œuvre (RPMO)**

[Organisation] DOIT conduire une revue post-mise en œuvre pour :

- Tous les changements d'urgence (obligatoire)
- Tous les changements en échec (obligatoire)
- Les changements normaux au-delà du seuil de risque défini
- Les changements standard lorsque les patterns suggèrent qu'une revue est nécessaire

**Contenu de la RPMO** :

- Objectifs atteints vs. résultats planifiés
- Problèmes de mise en œuvre rencontrés
- Efficacité de la planification et de l'exécution
- Retours utilisateurs et impact sur le service
- Enseignements tirés et opportunités d'amélioration

**Timing de la RPMO** : Dans le délai défini par [Organisation] (recommandé : 7 jours ouvrables pour les changements d'urgence, 14 jours pour les changements normaux).

---

## Exigences de classification des changements

### Exigences de changement standard

**EXG-CLASSIF-001 : Catalogue des changements standard**

[Organisation] DOIT maintenir un Catalogue des changements standard contenant des changements pré-approuvés, à faible risque qui :

- Ont des impacts et des résultats bien compris
- Suivent des procédures documentées et répétables
- Présentent un faible risque d'échec
- Ont des procédures de retour arrière définies (si nécessaire)

**Maintenance du catalogue** : Révisé trimestriellement par le Responsable des changements avec contribution du CAC. La version actuelle est documentée dans ISMS-IMP-A.8.32.2.

**Contrôle des versions du catalogue** : Conserver l'historique des versions documentant : (1) numéro de version et date, (2) changements apportés, (3) raison des changements, (4) approbateur.

---

**EXG-CLASSIF-002 : Exécution des changements standard**

Les changements standard DOIVENT :

- Être journalisés dans le système de gestion des changements (aucune approbation CAC requise)
- Suivre la procédure documentée du Catalogue des changements standard
- Être exécutés par du personnel autorisé
- Inclure une vérification post-exécution

---

**EXG-CLASSIF-003 : Revue des changements standard**

[Organisation] DOIT réviser le Catalogue des changements standard :

- Trimestriellement (minimum)
- Après tout échec de changement standard
- Lorsque les patterns d'utilisation suggèrent une reclassification

**Critères de revue** : Taux de succès élevé (> 95 % recommandé), aucun incident significatif causé, procédure précise et complète.

---

### Exigences de changement normal

**EXG-CLASSIF-004 : Processus de changement normal**

Les changements normaux DOIVENT suivre le processus complet de gestion des changements incluant :

- Demande de changement formelle avec évaluation de l'impact
- Évaluation et classification des risques
- Revue et recommandation du CAC
- Approbation par l'autorité appropriée
- Tests dans un environnement hors production
- Communication aux parties prenantes
- Mise en œuvre planifiée
- Vérification post-mise en œuvre
- Revue post-mise en œuvre (pour les changements à haut risque)

---

**EXG-CLASSIF-005 : Évaluation des risques des changements**

[Organisation] DOIT évaluer le risque des changements normaux en utilisant une méthodologie définie considérant :

- **Impact** : Périmètre des systèmes/utilisateurs affectés, criticité métier, sensibilité des données
- **Probabilité** : Complexité, nouveauté, expérience de l'exécutant, complétude des tests
- **Niveau de risque** : Combinaison de l'impact et de la probabilité

**Résultat** : Classification Faible / Moyen / Élevé / Critique déterminant l'autorité d'approbation et le niveau de rigueur.

---

### Calendrier des changements et planification

**EXG-CLASSIF-006 : Calendrier des changements**

[Organisation] DOIT maintenir un calendrier des changements identifiant :

- Changements planifiés (date, heure, systèmes affectés)
- Périodes de gel des changements (aucun changement non urgent)
- Fenêtres d'exclusion (périodes métier critiques)
- Conflits entre changements (impacts se chevauchant)

**Exemples de périodes de gel des changements** :

- Clôture financière de fin d'exercice
- Lancement majeur de produits
- Périodes de haute activité métier
- Soumissions réglementaires majeures

---

## Exigences de tests et de validation

### Exigences de séparation des environnements

**EXG-TEST-001 : Environnements hors production**

[Organisation] DOIT maintenir des environnements hors production séparés pour les tests de changements (conformément à ISMS-POL-A.8.31).

**EXG-TEST-002 : Flux de promotion des environnements**

[Organisation] DOIT mettre en œuvre un flux de promotion contrôlé :

- **Dev → Test** : Code complété, tests unitaires réussis
- **Test → Préproduction** : Tests d'intégration réussis, UAT complété
- **Préproduction → Production** : Validation finale complétée, approbations obtenues

**EXG-TEST-003 : Protection de l'environnement de production**

[Organisation] DOIT restreindre les changements en production à :

- Uniquement les exécutants de changements autorisés
- Changements avec tests complétés (sauf changements d'urgence approuvés)
- Fenêtres de changements planifiées (sauf urgences)
- Changements avec approbations appropriées

---

### Exigences de tests

**EXG-TEST-004 : Procédures de test**

[Organisation] DOIT exiger des tests appropriés au risque du changement :

| Risque du changement | Tests requis |
|---------------------|-------------|
| **Faible** | Tests de vérification de l'exécutant |
| **Moyen** | Tests fonctionnels, tests d'intégration |
| **Élevé** | Tests complets : fonctionnel, intégration, performance, UAT |
| **Critique** | Suite complète de tests : fonctionnel, intégration, performance, sécurité, UAT, reprise après sinistre |

**Exigences minimales de test** (tous les changements) :

- Tests fonctionnels (le changement atteint l'objectif prévu)
- Tests d'intégration (le changement ne casse pas les systèmes dépendants)
- Tests du retour arrière (la procédure de retour arrière est vérifiée)

---

**EXG-TEST-005 : Intégration des tests de sécurité**

[Organisation] DOIT intégrer des tests de sécurité pour les changements qui :

- Affectent les mécanismes d'authentification ou d'autorisation
- Modifient les contrôles ou configurations de sécurité
- Exposent de nouvelles interfaces externes
- Traitent des données Restreintes ou Confidentielles
- Affectent des implémentations cryptographiques

**Intégration avec le Contrôle 8.29** : Les exigences de tests de sécurité s'alignent avec ISMS-POL-A.8.25-26-29 (Cycle de vie du développement sécurisé).

---

**EXG-TEST-006 : Critères d'acceptation**

[Organisation] DOIT définir des critères d'acceptation pour les changements incluant :

- Exigences fonctionnelles satisfaites
- Exigences de performance satisfaites (aucune dégradation inacceptable)
- Points d'intégration validés
- Exigences de sécurité validées
- Aucun défaut de gravité critique ou élevée
- Acceptation des utilisateurs obtenue (le cas échéant)

---

### Gestion des données de test

**EXG-TEST-007 : Protection des données de production**

[Organisation] DOIT protéger les données de production dans les environnements de test :

- Les données de production NE DOIVENT PAS être utilisées dans les environnements de test sans protection
- Si des données de production sont requises pour les tests, les données DOIVENT être masquées/anonymisées conformément à ISMS-POL-A.8.11
- Les données de test synthétiques DEVRAIENT être utilisées lorsque c'est faisable
- Les données de test DOIVENT être classifiées et protégées conformément à ISMS-POL-A.5.12

---

## Exigences de changement d'urgence

### Critères de changement d'urgence

**EXG-URGENCE-001 : Classification d'urgence**

[Organisation] DOIT classifier les changements comme urgence uniquement lorsque :

- Résolution d'un incident de sécurité actif ou d'une vulnérabilité
- Restauration d'une interruption de service critique
- Prévention d'une défaillance système imminente
- Traitement d'une exigence réglementaire urgente
- Atténuation d'une violation de données active

**Les changements d'urgence NE DOIVENT PAS être utilisés pour** :

- La commodité ou la pression des délais
- Une mauvaise planification
- Des travaux de routine
- Des fonctionnalités souhaitées

**Objectif** : Taux de changements d'urgence < 5 % de tous les changements.

---

**EXG-URGENCE-005 : Gestion du seuil de changements d'urgence**

[Organisation] DOIT surveiller le pourcentage de changements d'urgence mensuellement. Lorsque les changements d'urgence dépassent le seuil cible (< 5 % de tous les changements) pendant deux mois consécutifs, le Responsable des changements DOIT :

- Conduire une analyse des causes profondes identifiant les problèmes systémiques
- Présenter les résultats au CAC avec des recommandations de remédiation
- Mettre en œuvre des actions correctives dans les 30 jours
- Rapporter le dépassement du seuil et le plan de remédiation au RSSI

---

### Approbation des changements d'urgence

**EXG-URGENCE-002 : Approbation accélérée**

Les changements d'urgence DOIVENT obtenir l'approbation de :

- Responsable des opérations IT ou RSSI (minimum)
- Approbations supplémentaires dans la mesure du faisable selon les contraintes de temps
- Revue rétrospective du CAC dans le délai défini par [Organisation] (recommandé : 24-48 heures)

**Documentation d'approbation** :

- Justification de l'urgence
- Risque et impact évalués
- Alternatives considérées
- Décision d'acceptation du risque

---

### Tests des changements d'urgence

**EXG-URGENCE-003 : Tests proportionnels au risque**

Les changements d'urgence DOIVENT subir des tests proportionnels aux contraintes de temps :

- **Minimum** : Vérification par l'exécutant dans un environnement isolé (si possible)
- **Préféré** : Tests limités dans l'environnement de test
- **Si aucun test possible** : Acceptation du risque documentée et plan de retour arrière

---

### Revue post-urgence

**EXG-URGENCE-004 : Revue post-mise en œuvre obligatoire**

[Organisation] DOIT conduire une revue post-mise en œuvre pour TOUS les changements d'urgence dans le délai défini (recommandé : 5 jours ouvrables) traitant :

- Justification de l'urgence validée
- Approches alternatives disponibles
- Efficacité du changement
- Améliorations de processus pour prévenir les urgences futures
- Si le changement devrait être ajouté au Catalogue des changements standard

---

### Délais spécifiés par [Organisation]

**EXG-PROCESSUS-013 : Délais définis par [Organisation]**

[Organisation] DOIT documenter des délais spécifiques pour les activités de gestion des changements dans ISMS-IMP-A.8.32.1 :

| Activité | Délai recommandé par défaut |
|----------|---------------------------|
| Mises à jour de la documentation | 5 jours ouvrables |
| Déclencheur de révision des plans de continuité | Dans le processus d'approbation du changement |
| Revue post-mise en œuvre (changements normaux) | 14 jours ouvrables |
| Revue post-mise en œuvre (changements d'urgence) | 5 jours ouvrables |
| Revue rétrospective CAC urgence | 24-48 heures |
| Notification d'avance aux parties prenantes | Selon les exigences opérationnelles |
| Conservation des dossiers de changement | 7 ans (audit), 3 ans (opérationnel) |

---

# Rôles et responsabilités

| Rôle | Responsabilités |
|------|----------------|
| **Responsable des changements** | Responsable du processus ; préside le CAC ; maintient le Catalogue ; suit les métriques |
| **CAC** | Revoit et recommande sur les changements normaux et d'urgence ; multi-disciplinaire |
| **Demandeur** | Soumet les demandes avec information complète ; obtient la justification métier |
| **Exécutant** | Exécute les changements approuvés ; vérifie les prérequis ; documente les étapes |
| **Propriétaire du système** | Révise les changements sur ses systèmes ; approuve selon la matrice d'autorité |
| **RSSI / Sécurité de l'information** | Révise les changements liés à la sécurité ; approuve les changements à haut risque |
| **Responsable des opérations IT** | Approuve les changements moyens et élevés ; coordonne les fenêtres |
| **Direction générale** | Approuve les changements critiques ; reçoit les métriques |

---

# Gouvernance de la politique

## Propriété de la politique

**Propriétaire de la politique** : Responsable de la Sécurité des Systèmes d'Information (RSSI)

## Cycle de vie de la politique

**Révision annuelle** (obligatoire) : Révision complète de la politique, Q4 recommandé.

**Révisions déclenchées** : Mises à jour de la norme ISO/IEC 27001, changements réglementaires significatifs, changements organisationnels majeurs, changements technologiques, incidents majeurs ou constats d'audit.

## Gestion des exceptions

**Scénarios valides d'exception** :

- Contraintes techniques empêchant la pleine conformité
- Circonstances métier nécessitant une dérogation temporaire
- Contrôles compensatoires alternatifs offrant une protection équivalente

**Exceptions NON appropriées** : Commodité, préférence, contraintes de ressources, désaccord avec l'intention de la politique.

**Autorité d'approbation des exceptions** :

- Exceptions aux exigences standard : Responsable des changements
- Exceptions aux exigences critiques : RSSI
- Toutes les exceptions : Risque accepté par le Propriétaire du système

## Surveillance de la conformité

**Métriques de conformité** (suivies via les tableaux de bord récapitulatifs des classeurs ISMS-IMP-A.8.32.1-4) :

- Taux de succès des changements
- Pourcentage de changements d'urgence
- Taux de complétion des RPMO
- Utilisation du Catalogue des changements standard
- Incidents liés aux changements
- Durée moyenne des changements
- Fréquence et présence aux réunions du CAC

**Reporting de conformité** :

- Tableau de bord récapitulatif trimestriel au RSSI
- Résumé annuel de conformité à la Direction générale
- Suivi des constats d'audit et remédiation

---

# Intégration avec les contrôles connexes

La gestion des changements (A.8.32) s'intègre avec six contrôles ISO 27001 connexes :

| Contrôle | Relation |
|----------|----------|
| **A.5.30** (Continuité TIC) | Plans de continuité mis à jour lors de changements d'infrastructure |
| **A.5.37** (Procédures documentées) | Procédures opérationnelles mises à jour après les changements |
| **A.8.19** (Installation de logiciels) | L'installation suit le processus de gestion des changements |
| **A.8.29** (Tests de sécurité) | Tests de sécurité intégrés dans les procédures de test des changements |
| **A.8.31** (Séparation des environnements) | La séparation est appliquée via le flux de promotion |
| **A.8.33** (Informations de test) | Données de production protégées dans les environnements de test |

---

# Enregistrement d'approbation

| Rôle | Nom | Date |
|------|-----|------|
| **Responsable de la Sécurité des Systèmes d'Information (RSSI)** | [Nom] | [Date] |
| **Directeur des Systèmes d'Information (DSI)** | [Nom] | [Date] |
| **Responsable des opérations IT** | [Nom] | [Date] |
| **Responsable juridique/conformité** | [Nom] | [Date] |
| **Direction générale (PDG)** | [Nom] | [Date] |

---

**FIN DU DOCUMENT DE POLITIQUE**

---

*Cette politique établit les exigences de gestion des changements. Les procédures de mise en œuvre, modèles, outils et guides de référence rapide sont documentés dans ISMS-IMP-A.8.32 (classeurs d'évaluation) et ISMS-REF-A.8.32 (référence technique).*

<!-- QA_VERIFIED: 2026-04-02 -->
