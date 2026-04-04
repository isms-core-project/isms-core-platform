<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.6.7-8-FR:operational:OP-POL:a.6.7-8 -->
**ISMS-OP-POL-A.6.7-8 — Télétravail et signalement des événements de sécurité**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Télétravail et signalement des événements de sécurité |
| **Type de document** | Politique opérationnelle |
| **Identifiant du document** | ISMS-OP-POL-A.6.7-8 |
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

- ISO/IEC 27001:2022 Contrôle A.6.7 — Télétravail
- ISO/IEC 27001:2022 Contrôle A.6.8 — Signalement des événements de sécurité de l'information
- ISO/IEC 27002:2022 Sections 6.7, 6.8 — Lignes directrices de mise en œuvre

**Contrôles Annexe A connexes** :

| Contrôle | Relation avec le télétravail et le signalement des événements |
|----------|--------------------------------------------------------------|
| A.5.10 Utilisation acceptable des informations et des actifs associés | Définit l'utilisation acceptable des appareils et des informations dans le cadre du télétravail |
| A.5.11 Restitution des actifs | Restitution des équipements à la fin du télétravail ou de l'emploi |
| A.5.14 Transfert des informations | Exigences de transfert sécurisé pour les données envoyées depuis des emplacements distants |
| A.5.24-28 Cycle de vie de la gestion des incidents | Chemin d'escalade lorsque les événements signalés sont confirmés comme incidents |
| A.6.3 Sensibilisation et formation à la sécurité de l'information | Formation sur la sécurité du télétravail et les procédures de signalement |
| A.8.1 Appareils de point de terminaison utilisateur | Niveaux de sécurité de base pour les points de terminaison distants et mobiles |
| A.8.5 Authentification sécurisée | Exigences MFA et d'authentification pour l'accès distant |

**Politiques internes connexes** :

- Politique de contrôle d'accès
- Politique de sécurité des points de terminaison
- Politique de gestion des incidents
- Politique de classification et de traitement des informations
- Politique de transfert des informations
- Politique d'utilisation acceptable et de restitution des actifs

---

# Politique de télétravail et de signalement des événements de sécurité

## Objectif

La présente politique établit les exigences de l'organisation en matière de télétravail sécurisé et de signalement en temps opportun des événements de sécurité de l'information. Elle définit les mesures de sécurité requises lorsque le personnel travaille en dehors des locaux de l'organisation, et fournit un mécanisme structuré permettant à l'ensemble du personnel de signaler les événements de sécurité observés ou suspectés par les canaux appropriés.

La présente politique soutient la nLPD suisse (nFADP/revDSG) art. 8 en mettant en œuvre des mesures techniques et organisationnelles appropriées aux risques pour protéger les données personnelles (y compris les données personnelles sensibles) dans les environnements de télétravail. Lorsque l'organisation traite des données de personnes situées dans l'UE/EEE, les exigences du RGPD s'appliquent également.

Ces deux contrôles sont combinés parce que les télétravailleurs constituent la première ligne de détection des événements, qu'ils font face à des menaces absentes dans les environnements de bureau, et qu'ISO 27002:2022 exige explicitement que les procédures de signalement des incidents soient accessibles depuis les emplacements distants.

## Champ d'application

Tous les employés et utilisateurs tiers.

Tous les appareils d'entreprise et personnels utilisés pour accéder à, traiter ou stocker des informations organisationnelles à distance.

Tous les arrangements de télétravail incluant le travail depuis le domicile, les espaces de coworking, les locaux de clients et lors des déplacements professionnels.

Tout le personnel responsable du signalement des événements de sécurité, quel que soit le lieu de travail.

## Principe

Le télétravail devrait faire l'objet d'une autorisation formelle et être soumis à des contrôles de sécurité proportionnels à la classification des informations auxquelles il est accédé. Tout le personnel devrait signaler promptement les événements de sécurité de l'information observés ou suspectés, par les canaux désignés. L'organisation favorise une culture sans blâme où le signalement de bonne foi est protégé et encouragé.

---

# Partie 1 — Télétravail (A.6.7)

## Autorisation du télétravail

Tous les arrangements de télétravail réguliers devront faire l'objet d'une approbation formelle avant leur commencement.

- **Autorité d'approbation** : Le responsable hiérarchique autorise l'arrangement de télétravail ; la Sécurité informatique approuve l'accès technique.
- **Évaluation des risques** : Une évaluation des risques devra être réalisée pour les rôles traitant des données Confidentielles ou Restreintes à distance. L'évaluation devra porter au minimum sur : (a) le niveau de classification des données accédées à distance ; (b) la capacité de sécurité physique du lieu de télétravail ; (c) la posture de sécurité réseau du site distant ; (d) la conformité de l'appareil au niveau de sécurité de base ; et (e) toute restriction réglementaire ou contractuelle.
- **Accusé de réception documenté** : Les télétravailleurs devront signer un accusé de réception confirmant qu'ils comprennent et acceptent les exigences de sécurité de la présente politique.
- **Révision annuelle** : Toutes les autorisations de télétravail devront être révisées au moins annuellement. Les révisions devront confirmer que l'autorisation reste appropriée, que les exigences de sécurité sont maintenues, et que tout changement de rôle, d'accès aux données ou de lieu de travail est reflété.

