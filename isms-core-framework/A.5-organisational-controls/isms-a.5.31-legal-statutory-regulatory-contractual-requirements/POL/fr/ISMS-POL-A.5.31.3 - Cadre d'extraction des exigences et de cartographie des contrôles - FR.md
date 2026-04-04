<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.31.3-FR:framework:POL:a.5.31.3 -->
**ISMS-POL-A.5.31.3 — Cadre d'extraction des exigences et de cartographie des contrôles**
**Exigences légales, réglementaires, statutaires et contractuelles**

**Contrôle documentaire**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Cadre d'extraction des exigences et de cartographie des contrôles |
| **Type de document** | Politique |
| **Identifiant** | ISMS-POL-A.5.31.3 |
| **Auteur** | Responsable de la sécurité des systèmes d'information (RSSI) |
| **Propriétaire** | Directeur général (PDG) |
| **Approuvé par** | Direction générale |
| **Date de création** | [Date] |
| **Version** | 1.0 |
| **Date de version** | [À déterminer] |
| **Classification** | Interne |
| **Statut** | Brouillon |

**Historique des versions** :

| Version | Date | Auteur | Modifications |
|---------|------|--------|---------------|
| 1.0 | [Date] | RSSI/RSI | Cadre politique initial — première certification ISO 27001:2022 |

---

# Introduction et relation avec les sections 5.31.1/5.31.2

## Objet de cette section

La présente section de politique établit le cadre systématique de l'[Organisation] pour traduire les obligations réglementaires en contrôles de sécurité opérationnels, avec une traçabilité complète. Elle définit les processus par lesquels le texte juridique et réglementaire est transformé en exigences applicables, cartographié sur les contrôles ISO 27001 et suivi jusqu'à la preuve de conformité.

**C'est la « couche de traduction »** du cadre de conformité réglementaire — le maillon essentiel entre l'identification des réglementations applicables et la démonstration de la conformité au travers des contrôles mis en œuvre.

## Progression : applicabilité → exigences → contrôles

Le cadre de conformité réglementaire fonctionne selon une progression logique :

