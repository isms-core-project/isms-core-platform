<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.8.17-FR:operational:OP-POL:a.8.17 -->
**ISMS-OP-POL-A.8.17 — Synchronisation des horloges**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Synchronisation des horloges |
| **Type de document** | Politique opérationnelle |
| **Identifiant du document** | ISMS-OP-POL-A.8.17 |
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

- ISO/IEC 27001:2022 Contrôle A.8.17 — Synchronisation des horloges

**Contrôles Annexe A associés** :

| Contrôle | Relation avec la synchronisation des horloges |
|----------|-----------------------------------------------|
| A.8.15 Journalisation | Des horodatages précis sont un prérequis pour des enregistrements de journaux significatifs |
| A.8.16 Activités de surveillance | La corrélation des événements dépend d'horloges synchronisées sur tous les systèmes |
| A.5.24–28 Gestion des incidents | L'investigation légale nécessite une chronologie cohérente sur tous les systèmes |
| A.5.28 Collecte de preuves | La précision des horloges sous-tend la recevabilité légale des preuves numériques |
| A.8.20 Sécurité des réseaux | Les appareils réseau doivent être synchronisés dans le temps pour la corrélation des événements de sécurité |

**Politiques internes associées** :

- Politique de journalisation (A.8.15)
- Politique des activités de surveillance (A.8.16)
- Politique de gestion des incidents
- Politique de sécurité des réseaux

---

# Politique de synchronisation des horloges

## Finalité

La présente politique a pour objet de s'assurer que les horloges de tous les systèmes de traitement de l'information concernés au sein de l'organisation sont synchronisées avec une source de temps de référence unique et cohérente. Des horodatages précis et cohérents sont essentiels pour la corrélation des journaux, l'investigation des incidents, les preuves légales, la conformité réglementaire et l'intégrité des systèmes distribués.

La présente politique soutient la nLPD (revLPD) suisse art. 8 en maintenant l'intégrité des données par un horodatage vérifiable. Lorsque l'organisation traite des données de personnes dans l'UE/EEE, le RGPD art. 32 (sécurité du traitement) s'applique également. Les obligations de journalisation de l'OPDo art. 4 pour le traitement de données personnelles sensibles nécessitent des horodatages précis pour garantir l'intégrité et la traçabilité des journaux.

## Champ d'application

La présente politique s'applique à tous les systèmes générant des données de journaux ou des enregistrements sensibles au temps, notamment :

