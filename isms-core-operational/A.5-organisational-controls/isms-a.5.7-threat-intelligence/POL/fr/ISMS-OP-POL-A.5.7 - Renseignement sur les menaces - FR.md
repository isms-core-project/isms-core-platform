<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.5.7-FR:operational:OP-POL:a.5.7 -->
**ISMS-OP-POL-A.5.7 — Renseignement sur les menaces**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Renseignement sur les menaces |
| **Type de document** | Politique opérationnelle |
| **Identifiant du document** | ISMS-OP-POL-A.5.7 |
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

- ISO/IEC 27001:2022 Contrôle A.5.7 — Renseignement sur les menaces
- ISO/IEC 27002:2022 Section 5.7 — Conseils d'implémentation
- NIST SP 800-150 — Guide to Cyber Threat Information Sharing
- NIST SP 800-53 Rév. 5 PM-16 — Programme de sensibilisation aux menaces
- NIST SP 800-53 Rév. 5 RA-3 — Évaluation des risques
- NIST SP 800-53 Rév. 5 SI-5 — Alertes, avis et directives de sécurité
- FIRST TLP v2.0 — Protocole des feux de signalisation pour le partage d'informations
- OASIS STIX v2.1 / TAXII v2.1 — Normes d'échange de renseignements sur les menaces

**Contrôles Annexe A connexes** :

| Contrôle | Relation avec le renseignement sur les menaces |
|----------|------------------------------------------------|
| A.5.1 Politiques de sécurité de l'information | Cadre de politique général régissant les exigences en matière de renseignement sur les menaces |
| A.5.24-28 Gestion des incidents | Le renseignement sur les menaces améliore la détection, l'investigation et la réponse |
| A.5.30 Préparation des TIC pour la continuité des activités | Le renseignement sur les menaces informe la planification de la continuité et la préparation aux menaces |
| A.8.7 Protection contre les logiciels malveillants | Le renseignement sur les menaces fournit des IoC pour la détection des logiciels malveillants |
| A.8.8 Gestion des vulnérabilités techniques | Le renseignement sur l'exploitation priorise la remédiation des vulnérabilités |
| A.8.15 Journalisation | Les journaux fournissent la télémétrie interne pour l'analyse du renseignement sur les menaces |
| A.8.16 Activités de surveillance | Le renseignement sur les menaces fournit le contexte de détection et les règles de corrélation |
| A.8.23 Filtrage web | Le renseignement sur les menaces fournit des flux de domaines et d'URL malveillants |

**Politiques internes connexes** :

- Politique de gestion des incidents
- Politique de gestion des risques
- Politique de gestion des vulnérabilités
- Politique de journalisation
- Politique des activités de surveillance (A.8.16)
- Politique de protection contre les logiciels malveillants
- Politique de classification et de traitement de l'information

---

# Politique de renseignement sur les menaces

## Objet

L'objet de cette politique est d'établir les exigences relatives à la collecte, à l'analyse et à l'utilisation des informations sur les menaces de sécurité de l'information actuelles et émergentes, afin d'assurer une défense proactive, d'informer les décisions de gestion des risques et d'améliorer la capacité de l'organisation à détecter, prévenir et répondre aux incidents de sécurité.

Le renseignement sur les menaces transforme les données brutes sur les menaces en connaissances exploitables. Sans renseignement structuré, l'organisation opère de manière réactive — en répondant aux incidents après que les dommages sont survenus plutôt qu'en les anticipant et en les prévenant. Cette politique garantit que l'organisation maintient une connaissance situationnelle appropriée du paysage des menaces pertinent pour ses activités, ses actifs et son secteur.

Cette politique soutient la nFADP suisse (LPD révisée) en mettant en œuvre des mesures techniques et organisationnelles appropriées au risque pour protéger l'intégrité du traitement des données personnelles. Le renseignement sur les menaces contribue aux mesures de sécurité des données requises en vertu de l'art. 8 nFADP en permettant l'identification proactive des menaces pesant sur les systèmes traitant des données personnelles. Là où l'organisation traite des données de personnes résidant dans l'UE/EEE, les exigences de l'art. 32 du RGPD en matière de mesures de sécurité, y compris la surveillance des menaces, s'appliquent également.

## Périmètre

Toutes les activités liées à la collecte, à l'analyse, à la production, à la diffusion et à l'utilisation du renseignement sur les menaces au sein de l'organisation.

Cela comprend :

- La collecte d'informations sur les menaces provenant de sources externes et internes.
- L'analyse et la production de renseignements aux niveaux stratégique, tactique et opérationnel.
- La diffusion des renseignements aux parties prenantes appropriées.
- L'intégration du renseignement sur les menaces dans les processus d'évaluation des risques.
- L'intégration du renseignement sur les menaces dans la gestion des incidents et la surveillance de la sécurité.
- Le partage externe de renseignements sur les menaces avec des partenaires et des communautés de confiance.

**Hors périmètre** : Les opérations cyber offensives ou les représailles (interdites) ; les enquêtes des autorités compétentes (coopération soutenue, non conduite) ; les opérations d'analyse des vulnérabilités et de tests d'intrusion (couvertes par A.8.8) ; les procédures de recherche proactive des menaces (couvertes par A.8.16) ; les opérations de renseignement sans rapport avec la sécurité de l'information.

## Principe

Les informations relatives aux menaces de sécurité de l'information devraient être collectées et analysées pour produire du renseignement sur les menaces. Ce renseignement devrait être pertinent pour le paysage des menaces propre à l'organisation, techniquement précis, contextualisé par rapport aux actifs organisationnels et au profil de risque, et exploitable — fournissant des orientations claires permettant à l'organisation de détecter, prévenir ou répondre aux menaces identifiées.

L'organisation doit maintenir des capacités de renseignement sur les menaces proportionnées à sa taille, à son exposition aux risques et à son secteur. Toutes les organisations n'ont pas besoin d'un Centre des opérations de sécurité (SOC) dédié ou d'analystes de renseignement sur les menaces à plein temps. Ce que toute organisation nécessite, c'est un processus structuré et documenté pour se tenir informée des menaces pertinentes pour ses activités et agir sur cette information.

---

## Définitions

| Terme | Définition |
|-------|-----------|
| **Renseignement sur les menaces** | Informations sur les menaces actuelles ou émergentes qui ont été collectées, traitées et analysées pour permettre des décisions de sécurité éclairées et une défense proactive |
| **Renseignement stratégique** | Renseignement de haut niveau traitant des grandes tendances des menaces, des motivations des acteurs de la menace et des risques sectoriels, soutenant les décisions des dirigeants et la stratégie de sécurité à long terme |
| **Renseignement tactique** | Renseignement décrivant les tactiques, techniques et procédures (TTP) des adversaires, soutenant la planification des opérations de sécurité et la configuration des défenses |
| **Renseignement opérationnel** | Renseignement technique exploitable incluant les indicateurs de compromission (IoC) et les signatures de détection, soutenant les opérations immédiates de détection et de réponse |
| **Indicateur de compromission (IoC)** | Un artefact observable — tel qu'une adresse IP, un nom de domaine, un hachage de fichier ou une adresse e-mail — indiquant qu'une violation de sécurité s'est produite ou est en cours |
| **Tactiques, techniques et procédures (TTP)** | Schémas de comportement et méthodes utilisés par les acteurs de la menace pour mener des attaques, documentés dans des référentiels tels que MITRE ATT&CK |
| **Protocole des feux de signalisation (TLP)** | Un système de classification du partage d'informations utilisant des codes couleur (TLP:RED, TLP:AMBER+STRICT, TLP:AMBER, TLP:GREEN, TLP:CLEAR) pour indiquer les limites de partage autorisées |
| **STIX (Structured Threat Information eXpression)** | Un langage standard OASIS et un format de sérialisation pour l'échange de renseignements sur les cybermenaces de manière structurée et lisible par machine |
| **TAXII (Trusted Automated eXchange of Intelligence Information)** | Un protocole d'application standard OASIS pour l'échange automatisé de renseignements sur les cybermenaces via HTTPS |
| **MITRE ATT&CK** | Une base de connaissances mondialement accessible des tactiques et techniques adversariales basée sur des observations du monde réel, maintenue par la MITRE Corporation |
| **Acteur de la menace** | Un individu, un groupe ou une organisation menant des activités cybernétiques malveillantes avec une intention et une capacité identifiables |
| **OSINT (Renseignement de source ouverte)** | Renseignement sur les menaces dérivé de sources accessibles au public, notamment les blogs de sécurité, les bases de données de vulnérabilités, les réseaux sociaux et les avis publics |