**ISMS-POL-A.5.31.1** a établi l'architecture globale du cadre, le modèle de gouvernance et l'intégration avec ISMS-POL-00 (Cadre d'applicabilité réglementaire). Il a défini le « pourquoi » et la fondation structurelle.

**ISMS-POL-A.5.31.2** a défini la méthodologie systématique permettant de déterminer QUELLES réglementations s'appliquent à l'[Organisation], sur la base de critères géographiques, opérationnels et contractuels. Il répond à la question : « Quelles lois nous régissent ? »

**ISMS-POL-A.5.31.3** (le présent document) définit la méthodologie systématique permettant de déterminer CE QUE ces réglementations applicables exigent et COMMENT l'[Organisation] s'y conforme au travers des contrôles ISO 27001. Il répond aux questions suivantes :

- « Quelles obligations spécifiques ces réglementations imposent-elles ? »
- « Quels contrôles de sécurité satisfont ces obligations ? »
- « Où se situent les lacunes dans notre mise en œuvre actuelle des contrôles ? »
- « Comment prouver la conformité par des preuves ? »

**ISMS-POL-A.5.31.4** (document suivant) définira comment l'[Organisation] surveille les évolutions réglementaires, gère les mises à jour du cadre et maintient des preuves prêtes à l'audit.

## Le défi de la traduction

Les réglementations sont rédigées en langage juridique par des législateurs et des régulateurs. Les contrôles de sécurité sont rédigés en langage technique et organisationnel par des professionnels de la sécurité. Ces deux domaines s'expriment dans des langages différents :

**Langage juridique** :

- « Le responsable du traitement doit mettre en œuvre des mesures techniques et organisationnelles appropriées afin de garantir un niveau de sécurité adapté au risque... »
- Rédigé pour la conformité juridique et l'application des sanctions
- Souvent fondé sur des principes plutôt que prescriptif
- Peut référencer des concepts techniques sans guidance de mise en œuvre spécifique

**Langage des contrôles de sécurité** :

- « A.5.15 Contrôle des accès : les informations et autres actifs associés ne doivent être accessibles qu'aux utilisateurs autorisés. »
- Rédigé pour les praticiens de la sécurité
- Centré sur ce qu'il faut mettre en œuvre, non sur la conformité juridique
- Suffisamment spécifique pour guider la mise en œuvre

**Le défi de la traduction** : Comment extraire de manière systématique et reproductible des exigences spécifiques et opérationnelles d'un texte réglementaire, et les cartographier sur les contrôles de sécurité existants ?

La méthodologie définie dans ce document résout ce défi grâce à :
1. **L'extraction systématique des exigences** — analyse du texte réglementaire pour identifier des exigences discrètes et opérationnelles
2. **La catégorisation des exigences** — organisation des exigences par nature (technique, organisationnelle, déclarative, opérationnelle)
3. **La cartographie des contrôles** — identification des contrôles ISO 27001 Annexe A satisfaisant chaque exigence
4. **L'analyse des écarts** — identification des exigences sans contrôle correspondant
5. **La traçabilité** — maintien d'une piste d'audit complète depuis la réglementation jusqu'à l'exigence, puis au contrôle et à la preuve

## Périmètre du document

La présente section de politique s'applique à :

- **Toutes les réglementations** identifiées comme applicables dans ISMS-POL-00 (réglementations de Niveau 1 obligatoires et de Niveau 2 conditionnelles)
- **Tous les contrôles ISO 27001:2022 Annexe A** (93 contrôles couvrant les domaines organisationnel, humain, physique et technologique)
- **Les contrôles propres à l'organisation** créés lorsqu'aucun contrôle Annexe A ne satisfait une exigence
- **L'ensemble du personnel** impliqué dans la conformité réglementaire, la mise en œuvre des contrôles et la gestion des preuves

Ce document ne :

- Fournit pas d'interprétations juridiques de réglementations spécifiques (l'intervention d'un conseiller juridique est requise)
- Précise pas quelles réglementations s'appliquent à l'[Organisation] (couvert par la section 5.31.2)
- Définit pas les procédures opérationnelles d'extraction et de cartographie (couvertes par IMP-5.31.2 et IMP-5.31.3)
- Définit pas les processus de gestion des preuves (couvert par la section 5.31.4)

---

# Processus d'extraction des exigences

## Méthodologie d'extraction des exigences

L'extraction des exigences est le processus systématique d'analyse du texte réglementaire pour identifier les obligations spécifiques et impératives auxquelles l'[Organisation] doit se conformer. Ce processus transforme un texte juridique verbeux et fondé sur des principes en exigences discrètes et opérationnelles, adaptées à la cartographie sur les contrôles.

### Lecture systématique du texte réglementaire

Les réglementations ont une structure, bien qu'elle varie selon la juridiction et le type :

- **Lois et actes** : Généralement organisés en chapitres, sections, sous-sections, paragraphes
- **Règlements et directives** : Organisés en articles, sections, annexes, schedules
- **Normes** : Organisées en clauses, sous-clauses, exigences, recommandations
- **Contrats** : Organisés en sections, clauses, annexes, accords de niveau de service

Chaque élément structurel peut contenir :

- **Définitions** — établissant la signification des termes (à extraire pour le glossaire, non en tant qu'exigences)
- **Principes** — objectifs de haut niveau (peuvent générer des exigences lorsqu'ils deviennent impératifs)
- **Obligations** — choses spécifiques que l'[Organisation] DOIT faire (CE SONT des exigences)
- **Interdictions** — choses que l'[Organisation] ne doit PAS faire (exigences formulées négativement)
- **Procédures** — comment se conformer aux obligations (peuvent générer des exigences opérationnelles)
- **Obligations déclaratives** — ce qu'il faut soumettre et quand
- **Sanctions** — conséquences du non-respect (informent la priorisation, non extraites en tant qu'exigences)

**Processus de lecture systématique** :

1. **Examiner l'intégralité de la réglementation** pour comprendre son intention et son périmètre globaux
2. **Identifier les délimitations structurelles** (où une exigence se termine et où une autre commence)
3. **Analyser chaque section/article** pour en extraire les obligations discrètes
4. **Distinguer** les obligations impératives, les recommandations et les informations contextuelles
5. **Extraire** chaque obligation impérative en tant qu'exigence distincte
6. **Noter les interdépendances** lorsque les exigences se référencent ou dépendent les unes des autres

**Pièges courants** :

- **Sur-agrégation** : Extraire un article entier comme exigence unique alors qu'il contient plusieurs obligations distinctes
- **Sous-extraction** : Omettre des exigences intégrées dans un texte définitionnel ou procédural
- **Dérive d'interprétation** : Ajouter des obligations non explicitement mentionnées dans la réglementation
- **Ignorance du contexte** : Extraire des exigences sans comprendre leur objectif réglementaire global

### Identifier le langage impératif et le langage recommandatoire

Les réglementations utilisent un langage spécifique pour indiquer le niveau d'obligation. L'[Organisation] extrait les exigences IMPÉRATIVES pour la conformité et prend note du langage recommandatoire à titre de contexte et de guidance de meilleures pratiques.

**Langage impératif** (DOIT être extrait) :

- **« doit »** — indicateur principal d'obligation légale
- **« est tenu de »** — exigence explicite
- **« il est obligatoire de »** — obligation explicite
- **« a le devoir de »** — impose une obligation

**Langage recommandatoire** (PEUT être extrait en tant que mesure facultative/bonne pratique) :

- **« devrait »** — recommandation, non impérative
- **« est encouragé à »** — action volontaire
- **« peut »** — permissif, facultatif
- **« il est recommandé »** — guidance de meilleures pratiques

**Langage conditionnel** (extraire AVEC les conditions) :

- **« doit, le cas échéant »** — impératif lorsque la condition est remplie
- **« doit, si [condition] »** — impératif dans une circonstance spécifique
- **« est tenu de, dans les cas où... »** — obligation conditionnelle

**Le contexte est déterminant** : le langage seul est insuffisant. Un conseiller juridique doit examiner les extractions pour confirmer si un langage apparemment recommandatoire crée des obligations exécutoires dans des contextes réglementaires spécifiques.

**Exemples de décisions d'extraction** :

| Texte réglementaire | Impératif ? | Décision d'extraction |
|--------------------|-------------|----------------------|
| « Les organisations doivent mettre en œuvre le chiffrement pour les données au repos » | Oui (doit) | Extraire : « Mettre en œuvre le chiffrement pour les données au repos » |
| « Les organisations devraient envisager l'authentification multifacteur » | Non (devrait) | Noter comme bonne pratique, ne pas extraire en tant qu'exigence |
| « Les organisations doivent effectuer des évaluations des risques annuellement » | Oui (doit) | Extraire : « Effectuer des évaluations des risques annuellement » |
| « Les organisations peuvent utiliser des cadres sectoriels reconnus » | Non (peuvent) | Noter comme option, ne pas extraire en tant qu'exigence |
| « Lorsque des données personnelles sont traitées, les organisations doivent obtenir le consentement » | Conditionnel (doit, lorsque...) | Extraire : « Obtenir le consentement lors du traitement de données personnelles » |

### Lignes directrices sur la granularité

Les exigences doivent être extraites au bon niveau de détail — suffisamment spécifiques pour être opérationnelles, mais sans être si prescriptives qu'elles éliminent toute flexibilité de mise en œuvre.

**Trop grossier** (non opérationnel) :

- ❌ « Se conformer à l'Article 32 »
  - Problème : Aucune indication sur CE QU'IL FAUT FAIRE pour se conformer
  - Impossible à cartographier sur des contrôles spécifiques
  - Non implémentable

- ❌ « Mettre en œuvre des mesures de sécurité appropriées »
  - Problème : « Appropriées » n'est pas défini
  - Trop vague pour vérifier la conformité
  - Laisse les responsables de mise en œuvre dans l'incertitude

**Trop fin** (trop prescriptif) :

- ❌ « Utiliser le chiffrement AES-256-GCM avec une dérivation de clé PBKDF2 à 10 000 itérations et hachage SHA-256 pour toutes les données au repos »
  - Problème : Élimine toute flexibilité de mise en œuvre
  - La technologie évolue ; des exigences trop spécifiques deviennent obsolètes
  - Peut entrer en conflit avec d'autres réglementations autorisant des contrôles équivalents

- ❌ « Effectuer des tests de pénétration le deuxième mardi de mars chaque année »
  - Problème : Calendrier inutilement précis
  - La réglementation exige probablement seulement des tests « annuels »
  - Crée un processus rigide pouvant ne pas s'aligner sur les besoins métier

**Niveau adapté** (opérationnel avec flexibilité) :

- ✅ « Mettre en œuvre le chiffrement des données au repos en utilisant des algorithmes reconnus par le secteur et des longueurs de clé adaptées à la sensibilité des données »
  - Opérationnel : QUOI clairement défini (chiffrer les données au repos)
  - Flexible : Choix d'algorithme (AES-256, ChaCha20, etc.)
  - Guidé : « Reconnu par le secteur » et « adapté à la sensibilité » fournissent des limites
  - Cartographiable : Peut être associé aux contrôles ISO 27001 sur le chiffrement

- ✅ « Effectuer des évaluations de vulnérabilités de tous les systèmes accessibles depuis Internet au moins trimestriellement »
  - Opérationnel : QUOI (évaluations), SUR QUOI (systèmes exposés), QUAND (trimestriel minimum)
  - Flexible : Choix des outils de scan, détails méthodologiques
  - Vérifiable : Peut démontrer que des scans trimestriels ont eu lieu
  - Cartographiable : Peut être associé aux contrôles ISO 27001 sur la gestion des vulnérabilités

**Cadre de décision de granularité** :

Poser ces questions lors de la détermination de la granularité d'extraction :
1. **Quelqu'un peut-il mettre en œuvre ceci sans suppositions ?** (Si non → trop grossier)
2. **Ceci permet-il des choix d'implémentation raisonnables ?** (Si non → trop fin)
3. **Peut-on cartographier ceci sur un ou plusieurs contrôles ?** (Si non → ajuster la granularité)
4. **Peut-on collecter des preuves pour démontrer la conformité ?** (Si non → trop vague)
5. **Cette exigence restera-t-elle valide à mesure que la technologie évolue ?** (Si non → trop prescriptif)

**Principe général** : Extraire les exigences au niveau où la réglementation impose RÉELLEMENT la spécificité. Si la réglementation dit « chiffrement », ne pas ajouter « AES-256 ». Si la réglementation dit « AES-256 », ne pas généraliser en « chiffrement ».

## Catégorisation des exigences

Une fois extraites, les exigences sont catégorisées selon leur nature afin de faciliter la cartographie sur les contrôles et l'attribution de la mise en œuvre. Chaque exigence peut appartenir à une ou plusieurs catégories.

### Exigences techniques

Exigences imposant des mesures de sécurité technique spécifiques, des configurations système ou des implémentations technologiques.

**Caractéristiques** :

- Nécessitent une mise en œuvre technique (code, configuration, systèmes)
- Généralement mises en œuvre par les équipes IT, Ingénierie de sécurité, Développement
- Peuvent être vérifiées techniquement (scans, audits, tests)

**Exemples** (génériques) :

- « Mettre en œuvre la segmentation réseau pour isoler les systèmes sensibles »
- « Déployer une protection anti-malware sur tous les postes de travail »
- « Activer le chiffrement des données en transit via TLS 1.2 ou supérieur »
- « Configurer les systèmes pour imposer des exigences de complexité des mots de passe »
- « Mettre en œuvre la collecte automatisée de journaux et un stockage centralisé »

**Cartographies types** : Les exigences techniques se cartographient généralement sur les contrôles ISO 27001 des domaines :

- **Domaine 8 (Contrôles technologiques)** : A.8.1 à A.8.34
- Certains contrôles organisationnels à composante technique (p. ex. A.5.15 Contrôle des accès)

### Exigences organisationnelles

Exigences imposant des politiques, procédures, structures de gouvernance, rôles, formations ou processus organisationnels.

**Caractéristiques** :

- Nécessitent la documentation de politiques/procédures
- Généralement mises en œuvre par les équipes Juridique, Conformité, RH, Direction
- Vérifiées par examen documentaire et entretiens

**Exemples** (génériques) :

- « Établir et maintenir une politique de sécurité de l'information approuvée par la direction générale »
- « Définir les rôles et responsabilités en matière de protection des données »
- « Effectuer des vérifications des antécédents pour le personnel ayant accès à des informations sensibles »
- « Dispenser annuellement une formation de sensibilisation à la sécurité à tous les employés »
- « Établir des procédures de réponse aux incidents incluant des voies d'escalade »

**Cartographies types** : Les exigences organisationnelles se cartographient généralement sur les contrôles ISO 27001 des domaines :

- **Domaine 5 (Contrôles organisationnels)** : A.5.1 à A.5.37
- **Domaine 6 (Contrôles liés aux personnes)** : A.6.1 à A.6.8

### Exigences déclaratives

Exigences imposant des soumissions, notifications, divulgations ou rapports aux autorités réglementaires, aux personnes concernées ou à d'autres parties externes.

**Caractéristiques** :

- Sensibles au temps (délais spécifiques)
- À destination de l'extérieur (soumises à des autorités ou tiers)
- Souvent présentent des formats ou modèles prescrits
- Le non-respect est directement visible par les régulateurs

**Exemples** (génériques) :

- « Notifier l'autorité de contrôle des violations de données personnelles dans les 72 heures suivant la prise de connaissance »
- « Soumettre l'attestation annuelle de conformité à l'organisme réglementaire avant le 31 mars »
- « Notifier les personnes concernées des incidents de sécurité impliquant leurs informations personnelles sans délai injustifié »
- « Maintenir un registre public des activités de traitement de données accessible via le site web »
- « Signaler les événements de cybersécurité significatifs au régulateur sectoriel dans les 24 heures »

**Cartographies types** : Les exigences déclaratives se cartographient souvent sur :

- Contrôles de gestion des incidents (A.5.24 à A.5.28)
- Contrôles de surveillance de la conformité (A.5.31, A.5.36)
- Nécessitent souvent des processus SPÉCIFIQUES allant au-delà de l'Annexe A

**Considérations particulières** :

- Les exigences déclaratives ont souvent les délais les plus stricts
- Le défaut de notification constitue généralement une violation distincte
- Requièrent des processus robustes et une attribution claire des responsabilités

### Exigences opérationnelles

Exigences imposant des procédures opérationnelles spécifiques, des mesures de continuité d'activité, des tests, une surveillance ou des activités opérationnelles continues.

**Caractéristiques** :

- Nécessitent une exécution continue (non ponctuelle)
- Souvent cycliques (activités quotidiennes, mensuelles, annuelles)
- Mises en œuvre par les équipes Opérations, IT, Centre opérationnel de sécurité (SOC)
- Vérifiées par les journaux d'activité et les preuves d'exécution

**Exemples** (génériques) :

- « Tester les plans de continuité d'activité annuellement avec des résultats documentés »
- « Surveiller en continu les journaux d'événements de sécurité pour détecter les indicateurs de compromission »
- « Mener des exercices sur table pour les procédures de réponse aux incidents semestriellement »
- « Revoir et mettre à jour les évaluations des risques trimestriellement »
- « Effectuer des scans de vulnérabilités des systèmes de production mensuellement »

**Cartographies types** : Les exigences opérationnelles se cartographient généralement sur :

- Contrôles de test et de surveillance (A.8.7, A.8.15, A.8.16)
- Contrôles de continuité d'activité (A.5.29, A.5.30)
- Contrôles de conformité et d'audit (A.5.36, A.5.37)

### Objectif de la catégorisation

La catégorisation remplit plusieurs fonctions :

**Efficacité de la cartographie** :

- Exigences techniques → se concentrer d'abord sur les contrôles du Domaine 8
- Exigences organisationnelles → se concentrer d'abord sur les contrôles des Domaines 5 & 6
- Réduit le temps en rétrécissant l'espace de recherche

**Attribution de la mise en œuvre** :

- Exigences techniques → équipes IT/Ingénierie de sécurité
- Exigences organisationnelles → équipes Conformité/Juridique/RH
- Exigences déclaratives → équipes Conformité/Communication
- Exigences opérationnelles → équipes Opérations/SOC

**Planification des preuves** :

- Exigences techniques → audits de configuration, résultats de scans, journaux système
- Exigences organisationnelles → documents de politique, relevés de formation, comptes-rendus
- Exigences déclaratives → confirmations de soumission, journaux de notification
- Exigences opérationnelles → journaux d'activité, résultats de tests, tableaux de bord de surveillance

**Analyse des écarts** :

- Les catégories aident à identifier OÙ se situent les écarts (lacunes techniques vs. lacunes de processus)
- Oriente l'approche corrective (correctif technique vs. création de politique)

**Note** : Les exigences peuvent couvrir plusieurs catégories. Exemple : « Mettre en œuvre et maintenir l'authentification multifacteur pour tous les comptes privilégiés » est à la fois Technique (mise en œuvre de l'AMF) et Organisationnelle (politique l'imposant).

## Structure du registre des exigences

Le Registre des exigences est le référentiel centralisé et faisant autorité de toutes les exigences extraites des réglementations applicables. Il constitue la base structurée pour la cartographie des contrôles, l'analyse des écarts et le reporting de conformité.

### Champs du registre

Chaque entrée d'exigence dans le registre DOIT contenir les champs suivants :

**Identifiant d'exigence** (identifiant unique)

- **Format** : REG-[CodeRéglementation]-[Article/Section]-[Séquence]
- **Objet** : Identifiant unique et stable pour chaque exigence, constant même si le texte est mis à jour
- **Exemples** :
  - REG-DP01-32-001 (première exigence extraite de l'Article 32 du règlement sur la protection des données)
  - REG-DP01-32-002 (deuxième exigence du même article)
  - REG-SEC15-4.2-001 (première exigence de la Section 4.2 de la norme de sécurité)
- **CodeRéglementation** : Code court du registre réglementaire ISMS-POL-00 (p. ex. DP01 pour la loi principale sur la protection des données, SEC15 pour la norme de sécurité)

**Identifiant de réglementation** (lien vers ISMS-POL-00)

- **Objet** : Lie l'exigence à la réglementation parente dans le registre réglementaire
- **Contenu** : Même CodeRéglementation utilisé dans l'identifiant d'exigence
- **Usage** : Permet le filtrage/reporting par réglementation, permet les mises à jour en cascade lors de la modification d'une réglementation

**Nom de la réglementation** (nom complet)

- **Objet** : Identification lisible de la réglementation source
- **Contenu** : Nom officiel complet de la réglementation
- **Exemples** :
  - « Loi fédérale sur la protection des données (nLPD) »
  - « Règlement sur la cybersécurité (UE) 2024/1234 »
  - « Norme de sécurité des données de l'industrie des cartes de paiement PCI DSS v4.0.1 »

**Référence** (localisation source précise)

- **Objet** : Référence précise à L'ENDROIT où cette exigence apparaît dans la réglementation
- **Contenu** : Article, section, sous-section, paragraphe, clause selon le cas
- **Exemples** :
  - « Article 32, Paragraphe 1(a) »
  - « Section 4.2.1 »
  - « Exigence 8.3.2 »
  - « Annexe A, Clause 12 »
- **Importance** : Permet l'examen juridique, la vérification et la citation dans la documentation de conformité

**Texte original de l'exigence** (citation verbatim)

- **Objet** : Langage réglementaire exact tel qu'écrit dans la réglementation source
- **Contenu** : Citation directe, sans paraphrase
- **Exemples** :
  - « Le responsable du traitement doit mettre en œuvre des mesures techniques et organisationnelles appropriées afin de garantir un niveau de sécurité adapté au risque, notamment par : (a) la pseudonymisation et le chiffrement des données personnelles »
- **Importance** : Exactitude juridique ; permet de vérifier que l'interprétation est fidèle à la source

**Exigence interprétée** (traduction opérationnelle)

- **Objet** : Exigence reformulée en langage clair et opérationnel adapté à la mise en œuvre
- **Contenu** : Ce que l'[Organisation] DOIT FAIRE pour se conformer, rédigé à la granularité appropriée (cf. Section 2.1.3)
- **Exemples** :
  - D'après l'original ci-dessus : « Mettre en œuvre le chiffrement et la pseudonymisation pour les données personnelles, proportionnellement au niveau de risque évalué »
- **Guidance** : Doit être compréhensible par les responsables de mise en œuvre sans formation juridique

**Catégorie d'exigence** (classification)

- **Objet** : Type d'exigence selon la Section 2.2
- **Contenu** : Un ou plusieurs parmi : Technique / Organisationnelle / Déclarative / Opérationnelle
- **Format** : Peut être multi-sélection (p. ex. « Technique, Organisationnelle » pour les exigences couvrant les deux)

**Priorité** (urgence de mise en œuvre)

- **Objet** : Importance relative pour la mise en œuvre et la remédiation des écarts
- **Valeurs** :
  - **Élevée** : Conséquence juridique significative en cas de non-conformité, ou délai de conformité imminent, ou réglementation de Niveau 1
  - **Moyenne** : Conséquence juridique modérée, ou délai raisonnable pour la conformité
  - **Faible** : Conséquence mineure ou exigence aspirationnelle
- **Base** : Informée par le conseiller juridique, le niveau réglementaire (Niveau 1 vs. Niveau 2), l'historique d'application

**Délai de mise en œuvre** (date de conformité)

- **Objet** : Quand cette exigence doit être mise en œuvre/respectée
- **Contenu** : Date spécifique si la réglementation le précise, sinon date cible organisationnelle
- **Exemples** :
  - « 2025-01-17 » (date d'entrée en vigueur de la réglementation)
  - « Dans les 6 mois suivant l'entrée en vigueur »
  - « À déterminer — priorité organisationnelle » (pour les exigences continues)
- **Usage** : Oriente la planification de la mise en œuvre et le calendrier de remédiation des écarts

**Statut de mise en œuvre** (état actuel)

- **Objet** : Suivre la progression de la mise en œuvre
- **Valeurs** :
  - **Non démarré** : Aucune activité de mise en œuvre
  - **En cours** : Mise en œuvre engagée, non encore terminée
  - **Mis en œuvre** : Intégralement mis en œuvre et opérationnel
  - **Vérifié** : Mis en œuvre et conformité vérifiée (preuves disponibles)
  - **N/A** : L'exigence ne s'applique pas à l'[Organisation] selon le périmètre/contexte
- **Mis à jour par** : Responsable du contrôle chargé de la mise en œuvre

**Partie responsable** (propriétaire)

- **Objet** : Qui est redevable de la mise en œuvre de cette exigence
- **Contenu** : Rôle ou individu nommé
- **Exemples** :
  - « Responsable de la sécurité des systèmes d'information (RSSI) »
  - « Responsable de la sécurité IT »
  - « Délégué à la protection des données (DPD) »
  - « Responsable du contrôle A.8.24 » (lien avec la propriété du contrôle)

**Contrôles cartographiés** (contrôles ISO 27001)

- **Objet** : Quels contrôles satisfont cette exigence
- **Contenu** : Liste des identifiants de contrôle avec le type de cartographie
- **Format** : « A.5.15 (P), A.5.16 (S), A.8.2 (Co) »
  - P = Primaire, S = Secondaire, Co = Complémentaire (cf. Section 3.2)
- **Usage** : Lie les exigences aux contrôles ; permet l'identification des écarts (exigences sans cartographie)

**Statut d'écart** (lacune de conformité)

- **Objet** : Si l'exigence est intégralement satisfaite par les contrôles existants
- **Valeurs** :
  - **Aucun écart** : Exigence intégralement satisfaite par les contrôles cartographiés
  - **Écart partiel** : Les contrôles cartographiés procurent une satisfaction partielle, des améliorations sont nécessaires
  - **Écart total** : Aucun contrôle ne satisfait cette exigence ; de nouveaux contrôles sont nécessaires
- **Oriente** : Les activités de remédiation des écarts (Section 4)

**Notes** (contexte complémentaire)

- **Objet** : Capturer le contexte important, les nuances juridiques, les considérations de mise en œuvre
- **Contenu** : Champ libre pour :
  - Les notes d'interprétation du conseiller juridique
  - Les dépendances vis-à-vis d'autres exigences
  - Les difficultés ou considérations de mise en œuvre
  - Les clarifications issues des orientations réglementaires
  - Les liens vers les FAQ réglementaires ou les décisions d'application

**Extrait par / Date** (traçabilité)

- **Objet** : Qui a effectué l'extraction et quand
- **Contenu** : Nom/rôle et date
- **Exemple** : « Analyste conformité / 2025-01-15 »
- **Usage** : Contrôle qualité, responsabilisation, contact en cas de questions

**Revu par / Date** (contrôle qualité)

- **Objet** : Qui a examiné l'extraction pour en vérifier l'exactitude et quand
- **Contenu** : Nom/rôle et date (typiquement Conseiller juridique ou conformité senior)
- **Exemple** : « Conseiller juridique / 2025-01-20 »
- **Usage** : Assure l'exactitude juridique, vérification secondaire

**Dernière mise à jour / Mis à jour par** (suivi des modifications)

- **Objet** : Quand l'entrée d'exigence a été modifiée en dernier et par qui
- **Contenu** : Date et nom/rôle
- **Usage** : Piste d'audit, contrôle de version, identification des entrées obsolètes

### Maintenance du registre

**Référentiel centralisé** :
Le Registre des exigences DEVRAIT être maintenu dans un format structuré et consultable :

- **Préféré** : Base de données (permet des requêtes complexes, du reporting et de la traçabilité)
- **Acceptable** : Tableur structuré (Excel/LibreOffice avec validation des données, feuilles protégées)
- **Emplacement** : Emplacement centralisé accessible à toutes les parties prenantes avec les autorisations appropriées
- **Outil** : Le Cahier d'évaluation 3 fournit un modèle standardisé

**Contrôle d'accès** :

- **Accès en lecture** : Toutes les parties prenantes SMSI, responsables de contrôles, auditeurs
- **Accès en écriture (ajout/modification)** : Responsable de la conformité, Conseiller juridique, Analystes des exigences désignés
- **Autorité d'approbation** : Responsable SMSI, Conseiller juridique (pour les nouvelles exigences ou modifications du champ « Exigence interprétée »)
- **Accès administratif** : Responsable SMSI (pour les modifications de structure, l'archivage)

**Contrôle de version** :

- **Version du registre** : L'intégralité du registre est versionnée (p. ex. v1.0, v1.1, v2.0)
- **Suivi au niveau des exigences** : Chaque exigence suit son propre historique de modification (champ Dernière mise à jour)
- **Journal des modifications** : Un journal distinct consigne ce qui a changé, quand et pourquoi
  - Exemple : « v1.1 — 2025-02-15 — Ajout de 12 exigences issues de la modification du Règlement sur la protection des données »
- **Archivage** : Les versions précédentes du registre sont conservées au minimum [X années selon la politique de rétention]

**Piste d'audit** :
Toutes les modifications du registre DOIVENT être consignées :

- Date/heure de la modification
- Utilisateur ayant effectué la modification
- Champ(s) modifié(s)
- Ancienne valeur → Nouvelle valeur
- Motif de la modification (depuis les Notes ou une justification séparée)

**Processus de contrôle qualité** :
1. **Extraction** : L'Analyste des exigences extrait les exigences conformément à la Section 2.1
2. **Examen juridique** : Le Conseiller juridique vérifie la traduction Texte original → Exigence interprétée
3. **Approbation** : Le Responsable SMSI ou le Responsable de la conformité approuve l'ajout au registre
4. **Publication** : L'exigence est ajoutée au registre avec le champ « Revu par » complété
5. **Revue périodique** : Toutes les exigences sont révisées annuellement ou lors de toute modification de la réglementation source

**Déclencheurs de maintenance** :
Le Registre des exigences DOIT être mis à jour lorsque :

- Une nouvelle réglementation est identifiée comme applicable (issue du processus 5.31.2)
- Une réglementation existante est modifiée (via la surveillance réglementaire 5.31.4)
- Une réglementation est abrogée ou expire (les exigences sont archivées)
- Le périmètre organisationnel change (de nouvelles exigences deviennent applicables)
- Le statut de mise en œuvre change (les exigences progressent dans leur cycle de vie)
- La remédiation d'un écart est terminée (le Statut d'écart est mis à jour)
- Les cartographies de contrôles changent (les Contrôles cartographiés sont mis à jour)

## Principes d'extraction

Ces principes gouvernent le processus d'extraction des exigences pour garantir la cohérence, l'exactitude et la défendabilité juridique.

**Principe 1 : Exhaustivité**

- Extraire TOUTES les exigences impératives des réglementations applicables
- Ne pas sélectionner les exigences en fonction de la facilité de mise en œuvre
- Si une exigence existe dans une réglementation, elle doit figurer dans le registre
- Justification : Les auditeurs réglementaires examineront l'intégralité de la réglementation ; les lacunes d'extraction constituent des défaillances de conformité

**Principe 2 : Exactitude**

- L'Exigence interprétée doit être fidèle au Texte original de l'exigence
- Ne pas ajouter d'obligations absentes du langage réglementaire
- Ne pas affaiblir les obligations par l'interprétation
- Ne pas modifier le périmètre ou l'applicabilité par la paraphrase
- Justification : La défendabilité juridique exige une représentation fidèle de l'intention réglementaire

**Principe 3 : Clarté**

- Rédiger les Exigences interprétées en langage clair, exempt de jargon
- Public cible : Responsables de mise en œuvre et propriétaires de contrôles, pas les juristes
- Éviter les termes ambigus (« raisonnable », « approprié » sans contexte)
- Rendre les exigences opérationnelles (suffisamment spécifiques pour être mises en œuvre et vérifiées)
- Justification : Les responsables de mise en œuvre doivent comprendre ce qui est requis sans formation juridique

**Principe 4 : Traçabilité**

- Chaque exigence DOIT citer sa source (Identifiant de réglementation, Référence)
- Chaque interprétation DOIT préserver le texte original (champ Texte original)
- Maintenir la piste d'audit de l'extraction et de l'examen (Extrait par, Revu par)
- Permettre la recherche inversée (à partir d'un contrôle, trouver toutes les exigences qu'il satisfait)
- Justification : Les auditeurs exigeront la preuve que les exigences extraites correspondent à la source réglementaire

**Principe 5 : Cohérence**

- Utiliser un langage cohérent entre les exigences issues de différentes réglementations
  - Exemple : Si « données au repos » est le terme utilisé dans l'Exigence 1, utiliser le même terme dans l'Exigence 2, pas « données stockées »
- Appliquer les mêmes lignes directrices de granularité à toutes les extractions
- Utiliser la même logique de catégorisation pour des exigences similaires
- Justification : L'incohérence crée de la confusion, complique la cartographie des contrôles et donne une impression peu professionnelle aux auditeurs

**Principe 6 : Absence de dérive d'interprétation**

- Ne pas ajouter d'exigences au-delà de ce que la réglementation impose
- Exemple : Si la réglementation dit « revue annuelle », ne pas extraire « revue trimestrielle » même si c'est une meilleure pratique
- Distinguer les exigences de conformité des meilleures pratiques organisationnelles
- Si l'[Organisation] choisit de dépasser les exigences réglementaires, le documenter séparément en tant que politique organisationnelle
- Justification : Le cadre de conformité doit refléter les obligations réelles, non les aspirations

**Principe 7 : Examen juridique**

- Toutes les extractions DEVRAIENT être examinées par un conseiller juridique qualifié
- L'examen juridique confirme :
  - Que l'interprétation est juridiquement exacte
  - Qu'aucune exigence impérative n'a été omise
  - Qu'aucune obligation n'a été ajoutée par l'interprétation
  - Que la catégorisation est alignée sur l'intention réglementaire
- Documenter l'examen juridique (champ Revu par)
- Justification : L'extraction des exigences a des implications juridiques ; l'expertise juridique est essentielle

**Principe 8 : Contexte réglementaire**

- Considérer la réglementation dans son intégralité, non article par article isolément
- Les exigences peuvent référencer des définitions, exceptions ou procédures situées ailleurs dans la réglementation
- Interpréter les exigences à la lumière de l'objectif réglementaire et des orientations d'application
- Consulter les FAQ réglementaires, les documents d'orientation et les décisions d'application pour clarification
- Justification : Les réglementations sont des instruments holistiques ; le contexte est déterminant

**Principe 9 : Mise à jour lors des modifications réglementaires**

- Lors de la modification d'une réglementation, revoir TOUTES les exigences extraites de celle-ci
- Mettre à jour les Exigences interprétées si le langage réglementaire a changé
- Ajouter de nouvelles exigences si les modifications créent de nouvelles obligations
- Archiver les exigences si des dispositions sont abrogées
- Justification : Le paysage réglementaire évolue ; le cadre de conformité doit rester à jour

**Principe 10 : Éviter l'enfermement technologique**

- Ne pas extraire les exigences de manière plus prescriptive que ce que la réglementation impose
- Si la réglementation dit « chiffrement », ne pas spécifier l'algorithme sauf si la réglementation le fait
- Si la réglementation dit « reconnu par le secteur », préserver cette flexibilité
- Permettre l'évolution technologique
- Justification : La technologie évolue plus vite que les réglementations ; des exigences trop spécifiques deviennent obsolètes

---

# Méthodologie de cartographie des contrôles

## Approche de cartographie

La cartographie des contrôles est le processus systématique d'identification des contrôles ISO 27001 Annexe A qui satisfont les exigences réglementaires extraites. Elle établit le lien essentiel entre ce que les réglementations exigent et la manière dont l'[Organisation] met en œuvre ces exigences au travers des contrôles de sécurité.

### Le défi de la cartographie

La cartographie des exigences réglementaires sur les contrôles ISO 27001 présente plusieurs défis :

**Inadéquation du langage** :

- Les réglementations utilisent un langage juridique centré sur les obligations et les sanctions
- ISO 27001 utilise un langage de gestion de la sécurité centré sur le risque et les contrôles
- Le même concept est décrit différemment (réglementation : « prévention des accès non autorisés » vs. ISO : « contrôle des accès »)

**Différences de niveau d'abstraction** :

- Les réglementations peuvent être très spécifiques (« notifier dans les 72 heures ») ou très générales (« mesures de sécurité appropriées »)
- Les contrôles ISO sont des abstractions de niveau intermédiaire cohérentes (ce qu'il faut faire, non comment)
- La cartographie doit combler ces écarts d'abstraction

**Relations de type N-N** :

- Une exigence peut nécessiter plusieurs contrôles pour être pleinement satisfaite
- Un contrôle peut satisfaire (partiellement ou intégralement) plusieurs exigences
- Chevauchement et interdépendances entre les contrôles

**Absence d'alignement parfait** :

- ISO 27001 est une norme SMSI à usage général
- Les réglementations sont spécifiques à une juridiction, un secteur ou un type de données
- Certaines exigences réglementaires peuvent n'avoir aucun équivalent direct dans les contrôles ISO

### La question de la cartographie

Pour chaque exigence du Registre des exigences, répondre systématiquement à :

**« Quel(s) contrôle(s) ISO 27001 Annexe A, correctement mis en œuvre, satisfait/satisfont cette exigence ? »**

Cette question peut avoir plusieurs réponses :

- **Contrôle primaire unique** : Un seul contrôle satisfait intégralement l'exigence
- **Contrôles multiples** : Plusieurs contrôles conjugués satisfont l'exigence
- **Contrôles partiels** : Les contrôles existants satisfont partiellement, des lacunes persistent
- **Aucun contrôle existant** : L'exigence n'a pas de correspondance dans l'Annexe A (nécessite un nouveau contrôle organisationnel)

### Philosophie de cartographie

**Principe : Prioriser les contrôles existants**

- Commencer par l'Annexe A ISO 27001 (93 contrôles dans 4 domaines)
- Cartographier les exigences sur les contrôles existants dans la mesure du possible
- Préférer la combinaison de contrôles existants à la création de nouveaux contrôles
- Ne créer des contrôles propres à l'organisation que lorsqu'aucun contrôle Annexe A ne convient

**Justification** :

- Les contrôles ISO 27001 sont bien définis, reconnus par le secteur et familiers aux auditeurs
- La mise en œuvre de contrôles standards est plus simple que la conception de contrôles personnalisés
- Tirer parti des contrôles existants réduit la complexité
- Les audits de certification se concentrent sur l'Annexe A ; les contrôles personnalisés requièrent une justification supplémentaire

**Principe : Accepter les cartographies N-N**

- Des exigences complexes DEVRAIENT se cartographier sur plusieurs contrôles (couverture complète)
- Des contrôles simples DEVRAIENT satisfaire plusieurs exigences (efficacité)
- Ne pas forcer des cartographies 1-à-1 là où N-à-N est plus précis

**Principe : Documenter les cartographies partielles**

- Si un contrôle satisfait partiellement une exigence, le documenter comme Secondaire ou Complémentaire
- Ne pas prétendre à une satisfaction complète lorsque des lacunes existent
- Les cartographies partielles informent l'analyse des écarts et la remédiation

## Types de cartographie

L'[Organisation] utilise un système de classification à quatre niveaux pour caractériser la relation entre une exigence et un contrôle.

### Primaire (P) : Satisfaction directe et substantielle

**Définition** : Le contrôle satisfait DIRECTEMENT et SUBSTANTIELLEMENT l'exigence. Si ce contrôle est correctement mis en œuvre, la majeure partie de l'obligation est satisfaite.

**Caractéristiques** :

- L'objectif déclaré du contrôle s'aligne sur l'intention de l'exigence
- La mise en œuvre du contrôle permet la conformité à l'exigence
- Le contrôle est le moyen « principal » par lequel l'[Organisation] satisfait cette exigence
- La preuve de mise en œuvre du contrôle constitue la preuve de conformité à l'exigence

**Exemples de cartographies** :

| Exigence (interprétée) | Contrôle primaire | Justification |
|------------------------|-------------------|---------------|
| « Mettre en œuvre des contrôles d'accès pour restreindre l'accès aux informations au personnel autorisé uniquement » | A.5.15 Contrôle des accès | Le contrôle impose directement des restrictions d'accès |
| « Chiffrer les données sensibles au repos » | A.8.24 Utilisation de la cryptographie | Le contrôle traite spécifiquement la protection cryptographique |
| « Effectuer des vérifications des antécédents des employés ayant accès à des informations sensibles » | A.6.1 Présélection | Le contrôle impose la vérification préalable à l'embauche |
| « Maintenir un inventaire des actifs informationnels » | A.5.9 Inventaire des informations et autres actifs | Le contrôle exige directement un inventaire des actifs |

**Guidance d'utilisation** :

- Chaque exigence DEVRAIT avoir au moins un contrôle Primaire (si aucun Primaire → lacune probable)
- Des exigences complexes peuvent avoir plusieurs contrôles Primaires conjugués
- Les cartographies Primaires orientent la collecte des preuves (preuve du contrôle Primaire = preuve de conformité)

### Secondaire (S) : Satisfaction partielle ou d'appui

**Définition** : Le contrôle satisfait PARTIELLEMENT l'exigence ou APPUIE la satisfaction sans l'assurer seul. Les contrôles Secondaires fonctionnent aux côtés des contrôles Primaires pour une couverture complète.

**Caractéristiques** :

- Le contrôle contribue à la conformité mais est insuffisant seul
- Le contrôle traite un aspect d'une exigence multidimensionnelle
- Le contrôle fournit un soutien technique ou procédural au contrôle Primaire
- Plusieurs contrôles Secondaires peuvent se combiner avec le Primaire pour une conformité intégrale

**Exemples de cartographies** :

| Exigence (interprétée) | Contrôle(s) primaire(s) | Contrôle(s) secondaire(s) | Justification |
|------------------------|------------------------|--------------------------|---------------|
| « Mettre en œuvre un programme complet de sensibilisation à la sécurité pour tout le personnel » | A.6.3 Sensibilisation, éducation et formation | A.5.2 Rôles et responsabilités ; A.6.2 Conditions d'emploi | Le Primaire est le programme de sensibilisation ; les Secondaires définissent qui est formé |
| « Garantir des pratiques sécurisées de développement logiciel » | A.8.25 Cycle de développement sécurisé | A.8.8 Vulnérabilités techniques ; A.8.29 Tests de sécurité | Le Primaire est le cycle de développement ; les Secondaires couvrent tests et vulnérabilités |
| « Protéger contre les malwares sur tous les systèmes » | A.8.7 Protection contre les malwares | A.8.5 Authentification sécurisée ; A.8.19 Installation de logiciels | Le Primaire est l'anti-malware ; les Secondaires réduisent la surface d'attaque |

**Guidance d'utilisation** :

- Les cartographies Secondaires montrent une approche complète des exigences complexes
- Les contrôles Secondaires peuvent partager la charge de mise en œuvre (différentes équipes)
- Les preuves des contrôles Secondaires complètent celles des contrôles Primaires

### Complémentaire (Co) : Contribution indirecte

**Définition** : Le contrôle contribue INDIRECTEMENT à la satisfaction de l'exigence. Les contrôles Complémentaires créent la fondation organisationnelle, procédurale ou technique qui permet aux contrôles Primaires et Secondaires de fonctionner efficacement.

**Caractéristiques** :

- Le contrôle n'est pas directement lié au mandat spécifique de l'exigence
- Le contrôle fournit une capacité de fond, une fondation ou un élément facilitateur
- L'absence du contrôle Complémentaire ne créerait pas immédiatement un écart de conformité, mais affaiblirait la posture globale de sécurité

**Exemples de cartographies** :

| Exigence (interprétée) | Contrôle(s) primaire(s) | Contrôle(s) secondaire(s) | Contrôle(s) complémentaire(s) | Justification |
|------------------------|------------------------|--------------------------|-------------------------------|---------------|
| « Mettre en œuvre la journalisation et la surveillance des événements de sécurité » | A.8.15 Journalisation ; A.8.16 Surveillance | A.8.11 Masquage des données | A.5.24 Gestion des événements ; A.5.37 Procédures documentées | Les Primaires journalisent/surveillent ; le Secondaire masque les données sensibles ; les Complémentaires régissent la gestion des incidents |
| « Établir des capacités de réponse aux incidents » | A.5.24 à A.5.28 (série gestion des incidents) | A.6.8 Signalement des événements | A.5.1 Politiques de sécurité ; A.7.7 Bureau rangé et écran verrouillé | Les Primaires couvrent la réponse ; le Secondaire le signalement ; les Complémentaires sont des fondations |

**Guidance d'utilisation** :

- Les cartographies Complémentaires sont optionnelles (utiliser le jugement sur la pertinence de la relation)
- Montrent une approche holistique de la conformité
- Peuvent être précieuses pour démontrer la « défense en profondeur » aux auditeurs
- Ne pas en abuser (risque d'encombrer la matrice avec des relations ténues)

### Non applicable (N/A) : Aucune relation

**Définition** : Le contrôle n'a aucune relation significative avec l'exigence. Le contrôle et l'exigence traitent d'objectifs de sécurité entièrement différents.

**Représentation dans la matrice** :

- N/A est représenté par une CELLULE VIDE
- La majorité des cellules seront vides (93 contrôles × typiquement des dizaines d'exigences = des milliers de cellules, la plupart vides)

**Guidance d'utilisation** :

- Ne PAS marquer chaque absence de relation comme « N/A » dans la matrice (encombre la matrice)
- Cellule vide = N/A (implicite)
- Concentrer l'effort de cartographie sur les relations P, S, Co

## Structure de la matrice de cartographie des contrôles

La Matrice de cartographie des contrôles est la représentation visuelle des relations exigence-contrôle. Elle offre une vue synthétique de la couverture de conformité et permet l'identification des écarts.

### Organisation de la matrice

**Lignes** : Exigences

- Chaque ligne représente une exigence du Registre des exigences
- Identifiant de ligne : ID d'exigence (p. ex. REG-DP01-32-001)
- Libellé de ligne : Exigence interprétée (abrégée si nécessaire)
- Les lignes peuvent être regroupées par réglementation ou par catégorie

**Colonnes** : Contrôles ISO 27001 Annexe A

- Chaque colonne représente un des 93 contrôles Annexe A
- Identifiant de colonne : ID de contrôle (p. ex. A.5.1, A.8.24)
- Libellé de colonne : Nom du contrôle (abrégé)
- Colonnes organisées par domaine (A.5.x Organisationnel, A.6.x Humain, A.7.x Physique, A.8.x Technologique)

**Cellules** : Type de cartographie

- La cellule à l'intersection d'une ligne Exigence et d'une colonne Contrôle contient le type de cartographie
- **Valeurs** : P, S, Co, ou vide
  - P = Cartographie Primaire
  - S = Cartographie Secondaire
  - Co = Cartographie Complémentaire
  - Vide = Non applicable
- **Mise en forme** (optionnelle mais recommandée) :
  - Cellules P en surbrillance (p. ex. gras, fond coloré)
  - Cellules S différenciées (p. ex. italique)
  - Cellules Co avec marquage minimal
  - Rend les cartographies Primaires immédiatement visibles

**Exemple d'extrait de matrice** :

| ID d'exigence | Exigence | A.5.15 Contrôle accès | A.5.16 Gestion identités | A.8.2 Accès privilégié | A.8.5 Auth sécurisée | ... |
|---------------|----------|----------------------|--------------------------|------------------------|----------------------|-----|
| REG-DP01-32-001 | Chiffrer données au repos | | | | | ... |
| REG-DP01-32-002 | Contrôles d'accès | **P** | **P** | S | S | ... |
| REG-SEC15-4.2-001 | AMF pour comptes privilégiés | | S | **P** | **P** | ... |

### Avantages de la matrice

**Identification visuelle des écarts** :

- Ligne sans marquage P/S/Co = exigence sans couverture contrôle (ÉCART TOTAL)
- Ligne avec S ou Co uniquement (pas de P) = couverture partielle (ÉCART PARTIEL)
- Identification visuelle immédiate des risques de conformité

**Analyse de réutilisation des contrôles** :

- Colonne avec de nombreux marquages P/S/Co = contrôle satisfaisant de nombreuses exigences
- Identifie les contrôles « à haute valeur » pour la priorisation
- Montre l'efficacité du cadre de contrôles

**Couverture par réglementation** :

- Regrouper les lignes par réglementation pour voir la couverture par réglementation
- Identifier les réglementations avec un nombre élevé d'écarts (priorisation)
- Soutenir le reporting de conformité par réglementation

**Analyse d'impact des modifications** :

- Si un contrôle change, scanner la colonne pour voir toutes les exigences affectées
- Si une exigence change, scanner la ligne pour voir tous les contrôles affectés
- Permet une évaluation d'impact systématique

**Soutien à l'audit** :

- Fournir la matrice aux auditeurs comme représentation visuelle de l'approche
- Parcourir des exigences spécifiques et leurs cartographies de contrôles
- Démontrer une approche systématique et complète

### Maintenance de la matrice

**Outil** : Le Cahier d'évaluation 4 fournit un modèle standardisé avec :

- 93 colonnes de contrôles Annexe A pré-remplies
- Validation des données (seuls P, S, Co, vide autorisés)
- Mise en forme conditionnelle pour la mise en évidence visuelle
- Formules de détection des écarts (lignes sans Primaire)

**Contrôle de version** :

- Matrice versionnée en parallèle du Registre des exigences
- Modifications consignées (date, utilisateur, cellule modifiée, ancienne valeur → nouvelle valeur, raison)
- Versions précédentes archivées

**Déclencheurs de mise à jour** :
La matrice DOIT être mise à jour lorsque :

- Une nouvelle exigence est ajoutée au Registre (nouvelle ligne, cartographies renseignées)
- L'interprétation d'une exigence change (révision des cartographies pour maintenir la pertinence)
- La mise en œuvre d'un contrôle change (le type de cartographie peut évoluer : S → P si le contrôle est amélioré)
- Un nouveau contrôle est ajouté au SMSI (nouvelle colonne, révision de toutes les exigences)
- Un contrôle est supprimé ou déprécié (colonne supprimée, exigences affectées identifiées, nouvelle cartographie)
- La remédiation d'un écart est terminée (vide → P/S/Co)

## Cartographies 1-à-N et N-à-1

Les scénarios de conformité réels impliquent fréquemment des relations complexes entre exigences et contrôles.

### Une exigence → Plusieurs contrôles (1-à-N)

**Scénario** : Une seule exigence réglementaire impose une approche de sécurité complète qu'aucun contrôle unique ne peut satisfaire. Plusieurs contrôles doivent fonctionner ensemble.

**Exemple 1 : Gestion complète des accès**

**Exigence** (REG-DP01-32-003) : « Mettre en œuvre une gestion complète des accès garantissant que seul le personnel autorisé accède aux informations sensibles, sur la base du besoin métier, avec des capacités d'authentification, d'autorisation et d'audit »

**Cartographies de contrôles** :

- **A.5.15 Contrôle des accès** (Primaire) — Établit la politique de contrôle des accès
- **A.5.16 Gestion des identités** (Primaire) — Gère les identités utilisateurs
- **A.5.17 Informations d'authentification** (Primaire) — Gère les credentials
- **A.5.18 Droits d'accès** (Primaire) — Gère l'autorisation
- **A.8.2 Droits d'accès privilégié** (Secondaire) — Gère les comptes privilégiés
- **A.8.3 Restriction d'accès à l'information** (Secondaire) — Restrictions d'accès techniques
- **A.8.5 Authentification sécurisée** (Secondaire) — Mécanismes d'authentification
- **A.8.15 Journalisation** (Complémentaire) — Piste d'audit des accès

**Exemple 2 : Cycle de développement sécurisé**

**Exigence** (REG-SEC15-8.1-002) : « Mettre en œuvre des pratiques de développement logiciel sécurisées incluant le codage sécurisé, les tests, la gestion des vulnérabilités et le contrôle des modifications »

**Cartographies de contrôles** :

- **A.8.25 Cycle de développement sécurisé** (Primaire) — Politique et processus SDLC
- **A.8.28 Codage sécurisé** (Primaire) — Normes de codage
- **A.8.29 Tests de sécurité** (Primaire) — Exigences de tests
- **A.8.8 Gestion des vulnérabilités techniques** (Secondaire) — Remédiation des vulnérabilités
- **A.8.32 Gestion des modifications** (Secondaire) — Contrôle des modifications
- **A.5.37 Procédures opérationnelles documentées** (Complémentaire) — Documentation des procédures

### Plusieurs exigences → Un contrôle (N-à-1)

**Scénario** : Un seul contrôle, lorsqu'il est mis en œuvre, satisfait simultanément plusieurs exigences réglementaires. C'est l'efficacité en action — mettre en œuvre une fois, se conformer à de multiples réglementations.

**Exemple 1 : Contrôle de chiffrement**

**Contrôle** : A.8.24 Utilisation de la cryptographie

**Satisfait les exigences** :

- REG-DP01-32-001 : « Chiffrer les données personnelles au repos » (Primaire)
- REG-DP01-32-002 : « Chiffrer les données personnelles en transit » (Primaire)
- REG-FIN05-15-003 : « Protéger les données de carte de paiement par chiffrement » (Primaire)
- REG-HEALTH-12-001 : « Chiffrer les dossiers de santé électroniques » (Primaire)
- REG-SEC15-4.4-002 : « Utiliser le chiffrement conforme aux standards sectoriels pour les données sensibles » (Primaire)

**Exemple 2 : Journalisation et surveillance**

**Contrôle** : A.8.15 Journalisation

**Satisfait les exigences** :

- REG-DP01-33-001 : « Journaliser les accès aux données personnelles » (Primaire)
- REG-FIN05-10-002 : « Maintenir des pistes d'audit des transactions financières » (Primaire)
- REG-SEC15-5.2-001 : « Journaliser les événements de sécurité pour la détection des incidents » (Primaire)
- REG-CYBER-Article4-002 : « Surveiller les activités système pour détecter les anomalies » (Secondaire)
- REG-CONTRACT-SLA-003 : « Fournir les journaux d'accès au client sur demande » (Primaire)

**Avantages des cartographies N-à-1** :

- **Efficacité de mise en œuvre** : Construire une fois, satisfaire plusieurs exigences
- **Efficacité des preuves** : Collecter une fois, présenter à plusieurs audits
- **Efficacité de maintenance** : Mettre à jour un contrôle, maintenir la conformité avec plusieurs réglementations
- **Efficacité de coûts** : Éviter les mises en œuvre dupliquées
- **Cohérence** : Même contrôle pour des exigences similaires = posture de sécurité cohérente

## Au-delà de l'Annexe A : contrôles propres à l'organisation

### Quand aucun contrôle Annexe A ne convient

Malgré les 93 contrôles couvrant un périmètre SMSI exhaustif, les exigences réglementaires exigent occasionnellement des capacités non couvertes par l'Annexe A.

**Situations requérant des contrôles propres à l'organisation** :

- **Exigences techniques sectorielles** : Services financiers — « Mettre en œuvre une surveillance des transactions pour la détection des fraudes » (aucun contrôle Annexe A pour les systèmes de détection de fraude) ; Santé — « Mettre en œuvre un accès d'urgence pour les situations médicales critiques » (l'accès d'urgence avec dérogation est spécifique au secteur)
- **Obligations déclaratives juridictionnelles** : « Soumettre l'attestation annuelle de cybersécurité au Régulateur X avant le 31 mars » (l'Annexe A n'a aucun contrôle pour les processus de déclaration réglementaire)
- **Obligations contractuelles** : « Fournir au client un tableau de bord mensuel de métriques de sécurité conformément à l'Article 12 du contrat de niveau de service »
- **Menaces/technologies émergentes** : « Mettre en œuvre des tests de biais et une surveillance des modèles d'IA » (contrôles spécifiques à l'IA non présents dans ISO 27001:2022)

### Création de contrôles propres à l'organisation

Lorsque l'analyse des écarts (Section 4) identifie des exigences sans cartographie Annexe A, l'[Organisation] DOIT créer des contrôles propres en suivant cette méthodologie :

**Étape 1 : Vérifier l'écart**

- Confirmer qu'AUCUN contrôle Annexe A, même partiellement, ne traite l'exigence
- Consulter le Responsable SMSI, les Responsables de contrôles et le conseiller Juridique
- Documenter la justification du nouveau contrôle (pourquoi l'Annexe A est insuffisante)

**Étape 2 : Définir le contrôle**

- **ID du contrôle** : CTRL-ORG-[Domaine]-[Séquence]
  - Domaine : ORG (Organisationnel), HUM (Humain), PHY (Physique), TEC (Technologique)
  - Séquence : 001, 002, 003, etc.
  - Exemple : CTRL-ORG-TEC-001 (premier contrôle technologique organisationnel)
- **Nom du contrôle** : Description claire et concise
- **Objectif du contrôle** : Pourquoi ce contrôle existe
- **Description du contrôle** : Ce que fait le contrôle

**Étape 3 : Spécifier la mise en œuvre**

- Guidance de mise en œuvre : Comment mettre en œuvre le contrôle
- Exigences de preuve : Comment démontrer l'efficacité du contrôle

**Étape 4 : Attribuer la propriété**

- Responsable du contrôle : Qui met en œuvre et maintient le contrôle
- Approbation : Approbation de la Direction générale (ajoute au périmètre et aux coûts du SMSI)

**Étape 5 : Intégrer au SMSI**

- Ajouter à la Déclaration d'Applicabilité (DdA) si une certification est envisagée
- Ajouter à la Matrice de cartographie des contrôles (nouvelle colonne pour CTRL-ORG-TEC-001)
- Cartographier l'exigence sur le nouveau contrôle (cartographie Primaire)
- Inclure dans le périmètre d'audit interne
- Inclure dans la revue de direction

**Étape 6 : Documenter dans le registre des contrôles organisationnels**

- Maintenir un registre distinct des contrôles propres à l'organisation
- Lier aux exigences réglementaires motivant leur création
- Suivre le statut de mise en œuvre, les preuves et les audits

**Exemple : Contrôle propre à l'organisation**

**Exigence** : REG-FIN05-23-005 : « Mettre en œuvre la détection de fraude en temps réel pour toutes les transactions par carte de paiement avec alertes automatisées pour les schémas suspects »

**Contrôle propre à l'organisation créé** :

- **ID** : CTRL-ORG-TEC-001
- **Nom** : Détection de fraude et surveillance des transactions
- **Objectif** : Détecter et prévenir la fraude par carte de paiement en temps réel
- **Description** :
  - Déployer un système de surveillance des transactions en temps réel
  - Le système compare les transactions aux indicateurs de fraude
  - Alertes automatisées générées pour les transactions à haut risque
  - L'équipe SOC enquête sur les alertes dans les 15 minutes
  - Transactions frauduleuses bloquées, titulaires de cartes notifiés
- **Preuves requises** :
  - Documentation de configuration du système
  - Tableau de bord de surveillance
  - Journaux d'alertes (date, heure, transaction, score de risque, action)
  - Métriques mensuelles de détection de fraude
  - Tests annuels des règles de détection

### Gouvernance des contrôles propres à l'organisation

- Nouveaux contrôles requièrent l'approbation de la Direction générale
- Cycle de révision annuel : vérifier la nécessité continue, l'efficacité
- Intégration à la certification : documenter dans la DdA avec justification claire
- Limitation : éviter la prolifération ; préférer l'amélioration des contrôles Annexe A

---

# Processus d'analyse des écarts

L'analyse des écarts est l'identification systématique des exigences réglementaires non intégralement satisfaites par les contrôles existants ou planifiés. C'est la « vérification de réalité » qui répond à : « Où sommes-nous non conformes ? »

## Identification des écarts

### Types d'écarts

**Écarts totaux** :

- **Définition** : L'exigence n'a AUCUN contrôle cartographié (aucun marquage P, S ou Co dans la matrice)
- **Gravité** : Critique — représente une non-conformité totale
- **Identification** : La ligne d'exigence dans la matrice est entièrement vide
- **Exemple** :
  - Exigence : « Notifier l'autorité de contrôle des violations de données dans les 72 heures »
  - Contrôles actuels : L'[Organisation] a des procédures de réponse aux incidents (A.5.24-A.5.28) mais aucun processus spécifique de notification réglementaire dans les 72 heures
  - Remédiation requise : Créer une procédure de notification dans le cadre de la gestion des incidents

**Écarts partiels** :

- **Définition** : L'exigence a des cartographies Secondaires ou Complémentaires mais AUCUNE cartographie Primaire, OU une cartographie Primaire existe mais le contrôle ne satisfait que partiellement l'exigence
- **Gravité** : Élevée — conformité partielle, mais des lacunes significatives persistent
- **Exemple 1** (sans Primaire) :
  - Exigence : « Effectuer des tests de pénétration de tous les systèmes accessibles depuis Internet annuellement »
  - Contrôle actuel : A.8.8 (Secondaire — scans de vulnérabilités, pas tests de pénétration)
  - Remédiation : Améliorer A.8.8 pour inclure les tests de pénétration
- **Exemple 2** (Primaire incomplet) :
  - Exigence : « Chiffrer toutes les données sensibles au repos et en transit »
  - Contrôle actuel : A.8.24 (Primaire) — chiffrement au repos mis en œuvre, en transit partiel
  - Remédiation : Compléter la mise en œuvre (mettre à niveau les systèmes hérités vers TLS)

**Écarts de mise en œuvre** :

- **Définition** : L'exigence est cartographiée sur un contrôle approprié (cartographie Primaire), mais le contrôle n'est pas encore mis en œuvre ou l'est insuffisamment
- **Gravité** : Variable (Élevée si délai approchant, Moyenne sinon)
- **Exemple** :
  - Exigence : « Dispenser une formation de sensibilisation à la sécurité à tous les employés annuellement »
  - Contrôle : A.6.3 (Primaire) — politique existante mais formation non dispensée régulièrement, sans suivi
  - Remédiation : Mettre en œuvre le programme de formation, établir le suivi

### Processus d'identification des écarts

**Étape 1 : Analyse de la matrice de cartographie**

- Identifier les lignes sans cartographie Primaire → Écarts totaux ou partiels
- Pour chaque exigence, évaluer :
  - A-t-elle une cartographie Primaire ? (Si non → écart)
  - Les cartographies Secondaires/Complémentaires couvrent-elles partiellement ? (Si oui → écart partiel ; si non → écart total)
  - La cartographie est-elle exacte ? (Parfois l'écart est une erreur de cartographie)

**Étape 2 : Revue de mise en œuvre des contrôles**

- Pour les exigences avec cartographies Primaires, vérifier le statut de mise en œuvre
- Sources : Statut dans le Registre des exigences ; rapports d'audit interne ; évaluations d'efficacité ; confirmations des Responsables de contrôles

**Étape 3 : Vérification des preuves**

- Pour les exigences marquées « Mis en œuvre », vérifier l'existence des preuves
- Si les preuves sont manquantes ou insuffisantes → écart de preuves

**Étape 4 : Consultation des parties prenantes**

- **Conseiller juridique** : Confirmer que l'interprétation de l'écart est juridiquement correcte
- **Responsables de contrôles** : Confirmer que les contrôles ne peuvent pas satisfaire l'exigence
- **Responsable de la conformité** : Prioriser les écarts selon le risque réglementaire

**Étape 5 : Documentation des écarts**

- Documenter TOUS les écarts identifiés dans le Registre des écarts
- Champs du Registre des écarts :
  - ID d'écart (identifiant unique)
  - ID d'exigence (quelle exigence n'est pas satisfaite)
  - Type d'écart (Total, Partiel, Mise en œuvre)
  - Description de l'écart (ce qui manque)
  - Risque/Impact (conséquence du non-respect)
  - Priorité (Critique/Élevée/Moyenne/Faible)
  - Plan de remédiation (comment fermer l'écart)
  - Partie responsable (qui remédiera)
  - Date cible (quand l'écart sera fermé)
  - Statut (Ouvert, En cours, Fermé)

## Priorisation des écarts

**Facteur 1 : Niveau réglementaire** (de ISMS-POL-00)

- **Niveau 1 Obligatoire** : Priorité la plus élevée (obligation légale, application directe)
- **Niveau 2 Conditionnel** : Priorité élevée si la condition est remplie
- **Niveau 3 Informatif** : Priorité moindre (bonne pratique, non obligatoire légalement)

**Facteur 2 : Gravité des conséquences juridiques**

- **Pénal/Amendes sévères** : Priorité la plus élevée
- **Sanctions civiles/Amendes modérées** : Priorité élevée
- **Dommage réputationnel** : Priorité Moyenne-Élevée
- **Sanctions mineures/Avertissements** : Priorité moindre

**Facteur 3 : Délai de conformité**

- **Immédiat** (délai passé ou < 30 jours) : Priorité la plus élevée
- **Court terme** (30-90 jours) : Priorité élevée
- **Moyen terme** (90 jours - 1 an) : Priorité moyenne
- **Long terme** (> 1 an) : Priorité moindre

**Matrice de priorisation** :

**Priorité : CRITIQUE** (Action immédiate requise)
- Écart total ou partiel dans une réglementation de Niveau 1
- Délai passé ou < 30 jours
- Conséquence juridique sévère (responsabilité pénale, amendes importantes)
- Affecte les opérations métier critiques

**Priorité : ÉLEVÉE** (Urgent, planifier la remédiation)
- Écart total ou partiel dans une réglementation de Niveau 1
- Délai 30-90 jours
- Conséquence juridique significative (sanctions civiles, amendes modérées)
- Client ou contractuel

**Priorité : MOYENNE** (Planifier et exécuter)
- Écart partiel dans le Niveau 1, ou écart total dans le Niveau 2 (si applicable)
- Délai 90 jours - 1 an
- Conséquence juridique modérée ou risque réputationnel
- Opérations internes

**Priorité : FAIBLE** (Planification stratégique)
- Écart de mise en œuvre uniquement (contrôle défini, mise en œuvre en cours)
- Écart dans le Niveau 3 (informatif/bonne pratique)
- Délai > 1 an
- Conséquence mineure ou nulle

**Exemples de priorisations** :

| Description de l'écart | Niveau | Délai | Conséquence | Complexité | Priorité | Justification |
|------------------------|--------|-------|-------------|------------|----------|---------------|
| Absence de processus de notification pour l'exigence 72h | Niveau 1 | 30 jours | Amendes importantes (RGPD) | Faible | CRITIQUE | Niveau 1, délai imminent, sanction sévère |
| Mise en œuvre partielle du chiffrement (repos seulement) | Niveau 1 | 90 jours | Amendes modérées | Moyen | ÉLEVÉE | Niveau 1, écart partiel, délai moyen terme |
| Absence de programme de tests de pénétration | Niveau 2 (PCI DSS s'applique) | 6 mois | Perte de capacité de traitement des cartes | Élevée | ÉLEVÉE | Niveau 2 mais critique pour le métier |
| Formation de sensibilisation incohérente | Niveau 1 | Aucun délai spécifique | Mineur (violation de politique) | Faible | MOYENNE | Écart de mise en œuvre, faible complexité, pas de pression |
| Absence de procédure de test de biais IA | Niveau 3 (NIST AI) | Aucun | Réputationnel | Élevée | FAIBLE | Informatif seulement, complexe, aucune obligation légale |

## Approches de remédiation des écarts

**Option 1 : Mettre en œuvre un nouveau contrôle**

- Quand : Écart total, aucun contrôle existant ne traite l'exigence
- Action : Créer et mettre en œuvre un contrôle propre à l'organisation (Section 3.5)

**Option 2 : Améliorer un contrôle existant**

- Quand : Écart partiel, le contrôle existant est proche mais incomplet
- Action : Étendre le périmètre, ajouter des capacités ou améliorer la mise en œuvre

**Option 3 : Mettre en œuvre une combinaison de contrôles**

- Quand : Exigence complexe nécessitant plusieurs contrôles conjugués
- Action : Mettre en œuvre plusieurs contrôles (Annexe A et/ou organisationnels) qui satisfont collectivement l'exigence

**Option 4 : Mettre en œuvre un contrôle compensatoire**

- Quand : Le contrôle idéal ne peut être mis en œuvre (contraintes techniques, coût, opérations) mais une approche alternative atteint le même objectif
- Processus : Documenter la justification → Identifier le contrôle compensatoire → Obtenir l'approbation du Conseiller juridique et de la Direction → Mettre en œuvre → Documenter dans la matrice avec annotation
- Attention : Les régulateurs/auditeurs peuvent contester les contrôles compensatoires ; une justification solide et des preuves d'efficacité sont requises

**Option 5 : Accepter le risque**

- Quand : L'écart existe mais le coût/complexité dépasse le risque, OU l'écart est de faible priorité avec des ressources limitées
- Processus : Évaluation des risques → Documentation de la justification → Approbation de la Direction générale → Enregistrement dans le Registre des risques → Surveillance continue
- Restrictions :
  - IMPOSSIBLE d'accepter le risque pour les exigences de Niveau 1 Obligatoires
  - NE DEVRAIT PAS accepter le risque pour les écarts de priorité Élevée
  - DOIT réviser l'acceptation de risque si les circonstances changent

### Planification de la remédiation

Pour chaque remédiation d'écart :

**Développer un plan de remédiation** :

- ID et description de l'écart
- Approche de remédiation choisie
- Étapes de mise en œuvre détaillées
- Partie responsable
- Ressources requises (budget, personnel, technologie)
- Calendrier (date de début, jalons, date de complétion)
- Dépendances
- Critères de succès

**Obtenir les approbations** → **Exécuter le plan** → **Vérifier la fermeture**

## Suivi des écarts

### Registre des écarts

**Champs du Registre des écarts** :

- **ID d'écart** : Identifiant unique (ECR-AAAA-###)
- **Date d'identification** : Quand l'écart a été identifié
- **ID d'exigence** : Quelle exigence n'est pas satisfaite
- **Nom de la réglementation** : Réglementation parente
- **Type d'écart** : Total, Partiel, Mise en œuvre
- **Description de l'écart** : Ce qui manque (clair, spécifique)
- **Contrôle(s) actuel(s)** : Contrôles existants (si écart partiel)
- **Risque/Impact** : Conséquence du non-respect
- **Priorité** : Critique/Élevée/Moyenne/Faible
- **Approche de remédiation** : Nouveau contrôle, Amélioration, Combinaison, Compensatoire, Acceptation du risque
- **Plan de remédiation** : Résumé ou lien vers le plan détaillé
- **Partie responsable** : Qui gère la remédiation
- **Date de fermeture cible** : Quand l'écart sera fermé
- **Statut** : Ouvert, En cours, En attente d'approbation, Fermé, Risque accepté
- **Date de fermeture réelle** : Quand l'écart a effectivement été fermé
- **Vérification** : Comment la fermeture a été vérifiée
- **Notes** : Contexte complémentaire

### Processus de gestion des écarts

**Revue trimestrielle des écarts** :

- Responsable SMSI, Responsable de la conformité, Conseiller juridique examinent le Registre
- Évaluation de l'avancement des plans de remédiation
- Re-priorisation si les circonstances ont changé
- Identification des remédiations en retard, escalade si nécessaire
- Rapport du statut des écarts à la Direction générale

**Indicateurs clés de performance** :

- Nombre total d'écarts ouverts (par priorité)
- Délai moyen de fermeture des écarts (par priorité)
- Vieillissement des écarts (ouverts > 90 jours, > 180 jours, > 1 an)
- Taux de fermeture des écarts (par mois/trimestre)
- Pourcentage d'exigences satisfaites (exigences avec cartographie Primaire / total des exigences)

---

# Exigences de traçabilité

La traçabilité est la capacité de relier les réglementations, les exigences, les contrôles et les preuves dans les deux sens. Elle est fondamentale pour la préparation à l'audit et la démonstration de la conformité.

## Traçabilité directe

### La chaîne de traçabilité directe

**Définition** : La traçabilité directe est la capacité de partir d'une réglementation et de remonter jusqu'aux preuves démontrant la conformité.

**La chaîne directe** :
```
Réglementation (dans ISMS-POL-00)
    ↓
Exigences extraites (dans le Registre des exigences)
    ↓
Contrôles cartographiés (dans la Matrice de cartographie)
    ↓
Contrôles mis en œuvre (dans la documentation, politiques, procédures)
    ↓
Preuves collectées (dans le Registre des preuves et le référentiel)
```

**Exemple de traçabilité directe** :

**Point de départ** : Article 32 du Règlement sur la protection des données (« Sécurité du traitement »)

**Étape 1** : Identifier dans ISMS-POL-00
- ID de réglementation : REG-DP01 | Niveau : 1 - Obligatoire | Statut : Applicable

**Étape 2** : Trouver les exigences extraites dans le Registre
- REG-DP01-32-001 : « Mettre en œuvre le chiffrement pour les données personnelles au repos et en transit »
- REG-DP01-32-002 : « Mettre en œuvre des contrôles d'accès pour restreindre l'accès aux données personnelles »
- REG-DP01-32-003 : « Effectuer des tests et évaluations réguliers des mesures de sécurité »

**Étape 3** : Identifier les contrôles cartographiés dans la Matrice
- REG-DP01-32-001 → A.8.24 (Primaire)
- REG-DP01-32-002 → A.5.15 (Primaire), A.5.16 (Primaire), A.5.18 (Primaire)
- REG-DP01-32-003 → A.5.36 (Primaire), A.8.8 (Secondaire)

**Étape 4** : Revoir les contrôles mis en œuvre
- A.8.24 : Politique de chiffrement v2.1, Procédures de gestion des clés
- A.5.15 : Politique de contrôle des accès v3.0
- A.5.16 : Norme de gestion des identités
- A.5.18 : Procédure d'attribution des droits d'accès
- A.5.36 : Procédure de surveillance de la conformité
- A.8.8 : Politique de gestion des vulnérabilités, Norme de tests de pénétration

**Étape 5** : Localiser les preuves
- A.8.24 : Configuration de chiffrement au repos, configuration TLS, journaux de rotation des clés
- A.5.15/16/18 : Matrice de contrôle des accès, journaux de demande/approbation d'accès, rapports de revue trimestrielle
- A.5.36/A.8.8 : Rapport annuel de tests de pénétration, résultats de scans trimestriels, suivi des remédiations

**Résultat** : Capacité à démontrer à l'auditeur la traçabilité complète depuis la réglementation jusqu'aux preuves.

## Traçabilité inverse

### La chaîne de traçabilité inverse

**Définition** : La traçabilité inverse est la capacité de partir d'une preuve (ou d'un contrôle) et de remonter jusqu'aux réglementations qu'elle/il satisfait.

**La chaîne inverse** :
```
Preuves (dans le Registre des preuves et le référentiel)
    ↓
Contrôle mis en œuvre (documenté dans politiques, procédures)
    ↓
Exigences cartographiées (dans la Matrice de cartographie)
    ↓
Réglementation source (dans ISMS-POL-00)
```

**Exemple de traçabilité inverse** :

**Point de départ** : Document Politique de chiffrement (v2.1)

**Étape 1** : Identifier comme preuve d'un contrôle
- Contrôle : A.8.24 Utilisation de la cryptographie

**Étape 2** : Trouver le contrôle dans la Matrice
- La colonne A.8.24 montre des cartographies vers plusieurs exigences :
  - REG-DP01-32-001 (Primaire) | REG-FIN05-15-003 (Primaire) | REG-HEALTH-12-001 (Primaire) | REG-SEC15-4.4-002 (Primaire)

**Étape 3** : Remonter jusqu'aux réglementations
- REG-DP01-32-001 → Règlement sur la protection des données, Article 32
- REG-FIN05-15-003 → Règlement financier, Section 15
- REG-HEALTH-12-001 → Loi sur la sécurité des données de santé, Article 12
- REG-SEC15-4.4-002 → Norme de sécurité, Section 4.4

**Résultat** : Une seule politique de chiffrement satisfait des exigences issues de QUATRE réglementations différentes.

### Pourquoi la traçabilité inverse est importante

- **Efficacité des preuves** : Identifier quelle preuve satisfait quelles exigences ; éviter la collecte de preuves dupliquées
- **Justification des contrôles** : Expliquer POURQUOI un contrôle existe (quelles réglementations l'imposent)
- **Analyse d'impact** : Si un contrôle est modifié, identifier immédiatement les exigences affectées
- **Efficacité de l'audit** : Présenter les preuves une fois, satisfaire plusieurs besoins d'audit

## Traçabilité des modifications

### Types de modifications requérant une traçabilité

**Modifications réglementaires** → **Modifications des contrôles** → **Modifications organisationnelles**

### Analyse d'impact par traçabilité

**Lors d'une modification réglementaire** :
1. Identifier la réglementation modifiée dans ISMS-POL-00
2. Utiliser la traçabilité directe pour trouver toutes les exigences extraites de cette réglementation
3. Revoir le texte réglementaire modifié — exigences existantes toujours exactes ? Nouvelles exigences créées ? Exigences obsolètes ?
4. Réévaluer les cartographies de contrôles pour les exigences affectées
5. Mettre à jour les preuves si nécessaire
6. Communiquer les modifications aux parties prenantes

**Exemple** : L'Article 32 est modifié pour exiger « le chiffrement par algorithmes post-quantiques dans les 2 ans » → tracer vers REG-DP01-32-001 → mettre à jour l'exigence interprétée → évaluer A.8.24 → identifier l'écart → ajouter au Registre des écarts avec délai de 2 ans.

**Lors d'une modification de contrôle** :
1. Identifier le contrôle en cours de modification
2. Utiliser la traçabilité inverse pour trouver toutes les exigences cartographiées sur ce contrôle
3. Évaluer l'impact de la modification sur chaque exigence
4. Mettre à jour la Matrice et le Registre des écarts
5. Communiquer si des écarts sont créés

**Exemple** : A.8.15 — Réduction de la rétention des journaux de 2 ans à 6 mois → traçabilité inverse révèle REG-DP01-33-001 (1 an minimum) et REG-FIN05-10-002 (7 ans) → DEUX ÉCARTS CRÉÉS → Revenir en arrière ou implémenter une rétention différenciée.

## Piste d'audit

**Ce qu'il faut consigner** :

**Modifications du Registre des exigences** : Nouvelles exigences, modifications d'interprétation, changements de statut, archivage

**Modifications de la Matrice de cartographie** : Nouvelles cartographies, changements de type, suppressions

**Modifications du Registre des écarts** : Identification, re-priorisation, mises à jour de plan, changements de statut, fermeture

**Modifications des preuves** : Nouvelles collectes, mises à jour, vérifications

**Journal centralisé de conformité** (optionnel mais recommandé) :

| Date | Document | Type de modification | Description | Utilisateur | Justification |
|------|----------|---------------------|-------------|-------------|---------------|
| 2025-01-15 | Registre des exigences | Ajout | Ajout REG-DP01-32-004 (exigence AIP) | Analyste conformité | Nouvelle exigence issue des orientations DP |
| 2025-01-20 | Matrice de cartographie | Modification | REG-FIN05-23-005 → CTRL-ORG-TEC-001 S → P | Responsable SMSI | Système de détection de fraude intégralement mis en œuvre |
| 2025-02-01 | Registre des écarts | Changement de statut | ECR-2025-003 : Ouvert → Fermé | RSSI | Programme de tests de pénétration mis en œuvre et vérifié |

**Utilisations de la piste d'audit** :

- Démontre une gestion active (le cadre n'est pas statique)
- Soutient les audits internes/externes
- Permet l'analyse forensique en cas d'incident de conformité
- Défense réglementaire — démontre la bonne foi et la diligence raisonnable

---

# Gestion des exigences chevauchantes

De nombreuses réglementations imposent des contrôles de sécurité similaires ou identiques. Plutôt que de dupliquer les mises en œuvre, l'[Organisation] identifie les chevauchements et met en œuvre selon la norme la plus stricte, atteignant simultanément la conformité avec plusieurs réglementations.

## Identification des exigences chevauchantes

### Scénarios de chevauchement courants

**Réglementations sur la protection des données** :

- RGPD (UE), CCPA (Californie), nLPD (Suisse), LGPD (Brésil) exigent toutes :
  - Le chiffrement des données personnelles
  - Les contrôles d'accès
  - La notification des violations
  - La minimisation des données
  - Exigences similaires, juridictions différentes

**Réglementations sectorielles** :

- Services financiers : Multiple régulateurs avec des exigences de cybersécurité chevauchantes
- Santé : Plusieurs lois sur la santé se chevauchent

**Harmonisation des cadres** :

- De nombreuses réglementations référencent ou s'alignent sur ISO 27001, NIST CSF 2.0, CIS Controls
- La mise en œuvre d'ISO 27001 satisfait souvent plusieurs exigences réglementaires

### Méthodes de détection des chevauchements

**Lors de l'extraction des exigences** :
- Lors de l'extraction d'une nouvelle réglementation, comparer aux exigences existantes dans le Registre
- Signaler les exigences similaires (langage similaire, intention similaire)

**Lors de la cartographie des contrôles** :
- La Matrice de cartographie montre visuellement les chevauchements
- Si une colonne de contrôle a déjà de nombreuses cartographies Primaires → probable chevauchement

**Analyse trimestrielle des chevauchements** :
- Examiner périodiquement le Registre et la Matrice
- Identifier les contrôles cartographiés comme Primaire pour 5+ exigences
- Documenter les chevauchements dans le champ Notes du Registre

## Identifier l'exigence la plus stricte

Lorsque des exigences chevauchantes existent, l'[Organisation] DOIT mettre en œuvre selon la norme LA PLUS STRICTE.

### Cadre de comparaison de la rigueur

**Spécifications techniques** :

| Exigence | Spécification | Comparaison de rigueur |
|----------|--------------|----------------------|
| REG-DP01 : « Utiliser le chiffrement conforme aux standards sectoriels » | Non spécifié | Moins stricte (vague) |
| REG-FIN05 : « Utiliser AES-128 ou supérieur » | AES-128 minimum | Modérément stricte |
| REG-SEC15 : « Utiliser AES-256 pour les données au repos » | AES-256 requis | **La plus stricte** |

**Mise en œuvre** : Utiliser AES-256 (satisfait les trois exigences)

**Fréquences de processus** :

| Exigence | Fréquence | Comparaison de rigueur |
|----------|-----------|----------------------|
| REG-DP01 : « Revue périodique des droits d'accès » | Non spécifié | Moins stricte |
| REG-FIN05 : « Revue annuelle des droits d'accès » | Annuelle | Modérément stricte |
| REG-PCI : « Revue trimestrielle des droits d'accès » | Trimestrielle | **La plus stricte** |

**Mise en œuvre** : Revues trimestrielles (satisfait les trois)

**Délais et échéances** :

| Exigence | Délai | Comparaison de rigueur |
|----------|-------|----------------------|
| REG-DP01 : « Notifier les personnes concernées sans délai injustifié » | Non spécifié | Moins stricte |
| REG-CCPA : « Dans un délai raisonnable » | Non spécifié | Moins stricte |
| REG-RGPD : « Notifier dans les 72 heures sauf risque faible » | 72 heures | **La plus stricte** |

**Mise en œuvre** : Processus de notification en 72 heures (satisfait les trois)

### Documentation de la détermination la plus stricte

**Dans le Registre des exigences** (champ Notes) :
- « Se chevauche avec [liste des IDs d'exigences] »
- « Exigence la plus stricte : [ID d'exigence] »
- « La mise en œuvre suit la norme la plus stricte »

**Dans la mise en œuvre du contrôle** :
- La description du contrôle référence l'exigence la plus stricte

**Registre des chevauchements** (optionnel) :
- Champs : ID de groupe de chevauchement, IDs d'exigences, Exigence la plus stricte, Justification de rigueur, Norme mise en œuvre, Preuves communes

## Démontrer la conformité à toutes les réglementations applicables

### La matrice montre la satisfaction multi-réglementaire

**Exemple (partiel)** :

| ID d'exigence | Exigence | A.8.24 Cryptographie | A.8.15 Journalisation | ... |
|---------------|----------|---------------------|----------------------|-----|
| REG-DP01-32-001 | Chiffrer données personnelles | **P** | | |
| REG-FIN05-15-003 | Chiffrer données financières | **P** | | |
| REG-HEALTH-12-001 | Chiffrer dossiers de santé | **P** | | |
| REG-SEC15-4.4-002 | Utiliser AES-256 | **P** | | |

**Interprétation** : A.8.24, mis en œuvre selon la norme REG-SEC15-4.4-002 (AES-256), satisfait QUATRE exigences réglementaires de QUATRE réglementations différentes. **Une seule mise en œuvre**, **un seul ensemble de preuves**, **quatre réglementations conformes**.

### Les preuves servent plusieurs exigences

**Scénario d'audit** :

- **Auditeur RGPD** : « Montrez-moi comment vous respectez l'exigence de chiffrement de l'Article 32 »
  → L'[Organisation] fournit : Politique de chiffrement v2.1, documentation de configuration, journaux de clés
- **Auditeur financier** : « Montrez-moi comment vous protégez les données financières »
  → L'[Organisation] fournit : **LES MÊMES** documents
- **Auditeur santé** : « Montrez-moi la protection des dossiers de santé »
  → L'[Organisation] fournit : **LES MÊMES** preuves

**Résultat** : Une politique, trois audits satisfaits. L'efficacité des preuves en action.

### Reporting de conformité par réglementation

| Réglementation | Total exigences | Satisfaites | Écarts | % Conformité |
|---------------|-----------------|-------------|--------|--------------|
| Règlement sur la protection des données (REG-DP01) | 45 | 42 | 3 | 93 % |
| Règlement financier (REG-FIN05) | 38 | 38 | 0 | 100 % |
| Loi santé (REG-HEALTH) | 22 | 20 | 2 | 91 % |
| Norme de sécurité (REG-SEC15) | 67 | 63 | 4 | 94 % |

**Flexibilité de reporting** :

- Reporting par réglementation (pour les audits réglementaires)
- Reporting par contrôle (pour l'audit de certification ISO 27001)
- Reporting par niveau (statut Niveau 1 vs. Niveau 2)
- Reporting d'efficacité des contrôles (contrôles satisfaisant le plus d'exigences = ROI élevé)

## Optimisation des preuves

### Étiquetage des preuves avec plusieurs exigences

Le **Registre des preuves** inclut le champ : « Satisfait les exigences »

- Champ multi-sélection listant TOUS les IDs d'exigences satisfaits par cette preuve
- Exemple :
  - **Preuve** : Politique de chiffrement v2.1
  - **Satisfait les exigences** : REG-DP01-32-001, REG-FIN05-15-003, REG-HEALTH-12-001, REG-SEC15-4.4-002

### Éviter la duplication des preuves

**Avant de collecter de nouvelles preuves** :
1. Vérifier si l'exigence appartient à un groupe de chevauchement (Notes du Registre)
2. Si oui, identifier le contrôle qui la satisfait dans la Matrice
3. Rechercher des preuves existantes dans le Registre des preuves
4. Si les preuves existantes satisfont l'exigence la plus stricte → Étiqueter avec le nouvel ID
5. NE PAS collecter de nouvelles preuves

**Exemple** : Nouvelle réglementation REG-NEWREG identifiée → Exigence REG-NEWREG-10-001 : « Chiffrer les données avec des algorithmes reconnus par le secteur » → Chevauchement identifié avec REG-DP01-32-001, REG-FIN05-15-003 → Politique de chiffrement v2.1 couvre déjà → **Action** : Ajouter REG-NEWREG-10-001 comme étiquette à la preuve existante.

---

# Contrôle documentaire et documents liés

## Informations documentaires

**ID du document** : ISMS-POL-A.5.31.3
**Titre** : Cadre d'extraction des exigences et de cartographie des contrôles
**Version** : 1.0
**Date d'entrée en vigueur** : [À déterminer lors de l'approbation]
**Classification** : Interne
**Propriétaire** : Responsable SMSI / Responsable de la conformité

**Fréquence de revue** : Annuellement ou lors de :

- Modifications réglementaires significatives affectant plusieurs réglementations
- Modifications majeures de la norme ISO 27001
- Modifications organisationnelles affectant le périmètre de conformité
- Améliorations méthodologiques identifiées lors de l'utilisation

**Prochaine date de revue** : [Date d'entrée en vigueur + 12 mois]

## Documents liés

**Cadre de politique SMSI** :

- **ISMS-POL-A.5.31.1** : Résumé exécutif et alignement des contrôles
  - Fournit la fondation du cadre et la structure de gouvernance
  - Définit les rôles référencés dans le présent document
- **ISMS-POL-A.5.31.2** : Méthodologie d'applicabilité réglementaire
  - Détermine QUELLES réglementations s'appliquent (entrée pour le présent document)
  - Maintient le registre réglementaire ISMS-POL-00
- **ISMS-POL-00** : Cadre d'applicabilité réglementaire
  - Liste maîtresse des réglementations applicables
  - Source des réglementations d'où les exigences sont extraites
- **ISMS-POL-A.5.31.4** : Cadre de gestion des modifications et des preuves (suivant)
  - Définit les processus de surveillance réglementaire et de gestion des preuves
  - S'appuie sur les cartographies de contrôles définies dans le présent document

**Guides de mise en œuvre** :

- **ISMS-IMP-A.5.31.3-UG/TG** : Processus d'extraction des exigences
  - Guide opérationnel étape par étape pour l'extraction des exigences
  - Met en œuvre la méthodologie d'extraction (Section 2)
- **ISMS-IMP-A.5.31.3-UG/TG** : Processus de cartographie des contrôles
  - Guide opérationnel étape par étape pour la cartographie
  - Met en œuvre la méthodologie de cartographie (Section 3)

**Cahiers d'évaluation** :

- **Cahier d'évaluation 3** : Registre d'extraction des exigences
  - Modèle pour le Registre des exigences (Section 2.3)
  - Format standardisé avec validation des données
- **Cahier d'évaluation 4** : Matrice de cartographie des contrôles
  - Modèle pour la Matrice (Section 3.3)
  - 93 contrôles Annexe A pré-remplies
  - Mise en forme conditionnelle pour la visualisation des écarts

**Normes et références externes** :

- **ISO/IEC 27001:2022** : Systèmes de management de la sécurité de l'information — Exigences
  - Annexe A : Catalogue de contrôles (93 contrôles référencés dans le présent document)
- **ISO/IEC 27002:2022** : Contrôles de sécurité de l'information
  - Guidance de mise en œuvre pour les contrôles Annexe A
  - Référence pour comprendre les capacités des contrôles lors de la cartographie

## Définitions

**Cartographie des contrôles** : Processus de liaison des exigences réglementaires aux contrôles ISO 27001 qui les satisfont.

**Contrôle Complémentaire (Co)** : Contrôle contribuant indirectement à la satisfaction d'une exigence réglementaire.

**Contrôle Primaire (P)** : Contrôle satisfaisant directement et substantiellement une exigence réglementaire.

**Contrôle Secondaire (S)** : Contrôle satisfaisant partiellement ou appuyant la satisfaction d'une exigence réglementaire.

**Écart** : Exigence réglementaire pour laquelle aucun contrôle n'existe ou les contrôles existants sont inadéquats.

**Registre des exigences** : Référentiel faisant autorité de toutes les exigences extraites des réglementations applicables.

**Traçabilité** : Capacité à remonter vers l'avant (réglementation → preuves) et vers l'arrière (preuves → réglementation) au travers des exigences et des contrôles.

---

**FIN DU DOCUMENT**

---

*La présente politique établit la méthodologie de traduction du texte réglementaire en contrôles opérationnels, permettant à l'[Organisation] de démontrer COMMENT elle satisfait les exigences réglementaires au travers d'une mise en œuvre systématique des contrôles.*

<!-- QA_VERIFIED: 2026-03-30 -->
