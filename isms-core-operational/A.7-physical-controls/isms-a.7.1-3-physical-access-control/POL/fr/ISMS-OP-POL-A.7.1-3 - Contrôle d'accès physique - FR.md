<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.7.1-3-FR:operational:OP-POL:a.7.1-3 -->
**ISMS-OP-POL-A.7.1-3 — Contrôle d'accès physique**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Contrôle d'accès physique |
| **Type de document** | Politique opérationnelle |
| **Identifiant du document** | ISMS-OP-POL-A.7.1-3 |
| **Créateur du document** | Responsable de la Sécurité des Systèmes d'Information (RSSI) |
| **Propriétaire du document** | Directeur général (DG) |
| **Approuvé par** | Direction générale |
| **Date de création** | [Date] |
| **Version** | 0.1 |
| **Date de version** | [À déterminer] |
| **Classification** | Interne |
| **Statut** | Brouillon |

**Historique des versions** :

| Version | Date | Auteur | Modifications |
|---------|------|--------|---------------|
| 0.1 | [Date] | RSSI | Politique opérationnelle initiale pour ISO 27001:2022 |

**Cycle de révision** : Annuel
**Prochaine date de révision** : [Date d'entrée en vigueur + 12 mois]

**Approuvé par** : [RSSI / Direction générale]

**Documents connexes** :

- ISO/IEC 27001:2022 Contrôles A.7.1, A.7.2, A.7.3
- ISO/IEC 27002:2022 Sections 7.1, 7.2, 7.3 — Lignes directrices de mise en œuvre
- ISMS-OP-POL-A.7.4-5-11 — Sécurité de l'infrastructure physique
- ISMS-OP-POL-A.7.6-7-14 — Traitement des informations et des supports
- ISMS-OP-POL-A.7.8-9 — Sécurité de l'emplacement des équipements
- ISMS-OP-POL-A.5.15-16-18 — Gestion des identités et des accès
- ISMS-OP-POL-A.5.24-28 — Gestion des incidents

**Contrôles Annexe A connexes** :

| Contrôle | Relation avec le contrôle d'accès physique |
|----------|-------------------------------------------|
| A.7.4 Surveillance de la sécurité physique | Surveillance des périmètres et des points d'entrée définis dans la présente politique |
| A.7.5 Protection contre les menaces physiques et environnementales | Protection environnementale pour les zones sécurisées par la présente politique |
| A.7.6 Travail dans des zones sécurisées | Exigences comportementales au sein des zones définies ici |
| A.7.8 Emplacement et protection des équipements | Placement des équipements dans les zones sécurisées |
| A.5.15-16-18 Gestion des identités et des accès | Intégration de l'accès logique avec les contrôles d'accès physique |
| A.5.24-28 Cycle de vie de la gestion des incidents | Chemin d'escalade pour les événements de sécurité physique |
| A.6.7 Télétravail | Le télétravail réduit l'empreinte d'accès sur site |
| A.8.12 Prévention de la fuite de données | Les contrôles physiques complètent les mesures DLP techniques |

---

# Politique de contrôle d'accès physique

## Objectif

La présente politique établit les exigences de l'organisation en matière de contrôle d'accès physique, couvrant les périmètres de sécurité, les contrôles d'entrée physique, et la sécurisation des bureaux, salles et installations. Elle définit les zones de sécurité, les exigences d'authentification, les procédures de gestion des visiteurs et les mesures de protection des installations nécessaires pour prévenir tout accès physique non autorisé aux locaux organisationnels et aux actifs informationnels.

La présente politique soutient la nLPD suisse (nFADP/revDSG) art. 8 en mettant en œuvre des mesures techniques et organisationnelles appropriées aux risques pour protéger les données personnelles (y compris les données personnelles sensibles) stockées ou traitées dans les locaux organisationnels. Lorsque l'organisation traite des données de personnes situées dans l'UE/EEE, les exigences de l'art. 32 du RGPD concernant la sécurité physique du traitement s'appliquent également.

Les contrôles A.7.1 (Périmètres de sécurité physique), A.7.2 (Entrée physique) et A.7.3 (Sécurisation des bureaux, salles et installations) sont combinés car ils forment un cadre intégré de sécurité physique : les périmètres définissent les limites, les contrôles d'entrée protègent le franchissement de ces limites, et les mesures de sécurité internes protègent des zones spécifiques à l'intérieur de celles-ci.

**Organisations entièrement dans le cloud** : Les organisations opérant entièrement depuis une infrastructure cloud sans salle de serveurs ni centre de données en propre ou loué devront néanmoins appliquer la présente politique aux locaux de bureaux, aux espaces de coworking et à tout lieu où des informations organisationnelles sont physiquement consultées ou stockées. Les exigences relatives aux salles de serveurs et aux centres de données ne s'appliquent que lorsque l'organisation contrôle de telles installations ; pour les centres de données tiers et la colocation, les exigences d'assurance fournisseur s'appliquent.

## Champ d'application

La présente politique s'applique à :

- Tous les locaux en propriété, loués ou exploités, incluant les bureaux, centres de données et sites distants.
- Toutes les zones : réception publique, espace de bureaux général, salles de serveurs, centres de données, stockage sécurisé et salles d'archives.
- Tous les points d'entrée : entrées principales, portes secondaires, sorties de secours, zones de chargement et de livraison, fenêtres et points d'accès aux toits.
- Tout le personnel : employés, sous-traitants, visiteurs, personnel de maintenance et personnel de livraison.

Hors champ d'application :

- Surveillance et systèmes de sécurité physique (couverts par A.7.4).
- Protection environnementale — incendie, eau, température (couverts par A.7.5).
- Emplacement des équipements et sécurité hors des locaux (couverts par A.7.8-9).
- Services supports (couverts par A.7.11).

## Principe

La sécurité physique devrait être conçue selon une approche de défense en profondeur avec des zones de sécurité concentriques, où chaque zone successive requiert une authentification et une autorisation plus fortes. L'accès devra être accordé selon le principe du moindre privilège — le personnel ne reçoit l'accès qu'aux zones nécessaires à l'exercice de son rôle. Tout accès physique devra être consigné, régulièrement révisé et rapidement révoqué lorsqu'il n'est plus nécessaire. L'organisation favorise une culture consciente de la sécurité où tout le personnel est attendu à interpeller les personnes non reconnues dans les zones sécurisées et à signaler les préoccupations de sécurité physique sans crainte de représailles.

---

## Périmètres de sécurité physique (A.7.1)

**ISO/IEC 27001:2022 Annexe A.7.1 — Périmètres de sécurité physique** :

> *Des périmètres de sécurité devraient être définis et utilisés pour protéger les zones contenant des informations et d'autres actifs associés.*

### Modèle de zones de sécurité

L'organisation devrait définir et documenter les zones de sécurité selon la classification suivante :

| Zone | Description | Exemples de zones | Population d'accès |
|------|-------------|-------------------|-------------------|
| **Zone Publique** | Accessible au grand public | Hall de réception, salles d'attente visiteurs, extérieurs | Toute personne |
| **Zone Contrôlée** | Personnel autorisé uniquement | Espaces de bureaux généraux, salles de réunion, salles de pause | Employés, visiteurs accompagnés |
| **Zone Restreinte** | Accès limité, base du besoin d'en connaître | Bureaux de la direction, RH, finance, juridique, stockage des documents | Personnel nommément désigné avec besoin métier |
| **Zone Haute Sécurité** | Accès strictement contrôlé | Salles de serveurs, centres de données, opérations de sécurité, coffres-forts | Personnel nommément désigné avec autorisation explicite |

Chaque zone devra être documentée sur des plans d'étage avec des limites clairement marquées, des points d'entrée et les mécanismes de contrôle d'accès utilisés.

### Exigences de construction du périmètre

**Périmètre du bâtiment (externe)** :

- Les murs extérieurs, toits et planchers devront être de construction solide adaptée au risque.
- Les portes extérieures devront être sécurisées avec des serrures et des mécanismes de contrôle d'accès (p. ex., lecteurs de badges [Système de contrôle d'accès], serrures électroniques).
- Les fenêtres devront être sécurisées, particulièrement au rez-de-chaussée ; les fenêtres du rez-de-chaussée à proximité des Zones Restreintes ou Haute Sécurité devront être renforcées ou équipées de vitrage de sécurité.
- Les sorties de secours devront être équipées d'alarmes et surveillées ; les sorties de secours ne devront pas être utilisables pour une entrée de routine depuis l'extérieur.
- Toutes les portes coupe-feu sur un périmètre de sécurité devront être équipées d'alarmes, surveillées et testées conjointement avec les murs pour établir le niveau de résistance requis. Les portes coupe-feu devront fonctionner conformément aux réglementations suisses de sécurité incendie en mode sûr défaut.
- Les points de ventilation et les ouvertures de service ne devront pas constituer une voie de contournement vers les zones sécurisées.
- Des systèmes de détection d'intrusion appropriés devront être installés conformément aux normes nationales ou internationales applicables (p. ex., EN 50131).

