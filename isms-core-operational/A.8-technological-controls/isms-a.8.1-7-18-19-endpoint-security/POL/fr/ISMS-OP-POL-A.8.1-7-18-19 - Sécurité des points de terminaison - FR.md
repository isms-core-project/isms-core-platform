<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.8.1-7-18-19-FR:operational:OP-POL:a.8.1-7-18-19 -->
**ISMS-OP-POL-A.8.1-7-18-19 — Sécurité des points de terminaison**

---

**Contrôle documentaire**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Sécurité des points de terminaison |
| **Type de document** | Politique opérationnelle |
| **Identifiant du document** | ISMS-OP-POL-A.8.1-7-18-19 |
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

- ISO/IEC 27001:2022 Contrôles A.8.1, A.8.7, A.8.18, A.8.19 — Appareils des utilisateurs finaux, protection contre les logiciels malveillants, utilisation des programmes utilitaires à privilèges, installation de logiciels sur les systèmes opérationnels

**Contrôles Annexe A associés** :

| Contrôle | Relation avec la sécurité des points de terminaison |
|----------|-----------------------------------------------------|
| A.5.9 Inventaire des informations et autres actifs associés | Inventaire des appareils et registre des actifs |
| A.5.15-18 Contrôle d'accès et gestion des identités | Authentification des utilisateurs et droits d'accès sur les points de terminaison |
| A.8.2 Droits d'accès à privilèges | Gestion des accès à privilèges sur les appareils des utilisateurs finaux |
| A.8.5 Authentification sécurisée | Mécanismes d'authentification pour l'accès aux points de terminaison |
| A.8.8 Gestion des vulnérabilités techniques | Gestion des correctifs pour les systèmes d'exploitation et applications des points de terminaison |
| A.8.9 Gestion de la configuration | Configurations de base et durcissement des points de terminaison |
| A.8.20 Sécurité des réseaux | Exigences d'admission réseau pour les appareils des utilisateurs finaux |
| A.8.24 Utilisation de la cryptographie | Chiffrement intégral du disque pour les appareils des utilisateurs finaux |

**Politiques internes associées** :

- Politique de contrôle d'accès
- Politique d'utilisation de la cryptographie
- Politique de sécurité des réseaux
- Politique de gestion des actifs
- Politique de classification et de gestion des informations
- Politique de gestion des incidents

---

# Politique de sécurité des points de terminaison

## Objet

Cette politique vise à gérer et protéger les appareils des utilisateurs finaux de l'organisation et à atténuer le risque de logiciels malveillants, de logiciels non autorisés et d'abus des programmes utilitaires à privilèges.

Cette politique soutient la nLPD suisse (revDSG) et l'Ordonnance sur la protection des données (OPDo) en mettant en œuvre des mesures techniques et organisationnelles proportionnées au risque pour protéger les données personnelles (y compris les données personnelles sensibles) sur les appareils des utilisateurs finaux. Lorsque l'organisation traite des données de personnes dans l'UE/EEE, les exigences du RGPD s'appliquent également.

## Champ d'application

Tous les employés et utilisateurs tiers.

Tous les appareils appartenant à l'organisation (ordinateurs portables, postes de travail, téléphones mobiles, tablettes).

Tous les appareils utilisés pour accéder, traiter, transmettre ou stocker des informations de l'organisation, y compris les appareils personnels lorsque l'AVEC (Apportez Votre Équipement Connecté) est autorisé.

Les appareils virtuels et les points de terminaison hébergés dans le cloud lorsque applicable et possible.

## Principe

Les appareils de l'organisation doivent avoir une protection adéquate des informations contre le risque de logiciels malveillants, de logiciels non autorisés, de perte ou de vol. Les points de terminaison sont gérés selon le principe du moindre privilège avec une sécurité dès la conception et par défaut.

---

## Appareils des utilisateurs finaux

### Enregistrement et inventaire des appareils

