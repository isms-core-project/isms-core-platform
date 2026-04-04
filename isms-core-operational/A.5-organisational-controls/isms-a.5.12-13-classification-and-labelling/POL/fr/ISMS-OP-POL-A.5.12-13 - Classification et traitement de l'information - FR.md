<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.5.12-13-FR:operational:OP-POL:a.5.12-13 -->
**ISMS-OP-POL-A.5.12-13 — Classification et traitement de l'information**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Classification et traitement de l'information |
| **Type de document** | Politique opérationnelle |
| **Identifiant du document** | ISMS-OP-POL-A.5.12-13 |
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

- ISO/IEC 27001:2022 Contrôles A.5.12, A.5.13 — Classification de l'information, étiquetage de l'information

**Contrôles Annexe A connexes** :

| Contrôle | Relation avec la classification de l'information |
|----------|--------------------------------------------------|
| A.5.9 Inventaire des informations et des actifs associés | Classification assignée aux actifs informationnels inventoriés |
| A.5.10 Utilisation acceptable de l'information | Les règles d'utilisation acceptable appliquent les exigences de traitement par niveau de classification |
| A.5.14 Transfert de l'information | La méthode de transfert est déterminée par le niveau de classification |
| A.5.15–18 Contrôle d'accès et gestion des identités | Les droits d'accès sont accordés selon la classification et le besoin d'en connaître |
| A.5.33 Protection des enregistrements | La conservation et la protection des enregistrements sont alignées sur la classification |
| A.5.34 Protection de la vie privée et des DCP | Classification des données personnelles et exigences de traitement |
| A.7.10 Supports de stockage | Traitement et élimination des supports selon la classification |
| A.7.14 Mise hors service ou réutilisation sécurisée des équipements | Les normes d'élimination sont déterminées par la classification |
| A.8.10 Suppression de l'information | Normes de suppression sécurisée par niveau de classification |
| A.8.11 Masquage des données | Masquage des données classifiées dans les environnements hors production |
| A.8.12 Prévention des fuites de données | Les contrôles DLP appliquent les règles de traitement selon la classification |
| A.8.24 Utilisation de la cryptographie | Les exigences de chiffrement sont déterminées par la classification |

**Politiques internes connexes** :

- Politique de gestion des actifs
- Politique de contrôle d'accès
- Politique de transfert de l'information
- Politique d'utilisation de la cryptographie
- Politique de protection de la vie privée et des DCP
- Politique d'utilisation acceptable

---

# Politique de classification et de traitement de l'information

## Objet

L'objet de cette politique est d'assurer la classification et le traitement corrects de l'information en fonction de sa sensibilité, de sa valeur et des exigences légales, afin que l'information bénéficie d'un niveau de protection approprié tout au long de son cycle de vie.

Cette politique soutient la nFADP suisse (LPD révisée) et l'Ordonnance sur la protection des données (DSV) en mettant en œuvre des mesures techniques et organisationnelles appropriées au risque pour protéger les données personnelles (y compris les données personnelles sensibles) par des contrôles basés sur la classification. Là où l'organisation traite des données de personnes résidant dans l'UE/EEE, les exigences du RGPD s'appliquent également.

## Périmètre

Tous les employés et utilisateurs tiers.

Toutes les informations sous quelque format que ce soit (numérique, physique, verbal) faisant partie des systèmes et applications considérés comme dans le périmètre par la déclaration de périmètre ISO 27001.

## Principe

L'information doit être classifiée en fonction des exigences légales, de sa valeur, de sa criticité et de sa sensibilité à la divulgation ou à la modification non autorisée. La classification détermine les contrôles de traitement appliqués tout au long du cycle de vie de l'information — de la création au stockage, en passant par la transmission et la destruction.

---

## Schéma de classification

L'information doit être classifiée dans l'un des trois niveaux suivants :

| Niveau | Description | Impact d'une divulgation non autorisée |
|--------|-------------|----------------------------------------|
| **CONFIDENTIEL** | Informations dont la divulgation causerait un préjudice significatif à l'organisation, à ses clients ou aux personnes concernées. Inclut les données légalement protégées. | Pertes financières graves, sanctions réglementaires, actions en justice, dommages réputationnels significatifs, risque élevé pour les personnes concernées |
| **INTERNE** | Informations destinées à un usage interne à l'organisation. Non destinées à la divulgation publique. | Gêne opérationnelle mineure, embarras mineur, impact réputationnel limité |
| **PUBLIC** | Informations approuvées pour la publication publique. La divulgation ne cause aucun préjudice. | Aucun impact négatif |