**Périmètres internes (entre zones)** :

- Les cloisons entre les Zones Contrôlées, Restreintes et Haute Sécurité devront s'étendre du plancher au plafond, y compris au-dessus des faux plafonds et en dessous des faux planchers.
- Les points d'accès entre les zones devront disposer de contrôles d'accès appropriés correspondant à la zone de destination.
- Les murs des Zones Restreintes et Haute Sécurité devront empêcher l'espionnage visuel et sonore lorsque l'évaluation des risques l'exige.

**Inspections des périmètres** :

- Les inspections du périmètre du bâtiment devront être effectuées au minimum annuellement.
- Les périmètres des Zones Restreintes et Haute Sécurité devront être inspectés au moins trimestriellement et après toute modification du bâtiment ou incident de sécurité.
- Les constatations d'inspection devront être documentées et toute lacune remédiée dans les 30 jours (ou immédiatement si elle présente un risque imminent).

### Colocation et installations partagées

Lorsque l'organisation opère dans des centres de données en colocation ou des immeubles de bureaux partagés :

- Les zones contrôlées par [l'Organisation] (cages, salles, étages) devront être clairement délimitées et documentées.
- Des exigences contractuelles en matière de sécurité physique, de journalisation des accès et de notification des incidents devront être en place avec le prestataire de l'installation.
- Des preuves d'assurance fournisseur (certificat ISO 27001, rapport SOC 2 Type II ou attestation équivalente) devront être obtenues et révisées annuellement.
- Lorsque la sécurité physique du prestataire de colocation ne répond pas aux exigences de la présente politique, une acceptation documentée des risques avec des mesures compensatoires devra être enregistrée.
- L'infrastructure partagée (ascenseurs, couloirs, parties communes) ne devra pas fournir un accès incontrôlé aux zones sécurisées de l'organisation.
- La gestion des clés et des cartes pour l'accès au bâtiment dans les installations partagées devra être coordonnée avec la gestion du bâtiment, [l'Organisation] maintenant un registre indépendant de toutes les accréditations émises.

**Séparation des installations de traitement de l'information** : Les installations de traitement de l'information gérées par l'organisation devront être physiquement séparées de celles gérées par des parties extérieures partageant le même bâtiment ou étage.

---

## Contrôles d'entrée physique (A.7.2)

**ISO/IEC 27001:2022 Annexe A.7.2 — Entrée physique** :

> *Les zones sécurisées devraient être protégées par des contrôles d'entrée appropriés pour garantir que seul le personnel autorisé est admis.*

### Sécurité des points d'entrée

Tous les points d'entrée vers les zones sécurisées devront être protégés :

**Entrées principales** :

