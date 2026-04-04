<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.7.12-13-FR:operational:OP-POL:a.7.12-13 -->
**ISMS-OP-POL-A.7.12-13 — Sécurité du câblage et maintenance des équipements**

---

**Contrôle documentaire**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Sécurité du câblage et maintenance des équipements |
| **Type de document** | Politique opérationnelle |
| **Identifiant du document** | ISMS-OP-POL-A.7.12-13 |
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

- ISO/IEC 27001:2022 Contrôles A.7.12, A.7.13 — Sécurité du câblage, Maintenance des équipements
- ISO/IEC 27002:2022 Sections 7.12, 7.13 — Recommandations de mise en œuvre
- NIST SP 800-53 Rev 5 PE-4 (Contrôle d'accès pour la transmission), PE-9 (Équipements électriques et câblage), MA-2 (Maintenance contrôlée), MA-5 (Personnel de maintenance)
- IEC 11801 / EN 50173 / TIA-568 — Normes de câblage structuré
- NIN suisse (Niederspannungs-Installationsnorm) — Normes d'installation basse tension

**Contrôles Annexe A associés** :

| Contrôle | Relation avec la sécurité du câblage et la maintenance des équipements |
|----------|-----------------------------------------------------------------------|
| A.5.9 Inventaire des informations et autres actifs associés | L'inventaire des actifs conditionne l'exhaustivité du programme de maintenance |
| A.5.24-28 Cycle de vie de la gestion des incidents | Les défaillances d'infrastructure escaladent vers la gestion des incidents |
| A.5.30 Préparation des TIC pour la continuité d'activité | La disponibilité des équipements soutient les objectifs de continuité d'activité |
| A.7.1-3 Périmètres et accès physiques | Contrôle d'accès aux locaux de câblage et armoires de brassage |
| A.7.4 Surveillance de la sécurité physique | Surveillance des zones d'infrastructure où le câblage est acheminé |
| A.7.5 Protection contre les menaces physiques et environnementales | Protection environnementale du câblage et des équipements |
| A.7.8-9 Implantation et protection des équipements | Le placement des équipements tient compte du routage des câbles et de l'accès à la maintenance |
| A.7.14 Mise au rebut ou réutilisation sécurisée des équipements | Les procédures de mise au rebut s'appliquent lors du retrait d'équipements en fin de vie après maintenance |
| A.8.6 Gestion de la capacité | La planification de la capacité informe la planification de la maintenance et le dimensionnement de l'infrastructure de câblage |
| A.8.32 Gestion des changements | Les modifications d'infrastructure et de câblage suivent le processus de gestion des changements |

**Politiques internes associées** :

- Politique de contrôle d'accès physique
- Politique de sécurité de l'infrastructure physique
- Politique d'implantation et de protection des équipements
- Politique de gestion des actifs
- Politique de gestion des changements
- Politique de gestion des incidents
- Politique de continuité d'activité et reprise après sinistre

---

# Politique de sécurité du câblage et de maintenance des équipements

## Objet

L'objet de cette politique est de protéger l'infrastructure physique qui transporte et traite l'information — en particulier le câblage électrique et de données ainsi que les équipements qui y sont connectés. Le câblage constitue le système nerveux de l'environnement de traitement de l'information de l'organisation. Les câbles non protégés sont vulnérables à l'interception, aux interférences électromagnétiques et aux dommages physiques. Les équipements mal maintenus se dégradent, tombent en panne et créent des expositions de sécurité. Cette politique établit les exigences pour les deux aspects.

Les contrôles A.7.12 (Sécurité du câblage) et A.7.13 (Maintenance des équipements) sont combinés car ils traitent des aspects complémentaires de la protection de l'infrastructure : le câblage fournit le fondement de la connectivité, et la maintenance assure la fiabilité continue. Ils partagent des installations, du personnel et des processus d'évaluation communs.

Cette politique soutient la nLPD suisse (revDSG) art. 8 en mettant en œuvre des mesures techniques et organisationnelles proportionnées au risque pour protéger la disponibilité, l'intégrité et la confidentialité des données personnelles par des contrôles d'infrastructure physique. Lorsque l'organisation traite des données de personnes dans l'UE/EEE, les exigences du RGPD art. 32 relatives à la sécurité du traitement incluant les mesures physiques s'appliquent également.

## Champ d'application

Tous les employés, prestataires et personnel de maintenance tiers ayant accès à l'infrastructure de câblage ou aux équipements nécessitant une maintenance.

Cela comprend :

- **Câblage** : câbles électriques, câbles réseau (cuivre et fibre optique), câbles de télécommunication, systèmes de câblage structuré, panneaux de brassage, répartiteurs, chemins de câbles, conduits et cheminements.
- **Équipements** : serveurs, équipements réseau (commutateurs, routeurs, pare-feu), systèmes de stockage, onduleurs (ASI), PDU, systèmes CVC supportant le traitement de l'information, systèmes de sécurité physique (contrôle d'accès, vidéosurveillance) et équipements de télécommunication.
- **Installations** : centres de données, salles des serveurs, armoires de câblage, locaux techniques, colonnes montantes de câbles et tracés de câbles souterrains.
- **Activités** : installation de câbles, inspection de câbles, maintenance des équipements, maintenance préventive, maintenance corrective, maintenance à distance et retrait d'équipements pour réparation.

**Hors champ d'application** :

- Contrôle d'accès physique aux zones d'infrastructure (couvert par A.7.1-3).
- Surveillance et protection environnementales (couvertes par A.7.4-5-11).
- Mise au rebut et destruction sécurisée des équipements (couvertes par A.7.14 et A.7.10).
- Infrastructure hébergée dans le cloud entièrement maintenue par le fournisseur cloud (couverte par la gestion des fournisseurs, A.5.19-23). Lorsque l'organisation opère à 100 % dans le cloud sans équipements sur site, les contrôles A.7.12 et A.7.13 peuvent être marqués « Non applicable » dans la Déclaration d'applicabilité avec justification documentée.

## Principe

Le câblage transportant l'électricité ou les données devrait être protégé contre l'interception, les interférences et les dommages. Les équipements devraient être correctement maintenus pour garantir la disponibilité, l'intégrité et la confidentialité des informations. Les niveaux de protection et de maintenance doivent être proportionnés à la criticité des actifs desservis, déterminée par l'évaluation des risques et la classification des actifs de l'organisation.

---

## Normes de protection du câblage (A.7.12)

> *Les câbles transportant l'électricité, les données ou supportant des services d'information devraient être protégés contre l'interception, les interférences et les dommages.*

### Protection physique du câblage

Tous les câbles transportant l'électricité, les données ou supportant des services d'information doivent être physiquement protégés :

- Les câbles doivent être acheminés par des cheminements protégés — conduits, chemins de câbles, faux planchers surélevés ou vides de plafond — et non exposés dans des espaces ouverts.
- Le câblage souterrain doit être protégé contre les dommages accidentels à l'aide de conduits blindés ou de systèmes de gaine. Des marqueurs de tracé doivent identifier les passages de câbles enterrés.
- Les câbles doivent être protégés contre les risques environnementaux, notamment les infiltrations d'eau, les sources de chaleur, l'exposition chimique et les chocs physiques. Les tracés de câbles doivent éviter les zones à risque élevé de dommages.
- Lorsque les câbles traversent entre bâtiments, une protection adéquate doit être appliquée (câble blindé, gaine scellée ou conduit enterré).
- Les armoires de câblage, locaux techniques et répartiteurs doivent être physiquement sécurisés. Ces espaces doivent être verrouillés lorsqu'ils sont inoccupés et l'accès réservé au personnel autorisé.
- Les regards et points d'accès aux gaines doivent être sécurisés et les accès journalisés.

