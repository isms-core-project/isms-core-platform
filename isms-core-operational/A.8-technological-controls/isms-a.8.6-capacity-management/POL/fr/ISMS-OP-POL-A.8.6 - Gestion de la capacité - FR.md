<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.8.6-FR:operational:OP-POL:a.8.6 -->
**ISMS-OP-POL-A.8.6 — Gestion de la capacité**

---

**Contrôle documentaire**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Gestion de la capacité |
| **Type de document** | Politique opérationnelle |
| **Identifiant du document** | ISMS-OP-POL-A.8.6 |
| **Créateur du document** | Responsable de la sécurité des systèmes d'information (RSSI) |
| **Propriétaire du document** | Directeur général (DG) |
| **Approuvé par** | Direction générale |
| **Date de création** | [Date] |
| **Version** | 1.0 |
| **Date de version** | [À déterminer] |
| **Classification** | Usage interne |
| **Statut** | Brouillon |

**Historique des versions** :

| Version | Date | Auteur | Modifications |
|---------|------|--------|---------------|
| 1.0 | [Date] | RSSI | Politique opérationnelle initiale pour ISO 27001:2022 |

**Cycle de révision** : Annuel (aligné sur le cycle de planification de la capacité)
**Prochaine date de révision** : [Date d'entrée en vigueur + 12 mois]

**Approuvé par** : [RSSI / Direction générale]

**Documents associés** :

- ISO/IEC 27001:2022 Contrôle A.8.6 — Gestion de la capacité
- ISO/IEC 27002:2022 Section 8.6 — Recommandations de mise en œuvre pour la gestion de la capacité
- NIST SP 800-53 Rév. 5 — AU-4 (Capacité de stockage des journaux d'audit), CP-2(2) (Planification de la capacité), SC-5 (Protection contre les dénis de service)
- ITIL 4 — Pratique de gestion de la capacité et des performances

**Contrôles Annexe A associés** :

| Contrôle | Relation avec la gestion de la capacité |
|----------|-----------------------------------------|
| A.5.30–8.13–14 Continuité d'activité et PRA | Planification de la capacité du site de reprise ; capacité de stockage des sauvegardes |
| A.7.11 Utilités de support | Capacité des infrastructures physiques (énergie, refroidissement, espace baies) |
| A.8.1–7–18–19 Sécurité des points de terminaison | Supervision des ressources des points de terminaison et capacité du parc |
| A.8.8 Gestion des vulnérabilités | Capacité des outils d'analyse ; ressources requises pour le déploiement des correctifs |
| A.8.9 Gestion de la configuration | Les configurations de référence incluent les seuils de capacité |
| A.8.15 Journalisation | Planification de la capacité de stockage des journaux et gestion de la conservation |
| A.8.16 Activités de supervision | Les métriques de capacité constituent un sous-ensemble de la supervision globale |
| A.8.20–22 Sécurité des réseaux | Capacité de la bande passante et du débit réseau |

**Politiques internes associées** :

- Politique des activités de supervision (A.8.16)
- Politique de continuité d'activité et de reprise après sinistre (A.5.30–8.13–14)
- Politique de journalisation (A.8.15)
- Politique de sécurité des réseaux (A.8.20–22)
- Politique de gestion des changements (A.8.32)

---

# Politique de gestion de la capacité

## Objet

La présente politique a pour objet de s'assurer que l'utilisation des ressources de traitement de l'information est supervisée et ajustée en fonction des besoins de capacité actuels et anticipés, afin de prévenir les interruptions de service causées par l'épuisement des ressources et de soutenir les décisions d'investissement éclairées.

La gestion de la capacité est à la fois une nécessité opérationnelle et un contrôle de sécurité. Une capacité insuffisante peut provoquer des interruptions de service, dégrader la supervision de la sécurité, empêcher la collecte des journaux d'audit et créer des conditions exploitables par des attaques par déni de service. Une planification proactive de la capacité garantit que les infrastructures, les applications et les services de support restent disponibles, performants et sécurisés.

Cette politique soutient la nLPD suisse (revDSG) art. 8 en mettant en œuvre des mesures techniques et organisationnelles proportionnées au risque pour protéger la disponibilité et l'intégrité des systèmes traitant des données personnelles. Lorsque l'organisation traite des données de personnes situées dans l'UE/EEE, les exigences du RGPD art. 32 relatives à la disponibilité et à la résilience continues des systèmes de traitement s'appliquent également.

## Champ d'application

La présente politique s'applique à l'ensemble des ressources d'infrastructure, d'application et de service dans le périmètre du SMSI nécessitant une supervision et une planification de la capacité. Cela comprend :

- **Ressources de calcul** : Serveurs, machines virtuelles, conteneurs, instances cloud (utilisation CPU et mémoire).
- **Ressources de stockage** : Stockage sur disque, stockage de base de données, stockage de sauvegarde, stockage d'archivage, stockage de journaux.
- **Ressources réseau** : Bande passante, débit, connexions, capacité d'équilibrage de charge, capacité des requêtes DNS.
- **Ressources applicatives** : Utilisateurs simultanés, taux de transactions, limites des taux API, profondeur des files de messages.
- **Ressources des services cloud** : Quotas de service, limites d'instances, limites des appels API, capacité réservée.
- **Capacité de licences** : Licences logicielles, sièges d'abonnement, utilisation des licences simultanées.
- **Infrastructure physique** : Capacité électrique, capacité de refroidissement, espace baies (conformément à A.7.11).

Tous les employés, prestataires et fournisseurs de services tiers ayant des responsabilités en matière de gestion de l'infrastructure, des applications ou des services.

**Hors périmètre** : Optimisation des performances applicatives et du code (couverts par le développement sécurisé) ; gestion détaillée des actifs logiciels et approvisionnement en licences (couverts par la gestion des actifs A.5.9) ; capacité des bâtiments physiques sans lien avec le traitement de l'information.

## Principe

L'organisation supervise, prévoit et planifie de manière proactive les besoins en capacité pour l'ensemble des ressources critiques. La gestion de la capacité suit le principe de la prévention plutôt que de la réaction — il est nettement moins coûteux et moins perturbateur de planifier la croissance de la capacité que de réagir à des incidents d'épuisement.

Les décisions en matière de capacité sont fondées sur les données, basées sur les tendances d'utilisation mesurées et les projections documentées de croissance de l'activité, et non sur des hypothèses ou des suppositions. Les ressources maintiennent une marge suffisante pour absorber les pics de demande imprévus sans dégradation du service.

---

## Supervision des ressources

### Couverture de la supervision

Tous les systèmes et services de production doivent disposer d'une supervision de la capacité activée. La supervision couvre, au minimum, les catégories de ressources énumérées dans la section Champ d'application.

**Exigences de couverture** :

| Environnement | Objectif de couverture | Fréquence de supervision |
|---------------|------------------------|--------------------------|
| Systèmes de production | 100 % | Toutes les 5 minutes ou moins |
| Reprise après sinistre / serveur de secours | 100 % | Toutes les 15 minutes ou moins |
| Hors production (pré-production, test) | 90 % | Toutes les 15 minutes ou moins |

La supervision est mise en œuvre via [Plateforme de supervision] (par exemple Prometheus, Zabbix, Datadog, Azure Monitor, CloudWatch, ou équivalent). La plateforme est documentée dans l'inventaire des actifs avec son modèle d'hébergement, la résidence des données et les contrôles d'accès administrateur.

### Métriques supervisées

Les métriques suivantes sont collectées pour chaque type de ressource applicable :

| Type de ressource | Métriques | Unités |
|-------------------|-----------|--------|
| **CPU** | Utilisation (moyenne, pic), charge moyenne, temps d'attente | Pourcentage, valeur |
| **Mémoire** | Utilisation, utilisation du swap, mémoire disponible | Pourcentage, Go |
| **Stockage** | Capacité utilisée, capacité disponible, taux de croissance, IOPS | Go/To, pourcentage, opérations/s |
| **Réseau** | Utilisation de la bande passante, perte de paquets, latence, nombre de connexions | Mbps/Gbps, pourcentage, ms, valeur |
| **Application** | Utilisateurs simultanés, sessions actives, taux de transactions, profondeur de file | Valeur, transactions/s |
| **Quotas cloud** | Utilisation des limites de service par région et par compte | Pourcentage du quota |
| **Licences** | Allocations actives par rapport aux droits totaux | Valeur, pourcentage |

### Conservation des métriques

- **Métriques brutes** : Minimum 30 jours à résolution complète (pour l'investigation des incidents).
- **Métriques agrégées** : Minimum 12 mois à granularité horaire ou quotidienne (pour l'analyse des tendances).
- **Résumés historiques** : Minimum 36 mois à granularité mensuelle (pour la planification stratégique).

Les données métriques sont protégées contre toute modification ou suppression non autorisée. Lorsque les métriques alimentent la supervision de la sécurité (A.8.16), les exigences d'intégrité des journaux de la Politique de journalisation (A.8.15) s'appliquent également.

---

## Référentiel de seuils et alertes

### Niveaux de seuils

Tous les ressources supervisées disposent de seuils de capacité définis à trois niveaux :

| Niveau | Objet | Plage habituelle | Action |
|--------|-------|------------------|--------|
| **Avertissement** | Indication précoce de pression sur la capacité | 70–80 % d'utilisation | Revue de la planification de la capacité ; analyse de la tendance de croissance |
| **Critique** | Capacité approchant l'épuisement | 85–90 % d'utilisation | Investigation immédiate ; lancement de l'extension de capacité ou de la mitigation de charge |
| **Maximum** | Épuisement de la ressource imminent ou en cours | 95 %+ d'utilisation | Réponse d'urgence ; activation de la gestion des incidents en cas d'impact sur le service |

Les valeurs exactes des seuils sont définies par type de ressource et classification du système, documentées dans la plateforme de supervision et révisées trimestriellement. Les seuils sont ajustés en fonction des taux de faux positifs, des schémas de charge et des incidents quasi-manqués.

**Les seuils spécifiques au stockage** tiennent également compte du taux de croissance : si le stockage est projeté pour atteindre 95 % dans les 30 jours au taux de consommation actuel, une alerte d'avertissement est générée quel que soit le pourcentage actuel.

### Configuration des alertes

Les alertes de seuil de capacité sont configurées avec :

- **Acheminement** : Alertes transmises à l'équipe des opérations responsable via [Outil d'alerte] (par exemple PagerDuty, Opsgenie, ServiceNow, ou équivalent).
- **Délai de transmission** : Alertes transmises dans les 5 minutes suivant la détection du dépassement de seuil.
- **Escalade** : Alertes d'avertissement sans accusé de réception escaladées après 4 heures ; alertes critiques sans accusé de réception escaladées après 30 minutes.
- **Déduplication** : Alertes répétées pour la même ressource et le même seuil supprimées pour éviter la fatigue aux alertes ; réalerte si la condition persiste au-delà de la fenêtre de suppression.
- **Intégration** : Les alertes critiques et maximales créent automatiquement des incidents dans [Outil ITSM] (par exemple ServiceNow, Jira Service Management, ou équivalent).

### Réponse aux alertes

| Niveau d'alerte | Délai de réponse | Action de réponse |
|-----------------|------------------|-------------------|
| **Avertissement** | Accusé de réception dans les 4 heures (heures ouvrées) | Analyser les données de tendance ; mettre à jour la prévision de capacité ; planifier l'extension si nécessaire |
| **Critique** | Accusé de réception dans les 30 minutes | Investiguer la cause profonde ; mettre en œuvre une mitigation immédiate (délestage, mise à l'échelle temporaire) ; lancer l'extension de capacité |
| **Maximum** | Accusé de réception dans les 15 minutes | Exécuter la réponse d'urgence ; activer la gestion des incidents conformément à A.5.24–28 en cas d'impact sur le service ; mettre en œuvre une extension d'urgence de la capacité |

---

## Prévision de la capacité

### Horizons de prévision

L'organisation élabore et maintient des prévisions de capacité à trois horizons :

| Horizon | Période | Objet | Fréquence de mise à jour |
|---------|---------|-------|--------------------------|
| **Court terme** | 3–6 mois | Planification tactique ; approvisionnement immédiat | Mensuel |
| **Moyen terme** | 6–12 mois | Planification budgétaire ; renouvellements de contrats | Trimestriel |
| **Long terme** | 12–24 mois | Planification stratégique ; décisions de migration vers le centre de données ou le cloud | Annuel |

### Méthodologie de prévision

Les prévisions sont basées sur :

- **Analyse des tendances historiques** : Extrapolation à partir des données d'utilisation mesurées (minimum 6 mois de données requis pour des tendances fiables).
- **Projections de croissance de l'activité** : Contributions des propriétaires d'applications et des unités métier sur les projets planifiés, la croissance du nombre d'utilisateurs, les augmentations de volume de données et les nouveaux lancements de services.
- **Schémas saisonniers** : Identification et modélisation des variations périodiques de la demande (traitement de fin de mois, cycles de reporting annuels, campagnes marketing).
- **Changements planifiés** : Déploiements, migrations, décommissionnements et modifications d'infrastructure programmés.

Lorsque les données historiques sont insuffisantes (nouveaux systèmes ou services), des estimations conservatrices sont utilisées avec une révision plus fréquente au cours des 6 premiers mois d'exploitation.

### Précision des prévisions

- **Précision cible** : Les prévisions se situent dans un écart de +/-15 % par rapport à l'utilisation réelle (mesurée trimestriellement).
- **Nouveaux systèmes (6 premiers mois)** : Précision de +/-30 % acceptable pendant l'établissement des référentiels.
- **Charges de travail à forte variabilité** : Précision de +/-25 % avec justification documentée.
- **Écarts dépassant 15 %** : Analyse des causes profondes requise dans les 10 jours ouvrés ; résultats documentés et intégrés dans le prochain cycle de prévision.

---

## Politiques de mise à l'échelle automatique

Lorsque l'organisation exploite une infrastructure cloud, la mise à l'échelle automatique est configurée pour les charges de travail à schémas de demande variables.

### Exigences de mise à l'échelle automatique

| Exigence | Norme |
|----------|-------|
| **Déclencheur de mise à l'échelle** | Utilisation CPU, mémoire, taux de requêtes, profondeur de file ou métriques applicatives personnalisées |
| **Seuil d'extension** | Défini par charge de travail ; typiquement 70–80 % de la métrique cible pendant 3–5 minutes de manière soutenue |
| **Seuil de réduction** | Défini par charge de travail ; typiquement 30–40 % de la métrique cible pendant 10–15 minutes de manière soutenue |
| **Instances minimales** | Au moins 2 pour les charges de travail de production (disponibilité) ; au moins 1 pour la hors-production |
| **Instances maximales** | Définies par charge de travail pour prévenir les dépassements de coûts ; alignées sur les contraintes budgétaires |
| **Période de refroidissement** | Minimum 5 minutes entre les actions de mise à l'échelle pour éviter les oscillations |

### Gouvernance de la mise à l'échelle automatique

- Les configurations de mise à l'échelle automatique sont documentées et soumises au contrôle de version.
- Les modifications des politiques de mise à l'échelle automatique pour les charges de travail de production suivent le processus de gestion des changements (A.8.32).
- Les limites maximales d'instances sont révisées trimestriellement et alignées sur les budgets approuvés.
- Les événements de mise à l'échelle automatique sont journalisés et examinés mensuellement pour identifier les opportunités d'optimisation.
- **Garde-fous de coûts** : Des limites mensuelles de dépenses maximales sont configurées au niveau du compte ou de l'abonnement cloud. Une mise à l'échelle automatique susceptible de dépasser la limite de dépenses déclenche une alerte au Responsable de l'infrastructure et au délégué du DFin.

Lorsque la mise à l'échelle automatique n'est pas disponible ou appropriée (infrastructure sur site, services à capacité fixe), les procédures d'extension manuelle de la capacité sont documentées avec les délais d'approvisionnement et de déploiement définis.

---

## Optimisation de la capacité et des coûts

La gestion de la capacité équilibre la disponibilité, la performance et les coûts. Le surprovisionnement gaspille le budget ; le sous-provisionnement crée des risques. L'organisation optimise activement l'allocation des ressources sur la base des données d'utilisation mesurées.

### Stratégies d'optimisation

| Stratégie | Description | Applicabilité |
|-----------|-------------|---------------|
| **Dimensionnement adapté** | Éliminer les ressources surprovisionnées où l'utilisation soutenue est inférieure à 40 % | Tous les environnements |
| **Capacité réservée** | Acheter des instances réservées ou des remises d'utilisation engagée pour les charges de travail stables (par exemple AWS RIs, Azure RIs, GCP CUDs) | Environnements cloud avec base de référence prévisible |
| **Instances spot/préemptibles** | Utiliser pour les charges de travail non critiques et interruptibles (traitement par lots, test, développement) | Environnements cloud avec charges de travail tolérantes aux pannes |
| **Mise à l'échelle automatique** | Aligner la capacité sur la demande en temps réel pour éviter de payer des ressources inactives | Environnements cloud avec demande variable |
| **Cycle de vie du stockage** | Basculer les données peu fréquemment consultées vers des classes de stockage moins coûteuses (par exemple S3 Glacier, Azure Cool/Archive, GCS Nearline/Coldline) | Tout stockage avec des schémas d'accès définis |

### Revue trimestrielle des coûts

Le Responsable de l'infrastructure conduit une revue trimestrielle des coûts comprenant :

- Identification des ressources surprovisionnées (utilisation soutenue constamment inférieure à 40 %).
- Évaluation des ratios capacité réservée par rapport aux dépenses à la demande.
- Évaluation des opportunités de hiérarchisation du stockage.
- Rapport sur les actions d'optimisation des coûts entreprises et les économies réalisées.

Les résultats de l'optimisation des coûts sont inclus dans le rapport trimestriel de revue de la capacité présenté au DSI, au RSSI et au délégué du DFin.

---

## Capacité et objectifs de niveau de service

Les seuils de capacité sont alignés sur les objectifs de niveau de service (ONS) pour s'assurer que les contraintes de capacité ne dégradent pas la qualité de service en dessous des niveaux convenus. La corrélation entre l'utilisation des ressources et les performances du service est documentée pour chaque service critique.

### Alignement sur les ONS

| Type de service | ONS habituel | Alignement des seuils de capacité |
|-----------------|-------------|-----------------------------------|
| Application web | 99,9 % de disponibilité, latence p95 <500 ms | CPU inférieur à 75 % en moyenne (la latence se dégrade au-dessus de 75 %) |
| Service API | 99,95 % de disponibilité, latence p95 <200 ms | CPU inférieur à 70 % en moyenne ; mémoire inférieure à 80 % |
| Base de données | 99,99 % de disponibilité, délai de réponse aux requêtes <50 ms | IOPS inférieurs à 80 % du maximum ; connexions inférieures à 90 % du maximum |
| File de messages | 99,9 % de disponibilité, délai de traitement <5 s | Profondeur de file inférieure à 80 % du maximum ; capacité du consommateur maintenue |

Lorsque l'utilisation mesurée des ressources approche des niveaux susceptibles de dégrader les performances des ONS, les seuils de capacité sont ajustés à la baisse pour déclencher une intervention plus précoce. L'alignement sur les ONS est révisé trimestriellement dans le cadre du processus de revue de la capacité.

---

## Rapports de capacité

### Cadence des rapports

| Rapport | Audience | Fréquence | Contenu |
|---------|----------|-----------|---------|
| **Tableau de bord opérationnel** | Opérations informatiques | Continu (temps réel) | Utilisation actuelle, alertes actives, indicateurs de tendance |
| **Rapport mensuel de capacité** | Direction informatique, Responsable de l'infrastructure | Mensuel | Résumé d'utilisation, historique des alertes, points saillants des prévisions, actions de capacité entreprises |
| **Revue trimestrielle de la capacité** | DSI, RSSI, délégué du DFin | Trimestriel | Prévisions, plans d'extension, impact budgétaire, tableau de bord de santé, métriques de conformité |
| **Plan annuel de capacité** | Direction générale | Annuel | Plan stratégique avec projections pluriannuelles, besoins en investissements, évaluation des risques |

### Exigences de contenu des rapports

Les rapports mensuels et trimestriels comprennent :

- Utilisation actuelle par type de ressource (moyenne, pic, direction de la tendance).
- Nombre de dépassements de seuils et délais de réponse.
- Incidents liés à la capacité (nombre, gravité, résumé des causes profondes).
- Mesure de la précision des prévisions (réel par rapport au prévu).
- Modifications de capacité planifiées (extensions, décommissionnements, migrations).
- Utilisation budgétaire pour les dépenses de capacité.

Les rapports sont générés à partir des données de [Plateforme de supervision]. Le plan annuel de capacité est approuvé par le DSI et inclus dans la revue de direction conformément à la Clause 9.3 de l'ISO 27001.

---

## Gestion de la capacité de stockage

La capacité de stockage requiert une attention particulière en raison de ses caractéristiques de croissance continue et de l'impact direct sur la sécurité en cas d'épuisement du stockage (perte de journaux d'audit, impossibilité d'écrire des événements de sécurité, défaillances applicatives).

### Stockage des journaux

- La capacité de stockage des journaux est planifiée en coordination avec la Politique de journalisation (A.8.15) pour s'assurer que les exigences de conservation peuvent être satisfaites sans épuisement du stockage.
- Le stockage des journaux dispose d'un seuil d'avertissement dédié à 70 % et d'un seuil critique à 85 %.
- Si le stockage des journaux atteint le seuil critique, une rotation ou un archivage automatique des journaux est déclenché avant toute perte de données.
- Le taux de croissance du stockage des journaux est suivi et projeté mensuellement.

### Stockage des bases de données

- La croissance du stockage des bases de données est supervisée et prévue séparément du stockage de fichiers.
- Les activités de maintenance des bases de données (vacuum, reconstruction des index, archivage) sont intégrées dans la planification de la capacité.
- Les seuils de stockage des bases de données tiennent compte des surcharges opérationnelles (tables temporaires, journaux de transactions, décalage de réplication).

### Stockage des sauvegardes

- La capacité de stockage des sauvegardes est planifiée pour accueillir les jeux de sauvegardes complets pendant la période de conservation requise conformément à la politique de sauvegarde (A.5.30–8.13–14).
- La croissance du stockage des sauvegardes est prévue sur la base de la croissance des données de production et des modifications de la politique de conservation.

---

## Gestion de la capacité des licences

La capacité des licences logicielles est supervisée pour prévenir les violations de conformité et les interruptions de service causées par l'épuisement des licences.

### Exigences de supervision des licences

| Exigence | Norme |
|----------|-------|
| **Inventaire des licences** | Maintenu dans l'inventaire des actifs (A.5.9) avec les nombres de droits, les dates d'expiration et le type de licence (simultanée, nominative, par appareil) |
| **Supervision de l'utilisation** | Utilisation active suivie par rapport aux droits pour tous les logiciels critiques |
| **Seuil d'avertissement** | Alerte lorsque l'utilisation atteint 80 % des droits |
| **Seuil critique** | Alerte lorsque l'utilisation atteint 90 % des droits |
| **Fréquence de revue** | Revue d'utilisation trimestrielle ; planification annuelle des renouvellements |

### Planification des renouvellements de licences

Les renouvellements de licences sont suivis avec un préavis minimum de 90 jours avant l'expiration. Les besoins en capacité de licences sont inclus dans la prévision de capacité à moyen terme (6–12 mois) et alignés sur les cycles de planification budgétaire.

---

## Réponse aux incidents de capacité

Lorsque l'épuisement de la capacité cause ou menace de causer un impact sur le service, le processus de gestion des incidents de l'organisation (A.5.24–28) est activé.

### Procédures d'incidents spécifiques à la capacité

| Scénario | Classification | Réponse immédiate |
|----------|---------------|-------------------|
| **Seuil d'avertissement soutenu plus de 24 heures** | Événement de capacité (non-incident) | Révision et planification ; aucune action d'urgence requise |
| **Seuil critique soutenu plus d'1 heure** | Incident priorité 3 | Mettre en œuvre la mitigation de charge ; lancer l'extension d'urgence de la capacité |
| **Dégradation du service due à la capacité** | Incident priorité 2 | Mise à l'échelle d'urgence ou délestage ; notification des clients en cas d'impact externe |
| **Interruption de service due à l'épuisement de la capacité** | Incident priorité 1 | Réponse complète aux incidents ; approvisionnement d'urgence ; revue post-incident obligatoire |

### Revue post-incident

Tous les incidents liés à la capacité classés priorité 1 ou priorité 2 font l'objet d'une revue post-incident dans les 5 jours ouvrés. La revue détermine :

- Pourquoi la supervision et les prévisions n'ont pas empêché l'incident.
- Si les seuils nécessitent un ajustement.
- Si la méthodologie de prévision nécessite une amélioration.
- Quelle extension de capacité est nécessaire pour éviter une récidive.
- Si l'incident a révélé une lacune dans la couverture de la supervision.

Les résultats sont suivis dans le registre d'amélioration de la capacité jusqu'à la finalisation de la remédiation.

---

## Résilience face aux dénis de service

La planification de la capacité intègre la résilience contre les conditions de déni de service (DoS/DDoS). La capacité ne doit pas être planifiée uniquement pour des charges moyennes ou attendues à leur pic — une marge est maintenue pour absorber les pics de demande imprévus, y compris ceux causés par une activité malveillante.

### Exigences de marge

| Ressource | Marge minimale au pic | Justification |
|-----------|----------------------|---------------|
| **CPU** | 20 % | Absorber les pics de trafic sans dégradation |
| **Mémoire** | 20 % | Prévenir les défaillances par manque de mémoire sous charge |
| **Stockage** | 3 mois au taux de croissance actuel | Délai d'approvisionnement et de provisionnement |
| **Bande passante réseau** | 30 % pendant les heures ouvrées | Absorber les pics de trafic ; accommoder les surcharges de mitigation DDoS |

Lorsque des services exposés vers l'extérieur sont exposés au risque DDoS, des mesures de mitigation supplémentaires (CDN, services de protection DDoS, limitation de débit) sont mises en œuvre en coordination avec la Politique de sécurité des réseaux (A.8.20–22).

---

## Comité de planification de la capacité

Les organisations disposant d'une infrastructure complexe ou à grande échelle (50+ serveurs ou charges de travail cloud équivalentes) devraient mettre en place un Comité de planification de la capacité pour coordonner la gestion de la capacité entre les équipes et assurer l'alignement entre les décisions techniques de capacité et la stratégie d'entreprise.

### Structure du comité

| Rôle | Fonction |
|------|----------|
| **Responsable de l'infrastructure** (président) | Définit l'ordre du jour ; présente les données de capacité et les prévisions |
| **Architecte cloud / Ingénieur de plateforme** | Tendances de capacité cloud, efficacité de la mise à l'échelle automatique, optimisation des coûts |
| **Administrateur de base de données** | Croissance du stockage des bases de données, capacité de performance, capacité de réplication |
| **Propriétaires d'applications** (en rotation) | Projections de croissance de l'activité, lancements planifiés, évolutions de la demande |
| **Délégué du DFin** | Revue budgétaire, approbation des investissements, analyse coût-bénéfice |

### Cadence des réunions

Le Comité de planification de la capacité se réunit trimestriellement. L'ordre du jour comprend :

- Revue des prévisions de capacité et de la précision des prévisions.
- Approbation des extensions de capacité planifiées et des budgets associés.
- Revue des incidents liés à la capacité et des événements quasi-manqués.
- Discussion de l'impact budgétaire et des opportunités d'optimisation des coûts.
- Identification des risques de capacité émergents liés à la croissance de l'activité ou aux évolutions technologiques.

Les comptes rendus des réunions sont conservés comme preuve de gouvernance (Preuve n° 10).

Lorsque l'organisation est trop petite pour justifier un comité formel, la réunion trimestrielle de revue de la capacité entre le Responsable de l'infrastructure et le DSI remplit cette fonction de gouvernance.

---

## Définitions

| Terme | Définition |
|-------|------------|
| **Mise à l'échelle automatique** | Ajustement automatisé des ressources de calcul (instances, conteneurs) en réponse à la demande mesurée, typiquement dans des environnements cloud |
| **Prévision de capacité** | Projection des besoins futurs en ressources basée sur les tendances historiques, les plans de croissance de l'activité et les schémas saisonniers |
| **Marge de capacité** | Capacité inutilisée disponible pour la croissance ou la demande imprévue au-delà de l'utilisation au pic actuel |
| **Seuil de capacité** | Niveau d'utilisation défini qui déclenche des alertes ou des actions lorsqu'il est dépassé (avertissement, critique ou maximum) |
| **Période de refroidissement** | Intervalle minimum entre les actions de mise à l'échelle automatique pour éviter les oscillations rapides entre l'extension et la réduction |
| **DDoS** | Déni de service distribué — attaque qui tente de saturer un service en le submergeant de trafic provenant de sources multiples |
| **Taux de croissance** | Vitesse à laquelle la consommation de ressources augmente dans le temps, généralement mesurée en pourcentage par mois ou en unités absolues par mois |
| **IOPS** | Opérations d'entrée/sortie par seconde — métrique de performance du stockage mesurant le taux d'opérations de lecture et d'écriture |
| **Délestage** | Réduction délibérée de la charge système lors d'une pression sur la capacité en dépriorisant les charges de travail non essentielles ou en limitant les requêtes |
| **Dimensionnement adapté** | Ajustement de l'allocation des ressources pour correspondre à l'utilisation réelle, en éliminant les ressources surprovisionnées ou sous-provisionnées |
| **Réduction** | Diminution du nombre de ressources allouées (instances, conteneurs) lorsque la demande diminue |
| **Extension** | Augmentation du nombre de ressources allouées (instances, conteneurs) lorsque la demande augmente |
| **ONS** | Objectif de niveau de service — cible mesurable pour la performance du service (par exemple disponibilité, latence) que la capacité doit soutenir |
| **Utilisation** | Proportion de la capacité totale d'une ressource actuellement en usage, généralement exprimée en pourcentage |

---

## Rôles et responsabilités

| Rôle | Responsabilités |
|------|-----------------|
| **RSSI** | Propriété de la politique ; assurance de la capacité pour les systèmes de sécurité (SIEM, journalisation, EDR) ; vérification de la conformité pour A.8.6 ; escalade des risques de capacité affectant la posture de sécurité ; révision annuelle de la politique |
| **DSI / Directeur informatique** | Responsabilité globale de l'efficacité du programme de gestion de la capacité ; approbation des plans d'extension de la capacité ; planification stratégique de la capacité ; supervision budgétaire |
| **DFin / Finance** | Approbation des budgets de gestion de la capacité (CapEx et OpEx) ; revue financière des investissements en capacité ; supervision de l'optimisation des coûts |
| **Responsable de l'infrastructure / Responsable des opérations informatiques** | Supervision quotidienne de la capacité et réponse aux alertes ; configuration et ajustement des seuils ; prévision de la capacité ; rapports ; mitigation d'urgence de la capacité |
| **Architecte cloud / Ingénieur de plateforme** | Conception et mise en œuvre des politiques de mise à l'échelle automatique ; gestion des quotas cloud ; optimisation des coûts pour les ressources cloud ; planification des instances réservées |
| **Propriétaires d'applications / Propriétaires de systèmes** | Projections de croissance de l'activité pour la planification de la capacité ; participation aux réunions de revue de la capacité ; budget pour la capacité spécifique aux applications |
| **Responsable de la sécurité de l'information** | Maintenance de la politique ; revue des exceptions ; rapport de conformité ; coordination des audits ; suivi des non-conformités |
| **Ensemble du personnel** | Signalement des problèmes de performance observés ; respect des politiques d'utilisation des ressources approuvées |

---

## Preuves

Les éléments de preuve suivants démontrent la conformité à la présente politique :

| # | Preuve | Responsable | Fréquence | Conservation |
|---|--------|-------------|-----------|--------------|
| 1 | **Rapport de couverture de supervision** indiquant le pourcentage de systèmes de production et hors production supervisés | Responsable de l'infrastructure | Mensuel | 3 ans |
| 2 | **Documentation de configuration des seuils** pour toutes les ressources supervisées | Responsable de l'infrastructure | Révisé trimestriellement ; mis à jour si nécessaire | Actuel + 2 ans |
| 3 | **Historique des alertes et enregistrements de réponse** (alertes déclenchées, accusées de réception, résolues, délais de réponse) | Opérations informatiques | Continu | 3 ans |
| 4 | **Rapports mensuels de capacité** avec résumés d'utilisation et données de tendance | Responsable de l'infrastructure | Mensuel | 3 ans |
| 5 | **Prévisions trimestrielles de capacité** avec mesures de précision (réel par rapport au prévu) | Responsable de l'infrastructure | Trimestriel | 3 ans |
| 6 | **Plan annuel de capacité** avec projections stratégiques et besoins en investissements | DSI / Responsable de l'infrastructure | Annuel | 5 ans |
| 7 | **Enregistrements de configuration de mise à l'échelle automatique** et historique des changements | Architecte cloud / Ingénieur de plateforme | Maintenu en continu ; révisé trimestriellement | Durée de vie de la configuration + 1 an |
| 8 | **Enregistrements des incidents liés à la capacité** et rapports de revue post-incident | Opérations informatiques / Responsable de l'infrastructure | Par incident | 3 ans |
| 9 | **Rapports d'inventaire et d'utilisation des licences** indiquant les droits par rapport aux allocations actives | Opérations informatiques / Achats | Trimestriel | 3 ans |
| 10 | **Comptes rendus des réunions du Comité de planification de la capacité** ou notes de réunion de revue de la capacité | Responsable de l'infrastructure | Par réunion | 3 ans |
| 11 | **Registre des exceptions** pour les dérogations à la politique de capacité avec approbations et contrôles compensatoires | Responsable de la sécurité de l'information | Maintenu en continu ; révisé trimestriellement | Durée de l'exception + 3 ans |
| 12 | **Rapports de tendance de croissance du stockage** (incluant journaux, bases de données et stockage de sauvegardes) | Responsable de l'infrastructure | Mensuel | 3 ans |
| 13 | **Rapports d'optimisation des coûts** documentant les actions de dimensionnement adapté, les décisions de capacité réservée et les économies réalisées | Responsable de l'infrastructure / Architecte cloud | Trimestriel | 3 ans |

---

# Conformité à la politique

## Mesure de la conformité

L'équipe de gestion de la sécurité de l'information vérifie la conformité à la présente politique par des audits de couverture de supervision, des revues de configuration des seuils, des évaluations de la précision des prévisions, la ponctualité des rapports de capacité, des audits internes et externes, et des retours au propriétaire de la politique.

**Métriques de conformité** :

| Métrique | Cible | Fréquence de mesure |
|----------|-------|---------------------|
| Systèmes de production avec supervision de la capacité activée | 100 % | Mensuel |
| Systèmes hors production avec supervision de la capacité activée | >= 90 % | Trimestriel |
| Ressources avec seuils définis et documentés | >= 95 % | Trimestriel |
| Alertes d'avertissement accusées de réception dans les 4 heures (heures ouvrées) | >= 90 % | Mensuel |
| Alertes critiques accusées de réception dans les 30 minutes | >= 95 % | Mensuel |
| Précision des prévisions de capacité (dans un écart de +/-15 %) | >= 80 % des prévisions | Trimestriel |
| Rapports mensuels de capacité livrés dans les délais | 100 % | Mensuel |
| Interruptions de service liées à la capacité par trimestre | < 2 | Trimestriel |

**Notation de la conformité** :

| Composant | Pondération | Calcul |
|-----------|-------------|--------|
| Couverture de la supervision | 30 % | (Systèmes de production supervisés / Total systèmes de production) × 100 |
| Seuils et alertes | 25 % | (Ressources avec seuils conformes + alertes traitées dans les délais) / Total × 100 |
| Prévisions et planification | 25 % | (Prévisions précises + prévisions livrées dans les délais) / Total prévisions × 100 |
| Rapports et gouvernance | 20 % | (Rapports livrés dans les délais + revues complétées) / Total requis × 100 |

**Traitement des non-conformités** : En dessous de 70 %, une escalade immédiate au DSI et au RSSI avec un plan de remédiation dans les 10 jours ouvrés est requise. Entre 70 et 89 %, la supervision du Responsable de l'infrastructure avec des revues mensuelles d'amélioration est requise. À 90 % et au-delà, la supervision trimestrielle standard s'applique.

**Responsabilité de remédiation par composant** :

| Composant | En dessous de la cible | Responsable de la remédiation | Escalade |
|-----------|------------------------|-------------------------------|----------|
| Couverture de la supervision | <100 % production | Responsable de l'infrastructure | DSI à 30 jours de retard |
| Seuils et alertes | <95 % | Opérations informatiques / Responsable de l'infrastructure | RSSI à 15 jours de retard |
| Prévisions et planification | <80 % de précision | Responsable de l'infrastructure | DSI lors de la revue trimestrielle |
| Rapports et gouvernance | <100 % dans les délais | Responsable de l'infrastructure | DSI à 15 jours de retard |

## Exceptions

Toute exception à la présente politique est approuvée et enregistrée par le Responsable de la sécurité de l'information au préalable, avec acceptation des risques documentée, contrôles compensatoires et date de révision définie (maximum 12 mois). Les exceptions pour les systèmes de production critiques requièrent l'approbation conjointe du DSI et du RSSI. Toutes les exceptions actives sont révisées trimestriellement et communiquées à l'équipe de revue de direction.

## Non-conformité

Tout employé reconnu coupable d'avoir enfreint la présente politique peut faire l'objet de mesures disciplinaires pouvant aller jusqu'au licenciement. Les violations de la politique sont documentées, font l'objet d'une enquête par le Responsable de la sécurité de l'information et sont signalées au RSSI. Les incidents liés à la capacité causés par une non-conformité à la politique (par exemple absence de supervision, absence de réaction aux alertes) sont traités comme des facteurs contributifs lors des analyses post-mortem des incidents.

## Amélioration continue

La présente politique est révisée et mise à jour dans le cadre du processus d'amélioration continue. Les révisions prennent en compte les évolutions des plateformes d'infrastructure et des services cloud, les tendances des incidents liés à la capacité et l'analyse des quasi-incidents, les améliorations des outils de supervision et de prévision, les évolutions réglementaires affectant les exigences de disponibilité, les opportunités d'optimisation des coûts et les enseignements tirés des événements d'épuisement de la capacité.

---

# Domaines de la norme ISO 27001 couverts

Politique de gestion de la capacité — Correspondance des contrôles ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership et engagement | 5.1 Politiques de sécurité de l'information |
| Clause 5.2 Politique | 5.4 Responsabilités de la direction |
| Clause 6.2 Objectifs de sécurité de l'information | 5.36 Conformité aux politiques, règles et normes |
| Clause 9.1 Surveillance, mesure, analyse et évaluation | 5.37 Procédures d'exploitation documentées |
| Clause 9.3 Revue de direction | 6.3 Sensibilisation, éducation et formation à la sécurité de l'information |
| | **8.6 Gestion de la capacité** |
| | 8.13 Sauvegarde de l'information |
| | 8.14 Redondance des installations de traitement de l'information |
| | 8.16 Activités de surveillance |

**Cadre réglementaire et juridique** :

| Cadre | Pertinence |
|-------|-----------|
| nLPD suisse (revDSG) | Art. 8 — Mesures techniques et organisationnelles ; la gestion de la capacité assure la disponibilité des systèmes traitant des données personnelles |
| DSV suisse (Ordonnance sur la protection des données) | Art. 1–3 — Les exigences minimales de sécurité des données incluent la disponibilité des systèmes |
| RGPD (le cas échéant) | Art. 32(1)(b) — Capacité à assurer la disponibilité et la résilience continues des systèmes et services de traitement |
| ISO/IEC 27001:2022 | Contrôle Annexe A 8.6 — Gestion de la capacité |
| ISO/IEC 27002:2022 | Section 8.6 — Recommandations de mise en œuvre pour la gestion de la capacité |
| NIST SP 800-53 Rév. 5 | AU-4 (Capacité de stockage des journaux d'audit), CP-2(2) (Planification de la capacité), SC-5 (Protection contre les dénis de service) |
| NIST CSF 2.0 | PR.IR-01 (Les réseaux et environnements sont protégés contre les accès logiques non autorisés), DE.CM (Supervision continue) |
| CIS Controls v8 | Contrôle 8 (Gestion des journaux d'audit — capacité de stockage), Contrôle 13 (Supervision et défense du réseau) |
| ITIL 4 | Pratique de gestion de la capacité et des performances |
| FINMA (le cas échéant) | Circulaire 2023/1 — La résilience opérationnelle des TIC inclut la gestion de la capacité |
| DORA (le cas échéant) | Art. 11 — Planification de la capacité des TIC pour la résilience opérationnelle numérique |
| NIS2 (le cas échéant) | Art. 21(2) — La continuité d'activité inclut la gestion de la capacité |

---

<!-- QA_VERIFIED: 2026-03-29 -->
