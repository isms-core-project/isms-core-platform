<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.14-FR:framework:POL:a.5.14 -->
**ISMS-POL-A.5.14 — Transfert d'informations**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Transfert d'informations |
| **Type de document** | Politique |
| **Identifiant du document** | ISMS-POL-A.5.14 |
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
- ISMS-POL-A.5.12-13 (Classification et étiquetage de l'information)
- ISMS-POL-A.8.24 (Utilisation de la cryptographie)
- ISMS-POL-A.5.19-23 (Services en nuage)
- ISMS-POL-A.6.6 (Accords de confidentialité et de non-divulgation)
- ISMS-IMP-A.5.14.1-UG/TG (Règles et procédures de transfert)
- ISMS-IMP-A.5.14.2-UG/TG (Évaluation de la sécurité des canaux)
- ISMS-IMP-A.5.14.3-UG/TG (Registre des accords de transfert)
- ISO/IEC 27001:2022 Contrôle A.5.14

---

## Résumé exécutif

La présente politique établit les exigences de [Organisation] pour le transfert sécurisé d'informations afin de protéger celles-ci lors de leur transmission via tous types de canaux et installations de communication.

**Périmètre** : La présente politique s'applique à tous les transferts d'informations, qu'ils soient électroniques, physiques ou verbaux, y compris les transferts au sein de [Organisation] et avec des tiers.

**Objet** : Définir les exigences organisationnelles en matière de sécurité des transferts d'informations. La présente politique établit QUELLES méthodes de transfert sont approuvées et QUI est autorisé à les utiliser. Les procédures de mise en œuvre (COMMENT) sont documentées séparément dans ISMS-IMP-A.5.14 (variantes UG/TG).

**Alignement réglementaire** : La présente politique répond aux exigences de conformité obligatoires visées par ISMS-POL-00 (Cadre d'applicabilité réglementaire), notamment la nLPD suisse, le RGPD de l'UE et la norme ISO/IEC 27001:2022. Les exigences sectorielles conditionnelles (FINMA, PCI DSS v4.0.1) s'appliquent lorsque les activités commerciales de [Organisation] en déclenchent l'applicabilité.

---

**Alignement des contrôles et périmètre**

**Contrôle ISO/IEC 27001:2022 A.5.14**

**ISO/IEC 27001:2022 Annexe A.5.14 — Transfert d'informations**

> *Des règles, procédures ou accords de transfert d'informations devraient être en place pour tous les types d'installations de transfert au sein de l'organisation et entre l'organisation et d'autres parties.*

**Objectifs du contrôle** :

- Protéger la confidentialité, l'intégrité et la disponibilité des informations lors de leur transfert
- Garantir des méthodes de transfert appropriées en fonction de la sensibilité des informations
- Établir des accords de transfert avec les parties externes
- Maintenir la traçabilité et les pistes d'audit pour les transferts

**Type de contrôle** : Préventif
**Catégorie de contrôle** : Organisationnelle

**La présente politique traite** :

- Les méthodes et canaux de transfert approuvés
- Les exigences de transfert par niveau de classification de l'information
- Les accords et exigences de transfert externe
- L'autorisation de transfert et la responsabilité
- La gestion des incidents liés aux défaillances de transfert

## Ce que fait cette politique

La présente politique :

- **Définit** les méthodes de transfert approuvées pour chaque niveau de classification
- **Établit** les exigences pour les transferts externes et transfrontaliers
- **Spécifie** les exigences d'autorisation pour différents types de transferts
- **Référence** les exigences réglementaires applicables conformément à ISMS-POL-00

## Ce que cette politique ne fait PAS

La présente politique ne :

- **Définit pas les configurations des outils de chiffrement** (voir ISMS-IMP-A.5.14 et ISMS-POL-A.8.24)
- **Établit pas les procédures des plateformes de transfert de fichiers** (voir ISMS-IMP-A.5.14)
- **Couvre pas l'administration des passerelles de messagerie sécurisée** (documentation opérationnelle)
- **Détaille pas le recours aux coursiers physiques** (voir ISMS-IMP-A.5.14)

**Justification** : La séparation entre les exigences de politique et les orientations de mise en œuvre permet :

- La stabilité de la politique malgré les changements de technologie ou de plateforme
- La flexibilité pour différentes solutions de transfert
- Une distinction claire entre gouvernance (politique) et exécution (mise en œuvre)

## Périmètre

**La présente politique s'applique à** :

- Tous les transferts d'informations (électroniques, physiques, verbaux)
- Toutes les méthodes de transfert (messagerie, partage de fichiers, coursier, en personne)
- Tout le personnel (employés, prestataires, tiers) transférant des informations organisationnelles
- Tous les transferts externes vers des clients, partenaires, fournisseurs et autorités de réglementation

**Hors périmètre** :

- Les communications personnelles sans lien avec les informations organisationnelles
- Les informations publiques déjà librement accessibles
- La réplication de bases de données en temps réel (couverte par l'architecture système)

## Applicabilité réglementaire

Les exigences réglementaires sont catégorisées conformément à **ISMS-POL-00 (Cadre d'applicabilité réglementaire)**.

**Niveau 1 : Conformité obligatoire**

| Règlementation | Applicabilité | Exigences principales |
|----------------|---------------|----------------------|
| **nLPD suisse art. 16-17** | Tous les transferts de données personnelles | Exigences de transfert transfrontalier |
| **ISO/IEC 27001:2022** | Périmètre de certification | Contrôle A.5.14 — Transfert d'informations |

**Niveau 2 : Applicabilité conditionnelle**

S'applique uniquement lorsque des conditions commerciales spécifiques déclenchent l'applicabilité :

| Règlementation | Condition déclenchante | Exigences de transfert |
|----------------|------------------------|------------------------|
| **RGPD UE art. 44-49** | Traitement de données personnelles de l'UE | Garanties de transfert international de données, CCT |
| **FINMA** | Établissement financier réglementé suisse | Sécurité renforcée pour les transferts de données financières |
| **Secret bancaire suisse** | Données clients bancaires | Contrôles de transfert stricts |
| **PCI DSS v4.0.1** | Données de cartes de paiement | Exigences de chiffrement pour les données titulaires de carte |
| **HIPAA** | Données de santé américaines | Accords d'associé commercial |

**Niveau 3 : Orientations informatives**

Ces cadres guident la mise en œuvre, mais ne constituent pas une conformité obligatoire sauf obligation contractuelle :

- ISO 27002:2022 Orientations de mise en œuvre pour A.5.14
- NIST SP 800-53 (Protection des systèmes et des communications)
- CIS Controls v8.1 (Protection des données)
- Lignes directrices de l'ENISA sur la sécurité des transferts de données

**Détermination de la conformité** : [Organisation] détermine les réglementations de niveau 2 applicables par une évaluation périodique des activités commerciales. Les exigences de transfert les plus strictes s'appliquent lorsque plusieurs réglementations se chevauchent.

---

# Énoncés de politique

## Exigences relatives aux méthodes de transfert

### Transfert électronique

**Communications par messagerie électronique** :

| Classification | Exigence |
|----------------|----------|
| PUBLIC | Messagerie d'entreprise standard autorisée |
| INTERNE | Messagerie d'entreprise uniquement ; les destinataires externes nécessitent une justification commerciale documentée (objet, destinataire, classification, expiration d'accès) |
| CONFIDENTIEL | Messagerie chiffrée (TLS obligatoire) ou plateforme de partage de fichiers sécurisée |
| RESTREINT | Plateforme chiffrée de bout en bout, vérification du destinataire obligatoire |

**Contrôles de sécurité de la messagerie** :

- Transport Layer Security (TLS) obligatoire pour tous les courriels sortants
- S/MIME ou équivalent pour les pièces jointes CONFIDENTIELLES/RESTREINTES
- Limites de taille des messages respectées (pièces jointes > 25 Mo via plateforme de partage sécurisé)
- Politiques DLP actives pour la détection des modèles de données sensibles
- Avertissements pour les destinataires externes affichés avant l'envoi

**Transfert de fichiers** :

| Méthode | Utilisation autorisée | Limite de classification |
|---------|----------------------|--------------------------|
| Partage de fichiers d'entreprise (SharePoint/OneDrive) | Transferts internes | Jusqu'à RESTREINT |
| Plateforme de transfert de fichiers sécurisée | Transferts externes | Jusqu'à RESTREINT |
| SFTP/SCP | Intégrations système | Jusqu'à CONFIDENTIEL |
| Clés USB (chiffrées) | Exceptions uniquement | Jusqu'à CONFIDENTIEL |
| Partage de fichiers public (Dropbox, Google Drive) | Jamais pour données d'entreprise | PUBLIC uniquement (usage personnel) |

**Transfert via le web** :

- HTTPS obligatoire pour tous les transferts web
- Validation des certificats obligatoire
- Les informations CONFIDENTIELLES et RESTREINTES ne DOIVENT être transférées que via des services web approuvés répertoriés dans le Registre des outils de transfert approuvés ; les autres destinations nécessitent une exception approuvée (ISMS-REG-EXCEPTIONS)
- Portails de téléversement sécurisé pour la soumission de données clients

### Transfert physique

**Transfert de documents** :

| Classification | Méthode de transfert |
|----------------|---------------------|
| PUBLIC | Courrier standard ou coursier |
| INTERNE | Courrier interne ou coursier standard |
| CONFIDENTIEL | Enveloppe scellée, coursier avec suivi, signature du destinataire |
| RESTREINT | Double emballage scellé, coursier agréé, documentation de chaîne de contrôle |

**Transfert de supports** (clés USB, disques durs, bandes de sauvegarde) :

- Tous les supports amovibles chiffrés avant transfert
- Inventaire des supports consigné avec numéro de suivi
- Coursier sécurisé avec chaîne de contrôle pour niveau CONFIDENTIEL+
- Supports RESTREINTS : coursier sécurisé dédié, emballage inviolable

**Transfert en personne** :

- Vérifier l'identité du destinataire avant remise
- Documenter le transfert avec accusé de réception
- Informations RESTREINTES : présence d'un témoin obligatoire

### Transfert verbal

**Communications téléphoniques/vidéo** :

| Classification | Exigence |
|----------------|----------|
| PUBLIC/INTERNE | Systèmes d'entreprise standard |
| CONFIDENTIEL | Participants vérifiés, pas d'enregistrement sans consentement |
| RESTREINT | Canaux sécurisés/chiffrés uniquement, vérification des participants |

**Discussions en personne** :

- CONFIDENTIEL : Lieu privé, pas d'auditeurs non autorisés
- RESTREINT : Salle sécurisée, pas d'appareils électroniques, participants selon le besoin d'en connaître uniquement

## Exigences de transfert externe

### Accords de transfert

Les transferts externes d'informations de classification INTERNE ou supérieure DOIVENT exiger :

**Éléments minimaux de l'accord** :

- Obligations du destinataire en matière de traitement de l'information
- Restrictions d'utilisation et de divulgation autorisées
- Exigences de retour/destruction
- Obligations de notification en cas d'incident
- Droits d'audit le cas échéant

**Types d'accords** :

| Type de transfert | Accord requis |
|-------------------|---------------|
| Transfert ponctuel | Accusé de réception de confidentialité |
| Relation continue | NDA (conformément à ISMS-POL-A.6.6) |
| Fournisseur/prestataire | Accord de traitement des données (en cas d'implication de données personnelles) |
| Données clients | Contrat de service avec conditions de sécurité |

### Transferts transfrontaliers

Les transferts hors de Suisse/EEE DOIVENT se conformer aux :

**Exigences légales** :

- Vérification de la décision d'adéquation (évaluation du pays)
- Clauses contractuelles types (CCT) lorsque requis
- Mesures supplémentaires pour les juridictions à haut risque ; pour les transferts transfrontaliers de données personnelles, un enregistrement d'Évaluation de transfert international DOIT être complété et conservé dans le registre des preuves (incluant la base d'adéquation/CCT, la décision relative aux mesures supplémentaires et la référence d'approbation du DPD)
- Approbation du DPD pour les transferts de données personnelles

**Exigences techniques** :

- Chiffrement en transit obligatoire
- Vérification de conformité à la résidence des données
- Journalisation et surveillance des transferts

**Destinations interdites** :

- Pays soumis à des sanctions
- Juridictions sans protection juridique adéquate (sans garanties appropriées)

### Données clients et tierces

Traitement spécial pour les données appartenant à des tiers :

- Classification : CONFIDENTIEL au minimum pour toutes les données clients
- Transfert : Conformément aux exigences contractuelles clients
- Documentation : Journaux de transfert conservés conformément aux exigences contractuelles/réglementaires
- Notification : Informer les propriétaires des données des transferts lorsque requis par contrat

## Contrôles de transfert

### Autorisation

**Matrice d'autorisation des transferts** :

| Classification | Transfert interne | Transfert externe |
|----------------|-------------------|-------------------|
| PUBLIC | Auto-autorisé | Auto-autorisé |
| INTERNE | Auto-autorisé | Approbation du responsable hiérarchique |
| CONFIDENTIEL | Approbation du responsable hiérarchique | Propriétaire de l'information + responsable hiérarchique |
| RESTREINT | Responsable de département | Responsable de département + RSSI |

### Journalisation et traçabilité

Tous les transferts CONFIDENTIELS et RESTREINTS DOIVENT être journalisés :

**Contenu du journal** :

- Date/heure du transfert
- Identification de l'expéditeur et du destinataire
- Description de l'information (pas le contenu)
- Méthode de transfert utilisée
- Référence d'autorisation

**Conservation** : Les journaux de transfert sont conservés pendant 2 ans au minimum.

### Réponse aux incidents

En cas d'échec de transfert ou de compromission suspectée :

- Notification immédiate au RSSI pour les niveaux CONFIDENTIEL+
- Enquête conformément à ISMS-POL-A.5.24-28 (Gestion des incidents)
- Notification au propriétaire des données/propriétaire de l'information
- Les notifications réglementaires et contractuelles pour les violations de données personnelles DOIVENT être gérées via le processus de gestion des incidents (ISMS-POL-A.5.24-28) et la procédure de notification des violations de la vie privée de l'organisation, sur la base des décisions d'applicabilité de ISMS-POL-00

---

# Rôles et responsabilités

## Matrice d'imputabilité

| Rôle | Responsabilités en matière de transfert |
|------|----------------------------------------|
| **Direction générale** | Approuver la politique de transfert, autoriser les transferts externes RESTREINTS |
| **RSSI** | Définir les exigences de transfert, approuver les plateformes de transfert, superviser les incidents |
| **Exploitation informatique** | Mettre en œuvre l'infrastructure de transfert sécurisé, gérer les plateformes |
| **Propriétaires de l'information** | Autoriser les transferts d'informations dont ils sont propriétaires, vérifier l'adéquation des destinataires |
| **Responsables de département** | Approuver les transferts départementaux, assurer la conformité |
| **Tout le personnel** | Utiliser les méthodes de transfert approuvées, protéger les informations lors du transfert |

## Chemin d'escalade

- Incertitude sur la méthode de transfert : Personnel → Responsable hiérarchique → RSSI
- Approbation de transfert externe : Propriétaire de l'information → Responsable de département → RSSI (RESTREINT)
- Incident de transfert : Personnel → RSSI → Direction générale (incidents significatifs)

---

# Gouvernance et conformité

## Cadre d'évaluation

| Évaluation | Fréquence | Responsable | Preuve |
|------------|-----------|-------------|--------|
| Revue de sécurité de la plateforme de transfert | Trimestrielle | Exploitation informatique | Rapports de plateforme |
| Efficacité des politiques DLP | Mensuelle | RSSI | Rapports DLP |
| Conformité des transferts transfrontaliers | Trimestrielle | DPD | Registres de conformité |
| Inventaire des accords de transfert | Annuel | Conseil juridique | Registre des accords |

**Indicateurs de gouvernance** :

- Utilisation des méthodes de transfert approuvées (cible : 100 %)
- Délai de correction des incidents DLP (cible : < 24 heures)
- Conformité des transferts transfrontaliers (cible : 100 %)
- Couverture des accords de transfert (cible : 100 % pour les relations continues)

## Révision de la politique

- **Fréquence** : Annuelle au minimum
- **Déclencheurs** : Nouvelles technologies de transfert, modifications réglementaires, incidents de sécurité
- **Réviseurs** : RSSI, DPD, Exploitation informatique, Conseil juridique
- **Approbation** : Direction générale

## Gestion des exceptions

**Exceptions autorisées** :

- Méthode de transfert alternative lorsque la méthode approuvée est indisponible (avec contrôles compensatoires)
- Transferts d'urgence avec documentation post-facto dans les 24 heures
- Transferts via systèmes hérités avec plan de mitigation documenté

**Processus d'exception** :

1. Demander une exception avec justification commerciale
2. Évaluation du risque de la méthode alternative
3. Documenter les contrôles compensatoires
4. Approbation du RSSI requise pour les niveaux CONFIDENTIEL+
5. Approbation limitée dans le temps (90 jours maximum)

**Non autorisé** :

- Transfert d'informations RESTREINTES via des canaux non approuvés
- Transferts transfrontaliers sans base légale
- Utilisation persistante de méthodes de transfert non sécurisées

Toutes les exceptions DOIVENT être enregistrées dans le registre des exceptions (ISMS-REG-EXCEPTIONS).

## Lien avec les actions correctives

Les non-conformités liées à la présente politique (par exemple, méthodes de transfert non approuvées, accords manquants, violations transfrontalières) DOIVENT être enregistrées et gérées via le processus d'action corrective du SMSI (Clause 10.2) avec analyse des causes profondes et suivi des mesures correctives.

---

# Mise en œuvre et références

## Intégration au SMSI

La présente politique s'intègre au Système de management de la sécurité de l'information de [Organisation] :

**Appréciation du risque** (ISO 27001 Clause 6.1) :

- Les contrôles de transfert sélectionnés sur la base de l'appréciation du risque de [Organisation]
- La classification de l'information détermine les exigences minimales de sécurité des transferts
- Les plans de traitement du risque documentent la mise en œuvre des contrôles de transfert

**Déclaration d'applicabilité (DdA)** (ISO 27001 Clause 6.1.3) :

- L'applicabilité du contrôle A.5.14 est justifiée dans la DdA de [Organisation]
- Le statut de mise en œuvre est suivi et rapporté

**Contrôles connexes** :

- A.5.12-13 (Classification et étiquetage de l'information) : Détermine les exigences de sécurité des transferts
- A.5.19-23 (Services en nuage) : Exigences des plateformes de transfert en nuage
- A.6.6 (Accords de confidentialité et de non-divulgation) : Accords de transfert externe
- A.8.24 (Utilisation de la cryptographie) : Normes de chiffrement pour les transferts
- A.8.12 (Prévention des fuites de données) : Contrôles DLP pour la surveillance des transferts
- A.8.15 (Journalisation) : Exigences de journalisation de l'activité de transfert

**Intégration des contrôles empilés** :

A.5.14 (Transfert d'informations) s'articule avec les contrôles connexes pour assurer une protection complète :

| Contrôle empilé | Point d'intégration | Contribution de A.5.14 |
|-----------------|---------------------|------------------------|
| **A.5.12-13** (Classification) | Traitement basé sur la classification | A.5.14 spécifie les méthodes de transfert par niveau de classification |
| **A.8.24** (Cryptographie) | Chiffrement en transit | A.5.14 rend le chiffrement obligatoire ; A.8.24 spécifie les algorithmes |
| **A.8.12** (DLP) | Inspection du contenu | A.5.14 définit les canaux de transfert ; A.8.12 surveille les violations de politique |

L'évaluation de A.5.14 devrait référencer les évaluations des contrôles empilés pour une couverture complète.

## Ressources de mise en œuvre

**Structure des documents de mise en œuvre** (Suite ISMS-IMP-A.5.14) :

| Identifiant du document | Titre | Objet |
|-------------------------|-------|-------|
| **ISMS-IMP-A.5.14-UG/TG** | Guide de mise en œuvre — Transfert d'informations | Procédures détaillées pour le transfert sécurisé d'informations |

**Références croisées** :

- ISMS-POL-A.8.24 pour les exigences cryptographiques
- ISMS-POL-A.5.12-13 pour les exigences de classification
- ISMS-IMP-A.5.14 pour les procédures détaillées de transfert

---

# Preuves pour cette politique

**Preuves d'étape 1 (revue de la documentation) :**

Les preuves requises à l'étape 1 comprennent :

- ✅ Ce document de politique (ISMS-POL-A.5.14 v1.0)
- ✅ Approbation enregistrée par le RSSI, le DSI, la direction générale
- ✅ Preuve de communication aux rôles concernés
- ✅ Méthodes de transfert approuvées définies (Exigences relatives aux méthodes de transfert)
- ✅ Exigences de transfert externe documentées (Exigences de transfert externe)
- ✅ Exigences de transfert transfrontalier spécifiées (Transferts transfrontaliers)
- ✅ Matrice d'autorisation des transferts définie (Contrôles de transfert)
- ✅ Rôles et responsabilités attribués (Rôles et responsabilités)

Le statut des preuves est suivi dans le registre des preuves du SMSI.

**Preuves d'étape 2 (efficacité opérationnelle) :**

Preuves requises pour démontrer l'efficacité opérationnelle de la présente politique :

- Journaux de transfert pour les transferts CONFIDENTIELS/RESTREINTS
- Exemples d'accords de transfert externe (expurgés)
- Rapports d'incidents DLP et mesures correctives
- Journaux d'accès à la plateforme de partage de fichiers sécurisée
- Rapports de la passerelle de messagerie sécurisée (application TLS)
- Documentation des transferts transfrontaliers (CCT, évaluations d'adéquation)
- Registres de formation aux procédures de transfert
- Registre des exceptions avec approbations

---

# Définitions

| Terme | Définition |
|-------|------------|
| **Transfert d'informations** | Le déplacement d'informations d'un emplacement, système ou individu vers un autre par tout moyen |
| **Installation de transfert** | Toute technologie, équipement ou service utilisé pour transmettre des informations (systèmes de messagerie, partage de fichiers, coursiers, etc.) |
| **Transfert transfrontalier** | Transfert d'informations vers un destinataire dans un pays ou une juridiction différents |
| **Clauses contractuelles types (CCT)** | Clauses contractuelles approuvées par la Commission de l'UE pour les transferts internationaux de données |
| **Chaîne de contrôle** | Enregistrement documenté de tous les individus ayant traité des informations lors d'un transfert physique |
| **Chiffrement de bout en bout** | Chiffrement permettant uniquement à l'expéditeur et au destinataire prévu de déchiffrer les informations |

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

*La présente politique établit les exigences en matière de transfert d'informations. Les procédures de mise en œuvre sont documentées dans ISMS-IMP-A.5.14 (UG/TG).*

<!-- QA_VERIFIED: 2026-03-30 -->
