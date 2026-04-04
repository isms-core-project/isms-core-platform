<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.5.17-FR:operational:OP-POL:a.5.17 -->
**ISMS-OP-POL-A.5.17 — Informations d'authentification**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Informations d'authentification |
| **Type de document** | Politique opérationnelle |
| **Identifiant du document** | ISMS-OP-POL-A.5.17 |
| **Créateur du document** | Responsable de la Sécurité des Systèmes d'Information (RSSI) |
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
| 1.0 | [Date] | RSSI | Politique opérationnelle initiale pour ISO 27001:2022 |

**Cycle de révision** : Annuel
**Prochaine date de révision** : [Date d'entrée en vigueur + 12 mois]

**Approuvé par** : [RSSI / Direction générale]

**Documents connexes** :

- ISO/IEC 27001:2022 Contrôle A.5.17 — Informations d'authentification
- NIST SP 800-63B-4 — Lignes directrices sur l'identité numérique : authentification et gestion des authentificateurs

**Contrôles Annexe A connexes** :

| Contrôle | Relation avec les informations d'authentification |
|----------|--------------------------------------------------|
| A.5.15–18 Contrôle d'accès et gestion des identités | Le cycle de vie des identités alimente l'authentification ; les droits d'accès déterminent la portée des identifiants |
| A.5.24–28 Gestion des incidents | La compromission d'identifiants déclenche la réponse aux incidents et le changement de mot de passe forcé |
| A.8.2 Droits d'accès privilégiés | Les comptes à privilèges requièrent une authentification plus stricte (MFA, clés matérielles) |
| A.8.3 Restriction de l'accès à l'information | L'authentification applique les frontières d'accès |
| A.8.5 Authentification sécurisée | Mise en œuvre technique du mécanisme d'authentification |
| A.8.15 Journalisation | Les événements d'authentification alimentent la journalisation centralisée |
| A.8.16 Surveillance des activités | Surveillance en temps réel des échecs et anomalies d'authentification |
| A.8.24 Utilisation de la cryptographie | Protection cryptographique des identifiants, jetons et hachages de mots de passe |

**Politiques internes connexes** :

- Politique de gestion des identités et des accès
- Politique d'authentification et d'accès privilégié
- Politique d'utilisation de la cryptographie
- Politique de journalisation
- Politique de surveillance des activités (A.8.16)
- Politique de gestion des incidents

---

# Politique relative aux informations d'authentification

## Objet

La présente politique a pour objet de garantir que les informations d'authentification sont allouées, gérées, protégées et révoquées de manière sécurisée à travers des processus de cycle de vie définis, et que le personnel reçoit des instructions sur la gestion sécurisée des identifiants d'authentification.

Cette politique établit les exigences relatives aux normes de mots de passe, à l'authentification multifacteur, à la distribution des identifiants et à la protection des secrets d'authentification, afin de prévenir tout accès non autorisé aux systèmes et aux données de l'organisation.

Cette politique soutient les exigences de la nLPD suisse (revDSG) art. 8 en mettant en œuvre des mesures techniques et organisationnelles proportionnées aux risques pour protéger les données personnelles (y compris les données personnelles sensibles) par des contrôles d'authentification. Lorsque l'organisation traite des données de personnes dans l'UE/EEE, les exigences du RGPD s'appliquent également.

## Champ d'application

Cette politique s'applique à :

- Tous les employés, contractants et utilisateurs tiers ayant accès aux systèmes de l'organisation.
- Toutes les informations d'authentification, notamment les mots de passe, phrases secrètes, codes PIN, clés cryptographiques, jetons, modèles biométriques, clés API, certificats et autres secrets d'authentification.
- Tous les systèmes, applications, services cloud, périphériques réseau et bases de données détenus ou exploités par l'organisation et considérés dans le périmètre de la déclaration de périmètre ISO 27001.
- Tous les processus du cycle de vie de l'authentification : allocation, distribution, utilisation, stockage, réinitialisation et révocation.

## Principe

Les informations d'authentification doivent être gérées selon les principes de confidentialité, de responsabilité individuelle et de défense en profondeur. Chaque utilisateur doit être positivement identifié et authentifié avant d'accéder aux systèmes ou aux données. Les mécanismes d'authentification doivent être proportionnés à la sensibilité des informations et des systèmes auxquels ils donnent accès.

Les mots de passe seuls ne sont pas suffisants pour les accès à haut risque. L'authentification multifacteur offre une protection en couches contre la compromission des identifiants. Les contrôles d'authentification doivent être fondés sur les risques, en tenant compte de la classification des informations et de la criticité du système.

---

## Infrastructure d'authentification

> **Spécification des systèmes** : L'organisation utilise les systèmes suivants pour mettre en œuvre les contrôles d'authentification. Les références à des espaces réservés (p. ex. [Fournisseur d'identité]) dans cette politique renvoient aux systèmes listés ci-dessous.
>
> | Fonction | Système/Outil | Responsable |
> |----------|---------------|-------------|
> | **Fournisseur d'identité (IdP)** | [p. ex. Microsoft Entra ID, Okta, Google Workspace Identity] | Opérations IT / Équipe GIA |
> | **Gestionnaire de mots de passe** | [p. ex. 1Password Business, Bitwarden Enterprise, KeePass + synchronisation centralisée] | Sécurité IT |
> | **Plateforme MFA** | [p. ex. MFA IdP intégré, Duo Security, gestion YubiKey] | Opérations IT |
> | **Gestion des accès privilégiés (PAM)** | [p. ex. CyberArk, Delinea Secret Server, HashiCorp Vault] | Sécurité IT |
> | **Service de vérification des fuites** | [p. ex. Have I Been Pwned API (modèle k-anonymat), Enzoic, Microsoft Password Protection] | Opérations IT |
> | **SIEM / Gestion des journaux** | [p. ex. Microsoft Sentinel, Splunk, Elastic SIEM] | Sécurité IT |

---

## Allocation des informations d'authentification

### Vérification d'identité

Avant d'émettre des identifiants d'authentification nouveaux ou de remplacement, l'identité de la personne demandeuse doit être vérifiée par au moins l'une des méthodes suivantes :

- Vérification d'un contact secondaire pré-enregistré (adresse e-mail, numéro de téléphone mobile).
- Vérification en personne avec pièce d'identité avec photo.
- Confirmation de l'identité de l'utilisateur par le responsable ou les RH.
- Processus de libre-service vérifié par MFA via le fournisseur d'identité [Fournisseur d'identité].

La méthode de vérification utilisée doit être documentée à des fins d'audit.

### Distribution sécurisée

Les informations d'authentification doivent être distribuées via des canaux sécurisés. Les méthodes non sécurisées telles que les e-mails non chiffrés ou les messages en texte clair ne doivent pas être utilisées pour la distribution des identifiants.

| Type d'authentification | Méthode de distribution |
|------------------------|------------------------|
| **Mots de passe initiaux** | Canal sécurisé (e-mail chiffré, enveloppe scellée ou auto-inscription via le fournisseur d'identité) ; séparé du nom d'utilisateur ; changement forcé à la première utilisation |
| **Jetons / clés matérielles** | Remise en mains propres avec vérification d'identité et reçu signé |
| **Certificats** | Processus d'enrôlement sécurisé des certificats ; vérification par e-mail ou workflow du fournisseur d'identité |
| **Clés API** | Canal chiffré ; durée de validité limitée ; émission journalisée ; stockées dans un coffre-fort de secrets |

### Authentification temporaire

Les identifiants d'authentification temporaires (mots de passe initiaux, jetons de réinitialisation, codes à usage unique) :

- Doivent avoir une validité maximale de 24 heures.
- Doivent être changés à la première utilisation.
- Doivent être générés avec une entropie et une longueur suffisantes pour résister aux tentatives de devinette.
- Doivent être invalidés après utilisation réussie.

### Gestion des identifiants par défaut

Les mots de passe fournis par les fournisseurs et les mots de passe par défaut doivent être changés immédiatement lors de l'installation, avant toute connexion du système au réseau de production.

Les comptes par défaut doivent être désactivés ou renommés lorsque cela est techniquement réalisable.

Lorsque les identifiants par défaut ne peuvent pas être modifiés (dépendance vis-à-vis du firmware du fournisseur, limitation du système), les mesures compensatoires suivantes doivent être appliquées :

- Mot de passe fort unique défini par appareil (pas le mot de passe par défaut du fournisseur).
- Segmentation réseau restreignant l'accès à l'appareil.
- MFA appliqué si supporté.
- Surveillance et alertes renforcées sur le compte.
- Identifiant stocké dans le coffre-fort d'identifiants approuvé [Gestionnaire de mots de passe].
- Exception documentée avec approbation du RSSI et révision annuelle.

---

## Exigences relatives aux mots de passe

### Normes de mots de passe (conformes à NIST SP 800-63B)

L'organisation doit appliquer les normes de mots de passe suivantes, conformément à NIST SP 800-63B-4 :

| Exigence | Norme |
|----------|-------|
| **Longueur minimale** | 12 caractères (15 caractères lorsque le mot de passe est le seul authentificateur sans MFA) |
| **Longueur maximale** | Les systèmes doivent accepter au moins 64 caractères pour prendre en charge les phrases secrètes |
| **Prise en charge des caractères** | Tous les caractères ASCII imprimables (y compris l'espace) et Unicode doivent être acceptés |
| **Règles de complexité** | Aucune règle de composition obligatoire (pas de mélange requis de majuscules, minuscules, chiffres, symboles) ; la longueur est le principal facteur de robustesse |
| **Vérification des fuites** | Les mots de passe doivent être validés par rapport aux bases de données d'identifiants compromis/divulgués (p. ex. Have I Been Pwned API, ou corpus de fuites équivalent intégré à [Fournisseur d'identité]) lors de la création et périodiquement. **Fréquence de vérification** : à la création du mot de passe (obligatoire), à chaque authentification lorsque techniquement réalisable (vérification en temps réel via intégration IdP), et vérification par lots de tous les hachages de mots de passe stockés trimestriellement (vérification hors ligne par rapport au corpus de fuites mis à jour). |
| **Rotation** | Basée sur les événements uniquement — en cas de compromission suspectée ou avérée, de découverte d'identifiants partagés, ou de changement de rôle du personnel affectant la portée des accès ; la rotation périodique forcée n'est pas requise |
| **Mots de passe initiaux** | Doivent être changés à la première utilisation |
| **Mots de passe par défaut** | Les mots de passe fournis par les fournisseurs et les mots de passe par défaut sont changés immédiatement lors de l'installation |
| **Réutilisation** | Un historique d'au moins 24 mots de passe précédents doit être maintenu pour prévenir la réutilisation |
| **Partage** | Les mots de passe ne doivent pas être génériques, partagés ou définis au niveau d'un groupe |
| **Verrouillage** | Les systèmes doivent verrouiller les utilisateurs après 6 tentatives d'accès échouées ; durée de verrouillage minimale de 15 minutes ou jusqu'à réinitialisation manuelle |
| **Gestionnaires de mots de passe** | L'utilisation de gestionnaires de mots de passe approuvés par l'organisation [Gestionnaire de mots de passe] est recommandée et supportée ; les systèmes doivent permettre le collage dans les champs de mot de passe |

**Normes de mots de passe pour les comptes à privilèges** :

Les comptes à privilèges (administrateur, comptes de niveau 0/1) doivent appliquer :

- Minimum 16 caractères (ou 24 caractères pour les comptes de service).
- Verrouillage après 3 tentatives échouées.
- Vérification des fuites à la création et à chaque authentification lorsque techniquement réalisable.
- Stockage dans le coffre-fort d'identifiants approuvé [Gestionnaire de mots de passe].

**Justification de la rotation basée sur les événements** : NIST SP 800-63B-4 établit que la rotation périodique obligatoire des mots de passe conduit à des mots de passe plus faibles (schémas prévisibles, modifications incrémentales minimales) sans bénéfice de sécurité mesurable. La rotation basée sur les événements combinée à la vérification des fuites et au MFA offre une protection plus solide.

### Pratiques de mots de passe interdites

Le personnel ne doit pas :

- Partager des mots de passe avec quelque personne que ce soit, y compris le personnel du support IT.
- Écrire des mots de passe dans des emplacements non protégés (notes autocollantes, fichiers non chiffrés, cahiers).
- Stocker des mots de passe dans des fichiers en texte clair, documents, feuilles de calcul ou dans la saisie automatique du navigateur sans gestionnaire de mots de passe approuvé.
- Utiliser le même mot de passe sur plusieurs systèmes ou services.
- Inclure des mots de passe dans des scripts, du code, des macros ou des fichiers de configuration.
- Transmettre des mots de passe via des canaux non chiffrés (corps d'e-mail, messagerie instantanée, SMS).

### Stockage des mots de passe

Les systèmes doivent stocker les mots de passe en utilisant un hachage cryptographique à sens unique approuvé avec sel unique par mot de passe :

- **Algorithmes approuvés** : bcrypt, Argon2id, scrypt ou PBKDF2 (avec un nombre d'itérations approprié aux capacités matérielles actuelles).
- **Le stockage en texte clair est interdit** en toutes circonstances.
- **Le chiffrement réversible des mots de passe est interdit.**
- Les bases de données de mots de passe doivent être protégées par chiffrement au repos et l'accès restreint aux comptes de service autorisés.

---

## Authentification multifacteur

### Exigences MFA

L'authentification multifacteur doit être requise pour les types d'accès suivants :

| Type d'accès | Exigence MFA |
|-------------|-------------|
| **Accès à distance** (VPN, services cloud, applications accessibles de l'extérieur) | Obligatoire |
| **Comptes à privilèges / administrateur** | Obligatoire |
| **Systèmes critiques et infrastructure** | Obligatoire |
| **Systèmes traitant des données personnelles** (périmètre nLPD / RGPD) | Obligatoire |
| **Messagerie** (accès externe) | Obligatoire |
| **Consoles d'administration de plateformes cloud** | Obligatoire |
| **Accès interne standard** (sur site, réseau de confiance) | Basé sur les risques ; la mise en œuvre est déterminée par la classification du système et enregistrée dans la politique d'accès conditionnel de [Fournisseur d'identité] |

**Objectifs de couverture MFA** :

- Utilisateurs à privilèges : 100 % d'enrôlement MFA à partir de la date d'entrée en vigueur de la politique.
- Tous les utilisateurs (accès à distance) : 100 % d'application du MFA.
- Tous les utilisateurs (tous les accès) : enrôlement MFA ≥ 95 % dans les 12 mois suivant l'adoption de la politique.

### Types de facteurs MFA

Les facteurs d'authentification acceptables doivent être tirés d'au moins deux catégories différentes :

| Catégorie de facteur | Exemples | Remarques |
|---------------------|----------|-----------|
| **Ce que vous savez** | Mot de passe, phrase secrète, code PIN | Conformément aux normes de mots de passe ci-dessus |
| **Ce que vous avez** | Clé de sécurité matérielle (FIDO2/WebAuthn), application d'authentification (TOTP), carte à puce | Enregistrée à l'utilisateur individuel ; clés matérielles préférées pour l'accès privilégié |
| **Ce que vous êtes** | Empreinte digitale, reconnaissance faciale, scanner de l'iris | Modèle biométrique stocké de manière sécurisée ; utilisé comme facteur de déverrouillage local |

### Préférence des méthodes MFA

Les méthodes MFA doivent être sélectionnées en privilégiant la résistance au phishing :

| Méthode | Résistance au phishing | Utilisation recommandée |
|---------|----------------------|------------------------|
| **Clés de sécurité matérielles** (FIDO2/WebAuthn) | Élevée — liées cryptographiquement à l'origine | Requises pour les comptes de plus haut privilège ; recommandées pour tous les utilisateurs |
| **Clés d'accès (passkeys)** (liées à l'appareil, non exportables) | Élevée — liées à l'origine, vérifiées par l'utilisateur | Acceptables pour tous les types d'accès ; préférées au TOTP |
| **Applications d'authentification** (TOTP) | Moyenne — les codes peuvent être hameçonnés en temps réel | Acceptables pour l'accès standard et à privilèges modérés |
| **Notifications push** (avec correspondance de numéro) | Moyenne — nécessite une correspondance de numéro pour atténuer les attaques par fatigue | Acceptables lorsque la correspondance de numéro est appliquée |
| **SMS / OTP vocal** | Faible — vulnérable à l'échange de SIM et à l'interception | Uniquement lorsqu'aucune autre méthode n'est techniquement réalisable ; exception documentée requise |

Le recours à l'OTP par SMS doit être documenté dans le registre des risques avec un plan de migration vers une méthode plus robuste. Les nouveaux déploiements de systèmes ne doivent pas mettre en œuvre le MFA par SMS comme seul second facteur.

**Feuille de route de migration vers l'authentification résistante au phishing** :

L'organisation doit planifier et exécuter la migration vers une authentification résistante au phishing (clés d'accès FIDO2/WebAuthn) comme méthode MFA principale. FIDO2 utilise la cryptographie à clé publique liée à l'origine légitime du service, empêchant le hameçonnage des identifiants même si les utilisateurs sont trompés par des sites frauduleux.

| Phase | Calendrier | Périmètre | Objectif |
|-------|------------|-----------|----------|
| **Phase 1 — Pilote** | Mois 1-3 | Équipe IT, équipe sécurité, RSSI | 100 % du groupe pilote utilisant des clés matérielles FIDO2 |
| **Phase 2 — Utilisateurs à privilèges** | Mois 3-6 | Tous les comptes à privilèges/admin, dirigeants | 100 % des comptes à privilèges sur FIDO2/clés d'accès |
| **Phase 3 — Utilisateurs à haut risque** | Mois 6-12 | Utilisateurs avec accès aux données CONFIDENTIEL, travailleurs à distance | ≥ 80 % des utilisateurs à haut risque migrés |
| **Phase 4 — Déploiement général** | Mois 12-24 | Tous les utilisateurs | ≥ 90 % de tous les utilisateurs utilisant le MFA résistant au phishing ; SMS/OTP vocal éliminés |

**Suivi de la migration** : Avancement rapporté trimestriellement au RSSI avec : utilisateurs migrés (nombre et %), utilisateurs SMS/TOTP restants, blocages (systèmes legacy, résistance des utilisateurs), état du stock de clés matérielles.

### Processus de récupération MFA

Lorsqu'un utilisateur perd l'accès à son dispositif MFA (téléphone perdu, clé matérielle défaillante, réinitialisation d'usine) :

1. **Contact helpdesk** : L'utilisateur contacte le helpdesk IT avec vérification d'identité (même procédure que la réinitialisation de mot de passe assistée par le helpdesk).
2. **Accès temporaire** : Le helpdesk émet un code de contournement à durée limitée (validité maximale 24 heures, à usage unique) pour permettre un accès immédiat pendant le ré-enrôlement du MFA.
3. **Ré-enrôlement MFA** : L'utilisateur se ré-enrôle dans le MFA dans les 24 heures via le portail en libre-service de [Fournisseur d'identité]. Si le ré-enrôlement n'est pas effectué dans les 24 heures, l'accès est suspendu jusqu'à la réalisation de l'enrôlement.
4. **Clé matérielle perdue** : Signalée comme incident de sécurité (compromission physique potentielle). La clé précédente est désenregistrée immédiatement. Une clé de remplacement est émise en mains propres avec vérification d'identité.
5. **Méthode MFA de sauvegarde** : Les utilisateurs sont encouragés à enregistrer une méthode MFA de sauvegarde (p. ex. seconde clé matérielle stockée en lieu sûr, application d'authentification de sauvegarde). Les utilisateurs à privilèges doivent enregistrer au moins deux méthodes MFA indépendantes.
6. **Journalisation** : Tous les événements de récupération MFA sont journalisés dans [SIEM] avec l'utilisateur, l'horodatage, la méthode de vérification et la méthode de récupération utilisée. Les schémas anormaux (p. ex. même utilisateur récupérant le MFA plusieurs fois) sont examinés dans les 24 heures.

### Exigences relatives à l'authentification biométrique

Lorsque l'authentification biométrique est utilisée (empreinte digitale, reconnaissance faciale, scanner de l'iris) :

- **Stockage des modèles** : Les modèles biométriques doivent être stockés localement sur l'appareil (pas de manière centralisée) lorsque cela est techniquement réalisable. Si un stockage centralisé est requis, les modèles doivent être chiffrés au repos avec AES-256.
- **Détection de vivacité** : Les systèmes biométriques doivent mettre en œuvre la détection de vivacité pour prévenir les attaques par rejeu (p. ex. photographies, empreintes en silicone).
- **Solution de repli** : Une méthode d'authentification non biométrique de repli doit toujours être disponible (la biométrie ne doit pas être le seul facteur d'authentification).
- **Consentement** : Le personnel doit donner son consentement éclairé avant l'enrôlement biométrique, conformément aux exigences de la nLPD suisse concernant le traitement des données personnelles sensibles.
- **Révocation** : Les modèles biométriques doivent être supprimés à la fin du contrat de travail ou lorsque l'individu retire son consentement.
- **Précision** : Les systèmes biométriques doivent être configurés avec un taux de fausse acceptation (FAR) approprié au niveau de risque (recommandé : FAR ≤ 1:50 000 pour l'accès standard, FAR ≤ 1:1 000 000 pour l'accès privilégié).

### Systèmes ne pouvant pas prendre en charge le MFA

Les systèmes ne pouvant pas prendre en charge le MFA doivent être documentés dans le registre des risques avec :

- Justification technique de la limitation.
- Mesures compensatoires (segmentation réseau, restriction IP, surveillance renforcée, délai de session réduit).
- Acceptation du risque approuvée par le RSSI.
- Révision annuelle et plan de migration si réalisable.

---

## Protection des informations d'authentification

### Responsabilités des utilisateurs

Tout le personnel doit :

- Garder les informations d'authentification confidentielles et ne pas les divulguer à quelque autre personne que ce soit.
- Utiliser des mots de passe ou des phrases secrètes forts et uniques pour chaque système.
- Utiliser le gestionnaire de mots de passe approuvé par l'organisation [Gestionnaire de mots de passe] pour le stockage sécurisé des identifiants.
- Signaler immédiatement toute compromission suspectée ou avérée d'identifiants au service d'assistance IT et à l'équipe de sécurité.
- Ne pas autoriser d'autres personnes à utiliser leurs identifiants ou à s'authentifier en leur nom.
- Compléter l'enrôlement MFA dans le délai requis.
- Ne pas tenter de contourner les contrôles d'authentification.

### Réponse à la compromission d'identifiants

Lorsqu'une compromission d'identifiants est suspectée ou avérée :

1. **Réinitialisation immédiate du mot de passe** : L'utilisateur concerné réinitialise son mot de passe via le libre-service de [Fournisseur d'identité] (vérifié par MFA) ou via le processus assisté par le helpdesk. Pour les comptes à privilèges : la sécurité IT force la réinitialisation immédiate du mot de passe.
2. **Vérification du MFA** : Vérifier que les facteurs MFA n'ont pas été altérés (aucun appareil non autorisé enregistré). Si des appareils MFA suspects sont trouvés, supprimer tous les enregistrements MFA et se ré-enrôler depuis un appareil de confiance.
3. **Résiliation des sessions** : Toutes les sessions actives du compte concerné sont terminées immédiatement via la console d'administration de [Fournisseur d'identité].
4. **Évaluation de l'étendue de la violation** : La sécurité IT examine : à quoi a-t-on accédé en utilisant l'identifiant compromis ? D'autres comptes ont-ils été affectés (réutilisation des identifiants) ? Des données ont-elles été exfiltrées ?
5. **Vérification des fuites** : Vérifier le hachage du mot de passe compromis par rapport au corpus de fuites. S'il est trouvé dans une base de données de fuites externe, évaluer l'étendue de l'exposition.
6. **Notification** : Si la compromission impliquait un accès à des données personnelles, évaluer les obligations de notification de violation conformément à A.5.24-28 Gestion des incidents et à la législation applicable sur la protection des données.
7. **Cause profonde** : Déterminer comment les identifiants ont été compromis (hameçonnage, logiciel malveillant, ingénierie sociale, force brute, violation d'un service externe). Mettre en œuvre des mesures correctives ciblées (p. ex. formation de sensibilisation au phishing si le hameçonnage était le vecteur).
8. **Documentation** : Incident enregistré dans [Outil ITSM] avec : compte concerné, vecteur de compromission, portée des accès pendant la fenêtre de compromission, actions correctives, cause profonde, mesures préventives.

### Exigences des systèmes

Le système d'authentification d'accès principal doit :

- Ne pas afficher les identifiants du système ou de l'application tant que le processus de connexion n'a pas été achevé avec succès.
- Afficher un avertissement général indiquant que le système ne doit être accessible que par des utilisateurs autorisés.
- Ne pas fournir de messages d'aide pendant la procédure de connexion qui aideraient un utilisateur non autorisé.
- Valider les informations de connexion uniquement à la saisie complète de toutes les données ; en cas d'erreur, le système ne doit pas indiquer quelle partie des données est correcte ou incorrecte.
- Protéger contre les tentatives de connexion par force brute (limitation du débit, délai progressif, CAPTCHA ou verrouillage du compte).
- Journaliser toutes les tentatives d'authentification réussies et échouées.
- Déclencher un événement de sécurité si une tentative ou une violation avérée des contrôles de connexion est détectée.
- Ne pas afficher un mot de passe en cours de saisie (masquer la saisie).
- Ne pas transmettre les mots de passe en clair sur un réseau.
- Mettre fin aux sessions inactives après une période d'inactivité définie.
- Restreindre les durées de connexion pour renforcer la sécurité des applications à haut risque.

**Exigences de délai d'expiration des sessions** :

| Classification du système | Délai d'inactivité | Délai absolu |
|--------------------------|-------------------|--------------|
| Systèmes CONFIDENTIEL / critiques | 15 minutes | 8 heures |
| Systèmes traitant des données personnelles sensibles | 5 minutes | 4 heures |
| Consoles d'administration à privilèges | 10 minutes | 4 heures |
| Systèmes métiers standard | 30 minutes | 12 heures |

Le délai absolu nécessite une ré-authentification quelle que soit l'activité.

### Informations d'authentification partagées

Les informations d'authentification partagées sont déconseillées et doivent être évitées dans la mesure du possible. Lorsque des identifiants partagés sont requis (systèmes legacy, comptes imposés par des fournisseurs) :

- L'approbation du RSSI est obligatoire avec une justification professionnelle documentée.
- Les identifiants doivent être stockés dans le coffre-fort d'identifiants approuvé [Gestionnaire de mots de passe], et non dans des documents en texte clair, des e-mails ou des messageries.
- Un dépositaire nommé doit être désigné pour chaque identifiant partagé.
- La journalisation des emprunts avec identification de l'utilisateur et horodatage doit être maintenue.
- L'enregistrement des sessions est recommandé pour les comptes partagés à privilèges lorsque cela est techniquement réalisable.
- La responsabilité individuelle doit être maintenue grâce à la journalisation d'audit.
- L'accès et l'utilisation doivent être examinés trimestriellement ; une réautorisation annuelle est requise.
- Les comptes partagés doivent être inclus dans le registre des comptes à privilèges et dans le processus de révision des accès.

---

## Réinitialisation et récupération des mots de passe

### Réinitialisation des mots de passe en libre-service

Lorsque la réinitialisation des mots de passe en libre-service est mise en œuvre via [Fournisseur d'identité] :

- La vérification par MFA (authentification push, FIDO2 ou jeton matériel) doit être requise avant toute réinitialisation de mot de passe.
- Les questions de sécurité basées sur la connaissance ne doivent pas être utilisées comme seule méthode de vérification en raison de leur vulnérabilité à l'ingénierie sociale.
- Les jetons de réinitialisation doivent avoir une durée de validité limitée (validité maximale de 1 heure) et être à usage unique.
- Toutes les activités de réinitialisation doivent être journalisées, y compris la méthode de vérification utilisée.
- L'utilisateur doit être notifié du changement de mot de passe via un contact secondaire enregistré (e-mail ou mobile).
- Le processus de réinitialisation ne doit pas révéler si un compte existe (prévenir l'énumération des comptes).

### Réinitialisation des mots de passe assistée par le helpdesk

Les réinitialisations de mots de passe assistées par le helpdesk doivent suivre cette procédure :

1. **Vérifier l'identité** : Le helpdesk doit vérifier l'identité de l'appelant en utilisant au moins une méthode de vérification pré-enregistrée (e-mail secondaire, numéro de mobile enregistré, confirmation du responsable ou en personne avec pièce d'identité avec photo).
2. **Générer un mot de passe temporaire** : Un mot de passe temporaire aléatoire doit être généré en respectant les exigences de longueur minimale.
3. **Communiquer de manière sécurisée** : Le mot de passe temporaire doit être communiqué via un canal sécurisé (pas par e-mail non chiffré) ; dans la mesure du possible, utiliser le lien de réinitialisation sécurisé du fournisseur d'identité.
4. **Forcer le changement** : Le mot de passe temporaire doit expirer à la première utilisation, obligeant l'utilisateur à définir immédiatement un nouveau mot de passe.
5. **Documenter** : La demande de réinitialisation, la méthode de vérification utilisée et l'horodatage doivent être enregistrés dans le système de gestion des services IT.

Le personnel du helpdesk ne doit pas avoir accès aux mots de passe des utilisateurs après leur émission.

---

## Rôles et responsabilités

| Rôle | Responsabilités |
|------|----------------|
| **Direction générale** | Approuver la politique ; allouer le budget pour l'infrastructure d'authentification (MFA, gestionnaire de mots de passe, fournisseur d'identité) ; examiner les indicateurs de sécurité trimestriellement |
| **RSSI** | Responsabilité de la politique ; approuver la stratégie MFA et la feuille de route d'authentification résistante au phishing ; approuver les exceptions (risque moyen/élevé) ; examiner les rapports de conformité trimestriels |
| **Responsable de la sécurité IT** | Gestion quotidienne de la sécurité de l'authentification ; surveiller les alertes et anomalies d'authentification ; conduire les révisions trimestrielles de couverture MFA ; approuver les exceptions à faible risque |
| **Opérations IT / Équipe GIA** | Gérer [Fournisseur d'identité] et l'infrastructure d'authentification ; traiter l'émission et la réinitialisation des identifiants ; maintenir l'enrôlement MFA ; configurer les paramètres de politique de mot de passe ; intégrer la vérification des fuites |
| **Helpdesk** | Exécuter les réinitialisations de mots de passe assistées par le helpdesk selon la procédure documentée ; vérifier l'identité de l'utilisateur avant tout changement d'identifiant ; escalader les demandes de réinitialisation suspectes à la sécurité IT |
| **Propriétaires de systèmes** | Veiller à ce que les systèmes sous leur responsabilité soient conformes aux exigences d'authentification ; mettre en œuvre le MFA lorsqu'il est imposé ; signaler les lacunes dans les contrôles d'authentification |
| **Tout le personnel** | Protéger les identifiants d'authentification ; compléter l'enrôlement MFA dans le délai requis ; signaler immédiatement toute compromission suspectée d'identifiants ; ne pas partager de comptes ou d'identifiants ; se conformer aux normes de mots de passe |

---

## Preuves

Les preuves suivantes démontrent la conformité à cette politique :

| # | Preuve | Responsable | Fréquence |
|---|--------|-------------|-----------|
| 1 | **Preuve de configuration de la politique de mots de passe** (paramètres de [Fournisseur d'identité] : longueur minimale, vérification des fuites, verrouillage, historique) | Opérations IT | Capturée annuellement et lors de tout changement |
| 2 | **Rapports d'enrôlement MFA** (pourcentage de couverture par type d'utilisateur : à privilèges, standard, à distance) | Sécurité IT | Mensuel pour les utilisateurs à privilèges ; trimestriel pour tous les utilisateurs |
| 3 | **Distribution des méthodes MFA** (FIDO2, TOTP, push, SMS — avancement de la migration vers les méthodes résistantes au phishing) | Sécurité IT | Trimestriel |
| 4 | **Preuve de configuration de vérification des fuites** (intégration avec la base de données d'identifiants compromis, fréquence de vérification) | Opérations IT | Annuellement et lors de tout changement |
| 5 | **Résultats d'analyse des identifiants par défaut** (aucun identifiant par défaut ou fourni par un fournisseur en production) | Sécurité IT | Trimestriel |
| 6 | **Journaux d'événements d'authentification** (connexions réussies/échouées, verrouillages, investigations d'anomalies, alertes de déplacement impossible) | Sécurité IT | Conservés 12 mois ; anomalies examinées dans les 24 heures |

**Exemples d'anomalies d'authentification** (indicateurs déclenchant une investigation) :

| Type d'anomalie | Méthode de détection | Réponse |
|----------------|---------------------|---------|
| **Déplacement impossible** | Connexion depuis deux endroits géographiquement distants dans un délai de déplacement impossible | Bloquer la seconde session ; notifier l'utilisateur ; investiguer |
| **Force brute** | > 10 tentatives de connexion échouées en 5 minutes depuis une source unique | Bloquer l'IP source ; notifier la sécurité IT |
| **Bourrage d'identifiants** | Plusieurs comptes ciblés avec des connexions échouées depuis la même plage IP | Bloquer la plage IP ; examiner les comptes concernés ; notifier la sécurité IT |
| **Fatigue MFA** | > 3 notifications push MFA refusées en 10 minutes | Bloquer le compte ; contacter l'utilisateur via un canal secondaire pour vérification |
| **Horaires inhabituels** | Connexion en dehors des horaires normaux de travail pour les travailleurs non en équipe | Journaliser et examiner ; alerter si combiné à d'autres anomalies |
| **Nouvel appareil/emplacement** | Première connexion depuis un appareil ou un emplacement non reconnu | Authentification renforcée (défi MFA supplémentaire) ; notifier l'utilisateur |
| **Élévation de privilèges** | Utilisateur doté de privilèges élevés sans demande de changement approuvée | Investigation immédiate ; annulation si non autorisé |
| 7 | **Journaux de réinitialisation des mots de passe** (libre-service et assisté par le helpdesk ; méthode de vérification d'identité documentée) | Opérations IT | Par événement ; audité semestriellement |
| 8 | **Registre des identifiants partagés** (compte, dépositaire, emplacement dans le coffre-fort, dernière révision, date de réautorisation) | Sécurité IT | Révisé trimestriellement |
| 9 | **Registre des exceptions** (systèmes sans MFA, limitations de mots de passe legacy, MFA par SMS uniquement — avec mesures compensatoires et approbation du RSSI) | Sécurité IT | Révisé trimestriellement ; chaque exception de 12 mois maximum |
| 10 | **Registres de completion de la formation de sensibilisation à l'authentification** | RH / Sécurité IT | Annuellement |

### Exigences de formation à l'authentification

Tout le personnel doit compléter une formation de sensibilisation à l'authentification comme suit :

| Module de formation | Public | Fréquence | Contenu |
|--------------------|--------|-----------|---------|
| **Sensibilisation à la sécurité — bases de l'authentification** | Tout le personnel | Annuel (dans le cadre de la sensibilisation obligatoire à la sécurité) | Hygiène des mots de passe, enrôlement MFA, reconnaissance du phishing, signalement des identifiants |
| **Intégration au gestionnaire de mots de passe** | Tout le personnel | À l'intégration + lors d'un changement d'outil | Configuration de [Gestionnaire de mots de passe], création du coffre-fort, extension de navigateur, application mobile, accès d'urgence |
| **Formation à l'accès privilégié** | Utilisateurs à privilèges (administrateurs, DBAs, équipe sécurité) | Annuel + lors de la prise de poste | Utilisation de l'outil PAM, emprunt/restitution dans le coffre-fort d'identifiants, sensibilisation à l'enregistrement des sessions, gestion des clés matérielles MFA |
| **Simulation de phishing** | Tout le personnel | Trimestriel | Campagnes de phishing simulées testant la sensibilisation à la collecte d'identifiants ; résultats rapportés au RSSI ; recyclage ciblé pour le personnel qui échoue |
| **Gestion des comptes de service** | Propriétaires de systèmes, DevOps, opérations IT | Annuel | Cycle de vie des comptes de service, stockage des identifiants (pas de codage en dur), procédures de rotation, mise hors service |

**Mesure de l'efficacité de la formation** : Le taux de clic lors des simulations de phishing est suivi trimestriellement (objectif : < 5 %). Le personnel qui échoue deux simulations de phishing en 12 mois reçoit une formation individuelle de sécurité obligatoire.

---

# Conformité à la politique

## Mesure de la conformité

L'équipe de management de la sécurité de l'information doit vérifier la conformité à cette politique par diverses méthodes, notamment, sans s'y limiter, les audits de configuration du fournisseur d'identité, les rapports de couverture MFA, la vérification de la vérification des fuites, l'analyse des journaux d'authentification, les tests d'intrusion, les audits internes et externes, ainsi que les retours d'information au propriétaire de la politique.

**Indicateurs clés de performance** :

| Indicateur | Objectif | Fréquence |
|-----------|---------|-----------|
| Enrôlement MFA (tous les utilisateurs) | ≥ 95 % | Mensuel |
| Enrôlement MFA (utilisateurs à privilèges) | 100 % | Mensuel |
| Conformité à la politique de mots de passe | ≥ 98 % | Mensuel |
| Résultats d'identifiants par défaut en production | 0 | Trimestriel |
| Couverture de vérification des fuites des mots de passe | 100 % des nouveaux mots de passe | Mensuel |
| Investigation des anomalies d'authentification (dans les 24 heures) | 100 % | En continu |
| Réduction du MFA par SMS (d'une année sur l'autre) | Tendance à la baisse | Annuellement |
| Adoption du gestionnaire de mots de passe (à l'échelle de l'organisation) | ≥ 80 % des utilisateurs avec un coffre-fort actif | Trimestriel |
| Ratio de mots de passe uniques dans le gestionnaire de mots de passe | ≥ 90 % de mots de passe uniques dans les coffres-forts | Trimestriel |
| Conformité à la rotation des identifiants des comptes de service | 100 % dans la période de rotation définie | Trimestriel |

Les indicateurs doivent être rapportés au RSSI trimestriellement. Les indicateurs ne atteignant pas l'objectif doivent inclure un plan de remédiation avec responsable et date cible.

## Exceptions

Toute exception à cette politique doit être approuvée et enregistrée à l'avance par le Responsable de la sécurité de l'information, avec une acceptation du risque documentée, des mesures compensatoires et une date de révision définie. Les exceptions doivent être rapportées à l'Équipe de révision de la direction. Durée maximale des exceptions : 12 mois, renouvelable avec une nouvelle approbation.

**Exceptions permises** (avec mesures compensatoires) :

- Systèmes legacy ne pouvant pas répondre aux exigences de longueur de mot de passe (mesure compensatoire : segmentation réseau, surveillance renforcée, accès restreint).
- Systèmes incompatibles avec le MFA (mesure compensatoire : restriction IP, journalisation renforcée, délai de session réduit, accès uniquement via VPN).
- Comptes de service nécessitant des politiques d'authentification différentes (mesure compensatoire : stockage des identifiants dans le coffre-fort, rotation automatisée, surveillance renforcée).

### Authentification des comptes de service

Les comptes de service (comptes non interactifs utilisés pour la communication application-à-application, les tâches planifiées et l'automatisation) doivent respecter les exigences suivantes :

| Exigence | Norme |
|----------|-------|
| **Convention de nommage** | Préfixe `svc-` suivi du nom de l'application/fonction (p. ex. `svc-backup-agent`, `svc-crm-integration`) |
| **Longueur du mot de passe** | Minimum 24 caractères, généré aléatoirement |
| **Stockage des identifiants** | Coffre-fort de secrets approuvé [PAM / Gestionnaire de mots de passe] — pas dans des scripts, fichiers de configuration ou code source |
| **Rotation** | Rotation automatisée tous les 90 jours lorsque techniquement réalisable ; rotation manuelle tous les 180 jours avec justification documentée |
| **Connexion interactive** | Interdite — les comptes de service ne doivent pas être utilisés pour la connexion interactive. Des contrôles techniques (GPO/politique IdP) doivent empêcher la connexion interactive lorsque cela est supporté. |
| **Responsabilité** | Propriétaire humain nommé (propriétaire du système ou responsable de l'application) en charge de la gestion du cycle de vie |
| **Révision** | Révision trimestrielle de tous les comptes de service : toujours nécessaire ? propriétaire toujours valide ? identifiants rotés ? permissions toujours appropriées ? |
| **Mise hors service** | Désactivé dans les 5 jours ouvrables suivant la mise hors service de l'application ; identifiants rotés immédiatement |

**Inventaire des comptes de service** : Maintenu dans [PAM / Système de gestion des actifs] avec : nom du compte, objet, propriétaire, date de création, date de dernière rotation, prochaine date de rotation, application associée, portée des permissions.

- Systèmes pour lesquels le SMS est la seule méthode MFA disponible (mesure compensatoire : restriction IP, surveillance des anomalies, plan de migration documenté).

**Non permis en tant qu'exceptions** :

- Élimination du MFA pour l'accès privilégié.
- Autorisation du partage de mots de passe sans responsabilité.
- Autorisation des identifiants par défaut dans les environnements de production.
- Désactivation de la journalisation d'authentification.

## Non-conformité

Un employé reconnu coupable d'avoir violé cette politique peut faire l'objet de mesures disciplinaires pouvant aller jusqu'au licenciement.

**Réponse progressive** (sur une période glissante de 12 mois) :

| Occurrence | Réponse | Délai | Responsable |
|------------|---------|-------|-------------|
| Première | Rappel de sensibilisation et formation ciblée | Dans les 5 jours ouvrables | Sécurité IT |
| Deuxième (dans les 90 jours) | Notification du responsable + avertissement documenté | Dans les 3 jours ouvrables | Sécurité IT + RH |
| Troisième (dans les 12 mois) | Restriction d'accès en attente de remédiation | Immédiat | Sécurité IT + Responsable |
| Violation délibérée / critique | Action disciplinaire conformément aux politiques RH | Escalade immédiate | RH + RSSI |

**Violations critiques** justifiant une escalade immédiate quelle que soit l'historique antérieur :

- Partage d'identifiants à privilèges.
- Contournement délibéré des contrôles d'authentification.
- Stockage d'identifiants en texte clair dans des emplacements partagés.
- Utilisation d'identifiants par défaut ou fournis par un fournisseur en production après notification.

## Amélioration continue

Cette politique est révisée et mise à jour dans le cadre du processus d'amélioration continue. Les révisions doivent prendre en compte les modifications des normes d'authentification (y compris les révisions de NIST SP 800-63B), les menaces émergentes (bourrage d'identifiants, phishing, techniques de contournement du MFA telles que les attaques adversaire-dans-le-milieu et les attaques par fatigue MFA), les avancées en matière d'authentification résistante au phishing (FIDO2/WebAuthn, clés d'accès), les changements réglementaires et les leçons tirées des incidents.

---

# Domaines de la norme ISO 27001 couverts

Politique relative aux informations d'authentification — Cartographie des contrôles ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership et engagement | 5.1 Politiques de sécurité de l'information |
| Clause 5.2 Politique | 5.4 Responsabilités de la direction |
| Clause 6.2 Objectifs de sécurité de l'information | **5.17 Informations d'authentification** |
| Clause 7.3 Sensibilisation | 5.15 Contrôle d'accès |
| Clause 7.5.3 Contrôle des informations documentées | 5.16 Gestion des identités |
| | 5.18 Droits d'accès |
| | 5.36 Conformité aux politiques, règles et normes |
| | 6.3 Sensibilisation, éducation et formation à la sécurité de l'information |
| | 6.4 Processus disciplinaire |
| | 8.2 Droits d'accès privilégiés |
| | 8.5 Authentification sécurisée |
| | 8.24 Utilisation de la cryptographie |

**Cadre réglementaire et légal** :

| Cadre | Pertinence |
|-------|-----------|
| nLPD suisse (revDSG) | Art. 8 — Mesures techniques et organisationnelles incluant les contrôles d'authentification pour la protection des données |
| DSV suisse (Ordonnance sur la protection des données) | Art. 1–3 — Exigences minimales en matière de sécurité des données |
| RGPD de l'UE (le cas échéant) | Art. 32 — Sécurité du traitement (contrôles d'authentification comme mesure technique appropriée) |
| ISO/IEC 27001:2022 | Contrôle Annexe A 5.17 — Informations d'authentification |
| ISO/IEC 27002:2022 | Section 5.17 — Guide de mise en œuvre pour les informations d'authentification |
| NIST SP 800-63B-4 | Lignes directrices sur l'identité numérique — secrets mémorisés, authentification multifacteur, exigences des vérificateurs |
| CIS Controls v8 | Contrôle 5 (Gestion des comptes), Contrôle 6 (Gestion du contrôle d'accès) |

---

<!-- QA_VERIFIED: 2026-03-29 -->
