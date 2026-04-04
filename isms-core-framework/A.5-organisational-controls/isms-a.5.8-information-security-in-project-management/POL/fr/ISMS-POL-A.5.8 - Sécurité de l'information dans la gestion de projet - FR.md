<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.8-FR:framework:POL:a.5.8 -->
**ISMS-POL-A.5.8 — Sécurité de l'information dans la gestion de projet**

---

**Contrôle documentaire**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Sécurité de l'information dans la gestion de projet |
| **Type de document** | Politique |
| **Identifiant du document** | ISMS-POL-A.5.8 |
| **Créateur du document** | Responsable de la sécurité des systèmes d'information (RSSI) |
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
| 1.0 | [Date] | RSSI | Cadre de politique initial |

**Cycle de révision** : Annuel
**Prochaine date de révision** : [Date à définir]

---

# Résumé exécutif

La présente politique établit les exigences de [Organisation] pour l'intégration de la sécurité de l'information dans la gestion de projet, afin de s'assurer que les risques de sécurité sont traités de manière systématique tout au long du cycle de vie du projet, conformément au contrôle A.5.8 de l'ISO/IEC 27001:2022.

**Objet** : Définir les exigences organisationnelles pour l'intégration de la sécurité de l'information dans les processus de gestion de projet. Cette politique établit QUELLES activités de sécurité sont requises à chaque phase du projet et QUI est responsable des résultats en matière de sécurité.

**Périmètre** : Cette politique s'applique à tous les projets menés par [Organisation], quel que soit leur type, leur méthodologie, leur complexité, leur taille, leur durée ou leur portée organisationnelle, y compris les projets gérés par des équipes internes, des prestataires externes ou des structures hybrides.

