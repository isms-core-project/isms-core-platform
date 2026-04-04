<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.7.4-5-11-FR:operational:OP-POL:a.7.4-5-11 -->
**ISMS-OP-POL-A.7.4-5-11 — Sécurité de l'infrastructure physique**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Sécurité de l'infrastructure physique |
| **Type de document** | Politique opérationnelle |
| **Identifiant du document** | ISMS-OP-POL-A.7.4-5-11 |
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

- ISO/IEC 27001:2022 Contrôles A.7.4, A.7.5, A.7.11 — Surveillance de la sécurité physique, protection contre les menaces physiques et environnementales, services supports
- ISO/IEC 27002:2022 Sections 7.4, 7.5, 7.11 — Lignes directrices de mise en œuvre

**Contrôles Annexe A connexes** :

| Contrôle | Relation avec la sécurité de l'infrastructure physique |
|----------|-------------------------------------------------------|
| A.7.1 Périmètres de sécurité physique | Les limites du périmètre définissent la portée de surveillance et les zones de protection environnementale |
| A.7.2 Entrée physique | Les contrôles d'entrée génèrent des événements d'accès pour la surveillance et la corrélation |
| A.7.3 Sécurisation des bureaux, salles et installations | Les zones sécurisées nécessitent une protection environnementale et la résilience des services supports |
| A.7.8 Emplacement et protection des équipements | Le placement des équipements tient compte des conditions environnementales et de la disponibilité des services supports |
| A.7.12 Sécurité du câblage | L'intégrité du câblage d'alimentation et de télécommunications soutient la résilience des services supports |
| A.7.13 Maintenance des équipements | Calendriers de maintenance pour les systèmes environnementaux et de services supports |
| A.5.24–28 Cycle de vie de la gestion des incidents | Les incidents de sécurité physique et environnementaux sont escaladés vers la gestion des incidents |
| A.5.30 Préparation TIC à la continuité d'activité | La résilience des services supports soutient les objectifs de continuité d'activité |
| A.8.16 Activités de surveillance | Les événements de sécurité physique sont intégrés dans le SIEM pour une détection corrélée |

**Politiques internes connexes** :

- Politique de contrôle d'accès physique
- Politique de gestion des incidents
- Politique de continuité d'activité et de reprise après sinistre
- Politique de journalisation
- Politique des activités de surveillance (A.8.16)
- Politique de sécurité des services cloud et des fournisseurs
- Politique de gestion des actifs

---

# Politique de sécurité de l'infrastructure physique

## Objectif

L'objet de la présente politique est de protéger les installations de traitement de l'information et l'infrastructure associée grâce à la surveillance de la sécurité physique, à la protection contre les menaces environnementales et à la résilience des services supports. Elle établit des exigences en matière de surveillance continue, de protection contre l'incendie et l'eau, de contrôle climatique, et de continuité de l'alimentation électrique et des télécommunications.

La présente politique traite de trois contrôles ISO 27001:2022 connexes comme un cadre unifié, car ils opèrent sur la même infrastructure physique, créent des interdépendances et partagent des processus d'évaluation communs : la surveillance détecte les menaces (A.7.4), les contrôles environnementaux préviennent les dommages (A.7.5), et les systèmes de services supports maintiennent les opérations (A.7.11). Chaque contrôle maintient des exigences distinctes à des fins de Déclaration d'applicabilité.

La présente politique soutient la nLPD suisse (nFADP/revDSG) art. 8 en mettant en œuvre des mesures techniques et organisationnelles appropriées aux risques pour protéger la disponibilité, l'intégrité et la confidentialité des données personnelles grâce aux contrôles de sécurité de l'infrastructure physique. Lorsque l'organisation traite des données de personnes situées dans l'UE/EEE, les exigences de l'art. 32 du RGPD concernant la sécurité du traitement, y compris les mesures physiques, s'appliquent également.

## Champ d'application

Tous les employés et utilisateurs tiers.

Tous les locaux en propriété, loués ou en colocation par l'organisation, incluant :

- Centres de données sur site et sites de reprise après sinistre
- Salles de serveurs et armoires de télécommunications
- Bureaux d'entreprise (siège social, régionaux, agences)
- Installations de colocation (avec modèle de responsabilité partagée)
- Installations distantes et temporaires où sont situés des équipements appartenant à l'organisation

**Hors champ d'application** :

