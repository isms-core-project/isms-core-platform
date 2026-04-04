<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.5.29-FR:operational:OP-POL:a.5.29 -->
**ISMS-OP-POL-A.5.29 — Sécurité de l'information lors d'une perturbation**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Sécurité de l'information lors d'une perturbation |
| **Type de document** | Politique opérationnelle |
| **Identifiant du document** | ISMS-OP-POL-A.5.29 |
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

- ISO/IEC 27001:2022 Contrôle A.5.29 — Sécurité de l'information lors d'une perturbation
- ISO/IEC 22301 — Systèmes de management de la continuité d'activité (référence informative)
- NIST SP 800-34 Rev 1 — Guide de planification des mesures d'urgence pour les systèmes d'information fédéraux (référence informative)
- NIST SP 800-61 Rev 2 — Guide de gestion des incidents de sécurité informatique (référence informative)

**Contrôles Annexe A connexes** :

| Contrôle | Relation avec la sécurité de l'information lors d'une perturbation |
|----------|-------------------------------------------------------------------|
| A.5.24–28 Cycle de vie de la gestion des incidents | Les incidents de sécurité peuvent déclencher ou coïncider avec des perturbations de l'activité |
| A.5.30 Préparation TIC pour la continuité d'activité | La planification BC/DR fournit le cadre opérationnel ; A.5.29 fournit la couche sécurité |
| A.8.13 Sauvegarde des informations | La protection des sauvegardes est un contrôle de sécurité non négociable lors d'une perturbation |
| A.8.14 Redondance des installations de traitement de l'information | La sécurité du site de reprise doit être équivalente à celle du site principal |
| A.5.15–16–18 Gestion des identités et des accès | Procédures d'accès d'urgence et contrôle d'accès lors d'une perturbation |
| A.8.15 Journalisation | La continuité de la journalisation est obligatoire même en mode dégradé |
| A.8.16 Surveillance des activités | Une surveillance renforcée est requise en mode élevé et dégradé |

**Politiques internes connexes** :

- Politique de continuité d'activité et de reprise après sinistre
- Politique de gestion des incidents
- Politique de gestion des identités et des accès
- Politique de journalisation
- Politique de surveillance des activités (A.8.16)
- Politique de gestion des changements

---

# Politique de sécurité de l'information lors d'une perturbation

## Objet

La présente politique établit les exigences pour le maintien des contrôles de sécurité de l'information pendant les événements perturbateurs. Les perturbations — qu'il s'agisse de catastrophes naturelles, de défaillances d'infrastructure, de cyberattaques, de pandémies ou d'interruptions de la chaîne d'approvisionnement — créent des conditions dans lesquelles les contrôles de sécurité sont les plus susceptibles d'être affaiblis précisément au moment où l'exposition aux menaces est la plus élevée.

**« La sécurité ne peut pas prendre de vacances. »** Lorsque les organisations se concentrent sur la reprise, les adversaires exploitent la vigilance réduite, le personnel distrait et les contrôles dégradés. Cette politique garantit que l'organisation maintient une posture de sécurité minimale définie tout au long de toutes les phases de perturbation et de reprise, et valide que les contrôles de sécurité complets sont restaurés avant le retour aux opérations normales.

Cette politique soutient la nLPD suisse (revDSG) art. 8 en maintenant des mesures de sécurité techniques et organisationnelles appropriées dans des conditions défavorables. Lorsque l'organisation traite des données de personnes dans l'UE/EEE, les exigences du RGPD art. 32 concernant la sécurité continue du traitement s'appliquent également.

## Champ d'application

Cette politique s'applique à :

- Tous les événements perturbateurs affectant la capacité de l'organisation à fonctionner normalement, notamment les catastrophes naturelles, les défaillances d'infrastructure, les incidents cyber, les pandémies, les perturbations de la chaîne d'approvisionnement et les troubles civils.
- Tous les systèmes d'information, réseaux, applications et installations de traitement des données dans le périmètre ISO 27001.
- Tous les processus de continuité d'activité et de reprise après sinistre.
- Tout le personnel — employés, contractants et utilisateurs tiers — pendant les phases de perturbation et de reprise.

## Principe

**La sécurité des personnes doit être notre première priorité. Toujours.**

Une fois la sécurité et le bien-être du personnel assurés, la continuité de la sécurité de l'information devient la priorité immédiate. L'organisation doit planifier, mettre en œuvre et maintenir des processus pour garantir le niveau requis de sécurité de l'information dans des situations défavorables, y compris des mesures compensatoires lorsque les mesures de sécurité standard ne peuvent pas être maintenues.

Aucune action de reprise, aussi urgente soit-elle, ne justifie la suppression permanente des contrôles de sécurité essentiels. Lorsqu'un assouplissement temporaire est nécessaire, il doit être documenté, limité dans le temps, compensé et suivi jusqu'à sa clôture.

---

## Définitions

| Terme | Définition |
|-------|-----------|
| **Perturbation** | Tout événement qui interrompt ou menace d'interrompre les opérations normales de l'activité |
| **Niveau de posture de sécurité** | État défini de la mise en œuvre des contrôles de sécurité (Normal, Élevé, Dégradé, Urgence, Reprise) |
| **Référentiel de sécurité minimal** | Contrôles de sécurité non négociables qui doivent être maintenus quel que soit l'état opérationnel |
| **Accès bris de glace (break-glass)** | Mécanisme d'accès privilégié d'urgence activé lorsque l'accès normal est indisponible |
| **Dette de sécurité** | Contrôles ou activités de sécurité différés pendant une perturbation qui nécessitent une remédiation ultérieure |
| **Site de reprise** | Emplacement alternatif (physique ou cloud) pour la reprise des opérations pendant une perturbation |
| **Mesure compensatoire** | Mesure de sécurité alternative mise en œuvre lorsque le contrôle principal est indisponible |
| **Équipe de gestion de crise** | Équipe plurifonctionnelle activée pour gérer la réponse organisationnelle à une perturbation majeure |

---

## Référentiel de sécurité minimal

### Contrôles non négociables

Les contrôles de sécurité suivants doivent être maintenus en tout temps, quel que soit l'état de perturbation. Ces contrôles ne sont pas soumis à assouplissement ou exception :