### Protection électromagnétique

- Les câbles doivent être protégés contre les interférences électromagnétiques (EMI) par un blindage approprié, une séparation des sources d'interférence et le choix d'un type de câble adapté à l'environnement.
- Dans les environnements à fortes interférences électromagnétiques (p. ex., à proximité d'équipements électriques lourds, de machines industrielles ou d'émetteurs radio), des câbles blindés (STP/FTP) ou à fibre optique doivent être utilisés.
- Les installations de câblage doivent se conformer à la norme de câblage structuré adoptée par l'organisation (IEC 11801 / EN 50173 / TIA-568 selon le cas) pour les exigences de blindage et de séparation.

---

## Séparation du câblage

### Séparation électricité et données

Les câbles électriques et les câbles de communication doivent être séparés pour prévenir les interférences électromagnétiques :

- Les distances minimales de séparation doivent suivre la norme de câblage structuré adoptée par l'organisation. En référence : séparation minimale de 200 mm entre les câbles de données non blindés et les câbles électriques cheminant en parallèle. Lorsque le croisement est inévitable, les câbles doivent se croiser à angle droit.
- Les câbles électriques et de données doivent utiliser des conduits, chemins de câbles ou cheminements séparés. Les cheminements partagés ne sont pas autorisés pour les câbles de données non blindés et les câbles électriques.
- Les exigences de séparation doivent être documentées dans la norme de câblage de l'organisation et appliquées de manière cohérente dans toutes les installations.

### Séparation par classification réseau

- Les câbles transportant du trafic de différentes classifications de sécurité doivent être physiquement séparés dans la mesure du possible, ou clairement identifiés par un code couleur ou un étiquetage pour prévenir les interconnexions croisées.
- Les câbles réseau à haute sécurité (p. ex., réseaux de gestion, systèmes financiers, systèmes de sécurité) doivent être identifiables grâce à une convention cohérente de code couleur ou d'étiquetage définie par l'organisation.

---

## Documentation et étiquetage du câblage

### Exigences de documentation

L'infrastructure de câblage doit être documentée et maintenue :

- Un registre du câblage ou une base de données de gestion du câblage doit enregistrer toutes les installations de câblage structuré, y compris le type de câble, les extrémités, le tracé, la date d'installation et la classification.
- Des plans de recollement du câblage doivent être maintenus pour toutes les installations. Les plans doivent montrer les tracés des câbles, les emplacements des panneaux de brassage, les répartiteurs et les interconnexions.
- La documentation du câblage doit être tenue à jour. Toutes les modifications de câblage doivent être reflétées dans la documentation dans les 5 jours ouvrables suivant leur réalisation.
- La documentation du câblage doit être sécurisée et son accès contrôlé. Seul le personnel autorisé doit avoir accès aux plans de câblage détaillés (ceux-ci révèlent la topologie réseau et les tracés physiques).

### Normes d'étiquetage

- Tous les câbles doivent être étiquetés aux deux extrémités avec un identifiant unique qui correspond au registre du câblage.
- Les panneaux de brassage, répartiteurs et prises de télécommunication doivent être clairement étiquetés.
- Les étiquettes doivent être durables, lisibles et permettre l'identification sans nécessiter de référence à une documentation détaillée pour les opérations courantes.
- L'organisation doit définir et documenter une convention d'étiquetage cohérente (p. ex., bâtiment-étage-salle-baie-port).

### Contrôle des modifications du câblage

Toutes les installations, modifications et retraits de câblage doivent suivre le processus de gestion des changements de l'organisation (A.8.32) avec les exigences spécifiques suivantes :

#### Exigences des demandes de modification

Les demandes de modification du câblage doivent inclure :
- **Justification commerciale** : pourquoi la modification est nécessaire
- **Périmètre** : câbles, cheminements et points de terminaison spécifiques concernés
- **Évaluation de l'impact sur les services** : temps d'arrêt potentiel, systèmes/services affectés
- **Plan de mise en œuvre** : procédure étape par étape incluant le plan de test
- **Plan de retour arrière** : comment rétablir le service en cas d'échec de la mise en œuvre
- **Mises à jour de la documentation** : quels plans et registres seront mis à jour

#### Exigences d'approbation

| Type de modification | Approbation requise | Test requis | Délai de mise à jour de la documentation |
|---------------------|--------------------|--------------|-----------------------------------------|
| **Nouvelle installation de câbles** | Responsable de l'exploitation informatique + Responsable des installations | Test du câblage (continuité, performance) selon les normes IEC/TIA | 5 jours ouvrables |
| **Retrait de câbles** | Responsable de l'exploitation informatique | Vérifier l'absence de connexions actives avant retrait | 5 jours ouvrables |
| **Modification du tracé de câbles** | Responsable de l'exploitation informatique + Responsable des installations | Test du câblage après modification | 5 jours ouvrables |
| **Installation/modification de fibre optique** | RSSI + Responsable de l'exploitation informatique (infrastructure haute sécurité) | Test de la fibre (affaiblissement, continuité) | 5 jours ouvrables |
| **Réparation d'urgence** | Responsable de l'exploitation informatique (approbation post-mise en œuvre dans les 24 heures) | Test post-réparation obligatoire | 2 jours ouvrables |

#### Test et validation

Toutes les modifications du câblage doivent inclure des tests post-mise en œuvre :
- **Câble cuivre** : continuité, carte des fils, longueur, affaiblissement, paradiaphonie (NEXT), perte par réflexion selon les exigences Catégorie 6A TIA-568 au minimum
- **Câble à fibre optique** : perte optique, continuité, polarité selon TIA-568 ou les spécifications du fabricant
- **Documentation des résultats de test** : rapports de test conservés avec l'enregistrement de modification ; les tests échoués nécessitent une remédiation avant acceptation
- **Critères d'acceptation** : doit atteindre ou dépasser les spécifications de performance de la norme de câblage applicable

#### Revue post-mise en œuvre

Dans les 30 jours suivant les modifications du câblage affectant plus de 10 connexions ou l'infrastructure critique :
- Examiner l'impact réel sur les services par rapport au planifié
- Examiner les résultats des tests et les écarts par rapport au plan
- Mettre à jour les normes ou procédures de câblage en tenant compte des enseignements tirés
- Documenter les résultats de la revue dans l'enregistrement de modification

- Les câbles inutilisés doivent être déconnectés, documentés et soit retirés, soit clairement marqués comme inactifs.
- Des inspections physiques trimestrielles doivent être réalisées pour identifier les ajouts, modifications ou dommages non autorisés. Les constatations doivent être réconciliées avec les plans de recollement et les enregistrements de modifications, avec des résultats documentés et validés par le Responsable des installations.

---

## Exigences pour la fibre optique

Les câbles à fibre optique doivent être préférés aux câbles en cuivre pour la transmission de données dans les circonstances suivantes :

- **Zones haute sécurité** : salles des serveurs, centres de données et zones sécurisées où le risque d'interception est élevé. Les câbles à fibre optique n'émettent pas de rayonnement électromagnétique et sont nettement plus difficiles à dériver sans être détectés que les câbles en cuivre.
- **Longues distances** : entre bâtiments, entre étages (colonnes montantes) et tout tirage horizontal dépassant 90 mètres (limite de distance du cuivre Catégorie 6A).
- **Besoins en bande passante élevée** : lorsque les besoins en bande passante dépassent les capacités du cuivre (p. ex., 40 Gbps et au-delà).
- **Environnements sensibles aux EMI** : zones à fortes interférences électromagnétiques où les performances des câbles en cuivre seraient dégradées.

