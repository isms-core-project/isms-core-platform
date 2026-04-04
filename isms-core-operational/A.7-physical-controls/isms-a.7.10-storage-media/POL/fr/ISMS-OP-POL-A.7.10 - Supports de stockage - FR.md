<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.7.10-FR:operational:OP-POL:a.7.10 -->
**ISMS-OP-POL-A.7.10 — Supports de stockage**

---

**Contrôle documentaire**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Supports de stockage |
| **Type de document** | Politique opérationnelle |
| **Identifiant du document** | ISMS-OP-POL-A.7.10 |
| **Créateur du document** | Responsable de la sécurité de l'information (RSSI) |
| **Propriétaire du document** | Directeur général (DG) |
| **Approuvé par** | Direction générale |
| **Date de création** | [Date] |
| **Version** | 0.1 |
| **Date de version** | [Date] |
| **Classification** | Interne |
| **Statut** | Brouillon |

**Historique des versions** :

| Version | Date | Auteur | Modifications |
|---------|------|--------|---------------|
| 0.1 | [Date] | RSSI | Politique opérationnelle initiale pour ISO 27001:2022 |

**Cycle de révision** : Annuel
**Prochaine date de révision** : [Date d'entrée en vigueur + 12 mois]

**Approuvé par** : [RSSI / Direction générale]

**Documents associés** :

- ISO/IEC 27001:2022 Contrôle A.7.10 — Supports de stockage
- ISO/IEC 27002:2022 Section 7.10 — Recommandations de mise en œuvre
- NIST SP 800-88 Rev. 2 — Lignes directrices pour l'assainissement des supports (septembre 2025)
- IEEE 2883:2022 — Norme pour l'assainissement des supports de stockage
- DIN 66399 — Destruction des supports de données (niveaux de sécurité et catégories de supports)
- nLPD suisse (revDSG) — Loi fédérale sur la protection des données
- OPDo suisse (Ordonnance sur la protection des données) — Art. 1-3 (exigences minimales de sécurité des données)

**Contrôles Annexe A associés** :

| Contrôle | Relation avec les supports de stockage |
|----------|----------------------------------------|
| A.5.9 Inventaire des informations et autres actifs associés | Registre des actifs incluant l'inventaire des supports de stockage |
| A.5.10-11 Utilisation acceptable et restitution des actifs | Règles d'utilisation acceptable et restitution des supports lors du départ |
| A.5.12-13 Classification et étiquetage des informations | Le niveau de classification détermine les exigences de manipulation, stockage et mise au rebut |
| A.7.6-7-14 Zones sécurisées, bureau propre, mise au rebut sécurisée | Sécurité physique des zones de stockage ; méthodes de mise au rebut des équipements contenant des supports |
| A.8.10 Suppression des informations | Exigences de suppression logique complémentaires à l'assainissement physique des supports |
| A.8.24 Utilisation de la cryptographie | Normes de chiffrement pour la protection des supports au repos et en transit |

**Politiques internes associées** :

- Politique de classification et de gestion des informations
- Politique sur les zones sécurisées et la gestion des supports
- Politique de gestion des actifs
- Politique de sécurité des postes de travail
- Politique d'utilisation de la cryptographie

---

# Politique sur les supports de stockage

## Objet

L'objet de cette politique est de garantir que tous les supports de stockage sont gérés de manière sécurisée tout au long de leur cycle de vie — de l'acquisition et l'enregistrement, en passant par l'utilisation et le transport, jusqu'à la mise au rebut ou la réutilisation — conformément au schéma de classification des informations de l'organisation et aux exigences réglementaires applicables.

Cette politique soutient la nLPD suisse (revDSG) art. 8 en mettant en œuvre des mesures techniques et organisationnelles proportionnées au risque pour protéger les données personnelles (y compris les données personnelles sensibles) stockées sur des supports physiques et numériques. Lorsque l'organisation traite des données de personnes dans l'UE/EEE, les exigences du RGPD s'appliquent également. Les deux cadres exigent que les données personnelles sur les supports de stockage soient rendues irrécupérables avant leur mise au rebut ou leur réutilisation.

Le contrôle A.7.10 couvre un seul contrôle de l'Annexe A, mais son périmètre s'étend à l'ensemble du cycle de vie des supports : acquisition, enregistrement, utilisation, transfert de données, transport, stockage sécurisé, réutilisation et mise au rebut. Cette politique combine les exigences de politique et les recommandations opérationnelles suffisantes pour qu'une PME puisse mettre en œuvre et démontrer sa conformité.

## Champ d'application

Tous les employés, prestataires et utilisateurs tiers qui manipulent, accèdent ou sont responsables de supports de stockage contenant des informations de l'organisation.

**Types de supports dans le périmètre** :

- Supports amovibles numériques : clés USB, disques durs externes, cartes SD/microSD, supports optiques (CD, DVD, Blu-ray)
- Stockage fixe : disques durs internes (HDD), disques SSD, disques NVMe
- Supports de sauvegarde et d'archivage : bandes LTO, cartouches DAT/DLT, cartouches RDX
- Stockage d'appareils mobiles : smartphones, tablettes et appareils avec stockage intégré
- Stockage cloud et virtuel : sauvegarde cloud, stockage de fichiers cloud, images de disques de machines virtuelles
- Supports papier et analogiques : documents imprimés, microfilms, microfiches, supports photographiques

**Phases du cycle de vie couvertes** : Acquisition, enregistrement, utilisation, transfert de données, transport, stockage, réutilisation et mise au rebut.

**Hors champ d'application** :

- Définitions du schéma de classification des informations (voir Politique de classification et de gestion des informations, A.5.12-13)
- Contrats avec les fournisseurs de services cloud et gestion des prestataires tiers (voir Politique de services cloud, A.5.19-23)
- Sélection des algorithmes cryptographiques et détails de la gestion des clés (voir Politique d'utilisation de la cryptographie, A.8.24)

## Principe

L'ISO/IEC 27001:2022 Annexe A.7.10 stipule :

> *Les supports de stockage devraient être gérés tout au long de leur cycle de vie d'acquisition, d'utilisation, de transport et de mise au rebut conformément au schéma de classification et aux exigences de manipulation de l'organisation.*

Les supports de stockage doivent être gérés de manière proportionnée à la sensibilité des informations qu'ils contiennent ou ont contenu. Le niveau de classification le plus élevé des données jamais stockées sur un support détermine les exigences de manipulation et de mise au rebut, indépendamment du fait que ces données aient depuis été supprimées.

Tous les supports de stockage contenant des informations de l'organisation doivent être enregistrés, suivis et protégés. La mise au rebut doit rendre les données irrécupérables en utilisant des méthodes conformes aux normes NIST SP 800-88 Rev. 2 et DIN 66399, adaptées au type de support et à la classification des informations.

Les supports amovibles personnels ne doivent pas être utilisés pour les données de l'organisation. Seuls les supports approuvés par l'organisation et chiffrés sont autorisés.

---

## Gestion des supports amovibles

### Autorisation et enregistrement

L'utilisation de supports de stockage amovibles doit être autorisée avant le déploiement :

- Les employés doivent obtenir l'autorisation de leur responsable hiérarchique avant d'utiliser tout support de stockage amovible pour les données de l'organisation. L'autorisation doit préciser le cas d'utilisation autorisé, la classification des données et la durée (12 mois par défaut, 24 mois maximum).
- Tous les supports amovibles doivent être enregistrés dans [Système de gestion des actifs] avec les informations suivantes : type de support, capacité, numéro de série ou étiquette d'actif, utilisateur assigné, objectif, niveau de classification maximal des données à stocker et date d'expiration de l'autorisation.
- Seuls les supports amovibles émis par l'organisation ou approuvés par elle peuvent être utilisés pour les données de l'organisation. Les clés USB personnelles, disques durs externes ou autres dispositifs de stockage personnels ne doivent en aucun cas être utilisés pour des données CONFIDENTIELLES ou INTERNES.
- Les supports amovibles émis par l'organisation doivent être achetés auprès de fournisseurs agréés dans le cadre du processus d'approvisionnement de l'organisation. Les supports non approuvés ou d'origine inconnue ne doivent pas être connectés aux systèmes de l'organisation.

**Cycle de vie de l'autorisation** :
- 30 jours avant l'expiration : rappel automatique par e-mail à l'employé et au responsable hiérarchique depuis [Système de gestion des actifs]
- À l'expiration : statut du support changé en « Expiré » dans le système
- Si le support n'est pas renouvelé ou restitué dans les 15 jours suivant l'expiration : l'exploitation informatique contacte l'employé pour retour ou renouvellement
- Renouvellement : l'employé soumet une demande de renouvellement avec justification commerciale continue ; le responsable hiérarchique approuve (maximum 24 mois par autorisation ; au-delà de 24 mois, re-justifier le besoin depuis le début)
- Retour : l'employé restitue le support à l'exploitation informatique ; le support est effacé de manière sécurisée conformément aux procédures de mise au rebut (même si le support doit être réémis — effacement entre utilisateurs) ; [Système de gestion des actifs] mis à jour
- Escalade pour support non restitué : retard de 15 jours → escalade au responsable hiérarchique ; retard de 30 jours → escalade au RSSI, support marqué « Manquant », enquête sur la perte initiée ; retard de 60 jours → considérer comme perdu/volé, déclencher la réponse aux incidents conformément à la procédure de support perdu
- Métriques : taux de conformité des autorisations de supports (% retournés ou renouvelés à temps) — cible > 95 % ; supports en retard (> 15 jours après expiration) — cible < 3 éléments ; signalés lors de la revue de direction trimestrielle

### Types de supports approuvés

L'organisation doit maintenir une liste des types de supports amovibles approuvés. Au minimum :

- **Clés USB** : chiffrées matériellement, émises par l'organisation uniquement (p. ex., [Modèle de clé USB chiffrée]). Le chiffrement logiciel uniquement est acceptable pour les données INTERNES lorsque les appareils à chiffrement matériel ne sont pas disponibles, sous réserve de l'approbation du RSSI et des contrôles compensatoires suivants :
  - Les données CONFIDENTIELLES requièrent un chiffrement matériel — aucune exception pour le chiffrement logiciel uniquement
  - Durée maximale de l'exception : 6 mois (renouvelable avec approbation du RSSI)
  - Outils logiciels approuvés : BitLocker To Go (Windows, AES-256), FileVault (macOS, AES-256), VeraCrypt (multiplateforme, AES-256)
  - Phrase de passe forte obligatoire : minimum 16 caractères, stockée dans [Gestionnaire de mots de passe]
  - Le support doit être chiffré avant la première utilisation (pas de chiffrement après que les données sont déjà écrites — risque de données non chiffrées résiduelles)
  - Surveillance renforcée : utilisation des supports chiffrés par logiciel enregistrée, révision mensuelle des modèles d'accès
  - Re-autorisation trimestrielle : l'utilisateur reconfirme le besoin commercial tous les 3 mois ; si le besoin prend fin, le support est restitué pour mise au rebut sécurisée
  - Migration vers le chiffrement matériel : les exceptions pour chiffrement logiciel doivent être progressivement abandonnées au fur et à mesure que les supports à chiffrement matériel deviennent disponibles (objectif : toutes les données INTERNES sur chiffrement matériel dans les 12 mois)
- **Disques durs externes** : modèles à chiffrement matériel AES-256 auprès de fournisseurs approuvés.
- **Supports optiques (CD/DVD/Blu-ray)** : émis par l'organisation, étiquetés avec la classification, la référence d'actif, la date d'écriture, la description du contenu et la date d'expiration de conservation. Supports inscriptibles une seule fois (CD-R, DVD-R, BD-R) obligatoires pour : l'archivage CONFIDENTIEL (documents juridiques, dossiers d'audit, relevés financiers), la préservation des preuves (images forensiques, preuves d'incidents, blocages légaux) et la conservation à long terme (> 5 ans). Supports réinscriptibles (CD-RW, DVD-RW, BD-RE) autorisés uniquement pour le transfert temporaire de données INTERNES et les données de test/développement (maximum 12 mois, puis destruction sécurisée). Stockage : boîtiers plastiques ou boîtiers minces (pas de pochettes papier — risque de rayures), orientation verticale (pas empilés à plat — risque de déformation), environnement frais et sec à l'abri du soleil. Planifier la migration vers de nouveaux supports à l'échéance de 5 ans pour les données de conservation à long terme.
- **Cartes SD/microSD** : autorisées uniquement pour des usages spécifiques approuvés (p. ex., appareils photo, systèmes embarqués). Doivent être chiffrées lorsque l'appareil le permet.

Les supports amovibles non chiffrés ne doivent pas être utilisés pour des données CONFIDENTIELLES. Les exceptions nécessitent une approbation documentée du RSSI avec des contrôles compensatoires et une limite de temps ne dépassant pas 6 mois.

### Maintenance de la liste des supports approuvés

La liste des supports approuvés doit être révisée et maintenue selon un cycle régulier :

- **Révision annuelle** : l'exploitation informatique et le RSSI révisent la liste des supports approuvés au T4
- **Révision déclenchée** : lorsqu'une nouvelle technologie de support devient disponible, qu'une vulnérabilité de sécurité est découverte dans un modèle actuellement approuvé, ou que les achats identifient un modèle abandonné

Critères de révision :
- Norme de chiffrement actuelle (AES-256 minimum pour CONFIDENTIEL, AES-128 minimum pour INTERNE)
- Chiffrement matériel préféré (FIPS 140-2 niveau 2 ou supérieur pour les supports CONFIDENTIELS)
- Statut du support fournisseur (support actif, mises à jour de sécurité disponibles)
- Rapport coût/efficacité (prix par Go, disponibilité pour achats groupés)
- Compatibilité avec les postes de l'organisation (Windows, macOS, Linux)

Processus d'approbation : l'exploitation informatique propose des ajouts ou suppressions avec évaluation technique ; le RSSI approuve les modifications ; les achats mettent à jour la liste des fournisseurs préférés ; la liste des supports approuvés est publiée sur l'intranet et communiquée à l'ensemble du personnel. La liste doit inclure la date de version et la prochaine date de révision.

### Audit trimestriel des supports

Un audit basé sur les risques des supports amovibles enregistrés doit être réalisé chaque trimestre :

**Périmètre d'audit par niveau de risque** :

| Niveau de risque | Critères | Échantillon trimestriel | Couverture annuelle |
|-----------------|----------|------------------------|---------------------|
| **Risque élevé** | Supports ayant stocké des données CONFIDENTIELLES (actuelles ou historiques) ; supports transportés hors site régulièrement ; supports assignés à des dirigeants ou utilisateurs à privilèges | Vérification à 100 % | 100 % par trimestre |
| **Risque moyen** | Supports avec données INTERNES uniquement ; utilisation en bureau uniquement | Échantillon rotatif à 50 % | 100 % sur 2 trimestres |
| **Risque faible** | Supports avec données PUBLIQUES uniquement ; supports en stockage d'archive sécurisé à long terme | Échantillon rotatif à 25 % | 100 % annuellement |

**Procédure d'audit** :
1. Générer une liste d'échantillons depuis [Système de gestion des actifs] en fonction du niveau de risque
2. Vérification physique : confirmer l'emplacement, le détenteur, le statut de chiffrement, le numéro de série correspond à l'enregistrement
3. Contrôle ponctuel du chiffrement : tester aléatoirement 10 % des supports échantillonnés (tentative d'accès sans mot de passe/clé de chiffrement)
4. Documenter les résultats : rapport de réconciliation avec les constatations, divergences et actions de suivi

**Escalade des constatations** :
- Support à risque élevé manquant : escalade immédiate au RSSI (le jour même) ; considérer comme perdu/volé ; déclencher l'évaluation d'une violation selon la procédure de réponse aux incidents pour support perdu
- Support à risque moyen manquant : escalade dans les 2 jours ouvrables ; enquête par l'exploitation informatique
- Support à risque faible manquant : documenter et assurer le suivi dans les 5 jours ouvrables

**Audit complet annuel** : vérification à 100 % de TOUS les supports (tous niveaux de risque) réalisée une fois par an (T4 ou tel que planifié par le RSSI).

Les résultats d'audit doivent être documentés et conservés pendant 12 mois.

---

## Exigences d'utilisation des supports

### Transfert de données vers des supports amovibles

- Le transfert de données CONFIDENTIELLES vers des supports amovibles nécessite une approbation managériale documentée préalablement au transfert. L'enregistrement d'approbation doit préciser la justification commerciale, le destinataire et la date de retour prévue.
- Toutes les données transférées vers des supports amovibles doivent être chiffrées. Pour les données CONFIDENTIELLES, le chiffrement AES-256 (matériel ou logiciel) est obligatoire. Pour les données INTERNES, AES-128 ou plus fort est requis.
- Des journaux de transfert doivent être maintenus pour les données CONFIDENTIELLES, enregistrant : la date, l'utilisateur, l'identifiant du support, la description des données et le destinataire.
- Les données doivent être supprimées des supports amovibles dès qu'elles ne sont plus nécessaires à l'objectif approuvé.

### Contrôle d'accès et protection

- Les supports contenant des données CONFIDENTIELLES doivent être protégés par mot de passe ou chiffrés avec une authentification forte (PIN, phrase de passe ou déverrouillage biométrique sur l'appareil).
- Les supports ne doivent jamais être laissés sans surveillance. Lorsqu'ils ne sont pas en cours d'utilisation, les supports doivent être sécurisés dans un stockage verrouillé approprié au niveau de classification.
- Les supports amovibles ne doivent pas être connectés à des systèmes non fiables ou publics.
- Le contenu des supports doit être analysé à la recherche de logiciels malveillants par [Outil de protection des postes] avant que les données soient ouvertes ou transférées vers les systèmes de l'organisation. L'exécution automatique et la lecture automatique doivent être désactivées sur tous les postes via la politique [Outil de gestion des postes].

### Contrôles des ports USB et des supports amovibles

- Les ports USB et l'accès aux supports amovibles doivent être gérés de manière centralisée via [Outil de gestion des postes] (p. ex., Stratégie de groupe, MDM ou plateforme de protection des postes).
- Politique par défaut : dispositifs de stockage de masse USB bloqués sur tous les postes. Exceptions accordées par numéro de série de l'appareil pour les supports chiffrés enregistrés uniquement.
- Tous les événements de connexion USB doivent être journalisés par la plateforme de protection des postes. Les journaux doivent être conservés pendant un minimum de 12 mois.

**Contrôle des ports USB par type de poste** — Différents types de postes ont des exigences d'accès USB différentes :

| Type de poste | Stockage de masse USB | Supports approuvés | Journalisation |
|--------------|----------------------|-------------------|----------------|
| **Poste de travail/ordinateur portable de bureau standard** | Bloqué par défaut | Exception par numéro de série (supports chiffrés enregistrés uniquement) | Toutes les tentatives de connexion journalisées |
| **Poste de travail développeur** | Autorisé pour les supports chiffrés enregistrés uniquement | Clé USB chiffrée émise par l'organisation + outils de développement approuvés (Yubikey, clés de sécurité matérielles) | Toutes les connexions journalisées |
| **Ordinateur portable dirigeant/travailleur mobile** | Autorisé pour les supports chiffrés enregistrés uniquement | Clé USB chiffrée émise par l'organisation | Toutes les connexions journalisées ; révision d'accès trimestrielle |
| **Borne/système en accès public** | Bloqué (aucune exception) | Aucun | Toutes les tentatives de connexion journalisées et alertes |
| **Serveur/infrastructure** | Bloqué (aucune exception sauf pour l'exploitation informatique autorisée lors de la maintenance) | Supports de secours/diagnostic approuvés uniquement (chiffrés, lecture seule dans la mesure du possible) | Toutes les connexions journalisées et alertes |

Mise en œuvre via [Outil de gestion des postes] : Politique de contrôle des appareils avec liste blanche par numéro de série d'appareil (pas par type d'appareil) ; groupes de politique différents par type de poste (basé sur groupe AD ou tag d'appareil). Alerte sur : tentatives de connexion USB non autorisées, connexions USB en dehors des heures ouvrables, transferts de données en masse (> 1 Go), tentatives d'authentification échouées multiples sur des supports chiffrés.

**Exception temporaire** (visiteur/prestataire, besoin de courte durée < 7 jours) : approbation par l'exploitation informatique + responsable hiérarchique ; maximum 7 jours ; journalisation renforcée + révision quotidienne ; exception automatiquement retirée de la liste blanche à expiration.

---

## Transport des supports de stockage

### Exigences de transport sécurisé

Lors du transport de supports de stockage, les exigences suivantes s'appliquent :

**Expédition par coursier et service postal** :

- Les supports CONFIDENTIELS doivent être transportés uniquement par des services de coursier sécurisés approuvés avec suivi et signature à la livraison. Les services postaux standard ne doivent pas être utilisés pour les données CONFIDENTIELLES.
- Les supports INTERNES devraient utiliser des services de coursier avec suivi. Les services postaux standard peuvent être utilisés avec livraison recommandée/suivie.
- Un emballage inviolable doit être utilisé pour tous les supports contenant des données CONFIDENTIELLES. Le destinataire doit inspecter l'emballage pour détecter toute preuve d'altération et signaler immédiatement toute anomalie.
- La documentation de la chaîne de possession doit accompagner tous les envois de supports CONFIDENTIELS (voir section Chaîne de possession ci-dessous).

**Transport personnel (en main propre)** :

- Les supports doivent être transportés en bagage à main lors des déplacements (jamais en bagages enregistrés en soute).
- Les supports doivent être chiffrés et ne doivent jamais être laissés sans surveillance pendant le transport.
- Le transit par des zones à risque élevé (aéroports, conférences, juridictions étrangères sans protection adéquate des données) devrait être évité dans la mesure du possible. Lorsque cela est inévitable, des mesures de chiffrement et de contrôle d'accès supplémentaires doivent être appliquées.

**Alternative par transfert électronique** :

Lorsque c'est possible, le transfert électronique chiffré (p. ex., partage de fichiers sécurisé, SFTP, messagerie chiffrée) devrait être préféré au transport physique de supports. Le transport physique ne devrait être utilisé que lorsque le transfert électronique est impossible ou interdit.

**Protection environnementale pendant le transport** :

Les supports de stockage (en particulier les bandes magnétiques et les HDD) sont sensibles aux températures, à l'humidité et aux chocs physiques pendant le transport :

- **Transport estival (ambiant > 30 °C)** : Utiliser des conteneurs d'expédition isolés ; éviter de laisser les supports dans des véhicules ; privilégier la livraison le jour même ou le lendemain pour minimiser le temps de transit
- **Transport hivernal (ambiant < 5 °C)** : Utiliser des conteneurs d'expédition isolés ; laisser les supports s'acclimater à la température ambiante (minimum 2 heures) avant utilisation en cas d'exposition à des conditions de gel
- **Protection contre les chocs** : Utiliser du papier à bulles antistatique + contenant rigide extérieur (pas d'enveloppe matelassée) ; étiqueter « Fragile — Supports électroniques » sur tous les côtés ; marquer « Ce côté vers le haut » pour les cartouches de bandes
- **Protection contre l'humidité** : Utiliser des sachets desséchants (gel de silice) dans les conteneurs d'expédition pour les climats humides ou les changements rapides d'humidité

| Type de support | Tolérance de température (hors fonctionnement) | Sensibilité aux chocs | Emballage recommandé |
|----------------|------------------------------------------------|----------------------|---------------------|
| Bande magnétique (LTO, DAT) | –40 à 65 °C | Élevée (parties mécaniques internes) | Antistatique + boîtier rigide + étiquette « Fragile » |
| HDD | –40 à 70 °C | Élevée (pièces mobiles) | Antistatique + rembourrage mousse + boîtier rigide |
| SSD / Flash | –40 à 85 °C | Faible (pas de pièces mobiles) | Antistatique + emballage standard |
| Optique (CD/DVD) | 5 à 50 °C | Faible | Boîtier plastique + enveloppe matelassée |

Instructions pour les coursiers transportant des supports CONFIDENTIELS : fournir des instructions de manipulation au coursier ; exiger une signature à la livraison (pas de dépôt sans présence) ; suivre l'expédition en temps réel ; enquêter si la livraison est retardée de plus de 24 heures. Le destinataire doit inspecter l'emballage pour détecter tout dommage à la réception et signaler immédiatement tout dommage physique.

### Chaîne de possession

Tous les transferts de supports contenant des données CONFIDENTIELLES entre individus, emplacements ou organisations doivent être documentés avec :

- Date et heure du transfert
- Identité de la partie cédante (nom, rôle)
- Identité de la partie réceptrice (nom, rôle, organisation si externe)
- Identifiant du support (étiquette d'actif, numéro de série)
- Description du contenu (niveau de classification, catégorie générale de données — pas les données elles-mêmes)
- Accusé de réception (signature ou confirmation électronique)
- Date de retour prévue (le cas échéant)

Les enregistrements de la chaîne de possession doivent être conservés pendant 7 ans.

**Chaîne de possession pour le transfert logique de données** : Lorsque les données sont transférées électroniquement plutôt que via un support physique, la chaîne de possession doit également être documentée :
- Documentation requise : date/heure, expéditeur, destinataire, noms/tailles des fichiers, classification, méthode de transfert (e-mail/SFTP/partage de fichiers sécurisé), méthode de chiffrement (p. ex., « AES-256 via [Outil] »), expiration du lien (si basé sur un lien)
- Journalisation : capture automatique via les journaux d'audit [Outil de partage de fichiers sécurisé] / [Passerelle e-mail] lorsque disponibles
- Conservation : 12 mois (journaux) ; 7 ans (enregistrements de transferts CONFIDENTIELS)

*Méthode de transfert préférée par scénario* :

| Scénario | Méthode préférée | Justification |
|----------|-----------------|---------------|
| Fichier < 100 Mo | E-mail chiffré ou partage de fichiers sécurisé (p. ex., [Outil]) | Plus rapide ; pas de risque lié aux supports physiques |
| Fichier 100 Mo – 10 Go | Partage de fichiers sécurisé avec lien à expiration | Évite les limites de taille des e-mails ; traçable |
| Fichier > 10 Go | Clé USB chiffrée via coursier, ou SFTP/synchronisation cloud | Support physique pratique pour les transferts volumineux |
| Archivage/sauvegarde (échelle To) | Bande chiffrée via coursier | Solution la plus économique pour l'archivage en masse |

Pour les transferts logiques CONFIDENTIELS : chiffrement de bout en bout obligatoire (chiffré avant envoi/chargement, le destinataire déchiffre). Partage basé sur un lien : liens à expiration (maximum 7 jours), protégés par mot de passe, notification de téléchargement à l'expéditeur. E-mail : pièce jointe chiffrée (GPG/PGP ou [Outil de messagerie sécurisée]), identité du destinataire vérifiée avant envoi.

---

## Exigences de stockage

### Stockage physique par classification

Les supports de stockage doivent être stockés dans des conditions adaptées à la fois à la sensibilité des informations et à l'intégrité physique du support :

| Classification | Stockage physique | Chiffrement | Contrôle d'accès | Exigences environnementales |
|----------------|------------------|-------------|-----------------|----------------------------|
| **CONFIDENTIEL** | Coffre-fort verrouillé ou armoire sécurisée dans une zone restreinte | Obligatoire — AES-256 (conformément à la Politique de cryptographie) | Personnes nommées uniquement ; accès journalisé | Température 15-25 °C ; 30-60 % HR ; à l'écart des champs magnétiques et de la lumière directe du soleil |
| **INTERNE** | Armoire ou tiroir verrouillé | Recommandé — AES-128 ou plus fort | Personnel autorisé ayant un besoin commercial légitime | Conditions de bureau standard ; à l'écart des risques environnementaux |
| **PUBLIC** | Stockage de bureau standard | Facultatif | Accès général ; sécurité physique maintenue | Conditions de bureau standard |

### Stockage des supports de sauvegarde

- Les bandes et cartouches de sauvegarde doivent être stockées dans un emplacement physique séparé des systèmes qu'elles sauvegardent (hors site ou dans une zone coupe-feu séparée).
- Les supports de sauvegarde doivent être chiffrés en utilisant un chiffrement fournisseur fort ou un outil de chiffrement approuvé par l'organisation.
- Les supports de sauvegarde doivent être inclus dans l'inventaire des supports et soumis au même audit trimestriel que les supports amovibles.

### Conservation et expiration

- Les supports doivent être conservés conformément au calendrier de conservation des données de l'organisation. Les durées de conservation sont définies par le type de données, l'exigence réglementaire et le besoin commercial.
- Lorsque la période de conservation des données sur un support expire, le support doit être assaini ou détruit conformément à la section Mise au rebut de cette politique.
- Les bandes de sauvegarde et les instantanés cloud doivent avoir des déclencheurs de mise au rebut ou de suppression documentés alignés avec le calendrier de conservation. La conservation « indéfinie » n'est pas autorisée sans approbation documentée du RSSI et révision annuelle.

**Cadre de conservation des supports de sauvegarde** — Approche à deux niveaux séparant la reprise opérationnelle de la conservation légale/conformité :

*Conservation des sauvegardes opérationnelles* (pour la reprise après sinistre et la restauration opérationnelle) :
- Sauvegardes quotidiennes : 30 jours
- Sauvegardes hebdomadaires : 90 jours (3 mois)
- Sauvegardes mensuelles : 12 mois
- Sauvegardes annuelles : 3 ans (filet de sécurité pour restauration à long terme)

*Conservation des données légales/conformité* (pour les exigences réglementaires, blocages légaux, audits) :
- Séparée des sauvegardes opérationnelles — utiliser un stockage d'archivage structuré, pas des sauvegardes système complètes sur bandes
- Relevés financiers : 10 ans (CO suisse art. 958f)
- Dossiers RH : 10 ans
- Données clients : selon contrat ou réglementation applicable

*Déclencheurs de suppression des sauvegardes* :

| Type de sauvegarde | Déclencheur de suppression | Méthode |
|-------------------|--------------------------|---------|
| Sauvegardes quotidiennes > 30 jours | Suppression automatique par l'outil de sauvegarde | Politique de conservation dans [Outil de sauvegarde], journalisée |
| Sauvegardes hebdomadaires > 90 jours | Suppression automatique par l'outil de sauvegarde | Politique de conservation dans [Outil de sauvegarde] |
| Sauvegardes mensuelles > 12 mois | Révision manuelle + approbation du Responsable de l'exploitation informatique | Révision trimestrielle ; suppression avec approbation signée |
| Sauvegardes annuelles > 3 ans | Révision manuelle + approbation du RSSI | Révision annuelle ; suppression avec approbation signée |
| Instantanés cloud (orphelins) | Identification trimestrielle + délai de grâce de 90 jours | Politique de cycle de vie ; révision des instantanés orphelins trimestriellement |

*Exception de blocage légal* : Si des données font l'objet d'un blocage légal (litige, enquête, audit), la suppression des sauvegardes doit être suspendue pour les données concernées. Le blocage légal est documenté dans [Système de gestion des actifs] avec la raison du blocage, la date de début et la date de révision. La reprise de la suppression nécessite l'approbation du service juridique/conformité.

---

## Mise au rebut des supports de stockage

### Principes de mise au rebut

La mise au rebut et l'assainissement doivent garantir que les informations ne peuvent pas être récupérées, en utilisant des méthodes approuvées par l'organisation adaptées au type de support et au niveau de classification le plus élevé des données jamais stockées sur le support.

L'organisation adopte le cadre NIST SP 800-88 Rev. 2 pour l'assainissement des supports, aligné sur les recommandations techniques IEEE 2883:2022 pour l'assainissement des dispositifs de stockage :

| Niveau d'assainissement | Méthode | Description | Cas d'utilisation |
|------------------------|---------|-------------|------------------|
| **Effacement** | Écrasement logique | Écrase les emplacements de stockage accessibles à l'utilisateur avec des données non sensibles à l'aide de commandes de lecture/écriture standard. Protège contre les techniques simples et non invasives de récupération de données. | Données PUBLIQUES ; réutilisation interne d'équipements peu sensibles |
| **Purge** | Effacement cryptographique, effacement de bloc ou commandes au niveau du micrologiciel | Rend la récupération des données infaisable avec des techniques de laboratoire de pointe. Comprend l'effacement cryptographique (destruction des clés de chiffrement sur les disques auto-chiffrants) et les commandes d'effacement sécurisé du fabricant conformément à IEEE 2883. | Données INTERNES ; réutilisation interne ; transfert externe d'équipements précédemment INTERNES |
| **Destruction** | Destruction physique | Rend le support physiquement inutilisable par déchiquetage, désintégration, broyage ou incinération. La récupération des données est infaisable quel que soit l'effort appliqué. | Données CONFIDENTIELLES ; toute mise au rebut externe de supports ayant stocké des données sensibles ; fin de vie pour tout support dont l'assainissement ne peut pas être vérifié |

### Exigences de mise au rebut par classification

| Classification | Résultat requis | Niveau NIST minimum | Vérification |
|----------------|-----------------|---------------------|--------------|
| **CONFIDENTIEL** | Irrécupérable par tous moyens, y compris les techniques de laboratoire de pointe | Destruction (ou Purge uniquement pour réutilisation interne avec effacement cryptographique vérifié) | Certificat de destruction du prestataire agréé ; destruction attestée pour les données hautement sensibles |
| **INTERNE** | Irrécupérable sans équipement ou techniques spécialisés | Purge | Vérification de l'effacement réussi documentée avec le journal de sortie de l'outil |
| **PUBLIC** | Suppression standard avec mise au rebut documentée | Effacement | Documentation de la mise au rebut dans le registre des actifs |

### Méthodes de mise au rebut par type de support

| Type de support | CONFIDENTIEL | INTERNE | PUBLIC |
|----------------|--------------|---------|--------|
| **Disques durs (HDD)** | Destruction physique : déchiquetage ou démagnétisation + déchiquetage | Purge : effacement sécurisé du fabricant (ATA Secure Erase, NVMe Sanitize) ou écrasement en une seule passe avec vérification, ou destruction physique | Formatage et réinstallation |
| **Disques SSD/NVMe** | Destruction physique : déchiquetage ou désintégration | Effacement cryptographique ou effacement sécurisé du fabricant conformément à IEEE 2883 ; destruction physique si l'effacement cryptographique n'est pas disponible | Commande d'effacement sécurisé |
| **Clés USB / Cartes SD** | Destruction physique : déchiquetage | Écrasement sécurisé ou destruction physique | Formatage |
| **Bandes LTO / de sauvegarde** | Destruction physique : déchiquetage ou incinération | Démagnétisation + écrasement ou destruction physique | Démagnétisation ou écrasement |
| **Supports optiques (CD/DVD/Blu-ray)** | Destruction physique : déchiquetage ou incinération | Destruction physique : déchiquetage | Destruction physique ou dégradation |
| **Appareils mobiles** | Destruction physique des composants de stockage | Réinitialisation usine + vérification de l'effacement cryptographique | Réinitialisation usine |
| **Imprimantes / Copieurs (HDD/SSD internes)** | Retrait + destruction du stockage interne | Retrait + effacement sécurisé du stockage interne | Effacement mémoire / réinitialisation usine |
| **Stockage cloud / virtuel** | Effacement cryptographique + confirmation de suppression + recours à la certification SOC 2/ISO 27001 du prestataire | Effacement cryptographique + confirmation de suppression du prestataire | Suppression standard via API/console du prestataire |

**Remarque importante sur les SSD et les supports flash** : Les méthodes d'écrasement traditionnelles sont peu fiables pour les SSD et les supports flash en raison du nivellement d'usure, du sur-provisionnement et de l'amplification d'écriture. Pour les SSD et les supports à base de flash, l'effacement cryptographique (lorsque pris en charge par les disques auto-chiffrants) ou les commandes d'effacement sécurisé fournies par le fabricant conformément à IEEE 2883:2022 sont les méthodes de Purge approuvées. Lorsqu'aucune n'est disponible ou ne peut être vérifiée, la destruction physique est requise.

**Écrasement HDD — recommandations NIST SP 800-88 Rev. 2** : Le NIST SP 800-88 Rev. 2 (septembre 2025) confirme qu'un écrasement en une seule passe est suffisant pour les HDD modernes (fabrication après 2001). L'écrasement en plusieurs passes (p. ex., méthodes DoD 5220.22-M historiques à 3 ou 7 passes) n'est plus requis et n'offre aucun avantage de sécurité supplémentaire sur les disques modernes. Méthodes de Purge approuvées pour les HDD : commande d'effacement sécurisé du fabricant (ATA Secure Erase, NVMe Sanitize), ou écrasement en une seule passe avec vérification à l'aide d'un outil approuvé (p. ex., DBAN, nwipe, shred ou dd). La vérification doit inclure un rapport de fin d'outil avec numéro de série, horodatage et statut réussite/échec.

**Exigences de démagnétisation pour les supports magnétiques** : L'efficacité de la démagnétisation dépend de la force du champ magnétique du démagnétiseur par rapport à la coercivité du support. Le démagnétiseur doit être calibré pour le type de support à assainir :

| Type de support | Plage de coercivité | Puissance minimale du démagnétiseur |
|----------------|--------------------|------------------------------------|
| Bandes LTO-7/8/9 | ~2 800–3 200 Oe | ≥ 7 000 Gauss (liste NSA/CSS EPL recommandée) |
| Bandes LTO-5/6 | ~2 500–2 800 Oe | ≥ 5 000 Gauss |
| Cartouches DAT/DLT | ~1 500–2 000 Oe | ≥ 5 000 Gauss |
| HDD (anciens, pré-SSD) | ~2 000–5 000 Oe | ≥ 9 000 Gauss pour un effacement fiable |

Validation du démagnétiseur : l'équipement de démagnétisation doit être testé annuellement (ou selon les recommandations du fabricant) pour vérifier que la force du champ reste dans les spécifications. Les enregistrements de tests doivent être conservés. Les SSD et supports flash ne peuvent pas être démagnétisés — la démagnétisation n'a aucun effet sur les supports de stockage à semi-conducteurs.

**Mise au rebut du stockage cloud et virtuel** : Les principaux fournisseurs cloud (AWS, Azure, GCP) ne fournissent pas de certificats de destruction individuels pour les supports virtuels. Pour la mise au rebut cloud, l'organisation doit :
- Supprimer les volumes/objets via la console cloud ou l'API et supprimer les clés de chiffrement du KMS (effacement cryptographique)
- Conserver les preuves de confirmation de suppression (capture d'écran ou journal d'audit API avec identifiant du volume et horodatage de suppression)
- S'appuyer sur la certification SOC 2 Type II / ISO 27001 du prestataire attestant que le stockage supprimé est assaini conformément à NIST SP 800-88 avant la réutilisation ou la mise au rebut du matériel
- Documenter le recours à la certification du prestataire dans l'enregistrement de mise au rebut (p. ex., « SOC 2 Type II AWS daté du [Date] »)
- Pour les données CONFIDENTIELLES les plus sensibles : utiliser le chiffrement côté client (l'organisation contrôle les clés, pas le prestataire) comme mesure d'atténuation — même si le prestataire échoue à supprimer les données, elles restent chiffrées
- La direction générale doit reconnaître annuellement le recours aux processus de suppression certifiés par le prestataire lors de la revue de direction

### Réutilisation interne

Avant toute réutilisation d'un support au sein de l'organisation :

- Toutes les données doivent être effacées de manière sécurisée en utilisant une méthode approuvée adaptée à la classification précédente des données.
- L'effacement doit être vérifié à l'aide de [Outil d'effacement sécurisé] et le journal de vérification conservé.
- Les supports doivent être inspectés pour détecter tout problème d'intégrité physique. Les supports endommagés ne doivent pas être réutilisés mais détruits.
- Les enregistrements du [Système de gestion des actifs] doivent être mis à jour avec la nouvelle attribution, la date et les preuves d'assainissement.
- Les logiciels sous licence doivent être transférés ou supprimés conformément aux conditions de licence.

### Mise au rebut externe

Les supports destinés à être mis au rebut en externe doivent :

- Avoir toutes les données effacées de manière sécurisée au niveau requis, ou être physiquement détruits.
- Être mis au rebut uniquement par des prestataires de destruction agréés.
- Avoir leur mise au rebut documentée avec des certificats de destruction conservés pendant 7 ans.
- Ne jamais être vendus, donnés ou jetés avec des données récupérables.

Les équipements ayant stocké des données CONFIDENTIELLES ne doivent pas être réutilisés en externe. Les supports de stockage doivent être physiquement détruits avant tout transfert externe.

### Certificats de destruction

Pour tous les supports détruits par [Prestataire de destruction] externe ou des fournisseurs spécialisés :

- Un certificat de destruction doit être obtenu pour chaque lot ou élément individuel détruit.
- Les certificats doivent faire référence aux numéros de série ou étiquettes d'actifs individuels, pas seulement aux identifiants de lot.
- La méthode de destruction et la norme de conformité (p. ex., Destruction NIST SP 800-88, niveau DIN 66399) doivent être indiquées.
- Les certificats doivent être confrontés à l'enregistrement de transfert pour s'assurer que tous les éléments sont comptabilisés. Les divergences doivent être escaladées immédiatement et enregistrées comme événement de sécurité.
- Les certificats doivent être classés avec l'enregistrement de mise au rebut et conservés pendant 7 ans.

---

## Documents papier et supports physiques

### Gestion des documents papier

- Les documents papier doivent être classifiés et manipulés conformément à la Politique de classification et de gestion des informations.
- Les documents CONFIDENTIELS doivent être stockés dans des armoires ou coffres-forts verrouillés lorsqu'ils ne sont pas en cours d'utilisation active :
  - **Armoire de classement verrouillée** : Adaptée aux documents d'affaires CONFIDENTIELS standard (contrats, relevés financiers, listes de clients) jusqu'à environ 1 tiroir (~1 000 feuilles). Armoire métallique avec serrure à clé ou à combinaison, fixée au sol/mur dans la mesure du possible.
  - **Coffre-fort verrouillé** : Requis pour les secrets commerciaux, les documents de fusions-acquisitions, les documents relevant du secret professionnel et les données personnelles hautement sensibles (dossiers médicaux des dirigeants, résultats de vérification des antécédents). Coffre-fort résistant au feu (résistance minimum de 1 heure), à combinaison ou à serrure électronique, accès limité à 2-3 personnes nommées.
  - **Chambre forte/salle sécurisée** : Requise pour le stockage archivistique CONFIDENTIEL en grande quantité (> 10 boîtes à archives). Salle dédiée verrouillée avec contrôle d'accès par carte, vidéosurveillance et contrôles environnementaux (extinction incendie, humidité).
- Les documents doivent être collectés immédiatement des imprimantes, copieurs et télécopieurs. L'impression sécurisée à la demande (pull printing) devrait être mise en œuvre lorsque disponible.
- La politique de bureau propre doit être respectée à tout moment (voir Politique sur les zones sécurisées et la gestion des supports, A.7.6-7-14).

### Destruction des documents papier

La destruction des documents papier doit se conformer aux normes DIN 66399. La norme DIN 66399 définit les niveaux de sécurité en utilisant un préfixe de lettre pour la catégorie de support (P = papier) et un numéro pour le niveau de sécurité (1-7, plus le numéro est élevé, plus les particules sont petites) :

| Classification | Niveau DIN 66399 | Taille des particules | Méthode |
|----------------|-----------------|----------------------|---------|
| **CONFIDENTIEL** | P-4 minimum (P-5 recommandé pour les données personnelles sensibles) | P-4 : max 160 mm², largeur max 6 mm | Déchiquetage croisé |
| **INTERNE** | P-3 minimum | P-3 : max 320 mm², largeur max 2 mm | Déchiquetage croisé ou en bandes |
| **PUBLIC** | Aucune exigence minimale | S/O | Déchets généraux / recyclage |

- Le déchiquetage doit être effectué sur site à l'aide de déchiqueteuses appartenant à l'organisation dans la mesure du possible. Pour la destruction en masse, des prestataires externes agréés peuvent être utilisés avec collecte dans des poubelles de déchets confidentiels verrouillées et certificats de destruction.
- Des poubelles de déchets confidentiels doivent être disponibles dans des emplacements accessibles dans tout le bureau. Les poubelles doivent être verrouillées et vidées selon un calendrier planifié par le personnel autorisé ou [Prestataire de destruction].
- Les événements de destruction en masse (déménagements de bureau, purges d'archives) doivent être attestés ou certifiés.

### Microfilms, microfiches et supports photographiques

- La destruction doit suivre la catégorie de support F (film) de la norme DIN 66399 aux niveaux de sécurité correspondant à la classification des informations.
- CONFIDENTIEL : F-4 minimum (taille maximale des particules 160 mm²). INTERNE : F-3 minimum.
- Lorsque le déchiquetage sur site des supports de film n'est pas possible, un prestataire externe agréé doit être utilisé.

---

## Rôles et responsabilités

| Rôle | Responsabilités liées aux supports de stockage |
|------|------------------------------------------------|
| **Direction générale** | Approuver la politique ; allouer les ressources pour l'infrastructure de sécurité des supports et les contrats fournisseurs |
| **RSSI** | Propriété de la politique ; définir les normes d'assainissement ; superviser la conformité ; approuver les exceptions ; examiner les résultats d'audit trimestriels |
| **Exploitation informatique** | Approvisionnement et fourniture des supports ; déploiement du chiffrement ; exécuter l'assainissement et la destruction ; maintenir les enregistrements de mise au rebut ; gérer [Outil d'effacement sécurisé] et [Outil de gestion des postes] |
| **Responsable des installations** | Gérer l'infrastructure de stockage physique (coffres-forts, armoires verrouillées) ; coordonner la fourniture et la collecte des poubelles de déchets confidentiels ; gérer l'équipement de déchiquetage sur site |
| **Responsables hiérarchiques** | Autoriser l'utilisation de supports amovibles pour leurs équipes ; assurer la conformité de l'équipe aux exigences de manipulation et de stockage ; traiter les constatations d'audit |
| **Achats / Gestion des fournisseurs** | Gérer les contrats [Prestataire de destruction] ; vérifier les certifications des prestataires ; collecter et vérifier les certificats de destruction |
| **Gestion des actifs** | Maintenir l'inventaire des supports dans [Système de gestion des actifs] ; réaliser les audits trimestriels des supports ; réconcilier les enregistrements ; mettre à jour le statut des actifs à la mise au rebut |
| **Tout le personnel** | Manipuler les supports conformément aux exigences de classification ; restituer les supports lors du départ de l'emploi ; signaler immédiatement les supports perdus, volés ou endommagés ; ne pas utiliser de supports personnels pour les données de l'organisation |

**Chemin d'escalade** :

- Support perdu ou volé : Employé → Responsable hiérarchique + Exploitation informatique (immédiat) → RSSI
- Questions sur la politique des supports : Employé → Exploitation informatique → RSSI
- Certificats de destruction manquants : Exploitation informatique → Achats → RSSI
- Divergences d'audit trimestriel : Gestion des actifs → RSSI → Direction générale (si non résolues dans les 5 jours ouvrables)

### Procédure de réponse aux incidents pour support perdu ou volé

Lorsqu'une perte ou un vol de support est signalé, les actions immédiates suivantes doivent être prises :

**Dans les 15 minutes suivant le signalement :**

1. **Évaluer la gravité** :
   - Classification des données sur le support (CONFIDENTIEL = Critique, INTERNE = Élevé, PUBLIC = Faible)
   - Statut de chiffrement (chiffré = risque moindre, non chiffré = risque plus élevé)
   - Quantité d'enregistrements de données personnelles (> 100 personnes = risque plus élevé de notification de violation)

2. **Confinement immédiat** (si le support est non chiffré ou contient des données CONFIDENTIELLES) :
   - Exploitation informatique : Effacement à distance du support si la capacité d'effacement à distance existe (p. ex., appareil mobile, support synchronisé avec le cloud)
   - Exploitation informatique : Désactiver les identifiants d'accès associés si le support contenait des identifiants (clés API, mots de passe)
   - Exploitation informatique : Désactiver le numéro de série du support de la liste des supports approuvés (prévenir la reconnexion si retrouvé)

**Dans l'heure :**

3. **Classification de l'incident** :
   - CONFIDENTIEL + non chiffré = Gravité critique (supposer une violation de données, déclencher la réponse à la violation conformément à A.5.24-28)
   - CONFIDENTIEL + chiffré = Gravité élevée (évaluer la sécurité des clés, possibilité de déchiffrement)
   - INTERNE + non chiffré = Gravité élevée
   - INTERNE + chiffré OU PUBLIC = Gravité moyenne/faible

4. **Escalade et investigation** :
   - Notification du RSSI (gravité Critique/Élevée)
   - Notification du DPD (si des données personnelles sont impliquées — évaluer la notification de violation en vertu de la nLPD art. 24 / RGPD art. 33)
   - Investigation : Comment le support a-t-il été perdu ? Circonstances, chronologie, dernier emplacement connu

**Dans les 24 heures :**

5. **Évaluation de la notification de violation** :
   - Si les critères de violation nLPD/RGPD sont satisfaits : notifier le PFPDT/autorité de contrôle conformément au délai applicable (nLPD : dès que possible ; RGPD : 72 heures)
   - Si une notification contractuelle est requise (ATD client) : notifier les clients conformément aux conditions du contrat
   - Documenter la décision relative à la violation dans le journal des incidents

6. **Remédiation** :
   - Remplacer le support si l'utilisateur a encore besoin d'un support amovible pour ses activités
   - Réémettre un support chiffré si le support perdu n'était pas chiffré
   - Mettre à jour [Système de gestion des actifs] : marquer le support comme « Perdu » avec la référence de l'incident
   - Formation/sensibilisation de l'utilisateur si la perte est due à une négligence

**Post-incident :**
- Analyse des causes profondes : pourquoi le support a-t-il été perdu ? Lacune de processus ? Violation de politique ?
- Actions préventives : en cas de schéma de pertes (p. ex., liées aux voyages), mettre en œuvre des contrôles supplémentaires
- Signalé lors de la revue de direction trimestrielle : statistiques de supports perdus/volés, tendances, actions de remédiation

---

## Preuves associées à cette politique

| N° | Preuve | Responsable | Fréquence | Conservation |
|----|--------|-------------|-----------|--------------|
| 1 | Inventaire des supports amovibles (registre complet avec statut de chiffrement) | Gestion des actifs | En continu ; audit trimestriel | Durée de l'enregistrement de l'actif |
| 2 | Enregistrements d'autorisation des supports (approbations managériales pour l'utilisation de supports amovibles) | Responsables hiérarchiques | Par événement d'autorisation | 3 ans |
| 3 | Journaux de transfert de données CONFIDENTIELLES (date, utilisateur, identifiant du support, description des données, destinataire) | Exploitation informatique | Par événement de transfert | 7 ans |
| 4 | Rapports d'audit trimestriel des supports (résultats de réconciliation, divergences, résolutions) | Gestion des actifs | Trimestriellement | 3 ans |
| 5 | Enregistrements de mise au rebut des équipements (étiquette d'actif, classification, méthode, date, opérateur) | Exploitation informatique | Par événement de mise au rebut | 7 ans |
| 6 | Certificats de destruction du [Prestataire de destruction] | Achats | Par événement de destruction | 7 ans |
| 7 | Journaux de vérification d'effacement sécurisé (sortie de l'outil par actif) | Exploitation informatique | Par événement d'effacement | 7 ans |
| 8 | Enregistrements de chaîne de possession pour le transport de supports | Exploitation informatique | Par événement de transport | 7 ans |
| 9 | Journaux de connexion des ports USB et supports amovibles (télémétrie des postes) | Exploitation informatique | En continu | 12 mois |
| 10 | Enregistrements de collecte et de déchiquetage des poubelles de déchets confidentiels | Responsable des installations | Par événement de collecte | 3 ans |
| 11 | Enregistrements de diligence raisonnable des prestataires pour les services de destruction | Achats | Révision annuelle | Durée du contrat + 2 ans |
| 12 | Enregistrements de reconnaissance de politique (formation à la gestion des supports) | RH / RSSI | Annuellement | Durée de l'emploi + 1 an |
| 13 | Rapports d'incidents de perte/vol de supports (gravité, confinement, évaluation de la violation) | RSSI | Par incident | 7 ans |
| 14 | Enregistrements d'expiration et de renouvellement des autorisations de supports | Exploitation informatique | Par événement | Durée de l'attribution + 1 an |
| 15 | Historique des versions de la liste des supports approuvés et enregistrements de révision | Exploitation informatique / RSSI | Annuellement + déclenchement | 3 ans |

---

## Optionnel : Contrôles des données de paiement par carte (PCI DSS)

*Applicable uniquement si les données de cartes de paiement sont traitées et si le périmètre PCI existe.*

Si le périmètre PCI DSS s'applique, les exigences supplémentaires suivantes doivent être respectées :

- Les supports contenant des données de titulaires de carte doivent être physiquement détruits lorsqu'ils ne sont plus nécessaires pour des raisons commerciales ou légales (exigence PCI DSS 9.4).
- Un inventaire des supports contenant des données de titulaires de carte doit être maintenu et réconcilié au moins annuellement (exigence PCI DSS 9.4.1).
- La mise au rebut sécurisée des supports de données de titulaires de carte doit être documentée avec des certificats de destruction (exigence PCI DSS 9.4.7).
- Le transport interne et externe de supports contenant des données de titulaires de carte doit utiliser un coursier sécurisé et être journalisé (exigences PCI DSS 9.4.3-9.4.4).

---

# Conformité à la politique

## Mesure de la conformité

L'équipe de gestion de la sécurité de l'information vérifiera la conformité à cette politique par diverses méthodes, notamment :

- Audits trimestriels des supports amovibles selon la méthodologie d'échantillonnage basée sur les risques (couverture annuelle à 100 %).
- Révision mensuelle des journaux de connexion USB et des alertes de protection des postes pour les supports non autorisés.
- Révision semestrielle des enregistrements de mise au rebut par rapport au registre des actifs pour identifier les mises au rebut non comptabilisées.
- Révision annuelle des contrats [Prestataire de destruction], des certifications et de l'exhaustivité des certificats de destruction.
- Vérification annuelle que la liste des supports approuvés, les outils d'assainissement et les procédures restent à jour.
- Audits internes et externes, et retours adressés au propriétaire de la politique.

**Métriques de gouvernance** :

| Métrique | Cible |
|----------|-------|
| Supports enregistrés avec conformité au chiffrement | 100 % |
| Pertes ou vols de supports (par trimestre) | 0 |
| Mises au rebut avec certificat (CONFIDENTIEL) | 100 % |
| Vérification d'effacement sécurisé complétée (par mise au rebut) | 100 % |
| Taux d'achèvement de l'audit trimestriel | 100 % |
| Retours de supports en retard | < 3 |
| Taux de correspondance des numéros de série sur les certificats de destruction | 100 % |

## Exceptions

Toute exception à cette politique doit être approuvée et enregistrée par le RSSI à l'avance, avec acceptation des risques documentée, contrôles compensatoires et date de révision définie ne dépassant pas 6 mois. Les exceptions doivent être signalées à l'équipe de revue de direction.

Les exceptions autorisées comprennent :

- Supports amovibles non chiffrés pour des exigences opérationnelles spécifiques où le chiffrement est techniquement incompatible, avec des contrôles physiques renforcés et une approbation à durée limitée.
- Conservation prolongée au-delà des périodes standard avec justification commerciale ou légale documentée et révision annuelle.
- Méthodes de transport alternatives avec acceptation des risques signée par le RSSI.

Les exceptions ne peuvent pas être accordées pour :

- Données CONFIDENTIELLES sur des supports amovibles non chiffrés sans aucun contrôle compensatoire.
- Supports personnels pour les données CONFIDENTIELLES ou INTERNES de l'organisation.
- Mise au rebut de supports CONFIDENTIELS sans vérification ou certificat.
- Contournement des exigences d'audit trimestriel des supports.

## Non-conformité

Un employé dont il est établi qu'il a enfreint cette politique peut faire l'objet de mesures disciplinaires, pouvant aller jusqu'au licenciement.

La manipulation ou la mise au rebut incorrecte de supports contenant des données personnelles peut en outre constituer une violation de la nLPD suisse, pouvant entraîner une enquête réglementaire par le Préposé fédéral à la protection des données et à la transparence (PFPDT) et, le cas échéant, les autorités de protection des données de l'UE en vertu du RGPD.

La perte de supports non chiffrés contenant des données personnelles doit être signalée comme une violation de données et évaluée dans le cadre des procédures de gestion des incidents de l'organisation et des exigences de notification de violation applicables.

## Amélioration continue

Cette politique est révisée et mise à jour dans le cadre du processus d'amélioration continue. Les révisions doivent tenir compte de :

- Les modifications des normes d'assainissement (y compris les mises à jour de NIST SP 800-88, les révisions d'IEEE 2883, les amendements à DIN 66399)
- Les nouvelles technologies de stockage (p. ex., NVMe, mémoire persistante, nouvelles architectures flash)
- Les modifications de la nLPD suisse, du RGPD ou d'autres réglementations applicables
- Les constatations d'audit et les incidents de mise au rebut
- Les retours des audits trimestriels des supports et des révisions des prestataires
- Les modifications du schéma de classification des informations de l'organisation

---

# Domaines de la norme ISO 27001 couverts

Politique sur les supports de stockage — Correspondance avec les contrôles ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership et engagement | 5.1 Politiques de sécurité de l'information |
| Clause 5.2 Politique | 5.4 Responsabilités de la direction |
| Clause 6.1 Actions pour traiter les risques | 5.9 Inventaire des informations et autres actifs associés |
| Clause 7.3 Sensibilisation | 5.10 Utilisation acceptable des informations et autres actifs associés |
| Clause 7.5 Informations documentées | 5.12 Classification des informations |
| Clause 8.1 Planification et contrôle opérationnels | 5.13 Étiquetage des informations |
| Clause 10.2 Non-conformité et action corrective | **7.10 Supports de stockage** |
| | 7.14 Mise au rebut ou réutilisation sécurisée des équipements |
| | 8.10 Suppression des informations |
| | 8.24 Utilisation de la cryptographie |

# Cadre réglementaire

| Cadre | Pertinence |
|-------|-----------|
| nLPD suisse (revDSG) | Art. 8 — Mesures techniques et organisationnelles ; rendre les données personnelles irrécupérables avant la mise au rebut |
| OPDo suisse (Ordonnance sur la protection des données) | Art. 1-3 — Exigences minimales de sécurité des données incluant la protection physique des supports |
| RGPD de l'UE (le cas échéant) | Art. 5(1)(f) — Intégrité et confidentialité ; Art. 17 — Droit à l'effacement ; Art. 32 — Sécurité du traitement |
| ISO/IEC 27001:2022 | Contrôle Annexe A 7.10 — Gestion du cycle de vie des supports de stockage |
| ISO/IEC 27002:2022 | Section 7.10 — Recommandations de mise en œuvre pour les supports de stockage |
| NIST SP 800-88 Rev. 2 | Lignes directrices pour l'assainissement des supports — Effacement, Purge, Destruction (septembre 2025 ; remplace Rev. 1) |
| IEEE 2883:2022 | Norme pour l'assainissement des supports de stockage — méthodes techniques pour les disques et supports |
| DIN 66399 | Destruction des supports de données — niveaux de sécurité (catégories P/F/O/T/H/E, niveaux 1-7) et classes de protection |

---

<!-- QA_VERIFIED: 2026-03-29 -->
