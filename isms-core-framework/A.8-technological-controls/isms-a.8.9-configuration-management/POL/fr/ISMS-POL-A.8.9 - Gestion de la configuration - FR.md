<!-- ISMS-CORE:POLICY:ISMS-POL-A.8.9-FR:framework:POL:a.8.9 -->
**ISMS-POL-A.8.9 – Gestion de la configuration**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Gestion de la configuration |
| **Type de document** | Politique |
| **Identifiant du document** | ISMS-POL-A.8.9 |
| **Créateur du document** | Responsable de la Sécurité des Systèmes d'Information (RSSI) |
| **Propriétaire du document** | Directeur général (DG) |
| **Approuvé par** | Direction générale |
| **Date de création** | [Date] |
| **Version** | 1.0 |
| **Date de version** | [À définir] |
| **Classification** | Interne |
| **Statut** | Brouillon |

**Historique des versions** :

| Version | Date | Auteur | Modifications |
|---------|------|--------|---------------|
| 1.0 | [Date] | RSSI / Responsable de la configuration | Politique initiale consolidée pour la certification ISO 27001:2022 |

**Cycle de révision** : Annuel
**Prochaine date de révision** : [Date d'entrée en vigueur + 12 mois]

**Chaîne d'approbation** :

- Principale : Responsable de la Sécurité des Systèmes d'Information (RSSI)
- Technique : Directeur des Systèmes d'Information (DSI)
- Opérations : Directeur de la Technologie (DT)
- Gouvernance : Responsable de la configuration
- Autorité finale : Direction générale

**Documents connexes** :

- ISMS-POL-00 (Cadre d'applicabilité réglementaire)
- ISMS-IMP-A.8.9.1-UG/TG (Évaluation de la configuration de référence)
- ISMS-IMP-A.8.9.2-UG/TG (Évaluation du contrôle des changements)
- ISMS-IMP-A.8.9.3-UG/TG (Évaluation de la surveillance de la configuration)
- ISMS-IMP-A.8.9.4-UG/TG (Évaluation du durcissement de la sécurité)
- ISMS-CTX-A.8.9 (Référence de gestion de la configuration — NON SMSI)
- ISO/IEC 27001:2022 Contrôle A.8.9

---

## Résumé exécutif

Cette politique établit les exigences de [Organisation] en matière de contrôles de gestion de la configuration, conformément au Contrôle A.8.9 de la norme ISO/IEC 27001:2022.

**Périmètre** : Cette politique s'applique à tous les actifs IT nécessitant une gestion de la configuration (infrastructure de calcul, équipements réseau, systèmes de stockage, services cloud, applications, outils de sécurité, systèmes IoT/OT) dans tous les environnements (production, hors production, cloud, sur site) et toutes les étapes du cycle de vie (déploiement, exploitation, changement, décommissionnement).

**Objet** : Définir les exigences organisationnelles pour la gestion de la configuration. Cette politique établit CE QUI doit être configuré, QUAND les changements nécessitent une approbation, QUI en est responsable, et QUELLES normes s'appliquent. Les procédures de mise en œuvre (COMMENT) sont dans ISMS-IMP-A.8.9. La référence technique est dans ISMS-CTX-A.8.9 (NON SMSI).

**Alignement réglementaire** : Cette politique traite des exigences de conformité obligatoires conformément à ISMS-POL-00, notamment la nLPD suisse, le RGPD de l'UE (le cas échéant) et la norme ISO/IEC 27001:2022. Les exigences conditionnelles (PCI DSS v4.0.1, FINMA, DORA, NIS2) s'appliquent lorsque les activités de [Organisation] déclenchent l'applicabilité.

---

# Alignement sur les contrôles et périmètre

## Contrôle A.8.9 de la norme ISO/IEC 27001:2022

**Norme ISO/IEC 27001:2022 Annexe A.8.9 — Gestion de la configuration**

> *« Les configurations, y compris les configurations de sécurité, du matériel, des logiciels, des services et des réseaux doivent être établies, documentées, mises en œuvre, surveillées et révisées. »*

**Objectif du contrôle** : Établir des configurations de référence sécurisées, empêcher les changements non autorisés, détecter les dérives de configuration, imposer le durcissement de la sécurité et permettre une récupération rapide tout en soutenant les opérations métier.

## Ce que cette politique fait

Cette politique :

- **Définit** les exigences de gestion de la configuration alignées sur la criticité des actifs
- **Établit** le cadre de gouvernance pour les décisions de configuration
- **Précise** les exigences obligatoires de référence, de changement, de surveillance et de durcissement
- **Référence** les exigences réglementaires conformément à ISMS-POL-00
- **Identifie** les rôles et responsabilités

## Ce que cette politique ne fait pas

Cette politique NE :

- **Précise pas les outils ou fournisseurs** (sélection basée sur l'évaluation de [Organisation])
- **Définit pas les référentiels spécifiques aux systèmes** (voir ISMS-CTX-A.8.9 pour les normes techniques)
- **Fournit pas de procédures étape par étape** (voir les évaluations ISMS-IMP-A.8.9)
- **Remplace pas la gestion des actifs** (s'appuie sur l'inventaire A.5.9)
- **Définit pas les flux de travail du système de changements** (les organisations adaptent à leur ITIL/ServiceNow/Jira existant)

## Périmètre

**Types d'actifs** : Calcul et infrastructure, réseau et connectivité, stockage et sauvegarde, cloud et SaaS, applications et middleware, sécurité et identité, systèmes IoT et OT.

**Environnements** : Production, hors production (dev/test/QA/préproduction), reprise après sinistre, formation, sandbox.

**Étapes du cycle de vie** : Définition de la référence, déploiement, changements opérationnels, surveillance, décommissionnement.

**Organisationnel** : Tout le personnel de [Organisation], contractants, tiers, fournisseurs cloud.

**Hors périmètre** : BYOD non géré par [Organisation], systèmes publics sans exigence de sécurité, systèmes temporaires < 24 h de cycle de vie (sauf traitement de données sensibles), exclusions évaluées par les risques avec approbation du RSSI.

## Applicabilité réglementaire

Conformément à **ISMS-POL-00 (Cadre d'applicabilité réglementaire)** :

**Niveau 1 : Obligatoire**

| Réglementation | Exigences |
|----------------|-----------|
| ISO/IEC 27001:2022 | Mise en œuvre du Contrôle A.8.9 |
| nLPD suisse | Art. 8 — Sécurité des données par la gestion de la configuration |
| RGPD de l'UE | Art. 32 — Sécurité du traitement (si traitement de données UE) |

**Niveau 2 : Conditionnel** (SI déclenché)

| Réglementation | Déclencheur | Exigences |
|---------------|------------|-----------|
| PCI DSS v4.0.1 | Traitement de cartes de paiement | Exig. 1-4, 6, 11 : Normes de configuration |
| FINMA | Services financiers suisses | Gestion de la configuration basée sur les risques |
| DORA | Finance critique UE | Art. 9, 21 : Risque TIC et gestion des incidents |
| NIS2 | Entités essentielles/importantes UE | Art. 21 : Mesures de risque en cybersécurité |

---

# Exigences de gestion de la configuration

## Cadre à quatre domaines

[Organisation] met en œuvre la gestion de la configuration à travers **quatre domaines** :

1. **Configuration de référence** — Définir des référentiels sécurisés
2. **Contrôle des changements** — Approuver les modifications de configuration
3. **Surveillance de la configuration** — Détecter les changements non autorisés
4. **Durcissement de la sécurité** — Imposer les normes de sécurité

## Gestion de la configuration de référence

[Organisation] établit, documente et maintient des configurations de référence sécurisées.

### Définition du référentiel

**Couverture** :

[Organisation] DOIT définir des référentiels pour :

- Les types d'actifs en usage actif (pas les actifs individuels)
- Les configurations de systèmes critiques
- Les équipements de sécurité réseau
- Les systèmes d'identité et d'accès
- Les outils de sécurité

**Granularité** : Au niveau du type d'actif (par ex. « Référentiel Windows Server 2022 DC »), PAS au niveau de l'actif individuel.

**Justification** : Extensibilité (100 serveurs ≠ 100 référentiels), vérification de la conformité, déploiement rapide, maintenance simplifiée.

**Composantes** :

Les référentiels DOIVENT documenter :

- Configurations OS (paramètres de sécurité, services, registre, paramètres du noyau)
- Configurations des applications
- Configurations réseau (IP, routage, règles de pare-feu, ACL)
- Configurations de sécurité (authentification, chiffrement, journalisation, audit)
- Normes de durcissement appliquées (CIS, STIG, guides fournisseurs)
- Exceptions et dérogations avec justification
- Critères de validation

### Approbation

**Flux de travail** : Trois niveaux

- Niveau 1 : Le Responsable technique valide la précision/faisabilité
- Niveau 2 : L'Architecte de sécurité valide le durcissement/la conformité
- Niveau 3 : Le Responsable de la configuration/RSSI approuve

**Calendrier** :

- Nouveaux référentiels : **14 jours**
- Mises à jour : **7 jours**
- Urgence : **24 heures**

### Images de référence (Golden Images)

Les images de référence DOIVENT :

- Mettre en œuvre les référentiels approuvés
- Être testées en hors production
- Contenir uniquement des logiciels approuvés et sous licence
- Inclure les derniers correctifs de sécurité
- Être versionnées et suivies
- Être actualisées trimestriellement

### Documentation

Les référentiels DOIVENT être documentés avec :

- Identifiant du référentiel (par ex. « BASE-WIN2022-DC-v1.2 »)
- Type d'actif, version, date, statut d'approbation
- Paramètres et valeurs de configuration
- Justification sécurité
- Validation des tests
- Procédures de dérogation

**Référentiel** : Sous contrôle de version, contrôle d'accès, sauvegarde hebdomadaire, journalisation des audits.

**Révision** : Annuelle (minimum), trimestrielle (systèmes critiques), ponctuelle (changements de technologie/vulnérabilité/réglementation).

### Statut de l'inventaire des référentiels

[Organisation] maintient la documentation des référentiels pour les types d'actifs de production :

- **Cible de couverture des référentiels** : ≥ 90 % des types d'actifs de production
- **Systèmes critiques** (Niveaux 1/2) : Référentiels prioritaires pour les OS, équipements réseau, services cloud, outils de sécurité
- **Emplacement du référentiel** : Référentiel sous contrôle de version (référencé dans ISMS-IMP-A.8.9.1)

### Infrastructure en tant que code (IaC)

[Organisation] DEVRAIT adopter l'IaC lorsque c'est faisable :

- Définir les référentiels sous forme de code (Terraform, Ansible, CloudFormation, Kubernetes)
- Stocker dans un système de contrôle de version (Git)
- Mettre en œuvre des flux de révision (pull requests, tests automatisés)
- Utiliser pour le déploiement automatisé (CI/CD)
- Analyser les mauvaises configurations

## Contrôle des changements et mises à jour de la configuration

[Organisation] s'assure que tous les changements de configuration suivent des processus approuvés avec autorisation, tests et documentation.

### Classification des changements

**Types de changements** :

| Type | Définition | Approbation | Tests | Exemples |
|------|------------|-------------|-------|---------|
| **Standard** | Pré-approuvé, faible risque, répétable | Pré-approuvé (procédure standard) | Selon procédure | Réinitialisations de mots de passe, correctifs standard, renouvellements de certificats |
| **Normal** | Nécessite évaluation et approbation | Approbation du CAC | Requis (environnement de test) | Mises à niveau systèmes, règles de pare-feu, changements de référentiel |
| **Urgence** | Urgent pour incidents/vulnérabilités | Accéléré (DSI/RSSI) | Abrégé/dispensé | Exploits de sécurité, pannes critiques, bugs critiques |

**Changements d'urgence** :

- DOIVENT avoir une justification d'urgence réelle
- NE DOIVENT PAS être utilisés pour la commodité ou une mauvaise planification
- La classification d'urgence DOIT être révisée après mise en œuvre
- Cible : < 10 % de tous les changements doivent être des urgences

### Processus de révision des changements d'urgence

Tous les changements d'urgence DOIVENT faire l'objet d'une révision post-mise en œuvre dans les **5 jours ouvrables** :

1. **Révision rétrospective du CAC** : Le CAC valide que la classification d'urgence était appropriée
2. **Contestation de la classification** : Si le CAC détermine que le changement n'était pas une véritable urgence :
   - **Première infraction** : Le demandeur du changement reçoit une formation sur la classification appropriée
   - **Infraction répétée** : Escalade vers le DSI/RSSI, peut entraîner une restriction des privilèges de changement
3. **Analyse des tendances** : Le Responsable de la configuration rapporte le taux de changements d'urgence mensuellement
4. **Alerte de seuil** : Si le taux d'urgence dépasse 15 % en un mois, déclenche un audit du processus

### Comité d'Approbation des Changements (CAC)

**Composition** :

- **Président du CAC** : Responsable de la configuration ou cadre IT senior (autorité décisionnelle)
- **Membres principaux** : Architecte de sécurité, Responsable réseau, représentants des Propriétaires d'applications
- **Membres variables** : Propriétaires de services, représentants fournisseurs, Responsable conformité (selon les besoins)

**Responsabilités** :

- Réviser et approuver/rejeter/reporter les changements normaux
- Évaluer l'impact et le risque des changements
- Vérifier les plans de tests et de retour arrière
- Prioriser les changements en cas de conflits
- Conduire les révisions post-mise en œuvre pour les changements d'urgence
- Identifier les tendances des changements et les améliorations de processus

**Opérations** :

- **Réunions régulières** : Hebdomadaires ou bimensuelles (selon le volume de changements)
- **Sessions d'urgence** : Ponctuelles pour les changements critiques
- **Révisions virtuelles** : Approbation par e-mail pour les changements à faible risque
- **Documentation** : Procès-verbaux, présence, décisions avec justification

### Preuves opérationnelles du CAC

Les opérations du CAC DOIVENT être prouvées par :

1. **Procès-verbaux de réunion** : Documentés pour toutes les sessions, incluant date, durée, participants, changements révisés (ID, demandeurs), décisions (approuver/rejeter/reporter) avec justification, actions et responsables

2. **Suivi de la présence** : Participation des membres principaux suivie pour vérifier la cible de ≥ 80 %

3. **Registre des décisions** : Toutes les approbations/rejets du CAC journalisés dans le système de gestion des changements

4. **Conservation** : Dossiers du CAC conservés minimum **3 ans** pour l'audit

### Flux d'approbation

**Niveaux d'approbation selon le risque** :

| Niveau de risque | Niveaux d'approbation | Approbateurs | Délai |
|-----------------|----------------------|-------------|-------|
| **Standard** | Aucun (pré-approuvé) | N/A | Exécution immédiate |
| **Faible risque** | Un niveau | Responsable technique / Propriétaire du système | 1-2 jours ouvrables |
| **Risque moyen** | Deux niveaux | Responsable technique + Propriétaire du service | 3-5 jours ouvrables |
| **Risque élevé** | Trois niveaux | Responsable technique + Propriétaire du service + CAC | 5-10 jours ouvrables |
| **Urgence** | Accéléré | DSI ou RSSI (verbal/e-mail) | < 4 heures ; révision CAC rétrospective dans 5 jours |

### Tests et validation

**Exigences de tests** :

Les changements normaux DOIVENT être testés :

- **Environnement de développement/test** : Tests hors production obligatoires
- **Critères de validation** : Critères de succès définis avant les tests
- **Documentation des tests** : Résultats et problèmes documentés
- **Tests de performance** : Vérifier l'absence de dégradation inacceptable
- **Tests de sécurité** : Vérifier l'absence de vulnérabilités introduites

**Décision de mise en production / arrêt** : Avant la production, décision formelle tenant compte des résultats des tests, de la préparation au retour arrière, de la préparation métier et de la complétion des communications.

### Retour arrière et récupération

**Planification du retour arrière** :

Les changements DOIVENT inclure un plan de retour arrière documentant :

- **Critères de déclenchement** : Quand exécuter (conditions d'échec spécifiques)
- **Procédure** : Instructions étape par étape
- **Calendrier** : Durée du retour arrière
- **Risque de perte de données** : Données irrécupérables le cas échéant
- **Vérification de la sauvegarde** : Confirmer l'existence d'une sauvegarde avant le changement

**Autorité de retour arrière** :

- Président du CAC ou DSI : Changements majeurs de production
- Propriétaire du service : Changements spécifiques au service
- Ingénieur d'astreinte : Urgences hors heures ouvrables (avec notification de la direction)

### Métriques de succès des changements

**ICP** :

| Métrique | Cible | Mesure |
|---------|-------|--------|
| **Taux de succès des changements** | ≥ 95 % | % de changements ne nécessitant pas de retour arrière |
| **Taux de changements d'urgence** | < 10 % | % classifiés comme Urgence |
| **Conformité SLA d'approbation** | ≥ 90 % | % approuvés dans le délai |
| **Présence au CAC** | ≥ 80 % | Présence moyenne des membres requis |
| **Complétion des revues post-mise en œuvre** | 100 % | % avec revue complétée dans les 5 jours |

## Surveillance de la configuration et détection des dérives

[Organisation] surveille en continu les configurations et détecte les changements non autorisés.

### Surveillance continue

**Cibles de couverture** :

| Niveau | Cible de couverture | Fréquence | Écart acceptable |
|--------|---------------------|-----------|-----------------|
| **Niveau 1 (Critique)** | 100 % | Temps réel ou horaire | 0 % |
| **Niveau 2 (Élevé)** | ≥ 95 % | Quotidienne | < 5 % |
| **Niveau 3 (Moyen)** | ≥ 85 % | Hebdomadaire | < 15 % |
| **Niveau 4 (Faible)** | ≥ 70 % | Mensuelle | < 30 % |

**Capacités de surveillance** :

Les outils de surveillance DOIVENT :

- Être déployés pour les actifs de Niveaux 1 et 2
- Comparer la configuration réelle au référentiel approuvé
- Générer des alertes pour les déviations de configuration
- Conserver les résultats pour l'audit (minimum 90 jours)

### Détection des dérives et alertes

**Classification des dérives** :

| Gravité | Définition | SLA de réponse | Exemple |
|---------|------------|----------------|---------|
| **Critique** | Contrôle de sécurité désactivé | < 1 heure | Pare-feu désactivé, compte admin non autorisé, chiffrement désactivé |
| **Élevée** | Changement lié à la sécurité | < 4 heures | Politique de mots de passe affaiblie, journalisation désactivée, service non autorisé |
| **Moyenne** | Dérive non liée à la sécurité | < 24 heures | Port de service modifié, paramètre non critique, discordance de documentation |
| **Faible** | Dérive informative | < 5 jours ouvrables | Changements cosmétiques, paramètres non fonctionnels |

### Remédiation des dérives

**Flux de remédiation** :

1. **Détection** : La surveillance automatisée détecte la dérive
2. **Triage** : Le Responsable de la configuration enquête sur la cause
3. **Classification** : Autorisée, non autorisée ou faux positif
4. **Action** :

   - Autorisée : Mettre à jour le référentiel, clôturer l'incident
   - Non autorisée : Remédier au référentiel, enquêter sur la cause profonde, clôturer l'incident
   - Faux positif : Ajuster la surveillance, clôturer l'incident

**Délais de remédiation** :

| Gravité | SLA de remédiation | Escalade |
|---------|-------------------|---------|
| **Critique** | < 4 heures | Escalader vers le RSSI si non résolu |
| **Élevée** | < 24 heures | Escalader vers le Responsable de la configuration |
| **Moyenne** | < 5 jours ouvrables | Escalader vers le Responsable des opérations IT |
| **Faible** | < 30 jours | Au mieux |

**Autorité d'escalade de la remédiation des dérives** :

Si le SLA de remédiation n'est pas respecté :

**Étape 1** : Le Responsable de la configuration escalade vers le responsable du Propriétaire du système
**Étape 2** : Si toujours non résolu après 48 heures, le RSSI révise et peut :
- **Option A** : Accorder une exception avec contrôles compensatoires (maximum 30 jours)
- **Option B** : Initier un changement d'urgence pour forcer la remédiation
- **Option C** : Isoler le système non conforme de la production (si le risque est inacceptable)

**Autorité finale** : Le RSSI a l'autorité pour retirer des systèmes de production pour une dérive critique non résolue créant un risque inacceptable.

## Durcissement de la sécurité et conformité

[Organisation] applique le durcissement de la sécurité selon les normes sectorielles et maintient la conformité.

### Sélection des normes de durcissement

**Critères de sélection** : Type d'actif/technologie, exigences réglementaires (conformément à ISMS-POL-00), meilleures pratiques sectorielles, appétit au risque organisationnel, faisabilité opérationnelle.

**Normes reconnues** (exemples) :

| Norme | Fournisseur | Utilisation |
|-------|------------|-------------|
| **CIS Benchmarks** | Center for Internet Security | Référence principale pour les plateformes courantes |
| **DISA STIGs** | Defense Information Systems Agency | Haute sécurité, gouvernement/défense |
| **Guides fournisseurs** | Microsoft, AWS, Azure, GCP, etc. | Plateformes cloud et fournisseurs |
| **Référentiels NIST** | NIST SP 800-53, 800-128 | Alignement sur le cadre |

### Mise en œuvre du durcissement

**Exigences de mise en œuvre** :

Tous les actifs de production DOIVENT :

- Être durcis selon les normes applicables avant le déploiement en production
- Mettre en œuvre les contrôles de sécurité critiques à ≥ 95 % de conformité
- Avoir le durcissement vérifié avant le placement en production
- Documenter et évaluer par les risques les lacunes de durcissement

**Cibles de couverture** :

| Niveau | Contrôles critiques | Conformité globale | Écarts acceptables |
|--------|---------------------|--------------------|--------------------|
| **Niveau 1** | 100 % | ≥ 95 % | 0 écart critique |
| **Niveau 2** | ≥ 95 % | ≥ 90 % | < 5 écarts critiques |
| **Niveau 3** | ≥ 90 % | ≥ 80 % | < 10 écarts critiques |
| **Niveau 4** | ≥ 80 % | ≥ 70 % | Au mieux |

### Vérification de la conformité

**Fréquence des analyses automatisées** :

| Niveau d'actif | Fréquence d'analyse | Vérification manuelle (si automatisation indisponible) |
|----------------|---------------------|------------------------------------------------------|
| **Niveau 1 (Critique)** | Trimestrielle (automatisée) | Semestrielle (manuelle) |
| **Niveau 2 (Élevé)** | Semestrielle (automatisée) | Annuelle (manuelle) |
| **Niveau 3/4 (Moyen/Faible)** | Annuelle (automatisée) | Annuelle (manuelle) |

### Remédiation des lacunes

**Priorisation de la remédiation** :

| Risque de lacune | Délai | Autorité d'approbation des exceptions |
|-----------------|-------|--------------------------------------|
| **Critique** | < 30 jours | RSSI uniquement |
| **Élevé** | < 90 jours | Responsable de la configuration + Architecte de sécurité |
| **Moyen** | < 180 jours | Responsable de la configuration |
| **Faible** | Au mieux | Responsable de la configuration |

---

# Rôles et responsabilités

## Matrice RACI

| Activité | RSSI | DSI/DT | Resp. Config. | Archit. Sécu. | Propr. Syst. | Admin. Syst. | CAC | Auditeur |
|----------|------|--------|--------------|--------------|-------------|-------------|-----|---------|
| **Approbation de la politique** | R | C | R | C | I | I | I | I |
| **Définition du référentiel** | C | I | R | R | C | R | I | I |
| **Approbation du référentiel** | R | C | R | R | C | I | I | I |
| **Approbation du changement (Normal)** | I | I | R | C | C | R | R | I |
| **Mise en œuvre du changement** | I | I | C | I | R | R | I | I |
| **Configuration de la surveillance** | C | I | R | R | C | R | I | I |
| **Remédiation des dérives** | I | I | C | C | R | R | I | I |
| **Mise en œuvre du durcissement** | C | I | C | R | C | R | I | I |
| **Évaluation de la conformité** | R | C | R | R | C | C | I | R |
| **Soutien à l'audit** | C | I | R | C | C | C | I | R |

**Légende** : R = En charge, R (majuscule) = Responsable, C = Consulté, I = Informé

## Descriptions des rôles clés

**RSSI** : Responsable de la politique et du programme de gestion de la configuration ; approuve les référentiels, normes de durcissement et exceptions ; révise les métriques de conformité.

**Responsable de la configuration** : Responsable des opérations quotidiennes ; préside le CAC ; gère le référentiel des référentiels et le contrôle de version ; coordonne la surveillance et les activités de remédiation ; rapporte les métriques au RSSI/DSI.

**Architecte de sécurité** : En charge de la sélection des normes de durcissement ; révise les référentiels pour la conformité à la sécurité ; définit les exigences de sécurité pour les configurations.

**Propriétaire du système** : Responsable de la conformité de configuration des systèmes détenus ; approuve les changements affectant les systèmes détenus ; assure la remédiation rapide des dérives.

**Administrateur système / Ingénieur DevOps** : Responsable de la mise en œuvre des référentiels et des changements ; effectue la configuration de la surveillance ; trie les alertes de dérive ; documente l'état de la configuration.

**Comité d'Approbation des Changements (CAC)** : Responsable des décisions d'approbation des changements ; révise les changements normaux pour l'impact et le risque ; valide les plans de tests et de retour arrière.

---

# Gouvernance de la politique

## Conformité

**Métriques de conformité** :

| Métrique | Cible | Fréquence | Responsable |
|---------|-------|-----------|------------|
| **Couverture des référentiels** | ≥ 90 % des types d'actifs | Mensuelle | Responsable de la configuration |
| **Taux de succès des changements** | ≥ 95 % | Mensuelle | Président du CAC |
| **Taux de changements d'urgence** | < 10 % de tous les changements | Mensuelle | Président du CAC |
| **Conformité des réunions du CAC** | 100 % documentées | Mensuelle | Président du CAC |
| **Conformité SLA remédiation dérives** | ≥ 90 % dans les délais | Mensuelle | Responsable de la configuration |
| **Conformité au durcissement** | ≥ 90 % contrôles critiques | Trimestrielle | Architecte de sécurité |
| **Présence au CAC** | ≥ 80 % membres principaux | Mensuelle | Président du CAC |
| **Révision des exceptions** | 100 % révisées annuellement | Trimestrielle | Responsable de la configuration |

**Note** : Tous les changements nécessitant un retour arrière DOIVENT faire l'objet d'une analyse des causes profondes complétée dans les 10 jours ouvrables, présentée au CAC, et des actions de remédiation suivies.

## Gestion des exceptions

Les exceptions aux exigences de configuration DOIVENT :

- Être demandées par écrit avec justification métier
- Inclure une évaluation des risques et des contrôles compensatoires
- Être révisées par l'Architecte de sécurité
- Être approuvées par l'autorité appropriée (conformément à la Section 2.5.4)
- Avoir une date d'expiration définie (maximum 12 mois)
- Être révisées annuellement pour renouvellement ou révocation

---

# Définitions

**Configuration de référence** : Ensemble documenté de paramètres de configuration de sécurité et opérationnels pour un type d'actif, servant de référence pour le déploiement et la vérification de la conformité.

**Comité d'Approbation des Changements (CAC)** : Équipe interfonctionnelle responsable de l'évaluation, de l'approbation et de la révision des changements de configuration pour minimiser les risques et assurer la coordination.

**Taux de succès des changements** : Pourcentage de changements mis en œuvre atteignant le résultat escompté sans nécessiter de retour arrière.

**Dérive de configuration** : Écart de la configuration réelle du système par rapport au référentiel approuvé, pouvant indiquer des changements non autorisés ou des lacunes de documentation du référentiel.

**Base de données de gestion des configurations (CMDB)** : Référentiel stockant les référentiels de configuration, les images de référence, les configurations des actifs, l'historique des changements et les relations entre les éléments de configuration.

**Changement d'urgence** : Changement de configuration urgent nécessaire pour résoudre un incident de sécurité critique, une interruption de service ou une vulnérabilité, suivant un processus d'approbation accéléré avec révision rétrospective.

**Image de référence (Golden Image)** : Image système préconfigurée mettant en œuvre la configuration de référence approuvée, utilisée pour le déploiement rapide et cohérent de nouveaux systèmes.

**Durcissement** : Processus de sécurisation des configurations système en mettant en œuvre des normes de sécurité reconnues (CIS Benchmarks, DISA STIGs) et en supprimant les services, comptes et fonctionnalités inutiles.

**Infrastructure en tant que code (IaC)** : Pratique de gestion des référentiels de configuration et du provisionnement de l'infrastructure via du code lisible par machine stocké dans des systèmes de contrôle de version.

**Changement normal** : Changement de configuration nécessitant une évaluation individuelle et l'approbation du CAC, suivant le processus de contrôle des changements standard avec planification des tests et du retour arrière.

**Retour arrière** : Processus d'annulation d'un changement de configuration pour restaurer le système à son état antérieur au changement, exécuté lorsque le changement échoue aux critères de validation ou introduit un risque inacceptable.

**Changement standard** : Changement de configuration pré-approuvé, à faible risque et répétable suivant une procédure documentée, exécutable sans révision individuelle du CAC.

---

# Enregistrement d'approbation

| Rôle | Nom | Date |
|------|-----|------|
| **Responsable de la Sécurité des Systèmes d'Information (RSSI)** | [Nom] | [Date] |
| **Directeur des Systèmes d'Information (DSI)** | [Nom] | [Date] |
| **Directeur de la Technologie (DT)** | [Nom] | [Date] |
| **Responsable de la configuration** | [Nom] | [Date] |
| **Direction générale** | [Nom] | [Date] |

---

**FIN DU DOCUMENT DE POLITIQUE**

---

*Cette politique établit les exigences de gestion de la configuration. Les procédures de mise en œuvre sont documentées dans ISMS-IMP-A.8.9 (UG/TG). Les informations de référence technique sont fournies dans ISMS-CTX-A.8.9 (NON SMSI).*

<!-- QA_VERIFIED: 2026-04-02 -->
