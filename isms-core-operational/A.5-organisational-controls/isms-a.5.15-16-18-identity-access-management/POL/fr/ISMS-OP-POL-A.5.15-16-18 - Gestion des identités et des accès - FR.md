<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.5.15-16-18-FR:operational:OP-POL:a.5.15-16-18 -->
**ISMS-OP-POL-A.5.15-16-18 — Gestion des identités et des accès**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Gestion des identités et des accès |
| **Type de document** | Politique opérationnelle |
| **Identifiant du document** | ISMS-OP-POL-A.5.15-16-18 |
| **Créateur du document** | Responsable de la sécurité des systèmes d'information (RSSI) |
| **Propriétaire du document** | Directeur général (PDG) |
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

- ISO/IEC 27001:2022 Contrôles A.5.15, A.5.16, A.5.18 — Contrôle d'accès, gestion des identités, droits d'accès

**Contrôles Annexe A connexes** :

| Contrôle | Relation avec la GIA |
|----------|----------------------|
| A.5.3 Séparation des tâches | La matrice de SdT est appliquée via les contrôles d'accès |
| A.5.10 Utilisation acceptable de l'information | L'utilisation acceptable dépend des accès accordés |
| A.5.12–13 Classification et étiquetage | La classification détermine le niveau d'accès requis |
| A.5.17 Informations d'authentification | Gestion des identifiants pour les identités authentifiées |
| A.5.19–23 Relations avec les fournisseurs | Gouvernance des accès des tiers |
| A.5.24–28 Gestion des incidents | Gestion des incidents de compromission de comptes |
| A.8.2 Droits d'accès privilégiés | Gestion des accès privilégiés |
| A.8.3 Restriction d'accès à l'information | Application technique des règles d'accès |
| A.8.5 Authentification sécurisée | Mécanismes d'authentification pour la vérification d'identité |
| A.8.11 Masquage des données | Contrôles de masquage alignés sur la classification d'accès |

**Politiques internes connexes** :

- Politique de classification et de traitement de l'information
- Politique d'authentification et d'accès privilégié
- Politique de gestion des incidents
- Politique de transfert de l'information
- Politique de développement sécurisé

---

# Politique de contrôle d'accès

## Objet

L'objet de cette politique est d'assurer un accès correct aux informations et ressources appropriées par les personnes appropriées, et de gérer le cycle de vie complet des identités utilisateurs.

Cette politique soutient la nFADP suisse (LPD révisée) en mettant en œuvre des mesures techniques et organisationnelles appropriées au risque pour protéger les données personnelles (y compris les données personnelles sensibles) par des contrôles d'accès. Là où l'organisation traite des données de personnes résidant dans l'UE/EEE, les exigences du RGPD s'appliquent également.

## Périmètre

Tous les employés et utilisateurs tiers.
Tous les systèmes et applications considérés comme dans le périmètre par la déclaration de périmètre ISO 27001.
L'accès physique est défini dans la Politique physique et environnementale.

## Principe

Le contrôle d'accès est accordé selon le principe du moindre privilège. Les utilisateurs ne bénéficient que de l'accès aux informations nécessaires à l'accomplissement de leurs tâches et de leur rôle.

L'accès est refusé par défaut et n'est accordé qu'avec une approbation documentée. Toutes les décisions d'accès doivent être basées sur les risques, en tenant compte de la classification des informations et de la criticité du système.

---

## Accords de confidentialité

Tous les employés et prestataires auxquels un accès aux informations confidentielles est accordé doivent signer un accord de confidentialité ou de non-divulgation avant de se voir accorder l'accès aux installations de traitement de l'information.

## Accès basé sur les rôles

L'accès aux systèmes est basé sur le rôle. L'accès est accordé par le propriétaire métier, le propriétaire du système ou le propriétaire des données, et formellement approuvé.

L'organisation doit mettre en œuvre le contrôle d'accès basé sur les rôles (RBAC) comme méthode privilégiée d'attribution des accès. Les rôles doivent être documentés et révisés annuellement par les propriétaires métier.

## Identifiant unique

