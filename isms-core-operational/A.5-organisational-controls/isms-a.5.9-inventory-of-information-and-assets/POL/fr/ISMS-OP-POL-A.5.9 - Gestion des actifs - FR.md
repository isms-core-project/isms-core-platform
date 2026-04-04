<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.5.9-FR:operational:OP-POL:a.5.9 -->
**ISMS-OP-POL-A.5.9 — Gestion des actifs**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Gestion des actifs |
| **Type de document** | Politique opérationnelle |
| **Identifiant du document** | ISMS-OP-POL-A.5.9 |
| **Créateur du document** | Responsable de la sécurité des systèmes d'information (RSSI) |
| **Propriétaire du document** | Directeur général (PDG) |
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

- ISO/IEC 27001:2022 Contrôle A.5.9 — Inventaire des informations et des actifs associés

**Contrôles Annexe A connexes** :

| Contrôle | Relation avec la gestion des actifs |
|----------|--------------------------------------|
| A.5.10 Utilisation acceptable des informations et actifs associés | Les règles d'utilisation acceptable font référence aux actifs inventoriés |
| A.5.11 Restitution des actifs | La restitution des actifs est suivie dans l'inventaire ; le registre est mis à jour lors de la restitution/suppression |
| A.5.12–13 Classification et étiquetage de l'information | La classification est assignée aux actifs informationnels dans le registre |
| A.5.14 Transfert de l'information | Les contrôles de transfert sont basés sur la classification des actifs |
| A.5.15–18 Contrôle d'accès et gestion des identités | Les droits d'accès sont approuvés par les propriétaires des actifs |
| A.7.10 Supports de stockage | Les supports amovibles sont enregistrés comme actifs |
| A.7.14 Mise hors service ou réutilisation sécurisée des équipements | La mise hors service met à jour le statut dans l'inventaire |
| A.8.1 Terminaux utilisateurs | Les terminaux sont enregistrés dans l'inventaire des actifs |
| A.8.8 Gestion des vulnérabilités techniques | La gestion des correctifs nécessite un inventaire complet des actifs |
| A.8.9 Gestion de la configuration | Les référentiels de configuration sont liés aux actifs informatiques inventoriés |

**Politiques internes connexes** :

- Politique de classification et de traitement de l'information
- Politique de contrôle d'accès
- Politique de sécurité des terminaux
- Politique d'utilisation acceptable
- Politique de protection de la vie privée et des DCP

---

# Politique de gestion des actifs

## Objet

L'objet de cette politique est l'identification, l'enregistrement et la gestion des actifs de l'organisation afin d'assurer une protection et une responsabilisation appropriées tout au long de leur cycle de vie.

Cette politique soutient la nFADP suisse (LPD révisée) et l'Ordonnance sur la protection des données (DSV) en mettant en œuvre des mesures techniques et organisationnelles appropriées au risque pour protéger les données personnelles, notamment en sachant quelles données existent, où elles sont stockées et qui en est responsable. Là où l'organisation traite des données de personnes résidant dans l'UE/EEE, les exigences du RGPD s'appliquent également.

## Périmètre

Tous les employés et utilisateurs tiers.

Toutes les informations, l'infrastructure informatique, les applications, les actifs physiques et les services cloud de l'organisation considérés comme dans le périmètre par la déclaration de périmètre ISO 27001.

## Principe

Les actifs de l'organisation sont connus, identifiés, classifiés et gérés avec une protection appropriée en place. On ne peut pas protéger ce qu'on ne sait pas posséder. L'inventaire des actifs est le fondement sur lequel reposent tous les autres contrôles de sécurité — évaluation des risques, contrôle d'accès, classification, gestion des vulnérabilités, réponse aux incidents et planification de la continuité des activités.

### Registre des actifs

