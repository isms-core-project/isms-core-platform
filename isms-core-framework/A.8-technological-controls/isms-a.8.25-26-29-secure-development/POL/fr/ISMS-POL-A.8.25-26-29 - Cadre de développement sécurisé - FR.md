<!-- ISMS-CORE:POLICY:ISMS-POL-A.8.25-26-29-FR:framework:POL:a.8.25-26-29 -->
**ISMS-POL-A.8.25-26-29 – Cadre de développement sécurisé**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Cadre de développement sécurisé |
| **Type de document** | Politique |
| **Identifiant du document** | ISMS-POL-A.8.25-26-29 |
| **Créateur du document** | Responsable de la Sécurité des Systèmes d'Information (RSSI) |
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
| 1.0 | [Date] | RSSI / Responsable de la sécurité applicative | Cadre de développement sécurisé initial consolidé |

**Cycle de révision** : Annuel (ou lors de changements significatifs de méthodologie SDLC, mises à jour réglementaires ou incidents de sécurité majeurs)

---

# Résumé exécutif

Cette politique établit le Cadre de développement sécurisé de [Organisation], mettant en œuvre les Contrôles ISO/IEC 27001:2022 A.8.26 (Exigences de sécurité des applications), A.8.25 (Cycle de vie du développement sécurisé) et A.8.29 (Tests de sécurité dans le développement et l'acceptation) sous forme de cadre de sécurité unifié.

**Objet** : Définir les exigences organisationnelles pour le développement logiciel sécurisé tout au long du cycle de vie de développement logiciel (SDLC). Cette politique établit QUELLES pratiques de sécurité sont requises, QUAND elles doivent être appliquées et QUI en est responsable. Les procédures de mise en œuvre (COMMENT) sont documentées séparément dans ISMS-IMP-A.8.25-26-29 (variantes UG/TG).

**Alignement réglementaire** : Cette politique traite des exigences de conformité obligatoires conformément à ISMS-POL-00, notamment la nLPD suisse (protection des données dès la conception), le RGPD de l'UE Article 25 (protection des données dès la conception et par défaut) et la norme ISO/IEC 27001:2022.

---

# Périmètre

## Dans le périmètre

**Applications** :

- Toutes les applications développées en interne (web, mobile, desktop, embarquées, API)
- Applications acquises nécessitant une personnalisation ou intégration
- Infrastructure-as-Code (IaC) et code de gestion de la configuration

**Activités de développement** :

- Développement de nouvelles applications
- Améliorations d'applications et correctifs de sécurité
- Modernisation des applications et migration cloud

**Modèles de développement** :

- Équipes de développement internes
- Développement externalisé (contractants, équipes offshore)
- Modèles de développement hybrides

**Méthodologies SDLC** :

- Cascade, Agile/Scrum, DevOps/DevSecOps
- Livraison continue et déploiement continu (CI/CD)

## Hors périmètre

- Logiciels commerciaux sur étagère (COTS) sans personnalisation (couverts par l'évaluation de sécurité des fournisseurs)
- Gestion des vulnérabilités en production post-déploiement (couverte par ISMS-POL-A.8.8)
- Surveillance de sécurité opérationnelle (couverte par ISMS-POL-A.8.15-16)

---

# Énoncés des contrôles ISO/IEC 27001:2022

**A.8.26 — Exigences de sécurité des applications**

> *Les exigences de sécurité de l'information doivent être identifiées, spécifiées et approuvées lors du développement ou de l'acquisition d'applications.*

**A.8.25 — Cycle de vie du développement sécurisé**

> *Des règles pour le développement sécurisé de logiciels et systèmes doivent être établies et appliquées.*

**A.8.29 — Tests de sécurité dans le développement et l'acceptation**

> *Des processus de test de sécurité doivent être définis et mis en œuvre dans le cycle de vie du développement.*

---

# Exigences de sécurité des applications (A.8.26)

## Identification des exigences de sécurité

[Organisation] DOIT identifier et documenter les exigences de sécurité pour toutes les applications avant ou au début du développement.

**Catégories d'exigences de sécurité** :

- **Authentification et contrôle d'accès** : Mécanismes d'authentification requis, RBAC, gestion des sessions
- **Protection des données** : Classification des données traitées, exigences de chiffrement, masquage
- **Journalisation et audit** : Événements à journaliser, durée de conservation, intégrité des journaux
- **Conformité réglementaire** : Exigences RGPD/nLPD applicables, PCI DSS (si applicable), FINMA (si applicable)
- **Disponibilité et résilience** : RTO, RPO, mécanismes de basculement
- **Intégrations sécurisées** : Exigences de sécurité des API, gestion des secrets

**Sources d'exigences de sécurité** :

- Modélisation des menaces (threat modeling) — STRIDE ou équivalent
- Cadres de référence sectoriels (OWASP, NIST, CIS)
- Exigences réglementaires applicables (RGPD Art. 25, nLPD)
- Classification des données traitées par l'application
- Résultats des tests de pénétration d'applications similaires

**Documentation obligatoire** :

- Spécification des exigences de sécurité documentées et approuvées avant le début du développement
- Validation par le RSSI ou le Responsable de la sécurité applicative pour les applications traitant des données Confidentielles/Restreintes
- Traçabilité entre exigences de sécurité et cas de tests de sécurité

---

# Cycle de vie du développement sécurisé (A.8.25)

## Principes fondamentaux du SDL

[Organisation] DOIT intégrer la sécurité à chaque phase du SDLC selon les principes suivants :

- **Shift-Left** : Intégrer la sécurité le plus tôt possible dans le cycle de développement
- **Protection des données dès la conception** : Intégrer la confidentialité et la sécurité dans l'architecture dès le début (conformément au RGPD Art. 25 et à la nLPD)
- **Moindre privilège** : Les applications et leurs composants ne doivent demander que les permissions strictement nécessaires
- **Défense en profondeur** : Superposer plusieurs contrôles de sécurité indépendants
- **Sécurité par défaut** : Les paramètres par défaut doivent être les plus sécurisés

## Exigences par phase du SDLC

**Phase de planification et d'exigences** :

- ✅ Identification et documentation des exigences de sécurité (A.8.26)
- ✅ Classification des données traitées par l'application
- ✅ Évaluation préliminaire des risques de sécurité

**Phase de conception** :

- ✅ Revue d'architecture de sécurité par le RSSI ou l'Architecte de sécurité (pour les applications critiques)
- ✅ Modélisation des menaces (STRIDE ou équivalent) pour les nouvelles applications et les changements significatifs
- ✅ Définition des contrôles de sécurité à mettre en œuvre

**Phase de développement** :

- ✅ Application des règles de codage sécurisé (conformément à ISMS-POL-A.8.28)
- ✅ Utilisation de bibliothèques et composants approuvés et à jour
- ✅ Aucun secret (mots de passe, clés API, jetons) dans le code source ou les référentiels
- ✅ Révisions de code avec contrôles de sécurité (conformément à A.8.29)

**Phase de test** :

- ✅ Tests de sécurité automatisés dans les pipelines CI/CD (SAST, DAST, SCA — conformément à A.8.29)
- ✅ Tests de sécurité manuels pour les fonctionnalités à haut risque
- ✅ Tests d'acceptation de sécurité (SAT) avant déploiement en production

**Phase de déploiement** :

- ✅ Processus de déploiement sécurisé (pipelines CI/CD signés, artefacts vérifiés)
- ✅ Gestion des changements (conformément à ISMS-POL-A.8.32)
- ✅ Séparation des environnements (conformément à ISMS-POL-A.8.31)

**Phase d'exploitation et de maintenance** :

- ✅ Gestion des correctifs de sécurité (conformément à ISMS-POL-A.8.8)
- ✅ Surveillance et journalisation des applications (conformément à ISMS-POL-A.8.15-16)
- ✅ Gestion des incidents de sécurité applicatifs (conformément à ISMS-POL-A.5.24)

---

# Tests de sécurité dans le développement et l'acceptation (A.8.29)

## Types de tests de sécurité obligatoires

**Analyse statique de la sécurité des applications (SAST)** :

- Les outils SAST DOIVENT être intégrés dans les pipelines CI/CD pour toutes les applications développées en interne
- Analyse du code source pour détecter les vulnérabilités (injection SQL, XSS, buffer overflow, etc.)
- Les résultats de gravité Critique et Élevée DOIVENT être corrigés avant le déploiement en production
- Les résultats de gravité Moyenne DOIVENT avoir un plan de remédiation documenté

**Analyse de la composition des logiciels (SCA)** :

- Les outils SCA DOIVENT analyser les dépendances et composants tiers pour les vulnérabilités connues (CVE)
- Les licences des composants tiers DOIVENT être vérifiées pour la conformité
- Les composants avec des vulnérabilités Critiques ou Élevées DOIVENT être mis à jour ou remplacés avant le déploiement
- Un inventaire des composants tiers (SBOM — Software Bill of Materials) DOIT être maintenu

**Analyse dynamique de la sécurité des applications (DAST)** :

- Les outils DAST DOIVENT analyser les applications web déployées dans les environnements de préproduction
- Tests des vulnérabilités OWASP Top 10 minimum (injection, mauvaise authentification, exposition des données, etc.)
- Effectués avant chaque déploiement majeur en production

**Tests de pénétration** :

- Tests de pénétration annuels DOIVENT être effectués sur les applications web exposées à Internet
- Tests de pénétration DOIVENT être effectués par des testeurs qualifiés (internes ou tiers)
- Les résultats DOIVENT être documentés et les vulnérabilités Critiques/Élevées remédiées dans les délais définis (conformément à A.8.8)
- Tests de pénétration supplémentaires requis lors de changements architecturaux majeurs

## Critères d'acceptation de sécurité

**Aucune application ne DOIT être déployée en production si** :

- Des vulnérabilités SAST ou DAST de gravité Critique non résolues subsistent
- Des composants avec des CVE Critiques non corrigées subsistent
- Des secrets sont détectés dans le code source
- Les tests de sécurité requis n'ont pas été effectués

**Processus de dérogation** :

- Les exceptions aux critères d'acceptation DOIVENT être approuvées par le RSSI
- Les exceptions DOIVENT inclure : justification, délai de remédiation, contrôles compensatoires
- Toutes les exceptions DOIVENT être documentées

---

# Formation en développement sécurisé

[Organisation] DOIT fournir une formation en développement sécurisé :

- **Formation initiale** : Tous les développeurs DOIVENT recevoir une formation de base en développement sécurisé lors de l'intégration
- **Formation continue** : Formation annuelle de remise à niveau en sécurité pour tous les développeurs
- **Formation spécialisée** : Formation spécifique au langage/framework pour les développeurs exposés à des risques particuliers
- **Sensibilisation OWASP** : Formation sur les vulnérabilités OWASP Top 10 Web et API Security Top 10

---

# Rôles et responsabilités

| Rôle | Responsabilités |
|------|----------------|
| **RSSI** | Propriétaire de la politique ; approbation des exceptions ; supervision de la conformité |
| **Responsable de la sécurité applicative** | Mise en œuvre du programme ; revues d'architecture ; coordination des tests |
| **Architecte de sécurité** | Revues d'architecture de sécurité ; modélisation des menaces |
| **Responsables des équipes de développement** | Application des exigences SDLC dans leurs équipes ; formation |
| **Développeurs** | Mise en œuvre des pratiques de codage sécurisé ; participation aux revues de code |
| **Équipe DevOps/CI-CD** | Intégration et maintenance des outils de sécurité dans les pipelines |

---

# Enregistrement d'approbation

| Rôle | Nom | Date |
|------|-----|------|
| **Responsable de la Sécurité des Systèmes d'Information (RSSI)** | [Nom] | [Date] |
| **Directeur de la Technologie (DT)** | [Nom] | [Date] |
| **Responsable juridique/conformité** | [Nom] | [Date] |
| **Direction générale** | [Nom] | [Date] |

---

**FIN DU DOCUMENT DE POLITIQUE**

---

*Cette politique établit le cadre de développement sécurisé. Les procédures de mise en œuvre sont documentées dans ISMS-IMP-A.8.25-26-29 (UG/TG).*

<!-- QA_VERIFIED: 2026-04-02 -->
