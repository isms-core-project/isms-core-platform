<!-- ISMS-CORE:REF:ISMS-REF-FINMA-FR-finma-circular-2023-1-requirements-reference:framework:REF:finma -->
**ISMS-REF-FINMA — Référence des exigences de la Circulaire FINMA 2023/1**
**Exigences de sécurité de l'information pour les établissements financiers suisses (Référence technique non-SMSI)**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Référence des exigences de la Circulaire FINMA 2023/1 |
| **Type de document** | Interne — Référence technique (Non-SMSI) |
| **Identifiant du document** | ISMS-REF-FINMA |
| **Créateur du document** | Responsable de la Sécurité des Systèmes d'Information (RSSI) |
| **Propriétaire du document** | Directeur Général (PDG) |
| **Approuvé par** | RSSI (Référence technique — Aucune approbation de la Direction générale requise) |
| **Date de création** | [Date] |
| **Version** | 1.0 |
| **Date de version** | [À déterminer] |
| **Classification** | Interne |
| **Statut** | Brouillon |

**Historique des versions** :

| Version | Date | Auteur | Modifications |
|---------|------|--------|---------------|
| 1.0 | [Date] | RSSI / Juridique/Conformité | Référence technique initiale pour les établissements financiers suisses |

**Cycle de révision** : Annuel (ou lors de mises à jour des circulaires FINMA)
**Prochaine date de révision** : [Date + 12 mois]
**Approbateurs** : Juridique/Conformité / RSSI (référence technique, aucune approbation SMSI requise)

**Distribution** : Équipe de conformité, RSSI, Conseil juridique (pour les organisations soumises à la surveillance FINMA)

---

⚠️ **IMPORTANT — DOCUMENT DE SUPPORT TECHNIQUE NON-SMSI**

Ce document est fourni à des fins d'information et de sensibilisation uniquement.

- Ce document ne fait PAS partie du Système de Management de la Sécurité de l'Information (SMSI).
- Ce document ne définit PAS d'exigences obligatoires à moins que [Organisation] ne soit une entité réglementée par la FINMA.
- Ce document n'établit PAS d'exigences contraignantes, de délais, de KPI ou de SLA pour les entités non réglementées.
- Ce document n'impose PAS l'adoption des exigences FINMA aux organisations non soumises à la surveillance de la FINMA.
- Ce document ne remplace ni n'étend aucune politique du SMSI.

**Détermination de l'applicabilité** :
Les exigences FINMA s'appliquent UNIQUEMENT SI [Organisation] :

- Détient une licence FINMA (banque, négociant en valeurs mobilières, assurance, gestion de fonds, services de paiement)
- Est soumise à la surveillance de la FINMA
- Opère en tant qu'établissement financier suisse

Pour toutes les autres organisations, ce document sert uniquement de :

- Référence technique pour les exigences FINMA potentielles
- Contexte pour les relations avec des prestataires de services aux établissements financiers suisses
- Sensibilisation aux normes de sécurité du secteur financier suisse
- **Ce document ne doit pas être utilisé comme preuve d'audit à moins que [Organisation] ne soit réglementée par la FINMA**

L'utilisation de ce document n'implique pas l'applicabilité de la FINMA, des obligations de conformité ou un statut réglementaire.

**Déclaration de positionnement critique** :
Ce document fournit intentionnellement des détails réglementaires au-delà de ce qui s'applique à la plupart des organisations. Son objectif est la sensibilisation uniquement pour les organisations susceptibles de devenir soumises à la surveillance de la FINMA, ou qui fournissent des services à des entités réglementées par la FINMA. Aucune conclusion d'audit ne doit être tirée de la présence, de l'absence ou du statut de mise en œuvre de toute exigence FINMA énumérée ici, à moins que [Organisation] ne soit explicitement réglementée par la FINMA.

---

# Objet et périmètre du document

## Objet

Ce document fournit une vue d'ensemble technique des exigences de sécurité de l'information de l'Autorité fédérale de surveillance des marchés financiers (FINMA) telles que définies dans la Circulaire FINMA 2023/1 « Risques opérationnels et résilience — banques » (en vigueur depuis le 1er juin 2024). Il vise à soutenir :

- La sensibilisation aux exigences FINMA pour les établissements financiers suisses
- La compréhension de la structure des marges FINMA et des exigences clés
- Le contexte pour les organisations fournissant des services aux établissements financiers suisses
- L'évaluation d'une applicabilité future potentielle
- La mise en correspondance des exigences FINMA avec les contrôles ISO 27001:2022

## Ce que ce document n'est PAS

Ce document ne :

