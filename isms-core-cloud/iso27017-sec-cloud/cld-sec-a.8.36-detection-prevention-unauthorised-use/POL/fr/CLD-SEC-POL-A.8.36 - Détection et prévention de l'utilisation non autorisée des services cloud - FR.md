<!-- ISMS-CORE:POLICY:CLD-SEC-POL-A.8.36-FR:sec:POL:a.8.36 -->
**CLD-SEC-POL-A.8.36 — Détection et prévention de l'utilisation non autorisée des services cloud**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Détection et prévention de l'utilisation non autorisée des services cloud |
| **Type de document** | Politique |
| **Identifiant du document** | CLD-SEC-POL-A.8.36 |
| **Auteur du document** | RSSI / Responsable Sécurité Cloud |
| **Propriétaire du document** | RSSI |
| **Approuvé par** | Direction générale |
| **Date de création** | [Date à définir] |
| **Version** | 1.0 |
| **Date de version** | [Date à définir] |
| **Classification** | Interne |
| **Statut** | Brouillon |
| **Version du produit Cloud** | 1.0 |

**Historique des versions** :

| Version | Date | Auteur | Modifications |
|---------|------|--------|---------------|
| 1.0 | [Date à définir] | RSSI | Politique initiale pour la mise en œuvre d'ISO/IEC 27017:2026 Éd. 2 |

