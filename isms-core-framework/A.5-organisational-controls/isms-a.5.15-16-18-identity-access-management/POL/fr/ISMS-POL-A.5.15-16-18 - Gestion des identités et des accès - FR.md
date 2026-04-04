<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.15-16-18-FR:framework:POL:a.5.15-16-18 -->
**ISMS-POL-A.5.15-16-18 — Gestion des identités et des accès**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Politique de gestion des identités et des accès |
| **Type de document** | Politique |
| **Identifiant du document** | ISMS-POL-A.5.15-16-18 |
| **Créateur du document** | Responsable de la sécurité des systèmes d'information (RSSI) |
| **Propriétaire du document** | Directeur général (DG) |
| **Approuvé par** | Direction générale |
| **Date de création** | [Date] |
| **Version** | 1.0 |
| **Date de version** | [À définir] |
| **Classification** | Interne |
| **Statut** | Projet |

**Historique des versions** :

| Version | Date | Auteur | Modifications |
|---------|------|--------|---------------|
| 1.0 | [Date] | RSSI | Politique initiale pour la première certification ISO 27001:2022 |

**Cycle de révision** : Annuel
**Prochaine date de révision** : [Date d'entrée en vigueur + 12 mois]

**Chaîne d'approbation** :

- Principal : Responsable de la sécurité des systèmes d'information (RSSI)
- Secondaire : Directeur des systèmes d'information (DSI)
- Intégration RH : Directeur des ressources humaines (DRH)
- Conformité : Responsable juridique/conformité
- Autorité finale : Direction générale

**Documents connexes** :

- ISMS-POL-00 (Cadre d'applicabilité réglementaire)
- ISMS-IMP-A.5.15-16-18.S1-UG/TG (Évaluation de la conformité du cycle de vie et de l'inventaire des utilisateurs)
- ISMS-IMP-A.5.15-16-18.S2-UG/TG (Évaluation de la matrice des droits d'accès)
- ISMS-IMP-A.5.15-16-18.S3-UG/TG (Évaluation des résultats de la revue des accès)
- ISMS-IMP-A.5.15-16-18.S4-UG/TG (Évaluation de la définition des rôles et de la conformité SdF)
- ISMS-POL-A.8.2-3-5 (Authentification et accès privilégié)
- ISO/IEC 27001:2022 Contrôles A.5.15, A.5.16, A.5.18

---

## Résumé exécutif

La présente politique établit les exigences de [Organisation] en matière de contrôles de gestion des identités et des accès afin de garantir une gouvernance appropriée des accès tout au long du cycle de vie complet des identités, conformément aux contrôles ISO/IEC 27001:2022 A.5.15, A.5.16 et A.5.18.

**Objet** : Définir les exigences organisationnelles de gouvernance de la gestion des identités et des accès (GIA). La présente politique établit QUELS contrôles GIA sont requis et QUI en est responsable. Les procédures de mise en œuvre (COMMENT) sont documentées séparément dans ISMS-IMP-A.5.15-16-18 (variantes UG/TG).

**Périmètre** : La présente politique s'applique à toutes les identités (employés, prestataires, fournisseurs, comptes de service), à tous les systèmes d'identité et à tous les types d'accès, quel que soit le modèle de déploiement ou la technologie.

**Approche combinée des contrôles** : Ces trois contrôles sont mis en œuvre comme un cadre unifié car ils traitent d'aspects indissociables de la gouvernance des identités et des accès.

**Alignement réglementaire** : La présente politique répond aux exigences de conformité obligatoires visées par ISMS-POL-00, notamment la nLPD suisse, le RGPD de l'UE et la norme ISO/IEC 27001:2022.

---

# Périmètre et alignement des contrôles

## Contrôles ISO/IEC 27001:2022

**A.5.15 — Contrôle d'accès** : Des règles pour contrôler l'accès physique et logique aux informations et autres actifs associés devraient être établies et mises en œuvre sur la base des exigences métier et de sécurité de l'information.

**A.5.16 — Gestion des identités** : Le cycle de vie complet des identités devrait être géré.

**A.5.18 — Droits d'accès** : Les droits d'accès aux informations et autres actifs associés devraient être provisionnés, révisés, modifiés et supprimés conformément à la politique et aux règles thématiques de contrôle d'accès de l'organisation.

## Périmètre de la politique

**La présente politique s'applique à** :

| Catégorie | Périmètre |
|-----------|-----------|
| **Types d'utilisateurs** | Employés, prestataires, fournisseurs, comptes de service, comptes partagés (avec approbation), comptes d'urgence |
| **Systèmes d'identité** | Active Directory, Azure AD/Entra ID, Okta, Google Workspace, LDAP et tout système d'identité utilisé par [Organisation] |
| **Types d'accès** | Accès applicatif, système, données, réseau et accès administratif/privilégié |
| **Personnel** | Équipe GIA, équipe sécurité, équipe RH, exploitation informatique, responsables hiérarchiques, propriétaires de systèmes, tous les employés |

**La présente politique ne s'applique PAS à** :

- Les systèmes de contrôle d'accès physique (couvert par A.7.2)
- Les mécanismes d'authentification (couverts par A.8.5)
- La mise en œuvre de la gestion des accès privilégiés (couverte par A.8.2)

## Applicabilité réglementaire

**Niveau 1 — Conformité obligatoire** (Toutes les opérations) :

| Règlementation | Exigences GIA principales |
|----------------|--------------------------|
| **nLPD suisse** | Article 8 — Mesures techniques et organisationnelles pour le contrôle d'accès |
| **RGPD UE** | Article 32 — Sécurité du traitement incluant les contrôles d'accès |
| **ISO/IEC 27001:2022** | Contrôles A.5.15, A.5.16, A.5.18 |

**Niveau 2 — Applicabilité conditionnelle** (Déclenchée par les activités commerciales) :

- **FINMA** : Si [Organisation] détient une licence FINMA (Circulaire 2023/1 Chiffres 50-62)
- **DORA** : Si [Organisation] est une entité financière de l'UE (Articles 6, 28-30)
- **NIS2** : Si [Organisation] est une entité essentielle ou importante (Article 21)
- **PCI DSS v4.0.1** : Si [Organisation] traite des données de cartes de paiement (Exigences 7, 8)

Détermination de la conformité conformément à ISMS-POL-00 (Cadre d'applicabilité réglementaire).

---

# Énoncés de politique

## Exigences de contrôle d'accès (A.5.15)

### Principes de contrôle d'accès

[Organisation] DOIT mettre en œuvre des contrôles d'accès fondés sur les principes suivants :

| Principe | Exigence |
|----------|----------|
| **Moindre privilège** | Les utilisateurs bénéficient de l'accès minimum requis pour leur fonction |
| **Besoin d'en connaître** | Accès restreint à un besoin commercial documenté |
| **Séparation des fonctions** | Les responsabilités conflictuelles sont séparées pour prévenir la fraude et les erreurs |
| **Défense en profondeur** | Plusieurs couches de contrôle d'accès mises en œuvre |
| **Refus par défaut** | L'accès est refusé sauf octroi explicite avec approbation |

### Classification des accès

[Organisation] DOIT classifier les accès selon :

| Dimension | Classifications |
|-----------|----------------|
| **Type d'utilisateur** | Employé, prestataire (limité dans le temps), fournisseur (externe), compte de service (non humain), partagé (exceptionnel), urgence (brise-glace) |
| **Criticité du système** | Critique, élevée, moyenne, faible |
| **Sensibilité des données** | Restreint, confidentiel, interne, public |
| **Niveau d'accès** | Lecture, écriture, administrateur, privilégié |

Les critères de classification sont définis dans ISMS-IMP-A.5.15-16-18.1.

### Justification commerciale et approbation

Toutes les demandes d'accès DOIVENT inclure une justification commerciale documentée avec une autorité d'approbation basée sur le type d'accès :

| Type d'accès | Autorité d'approbation |
|--------------|------------------------|
| **Accès utilisateur standard** | Responsable hiérarchique direct |
| **Accès système sensible** | Propriétaire du système + Responsable hiérarchique |
| **Données confidentielles/restreintes** | Propriétaire des données + RSSI |
| **Accès privilégié/administrateur** | RSSI + DSI |
| **Accès fournisseur tiers** | Sponsor métier + RSSI |
| **Compte partagé** (exceptionnel) | RSSI avec contrôles compensatoires |

### Séparation des fonctions

[Organisation] DOIT maintenir une matrice de séparation des fonctions (SdF) identifiant les combinaisons de rôles incompatibles (documentée dans ISMS-IMP-A.5.15-16-18.3 Annexe A ou [Module SdF de la plateforme GRC]). Les violations de SdF nécessitent des exceptions approuvées par le RSSI avec des contrôles compensatoires (consignées dans le registre des exceptions conformément à la Section 4.2).

La détection des violations de SdF DOIT avoir lieu mensuellement (automatisée via un script de vérification SdF) avec rapport à l'équipe sécurité (résultats dans IAM-SoD-Workbook-[AAAA-MM]). Les violations DOIVENT être corrigées dans les 30 jours ouvrés ou consignées comme exceptions avec approbation du RSSI.

### Intégration RH

Le contrôle d'accès DOIT s'intégrer aux événements du cycle de vie RH :

| Événement RH | Action sur les accès | Délai |
|--------------|---------------------|-------|
| **Nouvelle embauche** | Déclencher le processus d'arrivée | Accès prêt à la date de démarrage |
| **Changement de poste** | Déclencher le processus de mobilité | Dans les 2 jours ouvrés |
| **Fin de contrat** | Déclencher le processus de départ | Immédiat (pour faute) ou le même jour ouvré |
| **Expiration de contrat** | Supprimer l'accès du prestataire | À la date d'expiration du contrat |

Le système RH est désigné comme source faisant autorité pour les événements du cycle de vie des identités.

---

## Exigences de gestion des identités (A.5.16)

### Cadre du cycle de vie des identités

[Organisation] DOIT gérer les identités via des processus de cycle de vie standardisés :

| Processus | Déclencheur | Délai | Responsabilité |
|-----------|-------------|-------|----------------|
| **Arrivée** | Notification RH de nouvelle embauche/prestataire | Accès prêt à la date de démarrage | RH déclenche, équipe GIA crée, informatique provisionne |
| **Mobilité** | Notification RH de changement de poste | Dans les 2 jours ouvrés | RH déclenche, responsable approuve, équipe GIA met à jour |
| **Départ** | Notification RH de fin de contrat | Immédiat au même jour ouvré | RH déclenche, équipe GIA désactive, informatique vérifie |

Les procédures détaillées sont documentées dans ISMS-IMP-A.5.15-16-18.2.

### Exigences par type de compte

| Type de compte | Exigences |
|----------------|-----------|
| **Employé** | Permanent jusqu'à la fin du contrat, responsabilité individuelle |
| **Prestataire/Fournisseur** | Limité dans le temps avec expiration obligatoire (appliquée par le système via la date d'expiration du compte définie lors du provisionnement), sponsor interne requis (renouvelé trimestriellement avec approbation du sponsor ou déprovisionnement automatique) |
| **Compte de service** | Propriétaire documenté (maintenu dans le [système GIA/plateforme GRC]), rotation des mots de passe (trimestrielle au minimum, vérifiée via scan automatisé ou attestation manuelle), contrôles d'accès privilégié conformément à A.8.2, non-conformité signalée dans l'évaluation GIA mensuelle |
| **Compte partagé** | Approbation du RSSI requise (documentée dans le registre des exceptions conformément à la Section 4.2), contrôles compensatoires obligatoires (journalisation individuelle via [SIEM/système d'audit], surveillance des accès privilégiés conformément à A.8.2, revue trimestrielle par le RSSI), fortement déconseillé (objectif : zéro compte partagé ou exception formellement approuvée par le RSSI avec justification commerciale pour chacun), approbation limitée dans le temps (revalidation annuelle requise) |
| **Urgence/Brise-glace** | Dormant jusqu'à un scénario de catastrophe, double autorisation, utilisation déclenche une alerte (testé semestriellement conformément aux procédures PCA, utilisation de test documentée) |

### Gestion des comptes orphelins

[Organisation] DOIT détecter et corriger les comptes orphelins :

- **Détection** : Recoupement mensuel des systèmes d'identité avec le système RH
- **Correction** : Séquence investigation, notification, désactivation, suppression dans les 30 jours
- **Exceptions** : Approbation du RSSI requise avec justification documentée

---

## Exigences relatives aux droits d'accès (A.5.18)

### Attribution des droits d'accès

[Organisation] DOIT attribuer les droits d'accès via :

- Flux de demande et d'approbation documenté
- Contrôle d'accès basé sur les rôles (RBAC) comme méthode privilégiée
- Justification commerciale documentée pour tous les octrois d'accès
- Piste d'audit maintenue (demandeur, approbateur, horodatage, justification)

**Délais de provisionnement** :

| Type de demande | SLA |
|-----------------|-----|
| **Accès standard** | Dans les 2 jours ouvrés |
| **Accès sensible** | Dans les 5 jours ouvrés |
| **Accès d'urgence** | Dans les 4 heures |

### Contrôle d'accès basé sur les rôles

[Organisation] DOIT mettre en œuvre le RBAC :

- **Catalogue de rôles** : Maintenu par l'équipe GIA dans le [Plateforme GRC/Système GIA], mis à jour dans les 10 jours ouvrés suivant les changements organisationnels
- **Propriété des rôles** : Chaque rôle attribué à un propriétaire métier (documenté dans la définition du rôle)
- **Cycle de vie des rôles** : Les nouveaux rôles nécessitent l'approbation de l'équipe GIA, les modifications nécessitent l'approbation du propriétaire métier, les rôles obsolètes sont archivés (non supprimés) pour la piste d'audit
- Rôles mappés à des droits d'accès spécifiques (matrice des droits d'accès documentée dans ISMS-IMP-A.5.15-16-18.3)
- Objectif : 80 % ou plus des utilisateurs affectés via des rôles plutôt que par accès direct
- Revue annuelle des rôles par les propriétaires métier (suivie dans la [Plateforme GRC], achèvement requis au T1 annuellement)

### Revue et recertification des accès

[Organisation] DOIT réviser les droits d'accès périodiquement :

| Classification | Fréquence | Réviseur |
|----------------|-----------|----------|
| **Systèmes critiques / Accès privilégié** | Trimestrielle | RSSI + Équipe sécurité |
| **Systèmes à risque élevé / Données confidentielles** | Semestrielle | Propriétaires de systèmes + Responsables hiérarchiques |
| **Systèmes standard / Données internes** | Annuelle | Responsables hiérarchiques |
| **Accès tiers/fournisseurs** | Trimestrielle | Sponsor métier + RSSI |

Les revues d'accès tiers incluent la validation que l'accord contractuel reste actif et que l'accès reste nécessaire conformément à A.5.20.

Les réviseurs DOIVENT certifier que l'accès est approprié ou demander sa suppression. L'accès inapproprié DOIT être supprimé dans les 5 jours ouvrés.

**Suivi des revues d'accès** :

Si l'accès inapproprié ne peut être supprimé dans les 5 jours ouvrés en raison de contraintes techniques :

- Le responsable hiérarchique DOIT documenter la justification et les contrôles compensatoires dans la [plateforme GRC]
- Approbation du RSSI requise pour les exceptions > 10 jours ouvrés
- Les suppressions en attente sont escaladées au DSI après 15 jours ouvrés
- La non-conformité prolongée (> 30 jours) est signalée comme incident de sécurité conformément à A.5.24-27

### Suppression des accès

[Organisation] DOIT supprimer les accès rapidement :

| Déclencheur | Délai |
|-------------|-------|
| **Fin de contrat pour faute** | Immédiat (dans l'heure) |
| **Départ volontaire** | Le même jour ouvré |
| **Changement de poste** | Dans les 2 jours ouvrés (supprimer l'accès du rôle précédent) |
| **Constatation de revue d'accès** | Dans les 5 jours ouvrés |
| **Incident de sécurité** | Immédiat |

### Prévention de la dérive des privilèges

[Organisation] DOIT détecter et corriger la dérive des privilèges via :

**Méthodologie de détection** :

| Méthode de détection | Fréquence | Outil/Processus | Responsable |
|----------------------|-----------|-----------------|-------------|
| **Analyse des écarts basée sur les rôles** | Trimestrielle | Le [Système GIA/Plateforme GRC] compare l'accès réel aux droits du rôle | Équipe GIA |
| **Audit du processus de mobilité** | Mensuel | Revue des changements de poste pour vérifier la suppression des accès précédents | Équipe sécurité |
| **Revue des droits d'accès directs** | Semestrielle | Revue par le responsable de tous les octrois d'accès directs (hors rôle) | Responsables hiérarchiques |
| **Audit des accès privilégiés** | Trimestrielle | Analyse des octrois d'accès privilégiés par rapport au besoin documenté | RSSI |

**Déclencheurs de détection** :

- L'utilisateur dispose de > 20 % de droits d'accès en plus par rapport à la définition du rôle (signalé pour revue)
- L'utilisateur conserve un accès provenant d'un rôle précédent > 30 jours après un événement de mobilité
- L'utilisateur dispose de > 3 octrois d'accès directs en dehors des affectations basées sur les rôles
- Le compte de service a accès au-delà de son périmètre documenté

**Processus de correction** :

1. L'excès d'accès est identifié et consigné dans le [plateforme GRC/système GIA]
2. Le responsable est notifié avec 5 jours ouvrés pour justifier ou approuver la suppression
3. L'accès non justifié est supprimé dans les 10 jours ouvrés suivant l'identification
4. La dérive récurrente (> 2 occurrences) déclenche une revue d'amélioration des processus

**Rapports** : Les indicateurs de dérive des privilèges figurent dans le tableau de bord mensuel de gouvernance GIA (nombre de constatations, délai moyen de correction, départements récidivistes)

---

# Rôles et responsabilités

| Rôle | Imputabilité |
|------|-------------|
| **Direction générale** | Efficacité globale du programme GIA, approbation de la politique, allocation des ressources |
| **RSSI** | Mise en œuvre et conformité de la politique GIA, approbation des exceptions, revue mensuelle des indicateurs |
| **DSI** | Infrastructure technique GIA, sélection technologique, allocation des ressources informatiques |
| **DRH** | Système RH comme source faisant autorité pour les identités, déclenchement des événements arrivée/mobilité/départ |
| **Équipe sécurité** | Développement de la politique, surveillance de la conformité, investigation des incidents, évaluations |
| **Équipe GIA** | Processus du cycle de vie des identités, maintenance des systèmes d'identité, détection des comptes orphelins |
| **Équipe RH** | Notifications arrivée/mobilité/départ, maintenance des données employés exactes |
| **Exploitation informatique** | Provisionnement/déprovisionnement des accès, mise en œuvre technique |
| **Responsables hiérarchiques** | Approbation des accès pour les collaborateurs directs, revues d'accès, notification de fin de contrat |
| **Propriétaires de systèmes** | Définition des exigences d'accès, revues d'accès spécifiques aux systèmes, approbation pour les systèmes sensibles |
| **Audit interne** | Vérification de l'efficacité des contrôles GIA, tests de conformité |
| **Tout le personnel** | Demander des accès uniquement avec besoin commercial, utiliser les accès de manière appropriée, signaler toute activité suspecte |

La matrice RACI détaillée est documentée dans ISMS-IMP-A.5.15-16-18.1.

---

# Gouvernance et conformité

## Cadre d'évaluation

[Organisation] DOIT vérifier l'efficacité des contrôles GIA via :

| Évaluation | Fréquence | Responsable | Emplacement des preuves |
|------------|-----------|-------------|------------------------|
| Conformité du cycle de vie et de l'inventaire des utilisateurs | Mensuelle | Équipe GIA | IAM-Workbook-[AAAA-MM] (automatisé) |
| Matrice des droits d'accès | Mensuelle | Équipe GIA | [Export plateforme GRC/système GIA] |
| Résultats des revues d'accès | Trimestrielle | Équipe sécurité | [Système de tickets], résumé trimestriel au RSSI |
| Conformité des rôles et SdF | Trimestrielle | Équipe GIA | IAM-SoD-Workbook-[AAAA-MM] (automatisé) |
| Tableau de bord de gouvernance GIA | Mensuel | Équipe sécurité | [Outil de BI/SharePoint] |

**Génération et conservation des preuves** :

- Conformité du cycle de vie et de l'inventaire des utilisateurs : Généré par script Python, résultats conservés dans IAM-Workbook-[AAAA-MM]
- Matrice des droits d'accès : Maintenue dans le [Plateforme GRC/système GIA], exportée mensuellement pour revue par l'équipe sécurité
- Résultats des revues d'accès : Suivis dans le [Système de tickets], rapport de synthèse trimestriel au RSSI documentant le taux d'achèvement et la suppression des accès inappropriés
- Conformité des rôles et SdF : Généré par script Python, violations consignées dans le registre des exceptions, résultats dans IAM-SoD-Workbook-[AAAA-MM]
- Tableau de bord de gouvernance GIA : Mis à jour mensuellement par l'équipe sécurité avec les KPI (voir Indicateurs de gouvernance ci-dessous)

Toutes les preuves d'évaluation DOIVENT être conservées pendant 24 mois minimum conformément à A.5.33 (Protection des enregistrements).

**Détection des défaillances de contrôle** :

- **Revues d'accès manquées** : L'équipe GIA suit l'achèvement des revues dans la [plateforme GRC], escalade les revues en retard au RSSI après 10 jours ouvrés
- **Comptes orphelins non détectés** : L'équipe sécurité échantillonne les rapports mensuels de comptes orphelins pour l'assurance qualité (échantillon minimum de 10 %)
- **Violations SdF non corrigées** : Le registre des exceptions suit les violations SdF ouvertes, revue trimestrielle par le RSSI signalant les éléments périmés (> 90 jours sans avancement)
- **Dépassements de SLA de provisionnement/déprovisionnement** : Le [système de tickets] signale automatiquement les dépassements de SLA, rapport mensuel au DSI avec analyse des causes profondes pour les dépassements récurrents
- **Non-conformité de l'âge des mots de passe des comptes de service** : Le scan automatisé signale les comptes avec des mots de passe de > 90 jours, rapport à l'équipe GIA pour correction dans les 15 jours ouvrés

Les événements de défaillance de contrôle DOIVENT être consignés comme incidents conformément à ISMS-POL-A.5.24-27 (Gestion des incidents) lorsqu'ils créent un risque de sécurité.

**Suivi de la correction des écarts** :

Les constatations des évaluations GIA (comptes orphelins, insuffisances de revue des accès, violations SdF, retards de provisionnement, non-conformité des comptes de service) DOIVENT être :

- Consignées dans le [registre central des écarts/plateforme GRC] dans les 5 jours ouvrés suivant leur identification
- Attribuées à un responsable (équipe GIA, responsable hiérarchique, propriétaire de système selon le type de constatation)
- Suivies avec des dates de correction cibles basées sur le risque :
  - Critique (risque de sécurité immédiat) : 5 jours ouvrés
  - Élevé (défaillance de contrôle) : 15 jours ouvrés
  - Moyen (faiblesse de contrôle) : 30 jours ouvrés
  - Faible (opportunité d'optimisation) : 90 jours ouvrés
- Revues mensuellement par l'équipe sécurité pour vérification de clôture
- Escaladées au RSSI si la correction est en retard de > 30 jours au-delà de la date cible

**Indicateurs de gouvernance GIA (tableau de bord mensuel)** :

- Nombre de comptes orphelins et délai moyen de correction (objectif : < 10 comptes, < 30 jours de correction)
- Taux d'achèvement des revues d'accès par type (objectif : 100 % dans la période de revue)
- Taux de conformité au SLA de provisionnement/déprovisionnement (objectif : > 95 %)
- Taux d'adoption du RBAC (pourcentage d'utilisateurs affectés via des rôles par rapport à l'accès direct, objectif : > 80 %)
- Nombre de violations SdF et statut d'approbation des exceptions (objectif : < 5 violations ouvertes, toutes avec exceptions approuvées par le RSSI)
- Taux de conformité de l'âge des mots de passe des comptes de service (objectif : > 95 % rotation dans les 90 jours)
- Statut de correction des écarts GIA (constatations ouvertes par âge et niveau de risque)

Indicateurs revus mensuellement par l'équipe sécurité, trimestriellement par le RSSI, intégrés à la revue de direction conformément à la Clause 9.3.

Les procédures d'évaluation sont documentées dans ISMS-IMP-A.5.15-16-18.5.

## Gestion des exceptions

Les exceptions à la politique GIA nécessitent :

- Justification commerciale documentée
- Évaluation du risque par l'équipe sécurité
- Approbation du RSSI avec contrôles compensatoires
- Documentation dans le registre des exceptions
- Revue annuelle de la nécessité continue

Les procédures de demande d'exception sont documentées dans ISMS-IMP-A.5.15-16-18.1.

## Réponse aux incidents

Les incidents liés à la GIA (compromission de compte, exploitation de compte orphelin, élévation de privilèges) DOIVENT être gérés conformément à ISMS-POL-A.5.24-27 (Gestion des incidents).

Le déprovisionnement d'urgence DOIT avoir lieu dans l'heure pour les incidents de sécurité.

## Révision de la politique

La présente politique DOIT être révisée :

- **Annuellement** (obligatoire)
- **En cas de déclencheur** : modifications réglementaires, changements organisationnels, évolutions technologiques, constatations d'audit, modifications de l'appréciation du risque ou retours d'expérience d'incidents

Les modifications de politique nécessitent l'approbation du RSSI ; les révisions majeures nécessitent l'approbation de la direction générale.

---

# Intégration SMSI

## Déclaration d'applicabilité

| Contrôle | Statut | Référence de mise en œuvre |
|----------|--------|---------------------------|
| **A.5.15 — Contrôle d'accès** | Applicable | Section 2.1, ISMS-IMP-A.5.15-16-18.1-UG/TG |
| **A.5.16 — Gestion des identités** | Applicable | Section 2.2, ISMS-IMP-A.5.15-16-18.2-UG/TG |
| **A.5.18 — Droits d'accès** | Applicable | Section 2.3, ISMS-IMP-A.5.15-16-18.3/4 |

## Contrôles connexes

- **A.8.2** (Droits d'accès privilégiés) : La GIA définit les utilisateurs privilégiés, A.8.2 met en œuvre PAM
- **A.8.5** (Authentification sécurisée) : La GIA crée les identités, A.8.5 les authentifie
- **A.5.24-27** (Gestion des incidents) : Les incidents de compromission de compte gérés conformément au cadre des incidents

## Ressources de mise en œuvre

| Document | Objet |
|----------|-------|
| **ISMS-IMP-A.5.15-16-18.1-UG/TG** | Gouvernance du contrôle d'accès |
| **ISMS-IMP-A.5.15-16-18.2-UG/TG** | Processus du cycle de vie des identités |
| **ISMS-IMP-A.5.15-16-18.3-UG/TG** | Définition et affectation des rôles |
| **ISMS-IMP-A.5.15-16-18.4-UG/TG** | Processus de revue des accès |
| **ISMS-IMP-A.5.15-16-18.5-UG/TG** | Procédures d'évaluation GIA |

---

# Définitions

| Terme | Définition |
|-------|------------|
| **Identité** | Représentation numérique d'un utilisateur (personne, service, appareil) avec identifiant unique |
| **Contrôle d'accès** | Technique de sécurité régissant qui peut consulter ou utiliser des ressources |
| **RBAC** | Modèle de contrôle d'accès dans lequel les autorisations sont attribuées à des rôles plutôt qu'à des individus |
| **Moindre privilège** | Principe exigeant l'accès minimum nécessaire pour la fonction |
| **Séparation des fonctions** | Pratique consistant à diviser les tâches critiques pour prévenir la fraude et les erreurs |
| **Processus d'arrivée** | Intégration de nouveaux utilisateurs incluant la création de compte et le provisionnement des accès |
| **Processus de mobilité** | Gestion des changements de poste incluant l'ajustement des accès |
| **Processus de départ** | Désinscription incluant la désactivation du compte et la suppression des accès |
| **Compte orphelin** | Compte sans propriétaire commercial valide nécessitant une correction |
| **Dérive des privilèges** | Accumulation de droits d'accès excessifs au fil du temps lors de changements de poste |
| **Compte de service** | Compte non humain utilisé pour des processus automatisés |
| **Compte brise-glace** | Compte privilégié d'urgence pour les scénarios de catastrophe |

---

# Registre d'approbation

| Rôle | Nom | Date |
|------|-----|------|
| **Responsable de la sécurité des systèmes d'information (RSSI)** | [Nom] | [Date à définir] |
| **Directeur des systèmes d'information (DSI)** | [Nom] | [Date à définir] |
| **Directeur des ressources humaines (DRH)** | [Nom] | [Date à définir] |
| **Responsable juridique/conformité** | [Nom] | [Date à définir] |
| **Direction générale** | [Nom] | [Date à définir] |

---

# Preuves pour cette politique

**Preuves d'étape 1 (revue de la documentation) :**

Preuves requises pour démontrer que la présente politique est correctement documentée et approuvée :

- ✅ Ce document de politique (ISMS-POL-A.5.15-16-18 v1.0)
- ✅ Signatures d'approbation du RSSI, DSI, DRH, Responsable juridique/conformité, Direction générale (Registre d'approbation)
- ✅ Principes de contrôle d'accès et cadre de classification définis (Section 2.1)
- ✅ Cadre du cycle de vie des identités (Arrivée/Mobilité/Départ) documenté (Section 2.2)
- ✅ Exigences par type de compte spécifiées (employé, prestataire, service, partagé, urgence) (Section 2.2)
- ✅ Attribution des droits d'accès et cadre RBAC documentés (Section 2.3)
- ✅ Fréquence et critères de revue des accès spécifiés (Section 2.3)
- ✅ Exigences de séparation des fonctions définies (Section 2.1)
- ✅ Méthodologie de détection de la dérive des privilèges documentée (Section 2.3)
- ✅ Rôles et responsabilités attribués avec référence RACI (Section 3)
- ✅ Cadre de gouvernance avec calendrier d'évaluation défini (Section 4)
- ✅ Intégration avec les contrôles connexes documentée (Section 5)

**Preuves d'étape 2 (efficacité opérationnelle) :**

Preuves requises pour démontrer l'efficacité opérationnelle de la présente politique :

- **Rapports d'inventaire des utilisateurs** : IAM-Workbook-[AAAA-MM] mensuel montrant les identités actives, les types de comptes et le statut du cycle de vie
- **Registres d'achèvement des revues d'accès** : Journaux de revue trimestriels/semestriels/annuels dans le [Système de tickets] montrant le réviseur, la décision, l'horodatage pour tous les accès dans le périmètre
- **Enregistrements du processus Arrivée/Mobilité/Départ** : Tickets de flux de travail déclenchés par RH démontrant la conformité au SLA (accès prêt à la date de démarrage, mobilité 2 jours, départ le jour même)
- **Journaux de correction de comptes orphelins** : Rapports de détection mensuels avec horodatages d'investigation, désactivation, suppression montrant une correction < 30 jours
- **Rapports de séparation des fonctions** : IAM-SoD-Workbook-[AAAA-MM] montrant les vérifications SdF, violations identifiées et approbations d'exceptions
- **Analyse de la dérive des privilèges** : Rapports d'écarts trimestriels comparant les droits réels aux droits du rôle, avec suivi des corrections
- **Tableau de bord de gouvernance GIA** : Indicateurs mensuels (nombre de comptes orphelins, taux d'achèvement des revues, conformité SLA, taux d'adoption RBAC, violations SdF, conformité des mots de passe)
- **Registre des exceptions** : Exceptions documentées avec justification commerciale, approbation du RSSI, contrôles compensatoires et revalidation annuelle
- **Conformité des comptes de service** : Attestation trimestrielle montrant les propriétaires documentés et la conformité de rotation des mots de passe (> 95 % dans les 90 jours)
- **Vérification de suppression des accès** : Piste d'audit de déprovisionnement montrant les horodatages fin de contrat-désactivation conformes aux SLA de la politique
- **Revues d'accès tiers** : Attestations trimestrielles des sponsors confirmant la nécessité commerciale continue et les accords contractuels actifs
- **Résultats des cahiers d'évaluation** : Cahiers d'évaluation ISMS-IMP-A.5.15-16-18.5 complétés démontrant les tests d'efficacité des contrôles

## Clarification sur les preuves de conformité

La présente politique établit les **exigences de gouvernance de la gestion des identités et des accès** couvrant les principes de contrôle d'accès, les processus du cycle de vie des identités et la gestion des droits d'accès pour tous les types d'utilisateurs et systèmes.

Elle n'établit **PAS** :
- Les **contrôles d'accès physique** (traités dans ISMS-POL-A.7.2 — Contrôle d'accès physique)
- Les **mécanismes d'authentification** (traités dans ISMS-POL-A.8.5 — Authentification sécurisée)
- La **mise en œuvre de la gestion des accès privilégiés** (traitée dans ISMS-POL-A.8.2 — Droits d'accès privilégiés)
- Les **configurations spécifiques des systèmes d'identité** (décisions technologiques organisationnelles, documentées dans les procédures IMP)

La délimitation est la suivante : **La présente politique définit QUI obtient QUEL accès, QUAND et COMMENT il est gouverné** → Les politiques techniques (A.8.x) définissent COMMENT l'accès est authentifié et les accès privilégiés protégés → Les procédures de mise en œuvre (IMP) documentent les configurations spécifiques aux systèmes.

---

**FIN DU DOCUMENT DE POLITIQUE**

---

*La présente politique établit les exigences. Les procédures de mise en œuvre sont documentées dans ISMS-IMP-A.5.15-16-18 (UG/TG).*

<!-- QA_VERIFIED: 2026-03-30 -->