**Approbation du lieu** :
- **Lieux de télétravail standard** (bureau à domicile en Suisse, espace de travail distant établi) : Approbation du responsable hiérarchique suffisante.
- **Télétravail international** (travail depuis l'extérieur de la Suisse) : Nécessite l'approbation du RSSI + approbation des RH + avis juridique (implications fiscales, droit du travail, résidence des données).
- **Télétravail temporaire depuis des emplacements à haut risque** (espaces de coworking publics, cafés, déplacements) : Requiert la connaissance du responsable hiérarchique ; l'accès aux données Confidentielles depuis des lieux publics est interdit.

**Changements de lieu** : Les changements permanents du lieu de télétravail (p. ex., déménagement dans un nouveau domicile, déplacement prolongé) devront être signalés au responsable hiérarchique et à la Sécurité informatique dans les **14 jours**.

**Révocation** : L'autorisation de télétravail devra être révoquée lorsque l'emploi ou le contrat prend fin, lorsque le rôle évolue vers un rôle inadapté au télétravail, lorsque les exigences de sécurité ne sont plus maintenues, en cas de violations de la politique, ou lorsque les besoins de l'entreprise nécessitent une présence sur site.

## Enregistrement et responsabilités des appareils mobiles

Les appareils mobiles émis ou approuvés pour le télétravail devront être enregistrés dans le registre des actifs et affectés à un individu nommément désigné.

**Exigences d'enregistrement des appareils** :

- Tous les appareils mobiles (appareils d'entreprise et AVEC approuvés) devront être enregistrés dans le registre des actifs avec le propriétaire affecté, le type d'appareil, le numéro de série et l'usage prévu.
- Les propriétaires affectés devront recevoir une copie de la présente politique et être informés de leurs responsabilités.
- Les appareils devront disposer d'un chiffrement approprié, d'une protection antivirus/des points de terminaison et de contrôles d'accès installés.

**Responsabilités du propriétaire affecté** :

- Veiller à ce que les correctifs du système d'exploitation et des applications soient appliqués rapidement.
- Veiller à ce que le chiffrement et la protection des points de terminaison restent activés et à jour.
- Ne pas laisser l'appareil sans surveillance ; sécuriser physiquement l'appareil lorsqu'il n'est pas utilisé.
- Accéder uniquement aux informations organisationnelles requises pour son rôle, conformément à la Politique de contrôle d'accès.
- Ne pas installer de logiciels ou effectuer des modifications qui violeraient les politiques de sécurité de l'information, les réglementations ou la législation applicable de l'organisation.
- Ne pas permettre à d'autres personnes, y compris les membres de la famille, d'accéder à l'appareil affecté ou de l'utiliser.
- Ne pas stocker de données personnelles ou de données personnelles sensibles (au sens de la nLPD) sur l'appareil, sauf si cela est autorisé et consigné dans le registre des actifs.
- Restituer l'appareil mobile lorsqu'il n'est plus nécessaire, sur demande, ou lors du départ de l'organisation.

## Effacement à distance et sauvegarde

- **Effacement à distance** : Tous les appareils mobiles d'entreprise devront disposer d'une capacité d'effacement à distance activée avant que l'appareil ne soit remis à l'utilisateur. Un verrouillage automatique devra être activé (maximum 5 tentatives d'authentification échouées).
- **Sauvegarde** : Les appareils mobiles ne sont pas sauvegardés par défaut dans les solutions de sauvegarde d'entreprise. Les utilisateurs devront stocker les fichiers de travail dans des emplacements cloud ou réseau approuvés (p. ex., SharePoint, OneDrive Entreprise, serveur de fichiers approuvé). Les données de travail critiques ne devront pas résider uniquement sur le stockage local de l'appareil.

## Sécurité physique

Les télétravailleurs devront maintenir une sécurité physique appropriée à la classification des informations traitées :

- **Positionnement de l'écran** : Positionner les écrans de manière à éviter une visualisation non autorisée par d'autres personnes dans l'espace de travail.
- **Filtres de confidentialité** : Utiliser des filtres de confidentialité lors du travail dans des espaces partagés ou publics (espaces de coworking, cafés, transports en commun).
- **Sécurité des équipements** : Sécuriser les équipements de travail lorsque l'espace de travail est sans surveillance. Ne jamais laisser les appareils sans surveillance dans les espaces publics. Verrouiller les appareils en cas d'absence, même brève.
- **Bureau propre** : La politique de bureau propre (A.7.7 — voir Politique de sécurité physique et environnementale) s'étend aux environnements de télétravail. Les documents sensibles ne devront pas être laissés visibles lorsqu'ils ne sont pas activement utilisés. Les documents de travail devront être sécurisés à la fin de chaque session de travail.

  **Exigences de bureau propre pour le télétravail** :
  - Documents verrouillés dans un tiroir, un classeur ou un bureau à domicile sécurisé lorsqu'ils ne sont pas utilisés.
  - Écrans verrouillés lors de toute absence (Windows+L, Ctrl+Cmd+Q).
  - Aucun document de travail laissé sur des tables de cuisine, dans des pièces communes ou dans d'autres espaces familiaux partagés.
- **Élimination des documents** : Les documents sensibles devront être éliminés selon des méthodes approuvées (déchiquetage). Lorsqu'un déchiqueteur n'est pas disponible sur le lieu de télétravail, les documents sensibles devront être retournés au bureau pour une élimination sécurisée.
- **Accès des membres de la famille et des visiteurs** : Empêcher l'accès aux appareils et documents de travail par les membres de la famille, les visiteurs ou d'autres personnes non autorisées.

## Sécurité technique

Les contrôles de sécurité technique suivants devront s'appliquer à tous les accès distants :

- **VPN ou Zéro confiance** : Toutes les connexions aux ressources organisationnelles internes devront utiliser un VPN ou une architecture Zéro confiance équivalente. La tunnelisation fractionnée peut être autorisée uniquement lorsqu'une évaluation des risques démontre un risque résiduel acceptable et que toutes les ressources organisationnelles sont accédées via le tunnel chiffré.

  **Mise en œuvre actuelle** : [Préciser : p. ex., « Cisco AnyConnect VPN », « Palo Alto GlobalProtect », « Zéro confiance via Cloudflare Access / Zscaler », ou « Sélection en cours ; provisoire : VPN requis »]

  **Exigences VPN/Zéro confiance** :
  - Imposer le MFA avant d'établir la connexion.
  - Imposer une vérification de conformité de l'appareil (chiffrement, correctifs, protection des points de terminaison) avant l'accès.
  - Terminer les sessions après une période d'inactivité définie (conformément aux exigences de délai d'expiration des sessions ci-dessous).
  - Consigner toutes les tentatives de connexion (réussies et échouées).
