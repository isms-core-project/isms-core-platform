<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.8.16-FR:operational:OP-POL:a.8.16 -->
**ISMS-OP-POL-A.8.16 — Activités de surveillance**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Activités de surveillance |
| **Type de document** | Politique opérationnelle |
| **Identifiant du document** | ISMS-OP-POL-A.8.16 |
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

- ISO/IEC 27001:2022 Contrôle A.8.16 — Activités de surveillance

**Contrôles Annexe A associés** :

| Contrôle | Relation avec les activités de surveillance |
|----------|---------------------------------------------|
| A.5.7 Renseignement sur les menaces | Le renseignement sur les menaces informe les règles de surveillance et les schémas de détection |
| A.5.24–28 Gestion des incidents | La surveillance déclenche la détection et l'escalade des incidents |
| A.5.28 Collecte de preuves | Les données de surveillance servent de preuves légales |
| A.5.34 Protection de la vie privée et des données à caractère personnel | La surveillance des employés doit respecter les exigences de protection de la vie privée |
| A.8.7 Protection contre les logiciels malveillants | Les événements de détection de logiciels malveillants alimentent la surveillance |
| A.8.15 Journalisation | Les journaux fournissent les données brutes analysées par la surveillance |
| A.8.17 Synchronisation des horloges | Des horodatages précis sont essentiels pour la corrélation des événements |
| A.8.20 Sécurité des réseaux | Le trafic réseau constitue une source de données de surveillance principale |

**Politiques internes associées** :

- Politique de journalisation (A.8.15)
- Politique de gestion des incidents
- Politique de sécurité des réseaux
- Politique de sécurité des terminaux
- Politique de contrôle d'accès
- Politique de protection de la vie privée et des données à caractère personnel

---

# Politique des activités de surveillance

## Finalité

La présente politique a pour objet de définir les exigences relatives à la surveillance active des réseaux, systèmes et applications pour détecter les comportements anormaux, les menaces sécuritaires et les violations de politique. Là où la journalisation (A.8.15) capture et préserve les événements, la surveillance analyse ces événements en temps réel ou quasi-réel pour identifier et répondre aux menaces avant qu'elles causent des préjudices.

La présente politique soutient la nLPD (revLPD) suisse art. 8 en mettant en œuvre la surveillance comme mesure technique et organisationnelle appropriée au risque. Les activités de surveillance doivent être conformes au droit suisse du travail (CO art. 328/328b) et à l'interdiction de la surveillance des comportements (OLT 3 art. 26). Lorsque l'organisation traite des données de personnes dans l'UE/EEE, les exigences du RGPD art. 32 s'appliquent également.

## Champ d'application

La présente politique s'applique à :

- Tous les réseaux, systèmes, applications et services cloud dans le périmètre ISMS.
- Toutes les technologies de surveillance : SIEM, EDR/XDR, NDR, IDS/IPS, UEBA et outils équivalents.
- Tous les employés et utilisateurs tiers dont les activités génèrent des événements pertinents pour la sécurité.
- Tous les environnements : production, staging et systèmes accessibles depuis l'extérieur.

La surveillance des systèmes de sécurité physique (vidéosurveillance, lecteurs de badges) est couverte par la Politique de contrôle d'accès physique. La configuration de la journalisation et la conservation des journaux sont couvertes par la Politique de journalisation (A.8.15).

## Principe

La surveillance est un contrôle actif de détection. Les réseaux, systèmes et applications doivent être surveillés pour détecter les comportements anormaux, et des actions appropriées doivent être prises pour évaluer les incidents potentiels de sécurité de l'information. La surveillance doit opérer sur la base de références comportementales établies, de règles de détection définies et de renseignements sur les menaces — et non d'une surveillance indiscriminée.

---

## Quoi surveiller

### Périmètre de surveillance

Les éléments suivants doivent être surveillés pour détecter les comportements anormaux et les événements de sécurité :