---

## Types et couches de renseignement

L'organisation doit produire ou consommer du renseignement sur les menaces à trois niveaux, chacun servant un public et un objectif distincts. Toutes les organisations ne produiront pas de renseignements à chaque niveau en interne ; la consommation à partir de sources externes est acceptable lorsque la capacité de production interne est limitée.

### Renseignement stratégique

**Public** : Direction générale, RSSI, Gestion des risques.
**Objectif** : Informer les décisions commerciales, les investissements en sécurité et la stratégie à long terme.

Le renseignement stratégique devrait traiter :

- Le paysage global des menaces pertinent pour le secteur et la zone géographique de l'organisation.
- Les motivations et capacités des acteurs de la menace ciblant le secteur de l'organisation.
- Les tendances émergentes des menaces et leur impact commercial potentiel.
- Les évolutions réglementaires et géopolitiques affectant l'environnement des menaces.
- Les incidents des organisations homologues et les campagnes d'attaques à l'échelle du secteur.

**Fréquence de production** : Trimestrielle au minimum, ou déclenchée par des changements significatifs du paysage des menaces. Si l'organisation ne produit pas de renseignement stratégique en interne, elle devrait s'abonner à au moins une source de rapports stratégiques sur les menaces pertinents pour son secteur (p. ex., rapports semestriels du NCSC suisse, avis CERT ou services de renseignement stratégique commerciaux).

### Renseignement tactique

**Public** : Personnel des opérations de sécurité, administrateurs informatiques, intervenants en cas d'incident.
**Objectif** : Informer les configurations défensives, les règles de détection et l'architecture de sécurité.

Le renseignement tactique devrait traiter :

- Les profils des acteurs de la menace et les TTP pertinents pour la pile technologique de l'organisation.
- Les schémas d'attaque et l'analyse des campagnes ciblant le secteur de l'organisation.
- Les familles de logiciels malveillants et leurs caractéristiques comportementales.
- Les techniques d'ingénierie sociale et les schémas de campagnes d'hameçonnage.
- Les mesures défensives recommandées et les stratégies de détection.

**Fréquence de production** : Mensuelle au minimum, ou déclenchée par des menaces émergentes. Si la capacité d'analyse interne est limitée, l'organisation devrait consommer du renseignement tactique provenant d'au moins une source structurée (p. ex., MITRE ATT&CK, avis du NCSC suisse, flux CERT ou rapports commerciaux sur les menaces).

### Renseignement opérationnel

**Public** : Personnel technique de sécurité, administrateurs de systèmes, analystes SOC.
**Objectif** : Permettre la détection et le blocage immédiats des menaces connues.

Le renseignement opérationnel devrait inclure :

- Les indicateurs de compromission (IoC) : adresses IP malveillantes, domaines, URL, hachages de fichiers, adresses e-mail.
- Les signatures de logiciels malveillants et les indicateurs comportementaux.
- Les règles de détection et les règles YARA.
- Les listes de blocage pour les pare-feu, les passerelles e-mail et les filtres web.

**Fréquence de production** : En continu via des flux automatisés, avec révision périodique par les analystes (quotidienne si un SOC est opérationnel ; hebdomadaire au minimum pour les organisations sans SOC dédié).

---

## Catégories de sources

L'organisation doit maintenir des sources de renseignement sur les menaces dans plusieurs catégories afin d'éviter la dépendance à une source unique et d'assurer une couverture complète. Le nombre et la profondeur des sources doivent être proportionnés à la taille de l'organisation et à son exposition aux risques.

### Catégories de sources obligatoires

| Catégorie | Description | Exemples | Exigence minimale |
|-----------|-------------|----------|-------------------|
| **Gouvernement / CERT** | Avis et alertes CERT nationaux et sectoriels | NCSC suisse (ncsc.admin.ch), GovCERT.ch, CERT-EU, US-CERT/CISA | Au moins un abonnement à un CERT national |
| **Renseignement de source ouverte (OSINT)** | Données sur les menaces accessibles au public, bases de données de vulnérabilités, recherche en sécurité | CVE/NVD, AlienVault OTX, Abuse.ch, VirusTotal, blogs de chercheurs en sécurité | Au moins deux flux OSINT |
| **Télémétrie interne** | Événements de sécurité et résultats des propres systèmes de l'organisation | Alertes [SIEM], journaux de pare-feu, rapports de passerelle e-mail, alertes de détection des terminaux, post-mortems d'incidents | Toutes les sorties des outils de sécurité internes disponibles |

### Catégories de sources recommandées

| Catégorie | Description | Exemples | Quand mettre en œuvre |
|-----------|-------------|----------|----------------------|
| **Plateformes commerciales** | Renseignement sur les menaces organisé et validé avec qualité garantie par SLA | [Plateforme de renseignement sur les menaces], Recorded Future, Mandiant, CrowdStrike | Si le budget le permet et que l'exposition aux menaces justifie l'investissement |
| **Partage sectoriel (ISAC/ISAO)** | Renseignement sur les menaces spécifique au secteur partagé entre pairs | FS-ISAC (secteur financier), Health ISAC, groupes de partage sectoriels | Si un ISAC/ISAO pertinent existe pour le secteur de l'organisation |
| **Avis de sécurité des fournisseurs** | Informations sur les menaces et les vulnérabilités provenant des fournisseurs de technologie | Microsoft Security Response Centre, AWS Security Bulletins, flux spécifiques aux fournisseurs | Pour tous les fournisseurs de technologie critiques utilisés |

### Évaluation des sources

Toutes les sources de renseignement sur les menaces doivent être évaluées avant opérationnalisation et périodiquement par la suite. L'évaluation doit prendre en compte :

- **Fiabilité** : Le bilan de la source en matière de fourniture d'informations précises.
- **Actualité** : La rapidité avec laquelle les informations sont disponibles après l'émergence d'une menace.
- **Pertinence** : Si la source couvre les menaces applicables au secteur, à la zone géographique et à la pile technologique de l'organisation.
- **Exploitabilité** : Si les informations permettent des actions défensives concrètes.
- **Taux de faux positifs** : La proportion d'indicateurs qui s'avèrent inoffensifs lors de l'investigation.

Les sources qui fournissent systématiquement des informations inexactes, non pertinentes ou excessivement bruyantes doivent être remplacées ou dépriorisées. Les performances des sources doivent être examinées au moins une fois par an.

---

## Gestion des renseignements fournis par les fournisseurs

Lorsque l'organisation s'abonne à des services ou plateformes de renseignement sur les menaces commerciaux, les exigences de gestion des fournisseurs s'appliquent.

### Critères de sélection des fournisseurs

Les fournisseurs de renseignements sur les menaces commerciaux doivent être évalués selon les critères suivants :

| Critère | Méthode d'évaluation | Seuil d'acceptation |
|---------|---------------------|---------------------|
| **Qualité du renseignement** | Examen de 30 jours d'échantillon de données lors d'une période d'essai ; analyse du taux de faux positifs | Taux de faux positifs < 10 % ; pertinence > 90 % pour le secteur de l'organisation |
| **Actualité** | Délai entre l'émergence de la menace et la disponibilité dans le flux | < 24 heures pour les IoC critiques ; < 72 heures pour le renseignement tactique |
| **Transparence des sources** | Le fournisseur divulgue les méthodes de collecte de renseignements et les sources | Méthodologie documentée ; sources primaires identifiées |
| **Conformité à la protection des données** | Le traitement par le fournisseur des données personnelles dans les IoC respecte nFADP/RGPD | Accord de traitement des données en place ; base juridique documentée |
| **Intégration à la plateforme** | Compatibilité avec les outils de sécurité de l'organisation (SIEM, EDR, pare-feu) | Protocoles d'intégration standard pris en charge (STIX/TAXII, API, syslog) |
| **Stabilité du fournisseur** | Viabilité financière, base de clientèle, réputation dans le secteur | Fournisseur établi avec > 2 ans d'activité ; références disponibles |