- **Authentification multifacteur (MFA)** : Le MFA devra être requis pour tout accès distant aux systèmes organisationnels. Cela inclut les connexions VPN, les services cloud, la messagerie électronique et tout système contenant des données INTERNES, Confidentielles ou Restreintes.
- **Chiffrement en transit** : Toutes les données transmises entre les points de terminaison distants et les systèmes organisationnels devront être chiffrées en utilisant TLS 1.2 au minimum (TLS 1.3 préféré).
- **Sécurité Wi-Fi** : Les télétravailleurs devront utiliser uniquement des réseaux sans fil sécurisés et chiffrés (WPA2 minimum, WPA3 préféré).

  **Utilisation du Wi-Fi public** :
  - **Interdit sans VPN** : Le Wi-Fi public non sécurisé (aéroports, hôtels, cafés) ne devra pas être utilisé pour le travail organisationnel sans protection VPN.
  - **Avec VPN** : Le Wi-Fi public peut être utilisé avec une connexion VPN active pour l'accès aux données INTERNES uniquement.
  - **Données Confidentielles** : L'accès aux données Confidentielles via le Wi-Fi public est déconseillé même avec VPN ; utiliser un point d'accès cellulaire ou un réseau de confiance dans la mesure du possible.
  - **Activités interdites sur le Wi-Fi public** (même avec VPN) : Transactions financières, changements de mot de passe pour les comptes critiques (utiliser les données cellulaires ou un réseau de confiance).

  **Sécurité du réseau domestique** : Les télétravailleurs devraient sécuriser leurs réseaux domestiques (modifier le mot de passe par défaut du routeur, activer WPA3/WPA2, désactiver le WPS, appliquer les mises à jour du micrologiciel du routeur).
- **Délai d'expiration des sessions** : Les sessions d'accès distant devront être configurées pour se déconnecter après une période d'inactivité définie (maximum 15 minutes pour les systèmes traitant des données Confidentielles ou Restreintes ; maximum 30 minutes pour les autres systèmes).

## Traitement des données

Les télétravailleurs devront traiter les données conformément à leur niveau de classification selon la Politique de classification et de traitement des informations :

| Classification des données | Stockage distant autorisé | Conditions |
|---------------------------|--------------------------|------------|
| **Public** | Oui | Sécurité standard de l'appareil |
| **INTERNE** | Oui | Appareil chiffré requis |
| **Confidentiel** | Conditionnel | Appareil chiffré, emplacement de stockage approuvé, approbation du responsable hiérarchique |
| **Restreint** | Non (par défaut) | Nécessite l'approbation explicite du RSSI avec des mesures compensatoires documentées |

Les télétravailleurs devront respecter la Politique de transfert des informations lors de l'envoi ou de la réception de données organisationnelles depuis des emplacements distants. Les données organisationnelles ne devront pas être transférées vers des services de stockage cloud personnels, des comptes de messagerie personnels ou des services de partage de fichiers non approuvés.

## Exigences pour les appareils d'entreprise et AVEC

### Appareils d'entreprise

Les appareils fournis par l'entreprise utilisés pour le télétravail devront :