- Un poste de réception avec personnel ou un contrôle équivalent (interphone, entrée vidéo) devra fonctionner pendant les heures ouvrables.
- Un système de contrôle d'accès ([Système de contrôle d'accès] — p. ex., Verkada, Genetec, Honeywell, Lenel, ASSA ABLOY/Salto, ou lecteurs de badges RFID équivalents, accréditations mobiles, ou lecteurs biométriques) devra authentifier tout le personnel entrant au-delà de la Zone Publique. Lorsque des systèmes sont en cours de sélection, l'approche provisoire et la date cible de déploiement devront être documentées.
- Des mesures anti-filature devront être mises en œuvre aux points d'entrée des Zones Restreintes et Haute Sécurité :

| Mesure | Efficacité | Applicabilité par zone |
|--------|-----------|----------------------|
| **Sas de sécurité** (systèmes à deux portes en interverrouillage) | Élevée — prévention physique | Zones Haute Sécurité (serveurs, centres de données) |
| **Tourniquets avec détecteurs de hauteur** | Moyenne-élevée — barrière physique + détection | Zones Restreintes |
| **CCTV renforcée par IA** avec détection de filature | Moyenne — détection + alerte | Toutes les zones sécurisées |
| **Signalisation de sensibilisation à la sécurité** + culture d'interpellation | Faible-moyenne — comportementale | Minimum pour toutes les zones |

Mise en œuvre actuelle : [Préciser, p. ex., « Tourniquets à l'entrée principale ; sas de sécurité au centre de données ; CCTV + sensibilisation aux entrées secondaires » ou « Sensibilisation + CCTV uniquement ; barrières physiques planifiées pour [trimestre] »].
- L'accès hors heures ouvrables devra nécessiter une authentification supplémentaire et devra générer des alertes au personnel de sécurité ou à l'équipe d'astreinte.

### Accès d'urgence

**Accès hors heures ouvrables** (en dehors des heures de bureau — [préciser, p. ex., 06h00–20h00 lun.–ven.]) :
- Nécessite une authentification par badge + code PIN (Zone Contrôlée minimum).
- Génère une alerte à l'astreinte des installations / surveillance de sécurité.
- Si aucune réponse à l'interpellation dans les 15 minutes, escalade selon la procédure d'incident.

**Confinement d'urgence** :
- Autorité pour initier le confinement : PDG, COO, Responsable des installations, RSSI, ou sécurité sur site.
- Déclencheurs du confinement : Menace active sur site, incident à proximité affectant la sécurité, catastrophe naturelle.
- Procédure de confinement : Toutes les portes extérieures verrouillées (accès par badge désactivé) ; le personnel reste en place ; les services d'urgence sont notifiés ; fin d'alerte communiquée via [système de sonorisation / SMS / e-mail].

**Évacuation incendie et sécurité** :
- Les portes coupe-feu se déverrouillent automatiquement lors du déclenchement de l'alarme incendie (mode sûr défaut conformément au code suisse d'incendie).
- Le système de contrôle d'accès se rétablit après la remise à zéro de l'alarme et l'inspection de sécurité des installations.
- Point de rassemblement d'évacuation en dehors du périmètre sécurisé ; réentrée via un processus contrôlé après fin d'alerte.

**Entrées secondaires et de secours** :

- Les portes latérales et entrées secondaires devront disposer de contrôles d'accès équivalents à l'entrée principale pour la zone correspondante.
- Les portes coupe-feu et sorties de secours devront être équipées d'alarmes et surveillées. Les sorties de secours devront s'ouvrir vers l'extérieur (conformément aux réglementations incendie) mais ne devront pas être ouvrables de l'extérieur sans autorisation.
- Les portes d'accès aux toits et trappes de service devront être verrouillées et équipées d'alarmes.

### Authentification par zone

| Zone de sécurité | Authentification minimale | Exigences supplémentaires |
|-----------------|--------------------------|--------------------------|
| **Zone Contrôlée** | Accès par badge/carte (RFID, accréditation mobile) | — |
| **Zone Restreinte** | Badge + code PIN | Accès consigné avec identité et horodatage |
| **Zone Haute Sécurité** | Badge + code PIN + biométrie, OU contrôle à deux personnes | Accès consigné ; CCTV à l'entrée ; accès hors heures génère une alerte |

**Exigences du système de contrôle d'accès** :

- Le système de contrôle d'accès devra consigner tous les événements d'accès (accordés et refusés) avec l'identité, l'horodatage et le point d'entrée.
- Les droits d'accès devront être basés sur les rôles et accordés selon le principe du besoin d'en connaître / besoin d'accès.
- Les droits d'accès devront être révisés trimestriellement (au minimum) ; l'accès aux Zones Restreintes et Haute Sécurité devra être reconfirmé par le responsable habilité.

**Processus de révision trimestrielle des accès** :