Les utilisateurs se voient attribuer un nom d'utilisateur ou identifiant unique selon le principe un utilisateur, un identifiant, afin d'assurer la responsabilité individuelle. Les noms d'utilisateur et identifiants ne doivent pas être partagés entre utilisateurs.

Les comptes partagés sont interdits sauf lorsque techniquement inévitables (systèmes hérités, comptes requis par les fournisseurs). Toute exception nécessite l'approbation écrite du RSSI avec une justification commerciale documentée, des contrôles compensatoires (journalisation des utilisateurs individuels, révision trimestrielle) et une acceptation formelle des risques. Les comptes partagés doivent être inclus dans le registre des comptes privilégiés.

## Authentification des accès

Les utilisateurs sont positivement identifiés et authentifiés avant d'obtenir l'accès aux systèmes, services ou informations.

L'authentification multifacteur (MFA) doit être requise pour :

- Tous les accès à distance aux réseaux et services cloud de l'organisation.
- Tous les comptes privilégiés et administrateurs.
- Toutes les applications exposées en externe.
- Tous les systèmes traitant des données confidentielles ou personnelles.

Les systèmes ne pouvant pas prendre en charge la MFA doivent être documentés dans le registre des risques avec une justification technique, des contrôles compensatoires (p. ex., segmentation réseau, surveillance renforcée) et une acceptation des risques approuvée par le RSSI, révisée annuellement.

## Révision des droits d'accès

L'accès des utilisateurs aux systèmes doit être révisé périodiquement pour s'assurer qu'il est toujours approprié et pertinent :

| Type de compte | Fréquence de révision |
|----------------|----------------------|
| Comptes privilégiés / administrateurs | Trimestrielle |
| Accès des tiers / prestataires | Trimestrielle |
| Comptes de service | Trimestrielle |
| Comptes utilisateurs standard | Annuelle |

Les comptes inactifs et dormants doivent faire l'objet d'une investigation. Un compte est considéré comme inactif s'il ne s'est pas authentifié avec succès pendant la période spécifiée. Les comptes inactifs depuis plus de 45 jours doivent être désactivés. Les comptes inactifs depuis plus de 90 jours doivent être supprimés à moins qu'une justification commerciale documentée n'existe.

Les comptes de service sont exemptés de la désactivation basée sur l'inactivité, mais doivent être révisés trimestriellement pour vérifier qu'ils restent en usage actif et sont toujours nécessaires. Les comptes de service non utilisés doivent être désactivés immédiatement lors de leur découverte.

## Comptes privilégiés / Comptes administrateurs

Les comptes administrateurs ne doivent pas être attribués aux utilisateurs pour les tâches standard, y compris, mais sans s'y limiter, les ordinateurs portables et la technologie mobile.

Dans la mesure du possible, les utilisateurs privilégiés et administrateurs doivent se voir attribuer des comptes privilégiés spécifiques en plus de leur compte normal, pour l'usage exclusif de l'accomplissement des tâches privilégiées et administratives.

Les comptes privilégiés et administrateurs doivent :

- Ne pas être des comptes partagés ou génériques.
- Être clairement identifiables (convention de nommage).
- Être journalisés et surveillés.
- Être limités dans le temps lorsque cela est faisable (accès juste-à-temps préféré).
- Être enregistrés dans un inventaire maintenu.

## Comptes de service

Les comptes de service (comptes non humains utilisés par les applications, les scripts ou les processus automatisés) doivent être gérés conformément aux exigences suivantes :

- La création de compte de service doit être approuvée par le propriétaire du système et le RSSI.
- Tous les comptes de service doivent être documentés avec leur objectif, système/application, propriétaire et date de révision.
- Les comptes de service ne doivent se voir accorder que les autorisations minimales requises pour leur fonction.
- Les comptes de service ne doivent pas être utilisés pour une connexion interactive par le personnel.
- Les identifiants des comptes de service doivent être stockés dans une solution de gestion des secrets approuvée, et non codés en dur ou stockés en texte clair.
- L'activité des comptes de service doit être journalisée et surveillée pour détecter les comportements anormaux.
- Les comptes de service doivent être révisés trimestriellement conformément au calendrier de révision des accès.

