<!-- ISMS-CORE:POLICY:PRIV-POL-00-FR:privacy:POL:00 -->
**PRIV-POL-00 — Cadre d'applicabilité réglementaire en matière de protection des données**
**Référence faisant autorité pour les obligations de conformité du SGDP**

---

## Contrôle du document

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Cadre d'applicabilité réglementaire en matière de protection des données |
| **Type de document** | Politique |
| **Identifiant du document** | PRIV-POL-00 |
| **Auteur du document** | Délégué à la Protection des Données (DPD) |
| **Propriétaire du document** | Directeur Général (DG) |
| **Approuvé par** | Direction générale |
| **Date de création** | [Date] |
| **Version** | 1.0 |
| **Date de version** | [À définir] |
| **Classification** | Interne |
| **Statut** | Brouillon |

**Historique des versions** :

| Version | Date | Auteur | Modifications |
|---------|------|--------|---------------|
| 0.1 | [Date - 8 sem.] | DPD | Brouillon initial — structure du cadre à trois niveaux, périmètre RGPD + LPD |
| 0.2 | [Date - 6 sem.] | DPD + Juridique | Ajout des niveaux ISO 27701:2025 et ISO 27018:2025 ; conditions de périmètre international |
| 0.3 | [Date - 4 sem.] | RSSI | Alignement avec la méthodologie ISMS-POL-00 ; références cloud et sécurité cloud ajoutées |
| 0.4 | [Date - 2 sem.] | DPD/Juridique/RSSI | Intégration des retours des parties prenantes ; note ISO 27017 à venir ajoutée |
| 1.0 | [Date] | DPD/Juridique/RSSI | Première version approuvée |

