<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.8.25-26-29-FR:operational:OP-POL:a.8.25-26-29 -->
**ISMS-OP-POL-A.8.25-26-29 — Cycle de développement sécurisé**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Cycle de développement sécurisé |
| **Type de document** | Politique opérationnelle |
| **Identifiant du document** | ISMS-OP-POL-A.8.25-26-29 |
| **Créateur du document** | Responsable de la sécurité de l'information (RSSI) |
| **Propriétaire du document** | Directeur général (PDG) |
| **Approuvé par** | Direction générale |
| **Date de création** | [Date] |
| **Version** | 1.0 |
| **Date de version** | [À déterminer] |
| **Classification** | Interne |
| **Statut** | Brouillon |

**Historique des versions** :

| Version | Date | Auteur | Modifications |
|---------|------|--------|---------------|
| 1.0 | [Date] | RSSI | Politique opérationnelle initiale pour ISO 27001:2022 |

**Cycle de révision** : Annuel
**Prochaine date de révision** : [Date d'entrée en vigueur + 12 mois]

**Approuvé par** : [RSSI / Direction générale]

**Documents associés** :

- ISO/IEC 27001:2022 Contrôle A.8.25 — Cycle de développement sécurisé
- ISO/IEC 27001:2022 Contrôle A.8.26 — Exigences de sécurité des applications
- ISO/IEC 27001:2022 Contrôle A.8.29 — Tests de sécurité dans le développement et l'acceptation
- OWASP Application Security Verification Standard (ASVS) 4.0
- OWASP Top 10:2025
- NIST SP 800-218 — Secure Software Development Framework (SSDF) v1.1

**Contrôles Annexe A associés** :

| Contrôle | Relation avec le développement sécurisé |
|----------|-----------------------------------------|
| A.5.8 Sécurité de l'information dans la gestion de projets | Exigences de sécurité intégrées dans le cycle de vie du projet |
| A.5.15–16–18 Gestion des identités et des accès | Contrôle d'accès aux référentiels, environnements et outils de déploiement |
| A.8.4 Accès au code source | Restriction et protection de l'accès au code source |
| A.8.8 Gestion des vulnérabilités techniques | Remédiation des vulnérabilités des applications déployées |
| A.8.28 Codage sécurisé | Normes et pratiques de codage sécurisé |
| A.8.31 Séparation des environnements de développement, de test et de production | Exigences de cloisonnement des environnements |
| A.8.32 Gestion des changements | Contrôle des changements pour la promotion et le déploiement du code |
| A.8.33 Informations de test | Protection des données de test |

**Politiques internes associées** :

- Politique de contrôle d'accès
- Politique de gestion des vulnérabilités
- Politique de gestion des changements
- Politique de classification et de traitement de l'information
- Politique de sécurité des postes de travail

---

# Politique relative au cycle de développement sécurisé

## Objet

La présente politique a pour objet de garantir que la sécurité de l'information est conçue et mise en œuvre tout au long du cycle de développement des logiciels et des systèmes, que les exigences de sécurité sont identifiées et spécifiées lors du développement ou de l'acquisition d'applications, et que les tests de sécurité sont définis et réalisés avant tout déploiement en production.

Cette politique soutient la nLPD (revDSG) suisse en mettant en œuvre des mesures techniques et organisationnelles proportionnées aux risques pour protéger les données personnelles, conformément à l'art. 7 (protection des données dès la conception et par défaut) et à l'art. 8 (mesures techniques et organisationnelles de sécurité). Lorsque l'organisation traite des données de personnes dans l'UE/EEE, les exigences du RGPD s'appliquent également (art. 25 — protection des données dès la conception et par défaut ; art. 32 — sécurité du traitement).

## Champ d'application

Le développement de solutions logicielles sur mesure de l'organisation, y compris les applications web, les API, les applications mobiles et l'infrastructure en tant que code.

Toutes les activités de développement internes et externalisées relevant du périmètre de l'ISO 27001.

Tous les employés et utilisateurs tiers impliqués dans le développement, les tests et le déploiement de logiciels.

## Principe

Des principes et des normes d'ingénierie de logiciels et de systèmes sécurisés sont mis en œuvre et testés tout au long du cycle de développement logiciel.

La sécurité de l'information et la protection de la vie privée sont intégrées dès la conception et par défaut, conformément aux groupes de pratiques du NIST SP 800-218 (SSDF) : Préparer l'organisation (PO), Protéger le logiciel (PS), Produire des logiciels bien sécurisés (PW) et Répondre aux vulnérabilités (RV).

Les contrôles de sécurité sont appliqués proportionnellement au risque applicatif, les applications à risque élevé étant soumises à des exigences plus rigoureuses.

---

## Outillage de sécurité du développement

L'organisation doit maintenir une chaîne d'outils de sécurité approuvée, intégrée dans le cycle de développement.

**Chaîne d'outils de sécurité approuvée** :

| Catégorie | Objet | Responsable | Point d'intégration |
|-----------|-------|-------------|---------------------|
| **Référentiel de code source** | Gestion des versions, protection des branches, contrôle d'accès | DevOps / Équipe plateforme | Phase de développement |
| **SAST** (Analyse statique de la sécurité applicative) | Détection des vulnérabilités dans le code source (ex. SonarQube, Semgrep, Checkmarx ou équivalent) | DevOps / Responsable développement | Pipeline CI/CD — phase de compilation |
| **SCA** (Analyse de la composition logicielle) | Détection des vulnérabilités dans les dépendances open source (ex. Snyk, OWASP Dependency-Check ou équivalent) | DevOps / Responsable développement | Pipeline CI/CD — phase de compilation |
| **DAST** (Analyse dynamique de la sécurité applicative) | Détection des vulnérabilités à l'exécution (ex. OWASP ZAP, Burp Suite ou équivalent) | AQ / Équipe sécurité | Phase pré-déploiement |
| **Analyse des secrets** | Détection des identifiants, clés API, jetons dans le code (ex. GitLeaks, TruffleHog ou équivalent) | DevOps / Équipe plateforme | Hook pré-commit + pipeline CI/CD |
| **Base de données de dépendances** | Renseignement sur les vulnérabilités des composants tiers (ex. NVD, OSV, GitHub Advisory Database) | Responsable développement | Surveillance continue |
| **Générateur SBOM** | Génération du catalogue de composants logiciels (ex. Syft, CycloneDX CLI ou équivalent) | DevOps / Équipe plateforme | Pipeline CI/CD — phase de compilation |
| **Plateforme de revue de code** | Revue par les pairs, processus d'approbation, piste d'audit (ex. GitHub, GitLab, Bitbucket ou équivalent) | Responsable développement | Phase pré-fusion |
| **Tests d'intrusion** | Évaluation manuelle de la sécurité par des spécialistes externes qualifiés | RSSI | Pré-lancement (risque élevé) / périodique |

La chaîne d'outils est révisée annuellement par le responsable développement et le RSSI. Tout changement d'outil doit suivre le processus de gestion des changements. Tous les outils doivent être maintenus à leur version supportée la plus récente.

---

## Cloisonnement des environnements

Les environnements de développement, de test et de production sont séparés et ne partagent pas de composants communs, de bases de données ou d'espaces de stockage.

Les environnements de développement, de test et de production sont placés sur des réseaux ou des segments réseau distincts.

Les responsabilités administratives entre les environnements de développement/test et de production sont séparées. Le personnel disposant d'un accès en écriture aux référentiels de développement ne doit pas avoir d'accès administratif direct aux systèmes de production sans autorisation distincte.

Les données ne doivent pas circuler de la production vers les environnements de développement ou de test sans approbation explicite et assainissement approprié (voir la section Gestion des données de test).

La configuration du cloisonnement des environnements est documentée et sa conformité est vérifiée au moins une fois par an.

---

## Classification des risques applicatifs

Toutes les applications sont classées par niveau de risque afin de déterminer les exigences de sécurité appropriées.

**Critères de classification des risques** :

| Niveau de risque | Critères |
|------------------|----------|
| **Risque élevé** | Répond à L'UN des critères suivants : traite des données Confidentielles ou Restreintes ; traite des DCP soumises à la nLPD/RGPD ; accessible depuis Internet ou par des parties externes ; fonction métier critique ou traitement de transactions financières ; données de cartes de paiement (si périmètre PCI DSS applicable) |
| **Risque moyen** | Répond à L'UN des critères suivants : traite des données à usage interne ; exposition limitée aux DCP (noms et adresses électroniques uniquement) ; accès interne uniquement ; fonction métier importante mais non critique |
| **Risque faible** | Répond à TOUS les critères suivants : traite uniquement des données publiques ; aucune DCP, aucune donnée métier sensible ; fonction métier non critique |

Les classifications des risques applicatifs sont révisées annuellement par le responsable développement et le RSSI.

**Déclencheurs de reclassification** (en complément de la révision annuelle) :

| Événement déclencheur | Action |
|-----------------------|--------|
| Nouveau type de données traité (ex. DCP, données financières, données de santé) | Reclassifier sous 14 jours |
| Changement d'exposition réseau (interne → accessible depuis Internet) | Reclassifier avant déploiement |
| Changement d'architecture significatif (nouvelle API, nouvelle intégration) | Reclassifier à la phase de conception |
| Changement réglementaire affectant l'application | Reclassifier sous 30 jours |
| Incident de sécurité impliquant l'application | Reclassifier sous 14 jours après clôture de l'incident |
| Acquisition ou fusion affectant le périmètre de l'application | Reclassifier sous 60 jours |

**Processus de reclassification** : (1) Le propriétaire de l'application soumet une demande de changement motivée → (2) Le responsable développement évalue selon les critères de classification → (3) Le RSSI approuve si la classification augmente → (4) Les exigences de sécurité mises à jour sont appliquées sous 60 jours si la classification augmente → (5) La classification mise à jour est enregistrée dans le registre.

La classification est consignée dans le registre de classification des risques applicatifs.

---

## Exigences de sécurité

Des exigences de sécurité sont spécifiées pour toutes les applications en fonction de leur niveau de risque.

**Exigences obligatoires par niveau de risque** :

| Exigence | Risque élevé | Risque moyen | Risque faible |
|----------|-------------|-------------|--------------|
| Spécification des exigences de sécurité | Obligatoire | Obligatoire | Liste de contrôle de base |
| Modélisation des menaces (ex. STRIDE, PASTA, arbres d'attaque) | Obligatoire | Recommandé | Optionnel |
| Revue de l'architecture de sécurité | Obligatoire | Recommandé | Optionnel |
| Traçabilité des exigences | Obligatoire | Recommandé | Optionnel |

**Processus de modélisation des menaces** :

Lorsque la modélisation des menaces est requise (obligatoire pour les applications à risque élevé, recommandée pour le risque moyen), le processus suivant est appliqué :

| Étape | Activité | Résultat |
|-------|----------|----------|
| 1. **Préparation** | Constituer l'équipe (développeur, architecte, Champion sécurité/RSSI) ; rassembler la documentation système, les diagrammes de flux de données et les schémas d'architecture | Définition du périmètre et dossier de travail |
| 2. **Identification des menaces** | Appliquer la méthodologie STRIDE (Usurpation, Falsification, Répudiation, Divulgation d'informations, Déni de service, Élévation de privilèges) à chaque composant et flux de données | Catalogue des menaces |
| 3. **Évaluation des risques** | Évaluer la probabilité et l'impact de chaque menace identifiée selon les critères de risque de l'organisation | Liste des menaces priorisées |
| 4. **Plan d'atténuation** | Définir les contrôles de sécurité et les exigences pour traiter chaque menace ; associer aux tâches d'implémentation | Plan d'atténuation avec responsables et échéances |
| 5. **Documentation** | Consigner le modèle de menaces dans le format approuvé ; lier aux spécifications des exigences de sécurité | Document de modélisation des menaces complété |

Les modèles de menaces sont révisés et mis à jour : à chaque version majeure ; lors de changements architecturaux significatifs ; lors de l'identification de nouveaux renseignements sur les menaces pertinents pour l'application ; et au moins une fois par an pour les applications à risque élevé.

**Les exigences de sécurité doivent couvrir au minimum les domaines suivants** :

- **Authentification et autorisation** — vérification de l'identité, accès basé sur les rôles, gestion des sessions.
- **Validation des entrées et encodage des sorties** — protection contre les attaques par injection (OWASP Top 10 A05:2025).
- **Cryptographie** — chiffrement des données en transit (TLS 1.2 minimum) et au repos conformément à la Politique d'utilisation de la cryptographie.
- **Gestion des sessions** — jetons de session sécurisés, délais d'expiration, invalidation à la déconnexion.
- **Gestion des erreurs et journalisation** — aucune donnée sensible dans les messages d'erreur ; événements de sécurité journalisés conformément à la Politique de journalisation.
- **Sécurité des API** — authentification, limitation du débit, validation des entrées pour tous les points de terminaison API.
- **Protection des données** — traitement des données personnelles conformément à l'art. 7 nLPD (protection dès la conception et par défaut) ; minimisation des données ; suppression sécurisée.

Pour les applications fournissant des services transactionnels entre l'organisation et des parties externes, des exigences supplémentaires portent sur les niveaux de confiance des identités, l'intégrité des informations échangées, la non-répudiation et la confidentialité des transactions.

**Modèle de spécification des exigences de sécurité** :

Les spécifications des exigences de sécurité suivent un modèle standardisé couvrant les rubriques suivantes :

| N° | Rubrique | Description |
|----|----------|-------------|
| 1 | Présentation de l'application | Nom, objet, classification des risques, classification des données |
| 2 | Diagramme de flux de données | Schéma de contexte système montrant les flux de données, les frontières de confiance et les interfaces externes |
| 3 | Exigences d'authentification | Méthodes d'authentification, exigences AMF, gestion des sessions |
| 4 | Exigences d'autorisation | Modèle de contrôle d'accès (RBAC/ABAC), niveaux de privilèges, séparation des fonctions |
| 5 | Validation des entrées | Règles de validation par type d'entrée, exigences d'encodage, restrictions sur les fichiers téléchargés |
| 6 | Exigences cryptographiques | Normes de chiffrement (conformément à la Politique d'utilisation de la cryptographie), gestion des clés |
| 7 | Sécurité des API | Authentification, limitation du débit, validation des entrées, gestion des versions, traitement des erreurs |
| 8 | Protection des données | Traitement des DCP, minimisation des données, conservation, suppression, conformité art. 7 nLPD |
| 9 | Journalisation et surveillance | Événements de sécurité à journaliser, format des journaux, conservation, seuils d'alerte |
| 10 | Gestion des erreurs | Restrictions sur le contenu des messages d'erreur, comportement de repli, dégradation gracieuse |
| 11 | Intégrations tierces | Évaluation de la confiance, partage des données, sécurité des API, exigences SLA |
| 12 | Exigences de conformité | Exigences réglementaires (nLPD, RGPD si applicable), normes sectorielles |
| 13 | Synthèse de la modélisation des menaces | Principales menaces identifiées, atténuations requises (pour les applications à risque élevé) |
| 14 | Plan de tests de sécurité | Types de tests requis, périmètre, calendrier, critères d'acceptation |

Les exigences de sécurité sont approuvées par le RSSI (risque élevé) ou le responsable développement (risque moyen/faible) avant le début du développement.

---

## Directives de codage sécurisé

Les logiciels sont conçus et développés sur la base de directives de codage sécurisé reconnues par l'industrie, notamment :

- **OWASP** — OWASP Top 10:2025, OWASP Application Security Verification Standard (ASVS) et OWASP Secure Coding Practices.
- **NIST SP 800-218 (SSDF)** — Secure Software Development Framework pour réduire le risque de vulnérabilités logicielles.
- **CWE/SANS Top 25** — Les faiblesses logicielles les plus dangereuses, couvrant les catégories telles que l'injection, la corruption de mémoire et les défaillances d'authentification.

Des normes de codage sécurisé spécifiques aux langages sont documentées et maintenues pour chaque langage de programmation utilisé. Elles couvrent au minimum :

- Les fonctions interdites et les schémas non sécurisés.
- Les techniques de validation des entrées et d'encodage des sorties requises.
- Les bibliothèques cryptographiques approuvées et leurs modes d'utilisation.
- Les pratiques sécurisées de gestion des erreurs et de journalisation.
- La gestion des dépendances et la fixation des versions.

**Exemple — Norme de codage sécurisé Python** (à titre illustratif ; chaque langage dispose d'une documentation équivalente) :

| Catégorie | Exigence |
|-----------|----------|
| **Fonctions interdites** | `eval()`, `exec()`, `pickle.loads()` sur des données non fiables, `os.system()` (utiliser `subprocess.run()` avec shell=False), `yaml.load()` sans SafeLoader |
| **Pratiques requises** | Requêtes paramétrées (pas de concaténation de chaînes pour le SQL), module `secrets` pour la génération aléatoire (pas `random`), annotations de type pour les fonctions critiques de sécurité, validation des entrées par listes d'autorisation |
| **Bibliothèques crypto approuvées** | Bibliothèque `cryptography` (préférée), `hashlib` (hachage uniquement) ; interdites : `pycrypto` (non maintenu), implémentations cryptographiques personnalisées |
| **Gestion des erreurs** | Aucune donnée sensible dans les messages d'exception ; utiliser la journalisation structurée ; intercepter des exceptions spécifiques (pas de `except:` nu) |
| **Dépendances** | Fixer les versions dans `requirements.txt` ou `pyproject.toml` ; examiner les journaux de modifications avant les mises à jour majeures ; aucune dépendance avec des CVE critiques connus |

Les normes spécifiques aux langages sont stockées dans le référentiel de code (ex. `docs/secure-coding/` ou équivalent), révisées annuellement et mises à jour lors de l'émergence de nouvelles vulnérabilités ou pratiques.

Tous les développeurs suivent une formation au codage sécurisé avant de se voir accorder l'accès au code de production (voir la section Formation à la sécurité des développeurs).

---

## Référentiels de code et gestion des versions

Le code de développement est stocké dans un référentiel de code sécurisé qui applique les exigences de la Politique de contrôle d'accès et la séparation des fonctions.

L'accès aux référentiels respecte le principe du moindre privilège :

- L'accès est accordé en fonction de l'affectation au projet et du rôle.
- L'accès aux référentiels est révisé au moins une fois par an, dans le cadre des révisions de la gestion des identités et des accès.
- L'accès des membres ayant quitté l'équipe est révoqué le jour ouvré suivant le départ.

Les référentiels de code appliquent :

- **La gestion des versions** avec archivage et stratégie de branches appropriés.
- **La protection des branches** sur les branches principale/production — les commits directs sont interdits ; les changements nécessitent une demande de fusion approuvée.
- **La signature des commits** recommandée pour les applications à risque élevé.
- **L'analyse des secrets** pour prévenir la validation accidentelle d'identifiants, de clés API ou de jetons.

**Analyse et gestion des secrets** :

L'analyse des secrets détecte au minimum : les clés API, les jetons d'accès, les clés privées, les chaînes de connexion aux bases de données, les identifiants de fournisseurs cloud et les URL de webhooks.

**Processus de remédiation en cas de secret détecté** :

| Étape | Action | Délai |
|-------|--------|-------|
| 1 | **Bloquer le commit** (hook pré-commit) ou signaler dans le pipeline CI/CD | Immédiat |
| 2 | **Révoquer et renouveler** l'identifiant exposé | Sous 4 heures pour les secrets de production ; sous 24 heures pour les environnements hors production |
| 3 | **Supprimer de l'historique du référentiel** (si validé) à l'aide d'outils approuvés (ex. git filter-branch, BFG Repo-Cleaner) | Sous 24 heures |
| 4 | **Analyser l'exposition** — déterminer si le secret a été accédé par des parties non autorisées | Sous 48 heures |
| 5 | **Documenter l'incident** — enregistrer dans le journal des incidents ; escalader vers le RSSI si un secret de production a été exposé à des parties externes | Conformément à la politique de gestion des incidents |

**Gestion des secrets approuvée** :

| Environnement | Méthode approuvée |
|---------------|-------------------|
| Développement | Variables d'environnement, fichiers `.env` (exclus du gestionnaire de versions via `.gitignore`) |
| Test | Gestionnaire de secrets ou variables d'environnement chiffrées |
| Production | Gestionnaire de secrets dédié (ex. HashiCorp Vault, AWS Secrets Manager, Azure Key Vault ou équivalent) |
| Pipelines CI/CD | Magasin de secrets du pipeline (ex. GitHub Secrets, GitLab CI/CD Variables ou équivalent) ; aucun secret en dur dans les définitions de pipeline |

Les secrets codés en dur dans le code source sont interdits. Les résultats de l'analyse des secrets sont examinés chaque semaine par le responsable développement.

---

## Revue de code

Tout le code est examiné avant sa mise en production par des personnels qualifiés autres que l'auteur ou le développeur.

Le code est passé en revue par rapport aux directives de codage sécurisé de l'organisation.

Les revues de code emploient des techniques manuelles et automatisées :

- **Revue manuelle par les pairs** — obligatoire pour toutes les modifications de code avant la fusion vers les branches protégées.
- **Revue axée sur la sécurité** — obligatoire pour les applications à risque élevé, réalisée par un Champion sécurité ou un examinateur formé à la sécurité.
- **Revue automatisée** — outils SAST intégrés dans le pipeline CI/CD (ex. SonarQube, Semgrep, Checkmarx ou équivalent).

**Processus de revue de code** :

| Étape | Activité | Responsable |
|-------|----------|-------------|
| 1. **Soumission** | Le développeur crée une demande de fusion avec description, exigences liées et liste de contrôle d'auto-vérification | Développeur |
| 2. **Contrôles automatisés** | Le pipeline CI/CD exécute le SAST, le SCA, l'analyse des secrets, le linting et les tests unitaires | Automatisé (DevOps) |
| 3. **Revue manuelle par les pairs** | L'examinateur vérifie la logique, la lisibilité, la conformité aux normes de codage et la couverture des tests | Pair examinateur |
| 4. **Revue de sécurité** | Revue axée sur la sécurité selon la liste de contrôle de codage sécurisé (risque élevé : obligatoire ; risque moyen : recommandé) | Champion sécurité ou examinateur formé |
| 5. **Approbation et fusion** | Les examinateurs approuvent ; fusion vers la branche protégée | Examinateur(s) / Responsable développement |

**Liste de contrôle de la revue de code sécurisé** (éléments minimum pour une revue axée sur la sécurité) :

1. Validation des entrées appliquée à toutes les entrées externes (saisie utilisateur, paramètres API, fichiers téléchargés)
2. Encodage des sorties appliqué partout où les données sont restituées (HTML, JSON, SQL, LDAP)
3. Contrôles d'authentification et d'autorisation présents et corrects
4. Aucun secret, identifiant ou clé API codé en dur
5. Les fonctions cryptographiques utilisent des bibliothèques et des algorithmes approuvés
6. La gestion des erreurs n'expose pas d'informations sensibles
7. La journalisation inclut les événements de sécurité pertinents sans enregistrer de données sensibles
8. Les requêtes SQL utilisent des instructions paramétrées (pas de concaténation de chaînes)
9. Les opérations sur les fichiers valident les chemins (pas de traversée de répertoire)
10. Les dépendances tierces sont fixées à des versions vérifiées

**Exigences d'approbation par niveau de risque** :

| Niveau de risque | Nombre minimal d'approbateurs | Revue de sécurité requise |
|------------------|-------------------------------|---------------------------|
| Risque élevé | 2 (dont un Champion sécurité ou examinateur désigné par le RSSI) | Obligatoire |
| Risque moyen | 1 | Recommandé |
| Risque faible | 1 | Optionnel |

Les résultats des revues de code sont documentés et suivis jusqu'à résolution avant que le code soit approuvé pour promotion.

Le code est approuvé avant d'être promu vers les environnements de test ou de production.

---

## Portes de sécurité du pipeline CI/CD

Les contrôles de sécurité sont automatisés dans le pipeline CI/CD à des portes définies.

**Portes de sécurité du pipeline** :

| Porte | Étape | Contrôles | Action en cas d'échec |
|-------|-------|-----------|----------------------|
| **Porte 1 : Pré-commit** | Poste de travail du développeur | Analyse des secrets (hook pré-commit) | Bloquer le commit ; le développeur doit supprimer le secret |
| **Porte 2 : Compilation** | Pipeline CI — phase de compilation | Scan SAST, scan SCA des dépendances, vérification de conformité des licences, tests unitaires | Bloquer la fusion ; le développeur doit corriger |
| **Porte 3 : Pré-déploiement** | Pipeline CI — pré-déploiement | Scan DAST (risque élevé/moyen), tests d'intégration, tests de régression sécurité | Bloquer le déploiement ; corriger ou escalader |
| **Porte 4 : Déploiement en production** | Pipeline de déploiement | Vérification des approbateurs requis, contrôle du ticket de changement, validation de l'environnement | Bloquer le déploiement jusqu'à obtention des approbations |

**Seuils de blocage automatique** :

| Sévérité du résultat | Porte 2 SAST/SCA | Porte 3 DAST |
|---------------------|-----------------|-------------|
| Critique | Bloquer | Bloquer |
| Élevé | Bloquer | Bloquer |
| Moyen | Avertissement (suivre comme dette technique) | Avertissement (suivre comme dette technique) |
| Faible | Consigner uniquement | Consigner uniquement |

**Règles de dérogation** : Les dérogations aux portes du pipeline nécessitent l'approbation du RSSI (documentée dans le ticket de changement avec acceptation du risque et contrôles compensatoires). Les déploiements d'urgence peuvent contourner la Porte 3 (DAST) avec l'approbation du RSSI et un scan rétrospectif obligatoire dans les 72 heures.

Les résultats des portes de sécurité du pipeline sont rapportés au responsable développement chaque semaine et au RSSI chaque mois.

---

## Exigences en matière de tests de sécurité

Des processus de tests de sécurité sont définis et mis en œuvre dans le cycle de développement. Les tests valident que les exigences de sécurité ont été satisfaites avant le déploiement en production.

**Tests requis par niveau de risque** :

| Type de test | Risque élevé | Risque moyen | Risque faible |
|-------------|-------------|-------------|--------------|
| **SAST** (Analyse statique de la sécurité applicative) | Par commit ou quotidien | Par commit ou quotidien | Hebdomadaire |
| **SCA** (Analyse de la composition logicielle / scan des dépendances) | Quotidien ou continu | Quotidien ou continu | Hebdomadaire |
| **DAST** (Analyse dynamique de la sécurité applicative) | Par déploiement ou hebdomadaire | Mensuel | Optionnel |
| **Tests d'intrusion** | Annuellement + avant le lancement initial + après changement significatif | Tous les 2 ans | Optionnel |

**Exigences de base des tests** :

- Tous les tests de sécurité applicative doivent, au minimum, couvrir les catégories **OWASP Top 10:2025** : Contrôle d'accès défaillant, Mauvaise configuration de la sécurité, Défaillances de la chaîne d'approvisionnement logicielle, Défaillances cryptographiques, Injection, Conception non sécurisée, Défaillances d'authentification, Défaillances d'intégrité des logiciels et des données, Défaillances de journalisation et de surveillance de la sécurité, et Traitement inadéquat des conditions exceptionnelles.
- Tous les tests pré-production sont réalisés dans un environnement de test reflétant l'environnement de production aussi fidèlement que possible.

**Exigences de parité des environnements de test** :

| Composant | Exigence de parité avec la production |
|-----------|---------------------------------------|
| Système d'exploitation | Même système d'exploitation et version |
| Version du runtime / framework | Mêmes versions majeure et mineure |
| Moteur de base de données | Même moteur et version majeure |
| Architecture réseau | Même modèle de segmentation et règles de pare-feu (les plages IP peuvent différer) |
| Configuration TLS/SSL | Mêmes suites de chiffrement et versions de protocole |
| Authentification | Même mécanisme d'authentification et configuration AMF |
| Équilibreur de charge / proxy inverse | Même type et configuration |
| Conteneurisation / orchestration | Même plateforme et version (si applicable) |

**Différences acceptables** : adresses IP, noms d'hôtes, échelle (moins d'instances autorisées en test), seuils de volume de surveillance, et données synthétiques/anonymisées à la place des données de production.

**Vérification de l'environnement** : La parité de l'environnement est vérifiée avant les tests de sécurité majeurs (tests d'intrusion, DAST). La vérification est documentée et validée par l'équipe DevOps / Plateforme.

**Sécurité de l'environnement de test** : Les environnements de test sont soumis aux mêmes contrôles d'accès que les environnements de production. Les environnements de test ne sont pas accessibles depuis Internet sauf si nécessaire pour les tests DAST (avec des règles de pare-feu à durée limitée).
- Tous les tests d'intrusion sont réalisés par une société spécialisée externe.
- Toutes les applications web publiques sont testées à l'aide d'outils de sécurité manuels ou automatisés au moins une fois par an ou après un changement significatif.

**Normes et périmètre des tests d'intrusion** :

| Type d'application | Approche de test | Fréquence |
|-------------------|------------------|-----------|
| Application web accessible depuis Internet (risque élevé) | Évaluation complète selon le Guide de tests OWASP + tests de logique métier | Annuellement + avant le lancement initial + après changement significatif |
| Application web accessible depuis Internet (risque moyen) | Évaluation axée sur OWASP Top 10 | Tous les 2 ans |
| Application interne (risque élevé) | Tests authentifiés avec revue de la logique métier | Annuellement |
| Service API uniquement (risque élevé) | Tests de sécurité API (OWASP API Security Top 10) | Annuellement |
| Application mobile | Tests spécifiques mobiles (OWASP MASTG) | Annuellement pour le risque élevé |

**Dans le périmètre** (minimum) : authentification et gestion des sessions, autorisation et contrôle d'accès, validation des entrées (injection, XSS, SSRF), logique métier, sécurité des API, implémentation cryptographique, configuration et déploiement, gestion des erreurs et divulgation d'informations.

**Hors périmètre** (sauf inclusion explicite) : tests de déni de service, ingénierie sociale, tests de sécurité physique, composants hébergés par des tiers (testés séparément par le fournisseur).

**Normes de test** : Les tests d'intrusion suivent le Guide de tests OWASP v4.2 et/ou le PTES (Penetration Testing Execution Standard). Les rapports de test comprennent : résumé exécutif, méthodologie, résultats avec score CVSS, preuves (captures d'écran, requêtes/réponses), recommandations de remédiation et vérification des corrections.

**Critères de sélection des prestataires** : Les prestataires de tests d'intrusion doivent détenir des certifications pertinentes (ex. CREST, OSCP, CEH) et fournir une preuve d'assurance de responsabilité civile professionnelle. Les engagements avec les prestataires comprennent des règles d'engagement signées et un accord de confidentialité.

**Actions post-test** : (1) Remédier aux résultats selon les SLA de remédiation des vulnérabilités → (2) Le prestataire re-teste les résultats critiques/élevés après remédiation → (3) Rapport final avec résultats de re-test présenté au RSSI et à l'équipe de revue de direction → (4) Les enseignements tirés sont intégrés aux normes de codage sécurisé → (5) Rapport conservé pendant 5 ans.

**Catalogue de composants logiciels (SBOM)** :

- Les applications à risque élevé maintiennent un SBOM au format CycloneDX ou SPDX.
- Les SBOM sont générés automatiquement lors du processus de compilation (à chaque compilation pour le risque élevé ; hebdomadairement pour le risque moyen).
- Les SBOM sont mis à jour lors de changements de dépendances et révisés trimestriellement pour identifier les vulnérabilités connues.

**Contenu requis des SBOM** : Chaque SBOM comprend : nom et version du composant, fournisseur/auteur, type de licence, relations de dépendance (directes et transitives), et statut de vulnérabilité connu (références CVE si applicable).

**Processus de révision trimestrielle des SBOM** : (1) Générer le SBOM actuel → (2) Croiser tous les composants avec les bases de données de vulnérabilités (NVD, OSV, GitHub Advisory Database) → (3) Identifier les composants avec vulnérabilités connues, statut en fin de vie ou changements de licence → (4) Créer un plan de remédiation pour les problèmes identifiés (selon les SLA de remédiation des vulnérabilités).

**Surveillance des vulnérabilités des SBOM** : Les outils SCA surveillent en continu les composants des SBOM par rapport aux bases de données de vulnérabilités. Les nouvelles vulnérabilités critiques/élevées affectant les composants des SBOM déclenchent des alertes au responsable développement dans les 24 heures.

**Conservation des SBOM** : Les SBOM sont conservés pendant la durée de vie de l'application plus 3 ans.

Les résultats des tests, y compris les rapports de tests d'intrusion, sont communiqués à l'équipe de revue de direction.

---

## Remédiation des vulnérabilités

Les vulnérabilités de sécurité identifiées lors du développement et des tests sont remédiées dans des délais définis en fonction de la sévérité.

**Accords de niveau de service de remédiation** :

| Sévérité | Score CVSS | SLA de remédiation | Impact sur le déploiement |
|----------|------------|-------------------|---------------------------|
| **Critique** | 9,0–10,0 | 7 jours | Bloquer le déploiement si non résolu |
| **Élevé** | 7,0–8,9 | 30 jours | Bloquer le déploiement si dépassé |
| **Moyen** | 4,0–6,9 | 90 jours | Suivre comme dette technique |
| **Faible** | 0,1–3,9 | 180 jours | Planifier pour la prochaine version majeure |

Toutes les vulnérabilités identifiées lors de la phase de test, y compris les tests d'intrusion, sont corrigées avant la promotion en production ou gérées via le processus de gestion des risques et des exceptions.

**Processus d'escalade** :

- Les vulnérabilités dépassant le SLA de remédiation sont escaladées vers le RSSI et le propriétaire de l'application.
- Les vulnérabilités Critiques et Élevées dont le SLA est dépassé bloquent les déploiements ultérieurs jusqu'à remédiation ou approbation d'une exception avec contrôles compensatoires.
- Le statut de remédiation des vulnérabilités est examiné mensuellement et rapporté trimestriellement à l'équipe de revue de direction.

---

## Protection des données de test

Les données de production ne sont pas utilisées à des fins de test ou de développement.

Les données personnelles (au sens de l'art. 5 de la nLPD suisse) ne sont pas utilisées à des fins de test ou de développement.

Si des informations sensibles sont nécessaires dans le cadre du processus de test, elles sont :

- **assainies** (les champs sensibles sont supprimés ou remplacés),
- **anonymisées** (suppression irréversible des caractéristiques identifiantes), ou
- **pseudonymisées** (les données identifiantes sont remplacées par des identifiants artificiels).

Les **données synthétiques** (données générées artificiellement sans lien avec des personnes réelles) constituent l'approche privilégiée et sont utilisées autant que possible.

La création et l'utilisation des jeux de données de test sont documentées et approuvées par le propriétaire des données. Les jeux de données de test contenant des données personnelles transformées sont traités au minimum comme classification Interne.

Les données de test sont supprimées de manière sécurisée lorsqu'elles ne sont plus nécessaires.

---

## Promotion du code en production

Le code est promu en production exclusivement par des personnels autorisés et est soumis au processus documenté de gestion des changements.

Avant la promotion en production :

- Toutes les portes de sécurité requises ont été franchies (tests de sécurité, revue de code, remédiation des vulnérabilités).
- L'environnement de production est sauvegardé pour permettre un retour arrière en cas d'échec.
- Les données de test sont supprimées de l'application.
- Aucun fichier de développement, configuration de débogage, compte de test ou donnée de test ne doit être présent dans l'environnement de production.
- Pour les applications à risque élevé, le RSSI ou l'autorité de sécurité désignée fournit une validation explicite.

Les enregistrements de promotion comprennent la référence du ticket de changement, l'approbateur, le statut des portes de sécurité et l'horodatage du déploiement.

---

## Développement externalisé

Lorsque le développement logiciel est externalisé à des sous-traitants ou partenaires de développement tiers, les exigences de développement sécurisé de l'organisation s'appliquent.

**Les exigences contractuelles comprennent** :

- La conformité aux normes de codage sécurisé et aux exigences de sécurité de l'organisation.
- Les obligations de tests de sécurité (SAST, DAST, SCA) avec rapport à l'organisation.
- Les SLA de remédiation des vulnérabilités alignés sur cette politique.
- La notification des incidents de sécurité dans les 24 heures suivant leur découverte.
- Le droit de l'organisation d'auditer les pratiques de sécurité du sous-traitant avec préavis de 30 jours.
- Les droits de participation aux revues de code et aux revues d'architecture de sécurité.

**Vérification de la conformité des sous-traitants** :

- Les sous-traitants soumettent des rapports de tests de sécurité (résultats SAST/DAST/SCA, statut de remédiation) aux intervalles convenus.
- Les projets externalisés à risque élevé font l'objet d'une revue de sécurité par les personnels qualifiés en sécurité de l'organisation aux jalons majeurs (approbation de la conception, pré-production).
- Le code livré par les sous-traitants est soumis au même processus de revue de code et de tests de sécurité que le code développé en interne avant acceptation.

---

## Formation à la sécurité des développeurs

Tous les développeurs suivent une formation à la sécurité adaptée à leur rôle et à leurs responsabilités.

**Exigences de formation** :

| Type de formation | Public | Fréquence | Durée minimale |
|-------------------|--------|-----------|----------------|
| **Formation initiale à la sécurité** | Tous les développeurs | Avant l'accès au code de production | 4 heures |
| **Mise à jour annuelle** | Tous les développeurs | Annuellement | 2 heures |
| **Formation Champion sécurité** (optionnel pour les PME) | Champions sécurité désignés | Initiale + annuellement | 8 heures + 4 heures |

La formation couvre au minimum :

- Les vulnérabilités OWASP Top 10 et les techniques d'atténuation.
- Les pratiques de codage sécurisé pertinentes pour la pile technologique du développeur.
- La politique de développement sécurisé et les normes de codage de l'organisation.
- Les faiblesses logicielles courantes (CWE/SANS Top 25).

La complétion de la formation est enregistrée et vérifiée avant l'octroi de l'accès au code de production. Les dossiers de formation sont conservés pendant la durée de l'emploi plus 3 ans.

Lorsque les ressources le permettent, l'organisation devrait mettre en place un **programme de Champions sécurité** — des développeurs désignés au sein de chaque équipe qui reçoivent une formation avancée en sécurité et servent de premier point de contact pour les questions de sécurité dans leur équipe.

**Programme de Champions sécurité** (si mis en place) :

**Critères de sélection** : Les Champions sécurité sont désignés parmi les équipes de développement sur la base de : un intérêt démontré pour la sécurité, au moins 2 ans d'expérience en développement, la volonté de consacrer environ 10 % du temps de travail aux activités de sécurité, et l'approbation du responsable d'équipe.

**Responsabilités** :
- Conduire les revues de code axées sur la sécurité pour les changements à risque élevé au sein de leur équipe.
- Fournir des conseils et un mentorat en codage sécurisé aux membres de l'équipe.
- Participer aux sessions de modélisation des menaces en tant que représentant sécurité de l'équipe.
- Escalader les problèmes de sécurité vers le RSSI ou l'équipe sécurité.
- Se tenir informé des menaces et vulnérabilités émergentes pertinentes pour la pile technologique de l'équipe.
- Promouvoir la culture et la sensibilisation à la sécurité au sein de l'équipe.

**Formation** : Formation initiale : 8 heures (approfondissement OWASP Top 10, schémas d'architecture sécurisée, modélisation des menaces, outils de test de sécurité). Mise à jour annuelle : 4 heures (menaces émergentes, nouvelles techniques d'attaque, normes actualisées).

**Incitations** : Les contributions des Champions sécurité sont reconnues dans les évaluations de performance. L'organisation devrait envisager la participation à des conférences, le financement de certifications ou des opportunités de développement professionnel similaires.

**Indicateurs du programme** : Nombre de Champions sécurité actifs (objectif : au moins 1 par équipe de développement), taux de participation aux revues de sécurité, résultats de sécurité identifiés en revue de code, taux de complétion de la formation.

---

## Rôles et responsabilités

| Rôle | Responsabilités |
|------|----------------|
| **RSSI** | Propriété de la politique ; approbation des portes de sécurité pour les applications à risque élevé ; approbation des exceptions ; autorité d'escalade ; supervision du programme de formation |
| **Responsable développement** | Intégration de la sécurité dans le SDLC ; application des revues de code ; maintenance des normes de codage sécurisé ; supervision de la remédiation des vulnérabilités ; classification des risques applicatifs |
| **Champion sécurité** (si désigné) | Promotion de la sécurité au sein de l'équipe de développement ; revue de code axée sur la sécurité ; mentorat en codage sécurisé |
| **Développeurs** | Respect des normes de codage sécurisé ; remédiation des vulnérabilités ; complétion de la formation à la sécurité ; participation aux revues de code |
| **Responsable AQ / Tests** | Exécution des tests de sécurité ; gestion de l'environnement de test ; protection des données de test ; rapports de tests de sécurité |
| **DevOps / Équipe plateforme** | Intégration des outils de sécurité CI/CD ; cloisonnement des environnements ; automatisation du déploiement ; analyse des secrets |
| **Propriétaire de l'application** | Contribution à la classification des risques applicatifs ; demandes d'exceptions ; approbation des exigences de sécurité |

---

## Preuves

Les preuves suivantes démontrent la conformité à cette politique :

| N° | Preuve | Responsable | Fréquence |
|----|--------|-------------|-----------|
| 1 | **Registre de classification des risques applicatifs** (toutes les applications classées par niveau de risque) | Responsable développement / RSSI | *Maintenu en continu ; révisé annuellement ; objectif : 100 % des applications classées* |
| 2 | **Documentation des exigences de sécurité** (spécifications des exigences, modèles de menaces pour le risque élevé) | Responsable développement | *Par projet ; conservé pendant la durée de vie de l'application* |
| 3 | **Rapports de scan SAST/SCA** (journaux d'exécution des outils, résultats, statut de remédiation) | DevOps / Responsable développement | *Selon la fréquence définie par niveau de risque ; conservé 2 ans* |
| 4 | **Rapports de tests d'intrusion** (périmètre, résultats, vérification des corrections) | RSSI | *Annuellement pour le risque élevé ; tous les 2 ans pour le risque moyen ; conservé 5 ans* |
| 5 | **Enregistrements des revues de code** (commentaires de revue, enregistrements d'approbation, historique des demandes de fusion) | Responsable développement | *Par modification de code ; conservé 2 ans* |
| 6 | **Enregistrements de remédiation des vulnérabilités** (tickets avec suivi des SLA, preuves de clôture) | Responsable développement | *Par vulnérabilité ; examiné mensuellement ; conservé 3 ans* |
| 7 | **Documentation du cloisonnement des environnements** (schémas réseau, enregistrements de contrôle d'accès) | DevOps / IT Opérations | *Révisé annuellement ; mis à jour lors de changements* |
| 8 | **Dossiers de formation à la sécurité des développeurs** (dates de complétion, contenu de la formation) | RSSI / RH | *Suivi par développeur ; examiné annuellement ; objectif : 100 % de complétion* |
| 9 | **Rapports de sécurité du développement externalisé** (résultats SAST/DAST/SCA des sous-traitants, enregistrements d'audit) | Responsable développement / RSSI | *Selon les termes du contrat ; conservé pour la durée du contrat + 3 ans* |
| 10 | **Enregistrements de déploiement en production** (tickets de changement, validation des portes de sécurité, plans de retour arrière) | Gestion des changements / DevOps | *Par déploiement ; conservé 3 ans* |

---

# Conformité à la politique

## Mesure de la conformité

L'équipe de management de la sécurité de l'information vérifie la conformité à cette politique par diverses méthodes, notamment les rapports de scan SAST/DAST/SCA, les enregistrements de revues de code, les rapports de tests d'intrusion, les dossiers de formation des développeurs, les audits internes et externes, et les retours au propriétaire de la politique.

## Exceptions

Toute exception à cette politique doit être approuvée et enregistrée à l'avance par le Responsable de la sécurité de l'information, avec acceptation documentée du risque, contrôles compensatoires et date de révision définie. Les exceptions sont communiquées à l'équipe de revue de direction. Les déploiements d'urgence contournant les portes de sécurité nécessitent l'approbation du RSSI et une validation de sécurité rétrospective dans les 72 heures.

## Non-conformité

Tout employé reconnu coupable d'avoir violé cette politique peut faire l'objet de mesures disciplinaires pouvant aller jusqu'au licenciement.

## Amélioration continue

Cette politique est révisée et mise à jour dans le cadre du processus d'amélioration continue. Les révisions tiennent compte des évolutions des normes de développement sécurisé (OWASP, NIST SSDF, CWE/SANS Top 25), des menaces et techniques d'attaque émergentes, des changements réglementaires, des évolutions de l'outillage et des méthodologies de développement, et des enseignements tirés des incidents de sécurité et des tests d'intrusion.

---

# Domaines de la norme ISO 27001 couverts

Politique de cycle de développement sécurisé — Correspondance avec les contrôles ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership et engagement | 5.1 Politiques de sécurité de l'information |
| Clause 5.2 Politique | 5.4 Responsabilités de la direction |
| Clause 6.2 Objectifs de sécurité de l'information | 5.36 Conformité aux politiques, règles et normes |
| Clause 7.3 Sensibilisation | 6.3 Sensibilisation, formation et éducation à la sécurité de l'information |
| | 6.4 Processus disciplinaire |
| | 8.4 Accès au code source |
| | **8.25 Cycle de développement sécurisé** |
| | **8.26 Exigences de sécurité des applications** |
| | 8.27 Principes d'ingénierie et d'architecture de systèmes sécurisés |
| | 8.28 Codage sécurisé |
| | **8.29 Tests de sécurité dans le développement et l'acceptation** |
| | 8.30 Développement externalisé |
| | 8.31 Séparation des environnements de développement, de test et de production |
| | 8.33 Informations de test |

**Cadre réglementaire et juridique** :

| Cadre | Pertinence |
|-------|-----------|
| nLPD suisse (revDSG) | Art. 7 — Protection des données dès la conception et par défaut ; Art. 8 — Mesures techniques et organisationnelles de protection des données |
| OPDo suisse (Ordonnance sur la protection des données) | Art. 1–3 — Exigences minimales en matière de sécurité des données |
| RGPD de l'UE (si applicable) | Art. 25 — Protection des données dès la conception et par défaut ; Art. 32 — Sécurité du traitement |
| ISO/IEC 27001:2022 | Contrôles Annexe A 8.25, 8.26, 8.29 — Développement sécurisé, exigences de sécurité des applications, tests de sécurité |
| ISO/IEC 27002:2022 | Sections 8.25–8.31, 8.33 — Conseils de mise en œuvre des contrôles de développement sécurisé |
| NIST SP 800-218 (SSDF) | Secure Software Development Framework — groupes de pratiques PO, PS, PW, RV |
| OWASP Top 10:2025 | Référence de base minimale pour les tests — inclut les défaillances de la chaîne d'approvisionnement logicielle et le traitement inadéquat des conditions exceptionnelles |
| CWE/SANS Top 25 | Faiblesses logicielles les plus dangereuses — référence de codage sécurisé |

---

<!-- QA_VERIFIED: 2026-03-29 -->
