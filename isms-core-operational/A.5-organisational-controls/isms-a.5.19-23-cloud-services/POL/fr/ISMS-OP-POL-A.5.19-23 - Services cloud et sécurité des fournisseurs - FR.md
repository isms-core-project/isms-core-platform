<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.5.19-23-FR:operational:OP-POL:a.5.19-23 -->
**ISMS-OP-POL-A.5.19-23 — Services cloud et sécurité des fournisseurs**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Services cloud et sécurité des fournisseurs |
| **Type de document** | Politique opérationnelle |
| **Identifiant du document** | ISMS-OP-POL-A.5.19-23 |
| **Créateur du document** | Responsable de la Sécurité des Systèmes d'Information (RSSI) |
| **Propriétaire du document** | Directeur général (DG) |
| **Approuvé par** | Direction générale |
| **Date de création** | [Date] |
| **Version** | 0.1 |
| **Date de version** | [À déterminer] |
| **Classification** | Interne |
| **Statut** | Brouillon |

**Historique des versions** :

| Version | Date | Auteur | Modifications |
|---------|------|--------|---------------|
| 0.1 | [Date] | RSSI | Politique opérationnelle initiale pour ISO 27001:2022 |

**Cycle de révision** : Annuel
**Prochaine date de révision** : [Date d'entrée en vigueur + 12 mois]

**Approuvé par** : [RSSI / Direction générale]

**Documents connexes** :

- ISO/IEC 27001:2022 Contrôles A.5.19–A.5.23 — Sécurité des fournisseurs et des services cloud
- ISO/IEC 27002:2022 Contrôles 5.19–5.23 — Lignes directrices de mise en œuvre

**Contrôles Annexe A connexes** :

| Contrôle | Relation avec la sécurité des fournisseurs et des services cloud |
|----------|----------------------------------------------------------------|
| A.5.9 Inventaire des informations et des actifs | Les fournisseurs et services cloud sont répertoriés dans l'inventaire des actifs |
| A.5.12–13 Classification et étiquetage de l'information | La classification des données détermine les exigences de sécurité des fournisseurs |
| A.5.14 Transfert de l'information | Exigences de transfert chiffré pour l'échange de données avec les fournisseurs |
| A.5.15–16–18 Gestion des identités et des accès | Provisionnement et révocation des accès du personnel des fournisseurs |
| A.5.24–28 Gestion des incidents | La notification des incidents par les fournisseurs s'intègre au processus de gestion des incidents |
| A.5.30, A.8.13–14 Continuité d'activité et sauvegarde | Scénarios de perturbation des fournisseurs, validation des stratégies de sortie, sauvegardes indépendantes |
| A.5.31 Exigences légales, réglementaires et contractuelles | Obligations contractuelles, exigences nFADP/RGPD pour les sous-traitants |
| A.5.34 Vie privée et DCP | Accords de traitement des données, divulgation des sous-traitants ultérieurs, transferts transfrontaliers |
| A.8.8 Gestion des vulnérabilités | Engagements des fournisseurs en matière de correctifs, divulgation des vulnérabilités |
| A.8.10 Suppression de l'information | Vérification de la destruction des données par les fournisseurs en fin de contrat |
| A.8.24 Utilisation de la cryptographie | Exigences de chiffrement des données des fournisseurs au repos et en transit |

**Politiques internes connexes** :

- Politique de classification et de traitement de l'information
- Politique de gestion des incidents
- Politique de transfert de l'information
- Politique de vie privée et de protection des DCP
- Politique de continuité d'activité et de reprise après sinistre

---

# Politique relative aux services cloud et à la sécurité des fournisseurs

## Objet

La présente politique a pour objet de gérer la sécurité de l'information pour l'utilisation des services cloud et de garantir les exigences de sécurité des données des fournisseurs tiers, de leurs sous-traitants et de la chaîne d'approvisionnement.

Cette politique soutient la nLPD suisse (revDSG) en mettant en œuvre des mesures techniques et organisationnelles proportionnées aux risques pour protéger les données personnelles (y compris les données personnelles sensibles) lorsqu'elles sont traitées par des fournisseurs externes et des prestataires de services cloud. Lorsque l'organisation traite des données de personnes dans l'UE/EEE, les exigences du RGPD s'appliquent également. Les contrôles de sécurité des fournisseurs et des services cloud sont des mesures essentielles pour démontrer la conformité aux obligations de protection des données dans le cadre des deux régimes.

## Champ d'application

Tous les employés et utilisateurs tiers.

Tous les fournisseurs tiers et prestataires de services cloud qui traitent, stockent ou transmettent des données confidentielles ou personnelles.

Tous les services cloud (IaaS, PaaS, SaaS) utilisés par l'organisation.

## Principe

Les fournisseurs tiers et les prestataires de services cloud doivent satisfaire aux exigences de l'organisation, de la législation et de la réglementation en matière de sécurité des données. La confiance accordée aux fournisseurs doit être vérifiée, non présumée — une validation fondée sur des preuves de la posture de sécurité des fournisseurs est requise par le biais d'une diligence raisonnable systématique, d'engagements contractuels et d'une surveillance continue.

Les accords de services cloud sont souvent prédéfinis et non ouverts à la négociation. Dans ce cas, l'organisation doit évaluer si les conditions standard du prestataire répondent à ses exigences de sécurité et documenter tout risque résiduel. Lorsque les conditions ne sont pas négociables et ne répondent pas aux exigences, des mesures compensatoires doivent être identifiées ou un prestataire alternatif doit être évalué.

L'organisation doit comprendre et documenter le modèle de responsabilité partagée pour chaque service cloud. Les responsabilités en matière de sécurité sont réparties entre le prestataire de services cloud et l'organisation, et cette répartition varie selon le modèle de service (IaaS, PaaS, SaaS). L'organisation reste responsable de la sécurité de ses données, de la gestion des identités et des accès et de la protection des points de terminaison, quel que soit le modèle de service. Le prestataire est responsable de la sécurité de l'infrastructure sous-jacente. Les domaines de responsabilité partagée doivent être explicitement documentés et examinés.

**La documentation sur la responsabilité partagée doit inclure** :

| Domaine de responsabilité | Prestataire responsable | Organisation responsable | Remarques |
|--------------------------|------------------------|------------------------|-----------|
| Sécurité physique du centre de données | Oui | | Le prestataire contrôle l'accès physique |
| Infrastructure réseau | Oui | | Le prestataire sécurise le réseau sous-jacent |
| Infrastructure hôte | Oui (IaaS/PaaS/SaaS) | Oui (IaaS uniquement — correctifs du système d'exploitation) | Pour IaaS, l'organisation gère le système d'exploitation |
| Sécurité des applications | Oui (SaaS uniquement) | Oui (IaaS/PaaS) | Pour SaaS, le prestataire est responsable |
| Chiffrement des données au repos | Oui (par défaut) | Oui (gestion des clés) | L'organisation peut apporter ses propres clés (BYOK) |
| Gestion des identités et des accès | | Oui | L'organisation est toujours responsable |
| Classification et traitement des données | | Oui | L'organisation est toujours responsable |
| Sécurité des points de terminaison | | Oui | L'organisation est toujours responsable |

Les modèles de responsabilité partagée doivent être documentés pour chaque service cloud **CRITIQUE** et révisés annuellement.

---

## Registre des fournisseurs et des services cloud

Tous les fournisseurs tiers et services cloud doivent être enregistrés et consignés dans le **Registre des fournisseurs et des services cloud**.

**Emplacement du registre** : [Plateforme GRC, système d'approvisionnement ou feuille de calcul dédiée dans SharePoint/équivalent]

**Responsable du registre** : [RSSI, Responsable des achats ou Responsable IT]

**Accès** : L'accès au registre est limité au personnel autorisé (direction IT, équipe sécurité de l'information, achats). Le registre est classifié **INTERNE**.

**Fréquence de mise à jour** : Le registre doit être révisé et mis à jour au minimum **trimestriellement** ou lors de tout nouvel engagement fournisseur, changement de contrat ou sortie d'un fournisseur.

Les fournisseurs et services cloud doivent être évalués quant à leur criticité pour l'activité.

Les fournisseurs et services cloud doivent être classifiés en fonction des données traitées, stockées ou transmises et de leur criticité pour les opérations commerciales :

| Classification | Critères | Fréquence de révision |
|---------------|----------|-----------------------|
| **Critique** | Accès aux données CONFIDENTIEL/RESTREINT, OU opérations commerciales essentielles (une interruption entraîne un impact immédiat sur l'activité), OU traitement de données personnelles sensibles (nLPD art. 5) | Annuellement |
| **Important** | Accès aux données INTERNE mais pas CONFIDENTIEL, OU services de support (une interruption entraîne une perturbation modérée dans les 24–48 heures), OU traitement limité de données personnelles | Tous les deux ans |
| **Standard** | Aucun accès aux données ou données PUBLIQUES uniquement, OU services de commodité (facilement remplaçables, impact minimal sur l'activité) | Lors du renouvellement du contrat |

**Exemples** : Critique — prestataire d'hébergement cloud, sous-traitant de la paie, service de sauvegarde, CRM avec données clients. Important — outil d'automatisation du marketing, SaaS de gestion de projet, outils de collaboration. Standard — fournisseur de fournitures de bureau, services de gardiennage (sans accès aux données).

En outre, les informations suivantes doivent au minimum être saisies :

- Nom et coordonnées du fournisseur ou du service cloud
- Ce qu'il fait pour nous (description du service)
- Les données qu'il traite, stocke ou transmet
- Niveau de classification des données (PUBLIC, INTERNE, CONFIDENTIEL, RESTREINT)
- Si nous disposons d'un contrat et d'une copie du contrat
- Les garanties que nous avons sur leur sécurité des données (certifications, rapports d'audit)
- Lieux de traitement et de stockage des données (pays et région)
- Date d'expiration du contrat et prochaine date de révision
- Sous-traitants ultérieurs utilisés par le fournisseur (lorsque ceux-ci sont connus)

## Exigences de sécurité de l'information

Les fournisseurs et prestataires de services cloud devraient détenir des certifications pertinentes en matière de sécurité de l'information couvrant les services fournis. Au minimum, ils devraient disposer de :

- Une certification ISO 27001, **ou**
- Un rapport SOC 2 Type II (récent, datant de moins de 12 mois)

Pour les prestataires de services cloud traitant des données personnelles, ISO 27018 (protection des DCP dans les clouds publics) ou une preuve équivalente de contrôles de protection des DCP est attendue en supplément.

La certification CSA STAR Niveau 2 (ISO 27001 + Cloud Controls Matrix) est reconnue comme un indicateur fort de maturité de sécurité spécifique au cloud.

Lorsqu'un fournisseur ne peut pas fournir de certification reconnue, l'organisation doit effectuer une évaluation des risques documentée et, si le fournisseur est engagé, mettre en œuvre des mesures compensatoires et obtenir l'acceptation du risque de la part du Responsable de la sécurité de l'information et du propriétaire du risque.

**Mesures compensatoires potentielles** :

- Conditions contractuelles renforcées avec des obligations de sécurité spécifiques (chiffrement, journalisation des accès, notification des incidents)
- Questionnaire de sécurité complété annuellement avec des réponses vérifiées par rapport aux résultats ultérieurs
- Accès aux données limité — restreindre le fournisseur aux données non personnelles ou non confidentielles uniquement
- Droits d'audit — droit de mener un audit de sécurité ou un test d'intrusion (si contractuellement réalisable)
- Dispositions de séquestre — séquestre du code ou des données pour la continuité d'activité
- Exigences en matière d'assurance responsabilité cyber

## Audit et révision

Chaque fournisseur et service cloud fait l'objet d'un audit et d'une révision de la sécurité des données conformément au calendrier basé sur les risques suivant :

| Classification du fournisseur | Fréquence de révision | Périmètre de révision |
|------------------------------|----------------------|----------------------|
| **Critique** (accès aux données CONFIDENTIEL/RESTREINT ou opérations essentielles) | Annuellement | Révision complète de conformité, performance SLA, actualité des certifications, réévaluation des risques |
| **Important** (accès limité aux données ou services de support) | Tous les deux ans | Validation de la conformité, statut du contrat, vérification de la certification |
| **Standard** (sans accès aux données, services de commodité) | Lors du renouvellement du contrat | Besoin commercial continu, vérification de sécurité de base |

Le niveau d'audit et de révision est fondé sur la classification du risque du fournisseur et la sensibilité des données impliquées.

Les fournisseurs de services cloud sont soumis aux mêmes exigences d'audit et de révision.

### Approche d'audit des services cloud

Les grands prestataires de services cloud (AWS, Azure, Google Cloud, Microsoft 365, Salesforce, etc.) n'autorisent généralement pas les audits directs par les clients en raison des contraintes de sécurité multi-locataires et d'évolutivité opérationnelle.

**Mécanismes d'assurance alternatifs** (acceptés en lieu et place d'un audit direct) :

- Rapports indépendants de tiers : SOC 2 Type II, certification ISO 27001, attestation CSA STAR
- Certifications de conformité : ISO 27017, ISO 27018 et attestations sectorielles le cas échéant
- Rapports de transparence : documentation de sécurité publiée par le prestataire, matrices de conformité, listes de sous-traitants ultérieurs
- Tableaux de bord de santé des services : disponibilité du service en temps réel et divulgation des incidents

L'organisation doit obtenir et examiner les rapports d'audit indépendants les plus récents (**datant de moins de 12 mois**) pour chaque service cloud Critique annuellement.

Lorsqu'un prestataire cloud ne fournit pas de rapports indépendants de tiers, le service ne doit pas être utilisé pour des données CONFIDENTIEL ou RESTREINT sans approbation du RSSI et acceptation documentée du risque résiduel.

## Gestion des risques

Chaque fournisseur traitant des données confidentielles ou personnelles doit être inscrit au Registre des risques et géré dans le cadre du processus de gestion des risques de l'organisation.

Les risques liés aux services cloud doivent inclure une évaluation de :

- Disponibilité du service et impact sur l'activité en cas d'interruption
- Résidence des données et exposition juridictionnelle
- Dépendance vis-à-vis du fournisseur et faisabilité de la sortie
- Risque de concentration (dépendance envers un seul prestataire pour les services critiques) — lorsqu'un seul prestataire héberge plus de 50 % des services critiques ou plus de 75 % des données CONFIDENTIEL, cela doit être signalé dans le registre des risques avec un plan d'atténuation ou un risque résiduel accepté. Les options d'atténuation comprennent la diversification multi-prestataire, le déploiement multi-régional chez le même prestataire et une stratégie de sortie validée
- Risque lié aux sous-traitants ultérieurs (traitement des données en aval)

## Sélection des fournisseurs et des services cloud

Les fournisseurs et les services cloud doivent être sélectionnés en fonction de leur capacité à répondre aux besoins de l'activité.

Avant d'engager un fournisseur ou un prestataire de services cloud, une diligence raisonnable en matière de sécurité des données doit être effectuée, comprenant :

- Un niveau acceptable de sécurité des données avec des risques identifiés, enregistrés et gérés
- Des références appropriées de clients existants
- Des certifications appropriées (ISO 27001, SOC 2 Type II ou équivalent — voir Exigences de sécurité de l'information ci-dessus)
- Des accords et contrats fournisseurs appropriés incluant les exigences de sécurité des données
- La conformité légale et réglementaire, y compris la nLPD (revDSG) et le RGPD le cas échéant
- L'évaluation des lieux de traitement et de stockage des données par rapport aux exigences de résidence des données de l'organisation
- La vérification que les conditions standard du prestataire répondent aux exigences de sécurité de l'organisation (notamment pour les services cloud avec des accords non négociables)
- L'évaluation de la faisabilité de la sortie : capacité d'exportation des données, formats pris en charge, assistance à la transition et prestataires alternatifs

## Contrats, accords et accords de traitement des données

Un contrat, accord et/ou accord de traitement des données approprié doit être en place et exécutoire avant d'engager tout fournisseur ou prestataire de services cloud pour traiter, stocker ou transmettre des informations confidentielles ou personnelles.

Les contrats et accords doivent aborder, au minimum :

- Description des données traitées, stockées ou transmises
- Exigences et obligations en matière de sécurité de l'information
- Exigences de notification des incidents (voir Gestion des incidents de sécurité ci-dessous)
- Droits d'audit, le cas échéant, réalisables et autorisés (il est reconnu que les grands prestataires cloud n'autorisent généralement pas l'audit direct ; l'attestation indépendante de tiers est acceptée comme preuve alternative)
- Exigences de divulgation et d'approbation des sous-traitants ultérieurs
- Obligations de restitution et de destruction des données à la résiliation du contrat
- Accords de niveau de service couvrant la disponibilité, la réactivité du support et les indicateurs de sécurité
- Dispositions de sortie incluant l'exportation des données, l'assistance à la transition et les délais de préavis de résiliation

Toutes les politiques de l'organisation s'appliquent à l'utilisation du fournisseur ou du service cloud.

### Exigences relatives aux sous-traitants et aux sous-traitants ultérieurs

L'utilisation par les fournisseurs de sous-traitants ou de sous-traitants ultérieurs doit être approuvée par le Responsable de la sécurité de l'information. Les sous-traitants et sous-traitants ultérieurs sont soumis aux mêmes conditions et exigences de sécurité que le fournisseur.

**Modèles d'approbation** :

- **Autorisation spécifique** : L'organisation approuve chaque sous-traitant ultérieur individuellement (préféré pour les fournisseurs Critiques traitant des données CONFIDENTIEL ou RESTREINT)
- **Autorisation générale avec notification** : L'organisation accorde une autorisation générale pour les sous-traitants ultérieurs répondant à des critères spécifiés, avec un préavis d'au moins 30 jours en cas de modifications (acceptable pour les fournisseurs Importants)

Les prestataires de services cloud doivent divulguer leur liste de sous-traitants ultérieurs. L'organisation doit être notifiée des modifications apportées aux sous-traitants ultérieurs **au moins 30 jours à l'avance** et doit conserver le droit de s'y opposer lorsque cela est contractuellement réalisable. Lorsque les droits d'opposition ne peuvent pas être obtenus (comme c'est souvent le cas avec les grands prestataires cloud), cette limitation doit être documentée dans le registre des risques comme risque résiduel avec des mesures compensatoires (chiffrement, surveillance des accès).

### Accords de traitement des données (nLPD/RGPD)

Tous les fournisseurs traitant des données personnelles pour le compte de l'organisation doivent avoir en place un accord de traitement des données répondant aux exigences de la nLPD suisse (revDSG) art. 9 et, le cas échéant, du RGPD art. 28.

L'accord de traitement des données doit aborder :

- Objet et durée du traitement
- Nature et finalité du traitement
- Type de données personnelles et catégories de personnes concernées
- Obligations et droits du responsable du traitement
- Exigences d'approbation des sous-traitants ultérieurs (spécifique ou générale avec notification)
- Mesures de sécurité des données (techniques et organisationnelles)
- Assistance avec les demandes relatives aux droits des personnes concernées
- Restitution ou suppression des données à la résiliation
- Droits d'audit et d'inspection

### Transferts transfrontaliers de données

Lorsque des fournisseurs ou des prestataires de services cloud traitent ou stockent des données personnelles en dehors de la Suisse, l'organisation doit vérifier qu'une protection adéquate des données existe dans le pays de destination conformément à la liste d'adéquation du Conseil fédéral suisse (Annexe 1 de l'Ordonnance sur la protection des données).

Pour les transferts vers des pays ne figurant pas sur la liste d'adéquation, des garanties appropriées doivent être en place :

- Clauses contractuelles types (CCT) adaptées à la conformité au droit suisse, **ou**
- Règles d'entreprise contraignantes (REC) approuvées par le PFPDT, **ou**
- Autres mécanismes de transfert reconnus

Pour les transferts vers les États-Unis, l'organisation doit vérifier que l'organisation destinataire est certifiée dans le cadre du Cadre de confidentialité des données Suisse-États-Unis (DPF). Lorsque le prestataire a son siège aux États-Unis et est soumis au US CLOUD Act, une évaluation des risques juridictionnels doit être documentée, incluant les dispositions de chiffrement et de gestion des clés ainsi que les engagements du prestataire en matière de contestation judiciaire.

## Gestion des incidents de sécurité

Les fournisseurs et prestataires de services cloud doivent disposer d'un processus de gestion des incidents de sécurité.

Les incidents de sécurité des fournisseurs et des services cloud qui ont un impact sur les informations confidentielles ou personnelles doivent être signalés à l'organisation dans les délais suivants :

| Classification du fournisseur | Délai de notification | Remarques |
|------------------------------|----------------------|-----------|
| **Critique** | **12 heures** (obligatoire) | Doit être contractuellement engagé |
| **Important** | **24 heures** (cible) | Au mieux si 12 heures n'est pas réalisable |
| **Standard** | **72 heures** (acceptable) | Acceptable si aucune violation de données personnelles n'est impliquée |

Lorsqu'un fournisseur ne peut pas s'engager sur le délai de 12 heures, cela doit être documenté comme risque résiduel avec des mesures compensatoires (révisions plus fréquentes des fournisseurs, surveillance renforcée, prestataire de sauvegarde).

La notification doit inclure, au minimum :

- Description de l'incident
- Systèmes et données affectés
- Mesures de confinement prises
- Impact estimé et calendrier de résolution

Les incidents de sécurité des fournisseurs et des services cloud doivent être gérés dans le cadre du processus de gestion des incidents de l'organisation, conformément à la Politique de gestion des incidents.

Lorsqu'un incident d'un fournisseur implique une violation de données personnelles, l'organisation doit évaluer les obligations de notification en vertu de la nLPD (notification au PFPDT dès que possible) et, le cas échéant, du RGPD art. 33 (notification à l'autorité de contrôle dans les 72 heures).

Le cas échéant, le processus de gestion des incidents du fournisseur doit être suivi en coordination avec les propres procédures de l'organisation.

## Fin de contrat

À la fin du contrat, le fournisseur ou le prestataire de services cloud doit confirmer par écrit qu'il a rempli ses obligations contractuelles et légales concernant la destruction des informations confidentielles et personnelles de l'organisation.

Le cas échéant, réalisable et pertinent (en reconnaissant les limitations liées aux services cloud), les actions suivantes doivent être effectuées :

- Toutes les données de l'organisation sont restituées dans un format utilisable ou détruites de manière sécurisée, conformément aux instructions de l'organisation
- Une confirmation écrite de la destruction des données est fournie, incluant la méthode utilisée
- Tous les accès aux systèmes et informations de l'organisation sont révoqués
- Tous les actifs de l'organisation (physiques et logiques) sont restitués
- Des certificats de destruction sont obtenus lorsque les données étaient classifiées CONFIDENTIEL ou RESTREINT

## Modifications des fournisseurs de services cloud

Les modifications apportées à un fournisseur de services cloud nécessitent l'approbation formelle, écrite et documentée du PDG ou d'une autorité déléguée.

Les modifications doivent suivre la Politique de gestion des changements et le processus de gestion des changements.

Les modifications apportées aux fournisseurs cloud sont des changements importants et ne doivent pas être prises à la légère. Ces modifications doivent être traitées comme un projet avec les ressources appropriées, la gestion des risques, la gestion de projet et la communication avec les parties prenantes.

L'organisation doit maintenir une stratégie de sortie pour chaque service cloud **Critique** afin de garantir qu'une transition ou une sortie puisse être exécutée de manière contrôlée si nécessaire.

**Composantes minimales de la stratégie de sortie** :

- **Capacité d'exportation des données** : processus d'exportation des données documenté et formats pris en charge (CSV, JSON, API, restauration de sauvegarde)
- **Calendrier de transition** : délai estimé pour migrer vers un prestataire alternatif (supposer le pire cas : sortie forcée)
- **Prestataires alternatifs** : au moins un prestataire alternatif pré-identifié et évalué
- **Coûts de transition** : coût estimé (licences, services professionnels, migration des données)
- **Dépendances** : intégrations et dépendances identifiées nécessitant une reconfiguration
- **Test de sortie** : vérification du fonctionnement de l'exportation des données (test effectué annuellement pour les services Critiques)

Les stratégies de sortie doivent être révisées **annuellement** ou lors du renouvellement du contrat.

---

## Preuves

Les preuves suivantes démontrent la conformité à cette politique :

- **Registre des fournisseurs et des services cloud** — complet, à jour, avec classification des données et dates de révision ; *révisé trimestriellement*
- **Contrats signés et accords de traitement des données** — pour tous les fournisseurs traitant des données confidentielles ou personnelles ; *registre des contrats maintenu par [Achats/Juridique]*
- **Certifications des fournisseurs conservées** — ISO 27001, SOC 2 Type II, CSA STAR (récentes, datant de moins de 12 mois) ; *révisées annuellement pour les fournisseurs Critiques*
- **Comptes rendus des réunions de révision des fournisseurs** et rapports de performance — *révisions annuelles pour les Critiques, biennales pour les Importants*
- **Entrées du Registre des risques** — pour les fournisseurs traitant des données confidentielles ou personnelles ; *révisées trimestriellement*
- **Enregistrements de notification d'incidents** des fournisseurs — *suivis dans le système de gestion des incidents*
- **Accords de traitement des données** avec des conditions conformes à la nLPD/RGPD — *révisés lors du renouvellement du contrat ou d'un changement réglementaire*
- **Évaluations des transferts transfrontaliers** — vérification d'adéquation, CCT ou certification DPF ; *documentées pour chaque fournisseur/service cloud transfrontalier*
- **Documentation sur la stratégie de sortie** pour les services cloud Critiques — *révisée annuellement ; tests de sortie effectués pour les principaux services Critiques*
- **Registres des sous-traitants ultérieurs** et enregistrements de notification des changements — *maintenus conformément aux termes des ATD*
- **Confirmations de destruction des données** à la résiliation du contrat — *certificats de destruction ou confirmation écrite conservés pendant 2 ans*
- **Documentation sur le modèle de responsabilité partagée** — pour chaque service cloud Critique ; *révisée annuellement*

---

# Conformité à la politique

## Mesure de la conformité

L'équipe de management de la sécurité de l'information vérifiera la conformité à cette politique par diverses méthodes, notamment, sans s'y limiter, les révisions du registre des fournisseurs, les audits de contrats, les vérifications de certifications, les audits internes et externes, ainsi que les retours d'information au propriétaire de la politique.

## Exceptions

Toute exception à cette politique doit être approuvée et enregistrée à l'avance par le Responsable de la sécurité de l'information, avec une acceptation du risque documentée et des mesures compensatoires. Les exceptions doivent être rapportées à l'Équipe de révision de la direction.

## Non-conformité

Un employé reconnu coupable d'avoir violé cette politique peut faire l'objet de mesures disciplinaires pouvant aller jusqu'au licenciement.

## Amélioration continue

Cette politique est révisée et mise à jour dans le cadre du processus d'amélioration continue. Les révisions doivent prendre en compte les évolutions du paysage des risques fournisseurs, les développements du marché des services cloud, les changements réglementaires (y compris la nLPD, le RGPD et les cadres émergents), les développements des menaces dans la chaîne d'approvisionnement et les leçons tirées des incidents fournisseurs.

---

# Domaines de la norme ISO 27001 couverts

Politique relative aux services cloud et à la sécurité des fournisseurs — Cartographie des contrôles ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership et engagement | 5.1 Politiques de sécurité de l'information |
| Clause 5.2 Politique | 5.4 Responsabilités de la direction |
| Clause 6.2 Objectifs de sécurité de l'information | 5.19 Sécurité de l'information dans les relations avec les fournisseurs |
| Clause 7.3 Sensibilisation | 5.20 Prise en compte de la sécurité de l'information dans les accords avec les fournisseurs |
| Clause 8.1 Planification et contrôle opérationnels | 5.21 Gestion de la sécurité de l'information dans la chaîne d'approvisionnement TIC |
| | 5.22 Surveillance, révision et gestion des changements des services fournisseurs |
| | **5.23 Sécurité de l'information dans l'utilisation des services cloud** |
| | 5.36 Conformité aux politiques, règles et normes |
| | 6.3 Sensibilisation, éducation et formation à la sécurité de l'information |
| | 6.4 Processus disciplinaire |
| | 8.30 Développement externalisé |

**Cadre réglementaire et légal** :

| Cadre | Pertinence |
|-------|-----------|
| nLPD suisse (revDSG) | Art. 9 — Accords de traitement et exigences relatives aux sous-traitants ultérieurs |
| OPDo suisse (Ordonnance sur la protection des données) | Annexe 1 — Liste des pays adéquats pour les transferts transfrontaliers |
| RGPD de l'UE (le cas échéant) | Art. 28 — Obligations des sous-traitants ; Art. 44–50 — Transferts internationaux |
| Cadre de confidentialité des données Suisse-États-Unis | Mécanisme d'adéquation pour les transferts vers les organisations américaines certifiées |
| ISO/IEC 27001:2022 | Contrôles Annexe A 5.19–5.23 |
| ISO/IEC 27002:2022 | Sections 5.19–5.23 — Lignes directrices de mise en œuvre |
| ISO/IEC 27017:2026 | Contrôles de sécurité cloud (informatif) |
| ISO/IEC 27018:2025 | Lignes directrices pour la protection des DCP dans le cloud (informatif) |

---

<!-- QA_VERIFIED: 2026-03-29 -->