Lorsque la fibre optique est déployée, l'épissure par fusion doit être utilisée pour les connexions permanentes (pas les épissures mécaniques) dans les zones sécurisées. Les panneaux de brassage fibre optique doivent être logés dans des armoires verrouillées.

Lorsque des câbles en cuivre sont utilisés dans des zones à risque d'interception, des câbles blindés (STP/FTP) doivent être spécifiés et les tracés de câbles doivent être physiquement sécurisés.

---

## Inspection et maintenance du câblage

Des inspections et une maintenance régulières de l'infrastructure de câblage doivent être réalisées :

- L'infrastructure de câblage doit être incluse dans le programme de maintenance de l'organisation avec des intervalles d'inspection définis.
- Des inspections visuelles doivent être réalisées trimestriellement pour les tracés de câbles accessibles, en vérifiant les dommages, les modifications non autorisées, l'intégrité de l'étiquetage et les obstructions des cheminements.
- Des tests formels du câblage (continuité, performance) doivent être réalisés annuellement ou à la suite de tout problème signalé.
- Les câbles endommagés doivent être réparés ou remplacés rapidement. Les réparations temporaires doivent être documentées et une réparation permanente planifiée dans les 30 jours calendaires.
- Les constatations d'inspection doivent être documentées et conservées pendant un minimum de 3 ans.

---

## Programme de maintenance (A.7.13)

> *Les équipements devraient être correctement maintenus pour garantir la disponibilité, l'intégrité et la confidentialité des informations.*

### Établissement du programme

L'organisation doit établir et maintenir un programme de maintenance couvrant tous les équipements qui traitent, stockent ou supportent le traitement de l'information :

- Tous les équipements dans le périmètre enregistrés dans l'inventaire des actifs (conformément à A.5.9) doivent être inclus dans le programme de maintenance. L'inventaire des actifs est la source faisant autorité pour l'exhaustivité du programme.
- Une réconciliation trimestrielle doit vérifier que tous les équipements inventoriés ont une couverture de maintenance. Les résultats de réconciliation et la validation doivent être conservés comme preuves.
- Les calendriers de maintenance doivent suivre les recommandations du fabricant comme minimums. Les écarts nécessitent une acceptation des risques documentée via le registre des exceptions.
- Le programme de maintenance doit être géré via [SGMM] ou un système de suivi de maintenance équivalent. Lorsqu'un SGMM dédié n'est pas déployé, un tableur ou registre contrôlé doit être utilisé.

### Calendrier de maintenance

Les fréquences minimales de maintenance préventive suivantes s'appliquent :