**Cycle de révision** : Annuel (ou en cas de changements réglementaires significatifs, nouvelles publications normatives, ou changements du périmètre de certification)
**Prochaine date de révision** : [Date d'entrée en vigueur + 12 mois]

**Chaîne d'approbation** :

- Principale : Délégué à la Protection des Données (DPD)
- Secondaire : Responsable de la Sécurité des Systèmes d'Information (RSSI)
- Conformité : Responsable Juridique/Conformité
- Autorité finale : Direction générale

**Documents connexes** :

- PRIV-POL-01 — Cadre de gouvernance et de prise de décisions en matière de protection des données
- ISMS-POL-00 — Cadre d'applicabilité réglementaire (base SGSI — co-référence obligatoire)
- ISO/IEC 27701:2025 Clause 5.2 (Compréhension des besoins et attentes des parties intéressées)
- ISO/IEC 27701:2025 Clause 5.3 (Détermination du périmètre du SGDP)
- Tous les documents de politique SGDP (référence obligatoire)

**Distribution** : Tous les acteurs SGDP, délégués à la protection des données, auteurs de politiques, propriétaires de systèmes, auditeurs, sous-traitants
**Référencé par** : Tous les documents de politique SGDP (PRIV-POL-01, tous les POL des groupes de contrôle PRIV-POL-A.x.x)

**Stratégie linguistique** : Lorsque des termes techniques ou réglementaires sont établis à l'échelle internationale (ex. RGPD, ISO/IEC, LPD, DCP), la terminologie anglaise est conservée pour préserver la précision et faciliter les références réglementaires transfrontalières.

---

## Résumé exécutif

Ce document constitue la **référence faisant autorité** pour interpréter l'applicabilité des réglementations et cadres de protection des données dans l'ensemble du Système de Gestion de la Protection des Données (SGDP).

**Objet** : Éliminer l'ambiguïté et les incohérences dans les références aux lois sur la protection des données, aux réglementations et aux normes dans l'ensemble de la documentation SGDP.

**Périmètre** : Toutes les références aux lois sur la protection des données, aux réglementations sur la confidentialité et aux cadres de protection des données dans la documentation SGDP.

**Relation avec le SGSI** : Cette politique est le complément spécifique à la protection des données de **ISMS-POL-00** (Cadre d'applicabilité réglementaire). ISMS-POL-00 régit les obligations de sécurité de l'information. PRIV-POL-00 régit les obligations de confidentialité et de protection des données. Là où les obligations se chevauchent (ex. Article 32 du RGPD — sécurité du traitement), ISMS-POL-00 prévaut pour la dimension sécurité de l'information ; PRIV-POL-00 régit la dimension protection des données.

**Principe clé** : **L'applicabilité des réglementations sur la protection des données doit être explicite, pas supposée.** Les références aux réglementations et cadres de protection des données se répartissent en trois catégories :

1. **Conformité obligatoire** — Obligations légales applicables à l'organisation
2. **Applicabilité conditionnelle** — Exigences s'appliquant uniquement dans des circonstances spécifiques
3. **Référence informative** — Meilleures pratiques et orientations techniques

**Utilisation** : Toutes les politiques SGDP DOIVENT inclure une section « Cadre réglementaire » référençant ce document, identifiant à quel niveau appartient chaque réglementation/norme citée.

**Termes clés** : Les définitions des termes utilisés dans cette politique (Obligatoire, Conditionnel, Niveau 1/2/3, Déclencheur d'applicabilité, DCP, Personne concernée, Responsable du traitement, Sous-traitant) sont fournies dans le **Glossaire** à la fin de ce document.

---

## Autorité de la politique et limites

### Objet et périmètre de cette politique

Cette politique définit l'**identification et l'applicabilité** des exigences légales, réglementaires et contractuelles pour le Système de Gestion de la Protection des Données de l'organisation.

**Cette politique établit :**

- Quelles lois et normes de protection des données s'appliquent à l'organisation
- La catégorisation des obligations de protection des données (Obligatoire, Conditionnelle, Informative)
- La méthodologie d'évaluation pour déterminer l'applicabilité
- Les processus de révision et de mise à jour pour les changements réglementaires

**Cette politique n'établit PAS :**

- Les décisions de traitement des risques pour la protection des données (traitées dans la gestion des risques SGDP)
- Les exigences de mise en œuvre des contrôles (traitées dans les POL et IMP des groupes de contrôle)
- Le statut de conformité ou la vérification (traités dans les processus de suivi de la conformité)
- Les obligations de sécurité de l'information (traitées dans ISMS-POL-00)

Le résultat de l'évaluation de l'applicabilité réglementaire en matière de protection des données sert d'**entrée** pour :

- Les décisions de périmètre des contrôles dans tous les groupes de contrôle SGDP
- La priorisation de l'évaluation et du traitement des risques de protection des données
- Les décisions de proportionnalité pour la mise en œuvre des contrôles (obligations responsable du traitement vs. sous-traitant)
- La planification des audits et la vérification de la conformité

**Principe de délimitation** : Cette politique établit l'applicabilité réglementaire en matière de protection des données. La mise en œuvre, l'application et la vérification sont traitées par des processus SGDP distincts et des politiques de groupes de contrôle.

**Intégration avec ISO 27701:2025 :**

- **Clause 5.2 (Parties intéressées)** : Les exigences réglementaires en matière de protection des données constituent les principales obligations des parties intéressées. Cette politique les identifie explicitement.
- **Clause 5.3 (Périmètre)** : La détermination du périmètre est éclairée par les réglementations de Niveau 1 applicables et le rôle de l'organisation (responsable du traitement, sous-traitant, ou les deux).
- **Clause 6 (Évaluation des risques)** : Les obligations réglementaires alimentent le registre des risques SGDP. Niveau 1 = priorité élevée, Niveau 2 conditionnel = priorité moyenne, Niveau 3 = contribution informative.

**Intégration avec ISMS-POL-00 :**

Cette politique opère aux côtés de et est subordonnée à ISMS-POL-00 pour toutes les questions de sécurité de l'information. Lorsqu'une réglementation présente à la fois des dimensions de protection des données et de sécurité (ex. RGPD Article 32, CH-nLPD Article 7), les obligations sont traitées conjointement. PRIV-POL-00 régit l'interprétation protection des données ; ISMS-POL-00 régit l'interprétation sécurité.

---

## Catégories d'applicabilité réglementaire

**Conformité obligatoire**
Obligations légales ou contractuelles de protection des données que l'organisation DOIT respecter. Le non-respect entraîne une responsabilité légale, des amendes réglementaires, des investigations de l'autorité de contrôle ou une perte de certification.

**Caractéristiques** :

- Exécutoire par l'autorité de protection des données (APD) ou un tribunal
- Le non-respect a des conséquences juridiques/financières (amendes, mesures coercitives)
- Nécessite des preuves documentées de conformité (registres de traitement, AIPD, enregistrements de consentement)
- Soumis aux audits réglementaires, inspections et pouvoirs des autorités de contrôle

**Applicabilité conditionnelle**
Exigences de protection des données s'appliquant uniquement lorsque des conditions spécifiques sont remplies (ex. types de données spécifiques traités, périmètre géographique, certification recherchée, contrats clients, modèle de service cloud).

**Caractéristiques** :

- L'applicabilité dépend des activités de traitement, des types de données ou du périmètre géographique
- Peut devenir obligatoire en fonction des activités commerciales ou des exigences contractuelles
- Nécessite une réévaluation périodique à mesure que les activités commerciales et de traitement évoluent

**Référence informative / Alignement sur les meilleures pratiques**
Cadres et normes utilisés pour des orientations techniques et organisationnelles, l'analyse comparative ou l'alignement volontaire. Ces éléments informent les pratiques en matière de protection des données mais ne constituent pas des exigences de conformité obligatoires.

**Caractéristiques** :

- Adoption volontaire pour les meilleures pratiques
- Pas de mécanisme légal direct d'exécution
- Utilisé pour la mise en œuvre des mesures techniques et organisationnelles (MTO)
- Peut devenir obligatoire s'il est référencé dans des contrats ou des exigences de certification

---

## Hiérarchie de conformité

```
┌─────────────────────────────────────────────────────────────────┐
│         HIÉRARCHIE DE CONFORMITÉ EN PROTECTION DES DONNÉES      │
├─────────────────────────────────────────────────────────────────┤
│  NIVEAU 1 : OBLIGATOIRE (Légal/Contractuel)                     │
│  • RGPD UE (si traitement de données personnelles UE)           │
│  • Loi fédérale suisse sur la protection des données (LPD/nLPD) │
│                                                                 │
│  NIVEAU 2 : CONDITIONNEL (Selon le contexte)                    │
│  • ISO/IEC 27701:2025 (si certification recherchée ou           │
│    contractuellement requise)                                   │
│  • ISO/IEC 27018:2025 (sous-traitants DCP en cloud)            │
│  • UK GDPR (si traitement de données personnelles brit.         │
│    post-Brexit)                                                 │
│  • LGPD (si traitement de données personnelles brésiliennes)    │
│  • PIPL (si traitement de données personnelles chinoises)       │
│  • Autres lois nationales (évaluation basée sur déclencheurs)  │
│                                                                 │
│  NIVEAU 3 : INFORMATIF (Meilleures pratiques / Orientations)    │
│  • ISO/IEC 27017:2026 (base sécurité cloud pour 27018 ;        │
│    remplace l'édition 2015 — adoption formelle en attente)      │
│  • ISO/IEC 27002:2022 (mise en œuvre des contrôles sécu.)      │
│  • NIST Privacy Framework 2.0 (gestion des risques)            │
└─────────────────────────────────────────────────────────────────┘
```

> *Si les caractères de cadre ne s'affichent pas correctement, se référer aux sections ci-dessous pour les définitions des niveaux.*

---

# Conformité obligatoire (Niveau 1)

> **Note sur la classification ISO/IEC 27701:2025** : ISO/IEC 27701:2025 est classifiée **Niveau 2 (Conditionnelle)** dans ce cadre. Ce n'est pas une réglementation légalement exécutoire. Elle devient obligatoire pour [Organisation] lorsque la certification est activement recherchée ou qu'un contrat client exige explicitement la conformité au SGDP. Lorsqu'aucune de ces conditions ne s'applique, elle fonctionne comme un cadre de meilleures pratiques volontaire. Voir la section ISO/IEC 27701:2025 sous le Niveau 2 pour tous les détails.

## Règlement Général sur la Protection des Données (RGPD) de l'UE

**Applicabilité** : Lors du traitement de données à caractère personnel de résidents de l'UE/EEE, quel que soit le lieu d'établissement de l'organisation.

**Exigences clés** :

- Article 5 : Principes du traitement (licéité, loyauté, transparence, limitation des finalités, minimisation des données, exactitude, limitation de la conservation, intégrité et confidentialité, responsabilité)
- Article 6 : Licéité du traitement
- Articles 7–9 : Exigences de consentement et données de catégorie spéciale
- Articles 13–14 : Informations à fournir aux personnes concernées (avis de confidentialité)
- Articles 15–22 : Droits des personnes concernées (accès, rectification, effacement, limitation, portabilité, opposition, décision automatisée)
- Article 24 : Responsabilités du responsable du traitement (responsabilité, politiques, mesures)
- Article 25 : Protection des données dès la conception et par défaut
- Article 28 : Obligations du sous-traitant (contrat écrit, mesures de sécurité, contrôles des sous-traitants ultérieurs)
- Article 30 : Registre des activités de traitement (RADT)
- Article 32 : Sécurité du traitement (chiffrement, pseudonymisation, résilience, tests)
- Articles 33–34 : Notification des violations (72 heures à l'APD ; sans retard injustifié aux personnes concernées pour les violations à haut risque)
- Articles 35–36 : Analyse d'impact relative à la protection des données (AIPD) pour les traitements à haut risque ; consultation préalable de l'APD lorsque le risque résiduel reste élevé
- Articles 37–39 : Obligations du Délégué à la Protection des Données (DPD) le cas échéant
- Articles 44–49 : Restrictions sur les transferts internationaux de données

**Impact sur le SGDP** :

- Protection des données dès la conception et par défaut dans toutes les activités de traitement
- Registres des activités de traitement (RADT) tenus par le responsable du traitement et le sous-traitant
- Base légale documentée pour chaque activité de traitement
- Procédures des droits des personnes concernées mises en œuvre et testées
- Contrats de sous-traitance conformes à l'Article 28 en place
- Processus AIPD pour les traitements à haut risque
- Procédure de notification des violations avec délai de 72 heures
- Garanties pour les transferts internationaux (décisions d'adéquation, Clauses Contractuelles Types, BCR)

**Autorité de contrôle** : Autorité de protection des données (APD) UE/EEE compétente de l'établissement principal ou du pays de la personne concernée.

**Référence** : Règlement (UE) 2016/679, en vigueur depuis le 25 mai 2018

---

## Loi fédérale suisse sur la protection des données (LPD/nLPD)

**Applicabilité** : Tout traitement de données à caractère personnel par l'organisation soumis à la juridiction suisse ; et tout traitement de données à caractère personnel de résidents suisses depuis l'étranger lorsque les effets se produisent en Suisse.

**Exigences clés** :

- Article 6 : Principes (licéité, bonne foi, proportionnalité, limitation des finalités)
- Article 7 : Sécurité des données (mesures techniques et organisationnelles appropriées au risque)
- Article 8 : Traitement des données par des sous-traitants (accord écrit, sécurité, sous-traitants ultérieurs)
- Article 9 : Communication à l'étranger (décision d'adéquation ou garanties appropriées)
- Article 10 : Représentants en Suisse (en l'absence d'établissement)
- Article 12 : Registre des activités de traitement (pour les responsables du traitement avec >250 ETP ou traitement à haut risque)
- Articles 19–21 : Devoir de fournir des informations (avis de confidentialité aux personnes concernées)
- Article 22 : Analyse d'impact relative à la protection des données (AIPD) pour les traitements à haut risque
- Article 25 : Protection des données dès la conception et par défaut
- Article 26 : Droits des personnes concernées (accès, rectification, effacement, limitation, portabilité, opposition)
- Article 24 : Notification des violations au PFPDT lorsque susceptible d'entraîner un risque élevé
- Article 328b CO : Surveillance des employés et protection de la personnalité

**Alignement LPD/RGPD** : La LPD révisée (en vigueur le 1er septembre 2023) est substantiellement alignée avec le RGPD en termes de structure et de principes. Pour les organisations soumises aux deux, un programme aligné RGPD satisfait généralement les exigences de la LPD. Différences clés : la LPD ne prévoit pas d'obligation de DPD ; la liste d'adéquation suisse diffère de l'UE ; pas de régime d'amendes administratives (sanctions pénales à la place).

**Impact sur le SGDP** :

- Registre de traitement tenu (Art. 12)
- Contrats de sous-traitance conformes à l'Art. 8 en place
- Avis de confidentialité délivrés aux personnes concernées (Art. 19–21)
- Processus AIPD pour les traitements à haut risque (Art. 22)
- Notification des violations à haut risque au PFPDT
- Garanties pour les transferts internationaux lorsque les données quittent la Suisse

**Autorité de contrôle** : Préposé fédéral à la protection des données et à la transparence (PFPDT — Eidgenössischer Datenschutz- und Öffentlichkeitsbeauftragter, EDÖB)

**Référence** : Loi fédérale sur la protection des données (RS 235.1), en vigueur le 1er septembre 2023

---

# Applicabilité conditionnelle (Niveau 2)

Ces réglementations et normes s'appliquent **uniquement lorsque des conditions spécifiques sont remplies**.

## ISO/IEC 27701:2025 — Système de Gestion de la Protection des Données

**Norme** : ISO/IEC 27701:2025 (Deuxième édition) — Système de gestion de la protection des données à caractère personnel

**Déclencheurs d'applicabilité** :

- L'organisation **recherche la certification ISO/IEC 27701:2025** (autonome ou combinée avec la certification ISO 27001)
- Un contrat client **exige explicitement** la conformité au SGDP avec cette norme

**Note de classification** : ISO/IEC 27701:2025 est classifiée Niveau 2 (Conditionnelle) dans ce cadre. Ce n'est pas une réglementation légalement exécutoire. Elle ne devient pas obligatoire simplement parce que l'organisation traite des DCP — le RGPD et la LPD remplissent ce rôle. Lorsque la certification est recherchée ou contractuellement requise, elle est traitée comme un engagement opérationnel contraignant équivalent au Niveau 1 pendant la durée de la certification.

**Exigences clés** :

- Clause 5 : Contexte du SGDP (compréhension de l'organisation, des parties intéressées, du périmètre)
- Clause 6 : Leadership (engagement, politique, rôles, responsabilités)
- Clause 7 : Planification (risques, objectifs, déclencheurs privacy by design)
- Clause 8 : Support (ressources, compétence, sensibilisation, communication, information documentée)
- Clause 9 : Opération (planification opérationnelle, traitement des risques, processus AIPD)
- Clause 10 : Évaluation des performances (surveillance, audit interne, revue de direction)
- Clause 11 : Amélioration (non-conformité, action corrective, amélioration continue)
- Annexe A : Contrôles spécifiques au responsable du traitement (A.1.x — 31 contrôles)
- Annexe A : Contrôles spécifiques au sous-traitant (A.2.x — 18 contrôles)
- Annexe A : Contrôles de sécurité partagés (A.3.x — 29 contrôles)
- Annexe B : Correspondance des contrôles ISO/IEC 27001:2022 avec le SGDP (normative)

**Impact sur le SGDP** :

- Mise en œuvre complète de toutes les politiques de groupes de contrôle PRIV-POL-A.x.x dans 51-isms-core-privacy/
- Détermination du rôle documentée (responsable du traitement, sous-traitant, ou les deux par activité de traitement)
- SGDP intégré ou superposé à l'ISO 27001 SGSI

**Note sur l'édition** : ISO/IEC 27701:2025 (Deuxième édition) est une norme SGDP autonome, et non un ensemble de clauses d'extension pour ISO 27001. Elle peut être mise en œuvre et certifiée indépendamment. Lorsqu'une organisation détient une certification ISO 27001, l'Annexe B fournit la correspondance normative entre les contrôles 27001 et les exigences 27701.

**Référence** : ISO/IEC 27701:2025, Sécurité de l'information, cybersécurité et protection des données à caractère personnel — Système de gestion de la protection des données à caractère personnel

---

## ISO/IEC 27018:2025 — Sous-traitants DCP en cloud

**Norme** : ISO/IEC 27018:2025 (Troisième édition) — Technologies de l'information — Techniques de sécurité — Code de bonnes pratiques pour la protection des données à caractère personnel (DCP) dans les clouds publics agissant comme sous-traitants de DCP

**Déclencheurs d'applicabilité** :

- L'organisation agit en tant que **sous-traitant de DCP exploitant des services cloud publics** (fournisseur de services cloud traitant les DCP des clients)
- Des contrats clients **exigent explicitement** la conformité ou la certification ISO/IEC 27018
- La certification à ISO/IEC 27018:2025 est recherchée

**Contenu d'ISO 27018:2025** :

ISO 27018:2025 comprend deux parties distinctes :

- **Corps (Clauses 5–18)** : Orientations de mise en œuvre pour les contrôles ISO/IEC 27002:2022 dans les environnements cloud publics. Ces orientations sont informatives dans le contexte et ne créent pas d'exigences obligatoires supplémentaires au-delà d'ISO 27002.
- **Annexe A (normative lors de la certification)** : 25 contrôles spécifiques aux DCP non inclus dans ISO 27002. Ce sont les véritables nouvelles obligations des sous-traitants DCP en cloud (consentement, transparence, limitation des finalités, retour/effacement, divulgation des sous-traitants ultérieurs, etc.).

**Livraison SGDP** : Les contrôles Annexe A d'ISO 27018 (25 contrôles) sont fournis en tant qu'overlay de correspondance sur `priv-a.2.5.7-9-sub-processor-management` et les packs sous-traitants adjacents. Ils NE sont PAS des packs autonomes.

**Évaluation** : Si l'organisation fournit des services cloud publics et traite les DCP des clients → évaluer l'Annexe A d'ISO 27018:2025 pour l'applicabilité.

**Référence** : ISO/IEC 27018:2025, Troisième édition, 2025

---

## Règlement général sur la protection des données du Royaume-Uni (UK GDPR)

**Réglementation** : UK GDPR (droit UE conservé tel que modifié par les Data Protection, Privacy and Electronic Communications (Amendments etc) (EU Exit) Regulations 2019) + Data Protection Act 2018, tel que modifié par le **Data (Use and Access) Act 2025**

**Déclencheurs d'applicabilité** :

- L'organisation **traite des données à caractère personnel de résidents britanniques** post-Brexit (1er janvier 2021)
- L'organisation a un **établissement au Royaume-Uni**
- L'organisation **cible ou surveille des individus** au Royaume-Uni

**Différences clés avec le RGPD UE** :

- Autorité de contrôle : Information Commissioner's Office (ICO), et non les APD UE
- Transferts internationaux : réglementations d'adéquation britanniques (pas les décisions d'adéquation UE) ; transfert UE→UK couvert par la décision d'adéquation UE pour le UK (en vigueur au moment de la rédaction — surveiller la révision)
- Clauses contractuelles types britanniques (IDTA) ou addendum britannique aux CCT UE requis pour les transferts vers des pays tiers
- **Data (Use and Access) Act 2025** : Introduit des modifications ciblées spécifiques au UK des obligations de protection des données ; le DPD évalue l'impact pour les organisations avec des opérations au UK en continu

**Évaluation** : Si l'organisation traite des données personnelles britanniques → la conformité au UK GDPR est requise parallèlement au RGPD UE. Pour la plupart des organisations CH/UE avec des opérations au UK ou des clients britanniques, cela sera obligatoire. Surveiller les orientations de l'ICO sur la mise en œuvre du Data (Use and Access) Act 2025.

**Référence** : UK GDPR ; Data Protection Act 2018 (UK) ; Data (Use and Access) Act 2025

---

## Lei Geral de Proteção de Dados (LGPD) — Brésil

**Réglementation** : Lei n° 13.709/2018 — Lei Geral de Proteção de Dados Pessoais

**Déclencheurs d'applicabilité** :

- L'organisation **traite des données à caractère personnel d'individus situés au Brésil**
- Le traitement **se déroule au Brésil** (quel que soit le lieu d'établissement)
- Le traitement a **pour but l'offre de biens ou de services** au Brésil

**Exigences clés** (structure alignée RGPD) :

- Bases légales du traitement (10 bases légales, dont le consentement et l'intérêt légitime)
- Droits des personnes concernées (accès, rectification, suppression, portabilité, opposition)
- Obligations du Délégué à la Protection des Données (DPD/Encarregado)
- Notification des incidents de sécurité à l'ANPD (APD brésilienne) et aux personnes concernées
- Transferts internationaux : décision d'adéquation, clauses contractuelles ou consentement

**Évaluation** : Si l'organisation sert des clients brésiliens ou traite des données personnelles brésiliennes → évaluer l'applicabilité de la LGPD. Structure similaire au RGPD ; un programme aligné RGPD couvre la plupart des exigences.

**Autorité de contrôle** : Autoridade Nacional de Proteção de Dados (ANPD)

**Référence** : Lei n° 13.709/2018, en vigueur depuis septembre 2020 (application depuis août 2021)

---

## Loi sur la protection des données personnelles (PIPL) — Chine

**Réglementation** : Personal Information Protection Law (个人信息保护法), en vigueur le 1er novembre 2021

**Déclencheurs d'applicabilité** :

- L'organisation **traite des informations personnelles d'individus situés en Chine**
- L'organisation fournit **des produits ou services** ciblant des individus en Chine
- L'organisation **analyse le comportement** d'individus en Chine

**Exigences clés** :

- Le consentement comme base légale principale (périmètre de l'intérêt légitime plus étroit que le RGPD)
- Localisation des données : les informations personnelles d'individus chinois collectées en Chine peuvent nécessiter un stockage local
- Transferts transfrontaliers : trois mécanismes disponibles — (1) évaluation de sécurité par le CAC requise pour les transferts dépassant les seuils de volume ; (2) contrat standard (CCT) pour les volumes plus faibles ; (3) certification de protection des données personnelles par un organisme reconnu (pour les transferts au sein de groupes multinationaux — voir les dispositions d'application du CAC)
- Délégué à la Protection des Données : requis si le traitement dépasse les seuils
- Notification des violations dans les 24 heures au régulateur

**Évaluation** : Si l'organisation offre des services à ou collecte des données personnelles d'individus en Chine → une évaluation de l'applicabilité de la PIPL est requise. Note : la PIPL est plus stricte que le RGPD à plusieurs égards (consentement par défaut, localisation, contrôles des transferts transfrontaliers).

**Autorité de contrôle** : Cyberspace Administration of China (CAC — 国家互联网信息办公室)

**Référence** : PIPL 2021 ; Dispositions du CAC sur les contrats standard pour le transfert transfrontalier de données personnelles (2023)

---

## Réglementations conditionnelles supplémentaires en matière de protection des données

Les organisations doivent évaluer et documenter des réglementations supplémentaires en fonction de leurs activités de traitement spécifiques et de leur périmètre géographique :

| Réglementation | Déclencheur | Autorité de contrôle |
|---------------|-------------|---------------------|
| **CCPA/CPRA** (Californie) | Résidents californiens ; seuils de revenus/données | California Privacy Protection Agency (CPPA) |
| **PIPEDA** (Canada) | Traitement commercial de données personnelles canadiennes | Commissariat à la protection de la vie privée du Canada (OPC) |
| **PDPA** (Singapour) | Traitement de données personnelles de résidents singapouriens | Personal Data Protection Commission (PDPC) |
| **APPI** (Japon) | Traitement d'informations personnelles de résidents japonais | Personal Information Protection Commission (PPC) |
| **POPIA** (Afrique du Sud) | Traitement d'informations personnelles de résidents sud-africains | Autorité de protection de l'information (Information Regulator) |
| **Réglementations sectorielles** | Santé (e-santé), données financières, données d'enfants | Autorité compétente du secteur |

**Approche d'évaluation** : Pour chaque nouveau marché géographique ou activité de traitement, évaluer si une réglementation sur la protection des données s'applique en utilisant les déclencheurs ci-dessus. Documenter la détermination dans le journal de surveillance réglementaire (voir la section Maintenance).

---

# Référence informative / Meilleures pratiques (Niveau 3)

## ISO/IEC 27017:2015 — Contrôles de sécurité pour les services cloud

**Norme** : ISO/IEC 27017:2015 — Technologies de l'information — Techniques de sécurité — Code de bonnes pratiques pour les contrôles de sécurité de l'information basés sur ISO/IEC 27002 pour les services cloud

**Rôle dans PRIV-POL-00** : ISO 27017 est une norme de **sécurité cloud** (pas une norme de protection des données). Elle est référencée ici comme base technique de support car ISO 27018:2025 (Annexe A — contrôles des sous-traitants DCP en cloud) s'appuie directement sur le fondement de sécurité établi par ISO 27017. Les organisations mettant en œuvre ISO 27018 doivent traiter les contrôles ISO 27017 comme le socle de sécurité pour les environnements de traitement DCP en cloud.

**Référence principale** : ISO 27017 est référencé dans **ISMS-POL-00** (Niveau 3) comme meilleure pratique de sécurité cloud. Sa présence dans PRIV-POL-00 est uniquement comme référence de support à la protection des données.

**Domaines d'orientation clés** (pertinents pour le traitement DCP en cloud) :

- Responsabilité partagée entre le client cloud et le fournisseur de services cloud
- Durcissement et isolation des machines virtuelles
- Sécurité opérationnelle des administrateurs
- Surveillance des services cloud
- Sécurité réseau dans les environnements cloud

**Utilisation dans le SGDP** : Référencé dans `priv-a.2.4.2-4-processor-lifecycle-controls` et `priv-a.2.5.7-9-sub-processor-management` (packs overlay ISO 27018).

**Référence** : ISO/IEC 27017:2015, Contrôles de sécurité de l'information pour les services cloud

---

## ISO/IEC 27017:2026 — Publiée (Adoption formelle en attente)

**Statut** : **Publiée** (2026), remplace l'édition 2015. Les actions à la publication ci-dessous sont en attente.

ISO/IEC 27017:2026 est la deuxième édition de la norme sur les contrôles de sécurité pour les services cloud. Cette politique sera mise à jour pour référencer ISO/IEC 27017:2026 à la place de (ou parallèlement à) ISO/IEC 27017:2015 une fois les actions à la publication ci-dessous réalisées.

**Actions à la publication** :

1. Examiner ISO/IEC 27017:2026 pour les changements structurels par rapport à l'édition 2019
2. Évaluer l'impact sur les packs de contrôle `priv-a.2.4.2-4` et `priv-a.2.5.7-9`
3. Mettre à jour la référence Niveau 3 de PRIV-POL-00 de 2019 à l'édition 2026
4. Communiquer les changements aux propriétaires des groupes de contrôle concernés
5. Mettre à jour les IMP des packs de contrôle où les orientations 27017 sont référencées

**Surveiller** : Publications ISO.org — programme de travail SC 27 — WG 4 (Contrôles et services de sécurité)

---

## ISO/IEC 27002:2022 — Orientations sur la mise en œuvre des contrôles de sécurité

**Norme** : ISO/IEC 27002:2022 — Sécurité de l'information, cybersécurité et protection des données à caractère personnel — Contrôles de sécurité de l'information

**Rôle dans PRIV-POL-00** : ISO 27002 fournit des orientations de mise en œuvre pour les contrôles de sécurité partagés A.3.x (Annexe A.3 d'ISO 27701:2025). Les 29 contrôles partagés A.3 sont des overlays spécifiques à la protection des données sur le cadre de contrôles de sécurité de l'information établi par ISO 27002.

**Référence** : ISO/IEC 27002:2022

---

## NIST Privacy Framework 2.0

**Cadre** : NIST Privacy Framework : Un outil pour améliorer la protection des données à travers la gestion des risques d'entreprise, Version 2.0 (2024)

**Rôle dans PRIV-POL-00** : Référence informative pour la méthodologie de gestion des risques de protection des données. Fournit un vocabulaire basé sur les fonctions (Identify-P, Govern-P, Control-P, Communicate-P, Protect-P) pour l'évaluation de la maturité du programme de protection des données. La version 2.0 s'aligne plus étroitement avec le NIST Cybersecurity Framework 2.0, ajoutant la fonction Govern-P et renforçant les orientations sur les risques de protection des données dans la chaîne d'approvisionnement. Peut être utilisé pour l'analyse des écarts et l'évaluation comparative des risques de protection des données.

**Référence** : NIST Privacy Framework v2.0, NIST, 2024

---

# Détermination de l'applicabilité réglementaire en matière de protection des données

## Processus d'évaluation

Lors de l'évaluation de l'applicabilité d'une réglementation sur la protection des données à l'organisation, suivre ce processus de décision :

**Étape 1 : Identifier les activités de traitement**

Documenter chaque catégorie de traitement de DCP : quelles données, de qui (personnes concernées), dans quels territoires, pour quelle finalité, en tant que responsable du traitement ou sous-traitant.

**Étape 2 : Appliquer les déclencheurs géographiques**

Pour chaque réglementation, évaluer le déclencheur d'applicabilité par rapport à la cartographie des traitements :

| Type de déclencheur | Questions |
|--------------------|-----------| 
| **Établissement** | L'organisation est-elle établie dans la juridiction ? |
| **Localisation des personnes concernées** | Des individus dans la juridiction dont les données sont traitées existent-ils ? |
| **Ciblage / Surveillance** | L'organisation cible-t-elle ou surveille-t-elle des individus dans la juridiction ? |
| **Prestation de services** | L'organisation offre-t-elle des biens/services dans la juridiction ? |

**Étape 3 : Déterminer le rôle responsable du traitement/sous-traitant**

Les obligations de protection des données diffèrent significativement selon le rôle :

- **Responsable du traitement** : Détermine les finalités et les moyens du traitement → Les obligations complètes de Niveau 1 s'appliquent (RGPD Articles 5–39)
- **Sous-traitant** : Traite pour le compte d'un responsable du traitement → Les obligations spécifiques au sous-traitant s'appliquent (RGPD Article 28 ; ISO 27701 Annexe A.2)
- **Les deux** : Lorsque l'organisation agit comme responsable du traitement pour certains traitements et sous-traitant pour d'autres → Les obligations s'appliquent par activité de traitement

**Étape 4 : Classifier et documenter**

| Constat | Action |
|---------|--------|
| Réglementation applicable — sans conditions | Classer Niveau 1 (Obligatoire) |
| Réglementation applicable uniquement si condition remplie | Classer Niveau 2 (Conditionnel) — documenter le déclencheur |
| Norme fournissant des orientations — non légalement exécutoire | Classer Niveau 3 (Informatif) |
| Réglementation explicitement non applicable | Documenter comme Non Applicable avec justification |

**Étape 5 : Mettre à jour les enregistrements**

Mettre à jour le Registre réglementaire de protection des données (tenu dans le référentiel de documentation SGDP) avec la détermination, la justification et la date de révision.

---

## Modèle de matrice d'applicabilité réglementaire en matière de protection des données

Utiliser ce modèle pour documenter l'applicabilité de chaque réglementation :

| Réglementation | Niveau | S'applique ? | Déclencheur | Date d'évaluation | Évaluateur | Prochaine révision |
|---------------|--------|-------------|------------|-------------------|-----------|-------------------|
| RGPD UE | 1 | Oui/Non | Traitement de personnes concernées UE | [Date] | DPD | Annuellement |
| LPD suisse | 1 | Oui/Non | Opérations suisses | [Date] | DPD | Annuellement |
| ISO 27701:2025 | 1/2 | Oui/Non | Certification recherchée | [Date] | RSSI | Annuellement |
| ISO 27018:2025 | 2 | Oui/Non | Sous-traitant DCP cloud | [Date] | RSSI | Annuellement |
| UK GDPR | 2 | Oui/Non | Personnes concernées britanniques | [Date] | DPD/Juridique | Annuellement |
| LGPD | 2 | Oui/Non | Personnes concernées brésiliennes | [Date] | Juridique | Annuellement |
| PIPL | 2 | Oui/Non | Personnes concernées chinoises | [Date] | Juridique | Annuellement |

---

## Quand réévaluer

| Événement déclencheur | Action requise |
|----------------------|---------------|
| Nouveau marché géographique | Évaluation complète d'applicabilité pour cette juridiction |
| Nouvelle activité de traitement (nouveau produit, service, type de données) | Rôle responsable/sous-traitant + réglementations applicables |
| Passage du traitement local au cloud | Évaluation ISO 27018:2025 |
| Contrat client avec exigences explicites de protection des données | Mise à jour du niveau spécifique au contrat |
| Nouvelle réglementation publiée ou adoptée | Évaluer l'applicabilité, mettre à jour le registre |
| Réglementation existante substantiellement modifiée | Réévaluer la classification du niveau concerné |
| Publication d'ISO 27017:2026 | Mettre à jour la référence Niveau 3 ; évaluer l'impact sur les packs de contrôle |
| Changement d'activité (acquisition, nouvelle entité, externalisation) | Réévaluation complète d'applicabilité pour les activités concernées |

---

# Utilisation dans les politiques SGDP

## Langage de référence standard

Toutes les politiques des groupes de contrôle SGDP (PRIV-POL-01 et tous les POL des groupes de contrôle PRIV-POL-A.x.x) DOIVENT inclure une section **Cadre réglementaire** utilisant cette référence standard :

```
## Cadre réglementaire

Cette politique s'inscrit dans le cadre réglementaire de protection des données
établi dans PRIV-POL-00.
Les obligations suivantes sont pertinentes pour ce groupe de contrôle :

**Obligatoire (Niveau 1) :**
- RGPD UE : [articles spécifiques pertinents pour ce groupe de contrôle]
- LPD suisse : [articles spécifiques]
- ISO/IEC 27701:2025 : [clauses/contrôles spécifiques]

**Conditionnel (Niveau 2) :**
- ISO/IEC 27018:2025 : [contrôles Annexe A, si packs sous-traitants]

**Informatif (Niveau 3) :**
- ISO/IEC 27017:2015 : [si contrôles liés au cloud]
```

## Étiquetage des rôles dans les packs de contrôle

Les politiques des groupes de contrôle DOIVENT indiquer clairement le rôle organisationnel concerné :

- Packs `privacy-controller/` → **« Cette politique s'applique à l'organisation agissant en tant que Responsable du traitement des DCP. »**
- Packs `privacy-processor/` → **« Cette politique s'applique à l'organisation agissant en tant que Sous-traitant des DCP. »**
- Packs `privacy-shared/` → **« Cette politique s'applique à l'organisation agissant à la fois comme Responsable du traitement et comme Sous-traitant des DCP. »**

---

# Cadre réglementaire (cette politique)

## Conformité obligatoire

| Réglementation | Version | Statut | Pertinence pour le SGDP |
|---------------|---------|--------|------------------------|
| RGPD UE | 2016/679 | En vigueur — Obligatoire | Tous les groupes de contrôle PRIV-POL-A.x.x |
| LPD suisse/nLPD | RS 235.1 (2023) | En vigueur — Obligatoire | Tous les groupes de contrôle PRIV-POL-A.x.x |

## Applicabilité conditionnelle

| Réglementation | Version | Statut | Déclencheur |
|---------------|---------|--------|------------|
| ISO/IEC 27701:2025 | Éd. 2, 2025 | Conditionnel | Certification recherchée ou contractuellement requise |
| ISO/IEC 27018:2025 | Éd. 3, 2025 | Conditionnel | Services cloud de sous-traitant de DCP |
| UK GDPR + DUA Act 2025 | 2018/2021/2025 | Conditionnel | Personnes concernées britanniques |
| LGPD | 2018 | Conditionnel | Personnes concernées brésiliennes |
| PIPL | 2021 | Conditionnel | Personnes concernées chinoises |

## Référence informative

| Norme | Version | Statut | Utilisation |
|------|---------|--------|------------|
| ISO/IEC 27017:2015 | 2015 | En vigueur — Niveau 3 | Base de sécurité cloud (supporte la mise en œuvre 27018) |
| ISO/IEC 27017:2026 | Publiée (2026) | Actions à la publication en attente | Remplace l'édition 2015 |
| ISO/IEC 27002:2022 | 2022 | En vigueur — Niveau 3 | Orientations sur les contrôles de sécurité pour les contrôles partagés A.3 |
| NIST Privacy Framework | 2.0, 2024 | En vigueur — Niveau 3 | Méthodologie de gestion des risques de protection des données |

## Références d'audit

| Exigence | Preuve | Emplacement |
|---------|--------|------------|
| Applicabilité réglementaire documentée | Cette politique + Registre réglementaire de protection des données | Référentiel de documentation SGDP |
| Enregistrements APD à jour | Certificats d'enregistrement | Dossier Juridique/Conformité |
| RADT tenu | Registres des activités de traitement | [Plateforme GRC / Système SGSI] |
| Processus AIPD documenté | Modèle AIPD + AIPD complétées | [Plateforme GRC] |
| Contrats de sous-traitance en place | AVV signés per RGPD Art. 28 | Référentiel des contrats |

---

# Statut réglementaire actuel

## Niveau 1 : Conformité obligatoire (Actif)

| Réglementation | Base d'applicabilité | Confirmé | Prochaine révision |
|---------------|---------------------|---------|-------------------|
| RGPD UE | Traitement de données personnelles UE | [Date] | [Date + 12M] |
| LPD suisse | Opérations basées en Suisse | [Date] | [Date + 12M] |

## Niveau 2 : Applicabilité conditionnelle

| Réglementation | Statut actuel | Statut du déclencheur | Action |
|---------------|--------------|----------------------|--------|
| ISO 27701:2025 | [Applicable / Non applicable] | [Certification recherchée ou contractuellement requise ?] | [Traiter comme engagement contraignant si applicable] |
| ISO 27018:2025 | [Applicable / Non applicable] | [Services cloud de sous-traitant DCP dans le périmètre ?] | [Mettre en œuvre l'overlay Annexe A si applicable] |
| UK GDPR + DUA Act 2025 | [Applicable / Non applicable] | [Personnes concernées britanniques dans le périmètre ?] | [Documenter si applicable ; surveiller les orientations ICO DUA] |
| LGPD | [Applicable / Non applicable] | [Personnes concernées brésiliennes dans le périmètre ?] | [Évaluer si applicable] |
| PIPL | [Applicable / Non applicable] | [Personnes concernées chinoises dans le périmètre ?] | [Évaluer si applicable] |

## Niveau 3 : Référence informative (Utilisation active)

| Norme | Utilisation | Référencé dans |
|------|-----------|--------------|
| ISO/IEC 27017:2015 | Base de sécurité cloud | Packs sous-traitants priv-a.2.4 et priv-a.2.5 |
| ISO/IEC 27002:2022 | Orientations sur les contrôles de sécurité | Tous les packs de contrôle partagés A.3 |
| NIST Privacy Framework 2.0 | Référence de méthodologie des risques | Documentation d'évaluation des risques SGDP |

---

# Maintenance et mises à jour

## Programme de révision

| Type de révision | Fréquence | Responsable | Livrable |
|-----------------|-----------|------------|---------|
| Révision annuelle complète | Annuelle (T4) | DPD + RSSI + Juridique | Politique mise à jour + note à la direction |
| Surveillance trimestrielle | Trimestrielle | DPD + Juridique | Mise à jour du journal de surveillance réglementaire |
| Évaluation déclenchée | Sur événement déclencheur | DPD (lead) | Rapport d'évaluation déclenchée |
| Évaluation d'impact ISO 27017:2026 | Une fois les actions à la publication réalisées | RSSI | Évaluation de l'impact sur les packs de contrôle |

## Sources de surveillance réglementaire

| Source | Fréquence de surveillance | Responsable |
|--------|--------------------------|------------|
| Journal officiel UE (eur-lex.europa.eu) | Mensuelle | Juridique |
| Lignes directrices et avis du CEPD (edpb.europa.eu) | Mensuelle | DPD |
| Publications du PFPDT (edoeb.admin.ch) | Trimestrielle | DPD |
| ISO.org — publications SC 27 | Trimestrielle | RSSI |
| Orientations de l'ICO (UK) | Trimestrielle (si UK dans le périmètre) | Juridique |
| Orientations des APD nationales (États membres) | Trimestrielle | DPD |

## Communication

Les modifications apportées à cette politique DOIVENT être communiquées à :

- Tous les propriétaires de politiques des groupes de contrôle SGDP
- Champions de la protection des données / propriétaires des données
- Sous-traitants sous contrat avec l'organisation
- Audit interne

---

# Documents connexes

| Document | Type | Relation |
|---------|------|---------|
| ISMS-POL-00 | Politique SGSI | Parent — cadre réglementaire de sécurité de l'information |
| PRIV-POL-01 | Politique SGDP | Politique sœur — gouvernance et prise de décisions en matière de protection des données |
| priv-a.1.2.6-9 POL | Politique de groupe de contrôle | Gouvernance et registres de la protection des données (responsable du traitement) |
| priv-a.3.13-16 POL | Politique de groupe de contrôle | Conformité et audit en matière de protection des données (partagé) |
| ISO/IEC 27701:2025 | Norme | Norme de gouvernance principale |
| ISO/IEC 27018:2025 | Norme | Norme complémentaire pour les sous-traitants DCP en cloud |

---

# Glossaire

| Terme | Définition |
|-------|-----------|
| **DCP** | Données à Caractère Personnel — toute information pouvant être utilisée pour identifier directement ou indirectement une personne physique (équivalent à « données personnelles » dans le RGPD/LPD) |
| **Personne concernée** | La personne physique à laquelle se rapportent les DCP (équivalent à « PII Principal ») |
| **Responsable du traitement** | L'entité qui détermine les finalités et les moyens du traitement des DCP (RGPD : « data controller ») |
| **Sous-traitant** | L'entité qui traite les DCP pour le compte d'un responsable du traitement (RGPD : « data processor ») |
| **Traitement** | Toute opération effectuée sur les DCP : collecte, enregistrement, conservation, adaptation, consultation, utilisation, communication, effacement |
| **SGDP** | Système de Gestion de la Protection des Données — le cadre de système de management établi selon ISO/IEC 27701:2025 |
| **APD** | Autorité de Protection des Données — l'autorité de contrôle responsable de l'application de la loi sur la protection des données dans une juridiction |
| **AIPD** | Analyse d'Impact relative à la Protection des Données — évaluation structurée des activités de traitement à haut risque |
| **RADT** | Registre des Activités de Traitement — documentation requise par l'Article 30 du RGPD et l'Article 12 de la LPD |
| **Obligatoire** | Obligation légale, exécutoire par l'APD ou un tribunal, le non-respect a des conséquences |
| **Conditionnel** | S'applique uniquement si des déclencheurs spécifiques sont atteints (juridiction, type de données, rôle, certification) |
| **Informatif** | Référence pour les meilleures pratiques, non légalement exécutoire, adoption volontaire |
| **Niveau 1** | Conformité obligatoire (légale, contractuelle) |
| **Niveau 2** | Conformité conditionnelle (selon le contexte) |
| **Niveau 3** | Référence informative (meilleures pratiques, volontaire) |
| **Déclencheur d'applicabilité** | Événement ou condition qui rend applicable une réglementation de Niveau 2 |
| **Surveillance réglementaire** | Révision trimestrielle systématique des changements réglementaires et des activités organisationnelles pour détecter les changements d'applicabilité |


---

# Déclaration de clôture

Cette politique établit l'applicabilité réglementaire en matière de protection des données pour le Système de Gestion de la Protection des Données de l'organisation.

**Ce que cette politique établit :**

- L'identification des réglementations de protection des données applicables (obligatoires, conditionnelles, informatives)
- La méthodologie d'évaluation pour déterminer l'applicabilité réglementaire en matière de protection des données
- Les processus de révision et de mise à jour pour les changements réglementaires

**Ce que cette politique n'établit PAS :**

- Les décisions de traitement des risques de protection des données (traitées dans la gestion des risques SGDP et les IMP des groupes de contrôle)
- Les exigences de mise en œuvre des contrôles (traitées dans les POL et IMP des groupes de contrôle PRIV-POL-A.x.x)
- Le statut de conformité ou la vérification (traités dans les processus de suivi de la conformité)
- Les obligations de sécurité de l'information (traitées dans ISMS-POL-00)

**Séparation des responsabilités :**

- **Cette politique (PRIV-POL-00)** : Définit QUELLES réglementations de protection des données s'appliquent
- **PRIV-POL-01** : Définit COMMENT le SGDP est géré et COMMENT les décisions sont prises
- **POL des groupes de contrôle (PRIV-POL-A.x.x)** : Définissent CE QUE l'organisation doit faire par domaine de contrôle
- **IMP des groupes de contrôle** : Définissent COMMENT mettre en œuvre les exigences de contrôle
- **Suivi de la conformité** : Vérifie et suit le statut de CONFORMITÉ

---

**FIN DE PRIV-POL-00**

*« L'applicabilité réglementaire en matière de protection des données est le fondement. La mise en œuvre et la conformité sont la structure construite sur ce fondement. »*

<!-- QA_VERIFIED: 2026-04-03 -->