### Suivi continu des performances des fournisseurs

| Indicateur | Cible | Fréquence de révision | Responsable |
|------------|-------|----------------------|-------------|
| **Disponibilité du flux** | > 99 % | Mensuelle | Opérations informatiques |
| **Taux de faux positifs** | < 10 % | Trimestrielle | RSSI |
| **Contribution aux vrais positifs** | > 5 détections validées par trimestre | Trimestrielle | RSSI |
| **Actualité vs. sources OSINT** | Le flux commercial fournit des renseignements ≥ 24 heures avant les sources gratuites | Trimestrielle | RSSI |
| **Réactivité du support** | Demandes de support résolues dans les délais SLA du fournisseur | Par incident | Opérations informatiques |
| **Conformité à la protection des données** | Aucun incident de traitement non autorisé de données personnelles | Continue | Conseiller en protection des données |

### Exigences contractuelles envers les fournisseurs

Les contrats avec les fournisseurs de renseignements sur les menaces commerciaux doivent inclure :

- **Accord de niveau de service (SLA)** précisant la disponibilité, la fraîcheur des flux et les délais de réponse du support
- **Accord de traitement des données (ATD)** traitant des données personnelles dans les IoC (obligations du sous-traitant selon l'art. 9 nFADP ou l'art. 28 RGPD)
- **Conditions de propriété intellectuelle** clarifiant l'utilisation autorisée des renseignements (sécurité interne uniquement ; aucune redistribution sans approbation)
- **Résiliation et portabilité des données** — capacité à exporter les données de renseignements dans un format standard à la résiliation du contrat
- **Notification d'incident** — obligation du fournisseur de notifier l'organisation de tout incident de sécurité affectant le service de renseignements dans les 24 heures

### Révision annuelle des fournisseurs

Les fournisseurs de renseignements commerciaux doivent faire l'objet d'une révision annuelle couvrant :
- Les performances par rapport aux SLA et aux indicateurs de qualité
- L'analyse coût-bénéfice (valeur fournie par rapport au coût de l'abonnement)
- La comparaison avec des fournisseurs alternatifs ou des sources OSINT
- La recommandation de renouvellement du contrat avec justification documentée

**La documentation de révision est conservée 3 ans ; les décisions de renouvellement sont documentées dans le registre des risques fournisseurs.**

---

## Collecte et analyse

### Processus de collecte

L'organisation doit mettre en œuvre un processus documenté de collecte des renseignements sur les menaces qui comprend :

1. **Collecte automatisée** : Les flux de menaces doivent être ingérés automatiquement lorsque cela est faisable, en utilisant des protocoles standard (STIX/TAXII si pris en charge) ou des API spécifiques aux fournisseurs. Les flux automatisés doivent être dirigés vers [SIEM] ou [Plateforme de renseignement sur les menaces] pour un traitement centralisé.

2. **Collecte manuelle** : Le personnel de sécurité doit examiner les sources d'avis, les actualités en matière de sécurité et les forums communautaires selon un calendrier défini. Les résultats de la collecte manuelle doivent être documentés et enregistrés dans le registre de renseignements sur les menaces.

3. **Collecte interne** : Les événements de sécurité, les résultats des investigations d'incidents et les résultats d'analyses forensiques doivent être capturés en tant que renseignements sur les menaces internes. Les bilans post-incidents doivent identifier et enregistrer explicitement les IoC et TTP rencontrés.