| Catégorie d'équipement | Fréquence de maintenance préventive | Activités |
|------------------------|-------------------------------------|-----------|
| **Serveurs** | Annuellement | Mises à jour du micrologiciel, nettoyage, inspection physique, vérifications de l'état des composants |
| **Équipements réseau** (commutateurs, routeurs, pare-feu) | Semestriellement | Mises à jour du micrologiciel, nettoyage des ventilateurs, inspection des ports, révision des journaux |
| **Onduleurs (ASI)** | Vérifications de batterie trimestrielles ; test de capacité complète annuel | État de la batterie, test de charge, test de transfert, intégrité des connexions |
| **PDU** | Annuellement | Inspection des connexions, révision de l'équilibrage de charge, thermographie infrarouge |
| **CVC/Refroidissement** (desservant les zones informatiques) | Trimestriellement | Remplacement des filtres, vérifications du réfrigérant, vérification des performances |
| **Détection et extinction d'incendie** | Conformément aux réglementations cantonales incendie (annuellement au minimum) | Test des détecteurs, inspection du système, vérification de l'agent extincteur |
| **Systèmes de sécurité physique** (contrôle d'accès, vidéosurveillance) | Semestriellement | Santé des caméras, test des lecteurs, micrologiciel du contrôleur, vérification de l'enregistrement |
| **Câblage structuré** | Annuellement (inspection visuelle trimestrielle) | Test des câbles, inspection des cheminements, vérification de l'étiquetage |

Les calendriers de maintenance doivent être ajustés en fonction de l'âge des équipements, des conditions environnementales, des avis des fabricants et de l'historique des incidents. Les équipements approchant de leur fin de vie doivent avoir une fréquence de maintenance accrue ou être planifiés pour remplacement.

---

## Disponibilité et continuité des services

Le câblage et l'infrastructure des équipements supportent directement les engagements de disponibilité de service de l'organisation envers ses clients. Les activités de maintenance doivent être planifiées et exécutées pour minimiser les interruptions de service.

### Évaluation de l'impact sur les services

Toutes les activités de maintenance doivent être évaluées pour leur impact potentiel sur les services avant planification :

| Niveau d'impact | Définition | Notification client | Approbation requise |
|----------------|-----------|--------------------|--------------------|
| **Impact nul** | Système redondant ; aucune interruption de service | Aucune | Responsable de l'exploitation informatique |
| **Impact mineur** | Possible brève dégradation des performances (< 5 minutes) | Préavis 48 heures | Responsable de l'exploitation informatique |
| **Impact modéré** | Interruption de service planifiée (5-60 minutes) | Préavis 5 jours ouvrables | RSSI + Propriétaire de l'activité |
| **Impact majeur** | Interruption prolongée (> 60 minutes) ou service orienté client hors ligne | Préavis 10 jours ouvrables | Direction générale + approbation client (si contractuelle) |

### Fenêtres de maintenance

- **Fenêtre de maintenance standard** : [À définir : p. ex., « Dimanches 02h00-06h00 heure locale » ou « Premier samedi de chaque mois 20h00-minuit »]
- Toute maintenance non urgente susceptible d'impacter les services doit être planifiée pendant les fenêtres de maintenance approuvées
- La maintenance d'urgence en dehors des fenêtres de maintenance nécessite l'approbation du RSSI et une notification immédiate aux clients (lorsque l'impact dépasse les seuils des ANS)

### Impact sur les objectifs de disponibilité

Le programme de maintenance de l'infrastructure doit soutenir les engagements de disponibilité de l'organisation :

| Service | Engagement de disponibilité | Temps d'arrêt maximum autorisé par an | Contribution de l'infrastructure |
|---------|---------------------------|--------------------------------------|----------------------------------|
| [Service principal] | Disponibilité à 99,5 % | 43,8 heures | Maintenance planifiée : < 24 heures par an ; Pannes non planifiées : < 20 heures par an |
| [Service secondaire] | Disponibilité à 99,0 % | 87,6 heures | Maintenance planifiée : < 40 heures par an ; Pannes non planifiées : < 48 heures par an |

**Contrainte de planification de la maintenance préventive** : le temps d'arrêt planifié total pour la maintenance de l'infrastructure ne doit pas dépasser 50 % du budget de temps d'arrêt annuel autorisé, réservant une capacité pour les pannes non planifiées.

### Exigences de redondance

Le programme de maintenance des équipements doit tenir compte de la conception de la redondance :

- **Points de défaillance uniques** : les équipements sans redondance doivent avoir leur maintenance planifiée pendant les périodes de faible utilisation avec préavis client
- **Systèmes redondants** : lorsqu'une redondance N+1 ou 2N existe, la maintenance doit être échelonnée pour maintenir au minimum une capacité N à tout moment
- **Équipements de chemin critique** (ASI, réseau cœur, serveurs principaux) : la maintenance doit inclure une vérification préalable du statut de redondance et un test de basculement post-maintenance

### Capacité pendant la maintenance

Lorsque des équipements redondants sont mis hors ligne pour maintenance, la capacité restante doit être vérifiée comme suffisante pour la charge actuelle plus une marge de 20 % :
- Si la capacité devait tomber en dessous du seuil de marge, la maintenance doit être replanifiée ou une capacité temporaire supplémentaire provisionnée
- Le test de charge après maintenance doit vérifier que la redondance complète est restaurée avant de marquer l'équipement « en service »

### Dépendances avec la continuité d'activité et la reprise après sinistre

Le programme de maintenance de l'infrastructure doit soutenir la planification de la continuité d'activité :

#### Identification de l'infrastructure critique

Les équipements et câblages critiques pour la continuité d'activité doivent être identifiés et priorisés :

| Classification | Définition | Priorité de maintenance | Pièces de rechange |
|----------------|-----------|------------------------|-------------------|
| **Niveau 1 - Mission critique** | Équipement dont la panne cause une interruption de service immédiate sans solution de contournement | Priorité la plus haute ; maintenance préventive jamais différée | Pièces critiques sur site ou disponibilité < 4 heures |
| **Niveau 2 - Critique pour l'activité** | Équipement dont la panne cause une dégradation du service ou affecte un sous-ensemble d'utilisateurs | Priorité haute ; maintenance peut être différée au maximum 30 jours avec approbation du RSSI | Pièces de rechange disponibles dans les 24 heures |
| **Niveau 3 - Important** | Équipement dont la panne cause des inconvénients mais les services restent opérationnels | Priorité standard ; reports de maintenance autorisés avec justification documentée | Pièces de rechange commandées à la demande |

#### Test de l'infrastructure de reprise après sinistre

- **Le test annuel de basculement de reprise** doit inclure les composants d'infrastructure :
  - Systèmes d'alimentation de secours (ASI, groupe électrogène si équipé)
  - Chemins réseau redondants
  - Systèmes de refroidissement de secours
  - Chemins de câblage critiques (vérifier l'existence de routes alternatives documentées)
- Le test de reprise doit vérifier que le programme de maintenance a maintenu l'infrastructure dans un état prêt pour la reprise
- Les constatations du test de reprise révélant des lacunes d'infrastructure doivent déclencher des mises à jour du programme de maintenance

#### Infrastructure du site alternatif

Si l'organisation maintient un site de reprise après sinistre :
- Toutes les exigences du programme de maintenance s'appliquent aux équipements du site de reprise
- L'infrastructure de câblage du site de reprise est documentée selon les mêmes normes que le site principal
- Synchronisation des activités de maintenance (si les batteries ASI du site principal sont remplacées, les batteries du site de reprise sont évaluées et remplacées si nécessaire)
- La maintenance des équipements du site de reprise peut être moins fréquente si l'environnement est contrôlé et les équipements peu utilisés (avec justification documentée)

---

## Autorisation du personnel de maintenance

### Personnel interne

- Seul le personnel avec une autorisation documentée doit effectuer la maintenance sur les équipements de traitement de l'information.
- L'autorisation de maintenance doit préciser les catégories d'équipements et les activités de maintenance que l'individu est qualifié pour effectuer.
- Les enregistrements d'autorisation doivent être maintenus et révisés annuellement.

### Personnel de maintenance tiers

- La maintenance par des tiers doit être effectuée uniquement par des prestataires sous contrat et approuvés. Les contrats de maintenance doivent inclure des obligations de confidentialité et des exigences de sécurité.
- Le personnel de maintenance tiers doit être identifié et vérifié (pièce d'identité délivrée par les autorités) avant de se voir accorder l'accès aux équipements.
- L'organisation doit maintenir un registre des prestataires de maintenance tiers approuvés, révisé annuellement.

### Exigences de supervision

- Le personnel de maintenance tiers doit être supervisé lors de l'accès aux équipements qui traitent ou stockent des informations sensibles ou confidentielles, à moins qu'une évaluation documentée des risques ne conclue que l'accès non supervisé est acceptable (p. ex., contrat de maintenance dédié avec personnel ayant fait l'objet d'une vérification des antécédents, équipement isolé).
- L'accès non supervisé de maintenance tiers doit être journalisé avec l'identification individuelle, les heures d'entrée/sortie et les équipements accédés.
- Les enregistrements de supervision doivent être maintenus comme preuves.

---

## Gestion des prestataires de maintenance tiers

### Exigences contractuelles

Les contrats de maintenance avec des prestataires tiers doivent inclure :

| Élément contractuel | Exigence |
|--------------------|----------|
| **Accord de niveau de service (ANS)** | Délai de réponse (arrivée sur site) ; délai de résolution ; procédures d'escalade |
| **Heures de couverture** | 24h/24-7j/7 pour les équipements critiques ; heures ouvrables pour les non-critiques |
| **Disponibilité des pièces de rechange** | Pièces critiques sur site ou engagement de livraison < 4 heures |
| **Exigences de sécurité** | Vérifications des antécédents du personnel ; obligations de confidentialité ; acceptation de la supervision |
| **Protection des données** | Procédures de traitement des données ; capacités d'effacement sécurisé ; obligations de notification de violation de données |
| **Reporting** | Rapports de service mensuels ; réunions de bilan de performance annuelles |
| **Assurance** | Responsabilité professionnelle ; responsabilité cybernétique (pour les prestataires d'accès à distance) |
| **Droits de résiliation** | Résiliation pour violation de sécurité ; obligations d'assistance à la transition |

### Suivi des performances des prestataires

Les performances des prestataires de maintenance doivent être suivies et révisées :

| Métrique | Cible | Fréquence de révision |
|----------|-------|----------------------|
| **Conformité ANS (délai de réponse)** | > 95 % | Trimestriellement |
| **Conformité ANS (délai de résolution)** | > 90 % | Trimestriellement |
| **Qualité de la maintenance** | < 5 % de pannes récurrentes dans les 30 jours | Trimestriellement |
| **Taux d'incidents de sécurité** | 0 | Par occurrence |
| **Satisfaction client** (utilisateurs internes) | > 4/5 | Par événement de service |
| **Conformité documentaire** | 100 % des rapports de service reçus à temps | Trimestriellement |

### Bilan annuel des prestataires

Chaque prestataire de maintenance doit faire l'objet d'un bilan annuel couvrant :
- Performance ANS par rapport aux cibles
- Conformité sécurité (respect de la supervision, bilan sans incident)
- Rapport coût/efficacité par rapport aux alternatives
- Réactivité et qualité de la communication
- Recommandation : continuer, renégocier ou remplacer

**Documentation du bilan** : Conservée 3 ans ; décisions de renouvellement/remplacement documentées avec justification.

### Incidents de sécurité liés aux prestataires

Si un prestataire de maintenance cause ou contribue à un incident de sécurité :
1. **Action immédiate** : suspendre l'accès du prestataire pendant l'enquête
2. **Enquête** : analyse des causes profondes ; déterminer si une violation contractuelle s'est produite
3. **Action corrective** : plan de remédiation fourni par le prestataire ; supervision renforcée si l'accès est rétabli
4. **Révision contractuelle** : évaluer si la résiliation est justifiée ; documenter la décision
5. **Enseignements tirés** : mettre à jour les procédures de gestion des prestataires ou les exigences contractuelles

---

## Sécurité pendant la maintenance

### Protection des données pendant la maintenance

- Les données sensibles doivent être protégées pendant toutes les activités de maintenance. Le personnel de maintenance ne doit pas avoir accès aux données stockées sur les équipements, sauf si cela est spécifiquement requis et autorisé.
- Les équipements contenant des données ne doivent pas être retirés des locaux pour maintenance lorsqu'une réparation sur site est possible.
- Si une maintenance hors site est nécessaire, les données doivent être effacées de manière sécurisée de l'équipement avant retrait (conformément aux procédures de mise au rebut sécurisée A.7.14), ou le support de stockage doit être retiré et conservé par l'organisation.
- Pour les équipements où l'effacement des données n'est pas possible avant retrait (p. ex., la panne empêche l'accès), une évaluation documentée des risques doit être réalisée et les obligations de traitement des données du prestataire confirmées par écrit.

### Vérification physique après maintenance

- Après maintenance, les équipements doivent être physiquement inspectés avant d'être remis en service pour vérifier qu'aucune modification non autorisée n'a été apportée.
- Tous les outils et équipements apportés sur site par le personnel de maintenance doivent être comptabilisés avant et après la maintenance.
- Les versions du micrologiciel et des logiciels doivent être vérifiées après maintenance pour confirmer l'absence de modifications non autorisées.

### Contrôles d'accès pour la maintenance

- L'accès à la maintenance doit être limité dans le temps. Les fenêtres d'accès doivent être convenues à l'avance et documentées.
- Tout accès à des fins de maintenance doit être journalisé : qui a effectué le travail, quand, quels équipements ont été accédés et quel travail a été réalisé.
- Des identifiants d'accès temporaires (badges, accès système) doivent être délivrés au personnel de maintenance, avec expiration à la fin de la fenêtre de maintenance.

---

## Maintenance à distance

La maintenance à distance introduit des risques supplémentaires. Les contrôles suivants doivent s'appliquer :

- La maintenance à distance doit être explicitement autorisée avant chaque session. L'autorisation permanente pour l'accès à distance n'est pas autorisée.
- Les sessions de maintenance à distance doivent utiliser des connexions chiffrées (VPN, SSH ou protocole sécurisé équivalent). L'accès à distance non chiffré n'est pas autorisé.
- Les sessions de maintenance à distance doivent être journalisées, y compris les heures de début/fin de session, l'identité de l'individu et les actions effectuées. L'enregistrement des sessions est recommandé pour les équipements critiques.
- L'accès à distance doit être désactivé lorsqu'il n'est pas activement utilisé. Les connexions d'accès à distance persistantes à des fins de maintenance ne doivent pas rester ouvertes.
- La maintenance à distance d'équipements contenant des données sensibles doit requérir la même autorisation que l'accès physique à ces équipements.
- Lorsque le prestataire de maintenance nécessite un accès à distance aux systèmes internes, un serveur relais dédié ou un hôte bastion avec authentification multifacteur doit être utilisé.

---

## Retrait et retour des équipements

Lorsqu'un équipement doit être retiré des locaux pour maintenance hors site :

1. **Autorisation** : le retrait doit être autorisé par écrit par le propriétaire de l'équipement ou son délégué désigné.
2. **Protection des données** : les données doivent être effacées de manière sécurisée avant retrait. Si l'effacement n'est pas possible, le support de stockage doit être retiré et conservé par l'organisation. L'approche de protection des données doit être documentée.
3. **Chaîne de possession** : un enregistrement de chaîne de possession doit être créé documentant : l'identification de l'équipement, l'état au retrait, la date/heure de retrait, l'autorisation par, le transporteur, la destination, la date de retour prévue.
4. **Inspection au retour** : à la réception, l'équipement doit être inspecté pour détecter tout sabotage, modification non autorisée et vérifier la configuration correcte. Les versions du micrologiciel et des logiciels doivent être vérifiées.
5. **Mise à jour du registre des actifs** : le retour de l'équipement doit être journalisé dans [Système de gestion des actifs] avec un résumé de maintenance et les résultats d'inspection.

---

## Réponse aux incidents de défaillance d'infrastructure

Les défaillances d'infrastructure (dommages de câbles, dysfonctionnements d'équipements) qui impactent ou peuvent impacter les services doivent être gérées via le processus de gestion des incidents de l'organisation.

### Classification des incidents pour les événements d'infrastructure

| Gravité | Définition | Exemples | Délai de réponse | Notification |
|---------|-----------|----------|-----------------|--------------|
| **P1 - Critique** | Interruption complète du service ou risque imminent | Panne de l'alimentation principale, panne du commutateur réseau cœur, coupure complète de câble | Réponse immédiate ; objectif de rétablissement en 1 heure | RSSI, Direction générale, clients affectés immédiatement |
| **P2 - Élevée** | Dégradation significative du service ; redondance perdue | Panne ASI (alimentation secteur opérationnelle), panne de lien de secours, dommage partiel de câble | Réponse en 2 heures ; objectif de rétablissement en 4 heures | Responsable de l'exploitation informatique, RSSI, notification client si ANS impacté |
| **P3 - Moyenne** | Dégradation mineure ; redondance intacte | Panne d'un serveur unique (en cluster), panne d'un climatiseur (secours opérationnel) | Réponse en 4 heures ; objectif de rétablissement en 24 heures | Responsable de l'exploitation informatique |
| **P4 - Faible** | Aucun impact actuel sur les services ; alertes de surveillance | Batterie ASI vieillissante, équipement chauffe mais dans les tolérances | Réponse le prochain jour ouvrable ; maintenance planifiée | Exploitation informatique |

### Processus de réponse aux incidents d'infrastructure

1. **Détection et journalisation**
   - Les alertes de surveillance de l'infrastructure ou les signalements d'utilisateurs déclenchent la création d'un incident
   - Ticket d'incident créé dans [Système de gestion des incidents] avec classification de gravité
   - Évaluation initiale : périmètre de l'impact, services affectés, clients affectés

2. **Escalade**
   - P1 : escalade immédiate au RSSI et au Responsable de l'exploitation informatique
   - P2 : escalade au Responsable de l'exploitation informatique dans les 30 minutes
   - P3/P4 : assigné à l'ingénieur de service

3. **Communication**
   - **Interne** : mises à jour du statut de l'incident toutes les 2 heures (P1), toutes les 4 heures (P2) jusqu'à résolution
   - **Client** : notification selon le tableau d'évaluation de l'impact sur les services ci-dessus ; mises à jour du statut selon les conditions des ANS
   - **Prestataires** : engagement des prestataires de maintenance selon les procédures d'escalade contractuelles

4. **Investigation et remédiation**
   - Analyse des causes profondes obligatoire pour tous les incidents P1/P2
   - Solutions de contournement temporaires documentées avec correctif permanent planifié
   - Pannes d'équipements : déterminer l'historique de maintenance, le statut de garantie, les besoins de remplacement

5. **Revue post-incident**
   - Incidents P1/P2 : revue post-incident dans les 5 jours ouvrables
   - Enseignements tirés : identifier les mesures préventives, les améliorations du programme de maintenance
   - Documentation : mettre à jour les procédures de maintenance, les normes de câblage ou les seuils de surveillance sur la base des constatations

### Collecte de preuves pour les incidents d'infrastructure

Les incidents d'infrastructure doivent documenter :
- Chronologie des événements (détection, escalade, actions prises, résolution)
- Évaluation de l'impact (services affectés, impact client, durée de l'arrêt)
- Analyse des causes profondes (âge de l'équipement, historique de maintenance, facteurs environnementaux)
- Actions de résolution (réparations, remplacements, modifications de configuration)
- Actions préventives (ajustements du calendrier de maintenance, améliorations de la surveillance)

Documentation de revue post-incident conservée 3 ans minimum.

---

## Registres de maintenance

### Exigences de documentation

Toute maintenance — préventive et corrective — doit être documentée :

- **Maintenance préventive** : date, identifiant de l'équipement, activités de maintenance réalisées, constatations, pièces remplacées, prochaine date de maintenance planifiée, personnel ayant réalisé le travail.
- **Maintenance corrective** : date, identifiant de l'équipement, description de la panne, cause profonde (le cas échéant), actions de réparation prises, pièces remplacées, résultats de vérification post-réparation, personnel ayant réalisé le travail.
- **Maintenance à distance** : date/heure de session, équipement accédé, identité de l'individu, actions effectuées, durée de la session.

### Conservation des enregistrements

- Les enregistrements de maintenance doivent être conservés pendant un minimum de 3 ans ou la durée de vie de l'équipement, selon la durée la plus longue.
- Les enregistrements doivent être disponibles pour audit à tout moment.
- Les enregistrements doivent être stockés dans [SGMM] ou un registre contrôlé équivalent.

### Analyse des tendances de maintenance

- Les enregistrements de maintenance doivent être révisés trimestriellement pour identifier les tendances : pannes récurrentes, équipements approchant de leur fin de vie, fréquence de pannes croissante ou violations des ANS de maintenance.
- L'analyse des tendances doit informer la planification du remplacement des équipements et les ajustements du programme de maintenance.
- Des rapports trimestriels d'analyse des tendances doivent être fournis au Responsable de l'exploitation informatique et au RSSI.

---

## Surveillance des performances de l'infrastructure

Au-delà des métriques d'achèvement de maintenance, l'organisation doit surveiller les indicateurs de santé de l'infrastructure pour permettre la maintenance prédictive et démontrer l'efficacité de la disponibilité.

### Surveillance de la santé des équipements

| Métrique | Méthode de surveillance | Seuil d'alerte | Fréquence de révision |
|----------|------------------------|----------------|----------------------|
| **Santé de la batterie ASI** | Test d'impédance de batterie | > 20 % de dégradation par rapport à la valeur de référence | Analyse de tendance mensuelle |
| **Capacité d'autonomie ASI** | Test annuel sous charge | < 90 % de l'autonomie nominale | Annuellement avec tendance |
| **Température des équipements** | Système de surveillance environnementale | > 80 % de la température de fonctionnement maximale | Alertes continues |
| **Erreurs d'équipements réseau** | Surveillance SNMP / syslog | > 0,1 % de taux d'erreur d'interface | Révision quotidienne |
| **Santé matérielle des serveurs** | Surveillance de l'interface de gestion (iDRAC, iLO) | Alertes de panne prédictive | Alertes continues |
| **Performances CVC** | Capteurs de température/humidité | Temp > 24 °C ou < 18 °C ; HR > 60 % ou < 40 % | Alertes continues |
| **Tendances de consommation électrique** | Surveillance PDU | > 80 % de la capacité nominale | Tendance mensuelle |
| **Problèmes d'infrastructure de câblage** | Tickets d'assistance, constatations de rondes | Tout dommage, modifications non autorisées | Révision trimestrielle |

### Déclencheurs de maintenance prédictive

La surveillance de la santé doit déclencher des actions de maintenance précoces avant panne :

| Indicateur | Seuil de déclenchement | Action |
|-----------|----------------------|--------|
| Dégradation de la batterie ASI | 15-20 % de perte de capacité | Planifier le remplacement de la batterie dans les 30 jours |
| Température des équipements à la hausse | Moyenne sur 3 mois en hausse de > 5 °C | Investiguer le refroidissement, planifier un nettoyage approfondi |
| Erreurs d'interface réseau en augmentation | Tendance sur 3 mois montrant un doublement des erreurs | Planifier le test des câbles, inspection de l'interface |
| Alerte de panne prédictive matérielle de serveur | Erreur SMART, erreurs ECC mémoire | Planifier le remplacement avant panne ; vérification de sauvegarde |

### Tableau de bord des métriques de disponibilité

Reporting mensuel au Responsable de l'exploitation informatique et au RSSI :

| Métrique | Cible | Calcul |
|----------|-------|--------|
| **Arrêt d'infrastructure non planifié** | < 20 heures par an | Somme de toutes les durées d'incidents P1/P2 |
| **Arrêt planifié pour maintenance** | < 24 heures par an | Somme de toutes les durées de fenêtres de maintenance impactant les services |
| **Disponibilité de l'infrastructure** | > 99,5 % | (Heures totales - heures d'arrêt) / Heures totales × 100 % |
| **Temps moyen entre pannes (MTBF)** | Tendance à la hausse | Suivi par catégorie d'équipement |
| **Temps moyen de réparation (MTTR)** | < 4 heures (P1/P2) | Délai moyen de la détection à la résolution |
| **Conformité de la maintenance préventive** | 100 % | Réalisées dans les délais / Total planifié × 100 % |
| **Équipements au-delà de leur fin de vie** | 0 équipement critique | Nombre d'équipements critiques dépassant la date de fin de vie du fabricant |

**Analyse trimestrielle des tendances** : réviser les métriques pour les tendances se dégradant ; ajuster le programme de maintenance ou planifier les remplacements d'équipements.

---

## Définitions

| Terme | Définition |
|-------|------------|
| **Câblage structuré** | Infrastructure de câblage normalisée (cuivre et fibre optique) suivant les normes industrielles (IEC 11801, EN 50173, TIA-568) qui fournit un cadre flexible et fiable pour les communications voix, données et vidéo |
| **Infrastructure de câblage** | Tous les câbles électriques et de communication, conduits, cheminements, panneaux de brassage, répartiteurs et points de terminaison |
| **Câble à fibre optique** | Câble contenant une ou plusieurs fibres optiques qui transmettent les données sous forme d'impulsions lumineuses, offrant une bande passante plus élevée, des distances plus longues, une immunité aux EMI et une plus grande résistance à l'interception que le câble en cuivre |
| **Maintenance préventive** | Maintenance planifiée réalisée à des intervalles définis pour prévenir les pannes d'équipements et maintenir les performances dans les spécifications |
| **Maintenance corrective** | Maintenance non planifiée réalisée pour remettre un équipement en état opérationnel suite à une panne ou une défaillance |
| **Maintenance à distance** | Maintenance réalisée via un accès réseau à distance sans présence physique à l'emplacement de l'équipement |
| **Chaîne de possession** | Enregistrement chronologique documenté du transfert de responsabilité pour un équipement, suivant la possession du retrait à la maintenance jusqu'au retour |
| **SGMM** | Système de gestion de la maintenance assistée par ordinateur — logiciel utilisé pour planifier, suivre et documenter les activités de maintenance |
| **EMI** | Interférences électromagnétiques — bruit électrique indésirable provenant de sources externes pouvant dégrader la qualité du signal dans les câbles de données |

---

## Rôles et responsabilités

| Rôle | Responsabilités liées au câblage et à la maintenance |
|------|------------------------------------------------------|
| **Direction générale** | Approuver la politique ; allouer le budget pour la maintenance de l'infrastructure et les mises à niveau de l'installation de câblage |
| **RSSI** | Propriété de la politique ; normes de sécurité pour les activités de maintenance ; acceptation des risques pour les exceptions ; reporting trimestriel sur la conformité de l'infrastructure |
| **Responsable de l'exploitation informatique** | Propriété du programme de maintenance des équipements ; gestion des prestataires de maintenance ; supervision du calendrier de maintenance ; révision de l'analyse des tendances |
| **Responsable des installations** | Propriété de l'infrastructure de câblage ; maintenance et inspection de l'installation de câblage ; coordination des services du bâtiment ; gestion des cheminements physiques |
| **Propriétaires de systèmes** | S'assurer que les équipements dont ils sont propriétaires sont inclus dans le programme de maintenance ; autoriser le retrait des équipements ; définir les exigences de protection des données pour la maintenance |
| **Exploitation informatique** | Exécution et coordination quotidiennes de la maintenance ; tenue des registres de maintenance ; gestion des sessions de maintenance à distance |
| **Audit interne** | Vérification annuelle de la conformité du programme de maintenance ; audit de l'infrastructure de câblage ; révision des preuves |
| **Tous les employés** | Signaler rapidement les dommages présumés de câbles, les pannes d'équipements ou les modifications d'infrastructure non autorisées |

### Chemin d'escalade

- Dommages de câbles ou modifications non autorisées découverts : l'individu signalant notifie le Responsable des installations. Le Responsable des installations évalue l'impact et notifie le RSSI si cela est pertinent pour la sécurité.
- Défaillances de maintenance d'équipements : l'exploitation informatique notifie le Responsable de l'exploitation informatique. Les défaillances d'équipements critiques escaladent au RSSI.
- Préoccupations de sécurité pendant la maintenance : tout membre du personnel notifie directement le RSSI.

---

## Preuves

Les preuves suivantes démontrent la conformité à cette politique. **Pour les audits SOC 2 Type II**, les auditeurs testeront l'efficacité opérationnelle sur la période d'audit (typiquement 12 mois).

| N° | Preuve | Responsable | Fréquence | Exigences de piste d'audit |
|----|--------|-------------|-----------|---------------------------|
| 1 | **Registre du câblage / base de données de gestion du câblage** documentant tout le câblage structuré avec type, extrémités, tracé et classification | Responsable des installations | *Maintenu en continu ; révisé annuellement* | Registre à jour avec historique des versions montrant les mises à jour |
| 2 | **Plans de recollement du câblage** pour toutes les installations, à jour et sous contrôle de version | Responsable des installations | *Mis à jour dans les 5 jours ouvrables des modifications ; révisé annuellement* | Versions des plans corrélées avec les enregistrements de modifications |
| 3 | **Rapports de rondes trimestrielles du câblage** avec constatations, réconciliation avec les plans et validation | Responsable des installations | *Trimestriellement ; conservé 3 ans* | Rapport de ronde signé avec constatations et actions de remédiation |
| 4 | **Enregistrements de test du câblage** (continuité, performance) pour les nouvelles installations et la vérification annuelle | Responsable des installations | *Annuellement et par installation ; conservé 3 ans* | Rapports de test avec résultats réussite/échec par norme de câblage |
| 5 | **Programme de maintenance** montrant tous les équipements dans le périmètre avec des calendriers alignés sur les recommandations du fabricant | Responsable de l'exploitation informatique | *Révisé trimestriellement ; conservé 3 ans* | Document de programme avec validation de révision trimestrielle |
| 6 | **Réconciliation trimestrielle** de l'inventaire des actifs par rapport à la couverture du programme de maintenance | Responsable de l'exploitation informatique | *Trimestriellement ; conservé 3 ans* | Rapport de réconciliation avec pourcentage de couverture et remédiation des lacunes |
| 7 | **Enregistrements de maintenance préventive** documentant la maintenance réalisée avec les constatations et la prochaine date planifiée | Exploitation informatique | *Par événement de maintenance ; conservé 3 ans minimum* | Enregistrements de maintenance individuels avec horodatages de réalisation |
| 8 | **Enregistrements de maintenance corrective** documentant les pannes, la cause profonde, les actions de réparation et la vérification post-réparation | Exploitation informatique | *Par événement ; conservé 3 ans minimum* | Enregistrements de maintenance liés aux incidents avec analyse des causes profondes |
| 9 | **Enregistrements d'autorisation du personnel de maintenance** (interne et tiers) | Responsable de l'exploitation informatique | *Révisé annuellement ; conservé 3 ans* | Registre des autorisations avec validation de révision annuelle |
| 10 | **Registre des prestataires de maintenance tiers** avec détails contractuels et révision annuelle | Responsable de l'exploitation informatique | *Révisé annuellement ; conservé actif + 2 ans* | Registre des prestataires avec résumés des contrats et dates de révision |
| 11 | **Journaux de sessions de maintenance à distance** avec identification individuelle, heures et actions | Exploitation informatique | *Par session ; conservé 3 ans* | Journaux de session avec enregistrements d'autorisation |
| 12 | **Enregistrements de retrait et de retour d'équipements** avec chaîne de possession, preuves de protection des données et inspection au retour | Exploitation informatique | *Par événement ; conservé 3 ans* | Formulaires de chaîne de possession avec validation d'inspection |
| 13 | **Rapports d'analyse des tendances de maintenance** identifiant les problèmes récurrents et les recommandations sur le cycle de vie des équipements | Responsable de l'exploitation informatique | *Trimestriellement ; conservé 3 ans* | Rapport de tendances avec recommandations exploitables et réponse de la direction |
| 14 | **Registre des exceptions** pour les dérogations approuvées aux calendriers de maintenance ou aux normes de câblage | RSSI | *Par événement ; révisé trimestriellement ; conservé actif + 2 ans* | Enregistrements d'exceptions avec évaluation des risques et contrôles compensatoires |
| 15 | **Évaluations de l'impact sur les services** pour les activités de maintenance | Exploitation informatique | *Par événement de maintenance impactant les services* | Demande de modification montrant l'évaluation d'impact, l'approbation, la notification client (le cas échéant) |
| 16 | **Rapport d'utilisation des fenêtres de maintenance** | Responsable de l'exploitation informatique | *Trimestriellement* | Résumé montrant : temps d'arrêt planifié vs. budget de disponibilité, conformité ANS, notifications clients envoyées |
| 17 | **Métriques de disponibilité de l'infrastructure** | Responsable de l'exploitation informatique | *Mensuellement ; agrégé trimestriellement* | Tableau de bord montrant % de disponibilité, arrêt non planifié, MTBF, MTTR par catégorie d'équipement |
| 18 | **Enregistrements d'incidents d'infrastructure** (P1/P2) | Exploitation informatique | *Par incident* | Ticket d'incident avec : chronologie, analyse des causes profondes, impact client, résolution, revue post-incident |
| 19 | **Rapports de surveillance de la santé des équipements** | Exploitation informatique | *Mensuellement* | Tendances de santé de la batterie ASI, surveillance de la température, tendances des taux d'erreur, alertes de panne prédictive |
| 20 | **Tableaux de bord de performance des prestataires** | Responsable de l'exploitation informatique | *Trimestriellement par prestataire* | Données de conformité ANS, métriques de qualité, suivi des incidents de sécurité, satisfaction client |
| 21 | **Bilans annuels des prestataires** | Responsable de l'exploitation informatique | *Annuellement par prestataire* | Document de bilan avec évaluation des performances, recommandation de renouvellement/remplacement, signature d'approbation |
| 22 | **Résultats des tests d'infrastructure de reprise** | Responsable de l'exploitation informatique | *Annuellement (ou par test de reprise)* | Rapport de test de reprise couvrant le test de basculement de l'infrastructure, les constatations, les actions correctives |
| 23 | **Enregistrements de gestion des modifications du câblage** | Responsable des installations | *Par modification du câblage* | Demande de modification, approbation, résultats de test, mises à jour des plans de recollement, validation de réalisation |

### Attentes des tests SOC 2 Type II

Les auditeurs vont généralement échantillonner :
- **25 événements de maintenance préventive** sur la période d'audit (vérifier la planification, la réalisation dans les délais, la documentation)
- **Tous les incidents d'infrastructure P1/P2** (vérifier la classification, l'escalade, la notification client, la revue post-incident)
- **Toutes les révisions des performances des prestataires** (vérifier la réalisation, le suivi des métriques, les décisions documentées)
- **Toutes les modifications d'infrastructure de câblage** (vérifier l'approbation des modifications, les tests, les mises à jour de documentation)
- **Les réconciliations trimestrielles** (inventaire des actifs vs. couverture du programme de maintenance)
- **Les métriques de disponibilité mensuelles** (vérifier l'exactitude, l'analyse des tendances, l'escalade des problèmes)

**L'exhaustivité est critique** : toute preuve manquante pour un élément de l'échantillon = constatation d'audit.

---

# Conformité à la politique

## Mesure de la conformité

L'équipe de gestion de la sécurité de l'information vérifiera la conformité à cette politique par diverses méthodes, notamment les audits de l'infrastructure de câblage, les revues du programme de maintenance, les audits des enregistrements de maintenance, les inspections physiques, les évaluations de conformité des prestataires, les audits internes et externes, et les retours adressés au propriétaire de la politique.

Les métriques suivantes doivent être suivies et communiquées au RSSI trimestriellement :

| Métrique | Cible | Seuil rouge |
|----------|-------|-------------|
| Maintenance préventive réalisée dans les délais | 100 % | < 85 % |
| Pannes d'équipements attribuables à une maintenance manquée ou inadéquate | 0 | Toute occurrence |
| Exactitude de la documentation du câblage (constatations de rondes vs. plans) | > 95 % | < 85 % |
| Modifications de câblage non autorisées détectées | 0 | Toute occurrence |
| Incidents de sécurité liés à la maintenance | 0 | Toute occurrence |
| Réconciliation inventaire des actifs / programme de maintenance | Couverture à 100 % | < 90 % de couverture |
| Personnel de maintenance tiers correctement autorisé et supervisé | 100 % | < 95 % |

## Exceptions

Toute exception à cette politique doit être approuvée et enregistrée par le RSSI à l'avance, avec une évaluation documentée des risques, des contrôles compensatoires et une date de révision définie (maximum 6 mois, renouvelable). Les scénarios d'exception valables comprennent :

- Maintenance différée pour les systèmes critiques lorsqu'une fenêtre de maintenance ne peut pas être planifiée sans impact commercial inacceptable (avec surveillance compensatoire).
- Intervalles de maintenance prolongés pour les équipements de faible criticité (avec justification documentée et consultation du fabricant le cas échéant).
- Utilisation de câbles en cuivre dans des emplacements où la fibre optique est spécifiée mais l'installation n'est pas possible (avec contrôles compensatoires de blindage et protection physique).
- Maintenance par des tiers sans supervision complète (avec journalisation renforcée et inspection post-maintenance).

Les exceptions doivent être enregistrées dans le Registre des exceptions et signalées à l'équipe de revue de direction.

**Non autorisé** :

- Ignorer la maintenance de sécurité critique (ASI, systèmes incendie, systèmes de sécurité) sans contrôles compensatoires.
- Modifications de câblage non documentées.
- Maintenance par des tiers non supervisée et non journalisée sur des équipements contenant des données sensibles.
- Exceptions permanentes à la couverture du programme de maintenance.

## Non-conformité

Un employé dont il est établi qu'il a enfreint cette politique peut faire l'objet de mesures disciplinaires, pouvant aller jusqu'au licenciement. Les modifications de câblage effectuées sans autorisation ou documentation doivent être traitées comme un incident de sécurité et faire l'objet d'une enquête. La maintenance d'équipements contournée sans approbation doit être signalée au RSSI pour évaluation des risques.

## Amélioration continue

Cette politique est révisée et mise à jour dans le cadre du processus d'amélioration continue. Les révisions doivent tenir compte des modifications apportées aux opérations des installations, à la technologie de l'infrastructure, aux normes de câblage, aux recommandations de maintenance des fabricants, au statut du cycle de vie des équipements, aux exigences réglementaires, aux constatations d'audit, aux tendances des incidents et aux enseignements tirés des pannes d'équipements. Les non-conformités liées à cette politique doivent être enregistrées et gérées via le processus d'action corrective du SMSI (Clause 10.2) avec analyse des causes profondes et suivi de la remédiation.

---

# Domaines de la norme ISO 27001 couverts

Politique de sécurité du câblage et de maintenance des équipements — Correspondance avec les contrôles ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership et engagement | 5.1 Politiques de sécurité de l'information |
| Clause 5.2 Politique | 5.9 Inventaire des informations et autres actifs associés |
| Clause 6.1 Actions pour traiter les risques et opportunités | 5.30 Préparation des TIC pour la continuité d'activité |
| Clause 7.3 Sensibilisation | 7.4 Surveillance de la sécurité physique |
| Clause 8.1 Planification et contrôle opérationnels | 7.5 Protection contre les menaces physiques et environnementales |
| Clause 9.1 Surveillance, mesure, analyse et évaluation | 7.8 Implantation et protection des équipements |
| Clause 10.2 Non-conformité et action corrective | **7.12 Sécurité du câblage** |
| | **7.13 Maintenance des équipements** |
| | 7.14 Mise au rebut ou réutilisation sécurisée des équipements |
| | 8.32 Gestion des changements |

**Cadre réglementaire et juridique** :

| Cadre | Pertinence |
|-------|-----------|
| nLPD suisse (revDSG) | Art. 8 — Mesures techniques et organisationnelles pour la sécurité physique de l'infrastructure de traitement des données |
| OPDo suisse (Ordonnance sur la protection des données) | Art. 1-3 — Exigences minimales de sécurité des données incluant les mesures physiques |
| NIN suisse (Niederspannungs-Installationsnorm) | Normes d'installation électrique basse tension applicables au câblage électrique dans les bâtiments |
| Ordonnance fédérale suisse sur les installations à basse tension (RS 734.27) | Conditions préalables et exigences d'inspection pour les installations électriques |
| RGPD de l'UE (le cas échéant) | Art. 32 — Sécurité du traitement incluant les mesures d'infrastructure physique |
| ISO/IEC 27001:2022 | Contrôles Annexe A 7.12 (Sécurité du câblage), 7.13 (Maintenance des équipements) |
| ISO/IEC 27002:2022 | Sections 7.12, 7.13 — Recommandations de mise en œuvre pour la sécurité du câblage et la maintenance des équipements |
| IEC 11801 / EN 50173 | Normes de câblage structuré internationales et européennes pour le câblage générique dans les locaux clients |
| TIA-568 / TIA-942 | Normes de câblage structuré et de câblage de centre de données nord-américaines |
| NIST SP 800-53 Rev 5 | PE-4 (Contrôle d'accès pour la transmission), PE-9 (Équipements électriques et câblage), MA-2 (Maintenance contrôlée), MA-5 (Personnel de maintenance) |
| CIS Controls v8 | Contrôle 1 (Inventaire et contrôle des actifs d'entreprise), Contrôle 12 (Gestion de l'infrastructure réseau) |
| **Conditionnel** : Circulaire FINMA 2023/1 | Établissement financier réglementé suisse — exigences renforcées de résilience de l'infrastructure |
| **Conditionnel** : DORA (UE) 2022/2554 | Entité de services financiers de l'UE — résilience opérationnelle des TIC pour l'infrastructure |
| **Conditionnel** : NIS 2 (UE) 2022/2555 | Entité essentielle/importante dans l'UE — exigences de protection de l'infrastructure |

---

<!-- QA_VERIFIED: 2026-03-29 -->