| Catégorie de contrôle | Exigence minimale | Justification |
|-----------------------|-------------------|---------------|
| **Contrôle d'accès** | Authentification requise pour tout accès au système | Prévient les accès non autorisés dans des conditions chaotiques |
| **Chiffrement des données** | Chiffrement au repos pour les données CONFIDENTIEL et RESTREINT | Les données restent protégées si les supports sont perdus, volés ou exposés pendant la reprise |
| **Journalisation** | La journalisation des systèmes critiques continue sur tous les systèmes de niveau 1 et 2 | Maintient la piste d'audit pour l'investigation post-incident et la conformité réglementaire |
| **Segmentation réseau** | Les frontières réseau critiques sont maintenues | Prévient le mouvement latéral si un attaquant exploite la perturbation |
| **Protection des sauvegardes** | Les sauvegardes restent chiffrées et avec contrôle d'accès | Prévient la compromission des sauvegardes comme route alternative pour le vol de données |

### Contrôles acceptables en mode dégradé

Les contrôles suivants peuvent être temporairement assouplis pendant une perturbation, sous réserve d'une approbation documentée du RSSI (ou de son suppléant désigné), de la mise en œuvre de mesures compensatoires, et d'une entrée dans le Registre de la dette de sécurité :

| Catégorie de contrôle | Dégradation acceptable | Mesure compensatoire requise | Durée maximale |
|-----------------------|----------------------|------------------------------|----------------|
| **Authentification multifacteur** | Monofacteur si l'infrastructure MFA est indisponible | Journalisation renforcée, limites de durée de session, restrictions IP | Durée de la perturbation + 7 jours |
| **Analyse de vulnérabilités** | Analyse planifiée différée | Révision manuelle des correctifs critiques ; appliquer les correctifs critiques/élevés dans 72h/7j | 30 jours |
| **Surveillance de la sécurité** | Périmètre de surveillance réduit | Concentrer sur les systèmes de niveau 1 et 2 ; révision manuelle renforcée | Durée de la perturbation + 14 jours |
| **Révisions des accès** | Révisions périodiques reportées | Approbation plus stricte pour les nouvelles demandes d'accès pendant la perturbation | 30 jours |
| **Gestion des correctifs** | Correctifs différés pour les vulnérabilités non critiques | Les vulnérabilités critiques et élevées sont toujours corrigées dans 72h/7j | 30 jours pour les non critiques |

**Suivi obligatoire** : Tout assouplissement de contrôle approuvé doit immédiatement créer une entrée à durée limitée dans le Registre de la dette de sécurité, incluant : le responsable, les mesures compensatoires en vigueur, la date de début, la date cible de clôture et la preuve de clôture à la remédiation.

### Jamais acceptable

Les actions suivantes sont interdites même lors de la perturbation la plus grave. Il n'y a pas d'exceptions :

- **Désactivation de la journalisation** sur les systèmes critiques — la piste d'audit ne doit jamais être interrompue
- **Suppression des exigences d'authentification** — aucun accès anonyme à quelque système que ce soit
- **Déchiffrement des données au repos** sans rechiffrement — les données doivent rester protégées
- **Désactivation des pare-feux ou IDS/IPS** sur les frontières réseau critiques
- **Partage d'identifiants à privilèges** sans responsabilité individuelle — chaque action doit être attribuable à une personne
- **Contournement de la gestion des changements** pour les systèmes de production sans suivre la procédure de changement d'urgence (avec révision post-mise en œuvre obligatoire dans les 5 jours ouvrables)

### Gestion des changements d'urgence pendant une perturbation

**Règle standard** : Toutes les modifications en production nécessitent une approbation de gestion des changements conformément à la Politique de gestion des changements.

**Exception pour changement d'urgence** : Pendant une posture de sécurité **Dégradée** ou d'**Urgence**, des changements d'urgence peuvent être mis en œuvre avec une approbation abrégée, sous réserve des exigences suivantes.

**Critères de changement d'urgence** (tous doivent être remplis) :

1. Le changement est nécessaire pour restaurer les opérations métier critiques ou atténuer un incident de sécurité actif.
2. Le délai jusqu'à l'approbation standard du changement causerait un préjudice significatif.
3. Le changement est approuvé verbalement par le DSI ou le RSSI (ou son suppléant désigné).
4. Le changement est journalisé immédiatement dans [Système de gestion des changements / Ticket d'incident].

**Processus de changement d'urgence** :

1. **Approbation verbale** : Le demandeur du changement contacte le DSI/RSSI via la plateforme de communication de crise ou par téléphone ; décrit le changement, la justification et le plan de retour arrière.
2. **Approbation** : Le DSI ou le RSSI donne l'approbation verbale ; l'approbation est journalisée avec l'horodatage et le nom de l'approbateur.
3. **Mise en œuvre** : Changement mis en œuvre avec surveillance renforcée.
4. **Documentation** : Dans les 4 heures suivant la mise en œuvre — ticket de changement créé dans [Système de gestion des changements] avec les détails : ce qui a changé, pourquoi, qui a approuvé, plan de retour arrière, résultat réel.
5. **Révision post-mise en œuvre** : Dans les 5 jours ouvrables — réunion de révision du changement (DSI, RSSI, implémenteur du changement, propriétaire du système affecté). Déterminer si le changement doit rester, être annulé ou affiné. Documenter les enseignements tirés et toute mise à jour de politique/procédure requise.

**Restrictions des changements d'urgence** :

- Les changements d'urgence ne doivent pas désactiver les contrôles de sécurité de la liste « Jamais acceptable » (journalisation, authentification, chiffrement, pare-feux, gestion des changements elle-même).
- Les changements d'urgence contournant les contrôles de sécurité nécessitent spécifiquement l'approbation du RSSI (pas seulement du DSI).
- Les changements d'urgence augmentant les risques (p. ex. ouverture de règles de pare-feu, réduction des exigences d'authentification) nécessitent des mesures compensatoires documentées avant la mise en œuvre.

**Renvoi** : Procédure complète de changement d'urgence documentée dans la Politique de gestion des changements.

---

## Posture de sécurité à plusieurs niveaux

L'organisation doit opérer à l'un des cinq niveaux de posture de sécurité définis. Le niveau de posture actuel détermine quels contrôles sont pleinement actifs, lesquels peuvent être dégradés, et quelles mesures supplémentaires sont requises.

### Niveaux de posture