**Alignement réglementaire** : Cette politique répond aux exigences de conformité obligatoires définies dans ISMS-POL-00 (Cadre d'applicabilité réglementaire), notamment le nLPD suisse (art. 8), le RGPD de l'UE (art. 25) et l'ISO/IEC 27001:2022. Des exigences sectorielles conditionnelles (NIS2, DORA, FINMA) s'appliquent lorsque les activités de [Organisation] déclenchent leur applicabilité.

---

# Périmètre et applicabilité

## Contrôle ISO/IEC 27001:2022 A.5.8

> *La sécurité de l'information devrait être intégrée dans la gestion de projet.*

**Objectif du contrôle** : S'assurer que les risques de sécurité de l'information associés aux projets et aux livrables sont systématiquement identifiés, évalués et traités tout au long du cycle de vie du projet.

## Dans le périmètre

Cette politique s'applique à :

- **Projets informatiques** : Développement logiciel, implémentation de systèmes, déploiement d'infrastructures
- **Projets métier** : Reengineering de processus, changement organisationnel, activités de fusion/acquisition
- **Projets d'infrastructure** : Construction de datacentres, modifications d'installations, installation d'équipements
- **Projets de conformité** : Mise en œuvre réglementaire, remédiation d'audit, programmes de certification
- Projets de toutes tailles et durées
- Projets quelle que soit la méthodologie de gestion (Agile, Waterfall, hybride)
- Projets gérés par des équipes internes, des prestataires externes ou des équipes mixtes
- Toutes les phases du projet : Initialisation, planification, exécution, surveillance/contrôle, clôture

## Hors périmètre

- Les activités opérationnelles courantes ne constituant pas un projet (maintenance en mode normal)
- Les activités de réponse aux incidents d'urgence (couvertes par A.5.24-27 Gestion des incidents)
- Les modifications mineures gérées via le processus de gestion des changements (couvertes par A.8.32)

## Exigences réglementaires

**Niveau 1 — Conformité obligatoire** :

- nLPD suisse (art. 8) : Mesures techniques et organisationnelles appropriées
- RGPD UE (art. 25, 32) : Protection des données dès la conception et par défaut
- ISO/IEC 27001:2022 : Contrôle A.5.8 — sécurité de l'information dans la gestion de projet

**Niveau 2 — Applicabilité conditionnelle** (conformément à ISMS-POL-00) :

- NIS2, DORA, Circulaire FINMA 2008/21, PCI DSS v4.0.1 — s'appliquent lorsque les conditions métier déclenchent l'applicabilité

---

# Énoncés de politique

## Principes d'intégration de la sécurité dans les projets

[Organisation] DOIT intégrer la sécurité de l'information dans tous les projets sur la base des principes suivants :

| Principe | Exigence | Exemple d'application |
|----------|----------|----------------------|
| **Intégration précoce** | La sécurité DOIT être considérée dès l'initialisation du projet, non ajoutée après coup | La charte de projet inclut la classification de sécurité ; les ressources de sécurité sont allouées dans le budget du projet avant la phase de planification |
| **Proportionnalité** | L'effort de sécurité DOIT être proportionnel à la classification du risque du projet | Un outil interne à faible risque reçoit une validation par liste de contrôle (2 heures) ; un portail client à risque élevé reçoit un test de pénétration (40 heures) |
| **Couverture du cycle de vie** | Les activités de sécurité DOIVENT se produire à toutes les phases du projet | Revue de sécurité à chaque porte de phase ; exigences de sécurité en planification, tests en exécution, transfert à la clôture |
| **Fondé sur les risques** | Les décisions de sécurité DOIVENT être fondées sur l'évaluation des risques | Contrôles de sécurité sélectionnés sur la base de la modélisation des menaces et de la classification des données, non sur des listes génériques |
| **Exigences traçables** | Les exigences de sécurité DOIVENT être documentées et suivies jusqu'à leur mise en œuvre | Le registre des exigences de sécurité relie chaque exigence à un élément de conception, un cas de test et une preuve de déploiement |
| **Enseignements tirés** | Les expériences de sécurité du projet DOIVENT alimenter l'amélioration continue | La revue de sécurité post-projet identifie les lacunes de contrôle ; les résultats mettent à jour les modèles d'exigences |

## Exigence de classification des projets

Tous les projets DOIVENT être classifiés en fonction de leur impact sur la sécurité de l'information pour déterminer les exigences de sécurité proportionnelles.

**Facteurs de classification et matrice de décision** :

Les projets DOIVENT être classifiés sur la base du facteur le plus élevé applicable :

| Facteur | Risque élevé | Risque moyen | Risque faible |
|---------|--------------|--------------|---------------|
| **Sensibilité des données** | Données critiques/confidentielles (DCP, données de paiement, PI, informations métier confidentielles conformément à A.5.12) | Données internes (données métier non publiques, dossiers des employés) | Données publiques (contenu marketing, documentation publiée) |
| **Criticité du système** | RTO < 4 heures, système générateur de revenus, service client | RTO 4-24 heures, important pour l'activité mais non critique pour les revenus | RTO > 24 heures, système de support opérationnel |
| **Périmètre réglementaire** | RGPD/PCI DSS v4.0.1/FINMA directement applicables | nLPD suisse applicable | Aucun traitement de données réglementées |
| **Exposition externe** | Accessible depuis Internet ou par des parties externes (clients, partenaires, public) | Accès externe contrôlé (VPN, connexion dédiée) | Accès interne uniquement |
| **Complexité technique** | Nouveau schéma d'architecture, intégrations nouvelles, contrôles de sécurité personnalisés | Architecture standard avec personnalisation modérée | Déploiement standard, architecture éprouvée |
| **Implication de tiers** | Fonction critique externalisée (hébergement, authentification, traitement des paiements) | Composants gérés par un fournisseur (intégration SaaS, services gérés) | Développement et hébergement entièrement internes |

**Logique de classification** : Si **un facteur** répond aux critères Risque élevé → classifier en **Risque élevé**. Si **un facteur** répond aux critères Risque moyen (et aucun facteur à Risque élevé) → classifier en **Risque moyen**. Si **tous les facteurs** répondent aux critères Risque faible → classifier en **Risque faible**.

**Documentation de la classification** : La détermination de la classification et sa justification DOIVENT être documentées dans la charte de projet et approuvées conformément à l'autorité d'approbation ci-dessous.

**Niveaux de classification** :

| Classification | Description | Autorité d'approbation |
|----------------|-------------|------------------------|
| **Risque élevé** | Impact critique sur la sécurité de l'information | Approbation du RSSI requise |
| **Risque moyen** | Impact modéré sur la sécurité de l'information | Approbation du responsable sécurité de l'information |
| **Risque faible** | Impact minimal sur la sécurité de l'information | Auto-classification par le chef de projet avec revue InfoSec |

La classification DOIT être révisée à chaque porte de phase et mise à jour si le périmètre, la sensibilité des données ou l'exposition externe change de manière significative.

## Exigences des portes de phase sécurité

[Organisation] DOIT intégrer des revues de sécurité dans la gouvernance des projets aux portes de phase suivantes :

| Porte de phase | Critères de sécurité requis |
|----------------|------------------------------|
| **Approbation du projet** | Classification de sécurité déterminée ; risques de sécurité initiaux identifiés ; budget de sécurité alloué |
| **Approbation de la planification** | Exigences de sécurité documentées et approuvées ; ressources de sécurité engagées |
| **Point de contrôle de l'exécution** | Tests de sécurité réalisés ; résultats critiques remédiés |
| **Approbation du déploiement** | Tous les résultats Critiques/Élevés remédiés ou acceptés ; documentation de transfert de sécurité complète |
| **Clôture du projet** | Risques résiduels formellement acceptés ; enseignements tirés documentés ; actifs enregistrés |

Les projets NE DOIVENT PAS passer à la phase suivante tant que les critères de sécurité de la phase en cours ne sont pas satisfaits ou formellement acceptés par l'autorité compétente.

## Identification des exigences de sécurité

Les exigences de sécurité pour les livrables du projet DOIVENT être identifiées de manière systématique selon le processus suivant :

**Processus d'identification des exigences** :

1. **Évaluation de l'applicabilité** : Le chef de projet, avec le soutien du responsable sécurité, examine chaque catégorie d'exigences de sécurité par rapport au périmètre du projet :
   - Sécurité des applications (A.8.25-28) : Applicable si le projet inclut du développement logiciel ou du code personnalisé
   - Protection des données (A.8.24, RGPD/nLPD) : Applicable selon la classification des données conformément à A.5.12
   - Contrôle d'accès (A.5.15-18) : Applicable pour tous les projets (minimum : conformité à la politique de contrôle d'accès)
   - Sécurité des infrastructures (A.8.20-22) : Applicable si le projet affecte l'architecture réseau ou déploie des infrastructures
   - Sécurité des tiers (A.5.19-22) : Applicable si le projet implique des fournisseurs externes ou des services cloud
   - Exigences réglementaires (ISMS-POL-00) : Applicable selon l'analyse niveau 1/2

