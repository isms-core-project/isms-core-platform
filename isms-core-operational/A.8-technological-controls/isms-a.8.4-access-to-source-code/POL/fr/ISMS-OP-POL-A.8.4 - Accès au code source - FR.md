<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.8.4-FR:operational:OP-POL:a.8.4 -->
**ISMS-OP-POL-A.8.4 — Accès au code source**

---

**Contrôle documentaire**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Accès au code source |
| **Type de document** | Politique opérationnelle |
| **Identifiant du document** | ISMS-OP-POL-A.8.4 |
| **Créateur du document** | Responsable de la sécurité des systèmes d'information (RSSI) |
| **Propriétaire du document** | Directeur général (DG) |
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
**Prochaine date de révision** : [Date d'entrée en vigueur + 12 mois]

**Approuvé par** : [RSSI / Direction générale]

**Documents associés** :

- ISO/IEC 27001:2022 Contrôle A.8.4 — Accès au code source
- ISO/IEC 27002:2022 Section 8.4 — Recommandations de mise en œuvre pour le contrôle d'accès au code source
- NIST SP 800-218 — Cadre de développement logiciel sécurisé (SSDF) v1.1
- CIS Controls v8 — Mesure de sécurité 16.1–16.14 (Sécurité des applications logicielles)

**Contrôles Annexe A associés** :

| Contrôle | Relation avec l'accès au code source |
|----------|--------------------------------------|
| A.5.9 Inventaire des informations et autres actifs associés | Les dépôts de code source sont inclus dans l'inventaire des actifs |
| A.5.15–16–18 Gestion des identités et des accès | Cadre GIA fondamental ; authentification et autorisation pour les dépôts |
| A.5.19–23 Sécurité des fournisseurs et des services cloud | Accès des développeurs tiers et contrôles des dépôts cloud |
| A.8.2–3–5 Authentification et accès à privilèges | Exigences AMF ; accès administrateur traité comme accès à privilèges |
| A.8.9 Gestion de la configuration | Référentiels de configuration des plateformes de dépôts |
| A.8.15 Journalisation | Journalisation des audits pour les accès aux dépôts et les modifications de code |
| A.8.25–26–29 Cycle de vie du développement sécurisé | Codage sécurisé, protection des branches, intégration des revues de code |
| A.8.32 Gestion des changements | Contrôle des changements pour le déploiement du code en production |

**Politiques internes associées** :

- Politique de gestion des identités et des accès
- Politique du cycle de vie du développement sécurisé
- Politique de journalisation
- Politique de gestion des changements
- Politique de classification et de traitement de l'information

---

# Politique d'accès au code source

## Objet

La présente politique a pour objet de s'assurer que les accès en lecture et en écriture au code source, aux outils de développement et aux bibliothèques logicielles sont gérés de manière appropriée, afin de protéger la propriété intellectuelle, d'empêcher l'introduction de fonctionnalités non autorisées, d'éviter les modifications involontaires ou malveillantes, et de préserver la confidentialité des actifs logiciels de l'organisation.

Cette politique soutient la nLPD suisse (revDSG) art. 8 en mettant en œuvre des mesures techniques et organisationnelles proportionnées au risque pour protéger les données personnelles intégrées dans les systèmes de code source ou traitées par ceux-ci. Lorsque l'organisation traite des données de personnes situées dans l'UE/EEE, les exigences du RGPD art. 32 s'appliquent également. Le contrôle d'accès au code source est une mesure technique essentielle pour démontrer que les systèmes traitant des données personnelles font l'objet de restrictions d'accès appropriées.

## Champ d'application

Les dépôts de code source, les outils de développement et les bibliothèques logicielles détenus, gérés ou contrôlés par l'organisation et inclus dans le périmètre de la déclaration de champ d'application ISO 27001. Cela comprend :

- Tous les dépôts de code source (applications en production, outils internes, infrastructure en tant que code, gestion de la configuration, contributions open source, code archivé).
- Toutes les plateformes de dépôts ([Plateforme de dépôt] — par exemple GitHub Enterprise, GitLab, Bitbucket, Azure DevOps, ou serveur Git autohébergé). L'organisation documente ses principales plateformes de dépôts dans l'inventaire des actifs, notamment : modèle d'hébergement (cloud ou autohébergé), résidence des données, dispositions de sauvegarde et contrôles d'accès administrateur. Lorsque plusieurs plateformes sont utilisées, la présente politique s'applique à toutes sans distinction.
- Tous les artefacts de développement (code source, bibliothèques, scripts de construction, code de test, définitions de conteneurs, définitions de pipelines CI/CD).

Tous les employés, prestataires et utilisateurs tiers disposant d'un accès au code source.

**Hors périmètre** : Binaires compilés et exécutables ; configurations d'exécution en production (couvertes par A.8.9) ; normes de codage sécurisé (couvertes par A.8.25-26-29) ; logiciels commerciaux tiers pour lesquels l'organisation n'a pas accès au code source.

## Principe

L'accès au code source doit respecter le principe du moindre privilège. L'accès n'est accordé que sur la base d'un besoin métier documenté et approuvé par le propriétaire du dépôt.

L'organisation doit administrer de manière centralisée l'accès aux dépôts de code source en utilisant un système de gestion du code source. Les autorisations par défaut des dépôts sont « aucun accès » — tout niveau d'accès requiert une autorisation explicite.

Le code source est classé comme actif organisationnel critique. Tout accès non autorisé, toute modification ou toute divulgation du code source peut entraîner une perte de propriété intellectuelle, l'introduction de vulnérabilités, une non-conformité réglementaire ou un préjudice réputationnel.

---

## Classification des dépôts

Tous les dépôts de code source doivent être classifiés afin de déterminer les niveaux de protection appropriés.

**Catégories de classification** :

| Classification | Description | Exemples |
|----------------|-------------|----------|
| **Production** | Code déployé dans des systèmes de production critiques pour l'activité ou destinés aux clients | Application web client, service de traitement des paiements, passerelle API, backend d'application mobile |
| **Outils internes** | Code destiné à l'automatisation interne, aux utilitaires et aux outils opérationnels | Scripts de pipeline CI/CD, tableaux de bord de supervision, outils d'administration internes, automatisation des déploiements |
| **Open source** | Code de projet public ou open source auquel l'organisation contribue | Bibliothèques open source dérivées, contributions à la communauté, documentation publique |
| **Archivé** | Code historique qui n'est plus en développement actif | Code d'application héritée (fin de vie), versions antérieures de produits, preuves de concept terminées |

La classification des dépôts est attribuée par le propriétaire du dépôt lors de la création et révisée annuellement. Elle est mise à jour lorsque l'objet du dépôt change.

**Dépôts hérités et dormants** : Les dépôts hérités (par exemple après une acquisition, une restructuration d'équipe ou un départ de développeur) ou dormants (aucune contribution depuis plus de 12 mois) sont traités comme suit :

- **Dépôts hérités** : Le responsable d'équipe bénéficiaire est désigné propriétaire intérimaire du dépôt dans les 5 jours ouvrés. Le dépôt fait l'objet d'un examen de l'exactitude de sa classification, des autorisations d'accès et de la conformité au balayage de secrets dans les 30 jours.
- **Dépôts dormants** : Les dépôts sans activité de contribution depuis 12 mois sont signalés pour examen. Le propriétaire du dépôt confirme : (a) le dépôt est toujours nécessaire (maintien avec la classification actuelle), (b) le dépôt doit être archivé (passage à la classification Archivé, accès limité à la lecture seule), ou (c) le dépôt doit être supprimé (conformément à la politique de conservation des données). En l'absence de réponse après 30 jours, l'archivage automatique est effectué avec notification au Responsable du développement.

---

## Contrôle d'accès basé sur les rôles

L'accès aux dépôts est accordé sur la base de rôles définis avec les autorisations minimales requises.

**Rôles d'accès** :

| Rôle | Autorisations | Restrictions |
|------|---------------|--------------|
| **Développeur** | Cloner, tirer, créer des branches, pousser vers des branches non protégées, soumettre des demandes de fusion | Ne peut pas pousser vers des branches protégées, approuver ses propres demandes de fusion ni modifier les paramètres du dépôt |
| **Réviseur sécurité** | Accès en lecture à tous les dépôts pour les revues et audits de sécurité | Ne peut pas valider des modifications ni modifier des paramètres, sauf autorisation spécifique |
| **Auditeur** | Accès en lecture seule à durée déterminée pendant la période d'audit ; accès aux journaux d'audit et aux rapports d'autorisations | L'accès expire automatiquement à la fin de l'audit |
| **Prestataire externe** | Accès en écriture à durée déterminée, limité aux dépôts du périmètre contractuel | Ne peut pas accéder aux dépôts hors du périmètre du projet ; toutes les contributions soumises à une revue renforcée ; l'accès expire à la fin du contrat |
| **Administrateur de dépôt** | Gérer les paramètres du dépôt, la protection des branches et les accès des collaborateurs | L'accès administrateur n'accorde pas automatiquement l'accès en écriture au code (séparation des fonctions) ; les actions d'administration sont journalisées |
| **Propriétaire de dépôt** | Approuver les demandes d'accès, conduire les revues d'accès, définir la classification | Peut ou non disposer d'un accès en écriture au code selon son rôle |
| **Compte de service** | Accès automatisé pour les outils CI/CD, de déploiement et d'analyse de sécurité | Nommage descriptif ; authentification par jeton avec expiration ; accès limité à des dépôts spécifiques ; propriétaire et objet documentés. Les portées des jetons sont minimisées — par exemple CI/CD : `repo:read`, `actions:write` ; déploiement : `repo:read`, `packages:write` ; analyseur de sécurité : `repo:read`, `security_events:write` |

L'accès administrateur ou propriétaire n'est pas accordé aux prestataires externes, sauf dans des cas exceptionnels documentés avec approbation du RSSI.

---

## Demande et approbation d'accès

Toute demande d'accès à un dépôt doit comprendre :

- Nom et rôle du demandeur.
- Nom et classification du dépôt.
- Niveau d'accès demandé (lecture / écriture / administration).
- Justification métier.
- Durée prévue (si accès à durée déterminée).

**Exigences d'approbation** :

| Niveau d'accès | Approbateurs requis |
|----------------|---------------------|
| Accès en lecture | Propriétaire du dépôt |
| Accès en écriture | Propriétaire du dépôt + Responsable d'équipe de développement |
| Accès administrateur (tout dépôt) | Propriétaire du dépôt + Responsable d'équipe de développement |
| Accès administrateur (dépôt Production) | Propriétaire du dépôt + RSSI ou délégué |

L'accès est provisionné dans les 24 heures suivant l'approbation pendant les heures ouvrées. Les demandes d'accès d'urgence suivent un processus d'approbation accéléré avec revue a posteriori dans les 48 heures.

Toutes les demandes d'accès et approbations sont documentées et conservées pendant au minimum 3 ans.

---

## Revue et déprovisionement des accès

Les accès aux dépôts sont révisés trimestriellement pour confirmer la justification métier continue.

**Processus de revue trimestrielle des accès** :

1. Le propriétaire du dépôt examine l'accès de chaque utilisateur et confirme : accès toujours nécessaire (oui/non), niveau d'accès approprié (oui/non), action (maintien / modification / révocation).
2. La revue est documentée avec la confirmation et la date du propriétaire du dépôt.
3. L'absence de réponse est escaladée au Responsable du développement après 10 jours ouvrés ; au RSSI après 15 jours ouvrés.

**Revue des comptes de service** (trimestrielle) :

- L'automatisation ou le pipeline est-il encore actif ? (Signaler pour suppression si inactif depuis plus de 90 jours.)
- Le propriétaire documenté est-il toujours responsable ?
- Le niveau d'accès est-il toujours approprié ?
- L'expiration du jeton est-elle définie de manière appropriée ? (Maximum 1 an ; 90 jours recommandés pour les comptes à hauts privilèges.)

**Déprovisionement** :

- L'accès aux dépôts est révoqué le jour ouvré même suivant la fin du contrat de travail, un changement de rôle supprimant le besoin d'accès, ou l'expiration du contrat.
- Le déprovisionement automatisé via le système de gestion des identités est privilégié.
- Le déprovisionement est vérifié dans les 24 heures suivant l'événement déclencheur.

---

## Protection des branches et revue de code

La branche principale (main/master/trunk) des dépôts Production et Outils internes doit être protégée.

**Exigences de protection des branches** :

| Exigence | Production | Outils internes |
|----------|------------|-----------------|
| Contributions directes bloquées | Oui | Oui |
| Demande de fusion requise avant intégration | Oui | Oui |
| Nombre minimum de réviseurs | 2 | 1 |
| Invalidation des approbations obsolètes lors de nouvelles contributions | Oui | Recommandé |
| Les vérifications d'état doivent réussir (tests CI/CD, linters, analyses de sécurité) | Oui | Oui |
| Contributions signées | Recommandé | Optionnel |

Les branches de version (release/*, hotfix/*) bénéficient de la même protection que la branche principale.

Seuls les administrateurs de dépôt peuvent modifier les règles de protection des branches. La suppression temporaire de la protection d'une branche requiert une justification documentée, l'approbation du RSSI et la réactivation automatique à l'issue de la période spécifiée.

**Exigences des demandes de fusion** :

- Toutes les modifications de code apportées aux branches protégées sont soumises via des demandes de fusion.
- Les demandes de fusion ne peuvent pas être approuvées par l'auteur du code (séparation des fonctions).
- Les demandes de fusion comprennent une description claire des modifications, un lien vers l'anomalie ou le ticket associé le cas échéant, et la preuve des tests effectués.
- Les modifications liées à la sécurité comprennent une évaluation de l'impact sur la sécurité.

**Revue accélérée** : Les modifications à faible risque (mises à jour de la documentation, corrections de fautes de frappe, modifications de configuration sans logique de code) peuvent faire l'objet d'une période de revue d'1 heure pour les dépôts Production si elles sont étiquetées « faible risque » ou « docs uniquement », limitées aux fichiers de documentation ou de configuration, et approuvées par un propriétaire de code. Période de revue standard pour les modifications du code Production : 4 heures.

---

## Gestion des secrets

Les dépôts de code source ne doivent contenir aucun mot de passe, clé API, jeton, clé privée, chaîne de connexion de base de données avec des identifiants intégrés, clé privée SSH, clé de chiffrement, ni aucun autre matériau d'authentification sensible.

**Balayage des secrets** :

Tous les dépôts disposent d'un balayage automatisé des secrets activé via [Outil de balayage de secrets] (par exemple GitLeaks, TruffleHog, GitHub Secret Scanning, ou équivalent).

| Type de balayage | Périmètre | Fréquence |
|------------------|-----------|-----------|
| Balayage pré-contribution | Empêche les secrets d'entrer dans le dépôt | Temps réel (à chaque contribution) |
| Balayage côté serveur | Détecte les secrets déjà présents dans le dépôt | Balayage complet quotidien |

Les dépôts Production doivent avoir le balayage pré-contribution des secrets activé (mode bloquant).

Le balayage des secrets détecte les secrets génériques (motifs par expressions régulières), les secrets spécifiques aux fournisseurs (clés AWS, jetons GitHub, identifiants Azure) et les motifs personnalisés définis par l'équipe sécurité.

**Remédiation des secrets** :

| Classification du dépôt | Délai de remédiation |
|-------------------------|----------------------|
| Production | 1 heure (rotation immédiate si exposition confirmée) |
| Outils internes | 24 heures |

La remédiation comprend : (1) rotation immédiate du secret exposé, (2) suppression de l'historique du dépôt si validé, (3) évaluation de l'impact (le secret a-t-il été consulté par des parties non autorisées ?), et (4) signalement d'incident si requis.

**Méthodes approuvées de gestion des secrets** :

| Environnement | Méthode approuvée |
|---------------|-------------------|
| Développement | Variables d'environnement ; fichiers `.env` exclus du contrôle de version via `.gitignore` |
| Pipelines CI/CD | Coffre de secrets de la plateforme ([Plateforme CI/CD] Secrets ou équivalent) ; aucun secret en dur dans les définitions de pipeline |
| Production | Gestionnaire de secrets dédié (par exemple HashiCorp Vault, AWS Secrets Manager, Azure Key Vault, ou équivalent) |

Les développeurs sont formés aux bonnes pratiques de gestion des secrets, notamment l'utilisation des variables d'environnement, des systèmes de gestion des secrets et des hooks pré-contribution.

---

## Authentification et authentification multifacteur

L'accès aux dépôts de code source est authentifié via des méthodes approuvées : nom d'utilisateur/mot de passe (avec AMF), authentification par clé publique SSH, jetons d'accès personnels (avec expiration), authentification par certificat ou authentification unique (SSO) via le fournisseur d'identité de l'organisation.

**Exigences AMF** :

L'authentification multifacteur (AMF) est requise pour :

- Tous les comptes utilisateurs avec accès en écriture ou en administration aux dépôts Production.
- Tous les comptes utilisateurs avec accès administrateur à tout dépôt.
- L'accès aux dépôts via interface web pour tous les utilisateurs.

Méthodes AMF acceptées : applications d'authentification (par exemple Google Authenticator, Microsoft Authenticator, Authy), clés de sécurité matérielles (par exemple YubiKey) ou notification push sur l'appareil enregistré. Les codes par SMS sont la méthode la moins préférable et ne sont utilisés que si les autres méthodes ne sont pas disponibles.

**Clés SSH et jetons d'accès personnels** :

- Uniques par utilisateur et par appareil.
- Protégés par une phrase de passe ou un stockage sécurisé.
- Renouvelés annuellement ou immédiatement en cas de soupçon de compromission.
- Révoqués en cas de perte ou de mise hors service de l'appareil.

**Comptes de service** : Les comptes de service ne peuvent pas effectuer d'AMF interactive. Les contrôles compensatoires comprennent : jetons émis avec les portées minimales requises, expiration des jetons appliquée (maximum 1 an ; 90 jours recommandés pour les comptes à hauts privilèges), activité journalisée et supervisée pour détecter les anomalies, et revue trimestrielle du besoin continu.

---

## Journalisation des audits et supervision

Les plateformes de dépôts journalisent les événements suivants :

| Catégorie d'événement | Événements journalisés |
|-----------------------|------------------------|
| **Accès** | Tentatives de connexion, déconnexions, durée de session |
| **Accès aux dépôts** | Clonage, tirage, opérations de navigation |
| **Modifications du code** | Contributions (auteur, horodatage, message, fichiers), poussées, poussées forcées |
| **Opérations sur les branches** | Création, suppression, modifications de protection |
| **Demandes de fusion** | Création, revue, approbation, intégration, rejet |
| **Modifications d'autorisations** | Accès accordé, révoqué, changements de rôle |
| **Actions d'administration** | Modifications des paramètres du dépôt, gestion des collaborateurs |
| **Événements de sécurité** | Alertes de balayage de secrets, échecs d'authentification, schémas d'accès suspects |

Les journaux comprennent : horodatage (UTC), identité de l'utilisateur, adresse IP source, action effectuée, dépôt concerné et statut (succès ou échec).

**Conservation des journaux** :

| Type d'événement | Conservation minimale |
|------------------|-----------------------|
| Événements d'accès | 1 an |
| Événements de modification du code | 3 ans |
| Modifications d'autorisations | 3 ans |
| Événements de sécurité | 3 ans |
| Actions d'administration | 3 ans |

Les journaux sont inviolables et protégés contre toute modification ou suppression non autorisée.

**Supervision et alertes** :

Les journaux d'accès aux dépôts sont supervisés pour détecter : les tentatives d'authentification multiples échouées, les accès depuis des localisations géographiques inhabituelles, les accès en dehors des heures ouvrées normales, les opérations de téléchargement en masse, les tentatives d'élévation de privilèges, les poussées forcées vers des branches protégées et les alertes de balayage de secrets.

Des alertes de sécurité sont générées et transmises à l'équipe des opérations de sécurité dans les 15 minutes suivant la détection. Les événements critiques (accès non autorisé confirmé, modifications massives d'autorisations) déclenchent une réponse immédiate aux incidents conformément au processus de gestion des incidents de l'organisation. Les incidents de sécurité confirmés impliquant du code source (accès non autorisé, falsification de code, vol de propriété intellectuelle) sont escaladés au RSSI dans l'heure suivant la confirmation. Lorsque l'incident implique des données client ou des systèmes de production, le processus de gestion des incidents (A.5.24-28) est activé immédiatement.

---

## Sauvegarde et reprise

Tous les dépôts de code source doivent être sauvegardés pour permettre la reprise en cas de perte de données, de corruption ou de défaillance de la plateforme.

**Exigences de sauvegarde** :

| Exigence | Norme |
|----------|-------|
| Fréquence | Incrémentale quotidienne ; complète hebdomadaire |
| Conservation | 90 jours (dépôts actifs) ; 7 ans (dépôts Production) |
| Redondance géographique | Sauvegardes stockées dans un emplacement géographique différent du dépôt principal |
| Chiffrement | Chiffrement au repos utilisant le chiffrement approuvé par l'organisation |
| Contrôle d'accès | Limité aux administrateurs de sauvegarde autorisés ; AMF requise |

Les sauvegardes comprennent le code source (toutes les branches, contributions, historique complet), les métadonnées du dépôt (autorisations, paramètres, configurations), l'historique des demandes de fusion et les données de suivi des anomalies si intégrées.

**Tests de reprise** :

| Classification du dépôt | Fréquence des tests | Objectif de délai de reprise (RTO) |
|-------------------------|---------------------|-------------------------------------|
| Production | Trimestriel | 4 heures |
| Outils internes | Annuel | 24 heures |

Les tests de reprise vérifient : la restauration du dépôt dans le RTO, l'intégrité des données (toutes les contributions, branches et historique intacts), la restauration des autorisations et la fonctionnalité du dépôt restauré. Les tests portent sur un échantillon représentatif de dépôts (minimum 3 dépôts Production par trimestre, en rotation pour couvrir l'ensemble sur l'année). Les résultats sont documentés.

---

## Gestion des accès tiers

Les développeurs tiers, prestataires et équipes de développement externalisées doivent satisfaire aux exigences suivantes avant de recevoir un accès aux dépôts :

- Accord de non-divulgation (NDA) signé, vérifié par les achats ou le service juridique.
- Accès limité aux dépôts spécifiques requis pour les travaux contractuels.
- Accès à durée déterminée lié à la durée du contrat, avec expiration automatique.
- Accès approuvé par le propriétaire du dépôt (obligatoire) et le RSSI ou délégué (pour les dépôts Production).

**Supervision des tiers** :

- L'accès des tiers est révisé mensuellement pour confirmer le besoin continu.
- Toutes les contributions de code provenant de tiers requièrent une revue par un développeur interne (minimum un réviseur) et une revue de sécurité pour les modifications liées à la sécurité.
- L'accès des tiers est immédiatement révoqué à l'expiration du contrat, la résiliation du contrat, un incident de sécurité impliquant le tiers, ou à la demande du propriétaire du dépôt.

L'accès des tiers est documenté dans un registre des accès tiers comprenant : société contractante, noms des individus, dépôts consultés, dates du contrat et responsabilité du chef de projet.

---

## Gestion des exceptions

Les exceptions à la présente politique sont demandées par écrit et comprennent :

- Exigence(s) spécifique(s) nécessitant une dérogation.
- Justification métier.
- Contrôles compensatoires.
- Durée de dérogation demandée (maximum 12 mois).
- Évaluation et acceptation des risques.

Les exceptions sont approuvées par le propriétaire du dépôt et le Responsable de la sécurité de l'information (obligatoire), ainsi que par le RSSI pour les exceptions concernant les dépôts Production. Toutes les exceptions actives sont révisées trimestriellement.

Lorsqu'il est techniquement impossible de satisfaire à une exigence, des contrôles compensatoires sont mis en place pour obtenir une réduction équivalente du risque, documentés, vérifiés par le Responsable de la sécurité de l'information et révisés annuellement.

---

## Définitions

| Terme | Définition |
|-------|------------|
| **Protection des branches** | Règles de configuration qui empêchent les contributions directes vers des branches spécifiées, exigeant des demandes de fusion, des revues et la réussite des vérifications d'état |
| **Propriétaire de code** | Individu ou équipe désigné(e) responsable de la revue des modifications apportées à des parties spécifiques du code |
| **Poussée forcée** | Opération Git qui écrase l'historique de la branche distante ; restreinte sur les branches protégées |
| **AMF** | Authentification multifacteur — exigeant deux facteurs de vérification ou plus pour obtenir l'accès |
| **Hook pré-contribution** | Script s'exécutant avant la création d'une contribution, utilisé pour empêcher les secrets ou violations de politique d'entrer dans le dépôt |
| **Demande de fusion (merge request)** | Demande d'intégration des modifications de code d'une branche vers une autre, permettant une revue avant intégration |
| **RBAC** | Contrôle d'accès basé sur les rôles — attribution des autorisations sur la base des rôles organisationnels définis |
| **Dépôt** | Emplacement de stockage du code source, géré par un système de contrôle de version (par exemple Git) |
| **Secret** | Tout identifiant, clé API, jeton, clé privée ou matériau d'authentification ne devant pas être stocké dans le code source |
| **Compte de service** | Compte non humain utilisé pour l'automatisation, le CI/CD et l'intégration système à système |
| **SSO** | Authentification unique — authentification permettant aux utilisateurs d'accéder à plusieurs systèmes avec un seul ensemble d'identifiants |

---

## Rôles et responsabilités

| Rôle | Responsabilités |
|------|-----------------|
| **RSSI** | Propriété de la politique ; approbation de l'accès administrateur aux dépôts Production ; approbation des exceptions ; supervision des incidents de sécurité impliquant du code source ; révision annuelle de la politique ; rapport à la Direction générale |
| **DT / Responsable du développement** | Sélection et configuration de la plateforme de développement ; approbation de la classification des dépôts ; conformité de l'équipe de développement ; allocation des ressources pour la mise en œuvre de la politique |
| **Responsable de la sécurité de l'information** | Maintenance de la politique ; revue des exceptions (dépôts hors Production) ; supervision de la sécurité et enquête sur les incidents ; coordination des audits ; rapport de conformité trimestriel au RSSI |
| **Propriétaires de dépôts** | Attribution de la classification des dépôts ; approbation des demandes d'accès ; revues d'accès trimestrielles ; configuration de la sécurité des dépôts ; signalement des incidents à l'équipe sécurité |
| **Responsables d'équipe de développement** | Revue des demandes d'accès pour les membres de l'équipe ; application du processus de revue de code ; formation des développeurs aux pratiques de dépôt sécurisé ; application de la gestion des secrets au sein de l'équipe |
| **Équipe sécurité** | Configuration de la supervision et des alertes de sécurité ; gestion des outils de balayage de secrets ; audits et évaluations de sécurité ; réponse aux incidents pour les événements de sécurité du code source |
| **Opérations informatiques** | Maintenance et disponibilité de la plateforme de dépôts ; mise en œuvre de la sauvegarde et de la reprise ; automatisation du provisionement et du déprovisionement des accès ; collecte et conservation des journaux |
| **Développeurs et prestataires individuels** | Conformité aux exigences de contrôle d'accès et d'authentification ; protection des identifiants ; aucun stockage de secrets dans les dépôts ; participation aux revues de code ; signalement des incidents ; suivi des formations de sécurité requises |

---

## Preuves

Les éléments de preuve suivants démontrent la conformité à la présente politique :

| # | Preuve | Responsable | Fréquence | Conservation |
|---|--------|-------------|-----------|--------------|
| 1 | **Inventaire des dépôts** avec classification, propriétaire et métadonnées de plateforme | DT / Responsable du développement | Maintenu en continu ; révisé annuellement | Durée de vie du dépôt + 3 ans |
| 2 | **Enregistrements des demandes d'accès et approbations** (demandes, justifications, approbations) | Propriétaires de dépôts | Par demande | 3 ans |
| 3 | **Enregistrements des revues d'accès trimestrielles** (confirmation utilisateur par utilisateur, actions prises) | Propriétaires de dépôts | Trimestriel | 3 ans |
| 4 | **Inventaire des comptes de service** avec propriétaire, objet et enregistrements de revue trimestrielle | Opérations informatiques / Responsable du développement | Maintenu en continu ; révisé trimestriellement | Durée de vie du compte + 1 an |
| 5 | **Exports de configuration de protection des branches** depuis la plateforme de dépôts | Responsable du développement / DevOps | Trimestriel | 2 ans |
| 6 | **Enregistrements des demandes de fusion et des revues de code** (commentaires de revue, approbations, historique des intégrations) | Responsable du développement | Par modification de code | 3 ans |
| 7 | **Journal de configuration et de résultats du balayage de secrets** (paramètres de l'outil, alertes, enregistrements de remédiation) | Équipe sécurité / DevOps | Continu ; résultats révisés hebdomadairement | 3 ans |
| 8 | **Rapports d'enrôlement AMF** indiquant la couverture parmi les utilisateurs des dépôts | Opérations informatiques / Équipe sécurité | Trimestriel | 1 an |
| 9 | **Journaux d'authentification et d'accès** de la plateforme de dépôts | Opérations informatiques | Continu | Selon le tableau de conservation (1–3 ans par type d'événement) |
| 10 | **Enregistrements d'exécution des sauvegardes et de tests de reprise** (journaux de sauvegarde, rapports de test, mesures RTO) | Opérations informatiques | Sauvegarde : quotidienne ; Tests de reprise : trimestriel (Production) / annuel (autres) | 3 ans |
| 11 | **Registre des accès tiers** (coordonnées des prestataires, NDA, dates du contrat, expiration des accès) | Propriétaires de dépôts / Achats | Maintenu en continu ; révisé mensuellement | Durée du contrat + 3 ans |
| 12 | **Registre des exceptions** (demandes, approbations, contrôles compensatoires, revues trimestrielles) | Responsable de la sécurité de l'information | Maintenu en continu ; révisé trimestriellement | Durée de l'exception + 3 ans |
| 13 | **Enregistrements de formation sécurité des développeurs** (gestion des secrets, pratiques de dépôt sécurisé) | RSSI / RH | Annuel | Durée d'emploi + 3 ans |
| 14 | **Enregistrements de vérification du déprovisionement** (confirmations de révocation déclenchées par les fins de contrat) | Opérations informatiques / RH | Par événement de fin de contrat | 3 ans |

---

# Conformité à la politique

## Mesure de la conformité

L'équipe de gestion de la sécurité de l'information vérifie la conformité à la présente politique par diverses méthodes, notamment les rapports d'accès à la plateforme de dépôts, les audits de configuration de protection des branches, les rapports des outils de balayage de secrets, les enregistrements de revues d'accès, les audits internes et externes, et les retours au propriétaire de la politique.

**Métriques de conformité** :

| Métrique | Cible | Fréquence de mesure |
|----------|-------|---------------------|
| Dépôts avec RBAC conforme et revues trimestrielles complétées | >= 90 % | Trimestriel |
| Dépôts avec protection des branches requise activée | >= 95 % | Trimestriel |
| Dépôts avec balayage de secrets activé et secrets remédiés dans les délais | >= 90 % | Mensuel |
| Comptes tiers avec NDA valide et contrat en cours | 100 % | Mensuel |
| Enrôlement AMF pour les utilisateurs avec accès en écriture ou administration | 100 % | Trimestriel |
| Accès déprovisionné le jour ouvré même suivant la fin du contrat | 100 % | Par événement |

**Notation de la conformité** :

| Composant | Pondération | Calcul |
|-----------|-------------|--------|
| Conformité de l'accès aux dépôts | 35 % | (Dépôts avec RBAC conforme + revues trimestrielles complétées) / Total dépôts × 100 |
| Conformité de la protection des branches | 35 % | (Dépôts avec protection des branches requise activée) / Dépôts applicables × 100 |
| Conformité de la gestion des secrets | 20 % | (Dépôts avec balayage activé + secrets remédiés dans les délais) / Total × 100 |
| Conformité de l'accès tiers | 10 % | (Comptes tiers avec NDA valide + contrat en cours) / Total comptes tiers × 100 |

**Traitement des non-conformités** : En dessous de 70 %, une escalade immédiate au RSSI et un plan de remédiation sont requis. Entre 70 et 89 %, la supervision du Responsable de la sécurité de l'information avec des revues mensuelles est requise. À 90 % et au-delà, la supervision trimestrielle standard s'applique.

**Responsabilité de remédiation par composant** :

| Composant | En dessous de la cible | Responsable de la remédiation | Escalade |
|-----------|------------------------|-------------------------------|----------|
| Conformité de l'accès aux dépôts | <90 % | Propriétaires de dépôts + Responsable du développement | RSSI à 30 jours de retard |
| Conformité de la protection des branches | <95 % | DevOps / Responsable du développement | RSSI à 15 jours de retard |
| Conformité de la gestion des secrets | <90 % | Équipe sécurité + DevOps | RSSI immédiatement si secrets actifs exposés |
| Conformité de l'accès tiers | <100 % | Achats + Propriétaires de dépôts | RSSI à 5 jours de retard (risque juridique/contractuel) |

## Exceptions

Toute exception à la présente politique est approuvée et enregistrée par le Responsable de la sécurité de l'information au préalable, avec acceptation des risques documentée, contrôles compensatoires et date de révision définie (maximum 12 mois). Les exceptions sont communiquées à l'équipe de revue de direction.

## Non-conformité

Tout employé reconnu coupable d'avoir enfreint la présente politique peut faire l'objet de mesures disciplinaires pouvant aller jusqu'au licenciement. Les violations de la politique sont documentées, font l'objet d'une enquête par le Responsable de la sécurité de l'information et sont signalées au RSSI.

## Étapes de mise en œuvre SOC 2

Pour les organisations poursuivant la certification SOC 2 Type II, la mise en œuvre progressive suivante est recommandée :

| Étape | Axe | Actions clés |
|-------|-----|--------------|
| 1 | **Inventaire des actifs** | Inventaire complet des dépôts avec classification et propriétaire |
| 2 | **Mise en œuvre du RBAC** | Contrôle d'accès basé sur les rôles avec moindre privilège |
| 3 | **Application de l'AMF** | AMF pour tous les accès en écriture/administration |
| 4 | **Protection des branches** | Branches protégées avec revues requises |
| 5 | **Balayage de secrets** | Balayage automatisé pré-contribution et côté serveur |
| 6 | **Journalisation et supervision** | Journalisation d'audit complète transmise au SIEM |
| 7 | **Revues d'accès** | Revues trimestrielles avec preuves documentées |
| 8 | **Sauvegarde et reprise** | Stratégie de sauvegarde avec reprise testée |
| 9 | **Contrôles tiers** | NDA, accès à durée déterminée, revue renforcée |
| 10 | **Amélioration continue** | Métriques, notation de conformité, rapport trimestriel |

## Amélioration continue

La présente politique est révisée et mise à jour dans le cadre du processus d'amélioration continue. Les révisions prennent en compte les évolutions des capacités de la plateforme de dépôts, les menaces émergentes pour la sécurité du code source (attaques sur la chaîne d'approvisionnement, confusion de dépendances, compromission des pipelines CI/CD), les évolutions réglementaires, les conclusions des audits et les enseignements tirés des incidents de sécurité.

---

# Domaines de la norme ISO 27001 couverts

Politique d'accès au code source — Correspondance des contrôles ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership et engagement | 5.1 Politiques de sécurité de l'information |
| Clause 5.2 Politique | 5.4 Responsabilités de la direction |
| Clause 6.2 Objectifs de sécurité de l'information | 5.36 Conformité aux politiques, règles et normes |
| Clause 7.3 Sensibilisation | 6.3 Sensibilisation, éducation et formation à la sécurité de l'information |
| | 6.4 Processus disciplinaire |
| | **8.4 Accès au code source** |
| | 8.5 Authentification sécurisée |
| | 8.25 Cycle de vie du développement sécurisé |

**Cadre réglementaire et juridique** :

| Cadre | Pertinence |
|-------|-----------|
| nLPD suisse (revDSG) | Art. 8 — Mesures techniques et organisationnelles pour la protection des données ; contrôle d'accès au code source comme mesure technique |
| DSV suisse (Ordonnance sur la protection des données) | Art. 1–3 — Exigences minimales de sécurité des données |
| RGPD (le cas échéant) | Art. 32 — Sécurité du traitement (contrôle d'accès comme mesure technique appropriée) |
| ISO/IEC 27001:2022 | Contrôle Annexe A 8.4 — Accès au code source |
| ISO/IEC 27002:2022 | Section 8.4 — Recommandations de mise en œuvre pour le contrôle d'accès au code source |
| NIST SP 800-218 (SSDF) | PS.1 — Protéger toutes les formes de code contre tout accès et toute falsification non autorisés |
| NIST SP 800-53 Rév. 5 | AC-3 (Application du contrôle d'accès), AC-6 (Moindre privilège), CM-5 (Restrictions d'accès aux modifications), AU-2 (Événements d'audit) |
| CIS Controls v8 | 6.1–6.2 (Octroi/révocation d'accès), 6.7 (Contrôle d'accès centralisé), 6.8 (Accès basé sur les rôles), 16.1–16.4 (Sécurité des applications logicielles) |
| FINMA (le cas échéant) | Circulaire 2023/1 Marge 50–62 — La sécurité de l'information inclut la protection du code source |
| DORA (le cas échéant) | Art. 9 — La gestion des actifs TIC inclut le code source ; Art. 15 — Le signalement des incidents inclut la compromission du code source |
| NIS2 (le cas échéant) | Art. 21(2) — La gestion des actifs inclut le code source ; Art. 23 — Signalement des incidents de sécurité du code source |

---

<!-- QA_VERIFIED: 2026-03-29 -->