Tous les appareils doivent être enregistrés dans le registre des actifs avant d'être remis aux utilisateurs. Le registre doit enregistrer le type d'appareil, le numéro de série, l'utilisateur assigné, le système d'exploitation, le statut de chiffrement et la date de remise.

Les appareils perdus, volés, mis hors service ou réaffectés doivent être mis à jour dans le registre des actifs sans délai.

### Configuration de base des points de terminaison

Tous les appareils doivent être configurés selon une configuration de base de sécurité documentée avant déploiement. La configuration de base doit inclure :

- Système d'exploitation durci selon les recommandations du fournisseur et le Référentiel CIS (Niveau 1 minimum ; Niveau 2 pour les systèmes traitant des données confidentielles ou personnelles sensibles).
- Services, ports et comptes par défaut inutiles désactivés ou supprimés.
- Chiffrement intégral du disque activé (voir section Chiffrement ci-dessous).
- Protection contre les logiciels malveillants installée et active (voir section Protection contre les logiciels malveillants ci-dessous).
- Verrouillage de l'écran et délai d'expiration de session configurés.
- Pare-feu local activé.
- Mises à jour automatiques du système d'exploitation et des applications activées.

La configuration de base doit être documentée et sous contrôle de version. Les normes de configuration de base doivent référencer les guides de durcissement des fournisseurs et les Référentiels CIS. La configuration de base doit être révisée au moins annuellement ou lors de modifications importantes du système d'exploitation ou du paysage des menaces.

### Outils de gestion des points de terminaison

Les catégories d'outils de gestion suivantes doivent être déployées pour soutenir la sécurité des points de terminaison :

| Catégorie | Objectif | Exemples |
|-----------|---------|----------|
| **Détection et réponse des points de terminaison (EDR)** | Détection des menaces, investigation et réponse sur les points de terminaison | CrowdStrike Falcon, Microsoft Defender for Endpoint, SentinelOne ou équivalent |
| **Gestion des appareils mobiles (MDM)** | Enrôlement des appareils, configuration, conformité, effacement à distance | Jamf Pro, Microsoft Intune, VMware Workspace ONE ou équivalent |
| **Gestion des correctifs** | Déploiement automatisé et rapport de conformité pour les correctifs du système d'exploitation et des applications | WSUS, Jamf Pro, ManageEngine ou équivalent |
| **Séquestre des clés de chiffrement** | Stockage centralisé des clés de récupération pour le chiffrement intégral du disque | Intégré au MDM ou gestion des clés dédiée |
| **Approbation des logiciels** | Liste d'autorisation des applications et contrôle des installations | AppLocker, Santa, catalogue d'applications MDM ou équivalent |

### Chiffrement

Tous les appareils (ordinateurs portables, postes de travail, appareils mobiles) doivent avoir le chiffrement intégral du disque activé :

| Plateforme | Technologie de chiffrement | Norme minimale |
|------------|--------------------------|----------------|
| Windows | BitLocker | AES-XTS 256 bits |
| macOS | FileVault | XTS-AES 128 bits |
| Mobile (iOS/Android) | Chiffrement natif de l'appareil | Activé par défaut ; vérifier actif |
| Linux | LUKS / dm-crypt | AES-XTS 256 bits |

- Le chiffrement de l'appareil ne doit pas être désactivé par l'utilisateur final.
- Les clés de récupération doivent être séquestrées de manière centralisée via le MDM (p. ex., Jamf Pro, Intune ou équivalent) ou une solution équivalente de séquestre des clés gérée par l'informatique. L'accès aux clés de récupération doit être journalisé et limité au personnel informatique autorisé.
- Le statut de chiffrement doit être vérifié avant que l'appareil soit approuvé pour l'utilisation avec des données confidentielles.

### Verrouillage de l'écran et délai d'expiration de session

