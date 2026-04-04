<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.5.3-FR:operational:OP-POL:a.5.3 -->
**ISMS-OP-POL-A.5.3 — Séparation des tâches**

---

**Contrôle documentaire**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Séparation des tâches |
| **Type de document** | Politique opérationnelle |
| **Identifiant du document** | ISMS-OP-POL-A.5.3 |
| **Créateur du document** | Responsable de la Sécurité des Systèmes d'Information (RSSI) |
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
| 1.0 | [Date] | RSSI | Politique opérationnelle initiale pour ISO 27001:2022 |

**Cycle de révision** : Annuel
**Prochaine date de révision** : [Effective Date + 12 months]

**Approuvé par** : [RSSI / Direction générale]

**Documents connexes** :

- ISO/IEC 27001:2022 Contrôle A.5.3 — Séparation des tâches
- ISO/IEC 27002:2022 Section 5.3 — Préconisations de mise en œuvre
- Code des obligations suisse Art. 728a — Système de contrôle interne
- NIST SP 800-53 Rév. 5 AC-5 — Séparation des tâches

**Contrôles Annexe A connexes** :

| Contrôle | Relation avec la séparation des tâches |
|----------|----------------------------------------|
| A.5.1 Politiques de sécurité de l'information | Référentiel de politique général régissant les exigences de SdT |
| A.5.2 Rôles et responsabilités en matière de sécurité de l'information | Définitions des rôles permettant la séparation des tâches |
| A.5.15 Contrôle des accès | Les règles de contrôle des accès appliquent les périmètres de séparation |
| A.5.16 Gestion des identités | Les identités uniques garantissent l'imputabilité individuelle |
| A.5.18 Droits d'accès | L'attribution des accès met en œuvre les contraintes d'exclusion mutuelle |
| A.8.2 Droits d'accès privilégiés | Les comptes privilégiés sont séparés des opérations standard |
| A.8.3 Restriction de l'accès à l'information | Application technique des règles de séparation |
| A.8.5 Authentification sécurisée | L'authentification vérifie l'identité de l'acteur à chaque étape du processus |
| A.8.15 Journalisation | Les pistes d'audit enregistrent les activités séparées à des fins de vérification |
| A.8.32 Gestion des changements | Le processus de changement impose la séparation développeur/testeur/déployeur |

**Politiques internes connexes** :

- Politique de gestion des identités et des accès
- Politique d'authentification et d'accès privilégiés
- Politique de gestion des changements
- Politique de journalisation
- Politique de classification et de traitement de l'information

---

# Politique de séparation des tâches

## Objectif

L'objectif de cette politique est de réduire le risque de fraude, d'erreur et de contournement des contrôles de sécurité de l'information en veillant à ce que les tâches conflictuelles et les domaines de responsabilité conflictuels soient répartis entre différentes personnes ou différents rôles. La séparation des tâches empêche toute personne d'exercer un contrôle de bout en bout sur un processus critique — de l'initiation à l'autorisation, de l'exécution à la vérification.

Cette politique soutient la nFADP suisse (revDSG) en mettant en œuvre des mesures organisationnelles adaptées aux risques afin de protéger l'intégrité du traitement des données personnelles. La séparation des tâches est un contrôle interne reconnu au sens du Code des obligations suisse Art. 728a, qui exige des entreprises soumises au contrôle ordinaire le maintien d'un système de contrôle interne. Lorsque l'organisation traite des données de personnes dans l'UE/EEE, les exigences du RGPD s'appliquent également.

## Périmètre d'application

Tous les employés, prestataires et utilisateurs tiers impliqués dans des processus métier où des tâches conflictuelles pourraient permettre des fraudes, des erreurs ou des violations de la sécurité si elles étaient réalisées par une seule personne.

Cela comprend :

- Les transactions financières, les approbations et les versements.
- L'administration des systèmes d'information, le développement et le déploiement.
- L'attribution, la révision et la révocation des accès.
- La surveillance de la sécurité, la revue des journaux et la réponse aux incidents.
- Les achats, la gestion des fournisseurs et l'administration des contrats.
- Les opérations de sauvegarde, de restauration et de récupération des données.

**Hors périmètre** : Les processus opérationnels non sensibles avec une supervision adéquate ; les processus entièrement automatisés avec des contrôles de séparation intégrés (lorsque la séparation est assurée par l'automatisation, la configuration des contrôles et les pistes d'audit doivent être validées au minimum annuellement par le RSSI ou le réviseur désigné).

## Principe directeur

