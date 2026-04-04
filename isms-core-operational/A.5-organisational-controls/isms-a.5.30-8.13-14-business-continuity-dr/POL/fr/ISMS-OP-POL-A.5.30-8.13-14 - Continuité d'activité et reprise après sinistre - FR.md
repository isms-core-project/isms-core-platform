<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.5.30-8.13-14-FR:operational:OP-POL:a.5.30-8.13-14 -->
**ISMS-OP-POL-A.5.30-8.13-14 — Continuité d'activité et reprise après sinistre**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Continuité d'activité et reprise après sinistre |
| **Type de document** | Politique opérationnelle |
| **Identifiant du document** | ISMS-OP-POL-A.5.30-8.13-14 |
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

- ISO/IEC 27001:2022 Contrôle A.5.30 — Préparation TIC pour la continuité d'activité
- ISO/IEC 27001:2022 Contrôle A.8.13 — Sauvegarde des informations
- ISO/IEC 27001:2022 Contrôle A.8.14 — Redondance des installations de traitement de l'information
- ISO/IEC 22301 — Systèmes de management de la continuité d'activité (référence informative)
- NIST SP 800-34 Rev 1 — Guide de planification des mesures d'urgence pour les systèmes d'information fédéraux (référence informative)

**Contrôles Annexe A connexes** :

| Contrôle | Relation avec la continuité d'activité et la reprise après sinistre |
|----------|---------------------------------------------------------------------|
| A.5.9 Inventaire des informations et autres actifs associés | L'inventaire des actifs oriente le BIA et l'identification du périmètre des sauvegardes |
| A.5.19–23 Relations fournisseurs et services cloud | Engagements BC/DR des fournisseurs et modèle de responsabilité partagée |
| A.5.24–28 Cycle de vie de la gestion des incidents | Les incidents majeurs peuvent déclencher l'activation des plans BC/DR |
| A.5.29 Sécurité de l'information lors d'une perturbation | Continuité de la sécurité pendant les événements BC/DR |
| A.8.6 Gestion des capacités | La planification des capacités soutient la redondance et l'infrastructure DR |
| A.8.9 Gestion des configurations | Les référentiels de configuration sont nécessaires pour la reconstruction et la reprise des systèmes |
| A.8.15 Journalisation | Les opérations de sauvegarde et de reprise doivent être journalisées |
| A.8.16 Surveillance des activités | Surveillance des sauvegardes et vérifications de santé de la redondance |

**Politiques internes connexes** :

- Politique de gestion des actifs
- Politique de gestion des incidents
- Politique des services cloud et de la sécurité des fournisseurs
- Politique de journalisation
- Politique de surveillance des activités (A.8.16)
- Politique de gestion des changements

---

# Politique de continuité d'activité et de reprise après sinistre

## Objet

La présente politique a pour objet de garantir que l'organisation peut poursuivre ou reprendre ses opérations métier critiques et ses installations de traitement de l'information à la suite d'un incident perturbateur. Elle établit les exigences pour l'analyse d'impact sur l'activité, la sauvegarde des informations, la redondance des systèmes et la planification de la continuité TIC.

Cette politique couvre trois contrôles ISO 27001:2022 connexes dans un cadre unifié, car ils fonctionnent comme un écosystème BC/DR intégré : la sauvegarde fournit les capacités de récupération des données (A.8.13), la redondance fournit les capacités de disponibilité des systèmes (A.8.14), et la préparation TIC fournit la préparation globale et la gouvernance (A.5.30). Chaque contrôle maintient des exigences distinctes à des fins de Déclaration d'applicabilité.

Cette politique soutient la nLPD suisse (revDSG) art. 8 en mettant en œuvre des mesures techniques et organisationnelles proportionnées aux risques pour protéger la disponibilité et l'intégrité des données personnelles et des systèmes de traitement de l'information. Lorsque l'organisation traite des données de personnes dans l'UE/EEE, les exigences du RGPD art. 32(1)(c) concernant la capacité à rétablir la disponibilité et l'accès aux données personnelles dans les meilleurs délais s'appliquent également.

## Champ d'application

Tous les employés et utilisateurs tiers.

Tous les systèmes d'information, applications, infrastructures et services considérés dans le périmètre de la déclaration de périmètre ISO 27001, notamment :

- Serveurs, bases de données et référentiels de code
- Infrastructure cloud et applications SaaS
- Infrastructure réseau et systèmes de sécurité
- Applications et données critiques pour l'activité
- Configurations système et infrastructure sous forme de code

**Hors périmètre pour les sauvegardes** (sauf si spécifiquement évalué pour les risques) :

- Stockage local des postes de travail et ordinateurs portables (les données doivent résider sur des serveurs sauvegardés, des services cloud ou des référentiels ; les données locales uniquement sont exposées à une perte permanente et ne sont pas protégées par cette politique)
- Stockage local des appareils mobiles

**Hors périmètre de cette politique** :

- Continuité d'activité non-TIC (cadre BCM organisationnel)
- Documents physiques et informations non numériques (couverts par les contrôles de sécurité physique)

## Principe

**La sécurité des personnes doit être notre première priorité. Toujours.**

Le management de la continuité d'activité et la continuité de la sécurité de l'information doivent aborder les menaces, les risques et les incidents qui ont un impact sur la continuité des opérations. Le cadre est basé sur les meilleures pratiques du secteur et s'aligne sur ISO 22301 Management de la continuité d'activité.

L'organisation doit :

- Conduire une analyse d'impact sur l'activité pour identifier les systèmes critiques et déterminer les exigences de reprise.
- Maintenir des copies de sauvegarde des informations, des logiciels et des systèmes, testées régulièrement pour confirmer la recouvrabilité.
- Mettre en œuvre une redondance pour les installations de traitement de l'information critiques afin de répondre aux exigences de disponibilité.
- Planifier, mettre en œuvre, maintenir et tester la continuité TIC sur la base des objectifs de continuité d'activité.

