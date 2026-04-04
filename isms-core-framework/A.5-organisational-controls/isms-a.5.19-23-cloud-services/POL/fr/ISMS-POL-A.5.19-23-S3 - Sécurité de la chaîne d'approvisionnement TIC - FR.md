<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.19-23-S3-FR:framework:POL:a.5.19-23-s3 -->
**ISMS-POL-A.5.19-23-S3 — Sécurité de la chaîne d'approvisionnement TIC**
**Contrôle A.5.21 : Gestion de la sécurité de l'information dans la chaîne d'approvisionnement TIC**

---

**Contrôle documentaire**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Sécurité de la chaîne d'approvisionnement TIC |
| **Type de document** | Section de politique |
| **Identifiant du document** | ISMS-POL-A.5.19-23-S3 |
| **Créateur du document** | Responsable de la sécurité de l'information (RSI) |
| **Propriétaire du document** | Responsable de la sécurité des systèmes d'information (RSSI) |
| **Approuvé par** | Direction générale |
| **Date de création** | [Date] |
| **Version** | 1.0 |
| **Date de version** | [À déterminer] |
| **Classification** | Interne |
| **Statut** | Brouillon |

**Historique des versions** :

| Version | Date | Auteur | Modifications |
|---------|------|--------|---------------|
| 1.0 | [Date] | RSI | Section initiale pour le contrôle ISO 27001:2022 A.5.21 |

