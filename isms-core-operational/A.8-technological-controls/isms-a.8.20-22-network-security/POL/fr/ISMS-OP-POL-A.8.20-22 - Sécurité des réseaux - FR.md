<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.8.20-22-FR:operational:OP-POL:a.8.20-22 -->
**ISMS-OP-POL-A.8.20-22 — Sécurité des réseaux**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Sécurité des réseaux |
| **Type de document** | Politique opérationnelle |
| **Identifiant du document** | ISMS-OP-POL-A.8.20-22 |
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

- ISO/IEC 27001:2022 Contrôles A.8.20, A.8.21, A.8.22 — Sécurité des réseaux, sécurité des services réseau, cloisonnement des réseaux

**Contrôles Annexe A associés** :

| Contrôle | Relation avec la sécurité des réseaux |
|----------|---------------------------------------|
| A.5.14 Transfert de l'information | Exigences de chiffrement et de canaux sécurisés pour les données en transit |
| A.5.15 Contrôle d'accès | Contrôle d'accès réseau aligné sur la politique d'identité et d'accès |
| A.5.23 Sécurité de l'information pour les services cloud | Connectivité réseau cloud et segmentation |
| A.8.1 Appareils des utilisateurs finaux | Conformité des terminaux avant l'admission réseau |
| A.8.5 Authentification sécurisée | Authentification pour l'accès réseau (802.1X, VPN) |
| A.8.9 Gestion de la configuration | Configurations de référence et durcissement des appareils réseau |
| A.8.15 Journalisation | Journalisation des événements et du trafic réseau |
| A.8.16 Activités de surveillance | Surveillance réseau, IDS/IPS, détection d'anomalies |
| A.8.23 Filtrage web | Filtrage URL/DNS comme contrôle au niveau réseau |
| A.8.24 Utilisation de la cryptographie | TLS/IPsec pour le transport réseau chiffré |

**Politiques internes associées** :

- Politique de contrôle d'accès
- Politique d'utilisation de la cryptographie
- Politique de transfert de l'information
- Politique de sécurité physique et environnementale
- Politique de gestion des actifs
- Politique de journalisation
- Politique des activités de surveillance (A.8.16)

---

# Politique de gestion de la sécurité des réseaux

## Finalité

La présente politique a pour objet d'assurer la protection des informations dans les réseaux et dans les installations de traitement de l'information qui les supportent.

La présente politique soutient la nLPD (revLPD) suisse et l'Ordonnance sur la protection des données (OPDo) en mettant en œuvre des mesures techniques et organisationnelles appropriées au risque pour protéger les données personnelles (y compris les données personnelles sensibles) par des mesures de sécurité réseau. Lorsque l'organisation traite des données de personnes dans l'UE/EEE, les exigences du RGPD s'appliquent également.

## Champ d'application

Tous les employés et utilisateurs tiers.

Tous les réseaux, services réseau, solutions d'administration et de gestion réseau et appareils réseau de l'organisation considérés dans le périmètre par la déclaration de périmètre ISO 27001.

## Principe

Le réseau est géré selon le principe du moindre privilège avec la sécurité dès la conception et par défaut. L'accès réseau est refusé par défaut et accordé uniquement avec une approbation documentée. Toutes les décisions d'architecture réseau doivent être fondées sur le risque, en tenant compte de la classification des informations et de la criticité des systèmes.

---

## Contrôles réseau