**Classification par défaut** : Les informations qui n'ont pas été explicitement classifiées doivent être traitées comme **INTERNES** jusqu'à leur classification par leur propriétaire.

### Classification par type d'information

| Type d'information | Classification minimale |
|-------------------|------------------------|
| **Données personnelles sensibles** (art. 5 nFADP : santé, origine raciale/ethnique, opinions religieuses/politiques, casiers judiciaires, données génétiques, données biométriques) | **CONFIDENTIEL** |
| **Données personnelles** (noms, adresses e-mail, numéros de téléphone, dossiers des employés) | **INTERNE** (minimum) ; **CONFIDENTIEL** si volume > 1 000 enregistrements ou combinées avec des catégories sensibles |
| **Dossiers financiers** (comptes, transactions, informations salariales, coordonnées bancaires) | **CONFIDENTIEL** |
| **Secrets commerciaux et propriété intellectuelle** (méthodes propriétaires, code source, designs, formules) | **CONFIDENTIEL** |
| **Mots de passe, clés cryptographiques, identifiants** | **CONFIDENTIEL** |
| **Contrats et accords juridiques** | **CONFIDENTIEL** |
| **Politiques internes, procédures, procès-verbaux** | **INTERNE** |
| **Organigrammes, communications internes** | **INTERNE** |
| **Supports marketing, communiqués de presse, contenu publié** | **PUBLIC** |
| **Informations déjà dans le domaine public** | **PUBLIC** |

### Responsabilités de classification

