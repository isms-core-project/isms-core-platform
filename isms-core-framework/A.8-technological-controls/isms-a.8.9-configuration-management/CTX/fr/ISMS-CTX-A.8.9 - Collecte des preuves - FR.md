<!-- ISMS-CORE:CTX:ISMS-CTX-A.8.9-FR-evidence-collection:framework:CTX:a.8.9 -->
**ISMS-CTX-A.8.9 — Collecte des preuves**

**Contrôle du document**

| Attribut | Valeur |
|----------|--------|
| **Identifiant du document** | ISMS-CTX-A.8.9-collecte-des-preuves |
| **Version** | 1.0 |
| **Type de document** | Référence technique (NON SMSI) |
| **Politique connexe** | ISMS-POL-A.8.9 (Toutes sections) |
| **Objet** | Fournir une structure standardisée de référentiel de preuves pour la démonstration de conformité au Contrôle A.8.9 de la norme ISO 27001:2022 et la préparation aux audits |
| **Public visé** | Responsables de configuration, administrateurs systèmes, auditeurs, responsables de conformité, dépositaires de preuves |
| **Cycle de révision** | Annuel (ou lors de changements d'exigences d'audit) |
| **Date** | [Date] |

### Historique des versions

| Version | Date | Modifications | Auteur |
|---------|------|---------------|--------|
| 1.0 | [Date] | Guide initial de collecte des preuves (NON SMSI) | Équipe de mise en œuvre SMSI |

### Approbateurs

- Principale : Responsable de la configuration
- Révision technique : Architecte de sécurité
- AUCUNE approbation exécutive requise (NON SMSI)

### Distribution

Équipe de gestion de la configuration, administrateurs systèmes, opérations IT, ingénieurs sécurité, responsables de conformité, auditeurs internes, auditeurs externes.

### Documents connexes

- ISMS-POL-A.8.9 : Politique de gestion de la configuration (consolidée)
- ISMS-CTX-A.8.9 : Référence de gestion de la configuration (NON SMSI)
- ISMS-IMP-A.8.9-UG : Guide de mise en œuvre de la gestion de la configuration (utilisateur)
- ISMS-IMP-A.8.9-TG : Guide de mise en œuvre de la gestion de la configuration (technique)

---

## ⚠️ IMPORTANT : Statut du document

**CE DOCUMENT NE FAIT PAS PARTIE DU SMSI.**

**CE DOCUMENT NE DÉFINIT PAS D'EXIGENCES OBLIGATOIRES.**

**CE DOCUMENT N'ÉTABLIT PAS D'OBLIGATIONS CONTRAIGNANTES.**

**TOUTES LES EXIGENCES CONTRAIGNANTES SONT DÉFINIES DANS ISMS-POL-A.8.9.**

Il s'agit d'une référence technique et d'orientations opérationnelles pour la collecte, l'organisation et la préparation aux audits des preuves uniquement.

**Objet** : Fournir des orientations pratiques pour organiser les preuves visant à démontrer la conformité au Contrôle A.8.9 lors des audits ISO 27001:2022. Ce document complète ISMS-POL-A.8.9 et ISMS-IMP-A.8.9 mais NE remplace PAS les exigences de politique.

**Public visé** : Dépositaires de preuves, coordinateurs d'audit, responsables de configuration chargés de préparer les dossiers de preuves d'audit.

**Utilisation** : Référence pour établir la structure du référentiel de preuves, les conventions de nommage, les politiques de conservation et les flux de préparation aux audits. Les organisations personnalisent ce contenu en fonction de leurs systèmes de gestion documentaire et de leurs exigences d'audit spécifiques.

---

## Vue d'ensemble

Ce guide définit la structure standardisée du référentiel de preuves pour le Contrôle A.8.9 (Gestion de la configuration) de la norme ISO 27001:2022. Une organisation correcte des preuves permet des audits efficaces, démontre l'efficacité des contrôles et soutient la vérification de la conformité.