Les tâches conflictuelles et les domaines de responsabilité conflictuels devraient être séparés. Lorsqu'une séparation complète n'est pas réalisable en raison de la taille de l'organisation, des contrôles compensatoires — incluant une surveillance renforcée, une revue par la direction, un audit indépendant et des pistes d'audit protégées contre la falsification — doivent être mis en œuvre et formellement documentés.

Toutes les décisions de séparation doivent être fondées sur le risque, en tenant compte de la valeur et de la classification des actifs concernés, du potentiel de perte financière ou d'atteinte à la réputation, et des exigences réglementaires.

---

## Définitions

| Terme | Définition |
|-------|-----------|
| **Séparation des tâches (SdT)** | La pratique consistant à diviser les tâches et les privilèges entre plusieurs personnes afin d'empêcher toute personne d'exercer un contrôle complet sur un processus critique |
| **Tâches conflictuelles** | Des responsabilités qui, si elles étaient réunies chez une même personne, permettraient à celle-ci de commettre et de dissimuler des erreurs ou des fraudes sans être détectée |
| **Contrôle compensatoire** | Une mesure de contrôle alternative mise en œuvre lorsque la séparation primaire ne peut être atteinte, offrant une réduction équivalente du risque |
| **Exclusion mutuelle** | Un contrôle technique empêchant un utilisateur de se voir attribuer simultanément des rôles conflictuels dans un système de contrôle des accès |
| **Principe des quatre yeux** | Une exigence selon laquelle les actions critiques nécessitent l'approbation ou la vérification d'au moins deux personnes autorisées avant exécution |
| **Matrice SdT** | Une cartographie documentée des rôles, des tâches et des conflits identifiés utilisée pour planifier et vérifier la séparation des tâches |

---

## Principes de séparation

Tous les processus métier et systèmes d'information doivent mettre en œuvre la séparation des tâches lorsque :

- Les activités impliquent des transactions financières **supérieures à CHF 10 000**, sauf si un seuil inférieur est défini dans une procédure départementale approuvée par le DAF et le RSSI sur la base d'une évaluation des risques.
- L'accès à des informations confidentielles ou restreintes est requis.
- L'administration de systèmes ou des accès privilégiés sont exercés.
- Des contrôles de sécurité peuvent être contournés, modifiés ou désactivés.
- Des journaux d'audit ou des éléments de preuve de conformité peuvent être modifiés ou supprimés.

**Détermination des seuils financiers** :
- **CHF 10 000** est le seuil de référence de l'organisation, établi sur la base d'une évaluation des risques tenant compte de la taille de l'organisation, du volume des transactions et de l'historique d'exposition à la fraude.
- Des seuils inférieurs peuvent être définis pour les catégories à haut risque (p. ex. CHF 5 000 pour les décaissements en espèces, CHF 2 000 pour les remboursements de frais des employés) par le DAF et le RSSI sur la base d'une évaluation des risques départementale.
- Des seuils supérieurs ne sont pas autorisés sans l'approbation de la Direction générale et la mise en place de contrôles compensatoires.

**Révision des seuils** : Les seuils financiers doivent être révisés annuellement par le DAF et le RSSI et ajustés en fonction de l'inflation, de la croissance organisationnelle et de la réévaluation du risque de fraude.

### Normes minimales de séparation

Les exigences minimales de séparation suivantes s'appliquent :

| Type de processus | Exigence minimale de séparation |
|------------------|---------------------------------|
| **Transactions financières** >CHF 10 000 | L'initiateur ne doit pas être l'approbateur |
| **Demandes d'accès système** | Le demandeur ne doit pas être l'approbateur ; l'approbateur ne doit pas être le provisionnant |
| **Gestion des changements** | Le développeur ne doit pas être le testeur ; le testeur ne doit pas être le déployeur |
| **Surveillance de la sécurité** | L'administrateur système ne doit pas être le réviseur des journaux |
| **Sauvegarde et restauration** | L'opérateur de sauvegarde ne doit pas être le vérificateur de restauration |

Lorsqu'une personne assume actuellement des tâches conflictuelles, le conflit doit être résolu dans les 30 jours calendaires suivant son identification — soit par réaffectation, exclusion mutuelle technique, soit par documentation formelle d'un contrôle compensatoire.

---

## Identification des tâches conflictuelles

L'organisation doit maintenir une matrice SdT documentée identifiant les combinaisons de tâches nécessitant une séparation. Les catégories suivantes constituent la référence de base :

### Processus financiers

Les combinaisons de tâches suivantes doivent être séparées :

