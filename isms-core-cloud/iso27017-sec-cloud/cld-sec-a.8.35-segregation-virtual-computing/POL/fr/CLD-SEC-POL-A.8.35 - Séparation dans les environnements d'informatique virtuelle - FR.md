<!-- ISMS-CORE:POLICY:CLD-SEC-POL-A.8.35-FR:sec:POL:a.8.35 -->
**CLD-SEC-POL-A.8.35 — Séparation dans les environnements d'informatique virtuelle**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Séparation dans les environnements d'informatique virtuelle |
| **Type de document** | Politique |
| **Identifiant du document** | CLD-SEC-POL-A.8.35 |
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

**Cycle de révision** : Annuel (ou lors d'un changement significatif de l'architecture de virtualisation, ou à la suite d'un incident lié à la séparation)
**Prochaine date de révision** : [Date d'entrée en vigueur + 12 mois]

**Chaîne d'approbation** :

- Principale : RSSI
- Secondaire : Responsable Sécurité Cloud
- Technique : Responsable Ingénierie Cloud
- Autorité finale : Direction générale

**Documents connexes** :

- ISMS-POL-A.8.20-22 (Sécurité réseau — politique SGSI parente pour la séparation des réseaux A.8.22)
- CLD-SEC-POL-A.5.38 (Rôles et responsabilités partagés au sein d'un environnement d'informatique en nuage)
- CLD-SEC-POL-A.8.36 (Détection et prévention de l'utilisation non autorisée des services cloud)
- CLD-SEC-IMP-A.8.35-TG (Séparation dans les environnements d'informatique virtuelle — Guide technique, contient les schémas complets de séparation et le modèle d'architecture)
- CLD-SEC-REF-A.5-A.8 (Addendum de guidance sur la sécurité cloud)
- ISO/IEC 27017:2026, Clause 8.35 (CLD — Séparation dans les environnements d'informatique virtuelle)
- ISO/IEC 27040 (Sécurité du stockage)

---

## Résumé exécutif

Cette politique établit la manière dont [Organisation] protège les environnements des locataires contre les accès non autorisés au sein des environnements d'informatique virtuelle multi-locataires, conformément à ISO/IEC 27017:2026, Clause 8.35.

**Périmètre** : Tous les environnements d'informatique virtuelle dans lesquels [Organisation] opère au sein d'un service cloud multi-locataires — que ce soit le propre environnement virtuel de [Organisation] s'exécutant sur le service cloud d'un CSP tiers (rôle CSC), ou l'infrastructure multi-locataires que [Organisation] exploite pour ses propres CSC (rôle CSP).

**Note sur les contrôles étendus** : ISO/IEC 27017:2026, Clause 8.35 est l'un des quatre contrôles étendus spécifiques au cloud « CLD » introduits par la deuxième édition de la norme (aux côtés des clauses 5.38, 5.39 et 8.36). Il est thématiquement le plus proche — et mis en œuvre parallèlement — des obligations de séparation des réseaux du contrôle 8.22 de l'Annex A d'ISO/IEC 27001:2022, mais traite spécifiquement de la séparation logique des applications virtualisées, du stockage et des ressources réseau, et non uniquement du trafic réseau.

**Risque fondamental** : Une séparation inadéquate dans un environnement d'informatique virtuelle partagé peut exposer les données ou charges de travail d'un locataire à un autre locataire, à des tiers, ou à du personnel non autorisé du CSP. L'isolation des locataires étant largement invisible pour le CSC, [Organisation] doit définir explicitement ses exigences de séparation (en tant que CSC) et appliquer rigoureusement la séparation logique (en tant que CSP), plutôt que de présumer que l'isolation est automatiquement adéquate. Un écart de séparation identifié à quelque moment que ce soit — lors de l'intégration, de la vérification périodique ou des tests — est traité comme un risque de sécurité de l'information nécessitant une évaluation, et non comme une note de configuration à revoir ultérieurement.

---

# Périmètre et applicabilité

## ISO/IEC 27017:2026 — Clause 8.35

**Énoncé du contrôle (ISO/IEC 27017:2026, 8.35) :**
> « L'environnement virtuel d'un CSC s'exécutant sur un service cloud devrait être protégé contre les accès non autorisés. »

**Finalité (ISO/IEC 27017:2026, 8.35) :**
> « Empêcher tout accès inapproprié ou toute divulgation d'informations résultant d'une virtualisation non sécurisée. »

*(Traduction de travail établie à partir du texte anglais original de la norme, à des fins de lisibilité ; en cas de divergence, le texte anglais officiel d'ISO/IEC 27017:2026 fait foi.)*

## Applicabilité

Cette politique s'applique à :

- Toutes les instances de machines virtuelles, conteneurs, volumes de stockage et réseaux virtuels de [Organisation] s'exécutant sur le service cloud multi-locataires d'un CSP tiers (rôle CSC)
- Toute l'infrastructure virtualisée multi-locataires que [Organisation] exploite pour fournir des services cloud à ses propres CSC (rôle CSP)
- Tout le personnel disposant d'un accès administratif aux couches de virtualisation, d'hyperviseur ou d'orchestration de conteneurs

## Cadre réglementaire et normatif

ISO/IEC 27017:2026 est une extension informative d'ISO/IEC 27002:2022. La clause 8.35 ne correspond à aucun contrôle numéroté d'ISO/IEC 27002:2022 ; elle est nouvelle dans la deuxième édition de 2026, remplaçant et élargissant le CLD.9.5.1 de la première édition de 2015 (« Séparation dans les environnements d'informatique virtuelle »). Elle est mise en œuvre parallèlement au contrôle 8.22 de l'Annex A d'ISO/IEC 27001:2022 (Séparation des réseaux) et s'appuie sur les orientations relatives à la sécurité de la multi-location fournies par ISO/IEC 27040.

---

# Dispositions de la politique : Séparation dans les environnements d'informatique virtuelle (8.35)

## Obligations en tant que client de service cloud (CSC)

Lorsque [Organisation] agit en tant que client de service cloud, [Organisation] DOIT :

- Classer les données et la charge de travail à exécuter sur le service cloud selon leur sensibilité, et définir ses exigences de séparation de l'environnement de [Organisation] afin d'assurer l'isolation des locataires, avant la sélection du service
- Fixer un niveau d'isolation minimal acceptable adapté à cette classification (par ex. isolation logique imposée par l'hyperviseur pour les charges de travail standard, infrastructure dédiée/mono-locataire pour les charges de travail les plus sensibles), et le documenter dans la déclaration des exigences de séparation (schéma dans CLD-SEC-IMP-A.8.35-TG, Section 1)
- Vérifier, avant et périodiquement pendant l'utilisation du service, que le CSP satisfait à ces exigences de séparation, en utilisant la documentation du CSP recoupée avec des assurances indépendantes (certifications, rapports d'audit) lorsqu'elles sont disponibles
- Effectuer une nouvelle vérification au moins une fois par an, et chaque fois que le CSP annonce un changement significatif de son architecture de virtualisation ou de multi-location
- Lorsque la vérification identifie un écart entre les contrôles de séparation du CSP et l'exigence énoncée par [Organisation], le traiter comme un risque de sécurité de l'information et l'intégrer au processus documenté d'appréciation et de traitement des risques de [Organisation]

## Obligations en tant que fournisseur de service cloud (CSP)

Lorsque [Organisation] agit en tant que fournisseur de service cloud, [Organisation] DOIT :

- Appliquer la séparation logique des données des CSC, des applications virtualisées, des systèmes d'exploitation, du stockage et des ressources réseau, afin d'assurer l'isolation des ressources utilisées par différents locataires dans un environnement multi-locataires, documentée par couche dans la documentation d'architecture de séparation (modèle dans CLD-SEC-IMP-A.8.35-TG, Section 3)
- Évaluer les risques associés à l'exécution de logiciels fournis par les CSC au sein des services cloud proposés par [Organisation], avant d'autoriser l'exécution de tels logiciels dans une infrastructure partagée, en appliquant des contrôles compensatoires lorsque la frontière d'isolation est jugée insuffisante
- Appliquer la séparation des fonctions d'administration interne propres à [Organisation] par rapport aux ressources utilisées par les CSC, au moyen d'un chemin d'accès administratif distinct
- Planifier des tests périodiques de l'architecture de séparation (par ex. tests d'intrusion aux frontières des locataires, audits de configuration de l'isolation des hyperviseurs/conteneurs) pour confirmer que la conception documentée demeure efficace en pratique, et pas seulement correcte sur le papier

## Mise en œuvre dépendante de la technologie

[Organisation] reconnaît que la mise en œuvre de la séparation logique dépend des technologies de virtualisation appliquées. Les configurations réseau et de stockage peuvent être virtualisées via une fonction de virtualisation logicielle fournissant un environnement virtuel (par exemple, un système d'exploitation virtuel ou un mécanisme d'isolation de conteneurs). Lorsqu'une telle virtualisation logicielle est utilisée, [Organisation] DOIT concevoir et mettre en œuvre la séparation à l'aide des fonctions de séparation natives de ce logiciel, en complément des contrôles physiques ou de niveau réseau sous-jacents.

## Considérations juridiques et réglementaires

Lorsque des lois ou réglementations applicables exigent la séparation des réseaux ou l'isolation du trafic réseau pour les données que [Organisation] traite, [Organisation] DOIT s'assurer que ses contrôles de séparation en informatique virtuelle satisfont à ces exigences en complément des exigences de base de cette politique, et le confirmer dans le cadre de la révision annuelle.

## Communication et sensibilisation

[Organisation] DOIT communiquer les exigences de séparation et les décisions d'architecture aux équipes internes qui les conçoivent, les exploitent ou s'appuient sur elles (Ingénierie Cloud, Prestation de services cloud, Opérations de sécurité), au moyen de la documentation d'architecture de séparation et de leur intégration au programme de sensibilisation à la sécurité de l'information de l'organisation (voir ISMS-POL-A.6.3). Lorsque [Organisation] agit en tant que CSP, les engagements de séparation clés pertinents pour un CSC DOIVENT être communiqués à ce CSC par le biais des supports d'intégration ou de la documentation de service.

## Déclaration des exigences de séparation — Contenu minimal

La déclaration des exigences de séparation (schéma complet dans CLD-SEC-IMP-A.8.35-TG, Section 1) DOIT consigner, par service cloud consommé : l'identifiant du service ; la classification des données/de la charge de travail ; le niveau d'isolation minimal acceptable et sa justification ; et la date à laquelle l'exigence a été définie.

## Documentation d'architecture de séparation — Contenu minimal

La documentation d'architecture de séparation (modèle complet dans CLD-SEC-IMP-A.8.35-TG, Section 3) DOIT consigner, par environnement multi-locataires exploité par [Organisation] : le mécanisme de séparation appliqué à chaque couche (données des CSC, applications virtualisées, systèmes d'exploitation, stockage, réseau) ; la conception de la séparation de l'administration interne ; et un résumé des tests de séparation les plus récents et de leurs résultats.

---

# Rôles et responsabilités

| Rôle | Responsabilités |
|------|-----------------|
| **RSSI** | Est propriétaire de CLD-SEC-POL-A.8.35 ; approuve l'architecture de séparation des environnements multi-locataires exploités par [Organisation] (rôle CSP) ; approuve l'acceptation des contrôles de séparation d'un CSP pour les charges de travail critiques (rôle CSC) ; examine les escalades de risques liées à la séparation |
| **Responsable Sécurité Cloud** | Définit les exigences de séparation pour les services consommés (rôle CSC) ; vérifie périodiquement les contrôles de séparation du CSP ; rapporte au RSSI les indicateurs de vérification et de tests de séparation |
| **Responsable Ingénierie Cloud** | Conçoit et met en œuvre les contrôles de séparation logique (hyperviseur, conteneur, stockage, réseau) pour les environnements multi-locataires exploités par [Organisation] (rôle CSP) ; planifie et examine les tests de séparation périodiques |
| **Prestation de services cloud / Ingénierie** | Évalue le risque des logiciels fournis par les CSC avant d'en autoriser l'exécution dans une infrastructure partagée ; maintient la séparation de l'accès d'administration interne par rapport aux ressources des CSC |

---

# Exigences en matière de preuves

| Preuve | Description | Propriétaire | Conservation |
|-------|-------------|-------------|-------------|
| Déclaration des exigences de séparation (rôle CSC) | Exigences d'isolation des locataires documentées par [Organisation] pour chaque service cloud consommé | Responsable Sécurité Cloud | En cours + 3 ans |
| Registres de vérification de séparation du CSP | Registres de la vérification périodique attestant que les contrôles de séparation d'un CSP satisfont aux exigences de [Organisation] | Responsable Sécurité Cloud | En cours + 3 ans |
| Documentation d'architecture de séparation (rôle CSP) | Documentation technique des contrôles de séparation logique mis en œuvre à travers les applications virtualisées, le stockage et le réseau | Responsable Ingénierie Cloud | Version actuelle + versions précédentes pendant 3 ans |
| Évaluations des risques des logiciels fournis par les CSC | Registres des évaluations de risque effectuées avant d'autoriser l'exécution de logiciels fournis par les CSC dans une infrastructure partagée | Prestation de services cloud / Ingénierie | En cours + 3 ans |
| Registres de tests de séparation | Résultats des tests périodiques aux frontières des locataires et des audits de configuration de l'isolation | Responsable Ingénierie Cloud | En cours + 3 ans |
| Registres d'écarts de séparation / de risques | Registres de tout écart de séparation escaladé dans le processus d'appréciation et de traitement des risques, avec sa résolution | RSSI | En cours + 3 ans |

---

# Suivi et indicateurs

Le Responsable Sécurité Cloud rapporte au RSSI, au moins trimestriellement :

- La proportion des services cloud (rôle CSC) disposant d'une vérification de séparation à jour dans les 12 derniers mois
- Les résultats et le statut de remédiation des tests de séparation les plus récents (rôle CSP)
- Le nombre d'écarts de séparation identifiés et escaladés dans le processus d'appréciation et de traitement des risques, ainsi que leur statut de résolution

---

# Considérations d'audit

Les auditeurs vérifiant la conformité à CLD-SEC-POL-A.8.35 doivent s'attendre à trouver :

- Des exigences de séparation documentées pour chaque service cloud que [Organisation] consomme en tant que CSC
- Des preuves de la vérification périodique que les contrôles de séparation du CSP satisfont à ces exigences, et que les écarts sont escaladés en tant que risques plutôt que laissés ouverts
- Une documentation technique de l'architecture de séparation logique pour tout environnement multi-locataires exploité par [Organisation] en tant que CSP, couvrant les données, les applications virtualisées, les systèmes d'exploitation, le stockage et le réseau
- Des preuves que l'accès d'administration interne de [Organisation] est séparé des ressources destinées aux CSC
- Des registres d'évaluation des risques pour les logiciels fournis par les CSC exécutés au sein de l'infrastructure partagée de [Organisation]
- Des registres de tests de séparation périodiques, et non une simple revue ponctuelle de la conception de l'architecture

---

<!-- QA_VERIFIED: 2026-08-01 -->