- Être configurés conformément au niveau de sécurité de base organisationnel.
- Disposer d'un chiffrement intégral du disque (CID) activé.
- Avoir un logiciel de protection des points de terminaison actuel installé et actif.
- Être corrigés et mis à jour conformément au calendrier de correctifs organisationnel.
- Disposer d'une capacité d'effacement à distance activée.
- Être enregistrés dans l'inventaire des appareils.

### AVEC (Apportez votre équipement personnel de communication)

L'organisation n'a pas pour politique d'autoriser par défaut l'utilisation d'appareils mobiles personnels pour le travail. Une autorisation est requise de la part de l'équipe de management de la sécurité de l'information.

**Critères d'approbation AVEC** :
- Justification métier (besoin temporaire, exigence du rôle, réduction des coûts).
- L'appareil répond aux exigences minimales de sécurité (OS actuel, compatible MDM, non débridé/rooté).
- Classification des données : AVEC autorisé uniquement pour les données INTERNES et Publiques ; les données Confidentielles nécessitent une approbation d'exception du RSSI.
- Formation de l'utilisateur complétée et accusé de réception signé.
- Solution MDM ou de conteneurisation déployée avant l'attribution de l'accès.

Lorsqu'un appareil personnel est autorisé :

- L'appareil devra être enregistré dans le registre des actifs.
- L'utilisateur devra recevoir une formation et signer un accusé de responsabilité.
- Toutes les politiques de l'organisation, incluant la présente politique et la Politique de contrôle d'accès, devront s'appliquer.
- Une solution MDM (gestion des appareils mobiles) ou de conteneurisation devra être installée pour séparer les données personnelles et organisationnelles.
- L'organisation se réserve le droit d'effacer à distance les données organisationnelles de l'appareil en cas de résiliation de l'emploi ou de l'accès, ou en cas de perte ou de vol.
- Aucune donnée personnelle ou donnée personnelle sensible (au sens de la nLPD) ne devra être stockée sur l'appareil en dehors du conteneur géré.

### Appareils interdits

Les appareils suivants ne devront pas être utilisés pour le travail organisationnel :

- Appareils débridés (jailbreakés) ou rootés.
- Appareils dont les fonctionnalités de sécurité sont désactivées.
- Appareils partagés ne relevant pas du contrôle exclusif de l'utilisateur.
- Appareils fonctionnant sous des systèmes d'exploitation en fin de vie ne recevant plus de mises à jour de sécurité.
- Appareils ne pouvant pas satisfaire aux exigences minimales de sécurité définies par la Sécurité informatique.

## Résiliation du télétravail

Lors de la résiliation de l'autorisation de télétravail ou de l'emploi :

- Les identifiants d'accès distant devront être révoqués immédiatement (le jour même).
- Les jetons VPN et d'accès distant devront être désactivés.
- Tous les équipements organisationnels devront être restitués conformément à la Politique de restitution des actifs (A.5.11).
- Toutes les données organisationnelles devront être supprimées des appareils personnels. Pour les appareils AVEC, l'effacement à distance MDM du conteneur organisationnel devra être exécuté.
- La restitution et la suppression des données devront être vérifiées et documentées.

---

# Partie 2 — Signalement des événements de sécurité (A.6.8)

## Canaux de signalement

L'organisation devrait fournir des mécanismes accessibles permettant à tout le personnel de signaler les événements de sécurité de l'information observés ou suspectés.

**Exigences relatives aux canaux** :

- Au moins **deux canaux de signalement distincts** devront être disponibles.
- Au moins **un canal** devra être disponible en dehors des heures ouvrables (24h/24, 7j/7).
- Tous les canaux devront être accessibles depuis des emplacements distants sans nécessiter d'accès aux systèmes internes (pour permettre le signalement d'événements liés aux accès).

**Canaux de signalement standard** :

| Canal | Objet | Disponibilité |
|-------|-------|---------------|
| **Messagerie sécurité** (p. ex., security@[organisation].ch) | Événements non urgents, rapports détaillés avec pièces jointes | 24h/24, 7j/7 (surveillé pendant les heures ouvrables) |
| **Téléphone / permanence** | Événements urgents, attaques actives, appareils perdus/volés | 24h/24, 7j/7 (permanence en dehors des heures) |
| **Système de ticketing** | Soumission formelle d'événements, suivi, relance | Heures ouvrables |
| **Option anonyme** (formulaire web ou permanence tierce) | Signalements où le déclarant souhaite rester anonyme | 24h/24, 7j/7 |

