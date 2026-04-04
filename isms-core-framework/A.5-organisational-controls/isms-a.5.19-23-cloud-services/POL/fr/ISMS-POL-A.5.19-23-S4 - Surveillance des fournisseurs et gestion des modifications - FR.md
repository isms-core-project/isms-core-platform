<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.19-23-S4-FR:framework:POL:a.5.19-23-s4 -->
**ISMS-POL-A.5.19-23-S4 — Surveillance des fournisseurs et gestion des modifications**
**Contrôle A.5.22 : Surveillance, révision et gestion des modifications des services fournisseurs**

---

**Contrôle documentaire**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Surveillance des fournisseurs et gestion des modifications |
| **Type de document** | Section de politique |
| **Identifiant du document** | ISMS-POL-A.5.19-23-S4 |
| **Créateur du document** | Responsable de la sécurité de l'information (RSI) |
| **Propriétaire du document** | Responsable de la sécurité des systèmes d'information (RSSI) |
| **Approuvé par** | Direction générale |
| **Date de création** | [Date] |
| **Version** | 1.0 |
| **Date de version** | [À déterminer] |
| **Classification** | Interne |
| **Statut** | Brouillon |

**Historique des versions** :

| Version | Date | Auteur | Modifications |
|---------|------|--------|---------------|
| 1.0 | [Date] | RSI | Section initiale pour le contrôle ISO 27001:2022 A.5.22 |

