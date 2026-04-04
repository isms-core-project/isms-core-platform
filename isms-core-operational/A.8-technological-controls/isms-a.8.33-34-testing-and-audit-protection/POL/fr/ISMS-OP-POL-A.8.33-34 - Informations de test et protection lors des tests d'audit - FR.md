<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.8.33-34-FR:operational:OP-POL:a.8.33-34 -->
**ISMS-OP-POL-A.8.33-34 — Informations de test et protection lors des tests d'audit**

---

**Contrôle documentaire**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Informations de test et protection lors des tests d'audit |
| **Type de document** | Politique opérationnelle |
| **Identifiant du document** | ISMS-OP-POL-A.8.33-34 |
| **Créateur du document** | Responsable de la sécurité de l'information (RSSI) |
| **Propriétaire du document** | Directeur général (PDG) |
| **Approuvé par** | Direction générale |
| **Date de création** | [Date] |
| **Version** | 1.0 |
| **Date de version** | [À déterminer] |
| **Classification** | Usage interne |
| **Statut** | Brouillon |

**Historique des versions** :

| Version | Date | Auteur | Modifications |
|---------|------|--------|---------------|
| 1.0 | [Date] | RSSI | Politique opérationnelle initiale pour ISO 27001:2022 |

**Cycle de révision** : Annuel
**Prochaine révision** : [Date d'entrée en vigueur + 12 mois]

**Approuvé par** : [RSSI / Direction générale]

**Documents connexes** :

- ISO/IEC 27001:2022 Contrôle A.8.33 — Informations de test
- ISO/IEC 27001:2022 Contrôle A.8.34 — Protection des systèmes d'information lors des tests d'audit
- ISO/IEC 27002:2022 Sections 8.33 et 8.34 — Recommandations de mise en œuvre
- NIST SP 800-53 Rév. 5 — SA-11 (Tests et évaluation par les développeurs), CA-8 (Tests d'intrusion), AU-11 (Conservation des enregistrements d'audit)
- CIS Controls v8 — Mesure 3.1–3.14 (Protection des données), Mesure 18.1–18.5 (Tests d'intrusion)

**Contrôles Annexe A connexes** :

| Contrôle | Relation avec les informations de test et la protection lors des audits |
|----------|-------------------------------------------------------------------------|
| A.5.9 Inventaire des informations et autres actifs associés | Les environnements de test et les outils d'audit sont inclus dans l'inventaire des actifs |
| A.5.15–16–18 Gestion des identités et des accès | Provisionnement des accès pour les auditeurs et les testeurs ; contrôles d'accès limités dans le temps |
| A.5.24–28 Cycle de gestion des incidents | Gestion des incidents lors des tests d'audit ; escalade des découvertes de vulnérabilités |
| A.5.34 Vie privée et DCP | Protection des DCP dans les données de test ; exigences d'anonymisation et de pseudonymisation |
| A.8.2–3–5 Authentification et accès privilégié | Exigences d'AMF pour l'accès aux environnements de test ; authentification des auditeurs |
| A.8.8 Gestion des vulnérabilités | Traitement des vulnérabilités détectées lors des tests d'intrusion et des audits |
| A.8.11 Masquage des données | Techniques de masquage appliquées aux données de production utilisées pour les tests |
| A.8.15 Journalisation | Piste d'audit pour le traitement des données de test et les activités d'accès des auditeurs |
| A.8.16 Surveillance | Surveillance en temps réel lors des audits actifs et des tests d'intrusion |
| A.8.31 Séparation des environnements | Isolation des environnements pour la protection des données de test |

**Politiques internes connexes** :

- Politique de gestion des identités et des accès
- Politique de masquage des données
- Politique de journalisation
- Politique des activités de surveillance (A.8.16)
- Politique de gestion des vulnérabilités
- Politique de gestion des incidents
- Politique de classification et de traitement des données
- Politique de séparation des environnements

---

# Politique sur les informations de test et la protection lors des tests d'audit

## Objectif

La présente politique a pour objectif de garantir que les informations de test sont sélectionnées, protégées et gérées de manière appropriée, et que les tests d'audit ainsi que les autres activités d'assurance impliquant l'évaluation de systèmes en production sont planifiés et convenus afin de minimiser les perturbations tout en maintenant l'intégrité des systèmes.

Cette politique traite deux préoccupations complémentaires : protéger les données sensibles contre toute exposition via les environnements de test (A.8.33), et protéger les systèmes en production contre tout impact non intentionnel lors des tests d'audit et de sécurité (A.8.34).

Cette politique soutient la nLPD suisse (revLPD) en son art. 8, en mettant en œuvre des mesures techniques et organisationnelles proportionnées au risque pour protéger les données personnelles utilisées dans ou exposées via les environnements de test. Lorsque l'organisation traite des données de personnes résidant dans l'UE/EEE, les exigences de l'art. 25 du RGPD (protection des données dès la conception et par défaut) et de l'art. 32 (sécurité du traitement) s'appliquent également. La gestion des données de test est une mesure technique clé pour démontrer que les données personnelles ne sont pas inutilement exposées via des environnements hors production.

## Champ d'application

La présente politique s'applique à toutes les activités de sélection, de création, de protection et d'élimination des données de test, ainsi qu'à toutes les activités d'audit, de tests d'intrusion et d'assurance impliquant l'évaluation de systèmes en production.

Cela inclut :

- Toutes les données de test utilisées dans les environnements de développement, AQ, staging, UAT, formation, sandbox et démonstration.
- Toutes les copies, extraits ou dérivés de données de production utilisés à des fins de test.
- Tous les jeux de données de test synthétiques, anonymisés, pseudonymisés et masqués.
- Tous les audits et évaluations de sécurité internes.
- Tous les audits de certification externes (ISO 27001 et équivalents).
- Tous les tests d'intrusion, évaluations de vulnérabilités et tests de sécurité actifs.
- Toutes les évaluations de sécurité par des tiers et les audits de conformité réglementaire.
- Tout le personnel impliqué dans les activités de test, d'audit ou d'assurance, y compris les employés, les sous-traitants, les auditeurs internes, les auditeurs externes et les testeurs d'intrusion.

**Hors champ d'application** : Opérations de l'environnement de production (couvertes par les politiques opérationnelles) ; surveillance automatisée de routine (couverte par A.8.16) ; spécifications des techniques de masquage des données et configuration des outils (couvertes par A.8.11) ; architecture et exigences de séparation des environnements (couvertes par A.8.31) ; pratiques de codage sécurisé et de test de développement (couvertes par A.8.25–26–29).

## Principe

Les données de test doivent être traitées comme un vecteur potentiel de violation des données. La position par défaut est que les données de production contenant des données personnelles, des informations sensibles ou des données métier confidentielles ne doivent pas être utilisées dans les environnements de test. Lorsque des données dérivées de la production sont nécessaires, elles doivent être anonymisées, pseudonymisées ou masquées avant utilisation.

Les activités d'audit et d'assurance doivent être conduites avec l'accès et l'impact minimaux nécessaires pour atteindre leurs objectifs. Les auditeurs doivent recevoir un accès en lecture seule par défaut, les tests doivent être limités dans le temps et la portée, et les systèmes en production doivent être protégés contre toute perturbation non intentionnelle.

---

## Sélection des données de test

L'organisation doit établir une hiérarchie claire de préférence pour les sources de données de test.

**Hiérarchie des sources de données de test** (par ordre de préférence) :

| Priorité | Source de données | Description | Approbation requise |
|----------|-------------------|-------------|---------------------|
| 1 | **Données synthétiques** | Données générées artificiellement sans relation avec des personnes réelles ou des enregistrements métier | Responsable du développement |
| 2 | **Données anonymisées** | Données de production dé-identifiées de manière irréversible pour lesquelles la ré-identification n'est pas raisonnablement possible | Responsable de la sécurité de l'information |
| 3 | **Données pseudonymisées** | Données de production dont les identifiants sont remplacés par des pseudonymes ; ré-identifiables avec une clé séparée | Responsable de la sécurité de l'information + Propriétaire des données |
| 4 | **Données de production masquées** | Données de production dont les champs sensibles sont obscurcis à l'aide de techniques de masquage approuvées | RSSI + Propriétaire des données |
| 5 | **Copie directe de la production** | Données de production non modifiées (circonstances exceptionnelles uniquement) | RSSI + DPD + Propriétaire des données |

Les copies directes de production ne sont autorisées que lorsque toutes les autres options sont manifestement insuffisantes, avec une justification documentée, une approbation limitée dans le temps (maximum 30 jours), des contrôles d'accès renforcés et une suppression obligatoire à l'achèvement.

**Arbre de décision pour la source de données de test** :

Pour déterminer la source de données de test appropriée, appliquer la logique de décision suivante :

```
Le test requiert-il des caractéristiques de données réelles (distributions, cas limites) ?
+-- NON --> Utiliser des données synthétiques (Priorité 1)
+-- OUI
    +-- Peut-on générer des données synthétiques avec ces caractéristiques ?
        +-- OUI --> Utiliser des données synthétiques (Priorité 1)
        +-- NON
            +-- S'agit-il de données personnelles au sens de la nLPD/RGPD ?
                +-- NON --> Utiliser des données de production masquées (Priorité 4)
                +-- OUI
                    +-- La ré-identification peut-elle être rendue impossible ?
                        +-- OUI --> Utiliser des données anonymisées (Priorité 2)
                        +-- NON --> Utiliser des données pseudonymisées (Priorité 3)
                            (Requiert l'approbation du Responsable de la sécurité de l'information + Propriétaire des données)
```

Lorsqu'une décision aboutit à la priorité 3 ou plus, le Propriétaire des données et le Responsable de la sécurité de l'information doivent être consultés avant de procéder.

**Classification des données de test** : Les données de test doivent être classifiées selon le schéma de classification des données de l'organisation. Les données de test dérivées de la production héritent de la classification des données sources jusqu'à ce que le masquage ou l'anonymisation soit validé. Les données synthétiques sont classifiées selon le contexte métier (généralement Usage interne). La classification détermine les contrôles de protection requis.

---

## Protection des données de test

### Anonymisation et pseudonymisation

Lorsque des données de production sont nécessaires pour les tests, l'organisation doit appliquer des techniques de protection des données avant que celles-ci ne soient accessibles dans tout environnement de test.

**Exigences d'anonymisation** :

- L'anonymisation doit rendre la ré-identification non raisonnablement possible, en tenant compte des moyens de ré-identification disponibles, du coût de la ré-identification et de l'objectif visé.
- Les données anonymisées ne constituent plus des données personnelles au sens de la nLPD ou du RGPD et peuvent être classifiées à un niveau inférieur avec l'approbation du Propriétaire des données.
- Les techniques d'anonymisation doivent être validées avant utilisation et révisées annuellement pour vérifier leur efficacité continue, en tenant compte des avancées en matière de techniques de ré-identification, y compris les méthodes assistées par l'IA.

**Exigences de pseudonymisation** :

- Les données pseudonymisées restent des données personnelles et doivent être protégées en conséquence.
- La clé de correspondance (pseudonyme-identité) doit être stockée séparément du jeu de données pseudonymisé, avec un accès limité au personnel autorisé.
- Les données de test pseudonymisées doivent être soumises aux mêmes contrôles d'accès que la classification des données d'origine.

### Masquage des données

Le masquage des données doit être appliqué à l'aide de [Outil de masquage des données] (ex. : Informatica, Delphix, IBM InfoSphere Optim ou équivalent) ou de méthodes scriptées approuvées.

**Exigences de masquage** :

| Type de données | Technique de masquage | Validation |
|-----------------|----------------------|------------|
| Noms de personnes | Substitution par des noms synthétiques | Vérifier qu'aucun nom d'origine ne subsiste |
| Adresses e-mail | Remplacement du domaine (ex. : @example.com) | Vérifier que le format est préservé, aucune adresse réelle |
| Identifiants nationaux (AVS/NAS) | Randomisation préservant le format | Vérifier que le format est valide mais inexistant |
| Données financières (IBAN, numéros de compte) | Chiffrement ou randomisation préservant le format | Vérifier que le format est préservé, intégrité référentielle maintenue |
| Dates de naissance | Décalage de dates (offset cohérent par enregistrement) | Vérifier que les distributions d'âge sont préservées pour les tests |
| Champs de texte libre | Rédaction ou remplacement synthétique | Vérifier l'absence de fuite de DCP dans le texte non structuré |
| Adresses | Substitution par des adresses synthétiques | Vérifier que la distribution géographique est préservée si nécessaire |

**Référence rapide pour le masquage des données** :

Le tableau suivant fournit une référence rapide pour les types de données courants et les approches de masquage recommandées :

| Type de données | Technique recommandée | Exemple d'outil/méthode |
|-----------------|----------------------|-------------------------|
| Noms | Substitution | Bibliothèque Faker : `fake.name()` (locale suisse) |
| E-mails | Échange de domaine | `utilisateur123@domainetest.example` |
| Numéros de téléphone | Randomisation préservant le format | Bibliothèque Faker : `fake.phone_number()` |
| Dates | Offset cohérent | Toutes les dates décalées d'un aléatoire +/- 1–3 ans |
| Adresses | Substitution | Bibliothèque Faker : `fake.address()` (locale suisse) |
| Texte libre | Rédaction ou NER + remplacement | Service NLP cloud + logique de remplacement personnalisée |
| Valeurs financières | Chiffrement préservant le format | Algorithme FPE avec gestion approuvée des clés |

**Validation du masquage** : Les données masquées doivent être validées avant leur diffusion dans les environnements de test afin de confirmer que les valeurs sensibles d'origine ne sont pas récupérables, que le format des données est préservé pour la compatibilité applicative, que l'intégrité référentielle est maintenue entre les jeux de données liés, et qu'il n'existe aucune donnée personnelle en clair dans la sortie masquée. Les résultats de validation doivent être documentés et approuvés par le Responsable de la sécurité de l'information.

### Génération de données synthétiques

Lorsque des données synthétiques sont utilisées, elles doivent être générées de manière à préserver les propriétés statistiques, les distributions de données et l'intégrité référentielle nécessaires à des tests efficaces, sans contenir aucune donnée personnelle ou métier réelle.

Les générateurs de données synthétiques doivent être documentés, versionnés et révisés périodiquement pour s'assurer que les données générées restent adaptées à l'usage. L'organisation doit conserver des enregistrements des paramètres de génération des données synthétiques et des résultats de validation.

---

## Cycle de vie des données de test

### Création et approvisionnement

- La création ou le renouvellement des données de test doit être demandé via un processus documenté.
- L'approbation du Propriétaire des données est requise avant que toute donnée dérivée de la production n'entre dans un environnement de test.
- Le masquage ou l'anonymisation doit être appliqué avant que les données ne soient accessibles dans l'environnement de test (pas après).
- Toutes les activités d'approvisionnement en données doivent être journalisées à des fins d'audit.

### Conservation et élimination

Les données de test contenant des données de production masquées ou pseudonymisées ne doivent être conservées que pour la durée de l'exigence de test. À l'achèvement du projet, les données de test doivent être supprimées dans les 30 jours.

Pour les environnements de test continus :

- Les données de test doivent être révisées trimestriellement pour vérifier leur utilité continue.
- Les données de plus de 90 jours sans usage actif documenté doivent être signalées pour suppression.
- La conservation au-delà de 90 jours nécessite l'approbation du Propriétaire des données avec une justification métier documentée.
- Une surveillance automatisée de la conservation doit alerter lorsque les données dépassent les seuils.

**Élimination** : L'élimination des données de test doit suivre les mêmes procédures de suppression sécurisée que les données de production de classification équivalente. L'élimination doit être vérifiée et documentée.

### Renouvellement des données

Lors du renouvellement des données de test à partir de sources de production :

- Un nouveau masquage doit être appliqué à chaque cycle de renouvellement (le masquage précédent ne se transfère pas).
- Les procédures de renouvellement doivent être documentées et approuvées par le Propriétaire des données.
- Les activités de renouvellement doivent être journalisées, incluant le système source, le volume, la méthode de masquage et l'opérateur.
- Les données de test précédentes doivent être supprimées de manière sécurisée avant ou immédiatement après l'achèvement du renouvellement.

---

## Planification et gouvernance des audits

### Accord préalable à l'audit

Avant le commencement de tout test d'audit, l'organisation doit établir un accord formel entre le testeur et la direction appropriée couvrant :

- **Périmètre** : Systèmes, réseaux, applications et données à tester.
- **Méthodologie** : Méthodes, outils et techniques de test à utiliser.
- **Calendrier** : Dates de début et de fin, fenêtres de test et périodes exclues.
- **Limites** : Systèmes et données explicitement exclus des tests.
- **Escalade** : Procédures pour les problèmes, incidents ou résultats critiques durant les tests.
- **Confidentialité** : Exigences de non-divulgation pour les résultats d'audit et les données accédées.
- **Rapports** : Livrables attendus, format et délais pour les résultats.

Les accords préalables à l'audit doivent être documentés, signés par les deux parties et conservés comme preuves.

### Planification et coordination

Les activités de test d'audit doivent être planifiées pour minimiser l'impact opérationnel :

- Les périodes métier critiques (ex. : clôture de fin de mois, pic d'activité, fenêtres de maintenance des systèmes) doivent être évitées, sauf si les tests visent spécifiquement la résilience durant ces périodes.
- Les fenêtres de test doivent être coordonnées avec les opérations informatiques et les propriétaires de systèmes concernés.
- Les parties prenantes affectées doivent être notifiées des activités de test planifiées, incluant le calendrier, la portée et l'impact potentiel.
- Les tests d'urgence ou non planifiés doivent suivre un processus d'approbation accéléré avec une revue post-facto dans les 48 heures.

---

## Contrôle d'accès des auditeurs

Les accès accordés aux auditeurs, évaluateurs et testeurs d'intrusion doivent respecter le principe du moindre privilège.

**Exigences d'accès** :

| Exigence | Standard |
|----------|----------|
| Niveau d'accès par défaut | Lecture seule aux informations et aux logiciels |
| Accès en écriture ou d'administration | Uniquement lorsque la lecture seule est insuffisante ; un administrateur dispose des droits d'accès nécessaires et agit au nom de l'auditeur dans la mesure du possible |
| Authentification | AMF requise pour l'accès à tout système contenant des données sensibles |
| Durée | Limitée à la période d'audit convenue ; expiration automatique |
| Périmètre | Limité aux systèmes et données définis dans l'accord préalable à l'audit |
| Journalisation | Tous les accès des auditeurs sont journalisés et surveillés tout au long de la mission |

Lorsque l'accès en lecture seule n'est pas réalisable, un administrateur disposant des droits d'accès nécessaires doit effectuer l'accès au système ou aux données au nom de l'auditeur, ce dernier observant et dirigeant.

**Sécurité des équipements** : Avant d'accorder l'accès, l'organisation doit vérifier que les équipements des auditeurs satisfont aux exigences minimales de sécurité, incluant des correctifs du système d'exploitation à jour, une protection des terminaux active, un chiffrement intégral du disque, et l'absence de logiciel malveillant connu. Les auditeurs utilisant des équipements non conformes doivent se voir fournir des équipements gérés par l'organisation ou un accès bureau virtuel.

**Déprovisionnement des accès** : Les accès des auditeurs doivent être révoqués dans les 24 heures suivant l'achèvement de l'audit ou la date d'expiration d'accès convenue, selon la première de ces deux échéances. Le déprovisionnement doit être vérifié et documenté.

---

## Contrôles des tests d'intrusion

### Autorisation et règles d'engagement

Les tests d'intrusion et les tests de sécurité actifs doivent être autorisés par écrit par le RSSI (ou son délégué) et les propriétaires de systèmes concernés avant le début des tests.

**Les règles d'engagement** doivent documenter :

- Le périmètre de test autorisé (plages IP, applications, comptes, emplacements physiques).
- Les activités interdites (déni de service, ingénierie sociale ciblant des individus spécifiques, exfiltration de données réelles).
- La méthodologie et le cadre de test (ex. : Guide de test OWASP, PTES, NIST SP 800-115).
- Les protocoles de communication (contact principal, contact d'urgence, fréquence du reporting de statut).
- Les exigences de traitement des données pour toute donnée accédée durant les tests.
- Les procédures d'incident en cas d'impact opérationnel non intentionnel lors des tests.
- La gestion des preuves et la destruction sécurisée des artefacts de test.

### Garanties opérationnelles

Durant les tests d'intrusion :

- Les opérations informatiques doivent être en veille avec la capacité d'intervenir si les systèmes en production sont affectés.
- Les tests doivent être conduits dans des environnements isolés ou hors production dans la mesure du possible.
- Lorsque des tests en production sont requis, des procédures de retour arrière et de restauration doivent être préparées à l'avance.
- Les tests doivent être immédiatement suspendus en cas d'impact opérationnel non intentionnel et ne doivent pas reprendre sans approbation explicite du Responsable des opérations informatiques et du RSSI.

### Gestion des résultats

- Les vulnérabilités critiques découvertes lors des tests doivent être signalées immédiatement à l'Équipe sécurité (pas différées au rapport final).
- Les vulnérabilités doivent être traitées conformément au processus de gestion des vulnérabilités de l'organisation (A.8.8).
- Les testeurs ne doivent pas exploiter les vulnérabilités au-delà du périmètre nécessaire à la vérification et à l'évaluation du risque.
- Les rapports de tests d'intrusion doivent être classifiés Confidentiel et distribués uniquement aux destinataires autorisés.

### Communication du statut des tests

Durant les tests d'intrusion actifs ou les missions d'audit prolongées, le testeur doit fournir des mises à jour quotidiennes du statut au contact organisationnel désigné. Les mises à jour de statut doivent inclure :

- Résumé des activités réalisées durant la période de reporting.
- Résumé des résultats identifiés (par sévérité : Critique, Élevé, Moyen, Faible).
- Activités prévues pour la prochaine période de reporting.
- Tout problème, préoccupation ou impact opérationnel observé.

Les résultats critiques doivent être signalés immédiatement par téléphone au RSSI, en plus de toute mise à jour quotidienne. Le format et la fréquence du reporting de statut doivent être convenus dans l'accord préalable à l'audit.

---

## Gestion des outils d'audit

### Approbation et contrôle des outils

Les outils d'audit et de test utilisés pour évaluer les systèmes de l'organisation doivent être :

- Pré-approuvés par le Responsable de la sécurité de l'information avant utilisation sur les systèmes organisationnels.
- Vérifiés comme exempts de logiciels malveillants ou de fonctionnalités non autorisées.
- Documentés dans l'accord préalable à l'audit (nom de l'outil, version, objectif).
- Limités au périmètre de test convenu.

Les outils d'audit ne doivent pas être installés sur les systèmes en production sans approbation explicite du RSSI. Dans la mesure du possible, les outils d'audit doivent être exécutés depuis des postes de travail d'audit dédiés ou des environnements virtuels isolés.

### Protection des outils

Les outils d'audit, scripts et fichiers de configuration doivent être protégés contre tout accès non autorisé tant pendant qu'après la mission. Les outils capables d'exploiter des vulnérabilités ou de contourner des contrôles de sécurité doivent être retirés des systèmes organisationnels à l'achèvement de l'audit.

---

## Protection des journaux d'audit

Les journaux générés lors des activités d'audit et de test doivent être protégés contre toute modification ou suppression non autorisée afin de maintenir l'intégrité de la piste d'audit.

**Exigences de protection des journaux** :

- Les journaux d'audit doivent être écrits sur des supports à l'épreuve des falsifications (ex. : supports à écriture unique, SIEM avec contrôles d'intégrité ou équivalent).
- Les journaux doivent capturer : l'horodatage (UTC), l'identité de l'utilisateur, l'IP source, l'action effectuée, le système affecté et le résultat (succès/échec).
- Les journaux générés lors des tests d'audit doivent être conservés conformément à la politique de conservation des journaux de l'organisation (minimum 1 an pour les événements d'accès, 3 ans pour les événements de sécurité).
- Les journaux doivent être disponibles pour révision si les résultats d'audit sont contestés ou nécessitent des éclaircissements.
- Durant les tests d'intrusion actifs, une surveillance renforcée doit être activée pour distinguer les activités de test autorisées des véritables événements de sécurité.

---

## Gestion des incidents lors des tests d'audit

Si un audit ou des tests d'intrusion provoquent un impact opérationnel non intentionnel :

1. **Suspension immédiate** : Les tests doivent cesser immédiatement lors de la détection d'un impact non intentionnel.
2. **Notification** : Les opérations informatiques doivent être notifiées pour le confinement et la restauration.
3. **Analyse des causes racines** : La cause de l'impact non intentionnel doit être documentée.
4. **Remédiation** : Les systèmes affectés doivent être restaurés en fonctionnement normal.
5. **Approbation de reprise** : Les tests ne doivent pas reprendre sans approbation explicite du Responsable des opérations informatiques.
6. **Retour d'expérience** : L'incident doit être documenté et intégré dans la planification future des audits préalables.

Les véritables incidents de sécurité découverts lors des tests d'audit (ex. : preuves d'une compromission antérieure, menaces actives) doivent être immédiatement escaladés conformément au processus de gestion des incidents de l'organisation (A.5.24-28).

---

## Définitions

| Terme | Définition |
|-------|------------|
| **Anonymisation** | Processus irréversible de suppression de toutes les informations identificatrices tel que la ré-identification n'est pas raisonnablement possible |
| **Test d'audit** | Examen systématique des systèmes, contrôles et processus pour vérifier la conformité et l'efficacité |
| **Masquage des données** | Processus d'obscurcissement des données d'origine par un contenu modifié tout en maintenant le format et l'utilisabilité pour les tests |
| **Test en boîte grise** | Approche de test d'intrusion où le testeur dispose d'une connaissance partielle de l'environnement cible |
| **Test d'intrusion** | Attaque simulée autorisée sur les systèmes pour identifier les vulnérabilités de sécurité exploitables |
| **Données de production** | Données opérationnelles en direct issues des systèmes métier contenant des informations personnelles ou métier réelles |
| **Pseudonymisation** | Remplacement des identifiants directs par des pseudonymes ; ré-identifiable avec une clé de correspondance stockée séparément |
| **Règles d'engagement** | Accord documenté définissant le périmètre, les limites, les méthodes et les contraintes pour les tests d'intrusion |
| **Données synthétiques** | Données générées artificiellement ne contenant aucune information personnelle ou métier réelle, conçues pour imiter les caractéristiques des données de production |
| **Environnement de test** | Système hors production utilisé à des fins de développement, de test, de formation ou de démonstration |

---

## Rôles et responsabilités

| Rôle | Responsabilités |
|------|-----------------|
| **RSSI** | Propriété de la politique ; autorisation des tests d'intrusion ; approbation des exceptions pour l'utilisation directe de données de production ; supervision de la gouvernance des tests d'audit ; révision annuelle de la politique ; reporting à la Direction générale |
| **Responsable de la sécurité de l'information** | Maintenance de la politique ; coordination des audits ; approbation de la validation du masquage ; révision des exceptions ; surveillance de la conformité ; reporting trimestriel au RSSI |
| **Délégué à la protection des données (DPD)** | Conformité des données de test à la protection de la vie privée ; révision de l'adéquation de l'anonymisation ; alignement nLPD et RGPD ; approbation pour l'utilisation de données pseudonymisées |
| **Responsable des opérations informatiques** | Protection des systèmes en production lors des tests d'audit ; coordination de la planification ; réponse aux incidents durant les tests ; vérification des équipements des auditeurs |
| **Propriétaires des données** | Autorisation des données de test ; approbation du masquage ; décisions de classification des données ; révision de la conservation pour les données de test dérivées de leurs systèmes |
| **Responsable du développement / Responsable AQ** | Gestion des environnements de test ; procédures d'approvisionnement en données de test ; conformité des développeurs et testeurs ; supervision de la génération de données synthétiques |
| **Équipe sécurité** | Gestion des outils d'audit ; coordination des tests d'intrusion ; traitement des vulnérabilités détectées ; surveillance renforcée durant les tests |
| **Audit interne** | Planification et gestion des missions d'audit ; préparation des accords préalables à l'audit ; reporting des résultats et suivi |
| **Auditeurs externes et testeurs d'intrusion** | Conformité aux restrictions d'accès, règles d'engagement et exigences de confidentialité ; respect du périmètre ; signalement immédiat des résultats critiques |
| **Tout le personnel de test** | Conformité aux exigences de traitement des données de test ; pas d'utilisation de données de production non masquées sans approbation ; signalement des incidents ; élimination sécurisée des artefacts de test |

---

## Preuves

Les preuves suivantes démontrent la conformité à la présente politique :

| # | Preuve | Responsable | Fréquence | Conservation |
|---|--------|-------------|-----------|--------------|
| 1 | **Inventaire des données de test** listant tous les jeux de données de test, le type de source (synthétique/anonymisé/masqué), la classification et l'équipe responsable | Responsable du développement / Responsable AQ | Maintenu en continu ; révisé trimestriellement | Durée de vie du jeu de données + 1 an |
| 2 | **Enregistrements de demande et d'approbation des données de test** (demandes, justifications, approbations des propriétaires de données, méthode de masquage utilisée) | Propriétaires des données / Responsable de la sécurité de l'information | Par demande | 3 ans |
| 3 | **Enregistrements de validation du masquage des données** (résultats des tests de validation, approbation du Responsable de la sécurité de l'information, date) | Responsable de la sécurité de l'information / Équipe sécurité | Par opération de masquage | 3 ans |
| 4 | **Enregistrements de génération de données synthétiques** (paramètres du générateur, résultats de validation, version) | Responsable du développement | Par génération | 2 ans |
| 5 | **Enregistrements de conservation et d'élimination des données de test** (révisions trimestrielles, confirmations de suppression, méthode d'élimination) | Responsable du développement / Responsable AQ | Révision trimestrielle ; par événement d'élimination | 3 ans |
| 6 | **Accords préalables aux tests d'intrusion et d'audit** (périmètre, méthodologie, calendrier, règles d'engagement, signatures) | RSSI / Audit interne | Par mission | 3 ans |
| 7 | **Enregistrements d'accès des auditeurs et testeurs** (provisionnement des accès, périmètre, durée, confirmation de déprovisionnement) | Opérations informatiques / Responsable de la sécurité de l'information | Par mission | 3 ans |
| 8 | **Enregistrements de vérification de conformité des équipements des auditeurs** (résultats des contrôles de sécurité, approbation) | Opérations informatiques | Par mission | 1 an |
| 9 | **Rapports et résultats des tests d'intrusion** (rapports complets, suivi de remédiation, preuves de clôture) | RSSI / Équipe sécurité | Par mission | 3 ans |
| 10 | **Enregistrements d'approbation des outils d'audit** (nom de l'outil, version, objectif, approbation du Responsable de la sécurité de l'information) | Responsable de la sécurité de l'information | Par mission | 2 ans |
| 11 | **Journaux des activités d'audit et de test** (journaux d'accès des auditeurs, enregistrements d'activité de test, alertes de surveillance) | Opérations informatiques / Équipe sécurité | Continu | Selon la politique de conservation des journaux (1–3 ans) |
| 12 | **Rapports d'incidents issus des activités de test** (impacts non intentionnels, cause racine, remédiation, retour d'expérience) | Opérations informatiques / RSSI | Par incident | 3 ans |
| 13 | **Registre des exceptions** (demandes d'utilisation directe de données de production, approbations, contrôles compensatoires, expiration) | Responsable de la sécurité de l'information | Maintenu en continu ; révisé trimestriellement | Durée de l'exception + 3 ans |

---

# Conformité à la politique

## Mesure de la conformité

L'équipe de gestion de la sécurité de l'information vérifiera la conformité à la présente politique par diverses méthodes, incluant notamment les inventaires des données de test, les enregistrements de validation du masquage, la documentation des missions d'audit, les journaux d'accès, les rapports de tests d'intrusion, les audits internes et externes, et le retour d'information au propriétaire de la politique.

**Métriques de conformité** :

| Métrique | Cible | Fréquence de mesure |
|----------|--------|---------------------|
| Environnements de test utilisant des données synthétiques ou anonymisées (pas de données de production non masquées) | >= 95 % | Trimestrielle |
| Validation du masquage effectuée et approuvée avant la diffusion des données de test | 100 % | Par opération de masquage |
| Accords préalables à l'audit signés avant le début des tests | 100 % | Par mission |
| Accès des auditeurs déprovisionné dans les 24 heures suivant l'achèvement de l'audit | 100 % | Par mission |
| Résultats des tests d'intrusion remédiés dans les SLA | >= 90 % | Par mission |
| Données de test éliminées dans les 30 jours suivant l'achèvement du projet | >= 90 % | Trimestrielle |

**Notation de la conformité** :

| Composant | Pondération | Calcul |
|-----------|-------------|--------|
| Conformité de la protection des données de test | 40 % | (Environnements de test avec sources de données approuvées + validations de masquage effectuées) / Total des environnements de test × 100 |
| Conformité de la gouvernance des audits | 30 % | (Missions avec accords préalables signés + accès correctement provisionné et déprovisionné) / Total des missions × 100 |
| Conformité de la gestion des résultats | 20 % | (Résultats de tests d'intrusion et d'audit remédiés dans les SLA) / Total des résultats × 100 |
| Conformité du cycle de vie des données | 10 % | (Jeux de données de test éliminés dans les délais de la politique) / Total des jeux de données nécessitant élimination × 100 |

**Gestion de la non-conformité** : Un score inférieur à 70 % nécessite une escalade immédiate au RSSI et un plan de remédiation. Entre 70 et 89 %, une supervision du Responsable de la sécurité de l'information avec des revues mensuelles est requise. À partir de 90 %, le suivi trimestriel standard s'applique.

## Exceptions

Toute exception à la présente politique doit être approuvée et enregistrée à l'avance par le RSSI, avec acceptation documentée du risque, contrôles compensatoires (journalisation renforcée, conservation réduite, restrictions d'accès supplémentaires) et date de révision définie (maximum 12 mois). Les exceptions pour l'utilisation directe de données de production dans les environnements de test nécessitent en outre l'approbation du DPD. Les exceptions doivent être rapportées à l'Équipe de revue de direction.

## Non-conformité

Tout employé reconnu coupable d'avoir violé la présente politique peut faire l'objet de mesures disciplinaires, pouvant aller jusqu'au licenciement. L'utilisation de données de production non masquées dans des environnements de test sans approbation doit être traitée comme un incident de traitement des données et faire l'objet d'une investigation. Les violations de la politique doivent être documentées, investiguées par le Responsable de la sécurité de l'information et rapportées au RSSI.

## Amélioration continue

La présente politique est révisée et mise à jour dans le cadre du processus d'amélioration continue. Les révisions doivent prendre en compte les avancées dans les techniques d'anonymisation et de génération de données synthétiques, les risques émergents de ré-identification (notamment la dé-anonymisation assistée par l'IA), les évolutions des méthodologies de tests d'intrusion et du paysage des menaces, les changements réglementaires (notamment les orientations nLPD et la jurisprudence d'application du RGPD), les constatations d'audit et les enseignements tirés des incidents de test, et le retour des équipes de développement, AQ et audit.

---

# Zones de la norme ISO 27001 couvertes

Politique sur les informations de test et la protection lors des tests d'audit — Correspondance avec les contrôles ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership et engagement | 5.1 Politiques de sécurité de l'information |
| Clause 5.2 Politique | 5.4 Responsabilités de la direction |
| Clause 6.2 Objectifs de sécurité de l'information | 5.36 Conformité aux politiques, règles et standards |
| Clause 7.3 Sensibilisation | 6.3 Sensibilisation, éducation et formation à la sécurité de l'information |
| Clause 9.2 Audit interne | 8.11 Masquage des données |
| | **8.33 Informations de test** |
| | **8.34 Protection des systèmes d'information lors des tests d'audit** |
| | 8.31 Séparation des environnements de développement, de test et de production |

**Cadre réglementaire et légal** :

| Cadre | Pertinence |
|-------|-----------|
| nLPD suisse (revLPD) | Art. 8 — Mesures techniques et organisationnelles pour la protection des données ; anonymisation et pseudonymisation comme mesures de protection des données ; les données de test contenant des données personnelles sont soumises aux exigences de la nLPD |
| OPDo suisse (Ordonnance sur la protection des données) | Art. 1–3 — Exigences minimales en matière de sécurité des données, incluant les contrôles des environnements de test |
| RGPD de l'UE (le cas échéant) | Art. 5(1)(c) — Minimisation des données (pas de données de production inutiles dans les environnements de test) ; Art. 25 — Protection des données dès la conception et par défaut ; Art. 32 — Sécurité du traitement (pseudonymisation comme mesure de sécurité) |
| ISO/IEC 27001:2022 | Contrôles Annexe A 8.33 et 8.34 |
| ISO/IEC 27002:2022 | Sections 8.33 et 8.34 — Recommandations de mise en œuvre |
| NIST SP 800-53 Rév. 5 | SA-11 (Tests et évaluation par les développeurs), CA-8 (Tests d'intrusion), AU-11 (Conservation des enregistrements d'audit), SI-12 (Gestion et conservation des informations) |
| CIS Controls v8 | 3.1–3.14 (Protection des données), 18.1–18.5 (Tests d'intrusion) |

---

<!-- QA_VERIFIED: 2026-03-29 -->