| # | Domaine de surveillance | Ce qu'il faut surveiller |
|---|------------------------|--------------------------|
| 1 | **Trafic réseau** | Flux de trafic entrant et sortant, trafic est-ouest (latéral) entre segments, connexions vers des IP/domaines malveillants connus |
| 2 | **Authentification et accès** | Tentatives de connexion échouées, déplacement impossible, schémas de bourrage d'identifiants, accès depuis des emplacements ou appareils inattendus |
| 3 | **Activité à privilèges** | Actions administratives, escalades de privilèges, utilisation de comptes de service, accès à privilèges en dehors des heures de travail |
| 4 | **Comportement des terminaux** | Anomalies d'exécution de processus, binaires non signés, exécution de scripts, mécanismes de persistance, injection en mémoire |
| 5 | **Activité applicative** | Volumes de transactions inhabituels, opérations en masse sur les données, schémas d'abus d'API, pics d'erreurs applicatives |
| 6 | **Modifications de configuration** | Modifications des paramètres de sécurité, règles de pare-feu, politiques de groupe, enregistrements DNS, configurations de certificats |
| 7 | **État des outils de sécurité** | Désactivation d'antivirus/EDR, modifications des règles de pare-feu, interruptions du service de journalisation, tentatives de contournement d'IDS/IPS |
| 8 | **Services cloud** | Accès aux consoles d'administration, modifications de configuration des locataires, appels API excessifs, opérations d'export de données |
| 9 | **Mouvements de données** | Transferts de fichiers volumineux, téléchargements en masse, utilisation de périphériques USB, envois vers le stockage cloud, pièces jointes de courriel dépassant les seuils |
| 10 | **Utilisation des ressources** | Anomalies de CPU/mémoire/disque/bande passante pouvant indiquer du cryptominage, une participation à des botnets DDoS ou une compromission système |

### Priorité des systèmes critiques

Les systèmes doivent être priorisés pour la surveillance selon le risque :

| Priorité | Type de système | Niveau de surveillance |
|----------|----------------|----------------------|
| **Critique** | Infrastructure d'authentification, pare-feux, VPN, contrôleurs de domaine, systèmes de paiement | Temps réel avec alertes automatiques |
| **Élevé** | Serveurs hébergeant des données confidentielles/personnelles, passerelles de courriel, consoles d'administration cloud | Temps réel ou quasi-réel (dans les 15 minutes) |
| **Moyen** | Serveurs d'applications internes, infrastructure de développement, partages de fichiers internes | Quasi-réel (dans l'heure) |
| **Standard** | Postes de travail, imprimantes, infrastructure non critique | Révision périodique (agrégation quotidienne ou hebdomadaire) |

---

## Références comportementales

### Établissement des références

Avant que la détection des anomalies soit efficace, l'organisation doit établir des références de comportement normal. Les références initiales doivent être établies dans les 30 jours suivant le déploiement de la surveillance pour chaque système ou groupe de systèmes. Pendant la période d'établissement des références, la surveillance doit fonctionner en « mode apprentissage » — les alertes sont générées mais révisées avec une tolérance accrue pour les faux positifs jusqu'à ce que les références soient validées.

Les références doivent documenter :

- L'utilisation du système pendant les périodes d'exploitation standard et de pointe.
- Les schémas d'accès typiques : timing, emplacement, fréquence et volume par groupe d'utilisateurs.
- Les flux de trafic réseau attendus : paires source-destination, protocoles, volumes de données.
- Les taux de transactions applicatives standard et les niveaux d'erreurs.

Les références doivent être révisées et mises à jour :

- **Trimestriellement** pour les systèmes généraux.
- **Après des changements significatifs** (nouveaux systèmes, réorganisations, migrations cloud, cycles métier saisonniers).
- **Suite à des incidents** où l'incident a révélé une lacune dans la définition de la référence.

### Détection des écarts

Les systèmes de surveillance doivent être configurés pour détecter les écarts par rapport aux références établies, notamment :

