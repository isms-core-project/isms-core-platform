<!-- ISMS-CORE:POLICY:AI-POL-01-FR:ai:POL:01 -->
**AI-POL-01 — Cadre de gouvernance et de prise de décisions AIMS**

---

## Contrôle du document

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Cadre de gouvernance et de prise de décisions AIMS |
| **Type de document** | Politique |
| **ID du document** | AI-POL-01 |
| **Auteur du document** | Responsable de la Gouvernance IA (RGIA) / Responsable de la Sécurité des Systèmes d'Information (RSSI) |
| **Propriétaire du document** | Directeur Général (DG) |
| **Approuvé par** | Direction générale |
| **Date de création** | [Date] |
| **Version** | 1.0 |
| **Date de version** | [À définir] |
| **Classification** | Interne |
| **Statut** | Brouillon |
| **Version du produit AIMS** | 1.0 |

**Historique des versions** :

| Version | Date | Auteur | Modifications |
|---------|------|--------|--------------|
| 1.0 | [Date - 4 semaines] | RGIA | Brouillon initial — limites de gouvernance AIMS et cadre de prise de décisions |

**Cycle de révision** : Annuel (ou en cas de modifications significatives de l'AIMS ou de la réglementation)
**Date de prochaine révision** : [Date d'entrée en vigueur + 12 mois]

**Chaîne d'approbation** :

- Primaire : Responsable de la Gouvernance IA (ou RSSI désigné en l'absence d'une fonction dédiée à la gouvernance IA)
- Secondaire : Responsable de la Sécurité des Systèmes d'Information (RSSI)
- Conformité : Responsable Légal / Compliance
- Autorité finale : Direction générale

**Documents connexes** :

- AI-POL-00 (Cadre d'applicabilité réglementaire IA — référence croisée obligatoire)
- ISMS-POL-01 (Cadre de gouvernance et de prise de décisions ISMS — document de gouvernance parent)
- ISO/IEC 42001:2023 Clause 4.3 (Détermination du périmètre de l'AIMS)
- ISO/IEC 42001:2023 Clause 5.1 (Leadership et engagement)
- ISO/IEC 42001:2023 Clause 5.2 (Politique IA)
- ISO/IEC 42001:2023 Clause 5.3 (Rôles, responsabilités et autorités)
- ISO/IEC 42001:2023 Clause 9.2 (Audit interne)
- ISO/IEC 42001:2023 Clause 9.3 (Revue de direction)
- ISO/IEC 42001:2023 Clause 10.2 (Non-conformité et action corrective)

**Distribution** : Tous les parties prenantes AIMS, propriétaires de systèmes IA, responsables des risques IA, responsables conformité, auditeurs internes/externes
**Référencé par** : Tous les documents de politique AIMS, Déclaration d'Applicabilité (DDA) AIMS, Plan de traitement des risques IA

---

## Synthèse exécutive

La présente politique établit **le cadre dans lequel le jugement professionnel est exercé** au sein du Système de Management de l'IA (AIMS) de l'[organisation], en garantissant que :

- **Les décisions de conception AIMS sont documentées et autorisées** (interprétation des contrôles, applicabilité réglementaire, acceptation des risques IA)
- **L'autorité de prise de décisions est clairement attribuée** (RGIA, RSSI, Légal, Direction générale — compétence et périmètre)
- **Les critères AIMS évoluent par des processus contrôlés** (changements réglementaires, nouveaux standards, orientations des autorités, retours d'audit)
- **La vérification par les auditeurs est objective et fondée sur des preuves** (les auditeurs vérifient la conception documentée, sans réinterpréter les exigences)

**Objectif** : Permettre une **vérification d'audit objective** en déplaçant le jugement professionnel vers la **phase de conception AIMS** (politiques documentées, évaluations des risques, décisions d'applicabilité) plutôt que vers la **phase de discussion d'audit** (interprétation subjective lors de la certification).

**Périmètre** : Toute l'autorité de prise de décisions AIMS, les déterminations d'applicabilité réglementaire IA, la gestion des exceptions de contrôle, l'évolution des critères IA et les processus de revue de gouvernance.

**Principe clé** : **La certification ISO/IEC 42001:2023 requiert un jugement professionnel à deux stades :**

1. **Conception AIMS** (Responsabilité de l'organisation) : Interpréter ISO 42001 dans le contexte organisationnel, déterminer les rôles fournisseur/opérateur IA, sélectionner les contrôles basés sur le risque, définir la suffisance des preuves
2. **Vérification AIMS** (Responsabilité de l'auditeur) : Apprécier si l'interprétation organisationnelle satisfait ISO 42001, vérifier que la mise en œuvre correspond à la documentation

La présente politique documente le jugement professionnel organisationnel (Stade 1) pour permettre une vérification d'audit objective (Stade 2).

**Relation avec ISMS-POL-01** : La présente politique est le complément IA de ISMS-POL-01. Lorsque les principes de gouvernance se recoupent (escalade des décisions, exigences de compétence, contrôle des changements), ISMS-POL-01 prévaut pour la gouvernance de la sécurité de l'information. AI-POL-01 établit les extensions de gouvernance spécifiques à l'IA et l'autorité distincte du RGIA.

---

## Limites d'autorité et de gouvernance

### Objectif et périmètre

La présente politique définit l'**autorité de prise de décisions** pour la gouvernance AIMS, en garantissant :

- Une attribution claire des responsabilités pour l'interprétation de la conformité IA
- Des processus documentés pour l'applicabilité, les exceptions et l'évolution
- Des exigences de compétence pour les décideurs de la gouvernance IA
- Des critères objectifs pour la vérification par les auditeurs

**La présente politique établit :**

- Les limites d'autorité pour les décisions AIMS (Section 2 : qui décide quoi, avec quelle compétence)
- L'autorité d'applicabilité réglementaire et de contrôle IA (Section 3 : qui détermine ce qui s'applique)
- Les processus d'acceptation des risques IA (Section 4 : comment les risques IA qui ne peuvent pas être atténués sont gérés)
- Le contrôle des changements des critères AIMS (Section 5 : comment l'AIMS évolue dans le temps)
- Le suivi de l'efficacité de la gouvernance (Section 6 : comment la qualité de la gouvernance est évaluée)

**La présente politique N'établit PAS :**

- Les exigences spécifiques de mise en œuvre des contrôles IA (traitées dans les politiques de groupe de contrôle AI-POL-A.x.x et les documents IMP)
- La méthodologie d'évaluation des risques IA (traitée dans la Procédure d'évaluation des risques AIMS)
- Les procédures de contrôle des documents (traitées dans la Procédure de contrôle des documents conformément à la Clause 7.5)
- Le programme d'audit interne (traité dans la Procédure d'audit interne conformément à la Clause 9.2)

**Principe de délimitation** : La présente politique établit l'**autorité de prise de décisions et les processus**. Les décisions elles-mêmes sont documentées dans **AI-POL-00 (applicabilité réglementaire), la DDA AIMS (applicabilité des contrôles) et le Registre d'acceptation des risques IA (décisions de traitement des risques)**.

**Intégration avec ISO/IEC 42001:2023** :

- **Clause 4.2 (Parties intéressées)** : La présente politique formalise l'autorité pour l'interprétation des exigences réglementaires IA
- **Clause 4.3 (Périmètre)** : Le RGIA et le RSSI recommandent conjointement le périmètre AIMS ; la Direction générale approuve
- **Clause 5.1 (Leadership)** : Établit la voie d'escalade des décisions garantissant l'engagement de la haute direction
- **Clause 5.2 (Politique IA)** : Le RGIA est propriétaire de la suite de politiques AIMS ; le RSSI est copropriétaire lorsque les obligations IA et sécurité se recoupent
- **Clause 5.3 (Rôles)** : Définit l'attribution d'autorité pour tous les rôles AIMS
- **Clause 9.3 (Revue de direction)** : Fournit le cadre de gouvernance pour la revue AIMS annuelle
- **Clause 10.1 (Amélioration continue)** : Permet l'amélioration des processus de gouvernance par les enseignements tirés

---

## Limites d'autorité et compétence

### Autorité de prise de décisions

| Niveau d'autorité | Rôle | Périmètre de décision | Exigence de compétence |
|------------------|------|-----------------------|------------------------|
| **Primaire** | RGIA | Conception des contrôles IA, interprétation ISO 42001/Règlement IA, autorité ÉISIA, processus d'évaluation des risques IA, applicabilité réglementaire (Niveaux 1/2 AI-POL-00), décisions AIMS courantes | Connaissance ISO 42001, expertise en gouvernance IA (Implémenteur principal / Auditeur ISO 42001, Certificat de gouvernance IA IAPP ou équivalent), 3+ ans d'expérience en gouvernance/risque IA, indépendance vis-à-vis des opérations IA |
| **Secondaire** | RSSI | Mesures de sécurité IA techniques, architecture de sécurité des systèmes IA, contrôles Annexe A à dimension sécurité (A.6.2.4, A.6.2.6, A.7.4), intégration avec l'ISMS | Expertise en sécurité de l'information (CISSP/CISM ou équivalent), connaissance ISO 27001/42001 |
| **Tertiaire** | Responsable Légal / Compliance | Interprétation juridique des obligations IA (Règlement IA UE, RGPD Art. 22), révision des contrats processeur/fournisseur, engagement avec les autorités réglementaires, évaluation de la conformité au Règlement IA UE | Formation juridique, connaissance de la réglementation IA, accès à un conseil IA externe |
| **Technique** | Directeur Technique (DT) / Responsable IA Engineering | Décisions d'architecture des systèmes IA, contrôles du cycle de vie (A.6.x), gouvernance des données (A.7.x), documentation technique | Expertise technique approfondie en IA/ML, pratiques d'ingénierie IA responsable |
| **Approbation** | Direction générale (DG / Conseil) | Décisions IA stratégiques, changements de périmètre AIMS, allocation des ressources, acceptation des risques IA, décisions relatives au portefeuille de systèmes IA | Responsabilité fiduciaire pour le risque IA, compréhension des obligations de responsabilité ISO 42001, autorité budgétaire |

**Indépendance du RGIA** :

Le RGIA DOIT opérer en toute indépendance vis-à-vis des fonctions de développement et de déploiement IA :

- Rapporte directement au DG ou à la haute direction équivalente
- N'est pas soumis aux instructions des équipes de développement IA ou du management produit concernant les déterminations de gouvernance IA
- N'a pas de conflit d'intérêts — ne détient pas d'autorité sur les décisions de conception des systèmes IA qui pourrait compromettre l'objectivité de la gouvernance
- A accès à tous les systèmes IA, documents et processus requis pour exercer ses fonctions de gouvernance

En l'absence d'un RGIA dédié, le RSSI assume l'autorité primaire avec la contrainte que les responsabilités de sécurité IA et de gouvernance IA sont exercées de manière indépendante.

**Voie d'escalade des décisions** :

1. **Décisions courantes** (conception des contrôles IA, format des preuves, documentation AIMS) :
   - **Autorité** : RGIA
   - **Documentation** : Documents AIMS POL/IMP, registres ÉISIA
   - **Révision** : Audit interne (Clause 9.2), revue de direction annuelle (Clause 9.3)

2. **Interprétation réglementaire** (attribution des niveaux AI-POL-00, classification Règlement IA UE, exigences EIDF du Règlement IA) :
   - **Autorité** : RGIA détermine l'applicabilité IA ; RSSI met en œuvre les mesures techniques ; le Légal examine les dimensions juridiques
   - **Documentation** : Matrice d'applicabilité réglementaire AI-POL-00
   - **Révision** : Suivi trimestriel, revue annuelle complète

3. **Acceptation des risques IA** (exclusion de contrôle IA ou acceptation de risque IA résiduel) :
   - **Autorité** : Le RGIA propose (avec l'évaluation des risques IA) ; la Direction générale approuve
   - **Documentation** : Registre d'acceptation des risques IA
   - **Révision** : Revue de direction annuelle (Clause 9.3)

4. **Changements stratégiques** (changement de périmètre AIMS, changement de détermination de rôle IA, expansion du portefeuille de systèmes IA vers des catégories à haut risque) :
   - **Autorité** : Approbation de la Direction générale (RGIA + RSSI recommandent ; DG/Conseil décide)
   - **Documentation** : Compte-rendus de revue de direction (Clause 9.3), procès-verbaux du conseil le cas échéant
   - **Révision** : Dans le cadre du cycle de planification stratégique organisationnel

**Exigences obligatoires** :

1. Le RGIA **doit** approuver toutes les mises en œuvre de contrôles IA avant le déploiement.
2. Le RGIA **doit** approuver toutes les déterminations d'applicabilité réglementaire (attributions de niveaux AI-POL-00) avant publication ou mise à jour.
3. La Direction générale **doit** approuver toutes les décisions d'acceptation des risques IA conformément à la Clause 6.1.3 d'ISO 42001:2023.
4. Le RGIA **doit** être consulté pour tout nouvel achat, développement ou modification matérielle d'un système IA — déclencheur de gouvernance IA. Aux fins de la présente politique, une **modification matérielle** désigne toute modification d'un système IA affectant la finalité prévue, la méthodologie d'entraînement, les sources de données, le type de résultats, le contexte opérationnel ou le périmètre de déploiement, qui n'avait pas été anticipée dans l'ÉISIA initiale et dans l'évaluation des risques. Cela s'aligne sur le concept de **modification substantielle** du Règlement IA de l'UE (Article 3(23)) : une modification qui affecte la conformité aux exigences applicables ou entraîne une modification de la finalité prévue évaluée. Un comportement d'apprentissage continu prédéterminé par le fournisseur au moment de l'évaluation initiale de la conformité ne constitue pas une modification substantielle.
5. L'escalade des décisions **doit** suivre la voie définie ci-dessus.

---

## Jugement professionnel dans la certification ISO 42001:2023

### Stade 1 : Conception AIMS (Responsabilité de l'organisation)

Le jugement professionnel exercé par l'organisation comprend :

1. **Détermination du rôle IA** (fournisseur, opérateur ou les deux par système IA) :
   - Identifier pour chaque système IA si l'organisation agit en tant que fournisseur IA, opérateur IA, ou les deux
   - Documenter la détermination par système IA dans l'Inventaire des systèmes IA
   - Sélectionner les contrôles applicables en fonction du rôle — certains contrôles s'appliquent principalement aux fournisseurs (ex. A.6.1.x, A.7.x), d'autres à tous les rôles
   - Documenté dans : Inventaire des systèmes IA, DDA AIMS

2. **Détermination du périmètre AIMS** (Clause 4.3) :
   - Quels systèmes IA sont dans le périmètre AIMS
   - Si l'AIMS est intégré à l'ISMS ISO 27001 ou exploité de manière autonome
   - Limites géographiques et organisationnelles
   - Documenté dans : Document de périmètre AIMS

3. **Sélection des contrôles et DDA** (Clause 6.1.3 / Annexe A) :
   - Sélectionner les contrôles en fonction de l'évaluation des risques IA et des résultats de l'ÉISIA
   - Déterminer l'applicabilité des 36 contrôles de l'Annexe A
   - Justifier les exclusions — « non applicable à notre rôle » ou « le risque ne s'applique pas » sont des exclusions valides ; « pas encore mis en œuvre » ne l'est pas
   - Documenté dans : DDA AIMS, Plan de traitement des risques IA, documents AI-POL-A.x.x

4. **Suffisance des preuves** :
   - Définir quelles preuves démontrent l'efficacité des contrôles (registres ÉISIA, entrées au registre des risques IA, rapports de test, journaux de monitoring)
   - Déterminer la fréquence et la conservation des preuves
   - Documenté dans : Documents IMP de contrôle (section preuves)

5. **Applicabilité réglementaire IA** (AI-POL-00) :
   - Déterminer quelles lois IA s'appliquent (cadre Niveaux 1/2/3 per AI-POL-00)
   - Évaluer les déclencheurs des réglementations conditionnelles (certification ISO 42001, classification à haut risque du Règlement IA UE)
   - Documenté dans : Matrice d'applicabilité réglementaire AI-POL-00

### Stade 2 : Vérification AIMS (Responsabilité de l'auditeur)

Le jugement professionnel exercé par l'auditeur comprend :

1. **Évaluation de la qualité des processus** :
   - La méthodologie d'évaluation des risques IA est-elle rigoureuse et appliquée de manière cohérente ?
   - Les déterminations de rôle IA (fournisseur/opérateur) sont-elles raisonnables compte tenu du portefeuille de systèmes IA ?
   - Les décideurs sont-ils compétents selon le tableau d'autorité ci-dessus ?

2. **Alignement avec ISO 42001:2023** :
   - L'interprétation organisationnelle des contrôles de l'Annexe A satisfait-elle les objectifs des contrôles ?
   - La DDA AIMS est-elle complète et justifiée (36 contrôles de l'Annexe A documentés) ?
   - Les clauses obligatoires (4–10) sont-elles traitées ?

3. **Efficacité de la mise en œuvre** (Stade 2) :
   - La mise en œuvre effective correspond-elle à la conception documentée (chaîne POL → IMP → Preuves) ?
   - Les preuves sont-elles suffisantes pour démontrer le fonctionnement des contrôles ?
   - Les non-conformités et actions correctives sont-elles traitées conformément à la Clause 10.2 ?

---

## Protocole de contestation de l'applicabilité

**Objectif** : Processus structuré pour résoudre les désaccords sur les déterminations d'applicabilité IA entre l'organisation et l'auditeur.

**Quand ce protocole s'applique** :

- L'auditeur remet en question l'applicabilité réglementaire IA (ex. « La classification à haut risque du Règlement IA UE est-elle justifiée ? »)
- L'auditeur conteste la détermination du rôle IA pour un système IA spécifique
- L'auditeur conteste une exclusion de contrôle dans la DDA AIMS
- L'auditeur estime qu'un contrôle alternatif n'atteint pas l'objectif ISO 42001:2023

**Étapes du protocole** :

**Étape 1 — L'auditeur soulève une préoccupation** : Documente la préoccupation spécifique — quelle détermination, quelles preuves sont en contradiction, quelle clause ou quel objectif de contrôle ISO 42001 pourrait ne pas être satisfait.

**Étape 2 — L'organisation fournit la documentation** :

- Pour l'**applicabilité réglementaire** : Évaluation selon la méthodologie AI-POL-00 ; évaluation du déclencheur ; registre d'approbation RGIA + Légal
- Pour la **détermination de rôle** : Description du système IA ; entrée dans l'inventaire ; justification du RGIA pour la classification fournisseur/opérateur
- Pour l'**exclusion de contrôle** : Évaluation des risques IA montrant pourquoi le risque ne s'applique pas ou pourquoi le contrôle est hors du périmètre organisationnel ; justification dans la DDA ; contexte organisationnel

**Étape 3 — Évaluation collaborative** : L'organisation et l'auditeur évaluent conjointement si la justification documentée satisfait les exigences ISO 42001:2023. La discussion est basée sur les faits.

**Étape 4 — Résolution** :

| Résultat | Action |
|---------|--------|
| Justification de l'organisation acceptée | Documenter dans les dossiers de travail d'audit ; aucune modification requise |
| Lacune confirmée | L'organisation déclenche une action corrective (Clause 10.2) ; mettre à jour la DDA/AI-POL-00 selon le cas |
| Désaccord non résolu | Escalader au processus de résolution des litiges de l'organisme de certification |

---

## Détermination du périmètre AIMS

### Exigences du document de périmètre

Le Document de périmètre AIMS (conformément à la Clause 4.3 d'ISO 42001:2023) doit préciser :

- **Les systèmes IA dans le périmètre** : Systèmes IA nommés avec finalité, type et contexte de déploiement
- **Les systèmes IA explicitement exclus** : Avec justification documentée
- **Les unités organisationnelles** : Quels départements, fonctions ou entités juridiques sont dans le périmètre
- **Les limites géographiques** : Quels sites ou juridictions sont inclus
- **L'intégration avec l'ISMS** : Si l'AIMS et l'ISMS partagent des processus (revue de direction, audit interne, contrôle des informations documentées)

### Inventaire des systèmes IA

L'[organisation] doit maintenir un Inventaire des systèmes IA en tant que document contrôlé. L'inventaire doit inclure, pour chaque système IA dans le périmètre :

| Champ | Description |
|-------|-------------|
| ID du système IA | Identifiant unique |
| Nom du système IA | Nom courant et version |
| Propriétaire du système IA | Personne responsable nommée |
| Finalité du système IA | Usage prévu et contexte de déploiement |
| Rôle IA | Fournisseur / Opérateur / Les deux |
| Classification de risque Règlement IA UE | Interdit / Haut risque / Risque limité / Risque minimal / GPAI |
| Référence ÉISIA | Lien vers le registre ÉISIA complété |
| Dans le périmètre AIMS | Oui / Non (avec justification si Non) |
| Référence DDA | Entrée dans la Déclaration d'Applicabilité |

L'Inventaire des systèmes IA doit être révisé :

- Au minimum annuellement lors de la revue de direction
- Lors de l'acquisition ou du développement d'un nouveau système IA
- Lorsqu'un système IA existant fait l'objet d'une modification matérielle (nouvelle finalité, nouvelle population, nouveau contexte de déploiement)
- Lorsqu'un changement de classification au titre du Règlement IA UE est identifié

---

## Déclaration d'Applicabilité (DDA) AIMS

L'[organisation] doit produire et maintenir une Déclaration d'Applicabilité conformément à la Clause 6.1.3 d'ISO 42001:2023. La DDA doit :

- Lister les 36 contrôles de l'Annexe A
- Pour chaque contrôle : indiquer s'il est applicable (Inclus) ou non applicable (Exclu)
- Pour les contrôles inclus : documenter le statut de mise en œuvre et la référence à la politique AI-POL-A.x.x
- Pour les contrôles exclus : documenter une justification écrite — l'exclusion n'est valide que lorsque le contrôle ne s'applique pas réellement au rôle IA, au périmètre et à l'évaluation des risques de l'organisation ; « pas encore mis en œuvre » ne constitue pas une justification d'exclusion valide
- Être approuvée par le RGIA avant première utilisation
- Être révisée annuellement et après des modifications matérielles du portefeuille de systèmes IA ou des exigences réglementaires

---

## Contrôle des changements AIMS

**Déclencheurs d'une mise à jour AIMS contrôlée** :

- Nouvelle réglementation IA adoptée ou mise à jour significative (actes délégués du Règlement IA UE, loi IA suisse)
- Nouveau standard ISO publié affectant l'AIMS (ISO 42006, mise à jour ISO 42005)
- Modification matérielle du portefeuille de systèmes IA (nouveau système IA à haut risque, retrait d'un système dans le périmètre)
- Constat d'audit interne ou action corrective affectant le périmètre de la politique
- Décision de la revue de direction

**Processus de changement** :

1. Le RGIA propose le changement avec une justification documentée
2. Le RSSI et le Légal examinent les dimensions sécurité et juridiques
3. La Direction générale approuve si décision stratégique (changement de périmètre, allocation de ressources)
4. La politique mise à jour est distribuée et communiquée conformément à la Clause 7.4
5. Une mise à jour de la formation ou de la sensibilisation est déclenchée si le changement affecte les obligations du personnel

---

## Revue de direction (Clause 9.3)

Le RGIA doit convoquer ou garantir une revue de direction AIMS annuelle avec la participation de :

- Direction générale (commanditaire)
- RGIA (président)
- RSSI
- Responsable Légal / Compliance
- DT / Responsable IA Engineering (lorsque le développement IA est dans le périmètre)
- Propriétaires de systèmes IA (pour les systèmes dans le périmètre)

**Points obligatoires à l'ordre du jour** (conformément à la Clause 9.3.2 d'ISO 42001:2023) :

1. Statut des actions de la revue de direction précédente
2. Changements du contexte externe/interne affectant l'AIMS
3. Changements dans le paysage réglementaire IA (mises à jour AI-POL-00)
4. Résultats de l'évaluation des risques IA et de l'ÉISIA
5. Indicateurs de performance AIMS (avancement des objectifs IA, nombre d'incidents/MTTR, avancement de la DDA)
6. Résultats de l'audit interne
7. Non-conformités et actions correctives
8. Revue de l'adéquation des ressources
9. Opportunités d'amélioration continue

**Résultats de la revue de direction** (Clause 9.3.3) :

Décisions documentées et éléments d'action incluant :

- Décisions d'amélioration continue
- Changements de périmètre AIMS
- Décisions d'allocation des ressources
- Mises à jour des politiques IA
- Décisions relatives au portefeuille de systèmes IA

Les registres de revue de direction doivent être conservés en tant que preuves documentées conformément à la Clause 7.5.

---

## Rôles et responsabilités

| Rôle | Responsabilités de gouvernance AIMS |
|------|-------------------------------------|
| **RGIA** | Autorité primaire AIMS ; propriétaire de la DDA ; propriétaire d'AI-POL-00 ; propriétaire du processus ÉISIA ; suivi réglementaire ; président de la revue de direction ; interlocuteur avec l'organisme de certification |
| **RSSI** | Dimensions sécurité des contrôles IA ; intégration ISMS/AIMS ; supervision des mesures techniques ; révision sécurité A.6.2.4/A.6.2.6 |
| **Légal / Compliance** | Suivi réglementaire IA ; coordination de l'évaluation de la conformité au Règlement IA UE ; clauses IA dans les contrats fournisseurs IA ; engagement avec les autorités de surveillance |
| **DT / Responsable IA Engineering** | Mise en œuvre des contrôles A.6.x et A.7.x ; documentation du cycle de vie des systèmes IA ; génération des preuves techniques |
| **Propriétaires de systèmes IA** | Entrées dans l'inventaire des systèmes IA ; réalisation de l'ÉISIA pour les systèmes dont ils sont propriétaires ; contrôles opérationnels ; signalement des incidents |
| **Direction générale** | Acceptation des risques IA ; allocation des ressources ; approbation du périmètre AIMS ; participation à la revue de direction |
| **Auditeur interne** | Programme d'audit AIMS indépendant ; rapport des constats ; vérification des actions correctives |

---

<!-- QA_VERIFIED: [YYYY-MM-DD] -->
