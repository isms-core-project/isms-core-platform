<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.19-23-S1-FR:framework:POL:a.5.19-23-s1 -->
**ISMS-POL-A.5.19-23-S1 — Fondamentaux des relations fournisseurs**
**Contrôle A.5.19 : Sécurité de l'information dans les relations avec les fournisseurs**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Fondamentaux des relations fournisseurs |
| **Type de document** | Section de politique |
| **Identifiant du document** | ISMS-POL-A.5.19-23-S1 |
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
| 1.0 | [Date] | RSI | Section initiale pour le contrôle ISO 27001:2022 A.5.19 |

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
- ISMS-POL-A.5.19-23-S2 (Exigences des accords fournisseurs)
- ISMS-IMP-A.5.19-23.S1-UG/TG (Inventaire et classification des services en nuage)
- ISMS-REF-A.5.23 (Registre des prestataires de services en nuage)
- ISO/IEC 27001:2022 Contrôle A.5.19
- ISO/IEC 27036-1 (Sécurité de l'information pour les relations fournisseurs — Présentation et concepts)

---

# Objet

La présente section définit les exigences fondamentales pour la gestion des risques de sécurité de l'information dans les relations fournisseurs. Elle établit le cadre de classification, la méthodologie d'évaluation des risques et les exigences de diligence raisonnable applicables à tous les fournisseurs externes.

**Principe critique — « Connaissez vos fournisseurs avant qu'ils ne connaissent vos données »** : Les relations fournisseurs doivent commencer par une évaluation systématique des risques et une diligence raisonnable fondée sur des preuves, et non par une découverte post-contractuelle. Accorder l'accès à un fournisseur sans classification, permettre l'accès aux données sans diligence raisonnable, ou signer des contrats sans évaluation de sécurité crée des risques inacceptables et potentiellement irrécupérables. La sélection des fournisseurs est une décision de sécurité, pas seulement une décision d'achats.

**ISO/IEC 27001:2022 Contrôle A.5.19 — Sécurité de l'information dans les relations avec les fournisseurs**

> *Des processus et procédures devraient être définis et convenus avec les fournisseurs pour gérer les risques de sécurité de l'information associés à l'utilisation des produits ou services du fournisseur.*

**Objectif du contrôle** : S'assurer que les risques de sécurité de l'information associés aux relations fournisseurs sont identifiés, évalués et gérés tout au long du cycle de vie de la relation.

**Synthèse des orientations ISO/IEC 27002:2022** :

- Les relations fournisseurs doivent être gérées via des processus définis couvrant le cycle de vie complet (sélection, intégration, exploitation, sortie)
- Les fournisseurs doivent être identifiés et classifiés selon le type d'accès, la sensibilité des données et la criticité du service
- Une diligence raisonnable doit être effectuée avant d'accorder l'accès des fournisseurs aux informations ou systèmes organisationnels
- Les exigences de sécurité des fournisseurs doivent être définies sur la base de la classification des risques et des données
- La performance et la posture de sécurité des fournisseurs doivent être surveillées tout au long de la relation
- Des procédures de sortie fournisseur doivent être établies pour assurer une résiliation sécurisée et le retour des données
- L'informatique fantôme et l'utilisation non autorisée de fournisseurs doivent être activement identifiées et gérées
- Les risques de dépendance et de concentration des fournisseurs doivent être évalués pour les services critiques

---

# Périmètre

## Types de fournisseurs applicables

| Type de fournisseur | Description | Exemples |
|---------------------|-------------|----------|
| **Prestataires de services en nuage** | Fournisseurs d'IaaS, PaaS, SaaS, services XDR | Calcul, stockage, messagerie, plateformes de sécurité |
| **Prestataires de services gérés** | Exploitation et support IT externalisés | Service d'assistance, gestion réseau, services SOC |
| **Éditeurs de logiciels** | Fournisseurs de logiciels sous licence ou par abonnement | ERP, CRM, outils de développement |
| **Fournisseurs de matériel** | Fournisseurs d'équipements IT physiques | Serveurs, équipements réseau, postes de travail |
| **Services professionnels** | Consultants avec accès aux systèmes/données | Auditeurs, intégrateurs, développeurs |
| **Fournisseurs d'installations** | Services de centres de données et d'hébergement | Colocation, sécurité physique |
| **Télécommunications** | Fournisseurs de réseau et de connectivité | Internet, WAN, services voix |

## Exclusions

La présente politique ne s'applique pas à :

- Les fournisseurs proposant des biens/services sans accès aux informations organisationnelles
- Les achats ponctuels sans relation continue
- Les clients individuels des services de [Organisation]

---

# Classification des fournisseurs

## Critères de classification

Les fournisseurs doivent être classifiés sur la base des facteurs suivants :

| Facteur | Pondération | Questions d'évaluation |
|---------|-------------|------------------------|
| **Accès aux données** | Élevée | À quels niveaux de classification des données le fournisseur peut-il accéder ? |
| **Accès aux systèmes** | Élevée | Le fournisseur a-t-il accès aux systèmes de production ? |
| **Criticité du service** | Élevée | Une défaillance du fournisseur aurait-elle un impact sur les opérations ? |
| **Remplaçabilité** | Moyenne | Dans quelle mesure le fournisseur peut-il être remplacé facilement ? |
| **Profondeur d'intégration** | Moyenne | À quel point les services du fournisseur sont-ils intégrés ? |
| **Impact réglementaire** | Élevée | Le fournisseur affecte-t-il la conformité réglementaire ? |

## Niveaux de classification

### Niveau 1 : Fournisseurs critiques

**Critères (tout élément déclenche le Niveau 1) :**

- Accès aux données Restreintes ou Confidentielles
- Accès direct aux systèmes ou infrastructures de production
- Point de défaillance unique pour les processus métier critiques
- Dépendance de conformité réglementaire (prestataire critique DORA, service essentiel NIS2, sous-traitant RGPD pour le traitement à haut risque)

**Exigences :**

- Évaluation annuelle sur site ou à distance détaillée
- Revues de performance et de sécurité trimestrielles
- Plan de continuité d'activité documenté
- Clause de droit d'audit obligatoire
- Sponsor exécutif désigné
- Certification SOC 2 Type II ou ISO/IEC 27001 requise
- Notification d'incident dans les 4 heures
- Divulgation et approbation des sous-traitants ultérieurs

### Niveau 2 : Fournisseurs à risque élevé

**Critères :**

- Accès aux données de classification Interne
- Accès aux systèmes hors production (développement, test)
- Fonction métier importante mais non critique
- Plusieurs options fournisseurs disponibles
- Sous-traitant RGPD pour le traitement à risque standard

**Exigences :**

- Évaluation de sécurité annuelle (questionnaire + preuves)
- Revues de performance semestrielles
- Considérations de continuité d'activité documentées
- Clause de droit d'audit recommandée
- Certification SOC 2 ou ISO/IEC 27001 requise
- Notification d'incident dans les 24 heures
- Divulgation des sous-traitants ultérieurs

### Niveau 3 : Fournisseurs à risque moyen

**Critères :**

- Accès limité aux données (Public ou Interne minimal)
- Pas d'accès direct aux systèmes
- Fonction métier de soutien
- Facilement remplaçable
- Aucun impact sur la conformité réglementaire

**Exigences :**

- Évaluation de sécurité bisannuelle
- Revue de performance annuelle
- Clauses de sécurité contractuelles standard
- Certification préférable si traitement de données organisationnelles
- Notification d'incident dans les 72 heures

### Niveau 4 : Fournisseurs à faible risque

**Critères :**

- Pas d'accès aux données organisationnelles
- Pas d'accès aux systèmes
- Services génériques
- Multiples alternatives disponibles
- Aucun impact réglementaire

**Exigences :**

- Diligence raisonnable initiale uniquement
- Conditions générales standard
- Revue lors du renouvellement contractuel

## Matrice de classification

```
                    │ Pas d'accès │ Accès hors  │ Accès       │
                    │ aux systèmes│ production  │ production  │
────────────────────┼─────────────┼─────────────┼─────────────┤
Données Restreintes │ Niveau 2    │ Niveau 1    │ Niveau 1    │
Données Confidenti. │ Niveau 2    │ Niveau 1    │ Niveau 1    │
Données Internes    │ Niveau 3    │ Niveau 2    │ Niveau 2    │
Données Publiques   │ Niveau 4    │ Niveau 3    │ Niveau 3    │
Pas d'accès données │ Niveau 4    │ Niveau 4    │ Niveau 3    │
```

**Réévaluation de la classification** : La classification des fournisseurs doit être réévaluée :

- Annuellement pour tous les fournisseurs
- Lors d'un changement significatif du périmètre de service
- Lors d'une fusion/acquisition du fournisseur
- Suite à un incident de sécurité majeur
- Lors de changements de périmètre réglementaire (ex. : applicabilité DORA/NIS2)

---

# Évaluation des risques fournisseurs

## Catégories de risques

| Catégorie | Description | Axes d'évaluation |
|-----------|-------------|-------------------|
| **Risque de confidentialité** | Divulgation non autorisée d'informations | Traitement des données, contrôles d'accès, chiffrement |
| **Risque d'intégrité** | Modification non autorisée des données/systèmes | Gestion des changements, validation des entrées, contrôles qualité |
| **Risque de disponibilité** | Interruption de service ou perte de données | Redondance, sauvegarde, reprise après sinistre, engagements SLA |
| **Risque de conformité** | Violations réglementaires ou contractuelles | Certifications, rapports d'audit, attestations, alignement réglementaire |
| **Risque de concentration** | Dépendance excessive envers un seul fournisseur | Alternatives sur le marché, faisabilité de sortie, enfermement fournisseur |
| **Risque géopolitique** | Facteurs juridictionnels ou politiques | Résidence des données, cadres légaux, exposition au CLOUD Act américain |

## Processus d'évaluation des risques

**Étape 1 : Collecte d'informations**

- Questionnaire de sécurité du fournisseur
- Revue documentaire (certifications, politiques, procédures)
- Analyse de la documentation technique (architecture, flux de données)
- Évaluation de la stabilité financière (pour les fournisseurs de Niveau 1)
- Vérification des références auprès des clients existants

**Étape 2 : Identification des risques**

- Mapper les services fournisseurs aux catégories de risques
- Identifier les scénarios de menaces potentiels par catégorie
- Documenter les contrôles existants (fournisseur + organisationnels)
- Évaluer le modèle de responsabilité partagée (pour les services en nuage)
- Évaluer les risques des sous-traitants ultérieurs et de la chaîne d'approvisionnement

**Étape 3 : Évaluation des risques**

- Évaluer la probabilité et l'impact par catégorie de risque
- Calculer le score de risque par catégorie (Section 4.3)
- Déterminer la cote de risque globale du fournisseur
- Comparer par rapport à l'appétit et la tolérance au risque

**Étape 4 : Traitement des risques**

- **Accepter** : Risque dans la tolérance, documenter l'acceptation avec approbation du RSSI
- **Atténuer** : Contrôles supplémentaires requis (clauses contractuelles, contrôles techniques, surveillance)
- **Transférer** : Dispositions d'assurance ou de responsabilité contractuelle
- **Éviter** : Ne pas procéder à l'engagement fournisseur

**Étape 5 : Documentation**

- Rapport d'évaluation des risques avec constatations et recommandations
- Plan de traitement des risques avec responsabilités et délais assignés
- Dossiers d'approbation (RSSI pour les risques élevés/critiques)
- Intégration dans le registre des fournisseurs

## Notation des risques

| Probabilité | Impact : Faible | Impact : Moyen | Impact : Élevé | Impact : Critique |
|-------------|-----------------|----------------|----------------|-------------------|
| **Rare** | 1 | 2 | 3 | 4 |
| **Improbable** | 2 | 4 | 6 | 8 |
| **Possible** | 3 | 6 | 9 | 12 |
| **Probable** | 4 | 8 | 12 | 16 |
| **Quasi-certain** | 5 | 10 | 15 | 20 |

**Seuils de cote de risque :**

- **1-4 :** Risque faible → Contrôles standard, revue annuelle
- **5-9 :** Risque moyen → Contrôles renforcés, revue semestrielle
- **10-15 :** Risque élevé → Contrôles significatifs + approbation RSSI + revue trimestrielle
- **16-20 :** Risque critique → Approbation de la direction générale + surveillance continue + plan d'atténuation obligatoire

**Risque inacceptable** : Les scores de risque 16-20 sans atténuation réalisable doivent entraîner le rejet du fournisseur ou la résiliation de la relation.

---

# Exigences de diligence raisonnable

## Diligence raisonnable par niveau de classification

| Exigence | Niveau 1 | Niveau 2 | Niveau 3 | Niveau 4 |
|----------|----------|----------|----------|----------|
| Questionnaire de sécurité | ✓ Détaillé | ✓ Standard | ✓ Basique | — |
| Vérification des certifications | ✓ Requise | ✓ Requise | ✓ Si déclarées | — |
| Revue des documents de politique | ✓ Requise | ✓ Requise | — | — |
| Évaluation technique | ✓ Requise | ✓ Basée sur les risques | — | — |
| Vérification de stabilité financière | ✓ Requise | ✓ Recommandée | — | — |
| Vérification des références | ✓ Requise | ✓ Recommandée | — | — |
| Évaluation sur site | ✓ Basée sur les risques | — | — | — |
| Revue du test d'intrusion | ✓ Requise | ✓ Si disponible | — | — |
| Évaluation des sous-traitants | ✓ Requise | ✓ Si applicable | — | — |
| Accord de traitement des données | ✓ Requis | ✓ Requis | ✓ Si accès données | — |
| Revue de la continuité d'activité | ✓ Requise | ✓ Requise | ✓ Si critique | — |

## Certifications de sécurité

**Certifications préférées (par ordre de préférence) :**

| Certification | Périmètre | Validité | Notes |
|---------------|-----------|----------|-------|
| ISO/IEC 27001 | Système de management de la sécurité de l'information | 3 ans (surveillance annuelle) | Norme mondiale, complète |
| SOC 2 Type II | Critères de confiance des services | 12 mois | Axé sur les États-Unis, contrôles détaillés |
| SOC 2 Type I | Évaluation à un instant donné | À un instant donné | Moins rigoureux que le Type II |
| ISO/IEC 27017 | Contrôles de sécurité en nuage | 3 ans | Extension spécifique au nuage |
| ISO/IEC 27018 | Protection de la vie privée en nuage | 3 ans | Protection de la vie privée dans le nuage |
| CSA STAR | Maturité de sécurité nuage | Variable selon le niveau | Auto-évaluation jusqu'à certifié |

**Exigences de certification par niveau :**

- **Niveau 1 :** ISO/IEC 27001 ou SOC 2 Type II requis (en cours dans les 12 mois)
- **Niveau 2 :** ISO/IEC 27001 ou SOC 2 (Type I acceptable) requis (en cours dans les 12 mois)
- **Niveau 3 :** Certification préférable mais non obligatoire si traitement de données organisationnelles
- **Niveau 4 :** Aucune exigence de certification

**Critères d'acceptation des certifications :**

- Le certificat doit être en cours (dans la période de validité)
- Le périmètre doit couvrir les services fournis à [Organisation]
- L'organisme émetteur doit être accrédité (ISO : organisme de certification accrédité ; SOC : cabinet CPA agréé)
- Pour les certificats pluriannuels (ISO), les audits de surveillance annuels doivent être complétés

**Attestations alternatives** : Si les certifications ISO/SOC ne sont pas disponibles, [Organisation] peut accepter :

- Certifications gouvernementales (FedRAMP, C5 en Allemagne)
- Certifications sectorielles (PCI DSS v4.0.1 pour les processeurs de paiement, HITRUST pour la santé)
- Rapports détaillés d'audit de sécurité tiers (nécessite l'approbation du RSSI)