**Signalement anonyme** :
- **Objet** : Permet le signalement de violations de politique suspectées, de menaces internes ou de préoccupations sensibles lorsque le déclarant craint des représailles.
- **Préservation de l'anonymat** : Canal anonyme opéré par un prestataire tiers (le cas échéant) ou via un formulaire web sans journalisation d'informations personnellement identifiables. L'identité du déclarant n'est ni suivie ni consignée.
- **Limitation du suivi** : Étant donné que l'identité du déclarant est inconnue, le suivi est limité. Les déclarants anonymes sont encouragés à consulter le portail/canal de signalement pour les réponses si le système prend en charge la communication anonyme bidirectionnelle.
- **Approche alternative** : Les déclarants peuvent également signaler aux RH ou au Conseil juridique en toute confidentialité (pas d'anonymat complet) si un suivi est nécessaire.

Les signalements anonymes reçoivent la même priorité et le même niveau d'investigation que les signalements identifiés.

**Publication** : Les canaux de signalement devront être publiés sur l'intranet, inclus dans les documents d'intégration des employés, référencés dans la formation annuelle à la sensibilisation à la sécurité, et affichés sur les écrans de connexion ou les fonds d'écran du bureau.

## Événements à signaler

**Distinction entre événement et incident** :

| Terme | Définition |
|-------|------------|
| **Événement de sécurité** | Occurrence identifiée indiquant une *possible* violation de la politique de sécurité ou une défaillance des contrôles |
| **Incident de sécurité** | Événement de sécurité qui a été évalué et confirmé comme ayant un effet défavorable réel ou potentiel sur la confidentialité, l'intégrité ou la disponibilité des informations |

**Le personnel signale les ÉVÉNEMENTS. L'équipe Sécurité informatique évalue si les événements constituent des INCIDENTS.** En cas de doute, signalez-le.

**Catégories d'événements à signaler** :

**Hameçonnage et ingénierie sociale** :

- E-mails suspects demandant des identifiants, des paiements ou des informations sensibles.
- Appels téléphoniques ou messages texte suspects usurpant l'identité de collègues ou de fournisseurs.
- Tentatives de manipulation pour contourner les contrôles de sécurité ou obtenir un accès.

**Logiciels malveillants et compromission de systèmes** :

- Comportement inattendu du système, dégradation des performances ou pannes.
- Fenêtres contextuelles, messages ou notifications suspects.
- Infection suspectée par un logiciel malveillant (y compris les indicateurs de rançongiciel).
- Modifications du système non traitées via le contrôle des changements.

**Accès non autorisé** :

- Tentatives de connexion inconnues ou inattendues sur des comptes.
- Appareils non familiers connectés à des comptes.
- Verrouillages de comptes ou changements de mot de passe inattendus.
- Changements de privilèges suspects ou nouveaux comptes administrateurs.

**Violation et fuite de données** :

- E-mails mal adressés contenant des données sensibles ou personnelles.
- Accès, exposition ou téléchargement non autorisé de données.
- Documents ou supports perdus ou volés contenant des données organisationnelles.
- Exfiltration de données suspectée.

**Sécurité physique** :

- Appareils perdus ou volés (ordinateurs portables, téléphones, clés USB, cartes d'accès).
- Filature ou accès physique non autorisé à des zones sécurisées.
- Équipements manquants ou endommagés.

**Violations de politique** :

- Contournement observé des contrôles de sécurité.
- Violations connues de la politique de sécurité par d'autres personnes.
- Installations de logiciels non approuvés ou changements de configuration.

**Spécifiques au télétravail** :

- Compromission suspectée du réseau ou du routeur domestique.
- Accès non autorisé à l'appareil de travail par des membres de la famille ou d'autres personnes.
- Défaillances VPN ou d'accès distant suggérant une attaque ou une compromission.
- Activité suspecte lors d'un travail depuis des lieux publics.
- Vol ou perte d'appareils lors de déplacements ou sur un site distant.
- Demandes suspectes du support informatique demandant des identifiants d'accès distant.
- Modifications de la configuration du routeur domestique non initiées par l'utilisateur.
- Observation physique des documents de travail par des personnes non autorisées.

### Procédure en cas de perte ou de vol d'un appareil

Si un appareil contenant des données organisationnelles est perdu ou volé :

1. **Signaler immédiatement** via téléphone/permanence (Gravité Critique — signaler immédiatement).
2. **Fournir les détails** : Type d'appareil, numéro de série (si connu), dernier emplacement connu, heure approximative de la perte ou du vol, classification des données sur l'appareil.
3. **Actions de la Sécurité informatique** :
   - Initier l'effacement à distance (si l'appareil est allumé et connecté).
   - Révoquer les identifiants VPN et d'accès distant.
   - Surveiller toute activité suspecte sur les comptes.
   - Documenter l'incident à des fins d'investigation.
4. **Actions de l'utilisateur** :
   - Changer les mots de passe des comptes accédés depuis l'appareil perdu (selon les instructions de la Sécurité informatique).
   - Déposer une plainte auprès des forces de l'ordre (en cas de vol) et communiquer le numéro de rapport à la Sécurité informatique.
   - Ne pas tenter de récupérer l'appareil soi-même (priorité à la sécurité personnelle).
5. **Assurance / Remplacement** : Contacter les RH pour la procédure de remplacement de l'appareil.

**Préservation des preuves** : Si l'appareil est retrouvé ultérieurement, ne pas le mettre sous tension ni tenter de l'utiliser. Le remettre à la Sécurité informatique pour analyse forensique.

## Procédures de signalement

**Informations à inclure dans un signalement** (dans la mesure du possible) :

- Date et heure à laquelle l'événement a été observé ou découvert.
- Description de ce qui s'est passé.
- Systèmes, applications ou données potentiellement affectés.
- Actions déjà prises (le cas échéant).
- Coordonnées pour le suivi (sauf en cas de signalement anonyme).
- Toute preuve à l'appui (captures d'écran, en-têtes d'e-mail, messages d'erreur).

