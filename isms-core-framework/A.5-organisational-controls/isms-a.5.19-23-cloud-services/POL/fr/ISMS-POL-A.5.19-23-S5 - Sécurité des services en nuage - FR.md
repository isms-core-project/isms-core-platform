<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.19-23-S5-FR:framework:POL:a.5.19-23-s5 -->
**ISMS-POL-A.5.19-23-S5 — Sécurité des services en nuage**
**Contrôle A.5.23 : Sécurité de l'information pour l'utilisation des services en nuage**

---

**Contrôle documentaire**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Sécurité des services en nuage |
| **Type de document** | Section de politique |
| **Identifiant du document** | ISMS-POL-A.5.19-23-S5 |
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
| 1.0 | [Date] | RSI | Section initiale pour le contrôle ISO 27001:2022 A.5.23 |

**Cycle de révision** : Annuel
**Prochaine révision** : [Date d'entrée en vigueur + 12 mois]

**Chaîne d'approbation** :

- Primaire : Responsable de la sécurité des systèmes d'information (RSSI)
- Secondaire : Responsable de la sécurité de l'information (RSI)
- Technique : Responsable de l'équipe architecture cloud
- Conformité : Responsable juridique/conformité
- Autorité finale : Direction générale

**Documents connexes** :

- ISMS-POL-00 (Cadre d'applicabilité réglementaire)
- ISMS-POL-A.5.19-23 (Politique parente — Sécurité des fournisseurs et des services en nuage)
- ISMS-IMP-A.5.19-23.S1-UG/TG (Inventaire et classification des services en nuage)
- ISMS-IMP-A.5.19-23.S2-UG/TG (Diligence raisonnable et contrats fournisseurs)
- ISMS-IMP-A.5.19-23.S3-UG/TG (Configuration et déploiement sécurisés)
- ISMS-IMP-A.5.19-23.S4-UG/TG (Gouvernance continue et gestion des risques)
- ISMS-IMP-A.5.19-23.S5-UG/TG (Tableau de bord de surveillance de la conformité)
- ISMS-REF-A.5.23 (Registre des fournisseurs de services en nuage)
- ISO/IEC 27001:2022 Contrôle A.5.23
- ISO/IEC 27017:2015 (Contrôles de sécurité pour les services en nuage)
- ISO/IEC 27018:2019 (Protection de la vie privée dans le nuage)

---

# Objet

La présente section définit les exigences relatives à l'acquisition sécurisée, à l'utilisation, à la gestion et à la sortie des services en nuage. Elle établit le cadre du cycle de vie des services en nuage et les contrôles de sécurité propres au nuage.

**Objectif de contrôle (ISO 27002:2022) :**
> « Des processus d'acquisition, d'utilisation, de gestion et de sortie des services en nuage doivent être établis conformément aux exigences de sécurité de l'information de l'organisation. »

**Principe fondamental — « Le nuage, c'est l'ordinateur de quelqu'un d'autre »** : Les services en nuage fonctionnent sur une infrastructure que vous ne contrôlez pas, dans des juridictions que vous ne régissez pas, avec un accès par du personnel que vous n'avez pas contrôlé. Le modèle de responsabilité partagée signifie que des défaillances de sécurité peuvent survenir dans le domaine de l'une ou l'autre partie — mais les conséquences en termes de conformité et de réputation incombent à l'[Organisation]. Cette politique exige une gestion systématique du cycle de vie du nuage, depuis la sélection jusqu'à la sortie, avec une vérification continue que les déclarations des prestataires en matière de sécurité correspondent à la réalité opérationnelle.

**Résumé des lignes directrices ISO/IEC 27002:2022** :

- L'acquisition de services en nuage doit suivre un processus de sélection fondé sur le risque avec une évaluation de sécurité complète
- Les accords sur les services en nuage doivent traiter des exigences de sécurité de l'information et définir clairement le modèle de responsabilité partagée
- Le modèle de responsabilité partagée doit être explicitement compris, documenté et géré (contrôles du prestataire versus contrôles du client)
- La configuration des services en nuage doit être sécurisée conformément aux référentiels de sécurité du fournisseur et aux exigences organisationnelles
- Les exigences de résidence et de souveraineté des données dans le nuage doivent être appliquées conformément aux obligations réglementaires (RGPD, nLPD)
- La surveillance et la journalisation des services en nuage doivent être mises en œuvre avec une conservation et une révision appropriées
- La stratégie de sortie des services en nuage doit être planifiée et testée, incluant l'exportation des données, la portabilité et les procédures de transition
- Les risques propres au nuage (multi-location, commingling des données, juridiction, accès du prestataire) doivent être évalués et atténués
- Les certifications et la conformité du prestataire cloud (SOC 2, ISO 27017, CSA STAR) doivent être vérifiées annuellement

---

# Périmètre d'application

## Modèles de services en nuage

| Modèle | Description | Responsabilité de l'[Organisation] |
|--------|-------------|-----------------------------------|
| **IaaS** | Infrastructure en tant que service | SE, middleware, applications, données |
| **PaaS** | Plateforme en tant que service | Applications, données |
| **SaaS** | Logiciel en tant que service | Données, configuration utilisateur |
| **XDR/SECaaS** | Sécurité en tant que service | Configuration, politique, réponse |
| **FaaS** | Fonction en tant que service | Code, données |
| **DaaS** | Poste de travail en tant que service | Données utilisateur, politique de point de terminaison |

## Modèles de déploiement en nuage

| Modèle | Description | Considération |
|--------|-------------|---------------|
| **Public** | Infrastructure mutualisée, multi-location | Isolation des données, conformité |
| **Privé** | Infrastructure dédiée | Coût, charge de gestion |
| **Hybride** | Combinaison de public et privé | Complexité d'intégration |
| **Multi-cloud** | Plusieurs prestataires cloud | Portabilité, cohérence |
| **Communautaire** | Mutualisé par une communauté spécifique | Gouvernance, risque partagé |

## Applicabilité

La présente section s'applique à tous les services en nuage qui :

- Traitent, stockent ou transmettent des données organisationnelles
- Fournissent une infrastructure pour les systèmes organisationnels
- Sont accessibles par les utilisateurs de l'organisation
- S'intègrent aux systèmes organisationnels

---

# Cycle de vie des services en nuage

## Vue d'ensemble du cycle de vie

```
┌───────────────────────────────────────────────────────────────────────┐
│                  CYCLE DE VIE DES SERVICES EN NUAGE                   │
├───────────────────────────────────────────────────────────────────────┤
│                                                                       │
│  ┌──────────────┐   ┌──────────────┐   ┌──────────────┐   ┌────────┐ │
│  │ SÉLECTION    │ → │  MISE EN     │ → │ EXPLOITATION │ → │ SORTIE │ │
│  │              │   │  ŒUVRE       │   │              │   │        │ │
│  └──────────────┘   └──────────────┘   └──────────────┘   └────────┘ │
│        │                  │                  │                 │      │
│        ▼                  ▼                  ▼                 ▼      │
│  • Exigences         • Configuration    • Surveillance   • Plan       │
│  • Évaluation        • Intégration      • Révision       • Exportation│
│  • Éval. risques     • Migration        • Correctifs     • Transition │
│  • Contrat           • Tests            • Incidents      • Résiliation│
│  • Approbation       • Mise en prod.    • Modifications  • Vérif.     │
│                                                            suppression│
│                                                                       │
└───────────────────────────────────────────────────────────────────────┘
```

## Résumé des exigences par phase

| Phase | Activités clés | Livrables |
|-------|----------------|-----------|
| **Sélection** | Exigences, évaluation, évaluation des risques | Service approuvé + contrat |
| **Mise en œuvre** | Configuration, intégration, migration | Service prêt pour la production |
| **Exploitation** | Surveillance, révision, réponse aux incidents | Conformité continue |
| **Sortie** | Planification, exportation des données, résiliation | Sortie propre + destruction des données |

---

# Sélection et évaluation

## Exigences préalables à la sélection

Avant d'évaluer les services en nuage :

| Exigence | Description |
|----------|-------------|
| Besoin métier | Justification métier documentée |
| Classification des données | Classification des données à traiter |
| Exigences de conformité | Obligations réglementaires et contractuelles |
| Exigences d'intégration | Systèmes et flux de données concernés |
| Exigences de sécurité | Contrôles de sécurité minimaux requis |

## Critères d'évaluation des services en nuage

| Catégorie | Domaines d'évaluation |
|-----------|----------------------|
| **Sécurité** | Certifications, contrôles, historique des incidents |
| **Conformité** | Alignement réglementaire, résidence des données, support d'audit |
| **Fiabilité** | SLA, historique de disponibilité, redondance |
| **Portabilité** | Exportation des données, standards d'API, risque de verrouillage |
| **Support** | Disponibilité, réactivité, expertise |
| **Viabilité** | Solidité financière, positionnement sur le marché, feuille de route |

## Liste de contrôle pour l'évaluation de la sécurité

| Exigence | Méthode de vérification |
|----------|------------------------|
| Certification ISO 27001 ou SOC 2 | Révision du certificat/rapport |
| Chiffrement au repos et en transit | Documentation technique |
| Authentification multifacteur | Capacité de configuration |
| Journalisation et surveillance des accès | Vérification des fonctionnalités |
| Options de résidence des données | Révision contractuelle et technique |
| Processus de notification des incidents | Contrat et documentation |
| Capacités de sauvegarde et de récupération | Documentation technique |
| Programme de tests d'intrusion | Disponibilité des rapports |
| Gestion des vulnérabilités | Documentation des processus |
| Transparence sur les sous-traitants | Révision de la liste des sous-traitants |

## Évaluation des risques

Avant approbation, réaliser une évaluation des risques couvrant :

| Domaine de risque | Focus de l'évaluation |
|-------------------|----------------------|
| Exposition des données | Quelles données, quelle classification, quels contrôles |
| Disponibilité | Impact métier d'une défaillance de service |
| Conformité | Implications réglementaires |
| Dépendance fournisseur | Coûts et faisabilité d'une migration |
| Concentration | Dépendance envers un seul prestataire |
| Juridiction | Cadre légal et réglementaire |

## Exigences d'approbation

| Classification des données | Approbation requise |
|---------------------------|---------------------|
| Restreint | RSSI + Propriétaire métier + Juridique |
| Confidentiel | RSI + Propriétaire métier |
| Interne | Propriétaire métier + revue de sécurité |
| Public | Propriétaire métier |

---

# Mise en œuvre et configuration

## Principes de configuration sécurisée

| Principe | Mise en œuvre |
|----------|--------------|
| **Moindre privilège** | Permissions minimales pour les utilisateurs et services |
| **Défense en profondeur** | Couches multiples de contrôles |
| **Sécurité par défaut** | Démarrer en mode sécurisé, toute déviation requiert approbation |
| **Séparation** | Isoler les environnements, les données, les accès |
| **Chiffrement** | Protéger les données au repos et en transit |
| **Journalisation** | Pistes d'audit complètes |

## Exigences de configuration

| Domaine de contrôle | Exigences |
|---------------------|----------|
| **Identité et accès** | Intégration SSO, AMF appliqué, RBAC mis en œuvre |
| **Protection des données** | Chiffrement activé, classification appliquée, DLP configuré |
| **Sécurité réseau** | Restrictions d'accès, connectivité sécurisée, segmentation |
| **Journalisation et surveillance** | Journaux d'audit activés, intégration SIEM, alertes configurées |
| **Sauvegarde et récupération** | Sauvegardes automatisées, récupération testée, conservation appropriée |
| **Intégration des terminaux** | Accès sécurisé depuis les équipements gérés |

## Liste de contrôle de mise en œuvre

| Phase | Activités |
|-------|----------|
| **Pré-déploiement** | Revue de la configuration de sécurité, tests d'intégration |
| **Déploiement** | Déploiement progressif, tests de validation |
| **Post-déploiement** | Vérification de la sécurité, confirmation de la surveillance |
| **Documentation** | Enregistrements de configuration, runbooks, inventaire des accès |

## Sécurité de la migration des données

| Exigence | Description |
|----------|-------------|
| Plan de migration | Approche documentée avec contrôles de sécurité |
| Inventaire des données | Quelles données, classification, volume |
| Transfert sécurisé | Transmission chiffrée |
| Validation | Vérification de l'intégrité des données |
| Nettoyage de la source | Suppression sécurisée depuis la source (le cas échéant) |

---

# Gestion opérationnelle

## Activités de sécurité continues

| Activité | Fréquence | Responsabilité |
|----------|-----------|----------------|
| Révision des accès | Trimestrielle | Propriétaire métier + IT |
| Révision de la configuration | Semestrielle | Sécurité + IT |
| Évaluation de la sécurité | Annuelle | Sécurité |
| Vérification de la conformité | Annuelle | Conformité |
| Test des sauvegardes | Semestriel | Opérations IT |
| Exercice de réponse aux incidents | Annuel | Sécurité |

## Gestion des modifications

Les modifications des services en nuage doivent suivre le processus de gestion des modifications de l'organisation :

| Type de modification | Processus |
|---------------------|-----------|
| Initiée par le prestataire | Réviser la notification, évaluer l'impact, approuver ou escalader |
| Initiée par l'organisation | Demande de modification, revue de sécurité, approbation, mise en œuvre |
| Urgence | Approbation accélérée, revue post-mise en œuvre |

## Gestion des incidents

| Exigence | Description |
|----------|-------------|
| Détection | Surveiller les événements de sécurité via journaux et alertes |
| Notification | Recevoir et traiter les notifications du prestataire |
| Réponse | Exécuter les procédures de réponse aux incidents |
| Coordination | Collaborer avec le prestataire sur l'investigation |
| Récupération | Restaurer les services et les données selon les besoins |
| Retours d'expérience | Mettre à jour les contrôles suite aux incidents |

## Préparation à l'investigation numérique

| Exigence | Description |
|----------|-------------|
| Conservation des journaux | Conservation suffisante pour les investigations |
| Accès aux journaux | Capacité à récupérer les journaux pour analyse |
| Préservation des preuves | Coopération du prestataire pour les conservations légales |
| Chaîne de custody | Documentation pour les procédures judiciaires |
| Support d'investigation | Assistance du prestataire pour la forensique |

---

# Modèle de responsabilité partagée

## Comprendre la responsabilité partagée

```
┌─────────────────────────────────────────────────────────────────────┐
│         RESPONSABILITÉ PARTAGÉE PAR MODÈLE DE SERVICE               │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│ Responsabilité       │   IaaS   │   PaaS   │   SaaS   │            │
│ ─────────────────────┼──────────┼──────────┼──────────┤            │
│ Données              │   VOUS   │   VOUS   │   VOUS   │            │
│ Applications         │   VOUS   │   VOUS   │ PRESTAT. │            │
│ Exécution            │   VOUS   │ PRESTAT. │ PRESTAT. │            │
│ Middleware           │   VOUS   │ PRESTAT. │ PRESTAT. │            │
│ Système d'exploitat. │   VOUS   │ PRESTAT. │ PRESTAT. │            │
│ Virtualisation       │ PRESTAT. │ PRESTAT. │ PRESTAT. │            │
│ Infrastructure       │ PRESTAT. │ PRESTAT. │ PRESTAT. │            │
│ Physique             │ PRESTAT. │ PRESTAT. │ PRESTAT. │            │
│                                                                     │
│ VOUS = Responsabilité de l'[Organisation]                           │
│ PRESTAT. = Responsabilité du prestataire de services en nuage       │
└─────────────────────────────────────────────────────────────────────┘
```

## Documentation des responsabilités

Pour chaque service en nuage, documenter :

| Élément | Documentation |
|---------|---------------|
| Responsabilités du prestataire | Ce à quoi le prestataire s'engage |
| Responsabilités de l'organisation | Ce que nous devons faire |
| Responsabilités partagées | Activités conjointes |
| Lacunes | Domaines non couverts par l'une ou l'autre partie |
| Mesures compensatoires | Comment les lacunes sont traitées |

---

# Stratégie de sortie

## Exigences de planification de la sortie

**Tous les services en nuage doivent disposer d'une stratégie de sortie documentée incluant :**

| Élément | Description |
|---------|-------------|
| Événements déclencheurs | Conditions qui initieraient une sortie |
| Exportation des données | Comment extraire les données dans un format utilisable |
| Services alternatifs | Alternatives identifiées ou options internes |
| Approche de migration | Plan de transition général |
| Estimation du délai | Durée prévue de la sortie |
| Ressources nécessaires | Compétences et effort requis |
| Estimation des coûts | Budget pour la transition |

## Options de stratégie de sortie

Les stratégies de sortie DOIVENT évaluer trois principales voies de transition en fonction de la criticité du service, du coût, du calendrier et des exigences réglementaires. L'[Organisation] doit documenter la stratégie de sortie appropriée pour chaque service en nuage lors de l'évaluation initiale des risques et la réviser annuellement.

**Principes de sélection de la stratégie de sortie :**

1. **Migration nuage-vers-nuage** — Stratégie de sortie par défaut pour la plupart des services (90 %+)
2. **Transition hybride** — Pour les contraintes réglementaires ou de coût nécessitant un rapatriement partiel (5-10 %)
3. **Rapatriement sur site** — Réservé aux obligations réglementaires ou circonstances exceptionnelles (< 5 %)

---

### Migration nuage-vers-nuage (Stratégie de sortie principale)

La migration vers un prestataire cloud alternatif est la **stratégie de sortie par défaut** pour la plupart des services en raison de ses dépenses en capital plus faibles, de délais plus courts, du maintien de l'élasticité et d'une charge opérationnelle réduite.

**Justification stratégique :**

| Avantage | Bénéfice |
|----------|---------|
| Pas d'achat d'infrastructure | Zéro CAPEX, modèle de dépenses opérationnelles préservé |
| Transition plus rapide | 1-6 mois typique contre 6-18 mois pour une solution sur site |
| Élasticité maintenue | Capacité de pointe, mise à l'échelle automatique, paiement à l'usage préservés |
| Capacités modernes | Accès aux services natifs du nuage (conteneurs, serverless, IA/ML) |
| Charge opérationnelle réduite | Infrastructure, correctifs et mises à jour gérés par le prestataire |
| Flexibilité géographique | Déploiement multi-région sans investissement immobilier |

**Exigences d'évaluation :**

| Critère | Méthode d'évaluation | Documentation |
|---------|---------------------|---------------|
| **Prestataires alternatifs** | Identifier 2+ alternatives viables (AWS, Azure, GCP, OVHcloud, Alibaba Cloud) | Matrice de comparaison des prestataires |
| **Parité de services** | Vérifier que l'alternative offre des fonctionnalités équivalentes (calcul, stockage, base de données, réseau) | Mapping des fonctionnalités |
| **Portabilité des données** | Confirmer la compatibilité du format d'exportation avec l'alternative (JSON, CSV, Parquet, dumps de base de données) | Résultats des tests d'exportation |
| **Compatibilité d'intégration** | Évaluer les exigences de réécriture API/intégration (API REST, SDK, authentification) | Analyse de l'impact sur les intégrations |
| **Comparaison des coûts** | TCO sur 3 ans de l'alternative vs. le prestataire actuel (calcul, stockage, réseau, licences) | Tableur TCO |
| **Alignement des certifications** | Vérifier que l'alternative satisfait aux exigences de conformité (ISO 27001, SOC 2, RGPD, sectorielles) | Matrice des certifications |
| **Calendrier de migration** | Estimer la durée de transition incluant tests et validation | Calendrier du projet (Gantt) |
| **Preuve de concept** | Tester la charge de travail critique chez le prestataire alternatif (exigence annuelle DORA article 28.6) | Rapport de PoC, captures d'écran |

**Phases de migration (nuage-vers-nuage) :**

| Phase | Durée | Activités | Livrables |
|-------|-------|-----------|-----------|
| **Évaluation** | 2-4 semaines | Évaluation du prestataire alternatif, analyse des coûts, évaluation des risques | Sélection du prestataire, plan de migration |
| **Préparation** | 4-8 semaines | Création du compte, connectivité réseau, configuration IAM, classification des données | Environnement cible configuré |
| **Migration** | 4-12 semaines | Migration des données, déploiement applicatif, tests d'intégration | Services migrés en production |
| **Validation** | 2-4 semaines | Tests de performance, validation de sécurité, recette utilisateur | Validation et mise hors service de la source |
| **Nettoyage** | 1-2 semaines | Décommissionnement de l'environnement source, vérification de la suppression des données | Certificats de suppression |

**Durée totale : 3-6 mois typiquement pour les services de complexité moyenne**

**Considérations de coûts (nuage-vers-nuage) :**

| Catégorie de coût | Fourchette estimative | Notes |
|------------------|----------------------|-------|
| **Services professionnels** | CHF 20K-100K | Conseil, support à la migration (si nécessaire) |
| **Frais de sortie des données** | CHF 5K-50K | Transfert de données sortantes depuis le prestataire source |
| **Fonctionnement en parallèle** | 1-3 mois de coûts cloud | Exécution des deux environnements pendant la migration |
| **Tests et validation** | CHF 10K-30K | Tests de charge, évaluation de sécurité |
| **Formation** | CHF 5K-20K | Formation du personnel sur la plateforme du nouveau prestataire |
| **TOTAL (ponctuel)** | **CHF 40K-200K** | Variable selon la complexité du service et le volume de données |

**Quand la migration nuage-vers-nuage est optimale :**

✅ **Le service est natif du nuage** (conteneurs, microservices, serverless, bases de données managées)
✅ **La charge de travail a une demande variable** (pics de trafic, schémas saisonniers, croissance imprévisible)
✅ **L'organisation manque de capacité sur site** (pas de centre de données, personnel d'infrastructure limité)
✅ **Aucune obligation réglementaire** d'hébergement physique sur site
✅ **Le TCO cloud reste favorable** par rapport au sur site sur un horizon de 3-5 ans
✅ **Distribution géographique requise** (multi-région, accès mondial à faible latence)
✅ **Services cloud modernes utilisés** (IA/ML, IoT, analytique, CDN)

**Exemple de scénario :**

> **Plateforme de collaboration SaaS (Microsoft 365 → Google Workspace)**
> - **Service** : Messagerie, calendrier, stockage de fichiers, visioconférence
> - **Utilisateurs** : 300 collaborateurs
> - **Calendrier de migration** : 3 mois (planification 4 semaines, migration 8 semaines, validation 2 semaines)
> - **Coût de migration** : CHF 45K (conseil CHF 30K, formation CHF 10K, licences parallèles CHF 5K)
> - **Résultat** : Zéro CAPEX, élasticité cloud maintenue, fonctionnalités de collaboration améliorées

---

### Transition hybride (Rapatriement partiel)

L'approche hybride maintient certaines charges de travail dans le nuage tout en rapatriant des composants sélectionnés vers une infrastructure sur site. Cette stratégie équilibre les avantages du nuage avec des exigences spécifiques de contrôle sur site.

**Scénarios hybrides typiques :**

| Scénario | Composant cloud | Composant sur site | Justification |
|----------|----------------|-------------------|---------------|
| **Souveraineté des données** | Couche applicative, calcul, dev/test | Base de données avec données sensibles/réglementées | Exigences de résidence des données réglementaires (nLPD, lois sectorielles) |
| **Optimisation des coûts** | Capacité de pointe, hors-production | Production de base prévisible | Baseline prévisible sur site, dépassement élastique dans le nuage |
| **Sensible à la latence** | Sauvegarde/PRA, analytique, reporting | Traitement transactionnel en temps réel | Réduire la latence réseau pour les charges de travail interactives critiques |
| **Migration progressive** | Nouveaux services natifs nuage | Systèmes legacy en cours de refactorisation | Transition graduelle sur 12-24 mois, migration sans risque |
| **Hybride réglementaire** | Traitement de données non critiques | Données confidentielles/restreintes | Limitations de transfert RGPD art. 44-50, piloté par la classification des données |

**Exigences d'évaluation :**

| Critère | Méthode d'évaluation | Documentation |
|---------|---------------------|---------------|
| **Segmentation des charges** | Identifier les composants restant cloud vs. sur site (par classification des données, latence, conformité) | Matrice de placement des charges de travail |
| **Synchronisation des données** | Évaluer les exigences de réplication (tolérance à la latence, modèle de cohérence, volume) | Diagramme des flux de données, SLA de synchronisation |
| **Connectivité réseau** | Évaluer les options de connectivité hybride (VPN, AWS Direct Connect, Azure ExpressRoute, GCP Interconnect) | Diagramme d'architecture réseau |
| **Complexité de gestion** | Documenter la surcharge opérationnelle supplémentaire (multiples plateformes, outils, compétences) | Runbook opérationnel |
| **Exigences en compétences** | Évaluer le besoin d'expertise cloud hybride (infrastructure cloud et sur site) | Plan de formation, besoins en recrutement |
| **Modèle de coût** | TCO hybride vs. tout-cloud vs. tout sur site sur 3-5 ans | Tableau comparatif TCO |
| **Périmètres de sécurité** | Définir les zones de confiance, exigences de chiffrement, contrôles d'accès entre environnements | Document d'architecture de sécurité |
| **Impact sur la conformité** | Vérifier que le modèle hybride satisfait aux exigences réglementaires (résidence des données, audit, contrôles d'accès) | Évaluation de la conformité |

**Architectures hybrides types :**

| Architecture | Description | Cas d'usage |
|-------------|-------------|------------|
| **Cloud-Bursting** | Baseline sur site + dépassement dans le nuage | Charge prévisible avec pics occasionnels (e-commerce, période fiscale) |
| **Séparation de résidence des données** | Données sensibles sur site, traitement dans le nuage | Résidence stricte nLPD/RGPD, mais besoin de calcul cloud |
| **Actif-Actif** | Charges réparties entre nuage et sur site | Haute disponibilité, reprise après sinistre, distribution géographique |
| **Actif-Passif** | On-site principal, nuage PRA/sauvegarde | Continuité d'activité avec nuage en veille |
| **Edge-Core** | Traitement edge sur site, agrégation dans le nuage | IoT, points de vente, informatique de pointe sensible à la latence |

**Dépenses en capital et d'exploitation (Transition hybride) :**

| Composant | CAPEX (Année 0) | OPEX (Annuel) | Notes |
|-----------|----------------|---------------|-------|
| **Infrastructure sur site** | CHF 50K-500K | CHF 30K-100K | Infrastructure partielle (calcul, stockage, réseau) |
| **Connectivité réseau** | CHF 10K-30K | CHF 5K-50K/an | VPN ou circuits dédiés (1-10 Gbps) |
| **Outils de gestion hybride** | CHF 0-20K | CHF 10K-50K/an | Orchestration (Terraform, Ansible), supervision (Datadog, Prometheus) |
| **Compétences/formation** | CHF 0-30K | CHF 20K-50K | Formation du personnel sur les architectures hybrides, conseil |
| **Synchronisation des données** | CHF 5K-20K | CHF 5K-20K | Outils de réplication, coûts de bande passante |
| **Services professionnels** | CHF 30K-100K | CHF 10K-30K | Conception d'architecture, support à la mise en œuvre |
| **TOTAL** | **CHF 95K-700K** | **CHF 80K-300K/an** | **TCO sur 3 ans : CHF 335K-1,6M** |

**Calendrier de migration (Transition hybride) :**

| Phase | Durée | Activités |
|-------|-------|----------|
| **Conception de l'architecture** | 4-8 semaines | Placement des charges, conception réseau, cartographie des flux de données |
| **Approvisionnement en infrastructure** | 8-12 semaines | Achat matériel, préparation des locaux, circuits réseau |
| **Mise en place de la connectivité hybride** | 4-6 semaines | Configuration VPN/Direct Connect, tests |
| **Migration des charges de travail** | 8-16 semaines | Migration progressive des charges sélectionnées vers le sur-site |
| **Intégration et tests** | 4-8 semaines | Synchronisation des données, tests de basculement, validation des performances |
| **Optimisation** | 4-8 semaines | Optimisation des coûts, réglage des performances, transfert opérationnel |

**Durée totale : 6-12 mois typiquement**

**Quand la transition hybride est optimale :**

✅ **Les exigences réglementaires** imposent un stockage sur site pour certaines données (nLPD art. 16, spécifiques au secteur)
✅ **Des charges de travail spécifiques** ont une extrême sensibilité à la latence (exigences < 10 ms)
✅ **L'organisation dispose d'une capacité sur site existante** avec une marge disponible
✅ **Les caractéristiques de la charge de travail permettent la segmentation** (couche applicative sans état vs. base de données avec état)
✅ **Stratégie de transition graduelle** préférée (répartir le coût/risque sur 12-24 mois)
✅ **Profil de coût mixte** (certaines charges moins chères sur site, d'autres dans le nuage)
✅ **Les systèmes legacy** nécessitent une refactorisation avant la migration cloud (état hybride intermédiaire)

**Exemple de scénario :**

> **Système de dossiers patients en santé (Hybride)**
> - **Nuage** : Front-end applicatif (Azure), analytique/reporting (Power BI), sauvegarde (Azure Backup)
> - **Sur site** : Base de données patients avec dossiers médicaux sensibles (conformité HIPAA/nLPD)
> - **Réseau** : Azure ExpressRoute 1 Gbps
> - **Calendrier de migration** : 8 mois (conception 2 mois, infrastructure 3 mois, migration 3 mois)
> - **Coût de migration** : CHF 250K CAPEX + CHF 80K/an OPEX
> - **Résultat** : Conformité réglementaire maintenue, bénéfices du nuage pour les charges non sensibles

---

### Rapatriement sur site (Reconstruction complète)

Migration complète depuis le nuage vers une infrastructure appartenant à l'[Organisation]. Il s'agit de la **stratégie de sortie la plus risquée et la plus coûteuse**, à envisager uniquement lorsque des mandats réglementaires ou des circonstances exceptionnelles le justifient.

**⚠️ CRITIQUE : Le rapatriement sur site est économiquement justifié dans moins de 5 % des scénarios de sortie du nuage.**

**Scénarios réalistes de rapatriement complet :**

| Scénario | Justification | Probabilité | Exemple |
|----------|---------------|-------------|---------|
| **Mandat réglementaire** | Obligation légale d'infrastructure sur site physiquement contrôlée, isolée | Faible-Moyen | Systèmes gouvernementaux classifiés, certains systèmes bancaires core |
| **Inversion des coûts** | Les coûts cloud dépassent le TCO sur site sur 3-5 ans pour des charges stables à haut volume | Faible | Traitement batch massif (>1 Po de données, charge prévisible) |
| **Indépendance stratégique** | Éliminer toutes les dépendances externes pour l'infrastructure critique | Très faible | Systèmes de défense, infrastructures critiques (énergie, eau) |
| **Défaillance du prestataire** | Faillite, violation irréparable, perte d'accès géopolitique | Très faible | Scénario d'urgence PCA/PRA (cf. ISMS-POL-A.5.30-8.13-14) |
| **Risque de concentration** | Diversification DORA art. 28.9 depuis un prestataire critique unique | Faible | Établissements financiers réduisant leur dépendance envers un hyperscaler |

**Exigences d'évaluation :**

| Critère | Méthode d'évaluation | Documentation |
|---------|---------------------|---------------|
| **Exigences d'infrastructure** | Dimensionner calcul, stockage, réseau, installations, alimentation/refroidissement | Plan de capacité d'infrastructure |
| **Dépenses en capital** | Investissement initial pour matériel, logiciels, installations | Budget CAPEX (CHF 200K-2M+) |
| **Dépenses d'exploitation** | Personnel, maintenance, services, licences logicielles | Budget OPEX (annuel) |
| **Coût total de possession** | TCO amorti sur 3-5 ans vs. coûts cloud actuels | Modèle de comparaison TCO |
| **Calendrier** | Construction réaliste incluant approvisionnement, déploiement, tests | Calendrier du projet (6-18 mois) |
| **Compétences/personnel** | Recrutement, formation, rétention pour les opérations d'infrastructure | Plan de dotation (3-10 ETP) |
| **Installations** | Espace centre de données, capacité d'alimentation/refroidissement, sécurité physique | Évaluation des installations |
| **Conformité** | Exigences d'audit de l'infrastructure sur site (ISO 27001, sectorielles) | Analyse des écarts de conformité |
| **Renouvellement technologique** | Cycles de renouvellement du matériel (3-5 ans), risque de dette technologique | Feuille de route technologique |
| **Perte d'élasticité** | Impact de la perte de la capacité de pointe cloud sur l'activité | Analyse d'impact métier |

**Estimations de coûts (Organisation de taille moyenne, ~300 collaborateurs) :**

**CAPEX (Année 0) — Construction de l'infrastructure :**

| Composant | Spécification | Fourchette de coût (CHF) | Cycle de vie |
|-----------|--------------|--------------------------|-------------|
| **Calcul** | 50 VM @ 4-8 vCPU, 16-32 Go RAM | 150K-300K | 3-5 ans |
| **Stockage** | 100 To utilisables (SAN/NAS, RAID 6, multiniveaux) | 50K-150K | 5 ans |
| **Réseau** | Commutateurs cœur (10/25 GbE), pare-feux, répartiteurs de charge | 40K-80K | 5 ans |
| **Sauvegarde** | Appliances de sauvegarde, déduplication, bibliothèque de bandes (optionnel) | 30K-60K | 5 ans |
| **Installations** | Espace rack, distribution d'alimentation, refroidissement (si colocation) | 0-100K | S.O. (ou contrat colo) |
| **Licences logicielles** | Virtualisation (VMware, Hyper-V), sauvegarde (Veeam, Commvault) | 20K-50K | 1-3 ans |
| **Services professionnels** | Conseil en migration, support à la mise en œuvre | 50K-100K | Ponctuel |
| **Provision pour imprévus** | Tampon de 15-20 % pour les coûts inattendus | 50K-150K | Ponctuel |
| **TOTAL CAPEX** | | **CHF 390K-990K** | |

**OPEX (Annuel) — Opérations continues :**

| Composant | Spécification | Fourchette de coût (CHF) | Notes |
|-----------|--------------|--------------------------|-------|
| **Personnel** | 3-5 ETP (sysadmin, réseau, sécurité) @ CHF 100K-120K chargé | 300K-600K | Salaires, avantages sociaux, formation |
| **Maintenance** | Contrats de support matériel (15-20 % du CAPEX annuellement) | 30K-80K | Critique pour la disponibilité |
| **Licences logicielles** | Virtualisation, sauvegarde, supervision, outils de sécurité | 30K-100K | Renouvellements annuels, support |
| **Installations** | Loyer colo, alimentation, refroidissement (si pas de DC propre) | 30K-100K | Ou CAPEX si installation en propre |
| **Réseau** | WAN, FAI, bande passante | 10K-30K | Multi-hébergé pour la redondance |
| **Conseil** | Architecture, sécurité, optimisation des performances en cours | 20K-50K | Support intermittent |
| **Provision de renouvellement technologique** | Mise de côté pour le remplacement matériel à 3-5 ans | 50K-150K | CAPEX amorti |
| **TOTAL OPEX** | | **CHF 470K-1,11M/an** | |

**Coût total de possession sur 5 ans :**

| Poste | Coût (CHF) |
|-------|-----------|
| **CAPEX (Année 0)** | 390K-990K |
| **OPEX (Années 1-5)** | 2,35M-5,55M |
| **Renouvellement technologique (Années 3-4)** | 200K-500K |
| **TOTAL TCO SUR 5 ANS** | **CHF 2,94M-7,04M** |

**Comparaison avec le nuage (exemple) :**

| Scénario | Coût cloud annuel | Coût cloud sur 5 ans | TCO sur site | Verdict |
|----------|------------------|---------------------|-------------|---------|
| **Petite charge** | CHF 200K | CHF 1M | CHF 2,94M-7,04M | ❌ Nuage moins cher |
| **Charge moyenne** | CHF 500K | CHF 2,5M | CHF 2,94M-7,04M | 🟡 Seuil de rentabilité |
| **Grande charge stable** | CHF 1M+ | CHF 5M+ | CHF 2,94M-7,04M | ✅ Sur site potentiellement moins cher |

**Cadre de décision : Quand le rapatriement sur site est justifié**

Le rapatriement complet sur site est économiquement justifié **UNIQUEMENT** lorsqu'un ou plusieurs des critères suivants s'appliquent :

**1. Mandat réglementaire (piloté par la conformité) :**

- Obligation légale d'infrastructure sur site physiquement contrôlée, isolée (air gap)
- Les services en nuage ne peuvent pas satisfaire aux exigences de souveraineté des données même avec des déploiements en pays
- Des réglementations sectorielles prohibent le nuage public (gouvernement classifié, certains domaines de défense)
- **Exemple** : Systèmes Bundesverwaltung suisses nécessitant une infrastructure isolée, certains systèmes cantonaux de santé

**2. Inversion des coûts (piloté par l'économie) :**

- Coûts cloud annuels > CHF 500K **ET** caractéristiques de la charge :
  - Baseline stable et prévisible (pas d'exigences de pointe)
  - Traitement de données à haut volume (> 500 To, faibles besoins en sortie)
  - Charges de traitement batch intensives en CPU (utilisation élevée en continu)
- TCO sur site sur 3-5 ans < 70 % des coûts cloud équivalents
- **Exemple** : Recherche en génomique (données à l'échelle du pétaoctet, calcul continu), traitement batch à grande échelle

**3. Indépendance stratégique (piloté par le risque) :**

- Infrastructure critique nécessitant zéro dépendance externe
- Secteurs de la sécurité nationale, de la défense ou des infrastructures essentielles
- Atténuation du risque géopolitique (conflits de juridiction du prestataire)
- **Exemple** : Systèmes de commandement militaires, SCADA d'infrastructures critiques, systèmes core des banques centrales

**4. Élimination du risque de concentration (piloté par DORA) :**

- DORA art. 28.9 : Risque de concentration chez un prestataire tiers ICT critique
- Établissements financiers diversifiant depuis un hyperscaler unique
- Pas un rapatriement complet, mais hybride avec une composante sur site substantielle
- **Exemple** : Banque de premier rang déplaçant 40 % des charges sur site pour réduire la dépendance AWS

**Pour tous les autres scénarios, les modèles nuage-vers-nuage ou hybride sont préférés pour :**

- TCO inférieur pour la plupart des charges (70-80 % des cas)
- Mise en œuvre plus rapide (1/3 du délai)
- Élasticité et accès à l'innovation maintenus
- Charge opérationnelle réduite (pas de gestion du cycle de vie matériel)

**Calendrier de migration (Rapatriement sur site) :**

| Phase | Durée | Activités | Éléments du chemin critique |
|-------|-------|-----------|---------------------------|
| **Analyse de cas** | 4-6 semaines | Analyse TCO, justification réglementaire, approbation de la direction | Approbation du conseil, allocation budgétaire |
| **Conception** | 6-8 semaines | Architecture, dimensionnement, évaluation des installations | Sélection du centre de données (si nécessaire) |
| **Approvisionnement** | 8-16 semaines | Appel d'offres, sélection des fournisseurs, bons de commande | Délais de livraison (réseau 12+ semaines) |
| **Préparation des installations** | 4-8 semaines | Installation des baies, alimentation/refroidissement, sécurité physique (si nouveau DC) | Inspection de l'état de préparation des installations |
| **Déploiement de l'infrastructure** | 6-10 semaines | Installation matériel, configuration réseau, mise en place de la virtualisation | Connectivité réseau établie |
| **Migration et tests** | 8-16 semaines | Migration progressive des charges, tests d'intégration, validation des performances | Fenêtres de bascule, plans de retour arrière |
| **Optimisation** | 4-8 semaines | Optimisation des performances, réduction des coûts, transfert opérationnel | Acceptation opérationnelle |

**Durée totale : 9-18 mois typiquement (médiane : 12 mois)**

**Exigences en personnel (Opérations sur site) :**

| Rôle | ETP | Responsabilités | Fourchette salariale (CHF) |
|------|-----|-----------------|--------------------------|
| **Responsable infrastructure** | 1,0 | Architecture, gestion des fournisseurs, planification des capacités | 120K-150K |
| **Administrateurs systèmes** | 2-4 | Gestion des serveurs, correctifs, sauvegarde, supervision | 90K-120K chacun |
| **Ingénieur réseau** | 1,0 | Conception réseau, pare-feu, routage, connectivité | 100K-130K |
| **Ingénieur sécurité** | 0,5-1,0 | Durcissement, gestion des vulnérabilités, réponse aux incidents | 110K-140K |
| **Support d'astreinte** | Rotation | Réponse aux incidents 24/7 (si services critiques) | +20 % prime d'astreinte |
| **TOTAL** | **4,5-7,0 ETP** | | **CHF 450K-790K/an** |

**Considérations de risques (Rapatriement sur site) :**

| Risque | Impact | Atténuation |
|--------|--------|-------------|
| **Dette technologique** | Le matériel devient obsolète, renouvellement nécessaire tous les 3-5 ans | Prévoir les cycles de renouvellement, planification du cycle de vie |
| **Planification des capacités** | Sur-approvisionnement (coût gaspillé) ou sous-approvisionnement (problèmes de performance) | Démarrer avec 30 % de marge, surveiller l'utilisation |
| **Perte d'élasticité** | Incapacité à gérer des pics de trafic ou une croissance imprévue | Architecture hybride avec capacité de pointe cloud |
| **Rétention des compétences** | Rotation du personnel d'infrastructure, perte de connaissances | Documentation, formation croisée, rémunération compétitive |
| **Points de défaillance unique** | L'infrastructure sur site présente des domaines de défaillance | Redondance (N+1), PCA/PRA vers nuage ou colocation |
| **Charge de conformité** | Les audits sur site sont plus intensifs (sécurité physique, environnement) | Tests d'intrusion annuels, automatisation de la conformité |
| **Coût de sortie** | Investissement déjà réalisé sur site, difficile de retourner au nuage | Éviter le verrouillage propriétaire (VMware NSX, etc.), utiliser des formats portables |

**Quand le rapatriement sur site n'est PAS justifié :**

❌ **Les coûts cloud sont élevés mais la charge est élastique** → Rester dans le nuage, optimiser les coûts (instances réservées, mise à l'échelle automatique)
❌ **Perception managériale « nous voulons le contrôle »** → Un hybride avec une gouvernance appropriée atteint le contrôle sans rapatriement complet
❌ **Augmentation à court terme des tarifs cloud** → Négocier un accord d'entreprise, envisager un prestataire cloud alternatif
❌ **Préoccupations de sécurité** → Les prestataires cloud ont une meilleure sécurité que la plupart des solutions sur site (bénéficier de leurs économies d'échelle)
❌ **« Nous avons toujours été sur site »** → Raisonnement par tradition, pas une justification métier valide

**Exemple de scénario :**

> **Système de traitement batch à grande échelle (Rapatriement sur site justifié)**
> - **Charge** : ETL nocturnelle, entrepôt de données de 800 To, utilisation CPU prévisible à 90 %
> - **Coût cloud actuel** : CHF 1,2M/an (EC2, S3, RDS)
> - **TCO sur site** : CHF 600K CAPEX + CHF 400K/an OPEX = CHF 2,6M sur 5 ans
> - **Nuage sur 5 ans** : CHF 6M
> - **Économies** : CHF 3,4M sur 5 ans (réduction de 57 %)
> - **Justification** : Charge stable et prévisible sans exigences de pointe
> - **Calendrier de migration** : 10 mois
> - **Résultat** : Rapatriement justifié par les coûts pour une charge à haut volume et faible variabilité

---

### Matrice de décision

**Cadre de décision quantitatif :**

Utiliser cet arbre de décision pour la sélection de la stratégie de sortie :
```
                    DÉBUT : Sortie du service en nuage requise
                                       │
                                       ▼
                    ┌──────────────────────────────────────┐
                    │ Existe-t-il un MANDAT RÉGLEMENTAIRE  │
                    │ pour le sur site ?                   │
                    │ (souveraineté des données, air gap)  │
                    └──────┬────────────────────┬──────────┘
                           │                    │
                      OUI  │                    │  NON
                           ▼                    ▼
                    ┌─────────┐   ┌──────────────────────────────┐
                    │ Sur site│   │ Coût cloud annuel > CHF 500K │
                    │    ou   │   │ ET charge stable (pas de     │
                    │ Hybride │   │ pointe) ?                    │
                    └─────────┘   └──────┬───────────────┬───────┘
                                         │               │
                                    OUI  │               │  NON
                                         ▼               ▼
                                  ┌──────────┐  ┌──────────────────┐
                                  │ Réaliser │  │ Nuage-vers-nuage │
                                  │ analyse  │  │    (Défaut)      │
                                  │   TCO    │  └──────────────────┘
                                  └────┬─────┘
                                       │
                            TCO sur site < 70 %
                            du nuage sur 5 ans ?
                                       │
                                  OUI  │  NON
                                       ▼  ▼
                              ┌──────────────────────┐
                              │ Sur site   │ Nuage-  │
                              │    ou      │ vers-   │
                              │  Hybride   │ nuage   │
                              └──────────────────────┘
```

**Matrice de comparaison :**

| Facteur | Nuage-vers-nuage | Hybride | Sur site |
|---------|----------------|---------|---------|
| **CAPEX** | ✅ Aucun (zéro infrastructure) | 🟡 CHF 95K-700K | ❌ CHF 390K-990K |
| **OPEX (Annuel)** | 🟡 CHF 50K-500K+ (frais cloud) | 🟡 CHF 80K-300K (réparti) | ❌ CHF 470K-1,11M |
| **TCO sur 5 ans** | 🟡 CHF 250K-2,5M+ | 🟡 CHF 335K-1,6M | ❌ CHF 2,94M-7,04M |
| **Délai** | ✅ 3-6 mois | 🟡 6-12 mois | ❌ 9-18 mois |
| **Risque** | ✅ Faible (schéma éprouvé) | 🟡 Moyen (complexité) | ❌ Élevé (dette technologique) |
| **Élasticité** | ✅ Maintenue | 🟡 Partielle | ❌ Perdue (capacité fixe) |
| **Compétences requises** | ✅ Compétences cloud existantes | 🟡 Cloud + sur site | ❌ Expertise sur site approfondie |
| **Complexité opérationnelle** | ✅ Faible (plateforme unique) | 🟡 Moyen (multi-plateforme) | ❌ Élevé (cycle de vie complet) |
| **Flexibilité réglementaire** | 🟡 Dépendant du prestataire | ✅ Élevé (placement flexible) | ✅ Contrôle total |
| **Renouvellement technologique** | ✅ Géré par le prestataire | 🟡 Responsabilité partielle | ❌ Responsabilité totale |
| **Continuité d'activité** | ✅ SLA prestataire + géo-redondance | 🟡 Complexe (multi-site) | ❌ À la charge de l'organisation |
| **Accès à l'innovation** | ✅ Derniers services cloud (IA/ML, IoT) | 🟡 Services cloud uniquement | ❌ Limité (cycles fournisseurs) |

**Priorité de recommandation (Règle 90-5-5) :**

| Stratégie de sortie | Usage attendu | Principaux facteurs |
|--------------------|---------------|---------------------|
| **Nuage-vers-nuage** | 90 %+ des services | Coût, rapidité, élasticité, innovation |
| **Hybride** | 5-10 % des services | Conformité réglementaire, latence, optimisation des coûts |
| **Sur site** | < 5 % des services | Mandat réglementaire, inversion extrême des coûts, indépendance stratégique |

---

### Renvoi croisé : Continuité d'activité et reprise après sinistre

Les stratégies de sortie traitent des **transitions planifiées et volontaires** depuis les services en nuage. Pour les **scénarios d'urgence** impliquant une défaillance du prestataire cloud, se référer à la planification de la Continuité d'activité et de la Reprise après sinistre (ISMS-POL-A.5.30-8.13-14).

**Distinction :**

| Type de scénario | Cadre de planification | Délai | Exemple |
|-----------------|----------------------|-------|---------|
| **Sortie planifiée** | Cette politique (A.5.23) | 3-18 mois | Échec de négociation contractuelle, optimisation des coûts, changement stratégique |
| **Basculement d'urgence** | PCA/PRA (A.5.30-8.13-14) | Heures-Jours | Panne du prestataire, violation de sécurité, perte d'accès géopolitique |

**Scénarios d'urgence nécessitant le PCA/PRA :**

| Scénario | Probabilité | Réponse | Point de récupération |
|----------|-------------|---------|----------------------|
| **Panne régionale du prestataire** | Moyen | Basculement vers une région alternative | Heures (RTO 4-8h) |
| **Violation de sécurité du prestataire** | Faible | Évaluation des risques, envisager une sortie immédiate | Jours (RTO 24-72h) |
| **Faillite du prestataire** | Très faible | Exécuter immédiatement le plan de sortie | Semaines (RTO 2-4 sem.) |
| **Perte d'accès géopolitique** | Très faible | Basculement d'urgence sur site ou vers un prestataire alternatif | Jours-Semaines (RTO 3-14 j.) |
| **Résiliation pour motif valable** | Faible | Sortie planifiée avec calendrier accéléré | Mois (RTO 1-3 mois) |

**Exigence DORA article 28.6 :**

> « Les arrangements contractuels sur l'utilisation de services TIC soutenant des fonctions critiques ou importantes doivent inclure [...] des stratégies de sortie, notamment pour les fonctions critiques ou importantes [...] ainsi qu'une obligation pour le prestataire tiers de services TIC de coopérer avec l'entité financière et les autorités compétentes pendant les processus de sortie. »

L'[Organisation] doit documenter **les deux** :
1. **Stratégies de sortie planifiées** (cette section) pour les transitions volontaires
2. **Procédures de sortie d'urgence** (politique PCA/PRA) pour les scénarios de défaillance du prestataire

**Points d'intégration :**

- **Stratégie de sauvegarde des données** : L'emplacement de sauvegarde PCA/PRA sert de source de données pour la sortie (ex. appliance de sauvegarde sur site ou nuage alternatif)
- **Prestataire alternatif en veille** : Pour les services critiques, maintenir une veille chaude/tiède chez un prestataire cloud alternatif (PCA/PRA + stratégie de sortie)
- **Tests de basculement annuels** : Les tests PCA/PRA valident la portabilité des données de sortie et la disponibilité du prestataire alternatif
- **Consolidation de la documentation** : Les plans de sortie dans le cahier ISMS-IMP-A.5.19-23.4 font référence croisée aux runbooks PCA/PRA

---

### Révision et tests annuels

La viabilité de la stratégie de sortie DOIT être révisée et testée annuellement pour s'assurer que les hypothèses restent valables et que les plans de sortie sont exécutables.

**Exigences de révision annuelle :**

| Domaine de révision | Activités | Documentation |
|--------------------|-----------|---------------|
| **Mise à jour des coûts** | Recalculer le TCO nuage vs. alternative aux prix actuels | Tableur TCO actualisé |
| **Évaluation des prestataires alternatifs** | Vérifier que les alternatives répondent toujours aux exigences | Matrice de comparaison des prestataires |
| **Évolutions réglementaires** | Évaluer l'impact des nouvelles réglementations sur la stratégie de sortie | Évaluation de l'impact réglementaire |
| **Évolutions technologiques** | Évaluer les nouvelles technologies facilitant la sortie (outils de portabilité, plateformes multi-cloud) | Évaluation technologique |
| **Conditions contractuelles** | Réviser les clauses de résiliation, délais de préavis, exigences de suppression des données | Liste de contrôle de révision contractuelle |
| **Évolutions organisationnelles** | Évaluer les changements d'appétit au risque, de stratégie métier, de personnel | Document d'alignement stratégique |

**Exigences de tests annuels (conformes DORA article 28.6) :**

| Type de stratégie de sortie | Exigence de test | Preuves | Fréquence |
|----------------------------|-----------------|---------|-----------|
| **Nuage-vers-nuage** | Exporter un sous-ensemble de données (échantillon 10-20 %), déployer chez le prestataire alternatif | Captures d'écran PoC, rapport de validation des exportations, devis de coûts | Annuelle |
| **Hybride** | Tester la connectivité hybride, la latence de synchronisation des données, les procédures de basculement | Métriques de performance réseau, résultats des tests de synchronisation, journal de basculement | Annuelle |
| **Sur site** | Mettre à jour le calcul TCO, vérifier la disponibilité/capacité de l'infrastructure | Tableur TCO, rapport de planification des capacités, devis fournisseurs | Annuelle |

**Profondeur des tests :**

| Criticité du service | Profondeur des tests | Taille de l'échantillon |
|---------------------|---------------------|------------------------|
| **Critique** | Simulation complète de sortie (exporter toutes les données, déployer dans l'environnement alternatif) | 100 % des données, charge complète |
| **Élevée** | Test sur échantillon significatif (exporter 50 % des données, déployer une charge représentative) | Échantillon de 50 % |
| **Moyen** | Échantillon représentatif (exporter 10-20 % des données, valider le format) | Échantillon de 10-20 % |
| **Faible** | Vérification uniquement (confirmer l'existence de la capacité d'exportation) | Revue documentaire |

**Documentation et preuves :**

Tous les résultats de tests DOIVENT être documentés dans :

- **ISMS-IMP-A.5.19-23.4-UG/TG** (Cahier Gouvernance et gestion des risques) — onglet « Stratégie de sortie »

**Preuves requises :**

| Type de preuve | Description | Conservation |
|---------------|-------------|-------------|
| **Résultats des tests d'exportation** | Captures d'écran, listes de fichiers, validation de l'intégrité des données | 3 ans |
| **Devis de coûts** | Tarification du prestataire alternatif (calcul, stockage, réseau, licences) | 1 an (renouvellement annuel) |
| **Rapports de PoC** | Résultats du déploiement preuve de concept, métriques de performance, problèmes identifiés | 3 ans |
| **Mises à jour du calendrier** | Calendrier de migration révisé selon l'expérience des tests | 1 an (renouvellement annuel) |
| **Retours d'expérience** | Difficultés rencontrées, améliorations des processus | 3 ans |

**Escalade et correction :**

| Constat | Action | Délai |
|---------|--------|-------|
| **Sortie non réalisable** | Initier l'évaluation d'un prestataire alternatif ou la refonte architecturale | 3 mois |
| **Inversion des coûts** | Réévaluer la décision nuage vs. sur site, envisager des prestataires alternatifs | 6 mois |
| **Non-conformité réglementaire** | Correction immédiate, envisager un prestataire alternatif ou un modèle hybride | 30 jours |
| **Échec de la portabilité des données** | Engager le prestataire pour corriger l'exportation, évaluer une méthode de sortie alternative | 60 jours |
| **Prestataire alternatif non disponible** | Identifier des alternatives supplémentaires, envisager une architecture multi-cloud | 3 mois |

**Cycle de révision :**

- **Trimestrielle** : Services critiques (niveau de risque = Critique)
- **Semestrielle** : Services à risque élevé (niveau de risque = Élevé)
- **Annuelle** : Services à risque moyen/faible

**Piste d'audit :**

Les révisions et résultats de tests des stratégies de sortie doivent être conservés à des fins d'audit :

- **Emplacement des preuves** : `/evidence/cloud-services/exit-strategy/YYYY/`
- **Convention de nommage** : `EV-EXIT-[ID-Service]-[AAAAMMJJ]-[Type-Test].pdf`
- **Durée de conservation** : 3 ans minimum (7 ans pour les entités réglementées par DORA)

## Déclencheurs de sortie

| Déclencheur | Réponse |
|------------|---------|
| Résiliation du contrat | Exécuter la sortie planifiée |
| Défaillance du prestataire | Procédures de sortie d'urgence |
| Violation de sécurité | Décision de sortie fondée sur le risque |
| Défaillance de conformité | Sortie immédiate ou correction |
| Coût ou valeur | Transition planifiée |
| Changement stratégique | Transition planifiée |

## Exigences de portabilité des données

| Exigence | Description |
|----------|-------------|
| Format d'exportation | Formats standards du secteur, documentés |
| Méthode d'exportation | Mécanisme d'extraction sécurisé et fiable |
| Complétude | Toutes les données, métadonnées, configurations |
| Validation | Vérification de l'intégrité de l'exportation |
| Calendrier | Fenêtre raisonnable pour l'extraction |
| Assistance | Support du prestataire pour la migration |

## Exécution de la sortie

| Phase | Activités |
|-------|----------|
| **Planification** | Confirmer la stratégie, le calendrier, les ressources |
| **Préparation** | Configurer la cible, tester la migration |
| **Exécution** | Exporter les données, migrer les services, valider |
| **Résiliation** | Confirmer la suppression des données, clôturer les comptes |
| **Vérification** | Certificat de destruction, suppression des accès |

## Atténuation du verrouillage fournisseur

| Stratégie | Mise en œuvre |
|-----------|--------------|
| Formats standards | Utiliser des formats de données portables |
| Abstraction des API | Éviter les intégrations propriétaires profondes |
| Capacité multi-cloud | Concevoir pour la portabilité |
| Tests d'exportation réguliers | Vérifier que les données peuvent être extraites |
| Évaluation des alternatives | Maintenir une connaissance des alternatives disponibles |

---

# Exigences de sécurité propres au nuage

## Gestion des identités et des accès

| Exigence | Mise en œuvre |
|----------|--------------|
| Identité fédérée | SSO via le fournisseur d'identité organisationnel |
| Application de l'AMF | Obligatoire pour tous les utilisateurs, impérative pour les administrateurs |
| Accès à privilèges | Juste-à-temps, limité dans le temps, supervisé |
| Comptes de service | Inventaire, rotation des identifiants, moindre privilège |
| Révisions des accès | Certification régulière des droits d'accès |

## Protection des données

| Exigence | Mise en œuvre |
|----------|--------------|
| Chiffrement en transit | TLS 1.2+ pour toutes les communications |
| Chiffrement au repos | Clés gérées par le prestataire ou le client |
| Gestion des clés | Stockage sécurisé des clés, politique de rotation |
| Classification des données | Étiquettes appliquées, contrôles appliqués |
| Résidence des données | Localisation du traitement documentée et vérifiée |
| Ségrégation des données | Isolation logique ou physique selon les exigences |

## Surveillance de la sécurité

| Exigence | Mise en œuvre |
|----------|--------------|
| Journalisation des audits | Tous les événements pertinents pour la sécurité sont journalisés |
| Centralisation des journaux | Journaux exportés vers le SIEM organisationnel |
| Alertes | Les événements de sécurité déclenchent les alertes appropriées |
| Conservation | Journaux conservés conformément à la politique (minimum 12 mois) |
| Détection des menaces | Détection par le prestataire et par l'organisation |

---

# Considérations multi-cloud

## Défis du multi-cloud

| Défi | Atténuation |
|------|-------------|
| Contrôles incohérents | Référentiel de base standardisé entre les prestataires |
| Lacunes de visibilité | Supervision et journalisation unifiées |
| Exigences en compétences | Formation et documentation |
| Complexité | Architecture et gouvernance claires |
| Gestion des coûts | Suivi et optimisation centralisés |

## Gouvernance multi-cloud

| Élément | Exigence |
|---------|----------|
| Cohérence des politiques | Mêmes politiques de sécurité entre les prestataires |
| Fédération d'identité | Identité unifiée entre les clouds |
| Supervision | Surveillance de la sécurité via les tableaux de bord |
| Réponse aux incidents | Procédures de réponse coordonnées |
| Conformité | Posture de conformité cohérente |

---

# Références

| Document | Relation |
|----------|---------|
| ISMS-POL-A.5.19-23 | Cadre de politique parentale |
| ISMS-POL-A.5.19-23-S1 | Les prestataires cloud sont des fournisseurs |
| ISMS-POL-A.5.19-23-S2 | Exigences contractuelles cloud |
| ISMS-POL-A.5.19-23-S3 | Gestion des sous-traitants cloud |
| ISMS-POL-A.5.19-23-S4 | Surveillance des services en nuage |
| ISO/IEC 27017 | Contrôles de sécurité pour les services en nuage |
| ISO/IEC 27018 | Protection de la vie privée dans le nuage |

---

**Document suivant :** ISMS-POL-A.5.19-23-S6 — Méthodologie d'évaluation et automatisation

<!-- QA_VERIFIED: 2026-03-30 -->