- Les **propriétaires d'informations** (tels que définis dans la Politique de gestion des actifs) sont responsables de la classification de leurs actifs informationnels.
- La classification doit être assignée lors de la création ou de la réception de l'information.
- La classification doit être révisée lorsque l'information est significativement modifiée, partagée avec de nouvelles parties ou lorsque les circonstances commerciales changent.
- La sur-classification doit être évitée — classifier tout comme CONFIDENTIEL dilue le sens et gaspille des ressources.
- **Risque d'agrégation** : Les informations classifiées individuellement comme INTERNES peuvent nécessiter une reclassification en CONFIDENTIEL lorsqu'elles sont combinées avec d'autres jeux de données, si l'agrégation crée un risque de préjudice matériellement plus élevé (p. ex., combinaison de noms avec des conditions de santé, ou combinaison de registres de salaires individuels en un rapport de rémunération à l'échelle du département). Les propriétaires d'informations doivent prendre en compte le risque d'agrégation lors de la classification des jeux de données.

---

## Étiquetage de l'information

### Exigences d'étiquetage

Toutes les informations doivent être étiquetées conformément à leur niveau de classification :

| Format | Méthode d'étiquetage |
|--------|---------------------|
| **Documents numériques** (Word, PDF, Excel) | Classification dans l'en-tête ou le pied de page du document sur chaque page (p. ex., « CONFIDENTIEL ») |
| **E-mail** | Préfixe de classification dans l'objet (p. ex., « [CONFIDENTIEL] Objet ») |
| **Documents physiques** | Classification sur la page de couverture ; en-tête ou pied de page sur les pages suivantes |
| **Supports physiques** (clés USB, bandes de sauvegarde) | Étiquette physique apposée sur l'appareil ou le contenant |
| **Métadonnées de fichier** | Classification enregistrée dans les propriétés du fichier ou les métadonnées du système de gestion documentaire |
| **Enregistrements de base de données** | Colonne de classification ou balise de métadonnées par jeu de données |

Les informations **PUBLIC** ne nécessitent pas d'étiquette de classification à moins d'être publiées sur des plateformes internes où leur statut public pourrait être ambigu.

Les **informations non étiquetées** doivent être traitées comme **INTERNES** par défaut.

Lorsque l'organisation utilise Microsoft 365 ou des plateformes équivalentes, des étiquettes de sensibilité doivent être configurées pour automatiser l'application de la classification, y compris le chiffrement, les restrictions d'accès et les marquages visuels.

---

## Traitement de l'information

### Matrice de traitement

| Aspect de traitement | PUBLIC | INTERNE | CONFIDENTIEL |
|---------------------|--------|---------|-------------|
| **Stockage numérique** | Aucune restriction | Systèmes gérés par l'organisation uniquement ; pas sur des appareils personnels sans MDM | Chiffré au repos (AES-256) ; dossiers à accès contrôlé ; pas de supports amovibles sans chiffrement |
| **Stockage physique** | Aucune restriction | Locaux de l'organisation ; archivage standard | Armoires verrouillées ou salles à accès restreint ; bureau propre imposé |
| **Transmission par e-mail** | Aucune restriction | E-mail interne ou chiffrement externe | E-mail chiffré obligatoire ; mot de passe/clé de déchiffrement via canal séparé |
| **Transfert de fichiers** | Aucune restriction | Plateformes de partage de fichiers approuvées uniquement | Transfert chiffré uniquement (SFTP, HTTPS) ; aucun service cloud non approuvé |
| **Transfert physique** | Aucune restriction | Enveloppe cachetée ; courrier interne | Emballage inviolable ; coursier approuvé avec suivi ; confirmation du destinataire |
| **Partage — interne** | Sans restriction | Au sein de l'organisation | Sur la base du besoin d'en connaître avec approbation documentée du propriétaire de l'information |
| **Partage — externe** | Sans restriction | NDA requis ; canaux approuvés | NDA + autorisation spécifique du propriétaire de l'information ; accord de transfert si requis |
| **Impression** | Aucune restriction | Récupérer rapidement ; pas d'impressions abandonnées | Impression sécurisée avec déblocage (badge/PIN) ; récupération immédiate |
| **Stockage cloud** | Services approuvés | Services approuvés ; données en Suisse ou pays adéquat | Services approuvés ; données de préférence en Suisse ; chiffrement avec clés gérées par l'organisation |
| **Appareils mobiles** | Aucune restriction | Appareils inscrits au MDM de l'organisation uniquement | Inscrits au MDM ; chiffrement de l'appareil ; capacité d'effacement à distance |
| **Sauvegarde** | Sauvegarde standard | Sauvegarde chiffrée | Sauvegarde chiffrée ; accès restreint à la restauration |

### Stockage de l'information

Les informations de l'organisation ne doivent pas être stockées sur des équipements personnels, des comptes e-mail personnels ou des services cloud personnels à moins d'être approuvées par le RSSI et enregistrées dans un registre approuvé.

Les informations de l'organisation doivent être protégées par des contrôles d'accès tels que définis dans la Politique de contrôle d'accès.

Les informations confidentielles doivent être chiffrées au repos et en transit lorsqu'elles sont stockées sur ou transmises à travers tout système, conformément à la Politique d'utilisation de la cryptographie.

Les informations confidentielles et internes ne doivent pas être stockées ou traitées dans des environnements de développement ou de test à moins que les données n'aient été masquées, anonymisées ou pseudonymisées. Lorsque des données de production doivent être utilisées dans des environnements hors production, l'approbation du propriétaire de l'information et du RSSI est requise, et les données doivent être traitées au même niveau de classification qu'en production.

Lorsque l'organisation déploie des outils de Prévention des fuites de données (DLP), les politiques DLP doivent être alignées sur le schéma de classification pour détecter et prévenir le transfert ou la divulgation non autorisé des informations CONFIDENTIELLES (p. ex., blocage de l'envoi par e-mail externe de fichiers étiquetés CONFIDENTIEL, prévention du téléchargement vers des services cloud non sanctionnés).

### Traitement des informations verbales

Les informations confidentielles discutées verbalement (en réunions, appels téléphoniques ou conversations) doivent être traitées avec le soin approprié :

- Les discussions sur les informations confidentielles doivent se tenir dans des espaces privés (bureaux fermés, salles de réunion avec portes fermées) — et non dans des zones ouvertes, des espaces publics ou dans les transports en commun.
- Les réunions virtuelles discutant d'informations confidentielles doivent utiliser des plateformes chiffrées avec un accès restreint aux participants autorisés.
- Les participants doivent être rappelés de la nature confidentielle de la discussion au début de la réunion.
- Les notes ou procès-verbaux des discussions confidentielles doivent être classifiés et traités en conséquence.