## Documentation de la diligence raisonnable

Toutes les activités de diligence raisonnable doivent être documentées, notamment :

- Questionnaires de sécurité complétés avec preuves
- Copies des certifications avec vérification de la validité
- Résultats et notation de l'évaluation des risques
- Justification de la décision et dossiers d'approbation
- Lacunes identifiées et plans de remédiation
- Contrôles compensatoires le cas échéant
- Réponses du fournisseur aux constatations
- Éléments de suivi et suivi de clôture

**Conservation de la documentation** : La documentation de diligence raisonnable doit être conservée :

- Pendant la durée de la relation fournisseur + 7 ans (exigence réglementaire)
- Au minimum 3 ans après la résiliation de la relation
- Conservation permanente pour les fournisseurs de Niveau 1 impliqués dans des incidents significatifs

---

# Exigences de sécurité de l'information

## Exigences de base (Tous les fournisseurs avec accès aux données)

| Exigence | Description |
|----------|-------------|
| **Contrôle d'accès** | Principe du moindre privilège, comptes individuels, accès basé sur les rôles, journalisation des accès |
| **Authentification** | Authentification forte (mots de passe complexes ou certificats), AMF pour les accès privilégiés |
| **Chiffrement en transit** | Données chiffrées lors de la transmission avec TLS 1.2+ ou équivalent |
| **Signalement des incidents** | Incidents de sécurité signalés à [Organisation] dans les 24 heures suivant la prise de connaissance |
| **Sécurité du personnel** | Vérifications des antécédents adaptées au niveau d'accès pour le personnel accédant aux données de [Organisation] |
| **Confidentialité** | NDA ou engagement contractuel de confidentialité équivalent |
| **Minimisation des données** | Accès uniquement aux données nécessaires à la prestation du service |
| **Résidence des données** | Traitement des données dans les juridictions approuvées conformément au contrat |