- Initier des paiements ET approuver des paiements.
- Créer des fiches fournisseurs ET traiter des paiements à ces fournisseurs.
- Enregistrer des transactions ET réconcilier des comptes.
- Gérer la paie ET approuver les versements de paie.
- Préparer le budget ET approuver le budget.

### Opérations informatiques

Les combinaisons de tâches suivantes doivent être séparées :

- Développer du code ET le déployer en production.
- Administrer des systèmes ET réviser les journaux système.
- Créer des comptes utilisateurs ET approuver les demandes d'accès.
- Gérer les sauvegardes ET autoriser les restaurations de données.
- Configurer les contrôles de sécurité ET auditer leur efficacité.
- Gérer les règles de pare-feu ET réviser la conformité du pare-feu.

### Achats et contrats

Les combinaisons de tâches suivantes doivent être séparées :

- Sélectionner des fournisseurs ET négocier les contrats.
- Approuver les achats ET réceptionner les biens ou services.
- Gérer les contrats ET vérifier leur conformité.

### Ressources humaines

Les combinaisons de tâches suivantes doivent être séparées :

- Décisions d'embauche ET vérification du contrôle des antécédents.
- Fixation des rémunérations ET approbation de la paie.
- Résiliation des accès ET confirmation de la révocation des accès.

Les responsables de département doivent réviser annuellement la matrice SdT pour leur périmètre et signaler tout conflit nouvellement identifié au RSSI. Le RSSI doit maintenir la matrice SdT organisationnelle consolidée dans [GRC Tool] ou un registre équivalent.

> **Emplacement de la matrice SdT** : [Préciser : module GRC ServiceNow, Archer, MetricStream, registre SharePoint, ou « En cours de sélection ; provisoirement : registre Excel sur espace partagé contrôlé »]
>
> **Emplacement du Registre des exceptions** : [Même système que la matrice SdT ou préciser séparément]
>
> Lorsqu'un outil GRC dédié n'est pas encore déployé, l'organisation doit maintenir les registres dans un espace partagé contrôlé avec contrôle de version, journalisation des accès et vérification trimestrielle de l'intégrité par le RSSI.

---

## Contrôles compensatoires pour les petites équipes et les PME

Lorsque la séparation ne peut être pleinement réalisée en raison d'un effectif limité — situation fréquente dans les petites et moyennes organisations — des contrôles compensatoires doivent être mis en œuvre pour assurer une atténuation des risques équivalente.

### Contrôles compensatoires requis

Lorsque la séparation complète des tâches n'est pas réalisable, **les cinq** contrôles compensatoires suivants doivent être mis en œuvre pour chaque conflit identifié :

| N° | Contrôle compensatoire | Mise en œuvre |
|----|------------------------|---------------|
| 1 | **Surveillance et journalisation renforcées** | Toutes les activités dans le processus conflictuel doivent être journalisées avec des pistes d'audit immuables. Les journaux doivent capturer l'identité de l'utilisateur, l'action, l'horodatage et les enregistrements affectés |
| 2 | **Revue des transactions par la direction** | Un responsable ou un collègue senior non impliqué dans le processus doit réviser toutes les transactions au minimum hebdomadairement |
| 3 | **Revue périodique indépendante** | Une partie indépendante (audit interne, auditeur externe ou direction générale) doit réviser le processus au minimum trimestriellement |
| 4 | **Alertes automatisées pour les anomalies** | Le [SIEM] ou un système de surveillance équivalent doit générer des alertes pour les schémas inhabituels tels que les transactions hors des heures normales, les montants dépassant les seuils ou les opérations en masse |
| 5 | **Piste d'audit post-transaction avec protection contre la falsification** | Les enregistrements de transactions doivent être stockés de manière à empêcher leur modification ou suppression par la personne ayant effectué la transaction |

### Périmètre de la revue indépendante périodique (Contrôle compensatoire n° 3)

Une partie indépendante doit réviser le processus **trimestriellement** au minimum. La revue doit porter sur :

**Périmètre de la revue** :
- **Transactions par échantillonnage** (minimum 10 % du volume des transactions ou 20 transactions, selon le chiffre le plus élevé).
- **Vérification de la piste d'audit** (confirmer que toutes les activités sont journalisées ; journaux immuables).
- **Complétion des revues de direction** (vérifier que les revues hebdomadaires de la direction ont eu lieu avec une validation documentée).
- **Détection des anomalies** (vérifier le fonctionnement des alertes automatisées ; réviser les alertes déclenchées et leur résolution).
- **Conformité au processus** (confirmer que le processus est suivi tel que documenté).