1. **Génération du rapport d'accès** : Le Responsable des installations génère un rapport des droits d'accès depuis [Système de contrôle d'accès] indiquant tout le personnel avec accès aux zones, regroupé par zone et département (échéance : 1er jour ouvrable du mois de révision).
2. **Attestation du responsable** : Les responsables hiérarchiques reçoivent la liste d'accès de leur équipe ; confirment que l'accès aux zones de chaque personne est toujours requis ; identifient les accès à révoquer (échéance : 14 jours après la distribution du rapport).
3. **Exécution de la révocation** : Le Responsable des installations révoque les accès inutiles dans les 5 jours ouvrables suivant l'attestation du responsable.
4. **Piste d'audit** : Les dossiers d'attestation (confirmations par e-mail, formulaires signés, ou enregistrements de flux de travail [Outil GRC]) sont conservés pendant 3 ans.

**Gestion des non-réponses** : Les responsables qui ne répondent pas dans les 14 jours reçoivent une escalade au responsable de département. L'accès des utilisateurs non attestés dans les Zones Restreintes/Haute Sécurité est suspendu dans l'attente de l'attestation.

- L'accès physique des employés résiliés devra être révoqué le jour même de la résiliation de l'emploi, en coordination avec les RH.
- Les badges perdus, volés ou endommagés devront être signalés immédiatement et désactivés selon le calendrier suivant :

| Type de badge | Délai de désactivation | Actions supplémentaires |
|---------------|----------------------|------------------------|
| **Badge Zone Haute Sécurité** | **Immédiat** (dans les 30 minutes suivant le signalement) | Notification au RSSI ; révision des journaux d'accès des 72 heures précédentes ; réémission avec nouveau numéro d'accréditation |
| **Badge Zone Restreinte** | Dans les 2 heures | Révision des journaux d'accès en cas de circonstances suspectes |
| **Badge Zone Contrôlée** | Dans les 4 heures | Procédure de remplacement standard |

**Badge perdu hors heures ouvrables** : Contact d'astreinte des installations notifié immédiatement pour les badges des Zones Restreintes/Haute Sécurité ; désactivation exécutée à distance.

- Le partage et le prêt de badges sont interdits.
- Les cartes d'accès temporaires devront être limitées dans le temps et expirer automatiquement.

### Accès des employés

- L'accès des employés devra être basé sur le principe du moindre privilège, n'accordant l'accès qu'aux zones requises pour le rôle de l'employé.
- Les jetons de contrôle d'accès (badges, cartes, accréditations mobiles) devront être émis à chaque employé et devront identifier l'individu. Les badges devront être portés visiblement à tout moment dans les locaux (cordon, clip ou porte-badge). Les badges dissimulés ou couverts pourront être interpellés par le personnel de sécurité.

**Exigences relatives aux badges** :
- Les badges des employés devront inclure : photo, nom, identifiant employé, indicateur d'accès aux zones (code couleur ou texte).
- Les badges des visiteurs devront être clairement distinguables des badges des employés (couleur distincte, marquage « VISITEUR », sans accès aux zones encodé).
- Les badges des sous-traitants devront être distinguables et inclure la date d'expiration.
- Les badges temporaires (remplacement d'un badge permanent perdu) devront être marqués « TEMPORAIRE » et expirer automatiquement après 7 jours.
- Les jetons de contrôle d'accès ne devront pas être partagés, transférés ou prêtés à d'autres personnes.
- L'accès devra être révoqué immédiatement à la résiliation de l'emploi ; tous les jetons d'accès physique devront être désactivés et restitués. Les RH devront notifier les Installations de toutes les résiliations au plus tard le dernier jour de travail.
- Les changements de rôle devront être évalués quant à leurs implications d'accès physique ; l'accès aux zones qui ne sont plus requises pour le nouveau rôle devra être révoqué dans les 5 jours ouvrables.

**Conservation des journaux d'accès** : Les journaux du système de contrôle d'accès physique devront être conservés pendant au moins 12 mois (ou plus longtemps si requis par la réglementation ou le contrat applicable), protégés contre toute modification non autorisée, et disponibles dans les 2 jours ouvrables à des fins d'audit et de réponse aux incidents.

### Gestion des visiteurs

**Enregistrement des visiteurs** :

- Tous les visiteurs devront s'enregistrer à la réception avant de s'avancer au-delà de la Zone Publique. L'enregistrement devra être consigné dans [Système de gestion des visiteurs] (ou registre papier des visiteurs) et inclure : nom du visiteur, entreprise/organisation, hôte (employé visité), date et heure d'arrivée, et objet de la visite.
- Les visiteurs devront présenter une pièce d'identité photographique valide.
- Les badges des visiteurs devront être clairement distinguables des badges des employés (couleur distincte, marqués « VISITEUR », sans accès aux zones encodé).
- Les visiteurs devront restituer les badges lors de leur départ et signer leur sortie. Les badges non restitués devront être désactivés avant la fin de la journée ouvrée.

**Accompagnement et supervision** :

- Les visiteurs dans les Zones Contrôlées peuvent se déplacer sans accompagnement uniquement si l'hôte a confirmé la visite et que le badge visiteur restreint l'accès à d'autres zones.
- Les visiteurs dans les Zones Restreintes devront être accompagnés à tout moment par un employé autorisé.
- Les visiteurs dans les Zones Haute Sécurité devront être accompagnés à tout moment par un employé autorisé disposant d'un accès explicite à la zone, et la visite devra être préapprouvée par le propriétaire de la zone.
- L'accès des visiteurs aux Zones Haute Sécurité devra être préautorisé par écrit (e-mail ou approbation du [Système de gestion des visiteurs]) avant l'arrivée.

**Conservation des journaux de visiteurs** :

- Les journaux de visiteurs devront être conservés pendant un minimum de 12 mois et protégés contre toute modification non autorisée.
- Les journaux devront être disponibles dans les 2 jours ouvrables pour un audit ou une investigation d'incident.

**Accès des sous-traitants et du personnel de maintenance** :

- Les sous-traitants et le personnel de maintenance devront être préautorisés avant l'arrivée, avec la portée des travaux et les zones d'accès documentées.
- L'accès des sous-traitants devra être limité dans le temps et consigné.
- Les sous-traitants accédant aux Zones Restreintes ou Haute Sécurité devront être accompagnés et leurs travaux supervisés lorsque des systèmes ou données sensibles sont accessibles.
- La maintenance externe sur les systèmes de sécurité (alarmes, contrôle d'accès, CCTV) devra être effectuée sous la supervision directe d'un employé autorisé.

### Zones de livraison et de chargement

- L'accès aux zones de livraison et de chargement depuis l'extérieur du bâtiment devra être limité au personnel de livraison identifié et autorisé.
- Les zones de livraison et de chargement devront être conçues (ou gérées opérationnellement) de façon à ce que le personnel de livraison ne puisse pas accéder aux autres parties du bâtiment.
- Les portes extérieures d'une zone de livraison et de chargement devront être sécurisées lorsque les portes intérieures vers les zones opérationnelles sont ouvertes ; les deux ne devront pas être ouvertes simultanément si cela peut être évité.
- Les matériaux entrants devront être inspectés pour déceler tout signe de falsification avant d'être déplacés depuis la zone de livraison.
- Les matériaux entrants devront être enregistrés conformément aux procédures de gestion des actifs lors de leur entrée sur le site.
- Les expéditions entrantes et sortantes devront être physiquement séparées dans la mesure du possible.
- Les matériaux entrants devront être inspectés pour détecter la présence de substances dangereuses lorsque l'évaluation des risques le justifie (selon le contexte : risques chimiques, biologiques ou explosifs).

---

## Sécurisation des bureaux, salles et installations (A.7.3)

**ISO/IEC 27001:2022 Annexe A.7.3 — Sécurisation des bureaux, salles et installations** :

> *La sécurité physique des bureaux, salles et installations devrait être conçue et mise en œuvre.*

### Sécurité générale des bureaux

- Les bureaux devront être verrouillés lorsqu'ils sont inoccupés en dehors des heures ouvrables.
- La politique de bureau propre devra être appliquée — les documents sensibles sont sécurisés dans un rangement verrouillé lorsqu'ils ne sont pas activement utilisés.
- Les écrans devront être positionnés pour prévenir le regard par-dessus l'épaule par les visiteurs ou les passants.
- Des installations de rangement (armoires, coffres-forts, tiroirs verrouillables) devront être fournies pour sécuriser les documents classifiés et les supports portables.
- Les installations critiques devraient être situées de manière à éviter l'accès du public et ne devraient donner aucune indication évidente de leur objet, sans signalétique extérieure identifiant la présence d'activités de traitement de l'information.
- Les installations devraient être configurées pour empêcher que les informations ou activités confidentielles soient visibles ou audibles depuis l'extérieur.

### Zones sensibles

Les zones traitant des informations Confidentielles ou Restreintes (p. ex., RH, finance, juridique, bureaux de la direction) devront disposer de :

- Contrôles d'accès appropriés à la classification de la zone (Zone Restreinte minimum).
- Journaux d'accès maintenus et révisés.
- Fenêtres donnant sur les zones sensibles givrées, couvertes ou équipées d'un film de confidentialité pour empêcher l'observation visuelle.
- Appareils d'enregistrement (caméras, téléphones avec caméras) restreints ou interdits sauf autorisation explicite.

### Salles de serveurs et centres de données

**Pour les salles de serveurs et centres de données contrôlés par [l'Organisation]** :

**Contrôle d'accès** :

- L'accès devra être limité au personnel informatique autorisé uniquement, avec des listes d'accès nominatives maintenues.
- L'authentification multifacteur devra être requise (badge + code PIN + biométrie, ou contrôle à deux personnes).
- Tout accès devra être consigné avec identité et horodatage.
- Les visiteurs et sous-traitants dans les salles de serveurs devront être accompagnés à tout moment.

**Construction physique** :

- Aucune fenêtre extérieure.
- Murs, planchers et plafonds renforcés.
- Cloisons pleine hauteur (dalle de plancher à dalle de plafond, et non faux plafond).
- Surveillance environnementale (suppression d'incendie, détection d'eau, capteurs de température et d'humidité).
- Couverture CCTV avec enregistrement (conservation conformément à ISMS-OP-POL-A.7.4-5-11).

**Journalisation et surveillance des accès** (salles de serveurs et centres de données) :
- Tout accès consigné avec identité, horodatage, heure d'entrée/sortie.
- Journaux d'accès révisés **hebdomadairement** par le Responsable de la sécurité informatique.
- Anomalies investiguées (accès hors heures, schémas d'accès inhabituels, visiteurs inattendus).
- Conservation des journaux d'accès : **3 ans** (durée supérieure aux 12 mois standard en raison de la protection des actifs critiques).
- Alertes en temps réel pour : accès hors heures non planifié, tentatives d'authentification répétées échouées, porte maintenue ouverte >2 minutes.
- **Corrélation accès physique–changements** : Lors de changements de serveurs ou d'infrastructure, les journaux d'accès physique sont révisés pour vérifier que le travail a été effectué par du personnel autorisé.

**Pour les centres de données et la colocation tiers** :

- Des protections équivalentes devront être assurées par des garanties fournisseur (certificat ISO 27001, rapport SOC 2 Type II) et des exigences de sécurité contractuelles.
- Lorsqu'une équivalence exacte n'est pas réalisable, un traitement documenté des risques avec des mesures compensatoires devra être enregistré.

### Sécurité des salles de réunion

- Les salles de réunion devront être vérifiées pour la présence d'appareils d'enregistrement ou de matériaux oubliés avant des discussions sensibles.
- Les tableaux blancs et les blocs de conférence devront être effacés ou retirés après les réunions.
- Les documents ne devront pas être laissés dans les salles de réunion après la fin des réunions.
- Les équipements de vidéoconférence devront être sécurisés lorsqu'ils ne sont pas utilisés ; les caméras et microphones devront être dans un état connu d'arrêt entre les réunions.

### Points d'accès réseau et câblage

- L'accès physique aux équipements réseau (commutateurs, routeurs, points d'accès sans fil, panneaux de brassage) devra être limité au personnel informatique autorisé.
- Les prises et ports réseau dans les Zones Publiques devront être désactivés ou ne devront pas fournir d'accès au réseau interne.
- Les prises et ports réseau dans les Zones Contrôlées fournissant un accès au réseau interne devront être sécurisés par des contrôles d'accès physique à la zone.
- Les visiteurs ne devront pas connecter des appareils aux ports réseau internes sauf autorisation explicite et accompagnement.
- Le câblage d'alimentation et de télécommunications transportant des données devra être protégé contre l'interception, les interférences et les dommages.
- Les câbles d'alimentation devront être séparés des câbles de communication pour éviter les interférences.
- L'accès aux salles de câblage et aux panneaux de brassage devra être limité par un contrôle d'accès physique (Zone Restreinte minimum).
- Lorsque le câblage souterrain entrant dans le bâtiment est réalisable, les lignes d'alimentation et de télécommunications vers les installations de traitement de l'information devraient être acheminées en souterrain.

### Zones sécurisées — Exigences supplémentaires

En plus des contrôles basés sur les zones ci-dessus, les exigences suivantes s'appliquent à toutes les zones sécurisées désignées (Zones Restreintes et Haute Sécurité) :

- Les droits d'accès aux zones sécurisées devront être accordés par défaut selon le principe du refus — l'accès n'est accordé que sur autorisation explicite.
- Les équipements photographiques, vidéo, audio ou d'enregistrement (y compris les caméras des appareils mobiles) ne devront pas être autorisés dans les zones sécurisées, sauf autorisation spécifique du propriétaire de la zone.
- Le personnel travaillant dans des zones sécurisées devra être informé des exigences et restrictions de sécurité spécifiques applicables à cette zone.
- Le travail non supervisé dans les Zones Haute Sécurité devrait être évité, tant pour des raisons de sécurité personnelle que pour prévenir les opportunités d'activités malveillantes.

### Formation et sensibilisation

**Formation annuelle à la sensibilisation à la sécurité physique** pour tout le personnel, couvrant :
- Utilisation des badges (porter visiblement, ne pas partager, signaler immédiatement si perdu)
- Interpellation des personnes non reconnues (interrogation polie : « Puis-je vous aider ? » ou « Avez-vous un accompagnateur ? »)
- Prévention de la filature (ne pas retenir les portes, une personne par validation de badge)
- Politique de bureau propre (verrouiller les documents lors du départ du poste de travail)
- Signalement des incidents de sécurité physique (quoi signaler, comment signaler, à qui)
- Responsabilités d'accompagnement des visiteurs

**Formation spécifique aux rôles** :
- **Réception/Sécurité** : Procédures de gestion des visiteurs, émission/désactivation des badges, procédures d'urgence.
- **Installations** : Fonctionnement du système de contrôle d'accès, gestion des zones, exigences d'accompagnement des sous-traitants.
- **Informatique** : Sécurité des points d'accès réseau, procédures d'accès aux salles de serveurs, sécurité des salles d'équipement.

**Formation des nouveaux employés** : Formation à la sécurité physique dans les **5 jours ouvrables** suivant la date de prise de fonctions, avant l'attribution de l'accès aux zones.

Suivi de la réalisation de la formation ; objectif : **95 % de réalisation** annuellement.

### Visites de contrôle de la sécurité physique

La conformité aux exigences de sécurité des bureaux, salles de réunion et installations devra être vérifiée via des visites de contrôle de la sécurité physique documentées :

- **Fréquence** : Au moins trimestriellement, et après tout incident de sécurité matériel ou modification des installations.
- **Portée** : Toutes les zones de sécurité, points d'entrée, zones sensibles, salles de serveurs, salles de câblage et salles de réunion.
- **Constatations** : Documentées comme non-conformités ou actions d'amélioration avec un responsable assigné, une date d'échéance et un suivi jusqu'à la clôture.
- **Liste de vérification** : Une liste de vérification standardisée devra être maintenue et utilisée pour toutes les inspections.

---

## Rôles et responsabilités

| Rôle | Responsabilités |
|------|-----------------|
| **Direction générale** | Approuver la politique ; allouer le budget pour l'infrastructure de sécurité physique ; recevoir des rapports sur la posture de sécurité physique |
| **RSSI** | Propriété de la politique ; définir les normes de sécurité physique ; superviser la conformité ; approuver les exceptions ; réviser les indicateurs de sécurité physique |
| **Responsable des installations** | Mettre en œuvre et maintenir les contrôles de sécurité physique ; gérer les systèmes de contrôle d'accès ; coordonner la sécurité du bâtiment ; gérer les sous-traitants et la maintenance |
| **Sécurité informatique** | Intégrer les contrôles d'accès physique et logique ; gérer la sécurité des points d'accès réseau ; réviser l'accès aux salles de serveurs ; soutenir la réponse aux incidents |
| **Réception / Personnel de sécurité** | Opérer la gestion des visiteurs ; surveiller les points d'entrée ; répondre aux alarmes et alertes ; interpeller les personnes non reconnues |
| **Responsables hiérarchiques** | Autoriser l'accès physique pour les membres de l'équipe ; réviser et confirmer les droits d'accès trimestriellement ; signaler les départs et changements de rôle pour la révocation des accès |
| **RH** | Notifier les Installations des nouvelles embauches, changements de rôle et résiliations pour le provisionnement/la révocation des accès ; gérer l'intégration des sous-traitants |
| **Tout le personnel** | Suivre les procédures d'accès ; porter les badges visiblement ; interpeller ou signaler les personnes non reconnues ; signaler les badges perdus et les événements de sécurité physique ; respecter les exigences de bureau propre |

**Chemins d'escalade** :

### Signalement des incidents de sécurité physique

Tout le personnel devrait immédiatement signaler les événements de sécurité physique à la Réception, au Responsable des installations ou au Personnel de sécurité. Les événements à signaler incluent :

**Critique (escalade immédiate au RSSI)** :
- Personne non autorisée découverte dans une Zone Restreinte ou Haute Sécurité
- Preuve d'intrusion physique (portes forcées, fenêtres brisées, serrures altérées)
- Vol ou vol présumé d'équipements ou de documents
- Menaces physiques ou confrontations dans les locaux
- Clonage ou altération de badge découvert

**Priorité élevée** :
- Filature réussie dans une zone sécurisée
- Visiteur non accompagné dans une Zone Contrôlée
- Porte de sécurité maintenue ouverte délibérément (contournement délibéré)
- Badge perdu avec accès aux Zones Haute Sécurité ou Restreintes

**Priorité standard** :
- Badge perdu avec accès à la Zone Contrôlée uniquement
- Visiteur sans badge au-delà de la réception
- Défaillance des installations (serrure cassée, capteur de porte défaillant)
- Violation de la politique de bureau propre

**Canaux de signalement** : Réception (pendant les heures ouvrables), Responsable des installations, [numéro d'urgence] (hors heures), RSSI (pour les événements critiques).

**Chemins d'escalade** :

- **Incidents de sécurité physique** : Employé/Personnel de sécurité → Responsable des installations → RSSI → Direction générale
- **Demandes d'accès** : Employé → Responsable hiérarchique (approbation) → Responsable des installations (provisionnement)
- **Problèmes avec les visiteurs** : Réception → Responsable des installations → RSSI
- **Badges perdus/volés** : Employé → Réception/Installations (désactivation immédiate) → Sécurité informatique (si implications d'accès système)
- **Non-conformité du sous-traitant** : Accompagnateur/Superviseur → Responsable des installations → Achats/Propriétaire du contrat

---

## Preuves pour cette politique

| # | Preuve | Responsable | Fréquence | Conservation |
|---|--------|-------------|-----------|--------------|
| 1 | **Documentation des zones de sécurité et plans d'étage** indiquant les limites des zones, les points d'entrée et les mécanismes de contrôle d'accès | Responsable des installations | Mis à jour lors de changements des installations ; révisé annuellement | Version actuelle + version précédente |
| 2 | **Configuration du système de contrôle d'accès** — attributions de zones, niveaux d'authentification, règles d'accès basées sur les rôles | Installations / Informatique | Révisé trimestriellement | Configuration actuelle + journal des changements |
| 3 | **Journaux du système de contrôle d'accès** — événements d'entrée/sortie avec identité, horodatage, point d'entrée (accordés et refusés) | [Système de contrôle d'accès] | Continu ; révisé mensuellement pour les anomalies | 12 mois minimum |
| 4 | **Journaux des visiteurs** — dossiers d'enregistrement avec nom, entreprise, hôte, date/heure d'entrée/sortie, identification vérifiée | Réception / [Système de gestion des visiteurs] | Continu | 12 mois minimum |
| 5 | **Dossiers de révision des droits d'accès** — révision trimestrielle des droits d'accès du personnel avec validation du responsable | Responsable des installations / Responsables hiérarchiques | Trimestrielle | 3 ans |
| 6 | **Rapports d'inspection des périmètres** — constatations documentées des inspections des périmètres du bâtiment et des zones | Responsable des installations | Annuel (bâtiment) ; trimestriel (Restreint/Haute Sécurité) | 3 ans |
| 7 | **Rapports de visite de contrôle de la sécurité physique** — résultats des listes de vérification, constatations et suivi des remédiations | Responsable des installations / RSSI | Trimestrielle | 3 ans |
| 8 | **Dossiers de gestion des badges** — émission, remplacement, désactivation, signalements de perte/vol | Responsable des installations | Par événement ; audité annuellement | Durée de l'emploi + 1 an |
| 9 | **Dossiers d'accès des sous-traitants et du personnel de maintenance** — préautorisation, portée, dossiers d'accompagnement | Responsable des installations | Par mission | 3 ans |
| 10 | **Dossiers d'assurance fournisseur** pour les installations de colocation/partagées — certificats, rapports SOC, conditions contractuelles | RSSI / Achats | Révisé annuellement | Durée du contrat + 2 ans |
| 11 | **Registre des exceptions** — exceptions approuvées avec justification, mesures compensatoires, date d'expiration | RSSI | Mis à jour par exception ; révisé trimestriellement | 3 ans après la clôture de l'exception |
| 12 | **Rapports d'incidents de sécurité physique** — tentatives d'accès non autorisé, pertes de badges, événements de filature, violations du périmètre | RSSI / Responsable des installations | Par incident | 3 ans |

---

# Conformité à la politique

## Mesure de la conformité

L'équipe de management de la sécurité de l'information vérifiera la conformité à la présente politique par diverses méthodes, notamment : les rapports du système de contrôle d'accès, les audits des journaux de visiteurs, les résultats des visites de contrôle de la sécurité physique, les taux de réalisation des révisions des droits d'accès, les indicateurs de gestion des badges, les révisions d'assurance fournisseur, les audits internes et externes, et les retours au propriétaire de la politique.

**Indicateurs clés** :

| Indicateur | Objectif | Fréquence de révision |
|-----------|---------|----------------------|
| Couverture du contrôle d'accès (% des points d'entrée avec contrôles actifs) | 100 % | Trimestrielle |
| Révisions des droits d'accès complétées dans les délais | 100 % | Trimestrielle |
| Conformité à l'accompagnement des visiteurs (Zones Restreintes/Haute Sécurité) | 100 % | Mensuelle |
| Accès des employés résiliés révoqué le même jour | 100 % | Par événement ; audité mensuellement |
| Incidents de perte/vol de badges | < 5 par trimestre | Trimestrielle |
| Tentatives d'accès non autorisé (réussies) | 0 | Mensuelle |
| Réalisation des visites de contrôle de la sécurité physique | 100 % dans les délais | Trimestrielle |
| Révisions d'assurance fournisseur à jour | 100 % | Annuelle |

**Rapports** :
- **Tableau de bord mensuel** au RSSI : Conformité à la révocation des accès, incidents de perte de badges, tentatives d'accès non autorisé, conformité à l'accompagnement des visiteurs.
- **Rapport trimestriel** à la Direction générale : Tous les indicateurs, analyse des tendances, constatations des visites de contrôle, statut des exceptions.
- **Rapport annuel** à la Revue de direction : Efficacité du programme de sécurité physique, recommandations d'investissements en capital, statut de conformité réglementaire.

Les indicateurs dépassant les objectifs devront être escaladés immédiatement au RSSI avec un plan de remédiation incluant un responsable et une date cible.

## Exceptions

Toute exception à la présente politique devra être approuvée et enregistrée à l'avance par le RSSI, avec une justification métier documentée, une évaluation des risques, des mesures compensatoires et une date d'expiration définie (maximum 6 mois, renouvelable avec réévaluation). Les exceptions devront être rapportées à l'équipe de revue de direction.

**Exceptions autorisées** (avec mesures compensatoires appropriées) :

- Accès d'urgence temporaire pour des réparations urgentes (avec surveillance renforcée et accompagnement).
- Accès visiteur prolongé pour les auditeurs ou les inspecteurs réglementaires (avec approbation documentée et portée définie).
- Méthodes d'authentification alternatives pour le personnel ayant des exigences d'accessibilité.

**Non autorisé** comme exceptions :

- Contournement permanent des exigences d'authentification des zones.
- Exceptions sans mesures compensatoires.
- Exceptions à la révocation d'accès le même jour pour les employés résiliés.

## Non-conformité

Un employé reconnu coupable de violation de la présente politique peut faire l'objet de mesures disciplinaires pouvant aller jusqu'au licenciement. Scénarios spécifiques de non-conformité et réponses :

- **Filature ou permission de filature** : Avertissement formel ; infraction répétée déclenchant le processus disciplinaire.
- **Partage ou prêt de badge** : Désactivation immédiate du badge ; processus disciplinaire.
- **Manquement à l'interpellation ou au signalement de personnes non reconnues** : Traité par la formation à la sensibilisation.
- **Maintien délibéré d'une porte sécurisée ouverte** : Remédiation immédiate ; avertissement formel si délibéré.

Les sous-traitants reconnus en non-conformité peuvent se voir révoquer leur accès et leur organisation contractante peut être notifiée.

## Amélioration continue

La présente politique est révisée et mise à jour dans le cadre du processus d'amélioration continue. Les révisions devront prendre en compte :

- Les changements d'installations (déménagements de bureaux, rénovations, nouveaux sites, changements de bail).
- Les incidents de sécurité physique et quasi-incidents (accès non autorisé, filature, violations du périmètre).
- Les constatations d'audit et les résultats des visites de contrôle.
- Les avancées technologiques en matière de contrôle d'accès (accréditations mobiles, biométrie sans contact, détection d'anomalies renforcée par IA).
- Les changements réglementaires (notamment la nLPD, les exigences cantonales de protection des données et les mises à jour du RGPD UE).
- L'évolution du paysage des menaces (p. ex., augmentation de l'ingénierie sociale ciblant l'accès physique).
- Les enseignements tirés des événements de sécurité physique dans l'organisation ou rapportés dans le secteur.

Les actions d'amélioration devront être suivies, attribuées à un responsable et rapportées au RSSI et à l'équipe de revue de direction.

---

# Domaines de la norme ISO 27001 couverts

Politique de contrôle d'accès physique — Correspondance avec les contrôles ISO 27001:2022

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership et engagement | 5.1 Politiques de sécurité de l'information |
| Clause 5.2 Politique | 5.4 Responsabilités de la direction |
| Clause 6.1 Actions face aux risques et opportunités | 5.36 Conformité aux politiques, règles et normes |
| Clause 6.2 Objectifs de sécurité de l'information | 6.3 Sensibilisation, formation et éducation à la sécurité de l'information |
| Clause 7.3 Sensibilisation | 6.4 Processus disciplinaire |
| Clause 8.1 Planification et contrôle opérationnels | **7.1 Périmètres de sécurité physique** |
| Clause 9.1 Surveillance, mesure, analyse, évaluation | **7.2 Entrée physique** |
| Clause 10.2 Non-conformité et action corrective | **7.3 Sécurisation des bureaux, salles et installations** |
| | 7.4 Surveillance de la sécurité physique |
| | 7.6 Travail dans des zones sécurisées |
| | 7.8 Emplacement et protection des équipements |

---

# Cadre réglementaire

| Cadre | Applicabilité | Pertinence pour le contrôle d'accès physique |
|-------|---------------|---------------------------------------------|
| **nLPD suisse (nFADP/revDSG)** | **Obligatoire** — tout traitement de données personnelles | Art. 8 — Mesures techniques et organisationnelles appropriées aux risques ; sécurité physique des locaux où les données personnelles sont traitées ou stockées |
| **OPDo suisse (Ordonnance sur la protection des données)** | **Obligatoire** — complète la nLPD | Art. 1-3 — Exigences minimales en matière de sécurité des données, incluant les contrôles d'accès physique |
| **ISO/IEC 27001:2022** | **Obligatoire** — périmètre de certification | Contrôles Annexe A 7.1, 7.2, 7.3 |
| **ISO/IEC 27002:2022** | **Guide** | Sections 7.1, 7.2, 7.3 — Lignes directrices de mise en œuvre des contrôles physiques |
| **RGPD UE** | **Conditionnel** — lors du traitement de données personnelles UE/EEE | Art. 32 — Sécurité du traitement, incluant les mesures de sécurité physique |
| **PCI DSS v4.0** | **Conditionnel** — lors du traitement de données de cartes de paiement | Exigence 9 — Restreindre l'accès physique aux données des titulaires de cartes ; requiert un accès contrôlé par badge, des journaux de visiteurs, des procédures de destruction des supports |
| **FINMA Circulaire 2023/1** | **Conditionnel** — institutions financières suisses réglementées | Gestion du risque opérationnel incluant la sécurité physique de l'infrastructure critique |
| **NIST SP 800-53 Rév. 5** | **Guide** | Famille PE — Contrôles de protection physique et environnementale |
| **CIS Controls v8** | **Guide** | Contrôle 3 (Protection des données), Contrôle 6 (Gestion du contrôle d'accès) — dimensions de l'accès physique |

---

<!-- QA_VERIFIED: 2026-03-29 -->
