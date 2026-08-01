<!-- ISMS-CORE:POLICY:CLD-SEC-POL-A.5.38-FR:sec:POL:a.5.38 -->
**CLD-SEC-POL-A.5.38 — Rôles et responsabilités partagés au sein d'un environnement d'informatique en nuage**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Rôles et responsabilités partagés au sein d'un environnement d'informatique en nuage |
| **Type de document** | Politique |
| **Identifiant du document** | CLD-SEC-POL-A.5.38 |
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

**Cycle de révision** : Annuel (ou lors d'un changement significatif du modèle de service cloud ou des relations avec les fournisseurs, ou à la suite de tout incident ou litige relatif à une responsabilité partagée)
**Prochaine date de révision** : [Date d'entrée en vigueur + 12 mois]

**Chaîne d'approbation** :

- Principale : RSSI
- Secondaire : Responsable Sécurité Cloud
- Conformité : Responsable Juridique/Conformité
- Autorité finale : Direction générale

**Documents connexes** :

- ISMS-POL-A.5.1-2-6.1-2 (Emploi sécurisé et rôles — politique SGSI parente pour les rôles et responsabilités A.5.2)
- ISMS-POL-A.5.19-23-S5 (Sécurité des services cloud — politique SGSI cloud parente)
- CLD-SEC-POL-A.5.39 (Accord sur les rôles et responsabilités du partenaire de service cloud — régit la cascade de ces responsabilités vers les partenaires de service cloud)
- CLD-SEC-POL-A.8.35 (Séparation dans les environnements d'informatique virtuelle)
- CLD-SEC-POL-A.8.36 (Détection et prévention de l'utilisation non autorisée des services cloud)
- CLD-SEC-IMP-A.5.38-TG (Rôles et responsabilités partagés — Guide technique, contient le schéma complet de la matrice de responsabilité partagée)
- CLD-SEC-REF-A.5-A.8 (Addendum de guidance sur la sécurité cloud)
- ISO/IEC 27017:2026, Clause 5.38 (CLD — Rôles et responsabilités partagés au sein d'un environnement d'informatique en nuage)
- ISO/IEC 27002:2022 (Mesures de sécurité de l'information)
- ISO/IEC 22123-3 (Informatique en nuage — Architecture de référence)

---

## Résumé exécutif

Cette politique établit la manière dont [Organisation] alloue, documente, communique et met en œuvre les rôles et responsabilités en matière de sécurité de l'information dans chaque relation d'informatique en nuage à laquelle elle participe, conformément à ISO/IEC 27017:2026, Clause 5.38.

**Périmètre** : Tous les services cloud auxquels [Organisation] participe — que ce soit en tant que client de service cloud (CSC) consommant un service cloud tiers, ou en tant que fournisseur de service cloud (CSP) fournissant un service cloud à ses propres clients. Lorsque [Organisation] occupe les deux rôles simultanément (par exemple, en s'appuyant sur l'infrastructure d'un CSP pour fournir son propre service cloud), cette politique s'applique à chaque rôle de manière indépendante. Elle couvre les déploiements publics, privés, hybrides et multi-cloud selon les modèles IaaS, PaaS et SaaS, y compris les relations en cascade où les responsabilités se répercutent tout au long d'une chaîne d'approvisionnement.

**Note sur les contrôles étendus** : ISO/IEC 27017:2026, Clause 5.38 est l'un des quatre contrôles étendus spécifiques au cloud « CLD » introduits par la deuxième édition de la norme (aux côtés des clauses 5.39, 8.35 et 8.36) qui n'ont pas d'équivalent direct dans ISO/IEC 27002:2022 ou dans l'Annex A d'ISO/IEC 27001:2022. [Organisation] le met en œuvre comme une extension informative de son SGSI fondé sur ISO/IEC 27001:2022, conformément à la manière dont ISO/IEC 27017:2026 présente lui-même ces contrôles.

**Principe fondamental** : La sécurité de l'information dans l'informatique en nuage n'est jamais uniquement la responsabilité du CSP ni uniquement celle du CSC — elle est partagée, et l'allocation partagée doit être identifiée, documentée, communiquée et mise en œuvre par les deux parties avant de pouvoir être invoquée. Toute ambiguïté dans cette allocation est traitée comme un risque de sécurité de l'information, et non comme une formalité à résoudre ultérieurement.

---

# Périmètre et applicabilité

## ISO/IEC 27017:2026 — Clause 5.38

**Énoncé du contrôle (ISO/IEC 27017:2026, 5.38) :**
> « Les responsabilités relatives aux rôles partagés en matière de sécurité de l'information dans l'utilisation du service cloud devraient être allouées à des parties identifiées, documentées, communiquées et mises en œuvre à la fois par le CSC et le CSP. »

**Finalité (ISO/IEC 27017:2026, 5.38) :**
> « Clarifier la relation concernant les rôles et responsabilités partagés entre le CSC et le CSP pour la gestion de la sécurité de l'information. »

*(Traduction de travail établie à partir du texte anglais original de la norme, à des fins de lisibilité ; en cas de divergence, le texte anglais officiel d'ISO/IEC 27017:2026 fait foi.)*

## Applicabilité

Cette politique s'applique à :

- Tous les services cloud que [Organisation] consomme en tant que client de service cloud (CSC), quel que soit le modèle de déploiement (public, privé, hybride, multi-cloud) et le modèle de service (IaaS, PaaS, SaaS)
- Tous les services cloud que [Organisation] fournit en tant que fournisseur de service cloud (CSP) à ses propres clients
- Tout le personnel impliqué dans la sélection, la configuration, l'exploitation ou la fourniture de services cloud pour le compte de [Organisation]

## Cadre réglementaire et normatif

ISO/IEC 27017:2026 est une extension informative d'ISO/IEC 27002:2022, fournissant des orientations spécifiques au cloud pour des contrôles que l'organisation met déjà en œuvre dans le cadre de son SGSI fondé sur ISO/IEC 27001:2022. La clause 5.38 ne correspond à aucun contrôle numéroté d'ISO/IEC 27002:2022 ; il s'agit d'un nouveau contrôle introduit dans la deuxième édition de 2026, thématiquement le plus proche — et mis en œuvre parallèlement — des obligations de rôles et responsabilités du contrôle 5.2 de l'Annex A d'ISO/IEC 27001:2022.

---

# Dispositions de la politique : Rôles et responsabilités partagés (5.38)

## Obligations en tant que client de service cloud (CSC)

Lorsque [Organisation] agit en tant que client de service cloud, [Organisation] DOIT :

- Obtenir l'allocation proposée par le CSP des rôles et responsabilités en matière de sécurité de l'information lors de la sélection et de l'intégration du service, et l'examiner au regard des propres capacités et de l'appétence au risque de [Organisation] avant la mise en production du service
- S'assurer que les rôles et responsabilités en matière de sécurité de l'information de [Organisation] et du CSP sont énoncés dans un accord écrit — et non laissés à la seule documentation publique du CSP, qui peut évoluer sans préavis
- Identifier et maintenir un point de contact nommé au sein de la fonction de support client du CSP pour l'escalade des questions de sécurité de l'information
- Demander au CSP des informations concernant ses capacités en matière de sécurité de l'information — notamment l'authentification, la cryptographie, la sauvegarde et la journalisation — et utiliser des référentiels tiers ou indépendants (par ex. le périmètre de certification ISO/IEC 27001, un rapport SOC 2, une entrée CSA STAR) pour compléter ces informations lorsque les divulgations du CSP sont insuffisantes
- Évaluer tout écart entre l'allocation proposée par le CSP et la capacité de [Organisation] à assumer ses propres responsabilités allouées comme un risque de sécurité de l'information, en l'intégrant au processus documenté d'appréciation et de traitement des risques de [Organisation] lorsqu'il ne peut être résolu avant la mise en production
- Maintenir la sensibilisation du personnel à l'allocation convenue pour les services cloud qu'il utilise, au moyen du programme de sensibilisation à la sécurité de l'information de l'organisation (voir ISMS-POL-A.6.3) et de son intégration aux activités de revue de l'architecture cloud

## Obligations en tant que fournisseur de service cloud (CSP)

Lorsque [Organisation] agit en tant que fournisseur de service cloud, [Organisation] DOIT :

- Définir et documenter l'allocation des rôles et responsabilités en matière de sécurité de l'information que ses CSC, [Organisation] elle-même, et les propres fournisseurs ou partenaires de service cloud de [Organisation] sont chacun censés mettre en œuvre
- Communiquer l'allocation aux CSC prospectifs et existants avant la signature du contrat et après tout changement significatif — via l'accord de service, la documentation de sécurité destinée aux clients, ou les supports d'intégration, selon ce qui convient au service
- Établir et maintenir la relation avec chaque CSC concernant les questions de sécurité de l'information, y compris un chemin d'escalade défini et documenté dans l'accord
- Fournir aux CSC des informations concernant les capacités de sécurité de l'information du service cloud et les mesures de sécurité de l'information prises par [Organisation], à un niveau de clarté suffisant pour que le CSC les comprenne adéquatement — en utilisant des référentiels tiers ou indépendants reconnus lorsque cela est utile pour transmettre ces informations
- Lorsque le service repose sur un CSP sous-jacent (relation en couches ou de chaîne d'approvisionnement), évaluer et documenter la manière dont les responsabilités se répercutent, et s'assurer de la cohérence avec les accords que [Organisation] détient avec ses propres partenaires de service cloud au titre de CLD-SEC-POL-A.5.39
- Traiter tout litige ou toute ambiguïté persistante concernant l'allocation des responsabilités, soulevé par un CSC ou identifié en interne, comme un événement de sécurité de l'information nécessitant une escalade, et non comme une demande de support de routine

## Principe d'allocation partagée

Les rôles et responsabilités dans l'informatique en nuage sont généralement répartis entre le CSC et le CSP. [Organisation] DOIT prendre en compte, lors de l'allocation des rôles et responsabilités dans l'une ou l'autre de ses qualités, les données du CSC et les applications du CSC dont [Organisation] (en tant que CSP) est dépositaire, ou dont [Organisation] (en tant que CSC) demeure responsable nonobstant la garde technique du CSP.

## Matrice de responsabilité partagée — Contenu minimal

Chaque relation de service cloud relevant du périmètre de cette politique DOIT être étayée par une matrice de responsabilité partagée à jour. Au minimum, la matrice consigne, par domaine de responsabilité (par ex. authentification, cryptographie, sauvegarde, journalisation, application de correctifs, segmentation réseau) : à quelle partie il est alloué (CSC, CSP ou partagé) ; quelle action chaque partie doit entreprendre pour assumer sa part ; si [Organisation] a confirmé pouvoir assumer sa propre part allouée ; et la date de la dernière révision. Le schéma complet est tenu dans CLD-SEC-IMP-A.5.38-TG, Section 1. La matrice DOIT être révisée par le Responsable Sécurité Cloud avant la mise en production de toute nouvelle relation de service cloud, puis au moins une fois par an par la suite.

---

# Rôles et responsabilités

| Rôle | Responsabilités |
|------|-----------------|
| **RSSI** | Est propriétaire de CLD-SEC-POL-A.5.38 ; approuve l'allocation de responsabilité partagée pour les relations de service cloud stratégiques ou à haut risque ; fait remonter les écarts d'allocation non résolus à la Direction générale ; examine l'efficacité de la politique lors de la revue de direction |
| **Responsable Sécurité Cloud** | Examine la documentation des rôles/responsabilités fournie par le CSP pour les services consommés (rôle CSC) ; crée et tient à jour la documentation des rôles/responsabilités publiée aux CSC pour les services fournis (rôle CSP) ; tient à jour la matrice de responsabilité partagée pour chaque relation active ; rapporte au RSSI les indicateurs d'écarts d'allocation et de couverture de la matrice |
| **Responsable Juridique/Conformité** | S'assure que l'allocation convenue des rôles et responsabilités est reflétée dans l'accord écrit avec chaque contrepartie CSC ou CSP |
| **Prestation de services cloud / Ingénierie** | Met en œuvre les contrôles techniques correspondant aux responsabilités allouées à [Organisation] ; fait remonter toute responsabilité que [Organisation] ne peut assumer |
| **Tout le personnel** | N'opère que dans le cadre des rôles et responsabilités alloués à sa fonction ; signale toute ambiguïté dans l'allocation de responsabilité partagée au Responsable Sécurité Cloud |

---

# Exigences en matière de preuves

| Preuve | Description | Propriétaire | Conservation |
|-------|-------------|-------------|-------------|
| Matrice de responsabilité partagée | Par relation de service cloud, documentant les responsabilités de sécurité incombant à [Organisation] et celles incombant à la contrepartie (CSC ou CSP), selon le contenu minimal ci-dessus | Responsable Sécurité Cloud | En cours + 3 ans à compter de la fin de la relation |
| Clauses d'accord | Extrait de l'accord écrit énonçant les rôles et responsabilités convenus | Responsable Juridique/Conformité | Durée de l'accord + 3 ans |
| Registres de révision et d'approbation | Registres démontrant que la matrice a été activement révisée et approuvée avant la mise en production, et non acceptée passivement | Responsable Sécurité Cloud | En cours + 3 ans |
| Divulgations de capacités du CSP (rôle CSC) | Registres des informations demandées aux CSP et fournies par eux concernant leurs capacités de sécurité | Responsable Sécurité Cloud | En cours + 3 ans |
| Documentation de capacités destinée aux CSC (rôle CSP) | Documentation publiée aux CSC décrivant les capacités et mesures de sécurité de [Organisation] | Responsable Sécurité Cloud | Version actuelle + versions précédentes pendant 3 ans |
| Registres d'écarts d'allocation / de risques | Registres de tout écart d'allocation escaladé dans le processus d'appréciation et de traitement des risques, avec sa résolution | RSSI | En cours + 3 ans |

> **Base de conservation** : Les périodes de 3 ans s'alignent sur l'approche de conservation utilisée dans l'ensemble de la gamme de produits cloud d'ISMS Core pour les preuves relatives aux contrats et accords.

---

# Suivi et indicateurs

Le Responsable Sécurité Cloud rapporte au RSSI, au moins trimestriellement :

- La proportion des relations de service cloud actives (rôles CSC et CSP) disposant d'une matrice de responsabilité partagée à jour et révisée
- Le nombre d'écarts d'allocation identifiés et escaladés dans le processus d'appréciation et de traitement des risques, ainsi que leur statut de résolution
- Le nombre de litiges ou d'ambiguïtés concernant l'allocation des responsabilités soulevés par des CSC ou des équipes internes

L'efficacité de cette politique est évaluée dans le cadre de la revue de direction, et à la suite de tout incident de sécurité lié au cloud pour lequel l'allocation de responsabilité partagée est pertinente quant à la cause profonde.

---

# Considérations d'audit

Les auditeurs vérifiant la conformité à CLD-SEC-POL-A.5.38 doivent s'attendre à trouver :

- Une matrice de responsabilité partagée pour chaque relation de service cloud active, en rôle CSC ou CSP, satisfaisant aux exigences de contenu minimal ci-dessus
- Des accords écrits qui énoncent, plutôt que d'impliquer, l'allocation des rôles et responsabilités en matière de sécurité de l'information
- Des preuves que [Organisation], lorsqu'elle agit en tant que CSC, a activement examiné et confirmé l'allocation proposée par le CSP plutôt que de l'accepter par défaut
- Des preuves que [Organisation], lorsqu'elle agit en tant que CSP, a documenté et communiqué de manière proactive son allocation aux CSC plutôt que d'attendre que les CSC le demandent
- Des preuves que les écarts d'allocation ont été intégrés au processus d'appréciation et de traitement des risques, et non simplement notés et laissés ouverts
- Des indicateurs de suivi trimestriels démontrant une surveillance active de la couverture de la matrice, et non un exercice ponctuel

---

<!-- QA_VERIFIED: 2026-08-01 -->