**Documentation de la revue** : Chaque revue trimestrielle doit produire un rapport écrit documentant le périmètre, les constats, les problèmes identifiés et les recommandations. Les rapports sont conservés pendant 3 ans.

**Escalade des problèmes** : Les problèmes identifiés lors de la revue indépendante doivent être escaladés au RSSI dans les 5 jours ouvrables et résolus dans les 30 jours calendaires.

### Exigence de documentation

Chaque dispositif de contrôles compensatoires doit être formellement documenté avec :

- Les tâches conflictuelles spécifiques qui ne peuvent être séparées.
- La justification métier de l'impossibilité de séparation.
- Les contrôles compensatoires en place (les cinq ci-dessus).
- L'acceptation formelle du risque signée par la Direction générale.
- Un calendrier de révision défini (trimestriel au minimum).

La documentation des contrôles compensatoires doit être tenue dans [GRC Tool] ou un registre équivalent accessible au RSSI et à l'Audit interne.

### Déclencheurs de réévaluation

Les dispositifs de contrôles compensatoires doivent être réévalués lorsque :

- Du personnel supplémentaire est embauché et pourrait assumer des tâches séparées.
- La structure organisationnelle change.
- L'évaluation des risques identifie une exposition accrue.
- Les résultats d'audit indiquent des faiblesses de contrôle.
- Un incident de sécurité survient dans le périmètre des contrôles compensatoires.

### Vérification de l'efficacité des contrôles compensatoires

L'efficacité des contrôles compensatoires doit être vérifiée par :

**Revue indépendante trimestrielle** (Contrôle compensatoire n° 3) :
- Vérifier que les cinq contrôles compensatoires fonctionnent comme documenté.
- Échantillonner les transactions pour confirmer l'intégrité de la piste d'audit.
- Confirmer la complétion des revues de direction avec validation documentée.
- Tester la configuration des alertes automatisées et la réponse apportée.

**Évaluation annuelle de l'efficacité** par le RSSI :
- Réviser tous les dispositifs de contrôles compensatoires.
- Évaluer si les contrôles atténuent adéquatement le risque de séparation.
- Identifier les opportunités d'atteindre une séparation complète (p. ex. un nouvel embauché peut assumer une tâche séparée).
- Mettre à jour la documentation d'acceptation des risques.

**Défaillance d'un contrôle compensatoire** : Si un contrôle compensatoire s'avère inefficace, notification immédiate à la Direction générale et remédiation dans les 14 jours calendaires ou réacceptation formelle du risque résiduel.

---

## Contrôles techniques de séparation

Les systèmes d'information supportant les processus séparés doivent mettre en œuvre les contrôles techniques suivants :

> **Système de journalisation et de surveillance** : [Préciser : Splunk, Elastic SIEM, Azure Sentinel, ou « Sélection en cours ; provisoirement : journalisation centralisée vers un serveur syslog avec revue manuelle »]
>
> **Fournisseur d'identité** : [Préciser : Azure AD, Okta, Google Workspace, ou « Active Directory sur site »]
>
> **ERP/Système financier** : [Préciser : SAP, Oracle, NetSuite, ou le système applicable]
>
> Lorsque des systèmes sont en cours de sélection ou de transition, documenter l'approche provisoire et la date de déploiement cible.

### Application du contrôle des accès

- **Contrôle d'accès basé sur les rôles (RBAC)** : Les rôles doivent être définis dans le fournisseur d'identité ou l'application pour assurer la séparation des tâches. Les rôles conflictuels doivent être documentés comme mutuellement exclusifs.
- **Contraintes d'exclusion mutuelle** : Le système de contrôle des accès ([Fournisseur d'identité / ERP / HR System]) doit empêcher un utilisateur unique de détenir simultanément des rôles conflictuels. Lorsque le système ne prend pas nativement en charge l'exclusion mutuelle, une revue manuelle doit être effectuée à chaque événement d'attribution d'accès.
- **Contrôles de flux de travail** : Les processus métier à plusieurs étapes doivent requérir différentes personnes autorisées à chaque étape d'approbation. L'auto-approbation doit être techniquement bloquée dans la mesure du possible et est interdite par politique dans tous les cas.
- **Gestion des accès privilégiés** : Les comptes privilégiés doivent être distincts des comptes standard. Aucune personne ne doit approuver ses propres demandes d'accès élevé.

