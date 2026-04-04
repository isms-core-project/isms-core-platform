<!-- ISMS-CORE:POLICY:PRIV-POL-A.3.23-31-FR:privacy:POL:a.3.23-31 -->
**PRIV-POL-A.3.23-31 — Contrôles techniques de sécurité pour les DCP**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Contrôles techniques de sécurité pour les DCP |
| **Type de document** | Politique |
| **Identifiant du document** | PRIV-POL-A.3.23-31 |
| **Auteur du document** | Délégué à la Protection des Données (DPD) |
| **Propriétaire du document** | Directeur Général (DG) |
| **Approuvé par** | Direction générale |
| **Date de création** | [Date] |
| **Version** | 1.0 |
| **Classification** | Interne |
| **Statut** | Brouillon |
| **Version du produit Privacy** | 1.0 |

**Historique des versions** :

| Version | Date | Auteur | Modifications |
|---------|------|--------|---------------|
| 1.0 | [Date] | DPD | Politique initiale pour la première certification ISO/IEC 27701:2025 |

**Cycle de révision** : Annuel | **Prochaine date de révision** : [Date d'entrée en vigueur + 12 mois]

**Chaîne d'approbation** : Principale: DPD; Secondaire: RSSI; Technique: Responsable du Développement / Architecture IT; Autorité finale: Direction générale.

**Documents connexes** :
- PRIV-POL-00 / PRIV-POL-01; PRIV-IMP-A.3.23-31-UG / TG
- ISMS-POL-A.8.2, A.8.5, A.8.13, A.8.15-16, A.8.24, A.8.25-31 (parallèles SGSI)
- ISO/IEC 27701:2025 Contrôles A.3.23 à A.3.31
- RGPD Article 25 (Protection des données dès la conception) ; Article 32 (Sécurité du traitement)
- LPD suisse Article 7 (Mesures techniques proportionnées au risque)

**Applicabilité du rôle** : Cette politique s'applique à l'organisation agissant à la fois comme **Responsable du traitement et comme Sous-traitant des DCP**. Les contrôles A.3.23–A.3.31 sont des contrôles partagés (Tableau A.3).

---

## Résumé exécutif

Cette politique établit les exigences de [Organisation] pour les contrôles de sécurité techniques appliqués au traitement des DCP, couvrant l'authentification, la sauvegarde, la journalisation, la cryptographie, le développement sécurisé, la sécurité des applications, l'architecture des systèmes, le développement externalisé et les informations de test — conformément aux contrôles A.3.23 à A.3.31 d'ISO/IEC 27701:2025.

**Périmètre** : Tous les contrôles techniques mis en œuvre pour les systèmes, applications et infrastructures traitant des DCP ; toutes les activités de développement de logiciels et systèmes impliquant le traitement des DCP ; tous les environnements de test utilisant ou simulant des DCP.

**Justification** : A.3.23–A.3.31 constituent la couche d'assurance technique pour le traitement des DCP. Ils étendent et spécialisent le cadre de contrôles techniques SGSI pour les contextes DCP — garantissant que chaque domaine technique (authentification, sauvegarde, journalisation, cryptographie, développement, architecture, externalisation, test) traite explicitement des DCP. Le RGPD Articles 25 et 32 fournissent la base réglementaire pour ce groupe.

---

# Périmètre et applicabilité

## Énoncés des contrôles ISO/IEC 27701:2025

**A.3.23 — Authentification sécurisée** : [Organisation] DOIT mettre en œuvre des technologies et procédures d'authentification sécurisée pour les systèmes de traitement des DCP, calibrées aux restrictions d'accès applicables.

**A.3.24 — Sauvegarde des informations** : [Organisation] DOIT maintenir des copies de sauvegarde des DCP et des logiciels/systèmes impliqués dans leur traitement, et les tester régulièrement.

**A.3.25 — Journalisation** : [Organisation] DOIT produire, stocker, protéger et analyser des journaux capturant les activités, exceptions, pannes et autres événements liés au traitement des DCP.

**A.3.26 — Utilisation de la cryptographie** : [Organisation] DOIT définir et mettre en œuvre des règles pour l'utilisation efficace de la cryptographie dans les contextes de traitement des DCP, incluant la gestion des clés.

**A.3.27 — Cycle de vie de développement sécurisé** : [Organisation] DOIT établir et appliquer des règles pour le développement sécurisé des logiciels et systèmes impliqués dans le traitement des DCP.

**A.3.28 — Exigences de sécurité des applications** : [Organisation] DOIT identifier, spécifier et approuver les exigences de sécurité liées au traitement des DCP lors du développement ou de l'acquisition d'applications.

**A.3.29 — Principes d'architecture et d'ingénierie des systèmes sécurisés** : [Organisation] DOIT établir, documenter, maintenir et appliquer des principes d'ingénierie des systèmes sécurisés dans le contexte du traitement des DCP.

**A.3.30 — Développement externalisé** : [Organisation] DOIT diriger, surveiller et examiner les activités liées au développement externalisé de systèmes utilisés pour le traitement des DCP.

**A.3.31 — Informations de test** : [Organisation] DOIT sélectionner, protéger et gérer de manière appropriée les informations de test utilisées dans le contexte des systèmes de traitement des DCP.

## Cadre réglementaire

**Obligatoire (Niveau 1)** (per PRIV-POL-00) :
- **RGPD UE** : Article 25 (protection des données dès la conception et par défaut — contrôles techniques comme exigence de conception) ; Article 32 (pseudonymisation, chiffrement, restauration de la disponibilité, test régulier des MTO)
- **LPD suisse** : Article 7 (mesures techniques proportionnées au risque)
- **ISO/IEC 27701:2025** : Contrôles A.3.23–A.3.31 (normatifs)

---

# A.3.23 — Authentification sécurisée pour le traitement des DCP

[Organisation] DOIT mettre en œuvre des technologies et procédures d'authentification sécurisée pour l'accès aux systèmes de traitement des DCP.

### Exigences d'authentification pour les systèmes DCP

| Sensibilité des DCP | Exigence d'authentification minimale |
|--------------------|--------------------------------------|
| DCP CONFIDENTIELS | Authentification multi-facteurs (AMF) pour l'accès distant ; politique de mot de passe fort pour l'accès interne |
| DCP RESTREINTS (catégorie spéciale) | AMF requise pour TOUT accès (interne et distant) |
| Accès administratif / privilégié aux DCP | AMF requise ; identifiant privilégié distinct de l'identité standard |

Les procédures d'authentification DOIVENT appliquer les restrictions d'accès alignées aux droits d'accès définis dans PRIV-POL-A.3.8-10. Les tentatives d'authentification échouées DOIVENT être journalisées et déclencher un verrouillage per les seuils définis dans PRIV-IMP-A.3.23-31-TG. Les identifiants d'authentification pour les systèmes DCP DOIVENT être uniques par individu ; les identifiants partagés sont interdits.

---

# A.3.24 — Sauvegarde des DCP et systèmes connexes

[Organisation] DOIT maintenir des copies de sauvegarde des DCP et des logiciels/systèmes connexes, et tester régulièrement l'intégrité et la restorabilité de ces sauvegardes.

- Toutes les DCP traitées DOIVENT être couvertes par un régime de sauvegarde avec des objectifs de point de récupération (RPO) documentés
- Les sauvegardes contenant des DCP DOIVENT être soumises aux mêmes contrôles de classification et d'accès que les DCP primaires
- Les copies de sauvegarde DOIVENT être chiffrées avec le même standard que les données primaires
- Les sauvegardes hors site ou cloud DOIVENT être soumises à des contrôles de sécurité équivalents, incluant chiffrement en transit et au repos
- La restauration des sauvegardes DOIT être testée au minimum annuellement ; les résultats DOIVENT être documentés ; les échecs de test impliquant des DCP DOIVENT être escaladés au RSSI et au DPD

---

# A.3.25 — Journalisation pour le traitement des DCP

[Organisation] DOIT produire, stocker, protéger et analyser des journaux enregistrant les activités, exceptions, pannes et autres événements liés au traitement des DCP.

### Événements DCP devant être journalisés

- Accès aux entrepôts de DCP (lecture, écriture, export) par des utilisateurs authentifiés
- Tentatives d'accès échouées aux systèmes DCP
- Opérations de données en masse impliquant des DCP (export, suppression, pseudonymisation, anonymisation)
- Modifications des droits d'accès aux systèmes DCP
- Opérations privilégiées sur les systèmes de traitement des DCP
- Opérations de satisfaction des droits des personnes concernées
- Erreurs ou exceptions système dans les composants de traitement des DCP

### Protection des journaux

Les journaux DOIVENT être : protégés contre la modification et la suppression (stockage à l'épreuve des altérations) ; classifiés au minimum CONFIDENTIEL ; accessibles uniquement aux personnels autorisés ; conservés pendant **minimum 12 mois** comme plancher opérationnel, avec un **minimum de 3 ans** pour les journaux pouvant être requis comme preuves de responsabilité RGPD (journaux d'accès pour la satisfaction des droits, opérations de suppression et d'anonymisation en masse, accès privilégié aux systèmes DCP). Le RSSI et le DPD DOIVENT convenir de périodes de conservation spécifiques par catégorie de journal dans PRIV-IMP-A.3.23-31-TG.

Les journaux DOIVENT être examinés sur la base d'exceptions (alertes pour les modèles d'accès DCP anormaux), dans le cadre de la revue de conformité périodique, en réponse à un incident de protection des données, et dans le cadre de la revue des droits d'accès.

---

# A.3.26 — Cryptographie pour le traitement des DCP

[Organisation] DOIT définir et mettre en œuvre des règles pour l'utilisation efficace de la cryptographie dans les contextes de traitement des DCP, incluant la gestion des clés cryptographiques.

- **Chiffrement au repos** : Toutes les DCP CONFIDENTIELLES et RESTREINTES DOIVENT être chiffrées au repos avec un algorithme approuvé (minimum AES-256 ou équivalent per ISMS-POL-A.8.24)
- **Chiffrement en transit** : Toutes les DCP transmises sur des réseaux DOIVENT être chiffrées en transit avec les normes TLS actuelles (minimum TLS 1.2 ; TLS 1.3 préféré)
- **Pseudonymisation** : Lorsque les DCP sont utilisées pour des analyses, des tests, des recherches ou des finalités secondaires, la pseudonymisation DOIT être appliquée pour réduire le risque de réidentification lorsque techniquement faisable
- **Anonymisation** : Lorsqu'une anonymisation irréversible est appliquée, le résultat n'est plus des DCP — mais l'anonymisation doit être robuste. Le DPD DOIT confirmer, selon une méthodologie documentée, que la réidentification n'est pas raisonnablement possible par tout moyen raisonnablement susceptible d'être utilisé, en considérant les risques de singularisation (isoler un individu dans un jeu de données), de liaison (lier des enregistrements pour identifier un individu) et d'inférence (déduire des attributs d'un individu). Une anonymisation ne résistant pas à cette évaluation DOIT être traitée comme une pseudonymisation, et les données sous-jacentes restent des DCP

### Gestion des clés

Les clés cryptographiques protégeant les DCP DOIVENT être gérées séparément des DCP qu'elles protègent ; l'accès aux clés DOIT être restreint ; la rotation des clés DOIT avoir lieu aux intervalles définis dans PRIV-IMP-A.3.23-31-TG ; la compromission ou la perte de clés protégeant des DCP DOIT être traitée comme un incident DCP per PRIV-POL-A.3.11-12.

---

# A.3.27 — Cycle de vie de développement sécurisé pour les systèmes DCP

[Organisation] DOIT établir et appliquer des règles pour le développement sécurisé des logiciels et systèmes liés au traitement des DCP.

- **Protection des données dès la conception** : Les exigences de confidentialité et de protection des DCP DOIVENT être prises en compte dès la première étape de conception de tout système destiné à traiter des DCP ; la correction de contrôles de confidentialité a posteriori n'est pas une approche acceptable
- **Protection des données par défaut** : Les paramètres par défaut des systèmes DOIVENT minimiser la collecte et le traitement des DCP ; les paramètres les plus protecteurs DOIVENT être les paramètres par défaut
- **Minimisation des DCP dans la conception** : Les systèmes DOIVENT être conçus pour collecter et traiter uniquement les DCP minimum nécessaires pour la finalité déclarée ; la collecte de champs en excès DOIT être identifiée et supprimée lors de la revue de conception
- **Séparation des DCP** : Lorsque techniquement faisable, les DCP DOIVENT être isolées des données non-DCP dans la conception du système

### Conformité RGPD Article 25

Les systèmes impliquant le traitement des DCP DOIVENT être documentés comme conformes à la protection des données dès la conception avant le déploiement en production. Le processus AIPD (PRIV-POL-A.1.2.6-9) DOIT être déclenché pour les systèmes de traitement à haut risque pendant la phase de conception, pas après le déploiement.

---

# A.3.28 — Exigences de sécurité des applications pour les DCP

[Organisation] DOIT identifier, spécifier et approuver les exigences de sécurité liées au traitement des DCP lors du développement ou de l'acquisition d'applications.

- Les exigences de sécurité DCP DOIVENT être documentées avant le début du développement ou de l'acquisition
- Les exigences DOIVENT couvrir au minimum : authentification, contrôle d'accès, chiffrement au repos et en transit, journalisation, conservation/suppression des données
- Les exigences DOIVENT être approuvées par le DPD (exigences de confidentialité) et le RSSI (exigences de sécurité) avant le début
- Pour les applications acquises : les exigences de sécurité DOIVENT être incluses dans les spécifications d'achat ; l'évaluation de sécurité du fournisseur DOIT aborder les contrôles de traitement des DCP

---

# A.3.29 — Principes d'architecture et d'ingénierie sécurisées pour les DCP

[Organisation] DOIT établir, documenter, maintenir et appliquer des principes d'ingénierie des systèmes sécurisés en lien avec le traitement des DCP.

Les principes d'architecture suivants DOIVENT être appliqués aux systèmes impliquant des DCP :

1. **Exposition minimale** : Les DCP ne DOIVENT transiter que par le minimum de composants système nécessaires ; l'exposition inutile à des systèmes intermédiaires ou journaux DOIT être évitée
2. **Moindre privilège dans l'architecture** : Les composants système n'accèdent qu'aux DCP dont ils ont besoin ; l'accès de service à service aux DCP DOIT être limité et authentifié
3. **Ségrégation des données** : Lorsque faisable, les DCP de différentes finalités DOIVENT être logiquement séparées
4. **Auditabilité** : Les systèmes traitant des DCP DOIVENT être conçus pour produire les journaux requis par A.3.25 sans instrumentation supplémentaire
5. **Restorabilité** : L'architecture DOIT supporter les exigences de sauvegarde et de récupération de A.3.24 pour les DCP
6. **Chemins d'anonymisation et de pseudonymisation** : L'architecture DOIT inclure des mécanismes techniques pour pseudonymiser ou anonymiser les DCP pour les cas d'usage secondaires sans nécessiter l'accès aux entrepôts DCP primaires

---

# A.3.30 — Développement externalisé de systèmes de traitement des DCP

[Organisation] DOIT diriger, surveiller et examiner les activités liées au développement externalisé de systèmes de traitement des DCP.

- Le partenaire de développement DOIT être traité comme un sous-traitant de DCP ou fournisseur adjacent per PRIV-POL-A.3.8-10
- Un accord couvrant les obligations de sécurité DCP DOIT être en place avant l'accès au développement aux DCP
- Les exigences de sécurité DCP (A.3.28) DOIVENT être communiquées et convenues avant le début du développement
- [Organisation] DOIT conserver le droit d'examiner les artefacts de développement (code, documents de conception) pour la conformité DCP
- Le partenaire de développement NE DOIT PAS utiliser de vraies DCP dans des environnements de développement ou de test sans approbation explicite du DPD

---

# A.3.31 — Informations de test pour les DCP

[Organisation] DOIT sélectionner, protéger et gérer de manière appropriée les informations de test liées au traitement des DCP.

### Interdiction des vraies DCP dans les environnements de test

Les vraies DCP NE DOIVENT PAS être utilisées dans les environnements de test comme pratique par défaut. Les environnements de test DOIVENT utiliser : des données générées synthétiquement ressemblant aux DCP en structure mais sans données personnelles réelles, OU des données irréversiblement anonymisées à partir de jeux de données DCP réels (confirmation d'anonymisation du DPD requise).

### Exception : utilisation de vraies DCP dans les tests

Lorsque l'utilisation de vraies DCP dans les tests est opérationnellement nécessaire : approbation écrite du DPD requise avant la copie dans l'environnement de test ; périmètre limité au minimum de DCP nécessaire, pour la durée minimale requise ; les vraies DCP DOIVENT être supprimées de l'environnement de test immédiatement après la conclusion du test spécifique, avec confirmation et documentation ; tout accès aux vraies DCP dans l'environnement de test DOIT être journalisé.

---

# Rôles et responsabilités

| Rôle | Responsabilités pour A.3.23–A.3.31 |
|------|-------------------------------------|
| **DPD** | Approuve les exigences de sécurité DCP pour les nouveaux systèmes (A.3.28) ; confirme les décisions d'anonymisation (A.3.26) ; approuve les AIPD pour les nouveaux systèmes DCP (A.3.27) ; approuve l'utilisation de vraies DCP dans les tests (A.3.31) ; examine la conformité DCP du développement externalisé (A.3.30) |
| **RSSI** | Définit les normes d'authentification (A.3.23) ; définit les normes de sauvegarde (A.3.24) ; gère l'infrastructure de journalisation (A.3.25) ; maintient les normes cryptographiques (A.3.26) ; est propriétaire du cadre de développement sécurisé (A.3.27–A.3.30) |
| **Équipe Sécurité IT** | Met en œuvre l'authentification, la sauvegarde, la journalisation et le chiffrement ; surveille les journaux pour les anomalies d'accès DCP ; gère l'infrastructure de gestion des clés |
| **Équipes Développement / DevOps** | Applique les règles de protection des données dès la conception et de développement sécurisé ; met en œuvre les exigences de sécurité DCP ; utilise uniquement des données de test approuvées |
| **Architecture IT** | Maintient les principes d'architecture sécurisée pour les DCP ; examine les nouvelles conceptions de systèmes |
| **Achats / Juridique** | Veille à ce que les contrats de développement externalisé incluent les obligations de sécurité DCP |

---

# Exigences en matière de preuves

| Preuve | Description | Conservation |
|-------|-------------|-------------|
| Configuration d'authentification des systèmes DCP | Enregistrements d'application AMF et configurations de restriction d'accès | En cours + 3 ans |
| Enregistrements de test de sauvegarde | Résultats de test de restauration annuels pour les sauvegardes DCP | 3 ans |
| Journaux d'accès DCP | Journaux d'activité pour l'accès aux entrepôts DCP et systèmes | Minimum 12 mois ; plus long selon exigences réglementaires ou contractuelles |
| Documentation des normes cryptographiques | Algorithmes approuvés, procédures de gestion des clés, enregistrements de rotation | En cours + 3 ans |
| Évaluations Privacy by Design | Enregistrements de revue de conception confirmant la conformité PbD | Durée de fonctionnement du système + 3 ans |
| Documents d'exigences de sécurité DCP | Exigences approuvées pour les applications DCP développées ou acquises | Durée de fonctionnement de l'application + 3 ans |
| Enregistrements d'approbation de test avec vraies DCP | Approbations DPD pour l'utilisation de vraies DCP dans les tests, avec confirmations de suppression | 3 ans |
| Accords de développement externalisé DCP | Accords avec les partenaires de développement couvrant les obligations de sécurité DCP | Durée de l'accord + 3 ans |

---

# Considérations d'audit

**A.3.23 (Authentification)** : Preuves de configuration AMF pour les systèmes DCP CONFIDENTIELS/RESTREINTS ; alignement des restrictions d'accès ; journalisation des connexions échouées.

**A.3.24 (Sauvegarde)** : Politique de sauvegarde couvrant les DCP ; chiffrement des sauvegardes ; enregistrements de test de restauration annuels.

**A.3.25 (Journalisation)** : Événements DCP définis journalisés ; stockage à l'épreuve des altérations ; contrôles d'accès sur les journaux ; preuves d'analyse des journaux.

**A.3.26 (Cryptographie)** : Chiffrement au repos pour les DCP CONFIDENTIELS/RESTREINTS ; application de TLS en transit ; documentation de gestion des clés ; preuves d'utilisation de la pseudonymisation.

**A.3.27 (Développement sécurisé)** : Preuves de protection des données dès la conception dans les enregistrements de conception système ; déclenchement AIPD pour les systèmes à haut risque ; revue de minimisation des données dans la conception.

**A.3.28 (Exigences des applications)** : Exigences de sécurité DCP documentées et approuvées DPD/RSSI ; exigences de sécurité dans les spécifications d'acquisition.

**A.3.29 (Principes d'architecture)** : Principes d'architecture DCP documentés ; preuves de revue de conception appliquant les principes aux nouveaux systèmes.

**A.3.30 (Développement externalisé)** : Accords de développement externalisé avec clauses de sécurité DCP ; aucune vraie DCP dans les environnements de développement externalisé sans approbation DPD.

**A.3.31 (Informations de test)** : Utilisation par défaut de données de test synthétiques ou anonymisées ; enregistrements d'approbation DPD pour toute utilisation de vraies DCP dans les tests ; confirmations de suppression des vraies DCP après les tests.

---

<!-- QA_VERIFIED: 2026-04-03 -->
