<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.7-FR:framework:POL:a.5.7 -->
**ISMS-POL-A.5.7 — Renseignement sur les menaces**

---

**Contrôle documentaire**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Politique de renseignement sur les menaces |
| **Type de document** | Politique |
| **Identifiant du document** | ISMS-POL-A.5.7 |
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
| 1.0 | [Date] | RSSI | Politique initiale pour la certification ISO 27001:2022 |

**Cycle de révision** : Annuel
**Prochaine date de révision** : [Date d'entrée en vigueur + 12 mois]

**Chaîne d'approbation** :

- Primaire : Responsable de la sécurité des systèmes d'information (RSSI)
- Secondaire : Directeur des systèmes d'information (DSI)
- Risque : Directeur des risques (CRO)
- Conformité : Responsable juridique/conformité
- Autorité finale : Direction générale

**Documents connexes** :

- ISMS-POL-00 (Cadre d'applicabilité réglementaire)
- ISMS-IMP-A.5.7.1-UG/TG (Évaluation des sources de renseignement sur les menaces)
- ISMS-IMP-A.5.7.2-UG/TG (Évaluation de la collecte et de l'analyse de renseignements)
- ISMS-IMP-A.5.7.3-UG/TG (Évaluation de l'intégration et de la diffusion du renseignement)
- ISO/IEC 27001:2022 Contrôle A.5.7

---

# Résumé exécutif

La présente politique établit les exigences de [Organisation] en matière de renseignement sur les menaces, afin de permettre une défense proactive, d'informer la gestion des risques et de renforcer les opérations de sécurité conformément au contrôle A.5.7 de l'ISO/IEC 27001:2022.

**Objet** : Définir les exigences organisationnelles pour la gouvernance du renseignement sur les menaces. Cette politique établit QUELLES capacités de renseignement sont requises et QUI en est responsable. Les procédures de mise en œuvre (COMMENT) sont documentées séparément dans ISMS-IMP-A.5.7 (variantes UG/TG).

**Périmètre** : Cette politique s'applique à :

- Toutes les activités de renseignement sur les menaces (collecte, analyse, production, diffusion)
- Tous les types de renseignements (stratégiques, tactiques, opérationnels)
- Toutes les sources de renseignements (plateformes commerciales, OSINT, flux gouvernementaux, télémétrie interne)
- Tout le personnel impliqué dans les opérations de sécurité
- Tous les outils de sécurité intégrant le renseignement sur les menaces

**Alignement réglementaire** : Cette politique répond aux exigences de conformité obligatoires définies dans ISMS-POL-00, notamment le nLPD suisse, le RGPD de l'UE et l'ISO/IEC 27001:2022. Des exigences sectorielles (PCI DSS v4.0.1, FINMA, DORA, NIS2) s'appliquent lorsque les activités de [Organisation] déclenchent leur applicabilité.

---

# Périmètre

## Contrôle ISO/IEC 27001:2022 A.5.7

**Annexe A.5.7 de l'ISO/IEC 27001:2022 — Renseignement sur les menaces**

> *Les informations relatives aux menaces pesant sur la sécurité de l'information devraient être collectées et analysées pour produire des renseignements sur les menaces.*

**Objectif du contrôle** : Établir une politique organisationnelle pour les contrôles de renseignement sur les menaces permettant une détection proactive, l'information des décisions de gestion des risques, la priorisation des investissements de sécurité et le renforcement de l'efficacité de la réponse aux incidents.

## Périmètre de la politique

**Cette politique porte sur** (CE QUOI/QUI) :

- Exigences de collecte de renseignements à partir de plusieurs types de sources
- Exigences d'analyse et de production de renseignements
- Exigences de diffusion des renseignements aux parties prenantes
- Exigences d'intégration avec l'évaluation des risques (clause 6.1 de l'ISO 27001)
- Exigences d'intégration avec la gestion des incidents (contrôles A.5.24-5.28)
- Rôles et responsabilités organisationnels
- Cadres de dérogations et de gouvernance

**Cette politique ne porte PAS sur** (COMMENT — voir ISMS-IMP-A.5.7) :

- Les détails techniques de mise en œuvre et la configuration des plateformes
- Les outils spécifiques de renseignement ou la sélection de fournisseurs
- Les cadres d'analyse détaillés et les procédures des analystes
- Les méthodologies spécifiques de mesure des KPI
- Les procédures de déploiement des IoC
- Les critères de notation pour l'évaluation des sources

## Couverture organisationnelle

**Dans le périmètre** :

- Tous les employés (permanents, temporaires, prestataires)
- Toutes les équipes d'opérations de sécurité et de réponse aux incidents
- Toutes les fonctions de gestion des risques et de conformité
- Les prestataires de services tiers ayant accès aux renseignements sur les menaces
- Tous les sites et unités organisationnels

**Hors périmètre** :

- Les opérations cyber offensives ou les actions de représailles (interdites)
- Les enquêtes des forces de l'ordre (coopération soutenue, non conduite)
- L'analyse de vulnérabilités et les tests de pénétration (couverts par le contrôle A.8.8)
- Les opérations de chasse aux menaces (couvertes par le contrôle A.8.16)

---

# Énoncés de politique

## Collecte de renseignements sur les menaces

[Organisation] DOIT mettre en œuvre la collecte de renseignements sur les menaces à partir de plusieurs catégories de sources pour assurer une visibilité complète sur les menaces.

**Catégories de sources requises** :

- **Plateformes commerciales** : Flux de renseignements sur les menaces organisés avec validation
- **Renseignement de source ouverte (OSINT)** : Données publiques sur les menaces, bases de données de vulnérabilités
- **Flux gouvernementaux/CERT** : Avis des CERT nationaux, alertes sur les infrastructures critiques
- **Partage sectoriel (ISAC/ISAO)** : Menaces spécifiques au secteur et collaboration avec les pairs (recommandé)
- **Télémétrie interne** : Alertes des outils de sécurité, données d'incidents, résultats forensiques

**Exigences de gestion des sources** :

- Toutes les sources DOIVENT être évaluées pour leur fiabilité et leur crédibilité avant leur mise en production
- Les sources DOIVENT être validées périodiquement pour leur exactitude et leurs performances
- Les exigences de protection des données DOIVENT être appliquées à tous les renseignements collectés
- Le partage avec des tiers DOIT être régi par les classifications du Traffic Light Protocol (TLP)

**Référence de mise en œuvre** : Inventaire des sources et critères d'évaluation documentés dans ISMS-IMP-A.5.7.1.

## Analyse et production de renseignements sur les menaces

[Organisation] DOIT mettre en œuvre une analyse structurée du renseignement pour transformer les données brutes sur les menaces en renseignements exploitables.

**Exigences de production de renseignements** :

**Renseignement stratégique** (Audience : direction générale) :

- Évaluations du paysage des menaces et analyse des tendances
- Recommandations d'investissements en sécurité fondées sur les risques
- Produit au minimum trimestriellement, ou déclenché par des événements significatifs

**Renseignement tactique** (Audience : opérations de sécurité) :

- Profils d'acteurs de menaces et TTPs
- Analyse de campagnes et schémas d'attaque
- Produit au minimum mensuellement, ou déclenché par des menaces émergentes

**Renseignement opérationnel** (Audience : équipes techniques) :

- Indicateurs de compromission (IoC) pour la détection
- Signatures de logiciels malveillants et indicateurs comportementaux
- Produit en continu via des flux automatisés, avec revue quotidienne des analystes

**Exigences de qualité** :

- Tous les produits de renseignement DOIVENT citer leurs sources avec évaluation de la fiabilité
- Le renseignement DOIT être validé par plusieurs sources dans la mesure du possible
- Le renseignement DOIT être rattaché au modèle de menaces et aux actifs de [Organisation]
- Le renseignement DOIT inclure des recommandations exploitables ou des orientations de détection
- Le renseignement DOIT être classifié selon le TLP et les schémas de classification internes

**Référence de mise en œuvre** : Cadres d'analyse et métriques de production documentés dans ISMS-IMP-A.5.7.2.

## Diffusion du renseignement sur les menaces

[Organisation] DOIT mettre en œuvre une diffusion structurée du renseignement pour que les bons renseignements parviennent aux bonnes parties prenantes.

**Exigences de diffusion** :

- La direction générale DOIT recevoir les évaluations stratégiques des menaces
- Les opérations de sécurité DOIVENT recevoir les IoC opérationnels et les TTPs tactiques
- La réponse aux incidents DOIT recevoir les renseignements pertinents pour les enquêtes
- La gestion des risques DOIT recevoir les données sur les menaces pour les mises à jour de l'évaluation des risques
- Les opérations informatiques DOIVENT recevoir les orientations de blocage liées aux infrastructures

**Contrôles de partage** :

- Le partage externe DOIT être régi par le Traffic Light Protocol (TLP)
- Les consommateurs de renseignements DOIVENT fournir des retours sur l'efficacité du renseignement
- Des boucles de rétroaction bidirectionnelles DOIVENT être établies entre consommateurs et producteurs

**Référence de mise en œuvre** : Suivi de la diffusion et engagement des parties prenantes documentés dans ISMS-IMP-A.5.7.3.

## Intégration avec l'évaluation des risques (OBLIGATOIRE)

Le renseignement sur les menaces DOIT informer le processus d'évaluation des risques de [Organisation] conformément à la clause 6.1 de l'ISO 27001:2022.

**Exigences d'intégration** :

- Les résultats du renseignement sur les menaces DOIVENT informer les estimations de vraisemblance des risques de sécurité
- Les campagnes de menaces émergentes DOIVENT déclencher une réévaluation des risques lorsqu'elles ciblent le secteur de [Organisation]
- Le renseignement sur l'exploitation des vulnérabilités DOIT informer les évaluations d'impact
- Les recommandations du renseignement sur les menaces DOIVENT informer la sélection et la priorisation des contrôles
- Les mises à jour du registre des risques DOIVENT référencer les rapports de renseignement sur les menaces qui les soutiennent

**Exigences documentaires** :

- Chaque mise à jour de l'évaluation des risques DOIT documenter la source du renseignement
- La traçabilité entre les rapports de renseignement et les entrées du registre des risques DOIT être maintenue

**Référence de mise en œuvre** : Suivi de l'intégration des risques documenté dans ISMS-IMP-A.5.7.3.

## Intégration avec la gestion des incidents (OBLIGATOIRE)

Le renseignement sur les menaces DOIT renforcer la détection, l'investigation et la réponse aux incidents conformément aux contrôles A.5.24-5.28.

**Exigences d'intégration** :

- Les IoC du renseignement sur les menaces DOIVENT être déployés dans les outils de détection
- Les TTPs des acteurs de menaces DOIVENT être traduits en règles de détection
- Le renseignement sur les menaces DOIT fournir du contexte lors des investigations d'incidents
- Les résultats des incidents DOIVENT contribuer à la collecte interne de renseignements
- Les revues post-incident DOIVENT valider l'efficacité du renseignement sur les menaces

**Référence de mise en œuvre** : Suivi de l'intégration incidents-renseignements documenté dans ISMS-IMP-A.5.7.3.

## Intégration avec la gestion des vulnérabilités (OPTIONNEL)

Lorsque [Organisation] met en œuvre le contrôle A.8.8 (Gestion des vulnérabilités techniques), l'intégration du renseignement sur les menaces est OPTIONNELLE mais recommandée.

**Si mis en œuvre** :

- Le renseignement sur les vulnérabilités DOIT combiner les données CVE avec le statut d'exploitation
- Le renseignement sur l'exploitation active DOIT informer la priorisation de la remédiation
- Les scores CVSS combinés avec le renseignement sur les menaces DOIVENT permettre une priorisation fondée sur les risques

**Référence de mise en œuvre** : Lorsque mis en œuvre, l'intégration VulnérabilityThreatLink est documentée dans ISMS-IMP-A.5.7.2 et ISMS-IMP-A.8.8.

## Mesure de l'efficacité

[Organisation] DOIT mesurer l'efficacité du programme de renseignement sur les menaces par des métriques objectives.

**Domaines de mesure requis** :

- Mises à jour de l'évaluation des risques pilotées par le renseignement sur les menaces
- Incidents prévenus ou détectés grâce au renseignement sur les menaces
- Exactitude et performances des sources
- Enrichissement des investigations d'incidents avec le renseignement sur les menaces
- Décisions de sécurité informées par le renseignement
- Satisfaction des parties prenantes vis-à-vis des produits de renseignement

**Maturité du programme** :

- [Organisation] DOIT évaluer annuellement la maturité du programme de renseignement
- L'évaluation DOIT couvrir la collecte, l'analyse, la diffusion, l'opérationnalisation et la gouvernance

**Référence de mise en œuvre** : Métriques d'efficacité et suivi des KPI documentés dans le tableau de bord de synthèse.

---

# Rôles et responsabilités

## Matrice de responsabilités

| Rôle | Responsabilités |
|------|-----------------|
| **Direction générale** | Approbation stratégique, allocation des ressources, approbation de la politique |
| **Responsable de la sécurité des systèmes d'information (RSSI)** | Propriété de la politique, supervision du programme, approbation des dérogations |
| **Directeur des risques (CRO)** | Intégration dans l'évaluation des risques, approbation des mises à jour de risques pilotées par le renseignement |
| **Responsable de l'équipe de renseignement sur les menaces** | Gestion du programme, production de renseignements, gestion des sources |
| **Analystes en renseignement sur les menaces** | Collecte, analyse, production, assurance qualité |
| **Opérations de sécurité (SOC)** | Opérationnalisation du renseignement, déploiement des IoC, ajustement de la détection |
| **Équipe de réponse aux incidents** | Application du renseignement lors des investigations, extraction des IoC |
| **Opérations informatiques** | Mise en œuvre technique des contrôles pilotés par le renseignement |
| **Équipe de gestion des risques** | Mises à jour de l'évaluation des risques fondées sur le renseignement |
| **Conformité/Juridique** | Interprétation réglementaire, conformité à la protection des données |
| **Tout le personnel** | Sensibilisation aux menaces, signalement des activités suspectes |

## Voie d'escalade

- Problèmes opérationnels : Analyste → Responsable équipe renseignement → Équipe sécurité → RSSI
- Dérogations techniques : Responsable équipe renseignement → Équipe sécurité → RSSI
- Préoccupations de conformité : Responsable équipe renseignement → Conformité → RSSI → Direction générale
- Questions de risque : Responsable équipe renseignement → CRO → RSSI → Direction générale
- Incidents de sécurité : Tout personnel → SOC → Réponse aux incidents → RSSI

## Exigences de formation

- **Tout le personnel** : Sensibilisation annuelle à la sécurité incluant un aperçu du paysage des menaces
- **Analystes en renseignement** : Formation spécialisée sur les cadres d'analyse et la rédaction de rapports
- **Personnel SOC** : Formation sur l'opérationnalisation du renseignement et le déploiement des IoC
- **Direction sécurité** : Séances d'information sur le renseignement stratégique

## Continuité des activités

[Organisation] DOIT assurer la continuité des capacités critiques de renseignement sur les menaces :

- Analystes primaires et de secours désignés pour chaque fonction de renseignement
- Redondance des sources pour les catégories de renseignements critiques
- Procédures de basculement documentées pour la plateforme de renseignement
- Test annuel de la continuité des activités pour les opérations de renseignement

---

# Conformité et dérogations

## Applicabilité réglementaire

**Niveau 1 : Conformité obligatoire**

| Réglementation | Exigences clés |
|----------------|----------------|
| **nLPD suisse** | Art. 8 — Mesures techniques et organisationnelles pour la détection des menaces |
| **RGPD UE** | Art. 32 — Mesures de sécurité incluant la surveillance des menaces |
| **ISO/IEC 27001:2022** | Contrôle A.5.7 — Collecte et analyse de renseignements sur les menaces |

**Niveau 2 : Applicabilité conditionnelle** (conformément à ISMS-POL-00)

| Réglementation | Condition déclenchante |
|----------------|------------------------|
| **FINMA** | Établissement financier réglementé suisse |
| **DORA** | Entité de services financiers UE |
| **NIS2** | Entité essentielle/importante (UE) |

**Détermination de la conformité** : [Organisation] détermine les réglementations de niveau 2 applicables par le biais d'évaluations périodiques de ses activités. Les exigences les plus strictes s'appliquent lorsque plusieurs réglementations se recoupent.

## Gestion des dérogations

Les dérogations aux exigences de renseignement sur les menaces nécessitent une justification commerciale documentée, une évaluation des risques et une approbation formelle.

**Types de dérogations** :

- Dérogations de couverture des sources (contraintes budgétaires)
- Dérogations de délai d'intégration (complexité technique)
- Dérogations de ressources (effectif insuffisant)
- Dérogations d'objectifs KPI (programme nouvellement mis en œuvre)

**Exigences de dérogation** :

- Limitées dans le temps avec dates d'expiration explicites
- Contrôles compensatoires documentés et vérifiés
- Revue trimestrielle de la nécessité de la dérogation
- Preuve de progression vers la conformité complète

**Autorité d'approbation** :

- RSSI : Dérogations de sources, d'intégration et de KPI
- RSSI + Direction générale : Dérogations de ressources

**Documentation** : Demandes et approbations de dérogations maintenues dans le registre des dérogations.

## Intégration avec la réponse aux incidents

Lorsque le renseignement sur les menaces identifie des menaces imminentes ou actives, les procédures de réponse aux incidents s'appliquent conformément aux contrôles A.5.24-5.28.

**Réponse fondée sur la gravité** :

- Résultats critiques/élevés : Escalade immédiate vers le SOC et la réponse aux incidents
- Résultats moyens/faibles : Processus standard de diffusion du renseignement
- Séances d'information d'urgence : RSSI informé selon la classification de gravité de l'incident

**Exigences de coordination** :

- L'équipe de renseignement sur les menaces soutient les investigations d'incidents
- L'équipe de réponse aux incidents extrait les IoC pour le partage de renseignements
- Les revues post-incident évaluent l'efficacité du renseignement

---

# Gouvernance de la politique

## Révision de la politique

- **Fréquence** : Annuelle au minimum
- **Déclencheurs** : Changements réglementaires, incidents majeurs, changements significatifs du paysage des menaces, changements organisationnels, conclusions d'audit
- **Réviseurs** : RSSI, responsable de l'équipe de renseignement, équipe sécurité, gestion des risques, conformité
- **Approbation** : RSSI (technique), direction générale (stratégique)

## Mises à jour de la politique

- **Mineures** (clarifications, références) : Approbation RSSI, communication dans les 30 jours
- **Majeures** (changements de périmètre, nouvelles exigences) : Chaîne d'approbation complète
- **D'urgence** (menaces critiques) : Approbation RSSI, communication immédiate

## Normes de mise en œuvre

Les mises à jour des normes de mise en œuvre (ISMS-IMP-A.5.7) ne nécessitent pas de révision de la politique. Le guide de mise en œuvre est examiné trimestriellement par l'équipe sécurité avec approbation du RSSI.

---

# Documents connexes

## Intégration avec le SMSI

Cette politique s'intègre dans le Système de management de la sécurité de l'information de [Organisation] :

- **Évaluation des risques** (Clause 6.1) : Le renseignement sur les menaces informe l'identification et l'analyse des risques
- **Déclaration d'applicabilité** (Clause 6.1.3) : Applicabilité du contrôle A.5.7 documentée
- **Audit interne** (Clause 9.2) : Programme de renseignement inclus dans le périmètre d'audit du SMSI
- **Amélioration continue** (Clause 10) : Les métriques contribuent à l'évaluation des performances du SMSI

## Contrôles connexes

| Contrôle | Type d'intégration | Description |
|----------|-------------------|-------------|
| **A.5.24-5.28** | OBLIGATOIRE | Gestion des incidents — le renseignement renforce la détection et la réponse |
| **A.8.16** | OBLIGATOIRE | Activités de surveillance — le renseignement fournit le contexte de détection |
| **A.8.8** | OPTIONNEL | Gestion des vulnérabilités — le renseignement priorise la remédiation |
| **A.5.19-5.22** | OPTIONNEL | Sécurité des fournisseurs — le renseignement évalue les risques tiers |
| **A.5.23** | OPTIONNEL | Sécurité cloud — le renseignement couvre les menaces spécifiques au cloud |
| **A.8.23** | OPTIONNEL | Filtrage web — le renseignement fournit des flux de domaines malveillants |

## Ressources de mise en œuvre

- **ISMS-IMP-A.5.7.1-UG/TG** : Évaluation des sources de renseignement sur les menaces
- **ISMS-IMP-A.5.7.2-UG/TG** : Évaluation de la collecte et de l'analyse de renseignements
- **ISMS-IMP-A.5.7.3-UG/TG** : Évaluation de l'intégration et de la diffusion du renseignement

---

# Définitions

**Renseignement sur les menaces** : Collecte, analyse et diffusion d'informations sur les menaces actuelles ou émergentes, permettant une défense proactive et des décisions de sécurité éclairées.

**Renseignement stratégique** : Renseignement de haut niveau portant sur les menaces et tendances générales, soutenant les décisions de la direction et la stratégie à long terme.

**Renseignement tactique** : Renseignement décrivant les tactiques, techniques et procédures (TTPs) des adversaires, soutenant les opérations de sécurité et la planification de la défense.

**Renseignement opérationnel** : Renseignement technique exploitable incluant les IoC et les règles de détection, soutenant les opérations de sécurité immédiates.

**Indicateur de compromission (IoC)** : Artefact observable indiquant qu'une violation de sécurité s'est produite ou est en cours (adresses IP, domaines, hachages de fichiers).

**Tactiques, Techniques et Procédures (TTPs)** : Schémas d'activités utilisés par les acteurs de menaces, documentés dans des référentiels comme MITRE ATT&CK.

**Traffic Light Protocol (TLP)** : Norme de partage d'informations utilisant des codes couleur (ROUGE, AMBRE, AMBRE+STRICT, VERT, CLAIR) pour indiquer les restrictions de diffusion.

**CVSS (Common Vulnerability Scoring System)** : Norme d'évaluation de la gravité des vulnérabilités (0,0 à 10,0). CVSS 4.0 est la norme actuelle ; CVSS 3.1 reste largement déployé.

**Acteur de menace** : Individu, groupe ou organisation conduisant des activités cyber malveillantes.

---

# Éléments de preuve pour cette politique

**Éléments de preuve pour l'Étape 1 (revue documentaire) :**

Éléments de preuve requis pour démontrer que cette politique est adéquatement documentée et approuvée :

- ✅ Ce document de politique (ISMS-POL-A.5.7 v1.0)
- ✅ Signatures d'approbation du RSSI et de la direction générale
- ✅ Cadre de gouvernance du renseignement sur les menaces défini (Section 2.1)
- ✅ Types de sources et exigences de collecte documentés (Section 2.2)
- ✅ Exigences d'analyse et de production précisées (Section 2.3)
- ✅ Exigences de diffusion et des parties prenantes documentées (Section 2.4)
- ✅ Exigences d'intégration dans l'évaluation des risques définies (Section 2.5)
- ✅ Exigences d'intégration dans la gestion des incidents précisées (Section 2.6)
- ✅ Rôles et responsabilités attribués (Section 3)
- ✅ Procédures de gouvernance et de dérogations définies (Section 3.6)
- ✅ Intégration avec les contrôles connexes documentée (Section 4.1)

**Éléments de preuve pour l'Étape 2 (efficacité opérationnelle) :**

Éléments de preuve requis pour démontrer que cette politique est opérationnellement efficace :

- Évaluations des sources de renseignement complétées conformément à ISMS-IMP-A.5.7.1 (inventaire des sources, évaluations selon le code Amirauté, validation des performances)
- Évaluations de la collecte et de l'analyse conformément à ISMS-IMP-A.5.7.2 (analyse de couverture, cartographie MITRE ATT&CK, métriques de production)
- Évaluations de l'intégration et de la diffusion conformément à ISMS-IMP-A.5.7.3 (statut d'intégration des outils, déploiement des IoC, engagement des parties prenantes)
- Mises à jour de l'évaluation des risques pilotées par le renseignement (≥ 3 exemples par trimestre avec traçabilité)
- Documentation des incidents prévenus (≥ 3 exemples par trimestre avec éléments de validation)
- Rapports de validation des performances des sources (trimestriels, montrant un taux d'exactitude ≥ 85 %)
- Relevés d'enrichissement des incidents (≥ 70 % des incidents P1/P2 avec contexte de renseignement)
- Décisions de sécurité pilotées par le renseignement (≥ 5 exemples par trimestre avec résultats documentés)
- Journaux opérationnels et métriques d'utilisation de la plateforme de renseignement
- Rapports de renseignements stratégiques, tactiques et opérationnels distribués aux parties prenantes
- Accords de partage de renseignements (le cas échéant)
- Résultats des tests de continuité des activités du programme de renseignement (annuels)
- Approbations de dérogations pour les écarts de renseignement (le cas échéant)
- Relevés de formation du personnel de renseignement
- Métriques d'efficacité suivies dans les tableaux de bord de synthèse

**Précision sur les éléments de preuve de conformité :**

Cette politique établit le cadre de gouvernance du renseignement sur les menaces (exigences de collecte, d'analyse, de production et de diffusion). Elle n'établit PAS :

- **Les contrôles techniques de détection** (traités dans A.8.16 Activités de surveillance — le renseignement fournit le contexte des règles de détection)
- **Les procédures de réponse aux incidents** (traitées dans A.5.24-5.28 Gestion des incidents — le renseignement renforce les investigations)
- **La priorisation des vulnérabilités** (traitée dans A.8.8 Gestion des vulnérabilités — l'intégration VulnérabilityThreatLink est optionnelle)
- **Les profils spécifiques d'acteurs de menaces** (renseignement opérationnel maintenu dans la plateforme, non dans la politique)
- **La sélection d'outils ou la configuration de plateformes** (décisions de mise en œuvre fondées sur les besoins organisationnels)

La délimitation est : POL-A.5.7 définit le cadre de gouvernance → Suite ISMS-IMP-A.5.7 fournit les procédures d'évaluation → La plateforme de renseignement met en œuvre la collecte/analyse technique → D'autres contrôles (A.8.16, A.5.24-28, A.8.8) consomment les résultats du renseignement pour leurs finalités respectives.

---

# Enregistrement des approbations

| Rôle | Nom | Date |
|------|-----|------|
| **Responsable de la sécurité des systèmes d'information (RSSI)** | [Nom] | [Date à définir] |
| **Directeur des systèmes d'information (DSI)** | [Nom] | [Date à définir] |
| **Directeur des risques (CRO)** | [Nom] | [Date à définir] |
| **Responsable juridique/conformité** | [Nom] | [Date à définir] |
| **Direction générale** | [Nom] | [Date à définir] |

---

**FIN DU DOCUMENT DE POLITIQUE**

---

*Cette politique établit les exigences en matière de renseignement sur les menaces. Les procédures de mise en œuvre sont documentées dans ISMS-IMP-A.5.7 (UG/TG).*

<!-- QA_VERIFIED: 2026-03-30 -->
