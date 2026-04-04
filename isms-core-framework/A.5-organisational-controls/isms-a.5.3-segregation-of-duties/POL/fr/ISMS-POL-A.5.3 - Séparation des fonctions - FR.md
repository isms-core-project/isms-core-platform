<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.3-FR:framework:POL:a.5.3 -->
**ISMS-POL-A.5.3 — Séparation des fonctions**

---

**Contrôle documentaire**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Séparation des fonctions |
| **Type de document** | Politique |
| **Identifiant du document** | ISMS-POL-A.5.3 |
| **Créateur du document** | Responsable de la sécurité des systèmes d'information (RSSI) |
| **Propriétaire du document** | Responsable de la sécurité des systèmes d'information (RSSI) |
| **Approuvé par** | Direction générale |
| **Date de création** | [Date] |
| **Version** | 1.0 |
| **Date de version** | [Date à définir] |
| **Classification** | Interne |
| **Statut** | Brouillon |

**Historique des versions** :

| Version | Date | Auteur | Modifications |
|---------|------|--------|---------------|
| 1.0 | [Date] | RSSI | Politique initiale pour la certification ISO 27001:2022 |

**Cycle de révision** : Annuel
**Prochaine date de révision** : [Date d'entrée en vigueur + 12 mois]

**Chaîne d'approbation** :

- Primaire : Responsable de la sécurité des systèmes d'information (RSSI)
- Secondaire : Directeur administratif et financier (DAF)
- Autorité finale : Direction générale

**Documents connexes** :

- ISMS-POL-00 (Cadre d'applicabilité réglementaire)
- ISMS-POL-A.5.15-16-18 (Gestion des identités et des accès)
- ISMS-POL-A.8.2-3-5 (Authentification et accès privilégiés)
- ISMS-IMP-A.5.3.1-UG/TG (Évaluation de la matrice SdF)
- ISMS-IMP-A.5.3.2-UG/TG (Analyse des conflits)
- ISMS-IMP-A.5.3.3-UG/TG (Cartographie rôles-fonctions)
- ISO/IEC 27001:2022 Contrôle A.5.3

---

## Résumé exécutif

La présente politique établit les exigences de [Organisation] en matière de séparation des fonctions, afin de réduire le risque de fraude, d'erreur et d'activités non autorisées en veillant à ce que les responsabilités conflictuelles soient réparties entre différentes personnes ou systèmes.

**Périmètre** : Cette politique s'applique à tous les processus métier, systèmes d'information et activités dans lesquels des fonctions conflictuelles pourraient donner lieu à une fraude, une erreur ou une violation de la sécurité si elles étaient exercées par une seule personne.

**Objet** : Définir les exigences organisationnelles en matière de séparation des fonctions. Cette politique établit CE QUI est requis et QUI en est responsable. Les procédures de mise en œuvre (COMMENT) sont documentées séparément dans ISMS-IMP-A.5.3 (variantes UG/TG).

**Alignement réglementaire** : Cette politique répond aux exigences de conformité obligatoires définies dans ISMS-POL-00 (Cadre d'applicabilité réglementaire), notamment le CO suisse, l'ISO/IEC 27001:2022 et le RGPD de l'UE. Des exigences sectorielles conditionnelles (FINMA, SOX, PCI DSS v4.0.1) s'appliquent lorsque les activités de [Organisation] déclenchent leur applicabilité.

---

**Alignement des contrôles et périmètre**

**Contrôle ISO/IEC 27001:2022 A.5.3**

**Annexe A.5.3 de l'ISO/IEC 27001:2022 — Séparation des fonctions**

> *Les fonctions conflictuelles et les domaines de responsabilité conflictuels devraient être séparés.*

**Objectif du contrôle** : Réduire le risque de fraude, d'erreur et de contournement des contrôles de sécurité de l'information en séparant les fonctions conflictuelles.

**Type de contrôle** : Préventif
**Catégorie du contrôle** : Organisationnel

**Cette politique porte sur** :

- L'identification des fonctions conflictuelles nécessitant une séparation
- Les principes et exigences de séparation par type de processus
- Les contrôles compensatoires pour les petites équipes
- La gestion des dérogations et les processus d'approbation
- Les exigences de surveillance et de vérification

## Ce que fait cette politique

Cette politique :

- **Définit** les combinaisons de fonctions conflictuelles qui doivent être séparées
- **Établit** des normes minimales de séparation pour les processus critiques
- **Précise** les contrôles compensatoires lorsque la séparation ne peut être obtenue
- **Référence** les exigences réglementaires applicables conformément à ISMS-POL-00

## Ce que cette politique ne fait PAS

Cette politique NE :

- **Précise pas les détails techniques de mise en œuvre** (voir le guide de mise en œuvre ISMS-IMP-A.5.3)
- **Définit pas les matrices d'attribution des fonctions** (spécifiques à l'organisation, gérées opérationnellement)
- **Fournit pas de procédures de configuration des systèmes** (voir les contrôles techniques ISMS-IMP-A.5.3)
- **Se substitue pas à l'évaluation des risques** (les exigences de séparation sont informées par le traitement des risques de [Organisation])

**Justification** : La séparation des exigences politiques et du guide de mise en œuvre permet :

- La stabilité de la politique malgré les changements de structure organisationnelle
- La flexibilité pour différentes implémentations de systèmes
- Une distinction claire entre la gouvernance (politique) et l'exécution (mise en œuvre)

## Périmètre

**Cette politique s'applique à** :

- Tous les processus métier impliquant des transactions financières, des approbations ou des opérations sensibles
- Tous les systèmes d'information dans lesquels des fonctions conflictuelles pourraient permettre une fraude ou une erreur
- Tout le personnel (employés, prestataires, tiers) exerçant des fonctions séparées
- Tous les systèmes de contrôle d'accès appliquant la séparation des fonctions

**Hors périmètre** :

- Les processus opérationnels non sensibles bénéficiant d'une supervision adéquate
- Les processus automatisés disposant de contrôles de séparation intégrés (lorsque la séparation est assurée par l'automatisation, la configuration des contrôles et les pistes d'audit DOIVENT être validées au moins annuellement et lors de tout changement significatif par l'audit interne ou le propriétaire du contrôle)
- Les accès d'urgence temporaires (couverts par la gestion des dérogations)

## Applicabilité réglementaire

Les exigences réglementaires sont catégorisées conformément à **ISMS-POL-00 (Cadre d'applicabilité réglementaire)**.

**Niveau 1 : Conformité obligatoire**

| Réglementation | Applicabilité | Exigences clés |
|----------------|---------------|----------------|
| **CO suisse art. 728** | Toutes les entités suisses | Système de contrôle interne incluant la séparation des fonctions |
| **ISO/IEC 27001:2022** | Périmètre de certification | Contrôle A.5.3 — Séparation des fonctions |

**Niveau 2 : Applicabilité conditionnelle**

S'applique uniquement lorsque des conditions commerciales spécifiques déclenchent l'applicabilité :

| Réglementation | Condition déclenchante | Exigences de séparation |
|----------------|------------------------|-------------------------|
| **RGPD UE art. 32** | Traitement de données personnelles de l'UE | Mesures techniques et organisationnelles appropriées |
| **FINMA** | Établissement financier réglementé suisse | Séparation stricte dans les activités de trading, règlement et gestion des risques |
| **SOX Section 404** | Société cotée aux États-Unis | Séparation des contrôles financiers, attestation du contrôle interne |
| **PCI DSS v4.0.1** | Traitement de cartes de paiement | Exigence 6.4.2 — Séparation des environnements développement/test/production |

**Niveau 3 : Référentiels informatifs**

Ces cadres guident la mise en œuvre mais ne constituent pas une obligation de conformité sauf exigence contractuelle :

- Cadre de contrôle interne COSO
- ISACA COBIT (Objectifs de contrôle pour l'informatique)
- NIST SP 800-53 (Contrôle d'accès AC-5)
- Normes internationales de l'IIA (séparation en audit interne)

**Détermination de la conformité** : [Organisation] détermine les réglementations de niveau 2 applicables par le biais d'évaluations périodiques de ses activités. Les exigences les plus strictes s'appliquent lorsque plusieurs réglementations se recoupent.

---

# Énoncés de politique

## Principes de séparation

Tous les processus métier et systèmes d'information DOIVENT mettre en œuvre la séparation des fonctions lorsque :

**Exigence fondée sur le risque** :

- Les activités impliquent des transactions financières **supérieures à CHF 10 000**, sauf si un seuil inférieur est défini dans une procédure départementale approuvée par le DAF et le RSSI sur la base d'une évaluation des risques
- L'accès à des informations sensibles ou classifiées est requis
- Des privilèges d'administration des systèmes sont exercés
- Des contrôles de sécurité peuvent être contournés ou désactivés
- Des journaux d'audit ou des éléments de preuve peuvent être modifiés ou supprimés

**Normes minimales de séparation** :

| Type de processus | Séparation minimale |
|-------------------|---------------------|
| Transactions financières > CHF 10 000 | Initiateur ≠ Approbateur |
| Demandes d'accès aux systèmes | Demandeur ≠ Approbateur ≠ Provisionnant |
| Gestion des changements | Développeur ≠ Testeur ≠ Déployeur |
| Surveillance de la sécurité | Administrateur ≠ Réviseur des journaux |
| Sauvegarde/Restauration | Opérateur ≠ Vérificateur |

## Identification des fonctions conflictuelles

Les combinaisons de fonctions suivantes DOIVENT être séparées :

**Processus financiers** :

- Initier des paiements ET approuver des paiements
- Créer des enregistrements fournisseurs ET traiter des paiements à ces fournisseurs
- Enregistrer des transactions ET réconcilier des comptes
- Gérer la paie ET approuver les versements de salaires

**Opérations informatiques** :

- Développer du code ET le déployer en production
- Administrer des systèmes ET examiner les journaux système
- Créer des comptes utilisateurs ET approuver les demandes d'accès
- Gérer les sauvegardes ET autoriser la restauration des données
- Configurer les contrôles de sécurité ET auditer l'efficacité de la sécurité

**Achats et contrats** :

- Sélectionner des fournisseurs ET négocier des contrats
- Approuver des achats ET réceptionner des biens/services
- Gérer des contrats ET vérifier la conformité contractuelle

**Ressources humaines** :

- Décisions d'embauche ET vérification des antécédents
- Définir les rémunérations ET approuver la paie
- Révoquer des accès ET confirmer la révocation des accès

## Considérations pour les petites équipes

Lorsque la séparation ne peut être obtenue en raison d'un nombre limité de personnel :

**Contrôles compensatoires requis** :

1. Surveillance renforcée et journalisation de toutes les activités
2. Revue managériale de toutes les transactions (minimum hebdomadaire)
3. Revue indépendante périodique (minimum trimestrielle)
4. Alertes automatisées pour les schémas inhabituels
5. Pistes d'audit post-transaction avec protection contre la falsification

**Exigence documentaire** : Acceptation formelle du risque résiduel par la direction générale, avec documentation des contrôles compensatoires et du calendrier de révision.

**Déclencheur de réévaluation** : Les dispositifs de contrôles compensatoires DOIVENT être réévalués lorsque :

- Du personnel supplémentaire est recruté
- La structure organisationnelle change
- L'évaluation des risques identifie une exposition accrue
- Les conclusions d'audit révèlent des faiblesses de contrôle

## Contrôles techniques de séparation

Les systèmes d'information supportant des processus séparés DOIVENT mettre en œuvre :

**Exigences de contrôle d'accès** :

- Contrôle d'accès basé sur les rôles (RBAC) appliquant la séparation des fonctions
- Contraintes d'exclusion mutuelle empêchant l'attribution de rôles conflictuels
- Contrôles de flux de travail exigeant des approbateurs différents à chaque étape
- Gestion des accès privilégiés empêchant l'auto-approbation

**Exigences de piste d'audit** :

- Journalisation immuable de toutes les activités séparées
- Identification claire des acteurs à chaque étape du processus
- Enregistrement de l'horodatage et des actions pour toutes les approbations
- Protection contre la modification ou la suppression des journaux

**Définition de la journalisation immuable** : La journalisation immuable DOIT être réalisée en utilisant des plateformes et configurations de journalisation approuvées, telles que définies dans ISMS-IMP-A.5.3 et dans le contrôle de journalisation (ISMS-POL-A.8.15). Les implémentations acceptables incluent : le stockage WORM, l'accès administrateur restreint avec réviseur de journaux distinct, les verrous de rétention et l'agrégation centralisée des journaux avec vérification d'intégrité.

## Gestion des dérogations

Les dérogations aux exigences de séparation requièrent :

**Dérogations d'urgence** (≤ 24 heures) :

- Autorisation verbale du responsable de département + RSSI
- Documentation dans les 4 heures suivant l'utilisation de la dérogation
- Revue complète dans les 24 heures suivant la fin de la dérogation
- Contrôles compensatoires actifs pendant la période de dérogation

**Dérogations planifiées** (> 24 heures) :

- Demande de dérogation formelle avec justification métier
- Évaluation des risques liés à l'impact de la dérogation
- Contrôles compensatoires documentés et approuvés
- Approbation du RSSI et de la direction générale
- Durée maximale : 90 jours (renouvelable avec réévaluation)

**Non autorisé** :

- Dérogations permanentes aux exigences de séparation financière
- Dérogations éliminant les capacités de piste d'audit
- Auto-approbation des dérogations à la séparation

Toutes les dérogations DOIVENT être consignées dans le registre des dérogations (ISMS-REG-EXCEPTIONS).

**Contenu minimal d'un enregistrement de dérogation** : Chaque enregistrement de dérogation DOIT inclure : le(s) système(s) concerné(s), l'identité/le(s) rôle(s) bénéficiaire(s) de la dérogation, la fenêtre temporelle (début/fin), l'autorité approbatrice avec justificatif, les contrôles compensatoires actifs pendant la dérogation, le résultat de la revue post-dérogation et la date de clôture.

---

# Rôles et responsabilités

## Matrice de responsabilités

| Rôle | Responsabilités en matière de séparation |
|------|------------------------------------------|
| **Direction générale** | Approuver la politique de séparation, accepter les risques résiduels, approuver les contrôles compensatoires |
| **RSSI** | Définir les exigences de séparation, surveiller la conformité, approuver les dérogations |
| **DAF** | Supervision de la séparation des processus financiers, approbation des dérogations aux contrôles financiers |
| **Responsables de département** | Mettre en œuvre la séparation au sein des départements, identifier les conflits, demander des dérogations |
| **RH** | Maintenir la structure organisationnelle supportant la séparation, gestion des attributions de rôles |
| **Opérations informatiques** | Mettre en œuvre les contrôles techniques, configuration RBAC, surveillance des accès |
| **Audit interne** | Vérifier l'efficacité de la séparation, signaler les violations, évaluer les contrôles compensatoires |

## Voie d'escalade

- Conflits de séparation identifiés : Responsable de département → RSSI → Direction générale
- Demandes de dérogation : Demandeur → Responsable de département → RSSI → Direction générale
- Violation détectée : Notification immédiate au RSSI et à l'audit interne

---

# Gouvernance et conformité

## Cadre d'évaluation

| Évaluation | Fréquence | Responsable | Éléments de preuve |
|------------|-----------|-------------|---------------------|
| Révision de la matrice de séparation | Annuelle | RSSI | Matrice des fonctions mise à jour |
| Analyse des droits d'accès | Trimestrielle | Opérations informatiques | Rapports d'accès |
| Revue des contrôles compensatoires | Trimestrielle | Audit interne | Évaluation d'efficacité |
| Revue du registre des dérogations | Mensuelle | RSSI | Journal des dérogations |

**Surveillance de la conformité** :

- Revues des droits d'accès par rapport à la matrice de séparation des fonctions
- Analyse des schémas de transactions pour détecter les violations de séparation
- Vérification des chaînes d'approbation des flux de travail
- Revue de l'efficacité des contrôles compensatoires

**Métriques de gouvernance** :

- Nombre de conflits de séparation identifiés
- Délai de remédiation des conflits
- Demandes et approbations de dérogations
- Scores d'efficacité des contrôles compensatoires

## Révision de la politique

- **Fréquence** : Annuelle au minimum
- **Déclencheurs** : Restructuration organisationnelle, conclusions d'audit, mises à jour réglementaires, incidents de sécurité
- **Réviseurs** : RSSI, DAF, audit interne, directeur des ressources humaines (DRH)
- **Approbation** : Direction générale

## Lien avec les actions correctives

Les non-conformités relatives à cette politique (p. ex. violations de la séparation, dérogations non révisées, défaillances de contrôles compensatoires) DOIVENT être enregistrées et gérées dans le cadre du processus d'action corrective du SMSI (clause 10.2), avec analyse des causes profondes et suivi de la remédiation.

---

# Mise en œuvre et références

## Intégration avec le SMSI

Cette politique s'intègre dans le Système de management de la sécurité de l'information de [Organisation] :

**Évaluation des risques** (clause 6.1 de l'ISO 27001) :

- Exigences de séparation informées par l'évaluation des risques de fraude et d'erreur
- Contrôles compensatoires documentés dans les plans de traitement des risques
- Risques résiduels résultant d'une séparation limitée formellement acceptés

**Déclaration d'applicabilité** (clause 6.1.3 de l'ISO 27001) :

- Applicabilité du contrôle A.5.3 justifiée dans la DdA de [Organisation]
- Statut de mise en œuvre suivi et reporté

**Contrôles connexes** :

| Contrôle | Relation |
|----------|----------|
| **A.5.15-16-18** | Gestion des identités et des accès — le RBAC applique la séparation des fonctions |
| **A.8.2-3-5** | Authentification et accès privilégiés — séparation des accès privilégiés |
| **A.8.15** | Journalisation — pistes d'audit pour les activités séparées |

## Ressources de mise en œuvre

**Guide de mise en œuvre** (ISMS-IMP-A.5.3) :

| Identifiant du document | Titre | Objet |
|-------------------------|-------|-------|
| **ISMS-IMP-A.5.3-UG/TG** | Guide de mise en œuvre de la séparation des fonctions | Matrices des fonctions, contrôles techniques, procédures de surveillance |

---

# Éléments de preuve pour cette politique

**Éléments de preuve pour l'Étape 1 (revue documentaire) :**

Les éléments de preuve requis pour l'étape 1 incluent :

- Ce document de politique (ISMS-POL-A.5.3 v1.0)
- Approbation enregistrée par le RSSI, le DAF et la direction générale
- Preuve de communication aux rôles concernés
- Identification des fonctions conflictuelles documentée (Identification des fonctions conflictuelles)
- Principes de séparation et normes minimales définis (Principes de séparation)
- Exigences de contrôles compensatoires précisées (Considérations pour les petites équipes)
- Processus de gestion des dérogations documenté (Gestion des dérogations)
- Rôles et responsabilités attribués (Rôles et responsabilités)

La présence et le statut des éléments de preuve sont suivis dans le registre des éléments de preuve du SMSI.

**Éléments de preuve pour l'Étape 2 (efficacité opérationnelle) :**

Éléments de preuve requis pour démontrer que cette politique est opérationnellement efficace :

- Matrice de séparation des fonctions présentant les combinaisons de rôles conflictuels
- Rapports sur les droits d'accès démontrant l'application de la séparation
- Exemples d'approbations de flux de travail illustrant le contrôle multipartite
- Registre des dérogations avec approbations et contrôles compensatoires
- Rapports trimestriels d'analyse de la séparation
- Rapports d'audit interne sur la conformité à la séparation
- Éléments de preuve de la surveillance des contrôles compensatoires (lorsque la séparation n'est pas réalisable)
- Relevés de formation du personnel sur les exigences de séparation
- Rapports d'incidents liés à des violations de la séparation (le cas échéant)

---

# Définitions

| Terme | Définition |
|-------|------------|
| **Séparation des fonctions (SdF)** | La pratique consistant à répartir les tâches et les privilèges entre plusieurs personnes afin d'empêcher qu'une seule personne dispose d'un contrôle total sur un processus critique |
| **Fonctions conflictuelles** | Responsabilités qui, si elles étaient combinées, permettraient à un individu de commettre et de dissimuler des erreurs ou des fraudes |
| **Contrôle compensatoire** | Mesure de contrôle alternative mise en œuvre lorsque la séparation primaire ne peut être obtenue |
| **Exclusion mutuelle** | Contrôle technique empêchant l'attribution simultanée de rôles conflictuels à un utilisateur |
| **Principe des quatre yeux** | Exigence selon laquelle les actions critiques doivent être approuvées ou vérifiées par au moins deux personnes habilitées |

---

# Enregistrement des approbations

| Rôle | Nom | Date |
|------|-----|------|
| **Responsable de la sécurité des systèmes d'information (RSSI)** | [Nom] | [Date à définir] |
| **Directeur administratif et financier (DAF)** | [Nom] | [Date à définir] |
| **Direction générale** | [Nom] | [Date à définir] |

---

**FIN DU DOCUMENT DE POLITIQUE**

---

*Cette politique établit les exigences en matière de séparation des fonctions. Les procédures de mise en œuvre sont documentées dans ISMS-IMP-A.5.3 (UG/TG).*

<!-- QA_VERIFIED: 2026-03-30 -->