- Les appareils doivent se verrouiller automatiquement après **15 minutes** d'inactivité. Les appareils avec accès à des données confidentielles ou personnelles sensibles doivent se verrouiller après **5 minutes** d'inactivité.
- Les utilisateurs doivent verrouiller leurs appareils manuellement lorsqu'ils les laissent sans surveillance (Windows+L, Ctrl+Commande+Q, ou équivalent).
- Une authentification (mot de passe, PIN ou biométrique) doit être requise pour déverrouiller.
- Le verrouillage lors de la mise en veille et de la fermeture du couvercle doit être activé sur tous les ordinateurs portables.

### Sécurité physique

- Les appareils ne doivent pas être laissés sans surveillance dans des lieux publics ni visibles dans des véhicules sans présence.
- Des antivols câble devraient être utilisés pour les postes de travail dans les espaces partagés ou publics.
- Les appareils portables doivent être stockés en sécurité lorsqu'ils ne sont pas utilisés (tiroir ou armoire verrouillé).
- La perte ou le vol de tout appareil doit être signalé immédiatement à l'équipe de gestion de la sécurité de l'information.

### Effacement à distance

L'organisation doit maintenir la capacité d'effacer ou de verrouiller à distance les appareils perdus ou volés via la plateforme MDM ou un outil de gestion équivalent.

Processus d'effacement à distance :

1. Appareil signalé perdu ou volé — l'employé notifie immédiatement l'informatique et son responsable hiérarchique.
2. L'informatique initie le **verrouillage à distance** dans **1 heure** suivant la notification pendant les heures ouvrables (au début du prochain jour ouvrable pour les signalements hors heures ouvrables).
3. Si l'appareil n'est pas récupéré dans les **24 heures**, l'informatique initie l'**effacement à distance**.
4. La confirmation de l'effacement à distance doit être documentée, incluant la date, l'identifiant de l'appareil, le statut de l'effacement (confirmé/en attente) et la personne ayant autorisé.
5. Lorsqu'un appareil AVEC est effacé, seul le conteneur ou profil de travail de l'organisation doit être supprimé (pas les données personnelles), sauf si l'employé a consenti à un effacement complet dans l'accord AVEC.

### AVEC (Apportez Votre Équipement Connecté)

Si l'organisation autorise les appareils personnels à accéder aux informations de l'organisation, les exigences suivantes s'appliquent :

- L'appareil doit être enrôlé dans la solution de gestion des appareils mobiles (MDM) de l'organisation.
- Les données professionnelles doivent être séparées des données personnelles par cloisonnement ou un profil de travail géré.
- L'appareil doit satisfaire à la même configuration de base de sécurité que les appareils appartenant à l'organisation (chiffrement, verrouillage de l'écran, système d'exploitation à jour, protection contre les logiciels malveillants).
- L'organisation conserve le droit d'effacer à distance les données de l'organisation (pas les données personnelles) de l'appareil.
- Les utilisateurs doivent reconnaître leurs responsabilités, notamment la protection physique, les mises à jour des logiciels et la coopération avec les exigences de sécurité.
- L'accès AVEC doit être révoqué à la fin du contrat ou de l'emploi conformément à la Politique de contrôle d'accès.

### Processus d'enrôlement AVEC

