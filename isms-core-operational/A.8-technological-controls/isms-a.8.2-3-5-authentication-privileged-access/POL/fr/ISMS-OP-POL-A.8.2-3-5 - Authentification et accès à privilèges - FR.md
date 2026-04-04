<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.8.2-3-5-FR:operational:OP-POL:a.8.2-3-5 -->
**ISMS-OP-POL-A.8.2-3-5 — Authentification et accès à privilèges**

---

**Contrôle documentaire**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Authentification et accès à privilèges |
| **Type de document** | Politique opérationnelle |
| **Identifiant du document** | ISMS-OP-POL-A.8.2-3-5 |
| **Créateur du document** | Responsable de la sécurité de l'information (RSSI) |
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

**Documents associés** :

- ISO/IEC 27001:2022 Contrôles A.8.2, A.8.3, A.8.5 — Droits d'accès à privilèges, restriction de l'accès à l'information, authentification sécurisée

**Contrôles Annexe A associés** :

| Contrôle | Relation avec l'authentification et les accès à privilèges |
|----------|-------------------------------------------------------------|
| A.5.3 Séparation des tâches | La séparation des tâches est appliquée via des restrictions d'accès et des niveaux de privilèges hiérarchisés |
| A.5.15-18 Contrôle d'accès et gestion des identités | Le cycle de vie des identités alimente l'authentification ; les droits d'accès définissent les restrictions |
| A.5.17 Informations d'authentification | Gestion des identifiants pour les mots de passe, jetons et secrets |
| A.5.24-28 Gestion des incidents | La compromission des identifiants déclenche la réponse aux incidents |
| A.8.1 Appareils des utilisateurs finaux | La sécurité des points de terminaison soutient l'authentification (confiance de l'appareil, chiffrement) |
| A.8.9 Gestion de la configuration | Les configurations système appliquent les configurations de base d'authentification et d'accès |
| A.8.15 Journalisation | Les événements d'authentification et les actions à privilèges alimentent la journalisation centralisée |
| A.8.16 Activités de surveillance | Surveillance en temps réel des échecs d'authentification et des accès à privilèges |
| A.8.20-22 Sécurité des réseaux | La segmentation réseau soutient l'application des zones d'accès |
| A.8.24 Utilisation de la cryptographie | Protection cryptographique des identifiants, jetons et sessions |

**Politiques internes associées** :

- Politique de gestion des identités et des accès
- Politique de sécurité des points de terminaison
- Politique de sécurité des réseaux
- Politique d'utilisation de la cryptographie
- Politique de journalisation
- Politique de surveillance (A.8.16)
- Politique de gestion des incidents

---

# Politique d'authentification et d'accès à privilèges

## Objet

L'objet de cette politique est de garantir que les mécanismes d'authentification sont mis en œuvre en adéquation avec la sensibilité des informations et des systèmes auxquels on accède, que les droits d'accès à privilèges sont restreints et gérés selon le principe du moindre privilège, et que les contrôles d'accès techniques appliquent les limites d'accès autorisées.

Cette politique soutient la nLPD suisse (revDSG) et l'Ordonnance sur la protection des données (OPDo) en mettant en œuvre des mesures techniques et organisationnelles proportionnées au risque pour protéger les données personnelles (y compris les données personnelles sensibles) par des contrôles d'authentification et d'accès. Lorsque l'organisation traite des données de personnes dans l'UE/EEE, les exigences du RGPD s'appliquent également. L'authentification forte et la gestion des accès à privilèges sont des mesures techniques clés pour démontrer la conformité aux obligations de protection des données dans les deux cadres.

## Champ d'application

Tous les employés et utilisateurs tiers.

Tous les mécanismes d'authentification, comptes à privilèges et contrôles d'accès techniques sur les systèmes, plateformes et environnements appartenant à l'organisation ou exploités par elle et considérés dans le périmètre de la déclaration de périmètre ISO 27001.

Cela inclut les environnements sur site, cloud, hybrides et SaaS.

## Principe

Les contrôles d'authentification et d'accès sont mis en œuvre selon le principe de la défense en profondeur. Les utilisateurs sont positivement identifiés et authentifiés avant d'obtenir l'accès. L'accès à privilèges n'est accordé qu'avec une approbation documentée et limité au minimum requis pour la tâche. L'accès est refusé par défaut et accordé uniquement sur autorisation explicite.

Toutes les décisions d'authentification et d'accès doivent être basées sur les risques, en tenant compte de la classification des informations et de la criticité du système.

---

## Infrastructure de gestion des identités et des accès

Le tableau suivant documente la pile technologique GIA de l'organisation. Le choix réel des outils est propre à l'organisation ; des exemples sont fournis à titre indicatif :

| Fonction | Solution | Responsable | Utilisation principale |
|----------|----------|-------------|------------------------|
| **Fournisseur d'identité (FI)** | [p. ex., Azure Active Directory (Entra ID), Okta, Google Workspace, JumpCloud] | Exploitation informatique | Authentification centralisée, SSO, gestion du cycle de vie des utilisateurs |
| **Gestion des accès à privilèges (GAP)** | [p. ex., CyberArk, Delinea (Thycotic), BeyondTrust, Azure AD PIM] | Sécurité informatique | Coffre-fort de mots de passe, enregistrement de session, accès JIT, rotation des identifiants |
| **Authentification multifacteur (AMF)** | [p. ex., Azure MFA, Okta Verify, Duo Security, YubiKey (FIDO2)] | Exploitation informatique | Second facteur d'authentification pour tous les utilisateurs |
| **Gestionnaire de mots de passe d'entreprise** | [p. ex., 1Password Business, Bitwarden Teams, LastPass Enterprise] | Sécurité informatique | Stockage sécurisé des identifiants partagés ; solution intermédiaire avant GAP pour les comptes de service |
| **Authentification unique (SSO)** | [Intégré au FI via SAML 2.0 / OIDC] | Exploitation informatique | Authentification des applications via le FI centralisé |
| **Enregistrement de session** | [p. ex., natif GAP, CyberArk PSM, Teleport, Windows Defender for Identity] | Sécurité informatique | Enregistrement et audit des sessions à privilèges de Niveau 0 |
| **Contrôle des identifiants compromis** | [p. ex., Azure AD Password Protection, API Have I Been Pwned, Enzoic] | Sécurité informatique | Prévenir l'utilisation de mots de passe connus comme compromis |
| **Gouvernance des identités** | [p. ex., Azure AD Access Reviews, SailPoint, Saviynt ou processus manuel sur tableur] | Sécurité informatique | Campagnes de certification des accès, rapport de conformité |