**Principe critique — « Reprise non testée = Pas de reprise » **: La réussite des sauvegardes sans test de restauration, la redondance sans test de basculement, et les plans BC sans test de scénario procurent une fausse confiance. Une vérification basée sur des preuves par des tests systématiques est requise.

---

## Analyse d'impact sur l'activité et criticité des systèmes

### Analyse d'impact sur l'activité

La continuité d'activité doit être basée sur une analyse d'impact sur l'activité (AIA) documentée et une évaluation des risques. L'AIA doit :

- Identifier les processus métier critiques et leurs dépendances TIC.
- Quantifier l'impact des perturbations TIC (financier, opérationnel, réputationnel, réglementaire).
- Établir les Objectifs de point de reprise (OPR) et les Objectifs de temps de reprise (OTR) pour chaque système critique.
- Identifier les interdépendances entre les systèmes.

**Fréquence de l'AIA** : L'AIA doit être conduite initialement lors de la mise en œuvre du SMSI, révisée annuellement, et mise à jour lors de changements significatifs de l'activité (nouveaux services, acquisitions, changements majeurs de systèmes) ou après des incidents majeurs.

### Niveaux de criticité des systèmes

Les systèmes doivent être classifiés en niveaux de criticité sur la base des résultats de l'AIA. Ces niveaux déterminent la fréquence des sauvegardes, les exigences de redondance et les calendriers de tests :

| Niveau | Classification | OPR maximal | OTR maximal | Exemples |
|--------|---------------|------------|------------|---------|
| **Niveau 1** | Critique | 1 heure | 4 heures | Application métier principale, base de données primaire, système d'authentification |
| **Niveau 2** | Élevé | 6 heures | 24 heures | Messagerie, plateforme de collaboration, applications métier secondaires |
| **Niveau 3** | Moyen | 24 heures | 72 heures | Outils internes, environnements de développement, systèmes de reporting |
| **Niveau 4** | Faible | 7 jours | > 72 heures | Archives, services internes non critiques |

Les propriétaires de systèmes, en consultation avec le Coordinateur BC/DR, doivent déterminer le niveau approprié pour chaque système sur la base des résultats de l'AIA.

**Attribution des rôles** : Lorsque l'organisation n'a pas de Coordinateur BC/DR dédié, le Responsable des opérations IT assume les responsabilités de coordination BC/DR. Cette attribution doit être formellement documentée dans la description de rôle.

### OPR et OTR

**L'Objectif de point de reprise (OPR)** définit la perte de données maximale acceptable mesurée en temps. L'OPR détermine la fréquence des sauvegardes. Exemple : Un OPR de 6 heures signifie qu'une perte de données allant jusqu'à 6 heures est acceptable, donc les sauvegardes doivent avoir lieu au moins toutes les 6 heures.

**L'Objectif de temps de reprise (OTR)** définit le délai maximal acceptable pour restaurer un système après une perturbation. L'OTR détermine la stratégie de redondance et de reprise. Exemple : Un OTR de 4 heures signifie que le système doit être opérationnel dans les 4 heures suivant la défaillance.

Les systèmes ne pouvant pas répondre à leur OPR ou OTR défini doivent suivre le processus de gestion des exceptions (voir Conformité à la politique — Exceptions).

---

## Sauvegarde des informations

### Périmètre des sauvegardes

Les catégories d'informations suivantes doivent être sauvegardées :

| Catégorie | Exigence de sauvegarde |
|-----------|----------------------|
| Données métier critiques (clients, financières, opérationnelles) | Obligatoire |
| Données et configurations des systèmes de production | Obligatoire |
| Logiciels d'application et dépendances | Obligatoire |
| Configurations de sécurité et données de contrôle d'accès | Obligatoire |
| Données métier importantes | Obligatoire |
| Environnements de développement/test | Basé sur les risques (sauvegarde si le coût de recréation dépasse le coût de la sauvegarde) |
| Données éphémères (caches, journaux temporaires) | Non requise |

### Calendrier et conservation des sauvegardes

Un calendrier de sauvegarde, de conservation et de tests doit être maintenu et rendu disponible. La fréquence des sauvegardes doit s'aligner sur l'OPR pour chaque niveau de système :

| Niveau du système | Fréquence des sauvegardes | Conservation minimale |
|-------------------|--------------------------|----------------------|
| **Niveau 1 (Critique)** | Réplication continue ou horaire | Quotidien : 30 jours ; Hebdomadaire : 90 jours ; Mensuel : 12 mois |
| **Niveau 2 (Élevé)** | Toutes les 4–6 heures | Quotidien : 30 jours ; Hebdomadaire : 90 jours ; Mensuel : 12 mois |
| **Niveau 3 (Moyen)** | Quotidien | Quotidien : 7 jours ; Hebdomadaire : 28 jours ; Mensuel : 12 mois |
| **Niveau 4 (Faible)** | Hebdomadaire ou à la demande | Hebdomadaire : 28 jours ; Mensuel : 12 mois |

**Conservation étendue** : Des périodes de conservation plus longues peuvent être requises par la réglementation (p. ex. dossiers financiers 7–10 ans), les demandes de conservation légale ou les obligations contractuelles. La conservation étendue doit être justifiée (exigence réglementaire, conservation légale ou obligation contractuelle) pour éviter une accumulation inutile de données. Des périodes de conservation plus courtes nécessitent l'approbation du RSSI avec une acceptation du risque documentée.

### Types de sauvegardes

L'organisation doit sélectionner des stratégies de sauvegarde appropriées en fonction des exigences des systèmes :