**Cycle de révision** : Annuel
**Prochaine révision** : [Date d'entrée en vigueur + 12 mois]

**Chaîne d'approbation** :

- Primaire : Responsable de la sécurité des systèmes d'information (RSSI)
- Secondaire : Responsable de la sécurité de l'information (RSI)
- Conformité : Responsable juridique/conformité
- Opérations : Directeur des systèmes d'information (DSI)
- Autorité finale : Direction générale

**Documents connexes** :

- ISMS-POL-00 (Cadre d'applicabilité réglementaire)
- ISMS-POL-A.5.19-23 (Politique parente — Sécurité des fournisseurs et des services en nuage)
- ISMS-POL-A.5.19-23-S1 (Fondamentaux des relations fournisseurs)
- ISMS-IMP-A.5.19-23.S4-UG/TG (Gouvernance continue et gestion des risques)
- ISMS-REF-A.5.23 (Registre des fournisseurs de services en nuage)
- ISO/IEC 27001:2022 Contrôle A.5.22
- ISO/IEC 27036-4 (Services en nuage)

---

# Objet

La présente section définit les exigences relatives à la surveillance continue, aux révisions périodiques et à la gestion des modifications des services fournisseurs. Elle garantit que la posture de sécurité des fournisseurs est continuellement validée et que les modifications n'introduisent pas de risques inacceptables.

**Principe fondamental — « La confiance se dégrade avec le temps »** : Un fournisseur ayant satisfait à la diligence raisonnable initiale n'est pas garanti de demeurer sécurisé. Les certifications expirent, les pratiques de sécurité dérivent, les structures de propriété changent et des incidents surviennent. La surveillance continue et la réévaluation périodique ne sont pas un contrôle optionnel — elles sont des contrôles essentiels qui détectent la dégradation avant qu'elle ne devienne une violation. La présente politique exige une validation systématique et fondée sur des preuves tout au long du cycle de vie de la relation fournisseur.

**ISO/IEC 27001:2022 Contrôle A.5.22 — Surveillance, révision et gestion des modifications des services fournisseurs**

> *L'organisation devrait surveiller, réviser, évaluer et gérer régulièrement les changements dans les pratiques de sécurité de l'information des fournisseurs et la livraison des services.*

**Objectif de contrôle** : Assurer la validation continue de la posture de sécurité des fournisseurs et une gestion maîtrisée des modifications apportées aux services fournisseurs.

**Résumé des lignes directrices ISO/IEC 27002:2022** :

- Les performances des fournisseurs doivent être surveillées en continu au regard des engagements contractuels et des SLA
- Des révisions périodiques des pratiques de sécurité des fournisseurs doivent être réalisées selon leur niveau de risque
- Les modifications apportées aux services fournisseurs doivent être gérées par des procédures formelles de contrôle des modifications avec revue de sécurité
- La conformité des fournisseurs aux accords doit être vérifiée par des audits, des attestations ou des certifications tierces
- Les incidents et événements de sécurité impliquant les fournisseurs doivent être suivis, analysés et traités de manière appropriée
- Les rapports d'audit ou attestations tierces (SOC 2, ISO 27001) doivent être obtenus et examinés pour identifier les constats
- La relation avec les fournisseurs doit être entretenue par des communications régulières, des révisions et des réunions de gouvernance
- La dégradation de service ou la non-conformité d'un fournisseur doit déclencher des procédures d'escalade et de correction, y compris la résiliation potentielle

---

# Périmètre d'application

## Activités de surveillance

| Type d'activité | Description |
|-----------------|-------------|
| **Surveillance des performances** | Conformité aux SLA, métriques de qualité de service, suivi de la disponibilité |
| **Surveillance de la sécurité** | Évaluation de la posture de sécurité, suivi des incidents, statut des vulnérabilités, validité des certifications |
| **Surveillance de la conformité** | Validité des certifications, vérification de la conformité réglementaire, révision des rapports d'audit |
| **Surveillance des relations** | Efficacité des communications, résolution des problèmes, satisfaction des parties prenantes |
| **Surveillance des modifications** | Modifications de service, changements de personnel, changements de propriété, modifications d'infrastructure |

## Applicabilité par niveau de fournisseur

| Activité | Niveau 1 (Critique) | Niveau 2 (Élevé) | Niveau 3 (Moyen) | Niveau 4 (Faible) |
|----------|---------------------|------------------|------------------|-------------------|
| Surveillance des performances | Continue (automatisée) | Rapports mensuels | Trimestrielle | Annuelle |
| Évaluation de la sécurité | Annuelle complète | Annuelle standard | Bisannuelle | Initial seulement |
| Vérification de la conformité | Contrôle trimestriel des certifications | Semestrielle | Annuelle | À la reconduction |
| Révision de la relation | Gouvernance trimestrielle | Semestrielle | Annuelle | Selon les besoins |
| Révision des modifications | Toutes les modifications pré-approuvées | Modifications significatives examinées | Modifications importantes seulement | Conditions standard |

---

# Cycles de révision

## Calendrier de révision par niveau de fournisseur

| Niveau de fournisseur | Révision de sécurité | Révision des performances | Révision de la relation |
|----------------------|---------------------|--------------------------|------------------------|
| **Niveau 1 (Critique)** | Annuelle complète + surveillance continue | Rapports SLA mensuels | Réunions de gouvernance trimestrielles |
| **Niveau 2 (Élevé)** | Évaluation annuelle standard | Révision trimestrielle des performances | Bilan semestriel de la relation |
| **Niveau 3 (Moyen)** | Questionnaire de sécurité bisannuel | Semestrielle | Révision annuelle |
| **Niveau 4 (Faible)** | À la reconduction seulement | Synthèse annuelle | À la reconduction seulement |

## Déclencheurs de révision non programmée

Au-delà des révisions planifiées, déclencher une révision immédiate lors de :

| Déclencheur | Périmètre de la révision | Délai |
|-------------|--------------------------|-------|
| Incident de sécurité impliquant le fournisseur (confirmé) | Révision complète de sécurité, conformité contractuelle | Sous 48 heures |
| Modification de service significative (architecture, plateforme, localisation) | Évaluation de l'impact, réévaluation des risques | Avant mise en œuvre |
| Changement de propriété du fournisseur (F&A, acquisition) | Renouvellement de la diligence raisonnable, révision contractuelle | Sous 30 jours |
| Expiration ou perte de certification | Révision de la conformité, évaluation des risques | Immédiatement |
| Modification ou avenant contractuel significatif | Vérification des clauses de sécurité, analyse d'impact | Avant signature |
| Changement réglementaire affectant les obligations du fournisseur | Évaluation de la conformité, analyse des écarts | Sous 60 jours |
| Événement négatif ou atteinte à la réputation (incident public) | Réévaluation des risques, communication avec le fournisseur | Sous 7 jours |
| Changement organisationnel significatif (l'[Organisation] ou le fournisseur) | Révision de la relation, validation des accès | Sous 30 jours |
| Défaillances répétées des SLA (3 consécutives ou 6 en 12 mois) | Révision des performances, plan de correction | Immédiatement |
| Constat d'audit lié au fournisseur | Révision de la conformité, suivi des corrections | Sous 14 jours |

## Calendrier annuel de révision

```
┌─────────────────────────────────────────────────────────────────────┐
│ CALENDRIER DE RÉVISION DES FOURNISSEURS (Exemple)                   │
├─────────────────────────────────────────────────────────────────────┤
│ T1 (Jan-Mars) :                                                     │
│     • Fournisseurs niveau 1 — Évaluation annuelle de sécurité       │
│     • Tous les fournisseurs — Vérification de la validité des       │
│       certifications                                                 │
│     • Reconductions de contrats (expirations T1)                    │
│                                                                     │
│ T2 (Avr-Juin) :                                                     │
│     • Fournisseurs niveau 2 — Évaluation annuelle de sécurité       │
│     • Fournisseurs niveau 1 — Réunion de gouvernance trimestrielle  │
│     • Contrôle de conformité de mi-année                            │
│                                                                     │
│ T3 (Juil-Sept) :                                                    │
│     • Fournisseurs niveau 1 — Réunion de gouvernance trimestrielle  │
│     • Fournisseurs niveau 3 — Révision annuelle (si prévue ce cycle)│
│     • Préparation du reporting de fin d'année                       │
│                                                                     │
│ T4 (Oct-Déc) :                                                      │
│     • Fournisseurs niveau 1 — Réunion de gouvernance trimestrielle  │
│     • Tous les fournisseurs — Validation annuelle du registre       │
│     • Planification du cycle de révision de l'année suivante        │
│     • Reporting de conformité de fin d'année                        │
└─────────────────────────────────────────────────────────────────────┘
```

---

# Surveillance des performances

## Surveillance des niveaux de service

| Catégorie de métrique | Exemples | Fréquence de surveillance | Seuil d'alerte |
|----------------------|----------|--------------------------|----------------|
| Disponibilité | Taux de disponibilité, incidents de panne non planifiée | Continue/Temps réel | En dessous de la cible SLA |
| Performances | Temps de réponse, débit, latence | Continue/Temps réel | Dégradation > 10 % |
| Support | Temps de réponse aux tickets, délai de résolution, escalades | Agrégation hebdomadaire | Violation des SLA |
| Capacité | Utilisation des ressources, marge de scalabilité | Analyse tendancielle mensuelle | Utilisation > 80 % |
| Qualité | Taux d'erreur, taux de succès des transactions, satisfaction client | Révision mensuelle | Au-dessus du seuil de référence |

## Suivi de la conformité aux SLA

| Élément | Exigence |
|---------|----------|
| Établissement des référentiels | Documenter les cibles SLA convenues dans le contrat et le système de surveillance |
| Méthodologie de mesure | Suivre les performances réelles par rapport aux cibles à l'aide de métriques objectives |
| Cadence de reporting | Rapports mensuels de conformité aux SLA du fournisseur avec données justificatives |
| Suivi des violations | Enregistrer toutes les violations de SLA avec cause racine, évaluation de l'impact, correction |
| Crédits de service | Suivre et réclamer les crédits de service conformément aux conditions contractuelles en cas de défaillance SLA |
| Analyse tendancielle | Surveiller les schémas de dégradation indiquant des problèmes systémiques |
| Déclencheurs d'escalade | Définir les seuils d'escalade (ex. 3 violations par trimestre) |

## Processus de révision des performances

**Pour les fournisseurs de niveaux 1 et 2 :**

1. **Collecte des données** : Rassembler les rapports fournis par le fournisseur et les données de surveillance interne
2. **Comparaison SLA** : Comparer les performances réelles aux cibles SLA contractuelles
3. **Analyse tendancielle** : Identifier les schémas, les tendances de dégradation, les anomalies
4. **Documentation des problèmes** : Enregistrer les violations de SLA, les problèmes de performance, les demandes de correction
5. **Réunion de révision** : Discuter des résultats lors de la réunion fournisseur trimestrielle/semestrielle
6. **Suivi des corrections** : Suivre les engagements du fournisseur et vérifier leur réalisation
7. **Mise à jour des risques** : Mettre à jour l'évaluation des risques si les performances indiquent un risque accru
8. **Révision contractuelle** : Évaluer si les performances justifient le renouvellement ou la renégociation du contrat

---

# Évaluation de la sécurité

## Méthodes d'évaluation

| Méthode | Description | Applicabilité |
|---------|-------------|---------------|
| **Questionnaire de sécurité** | Évaluation standardisée (200-300 questions pour N1) | Tous les fournisseurs ayant accès aux données ou systèmes |
| **Révision des preuves** | Examen des politiques, procédures, configurations, journaux | Niveaux 1 et 2 |
| **Révision des certifications** | Vérification de la validité ISO 27001, SOC 2, etc. | Niveaux 1, 2, 3 (le cas échéant) |
| **Révision des rapports d'audit** | Examen détaillé des résultats de SOC 2 Type II, audits de surveillance ISO | Niveaux 1 et 2 (obligatoire) |
| **Révision des tests d'intrusion** | Examen des résultats de tests d'intrusion externes du fournisseur | Niveau 1 (obligatoire annuellement) |
| **Révision des analyses de vulnérabilités** | Examen des résultats d'analyse de vulnérabilités du fournisseur | Niveau 1 (obligatoire trimestriellement) |
| **Évaluation sur site** | Visite physique et inspection des installations/contrôles | Niveau 1 (selon le risque, tous les 2-3 ans) |
| **Tests de sécurité techniques** | Analyses de vulnérabilités indépendantes des interfaces exposées par le fournisseur | Niveau 1 (selon le risque) |

## Domaines d'évaluation

| Domaine | Domaines d'évaluation |
|---------|----------------------|
| **Gouvernance et organisation** | Politiques de sécurité, structure organisationnelle, rôles et responsabilités, formation à la sensibilisation |
| **Contrôle d'accès** | Mécanismes d'authentification, modèles d'autorisation, gestion des accès à privilèges, processus de révision des accès |
| **Protection des données** | Classification des données, chiffrement (transit et repos), procédures de traitement des données, prévention des fuites |
| **Sécurité des opérations** | Gestion des modifications, gestion des correctifs, gestion des configurations, sauvegarde et récupération, gestion des capacités |
| **Gestion des incidents** | Capacités de détection, procédures de réponse, processus de notification, revues post-incident |
| **Continuité d'activité** | Plans PCA/PRA, preuves de tests, capacités RTO/RPO, redondance géographique |
| **Conformité** | Certifications actuelles, preuves de conformité réglementaire, correction des constats d'audit, conformité contractuelle |
| **Chaîne d'approvisionnement** | Gestion des sous-traitants, dépendances logicielles (SBOM), gestion des vulnérabilités |

## Gestion des constats d'évaluation

| Gravité du constat | Description | Délai de réponse | Chemin d'escalade |
|-------------------|-------------|------------------|------------------|
| **Critique** | Risque de violation de données, contrôles critiques manquants, chiffrement expiré | Plan de correction immédiat, correction sous 7 jours | RSSI + Propriétaire métier + Direction générale |
| **Élevé** | Lacunes de contrôle significatives, violations de SLA, conformité partielle | Correction sous 30 jours avec mises à jour hebdomadaires | RSI + Propriétaire métier + notification RSSI |
| **Moyen** | Améliorations des contrôles nécessaires, lacunes documentaires, non-conformité mineure | Correction sous 90 jours avec mises à jour mensuelles | RSI + Propriétaire métier |
| **Faible** | Recommandations de bonnes pratiques, améliorations documentaires | Prochain cycle de révision ou 6 mois | Suivi dans le dossier d'évaluation |

**Suivi des constats** : Tous les constats doivent être enregistrés dans le système de gestion des fournisseurs avec :

- Description du constat et preuves
- Classification de la gravité
- Plan de correction et calendrier du fournisseur
- Méthode et critères de vérification
- Suivi du statut (Ouvert → En cours → Vérifié → Clôturé)
- Preuves de clôture

## Documentation des évaluations

Chaque évaluation doit produire une documentation complète :

| Document | Contenu | Conservation |
|----------|---------|-------------|
| **Rapport d'évaluation** | Périmètre, méthodologie, constats avec preuves, réponses du fournisseur | 5 ans |
| **Mise à jour de la notation des risques** | Score de risque fournisseur actualisé selon les constats | Actuel + 3 ans |
| **Plan de correction** | Actions requises, responsables, calendriers, méthode de vérification | Jusqu'à clôture + 2 ans |
| **Synthèse à la direction** | Vue d'ensemble pour les réunions de gouvernance | 3 ans |
| **Preuves de conformité** | Certifications, rapports d'audit, résultats de tests examinés | Actuel + 3 ans |

---

# Surveillance de la conformité

## Suivi des certifications

| Activité | Fréquence | Action en cas d'expiration ou d'échec |
|----------|-----------|--------------------------------------|
| Vérification de la validité ISO 27001 | Trimestrielle | Demander les preuves de renouvellement sous 30 jours, escalader au RSSI si caducité > 60 jours |
| Actualité du SOC 2 Type II | Demande annuelle (30 jours avant l'anniversaire) | Demander un nouveau rapport, réaliser une évaluation des risques en cas de retard |
| Certifications cloud (ISO 27017/27018, CSA STAR) | Annuelle | Vérifier le renouvellement, évaluer l'impact en cas d'abandon |
| Attestations de conformité réglementaire | Annuelle | Demander une lettre de confirmation de la direction du fournisseur |
| Tests d'intrusion | Annuelle | Demander un rapport récent (< 12 mois), vérifier que les constats critiques sont résolus |

## Exigences de preuves de conformité

| Niveau de fournisseur | Preuves requises | Méthode de vérification |
|----------------------|-----------------|------------------------|
| **Niveau 1** | Certification valide + rapport d'audit complet + preuves de correction de tous les constats | Révision détaillée, vérification de la clôture des constats |
| **Niveau 2** | Certification valide + résumé du rapport d'audit ou synthèse | Révision pour les constats significatifs, vérification de la clôture des éléments critiques |
| **Niveau 3** | Certification valide (si déclarée lors de la diligence raisonnable) | Vérification du certificat uniquement |
| **Niveau 4** | Aucune requise | S.O. |

**Vérification des certifications** : Toutes les certifications doivent être vérifiées auprès de l'organisme émetteur :

- ISO 27001 : Consulter la base de données IAF/organisme d'accréditation
- SOC 2 : Vérifier la licence du cabinet comptable agréé, demander une confirmation AICPA si nécessaire
- Certifications sectorielles : Vérifier auprès de l'autorité de certification

## Réponse aux défaillances de conformité

| Scénario | Action immédiate | Délai | Escalade |
|----------|-----------------|-------|---------|
| Certification caduque (récemment expirée) | Délai de régularisation de 30 jours, évaluation des risques, mesures compensatoires | Le fournisseur doit renouveler sous 30 jours | Propriétaire métier + RSI |
| Certification retirée ou révoquée | Évaluation immédiate des risques, envisager la suspension du service en attendant le renouvellement | 14 jours pour résoudre ou engager le remplacement | RSSI + Propriétaire métier |
| Audit échoué (constats significatifs non résolus) | Examiner les constats, exiger un plan de correction avec calendrier | Plan de correction sous 30 jours, exécution sous 90 jours | RSI + Propriétaire métier |
| Violation ou sanction réglementaire | Revue juridique, évaluation de l'exposition de l'[Organisation], documentation de l'acceptation du risque ou stratégie de sortie | Consultation juridique immédiate | Juridique + RSSI + Direction générale |
| Non-conformité répétée (3 incidents ou plus) | Plan d'amélioration des performances formel ou initiation d'une procédure de résiliation | 60 jours d'amélioration ou planification de la transition | RSSI + Direction générale |

---

# Gestion des modifications

## Catégories de modifications

| Type de modification | Description | Notification requise | Approbation requise |
|---------------------|-------------|---------------------|---------------------|
| **Modifications de service** | Fonctionnalités, API, interfaces | Notification préalable (30 jours N1, 14 jours N2) | Modifications significatives (N1) |
| **Modifications d'infrastructure** | Migration de plateforme, déménagement de centre de données, refonte de l'architecture | Approbation préalable (N1), notification préalable (N2) | N1 : Oui, N2 : Si changement de localisation des données |
| **Modifications de sécurité** | Contrôles de sécurité, méthodes de chiffrement, mécanismes d'accès, authentification | Notification préalable (N1-N2) | Modifications de sécurité significatives (N1) |
| **Modifications de personnel** | Contacts clés, responsables de compte, personnel de sécurité | Notification rapide (sous 14 jours) | Non |
| **Changements de propriété** | Acquisition, fusion, cession, changement de contrôle | Notification immédiate (sous 48 heures) | N1 : Oui, N2 : Notification + revue des risques |
| **Modifications de sous-traitants** | Nouveaux sous-traitants ou modifications avec accès aux données | Approbation préalable (N1), notification préalable (N2) | N1 : Oui, N2 : Si accès aux données |
| **Modifications contractuelles** | Conditions, tarifs, SLA, conditions de traitement des données | Selon le processus d'avenant contractuel | Selon le contrat (généralement oui) |
| **Modifications réglementaires/conformité** | Perte de certification, sanctions réglementaires, défaillances de conformité | Notification immédiate | Évaluation des risques requise |

## Exigences de notification des modifications

| Niveau de fournisseur | Notification standard | Approbation des modifications significatives |
|----------------------|----------------------|---------------------------------------------|
| **Niveau 1** | Préavis de 30 jours pour toutes les modifications | Approbation écrite requise avant toute mise en œuvre de modification significative |
| **Niveau 2** | Préavis de 14 jours pour les modifications significatives | Notification suffisante, l'[Organisation] peut s'opposer sous 7 jours |
| **Niveau 3** | Notification rapide des changements importants (7 jours) | Conditions contractuelles standard applicables |
| **Niveau 4** | Conditions contractuelles standard applicables | Aucune exigence spécifique |

## Processus de révision des modifications

```
┌─────────────────────────────────────────────────────────────────────┐
│ PROCESSUS DE RÉVISION DES MODIFICATIONS FOURNISSEURS                │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  1. Le fournisseur notifie l'[Organisation] de la modification      │
│     • Description de la modification et justification métier        │
│     • Calendrier de mise en œuvre                                   │
│     • Évaluation de l'impact (point de vue du fournisseur)          │
│                          ↓                                          │
│  2. Enregistrement dans le registre des modifications fournisseurs  │
│     • Attribution d'un identifiant de demande de modification       │
│     • Routage vers le réviseur approprié (Sécurité/IT/Métier)       │
│                          ↓                                          │
│  3. L'[Organisation] évalue l'impact de la modification             │
│     • Impact sécuritaire (contrôles, risques, vulnérabilités)       │
│     • Impact opérationnel (prestation de service, intégration)      │
│     • Impact conformité (réglementaire, contractuel)                │
│     • Impact métier (coût, calendrier, fonctionnalité)              │
│                          ↓                                          │
│  4. Détermination de la décision                                    │
│     • APPROUVER : Aucune réserve, procéder comme prévu              │
│     • APPROUVER SOUS CONDITIONS : Contrôles/tests supplémentaires   │
│     • DEMANDER UNE MODIFICATION : Changements requis avant accord   │
│     • REJETER : Risque inacceptable (négocier une alternative)      │
│                          ↓                                          │
│  5. Communication de la décision au fournisseur (dans les délais)   │
│     • Décision avec justification                                   │
│     • Conditions ou exigences le cas échéant                        │
│     • Calendrier révisé si nécessaire                               │
│                          ↓                                          │
│  6. Mise à jour de la documentation                                 │
│     • Évaluation des risques (si le profil de risque change)        │
│     • Registre des fournisseurs (enregistrer la modification)       │
│     • Avenants contractuels (le cas échéant)                        │
│                          ↓                                          │
│  7. Vérification de la mise en œuvre (post-modification)            │
│     • Confirmer que la modification a été réalisée comme approuvée  │
│     • Valider l'absence d'impacts inattendus                        │
│     • Clôturer la demande de modification                           │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

## Définition d'une modification significative

Une modification est considérée comme **significative** si elle répond à l'un des critères suivants :

**Liée à la sécurité** :

- Affecte les contrôles de sécurité protégeant les données de l'[Organisation]
- Modifie les méthodes de chiffrement, la gestion des clés ou les mécanismes d'authentification
- Modifie l'architecture de contrôle d'accès ou les procédures d'accès à privilèges
- Introduit une nouvelle surface d'attaque ou étend les vecteurs d'attaque existants

**Liée aux données** :

- Modifie la localisation ou la juridiction du traitement des données (notamment EU/CH vers un pays n'offrant pas de garanties adéquates)
- Modifie les procédures de conservation, de sauvegarde ou de reprise après sinistre
- Modifie les processus de traitement des données ou introduit de nouveaux flux de données
- Affecte l'exercice des droits des personnes concernées ou la conformité RGPD/nLPD

**Liée à la conformité** :

- Affecte la conformité aux exigences réglementaires (DORA, NIS2, RGPD)
- Introduit de nouveaux sous-traitants ayant accès aux données de l'[Organisation]
- Modifie le périmètre de certification ou entraîne une caducité de certification
- Affecte les obligations contractuelles de sécurité

**Liée au service** :

- Modifie sensiblement l'architecture de service ou la pile technologique
- Modifie la disponibilité, les performances ou la capacité du service
- Modifie les engagements SLA ou introduit de nouvelles dépendances
- Affecte les capacités de continuité d'activité ou de reprise après sinistre

**Liée à l'entreprise** :

- Modifie la propriété ou le contrôle de l'entité fournisseur
- Déclenche des clauses de changement de contrôle dans le contrat
- Affecte la capacité du fournisseur à exécuter ses obligations contractuelles

---

# Gouvernance des relations

## Structure de gouvernance par niveau de fournisseur

| Niveau de fournisseur | Modèle de gouvernance | Fréquence des réunions | Participants |
|----------------------|----------------------|------------------------|-------------|
| **Niveau 1 (Critique)** | Comité de gouvernance formel avec charte documentée | Trimestrielle | L'[Organisation] : Propriétaire métier, RSI, IT ; Fournisseur : Responsable de compte, Responsable technique, Sécurité |
| **Niveau 2 (Élevé)** | Bilans métier réguliers avec volet sécurité | Semestrielle | L'[Organisation] : Propriétaire métier, RSI ; Fournisseur : Responsable de compte |
| **Niveau 3 (Moyen)** | Points réguliers selon les besoins | Annuelle | L'[Organisation] : Propriétaire métier ; Fournisseur : Responsable de compte |
| **Niveau 4 (Faible)** | Relation transactionnelle | Selon les besoins | Par transaction |

## Ordre du jour type — Réunion de gouvernance trimestrielle (Niveau 1)

| Point à l'ordre du jour | Animé par | Durée allouée |
|------------------------|-----------|---------------|
| **Bilan des performances** | Propriétaire métier | 15 minutes |
| **Conformité SLA et qualité de service** | Opérations IT | 15 minutes |
| **Mise à jour de la posture de sécurité** | RSI | 20 minutes |
| **Revue des incidents** (le cas échéant) | RSI / Propriétaire métier | 10 minutes |
| **Demandes de modification et feuille de route** | Fournisseur | 15 minutes |
| **Statut de conformité** (certifications, audits) | RSI | 10 minutes |
| **Problèmes, risques et escalades** | Propriétaire métier | 15 minutes |
| **Revue des actions** | Tous | 10 minutes |

**Documentation des réunions** : Les comptes rendus doivent être rédigés incluant les décisions prises, les actions avec responsables et échéances, et les escalades.

## Procédures d'escalade

| Type de problème | Escalade niveau 1 | Escalade niveau 2 | Escalade niveau 3 |
|-----------------|-------------------|-------------------|-------------------|
| **Dégradation de service** | Propriétaire métier | Direction IT | DSI |
| **Problème de sécurité** | RSI | RSSI | Direction générale |
| **Violation de conformité** | RSI | RSSI + Juridique | Direction générale |
| **Litige contractuel** | Achats | Juridique | Direction générale |
| **Dégradation de la relation** | Propriétaire métier | DSI/RSSI | Direction générale |
| **Problème financier** (litiges de facturation) | Propriétaire métier | Finance | DAF |

**Documentation des escalades** : Toutes les escalades doivent être documentées avec la description du problème, le chemin d'escalade emprunté, la résolution et le calendrier.

---

# Revue des incidents

## Catégories d'incidents fournisseurs

| Catégorie | Exemples | Indicateurs de gravité |
|-----------|----------|----------------------|
| **Incidents de sécurité** | Violation de données, accès non autorisé, infection par maliciel, compromission d'identifiants | Exposition de données, compromission de systèmes, obligation de notification réglementaire |
| **Incidents de service** | Panne non planifiée, dégradation significative, perte de données, corruption | Durée, impact utilisateur, gravité de la violation SLA |
| **Incidents de conformité** | Perte de certification, violation réglementaire, échec d'audit | Impact réglementaire, violation contractuelle, risque de réputation |
| **Incidents de chaîne d'approvisionnement** | Violation d'un sous-traitant, vulnérabilité logicielle (de type Log4Shell), compromission de dépendance | Impact en cascade, exposition étendue, complexité de la correction |
| **Quasi-incidents** | Incidents potentiels évités, situations critiques évitées de peu | Opportunité d'apprentissage, validation des contrôles |

## Processus de revue des incidents

| Étape | Activité | Délai | Responsable |
|-------|----------|-------|-------------|
| **1. Notification** | Recevoir la notification d'incident du fournisseur conformément aux conditions contractuelles | Selon le SLA (4-48 heures) | Fournisseur → RSI |
| **2. Enregistrement** | Enregistrer l'incident dans le registre des incidents fournisseurs avec évaluation initiale | Sous 4 heures | RSI |
| **3. Évaluation de l'impact** | Évaluer l'impact sur l'[Organisation] (données, systèmes, conformité, activité) | Sous 24 heures | RSI + Propriétaire métier |
| **4. Vérification du confinement** | Vérifier que le fournisseur a contenu l'incident, évaluer le risque résiduel | Sous 48 heures | RSI |
| **5. Analyse des causes racines** | Demander et examiner l'ACR du fournisseur | Sous 30 jours | Fournisseur fournit, RSI examine |
| **6. Revue de la correction** | Examiner les mesures correctives et préventives du fournisseur | Sous 60 jours | RSI |
| **7. Réévaluation des risques** | Mettre à jour l'évaluation des risques si l'incident révèle une faiblesse des contrôles | Sous 30 jours après clôture | RSI |
| **8. Retours d'expérience** | Documenter les enseignements tirés, mettre à jour les politiques/procédures si nécessaire | Sous 90 jours | RSI + IT |
| **9. Revue contractuelle** | Évaluer la conformité contractuelle (ponctualité de la notification, coopération) | Post-incident | Juridique + RSI |

## Exigences post-incident par niveau de fournisseur

| Niveau de fournisseur | Documentation post-incident requise |
|----------------------|-------------------------------------|
| **Niveau 1** | Analyse complète des causes racines, chronologie détaillée, plan de correction complet, preuves de vérification, document de retours d'expérience, expertise forensique tierce (en cas de violation) |
| **Niveau 2** | Synthèse de l'analyse des causes racines, confirmation de la correction, chronologie générale, principaux constats et mesures correctives |
| **Niveau 3** | Synthèse de l'incident, confirmation de la résolution, mesures correctives de base |
| **Niveau 4** | Notification de l'incident et confirmation de clôture |

**Révisions déclenchées par un incident** : Les incidents de sécurité doivent déclencher :

- Réévaluation immédiate de la sécurité si gravité Critique ou Élevée
- Révision de la conformité contractuelle (délais de notification, obligations de coopération)
- Possible reclassification du niveau de risque du fournisseur
- Examen des droits de résiliation en cas de violation significative

---

# Documentation et reporting

## Documentation requise

| Type de document | Déclencheur de mise à jour | Durée de conservation | Lieu de stockage |
|-----------------|---------------------------|----------------------|-----------------|
| **Registre des fournisseurs** | À chaque modification | Actuel + 3 ans | Système de gestion des fournisseurs |
| **Rapports d'évaluation** | Selon le calendrier ou déclencheur | 5 ans | Système de gestion documentaire |
| **Comptes rendus de réunion** | Après chaque réunion de gouvernance | 3 ans | Dossier fournisseur |
| **Dossiers d'incidents** | À chaque occurrence | 5 ans | Système de gestion des incidents |
| **Dossiers de modifications** | À chaque demande de modification | 3 ans | Système de gestion des modifications |
| **Rapports SLA** | Selon la périodicité (mensuelle/trimestrielle) | 3 ans | Système de surveillance des performances |
| **Certificats de conformité** | À la réception/renouvellement | Actuel + 2 ans | Référentiel de conformité |
| **Constats d'audit** | À chaque évaluation | Jusqu'à clôture + 3 ans | Système de gestion des fournisseurs |

## Reporting à la direction

| Rapport | Fréquence | Destinataires | Contenu |
|---------|-----------|---------------|---------|
| **Synthèse des risques fournisseurs** | Trimestrielle | RSSI, DSI, Direction | Panorama des risques fournisseurs, fournisseurs à risque élevé, tendances |
| **Statut des fournisseurs critiques** | Mensuelle | RSI, Propriétaires métier | Performances niveau 1, problèmes, modifications |
| **Synthèse des incidents** | Trimestrielle | RSSI, Conformité | Incidents de sécurité fournisseurs, impact, statut des corrections |
| **Statut de conformité** | Trimestrielle | RSI, Conformité | Validité des certifications, constats de conformité, écarts |
| **Tableau de bord des performances** | Continue | Propriétaires métier, IT | Conformité SLA, qualité de service, disponibilité |
| **Revue annuelle des fournisseurs** | Annuelle | Direction générale | Révision complète du portefeuille fournisseurs, recommandations stratégiques |

## Reporting réglementaire (le cas échéant)

**Services couverts par DORA** :

- Maintenir un registre des risques ICT tiers avec mises à jour trimestrielles
- Signaler les modifications significatives des arrangements ICT tiers à l'autorité compétente
- Documenter les évaluations du risque de concentration annuellement

**Services couverts par NIS2** :

- Inclure les incidents fournisseurs dans le reporting d'incident réglementaire (alerte précoce sous 24 heures)
- Documenter les mesures de sécurité de la chaîne d'approvisionnement dans le rapport annuel de cybersécurité
- Conserver les preuves des exigences de sécurité fournisseurs et de leur vérification

---

# Références

| Document | Relation |
|----------|---------|
| **ISMS-POL-A.5.19-23** | Cadre de politique parentale |
| **ISMS-POL-A.5.19-23-S1** | La classification des fournisseurs détermine la fréquence de surveillance |
| **ISMS-POL-A.5.19-23-S2** | Conditions contractuelles faisant l'objet d'un suivi de conformité |
| **ISMS-POL-A.5.19-23-S3** | Exigences de surveillance des sous-traitants |
| **ISMS-IMP-A.5.19-23.S4-UG/TG** | Cahier d'évaluation de la gouvernance opérationnelle |
| **ISO/IEC 27036-4:2016** | Sécurité de l'information pour les relations fournisseurs — Services en nuage |

---

**Document suivant :** ISMS-POL-A.5.19-23-S5 — Sécurité des services en nuage (Contrôle A.5.23)

---

*« Surveiller sans agir, c'est de l'observation coûteuse. Agir sans surveiller, c'est une confiance aveugle. »*
<!-- QA_VERIFIED: 2026-03-30 -->