**Vérification des contraintes d'exclusion mutuelle** :
- **Systèmes automatisés** : Les contraintes d'exclusion mutuelle doivent être testées **annuellement** en tentant d'attribuer des rôles conflictuels à un utilisateur de test et en vérifiant que le système bloque l'attribution. Les résultats des tests sont documentés.
- **Systèmes à revue manuelle** : Les listes de contrôle d'attribution des accès doivent inclure une vérification des conflits SdT avec une validation documentée avant l'octroi de l'accès. Le provisionnant doit se référer à la matrice SdT et confirmer l'absence de conflits.
- **Revue trimestrielle des accès** : Toutes les attributions de rôles utilisateur doivent être comparées à la matrice SdT pour détecter tout conflit ayant contourné les contrôles de provisionnement. Les constats sont résolus dans les 30 jours calendaires.

### Exigences relatives aux pistes d'audit

- **Journalisation immuable** : Toutes les activités dans les processus séparés doivent être journalisées vers une plateforme de journalisation centralisée ([SIEM] ou équivalent) que les participants au processus ne peuvent modifier ou supprimer.
- **Identification de l'acteur** : Les journaux doivent identifier clairement la personne effectuant chaque action à chaque étape du processus.
- **Enregistrement de l'horodatage et de l'action** : Toutes les approbations, modifications et complétions de processus doivent être enregistrées avec des horodatages précis.
- **Protection des journaux** : Les journaux d'audit doivent être protégés contre toute modification ou suppression conformément à la Politique de journalisation. Les mises en œuvre acceptables incluent le stockage en écriture seule, l'accès administrateur restreint avec réviseur de journaux séparé, les verrous de conservation ou l'agrégation centralisée des journaux avec vérification de l'intégrité.

---

## Gestion des exceptions

Les exceptions aux exigences de séparation doivent être gérées par un processus formel. L'auto-approbation des exceptions de séparation n'est jamais autorisée.

### Exceptions d'urgence (durée de 24 heures ou moins)

Lorsque l'urgence opérationnelle nécessite de contourner temporairement les contrôles de séparation :