2. **Cadrage des exigences** : Pour les catégories applicables, les exigences spécifiques sont sélectionnées sur la base de :
   - La classification des données (Critique/Confidentiel/Interne/Public conformément à A.5.12)
   - La criticité du système (exigences RTO/RPO conformément à A.5.29-30)
   - Le profil de menaces (conformément au renseignement A.5.7 et à la modélisation des menaces du projet)
   - Les obligations réglementaires (conformément aux exigences obligatoires niveau 1/2 d'ISMS-POL-00)

3. **Documentation** : Les exigences applicables DOIVENT être documentées dans :
   - **Projets Risque moyen/élevé** : Registre des exigences de sécurité (outil de suivi formel)
   - **Projets Risque faible** : Registre des risques du projet (exigences de sécurité en tant que mesures d'atténuation des risques)

4. **Approbation** : Les exigences DOIVENT être révisées et approuvées par :
   - **Projets Risque élevé** : Approbation du RSSI avant la phase d'exécution
   - **Projets Risque moyen** : Approbation du responsable sécurité avant la phase d'exécution
   - **Projets Risque faible** : Confirmation de la complétude des exigences par le responsable sécurité

**Les procédures détaillées d'identification des exigences, les listes de contrôle par catégorie et le modèle de registre des exigences de sécurité sont fournis dans ISMS-IMP-A.5.8.**

## Exigence de tests de sécurité

Tous les projets DOIVENT inclure des tests de sécurité proportionnels à la classification du projet, avec la portée des tests déterminée comme suit :

**Exigences de tests de sécurité par classification** :

- **Projets à Risque élevé** :
  - **Obligatoires** : Test de pénétration externe (méthodologie OWASP ou équivalente), analyse automatisée des vulnérabilités (hebdomadaire pendant le développement + analyse finale avant déploiement), revue de code de sécurité pour le code personnalisé (couverture minimale de 20 % des fonctions d'authentification, d'autorisation, de protection des données et de cryptographie)
  - **Critères de test** : Le test de pénétration DOIT être réalisé par un tiers indépendant (hors équipe projet). Tous les résultats Critiques et ≥ 80 % des résultats Élevés DOIVENT être remédiés avant le déploiement.

- **Projets à Risque moyen** :
  - **Obligatoires** : Analyse automatisée des vulnérabilités (analyse finale avant déploiement), tests de sécurité fonctionnels de l'authentification, de l'autorisation, de la validation des données et de la gestion des erreurs
  - **Conditionnels** : Test de pénétration requis si le projet est exposé sur Internet OU traite des données réglementées (RGPD/PCI DSS v4.0.1)
  - **Critères de test** : Tous les résultats Critiques et ≥ 70 % des résultats Élevés DOIVENT être remédiés avant le déploiement.

- **Projets à Risque faible** :
  - **Obligatoires** : Validation de la sécurité par rapport à la liste de contrôle des exigences (minimum : vérification du contrôle d'accès A.5.15-18, vérification du chiffrement A.8.24 si applicable)
  - **Optionnels** : Analyse automatisée des vulnérabilités (recommandée mais non requise)
  - **Critères de test** : Les résultats Critiques DOIVENT être remédiés avant le déploiement.

**Documentation de la suffisance des tests** : Pour les projets Risque moyen/élevé, l'adéquation des tests DOIT être documentée dans un rapport d'évaluation de sécurité et approuvée par le responsable sécurité (Moyen) ou le RSSI (Élevé) avant l'autorisation de déploiement. Si l'objectif de remédiation n'est pas atteint, le risque résiduel DOIT être formellement accepté conformément à la section Gestion des dérogations.

**Les éléments de preuve de tests (rapports d'analyse, rapports de test de pénétration, résultats de revue de code) DOIVENT être archivés conformément à A.5.33 et fournis dans la documentation de transfert de sécurité.**

## Exigence de transfert de sécurité

À la clôture du projet, la documentation de transfert de sécurité DOIT être fournie aux opérations et validée comme complète avant l'autorisation de clôture du projet.

**Critères de complétude du transfert de sécurité** :

Le transfert de sécurité DOIT inclure la documentation suivante, remise au propriétaire opérationnel et confirmée complète via une liste de contrôle de transfert :

1. **Documentation de l'architecture de sécurité** :
   - Conception de la sécurité du système (frontières de confiance, modèle d'authentification/autorisation, implémentation du chiffrement)
   - Diagrammes de flux de données montrant la classification des données et les contrôles de protection
   - Architecture réseau (règles de pare-feu, segmentation réseau, points d'accès externes)
   - Sécurité des intégrations (authentification API, dépendances de services tiers)

2. **Procédures de sécurité opérationnelle** :
   - Exigences de surveillance (sources de journaux de sécurité, seuils d'alerte, intégration SIEM)
   - Exigences de rétention des journaux (conformément à A.8.15, périodes de rétention réglementaires)
   - Procédures de sauvegarde et de restauration (conformément à A.8.13, y compris les tests de restauration spécifiques à la sécurité)
   - Escalade de la réponse aux incidents (types d'incidents de sécurité, voies d'escalade, coordonnées)
   - Gestion des correctifs de sécurité (fréquence de mise à jour, exigences de test, procédures de retour arrière)

3. **Risques résiduels acceptés** :
   - Relevés d'acceptation formelle des risques avec signatures d'approbation (selon l'autorité de classification des risques)
   - Contrôles compensatoires (le cas échéant)
   - Calendrier de réévaluation des risques (pour les acceptations limitées dans le temps)

4. **Éléments de preuve des tests de sécurité** :
   - Rapport final d'analyse de vulnérabilités (daté dans les 7 jours suivant le déploiement)
   - Rapport de test de pénétration (le cas échéant conformément à l'exigence de tests de sécurité)
   - Relevés de remédiation pour les résultats Critiques/Élevés (ou acceptation des risques pour les résultats non résolus)

**Processus de validation du transfert** : Les opérations DOIVENT confirmer la complétude du transfert via une liste de contrôle de transfert de sécurité signée (modèle dans ISMS-IMP-A.5.8) avant que le chef de projet demande l'autorisation de clôture. Une documentation de transfert incomplète bloque la clôture du projet jusqu'à ce que les lacunes soient résolues ou explicitement acceptées par le propriétaire opérationnel et le RSSI (pour les projets à Risque élevé).

**La documentation de transfert est archivée conformément aux exigences de gestion des documents A.5.33 et maintenue comme documentation de référence opérationnelle pour le cycle de vie du système.**

---

# Rôles et responsabilités

## Direction générale

**Responsabilité** : Sécurité organisationnelle globale, y compris l'intégration de la sécurité dans les projets.

**Responsabilités** :

- Approuver cette politique et assurer les ressources organisationnelles pour sa mise en œuvre
- Examiner le statut de sécurité des projets à risque élevé lors des revues de direction
- Accepter les risques résiduels pour les projets critiques

## Responsable de la sécurité des systèmes d'information (RSSI)

**Responsabilité** : Mise en œuvre du programme de sécurité de l'information, y compris la supervision de la sécurité des projets.

**Responsabilités** :

- Approuver et maintenir cette politique
- Approuver les classifications de projets à Risque élevé
- Accepter les risques de sécurité résiduels pour les projets à Risque élevé
- Fournir des ressources de sécurité pour le soutien aux projets
- Surveiller les métriques de sécurité des projets et en rendre compte à la direction générale
- Approuver les dérogations aux exigences de sécurité

**Autorité** : Interrompre ou retarder les projets présentant des risques de sécurité inacceptables ; imposer des contrôles de sécurité supplémentaires.

## Responsable/Équipe de sécurité de l'information

**Responsabilité** : Conseil opérationnel en matière de sécurité et soutien à l'évaluation des risques.

**Responsabilités** :

- Soutenir les équipes projet dans l'évaluation des risques de sécurité et l'identification des exigences
- Examiner et approuver les classifications de projets à Risque moyen
- Examiner les exigences de sécurité et fournir des orientations techniques
- Réaliser ou commander des tests de sécurité
- Maintenir les modèles et les listes de contrôle d'exigences de sécurité

**Autorité** : Escalader les préoccupations de sécurité au RSSI ; recommander des retards de projet pour les risques non atténués.

## Chef de projet

**Responsabilité** : Succès global du projet, y compris la mise en œuvre des exigences de sécurité.

**Responsabilités** :

- Classifier le niveau de risque de sécurité du projet (avec le soutien du responsable sécurité)
- S'assurer que les activités de sécurité sont planifiées et budgétées
- Exécuter les activités de sécurité à chaque phase du projet
- Maintenir le registre des risques de sécurité du projet
- Escalader les risques et problèmes de sécurité
- Documenter les aspects de sécurité lors de la clôture et du transfert du projet

**Autorité** : Allouer des ressources du projet aux activités de sécurité ; demander un soutien sécurité à l'équipe InfoSec.

## Propriétaire métier / Propriétaire produit

**Responsabilité** : Exigences métier, y compris les besoins de sécurité des livrables du projet.

**Responsabilités** :

- Définir les exigences de sécurité métier
- Participer à l'évaluation des risques de sécurité
- Approuver les exigences de sécurité dans le périmètre du projet
- Accepter les risques de sécurité résiduels pour les systèmes/services dont ils sont propriétaires

## Responsable technique / Architecte de solution

**Responsabilité** : Conception et mise en œuvre technique, y compris l'architecture de sécurité.

**Responsabilités** :

- Intégrer les contrôles de sécurité dans l'architecture de la solution
- Mettre en œuvre les exigences de sécurité conformément aux spécifications
- Soutenir la modélisation des menaces et les revues d'architecture de sécurité
- Traiter les résultats de sécurité issus des tests ou des revues

## Fournisseurs tiers / Prestataires

**Responsabilité** : Sécurité des composants et services livrés par les fournisseurs conformément au contrat.

**Responsabilités** :

- Respecter les exigences de sécurité de [Organisation] dans les contrats
- Participer aux évaluations de sécurité et fournir les éléments de preuve requis
- Signaler les incidents de sécurité ou les vulnérabilités à [Organisation]

## Matrice RACI pour les activités de sécurité des projets

| Activité | CP | InfoSec | RSSI | Propriétaire métier | Responsable tech. |
|----------|----|---------|------|---------------------|-------------------|
| Classification du projet | R | A | I | C | C |
| Identification des exigences de sécurité | R | A | I | C | C |
| Conception de l'architecture de sécurité | C | C | I | I | R/A |
| Exécution des tests de sécurité | R | C | I | I | R |
| Acceptation des risques résiduels | I | C | A (Élevé) | A (Moyen/Faible) | I |
| Revue du transfert de sécurité | R | A | I | C | C |

R = Responsable (fait le travail), A = Autorité (décision finale), C = Consulté (fournit des contributions), I = Informé (tenu au courant)

---

# Gouvernance et gestion des dérogations

## Autorité de revue de sécurité

| Classification du projet | Autorité de revue |
|--------------------------|-------------------|
| Risque faible | Auto-évaluation par le chef de projet |
| Risque moyen | Revue du responsable sécurité requise |
| Risque élevé | Approbation du RSSI requise |

## Escalade

Les préoccupations de sécurité DOIVENT être escaladées dans les délais suivants :

- 2 jours ouvrables pour les projets à Risque élevé
- 5 jours ouvrables pour les projets à Risque moyen

**Voie d'escalade** : Chef de projet → Responsable sécurité de l'information → RSSI → Direction générale

**Déclencheurs d'escalade** :

Les préoccupations de sécurité nécessitant une escalade incluent :

- **Escalade obligatoire** :
  - Résultats de sécurité critiques ne pouvant être remédiés avant la date limite de déploiement
  - Exigences de sécurité en conflit avec les objectifs métier (nécessitant une acceptation des risques)
  - Fournisseur tiers incapable de satisfaire aux exigences de sécurité
  - Violation de données ou incident de sécurité affectant les livrables du projet
  - Préoccupations de conformité réglementaire identifiées pendant l'exécution du projet

- **Escalade discrétionnaire** :
  - Décisions d'architecture de sécurité ayant des implications à long terme significatives
  - Contraintes budgétaires affectant la mise en œuvre des contrôles de sécurité
  - Pression sur les délais nécessitant des raccourcis dans les tests de sécurité

Les conseils de sécurité courants (interprétation des exigences, sélection des contrôles, procédures de test) DOIVENT être gérés via le soutien du responsable sécurité sans escalade, sauf si l'autorité de décision dépasse la portée de l'équipe projet.

## Gestion des dérogations

Les dérogations aux exigences de sécurité DOIVENT être :

- Documentées avec justification métier et contrôles compensatoires
- Approuvées par l'autorité compétente selon la classification du projet
- Limitées dans le temps et suivies dans le registre des dérogations de sécurité
- Revues trimestriellement par le RSSI

## Révision de la politique

Cette politique DOIT être révisée :

- Annuellement (au minimum) par le RSSI
- Après des défaillances majeures de projets ayant des causes profondes liées à la sécurité
- Lors de changements réglementaires affectant la sécurité des projets
- Lors de changements organisationnels significatifs

---

# Conformité et surveillance

## Exigences de conformité

| Exigence | Mesure de conformité |
|----------|---------------------|
| Classification du projet | Tous les projets classifiés dans les 5 jours ouvrables suivant l'initialisation |
| Exigences de sécurité | Documentées pour tous les projets Risque moyen/élevé avant l'exécution |
| Tests de sécurité | Complétés avant le déploiement pour tous les projets |
| Acceptation des risques résiduels | Formellement documentée avant la clôture du projet |
| Enseignements tirés | Documentés pour tous les projets Risque moyen/élevé |

## Surveillance et métriques

[Organisation] DOIT suivre les métriques de sécurité des projets incluant :

- Projets par classification de sécurité
- Projets avec évaluations de sécurité complètes
- Résultats de sécurité par gravité et statut de remédiation
- Dérogations de sécurité accordées

**Exigences de reporting des métriques** :

- **Rapport mensuel du RSSI** : Tableau de bord détaillé des métriques incluant :
  - Projets par classification et statut de sécurité (dans les délais / à risque / en retard)
  - Résultats de sécurité ouverts par gravité et ancienneté
  - Dérogations de sécurité accordées vs. remédiées
  - Taux de complétion des tests de sécurité
  - Action requise : Le RSSI examine les tendances nécessitant une intervention (p. ex. > 20 % des projets à Risque élevé avec évaluations de sécurité en retard)

- **Rapport trimestriel à la direction** : Résumé exécutif incluant :
  - Nombre total de projets et nombre de projets à risque élevé
  - Résultats de sécurité critiques et statut de remédiation
  - Dérogations de sécurité nécessitant une attention de la direction
  - Incidents de sécurité significatifs affectant les projets
  - Action requise : La direction générale accepte les risques résiduels pour les projets critiques

Les métriques sont maintenues dans la plateforme GRC / tableau de bord des projets et accessibles au personnel autorisé conformément au contrôle d'accès A.5.15-18.

## Non-conformité

La non-conformité avec cette politique peut entraîner :

- Des retards de projet jusqu'à ce que les exigences de sécurité soient satisfaites
- Une escalade à la direction générale
- Des mesures disciplinaires conformément aux politiques RH de [Organisation]

---

# Documents connexes

## Documents SMSI

| Identifiant | Titre du document |
|-------------|-------------------|
| ISMS-POL-00 | Cadre d'applicabilité réglementaire |
| ISMS-IMP-A.5.8-UG/TG | Guide de mise en œuvre — Sécurité de l'information dans la gestion de projet |
| ISMS-POL-A.5.15-18 | Gestion des identités et des accès |
| ISMS-POL-A.5.19-22 | Sécurité des relations avec les fournisseurs |
| ISMS-POL-A.8.24 | Utilisation de la cryptographie |
| ISMS-POL-A.8.25-28 | Cycle de vie du développement sécurisé |
| ISMS-POL-A.8.32 | Gestion des changements |

## Références externes

| Référence | Description |
|-----------|-------------|
| ISO/IEC 27001:2022 | Systèmes de management de la sécurité de l'information — Exigences |
| ISO/IEC 27002:2022 | Mesures de sécurité de l'information — Conseils |
| ISO 21500:2021 | Management de projet, programme et portefeuille |
| NIST SP 800-64 | Considérations de sécurité dans le cycle de vie de développement des systèmes |

---

# Éléments de preuve pour cette politique

**Éléments de preuve pour l'Étape 1 (revue documentaire) :**

Éléments de preuve requis pour démontrer que cette politique est adéquatement documentée et approuvée :

- ✅ Ce document de politique (ISMS-POL-A.5.8 v1.0)
- ✅ Signatures d'approbation du RSSI, du DSI et de la direction générale
- ✅ Cadre de classification des projets défini (Section 2.2)
- ✅ Exigences des portes de phase sécurité documentées (Section 2.3)
- ✅ Catégories d'exigences de sécurité précisées (Section 2.4)
- ✅ Exigences de tests de sécurité par classification (Section 2.5)
- ✅ Exigences de transfert de sécurité documentées (Section 2.6)
- ✅ Rôles et responsabilités attribués (Section 3)
- ✅ Procédures de gouvernance et de dérogations définies (Section 4)
- ✅ Intégration avec les contrôles connexes documentée (Section 6)

**Éléments de preuve pour l'Étape 2 (efficacité opérationnelle) :**

Éléments de preuve requis pour démontrer que cette politique est opérationnellement efficace :

- Approbations de classification de projets montrant les déterminations de classification (Élevé/Moyen/Faible)
- Registres d'exigences de sécurité pour les projets Risque moyen/élevé
- Relevés d'approbation des portes de phase avec vérification des critères de sécurité
- Rapports de tests de sécurité (tests de pénétration, analyses de vulnérabilités, revues de code) par classification de projet
- Suivi des résultats de sécurité et remédiation jusqu'à clôture
- Dossiers de documentation de transfert de sécurité
- Relevés d'acceptation des risques résiduels avec approbations appropriées
- Documentation des enseignements tirés pour les projets Risque moyen/élevé
- Registre des dérogations de sécurité avec approbations et limites temporelles
- Tableaux de bord des métriques de sécurité des projets montrant les tendances
- Relevés de formation des chefs de projet sur les exigences de sécurité
- Résultats du classeur d'évaluation de sécurité (issus de ISMS-IMP-A.5.8)

## Précision sur les éléments de preuve de conformité

Cette politique établit les exigences d'intégration de la sécurité de l'information pour la gouvernance de la gestion de projet. Elle n'établit PAS :

- **Les contrôles techniques de sécurité spécifiques** (traités dans les politiques de contrôles techniques A.8.x)
- **La méthodologie de gestion de projet** (choix organisationnel — Agile, Waterfall, hybride)
- **Les critères de sélection des fournisseurs** (traités dans A.5.19-22 Sécurité des relations avec les fournisseurs)
- **Les techniques de tests de sécurité des applications** (traitées dans A.8.25-28 Cycle de vie du développement sécurisé)

La délimitation est : POL-A.5.8 définit QUELLES activités de sécurité doivent avoir lieu à chaque phase du projet et QUI les approuve → ISMS-IMP-A.5.8 fournit COMMENT évaluer les exigences de sécurité et suivre la conformité → Les contrôles techniques (A.8.x) définissent les capacités de sécurité spécifiques requises.

---

# Enregistrement des approbations

| Rôle | Nom | Signature | Date |
|------|-----|-----------|------|
| **Responsable de la sécurité des systèmes d'information (RSSI)** | [Nom] | | [Date à définir] |
| **Directeur des systèmes d'information (DSI)** | [Nom] | | [Date à définir] |
| **Directeur des opérations (COO)** | [Nom] | | [Date à définir] |
| **Responsable juridique/conformité** | [Nom] | | [Date à définir] |
| **Direction générale** | [Nom] | | [Date à définir] |

---

**FIN DU DOCUMENT DE POLITIQUE**

---

*Cette politique établit les exigences pour l'intégration de la sécurité de l'information dans la gestion de projet. Les procédures de mise en œuvre, les modèles d'évaluation et les orientations détaillées sont documentés dans ISMS-IMP-A.5.8 (UG/TG).*

<!-- QA_VERIFIED: 2026-03-30 -->