## Mots de passe

L'accès aux systèmes et aux informations est authentifié par des mots de passe. L'organisation doit appliquer les normes de mots de passe suivantes :

| Exigence | Norme |
|----------|-------|
| Longueur minimale | 12 caractères |
| Complexité | Longueur plutôt que complexité ; pas de règles de composition obligatoires (conformément à NIST SP 800-63B) |
| Dépistage | Les mots de passe doivent être validés par rapport aux bases de données d'identifiants compromis/violés connus |
| Rotation | Basée sur les événements uniquement — en cas de compromission suspectée ou confirmée ; la rotation périodique forcée n'est pas requise |
| Mots de passe initiaux | Doivent être changés lors de la première utilisation |
| Mots de passe par défaut | Les mots de passe fournis par les fournisseurs et les mots de passe par défaut doivent être changés immédiatement lors de l'installation |
| Partage | Les mots de passe ne doivent pas être génériques, partagés ou définis au niveau d'un groupe |
| Confidentialité | Les mots de passe doivent rester confidentiels et ne pas être notés |
| Affichage | Les mots de passe ne doivent pas être affichés lors de leur saisie |
| Code | Les mots de passe ne doivent pas être codés ou inclus dans des scripts, du code ou des macros |
| Transmission | Les mots de passe doivent être chiffrés lors de leur transmission sur les réseaux |
| Stockage | Les mots de passe doivent être stockés à l'aide de fonctions de hachage cryptographique approuvées (bcrypt, scrypt, Argon2 ou PBKDF2) et jamais en texte clair ou avec un chiffrement réversible |
| Verrouillage | Les systèmes doivent verrouiller les utilisateurs après 6 tentatives d'accès infructueuses |
| Délai d'expiration de session | Les sessions système inactives pendant 15 minutes doivent nécessiter une nouvelle authentification (5 minutes pour les systèmes traitant des données personnelles sensibles ou des données financières) |
| Gestionnaires de mots de passe | L'utilisation de gestionnaires de mots de passe approuvés par l'organisation est recommandée |

## Provisionnement des comptes utilisateurs

La création, la modification et la suppression de comptes doivent être effectuées par du personnel autorisé et intégralement documentées.

L'organisation doit mettre en œuvre un processus Arrivée-Mobilité-Départ (AMB) :