**Cycle de révision** : Annuel
**Prochaine révision** : [Date d'entrée en vigueur + 12 mois]

**Chaîne d'approbation** :

- Primaire : Responsable de la sécurité des systèmes d'information (RSSI)
- Secondaire : Responsable de la sécurité de l'information (RSI)
- Conformité : Responsable juridique/conformité
- Technique : Directeur des systèmes d'information (DSI)
- Autorité finale : Direction générale

**Documents connexes** :

- ISMS-POL-00 (Cadre d'applicabilité réglementaire)
- ISMS-POL-A.5.19-23 (Politique parente — Sécurité des fournisseurs et des services en nuage)
- ISMS-POL-A.5.19-23-S1 (Fondamentaux des relations fournisseurs)
- ISMS-POL-A.5.19-23-S2 (Exigences des accords fournisseurs)
- ISO/IEC 27001:2022 Contrôle A.5.21
- ISO/IEC 27036-3 (Sécurité de la chaîne d'approvisionnement TIC)
- NIST SP 800-161 (Gestion des risques de la chaîne d'approvisionnement en cybersécurité)

---

# Objet

La présente section définit les exigences applicables à la gestion des risques de sécurité de l'information au sein de la chaîne d'approvisionnement TIC, notamment les sous-traitants, les fournisseurs de composants et les dépendances logicielles. Elle traite du problème dit du « fournisseur du fournisseur » et des vecteurs d'attaque propres aux chaînes d'approvisionnement.

**Principe fondamental — « La confiance se propage tout au long de la chaîne »** : La posture de sécurité de vos fournisseurs dépend de leurs propres fournisseurs, qui dépendent eux-mêmes des leurs. Les violations de SolarWinds, Log4Shell et MOVEit illustrent la compromission de la chaîne d'approvisionnement comme effet multiplicateur : une seule porte dérobée dans un composant largement utilisé accorde aux attaquants l'accès à des milliers d'organisations en aval. La présente politique exige une visibilité systématique, la propagation des exigences de sécurité et une surveillance continue tout au long des chaînes d'approvisionnement TIC multi-niveaux.

**ISO/IEC 27001:2022 Contrôle A.5.21 — Gestion de la sécurité de l'information dans la chaîne d'approvisionnement TIC**

> *Des processus et procédures devraient être définis et convenus avec les fournisseurs afin de gérer les risques de sécurité de l'information associés à la chaîne d'approvisionnement des produits et services TIC.*

**Objectif de contrôle** : Gérer les risques de sécurité de l'information au sein de la chaîne d'approvisionnement TIC, y compris les sous-traitants, les composants et les dépendances logicielles.

**Résumé des lignes directrices ISO/IEC 27002:2022** :

- Les risques de la chaîne d'approvisionnement TIC doivent être identifiés et évalués de manière systématique
- Les exigences de sécurité relatives aux produits et services TIC doivent être précisées dans les processus d'approvisionnement
- Les sous-traitants des fournisseurs (transparence de la chaîne) doivent être évalués et déclarés
- La sécurité de la chaîne d'approvisionnement logicielle doit être prise en charge, y compris les dépendances, les bibliothèques et les composants open source
- La sécurité de la chaîne d'approvisionnement matérielle doit être prise en compte, notamment la détection des contrefaçons et la protection contre les altérations
- La continuité et la résilience de la chaîne d'approvisionnement doivent être planifiées pour les services TIC critiques
- Les changements et mises à jour chez les fournisseurs doivent être gérés par des processus formels de gestion des modifications
- L'évaluation des risques de la chaîne d'approvisionnement doit inclure les dépendances géopolitiques, de concentration et à source unique

---

# Périmètre d'application

## Éléments de la chaîne d'approvisionnement

| Élément | Description | Exemples |
|---------|-------------|----------|
| **Sous-traitants** | Fournisseurs engagés par les fournisseurs principaux | Sous-traitants, sous-responsables du traitement, prestataires de services des fournisseurs |
| **Parties de quatrième niveau** | Fournisseurs des sous-traitants | Fournisseurs d'infrastructure pour les éditeurs SaaS, centres de données pour les prestataires cloud |
| **Composants logiciels** | Dépendances de code et bibliothèques | Paquets open source, SDK, API, frameworks |
| **Composants matériels** | Composants physiques des produits TIC | Processeurs, modules mémoire, puces réseau, micrologiciels |
| **Dépendances de services** | Services requis par les services principaux | Fournisseurs DNS, réseaux CDN, passerelles de paiement, fournisseurs d'identité |
| **Outils de développement** | Outils utilisés pour construire ou livrer des produits | Plateformes CI/CD, référentiels de code, systèmes de build |

## Catégories de risques de la chaîne d'approvisionnement

| Catégorie de risque | Description | Impact |
|---------------------|-------------|--------|
| **Risque de compromission** | Code malveillant ou portes dérobées insérés dans la chaîne d'approvisionnement | Violation de données, compromission de systèmes, espionnage |
| **Risque de disponibilité** | Perturbation de la chaîne ou point de défaillance unique | Interruption de service, perturbation opérationnelle, retards de livraison |
| **Risque d'intégrité** | Modifications non autorisées de composants ou de services | Corruption de données, instabilité des systèmes, non-conformité réglementaire |
| **Risque de conformité** | Violations réglementaires via la chaîne (RGPD, DORA, NIS2) | Amendes, sanctions, responsabilité juridique, atteinte à la réputation |
| **Risque de concentration** | Sur-dépendance envers un seul fournisseur, composant ou territoire | Impact généralisé d'une défaillance unique, verrouillage fournisseur |
| **Risque géopolitique** | Chaîne exposée à des juridictions hostiles ou sous sanctions | Accès aux données par des gouvernements étrangers, perturbation de service |

---

# Gestion des sous-traitants

## Exigences de visibilité des sous-traitants

| Niveau fournisseur | Exigence de visibilité |
|--------------------|------------------------|
| Niveau 1 (Critique) | Registre complet des sous-traitants pour toutes les activités de traitement des données et services critiques |
| Niveau 2 (Élevé) | Registre des sous-traitants pour les services significatifs ou les accès aux données |
| Niveau 3 (Moyen) | Connaissance des sous-traitants clés sur demande |
| Niveau 4 (Faible) | Non requis |

**Renforcement réglementaire** :

- **Entités DORA** : Registre complet de la sous-externalisation requis conformément à l'article 30, incluant la visibilité des parties de quatrième niveau
- **Entités NIS2** : Déclaration des sous-traitants pour les services critiques conformément aux exigences de la chaîne d'approvisionnement de l'article 21

## Registre des sous-traitants

Pour les fournisseurs de niveaux 1 et 2, maintenir une visibilité complète incluant :

| Champ | Description | Déclencheur de mise à jour |
|-------|-------------|---------------------------|
| Nom du sous-traitant | Dénomination légale et identifiant | Nouvel engagement |
| Type de sous-traitant | Catégorie (infrastructure, développement, support, traitement) | Changement de service |
| Services fournis | Services spécifiques apportés par le sous-traitant au fournisseur principal | Changement de périmètre |
| Accès aux données | Accès du sous-traitant aux données de l'[Organisation], niveau de classification | Changement d'accès |
| Lieu de traitement | Localisation géographique du traitement des données ou de la prestation | Changement de lieu |
| Statut de certification | Certifications de sécurité détenues (ISO 27001, SOC 2) | Expiration/renouvellement |
| Criticité | Impact en cas de défaillance du sous-traitant (Critique/Élevé/Moyen/Faible) | Révision annuelle |
| Statut d'approbation | Approbation de l'[Organisation] (Approuvé/En attente/Rejeté) | Décision de révision |
| Conditions contractuelles | Principales obligations de sécurité transmises au sous-traitant | Modification du contrat |

**Maintenance du registre** :

- Mis à jour dans les 10 jours ouvrés suivant tout changement de sous-traitant
- Révision trimestrielle pour en vérifier l'exactitude et l'exhaustivité
- Rapprochement annuel avec la documentation fournie par le fournisseur

## Exigences de contrôle des sous-traitants

**Les fournisseurs principaux doivent :**

| Exigence | Niveau 1 | Niveau 2 | Niveaux 3-4 |
|----------|---------|---------|------------|
| Notifier l'[Organisation] des changements de sous-traitants | ✓ 30 jours à l'avance | ✓ Avant l'engagement | — |
| Obtenir l'approbation écrite pour tout nouveau sous-traitant | ✓ Requis | ✓ Notification suffisante | — |
| Transmettre les exigences de sécurité aux sous-traitants | ✓ À l'identique | ✓ De manière équivalente | — |
| Demeurer pleinement responsable des actes des sous-traitants | ✓ Requis | ✓ Requis | ✓ Requis |
| Fournir les rapports d'audit des sous-traitants sur demande | ✓ Sous 30 jours | ✓ Dans la mesure du possible | — |
| Permettre à l'[Organisation] de s'opposer à des sous-traitants spécifiques | ✓ Délai d'opposition de 14 jours | ✓ Opposition raisonnable | — |
| Maintenir un registre des sous-traitants | ✓ À jour, exhaustif | ✓ Sous-traitants clés | — |
| Réaliser une diligence raisonnable sur les sous-traitants | ✓ Équivalente à celle de l'[Organisation] | ✓ Fondée sur le risque | — |

## Processus de changement de sous-traitant

```
┌─────────────────────────────────────────────────────────────────────┐
│ PROCESSUS DE NOTIFICATION DE CHANGEMENT DE SOUS-TRAITANT            │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  1. Le fournisseur notifie l'[Organisation] du changement planifié  │
│     • Nom et coordonnées du sous-traitant                           │
│     • Services devant être fournis                                  │
│     • Exigences d'accès aux données                                 │
│     • Localisations géographiques                                   │
│     • Certifications de sécurité                                    │
│                          ↓                                          │
│  2. La sécurité de l'[Organisation] examine le sous-traitant        │
│     • Certifications (ISO 27001, SOC 2)                             │
│     • Périmètre et classification des accès aux données             │
│     • Localisation géographique et juridiction                      │
│     • Impact sur le risque de concentration                         │
│     • Implications réglementaires (DORA, NIS2, RGPD)               │
│                          ↓                                          │
│  3. L'[Organisation] répond (sous 14 jours)                         │
│     • APPROUVÉ : Procéder à l'engagement                            │
│     • DEMANDE D'INFORMATIONS COMPLÉMENTAIRES : Documentation requise│
│     • OBJECTION : Motif de sécurité ou de conformité valide fourni  │
│                          ↓                                          │
│  4. En cas d'objection : le fournisseur propose une alternative     │
│     ou des mesures d'atténuation compensatoires                     │
│                          ↓                                          │
│  5. Mise à jour du registre des sous-traitants et avenants          │
│     contractuels                                                    │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

**Motifs d'opposition** :

- Le sous-traitant est établi dans une juridiction à risque élevé
- Le sous-traitant ne dispose pas des certifications requises
- Le sous-traitant a un historique d'incidents de sécurité
- Risque de concentration (même sous-traitant chez plusieurs fournisseurs)
- Incompatibilité réglementaire (DORA, NIS2, RGPD)

---

# Gestion des risques liés aux parties de quatrième niveau

## Visibilité des parties de quatrième niveau

Les parties de quatrième niveau sont les fournisseurs des sous-traitants de vos fournisseurs (par exemple, le fournisseur d'infrastructure hébergeant la plateforme cloud de votre éditeur SaaS).

| Approche | Description | Applicabilité |
|----------|-------------|---------------|
| **Visibilité directe** | Demander au fournisseur des informations sur les parties de quatrième niveau avec documentation | Fournisseurs de niveau 1 pour les services critiques |
| **Reliance sur certifications** | La certification ISO 27001/SOC 2 du fournisseur couvre la gestion des parties de quatrième niveau | Fournisseurs de niveau 2 ; complément à la visibilité directe pour les niveaux 1 |
| **Transmission contractuelle** | Exiger du fournisseur qu'il impose des exigences de sécurité à toutes ses parties de quatrième niveau | Tous les fournisseurs ayant accès aux données |

## Dépendances critiques envers des parties de quatrième niveau

Identifier et documenter les dépendances envers des parties de quatrième niveau pour :

**Services d'infrastructure** :

- Plateformes de calcul (AWS, Azure, GCP sous-jacents aux éditeurs SaaS)
- Fournisseurs de stockage (stockage objet, stockage bloc, sauvegarde)
- Fournisseurs réseau (connectivité internet, liens privés, CDN)

**Services de sécurité** :

- Fournisseurs d'identité (SSO, MFA, annuaires)
- Services de chiffrement (gestion de clés, HSM, autorités de certification)
- Services de surveillance (SIEM, agrégation de journaux, renseignement sur les menaces)

**Services opérationnels** :

- Fournisseurs DNS (critiques pour la disponibilité)
- Réseaux CDN (distribution de contenu, protection DDoS)
- Processeurs de paiement (traitement des transactions financières)

## Indicateurs de risque des parties de quatrième niveau

| Indicateur | Signal de risque | Mesure d'atténuation |
|------------|-----------------|---------------------|
| Le fournisseur dépend d'une seule partie de quatrième niveau pour une fonction critique | Risque de concentration | Exiger une redondance ou un plan de contingence auprès du fournisseur |
| Partie de quatrième niveau établie dans une juridiction à risque élevé (CLOUD Act américain, sanctions) | Risque géopolitique | Évaluer la résidence des données, le chiffrement, les protections contractuelles |
| Partie de quatrième niveau avec historique d'incidents ou pannes | Risque de fiabilité | Demander l'historique des incidents et les preuves de PCA/PRA |
| Absence de contrôles contractuels sur la partie de quatrième niveau | Risque de conformité | S'assurer de la présence de clauses de transmission dans le contrat fournisseur |
| Partie de quatrième niveau sans certifications de sécurité | Risque sécuritaire | Exiger la documentation de diligence raisonnable du fournisseur |

**Évaluation du risque de concentration** : Si plusieurs fournisseurs de niveau 1 dépendent de la même partie de quatrième niveau (par ex. tous les éditeurs SaaS utilisent AWS), évaluer :

- L'impact en cas de défaillance de la partie de quatrième niveau
- Les fournisseurs alternatifs disponibles
- Les implications pour la continuité d'activité
- Les stratégies d'atténuation (multi-cloud, architecture hybride)

## Critères d'acceptation du risque lié aux parties de quatrième niveau

Lorsque des indicateurs de risque sont identifiés sur une partie de quatrième niveau, la sécurité de l'[Organisation] applique le processus décisionnel structuré suivant avant d'accepter ou d'escalader le risque :

**Seuil de l'historique des incidents :**

| Historique d'incidents de la partie de quatrième niveau | Décision |
|---------------------------------------------------------|---------|
| 0 à 1 incident majeur au cours des 3 dernières années | Accepter si les certifications sont à jour et si les preuves de PCA/PRA sont fournies |
| 2 incidents majeurs au cours des 3 dernières années | Acceptation conditionnelle — exiger que le fournisseur mette en œuvre une redondance géographique ou une partie de quatrième niveau alternative sous 90 jours |
| 3 incidents majeurs ou plus au cours des 3 dernières années | Rejeter sauf approbation du RSSI avec mesures compensatoires documentées et dérogation à durée limitée |
| Incident critique actif et non résolu au moment de l'examen | Rejeter jusqu'à résolution de l'incident et acceptation de l'analyse des causes racines (ACR) |

> « Incident majeur » = interruption ou événement de sécurité entraînant un impact de service supérieur à 4 heures sur des services critiques, violation avérée de données clients, ou sanction réglementaire prononcée à l'encontre de la partie de quatrième niveau.

**Processus décisionnel d'acceptation/rejet :**

```
Partie de quatrième niveau identifiée dans la chaîne d'approvisionnement du fournisseur
              ↓
La partie de quatrième niveau est-elle dans une juridiction à risque élevé ?
  OUI → Évaluer la résidence des données, le chiffrement, les protections contractuelles
        → Si aucune protection adéquate → REJET / exiger un changement de partie de quatrième niveau
  NON → Continuer
              ↓
La partie de quatrième niveau détient-elle les certifications requises (ISO 27001, SOC 2) ?
  NON → Le fournisseur doit fournir des éléments compensatoires (audit tiers, évaluation RSSI)
        → Absence de preuves → REJET
  OUI → Continuer
              ↓
Vérification de l'historique des incidents (rétrospective sur 3 ans)
  3 incidents majeurs ou plus → Escalade au RSSI pour décision de dérogation
  2 incidents → Acceptation conditionnelle avec plan de correction délimité dans le temps
  0-1 incident → ACCEPTER
              ↓
Vérification du risque de concentration
  Plus de 50 % des fournisseurs de niveau 1 dépendent de la même partie de quatrième niveau ?
  OUI → Documenter le risque de concentration dans le registre des risques ;
        exiger une feuille de route multi-cloud/redondance
  NON → ACCEPTER
```

**Escalade** : Toutes les décisions de REJET concernant une partie de quatrième niveau et les dérogations accordées par le RSSI doivent être documentées dans le Registre des risques fournisseurs avec le raisonnement, le propriétaire du risque et la date d'expiration de la dérogation (durée maximale de dérogation : 12 mois).

---

# Sécurité de la chaîne d'approvisionnement logicielle

## Risques liés aux composants logiciels

| Risque | Description | Mesure d'atténuation |
|--------|-------------|---------------------|
| Dépendances vulnérables | CVE connus dans les bibliothèques, frameworks ou composants open source | Analyse de vulnérabilités en continu, analyse de composition logicielle (SCA), application rapide des correctifs |
| Paquets malveillants | Attaques de typosquatting, paquets légitimes compromis, portes dérobées | Vérification des paquets, validation des sommes de contrôle, utilisation exclusive de sources de référentiels de confiance |
| Logiciels abandonnés | Composants non maintenus sans mises à jour de sécurité | Surveillance du cycle de vie, migration vers des alternatives maintenues, notification du fournisseur |
| Conformité des licences | Licences incompatibles (GPL, AGPL) ou licences incertaines | Analyse des licences, revue juridique, application de la politique open source |
| Compromission du processus de build | Pipelines de build altérés, CI/CD compromis, injection dans la chaîne d'approvisionnement | Durcissement du CI/CD sécurisé, signature du code, builds reproductibles, vérification des artefacts |

## Exigences applicables aux fournisseurs de logiciels

**Les fournisseurs de niveaux 1 et 2 fournissant des logiciels ou des logiciels en tant que service doivent :**

| Exigence | Description |
|----------|-------------|
| Nomenclature logicielle (SBOM) | Maintenir une SBOM complète pour tous les logiciels déployés, y compris les dépendances |
| Gestion des vulnérabilités | Analyses automatisées régulières et application rapide des correctifs (critique : 14 jours, élevé : 30 jours) |
| Cycle de développement sécurisé | Suivre un SDLC sécurisé (OWASP SAMM, Microsoft SDL ou équivalent) |
| Signature du code | Signer numériquement toutes les versions et mises à jour afin d'en vérifier l'intégrité et l'authenticité |
| Sécurité des référentiels de code | AMF, protection des branches, journalisation des audits, analyse de secrets dans les référentiels |
| Approbation des bibliothèques tierces | Processus formel d'approbation des composants open source et tiers |
| Notification de mise à jour | Notifier l'[Organisation] des mises à jour liées à la sécurité dans les 24 heures |
| Cadence de mise à jour des dépendances | Mises à jour régulières des dépendances (trimestriel au minimum pour les mises à jour hors sécurité) |

## Nomenclature logicielle (SBOM)

Pour les fournisseurs de logiciels de niveau 1, la SBOM doit inclure :

| Champ | Description |
|-------|-------------|
| Nom du composant | Identifiant du paquet ou de la bibliothèque (ex. org.apache.logging.log4j:log4j-core) |
| Version | Version spécifique utilisée (versionnement sémantique) |
| Source | Référentiel ou fournisseur d'où le composant a été obtenu |
| Licence | Identifiant de licence SPDX (MIT, Apache-2.0, GPL-3.0) |
| Direct ou transitif | Utilisation directe par l'[Organisation] ou dépendance indirecte |
| Vulnérabilités connues | Statut CVE actuel avec scores CVSS |
| Criticité | Impact en cas de compromission du composant (selon les privilèges et l'accès aux données) |

**Normes SBOM** : Privilégier les formats SBOM standardisés :

- **CycloneDX** : Norme OWASP pour les nomenclatures logicielles
- **SPDX** : Norme de la Linux Foundation
- Les deux formats supportent JSON et XML pour un traitement automatisé

**Fréquence de mise à jour des SBOM** :

- Trimestrielle pour les mises à jour de routine
- Dans les 48 heures suivant la découverte d'une nouvelle vulnérabilité critique dans un composant

**Responsabilité de surveillance des CVE** : Les fournisseurs doivent s'abonner à des flux de vulnérabilités faisant autorité — notamment NVD (nvd.nist.gov), GitHub Dependabot, Snyk ou des flux sectoriels CERT/ISAC — afin de surveiller les CVE affectant les composants de leur SBOM. Le délai de 48 heures pour la mise à jour commence à partir du moment où le fournisseur est notifié par l'un de ces flux, et non à partir du moment où l'[Organisation] soulève le problème. L'[Organisation] surveille également le renseignement sur les menaces de manière indépendante ; si elle identifie un CVE critique dans la SBOM d'un fournisseur avant que ce dernier ne le signale, elle peut demander une mise à jour de la SBOM et un calendrier de correction accélérés, en dehors du cycle prévu. Les fournisseurs qui ne maintiennent pas une surveillance active des CVE sont en infraction à la présente exigence.

## Sécurité de l'open source

| Considération | Recommandation |
|---------------|----------------|
| Vérification de la source | Télécharger les paquets uniquement depuis les référentiels officiels (npmjs.org, pypi.org, Maven Central) |
| Intégrité des paquets | Vérifier les sommes de contrôle et signatures avant utilisation, utiliser des fichiers de verrouillage (package-lock.json, Pipfile.lock) |
| Statut de maintenance | Éviter les projets abandonnés (aucun commit depuis plus de 12 mois) pour les fonctions critiques |
| Santé communautaire | Mainteneurs actifs, réactivité face aux problèmes de sécurité, gouvernance établie |
| Historique de sécurité | Antécédents en matière de divulgation de vulnérabilités et rapidité de correction |
| Compatibilité des licences | Vérifier que la licence autorise l'usage commercial et les œuvres dérivées (éviter l'AGPL dans les services) |
| Outillage de sécurité | Utiliser Dependabot, Snyk ou équivalent pour la détection automatisée des vulnérabilités |

**Pratiques interdites** :

- Installer des paquets depuis des miroirs non officiels ou des référentiels modifiés
- Utiliser des paquets non maintenus pour la cryptographie, l'authentification ou l'autorisation
- Inclure des paquets présentant des vulnérabilités critiques connues sans plan de correction
- Copier-coller du code depuis Stack Overflow ou GitHub sans revue de sécurité

---

# Sécurité de la chaîne d'approvisionnement matérielle

## Risques liés à la chaîne d'approvisionnement matérielle

| Risque | Description | Exemples |
|--------|-------------|----------|
| Composants contrefaits | Pièces non authentiques substituées à des composants d'origine | Faux commutateurs Cisco, puces mémoire contrefaites, batteries clonées |
| Matériel altéré | Modifications malveillantes lors de la fabrication ou du transport | Portes dérobées implantées dans des serveurs, équipements réseau compromis |
| Micrologiciel compromis | Micrologiciel malveillant préinstallé ou modifications du BIOS | Rootkits de micrologiciel, logiciels malveillants UEFI, portes dérobées BMC |
| Défaillance de composants | Composants défectueux ou reconditionnés entraînant une défaillance prématurée | Disques durs défaillants, alimentations non fiables |
| Matériel en fin de vie | Matériel non supporté sans correctifs de sécurité | Serveurs anciens, équipements réseau EOL présentant des vulnérabilités connues |

## Exigences d'approvisionnement matériel

**Pour les fournisseurs matériels de niveaux 1 et 2 :**

| Exigence | Description |
|----------|-------------|
| Canaux autorisés | Achat exclusivement auprès de distributeurs agréés par le fabricant |
| Chaîne de custody | Documentation complète de la manutention et du transport depuis l'usine |
| Vérification de l'intégrité | Vérification des scellés inviolables, de l'intégrité de l'emballage, authentification des numéros de série |
| Vérification du micrologiciel | Validation des versions de micrologiciel par rapport à la base de données du fabricant, vérification des signatures numériques |
| Authenticité des composants | Mesures anti-contrefaçon pour les composants critiques (processeurs, mémoire, stockage) |
| Configuration d'usine | Matériel livré dans l'état par défaut d'usine, non préconfiguré |
| Documentation | Documentation complète du fabricant, certificats d'authenticité |

**Méthodes de vérification** :

- Validation des numéros de série auprès du fabricant
- Inspection des emballages et hologrammes
- Comparaison du poids (les contrefaçons présentent souvent un poids différent)
- Inspection visuelle à la recherche de signes de modification
- Vérification du hachage du micrologiciel par rapport aux valeurs de référence connues

## Considérations sur le cycle de vie du matériel

| Phase | Considération de sécurité |
|-------|--------------------------|
| Approvisionnement | Source autorisée, vérification de l'intégrité, contrôles d'authenticité |
| Réception | Inspection des altérations, vérification de la documentation, période de quarantaine |
| Déploiement | Configuration sécurisée, mises à jour du micrologiciel vers les versions actuelles, enregistrement des actifs |
| Exploitation | Gestion des correctifs, mises à jour du micrologiciel, surveillance environnementale, sécurité physique |
| Maintenance | Prestataires de services autorisés uniquement, présence lors des interventions, vérification de l'intégrité post-intervention |
| Fin de vie | Mise hors service sécurisée, destruction des données (NIST SP 800-88 Rev. 2), certificat de destruction |

---

# Gestion des dépendances de services

## Dépendances de services critiques

Identifier les services dont dépendent les fournisseurs et évaluer l'impact :

| Type de dépendance | Exemples | Risque en cas d'indisponibilité |
|--------------------|----------|--------------------------------|
| Infrastructure | Plateformes cloud (AWS, Azure, GCP), centres de données, colocalisation | Interruption complète de service, inaccessibilité des données |
| Identité et accès | Fournisseurs d'authentification (Auth0, Okta), SSO, services AMF | Perturbation des accès, échecs d'authentification |
| Services de sécurité | Autorités de certification, gestion des clés de chiffrement (KMS), supervision de sécurité | Dégradation de la sécurité, expiration de certificats, lacunes de conformité |
| Communication | Passerelles de messagerie, plateformes de messagerie, services de notification | Défaillance des communications, retard de notification des incidents |
| Services opérationnels | Fournisseurs DNS, réseaux CDN, répartiteurs de charge, protection DDoS | Dégradation des performances, impact sur la disponibilité, exposition aux attaques |
| Traitement des paiements | Passerelles de paiement, détection de fraude, conversion de devises | Échecs de transaction, impact sur le chiffre d'affaires |

## Documentation des dépendances

Pour les fournisseurs de niveau 1, documenter toutes les dépendances de services critiques :

| Champ | Description |
|-------|-------------|
| Dépendance de service | Service spécifique dont dépend le fournisseur (ex. AWS RDS, Cloudflare CDN) |
| Prestataire | Nom du fournisseur de service de quatrième niveau |
| Criticité | Impact en cas de défaillance de la dépendance (Critique/Élevé/Moyen/Faible) |
| Alternatives | Options de secours ou de basculement (multi-cloud, prestataires redondants) |
| SLA | Engagement de niveau de service du prestataire de la dépendance |
| Périmètre géographique | Régions affectées par une défaillance de la dépendance |
| Résidence des données | Localisation du traitement ou du stockage des données par la dépendance |
| Risque de concentration | Existence d'une dépendance commune à plusieurs fournisseurs |

**Exemple de risque de concentration** :
Si tous vos éditeurs SaaS utilisent AWS us-east-1, une panne régionale AWS affecte simultanément tous les services. Mesure d'atténuation : exiger le multi-région ou le multi-cloud pour les fournisseurs de niveau 1.

---

# Atténuation des attaques contre la chaîne d'approvisionnement

## Vecteurs d'attaque courants

| Vecteur | Description | Exemple réel | Mesure d'atténuation |
|---------|-------------|--------------|---------------------|
| Mises à jour compromises | Mises à jour logicielles malveillantes diffusées via des canaux légitimes | SolarWinds Orion, ASUS Live Update | Vérification de la signature du code, déploiements progressifs, tests des mises à jour |
| Confusion de dépendances | Paquets malveillants portant le même nom dans des référentiels publics ou privés | Attaques de confusion de dépendances npm | Configuration de registre privé, réservation d'espaces de noms |
| Vol d'identifiants | Identifiants fournisseur volés et utilisés pour l'accès | Violations Okta/LastPass | Application de l'AMF, surveillance des identifiants, moindre privilège |
| Point d'eau | Outils de développement ou sites web des fournisseurs compromis pour infecter les utilisateurs en aval | CCleaner, NotPetya via MeDoc | Segmentation réseau, détection sur les points de terminaison, surveillance de la chaîne d'approvisionnement |
| Ingénierie sociale | Ciblage du personnel des fournisseurs par hameçonnage ou prétextage | Attaques LAPSUS$ sur les fournisseurs | Exigences de sensibilisation à la sécurité pour les fournisseurs, durcissement de l'authentification |
| Menace interne | Employé ou sous-traitant du fournisseur malveillant | Exfiltration de type Snowden | Vérifications des antécédents, contrôles d'accès, surveillance des activités, séparation des fonctions |

## Contrôles de sécurité de la chaîne d'approvisionnement

| Contrôle | Description |
|----------|-------------|
| Segmentation réseau des fournisseurs | Isoler les accès fournisseurs dans des segments dédiés, sans déplacement latéral vers la production |
| Gestion des accès à privilèges | Exiger PAM pour tous les accès administratifs des fournisseurs, enregistrement des sessions |
| Surveillance continue | Journaliser et alerter sur les activités des fournisseurs, analyse comportementale, détection des anomalies |
| Vérification de l'intégrité | Vérifier les sommes de contrôle et signatures pour les mises à jour, téléchargements et communications des fournisseurs |
| Plan de réponse aux incidents | Intégrer les scénarios de compromission de la chaîne d'approvisionnement dans les plans de réponse aux incidents et les exercices de simulation |
| Fournisseurs alternatifs | Identifier et pré-qualifier des alternatives pour les fournisseurs critiques (stratégie multi-fournisseurs) |
| Renseignement sur les menaces de la chaîne | Surveiller le renseignement sur les menaces concernant les vulnérabilités et compromissions liées aux fournisseurs |
| Attestation logicielle | Exiger des fournisseurs une attestation de l'intégrité du processus de build et de leurs pratiques de sécurité |

## Indicateurs de détection des incidents

Surveiller les signes de compromission de la chaîne d'approvisionnement :

- Utilisation inattendue des identifiants fournisseur (heure, lieu, volume)
- Schémas d'accès inhabituels aux données par des comptes fournisseurs
- Mises à jour logicielles avec des modifications de code inattendues ou des signatures manquantes
- Nouveaux sous-traitants ou dépendances de services non précédemment déclarés
- Communications du fournisseur provenant de canaux ou domaines inhabituels
- Trafic réseau anormal vers ou depuis des systèmes contrôlés par le fournisseur

---

# Transmission des exigences de sécurité

## Propagation dans la chaîne d'approvisionnement

Les fournisseurs principaux doivent propager les exigences de sécurité dans l'ensemble de la chaîne d'approvisionnement :

```
┌──────────────┐      ┌──────────────┐      ┌──────────────┐      ┌──────────────┐
│ Organisation │ ───► │  Fournisseur │ ───► │ Sous-traitant│ ───► │ Partie de 4e │
│              │      │  (Niveau 1)  │      │              │      │     niveau   │
│ Exigences    │      │ DOIT         │      │ DOIT         │      │ DOIT         │
│ définies     │      │ transmettre  │      │ transmettre  │      │ transmettre  │
│ dans cette   │      │ verbatim     │      │ de manière   │      │ de manière   │
│ politique    │      │              │      │ équivalente  │      │ équivalente  │
└──────────────┘      └──────────────┘      └──────────────┘      └──────────────┘
```

## Exigences minimales de transmission

| Exigence | Transmission aux sous-traitants obligatoire | Méthode de vérification |
|----------|---------------------------------------------|------------------------|
| Obligations de confidentialité | ✓ Toujours, à l'identique | Révision des contrats des sous-traitants |
| Protection des données (RGPD art. 28) | ✓ Si traitement de données personnelles | Révision des ATD avec les sous-responsables du traitement |
| Référentiel de contrôles de sécurité | ✓ Si accès aux données ou systèmes de l'[Organisation] | Révision des certifications des sous-traitants |
| Notification d'incident (24 heures) | ✓ Toujours | Vérification des procédures d'escalade des incidents |
| Coopération aux audits | ✓ Pour les sous-traitants critiques | Vérification de la clause de droit d'audit dans le contrat |
| Approbation des sous-contractants | ✓ Si le sous-traitant fait appel à des parties de quatrième niveau | Révision du processus d'approvisionnement du sous-traitant |
| Résidence des données | ✓ Si des restrictions géographiques s'appliquent | Vérification des lieux de traitement des données |
| Pratiques de développement sécurisé | ✓ Si développement logiciel impliqué | Révision de la documentation SDLC |

**Vérification** : L'[Organisation] peut demander des preuves de transmission incluant :

- Extraits de contrats des sous-traitants (expurgés pour les clauses non relatives à la sécurité)
- Questionnaires de sécurité et certifications des sous-traitants
- Procédures de gestion des fournisseurs du fournisseur
- Rapports d'audit couvrant la gestion des sous-traitants

---

# Surveillance et révision

## Activités de surveillance de la chaîne d'approvisionnement

| Activité | Fréquence | Responsable | Documentation |
|----------|-----------|-------------|---------------|
| Révision du registre des sous-traitants | Trimestrielle | Achats + Sécurité | Registre mis à jour, notes de révision |
| Évaluation des risques des parties de quatrième niveau | Annuelle | Gestion des risques de sécurité | Rapport d'évaluation des risques |
| Analyse des dépendances logicielles | Continue (automatisée) | Opérations IT + Développement | Résultats d'analyse, tickets de correction |
| Revue des incidents de la chaîne d'approvisionnement | À chaque occurrence | Réponse aux incidents de sécurité | Rapport d'incident, retours d'expérience |
| Validation des dépendances critiques | Semestrielle | Opérations IT | Cartographie des dépendances, vérification des SLA |
| Évaluation du risque de concentration | Annuelle | RSSI + Gestion des risques | Analyse de concentration, plan d'atténuation |
| Révision des SBOM (logiciels critiques) | Trimestrielle | Sécurité + IT | Validation des SBOM, évaluation des vulnérabilités |

## Métriques et KPI de la chaîne d'approvisionnement

| Métrique | Cible | Méthode de mesure |
|----------|--------|------------------|
| Visibilité des sous-traitants (niveau 1) | 100 % documentés | Audit d'exhaustivité du registre |
| Dépendances critiques identifiées | 100 % documentées | Complétude de l'inventaire des dépendances |
| Couverture SBOM (logiciels critiques) | 100 % disponibles, datant de moins de 90 jours | Collecte et validation des SBOM |
| Dépendances vulnérables | 0 critique, moins de 5 élevées | Résultats des outils SCA |
| Incidents de la chaîne d'approvisionnement | Suivre les tendances, ACR pour tous | Système de gestion des incidents |
| Taux de certification des sous-traitants (N1) | Plus de 90 % ISO 27001 ou SOC 2 | Suivi des certifications |
| Score de risque de concentration | Maintenir en dessous du seuil | Calcul du risque de concentration |

## Reporting sur la chaîne d'approvisionnement

**Le rapport trimestriel sur la chaîne d'approvisionnement** doit inclure :

- Changements chez les sous-traitants (ajouts, suppressions, modifications)
- Synthèse des risques des parties de quatrième niveau (dépendances critiques, risques identifiés)
- Tendances des vulnérabilités logicielles (nouveaux CVE, état des corrections)
- Incidents de la chaîne d'approvisionnement (synthèse, impact, correction)
- Mises à jour de l'évaluation du risque de concentration
- Problèmes de non-conformité et plans de correction

**Destinataires** : RSSI, DSI, Gestion des risques, Direction générale (synthèse annuelle)

---

# Exigences réglementaires

## Sous-externalisation DORA (Article 30)

Pour les services TIC relevant de DORA, maintenir un registre complet de sous-externalisation incluant :

- Tous les arrangements de sous-externalisation conclus par les prestataires tiers de services TIC
- Nature des fonctions sous-externalisées
- Juridictions dans lesquelles la sous-externalisation a lieu
- Date des contrats de sous-externalisation
- Notification préalable à l'[Organisation] avant toute sous-externalisation

**Risque de concentration** : Évaluer et documenter le risque de concentration découlant des arrangements de sous-externalisation conformément à l'article 28 de DORA.

## Sous-externalisation FINMA (Circulaire 2023/1)

Pour les banques suisses soumises à la Circulaire FINMA 2023/1, les exigences en matière de sous-externalisation comprennent :

- Registre complet de tous les arrangements de sous-externalisation
- Approbation préalable de la banque avant toute sous-externalisation significative
- Évaluation des risques couvrant les risques opérationnels, de concentration, de protection des données et juridictionnels
- Transmission contractuelle des exigences de la banque aux sous-externalisants
- Droits d'audit s'étendant aux sous-externalisants (directement ou via le prestataire de services)
- Suivi du statut d'approbation FINMA, le cas échéant

**Risque de concentration** : Évaluer le risque de concentration lié à la sous-externalisation, notamment lorsque plusieurs fournisseurs dépendent de sous-externalisants communs ou lorsque des sous-externalisants sont établis dans des juridictions à capacité d'exécution limitée.

## Sécurité de la chaîne d'approvisionnement NIS2 (Article 21)

Pour les entités couvertes par NIS2, les mesures de sécurité de la chaîne d'approvisionnement doivent inclure :

- Politiques relatives à l'acquisition, au développement et à la maintenance des systèmes TIC
- Exigences de sécurité pour les relations avec les fournisseurs et sous-traitants
- Signalement des incidents par les fournisseurs permettant une notification aux autorités sous 24 heures
- Évaluation des risques de la chaîne d'approvisionnement et stratégies d'atténuation

---

# Références

| Document | Relation |
|----------|---------|
| **ISMS-POL-A.5.19-23** | Cadre de politique parentale |
| **ISMS-POL-A.5.19-23-S1** | Classification des fournisseurs et diligence raisonnable |
| **ISMS-POL-A.5.19-23-S2** | Exigences contractuelles des sous-traitants et clauses de transmission |
| **ISMS-IMP-A.5.19-23.S1-UG/TG** | Inventaire des fournisseurs (incluant sous-traitants et dépendances) |
| **ISO/IEC 27036-3:2023** | Lignes directrices pour la sécurité de la chaîne d'approvisionnement TIC |
| **NIST SP 800-161r1** | Pratiques de gestion des risques de la chaîne d'approvisionnement en cybersécurité |

---

**Document suivant :** ISMS-POL-A.5.19-23-S4 — Surveillance des fournisseurs et gestion des modifications (Contrôle A.5.22)

---

*« Votre sécurité est aussi solide que celle du fournisseur le plus faible de votre fournisseur le plus faible. »*
<!-- QA_VERIFIED: 2026-03-30 -->