1. L'employé soumet une demande d'accès AVEC à l'informatique, en précisant le type d'appareil, le système d'exploitation et le périmètre d'utilisation professionnelle prévu.
2. L'informatique vérifie que l'appareil satisfait aux exigences minimales (version du système d'exploitation prise en charge, capacité de chiffrement, absence de jailbreak/rootage).
3. L'employé signe l'accord AVEC reconnaissant les exigences de sécurité, le consentement à l'effacement à distance pour les données de l'organisation et les obligations de coopération.
4. L'informatique enrôle l'appareil dans le MDM et configure le profil de travail géré ou le conteneur.
5. L'informatique vérifie la conformité à la configuration de base de sécurité (chiffrement actif, verrouillage de l'écran configuré, système d'exploitation à jour) avant d'accorder l'accès.

Si l'AVEC n'est pas autorisé, cela doit être indiqué et appliqué par des contrôles techniques.

---

## Protection contre les logiciels malveillants et antivirus

### Logiciels approuvés

Seuls les logiciels approuvés et sous licence par l'organisation peuvent être installés sur les équipements de l'organisation.

Les logiciels non autorisés, téléchargés, gratuits ou les utilitaires non approuvés ne doivent pas être installés.

### Exigences de protection contre les logiciels malveillants

Un logiciel de protection contre les logiciels malveillants (détection et réponse des points de terminaison — EDR, ou antivirus de nouvelle génération — NGAV, adapté au profil de risque de l'organisation) doit être installé sur chaque appareil pouvant l'exécuter.

Le logiciel de protection contre les logiciels malveillants doit :

- Mettre à jour automatiquement les définitions de détection et les moteurs dès leur publication par le fournisseur.
- Ne pas être modifié, désactivé ou désinstallé par l'utilisateur final.
- Produire une alerte lors d'une infection ou d'une infection suspectée.
- Être configuré pour réparer automatiquement ou mettre en quarantaine les fichiers suspects.
- Analyser automatiquement le stockage local et les appareils de stockage connectés.
- Analyser automatiquement tout fichier accédé, modifié ou exécuté.
- Conserver des journaux d'audit transmis au système de journalisation centralisé.

Les infections suspectées doivent être gérées via le processus de gestion des incidents. Les événements suivants doivent déclencher un rapport d'incident :

- Alerte EDR/antivirus indiquant une détection de logiciel malveillant confirmée (pas un faux positif).
- Indicateurs de rançongiciel (activité de chiffrement de fichiers, fichiers de demande de rançon).
- Connexions sortantes non autorisées vers une infrastructure de commande et contrôle connue.
- Comportement suspect signalé par l'utilisateur (fenêtres contextuelles inattendues, dégradation des performances, processus inconnus).
- Détection de logiciels ou outils non autorisés sur l'appareil.

### Protection de la messagerie

Les serveurs et passerelles de messagerie doivent disposer d'une analyse des logiciels malveillants qui inspecte tous les courriers entrants et sortants, y compris les pièces jointes.

### Protection de la passerelle web

Les proxys Internet ou les passerelles web sécurisées doivent être configurés pour :

- Bloquer les sites à réputation malveillante connue.
- Analyser le contenu à la recherche de menaces sur les sites à réputation intermédiaire.
- Journaliser toutes les détections.
- Vérifier automatiquement les mises à jour des définitions.

Les listes d'autorisation et les listes de refus doivent être déployées pour contrôler l'accès aux ressources web approuvées et interdites.

### Surveillance de l'intégrité des fichiers

La surveillance de l'intégrité des fichiers doit être mise en œuvre pour les fichiers critiques du système et les fichiers contenant ou donnant accès à des données personnelles ou confidentielles, en fonction du risque et des besoins de l'activité.

### Contrôles des supports amovibles

- L'exécution automatique et la lecture automatique doivent être désactivées pour tous les supports amovibles.
- Les supports amovibles doivent être automatiquement analysés à la recherche de logiciels malveillants lors de leur connexion.
- Seuls les supports amovibles chiffrés appartenant à l'organisation doivent être approuvés pour l'utilisation avec des données confidentielles, conformément à la Politique de transfert d'informations.

---

## Formation

Les utilisateurs doivent être formés périodiquement dans le cadre du programme de sensibilisation à la sécurité sur :

- La reconnaissance des e-mails d'hameçonnage et des attaques d'ingénierie sociale.
- L'utilisation sécurisée d'Internet et de la messagerie.
- L'utilisation des logiciels approuvés et l'interdiction des logiciels non approuvés.
- La conduite à tenir en cas d'infection suspectée par un logiciel malveillant.
- La sécurité physique des appareils (verrouillage, stockage, signalement de la perte/vol).

---

## Programmes utilitaires à privilèges

### Périmètre

Les programmes utilitaires à privilèges sont des outils pouvant contourner les contrôles système ou applicatifs. Ils incluent notamment :

- Outils d'administration système (gestion des utilisateurs/groupes, gestion des services).
- Éditeurs de registre, PowerShell (stratégie d'exécution non restreinte) et outils en ligne de commande avec des privilèges élevés.
- Outils de diagnostic, débogueurs et utilitaires disque.
- Utilitaires de sauvegarde et de récupération avec accès aux données brutes.
- Outils de gestion réseau et d'analyse.

### Contrôles

- L'accès aux programmes utilitaires à privilèges doit être restreint au personnel autorisé uniquement, selon le principe du moindre privilège.
- L'authentification multifacteur doit être requise pour l'accès aux programmes utilitaires à privilèges sur les systèmes critiques.
- Toute exécution de programmes utilitaires à privilèges doit être journalisée, incluant l'utilisateur, l'horodatage, le nom de l'utilitaire et le système cible.
- Les programmes utilitaires à privilèges non nécessaires à des fins opérationnelles doivent être supprimés ou désactivés.
- L'utilisation des programmes utilitaires à privilèges doit faire l'objet d'une révision périodique (au moins trimestrielle) pour vérifier la justification commerciale continue.
- L'organisation doit maintenir une liste documentée des programmes utilitaires à privilèges approuvés par rôle.

---

## Installation de logiciels sur les systèmes opérationnels

### Contrôles d'installation des logiciels

- L'installation de logiciels sur les systèmes opérationnels doit être réalisée uniquement par du personnel autorisé (administrateurs informatiques ou personnel de support désigné).
- Les utilisateurs standard ne doivent pas disposer de droits d'administrateur local. Lorsqu'une élévation est nécessaire, un mécanisme géré d'élévation de privilèges doit être utilisé :
  - **Accès juste-à-temps (JIT)** : élévation temporaire accordée pour une période définie (maximum 4 heures), révoquée automatiquement à expiration.
  - **Processus d'approbation** : l'utilisateur soumet une demande avec justification commerciale ; l'informatique ou le responsable hiérarchique approuve ; l'élévation est accordée et journalisée.
  - Toutes les élévations de privilèges doivent être journalisées (utilisateur, horodatage, justification, durée, approbateur).
- Toutes les installations de logiciels doivent suivre le processus de gestion des changements de l'organisation, incluant les tests, l'approbation et la documentation.
- Seuls les logiciels approuvés du catalogue de logiciels de l'organisation peuvent être installés. Les nouvelles demandes de logiciels doivent être soumises via un processus d'approbation formel.

### Gestion des correctifs

Les systèmes d'exploitation, applications et navigateurs sur les appareils des utilisateurs finaux doivent être maintenus à jour. Les correctifs de sécurité doivent être appliqués selon les délais suivants :

| Gravité | Délai |
|---------|-------|
| Vulnérabilités critiques (CVSS 9,0+, exploitation active) | Dans les 14 jours |
| Vulnérabilités élevées (CVSS 7,0-8,9) | Dans les 30 jours |
| Vulnérabilités moyennes (CVSS 4,0-6,9) | Dans les 90 jours |
| Vulnérabilités faibles (CVSS 0,1-3,9) | Prochaine fenêtre de maintenance planifiée |

Les correctifs doivent être testés avant déploiement selon l'approche suivante :

| Type de système | Exigence de test |
|----------------|-----------------|
| Points de terminaison standard (ordinateurs portables, postes de travail) | Déploiement sur un **groupe pilote** (5-10 % des appareils) pendant **48 heures** avant le déploiement complet |
| Appareils mobiles | Déploiement sur un groupe pilote via MDM pendant 48 heures avant le déploiement complet |
| Points de terminaison spécialisés (bornes, systèmes de laboratoire) | Test en environnement non-production avant déploiement |

- **Correctifs d'urgence P0** (exploitation active confirmée) peuvent contourner les tests du groupe pilote avec l'approbation du RSSI. Une surveillance renforcée pendant 48 heures après déploiement et un plan de retour arrière documenté sont requis.
- **Gestion des échecs de correctifs** : si un correctif provoque des problèmes opérationnels dans le groupe pilote, le déploiement doit être suspendu, le problème documenté et le fournisseur contacté. Un contournement ou un contrôle compensatoire doit être appliqué jusqu'à ce qu'un correctif stable soit disponible.

Les mises à jour automatiques doivent être activées pour les systèmes d'exploitation et les applications prises en charge. Les appareils n'ayant pas appliqué les correctifs critiques dans le délai défini doivent être signalés pour remédiation ou leur accès réseau restreint.

### Retour arrière

Une stratégie de retour arrière doit être convenue avant d'appliquer des mises à jour ou des installations sur les systèmes opérationnels pour garantir la continuité d'activité en cas de problème lié à un correctif.

### Piste d'audit

Un enregistrement de toutes les modifications logicielles sur les systèmes opérationnels doit être maintenu, incluant le nom du logiciel, la version, la date d'installation et la personne ayant effectué la modification.

---

## Rôles et responsabilités

| Rôle | Responsabilités |
|------|----------------|
| **RSSI** | Propriété de la politique ; approbation des exceptions et des contournements de correctifs d'urgence ; point d'escalade pour les non-conformités |
| **Exploitation informatique / Équipe points de terminaison** | Approvisionnement des appareils, configuration de base, gestion MDM, déploiement des correctifs, exécution des effacements à distance |
| **Équipe de gestion de la sécurité de l'information** | Surveillance EDR, triage des incidents de logiciels malveillants, révisions des utilitaires à privilèges, reporting de conformité |
| **Propriétaire d'actif / Responsable hiérarchique** | Approbation de l'attribution des appareils, des demandes AVEC et des demandes de logiciels pour leur équipe |
| **Tous les utilisateurs** | Sécurité physique des appareils, signalement immédiat de la perte/vol, coopération avec les exigences de sécurité, ne pas désactiver les contrôles de sécurité |

---

## Preuves

Les preuves suivantes démontrent la conformité à cette politique :

| N° | Preuve | Responsable | Fréquence |
|----|--------|-------------|-----------|
| 1 | **Inventaire des appareils** (registre des actifs avec statut de chiffrement, version du système d'exploitation, utilisateur assigné) | Exploitation informatique | *Mis à jour par événement ; audit complet annuellement* |
| 2 | Documentation de la **configuration de base des points de terminaison** et rapports d'analyse de conformité | Exploitation informatique | *Configuration de base révisée annuellement ; analyses de conformité mensuelles* |
| 3 | Rapports de **déploiement et de statut de mise à jour de la protection contre les logiciels malveillants** (pourcentage de couverture, actualité des définitions) | Sécurité de l'information | *Rapports mensuels ; cible : couverture à 100 %* |
| 4 | **Journaux de détection de logiciels malveillants et d'incidents** (détections, actions de quarantaine, escalades d'incidents) | Sécurité de l'information | *Révisés mensuellement ; conservés 12 mois* |
| 5 | **Enregistrements d'installation de logiciels** et approbations de gestion des changements | Exploitation informatique | *Par événement ; audité trimestriellement* |
| 6 | Liste approuvée et journaux d'utilisation des **programmes utilitaires à privilèges** | Sécurité de l'information | *Liste révisée trimestriellement ; journaux conservés 12 mois* |
| 7 | **Rapports de conformité des correctifs** (pourcentage d'appareils à jour, correctifs en retard par gravité) | Exploitation informatique | *Mensuel ; cible : ≥ 95 % dans les délais ANS* |
| 8 | **Enregistrements d'enrôlement AVEC** et statut de conformité MDM (le cas échéant) | Exploitation informatique | *Mis à jour par événement ; révisé semestriellement* |
| 9 | **Enregistrements d'exécution d'effacement à distance** (identifiant de l'appareil, date, statut de l'effacement, personne ayant autorisé) | Exploitation informatique | *Par événement ; conservé 3 ans* |
| 10 | **Enregistrements de test des correctifs du groupe pilote** (résultats des tests, problèmes identifiés, décisions de déploiement) | Exploitation informatique | *Par cycle de correctifs* |

---

# Conformité à la politique

## Mesure de la conformité

L'équipe de gestion de la sécurité de l'information vérifiera la conformité à cette politique par diverses méthodes, notamment l'analyse de conformité des points de terminaison, les rapports de détection de logiciels malveillants, les rapports de statut des correctifs, les audits d'inventaire des logiciels, les audits internes et externes, et les retours adressés au propriétaire de la politique.

## Exceptions

Toute exception à cette politique doit être approuvée et enregistrée à l'avance par le Responsable de la sécurité de l'information, avec acceptation des risques documentée, contrôles compensatoires et date de révision définie. Les exceptions doivent être signalées à l'équipe de revue de direction.

## Non-conformité

Un employé dont il est établi qu'il a enfreint cette politique peut faire l'objet de mesures disciplinaires, pouvant aller jusqu'au licenciement.

## Amélioration continue

Cette politique est révisée et mise à jour dans le cadre du processus d'amélioration continue. Les révisions doivent tenir compte des modifications des normes de sécurité des points de terminaison, des menaces émergentes (y compris les nouvelles techniques de logiciels malveillants et vecteurs d'attaque), des changements réglementaires et des enseignements tirés des incidents.

---

# Domaines de la norme ISO 27001 couverts

Politique de sécurité des points de terminaison — Correspondance avec les contrôles ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership et engagement | 5.1 Politiques de sécurité de l'information |
| Clause 5.2 Politique | 5.4 Responsabilités de la direction |
| Clause 6.2 Objectifs de sécurité de l'information | 5.36 Conformité aux politiques, règles et normes |
| Clause 7.3 Sensibilisation | 6.3 Sensibilisation, éducation et formation à la sécurité de l'information |
| | 6.4 Processus disciplinaire |
| | **8.1 Appareils des utilisateurs finaux** |
| | **8.7 Protection contre les logiciels malveillants** |
| | **8.18 Utilisation des programmes utilitaires à privilèges** |
| | **8.19 Installation de logiciels sur les systèmes opérationnels** |
| | 8.23 Filtrage web |

**Cadre réglementaire et juridique** :

| Cadre | Pertinence |
|-------|-----------|
| nLPD suisse (revDSG) | Art. 8 — Mesures techniques et organisationnelles pour la protection des données |
| OPDo suisse (Ordonnance sur la protection des données) | Art. 1-3 — Exigences minimales de sécurité des données |
| RGPD de l'UE (le cas échéant) | Art. 32 — Sécurité du traitement (contrôles des points de terminaison comme mesure appropriée) |
| ISO/IEC 27001:2022 | Contrôles Annexe A 8.1, 8.7, 8.18, 8.19 |
| ISO/IEC 27002:2022 | Sections 8.1, 8.7, 8.18, 8.19 — Recommandations de mise en œuvre |
| NIST SP 800-53 Rev 5 | SC-28 (Protection des informations au repos), SI-3 (Protection contre les codes malveillants), CM-11 (Logiciels installés par l'utilisateur) |
| CIS Controls v8 | Contrôle 2 (Inventaire et contrôle des actifs logiciels), Contrôle 4 (Configuration sécurisée), Contrôle 10 (Défenses contre les logiciels malveillants) |

---

<!-- QA_VERIFIED: 2026-03-29 -->