## Exigences renforcées (Fournisseurs de Niveaux 1 et 2)

| Exigence | Description |
|----------|-------------|
| **Chiffrement au repos** | Données chiffrées au repos avec des algorithmes robustes (AES-256 ou équivalent) |
| **Gestion des vulnérabilités** | Scans réguliers de vulnérabilités, correctifs dans les délais (critiques dans les 30 jours, élevés dans les 60 jours) |
| **Surveillance de la sécurité** | Journalisation, alertes, intégration SIEM le cas échéant, conservation conformément aux exigences réglementaires |
| **Continuité d'activité** | Plans PCA/PRA documentés et tests annuels avec preuves fournies |
| **Droits d'audit** | [Organisation] peut auditer ou examiner les rapports d'audit tiers (SOC 2, surveillance ISO 27001) |
| **Contrôles sur les sous-traitants** | Les exigences de sécurité s'appliquent aux sous-traitants, divulgation requise |
| **Gestion des changements** | Contrôle formel des changements avec notification de [Organisation] pour les changements importants |
| **Ségrégation des données** | Ségrégation logique ou physique des autres clients (contrôles de multilocation) |
| **Développement sécurisé** | SDLC avec tests de sécurité pour le développement personnalisé ou les intégrations |
| **Réponse aux incidents** | Plan de réponse aux incidents documenté avec coordonnées et procédures d'escalade |