- Trafic depuis ou vers des sources malveillantes connues (serveurs C2, infrastructure de botnet, IP/domaines signalés par le renseignement sur les menaces).
- Signatures et schémas d'attaques reconnus (force brute, DDoS, dépassement de tampon, injection SQL, bourrage d'identifiants).
- Comportement système inhabituel : terminaisons de processus inattendues, exécution de processus non autorisés, indicateurs de journalisation de frappes, déviations de protocole.
- Anomalies de comportement utilisateur : accès en dehors des heures de travail normales, accès à des ressources jamais accédées auparavant, déplacement impossible entre emplacements géographiques. Le **déplacement impossible** est défini comme des événements d'authentification depuis deux emplacements géographiques dans un laps de temps rendant le déplacement physique entre eux implausible (p. ex. connexions depuis Zurich et Tokyo en 2 heures). L'organisation doit définir les paramètres de déplacement impossible selon : la vitesse de déplacement maximale plausible, les exclusions VPN/proxy pour les points de sortie d'entreprise connus, et la tolérance pour l'imprécision de localisation des appareils mobiles.
- Anomalies de performance réseau : latence inattendue, saturation de la bande passante, volumes inhabituels de requêtes DNS.
- Anomalies de consommation de ressources : pics de CPU, E/S disque inattendues, épuisement de la mémoire sans charge de travail correspondante.

---

## Architecture de surveillance

### Plateforme de surveillance

L'organisation doit déployer une plateforme de surveillance centralisée capable de :

| Capacité | Exigence |
|----------|---------|
| **Corrélation d'événements** | Corréler les événements de plusieurs sources (journaux, réseau, terminal, cloud, identité) dans une vue unifiée |
| **Alertes automatiques** | Générer des alertes basées sur des règles prédéfinies, des seuils et la détection d'anomalies |
| **Intégration du renseignement sur les menaces** | Ingérer des flux de renseignement externes sur les menaces pour enrichir les règles de détection et identifier les indicateurs de compromission connus |
| **Tableaux de bord** | Fournir une visibilité en temps réel sur la posture de sécurité, les volumes d'alertes et les tendances |
| **Support d'investigation** | Permettre l'exploration depuis l'alerte jusqu'aux événements bruts pour l'investigation des incidents |
| **Conservation** | Conserver les données de surveillance conformément au calendrier de conservation de la Politique de journalisation (A.8.15) |

Exemples de plateformes : SIEM (p. ex. Microsoft Sentinel, Splunk, Elastic SIEM, Wazuh), XDR ou équivalent.

### Couches de détection

Une approche de surveillance en couches doit être mise en œuvre :

| Couche | Technologie | Couverture |
|--------|------------|-----------|
| **Réseau** | NDR, IDS/IPS, journaux de pare-feu, surveillance DNS | Visibilité du trafic nord-sud et est-ouest |
| **Terminal** | Agents EDR/XDR sur tous les appareils gérés | Exécution de processus, opérations sur les fichiers, analyse de la mémoire |
| **Identité** | Surveillance du fournisseur d'identité, UEBA | Anomalies d'authentification, mauvaise utilisation des identifiants, indicateurs de menace interne |
| **Application** | Journaux applicatifs transmis au SIEM, WAF | Anomalies de transactions, échecs de validation des entrées, abus d'API |
| **Cloud** | Surveillance native cloud (p. ex. AWS CloudTrail, Azure Monitor, GCP Cloud Audit Logs) | Actions administratives, modifications de configuration, accès aux données |

Lorsque l'organisation ne dispose pas des ressources pour un Centre opérationnel de sécurité (SOC) interne complet, un service de Détection et réponse gérées (MDR) devrait être envisagé pour assurer une couverture de surveillance 24h/7j.

### Surveillance spécifique au cloud

Pour les environnements cloud (IaaS, PaaS, SaaS), des exigences de surveillance supplémentaires s'appliquent :