| Type de sauvegarde | Description | Cas d'utilisation |
|--------------------|-------------|-------------------|
| **Complète** | Copie intégrale de toutes les données | Sauvegarde de référence ; hebdomadaire ou mensuelle |
| **Incrémentale** | Données modifiées depuis la dernière sauvegarde (quel que soit le type) | Sauvegardes quotidiennes ; rapide, efficace en stockage |
| **Différentielle** | Données modifiées depuis la dernière sauvegarde complète | Sauvegardes quotidiennes ; reprise plus rapide qu'incrémentale |
| **Instantané (snapshot)** | Copie à un moment donné au niveau stockage | Sauvegardes fréquentes ; machines virtuelles et charges de travail cloud |
| **Protection continue des données** | Réplication en temps réel ou quasi réel | Systèmes de niveau 1 nécessitant un OPR < 1 heure |

### Règle de sauvegarde 3-2-1

L'organisation doit mettre en œuvre la règle de sauvegarde 3-2-1 au minimum pour les systèmes de niveau 1 et 2 :

| Élément | Exigence |
|---------|---------|
| **3 copies** | Données originales plus au moins 2 copies de sauvegarde |
| **2 types de supports** | Différentes technologies de stockage (p. ex. disque + cloud, disque + bande) |
| **1 copie hors site** | Emplacement géographiquement séparé (bâtiment, région ou région cloud différent) |

**Sauvegardes immuables** : Pour les systèmes de niveau 1 et 2, au moins une copie de sauvegarde doit être immuable (écriture unique, lecture multiple) ou isolée (air-gapped) pour se protéger contre les rançongiciels et les suppressions accidentelles. Les technologies comprennent le stockage d'objets avec verrou d'objet (p. ex. AWS S3 Object Lock, Azure Immutable Blob Storage ou équivalent), la bande WORM ou les supports hors ligne isolés.