---

# Registre des fournisseurs

## Exigences du registre

[Organisation] DOIT maintenir un registre complet des fournisseurs contenant :

| Champ | Description | Déclencheur de mise à jour |
|-------|-------------|---------------------------|
| Nom du fournisseur | Raison sociale | Changement contractuel |
| Type de fournisseur | Catégories de la Section 2.1 | Changement de service |
| Niveau de classification | Niveaux 1-4 de la Section 3 | Revue annuelle |
| Services fournis | Description des services/produits | Changement de service |
| Accès aux données | Classification des données accessibles | Changement d'accès |
| Accès aux systèmes | Systèmes accessibles au fournisseur | Changement d'accès |
| Référence contractuelle | Lien vers l'accord et les avenants | Changement contractuel |
| Responsable métier | Responsable de la relation interne | Changement organisationnel |
| Contact sécurité | Point de contact sécurité du fournisseur | Changement fournisseur |
| Date de dernière évaluation | Évaluation de sécurité la plus récente | Achèvement de l'évaluation |
| Date de prochaine revue | Date de revue planifiée | Changement de classification |
| Cote de risque | Score de risque actuel de la Section 4.3 | Achèvement de l'évaluation |
| Certifications | Certifications en cours avec dates d'expiration | Renouvellement du certificat |
| Périmètre réglementaire | Applicabilité DORA/NIS2/RGPD | Changement commercial |
| Complexité de sortie | Facilité de remplacement du service (Faible/Moyenne/Élevée) | Revue annuelle |