### Contrôle des appareils et des supports

Tous les supports électroniques et papier contenant des informations confidentielles doivent être physiquement sécurisés contre tout accès non autorisé en les rangeant dans des tiroirs verrouillés, des armoires ou des salles à accès restreint.

Les supports amovibles (clés USB, disques durs externes, bandes de sauvegarde) contenant des données confidentielles doivent être chiffrés et enregistrés dans l'inventaire des actifs, conformément à la Politique de gestion des actifs.

### Sauvegarde de l'information

Les informations de l'organisation doivent être sauvegardées, conservées et testées conformément au calendrier de sauvegarde. Les sauvegardes doivent être chiffrées à l'aide d'un chiffrement fort. Toutes les sauvegardes doivent être stockées dans des emplacements sécurisés avec un accès restreint au personnel autorisé.

---

## Destruction de l'information

Lorsque l'information n'est plus nécessaire et que sa durée de conservation est expirée, elle doit être détruite de manière sécurisée selon son niveau de classification.

### Destruction des documents papier

| Classification | Norme de destruction |
|---------------|---------------------|
| **CONFIDENTIEL** | Déchiquetage en coupe croisée selon DIN 66399 Niveau de sécurité P-4 ou supérieur, ou placement dans des bacs à déchets confidentiels approuvés gérés par un prestataire de destruction certifié |
| **INTERNE** | Déchiquetage en coupe croisée selon DIN 66399 Niveau de sécurité P-3 ou supérieur, ou bacs à déchets confidentiels approuvés |
| **PUBLIC** | Recyclage standard ou déchets généraux |

### Destruction de l'information électronique

| Classification | Norme de destruction |
|---------------|---------------------|
| **CONFIDENTIEL** | Effacement cryptographique (destruction de la clé de chiffrement) ou réécriture conforme NIST SP 800-88 ; vérification de l'effacement documentée |
| **INTERNE** | Suppression sécurisée (réécriture) ; désinfection standard des supports |
| **PUBLIC** | Suppression standard |

Les journaux d'effacement doivent être maintenus lorsque l'outil de désinfection le permet.

### Destruction des supports et appareils électroniques

Les supports et appareils électroniques ayant stocké des informations confidentielles ou internes doivent être détruits par des méthodes approuvées lorsqu'ils ne sont plus nécessaires :

- **SSD et stockage flash** : Effacement cryptographique (ATA Secure Erase) ou destruction physique.
- **Disques durs** : Réécriture conforme NIST SP 800-88 ou destruction physique (démagnétisation, déchiquetage).
- **Bandes de sauvegarde** : Démagnétisation ou destruction physique.
- **Supports optiques** : Déchiquetage physique.

La destruction des supports confidentiels doit être effectuée par des fournisseurs tiers spécialisés approuvés lorsque la destruction interne n'est pas réalisable. Des certificats de destruction doivent être obtenus et conservés comme preuves.

Un inventaire des appareils, y compris ceux détruits, doit être maintenu conformément à la Politique de gestion des actifs.

---

## Reclassification

La classification de l'information n'est pas permanente. L'information doit être reclassifiée lorsque :

