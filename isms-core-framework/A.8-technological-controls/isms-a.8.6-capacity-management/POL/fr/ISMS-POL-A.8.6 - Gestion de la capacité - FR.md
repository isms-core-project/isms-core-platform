<!-- ISMS-CORE:POLICY:ISMS-POL-A.8.6-FR:framework:POL:a.8.6 -->
**ISMS-POL-A.8.6 – Gestion de la capacité**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Politique de gestion de la capacité |
| **Type de document** | Politique |
| **Identifiant du document** | ISMS-POL-A.8.6 |
| **Créateur du document** | Responsable de la Sécurité des Systèmes d'Information (RSSI) |
| **Propriétaire du document** | Directeur général (DG) |
| **Approuvé par** | Direction générale |
| **Date de création** | [Date] |
| **Version** | 1.0 |
| **Date de version** | [Date à définir] |
| **Classification** | Interne |
| **Statut** | Brouillon |

**Historique des versions** :

| Version | Date | Auteur | Modifications |
|---------|------|--------|---------------|
| 1.0 | [Date] | RSSI / Responsable de la sécurité de l'information | Politique initiale pour la certification ISO 27001:2022 |

**Cycle de révision** : Annuel (aligné sur le cycle de planification de la capacité)
**Prochaine date de révision** : [Date d'entrée en vigueur + 12 mois]

**Chaîne d'approbation** :

- Principale : Responsable de la Sécurité des Systèmes d'Information (RSSI)
- Revue technique : Responsable des opérations IT / Responsable de l'infrastructure
- Revue financière : Directeur financier (DF)
- Autorité finale : Directeur des Systèmes d'Information (DSI)

**Documents connexes** :

- ISMS-POL-00 (Cadre d'applicabilité réglementaire)
- ISMS-IMP-A.8.6.1-UG/TG (Mise en œuvre de la surveillance de la capacité)
- ISMS-IMP-A.8.6.2-UG/TG (Prévision et planification de la capacité)
- ISMS-IMP-A.8.6.3-UG/TG (Évaluation de la gestion de la capacité)
- ISO/IEC 27001:2022 Contrôle A.8.6

---

# Résumé exécutif

Cette politique établit les exigences de [Organisation] en matière de gestion de la capacité pour assurer une infrastructure et une capacité applicative suffisantes, conformément au Contrôle A.8.6 de la norme ISO/IEC 27001:2022.

**Objet** : Définir les exigences organisationnelles pour la gouvernance de la gestion de la capacité. Cette politique établit QUELS contrôles de gestion de la capacité sont requis, QUAND la planification de la capacité doit avoir lieu et QUI en est responsable. Les procédures de mise en œuvre (COMMENT la surveillance, la prévision et la planification sont réalisées) sont documentées dans la série ISMS-IMP-A.8.6.

**Alignement réglementaire** : Cette politique traite des exigences de conformité obligatoires conformément à ISMS-POL-00, notamment le Contrôle A.8.6 de la norme ISO/IEC 27001:2022. Les exigences sectorielles conditionnelles (FINMA Circulaire 2023/1, DORA Article 11, NIS2 Article 21) s'appliquent lorsque les activités métier de [Organisation] déclenchent leur applicabilité.

---

# Périmètre

## Applicabilité

**Cette politique s'applique à** :

**Ressources d'infrastructure** :

- Capacité de calcul (serveurs, machines virtuelles, conteneurs, instances cloud)
- Capacité de stockage (espace disque, stockage de bases de données, stockage de sauvegarde, stockage d'archivage)
- Capacité réseau (bande passante, débit, connexions, capacité des équilibreurs de charge)
- Capacité applicative (utilisateurs simultanés, taux de transactions, limites de débit des API)
- Capacité cloud (quotas et limites des services cloud, nombre d'instances)
- Infrastructure physique (capacité électrique, capacité de refroidissement, espace en rack conformément à A.7.11)

**Couverture** :

- Toute l'infrastructure soutenant les opérations métier de production (obligatoire)
- Environnements de développement, de test et d'assurance qualité (recommandé)
- Sites de continuité des activités et de reprise après sinistre (conformément à A.5.30)
- Infrastructure hébergée par des tiers (lorsque [Organisation] a la responsabilité de la gestion de la capacité)

**Personnel** :

- Direction générale (approbation du budget de planification de la capacité)
- Équipe de planification de la capacité (surveillance, prévision, planification, reporting)
- Équipe des opérations IT (surveillance quotidienne, réponse aux alertes)
- Propriétaires d'applications/systèmes (projections de croissance métier)
- Directeur financier (DF) (approbation du budget de capacité)

**Hors périmètre** :

- Optimisation des performances applicatives (couverte par l'optimisation des applications)
- Gestion des licences logicielles (couverte par la gestion des actifs)

## Alignement sur le Contrôle ISO/IEC 27001:2022

**Norme ISO/IEC 27001:2022 Annexe A.8.6 — Gestion de la capacité**

> *L'utilisation des ressources devrait être surveillée et ajustée, et des projections des besoins futurs en capacité devraient être effectuées pour garantir les performances requises du système et informer les décisions d'investissement.*

**Objectif du contrôle** : Assurer des ressources adéquates pour répondre aux exigences actuelles et futures de performance et de disponibilité par la surveillance, l'ajustement et la projection.

## Intégration de la politique

Ce contrôle s'intègre avec :

- **A.8.16 — Activités de surveillance** : métriques de capacité comme sous-ensemble de la surveillance globale
- **A.8.14 — Redondance** : planification de la capacité pour les scénarios de basculement
- **A.8.13 — Sauvegarde des informations** : planification de la capacité de stockage des sauvegardes
- **A.7.11 — Services généraux** : capacité de l'infrastructure physique (alimentation, refroidissement)
- **A.5.30 — Disponibilité des TIC pour la continuité des activités** : capacité du site de reprise

---

# Énoncés de politique

## Exigences de surveillance de la capacité

[Organisation] DOIT mettre en œuvre une surveillance de la capacité pour toutes les ressources d'infrastructure et applicatives soutenant les opérations métier, avec les caractéristiques suivantes :

- **Fréquence de collecte des métriques** : au minimum toutes les 5 minutes pour les systèmes de production, toutes les 15 minutes pour les systèmes hors production
- **Complétude des données** : disponibilité des métriques à 99,5 % (hors fenêtres de maintenance planifiées)
- **Livraison des alertes** : alertes de dépassement de seuil livrées dans les 5 minutes suivant la détection
- **Vérification de la couverture** : évaluation mensuelle conformément à ISMS-IMP-A.8.6.3

**Exigences de couverture de surveillance** :

- Systèmes de production : couverture de surveillance à 100 % requise
- Systèmes hors production : couverture de surveillance à 90 % recommandée
- Infrastructure cloud : tous les services et ressources cloud surveillés
- Infrastructure réseau : bande passante, débit et connexions surveillés
- Infrastructure physique : capacité d'alimentation et de refroidissement surveillée conformément à A.7.11

**Exigences de conservation des données** :

- Métriques brutes : minimum 30 jours pour l'investigation des incidents
- Métriques agrégées : minimum 12 mois pour l'analyse des tendances
- Données historiques : minimum 36 mois pour la planification stratégique

## Exigences relatives aux seuils de capacité

[Organisation] DOIT définir et mettre en œuvre des seuils de capacité pour toutes les ressources surveillées.

**Cadre des seuils** :

- **Seuil d'avertissement** : déclenche les activités de planification de la capacité avant épuisement
- **Seuil critique** : déclenche une action immédiate pour prévenir l'épuisement
- **Capacité maximale** : limite absolue nécessitant une réponse immédiate

Les seuils DOIVENT être révisés trimestriellement et ajustés sur la base des taux de faux positifs, des incidents proches de l'épuisement et des changements dans les schémas de charge de travail.

## Exigences d'alerte de capacité

[Organisation] DOIT mettre en œuvre des alertes pour les dépassements de seuils de capacité avec :

- Acheminement vers les équipes appropriées selon la gravité
- Procédures d'escalade pour les alertes sans accusé de réception
- Intégration avec les processus de gestion des incidents

## Exigences de prévision de la capacité

[Organisation] DOIT élaborer des prévisions de capacité pour toutes les ressources d'infrastructure et applicatives critiques.

**Exigences de prévision** :

- Prévisions à court terme : 3 à 6 mois (planification tactique)
- Prévisions à moyen terme : 6 à 12 mois (planification budgétaire)
- Prévisions à long terme : 12 à 24 mois (planification stratégique)

**Fréquence de mise à jour** :

- Mensuelle : mises à jour des prévisions à court terme
- Trimestrielle : révision complète des prévisions
- Annuelle : prévisions stratégiques alignées sur le cycle budgétaire

**Cible de précision** : Prévisions dans ± 15 % de l'utilisation réelle (mesurée trimestriellement).

**Exceptions à la cible de précision** :

- Nouveaux systèmes (6 premiers mois après déploiement) : précision de ± 30 % acceptable pendant l'établissement de la référence
- Charges de travail à haute variabilité (systèmes avec variance d'utilisation > 50 %) : précision de ± 25 % avec approbation du DSI
- Maturité du programme (12 premiers mois du programme) : cible de précision de ± 20 %, resserrée à ± 15 % par la suite

**Mesure de la précision** :

- Calcul trimestriel : (Utilisation réelle - Utilisation prévue) / Utilisation prévue
- Documentation dans le classeur ISMS-IMP-A.8.6.2 avec analyse des tendances
- Analyse des causes profondes requise pour les écarts > 15 % (complétée dans les 10 jours ouvrables)

## Exigences de planification de la capacité

[Organisation] DOIT mettre en œuvre un processus structuré de planification de la capacité.

**Exigences du cycle de planification** :

- Révision mensuelle : alertes de capacité, incidents proches de l'épuisement, prévisions à court terme
- Planification trimestrielle : planification complète avec horizon de 12 mois
- Budget annuel : planification à long terme alignée sur le cycle budgétaire

**Exigences d'approbation** :

- Capacité ordinaire : DSI dans le budget approuvé
- Capacité majeure : approbation du DF pour l'impact budgétaire
- Capacité d'urgence : approbation accélérée du DSI avec notification exécutive

## Exigences de reporting de la capacité

[Organisation] DOIT produire des rapports réguliers de capacité :

- **Mensuel** : résumé de l'utilisation, incidents, points saillants des prévisions, actions
- **Trimestriel** : prévisions complètes, plans d'expansion, tableau de bord de santé
- **Annuel** : plan stratégique de capacité avec projections pluriannuelles

**Exigences de preuves de reporting** :

- Les rapports DOIVENT être générés depuis la plateforme de surveillance via les scripts Python ISMS-IMP-A.8.6
- Rapports mensuels : livrés à l'Équipe de direction IT, stockés dans la plateforme GRC/SharePoint
- Rapports trimestriels : présentés au Comité de planification de la capacité avec procès-verbal de réunion
- Rapports annuels : approuvés par le DSI, inclus dans la revue de direction (Clause 9.3 ISO 27001)

## Exigences en matière de preuves de gestion de la capacité

[Organisation] DOIT maintenir des preuves vérifiables des activités de gestion de la capacité.

**Preuves de surveillance** :

- Données de métriques : 30 jours brutes, 12 mois agrégées, 36 mois historiques
- Évaluations de couverture : mensuelles conformément à ISMS-IMP-A.8.6.3, conservées 12 mois
- Configurations des seuils : configuration actuelle avec documentation de révision trimestrielle, conservée 24 mois

**Preuves de prévision** :

- Prévisions de capacité : toutes les prévisions conservées 36 mois
- Évaluations de précision : calculs trimestriels conformément à ISMS-IMP-A.8.6.2, conservés 36 mois
- Analyses des causes profondes : écarts > 15 % documentés et conservés 24 mois

**Preuves de planification** :

- Procès-verbaux du Comité de planification de la capacité : conservés 36 mois
- Plans d'expansion : plans approuvés conservés 36 mois
- Demandes d'exception : toutes les demandes avec approbations conservées jusqu'à la remédiation + 12 mois

## Modes de défaillance de la gestion de la capacité et réponse

**Défaillances de précision des prévisions** :

- SI l'écart de précision des prévisions est > 15 % : le Responsable de l'infrastructure DOIT effectuer une analyse des causes profondes dans les 10 jours ouvrables
- L'analyse DOIT documenter : hypothèses de prévision, comparaison réel/prévu, causes de l'écart, améliorations méthodologiques
- Les conclusions DOIVENT être présentées au Comité de planification de la capacité et intégrées dans le prochain cycle de prévision
- SI l'écart est > 30 % : notification du DSI requise avec plan d'amélioration du processus

**Événements d'épuisement de la capacité** :

- SI le seuil critique de capacité est dépassé : les Opérations IT DOIVENT immédiatement mettre en œuvre les mesures d'atténuation conformément au guide de procédures
- SI un épuisement de la capacité se produit (impact sur le service) : classifié comme incident de Priorité 1 conformément à ISMS-POL-A.5.24-28 (Gestion des incidents)
- La revue post-incident DOIT inclure : pourquoi la surveillance/prévision n'a pas prévenu l'épuisement, ajustement des seuils, améliorations des processus

**Lacunes de couverture de surveillance** :

- SI la couverture de production tombe en dessous de 100 % : le Responsable de l'infrastructure DOIT créer un plan de remédiation dans les 5 jours ouvrables
- Complétion requise dans les 30 jours pour les systèmes de production, 60 jours pour les systèmes hors production
- SI la surveillance d'un système critique échoue : escalade immédiate vers le DSI + RSSI dans les 4 heures
- Remédiation d'urgence (surveillance manuelle) requise dans les 24 heures

**Intégration dans le Registre des lacunes** :

Toutes les non-conformités de gestion de la capacité DOIVENT être journalisées dans le Registre des lacunes avec :

- ID de lacune, référence au contrôle (A.8.6), description, classification des risques
- Plan d'action corrective (qui, quoi, quand), méthode de vérification
- Registre des lacunes révisé mensuellement par l'Équipe de direction IT

---

# Rôles et responsabilités

## Direction générale (PDG, Conseil)

**Responsabilités** :

- Responsabilité ultime pour une capacité adéquate soutenant les opérations métier
- Approuver les investissements majeurs en capacité et les plans stratégiques de capacité
- Assurer une allocation budgétaire adéquate pour le programme de gestion de la capacité

## Directeur des Systèmes d'Information (DSI)

**Responsabilités** :

- Responsabilité globale de l'efficacité du programme de gestion de la capacité
- S'assurer que la marge de capacité répond aux cibles organisationnelles :
  - Systèmes de production : minimum 20 % de marge à l'utilisation maximale
  - Systèmes de stockage : minimum 3 mois de marge au taux de croissance actuel
  - Bande passante réseau : minimum 30 % de marge pendant les heures de pointe
- Équilibrer les besoins en capacité avec les contraintes budgétaires

**Autorités** :

- Approuver les plans d'expansion de la capacité dans le budget
- Autoriser les achats de capacité d'urgence
- Allouer les ressources IT pour la planification de la capacité

## Responsable de la Sécurité des Systèmes d'Information (RSSI)

**Responsabilités** :

- S'assurer que les systèmes de sécurité ont une capacité suffisante (SIEM, journalisation, surveillance, EDR)
- Évaluation des risques pour les problèmes de sécurité liés à la capacité
- Vérification de la conformité des contrôles de gestion de la capacité (ISO 27001 A.8.6)

**Autorités** :

- Exiger la planification de la capacité pour les systèmes de sécurité
- Approuver la politique de gestion de la capacité
- Escalader les risques de capacité ayant un impact sur la posture de sécurité

## Équipe de planification de la capacité / Responsable de l'infrastructure

**Responsabilités** :

- Exécution quotidienne du programme de gestion de la capacité
- Surveillance, prévision et analyse des tendances de la capacité
- Planification et coordination de l'expansion de la capacité
- Reporting de la capacité à la direction

**Autorités** :

- Mettre en œuvre la surveillance de la capacité pour toutes les ressources
- Définir les seuils de capacité et les règles d'alerte
- Recommander les plans d'expansion de la capacité

## Équipe des opérations IT

**Responsabilités** :

- Surveillance quotidienne de la capacité et réponse aux alertes
- Réponse immédiate aux incidents de capacité
- Déploiement des expansions de capacité approuvées

**Autorités** :

- Exécuter les actions d'atténuation d'urgence de la capacité
- Mettre en œuvre l'ajustement et l'optimisation de la capacité approuvés
- Escalader les problèmes de capacité conformément aux procédures

## Propriétaires d'applications / Propriétaires de systèmes

**Responsabilités** :

- Fournir des projections de croissance métier pour la planification de la capacité
- Participer à la planification de la capacité pour leurs applications
- Budgétiser les besoins en capacité des applications

## Directeur financier (DF)

**Responsabilités** :

- Approuver les budgets de gestion de la capacité (CapEx et OpEx)
- Reporting financier sur les investissements en capacité
- Supervision de l'optimisation des coûts

---

# Gouvernance et conformité

## Cadre de gouvernance de la politique

**Propriétaire de la politique** : Responsable de la Sécurité des Systèmes d'Information (RSSI)
**Approbateur de la politique** : Directeur des Systèmes d'Information (DSI)
**Révision de la politique** : Révision annuelle alignée sur le cycle de planification de la capacité

**Organes de gouvernance** :

**Comité de planification de la capacité** (Opérationnel) :

- Président : Responsable de l'infrastructure ou Responsable de la planification de la capacité
- Membres principaux : Responsable des opérations IT, Propriétaires d'applications, Responsable réseau, Architecte cloud
- Représentants métier : Responsable d'unité opérationnelle ou Chef de produit (pour les projections de croissance)
- Représentant financier : Responsable financier ou Analyste budgétaire (pour la planification budgétaire)
- Fréquence : Mensuelle
- Objet : Réviser le statut de la capacité, les prévisions, planifier les expansions, aligner sur la feuille de route métier

**Équipe de direction IT** (Stratégique) :

- Membres : DSI, RSSI, DF, Directeur IT
- Fréquence : Trimestrielle
- Objet : Réviser les rapports de capacité, approuver les budgets, décisions stratégiques

## Conformité réglementaire

Cette politique satisfait aux exigences conformément à **ISMS-POL-00 (Cadre d'applicabilité réglementaire)** :

**Niveau 1 — Conformité obligatoire** :

- **ISO/IEC 27001:2022** : Contrôle A.8.6 (Gestion de la capacité)

**Niveau 2 — Applicabilité conditionnelle** (lorsque les activités métier déclenchent l'applicabilité) :

- **FINMA Circulaire 2023/1** (établissements financiers suisses) : résilience opérationnelle des TIC
- **DORA Article 11** (entités de services financiers UE) : planification de la capacité des TIC
- **NIS2 Article 21(2)** (entités essentielles/importantes) : capacité pour la continuité des activités

**Niveau 3 — Référence informative** :

- ITIL 4 Gestion de la capacité
- NIST SP 800-53 AU-6

## Exceptions à la politique

**Exceptions temporaires — Systèmes critiques** (soutenant les opérations métier essentielles) :

- Durée maximale : 3 mois
- Approuvé par : DSI + RSSI (approbation conjointe requise)
- Conditions : contrôles compensatoires requis, acceptation de risque documentée, révision hebdomadaire du statut
- Documentation : demande d'exception avec évaluation des risques, plan d'atténuation, calendrier de remédiation

**Exceptions temporaires — Systèmes non critiques** :

- Durée maximale : 6 mois
- Approuvé par : Directeur IT ou DSI
- Conditions : acceptation de risque documentée, révision mensuelle du statut
- Documentation : demande d'exception avec plan d'atténuation, calendrier de remédiation

**Exceptions permanentes** :

- Approuvé par : DSI + RSSI + Direction générale
- Documentation : acceptation formelle des risques, contrôles compensatoires
- Révision : ré-approbation annuelle requise

## Vérification de la conformité

**Auto-évaluation mensuelle** (conformément à ISMS-IMP-A.8.6.3) :

- **Réalisée par** : Responsable de l'infrastructure ou membre désigné de l'Équipe de planification de la capacité
- **Périmètre** : couverture de surveillance en %, configuration des seuils, complétude de la prévision, ponctualité du reporting
- **Résultat** : classeur généré par Python ISMS-IMP-A.8.6.3 avec résultats réussite/échec
- **Révision** : présenté au Responsable des opérations IT dans les 10 jours ouvrables suivant la fin du mois
- **Suivi** : non-conformités journalisées dans le Registre des lacunes

**Audit interne trimestriel** :

- **Réalisé par** : fonction d'audit interne ou auditeur désigné par le RSSI (indépendant de l'équipe de planification de la capacité)
- **Périmètre** : échantillon de 3 systèmes critiques, vérification de la configuration de surveillance, révision des 3 derniers mois de prévisions, entretien avec l'équipe de planification de la capacité
- **Résultat** : rapport d'audit avec constats, échantillons de preuves, recommandations
- **Révision** : présenté à l'Équipe de direction IT dans les 15 jours ouvrables suivant la fin du trimestre
- **Suivi** : non-conformités suivies dans le Registre des lacunes avec plans d'actions correctives

**Audit externe annuel** :

- **Réalisé par** : auditeur de certification ISO 27001
- **Périmètre** : évaluation complète du contrôle conformément à ISO 27001:2022 A.8.6
- **Réponse** : le RSSI DOIT coordonner la réponse, plans d'actions correctives dans les 30 jours

**Gestion des non-conformités** :

- Non-conformités mineures : le Responsable de l'infrastructure crée un plan d'actions correctives, approuvé par le RSSI, complété dans les 90 jours
- Non-conformités majeures : le DSI et le RSSI créent un plan d'actions correctives, approuvé par la Direction générale, complété dans les 30 jours

**Métriques de conformité** (rapportées mensuellement) :

- Pourcentage de couverture de surveillance (cible : 100 % production, 90 % hors production)
- Complétude de la configuration des seuils
- Couverture de la prévision pour les ressources critiques
- Ponctualité du reporting
- Nombre de non-conformités et taux de clôture

**ICP du programme de gestion de la capacité** (rapportés trimestriellement) :

| Catégorie d'ICP | Métrique | Cible |
|----------------|---------|-------|
| **Disponibilité** | Incidents liés à la capacité par trimestre | < 2 |
| **Disponibilité** | Délai moyen d'expansion de la capacité | < 30 jours à compter de l'approbation |
| **Disponibilité** | Achats de capacité d'urgence par an | < 3 |
| **Précision** | Précision des prévisions | ± 15 % |
| **Précision** | Taux de faux positifs des alertes | < 10 % |
| **Précision** | Complétude des données de surveillance | > 99 % |
| **Efficience** | Marge moyenne sur l'ensemble des systèmes | 15 – 30 % |
| **Efficience** | Utilisation moyenne aux heures de pointe | 70 – 85 % |
| **Efficience** | Écart budgétaire (réel vs. prévu) | ± 10 % |

Les ICP DOIVENT être rapportés trimestriellement à l'Équipe de direction IT et annuellement à la Direction générale.

## Conséquences de la non-conformité

**Opérationnelles** : interruptions de service, dégradation des performances, achats d'urgence.
**Financières** : dépenses non budgétées, perte de revenus, pénalités contractuelles.
**Conformité** : non-conformité ISO 27001, violations réglementaires, constats d'audit.
**Organisationnelles** : mesures de gestion des performances, escalade exécutive.

---

# Documents connexes

## Documents SMSI

**Guides de mise en œuvre** :

- ISMS-IMP-A.8.6.1 : Mise en œuvre de la surveillance de la capacité
- ISMS-IMP-A.8.6.2 : Prévision et planification de la capacité
- ISMS-IMP-A.8.6.3 : Évaluation de la gestion de la capacité

**Politiques connexes** :

- ISMS-POL-00 : Cadre d'applicabilité réglementaire
- ISMS-POL-A.8.16 : Activités de surveillance
- ISMS-POL-A.8.14 : Redondance des installations de traitement de l'information
- ISMS-POL-A.8.13 : Sauvegarde des informations
- ISMS-POL-A.7.11 : Services généraux
- ISMS-POL-A.5.30 : Disponibilité des TIC pour la continuité des activités

## Normes externes

- ISO/IEC 27001:2022 — Contrôle A.8.6
- ISO/IEC 27002:2022 — Orientations du Contrôle 8.6
- FINMA Circulaire 2023/1 (si applicable)
- DORA — Règlement (UE) 2022/2554 (si applicable)
- NIS2 — Directive (UE) 2022/2555 (si applicable)

---

# Définitions

| Terme | Définition |
|-------|------------|
| **Gestion de la capacité** | Processus visant à assurer des ressources adéquates pour répondre aux exigences actuelles et futures de performance et de disponibilité |
| **Surveillance de la capacité** | Mesure continue de l'utilisation des ressources pour comprendre la consommation et suivre les tendances |
| **Planification de la capacité** | Processus proactif de détermination des besoins futurs en capacité et d'élaboration de plans d'expansion |
| **Seuil de capacité** | Niveau d'utilisation défini qui déclenche des alertes ou des actions lorsqu'il est dépassé |
| **Prévision de capacité** | Projection des besoins futurs en capacité basée sur les tendances et les plans métier |
| **Marge** | Capacité disponible inutilisée restante pour la croissance ou la demande imprévue |

---

# Enregistrement d'approbation

| Rôle | Nom | Date |
|------|-----|------|
| **Responsable de la Sécurité des Systèmes d'Information (RSSI)** | [Nom] | [Date à définir] |
| **Directeur des Systèmes d'Information (DSI)** | [Nom] | [Date à définir] |
| **Directeur financier (DF)** | [Nom] | [Date à définir] |
| **Responsable des opérations IT** | [Nom] | [Date à définir] |

---

**FIN DU DOCUMENT DE POLITIQUE**

---

*Cette politique établit les exigences de gestion de la capacité. Les procédures de mise en œuvre sont documentées dans ISMS-IMP-A.8.6.1 (Surveillance de la capacité), ISMS-IMP-A.8.6.2 (Prévision et planification de la capacité) et ISMS-IMP-A.8.6.3 (Évaluation de la gestion de la capacité).*

<!-- QA_VERIFIED: 2026-04-02 -->
