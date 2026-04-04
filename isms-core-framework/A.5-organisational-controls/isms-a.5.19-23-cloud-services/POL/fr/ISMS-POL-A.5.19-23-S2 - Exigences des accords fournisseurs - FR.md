<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.19-23-S2-FR:framework:POL:a.5.19-23-s2 -->
**ISMS-POL-A.5.19-23-S2 — Exigences des accords fournisseurs**
**Contrôle A.5.20 : Prise en compte de la sécurité de l'information dans les accords avec les fournisseurs**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Exigences des accords fournisseurs |
| **Type de document** | Section de politique |
| **Identifiant du document** | ISMS-POL-A.5.19-23-S2 |
| **Créateur du document** | Responsable de la sécurité de l'information (RSI) |
| **Propriétaire du document** | Responsable de la sécurité des systèmes d'information (RSSI) |
| **Approuvé par** | Direction générale |
| **Date de création** | [Date] |
| **Version** | 1.0 |
| **Date de version** | [À définir] |
| **Classification** | Interne |
| **Statut** | Projet |

**Historique des versions** :

| Version | Date | Auteur | Modifications |
|---------|------|--------|---------------|
| 1.0 | [Date] | RSI | Section initiale pour le contrôle ISO 27001:2022 A.5.20 |

**Cycle de révision** : Annuel
**Prochaine date de révision** : [Date d'entrée en vigueur + 12 mois]

**Chaîne d'approbation** :

- Principal : Responsable de la sécurité des systèmes d'information (RSSI)
- Secondaire : Responsable de la sécurité de l'information (RSI)
- Conformité : Responsable juridique/conformité
- Achats : Directeur des achats
- Autorité finale : Direction générale

**Documents connexes** :

- ISMS-POL-00 (Cadre d'applicabilité réglementaire)
- ISMS-POL-A.5.19-23 (Politique parente — Sécurité des fournisseurs et des services en nuage)
- ISMS-POL-A.5.19-23-S1 (Fondamentaux des relations fournisseurs)
- ISMS-IMP-A.5.19-23.S2-UG/TG (Diligence raisonnable et contrats fournisseurs)
- ISO/IEC 27001:2022 Contrôle A.5.20
- ISO/IEC 27036-2 (Exigences)
- RGPD Article 28 (Exigences des sous-traitants)

---

# Objet

La présente section définit les exigences de sécurité de l'information obligatoires qui doivent figurer dans les accords fournisseurs. Elle garantit que les obligations de sécurité sont contractuellement contraignantes et exécutoires tout au long de la relation fournisseur.

**Principe critique — « Les contrats sont votre dernière ligne de défense »** : Les exigences de sécurité sans exécutabilité contractuelle ne sont que des suggestions que les fournisseurs peuvent ignorer sans conséquence. La présente politique garantit que chaque accord fournisseur comprend des clauses de sécurité exécutoires, des droits d'audit, des exigences de notification d'incidents et des dispositions de responsabilité. Les accords informels, les engagements verbaux ou les contrats sans clauses de sécurité créent une vulnérabilité juridique et un risque opérationnel qu'aucun contrôle technique ne peut atténuer après une violation.

**ISO/IEC 27001:2022 Contrôle A.5.20 — Prise en compte de la sécurité de l'information dans les accords avec les fournisseurs**

> *Des exigences de sécurité de l'information pertinentes devraient être établies et convenues avec chaque fournisseur susceptible d'accéder, de traiter, de stocker, de communiquer ou de fournir des composants d'infrastructure informatique pour les informations de l'organisation.*

**Objectif du contrôle** : S'assurer que les exigences de sécurité de l'information sont contractuellement contraignantes et exécutoires tout au long de la relation fournisseur.

---

# Périmètre

## Accords applicables

La présente section s'applique à tous les accords formels avec les fournisseurs, notamment :

| Type d'accord | Description |
|---------------|-------------|
| Contrats-cadres de services (MSA) | Contrats généraux régissant la relation |
| Accords de niveau de service (SLA) | Engagements de performance et de disponibilité |
| Accords de traitement des données (ATD) | Traitement des données personnelles (RGPD, nLPD) |
| Accords de non-divulgation (NDA) | Engagements de confidentialité |
| Énoncés des travaux (SOW) | Périmètre de projet ou de service spécifique |
| Contrats de licence logicielle | Conditions d'utilisation des logiciels |
| Accords de services en nuage | Conditions de consommation des services en nuage |

## Responsabilité de la revue des accords

| Niveau du fournisseur | Revue de l'accord par |
|-----------------------|-----------------------|
| Niveau 1 (Critique) | Juridique + Sécurité + Responsable métier + Achats |
| Niveau 2 (Élevé) | Juridique + Sécurité + Achats |
| Niveau 3 (Moyen) | Achats + Sécurité (si accès aux données) |
| Niveau 4 (Faible) | Achats (conditions standard acceptables) |

**Délais de revue** :

- Nouveaux accords : Avant la signature du contrat
- Renouvellements : Au minimum 60 jours avant l'expiration (permet la renégociation)
- Avenants : Avant l'exécution des changements importants

---

# Clauses de sécurité obligatoires

## Exigences des clauses par niveau de fournisseur

| Clause de sécurité | N1 | N2 | N3 | N4 |
|--------------------|----|----|----|----|
| Obligations de confidentialité | ✓ | ✓ | ✓ | ✓ |
| Conformité à la protection des données | ✓ | ✓ | ✓ | — |
| Engagement en matière de contrôles de sécurité | ✓ | ✓ | ✓ | — |
| Notification d'incident | ✓ | ✓ | ✓ | — |
| Droits d'audit | ✓ | ✓ | — | — |
| Restrictions sur les sous-traitants | ✓ | ✓ | — | — |
| Exigences de continuité d'activité | ✓ | ✓ | — | — |
| Retour/destruction des données | ✓ | ✓ | ✓ | — |
| Dispositions de responsabilité | ✓ | ✓ | ✓ | — |
| Droits de résiliation | ✓ | ✓ | ✓ | ✓ |
| Exigences d'assurance | ✓ | ✓ | — | — |

## Obligations de confidentialité

**Éléments requis :**

| Élément | Exigence |
|---------|----------|
| Définition de l'information confidentielle | Périmètre clair de ce qui est protégé (données, systèmes, informations commerciales) |
| Utilisation autorisée | Limitée à la prestation de service uniquement, pas d'autres fins |
| Divulgation autorisée | Selon le besoin d'en connaître, personnes nommément désignées uniquement, avec confidentialité équivalente |
| Norme de protection | « Soin raisonnable » minimum, spécifier les contrôles (chiffrement, restrictions d'accès) |
| Durée | Survit à la résiliation (minimum 3 ans, ou à perpétuité pour les secrets commerciaux) |
| Retour/destruction | Lors de la résiliation ou sur demande, avec certification |
| Exceptions | Informations publiques, développées indépendamment, requises légalement (avec préavis) |

**Clause modèle** :
> « Le fournisseur traitera toutes les informations de [Organisation] comme confidentielles et ne les utilisera, divulguera ou reproduira pas, sauf dans la mesure nécessaire à la prestation des services. Le fournisseur protégera les informations de [Organisation] en faisant preuve d'au moins le même niveau de soin que celui utilisé pour protéger ses propres informations confidentielles de sensibilité similaire, et en tout état de cause d'un soin raisonnable. »

## Conformité à la protection des données

**Éléments requis :**

| Élément | Exigence |
|---------|----------|
| Définition des rôles | Désignation responsable du traitement vs. sous-traitant conformément au RGPD/nLPD |
| Finalité du traitement | Limitée aux finalités spécifiées uniquement |
| Catégories de données | Types de données personnelles traitées |
| Personnes concernées | Catégories de personnes concernées (employés, clients, etc.) |
| Lieu de traitement | Restrictions géographiques le cas échéant (UE, CH, juridictions spécifiques) |
| Mesures techniques | Contrôles de sécurité pour les données personnelles (chiffrement, pseudonymisation) |
| Mesures organisationnelles | Politiques, formation, contrôles d'accès |
| Règles sur les sous-traitants ultérieurs | Approbation préalable requise, exigences de transmission |
| Droits des personnes concernées | Soutien aux demandes d'accès, de rectification, d'effacement, de portabilité |
| Notification de violation | Dans les 24 heures à [Organisation], coopération avec la notification à l'autorité |
| Coopération à l'audit | Soutien aux audits réglementaires, analyses d'impact sur la protection des données |
| Transferts internationaux | Clauses contractuelles types (CCT) ou mécanismes d'adéquation |

**Note** : Pour les opérations suisses/européennes, l'accord de traitement des données (ATD) doit satisfaire :

- **RGPD Article 28** : Obligations des sous-traitants et exigences de sécurité
- **nLPD suisse Article 9** : Sécurité et confidentialité du sous-traitant
- **DORA Article 29** (le cas échéant) : Exigences supplémentaires pour les prestataires de services TIC

## Engagement en matière de contrôles de sécurité

**Langage contractuel requis** :

> « Le fournisseur mettra en œuvre et maintiendra des contrôles de sécurité administratifs, techniques et physiques adaptés à la classification des données auxquelles il accède, conformément aux normes sectorielles (ISO/IEC 27001, Critères de confiance des services SOC 2) et aux exigences spécifiées à l'Annexe [X] (Exigences de sécurité). »

**L'annexe sur les exigences de sécurité doit spécifier :**

| Domaine de contrôle | Exigences |
|---------------------|-----------|
| Gestion des accès | Authentification (AMF pour les accès privilégiés), autorisation (RBAC), journalisation des accès |
| Chiffrement | En transit (TLS 1.2+), au repos (AES-256 ou équivalent) |
| Sécurité réseau | Segmentation, pare-feu, détection/prévention des intrusions, surveillance |
| Sécurité des postes de travail | Protection contre les maliciels, EDR, correctifs |
| Sécurité du personnel | Vérifications des antécédents, formation à la sensibilisation à la sécurité, procédures de départ |
| Sécurité physique | Contrôles d'accès aux installations (le cas échéant), protections environnementales |
| Gestion des incidents | Détection, analyse, confinement, éradication, reprise, retours d'expérience |
| Gestion des changements | Changements contrôlés avec tests, capacité de retour arrière, notification à [Organisation] |
| Gestion des vulnérabilités | Scans, gestion des correctifs, tests d'intrusion |
| Sauvegarde et reprise | Sauvegardes régulières, stockage hors site, tests de restauration |

---

# Exigences de notification d'incident

## Délais de notification

| Type d'incident | Délai de notification | Destinataire |
|-----------------|----------------------|--------------|
| Violation de données confirmée | Dans les 4 heures suivant la confirmation | RSSI + RSI + Responsable métier |
| Violation de données suspectée | Dans les 24 heures suivant la détection | RSI + Responsable métier |
| Incident de sécurité (non-violation) | Dans les 48 heures | Équipe sécurité |
| Interruption de service (critique) | Dans l'heure | Exploitation IT + Responsable métier |
| Interruption de service (non critique) | Dans les 24 heures | Exploitation IT |
| Demande réglementaire | Dans les 24 heures | Juridique + RSSI |
| Incident de sécurité du sous-traitant | Dans les 24 heures | RSI |

**Notification renforcée pour les entités DORA/NIS2** :

- **Services couverts par DORA** : Dans les 2 heures pour les incidents critiques, inclure l'impact sur le risque de concentration
- **Services couverts par NIS2** : Dans les 4 heures pour l'interruption des services essentiels, permettre la notification réglementaire dans les 24 heures

> **Règle de priorité — Le délai le plus court s'applique :** Lorsque plusieurs délais de notification réglementaire s'appliquent simultanément au même incident, **le délai applicable le plus court prévaut**. Les fournisseurs doivent être opérationnellement capables de satisfaire à l'exigence la plus stricte pour leur classification de service.

## Contenu requis de la notification

**La notification initiale doit inclure (au minimum)** :

- Date et heure de découverte de l'incident
- Nature de l'incident (violation, interruption, compromission)
- Données/systèmes potentiellement affectés
- Nombre estimé d'enregistrements affectés (pour les violations de données)
- Actions de confinement initiales prises
- Contact désigné pour l'incident avec disponibilité 24/7
- Délai prévu pour les informations complémentaires

**La notification de suivi doit inclure** :

- Analyse des causes profondes (technique et procédurale)
- Évaluation complète de l'impact (données, systèmes, processus métier)
- Actions de remédiation prises avec preuves
- Mesures préventives mises en œuvre pour éviter la récurrence
- Chronologie détaillée des événements
- Recommandations pour les actions de [Organisation] le cas échéant

---

# Droits d'audit

## Droits d'audit par niveau

| Niveau du fournisseur | Droits d'audit requis |
|-----------------------|-----------------------|
| Niveau 1 | Droits d'audit complets (sur site ou à distance, annoncé ou non) |
| Niveau 2 | Droits d'audit ou acceptation de rapports tiers |
| Niveau 3 | Acceptation de rapports tiers |
| Niveau 4 | Non requis |

## Éléments de la clause de droit d'audit

**Pour les fournisseurs de Niveau 1 :**

| Élément | Exigence |
|---------|----------|
| Périmètre | Contrôles de sécurité, processus, installations, personnel, documentation |
| Fréquence | Annuelle au minimum, supplémentaire en cas d'incident, de changement important ou d'exigence réglementaire |
| Préavis | Préavis raisonnable (30 jours) pour les audits planifiés ; immédiat pour les audits causés |
| Auditeur | [Organisation] ou tiers désigné, auditeurs qualifiés |
| Coût | Fournisseur supporte les coûts pour les audits causés ; [Organisation] pour les audits de routine |
| Coopération | Accès au personnel, aux documents, aux systèmes, aux installations ; réponse rapide aux demandes |
| Constatations | Le fournisseur doit corriger dans le délai convenu (généralement 30-90 jours selon la gravité) |
| Rapport | Rapport d'audit fourni à [Organisation] dans les 30 jours suivant l'achèvement |
| Coopération réglementaire | Le fournisseur coopère aux audits réglementaires conformément à DORA art. 29 le cas échéant |

**Clause modèle pour le Niveau 1** :
> « [Organisation] aura le droit, après un préavis écrit de trente (30) jours (ou immédiatement en cas d'incident de sécurité ou d'exigence réglementaire), d'auditer les contrôles de sécurité, processus et installations du fournisseur liés aux services fournis. Le fournisseur assurera une coopération raisonnable et l'accès au personnel, à la documentation et aux systèmes. Les audits peuvent être effectués par [Organisation] ou ses auditeurs tiers désignés. »

## Acceptation des rapports tiers

Alternatives acceptables à un audit direct :

| Type de rapport | Validité | Exigence de périmètre | Notes |
|-----------------|----------|-----------------------|-------|
| SOC 2 Type II | 12 mois | Couvre les services fournis | Préféré pour les prestataires américains |
| Certificat ISO/IEC 27001 | Valide + surveillance | Le périmètre inclut les services concernés | Doit inclure les preuves d'audit de surveillance |
| Rapport de test d'intrusion | 12 mois | Couvre les systèmes concernés | Complément à la certification |
| Rapport d'évaluation des vulnérabilités | 6 mois | Couvre l'infrastructure concernée | Complément à la certification |
| Certification CSA STAR | Période de validité | Services en nuage | Spécifique au nuage |

---

# Exigences relatives aux sous-traitants

## Restrictions sur les sous-traitants

**Fournisseurs de Niveaux 1 et 2 :**

| Exigence | Description |
|----------|-------------|
| Approbation préalable | Approbation écrite avant l'engagement de sous-traitants avec accès aux données |
| Notification | Préavis de 30 jours pour les changements de sous-traitants pour revue |
| Transmission | Les exigences de sécurité doivent être transmises aux sous-traitants de manière identique |
| Responsabilité | Le fournisseur reste pleinement responsable des actes et omissions des sous-traitants |
| Registre | Maintenir la liste à jour des sous-traitants avec accès aux données |
| Droit d'opposition | [Organisation] peut s'opposer à des sous-traitants spécifiques dans les 14 jours |
| Droits d'audit | Les droits d'audit de [Organisation] s'étendent aux sous-traitants |
| Résiliation | Le sous-traitant doit être retiré si [Organisation] s'y oppose |

**Clause modèle** :
> « Le fournisseur ne fera appel à aucun sous-traitant pour accéder, traiter ou stocker les données de [Organisation] sans l'approbation écrite préalable de [Organisation]. Le fournisseur s'assurera que tout sous-traitant approuvé est lié par des obligations écrites offrant une protection au moins équivalente à celles du présent accord. Le fournisseur reste pleinement responsable des actes, omissions et défaillances de sécurité de ses sous-traitants. »

**Clause renforcée pour les services couverts par DORA** :
> « Pour les services TIC couverts par DORA, le fournisseur maintiendra un registre de tous les arrangements de sous-traitance en cascade et informera préalablement de toute sous-traitance en cascade prévue conformément à l'article 30 de DORA. [Organisation] se réserve le droit d'exiger la résiliation des arrangements de sous-traitance ne satisfaisant pas aux exigences de sécurité ou de risque de concentration. »

**Clause renforcée pour les institutions soumises à la FINMA (Circulaire 2023/1)** :
> « Pour les services externalisés soumis à la Circulaire FINMA 2023/1, le fournisseur maintiendra un registre de tous les arrangements de sous-externalisation en cascade et obtiendra l'approbation écrite préalable de [Organisation] avant toute sous-externalisation matérielle. [Organisation] conserve des droits d'audit sur les sous-externalisataires, exerçables directement ou via le fournisseur. »

---

# Exigences de continuité d'activité

## Exigences PCA par niveau

| Exigence | Niveau 1 | Niveau 2 | Niveaux 3-4 |
|----------|----------|----------|-------------|
| Plan PCA/PRA documenté | ✓ Requis | ✓ Requis | — |
| Test annuel PCA/PRA | ✓ Requis | ✓ Recommandé | — |
| Objectif de délai de reprise (RTO) | ✓ Défini dans SLA | ✓ Défini dans SLA | — |
| Objectif de point de reprise (RPO) | ✓ Défini dans SLA | ✓ Défini dans SLA | — |
| Redondance géographique | ✓ Basée sur les risques | — | — |
| Partage des résultats des tests | ✓ Sur demande | ✓ Sur demande | — |
| Notification de sinistre | ✓ Dans l'heure | ✓ Dans les 4 heures | — |

**Exigences renforcées DORA pour les prestataires TIC critiques** :

- Documentation de la stratégie de sortie avec plan de portabilité des données
- Identification d'un prestataire alternatif et faisabilité de changement
- Engagement d'assistance à la transition (minimum 6 mois)
- Atténuation du risque de concentration le cas échéant

## Exigences de niveau de service

**Éléments SLA pour les fournisseurs Critiques/Élevés :**

| Élément | Description |
|---------|-------------|
| Objectif de disponibilité | Engagement de disponibilité en pourcentage (ex. : 99,9 %, 99,95 %) |
| Période de mesure | Mesure mensuelle ou trimestrielle |
| Méthodologie de mesure | Comment la disponibilité est calculée, ce qui compte comme indisponibilité |
| Exclusions | Maintenance planifiée (avec préavis), force majeure |
| Crédits de service | Remèdes financiers en cas de non-respect du SLA |
| Processus d'escalade | Niveaux de notification et délais pour les services dégradés |
| Rapports | Rapports mensuels ou trimestriels avec résultats réels vs. objectifs |
| Restauration du service | Délai maximum de restauration après indisponibilité |

**Objectifs de disponibilité par criticité de service** :

- **Critique (Niveau 1)** : 99,95 % ou supérieur (max 4,38 heures d'indisponibilité/an)
- **Élevé (Niveau 2)** : 99,9 % (max 8,76 heures d'indisponibilité/an)
- **Moyen (Niveau 3)** : 99,5 % (max 43,8 heures d'indisponibilité/an)

---

# Retour et destruction des données

## Exigences de fin de contrat

| Exigence | Description |
|----------|-------------|
| Retour des données | Export complet dans un format utilisable et documenté |
| Format de retour | Standard sectoriel (CSV, JSON, XML) ou format natif de l'application |
| Délai de retour | Dans les 30 jours suivant la résiliation (ou plus court si critique) |
| Complétude du retour | Toutes les données, métadonnées, configurations, journaux d'audit |
| Assistance à la transition | Aide raisonnable pour la migration aux tarifs convenus |
| Destruction des données | Suppression sécurisée après confirmation de retour par [Organisation] |
| Méthode de destruction | DOD 5220.22-M, NIST SP 800-88 Rév. 2, ou effacement cryptographique |
| Certificat de destruction | Confirmation écrite de la destruction avec méthode et date |
| Exception de conservation | Uniquement si légalement requis, avec notification écrite et durée |
| Destruction des sauvegardes | Inclut toutes les copies de sauvegarde et de reprise après sinistre |

**Clause modèle** :
> « À la résiliation ou l'expiration du présent accord, le fournisseur devra, au choix de [Organisation], soit (a) restituer, soit (b) détruire de manière sécurisée toutes les données de [Organisation] dans les trente (30) jours. Pour la restitution des données, le fournisseur devra fournir les données dans [spécifier le format] et assister dans la migration. Pour la destruction des données, le fournisseur devra fournir une certification écrite de destruction utilisant des méthodes conformes à NIST SP 800-88 Rév. 2 ou équivalent. Le fournisseur ne conservera aucune copie sauf exigence légale, auquel cas il en informera [Organisation] par écrit. »

---

# Droits de résiliation

## Déclencheurs de résiliation

| Déclencheur | Délai de préavis | S'applique à |
|-------------|-----------------|--------------|
| Convenance | Selon contrat (généralement 30-90 jours) | Tous niveaux |
| Violation importante (non corrigée) | Immédiat après délai de correction (généralement 30 jours) | Tous niveaux |
| Incident de sécurité (important) | Immédiat | Niveaux 1-2 |
| Insolvabilité ou faillite | Immédiat | Tous niveaux |
| Changement de contrôle | 30 jours de préavis ou droit de résiliation immédiate | Niveaux 1-2 |
| Non-maintien des certifications | 30 jours pour corriger ou résiliation | Niveaux 1-2 |
| Exigence réglementaire | Selon la réglementation | Tous niveaux |
| Échecs SLA répétés | Après 3 mois consécutifs ou 6 mois sur 12 | Niveaux 1-2 |
| Violation de données par le fournisseur | Immédiat | Tous avec accès données |

## Assistance à la résiliation

**Les fournisseurs de Niveaux 1 et 2 doivent fournir :**

- Planification de la transition et soutien à la gestion de projet
- Documentation de transfert des connaissances et formation
- Assistance à la migration et à l'export des données
- Continuation du service pendant la période de transition (jusqu'à 6 mois pour le Niveau 1, 90 jours pour le Niveau 2)
- Remise complète de la documentation (configurations, procédures, identifiants)
- Coopération à l'intégration du fournisseur de remplacement

---

# Responsabilité et assurance

## Dispositions de responsabilité

| Disposition | Orientation |
|-------------|-------------|
| Plafond de responsabilité | À négocier selon les risques ; 12 fois les honoraires annuels minimum pour le Niveau 1 |
| Responsabilité illimitée | Violation de données, faute grave, actes intentionnels, violation de propriété intellectuelle |
| Indemnisation | Réclamations tierces résultant d'une violation des obligations de sécurité du fournisseur |
| Exclusions | L'exclusion des dommages consécutifs ne doit pas s'appliquer aux violations de données |
| Délai | Les réclamations doivent être déposées dans [X] ans suivant la découverte |

## Exigences d'assurance (Niveaux 1 et 2)

| Type d'assurance | Couverture minimale | Notes |
|------------------|---------------------|-------|
| Responsabilité cyber | 5 M€ minimum pour Niveau 1, 2 M€ pour Niveau 2 | Couverture première et tierce partie |
| Responsabilité professionnelle (E&O) | 5 M€ minimum pour Niveau 1, 2 M€ pour Niveau 2 | Couvrant les erreurs et omissions |
| Responsabilité civile générale | 2 M€ par sinistre | Couverture commerciale standard |
| Protection vie privée/RGPD | Inclus dans cyber ou 2 M€ séparé | Amendes RGPD et frais de défense |

---

# Registre des accords

Tous les accords fournisseurs doivent être suivis dans le système de gestion des contrats, notamment :

| Champ | Description |
|-------|-------------|
| Référence de l'accord | Identifiant unique dans le système de gestion des contrats |
| Nom du fournisseur | Raison sociale |
| Type d'accord | MSA, SLA, ATD, NDA, SOW |
| Date d'entrée en vigueur | Date de commencement |
| Date d'expiration | Date de fin ou de renouvellement |
| Renouvellement automatique | Oui/Non, délai de préavis requis pour éviter le renouvellement |
| Clauses de sécurité | Statut de conformité de la liste de contrôle par Section 3.1 |
| Date de revue | Date de dernière revue juridique/sécurité |
| Prochaine revue | Revue planifiée (annuelle ou avant renouvellement) |
| Localisation du document | Emplacement dans le référentiel ou référence du système de gestion documentaire |
| Responsable métier | Responsable de la relation interne |
| Statut d'approbation | Projet, En cours de revue, Approuvé, Signé |

---

# Exigences réglementaires spécifiques

## Prestataires de services TIC tiers DORA

Pour les fournisseurs proposant des services TIC soumis à DORA, les accords doivent inclure :

**Article 29 — Dispositions contractuelles clés** :

- Coopération totale avec les autorités compétentes (accès, inspection, droits d'audit)
- Droit d'émettre des instructions au prestataire de services TIC tiers
- Droit de résilier les arrangements si nécessaire
- Description claire des services fournis
- Lieux de prestation des services et de traitement des données
- Notification des changements affectant la performance du service
- Engagements de continuité et de reprise après sinistre
- Stratégies de sortie avec portabilité des données et assistance à la transition

**Article 30 — Sous-traitance en cascade** :

- Registre de tous les arrangements de sous-traitance en cascade
- Préavis de sous-traitance en cascade (30 jours minimum)
- Droit de s'opposer aux arrangements de sous-traitance
- Droits d'audit s'étendant aux sous-traitants

## Sécurité de la chaîne d'approvisionnement NIS2

Pour les fournisseurs d'entités couvertes par NIS2, les accords doivent traiter :

- Politiques et procédures de sécurité de la chaîne d'approvisionnement
- Documentation de l'évaluation de sécurité des fournisseurs
- Notification d'incident pour permettre le signalement réglementaire dans les 24 heures
- Participation à l'évaluation des risques de la chaîne d'approvisionnement

## Accords de traitement des données RGPD

Pour les fournisseurs traitant des données personnelles, l'accord de traitement des données (ATD) doit inclure :

**Exigences de l'Article 28** :

- Traitement uniquement sur instructions documentées
- Engagements de confidentialité du personnel
- Mesures de sécurité techniques et organisationnelles
- Exigences et processus d'approbation des sous-traitants ultérieurs
- Soutien aux droits des personnes concernées (accès, suppression, portabilité)
- Suppression ou retour à la fin des services
- Droits d'audit et d'inspection
- Assistance à la conformité réglementaire

**Clauses contractuelles types (CCT)** : Pour les fournisseurs non-UE/EEE, incorporer les CCT de la Commission de l'UE (Décision 2021/914) ou les équivalents approuvés suisses.

---

# Références

| Document | Relation |
|----------|----------|
| **ISMS-POL-A.5.19-23** | Cadre de politique parent |
| **ISMS-POL-A.5.19-23-S1** | Classification des fournisseurs (détermine les exigences des clauses) |
| **ISMS-POL-A.5.19-23-S3** | Sécurité de la chaîne d'approvisionnement (exigences sur les sous-traitants) |
| **ISMS-IMP-A.5.19-23.S2-UG/TG** | Cahier d'évaluation de la revue des contrats |
| **ISO/IEC 27036-2:2022** | Sécurité de l'information pour les relations fournisseurs — Exigences |

---

**Document suivant :** ISMS-POL-A.5.19-23-S3 — Sécurité de la chaîne d'approvisionnement TIC (Contrôle A.5.21)

---

*« Un contrat sans clauses de sécurité est une invitation à la violation. »*

<!-- QA_VERIFIED: 2026-03-30 -->