- La sensibilité ou la valeur de l'information change.
- Les exigences légales ou réglementaires changent.
- Une obligation contractuelle expire (p. ex., la durée d'un NDA prend fin).
- L'information est approuvée pour la publication publique.
- Le propriétaire de l'information détermine que la classification actuelle n'est plus appropriée.

La reclassification doit être effectuée par le propriétaire de l'information et l'étiquetage mis à jour en conséquence.

---

## Preuves

Les preuves suivantes démontrent la conformité à cette politique :

- **Documentation du schéma de classification** (cette politique) — *révisée annuellement*
- **Exemples de documents classifiés** montrant un étiquetage correct (en-têtes, pieds de page, préfixes d'e-mail) — *échantillon de 5 à 10 documents par niveau de classification collecté lors de l'audit annuel*
- **Preuves de mise en œuvre de la matrice de traitement** (contrôles d'accès, paramètres de chiffrement, restrictions de partage) — *captures d'écran de configuration système ou exportations d'audit ; révisées annuellement*
- **Enregistrements de destruction des supports confidentiels** (certificats de destruction, journaux d'effacement) — *conservés 5 ans ; réconciliés annuellement avec les enregistrements d'élimination des actifs*
- **Registre des actifs informationnels** montrant les assignations de classification (conformément à la Politique de gestion des actifs) — *cible : 100 % des actifs informationnels classifiés ; mesuré annuellement*
- **Enregistrements de formation** montrant les employés formés aux exigences de classification et de traitement — *formation annuelle de sensibilisation ; achèvement suivi*
- **Enregistrements d'exceptions** pour tout écart par rapport aux règles de traitement — *révisés trimestriellement ; présentés lors de la révision de direction*
- **Configuration des politiques DLP et rapports d'incidents** (si DLP déployé) — *révisés trimestriellement*

---

# Conformité à la politique

## Mesure de la conformité

L'équipe de gestion de la sécurité de l'information vérifiera la conformité à cette politique par diverses méthodes, notamment l'échantillonnage de documents pour vérifier l'étiquetage correct, les audits de contrôle d'accès, les enregistrements de destruction des supports, les audits internes et externes, et les retours d'information au propriétaire de la politique.

## Exceptions

Toute exception à cette politique doit être approuvée et consignée par le Responsable de la sécurité de l'information à l'avance, avec une acceptation documentée des risques, des contrôles compensatoires et une date de révision définie. Les exceptions doivent être rapportées à l'équipe de Révision de direction.

## Non-conformité

Un employé reconnu coupable d'avoir enfreint cette politique peut faire l'objet de mesures disciplinaires, pouvant aller jusqu'au licenciement.

## Amélioration continue

Cette politique est révisée et mise à jour dans le cadre du processus d'amélioration continue. Les révisions doivent prendre en compte les changements des normes de classification, les exigences réglementaires (notamment les évolutions de la nFADP suisse et du RGPD), les risques émergents en matière de protection des données et les enseignements tirés des incidents.

---

# Périmètre de la norme ISO 27001 couvert

Politique de classification et de traitement de l'information — Cartographie des contrôles ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership et engagement | 5.1 Politiques de sécurité de l'information |
| Clause 5.2 Politique | 5.4 Responsabilités de la direction |
| Clause 6.2 Objectifs de sécurité de l'information | 5.36 Conformité aux politiques, règles et normes |
| Clause 7.3 Sensibilisation | **5.12 Classification de l'information** |
| Clause 7.5.2 Création et mise à jour de la documentation | **5.13 Étiquetage de l'information** |
| Clause 7.5.3 Contrôle des informations documentées | 6.3 Sensibilisation, formation et éducation à la sécurité de l'information |
| | 6.4 Processus disciplinaire |
| | 7.10 Supports de stockage |
| | 7.14 Mise hors service ou réutilisation sécurisée des équipements |
| | 8.10 Suppression de l'information |
| | 8.11 Masquage des données |

**Cadre réglementaire et juridique** :

| Cadre | Pertinence |
|-------|-----------|
| nFADP suisse (LPD révisée) | Art. 5 — Définition des données personnelles sensibles (correspond à CONFIDENTIEL) ; art. 8 — Mesures techniques et organisationnelles |
| DSV suisse (Ordonnance sur la protection des données) | Art. 1-3 — Exigences minimales pour la sécurité des données |
| RGPD UE (le cas échéant) | Art. 5 — Principes de protection des données ; art. 9 — Catégories particulières de données personnelles ; art. 32 — Sécurité du traitement |
| ISO/IEC 27001:2022 | Contrôles Annexe A 5.12, 5.13 |
| ISO/IEC 27002:2022 | Sections 5.12, 5.13 — Conseils d'implémentation |
| NIST SP 800-53 Rév. 5 | RA-2 (Catégorisation de la sécurité), AC-16 (Attributs de sécurité et de protection de la vie privée), MP-3 (Marquage des supports), MP-6 (Désinfection des supports) |
| CIS Controls v8 | Contrôle 3 (Protection des données — y compris la classification, le chiffrement, l'élimination) |

---

<!-- QA_VERIFIED: 2026-03-29 -->