## Maintenance du registre

- Registre mis à jour lors de l'intégration d'un nouveau fournisseur (dans les 5 jours ouvrés)
- Registre mis à jour lors de changements contractuels (dans les 10 jours ouvrés)
- Revue trimestrielle pour l'exactitude par le RSI
- Audit annuel de complétude par l'audit interne ou le RSSI
- Disponibilité du registre : Accessible aux Achats, IT, Sécurité, Juridique, Audit

**Outils du registre** : Le registre des fournisseurs peut être maintenu dans :

- Plateforme GRC (Gouvernance, Risque, Conformité) dédiée
- Système de gestion des achats avec module sécurité
- Excel/base de données avec contrôle des versions (acceptable au minimum)
- Cahier d'évaluation ISMS-IMP-A.5.19-23-1 (Inventaire des services en nuage)

---

# Prévention de l'informatique fantôme

## Définition de l'informatique fantôme

**Informatique fantôme (Shadow IT)** : Utilisation de fournisseurs, services en nuage ou logiciels non autorisés sans approbation IT et Sécurité. L'informatique fantôme contourne les contrôles de sécurité, la diligence raisonnable et les protections contractuelles, créant des risques non gérés et souvent indétectables.

## Mesures de prévention

| Mesure | Description |
|--------|-------------|
| **Catalogue de services approuvés** | Maintenir et communiquer la liste des fournisseurs et services approuvés |
| **Intégration achats** | Exiger l'approbation IT/Sécurité dans le flux de travail des achats |
| **Surveillance réseau** | Surveiller le trafic réseau pour les services en nuage non approuvés |
| **Contrôles des postes de travail** | Liste blanche d'applications ou surveillance des logiciels non approuvés |
| **Sensibilisation des utilisateurs** | Formation régulière sur le processus d'approbation des fournisseurs et les risques du Shadow IT |
| **Canal de signalement** | Mécanisme simple pour les utilisateurs souhaitant demander l'évaluation d'un nouveau service |