- Les **journaux d'audit cloud** (AWS CloudTrail, Azure Activity Log, GCP Cloud Audit Logs) doivent être transmis à la plateforme de surveillance centralisée.
- Les modifications de la **posture de sécurité cloud** (p. ex. création d'un compartiment S3 public, modification d'un groupe de sécurité, modifications de politique IAM) doivent générer des alertes immédiates.
- Les services de **détection des menaces natifs cloud** (AWS GuardDuty, Azure Defender, GCP Security Command Center) devraient être activés et intégrés avec la plateforme de surveillance centralisée.
- Les **actions administratives SaaS** (portail d'administration M365, administration Google Workspace, modifications de configuration Salesforce) doivent être surveillées pour détecter les modifications de configuration non autorisées.
- L'**activité des API cloud** doit être surveillée pour détecter les volumes inhabituels, les accès depuis des emplacements inattendus et l'utilisation de points de terminaison API obsolètes ou à risque élevé.

### Santé du système de surveillance (SOC 2 : CC4.1)

L'infrastructure de surveillance elle-même doit être surveillée pour assurer une disponibilité continue :

- **Ingestion de données** : Alerter si l'ingestion de la source de journaux s'arrête ou tombe en dessous du volume de référence pendant plus de 15 minutes.
- **Santé des agents** : Surveiller l'état des agents EDR/surveillance sur tous les terminaux ; alerter en cas de déconnexion d'agent dépassant 1 heure.
- **Capacité de stockage** : Alerter à 80 % d'utilisation du stockage avec une planification de capacité pour une croissance minimum de 30 jours.
- **Disponibilité de la plateforme** : Cible de 99,9 % de disponibilité pour la plateforme de surveillance ; basculement ou redondance pour les composants critiques.
- **Rapport de santé mensuel** : Les Opérations IT doivent produire un rapport mensuel de santé de la plateforme de surveillance couvrant la disponibilité, les taux d'ingestion, la couverture des agents et les projections de capacité.

### Guide de mise en œuvre par phases

Les organisations déployant des capacités de surveillance pour la première fois ou étendant leur périmètre devraient suivre une approche par phases :

| Phase | Durée | Périmètre | Objectif |
|-------|-------|-----------|----------|
| **Phase 1 — Foundation** | Mois 1-3 | Journaux d'authentification, journaux de pare-feu, événements de protection des terminaux transmis au SIEM | Détection de base des menaces ; capacité de corrélation des journaux |
| **Phase 2 — Extension** | Mois 4-6 | Ajout de la surveillance du trafic réseau, des journaux d'audit cloud, des journaux applicatifs | Visibilité plus large ; établissement des références pour les systèmes supplémentaires |
| **Phase 3 — Maturation** | Mois 7-12 | UEBA, playbooks de réponse automatisée, cartographie de couverture MITRE ATT&CK, analyses avancées | Chasse aux menaces proactive ; réduction du DMTD |
| **Phase 4 — Optimisation** | En cours | Ajustement continu, enrichissement du renseignement sur les menaces, exercices équipe rouge/violette pour valider la détection | Efficacité durable ; réduction des faux positifs |

---

## Gestion des alertes

### Classification des alertes

Les alertes doivent être classifiées par gravité pour définir les délais de réponse :

| Gravité | Description | Délai de réponse | Exemples |
|---------|-------------|-----------------|---------|
| **Critique** | Compromission active ou menace imminente | **15 minutes** (heures ouvrables), **1 heure** (hors heures) | Exécution confirmée de logiciels malveillants, exfiltration active de données, indicateurs de rançongiciel |
| **Élevé** | Événement de sécurité probable nécessitant une investigation | **1 heure** (heures ouvrables), **4 heures** (hors heures) | Multiples échecs d'authentification depuis une source unique, désactivation des contrôles de sécurité, téléchargement en masse de données |
| **Moyen** | Activité suspecte nécessitant une analyse | **4 heures** (heures ouvrables), **prochain jour ouvrable** (hors heures) | Seul échec de connexion depuis un emplacement inhabituel, violation mineure de politique, modification de configuration inattendue |
| **Faible** | Informatif ou anomalie mineure | **Prochain jour ouvrable** | Scan de ports depuis une IP externe, requête web bloquée vers une catégorie suspecte, léger dépassement de seuil |

### Processus de triage des alertes

**Modèle de personnel pour la réponse aux alertes** : L'organisation doit définir son approche de personnel pour la réponse aux alertes :

| Modèle | Couverture | Adapté à |
|--------|-----------|---------|
| **SOC interne** | Analystes de sécurité dédiés pendant les heures ouvrables ; rotation d'astreinte pour après les heures | Organisations avec ≥ 3 personnel de sécurité ; environnements à risque élevé |
| **Détection et réponse gérées (MDR)** | Surveillance 24h/7j par un prestataire externe ; escalade vers l'équipe interne pour les événements confirmés | Organisations avec personnel de sécurité limité ; couverture 24h/7j rentable |
| **Hybride** | MDR pour le triage 24h/7j en première ligne ; équipe interne pour l'investigation et la réponse | Approche équilibrée ; la plus courante pour les PME |
| **Rotation d'astreinte** | Surveillance pendant les heures ouvrables avec astreinte hors heures pour les alertes Critiques/Élevées uniquement | Approche minimale viable pour les petites équipes ; nécessite des alertes bien ajustées |

Le modèle choisi doit être documenté et approuvé par le RSSI. La capacité de réponse hors heures doit être testée trimestriellement.

Lorsqu'une alerte est générée :

1. **Réception** : Alerte reçue par l'analyste de sécurité de l'information (ou le prestataire MDR).
2. **Triage** : L'analyste évalue si l'alerte est un vrai positif, un faux positif ou nécessite une investigation complémentaire.
3. **Enrichissement** : Collecter du contexte supplémentaire — criticité de l'actif, profil de l'utilisateur, renseignement sur les menaces, événements connexes.
4. **Décision** : Si vrai positif ou événement de sécurité probable, créer un enregistrement d'incident conformément à la Politique de gestion des incidents.
5. **Escalade** : Les incidents de gravité Critique et Élevée sont escaladés au RSSI immédiatement. Les incidents Moyens sont escaladés s'ils ne sont pas résolus dans les délais définis.
6. **Documentation** : Toutes les décisions de triage documentées — y compris les faux positifs avec justification.

### Ajustement des alertes

Pour maintenir l'efficacité de la surveillance et minimiser la fatigue des alertes :

- Les règles de détection doivent être révisées et ajustées **mensuellement** pour réduire les taux de faux positifs.
- Les règles de suppression doivent être documentées avec justification et révisées **trimestriellement**.
- De nouvelles règles de détection doivent être ajoutées lorsque : le renseignement sur les menaces identifie de nouveaux schémas d'attaque, les incidents révèlent des lacunes de détection, ou de nouveaux systèmes/applications sont déployés.
- **Contrôle des changements de règles de détection** : Tous les changements aux règles de détection (nouvelles règles, modifications, suppressions, suppressions) doivent suivre un processus documenté : demande de changement avec justification, révision par les pairs par un second analyste, test dans un environnement non-production/staging si possible, approbation par le responsable de la sécurité de l'information, et déploiement avec capacité de retour arrière. Les changements de règles d'urgence (p. ex. en réponse à une menace active) peuvent contourner la révision par les pairs mais doivent être révisés rétrospectivement dans les 48 heures.
- Les volumes d'alertes et les taux de faux positifs doivent être suivis comme indicateurs clés de performance.
- Cible : taux de faux positifs inférieur à **20 %** pour les alertes de haute gravité.
- **Processus de gestion des faux positifs** : Lorsqu'un faux positif est identifié, l'analyste doit : (a) documenter la cause profonde (règle mal configurée, processus métier légitime, bruit environnemental), (b) déterminer l'action appropriée (affiner la règle, ajouter une exception, supprimer avec expiration, accepter), (c) mettre en œuvre le changement via le processus de contrôle des changements de règles de détection, et (d) vérifier que l'ajustement ne supprime pas les vrais positifs. Les sources de faux positifs persistants (> 10 occurrences par semaine pour la même règle) doivent être priorisées pour ajustement dans les 5 jours ouvrables.

---

## Calendrier de révision de la surveillance

| Type de révision | Fréquence | Responsable | Périmètre |
|-----------------|-----------|-------------|-----------|
| **Alertes en temps réel** | Continu | Sécurité de l'information / MDR | Les événements Critique et Élevé déclenchent une notification immédiate |
| **Révision de la file d'alertes** | Quotidien | Analyste de sécurité de l'information | Triage des alertes en attente ; fermeture des faux positifs ; escalade des événements confirmés |
| **Révision des règles de détection** | Mensuel | Sécurité de l'information | Affiner les règles ; ajouter de nouvelles détections ; supprimer les faux positifs validés |
| **Audit de couverture de la surveillance** | Trimestriel | Opérations IT / Sécurité de l'information | Vérifier que tous les systèmes dans le périmètre sont surveillés ; identifier les lacunes ; intégrer les nouveaux systèmes |
| **Révision des références** | Trimestriel | Sécurité de l'information | Mettre à jour les références comportementales pour les changements de systèmes, d'utilisateurs ou d'opérations métier |
| **Révision de l'efficacité** | Semestriel | RSSI | Réviser les indicateurs DMTD et DMTR ; évaluer la couverture de détection par rapport à MITRE ATT&CK ; rapporter à la direction. **Livrables** : rapport d'efficacité écrit incluant : analyse des lacunes de couverture, carte thermique de couverture des techniques MITRE ATT&CK (pourcentage des techniques pertinentes avec des règles de détection actives), analyse de tendances des DMTD/DMTR/taux de faux positifs, et améliorations recommandées pour la prochaine période |

---

## Indicateurs clés de performance

Les indicateurs suivants doivent être suivis pour mesurer l'efficacité de la surveillance :

| # | Indicateur | Cible | Reporting |
|---|-----------|-------|-----------|
| 1 | **Délai moyen de détection (DMTD)** | Événements critiques détectés dans les 15 minutes suivant leur occurrence | Mensuel au RSSI |
| 2 | **Délai moyen de réponse (DMTR)** | Alertes critiques triées dans le délai SLA de réponse | Mensuel au RSSI |
| 3 | **Couverture de la surveillance** | 100 % des systèmes critiques, ≥ 95 % de tous les systèmes dans le périmètre. Couverture = (systèmes avec agent de surveillance actif + systèmes avec transmission de journaux au SIEM) / total des systèmes dans le périmètre de l'inventaire des actifs. Les systèmes marqués hors périmètre nécessitent une justification documentée. | Trimestriel |
| 4 | **Taux de faux positifs** | < 20 % pour les alertes de haute gravité | Mensuel |
| 5 | **Actualité des règles de détection** | Toutes les règles révisées dans les 90 derniers jours | Trimestriel |
| 6 | **Arriéré d'alertes** | Critique : pas d'alertes non triées de plus d'1 heure ; Élevé : 4 heures ; Moyen : 24 heures ; Faible : 48 heures | Hebdomadaire |

---

## Vie privée des employés et surveillance

### Exigences légales

Les activités de surveillance doivent être conformes au droit suisse du travail :

- **OLT 3 art. 26** : Les systèmes de surveillance ou de contrôle dont le seul ou principal objectif est de surveiller le comportement des employés sont interdits.
- **CO art. 328b** : Le traitement des données des employés doit être proportionnel et limité à ce qui est nécessaire pour la relation d'emploi ou pour vérifier l'aptitude de l'employé.
- **nLPD** : Le traitement des données des employés par la surveillance exige la licéité, la proportionnalité, la limitation de la finalité et la transparence.

### Mesures de protection de la vie privée

Les mesures de protection suivantes doivent être appliquées :

- La surveillance doit servir des **objectifs de sécurité légitimes** (détection des menaces, investigation des incidents, vérification de la conformité) — et non la surveillance comportementale ou la gestion des performances.
- Les employés doivent être **informés à l'avance** que la surveillance est en place, ce qui est surveillé et pourquoi, via la politique d'utilisation acceptable et la documentation de l'emploi.
- Seules les **données strictement nécessaires** doivent être collectées et conservées (minimisation des données).
- Les données de surveillance ne doivent **pas être utilisées** pour l'évaluation des performances RH, les mesures disciplinaires pour des raisons non sécuritaires, ou le profilage comportemental général.
- L'**analyse personnalisée** (identification des utilisateurs individuels) ne doit intervenir que lorsque : (a) une alerte indique un incident de sécurité potentiel ou une violation de politique, et (b) l'investigation est documentée avec justification.
- Lorsque les données de surveillance sont partagées avec des parties externes (p. ex. prestataires MDR, enquêteurs légaux), les identifiants personnels doivent être minimisés ou anonymisés dans la mesure du possible.
- Une Analyse d'impact relative à la protection des données (AIPD) selon la nLPD art. 22 doit être conduite avant le déploiement de toute surveillance répondant à l'un des critères suivants :
  - Surveillance de toute l'activité réseau des employés (capture complète des paquets, journalisation des URL).
  - Déploiement d'une Analyse comportementale des utilisateurs et des entités (UEBA) profilant les employés individuels.
  - Surveillance capturant les données de localisation des employés (géolocalisation des connexions VPN, positionnement WiFi).
  - Surveillance de l'activité des appareils personnels dans le cadre de BYOD.
  - Toute activité de surveillance pour laquelle le DPD ou le Conseiller à la protection des données détermine que le traitement est susceptible d'entraîner un risque élevé pour les droits de la personnalité des employés.

---

## Rôles et responsabilités

| Rôle | Responsabilités |
|------|----------------|
| **RSSI** | Propriétaire de la politique ; approbation du périmètre de surveillance et des priorités de détection ; point d'escalade pour les alertes critiques ; révision semestrielle de l'efficacité |
| **Analyste de sécurité de l'information** | Triage quotidien des alertes ; escalade des incidents ; maintenance des règles de détection ; gestion des faux positifs ; ajustement mensuel |
| **Opérations IT / Équipe plateforme** | Administration de la plateforme de surveillance ; déploiement des agents ; intégration des sources de journaux ; gestion de la capacité ; surveillance de la santé des systèmes |
| **Administrateurs système** | S'assurer que les agents de surveillance sont installés et opérationnels sur les systèmes gérés ; signaler les pannes ou lacunes de surveillance |
| **Prestataire MDR** (le cas échéant) | Surveillance des alertes 24h/7j ; triage initial et enrichissement ; escalade des événements confirmés selon les runbooks convenus |
| **Conseiller à la protection des données** | Orientation sur l'impact des activités de surveillance sur la vie privée ; exigences d'AIPD ; exigences de notification des employés |

---

## Preuves

Les preuves suivantes démontrent la conformité à la présente politique :

| # | Preuve | Responsable | Fréquence |
|---|--------|-------------|-----------|
| 1 | **Configuration de la plateforme de surveillance** et inventaire des systèmes (sources de données, règles de détection, routage des alertes) | Opérations IT | *Configuration documentée ; inventaire des sources de données révisé trimestriellement* |
| 2 | **Indicateur de couverture de la surveillance** (pourcentage des systèmes dans le périmètre avec surveillance active) | Opérations IT / Sécurité de l'information | *Trimestriel ; cible : 100 % critique, ≥ 95 % tous dans le périmètre* |
| 3 | **Documentation des références comportementales** pour les systèmes critiques et les groupes d'utilisateurs | Sécurité de l'information | *Documentée ; révisée trimestriellement et après des changements significatifs* |
| 4 | **Relevés de triage des alertes** montrant la classification, la décision de triage et le délai de réponse | Sécurité de l'information | *Conservés 12 mois ; échantillonnés lors des audits* |
| 5 | **Journal des changements de règles de détection** (nouvelles règles, règles ajustées, règles supprimées avec justification) | Sécurité de l'information | *Mensuel ; journal conservé 12 mois* |
| 6 | **Indicateurs DMTD et DMTR** reportés à la direction | RSSI | *Mensuel au RSSI ; semestriel lors de la revue de direction* |
| 7 | **Taux de faux positifs** et tendances de volume d'alertes | Sécurité de l'information | *Mensuel ; cible < 20 % de taux de faux positifs pour la haute gravité* |
| 8 | **Relevés de notification des employés** (politique d'utilisation acceptable, avis de confidentialité concernant la surveillance) | RH / Sécurité de l'information | *Mis à jour par changement de politique ; reconnaissance suivie annuellement* |
| 9 | **Relevés d'AIPD** (si une surveillance à grande échelle est mise en œuvre) | Conseiller à la protection des données | *Réalisée avant le déploiement ; révisée annuellement* |
| 10 | **Relevés de santé de la plateforme de surveillance** — disponibilité, taux d'ingestion de données, santé des agents, capacité de stockage (SOC 2 : CC4.1) | Opérations IT | *Surveillance continue ; rapport résumé mensuel* |
| 11 | **Relevés d'escalade** — utilisation du chemin d'escalade documenté, ponctualité de l'escalade, résultats de résolution | Sécurité de l'information | *Par escalade ; révisé mensuellement* |
| 12 | **Cartographie de couverture MITRE ATT&CK** — techniques couvertes par les règles de détection, lacunes identifiées, plans de remédiation | Sécurité de l'information | *Semestriel* |

---

# Conformité à la politique

## Mesure de la conformité

L'équipe de management de la sécurité de l'information vérifiera la conformité à la présente politique par des audits de couverture de la surveillance, des révisions de réponse aux alertes, le suivi des KPI, les audits internes et externes, et les retours au propriétaire de la politique.

## Exceptions

Toute exception à la présente politique doit être approuvée et enregistrée par le Responsable de la sécurité de l'information à l'avance, avec acceptation documentée du risque, mesures compensatoires et date de révision définie. Les exceptions doivent être rapportées à l'Équipe de revue de direction.

## Non-conformité

Un employé reconnu avoir violé la présente politique peut être soumis à des mesures disciplinaires pouvant aller jusqu'au licenciement.

## Amélioration continue

La présente politique est révisée et mise à jour dans le cadre du processus d'amélioration continue. Les révisions doivent prendre en compte les évolutions des technologies de surveillance, les développements du paysage des menaces, les exigences réglementaires et les enseignements tirés des incidents et de l'analyse des faux positifs.

---

# Domaines de la norme ISO 27001 couverts

Politique des activités de surveillance — Correspondance avec les contrôles ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership et engagement | 5.1 Politiques de sécurité de l'information |
| Clause 5.2 Politique | 5.4 Responsabilités de la direction |
| Clause 6.2 Objectifs de sécurité de l'information | 5.36 Conformité aux politiques, règles et normes |
| Clause 9.1 Surveillance, mesure, analyse et évaluation | 5.37 Procédures opérationnelles documentées |
| | 6.3 Sensibilisation, éducation et formation à la sécurité de l'information |
| | 6.4 Processus disciplinaire |
| | **8.16 Activités de surveillance** |

**Cadre réglementaire et légal** :

| Cadre | Pertinence |
|-------|-----------|
| nLPD suisse (revLPD) | Art. 8 — Mesures techniques et organisationnelles ; art. 6 — Proportionnalité |
| CO suisse (Code des obligations) | Art. 328b — Limitations du traitement des données des employés |
| OLT 3 suisse (Ordonnance 3 relative à la loi sur le travail) | Art. 26 — Interdiction de la surveillance des comportements |
| RGPD UE (le cas échéant) | Art. 32 — Sécurité du traitement |
| ISO/IEC 27001:2022 | Contrôle Annexe A 8.16 |
| ISO/IEC 27002:2022 | Section 8.16 — Lignes directrices de mise en œuvre |
| NIST SP 800-53 Rév. 5 | SI-4 (Surveillance du système d'information), AU-6 (Révision des enregistrements d'audit), CA-7 (Surveillance continue) |
| NIST CSF 2.0 | DE.CM (Surveillance continue), DE.AE (Analyse des événements défavorables) |
| CIS Controls v8 | Contrôle 8 (Gestion des journaux d'audit), Contrôle 13 (Surveillance et défense du réseau) |

<!-- QA_VERIFIED: 2026-03-29 -->