1. **Autorisation verbale** du Responsable de département et du RSSI (ou de son délégué) — enregistrer qui a autorisé, quand et l'exception spécifique accordée.
2. **Documentée dans les 4 heures** suivant l'utilisation de l'exception via [emergency exception form / ticket system / email to RSSI] incluant :
   - Identifiant de l'exception (identifiant unique).
   - Nom et rôle du demandeur.
   - Personnes ayant autorisé verbalement (noms, heure d'autorisation).
   - Justification métier (urgence opérationnelle spécifique).
   - Exception accordée (tâches spécifiques combinées ; durée).
   - Actions effectuées pendant la période d'exception.
   - Contrôles compensatoires actifs (surveillance renforcée, revue post-immédiate).
3. **Revue complète dans les 24 heures** suivant la fin de l'exception — le RSSI ou son délégué vérifie que les contrôles compensatoires ont été efficaces et qu'aucune irrégularité ne s'est produite. La validation de la revue est documentée.
4. **Contrôles compensatoires actifs** pendant la période d'exception — surveillance renforcée et revue post-activité au minimum.

**Journal des exceptions d'urgence** : Toutes les exceptions d'urgence doivent être enregistrées dans le Registre des exceptions avec un indicateur « Urgence ».

### Exceptions planifiées (durée supérieure à 24 heures)

Lorsqu'une exception de plus longue durée est nécessaire (p. ex. absence de personnel, contraintes de projet) :

1. **Demande d'exception formelle** soumise au RSSI avec justification métier.
2. **Évaluation des risques** liés à l'impact de l'exception sur la prévention des fraudes et des erreurs.
3. **Contrôles compensatoires** documentés et approuvés avant la prise d'effet de l'exception.
4. **Approbation du RSSI et de la Direction générale** — les deux sont requises.
5. **Durée maximale** : 90 jours calendaires. Le renouvellement nécessite une réévaluation et une nouvelle approbation.

### Exceptions non autorisées

Les exceptions suivantes ne doivent être accordées en aucune circonstance :

- Exceptions permanentes aux exigences de séparation financière.
- Exceptions éliminant ou contournant les capacités de piste d'audit.
- Auto-approbation de sa propre exception de séparation.

### Registre des exceptions

Toutes les exceptions doivent être enregistrées dans le Registre des exceptions tenu dans [GRC Tool] ou équivalent. Chaque enregistrement doit comprendre :

- Le(s) système(s) et processus concernés.
- L'identité et le(s) rôle(s) bénéficiant de l'exception.
- La fenêtre temporelle (date de début et date de fin).
- L'autorité approbatrice avec preuve d'approbation.
- Les contrôles compensatoires actifs pendant l'exception.
- Le résultat de la revue post-exception.
- La date de clôture.

Le RSSI doit réviser le Registre des exceptions mensuellement et rapporter les exceptions actives à la Direction générale trimestriellement.

---

## Maintenance de la matrice SdT

### Révision annuelle

La matrice SdT organisationnelle doit être révisée et mise à jour annuellement. La révision doit :

- Confirmer que tous les conflits documentés restent valides et complets.
- Identifier les nouveaux conflits découlant de changements organisationnels, de nouveaux systèmes ou de nouveaux processus.
- Vérifier que les contrôles compensatoires restent efficaces pour les conflits non résolus.
- Mettre à jour la matrice pour refléter la structure organisationnelle actuelle.

### Vérification trimestrielle des droits d'accès

Les Opérations informatiques doivent générer des rapports d'accès trimestriellement à partir du fournisseur d'identité et des systèmes d'accès aux applications. Le RSSI doit comparer ces rapports à la matrice SdT pour vérifier :

- Qu'aucune personne ne détient des rôles conflictuels dans les systèmes de production.
- Que les contraintes d'exclusion mutuelle fonctionnent correctement.
- Que les nouvelles attributions de rôles depuis la dernière révision ne créent pas de conflits non documentés.

Les constats doivent être documentés et les conflits résolus dans les 30 jours calendaires suivant leur découverte.

---

## Rôles et responsabilités

| Rôle | Responsabilités en matière de séparation des tâches |
|------|------------------------------------------------------|
| **Direction générale** | Approuve la politique de séparation ; accepte les risques résiduels ; approuve les contrôles compensatoires ; approuve les exceptions planifiées |
| **RSSI** | Définit et maintient la matrice SdT ; surveille la conformité ; approuve les exceptions d'urgence et planifiées ; révise le Registre des exceptions mensuellement |
| **DAF** | Supervise la séparation des processus financiers ; approuve les exceptions de contrôle financier conjointement avec le RSSI ; fixe les ajustements des seuils financiers |
| **Responsables de département** | Mettent en œuvre la séparation au sein des départements ; identifient les nouveaux conflits ; demandent des exceptions ; assurent la revue hebdomadaire de la direction des zones de contrôles compensatoires |
| **RH** | Maintient la structure organisationnelle supportant la séparation ; notifie l'informatique des changements de rôle affectant les attributions de tâches |
| **Opérations informatiques** | Met en œuvre les contrôles techniques (RBAC, exclusion mutuelle, flux de travail) ; génère les rapports d'accès trimestriels ; maintient les pistes d'audit |
| **Audit interne** | Vérifie l'efficacité de la séparation ; évalue l'adéquation des contrôles compensatoires ; signale les violations ; conduit les revues indépendantes trimestrielles |

### Chemin d'escalade

- **Conflits de séparation identifiés** : Le Responsable de département notifie le RSSI. Le RSSI escalade à la Direction générale si la résolution nécessite un changement organisationnel.
- **Demandes d'exception** : Le demandeur soumet au Responsable de département. Le Responsable de département soumet au RSSI. Le RSSI obtient l'approbation de la Direction générale pour les exceptions planifiées.
- **Violation détectée** : Notification immédiate au RSSI et à l'Audit interne. Investigation initiée dans les 24 heures.

### Processus d'investigation des violations

Lorsqu'une violation de séparation est détectée :

1. **Notification immédiate** au RSSI et à l'Audit interne (dans les 4 heures suivant la détection).
2. **Investigation initiée** dans les 24 heures par l'Audit interne ou l'enquêteur désigné par le RSSI.
3. **Périmètre de l'investigation** :
   - Déterminer si la violation était fortuite (mauvaise configuration système, erreur d'attribution d'accès) ou intentionnelle.
   - Réviser toutes les transactions effectuées pendant la période de violation.
   - Évaluer si une fraude ou une erreur s'est produite.
   - Identifier la cause profonde (défaillance du processus, lacune de formation, contournement intentionnel).
4. **Délai d'investigation** : À compléter dans les 10 jours ouvrables pour les violations administratives ; dans les 5 jours ouvrables pour les fraudes suspectées.
5. **Remédiation** : Révocation immédiate de l'accès si la violation est en cours ; plan d'action correctif dans les 14 jours calendaires.
6. **Reporting** : Rapport d'investigation au RSSI, au DAF et à la Direction générale (pour les violations financières ou les fraudes suspectées).

**Mesures disciplinaires** : Conformément à la section Non-conformité de la politique et aux procédures disciplinaires de l'organisation.

---

## Formation et sensibilisation

**Formation annuelle de sensibilisation à la SdT** à destination de tous les employés couvrant :
- L'objectif de la séparation des tâches (prévention de la fraude et des erreurs).
- Des exemples de tâches conflictuelles (financières, informatiques, achats).
- Les responsabilités individuelles (ne pas approuver son propre travail, signaler les conflits).
- Le processus d'exception (comment demander des exceptions correctement).
- Les conséquences des violations de la SdT (mesures disciplinaires, implications potentielles de fraude).

**Formation spécifique par rôle** :
- **Responsables de département** : Procédures de revue hebdomadaire de la direction pour les zones de contrôles compensatoires ; comment identifier les nouveaux conflits.
- **Opérations informatiques** : Configuration RBAC, mise en œuvre de l'exclusion mutuelle, protection des pistes d'audit.
- **Équipe financière** : Exigences de séparation financière, conformité au flux de travail d'approbation.

Suivi de la complétion des formations ; cible : **100 % des employés ayant des responsabilités de séparation formés annuellement**.

---

## Éléments de preuve

Les éléments de preuve suivants démontrent la conformité avec cette politique :

| N° | Élément de preuve | Responsable | Fréquence |
|----|-------------------|-------------|-----------|
| 1 | **Matrice SdT** documentant toutes les combinaisons de tâches conflictuelles identifiées et leur statut de séparation | RSSI | *Révisée annuellement ; mise à jour lors des changements organisationnels* |
| 2 | **Rapports de droits d'accès** montrant les attributions de rôles dans les systèmes, vérifiées par rapport à la matrice SdT | Opérations informatiques | *Générés trimestriellement ; révisés par le RSSI* |
| 3 | **Registre des contrôles compensatoires** avec validation d'acceptation des risques signée par la Direction générale | RSSI | *Révisé trimestriellement ; mis à jour lors des événements déclencheurs* |
| 4 | **Registre des exceptions** avec preuves d'approbation, contrôles compensatoires et enregistrements de clôture | RSSI | *Révisé mensuellement ; rapporté trimestriellement à la Direction générale* |
| 5 | **Registres de revue de direction** pour les zones de contrôles compensatoires (revues hebdomadaires des transactions) | Responsables de département | *Hebdomadaire ; conservés pendant 3 ans* |
| 6 | **Rapports de revue indépendante** pour les zones où la séparation n'est pas réalisable | Audit interne | *Trimestriel ; conservés pendant 3 ans* |
| 7 | **Éléments de preuve de configuration RBAC** montrant les contraintes d'exclusion mutuelle dans les systèmes de contrôle des accès | Opérations informatiques | *Capturés annuellement ou lors de changements ; conservés pendant 3 ans* |
| 8 | **Enregistrements d'approbation de flux de travail** montrant le contrôle multi-parties pour les transactions financières et les changements système | Opérations informatiques | *Par transaction ; conservés selon le calendrier de conservation* |
| 9 | **Enregistrements de vérification de l'intégrité des journaux d'audit** pour la journalisation des processus séparés | Opérations informatiques | *Mensuel ; conservés pendant 3 ans* |
| 10 | **Validation de la revue annuelle de la matrice SdT** et matrice mise à jour | RSSI | *Annuellement ; conservés pendant 3 ans* |

---

# Conformité à la politique

## Mesure de la conformité

L'équipe de management de la sécurité de l'information vérifiera la conformité à cette politique par diverses méthodes, notamment les revues de la matrice SdT, l'analyse des droits d'accès par rapport à la matrice des conflits, les évaluations de l'efficacité des contrôles compensatoires, les audits du registre des exceptions, les audits internes et externes, et les retours au propriétaire de la politique.

Les métriques suivantes doivent être suivies et rapportées au RSSI trimestriellement :

| Métrique | Cible | Seuil d'alerte |
|----------|-------|----------------|
| Conflits de séparation identifiés et documentés | 100 % des processus révisés | <80 % de couverture |
| Délai de résolution des conflits identifiés | 30 jours calendaires | >60 jours calendaires |
| Exceptions actives | Réduites au minimum ; tendance à la baisse | >5 simultanées ou toute exception >90 jours |
| Complétion des revues trimestrielles des contrôles compensatoires | 100 % | <80 % |
| Révision annuelle de la matrice SdT complétée dans les délais | Oui | En retard >30 jours |

**Exigences de reporting** :
- **Tableau de bord mensuel du RSSI** : Statut du Registre des exceptions, exceptions actives, résolutions de conflits en retard.
- **Rapport trimestriel à la Direction générale** : Statut des métriques, analyse des tendances (conflits résolus vs. nouveaux conflits identifiés), évaluation de l'efficacité des contrôles compensatoires.
- **Revue de direction annuelle** : Évaluation complète de l'efficacité du programme SdT incluant les tendances des métriques, les constats significatifs et les recommandations d'amélioration.

Les métriques dépassant les seuils d'alerte doivent être escaladées au RSSI pour traitement immédiat et rapportées lors de la prochaine Revue de direction.

## Exceptions

Toute exception à cette politique doit être approuvée et enregistrée par le RSSI au préalable, avec une acceptation documentée des risques, des contrôles compensatoires et une date de révision définie. Les exceptions planifiées nécessitent une approbation conjointe du RSSI et de la Direction générale. Les exceptions doivent être rapportées à l'Équipe de Revue de Direction. Les exceptions permanentes à la séparation financière et les exceptions éliminant les capacités de piste d'audit ne sont pas autorisées.

## Non-conformité

Un employé reconnu coupable d'avoir enfreint cette politique peut faire l'objet de mesures disciplinaires pouvant aller jusqu'au licenciement. Les violations de séparation impliquant des processus financiers doivent être signalées au DAF et peuvent déclencher une investigation complémentaire dans le cadre des procédures de réponse à la fraude de l'organisation.

## Amélioration continue

Cette politique est révisée et mise à jour dans le cadre du processus d'amélioration continue. Les révisions doivent prendre en compte les changements de structure organisationnelle, les nouveaux systèmes ou processus, les résultats d'audit, les évolutions réglementaires, les tendances des exceptions, l'efficacité des contrôles compensatoires et les leçons tirées des incidents liés à la séparation. Les non-conformités relatives à cette politique doivent être enregistrées et gérées par le processus d'action corrective du SMSI (Clause 10.2) avec une analyse des causes profondes et un suivi de la remédiation.

---

# Domaines de la norme ISO 27001 traités

Politique de séparation des tâches — Correspondance avec les contrôles ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership et engagement | 5.1 Politiques de sécurité de l'information |
| Clause 5.2 Politique | 5.2 Rôles et responsabilités en matière de sécurité de l'information |
| Clause 5.3 Rôles, responsabilités et autorités au sein de l'organisation | **5.3 Séparation des tâches** |
| Clause 6.1 Actions face aux risques et opportunités | 5.4 Responsabilités de la direction |
| Clause 7.3 Sensibilisation | 5.15 Contrôle des accès |
| Clause 8.1 Planification et contrôle opérationnels | 5.16 Gestion des identités |
| Clause 9.1 Surveillance, mesure, analyse et évaluation | 5.18 Droits d'accès |
| Clause 10.2 Non-conformité et action corrective | 8.2 Droits d'accès privilégiés |
| | 8.3 Restriction de l'accès à l'information |
| | 8.15 Journalisation |

**Cadre réglementaire et légal** :

| Référentiel | Pertinence |
|-------------|-----------|
| nFADP suisse (revDSG) | Art. 8 — Mesures techniques et organisationnelles (la séparation des tâches comme mesure organisationnelle protégeant l'intégrité du traitement des données) |
| DSV suisse (Ordonnance sur la protection des données) | Art. 1–3 — Exigences minimales pour la sécurité des données |
| CO suisse Art. 728a | Système de contrôle interne — les auditeurs examinent l'existence du SCI incluant les contrôles de séparation des tâches |
| RGPD (le cas échéant) | Art. 32 — Sécurité du traitement (mesures techniques et organisationnelles appropriées) |
| ISO/IEC 27001:2022 | Contrôle Annexe A 5.3 — Séparation des tâches |
| ISO/IEC 27002:2022 | Section 5.3 — Préconisations de mise en œuvre pour la séparation des tâches |
| NIST SP 800-53 Rév. 5 | AC-5 (Séparation des tâches) — Division des fonctions de mission entre différentes personnes ou rôles |
| CIS Controls v8 | Contrôle 5 (Gestion des comptes) et Contrôle 6 (Gestion du contrôle des accès) — Mesures de protection supportant la séparation des tâches par la gouvernance des accès |
| Référentiel de contrôle interne COSO | Principe 10 — La séparation des tâches comme composante des activités de contrôle |

---

<!-- QA_VERIFIED: 2026-03-29 -->