**Cycle de révision** : Annuel (ou lors d'un changement significatif de la capacité de surveillance de l'utilisation du cloud, ou à la suite d'un incident confirmé d'utilisation non autorisée)
**Prochaine date de révision** : [Date d'entrée en vigueur + 12 mois]

**Chaîne d'approbation** :

- Principale : RSSI
- Secondaire : Responsable Sécurité Cloud
- Technique : Responsable des Opérations de Sécurité
- Autorité finale : Direction générale

**Documents connexes** :

- ISMS-POL-A.8.16 (Activités de surveillance — politique SGSI parente)
- CLD-SEC-POL-A.5.38 (Rôles et responsabilités partagés au sein d'un environnement d'informatique en nuage)
- CLD-SEC-POL-A.8.35 (Séparation dans les environnements d'informatique virtuelle)
- CLD-SEC-IMP-A.8.36-TG (Détection et prévention de l'utilisation non autorisée des services cloud — Guide technique, contient les schémas complets de surveillance)
- CLD-SEC-REF-A.5-A.8 (Addendum de guidance sur la sécurité cloud)
- ISO/IEC 27017:2026, Clause 8.36 (CLD — Détection et prévention de l'utilisation non autorisée des services cloud)
- ISO/IEC 19086 (toutes parties) (Informatique en nuage — Cadre relatif aux accords de niveau de service)

---

## Résumé exécutif

Cette politique établit la manière dont [Organisation] surveille l'activité des utilisateurs de services cloud (CSU) afin de détecter et de prévenir les accès non autorisés, les transferts de données non intentionnels et toute autre activité non autorisée sur les services cloud, conformément à ISO/IEC 27017:2026, Clause 8.36.

**Périmètre** : Tous les services cloud que [Organisation] gère en tant que client de service cloud (CSC), y compris la surveillance des propres utilisateurs de services cloud de [Organisation] ; et tous les services cloud que [Organisation] fournit en tant que fournisseur de service cloud (CSP), y compris les orientations et fonctions de surveillance fournies aux CSC.

**Note sur les contrôles étendus** : ISO/IEC 27017:2026, Clause 8.36 est l'un des quatre contrôles étendus spécifiques au cloud « CLD » introduits par la deuxième édition de la norme (aux côtés des clauses 5.38, 5.39 et 8.35). Il est entièrement nouveau — il n'a pas d'équivalent dans la première édition de 2015 d'ISO/IEC 27017 ni d'équivalent direct dans ISO/IEC 27002:2022. [Organisation] le met en œuvre comme une extension informative de son SGSI fondé sur ISO/IEC 27001:2022, aux côtés du contrôle 8.16 de l'Annex A (Activités de surveillance).

**Risque fondamental** : Les services cloud sont faciles à provisionner et faciles à détourner — un seul CSU peut créer une infrastructure fantôme, exfiltrer des données via un service autorisé d'une manière non autorisée, ou dépasser l'accès prévu sans déclencher les contrôles de périmètre réseau classiques. La détection repose sur la surveillance des schémas d'utilisation, et non uniquement sur la surveillance des attaques externes. Toute instance confirmée d'utilisation non autorisée d'un service cloud est traitée comme un incident de sécurité de l'information, escaladée et investiguée selon le processus de gestion des incidents de [Organisation] — et non simplement consignée puis clôturée.

---

# Périmètre et applicabilité

## ISO/IEC 27017:2026 — Clause 8.36

**Énoncé du contrôle (ISO/IEC 27017:2026, 8.36) :**
> « L'utilisation des services cloud par les CSU devrait être surveillée afin de prévenir les accès non autorisés, les transferts de données et autres activités non autorisées sur les services cloud. »

**Finalité (ISO/IEC 27017:2026, 8.36) :**
> « Permettre la surveillance et la prévention de l'utilisation non intentionnelle des services cloud et du transfert non intentionnel de données à destination et en provenance des services cloud. »

*(Traduction de travail établie à partir du texte anglais original de la norme, à des fins de lisibilité ; en cas de divergence, le texte anglais officiel d'ISO/IEC 27017:2026 fait foi.)*

## Applicabilité

Cette politique s'applique à :

- Tous les utilisateurs de services cloud (CSU) au sein de [Organisation] qui accèdent à des services cloud pour le compte de [Organisation], en tant que CSC
- Tous les services cloud que [Organisation] fournit à ses propres CSC, en tant que CSP, s'agissant des orientations et fonctions de surveillance que [Organisation] doit fournir
- Tous les processus de gestion des événements de sécurité de l'information intégrant des données d'utilisation des services cloud

## Cadre réglementaire et normatif

ISO/IEC 27017:2026 est une extension informative d'ISO/IEC 27002:2022. La clause 8.36 ne correspond à aucun contrôle numéroté d'ISO/IEC 27002:2022 ; elle est nouvelle dans la deuxième édition de 2026, sans équivalent même dans la première édition de 2015 d'ISO/IEC 27017. Elle est mise en œuvre parallèlement au contrôle 8.16 de l'Annex A d'ISO/IEC 27001:2022 (Activités de surveillance), et s'appuie sur les orientations relatives aux accords de niveau de service de la série ISO/IEC 19086 lorsque les conditions du SLA cloud régissent les données de surveillance disponibles pour [Organisation].

---

# Dispositions de la politique : Détection et prévention de l'utilisation non autorisée du cloud (8.36)

## Détermination du périmètre fondée sur le risque

Avant de mettre en œuvre la surveillance pour un service cloud donné, [Organisation] DOIT :

- Confirmer la classification des données du service (Public / Interne / Confidentiel / Restreint), en utilisant la déclaration des exigences de séparation (CLD-SEC-IMP-A.8.35-TG, Section 1) lorsqu'elle existe déjà pour le service
- Appliquer la surveillance de l'activité des CSU comme référence obligatoire pour les services cloud classés Confidentiel ou Restreint
- Pour les services classés Public ou Interne, préparer une recommandation fondée sur le risque (surveiller ou non, et pourquoi) pour approbation par le RSSI, et consigner la décision — la surveillance n'est pas omise par défaut, il s'agit d'une décision documentée

## Obligations en tant que client de service cloud (CSC)

Lorsque [Organisation] agit en tant que client de service cloud, [Organisation] DOIT, pour chaque service cloud relevant du périmètre :

- Mettre en œuvre la surveillance des activités des CSU, en capturant au minimum les événements d'authentification, le provisionnement/déprovisionnement des ressources, l'accès aux données et les changements de configuration, acheminés vers la capacité centrale de surveillance de la sécurité de [Organisation] conformément à ISMS-POL-A.8.16 lorsque cela est possible
- Réaliser une revue technique de conformité périodique au regard de la politique de sécurité de l'information de [Organisation], de sa politique spécifique sur l'utilisation des services cloud, et des règles et normes applicables — au minimum annuellement pour les services Confidentiel ou Restreint — les constats de non-conformité étant escaladés au Responsable Sécurité Cloud pour le suivi de la remédiation
- Surveiller et prévenir tout transfert d'informations non intentionnel ou non autorisé à destination et en provenance de l'environnement de service cloud géré par [Organisation], à l'aide des contrôles techniques disponibles (par ex. intégration de prévention des pertes de données, paramètres de partage restreints, surveillance des flux sortants)
- Établir une référence d'utilisation normale du service cloud pour chaque service surveillé, et détecter les anomalies — telles qu'une augmentation de l'utilisation des ressources ou une utilisation de service inconnue — en identifiant les écarts par rapport à cette référence
- Investiguer chaque alerte d'anomalie déclenchée et consigner sa qualification (faux positif, utilisation non autorisée confirmée, remédiée, escaladée vers la réponse aux incidents) ; traiter tout constat d'utilisation non autorisée confirmée comme un incident de sécurité de l'information

## Obligations en tant que fournisseur de service cloud (CSP)

Lorsque [Organisation] agit en tant que fournisseur de service cloud, [Organisation] DOIT :

- Fournir aux CSC des orientations et des fonctions leur permettant de surveiller et de contrôler l'utilisation par leurs CSU du service cloud fourni par [Organisation] — en documentant quelles données d'activité sont exposées, comment les CSC peuvent y accéder, et comment configurer les éventuelles fonctions de surveillance paramétrables (par ex. seuils d'alerte personnalisés)
- Maintenir ces orientations de surveillance destinées aux CSC à jour à mesure que le service évolue, en les révisant au minimum lors de la révision annuelle de la politique

## Communication et sensibilisation

[Organisation] DOIT communiquer le périmètre de surveillance, les responsabilités des CSU, les règles d'utilisation acceptable, et la manière de signaler toute suspicion d'utilisation non autorisée aux CSU internes et aux équipes concernées, par le biais du programme de sensibilisation à la sécurité de l'information de l'organisation (voir ISMS-POL-A.6.3) et des supports d'intégration propres au service. Lorsque [Organisation] agit en tant que CSP, les informations équivalentes DOIVENT être communiquées aux CSU des clients par le biais des orientations de surveillance publiées destinées aux CSC.

## Journal des décisions de périmètre de surveillance — Contenu minimal

Le journal des décisions de périmètre de surveillance (schéma complet dans CLD-SEC-IMP-A.8.36-TG, Section 1) DOIT consigner, par service cloud : l'identifiant du service ; sa classification des données ; la décision de surveillance (obligatoire, fondée sur le risque et mise en œuvre, ou fondée sur le risque et non mise en œuvre) ; la justification et, le cas échéant, l'approbation du RSSI ; et la date de la dernière révision.

---

# Rôles et responsabilités

| Rôle | Responsabilités |
|------|-----------------|
| **RSSI** | Est propriétaire de CLD-SEC-POL-A.8.36 ; approuve la détermination fondée sur le risque du périmètre de surveillance pour les services cloud de classification inférieure ; examine les escalades d'anomalies ayant un impact à l'échelle de l'organisation ; est responsable des incidents confirmés d'utilisation non autorisée via le processus de gestion des incidents de [Organisation] |
| **Responsable des Opérations de Sécurité** | Met en œuvre et exploite la surveillance de l'activité des CSU, la revue technique de conformité et la détection d'anomalies (rôle CSC) ; rapporte au RSSI les indicateurs de couverture de surveillance et d'anomalies |
| **Responsable Sécurité Cloud** | S'assure que les orientations et fonctions de surveillance destinées aux CSC sont documentées et disponibles lorsque [Organisation] est CSP ; consigne les décisions de détermination du périmètre fondées sur le risque |
| **Prestation de services cloud / Ingénierie** | Configure les capacités de surveillance des services cloud ; répond à tout transfert d'informations non intentionnel ou non autorisé détecté |
| **Tout le personnel (en tant que CSU)** | N'utilise les services cloud que dans le périmètre autorisé ; signale toute suspicion d'utilisation non autorisée observée |

---

# Exigences en matière de preuves

| Preuve | Description | Propriétaire | Conservation |
|-------|-------------|-------------|-------------|
| Journal des décisions de périmètre de surveillance | Décisions fondées sur le risque approuvées par le RSSI pour les services Public/Interne où la surveillance n'est pas mise en œuvre | Responsable Sécurité Cloud | En cours + 3 ans |
| Configuration de surveillance de l'activité des CSU | Documentation du périmètre et des mécanismes de surveillance par service cloud (rôle CSC) | Responsable des Opérations de Sécurité | Version actuelle + versions précédentes pendant 3 ans |
| Registres de revue technique de conformité | Registres des revues périodiques au regard de la politique de sécurité de l'information, de la politique d'utilisation du cloud et des normes | Responsable des Opérations de Sécurité | En cours + 3 ans |
| Journal de détection d'anomalies | Journal des anomalies détectées (utilisation inattendue des ressources, utilisation de service inconnue) et de leur qualification | Responsable des Opérations de Sécurité | En cours + 3 ans |
| Registres d'utilisation non autorisée confirmée / d'incidents | Registres des anomalies confirmées comme utilisation non autorisée, corrélées au processus de gestion des incidents | RSSI | En cours + 3 ans |
| Orientations de surveillance destinées aux CSC (rôle CSP) | Documentation et fonctions fournies aux CSC pour surveiller et contrôler l'utilisation par leurs propres CSU | Responsable Sécurité Cloud | Version actuelle + versions précédentes pendant 3 ans |

---

# Suivi et indicateurs

Le Responsable des Opérations de Sécurité rapporte au RSSI, au moins trimestriellement :

- La proportion des services cloud Confidentiel/Restreint disposant d'une surveillance active des CSU
- Le nombre d'anomalies détectées, avec la répartition de leur qualification (faux positif / utilisation non autorisée confirmée / remédiée / escaladée)
- Le nombre de constats de revue technique de conformité et leur statut de remédiation
- Le délai entre la détection d'une anomalie et sa qualification, pour les anomalies confirmées comme utilisation non autorisée

---

# Considérations d'audit

Les auditeurs vérifiant la conformité à CLD-SEC-POL-A.8.36 doivent s'attendre à trouver :

- Un périmètre de surveillance de l'activité des CSU documenté pour chaque service cloud classé Confidentiel ou Restreint
- Des preuves de la revue technique de conformité périodique au regard de la politique de sécurité de l'information et de la politique d'utilisation du cloud
- Un journal de détection d'anomalies démontrant une revue active et un suivi de la qualification, et non une simple collecte passive de journaux
- Pour les services où [Organisation] est CSP, des orientations et fonctions de surveillance publiées et mises à disposition des CSC
- Une approbation documentée du RSSI lorsque la surveillance a été réduite sur la base du risque pour des services de classification inférieure
- Des preuves que les constats d'utilisation non autorisée confirmée ont été traités via le processus de gestion des incidents de [Organisation], avec un enregistrement du délai jusqu'à la qualification

---

<!-- QA_VERIFIED: 2026-08-01 -->
