<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.30-8.13-14-FR:framework:POL:a.5.30-8.13-14 -->
**ISMS-POL-A.5.30-8.13-14 – Cadre de continuité des activités et reprise après sinistre**

---

**Contrôle documentaire**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Cadre de continuité des activités et reprise après sinistre |
| **Type de document** | Politique |
| **Identifiant du document** | ISMS-POL-A.5.30-8.13-14 |
| **Créateur du document** | Responsable de la sécurité des systèmes d'information (RSSI) |
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
| 1.0 | [Date] | RSSI | Politique initiale pour la première certification ISO 27001:2022 |

**Cycle de révision** : Annuel
**Prochaine date de révision** : [Date d'entrée en vigueur + 12 mois]

**Chaîne d'approbation** :

- Principal : Responsable de la sécurité des systèmes d'information (RSSI)
- Secondaire : Directeur des systèmes d'information (DSI)
- Technique : Responsable des opérations informatiques / Coordinateur CA/RA
- Conformité : Responsable juridique/conformité
- Autorité finale : Direction générale

**Documents connexes** :

- ISMS-POL-00 (Cadre d'applicabilité réglementaire)
- ISMS-IMP-A.5.30-8.13-14-S1-UG/TG (Processus BIA et RPO:RTO)
- ISMS-IMP-A.5.30-8.13-14-S2-UG/TG (Mise en œuvre des sauvegardes)
- ISMS-IMP-A.5.30-8.13-14-S3-UG/TG (Mise en œuvre de la redondance)
- ISMS-IMP-A.5.30-8.13-14-S4-UG/TG (Processus de test de reprise)
- ISO/IEC 27001:2022 Contrôles A.8.13, A.8.14, A.5.30
- ISMS-POL-A.5.19-23 (Services fournisseurs/cloud – exigences CA/RA des fournisseurs)
- ISMS-POL-A.5.24 (Gestion des incidents)
- ISMS-POL-A.8.6 (Gestion de la capacité)

---

## Résumé exécutif

Cette politique établit les exigences de [Organisation] en matière de contrôles de continuité des activités et de reprise après sinistre (CA/RA) afin d'assurer la résilience organisationnelle grâce à des capacités systématiques de sauvegarde, de redondance et de continuité des TIC, conformément aux contrôles ISO/IEC 27001:2022 A.8.13, A.8.14 et A.5.30.

**Périmètre** : Cette politique s'applique à tous les actifs informationnels, systèmes TIC et processus métier, quel que soit le modèle de déploiement (sur site, cloud, hybride) ou la plateforme technologique.

**Objectif** : Définir les exigences organisationnelles pour la mise en œuvre et la gouvernance des contrôles CA/RA. Cette politique établit CE QUI est requis comme capacités de reprise et QUI en est responsable. Les procédures de mise en œuvre (COMMENT) sont documentées séparément dans ISMS-IMP-A.5.30-8.13-14 (variantes UG/TG). Les normes techniques et configurations sont intentionnellement définies en dehors de cette politique afin de préserver l'agilité technologique.

**Approche combinée des contrôles** : Ces trois contrôles sont mis en œuvre comme un cadre unifié car ils fonctionnent comme un écosystème CA/RA intégré : la sauvegarde fournit la capacité de reprise des données (A.8.13), la redondance fournit la capacité de disponibilité des systèmes (A.8.14), et la préparation à la continuité des TIC assure la préparation globale et la gouvernance (A.5.30). Une mise en œuvre séparée créerait des stratégies déconnectées où les politiques de sauvegarde ignorent l'architecture de redondance et les plans de continuité des activités ne reflètent pas les capacités techniques réelles. Malgré la mise en œuvre unifiée, chaque contrôle maintient des exigences distinctes à des fins de déclaration d'applicabilité (DdA).

**Principe fondamental — « Reprise non testée = aucune reprise »** : Ce cadre impose des tests réguliers de toutes les capacités de reprise. La réussite des sauvegardes sans test de restauration, la redondance sans test de basculement, et les plans de continuité sans test de scénario procurent une fausse confiance. La vérification fondée sur des preuves par des tests systématiques n'est pas négociable.

**Alignement réglementaire** : Cette politique répond aux exigences de conformité obligatoires conformément à ISMS-POL-00 (Cadre d'applicabilité réglementaire), incluant le nLPD suisse, le RGPD de l'UE, ISO/IEC 27001:2022, et les exigences conditionnelles pour DORA (immuabilité, sauvegarde hors site, redondance géographique), NIS2 (conformité à la règle 3-2-1, notification d'incident sous 24 heures), et les réglementations sectorielles lorsque les activités commerciales de [Organisation] déclenchent leur applicabilité.

---

# Alignement des contrôles et périmètre

## Contrôles ISO/IEC 27001:2022 A.8.13, A.8.14, A.5.30

**ISO/IEC 27001:2022 Annexe A.8.13 — Sauvegarde de l'information**

> *Des copies de sauvegarde des informations, des logiciels et des systèmes devraient être effectuées et testées régulièrement conformément à la politique thématique convenue.*

**Objectif du contrôle** : S'assurer que les informations, logiciels et systèmes peuvent être restaurés en cas de perte, d'endommagement, de corruption ou d'indisponibilité.

**Résumé des recommandations ISO/IEC 27002:2022** :

- Les copies de sauvegarde devraient être créées conformément à une politique de sauvegarde définie et documentée
- Les sauvegardes devraient inclure toutes les informations, logiciels, images système et configurations essentiels
- Les sauvegardes devraient être testées régulièrement pour s'assurer qu'elles peuvent être restaurées avec succès
- Les sauvegardes devraient être protégées au même niveau que les données originales
- Plusieurs générations de sauvegardes devraient être conservées selon les besoins métier
- Les sauvegardes devraient être stockées dans un endroit sécurisé et séparé (hors site ou hors ligne)

**ISO/IEC 27001:2022 Annexe A.8.14 — Redondance des installations de traitement de l'information**

> *Les installations de traitement de l'information devraient être mises en œuvre avec une redondance suffisante pour répondre aux exigences de disponibilité.*

**Objectif du contrôle** : S'assurer de la disponibilité des installations de traitement de l'information conformément aux exigences organisationnelles.

**Résumé des recommandations ISO/IEC 27002:2022** :

- La redondance devrait être mise en œuvre pour les installations critiques de traitement de l'information
- Le niveau de redondance est déterminé par les exigences de disponibilité
- La redondance peut inclure le matériel, les logiciels, le réseau, l'alimentation et le refroidissement
- La redondance géographique devrait être envisagée pour protéger contre les catastrophes à l'échelle d'un site
- Des mécanismes de basculement devraient être mis en œuvre et testés
- Les points de défaillance uniques (SPOF) devraient être identifiés et atténués

**ISO/IEC 27001:2022 Annexe A.5.30 — Préparation des TIC pour la continuité des activités**

> *La préparation des TIC devrait être planifiée, mise en œuvre, maintenue et testée sur la base des objectifs de continuité des activités et des exigences de continuité des TIC.*

**Objectif du contrôle** : S'assurer que les systèmes TIC sont prêts à soutenir la continuité des activités en cas de perturbation.

**Résumé des recommandations ISO/IEC 27002:2022** :

- Les plans de continuité des TIC devraient être développés sur la base d'une analyse d'impact sur les activités (AIA)
- Les plans devraient définir les objectifs de point de reprise (RPO) et les objectifs de délai de reprise (RTO)
- Les exigences de continuité des TIC devraient être alignées sur les objectifs de continuité des activités
- Les plans devraient être testés régulièrement par des exercices et des simulations
- Les dépendances entre les systèmes TIC devraient être documentées
- Les capacités de sauvegarde et de redondance devraient s'aligner sur les exigences de reprise

**Indépendance dans la déclaration d'applicabilité** : Malgré la mise en œuvre et la documentation unifiées, les contrôles A.8.13, A.8.14 et A.5.30 sont évalués indépendamment dans la déclaration d'applicabilité. Chaque contrôle maintient des exigences, une collecte de preuves et une notation de conformité distinctes à des fins d'audit.

**Cette politique traite** :

- Les exigences de sauvegarde de l'information (A.8.13)
- Les exigences de redondance et de basculement (A.8.14)
- Les exigences de préparation à la continuité des activités des TIC (A.5.30)
- Le cadre de test et de validation de la reprise
- Les rôles et responsabilités organisationnels pour la gouvernance CA/RA
- Les cadres de gestion des exceptions et des incidents
- L'intégration avec les processus d'évaluation et de traitement des risques de [Organisation]

## Ce que fait cette politique

Cette politique :

- **Définit** les exigences de sauvegarde, de redondance et de continuité des TIC alignées sur l'évaluation des risques organisationnels
- **Établit** un cadre de gouvernance pour la prise de décision CA/RA
- **Spécifie** la responsabilité pour la mise en œuvre des capacités CA/RA
- **Référence** les exigences réglementaires applicables conformément à ISMS-POL-00
- **Intègre** trois contrôles connexes dans un cadre CA/RA unifié pour l'efficacité de la mise en œuvre
- **Exige** des tests systématiques des capacités de reprise comme preuve de préparation

## Ce que cette politique ne fait PAS

Cette politique ne :

- **Spécifie pas les détails d'implémentation technique** (voir ISMS-IMP-A.5.30-8.13-14 Guides de mise en œuvre)
- **Ne définit pas les technologies ou solutions de sauvegarde** (voir ISMS-IMP-A.5.30-8.13-14-S2 Mise en œuvre des sauvegardes)
- **Ne fournit pas de conceptions d'architecture de redondance** (voir ISMS-IMP-A.5.30-8.13-14-S3 Mise en œuvre de la redondance)
- **Ne documente pas les procédures de reprise** (voir ISMS-IMP-A.5.30-8.13-14-S4 Processus de test de reprise)
- **Ne sélectionne pas les fournisseurs de sauvegarde ou de reprise après sinistre** (sélection technologique basée sur l'évaluation des risques de [Organisation])
- **Ne définit pas de valeurs RPO/RTO spécifiques** (pilotées par les métiers, documentées dans l'AIA conformément à ISMS-IMP-A.5.30-8.13-14-S1)

**Justification** : Séparer les exigences de politique des conseils de mise en œuvre permet :

- La stabilité de la politique malgré l'évolution des technologies CA/RA (reprise cloud, sauvegardes immuables, réplication continue)
- L'agilité technique pour les mises à jour technologiques sans révision de politique
- Une distinction claire entre gouvernance (politique) et exécution (mise en œuvre)
- Une approche indépendante de la technologie applicable à toute infrastructure (sur site, cloud, hybride)

## Périmètre

**Cette politique s'applique à** :

**Actifs informationnels** (A.8.13) :

- Données critiques pour les activités (clients, finances, propriété intellectuelle, opérations)
- Configurations système et infrastructure-as-code
- Logiciels d'application et dépendances
- Configurations de sécurité et contrôles d'accès
- Toutes les classifications de données (Restreint, Confidentiel, Interne, Public)

**Installations de traitement de l'information** (A.8.14) :

- Serveurs sur site (physiques et virtuels)
- Infrastructure cloud (IaaS, PaaS, SaaS)
- Environnements hybrides (intégration sur site + cloud)
- Infrastructure réseau (routeurs, commutateurs, pare-feux, équilibreurs de charge)
- Systèmes de stockage (SAN, NAS, stockage objet, bases de données)
- Systèmes d'utilisateurs finaux critiques (lorsque critiques pour les activités)

**Processus métier** (A.5.30) :

- Tous les processus métier dépendants des TIC identifiés par l'analyse d'impact sur les activités
- Fonctions métier critiques et processus de support
- Services tiers et dépendances

**Systèmes et services TIC** (A.5.30) :

- Tous les systèmes TIC soutenant les opérations métier
- Applications métier critiques
- Services d'infrastructure (annuaire, messagerie, collaboration)
- Systèmes de sécurité (SIEM, IAM, protection des endpoints)
- Services réseau (DNS, DHCP, VPN)
- Services cloud et plateformes SaaS

**Modèles de déploiement d'infrastructure** :

- Infrastructure sur site (centres de données, bureaux)
- Infrastructure cloud (IaaS : AWS EC2, Azure VMs, GCP Compute)
- Plateformes cloud (PaaS : AWS RDS, Azure SQL, GCP Cloud Functions)
- Applications cloud (SaaS : Office 365, Salesforce, ServiceNow)
- Architectures hybrides (intégration sur site + cloud)
- Environnements multi-cloud (plusieurs fournisseurs cloud)

**Scénarios de direction de reprise** :

- Sur site vers sur site (reprise après sinistre traditionnelle)
- Sur site vers cloud (cloud comme cible de reprise après sinistre)
- Cloud vers sur site (rapatriement cloud, scénarios de panne prolongée)
- Cloud vers cloud alternatif (portabilité multi-cloud)
- Basculement géographique (région à région chez le même fournisseur)

**Personnel** :

- Coordinateur CA/RA, administrateurs de sauvegarde, administrateurs système
- Administrateurs cloud, propriétaires d'applications, administrateurs de bases de données
- Équipe de continuité des activités, équipe de gestion de crise
- Tous les employés (sensibilisation CA/RA et responsabilités)

**Cette politique ne s'applique PAS à** :

- Les dossiers physiques et informations non numériques (couverts par les contrôles de sécurité physique)
- La continuité des activités pour les fonctions non-TIC (couverte par le cadre BCM organisationnel)
- La réponse aux incidents de sécurité de l'information (couverte par A.5.24-27, bien que CA/RA soit invoqué lors d'incidents majeurs)

**Périmètre des environnements cloud** :

Cette politique s'applique à tous les environnements cloud utilisés par [Organisation], quel que soit le fournisseur ou le modèle de service (IaaS/PaaS/SaaS). La liste officielle des environnements cloud dans le périmètre est maintenue dans :

- **Inventaire des sauvegardes (Classeur 1)** : Toutes les charges de travail cloud nécessitant une protection par sauvegarde, y compris les instances IaaS, les bases de données PaaS et les données d'applications SaaS
- **Analyse de redondance (Classeur 2)** : Infrastructure cloud mettant en œuvre les exigences de redondance (déploiements multi-AZ, multi-région, multi-cloud)
- **Inventaire des actifs (ISMS-POL-A.5.9)** : Inventaire complet des actifs informationnels incluant les ressources cloud, organisé par classification de criticité

Les références à des fournisseurs cloud spécifiques (AWS, Azure, GCP) dans cette politique sont illustratives des concepts et architectures CA/RA cloud. Les fournisseurs cloud réels, services et modèles de déploiement dans le périmètre sont déterminés par le déploiement d'infrastructure actuel de [Organisation] tel que documenté dans les inventaires ci-dessus.

**Gestion des changements de fournisseurs cloud** : L'ajout de nouveaux fournisseurs ou services cloud nécessite la mise en œuvre des capacités CA/RA (configuration de sauvegarde, architecture de redondance, test de reprise) avant le déploiement en production conformément à la Section 8.1 (Planification et contrôle opérationnels). Les mises à jour de l'inventaire des fournisseurs cloud ne nécessitent pas de révision de politique mais DOIVENT être reflétées dans les inventaires CA/RA dans les 30 jours suivant le déploiement en production.

**Considérations multi-cloud et hybrides** : Lorsque [Organisation] exploite des architectures multi-cloud (plusieurs fournisseurs) ou hybrides (sur site + cloud), les exigences CA/RA s'appliquent de manière cohérente à tous les modèles de déploiement. Les scénarios de reprise DOIVENT inclure :
- Basculement cloud-to-cloud (région cloud principale vers région secondaire ou fournisseur alternatif)
- Reprise cloud-to-on-premises (pour les pannes prolongées de fournisseur cloud)
- Reprise on-premises-to-cloud (cloud comme cible de reprise après sinistre)

Les capacités de reprise inter-plateformes DOIVENT être documentées dans les procédures de reprise (ISMS-IMP-A.5.30-8.13-14-S2, S3) et validées par des tests annuels conformément à la Section 2.3.4.

## Applicabilité réglementaire

Cette politique met en œuvre les exigences CA/RA pour se conformer aux réglementations conformément à **ISMS-POL-00 (Cadre d'applicabilité réglementaire)** :

**Niveau 1 : Conformité obligatoire**

| Réglementation | Exigence | Applicabilité |
|----------------|----------|---------------|
| **nLPD suisse (Loi fédérale sur la protection des données)** | Mesures techniques et organisationnelles appropriées incluant la protection de la disponibilité (art. 8) | Tout traitement de données personnelles par [Organisation] |
| **RGPD de l'UE** | Capacité à restaurer la disponibilité et l'accès aux données personnelles en temps voulu (art. 32(1)(c)) | Lors du traitement de données personnelles de l'UE |
| **ISO/IEC 27001:2022** | Contrôles A.8.13, A.8.14, A.5.30 | Périmètre de certification |

**Niveau 2 : Applicabilité conditionnelle**

| Réglementation | Exigence | Condition déclencheuse |
|----------------|----------|------------------------|
| **DORA (Digital Operational Resilience Act)** | Politique de continuité des activités TIC, politiques de sauvegarde, plans de reprise après sinistre, tests (art. 11-12) | Opérations de services financiers dans l'UE |
| **Directive NIS2** | Mesures de continuité des activités et de gestion de crise, gestion des sauvegardes (art. 21) | Désignation d'entité essentielle/importante |
| **FINMA** | Gestion de la continuité des activités pour les institutions financières | Opérations de services financiers suisses |
| **PCI DSS v4.0.1** | Sauvegarde et conservation des données (Req. 12.10), test de sauvegarde/reprise (Req. 12.10.7) | Traitement des données de cartes de paiement |

**Niveau 3 : Orientation informative**

Cadres de bonnes pratiques référencés mais non obligatoires :

- ISO/IEC 22301 (Management de la continuité des activités)
- NIST SP 800-34 (Planification de contingence)
- ISO/IEC 27031 (Préparation des TIC pour la continuité des activités)
- ITIL Gestion de la continuité des services

**Exigences spécifiques DORA** : Pour les entités financières de l'UE soumises à DORA, les exigences supplémentaires suivantes s'appliquent :

- Copies de sauvegarde immuables lorsque techniquement réalisable (art. 12(4))
- Stockage de sauvegarde hors site à une distance géographique suffisante (art. 12(4))
- Test annuel de reprise des sauvegardes (art. 12(6))
- Tests CA/RA intégrés avec les tests de pénétration pilotés par les menaces (art. 26)

**Exigences spécifiques NIS2** : Pour les entités essentielles/importantes soumises à NIS2 :

- Mise en œuvre de la règle de sauvegarde 3-2-1 (3 copies, 2 types de supports, 1 hors site)
- Chiffrement des sauvegardes en transit et au repos
- Capacité de notification d'incident sous 24 heures pour les événements CA/RA

**Détermination de conformité** : Le Responsable juridique/conformité détermine l'applicabilité des réglementations de Niveau 2 en fonction des activités commerciales et du statut réglementaire de [Organisation].

---

# Cadre des exigences

## Exigences de sauvegarde de l'information (A.8.13)

[Organisation] met en œuvre des capacités de sauvegarde de l'information pour permettre la reprise après perte de données, corruption ou défaillance système.

### Exigences de périmètre de sauvegarde

**Systèmes et données nécessitant une sauvegarde** :

| Catégorie | Exigence de sauvegarde | Justification |
|-----------|------------------------|---------------|
| **Données métier critiques** | Sauvegarde obligatoire | La perte de données aurait un impact sévère sur les opérations |
| **Systèmes de production** | Sauvegarde obligatoire (données + configuration) | Requis pour la continuité des activités |
| **Configurations d'infrastructure critiques** | Sauvegarde obligatoire | Requis pour la reprise de l'infrastructure |
| **Données métier importantes** | Sauvegarde obligatoire | La perte de données aurait un impact modéré sur les opérations |
| **Systèmes de développement/test** | Sauvegarde basée sur les risques | Sauvegarder si le coût de recréation dépasse le coût de sauvegarde |
| **Données éphémères** | Aucune sauvegarde requise | Données délibérément temporaires (caches, journaux avec rétention) |
| **Systèmes non critiques** | Sauvegarde basée sur les risques | Sauvegarder si le délai de restauration est inacceptable |

**Détermination du périmètre de sauvegarde** : Les propriétaires de systèmes, en consultation avec le Coordinateur CA/RA, déterminent les exigences de sauvegarde sur la base de :

- Résultats de l'analyse d'impact sur les activités (AIA)
- Classification de la criticité des données (conformément à ISMS-POL-A.5.12)
- Exigences réglementaires de rétention
- Objectifs de délai de reprise du système (RTO)
- Analyse de la complexité de reconstruction par rapport au coût de sauvegarde

### Exigences de calendrier de sauvegarde

**Fréquence de sauvegarde par criticité du système** :

| Niveau système | Fréquence de sauvegarde | Cible RPO | Justification |
|----------------|-------------------------|-----------|---------------|
| **Niveau 1 (Critique)** | Continue ou toutes les heures | ≤ 1 heure | Perte de données minimale acceptable |
| **Niveau 2 (Élevé)** | Toutes les 4 à 6 heures | ≤ 6 heures | Perte de données limitée acceptable |
| **Niveau 3 (Moyen)** | Quotidienne | ≤ 24 heures | Perte de données journalière acceptable |
| **Niveau 4 (Faible)** | Hebdomadaire ou sur modification | ≤ 7 jours | Perte de données hebdomadaire acceptable |

**Fenêtre de sauvegarde** : Les sauvegardes DOIVENT se terminer dans les fenêtres de maintenance définies. Si la durée de sauvegarde dépasse la fenêtre disponible, des stratégies incrémentales/différentielles ou une protection continue des données DOIVENT être mises en œuvre.

### Exigences RPO par criticité

**Cadre d'objectif de point de reprise (RPO)** :

Le RPO définit l'âge maximum acceptable des données pouvant être récupérées. Le RPO pilote les exigences de fréquence de sauvegarde.

| Criticité du système | RPO maximum | Stratégie de sauvegarde | Exemples de technologies |
|----------------------|-------------|-------------------------|--------------------------|
| **Niveau 1 (Critique)** | 1 heure ou moins | Réplication continue ou sauvegardes horaires | CDP, réplication temps réel, snapshots horaires |
| **Niveau 2 (Élevé)** | 4 à 6 heures | Plusieurs sauvegardes quotidiennes | 4 sauvegardes/jour, snapshots périodiques |
| **Niveau 3 (Moyen)** | 24 heures | Sauvegardes quotidiennes | Complètes ou incrémentales nocturnes |
| **Niveau 4 (Faible)** | 7 jours | Sauvegardes hebdomadaires | Sauvegardes complètes hebdomadaires |

**Calcul du RPO** : Les propriétaires de systèmes DOIVENT documenter les exigences RPO sur la base de :

- Perte de données maximale acceptable mesurée en temps (heures/jours)
- Impact métier de la perte de X heures de transactions
- Exigences de reconstitution des données réglementaires
- Coût de l'infrastructure de sauvegarde par rapport au coût de la perte de données

**Exceptions RPO** : Les systèmes incapables de respecter le RPO défini DOIVENT suivre le processus de gestion des exceptions (Section 3.2).

### Exigences de technologie de sauvegarde

**Types de sauvegarde** :

| Type de sauvegarde | Description | Cas d'usage | Avantages | Inconvénients |
|--------------------|-------------|-------------|-----------|---------------|
| **Sauvegarde complète** | Copie complète de toutes les données | Référence, hebdomadaire/mensuelle | Reprise la plus simple | Intensive en temps/stockage |
| **Incrémentale** | Données modifiées depuis la dernière sauvegarde (tout type) | Sauvegardes quotidiennes | Rapide, stockage efficace | Reprise plus lente (tous incréments nécessaires) |
| **Différentielle** | Données modifiées depuis la dernière sauvegarde complète | Sauvegardes quotidiennes | Reprise plus rapide qu'incrémentale | Plus de stockage qu'incrémentale |
| **Snapshot** | Copie ponctuelle (niveau stockage) | Sauvegardes fréquentes, VMs | Très rapide, économe en espace | Dépendant du stockage, non portable |
| **Protection continue des données (CDP)** | Réplication temps réel ou quasi temps réel | Systèmes critiques (RPO < 1 heure) | Perte de données minimale | Complexe, coûteux |

**Sélection de la stratégie de sauvegarde** : Les propriétaires de systèmes DOIVENT sélectionner la technologie de sauvegarde appropriée selon :

- Exigences RPO et RTO
- Architecture système (physique, virtuel, cloud, base de données)
- Taux de modification des données (quantité de données modifiées quotidiennement)
- Fenêtre de sauvegarde disponible
- Contraintes de capacité et de coût de stockage

**Exigences de rétention des sauvegardes** :

Les sauvegardes DOIVENT être conservées selon les périodes de rétention minimales suivantes :

| Type de sauvegarde | Rétention minimale | Considérations réglementaires |
|--------------------|--------------------|-------------------------------|
| **Sauvegardes quotidiennes** | 30 jours | La plupart des réglementations exigent une capacité de reprise de 30 jours |
| **Sauvegardes hebdomadaires** | 90 jours | Conformité trimestrielle et besoins d'audit |
| **Sauvegardes mensuelles** | 12 mois | Vérification annuelle de conformité et analyse historique |
| **Sauvegardes annuelles** | 7 ans (ou selon réglementation) | Dossiers financiers, conformité fiscale, conservations légales |

**Rétention étendue** : Des exigences de rétention supplémentaires peuvent s'appliquer selon :

- Exigences réglementaires (RGPD, FINMA, PCI DSS v4.0.1, droit fiscal)
- Demandes de conservation légale
- Obligations contractuelles
- Besoins métier (analyses historiques, audits de conformité)

**Exceptions à la politique de rétention** : Des périodes de rétention plus courtes nécessitent l'approbation du RSSI et une acceptation documentée du risque.

### Règle de sauvegarde 3-2-1-1-0 (meilleure pratique sectorielle)

**Définition de la règle 3-2-1-1-0** :

| Élément | Exigence | Justification |
|---------|----------|---------------|
| **3 copies** | Original + 2 copies de sauvegarde | Protection contre les points de défaillance uniques |
| **2 types de supports** | Technologies de stockage différentes | Protection contre les défaillances spécifiques aux supports |
| **1 copie hors site** | Emplacement géographiquement séparé | Protection contre les catastrophes locales |
| **1 immuable/isolée** | WORM ou hors ligne | Protection contre les rançongiciels et les menaces internes |
| **0 erreurs** | Intégrité de sauvegarde vérifiée | Seules les sauvegardes vérifiées sont fiables |

**Mise en œuvre pour les systèmes critiques** (Niveau 1) :

Les systèmes critiques (Niveau 1) DOIVENT mettre en œuvre la règle 3-2-1-1-0 :

- **3 copies** : Données de production + sauvegarde sur site + sauvegarde cloud/hors site
- **2 types de supports** : Disque + bande/stockage objet, ou sur site + cloud
- **1 hors site** : Séparation géographique (centre de données différent, région ou cloud)
- **1 immuable** : Stockage WORM, verrouillage d'objet (S3), ou bande isolée
- **0 erreurs** : Vérification automatisée des sauvegardes, test de restauration périodique

**Mise en œuvre pour les systèmes élevés/moyens** (Niveaux 2-3) :

Les systèmes élevés et moyens DEVRAIENT mettre en œuvre au minimum 3-2-1 :

- **3 copies** : Production + sauvegarde principale + sauvegarde secondaire
- **2 types de supports** : Technologies différentes (disque + cloud, disque + bande)
- **1 hors site** : Sauvegarde cloud ou centre de données distant

**Justification** : La règle 3-2-1-1-0 fournit une défense en profondeur contre plusieurs scénarios de défaillance : défaillance matérielle, rançongiciel, catastrophes naturelles, erreur humaine et corruption des données.

### Exigences de hors-site et d'immuabilité

**Exigences de sauvegarde hors site** :

| Niveau système | Exigence hors site | Séparation géographique | Fréquence de réplication |
|----------------|--------------------|-------------------------|--------------------------|
| **Niveau 1 (Critique)** | Obligatoire | Minimum 100 km ou région différente | Continue ou horaire |
| **Niveau 2 (Élevé)** | Obligatoire | Minimum 50 km ou zone de disponibilité différente | Quotidienne |
| **Niveau 3 (Moyen)** | Recommandée | Emplacement physique différent | Hebdomadaire |
| **Niveau 4 (Faible)** | Basée sur les risques | Stockage cloud acceptable | Sur modification |

**Critères de séparation géographique** :

- **Bâtiment différent** : Protection contre l'incendie, l'inondation, la panne d'alimentation du bâtiment
- **Centre de données différent** : Protection contre les catastrophes à l'échelle du centre de données
- **Ville/région différente** : Protection contre les catastrophes régionales (séisme, ouragan)
- **Pays/juridiction différents** : Protection contre les risques géopolitiques (pour les opérations multinationales)

**Conformité DORA** : Les entités financières de l'UE soumises à DORA DOIVENT mettre en œuvre la sauvegarde hors site à une distance géographique suffisante pour se protéger contre les catastrophes régionales (art. 12(4)).

**Exigences de sauvegarde immuable** :

**Systèmes critiques** (Niveau 1) :

- DOIVENT mettre en œuvre des sauvegardes immuables utilisant la technologie WORM (Write-Once-Read-Many)
- La période d'immuabilité DOIT s'aligner sur la politique de rétention (minimum 30 jours)
- Les sauvegardes immuables DOIVENT être séparées de l'infrastructure de sauvegarde standard
- Technologies : stockage objet avec verrouillage d'objet (AWS S3 Object Lock, Azure Immutable Blob), bibliothèques de bandes avec supports WORM, appliances de sauvegarde immuables dédiées

**Sauvegarde hors ligne/isolée** : Pour les systèmes critiques, au moins une copie de sauvegarde devrait être :

- Physiquement déconnectée du réseau (bande isolée, support amovible)
- Stockée dans un emplacement hors site sécurisé
- Tournée périodiquement (hebdomadaire/mensuelle)

**Justification** : Les sauvegardes immuables et isolées constituent la dernière ligne de défense contre les attaques de rançongiciel qui tentent de chiffrer ou supprimer les référentiels de sauvegarde.

**Sauvegarde cloud vers sur site** : Les charges de travail cloud devraient avoir des copies de sauvegarde :

- Exportables vers un format portable (éviter le verrouillage fournisseur cloud)
- Restaurables vers une infrastructure sur site si nécessaire
- Processus de reprise documenté pour les scénarios de rapatriement cloud

### Exigences de portabilité des sauvegardes

**Atténuation du verrouillage fournisseur** :

Pour assurer la flexibilité de reprise et éviter la dépendance à des fournisseurs de sauvegarde ou cloud spécifiques, les mises en œuvre de sauvegarde DOIVENT garantir :

**Portabilité du format de sauvegarde** :

- Les sauvegardes DOIVENT être exportables vers des formats industriels standard dans la mesure du possible
- Les formats propriétaires DOIVENT inclure des procédures de conversion documentées
- Les sauvegardes cloud DOIVENT être exportables sans outils spécifiques au fournisseur

**Indépendance de la plateforme de reprise** :

- Les sauvegardes DOIVENT être restaurables sur différentes plateformes (physique, virtuel, cloud)
- Les sauvegardes cloud DOIVENT être restaurables vers une infrastructure sur site
- Les sauvegardes sur site DOIVENT être portables vers une infrastructure cloud (reprise sur site vers cloud)
- Les solutions de sauvegarde DOIVENT documenter les procédures d'exportation/migration
- Les procédures de reprise DOIVENT adresser les scénarios de sortie fournisseur

**Justification** : Éviter le verrouillage fournisseur, permettre des stratégies DR flexibles, soutenir les scénarios de rapatriement cloud, maintenir les options de reprise lors de pannes cloud prolongées.

Cette exigence est critique pour l'indépendance cloud et est référencée dans les accords fournisseurs (ISMS-POL-A.5.19-23-S2 Section 8 : Retour et destruction des données).

### Exigences de test des sauvegardes

**Test de restauration** (tous les niveaux de sauvegarde) :

| Niveau système | Fréquence du test de restauration | Périmètre du test |
|----------------|-----------------------------------|-------------------|
| **Niveau 1** | Trimestriel minimum | Restauration complète du système vers un environnement alternatif |
| **Niveau 2** | Semestriel minimum | Ensembles de données représentatifs, système complet annuellement |
| **Niveau 3** | Annuel minimum | Vérification par restauration d'un échantillon |
| **Niveau 4** | En cas de changement significatif | Restauration d'un échantillon ou acceptation du risque |

**Exigences de documentation des tests** :

Chaque test de restauration de sauvegarde DOIT être documenté à l'aide d'un modèle standardisé incluant :

1. **Métadonnées du test** : ID du test, date, type (complet/partiel), système(s) testé(s), environnement de test, participants
2. **État avant test** : Systèmes dans le périmètre, source de sauvegarde (date/emplacement), RTO/RPO attendus
3. **Exécution du test** : Journal étape par étape des actions de restauration, horodatages, commandes/procédures utilisées
4. **Validation des résultats** :
   - Vérification de l'intégrité des données (sommes de contrôle, comptage d'enregistrements, inspection des données échantillon)
   - Validation de la fonctionnalité du système (démarrage de l'application, accès utilisateur, test de processus métier)
   - Validation des performances (répond aux exigences de production)
5. **Métriques** : Durée réelle de restauration, données récupérées (To/Go), variance RTO (réel vs cible)
6. **Artefacts de preuve** : Captures d'écran du système restauré, rapports de validation, extraits de journaux démontrant le succès
7. **Journal des problèmes** : Problèmes rencontrés, solutions de contournement appliquées, cause racine si identifiée
8. **Validation** : Approbation du Coordinateur CA/RA, confirmation de fonctionnalité par le Propriétaire du système

**Normes de documentation des tests** :
- Modèle standardisé maintenu dans ISMS-IMP-A.5.30-8.13-14-S4 (Processus de test de reprise)
- La documentation des tests DOIT être stockée dans [référentiel centralisé/SharePoint/outil ISMS]
- Rétention minimale : 3 ans ou selon exigence réglementaire
- Résultats des tests référencés dans le Classeur 4 (Résultats des tests CA/RA)

**Principe fondamental** : Les métriques de réussite des sauvegardes (sauvegarde terminée avec succès) ne valident PAS la capacité de reprise. Seuls les tests de restauration valident la capacité de reprise.

**Réponse aux tests échoués** : Les tests de sauvegarde révélant des échecs de reprise doivent déclencher :

- Investigation immédiate de la cause racine
- Remédiation des problèmes identifiés
- Nouveau test dans les 30 jours
- Signalement d'incident si affectant des systèmes critiques

**Conformité DORA** : Les entités financières soumises à DORA doivent tester la reprise des sauvegardes annuellement au minimum (art. 12(6)).

### Exigences de surveillance des sauvegardes

Les opérations de sauvegarde DOIVENT être surveillées :

| Élément de surveillance | Exigence | Seuil d'alerte |
|-------------------------|----------|----------------|
| **Succès/échec de sauvegarde** | Surveillance temps réel | Alerte immédiate en cas d'échec |
| **Durée de sauvegarde** | Analyse de tendance | Alerte si durée dépasse la fenêtre |
| **Taille de sauvegarde** | Analyse de tendance | Alerte sur croissance/réduction inattendue |
| **Capacité du référentiel** | Surveillance de capacité | Alerte à 75% d'utilisation |
| **Conformité de rétention** | Validation automatisée | Alerte sur violations de politique de rétention |

**Exigences d'alertes** :

| Déclencheur d'alerte | Sévérité | Notification à |
|----------------------|----------|----------------|
| Échec de sauvegarde de système critique | Élevée | Coordinateur CA/RA + Propriétaire du système |
| Échecs de sauvegarde consécutifs multiples | Élevée | Coordinateur CA/RA + RSSI |
| Seuil de capacité stockage sauvegarde (80%) | Moyenne | Administrateur de sauvegarde |
| Échec de réplication hors site | Élevée | Coordinateur CA/RA |
| Échec de vérification d'intégrité de sauvegarde | Élevée | Coordinateur CA/RA + Propriétaire du système |

**Rapports** : Des rapports mensuels sur l'état des sauvegardes doivent être fournis au RSSI incluant :

- Pourcentage de couverture des sauvegardes (systèmes sauvegardés vs. total)
- Taux de réussite des sauvegardes par criticité du système
- État d'achèvement des tests
- Problèmes en cours et calendrier de remédiation

Intégration de la surveillance : Les alertes de sauvegarde DOIVENT s'intégrer à la plateforme de surveillance organisationnelle (ISMS-POL-A.8.16 Activités de surveillance).

### Procédures de reprise

Des procédures de reprise DOIVENT être documentées pour chaque système sauvegardé incluant :

- Processus de restauration étape par étape
- Identifiants d'accès et autorisations requis
- Estimation du temps de reprise (RTO)
- Étapes de validation de la reprise
- Problèmes connus et solutions de contournement
- Coordonnées pour l'escalade

Les procédures de reprise DOIVENT être testées lors des exercices de test de restauration et mises à jour sur la base des résultats des tests.

**Considérations relatives aux sauvegardes cloud** :

**Sauvegarde par le fournisseur de services cloud** :

- Comprendre le « modèle de responsabilité partagée » du fournisseur
- Documenter quelles sauvegardes relèvent de la responsabilité du fournisseur par rapport à celle du client
- Mettre en œuvre des sauvegardes gérées par le client lorsque les capacités du fournisseur ne garantissent pas les exigences RPO

**Sauvegarde des applications SaaS** :

- Évaluer les capacités de sauvegarde et de rétention du fournisseur SaaS
- Mettre en œuvre une solution de sauvegarde SaaS tierce si les capacités du fournisseur sont insuffisantes
- Tester les procédures d'exportation et d'importation de données SaaS

**Portabilité des sauvegardes cloud** :

- Les formats de sauvegarde devraient permettre la restauration vers un fournisseur cloud alternatif ou sur site
- Documenter les procédures de reprise pour les scénarios cloud-to-cloud et cloud-to-on-premises
- Éviter les solutions de sauvegarde créant un verrouillage fournisseur

**Exigences fournisseurs** : Les fournisseurs de sauvegarde cloud doivent répondre aux exigences conformément à ISMS-POL-A.5.19-23 (Services fournisseurs/cloud) incluant :

- Classification comme fournisseur de Niveau 1 (Critique)
- Évaluation de sécurité et diligence raisonnable
- Engagements contractuels pour la disponibilité, la protection des données et la notification d'incident
- Droits d'audit ou attestation tierce (SOC 2 Type II, ISO 27001)

## Redondance des installations de traitement de l'information (A.8.14)

[Organisation] met en œuvre la redondance pour les installations critiques de traitement de l'information afin de répondre aux exigences de disponibilité et de minimiser les points de défaillance uniques.

### Exigences de redondance par criticité du système

**Détermination du niveau de redondance** :

| Criticité du système | RTO maximum | Exigence minimale de redondance |
|----------------------|-------------|----------------------------------|
| **Critique** | ≤ 4 heures | Actif-actif ou actif-passif avec basculement automatisé |
| **Élevé** | ≤ 24 heures | Veille chaude ou veille froide documentée avec reprise testée |
| **Moyen** | ≤ 72 heures | Veille froide ou procédures de reconstruction documentées |
| **Faible** | > 72 heures | Reprise basée sur les sauvegardes acceptable |

**Options d'architecture de redondance** :

| Architecture | Description | RTO typique | Cas d'usage |
|-------------|-------------|-------------|-------------|
| **Actif-Actif** | Plusieurs systèmes servant le trafic simultanément | Minutes | Systèmes critiques nécessitant une disponibilité continue |
| **Actif-Passif** | Système en veille prêt pour un basculement immédiat | Minutes à heures | Systèmes critiques avec interruption brève acceptable |
| **Veille chaude** | Environnement en veille partiellement provisionné | Heures | Systèmes haute priorité avec RTO modéré |
| **Veille froide** | Infrastructure disponible mais non provisionnée | Jours | Systèmes importants avec RTO plus long acceptable |

### Analyse des points de défaillance uniques (SPOF)

**Processus d'identification des SPOF** :

Les propriétaires de systèmes DOIVENT mener une analyse SPOF pour les systèmes critiques et élevés afin d'identifier les composants dont la défaillance entraînerait une défaillance complète du système :

**Exemples de SPOF d'infrastructure** :

- Serveur unique (sans clustering ni basculement)
- Chemin réseau unique (sans connectivité redondante)
- Alimentation unique ou onduleur unique
- Contrôleur de stockage unique
- Zone de disponibilité ou centre de données unique
- Serveur DNS unique
- Serveur d'authentification unique

**Documentation de l'analyse SPOF** :

- Inventaire des composants (serveurs, réseau, stockage, alimentation, refroidissement)
- Cartographie des dépendances (ce qui dépend de quoi)
- Identification des SPOF (composants sans redondance)
- Évaluation de l'impact (ce qui échoue si le composant échoue)
- Plan d'atténuation (comment éliminer le SPOF ou accepter le risque)

**Priorité de remédiation des SPOF** :

| Niveau de risque SPOF | Exigence de remédiation | Délai |
|-----------------------|-------------------------|-------|
| **SPOF de système critique** | Remédiation obligatoire | 90 jours ou acceptation du risque |
| **SPOF de système élevé** | Remédiation recommandée | 180 jours ou acceptation du risque |
| **SPOF de système moyen** | Décision basée sur les risques | Évaluation des risques requise |

**Exceptions SPOF** : Les SPOF acceptés DOIVENT être documentés dans le registre des exceptions avec acceptation du risque par le RSSI.

### Exigences de basculement et de commutation

**Mécanismes de basculement** :

| Niveau système | Type de basculement | Action de reprise | Impact RTO |
|----------------|---------------------|-------------------|------------|
| **Niveau 1 (Critique)** | Basculement automatisé | Le système bascule automatiquement vers le système en veille | Minutes |
| **Niveau 2 (Élevé)** | Basculement manuel avec procédure | L'opérateur exécute la procédure documentée | Heures |
| **Niveau 3 (Moyen)** | Reconstruction ou restauration | Provisionner un nouveau système ou restaurer depuis une sauvegarde | Jours |

**Exigences de test de basculement** :

Les systèmes critiques et élevés avec redondance DOIVENT tester les mécanismes de basculement :

| Niveau système | Fréquence du test de basculement | Périmètre du test |
|----------------|----------------------------------|-------------------|
| **Niveau 1 (Critique)** | Trimestriel | Basculement complet en production ou environnement similaire |
| **Niveau 2 (Élevé)** | Semestriel | Test de basculement documenté ou exercice de simulation |
| **Niveau 3 (Moyen)** | Annuel | Exercice de simulation ou validation de procédure documentée |

**Documentation des tests de basculement** :

- Date et périmètre du test
- Systèmes testés
- Mécanisme de déclenchement du basculement (manuel ou automatisé)
- Temps de basculement réel vs cible RTO
- Problèmes identifiés et remédiation
- Preuve de réussite du basculement

**Réponse aux échecs de basculement** : Les tests de basculement révélant une incapacité à atteindre le RTO doivent déclencher une remédiation immédiate et une évaluation des risques.

### Redondance géographique

**Systèmes critiques** : Les systèmes critiques devraient mettre en œuvre une redondance à une distance suffisante pour se protéger contre :

- Les catastrophes à l'échelle du site (incendie, inondation, panne d'alimentation)
- Les catastrophes régionales (séisme, ouragan)
- Les pannes prolongées de fournisseur cloud (déploiement multi-région)

**Options de redondance géographique** :

| Niveau de redondance | Séparation géographique | Protection contre | Exemple |
|----------------------|-------------------------|-------------------|---------|
| **Multi-serveur** | Même centre de données/rack | Défaillance matérielle serveur | Serveurs en cluster |
| **Multi-rack** | Même centre de données | Panne d'alimentation/refroidissement dans un rack | Serveurs dans différents racks |
| **Multi-zone** | Même région, zones de disponibilité différentes | Panne au niveau du centre de données | AWS Multi-AZ, Azure Availability Zones |
| **Multi-région** | Régions géographiques différentes | Catastrophe régionale | AWS us-east-1 + us-west-2 |
| **Multi-cloud** | Fournisseurs cloud différents | Panne du fournisseur cloud | Redondance AWS + Azure |

**Conformité DORA/NIS2** : Les entités financières et essentielles devraient mettre en œuvre une redondance géographique pour les systèmes critiques afin de répondre aux exigences de résilience opérationnelle.

**Analyse coût-bénéfice** : Les décisions de redondance géographique doivent équilibrer :

- Coût de l'infrastructure redondante
- Complexité de la gestion multi-région/multi-cloud
- Risque de pannes régionales
- Exigences réglementaires (DORA, NIS2, FINMA)
- Impact métier des pannes prolongées

### Redondance réseau

**Exigences de redondance réseau** :

Les systèmes critiques DOIVENT mettre en œuvre la redondance réseau à plusieurs couches :

| Couche réseau | Exigence de redondance | Exemple de mise en œuvre |
|--------------|------------------------|--------------------------|
| **Connectivité Internet** | Double FAI ou fournisseurs | Plusieurs connexions Internet |
| **Connectivité WAN** | Circuits redondants | MPLS + Internet, circuits doubles |
| **Réseau interne** | Commutateurs/routeurs redondants | Agrégation de commutateurs, HSRP/VRRP |
| **Équilibrage de charge** | Plusieurs équilibreurs de charge | Cluster LB actif-actif |
| **Pare-feux** | Paires de pare-feux HA | Cluster pare-feu actif-passif |

**Test de basculement réseau** : Les mécanismes de basculement réseau DOIVENT être testés trimestriellement pour les systèmes critiques.

### Redondance cloud vers sur site

**Stratégies de redondance hybride** :

Pour les organisations avec des déploiements cloud hybrides, les stratégies de redondance devraient considérer :

**Cloud en premier avec reprise sur site** :

- Principal : Infrastructure cloud (AWS, Azure, GCP)
- Secondaire : Infrastructure sur site pour les pannes cloud prolongées
- Cas d'usage : Rapatriement cloud lors d'incidents prolongés chez le fournisseur cloud

**Sur site en premier avec basculement cloud** :

- Principal : Infrastructure sur site
- Secondaire : Infrastructure cloud pour la reprise après sinistre
- Cas d'usage : Sur site traditionnel avec cloud comme cible de reprise après sinistre

**Hybride actif-actif** :

- Trafic partagé entre cloud et sur site
- Les deux environnements actifs simultanément
- Cas d'usage : Distribution géographique, optimisation des performances

**Considérations d'implémentation** :

- Synchronisation des données entre cloud et sur site
- Exigences de connectivité réseau (VPN, Direct Connect, ExpressRoute)
- Portabilité des licences (BYOL vers cloud)
- Procédures de reprise pour le basculement bidirectionnel

### Redondance électrique et environnementale

**Redondance des infrastructures critiques** :

Les centres de données et installations d'infrastructure critiques DOIVENT mettre en œuvre la redondance pour :

**Systèmes d'alimentation** :

- Double alimentation depuis le réseau électrique (si disponible)
- Systèmes d'alimentation sans interruption (ASI/UPS)
- Groupe électrogène de secours avec réserve de carburant
- Commutateurs de transfert automatique

**Systèmes de refroidissement** :

- Unités de climatisation (CVC) redondantes
- Surveillance environnementale (température, humidité)
- Alertes pour les violations de seuil environnemental

**Sécurité physique** :

- Systèmes de contrôle d'accès redondants
- Surveillance de sécurité physique de secours

**Environnements cloud** : Les fournisseurs cloud implémentent typiquement une redondance électrique/refroidissement N+1 ou 2N. Vérifier les affirmations de redondance du fournisseur via :

- Rapports SOC 2 Type II
- Visites sur site (lorsque autorisées)
- Certifications de centres de données tiers (Tier III/IV)

## Préparation des TIC pour la continuité des activités (A.5.30)

[Organisation] met en œuvre la planification de la continuité des TIC pour assurer la préparation aux perturbations des activités.

### Analyse d'impact sur les activités (AIA)

**Processus AIA** :

L'analyse d'impact sur les activités DOIT être conduite pour :

- Identifier les processus métier critiques
- Déterminer les dépendances TIC pour chaque processus métier
- Quantifier l'impact des perturbations TIC (financier, opérationnel, réputationnel, réglementaire)
- Établir la durée maximale d'interruption tolérable (DMIT), l'objectif de délai de reprise (RTO) et l'objectif de point de reprise (RPO)

**Fréquence de l'AIA** : L'AIA DOIT être conduite :

- Initialement lors de la mise en œuvre du SMSI
- Annuellement au minimum
- En cas de changements métier significatifs (nouveaux services, acquisitions, changements majeurs de systèmes)
- Après des incidents majeurs (intégration des leçons apprises)

**Résultats de l'AIA** :

- Inventaire des processus métier avec notations de criticité
- Inventaire des systèmes TIC avec classifications de criticité (Niveaux 1 à 4)
- DMIT, RTO et RPO pour chaque système critique
- Cartographie des dépendances (interdépendances des systèmes)
- Quantification de l'impact (perte financière par heure d'indisponibilité)

**Documentation de l'AIA** : Les résultats de l'AIA DOIVENT être documentés dans :

- **Registre de criticité des systèmes** : Inventaire principal de tous les systèmes avec classification Niveau 1-4, DMIT/RTO/RPO documentés, justification métier et validation du propriétaire. Maintenu par le Coordinateur CA/RA dans [outil ISMS/SharePoint/base de données]. Mis à jour dans les 30 jours suivant tout changement de classification de système.
- **Cartes de dépendance des processus métier** : Documentation visuelle ou tabulaire des dépendances TIC pour chaque processus métier critique, montrant les relations système en amont/aval.
- **Rapports d'évaluation AIA** : Rapport AIA formel avec quantification de l'impact, entretiens avec les parties prenantes, méthodologie d'analyse et signatures d'approbation des propriétaires de processus métier et du RSSI.

La documentation AIA DOIT :
- Être contrôlée en version avec suivi des modifications
- Être révisée et approuvée annuellement
- Être référencée dans le Classeur 3 (Matrice de conformité RPO/RTO)
- Être maintenue pour inspection d'audit (rétention minimale de 3 ans)

**Responsabilité AIA** : Le Coordinateur CA/RA pilote le processus AIA avec les contributions des propriétaires de processus métier et des propriétaires de systèmes.

### Stratégie de continuité des TIC

Sur la base des résultats AIA, [Organisation] DOIT définir une stratégie de continuité des TIC incluant :

**Stratégies de reprise par niveau de système** :

| Niveau système | Stratégie de reprise | Approche d'infrastructure |
|----------------|----------------------|---------------------------|
| **Niveau 1 (Critique)** | Actif-actif ou veille chaude | Infrastructure redondante, basculement automatisé |
| **Niveau 2 (Élevé)** | Veille chaude ou reconstruction rapide | Ressources pré-provisionnées, procédures documentées |
| **Niveau 3 (Moyen)** | Veille froide ou restauration depuis sauvegarde | Infrastructure disponible, restauration de sauvegarde |
| **Niveau 4 (Faible)** | Reconstruction ou reprise différée | Procédures de reconstruction standard |

**Stratégie de site de reprise** :

Stratégie de site de reprise de [Organisation] :

- **Site chaud** : Site pleinement opérationnel pour les systèmes de Niveau 1 (multi-région cloud, centre de données alternatif)
- **Site tiède** : Site partiellement provisionné pour les systèmes de Niveau 2 (capacité réservée cloud, centre de données DR)
- **Site froid** : Site prêt en infrastructure pour les systèmes de Niveau 3 (contrat avec fournisseur de centre de données)

**Stratégies alternatives** :

- Cloud comme site de reprise (sur site principal, cloud DR)
- Redondance multi-cloud (AWS + Azure, diversité régionale)
- Accords réciproques (accords DR mutuels avec partenaires — rarement utilisés)

### Plans de reprise des TIC

**Documentation du plan de continuité des TIC** :

Les plans de continuité des TIC DOIVENT documenter :

**Structure du plan** :
1. **Critères d'activation** : Quand activer le plan (processus de déclaration de sinistre)
2. **Rôles et responsabilités** : Structure de l'équipe de reprise, procédures d'escalade
3. **Contacts d'urgence** : Listes de contacts pour l'équipe de reprise, les fournisseurs, les parties prenantes
4. **Procédures de reprise** : Procédures de reprise système étape par étape
5. **Procédures de communication** : Modèles de communication interne et externe
6. **Priorités de reprise** : Séquence de reprise système basée sur les dépendances
7. **Procédures de validation** : Comment vérifier que les systèmes sont opérationnels

**Procédures de reprise spécifiques aux systèmes** :

Pour chaque système critique et élevé :

- Prérequis (infrastructure, réseau, dépendances)
- Instructions de reprise étape par étape
- Estimations de temps de reprise
- Étapes de validation pour confirmer la réussite de la reprise
- Procédures de retour arrière en cas d'échec de la reprise
- Problèmes connus et solutions de contournement

**Maintenance du plan** : Les plans de continuité des TIC DOIVENT :

- Être révisés annuellement
- Être mis à jour après les exercices de test
- Être mis à jour après les incidents majeurs
- Être mis à jour lorsque les systèmes ou l'infrastructure changent significativement
- Être contrôlés en version avec suivi des modifications

### Programme de test CA/RA

**Types de tests** :

| Type de test | Description | Fréquence | Périmètre |
|-------------|-------------|-----------|-----------|
| **Exercice de simulation** | Présentation Discussion | Annuelle | Tous les processus critiques |
| **Test de composant** | Test de reprise de système individuel | Trimestrielle | Systèmes critiques |
| **Test DR complet** | Basculement complet vers le site DR | Annuelle | Processus critiques de bout en bout |
| **Test surprise** | Test non annoncé (optionnel) | Selon besoin | Systèmes sélectionnés |

**Calendrier de test par criticité** :

| Criticité | Exigence de test annuel |
|-----------|-------------------------|
| **Critique** | Test DR complet + 2 tests de composant |
| **Élevé** | Test DR complet ou 2 tests de composant |
| **Moyen** | Test de composant ou exercice de simulation |
| **Faible** | Exercice de simulation |

**Conformité DORA** : Les entités financières soumises à DORA doivent :

- Tester les dispositions CA au moins annuellement (art. 11(9))
- Tester la sauvegarde et la restauration des TIC au moins annuellement (art. 12(6))
- Intégrer les tests CA/RA avec les tests de pénétration pilotés par les menaces (art. 26)

**Documentation des tests** : Chaque test CA/RA doit documenter :

- Date, périmètre, objectifs et participants du test
- Scénario et conditions du test
- Résultats du test (succès/échec/partiel)
- RTO/RPO réel vs cible
- Problèmes identifiés lors du test
- Leçons apprises et actions à mener
- Mises à jour du plan requises sur la base des résultats du test
- Validation par le Coordinateur CA/RA et le RSSI

**Réponse aux tests échoués** : Les tests révélant une incapacité à atteindre le RTO/RPO doivent déclencher :

- Investigation immédiate et analyse des causes racines
- Plan de remédiation des écarts avec calendrier
- Évaluation des risques de la capacité actuelle
- Contrôles compensatoires intérimaires si nécessaire
- Notification de la direction pour les systèmes critiques
- Nouveau test après remédiation

### Surveillance de la conformité RPO/RTO

**Alignement RPO/RTO** : Les capacités techniques (fréquence de sauvegarde, architecture de redondance) DOIVENT s'aligner sur les exigences RPO/RTO définies par les métiers.

**Évaluation de conformité** :

- Fréquence de sauvegarde vs RPO : Le calendrier de sauvegarde soutient-il le RPO ?
- Capacité de redondance vs RTO : Le basculement peut-il atteindre le RTO ?
- Résultats des tests vs cibles : Les temps de reprise réels respectent-ils le RTO ?

**Gestion des écarts** : Les écarts identifiés entre exigences et capacités doivent :

- Être documentés avec une évaluation des risques
- Avoir un plan de remédiation avec calendrier
- Nécessiter une acceptation du risque si non immédiatement remédiables
- Être escaladés au RSSI et à la direction générale pour les systèmes critiques

**Surveillance continue** : La surveillance automatisée doit suivre :

- Achèvement des sauvegardes dans la fenêtre RPO
- Vérifications de l'état de la redondance
- Vérification des capacités de basculement
- Conformité du calendrier de test

**Rapports RPO/RTO** : Les rapports trimestriels au RSSI doivent inclure :

- Systèmes respectant vs non conformes aux cibles RPO/RTO
- Analyse des écarts avec remédiation priorisée par criticité
- État de conformité des tests
- Analyse de tendance (amélioration vs dégradation)

### Coordination fournisseurs et tiers

**Exigences CA/RA des fournisseurs** : Les fournisseurs fournissant des services critiques ou élevés doivent répondre aux exigences conformément à ISMS-POL-A.5.19-23 (Services fournisseurs/cloud) incluant :

- Plans CA/RA documentés
- SLA définis incluant les engagements RTO/RPO
- Tests CA/RA annuels avec partage des résultats
- Procédures de notification d'incident
- Revues des plans CA/RA des fournisseurs lors de la diligence raisonnable

**Coordination avec les fournisseurs cloud** : Pour les systèmes hébergés dans le cloud :

- Comprendre les capacités et responsabilités CA/RA du fournisseur
- Valider que le SLA du fournisseur est aligné avec les RTO/RPO organisationnels
- Mettre en œuvre un DR géré par le client lorsque les capacités du fournisseur sont insuffisantes
- Documenter les procédures de notification d'incident du fournisseur
- Tester les procédures de reprise incluant l'engagement du fournisseur cloud

**Coordination avec les prestataires de services managés** : Pour les opérations TIC externalisées :

- S'assurer que les plans de reprise du PSM s'intègrent aux plans CA organisationnels
- Définir les rôles et responsabilités du PSM lors des sinistres
- Inclure le PSM dans les exercices de test CA/RA
- Vérifier la disponibilité du personnel et des ressources du PSM lors des sinistres

### Communication de crise

**Exigences du plan de communication** : Les plans CA/RA doivent inclure des procédures de communication pour :

**Communication interne** :

- Notification d'activation (qui, quand, comment)
- Mises à jour de statut pendant la reprise
- Notification de fin d'incident lorsque la reprise est terminée
- Planification de la revue post-incident

**Communication externe** :

- Notification client (proactive pour les pannes connues)
- Coordination fournisseurs/partenaires (si nécessaire pour la reprise)
- Notification réglementaire (si exigée par la réglementation)
- Communication publique/médias (si applicable)

**Canaux de communication** :

- Principal : Plateforme de communication de [Organisation] (courriel, Teams/Slack)
- Secours : SMS, appels téléphoniques (si principal indisponible)
- Urgence : Service de communication externe pré-établi

## Exigences inter-contrôles

### Approche de test intégrée

**Test inter-contrôles** :

Les tests CA/RA DOIVENT intégrer les trois contrôles :

**Scénario de test intégré** :
1. **Reprise depuis sauvegarde** (A.8.13) : Restaurer le système depuis la sauvegarde
2. **Basculement de redondance** (A.8.14) : Basculer vers l'infrastructure redondante
3. **Continuité des activités** (A.5.30) : Exécuter la reprise complète du processus métier

**Test intégré annuel** : Au moins un test CA/RA annuel DOIT exercer :

- Restauration de sauvegarde (reprise des données depuis sauvegarde hors site)
- Activation de redondance (basculement vers le site DR/région cloud)
- Validation du processus métier (confirmer que les opérations peuvent continuer)
- Procédures de communication (notifications internes et externes)

**Critères de réussite du test** :

- Tous les systèmes restaurés dans les cibles RTO
- Les données restaurées respectent les cibles RPO (perte de données acceptable)
- Processus métier opérationnels sur les systèmes récupérés
- Procédures de communication exécutées correctement

### Exigences de collecte des preuves

**Documentation des preuves d'audit** :

Pour chaque activité CA/RA, maintenir des preuves :

**Preuves de sauvegarde** :

- Journaux de réussite des sauvegardes
- Inventaire de stockage des sauvegardes (ce qui est sauvegardé, où)
- Résultats des tests de sauvegarde (tests de restauration avec captures d'écran)
- Alertes de surveillance des sauvegardes et réponses

**Preuves de redondance** :

- Schémas d'architecture de redondance
- Résultats de l'analyse SPOF
- Résultats des tests de basculement
- Données de surveillance de l'état de la redondance

**Preuves de continuité des TIC** :

- Résultats AIA et approbation
- Plans de continuité des TIC (versions actuelles)
- Résultats des exercices de test
- Historique des mises à jour du plan

**Référentiel de preuves suivi dans les tableaux de bord récapitulatifs** : Le Coordinateur CA/RA DOIT maintenir un référentiel centralisé de preuves incluant :

- Base de données des résultats de tests
- Versions du plan et historique des modifications
- Registre des exceptions
- Post-mortems d'incidents impliquant l'activation CA/RA

### Gestion des écarts et remédiation

**Identification des écarts** :

Les écarts de capacité CA/RA DOIVENT être identifiés par :

- Échecs de tests (systèmes ne respectant pas les RTO/RPO)
- Mises à jour AIA (nouveaux systèmes critiques identifiés)
- Conclusions d'audit (audits internes ou externes)
- Leçons apprises des incidents (réponse réelle aux sinistres)
- Changements technologiques (nouveaux systèmes sans sauvegarde/redondance)

**Priorisation des écarts** :

| Type d'écart | Priorité | Délai de remédiation |
|-------------|----------|----------------------|
| **Système critique ne respectant pas RTO/RPO** | P1 — Critique | 30 jours ou acceptation du risque |
| **Écart système élevé** | P2 — Élevé | 90 jours |
| **Écart système moyen** | P3 — Moyen | 180 jours |
| **Non-conformité aux tests** | P2 — Élevé | Prochain cycle de test |

**Processus de remédiation des écarts** :
1. Écart identifié et documenté
2. Analyse des causes racines
3. Plan de remédiation développé (solution technique, calendrier, ressources)
4. Approbation RSSI du plan
5. Mise en œuvre et validation
6. Nouveau test pour confirmer la fermeture de l'écart
7. Mise à jour de la documentation

**Registre des écarts** : Le Coordinateur CA/RA DOIT maintenir un registre des écarts incluant :

- Description de l'écart
- Système/processus affecté
- Évaluation des risques
- Plan de remédiation et calendrier
- Statut de remédiation
- Date cible de clôture

---

# Gouvernance et conformité

## Rôles et responsabilités

| Rôle | Responsabilités CA/RA |
|------|----------------------|
| **Directeur général (PDG)** | Responsabilité ultime pour la continuité des activités ; Approuver la stratégie et le budget CA/RA ; Déclarer les sinistres nécessitant l'activation du plan |
| **Responsable de la sécurité des systèmes d'information (RSSI)** | Propriétaire de la politique CA/RA ; Approuver les exigences CA/RA et l'acceptation des risques ; S'assurer des ressources adéquates pour la mise en œuvre CA/RA ; Rapporter l'état CA/RA à la direction générale |
| **Directeur des systèmes d'information (DSI)** | Responsabilité opérationnelle pour la continuité des TIC ; Allouer des ressources pour la mise en œuvre sauvegarde/redondance ; Approuver les investissements technologiques pour CA/RA ; S'assurer que les plans de reprise TIC sont alignés sur les exigences métier |
| **Coordinateur CA/RA** | Gestion quotidienne du programme CA/RA ; Coordonner le processus AIA ; Maintenir les plans de reprise ; Planifier et faciliter les tests CA/RA ; Suivre la conformité avec les exigences de sauvegarde/redondance ; Rapporter les métriques et écarts CA/RA |
| **Administrateur de sauvegarde** | Mettre en œuvre et gérer les solutions de sauvegarde ; Configurer les calendriers et la rétention des sauvegardes ; Surveiller les sauvegardes et résoudre les pannes ; Coordonner les tests de sauvegarde ; Maintenir l'infrastructure de sauvegarde |
| **Administrateurs système / Administrateurs cloud** | Mettre en œuvre la redondance pour les systèmes assignés ; Configurer les mécanismes de basculement ; Participer aux tests CA/RA ; Maintenir la documentation de reprise système ; Répondre aux défaillances système et aux événements de reprise |
| **Propriétaires de systèmes / Propriétaires d'applications** | Définir les exigences RTO/RPO pour leurs systèmes ; Fournir des contributions au processus AIA ; Approuver les priorités de reprise système ; Participer aux tests CA/RA ; Valider la fonctionnalité des systèmes récupérés |
| **Propriétaires de processus métier** | Définir les exigences de continuité des activités ; Identifier les processus critiques et les dépendances ; Approuver les RTO/RPO pour les processus métier ; Participer aux exercices CA/RA ; Valider la reprise des processus métier |
| **Équipe de sécurité** | Surveiller la sécurité de l'infrastructure de sauvegarde et DR ; Vérifier la mise en œuvre du chiffrement ; Examiner la sécurité des sites DR et du DR cloud ; Participer aux tests CA/RA ; Coordination de la réponse aux incidents |
| **Responsable juridique/conformité** | Déterminer les exigences réglementaires CA/RA ; Assurer la conformité avec DORA, NIS2, etc. ; Examiner les engagements CA/RA des fournisseurs ; Conseiller sur les implications de résidence des données |

**Matrice de responsabilité** :

| Activité | Pilote | Support | Approuve | Informe |
|----------|--------|---------|----------|---------|
| Processus AIA | Coordinateur CA/RA | Propriétaires métier, Propriétaires système | RSSI | DSI |
| Politique de sauvegarde | RSSI | Coordinateur CA/RA | Direction générale | Tout le personnel |
| Mise en œuvre des sauvegardes | Administrateur de sauvegarde | Administrateurs système | DSI | Coordinateur CA/RA |
| Conception de redondance | Propriétaires système | Équipe infrastructure | DSI | Coordinateur CA/RA |
| Développement du plan de reprise | Coordinateur CA/RA | Propriétaires système | RSSI | Propriétaires métier |
| Tests CA/RA | Coordinateur CA/RA | Toute l'équipe de reprise | RSSI | Direction générale |
| Remédiation des écarts | Propriétaires système | Équipe infrastructure | RSSI (acceptation risque) | Coordinateur CA/RA |

## Gestion des exceptions

**Processus de demande d'exception** :

Les exceptions aux exigences CA/RA (ex. système exclu de la sauvegarde, redondance non mise en œuvre) doivent suivre un processus d'approbation formel :

**Étape 1 : Soumission de la demande d'exception**

- Demandeur : Propriétaire du système ou propriétaire métier
- Informations requises : Système/périmètre, exigence faisant l'objet de l'exception, justification métier, évaluation des risques, contrôles compensatoires proposés, durée de l'exception

**Étape 2 : Évaluation des risques**

- Réalisée par : Coordinateur CA/RA + Équipe de sécurité
- Évaluation : Impact si un sinistre se produit, probabilité du sinistre, implications réglementaires, cote de risque

**Étape 3 : Décision d'approbation**

| Niveau de risque de l'exception | Autorité d'approbation |
|---------------------------------|------------------------|
| Risque faible (système non critique, courte durée) | Coordinateur CA/RA |
| Risque moyen | RSSI |
| Risque élevé (système critique, impact réglementaire) | RSSI + DSI |
| Risque critique (impact métier sévère) | Direction générale (PDG/DSI/RSSI) |

**Étape 4 : Suivi des exceptions**

- Toutes les exceptions documentées dans le registre des exceptions
- Révision périodique (trimestrielle pour les exceptions temporaires)
- Ré-approbation requise à l'expiration
- Suivi de la remédiation si l'exception est temporaire

**Exceptions permanentes** : Les systèmes définitivement exclus des exigences de sauvegarde/redondance doivent :

- Avoir une acceptation du risque documentée
- Être révisés annuellement
- Nécessiter l'approbation du RSSI pour les systèmes critiques/élevés
- Documenter pourquoi l'approche CA/RA standard n'est pas réalisable

## Surveillance et rapports

**Surveillance continue** :

- Taux de réussite/échec des sauvegardes
- Utilisation de la capacité de stockage des sauvegardes
- Vérifications de l'état de la redondance (état du clustering, de la réplication)
- Métriques de conformité RPO/RTO
- Respect du calendrier de test

**Exigences de rapport** :

**Rapports mensuels** (Coordinateur CA/RA → RSSI) :

- Taux de réussite des sauvegardes par criticité
- Sauvegardes échouées nécessitant une investigation
- État de disponibilité de la redondance
- Calendrier de test à venir
- Problèmes ouverts et état de remédiation

**Rapports trimestriels** (Coordinateur CA/RA → RSSI + DSI) :

- KPIs du programme CA/RA
- Résumé de conformité RPO/RTO
- Résultats des tests et leçons apprises
- Analyse des écarts avec priorisation
- Révision du registre des exceptions
- Analyse de tendance

**Rapports annuels** (RSSI → Direction générale) :

- Évaluation de maturité CA/RA
- Incidents majeurs et efficacité de la reprise
- Conformité avec les exigences réglementaires
- Besoins d'investissement et recommandations stratégiques

**Indicateurs clés de performance (KPIs)** :

| KPI | Cible | Mesure |
|-----|-------|--------|
| Couverture des sauvegardes (% systèmes critiques sauvegardés) | 100% | Mensuelle |
| Taux de réussite des sauvegardes | ≥ 99% | Mensuelle |
| Conformité des tests de sauvegarde | ≥ 95% | Trimestrielle |
| Conformité RPO (% systèmes respectant RPO) | 100% critique, ≥ 95% élevé | Trimestrielle |
| Conformité RTO (% systèmes respectant RTO aux tests) | 100% critique, ≥ 95% élevé | Trimestrielle |
| Taux de réussite des tests DR | ≥ 90% | Annuelle |
| Remédiation SPOF (% SPOF critiques atténués) | ≥ 90% | Trimestrielle |

## Gestion des incidents

**Types d'incidents CA/RA** :

| Type d'incident | Description | Réponse |
|----------------|-------------|---------|
| **Échec de sauvegarde** | La sauvegarde d'un système critique échoue à plusieurs reprises | Investiguer immédiatement, restaurer depuis la sauvegarde précédente si nécessaire |
| **Capacité de stockage** | Le stockage de sauvegarde dépasse le seuil | Augmenter la capacité ou ajuster la politique de rétention |
| **Échec de redondance** | Capacité de basculement indisponible | Remédiation immédiate, évaluation des risques |
| **Échec de test** | Le test de reprise ne respecte pas le RTO/RPO | Analyse des causes racines, plan de remédiation |
| **Événement sinistre** | Sinistre réel nécessitant une reprise | Activer le plan CA/RA, exécuter les procédures de reprise |

**Notification d'incident** :

- Échecs de sauvegarde (systèmes critiques) : Notifier le Coordinateur CA/RA + le Propriétaire du système immédiatement
- Échecs de redondance : Notifier le Coordinateur CA/RA + le RSSI immédiatement
- Déclaration de sinistre : Activer le plan de communication de crise

**Intégration avec la gestion des incidents** : Les incidents CA/RA s'intègrent au processus de gestion des incidents organisationnel (A.5.24-27) pour :

- Journalisation et suivi des incidents
- Analyse des causes racines
- Leçons apprises
- Amélioration continue

## Gouvernance de la politique

**Révision de la politique** :

- **Fréquence** : Annuelle minimum
- **Déclencheurs** : Changements réglementaires, incidents majeurs, changements métier significatifs, conclusions d'audit, changements technologiques
- **Réviseurs** : RSSI, Coordinateur CA/RA, DSI, Juridique/conformité
- **Approbation** : RSSI (technique), Direction générale (stratégique)

**Révision des normes de mise en œuvre** :

- **Fréquence** : Selon l'évolution technologique (au moins semestrielle)
- **Autorité** : Le Coordinateur CA/RA propose les mises à jour, le RSSI approuve
- **Note** : Les mises à jour des normes de mise en œuvre (ISMS-IMP-A.5.30-8.13-14) ne nécessitent pas de révision de politique

**Mises à jour de la politique** :

- **Mineures** (clarifications, références) : Approbation RSSI, communication dans les 30 jours
- **Majeures** (changements de périmètre, nouvelles exigences) : Chaîne d'approbation complète, calendrier de mise en œuvre selon la gestion des changements
- **D'urgence** (changement réglementaire critique, leçons apprises d'un incident majeur) : Approbation RSSI, communication et mise en œuvre immédiates

**Communication** : Politique publiée dans le référentiel de documents SMSI. Les modifications sont communiquées à l'échelle de l'organisation. Une formation est dispensée pour les changements significatifs affectant les responsabilités ou les procédures.

---

# Mise en œuvre et références

## Intégration avec le SMSI

Cette politique s'intègre au Système de management de la sécurité de l'information de [Organisation] :

**Évaluation des risques** (Clause ISO 27001 6.1) :

- Les contrôles CA/RA sélectionnés sur la base de l'évaluation des risques de [Organisation]
- Les résultats AIA alimentent le processus d'évaluation des risques
- Les plans de traitement des risques documentent la mise en œuvre des contrôles CA/RA
- Les risques résiduels des exceptions CA/RA documentés

**Inventaire des actifs** (A.5.9) :

- Les systèmes nécessitant sauvegarde/redondance identifiés via l'inventaire des actifs
- La classification de criticité des actifs pilote les exigences CA/RA
- Les modifications de l'inventaire des actifs déclenchent une révision CA/RA

**Gestion de la configuration** (A.8.9) :

- Les configurations système sauvegardées conformément à la politique de sauvegarde
- Les configurations de référence documentées pour la reprise
- L'infrastructure-as-code permet la reconstruction rapide
- Intégration : Les sauvegardes de configuration gérées conformément aux exigences A.8.9

**Journalisation** (A.8.15) :

- Les opérations de sauvegarde journalisées (succès, échec, durée)
- Les événements de basculement journalisés
- Les opérations de reprise journalisées pour la piste d'audit
- Intégration : Les journaux CA/RA centralisés conformément aux exigences A.8.15

**Activités de surveillance** (A.8.16) :

- La surveillance des sauvegardes intégrée à la plateforme de surveillance organisationnelle
- L'état des systèmes redondants surveillé en continu
- La conformité RTO/RPO surveillée
- Intégration : Surveillance CA/RA conformément aux exigences A.8.16

## Ressources de mise en œuvre

**Conseils de mise en œuvre** (suite ISMS-IMP-A.5.30-8.13-14) :

| Document | Objectif | Périmètre |
|----------|---------|-----------|
| **ISMS-IMP-A.5.30-8.13-14-S1** | Processus BIA et RPO/RTO | Méthodologie AIA, classification de criticité des systèmes, détermination RPO/RTO |
| **ISMS-IMP-A.5.30-8.13-14-S2** | Mise en œuvre des sauvegardes | Sélection de solution de sauvegarde, conception d'architecture, planification, rétention, surveillance, procédures de reprise |
| **ISMS-IMP-A.5.30-8.13-14-S3** | Mise en œuvre de la redondance | Identification SPOF, conception d'architecture de redondance, mécanismes de basculement, redondance géographique |
| **ISMS-IMP-A.5.30-8.13-14-S4** | Processus de test de reprise | Test de restauration des sauvegardes, test de basculement, test de scénario CA/RA, collecte de preuves |

**Outils d'évaluation** (classeurs Excel) :

- **Classeur 1** : Inventaire des sauvegardes et évaluation de couverture (systèmes sauvegardés, conformité RPO, conformité 3-2-1-1-0)
- **Classeur 2** : Analyse de redondance (architecture de redondance, analyse SPOF, conformité RTO)
- **Classeur 3** : Matrice de conformité RPO/RTO (exigences métier vs capacités techniques, analyse des écarts)
- **Classeur 4** : Résultats des tests CA/RA (inventaire des tests, suivi des résultats, état de remédiation)

**Matériaux de support** :

- Modèles de procédures de reprise
- Modèles de questionnaire AIA
- Listes de vérification et scénarios de test
- Formulaires de demande d'exception
- Modèles de suivi de remédiation des écarts

## Cartographie réglementaire

Cette politique répond aux exigences CA/RA des réglementations applicables :

| Catégorie d'exigence | nLPD suisse | RGPD UE | ISO 27001 | DORA* | NIS2* | PCI DSS v4.0.1* | FINMA* |
|----------------------|-------------|---------|-----------|-------|-------|---------|--------|
| Exigences de sauvegarde | Art. 8 | Art. 32 | A.8.13 | Art. 12 | Art. 21 | Req. 12.10 | Basé sur risques |
| Sauvegarde hors site | Art. 8 | Art. 32 | A.8.13 | Art. 12 (Obligatoire) | Art. 21 (Obligatoire) | Req. 12.10 | Basé sur risques |
| Immuabilité | — | — | A.8.13 | Art. 12 (Obligatoire) | Art. 21 (Recommandé) | — | Basé sur risques |
| Redondance | Art. 8 | Art. 32 | A.8.14 | Art. 12 | Art. 21 | — | Basé sur risques |
| Planification continuité TIC | Art. 8 | Art. 32 | A.5.30 | Art. 12, 14 | Art. 21 | Req. 12.10 | Basé sur risques |
| Exigences de test | Art. 8 | Art. 32 | A.8.13, A.5.30 | Art. 12 | Art. 21 | Req. 12.10 | Basé sur risques |
| Notification d'incident | Art. 24 | Art. 33 | A.5.24 | Art. 19 (24h) | Art. 23 (24h) | Req. 12.10 | Gestion incidents |
| CA/RA fournisseurs | Art. 9 | Art. 28 | A.5.19-23 | Art. 28 | Art. 22 | Req. 12.8 | Externalisation |

*Applicabilité conditionnelle conformément à ISMS-POL-00

**Cartographie spécifique DORA** (art. 11-12) :

- Politique de continuité des activités TIC → Section 2.3
- Politiques et procédures de sauvegarde → Section 2.1
- Plans de reprise après sinistre → Section 2.3.3
- Sauvegardes immuables → Section 2.1.6
- Stockage de sauvegarde hors site → Section 2.1.6
- Test annuel de sauvegarde → Section 2.1.8
- Test annuel du plan CA → Section 2.3.4

**Cartographie spécifique NIS2** (art. 21) :

- Continuité des activités et gestion de crise → Section 2.3
- Gestion et restauration des sauvegardes → Section 2.1
- Règle de sauvegarde 3-2-1 → Section 2.1.5
- Notification d'incident sous 24 heures → ISMS-POL-A.5.24 (Gestion des incidents)

## Formation et sensibilisation

**Sensibilisation à la sécurité** (tout le personnel) :

- Module de formation annuel sur la sensibilisation CA/RA
- Responsabilités des utilisateurs lors des sinistres
- Bonnes pratiques de sauvegarde des données (pour les domaines de responsabilité personnelle)
- État d'esprit et culture de la continuité des activités

**Formation équipe CA/RA** (Coordinateur CA/RA, Administrateurs de sauvegarde, Administrateurs système) :

- Politique et procédures CA/RA
- Configuration et gestion des technologies de sauvegarde
- Exécution des procédures de reprise
- Méthodologie de test et documentation
- Réponse aux incidents lors des sinistres

**Formation équipe de reprise** :

- Révision annuelle des plans de reprise
- Participation aux exercices CA/RA
- Procédures de reprise spécifiques aux rôles
- Procédures de communication de crise

**Formation direction** :

- Stratégie et gouvernance CA/RA
- Critères et procédures de déclaration de sinistre
- Responsabilités de leadership en crise
- Exigences de conformité réglementaire

---

# Définitions

**Sauvegarde** : Copie de données, de logiciels ou de configuration système créée à des fins de reprise en cas de perte, de corruption ou d'indisponibilité. Les sauvegardes sont généralement stockées séparément des systèmes de production.

**Redondance** : Mise en œuvre d'installations de traitement de l'information dupliquées ou alternatives pour assurer la disponibilité en cas de défaillance. La redondance peut être matérielle (plusieurs serveurs), logicielle (clustering) ou géographique (plusieurs centres de données).

**Continuité des activités (CA)** : Capacité organisationnelle à poursuivre les opérations métier pendant et après des événements perturbateurs. La CA englobe à la fois les systèmes TIC et les processus métier non-TIC.

**Reprise après sinistre (RA)** : Processus de restauration des systèmes TIC et des données après une perturbation. La RA est un sous-ensemble de la continuité des activités axé spécifiquement sur la reprise TIC.

**Objectif de point de reprise (RPO)** : Quantité maximale acceptable de perte de données mesurée en temps. Le RPO définit la fréquence à laquelle les sauvegardes doivent avoir lieu. Exemple : Un RPO de 4 heures signifie que les sauvegardes doivent avoir lieu au moins toutes les 4 heures, et qu'une perte de données allant jusqu'à 4 heures est acceptable.

**Objectif de délai de reprise (RTO)** : Délai maximum acceptable pour restaurer un système après une perturbation. Le RTO définit la rapidité avec laquelle la reprise doit avoir lieu. Exemple : Un RTO de 24 heures signifie que le système doit être restauré dans les 24 heures suivant la défaillance.

**Durée maximale d'interruption tolérable (DMIT)** : Durée maximale absolue pendant laquelle un processus métier peut être indisponible avant de provoquer des conséquences inacceptables. La DMIT est généralement plus longue que le RTO car elle inclut le temps pour les solutions de contournement et les processus manuels.

**Analyse d'impact sur les activités (AIA)** : Processus systématique d'identification et d'évaluation des effets potentiels d'une perturbation sur les opérations métier critiques. L'AIA détermine la DMIT, le RTO et le RPO pour les processus métier et les systèmes TIC de support.

**Point de défaillance unique (SPOF)** : Composant dont la défaillance entraînerait la défaillance de l'ensemble du système ou du processus. L'analyse SPOF identifie les composants manquant de redondance.

**Basculement** : Processus de commutation automatique ou manuelle vers un système redondant ou en veille lorsque le système principal est défaillant.

**Site chaud** : Installation de secours pleinement opérationnelle avec équipements, connectivité et réplication des données permettant un basculement immédiat.

**Site tiède** : Installation de secours avec équipements et connectivité mais nécessitant une restauration des données avant de devenir opérationnelle.

**Site froid** : Installation de secours avec infrastructure de base (alimentation, refroidissement, espace) mais nécessitant l'installation d'équipements et la restauration des données avant de devenir opérationnelle.

**Actif-Actif** : Architecture de redondance où plusieurs systèmes servent activement le trafic simultanément. La défaillance d'un système est gérée par les systèmes actifs restants.

**Actif-Passif** : Architecture de redondance où le système principal sert activement le trafic tandis que le système en veille reste inactif mais prêt pour une activation immédiate en cas de défaillance du système principal.

**Sauvegarde immuable** : Sauvegarde qui ne peut être modifiée ni supprimée après création (WORM — Write Once Read Many). Protège contre les rançongiciels et la suppression accidentelle.

**Sauvegarde isolée (air-gapped)** : Sauvegarde physiquement déconnectée du réseau, offrant une isolation contre les cyberattaques.

**Sauvegarde hors site** : Sauvegarde stockée dans un emplacement géographique séparé de l'emplacement principal des données, protégeant contre les sinistres spécifiques au site.

**Règle de sauvegarde 3-2-1** : Meilleure pratique recommandant 3 copies des données (original + 2 sauvegardes), sur 2 types de supports différents, avec 1 copie hors site.

**Règle de sauvegarde 3-2-1-1-0** : Règle de sauvegarde améliorée ajoutant 1 copie immuable/isolée et 0 erreur dans les tests de vérification des sauvegardes.

**Sauvegarde incrémentale** : Sauvegarde uniquement des données modifiées depuis la dernière sauvegarde (complète ou incrémentale), réduisant le temps de sauvegarde et le stockage.

**Sauvegarde différentielle** : Sauvegarde des données modifiées depuis la dernière sauvegarde complète, offrant une reprise plus rapide qu'incrémentale mais utilisant plus de stockage.

**Sauvegarde complète** : Sauvegarde complète de toutes les données, offrant la reprise la plus simple mais nécessitant le plus de temps et de stockage.

**Rapatriement cloud** : Processus de migration des charges de travail et des données du cloud vers une infrastructure sur site, pertinent pour les pannes cloud prolongées ou les changements stratégiques.

**Multi-cloud** : Architecture utilisant plusieurs fournisseurs cloud pour la redondance, l'évitement du verrouillage fournisseur ou l'optimisation des services.

**Cloud hybride** : Architecture combinant infrastructure sur site et services cloud, supportant des scénarios de reprise flexibles.

---

# Registre d'approbation

| Rôle | Nom | Date |
|------|-----|------|
| **Responsable de la sécurité des systèmes d'information (RSSI)** | [Nom] | [Date] |
| **Directeur des systèmes d'information (DSI)** | [Nom] | [Date] |
| **Coordinateur CA/RA** | [Nom] | [Date] |
| **Responsable juridique/conformité** | [Nom] | [Date] |
| **Direction générale** | [Nom] | [Date] |

---

**FIN DU DOCUMENT DE POLITIQUE**

---

*Cette politique établit les exigences CA/RA. Les procédures de mise en œuvre sont documentées dans ISMS-IMP-A.5.30-8.13-14-S1 à S4 (UG/TG). Chaque classeur d'évaluation inclut son propre tableau de bord récapitulatif pour la vérification de conformité.*

<!-- QA_VERIFIED: 2026-03-30 -->