- Les responsabilités et procédures pour la gestion des équipements réseau doivent être établies et documentées.
- La responsabilité opérationnelle des réseaux doit être séparée des opérations informatiques lorsque c'est approprié.
- Des contrôles spéciaux doivent être établis pour protéger la confidentialité et l'intégrité des données transitant sur les réseaux publics ou les réseaux sans fil et pour protéger les systèmes et applications connectés.
- Une journalisation et une surveillance appropriées doivent être appliquées pour permettre l'enregistrement et la détection des actions susceptibles d'affecter la sécurité de l'information ou qui y sont pertinentes.
- Les activités de gestion doivent être étroitement coordonnées pour optimiser le service à l'organisation et s'assurer que les contrôles sont appliqués de manière cohérente sur l'infrastructure de traitement de l'information.
- Les systèmes sur le réseau doivent être authentifiés avant de se voir accorder l'accès.
- Les connexions des systèmes au réseau doivent être limitées aux appareils autorisés et conformes.
- Les mots de passe et comptes par défaut des appareils réseau doivent être changés ou désactivés avant le déploiement.
- L'accès administratif aux appareils réseau doit utiliser des protocoles de gestion chiffrés (SSH, HTTPS). Telnet et SNMP non chiffré (v1/v2c) ne doivent pas être utilisés.
- Les microprogrammes et logiciels des appareils réseau doivent être maintenus à des versions actuelles prises en charge par le fournisseur. Les correctifs de sécurité doivent être appliqués selon les délais suivants :

| Gravité | Délai |
|---------|-------|
| Vulnérabilités critiques (CVSS 9.0+, exploitation active) | Dans les 14 jours |
| Vulnérabilités élevées (CVSS 7.0–8.9) | Dans les 30 jours |
| Vulnérabilités moyennes (CVSS 4.0–6.9) | Dans les 90 jours |
| Vulnérabilités faibles (CVSS 0.1–3.9) | Prochaine fenêtre de maintenance planifiée |

Les correctifs d'urgence pour les vulnérabilités activement exploitées peuvent être déployés sans tests en environnement non-production avec l'approbation du RSSI et une acceptation du risque documentée.

## Sécurité des services réseau

Les mécanismes de sécurité, les niveaux de service et les exigences de gestion de tous les services réseau doivent être identifiés et inclus dans les accords de services réseau, que ces services soient fournis en interne ou externalisés.

La capacité du fournisseur de services réseau à gérer les services convenus de manière sécurisée doit être déterminée et régulièrement surveillée, et le droit d'audit doit être convenu.

Les mesures de sécurité nécessaires pour des services particuliers, telles que les fonctionnalités de sécurité, les niveaux de service et les exigences de gestion, doivent être identifiées. L'organisation doit s'assurer que les fournisseurs de services réseau mettent en œuvre ces mesures.

Les services réseau comprennent notamment :

- Services DNS, DHCP et NTP.
- Services de courriel, de partage de fichiers et d'applications web.
- Services de pare-feu, de détection/prévention d'intrusion et de sécurité des passerelles.
- Services d'accès à distance et VPN.

## Cloisonnement des réseaux

Les grands réseaux doivent être divisés en domaines réseau distincts. Les domaines doivent être choisis en fonction des niveaux de confiance, de la classification des données et de la fonction métier.

Le cloisonnement peut être réalisé à l'aide de réseaux physiquement différents ou de réseaux logiques différents (p. ex. VLANs, réseaux définis par logiciel).

Le périmètre de chaque domaine doit être bien défini. L'accès entre les domaines réseau doit être contrôlé au périmètre à l'aide d'une passerelle (p. ex. pare-feu, routeur filtrant) avec une posture de refus par défaut.

Les critères de cloisonnement des réseaux en domaines, et les accès autorisés via les passerelles, doivent être fondés sur une évaluation des exigences de sécurité de chaque domaine. L'évaluation doit être conforme à la politique de contrôle d'accès, aux exigences d'accès, à la valeur et à la classification des informations traitées, et doit tenir compte du coût relatif et de l'impact sur les performances de l'incorporation d'une technologie de passerelle appropriée.

**Gouvernance des règles de pare-feu** :

- Toutes les modifications des règles de pare-feu doivent suivre un processus de gestion des changements documenté avec justification métier et approbation.
- Les ensembles de règles de pare-feu doivent être révisés au moins **annuellement** pour supprimer les règles obsolètes et vérifier la justification métier continue.
- Les révisions doivent être documentées avec signature de l'administrateur réseau et du RSSI.
- La politique de refus par défaut doit être vérifiée lors de chaque révision (tout le trafic bloqué sauf si explicitement autorisé).

