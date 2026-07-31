<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.19-23-S6-FR:framework:POL:a.5.19-23-s6 -->
**ISMS-POL-A.5.19-23-S6 — Méthodologie d'évaluation et automatisation**
**Sécurité des services en nuage — Approche d'ingénierie système**

---

**Contrôle documentaire**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Méthodologie d'évaluation et automatisation |
| **Type de document** | Section de politique |
| **Identifiant du document** | ISMS-POL-A.5.19-23-S6 |
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
| 1.0 | [Date] | RSI | Section initiale couvrant le cadre d'évaluation basé sur Python |

**Cycle de révision** : Annuel
**Prochaine révision** : [Date d'entrée en vigueur + 12 mois]

**Chaîne d'approbation** :

- Primaire : Responsable de la sécurité des systèmes d'information (RSSI)
- Secondaire : Responsable de la sécurité de l'information (RSI)
- Technique : Responsable de l'équipe ingénierie système
- Qualité : Responsable assurance qualité
- Autorité finale : Direction générale

**Documents connexes** :

- ISMS-POL-00 (Cadre d'applicabilité réglementaire)
- ISMS-POL-A.5.19-23 (Politique parente — Sécurité des fournisseurs et des services en nuage)
- Tous les documents de mise en œuvre ISMS-IMP-A.5.19-23
- ISMS-REF-A.5.23 (Registre des fournisseurs de services en nuage)
- Scripts Python de génération dans 50_scripts-excel/
- ISO/IEC 27001:2022 Clause 9.2 (Audit interne)

---

# Résumé exécutif

## Objet

Le présent document définit l'**approche d'ingénierie système (IS)** pour l'évaluation de la conformité de la sécurité des services en nuage. Plutôt que des audits traditionnels de type liste de contrôle, nous utilisons des **classeurs Excel générés par Python** qui garantissent :

- Des évaluations **reproductibles** (structure identique chaque trimestre)
- Des métriques de conformité **quantitatives** (87,3 % conforme vs. « globalement conforme »)
- Une vérification **fondée sur des preuves** (captures d'écran, configurations, contrats)
- Des tableaux de bord **transparents** (calculés automatiquement depuis les évaluations)

## Principe fondamental

**« Si vous ne pouvez pas le générer, vous ne pourrez pas le maintenir »** : Les feuilles de calcul manuelles se dégradent avec le temps — les formules se cassent, les validations disparaissent et des incohérences apparaissent entre les cycles d'évaluation. Les modèles copiés-collés dérivent au fil des modifications par différentes parties prenantes sans contrôle de version. Les outils d'évaluation doivent être générés de manière programmatique pour garantir cohérence, reproductibilité et mises à jour systématiques lors des changements d'exigences. Cette politique utilise des générateurs Python pour créer des classeurs d'évaluation Excel, permettant un déploiement rapide, des modifications maîtrisées et une mesure de la conformité fondée sur des preuves avec des pistes d'audit complètes.

**Approche d'ingénierie système :**
```
1. Exécuter le générateur Python → ISMS_REG_A523_1_Inventory.xlsx
2. Les achats complètent la liste des services avec preuves
3. Le tableau de bord calcule automatiquement : « 45/78 services conformes (57,7 %) »
4. Le rapport d'écarts identifie : « 33 services sans AMF »
```

**Résultat :** Évaluation objective et quantitative de l'état de conformité réel, et non une auto-évaluation subjective.

---

# Architecture du cadre

## Conception à cinq couches

```
┌─────────────────────────────────────────────────────────────────────┐
│ COUCHE 1 : COUCHE POLITIQUE                                         │
│ • ISMS-POL-A.5.19-23 (Index principal)                              │
│ • ISMS-POL-A.5.19-23-S5 (Exigences des services en nuage)           │
│ • ISMS-POL-A.5.19-23-S6 (Ce document — Méthodologie)                │
└─────────────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────────────┐
│ COUCHE 2 : SPÉCIFICATIONS D'ÉVALUATION (Markdown)                   │
│ • ISMS-IMP-A.5.19-23.S1.md — Inventaire et classification           │
│ • ISMS-IMP-A.5.19-23.S2.md — Diligence raisonnable fournisseurs     │
│ • ISMS-IMP-A.5.19-23.S3.md — Configuration sécurisée                │
│ • ISMS-IMP-A.5.19-23.S4.md — Gouvernance continue                   │
└─────────────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────────────┐
│ COUCHE 3 : MISE EN ŒUVRE (Scripts Python)                           │
│ • generate_reg_a523_1_inventory.py                                  │
│ • generate_reg_a523_2_vendor_dd.py                                  │
│ • generate_reg_a523_3_secure_config.py                              │
│ • generate_reg_a523_4_governance.py                                 │
└─────────────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────────────┐
│ COUCHE 4 : RÉVISION (Tableaux de bord intégrés)                     │
│ • Chaque classeur contient son propre onglet Tableau de bord        │
│ • Réviser les métriques de conformité directement dans chaque       │
│   classeur                                                          │
└─────────────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────────────┐
│ COUCHE 5 : VALIDATION (Approbation et piste d'audit)                │
│ • Onglet de validation dans chaque classeur                         │
│ • Registre des preuves pour la traçabilité des audits               │
│ • Analyse des écarts et planification des corrections par domaine   │
└─────────────────────────────────────────────────────────────────────┘
```

## Structure des classeurs d'évaluation

Chaque classeur suit ce modèle éprouvé :

| Onglet | Objet | Rempli par | Cycle de révision |
|--------|-------|-----------|-------------------|
| **Instructions et légende** | Mode d'emploi + codes de statut | Généré automatiquement | S.O. |
| **Onglets d'évaluation (2-6)** | Listes de contrôle par domaine | Parties prenantes | Trimestriel |
| **Tableau de bord** | % de conformité par domaine | Piloté par formules | Automatique |
| **Registre des preuves** | Liens vers les documents justificatifs | Parties prenantes | Trimestriel |
| **Validation** | Approbation RSSI + dates de révision | Direction | Trimestriel |

---

# Spécification des classeurs d'évaluation

## Classeur 1 : Inventaire et classification des services en nuage

**Identifiant du document :** ISMS-IMP-A.5.19-23.S1
**Nom de fichier :** `ISMS_REG_A523_1_Inventory_AAAAMMJJ.xlsx`
**Généré par :** `generate_reg_a523_1_inventory.py`
**Parties prenantes :** Opérations IT, Achats, Finance
**Nombre d'onglets :** 10

**Objet :** Maintenir un inventaire faisant autorité de tous les services en nuage avec leur classification de criticité.

**Structure des onglets :**
1. Instructions et légende
2. Services SaaS (Office 365, Salesforce, Zoom, etc.)
3. Services IaaS/PaaS (AWS, Azure, GCP, etc.)
4. Services de sécurité en nuage (CrowdStrike, Zscaler, etc.)
5. Services de stockage en nuage (Dropbox, Box, etc.)
6. Cartographie de la classification des données
7. Évaluation de la criticité des services
8. Tableau de bord
9. Registre des preuves
10. Validation

**Colonnes de base (17 colonnes standard A-Q) :**

- A : Nom du service en nuage
- B : Type de service (SaaS/IaaS/PaaS/Sécurité/Stockage)
- C : Nom du fournisseur
- D : Criticité du service (Critique/Élevée/Moyenne/Faible)
- E : Classification des données (Restreint/Confidentiel/Interne/Public)
- F : Région de résidence des données (Suisse/UE/USA/Global)
- G : Statut du contrat (Actif/Renouvellement en cours/Expiré)
- H : Statut (✅ Conforme / ⚠️ Partiel / ❌ Non conforme)
- I : Emplacement des preuves
- J : Description de l'écart
- K : Correction nécessaire (Oui/Non)
- L : Identifiant d'exception
- M : Identifiant de risque
- N : Mesures compensatoires
- O : Propriétaire du service
- P : Date cible de correction
- Q : Impact budgétaire (Élevé/Moyen/Faible/Aucun)

**Colonnes étendues (R-X spécifiques à l'inventaire) :**

- R : Coût mensuel (formule : validation numérique)
- S : Valeur annuelle du contrat
- T : Nombre d'utilisateurs sous licence
- U : Nombre d'intégrations (# de systèmes connectés)
- V : Service de sauvegarde disponible (Oui/Non)
- W : Faisabilité de la sortie (Facile/Moyen/Difficile/Inconnu)
- X : Date de la dernière révision de l'inventaire

## Classeur 2 : Diligence raisonnable et contrats fournisseurs

**Identifiant du document :** ISMS-IMP-A.5.19-23.S2
**Nom de fichier :** `ISMS_REG_A523_2_DueDiligence_AAAAMMJJ.xlsx`
**Généré par :** `generate_reg_a523_2_vendor_dd.py`
**Parties prenantes :** Juridique, Achats, Conformité, RSI
**Nombre d'onglets :** 10

**Objet :** Suivre les certifications de sécurité des fournisseurs, les conditions contractuelles, les SLA et les droits d'audit.

**Onglets :**
1. Instructions et légende
2. Certifications de sécurité des fournisseurs
3. Analyse des conditions contractuelles
4. Exigences et performances des SLA
5. Conformité à la souveraineté des données
6. Support forensique et réponse aux incidents
7. Droit d'audit et tests d'intrusion
8. Tableau de bord
9. Registre des preuves
10. Validation

**Colonnes étendues (R-X) :**

- R : Certification ISO 27001 (Oui/Non/Inconnu + N° cert.)
- S : Rapport SOC 2 Type II disponible (Oui/Non/Inconnu)
- T : Date de renouvellement du contrat
- U : Disponibilité SLA % (99,9 %, 99,95 %, etc.)
- V : Clause de droit d'audit (Oui/Non)
- W : Clause de portabilité des données (Oui/Non)
- X : Support forensique/RI (Oui/Non/Limité)

## Classeur 3 : Configuration et déploiement sécurisés

**Identifiant du document :** ISMS-IMP-A.5.19-23.S3
**Nom de fichier :** `ISMS_REG_A523_3_Configuration_AAAAMMJJ.xlsx`
**Généré par :** `generate_reg_a523_3_secure_config.py`
**Parties prenantes :** Sécurité IT, DevOps, Administrateurs système
**Nombre d'onglets :** 11

**Objet :** Évaluer la conformité au référentiel de configuration de sécurité pour les services en nuage déployés.

**Onglets :**
1. Instructions et légende
2. Gestion des identités et des accès
3. Chiffrement des données (au repos et en transit)
4. Sécurité réseau et segmentation
5. Configuration de la journalisation et de la surveillance
6. Sauvegarde et reprise après sinistre
7. Étiquetage de la classification des données
8. Sécurité des API et intégrations
9. Tableau de bord
10. Registre des preuves
11. Validation

**Colonnes étendues (R-X) :**

- R : AMF activé (Oui/Non/Partiel)
- S : Chiffrement au repos (Oui/Non/Inconnu)
- T : Chiffrement en transit (TLS 1.3/TLS 1.2/Faible)
- U : Journalisation centralisée (Oui/Non/Partiel)
- V : Intégration SSO (Oui/Non/Prévu)
- W : Étiquettes de classification des données appliquées (Oui/Non/Partiel)
- X : Référentiel de configuration documenté (Oui/Non)

## Classeur 4 : Gouvernance continue et gestion des risques

**Identifiant du document :** ISMS-IMP-A.5.19-23.S4
**Nom de fichier :** `ISMS_REG_A523_4_Governance_AAAAMMJJ.xlsx`
**Généré par :** `generate_reg_a523_4_governance.py`
**Parties prenantes :** Direction IT, Gestion des risques, RSI
**Nombre d'onglets :** 11

**Objet :** Surveiller la gouvernance continue, les risques fournisseurs, la continuité d'activité et la gestion des modifications.

**Onglets :**
1. Instructions et légende
2. Sensibilisation et formation à la sécurité
3. Procédures de réponse aux incidents
4. Gestion des mises à jour de sécurité
5. Évaluation du verrouillage fournisseur
6. Évaluation de l'exclusion fournisseur
7. Planification de la continuité d'activité
8. Suivi de la gestion des modifications
9. Tableau de bord
10. Registre des preuves
11. Validation

**Colonnes étendues (R-X) :**

- R : Formation à la sécurité réalisée (Oui/Non + Date)
- S : Date de la dernière revue de sécurité
- T : Plan de réponse aux incidents testé (Oui/Non/Prévu)
- U : Risque de verrouillage fournisseur (Élevé/Moyen/Faible)
- V : Plan PCA/PRA existant (Oui/Non)
- W : Date du dernier test PCA/PRA
- X : Processus de gestion des modifications (Oui/Non)

---

# Architecture des scripts Python

## Structure des scripts (modèle standard)

Tous les scripts de génération suivent cette architecture modulaire :

```python
# ============================================================================
# SECTION 1 : CRÉATION DU CLASSEUR ET DÉFINITIONS DE STYLES
# ============================================================================
def create_workbook() -> Workbook:
    """Créer tous les onglets conformément à la spécification."""

def setup_styles() -> dict:
    """Définir les couleurs, polices, bordures (NOUVEAUX objets par cellule !)."""

# ============================================================================
# SECTION 2 : DÉFINITIONS DES COLONNES (BASE + ÉTENDUES)
# ============================================================================
def get_base_cloud_columns() -> dict:
    """Retourne les 17 colonnes standard (A-Q) pour TOUTES les évaluations cloud."""

def get_extended_columns_inventory() -> dict:
    """Retourne les colonnes R-X spécifiques au domaine pour l'inventaire."""

# ============================================================================
# SECTION 3 : DÉFINITIONS DES VALIDATIONS
# ============================================================================
def create_base_validations(ws) -> dict:
    """Créer les validations de liste déroulante pour les champs standard."""

def create_extended_validations(ws, sheet_type) -> dict:
    """Créer les listes déroulantes spécifiques au domaine."""

# ============================================================================
# SECTION 4 : DÉFINITIONS DES ÉLÉMENTS DE LISTE DE CONTRÔLE
# ============================================================================
def get_checklist_items(sheet_type) -> list:
    """Retourner la liste de contrôle de conformité spécifique au domaine."""

# ============================================================================
# SECTION 5 : DÉFINITIONS DES TABLES DE RÉFÉRENCE
# ============================================================================
def get_reference_tables(sheet_type) -> dict:
    """Retourner les tables de consultation (fournisseurs, régions, normes)."""

# ============================================================================
# SECTION 6 : CONSTRUCTEUR GÉNÉRIQUE D'ONGLET D'ÉVALUATION
# ============================================================================
def create_assessment_sheet(ws, styles, section_title, policy_ref,
                           question, sheet_type):
    """Constructeur universel — UNE SEULE fonction crée TOUS les onglets."""

# ============================================================================
# SECTION 7 : CRÉATEURS D'ONGLETS SPÉCIALISÉS
# ============================================================================
def create_instructions_sheet(ws, styles):
def create_summary_dashboard(ws, styles):
def create_evidence_register(ws, styles):
def create_approval_signoff(ws, styles):

# ============================================================================
# SECTION 8 : ONGLETS D'ÉVALUATION SPÉCIFIQUES AU DOMAINE
# ============================================================================
def create_1_saas_services(ws, styles):
def create_2_iaas_paas_services(ws, styles):
# etc.

# ============================================================================
# SECTION 9 : EXÉCUTION PRINCIPALE
# ============================================================================
def main():
    """Orchestrer la génération du classeur."""
```

## Notes d'implémentation critiques

**Bonne pratique pour les objets de style :**
```python
# ❌ À ÉVITER — Les objets partagés peuvent causer des problèmes de compatibilité Excel
border = Border(left=Side(style="thin"), ...)
cell1.border = border  # Référence 1
cell2.border = border  # Référence 2

# ✅ RECOMMANDÉ — Un nouvel objet par cellule garantit la compatibilité
def apply_border(cell):
    cell.border = Border(
        left=Side(style="thin"),
        right=Side(style="thin"),
        top=Side(style="thin"),
        bottom=Side(style="thin")
    )
```

**Justification d'implémentation :** La création de nouveaux objets de style pour chaque cellule prévient les avertissements potentiels de compatibilité Excel et assure une génération propre des classeurs.

---

# Validation et intégration

## Scripts de traitement

| Script | Objet | Quand exécuter |
|--------|-------|----------------|
| **generate_a523_1_inventory.py** | Génère le classeur S1 Inventaire des services en nuage | Avant le début du cycle d'évaluation |
| **generate_a523_2_vendor_dd.py** | Génère le classeur S2 Diligence raisonnable fournisseurs | Avant le début du cycle d'évaluation |
| **generate_a523_3_secure_config.py** | Génère le classeur S3 Configuration sécurisée | Avant le début du cycle d'évaluation |
| **generate_a523_4_governance.py** | Génère le classeur S4 Gouvernance continue | Avant le début du cycle d'évaluation |

## Processus de traitement

```
┌───────────────────────────────────────────────────────────────────┐
│ 1. Générer le classeur                                            │
│    $ python3 generate_reg_a523_1_inventory.py                     │
│    Sortie : ISMS_REG_A523_1_Inventory_20260115.xlsx               │
└───────────────────────────────────────────────────────────────────┘
                         ↓
┌───────────────────────────────────────────────────────────────────┐
│ 2. Distribuer aux parties prenantes                               │
│    - Envoyer à Opérations IT, Achats, Juridique                   │
│    - Délai : 2 semaines pour la complétion                        │
└───────────────────────────────────────────────────────────────────┘
                         ↓
┌───────────────────────────────────────────────────────────────────┐
│ 3. Réviser les tableaux de bord                                   │
│    Ouvrir chaque classeur complété et réviser l'onglet Tableau    │
│    de bord pour les métriques de conformité                       │
└───────────────────────────────────────────────────────────────────┘
```

---

# Intégration des tableaux de bord

## Agrégation pilotée par formules

```excel
# Exemple : Compter les services conformes depuis le classeur Inventaire
=COUNTIF('[ISMS_REG_A523_1_Inventory_20260115.xlsx]2. Services SaaS'!$H$8:$H$50,"✅*")

# Exemple : Calculer le pourcentage de conformité
=IF((B4-F4)=0,"0%",ROUND(C4/(B4-F4)*100,1)&"%")
```

**Avantages :**

- **Aucune mise à jour manuelle** — modifier l'évaluation → le tableau de bord se rafraîchit
- **Métriques en temps réel** — les parties prenantes voient le % de conformité en direct
- **Piste d'audit** — les formules indiquent exactement l'origine des données

## Visualisations du tableau de bord

**Tableau de synthèse de la conformité :**
| Domaine d'évaluation | Total | Conforme | Partiel | Non conforme | S.O. | % Conformité |
|---------------------|-------|----------|---------|-------------|------|-------------|
| Inventaire          | 78    | 45       | 18      | 15          | 0    | 57,7 %      |
| Diligence raisonnable | 78  | 62       | 10      | 6           | 0    | 79,5 %      |
| Configuration       | 156   | 98       | 35      | 23          | 0    | 63,2 %      |
| Gouvernance         | 78    | 51       | 20      | 7           | 0    | 65,4 %      |
| **TOTAL**           | **390** | **256** | **83** | **51**     | **0** | **65,6 %** |

**Carte de chaleur des risques :**

- Verrouillage fournisseur élevé + Faisabilité de sortie faible = 🔴 Risque critique
- Données restreintes + Résidence hors UE = 🔴 Violation de souveraineté
- Service critique + Absence de test PCA/PRA = 🟡 Risque élevé

---

# Cycle d'évaluation et processus

## Cycle d'évaluation trimestriel

```
Semaine 1 : GÉNÉRATION
├─ L'ingénierie sécurité exécute les générateurs Python
├─ Revue qualité des classeurs générés
└─ Distribution aux parties prenantes avec instructions

Semaines 2-3 : ÉVALUATION
├─ Opérations IT complète l'inventaire et la configuration
├─ Achats met à jour les données fournisseurs et contractuelles
├─ Juridique révise les clauses de conformité et de sortie
└─ Preuves collectées (contrats, certifications, captures d'écran)

Semaine 4 : RÉVISION
├─ Le RSI révise les évaluations complétées
├─ Analyse des écarts réalisée
├─ Priorités de correction attribuées
└─ Approbation du RSSI obtenue

Semaine 5 : INTÉGRATION
├─ Révision des tableaux de bord
├─ Synthèse exécutive générée
└─ Dossier de reporting pour le conseil préparé
```

## Déclencheurs d'évaluation ad hoc

Effectuer des évaluations en dehors du cycle trimestriel lors :

- **Intégration d'un nouveau service en nuage** (utiliser Classeurs 1 + 2)
- **Modifications majeures de configuration** (utiliser Classeur 3)
- **Incidents de sécurité** (utiliser Classeurs 4 + 5)
- **Renouvellements de contrats** (utiliser Classeur 2)
- **Préparation d'audit** (utiliser les 5 classeurs)

---

# Guide des parties prenantes

## Qui remplit quoi

| Classeur | Principal | Secondaire | Tertiaire |
|----------|-----------|-----------|----------|
| 1. Inventaire | Opérations IT | Achats | Finance |
| 2. Diligence raisonnable | Achats | Juridique | Conformité |
| 3. Configuration | Sécurité IT | DevOps | Admins système |
| 4. Gouvernance | Gestion des risques | RSI | Direction IT |
| 5. Tableau de bord | RSI | (Généré automatiquement) | RSSI |

## Instructions de complétion

**Pour chaque onglet d'évaluation :**
1. Remplir les **cellules jaunes** avec vos données
2. Utiliser les **menus déroulants** (ne pas saisir en texte libre)
3. Fournir l'**emplacement des preuves** (chemin de fichier, lien, identifiant de document)
4. Si Statut = Partiel/Non conforme :

   - Remplir la **Description de l'écart**
   - Indiquer **Correction nécessaire** = Oui
   - Assigner un **Responsable**
   - Définir une **Date cible**

5. Mettre à jour le **Registre des preuves** avec les documents justificatifs

**Exigences en preuves :**

- ✅ PDF de contrats (accords fournisseurs, SLA)
- ✅ Certifications de sécurité (ISO 27001, rapports SOC 2)
- ✅ Captures d'écran de configuration (paramètres AMF, chiffrement)
- ✅ Rapports d'audit (tests d'intrusion, analyses de vulnérabilités)
- ✅ Registres de formation (complétion de la sensibilisation à la sécurité)
- ✅ Résultats des tests PCA/PRA (dernier rapport d'exercice de reprise)
- ❌ « Nous avons un processus » (non acceptable sans preuve !)

## Critères de validation de l'évaluation

Une évaluation est **prête pour la validation RSI/RSSI** uniquement lorsque toutes les conditions suivantes sont remplies :

| Critère | Exigence |
|---------|----------|
| **Colonnes obligatoires complètes** | 100 % des colonnes A–Q (colonnes de base) renseignées pour chaque ligne ; les entrées S.O. nécessitent une justification documentée dans la Description de l'écart |
| **Emplacement des preuves spécifié** | Chaque ligne non-S.O. a un emplacement de preuves (chemin de fichier, URL SharePoint, identifiant de document ou référence contractuelle) — « à fournir » n'est pas acceptable |
| **Descriptions d'écarts précises** | Toutes les lignes Partielles ou Non conformes ont une Description de l'écart nommant le contrôle manquant spécifique ; les textes génériques (« À définir », « en cours de révision », « en cours ») ne sont pas acceptés |
| **Dates de correction réalistes** | Les Dates cibles sont des dates calendaires ≤ 12 mois à venir ; « DQAP » ou vide ne sont pas acceptés |
| **Responsable assigné** | Chaque écart ouvert a une personne nommée (pas une équipe ou un intitulé de poste), confirmée comme informée de sa mission |
| **Champs réglementaires complétés** | Si le service est applicable à DORA ou NIS2 (selon ISMS-POL-A.5.19-23 Section 12), les champs réglementaires correspondants sont renseignés |
| **Vérification ponctuelle réussie** | Le RSI effectue une vérification ponctuelle sur un échantillon aléatoire de 10 % des lignes (minimum 5 lignes) et confirme que les preuves sont accessibles et correspondent au statut déclaré |

**Processus de validation :**

1. L'évaluateur soumet le classeur complété au RSI via le système de gestion documentaire
2. Le RSI vérifie la complétude au regard de tous les critères ci-dessus
3. Critères satisfaits → le RSI signe l'onglet de validation et enregistre la date
4. Critères non satisfaits → le RSI retourne le classeur avec des notes de non-conformité spécifiques ; l'évaluateur dispose de 5 jours ouvrés pour corriger et resoumettre
5. Le RSSI valide tous les classeurs des fournisseurs de niveau 1 ; le RSI valide les niveaux 2 à 4

**Formats de preuves minimaux acceptables :**

| Type de preuve | Acceptable | Non acceptable |
|---------------|-----------|----------------|
| Contrat | PDF signé, lien SharePoint, identifiant de contrat dans le système de gestion | Fil d'e-mail, confirmation verbale |
| Certification | PDF du certificat actuel ou lien direct vers le registre public | Certificat expiré, auto-déclaration du fournisseur |
| Configuration | Capture d'écran avec date et nom du système visibles, ou fichier de configuration exporté | Description sans preuve |
| Audit/test d'intrusion | Rapport signé d'un organisme accrédité/agréé | Diapositive de synthèse, présentation exécutive |
| Formation | Relevé de complétion LMS avec noms et dates | « La formation a été dispensée » |

---

# Amélioration continue

## Processus d'amélioration du cadre

**Déclencheurs d'amélioration :**

- Constats d'audit
- Retours des parties prenantes
- Nouveaux types de services en nuage
- Évolutions réglementaires
- Évolution technologique

**Processus :**
1. Documenter le problème dans GitHub/Jira
2. Mettre à jour la spécification markdown
3. Régénérer le script Python
4. Tester les classeurs générés
5. Mettre à jour le présent document S6
6. Communiquer les changements aux parties prenantes

## Métriques de qualité

**Indicateurs de santé du cadre :**

- ✅ Temps de génération < 2 heures (les 5 classeurs)
- ✅ Taux de complétion des parties prenantes > 80 % (sous 2 semaines)
- ✅ Taux d'erreur < 5 % dans les évaluations complétées
- ✅ Zéro constat critique lors des revues d'audit
- ✅ Mises à jour trimestrielles du cadre réalisées dans les délais

---

# Informations de référence

## Documents connexes

**Couche politique :**

- ISMS-POL-A.5.19-23 (Index principal)
- ISMS-POL-A.5.19-23-S5 (Exigences de sécurité des services en nuage)

**Spécifications d'évaluation :**

- ISMS-IMP-A.5.19-23.S1 — Spécification Inventaire et classification
- ISMS-IMP-A.5.19-23.S2 — Spécification Diligence raisonnable fournisseurs
- ISMS-IMP-A.5.19-23.S3 — Spécification Configuration sécurisée
- ISMS-IMP-A.5.19-23.S4 — Spécification Gouvernance continue

**Scripts de génération :**

- generate_reg_a523_1_inventory.py
- generate_reg_a523_2_vendor_dd.py
- generate_reg_a523_3_secure_config.py
- generate_reg_a523_4_governance.py

## Normes externes

- ISO/IEC 27001:2022 — Contrôle A.5.23
- ISO/IEC 27002:2022 — Lignes directrices pour la sécurité cloud
- ISO/IEC 27017:2026 — Contrôles spécifiques au cloud
- ISO/IEC 27018:2025 — DCP dans les clouds publics
- NIST SP 800-144 — Lignes directrices sur la sécurité et la confidentialité dans le cloud public
- CSA Cloud Controls Matrix (CCM) v4

---

# Annexe A : Référence rapide

## Aide-mémoire d'exécution des scripts

```bash
# Générer tous les classeurs d'évaluation
python3 generate_reg_a523_1_inventory.py
python3 generate_reg_a523_2_vendor_dd.py
python3 generate_reg_a523_3_secure_config.py
python3 generate_reg_a523_4_governance.py

# Réviser les tableaux de bord
```

---

**FIN DU DOCUMENT**

*« Le premier principe est que vous ne devez pas vous tromper vous-même — et vous êtes la personne la plus facile à tromper. »*
*— Richard Feynman*

**Traduction SMSI :** La conformité fondée sur des preuves prévient le cloud washing !
<!-- QA_VERIFIED: 2026-03-30 -->