L'organisation doit maintenir le registre des actifs dans un outil ou une plateforme centralisée (p. ex., système de gestion des actifs informatiques, CMDB ou tableur structuré avec contrôles d'accès). Le registre doit être accessible aux propriétaires d'actifs, à l'informatique et aux membres de l'équipe de gestion de la sécurité de l'information, et protégé contre toute modification non autorisée.

---

## Catégories d'actifs

Les catégories d'actifs suivantes doivent être inventoriées :

| Catégorie | Description | Exemples |
|-----------|-------------|----------|
| **Matériel** | Appareils physiques qui traitent, stockent ou transmettent des informations | Serveurs, postes de travail, ordinateurs portables, appareils mobiles, équipements réseau (routeurs, commutateurs, pare-feu), imprimantes |
| **Logiciels et licences** | Logiciels installés et services par abonnement | Systèmes d'exploitation, applications métier, outils de développement, logiciels de sécurité, abonnements SaaS |
| **Données et informations** | Informations numériques et physiques ayant de la valeur pour l'organisation | Bases de données, partages de fichiers, sauvegardes, archives, contrats, propriété intellectuelle, données de configuration |
| **Services cloud** | Services hébergés en externe traitant des données de l'organisation | IaaS (machines virtuelles, stockage), PaaS (bases de données, plateformes), SaaS (e-mail, CRM, collaboration) |
| **Actifs physiques** | Ressources tangibles soutenant la sécurité de l'information | Bureaux, salles de serveurs, coffres-forts, supports amovibles (clés USB, bandes de sauvegarde) |
| **Compétences du personnel** | Rôles clés et compétences spécialisées critiques pour les opérations | Rôles critiques (points de défaillance uniques), certifications spécialisées, connaissances institutionnelles |

**Compétences du personnel** : Le registre documente les **rôles et compétences**, et non les enregistrements de personnes individuelles. Exemple : « Compétence en administration de bases de données (2 personnes qualifiées) » — pas les noms individuels. Lorsqu'une fonction critique dépend d'un seul individu (point de défaillance unique), cela doit être signalé et un plan de succession ou de transfert des connaissances documenté pour atténuer le risque.

---

## Inventaire du matériel et de l'infrastructure informatique

Tous les actifs matériels et d'infrastructure informatique doivent être enregistrés dans l'inventaire des actifs. Pour chaque actif, les attributs suivants doivent être enregistrés :

**Attributs obligatoires** :

| Attribut | Description |
|----------|-------------|
| **Identifiant de l'actif** | Identifiant unique (p. ex., HW-0042) |
| **Nom de l'actif** | Nom lisible par un humain |
| **Type d'actif** | Catégorie (serveur, ordinateur portable, équipement réseau, mobile, etc.) |
| **Description** | Objectif et fonction |
| **Propriétaire** | Personne responsable de l'actif (nom et rôle) |
| **Département** | Unité organisationnelle |
| **Numéro de série / Étiquette d'actif** | Identifiant physique |
| **Emplacement** | Emplacement physique (bureau, rack, site) |
| **Classification** | Conformément à la Politique de classification et de traitement de l'information |
| **Statut** | Actif / En stockage / Mis hors service / Éliminé |
| **Dernière révision** | Date de la dernière vérification de l'enregistrement |

**Attributs supplémentaires recommandés** :

- Criticité (Élevée / Moyenne / Faible) — basée sur : **Élevée** = la perte entraînerait une perturbation significative des activités, une violation réglementaire ou une perte de données ; **Moyenne** = la perte aurait un impact modéré, une solution de contournement est disponible ; **Faible** = la perte a un impact minimal, facilement remplaçable
- Adresse IP ou nom d'hôte (pour les actifs connectés au réseau)
- Fabricant, modèle et version du micrologiciel/système d'exploitation
- Date d'acquisition et expiration de la garantie
- Statut de chiffrement

---

## Inventaire des actifs logiciels et de licences

Les logiciels et les licences de logiciels doivent être enregistrés dans l'inventaire des actifs. Pour chaque actif logiciel, les attributs suivants doivent être enregistrés :