**Délais de signalement** :

| Gravité de l'événement | Exemples | Délai de signalement |
|----------------------|----------|---------------------|
| **Critique** | Attaque active, violation de données confirmée, rançongiciel, appareil avec données Restreintes volé | Immédiatement |
| **Élevée** | Appareil perdu/volé, compromission d'identifiants, infection suspectée par logiciel malveillant | Dans l'heure |
| **Moyenne** | Tentative d'hameçonnage (sans clic), activité suspecte, violation de politique observée | Dans les 4 heures |
| **Faible** | Préoccupation de sécurité générale, dérogation mineure à la politique, activité inhabituelle mais non menaçante | Dans les 24 heures |

En cas d'incertitude sur la gravité, signaler au niveau supérieur. L'équipe Sécurité informatique réévaluera lors du triage. Ne pas retarder le signalement pour déterminer la classification précise.

**Responsabilités du déclarant** :

- Signaler rapidement conformément aux délais ci-dessus.
- Fournir des informations exactes au meilleur de sa connaissance.
- **Préserver les preuves** : Transmettre les e-mails d'hameçonnage en pièces jointes (ne pas les transmettre en ligne ni cliquer sur les liens). Capturer les anomalies et noter l'heure exacte et les systèmes affectés. Photographier les événements de sécurité physique si cela peut se faire en toute sécurité.
- **NE PAS** tenter d'enquêter, de vérifier ou de résoudre l'événement soi-même.
- **NE PAS** tenter de tester ou d'exploiter des vulnérabilités suspectées.
- Coopérer à toute investigation de suivi menée par l'équipe Sécurité informatique.

## Culture sans blâme

L'organisation favorise un environnement non punitif pour le signalement des événements de sécurité.