## Réponse à la découverte du Shadow IT

**En cas de découverte :**
1. Identifier le service et les utilisateurs
2. Évaluer le risque (accès aux données, criticité, impact conformité)
3. Décision : Approuver rétrospectivement, migrer vers une alternative approuvée, ou résilier
4. Si approuvé : Exécuter l'intégration accélérée avec acceptation du risque
5. Si résilié : Communiquer aux utilisateurs, bloquer l'accès, migrer les données si nécessaire
6. Analyse des causes profondes : Pourquoi les utilisateurs ont-ils contourné le processus d'approbation ?

---

# Rôles et responsabilités

| Rôle | Responsabilités |
|------|-----------------|
| **Responsable métier** | Identifier le besoin fournisseur, maintenir la relation, s'assurer que le service répond aux besoins métier, approbation budgétaire |
| **Achats** | Coordination du processus de sélection des fournisseurs, négociation et gestion des contrats, appels d'offres |
| **Responsable de la sécurité de l'information** | Évaluation des risques, définition des exigences de sécurité, revue et approbation des évaluations, maintenance du registre |
| **Juridique/Conformité** | Revue des contrats, vérification de la conformité réglementaire, revue des accords de traitement des données, résolution des litiges |
| **Exploitation informatique** | Mise en œuvre technique, provisionnement des accès, support d'intégration, surveillance des performances |
| **RSSI** | Approbation de la politique, approbation des fournisseurs à risque élevé, approbation des exceptions, rapport exécutif |
| **DPD** | Vérification de la conformité RGPD, approbation des accords de traitement des données, analyses d'impact sur la protection des données |

**Matrice des responsabilités** (RACI) :

| Activité | Responsable métier | Achats | Sécurité | Juridique | Exploitation IT | RSSI |
|----------|--------------------|--------|----------|-----------|-----------------|------|
| Identification du fournisseur | R | C | I | I | C | I |
| Évaluation des risques | C | C | R | C | C | A |
| Négociation contractuelle | I | R | C | R | I | I |
| Revue de sécurité | I | I | R | C | C | A |
| Intégration | C | C | C | I | R | I |
| Surveillance continue | A | C | R | I | C | I |
| Approbation d'exception | I | I | C | C | I | A |

*R=Responsable, A=Imputable, C=Consulté, I=Informé*

---

# Références

| Document | Relation |
|----------|----------|
| **ISMS-POL-A.5.19-23** | Cadre de politique parent |
| **ISMS-POL-A.5.19-23-S2** | Exigences des accords fournisseurs (Contrôle A.5.20) |
| **ISMS-POL-A.5.19-23-S3** | Sécurité de la chaîne d'approvisionnement TIC (Contrôle A.5.21) |
| **ISMS-IMP-A.5.19-23.S1-UG/TG** | Cahier d'évaluation de l'inventaire des services en nuage |
| **ISMS-IMP-A.5.19-23.S2-UG/TG** | Cahier d'évaluation de la diligence raisonnable fournisseurs |
| **ISO/IEC 27036-1:2021** | Sécurité de l'information pour les relations fournisseurs — Présentation |
| **NIST SP 800-161** | Gestion des risques de la chaîne d'approvisionnement en cybersécurité |

---

**Document suivant :** ISMS-POL-A.5.19-23-S2 — Exigences des accords fournisseurs (Contrôle A.5.20)

---

*« La solidité de votre sécurité est aussi forte que votre maillon fournisseur le plus faible. »*

<!-- QA_VERIFIED: 2026-03-30 -->