| Niveau | État de perturbation | Posture de sécurité | Déclencheurs exemples |
|--------|---------------------|---------------------|----------------------|
| **Normal** | Aucune perturbation | Contrôles de sécurité complets opérationnels | Opérations quotidiennes |
| **Élevé** | Perturbation mineure | Surveillance renforcée, correctifs accélérés | Défaillance d'un seul système, événement de sécurité mineur, alerte météo |
| **Dégradé** | Perturbation modérée | Contrôles essentiels maintenus, contrôles non critiques différés selon la table du mode dégradé | Basculement du centre de données, panne régionale, incident cyber significatif |
| **Urgence** | Perturbation grave | Référentiel minimal uniquement, mode survie | Catastrophe multi-sites, attaque majeure par rançongiciel, confinement pandémique |
| **Reprise** | Retour à la normale | Restauration progressive avec validation de sécurité à chaque phase | Reprise post-catastrophe, reconstruction des systèmes |

### Autorité de transition

Les transitions entre les niveaux de posture doivent être formellement autorisées. L'autorisation verbale est permise dans les situations urgentes, suivie d'une confirmation écrite dans les 4 heures.

| Transition | Autorité requise | Documentation |
|------------|-----------------|---------------|
| Normal → Élevé | RSSI ou Responsable de la sécurité IT | Ticket d'incident ou e-mail de notification |
| Élevé → Dégradé | RSSI + DSI (conjointement) | Notification formelle à la direction générale |
| Dégradé → Urgence | Direction générale (PDG ou délégué) | Document de déclaration d'urgence |
| Tout niveau → Reprise | RSSI | Enregistrement de transition de phase |
| Reprise → Normal | RSSI (confirmé par la direction générale) | Liste de contrôle de réalisation de phase et validation de sécurité signée |

Chaque transition doit être enregistrée avec : date/heure, personne autorisante, justification, état actuel, état cible et tout contrôle affecté.

### Communication du niveau de posture de sécurité

Tout le personnel doit être informé du niveau de posture de sécurité actuel et des exigences associées.

**Canaux de communication** :

| Canal | Format du message | Public |
|-------|------------------|--------|
| **E-mail** | Annonce formelle du niveau de posture du RSSI ou PDG | Tous les employés |
| **Bannière intranet** | Bannière visible en haut de la page d'accueil de l'intranet : « POSTURE DE SÉCURITÉ ACTUELLE : [NIVEAU] — [Brève description] » | Tous les employés (lors de l'accès à l'intranet) |
| **Plateforme de collaboration** (p. ex. Slack/Teams) | Message épinglé dans #général ou #sécurité | Tous les employés |
| **Équipe de gestion de crise** | Notification directe via la plateforme de communication de crise | Équipe de crise, équipe sécurité, direction |

**Convention pour la bannière intranet** :

| Posture | Couleur de bannière | Texte |
|---------|---------------------|-------|
| **Normal** | Vert | « POSTURE DE SÉCURITÉ : NORMALE — Tous les systèmes opérationnels » |
| **Élevé** | Jaune | « POSTURE DE SÉCURITÉ : ÉLEVÉE — Perturbation mineure ; surveillance renforcée en vigueur » |
| **Dégradé** | Orange | « POSTURE DE SÉCURITÉ : DÉGRADÉE — Perturbation modérée ; contrôles essentiels actifs ; suivre les procédures mises à jour » |
| **Urgence** | Rouge | « POSTURE DE SÉCURITÉ : URGENCE — Perturbation grave ; référentiel minimal uniquement ; attendre les instructions » |
| **Reprise** | Bleu | « POSTURE DE SÉCURITÉ : REPRISE — Retour à la normale ; valider les contrôles de sécurité avant de reprendre les opérations standard » |

**Calendrier de communication** :

- Transitions de niveau de posture : Communication immédiate (dans l'heure suivant l'autorisation).
- Mises à jour de statut lors de perturbations prolongées : Quotidiennement (au minimum) ou plus fréquemment selon l'évolution de la situation.
- Retour à Normal : Annonce formelle de « retour à la normale » après validation post-perturbation signée.

La livraison des communications doit être vérifiée (e-mail envoyé, bannière intranet active, message posté sur la plateforme de collaboration). La non-réception déclenche une escalade vers des méthodes de communication alternatives.

---

## Exigences de sécurité des plans BC/DR

Tous les plans de continuité d'activité et de reprise après sinistre doivent inclure des exigences de sécurité examinées et approuvées par le RSSI. La sécurité n'est pas une réflexion après coup dans la planification de la continuité — c'est une exigence de conception.

### Considérations de sécurité dans les plans BC/DR

Les plans BC/DR doivent aborder les quatre domaines suivants :

**1. Contrôle d'accès pendant la reprise**

- Qui a accès aux systèmes et données de reprise (rôles nommés, pas accès global).
- Comment l'accès est authentifié lorsque les systèmes d'identité normaux sont indisponibles.
- Comment l'accès temporaire est révoqué une fois la reprise terminée.
- Contrôles des comptes d'accès d'urgence (voir Accès bris de glace ci-dessous).

**2. Protection des données pendant la reprise**

- Exigences de chiffrement pour les données en transit vers le site de reprise.
- Exigences de chiffrement pour les supports de reprise (physiques et numériques).
- Procédures de chaîne de possession pour le déplacement physique des données.
- Application de la classification des données dans l'environnement de reprise.

**3. Sécurité des communications**

- Canaux de communication sécurisés pour l'équipe de gestion de crise (voir Plateforme de communication de crise ci-dessous).
- Canaux de communication alternatifs si les systèmes principaux sont compromis (p. ex. téléphone hors bande, groupes de messagerie pré-convenus).
- Authentification des communications de crise pour prévenir l'ingénierie sociale pendant la confusion.
- Limites de partage d'information — ce qui peut être partagé en externe et qui approuve les communications externes.

### Plateforme de communication de crise

