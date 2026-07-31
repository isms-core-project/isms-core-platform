<!-- ISMS-CORE:POLICY:ISMS-POL-00-FR:framework:POL:00 -->
**ISMS-POL-00 — Cadre d'applicabilité réglementaire**
**Référence faisant autorité pour les obligations de conformité du SMSI**

---

## Contrôle du document

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Cadre d'applicabilité réglementaire |
| **Type de document** | Politique |
| **Identifiant du document** | ISMS-POL-00 |
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
| 0.1 | [Date - 8 semaines] | RSSI | Brouillon initial — structure à trois niveaux |
| 0.2 | [Date - 6 semaines] | RSSI + Juridique | Ajout DORA, NIS2, AI Act (réglementations conditionnelles) |
| 0.3 | [Date - 4 semaines] | DPD | Développement des sections RGPD/nLPD, ajout de la méthodologie d'évaluation |
| 0.4 | [Date - 2 semaines] | RSSI/Juridique/DPD | Intégration des retours des parties prenantes lors de la revue de politique |
| 1.0 | [Date] | RSSI/Juridique/DPD | Version approuvée initiale pour l'audit de phase 1 |

**Cycle de révision** : Annuel (ou lors de modifications réglementaires significatives)
**Prochaine date de révision** : [Date d'entrée en vigueur + 12 mois]

**Chaîne d'approbation** :

- Principale : Responsable de la Sécurité des Systèmes d'Information (RSSI)
- Secondaire : Responsable juridique/conformité
- Conformité : Délégué à la Protection des Données (DPD)
- Autorité finale : Direction générale

**Documents connexes** :

- Tous les documents de politique du SMSI (référence obligatoire)
- ISO/IEC 27001:2022 Clause 4.1 (Compréhension de l'organisation et de son contexte)
- ISO/IEC 27001:2022 Clause 4.2 (Compréhension des besoins et attentes des parties intéressées)

**Références détaillées des exigences** (conservées pour les réglementations conditionnelles — voir Section 8.3) :

- ISMS-REF-DORA — Référence des exigences du Digital Operational Resilience Act
- ISMS-REF-EU-AI-ACT — Référence des exigences du règlement européen sur l'intelligence artificielle
- ISMS-REF-FINMA — Référence des exigences de la Circulaire FINMA 2023/1
- ISMS-REF-NIS2 — Référence des exigences de la Directive sur la sécurité des réseaux et de l'information 2
- ISMS-REF-PCI-DSS — Référence des exigences du standard de sécurité des données de l'industrie des cartes de paiement

**Distribution** : Toutes les parties prenantes du SMSI, auteurs de politiques, propriétaires de systèmes, auditeurs
**Référencé par** : Tous les documents de politique du SMSI

**Stratégie linguistique** : Lorsque des termes techniques ou réglementaires sont internationalement établis (p. ex. RGPD, ISO/IEC, NIST), la terminologie anglaise est conservée afin de préserver la précision et de faciliter les références réglementaires transfrontalières.

---

## Résumé exécutif

Ce document constitue la **référence faisant autorité** pour l'interprétation de l'applicabilité réglementaire et des référentiels au sein de l'ensemble du Système de Management de la Sécurité de l'Information (SMSI).

**Objet** : Éliminer l'ambiguïté et les incohérences dans la façon dont les réglementations et les référentiels sont référencés dans la documentation du SMSI (politiques, procédures, contrôles).

**Périmètre** : Toutes les références aux lois, réglementations, normes et référentiels dans la documentation du SMSI.

**Principe clé** : **L'applicabilité réglementaire doit être explicite, non présumée.** Les références aux réglementations et référentiels se répartissent en trois catégories :

1. **Conformité obligatoire** — Obligations légales qui s'appliquent à l'organisation
2. **Applicabilité conditionnelle** — Exigences qui ne s'appliquent que sous des conditions spécifiques
3. **Référence informative** — Bonnes pratiques et orientations techniques

**Utilisation** : Toutes les politiques du SMSI DOIVENT inclure une Section 1.3 référençant ce cadre, ou inclure une section « Cadre réglementaire » intégrant directement ces catégories.

**Termes clés** : Les définitions des termes utilisés tout au long de cette politique (Obligatoire, Conditionnel, Niveau 1/2/3, Déclencheur d'applicabilité, etc.) figurent dans le **Glossaire** en fin de document.

---

## Autorité et périmètre de la politique

### Objet et périmètre de cette politique

Cette politique définit l'**identification et l'applicabilité** des exigences légales, réglementaires, statutaires et contractuelles pour le Système de Management de la Sécurité de l'Information de l'organisation.

**Cette politique établit :**

- Quelles réglementations et normes s'appliquent à l'organisation
- La catégorisation des obligations réglementaires (Obligatoire, Conditionnel, Informatif)
- La méthodologie d'évaluation pour déterminer l'applicabilité
- Les processus de révision et de mise à jour face aux évolutions du paysage réglementaire

**Cette politique N'ÉTABLIT PAS :**

- Les décisions de traitement des risques (traitées dans la Clause 6 — Management des risques)
- Les exigences de mise en œuvre des contrôles (traitées dans les contrôles de l'Annexe A)
- Le statut de conformité ou la vérification (traités dans les processus de surveillance de la conformité)

Le résultat de l'évaluation d'applicabilité réglementaire constitue une **entrée** pour :

- Les décisions de délimitation des contrôles au sein de l'Annexe A
- La priorisation de l'évaluation et du traitement des risques
- Les décisions de proportionnalité pour la mise en œuvre des contrôles
- La planification des audits et la vérification de la conformité

**Principe de délimitation** : Cette politique établit l'applicabilité réglementaire. La mise en œuvre, l'application et la vérification sont gérées par des processus distincts du SMSI.

**Intégration avec la Clause 4 d'ISO 27001 :**

- **Clause 4.1 (Contexte de l'organisation)** : Cette politique traite du contexte externe (environnement légal/réglementaire). Le contexte interne (structure organisationnelle, technologie, culture) est traité dans le Document de contexte du SMSI.
- **Clause 4.2 (Parties intéressées)** : Les exigences des parties intéressées (obligations clients, attentes réglementaires) identifiées via ce cadre alimentent le registre des parties intéressées tenu dans le Document de contexte du SMSI.

**Intégration avec l'évaluation des risques (Clause 6) :**

Les obligations réglementaires identifiées dans cette politique alimentent :

- **ISMS-RISK-METHODOLOGY** (Clause 6.1.2 Évaluation des risques) : Les exigences réglementaires sont traitées comme des facteurs de risque externes avec une priorité inhérente (Niveau 1 = priorité élevée, Niveau 2 conditionnel = priorité moyenne si applicable, Niveau 3 = entrée informative)
- **ISMS-RISK-TREATMENT** (Clause 6.1.3 Traitement des risques) : La sélection et la priorisation des contrôles tiennent compte des obligations réglementaires en parallèle du risque technique
- **Déclaration d'applicabilité (SoA)** : La justification de l'applicabilité des contrôles référence les assignations de niveaux POL-00

---

**Catégories d'applicabilité réglementaire**

**Définitions des catégories**

**Conformité obligatoire**
Obligations légales ou contractuelles auxquelles l'organisation DOIT se conformer. Le non-respect entraîne une responsabilité légale, des amendes réglementaires, une rupture de contrat ou une perte de certification.

**Caractéristiques** :

- Applicable en vertu de la loi ou du contrat
- Le non-respect a des conséquences légales/financières
- Nécessite des preuves documentées de conformité
- Soumis aux audits et inspections réglementaires

**Référence informative / Alignement sur les bonnes pratiques**
Référentiels et normes utilisés à titre d'orientation technique, d'étalonnage ou d'alignement volontaire. Ils guident les pratiques de sécurité mais ne constituent pas des exigences de conformité obligatoire, sauf si explicitement requis par un contrat ou une réglementation.

**Caractéristiques** :

- Adoption volontaire pour les bonnes pratiques
- Aucun mécanisme d'application légale
- Utilisé à titre d'orientation pour la mise en œuvre technique
- Peut devenir obligatoire s'il est référencé dans des contrats

**Applicabilité conditionnelle**
Exigences qui ne s'appliquent que lorsque des conditions spécifiques sont remplies (p. ex., secteur d'activité, localisation géographique, type de service, contrats clients, périmètre réglementaire).

**Caractéristiques** :

- L'applicabilité dépend du contexte organisationnel
- Peut devenir obligatoire selon les activités de l'entreprise
- Nécessite une réévaluation périodique à mesure que l'activité évolue
- Exemples : PCI DSS v4.0.1 (uniquement si traitement des paiements par carte), HIPAA (uniquement si traitement de données de santé américaines)

**Clarification sur la classification par niveaux** : La classification par niveaux (Obligatoire, Conditionnel, Informatif) détermine la **force contraignante réglementaire** et n'implique pas en soi d'obligations de mise en œuvre. Les décisions de mise en œuvre sont prises via le processus d'évaluation et de traitement des risques, en tenant compte des exigences réglementaires ainsi que d'autres facteurs tels que l'appétit pour le risque, le contexte métier et la faisabilité technique.

## Hiérarchie de conformité

```
┌─────────────────────────────────────────────────────────────────┐
│                    HIÉRARCHIE DE CONFORMITÉ                     │
├─────────────────────────────────────────────────────────────────┤
│  NIVEAU 1 : OBLIGATOIRE (Légal/Contractuel)                     │
│  • Loi fédérale suisse sur la protection des données (nLPD)     │
│  • RGPD de l'UE (lors du traitement de données personnelles UE) │
│  • ISO/IEC 27001:2022 (pour la certification)                   │
│  • Réglementations sectorielles (selon applicabilité)           │
│  • Contrats clients (exigences de sécurité explicites)          │
│                                                                 │
│  NIVEAU 2 : CONDITIONNEL (Selon le contexte)                    │
│  • DORA (si entité de services financiers UE)                   │
│  • NIS2 (si entité essentielle/importante dans l'UE)            │
│  • PCI DSS v4.0.1 (si traitement de cartes de paiement)         │
│  • HIPAA (si traitement de données de santé américaines)        │
│  • Réglementations sectorielles (selon le secteur)              │
│                                                                 │
│  NIVEAU 3 : INFORMATIF (Bonnes pratiques)                       │
│  • NIST SP 800 (orientations techniques)                        │
│  • CIS Controls (référentiels de sécurité)                      │
│  • OWASP (sécurité applicative)                                 │
│  • Référentiels sectoriels (à titre de référence uniquement)    │
└─────────────────────────────────────────────────────────────────┘
```

> *Si les caractères de dessin de boîte ne s'affichent pas correctement, consultez les Sections 3 à 5 pour les définitions de niveaux.*

---

# Conformité obligatoire (Niveau 1)

## Loi fédérale suisse sur la protection des données (nLPD/nDSG)

**Applicabilité** : Toutes les opérations de l'organisation établie en Suisse ou servant des clients suisses

**Exigences clés** :

- Article 6 : Principes (licéité, proportionnalité, limitation de la finalité)
- Article 7 : Sécurité des données (mesures techniques et organisationnelles appropriées)
- Article 8 : Traitement des données par des sous-traitants
- Article 19 : Droit à l'information (droits des personnes concernées)
- Article 328b CO (Code des obligations) : Surveillance des employés et protection de la personnalité

**Impact sur le SMSI** :

- Protection des données dès la conception et par défaut
- Mesures de sécurité technique (chiffrement, contrôle d'accès)
- Transparence et proportionnalité de la surveillance des employés
- Registres de traitement des données (Art. 12)
- Notification des violations de données (Art. 24)

**Référence** : Loi fédérale sur la protection des données (RS 235.1), en vigueur depuis le 1er septembre 2023

## Règlement général sur la protection des données de l'UE (RGPD)

**Applicabilité** : Lors du traitement de données personnelles de résidents de l'UE

**Exigences clés** :

- Article 5 : Principes relatifs au traitement (licéité, loyauté, transparence, limitation de la finalité)
- Article 6 : Base légale du traitement
- Article 24 : Responsabilités du responsable du traitement (responsabilisation)
- Article 25 : Protection des données dès la conception et par défaut
- Article 28 : Obligations du sous-traitant (contrats, mesures de sécurité)
- Article 32 : Sécurité du traitement (chiffrement, pseudonymisation, résilience)
- Article 33 : Notification des violations (72 heures à l'autorité de contrôle)
- Article 35 : Analyse d'impact relative à la protection des données (AIPD) pour les traitements à haut risque

**Impact sur le SMSI** :

- Mesures techniques et organisationnelles (MTO)
- Chiffrement et pseudonymisation
- Contrôles d'accès et authentification
- Procédures de réponse aux violations de données
- Gestion des fournisseurs (accords de sous-traitance)
- Analyses d'impact sur la vie privée

**Référence** : Règlement (UE) 2016/679, en vigueur depuis le 25 mai 2018

## ISO/IEC 27001:2022

**Applicabilité** : Lorsque l'organisation cherche à obtenir la certification ISO 27001

**Exigences clés** :

- Contrôles de l'Annexe A (93 contrôles organisationnels, humains, physiques et technologiques)
- Clause 4 : Contexte de l'organisation
- Clause 5 : Leadership et engagement
- Clause 6 : Évaluation et traitement des risques
- Clause 7 : Support (ressources, compétences, sensibilisation, communication, informations documentées)
- Clause 8 : Activités opérationnelles (traitement des risques, évaluation)
- Clause 9 : Évaluation des performances (surveillance, audit interne, revue de direction)
- Clause 10 : Amélioration (non-conformité, actions correctives, amélioration continue)

**Impact sur le SMSI** :

- Mise en œuvre du cadre de politiques
- Méthodologie de management des risques
- Mise en œuvre des contrôles et constitution des preuves
- Programme d'audit interne
- Processus de revue de direction
- Amélioration continue

**Référence** : ISO/IEC 27001:2022 — Systèmes de management de la sécurité de l'information

## Réglementations obligatoires supplémentaires

Les organisations devraient documenter les réglementations obligatoires supplémentaires selon leur contexte spécifique :

| Réglementation | Déclencheur | Exemples |
|----------------|-------------|----------|
| **Droit du travail** | Employés dans une juridiction | Codécision des comités d'entreprise (Allemagne), lois sur la surveillance des employés |
| **Réglementations financières** | Services financiers | FINMA (Suisse), BaFin (Allemagne), MiFID II (UE) |
| **Télécommunications** | Services de télécom | Interception légale, conservation des données |
| **Contrôle des exportations** | Opérations transfrontalières | Biens à double usage, exportation de cryptographie |
| **Droit des contrats** | Accords clients | Exigences de sécurité explicites dans les contrats de service |

---

# Applicabilité conditionnelle (Niveau 2)

Ces réglementations s'appliquent **uniquement lorsque des conditions métier spécifiques sont remplies** :

## Autorité fédérale de surveillance des marchés financiers (FINMA)

**Réglementation** : Autorité fédérale de surveillance des marchés financiers (Eidgenössische Finanzmarktaufsicht)
**Principales circulaires** :

- Circulaire FINMA 2023/1 (Risques opérationnels et résilience — banques, en vigueur depuis le 1er janvier 2024)
- Circulaire FINMA 2008/7 (Externalisation — banques)
- Circulaire FINMA 2018/3 (Externalisation — assureurs)

**Déclencheurs d'applicabilité** :

- L'organisation est un **établissement financier suisse** réglementé par la FINMA :
  - Banques (licence bancaire FINMA)
  - Négociants en valeurs mobilières (licence de négociant en valeurs mobilières)
  - Compagnies d'assurance (licence d'assurance)
  - Fournisseurs d'infrastructures des marchés financiers (bourses, dépositaires centraux)
  - Organismes de placement collectif (licences de gestion de fonds)

**Exigences clés** :

- **Résilience opérationnelle** : Gestion des risques liés aux TIC, continuité des activités, reprise après sinistre
- **Externalisation** : Gestion des risques tiers, diligence raisonnable, contrats, stratégies de sortie
- **Protection des données** : Sécurité, confidentialité et disponibilité des données clients
- **Déclaration d'incidents** : Incidents opérationnels significatifs à la FINMA
- **Contrôles internes** : Gouvernance, gestion des risques, audit interne
- **Registre de sous-externalisation** (Circulaire FINMA 2023/1 Section 15) : Les banques doivent tenir un registre des arrangements de sous-externalisation où les prestataires délèguent davantage des services matériels. Le registre doit documenter : identité du sous-traitant, services fournis, accès aux données, localisation géographique, évaluation des risques, statut d'approbation.

**Impact sur le SMSI** :

- Contrôles renforcés de continuité des activités et de reprise après sinistre
- Gestion complète des risques tiers (A.5.19-23)
- Procédures de réponse aux incidents et de déclaration (A.5.24-28)
- Structures de gouvernance et de supervision (A.5.1, 5.4)
- Transparence et approbation de la sous-externalisation (A.5.19-23 S3 : Sécurité de la chaîne d'approvisionnement TIC)

**Évaluation** : Si l'organisation détient une licence ou un enregistrement FINMA → **Conformité obligatoire**

### Exigences de sous-externalisation (Circulaire FINMA 2023/1)

Pour les banques suisses soumises à la Circulaire FINMA 2023/1, les exigences de sous-externalisation suivantes s'appliquent :

**Définition de la sous-externalisation :**
Services matériels externalisés par une banque à un prestataire de services, où ce dernier délègue à son tour ces services à un sous-traitant (sous-fournisseur).

**Exigences du registre :**
- Tenir un registre complet de tous les arrangements de sous-externalisation
- Mettre à jour le registre lors de tout nouveau cas ou modification
- Inclure dans le registre :
  - Nom et juridiction du sous-traitant
  - Services fournis (description et criticité)
  - Accès aux données et activités de traitement
  - Localisation géographique de la prestation de services
  - Évaluation des risques et mesures d'atténuation
  - Statut d'approbation FINMA (si requis)

**Exigences d'approbation :**
- La sous-externalisation matérielle requiert l'approbation de la banque avant mise en œuvre
- La banque doit évaluer les risques de sous-externalisation (opérationnels, concentration, protection des données, juridiction)
- Répercussion contractuelle des exigences de la banque aux sous-traitants
- Droit d'audit des sous-traitants (directement ou via le prestataire)

**Mise en œuvre :**
- Registre de sous-externalisation tenu dans ISMS-IMP-A.5.23.2 (classeur de diligence raisonnable — feuille sous-fournisseurs)
- Évaluation des risques des sous-traitants documentée dans ISMS-IMP-A.5.23.4 (classeur de gouvernance)
- Flux d'approbation intégré au processus d'intégration des fournisseurs (Section 8 : Gestion du cycle de vie)

## Digital Operational Resilience Act (DORA)

**Réglementation** : Règlement (UE) 2022/2554 sur la résilience opérationnelle numérique du secteur financier
**Date d'entrée en vigueur** : 17 janvier 2025

**Déclencheurs d'applicabilité** :

- L'organisation est une **entité financière dans l'UE** :
  - Établissements de crédit (banques)
  - Établissements de paiement et établissements de monnaie électronique
  - Entreprises d'investissement
  - Prestataires de services sur crypto-actifs
  - Entreprises d'assurance et de réassurance
  - Fournisseurs tiers de services TIC aux entités financières (désignation critique/importante)

**Exigences clés** :

- **Gestion des risques liés aux TIC** : Cadre complet couvrant l'identification, la protection, la détection, la réponse et le rétablissement
- **Déclaration des incidents** : Incidents majeurs liés aux TIC aux autorités compétentes
- **Tests de résilience opérationnelle numérique** : Tests réguliers incluant des tests de pénétration basés sur la menace (TLPT)
- **Risques tiers** : Supervision des prestataires TIC, contrats, stratégies de sortie
- **Partage d'informations** : Échange d'informations sur les menaces et la cybersécurité

**Impact sur le SMSI** :

- Cadre avancé de gestion des risques TIC (au-delà d'ISO 27001)
- Détection et réponse renforcées aux incidents (A.5.24-28)
- Programmes de tests de résilience obligatoires
- Gestion des risques fournisseurs avec supervision réglementaire (A.5.19-23)
- Arrangements de partage d'informations

**Évaluation** : Si l'organisation est une entité financière UE ou un fournisseur TIC critique → **Conformité obligatoire**

## Directive sur la sécurité des réseaux et de l'information 2 (NIS2)

**Directive** : Directive (UE) 2022/2555 sur des mesures destinées à assurer un niveau élevé commun de cybersécurité
**Date limite de transposition** : 17 octobre 2024 (les États membres de l'UE doivent transposer en droit national)

**Déclencheurs d'applicabilité** :

- L'organisation est une **entité essentielle ou importante** dans l'UE dans les secteurs couverts :

**Entités essentielles** (exigences plus strictes) :

- Énergie (électricité, pétrole, gaz)
- Transports (aérien, ferroviaire, maritime, routier)
- Secteur bancaire et infrastructures des marchés financiers
- Santé (prestataires de soins, laboratoires de référence UE, fabricants pharmaceutiques)
- Eau potable et eaux usées
- Infrastructures numériques (points d'échange Internet, fournisseurs DNS, cloud, centres de données, CDN, prestataires de services de confiance)
- Gestion des services TIC (MSP, MSSP)
- Administration publique (entités gouvernementales centrales)
- Espace (infrastructures terrestres pour les systèmes spatiaux)

**Entités importantes** (exigences moins strictes) :

- Services postaux et de courrier
- Gestion des déchets
- Production et distribution de produits chimiques
- Production et distribution alimentaire
- Fabrication (dispositifs médicaux, électronique, machines, véhicules automobiles, aérospatial)
- Fournisseurs numériques (marchés en ligne, moteurs de recherche, réseaux sociaux)
- Organismes de recherche

**Exigences clés** :

- **Gestion des risques** : Évaluation des risques de cybersécurité et politiques de sécurité
- **Gestion des incidents** : Capacités de détection, réponse et rétablissement
- **Continuité des activités** : Gestion des sauvegardes, reprise après sinistre
- **Sécurité de la chaîne d'approvisionnement** : Gestion des risques tiers
- **Sécurité des réseaux** : Contrôles d'accès, chiffrement, authentification multi-facteurs
- **Notification des incidents** : Alerte précoce sous 24 heures, rapport d'incident détaillé sous 72 heures au CSIRT/autorité compétente nationale
- **Supervision** : Audits périodiques, évaluations de sécurité, surveillance ex post

**Impact sur le SMSI** :

- Gestion complète des risques de cybersécurité (Clause 6)
- Réponse aux incidents avec délais de déclaration réglementaires (A.5.24-28)
- Exigences de sécurité de la chaîne d'approvisionnement (A.5.19-23)
- Contrôles de sécurité technique (chiffrement, contrôle d'accès) (série A.8.x)
- Continuité des activités et reprise après sinistre (A.5.29-30)

**Sanctions** : Jusqu'à 10 millions EUR ou 2 % du chiffre d'affaires annuel mondial (entités essentielles), 7 millions EUR ou 1,4 % (entités importantes)

**Évaluation** : Si l'organisation opère dans un secteur couvert dans l'UE et répond aux seuils de taille/criticité → **Conformité obligatoire**

## Payment Card Industry Data Security Standard (PCI DSS v4.0.1)

**Standard** : PCI DSS v4.0.1 (en vigueur depuis le 31 mars 2024)
**Organisme de gouvernance** : PCI Security Standards Council

**Déclencheurs d'applicabilité** :

- L'organisation **stocke, traite ou transmet** des données de titulaires de carte :
  - Commerçants acceptant les cartes de crédit/débit
  - Processeurs et passerelles de paiement
  - Prestataires de services gérant des données de titulaires de carte
  - Toute entité ayant accès à l'environnement des données de titulaires de carte (CDE)

**Exigences clés** :

- **12 exigences réparties en 6 objectifs de contrôle** :

  1. Installer et maintenir des contrôles de sécurité réseau
  2. Appliquer des configurations sécurisées à tous les composants système
  3. Protéger les données de compte stockées
  4. Protéger les données de titulaires de carte par une cryptographie robuste lors de la transmission
  5. Protéger les systèmes et réseaux contre les logiciels malveillants
  6. Développer et maintenir des systèmes et logiciels sécurisés
  7. Restreindre l'accès aux données de titulaires de carte selon le besoin d'en connaître
  8. Identifier les utilisateurs et authentifier l'accès aux composants système
  9. Restreindre l'accès physique aux données de titulaires de carte
  10. Journaliser et surveiller tout accès aux composants système et aux données de titulaires de carte
  11. Tester régulièrement la sécurité des systèmes et réseaux
  12. Soutenir la sécurité de l'information par des politiques et programmes organisationnels

**Impact sur le SMSI** :

- Segmentation réseau et contrôles de pare-feu (A.8.20-22)
- Chiffrement des données de titulaires de carte au repos et en transit (A.8.24)
- Contrôles d'accès et authentification robustes (A.5.15-18, A.8.2-5)
- Gestion des vulnérabilités et application des correctifs (A.8.8)
- Journalisation, surveillance et pistes d'audit (A.8.15-16)
- Tests de pénétration et analyses de vulnérabilités (A.8.8)

**Validation** : Audit sur site annuel (Niveau 1), Questionnaire d'auto-évaluation (SAQ) pour les petits commerçants

**Évaluation** : Si l'organisation traite des cartes de paiement → **Conformité obligatoire**

## Règlement de l'UE sur l'intelligence artificielle (AI Act)

**Réglementation** : Règlement (UE) 2024/1689 établissant des règles harmonisées sur l'intelligence artificielle
**Date d'entrée en vigueur** : 1er août 2024 (mise en œuvre progressive jusqu'en août 2028)

**Déclencheurs d'applicabilité** :

- L'organisation est un **fournisseur** (développe ou commandite des systèmes d'IA mis sur le marché UE)
- L'organisation est un **déployeur** (utilise des systèmes d'IA sous sa propre autorité dans l'UE)
- L'organisation est un **importateur ou distributeur** de systèmes d'IA dans l'UE
- Les sorties du système d'IA affectent des personnes situées dans l'UE (quelle que soit la localisation du fournisseur)

**Classification des risques** (détermine le niveau d'obligation) :

| Niveau de risque | Exemples | Obligations clés |
|-----------------|----------|-----------------|
| **Inacceptable** | Notation sociale, identification biométrique en temps réel (avec exceptions), techniques de manipulation | **Interdit** |
| **Élevé** | Décisions d'emploi, scoring de crédit, accès aux services essentiels, catégorisation biométrique, infrastructures critiques | Évaluation de conformité, gestion des risques, gouvernance des données, transparence, supervision humaine, documentation |
| **Risque limité** | Chatbots, reconnaissance des émotions, génération de deepfakes | Obligations de transparence (divulgation de l'interaction avec l'IA) |
| **Risque minimal** | Filtres anti-spam, outils de développement assistés par IA, analyses internes | Aucune obligation spécifique (codes de conduite volontaires) |

**Exigences clés (Systèmes à haut risque)** :

- Article 9 : Système de gestion des risques tout au long du cycle de vie du système d'IA
- Article 10 : Gouvernance des données (ensembles de données d'entraînement, de validation et de test)
- Article 11 : Documentation technique
- Article 12 : Tenue de registres et journalisation
- Article 13 : Transparence et information aux déployeurs
- Article 14 : Mesures de supervision humaine
- Article 15 : Exactitude, robustesse et cybersécurité

**Exigences clés (Tous les fournisseurs/déployeurs)** :

- Article 4 : Maîtrise de l'IA pour le personnel opérant des systèmes d'IA
- Article 50 : Transparence pour certains systèmes d'IA (chatbots, contenu synthétique)

**Calendrier de mise en œuvre** :

- **Février 2025** : Interdictions sur les IA à risque inacceptable
- **Août 2025** : Obligations pour les modèles d'IA à usage général
- **Décembre 2027** : Application complète pour les systèmes d'IA à haut risque (reportée d'août 2026 par le Digital Omnibus, Règlement (UE) 2026/1744, en vigueur depuis le 27 juillet 2026)
- **Août 2028** : IA à haut risque dans les produits réglementés (dispositifs médicaux, machines) (reportée d'août 2027 par le même Digital Omnibus)

**Impact sur le SMSI** :

- Inventaire et classification des risques des systèmes d'IA (A.5.9)
- Gestion des risques pour les systèmes d'IA (Clause 6, A.5.7)
- Gouvernance des données et contrôles de qualité (A.5.12-14)
- Journalisation et surveillance des sorties d'IA (A.8.15-16)
- Procédures de supervision humaine (A.5.37)
- Formation du personnel à la maîtrise de l'IA (A.6.3)
- Gestion des fournisseurs pour les composants d'IA (A.5.19-23)
- Documentation et transparence (A.5.37)

**Sanctions** : Jusqu'à 35 millions EUR ou 7 % du chiffre d'affaires annuel mondial (pratiques interdites), 15 millions EUR ou 3 % (autres violations)

**Évaluation** : Si l'organisation développe, déploie ou distribue des systèmes d'IA affectant des personnes dans l'UE → Évaluer la classification des risques et les obligations applicables

## Health Insurance Portability and Accountability Act (HIPAA)

**Réglementation** : Loi fédérale américaine protégeant les informations de santé
**Date d'entrée en vigueur** : 1996 (avec mises à jour via le HITECH Act 2009, Omnibus Rule 2013)

**Déclencheurs d'applicabilité** :

- L'organisation est une **entité couverte** ou un **associé commercial** gérant des informations de santé protégées (PHI) américaines :
  - Prestataires de soins de santé (médecins, hôpitaux, cliniques)
  - Plans de santé (compagnies d'assurance, HMO, Medicare/Medicaid)
  - Centres de compensation des soins de santé
  - Associés commerciaux (fournisseurs, sous-traitants gérant des PHI pour le compte d'entités couvertes)

**Exigences clés** :

- **Règle de sécurité HIPAA** (45 CFR Partie 164) :
  - **Mesures de protection administratives** : Processus de gestion de la sécurité, sécurité du personnel, gestion des accès à l'information, formation à la sensibilisation à la sécurité, planification de la continuité
  - **Mesures de protection physiques** : Contrôles d'accès aux installations, sécurité des postes de travail, contrôles des équipements et supports
  - **Mesures de protection techniques** : Contrôles d'accès, contrôles d'audit, contrôles d'intégrité, sécurité des transmissions (chiffrement)
- **Règle de confidentialité HIPAA** : Droits des patients, accès minimal nécessaire, limitations d'utilisation et de divulgation
- **Règle de notification des violations** : Notification aux personnes concernées (60 jours), HHS, médias (si > 500 personnes affectées)
- **Accords d'associés commerciaux (BAA)** : Contrats obligatoires avec tous les fournisseurs gérant des PHI

**Impact sur le SMSI** :

- Évaluation et gestion des risques (obligatoires selon la Règle de sécurité)
- Contrôles d'accès et authentification (A.5.15-18, A.8.2-5)
- Chiffrement des PHI (A.8.24)
- Journalisation d'audit et surveillance (A.8.15-16)
- Réponse aux incidents et notification des violations (A.5.24-28)
- Formation et sensibilisation du personnel (A.6.3)
- Gestion des associés commerciaux (A.5.19-23)

**Sanctions** : 100 à 50 000 USD par violation (jusqu'à 1,5 million USD par an), sanctions pénales pour négligence délibérée

**Évaluation** : Si l'organisation traite des données de santé américaines (PHI) → **Conformité obligatoire**

## Federal Information Security Management Act (FISMA)

**Réglementation** : Loi fédérale américaine imposant la cybersécurité pour les systèmes gouvernementaux
**Date d'entrée en vigueur** : 2002 (mise à jour par le FISMA Reform Act 2014)

**Déclencheurs d'applicabilité** :

- L'organisation exploite des **systèmes d'information fédéraux** ou fournit des **services cloud à des agences fédérales américaines** :
  - Agences et départements fédéraux
  - Contractants fédéraux et prestataires de services cloud (autorisation FedRAMP)
  - Organisations traitant des informations fédérales

**Exigences clés** :

- **Approche basée sur les risques en cybersécurité** : Suivant les contrôles NIST SP 800-53
- **Catégorisation** : Catégorisation des systèmes (Faible, Modéré, Élevé) selon FIPS 199
- **Mise en œuvre des contrôles** : Contrôles de sécurité NIST SP 800-53 selon le niveau d'impact
- **Surveillance continue** : Évaluation et autorisation de sécurité continues (A&A)
- **FedRAMP (pour le cloud)** : Programme fédéral de gestion des risques et des autorisations
  - Évaluation par des tiers accrédités (3PAO)
  - Autorisation par le JAB (Joint Authorization Board) ou ATO (Authority to Operate) d'agence

**Impact sur le SMSI** :

- Mise en œuvre des contrôles NIST SP 800-53 (contrôles de sécurité complets)
- Catégorisation des systèmes et analyse d'impact (A.5.9)
- Surveillance et évaluation continues (A.8.15-16)
- Gestion des risques de la chaîne d'approvisionnement (A.5.19-23)
- Réponse aux incidents alignée sur les référentiels NIST (A.5.24-28)

**Évaluation** : Si l'organisation a des contrats fédéraux américains ou une autorisation FedRAMP → **Conformité obligatoire**

## Réglementations conditionnelles supplémentaires

Les organisations devraient évaluer l'applicabilité selon le contexte métier :

| Réglementation | Déclencheur d'applicabilité | Région/Périmètre |
|----------------|----------------------------|------------------|
| **Sarbanes-Oxley (SOX)** | Société cotée en bourse américaine | États-Unis |
| **GLBA (Gramm-Leach-Bliley)** | Établissement financier américain | États-Unis |
| **CCPA/CPRA** | Traitement de données de résidents californiens | Californie, États-Unis |
| **PIPL (Chine)** | Traitement d'informations personnelles de résidents chinois | Chine |
| **Privacy Act (Australie)** | Traitement d'informations personnelles australiennes | Australie |
| **PDPA (Singapour)** | Traitement de données personnelles singaporiennes | Singapour |
| **LGPD** | Traitement de données personnelles brésiliennes | Brésil |
| **Sectoriel** | Selon le secteur (télécommunications, énergie, pharma) | Variable |

---

# Référence informative / Bonnes pratiques (Niveau 3)

Ces référentiels fournissent des **orientations techniques et des bonnes pratiques** mais ne sont pas légalement contraignants :

## Publications spéciales NIST (série SP 800)

**Description** : Orientations de cybersécurité du National Institute of Standards and Technology
**Applicabilité** : Adoption volontaire pour les bonnes pratiques (sauf si requis par contrat FISMA/FedRAMP)

**Publications clés** :

- **NIST SP 800-53** : Contrôles de sécurité et de confidentialité (catalogue de contrôles complet)
- **NIST SP 800-171** : Protection des informations non classifiées contrôlées (CUI) dans les systèmes non fédéraux
- **NIST Cybersecurity Framework (CSF)** : Identifier, Protéger, Détecter, Répondre, Rétablir
- **NIST SP 800-61** : Guide de gestion des incidents de sécurité informatique
- **NIST SP 800-63** : Directives sur l'identité numérique (authentification, fédération)

**Utilisation dans le SMSI** :

- Orientations de mise en œuvre technique des contrôles ISO 27001
- Développement de plans d'intervention sur incident (800-61)
- Gestion des identités et des accès (800-63)
- Méthodologies d'évaluation des risques (800-30, 800-37)

## CIS Controls

**Description** : Contrôles de sécurité critiques du Center for Internet Security
**Version** : CIS Controls v8.1 (18 contrôles)
**Applicabilité** : Adoption volontaire pour l'étalonnage de la sécurité

**Contrôles clés** :
1. Inventaire et contrôle des actifs d'entreprise
2. Inventaire et contrôle des actifs logiciels
3. Protection des données
4. Configuration sécurisée des actifs d'entreprise
5. Gestion des comptes
6. Gestion du contrôle d'accès
7. Gestion continue des vulnérabilités
8. Gestion des journaux d'audit
9-18. Contrôles supplémentaires couvrant les sauvegardes, la réponse aux incidents, les tests de pénétration, la formation

**Utilisation dans le SMSI** :

- Pratiques de gestion des actifs (A.5.9)
- Gestion de la configuration (A.8.9)
- Gestion des vulnérabilités (A.8.8)
- Étalonnage de la maturité de la sécurité organisationnelle

## OWASP (Open Web Application Security Project)

**Description** : Normes de sécurité des applications web portées par la communauté
**Applicabilité** : Adoption volontaire pour le développement logiciel sécurisé

**Ressources clés** :

- **OWASP Top 10** : Risques les plus critiques en sécurité des applications web
- **OWASP ASVS** : Standard de vérification de la sécurité des applications
- **OWASP SAMM** : Modèle de maturité de l'assurance logicielle
- **OWASP Cheat Sheets** : Orientations de codage sécurisé

**Utilisation dans le SMSI** :

- Cycle de développement logiciel sécurisé (A.8.25-28)
- Tests de sécurité des applications web
- Formation des développeurs à la sécurité (A.6.3)
- Revue de code et évaluation des vulnérabilités

## ISO/IEC 27002:2022

**Description** : Code de bonnes pratiques pour les contrôles de sécurité de l'information
**Applicabilité** : Orientation complémentaire pour la mise en œuvre d'ISO 27001 (non certifiable séparément)

**Utilisation dans le SMSI** :

- Orientations détaillées de mise en œuvre des contrôles de l'Annexe A
- Sélection et adaptation des contrôles
- Considérations de proportionnalité et d'évolutivité

## Cloud Security Alliance (CSA)

**Description** : Bonnes pratiques de sécurité du cloud computing
**Applicabilité** : Adoption volontaire pour la sécurité du cloud

**Référentiels clés** :

- **CSA Cloud Controls Matrix (CCM)** : Référentiel de contrôles de sécurité du cloud
- **CSA Security Trust Assurance and Risk (STAR)** : Certification des fournisseurs cloud
- **CSA Consensus Assessments Initiative Questionnaire (CAIQ)** : Évaluation de la sécurité cloud

**Utilisation dans le SMSI** :

- Évaluation des fournisseurs de services cloud (A.5.23)
- Architecture de sécurité cloud
- Évaluations de sécurité des fournisseurs

## Référentiels de bonnes pratiques supplémentaires

Les organisations peuvent référencer des référentiels supplémentaires selon le contexte sectoriel :

| Référentiel | Description | Cas d'usage |
|-------------|-------------|-------------|
| **COBIT** | Gouvernance et management des TI | Alignement sur la gouvernance TI |
| **ITIL** | Gestion des services TI | Processus de prestation de services |
| **ISO 22301** | Management de la continuité d'activité | Structure du programme BCM |
| **ISO 27017/27018** | Sécurité et confidentialité dans le cloud | Contrôles spécifiques au cloud |
| **Directives ENISA** | Orientations de l'agence européenne de cybersécurité | Contexte réglementaire UE |

---

# Exigences fédérales américaines (Catégorie spéciale)

**Principe** : Les exigences fédérales américaines de cybersécurité (FISMA, FIPS, FedRAMP, NIST CSF 2.0) s'appliquent **uniquement lorsque l'organisation a des obligations contractuelles fédérales américaines explicites**.

**Note sur les infrastructures cloud :** Si l'organisation utilise des fournisseurs de services cloud basés aux États-Unis (AWS, Azure, GCP), cela ne déclenche PAS automatiquement des obligations de conformité fédérale américaine. FedRAMP/FISMA ne s'appliquent que si :

- L'organisation fournit des services directement à des agences fédérales américaines (en tant que contractant principal ou sous-traitant), OU
- Le contrat client de l'organisation exige explicitement une autorisation FedRAMP ou une conformité FISMA

L'utilisation de fournisseurs cloud autorisés FedRAMP (p. ex. AWS GovCloud) est une **décision de gestion des risques fournisseurs** (A.5.19-23), non une preuve que FedRAMP s'applique à l'organisation.

**Statut par défaut** : **Non applicable**, sauf si :

- L'organisation détient des contrats fédéraux américains
- L'organisation fournit des services à des agences fédérales américaines
- Le contrat exige explicitement des contrôles NIST ou une autorisation FedRAMP

**Justification** : Les exigences fédérales américaines ne sont pas extraterritoriales et ne s'appliquent pas aux organisations non américaines, sauf obligation contractuelle.

**Traitement dans le SMSI** :

- Les référentiels NIST peuvent être utilisés comme **référence informative** (Niveau 3)
- FISMA/FedRAMP deviennent **obligatoires** (Niveau 1) uniquement avec des contrats fédéraux
- La série NIST SP 800 est utilisée à titre d'orientation technique sans obligation de conformité

**Considération relative à la FedRAMP Marketplace :**

Si l'organisation cherche à référencer ses services sur la FedRAMP Marketplace (fedramp.gov) pour commercialiser ses services auprès des agences fédérales américaines, l'autorisation FedRAMP devient **obligatoire** (Niveau 1). Cette décision entraîne :

- Transition Niveau 2 → Niveau 1 pour FISMA/FedRAMP
- Réévaluation obligatoire selon la Section 5 (Quand réévaluer)
- Mise à jour de la matrice d'applicabilité réglementaire en Section 8.1
- Obligation de recourir à un 3PAO (organisation d'évaluation tierce accréditée)
- Recherche d'une autorisation JAB (Joint Authorization Board) ou ATO (Authority to Operate) d'agence

---

# Détermination de l'applicabilité réglementaire

## Processus d'évaluation

Les organisations DOIVENT conduire des évaluations annuelles d'applicabilité réglementaire :

**Étape 1 : Identification des activités métier**

- Localisations géographiques des opérations
- Secteurs d'activité et industries desservis
- Types de données traitées (PII, santé, financières, etc.)
- Base clientèle (B2B, B2C, gouvernement)
- Services fournis (cloud, conseil, logiciels, etc.)

**Étape 2 : Correspondance réglementations-activités**

| Activité métier | Réglementations déclenchées |
|-----------------|-----------------------------|
| Traitement de données de résidents UE | RGPD (obligatoire) |
| Opérations en Suisse | nLPD suisse (obligatoire) |
| Objectif de certification ISO 27001 | ISO 27001 (obligatoire) |
| Traitement des cartes de paiement | PCI DSS v4.0.1 (conditionnel — si oui, obligatoire) |
| Services financiers UE | DORA (conditionnel — si oui, obligatoire) |
| Développement/déploiement de systèmes d'IA affectant l'UE | AI Act UE (conditionnel — si oui, obligatoire) |
| Contrats fédéraux américains | FISMA/FedRAMP (conditionnel — si oui, obligatoire) |

**Étape 3 : Documentation de la détermination d'applicabilité**

- Créer une matrice d'applicabilité réglementaire
- Documenter la justification de la détermination d'applicabilité
- Attribuer la propriété (Juridique, Conformité, RSSI, DPD)
- Mettre à jour annuellement ou lors de changements métier

**Note** : Ce processus d'évaluation identifie **quelles réglementations s'appliquent**, non comment la conformité est mise en œuvre ou vérifiée. La mise en œuvre et la vérification sont traitées par des processus distincts du SMSI (évaluation des risques, mise en œuvre des contrôles, surveillance de la conformité).

## Modèle de matrice d'applicabilité réglementaire

Les organisations devraient tenir une matrice d'applicabilité réglementaire :

| Réglementation | Niveau | Statut | Déclencheurs | Responsable | Dernière révision | Révisé par | Approuvé par |
|----------------|--------|--------|--------------|-------------|-------------------|------------|--------------|
| nLPD suisse | 1 - Obligatoire | Applicable | Opérations suisses | DPD | [Date] | [Nom DPD] | [Direction] |
| RGPD UE | 1 - Obligatoire | Applicable | Données clients UE | DPD | [Date] | [Nom DPD] | [Direction] |
| ISO 27001 | 1 - Obligatoire | Applicable | Objectif de certification | RSSI | [Date] | [Nom RSSI] | [Direction] |
| DORA | 2 - Conditionnel | Non applicable | Pas d'entité financière | N/A | [Date] | [RSSI/Juridique] | [RSSI] |
| PCI DSS v4.0.1 | 2 - Conditionnel | Applicable | Traitement cartes | RSSI | [Date] | [Nom RSSI] | [Direction] |
| AI Act UE | 2 - Conditionnel | [À évaluer] | Développement/déploiement de systèmes d'IA affectant l'UE | RSSI | [Date] | [RSSI/Juridique] | [À déterminer] |
| NIST SP 800-53 | 3 - Informatif | Référence uniquement | Orientation technique | RSSI | [Date] | [Nom RSSI] | [RSSI] |

## Quand réévaluer

**Événements déclencheurs d'une réévaluation** :

- Nouvelle ligne d'activité ou offre de service
- Expansion vers de nouveaux marchés géographiques
- Acquisition ou fusion
- Nouveaux contrats clients avec exigences réglementaires
- Modifications réglementaires (nouvelles lois, normes mises à jour)
- Changements de périmètre de certification (extension ISO 27001)

**Fréquence** : Minimum annuel + réévaluations déclenchées

**Responsabilité** : RSSI + Juridique/Conformité + DPD (surveillance trimestrielle), approbation de la Direction générale (revue annuelle complète)

## Approche de surveillance des réglementations conditionnelles

Les organisations devraient mettre en place une surveillance systématique des réglementations conditionnelles de Niveau 2 pour détecter les déclencheurs d'applicabilité :

| Réglementation | Méthode de surveillance | Fréquence | Responsable |
|----------------|------------------------|-----------|-------------|
| **DORA** | Revue des contrats clients pour les clauses de conformité DORA ; surveillance si les clients deviennent des entités financières réglementées DORA | Trimestriel (lors des revues de contrats clients) | RSSI + Juridique |
| **NIS2** | Surveillance des plans de développement commercial pour l'expansion dans les secteurs couverts (énergie, transports, infrastructures numériques) ; suivi des lois NIS2 nationales des États membres UE | Trimestriel (revues de stratégie métier) + Ad hoc (publications de lois nationales) | RSSI + Juridique |
| **FINMA** | Surveillance du développement commercial pour les demandes de licence de services financiers ; suivi si les services fournis à des entités réglementées FINMA (règles d'externalisation susceptibles de se déclencher) | Trimestriel (revues de stratégie métier) | Juridique + RSSI |
| **PCI DSS** | Surveillance des décisions de traitement des paiements ; suivi des demandes de compte marchand ou d'intégrations de passerelles de paiement | Trimestriel (coordination finance/développement commercial) | RSSI |
| **AI Act UE** | Surveillance des décisions de développement/déploiement de systèmes d'IA ; suivi des achats d'outils IA ; évaluation si les sorties IA affectent des personnes dans l'UE | Trimestriel (revues de stratégie technologique) + Déclenché (adoption d'un nouvel outil IA) | RSSI |
| **HIPAA** | Surveillance des types de données clients ; suivi si le traitement de données de santé américaines commence | Trimestriel (revues d'inventaire des traitements de données) | DPD + RSSI |

**Escalade :** Si la surveillance détecte un déclencheur d'applicabilité probable → Initier une évaluation détaillée selon la Section 5 dans les 30 jours → Mettre à jour la matrice Section 8 → Informer la Direction générale si transition Niveau 2 → Niveau 1.

**Surveillance du calendrier de mise en œuvre réglementaire :** La surveillance trimestrielle doit référencer l'Annexe A (Calendriers de mise en œuvre réglementaire) pour anticiper les prochaines échéances de conformité pour les réglementations conditionnelles à mise en œuvre progressive (DORA, AI Act UE, PCI DSS v4.0.1, lois NIS2 nationales).

**Traitement des faux positifs :**

Si la surveillance détecte un déclencheur d'applicabilité potentiel mais qu'une évaluation détaillée (selon la Section 5) détermine que la réglementation n'est **pas applicable** :

- Documenter l'évaluation dans le **Registre des évaluations déclenchées**
- Consigner : déclencheur détecté, évaluation effectuée, conclusion (non applicable), justification
- Conserver pour la piste d'audit (démontre que la surveillance fonctionne — tout déclencheur n'implique pas une applicabilité)
- Exemple : « Le contrat client mentionnait DORA. Évaluation : le client n'est pas une entité réglementée DORA, la clause contractuelle est une exigence générale de sécurité, non spécifique à DORA. DORA reste Non applicable. »

---

# Utilisation dans les politiques du SMSI

## Formulation de référence standard

Toutes les politiques du SMSI DOIVENT inclure l'une des formulations suivantes :

**Option A : Référence Section 1.3** (recommandée pour la plupart des politiques) :

```markdown
## Applicabilité des cadres réglementaires

Les références aux normes, référentiels et réglementations dans ce SMSI sont
catégorisées conformément à ISMS-POL-00 (Cadre d'applicabilité réglementaire) :

**Conformité obligatoire :**

- Loi fédérale suisse sur la protection des données (nLPD)
- RGPD UE (lors du traitement de données personnelles de résidents UE)
- ISO/IEC 27001:2022
- [Réglementations obligatoires supplémentaires selon ISMS-POL-00]

**Référence informative / Alignement sur les bonnes pratiques :**

- Publications spéciales NIST (série SP 800)
- [Autres référentiels selon ISMS-POL-00]

**Exigences fédérales américaines :**
Les référentiels fédéraux américains (FISMA, FedRAMP, NIST) s'appliquent
uniquement lorsque des obligations contractuelles fédérales américaines
explicites existent (voir ISMS-POL-00, section Exigences fédérales américaines).

Pour une catégorisation réglementaire complète, consulter ISMS-POL-00.
```

**Option B : Section dédiée au cadre réglementaire** (pour les réglementations spécifiques à un contrôle) :

```markdown
# Cadre réglementaire

Ce contrôle met en œuvre les exigences des réglementations catégorisées
conformément à ISMS-POL-00 (Cadre d'applicabilité réglementaire).

## Conformité obligatoire
[Exigences obligatoires spécifiques au contrôle]

## Applicabilité conditionnelle
[Exigences conditionnelles spécifiques au contrôle]

## Référence informative
[Bonnes pratiques spécifiques au contrôle]

Pour une catégorisation réglementaire complète, consulter ISMS-POL-00.
```

## Références d'audit

**Pour les audits internes** :

- Vérifier que toutes les politiques du SMSI référencent ISMS-POL-00
- Confirmer que la matrice d'applicabilité réglementaire est à jour (révisée annuellement)
- Valider que les déterminations d'applicabilité ont une justification documentée

**Pour les audits externes** :

- Fournir ISMS-POL-00 en tant que document fondamental
- Référencer la matrice d'applicabilité réglementaire
- Démontrer le processus de réévaluation annuelle et la propriété

## Preuves pour cette politique

**Preuves pour la Phase 1 (revue documentaire) :**
Preuves requises pour démontrer que cette politique est adéquatement documentée et approuvée :

- ✅ Ce document de politique (ISMS-POL-00 v1.0)
- ✅ Signatures d'approbation du RSSI, du responsable juridique/conformité, du DPD et de la Direction générale
- ✅ Structure du cadre d'applicabilité réglementaire (taxonomie Niveau 1/2/3 définie)
- ✅ Méthodologie d'évaluation documentée (Section 5)
- ✅ Formulation de référence standard pour les politiques SMSI (Section 6)

**Preuves pour la Phase 2 (efficacité opérationnelle) :**
Preuves requises pour démontrer que cette politique est opérationnellement efficace :

- Matrice d'applicabilité réglementaire renseignée avec le statut organisationnel actuel (Section 8)
- Enregistrements de revue : journaux de surveillance trimestriels, comptes rendus de réunions de revue annuelle complète
- Documents de détermination d'applicabilité : justification des assignations de niveaux (en particulier les décisions de Niveau 2)
- Enregistrements des évaluations déclenchées : évaluations d'impact de l'expansion métier et des modifications réglementaires
- Versions historiques : versions précédentes de POL-00 montrant l'évolution du cadre

**Statut actuel des preuves opérationnelles** : Les journaux de surveillance trimestriels, les enregistrements des évaluations déclenchées et les preuves de la revue la plus récente sont tenus conformément au format défini dans la section Méthodologie d'évaluation (voir Statut réglementaire actuel → Exécution de la méthodologie d'évaluation).

**Clarification sur les preuves de conformité :**
Cette politique établit l'applicabilité réglementaire (QUELLES réglementations s'appliquent). Elle N'ÉTABLIT PAS :

- **Les preuves de mise en œuvre des contrôles** (traitées dans la documentation des contrôles Annexe A)
- **Les KPIs/tableaux de bord de conformité** (traités dans ISMS-POL-A.5.31-S4 §6)
- **Les conclusions d'audit réglementaire** (traitées dans les processus de surveillance de la conformité)

La délimitation est : POL-00 identifie les obligations → L'évaluation des risques priorise → Les contrôles mettent en œuvre → Des processus distincts vérifient la conformité.

---

# Maintenance et mises à jour

## Calendrier de révision

**Révision trimestrielle** (RSSI + Juridique + DPD) :

- Surveiller les évolutions réglementaires (mises à jour des orientations RGPD, nouvelles directives)
- Suivre les changements organisationnels (nouveaux services, nouveaux marchés)
- Mettre à jour la matrice d'applicabilité si les déclencheurs changent
- Documenter la revue dans la réunion de revue SMSI trimestrielle

**Révision annuelle** (approbation de la Direction générale) :

- Évaluation complète du paysage réglementaire
- Mise à jour d'ISMS-POL-00 pour les nouvelles réglementations
- Révision de la formulation de référence des politiques si nécessaire
- Validation de la Direction générale sur les obligations de conformité
- Mise à jour du contrôle des versions et de la distribution

**Révision déclenchée** :

- Publication d'une nouvelle réglementation (entrée en vigueur de DORA, publication de l'AI Act)
- Expansion métier (nouveau pays, nouveau service)
- Fusion/acquisition
- Contrat majeur avec de nouvelles exigences réglementaires

**Responsabilités** :

- **Surveillance réglementaire** : Responsable juridique/conformité (principal), RSSI (soutien)
- **Évaluation d'applicabilité** : RSSI + Juridique/Conformité + DPD (responsabilité conjointe)
- **Mises à jour de la matrice** : RSSI (propriétaire), DPD (réglementations de protection des données)
- **Mises à jour de la politique** : RSSI (auteur), Direction générale (approbation)

## Sources de surveillance réglementaire

**Principales sources de surveillance :**

- **nLPD/FADP** : Site web du Préposé fédéral à la protection des données et à la transparence (PFPDT), publications d'orientations
- **RGPD** : Directives du Comité européen de la protection des données (CEPD), orientations des ATD nationales, Journal officiel de l'UE
- **Normes ISO** : Publications ISO, mises à jour BSI (British Standards Institution), notifications des organismes de certification
- **DORA/NIS2** : Journal officiel de l'UE, publications ENISA, autorités nationales compétentes
- **PCI DSS** : PCI Security Standards Council (pcisecuritystandards.org), mises à jour pour les organisations participantes
- **FINMA** : Circulaires et publications d'orientations FINMA (finma.ch)
- **AI Act UE** : Journal officiel de l'UE, publications du Bureau de l'IA, autorités nationales compétentes en matière d'IA
- **Surveillance juridique** : Service d'abonnement de conseil juridique externe, surveillance par le département juridique interne

**Fréquence de surveillance :** Analyse hebdomadaire des sources réglementaires, revue complète trimestrielle

## Communication

**Mises à jour de politique communiquées via** :

- Mise à jour du portail de politiques
- Email à tous les propriétaires de politiques
- Briefing juridique/conformité
- Briefing du RSSI à la Direction générale
- Mises à jour des supports de formation (si modifications significatives)

**Parties prenantes notifiées** :

- Tous les auteurs de politiques SMSI (impact immédiat)
- Propriétaires de systèmes (impact sur la délimitation des contrôles)
- Audit interne (planification des audits)
- Auditeurs externes (périmètre de certification)

## Contrôle des versions

**Version majeure (X.0)** :

- Nouvelles réglementations obligatoires ajoutées (modifications de Niveau 1)
- Changements de niveau (informatif → obligatoire)
- Modifications structurelles du cadre
- Suppression de réglementations (plus applicables)

**Version mineure (X.Y)** :

- Clarifications des réglementations existantes
- Référentiels informatifs supplémentaires (Niveau 3)
- Mises à jour de référence (versions des publications NIST, orientations RGPD)
- Améliorations non structurelles

---

# Documents connexes

**Références internes** :

- Toutes les politiques du SMSI (série ISMS-POL-A.X.XX)
- Méthodologie d'évaluation des risques du SMSI (Clause 6)
- Déclaration d'applicabilité du SMSI (délimitation Annexe A)
- Processus de surveillance de la conformité du SMSI

**Références externes** :

- Loi fédérale suisse sur la protection des données (RS 235.1)
- RGPD UE (Règlement 2016/679)
- ISO/IEC 27001:2022
- Publications spéciales NIST (nist.gov)
- PCI DSS v4.0.1 (pcisecuritystandards.org)
- DORA (Règlement 2022/2554)
- NIS2 (Directive 2022/2555)

---

# Statut réglementaire actuel

**Statut de l'évaluation d'applicabilité (au [Date]) :**

Cette section documente les obligations actuelles de conformité réglementaire de l'organisation telles que déterminées par la méthodologie d'évaluation définie à la Section 5.

## Niveau 1 : Conformité obligatoire (Active)

| Réglementation | Justification d'applicabilité | Statut de mise en œuvre | Prochaine révision |
|----------------|------------------------------|------------------------|-------------------|
| **nLPD suisse (nDSG)** | ✅ Applicable — Organisation basée en Suisse avec des opérations et employés suisses | Contrôles mis en œuvre conformément à l'Annexe A (A.5.12-14 Protection des données, A.5.34 Protection de la vie privée) | [Date + 12 mois] |
| **RGPD UE** | ✅ Applicable — Traitement de données personnelles de résidents UE via les relations clients | Contrôles mis en œuvre conformément à l'Annexe A (A.5.34, A.8.11 Masquage des données, A.8.10 Suppression des informations) | [Date + 12 mois] |
| **ISO/IEC 27001:2022** | ✅ Applicable — Recherche de certification (objectif documenté dans le périmètre du SMSI) | 48/93 contrôles mis en œuvre (52 %), préparation Phase 1 atteinte, préparation Phase 2 en cours | Continue (maintien de la certification) |

## Niveau 2 : Applicabilité conditionnelle

### Actuellement non applicable (sous surveillance)

| Réglementation | Statut d'évaluation | Décision actuelle | Déclencheur de surveillance | Responsable | Dernière évaluation |
|----------------|--------------------|--------------------|------------------------------|-------------|---------------------|
| **DORA** | ✅ Évalué | **Non applicable** — L'organisation n'est pas une entité financière UE ni un fournisseur TIC critique désigné pour des entités financières | Changement de modèle d'activité (entrée dans les services financiers), contrats clients exigeant la conformité DORA | RSSI + Juridique | [Date] |
| **NIS2** | ✅ Évalué | **Non applicable** — L'organisation n'opère pas en tant qu'entité essentielle/importante dans les secteurs couverts (énergie, transports, secteur bancaire, santé, infrastructures numériques) | Expansion dans les secteurs couverts NIS2, désignation en tant qu'entité essentielle/importante | RSSI + Juridique | [Date] |
| **PCI DSS v4.0.1** | ✅ Évalué | **Non applicable** — L'organisation ne stocke, traite ni transmet actuellement des données de titulaires de carte | Décision d'accepter des cartes de paiement, ouverture d'un compte marchand | RSSI | [Date] |
| **FINMA** | ✅ Évalué | **Non applicable** — L'organisation ne détient pas de licence FINMA (pas une banque suisse, négociant en valeurs mobilières, compagnie d'assurance ou fournisseur d'infrastructure financière réglementé) | Acquisition d'une licence de services financiers, prestation de services à des entités réglementées FINMA | Juridique + RSSI | [Date] |

### En cours d'évaluation (décision en attente)

| Réglementation | Statut d'évaluation | Achèvement prévu | Constatations préliminaires | Responsable |
|----------------|--------------------|--------------------|------------------------------|-------------|
| **AI Act UE** | 🔄 En cours | À déterminer — en attente de publication des actes délégués de l'AI Act UE (cible T2 2026 ; voir étapes d'évaluation ci-dessous) | L'organisation utilise des outils d'IA (GitHub Copilot pour l'assistance au développement, futurs outils de sécurité assistés par IA possibles). Focus de l'évaluation : ces systèmes sont-ils des « systèmes d'IA » au sens de l'Article 3 ? Si oui, classification des risques selon l'Annexe III. **Interaction avec l'Article 22 RGPD :** Si les systèmes d'IA impliquent une prise de décision automatisée ayant des effets juridiques/significatifs sur des individus (Art. 22 RGPD), des exigences supplémentaires s'appliquent (droit à une revue humaine, transparence, AIPD). Préliminaire : Probable **risque minimal** (Niveau 3) ou **risque limité** (obligations de transparence uniquement). **Recommandation :** Finaliser l'évaluation détaillée d'ici [Date], documenter dans ISMS-REF-AI-ACT si des obligations sont identifiées. | RSSI + Juridique |

**Livrables d'évaluation à ce jour :**
- [Date] : Inventaire des systèmes d'IA complété (documenté dans ISMS-REF-AI-ACT-INVENTORY)
  - GitHub Copilot (génération de code, évalué comme risque minimal)
  - [Autres outils si applicable]
- [Date] : Analyse du chevauchement Article 22 RGPD complétée (aucune prise de décision automatisée ayant des effets juridiques/significatifs identifiée)
- **Prochain livrable :** Rapport de classification des risques dû le [Date + 2 semaines]

**Démarche d'évaluation pour l'AI Act UE :**
1. **Inventaire des usages IA** (Échéance : [Date + 2 semaines])

   - GitHub Copilot (assistant de génération de code)
   - [Lister les autres outils IA si applicable]

2. **Évaluation du chevauchement Article 22 RGPD** (Échéance : [Date + 2 semaines])
   - Pour chaque système d'IA, évaluer : prend-il des décisions automatisées ayant des effets juridiques ou significativement similaires sur des individus ?
   - Exemples déclenchant l'Art. 22 RGPD :
     - Présélection automatisée de CV (impact sur l'emploi)
     - Décisions automatisées de contrôle d'accès (impact sur le refus de service)
     - Classification automatisée d'incidents de sécurité (affecte les droits à la protection des données des individus)
   - Si oui → Exigences Art. 22 RGPD applicables (droit à une revue humaine, transparence, AIPD)
   - Documenter le chevauchement dans l'évaluation ISMS-REF-AI-ACT

3. **Classification des risques selon l'Annexe III de l'AI Act** (Échéance : [Date + 4 semaines])

   - Évaluer selon les catégories à haut risque (emploi, scoring de crédit, biométrie, infrastructures critiques, application des lois)
   - Détermination préliminaire : aucun des usages actuels de l'IA ne relève des catégories à haut risque

4. **Documentation de la décision** (Échéance : [Date + 6 semaines])

   - Si risque minimal/limité → Niveau 3 (Informatif) avec obligations de transparence
   - Si haut risque → Niveau 2 (Conditionnel → Obligatoire si confirmé)
   - Créer ISMS-REF-AI-ACT si des obligations sont identifiées

## Niveau 3 : Référence informative (Utilisation active)

| Référentiel | Utilisation | Référencé dans | Justification |
|-------------|-------------|----------------|---------------|
| **NIST SP 800** | Orientations de mise en œuvre technique | Plusieurs contrôles Annexe A (A.8.8 Gestion des vulnérabilités réf. NIST SP 800-40, A.5.24-28 Réponse aux incidents réf. NIST SP 800-61) | Orientations techniques standard du secteur pour la mise en œuvre des contrôles |
| **CIS Controls v8.1** | Étalonnage de la sécurité | Évaluation interne de la posture de sécurité, analyse des écarts de contrôles | Référentiel de sécurité largement reconnu pour la comparaison |
| **OWASP** | Pratiques de développement sécurisé | A.8.25-28 Cycle de vie du développement sécurisé | Bonnes pratiques de sécurité des applications web |
| **ISO/IEC 27002:2022** | Orientations de mise en œuvre des contrôles | Tous les contrôles Annexe A | Orientations officielles de mise en œuvre des contrôles ISO 27001 |

## Exécution de la méthodologie d'évaluation

**Revue annuelle complète :**

- **Planifiée :** T4 annuellement (décembre)
- **Participants :** RSSI (responsable), Conseiller juridique, DPD, Responsable conformité
- **Livrable :** Section 8 mise à jour + Briefing de la Direction générale
- **Approbation :** Direction générale

**Revue de surveillance trimestrielle :**

- **Planifiée :** Fin de chaque trimestre (mars, juin, septembre, décembre)
- **Participants :** RSSI, Juridique, DPD
- **Focus :** Modifications réglementaires détectées, événements déclencheurs métier, mises à jour du statut des réglementations conditionnelles
- **Livrable :** Journal de surveillance réglementaire, évaluations des événements déclencheurs

**Contenu du journal de surveillance réglementaire :**
- Date de la revue
- Modifications réglementaires détectées (nouvelles lois, mises à jour d'orientations, mesures d'exécution)
- Événements déclencheurs organisationnels (nouveaux services, expansion de marché, contrats clients)
- Évaluation de l'impact d'applicabilité (la modification affecte-t-elle le statut Niveau 1/2/3 ?)
- Action requise (mettre à jour POL-00, déclencher une évaluation détaillée, aucune action)
- Signatures des réviseurs (RSSI, Juridique, DPD)

**Format et emplacement du journal :**
- Format : Tableur structuré ou enregistrements sur plateforme GRC
- Emplacement : Registre Excel sur [SharePoint]/SMSI/Conformité/POL-00-Surveillance.xlsx (solution provisoire ; à migrer vers la plateforme GRC d'ici [date])
- Conservation : Minimum 3 ans (couvre le cycle de certification complet)
- Accès : RSSI, Juridique, DPD, Audit interne, Auditeurs externes

**Champs minimaux :**

| Champ | Description | Exemple |
|-------|-------------|---------|
| Date de revue | Date de surveillance trimestrielle | 2024-12-31 |
| Participants | Noms et signatures | [RSSI], [Juridique], [DPD] |
| Modifications réglementaires | Nouvelles lois/orientations détectées | Actes délégués AI Act UE publiés |
| Événements déclencheurs | Changements métier examinés | Aucun / Nouveau contrat client exigeant la conformité FINMA |
| Impact d'applicabilité | Changements de niveau | Aucun / FINMA Niveau 2 → Niveau 1 en raison du contrat client |
| Actions requises | Tâches de suivi | Aucune / Initier l'évaluation de conformité FINMA |
| Prochaine date de revue | Cadence trimestrielle | 2025-03-31 |

**Preuves d'exécution de la surveillance réglementaire :**
Journaux de surveillance trimestriels tenus dans [Plateforme GRC / Registre de conformité] avec :
- Date de revue et participants (signatures RSSI, Juridique, DPD)
- Modifications réglementaires détectées (aucune/liste avec évaluation d'impact)
- Événements déclencheurs examinés (expansions métier, contrats clients)
- Décisions de réévaluation d'applicabilité (changements de niveau documentés)
- Enregistrements d'escalade (si transition Niveau 2 → Niveau 1 détectée)

**Preuves les plus récentes :**
- Journal de surveillance T4 2024 : [Date], révisé par [RSSI/Juridique/DPD], aucun changement de niveau
- Revue annuelle 2024 : [Date], approuvée par la Direction générale, ISMS-POL-00 v1.0 publiée
- Évaluation AI Act UE : [Date] Étape 1 complétée (inventaire IA documenté dans [emplacement])

**Registre des évaluations déclenchées :**
Tenu dans [emplacement] avec :
- Description de l'événement déclencheur (contrat client, modification réglementaire, expansion métier)
- Date de l'évaluation et évaluateur
- Détermination d'applicabilité (Applicable / Non applicable / Nécessite une évaluation approfondie)
- Justification (motivation documentée pour la détermination)
- Mesures prises (changement de niveau, mise en œuvre de contrôles, aucune action requise)
- Autorité d'approbation (RSSI, Juridique, Direction générale si changement de niveau)

**Tenu dans :** [Système de conformité — p. ex. plateforme GRC, référentiel documentaire]

**Évaluations déclenchées :**

- Expansion métier (nouveaux marchés, nouveaux services)
- Exigences des contrats clients (obligations réglementaires explicites)
- Publications réglementaires (nouvelles lois, orientations d'application)
- **Exemple récent :** L'AI Act UE est entré en vigueur le 1er août 2024 → Évaluation déclenchée (actuellement en cours selon la Section 8.2.2)

**Prochaines activités planifiées :**

- **[Date + 2 semaines] :** Compléter l'évaluation AI Act UE (Étape 1 : inventaire des usages IA)
- **T4 [Année] :** Revue réglementaire annuelle complète
- **[Date + 12 mois] :** Reconfirmation de l'applicabilité nLPD/RGPD

## Références détaillées des exigences

Pour les réglementations conditionnelles avec des exigences complexes (quel que soit le statut d'applicabilité actuel), l'organisation tient des documents de référence détaillés pour les scénarios d'applicabilité future et la préparation.

| Réglementation | Document de référence | Objet | Statut de maintenance | Dernière mise à jour | Prochaine révision |
|----------------|----------------------|-------|-----------------------|---------------------|-------------------|
| **DORA** | ISMS-REF-DORA — Référence des exigences du Digital Operational Resilience Act | Exigences détaillées de gestion des risques TIC, déclaration d'incidents, tests de résilience et risques tiers selon les Articles DORA 3-49. Tenu pour l'évaluation d'applicabilité future si l'organisation entre dans les services financiers UE. | Tenu (mis à jour lors de la publication des normes techniques réglementaires DORA) | [Date de revue des RTS DORA] | Annuellement ou lors des mises à jour des RTS DORA |
| **FINMA** | ISMS-REF-FINMA — Référence des exigences de la Circulaire FINMA 2023/1 | Exigences de résilience opérationnelle et d'externalisation pour les établissements financiers suisses. Tenu pour l'applicabilité future si l'organisation obtient une licence FINMA ou sert des clients réglementés FINMA. | Tenu (mis à jour selon les révisions des circulaires FINMA) | [Date de revue de la Circulaire 2023/1] | Annuellement ou lors des révisions des circulaires FINMA |
| **NIS2** | ISMS-REF-NIS2 — Référence des exigences de la Directive NIS2 | Gestion des risques de cybersécurité, notification des incidents, sécurité de la chaîne d'approvisionnement et exigences de gouvernance selon les Articles NIS2 20-23. Tenu pour l'applicabilité future si l'organisation est désignée entité essentielle/importante. | Tenu (mis à jour à mesure que les États membres UE transposent NIS2 en droit national) | [Date de revue des lois nationales NIS2] | Semestriel (surveillance des transpositions nationales) |
| **PCI DSS v4.0.1** | ISMS-REF-PCI-DSS — Référence des exigences PCI DSS | 12 exigences PCI DSS v4.0.1 couvrant la sécurité réseau, la protection des données, la gestion des vulnérabilités, le contrôle d'accès, la surveillance et les tests. Tenu pour l'applicabilité future si l'organisation commence à traiter des cartes de paiement. | Tenu (mis à jour selon les publications PCI SSC, actuellement v4.0 en vigueur depuis mars 2024) | [Date d'incorporation de la v4.0.1] | Annuellement ou lors des mises à jour PCI SSC |
| **AI Act UE** | ISMS-REF-EU-AI-ACT — Référence des exigences du règlement UE sur l'IA | Cadre de gouvernance de l'IA basé sur les risques couvrant les pratiques interdites (Article 5), les systèmes d'IA à haut risque (Articles 9-72), les obligations de transparence pour le risque limité (Article 50) et les exigences pour les modèles d'IA à usage général (Articles 53-54). Tenu pour l'applicabilité future si l'organisation développe ou déploie des systèmes d'IA affectant des personnes dans l'UE. | En développement (mis à jour à mesure que les actes délégués et d'exécution de l'AI Act UE sont publiés, mise en œuvre progressive 2025-2028) | [Date du brouillon initial] | Lors de la publication des actes délégués de l'AI Act |

**Justification du maintien des références d'exigences « Non applicable » :**

1. **Préparation :** Si le contexte métier évolue (p. ex. obtention d'une licence de services financiers, entrée dans les secteurs couverts NIS2, acceptation des cartes de paiement), l'organisation peut rapidement évaluer l'écart et l'effort de mise en œuvre.

2. **Diligence raisonnable client :** Les clients peuvent demander des preuves de préparation aux réglementations conditionnelles même si elles ne sont pas encore applicables (p. ex. « Si nous exigeons la conformité PCI DSS v4.0.1 à l'avenir, pouvez-vous l'atteindre ? »).

3. **Surveillance réglementaire :** Le maintien des références d'exigences permet une surveillance proactive des modifications réglementaires susceptibles d'affecter l'applicabilité future (p. ex. normes techniques DORA, mises en œuvre nationales NIS2, mises à jour PCI DSS v4.0.1).

4. **Efficacité de la cartographie des contrôles :** Les références d'exigences facilitent la correspondance des réglementations conditionnelles avec les contrôles existants de l'Annexe A ISO 27001, montrant les chevauchements et la réutilisation potentielle (p. ex. « Si DORA s'applique, nous estimons que 70 % des exigences sont déjà satisfaites par les contrôles existants »).

5. **Planification stratégique :** La Direction générale peut prendre des décisions éclairées concernant l'entrée sur des marchés réglementés en comprenant l'effort de mise en conformité requis.

**Accès et utilisation :**

- **Les documents ISMS-REF-XXX ne sont PAS des documents de conformité obligatoire** (les réglementations sont de Niveau 2 — Non applicable).
- **Objet :** Préparation stratégique, demandes clients, diligence raisonnable en développement commercial.
- **Cycle de révision :** Révision annuelle alignée avec la révision POL-00 (vérifier que la réglementation n'a pas évolué au point de rendre l'évaluation obsolète).
- **Propriété :** RSSI (maintien des exigences techniques), Juridique (maintien de l'interprétation juridique et des déclencheurs d'applicabilité).

**Note pour les auditeurs :**
Le maintien des références d'exigences pour des réglementations non applicables est un **indicateur de maturité** démontrant une gestion proactive de la conformité, non une preuve d'extension du périmètre. La Clause 4.1 d'ISO 27001 (Compréhension de l'organisation et de son contexte) encourage la compréhension des obligations de conformité actuelles et futures potentielles.

---

# Glossaire

| Terme | Définition |
|-------|------------|
| **Applicable** | La réglementation s'applique à l'organisation en raison de ses activités, elle doit s'y conformer |
| **Conditionnel** | La réglementation ne s'applique que si des déclencheurs spécifiques sont remplis (secteur, géographie, type de données) |
| **Obligatoire** | Obligation légale, applicable en vertu de la loi ou du contrat, le non-respect a des conséquences |
| **Informatif** | Référence pour les bonnes pratiques, non légalement contraignant, adoption volontaire |
| **Niveau 1** | Conformité obligatoire (légale, contractuelle) |
| **Niveau 2** | Conformité conditionnelle (selon le contexte) |
| **Niveau 3** | Référence informative (bonnes pratiques, volontaire) |
| **Force contraignante** | Applicabilité légale ou contractuelle d'une réglementation |
| **Obligation de mise en œuvre** | Exigence de mise en œuvre de contrôles spécifiques (déterminée par l'évaluation des risques) |
| **Surveillance réglementaire** | Revue trimestrielle systématique des évolutions réglementaires et des événements déclencheurs organisationnels pour détecter les changements d'applicabilité des réglementations conditionnelles de Niveau 2 |
| **Déclencheur d'applicabilité** | Événement ou condition qui fait passer une réglementation conditionnelle (Niveau 2) à obligatoire (Niveau 1), nécessitant une évaluation de transition et la mise en œuvre de la conformité |
| **Évaluation déclenchée** | Évaluation d'applicabilité réglementaire non planifiée initiée par la détection d'un déclencheur d'applicabilité (p. ex. expansion métier, contrat client, modification réglementaire) |

---

# Annexe A : Calendriers de mise en œuvre réglementaire

**Réglementations avec mise en œuvre progressive (pour la surveillance) :**

| Réglementation | Dates de mise en œuvre clés | Pertinence organisationnelle |
|----------------|-----------------------------|-----------------------------|
| **DORA** | **17 janvier 2025 :** Application complète pour les entités financières | Surveiller : Si l'organisation devient une entité financière UE ou un fournisseur TIC critique avant le 2025-01-17, DORA devient immédiatement Niveau 1 |
| **AI Act UE** | **2 février 2025 :** Interdictions (IA à risque inacceptable)<br>**2 août 2025 :** Obligations pour les modèles d'IA à usage général<br>**2 décembre 2027 :** Systèmes d'IA à haut risque (reporté du 2 août 2026 par le Digital Omnibus, Règlement (UE) 2026/1744, en vigueur depuis le 27 juillet 2026)<br>**2 août 2028 :** IA à haut risque dans les produits réglementés (reporté du 2 août 2027 par le même Digital Omnibus)<br>**2 août 2030 :** Fin de la période de grâce pour les systèmes existants utilisés par des autorités publiques (inchangée) | Surveiller : Si l'organisation développe ou déploie des systèmes d'IA affectant des personnes dans l'UE → Conformité requise avant l'échéance applicable. Les systèmes existants bénéficient d'une période de grâce jusqu'à la date applicable ci-dessus (décembre 2027 / août 2028) ; les systèmes utilisés par des autorités publiques conservent une période de grâce jusqu'en 2030, sauf modification substantielle |
| **PCI DSS v4.0.1** | **31 mars 2024 :** v4.0 en vigueur (v3.2.1 retirée)<br>**31 mars 2025 :** Les nouvelles exigences (marquées « futures » dans la v4.0) deviennent obligatoires | Actuellement non applicable. Si le traitement des cartes de paiement commence → Les exigences v4.0 s'appliquent immédiatement (v3.2.1 retirée). Les exigences à date future (extension MFA, améliorations cryptographiques, anti-hameçonnage) obligatoires à partir de mars 2025 |
| **NIS2** | **17 octobre 2024 :** Les États membres UE doivent transposer en droit national<br>**2024-2025 :** Les mises en œuvre nationales varient selon l'État membre<br>**Variable selon l'État membre :** Les dates d'application dépendent de la loi nationale de transposition | Surveiller : Les mises en œuvre nationales peuvent affecter la détermination d'applicabilité si l'organisation opère dans plusieurs États membres UE. Consulter l'autorité nationale de cybersécurité pour les dates d'entrée en vigueur spécifiques |

---

# Déclaration de clôture

Cette politique établit l'applicabilité réglementaire pour le Système de Management de la Sécurité de l'Information de l'organisation.

**Ce que cette politique établit :**

- L'identification des réglementations applicables (obligatoires, conditionnelles, informatives)
- La méthodologie d'évaluation pour déterminer l'applicabilité réglementaire
- Les processus de révision et de mise à jour face aux évolutions du paysage réglementaire

**Ce que cette politique N'ÉTABLIT PAS :**

- Les décisions de traitement des risques (traitées dans la Clause 6 — Management des risques)
- Les exigences de mise en œuvre des contrôles (traitées dans les contrôles de l'Annexe A)
- Le statut de conformité ou la vérification (traités dans les processus de surveillance de la conformité)

**Séparation des responsabilités :**

- **Cette politique (POL-00)** : Définit QUELLES réglementations s'appliquent
- **Management des risques (Clause 6)** : Détermine COMMENT répondre aux exigences réglementaires
- **Mise en œuvre des contrôles (Annexe A)** : Met en œuvre les CONTRÔLES SPÉCIFIQUES
- **Surveillance de la conformité** : Vérifie et suit le STATUT DE CONFORMITÉ

---

**FIN DE ISMS-POL-00-FR**

*« L'applicabilité réglementaire est le fondement. La mise en œuvre et la conformité sont la structure construite sur ce fondement. »*

<!-- QA_VERIFIED: 2026-07-31 -->