Les segments réseau minimum doivent inclure :

| Segment | Objectif |
|---------|---------|
| Réseau d'entreprise / utilisateurs | Postes de travail et appareils standard des employés |
| Réseau des serveurs / applications | Applications métier et bases de données |
| Réseau de gestion | Administration des appareils réseau (hors bande si possible) |
| Réseau invité | Accès des visiteurs et appareils non-entreprise (isolé du réseau d'entreprise) |
| Réseau IoT / OT | Appareils Internet des objets et de technologie opérationnelle (isolés) |

Des segments supplémentaires (p. ex. DMZ pour les services exposés au public, environnements de développement/test) doivent être créés sur la base d'une évaluation des risques.

### Exigences du réseau invité

Les réseaux invités doivent être configurés avec les mesures de sécurité suivantes :

- **Isolation** : Pas d'accès aux segments du réseau d'entreprise (les règles de pare-feu doivent imposer la séparation).
- **Accès Internet uniquement** : Les invités n'accèdent qu'à Internet, pas aux ressources internes.
- **Chiffrement** : WPA2-Personnel minimum avec une phrase de passe robuste, ou WPA2-Entreprise avec des identifiants invités.
- **Accès limité dans le temps** : Les identifiants invités doivent expirer après une période définie (p. ex. 24 heures) et être réémis selon les besoins.
- **Surveillance** : Le trafic du réseau invité doit être journalisé pour investigation sécuritaire si nécessaire.

La phrase de passe du réseau invité doit être changée au moins **trimestriellement** ou immédiatement en cas de suspicion de compromission.

### Sécurité des appareils IoT et OT

Les appareils IoT (Internet des objets) et OT (Technologie opérationnelle) doivent être placés sur un segment réseau isolé avec les mesures de contrôle suivantes :

- Les appareils IoT/OT ne doivent pas avoir d'accès Internet direct et non contrôlé. Les communications Internet doivent être acheminées via un proxy ou une passerelle avec des destinations autorisées.
- Les appareils IoT/OT ne doivent pas être accessibles depuis Internet sans VPN et autorisation explicite.
- L'accès depuis le réseau d'entreprise vers le segment IoT/OT doit être restreint au personnel autorisé via des règles de pare-feu.
- L'accès à distance des fournisseurs tiers aux appareils IoT/OT nécessite une approbation, un VPN et des identifiants limités dans le temps.
- Tous les mots de passe par défaut des appareils IoT/OT doivent être changés avant le déploiement.
- Tous les appareils IoT/OT doivent être enregistrés dans le registre des actifs avec leur propriétaire, leur objectif et leur emplacement réseau.

### Cloisonnement des réseaux sans fil

Les réseaux sans fil nécessitent un traitement spécial en raison du périmètre réseau mal défini. Pour les environnements sensibles, tout accès sans fil doit être traité comme une connexion externe et cloisonné des réseaux internes jusqu'à ce que l'accès soit passé par une passerelle avant d'accorder l'accès aux systèmes internes.

L'accès réseau sans fil pour le personnel et les invités doit être cloisonné sur des SSID distincts avec des mesures de sécurité différenciées.

### Normes de sécurité sans fil

Les normes de sécurité sans fil suivantes s'appliquent :

- WPA3 est préféré pour tous les réseaux sans fil.
- Le mode WPA2 Entreprise avec authentification 802.1X et chiffrement AES est la norme minimale acceptable pour les réseaux d'entreprise.
- Le mode WPA2 Personnel peut être utilisé pour les réseaux non-production (p. ex. accès invité) avec une phrase de passe aléatoire d'au moins 16 caractères et le chiffrement AES.
- WEP ne doit en aucun cas être utilisé.
- WPA (original) et le chiffrement TKIP ne doivent pas être utilisés.

## Accès aux réseaux et aux services réseau

Les utilisateurs ne doivent se voir accorder l'accès qu'aux réseaux et services réseau pour lesquels ils ont été spécifiquement autorisés.

L'accès aux réseaux et aux services réseau doit être conforme à la Politique de contrôle d'accès.

Avant de se connecter au réseau, les appareils doivent :

- Être enregistrés dans le registre des actifs.
- Avoir été mis à jour avec les derniers correctifs de sécurité.
- Avoir une protection contre les logiciels malveillants appropriée et à jour.
- Avoir leurs mots de passe et comptes par défaut changés ou désactivés.
- Être inclus dans la mesure du possible dans le système de gestion et de surveillance réseau.
- Avoir supprimé ou désactivé les ports, services, applications et comptes invités non requis.

L'organisation doit mettre en œuvre des mesures techniques pour imposer la conformité des appareils avant d'accorder l'accès réseau. Les mécanismes d'application comprennent les solutions de contrôle d'accès réseau (NAC), l'authentification basée sur des certificats ou des identifiants 802.1X, l'évaluation de la posture de la passerelle VPN, ou l'enregistrement et l'approbation manuels par l'IT. Les appareils non conformes doivent être placés dans un segment de quarantaine ou restreint jusqu'à ce que la conformité soit atteinte.

## Accès à distance

L'accès à distance au réseau de l'organisation doit être sécurisé à l'aide de tunnels chiffrés (VPN ou équivalent) avec authentification multifacteur.

Les connexions VPN doivent utiliser des protocoles actuels et sécurisés :

- WireGuard ou IKEv2/IPsec sont préférés.
- OpenVPN est acceptable lorsque WireGuard ou IKEv2 ne sont pas pris en charge.
- PPTP et L2TP sans IPsec ne doivent pas être utilisés.

Les connexions à distance doivent être configurées pour se déconnecter après une période définie d'inactivité.

Une liste des utilisateurs ayant un accès à distance doit être maintenue et révisée trimestriellement.

La tunnellisation fractionnée (permettant à une partie du trafic de contourner le VPN) ne peut être autorisée que lorsque :

- Une évaluation des risques documentée démontre un risque résiduel acceptable.
- Toutes les ressources de l'organisation (partages de fichiers, bases de données, applications, courriel) ne sont accessibles que via le tunnel chiffré.
- Le trafic en tunnellisation fractionnée est limité à des destinations non sensibles accessibles uniquement via Internet.
- Le terminal de l'utilisateur satisfait à toutes les exigences de référence de sécurité (correctifs actuels, antivirus/EDR, chiffrement).
- La tunnellisation fractionnée est désactivée pour les comptes à privilèges et les comptes administrateurs.

## Emplacements réseau

L'infrastructure réseau et les emplacements de traitement des données doivent être sélectionnés sur la base d'une évaluation des risques, de la classification des données et des exigences applicables en matière de protection des données.

La hiérarchie de préférence suivante s'applique pour l'emplacement de l'infrastructure réseau, des centres de données et des services cloud traitant des données personnelles ou confidentielles :

1. En Suisse.
2. Dans les pays reconnus par le Conseil fédéral suisse comme offrant une protection adéquate des données conformément à l'**Annexe 1 de l'Ordonnance sur la protection des données (OPDo)**. La liste d'adéquation actuelle est publiée par le Préposé fédéral à la protection des données et à la transparence (PFPDT) et doit être vérifiée avant tout déploiement d'infrastructure ou de services dans une nouvelle juridiction.
3. Dans les pays où des Clauses contractuelles types (CCT) ou d'autres garanties appropriées selon la nLPD art. 16–17 sont en place.

Les transferts de données transfrontaliers doivent être conformes à la Politique de transfert de l'information et aux exigences de la nLPD. Le conseil juridique doit vérifier le statut d'adéquation de tout pays avant le déploiement.

## Appareils réseau physiques

Les appareils réseau physiques doivent être gérés conformément à la Politique de sécurité physique et environnementale, notamment les sections sur la sécurité du câblage, l'emplacement et la protection des équipements, et le contrôle d'accès.

Les appareils réseau physiques doivent être détruits conformément à la Politique de classification et de traitement de l'information, notamment la section sur la destruction des supports et appareils électroniques.

Les appareils réseau physiques doivent être gérés conformément à la Politique de gestion des actifs et soumis au processus de gestion des actifs.

## Filtrage web

L'accès aux sites web contenant des informations illicites ou connus pour contenir du contenu malveillant doit être restreint.

L'accès aux types de sites web suivants doit être bloqué dans la mesure du possible :

- Sites web avec une fonction de téléchargement d'informations, sauf si autorisé pour des raisons professionnelles valables.
- Sites web malveillants connus ou suspectés (phishing, distribution de logiciels malveillants).
- Serveurs de commande et contrôle.
- Sites web malveillants identifiés dans les flux de renseignement sur les menaces.
- Sites web partageant du contenu illicite.
- Services de proxy et d'anonymisation (sauf si requis à des fins professionnelles approuvées).

Le filtrage web doit être mis en œuvre à l'aide d'un filtrage DNS, d'un proxy web ou d'une technologie équivalente. Les catégories de filtres et les exceptions doivent être révisées trimestriellement.

### Sécurité DNS

- Les résolveurs DNS devraient valider les signatures DNSSEC lorsqu'elles sont disponibles pour se protéger contre l'usurpation DNS.
- Les zones DNS internes ne doivent pas être exposées à Internet. Le DNS à horizon partagé (split-horizon DNS) est recommandé pour les organisations avec une résolution de noms interne et externe.
- Les requêtes DNS devraient être journalisées pour l'investigation sécuritaire et la détection des menaces.

## Intrusion sur les hôtes, intrusion réseau, logiciels malveillants et antivirus

Les services et appareils réseau doivent être gérés conformément à la Politique sur les logiciels malveillants et les antivirus.

La détection d'intrusion sur les hôtes et la détection/prévention d'intrusion réseau doivent être déployées selon le risque, le besoin métier et lorsque c'est pratiquement faisable.

**Emplacements minimums de déploiement IDS/IPS** :

| Emplacement | Type | Objectif |
|-------------|------|---------|
| Périmètre Internet (pare-feu/passerelle) | IDS/IPS réseau | Détecter/prévenir les attaques externes et le trafic entrant malveillant |
| Entre les segments réseau (inter-VLAN) | IDS/IPS réseau | Détecter les déplacements latéraux entre les zones de confiance |
| Réseau des serveurs/applications | IDS réseau ou IDS sur hôte | Détecter les accès anormaux aux systèmes critiques |
| Terminaux (postes de travail, serveurs) | IDS sur hôte (EDR/XDR) | Détecter les menaces au niveau terminal, les logiciels malveillants sans fichier, les processus suspects |
| Charges de travail cloud (IaaS/PaaS) | IDS natif cloud ou CASB | Détecter les menaces ciblant l'infrastructure cloud |

Des emplacements de déploiement supplémentaires doivent être déterminés par évaluation des risques. Lorsque des appareils IDS/IPS dédiés ne sont pas faisables, des capacités de détection équivalentes (p. ex. EDR avec visibilité réseau, outils de sécurité natifs cloud) sont acceptables.

Le trafic réseau doit être surveillé pour détecter les comportements anormaux. Les alertes de sécurité doivent être triées et escaladées conformément au processus de gestion des incidents.

---

## Preuves

Les preuves suivantes démontrent la conformité à la présente politique :

- **Schéma d'architecture réseau** (actuel, montrant les segments, les zones de confiance, les passerelles) — *mis à jour lors des changements ; révisé annuellement*
- **Ensembles de règles de pare-feu et de passerelles** avec historique des changements documenté et signature de la révision annuelle — *changements de règles conservés 3 ans ; révision annuelle documentée avec signature du RSSI*
- **Inventaire des appareils réseau et configurations de référence** — *mis à jour dans les 5 jours ouvrables suivant un changement ; audité annuellement*
- **Relevés de configuration de sécurité sans fil** (WPA3/WPA2-Entreprise) — *révisés semestriellement*
- **Liste d'accès VPN et relevés de révision trimestrielle** — *révisés trimestriellement ; comptes inactifs désactivés*
- **Configuration du filtrage web et journaux des exceptions** — *exceptions révisées trimestriellement ; catégories de filtres mises à jour mensuellement*
- **Rapports de surveillance réseau et d'alertes IDS/IPS** — *conservés 12 mois minimum ; alertes critiques révisées quotidiennement*
- **Révision des accès réseau et relevés de conformité des appareils** — *révisés trimestriellement pour l'accès à privilèges ; annuellement pour le standard*
- **Rapports de conformité aux correctifs** (appareils réseau selon le tableau de délais CVSS) — *révisés mensuellement*
- **Relevés de rotation de la phrase de passe du réseau invité** — *rotation trimestrielle documentée*

---

# Conformité à la politique

## Mesure de la conformité

L'équipe de management de la sécurité de l'information vérifiera la conformité à la présente politique par diverses méthodes, notamment les audits de configuration réseau, les tests de pénétration, les analyses de vulnérabilités, les audits internes et externes, et les retours au propriétaire de la politique.

## Exceptions

Toute exception à la présente politique doit être approuvée et enregistrée par le Responsable de la sécurité de l'information à l'avance, avec acceptation documentée du risque, mesures compensatoires et date de révision définie. Les exceptions doivent être rapportées à l'Équipe de revue de direction.

## Non-conformité

Un employé reconnu avoir violé la présente politique peut être soumis à des mesures disciplinaires pouvant aller jusqu'au licenciement.

## Amélioration continue

La présente politique est révisée et mise à jour dans le cadre du processus d'amélioration continue. Les révisions doivent prendre en compte les modifications des normes de sécurité réseau, les menaces émergentes, les changements réglementaires et les enseignements tirés des incidents.

---

# Domaines de la norme ISO 27001 couverts

Politique de sécurité des réseaux — Correspondance avec les contrôles ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership et engagement | 5.1 Politiques de sécurité de l'information |
| Clause 5.2 Politique | 5.4 Responsabilités de la direction |
| Clause 6.2 Objectifs de sécurité de l'information | 5.36 Conformité aux politiques, règles et normes |
| Clause 7.3 Sensibilisation | 6.3 Sensibilisation, éducation et formation à la sécurité de l'information |
| | 6.4 Processus disciplinaire |
| | **8.20 Sécurité des réseaux** |
| | **8.21 Sécurité des services réseau** |
| | **8.22 Cloisonnement des réseaux** |
| | 8.23 Filtrage web |

**Cadre réglementaire et légal** :

| Cadre | Pertinence |
|-------|-----------|
| nLPD suisse (revLPD) | Art. 8 — Mesures techniques et organisationnelles pour la protection des données |
| OPDo suisse (Ordonnance sur la protection des données) | Art. 1–3 — Exigences minimales pour la sécurité des données ; Annexe 1 — Liste d'adéquation |
| RGPD UE (le cas échéant) | Art. 32 — Sécurité du traitement (contrôles réseau comme mesure appropriée) |
| ISO/IEC 27001:2022 | Contrôles Annexe A 8.20, 8.21, 8.22 |
| ISO/IEC 27002:2022 | Sections 8.20, 8.21, 8.22 — Lignes directrices de mise en œuvre |
| NIST SP 800-53 Rév. 5 | SC-7 (Protection des frontières), SC-8 (Confidentialité des transmissions) |
| CIS Controls v8 | Contrôle 12 (Gestion de l'infrastructure réseau), Contrôle 13 (Surveillance et défense du réseau) |

<!-- QA_VERIFIED: 2026-03-29 -->