**Plateforme principale** : [Préciser l'outil — p. ex. Microsoft Teams (avec E2EE), Signal, Wickr, Zoom chiffré, WhatsApp Business]

**Configuration** :

- Chiffrement de bout en bout activé (vérifier que E2EE est actif).
- Groupe de chat de gestion de crise pré-configuré avec tout le personnel autorisé.
- Nom du groupe de chat : **« Équipe de gestion de crise — Sécurisé »**.
- Accès limité au personnel pré-approuvé (pas d'ajouts ad hoc sans approbation du RSSI pendant la crise).

**Plateforme de sauvegarde** (si la plateforme principale est indisponible) : [Préciser l'alternative — p. ex. e-mail chiffré (PGP/S/MIME), pont téléphonique pré-convenu, groupe SMS hors bande]

**Authentification pendant la crise** :

- Tous les participants à la communication de crise doivent s'authentifier avec leurs identifiants organisationnels.
- Pendant une posture d'Urgence, si l'infrastructure MFA est indisponible, les participants doivent utiliser des phrases d'authentification partagées au préalable pour vérifier l'identité (renouvelées mensuellement, distribuées via une liste de contacts hors ligne).

**Vérification hors bande** : Pour les décisions critiques (p. ex. autorisation de la posture d'Urgence, approbation de l'activation du bris de glace), une confirmation verbale par appel téléphonique est requise pour prévenir les attaques d'usurpation d'identité. Numéros de téléphone vérifiés et mis à jour trimestriellement dans la liste de contacts hors ligne.

**Test** : Plateforme de communication de crise testée trimestriellement. Les tests comprennent la vérification de la connectivité, la vérification du statut du chiffrement, l'authentification des participants et la confirmation de livraison des messages. Documentation des tests conservée pendant 3 ans.

**4. Sécurité des tiers**

- Contrôles d'accès des fournisseurs pendant les opérations de reprise.
- Exigences de sécurité des contractants pendant les opérations d'urgence.
- Vérification de la sécurité des services cloud pendant le basculement.
- Sécurité de la chaîne d'approvisionnement pour les achats d'urgence.

### Révision de la sécurité des plans BC/DR

- Le RSSI ou son suppléant désigné doit examiner et approuver les sections sécurité de tous les plans BC/DR avant leur approbation.
- La révision de sécurité doit avoir lieu après chaque mise à jour d'un plan BC/DR.
- Au moins un scénario de test spécifique à la sécurité doit être inclus dans les tests annuels BC/DR.
- Les écarts de sécurité observés pendant les tests doivent être documentés et traités dans les 30 jours.

---

## Sécurité du site de reprise

Les sites de reprise — qu'ils soient en veille active, semi-active, froide ou des environnements de reprise après sinistre basés sur le cloud — doivent maintenir des contrôles de sécurité équivalents au site principal. Un environnement de reprise avec une sécurité plus faible que le site principal crée une lacune exploitable.

| Contrôle | Exigence |
|----------|---------|
| **Sécurité physique** | Équivalente au site principal pour le niveau de criticité des données traitées |
| **Sécurité réseau** | Mêmes règles de segmentation, politiques de pare-feu et surveillance |
| **Contrôle d'accès** | Même modèle d'authentification et d'autorisation ; pas de chemins d'accès plus faibles |
| **Protection des données** | Mêmes normes de chiffrement (au repos et en transit) et application de la classification |
| **Journalisation** | Capacité de journalisation équivalente ; les journaux doivent alimenter le même [SIEM] ou système de surveillance |
| **Durcissement** | Mêmes référentiels de configuration appliqués à l'infrastructure de reprise |

### Définition et configuration du site de reprise

**Site de reprise principal** : [Préciser le type et l'emplacement]

| Option | Description | Configuration |
|--------|-------------|---------------|
| **Reprise après sinistre cloud** (le plus courant pour les PME) | [p. ex. AWS, Azure, Google Cloud] dans [p. ex. eu-central-1 (Francfort), Europe Ouest (Pays-Bas)] | Veille active (toujours disponible), veille semi-active (démarrage en X heures) ou veille froide (déploiement manuel). Déclencheur de basculement : automatique (échec de vérification de santé) ou manuel (déclaré par DSI + RSSI) |
| **Colocation / centre de données secondaire** | [Nom de l'installation, ville] | Lien WAN dédié ou VPN chiffré vers le site principal |
| **Travail à distance** (pandémie/indisponibilité des bureaux) | Accès VPN, MFA, chiffrement des points de terminaison, conseils sur la sécurité du réseau domestique | Fonctions administratives/du travail du savoir uniquement ; dépend du cloud/colocation pour la reprise de l'infrastructure |

**Configuration actuelle** : [Préciser quelle(s) option(s) sont déployée(s)]

**Vérification de l'équivalence de sécurité** :

| Contrôle de sécurité | Méthode de vérification |
|---------------------|------------------------|
| **Sécurité physique** | Révision annuelle des rapports d'audit du prestataire (SOC 2 Type II ou ISO 27001) ; inspection sur site si installation physique |
| **Segmentation réseau** | Configuration du site de reprise comparée au référentiel du site principal |
| **Contrôle d'accès** | Test d'authentification (y compris MFA) sur les systèmes de reprise |
| **Chiffrement** | Analyse de configuration ; vérification des certificats |
| **Journalisation** | Vérifier le transfert des journaux vers [SIEM] pendant le test DR |
| **Protection des sauvegardes** | Test de restauration depuis les sauvegardes du site de reprise |

**Test de basculement** : Test de basculement annuel vers le site de reprise. La validation de sécurité pendant le test doit confirmer que l'authentification fonctionne (y compris MFA), que la segmentation réseau est appliquée, que la journalisation est active et transfère vers [SIEM], que le chiffrement est vérifié et que les contrôles d'accès correspondent au site principal. Les résultats de sécurité sont documentés et remédiés dans les 30 jours.

La sécurité du site de reprise doit être vérifiée :

- Lors du provisionnement initial, avant que le site soit déclaré opérationnel.
- Annuellement, dans le cadre du programme de tests BC/DR.
- Après tout changement significatif de l'infrastructure de reprise.

---

## Procédures d'accès d'urgence

### Accès bris de glace (break-glass)

L'organisation doit maintenir des comptes d'accès d'urgence pré-configurés (comptes « bris de glace ») pour les scénarios où les systèmes normaux d'authentification ou d'accès sont indisponibles.

**Exigences relatives aux comptes bris de glace** :

| Exigence | Spécification |
|----------|---------------|
| **Statut du compte** | Dormant (désactivé) jusqu'à la déclaration d'urgence |
| **Autorité d'activation** | RSSI, DSI ou PDG (chaîne d'autorité documentée avec suppléants désignés) |
| **Authentification** | Authentification forte — identifiants stockés de manière sécurisée selon la spécification ci-dessous |
| **Périmètre** | Prédéfini, limité aux systèmes essentiels à la reprise uniquement |
| **Journalisation** | Toutes les actions journalisées avec piste d'audit protégée contre la falsification |
| **Durée** | Limitée dans le temps — 24 heures par défaut, renouvelable avec nouvelle approbation |
| **Désactivation** | Désactivation formelle avec rotation des identifiants et révision complète des activités |

### Processus d'activation bris de glace

1. **Urgence déclarée** par une autorité autorisée (voir le tableau Autorité de transition).
2. **Demande d'activation documentée** — même si initialement verbale, enregistrement écrit dans les 4 heures.
3. **Activation à deux personnes** — pour les systèmes critiques, le bris de glace requiert un minimum de deux personnes autorisées (double contrôle).
4. **RSSI et Équipe de sécurité notifiés** immédiatement lors de l'activation.
5. **Surveillance renforcée activée** — toute activité du compte bris de glace surveillée en temps réel dans la mesure du possible.
6. **Limite de temps appliquée** — 24 heures par défaut ; le renouvellement nécessite une approbation explicite avec justification.
7. **Désactivation et révision** — lors de la résolution de l'urgence : désactiver le compte, faire pivoter les identifiants, réviser toutes les actions effectuées, documenter les résultats.

### Stockage et accès aux identifiants bris de glace

**Méthode de stockage** : [Préciser la méthode choisie par l'organisation parmi les options ci-dessous]

**Option 1 — Coffre-fort physique** (méthode principale pour les environnements haute sécurité) :

- **Emplacement** : [Nom du bâtiment], [Étage], [Numéro de salle] — salle physiquement sécurisée avec accès restreint.
- **Autorisation d'accès** : PDG, RSSI, DSI (chacun a la combinaison ou la clé du coffre-fort ; deux requis pour l'accès).
- **Contenu** : Enveloppes scellées inviolables contenant les noms d'utilisateur et mots de passe initiaux des comptes bris de glace, les identifiants VPN du site de reprise, les mots de passe racine pour les systèmes critiques (niveau 0) et les clés de récupération de chiffrement.
- **Intégrité des enveloppes** : Sceaux inviolables ; l'ouverture d'une enveloppe déclenche une rotation obligatoire des identifiants.
- **Vérification** : Vérification trimestrielle que le coffre-fort est accessible et que les enveloppes sont intactes (inspection externe uniquement ; pas d'ouverture).

**Option 2 — Coffre-fort d'urgence du gestionnaire de mots de passe** :

- **Outil** : [p. ex. Kit d'urgence 1Password, Accès d'urgence Bitwarden, Accès d'urgence LastPass].
- **Configuration** : Coffre-fort d'urgence séparé du coffre-fort d'entreprise standard.
- **Accès** : Accès d'urgence accordé au personnel désigné (PDG, RSSI, DSI) avec accès à délai (p. ex. délai d'attente de 12 heures avant l'accès accordé).
- **Contournement MFA** : Coffre-fort d'urgence accessible avec des codes de récupération stockés hors ligne (cartes imprimées dans des enveloppes scellées, stockées selon l'Option 1).
- **Test** : Test trimestriel du flux d'accès d'urgence (vérification du délai, confirmation d'accès, récupération des identifiants).

**Option 3 — Connaissance partagée / partage de secret** (avancé) :

- **Méthode** : Partage de secret de Shamir ou similaire cryptographique.
- **Configuration** : Mot de passe bris de glace divisé en 3 parts ; 2 parts sur 3 requises pour la reconstruction.
- **Détenteurs de parts** : PDG (Part 1), RSSI (Part 2), DSI (Part 3).
- **Stockage** : Chaque détenteur stocke sa part dans un coffre-fort personnel ou une enveloppe scellée (coffre-fort personnel, coffre bancaire).
- **Test** : Test annuel du processus de reconstruction.

**Méthode actuelle** : [Préciser quelle(s) option(s) l'organisation utilise]

**Accès de sauvegarde** (si la méthode principale échoue) : Si le coffre-fort est inaccessible (bâtiment détruit) → Coffre-fort d'urgence du gestionnaire de mots de passe (accessible depuis le cloud). Si le gestionnaire de mots de passe est inaccessible (panne du service) → Coffre-fort physique ou connaissance partagée.

### Test du bris de glace

Les comptes et procédures bris de glace doivent être testés au moins annuellement pour vérifier :

- Les identifiants sont accessibles et fonctionnels.
- Le processus d'activation est compris par tout le personnel autorisé.
- La journalisation capture toutes les actions effectuées.
- Le processus de désactivation fonctionne correctement.

Les résultats des tests doivent être documentés. Les tests échoués déclenchent une remédiation immédiate.

---

## Disponibilité du personnel

L'organisation doit garantir que le personnel ayant des responsabilités de sécurité est disponible pendant les événements perturbateurs. Les perturbations se produisent fréquemment en dehors des heures de bureau et peuvent empêcher l'accès normal au lieu de travail.

**Exigences de continuité de l'équipe sécurité** :

- Les rôles clés de sécurité doivent avoir des suppléants désignés documentés dans un plan de succession.
- Les coordonnées du personnel de sécurité doivent être maintenues hors ligne — listes de contacts imprimées et/ou USB chiffré — accessibles lorsque les e-mails, l'intranet et les autres systèmes numériques sont indisponibles.
- Dans la mesure du possible, le personnel de sécurité devrait être géographiquement distribué pour éviter qu'une défaillance sur un seul site désactive toute l'équipe de sécurité.
- La formation croisée doit garantir qu'au moins deux individus peuvent effectuer chaque fonction de sécurité critique (activation du bris de glace, révision des journaux, révocation des accès d'urgence, évaluation de la posture de sécurité).
- Une rotation d'astreinte doit être établie pour une couverture 24h/24, 7j/7 lorsque l'organisation opère aux niveaux de posture Élevé, Dégradé ou Urgence.

### Liste de contacts accessible hors ligne

**Approche multi-couches pour la résilience** :

**Couche 1 — Cartes plastifiées imprimées** :

- Cartes plastifiées de la taille d'un portefeuille remises à tous les membres de l'équipe de gestion de crise et au personnel de sécurité.
- Contient : Noms, numéros de téléphone mobile, adresses e-mail personnelles (pour contact hors bande), rôle.
- Mise à jour trimestrielle ; anciennes cartes détruites (déchiquetées). Distribution : Remise en mains propres ; le personnel signe un accusé de réception.

**Couche 2 — Clé USB chiffrée** :

- Clé USB stockée dans le coffre-fort bris de glace avec les identifiants.
- Contient : Liste de contacts complète (tout le personnel de sécurité, équipe de crise élargie, contacts d'urgence des fournisseurs).
- Fichier chiffré (p. ex. VeraCrypt, BitLocker To Go) avec mot de passe connu du PDG/RSSI/DSI.
- Mise à jour trimestrielle.

**Couche 3 — Stockage cloud sécurisé** (accessible si Internet disponible) :

- Liste de contacts stockée dans [référentiel de documents sécurisé] avec accès limité à l'équipe de gestion de crise.
- Régulièrement mise à jour (en temps réel lors des changements de personnel).

**Test** : Vérification trimestrielle — 3 personnes aléatoires contactées en utilisant les informations des cartes plastifiées (vérifier que les numéros de téléphone fonctionnent), clé USB testée (mot de passe de chiffrement vérifié, fichier ouvert), accès au stockage cloud vérifié. Résultats documentés ; les échecs déclenchent une mise à jour immédiate.

### Couverture d'astreinte de l'équipe sécurité

**Déclencheur d'activation** : Activé automatiquement lorsque la posture de sécurité passe à **Élevée**, **Dégradée** ou **Urgence**.

**Modèle de couverture** :

| Posture | Couverture |
|---------|-----------|
| **Normal** | Pas d'astreinte dédiée (support aux heures de bureau uniquement) |
| **Élevé** | Couverture 16h/7 (07:00–23:00 CET, 7 jours/semaine) |
| **Dégradé / Urgence** | Couverture 24h/24, 7j/7 |

**Planning de rotation** :

| Rôle | Responsabilité de couverture |
|------|------------------------------|
| **Astreinte principal** | Analyste en sécurité IT ou Responsable de la sécurité IT (rotation hebdomadaire) |
| **Astreinte de sauvegarde** | RSSI ou membre désigné de l'équipe sécurité |
| **Escalade** | RSSI (joignable 24h/24, 7j/7 pendant Dégradé/Urgence) |

**SLA de réponse** :

| Gravité | Élevé | Dégradé / Urgence |
|---------|-------|-------------------|
| **Critique** (activation bris de glace, violation confirmée) | 30 minutes | 15 minutes |
| **Élevé** (défaillance de contrôle de sécurité, activité suspecte) | 2 heures | 1 heure |
| **Moyen** (alerte non critique, avis) | 4 heures | 2 heures |

**Chemin d'escalade** : Astreinte principal → Astreinte de sauvegarde (si le principal est injoignable après 30 min pour Critique, 1 heure pour Élevé) → RSSI → Direction générale.

**Test** : Page de test d'astreinte mensuelle pendant les heures normales de bureau (vérifier les coordonnées et le délai de réponse). Test trimestriel en dehors des heures de bureau (heure aléatoire ; vérifier le fonctionnement du chemin d'escalade).

---

## Validation de sécurité post-perturbation

Avant de revenir au niveau de posture Normal, l'organisation doit valider que les contrôles de sécurité complets ont été restaurés. La transition reprise-normal n'est pas complète jusqu'à la validation de sécurité signée par le RSSI.

### Validation en quatre phases

| Phase | Calendrier | Activités de validation |
|-------|-----------|------------------------|
| **Immédiat** | 0–24 heures post-perturbation | Vérifier que les contrôles non négociables sont opérationnels ; désactiver tous les comptes bris de glace ; réviser les journaux pour les anomalies pendant la perturbation ; confirmer qu'aucun accès non autorisé ne s'est produit |
| **Court terme** | 1–7 jours | Validation complète des contrôles de sécurité ; analyse de vulnérabilités de tous les systèmes de niveau 1 et 2 ; révision des accès (vérifier qu'il n'y a pas de permissions d'urgence résiduelles) ; analyse initiale de l'incident |
| **Moyen terme** | 1–4 semaines | Remédiation de la dette de sécurité (appliquer les correctifs différés, restaurer les contrôles différés) ; recertification complète des accès ; test des contrôles pour vérifier l'efficacité ; mise à jour du plan BC/DR avec les enseignements tirés |
| **Long terme** | 1–3 mois | Mise en œuvre des enseignements tirés ; mises à jour des politiques et procédures ; mises à jour de la formation ; analyse des tendances de la posture de sécurité pendant la perturbation |

### Suivi de la dette de sécurité

Tous les assouplissements de sécurité approuvés pendant une perturbation doivent être suivis dans le Registre de la dette de sécurité jusqu'à leur remédiation complète.

**Système** : [Préciser l'outil — p. ex. plateforme GRC (Vanta, Drata, ServiceNow GRC), Jira, Asana, registre Excel stocké en lieu sûr]

**Responsabilité** : Le RSSI maintient le registre ; les responsables assignés remédient les éléments individuels de dette.

**Format du Registre de la dette de sécurité** :

| Champ | Description |
|-------|-------------|
| **Identifiant de dette** | Identifiant unique (p. ex. DETTE-2025-001) |
| **Contrôle assoupli** | Quel contrôle de sécurité a été dégradé ou différé |
| **Justification métier** | Pourquoi l'assouplissement était-il nécessaire ? (lié à un événement perturbateur spécifique) |
| **Mesure compensatoire** | Mesure de sécurité alternative mise en œuvre |
| **Date d'ouverture** | Quand l'assouplissement a été approuvé |
| **Posture de sécurité à l'ouverture** | Élevé / Dégradé / Urgence |
| **Approbateur** | RSSI ou délégué autorisé |
| **Responsable** | Personne responsable de la remédiation |
| **Date cible de clôture** | Quand le contrôle complet doit être restauré |
| **Statut actuel** | Ouvert / En cours / Clôturé |
| **Notes de progression** | Mises à jour sur les actions de remédiation |
| **Date de clôture** | Quand le contrôle a été entièrement restauré |
| **Vérification de clôture** | Vérification par le RSSI ou l'Équipe de sécurité de la restauration du contrôle |

**Cycle de vie de la dette** :

1. **Ouverture** : Assouplissement du contrôle approuvé pendant la perturbation → entrée immédiate dans le registre.
2. **Suivi** : Révision hebdomadaire pendant la perturbation active ; bimensuelle pendant la posture Reprise.
3. **Escalade** : Selon les seuils ci-dessous.
4. **Clôture** : Contrôle entièrement restauré → Équipe de sécurité vérifie → Dette marquée Clôturée.

**Intégration avec la posture de sécurité** : La transition Reprise → Normal nécessite que le Registre de la dette de sécurité soit vide ou dispose d'une approbation documentée de la direction générale pour les éléments restants.

**Reporting** : Statut de la dette de sécurité rapporté dans chaque Révision de management SMSI pendant et après la perturbation. Indicateurs : total des dettes ouvertes, âge moyen, dettes en retard, taux de clôture.

**Seuils d'escalade** :

- La dette de sécurité de plus de **30 jours** doit être escaladée au RSSI avec un plan de remédiation et une date cible révisée.
- La dette de sécurité de plus de **90 jours** doit être escaladée à la direction générale pour une décision : soit approuver une remédiation accélérée avec des ressources supplémentaires, soit accepter formellement le risque résiduel avec une acceptation du risque documentée.
- La dette de sécurité qui ne peut pas être remédiée doit être convertie en entrée permanente de risque dans le Registre des risques avec des mesures compensatoires et une révision annuelle.

---

## Rôles et responsabilités

| Rôle | Responsabilités liées à la sécurité de l'information lors d'une perturbation |
|------|----------------------------------------------------------------------------|
| **PDG / Direction générale** | Approuver les niveaux de posture de sécurité ; autoriser le mode Urgence ; allouer des ressources pour la sécurité pendant la reprise ; prendre des décisions d'acceptation des risques pour la dette de sécurité dépassant 90 jours |
| **RSSI** | Propriétaire de la politique ; définir les exigences de sécurité pour les plans BC/DR ; approuver les transitions de posture de sécurité ; autoriser l'activation du bris de glace ; posséder la validation de sécurité post-perturbation ; point d'escalade pour la dette de sécurité |
| **Coordinateur BC/DR** | Intégrer les exigences de sécurité dans les plans BC/DR ; coordonner avec le RSSI sur la révision de sécurité des plans ; inclure des scénarios de sécurité dans les tests BC/DR |
| **DSI** | Garantir que la reprise IT s'aligne sur les exigences de sécurité ; co-autoriser la transition Élevé → Dégradé ; autoriser l'activation du bris de glace |
| **Équipe sécurité / Sécurité IT** | Surveiller la sécurité pendant la perturbation ; activer et désactiver les procédures d'urgence ; valider la sécurité du site de reprise ; effectuer des analyses de vulnérabilités et des révisions des accès post-perturbation |
| **Équipe de gestion de crise** | Inclure les considérations de sécurité dans toutes les décisions de crise ; maintenir la communication avec le RSSI tout au long de la perturbation |
| **Opérations IT** | Mettre en œuvre les contrôles de sécurité dans les environnements de reprise ; maintenir la journalisation pendant la reprise ; signaler les anomalies de sécurité pendant la reprise |
| **Tout le personnel** | Suivre les procédures de sécurité pendant la perturbation ; signaler les préoccupations de sécurité via les canaux établis ; ne pas contourner les contrôles de sécurité sans autorisation |

### Composition de l'équipe de gestion de crise

**Objet** : Coordonner la réponse organisationnelle aux perturbations majeures affectant les opérations métier et la sécurité de l'information.

**Déclencheur d'activation** : Transition de la posture de sécurité vers **Dégradé** ou **Urgence** ; incident de gravité P0 (Critique) ou P1 (Élevé) avec impact à l'échelle de l'organisation ; ou déclaration du PDG, DSI ou RSSI que la gestion de crise est requise.

**Membres de l'équipe principale** :

| Rôle | Responsabilités pendant la crise |
|------|----------------------------------|
| **PDG** (Chef d'équipe) | Leadership général de la crise ; communication externe ; décisions stratégiques ; autoriser la posture d'Urgence |
| **DSI** | Coordination de la reprise IT ; allocation des ressources ; autorité de décision technologique |
| **RSSI** | Continuité de la sécurité de l'information ; gestion de la posture de sécurité ; autorisation bris de glace ; validation post-perturbation |
| **DAF** | Évaluation de l'impact financier ; autorisation budgétaire pour la reprise ; coordination de l'assurance |
| **Directeur RH** | Sécurité du personnel ; communication aux employés ; continuité de la main-d'œuvre |
| **Conseiller juridique** | Notification réglementaire ; gestion de la responsabilité ; problèmes contractuels ; obligations légales liées aux violations de données |
| **Communications / Relations publiques** (le cas échéant) | Communications externes ; gestion des médias ; notification des clients |

**Équipe élargie** (activée selon les besoins) : Coordinateur BC/DR, Responsable des opérations IT, Responsable de l'équipe sécurité, Responsable des installations, fournisseurs clés.

**Autorité décisionnelle** :

| Type de décision | Autorité |
|-----------------|---------|
| Transitions de niveau de posture de sécurité | Accord du PDG + DSI + RSSI requis |
| Décisions d'acceptation des risques, communications externes, allocation de ressources au-delà du budget | Autorité finale du PDG |
| Assouplissements des contrôles de sécurité, activation du bris de glace, approbation de la dette de sécurité | Autorité finale du RSSI |
| Priorités de reprise technologique, séquencement de la restauration des systèmes | Autorité finale du DSI |

**Cadence des réunions pendant la crise** :

| Posture | Fréquence |
|---------|-----------|
| **Dégradé** | Appel quotidien de l'équipe de gestion de crise (30 minutes) jusqu'au début de la reprise |
| **Urgence** | Deux fois par jour (matin et soir) plus ad hoc selon les besoins |
| **Reprise** | Tous les 2–3 jours jusqu'au retour à Normal |

Comptes rendus de réunion documentés (même brièvement) pour la révision post-incident. Plans d'action suivis avec responsable et date cible.

**Post-crise** : Session formelle d'enseignements tirés dans les 30 jours suivant le retour à la posture Normale. Les enseignements tirés éclairent les mises à jour de politique, les mises à jour du plan BC/DR et la formation.

---

## Preuves

Les preuves suivantes démontrent la conformité à cette politique :

| # | Preuve | Responsable | Fréquence |
|---|--------|-------------|-----------|
| 1 | **Plans BC/DR avec approbation de sécurité du RSSI** (révision signée confirmant l'adéquation des sections sécurité) | Coordinateur BC/DR / RSSI | *Révision annuelle ; mise à jour après tests et incidents ; 2 versions précédentes conservées* |
| 2 | **Documentation du référentiel de sécurité minimal** (définissant les contrôles non négociables et les seuils du mode dégradé) | RSSI | *Révision annuelle ; mise à jour lors d'un changement de politique ; conservée 3 ans* |
| 3 | **Inventaire des comptes bris de glace** (liste des comptes, périmètre, emplacement du stockage des identifiants, autorité d'activation) | Équipe sécurité | *Maintenu en continu ; révisé trimestriellement ; conservé 3 ans* |
| 4 | **Résultats des tests bris de glace** (test annuel documentant l'accessibilité des identifiants, le processus d'activation, la journalisation, la désactivation) | Équipe sécurité | *Annuel au minimum ; conservé 3 ans* |
| 5 | **Enregistrements des transitions de posture de sécurité** (date, autorité, justification, contrôles affectés) — si des perturbations se sont produites | RSSI | *Par événement ; conservé 5 ans* |
| 6 | **Registre de la dette de sécurité** (tous les assouplissements pendant la perturbation avec responsable, mesures compensatoires, date cible, clôture) | RSSI | *Par événement ; révisé mensuellement pendant la dette active ; conservé 3 ans* |
| 7 | **Rapports de validation de sécurité post-perturbation** (réalisation de la liste de contrôle en quatre phases avec signature) — si des perturbations se sont produites | RSSI / Équipe sécurité | *Par événement perturbateur ; conservé 5 ans* |
| 8 | **Évaluation de la sécurité du site de reprise** (vérification annuelle de l'équivalence de sécurité avec le site principal) | Équipe sécurité | *Annuel ; conservé 3 ans* |
| 9 | **Liste de contacts du personnel sécurité et plan de succession** (accessible hors ligne, testée trimestriellement) | RSSI | *Révisée trimestriellement ; mise à jour lors de tout changement* |
| 10 | **Enregistrements des tests BC/DR montrant des scénarios spécifiques à la sécurité** (périmètre du test, résultats de sécurité, actions correctives) | Coordinateur BC/DR / Équipe sécurité | *Annuel au minimum ; conservé 3 ans* |

---

# Conformité à la politique

## Mesure de la conformité

L'équipe de management de la sécurité de l'information vérifiera la conformité à cette politique par diverses méthodes, notamment, sans s'y limiter, les révisions de sécurité des plans BC/DR, les tests des comptes bris de glace, les enregistrements de transitions de posture de sécurité, le statut du Registre de la dette de sécurité, les évaluations du site de reprise, les audits internes et externes, ainsi que les retours d'information au propriétaire de la politique.

**Indicateurs de gouvernance** (rapportés à la direction générale au moins annuellement) :

| Indicateur | Objectif |
|-----------|---------|
| Plans BC/DR avec approbation de sécurité RSSI en cours | 100 % |
| Tests des comptes bris de glace réalisés dans les délais | 100 % |
| Incidents de sécurité pendant les événements perturbateurs | Suivi des tendances (objectif : décroissant) |
| Éléments de dette de sécurité ouverts depuis plus de 90 jours | 0 |
| Évaluations du site de reprise sans résultats critiques/élevés | 100 % |

## Exceptions

Toute exception à cette politique doit être approuvée et enregistrée à l'avance par le RSSI, avec une acceptation du risque documentée, des mesures compensatoires et une date de révision définie (durée maximale de la perturbation + 7 jours pour les exceptions de reprise ; 12 mois maximum pour les exceptions permanentes). Les exceptions doivent être rapportées à l'Équipe de révision de la direction.

Les exceptions ne sont pas permises pour les contrôles non négociables (contrôle d'accès, chiffrement des données, journalisation, segmentation réseau, protection des sauvegardes). Les exceptions éliminant la capacité de piste d'audit ne sont pas permises.

## Non-conformité

Un employé reconnu coupable d'avoir violé cette politique peut faire l'objet de mesures disciplinaires pouvant aller jusqu'au licenciement.

## Amélioration continue

Cette politique est révisée et mise à jour dans le cadre du processus d'amélioration continue. Les révisions doivent prendre en compte les enseignements tirés des perturbations réelles, les résultats des tests BC/DR, les évolutions du paysage des menaces, les mises à jour réglementaires, les résultats des audits et les meilleures pratiques émergentes pour la sécurité dans des conditions défavorables.

---

# Domaines de la norme ISO 27001 couverts

Politique de sécurité de l'information lors d'une perturbation — Cartographie des contrôles ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership et engagement | 5.1 Politiques de sécurité de l'information |
| Clause 5.2 Politique | 5.4 Responsabilités de la direction |
| Clause 6.2 Objectifs de sécurité de l'information | **5.29 Sécurité de l'information lors d'une perturbation** |
| Clause 7.3 Sensibilisation | 5.30 Préparation TIC pour la continuité d'activité |
| Clause 8.1 Planification et contrôle opérationnels | 5.36 Conformité aux politiques, règles et normes |
| | 6.3 Sensibilisation, éducation et formation à la sécurité de l'information |
| | 6.4 Processus disciplinaire |
| | 8.13 Sauvegarde des informations |
| | 8.14 Redondance des installations de traitement de l'information |

**Cadre réglementaire et légal** :

| Cadre | Pertinence |
|-------|-----------|
| nLPD suisse (revDSG) | Art. 8 — Maintenir des mesures de sécurité techniques et organisationnelles appropriées, y compris pendant les perturbations |
| OPDo suisse (Ordonnance sur la protection des données) | Art. 1–3 — Exigences minimales en matière de sécurité des données |
| RGPD de l'UE (le cas échéant) | Art. 32 — Sécurité du traitement, y compris la capacité à garantir la confidentialité, l'intégrité, la disponibilité et la résilience continues des systèmes et services de traitement |
| ISO/IEC 27001:2022 | Contrôle Annexe A 5.29 — Sécurité de l'information lors d'une perturbation |
| ISO/IEC 27002:2022 | Section 5.29 — Lignes directrices de mise en œuvre |
| ISO/IEC 22301 | Systèmes de management de la continuité d'activité (référence informative) |
| NIST SP 800-34 Rev 1 | Guide de planification des mesures d'urgence — approche en trois phases (notification/activation, reprise, reconstitution) (référence informative) |
| CIS Controls v8 | Contrôle 17 (Gestion de la réponse aux incidents), Contrôle 11 (Reprise des données) |
| DORA (conditionnel) | Art. 11 — Gestion de la continuité d'activité TIC incluant les exigences de sécurité pendant les perturbations |
| NIS2 (conditionnel) | Art. 21 — Mesures de continuité d'activité et de gestion de crise |
| FINMA (conditionnel) | Circulaire 2023/1 — Résilience opérationnelle pour les établissements financiers suisses réglementés |

---

<!-- QA_VERIFIED: 2026-03-29 -->
