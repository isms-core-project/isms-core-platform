<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.8.15-FR:operational:OP-POL:a.8.15 -->
**ISMS-OP-POL-A.8.15 — Journalisation**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Journalisation |
| **Type de document** | Politique opérationnelle |
| **Identifiant du document** | ISMS-OP-POL-A.8.15 |
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

- ISO/IEC 27001:2022 Contrôle A.8.15 — Journalisation
- Voir également : ISMS-OP-POL-A.8.16 (Activités de surveillance), ISMS-OP-POL-A.8.17 (Synchronisation des horloges)

**Contrôles Annexe A associés** :

| Contrôle | Relation avec la journalisation |
|----------|---------------------------------|
| A.5.7 Renseignement sur les menaces | Le renseignement sur les menaces informe les règles de surveillance et les schémas de détection |
| A.5.15–18 Contrôle d'accès et gestion des identités | Les événements d'authentification et d'accès constituent les principales sources de journaux |
| A.5.24–28 Gestion des incidents | L'analyse des journaux soutient la détection, l'investigation et la preuve des incidents |
| A.5.28 Collecte de preuves | Les journaux servent de preuves légales ; leur intégrité doit être préservée |
| A.5.34 Protection de la vie privée et des données à caractère personnel | La surveillance des employés doit respecter les exigences en matière de protection de la vie privée |
| A.8.1 Appareils des utilisateurs finaux | Les événements de terminaux sont journalisés pour la surveillance sécuritaire |
| A.8.7 Protection contre les logiciels malveillants | Les événements de détection de logiciels malveillants sont journalisés et transmis |
| A.8.8 Gestion des vulnérabilités techniques | Les résultats des analyses de vulnérabilités sont journalisés |
| A.8.20 Sécurité des réseaux | Le trafic réseau et les événements de sécurité sont journalisés |

**Politiques internes associées** :

- Politique de contrôle d'accès
- Politique de gestion des incidents
- Politique de protection de la vie privée et des données à caractère personnel
- Politique de sécurité des réseaux
- Politique de sécurité des terminaux
- Politique de classification et de traitement de l'information

---

# Politique de journalisation

## Finalité

La présente politique a pour objet de traiter l'identification et la gestion des événements de sécurité par la journalisation des systèmes de traitement de l'information. Les journaux constituent la piste de preuves pour la détection des incidents, les investigations, la vérification de la conformité et l'analyse légale.

La présente politique soutient la nLPD (revLPD) suisse et l'Ordonnance sur la protection des données (OPDo) en mettant en œuvre la journalisation comme mesure technique et organisationnelle appropriée au risque, y compris les obligations spécifiques de journalisation prévues par l'OPDo art. 4 pour le traitement de données personnelles sensibles. Lorsque l'organisation traite des données de personnes dans l'UE/EEE, les exigences du RGPD s'appliquent également. Pour les activités de surveillance, voir ISMS-OP-POL-A.8.16. Pour la synchronisation des horloges, voir ISMS-OP-POL-A.8.17.

## Champ d'application

Tous les employés et utilisateurs tiers.

Tous les appareils, systèmes et applications utilisés pour traiter, stocker ou transmettre des informations de l'organisation considérés dans le périmètre par la déclaration de périmètre ISO 27001.

## Principe

Tous les systèmes qui traitent, stockent ou transmettent des informations confidentielles ou personnelles doivent avoir la journalisation activée lorsque la journalisation est possible et pratique. Les journaux doivent être collectés de manière centralisée, protégés contre toute altération, conservés pendant une période définie et révisés régulièrement pour détecter les événements de sécurité.

---

## Journalisation des événements

### Événements à journaliser

Des journaux d'événements enregistrant les activités des utilisateurs, les exceptions, les pannes et les événements de sécurité de l'information doivent être produits, conservés et révisés régulièrement. Les événements suivants doivent être journalisés :