- Serveurs et postes de travail (physiques et virtuels).
- Infrastructure réseau (routeurs, commutateurs, pare-feux, équilibreurs de charge, contrôleurs sans fil).
- Appareils de sécurité (IDS/IPS, agents EDR, systèmes de contrôle d'accès).
- Services cloud et plateformes SaaS.
- Serveurs de bases de données et serveurs applicatifs.
- Systèmes de sécurité physique (vidéosurveillance, lecteurs de badges) lorsqu'intégrés à la journalisation IT.
- Appareils IoT et de technologie opérationnelle (OT) dans le périmètre ISMS.

Tous les employés et utilisateurs tiers responsables de l'administration ou du déploiement de systèmes sont responsables de la synchronisation du temps sur les systèmes qu'ils gèrent.

## Principe

Toutes les horloges doivent se synchroniser avec une source de temps de référence unique approuvée par l'organisation. Les données de temps doivent être protégées contre toute modification non autorisée. Les horodatages doivent être enregistrés dans un format cohérent pour permettre une corrélation fiable entre les systèmes, les emplacements et les prestataires de services.

---

## Sources de temps faisant autorité

### Référence principale

L'organisation doit désigner une source de temps faisant autorité principale :

| Attribut | Exigence |
|----------|---------|
| **Source principale** | Serveurs NTP de METAS (Institut fédéral de métrologie suisse) : `ntp.metas.ch`, `ntp11.metas.ch`, `ntp12.metas.ch`, `ntp13.metas.ch` — Stratum 1, traçable à UTC(CH) |
| **Source secondaire** | Pool NTP suisse : `0.ch.pool.ntp.org`, `1.ch.pool.ntp.org`, `2.ch.pool.ntp.org`, `3.ch.pool.ntp.org` |
| **Sources minimales** | Chaque serveur de temps interne doit se synchroniser avec au moins **deux** sources externes indépendantes (conformément au CIS Contrôle 8.4) |
| **Traçabilité** | La source principale doit être traçable à un institut national de métrologie ou à un signal horaire GPS/GNSS |

### Architecture de temps interne

L'organisation doit déployer des serveurs NTP internes dans une architecture à niveaux :

| Niveau | Rôle | Configuration |
|--------|------|---------------|
| **Stratum 2 interne** | Serveurs NTP internes principaux synchronisés directement aux sources Stratum 1 externes (METAS) | Minimum 2 serveurs pour la redondance ; séparés géographiquement si possible |
| **Stratum 3 interne** | Serveurs de site ou de département (optionnel pour les environnements plus grands) | Se synchronisent avec le Stratum 2 interne ; servent les clients locaux |
| **Clients** | Tous les terminaux, serveurs applicatifs, appareils réseau | Se synchronisent avec le Stratum 2 ou Stratum 3 interne via NTP |

Pour les petites organisations : le contrôleur de domaine principal ou un serveur interne désigné peut servir de seul serveur NTP interne, synchronisé avec au moins deux sources externes.

Lorsque l'organisation exploite des oscillateurs disciplinés par GPS (GPSDO) pour l'indépendance Stratum 0/1 (p. ex. réseaux isolés), ceux-ci doivent être documentés et maintenus selon les spécifications du fabricant.

---

## Protocole de synchronisation

### Configuration NTP

Le protocole NTP (Network Time Protocol) doit être utilisé pour la synchronisation du temps sur tous les systèmes d'entreprise standard.

| Exigence | Spécification |
|----------|--------------|
| **Protocole** | NTPv4 (RFC 5905) minimum |
| **Sécurité** | Network Time Security (NTS, RFC 8915) doit être activé lorsque pris en charge par le client et le serveur. Lorsque NTS n'est pas pris en charge, les communications NTP doivent être restreintes aux serveurs approuvés via des règles de pare-feu ou des listes de contrôle d'accès |
| **Authentification** | L'authentification par clé symétrique NTP ou NTS doit être utilisée entre les serveurs internes et les sources externes |
| **Intervalle de sondage** | Par défaut (64–1024 secondes) ; intervalles plus courts pour les systèmes critiques si nécessaire |
| **Règles de pare-feu** | NTP sortant (UDP 123) autorisé uniquement vers les sources externes approuvées ; NTP entrant restreint aux serveurs internes |

### Protocole de temps de précision (PTP)

Lorsqu'une précision sub-microseconde est requise (p. ex. transactions financières, contrôle industriel, traitement de données haute fréquence), le protocole IEEE 1588 PTP (PTPv2) doit être déployé :

- Des commutateurs réseau compatibles PTP (horloges de frontière ou transparentes) sont requis.
- Une horloge grand maître PTP (disciplinée par GPS) doit être déployée.
- PTP est un complément — et non un remplacement — de NTP dans l'ensemble de l'entreprise.

L'applicabilité de PTP est déterminée lors de la conception du système et documentée dans l'architecture du système.

---

## Format des horodatages

### Format standard

Tous les systèmes doivent enregistrer les horodatages dans l'un des formats suivants :

| Format | Exemple | Cas d'usage |
|--------|---------|------------|
| **UTC** (préféré) | `2026-02-07T14:30:00Z` | Serveurs, bases de données, appareils réseau, SIEM, toute l'infrastructure |
| **Heure locale avec décalage UTC** | `2026-02-07T15:30:00+01:00` | Journaux applicatifs, rapports destinés aux utilisateurs (lorsque l'UTC est impratique) |

**Règles obligatoires** :

- Le format ISO 8601 / RFC 3339 doit être utilisé pour tous les horodatages générés automatiquement.
- **L'UTC est le standard** pour toute l'infrastructure, la journalisation et les systèmes de sécurité.
- L'heure locale avec décalage UTC explicite est autorisée uniquement au niveau applicatif/de présentation.
- L'heure locale **sans** décalage UTC (p. ex. `15:30:00 CET`) est **inacceptable** — les abréviations de fuseau horaire sont ambiguës (les transitions CET/CEST créent des heures dupliquées).
- Les abréviations de fuseaux horaires nominaux ne doivent pas être utilisées dans les horodatages des journaux.

### Heure d'été

L'UTC élimine l'ambiguïté liée à l'heure d'été (HE). Lors de la transition automnale (CEST → CET), l'heure 02h00–03h00 se répète. Les systèmes utilisant l'heure locale sans décalage ne peuvent pas distinguer les deux occurrences. Les systèmes enregistrant en UTC ne sont pas affectés.

Tous les systèmes doivent utiliser UTC ou un décalage explicite pour prévenir l'ambiguïté d'horodatage liée à l'heure d'été.

---

## Tolérances de dérive des horloges

### Décalage maximal acceptable

Les systèmes doivent maintenir la précision des horloges dans les tolérances suivantes :

| Niveau de système | Décalage maximal | Seuil de surveillance | Action |
|------------------|-----------------|----------------------|--------|
| **Critique** (authentification, SIEM, financier, bases de données) | < 1 ms | Alerte à > 1 ms | Investiguer et resynchroniser immédiatement |
| **Entreprise standard** (serveurs, appareils réseau) | < 50 ms | Alerte à > 50 ms | Investiguer dans les 4 heures |
| **Général** (postes de travail, imprimantes) | < 500 ms | Alerte à > 500 ms | Resynchroniser au prochain cycle de sondage |
| **Alarme** (tout système) | > 128 ms | Seuil de saut NTP | Le client NTP effectuera un saut d'horloge ; enregistrer l'événement |
| **Panique** (tout système) | > 1 000 secondes | Seuil de panique NTP | Le démon NTP se termine ; intervention manuelle requise |

### Surveillance de la dérive

La dérive des horloges doit être surveillée en continu à l'aide d'outils de supervision système (p. ex. Prometheus, Nagios, CloudWatch ou équivalent) :

- Les métriques de décalage NTP, de gigue et de stratum doivent être collectées sur tous les systèmes surveillés.
- Alerter lorsque le décalage dépasse le seuil du niveau de système.
- Alerter en cas de changement de stratum (p. ex. un serveur passant du Stratum 2 au Stratum 16 indique la perte de synchronisation en amont).
- Les alertes de dérive des horloges doivent être transmises à la plateforme de surveillance centralisée.
- Analyse mensuelle des tendances de dérive des horloges sur l'ensemble du parc.

---

## Synchronisation du temps des services cloud

### Sources de temps spécifiques aux fournisseurs

Lorsque les systèmes fonctionnent dans des environnements cloud, le service de synchronisation du temps du fournisseur doit être utilisé :

| Fournisseur | Service de temps | Accès | Notes |
|-------------|----------------|-------|-------|
| **AWS** | Amazon Time Sync Service | `169.254.169.123` (lien local) | Horloges atomiques + GPS par région ; préconfiguré sur Amazon Linux ; utilise le lissage des secondes intercalaires |
| **Azure** | VMICTimeSync (PTP hyperviseur) | Appareil PTP dans la VM | Temps fourni via l'hyperviseur, pas via NTP réseau ; chrony recommandé |
| **GCP** | Google Public NTP | `time.google.com` | Préconfiguré sur Compute Engine ; utilise le lissage des secondes intercalaires (24 heures) |

### Exigences pour les environnements hybrides

Lorsque l'organisation opère à la fois sur site et dans le cloud :

- **Ne pas mélanger les sources de temps avec et sans lissage** dans le même environnement. Les fournisseurs cloud (AWS, GCP) lissent les secondes intercalaires sur 24 heures ; les sources NTP traditionnelles (METAS, pool.ntp.org) appliquent un saut. Le mélange crée des écarts de temps lors des événements de secondes intercalaires.
- Documenter quelle source de temps est utilisée par chaque environnement.
- Pour les architectures hybrides, désigner si le temps cloud ou sur site fait autorité, et configurer la direction de synchronisation en conséquence.
- Surveiller la dérive du temps des VM cloud — la planification de la virtualisation et la migration en direct peuvent introduire des décalages d'horloge.

---

## Gestion des secondes intercalaires

Une seconde intercalaire est un ajustement d'une seconde (positif ou négatif) appliqué à UTC pour le maintenir aligné avec la rotation terrestre. 27 secondes intercalaires ont été ajoutées depuis 1972 ; cette pratique devrait être abolie d'ici 2035 au plus tard (selon la Résolution 4 de la CGPM, novembre 2022).

### Stratégie organisationnelle

L'organisation doit adopter une **stratégie unique et cohérente de gestion des secondes intercalaires** dans tous les environnements :

| Stratégie | Description | Quand utiliser |
|-----------|-------------|---------------|
| **Saut** (traditionnel) | Insérer ou supprimer une seconde à 23:59:60 UTC | Systèmes sur site utilisant des sources NTP traditionnelles (METAS, pool.ntp.org) |
| **Lissage** | Répartir la seconde supplémentaire sur 24 heures en ajustant légèrement la vitesse de l'horloge | Environnements cloud utilisant les services de temps des fournisseurs (AWS, GCP) |

**Règles** :

- Ne jamais mélanger des sources de temps avec saut et des sources avec lissage dans le même environnement.
- Documenter la stratégie choisie et la communiquer aux administrateurs système.
- Tester la gestion des secondes intercalaires avant tout événement de seconde intercalaire planifié.
- Surveiller les systèmes pendant 24 heures après un événement de seconde intercalaire.
- Une fois les secondes intercalaires abolies (prévu d'ici 2035), mettre à jour les configurations pour supprimer la logique de gestion des secondes intercalaires.

---

## Sécurité NTP

### Protection contre les attaques basées sur le temps

L'infrastructure NTP doit être protégée contre les attaques par usurpation, rejeu et déni de service :

| Menace | Atténuation |
|--------|------------|
| **Usurpation NTP** | Activer NTS (RFC 8915) ou l'authentification par clé symétrique NTP ; restreindre les sources NTP aux serveurs approuvés |
| **Attaques par rejeu** | NTS assure la protection contre les rejeux via des cookies uniques par échange |
| **Amplification DDoS** | Désactiver la liste de surveillance NTP (monlist) (`restrict ... noquery`) ; restreindre l'accès NTP aux clients internes |
| **Modification non autorisée** | Configurations des serveurs NTP protégées par des contrôles d'accès ; les changements nécessitent l'approbation de la gestion des changements |
| **Point de défaillance unique** | Minimum deux sources externes indépendantes ; redondance des serveurs internes |

### Protection de la configuration

- Les fichiers de configuration NTP doivent être protégés contre toute modification non autorisée (permissions de fichiers, surveillance de l'intégrité).
- Les modifications de la configuration NTP doivent suivre le processus de gestion des changements.
- L'état du service NTP doit être surveillé ; la panne du service doit générer une alerte.

---

## Rôles et responsabilités

| Rôle | Responsabilités |
|------|----------------|
| **RSSI** | Propriétaire de la politique ; approbation de l'architecture de synchronisation du temps ; point d'escalade pour les problèmes de dérive persistants |
| **Opérations IT / Équipe plateforme** | Déploiement et maintenance des serveurs NTP ; configuration de la surveillance ; configuration des sources de temps cloud ; gestion des événements de secondes intercalaires |
| **Administrateurs système** | S'assurer que NTP est configuré sur les systèmes gérés ; signaler les pannes de synchronisation ; vérifier les paramètres de temps lors du déploiement des systèmes |
| **Administrateurs réseau** | Configuration NTP sur les appareils réseau ; règles de pare-feu pour le trafic NTP ; déploiement de NTS sur les appareils pris en charge |
| **Ingénieurs cloud** | Configuration des sources de temps spécifiques au cloud ; documentation des sources de temps pour l'architecture hybride ; surveillance de la dérive des VM cloud |

---

## Preuves

Les preuves suivantes démontrent la conformité à la présente politique :

| # | Preuve | Responsable | Fréquence |
|---|--------|-------------|-----------|
| 1 | **Documentation de l'architecture NTP** (serveurs internes, sources externes, hiérarchie des stratums, paramètres de protocole/sécurité) | Opérations IT | *Documentée ; révisée annuellement et lors des modifications d'architecture* |
| 2 | **Indicateur de couverture de conformité NTP** (pourcentage des systèmes dans le périmètre avec configuration NTP vérifiée et sources de temps approuvées) | Opérations IT | *Trimestriel ; cible : 100 % des systèmes critiques, ≥ 95 % de tous les systèmes dans le périmètre* |
| 3 | **Relevés de surveillance de la dérive des horloges** (métriques de décalage, de gigue et de stratum ; alertes générées et résolues) | Opérations IT | *Surveillance continue ; rapport de tendances mensuel ; alertes conservées 12 mois* |
| 4 | **Documentation des sources de temps cloud** (service fournisseur, configuration, stratégie de lissage, considérations hybrides) | Ingénieurs cloud | *Documentée par service cloud ; révisée annuellement* |
| 5 | **Configuration de sécurité NTP** (état NTS, authentification, règles de pare-feu, restrictions d'accès) | Opérations IT / Réseau | *Configuration documentée ; révisée annuellement* |
| 6 | **Conformité du format des horodatages** (exemples d'entrées de journaux de 5+ systèmes démontrant le format UTC ou avec décalage) | Sécurité de l'information | *Vérifié annuellement lors des audits* |
| 7 | **Documentation de la stratégie des secondes intercalaires** (approche choisie, relevés de tests, surveillance lors des événements) | Opérations IT | *Documentée ; testée avant chaque événement de seconde intercalaire (ou annuellement si aucun n'est planifié)* |

---

# Conformité à la politique

## Mesure de la conformité

L'équipe de management de la sécurité de l'information vérifiera la conformité à la présente politique par des audits de configuration NTP, des révisions de surveillance de la dérive, une vérification du format des horodatages, des audits internes et externes, et des retours au propriétaire de la politique.

## Exceptions

Toute exception à la présente politique doit être approuvée et enregistrée par le Responsable de la sécurité de l'information à l'avance, avec acceptation documentée du risque, mesures compensatoires et date de révision définie. Les exceptions doivent être rapportées à l'Équipe de revue de direction.

Les systèmes qui ne peuvent pas prendre en charge NTP (p. ex. appareils OT anciens, environnements de test isolés) doivent être documentés avec justification, et une vérification manuelle du temps doit être effectuée à une fréquence définie.

## Non-conformité

Un employé reconnu avoir violé la présente politique peut être soumis à des mesures disciplinaires pouvant aller jusqu'au licenciement.

## Amélioration continue

La présente politique est révisée et mise à jour dans le cadre du processus d'amélioration continue. Les révisions doivent prendre en compte les modifications des normes NTP, la disponibilité des sources de temps, les services de temps des fournisseurs cloud, les évolutions de la politique sur les secondes intercalaires, et les enseignements tirés des incidents de dérive des horloges ou des investigations légales.

---

# Domaines de la norme ISO 27001 couverts

Politique de synchronisation des horloges — Correspondance avec les contrôles ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership et engagement | 5.1 Politiques de sécurité de l'information |
| Clause 5.2 Politique | 5.4 Responsabilités de la direction |
| Clause 6.2 Objectifs de sécurité de l'information | 5.36 Conformité aux politiques, règles et normes |
| | 5.37 Procédures opérationnelles documentées |
| | 6.3 Sensibilisation, éducation et formation à la sécurité de l'information |
| | **8.17 Synchronisation des horloges** |

**Cadre réglementaire et légal** :

| Cadre | Pertinence |
|-------|-----------|
| nLPD suisse (revLPD) | Art. 8 — Mesures techniques et organisationnelles (intégrité des données) |
| OPDo suisse (Ordonnance sur la protection des données) | Art. 4 — Obligations de journalisation (horodatages précis requis) |
| RGPD UE (le cas échéant) | Art. 32 — Sécurité du traitement |
| ISO/IEC 27001:2022 | Contrôle Annexe A 8.17 |
| ISO/IEC 27002:2022 | Section 8.17 — Lignes directrices de mise en œuvre |
| NIST SP 800-53 Rév. 5 | AU-8 (Horodatages), AU-8(1) (Synchronisation avec la source faisant autorité), SC-45 (Synchronisation du temps du système) |
| NIST CSF 2.0 | PR.PS-04 (Enregistrements de journaux générés pour la surveillance continue) |
| CIS Controls v8 | Contrôle 8.4 (Normaliser la synchronisation du temps) |

<!-- QA_VERIFIED: 2026-03-29 -->
