<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.17-FR:framework:POL:a.5.17 -->
**ISMS-POL-A.5.17 — Informations d'authentification**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Informations d'authentification |
| **Type de document** | Politique |
| **Identifiant du document** | ISMS-POL-A.5.17 |
| **Créateur du document** | Responsable de la sécurité des systèmes d'information (RSSI) |
| **Propriétaire du document** | Responsable de la sécurité des systèmes d'information (RSSI) |
| **Approuvé par** | Direction générale |
| **Date de création** | [Date] |
| **Version** | 1.0 |
| **Date de version** | [Date à définir] |
| **Classification** | Interne |
| **Statut** | Projet |

**Historique des versions** :

| Version | Date | Auteur | Modifications |
|---------|------|--------|---------------|
| 1.0 | [Date] | RSSI | Politique initiale pour la certification ISO 27001:2022 |

**Cycle de révision** : Annuel
**Prochaine date de révision** : [Date d'entrée en vigueur + 12 mois]

**Chaîne d'approbation** :

- Principal : Responsable de la sécurité des systèmes d'information (RSSI)
- Secondaire : Directeur des systèmes d'information (DSI)
- Autorité finale : Direction générale

**Documents connexes** :

- ISMS-POL-00 (Cadre d'applicabilité réglementaire)
- ISMS-POL-A.5.15-16-18 (Gestion des identités et des accès)
- ISMS-POL-A.8.2-3-5 (Authentification et accès privilégié)
- ISMS-POL-A.8.24 (Utilisation de la cryptographie)
- ISMS-IMP-A.5.17.1-UG/TG (Guide de mise en œuvre de la politique des mots de passe)
- ISMS-IMP-A.5.17.2-UG/TG (Évaluation du déploiement AMF)
- ISMS-IMP-A.5.17.3-UG/TG (Procédures de gestion de l'authentification)
- ISO/IEC 27001:2022 Contrôle A.5.17

---

## Résumé exécutif

La présente politique établit les exigences de [Organisation] pour la gestion et la protection des informations d'authentification afin de prévenir tout accès non autorisé aux systèmes d'information et aux données.

**Périmètre** : La présente politique s'applique à toutes les informations d'authentification, notamment les mots de passe, les codes PIN, les clés cryptographiques, les jetons, les gabarits biométriques et autres secrets d'authentification utilisés pour accéder aux systèmes et données de [Organisation].

**Objet** : Définir les exigences organisationnelles en matière de gestion des informations d'authentification. La présente politique établit QUELS contrôles d'authentification sont requis et QUI en est responsable. Les procédures de mise en œuvre (COMMENT) sont documentées séparément dans ISMS-IMP-A.5.17 (variantes UG/TG).

**Alignement réglementaire** : La présente politique répond aux exigences de conformité obligatoires visées par ISMS-POL-00 (Cadre d'applicabilité réglementaire), notamment la nLPD suisse, le RGPD de l'UE et la norme ISO/IEC 27001:2022. Les exigences sectorielles conditionnelles (FINMA, PCI DSS v4.0.1, NIS2, DORA) s'appliquent lorsque les activités commerciales de [Organisation] en déclenchent l'applicabilité.

---

**Alignement des contrôles et périmètre**

**Contrôle ISO/IEC 27001:2022 A.5.17**

**ISO/IEC 27001:2022 Annexe A.5.17 — Informations d'authentification**

Les informations d'authentification sont émises, gérées, protégées et révoquées via des processus de cycle de vie définis. Le personnel reçoit des instructions sur la manipulation sécurisée et doit respecter les exigences documentées en matière de confidentialité et de signalement des compromissions.

**Objectifs du contrôle** :

- S'assurer que les informations d'authentification sont allouées de manière sécurisée via des processus vérifiés
- Protéger les informations d'authentification tout au long de leur cycle de vie
- Prévenir l'accès non autorisé par la compromission des identifiants
- Maintenir la traçabilité de l'utilisation des identifiants d'authentification

**Type de contrôle** : Préventif
**Catégorie de contrôle** : Organisationnelle

**La présente politique traite** :

- L'allocation et la distribution des informations d'authentification
- Les exigences et normes de complexité des mots de passe
- Les exigences d'authentification multifacteur
- La protection et la manipulation des secrets d'authentification
- Les procédures de réinitialisation et de récupération des mots de passe

## Ce que fait cette politique

La présente politique :

- **Définit** les exigences pour l'allocation sécurisée des informations d'authentification
- **Établit** les normes de complexité et de cycle de vie des mots de passe
- **Spécifie** les exigences d'authentification multifacteur par type d'accès
- **Référence** les exigences réglementaires applicables conformément à ISMS-POL-00

## Ce que cette politique ne fait PAS

La présente politique ne :

- **Définit pas la mise en œuvre technique des mécanismes d'authentification** (voir ISMS-POL-A.8.2-3-5 et ISMS-IMP-A.5.17)
- **Établit pas les procédures de gestion des accès privilégiés** (voir ISMS-POL-A.8.2-3-5)
- **Fournit pas les détails de l'infrastructure de gestion des clés cryptographiques** (voir ISMS-POL-A.8.24)
- **Détaille pas la gestion du cycle de vie des identités** (voir ISMS-POL-A.5.15-16-18)

**Justification** : La séparation entre les exigences de politique et les orientations de mise en œuvre permet :

- La stabilité de la politique malgré les changements de technologie ou de plateforme
- La flexibilité pour différentes solutions d'authentification
- Une distinction claire entre gouvernance (politique) et exécution (mise en œuvre)

## Périmètre

**La présente politique s'applique à** :

- Toutes les informations d'authentification (mots de passe, codes PIN, jetons, clés, données biométriques)
- Tous les systèmes d'information, applications, équipements réseau, services en nuage et bases de données
- Tout le personnel (employés, prestataires, tiers) disposant d'un accès système
- Tous les processus d'authentification (allocation, gestion, réinitialisation, révocation)

**Hors périmètre** :

- Les comptes personnels sans lien avec les systèmes organisationnels
- La conception et l'ingénierie des mécanismes d'authentification (couvert par A.8.5)
- Le cycle de vie de la gestion des clés cryptographiques (génération de clés, paramètres cryptographiques, contrôles HSM/KMS, opérations PKI d'entreprise) — régi par ISMS-POL-A.8.24

**Clarification des limites du périmètre** : La présente politique couvre l'émission, le stockage/la manipulation, le contrôle d'accès, les déclencheurs de rotation/révocation et la journalisation des secrets d'authentification (y compris les clés API et les certificats utilisés pour l'authentification). Les contrôles du cycle de vie de la gestion des clés cryptographiques sont régis par ISMS-POL-A.8.24 ; la mise en œuvre des mécanismes d'authentification est régie par ISMS-POL-A.8.2-3-5.

## Applicabilité réglementaire

Les exigences réglementaires sont catégorisées conformément à **ISMS-POL-00 (Cadre d'applicabilité réglementaire)**.

**Niveau 1 : Conformité obligatoire**

| Règlementation | Applicabilité | Exigences principales |
|----------------|---------------|----------------------|
| **nLPD suisse art. 8** | Tout traitement de données personnelles | Mesures techniques pour la protection des données |
| **ISO/IEC 27001:2022** | Périmètre de certification | Contrôle A.5.17 — Informations d'authentification |

**Niveau 2 : Applicabilité conditionnelle**

S'applique uniquement lorsque des conditions commerciales spécifiques déclenchent l'applicabilité :

| Règlementation | Condition déclenchante | Exigences d'authentification |
|----------------|------------------------|------------------------------|
| **RGPD UE art. 32** | Traitement de données personnelles de l'UE | Mesures de sécurité appropriées incluant l'authentification |
| **FINMA** | Établissement financier réglementé suisse | Authentification renforcée pour les systèmes financiers |
| **PCI DSS v4.0.1** | Traitement de cartes de paiement | Exigence 8 — Authentification forte |
| **NIS2** | Entité essentielle/importante (UE) | Exigences d'authentification forte |
| **DORA** | Entité de services financiers de l'UE | Sécurité TIC incluant les contrôles d'authentification |

**Niveau 3 : Orientations informatives**

Ces cadres guident la mise en œuvre, mais ne constituent pas une conformité obligatoire sauf obligation contractuelle :

- NIST SP 800-63B (Lignes directrices sur l'identité numérique — Authentification)
- CIS Controls v8.1 (Contrôle 5 — Gestion des comptes, Contrôle 6 — Contrôle d'accès)
- Directives d'authentification OWASP
- Recommandations Microsoft Security Baseline

**Détermination de la conformité** : [Organisation] détermine les réglementations de niveau 2 applicables par une évaluation périodique des activités commerciales. Les exigences d'authentification les plus strictes s'appliquent lorsque plusieurs réglementations se chevauchent.

---

# Énoncés de politique

## Allocation des informations d'authentification

### Exigences d'allocation initiale

[Organisation] DOIT allouer les informations d'authentification via des processus contrôlés :

**Vérification de l'identité** :

- Vérifier l'identité de l'utilisateur avant d'émettre des identifiants d'authentification
- Utiliser une vérification hors bande pour les accès aux systèmes sensibles
- Documenter la méthode de vérification utilisée pour la piste d'audit

**Distribution sécurisée** :

| Type d'authentification | Méthode de distribution |
|--------------------------|-------------------------|
| **Mots de passe initiaux** | Canal sécurisé, séparé du nom d'utilisateur, changement forcé à la première utilisation |
| **Jetons/matériel** | Remise en personne avec vérification de l'identité, reçu signé |
| **Certificats** | Processus d'enrôlement sécurisé, courriel vérifié |
| **Clés API** | Canal chiffré, validité limitée, émission journalisée |

**Authentification temporaire** :

- Les informations d'authentification temporaires DOIVENT avoir une validité maximale de 24 heures
- Les utilisateurs DOIVENT changer les identifiants temporaires à la première utilisation
- Le système DOIT appliquer l'expiration des identifiants temporaires

### Gestion des identifiants par défaut

[Organisation] NE DOIT PAS utiliser les informations d'authentification par défaut :

- Tous les mots de passe par défaut des fournisseurs/fabricants DOIVENT être changés avant le déploiement en production
- Les comptes par défaut DOIVENT être désactivés ou renommés dans la mesure du possible sur le plan technique
- La vérification du changement des identifiants par défaut DOIT figurer dans la liste de contrôle de mise en service des systèmes

**Conditions d'infaisabilité technique** : Un compte par défaut ne peut être désactivé/renommé lorsque : (1) le firmware/support du fournisseur requiert le compte, (2) le système ne dispose pas de la fonctionnalité de renommage, (3) la désactivation brise une fonctionnalité critique. Dans les cas d'infaisabilité, des contrôles compensatoires obligatoires s'appliquent : mot de passe fort unique par appareil, segmentation réseau limitant l'accès, AMF lorsque prise en charge, surveillance/alertes renforcées, mise en chambre forte des identifiants et exception documentée dans ISMS-REG-EXCEPTIONS.

## Exigences relatives aux mots de passe

### Normes de complexité des mots de passe

[Organisation] DOIT appliquer les exigences suivantes en matière de mots de passe :

| Exigence | Accès standard | Accès privilégié | Comptes de service |
|----------|----------------|------------------|--------------------|
| **Longueur minimale** | 12 caractères | 16 caractères | 24 caractères |
| **Complexité** | 3 types de caractères sur 4 | 4 types de caractères sur 4 | Complexe + aléatoire |
| **Historique** | 12 mots de passe mémorisés | 24 mots de passe mémorisés | S.O. (utilisation unique) |
| **Âge maximum** | 90 jours | 60 jours | 90 jours ou basé sur certificat |
| **Seuil de verrouillage** | 5 tentatives échouées | 3 tentatives échouées | Alerte sur une seule tentative échouée |

**Types de caractères** : Majuscules, minuscules, chiffres, caractères spéciaux.

**Justification de la rotation des mots de passe** : La rotation basée sur le temps est complétée par des déclencheurs de rotation basés sur des événements : (1) compromission suspectée, (2) découverte d'identifiant partagé, (3) absence de protection AMF, (4) changement de poste du personnel affectant le périmètre d'accès. Lorsqu'une AMF forte et une surveillance continue sont vérifiées, la rotation peut être étendue via une exception documentée avec approbation du RSSI. Les intervalles spécifiés (60/90 jours) reflètent les décisions de traitement du risque de [Organisation] en équilibrant sécurité et utilisabilité.

### Pratiques de mots de passe interdites

Le personnel NE DOIT PAS :

- Partager les mots de passe avec quiconque (y compris le support informatique)
- Écrire les mots de passe dans des emplacements non protégés
- Stocker les mots de passe dans des fichiers ou documents en clair
- Utiliser le même mot de passe sur plusieurs systèmes
- Utiliser des mots de passe basés sur des informations faciles à deviner (noms, dates, mots du dictionnaire)
- Transmettre des mots de passe via des canaux non chiffrés

### Stockage des mots de passe

[Organisation] DOIT stocker les mots de passe de manière sécurisée :

- Les mots de passe DOIVENT être stockés en utilisant un hachage cryptographique à sens unique approuvé avec sel
- Algorithmes de hachage des mots de passe : bcrypt, Argon2, PBKDF2 (avec paramètres appropriés)
- Le stockage des mots de passe en clair est INTERDIT
- Les bases de données de mots de passe DOIVENT être protégées par chiffrement au repos

## Authentification multifacteur

### Exigences AMF

[Organisation] DOIT exiger l'authentification multifacteur pour :

| Type d'accès | Exigence AMF |
|--------------|--------------|
| **Accès distant** (VPN, nuage) | Obligatoire |
| **Accès privilégié/administrateur** | Obligatoire |
| **Systèmes critiques** | Obligatoire |
| **Accès aux données clients** | Obligatoire |
| **Messagerie (accès externe)** | Obligatoire |
| **Accès interne standard** | Basé sur le risque selon le niveau système dans ISMS-IMP-A.5.17 ; décisions enregistrées dans la politique d'accès conditionnel du fournisseur d'identité ; couverture revue trimestriellement |

### Types de facteurs AMF

Facteurs d'authentification acceptables :

| Catégorie de facteur | Exemples | Exigences |
|----------------------|----------|-----------|
| **Ce que vous savez** | Mot de passe, code PIN, phrase de passe | Conformément aux exigences relatives aux mots de passe |
| **Ce que vous avez** | Jeton matériel, authentificateur mobile, carte à puce | Enregistré à l'utilisateur individuel |
| **Ce que vous êtes** | Empreinte digitale, reconnaissance faciale | Gabarit biométrique stocké de manière sécurisée |

Les mises en œuvre AMF DOIVENT utiliser des facteurs d'au moins deux catégories différentes.

## Protection des informations d'authentification

### Responsabilités des utilisateurs

Tout le personnel DOIT :

- Maintenir les informations d'authentification confidentielles
- Utiliser des mots de passe forts et uniques pour chaque système
- Signaler immédiatement toute compromission suspectée
- Ne pas permettre à d'autres d'utiliser leurs identifiants
- Changer les mots de passe immédiatement en cas de compromission suspectée
- Utiliser des gestionnaires de mots de passe approuvés pour un stockage sécurisé

### Exigences système

Les systèmes DOIVENT :

- Masquer la saisie des mots de passe à l'écran
- Ne pas afficher les mots de passe précédemment utilisés
- Chiffrer le trafic d'authentification en transit
- Journaliser les événements d'authentification (succès et échecs)
- Alerter sur les anomalies d'authentification
- Mettre en œuvre le verrouillage de compte après des tentatives échouées

### Informations d'authentification partagées

Les informations d'authentification partagées sont DÉCONSEILLÉES. Lorsqu'elles sont requises :

- Approbation du RSSI obligatoire avec justification commerciale documentée
- Stockage dans un coffre-fort d'identifiants approuvé (pas de documents en clair/messagerie/chat)
- Dépositaire nommé affecté pour chaque identifiant partagé
- Journalisation des consultations avec identification de l'utilisateur et horodatage
- Enregistrement de session pour les comptes partagés privilégiés dans la mesure du possible sur le plan technique
- Responsabilité individuelle maintenue via la journalisation d'audit
- Revue trimestrielle des accès et de l'utilisation ; reautorisation annuelle requise
- Procédures documentées dans ISMS-IMP-A.5.17

## Réinitialisation et récupération des mots de passe

### Réinitialisation en libre-service

Lorsque mise en œuvre, la réinitialisation en libre-service des mots de passe DOIT :

- Exiger une vérification basée sur AMF (push d'authentificateur, FIDO2, jeton matériel) pour les comptes privilégiés, l'accès distant et les systèmes critiques
- Les questions de sécurité basées sur la connaissance sont interdites sauf exception approuvée avec contrôles compensatoires documentés
- La vérification par courriel/SMS ne peut être utilisée que pour les comptes à faible risque là où approuvée dans l'évaluation du risque du système et où une surveillance supplémentaire est en place
- Utiliser des jetons de réinitialisation limités dans le temps (validité maximale de 1 heure)
- Journaliser toutes les activités de réinitialisation, y compris la méthode de vérification utilisée
- Alerter l'utilisateur du changement de mot de passe via son contact enregistré
- Ne pas révéler si un compte existe

### Réinitialisation assistée

Les réinitialisations de mots de passe assistées par le service d'assistance DOIVENT :

- Vérifier l'identité de l'utilisateur à l'aide d'informations pré-enregistrées
- Générer un mot de passe temporaire avec changement forcé
- Documenter la demande de réinitialisation et la méthode de vérification
- Communiquer le nouveau mot de passe via un canal sécurisé
- Ne pas divulguer les mots de passe au personnel de support après l'émission

---

# Rôles et responsabilités

## Matrice d'imputabilité

| Rôle | Responsabilités en matière d'authentification |
|------|-----------------------------------------------|
| **Direction générale** | Approuver la politique d'authentification, fournir les ressources pour la mise en œuvre |
| **RSSI** | Propriété de la politique, stratégie AMF, approbation des exceptions |
| **Exploitation informatique** | Mise en œuvre technique, configuration des systèmes, infrastructure des mots de passe |
| **Équipe GIA** | Provisionnement des utilisateurs, émission des identifiants, procédures de réinitialisation |
| **Service d'assistance** | Réinitialisation assistée des mots de passe, vérification de l'identité |
| **Propriétaires de systèmes** | Configuration de l'authentification spécifique au système, vérification de la conformité |
| **Tout le personnel** | Protection des identifiants, conformité à la politique, signalement des incidents |

## Chemin d'escalade

- Questions sur la politique d'authentification : Personnel → Équipe GIA → RSSI
- Demandes d'exception : Demandeur → Responsable hiérarchique → RSSI
- Incident d'authentification : Personnel → Équipe sécurité → RSSI → Direction générale

---

# Gouvernance et conformité

## Cadre d'évaluation

| Évaluation | Fréquence | Responsable | Preuve |
|------------|-----------|-------------|--------|
| Conformité de la politique des mots de passe | Mensuelle | Exploitation informatique | Audit de configuration des systèmes |
| Vérification de la couverture AMF | Trimestrielle | Équipe sécurité | Rapports des systèmes d'accès |
| Revue des journaux d'authentification | Mensuelle | Équipe sécurité | Rapports d'analyse SIEM |
| Scan des identifiants par défaut | Trimestrielle | Équipe sécurité | Résultats d'analyse de vulnérabilités |
| Vérification de la sensibilisation des utilisateurs | Annuelle | RH | Registres d'achèvement des formations |

**Indicateurs de gouvernance** :

- Taux d'adoption de l'AMF (cible : 100 % pour les systèmes obligatoires)
- Taux de conformité à la politique des mots de passe (cible : > 98 %)
- Distribution de l'âge moyen des mots de passe
- Schémas d'authentification échouée
- Volume de demandes de réinitialisation de mots de passe et délai de résolution
- Nombre de constatations d'identifiants par défaut (cible : 0)

## Révision de la politique

- **Fréquence** : Annuelle au minimum
- **Déclencheurs** : Évolutions des technologies d'authentification, incidents de sécurité, mises à jour réglementaires
- **Réviseurs** : RSSI, Exploitation informatique, Équipe GIA
- **Approbation** : Direction générale

## Gestion des exceptions

**Exceptions autorisées** :

- Systèmes hérités ne pouvant pas répondre aux exigences de complexité des mots de passe (avec mitigation documentée)
- Systèmes incompatibles avec l'AMF (avec contrôles compensatoires)
- Comptes de service nécessitant des politiques de mots de passe différentes (avec surveillance renforcée)

**Processus d'exception** :

1. Documenter la justification commerciale
2. Évaluation du risque par l'équipe sécurité
3. Approbation du RSSI avec contrôles compensatoires
4. Approbation limitée dans le temps (90 jours maximum, renouvelable)
5. Documentation dans le registre des exceptions

**Non autorisé** :

- Exceptions permettant le partage de mots de passe sans traçabilité
- Exceptions supprimant l'AMF pour les accès privilégiés
- Exceptions autorisant des identifiants par défaut en production

Toutes les exceptions DOIVENT être enregistrées dans le registre des exceptions (ISMS-REG-EXCEPTIONS).

## Lien avec les actions correctives

Les non-conformités liées à la présente politique (par exemple, configurations de mots de passe faibles, lacunes AMF, compromission d'identifiants, constatations d'identifiants par défaut) DOIVENT être enregistrées et gérées via le processus d'action corrective du SMSI (Clause 10.2) avec analyse des causes profondes et suivi des mesures correctives.

---

# Mise en œuvre et références

## Intégration au SMSI

La présente politique s'intègre au Système de management de la sécurité de l'information de [Organisation] :

**Appréciation du risque** (ISO 27001 Clause 6.1) :

- Les contrôles d'authentification sélectionnés sur la base de l'appréciation du risque de [Organisation]
- Les menaces de compromission des identifiants guident les exigences en matière de mots de passe et d'AMF
- Les plans de traitement du risque documentent la mise en œuvre des contrôles d'authentification

**Déclaration d'applicabilité (DdA)** (ISO 27001 Clause 6.1.3) :

- L'applicabilité du contrôle A.5.17 est justifiée dans la DdA de [Organisation]
- Le statut de mise en œuvre est suivi et rapporté

**Contrôles connexes** :

| Contrôle | Relation |
|----------|----------|
| **A.5.15-16-18** | La GIA définit les identités ; A.5.17 protège leur authentification |
| **A.8.2-3-5** | L'accès privilégié nécessite une authentification plus stricte |
| **A.8.24** | Protection cryptographique des informations d'authentification |
| **A.8.12** | Le DLP détecte les fuites d'identifiants |
| **A.8.15** | Journalisation des événements d'authentification |

**Intégration des contrôles empilés** :

A.5.17 (Informations d'authentification) s'articule avec les contrôles connexes pour assurer une protection complète :

| Contrôle empilé | Point d'intégration | Contribution de A.5.17 |
|-----------------|---------------------|------------------------|
| **A.5.15-16-18** (GIA) | Cycle de vie des identités | A.5.17 protège les identifiants ; la GIA gère les identités |
| **A.8.2-3-5** (Accès privilégié) | Authentification administrateur | A.5.17 définit les normes ; A.8.2 applique des exigences plus strictes |
| **A.8.24** (Cryptographie) | Protection des mots de passe | A.5.17 rend le hachage obligatoire ; A.8.24 spécifie les algorithmes |

L'évaluation de A.5.17 devrait référencer les évaluations des contrôles empilés pour une couverture complète.

## Ressources de mise en œuvre

**Orientations de mise en œuvre** (Suite ISMS-IMP-A.5.17) :

| Identifiant du document | Titre | Objet |
|-------------------------|-------|-------|
| **ISMS-IMP-A.5.17.1-UG/TG** | Guide de mise en œuvre de la politique des mots de passe | Procédures de configuration technique |
| **ISMS-IMP-A.5.17.2-UG/TG** | Évaluation du déploiement AMF | Déploiement et vérification de l'AMF |
| **ISMS-IMP-A.5.17.3-UG/TG** | Procédures de gestion de l'authentification | Procédures opérationnelles pour le cycle de vie des identifiants |

---

# Preuves pour cette politique

**Preuves d'étape 1 (revue de la documentation) :**

Les preuves requises à l'étape 1 comprennent :

- ✅ Ce document de politique (ISMS-POL-A.5.17 v1.0)
- ✅ Approbation enregistrée par le RSSI, le DSI, la direction générale
- ✅ Preuve de communication aux rôles concernés
- ✅ Normes de complexité des mots de passe définies (Exigences relatives aux mots de passe)
- ✅ Exigences AMF spécifiées (Authentification multifacteur)
- ✅ Procédures d'allocation initiale documentées (Allocation des informations d'authentification)
- ✅ Procédures de réinitialisation/récupération définies (Réinitialisation et récupération des mots de passe)
- ✅ Responsabilités des utilisateurs spécifiées (Protection des informations d'authentification)
- ✅ Rôles et responsabilités attribués (Rôles et responsabilités)

Le statut des preuves est suivi dans le registre des preuves du SMSI.

**Preuves d'étape 2 (efficacité opérationnelle) :**

Preuves requises pour démontrer l'efficacité opérationnelle de la présente politique :

- Exports de configuration de la politique des mots de passe montrant la complexité, l'historique et les paramètres de verrouillage
- Rapports de déploiement AMF montrant la couverture pour les types d'accès obligatoires
- Journaux d'authentification montrant la journalisation des événements et la détection des anomalies
- Registres de réinitialisation des mots de passe avec documentation de vérification de l'identité
- Résultats de scan des identifiants par défaut montrant l'absence d'identifiants par défaut
- Registres d'achèvement des formations à la sensibilisation à l'authentification
- Registre des exceptions avec approbation du RSSI et contrôles compensatoires
- Rapports d'incidents d'authentification et documentation de résolution

---

# Définitions

| Terme | Définition |
|-------|------------|
| **Informations d'authentification** | Données utilisées pour prouver l'identité, notamment les mots de passe, jetons, clés, données biométriques |
| **Authentification multifacteur (AMF)** | Authentification nécessitant deux facteurs de vérification ou plus provenant de catégories différentes |
| **Hachage de mot de passe** | Représentation cryptographique à sens unique d'un mot de passe |
| **Sel** | Données aléatoires ajoutées aux mots de passe avant le hachage pour prévenir les attaques par table arc-en-ciel |
| **Vérification hors bande** | Vérification de l'identité utilisant un canal de communication séparé |
| **Attaque par force brute** | Tentative de deviner les identifiants par essai systématique |
| **Bourrage d'identifiants** | Attaque utilisant des identifiants divulgués provenant d'autres violations |

---

# Registre d'approbation

| Rôle | Nom | Date |
|------|-----|------|
| **Responsable de la sécurité des systèmes d'information (RSSI)** | [Nom] | [Date à définir] |
| **Directeur des systèmes d'information (DSI)** | [Nom] | [Date à définir] |
| **Direction générale** | [Nom] | [Date à définir] |

---

**FIN DU DOCUMENT DE POLITIQUE**

---

*La présente politique établit les exigences en matière de gestion des informations d'authentification. Les procédures de mise en œuvre sont documentées dans ISMS-IMP-A.5.17 (UG/TG).*

<!-- QA_VERIFIED: 2026-03-30 -->