| # | Catégorie d'événement | Détails |
|---|----------------------|---------|
| 1 | **Événements d'authentification** | Tentatives réussies et rejetées de connexion et de déconnexion, y compris l'accès à distance (VPN, applications web) |
| 2 | **Accès aux données et aux ressources** | Tentatives réussies et rejetées d'accès aux fichiers, bases de données, applications et ressources réseau |
| 3 | **Modifications de configuration système** | Modifications des paramètres système, des paramètres de sécurité, de la configuration réseau et des règles de pare-feu |
| 4 | **Utilisation de privilèges élevés** | Toutes les actions effectuées avec un accès administrateur, root ou sudo |
| 5 | **Utilitaires système et applications** | Utilisation de programmes utilitaires à privilèges, outils de maintenance et utilitaires de diagnostic |
| 6 | **Opérations sur les fichiers** | Création, modification, suppression et migration de fichiers sur les systèmes critiques |
| 7 | **Alarmes de contrôle d'accès** | Verrouillages de compte, violations de seuil et alertes de détection d'intrusion |
| 8 | **Modifications des systèmes de sécurité** | Activation, désactivation ou modification des antivirus, pare-feux, IDS/IPS et autres systèmes de protection |
| 9 | **Gestion des identités** | Création, modification, suppression et désactivation des comptes utilisateurs et des autorisations |
| 10 | **Transactions applicatives** | Transactions effectuées par les utilisateurs dans les applications critiques pour l'entreprise (systèmes financiers, RH, CRM) |

### Contenu des entrées de journal

Chaque entrée de journal doit inclure, au minimum :

| Champ | Description |
|-------|-------------|
| **Identifiant utilisateur/compte** | Le compte qui a effectué l'action |
| **Horodatage** | Date et heure au format ISO 8601, synchronisées avec la source de temps de référence de l'organisation |
| **Type d'événement** | Description de ce qui s'est produit (connexion, accès aux fichiers, modification de configuration, etc.) |
| **Succès ou échec** | Si l'action a réussi ou a été rejetée |
| **Identifiant du système/appareil** | Nom d'hôte, identifiant d'actif ou adresse IP du système où l'événement s'est produit |
| **Adresse source** | Adresse IP source ou emplacement réseau (le cas échéant) |

---

## Contrôle d'accès aux journaux d'événements

La journalisation et la surveillance des événements doivent être effectuées uniquement par du personnel autorisé.

Les journaux d'événements et les systèmes de surveillance doivent être protégés et l'accès restreint conformément à la Politique de contrôle d'accès. L'accès aux journaux bruts doit être limité à l'équipe de management de la sécurité de l'information et au personnel IT autorisé.

Les administrateurs système ne doivent pas avoir la permission d'effacer ou de désactiver les journaux de leurs propres activités. Lorsque cela n'est pas techniquement applicable, des mesures compensatoires doivent être mises en œuvre (p. ex. transfert des journaux vers un système central hors du contrôle de l'administrateur, révision périodique de l'activité des administrateurs par un rôle distinct).

---

## Protection des informations des journaux d'événements

Les installations de journalisation et les informations des journaux doivent être protégées contre toute altération et tout accès non autorisé.

Les mesures de protection doivent prévenir :

- L'**altération** des entrées de journaux enregistrées ou des types de messages.
- La **suppression** de fichiers journaux ou d'entrées individuelles.
- L'**épuisement de la capacité de stockage** entraînant la perte de données de journaux (les journaux doivent être configurés en mode ouvert en cas de défaillance — alerter lorsque la capacité de stockage atteint **80 %** plutôt qu'écraser silencieusement). La capacité de stockage des journaux doit être surveillée en continu, avec des alertes automatiques aux seuils de 80 % et 90 %. Lorsque 90 % de capacité est atteint, les journaux archivés doivent être déchargés vers un stockage à long terme et l'équipe plateforme doit évaluer si une capacité supplémentaire est nécessaire.
- L'**accès non autorisé** aux données de journaux (les journaux peuvent contenir des données personnelles et sont classifiés au minimum INTERNE).