- Sécurité physique des appareils portables (couverte par A.7.9, A.8.1)
- Sécurité du transport des équipements (couverte par A.7.13)
- Stockage des supports de sauvegarde hors site (couvert par A.8.13)
- Sécurité du personnel et vérifications des antécédents (couverts par A.6.1–6.4)
- Sécurité des installations de tiers et de fournisseurs (couverte par A.5.19–23, à l'exception de la colocation comme indiqué ci-dessous)

### Organisations entièrement dans le cloud

Les organisations opérant à 100 % dans des environnements cloud sans installations de traitement de l'information sur site peuvent marquer les Contrôles A.7.4, A.7.5 et A.7.11 comme « Non applicable » dans la Déclaration d'applicabilité.

La décision « Non applicable » devra être documentée avec :

- Référence à l'inventaire des actifs confirmant l'absence d'installations de traitement de l'information sur site.
- Vérification de la sécurité physique du prestataire cloud par rapport SOC 2 Type II ou examen de la certification ISO 27001.
- Confirmation lors de la révision annuelle que le statut entièrement cloud reste exact.

La sécurité physique du prestataire cloud devra être évaluée dans le cadre du processus de gestion des fournisseurs (A.5.19–23).

### Installations de colocation

Lors de l'utilisation d'espaces de centres de données en colocation, les responsabilités d'infrastructure physique sont partagées entre le prestataire de colocation et l'organisation. L'organisation devra :

- Maintenir une matrice de responsabilités formelle dans le contrat de colocation documentant quelle partie est responsable de chaque contrôle d'infrastructure physique (surveillance, environnemental, services supports).
- Vérifier les contrôles du prestataire annuellement par des rapports d'audit SOC 2 Type II ou une certification ISO 27001.
- Conserver la responsabilité des contrôles de surveillance et environnementaux dans l'espace alloué à l'organisation (p. ex., surveillance environnementale au niveau des baies, contrôles d'accès aux cages).

## Principe

La sécurité physique et environnementale est construite sur le principe de la protection des installations de traitement de l'information contre les accès non autorisés, les menaces environnementales et les défaillances des services supports — proportionnellement à la criticité des actifs qu'elles contiennent. Les contrôles devront être sélectionnés sur la base d'une évaluation documentée des risques et de la classification des niveaux de criticité des installations définie dans la présente politique.

---

## Surveillance de la sécurité physique (A.7.4)

> *Les locaux devraient être surveillés en permanence pour détecter tout accès physique non autorisé.*

La surveillance de la sécurité physique devrait détecter et dissuader les accès physiques non autorisés aux installations et aux zones restreintes. La conception et la mise en œuvre du système de surveillance devront être proportionnelles à la criticité des installations.

### Systèmes de sécurité physique

Les systèmes de sécurité physique suivants devront être mis en œuvre et maintenus. Les organisations devront préciser les systèmes réellement déployés (ou documenter l'état de sélection) pour chaque catégorie :

| Catégorie de système | Objet | Exemples de solutions | Statut |
|---------------------|-------|----------------------|--------|
| **Système de contrôle d'accès** | Entrée/sortie par badge avec journalisation des événements | Verkada, Genetec, Honeywell, Lenel, ASSA ABLOY, Salto | [Préciser ou « Sélection en cours »] |
| **CCTV / vidéosurveillance** | Surveillance visuelle et enregistrement | Verkada, Axis, Milestone, Genetec | [Préciser ou « Sélection en cours »] |
| **Détection d'intrusion** | Détection de violation du périmètre et de l'intérieur | Honeywell, Bosch, DSC, Texecom | [Préciser ou « Sélection en cours »] |
| **Service de surveillance des alarmes** | Réponse et intervention sur alarme 24h/24, 7j/7 | Securitas, Protectas, centrale de surveillance locale | [Préciser ou « Sélection en cours »] |
| **Surveillance environnementale** | Capteurs de température, d'humidité, de détection d'eau | Paessler PRTG, Raritan, APC NetBotz, Sensaphone | [Préciser ou « Sélection en cours »] |
| **Système de gestion technique du bâtiment (GTB)** | Contrôle centralisé des services du bâtiment (CVC, éclairage, alimentation) | Siemens Desigo, Honeywell Niagara, Schneider EcoStruxure | [Préciser ou « Sélection en cours »] |
| **Détection et extinction incendie** | Détection fumée/chaleur et extinction à agent propre | Siemens, Minimax, Kidde, Wagner | [Préciser ou « Sélection en cours »] |
| **Systèmes ASI** | Alimentation sans interruption pour les équipements critiques | Eaton, APC/Schneider, Vertiv/Liebert, Riello | [Préciser ou « Sélection en cours »] |
| **Groupe électrogène de secours** | Continuité étendue de l'alimentation électrique | Caterpillar, Cummins, MTU, SDMO | [Préciser ou « Sélection en cours »] |

**Exigences d'intégration** : Lorsque cela est techniquement réalisable, les systèmes de sécurité physique devraient transmettre des événements au [SIEM] pour corrélation avec les événements de sécurité logique. Au minimum, les événements de contrôle d'accès et les alarmes de détection d'intrusion devront être transmis.

### Contrôle d'accès électronique

- Un contrôle d'accès électronique devra être mis en œuvre à tous les points d'entrée et de sortie des installations, avec authentification, journalisation des événements et intégration à la gestion des identités.
- Les événements d'accès (accordés, refusés, porte forcée, porte maintenue ouverte) devront être consignés avec horodatage, identité de la personne et identifiant de la porte.
- Les journaux d'accès devront être conservés pendant un minimum de 12 mois.
- Les droits d'accès devront être révisés semestriellement et révoqués lorsqu'ils ne sont plus requis (p. ex., changement de rôle, résiliation).
- La révocation d'accès le jour même devra être appliquée lors de la résiliation de l'emploi.

#### Processus de révision des droits d'accès

Les droits d'accès physique devront être révisés semestriellement selon le flux de travail structuré suivant :

| Étape | Action | Responsable | Délai |
|-------|--------|-------------|-------|
| 1 | Générer un rapport des droits d'accès depuis [Système de contrôle d'accès] listant tout le personnel par zone et département | Responsable des installations | 1er jour ouvrable du mois de révision |
| 2 | Distribuer les listes d'accès par zone aux responsables habilités pour attestation | Responsable des installations | Dans les 2 jours ouvrables |
| 3 | Les responsables révisent l'accès de chaque personne : confirment requis, signalent pour suppression, ou escaladent les questions | Responsables hiérarchiques | Dans les 10 jours ouvrables |
| 4 | Compiler les réponses des responsables ; générer la liste de révocation pour les accès qui ne sont plus requis | Responsable des installations | Dans les 2 jours ouvrables suivant l'échéance d'attestation |
| 5 | Exécuter les révocations d'accès dans [Système de contrôle d'accès] | Responsable des installations | Dans les 5 jours ouvrables |
| 6 | Confirmer les révocations effectuées ; classer les dossiers d'attestation | Responsable des installations | Dans les 2 jours ouvrables |

**Escalade en cas de non-réponse** :
- Non-réponse du responsable à 10 jours ouvrables → Rappel envoyé avec extension de 5 jours
- Non-réponse du responsable à 15 jours ouvrables → Escalade au responsable de département
- Non-réponse du responsable à 20 jours ouvrables → Accès du personnel non attesté dans les zones Restreintes suspendu dans l'attente de l'attestation

**Indicateurs de réalisation** :
- Objectif : 100 % des droits d'accès révisés par cycle
- Objectif : Toutes les révocations exécutées dans les 5 jours ouvrables suivant l'attestation
- Non-conformité rapportée au RSSI dans le rapport de conformité trimestriel

### Vidéosurveillance (CCTV)

- Une couverture CCTV devra être assurée aux entrées des installations, aux points d'accès des zones restreintes et aux emplacements d'infrastructure critique (salles de serveurs, locaux techniques).
- Les systèmes CCTV devront enregistrer en continu pendant les heures opérationnelles au minimum ; un enregistrement 24h/24, 7j/7 est requis pour les installations de Niveau 1.
- Conservation des enregistrements : minimum 30 jours pour les zones générales, 90 jours pour les zones restreintes. Une conservation plus longue peut être requise pour l'investigation d'incidents.
- Les systèmes CCTV devront respecter les exigences applicables en matière de protection des données (nLPD suisse, réglementations cantonales). Une signalétique indiquant la vidéosurveillance devra être affichée dans les zones surveillées.
- La santé des caméras (connectivité, qualité de l'image, capacité de stockage) devra être vérifiée hebdomadairement.

### Détection d'intrusion

- Des systèmes de détection d'intrusion (SDI) devront être installés dans les installations de Niveau 1, couvrant les portes du périmètre, les fenêtres et les points d'accès aux zones restreintes.
- La détection d'intrusion est recommandée pour les installations de Niveau 2 sur la base d'une évaluation des risques.
- Les alarmes devront être connectées à un point de réponse surveillé (centre d'opérations de sécurité, service de surveillance des alarmes, ou [Prestataire de surveillance des alarmes]).
- Le SDI devra être testé trimestriellement pour confirmer son bon fonctionnement.

### Gestion des visiteurs

- Tous les visiteurs devront s'enregistrer à l'arrivée, recevoir une identification temporaire et être accompagnés dans les zones restreintes.
- Les dossiers des visiteurs (nom, organisation, hôte, heure d'arrivée/départ) devront être conservés pendant un minimum de 12 mois.
- Les badges des visiteurs devront identifier clairement le statut de visiteur, refuser l'accès aux zones restreintes et expirer à la fin de la journée ouvrée à laquelle ils ont été émis.

### Surveillance des événements de sécurité et intégration

- Les événements de sécurité physique (accès refusé, entrée forcée, alarme d'intrusion, porte maintenue ouverte) devraient être transmis au [SIEM] pour corrélation avec les événements de sécurité logique lorsque cela est techniquement réalisable.
- Les tentatives d'accès répétées échouées (3 ou plus en 30 minutes) devront déclencher une alerte et une investigation.

### Protection des systèmes de surveillance

- La conception et la configuration des systèmes de surveillance devront être maintenues confidentielles.
- Les systèmes de surveillance devront être protégés contre la falsification, la désactivation non autorisée et les interférences à distance.
- Les équipements de surveillance devront être alimentés par une ASI pour assurer leur fonctionnement continu en cas d'interruption d'alimentation.

---

## Protection environnementale (A.7.5)

> *La protection contre les menaces physiques et environnementales devrait être conçue et mise en œuvre.*

Les contrôles de protection environnementale devront prévenir ou atténuer les dommages causés par l'incendie, l'eau, les extrêmes climatiques et autres menaces physiques. Les niveaux de protection devront être proportionnels à la criticité des installations.

### Évaluation des menaces environnementales

- Une évaluation des risques liés aux menaces environnementales devra être conduite pour chaque installation, en tenant compte de l'emplacement géographique, des caractéristiques du bâtiment, des événements historiques et des risques environnants.
- L'évaluation devra être révisée annuellement et mise à jour après des incidents ou des changements importants des installations.
- Les menaces à considérer incluent : incendie, inondation, infiltration d'eau, températures extrêmes, humidité, foudre, activité sismique, défaillance structurelle, troubles civils et risques industriels.

### Détection et extinction incendie

La détection incendie devra être mise en œuvre dans toutes les installations contenant des équipements de traitement de l'information.

| Exigence | Niveau 1 — Installations critiques | Niveau 2 — Installations standard |
|----------|-------------------------------------|------------------------------------|
| **Détection** | Détection fumée (VESDA/par aspiration ou conventionnelle) dans toutes les zones ; détection chaleur dans les locaux techniques | Détection fumée conventionnelle dans les zones serveurs/équipements |
| **Extinction** | Extinction à agent propre (gaz inerte, p. ex., IG-541/Inergen, IG-55/Argonite, ou équivalent) dans les salles de serveurs et les espaces de centres de données | Extinction requise lorsque la valeur des équipements dépasse CHF 500 000 ou que la criticité des données le justifie ; extincteurs portables ailleurs |
| **Intégration des alarmes** | Connecté au GTB, aux pompiers et à la surveillance de sécurité | Connecté au tableau d'alarme incendie du bâtiment |
| **Inspection** | Inspection semestrielle et test annuel complet conformément aux réglementations cantonales d'incendie | Inspection annuelle conformément aux réglementations cantonales d'incendie |

**Notes sur les agents d'extinction** : Les systèmes à agent propre conformes à la NFPA 2001 et à l'ISO 14520 sont requis pour les espaces occupés contenant des équipements électroniques. Les systèmes d'arrosage à eau ne devront pas être utilisés dans les salles de serveurs ou les centres de données. Les organisations devraient prendre en compte la disponibilité à long terme et le profil environnemental des agents sélectionnés lors de la spécification des systèmes d'extinction.

#### Guide de sélection des agents d'extinction incendie

Les organisations sélectionnant des systèmes d'extinction à agent propre pour les salles de serveurs et les centres de données devraient évaluer les options sur la base de l'efficacité, de la sécurité, du profil environnemental et de la disponibilité réglementaire à long terme :

| Agent | Type | Appauvrissement de la couche d'ozone | Potentiel de réchauffement global | Sécurité (espaces occupés) | Perspective de disponibilité | Recommandation |
|-------|------|---------------------------------------|-----------------------------------|---------------------------|------------------------------|----------------|
| **IG-541 (Inergen)** | Mélange de gaz inertes (N₂, Ar, CO₂) | Zéro | Zéro | Sûr — respirable à la concentration de conception | Stable à long terme | **Recommandé** pour les nouvelles installations |
| **IG-55 (Argonite)** | Mélange de gaz inertes (N₂, Ar) | Zéro | Zéro | Sûr — respirable à la concentration de conception | Stable à long terme | Alternative recommandée |
| **IG-100 (Azote)** | Azote pur | Zéro | Zéro | Sûr — respirable à la concentration de conception | Stable à long terme | Adapté aux grands volumes |
| **FK-5-1-12 (Novec 1230)** | Fluorocétone | Zéro | 1 | Sûr — faible toxicité | Stable (production 3M se poursuit) | Acceptable pour les installations à espace limité |
| **HFC-227ea (FM-200)** | Hydrofluorocarbure | Zéro | 3 220 | Sûr — faible toxicité à la concentration de conception | **Réduction progressive** en vertu du Règlement UE sur les gaz fluorés et de l'Amendement de Kigali | **Non recommandé** pour les nouvelles installations |

**Critères de sélection pour les nouvelles installations** :
1. Systèmes à gaz inertes (IG-541, IG-55) préférés en raison de l'impact environnemental nul et de la certitude réglementaire à long terme
2. FK-5-1-12 (Novec 1230) acceptable lorsque l'espace de stockage des cylindres est limité (volume inférieur requis par rapport aux gaz inertes)
3. HFC-227ea (FM-200) non recommandé pour les nouvelles installations en raison de la trajectoire de réduction progressive réglementaire

**Systèmes FM-200 existants** : Aucun remplacement immédiat requis. Maintenir selon le calendrier du fabricant. Prévoir un budget de remplacement par un système à gaz inerte lors du prochain grand remaniement ou dans les 10 ans (selon ce qui survient en premier). Documenter le calendrier de remplacement dans le plan d'investissement des installations.

- Les portes coupe-feu sur les périmètres de sécurité devront être équipées d'alarmes, surveillées et testées conformément aux codes d'incendie applicables.
- L'éclairage de secours et les voies d'évacuation devront être maintenus et testés semestriellement.

### Détection et protection contre l'eau

- Des capteurs de détection d'eau devront être installés dans les installations de Niveau 1 — sous les faux planchers, au-dessus des faux plafonds, près de l'infrastructure de refroidissement, et dans toutes les zones où une infiltration d'eau est possible.
- Les installations de Niveau 2 devront disposer d'une détection d'eau dans les zones à haut risque (près de la plomberie, des systèmes CVC, des pièces au rez-de-chaussée).
- Les alarmes d'eau devront déclencher une alerte immédiate au responsable des installations.
- Les installations devront mettre en œuvre un drainage, une imperméabilisation et des barrières physiques appropriés au risque d'inondation identifié.

### Contrôle climatique

Les équipements de traitement de l'information devront être maintenus dans des plages contrôlées de température et d'humidité pour prévenir les dommages et assurer un fonctionnement fiable.

| Paramètre | Plage recommandée (classe ASHRAE A1–A4) | Seuil d'alerte | Seuil critique |
|-----------|----------------------------------------|-----------------|--------------------|
| **Température** | 18–27 °C (64–81 °F) | En dehors de 18–27 °C | En dessous de 15 °C ou au-dessus de 32 °C |
| **Humidité** | 20–80 % d'humidité relative (HR) | En dehors de 20–80 % HR | En dessous de 10 % HR ou au-dessus de 90 % HR |
| **Taux de variation de température** | < 5 °C par heure | Dépasse 5 °C/h | Dépasse 10 °C/h |

**Installations de Niveau 1** : La température devra être maintenue entre 18–27 °C avec une tolérance de +/- 2 °C. Une surveillance environnementale continue avec alerte en temps réel est requise.

**Installations de Niveau 2** : La température devra être maintenue entre 18–27 °C avec une tolérance de +/- 5 °C. Une surveillance environnementale avec alerte pendant les heures de présence du personnel est requise.

Les données de surveillance environnementale (température, humidité) devront être journalisées et conservées pendant un minimum de 12 mois.

#### Configuration des alertes du système de surveillance environnementale

Les systèmes de surveillance environnementale devront être configurés avec les seuils d'alerte, les exigences de réponse et les chemins d'escalade suivants :

| Paramètre | Alerte d'avertissement | Alerte critique | Délai de réponse (Niveau 1) | Délai de réponse (Niveau 2) |
|-----------|----------------------|-----------------|----------------------------|----------------------------|
| **Température** | En dehors de 18–27 °C | En dessous de 15 °C ou au-dessus de 32 °C | 15 minutes | Prochain jour ouvrable |
| **Humidité** | En dehors de 20–80 % HR | En dessous de 10 % ou au-dessus de 90 % HR | 15 minutes | Prochain jour ouvrable |
| **Taux de variation de température** | Dépasse 5 °C/heure | Dépasse 10 °C/heure | 15 minutes | 1 heure |
| **Détection d'eau** | Toute activation de capteur | Plusieurs capteurs ou eau montante | Immédiat | 30 minutes |
| **Alimentation (ASI sur batterie)** | L'ASI bascule sur batterie | Capacité batterie inférieure à 50 % | Immédiat | 15 minutes |
| **Système de refroidissement** | Défaillance d'une unité (unité redondante active) | Toutes les unités de refroidissement défaillantes | 30 minutes | 1 heure |

**Routage des alertes** :
- Alertes d'avertissement → Responsable des installations + Opérations informatiques (e-mail + tableau de bord)
- Alertes critiques → Responsable des installations + Opérations informatiques + RSSI (e-mail + SMS + tableau de bord)
- Alertes critiques hors heures → Contact d'astreinte des installations + Opérations informatiques d'astreinte

**Escalade** :
- Alerte d'avertissement non acquittée après 30 minutes → Escalade vers niveau critique
- Alerte critique non acquittée après 15 minutes → Escalade vers RSSI + Direction générale

**Test des alertes** : Les chemins d'alerte de surveillance environnementale devront être testés trimestriellement (simuler un dépassement de seuil ; vérifier la livraison des alertes à tous les destinataires configurés dans les délais cibles).

### Protection structurelle et physique

- L'extérieur du bâtiment (toit, murs, sols) devra être de construction solide adaptée aux menaces identifiées.
- La protection contre la foudre devra être appliquée aux bâtiments abritant des installations de traitement de l'information. Des protections contre les surtensions devront être installées sur les lignes d'alimentation et de télécommunications entrant dans le bâtiment.
- L'emplacement des équipements devra minimiser le risque lié aux menaces environnementales identifiées (p. ex., éviter les emplacements en sous-sol dans les zones sujettes aux inondations, éviter les emplacements adjacents à des processus dangereux).
- Des directives concernant la nourriture, les boissons et le tabagisme à proximité des installations de traitement de l'information devront être établies et communiquées.

### Réponse aux urgences

Les procédures de réponse aux urgences devront être documentées pour les incidents environnementaux et testées régulièrement. Les informations de contact d'urgence devront être affichées aux entrées des installations et dans les salles de serveurs.

#### Réponse aux urgences incendie

| Étape | Action | Responsable | Délai |
|-------|--------|-------------|-------|
| 1 | L'alarme incendie se déclenche (détection automatique ou déclencheur manuel) | Automatique / tout personnel | Immédiat |
| 2 | Évacuer la zone concernée ; rassemblement au point de regroupement désigné | Tout le personnel | Dans les 3 minutes |
| 3 | Pompiers notifiés (automatiquement via GTB ou appel manuel) | Responsable des installations / Réception | Dans les 2 minutes |
| 4 | Confirmer l'évacuation de tout le personnel (appel nominal au point de regroupement) | Responsables d'étage | Dans les 5 minutes |
| 5 | Si l'extinction à agent propre s'est déclenchée : NE PAS réentrer tant que la concentration gazeuse n'est pas vérifiée sûre | Responsable des installations | Post-extinction |
| 6 | Les pompiers libèrent les locaux ; évaluation des dommages initiée | Responsable des installations + RSSI | Post-fin d'alerte |

**Actions post-incendie** : Évaluation des dommages aux équipements dans les 24 heures ; vérification de l'intégrité des données pour les systèmes affectés ; rapport d'incident soumis dans les 48 heures ; notification à l'assurance si applicable.

#### Réponse aux urgences d'infiltration d'eau / inondation

| Étape | Action | Responsable | Délai |
|-------|--------|-------------|-------|
| 1 | Alarme d'eau déclenchée ou eau détectée visuellement | Automatique / tout personnel | Immédiat |
| 2 | Identifier la source d'eau (plomberie, infiltration externe, condensation CVC) | Responsable des installations | Dans les 15 minutes |
| 3 | Si la source est contrôlable : isoler (fermer la vanne, rediriger le flux) | Responsable des installations | Immédiat |
| 4 | Déplacer les équipements et supports au-dessus du niveau d'eau ou vers une zone sèche | Opérations informatiques + Installations | Immédiat |
| 5 | Couper l'alimentation des équipements à risque (si la sécurité le permet) | Opérations informatiques | Selon besoin |
| 6 | Déployer l'extraction d'eau (pompes, aspirateurs à eau) ; faire appel à un entrepreneur de restauration d'urgence si étendue | Responsable des installations | Dans l'heure |

#### Réponse aux urgences de défaillance du refroidissement

| Étape | Action | Responsable | Délai |
|-------|--------|-------------|-------|
| 1 | Alerte de température reçue (seuil d'avertissement dépassé) | Alerte automatique aux Opérations informatiques | Immédiat |
| 2 | Vérifier l'état du système de refroidissement ; tenter un redémarrage ou un basculement vers l'unité redondante | Responsable des installations | Dans les 15 minutes |
| 3 | Si la température approche le seuil critique (32 °C) : Commencer l'arrêt ordonné des systèmes non essentiels pour réduire la charge thermique | Opérations informatiques | Dans les 30 minutes |
| 4 | Déployer un refroidissement temporaire (unités de climatisation portables) si disponible | Responsable des installations | Dans l'heure |
| 5 | Si la température dépasse le seuil critique : Arrêt ordonné de tous les systèmes ; notification des parties prenantes | Opérations informatiques + RSSI | Selon besoin |
| 6 | Entrepreneur CVC engagé pour réparation d'urgence | Responsable des installations | Dans les 2 heures |

#### Réponse aux urgences de défaillance totale d'alimentation

| Étape | Action | Responsable | Délai |
|-------|--------|-------------|-------|
| 1 | Défaillance de l'alimentation secteur détectée ; l'ASI s'active automatiquement | Automatique | Immédiat |
| 2 | Vérifier le démarrage du groupe électrogène (Niveau 1) ou confirmer que l'ASI soutient la charge | Responsable des installations | Dans les 2 minutes |
| 3 | Si le groupe électrogène ne démarre pas : Commencer l'arrêt ordonné des systèmes non essentiels | Opérations informatiques | Dans les 10 minutes |
| 4 | Notifier le distributeur d'énergie ; demander le délai estimé de rétablissement | Responsable des installations | Dans les 15 minutes |
| 5 | Si l'autonomie de l'ASI approche sa limite et que le groupe électrogène est indisponible : Arrêt ordonné complet de tous les systèmes | Opérations informatiques | Avant épuisement de l'ASI |
| 6 | Post-rétablissement : Vérifier le redémarrage correct de tous les systèmes ; vérifier l'intégrité des données | Opérations informatiques | Post-rétablissement de l'alimentation |

Les procédures d'urgence devront être testées au moins annuellement par des exercices ou des exercices sur table.

### Formation à la sensibilisation à la sécurité physique

Tout le personnel ayant accès aux installations devra compléter la formation à la sensibilisation à la sécurité physique. La formation est dispensée annuellement, avec une réalisation par les nouveaux employés requise dans les 10 jours ouvrables suivant l'attribution de l'accès aux installations.

#### Programme de formation

| Module | Contenu | Durée | Public |
|--------|---------|-------|--------|
| **Module 1 : Fondamentaux de la sécurité des installations** | Niveaux de criticité des installations ; modèle de zones de sécurité ; utilisation des badges et responsabilités ; obligations de gestion des visiteurs ; prévention de la filature | 10 minutes | Tout le personnel |
| **Module 2 : Sensibilisation environnementale** | Sécurité incendie et voies d'évacuation ; sensibilisation à la détection d'eau ; importance du contrôle climatique ; signalement des anomalies environnementales ; numéros de contact d'urgence | 10 minutes | Tout le personnel |
| **Module 3 : Reconnaissance et signalement des incidents** | Reconnaître les événements de sécurité physique (personnes non autorisées, portes bloquées, anomalies environnementales) ; canaux de signalement et attentes ; préservation des preuves (ne pas toucher/déplacer) | 5 minutes | Tout le personnel |
| **Module 4 : Responsabilités spécifiques aux rôles** | Procédures d'accompagnement des visiteurs ; protocoles d'accès aux salles de serveurs ; fonctions de responsable d'évacuation ; sensibilisation aux systèmes de services supports | 5 minutes | Personnel avec accès aux installations de Niveau 1 ou responsabilités d'accompagnement |

**Durée totale** : 30 minutes (tous modules).

**Évaluation** : Quiz court (5 questions, taux de réussite de 80 % requis). Évaluation échouée : reprise dans les 5 jours ouvrables.

**Orientation sur les installations de Niveau 1** (supplémentaire, en présentiel) :
- Visite physique des sorties de secours, emplacements des extincteurs et points de regroupement
- Démonstration du lecteur de badge et des procédures d'accès
- Introduction aux affichages de surveillance environnementale (le cas échéant)
- Durée : 15 minutes, conduite par le Responsable des installations ou son délégué

**Objectif de réalisation de la formation** : 95 % du personnel ayant accès aux installations annuellement. Réalisation suivie via [SGA ou registre de formation]. Non-réalisation escaladée au responsable hiérarchique à 30 jours de retard ; accès aux installations suspendu à 60 jours de retard.

---

## Services supports (A.7.11)

> *Les installations de traitement de l'information devraient être protégées contre les défaillances d'alimentation électrique et autres perturbations causées par des défaillances des services supports.*

Les systèmes de services supports devront être mis en œuvre avec une capacité et une redondance proportionnelles à la criticité des installations, et testés régulièrement pour garantir leur fiabilité.

### Protection de l'alimentation — Alimentation sans interruption (ASI)

| Exigence | Niveau 1 — Installations critiques | Niveau 2 — Installations standard |
|----------|-------------------------------------|------------------------------------|
| **Configuration** | Redondance N+1 (deux unités ASI) | ASI unique |
| **Autonomie** | Minimum 30 minutes par unité (suffisant pour le démarrage et la stabilisation du groupe électrogène, ou l'arrêt ordonné) | Minimum 15 minutes (suffisant pour l'arrêt ordonné) |
| **Surveillance** | Surveillance en temps réel avec alerte automatique sur l'état de la batterie, la charge et les événements de transfert | Surveillé pendant les heures de présence du personnel |
| **Maintenance** | Remplacement de la batterie selon le calendrier du fabricant ; test de capacité annuel | Remplacement de la batterie selon le calendrier du fabricant |

- Les systèmes ASI devront protéger tous les équipements de traitement de l'information critiques, l'infrastructure réseau et les systèmes de sécurité (contrôle d'accès, CCTV, détection incendie).
- Les systèmes ASI devront être configurés pour soutenir l'arrêt ordonné des équipements qui supportent les opérations métier critiques si une panne prolongée dépasse l'autonomie de l'ASI.

#### Méthodologie de dimensionnement des ASI

La capacité de l'ASI devra être calculée selon le processus en quatre étapes suivant pour assurer une autonomie adéquate pour les équipements protégés :

**Étape 1 — Calcul de la charge** :
- Inventorier tous les équipements à protéger (serveurs, commutateurs réseau, stockage, systèmes de sécurité)
- Additionner la consommation électrique totale en watts (W) ou volt-ampères (VA) à partir des plaques signalétiques des équipements ou de la consommation électrique mesurée
- Appliquer la correction du facteur de puissance si l'on utilise des valeurs VA (facteur de puissance typique des charges informatiques : 0,9)

**Étape 2 — Facteur de croissance** :
- Appliquer une marge de croissance de 20 à 30 % au-dessus de la charge actuelle pour tenir compte des ajouts d'équipements planifiés
- Installations de Niveau 1 : Marge de croissance de 30 % (horizon de planification de 3 ans)
- Installations de Niveau 2 : Marge de croissance de 20 %

**Étape 3 — Sélection de la capacité de l'ASI** :
- Sélectionner une ou des unités ASI dont la capacité nominale dépasse le total de l'étape 2
- Niveau 1 : Redondance N+1 (deux unités ASI, chacune capable de soutenir la charge complète de manière indépendante)
- Niveau 2 : ASI unique avec capacité dépassant le total de l'étape 2
- Vérifier que l'autonomie de la batterie à la charge calculée répond aux exigences minimales (30 minutes Niveau 1, 15 minutes Niveau 2)

**Étape 4 — Vérification de l'autonomie** :
- Après installation, effectuer un test de décharge en pleine charge pour vérifier l'autonomie réelle
- Documenter l'autonomie réelle vs. l'autonomie calculée
- Si l'autonomie réelle < exigence minimale : Ajouter des modules de batterie ou réduire la charge protégée
- Revérifier annuellement lors du test de capacité (la dégradation de la batterie réduit l'autonomie au fil du temps)

**Dossier de dimensionnement ASI** : Documenté dans le registre des actifs des installations avec le calcul de la charge, le modèle ASI sélectionné, la capacité nominale, la charge mesurée, l'autonomie calculée et l'autonomie réelle testée.

### Production d'électricité de secours

| Exigence | Niveau 1 — Installations critiques | Niveau 2 — Installations standard |
|----------|-------------------------------------|------------------------------------|
| **Groupe électrogène** | Groupe électrogène de secours requis | Non requis (décision basée sur le risque) |
| **Capacité en carburant** | Minimum 48 heures à pleine charge | S/O sauf si groupe électrogène installé |
| **Délai de démarrage** | Démarrage automatique dans les 30 secondes suivant la défaillance du secteur ; commutateur de transfert automatique (CTA) | Manuel ou automatique selon besoins |
| **Gestion du carburant** | Qualité du carburant testée annuellement ; contrats de ravitaillement en place | Selon les recommandations du fabricant |

- Lorsque des groupes électrogènes sont installés, ils devront être inspectés hebdomadairement et testés en charge selon le calendrier de tests ci-dessous.

#### Sélection et gestion du carburant pour les groupes électrogènes

Le type de carburant devra être sélectionné en fonction des exigences des installations, de l'infrastructure locale et des considérations environnementales :

| Type de carburant | Avantages | Inconvénients | Usage recommandé |
|------------------|-----------|---------------|-----------------|
| **Gazole** | Haute densité énergétique ; longue durée de conservation (12–18 mois avec traitement) ; largement disponible ; démarrage à froid fiable | Nécessite un stockage de carburant sur site ; qualité du carburant se dégrade avec le temps ; réglementations environnementales pour le stockage en cuve | Installations de Niveau 1 nécessitant une autonomie étendue (48+ heures) |
| **Gaz naturel** | Pas de stockage de carburant sur site ; autonomie illimitée (fourniture par réseau) ; émissions réduites ; maintenance réduite | Dépend du réseau de gaz (peut tomber en panne lors d'une catastrophe régionale) ; densité énergétique inférieure ; nécessite un groupe électrogène adapté au gaz | Installations de Niveau 1 avec infrastructure gazière fiable et alimentation gazière distincte de l'alimentation électrique |
| **Propane (GPL)** | Longue durée de conservation (indéfinie) ; combustion propre ; fiable dans les climats froids | Nécessite un stockage en réservoir pressurisé ; densité énergétique inférieure au gazole ; logistique de ravitaillement du réservoir | Installations de Niveau 2 ; secours pour les groupes électrogènes au gaz naturel |

**Calcul de la capacité en carburant** (groupes électrogènes au gazole) :
1. Déterminer le taux de consommation de carburant du groupe électrogène à pleine charge (litres/heure, données du fabricant)
2. Multiplier par la durée requise (48 heures pour le Niveau 1)
3. Ajouter une marge de sécurité de 20 %
4. Résultat = capacité minimale de la cuve à carburant

**Exigences de gestion du carburant** (gazole) :
- Qualité du carburant testée annuellement (teneur en eau, contamination microbienne, stabilité à l'oxydation)
- Traitement du carburant (biocide, stabilisateur) appliqué selon le calendrier du fabricant
- Inspection de la cuve annuellement (corrosion interne, accumulation d'eau, intégrité structurelle)
- Contrat de ravitaillement en place avec livraison garantie dans les 24 heures suivant la demande
- Niveau minimal de carburant maintenu à 75 % de capacité (surveillance automatique si réalisable)

### Systèmes de refroidissement

| Exigence | Niveau 1 — Installations critiques | Niveau 2 — Installations standard |
|----------|-------------------------------------|------------------------------------|
| **Redondance** | Deux voies de refroidissement (N+1 minimum) | Système de refroidissement unique |
| **Surveillance** | Surveillance continue de la température avec alertes automatiques | Surveillé pendant les heures de présence du personnel |
| **Réponse aux défaillances** | Basculement automatique vers l'unité redondante ; alerte au responsable des installations | Alerte au responsable des installations ; réponse manuelle |

- La capacité de refroidissement devra être suffisante pour la charge thermique actuelle plus la croissance planifiée.
- Les systèmes de refroidissement devront être maintenus selon les calendriers d'entretien du fabricant, avec remplacement des filtres à air aux intervalles recommandés.

### Redondance des télécommunications

| Exigence | Niveau 1 — Installations critiques | Niveau 2 — Installations standard |
|----------|-------------------------------------|------------------------------------|
| **Connectivité Internet** | Double FAI avec basculement automatique | FAI unique (FAI secondaire recommandé sur la base d'une évaluation des risques) |
| **Diversité des voies** | Points d'entrée physiques distincts si réalisable | Entrée unique acceptable |
| **Surveillance** | Continue avec basculement automatique et alertes | Surveillé pendant les heures de présence du personnel |

- Le câblage d'alimentation et de télécommunications transportant des données ou soutenant des services d'information devra être protégé contre l'interception, les interférences ou les dommages.
- Les câbles d'alimentation devront être séparés des câbles de communication pour éviter les interférences.
- L'accès aux salles de câblage et aux panneaux de brassage devra être limité par un contrôle d'accès physique.

#### Procédures de basculement des télécommunications

Des procédures de basculement automatique et manuel devront être documentées et testées pour assurer la continuité de la connectivité :

**Basculement automatique** (installations de Niveau 1 avec double FAI) :

| Étape | Action | Délai cible |
|-------|--------|------------|
| 1 | Défaillance du FAI principal détectée (lien hors service, perte de paquets >5 %, latence >200 ms) | Détection dans les 30 secondes |
| 2 | Basculement automatique vers le FAI secondaire initié par l'équipement de routage | Basculement dans les 60 secondes |
| 3 | Alerte générée aux Opérations informatiques (e-mail + tableau de bord de surveillance) | Immédiat |
| 4 | Les Opérations informatiques vérifient le rétablissement du service et enquêtent sur la défaillance du FAI principal | Dans les 15 minutes |
| 5 | FAI principal rétabli → retour automatique (ou manuel si configuré) | Selon rétablissement du FAI |

**Basculement manuel** (installations de Niveau 2 ou à FAI unique avec secours) :

| Étape | Action | Responsable |
|-------|--------|-------------|
| 1 | Panne du FAI signalée ou détectée via surveillance | Opérations informatiques |
| 2 | Vérifier que la panne est côté FAI (et non une défaillance d'équipement interne) | Opérations informatiques |
| 3 | Activer la connectivité de secours (basculement 4G/5G, point d'accès mobile, ou FAI alternatif) | Opérations informatiques |
| 4 | Notifier les utilisateurs concernés de la connectivité dégradée et du délai estimé de rétablissement | Opérations informatiques |
| 5 | Surveiller le rétablissement du FAI principal ; restaurer le routage normal une fois disponible | Opérations informatiques |

**Secours FAI unique pour les installations de Niveau 2** : Lorsqu'un FAI unique est déployé, un appareil de basculement mobile 4G/5G (p. ex., Cradlepoint, Peplink, ou équivalent) devra être disponible comme secours. L'appareil de basculement devra être testé trimestriellement pour confirmer l'activation de la carte SIM et la suffisance de la bande passante pour les services critiques.

### Calendrier de tests des services supports

Tous les systèmes de résilience des services supports devront être testés à intervalles réguliers pour vérifier leur disponibilité opérationnelle :

| Système | Type de test | Fréquence | Critères de réussite | Responsable |
|---------|-------------|-----------|---------------------|-------------|
| **ASI** | Test de basculement (simuler une défaillance secteur, vérifier le transfert sur batterie) | Trimestrielle | Transfert propre dans le délai nominal ; charge soutenue pendant l'autonomie nominale | Responsable des installations |
| **ASI** | Test de capacité de la batterie (décharge complète sous charge) | Annuelle | Capacité de la batterie >= 80 % de la capacité nominale | Responsable des installations |
| **Groupe électrogène** | Test de démarrage à vide | Mensuelle | Démarrage dans les 30 secondes ; tension et fréquence stables dans les 60 secondes | Responsable des installations |
| **Groupe électrogène** | Test en charge (minimum 30 % de la puissance nominale, 30 minutes) | Semestrielle | Soutient la charge nominale ; température des gaz d'échappement dans les limites | Responsable des installations |
| **Groupe électrogène** | Test de transfert en pleine charge (de bout en bout avec CTA) | Annuelle | Transfert automatique et retour sans interruption de la charge protégée | Responsable des installations |
| **Refroidissement** | Vérification du basculement de redondance | Trimestrielle | L'unité de secours s'active ; la température reste dans les seuils | Responsable des installations |
| **Télécommunications** | Test de basculement FAI | Annuelle | Basculement automatique ou manuel dans le délai cible documenté ; services rétablis | Opérations informatiques |

Les résultats des tests devront être documentés avec : date du test, système testé, procédure de test, résultat réussite/échec, problèmes identifiés et actions correctives. Les dossiers de tests devront être conservés pendant 5 ans.

**Réponse aux échecs de test** : Tout échec de test devra déclencher une investigation immédiate, des mesures compensatoires provisoires (p. ex., restreindre l'utilisation des installations, augmenter la surveillance) et une remédiation dans les 30 jours. Les échecs répétés devront être escaladés au RSSI.

### Surveillance des services supports

- Les systèmes de services supports (alimentation, refroidissement, télécommunications) devront être surveillés en temps réel avec des alertes pour les défaillances, les dépassements de seuils et les conditions dégradées.
- Les systèmes de surveillance des services supports devraient être intégrés au [GTB] ou au [Système de surveillance environnementale] pour une visibilité centralisée.
- Les incidents de services supports devront être journalisés et rapportés conformément au processus de gestion des incidents.

---

## Niveaux de criticité des installations

Les installations devront être classées en niveaux de criticité sur la base de l'analyse d'impact sur l'activité. La classification par niveau détermine l'intensité de la surveillance, les exigences de protection environnementale et les niveaux de résilience des services supports dans l'ensemble de la présente politique.

| Attribut | Niveau 1 — Critique | Niveau 2 — Standard |
|----------|---------------------|---------------------|
| **Définition** | Centres de données, salles de serveurs principales, sites de reprise après sinistre | Bureaux d'entreprise, agences, salles de serveurs non critiques |
| **Critères de classification** | Héberge les systèmes métier de Niveau 1/2 ; traite des données CONFIDENTIELLES ; OTR < 4 heures | Héberge les systèmes de Niveau 3/4 ; traite des données INTERNES ; OTR > 4 heures |
| **Surveillance** | Surveillance 24h/24, 7j/7 (SOC ou service de surveillance des alarmes) ; ANS de réponse < 15 minutes ; détection d'intrusion requise | Surveillance heures ouvrables (8h/5j) ; réponse le prochain jour ouvrable acceptable ; détection d'intrusion selon risque |
| **Environnemental** | Extinction + détection incendie ; détection d'eau toutes zones ; température 18–27 °C +/- 2 °C ; surveillance continue | Détection incendie obligatoire (extinction si équipements > CHF 500 000) ; détection d'eau zones à haut risque ; température 18–27 °C +/- 5 °C |
| **Services — Alimentation** | ASI N+1 (deux unités, 30 min d'autonomie chacune) ; groupe électrogène de secours (carburant 48 h) ; CTA | ASI unique (minimum 15 min d'autonomie) ; groupe électrogène facultatif |
| **Services — Refroidissement** | Double voie de refroidissement (N+1) ; surveillance continue | Système de refroidissement unique ; surveillance pendant les heures de présence du personnel |
| **Services — Télécoms** | Double FAI avec basculement automatique ; entrée à voies distinctes | FAI unique ; FAI secondaire recommandé |
| **Fréquence de révision** | Vérification manuelle mensuelle de tous les systèmes | Vérification manuelle trimestrielle de tous les systèmes |

**Processus d'attribution du niveau** : Les propriétaires de systèmes, en consultation avec le Responsable des installations et le RSSI, devront déterminer le niveau approprié pour chaque installation sur la base des résultats de l'analyse d'impact sur l'activité. Les attributions de niveaux devront être révisées annuellement.

---

## Classification des incidents

Les événements de sécurité de l'infrastructure physique devront être classifiés et traités en fonction de leur gravité :

| Gravité | Exemples | Réponse requise |
|---------|----------|-----------------|
| **Critique** | Accès non autorisé aux zones restreintes ; violation physique ; vol d'équipements ; incendie ou inondation majeur ; défaillance totale de l'alimentation ou du refroidissement | Réponse immédiate ; activer le processus de gestion des incidents ; notifier le RSSI et la Direction générale dans l'heure |
| **Élevée** | Tentatives d'accès répétées échouées ; filature détectée ; badges d'accès perdus ; alertes environnementales approchant les seuils critiques ; défaillance partielle des services supports | Investigation et réponse le même jour ; notifier le RSSI dans les 4 heures |
| **Moyenne** | Alertes de porte maintenue ouverte ; fausses alarmes fréquentes ; dépassements environnementaux mineurs (dans les seuils d'alerte mais pas critiques) ; échec unique de test de services supports | Documenté et investigué dans les 5 jours ouvrables ; analyse des tendances |
| **Faible** | Tentative d'accès unique échouée ; violations mineures de la politique ; notifications de maintenance planifiée | Consigné pour analyse des tendances ; révisé mensuellement |

Les incidents de sécurité physique devront être signalés et gérés via le processus de gestion des incidents de l'organisation (A.5.24–28).

---

## Rôles et responsabilités

| Rôle | Responsabilité |
|------|----------------|
| **RSSI** | Responsabilité globale de la politique de sécurité de l'infrastructure physique ; acceptation des risques pour les exceptions ; approbation du budget ; rapports à la direction sur la posture de sécurité physique |
| **Responsable des installations** | Opérations quotidiennes de l'infrastructure physique ; maintenance des systèmes environnementaux et de services supports ; gestion des prestataires pour les services du bâtiment ; exécution du programme de tests des services supports |
| **Responsable des opérations de sécurité** | Mise en œuvre de la surveillance de la sécurité physique ; gestion du système de contrôle d'accès ; opérations CCTV ; gestion de la détection d'intrusion ; coordination des incidents de sécurité physique |
| **Opérations informatiques** | Intégration physique-logique de la sécurité (SIEM) ; infrastructure réseau soutenant les systèmes de sécurité ; gestion de la redondance des télécommunications |
| **Propriétaires de systèmes** | Définir les exigences de sécurité physique pour les systèmes détenus ; participer à la classification des niveaux des installations ; signaler les incidents de sécurité physique |
| **Audit interne** | Vérification annuelle de la conformité à la sécurité physique ; révision des preuves ; test des contrôles |
| **Tous les employés** | Signaler les incidents de sécurité physique et les activités suspectes ; respecter les procédures de contrôle d'accès et de gestion des visiteurs ; suivre les procédures d'urgence environnementale |

---

## Preuves pour cette politique

| # | Preuve | Responsable | Fréquence |
|---|--------|-------------|-----------|
| 1 | **Journaux du système de contrôle d'accès physique** (événements d'accès accordé/refusé avec identification individuelle) | Responsable des opérations de sécurité | *Journalisation continue ; révisée mensuellement ; conservée 12 mois* |
| 2 | **Dossiers opérationnels du système CCTV** (rapports de disponibilité, vérifications de la santé des caméras, vérification des enregistrements) | Responsable des opérations de sécurité | *Vérifications hebdomadaires ; conservés 12 mois* |
| 3 | **Dossiers de test de détection d'intrusion** (résultats des tests trimestriels, vérification de la réponse aux alarmes) | Responsable des opérations de sécurité | *Trimestrielle ; conservés 3 ans* |
| 4 | **Journaux de gestion des visiteurs** (registre des visiteurs avec nom, organisation, hôte, conformité à l'accompagnement) | Responsable des opérations de sécurité | *Continu ; conservés 12 mois* |
| 5 | **Dossiers de révision des droits d'accès** (résultats des révisions semestrielles, actions de révocation) | Responsable des opérations de sécurité | *Semestrielle ; conservés 3 ans* |
| 6 | **Dossiers d'inspection et de test des systèmes incendie** (certificats des systèmes de détection et d'extinction, tests des portes coupe-feu) | Responsable des installations | *Semestriel/annuel selon niveau ; conservés 5 ans* |
| 7 | **Données de surveillance environnementale** (journaux de température et d'humidité ; dossiers de dépassement de seuils) | Responsable des installations | *Journalisation continue ; conservée 12 mois* |
| 8 | **Dossiers de maintenance et de test du système de détection d'eau** | Responsable des installations | *Vérification trimestrielle ; conservés 3 ans* |
| 9 | **Dossiers de test ASI** (tests de basculement trimestriels, tests de capacité annuels) | Responsable des installations | *Selon calendrier de tests ; conservés 5 ans* |
| 10 | **Dossiers de test du groupe électrogène** (tests de démarrage mensuels, tests en charge semestriels, tests de transfert annuels) | Responsable des installations | *Selon calendrier de tests ; conservés 5 ans* |
| 11 | **Dossiers de vérification de la redondance du refroidissement** (tests de basculement trimestriels) | Responsable des installations | *Trimestrielle ; conservés 3 ans* |
| 12 | **Dossiers de test de basculement des télécommunications** | Opérations informatiques | *Annuelle ; conservés 3 ans* |
| 13 | **Évaluation des risques liés aux menaces environnementales** (évaluation des risques spécifique aux installations avec historique des révisions) | Responsable des installations / RSSI | *Révision annuelle ; conservée 5 ans* |
| 14 | **Dossiers des exercices d'urgence** (date de l'exercice, scénario, participants, constatations, actions) | Responsable des installations | *Annuelle ; conservés 3 ans* |
| 15 | **Registre des exceptions** (dérogations approuvées à la politique avec acceptation des risques et mesures compensatoires) | RSSI | *Par événement ; révisé trimestriellement ; conservé actif + 2 ans* |

---

# Conformité à la politique

## Mesure de la conformité

L'équipe de management de la sécurité de l'information vérifiera la conformité à la présente politique par diverses méthodes, notamment les rapports des systèmes de sécurité physique, les dossiers de tests des services supports, les données de surveillance environnementale, les inspections des installations, les audits internes et externes, et les retours au propriétaire de la politique.

La conformité devra être évaluée selon les indicateurs pondérés suivants :

| Indicateur | Pondération | Source de mesure |
|-----------|-------------|-----------------|
| Disponibilité du système de contrôle d'accès et exhaustivité des journaux | 20 % | Journaux [Système de contrôle d'accès] |
| Conformité des paramètres environnementaux (température/humidité dans les seuils) | 20 % | [Système de surveillance environnementale] / [GTB] |
| Taux de succès des tests de résilience des services supports (tous les tests réussis dans les délais) | 15 % | Dossiers de tests |
| Statut opérationnel des systèmes de détection incendie et d'eau | 15 % | Dossiers d'inspection |
| Respect des délais de réponse aux incidents de sécurité physique | 15 % | Dossiers d'incidents |
| Conformité à la gestion des visiteurs (enregistrement, accompagnement, restitution des badges) | 10 % | Journaux des visiteurs |
| Réalisation de la formation à la sensibilisation à la sécurité physique | 5 % | Dossiers de formation |

| Score | Évaluation | Action |
|-------|-----------|--------|
| > 90 % | Excellent | Maintenir les contrôles actuels |
| 75–89 % | Bon | Traiter les lacunes lors du prochain cycle de révision |
| 60–74 % | Acceptable | Élaborer un plan de remédiation dans les 30 jours |
| < 60 % | Non conforme | Remédiation immédiate requise ; escalade au RSSI |

## Exceptions

Toute exception à la présente politique devra être approuvée et enregistrée à l'avance par le Responsable de la sécurité de l'information, avec une évaluation documentée des risques, des mesures compensatoires et une date de révision définie (maximum 6 mois, renouvelable). Les scénarios d'exception valides incluent l'infaisabilité technique, un coût disproportionné par rapport au risque et une dérogation temporaire lors de transitions d'installations. Les exceptions devront être rapportées à l'équipe de revue de direction.

## Non-conformité

Un employé reconnu coupable de violation de la présente politique peut faire l'objet de mesures disciplinaires pouvant aller jusqu'au licenciement.

## Amélioration continue

La présente politique est révisée et mise à jour dans le cadre du processus d'amélioration continue. Les révisions devront prendre en compte les changements dans les opérations des installations, les profils de risque environnemental, les exigences réglementaires, les avancées technologiques en matière de systèmes de sécurité physique, les enseignements tirés des incidents et des échecs de tests des services supports, et les constatations d'audit.

---

# Domaines de la norme ISO 27001 couverts

Politique de sécurité de l'infrastructure physique — Correspondance avec les contrôles ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership et engagement | 5.1 Politiques de sécurité de l'information |
| Clause 5.2 Politique | 5.4 Responsabilités de la direction |
| Clause 6.2 Objectifs de sécurité de l'information | 5.36 Conformité aux politiques, règles et normes |
| Clause 7.3 Sensibilisation | 6.3 Sensibilisation, formation et éducation à la sécurité de l'information |
| | 6.4 Processus disciplinaire |
| | **7.4 Surveillance de la sécurité physique** |
| | **7.5 Protection contre les menaces physiques et environnementales** |
| | 7.8 Emplacement et protection des équipements |
| | **7.11 Services supports** |
| | 7.12 Sécurité du câblage |

**Cadre réglementaire et juridique** :

| Cadre | Pertinence |
|-------|-----------|
| nLPD suisse (nFADP/revDSG) | Art. 8 — Mesures techniques et organisationnelles pour la sécurité physique des installations de traitement des données |
| OPDo suisse (Ordonnance sur la protection des données) | Art. 1–3 — Exigences minimales en matière de sécurité des données, y compris les mesures physiques |
| RGPD UE (si applicable) | Art. 32 — Sécurité du traitement, y compris les mesures physiques |
| ISO/IEC 27001:2022 | Contrôles Annexe A 7.4 (Surveillance de la sécurité physique), 7.5 (Protection environnementale), 7.11 (Services supports) |
| ISO/IEC 27002:2022 | Sections 7.4, 7.5, 7.11 — Lignes directrices de mise en œuvre |
| ASHRAE | Directives thermiques pour les environnements de traitement des données (température/humidité) |
| NFPA 2001 / ISO 14520 | Systèmes d'extinction à agent propre pour les espaces occupés |
| NFPA 110 | Exigences de test des systèmes d'alimentation de secours |
| NIST SP 800-53 Rév. 5 | PE-1 à PE-20 — Famille de protection physique et environnementale |
| CIS Controls v8 | Contrôle 1 (Inventaire), Contrôle 12 (Infrastructure réseau — câblage physique) |
| **Conditionnel** : FINMA Circulaire 2023/1 | Institution financière suisse réglementée — exigences renforcées de sécurité physique |
| **Conditionnel** : DORA (UE) 2022/2554 | Entité de services financiers UE — résilience opérationnelle pour l'infrastructure TIC |
| **Conditionnel** : NIS2 (UE) 2022/2555 | Entité essentielle/importante dans l'UE — sécurité physique pour l'infrastructure critique |

---

<!-- QA_VERIFIED: 2026-03-29 -->