- N'établit PAS d'exigences obligatoires pour les organisations non réglementées par la FINMA
- Ne définit PAS les obligations de conformité de [Organisation] (voir POL-00 pour l'applicabilité réglementaire)
- Ne crée PAS de critères d'audit à moins que [Organisation] ne soit réglementée par la FINMA
- Ne remplace PAS l'interprétation du conseil juridique ou de conformité
- Ne constitue PAS un avis juridique sur la conformité à la FINMA
- N'établit PAS de procédures de mise en œuvre ou de processus de vérification

## Relation avec le SMSI

Ce document est une **référence technique non contraignante** SAUF si [Organisation] est soumise à la surveillance de la FINMA (telle que déterminée dans ISMS-POL-00 Section 3.1).

**Si [Organisation] EST réglementée par la FINMA :**

- Les exigences FINMA deviennent Niveau 1 (Conformité obligatoire) selon POL-00
- Ce document fournit des orientations de mise en œuvre
- Les contrôles du SMSI doivent démontrer la conformité FINMA
- Une attestation annuelle de conformité FINMA est requise

**Si [Organisation] N'EST PAS réglementée par la FINMA :**

- La FINMA reste Niveau 3 (Référence informative) selon POL-00
- Ce document est fourni à titre de sensibilisation uniquement
- Aucune obligation de conformité FINMA n'existe
- Les contrôles du SMSI suivent uniquement ISO 27001:2022

## Organisation du contenu

Cette référence organise les exigences FINMA par :

- Structure des marges de la Circulaire FINMA 2023/1
- Exigences de sécurité de l'information (Marges 50–62)
- Exigences de journalisation et de surveillance (Marges 63–72)
- Exigences de continuité des activités (Marges 73–87)
- Exigences d'externalisation (FINMA 2008/7 et 2018/3)
- Mise en correspondance avec les contrôles de l'Annexe A de l'ISO 27001:2022

---

# Aperçu et applicabilité de la FINMA

## Qu'est-ce que la FINMA ?

L'**Eidgenössische Finanzmarktaufsicht (FINMA)** est l'Autorité fédérale de surveillance des marchés financiers suisse, chargée de surveiller les banques, les compagnies d'assurance, les bourses, les négociants en valeurs mobilières et d'autres intermédiaires financiers en Suisse.

**Base légale principale** :

- Loi sur les marchés financiers (LFINMA)
- Loi sur les banques (LB)
- Loi sur la surveillance des assurances (LSA)
- Loi sur les établissements financiers (LEFin)

**Autorité d'exécution** :

- Octroi et retrait de licences
- Examens sur place
- Surveillance à distance
- Mesures d'exécution (amendes, révocation de licence)
- Exigences de notification des incidents

## Circulaires FINMA

**Structure des circulaires** :
La FINMA émet des « circulaires » qui établissent des normes minimales contraignantes pour les établissements surveillés. Les principales circulaires en matière de sécurité de l'information :

**Circulaire FINMA 2023/1** — Risques opérationnels et résilience (banques) :

- En vigueur : 1er juin 2024
- S'applique à : Les banques et négociants en valeurs mobilières
- Périmètre : Gestion des risques opérationnels, continuité des activités, sécurité de l'information, externalisation
- **Marges 50–62** : Exigences de sécurité de l'information
- **Marges 63–72** : Exigences de journalisation et de surveillance
- **Marges 73–87** : Exigences de continuité des activités et de résilience

**Circulaire FINMA 2008/7** — Externalisation (banques) :

- Gestion des risques dans les relations d'externalisation
- Exigences de diligence raisonnable et contractuelles
- Protection des données et confidentialité
- Continuité des activités dans le cadre de l'externalisation

**Circulaire FINMA 2018/3** — Externalisation (assureurs) :

- Exigences similaires adaptées au secteur des assurances
- Exigences de notification à l'autorité de surveillance

## Détermination de l'applicabilité

**La FINMA s'applique à [Organisation] SI** :

| Critère | Statut | Preuve |
|---------|--------|--------|
| Détient une licence bancaire FINMA | ⬜ Oui ⬜ Non | [Numéro de licence / N/A] |
| Détient une licence de négociant en valeurs mobilières FINMA | ⬜ Oui ⬜ Non | [Numéro de licence / N/A] |
| Détient une licence d'assurance FINMA | ⬜ Oui ⬜ Non | [Numéro de licence / N/A] |
| Détient une licence de gestion de fonds FINMA | ⬜ Oui ⬜ Non | [Numéro de licence / N/A] |
| Détient une licence de services de paiement FINMA | ⬜ Oui ⬜ Non | [Numéro de licence / N/A] |
| Soumis à la surveillance FINMA | ⬜ Oui ⬜ Non | [Détermination de la surveillance] |

**Si UN « Oui » quelconque** : Les exigences FINMA sont **Niveau 1 (Conformité obligatoire)** selon POL-00 Section 3.1

**Si TOUS « Non »** : Les exigences FINMA restent **Niveau 3 (Référence informative)** selon POL-00

**Statut de prestataire de services** :
Si [Organisation] fournit des services À des entités réglementées par la FINMA :

- Les exigences d'externalisation FINMA 2008/7 ou 2018/3 peuvent s'appliquer
- Les contrats clients peuvent imposer des contrôles équivalents FINMA
- Les clauses de droit d'audit peuvent exiger une démonstration de conformité FINMA
- À considérer comme exigences contractuelles (Niveau 1 si contractuellement obligatoire)

---

# Circulaire FINMA 2023/1 — Exigences de sécurité de l'information

## Aperçu (Marges 50–62)

Les Marges 50–62 de la Circulaire FINMA 2023/1 établissent les exigences de sécurité de l'information pour les banques et négociants en valeurs mobilières suisses.

**Principe clé** :
Les organisations doivent mettre en œuvre des mesures de sécurité de l'information **basées sur les risques**, adaptées à :

- La nature et l'étendue des activités commerciales
- La complexité des systèmes informatiques
- La sensibilité des données traitées
- Le paysage des menaces et l'évaluation des risques

La FINMA ne prescrit pas de contrôles techniques spécifiques mais exige des « mesures organisationnelles et techniques appropriées ».

## Marges 50–55 : Cadre de sécurité de l'information

**Marge 50 : Stratégie de sécurité de l'information**

**Exigence** :
Les banques doivent définir et mettre en œuvre une stratégie de sécurité de l'information alignée sur :

- La stratégie commerciale et l'appétit pour le risque
- La stratégie et l'architecture informatiques
- Les exigences réglementaires
- Les meilleures pratiques du secteur

**Correspondance ISO 27001:2022** :

- Clause 5.2 : Politique
- Clause 6.2 : Objectifs de sécurité de l'information
- A.5.1 : Politiques de sécurité de l'information

**Considérations de mise en œuvre** :

- Approbation de la stratégie de sécurité de l'information au niveau du conseil d'administration
- Révision et mise à jour annuelles
- Intégration dans la gestion des risques d'entreprise
- Rôles et responsabilités clairement définis (RSSI, direction informatique, unités métier)

---

**Marge 51 : Organisation de la sécurité de l'information**

**Exigence** :
Structure organisationnelle claire pour la sécurité de l'information avec :

- Des rôles et responsabilités définis
- La séparation des tâches (développement, exploitation, sécurité)
- Une fonction de sécurité indépendante dotée d'une autorité suffisante
- Des voies d'escalade vers la direction générale et le conseil d'administration

**Correspondance ISO 27001:2022** :

- Clause 5.3 : Rôles, responsabilités et autorités organisationnels
- A.5.2 : Rôles et responsabilités en matière de sécurité de l'information

**Rôles clés** (attente FINMA) :

- Responsable de la Sécurité des Systèmes d'Information (RSSI) ou équivalent
- Comité de Sécurité de l'Information
- Propriétaires de systèmes
- Architectes de sécurité
- Équipe des Opérations de Sécurité

---

**Marge 52 : Évaluation des risques**

**Exigence** :
Évaluations régulières des risques liés à la sécurité de l'information couvrant :

- L'identification des actifs informationnels
- L'évaluation des menaces et des vulnérabilités
- L'évaluation et la priorisation des risques
- Les décisions de traitement des risques
- L'acceptation des risques résiduels

**Correspondance ISO 27001:2022** :

- Clause 6.1.2 : Évaluation des risques liés à la sécurité de l'information
- Clause 6.1.3 : Traitement des risques liés à la sécurité de l'information
- Clause 8.2 : Évaluation des risques liés à la sécurité de l'information
- Clause 8.3 : Traitement des risques liés à la sécurité de l'information

**Attentes FINMA** :

- Évaluation des risques annuelle au minimum
- Évaluations déclenchées lors de changements majeurs
- Rapport au conseil d'administration sur les risques clés
- Documentation des décisions de risque

---

**Marge 53 : Politiques et standards de sécurité**

**Exigence** :
Politiques et standards de sécurité de l'information complets couvrant :

- La classification de l'information
- Le contrôle des accès
- La cryptographie
- La sécurité physique
- La gestion des incidents
- La continuité des activités

**Correspondance ISO 27001:2022** :

- A.5.1 : Politiques de sécurité de l'information
- A.5.10 : Utilisation acceptable de l'information et des autres actifs associés
- A.5.12 : Classification de l'information

**Exigences de documentation** :

- Hiérarchie des politiques (stratégie → politique → standards → procédures)
- Révision et mise à jour régulières
- Communication et sensibilisation
- Approbation par la direction

---

**Marge 54 : Sensibilisation et formation à la sécurité**

**Exigence** :
Programme de sensibilisation et de formation à la sécurité de l'information garantissant :

- Que tout le personnel comprend ses obligations en matière de sécurité
- Une formation spécifique au rôle pour les responsabilités de sécurité
- Des campagnes régulières de sensibilisation
- Des tests et la validation de l'efficacité de la sensibilisation

**Correspondance ISO 27001:2022** :

- A.6.3 : Sensibilisation, éducation et formation à la sécurité de l'information

**Attentes FINMA** :

- Formation obligatoire annuelle pour tout le personnel
- Formation spécialisée pour les utilisateurs à privilèges
- Simulation de hameçonnage et tests
- Suivi et métriques de complétion des formations

---

**Marge 55 : Gestion des risques liés aux tiers**

**Exigence** :
Approche basée sur les risques pour la sécurité des tiers, incluant :

- Les évaluations de sécurité des fournisseurs
- Les exigences contractuelles de sécurité
- La surveillance continue des performances des fournisseurs
- Le droit d'audit et d'accès à l'information

**Correspondance ISO 27001:2022** :

- A.5.19 : Sécurité de l'information dans les relations avec les fournisseurs
- A.5.20 : Prise en compte de la sécurité de l'information dans les accords avec les fournisseurs
- A.5.21 : Gestion de la sécurité de l'information dans la chaîne d'approvisionnement TIC

**Spécificités FINMA** :

- La Circulaire FINMA 2008/7 s'applique aux relations d'externalisation
- Les externalisations significatives nécessitent une notification à la FINMA
- Les stratégies de sortie et la planification de la transition sont obligatoires

---

## Marge 56 : Authentification et contrôle des accès

**Exigence** :
Mettre en œuvre des mécanismes d'authentification et de contrôle des accès robustes :

- Identification et authentification des utilisateurs
- Comptes utilisateurs uniques (pas de comptes partagés)
- Authentification multi-facteurs pour les systèmes critiques
- Accès au moindre privilège
- Révisions régulières des accès

**Exigences spécifiques** :

**Authentification** :

- Authentification robuste pour tous les utilisateurs
- Authentification multi-facteurs (AMF) pour :
  - L'accès distant
  - Les comptes à privilèges
  - L'accès aux données sensibles
- Politiques de complexité des mots de passe et de rotation
- Verrouillage de compte après tentatives infructueuses

**Contrôle des accès** :

- Contrôle des accès basé sur les rôles (RBAC)
- Principe du moindre privilège
- Recertification régulière des accès (au moins annuellement)
- Provisionnement et déprovisionnement automatisés
- Gestion des accès à privilèges (PAM) pour les administrateurs

**Correspondance ISO 27001:2022** :

- A.5.15 : Contrôle des accès
- A.5.16 : Gestion des identités
- A.5.17 : Informations d'authentification
- A.5.18 : Droits d'accès
- A.8.2 : Droits d'accès à privilèges
- A.8.3 : Restriction de l'accès à l'information
- A.8.5 : Authentification sécurisée

**Orientations de mise en œuvre** :

- Plateforme de Gestion des Identités et des Accès (GIA)
- Authentification Unique (SSO) avec AMF
- Solution de Gestion des Accès à Privilèges (PAM)
- Revues d'accès automatisées et recertification
- Automatisation du processus Arrivées/Mobilités/Départs (AMD)

---

## Marge 58 : Séparation des tâches

**Exigence** :
Définir et mettre en œuvre la séparation des tâches (SdT) afin de prévenir les conflits d'intérêts et de réduire le risque de fraude :

- Identifier les processus métier critiques nécessitant une SdT
- Définir les rôles et activités incompatibles
- Mettre en œuvre des contrôles pour prévenir les violations de SdT
- Surveiller et détecter les conflits de SdT
- Contrôles compensatoires lorsque la SdT n'est pas réalisable

**Exemples de séparations critiques** :

- Développement vs. accès en production
- Initiateur de changement vs. approbateur de changement
- Initiateur de paiement vs. approbateur de paiement
- Administrateur de sécurité vs. administrateur de système
- Administrateur de sauvegardes vs. demandeur de restauration

**Correspondance ISO 27001:2022** :

- A.5.15 : Contrôle des accès (principe de séparation des tâches)
- A.5.18 : Droits d'accès (séparation basée sur les rôles)
- A.8.2 : Droits d'accès à privilèges (séparation administrative)

**Approches de mise en œuvre** :

- Contrôle des accès basé sur les rôles (RBAC) avec règles de SdT
- Détection automatisée des conflits de SdT (p. ex. SAP GRC, Oracle GRC)
- Rapports réguliers sur les violations de SdT et remédiation
- Documentation des contrôles compensatoires (p. ex. surveillance renforcée, double autorisation)

**Attentes FINMA** :

- Matrice de SdT documentant les activités incompatibles
- Surveillance automatisée de la SdT dans la mesure du possible
- Rapport trimestriel sur les violations de SdT à la direction
- Sensibilisation du conseil d'administration aux lacunes critiques de SdT

---

## Marge 62 : Chiffrement

**Exigence** :
Mettre en œuvre la cryptographie pour protéger les données sensibles :

- Chiffrement des données au repos et en transit
- Gestion des clés de chiffrement
- Alignement sur les standards de chiffrement actuels
- Révision cryptographique régulière

**Exigences spécifiques** :

**Données en transit** :

- TLS 1.2 au minimum (TLS 1.3 préféré)
- Suites de chiffrement robustes (aucun algorithme obsolète)
- Gestion et rotation des certificats
- Protocoles sécurisés pour toutes les transmissions de données sensibles

**Données au repos** :

- Chiffrement intégral du disque pour les terminaux (ordinateurs portables, appareils mobiles)
- Chiffrement des bases de données pour les données sensibles
- Chiffrement de fichiers/dossiers pour les documents confidentiels
- Chiffrement des sauvegardes

**Gestion des clés** :

- Système centralisé de gestion des clés
- Séparation de la gestion des clés de l'accès aux données
- Rotation et gestion du cycle de vie des clés
- Stockage sécurisé des clés (Module de Sécurité Matériel de préférence)
- Procédures de sauvegarde et de récupération des clés

**Standards de chiffrement** :

- AES-256 pour le chiffrement symétrique
- RSA 2048 bits minimum ou ECC 256 bits pour le chiffrement asymétrique
- SHA-256 minimum pour le hachage
- Aucun recours aux algorithmes obsolètes (DES, 3DES, MD5, SHA-1)

**Correspondance ISO 27001:2022** :

- A.8.24 : Utilisation de la cryptographie

**Orientations de mise en œuvre** :

- Microsoft BitLocker / FileVault pour le chiffrement des terminaux
- Azure Key Vault / AWS KMS pour la gestion des clés dans le cloud
- Module de Sécurité Matériel (HSM) pour les clés à haute valeur
- Gestion du cycle de vie des certificats (Let's Encrypt, DigiCert, etc.)
- Inventaire cryptographique régulier et analyse de conformité

---

## Marges 63–72 : Journalisation et surveillance

**Marges 63–65 : Journalisation des événements de sécurité**

**Exigence** :
Journalisation complète des événements pertinents pour la sécurité :

- Authentification et autorisation des utilisateurs
- Opérations privilégiées
- Changements et configurations du système
- Incidents et alertes de sécurité
- Accès aux données (notamment aux données sensibles)

**Contenu requis des journaux** :

- Qui : Identification de l'utilisateur
- Quoi : Action effectuée
- Quand : Horodatage (synchronisé)
- Où : Système/application/adresse IP
- Résultat : Succès ou échec

**Conservation des journaux** :

- Journaux de sécurité : 12 mois minimum (attente FINMA)
- Journaux d'audit : 10 ans (selon le type de données)
- Journaux de sauvegarde pour la conservation à long terme

**Correspondance ISO 27001:2022** :

- A.8.15 : Journalisation
- A.8.16 : Activités de surveillance

---

**Marges 66–68 : Gestion centralisée des journaux**

**Exigence** :
Collecte, stockage et analyse centralisés des journaux de sécurité :

- SIEM (Security Information and Event Management) ou équivalent
- Collecte des journaux en temps réel depuis tous les systèmes critiques
- Protection de l'intégrité des journaux (journaux immuables)
- Stockage sécurisé des journaux avec contrôles d'accès

**Capacités du SIEM** :

- Agrégation des journaux de sources multiples
- Corrélation et analyse
- Alertes et notifications
- Rapports et tableaux de bord
- Intégration avec la réponse aux incidents

**Correspondance ISO 27001:2022** :

- A.8.15 : Journalisation (gestion centralisée des journaux)
- A.8.16 : Activités de surveillance (corrélation SIEM)

**Exemples de mise en œuvre** :

- Splunk Enterprise Security
- Microsoft Sentinel (Azure)
- Elastic Security (pile ELK)
- IBM QRadar
- LogRhythm

---

**Marges 69–72 : Surveillance en temps réel et alertes**

**Exigence** :
Surveillance continue et alertes en temps réel pour les événements de sécurité :

- Surveillance de sécurité 24h/24 7j/7 (SOC ou équivalent)
- Alertes automatisées pour les événements de sécurité critiques
- Procédures d'escalade définies
- Intégration avec la réponse aux incidents

**Catégories d'alertes** :

- Critique : Réponse immédiate requise (dans les 15 minutes)
- Élevée : Réponse dans l'heure
- Moyenne : Réponse dans les 4 heures
- Faible : Réponse dans les 24 heures

**Événements surveillés** :

- Tentatives d'authentification infructueuses (force brute)
- Utilisation de comptes à privilèges
- Tentatives d'accès non autorisées
- Détection de logiciels malveillants
- Indicateurs d'exfiltration de données
- Changements de configuration du système
- Défaillances des contrôles de sécurité

**Correspondance ISO 27001:2022** :

- A.8.16 : Activités de surveillance
- A.5.24 : Planification et préparation de la gestion des incidents liés à la sécurité de l'information
- A.5.25 : Évaluation des événements liés à la sécurité de l'information et décisions

**Approches de mise en œuvre** :

- SOC (Centre des Opérations de Sécurité) interne
- Fournisseur de Services de Sécurité Gérés (MSSP)
- SOC co-géré (modèle hybride)

---

## Marges 73–87 : Continuité des activités et résilience

**Aperçu** :
Les Marges 73–87 de la Circulaire FINMA 2023/1 établissent des exigences complètes de continuité des activités et de reprise après sinistre pour les établissements financiers suisses.

**Marges 73–75 : Analyse d'Impact sur les Activités (AIA)**

**Exigence** :
Réaliser des Analyses d'Impact sur les Activités régulières afin de :

- Identifier les processus métier critiques
- Définir les Objectifs de Délai de Reprise (ODR)
- Définir les Objectifs de Point de Reprise (OPR)
- Évaluer l'impact financier et opérationnel

**Correspondance ISO 27001:2022** :

- Clause 8.1 : Planification et contrôle opérationnels (contexte de continuité des activités)
- A.5.29 : Sécurité de l'information lors d'une perturbation
- A.5.30 : Préparation des TIC à la continuité des activités

**Attentes FINMA** :

- ODR pour les processus critiques : généralement 2–4 heures
- OPR pour les données critiques : généralement 15 minutes à 1 heure
- Révision et mise à jour annuelles de l'AIA
- Approbation par le conseil d'administration des objectifs ODR/OPR

---

**Marges 76–80 : Plans de Continuité des Activités (PCA)**

**Exigence** :
Plans de continuité des activités documentés et testés incluant :

- Procédures de réponse aux incidents
- Structure de gestion de crise
- Plans de communication (internes et externes)
- Sites de traitement alternatifs
- Procédures de sauvegarde et de récupération des données

**Composantes du plan** :

- Rôles et responsabilités (Équipe de Gestion de Crise)
- Critères d'activation et d'escalade
- Protocoles de communication (exigences de notification à la FINMA)
- Procédures de reprise (étape par étape)
- Coordination avec les fournisseurs et prestataires
- Retour aux opérations normales

**Correspondance ISO 27001:2022** :

- A.5.29 : Sécurité de l'information lors d'une perturbation
- A.5.30 : Préparation des TIC à la continuité des activités
- A.8.13 : Sauvegarde de l'information
- A.8.14 : Redondance des installations de traitement de l'information

---

**Marges 81–84 : Tests et validation**

**Exigence** :
Tests réguliers des capacités de continuité des activités et de reprise après sinistre :

- Test de PRA complet annuel (minimum)
- Tests partiels trimestriels ou semestriels
- Exercices sur table
- Tests de composants (restauration des sauvegardes, basculement)

**Types de tests** :

- **Exercice sur table** : Basé sur la discussion, sans activation de systèmes
- **Test partiel** : Test de composants spécifiques (p. ex. basculement de base de données)
- **Test PRA complet** : Basculement complet vers le site alternatif
- **Test-surprise** : Activation sans préavis pour tester l'état de préparation

**Correspondance ISO 27001:2022** :

- A.5.30 : Préparation des TIC à la continuité des activités (exigence de tests)

**Attentes FINMA** :

- Test PRA complet annuel documenté et rapporté
- Résultats des tests examinés par le conseil d'administration
- Les lacunes identifiées sont corrigées dans un délai défini
- L'implication des tiers est testée (partenaires d'externalisation)

---

**Marges 85–87 : Gestion des incidents et notification**

**Exigence** :
Processus formel de gestion des incidents incluant :

- Classification et niveaux de gravité des incidents
- Procédures d'escalade
- Exigences de notification à la FINMA
- Analyse des causes profondes
- Retours d'expérience et amélioration continue

**Notification d'incidents à la FINMA** :
Les banques doivent notifier la FINMA des :

- **Immédiatement** : Incidents majeurs affectant les processus métier critiques
- **Dans les 24 heures** : Violations de sécurité, fuites de données, pannes significatives
- **Après l'incident** : Rapport d'incident détaillé dans un délai défini

**Contenu du rapport** :

- Description de l'incident et chronologie
- Évaluation de l'impact (clients, opérations, financier)
- Analyse des causes profondes
- Actions correctives prises
- Mesures pour prévenir toute récurrence

**Correspondance ISO 27001:2022** :

- A.5.24 : Planification et préparation de la gestion des incidents liés à la sécurité de l'information
- A.5.25 : Évaluation des événements liés à la sécurité de l'information et décisions
- A.5.26 : Réponse aux incidents liés à la sécurité de l'information
- A.5.27 : Apprentissage tiré des incidents liés à la sécurité de l'information
- A.5.28 : Collecte de preuves

---

# Circulaire FINMA 2008/7 — Externalisation (Banques)

## Aperçu

La Circulaire FINMA 2008/7 établit les exigences pour les banques externalisant des fonctions métier ou des services informatiques à des prestataires tiers.

**Applicabilité** :

- S'applique aux banques et négociants en valeurs mobilières
- Couvre l'externalisation de fonctions significatives
- Inclut l'externalisation nationale et transfrontalière
- Les services cloud sont considérés comme une externalisation

## Exigences clés

**Évaluation des risques** :

- Évaluation complète des risques avant l'externalisation
- Évaluation des capacités du prestataire de services
- Évaluation du risque de concentration
- Considérations de résidence et de souveraineté des données

**Exigences contractuelles** :

- Définition claire des services et des SLA
- Obligations de sécurité et de confidentialité
- Droit d'audit et d'accès à l'information
- Restrictions de sous-traitance
- Clauses de protection des données
- Exigences de continuité des activités
- Dispositions de stratégie de sortie et de transition

**Surveillance continue** :

- Révisions régulières des performances du prestataire de services
- Évaluations et audits de sécurité périodiques
- Exigences de notification des incidents
- Attestation annuelle de conformité (p. ex. SOC 2 Type II)

**Correspondance ISO 27001:2022** :

- A.5.19 : Sécurité de l'information dans les relations avec les fournisseurs
- A.5.20 : Prise en compte de la sécurité de l'information dans les accords avec les fournisseurs
- A.5.21 : Gestion de la sécurité de l'information dans la chaîne d'approvisionnement TIC
- A.5.22 : Surveillance, révision et gestion des changements des services fournisseurs
- A.5.23 : Sécurité de l'information pour l'utilisation des services cloud

---

# Mise en correspondance ISO 27001:2022 — FINMA

## Matrice de correspondance des contrôles

| Exigence FINMA | Marge FINMA | Contrôle ISO 27001:2022 | Priorité de mise en œuvre |
|----------------|-------------|-------------------------|---------------------------|
| Stratégie de sécurité de l'information | 50 | Clause 5.2, A.5.1 | Critique |
| Organisation de la sécurité | 51 | Clause 5.3, A.5.2 | Critique |
| Évaluation des risques | 52 | Clause 6.1.2, 6.1.3, 8.2, 8.3 | Critique |
| Politiques de sécurité | 53 | A.5.1, A.5.10, A.5.12 | Critique |
| Sensibilisation et formation | 54 | A.6.3 | Élevée |
| Risques liés aux tiers | 55 | A.5.19, A.5.20, A.5.21 | Critique |
| Authentification et contrôle des accès | 56 | A.5.15, A.5.16, A.5.17, A.5.18, A.8.2, A.8.3, A.8.5 | Critique |
| Séparation des tâches | 58 | A.5.15, A.5.18, A.8.2 | Critique |
| Chiffrement | 62 | A.8.24 | Critique |
| Journalisation de sécurité | 63–65 | A.8.15 | Critique |
| Gestion centralisée des journaux | 66–68 | A.8.15, A.8.16 | Critique |
| Surveillance et alertes | 69–72 | A.8.16, A.5.24, A.5.25 | Critique |
| Analyse d'Impact sur les Activités | 73–75 | A.5.29, A.5.30 | Critique |
| Plans de Continuité des Activités | 76–80 | A.5.29, A.5.30, A.8.13, A.8.14 | Critique |
| Tests PCA/PRA | 81–84 | A.5.30 | Critique |
| Gestion des incidents | 85–87 | A.5.24, A.5.25, A.5.26, A.5.27, A.5.28 | Critique |
| Externalisation (FINMA 2008/7) | N/A | A.5.19, A.5.20, A.5.21, A.5.22, A.5.23 | Critique |

## Approche d'analyse des écarts

Pour les organisations soumises à la FINMA :

**Étape 1** : Confirmer le statut d'applicabilité FINMA
**Étape 2** : Réaliser une évaluation de référence de la conformité ISO 27001:2022
**Étape 3** : Identifier les exigences FINMA spécifiques au-delà d'ISO 27001
**Étape 4** : Documenter les écarts et élaborer un plan de remédiation
**Étape 5** : Prioriser les marges FINMA critiques (56, 58, 62, 63–72)
**Étape 6** : Mettre en œuvre les contrôles avec des preuves de conformité FINMA
**Étape 7** : Réaliser un audit interne avec focus FINMA
**Étape 8** : Se préparer à une éventuelle inspection FINMA

## Exigences en matière de preuves de conformité

La FINMA attend des preuves documentées de :

- Politiques et procédures approuvées par la direction
- Évaluations des risques et décisions de traitement
- Configurations et révisions du contrôle des accès
- Capacités de conservation des journaux et de surveillance
- Résultats des tests PCA/PRA et actions correctives
- Rapports d'incidents et retours d'expérience
- Évaluations des risques liés aux tiers et contrats
- Rapports d'audit (internes et externes)

---

# Considérations de mise en œuvre

## Calendrier de conformité FINMA

**Si [Organisation] devient réglementée par la FINMA** :

**Mois 1–3 : Évaluation des écarts**

- Confirmer la détermination de l'applicabilité FINMA
- Documenter l'état actuel de conformité ISO 27001
- Identifier les écarts spécifiques à la FINMA
- Prioriser les activités de remédiation

**Mois 4–6 : Mise en œuvre des contrôles critiques**

- Authentification et contrôle des accès (Marge 56)
- Séparation des tâches (Marge 58)
- Chiffrement (Marge 62)
- Infrastructure de journalisation (Marges 63–68)

**Mois 7–9 : Surveillance et résilience**

- Mise en œuvre et réglage du SIEM (Marges 69–72)
- Renforcement de la continuité des activités (Marges 73–80)
- Procédures de réponse aux incidents (Marges 85–87)

**Mois 10–12 : Tests et validation**

- Audit interne avec focus FINMA
- Tests PCA/PRA (Marges 81–84)
- Documentation des preuves de conformité
- Rapports à la direction et au conseil d'administration

**Continu** : Cycle annuel de tests, d'évaluation et d'amélioration

## Ressources nécessaires

**Personnel** :

- RSSI ou équivalent (exigé par la FINMA)
- Responsable de la Conformité avec expertise FINMA
- Équipe des Opérations de Sécurité (SOC)
- Responsable de la Continuité des Activités
- Audit Interne avec expertise en sécurité informatique

**Technologie** :

- Plateforme de Gestion des Identités et des Accès (GIA)
- Gestion des Accès à Privilèges (PAM)
- Plateforme SIEM avec surveillance 24h/24 7j/7
- Gestion des clés de chiffrement (HSM ou KMS cloud)
- Outils de continuité des activités et site alternatif

**Support externe** :

- Conseil juridique avec expérience en réglementation financière suisse
- Auditeurs externes familiers des exigences FINMA
- Fournisseur de Services de Sécurité Gérés (MSSP) si nécessaire

## Implications financières

La conformité FINMA nécessite généralement :

- Une technologie de sécurité renforcée (GIA, PAM, SIEM, HSM)
- Des effectifs accrus (RSSI, SOC, conformité)
- Des honoraires d'audit et de conseil externes
- Une infrastructure de continuité des activités (site de PRA)
- Des programmes permanents de formation et de sensibilisation

Coût supplémentaire estimé : augmentation de 15–25 % par rapport à la conformité ISO 27001 de base pour les petits et moyens établissements financiers.

---

# Défis courants et retours d'expérience

## Défis courants en matière de conformité FINMA

**Défi 1 : Sous-estimer la rigueur de la FINMA**

- Les inspections FINMA sont approfondies et fondées sur des preuves
- La documentation doit être complète et à jour
- Les politiques seules sont insuffisantes ; des preuves de mise en œuvre sont requises

**Défi 2 : Séparation des tâches insuffisante**

- Les violations de SdT sont courantes dans les petits établissements
- Les contrôles compensatoires doivent être robustes et documentés
- La surveillance automatisée de la SdT est fortement recommandée

**Défi 3 : Journalisation et surveillance inadéquates**

- La conservation des journaux est souvent inférieure à l'attente FINMA (12 mois minimum)
- Le SIEM n'est pas adapté aux cas d'usage des établissements financiers
- Les effectifs du SOC sont insuffisants pour une couverture 24h/24 7j/7

**Défi 4 : Lacunes dans les tests PCA/PRA**

- Les tests PRA complets ne sont pas réalisés annuellement
- Les résultats des tests ne sont pas documentés de manière adéquate
- Les lacunes ne sont pas corrigées dans les délais impartis

**Défi 5 : Gestion des risques d'externalisation**

- Les services cloud sont traités comme une « technologie » plutôt que comme une externalisation
- Les exigences de notification à la FINMA sont manquées
- Les clauses de droit d'audit sont absentes des contrats

## Bonnes pratiques

**Pratique 1** : Faire appel tôt à des auditeurs expérimentés en matière FINMA
**Pratique 2** : Réaliser des révisions internes trimestrielles de conformité FINMA
**Pratique 3** : Maintenir un référentiel complet de preuves de conformité
**Pratique 4** : Intégrer les exigences FINMA dans la gestion des changements
**Pratique 5** : Former le conseil d'administration et la direction générale aux attentes FINMA
**Pratique 6** : Établir un canal de communication direct avec le superviseur FINMA

---

# Références et ressources

## Publications FINMA

**Sources primaires** :

- Circulaire FINMA 2023/1 : Risques opérationnels et résilience — banques
- Circulaire FINMA 2008/7 : Externalisation — banques
- Circulaire FINMA 2018/3 : Externalisation — assureurs
- Guidance FINMA 05/2023 : Externalisation vers le cloud

**Site web FINMA** : https://www.finma.ch/
**Circulaires FINMA** : https://www.finma.ch/fr/documentation/circulaires-finma/

## Normes et cadres connexes

**Normes ISO** :

- ISO/IEC 27001:2022 : Systèmes de Management de la Sécurité de l'Information
- ISO/IEC 27002:2022 : Contrôles de sécurité de l'information
- ISO/IEC 27017:2026 : Sécurité des services cloud
- ISO/IEC 27018:2025 : Protection des DCP dans le cloud public

**Publications NIST** :

- NIST SP 800-53 : Contrôles de sécurité et de confidentialité (référence informative)
- NIST Cybersecurity Framework (référence informative)

**Orientations sectorielles** :

- Association Suisse des Banquiers : Directives de sécurité informatique
- Directives ABE sur la gestion des risques liés aux TIC et à la sécurité (contexte UE)

## Ressources juridiques et de conformité

**Lois fédérales suisses** :

- Loi sur les marchés financiers (LFINMA)
- Loi sur les banques (LB)
- Loi fédérale sur la protection des données (nLPD)

**Conseil en conformité** :
Les organisations soumises à la surveillance FINMA devraient faire appel à :

- Un conseil juridique avec expertise en réglementation financière suisse
- Des auditeurs expérimentés dans les inspections FINMA
- Des consultants en conformité familiers des exigences FINMA

---

# Annexe A : Liste de contrôle d'auto-évaluation de la conformité FINMA

Cette liste de contrôle soutient l'évaluation initiale des écarts pour les organisations soumises à la surveillance FINMA :

## Cadre de sécurité de l'information (Marges 50–55)

| Exigence | Statut | Emplacement de la preuve | Notes |
|----------|--------|--------------------------|-------|
| Stratégie de sécurité de l'information documentée et approuvée par le conseil | ⬜ Oui ⬜ Non ⬜ Partiel | | |
| Rôle de RSSI ou équivalent établi | ⬜ Oui ⬜ Non | | |
| Évaluation annuelle des risques liés à la sécurité de l'information réalisée | ⬜ Oui ⬜ Non | | |
| Politiques de sécurité complètes documentées | ⬜ Oui ⬜ Non ⬜ Partiel | | |
| Formation annuelle de sensibilisation à la sécurité pour tout le personnel | ⬜ Oui ⬜ Non | | |
| Processus d'évaluation des risques liés aux tiers établi | ⬜ Oui ⬜ Non ⬜ Partiel | | |

## Authentification et contrôle des accès (Marge 56)

| Exigence | Statut | Emplacement de la preuve | Notes |
|----------|--------|--------------------------|-------|
| AMF mise en œuvre pour l'accès distant | ⬜ Oui ⬜ Non ⬜ Partiel | | |
| AMF mise en œuvre pour les comptes à privilèges | ⬜ Oui ⬜ Non ⬜ Partiel | | |
| Contrôle des accès basé sur les rôles (RBAC) mis en œuvre | ⬜ Oui ⬜ Non ⬜ Partiel | | |
| Recertification annuelle des accès réalisée | ⬜ Oui ⬜ Non | | |
| Gestion des Accès à Privilèges (PAM) mise en œuvre | ⬜ Oui ⬜ Non ⬜ Partiel | | |

## Séparation des tâches (Marge 58)

| Exigence | Statut | Emplacement de la preuve | Notes |
|----------|--------|--------------------------|-------|
| Matrice de SdT documentée | ⬜ Oui ⬜ Non ⬜ Partiel | | |
| Surveillance automatisée de la SdT mise en œuvre | ⬜ Oui ⬜ Non | | |
| Violations de SdT rapportées trimestriellement | ⬜ Oui ⬜ Non | | |
| Contrôles compensatoires documentés pour les conflits de SdT inévitables | ⬜ Oui ⬜ Non ⬜ Partiel | | |

## Chiffrement (Marge 62)

| Exigence | Statut | Emplacement de la preuve | Notes |
|----------|--------|--------------------------|-------|
| TLS 1.2+ pour toutes les données en transit | ⬜ Oui ⬜ Non ⬜ Partiel | | |
| Chiffrement intégral du disque pour les terminaux | ⬜ Oui ⬜ Non ⬜ Partiel | | |
| Chiffrement des bases de données pour les données sensibles | ⬜ Oui ⬜ Non ⬜ Partiel | | |
| Système centralisé de gestion des clés | ⬜ Oui ⬜ Non | | |
| Aucun recours aux algorithmes de chiffrement obsolètes | ⬜ Oui ⬜ Non | | |

## Journalisation et surveillance (Marges 63–72)

| Exigence | Statut | Emplacement de la preuve | Notes |
|----------|--------|--------------------------|-------|
| Journalisation complète des événements de sécurité | ⬜ Oui ⬜ Non ⬜ Partiel | | |
| Conservation des journaux 12+ mois | ⬜ Oui ⬜ Non | | |
| Gestion centralisée des journaux (SIEM) | ⬜ Oui ⬜ Non | | |
| Surveillance de sécurité 24h/24 7j/7 (SOC) | ⬜ Oui ⬜ Non | | |
| Alertes en temps réel pour les événements critiques | ⬜ Oui ⬜ Non ⬜ Partiel | | |

## Continuité des activités (Marges 73–87)

| Exigence | Statut | Emplacement de la preuve | Notes |
|----------|--------|--------------------------|-------|
| Analyse d'Impact sur les Activités (AIA) réalisée | ⬜ Oui ⬜ Non | | |
| ODR/OPR définis et approuvés par le conseil | ⬜ Oui ⬜ Non | | |
| Plans de continuité des activités documentés | ⬜ Oui ⬜ Non ⬜ Partiel | | |
| Test PRA complet annuel réalisé | ⬜ Oui ⬜ Non | | |
| Procédures de réponse aux incidents documentées | ⬜ Oui ⬜ Non ⬜ Partiel | | |
| Processus de notification des incidents à la FINMA établi | ⬜ Oui ⬜ Non | | |

## Externalisation (FINMA 2008/7)

| Exigence | Statut | Emplacement de la preuve | Notes |
|----------|--------|--------------------------|-------|
| Arrangements d'externalisation significatifs notifiés à la FINMA | ⬜ Oui ⬜ Non ⬜ N/A | | |
| Évaluations des risques des prestataires de services réalisées | ⬜ Oui ⬜ Non ⬜ Partiel | | |
| Les contrats incluent des clauses de droit d'audit | ⬜ Oui ⬜ Non ⬜ Partiel | | |
| Rapports SOC 2 Type II annuels obtenus auprès des prestataires | ⬜ Oui ⬜ Non ⬜ Partiel | | |
| Stratégies de sortie documentées pour les prestataires critiques | ⬜ Oui ⬜ Non ⬜ Partiel | | |

---

# Annexe B : Modèle de notification FINMA

**Objet** : Notification de [Type d'incident] — [Nom de l'organisation]

**À** : Équipe de surveillance FINMA
**De** : [Nom du RSSI / Responsable de la Conformité]
**Date** : [Date]
**Organisation** : [Dénomination sociale]
**Numéro de licence FINMA** : [Numéro]

**Résumé de l'incident** :

- **Type d'incident** : [Violation de sécurité / Panne de système / Perte de données / Autre]
- **Date/heure de découverte** : [Format ISO 8601]
- **Date/heure de début de l'incident** : [Format ISO 8601]
- **Statut actuel** : [En cours / Contenu / Résolu]

**Évaluation de l'impact** :

- **Processus métier critiques affectés** : [Liste]
- **Impact client** : [Nombre de clients, perturbation du service]
- **Impact sur les données** : [Types et volume de données affectés]
- **Impact financier** : [Estimé si connu]

**Cause profonde** (préliminaire si l'incident est en cours) :
[Brève description]

**Actions correctives prises** :
1. [Action 1 — date/heure]
2. [Action 2 — date/heure]
3. [Action 3 — date/heure]

**Actions en cours** :

- [Action avec date d'achèvement prévue]

**Parties externes notifiées** :

- [Clients : Oui/Non/Prévu]
- [Autorité de protection des données : Oui/Non/N/A]
- [Autres régulateurs : Préciser]

**Prochaine mise à jour** : [Date/heure de la prochaine mise à jour à la FINMA]

**Coordonnées** :

- **Contact principal** : [Nom, Titre, Téléphone, E-mail]
- **Contact alternatif** : [Nom, Titre, Téléphone, E-mail]

---

**FIN DE LA RÉFÉRENCE TECHNIQUE**

---

*Cette référence technique soutient les exigences potentielles de conformité FINMA telles que déterminées dans ISMS-POL-00. Toutes les déterminations d'applicabilité réglementaire et les exigences contraignantes sont définies dans ISMS-POL-00 et les documents de politique SMSI approuvés.*

*Pour les organisations NON soumises à la surveillance FINMA, ce document est fourni à titre de sensibilisation informative uniquement et ne crée PAS d'obligations de conformité.*

<!-- QA_VERIFIED: 2026-03-30 -->