| Attribut | Description |
|----------|-------------|
| **Nom du logiciel** | Nom du produit et éditeur |
| **Version** | Version actuelle déployée |
| **Propriétaire** | Personne responsable |
| **Type de licence** | Perpétuelle, abonnement, open source, gratuiciel |
| **Nombre de licences** | Nombre de licences achetées vs. déployées |
| **Date de renouvellement** | Expiration de l'abonnement ou prochain renouvellement |
| **Emplacement de déploiement** | Où le logiciel est installé ou hébergé |
| **Usage métier** | Pourquoi le logiciel est utilisé |
| **Statut du support** | Supporté par le fournisseur / Fin de vie (EOL) / Fin de support (EOS) |

Seuls les logiciels approuvés et sous licence par l'organisation doivent être déployés. Les logiciels non autorisés découverts lors des révisions de l'inventaire doivent être signalés à l'équipe de gestion de la sécurité de l'information pour évaluation et suppression.

Les logiciels ayant atteint leur fin de vie ou leur fin de support doivent être signalés et priorisés pour mise à niveau ou remplacement. Lorsque les logiciels non supportés ne peuvent pas être immédiatement remplacés, le risque doit être documenté dans le registre des risques avec des contrôles compensatoires.

---

## Inventaire des services cloud et SaaS

Les services cloud (IaaS, PaaS, SaaS) doivent être enregistrés dans l'inventaire des actifs aux côtés des logiciels traditionnels. Pour chaque service cloud, les attributs supplémentaires suivants doivent être enregistrés :

| Attribut | Description |
|----------|-------------|
| **Prestataire de services** | Nom du fournisseur |
| **Type de service** | IaaS / PaaS / SaaS |
| **Résidence des données** | Pays ou région où les données sont stockées |
| **Classification des données** | Classification des données traitées par le service |
| **Intégration SSO** | Si le service est intégré au fournisseur d'identité de l'organisation |
| **Propriétaire du contrat** | Personne responsable de la relation fournisseur |
| **Date de renouvellement** | Expiration du contrat ou de l'abonnement |

Les services cloud doivent être classifiés comme :

- **Sanctionnés** : Approuvés par l'informatique et la sécurité pour utilisation par l'organisation.
- **Tolérés** : Connus mais pas formellement approuvés ; en cours d'évaluation (maximum 90 jours avant d'être sanctionnés ou interdits).
- **Interdits** : Non autorisés ; doivent être supprimés.

Les nouveaux services cloud doivent être enregistrés dans l'inventaire des actifs **avant** que les données de l'organisation soient traitées dans le service (ou dans les 5 jours ouvrables pour les déploiements d'urgence avec approbation du RSSI).

Les services cloud non sanctionnés (informatique fantôme) doivent être identifiés lors de révisions périodiques des notes de frais, des journaux SSO et du trafic réseau. Les services nouvellement découverts doivent être évalués pour leur conformité à la sécurité et à la protection des données avant d'être sanctionnés.

---

## Inventaire des données et des actifs informationnels

Les données et actifs informationnels doivent être identifiés, et un inventaire élaboré et maintenu. Pour chaque actif de données, les attributs suivants doivent être enregistrés :

| Attribut | Description |
|----------|-------------|
| **Nom de l'actif** | Nom du jeu de données, de la base de données ou du magasin d'informations |
| **Propriétaire** | Personne responsable (la partie métier, pas le gardien technique) |
| **Classification** | Conformément à la Politique de classification et de traitement de l'information |
| **Emplacement de stockage** | Système ou service où les données résident |
| **Résidence des données** | Pays où les données sont physiquement stockées |
| **Durée de conservation** | Combien de temps les données sont conservées, selon les exigences de conservation |
| **Données personnelles** | Si le jeu de données contient des données personnelles (Oui / Non) |

Lorsque les actifs de données contiennent des données personnelles, le registre devrait capturer des champs supplémentaires pour soutenir la conformité à la nFADP suisse :

- Catégories de personnes concernées
- Finalité du traitement
- Catégories de destinataires
- Si des transferts transfrontaliers se produisent (et les garanties applicables)

Ces informations peuvent être enregistrées dans l'inventaire des actifs de données ou dans un **Registre des activités de traitement (RAT)** séparé conformément à l'art. 12 nFADP, avec un renvoi entre les deux registres.

---

## Propriété des actifs

Un propriétaire doit être assigné à chaque actif inventorié. La propriété ne doit jamais être laissée vide.

**Propriétaire** désigne la personne responsable de la sécurité de l'actif tout au long de son cycle de vie. Cela ne signifie pas les droits de propriété légaux. Le propriétaire peut déléguer la gestion quotidienne à un gardien (p. ex., l'informatique gère le serveur, mais le responsable de l'unité métier est propriétaire des données qui s'y trouvent), mais la responsabilité reste avec le propriétaire.