**Points d'intégration** : le FI doit s'intégrer au système RH pour l'automatisation des arrivées/mobilités/départs. La GAP, le FI et le SIEM doivent être intégrés pour une surveillance centralisée. L'AMF doit être appliquée via les politiques d'accès conditionnel du FI. Les journaux d'enregistrement de session doivent être transmis au SIEM.

---

## Exigences d'authentification

### Normes de mots de passe

L'accès aux systèmes et aux informations est authentifié par des mots de passe ou des mécanismes plus forts. L'organisation doit appliquer les normes de mots de passe suivantes, alignées sur NIST SP 800-63B :

| Exigence | Norme |
|----------|-------|
| Longueur minimale | 12 caractères (14 pour les comptes à privilèges) |
| Complexité | Longueur plutôt que complexité ; pas de règles de composition obligatoires |
| Longueur maximale | Les systèmes doivent accepter au moins 64 caractères |
| Prise en charge des caractères | Tous les caractères ASCII imprimables (y compris l'espace) et Unicode doivent être acceptés |
| Contrôle | Les mots de passe doivent être validés par rapport aux bases de données d'identifiants connus compromis lors de la définition/modification et mensuellement par la suite |
| Rotation | Basée sur des événements uniquement — en cas de compromission suspectée ou confirmée ; la rotation périodique forcée n'est pas requise |
| Mots de passe initiaux | Doivent être changés à la première utilisation |
| Mots de passe par défaut | Les mots de passe fournis par le fournisseur et par défaut doivent être changés immédiatement lors de l'installation |
| Partage | Les mots de passe ne doivent pas être génériques, partagés ou définis au niveau d'un groupe |
| Confidentialité | Les mots de passe doivent être gardés confidentiels et ne pas être écrits |
| Affichage | Les mots de passe ne doivent pas être affichés lors de la saisie |
| Code | Les mots de passe ne doivent pas être codés en dur ou inclus dans des scripts, du code ou des macros |
| Transmission | Les mots de passe doivent être chiffrés lors de leur transmission sur les réseaux |
| Stockage | Les mots de passe doivent être stockés à l'aide de fonctions de hachage cryptographiques approuvées (bcrypt, scrypt, Argon2 ou PBKDF2) et jamais en texte en clair ou avec chiffrement réversible |
| Verrouillage | Les systèmes doivent verrouiller les utilisateurs après 6 tentatives d'accès échouées |
| Historique | Un historique d'au moins 24 mots de passe précédents doit être maintenu pour prévenir la réutilisation |
| Gestionnaires de mots de passe | L'utilisation de gestionnaires de mots de passe approuvés par l'organisation est recommandée |

**Options de mise en œuvre du contrôle des identifiants compromis** :

| Option | Mise en œuvre | Remarques |
|--------|--------------|-----------|
| **Azure AD Password Protection** | Activer la liste de mots de passe interdits globale + liste personnalisée ; appliquer dans le cloud et sur site (via agents DC) | Recommandé pour les environnements Microsoft |
| **API Have I Been Pwned (HIBP)** | Modèle k-anonymat (seuls les 5 premiers caractères du hachage sont envoyés) ; contrôle lors de la définition/modification du mot de passe et analyse mensuelle | Open-source ; nécessite un effort d'intégration |
| **Solution tierce** | Enzoic, Specops Password Policy ou équivalent | Commercial ; inclut généralement une application supplémentaire de la politique de mots de passe |

Les mots de passe trouvés dans des bases de données de violations doivent être rejetés lors de la définition/modification et un changement forcé imposé s'ils sont détectés lors des analyses mensuelles. Métrique de couverture du contrôle : pourcentage d'événements de définition/modification de mots de passe validés par rapport aux bases de données de violations (cible : 100 %).

### Authentification multifacteur (AMF)

L'authentification multifacteur doit être requise pour :

- Tous les comptes à privilèges et d'administrateur.
- Tout accès à distance aux réseaux et services cloud de l'organisation.
- Toutes les applications exposées sur Internet avec authentification.
- Tout accès aux systèmes traitant des données confidentielles ou personnelles.
- Toutes les consoles d'administration de plateformes cloud.

**Méthodes AMF acceptables** (par ordre de préférence) :

| Méthode | Résistance à l'hameçonnage | Utilisation recommandée |
|---------|--------------------------|------------------------|
| Clés de sécurité matérielles (FIDO2/WebAuthn) | Élevée | Requis pour le Niveau 0 ; recommandé pour tous les comptes à privilèges |
| Applications d'authentification (TOTP) | Moyenne | Acceptable pour les Niveaux 1/2 et utilisateurs standard |
| Notifications push (avec correspondance de numéro) | Moyenne | Acceptable lorsque la correspondance de numéro est activée |
| OTP par SMS/Voix | Faible | Uniquement lorsque d'autres méthodes ne sont pas techniquement faisables (systèmes anciens) |

L'OTP par SMS devrait être progressivement abandonné dans la mesure du possible en raison des vulnérabilités connues (échange de carte SIM, interception). Les systèmes reposant uniquement sur l'AMF par SMS doivent être documentés dans le registre des risques avec un plan de migration.

**Objectifs de couverture AMF** :

- Utilisateurs à privilèges : enrôlement AMF à 100 %.
- Tous les utilisateurs : enrôlement AMF à 95 %+ dans les 12 mois suivant l'adoption de la politique.
- Accès à distance : application AMF à 100 %.

Les systèmes ne pouvant pas prendre en charge l'AMF doivent être documentés dans le registre des risques avec justification technique, contrôles compensatoires (p. ex., segmentation réseau, surveillance renforcée, restriction IP) et acceptation des risques approuvée par le RSSI révisée annuellement.

### Authentification unique (SSO)

L'organisation doit mettre en œuvre une SSO centralisée via le fournisseur d'identité en utilisant SAML 2.0 ou OIDC avec les objectifs suivants :

- Nouvelles applications SaaS : intégration SSO requise avant l'approbation des achats.
- Applications existantes : intégration SSO priorisée en fonction du niveau de risque ci-dessous.
- Objectif : intégration de 80 %+ des applications SaaS dans les 12 mois ; 90 %+ dans les 24 mois.

**Niveaux de priorité d'intégration SSO** :

| Priorité | Critères | Délai |
|----------|----------|-------|
| **Priorité 1** | Traite des données confidentielles ; > 50 utilisateurs ; exposé sur Internet ; consoles d'infrastructure cloud | 30 jours |
| **Priorité 2** | Traite des données internes ; 20-50 utilisateurs ; applications d'accès à privilèges | 90 jours |
| **Priorité 3** | < 20 utilisateurs ; exposition aux données limitée ; utilisation peu fréquente | 180 jours |
| **Priorité 4** | Applications anciennes avec limitations SSO ; applications programmées pour mise hors service ; fournisseurs ne prenant pas en charge SSO | 12 mois (ou exception documentée) |

Un inventaire des intégrations SSO doit être maintenu, répertoriant chaque application, son statut SSO (intégré / en cours / exception), le niveau de priorité et la date cible. L'inventaire doit être révisé trimestriellement.

Les applications sans capacité SSO nécessitent une exception documentée avec des contrôles compensatoires (p. ex., AMF individuelle, surveillance renforcée, application du gestionnaire de mots de passe).

### Journalisation de l'authentification

Tous les événements d'authentification doivent être journalisés et transmis au SIEM de journalisation centralisée :

- Tentatives d'authentification réussies et échouées.
- Enrôlement AMF et modifications de méthode.
- Modifications et réinitialisations de mots de passe.
- Verrouillages et déverrouillages de comptes.
- Création et fin de session.

Les journaux d'authentification doivent être conservés pendant un minimum de 12 mois.

**Règles d'alerte de surveillance de l'authentification** :

| Règle d'alerte | Seuil | Gravité | ANS de réponse |
|---------------|-------|---------|----------------|
| Attaque par force brute | ≥ 10 connexions échouées depuis une même IP en 5 minutes | Élevée | 1 heure |
| Bourrage d'identifiants | ≥ 5 connexions échouées sur plusieurs comptes depuis une même IP en 10 minutes | Élevée | 1 heure |
| Voyage impossible | Connexion réussie depuis des emplacements distants de > 500 km en 1 heure | Élevée | 1 heure |
| Compte à privilèges — nouvel appareil | Connexion Niveau 0/1 depuis un appareil non vu depuis 30 jours | Moyenne | 4 heures |
| Compte à privilèges — emplacement inattendu | Connexion Niveau 0/1 depuis un pays hors de la liste approuvée | Critique | Immédiate |
| Connexion interactive d'un compte de service | Compte de service utilisé pour une connexion RDP/SSH/console | Élevée | 2 heures |
| Tentative de contournement AMF | Authentification sans AMF requise | Élevée | 1 heure |
| Utilisation du compte d'urgence | Authentification du compte d'urgence/brise-glace | Critique | Immédiate ; révision dans les 24 heures |
| Pic de verrouillage de comptes | ≥ 10 verrouillages dans l'ensemble du parc en 1 heure | Moyenne | Investigation le jour ouvrable même |

**Emplacements géographiques approuvés** : Suisse, [pays supplémentaires selon les opérations de l'activité]. Les connexions depuis des pays non approuvés doivent déclencher des alertes conformément au tableau ci-dessus.

Les règles d'alerte doivent être révisées et ajustées trimestriellement pour réduire les taux de faux positifs. Processus d'investigation : recevoir l'alerte → valider (vrai/faux positif) → enrichir avec le contexte → escalader si confirmé → documenter le résultat.

### Exigences des systèmes d'authentification

Le principal système d'authentification d'accès doit :

- Ne pas afficher les identifiants du système ou de l'application avant que le processus de connexion ne soit mené à bien.
- Afficher un avertissement général indiquant que le système ne doit être accédé que par des utilisateurs autorisés.
- Ne pas fournir de messages d'aide pendant la procédure de connexion qui aideraient un utilisateur non autorisé.
- Valider les informations de connexion uniquement à la fin de la saisie complète des données. En cas d'erreur, le système ne doit pas indiquer quelle partie des données est correcte ou incorrecte.
- Se protéger contre les tentatives de connexion par force brute.
- Journaliser les tentatives réussies et échouées.
- Déclencher un événement de sécurité si une tentative potentielle ou une réussite de violation des contrôles de connexion est détectée.
- Ne pas afficher un mot de passe lors de sa saisie.
- Ne pas transmettre les mots de passe en texte clair sur un réseau.
- Mettre fin aux sessions inactives après une période d'inactivité définie.
- Restreindre les durées de connexion pour assurer une sécurité supplémentaire pour les applications à haut risque.

---

## Gestion des accès à privilèges

### Principes d'accès à privilèges

L'accès à privilèges doit être restreint en fonction de :

- **Moindre privilège** : accès minimum requis pour accomplir les fonctions professionnelles.
- **Besoin d'en connaître** : accès uniquement aux informations requises pour des tâches spécifiques.
- **Séparation des tâches** : les fonctions critiques réparties entre plusieurs individus.
- **Accès limité dans le temps** : provisionnement juste-à-temps (JIT) lorsque c'est possible.

### Classification des comptes à privilèges — Modèle de niveaux d'administration

L'organisation doit mettre en œuvre une administration hiérarchisée pour limiter l'impact des identifiants compromis :

| Niveau | Périmètre | Exemples | Exigences |
|--------|-----------|----------|-----------|
| **Niveau 0** | Domaine/Entreprise | Administrateurs de domaine, administrateur global Azure/M365, PKI, SIEM | AMF matérielle (FIDO2) ; poste d'administration dédié ; enregistrement de session obligatoire |
| **Niveau 1** | Serveur/Application | Administrateurs de serveurs, DBA, administrateurs d'abonnements cloud | AMF requise ; poste d'administration dédié recommandé |
| **Niveau 2** | Poste de travail/Terminal | Support informatique de bureau, service d'assistance avec admin local | AMF requise ; poste de travail standard acceptable |

**Exigences d'isolation des niveaux** :

- Les comptes de Niveau 0 ne doivent jamais s'authentifier sur les systèmes de Niveau 1 ou Niveau 2.
- Les comptes de Niveau 1 ne doivent jamais s'authentifier sur les systèmes de Niveau 2.
- Des identifiants séparés doivent être utilisés par niveau (p. ex., j.dupont.n0, j.dupont.n1).
- Les activités quotidiennes (messagerie, navigation web) ne doivent pas être effectuées sur les postes d'administration dédiés.

**Application de l'isolation des niveaux** :

Les contrôles techniques doivent appliquer les frontières entre les niveaux. Les options de mise en œuvre suivantes sont disponibles selon la plateforme d'identité de l'organisation :

*Accès conditionnel (Azure AD / Entra ID ou équivalent) :*

| Politique | Cible | Application |
|-----------|-------|-------------|
| Exiger une AMF résistante à l'hameçonnage pour le Niveau 0 | Comptes Niveau 0, toutes les applications cloud | FIDO2/WebAuthn uniquement ; bloquer les autres méthodes AMF |
| Bloquer le Niveau 0 des applications non-admin | Comptes Niveau 0 | Bloquer l'accès à Office 365, SharePoint, OneDrive, Teams |
| Exiger un appareil conforme pour l'accès admin | Comptes Niveau 0/1 | Exiger un appareil conforme ou joint hybride |
| Bloquer l'authentification héritée | Tous les utilisateurs | Bloquer IMAP, POP3, SMTP AUTH |
| Bloquer l'accès depuis des pays non approuvés | Tous les utilisateurs (exclure les comptes d'urgence) | Autoriser : CH + pays approuvés ; bloquer tous les autres |
| Exiger l'AMF pour tous les utilisateurs | Tous les utilisateurs, toutes les applications cloud | Fréquence de connexion : 90 jours |
| Bloquer les connexions à haut risque | Tous les utilisateurs (nécessite Azure AD P2) | Bloquer les connexions signalées comme à haut risque par Identity Protection |
| Délai d'expiration de session pour les applications sensibles | Finance, RH, bases de données clients | Ré-authentification toutes les 4 heures |

*Application sur site :*

- Restrictions d'ouverture de session GPO : interdire aux comptes de Niveau 0 de se connecter localement aux systèmes Niveau 1/2 ; interdire aux comptes Niveau 1 sur les postes de travail Niveau 2.
- Segmentation réseau : postes d'administration Niveau 0 sur VLAN dédié ; Niveau 1 sur VLAN séparé ; utilisateurs standard sur VLAN d'entreprise. Les règles de pare-feu restreignent l'accès inter-niveaux.

*Règles d'alerte SIEM pour les violations de niveaux :*

| Alerte | Gravité | Notification |
|--------|---------|-------------|
| Authentification Niveau 0 sur un système Niveau 1/2 | Critique | RSSI immédiatement |
| Authentification Niveau 1 sur un système Niveau 2 | Élevée | Responsable de la sécurité informatique |
| Compte à privilèges depuis un emplacement non approuvé | Élevée | Équipe de sécurité informatique |

**Postes d'administration sécurisés (PAW)** :

| Niveau | Exigence PAW |
|--------|-------------|
| **Niveau 0** | PAW obligatoire |
| **Niveau 1** | PAW recommandé ; obligatoire en Phase 2 |
| **Niveau 2** | Poste de travail standard acceptable |

*Configuration de base PAW (Niveau 0/1) :*

- **Matériel** : appareil physique dédié ; chiffrement intégral du disque ; TPM 2.0 ; Démarrage sécurisé activé.
- **Système d'exploitation** : durci selon le Référentiel CIS Niveau 2 ; mises à jour automatiques ; pas de logiciels installés par l'utilisateur (liste d'autorisation des applications appliquée).
- **Réseau** : VLAN d'administration dédié ; règles de pare-feu limitant les connexions aux seules cibles de gestion ; pas de navigation Internet générale.
- **Applications** : client RDP/SSH, client GAP et outils d'administration uniquement. La messagerie, le navigateur web, la suite bureautique et les outils de collaboration (Teams/Slack) sont interdits.
- **Contrôle d'accès** : administrateur local désactivé ; identifiants GAP requis ; AMF appliquée ; verrouillage de l'écran après 10 minutes.
- **Surveillance** : agent EDR installé ; toute l'activité transmise au SIEM ; alertes pour les logiciels non autorisés, connexions ou tentatives de navigation.

**Déploiement par phases** : Phase 1 (Année 1) : PAW Niveau 0 déployés. Phase 2 (Année 2) : PAW Niveau 1 déployés. Des contrôles compensatoires doivent être documentés pour toute période où les PAW ne sont pas encore en place (p. ex., surveillance renforcée, VM dédiées, comptes admin restreints sur les postes de travail standard).

**Suivi de l'état de déploiement** : La phase actuelle de déploiement (planification, pilote, application partielle, application complète) doit être documentée pour chaque niveau, avec des contrôles compensatoires pour les niveaux non encore appliqués et des dates d'achèvement cibles.

### Gestion des comptes à privilèges

Tous les comptes à privilèges doivent être :

- Non partagés ni génériques (un utilisateur, un compte à privilèges par niveau).
- Clairement identifiables (convention de nommage documentée et appliquée).
- Journalisés et surveillés pour détecter toute activité anormale.
- Limités dans le temps dans la mesure du possible (accès JIT préféré aux privilèges permanents).
- Enregistrés dans un inventaire des comptes à privilèges maintenu avec propriétaire, niveau, objectif et date de révision.

### Solution de gestion des accès à privilèges (GAP)

L'organisation doit mettre en œuvre des contrôles d'accès à privilèges, pouvant inclure une solution GAP dédiée (voir tableau de l'infrastructure GIA) ou des contrôles manuels équivalents :

| Capacité | Exigence | Approche progressive pour les PME |
|----------|----------|----------------------------------|
| **Coffre-fort de mots de passe** | Mots de passe à privilèges stockés dans un coffre-fort approuvé, pas en texte clair | Phase 1 : mettre en œuvre pour les comptes Niveau 0 ; étendre aux Niveaux 1/2 |
| **Enregistrement de session** | Sessions Niveau 0 enregistrées ; enregistrement Niveau 1 recommandé | Phase 1 : Niveau 0 obligatoire ; Niveau 1 au fur et à mesure de l'extension de la GAP |
| **Accès juste-à-temps** | Élévation temporaire des privilèges avec révocation automatique | Phase 2 : mettre en œuvre là où la GAP prend en charge les processus JIT |
| **Rotation des identifiants** | Mots de passe des comptes de service rotés selon le calendrier ci-dessous | Phase 1 : rotation manuelle avec preuves documentées |

Lorsqu'une solution GAP dédiée n'est pas encore déployée, des contrôles compensatoires doivent être documentés (p. ex., rotation manuelle des identifiants, gestionnaire de mots de passe partagé avec piste d'audit, journalisation alternative des sessions via SIEM).

**Exigences de rotation des identifiants** :

| Type de compte | Fréquence de rotation |
|---------------|-----------------------|
| Comptes de service (Niveau 0) | Maximum 90 jours |
| Comptes de service (Niveaux 1/2) | Maximum 180 jours |
| Comptes d'urgence | Après chaque utilisation + maximum 365 jours |
| Comptes admin partagés (déconseillés) | 90 jours ; migrer vers des comptes individuels avec exception RSSI |

Tous les identifiants doivent être rotés immédiatement en cas de compromission suspectée ou confirmée, indépendamment du calendrier.

### Gestion des comptes de service

Les comptes de service doivent être gérés selon un cycle de vie défini :

1. **Demande et approbation** : le demandeur soumet une demande via le système de ticketing. Le Responsable de la sécurité informatique approuve dans les 3 jours ouvrables. Critères d'approbation : justification commerciale documentée, permissions minimales définies, propriétaire désigné, niveau désigné.
2. **Création** : convention de nommage `svc-[système]-[objectif]` (p. ex., `svc-erp-sauvegarde`). Mot de passe aléatoire d'au moins 20 caractères. Identifiants transmis de manière sécurisée via le coffre-fort GAP ou équivalent (jamais par e-mail ou messagerie).
3. **Inventaire** : tous les comptes de service enregistrés avec : nom du compte, objectif, propriétaire, niveau, permissions, emplacement des identifiants (référence coffre-fort), date de dernière rotation, date de prochaine rotation.
4. **Révision des accès** : attestation trimestrielle par les propriétaires d'applications. Les comptes inutilisés (aucune authentification depuis 90 jours) sont désactivés immédiatement et supprimés après 90 jours de conservation.
5. **Rotation des identifiants** : automatisée via GAP lorsque c'est possible ; rotation manuelle documentée dans l'inventaire lorsque GAP n'est pas disponible.
6. **Mise hors service** : lorsque le service est retiré, le compte de service est désactivé immédiatement, les identifiants rotés et le compte supprimé après 90 jours de conservation.

**Surveillance des comptes de service** : des règles d'alerte SIEM doivent détecter les connexions interactives par des comptes de service, les authentifications depuis des emplacements inattendus et les tentatives d'authentification échouées. Une analyse de découverte trimestrielle doit identifier les comptes de service non documentés.

### Accès à privilèges juste-à-temps (JIT)

L'accès JIT est préféré aux privilèges permanents. Le processus suivant s'applique selon les outils disponibles :

**JIT basé sur GAP** (préféré) :

1. L'utilisateur demande une élévation de privilèges via le portail GAP avec justification.
2. Approbation : automatique pour les tâches pré-approuvées ; approbation du responsable/de la sécurité informatique pour les autres.
3. La GAP émet des identifiants à durée limitée (par défaut : 4 heures ; maximum : 8 heures).
4. Session enregistrée (Niveau 0 obligatoire ; Niveau 1 recommandé).
5. Privilèges automatiquement révoqués à expiration.
6. Toutes les sessions JIT journalisées dans la piste d'audit GAP.

**Azure AD PIM** (pour les rôles cloud) :

1. Rôle éligible assigné (pas actif).
2. L'utilisateur active le rôle avec justification et AMF.
3. Approbation requise pour l'administrateur global et autres rôles Niveau 0.
4. Activation à durée limitée (par défaut : 4 heures ; maximum : 8 heures).
5. Désactivation automatique à expiration.
6. Toutes les activations journalisées dans le journal d'audit Azure AD.

**JIT manuel** (intermédiaire là où GAP/PIM n'est pas déployé) :

1. L'utilisateur demande l'accès via le système de ticketing avec justification.
2. La sécurité informatique approuve et ajoute l'appartenance au groupe temporaire.
3. Rappel de calendrier défini pour l'heure de révocation.
4. L'exploitation informatique révoque manuellement l'accès à expiration.
5. Ticket clôturé avec confirmation de révocation.

**Objectifs JIT** : Année 1 : 50 % de l'accès Niveau 1 via JIT. Année 2 : 80 % de l'accès Niveau 1 via JIT. Niveau 0 : accès permanent pour les rôles d'astreinte ; JIT pour tous les autres.

### Révisions des accès à privilèges

| Type de compte | Fréquence de révision |
|---------------|-----------------------|
| Comptes à privilèges Niveau 0 | Trimestriellement (révisions par le RSSI ou le Responsable de la sécurité informatique) |
| Comptes à privilèges Niveaux 1/2 | Trimestriellement (révisions par les propriétaires de systèmes) |
| Comptes de service | Trimestriellement (les propriétaires de systèmes vérifient le besoin continu) |

**Processus de révision** :

- Campagnes de révision des accès initiées via l'outil de gouvernance des identités ou un processus manuel.
- Réviseurs : responsables directs pour les Niveaux 1/2 ; RSSI ou Responsable de la sécurité informatique pour le Niveau 0.
- Période de révision : 10 jours ouvrables pour compléter.
- Absence de réponse : rappel au jour 5 ; escalade au responsable du réviseur au jour 8 ; accès suspendu au jour 15 en l'absence de réponse.
- Les demandes de révocation traitées dans les 48 heures.

### Processus de campagne de certification des accès

Les révisions d'accès trimestrielles doivent suivre une campagne structurée :

**Semaine 1 — Préparation de la campagne** :
- Générer le rapport des comptes à privilèges, le rapport des comptes de service et le rapport des appartenances aux groupes depuis le fournisseur d'identité et la GAP.
- Distribuer aux réviseurs : comptes Niveau 0 au RSSI ; comptes Niveaux 1/2 aux propriétaires de systèmes ; comptes de service aux propriétaires d'applications.

**Semaines 2-3 — Période de révision (10 jours ouvrables)** :
- Les réviseurs attestent chaque compte : Approuver / Révoquer / Transférer / Impossible à déterminer.
- Rappels : Jour 5 (automatisé), Jour 8 (escalade au responsable du réviseur), Jour 10 (avertissement final — absence de réponse traitée comme refus implicite, accès suspendu).

**Semaine 4 — Remédiation** :
- L'exploitation informatique traite les révocations dans les 48 heures.
- Rapport récapitulatif généré avec les actions prises.

**Post-campagne** : résultats présentés au RSSI lors de la prochaine révision trimestrielle. Les enregistrements de certification conservés pendant 3 ans.

**Métriques de campagne** : taux d'achèvement des révisions (cible : 100 %) ; délai moyen de révision (cible : ≤ 5 jours ouvrables) ; taux de révocation (plage saine : 5-15 % ; les taux en dehors de cette plage justifient une investigation).

### Accès d'urgence / brise-glace

L'organisation doit maintenir des procédures d'accès d'urgence pour les situations où les canaux d'authentification normaux ne sont pas disponibles :

- Comptes d'urgence sécurisés avec identifiants scellés (coffre-fort physique ou enveloppe scellée de la solution GAP).
- Autorisation multi-personnes requise pour l'utilisation des comptes d'urgence (double contrôle — deux individus requis pour accéder aux identifiants).
- Toute utilisation des comptes d'urgence journalisée, alertée et révisée dans les 24 heures.
- Identifiants rotés immédiatement après utilisation.
- Comptes d'urgence testés semestriellement (p. ex., janvier et juillet) pour confirmer que les identifiants fonctionnent et que les procédures sont à jour.
- Les enregistrements de test doivent documenter la date, le testeur, la confirmation d'authentification réussie et la rotation des identifiants post-test.

---

## Restriction des accès

### Principes d'application

L'accès aux informations et autres actifs associés doit être restreint conformément à cette politique et à la Politique de gestion des identités et des accès :

- **Refus par défaut** : accès refusé par défaut ; autorisation explicite requise.
- **Contrôle d'accès basé sur les rôles (RBAC)** : accès basé sur des rôles professionnels documentés.
- **Contrôle d'accès basé sur les attributs (ABAC)** : accès contextuel (emplacement, conformité de l'appareil, score de risque) lorsque pris en charge par le fournisseur d'identité.
- **Alignement sur la classification des données** : les restrictions d'accès correspondent au niveau de classification des informations.

### Contrôles d'accès techniques

**Accès au système d'exploitation** :

- Permissions du système de fichiers appliquées selon la classification des données.
- Commandes à privilèges limitées aux administrateurs autorisés.
- Droits d'administrateur local supprimés des utilisateurs standard (élévation de privilèges gérée pour les exceptions).

**Accès aux bases de données** :

- Accès direct aux bases de données limité aux DBA autorisés.
- Accès applicatif via des comptes de service avec des privilèges minimaux.
- Colonnes sensibles chiffrées ou masquées pour l'accès non privilégié.

**Accès aux applications** :

- Contrôle d'accès basé sur les rôles dans les applications.
- Les fonctions sensibles nécessitent une authentification supplémentaire (AMF renforcée) lorsque c'est possible.

**Accès aux API** :

- Authentification API requise (OAuth 2.0 ou clés d'API avec rotation selon le calendrier de rotation des identifiants).
- Limitation du débit appliquée sur toutes les API.
- Les API sensibles nécessitent une autorisation supplémentaire.

**Accès aux ressources cloud** :

- Les politiques IAM cloud suivent le principe du moindre privilège.
- L'accès inter-comptes est restreint, journalisé et révisé trimestriellement.
- Les permissions au niveau des ressources sont appliquées.

### Délais d'expiration de session

Les sessions système doivent appliquer les délais d'expiration suivants :

| Classification | Délai d'inactivité | Délai absolu |
|---------------|-------------------|--------------|
| Systèmes confidentiels / critiques | 15 minutes | 8 heures |
| Systèmes traitant des données personnelles sensibles | 5 minutes | 4 heures |
| Consoles d'administration à privilèges | 10 minutes | 4 heures |
| Systèmes métier standard | 30 minutes | 12 heures |

Le délai absolu nécessite une ré-authentification quelle que soit l'activité.

### Restrictions d'accès basées sur le réseau

- La segmentation réseau doit séparer les zones de confiance pour soutenir la restriction des accès (détaillée dans la Politique de sécurité des réseaux).
- Les règles de pare-feu doivent appliquer les frontières d'accès entre les segments réseau.
- Le contrôle d'accès réseau (NAC) ou équivalent doit vérifier la conformité des points de terminaison avant d'accorder l'accès dans la mesure du possible.

### Masquage des données

L'organisation masque les données conformément aux obligations légales et réglementaires, notamment la nLPD suisse et les exigences du RGPD le cas échéant. Le masquage des données doit être appliqué à :

- Les données personnelles affichées dans des environnements non-production.
- Les champs de données sensibles visibles par les utilisateurs sans besoin légitime d'accès complet.
- Les données présentées dans des rapports, tableaux de bord ou journaux où les valeurs complètes ne sont pas nécessaires.

### Vérification des contrôles d'accès

L'organisation doit vérifier les contrôles d'accès par :

- Des tests d'intrusion annuels incluant des tentatives de contournement des contrôles d'accès.
- Des audits trimestriels des permissions pour les systèmes critiques et les comptes à privilèges.
- Une analyse automatisée de la conformité pour détecter la dérive de configuration dans la mesure du possible.

---

## Rôles et responsabilités

| Rôle | Responsabilités |
|------|----------------|
| **Direction générale** | Approuver la politique ; allouer le budget pour l'infrastructure d'authentification, le déploiement AMF et la GAP ; réviser les métriques de sécurité trimestriellement |
| **RSSI** | Responsabilité globale de la sécurité de l'authentification et des accès ; approuver la stratégie GAP et le modèle de niveaux d'administration ; approuver les exceptions (risque moyen/élevé) ; réviser les rapports trimestriels |
| **Responsable de la sécurité informatique** | Gestion quotidienne de l'infrastructure d'authentification ; surveiller les alertes d'authentification et d'accès à privilèges ; mener les campagnes trimestrielles de certification des accès ; approuver les demandes de comptes de service ; approuver les exceptions à faible risque |
| **Exploitation informatique / Équipe GIA** | Gérer le fournisseur d'identité et l'infrastructure SSO ; traiter les demandes d'accès à privilèges et JIT ; maintenir l'enrôlement AMF ; exécuter le provisionnement et le déprovisionnement ; générer les rapports de certification des accès ; maintenir l'inventaire des comptes de service ; gérer le déploiement PAW |
| **Administrateurs système** | Mettre en œuvre les contrôles d'accès sur les systèmes gérés ; se conformer aux exigences du modèle de niveaux d'administration ; utiliser des comptes à privilèges dédiés ; signaler les anomalies de contrôle d'accès |
| **Tous les utilisateurs** | Protéger les identifiants d'authentification ; signaler immédiatement toute compromission suspectée des identifiants ; compléter l'enrôlement AMF dans le délai requis ; ne pas partager les comptes ou identifiants ; ne pas tenter de contourner les contrôles d'accès |

---

## Indicateurs clés de performance

Les métriques suivantes doivent être suivies pour mesurer l'efficacité des contrôles d'authentification et d'accès à privilèges :

| Métrique | Cible | Fréquence |
|----------|-------|-----------|
| Enrôlement AMF (tous les utilisateurs) | ≥ 95 % | Mensuel |
| Enrôlement AMF (utilisateurs à privilèges) | 100 % | Mensuel |
| Achèvement des révisions d'accès à privilèges | 100 % | Trimestriel |
| Conformité à la politique de mots de passe | ≥ 98 % | Mensuel |
| Intégration des applications SaaS en SSO | ≥ 80 % (Année 1) ; ≥ 90 % (Année 2) | Trimestriel |
| Enregistrement des sessions à privilèges (Niveau 0) | 100 % | Mensuel |
| Conformité à la rotation des identifiants (comptes de service) | 100 % dans les délais | Trimestriel |
| Achèvement du test des comptes d'urgence | 100 % | Semestriel |
| Adoption de l'accès JIT (Niveau 1) | ≥ 50 % (Année 1) ; ≥ 80 % (Année 2) | Trimestriel |
| Exhaustivité de l'inventaire des comptes de service | 100 % | Trimestriel |
| Taux d'achèvement de la certification des accès | 100 % | Trimestriel |
| Couverture des politiques d'accès conditionnel | 100 % des politiques définies appliquées | Trimestriel |
| Contrôle des identifiants compromis | 100 % des événements de définition/modification validés | Mensuel |

Les métriques doivent être communiquées au RSSI trimestriellement. Les métriques en dessous de la cible doivent inclure un plan de remédiation avec propriétaire et date cible.

---

## Preuves

Les preuves suivantes démontrent la conformité à cette politique :

| N° | Preuve | Responsable | Fréquence |
|----|--------|-------------|-----------|
| 1 | Preuves de **configuration de la politique de mots de passe** (paramètres du fournisseur d'identité, configuration du contrôle de violations) | Exploitation informatique | *Capturé annuellement ou lors d'une modification* |
| 2 | **Rapports d'enrôlement AMF** (pourcentage de couverture par type d'utilisateur : à privilèges, standard, distant) | Sécurité informatique | *Mensuel pour les utilisateurs à privilèges ; trimestriel pour tous* |
| 3 | **Inventaire des intégrations SSO** (intégrées vs. non intégrées, enregistrements d'exceptions) | Exploitation informatique | *Révisé trimestriellement* |
| 4 | **Inventaire des comptes à privilèges** (compte, propriétaire, niveau, objectif, date de dernière révision) | Sécurité informatique | *Révisé trimestriellement* |
| 5 | **Enregistrements d'achèvement des révisions d'accès à privilèges** (attestation, réviseur, date, actions prises) | Sécurité informatique | *Trimestriel ; conservé 3 ans* |
| 6 | **Échantillons d'enregistrements de session** (sessions Niveau 0 ; échantillon aléatoire révisé pour détecter les anomalies) | Sécurité informatique | *Révisé trimestriellement* |
| 7 | **Enregistrements de test des comptes d'urgence** (date, testeur, résultat, confirmation de rotation post-test) | Sécurité informatique | *Semestriel* |
| 8 | **Journaux de rotation des identifiants** (comptes de service, comptes d'urgence, comptes partagés) | Exploitation informatique | *Par événement de rotation ; audité semestriellement* |
| 9 | **Journaux d'événements d'authentification** (connexions réussies/échouées, verrouillages, investigations d'anomalies) | Sécurité informatique | *Conservés 12 mois ; anomalies investiguées dans les 24 heures* |
| 10 | **Rapports de tests d'intrusion et d'audit des permissions** (constatations de contrôle d'accès et statut de remédiation) | Sécurité informatique | *Test d'intrusion annuellement ; audits des permissions trimestriellement* |
| 11 | **Inventaire des comptes de service** (nom du compte, propriétaire, niveau, objectif, emplacement des identifiants, dernière/prochaine rotation) | Sécurité informatique | *Maintenu en continu ; révisé trimestriellement ; conservé 3 ans* |
| 12 | **Journaux d'accès JIT** (demandes, approbations, durée, confirmation de révocation automatique) | Sécurité informatique | *Par événement ; audité trimestriellement ; conservé 12 mois* |
| 13 | **Enregistrements de campagnes de certification des accès** (résultats de campagne, attestations des réviseurs, révocations traitées) | Sécurité informatique | *Trimestriel ; conservé 3 ans* |
| 14 | **Documentation des politiques d'accès conditionnel** (définitions de politiques, statut de déploiement, exceptions) | Exploitation informatique | *Révisé trimestriellement ; mis à jour lors de modifications de politique* |
| 15 | **Statut de déploiement PAW** (inventaire des PAW, conformité de configuration, suivi de la phase de déploiement) | Sécurité informatique | *Révisé trimestriellement ; conservé 3 ans* |
| 16 | **Inventaire des intégrations SSO** (applications, statut SSO, niveau de priorité, enregistrements d'exceptions) | Exploitation informatique | *Révisé trimestriellement ; conservé 3 ans* |

---

# Conformité à la politique

## Mesure de la conformité

L'équipe de gestion de la sécurité de l'information vérifiera la conformité à cette politique par diverses méthodes, notamment les audits de configuration du fournisseur d'identité, les rapports de couverture AMF, les révisions des accès à privilèges, les tests d'intrusion, les audits internes et externes, et les retours adressés au propriétaire de la politique.

## Exceptions

Toute exception à cette politique doit être approuvée et enregistrée à l'avance par le Responsable de la sécurité de l'information, avec acceptation des risques documentée, contrôles compensatoires et date de révision définie. Les exceptions doivent être signalées à l'équipe de revue de direction. Durée maximale de l'exception : 12 mois, renouvelable avec ré-approbation.

## Non-conformité

Un employé dont il est établi qu'il a enfreint cette politique peut faire l'objet de mesures disciplinaires, pouvant aller jusqu'au licenciement.

**Réponse progressive** (sur une période de 12 mois glissants) :

| Occurrence | Réponse | Délai | Responsable |
|------------|---------|-------|-------------|
| Première | Rappel de sensibilisation et formation ciblée | Dans les 5 jours ouvrables | Sécurité informatique |
| Deuxième (dans les 90 jours) | Notification du responsable + avertissement documenté | Dans les 3 jours ouvrables | Sécurité informatique + RH |
| Troisième (dans les 12 mois) | Restriction d'accès en attente de remédiation | Immédiat | Sécurité informatique + Responsable |
| Violation délibérée / critique | Mesures disciplinaires conformément aux politiques RH | Escalade immédiate | RH + RSSI |

**Violations critiques** justifiant une escalade immédiate indépendamment des antécédents :

- Partage d'identifiants à privilèges.
- Contournement délibéré des contrôles de sécurité.
- Violations d'isolation des niveaux.
- Utilisation non autorisée des comptes d'urgence.

**Échecs aux simulations d'hameçonnage** (sur une période de 12 mois glissants) :

- 1 échec : Formation de sensibilisation ciblée (dans les 7 jours).
- 2 échecs : Notification du responsable + formation supplémentaire (dans les 5 jours).
- 3+ échecs : Accès à privilèges suspendu ; accès standard restreint en attendant une amélioration démontrée.

## Amélioration continue

Cette politique est révisée et mise à jour dans le cadre du processus d'amélioration continue. Les révisions doivent tenir compte des modifications des normes d'authentification (y compris les révisions de NIST SP 800-63B), des menaces émergentes (bourrage d'identifiants, hameçonnage, techniques de contournement AMF), des changements réglementaires et des enseignements tirés des incidents.

---

# Domaines de la norme ISO 27001 couverts

Politique d'authentification et d'accès à privilèges — Correspondance avec les contrôles ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership et engagement | 5.1 Politiques de sécurité de l'information |
| Clause 5.2 Politique | 5.4 Responsabilités de la direction |
| Clause 6.2 Objectifs de sécurité de l'information | 5.15 Contrôle d'accès |
| Clause 7.3 Sensibilisation | 5.17 Informations d'authentification |
| Clause 7.5.3 Maîtrise des informations documentées | 5.36 Conformité aux politiques, règles et normes |
| | 6.3 Sensibilisation, éducation et formation à la sécurité de l'information |
| | 6.4 Processus disciplinaire |
| | **8.2 Droits d'accès à privilèges** |
| | **8.3 Restriction de l'accès à l'information** |
| | **8.5 Authentification sécurisée** |

**Cadre réglementaire et juridique** :

| Cadre | Pertinence |
|-------|-----------|
| nLPD suisse (revDSG) | Art. 8 — Mesures techniques et organisationnelles incluant les contrôles d'authentification et d'accès |
| OPDo suisse (Ordonnance sur la protection des données) | Art. 1-3 — Exigences minimales de sécurité des données |
| RGPD de l'UE (le cas échéant) | Art. 32 — Sécurité du traitement (contrôles d'authentification comme mesure appropriée) |
| ISO/IEC 27001:2022 | Contrôles Annexe A 8.2, 8.3, 8.5 |
| ISO/IEC 27002:2022 | Sections 8.2, 8.3, 8.5 — Recommandations de mise en œuvre |
| NIST SP 800-63B | Lignes directrices sur l'identité numérique et l'authentification (secrets mémorisés, AMF) |
| NIST CSF 2.0 | PR.AA (Gestion des identités, authentification et contrôle d'accès) |
| CIS Controls v8 | Contrôle 5 (Gestion des comptes), Contrôle 6 (Gestion du contrôle d'accès) |

---

<!-- QA_VERIFIED: 2026-03-29 -->