4. **Protection des données** : Tous les renseignements collectés doivent respecter les exigences applicables en matière de protection des données. Les données personnelles incluses dans les renseignements sur les menaces (p. ex., adresses e-mail dans les indicateurs d'hameçonnage) ne doivent être traitées qu'au titre de l'intérêt légitime de la sécurité de l'information et conservées uniquement aussi longtemps que l'indicateur reste opérationnellement pertinent.

### Processus d'analyse

Les données brutes sur les menaces doivent être analysées avant diffusion pour garantir la qualité et la pertinence. L'analyse doit :

- **Valider** les informations via plusieurs sources dans la mesure du possible.
- **Contextualiser** les menaces par rapport aux actifs spécifiques, à la pile technologique et au profil de risque de l'organisation.
- **Évaluer** la probabilité et l'impact potentiel des menaces identifiées pour l'organisation.
- **Prioriser** les menaces en fonction de leur pertinence, de leur gravité et de l'exposition de l'organisation.
- **Produire** des recommandations exploitables ou des conseils de détection.

Si l'organisation ne dispose pas d'analystes de renseignement sur les menaces dédiés, les responsabilités d'analyse doivent être assignées au RSSI ou au personnel de sécurité désigné. L'analyse n'a pas besoin d'être une fonction à plein temps pour les petites organisations, mais elle doit être une activité documentée et récurrente avec une responsabilité clairement définie.

### Exigences de qualité

Tous les renseignements sur les menaces — qu'ils soient produits en interne ou consommés à partir de sources externes — doivent satisfaire aux critères de qualité suivants avant d'être mis en œuvre :

- **Pertinents** : Applicables au paysage des menaces, au secteur et à l'environnement technologique de l'organisation.
- **Précis** : Validés par corroboration ou évaluation de la fiabilité de la source.
- **Actuels** : À jour et fournis dans un délai permettant une action efficace.
- **Exploitables** : Accompagnés d'orientations claires sur les actions de détection, de prévention ou de réponse.

Les renseignements ne satisfaisant pas à ces critères doivent être signalés, investiqués ou écartés. Les enregistrements d'évaluation des sources doivent documenter les problèmes de qualité.

---

## Gestion du cycle de vie des données de renseignements

### Exigences de conservation

Les données de renseignements sur les menaces doivent être conservées conformément aux exigences opérationnelles et réglementaires :

| Type de renseignement | Durée de conservation | Justification |
|-----------------------|-----------------------|---------------|
| **IoC opérationnels** (en détection active) | Aussi longtemps que la menace reste pertinente ; minimum 90 jours | La détection active nécessite des indicateurs actuels |
| **IoC historiques** (plus actifs) | 12 mois après désactivation | Contexte historique pour les investigations d'incidents ; analyse des tendances |
| **Rapports de renseignement stratégique et tactique** | 3 ans | Piste d'audit de l'évaluation des risques ; évaluation de la maturité du programme ; contexte historique |
| **Renseignements internes issus des incidents** | Selon le calendrier de conservation des incidents (généralement 5 ans) | Conformité réglementaire ; procédures judiciaires potentielles |
| **Enregistrements d'évaluation des sources** | 3 ans | Piste d'audit pour les décisions de sélection des sources |
| **Accords de partage de renseignements** | 7 ans après résiliation | Exigences légales de conservation des documents |

### Gestion du cycle de vie des IoC

Les indicateurs de compromission déployés dans les systèmes de détection doivent être gérés selon un processus de cycle de vie :

1. **Ingestion** — IoC reçu de la source, validé et classifié (TLP, type de menace, gravité)
2. **Déploiement** — IoC déployé dans les systèmes de détection pertinents (SIEM, EDR, pare-feu, filtre web)
3. **Surveillance active** — L'IoC génère des alertes lorsqu'une correspondance est trouvée ; alertes triées et investiguées
4. **Révision** — IoC révisés trimestriellement pour leur pertinence continue :
   - L'indicateur a-t-il été observé dans les alertes ? (Actif vs. dormant)
   - La menace est-elle toujours d'actualité ? (Source de renseignement mise à jour ou obsolète ?)
   - Le taux de faux positifs est-il acceptable ? (Si > 20 % de faux positifs, envisager la suppression)
5. **Désactivation** — IoC retiré des systèmes de détection lorsqu'il n'est plus pertinent
6. **Archivage** — IoC transféré dans la base de données historique pour l'analyse des tendances et la référence aux investigations d'incidents
7. **Suppression** — IoC définitivement effacé après l'expiration de la durée de conservation

**Automatisation** : Dans la mesure du possible sur le plan technique, la gestion du cycle de vie des IoC devrait être automatisée via la plateforme de renseignement sur les menaces (TIP) ou la fonctionnalité SIEM. La gestion manuelle des IoC est acceptable pour les organisations sans capacité TIP.

### Considérations relatives à la protection des données

Lorsque les renseignements sur les menaces contiennent des données personnelles (p. ex., adresses e-mail dans les indicateurs d'hameçonnage, adresses IP de systèmes compromis) :

- **Base juridique** : Traitement justifié au titre de l'intérêt légitime pour la sécurité de l'information (art. 6 al. 2 nFADP ; art. 6(1)(f) RGPD le cas échéant)
- **Limitation de la finalité** : Les données personnelles dans les IoC ne sont traitées qu'aux fins de la détection des menaces et de la réponse aux incidents ; non utilisées à d'autres fins
- **Minimisation de la conservation** : Les données personnelles ne sont conservées que le temps opérationnellement nécessaire ; les IoC contenant des données personnelles sont priorisés pour la révision du cycle de vie
- **Restriction d'accès** : Les bases de données de renseignements contenant des données personnelles sont limitées au seul personnel de sécurité autorisé

**AIPD** : Si le traitement des renseignements sur les menaces implique une surveillance systématique à grande échelle ou des catégories particulières de données personnelles, une analyse d'impact relative à la protection des données peut être requise en vertu de l'art. 22 nFADP.

---

## Diffusion et partage

### Diffusion interne

Les renseignements sur les menaces doivent être distribués au public approprié en fonction du type de renseignement :

| Type de renseignement | Destinataires | Format | Fréquence |
|-----------------------|---------------|--------|-----------|
| **Stratégique** | Direction générale, RSSI, Gestion des risques | Documents de synthèse, rapports trimestriels | Trimestrielle ou lors d'un changement significatif |
| **Tactique** | Opérations informatiques, équipe de sécurité, administrateurs de systèmes | Avis, résumés de TTP, recommandations défensives | Mensuelle ou lors d'une menace émergente |
| **Opérationnel** | [SIEM] / outils de sécurité, analystes SOC, administrateurs informatiques | Flux IoC, règles de détection, listes de blocage | En continu (automatisé) ou hebdomadaire (manuel) |

### Escalade pour les menaces critiques

Lorsque le renseignement sur les menaces identifie une menace imminente ou active ciblant l'organisation ou son secteur :

1. **Notification immédiate** au RSSI (dans l'heure suivant l'identification).
2. **Évaluation rapide** de l'exposition organisationnelle (dans les 4 heures).
3. **Briefing d'urgence** aux parties prenantes concernées avec les actions recommandées.
4. **Activation de la réponse aux incidents** si l'évaluation de la menace le justifie (conformément à la Politique de gestion des incidents).

### Partage externe

L'organisation peut partager des renseignements sur les menaces avec des tiers de confiance, sous réserve des contrôles suivants :

- **Classification TLP** : Tous les renseignements partagés doivent être classifiés en utilisant le Protocole des feux de signalisation v2.0 (TLP:RED, TLP:AMBER+STRICT, TLP:AMBER, TLP:GREEN, TLP:CLEAR). Le partage ne doit pas dépasser la désignation TLP assignée par l'émetteur.
- **Accords de partage** : Des accords formels (NDA, accord de partage d'informations ou conditions d'adhésion) doivent être en place avant le partage avec des tiers.
- **Protection des données** : Les renseignements partagés ne doivent pas inclure de données personnelles au-delà de ce qui est nécessaire pour la détection des menaces (p. ex., IoC). Lorsque des données personnelles sont partagées, une base juridique doit être établie en vertu de la nFADP.
- **Notification réglementaire** : Lorsque les obligations de déclaration obligatoire du NCSC suisse s'appliquent (exploitants d'infrastructures critiques — art. 74b LSI), l'organisation doit signaler les cyberincidents pertinents au NCSC dans les 24 heures conformément aux exigences applicables.

### Réception de renseignements externes

Lors de la réception de renseignements sur les menaces provenant de sources externes :

- **Respecter les marquages TLP** : Les renseignements reçus avec des désignations TLP ne doivent pas être partagés au-delà des limites autorisées.
- **Valider avant d'agir** : Les IoC reçus de l'extérieur doivent être validés par rapport à l'environnement de l'organisation avant leur déploiement dans des systèmes de blocage ou de détection, afin de minimiser les faux positifs.
- **Accuser réception** : Lorsque le partage est bidirectionnel, l'organisation doit accuser réception et fournir des retours sur l'utilité des renseignements lorsque cela est demandé.

---

## Intégration à l'évaluation des risques

Le renseignement sur les menaces doit informer le processus d'évaluation des risques de l'organisation conformément à la clause 6.1 de l'ISO 27001:2022. Cette intégration est obligatoire — les renseignements sur les menaces qui n'influencent pas les décisions de risque apportent une valeur limitée.

### Points d'intégration obligatoires

- **Évaluation de la vraisemblance** : Le renseignement sur les menaces concernant les campagnes actives, l'activité d'exploitation et le ciblage par les acteurs de la menace doit informer les estimations de vraisemblance assignées aux risques identifiés.
- **Évaluation de l'impact** : Le renseignement sur les techniques d'attaque et les conséquences observées dans les organisations homologues doit informer les évaluations d'impact.
- **Mises à jour du registre des risques** : Lorsque le renseignement sur les menaces identifie de nouvelles menaces ou des changements aux menaces existantes, le registre des risques doit être mis à jour en conséquence. Chaque mise à jour doit référencer la source de renseignement sur les menaces étayant la décision.
- **Efficacité des contrôles** : Le renseignement sur les menaces concernant les contrôles contournés ou inefficaces observés dans la pratique doit déclencher une réévaluation de l'efficacité des contrôles de l'organisation.

### Processus

1. Le RSSI ou le personnel de sécurité désigné doit examiner les résultats du renseignement stratégique et tactique au moins trimestriellement par rapport au registre des risques actuel.
2. Les nouvelles menaces identifiées par l'analyse des renseignements doivent être soumises à la Gestion des risques pour une évaluation formelle.
3. Les modifications de la vraisemblance ou de l'impact des menaces basées sur les renseignements doivent être documentées avec des références traçables aux rapports de renseignement étayant la décision.
4. Les décisions de traitement des risques influencées par les renseignements sur les menaces doivent être enregistrées dans le registre des risques.

### Évaluation des menaces pour la vie privée et la confidentialité

Lorsque l'organisation traite des données personnelles soumises à la nFADP ou au RGPD, le renseignement sur les menaces doit aborder spécifiquement les menaces pesant sur la confidentialité des données et la vie privée :

| Catégorie de menace | Impact sur la vie privée | Exigences en matière de renseignement |
|---------------------|--------------------------|--------------------------------------|
| **Exfiltration de données** | Divulgation non autorisée de données personnelles | IoC pour les logiciels malveillants de vol de données, techniques d'exfiltration (tunneling DNS, stéganographie), infrastructure des attaquants utilisée pour la mise en scène des données |
| **Vol de données d'identification** | Accès non autorisé aux systèmes traitant des données personnelles | Indicateurs de campagnes d'hameçonnage, signatures de logiciels malveillants voleurs d'identifiants, bases de données d'identifiants compromis |
| **Menaces internes** | Mauvaise utilisation intentionnelle ou accidentelle des données | Indicateurs comportementaux, schémas d'abus d'accès privilégié, détection des anomalies d'accès aux données |
| **Violations de tiers** | Compromission de données personnelles via des sous-traitants/fournisseurs | Renseignements sur les fournisseurs de services victimes de violations, plateformes SaaS compromises, fuite de données dans la chaîne d'approvisionnement |

**Impact sur le registre des risques :**
- Les risques liés au traitement des données personnelles (p. ex., « R-DATA-01 : Accès non autorisé aux données personnelles des clients ») doivent être examinés trimestriellement par rapport aux résultats du renseignement sur les menaces
- Le renseignement sur les menaces indiquant un ciblage accru des responsables du traitement dans le secteur de l'organisation doit déclencher une réévaluation de l'adéquation des contrôles de protection des données
- Les règles de détection des tentatives d'exfiltration de données doivent être mises à jour en fonction des techniques observées chez les attaquants

---

## Intégration à la gestion des incidents

Le renseignement sur les menaces doit améliorer la détection, l'investigation et la réponse aux incidents conformément aux contrôles A.5.24-28.

### Amélioration de la détection

- Les IoC provenant des sources de renseignements sur les menaces doivent être déployés dans les systèmes de détection ([SIEM], [EDR], passerelle e-mail, filtre web) pour permettre des alertes automatisées.
- Les TTP des acteurs de la menace issus du renseignement tactique doivent être traduits en règles de détection ou en cas d'usage de surveillance lorsque cela est faisable.
- L'efficacité des règles de détection doit être révisée périodiquement et les règles mises à jour en fonction de l'évolution des renseignements.

### Support à l'investigation

- Lorsqu'un incident de sécurité survient, les renseignements disponibles sur les menaces doivent être interrogés pour rechercher les indicateurs connexes, les profils d'acteurs de la menace connus et le contexte des schémas d'attaque.
- Le contexte du renseignement sur les menaces doit être inclus dans les enregistrements d'investigation des incidents pour soutenir l'analyse des causes profondes et l'évaluation de l'attribution.

### Retour d'information post-incident

- Les résultats des incidents — y compris les nouveaux IoC découverts, les TTP observés et l'infrastructure d'attaque — doivent être capturés comme renseignements sur les menaces internes.
- Les bilans post-incidents doivent évaluer si les sources de renseignement existantes ont fourni une avertissement adéquat et si les règles de détection ont fonctionné comme prévu.
- Les enseignements tirés doivent être réintégrés dans l'évaluation des sources, l'affinage des règles de détection et les mises à jour de l'évaluation des risques.

---

## Intégration à la surveillance de la sécurité

Le renseignement sur les menaces doit être intégré aux capacités de surveillance de la sécurité pour améliorer l'efficacité de la détection.

### Exigences d'intégration

- **Intégration [SIEM]** : Les IoC opérationnels doivent être intégrés dans le [SIEM] pour la corrélation avec les événements de sécurité internes. Lorsque l'ingestion automatisée n'est pas faisable, la saisie manuelle des IoC doit être effectuée selon un calendrier défini.
- **Détection sur les terminaux** : Lorsque [EDR] ou les plateformes de protection des terminaux prennent en charge l'intégration des flux de renseignements sur les menaces, les IoC pertinents doivent être déployés dans les systèmes de détection des terminaux.
- **Sécurité e-mail** : Les domaines d'hameçonnage connus, les adresses d'expéditeurs malveillants et les hachages de pièces jointes doivent être déployés dans les règles de filtrage de la passerelle e-mail.
- **Filtrage web** : Les domaines et URL malveillants issus des renseignements sur les menaces doivent être déployés dans les systèmes de filtrage web ou de sécurité DNS.
- **Règles de pare-feu** : Les adresses IP malveillantes connues et les indicateurs réseau doivent être déployés dans les listes de blocage des pare-feu périmètre et internes, sous réserve de validation des faux positifs.

### Efficacité de la surveillance

L'organisation doit suivre les indicateurs suivants pour évaluer l'efficacité de l'intégration :

- Nombre d'alertes générées par les indicateurs issus des renseignements sur les menaces.
- Taux de vrais positifs confirmés pour les alertes issues des renseignements sur les menaces.
- Délai entre la réception des renseignements et le déploiement des règles de détection.
- Lacunes de couverture entre les renseignements sur les menaces et les capacités de surveillance.

---

## Intégration à la disponibilité et à la continuité des activités

Le renseignement sur les menaces doit informer la planification de la continuité des activités et la protection de la disponibilité des services conformément aux contrôles A.5.29-30.

### Surveillance des menaces pesant sur la disponibilité

Les catégories de menaces suivantes doivent être priorisées pour la détection et la réponse en raison de leur impact potentiel sur la disponibilité des services :

| Type de menace | Impact sur la disponibilité | Priorité de détection | Action de réponse |
|----------------|-----------------------------|-----------------------|-------------------|
| **Attaque par déni de service distribué (DDoS)** | Interruption directe des services | Élevée | Activer le service d'atténuation DDoS ; filtrage du trafic ; coordination avec le FAI en amont |
| **Rançongiciel** | Indisponibilité des données et des systèmes | Critique | Confinement immédiat ; restauration des sauvegardes ; aucun paiement de rançon |
| **Logiciels malveillants destructeurs (wiper)** | Destruction permanente des données | Critique | Isolation immédiate ; préservation forensique ; activation de la reprise après sinistre |
| **Attaques de la chaîne d'approvisionnement** | Perturbation des dépendances tierces | Élevée | Évaluation des prestataires alternatifs ; procédures de dégradation de service |
| **Attaques par épuisement des ressources** | Dégradation des capacités | Moyenne | Mise à l'échelle des capacités ; limitation du débit ; blocage de l'acteur malveillant |

### Intrants pour la planification de la continuité

Le renseignement sur les menaces doit fournir les intrants suivants à la planification de la continuité des activités et à la reprise après sinistre :

1. **Scénarios de menaces** — L'examen annuel des scénarios de menaces plausibles (rançongiciel, DDoS, destruction de données) basé sur les incidents observés dans le secteur doit informer l'analyse d'impact sur les activités (AIA) et les stratégies de reprise.

2. **Validation des objectifs de temps de reprise (OTR)** — Les vitesses d'attaque observées dans la pratique (p. ex., temps de chiffrement par rançongiciel, durée des attaques DDoS) doivent être comparées aux hypothèses d'OTR pour valider la faisabilité de la reprise.

3. **Risques liés aux dépendances tierces** — Les renseignements sur les attaques de la chaîne d'approvisionnement ou les incidents affectant les fournisseurs de services cloud doivent déclencher des révisions des plans de contingence des fournisseurs et de la préparation aux prestataires alternatifs.

4. **Scénarios d'exercice sur table** — Les exercices annuels de continuité des activités doivent incorporer des scénarios de menaces réalistes dérivés des renseignements actuels sur les menaces.

**Processus d'intégration :**
- Révision trimestrielle des menaces pesant sur la disponibilité par le RSSI et le Responsable de la continuité des activités
- Mise à jour annuelle des hypothèses de menaces dans l'AIA basée sur les résultats du renseignement
- Mises à jour du plan de continuité des activités documentées avec référence aux renseignements sur les menaces étayant la décision

---

## Mesure de l'efficacité

L'organisation doit mesurer l'efficacité du programme de renseignement sur les menaces afin de justifier l'investissement, d'identifier les opportunités d'amélioration et de démontrer la valeur aux parties prenantes.

### Indicateurs

Les indicateurs suivants doivent être suivis et rapportés au RSSI trimestriellement :

| Indicateur | Cible | Seuil d'alerte |
|------------|-------|----------------|
| Sources de renseignement actives | Conformément aux exigences minimales ci-dessus | En dessous du minimum dans l'une des catégories obligatoires |
| Révisions d'évaluation des sources effectuées | 100 % annuellement | < 80 % des sources révisées |
| Mises à jour du registre des risques informées par les renseignements | Au minimum 1 par trimestre | 0 mise à jour au cours d'un trimestre |
| Déploiement des IoC dans les systèmes de détection | Dans les 24 heures suivant la réception validée | > 72 heures de délai moyen de déploiement |
| Alertes issues des renseignements (taux de vrais positifs) | > 70 % | < 50 % |
| Briefings de renseignement stratégique fournis à la Direction générale | Trimestriel au minimum | Manqué dans > 1 trimestre |
| Retours d'information post-incident complétés | 100 % des incidents P1/P2 | < 80 % des incidents P1/P2 |

### Révision annuelle du programme

Le RSSI doit conduire une révision annuelle du programme de renseignement sur les menaces couvrant :

- L'adéquation et les performances du portefeuille de sources.
- La qualité et l'actualité de la production de renseignements.
- L'efficacité de l'intégration avec l'évaluation des risques, la gestion des incidents et la surveillance.
- L'adéquation des ressources (personnel, outils, budget).
- L'évaluation de la maturité par rapport au niveau de maturité cible de l'organisation.
- Les recommandations d'amélioration du programme.

---

## Tests et validation

L'organisation doit tester l'efficacité du renseignement sur les menaces pour valider que les sources de renseignement et les intégrations de détection fonctionnent comme prévu.

### Tests de détection des renseignements

| Type de test | Fréquence | Méthode | Critères de succès | Responsable |
|--------------|-----------|---------|---------------------|-------------|
| **Validation de la détection des IoC** | Trimestrielle | Déploiement de tests d'IoC (simulation non malveillante) dans les outils de sécurité ; vérification de la génération des alertes | > 90 % des IoC déployés déclenchent les alertes attendues | Sécurité informatique |
| **Intégrité des flux de renseignements** | Mensuelle | Vérification que les flux automatisés s'ingèrent correctement ; contrôle des données obsolètes | Tous les flux mis à jour dans les 24 heures ; aucun échec d'ingestion de plus de 48 heures | Opérations informatiques |
| **Couverture de la détection des TTP** | Semestrielle | Cartographie des règles de détection de l'organisation sur MITRE ATT&CK ; identification des lacunes de couverture | > 70 % des techniques MITRE ATT&CK pertinentes pour le profil de menaces de l'organisation couvertes par des règles de détection | RSSI |
| **Analyse des faux positifs** | Trimestrielle | Échantillonnage de 20 alertes issues des renseignements ; investigation du taux de vrais positifs | > 70 % de taux de vrais positifs | Sécurité informatique |
| **Test du chemin d'escalade** | Annuelle | Simulation d'un scénario de menace critique ; test de l'escalade vers le RSSI et la Direction générale | Escalade effectuée dans l'heure ; toutes les parties prenantes mobilisées | RSSI |
| **Évaluation de l'utilité des sources** | Annuelle | Pour chaque source de renseignement, identification des renseignements exploitables produits au cours des 12 derniers mois | Chaque source a produit ≥ 1 élément de renseignement exploitable ou raison documentée de rétention | RSSI |

### Exercices en équipe violette

Si les ressources le permettent, l'organisation devrait conduire des exercices annuels en équipe violette :
- L'**équipe rouge** simule des attaques basées sur les renseignements actuels sur les menaces (TTP adversariales réalistes)
- L'**équipe bleue** (détection et réponse) tente de détecter et de répondre en utilisant des détections informées par les renseignements
- Le **débriefing** identifie les lacunes dans la couverture des renseignements, les règles de détection ou les procédures de réponse
- Les **actions d'amélioration** sont documentées et suivies via le processus d'actions correctives

**Pour les organisations sans capacité d'équipe violette :** Les exercices sur table simulant des scénarios d'incidents pilotés par les renseignements constituent une alternative acceptable.

### Documentation des tests

Toutes les activités de test doivent être documentées avec :
- Date, périmètre et participants au test
- Résultats du test (réussite/échec, indicateurs atteints, lacunes identifiées)
- Actions correctives assignées (le cas échéant lors de l'identification de lacunes)
- Validation de suivi des actions correctives

La documentation des tests est conservée 3 ans ; rapportée lors de la révision annuelle du programme.

---

## Partage de renseignements avec les clients (le cas échéant)

*Remarque : Cette section s'applique uniquement si l'organisation fournit des services de sécurité gérés ou a des engagements contractuels de partage de renseignements avec des clients.*

### Livrables de renseignements pour les clients

Lorsque l'organisation s'est contractuellement engagée à fournir des renseignements sur les menaces aux clients :

| Livrable | Fréquence | Contenu | Public |
|----------|-----------|---------|--------|
| **Briefing sur les menaces** | Trimestrielle | Résumé du renseignement stratégique pertinent pour le secteur du client ; menaces émergentes ; actions recommandées | Direction sécurité du client |
| **Flux IoC** | Continu ou quotidien | IoC opérationnels pertinents pour l'environnement du client | SOC ou sécurité informatique du client |
| **Notifications d'incident** | Immédiate | Notification des menaces ciblant activement le secteur ou la pile technologique du client | Contact sécurité du client |
| **Rapport annuel sur les menaces** | Annuelle | Analyse complète du paysage des menaces ; données sur les tendances d'attaques ; profils des acteurs de la menace spécifiques au secteur | Direction générale du client |

### Renseignements spécifiques aux clients

Pour les clients bénéficiant d'accords de service dédiés, l'organisation doit :
- Adapter les renseignements à la pile technologique, la zone géographique et le profil de menaces spécifiques du client
- Fournir des recommandations exploitables spécifiques à l'environnement du client
- Coordonner avec l'équipe de sécurité du client sur l'application des renseignements
- Maintenir la confidentialité des renseignements spécifiques au client (non partagés avec d'autres clients sans anonymisation)

### Boucle de retour d'information des clients

- Les clients doivent être invités à fournir des retours sur l'utilité et la pertinence des renseignements
- Les retours des clients sont incorporés dans la révision trimestrielle du programme de renseignement
- Les ajustements aux livrables sont effectués en fonction des besoins et des retours des clients

**Preuves** : Les livrables de renseignements pour les clients sont documentés avec confirmation de livraison ; les retours des clients sont enregistrés ; la conformité aux niveaux de service est suivie.

---

## Guide de mise en œuvre pour les PME

Toutes les organisations ne disposent pas d'équipes dédiées de renseignement sur les menaces ou de capacités SOC. Les orientations suivantes aident les petites organisations à mettre en œuvre un renseignement sur les menaces proportionné à leurs ressources :

### Programme minimum viable (organisations sans personnel de sécurité dédié)

- S'abonner aux alertes du NCSC suisse et à au moins un flux CERT pertinent.
- S'abonner à au moins deux flux OSINT gratuits (p. ex., Abuse.ch, AlienVault OTX).
- Désigner une personne (RSSI, responsable informatique ou contact sécurité désigné) responsable de l'examen hebdomadaire des avis.
- Examiner les rapports stratégiques sur le paysage des menaces du NCSC suisse semestriellement.
- S'assurer que les avis de sécurité des fournisseurs critiques sont suivis et traités.
- Documenter les résultats du renseignement dans un registre simple (un tableur est acceptable).
- Examiner le registre trimestriellement par rapport au registre des risques.

### Voie de progression (organisations avec une fonction de sécurité émergente)

- Ajouter des flux de renseignements commerciaux pertinents pour le secteur et la pile technologique.
- Mettre en œuvre l'ingestion automatisée des IoC dans les systèmes [SIEM] ou de pare-feu.
- Commencer à produire des renseignements tactiques internes à partir des post-mortems d'incidents.
- Rejoindre les communautés de partage d'informations pertinentes (ISAC/ISAO) lorsqu'elles existent.
- Établir un calendrier de diffusion formel et des briefings aux parties prenantes.
- Cartographier les menaces observées sur le cadre MITRE ATT&CK pour une analyse structurée.

### Programme mature (organisations avec des opérations de sécurité dédiées)

- Déployer une [Plateforme de renseignement sur les menaces] dédiée pour la collecte, l'analyse et la diffusion.
- Employer ou contracter des analystes de renseignement sur les menaces dédiés.
- Produire des renseignements aux trois niveaux (stratégique, tactique, opérationnel).
- Intégrer les renseignements à tous les outils de sécurité via des flux automatisés.
- Participer activement aux communautés de partage externes.
- Conduire des exercices de modélisation des menaces informés par les renseignements.

---

## Rôles et responsabilités

| Rôle | Responsabilités en matière de renseignement sur les menaces |
|------|-------------------------------------------------------------|
| **Direction générale** | Approuver la politique de renseignement sur les menaces ; allouer les ressources ; recevoir les briefings de renseignement stratégique ; approuver les accords de partage |
| **RSSI** | Propriété du programme ; gestion du portefeuille de sources ; supervision de la qualité des renseignements ; escalade pour les menaces critiques ; révision annuelle du programme ; approbation des exceptions |
| **Responsable informatique / Responsable sécurité** | Collecte et révision quotidiennes des renseignements ; déploiement des IoC dans les outils de sécurité ; consommation des renseignements tactiques et opérationnels ; analyse de la télémétrie interne |
| **Gestion des risques** | Intégrer les renseignements dans les évaluations des risques ; mettre à jour le registre des risques sur la base des résultats des renseignements ; évaluer les changements de risques liés aux menaces |
| **Réponse aux incidents** | Appliquer les renseignements lors des investigations ; extraire les IoC des incidents ; fournir des retours post-incident à la fonction renseignement |
| **Opérations informatiques** | Déployer les IoC dans les systèmes de détection et de blocage ; maintenir les intégrations de flux ; signaler les anomalies techniques identifiées par la surveillance |
| **Tout le personnel** | Signaler les activités suspectes et les événements de sécurité potentiels ; suivre la formation de sensibilisation aux menaces ; suivre les avis diffusés |

### Chemin d'escalade

- **Renseignement de routine** : Le Responsable informatique / Responsable sécurité examine et agit. Le RSSI est informé lors des intervalles de rapport réguliers.
- **Menace élevée** : Le Responsable informatique / Responsable sécurité escalade vers le RSSI dans les 4 heures. Le RSSI évalue l'exposition organisationnelle et détermine la réponse.
- **Menace critique / imminente** : Escalade immédiate vers le RSSI. Le RSSI informe la Direction générale et active la réponse aux incidents si cela est justifié.
- **Notification réglementaire** : Le RSSI coordonne la notification obligatoire au NCSC suisse le cas échéant (exploitants d'infrastructures critiques — dans les 24 heures selon l'art. 74b LSI).

---

## Preuves (renforcées pour l'audit)

Les preuves suivantes démontrent la conformité à cette politique. **Pour les audits SOC 2 Type II**, les auditeurs testeront l'efficacité opérationnelle en échantillonnant les preuves de la période d'audit (généralement 12 mois).

| N° | Preuve | Responsable | Fréquence | Détails de la piste d'audit |
|----|--------|-------------|-----------|------------------------------|
| 1 | **Inventaire des sources de renseignement** | RSSI | *Révision annuelle ; mise à jour lors des changements* | Document d'inventaire avec historique des versions ; journal des modifications montrant les ajouts/suppressions de sources avec dates et approbations |
| 2 | **Enregistrements d'évaluation des sources** | RSSI | *Annuel par source* | Modèle d'évaluation rempli pour chaque source ; notation documentée ; décision de conserver/remplacer la source avec justification |
| 3 | **Rapports de renseignement stratégique** | RSSI | *Trimestriel au minimum* | Documents de rapport avec liste de distribution et confirmation de livraison ; procès-verbaux de la Direction générale montrant la réception et la discussion |
| 4 | **Avis de renseignement tactique** | Responsable informatique / Responsable sécurité | *Mensuel au minimum ; ponctuel* | Documents d'avis avec horodatage de distribution ; accusé de réception par les parties prenantes clés |
| 5 | **Enregistrements de déploiement des IoC** | Opérations informatiques | *Par déploiement* | Tickets de déploiement ou journaux TIP indiquant : identifiant de l'IoC, source, date/heure de déploiement, systèmes cibles, méthode de déploiement, résultats des tests de validation |
| 6 | **Mises à jour du registre des risques** | Gestion des risques | *Par mise à jour* | Entrées du registre des risques avec horodatage « dernière mise à jour » ; champ « source de renseignement » documentant le rapport de renseignement ayant déclenché la mise à jour |
| 7 | **Enregistrements d'investigation des incidents** | Réponse aux incidents | *Par incident P1/P2* | Tickets d'incident avec section « contexte du renseignement sur les menaces » renseignée ; résultats de la corrélation des IoC ; évaluation de l'attribution à l'acteur de la menace (si faisable) |
| 8 | **Retours d'information post-incident** | Réponse aux incidents | *Par incident P1/P2* | Section post-mortem de l'incident documentant : nouveaux IoC découverts, TTP observés, lacunes dans les renseignements identifiées, recommandations pour l'amélioration de la détection |
| 9 | **Accords de partage externe** | RSSI | *Par accord ; révision annuelle* | NDA signés, accords d'adhésion ISAC, MoU de partage d'informations ; notes de révision annuelle confirmant que les accords sont à jour |
| 10 | **Enregistrements de conformité TLP** | RSSI | *Par événement de partage* | Journal de partage documentant : date, destinataire, classification TLP assignée, approbation (si TLP:AMBER ou supérieur), confirmation de l'accusé de réception TLP du destinataire |
| 11 | **Révisions des performances des fournisseurs** | RSSI | *Annuel par fournisseur* | Modèle de révision des fournisseurs avec données de conformité SLA, taux de faux positifs, analyse coût-bénéfice, recommandation de renouvellement avec signature d'approbation |
| 12 | **Résultats des tests de renseignement** | Sécurité informatique | *Par test (trimestriel/semestriel)* | Rapports de test documentant : date du test, périmètre du test, résultats (réussite/échec, indicateurs), lacunes identifiées, actions correctives assignées avec délais |
| 13 | **Tableau de bord des indicateurs** | RSSI | *Trimestriel* | Capture d'écran ou rapport du tableau de bord montrant tous les KPI ; graphiques de tendances pour la comparaison d'une année sur l'autre ; dépassements des seuils d'alerte mis en évidence avec l'état des actions correctives |
| 14 | **Révision annuelle du programme** | RSSI | *Annuelle* | Document de révision complet couvrant les performances des sources, l'efficacité de l'intégration, l'évaluation de la maturité, l'adéquation des ressources, diapositives de présentation à la Direction générale avec signatures d'approbation |

### Exigences de la piste d'audit

Pour les tests d'efficacité opérationnelle SOC 2 Type II, s'assurer que :

- **Exhaustivité** : Toutes les preuves requises existent pour toute la période d'audit (généralement 12 mois)
- **Exactitude** : Les preuves reflètent les activités réelles (pas des espaces réservés de modèles)
- **Horodatages** : Toutes les preuves clairement datées ; les preuves électroniques comprennent des métadonnées indiquant les dates de création/modification
- **Approbations** : Là où la politique exige une approbation (p. ex., exceptions, sélections de fournisseurs, accords de partage), l'approbation est documentée avec le nom et la date de l'approbateur
- **Population vs. Échantillon** : Les auditeurs testeront généralement :
  - **Tous** les rapports stratégiques (doivent être au minimum 4 par an)
  - Un **échantillon** de déploiements d'IoC (20-25 échantillons)
  - **Tous** les incidents cotés P1/P2 (doivent avoir un contexte de renseignement)
  - **Toutes** les sources (doivent avoir une évaluation annuelle)
  - **Tous** les contrats fournisseurs (doivent avoir une révision annuelle des performances)

---

# Conformité à la politique

## Mesure de la conformité

L'équipe de gestion de la sécurité de l'information vérifiera la conformité à cette politique par diverses méthodes, notamment les audits des sources de renseignement, les révisions de l'efficacité de l'intégration, le suivi de la diffusion, le recoupement avec le registre des risques, les audits internes et externes, et les retours d'information au propriétaire de la politique.

Les indicateurs suivants doivent être suivis et rapportés au RSSI trimestriellement :

| Indicateur | Cible | Seuil d'alerte |
|------------|-------|----------------|
| Sources de renseignement actives dans toutes les catégories obligatoires | 100 % des catégories obligatoires couvertes | Toute catégorie obligatoire avec 0 source active |
| Révisions d'évaluation des sources effectuées dans les délais | 100 % annuellement | < 80 % des sources révisées |
| Briefings de renseignement stratégique fournis | Trimestriel au minimum | Manqué dans > 1 trimestre consécutif |
| Actualité du déploiement des IoC | Dans les 24 heures suivant la réception validée | > 72 heures en moyenne |
| Mises à jour du registre des risques informées par les renseignements | Au minimum 1 par trimestre | 0 mise à jour au cours d'un trimestre |
| Completion des retours d'information post-incident (P1/P2) | 100 % | < 80 % |

**Exigences de rapportage** :
- **Tableau de bord mensuel du RSSI** : Sources actives, points forts des renseignements récents, état du déploiement des IoC, actions en cours.
- **Rapport trimestriel à la Direction générale** : Résumé du paysage stratégique des menaces, état des indicateurs, recommandations d'amélioration du programme.
- **Révision annuelle de la direction** : Évaluation complète de l'efficacité du programme incluant l'évaluation de la maturité, l'adéquation des ressources et les recommandations stratégiques.

Les indicateurs dépassant les seuils d'alerte doivent être escaladés au RSSI pour une attention immédiate et rapportés lors de la prochaine Révision de direction.

## Exceptions

Toute exception à cette politique doit être approuvée et consignée par le RSSI à l'avance, avec une acceptation documentée des risques, des contrôles compensatoires et une date de révision définie. Les exceptions courantes comprennent les contraintes budgétaires limitant l'accès aux sources commerciales, les limitations techniques empêchant l'intégration automatisée des flux, et les programmes nouvellement mis en œuvre n'ayant pas encore atteint les indicateurs cibles. Les exceptions nécessitant une allocation de ressources dépassant l'autorité du RSSI nécessitent une approbation conjointe du RSSI et de la Direction générale. Les exceptions sont limitées dans le temps (maximum 12 mois), révisées trimestriellement et rapportées à l'équipe de Révision de direction.

## Non-conformité

Un employé reconnu coupable d'avoir enfreint cette politique peut faire l'objet de mesures disciplinaires, pouvant aller jusqu'au licenciement. Les préoccupations spécifiques de non-conformité comprennent : le partage de renseignements en violation des désignations TLP ; le non-traitement des avis critiques sur les menaces dans les délais requis ; l'omission de signaler les menaces connues par les canaux établis ; et la divulgation non autorisée des sources ou méthodes de renseignement.

## Amélioration continue

Cette politique est révisée et mise à jour dans le cadre du processus d'amélioration continue. Les révisions doivent prendre en compte les changements dans le paysage des menaces, les nouvelles sources et capacités de renseignement, les résultats des audits, les changements réglementaires (y compris les exigences de notification du NCSC suisse), l'efficacité de l'intégration avec l'évaluation des risques et la gestion des incidents, la progression de la maturité du programme et les enseignements tirés des incidents liés aux renseignements. Les non-conformités relatives à cette politique doivent être enregistrées et gérées via le processus d'actions correctives SMSI (clause 10.2) avec analyse des causes profondes et remédiation suivie.

---

# Périmètre de la norme ISO 27001 couvert

Politique de renseignement sur les menaces — Cartographie des contrôles ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership et engagement | 5.1 Politiques de sécurité de l'information |
| Clause 5.3 Rôles, responsabilités et autorités | **5.7 Renseignement sur les menaces** |
| Clause 6.1 Actions face aux risques et opportunités | 5.24 Planification et préparation de la gestion des incidents |
| Clause 7.3 Sensibilisation | 5.25 Évaluation et décision sur les événements de sécurité |
| Clause 8.1 Planification et contrôle opérationnels | 8.7 Protection contre les logiciels malveillants |
| Clause 9.1 Surveillance, mesure, analyse et évaluation | 8.8 Gestion des vulnérabilités techniques |
| Clause 10.2 Non-conformité et actions correctives | 8.15 Journalisation |
| | 8.16 Activités de surveillance |

**Cadre réglementaire et juridique** :

| Cadre | Pertinence |
|-------|-----------|
| nFADP suisse (LPD révisée) | Art. 8 — Mesures techniques et organisationnelles (le renseignement sur les menaces comme mesure de sécurité proactive protégeant l'intégrité du traitement des données) |
| DSV suisse (Ordonnance sur la protection des données) | Art. 1-3 — Exigences minimales pour la sécurité des données |
| LSI art. 74b | Notification obligatoire des cyberincidents pour les exploitants d'infrastructures critiques (notification dans les 24 heures au NCSC, en vigueur depuis avril 2025) |
| RGPD UE (le cas échéant) | Art. 32 — Sécurité du traitement (mesures techniques et organisationnelles appropriées, y compris la détection des menaces) |
| ISO/IEC 27001:2022 | Contrôle Annexe A 5.7 — Renseignement sur les menaces |
| ISO/IEC 27002:2022 | Section 5.7 — Conseils d'implémentation pour le renseignement sur les menaces |
| NIST SP 800-53 Rév. 5 | PM-16 (Programme de sensibilisation aux menaces), RA-3 (Évaluation des risques), SI-5 (Alertes, avis et directives de sécurité) |
| NIST SP 800-150 | Guide to Cyber Threat Information Sharing |
| NIST CSF 2.0 | ID.RA (Évaluation des risques), DE.AE (Événements adverses), DE.CM (Surveillance continue) |
| CIS Controls v8 | Contrôle 13 (Surveillance et défense du réseau) — Le renseignement soutient la sensibilisation situationnelle et la détection |
| MITRE ATT&CK | Base de connaissances des tactiques et techniques adversariales — Taxonomie structurée pour l'analyse du renseignement |
| FIRST TLP v2.0 | Protocole des feux de signalisation — Standard de classification et de contrôle du partage du renseignement |
| OASIS STIX v2.1 / TAXII v2.1 | Standards d'échange structuré de renseignements sur les menaces et protocole de partage automatisé |

---

## Annexe A : Modèle de tableau de bord des indicateurs de renseignement

**Période du rapport :** T[X] [ANNÉE]
**Date du rapport :** [Date]
**Préparé par :** [RSSI/Responsable sécurité]

### Résumé exécutif
[Résumé en 2-3 paragraphes du paysage des menaces, des principales menaces identifiées, des actions prises]

### État du portefeuille de sources

| Catégorie de source | Requis | Actif | État | Action requise |
|---------------------|--------|-------|------|----------------|
| Gouvernement/CERT | ≥ 1 | [X] | Vert | Aucune |
| OSINT | ≥ 2 | [X] | Vert | Aucune |
| Télémétrie interne | Toutes | [X] | Vert | Aucune |
| Commercial | [Selon budget] | [X] | Vert | Aucune |
| Avis fournisseurs | Tous les fournisseurs critiques | [X] | Ambre | Flux d'avis [Fournisseur X] non surveillé ; action : s'abonner avant le [date] |

### Indicateurs clés de performance

| Indicateur | Cible | T[X] Réel | Tendance | État |
|------------|-------|-----------|----------|------|
| Sources actives (toutes catégories obligatoires) | 100 % | 100 % | Stable | Conforme |
| Évaluations des sources effectuées | 100 % annuellement | 25 % en cours d'année (dans les délais) | En hausse | Conforme |
| Briefings stratégiques fournis | ≥ 1 par trimestre | 1 | Stable | Conforme |
| Actualité du déploiement des IoC | < 24 h en moyenne | 18 h en moyenne | Amélioré | Conforme |
| Mises à jour du registre des risques | ≥ 1 par trimestre | 3 | En hausse | Conforme |
| Taux de vrais positifs (alertes issues des renseignements) | > 70 % | 78 % | En hausse | Conforme |
| Completion des retours post-incident (P1/P2) | 100 % | 100 % (2/2 incidents) | Stable | Conforme |

### Résumé des activités de renseignement

- **IoC déployés ce trimestre :** [X] indicateurs (répartition : [Y] adresses IP, [Z] domaines, [N] hachages de fichiers)
- **Alertes générées par les renseignements :** [X] alertes ; [Y] vrais positifs, [Z] faux positifs
- **Incidents exploitant les renseignements :** [X] investigations ont utilisé le contexte de renseignement sur les menaces
- **Mises à jour du risque pilotées par les renseignements :** [X] entrées du registre des risques mises à jour
- **Renseignements partagés en externe :** [X] événements de partage (tous conformes au TLP)

### Principales menaces identifiées ce trimestre

1. **[Nom de la menace]** — [Brève description, pertinence pour l'organisation, action prise]
2. **[Nom de la menace]** — [Brève description, pertinence pour l'organisation, action prise]
3. **[Nom de la menace]** — [Brève description, pertinence pour l'organisation, action prise]

### Améliorations du programme de renseignement ce trimestre

- [Action d'amélioration 1 avec état d'avancement]
- [Action d'amélioration 2 avec état d'avancement]

### Priorités pour le trimestre suivant

- [Action prioritaire 1]
- [Action prioritaire 2]

**Préparé par :** [Nom, Rôle]
**Révisé par :** [RSSI]
**Distribution :** Direction générale, Gestion des risques, Responsable des opérations informatiques

---

<!-- QA_VERIFIED: 2026-03-29 -->