La protection des journaux doit être assurée par :

- La transmission des journaux vers un **système de journalisation centralisé** distinct des systèmes sources.
- Un stockage **en ajout seul** (append-only) ou **une seule écriture** (write-once) pour les données de journaux lorsque techniquement faisable.
- Des **contrôles d'intégrité cryptographiques** (hachage) pour détecter toute altération lorsque requis à des fins légales ou judiciaires.
- Des **contrôles d'accès** limitant la modification des journaux au seul personnel de sécurité autorisé.

---

## Journalisation centralisée

### Plateforme de journalisation centralisée

La plateforme de journalisation centralisée doit satisfaire aux exigences suivantes :

| Exigence | Spécification |
|----------|--------------|
| **Type de plateforme** | SIEM, agrégateur de journaux ou équivalent (p. ex. Splunk, Microsoft Sentinel, Elastic SIEM, Wazuh ou équivalent) |
| **Déploiement** | Distinct des systèmes sources ; les administrateurs des systèmes sources ne doivent pas avoir d'accès administratif |
| **Stockage** | Capacité suffisante pour les périodes de conservation définies ; seuil d'alerte à 80 % de capacité |
| **Recherche** | Capacité de requêtes en texte intégral et structurées pour l'investigation des incidents et les requêtes de conformité |
| **Alertes** | Règles configurables avec notification à l'équipe de management de la sécurité de l'information (courriel, SMS, système de tickets) |
| **Intégrité** | Stockage en ajout seul ou une seule écriture ; contrôles d'intégrité cryptographiques si requis |
| **Contrôle d'accès** | Accès basé sur les rôles ; lecture seule pour les analystes ; accès administratif restreint aux administrateurs de plateforme |

Les journaux de tous les systèmes critiques doivent être transmis à la plateforme de journalisation centralisée. La plateforme doit être :