| Principe | Engagement |
|----------|-----------|
| **Protection de la bonne foi** | Le personnel qui signale des événements de bonne foi ne devra pas subir de conséquences négatives pour l'acte de signalement |
| **Gestion des erreurs honnêtes** | Les erreurs honnêtes (p. ex., clic sur un lien d'hameçonnage) signalées rapidement devront être traitées de manière constructive, en se concentrant sur l'apprentissage et la prévention |
| **Pas de représailles** | Les représailles contre les déclarants de bonne foi sont interdites et feront elles-mêmes l'objet de mesures disciplinaires |
| **Confidentialité du déclarant** | L'identité du déclarant devra être protégée dans la mesure du possible et partagée uniquement sur la base du besoin d'en connaître |

L'organisation devrait reconnaître et encourager les comportements de signalement exemplaires. Les événements signalés devront être utilisés comme opportunités d'apprentissage, et non comme déclencheurs de sanctions.

**Exceptions à la protection sans blâme** :

- Violations délibérées de la politique signalées uniquement après découverte par d'autres.
- Activité malveillante déguisée en accident.
- Négligence répétée après formation et avertissements formels.
- Faux signalements effectués de mauvaise foi.

## Réponse et retour d'information

L'organisation devrait répondre à tous les signalements d'événements de sécurité dans les délais définis :

| Type de réponse | Délai |
|----------------|-------|
| **Accusé de réception** (confirmation de la réception du signalement) | Dans les 4 heures ouvrables |
| **Évaluation initiale** (événement classifié, priorité attribuée) | Dans les 24 heures |
| **Mise à jour de statut au déclarant** | Dans les 72 heures |
| **Notification de clôture** | À la résolution |

L'organisation devrait :

- Accuser réception de tous les signalements (y compris les signalements anonymes lorsqu'un canal de réponse existe).
- Fournir des mises à jour de statut aux déclarants sur la progression et l'issue de leurs signalements.
- Communiquer les enseignements tirés des événements par des mises à jour de sensibilisation (sans identifier les déclarants).
- Escalader les événements vers le processus de gestion des incidents (conformément à A.5.24-28) lorsque l'événement est évalué comme un incident de sécurité confirmé, nécessite des ressources au-delà de la réponse initiale, a des implications de notification réglementaire, ou affecte plusieurs systèmes ou unités opérationnelles.

## Indicateurs de signalement des événements

L'organisation devrait suivre les indicateurs de signalement des événements de sécurité suivants :

| Indicateur | Objectif | Fréquence de révision |
|-----------|---------|----------------------|
| **Accusé de réception dans les 4 heures ouvrables** | 100 % | Mensuelle |
| **Évaluation initiale dans les 24 heures** | 100 % | Mensuelle |
| **Tendance du volume de signalements** (sensibilisation accrue ou menace accrue) | Suivi | Trimestrielle |
| **Utilisation des canaux de signalement** (messagerie, téléphone, ticketing, anonyme) | Utilisation équilibrée entre les canaux | Trimestrielle |
| **Retour d'information des déclarants** (satisfaction quant à la réponse et à la communication) | >80 % satisfaits | Annuelle (enquête) |
| **Taux de faux positifs** (événements vs. incidents confirmés) | Suivi | Trimestrielle |

Les indicateurs devront être rapportés au RSSI mensuellement et à l'équipe de revue de direction trimestriellement.

**ICP de signalement des événements intégrés dans la formation à la sensibilisation** : La formation annuelle devra inclure le volume de signalements et des exemples de bonnes pratiques pour renforcer la culture sans blâme.

---

## Formation et sensibilisation au signalement

Tout le personnel devrait recevoir une formation sur le signalement des événements de sécurité :

**Formation initiale** (dans les 30 jours suivant l'embauche ou un changement de rôle) :
- Ce qui constitue un événement de sécurité par rapport à un incident.
- Catégories d'événements à signaler avec des exemples.
- Canaux de signalement et quand utiliser chacun d'eux.
- Délais de signalement par gravité.
- Culture sans blâme et protection de la bonne foi.

**Formation de remise à niveau annuelle** :
- Paysage des menaces mis à jour (campagnes d'hameçonnage récentes, tactiques d'ingénierie sociale).
- Exemples de bonnes pratiques (événements signalés ayant prévenu des incidents).
- Indicateurs de signalement (renforçant la valeur accordée au signalement).

**Simulation d'hameçonnage** : Simulations d'hameçonnage trimestrielles avec formation immédiate pour les utilisateurs qui cliquent ; les simulations sont traitées comme des opportunités d'apprentissage, et non comme des mesures punitives.

Suivi de la réalisation de la formation ; objectif : **100 % du personnel** complète la formation annuelle.

---

## Vérification de la conformité au télétravail

La conformité à la sécurité du télétravail devrait être vérifiée via :

**Contrôles de conformité trimestriels** :
- Journaux d'utilisation VPN/MFA (100 % des télétravailleurs accèdent via VPN avec MFA).
- État du chiffrement des appareils (100 % des appareils enregistrés chiffrés).
- Protection des points de terminaison à jour (100 % des appareils avec antivirus/EDR à jour).
- Conformité aux correctifs (≥95 % des appareils à jour sur les correctifs OS et critiques).

**Révisions annuelles du télétravail** :
- Révision des autorisations de télétravail (confirmation que les autorisations sont à jour et appropriées).
- Audit de l'inventaire des appareils AVEC (vérification que tous les appareils personnels sont enregistrés et conformes).
- Télétravailleurs à haut risque (accès aux données Confidentielles) — actualisation de l'évaluation des risques.

**Contrôles ponctuels** (aléatoires ou déclenchés) :
- La Sécurité informatique peut effectuer des contrôles de conformité à distance (demande de captures d'écran montrant le chiffrement, la protection des points de terminaison, la connexion VPN).
- La non-conformité déclenche un plan de remédiation ou la révocation des privilèges de télétravail.

Indicateurs de conformité rapportés au RSSI trimestriellement.

---

## Rôles et responsabilités

| Rôle | Responsabilités |
|------|-----------------|
| **Direction générale** | Approuver la politique de télétravail ; fournir les ressources ; défendre la culture de signalement sans blâme ; recevoir des briefings sur les événements de sécurité critiques |
| **RSSI** | Définir les exigences de sécurité du télétravail et les mécanismes de signalement des événements ; autoriser les exceptions à haut risque ; superviser la conformité ; rendre compte à la direction |
| **Équipe Sécurité informatique** | Mettre en œuvre et maintenir les contrôles d'accès distant ; recevoir et évaluer les signalements d'événements ; coordonner la réponse ; fournir un retour d'information aux déclarants ; maintenir les canaux de signalement |
| **Opérations informatiques** | Provisionner l'accès distant (VPN, MFA, appareils) ; soutenir l'infrastructure des canaux de signalement ; mettre en œuvre les actions de confinement lorsque dirigé |
| **RH** | Gérer les accords de télétravail et les résiliations ; inclure le signalement des événements dans l'intégration ; coordonner les questions liées au personnel |
| **Responsables hiérarchiques** | Autoriser le télétravail pour les membres de l'équipe ; assurer la conformité de l'équipe ; encourager le signalement des événements ; escalader les préoccupations de sécurité |
| **Tout le personnel** | Respecter les exigences du télétravail ; sécuriser les appareils et les données ; signaler rapidement les événements ; préserver les preuves ; coopérer aux investigations |

---

## Preuves

Les preuves suivantes démontrent la conformité à la présente politique :

| # | Preuve | Responsable | Fréquence |
|---|--------|-------------|-----------|
| 1 | **Dossiers d'autorisation de télétravail** (arrangements approuvés avec évaluation des risques le cas échéant) | RH / Responsables hiérarchiques | *Par arrangement ; révisé annuellement ; conservé durée + 2 ans* |
| 2 | **Dossiers d'accusé de réception de la politique** des télétravailleurs | RH | *Par intégration / renouvellement annuel ; objectif : couverture 100 %* |
| 3 | **Inventaire des appareils** (appareils d'entreprise et AVEC approuvés affectés aux télétravailleurs) | Opérations informatiques | *Mis à jour dans les 5 jours ouvrables suivant un changement ; audité annuellement* |
| 4 | **Rapports de conformité technique** (utilisation VPN, inscription MFA, chiffrement des appareils, état des correctifs) | Sécurité informatique | *Révisé mensuellement ; tableau de bord mis à jour en continu* |
| 5 | **Signalements d'événements de sécurité** reçus via les canaux désignés | Sécurité informatique | *Maintenu en continu ; conservé minimum 3 ans* |
| 6 | **Dossiers de réponse aux événements** (accusé de réception, évaluation, mises à jour de statut, clôture) avec indicateurs de délais de réponse | Sécurité informatique | *Par événement ; conformité aux délais de réponse révisée trimestriellement* |
| 7 | **Dossiers de formation à la sensibilisation à la sécurité** couvrant la sécurité du télétravail et le signalement des événements | RH / Sécurité informatique | *Annuel ; suivi de la réalisation ; objectif : 100 % des télétravailleurs* |
| 8 | **Dossiers de disponibilité des canaux de signalement** (test et disponibilité des canaux messagerie, téléphone, ticketing, anonyme) | Opérations informatiques | *Testés trimestriellement ; résultats documentés* |
| 9 | **Dossiers de restitution des équipements et de suppression des données** lors de la résiliation du télétravail | Opérations informatiques / RH | *Par résiliation ; vérifié et validé* |
| 10 | **Registre des exceptions** (exceptions autorisées à la présente politique avec justification et mesures compensatoires) | RSSI | *Mis à jour par exception ; révisé trimestriellement ; entrées à durée limitée réévaluées à l'expiration* |

---

# Conformité à la politique

## Mesure de la conformité

L'équipe de management de la sécurité de l'information vérifiera la conformité à la présente politique par diverses méthodes, notamment l'analyse des journaux d'accès distant, les rapports de conformité des appareils, les indicateurs de signalement des événements (volume, rapidité, délais de réponse), les audits internes et externes, et les retours au propriétaire de la politique.

## Exceptions

Toute exception à la présente politique devra être approuvée et enregistrée à l'avance par le Responsable de la sécurité de l'information, avec une acceptation documentée des risques, des mesures compensatoires et une date de révision définie. Les exceptions devront être rapportées à l'équipe de revue de direction.

## Non-conformité

Un employé reconnu coupable de violation de la présente politique peut faire l'objet de mesures disciplinaires pouvant aller jusqu'au licenciement. La non-conformité aux exigences du télétravail peut également entraîner la révocation des privilèges de télétravail. Le fait de ne pas signaler des événements de sécurité ne bénéficie pas de la protection sans blâme et peut être traité comme une violation de la politique.

## Amélioration continue

La présente politique est révisée et mise à jour dans le cadre du processus d'amélioration continue. Les révisions devront tenir compte des évolutions des modes de télétravail, des menaces émergentes ciblant les télétravailleurs, des changements réglementaires (notamment la nLPD et le RGPD), des développements technologiques, des tendances en matière de signalement des événements et des enseignements tirés des incidents.

---

# Domaines de la norme ISO 27001 couverts

Politique de télétravail et de signalement des événements de sécurité — Correspondance avec les contrôles ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership et engagement | 5.1 Politiques de sécurité de l'information |
| Clause 5.2 Politique | 5.4 Responsabilités de la direction |
| Clause 6.2 Objectifs de sécurité de l'information | 5.36 Conformité aux politiques, règles et normes |
| Clause 7.3 Sensibilisation | 6.3 Sensibilisation, formation et éducation à la sécurité de l'information |
| Clause 8.1 Planification et contrôle opérationnels | 6.4 Processus disciplinaire |
| | **6.7 Télétravail** |
| | **6.8 Signalement des événements de sécurité de l'information** |
| | 7.9 Sécurité des actifs hors des locaux |
| | 8.1 Appareils de point de terminaison utilisateur |

**Cadre réglementaire et juridique** :

| Cadre | Pertinence |
|-------|-----------|
| nLPD suisse (nFADP/revDSG) | Art. 8 — Mesures techniques et organisationnelles pour la protection des données dans les environnements de télétravail |
| CO suisse art. 328b | Le traitement des données des employés est limité aux données nécessaires à la relation de travail |
| OPDo suisse (Ordonnance sur la protection des données) | Art. 1-3 — Exigences minimales en matière de sécurité des données |
| RGPD UE (si applicable) | Art. 32 — La sécurité du traitement doit s'étendre au télétravail ; Art. 33 — La notification des violations dans les 72 heures nécessite une détection rapide des événements |
| ISO/IEC 27001:2022 | Contrôles Annexe A 6.7, 6.8 |
| ISO/IEC 27002:2022 | Sections 6.7, 6.8 — Lignes directrices de mise en œuvre |
| NIST SP 800-46 Rév. 2 | Guide de sécurité pour le télétravail en entreprise, l'accès distant et le AVEC |
| CIS Controls v8 | Contrôle 4 (Configuration sécurisée des actifs d'entreprise), Contrôle 6 (Gestion du contrôle d'accès), Contrôle 17 (Gestion de la réponse aux incidents) |

---

<!-- QA_VERIFIED: 2026-03-29 -->