| Événement RH | Action sur les accès | Délai |
|-------------|---------------------|-------|
| Nouvelle embauche | Création de compte avec accès basé sur le rôle | Accès prêt à la date de prise de poste |
| Changement de rôle | Accès ajusté au nouveau rôle ; accès précédent supprimé | Dans les 2 jours ouvrables |
| Cessation (volontaire) | Tous les accès révoqués | Le même jour ouvrable |
| Cessation (pour faute) | Tous les accès révoqués | Immédiatement (dans l'heure) |
| Fin de contrat | Accès prestataire/fournisseur supprimé | À la date de fin de contrat |

Les propriétaires métier, système ou d'informations doivent approuver l'accès aux systèmes et aux informations. Une demande documentée doit clairement indiquer l'accès requis et un enregistrement d'autorisation doit être maintenu.

**Flux de travail de demande d'accès :**

1. L'utilisateur soumet une demande via le service d'assistance informatique ou l'outil de gestion des accès, en spécifiant le système, le rôle et la justification commerciale.
2. Le responsable hiérarchique approuve le besoin commercial.
3. Le propriétaire du système ou des données approuve le niveau d'accès.
4. L'informatique provisionne l'accès et enregistre l'autorisation.
5. Le demandeur confirme que l'accès est fonctionnel.

L'accès d'urgence (bris de glace) peut être accordé par l'informatique avec l'approbation verbale du RSSI et doit être formellement documenté dans un délai d'un jour ouvrable.

Tous les utilisateurs demandant des réinitialisations de mot de passe ou des modifications des identifiants d'authentification doivent faire vérifier leur identité par au moins l'une des méthodes suivantes :

- Vérification d'un contact secondaire préenregistré (e-mail, téléphone).
- Challenge-réponse à l'aide de questions de sécurité préétablies.
- Vérification en personne avec pièce d'identité avec photo.
- Confirmation de l'identité de l'utilisateur par le responsable ou les RH.

La réinitialisation du mot de passe en libre-service via le fournisseur d'identité (avec inscription MFA vérifiée) est acceptable et ne nécessite pas de vérification d'identité supplémentaire.

## Collaborateurs partants

Les responsables hiérarchiques et les RH doivent informer l'équipe de provisionnement des comptes de la date de départ d'un utilisateur.

Lorsqu'un utilisateur quitte l'organisation, tous ses accès doivent être révoqués le même jour ouvrable, au minimum pour la principale technologie d'authentification, et pour tous les systèmes et données enregistrés dans la liste d'accès basée sur le rôle.

Les identifiants utilisateurs, mots de passe et identifiants d'authentification des collaborateurs partants ne doivent pas être réutilisés.

## Authentification

Le système d'authentification d'accès principal doit :

- Ne pas afficher les identifiants de système ou d'application tant que le processus de connexion n'est pas mené à bien.
- Afficher un avis général avertissant que le système ne doit être accessible que par des utilisateurs autorisés.
- Ne pas fournir de messages d'aide pendant la procédure de connexion qui aideraient un utilisateur non autorisé.
- Valider les informations de connexion uniquement à la fin de la saisie de toutes les données. En cas d'erreur, le système ne doit pas indiquer quelle partie des données est correcte ou incorrecte.
- Protéger contre les tentatives de connexion par force brute.
- Journaliser les tentatives infructueuses et réussies.
- Déclencher un événement de sécurité si une tentative ou une violation réussie des contrôles de connexion est détectée.
- Ne pas afficher un mot de passe lors de sa saisie.
- Ne pas transmettre les mots de passe en clair sur un réseau.
- Terminer les sessions inactives après une période d'inactivité définie, notamment dans les lieux à risque élevé tels que les espaces publics ou les zones externes en dehors de la gestion de la sécurité de l'organisation ou sur les appareils mobiles.
- Restreindre les durées de connexion pour fournir une sécurité supplémentaire pour les applications à risque élevé.

## Accès à distance

L'accès à distance aux réseaux de l'organisation, aux services cloud et aux applications accessibles en externe suit les mêmes règles couvertes par cette politique avec l'exigence supplémentaire d'une authentification multifacteur.

Les connexions à distance doivent être configurées pour se déconnecter après une période d'inactivité définie.

Une liste des utilisateurs bénéficiant d'un accès à distance aux systèmes réseau internes doit être maintenue et révisée trimestriellement.

## Accès à distance des tiers

L'accès n'est accordé aux tiers que dans le cadre d'un contrat en cours avec un accord de non-divulgation applicable en place.

L'accès doit être accordé pour une durée spécifique, à un système spécifique, à un individu spécifique, et fourni à la réception d'une demande d'accès formelle, valide et autorisée.

L'accès doit être supprimé immédiatement à la fin de la demande ou à l'expiration du contrat, selon la première échéance.

Une liste des tiers et des individus bénéficiant d'un accès doit être maintenue et révisée trimestriellement.

## Surveillance et rapportage

L'accès aux systèmes doit être surveillé et rapporté. Les actions qui affectent directement ou indirectement ou pourraient affecter la confidentialité, l'intégrité ou la disponibilité des données doivent être gérées via le processus de gestion des incidents.

## Masquage des données

L'organisation masque les données conformément aux obligations légales et réglementaires, y compris les exigences de la nFADP suisse et du RGPD le cas échéant.

---

## Preuves

Les preuves suivantes démontrent la conformité à cette politique :

- **Inventaire des comptes utilisateurs** (comptes actifs par type : employé, prestataire, service, partagé) — *maintenu dans le fournisseur d'identité ou l'outil de gestion des accès ; exporté trimestriellement*
- **Enregistrements du processus AMB** (journaux des flux de travail arrivée/mobilité/départ avec horodatages) — *conservés 12 mois après le départ ; audités semestriellement*
- **Enregistrements de révision des accès** (trimestrielle pour les privilégiés, annuelle pour les standard) — *signés par les propriétaires de systèmes ; conservés 3 ans*
- **Journaux de remédiation des comptes orphelins/dormants** — *révisés mensuellement ; comptes désactivés documentés*
- **Enregistrements d'inscription MFA** sur les systèmes — *rapport de couverture généré trimestriellement ; cible 100 % pour les systèmes dans le périmètre*
- **Registre des comptes privilégiés et journaux d'utilisation** — *révisés trimestriellement ; utilisation anormale investiguée*
- **Registre des comptes de service** (propriétaire, objectif, système, date de révision) — *révisé trimestriellement*
- **Registre des accès des tiers** avec dates d'expiration des contrats — *révisé trimestriellement ; accès révoqué à la fin du contrat*
- **Preuves de configuration de la politique de mots de passe** (captures d'écran système ou exportations d'audit) — *capturées annuellement ou lors de changements*
- **Enregistrements des demandes et approbations d'accès** — *conservés 12 mois ; échantillon audité lors des audits internes*

---

# Conformité à la politique

## Mesure de la conformité

L'équipe de gestion de la sécurité de l'information vérifiera la conformité à cette politique par diverses méthodes, notamment les rapports de révision des accès, les pistes d'audit AMB, la surveillance des accès privilégiés, les audits internes et externes, et les retours d'information au propriétaire de la politique.

## Exceptions

Toute exception à cette politique doit être approuvée et consignée par le Responsable de la sécurité de l'information à l'avance, avec une acceptation documentée des risques, des contrôles compensatoires et une date de révision définie. Les exceptions doivent être rapportées à l'équipe de Révision de direction.

## Non-conformité

Un employé reconnu coupable d'avoir enfreint cette politique peut faire l'objet de mesures disciplinaires, pouvant aller jusqu'au licenciement.

## Amélioration continue

Cette politique est révisée et mise à jour dans le cadre du processus d'amélioration continue. Les révisions doivent prendre en compte les changements des normes de gestion des identités et des accès, les menaces émergentes, les changements réglementaires et les enseignements tirés des incidents.

---

# Périmètre de la norme ISO 27001 couvert

Politique de gestion des identités et des accès — Cartographie des contrôles ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership et engagement | 5.1 Politiques de sécurité de l'information |
| Clause 5.2 Politique | 5.3 Séparation des tâches |
| Clause 6.2 Objectifs de sécurité de l'information | 5.4 Responsabilités de la direction |
| Clause 7.3 Sensibilisation | **5.15 Contrôle d'accès** |
| Clause 7.5.3 Contrôle des informations documentées | **5.16 Gestion des identités** |
| | 5.17 Informations d'authentification |
| | **5.18 Droits d'accès** |
| | 5.36 Conformité aux politiques, règles et normes |
| | 8.2 Droits d'accès privilégiés |
| | 8.3 Restriction d'accès à l'information |
| | 8.5 Authentification sécurisée |
| | 8.11 Masquage des données |

**Cadre réglementaire et juridique** :

| Cadre | Pertinence |
|-------|-----------|
| nFADP suisse (LPD révisée) | Art. 8 — Mesures techniques et organisationnelles incluant les contrôles d'accès |
| DSV suisse (Ordonnance sur la protection des données) | Art. 1-3 — Exigences minimales pour la sécurité des données |
| RGPD UE (le cas échéant) | Art. 32 — Sécurité du traitement (contrôles d'accès comme mesure appropriée) |
| ISO/IEC 27001:2022 | Contrôles Annexe A 5.15, 5.16, 5.18 |
| ISO/IEC 27002:2022 | Sections 5.15, 5.16, 5.18 — Conseils d'implémentation |
| NIST SP 800-63B | Directives sur l'identité numérique et l'authentification |
| CIS Controls v8 | Contrôles 5 (Gestion des comptes) et 6 (Gestion du contrôle d'accès) |

---

<!-- QA_VERIFIED: 2026-03-29 -->