### Responsabilités du propriétaire

Les propriétaires d'actifs doivent :

- S'assurer que leurs actifs sont inventoriés et que les enregistrements sont exacts.
- Classifier les actifs selon leur valeur commerciale et leur risque.
- Réviser les enregistrements d'inventaire des actifs dont ils sont propriétaires au moins une fois par an.
- Approuver les demandes d'accès aux actifs dont ils sont propriétaires.
- Signaler les incidents de sécurité affectant les actifs dont ils sont propriétaires.
- Participer aux décisions du cycle de vie des actifs (mise hors service, archivage, élimination).

### Attribution de la propriété

- Les nouveaux actifs doivent avoir un propriétaire assigné au moment de l'enregistrement.
- Lorsque la propriété n'est pas claire, l'équipe de gestion de la sécurité de l'information doit escalader vers le responsable approprié pour détermination dans les **30 jours calendaires**.
- Les actifs sans propriétaire assigné après 30 jours doivent être escaladés au RSSI avec une justification documentée.
- Les changements de propriété (p. ex., départ d'un employé, changement de rôle) doivent être mis à jour dans le registre dans les **5 jours ouvrables**.

### Actifs orphelins

**Actifs non enregistrés découverts** : Les actifs trouvés en cours d'utilisation mais absents de l'inventaire doivent être immédiatement enregistrés avec un propriétaire temporaire (le responsable du découvreur ou l'informatique), investiqués dans les **14 jours ouvrables** pour déterminer le propriétaire métier et l'objectif, et soit formellement assignés à un propriétaire permanent, soit mis hors service.

**Départ du propriétaire** : Lorsqu'un propriétaire d'actif quitte l'organisation, la propriété doit être réassignée au responsable du collaborateur partant ou à son successeur désigné dans les **10 jours ouvrables** suivant son départ. Les actifs sans propriété réassignée après 30 jours doivent être escaladés au RSSI.

---

## Cycle de vie des actifs

### Enregistrement

Tous les actifs doivent être enregistrés dans l'inventaire des actifs dans les **5 jours ouvrables** suivant leur acquisition ou déploiement. Les actifs ne doivent pas être connectés au réseau ou utilisés pour traiter des données de l'organisation avant d'être enregistrés.

### Maintenance et changement

Tout changement de propriétaire, d'emplacement, de classification ou de statut d'un actif doit être reflété dans le registre dans les **5 jours ouvrables** suivant le changement.

### Mise hors service et élimination

Lors de la mise hors service ou de l'élimination d'un actif :

- Les données doivent être effacées ou détruites de manière sécurisée conformément à la Politique de classification et de traitement de l'information, en utilisant des méthodes conformes à **NIST SP 800-88** (Directives pour la désinfection des supports) : Effacement (réécriture logique) pour les données INTERNES, Purge (effacement cryptographique ou démagnétisation) pour les données CONFIDENTIELLES, ou Destruction (destruction physique) si requis.
- Les licences logicielles doivent être récupérées ou désactivées.
- Le registre des actifs doit être mis à jour pour refléter l'élimination, y compris la date et la méthode d'élimination.
- Pour les actifs ayant stocké des données confidentielles ou personnelles, des preuves de désinfection des données doivent être conservées (p. ex., certificat de destruction, journal de confirmation d'effacement).

### AVEC (Apportez votre équipement personnel de communication)

Lorsque l'AVEC est autorisé, les appareils personnels utilisés pour accéder aux données de l'organisation doivent être enregistrés dans l'inventaire des actifs avec un indicateur de propriété personnelle. Attributs minimaux d'enregistrement AVEC :

- Type d'appareil et système d'exploitation
- Nom de l'employé
- Périmètre d'utilisation professionnelle (e-mail uniquement, accès complet, etc.)
- Statut d'inscription MDM
- Accord AVEC signé (date)

À la fin de l'emploi ou du contrat, les données de l'organisation doivent être effacées de l'appareil personnel, et l'enregistrement AVEC doit être mis à jour.

---

## Utilisation acceptable des actifs

L'utilisation acceptable des actifs doit être conforme à la Politique d'utilisation acceptable.

Les utilisateurs ne doivent pas installer de logiciels non autorisés, connecter des appareils non approuvés au réseau, ou utiliser les actifs de l'organisation à des fins dépassant le périmètre de leur rôle.

---

## Restitution des actifs

Tous les employés et utilisateurs tiers doivent restituer tous les actifs de l'organisation en leur possession lors de la cessation de leur emploi, contrat ou accord.

Lorsqu'un employé ou un utilisateur tiers a utilisé son propre équipement personnel (AVEC), des procédures doivent garantir que toutes les informations de l'organisation sont transférées à l'organisation et effacées de manière sécurisée de l'appareil personnel.

Pendant les préavis, l'organisation doit prendre des mesures raisonnables pour empêcher la copie non autorisée d'informations de l'organisation par des employés ou des utilisateurs tiers sur le départ.

Le registre des actifs doit être mis à jour pour refléter tous les actifs restitués, réassignés ou éliminés.

---

## Révision des actifs

L'inventaire des actifs doit être révisé aux intervalles suivants :

| Type de révision | Fréquence | Responsable |
|-----------------|-----------|-------------|
| **Mises à jour pilotées par les événements** | Continue (dans les 5 jours ouvrables suivant le changement) | Propriétaires d'actifs et informatique |
| **Attestation des propriétaires** | Annuelle | Chaque propriétaire d'actif confirme l'exactitude de ses actifs assignés |
| **Audit complet de l'inventaire** | Annuel (aligné sur la révision de direction) | Équipe de gestion de la sécurité de l'information |
| **Révision de la découverte cloud/SaaS** | Trimestrielle | Informatique et équipe de gestion de la sécurité de l'information |
| **Conformité des licences logicielles** | Semestrielle | Informatique |

Les responsables de département doivent confirmer que leurs listes d'actifs sont à jour lors de la révision annuelle. Les écarts doivent être investiqués et résolus dans les 30 jours.

---

## Preuves

Les preuves suivantes démontrent la conformité à cette politique :

- **Registre d'inventaire des actifs** (matériel, logiciels, données, services cloud — avec attributs obligatoires renseignés) — *maintenu dans un outil centralisé ; exporté comme preuve d'audit*
- **Enregistrements d'attribution des propriétaires d'actifs** — *cible : 100 % des actifs avec propriétaires assignés ; mesuré trimestriellement*
- **Enregistrements d'attestation des propriétaires** (confirmations de révision annuelle) — *signés par chaque propriétaire d'actif ; conservés 3 ans*
- **Registre des services cloud/SaaS** avec résidence des données et classification — *mis à jour par événement ; révisé trimestriellement*
- **Enregistrements de conformité des licences logicielles** (licences achetées vs. déployées) — *audités semestriellement*
- **Enregistrements d'élimination des actifs** (date, méthode, preuves de désinfection NIST SP 800-88, certificats de destruction) — *conservés 5 ans*
- **Enregistrements d'inscription AVEC et signatures des accords** (le cas échéant) — *mis à jour par événement ; révisés annuellement*
- **Rapport annuel d'audit de l'inventaire** avec résultats et actions correctives — *présenté lors de la révision de direction*
- **Indicateur d'exhaustivité de l'inventaire** — *cible : ≥ 95 % des actifs connus enregistrés avec des attributs obligatoires complets ; mesuré annuellement*
- **Rapports de découverte de l'informatique fantôme** — *révisions trimestrielles documentées avec résultats d'évaluation*

---

# Conformité à la politique

## Mesure de la conformité

L'équipe de gestion de la sécurité de l'information vérifiera la conformité à cette politique par diverses méthodes, notamment les audits du registre des actifs, les révisions des attestations des propriétaires, les contrôles de conformité des licences, les audits internes et externes, et les retours d'information au propriétaire de la politique.

## Exceptions

Toute exception à cette politique doit être approuvée et consignée par le Responsable de la sécurité de l'information à l'avance, avec une acceptation documentée des risques, des contrôles compensatoires et une date de révision définie. Les exceptions doivent être rapportées à l'équipe de Révision de direction.

## Non-conformité

Un employé reconnu coupable d'avoir enfreint cette politique peut faire l'objet de mesures disciplinaires, pouvant aller jusqu'au licenciement.

## Amélioration continue

Cette politique est révisée et mise à jour dans le cadre du processus d'amélioration continue. Les révisions doivent prendre en compte les changements des normes de gestion des actifs, les changements organisationnels (acquisitions, restructurations), l'adoption de services cloud, les changements réglementaires et les enseignements tirés des incidents et des audits.

---

# Périmètre de la norme ISO 27001 couvert

Politique de gestion des actifs — Cartographie des contrôles ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership et engagement | 5.1 Politiques de sécurité de l'information |
| Clause 5.2 Politique | 5.4 Responsabilités de la direction |
| Clause 6.2 Objectifs de sécurité de l'information | 5.36 Conformité aux politiques, règles et normes |
| Clause 7.3 Sensibilisation | **5.9 Inventaire des informations et des actifs associés** |
| | 5.10 Utilisation acceptable des informations et des actifs associés |
| | 5.11 Restitution des actifs |
| | 6.3 Sensibilisation, formation et éducation à la sécurité de l'information |
| | 6.4 Processus disciplinaire |

**Cadre réglementaire et juridique** :

| Cadre | Pertinence |
|-------|-----------|
| nFADP suisse (LPD révisée) | Art. 8 — Mesures techniques et organisationnelles (nécessite de savoir quelles données existent et où) ; art. 12 — Registre des activités de traitement |
| DSV suisse (Ordonnance sur la protection des données) | Art. 1-3 — Exigences minimales pour la sécurité des données |
| RGPD UE (le cas échéant) | Art. 5 — Principe de responsabilité ; art. 30 — Registre des activités de traitement ; art. 32 — Sécurité du traitement |
| ISO/IEC 27001:2022 | Contrôle Annexe A 5.9 — Inventaire des informations et des actifs associés |
| ISO/IEC 27002:2022 | Section 5.9 — Conseils d'implémentation |
| NIST SP 800-53 Rév. 5 | CM-8 (Inventaire des composants du système), PM-5 (Inventaire des systèmes) |
| CIS Controls v8 | Contrôle 1 (Inventaire et contrôle des actifs de l'entreprise), Contrôle 2 (Inventaire et contrôle des actifs logiciels) |

---

<!-- QA_VERIFIED: 2026-03-29 -->
