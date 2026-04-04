<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.8.30-FR:operational:OP-POL:a.8.30 -->
**ISMS-OP-POL-A.8.30 — Développement externalisé**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Développement externalisé |
| **Type de document** | Politique opérationnelle |
| **Identifiant du document** | ISMS-OP-POL-A.8.30 |
| **Créateur du document** | Responsable de la sécurité de l'information (RSSI) |
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

**Documents associés** :

- ISO/IEC 27001:2022 Contrôle A.8.30 — Développement externalisé
- ISO/IEC 27002:2022 Section 8.30 — Conseils de mise en œuvre pour le développement externalisé
- NIST SP 800-53 Rév. 5 — SA-4 (Processus d'acquisition), SA-9 (Services de systèmes externes)
- OWASP Secure Software Contract Annex
- OWASP Top 10:2025 — A03 Défaillances de la chaîne d'approvisionnement logicielle
- CIS Controls v8 — Mesure de protection 16.4 (Inventaire des composants logiciels tiers)

**Contrôles Annexe A associés** :

| Contrôle | Relation avec le développement externalisé |
|----------|--------------------------------------------|
| A.5.19–23 Sécurité de l'information dans les relations avec les fournisseurs et services cloud | Cadre d'évaluation des fournisseurs ; plateformes de développement hébergées dans le cloud |
| A.5.31 Exigences légales, réglementaires et contractuelles | Obligations réglementaires dans les contrats d'externalisation |
| A.5.34 Protection de la vie privée et des DCP | Exigences de protection des données pour l'accès des fournisseurs aux données personnelles |
| A.8.4 Accès au code source | Accès des fournisseurs aux référentiels organisationnels |
| A.8.25–26–29 Cycle de développement sécurisé | Codage sécurisé, tests et exigences SDLC appliqués au travail externalisé |
| A.8.28 Codage sécurisé | Normes de codage étendues aux développeurs tiers |
| A.8.31 Séparation des environnements | Cloisonnement des environnements pour le développement externalisé |
| A.8.32 Gestion des changements | Contrôle des changements pour la promotion du code externalisé |

**Politiques internes associées** :

- Politique de cycle de développement sécurisé
- Politique de sécurité de l'information dans les relations avec les fournisseurs et services cloud
- Politique d'accès au code source
- Politique de gestion des changements
- Politique de classification et de traitement de l'information
- Politique de protection de la vie privée et des DCP

---

# Politique relative au développement externalisé

## Objet

La présente politique a pour objet de garantir que l'organisation dirige, surveille et révise toutes les activités liées au développement externalisé de systèmes et de logiciels, afin que le code développé en externe satisfasse aux exigences de sécurité de l'information de l'organisation avant acceptation et déploiement.

Cette politique soutient l'art. 9 de la nLPD (revDSG) suisse en établissant des exigences contractuelles pour les sous-traitants impliqués dans le développement logiciel, garantissant que les activités de développement externalisé ne traitent les données personnelles que de la manière dont l'organisation elle-même est autorisée à les traiter. Les exigences de l'art. 8 en matière de mesures techniques et organisationnelles s'appliquent également aux composants externalisés. Lorsque l'organisation traite des données de personnes dans l'UE/EEE, les exigences de l'art. 28 du RGPD (obligations du sous-traitant) et de l'art. 32 (sécurité du traitement) s'appliquent également.

## Champ d'application

Toutes les activités de développement de systèmes et de logiciels réalisées par des parties externes pour le compte de l'organisation, notamment :

- Le développement logiciel sur mesure par des entreprises de développement sous contrat.
- Les équipes de développement offshore et nearshore.
- Les développeurs et sous-traitants indépendants.
- Les partenariats de développement et les arrangements de co-développement.
- La personnalisation et l'extension de logiciels acquis par des tiers.
- La maintenance et l'amélioration par des tiers de systèmes organisationnels existants.

Tous les employés responsables de l'approvisionnement, de la gestion ou de l'acceptation du travail de développement externalisé.

**Hors périmètre** : Les logiciels commerciaux sur étagère (COTS) achetés sans personnalisation (couverts par A.5.19–23) ; les activités de développement internes (couvertes par A.8.25-26-29) ; les services de plateforme cloud sans développement de code personnalisé ; les logiciels open source utilisés comme dépendances (couverts par les exigences SCA dans la Politique de cycle de développement sécurisé).

## Principe

L'organisation conserve la responsabilité de la sécurité du code externalisé indépendamment de l'endroit et de la personne qui le développe. Le développement externalisé est soumis à des exigences de sécurité, des contrôles contractuels et des activités de vérification équivalents — ou plus stricts — que ceux appliqués au développement interne.

Aucun code externalisé ne peut être déployé en production sans la validation de sécurité indépendante et l'acceptation formelle de l'organisation.

---

## Évaluation de la sécurité des fournisseurs

Avant de s'engager avec un partenaire de développement externe, l'organisation réalise une évaluation de sécurité pour confirmer la capacité du fournisseur à satisfaire aux exigences de sécurité de l'information.

**Critères d'évaluation pré-engagement** :

| Domaine d'évaluation | Exigences minimales |
|----------------------|---------------------|
| **Certifications de sécurité** | Preuves de certification ISO 27001, rapport SOC 2 Type II ou équivalent ; ou complétion du questionnaire de sécurité fournisseur de l'organisation |
| **Pratiques de développement sécurisé** | SDLC documenté avec activités de sécurité ; utilisation de processus SAST, SCA et de revue de code |
| **Sécurité du personnel** | Vérifications des antécédents pour les développeurs accédant aux données organisationnelles ; NDA signé par toutes les personnes ayant accès |
| **Protection des données** | Accord de traitement des données (ATD) conforme à l'art. 9 de la nLPD suisse ; évaluation de la résidence et du transfert des données réalisée |
| **Réponse aux incidents** | Capacité documentée de réponse aux incidents de sécurité ; capacité à notifier l'organisation dans les 24 heures suivant un événement de sécurité |
| **Continuité d'activité** | Preuves de planification de la continuité d'activité ; séquestre de code source ou arrangement de continuité équivalent le cas échéant |
| **Références** | Références vérifiables d'engagements comparables |

**Niveaux d'évaluation** :

| Niveau du fournisseur | Critères | Profondeur de l'évaluation |
|----------------------|----------|---------------------------|
| **Niveau 1 — Risque élevé** | Le fournisseur développe des applications à risque élevé ; accède aux données de production ou aux DCP ; développe des systèmes accessibles depuis Internet | Évaluation complète + audit sur site ou à distance + réévaluation annuelle |
| **Niveau 2 — Risque moyen** | Le fournisseur développe des outils internes ; accès limité aux données ; pas d'accès direct à la production | Questionnaire de sécurité + revue des preuves + réévaluation biennale |
| **Niveau 3 — Risque faible** | Le fournisseur développe des utilitaires non critiques ; pas d'accès aux données sensibles | Questionnaire de sécurité + auto-attestation + réévaluation au renouvellement du contrat |

**Détermination du niveau du fournisseur** :

Les fournisseurs sont classés sur la base du facteur de risque le plus élevé présent :

**Déclencheurs Niveau 1** (l'un ou l'autre suffit) :
- Développe des applications traitant des données Confidentielles ou Restreintes
- Accès direct aux environnements de production ou aux bases de données
- Développe des systèmes accessibles depuis Internet avec authentification utilisateur
- Traite les données personnelles de >1 000 personnes
- Personnalise le traitement des paiements ou des systèmes financiers
- Accès aux référentiels de code source contenant des algorithmes propriétaires

**Déclencheurs Niveau 2** (aucun critère Niveau 1, mais l'un des suivants) :
- Développe des applications uniquement internes
- Accès en lecture seule aux données hors production
- Traite les données personnelles de <1 000 personnes
- Travaux d'intégration avec des API tierces
- Développement d'outils de reporting et d'analyse

**Niveau 3** (par défaut) :
- Développement d'utilitaires (scripts, outils CLI, automatisation non critique)
- Développement de sites web statiques sans collecte de données utilisateur
- Documentation et conception UI/UX (sans accès au code)
- Travaux de prototype/preuve de concept avec données synthétiques uniquement

La détermination du niveau est documentée dans l'enregistrement de l'évaluation de sécurité du fournisseur et révisée lors des changements de périmètre.

Les résultats de l'évaluation sont documentés et conservés pour la durée de la relation avec le fournisseur plus 3 ans.

Les fournisseurs qui échouent à l'évaluation de sécurité ne peuvent pas être engagés jusqu'à ce que les déficiences identifiées aient été remédiées et vérifiées.

### Signaux d'alerte lors de l'évaluation des fournisseurs

Lors de l'évaluation des fournisseurs, les éléments suivants constituent des conclusions disqualifiantes sauf remédiation :

| Signal d'alerte | Risque | Remédiation requise |
|-----------------|--------|---------------------|
| **Aucun SDLC formel** | Développement non structuré ; pratiques de sécurité incohérentes | Documenter le SDLC avec des portes de sécurité ; démontrer ≥3 mois d'application cohérente |
| **Pas d'outils SAST/SCA** | Vulnérabilités non détectées avant livraison | Mettre en œuvre l'analyse automatisée de sécurité ; démontrer ≥3 analyses avec remédiation |
| **Le fournisseur refuse la clause de droits d'audit** | Impossibilité de vérifier les affirmations de sécurité | Accepter les droits d'audit ou fournir une certification SOC 2 Type II / ISO 27001 |
| **Externalisation à des sous-traitants non divulgués** | Posture de sécurité inconnue dans la chaîne d'approvisionnement | Transparence totale sur les sous-traitants ; répercussion des exigences de sécurité ; évaluation de chacun |
| **Pas de capacité de réponse aux incidents** | Impossibilité de détecter ou de répondre à une compromission | Documenter le plan de réponse aux incidents ; prendre l'engagement de notification en 24h ; démontrer les tests de réponse aux incidents |
| **Violation significative antérieure (non résolue)** | Schéma de mauvaise sécurité | Démontrer les améliorations post-incident ; validation tierce de la remédiation |
| **Absence de vérifications des antécédents** | Risque de menace interne | Mettre en œuvre les vérifications des antécédents pour le personnel ayant accès aux données |
| **Utilisation de messagerie personnelle pour le travail** | Pas de séparation des données professionnelles/personnelles | Fournir une messagerie professionnelle ; documenter la politique d'utilisation acceptable |

**Lors de l'engagement, ces éléments sont des déclencheurs d'escalade** :
- Le fournisseur fournit de fausses informations dans l'évaluation de sécurité
- Exfiltration de données non autorisée détectée
- Le fournisseur refuse la remédiation des vulnérabilités
- Les résultats des tests de sécurité sont retenus ou falsifiés

---

## Exigences contractuelles de sécurité

Tous les accords de développement externalisé incluent des exigences de sécurité en tant qu'obligations contractuelles.

**Clauses contractuelles obligatoires** :

| Clause | Exigence |
|--------|----------|
| **Normes de développement sécurisé** | Le fournisseur doit se conformer aux normes de codage sécurisé et à la Politique de cycle de développement sécurisé de l'organisation, ou démontrer des normes équivalentes approuvées par le RSSI |
| **Tests de sécurité** | Le fournisseur doit effectuer des analyses SAST et SCA sur tous les livrables ; DAST pour les applications web et les API ; les résultats doivent être partagés avec l'organisation avant acceptation |
| **Remédiation des vulnérabilités** | Critiques : 7 jours ; Élevées : 30 jours ; Moyennes : 90 jours ; Faibles : 180 jours — alignés sur les SLA de remédiation de l'organisation |
| **Notification d'incident de sécurité** | Le fournisseur doit notifier l'organisation dans les 24 heures suivant la découverte d'un incident de sécurité affectant l'engagement, y compris les violations de données suspectées, la compromission du code ou les accès non autorisés |
| **Droits d'audit** | L'organisation se réserve le droit d'auditer les pratiques de sécurité, les environnements de développement et les processus du fournisseur avec un préavis écrit de 30 jours calendaires |
| **Droits de revue de code** | L'organisation doit avoir le droit d'examiner, de tester et d'inspecter tout le code source, les scripts de compilation et les fichiers de configuration livrés dans le cadre de l'accord |
| **Sous-traitance** | Le fournisseur ne doit pas sous-traiter les travaux de développement sans l'approbation écrite préalable de l'organisation ; les sous-traitants doivent satisfaire à des exigences de sécurité équivalentes |
| **Protection des données** | Accord de traitement des données conformément à l'art. 9 de la nLPD suisse ; données personnelles traitées uniquement selon les instructions de l'organisation ; transferts transfrontaliers soumis à une évaluation de transfert |
| **Confidentialité** | NDA couvrant toutes les informations propriétaires, le code source, l'architecture système et les données auxquels il est accédé pendant l'engagement |
| **Dispositions de résiliation** | Retour sécurisé ou destruction de toutes les données organisationnelles, code source, identifiants et accès à la résiliation du contrat ; vérification dans les 30 jours |

**Clauses contractuelles recommandées** (selon le risque de l'engagement) :

| Clause | Applicabilité |
|--------|---------------|
| **Tests d'intrusion** | Requis pour les fournisseurs de Niveau 1 ; l'organisation ou un tiers qualifié réalise des tests d'intrusion avant acceptation en production |
| **Vérifications des antécédents** | Requises pour le personnel du fournisseur de Niveau 1 accédant aux DCP, aux données financières ou aux environnements de production |
| **Formation à la sécurité** | Le personnel du fournisseur doit suivre la formation de sensibilisation à la sécurité de l'organisation ou démontrer une formation équivalente |
| **Responsabilité et indemnisation** | Responsabilité du fournisseur pour les violations de sécurité causées par la non-conformité aux exigences contractuelles de sécurité |
| **Assurance** | Assurance de responsabilité civile professionnelle et de cybersécurité appropriée à la valeur et au risque de l'engagement |

**Processus d'approbation de la sous-traitance** :

Lorsqu'un fournisseur demande une approbation de sous-traitance :
1. **Notification** : Le fournisseur soumet une demande écrite ≥30 jours avant l'engagement du sous-traitant, incluant :
   - Nom et localisation du sous-traitant
   - Périmètre des travaux à sous-traiter
   - Accès aux données requis par le sous-traitant
   - Résultats de l'évaluation de sécurité du sous-traitant
   - Confirmation de la répercussion des exigences contractuelles de sécurité

2. **Évaluation** : L'organisation évalue le sous-traitant selon les mêmes critères de sécurité que le fournisseur principal (évaluation adaptée au niveau)

3. **Approbation** :
   - Fournisseurs de Niveau 1 : Approbation du RSSI requise
   - Fournisseurs de Niveau 2/3 : Approbation du responsable développement avec notification au RSSI

4. **Documentation** : Sous-traitants approuvés ajoutés à l'enregistrement d'évaluation de sécurité du fournisseur ; mêmes exigences de surveillance et de gestion des accès applicables

La sous-traitance non approuvée constitue une violation matérielle du contrat et un motif de résiliation.

---

## Exigences de développement sécurisé pour les fournisseurs

Les normes de développement sécurisé de l'organisation sont communiquées aux fournisseurs au début de chaque engagement.

**Package de normes de développement pour les fournisseurs** :

L'organisation fournit à chaque fournisseur :

- Les normes de codage sécurisé applicables à la pile technologique utilisée.
- La spécification des exigences de sécurité du projet.
- Le modèle de menaces (s'il en existe un pour l'application).
- Les normes et bibliothèques cryptographiques approuvées.
- Les exigences de journalisation et de gestion des erreurs.
- Les normes de sécurité des API (si applicable).
- Les exigences de validation des entrées et d'encodage des sorties.

**Exigences relatives à l'environnement de développement des fournisseurs** :

| Exigence | Détail |
|----------|--------|
| **Cloisonnement des environnements** | Les environnements de développement, de test et de production sont séparés ; les environnements de développement des fournisseurs ne doivent pas avoir d'accès direct aux systèmes de production de l'organisation |
| **Contrôle d'accès** | L'accès des fournisseurs aux référentiels et systèmes organisationnels doit respecter le principe du moindre privilège ; l'accès est limité dans le temps et lié à la durée du contrat |
| **Gestion des identifiants** | Pas d'identifiants codés en dur dans le code source ; secrets gérés via des outils de gestion des secrets approuvés |
| **Gestion des versions** | Tout le code est maintenu dans un système de gestion des versions approuvé avec historique complet des commits et attribution |
| **Gestion des dépendances** | Les fournisseurs maintiennent un catalogue de composants logiciels (SBOM) pour tous les livrables ; les dépendances tierces sont issues de registres approuvés et analysées pour détecter les vulnérabilités connues |

**Sécurité de la chaîne d'approvisionnement** :

Les fournisseurs mettent en œuvre des contrôles pour atténuer les risques liés à la chaîne d'approvisionnement logicielle conformément à OWASP Top 10:2025 A03 (Défaillances de la chaîne d'approvisionnement logicielle) :

- Toutes les dépendances tierces sont inventoriées et suivies dans un SBOM (format CycloneDX ou SPDX).
- Les dépendances sont fixées à des versions spécifiques et issues de registres fiables.
- Les dépendances transitives sont incluses dans l'analyse de vulnérabilités.
- Les fournisseurs surveillent les dépendances par rapport aux bases de données de vulnérabilités (NVD, OSV, GitHub Advisory Database) et remédie aux vulnérabilités identifiées dans les SLA convenus.
- L'utilisation de composants non maintenus ou en fin de vie nécessite une acceptation documentée du risque par l'organisation.

**Détail des exigences relatives au SBOM** :
- **Format** : CycloneDX 1.4+ (préféré) ou SPDX 2.3+
- **Profondeur** : Inclure les dépendances transitives (pas seulement les dépendances directes)
- **Contenu** : Nom, version, licence, fournisseur, empreinte cryptographique des composants
- **Livraison** : SBOM fourni avec chaque version et mis à jour pour tout changement de dépendance
- **Outil** : Généré via un outil SBOM automatisé (CycloneDX CLI, Syft, outils SPDX ou équivalent) — pas des feuilles de calcul créées manuellement
- **Validation** : L'organisation vérifie l'exhaustivité du SBOM à l'aide d'un outil SCA avant acceptation

## Flux de travail type de développement par le fournisseur

```
┌─────────────────────────────────────────────────────────────────┐
│ PHASE D'ENGAGEMENT                                               │
├─────────────────────────────────────────────────────────────────┤
│ 1. Évaluation de sécurité du fournisseur (RSSI) ───────────────┐│
│ 2. Contrat avec clauses de sécurité (Juridique + RSSI) ────────┐││
│ 3. Exécution de l'ATD (DPD) ───────────────────────────────────┘││
│ 4. Livraison du package de développement sécurisé (Resp. Dév.) ┘│
│ 5. Provisionnement de l'accès fournisseur (IT Opérations) ──────│
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│ PHASE DE DÉVELOPPEMENT (itérative)                               │
├─────────────────────────────────────────────────────────────────┤
│ 6. Développement + Tests de sécurité du fournisseur ────────────│
│    - SAST/SCA par compilation                                    │
│    - Résultats des tests de sécurité partagés avec l'org.       │
│ 7. Livraison de jalon (Fournisseur → Resp. Dév.) ───────────────│
│ 8. Revue de code de l'organisation (Équipe sécurité) ───────────│
│ 9. Remédiation des vulnérabilités (Fournisseur) ────────────────│
│    ↺ Répéter jusqu'à satisfaction des critères d'acceptation   │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│ PHASE D'ACCEPTATION                                              │
├─────────────────────────────────────────────────────────────────┤
│ 10. Tests de sécurité indépendants (Org. / Tiers) ──────────────│
│     - SAST/SCA/DAST                                              │
│     - Tests d'intrusion (Niveau 1)                              │
│ 11. Livraison et revue du SBOM (Resp. Dév.) ────────────────────│
│ 12. Complétion de la liste de contrôle d'acceptation ───────────│
│ 13. Validation finale (selon risque : RSSI/Resp. Dév./Prop. App)│
│ 14. Dépôt au séquestre de code (si applicable) ─────────────────│
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│ PHASE POST-DÉPLOIEMENT                                           │
├─────────────────────────────────────────────────────────────────┤
│ 15. Révocation de l'accès fournisseur (IT Opérations) ──────────│
│ 16. Vérification du retour/destruction des données (DPD) ───────│
│ 17. Contrat de support continu (si applicable) ─────────────────│
│ 18. Réévaluation annuelle de sécurité (Niveau 1) ───────────────│
└─────────────────────────────────────────────────────────────────┘
```

---

## Revue de code et tests de sécurité

Tout le code externalisé fait l'objet d'une validation de sécurité indépendante par l'organisation avant acceptation.

**Tests côté fournisseur** (réalisés par le fournisseur, résultats fournis à l'organisation) :

| Type de test | Exigence | Calendrier |
|-------------|----------|------------|
| **SAST** | Analyser tout le code source pour détecter les vulnérabilités de sécurité à l'aide de [Outil SAST] (exemples : SonarQube, Semgrep, Checkmarx, Veracode ou équivalent approuvé par le RSSI) | Par compilation ou au minimum hebdomadaire lors du développement actif |
| **SCA** | Analyser toutes les dépendances pour détecter les vulnérabilités connues et la conformité des licences | Par compilation ou au minimum hebdomadaire lors du développement actif |
| **Tests unitaires/d'intégration** | Démontrer l'efficacité des contrôles de sécurité (authentification, autorisation, validation des entrées) | En continu |
| **Analyse des secrets** | Vérifier l'absence d'identifiants, de clés API ou de jetons dans le code source ou la configuration | Pré-commit et par compilation |

Les résultats des tests côté fournisseur sont partagés avec l'organisation aux intervalles convenus (minimum : par jalon ou livraison de sprint).

**Tests côté organisation** (réalisés par l'organisation ou un tiers mandaté) :

| Type de test | Exigence | Calendrier |
|-------------|----------|------------|
| **Revue de code indépendante** | Un développeur interne ou Champion sécurité examine le code du fournisseur par rapport à la liste de contrôle de codage sécurisé | Avant acceptation de chaque livrable |
| **SAST/SCA indépendants** | L'organisation exécute ses propres analyses SAST et SCA sur le code livré | Avant acceptation |
| **DAST** | Tests dynamiques de l'application en exécution (ex. OWASP ZAP, Burp Suite ou équivalent) | Avant le déploiement en production |
| **Tests d'intrusion** | Test d'intrusion par un spécialiste externe indépendant pour les applications à risque élevé | Avant le déploiement initial en production ; annuellement par la suite |

**Référence minimale des tests** : Tous les tests de sécurité doivent au minimum couvrir les catégories OWASP Top 10:2025.

Tous les tests d'intrusion sont réalisés par une société spécialisée externe indépendante satisfaisant au moins l'un des critères suivants :
- Certification CREST (CREST Registered Penetration Tester ou supérieur)
- Membres de l'équipe détenant les certifications OSCP, GPEN ou CEH
- Expérience avérée avec ≥5 tests d'intrusion comparables au cours des 2 dernières années avec références vérifiables
- Entreprise de tests d'intrusion certifiée ISO 27001 avec portfolio client public

Le prestataire de tests d'intrusion ne doit pas être la même entité que le fournisseur de développement afin de garantir l'indépendance.

Les vulnérabilités identifiées lors des tests sont remédiées par le fournisseur aux frais du fournisseur avant que l'organisation accepte le livrable. Les vulnérabilités Critiques et Élevées bloquent l'acceptation.

### Gestion de la remédiation des vulnérabilités

Toutes les vulnérabilités identifiées dans les livrables du fournisseur sont suivies jusqu'à résolution :

**Processus de suivi** :
1. **Découverte** : Vulnérabilité identifiée via SAST/SCA/DAST/test d'intrusion
2. **Attribution** : Vulnérabilité assignée au fournisseur avec SLA de remédiation
3. **Vérification** : Le fournisseur fournit le correctif + les résultats de re-test
4. **Validation** : L'organisation valide l'efficacité du correctif
5. **Clôture** : Clôture documentée avec preuves de test

**Suivi des SLA de remédiation** :

| Sévérité | SLA | Réponse en cas de dépassement |
|----------|-----|-------------------------------|
| **Critique** | 7 jours | Escalade immédiate au RSSI ; blocage de l'acceptation ; revue de la performance du fournisseur |
| **Élevé** | 30 jours | Escalade au responsable développement ; acceptation conditionnelle à un plan de remédiation |
| **Moyen** | 90 jours | Suivi lors des réunions hebdomadaires d'état ; peut être accepté avec acceptation documentée du risque et engagement de remédiation |
| **Faible** | 180 jours | Suivi dans le backlog du projet ; peut être accepté avec un sprint futur planifié pour la remédiation |

**Décompte du SLA** :
- Commence à partir de la divulgation de la vulnérabilité au fournisseur
- Suspendu pour les demandes de clarification raisonnables du fournisseur (<5 jours ouvrés)
- Réinitialisé lors d'une demande d'extension de SLA du fournisseur avec justification (approbation du RSSI)

**Communication sur la conformité aux SLA** :
Suivie par fournisseur et par engagement. Une conformité <70 % déclenche une revue de la performance du fournisseur.

---

## Critères d'acceptation

Les livrables externalisés ne sont pas acceptés ou déployés en production avant que tous les critères d'acceptation soient satisfaits.

**Liste de contrôle d'acceptation de sécurité** :

| N° | Critère | Vérifié par |
|----|---------|-------------|
| 1 | Tous les tests de sécurité contractuellement requis complétés et résultats fournis | Responsable développement |
| 2 | Aucune vulnérabilité Critique ou Élevée non résolue dans les résultats SAST, SCA, DAST ou de test d'intrusion | RSSI / Équipe sécurité |
| 3 | Revue de code indépendante de l'organisation complétée sans constatation bloquante | Responsable développement |
| 4 | SBOM fourni au format CycloneDX ou SPDX ; aucun composant avec des vulnérabilités Critiques ou Élevées non corrigées lorsque des correctifs sont disponibles ; les vulnérabilités sans correctifs nécessitent une acceptation documentée du risque avec contrôles compensatoires | Responsable développement |
| 5 | Aucun secret, identifiant ou donnée de test codé en dur présent dans le code livré | Équipe sécurité |
| 6 | Le code satisfait aux normes de codage sécurisé de l'organisation | Champion sécurité / Développeur senior |
| 7 | Toute la documentation livrée (architecture, spécifications API, guides de déploiement, configuration) | Responsable développement |
| 8 | Code source et tous les artefacts livrés dans le référentiel ou chez l'agent séquestre de l'organisation | Responsable développement |
| 9 | Exigences de protection des données satisfaites ; aucune donnée personnelle non autorisée conservée par le fournisseur | Délégué à la protection des données / RSSI |
| 10 | Licences et propriété intellectuelle confirmées conformément au contrat | Juridique / Achats |

*Les constatations bloquantes incluent* :
- Identifiants, clés API ou secrets codés en dur
- Vulnérabilités d'injection SQL (toute sévérité)
- Vulnérabilités de contournement d'authentification
- Failles d'autorisation permettant l'élévation de privilèges
- Utilisation d'algorithmes cryptographiquement compromis (MD5, SHA-1 à des fins de sécurité, DES, RC4)
- Exposition de données sensibles dans les journaux ou les messages d'erreur
- Absence de validation des entrées sur les données fournies par l'utilisateur
- Constatations SAST/DAST de sévérité Critique ou Élevée non traitées

**Validation de l'acceptation** :

| Risque applicatif | Validation requise |
|-------------------|-------------------|
| Risque élevé | RSSI + Responsable développement + Propriétaire de l'application |
| Risque moyen | Responsable développement + Propriétaire de l'application |
| Risque faible | Responsable développement |

Les enregistrements d'acceptation sont conservés pour la durée du cycle de vie de l'application plus 3 ans.

---

## Propriété intellectuelle et séquestre de code

**Propriété du code** :

L'accord de développement définit clairement la propriété de tous les produits du travail, y compris le code source, la documentation, les conceptions et la propriété intellectuelle associée.

Lorsque l'organisation commande un développement sur mesure, la position par défaut est que l'organisation détient tous les droits de propriété intellectuelle sur les livrables au paiement final ou à la livraison si le paiement est à la livraison, selon la première éventualité. Tout écart par rapport à la propriété totale est documenté, approuvé par le service juridique et le RSSI, et justifié par un besoin métier.

**Licences** :

Lorsque le transfert de propriété complet n'est pas possible (ex. le fournisseur conserve des droits sur des composants ou frameworks préexistants), l'accord précise :

- Une licence perpétuelle et irrévocable pour l'organisation d'utiliser, de modifier et de maintenir le logiciel livré.
- L'identification claire des composants appartenant au fournisseur par opposition aux composants appartenant à l'organisation.
- Les termes de licence pour tous les composants tiers et open source inclus dans le livrable.

**Séquestre de code** :

Pour les engagements avec des fournisseurs de Niveau 1 où l'organisation ne détient pas directement le code source, l'organisation établit un arrangement de séquestre de code avec un agent de séquestre indépendant (ex. Escode, Codekeeper ou équivalent).

**Exigences de l'arrangement de séquestre** :

| Exigence | Détail |
|----------|--------|
| **Fréquence de dépôt** | Code source déposé à chaque version majeure, ou au minimum trimestriellement |
| **Contenu du dépôt** | Code source complet, scripts de compilation, spécifications de l'environnement de compilation, documentation, dépendances et instructions de déploiement suffisants pour compiler et déployer le logiciel indépendamment |
| **Conditions de libération** | Insolvabilité du fournisseur, cessation d'activité, violation matérielle des obligations de maintenance, ou défaut de fourniture des services contractés |
| **Vérification** | Les dépôts de séquestre sont vérifiés annuellement par l'agent de séquestre (vérification de compilation — confirmation que le code déposé se compile et produit une version fonctionnelle) |

**Critères de vérification du dépôt de séquestre** :
- Le code source se compile sans erreurs en utilisant les instructions de compilation documentées
- Toutes les dépendances sont résolvables à partir de référentiels publics ou privés documentés
- Les spécifications de l'environnement de compilation incluent tous les outils, SDK et versions requis
- L'artefact de compilation résultant (exécutable, image conteneur, package déployable) peut être déployé dans un environnement de test
- Un test minimal réussit (l'application démarre, le point de terminaison de contrôle d'état répond)
- Aucun outil propriétaire du fournisseur uniquement requis pour le processus de compilation

Vérification réalisée annuellement par l'agent de séquestre. Un échec de vérification oblige le fournisseur à corriger le dépôt dans les 30 jours.

Lorsque l'organisation détient directement le code source dans ses propres référentiels, le séquestre de code n'est pas requis, mais l'organisation maintient ses propres sauvegardes vérifiées.

---

## Surveillance continue

L'organisation surveille en continu les activités de développement externalisé tout au long du cycle de vie de l'engagement.

**Activités de surveillance** :

| Activité | Fréquence | Responsable |
|----------|-----------|-------------|
| **Revue des rapports de tests de sécurité** | Par jalon ou livraison de sprint | Responsable développement |
| **Revue de progression et de qualité** | Toutes les 2 semaines ou par sprint (pour les engagements agiles) | Responsable développement / Chef de projet |
| **Revue de la posture de sécurité du fournisseur** | Annuellement (Niveau 1) ; biennalement (Niveau 2) ; au renouvellement (Niveau 3) | RSSI / Responsable de la sécurité de l'information |
| **Revue des accès** | Trimestrielle — vérifier que le personnel du fournisseur avec un accès actif en a toujours besoin | IT Opérations / Responsable développement |
| **Contrôle de conformité ponctuel** | Semestriel — vérifier l'adhésion du fournisseur aux normes de codage sécurisé | Équipe sécurité |
| **Revue des incidents et quasi-accidents** | Par occurrence | RSSI |

Le tableau de bord de performance du fournisseur est maintenu trimestriellement, suivant : la conformité aux tests de sécurité, la conformité aux SLA, le nombre d'incidents et les constatations d'audit. Les résultats sont communiqués annuellement à la direction.

**Déclencheurs d'escalade** :

| Déclencheur | Action |
|-------------|--------|
| Le fournisseur ne fournit pas les résultats des tests de sécurité dans le délai convenu | Escalade au responsable développement ; blocage de l'acceptation |
| Vulnérabilité critique identifiée dans le code livré par le fournisseur | Escalade au RSSI ; remédiation du fournisseur dans les 7 jours |
| Incident de sécurité du fournisseur affectant les données ou systèmes de l'organisation | Activation du processus de gestion des incidents (A.5.24-28) ; notification au RSSI dans l'heure |
| Le fournisseur échoue à la réévaluation annuelle de sécurité | Suspension des nouvelles attributions de travail ; plan de remédiation dans les 30 jours ; révision du contrat |
| Preuves de sous-traitance non autorisée | Escalade au RSSI et au service juridique ; révision du contrat |

---

## Réponse aux incidents de sécurité des fournisseurs

Lorsqu'un fournisseur fait l'objet d'un incident de sécurité affectant l'engagement de l'organisation :

**Obligation de notification du fournisseur** :
- **Dans les 24 heures** : Notification initiale de la survenance, de la nature et de l'impact potentiel de l'incident
- **Dans les 72 heures** : Rapport d'incident détaillé incluant le périmètre, l'analyse des causes racines (préliminaire), les systèmes/données affectés et les actions de remédiation

**Réponse de l'organisation** :

| Type d'incident | Action de réponse |
|-----------------|------------------|
| **Compromission du référentiel de code du fournisseur** | 1. Suspendre l'accès du fournisseur aux systèmes de l'organisation 2. Revue forensique de tout le code livré par le fournisseur 3. Tests de sécurité complets avant toute autre acceptation 4. Envisager la réécriture du code si un code malveillant est suspecté |
| **Vol d'identifiants du personnel du fournisseur** | 1. Révoquer immédiatement tous les identifiants d'accès du fournisseur 2. Examiner les journaux d'accès pour détecter une activité non autorisée 3. Réémettre les identifiants après confirmation par le fournisseur de la remédiation de la compromission 4. AMF obligatoire pour le ré-accès |
| **Violation de données du fournisseur (données organisationnelles exposées)** | 1. Activer le processus de réponse aux incidents de l'organisation 2. Évaluer les exigences de notification à l'autorité de protection des données 3. Investigation conjointe de l'incident 4. Révision du contrat pour la responsabilité et les coûts de remédiation |
| **Compromission de la chaîne d'approvisionnement du fournisseur** | 1. Suspendre l'acceptation de tout livrable utilisant le composant affecté 2. Examiner le SBOM pour la dépendance affectée dans tous les travaux du fournisseur 3. Exiger que le fournisseur supprime/remplace le composant compromis 4. Re-test de sécurité indépendant |

Le RSSI notifie la direction générale dans les 24 heures suivant tout incident du fournisseur affectant les données ou systèmes organisationnels.

**Actions post-incident** :
- Le fournisseur doit fournir un rapport post-incident dans les 30 jours
- L'organisation réalise une réévaluation de la sécurité du fournisseur
- La continuation du contrat est conditionnelle à une remédiation satisfaisante
- Les incidents significatifs peuvent déclencher la clause de résiliation du contrat

---

## Exigences de protection des données

Lorsque le développement externalisé implique l'accès à des données personnelles ou à des systèmes traitant des données personnelles, des exigences supplémentaires de protection des données s'appliquent.

**Accord de traitement des données (ATD)** :

Conformément à l'art. 9 de la nLPD suisse, l'organisation conclut un ATD avec le fournisseur de développement qui couvre :

- Les catégories et types de données personnelles auxquels il est accédé.
- La finalité et la durée du traitement.
- L'obligation de traiter les données uniquement selon les instructions de l'organisation.
- Les obligations de confidentialité pour le personnel du fournisseur.
- Les mesures techniques et organisationnelles de sécurité mises en œuvre par le fournisseur.
- Les exigences de notification et d'approbation des sous-traitants ultérieurs.
- Les obligations d'assistance aux droits des personnes concernées.
- Le retour et la suppression des données à la résiliation du contrat.
- Les droits d'audit et d'inspection.

**Transferts transfrontaliers** :

Lorsque le développement du fournisseur s'effectue en dehors de la Suisse :

- Une évaluation d'impact du transfert est réalisée conformément aux exigences de la nLPD suisse.
- Des garanties appropriées sont en place (ex. Clauses contractuelles types, décisions d'adéquation du Conseil fédéral, ou règles d'entreprise contraignantes).
- Lorsque le fournisseur traite des données de personnes dans l'UE/EEE, les exigences du Chapitre V du RGPD en matière de transfert doivent également être satisfaites.

**Minimisation des données pour le développement** :

- Les fournisseurs ne reçoivent pas de données personnelles de production à des fins de développement ou de test.
- Lorsque des données réalistes sont requises, des données assainies, anonymisées ou pseudonymisées sont utilisées.
- Les données synthétiques (générées artificiellement) constituent l'approche privilégiée.
- Toute utilisation de données personnelles transformées est documentée et approuvée par le délégué à la protection des données ou le RSSI.

**Approches de génération de données synthétiques** :
- **Bibliothèques Faker** : Données réalistes mais fictives (noms, adresses, courriels) — adaptées aux tests d'interface, au développement de rapports
- **Outils de masquage de données** : Conserver la structure des données et l'intégrité référentielle tout en obscurcissant les valeurs — adaptés aux tests de schémas complexes
- **Génération basée sur des règles** : Générer des données correspondant aux schémas et distributions de production — adaptées aux tests de performance
- **Données générées par l'IA** : Modèles d'apprentissage automatique entraînés sur des données de production pour générer des ensembles de données synthétiques statistiquement similaires — adaptés au développement analytique

Exemples d'outils : Faker (Python/JavaScript), Mockaroo (web), Tonic.ai, Gretel.ai (entreprise)

Lorsqu'il est absolument nécessaire d'utiliser des données de production (relations de données complexes, cas limites rares), les données doivent être :
1. Sous-ensemblées au minimum d'enregistrements requis (pas un dump complet de la production)
2. Anonymisées ou pseudonymisées conformément à l'art. 5 de la nLPD
3. Approuvées par le délégué à la protection des données avec justification documentée
4. Chiffrées au repos et en transit vers l'environnement du fournisseur
5. Supprimées des systèmes du fournisseur dans les 30 jours suivant la complétion du développement

**Notification au Préposé fédéral à la protection des données et à la transparence (PFPDT)** :

Lorsqu'un incident de sécurité du fournisseur entraîne un risque élevé pour les personnes concernées (art. 24 de la nLPD), l'organisation notifie le PFPDT sans délai injustifié. Les indicateurs de risque élevé incluent :
- Accès non autorisé aux catégories particulières de données personnelles (art. 5 al. 2)
- Violation de données affectant >500 résidents suisses
- Compromission de données personnelles sensibles (santé, financières, biométriques)
- Incident impliquant du profilage systématique ou des données de prise de décision automatisée

L'ATD du fournisseur doit exiger que le fournisseur fournisse toutes les informations nécessaires à la notification au PFPDT dans les 48 heures suivant la découverte de l'incident.

---

## Définitions

| Terme | Définition |
|-------|------------|
| **Tests d'acceptation** | Vérification formelle qu'un livrable satisfait aux exigences spécifiées avant le déploiement |
| **Séquestre de code** | Arrangement par lequel le code source est déposé chez un tiers indépendant en vue d'être remis à l'organisation dans des conditions spécifiées |
| **DAST** | Analyse dynamique de la sécurité applicative (Dynamic Application Security Testing) — analyse les applications en cours d'exécution pour détecter les vulnérabilités de sécurité |
| **ATD** | Accord de traitement des données — contrat régissant la manière dont un sous-traitant gère les données personnelles pour le compte d'un responsable du traitement |
| **SAST** | Analyse statique de la sécurité applicative (Static Application Security Testing) — analyse le code source pour détecter les vulnérabilités de sécurité sans exécuter le code |
| **SBOM** | Catalogue de composants logiciels (Software Bill of Materials) — inventaire de tous les composants logiciels, dépendances et leurs versions |
| **SCA** | Analyse de la composition logicielle (Software Composition Analysis) — identifie les vulnérabilités et les problèmes de licence dans les dépendances tierces et open source |
| **Sous-traitant ultérieur** | Tiers engagé par le sous-traitant (fournisseur) pour traiter des données personnelles pour le compte du responsable du traitement (organisation) |
| **Attaque de la chaîne d'approvisionnement** | Compromission d'un composant logiciel, d'une dépendance ou d'un outil de développement pour injecter du code malveillant ou des vulnérabilités dans les systèmes en aval |
| **Fournisseur de Niveau 1/2/3** | Classification des risques des fournisseurs basée sur la sensibilité des systèmes développés et des données auxquelles il est accédé |

---

## Rôles et responsabilités

| Rôle | Responsabilités |
|------|----------------|
| **RSSI** | Propriété de la politique ; approbation de l'évaluation de sécurité des fournisseurs de Niveau 1 ; validation de l'acceptation pour les applications à risque élevé ; approbation des exceptions ; autorité d'escalade ; révision annuelle de la politique |
| **Responsable développement** | Coordination de l'engagement des fournisseurs ; communication des exigences de sécurité ; gestion de la revue de code et de l'acceptation ; surveillance des livrables des fournisseurs ; communication de la conformité |
| **Responsable de la sécurité de l'information** | Gestion des questionnaires de sécurité des fournisseurs ; contrôles de conformité ponctuels ; surveillance de la posture de sécurité des fournisseurs ; coordination des investigations d'incidents |
| **Chef de projet** | Gestion quotidienne de la relation avec le fournisseur ; suivi des jalons de livraison ; escalade des problèmes de sécurité au responsable développement |
| **Délégué à la protection des données / RSSI** | Revue et approbation des ATD ; évaluations des transferts transfrontaliers ; vérification de la minimisation des données ; coordination des droits des personnes concernées |
| **Juridique / Achats** | Rédaction et revue des contrats ; conditions de PI et de licences ; gestion des NDA ; vérification des assurances ; coordination des arrangements de séquestre |
| **Équipe sécurité** | Tests de sécurité indépendants des livrables des fournisseurs ; coordination des tests d'intrusion ; exécution SAST/DAST/SCA ; triage des vulnérabilités |
| **IT Opérations** | Provisionnement et déprovisionnement des accès des fournisseurs ; soutien des revues d'accès ; cloisonnement des environnements pour l'accès des fournisseurs |
| **Propriétaire de l'application** | Initiation des exigences de sécurité ; validation de l'acceptation ; demandes d'exceptions ; budget pour les tests de sécurité |

---

## Preuves

Les preuves suivantes démontrent la conformité à cette politique :

| N° | Preuve | Responsable | Fréquence | Conservation |
|----|--------|-------------|-----------|-------------|
| 1 | **Enregistrements d'évaluation de sécurité des fournisseurs** (questionnaires, rapports d'audit, preuves de certification, décisions d'évaluation) | RSSI / Responsable de la sécurité de l'information | Par engagement + réévaluation annuelle (Niveau 1) | Durée de la relation + 3 ans |
| 2 | **Contrats de développement avec clauses de sécurité** (accords signés, ATD, NDA, arrangements de séquestre) | Juridique / Achats | Par engagement | Durée du contrat + 7 ans |
| 3 | **Rapports de tests de sécurité du fournisseur** (résultats SAST, SCA, DAST fournis par le fournisseur par jalon) | Responsable développement | Par jalon ou livraison de sprint | Cycle de vie de l'application + 3 ans |
| 4 | **Résultats des tests indépendants de l'organisation** (revue de code interne, SAST/SCA/DAST indépendants, rapports de tests d'intrusion) | Équipe sécurité / RSSI | Par acceptation | Cycle de vie de l'application + 3 ans |
| 5 | **Enregistrements de validation de l'acceptation** (liste de contrôle d'acceptation de sécurité, validation avec date, approbateur, conditions) | Responsable développement | Par livrable | Cycle de vie de l'application + 3 ans |
| 6 | **Enregistrements d'accès des fournisseurs** (attributions d'accès, revues trimestrielles, confirmations de déprovisionnement) | IT Opérations / Responsable développement | Par événement d'accès ; revues trimestrielles | Durée de la relation + 3 ans |
| 7 | **Enregistrements SBOM** (catalogue de composants logiciels pour chaque livrable accepté) | Responsable développement | Par livrable | Cycle de vie de l'application + 3 ans |
| 8 | **Enregistrements de dépôt et de vérification du séquestre de code** (confirmations de dépôt, résultats de vérification de compilation annuels) | Juridique / Responsable développement | Par dépôt + vérification annuelle | Durée du contrat + 3 ans |
| 9 | **Suivi de la remédiation des vulnérabilités** (enregistrements de remédiation du fournisseur, conformité aux SLA, preuves de clôture) | Responsable développement / Équipe sécurité | Par vulnérabilité | 3 ans |
| 10 | **Enregistrements de surveillance des fournisseurs** (revues de progression, contrôles de conformité ponctuels, enregistrements d'escalade) | Responsable développement / RSSI | Par cycle de revue | Durée de la relation + 3 ans |
| 11 | **Enregistrements de protection des données** (ATD, évaluations d'impact des transferts, approbations de minimisation des données) | Délégué à la protection des données / RSSI | Par engagement | Durée du contrat + 10 ans (nLPD) |
| 12 | **Registre des exceptions** (demandes d'exceptions, approbations, contrôles compensatoires, revues trimestrielles) | Responsable de la sécurité de l'information | Par exception ; révisé trimestriellement | Durée de l'exception + 3 ans |

---

# Conformité à la politique

## Mesure de la conformité

L'équipe de management de la sécurité de l'information vérifie la conformité à cette politique par diverses méthodes, notamment les enregistrements d'évaluation de sécurité des fournisseurs, les audits des clauses contractuelles, les rapports de tests de sécurité, les enregistrements d'acceptation, les revues d'accès, les audits internes et externes, et les retours au propriétaire de la politique.

**Indicateurs de conformité** :

| Indicateur | Cible | Fréquence de mesure |
|------------|-------|---------------------|
| Engagements de fournisseurs avec évaluation de sécurité complétée avant signature du contrat | 100 % | Par engagement |
| Contrats de développement contenant toutes les clauses de sécurité obligatoires | 100 % | Par engagement |
| Livrables externalisés avec tests de sécurité indépendants de l'organisation avant acceptation | 100 % | Par livrable |
| Vulnérabilités signalées par les fournisseurs remédiées dans les SLA | >= 90 % | Trimestriel |
| Revues des accès des fournisseurs complétées selon le calendrier | 100 % | Trimestriel |
| Fournisseurs de Niveau 1 avec réévaluation de sécurité à jour (dans les 12 mois) | 100 % | Annuel |
| Dépôts de séquestre de code à jour (selon la fréquence convenue) | 100 % | Par calendrier de dépôt |

**Traitement de la non-conformité** : En dessous de 70 % sur tout indicateur, escalade immédiate vers le RSSI et plan de remédiation requis. Entre 70 et 89 %, supervision du Responsable de la sécurité de l'information avec revue mensuelle jusqu'au rétablissement. À 90 % et au-dessus, surveillance trimestrielle standard.

## Exceptions

Toute exception à cette politique doit être approuvée et enregistrée à l'avance par le Responsable de la sécurité de l'information, avec acceptation documentée du risque, contrôles compensatoires et date de révision définie (maximum 12 mois). Les exceptions sont communiquées à l'équipe de revue de direction.

## Non-conformité

Tout employé reconnu coupable d'avoir violé cette politique peut faire l'objet de mesures disciplinaires pouvant aller jusqu'au licenciement. La non-conformité du fournisseur est traitée par des recours contractuels, y compris la suspension ou la résiliation du contrat pour les violations matérielles de sécurité.

## Amélioration continue

Cette politique est révisée et mise à jour dans le cadre du processus d'amélioration continue. Les révisions tiennent compte des évolutions des pratiques d'externalisation et du paysage des menaces liées à la chaîne d'approvisionnement, des nouvelles techniques d'attaque de la chaîne d'approvisionnement logicielle (confusion de dépendances, typosquattage, compromission du pipeline CI/CD), des changements réglementaires affectant les accords de traitement des données et les transferts transfrontaliers, des mises à jour du cadre de gestion des fournisseurs, des constatations d'audit et des enseignements tirés des incidents de sécurité impliquant le développement externalisé.

---

## Liste de contrôle de mise en œuvre (pour les organisations qui débutent l'externalisation)

**Avant d'engager le premier fournisseur** :
- [ ] Modèle de questionnaire d'évaluation de la sécurité des fournisseurs créé
- [ ] Modèle de contrat standard de développement externalisé avec clauses de sécurité rédigé (revue juridique)
- [ ] Modèle d'ATD conforme à l'art. 9 de la nLPD préparé (revue du DPD)
- [ ] Normes de codage sécurisé documentées et publiées
- [ ] Outils SAST/SCA/DAST sélectionnés et opérationnels
- [ ] Modèle de liste de contrôle d'acceptation de sécurité créé
- [ ] Processus de provisionnement des accès fournisseurs documenté
- [ ] Agent de séquestre de code sélectionné (si applicable pour le Niveau 1)

**Par engagement** :
- [ ] Niveau du fournisseur déterminé et documenté
- [ ] Évaluation de sécurité complétée et approuvée
- [ ] Contrat avec clauses de sécurité signé
- [ ] ATD exécuté (si le fournisseur accède à des données personnelles)
- [ ] Package de développement sécurisé livré au fournisseur
- [ ] Vérifications des antécédents du personnel du fournisseur vérifiées (Niveau 1)
- [ ] Accès du fournisseur provisionné avec moindre privilège
- [ ] Cadence des tests de sécurité planifiée (revues de jalons/sprints)
- [ ] Critères d'acceptation communiqués au fournisseur
- [ ] Référentiel de code ou arrangement de séquestre établi

---

# Domaines de la norme ISO 27001 couverts

Politique de développement externalisé — Correspondance avec les contrôles ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership et engagement | 5.1 Politiques de sécurité de l'information |
| Clause 5.2 Politique | 5.4 Responsabilités de la direction |
| Clause 6.2 Objectifs de sécurité de l'information | 5.19 Sécurité de l'information dans les relations avec les fournisseurs |
| Clause 7.3 Sensibilisation | 5.20 Prise en compte de la sécurité de l'information dans les accords avec les fournisseurs |
| | 5.21 Gestion de la sécurité de l'information dans la chaîne d'approvisionnement des TIC |
| | 5.22 Surveillance, révision et gestion des changements des services des fournisseurs |
| | 5.36 Conformité aux politiques, règles et normes |
| | 6.3 Sensibilisation, formation et éducation à la sécurité de l'information |
| | 6.4 Processus disciplinaire |
| | 8.4 Accès au code source |
| | 8.25 Cycle de développement sécurisé |
| | 8.26 Exigences de sécurité des applications |
| | 8.28 Codage sécurisé |
| | 8.29 Tests de sécurité dans le développement et l'acceptation |
| | **8.30 Développement externalisé** |
| | 8.31 Séparation des environnements de développement, de test et de production |

**Cadre réglementaire et juridique** :

| Cadre | Pertinence |
|-------|-----------|
| nLPD suisse (revDSG) | Art. 8 — Mesures techniques et organisationnelles de protection des données ; Art. 9 — Traitement des données par des tiers (accords sous-traitants) |
| OPDo suisse (Ordonnance sur la protection des données) | Art. 1–3 — Exigences minimales en matière de sécurité des données |
| RGPD de l'UE (si applicable) | Art. 28 — Obligations du sous-traitant ; Art. 32 — Sécurité du traitement ; Chapitre V — Transferts transfrontaliers de données |
| ISO/IEC 27001:2022 | Contrôle Annexe A 8.30 — Développement externalisé |
| ISO/IEC 27002:2022 | Section 8.30 — Conseils de mise en œuvre pour le développement externalisé |
| NIST SP 800-53 Rév. 5 | SA-4 (Processus d'acquisition), SA-9 (Services de systèmes externes) |
| OWASP Top 10:2025 | A03 — Défaillances de la chaîne d'approvisionnement logicielle |
| CIS Controls v8 | 16.4 (Inventaire des composants logiciels tiers), 16.6 (Évaluation de la sévérité des vulnérabilités applicatives) |

---

<!-- QA_VERIFIED: 2026-03-29 -->