**Conditionnel** : Les organisations soumises à DORA (entités financières de l'UE) doivent mettre en œuvre des copies de sauvegarde immuables lorsque cela est techniquement réalisable (art. 12(4)) et un stockage de sauvegarde hors site à une distance géographique suffisante.

### Sécurité des sauvegardes

- Les sauvegardes doivent être chiffrées tant en transit qu'au repos en utilisant AES-256 ou équivalent, conformément à la Politique d'utilisation de la cryptographie (A.8.24). La solution de sauvegarde (p. ex. Veeam, Commvault, AWS Backup, Azure Backup ou équivalent) doit prendre en charge le chiffrement intégré.
- Les sauvegardes stockées dans des solutions basées sur le cloud doivent au minimum être hébergées chez un prestataire certifié ISO 27001.
- Lorsque la sauvegarde concerne des supports physiques :
  - Les supports doivent être chiffrés.
  - Les supports doivent être étiquetés et stockés de manière sécurisée avec un contrôle d'accès restreint et soumis à autorisation.
  - Le transfert hors site doit utiliser un coursier sécurisé approuvé ou un transfert électronique chiffré.
- Les sauvegardes doivent être protégées au moins au même niveau de sécurité que les données originales.
- **Gestion des clés de chiffrement des sauvegardes** : Les clés de chiffrement doivent être gérées séparément des données de sauvegarde. Les procédures de récupération des clés doivent être documentées et testées (les clés doivent être accessibles lorsque les systèmes principaux sont indisponibles). Les clés doivent être pivotées annuellement ou en cas de compromission suspectée. La mise sous séquestre des clés ou la garde à clé partagée est recommandée pour les sauvegardes de systèmes critiques. La gestion des clés doit être conforme à la Politique d'utilisation de la cryptographie (A.8.24).

### Portabilité des sauvegardes

Pour éviter la dépendance vis-à-vis des fournisseurs, les mises en œuvre de sauvegarde devraient garantir :

- Les sauvegardes sont exportables vers des formats standard du secteur dans la mesure du possible.
- Les sauvegardes cloud sont restorables vers des environnements alternatifs (prestataire cloud différent ou sur site).
- Les procédures de reprise abordent les scénarios de sortie du prestataire.

### Surveillance des sauvegardes

Les opérations de sauvegarde doivent être surveillées :

| Élément | Exigence |
|---------|---------|
| Succès/échec de la sauvegarde | Surveillance en temps réel ; alerte immédiate en cas d'échec pour les systèmes de niveau 1–2 |
| Durée de la sauvegarde | Alerte si la durée dépasse la fenêtre de sauvegarde |
| Capacité de stockage | Avertissement à 70 % d'utilisation ; alerte à 80 % ; critique à 90 % |
| Réplication hors site | Alerte en cas d'échec de réplication |

Les journaux de sauvegarde doivent être produits et vérifiés pour les erreurs et les performances au moins hebdomadairement. Lorsque des erreurs sont trouvées, des mesures correctives doivent être prises et enregistrées.

Des rapports mensuels sur le statut des sauvegardes doivent être fournis au RSSI, incluant la couverture des sauvegardes, les taux de réussite et les problèmes en cours.

### Test et vérification des sauvegardes

Les sauvegardes doivent être régulièrement testées pour garantir qu'elles peuvent être utilisées en cas d'urgence et qu'elles répondent aux besoins des plans de continuité d'activité :

| Niveau du système | Fréquence des tests de restauration | Périmètre du test |
|-------------------|-------------------------------------|-------------------|
| **Niveau 1 (Critique)** | Trimestriel | Restauration complète du système vers un environnement alternatif |
| **Niveau 2 (Élevé)** | Semestriel | Ensembles de données représentatifs ; système complet annuellement |
| **Niveau 3 (Moyen)** | Annuel | Vérification de la restauration par échantillonnage |
| **Niveau 4 (Faible)** | Lors d'un changement significatif | Restauration par échantillonnage ou acceptation du risque documentée |

Chaque test de restauration doit documenter : la date du test, les systèmes testés, la source de sauvegarde, le temps de reprise prévu vs. réel, la vérification de l'intégrité des données, les problèmes rencontrés et la validation par le responsable du test.

**Réponse aux tests échoués** : Les tests de restauration révélant des défaillances de reprise doivent déclencher une escalade basée sur le niveau du système :

| Niveau | Notification | Plan de remédiation | Mises à jour de statut | Escalade |
|--------|-------------|---------------------|----------------------|---------|
| **Niveau 1** | Notification à la direction dans les 4 heures | Dans les 24 heures | Quotidien | Rapporté à la prochaine Révision de management ; les défaillances récurrentes (même système deux fois en 12 mois) déclenchent une révision architecturale |
| **Niveau 2** | Notification au RSSI dans les 24 heures | Dans les 5 jours ouvrables | Hebdomadaire | Rapporté à la prochaine Révision de management |
| **Niveau 3–4** | Mise à jour du registre des risques dans les 10 jours ouvrables | Prochaine fenêtre de maintenance | Mensuel | Révision trimestrielle |

Le nouveau test doit avoir lieu dans les 30 jours suivant la remédiation pour les systèmes de niveau 1–2.

**Conditionnel** : Les organisations soumises à DORA doivent tester la reprise des sauvegardes au moins annuellement (art. 12(6)).

### Procédures de reprise

Les procédures de sauvegarde et de restauration doivent être documentées, maintenues et rendues accessibles (y compris lorsque les systèmes principaux sont indisponibles). Les procédures de reprise pour chaque système critique doivent inclure :

- Processus de restauration étape par étape.
- Identifiants d'accès et autorisation requis.
- Estimation du temps de reprise par rapport à l'objectif OTR (inclure une marge de 25 % pour les complications imprévues).
- Étapes de validation pour confirmer la réussite de la reprise.
- Contacts d'escalade.

### Responsabilités des sauvegardes cloud

Pour les systèmes hébergés dans le cloud, l'organisation doit :

- Comprendre le modèle de responsabilité partagée du prestataire (ce que le prestataire sauvegarde par rapport à ce que le client doit sauvegarder).
- Mettre en œuvre des sauvegardes gérées par le client lorsque les capacités du prestataire ne répondent pas aux exigences d'OPR.
- Tester les procédures d'exportation et de restauration des données SaaS.
- Documenter les procédures de reprise cloud-vers-sur-site pour les scénarios de panne cloud prolongée.

### Alignement des SLA des prestataires cloud

- Les garanties SLA des prestataires cloud doivent être vérifiées par rapport aux exigences d'OTR de l'organisation pour chaque niveau de système.
- La disponibilité historique du prestataire et la performance de réponse aux incidents doivent être documentées lors de l'évaluation des fournisseurs (conformément à A.5.19–23).
- Lorsque le SLA du prestataire est insuffisant pour les systèmes de niveau 1 ou 2, une redondance gérée par le client doit être mise en œuvre.
- Les capacités BC/DR du prestataire (multi-AZ, sauvegarde/restauration, basculement) doivent être documentées.
- Les engagements BC/DR des prestataires cloud doivent être inclus dans l'évaluation des risques fournisseurs.
- Les prestataires devraient maintenir une certification ISO 22301 ou équivalente lorsque disponible.

---

## Redondance des installations de traitement de l'information

### Exigences de redondance par niveau

Les installations de traitement de l'information doivent être mises en œuvre avec une redondance suffisante pour répondre aux exigences de disponibilité :

| Niveau du système | Redondance minimale | Type de basculement | OTR cible |
|-------------------|---------------------|---------------------|-----------|
| **Niveau 1 (Critique)** | Actif-actif ou actif-passif avec basculement automatisé | Automatique | Minutes |
| **Niveau 2 (Élevé)** | Veille chaude ou basculement manuel documenté | Manuel avec procédure | Heures |
| **Niveau 3 (Moyen)** | Veille froide ou reconstruction depuis sauvegarde | Reconstruction | Jours |
| **Niveau 4 (Faible)** | Reprise basée sur les sauvegardes | Restauration | Selon OTR |

**Options d'architecture de redondance** :

- **Actif-actif** : Plusieurs systèmes traitant le trafic simultanément ; la défaillance est gérée par les systèmes restants.
- **Actif-passif** : Le système principal traite le trafic ; le système de veille est prêt pour une activation immédiate en cas de défaillance.
- **Veille chaude** : L'environnement de veille est partiellement provisionné ; nécessite une synchronisation des données avant de devenir opérationnel.
- **Veille froide** : L'infrastructure est disponible mais non provisionnée ; nécessite un provisionnement et une restauration des données.

### Analyse des points de défaillance uniques (SPOF)

Les propriétaires de systèmes doivent conduire une analyse SPOF pour les systèmes de niveau 1 et 2 afin d'identifier les composants dont la défaillance entraînerait une indisponibilité complète du système. Les SPOF courants comprennent :

- Serveur unique sans clustering ou basculement.
- Chemin réseau unique sans connectivité redondante.
- Contrôleur de stockage, alimentation ou onduleur unique.
- Zone de disponibilité cloud ou centre de données unique.
- Serveur DNS ou d'authentification unique.

**Remédiation des SPOF** : Les SPOF identifiés pour les systèmes de niveau 1 doivent être remédiés dans les 90 jours ou disposer d'une acceptation du risque documentée du RSSI. Les SPOF des systèmes de niveau 2 doivent être remédiés dans les 180 jours ou disposer d'une acceptation du risque documentée.

### Tests de basculement

Les systèmes avec redondance doivent avoir leurs mécanismes de basculement testés :

| Niveau du système | Fréquence des tests de basculement |
|-------------------|-----------------------------------|
| **Niveau 1 (Critique)** | Trimestriel (basculement complet en production ou environnement similaire à la production) |
| **Niveau 2 (Élevé)** | Semestriel (test de basculement documenté ou exercice sur table) |
| **Niveau 3 (Moyen)** | Annuel (exercice sur table ou validation des procédures) |

Chaque test de basculement doit documenter : les systèmes testés, le mécanisme de déclenchement du basculement, le temps de basculement réel par rapport à l'objectif OTR, les problèmes identifiés et la validation.

**Tests de retour arrière** : Les tests de basculement doivent également valider le processus de retour arrière (retour vers l'infrastructure principale après reprise). Les procédures de retour arrière doivent être documentées et testées conjointement avec le basculement pour garantir la capacité du cycle de reprise complet.

**Réponse aux tests de basculement échoués** : Les tests révélant une incapacité à atteindre l'OTR doivent déclencher une remédiation immédiate et une évaluation des risques conformément au tableau d'escalade dans Test et vérification des sauvegardes.

### Redondance géographique et réseau

**Redondance géographique** : Pour les systèmes de niveau 1, la redondance doit être mise en œuvre à une distance géographique suffisante pour se protéger contre les catastrophes affectant l'ensemble du site :

| Niveau de distance | Séparation | Protection contre |
|-------------------|-----------|-----------------|
| **Minimum** | Bâtiment ou campus différent | Incidents localisés (incendie, inondation, coupure de courant) |
| **Recommandé** | Ville ou région différente (> 100 km) | Catastrophes régionales |
| **Meilleure pratique** | Zone géographique ou sismique différente | Catastrophes naturelles à grande échelle |

Conseils spécifiques au cloud : Le déploiement multi-AZ (séparation de quelques dizaines de kilomètres) répond au niveau minimum. Le déploiement multi-régional (centaines à milliers de kilomètres) répond au niveau recommandé.

**Redondance réseau** : Les systèmes critiques devraient mettre en œuvre une redondance réseau, notamment des FAI ou prestataires doubles, des commutateurs/routeurs redondants et des pare-feux redondants lorsque l'infrastructure de l'organisation le permet.

**Analyse coût-bénéfice** : Les décisions de redondance doivent équilibrer le coût de l'infrastructure redondante par rapport à l'impact sur l'activité des pannes prolongées et aux exigences réglementaires. Pour de nombreuses PME, la redondance native du cloud (déploiement multi-AZ) fournit une redondance géographique rentable sans maintenir une infrastructure physique séparée.

**Conditionnel** : Les organisations soumises à DORA ou NIS2 devraient mettre en œuvre une redondance géographique pour les systèmes critiques afin de répondre aux exigences de résilience opérationnelle.

---

## Planification de la continuité TIC

### Plans de continuité d'activité

L'organisation doit maintenir des procédures documentées pour répondre à un incident perturbateur et pour poursuivre ou reprendre ses activités dans des délais prédéterminés. Les plans de continuité d'activité doivent aborder les exigences de ceux qui les utiliseront.

**Les plans de continuité d'activité doivent couvrir** :

- Rôles et responsabilités pour les personnes et équipes disposant d'autorité pendant et après un incident.
- Un processus d'activation de la réponse.
- Des détails pour gérer les conséquences immédiates d'un incident perturbateur, en accordant une attention appropriée au bien-être des individus.
- Des options stratégiques, tactiques et opérationnelles pour répondre à la perturbation.
- La prévention de nouvelles pertes ou de l'indisponibilité des activités prioritaires.
- Comment et dans quelles circonstances l'organisation communiquera avec les employés et leurs proches, les principales parties prenantes et les contacts d'urgence.
- Comment l'organisation continuera ou reprendra ses activités prioritaires dans des délais prédéterminés.
- Des détails sur la réponse médiatique de l'organisation à la suite d'un incident, notamment une stratégie de communication, l'interface préférée avec les médias et les lignes directrices pour la rédaction de déclarations aux médias.
- Un processus de désengagement une fois l'incident terminé.

**Chaque plan doit définir** : objet et périmètre, objectifs, critères d'activation et procédures, procédures de mise en œuvre, rôles et autorités, exigences de communication, interdépendances internes et externes, besoins en ressources, et processus de flux d'information et de documentation.

### Plans de reprise TIC

Pour chaque système de niveau 1 et 2, l'organisation doit maintenir des plans de reprise TIC documentant :

1. **Critères d'activation** — Quand activer le plan (processus de déclaration de sinistre).
2. **Équipe de reprise** — Rôles, responsabilités et procédures d'escalade.
3. **Contacts d'urgence** — Équipe de reprise, fournisseurs, parties prenantes.
4. **Procédures de reprise** — Instructions de reprise système étape par étape par ordre de priorité.
5. **Procédures de communication** — Modèles de communication internes et externes.
6. **Priorités de reprise** — Séquence de reprise des systèmes basée sur les dépendances et la classification par niveaux.
7. **Procédures de validation** — Comment vérifier que les systèmes sont opérationnels après la reprise.
8. **Procédures de retour arrière** — Actions si la reprise échoue.

Les plans de reprise doivent être versionnés, révisés annuellement et mis à jour après les exercices de tests, les incidents majeurs ou les changements significatifs de systèmes.

### Processus de déclaration de sinistre

Un sinistre doit être déclaré lorsque :

- Une panne de système de niveau 1 dépasse 50 % de son OTR défini.
- Plusieurs systèmes tombent en panne simultanément.
- Une panne d'infrastructure étendue (centre de données, région cloud, réseau) est confirmée.
- Un incident cyber (rançongiciel, violation de données) empêche les opérations normales.
- La perte ou l'inaccessibilité d'un site physique se produit.

**Hiérarchie d'autorité de déclaration** : L'ingénieur d'astreinte évalue → escalade au Responsable des opérations IT → le RSSI évalue dans les 30 minutes → le PDG/Direction générale autorise la déclaration si nécessaire → les plans BC/DR sont activés et les équipes de reprise sont notifiées.

**Notification d'activation** : Des modèles de notification pré-approuvés doivent être maintenus dans le plan BC/DR. La notification doit être émise via le canal principal (e-mail, plateforme de collaboration) et le canal de sauvegarde (SMS, téléphone) simultanément.

**Escalade incident-à-sinistre** : Tout incident n'est pas un sinistre. La Politique de gestion des incidents (A.5.24–28) régit la réponse initiale aux incidents. L'escalade vers la déclaration de sinistre se produit lorsque la réponse aux incidents détermine qu'une reprise normale dans les délais de l'OTR n'est pas réalisable.

### Programme de tests BC/DR

Les plans de continuité d'activité et les plans de reprise technique doivent être testés au moins annuellement et lors de changements significatifs.

**Types de tests** :

| Type de test | Description | Fréquence |
|-------------|-------------|-----------|
| **Exercice sur table** | Parcours de scénario basé sur la discussion avec le personnel clé | Annuellement (tous les processus critiques) |
| **Test de composant** | Test de reprise de système individuel (restauration de sauvegarde, basculement) | Trimestriel pour le niveau 1 ; semestriel pour le niveau 2 |
| **Test DR complet** | Basculement complet vers le site DR ou l'environnement alternatif | Annuellement pour les systèmes de niveau 1 |

**Test intégré annuel** : Au moins un test BC/DR annuel devrait exercer conjointement la restauration des sauvegardes, l'activation de la redondance, la validation des processus métier et les procédures de communication pour vérifier la capacité de reprise de bout en bout.

**Documentation des tests** : Chaque test doit documenter : la date du test, le périmètre, les objectifs, les participants, le scénario, les résultats (réussite/partiel/échec), l'OTR/OPR réel vs. cible, les problèmes identifiés, les enseignements tirés, les plans d'action et la validation.

**Réponse aux tests échoués** : Les tests révélant une incapacité à atteindre l'OTR/OPR doivent déclencher une investigation immédiate, un plan de remédiation des lacunes, des mesures compensatoires transitoires et une notification à la direction pour les systèmes de niveau 1.

**Conditionnel** : Les organisations soumises à DORA doivent tester les dispositions BC au moins annuellement (art. 11(9)) et tester la sauvegarde TIC et la restauration au moins annuellement (art. 12(6)).

### Formation et sensibilisation BC/DR

| Public | Contenu de la formation | Fréquence |
|--------|------------------------|-----------|
| **Tous les employés** | Sensibilisation BC/DR (responsabilités individuelles, procédures de signalement, canaux de communication, concepts de base) | Annuellement |
| **Membres de l'équipe de reprise** | Formation spécifique au rôle (procédures de reprise, protocoles de communication, utilisation des outils) | Annuellement ; les nouveaux membres sont formés dans les 30 jours suivant leur nomination |
| **Direction générale** | Prise de décision en situation de crise, processus de déclaration de sinistre, gestion des médias | Annuellement (exercice sur table) |

Formation post-test : Les résultats des tests BC/DR et les enseignements tirés doivent être communiqués à tous les participants dans les 30 jours suivant chaque test.

**Objectifs de formation** : 100 % de l'équipe de reprise formée ; 95 % de tous les employés ayant complété la sensibilisation BC/DR.

### Communication de crise

Les plans BC/DR doivent inclure des procédures de communication pour :

**Communication interne** :

- Notification d'activation dans les 30 minutes suivant la déclaration de sinistre (qui est notifié, par quels canaux).
- Mises à jour de statut pendant la reprise à des intervalles définis (horaire pour le niveau 1, toutes les 4 heures pour le niveau 2).
- Notification de « retour à la normale » lorsque la reprise est complète et les systèmes validés.

**Communication externe** :

- Notification des clients (proactive pour les pannes connues affectant le service).
- Coordination fournisseurs/partenaires (si nécessaire pour la reprise).
- Notification réglementaire (si requise — p. ex. notification de violation de données conformément à la nLPD art. 24 ou RGPD art. 33).

**Canaux de communication** : Canaux principaux (e-mail, [Plateforme de collaboration]) ; canaux de sauvegarde (SMS, téléphone) si les canaux principaux sont indisponibles. Les listes de contacts doivent être maintenues, accessibles hors ligne (imprimées ou sur appareils mobiles) et révisées trimestriellement.

### Procédures de reprise

L'organisation doit maintenir des procédures documentées pour restaurer et faire revenir les activités métier des mesures temporaires adoptées pendant un incident aux opérations normales.

**Liste de contrôle de validation de la reprise** : Avant de déclarer un système repris et de revenir aux opérations normales, les éléments suivants doivent être vérifiés :

- Intégrité des données confirmée (sommes de contrôle, comptages d'enregistrements, validation au niveau applicatif).
- Tous les systèmes dépendants et intégrations opérationnels.
- Accès utilisateur restauré et testé.
- Contrôles de sécurité réactivés et vérifiés (EDR, règles de pare-feu, journalisation).
- Performances dans les paramètres acceptables.
- Validation par le propriétaire du système.

### Reprise après rançongiciel

Compte tenu de la prévalence des menaces par rançongiciel, les considérations de reprise spécifiques suivantes viennent compléter le cadre BC/DR général :

**Actions immédiates lors de la détection d'un rançongiciel** :

1. Isoler les systèmes infectés du réseau (ne pas mettre hors tension — préserver les preuves légales).
2. Activer l'équipe de réponse aux incidents conformément à la Politique de gestion des incidents (A.5.24–28).
3. Évaluer l'intégrité des sauvegardes — vérifier que les copies de sauvegarde ne sont pas compromises avant d'initier la restauration.

**Considérations de reprise** :

- Reconstruction depuis des sauvegardes propres vérifiées comme antérieures à l'infection.
- Corriger la vulnérabilité exploitée avant de restaurer les systèmes en production.
- Réinitialiser tous les identifiants (utilisateur, compte de service, administratif) avant de restaurer les accès.
- Mettre en œuvre une surveillance étendue pendant 30–90 jours post-reprise pour détecter les mécanismes de persistance.

**Importance des sauvegardes immuables** : Le stockage WORM, le verrou d'objet ou les supports hors ligne isolés garantissent qu'au moins un point de reprise est immunisé contre le chiffrement par rançongiciel.

**Paiement de rançon** : L'organisation ne doit pas effectuer de paiements de rançon sans approbation explicite de la direction générale et consultation préalable du conseiller juridique et de l'assureur cyber (le cas échéant).

### Signalement des incidents et de la continuité d'activité

Un processus de gestion des incidents doit être en place et suivi. Les incidents de continuité d'activité doivent de plus être :

- Enregistrés et suivis dans un registre.
- Rapportés à l'Équipe de révision de la direction.
- Soumis à une révision post-incident pour capitaliser les enseignements tirés.

---

## Rôles et responsabilités

| Rôle | Responsabilités BC/DR |
|------|----------------------|
| **PDG / Direction générale** | Responsabilité ultime de la continuité d'activité ; approuver la stratégie et le budget BC/DR ; déclarer les sinistres nécessitant l'activation des plans |
| **RSSI** | Propriétaire de la politique BC/DR ; approuver les exigences et les acceptations de risques ; garantir des ressources adéquates ; rapporter le statut BC/DR à la direction générale trimestriellement |
| **Coordinateur BC/DR** | Gestion quotidienne du programme BC/DR ; coordonner le processus AIA ; maintenir les plans de reprise ; planifier et faciliter les tests ; suivre la conformité aux exigences de sauvegarde et de redondance ; gérer le programme de formation BC/DR ; évaluer l'impact des changements sur les plans BC/DR |
| **Administrateurs systèmes / cloud** | Mettre en œuvre et gérer les solutions de sauvegarde ; configurer les mécanismes de redondance et de basculement ; surveiller les travaux de sauvegarde ; participer aux tests BC/DR ; maintenir la documentation de reprise |
| **Propriétaires de systèmes / d'applications** | Définir les exigences OTR/OPR ; contribuer à l'AIA ; approuver les priorités de reprise des systèmes ; valider les systèmes repris ; participer aux tests BC/DR |
| **Tous les employés** | Signaler les incidents de continuité d'activité ; suivre les plans BC pendant les perturbations ; participer à la formation de sensibilisation BC/DR |

---

## Indicateurs et reporting BC/DR

Les indicateurs suivants doivent être suivis pour mesurer l'efficacité du programme BC/DR :

| # | Indicateur | Objectif | Surveillance | Reporting |
|---|-----------|---------|------------|-----------|
| 1 | **Taux de réussite des sauvegardes** | ≥99 % Niveau 1 ; ≥98 % Niveau 2–3 | Quotidien | Mensuel au RSSI |
| 2 | **Réalisation des tests de restauration** | 100 % selon le calendrier | Par test | Trimestriel |
| 3 | **Résultats des tests OTR/OPR** | 100 % Niveau 1 dans les délais ; ≥95 % Niveau 2 | Par test | Tendance trimestrielle |
| 4 | **Réalisation des tests de basculement** | 100 % selon le calendrier | Par test | Trimestriel |
| 5 | **Actualité des plans BC/DR** | 100 % révisés dans le cycle annuel | Trimestriel | Trimestriel |
| 6 | **Remédiation des SPOF** | ≥90 % remédiés ou acceptés selon les délais | Trimestriel | Trimestriel |
| 7 | **Formation de l'équipe de reprise** | 100 % formés | Annuellement | Annuellement |

Les indicateurs dépassant les cibles pendant deux périodes de reporting consécutives doivent être escaladés au RSSI et rapportés à la prochaine Révision de management.

---

## Preuves

Les preuves suivantes démontrent la conformité à cette politique :

| # | Preuve | Responsable | Fréquence |
|---|--------|-------------|-----------|
| 1 | **Analyse d'impact sur l'activité** avec niveaux de criticité des systèmes, OPR/OTR et cartographie des dépendances | Coordinateur BC/DR / RSSI | *Révision annuelle ; mise à jour lors de changements significatifs ; conservée 5 ans* |
| 2 | **Inventaire des sauvegardes** (systèmes sauvegardés, type de sauvegarde, fréquence, conservation, statut hors site) | Administrateurs systèmes | *Maintenu en continu ; révisé trimestriellement ; conservé 3 ans* |
| 3 | **Journaux de surveillance des sauvegardes et rapports** (taux de réussite/échec, enregistrements de résolution des erreurs) | Administrateurs systèmes | *Vérifications hebdomadaires des journaux ; rapports mensuels au RSSI ; conservés 12 mois* |
| 4 | **Résultats des tests de restauration des sauvegardes** (date du test, systèmes, OTR/OPR réel vs. cible, vérification de l'intégrité des données) | Coordinateur BC/DR | *Selon le calendrier (trimestriel à annuel par niveau) ; conservés 3 ans* |
| 5 | **Analyse SPOF** pour les systèmes de niveau 1 et 2 avec statut de remédiation | Propriétaires de systèmes | *Révision annuelle ; mise à jour lors de changements d'infrastructure ; conservée 3 ans* |
| 6 | **Résultats des tests de basculement** (temps de basculement, problèmes, validation) | Coordinateur BC/DR | *Selon le calendrier (trimestriel à annuel par niveau) ; conservés 3 ans* |
| 7 | **Plans BC/DR** (plans de continuité d'activité et plans de reprise TIC, versions actuelles) | Coordinateur BC/DR / RSSI | *Révision annuelle ; mise à jour après tests et incidents ; versions actuelle + 2 précédentes conservées* |
| 8 | **Enregistrements des tests BC/DR** (exercices sur table, tests de composants, tests DR complets avec scénarios et résultats) | Coordinateur BC/DR | *Annuel au minimum ; conservés 3 ans* |
| 9 | **Registre des exceptions** (systèmes ne répondant pas aux OPR/OTR, acceptations de risques, mesures compensatoires) | RSSI | *Par événement ; révisé trimestriellement ; conservé 5 ans* |
| 10 | **Listes de contacts pour la communication de crise** (équipe interne, contacts externes, contacts fournisseurs, disponibles hors ligne) | Coordinateur BC/DR | *Révisées trimestriellement ; mises à jour lors de tout changement* |
| 11 | **Enregistrements de formation BC/DR** (taux de réalisation de la formation de l'équipe de reprise, taux de sensibilisation annuelle) | Coordinateur BC/DR | *Annuellement ; conservés 3 ans* |
| 12 | **Rapports d'indicateurs BC/DR** (taux de réussite des sauvegardes, réalisation des tests, tendances d'actualité des plans) | Coordinateur BC/DR | *Mensuel au RSSI ; rapports de tendance trimestriels ; conservés 3 ans* |
| 13 | **Documentation SLA et capacités BC/DR des prestataires cloud** (garanties SLA, modèle de responsabilité partagée, vérification d'alignement BC/DR) | Propriétaires de systèmes / Administrateurs cloud | *Révisée annuellement et lors du renouvellement du contrat ; conservée 3 ans* |

---

# Conformité à la politique

## Mesure de la conformité

L'équipe de management de la sécurité de l'information vérifiera la conformité à cette politique par diverses méthodes, notamment, sans s'y limiter, les rapports de surveillance des sauvegardes, les enregistrements des tests de restauration, les résultats des tests BC/DR, les rapports d'analyse SPOF, les audits internes et externes, ainsi que les retours d'information au propriétaire de la politique.

## Exceptions

Toute exception à cette politique (p. ex. système exclu des sauvegardes, redondance non mise en œuvre, OPR/OTR non atteints) doit être approuvée et enregistrée à l'avance par le Responsable de la sécurité de l'information, avec une acceptation du risque documentée, des mesures compensatoires et une date de révision définie (12 mois maximum, renouvelable). Les exceptions doivent être rapportées à l'Équipe de révision de la direction.

## Non-conformité

Un employé reconnu coupable d'avoir violé cette politique peut faire l'objet de mesures disciplinaires pouvant aller jusqu'au licenciement.

## Amélioration continue

Cette politique est révisée et mise à jour dans le cadre du processus d'amélioration continue. Les révisions doivent prendre en compte les évolutions des opérations métier, de l'infrastructure technologique, des exigences réglementaires, les enseignements tirés des tests BC/DR et des incidents réels, les résultats des audits, les menaces émergentes (p. ex. rançongiciels, perturbations de la chaîne d'approvisionnement), les évaluations des menaces environnementales et la prévision des capacités pour l'infrastructure de sauvegarde et DR.

L'organisation s'engage dans le développement et l'amélioration continue du processus, des plans et du système de continuité d'activité.

---

# Domaines de la norme ISO 27001 couverts

Politique de continuité d'activité et de reprise après sinistre — Cartographie des contrôles ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership et engagement | 5.1 Politiques de sécurité de l'information |
| Clause 5.2 Politique | 5.4 Responsabilités de la direction |
| Clause 6.2 Objectifs de sécurité de l'information | 5.29 Sécurité de l'information lors d'une perturbation |
| Clause 7.3 Sensibilisation | **5.30 Préparation TIC pour la continuité d'activité** |
| Clause 8.1 Planification et contrôle opérationnels | 5.36 Conformité aux politiques, règles et normes |
| | 6.3 Sensibilisation, éducation et formation à la sécurité de l'information |
| | 6.4 Processus disciplinaire |
| | **8.13 Sauvegarde des informations** |
| | **8.14 Redondance des installations de traitement de l'information** |

**Cadre réglementaire et légal** :

| Cadre | Pertinence |
|-------|-----------|
| nLPD suisse (revDSG) | Art. 8 — Mesures techniques et organisationnelles incluant la protection de la disponibilité et la capacité de récupération des données |
| OPDo suisse (Ordonnance sur la protection des données) | Art. 1–3 — Exigences minimales en matière de sécurité des données |
| RGPD de l'UE (le cas échéant) | Art. 32(1)(c) — Capacité à rétablir la disponibilité et l'accès aux données personnelles dans les meilleurs délais |
| ISO/IEC 27001:2022 | Contrôles Annexe A 5.30 (Préparation TIC), 8.13 (Sauvegarde des informations), 8.14 (Redondance) |
| ISO/IEC 27002:2022 | Sections 5.30, 8.13, 8.14 — Lignes directrices de mise en œuvre |
| ISO/IEC 22301 | Systèmes de management de la continuité d'activité (référence informative) |
| NIST SP 800-34 Rev 1 | Guide de planification des mesures d'urgence (référence informative) |
| CIS Controls v8 | Contrôle 11 (Reprise des données) |
| DORA (conditionnel) | Art. 11–12 — Continuité d'activité TIC, politiques de sauvegarde, plans de reprise après sinistre, tests annuels |
| NIS2 (conditionnel) | Art. 21 — Continuité d'activité et gestion de crise, gestion des sauvegardes |
| FINMA (conditionnel) | Management de la continuité d'activité pour les établissements financiers suisses |

---

<!-- QA_VERIFIED: 2026-03-29 -->
