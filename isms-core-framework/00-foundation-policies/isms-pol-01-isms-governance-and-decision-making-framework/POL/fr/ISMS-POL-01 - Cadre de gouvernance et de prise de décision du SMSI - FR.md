<!-- ISMS-CORE:POLICY:ISMS-POL-01-FR:framework:POL:01 -->
**ISMS-POL-01 — Cadre de gouvernance et de prise de décision du SMSI**

---

## Contrôle du document

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Cadre de gouvernance et de prise de décision du SMSI |
| **Type de document** | Politique |
| **Identifiant du document** | ISMS-POL-01 |
| **Créateur du document** | Responsable de la Sécurité des Systèmes d'Information (RSSI) |
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
| 1.0 | [Date - 4 semaines] | RSSI | Brouillon initial — cadre de délimitation de la gouvernance |

**Cycle de révision** : Annuel (ou lors de modifications significatives du SMSI)
**Prochaine date de révision** : [Date d'entrée en vigueur + 12 mois]

**Chaîne d'approbation** :

- Principale : Responsable de la Sécurité des Systèmes d'Information (RSSI)
- Secondaire : Responsable juridique/conformité
- Autorité finale : Direction générale

**Documents connexes** :

- ISMS-POL-00 (Cadre d'applicabilité réglementaire)
- ISMS-POL-A.5.1 (Politiques de sécurité de l'information)
- Déclaration d'applicabilité (SoA)
- Plan de traitement des risques (ISO 27001 Clause 6.1.3)
- Registre d'acceptation des risques (Clause 6.1.3d)
- ISO 27001:2022 Clause 4.1 (Compréhension de l'organisation et de son contexte)
- ISO 27001:2022 Clause 5.3 (Rôles, responsabilités et autorités)
- ISO 27001:2022 Clause 6.1.3 (Traitement des risques liés à la sécurité de l'information)
- ISO 27001:2022 Clause 7.5.3 (Maîtrise des informations documentées)
- ISO 27001:2022 Clause 9.2 (Audit interne)
- ISO 27001:2022 Clause 9.3 (Revue de direction)
- ISO 27001:2022 Clause 10.2 (Non-conformité et actions correctives)

**Distribution** : Toutes les parties prenantes du SMSI, auteurs de politiques, propriétaires de systèmes, auditeurs internes/externes
**Référencé par** : Tous les documents de politique du SMSI, Déclaration d'applicabilité, Plan de traitement des risques

## Résumé exécutif

Cette politique établit **où le jugement professionnel est exercé** dans le Système de Management de la Sécurité de l'Information (SMSI) de l'organisation, en garantissant que :

- **Les décisions de conception du modèle sont documentées et autorisées** (interprétation des contrôles, applicabilité réglementaire, acceptation des risques)
- **L'autorité décisionnelle est clairement attribuée** (compétences et périmètre du RSSI, du responsable juridique/conformité et de la Direction générale)
- **Les critères de conformité évoluent par des processus maîtrisés** (modifications réglementaires, évolution des menaces, retours d'audit)
- **La vérification par audit est objective et fondée sur des preuves** (les auditeurs vérifient la conception documentée, ils ne réinterprètent pas les exigences)

**Objet** : Permettre une **vérification objective par audit** en déplaçant le jugement professionnel vers la **phase de conception du modèle** (politiques documentées, évaluations des risques, décisions d'applicabilité) plutôt que vers la **phase de discussion d'audit** (interprétation subjective lors de la certification).

**Périmètre** : Toute l'autorité décisionnelle du SMSI, les déterminations d'applicabilité réglementaire, la gestion des exceptions de contrôles, l'évolution des critères de conformité et les processus de revue de gouvernance.

**Principe clé** : **La certification ISO 27001 requiert un jugement professionnel à deux stades :**

1. **Conception du modèle** (responsabilité de l'organisation) : Interpréter ISO 27001 pour le contexte organisationnel, sélectionner les contrôles basés sur les risques, définir la suffisance des preuves
2. **Vérification du modèle** (responsabilité de l'auditeur) : Évaluer si l'interprétation organisationnelle satisfait ISO 27001, vérifier que la mise en œuvre correspond à la documentation

Cette politique documente le jugement professionnel organisationnel (Stade 1) pour permettre une vérification objective par audit (Stade 2).

---

### Référence rapide

| Je dois... | Aller à |
|---|---|
| Comprendre qui décide quoi | Section 2.1 (Délimitations d'autorité) |
| Vérifier les exigences de compétence d'un rôle | Section 2.3 (Exigences de compétence) |
| Déterminer l'applicabilité réglementaire | Section 3.1 (Applicabilité réglementaire) → POL-00 |
| Déterminer l'applicabilité d'un contrôle | Section 3.2 (Applicabilité des contrôles) → SoA |
| Gérer un désaccord avec un auditeur | Section 3.3 (Protocole de contestation d'applicabilité) |
| Traiter une exception de contrôle | Section 4.2 (Processus d'exception — 5 étapes) |
| Suivre le volume et l'état des exceptions | Section 4.4 (Surveillance du volume d'exceptions) |
| Gérer une modification des critères de conformité | Section 5.2 (Processus de modification — 6 étapes) |
| Suivre la réévaluation après une modification | Section 5.4 (Suivi des réévaluations) |
| Préparer la revue annuelle de gouvernance | Section 6.1 (Revue annuelle de gouvernance) |
| Enregistrer un retour d'expérience | Section 6.2 (Registre des retours d'expérience) |
| Préparer la documentation pour un audit | Section 9.1 (Documents fournis aux auditeurs) |

---

## Autorité de la politique et délimitations de gouvernance

### Objet et périmètre

Cette politique définit l'**autorité décisionnelle** pour la gouvernance du SMSI, en garantissant :

- Une attribution claire des responsabilités pour l'interprétation de la conformité
- Des processus documentés pour l'applicabilité, les exceptions et l'évolution
- Des exigences de compétence pour les décideurs
- Des critères objectifs pour la vérification par audit

**Cette politique établit :**

- Les délimitations d'autorité pour les décisions du SMSI (Section 2 : qui décide quoi, avec quelle compétence)
- L'autorité d'applicabilité réglementaire et des contrôles (Section 3 : qui détermine ce qui s'applique)
- Les processus de gestion des exceptions et d'acceptation des risques (Section 4 : comment sont gérés les contrôles ne pouvant être mis en œuvre)
- Le contrôle des modifications des critères de conformité (Section 5 : comment le modèle évolue dans le temps)
- La surveillance de l'efficacité de la gouvernance (Section 6 : comment la qualité de la gouvernance est évaluée)

**Cette politique N'ÉTABLIT PAS :**

- Les exigences spécifiques de mise en œuvre des contrôles (traitées dans les politiques de contrôle Annexe A : série ISMS-POL-A.X.XX)
- Les méthodologies d'évaluation des risques (traitées dans la Procédure d'évaluation des risques : Clause 6.1.2)
- Les procédures de maîtrise des documents (traitées dans la Procédure de maîtrise des documents : Clause 7.5.3)
- Le programme d'audit interne (traité dans la Procédure d'audit interne : Clause 9.2)

**Principe de délimitation** : Cette politique établit l'**autorité décisionnelle et les processus**. Les décisions elles-mêmes (quels contrôles, quelles réglementations, quels risques accepter) sont documentées dans **POL-00 (applicabilité réglementaire), SoA (applicabilité des contrôles) et le Registre d'acceptation des risques (décisions de traitement des risques)**.

**Intégration avec ISO 27001** :

- **Clause 4.1 (Contexte)** : Cette politique soutient la compréhension du contexte externe (comment les réglementations et normes sont interprétées pour le contexte organisationnel)
- **Clause 5.3 (Rôles et responsabilités)** : Formalise la structure d'autorité pour la prise de décision du SMSI
- **Clause 6.1.3 (Traitement des risques)** : Soutient la sélection de contrôles basée sur les risques, les contrôles alternatifs et l'autorité d'acceptation des risques
- **Clause 7.5.3 (Maîtrise des documents)** : Établit la gouvernance des modifications des critères de conformité
- **Clause 9.3 (Revue de direction)** : Fournit un cadre pour l'évaluation de l'efficacité de la gouvernance
- **Clause 10.1 (Amélioration continue)** : Permet l'amélioration des processus de gouvernance via les retours d'expérience

## Délimitations d'autorité et compétence

### Autorité décisionnelle

**Attribution de l'autorité** :

Les rôles suivants exercent l'autorité décisionnelle pour la gouvernance du SMSI. Chaque rôle opère dans un **domaine d'autorité** défini — ce sont des responsabilités fonctionnelles, non une hiérarchie de séniorité :

| Domaine d'autorité | Rôle | Périmètre de décision | Exigence de compétence |
|-------------------|------|----------------------|----------------------|
| **Sécurité technique** | Responsable de la Sécurité des Systèmes d'Information (RSSI) | Conception des contrôles techniques, faisabilité opérationnelle, suffisance des preuves, décisions de mise en œuvre au quotidien | Expertise en sécurité de l'information (CISSP/CISM ou équivalent, 5+ ans d'expérience), background technique, connaissance d'ISO 27001 |
| **Réglementaire et juridique** | Responsable juridique/conformité | Interprétation des exigences réglementaires, obligations contractuelles, évaluation des risques juridiques, déterminations de niveaux POL-00 | Formation juridique ou certification conformité, capacité de surveillance réglementaire, accès à un conseil juridique externe si nécessaire |
| **Protection des données** | Délégué à la Protection des Données (DPD) | Contrôles spécifiques à la vie privée (A.5.34, conformité RGPD/nLPD), droits des personnes concernées, analyses d'impact sur la vie privée. Le DPD exerce une autorité indépendante dans ce domaine conformément à l'Article 38.3 du RGPD et ne peut recevoir d'instructions concernant l'exercice de ces tâches. | Expertise RGPD/nLPD, certification de protection des données (CIPP/E ou équivalent), indépendance selon l'Article 38 du RGPD |
| **Stratégie et risques** | Direction générale (PDG/Conseil) | Décisions stratégiques sur les risques, allocation des ressources, acceptation des risques (Clause 6.1.3d), modifications du périmètre du SMSI, décisions majeures d'architecture | Responsabilité fiduciaire pour le risque organisationnel, responsabilité ultime de la certification ISO 27001, autorité budgétaire |

**Chemin d'escalade des décisions** :

1. **Décisions courantes** (mise en œuvre technique, format des preuves, conception des contrôles) :
   - **Autorité** : RSSI
   - **Documentation** : Documents POL/IMP, décisions de conception des contrôles
   - **Revue** : Audit interne (Clause 9.2), revue de direction annuelle (Clause 9.3)

2. **Interprétation réglementaire** (applicabilité des niveaux 1/2 POL-00, exigences de conformité contractuelle) :
   - **Autorité** : Responsable juridique/conformité (détermine l'applicabilité) + RSSI (met en œuvre les contrôles)
   - **Documentation** : POL-00 Section 8 (Matrice d'applicabilité réglementaire)
   - **Revue** : Surveillance trimestrielle (POL-00 Section 4.3), revue annuelle complète

3. **Acceptation des risques** (exclusion de contrôle sans alternative, acceptation du risque résiduel selon Clause 6.1.3d) :
   - **Autorité** : Le RSSI propose (avec évaluation des risques), la Direction générale approuve
   - **Documentation** : Registre d'acceptation des risques (exigence documentaire Clause 6.1.3d)
   - **Revue** : Revue de direction annuelle (Clause 9.3), mises à jour du plan de traitement des risques

4. **Modifications stratégiques** (extension du périmètre SMSI, changement majeur d'architecture de contrôles, changement d'organisme de certification) :
   - **Autorité** : Approbation de la Direction générale requise (le RSSI recommande, le PDG/Conseil décide)
   - **Documentation** : Comptes rendus de revue de direction (Clause 9.3.3), procès-verbaux du conseil si applicable
   - **Revue** : Dans le cadre du cycle de planification stratégique de l'organisation

**Exigences obligatoires** :

1. Le RSSI **doit** approuver toutes les mises en œuvre de contrôles techniques avant déploiement.
2. Le responsable juridique/conformité **doit** approuver toutes les déterminations d'applicabilité réglementaire (assignations de niveaux POL-00) avant publication ou mise à jour de POL-00.
3. La Direction générale **doit** approuver toutes les décisions d'acceptation des risques (exclusions de contrôles, acceptation du risque résiduel) conformément à la Clause 6.1.3d d'ISO 27001.
4. L'escalade des décisions **doit** suivre le chemin défini ci-dessus. Les décisions prises en dehors de l'autorité désignée nécessitent une approbation rétroactive ou une action corrective conformément à la Clause 10.2.

**Preuves de l'exercice de l'autorité** :

- **Contrôles techniques** : Signatures d'approbation sur les documents POL/IMP (section contrôle du document)
- **Applicabilité réglementaire** : Signatures d'approbation sur POL-00 Section 8 (Matrice d'applicabilité réglementaire)
- **Acceptation des risques** : Signature de la Direction générale sur les entrées du Registre d'acceptation des risques
- **Décisions stratégiques** : Comptes rendus de réunions de revue de direction (Clause 9.3) ou résolutions du conseil

### Jugement professionnel dans la certification ISO 27001

**La certification ISO 27001 requiert un jugement professionnel à deux stades distincts :**

**Stade 1 : Conception du modèle (responsabilité de l'organisation)**

Le jugement professionnel exercé par l'organisation comprend :

1. **Interprétation du contexte** (Clause 4.1) :
   - Déterminer quels facteurs externes (réglementations, menaces, pratiques sectorielles) sont pertinents pour le périmètre du SMSI
   - Évaluer les contraintes organisationnelles (ressources, architecture, appétit pour le risque)
   - Documenté dans : Document de contexte organisationnel, POL-00 (applicabilité réglementaire)

2. **Sélection des contrôles** (Clause 6.1.3) :
   - Sélectionner les contrôles en fonction de l'évaluation des risques (quels risques nécessitent quels contrôles)
   - Déterminer l'applicabilité des contrôles (applicable, non applicable, contrôle alternatif)
   - Décider de l'approche de mise en œuvre (architecture technique, processus opérationnels)
   - Documenté dans : Déclaration d'applicabilité (SoA), Plan de traitement des risques, documents POL/IMP de contrôle

3. **Suffisance des preuves** :
   - Définir quelles preuves démontrent l'efficacité des contrôles (classeurs Python, journaux, configurations)
   - Déterminer la fréquence des preuves (temps réel, quotidien, mensuel, trimestriel)
   - Établir les périodes de conservation des preuves (12 mois, 3 ans, cycle de certification)
   - Documenté dans : Documents IMP de contrôle (section preuves), conception des scripts Python

4. **Applicabilité réglementaire** (POL-00) :
   - Déterminer quelles réglementations s'appliquent à l'organisation (cadre Niveau 1/2/3)
   - Évaluer les déclencheurs des réglementations conditionnelles (applicabilité de DORA, NIS2, PCI DSS)
   - Décider quand une réévaluation est requise (surveillance trimestrielle, événements déclencheurs)
   - Documenté dans : POL-00 Section 8 (Matrice d'applicabilité réglementaire)

**Stade 2 : Vérification du modèle (responsabilité de l'auditeur)**

Le jugement professionnel exercé par l'auditeur comprend :

1. **Évaluation de la qualité des processus** :
   - La méthodologie d'évaluation des risques est-elle solide et appliquée de manière cohérente ? (Clause 6.1.2)
   - Les décisions de sélection des contrôles sont-elles raisonnables compte tenu du contexte organisationnel ? (Clause 6.1.3)
   - Les décideurs sont-ils compétents selon les exigences de compétence de la Section 2.1 ?
   - Les processus de gouvernance sont-ils documentés et suivis ? (cette politique)

2. **Alignement sur ISO 27001** :
   - L'interprétation organisationnelle des contrôles de l'Annexe A satisfait-elle les objectifs de contrôle d'ISO 27001 ?
   - Les exigences obligatoires sont-elles traitées ? (exigences des Clauses 4-10, informations documentées selon Clause 7.5)
   - La Déclaration d'applicabilité est-elle complète et justifiée ? (93 contrôles documentés)

3. **Efficacité de la mise en œuvre** (Stade 2) :
   - La mise en œuvre réelle correspond-elle à la conception documentée ? (chaîne POL → IMP → Python → Preuves)
   - Les preuves sont-elles suffisantes pour démontrer le fonctionnement des contrôles ? (complétude, actualité, traçabilité)
   - Les non-conformités et actions correctives sont-elles traitées de manière appropriée ? (Clause 10.2)

4. **Amélioration continue** :
   - Le SMSI évolue-t-il ? (constatations d'audit interne traitées, revue de direction efficace, retours d'expérience mis en œuvre)
   - Les modifications sont-elles maîtrisées ? (contrôle de version des documents, réévaluation après modifications)

**Principe de collaboration** :

Lorsque l'auditeur identifie des lacunes potentielles dans le jugement organisationnel (p. ex. l'interprétation d'un contrôle peut ne pas satisfaire pleinement l'objectif ISO 27001, les preuves peuvent être insuffisantes), la résolution suit le **Protocole de contestation d'applicabilité de la Section 3.3** : la discussion se concentre sur l'alignement des clauses ISO 27001 et le raisonnement documenté, non sur les préférences personnelles ou un conflit d'autorité.

**Résultat** : Le jugement de l'auditeur se concentre sur la **vérification de la qualité du jugement organisationnel**, non sur le **remplacement des décisions organisationnelles**. Si l'évaluation de l'auditeur identifie de véritables lacunes, l'organisation déclenche une action corrective conformément à la Clause 10.2 (Non-conformité et actions correctives).

### Exigences de compétence pour les décideurs

**Justification** : L'autorité sans compétence compromet la crédibilité de la gouvernance. Cette section établit les attentes minimales de compétence pour les rôles exerçant l'autorité décisionnelle du SMSI.

**Exigences de compétence** :

| **Rôle** | **Compétence minimale** | **Vérification** |
|----------|------------------------|-----------------|
| **RSSI** | Certification en sécurité de l'information (CISSP, CISM ou équivalent) — 5+ ans d'expérience en sécurité de l'information — Background technique (infrastructure, développement ou opérations de sécurité) — Connaissance d'ISO 27001 (formation ou expérience de mise en œuvre) | CV documentant l'expérience — Certifications professionnelles (en cours, non expirées) — Enregistrements de formation ISO 27001 (Lead Implementer ou équivalent) |
| **Responsable juridique/conformité** | Formation juridique (diplôme en droit ou certification conformité telle que CCEP, CRCM) — Capacité de surveillance réglementaire (bases de données juridiques, accès à un conseil externe) — Expérience de revue de contrats — Compréhension du périmètre et de l'applicabilité d'ISO 27001 | Certifications juridiques ou conformité — Enregistrements de recours à un conseil juridique externe (interprétations complexes) — Processus de surveillance réglementaire documenté (POL-00 Section 4.3) |
| **Délégué à la Protection des Données (DPD)** | Expertise RGPD/nLPD (CIPP/E, CIPM ou équivalent) — Indépendance vis-à-vis de la direction opérationnelle (selon l'Article 38.3 du RGPD) — Rattachement direct au niveau de direction le plus élevé — Compréhension des mesures techniques de protection des données | Certifications de protection des données (IAPP ou équivalent) — Organigramme montrant le rattachement hiérarchique (vérification de l'indépendance) — Enregistrements de formation RGPD/nLPD |
| **Direction générale** | Responsabilité fiduciaire pour le risque organisationnel (PDG, DAF, Conseil) — Compréhension des implications de la certification ISO 27001 — Autorité d'allocation du budget et des ressources — Responsabilité pour les décisions d'acceptation des risques | Vérification du rôle (contrat de travail, nomination au conseil) — Briefing exécutif ISO 27001 (enregistré dans la revue de direction) — Documentation de l'autorité budgétaire |

**Vérification de la compétence** :

- **Nomination initiale** : Compétence vérifiée avant que le rôle assume l'autorité décisionnelle du SMSI (enregistrements RH, vérification des accréditations)
- **Revue annuelle** : Compétence réévaluée annuellement lors de la revue de direction (Clause 9.3) — certifications en cours, formation à jour, conseil externe sollicité si nécessaire
- **Lacunes de compétence** : Si des lacunes sont identifiées → Traitées par la formation, le soutien externe (consultants, conseil juridique) ou la réaffectation de rôle

**Vérification par l'auditeur** :

Lors des audits de Phase 1 et Phase 2, l'auditeur peut demander :
- Des preuves de la compétence des décideurs (certifications, enregistrements de formation, documentation de l'expérience)
- La vérification que les décisions s'alignent sur l'autorité attribuée (p. ex. acceptations de risques approuvées par la Direction générale, non par le RSSI lui-même)
- L'évaluation de la compétence des décideurs dans la pratique (revue de la qualité des décisions dans les justifications SoA, évaluations des risques, déterminations réglementaires)

**Note** : Les exigences de compétence sont des **attentes minimales**, non des qualifications exhaustives. Les organisations peuvent les dépasser. La vérification de compétence démontre aux auditeurs que le jugement professionnel (Section 2.2) est exercé par des **individus qualifiés**, non de manière arbitraire.

## Autorité d'applicabilité de la conformité

### Applicabilité réglementaire

**Cadre** : L'applicabilité réglementaire est déterminée conformément à **ISMS-POL-00 (Cadre d'applicabilité réglementaire)**, qui établit :

- **Niveau 1 (Obligatoire)** : Obligations légales ou contractuelles (nLPD suisse, RGPD si applicable, ISO 27001:2022 pour la certification)
- **Niveau 2 (Conditionnel)** : Exigences s'appliquant uniquement lorsque des déclencheurs spécifiques sont remplis (DORA, NIS2, PCI DSS, FINMA, AI Act UE)
- **Niveau 3 (Informatif)** : Bonnes pratiques volontaires et orientations techniques (NIST SP 800, CIS Controls, OWASP)

**Autorité décisionnelle** :

1. **Détermination du niveau** : Le responsable juridique/conformité détermine l'applicabilité réglementaire selon la Section 5 de POL-00 (Processus d'évaluation)
2. **Mise en œuvre des contrôles** : Le RSSI met en œuvre les contrôles pour satisfaire les réglementations applicables
3. **Approbation** : La Direction générale approuve la Matrice d'applicabilité réglementaire de POL-00 annuellement (POL-00 Section 7 : Revue annuelle)

**Documentation** :

- **POL-00 Section 8.1** : Niveau 1 (Conformité obligatoire) — statut actuel et justification de l'applicabilité
- **POL-00 Section 8.2** : Niveau 2 (Applicabilité conditionnelle) — statut d'évaluation, déclencheurs, approche de surveillance
- **POL-00 Section 8.3** : Niveau 3 (Référence informative) — référentiels utilisés pour les orientations techniques

**Cycle de révision** :

- **Surveillance trimestrielle** (POL-00 Section 4.3) : Révision des modifications réglementaires et des événements déclencheurs organisationnels par le responsable juridique/conformité + RSSI
- **Revue annuelle complète** (POL-00 Section 7) : Approbation par la Direction générale des déterminations d'applicabilité réglementaire
- **Réévaluation déclenchée** (POL-00 Section 5) : Expansion métier, modifications réglementaires, exigences des contrats clients

**Vérification par l'auditeur** :

L'auditeur vérifie :
- La méthodologie d'évaluation de l'applicabilité est solide (le processus de la Section 5 de POL-00 est documenté et rationnel)
- Les déclencheurs de réévaluation sont surveillés (les journaux de surveillance trimestriels existent, les évaluations déclenchées sont documentées)
- Les déterminations de niveau sont raisonnables compte tenu du contexte organisationnel (p. ex. « Ne traite pas de cartes de paiement » → PCI DSS Niveau 2 Non applicable est justifié)

L'auditeur ne substitue PAS son jugement aux décisions d'applicabilité (l'organisation détermine les activités métier, l'auditeur vérifie la qualité du processus d'évaluation).

### Applicabilité des contrôles (Annexe A d'ISO 27001)

**Cadre** : L'applicabilité des contrôles est déterminée conformément à la **Clause 6.1.3 d'ISO 27001 (Traitement des risques)**, qui requiert :

- La sélection de contrôles basée sur les risques (contrôles sélectionnés pour traiter les risques identifiés selon l'évaluation des risques de la Clause 6.1.2)
- La documentation de la Déclaration d'applicabilité (SoA) (93 contrôles Annexe A documentés avec statut de mise en œuvre et justification)
- Les décisions de traitement des risques (mettre en œuvre le contrôle, contrôle alternatif, accepter le risque selon Clause 6.1.3d)

**Autorité décisionnelle** :

1. **Sélection des contrôles** : Le RSSI propose l'approche de mise en œuvre des contrôles basée sur l'évaluation des risques (Clause 6.1.2)
2. **Acceptation des risques** : La Direction générale approuve les exclusions de contrôles (lorsqu'un contrôle est « Non applicable » ou que le risque est accepté sans atténuation selon Clause 6.1.3d)
3. **Contrôles alternatifs** : Le RSSI détermine l'équivalence des contrôles alternatifs (atteindre le même objectif de contrôle ISO 27001 par des moyens différents)

**Documentation** :

- **Déclaration d'applicabilité (SoA)** : 93 contrôles documentés avec :
  - **Statut de mise en œuvre** : Applicable (mis en œuvre), Non applicable (exclusion justifiée), Contrôle alternatif (mise en œuvre différente atteignant le même objectif)
  - **Justification** : Justification technique/opérationnelle (pourquoi le contrôle s'applique, pourquoi exclu, ou pourquoi une alternative est utilisée)
  - **Référence** : Documents POL/IMP pour les contrôles mis en œuvre, évaluation des risques pour les exclusions
- **Plan de traitement des risques** (Clause 6.1.3) : Justification basée sur les risques pour la sélection, la priorité et le calendrier de mise en œuvre des contrôles
- **Registre d'acceptation des risques** (Clause 6.1.3d) : Approbation de la Direction générale pour les contrôles exclus sans atténuation alternative

**Critères de décision d'applicabilité des contrôles** :

| Statut | Critères | Exemple | Documentation requise |
|--------|----------|---------|----------------------|
| **Applicable** | Le risque existe, le contrôle atténue le risque, la mise en œuvre est faisable | A.8.15 (Journalisation) : L'organisation opère des serveurs, la journalisation est requise pour la détection des incidents | POL-A.8.15 + IMP-A.8.15 + Classeur Python |
| **Non applicable** | Le risque n'existe pas en raison du contexte organisationnel | A.8.23 (Filtrage web) : L'infrastructure de l'organisation est uniquement serveurs, pas de navigation web utilisateur | Justification SoA : « Aucun service de navigation web fourni aux utilisateurs, l'infrastructure est API/backend uniquement. L'objectif de contrôle (empêcher l'accès aux sites malveillants) n'est pas applicable. » + Évaluation des risques confirmant l'absence de risque de navigation web |
| **Contrôle alternatif** | Le contrôle standard n'est pas faisable, une alternative atteint le même objectif | A.7.4 (Surveillance physique) : Infrastructure en colocation, CCTV opéré par le prestataire selon contrat | Justification SoA : « Surveillance de la sécurité physique mise en œuvre via le contrat du prestataire de colocation (CCTV 24/7, rapports d'audit trimestriels). Atteint le même objectif (détecter les accès physiques non autorisés). » + Référence de la clause contractuelle |
| **Risque accepté** | Le risque existe, le contrôle n'est pas mis en œuvre, le risque résiduel est accepté par la Direction générale | A.8.11 (Masquage des données) : Données de production utilisées en développement (limitation technique), risque résiduel accepté avec contrôles compensatoires (restrictions d'accès, chiffrement) | Justification SoA : « Masquage des données non mis en œuvre en raison de [contrainte technique]. Risque résiduel accepté par la Direction générale [Date]. Contrôles compensatoires : A.5.18 (Droits d'accès restreints), A.8.24 (Chiffrement au repos). » + Entrée du Registre d'acceptation des risques avec signature de la Direction générale |

### Protocole de contestation d'applicabilité

**Objet** : Processus structuré pour résoudre les désaccords sur les déterminations d'applicabilité (assignations de niveaux réglementaires, exclusions de contrôles) entre l'organisation et l'auditeur.

**Quand ce protocole s'applique** :

- L'auditeur remet en question la détermination d'applicabilité réglementaire (p. ex. « Le RGPD est-il vraiment applicable compte tenu de votre base clients ? »)
- L'auditeur conteste l'exclusion d'un contrôle (p. ex. « Le contrôle A.8.15 est marqué Non applicable mais l'évaluation des risques montre une exigence de journalisation »)
- L'auditeur estime qu'un contrôle alternatif n'atteint pas l'objectif ISO 27001 (p. ex. « Le CCTV du prestataire de colocation peut ne pas satisfaire l'objectif du contrôle A.7.4 »)

**Étapes du protocole** :

**Étape 1 : L'auditeur soulève une préoccupation**

L'auditeur documente la préoccupation spécifique :
- Quelle détermination d'applicabilité est remise en question ? (assignation de niveau POL-00, statut de contrôle SoA)
- Quels éléments suggèrent que la détermination peut être incorrecte ? (informations contradictoires, risque non traité)
- Quelle exigence ISO 27001 ou quel objectif de contrôle est potentiellement non satisfait ?

**Étape 2 : L'organisation fournit la documentation**

L'organisation fournit la justification documentée :

- **Pour l'applicabilité réglementaire** (contestation de niveau POL-00) :
  - Évaluation selon la Section 5 de POL-00 (méthodologie suivie)
  - Évaluation des déclencheurs (critères objectifs évalués)
  - Enregistrement d'approbation (validation du responsable juridique/conformité + Direction générale)
  - Preuves à l'appui (p. ex. accords de traitement des données clients confirmant l'absence de données personnelles UE → RGPD Non applicable)
- **Pour l'exclusion de contrôle** (SoA « Non applicable ») :
  - Évaluation des risques montrant pourquoi le risque n'existe pas (Clause 6.1.2)
  - Justification SoA (justification technique/opérationnelle)
  - Documentation du contexte organisationnel (Clause 4.1 — p. ex. architecture d'infrastructure confirmant l'absence de capacité de navigation web)
- **Pour le contrôle alternatif** :
  - Correspondance des objectifs de contrôle (objectif Annexe A ISO 27001 → mise en œuvre alternative)
  - Preuves d'efficacité (le contrôle alternatif fonctionne et atteint l'objectif)
  - Enregistrement d'approbation (approbation du RSSI pour l'approche alternative)

**Étape 3 : Évaluation collaborative**

L'organisation et l'auditeur évaluent :

1. **La justification documentée est-elle raisonnable compte tenu du contexte organisationnel ?**
   - La justification s'aligne-t-elle sur la Clause 4.1 d'ISO 27001 (compréhension du contexte) ?
   - La décision est-elle documentée et approuvée selon les délimitations d'autorité de la Section 2.1 ?
2. **Existe-t-il des preuves contradictoires ?**
   - L'organisation affirme « pas de données UE » mais la politique de confidentialité mentionne le RGPD ?
   - La SoA affirme « pas d'exigence de journalisation » mais le plan de réponse aux incidents référence des journaux ?
3. **L'interprétation satisfait-elle les exigences ISO 27001 ?**
   - Si le contrôle est exclu, l'objectif de contrôle ISO 27001 est-il réellement non applicable ?
   - Si un contrôle alternatif est utilisé, atteint-il le même résultat de sécurité ?

**Étape 4 : Résolution**

**Résultat A : L'auditeur accepte la justification**
- La justification documentée est raisonnable et étayée par des preuves
- Il n'existe pas d'informations contradictoires
- Les exigences ISO 27001 sont satisfaites
- **Résultat** : La détermination d'applicabilité est maintenue, aucune constatation n'est émise

**Résultat B : L'organisation reconnaît une lacune**
- L'auditeur fournit la clause ISO 27001 ou l'objectif de contrôle spécifique non satisfait
- L'organisation examine et convient que la détermination était incorrecte ou insuffisante
- **Résultat** : L'organisation déclenche une action corrective conformément à la Clause 10.2 d'ISO 27001 :
  - Analyse des causes profondes (pourquoi l'applicabilité a-t-elle été incorrectement déterminée ?)
  - Remédiation (mise à jour de POL-00, SoA, mise en œuvre du contrôle manquant, ou réévaluation du risque)
  - Vérification (l'audit interne confirme la correction mise en œuvre)
  - Calendrier (plan d'action corrective avec date cible d'achèvement)

**Résultat C : Le désaccord persiste**
- L'organisation maintient que la justification est solide, l'auditeur maintient que la préoccupation est valide
- Les deux parties ont un raisonnement documenté
- **Résultat** : Escalade à la revue technique de l'organisme de certification :
  - L'organisation fournit : Justification documentée, argument d'alignement sur la clause ISO 27001, preuves étayant la détermination
  - L'auditeur fournit : Préoccupation spécifique, exigence ISO 27001 potentiellement non satisfaite, interprétation alternative
  - Organisme de certification : Examine les deux positions, émet une décision technique
  - Organisation : Accepte la décision (si défavorable à l'organisation → déclenche une action corrective selon le Résultat B)

**Principes** :

- **Fondé sur les preuves** : Les désaccords sont résolus par un raisonnement documenté et une référence ISO 27001, non par l'autorité ou la séniorité
- **Collaboratif** : L'objectif est une compréhension commune des exigences ISO 27001, non un débat contradictoire
- **Proportionné** : Les clarifications mineures sont traitées à l'Étape 2 (échange de documentation), les lacunes majeures s'escaladent via un processus formel
- **Orienté amélioration** : Si la détermination d'applicabilité était réellement incorrecte, l'organisation apprend et s'améliore (Clause 10.1 amélioration continue)

## Gestion des exceptions et acceptation des risques

### Scénarios d'exception

**Définition** : Une exception survient lorsqu'un contrôle de l'Annexe A d'ISO 27001 ne peut pas être mis en œuvre comme documenté dans la politique de contrôle (POL-A.X.XX), nécessitant une approche alternative ou une acceptation du risque.

**Scénarios d'exception courants** :

| Scénario | Description | Exemple | Voie de résolution |
|----------|-------------|---------|-------------------|
| **Infaisabilité technique** | Le contrôle suppose une technologie/architecture absente de l'organisation | A.8.22 (Segmentation réseau) : L'infrastructure est un réseau plat unique par décision de conception | Contrôle alternatif : Mettre en œuvre l'isolation basée sur l'hôte, contrôles d'accès au niveau applicatif |
| **Coût disproportionné** | Le coût du contrôle dépasse la réduction du risque compte tenu de l'échelle organisationnelle | A.8.16 (Déploiement SIEM) : Infrastructure de 3 serveurs, la revue manuelle des journaux atteint le même objectif à moindre coût | Contrôle alternatif : Processus documenté de revue manuelle des journaux avec fréquence définie |
| **Risque déjà atténué** | Une mise en œuvre alternative atteint le même objectif de contrôle ISO 27001 | A.8.5 (MFA pour tous les comptes) : Les comptes de service utilisent une authentification par certificat (fonctionnellement équivalent au MFA) | Contrôle alternatif : Authentification par certificat documentée comme équivalent MFA |
| **Conflit réglementaire** | La mise en œuvre du contrôle violerait une exigence légale prioritaire (rare) | A.8.10 (Suppression des données) : Le RGPD exige la suppression, mais la loi suisse exige une conservation de 10 ans pour les dossiers financiers | Acceptation du risque : Documenter que l'obligation légale prévaut, mettre en œuvre la ségrégation des données pour minimiser le périmètre |
| **Contrainte de ressources** | L'organisation manque de capacité pour mettre en œuvre pleinement le contrôle (état temporaire) | A.6.3 (Formation annuelle de sécurité) : Programme de formation conçu mais pas encore dispensé à tout le personnel | Mise en œuvre différée : Contrôle planifié pour achèvement dans [délai], mesures provisoires documentées |

**Scénarios non valides d'exception** :
- « Nous n'étions pas au courant de cette exigence » → Lacune de formation, non exception (traiter par la sensibilisation)
- « C'est trop difficile » → Problème de planification des ressources, non exception (planifier la mise en œuvre ou accepter le risque formellement)
- « Notre précédent auditeur ne l'exigeait pas » → Variance d'interprétation d'audit, non exception (les exigences ISO 27001 n'ont pas changé)

### Processus d'exception

**Processus obligatoire** (conformément à la Clause 6.1.3 d'ISO 27001 — Traitement des risques) :

Toutes les exceptions **doivent** suivre ce processus en 5 étapes :

**Étape 1 : Documenter la raison**

Fournir une explication claire :
- **Explication technique** : Pourquoi le contrôle ne peut pas être mis en œuvre tel que rédigé (limitation technologique, contrainte d'architecture, incompatibilité opérationnelle)
- **Évaluation de l'impact** : Quel objectif de sécurité n'est pas pleinement atteint (quelle partie de l'objectif de contrôle ISO 27001 est affectée)
- **Justification du contexte** : Pourquoi cette limitation existe (décision métier, contrainte réglementaire, analyse coût-bénéfice)

Format de documentation : Formulaire de demande d'exception ou entrée de justification SoA

**Étape 2 : Évaluer le risque résiduel** (Clause 6.1.2 d'ISO 27001)

Quantifier le risque sans contrôle :
- **Probabilité** : Probabilité que la menace exploite la vulnérabilité (Faible/Moyen/Élevé ou échelle numérique selon la méthodologie de risque de l'organisation)
- **Impact** : Conséquence si la menace se matérialise (impact C/I/D, impact financier/réputationnel/opérationnel)
- **Niveau de risque résiduel** : Notation du risque combiné selon la méthodologie d'évaluation des risques de l'organisation
- **Comparaison avec l'appétit pour le risque** : Le risque résiduel est-il dans les limites de l'appétit pour le risque acceptable ? (selon les critères du plan de traitement des risques)

Documentation : Entrée d'évaluation des risques liée à l'exception, calcul du risque résiduel

**Étape 3 : Proposer une solution**

Sélectionner l'une des trois voies :

**Option A : Contrôle alternatif**
- Mettre en œuvre un contrôle différent atteignant le même objectif de contrôle ISO 27001
- Documenter : Correspondance des objectifs de contrôle (objectif Annexe A ISO 27001 → mise en œuvre alternative)
- Documenter : Preuves d'efficacité (comment le contrôle alternatif fonctionne et atteint l'objectif)
- Exemple : A.7.4 (Surveillance physique) → CCTV du prestataire de colocation au lieu de caméras auto-opérées

**Option B : Acceptation du risque** (Clause 6.1.3d d'ISO 27001)
- Accepter le risque résiduel sans atténuation supplémentaire
- Requiert : Le risque est dans les limites de l'appétit pour le risque ET approbation de la Direction générale
- Documenter : Justification de l'acceptation du risque, contrôles compensatoires (si applicable), calendrier de revue
- Exemple : A.8.11 (Masquage des données) non mis en œuvre, risque résiduel accepté avec contrôles d'accès comme mesure compensatoire

**Option C : Mise en œuvre différée**
- Contrôle planifié pour mise en œuvre future (exception temporaire)
- Requiert : Calendrier de mise en œuvre documenté, mesures provisoires définies, revue périodique
- Documenter : Date cible d'achèvement, atténuation provisoire du risque, suivi de l'avancement
- Exemple : A.6.3 (Formation sécurité) programme en développement, achèvement ciblé T2 2025, provisoire : emails de sensibilisation à la sécurité

**Étape 4 : Obtenir l'approbation** (selon les délimitations d'autorité de la Section 2.1)

Autorité requise selon la solution :

| Solution | Autorité d'approbation | Preuves requises |
|----------|----------------------|-----------------|
| **Contrôle alternatif** | RSSI | Correspondance des objectifs de contrôle, documentation d'efficacité, évaluation de faisabilité technique |
| **Acceptation du risque** | Direction générale (PDG/DAF) | Évaluation des risques montrant le risque résiduel, justification de l'acceptation, documentation des contrôles compensatoires |
| **Mise en œuvre différée** | RSSI (calendrier) + Direction générale (risque résiduel pendant la période de report) | Plan de mise en œuvre, mesures provisoires, engagement d'allocation des ressources |

Documentation : Signature d'approbation sur la demande d'exception ou entrée du Registre d'acceptation des risques

**Étape 5 : Documenter dans la Déclaration d'applicabilité**

Mettre à jour la SoA avec :
- **Statut du contrôle** : « Contrôle alternatif » ou « Risque accepté » ou « Mise en œuvre différée »
- **Justification** : Résumé des Étapes 1-3 (raison, risque, solution)
- **Approbation** : Référence à l'autorité d'approbation et à la date (Étape 4)
- **Revue** : Prochaine date de revue (annuelle minimum, ou selon le calendrier de mise en œuvre différée)

### Registre des exceptions

**Objet** : Suivi centralisé de toutes les exceptions à la mise en œuvre des contrôles.

**Tenu par** : RSSI (propriétaire), mis à jour au fur et à mesure du traitement des exceptions

**Contenu** :

| Champ | Description | Exemple |
|-------|-------------|---------|
| ID Exception | Identifiant unique | EXC-2025-001 |
| Contrôle | Référence de contrôle Annexe A | A.8.22 (Segmentation réseau) |
| Raison | Pourquoi l'exception est requise (Étape 1) | L'infrastructure est un réseau plat unique par conception |
| Risque résiduel | Niveau de risque sans contrôle (Étape 2) | Moyen (Probabilité : Faible, Impact : Élevé) |
| Solution | Contrôle alternatif / Acceptation du risque / Différé (Étape 3) | Contrôle alternatif : Politiques réseau Kubernetes |
| Approuvé par | Autorité selon Section 2.1 (Étape 4) | RSSI [Nom] |
| Date d'approbation | Date de l'approbation | 2025-01-15 |
| Date de revue | Prochaine date de revue de l'exception | 2026-01-15 (annuelle) |
| Statut | Ouvert / Résolu / Clôturé | Ouvert (contrôle alternatif mis en œuvre) |

**Cycle de révision** :
- **Trimestriel** : Le RSSI revoit les exceptions ouvertes, évalue si la résolution progresse (mises en œuvre différées sur la bonne voie)
- **Annuel** : Toutes les exceptions revues lors de la revue de direction (Section 6.1), évaluation de la tendance du volume d'exceptions

### Surveillance du volume d'exceptions

**Objet** : Le volume d'exceptions est un indicateur de santé de la gouvernance. Un volume élevé indique des problèmes systématiques (contraintes de ressources, inadéquation architecturale avec ISO 27001, attentes irréalistes vis-à-vis des contrôles).

**Indicateurs** :

| Indicateur | Cible | Seuil d'escalade | Action si seuil dépassé |
|-----------|--------|-----------------|------------------------|
| **Total exceptions** | <5 % des contrôles totaux (4-5 exceptions sur 93) | >10 % (10+ exceptions) | Revue par la Direction générale : Le périmètre SMSI est-il réaliste ? Les ressources sont-elles suffisantes ? L'architecture est-elle fondamentalement incompatible avec ISO 27001 ? |
| **Acceptations de risques** (sans contrôle alternatif) | <3 % des contrôles totaux (2-3 acceptations) | >5 % (5+ acceptations) | Réévaluation de l'appétit pour le risque : L'organisation accepte-t-elle trop de risque résiduel ? Le périmètre de certification devrait-il être réduit ? |
| **Mises en œuvre différées** | <2 % des contrôles totaux (1-2 reports) | >5 % (5+ reports) ou tout report en retard de >180 jours | Revue d'allocation des ressources : Les calendriers de mise en œuvre sont-ils réalistes ? Les reports deviennent-ils permanents (indiquant une acceptation de risque masquée) ? |
| **Exceptions en attente >90 jours** | 0 (toutes les exceptions résolues dans les 90 jours suivant l'identification) | Toute exception non résolue >90 jours sans extension approuvée | Escalade à la Direction générale : Pourquoi l'exception n'est-elle pas résolue ? S'agit-il d'un retard opérationnel ou d'un problème systématique ? |

## Contrôle des modifications des critères de conformité

### Déclencheurs de modification

**Déclencheurs de modification externes** :

| Catégorie de déclencheur | Description | Exemples | Méthode de détection |
|--------------------------|-------------|----------|---------------------|
| **Modifications réglementaires** | Nouvelles lois, réglementations ou orientations officielles affectant les exigences du SMSI | Actes d'exécution RGPD, amendements ISO 27001, mises à jour orientations nLPD, transposition nationale NIS2 | Surveillance trimestrielle POL-00 (Section 4.3), alertes du conseil juridique, abonnements aux autorités réglementaires |
| **Révisions de normes** | ISO 27001 ou normes connexes mises à jour (corrigenda, nouvelles versions) | ISO 27001:2022 → futur ISO 27001:202X potentiel, mises à jour orientations ISO 27002 | Surveillance des publications ISO, notifications des organismes de certification |
| **Modifications contractuelles** | Les contrats clients ajoutent de nouvelles exigences de sécurité ou obligations réglementaires | Un nouveau client exige SOC 2 Type II, extension du périmètre PCI DSS, modifications de SLA contractuel | Processus de revue des contrats (revue juridique + RSSI avant signature) |
| **Évolution du paysage des menaces** | De nouvelles classes d'attaques émergent nécessitant des mises à jour des contrôles | Rançongiciels ciblant les sauvegardes → A.8.13 (Sauvegarde) requiert des copies hors ligne/immuables | Surveillance du renseignement sur les menaces (A.5.7), analyse des tendances d'incidents, bulletins de sécurité sectoriels |
| **Modifications technologiques** | Changements d'infrastructure ou d'architecture affectant la mise en œuvre des contrôles | Migration cloud → A.5.23 (Services cloud) maintenant applicable | Processus de gestion des modifications TI, décisions du comité de revue d'architecture |

**Déclencheurs de modification internes** :

| Catégorie de déclencheur | Description | Exemples | Méthode de détection |
|--------------------------|-------------|----------|---------------------|
| **Constatations d'audit** | L'auditeur externe identifie une lacune de contrôle ou un problème d'interprétation | Constatation Phase 2 : « La conservation des journaux est insuffisante pour l'objectif A.8.15 » | Journal des constatations d'audit (Clause 10.2), revue du rapport d'audit |
| **Découvertes d'audit interne** | L'audit interne (Clause 9.2) identifie une non-conformité ou une opportunité d'amélioration | Audit interne : « Approbation d'exception sans signature de la Direction générale » | Rapports d'audit interne, registre des non-conformités |
| **Incidents de sécurité** | La réponse aux incidents révèle une faiblesse de contrôle nécessitant une mise à jour de politique/mise en œuvre | Incident : Attaque de phishing réussie → Fréquence de A.6.3 (Formation) augmentée | Processus de réponse aux incidents (A.5.24-28), retours d'expérience (Section 6.2) |
| **Revue de direction** | La revue de direction Clause 9.3 identifie une amélioration stratégique ou un changement d'appétit pour le risque | Revue de direction : « Accepter un risque résiduel plus élevé pour les contrôles à faible impact » | Comptes rendus de réunions de revue de direction (Clause 9.3.3), actions d'amélioration continue |
| **Amélioration continue** | Identification proactive de gains d'efficacité ou de mesures de sécurité renforcées | Proposition RSSI : « Automatiser l'analyse des journaux A.8.15 avec SIEM » | Réunions de revue du SMSI, évaluation technologique |

### Processus d'évaluation et de mise en œuvre des modifications

**Processus obligatoire en 6 étapes** :

**Étape 1 : Modification identifiée** — Événement déclencheur détecté ; entrée dans le Journal des déclencheurs de modification documentant la modification requise.

**Étape 2 : Impact évalué** — Évaluer le périmètre et les implications (quelles POL/IMP sont affectées, quelle lacune de conformité existe, quelle remédiation est requise, quel risque pendant la transition).

**Étape 3 : Proposition de modification documentée** — Formaliser la recommandation de modification : justification, contrôles affectés, plan de mise en œuvre, risque pendant la transition, plan de vérification.

**Étape 4 : Approbation obtenue** (selon les délimitations d'autorité de la Section 2.1) :

| Type de modification | Autorité d'approbation |
|---------------------|----------------------|
| **Modifications techniques** (mise en œuvre, format des preuves) | RSSI |
| **Modifications réglementaires** (changement de niveau 1/2) | RSSI + Responsable juridique/conformité (conjoint) |
| **Modifications stratégiques** (extension périmètre SMSI, changement majeur d'architecture) | Direction générale |
| **Modifications d'urgence** (vulnérabilité critique, délai réglementaire) | RSSI (mise en œuvre immédiate) + Direction générale (approbation rétroactive dans les 7 jours) |

**Étape 5 : Mise en œuvre exécutée** — Mettre à jour les documents POL/IMP, réévaluer les contrôles affectés par rapport aux nouvelles exigences, régénérer les preuves, mettre à jour le Journal des modifications (Section 5.3).

**Étape 6 : Vérification complétée** — Audit interne vérifiant les contrôles modifiés, clôture des lacunes, rapport à la revue de direction.

### Contrôle des versions et suivi des modifications

**Standard de versionnement** : Format `v[Majeur].[Mineur]`

| Type de modification | Incrément de version | Déclencheur |
|--------------------|---------------------|-------------|
| **Version majeure** | Incrémenter le numéro majeur, remettre le mineur à 0 | Modification significative des exigences affectant l'évaluation de conformité |
| **Version mineure** | Incrémenter le numéro mineur | Clarification, formatage ou modification non substantielle |

**Journal central des modifications du SMSI** : Source unique de vérité pour toutes les modifications des critères de conformité dans l'ensemble du SMSI. Contient : ID modification, date, déclencheur, politiques/contrôles affectés, résumé, justification, approbation, statut de vérification.

### Suivi des réévaluations

Lorsque les critères de conformité changent, les contrôles affectés doivent être réévalués dans les **90 jours** (extensibles à 180 jours avec approbation de la Direction générale pour les modifications complexes).

**Indicateurs de complétion des réévaluations** :

| Indicateur | Cible | Seuil d'escalade |
|-----------|--------|-----------------|
| **Taux de complétion des réévaluations** | >95 % dans les 90 jours | <80 % → Revue par la Direction générale |
| **Réévaluations en retard** | 0 éléments en retard de >90 jours | Tout élément en retard de >90 jours sans extension approuvée → Escalade |
| **Vérifications échouées** | <5 % | >10 % → Revue de processus |

## Surveillance de l'efficacité de la gouvernance

### Revue annuelle de gouvernance

**Fréquence** : Annuelle (alignée avec la Revue de direction Clause 9.3)
**Participants** : Direction générale, RSSI, Responsable juridique/conformité, Audit interne, Propriétaires de contrôles représentatifs

**Sujets de revue** (6 sujets) :

1. **Délimitations d'autorité** (Section 2.1) — Rôles clairement compris ? Processus d'escalade fonctionnels ? Compétence maintenue ?
2. **Cadre d'applicabilité** (Section 3) — POL-00 Niveau 1/2/3 efficace ? Déclencheurs de réglementations conditionnelles surveillés ? SoA suffisante ?
3. **Gestion des exceptions** (Section 4) — Volume d'exceptions dans les cibles ? Processus en 5 étapes suivi ? Acceptations de risques appropriées ?
4. **Gestion des modifications** (Section 5) — Taux de complétion des réévaluations > 95 % ? Modifications proactives vs réactives ?
5. **Retours d'audit** — Constatations liées à la gouvernance ? Protocole de contestation invoqué ? Résultats ?
6. **Efficacité de la gouvernance** — Processus efficaces ? Goulots d'étranglement bureaucratiques ? Opportunités de rationalisation ?

**Livrables** : Rapport de santé de la gouvernance, actions d'amélioration continue, mises à jour de politique si lacunes identifiées, compte rendu de la Revue de direction.

### Registre des retours d'expérience

**Objet** : Capturer les améliorations issues de l'exécution des processus de gouvernance, permettant une amélioration continue (Clause 10.1 d'ISO 27001).

**Tenu par** : RSSI (mises à jour trimestrielles ou lors de l'identification d'un retour d'expérience)

**Contenu** : Date — Événement — Leçon apprise — Action prise — Statut — Vérifié

## Intégration avec les processus du SMSI

Cette politique s'intègre avec :

- **Évaluation et traitement des risques (Clause 6)** : L'évaluation des risques informe la sélection des contrôles (SoA, Section 3.2) ; le traitement des risques documente les approches de mise en œuvre, les contrôles alternatifs (Section 4.2) et les acceptations de risques (Section 4.2 Option B)
- **Audit interne (Clause 9.2)** : Les programmes d'audit incluent la vérification de la conformité des processus de gouvernance (Sections 3, 4, 5) ; les audits pré-certification vérifient que la documentation de gouvernance est à jour
- **Revue de direction (Clause 9.3)** : Les contributions de gouvernance comprennent le résumé du journal des modifications, les constatations d'audit liées à la gouvernance, les retours d'expérience ; les décisions comprennent les approbations d'acceptation de risques, les modifications stratégiques, l'allocation des ressources
- **Non-conformité et actions correctives (Clause 10.2)** : Les non-conformités liées à la gouvernance (processus non suivi, lacune identifiée par audit, incident révélant une faiblesse de contrôle) déclenchent des analyses de causes profondes et des remédiations

## Preuves pour cette politique

**Preuves Phase 1 (Revue documentaire)** : Ce document de politique, signatures d'approbation, structure de gouvernance (Section 2.1), exigences de compétence (Section 2.3), processus d'exception en 5 étapes (Section 4.2), processus de gestion des modifications en 6 étapes (Section 5.2), processus de revue annuelle (Section 6.1).

**Preuves Phase 2 (Efficacité opérationnelle)** :
- **Délimitations d'autorité** : Enregistrements de vérification de compétence, preuves d'approbation des décisions
- **Autorité d'applicabilité** : Journaux de surveillance trimestriels POL-00, enregistrements d'évaluations déclenchées, SoA avec 93 justifications de contrôles
- **Gestion des exceptions** : Registre des exceptions avec processus en 5 étapes, Registre d'acceptation des risques avec signatures de la Direction générale
- **Gestion des modifications** : Journal des modifications du SMSI, évaluations d'impact, approbations, rapports d'audit interne vérifiant les contrôles modifiés
- **Efficacité de la gouvernance** : Comptes rendus de revue annuelle, rapport de santé de la gouvernance, registre des retours d'expérience

### Classeur d'évaluation de la conformité à la gouvernance

**ISMS-CHK-POL-01** — 20 exigences sur 5 domaines :
- **Domaine 1 : Délimitations d'autorité** (GOV-01 à GOV-04)
- **Domaine 2 : Décisions d'applicabilité** (GOV-05 à GOV-08)
- **Domaine 3 : Gestion des exceptions** (GOV-09 à GOV-12)
- **Domaine 4 : Gestion des modifications** (GOV-13 à GOV-16)
- **Domaine 5 : Revue de gouvernance** (GOV-17 à GOV-20)

**Fréquence** : Trimestrielle | **Script Python** : ISMS-SCR-CHK-POL-01.py

## Préparation des audits et package de documentation

**Documents fournis lors de l'audit Phase 1** : ISMS-POL-01, ISMS-POL-00, SoA, Plan de traitement des risques, Registre d'acceptation des risques, Document de contexte organisationnel, Journal des modifications du SMSI.

**Documents fournis lors de l'audit Phase 2** : Classeur d'évaluation de conformité à la gouvernance (ISMS-CHK-POL-01), Registre des exceptions, Journaux de surveillance trimestriels POL-00, Enregistrements d'évaluations déclenchées, Rapports d'audit interne, Comptes rendus de revue de direction, Rapport de revue annuelle de gouvernance, Registre des retours d'expérience, Enregistrements de vérification de compétence.

---

## Déclaration de clôture

Cette politique établit **où le jugement professionnel est exercé** dans le SMSI de l'organisation, permettant :

**Vérification objective par audit** : La conformité est évaluée par rapport aux décisions organisationnelles documentées (applicabilité réglementaire POL-00, justifications des contrôles SoA, Registre d'acceptation des risques), non à la discrétion de l'auditeur.

**Autorité décisionnelle claire** : Les rôles (RSSI, Responsable juridique/conformité, Direction générale) ont des délimitations d'autorité explicites avec des exigences de compétence.

**Évolution maîtrisée** : Les critères de conformité changent via un processus documenté en 6 étapes avec suivi des réévaluations, vérification et approbation — le modèle évolue, il ne stagne pas.

**Relation d'audit collaborative** : Le jugement de l'auditeur se concentre sur la vérification de la qualité du jugement organisationnel, non sur le remplacement des décisions organisationnelles.

---

**Ce que cette politique accomplit :**

✅ **Clarté** : Les critères de conformité sont explicites (POL-00, SoA, Plan de traitement des risques, politiques documentées)
✅ **Cohérence** : Les modifications sont maîtrisées (processus de modification Section 5, contrôle des versions, suivi des réévaluations)
✅ **Défendabilité** : Les décisions sont documentées et justifiées (signatures d'autorité, évaluations des risques, enregistrements d'approbation)
✅ **Auditabilité** : Les preuves démontrent que les processus de gouvernance sont suivis (évaluations trimestrielles, Registre des exceptions, Journal des modifications, revues annuelles)
✅ **Amélioration** : Les retours d'expérience et les revues de gouvernance permettent une amélioration continue (Clause 10.1)

---

**Le changement de paradigme :**

**SMSI traditionnel** : Jugement professionnel exercé lors de l'audit (l'auditeur interprète les exigences, l'organisation se défend après coup)

**Ce SMSI** : Jugement professionnel exercé lors de la conception du modèle (l'organisation documente l'interprétation, l'auditeur vérifie la qualité et l'alignement sur ISO 27001)

**Résultat** : L'audit devient une vérification objective de la conception documentée, non un concours d'interprétation subjective.

---

**Approbation et maintenance** : Cette politique est approuvée par la Direction générale et maintenue par le RSSI. Le cycle de révision est annuel, ou lors de modifications significatives du SMSI nécessitant des mises à jour des processus de gouvernance.

---

**FIN DE ISMS-POL-01-FR**

<!-- QA_VERIFIED: 2026-03-30 -->