**Emplacement du référentiel** : [À définir par l'organisation — par ex. SharePoint/Lecteur réseau/Système de gestion documentaire]

**Contrôle d'accès** : Le référentiel de preuves DOIT être contrôlé avec un accès en lecture pour les auditeurs et les responsables de conformité, et un accès en écriture restreint à l'équipe de gestion de la configuration.

**Durée de conservation** : Minimum 3 ans conformément aux exigences ISO 27001:2022 ; plus longtemps si requis par des réglementations sectorielles spécifiques.

---

## Structure racine des preuves

```
Evidence/
  ISMS-A.8.9-Baseline-Configuration/
  ISMS-A.8.9-Change-Control/
  ISMS-A.8.9-Configuration-Monitoring/
  ISMS-A.8.9-Security-Hardening/
```

---

## Preuves de configuration de référence

**Fichier d'évaluation** : ISMS-IMP-A.8.9.xlsx (généré par script Python)

### Structure des répertoires

**Evidence/ISMS-A.8.9-Baseline-Configuration/**

#### 1. Asset-Inventory/

Contient l'inventaire complet des actifs démontrant l'étendue de la couverture des référentiels.

**Fichiers requis** :

- `CMDB-Export-AAAAMMJJ.xlsx` — Export complet de la Base de données de gestion des configurations
- `Network-Scan-Results-AAAAMMJJ.pdf` — Résultats des analyses de découverte réseau
- `Asset-Criticality-Classifications.pdf` — Classifications des actifs par niveau (Niveaux 1-4)
- `Cloud-Asset-Inventory-AWS-AAAAMMJJ.csv` — Inventaire des actifs AWS
- `Cloud-Asset-Inventory-Azure-AAAAMMJJ.csv` — Inventaire des actifs Azure
- `Asset-Inventory-Reconciliation-Report.xlsx` — Comparaison de sources multiples

**Objet des preuves** : Démontre l'existence d'un inventaire complet des actifs et que les cibles de couverture des référentiels sont mesurables.

#### 2. Baseline-Documentation/

Contient les configurations de référence approuvées organisées par type d'actif.

**Sous-répertoires** :

**Windows-Server/**

- `BL-WIN2022-DC-v2.1.docx` — Référentiel Windows Server 2022 Contrôleur de domaine
- `BL-WIN2022-FS-v1.5.docx` — Référentiel Windows Server 2022 Serveur de fichiers
- `BL-WIN2022-APP-v1.8.docx` — Référentiel Windows Server 2022 Serveur d'applications
- `CIS-Windows-Server-2022-Mapping.xlsx` — Correspondance CIS Benchmark

**Linux-Unix/**

- `BL-RHEL9-STD-v1.3.pdf` — Référentiel Red Hat Enterprise Linux 9
- `BL-UBUNTU2204-WEB-v2.0.pdf` — Référentiel Ubuntu 22.04 Serveur web
- `BL-SUSE15-DB-v1.2.pdf` — Référentiel SUSE Linux 15 Serveur de base de données
- `CIS-Linux-Benchmark-Mapping.xlsx` — Correspondance CIS Benchmark

**Network-Devices/**

- `BL-Cisco-ASA-FW-v3.1.pdf` — Référentiel pare-feu Cisco ASA
- `BL-Palo-Alto-NGFW-v2.5.pdf` — Référentiel pare-feu nouvelle génération Palo Alto
- `BL-Cisco-Switch-IOS-v1.9.pdf` — Référentiel commutateur Cisco IOS
- `BL-F5-LoadBalancer-v1.4.pdf` — Référentiel équilibreur de charge F5

**Cloud-Platforms/**

- `BL-AWS-EC2-Linux-v2.2.pdf` — Référentiel instance EC2 Linux AWS
- `BL-AWS-RDS-MySQL-v1.6.pdf` — Référentiel AWS RDS MySQL
- `BL-Azure-VM-Windows-v1.8.pdf` — Référentiel VM Windows Azure
- `CIS-AWS-Foundations-Benchmark-Mapping.xlsx` — Correspondance CIS AWS

**Databases/**

- `BL-SQLServer2022-v1.7.pdf` — Référentiel SQL Server 2022
- `BL-PostgreSQL15-v1.4.pdf` — Référentiel PostgreSQL 15
- `BL-Oracle19c-v2.1.pdf` — Référentiel Oracle 19c
- `DISA-STIG-Database-Mapping.xlsx` — Correspondance DISA STIG

**Containers/**

- `BL-Docker-v1.5.pdf` — Référentiel Docker
- `BL-Kubernetes-v2.0.pdf` — Référentiel Kubernetes
- `CIS-Kubernetes-Benchmark-Mapping.xlsx` — Correspondance CIS Kubernetes

**Convention de nommage** : `BL-[Technologie]-[Rôle]-v[Version].pdf`

- BL = Référentiel (Baseline)
- Technologie = Produit/Plateforme (WIN2022, RHEL9, etc.)
- Rôle = Usage (DC, WEB, APP, DB, etc.)
- Version = Versionnage sémantique (majeure.mineure)

**Objet des preuves** : Démontre l'existence de référentiels documentés référençant des normes reconnues.

#### 3. Golden-Images/

Contient l'inventaire des images de référence et les dossiers d'approbation.

**Fichiers requis** :

- `Image-Inventory-Register.xlsx` — Liste maîtresse de toutes les images de référence
- `WIN2022-STD-v2.1-20240115-ApprovalRecord.pdf` — Approbation d'image avec signatures
- `RHEL9-SEC-v1.3-20240120-ApprovalRecord.pdf` — Approbation d'image avec signatures

**Image-Build-Manifests/** (code IaC pour les constructions reproductibles) :

- `WIN2022-STD-v2.1-BuildManifest.yaml` — Définition de construction automatisée
- `RHEL9-SEC-v1.3-BuildManifest.yaml` — Définition de construction automatisée

**Vulnerability-Scans/** (validation de sécurité pré-approbation) :

- `WIN2022-STD-v2.1-VulnScan-AAAAMMJJ.pdf` — Rapport d'analyse des vulnérabilités
- `RHEL9-SEC-v1.3-VulnScan-AAAAMMJJ.pdf` — Rapport d'analyse des vulnérabilités

**Objet des preuves** : Démontre que les images de référence mettent en œuvre les référentiels et sont validées sur le plan sécurité avant l'utilisation en production.

#### 4. Approval-Records/

Contient les approbations formelles des référentiels.

**Fichiers requis** :

- `Baseline-Approval-Matrix.xlsx` — Suivi maître de toutes les approbations de référentiels
- `CAB-Meeting-Minutes-AAAAMMJJ.pdf` — Réunions du CAC où les référentiels ont été approuvés
- `Email-Approval-BL-WIN2022-DC-v2.1.pdf` — Chaînes d'approbation par e-mail
- `RSSI-Approval-Baseline-Security-Standards.pdf` — Approbation exécutive

**Objet des preuves** : Démontre que les référentiels disposent d'une autorisation appropriée et d'une supervision de gouvernance.

#### 5. Configuration-Snapshots/

Contient les exports réels de configuration démontrant la conformité aux référentiels.

**Fichiers requis** :

- `Server-Config-WebServer01-AAAAMMJJ.txt` — Configuration réelle du serveur
- `Firewall-Rules-Export-AAAAMMJJ.xml` — Export de configuration du pare-feu
- `Database-Config-DBSERVER01-AAAAMMJJ.sql` — Configuration de la base de données
- `Kubernetes-Manifest-Export-AAAAMMJJ.yaml` — Configuration Kubernetes

**Objet des preuves** : Démontre que les configurations déployées correspondent aux référentiels approuvés.

#### 6. Deviation-Documentation/

Contient les exceptions approuvées aux référentiels.

**Fichiers requis** :

- `Deviation-Register.xlsx` — Liste maîtresse de toutes les dérogations approuvées
- `Deviation-Request-DEV-2024-001.pdf` — Demande de dérogation avec justification métier
- `Risk-Assessment-DEV-2024-001.pdf` — Analyse des risques pour la dérogation
- `Compensating-Controls-DEV-2024-001.pdf` — Documentation des contrôles d'atténuation
- `RSSI-Approval-DEV-2024-001.pdf` — Approbation exécutive

**Convention de nommage** : `DEV-AAAA-###` où ### est un numéro séquentiel.

**Objet des preuves** : Démontre que les dérogations sont formellement gérées avec évaluation des risques et approbation.

#### 7. Assessment-Reports/

Contient les classeurs d'évaluation complétés et les rapports récapitulatifs.

**Fichiers requis** :

- `Baseline-Assessment-AAAAMMJJ.xlsx` — Classeur ISMS-IMP-A.8.9 complété
- `Assessment-Summary-Presentation.pptx` — Résumé exécutif
- `Evidence-Register-Index.pdf` — Index de toutes les preuves collectées
- `Gap-Remediation-Plan.xlsx` — Plan d'action pour les lacunes identifiées

**Objet des preuves** : Démontre l'évaluation régulière de la conformité aux référentiels et la remédiation des lacunes.

---

## Preuves du contrôle des changements

**Fichier d'évaluation** : ISMS-IMP-A.8.9.xlsx (généré par script Python)

### Structure des répertoires

**Evidence/ISMS-A.8.9-Change-Control/**

#### 1. Change-Requests/

Contient toute la documentation des demandes de changement.

**Sous-répertoires par Année-Trimestre** :

- `2024-Q1/` — Tous les changements du T1 2024
- `2024-Q2/` — Tous les changements du T2 2024
- etc.

**Par changement** :

- `CR-2024-001-Change-Request-Form.pdf` — Formulaire de demande de changement complété
- `CR-2024-001-Risk-Assessment.pdf` — Analyse des risques
- `CR-2024-001-Testing-Results.pdf` — Validation des tests
- `CR-2024-001-Implementation-Log.pdf` — Étapes réelles de mise en œuvre
- `CR-2024-001-Post-Implementation-Review.pdf` — Revue post-mise en œuvre dans les 5 jours

**Convention de nommage** : `CR-AAAA-###` où ### est un numéro séquentiel.

#### 2. CAB-Records/

Contient la documentation des réunions du Comité d'Approbation des Changements.

**Fichiers requis** :

- `CAB-Meeting-Schedule-2024.pdf` — Calendrier publié du CAC
- `CAB-Membership-Roster.pdf` — Membres actuels du CAC et leurs rôles
- `CAB-Charter.pdf` — Autorité et responsabilités du CAC
- `CAB-Meeting-Minutes-20240115.pdf` — Procès-verbal de réunion avec décisions
- `CAB-Meeting-Minutes-20240122.pdf` — Procès-verbal de réunion avec décisions
- `CAB-Attendance-Log-2024.xlsx` — Suivi de présence pour la vérification du quorum

**Objet des preuves** : Démontre que le CAC fonctionne régulièrement avec une gouvernance appropriée.

#### 3. Approval-Workflows/

Contient les chaînes d'approbation pour différents types de changements.

**Fichiers requis** :

- `Approval-Workflow-Diagram.pdf` — Représentation visuelle des niveaux d'approbation
- `Standard-Change-Catalog.xlsx` — Changements standard pré-approuvés
- `Emergency-Change-Log.xlsx` — Tous les changements d'urgence avec révisions rétrospectives
- `Approval-Authority-Matrix.pdf` — Qui peut approuver quoi

#### 4. Testing-Validation/

Contient les plans de tests et résultats.

**Par changement à risque élevé** :

- `TEST-CR-2024-001-TestPlan.pdf` — Plan de test formel
- `TEST-CR-2024-001-TestResults.xlsx` — Résultats détaillés des tests
- `TEST-CR-2024-001-Screenshots.pdf` — Preuves visuelles
- `TEST-CR-2024-001-RollbackTest.pdf` — Validation de la procédure de retour arrière

#### 5. Change-Success-Metrics/

Contient les rapports d'ICP de la gestion des changements.

**Fichiers requis** (mensuel/trimestriel) :

- `Change-Metrics-Dashboard-202401.pdf` — Rapport de métriques mensuel
- `Change-Success-Rate-Trend-Analysis.xlsx` — Suivi historique
- `Emergency-Change-Analysis-Q1-2024.pdf` — Révision de la justification des changements d'urgence
- `Failed-Change-Root-Cause-Analysis.pdf` — Analyse des retours arrière

**Objet des preuves** : Démontre l'efficacité de la gestion des changements et l'amélioration continue.

#### 6. Assessment-Reports/

- `Change-Control-Assessment-AAAAMMJJ.xlsx` — Classeur ISMS-IMP-A.8.9 complété
- `Assessment-Summary-Presentation.pptx` — Résumé exécutif
- `Evidence-Register-Index.pdf` — Preuves collectées

---

## Preuves de surveillance de la configuration

**Fichier d'évaluation** : ISMS-IMP-A.8.9.xlsx (généré par script Python)

### Structure des répertoires

**Evidence/ISMS-A.8.9-Configuration-Monitoring/**

#### 1. Monitoring-Infrastructure/

Contient les preuves de déploiement des outils de surveillance.

**Fichiers requis** :

- `Monitoring-Tool-Inventory.xlsx` — Tous les outils de surveillance déployés
- `Monitoring-Architecture-Diagram.pdf` — Comment la surveillance est déployée
- `Monitoring-Coverage-Report.xlsx` — Couverture des actifs par niveau
- `Monitoring-Agent-Deployment-Status.xlsx` — Suivi de l'installation des agents

#### 2. Drift-Alerts/

Contient les alertes de détection de dérives et les remédiations.

**Sous-répertoires par gravité** :

- `Critical-Drift/` — Changements de contrôles de sécurité critiques
- `High-Drift/` — Changements de haute gravité
- `Medium-Drift/` — Changements de gravité moyenne
- `Low-Drift/` — Changements informationnels de faible gravité

**Par incident de dérive** :

- `DRIFT-2024-001-Alert.pdf` — Alerte originale avec détails
- `DRIFT-2024-001-Investigation.pdf` — Investigation des causes profondes
- `DRIFT-2024-001-Remediation.pdf` — Actions de remédiation prises
- `DRIFT-2024-001-Closure.pdf` — Clôture de l'incident avec vérification

**Convention de nommage** : `DRIFT-AAAA-###`

#### 3. Baseline-Comparison-Reports/

Contient les analyses régulières de conformité aux référentiels.

**Fichiers requis** (mensuel minimum pour le Niveau 1, trimestriel pour le Niveau 2) :

- `Baseline-Compliance-Scan-202401-Tier1.pdf` — Conformité des actifs de Niveau 1
- `Baseline-Compliance-Scan-202401-Tier2.pdf` — Conformité des actifs de Niveau 2
- `Drift-Trend-Analysis-Q1-2024.xlsx` — Analyse des tendances

#### 4. Remediation-Tracking/

Contient le suivi des actions de remédiation des dérives.

**Fichiers requis** :

- `Drift-Remediation-Register.xlsx` — Tous les incidents de dérive ouverts/clos
- `SLA-Compliance-Report.xlsx` — Respect des SLA de remédiation
- `Recurring-Drift-Analysis.pdf` — Analyse des causes profondes des dérives récurrentes

#### 5. Monitoring-Performance/

Contient les preuves de santé et de fiabilité des outils de surveillance.

**Fichiers requis** :

- `Monitoring-Tool-Uptime-Report.xlsx` — Métriques de disponibilité des outils
- `Alert-False-Positive-Rate.xlsx` — Efficacité de l'ajustement des alertes
- `Monitoring-Incident-Log.xlsx` — Défaillances du système de surveillance

#### 6. Assessment-Reports/

- `Monitoring-Assessment-AAAAMMJJ.xlsx` — Classeur ISMS-IMP-A.8.9 complété
- `Assessment-Summary-Presentation.pptx` — Résumé exécutif
- `Evidence-Register-Index.pdf` — Preuves collectées

---

## Preuves de durcissement de la sécurité

**Fichier d'évaluation** : ISMS-IMP-A.8.9.xlsx (généré par script Python)

### Structure des répertoires

**Evidence/ISMS-A.8.9-Security-Hardening/**

#### 1. Hardening-Standards/

Contient la documentation des normes de durcissement.

**Fichiers requis** :

- `Hardening-Standards-Register.xlsx` — Toutes les normes applicables mappées aux actifs
- `CIS-Benchmarks-Library/` — CIS Benchmark PDFs téléchargés
- `DISA-STIG-Library/` — Fichiers STIG téléchargés
- `Vendor-Security-Guides/` — Documentation de durcissement fournisseurs
- `Standard-Selection-Rationale.pdf` — Pourquoi chaque norme a été choisie

#### 2. Compliance-Scans/

Contient les analyses automatisées de conformité au durcissement.

**Sous-répertoires par type d'actif** :

- `Windows-Servers/`
- `Linux-Servers/`
- `Network-Devices/`
- `Databases/`
- `Cloud-Platforms/`

**Par type d'actif** (trimestriel minimum) :

- `CIS-Scan-WIN2022-202401.pdf` — Résultats d'analyse de conformité
- `CIS-Scan-RHEL9-202401.pdf` — Résultats d'analyse de conformité
- `Compliance-Trend-Analysis-Q1-2024.xlsx` — Suivi historique

#### 3. Gap-Analysis/

Contient les lacunes de durcissement identifiées et les plans de remédiation.

**Fichiers requis** :

- `Hardening-Gap-Register.xlsx` — Toutes les lacunes identifiées
- `Critical-Gap-Remediation-Plan.xlsx` — Plan d'action pour les lacunes critiques
- `Gap-Risk-Assessment.pdf` — Analyse des risques pour les lacunes
- `Remediation-Status-Dashboard.xlsx` — Suivi de la progression

#### 4. Hardening-Exceptions/

Contient les exceptions approuvées aux normes de durcissement.

**Par exception** :

- `HARD-EX-2024-001-Exception-Request.pdf` — Demande d'exception formelle
- `HARD-EX-2024-001-Risk-Assessment.pdf` — Analyse des risques
- `HARD-EX-2024-001-Compensating-Controls.pdf` — Mesures d'atténuation
- `HARD-EX-2024-001-Approval.pdf` — Approbation du RSSI/Architecte de sécurité

**Convention de nommage** : `HARD-EX-AAAA-###`

#### 5. Hardening-Implementation/

Contient les preuves de mise en œuvre du durcissement.

**Fichiers requis** :

- `Pre-Hardening-Scans/` — Référence avant durcissement
- `Post-Hardening-Scans/` — Validation après durcissement
- `Hardening-Scripts/` — Scripts de durcissement automatisés
- `Implementation-Logs/` — Piste d'audit des changements de durcissement

#### 6. Compliance-Reports/

Contient les rapports réguliers de conformité.

**Fichiers requis** (trimestriel) :

- `Hardening-Compliance-Dashboard-Q1-2024.pdf` — Tableau de bord exécutif
- `Compliance-by-Asset-Tier-Q1-2024.xlsx` — Conformité par niveau d'actif
- `Critical-Controls-Compliance-Report.xlsx` — Focus sur les contrôles critiques
- `Year-over-Year-Improvement-Analysis.pdf` — Progression de la maturité

#### 7. Assessment-Reports/

- `Hardening-Assessment-AAAAMMJJ.xlsx` — Classeur ISMS-IMP-A.8.9 complété
- `Assessment-Summary-Presentation.pptx` — Résumé exécutif
- `Evidence-Register-Index.pdf` — Preuves collectées

---

## Bonnes pratiques de collecte des preuves

### Résumé des conventions de nommage

**Format général** : `[Type]-[Date/ID]-[Description].[ext]`

**Exemples** :

- Classeurs d'évaluation : `Baseline-Assessment-20240315.xlsx`
- Demandes de changement : `CR-2024-042-Firewall-Rule-Update.pdf`
- Incidents de dérive : `DRIFT-2024-018-Unauthorised-Service-Start.pdf`
- Exceptions : `HARD-EX-2024-005-Legacy-App-Exception.pdf`
- Procès-verbaux du CAC : `CAB-Meeting-Minutes-20240315.pdf`

### Normes de format de date

**Toutes les dates dans les noms de fichiers** : Format AAAAMMJJ (ISO 8601)

- Correct : `20240315`
- Incorrect : `03-15-2024`, `15.03.2024`

**Justification** : Assure que le tri alphabétique = tri chronologique.

### Normes de format de fichier

**Formats préférés** :

- **Documents formels** : PDF/A (format d'archivage)
- **Tableurs** : XLSX (Excel) ou CSV (pour l'échange de données)
- **Exports de configuration** : Format natif (XML, JSON, YAML, TXT)
- **Diagrammes** : PDF (depuis Visio/draw.io), PNG (si interactif non nécessaire)

**À éviter** :

- Formats propriétaires sans lecteurs gratuits
- Fichiers protégés par mot de passe (utiliser le contrôle d'accès du référentiel)
- Archives compressées (stocker non compressées pour l'indexation)

### Règles de conservation des preuves

| Type de preuve | Durée de conservation | Justification |
|----------------|----------------------|---------------|
| Classeurs d'évaluation | 3 ans minimum | Exigence ISO 27001 |
| Demandes de changement | 3 ans minimum | Exigence de piste d'audit |
| Incidents de dérive | 3 ans minimum | Suivi des incidents de sécurité |
| Dossiers d'approbation | 7 ans | Exigence légale/conformité |
| Instantanés de configuration | 1 an glissant | Besoin opérationnel uniquement |
| Procès-verbaux du CAC | Permanente | Documentation de gouvernance |
| Analyses de durcissement | 1 an glissant | Besoin opérationnel uniquement |

**Extensions sectorielles** :

- Services financiers (FINMA) : 10 ans
- Soins de santé (HIPAA) : 6 ans
- Marchés publics : Selon les termes du contrat

### Liste de contrôle qualité des preuves

Avant de classer une preuve, vérifier :

- [ ] Le nom de fichier respecte la convention de nommage
- [ ] La date est exacte et au format AAAAMMJJ
- [ ] Le fichier est dans le format préféré (PDF/XLSX)
- [ ] Le document est complet (pas en brouillon/partiel)
- [ ] Les données sensibles sont correctement classifiées
- [ ] Le fichier n'est pas corrompu (ouvrir pour vérifier)
- [ ] Les références croisées vers d'autres preuves sont exactes
- [ ] Placé dans le bon répertoire conformément à ce guide

### Contrôle d'accès aux preuves

**Accès en lecture** :

- Équipe de gestion de la configuration
- Équipe d'audit interne
- Auditeurs externes (pendant les périodes d'audit)
- Responsables de conformité
- RSSI et collaborateurs directs

**Accès en écriture** :

- Responsable de la configuration
- Dépositaires de preuves désignés
- Systèmes de collecte automatisée (comptes de service)

**Aucun accès** :

- Personnel IT général (demande via le Responsable de la configuration)
- Parties externes sans accord de confidentialité (NDA)
- Employés ayant quitté l'organisation (révocation immédiate)

### Automatisation de la collecte des preuves

**Automatisation recommandée** :

- **Exports CMDB** : Export automatisé hebdomadaire
- **Analyses de conformité** : Analyses trimestrielles automatisées
- **Instantanés de configuration** : Sauvegarde nocturne des configurations critiques
- **Alertes de dérive** : Export en temps réel vers le référentiel de preuves
- **Archivage des demandes de changement** : Automatique à la clôture du changement

**Collecte manuelle** :

- Signatures d'approbation (signatures manuscrites requises)
- Évaluations des risques (jugement humain requis)
- Procès-verbaux du CAC (générés par l'humain)
- Investigations d'incidents (analyse humaine requise)

---

## Annexe : Téléchargements de modèles de preuves

[L'organisation doit fournir des modèles pour] :

- Formulaire de demande de changement (CR-Template.docx)
- Formulaire de demande de dérogation (DEV-Template.docx)
- Formulaire de demande d'exception (HARD-EX-Template.docx)
- Modèle d'évaluation des risques (Risk-Assessment-Template.xlsx)
- Modèle de procès-verbal du CAC (CAB-Minutes-Template.docx)

**Emplacement des modèles** : [À définir par l'organisation — par ex. SharePoint/Intranet]

---

## Maintenance du référentiel de preuves

**Révision trimestrielle** (responsabilités du Responsable de la configuration) :

- Vérifier la complétude des preuves du trimestre passé
- Archiver les preuves de plus d'un an selon le calendrier de conservation
- Mettre à jour le `Evidence-Register-Master-Index.pdf`
- Réviser la liste de contrôle d'accès (entrées/sorties)
- Vérifier la sauvegarde/reprise après sinistre du référentiel de preuves

**Révision annuelle** (responsabilités du RSSI) :

- Auditer la conformité de la structure du référentiel à ce guide
- Réviser la conformité à la politique de conservation
- Évaluer la qualité et la complétude des preuves
- Mettre à jour ce guide si des améliorations de processus sont identifiées

---

**FIN DU DOCUMENT DE RÉFÉRENCE TECHNIQUE**

*Pour les exigences de politique contraignantes, consulter ISMS-POL-A.8.9 Politique de gestion de la configuration.*

<!-- QA_VERIFIED: 2026-04-02 -->
