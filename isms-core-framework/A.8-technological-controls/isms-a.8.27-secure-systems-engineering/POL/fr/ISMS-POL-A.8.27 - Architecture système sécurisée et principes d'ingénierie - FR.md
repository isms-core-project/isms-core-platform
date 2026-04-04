<!-- ISMS-CORE:POLICY:ISMS-POL-A.8.27-FR:framework:POL:a.8.27 -->
**ISMS-POL-A.8.27 — Architecture système sécurisée et principes d'ingénierie**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Architecture système sécurisée et principes d'ingénierie |
| **Type de document** | Politique |
| **Identifiant du document** | ISMS-POL-A.8.27 |
| **Créateur du document** | Responsable de la Sécurité des Systèmes d'Information (RSSI) |
| **Propriétaire du document** | Responsable de la Sécurité des Systèmes d'Information (RSSI) |
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

- Principale : Responsable de la Sécurité des Systèmes d'Information (RSSI)
- Secondaire : Directeur de la Technologie (DT)
- Autorité finale : Direction générale

**Documents connexes** :

- ISMS-POL-00 (Cadre d'applicabilité réglementaire)
- ISMS-POL-A.8.25-26-29 (Cadre de développement sécurisé)
- ISMS-POL-A.8.28 (Règles de codage sécurisé)
- ISMS-POL-A.8.9 (Gestion de la configuration)
- ISMS-POL-A.5.8 (Sécurité de l'information dans la gestion de projet)
- ISMS-IMP-A.8.27.1-UG/TG (Processus de revue d'architecture de sécurité)
- ISMS-IMP-A.8.27.2-UG/TG (Méthodologie de modélisation des menaces)
- ISMS-IMP-A.8.27.3-UG/TG (Catalogue de modèles d'architecture sécurisée)
- ISMS-IMP-A.8.27.4-UG/TG (Évaluation de la mise en œuvre Zéro Confiance)
- ISO/IEC 27001:2022 Contrôle A.8.27
- NIST SP 800-160 Vol. 1 Rév. 1 — Ingénierie de systèmes sécurisés de confiance
- NIST SP 800-160 Vol. 2 Rév. 1 — Développement de systèmes cyber-résilients
- NIST SP 800-207 — Architecture Zéro Confiance

---

## Résumé exécutif

Cette politique établit les exigences fondamentales de [Organisation] en matière d'Ingénierie des Systèmes Sécurisés (ISS) — la discipline consistant à intégrer la sécurité dans toutes les couches de l'architecture système tout au long du cycle de vie complet du système.

**Objet** : Définir les principes, les approches et les exigences pour l'ingénierie de systèmes sécurisés de confiance. Cette politique établit QUELS principes d'ingénierie sécurisée s'appliquent et QUI est responsable de leur mise en œuvre. Les procédures de mise en œuvre (COMMENT) sont documentées dans ISMS-IMP-A.8.27.

**Périmètre** : Cette politique s'applique à TOUS les systèmes conçus, développés, acquis, intégrés, exploités et maintenus par [Organisation], notamment les systèmes d'information, les technologies opérationnelles, les services cloud et les systèmes développés par des tiers.

**Principe fondateur** : La sécurité DOIT être aussi fondamentale dans la conception des systèmes que la performance et la sécurité fonctionnelle. La sécurité n'est pas un ajout mais une propriété inhérente des systèmes bien conçus.

**Concept clé** : Cette politique met en œuvre la « Sécurité par conception et par défaut » — le principe selon lequel la sécurité doit être intégrée dans les systèmes dès leur conception, et non ajoutée après le déploiement.

---

# Périmètre et alignement sur les contrôles

## Contrôle A.8.27 de la norme ISO/IEC 27001:2022

**Norme ISO/IEC 27001:2022 Annexe A.8.27 — Architecture système sécurisée et principes d'ingénierie**

> *Des principes pour l'ingénierie de systèmes sécurisés devraient être établis, documentés, maintenus et appliqués à toutes les activités de développement de systèmes d'information.*

**Objectif du contrôle** : S'assurer que la sécurité est intégrée dans toutes les couches d'architecture tout au long du cycle de vie du système, en promouvant les stratégies de « sécurité par conception », de Zéro Confiance et de défense en profondeur.

## Périmètre de la politique

**Cette politique s'applique à** :

| Catégorie | Périmètre |
|-----------|-----------|
| **Systèmes** | Tous les systèmes d'information, applications, infrastructure, services cloud, systèmes OT/ICS |
| **Phases du cycle de vie** | Concept, développement, production, utilisation, support, retrait |
| **Couches d'architecture** | Métier, données, application, technologie, sécurité |
| **Personnel** | Architectes systèmes, ingénieurs, développeurs, professionnels de la sécurité, développeurs tiers |
| **Processus** | Conception, développement, intégration, déploiement, exploitation, décommissionnement |

## Applicabilité réglementaire

**Niveau 1 — Conformité obligatoire** :

| Réglementation | Exigences ISS clés |
|----------------|-------------------|
| **nLPD suisse** | Article 8 — Mesures techniques proportionnées au risque |
| **RGPD de l'UE** | Article 25 — Protection des données dès la conception et par défaut |
| **ISO/IEC 27001:2022** | Contrôle A.8.27 |

**Niveau 2 — Applicabilité conditionnelle** :

| Réglementation | Déclencheur | Exigence |
|---------------|------------|---------|
| **DORA** | Services financiers UE | Cadre de gestion des risques TIC, architecture sécurisée |
| **NIS2** | Entité essentielle/importante | Exigences de sécurité par conception |
| **PCI DSS v4.0.1** | Traitement de cartes de paiement | Exigences de développement sécurisé |
| **FINMA** | Institution financière suisse | Exigences de sécurité de l'architecture IT |

---

# Énoncés de politique

## Principes fondamentaux d'ingénierie sécurisée

### Principes fondateurs

[Organisation] DOIT appliquer les principes fondamentaux d'ingénierie des systèmes sécurisés suivants à TOUTES les activités de développement et d'acquisition de systèmes :

**Principe 1 : Sécurité par conception**

La sécurité DOIT être intégrée dès les premières étapes de la conception du système :

- Les exigences de sécurité DOIVENT être identifiées pendant le développement du concept initial
- L'architecture de sécurité DOIT être définie avant le début de la conception détaillée
- Les contrôles de sécurité DOIVENT être conçus comme des composants systèmes intégraux, non comme des ajouts
- Les compromis de sécurité DOIVENT être explicitement documentés et approuvés

**Principe 2 : Sécurité par défaut**

Les systèmes DOIVENT être sécurisés dans leur configuration par défaut :

- Les configurations par défaut DOIVENT mettre en œuvre les paramètres de sécurité les plus restrictifs appropriés
- Les utilisateurs NE DOIVENT PAS avoir à prendre des mesures pour sécuriser le système
- Les fonctionnalités de sécurité optionnelles DOIVENT être activées par défaut sauf justification métier
- Le refus par défaut (default deny) DOIT être appliqué aux contrôles d'accès, aux communications réseau et aux capacités système

**Principe 3 : Défense en profondeur**

Plusieurs couches de contrôles de sécurité DOIVENT être mises en œuvre :

- Aucun contrôle unique NE DOIT être la seule protection pour les actifs critiques
- Les contrôles DOIVENT être mis en œuvre sur plusieurs couches d'architecture (réseau, plateforme, application, données)
- La défaillance d'un contrôle sur une couche NE DOIT PAS entraîner une compromission totale
- Les contrôles en couches DOIVENT être complémentaires, non redondants

**Principe 4 : Moindre privilège**

Tous les utilisateurs, processus et systèmes DOIVENT fonctionner avec les privilèges minimum nécessaires :

- Les droits d'accès DOIVENT être limités à ceux requis pour exercer les fonctions autorisées
- Les privilèges élevés DOIVENT être accordés uniquement en cas de besoin et révoqués lorsqu'ils ne sont plus nécessaires
- Les comptes de service DOIVENT avoir des permissions à périmètre étroitement défini
- L'accès administratif DOIT être séparé de l'accès opérationnel

**Principe 5 : Fonctionnalité minimale**

Les systèmes DOIVENT fournir uniquement les capacités requises pour leur objectif :

- Les services, protocoles et fonctionnalités inutiles DOIVENT être désactivés ou supprimés
- Les fonctionnalités système DOIVENT être limitées aux exigences métier documentées
- La surface d'attaque DOIT être minimisée par la réduction des fonctionnalités
- Les ports, interfaces et capacités inutilisés DOIVENT être désactivés

**Principe 6 : Défaillance sécurisée (Fail Secure)**

Les systèmes DOIVENT tomber en panne dans un état sécurisé :

- Les défaillances système NE DOIVENT PAS exposer des données ou des fonctionnalités sensibles
- Les échecs d'authentification DOIVENT refuser l'accès par défaut
- Les conditions d'erreur NE DOIVENT PAS révéler d'informations sensibles pour la sécurité
- La récupération après une défaillance DOIT nécessiter une ré-authentification et une ré-autorisation

### Principes d'architecture Zéro Confiance

[Organisation] DOIT mettre en œuvre les principes Zéro Confiance pour tous les systèmes :

**Ne jamais faire confiance, toujours vérifier** :

- Aucune confiance implicite basée sur l'emplacement réseau, la propriété de l'appareil ou l'authentification précédente
- Chaque demande d'accès DOIT être authentifiée et autorisée quelle que soit sa source
- La confiance DOIT être évaluée en continu, non accordée une fois pour toutes

**Supposer la violation (Assume Breach)** :

- Concevoir les systèmes en supposant que des adversaires peuvent déjà avoir accès au réseau
- Le trafic réseau interne DOIT être traité comme potentiellement hostile
- Le déplacement latéral DOIT être restreint par la segmentation et les contrôles d'accès
- Les capacités de détection DOIVENT supposer que les contrôles de périmètre peuvent avoir échoué

**Vérifier explicitement** :

- Les décisions d'accès DOIVENT être basées sur tous les points de données disponibles :
  - Identité et force d'authentification de l'utilisateur
  - Santé et statut de conformité de l'appareil
  - Sensibilité et classification des données
  - Contexte de la demande (emplacement, heure, modèles de comportement)
  - Détection des anomalies dans les demandes

**Accès au moindre privilège** :

- Accès juste-à-temps (JIT) pour les privilèges élevés
- Accès juste-suffisant (JEA) pour tous les octrois d'accès
- Politiques d'accès conditionnel basées sur les risques
- Évaluation et révocation continues de l'accès

**Chiffrement par défaut** :

- Toutes les données en transit DOIVENT être chiffrées (TLS 1.2+ minimum)
- Toutes les données au repos DOIVENT être chiffrées pour la classification Confidentielle+
- La communication interne entre services DOIT utiliser des canaux chiffrés
- Les clés de chiffrement DOIVENT être gérées conformément à ISMS-POL-A.8.24

### Mise en œuvre de la défense en profondeur

[Organisation] DOIT mettre en œuvre des contrôles de sécurité en couches sur toutes les couches d'architecture :

| Couche | Contrôles de sécurité | Correspondance contrôles ISO 27001 |
|--------|----------------------|-----------------------------------|
| **Périmètre** | Pare-feu, WAF, protection DDoS, passerelles sécurisées | A.8.20, A.8.21, A.8.22 |
| **Réseau** | Segmentation, micro-segmentation, contrôle d'accès réseau, IDS/IPS | A.8.20, A.8.22 |
| **Plateforme** | Configurations durcies, gestion des correctifs, protection des postes de travail | A.8.1, A.8.8, A.8.9 |
| **Application** | Validation des entrées, encodage des sorties, authentification, autorisation | A.8.25, A.8.26, A.8.28 |
| **Données** | Chiffrement, masquage, contrôles d'accès, DLP | A.8.10, A.8.11, A.8.12, A.8.24 |
| **Identité** | AMF, gestion des accès privilégiés, gouvernance des identités | A.5.15, A.5.16, A.5.18, A.8.2, A.8.5 |
| **Surveillance** | SIEM, analyses comportementales, détection des menaces, réponse aux incidents | A.8.15, A.8.16, A.5.24, A.5.25 |

## Exigences d'architecture système

### Revue d'architecture de sécurité

Tous les nouveaux systèmes et les modifications significatives des systèmes existants DOIVENT faire l'objet d'une revue d'architecture de sécurité.

**Déclencheurs de revue** :

- Nouveau développement ou acquisition de système
- Mises à niveau majeures de version ou migrations
- Changements d'architecture affectant les périmètres de sécurité
- Intégration de nouveaux services externes ou flux de données
- Changements des mécanismes d'authentification ou d'autorisation

**Processus de revue** :

1. Modélisation des menaces avec méthodologie structurée :
   - **STRIDE** comme méthodologie principale pour tous les systèmes (obligatoire)
   - **PASTA** pour les systèmes complexes nécessitant une simulation d'attaque (amélioration optionnelle)
   - Justification du choix de méthodologie documentée dans ISMS-IMP-A.8.27.2
2. Validation des exigences de sécurité par rapport aux exigences métier
3. Revue des modèles d'architecture par rapport aux modèles approuvés
4. Revue de la conception des contrôles pour la défense en profondeur
5. Évaluation des risques et documentation du risque résiduel
6. Approbation du RSSI ou de l'Architecte de sécurité avant mise en œuvre

**Critères d'approbation de la revue d'architecture** :

Les systèmes DOIVENT satisfaire les critères suivants avant l'approbation de l'architecture :

- ✅ Modèle de menaces complété avec la méthodologie approuvée
- ✅ Tous les risques ÉLEVÉS et CRITIQUES ont des plans de traitement approuvés
- ✅ L'architecture met en œuvre des modèles approuvés OU les dérogations ont l'approbation d'exception du RSSI
- ✅ Défense en profondeur validée sur toutes les couches d'architecture
- ✅ Principes Zéro Confiance abordés pour l'authentification, l'autorisation et les flux de données
- ✅ Exigences de sécurité traçables aux exigences métier
- ✅ Les intégrations tierces sont conformes à ISMS-POL-A.5.19-23

**La revue d'architecture NE DOIT PAS être approuvée si** :

- Risques critiques sans plan de traitement
- Dérogations aux modèles non approuvés sans contrôles compensatoires
- Couches de défense en profondeur manquantes pour les données Confidentielles+

### Modèles d'architecture sécurisée

[Organisation] DOIT maintenir un catalogue de modèles d'architecture sécurisée approuvés.

**Catégories de modèles** :

| Catégorie | Exemples |
|-----------|---------|
| **Authentification** | Intégration SSO, mise en œuvre AMF, identité fédérée |
| **Autorisation** | Mise en œuvre RBAC, accès basé sur les attributs, autorisation API |
| **Protection des données** | Chiffrement au repos, chiffrement en transit, tokenisation |
| **Sécurité réseau** | Architecture DMZ, micro-segmentation, passerelle API |
| **Intégration** | Modèles API sécurisés, sécurité des files de messages, maillage de services |
| **Cloud** | Architecture de zone d'atterrissage (landing zone), isolation des charges de travail, sécurité cloud-native |

**Exigences minimales du catalogue de modèles** :

Le catalogue DOIT inclure au minimum :

- **Modèles d'authentification** : Intégration SSO (SAML/OIDC), mise en œuvre AMF, gestion des clés API
- **Modèles d'autorisation** : RBAC avec moindre privilège, accès basé sur les attributs pour les données sensibles
- **Modèles de protection des données** : Chiffrement au repos (AES-256), chiffrement en transit (TLS 1.3), tokenisation pour les DCP
- **Modèles de sécurité réseau** : Architecture DMZ, micro-segmentation, passerelle API avec WAF
- **Modèles cloud** : Architecture de zone d'atterrissage (par fournisseur cloud), isolation des charges de travail, intégration CSPM

**Gouvernance des modèles** :

- Les modèles DOIVENT être documentés avec leur justification sécurité
- Les modèles DOIVENT être révisés annuellement
- Les dérogations aux modèles approuvés nécessitent l'approbation de l'Architecte de sécurité
- Les nouveaux modèles DOIVENT être validés par modélisation des menaces avant approbation

### Systèmes tiers et acquis

Les principes d'architecture sécurisée DOIVENT s'appliquer aux systèmes développés par des tiers et aux systèmes acquis.

**Exigences d'acquisition** :

- Documentation de l'architecture de sécurité requise avant approbation des achats
- Évaluation de la sécurité des fournisseurs conformément à ISMS-POL-A.5.19-23
- Compatibilité de l'architecture avec les normes de sécurité de [Organisation]
- Revue de sécurité de l'intégration avant déploiement

**Vérification de la conformité des tiers** :

- **Pré-acquisition** : Évaluation de la sécurité des fournisseurs (documentation de l'architecture révisée)
- **Exigences contractuelles** : Les principes ISS DOIVENT être incorporés dans les contrats de développement
- **Revue au jalon de conception** : L'Architecte de sécurité DOIT réviser la documentation d'architecture lors de la phase de conception
- **Tests pré-acceptation** : Résultats des tests de sécurité requis avant acceptation du système
- **Surveillance continue** : Réévaluation annuelle de l'architecture pour les services SaaS/gérés

## Intégration dans le processus d'ingénierie

### Intégration dans le cycle de vie système

Les principes ISS DOIVENT être intégrés dans chaque phase du cycle de vie système :

| Phase | Activités ISS | Rôle responsable | Jalon/Porte |
|-------|--------------|-----------------|------------|
| **Concept** | Objectifs de sécurité, contexte des menaces, tolérance au risque, exigences de conformité | Propriétaire du système + Architecte de sécurité | Approbation du concept |
| **Développement** | Architecture de sécurité, modélisation des menaces, conception sécurisée, tests de sécurité | Architecte de sécurité + Équipe de développement | Gel de la conception |
| **Production** | Configuration de sécurité, durcissement, tests d'intrusion, approbation de sécurité | Équipe sécurité + Opérations | Approbation pré-production |
| **Utilisation** | Surveillance de sécurité, gestion des vulnérabilités, réponse aux incidents | Propriétaire du système + Opérations de sécurité | Révision trimestrielle |
| **Support** | Correctifs de sécurité, gestion de la configuration, revues d'accès | Propriétaire du système + Opérations | Mensuel/Trimestriel |
| **Retrait** | Assainissement des données, décommissionnement sécurisé, révocation des accès | Propriétaire du système + Équipe sécurité | Approbation du décommissionnement |

---

# Rôles et responsabilités

| Rôle | Responsabilités |
|------|----------------|
| **Direction générale** | Approuver la politique ISS ; allouer les ressources ; accepter les risques architecturaux résiduels |
| **RSSI** | Propriétaire de la politique ; normes ISS ; acceptation des risques d'architecture ; approbation des exceptions |
| **Directeur de la Technologie (DT)** | Gouvernance de l'architecture technique ; approbation des modèles ; normes technologiques |
| **Architecte de sécurité** | Développement des normes ISS ; revues d'architecture ; catalogue de modèles ; modélisation des menaces |
| **Architecte d'entreprise** | Intégration de la sécurité dans l'architecture d'entreprise ; alignement des modèles |
| **Propriétaires de systèmes** | Conformité ISS pour les systèmes détenus ; documentation d'architecture ; responsabilité des risques |
| **Équipes de développement** | Mise en œuvre des principes ISS ; conception sécurisée ; participation à la modélisation des menaces |
| **Fournisseurs tiers** | Conformité aux exigences ISS contractuelles |

**Exigences de formation ISS** :

| Rôle | Formation | Fréquence | Preuve |
|------|-----------|-----------|--------|
| Architectes de sécurité | Certification en modélisation des menaces (par ex. praticien STRIDE) | Initial + actualisation tous les 3 ans | Certificat + travaux de modélisation des menaces |
| Architectes systèmes | Vue d'ensemble des principes ISS, formation sur le catalogue de modèles | Initial + actualisation annuelle | Dossier de complétion de formation |
| Développeurs | Fondamentaux de la conception sécurisée (aligné avec ISMS-POL-A.8.28) | Initial + actualisation annuelle | Complétion de formation + évaluations |

---

# Gouvernance et conformité

## Cadre d'évaluation

[Organisation] DOIT vérifier la mise en œuvre ISS par :

| Évaluation | Fréquence | Responsable | Preuves |
|-----------|-----------|------------|---------|
| Revues d'architecture de sécurité | Par jalon de projet | Architecte de sécurité | Rapports de revue, modèles de menaces |
| Audit de conformité aux modèles | Annuel | Équipe sécurité | Analyse d'utilisation des modèles |
| Évaluation de la maturité Zéro Confiance | Annuel | RSSI | Tableau de bord de maturité |
| Validation de la défense en profondeur | Semestriel | Équipe sécurité | Analyse des couches de contrôle |
| Revue d'architecture tiers | Par acquisition/mission | Architecte de sécurité | Évaluations des fournisseurs |

**Méthodologie d'évaluation de la maturité Zéro Confiance** :

[Organisation] DOIT utiliser le **Modèle de maturité Zéro Confiance CISA v2.0** pour évaluer la maturité de mise en œuvre du Zéro Confiance.

**Cinq piliers évalués annuellement** : Identité, Appareils, Réseaux, Applications et Charges de travail, Données.

**Niveaux de maturité** (selon le modèle CISA) :

- **Traditionnel** (Niveau 0) : Sécurité basée sur le périmètre
- **Initial** (Niveau 1) : Principes Zéro Confiance reconnus
- **Avancé** (Niveau 2) : Zéro Confiance partiellement mis en œuvre
- **Optimal** (Niveau 3) : Zéro Confiance entièrement mis en œuvre et optimisé

**Maturité cible** : [Organisation] vise une maturité de **Niveau Avancé (2)** sur tous les piliers dans les 24 mois suivant l'approbation de la politique.

**Métriques de gouvernance (tableau de bord trimestriel)** :

| Métrique | Cible | Mesure |
|---------|-------|--------|
| % de nouveaux systèmes avec revue d'architecture complétée | 100 % | Nombre de systèmes avec revue approuvée / Total nouveaux systèmes |
| Délai moyen de conception à approbation d'architecture | ≤ 15 jours ouvrables | Délai moyen de la demande de revue à l'approbation du RSSI |
| Nombre d'exceptions d'architecture actives | ≤ 5 à tout moment | Nombre d'exceptions ouvertes dans le registre |
| Score de maturité de mise en œuvre Zéro Confiance | ≥ Niveau 2 (Avancé) sur tous les piliers | Évaluation annuelle du modèle de maturité ZC CISA |
| Taux d'adoption des modèles pour les nouveaux systèmes | ≥ 80 % | Systèmes utilisant des modèles approuvés / Total des systèmes révisés |

## Gestion des exceptions

Les exceptions à la politique d'architecture nécessitent :

- Justification métier documentée
- Évaluation des risques de l'impact de la dérogation
- Spécification des contrôles compensatoires
- Recommandation de l'Architecte de sécurité
- Approbation du RSSI
- Approbation limitée dans le temps (maximum 12 mois pour les exceptions d'architecture)
- Révision trimestrielle pour évaluer la nécessité persistante

**Non permissible** :

- Exceptions permanentes aux principes ISS fondamentaux
- Exceptions éliminant la défense en profondeur
- Systèmes sans revue d'architecture de sécurité

---

# Définitions

| Terme | Définition |
|-------|------------|
| **Ingénierie des Systèmes Sécurisés (ISS)** | Discipline intégrant les considérations de sécurité dans toutes les phases du cycle de vie système pour produire des systèmes sécurisés de confiance |
| **Sécurité par conception** | Principe selon lequel la sécurité est intégrée dans les systèmes dès leur conception plutôt qu'ajoutée après le développement |
| **Sécurité par défaut** | Principe selon lequel les systèmes sont configurés de manière sécurisée prêts à l'emploi sans nécessiter d'action de l'utilisateur |
| **Défense en profondeur** | Approche de sécurité en couches où plusieurs contrôles protègent les actifs |
| **Zéro Confiance** | Modèle de sécurité basé sur « ne jamais faire confiance, toujours vérifier » |
| **Modèle de menaces** | Analyse structurée des menaces potentielles, des vecteurs d'attaque et des contre-mesures pour un système |
| **Architecture de sécurité** | Artefacts de conception décrivant comment les contrôles de sécurité sont positionnés et comment ils se rapportent à l'architecture système globale |
| **Surface d'attaque** | Somme de tous les points où un attaquant pourrait potentiellement entrer dans un système ou en extraire des données |

---

# Preuves pour cette politique

**Preuves de l'Étape 1 (Revue de la documentation) :**

- ✅ Ce document de politique (ISMS-POL-A.8.27 v1.0)
- ✅ Signatures d'approbation du RSSI, DT, Direction générale
- ✅ Principes ISS fondamentaux documentés
- ✅ Principes Zéro Confiance définis
- ✅ Exigences de défense en profondeur spécifiées
- ✅ Exigences de revue d'architecture documentées
- ✅ Modèles d'architecture sécurisée référencés
- ✅ Exigences d'intégration dans le cycle de vie définies
- ✅ Rôles et responsabilités attribués

---

# Enregistrement d'approbation

| Rôle | Nom | Date |
|------|-----|------|
| **Responsable de la Sécurité des Systèmes d'Information (RSSI)** | [Nom] | [Date à définir] |
| **Directeur de la Technologie (DT)** | [Nom] | [Date à définir] |
| **Direction générale** | [Nom] | [Date à définir] |

---

**FIN DU DOCUMENT DE POLITIQUE**

---

*Cette politique établit les exigences fondamentales de [Organisation] pour l'Ingénierie des Systèmes Sécurisés. Les procédures de mise en œuvre sont documentées dans ISMS-IMP-A.8.27 (UG/TG).*

<!-- QA_VERIFIED: 2026-04-02 -->