- **Distincte** des systèmes générant les journaux (les administrateurs des systèmes sources ne doivent pas avoir d'accès administratif au dépôt central de journaux).
- **Interrogeable** pour soutenir l'investigation des incidents et les requêtes de conformité.
- **Capable d'alertes** pour notifier l'équipe de management de la sécurité de l'information des événements à risque élevé.
- **Protégée** avec les mêmes contrôles de sécurité ou des contrôles supérieurs à ceux des systèmes sources.

Systèmes à inclure dans la journalisation centralisée au minimum :

- Systèmes d'authentification et d'identité (Active Directory, fournisseurs d'identité, SSO).
- Pare-feux et appareils de sécurité réseau.
- Serveurs hébergeant des données confidentielles ou personnelles.
- Passerelles de courriel et web.
- Systèmes VPN et d'accès à distance.
- Systèmes de détection et de réponse sur les terminaux (EDR).
- Consoles d'administration de services cloud (Microsoft 365, AWS, Azure, etc.).

Lorsque la journalisation centralisée automatisée n'est pas faisable pour un système spécifique, la collecte et la révision manuelles des journaux doivent être effectuées à une fréquence définie avec une justification documentée.

---

## Journaux des administrateurs et opérateurs

Les activités des administrateurs système et des opérateurs système doivent être journalisées, et les journaux protégés et régulièrement révisés.

Les titulaires de comptes à privilèges peuvent être en mesure de manipuler les journaux sur les systèmes sous leur contrôle direct. Pour maintenir la responsabilité des utilisateurs à privilèges :

- Les actions des administrateurs doivent être transmises au système de journalisation centralisé en temps réel ou quasi-réel.
- Une révision périodique de l'activité des utilisateurs à privilèges doit être conduite (au moins trimestriellement).
- L'activité anormale des utilisateurs à privilèges (p. ex. accès en dehors des heures de travail, opérations en masse sur les données, modifications de configuration sécuritaire) doit générer des alertes.

---

## Synchronisation des horloges

Les horodatages des journaux doivent être précis et cohérents sur tous les systèmes. Les exigences de synchronisation des horloges sont définies dans **ISMS-OP-POL-A.8.17 — Synchronisation des horloges**. Tous les systèmes générant des données de journaux doivent se conformer aux exigences de source de temps et de tolérance de dérive définies en A.8.17.

---

## Révision des journaux d'événements

### Exigences de révision

Des responsabilités doivent être assignées pour l'analyse et la surveillance des événements de sécurité.

| Type de révision | Fréquence | Responsable | Périmètre |
|-----------------|-----------|-------------|-----------|
| **Alertes automatiques** | Temps réel | Sécurité de l'information | Les événements à risque élevé déclenchent une notification immédiate à l'équipe de management de la sécurité de l'information |
| **Révision des événements de sécurité** | Hebdomadaire | Analyste de sécurité de l'information | Tous les événements de sécurité, échecs d'authentification, anomalies d'accès |
| **Révision des activités à privilèges** | Trimestriel | RSSI / Responsable de la sécurité de l'information | Actions des administrateurs et opérateurs, escalades de privilèges |
| **Révision complète des journaux** | Mensuel | Sécurité de l'information | Tendances, schémas et anomalies sur toutes les sources de journaux |
| **Audit de couverture des sources de journaux** | Trimestriel | Opérations IT | Vérifier que tous les systèmes dans le périmètre transmettent les journaux ; identifier les lacunes |

### Événements à risque élevé

Les événements suivants doivent déclencher des alertes automatiques immédiates et être escaladés vers le processus de gestion des incidents :

| # | Événement à risque élevé | Seuil d'alerte | Réponse |
|---|--------------------------|----------------|---------|
| 1 | Multiples tentatives d'authentification échouées | **5 échecs** en 10 minutes (compte unique) ou **20 échecs** en 10 minutes (comptes multiples depuis une source unique) | Verrouillage du compte ; investiguer la source |
| 2 | Authentification réussie depuis des emplacements inattendus | Connexion depuis un nouveau pays ou une plage d'adresses IP hors de la référence | Vérifier avec l'utilisateur ; suspendre si non confirmé |
| 3 | Désactivation ou modification des contrôles de sécurité | Tout changement à l'antivirus, aux règles de pare-feu ou à la configuration de journalisation | Alerte immédiate à la sécurité de l'information |
| 4 | Accès, téléchargement ou suppression en masse de données | **> 500 fichiers** ou **> 1 Go** accédés/téléchargés en 1 heure par un seul utilisateur | Investiguer ; suspendre l'accès si justifié |
| 5 | Création de nouveaux comptes à privilèges ou élévation de privilèges | Tout nouveau compte admin/root ou élévation de privilèges | Vérifier l'autorisation par rapport aux enregistrements de changements |
| 6 | Détection de logiciels malveillants ou de tentatives d'intrusion | Toute détection confirmée | Processus de gestion des incidents |
| 7 | Modification ou suppression de fichiers journaux | Toute tentative | Alerte immédiate ; investigation légale |

### Escalade d'incident depuis la surveillance

Lorsqu'un événement à risque élevé est détecté, le processus d'escalade suivant doit être suivi :

1. **Alerte** : Alerte automatique générée et envoyée à l'équipe de management de la sécurité de l'information.
2. **Triage** (dans les **30 minutes** pendant les heures de bureau ; **2 heures** en dehors des heures de bureau) : L'analyste évalue l'alerte, détermine s'il s'agit d'un vrai positif, d'un faux positif ou si une investigation est requise.
3. **Investigation** : Si confirmé comme événement de sécurité potentiel, un enregistrement d'incident est créé conformément à la Politique de gestion des incidents.
4. **Escalade** : Les incidents classifiés Élevé ou Critique sont escaladés au RSSI immédiatement.

---

## Conservation des journaux d'événements

| Type de journal | En ligne (consultable) | Archive (récupérable) | Conservation totale |
|-----------------|----------------------|----------------------|---------------------|
| Événements de sécurité (authentification, contrôle d'accès) | 90 jours | 9 mois | **12 mois** |
| Journaux système et d'infrastructure | 90 jours | 6 mois | **9 mois** |
| Journaux applicatifs | 90 jours | 6 mois | **9 mois** |
| Journaux de pare-feu et de sécurité réseau | 90 jours | 9 mois | **12 mois** |
| Journaux de traitement de données personnelles sensibles (OPDo art. 4) | 90 jours | 9 mois | **12 mois** (minimum selon OPDo) |
| Journaux de systèmes financiers | 90 jours | Selon conservation légale | **Conformément au CO suisse art. 958f** |

**Justification de la conservation** : Les journaux d'événements de sécurité et de pare-feu sont conservés 12 mois pour soutenir l'investigation des incidents (le temps de persistance moyen des menaces avancées est de 10 à 21 jours, et les investigations réglementaires peuvent s'étendre sur 12 mois). Les journaux système et applicatifs sont conservés 9 mois pour équilibrer l'utilité opérationnelle et les coûts de stockage. Les journaux OPDo art. 4 nécessitent un minimum de 12 mois conformément à la réglementation.

### Archivage et récupération des journaux

Les journaux archivés doivent être chiffrés, stockés dans un emplacement sécurisé et récupérables dans les délais suivants :

| Âge de l'archive | Délai de récupération cible |
|-----------------|---------------------------|
| 0–90 jours (en ligne) | Immédiat (consultable dans la plateforme) |
| 91 jours – 6 mois | Dans les **4 heures** |
| 6–12 mois | Dans les **24 heures** |
| > 12 mois (si conservé pour des raisons légales/réglementaires) | Dans les **5 jours ouvrables** |

Les procédures de récupération doivent être testées au moins annuellement pour vérifier que les journaux archivés sont accessibles et intacts.

Les journaux ne doivent pas être conservés plus longtemps que nécessaire. À l'expiration des périodes de conservation, les journaux doivent être supprimés de manière sécurisée conformément à la Politique de classification et de traitement de l'information.

---

## nLPD suisse — Obligations de journalisation de l'OPDo article 4

Lorsque l'organisation traite automatiquement des données personnelles sensibles (nLPD art. 5) à grande échelle ou effectue un profilage à risque élevé, les exigences supplémentaires de journalisation suivantes s'appliquent conformément à l'OPDo art. 4 :

**Opérations à journaliser** : Stockage, modification, lecture, communication, suppression et destruction de données personnelles sensibles.

**Contenu du journal** : Identité de la personne ou du système effectuant le traitement, type de traitement, et date et heure.

**Stockage des journaux** : Les journaux du traitement de données personnelles sensibles doivent être stockés **séparément** du système de traitement, conservés pendant un minimum de **1 an**, et l'accès restreint à la vérification de la conformité à la sécurité des données et à la garantie de la confidentialité, de l'intégrité, de la disponibilité et de la traçabilité.

### Évaluation de l'applicabilité de l'OPDo art. 4

L'organisation doit déterminer si l'OPDo art. 4 s'applique en évaluant les critères suivants :

| Critère | Évaluation |
|---------|-----------|
| L'organisation traite-t-elle des **données personnelles sensibles** (nLPD art. 5) ? | Oui / Non |
| Le traitement est-il **automatisé** (pas purement manuel/sur papier) ? | Oui / Non |
| Le traitement est-il **à grande échelle** (volume de personnes concernées, volume de données, portée géographique) ? | Oui / Non |
| L'organisation effectue-t-elle un **profilage à risque élevé** ? | Oui / Non |

Si la réponse au premier critère ET à l'un quelconque des critères restants est **Oui**, les obligations de journalisation de l'OPDo art. 4 s'appliquent. Lorsque l'organisation est incertaine de l'applicabilité de l'art. 4, la mise en œuvre de ces exigences de journalisation est recommandée en tant que bonne pratique.

---

## Vie privée personnelle

La vie privée des employés et des clients doit être respectée conformément à la nLPD suisse et aux exigences légales applicables lors de la mise en œuvre de la journalisation.

### Principes de surveillance des employés

- Les systèmes de journalisation doivent servir des **objectifs de sécurité légitimes** (détection des menaces, investigation des incidents, vérification de la conformité) — et non principalement pour surveiller le comportement des employés.
- Les employés doivent être **informés à l'avance** que la journalisation est en place, ce qui est journalisé et pourquoi, via le programme de sensibilisation à la sécurité de l'information et la documentation de l'emploi.
- Seules les **données strictement nécessaires** doivent être collectées et conservées (minimisation des données).
- L'accès aux journaux contenant des données d'employés doit être restreint au seul personnel de sécurité et de conformité autorisé — pas aux responsables hiérarchiques pour une consultation générale.
- La **journalisation des frappes clavier** et la **surveillance individuelle continue des activités** sont disproportionnées et ne doivent pas être mises en œuvre.
- Lorsque des journaux contenant des données personnelles sont partagés avec des parties externes (p. ex. fournisseurs pour le dépannage), les identifiants personnels doivent être masqués ou anonymisés.

---

## Rôles et responsabilités

| Rôle | Responsabilités |
|------|----------------|
| **RSSI** | Propriétaire de la politique ; approbation du périmètre de surveillance ; point d'escalade pour les alertes critiques ; révision trimestrielle des activités à privilèges |
| **Analyste de sécurité de l'information** | Révision quotidienne/hebdomadaire des journaux ; triage des alertes ; escalade des incidents ; maintenance des règles de détection |
| **Opérations IT / Équipe plateforme** | Administration de la plateforme de journalisation ; gestion de la capacité ; intégration des sources de journaux ; configuration NTP ; archivage |
| **Administrateurs système** | S'assurer que la journalisation est activée sur les systèmes gérés ; coopérer à l'intégration des sources de journaux ; signaler les pannes de journalisation |
| **Conseiller à la protection des données** | Orientation sur l'applicabilité de l'OPDo art. 4 ; impact sur la vie privée des activités de surveillance ; exigences de notification des employés |

---

## Preuves

Les preuves suivantes démontrent la conformité à la présente politique :

| # | Preuve | Responsable | Fréquence |
|---|--------|-------------|-----------|
| 1 | **Configuration de la plateforme de journalisation centralisée** et inventaire des sources de journaux | Opérations IT | *Inventaire des sources révisé trimestriellement ; configuration documentée* |
| 2 | **Exemples d'entrées de journaux** démontrant que les champs requis sont capturés | Sécurité de l'information | *Vérifié annuellement lors de l'audit ; échantillon de 5 systèmes* |
| 3 | **Contrôles de protection des journaux** (restrictions d'accès, stockage en ajout seul, contrôles d'intégrité) | Opérations IT | *Configuration révisée annuellement ; journaux d'accès conservés 12 mois* |
| 4 | **Conformité à la synchronisation des horloges** selon ISMS-OP-POL-A.8.17 (source NTP, surveillance de la dérive, seuil d'alerte) | Opérations IT | *Voir les exigences de preuves de ISMS-OP-POL-A.8.17* |
| 5 | **Configuration de la conservation des journaux** correspondant aux périodes de conservation définies | Opérations IT | *Vérifié semestriellement ; récupération d'archive testée annuellement* |
| 6 | **Relevés de révision des événements de sécurité** (révisions hebdomadaires, révisions trimestrielles des activités à privilèges) | Sécurité de l'information | *Journaux de révision hebdomadaires conservés 12 mois ; révisions trimestrielles présentées lors de la revue de direction* |
| 7 | **Règles d'alertes** et exemples de notifications d'alerte pour les événements à risque élevé | Sécurité de l'information | *Règles révisées trimestriellement ; exemples d'alertes conservés 12 mois* |
| 8 | **Relevés de conformité OPDo art. 4** (évaluation d'applicabilité ; journaux de traitement de données personnelles sensibles stockés séparément) | Conseiller à la protection des données | *Évaluation d'applicabilité révisée annuellement ; séparation des journaux vérifiée trimestriellement* |
| 9 | **Relevés de notification des employés** (formation de sensibilisation, avis de confidentialité concernant la surveillance) | RH / Sécurité de l'information | *Mis à jour par changement de politique ; complétion de la formation suivie annuellement* |
| 10 | **Indicateur de couverture des sources de journaux** (pourcentage des systèmes dans le périmètre transmettant des journaux) | Opérations IT | *Trimestriel ; cible : 100 % des systèmes critiques, ≥ 95 % de tous les systèmes dans le périmètre* |

---

# Conformité à la politique

## Mesure de la conformité

L'équipe de management de la sécurité de l'information doit vérifier la conformité à la présente politique par diverses méthodes, notamment les audits de couverture des sources de journaux, les vérifications de conformité à la conservation, la complétion des révisions de journaux, les audits internes et externes, et les retours au propriétaire de la politique.

## Exceptions

Toute exception à la présente politique doit être approuvée et enregistrée par le Responsable de la sécurité de l'information à l'avance, avec acceptation documentée du risque, mesures compensatoires et date de révision définie. Les exceptions doivent être rapportées à l'Équipe de revue de direction.

## Non-conformité

Un employé reconnu avoir violé la présente politique peut être soumis à des mesures disciplinaires pouvant aller jusqu'au licenciement.

## Amélioration continue

La présente politique est révisée et mise à jour dans le cadre du processus d'amélioration continue. Les révisions doivent prendre en compte les modifications des normes de journalisation, des exigences réglementaires (y compris les mises à jour de l'OPDo) et les enseignements tirés des incidents.

---

# Domaines de la norme ISO 27001 couverts

Politique de journalisation — Correspondance avec les contrôles ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership et engagement | 5.1 Politiques de sécurité de l'information |
| Clause 5.2 Politique | 5.4 Responsabilités de la direction |
| Clause 6.2 Objectifs de sécurité de l'information | 5.36 Conformité aux politiques, règles et normes |
| Clause 7.3 Sensibilisation | 5.37 Procédures opérationnelles documentées |
| Clause 9.1 Surveillance, mesure, analyse et évaluation | 6.3 Sensibilisation, éducation et formation à la sécurité de l'information |
| | 6.4 Processus disciplinaire |
| | **8.15 Journalisation** |
| | 8.16 Activités de surveillance *(voir ISMS-OP-POL-A.8.16)* |
| | 8.17 Synchronisation des horloges *(voir ISMS-OP-POL-A.8.17)* |

**Cadre réglementaire et légal** :

| Cadre | Pertinence |
|-------|-----------|
| nLPD suisse (revLPD) | Art. 8 — Mesures techniques et organisationnelles ; art. 6 — Proportionnalité de la surveillance |
| OPDo suisse (Ordonnance sur la protection des données) | Art. 4 — Obligations de journalisation pour le traitement de données personnelles sensibles |
| CO suisse (Code des obligations) | Art. 328b — Limitations du traitement des données des employés ; art. 958f — Conservation des documents commerciaux |
| RGPD UE (le cas échéant) | Art. 32 — Sécurité du traitement (journalisation comme mesure appropriée) |
| ISO/IEC 27001:2022 | Contrôle Annexe A 8.15 (voir aussi 8.16, 8.17) |
| ISO/IEC 27002:2022 | Section 8.15 — Lignes directrices de mise en œuvre |
| NIST SP 800-53 Rév. 5 | AU-2 (Journalisation des événements), AU-3 (Contenu des enregistrements d'audit), AU-6 (Révision/analyse des audits), AU-8 (Horodatages), AU-9 (Protection des informations d'audit), AU-11 (Conservation des enregistrements d'audit) |
| NIST SP 800-92 | Guide de gestion des journaux de sécurité informatique |
| CIS Controls v8 | Contrôle 8 (Gestion des journaux d'audit) |

<!-- QA_VERIFIED: 2026-03-29 -->
