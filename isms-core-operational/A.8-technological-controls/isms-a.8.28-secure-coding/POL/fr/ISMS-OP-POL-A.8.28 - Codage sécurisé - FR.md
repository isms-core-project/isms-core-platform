<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.8.28-FR:operational:OP-POL:a.8.28 -->
**ISMS-OP-POL-A.8.28 — Codage sécurisé**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Codage sécurisé |
| **Type de document** | Politique opérationnelle |
| **Identifiant du document** | ISMS-OP-POL-A.8.28 |
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

- ISO/IEC 27001:2022 Contrôle A.8.28 — Codage sécurisé
- ISO/IEC 27002:2022 Section 8.28 — Conseils de mise en œuvre pour le codage sécurisé
- NIST SP 800-218 — Secure Software Development Framework (SSDF) v1.1
- NIST SP 800-53 Rév. 5 — SA-15, SA-16, SA-17 (Processus de développement, normes et outils)
- OWASP Secure Coding Practices — Guide de référence rapide
- OWASP Top 10 (2021) — Risques de sécurité des applications web
- CWE/SANS Top 25 — Faiblesses logicielles les plus dangereuses (édition 2025)
- CIS Controls v8 — Mesures de protection 16.1–16.14 (Application Software Security)
- CERT Secure Coding Standards (SEI/Carnegie Mellon)

**Contrôles Annexe A associés** :

| Contrôle | Relation avec le codage sécurisé |
|----------|----------------------------------|
| A.5.8 Sécurité de l'information dans la gestion de projets | Exigences de sécurité définies à l'initiation du projet |
| A.5.23 Sécurité de l'information pour l'utilisation des services cloud | Codage sécurisé pour les applications déployées dans le cloud |
| A.8.4 Accès au code source | Contrôle d'accès aux référentiels et protection des branches |
| A.8.8 Gestion des vulnérabilités techniques | Remédiation des vulnérabilités du code déployé |
| A.8.9 Gestion de la configuration | Configuration sécurisée des outils et environnements de développement |
| A.8.15 Journalisation | Exigences de journalisation de sécurité au niveau applicatif |
| A.8.24 Utilisation de la cryptographie | Implémentation cryptographique dans le code applicatif |
| A.8.25–26–29 Cycle de développement sécurisé | Cadre SDLC global ; exigences de sécurité, tests |
| A.8.31 Séparation des environnements | Isolation des environnements de développement, test et production |
| A.8.32 Gestion des changements | Déploiement contrôlé des modifications de code en production |

**Politiques internes associées** :

- Politique de cycle de développement sécurisé
- Politique d'accès au code source
- Politique de gestion des vulnérabilités
- Politique d'utilisation de la cryptographie
- Politique de gestion des changements
- Politique de journalisation

---

# Politique de codage sécurisé

## Objet

La présente politique a pour objet d'établir les principes de codage sécurisé obligatoires applicables tout au long du cycle de développement logiciel. Le codage sécurisé prévient l'introduction de vulnérabilités dans la base de code, réduisant ainsi la surface d'attaque et protégeant les actifs informationnels, les clients et la réputation de l'organisation. Les mauvaises pratiques de codage — validation insuffisante des entrées, génération de clés faibles, identifiants codés en dur, gestion des erreurs inadéquate — créent des faiblesses exploitables que les adversaires ciblent systématiquement.

Cette politique soutient l'art. 7 (protection des données dès la conception et par défaut) et l'art. 8 (mesures techniques et organisationnelles) de la nLPD (revDSG) suisse en exigeant que la sécurité soit intégrée dans le code applicatif dès la phase de conception. Lorsque l'organisation traite des données de personnes dans l'UE/EEE, les exigences des art. 25 (protection des données dès la conception et par défaut) et 32 (sécurité du traitement) du RGPD s'appliquent également. Le codage sécurisé est une mesure technique fondamentale pour démontrer que les systèmes traitant des données personnelles sont conçus pour prévenir les accès non autorisés, les violations de données et les atteintes à l'intégrité.

## Champ d'application

Toutes les activités de développement logiciel dans lesquelles l'organisation écrit, modifie ou maintient du code source, notamment :

- Toutes les applications développées en interne (web, mobile, bureau, API, microservices).
- L'infrastructure en tant que code (IaC), les scripts de gestion de configuration et les définitions de pipeline CI/CD.
- Les intégrations personnalisées, plugins et extensions de plateformes tierces.
- Les contributions open source faites au nom de l'organisation.
- Le code écrit par des sous-traitants, des équipes de développement externalisées et des développeurs offshore travaillant pour le compte de l'organisation.

Tous les développeurs, ingénieurs de sécurité, ingénieurs AQ, ingénieurs DevOps, sous-traitants et équipes de développement tiers écrivant du code pour l'organisation.

**Hors périmètre** : Les logiciels commerciaux sur étagère (COTS) sans personnalisation (couverts par l'évaluation de sécurité des fournisseurs) ; la gestion des vulnérabilités en production post-déploiement (couverte par A.8.8) ; la gouvernance du cycle de développement sécurisé (couverte par A.8.25-26-29) ; le contrôle d'accès au code source (couvert par A.8.4).

## Principe

Tout le code source produit pour ou au nom de l'organisation doit suivre des normes de codage sécurisé documentées. La sécurité doit être prise en compte avant de commencer à coder, appliquée pendant le codage, et vérifiée après sa complétion. Les développeurs ne doivent pas s'appuyer uniquement sur les tests de sécurité pour détecter les défauts — le codage sécurisé prévient l'introduction de défauts en premier lieu.

L'organisation doit définir explicitement les normes de codage qu'elle suit, en référençant des cadres reconnus par l'industrie (OWASP, CWE/SANS Top 25, CERT ou directives spécifiques aux langages). Les affirmations génériques de « codage sécurisé » sans référence à un cadre sont insuffisantes à des fins d'audit.

---

## Normes de codage sécurisé

L'organisation établit et maintient des normes de codage sécurisé documentées applicables à chaque langage de programmation et framework en usage actif.

**Cadres de référence de base** :

| Cadre | Périmètre | Application |
|-------|-----------|-------------|
| OWASP Top 10 (2021) | Vulnérabilités des applications web | Référence obligatoire pour tout code accessible depuis Internet |
| CWE/SANS Top 25 | Faiblesses logicielles les plus dangereuses | Référence obligatoire pour tout le code |
| OWASP Secure Coding Practices | Liste de contrôle de codage indépendante de la technologie | Référence obligatoire pour tout le développement |
| CERT Secure Coding Standards | Codage sécurisé spécifique aux langages (C, C++, Java, Perl) | Obligatoire lorsque des normes spécifiques aux langages existent |

**Normes spécifiques aux langages** :

Le responsable développement maintient un registre des langages approuvés et de leurs références de codage sécurisé associées. Au minimum :

| Langage / Framework | Référence de codage sécurisé |
|--------------------|------------------------------|
| Python | PEP 8 + OWASP Python Security + jeu de règles Bandit |
| JavaScript / TypeScript | Règles du plugin de sécurité ESLint + référence OWASP NodeGoat |
| Java | CERT Oracle Secure Coding Standard for Java + règles SpotBugs/FindSecBugs |
| C / C++ | CERT C/C++ Secure Coding Standards + application des avertissements du compilateur |
| Go | Bonnes pratiques de sécurité Go + govulncheck |
| .NET / C# | Microsoft Secure Coding Guidelines + analyseurs Roslyn |
| PHP | OWASP PHP Security Cheat Sheet + règles Psalm/PHPStan |

Si un langage est utilisé sans entrée dans ce registre, le responsable développement doit documenter la référence de codage sécurisé applicable avant que ce langage entre en usage en production.

**Révision des normes de codage** : Les normes de codage sécurisé sont révisées annuellement, ou lors de l'adoption d'un nouveau langage ou framework, ou lors de l'émergence d'une classe de vulnérabilités significative nécessitant des conseils supplémentaires.

---

## Prévention des vulnérabilités courantes

Les développeurs écrivent du code qui prévient les classes de vulnérabilités identifiées par l'OWASP Top 10 et le CWE/SANS Top 25. Les sections suivantes définissent les pratiques de codage obligatoires pour les catégories de vulnérabilités les plus répandues.

### Validation des entrées

Toutes les données provenant de sources externes sont traitées comme non fiables et validées avant tout traitement.

**Exigences** :

- Valider toutes les entrées côté serveur, quelle que soit la validation côté client. La validation côté client améliore l'expérience utilisateur mais ne constitue pas un contrôle de sécurité.
- Utiliser la validation par liste d'autorisation (positive) : définir ce qui est autorisé, rejeter tout le reste. La validation par liste de refus (négative) est insuffisante comme seul contrôle.
- Valider le type de données, la longueur, la plage et le format. Rejeter les entrées malformées avant tout traitement.
- Valider et assainir toutes les entrées provenant de formulaires, paramètres d'URL, en-têtes HTTP, cookies, charges utiles API, téléchargements de fichiers et données de systèmes en amont.
- Utiliser des requêtes paramétrées ou des instructions préparées pour toutes les interactions avec la base de données. La concaténation des données utilisateur dans des instructions SQL est interdite.
- Valider les téléchargements de fichiers : restreindre les types de fichiers autorisés, imposer des limites de taille, analyser les maliciels, stocker les fichiers téléchargés hors de la racine web et ne jamais exécuter les fichiers téléchargés.

### Encodage des sorties

Toutes les sorties restituées aux utilisateurs ou aux systèmes externes sont encodées pour prévenir les attaques par injection.

**Exigences** :

- Appliquer un encodage de sortie adapté au contexte (HTML, JavaScript, URL, CSS, XML) lors du rendu de contenu dynamique.
- Utiliser les fonctions d'encodage fournies par le framework plutôt que des implémentations personnalisées.
- Encoder les sorties au point de rendu, et non au point de stockage.
- Définir correctement les en-têtes Content-Type et charset sur toutes les réponses HTTP.
- Mettre en œuvre les en-têtes Content Security Policy (CSP) pour atténuer les risques de scripts intersites (XSS).

### Authentification et gestion des sessions

Le code applicatif mettant en œuvre l'authentification et la gestion des sessions doit suivre des schémas sécurisés établis.

**Exigences** :

- Ne pas implémenter de schémas d'authentification personnalisés. Utiliser le framework d'authentification approuvé ou le fournisseur d'identité de l'organisation.
- Stocker les mots de passe en utilisant des algorithmes de hachage adaptatifs approuvés (bcrypt, scrypt ou Argon2id) avec des sels uniques. MD5, SHA-1 et les hachages sans sel sont interdits.
- Mettre en œuvre le verrouillage de compte ou des délais progressifs après des tentatives d'authentification répétées échouées.
- Générer les identifiants de session à l'aide de générateurs de nombres aléatoires cryptographiquement sûrs. Les identifiants de session doivent être d'une longueur suffisante (minimum 128 bits d'entropie).
- Définir des attributs de cookies sécurisés : `Secure`, `HttpOnly`, `SameSite`. Transmettre les cookies de session uniquement via TLS.
- Invalider les sessions à la déconnexion, au changement de mot de passe et à l'élévation de privilèges. Définir des valeurs de délai d'expiration de session appropriées.
- Ne pas exposer les identifiants de session dans les URL, les messages d'erreur ou les journaux.

### Gestion des erreurs et journalisation

La gestion des erreurs applicatives doit prévenir la divulgation d'informations et soutenir la surveillance de la sécurité.

**Exigences** :

- Afficher des messages d'erreur génériques aux utilisateurs. Ne pas exposer les traces de pile, les messages d'erreur de base de données, les chemins de fichiers internes, les numéros de version des frameworks ou les détails de configuration du serveur.
- Journaliser tous les événements de sécurité pertinents : succès et échecs d'authentification, échecs d'autorisation, échecs de validation des entrées, erreurs applicatives et actions administratives.
- Journaliser suffisamment de contexte pour l'investigation : horodatage (UTC), identité de l'utilisateur, adresse IP source, action tentée, ressource affectée et statut de succès ou d'échec.
- Ne pas journaliser de données sensibles : mots de passe, jetons de session, données personnelles, numéros de carte de crédit ou clés de chiffrement.
- Utiliser un framework de journalisation centralisé. Ne pas écrire de mécanismes de journalisation personnalisés qui contournent l'infrastructure de journalisation de l'organisation.
- S'assurer que les entrées de journal contenant des données non fiables ne peuvent pas s'exécuter en tant que code dans l'interface d'affichage des journaux (prévention de l'injection de journaux).

### Pratiques cryptographiques

Le code applicatif qui implémente ou utilise la cryptographie doit respecter la politique cryptographique de l'organisation.

**Exigences** :

- Utiliser les bibliothèques cryptographiques fournies par la plateforme ou des bibliothèques tierces approuvées. Ne pas implémenter d'algorithmes cryptographiques personnalisés.
- Utiliser des algorithmes actuels et approuvés : AES-256 pour le chiffrement symétrique, RSA-2048+ ou ECDSA P-256+ pour les opérations asymétriques, SHA-256+ pour le hachage. MD5 et SHA-1 sont interdits à des fins de sécurité.
- TLS 1.2 minimum (TLS 1.3 préféré) pour toutes les données en transit. SSL, TLS 1.0 et TLS 1.1 sont interdits.
- Générer les clés cryptographiques à l'aide de générateurs de nombres aléatoires cryptographiquement sûrs. Ne pas utiliser de graines prévisibles.
- Ne pas coder en dur les clés cryptographiques, les clés API ou les secrets dans le code source. Utiliser la solution de gestion des secrets approuvée de l'organisation.
- Se référer à ISMS-OP-POL-A.8.24 (Utilisation de la cryptographie) pour les exigences cryptographiques complètes.

### Contrôle d'accès dans le code

Le code applicatif doit appliquer les autorisations de manière cohérente.

**Exigences** :

- Appliquer le contrôle d'accès côté serveur pour chaque demande. Ne pas s'appuyer uniquement sur le masquage des éléments d'interface.
- Refuser par défaut : si le niveau d'autorisation d'un utilisateur ne peut pas être déterminé, refuser l'accès.
- Appliquer le principe du moindre privilège dans le code : accorder les autorisations minimales requises pour chaque fonction.
- Valider les autorisations pour chaque point de terminaison API, y compris les références indirectes aux objets.
- Ne pas faire confiance aux revendications de rôle ou d'autorisation fournies par le client sans vérification côté serveur.

---

## Gestion des dépendances et des bibliothèques

Les bibliothèques tierces, frameworks et composants open source introduisent un risque lié à la chaîne d'approvisionnement et doivent être gérés tout au long de leur cycle de vie.

**Exigences** :

- Maintenir un inventaire des dépendances pour chaque application. Toutes les applications en production doivent maintenir un catalogue de composants logiciels (SBOM) au format CycloneDX ou SPDX, généré automatiquement via le pipeline de compilation.
- Utiliser des outils d'analyse de la composition logicielle (SCA) ([Outil SCA] — ex. Dependabot, Snyk, OWASP Dependency-Check ou équivalent) pour analyser les dépendances à la recherche de vulnérabilités connues.
- L'analyse SCA doit s'exécuter à chaque compilation (intégration dans le pipeline CI/CD). Les compilations doivent échouer si des vulnérabilités de dépendances critiques ou élevées sont détectées et non résolues.
- Fixer les versions des dépendances dans les fichiers de verrouillage. Ne pas utiliser de plages de versions flottantes (ex. `*` ou `>=`) pour les dépendances de production.
- Évaluer les nouvelles dépendances avant adoption : vérifier le statut de maintenance, les vulnérabilités connues, la compatibilité des licences et l'activité de la communauté. Les bibliothèques abandonnées ou non maintenues ne doivent pas être introduites.
- Supprimer les dépendances inutilisées. Réaliser un audit des dépendances au moins une fois par an pour identifier et supprimer les bibliothèques qui ne sont plus utilisées.

**Exigences relatives au catalogue de composants logiciels (SBOM)** :

La génération de SBOM est une pratique standard pour toutes les applications, et non limitée aux applications à risque élevé.

- **Format** : CycloneDX ou SPDX (JSON ou XML).
- **Génération** : Automatisée via le pipeline de compilation (chaque compilation génère un SBOM mis à jour). Outils : [Outil SBOM — ex. syft, cdxgen, cyclonedx-maven-plugin ou équivalent spécifique au langage].
- **Contenu** : Toutes les dépendances directes et transitives, versions, licences, fournisseurs, vulnérabilités connues.
- **Couverture** : Applications en production — SBOM obligatoire (couverture 100 %). Outils internes — SBOM obligatoire. Preuves de concept / expériences — SBOM recommandé (si le code persiste >30 jours).
- **Stockage et accès** : SBOM stockés dans [Référentiel d'artefacts / Dependency Track / Plateforme SBOM], accessibles à l'équipe développement, l'équipe sécurité, le service juridique (pour la conformité des licences) et l'équipe de réponse aux incidents. Chaque SBOM doit être étiqueté avec la version d'application correspondante (relation 1:1).
- **Utilisation** : Gestion des vulnérabilités (l'outil SCA ingère le SBOM, le croise avec les bases de données CVE, identifie les applications affectées) ; conformité des licences (l'équipe juridique examine le SBOM pour détecter les conflits de licences) ; réponse aux incidents (lors de la divulgation d'une nouvelle vulnérabilité, interroger le référentiel SBOM pour identifier les applications affectées en quelques heures) ; transparence de la chaîne d'approvisionnement (demandes d'audit tierce ou de diligence raisonnable client).
- **Validation de l'exactitude** : Audit trimestriel — échantillon de 10 % des applications, comparaison du SBOM avec les dépendances réellement déployées (analyse binaire). Si le SBOM ne correspond pas à la réalité, investigation de la cause racine (problème de processus de compilation, installation manuelle de dépendance).
- **Exceptions** : Applications héritées sans pipeline de compilation — génération manuelle trimestrielle du SBOM (transitoire jusqu'à migration ou décommissionnement de l'application héritée). Logiciels COTS tiers — demande de SBOM au fournisseur (si le fournisseur ne fournit pas de SBOM, documenter l'écart dans le registre des risques).
- **Calendrier** : Toutes les applications en production doivent générer des SBOM d'ici [Date — suggéré : 6 mois après la date d'entrée en vigueur de la politique]. Déploiement progressif : applications critiques en premier (mois 1–3), puis toute la production (mois 4–6).

**Gestion des versions des dépendances (fixation et mises à jour)** :

La fixation des versions des dépendances assure des compilations reproductibles mais crée un risque d'obsolescence si les versions ne sont jamais mises à jour. L'organisation maintient une cadence de mise à jour des dépendances pour équilibrer stabilité et sécurité.

- **Fichiers de verrouillage** : Obligatoires (package-lock.json, Gemfile.lock, poetry.lock, go.sum, etc.).
- **Plages flottantes** : Interdites en production (`*`, `>=`, `^` autorisés uniquement hors production).
- **Versions exactes** : Fixées dans le fichier de verrouillage (ex. `lodash@4.17.21` et non `lodash@^4.0.0`).

**Cadence de mise à jour des dépendances** :

| Type de mise à jour | Fréquence | Déclencheur | Périmètre de revue |
|--------------------|-----------|-------------|-------------------|
| **Correctifs de sécurité** (correctifs de vulnérabilités) | Immédiat | Alerte SCA (CVE Critique/Élevé) | Ciblé (seule la dépendance affectée) |
| **Mises à jour mineures** (rétrocompatibles) | Mensuel | Fenêtre de maintenance planifiée | Mise à jour par lots (plusieurs dépendances à la fois) |
| **Mises à jour majeures** (changements cassants) | Trimestriel ou par dépendance | Maintenance planifiée ou travail de fonctionnalité prévu | Évaluation individuelle par dépendance |

**Procédure de mise à jour** :
1. **Identifier les mises à jour** : L'outil SCA signale les dépendances obsolètes, ou Dependabot/Renovate génère une PR.
2. **Examiner le journal des modifications** : Vérifier les notes de version pour les changements cassants, les correctifs de sécurité et les nouvelles fonctionnalités.
3. **Mettre à jour et tester** : Mettre à jour le fichier de verrouillage, exécuter la suite de tests complète (unitaires, intégration, E2E).
4. **Analyse de sécurité** : Exécuter SAST et SCA sur les dépendances mises à jour.
5. **Déployer** : Suivre le processus de gestion des changements (environnement de qualification puis production).
6. **Surveiller** : Surveillance post-déploiement pour détecter les régressions (taux d'erreurs, performances).

**Mises à jour automatisées des dépendances** (recommandé) :
- Outil : Dependabot, Renovate ou équivalent.
- Configuration : Création automatique de PR pour les correctifs de sécurité (fusion automatique si les tests passent), revue manuelle pour les mises à jour mineures/majeures.
- SLA de revue : Correctifs de sécurité révisés sous 2 jours ouvrés, mises à jour mineures sous 1 semaine.

**Limites d'obsolescence des dépendances** :
- Dépendances critiques (authentification, cryptographie, frameworks web) : Aucune version datant de plus de 12 mois.
- Dépendances standard : Aucune version datant de plus de 24 mois.
- Exemption : Si la version plus récente présente des problèmes connus, documenter pourquoi l'ancienne version est conservée (avec contrôles compensatoires — surveillance renforcée).

**Indicateurs de gestion des dépendances** :
- Âge moyen des dépendances (jours depuis la publication de la version).
- Pourcentage de dépendances avec des vulnérabilités connues.
- Fréquence de mise à jour des dépendances (mises à jour par mois).
- Délai de la divulgation de CVE au déploiement du correctif.
- Cible : Âge moyen des dépendances <180 jours ; <1 % de dépendances avec des CVE Critiques/Élevés connus.

**SLA de remédiation des vulnérabilités des dépendances** :

| Sévérité | Score CVSS | SLA de remédiation |
|----------|------------|-------------------|
| Critique | 9,0–10,0 | 7 jours |
| Élevé | 7,0–8,9 | 30 jours |
| Moyen | 4,0–6,9 | 90 jours |
| Faible | 0,1–3,9 | Prochaine version planifiée |

---

## Exigences de revue de code

Toutes les modifications de code sont examinées avant la fusion vers les branches protégées.

**Types de revue** :

| Type de revue | Requis pour | Examinateur |
|---------------|-------------|-------------|
| Revue de code par les pairs | Toutes les modifications de code | Au moins un développeur autre que l'auteur |
| Revue axée sur la sécurité | Modifications concernant l'authentification, l'autorisation, la cryptographie, la validation des entrées, la gestion des sessions ou le code de protection des données | Développeur avec formation en sécurité ou Champion sécurité |
| Revue automatisée de code | Toutes les modifications de code | [Outil SAST] intégré dans le pipeline CI/CD |

**Exigences de revue de code basées sur les risques** :

Le nombre d'examinateurs et leurs qualifications sont déterminés par la classification des risques de la modification de code :

**Code standard** (non critique pour la sécurité) :
- Examinateurs : Minimum 1 développeur pair (pas l'auteur).
- Qualifications : Tout développeur de l'équipe avec >3 mois d'expérience.
- Approbation : 1 approbation requise pour la fusion.

**Code critique pour la sécurité** (authentification, autorisation, gestion des sessions, validation des entrées, cryptographie, protection des données) :
- Examinateurs : Minimum 2 examinateurs : (1) Développeur pair (n'importe quel membre de l'équipe), ET (2) Champion sécurité OU membre de l'équipe sécurité (obligatoire).
- Qualifications : Le Champion sécurité doit avoir suivi la formation de Champion sécurité.
- Approbation : Les deux examinateurs doivent approuver avant la fusion.

**Code d'infrastructure/déploiement** (IaC, modifications du pipeline CI/CD, gestion de la configuration) :
- Examinateurs : Minimum 1 pair + approbation du responsable DevOps.
- Qualifications : L'examinateur doit comprendre les implications en matière d'infrastructure.
- Approbation : 2 approbations requises.

**Modifications à risque élevé** (API externes, traitement des paiements, fonctions d'administration) :
- Examinateurs : 2 pairs + membre de l'équipe sécurité (3 au total).
- Tests : Doit inclure des tests de sécurité automatisés (SAST réussi, tests d'intégration réussis).
- Approbation : Les 3 examinateurs approuvent + les tests automatisés réussissent.

**Intégrité à deux personnes** (scripts de rotation des secrets, code d'élévation de privilèges, contournement des contrôles de sécurité) :
- Examinateurs : 2 développeurs seniors OU 1 senior + membre de l'équipe sécurité.
- Approbation : Les deux approuvent + le RSSI est informé (prise de connaissance, aucune approbation requise sauf pour les changements en production).

**Disponibilité des Champions sécurité** :
- Minimum 1 Champion sécurité par équipe de développement (ratio 1:8 développeurs).
- Les Champions sécurité disposent d'une allocation de temps dédiée aux revues de sécurité (10 % du temps de travail).
- Si le Champion sécurité est indisponible : l'équipe sécurité fournit une revue dans les 48 heures.

Documentation : La description de la PR doit indiquer le type de revue requis en fonction de la classification du code (standard, critique pour la sécurité, risque élevé). Les contrôles CI/CD doivent vérifier que le nombre d'approbations de revue correspond à l'exigence.

**Exigences de la revue de code par les pairs** :

- L'auteur du code ne peut pas approuver son propre code (séparation des fonctions).
- Les examinateurs vérifient la conformité aux normes de codage sécurisé de l'organisation.
- Les examinateurs vérifient notamment : les secrets codés en dur, les schémas de codage non sécurisés, l'absence de validation des entrées, l'absence d'encodage des sorties, les autorisations excessives, la gestion inadéquate des erreurs et l'absence de journalisation.
- Les demandes de fusion doivent inclure une description des modifications, un lien vers le problème ou le ticket associé, et des preuves de test.
- Les revues doivent être complétées avant la fusion du code vers une branche protégée.

**Liste de contrôle de la revue de code axée sur la sécurité** :

- [ ] Validation des entrées appliquée à toutes les entrées externes
- [ ] Encodage des sorties appliqué aux points de rendu
- [ ] Aucun secret, clé ou identifiant codé en dur
- [ ] Requêtes paramétrées utilisées pour les interactions avec la base de données
- [ ] L'authentification et la gestion des sessions utilisent des bibliothèques approuvées
- [ ] Les messages d'erreur ne divulguent pas de détails internes
- [ ] Les événements de sécurité pertinents sont journalisés
- [ ] Les données sensibles ne sont pas journalisées
- [ ] Les opérations cryptographiques utilisent des algorithmes et bibliothèques approuvés
- [ ] Les contrôles d'accès sont côté serveur et appliqués par demande
- [ ] Les dépendances sont fixées et exemptes de vulnérabilités critiques connues

---

## Analyse statique de la sécurité applicative (SAST)

L'analyse statique automatisée est intégrée dans le processus de développement pour détecter les défauts de sécurité avant le déploiement.

**Exigences** :

- L'organisation déploie un outil SAST ([Outil SAST] — ex. SonarQube, Semgrep, CodeQL, Checkmarx ou équivalent) intégré dans le pipeline CI/CD.
- Les analyses SAST s'exécutent sur chaque demande de fusion ou de tirage vers une branche protégée.
- Les résultats SAST sont examinés avant la fusion. Les résultats de sévérité critique et élevée bloquent la fusion jusqu'à résolution ou acceptation explicite comme faux positifs avec justification documentée.
- Les jeux de règles SAST doivent couvrir, au minimum, les classes de vulnérabilités OWASP Top 10 et CWE/SANS Top 25.
- Les faux positifs sont documentés et supprimés selon la procédure de suppression ci-dessous. La suppression sans justification et revue par les pairs est interdite.
- La configuration de l'outil SAST et les jeux de règles sont révisés annuellement par le responsable développement et l'équipe sécurité.

**Procédure de suppression des faux positifs SAST** :

La suppression d'un résultat SAST comme faux positif sans revue par les pairs est interdite. Les développeurs peuvent supprimer par inadvertance de vraies vulnérabilités.

**Processus de demande de suppression** :
1. Le développeur identifie un résultat SAST supposément faux positif.
2. Le développeur documente dans la demande de suppression : identifiant du résultat, pourquoi le résultat est un faux positif (justification technique), extrait de code montrant pourquoi la règle ne s'applique pas, et méthode de suppression proposée (commentaire en ligne, fichier de configuration).
3. **Revue par les pairs requise** : Un autre développeur OU un Champion sécurité doit examiner la demande de suppression.
4. **Approbation de l'équipe sécurité** (pour les résultats Critiques/Élevés) : L'équipe sécurité doit approuver la suppression des résultats de sévérité Critique/Élevée. Les résultats Moyens/Faibles peuvent être approuvés par un pair examinateur.
5. Suppression appliquée : Commentaire en ligne + mise à jour de la configuration de l'outil (double documentation).

**Modèle de justification de suppression** (commentaire en ligne) :
```
// SAST-SUPPRESS: [Nom de l'outil] [Identifiant de règle] - [Date]
// Motif: [Brève explication pourquoi il s'agit d'un faux positif]
// Révisé par: [Nom de l'examinateur]
// Approuvé par: [Membre de l'équipe sécurité] (si Critique/Élevé)
```

**Audit des suppressions** :
- Revue trimestrielle : L'équipe sécurité échantillonne 20 % des résultats supprimés.
- Revalidation : Les suppressions sont-elles encore valides ? (code modifié, règle mise à jour, nouveau contexte ?)
- Révocation : Si la suppression n'est plus justifiée, supprimer la suppression et remédier au résultat.

**Indicateurs de suppression suivis** :
- Total des suppressions actives par sévérité.
- Taux de suppression (pourcentage de résultats SAST supprimés vs. remédiés).
- Âge moyen des suppressions (les suppressions anciennes sont révisées pour leur validité continue).
- Suppressions révoquées (combien de suppressions se sont avérées ultérieurement incorrectes).

**Signaux d'alerte** (déclenchent une revue de l'équipe sécurité) :
- Un développeur supprime >5 résultats dans une seule PR (inhabituel — suggère un abus).
- Une équipe supprime >20 % des résultats Critiques/Élevés (suggère un besoin d'ajustement des règles ou que l'équipe ne comprend pas l'outil).
- Suppression sans justification adéquate (« non applicable » générique — insuffisant).

Cible : <5 % des résultats SAST supprimés (95 %+ remédiés ou confirmés faux positifs avec justification documentée).

**Exigences de couverture SAST** :

| Classification de l'application | Fréquence d'analyse | Revue des résultats |
|----------------------------------|---------------------|---------------------|
| Applications en production | Par commit / demande de fusion | Avant la fusion |
| Outils internes | Par commit / demande de fusion | Avant la fusion |
| Preuves de concept | Hebdomadaire (si stockées dans les référentiels organisationnels) | Triage hebdomadaire |

---

## Formation au codage sécurisé

Les développeurs reçoivent une formation pour écrire du code sécurisé efficacement.

**Exigences de formation** :

| Type de formation | Public | Fréquence | Durée minimale |
|-------------------|--------|-----------|----------------|
| Fondamentaux du codage sécurisé | Tous les développeurs (y compris les sous-traitants) | Avant d'écrire du code de production | 4 heures |
| Mise à jour annuelle | Tous les développeurs | Annuellement | 2 heures |
| Formation Champion sécurité | Champions sécurité désignés | Initiale + annuelle | 8 heures initiale ; 4 heures mise à jour |
| Codage sécurisé spécifique au langage | Développeurs adoptant un nouveau langage | Avant l'usage en production de ce langage | 2 heures |

**Le contenu de la formation** doit couvrir au minimum :

- Les classes de vulnérabilités OWASP Top 10 et CWE/SANS Top 25.
- Les normes de codage sécurisé applicables au langage principal du développeur.
- La validation des entrées, l'encodage des sorties et la prévention des injections.
- Les schémas d'authentification, de gestion des sessions et de contrôle d'accès.
- La gestion des secrets et l'interdiction des identifiants codés en dur.
- L'utilisation sécurisée des bibliothèques cryptographiques.
- La gestion des dépendances et la sécurité de la chaîne d'approvisionnement.
- L'utilisation des outils SAST et SCA de l'organisation.

**Preuves de formation** : Les enregistrements de complétion sont maintenus dans [Système RH / LMS] et examinés trimestriellement par le responsable développement.

**Application des exigences de formation au codage sécurisé** :

Les exigences de formation sont appliquées par des conséquences progressives en cas de non-conformité :

**Exigences de complétion** (conformément au tableau des exigences de formation) :
- Fondamentaux du codage sécurisé : Avant d'écrire du code de production (nouvelles recrues, sous-traitants).
- Mise à jour annuelle : Dans les 30 jours suivant la date anniversaire (tous les développeurs).
- Spécifique au langage : Avant l'usage en production d'un nouveau langage.
- Formation Champion sécurité : Dans les 30 jours suivant la nomination.

**Conséquences de non-conformité** (progressives) :

| Jours de retard | Action | Autorité |
|----------------|--------|----------|
| **0–14 jours** | Rappel par courriel (automatisé) | Système |
| **15–30 jours** | Notification au responsable + deuxième rappel | Responsable développement |
| **31–60 jours** | Blocage de l'approbation des déploiements en production (le développeur ne peut pas approuver les PR vers les branches de production) | Responsable développement |
| **61–90 jours** | Suspension des privilèges de revue de code (le développeur ne peut pas examiner le code des autres) | Responsable développement + RSSI |
| **>90 jours** | Suspension de l'accès aux systèmes de production (ne peut pas déployer, ne peut pas accéder aux environnements de production) | RSSI |

**Exemptions temporaires** :
- Congé prolongé (parental, médical) : La date d'échéance de formation est repoussée à 30 jours après le retour.
- Besoin métier urgent (incident critique, urgence client) : Le RSSI accorde une extension de 30 jours avec justification documentée.

**Vérification de la complétion de la formation** :
- Automatisée : Le LMS/Système RH envoie le statut de complétion à [Outil de déploiement] ou [Plateforme de revue de code].
- Vérification pré-déploiement : Le pipeline CI/CD vérifie le statut de formation avant d'autoriser le déploiement en production (si le développeur est non conforme, déploiement bloqué avec le motif « Formation en retard — compléter [Nom de la formation] »).

**Indicateurs d'application de la formation** :
- Pourcentage de développeurs avec une formation à jour (cible : 95 %+ dans les 30 jours suivant la date d'échéance).
- Délai moyen de complétion de la formation (jours de la date d'échéance à la complétion).
- Nombre de développeurs avec des privilèges suspendus (cible : 0).

**Communication** :
- 30 jours avant la date d'échéance : Rappel « Formation bientôt due ».
- 7 jours avant la date d'échéance : Rappel « Formation due cette semaine ».
- À la date d'échéance : Notification « Formation en retard » au développeur + responsable.
- Rappels automatisés : Hebdomadaires jusqu'à complétion de la formation.

Application active à partir du [Date — suggéré : 3 mois après la date d'entrée en vigueur de la politique pour permettre aux développeurs existants de se mettre à jour].

---

## Pratiques de codage non sécurisé — Interdiction

Les pratiques de codage suivantes sont interdites :

| Pratique interdite | Motif | Alternative requise |
|--------------------|-------|---------------------|
| Mots de passe, clés API ou secrets codés en dur dans le code source | Secrets exposés via l'accès au référentiel ou les fuites de code | Utiliser des variables d'environnement ou la gestion des secrets approuvée ([Gestionnaire de secrets]) |
| Construction d'instructions SQL par concaténation de chaînes avec des données utilisateur | Vulnérabilité d'injection SQL | Utiliser des requêtes paramétrées ou des instructions préparées |
| Désérialisation de données non fiables sans validation | Risque d'exécution de code à distance | Valider et assainir avant la désérialisation ; utiliser des bibliothèques de désérialisation sécurisées |
| Utilisation d'algorithmes cryptographiques obsolètes ou non sécurisés (MD5, SHA-1, DES, RC4) | Faiblesses connues ; attaques par force brute ou de collision | Utiliser des algorithmes approuvés conformément à la politique cryptographique |
| Désactivation ou contournement de la validation des certificats TLS | Exposition aux attaques de l'homme du milieu | Appliquer la validation des certificats dans tous les environnements sauf les tests isolés |
| Exemples de code non approuvés copiés de sources publiques sans revue | Peuvent contenir des vulnérabilités, des portes dérobées ou des violations de licence | Examiner et adapter ; vérifier la compatibilité des licences ; analyser avec SAST |
| Journalisation de données sensibles (mots de passe, jetons, données personnelles) | Exposition de données via les fichiers journaux | Utiliser le masquage de données ou exclure les champs sensibles de la journalisation |
| Utilisation de `eval()` ou d'une exécution dynamique de code équivalente avec des données utilisateur | Vulnérabilité d'injection de code | Utiliser des alternatives sûres ; valider et assainir les entrées |

### Détection des secrets codés en dur (outillage obligatoire)

L'interdiction des secrets codés en dur dans le tableau ci-dessus doit être appliquée par une détection automatisée à plusieurs couches.

**Analyse pré-commit** (recommandé, poste de travail du développeur) :
- Outil : [git-secrets / Talisman / detect-secrets] installé sur les machines des développeurs.
- Analyse les commits pour détecter des schémas regex (clés API, clés privées, mots de passe, jetons).
- Bloque le commit si des secrets sont détectés (le développeur doit les supprimer avant de recommitter).
- Intégration : Tous les développeurs doivent être instruits d'installer le hook pré-commit lors de l'intégration.

**Analyse du pipeline CI/CD** (obligatoire, couche d'application) :
- Outil : [GitGuardian / TruffleHog / Gitleaks] intégré dans le pipeline CI/CD.
- Analyse chaque commit/PR pour détecter des schémas de secrets.
- Les compilations doivent échouer si des secrets sont détectés (pas de fusion jusqu'à remédiation).
- Alerte : L'équipe sécurité est notifiée immédiatement des secrets détectés (sévérité Critique).

**Analyse du référentiel** (périodique, détection historique) :
- Outil : GitHub Advanced Security / GitLab Secret Detection / scanner dédié.
- Analyse l'intégralité de l'historique du référentiel (pas seulement les nouveaux commits — détecte les secrets historiques).
- Fréquence : Analyse complète hebdomadaire du référentiel.
- Remédiation : Les secrets trouvés dans l'historique nécessitent : suppression de l'historique (git filter-repo), rotation du secret compromis (supposer compromis) et documentation de l'incident dans le journal des violations de secrets.

**Schémas de secrets minimaux détectés** :
- Clés AWS (AKIA..., schéma de clé d'accès secrète AWS).
- Clés API (schémas génériques de clés API, formats spécifiques aux fournisseurs).
- Clés privées (en-têtes RSA, SSH, clés PGP).
- Mots de passe de bases de données (chaînes de connexion avec identifiants intégrés).
- Jetons OAuth, secrets JWT, clés de chiffrement.

**Procédure de remédiation des secrets** :
1. **Immédiat** : Le développeur supprime le secret du code, valide la correction.
2. **Dans l'heure** : Le secret est renouvelé (supposer compromis même s'il n'est que dans la branche de développement).
3. **Dans les 24 heures** : L'historique du référentiel est nettoyé (si le secret a été validé — utiliser git filter-repo ou BFG Repo-Cleaner).
4. **Dans les 48 heures** : Rapport d'incident déposé auprès du RSSI (comment le secret a été validé, évaluation de l'impact, actions préventives).

**Exceptions** (rares) :
- Données de test avec des secrets factices (clairement marqués comme faux, non fonctionnels).
- Exemples de code dans la documentation (clairement marqués comme exemples, utilisant des valeurs de substitution telles que `votre-cle-api-ici`).

Documentation : La configuration des outils de détection des secrets est maintenue dans [Référentiel de configuration CI/CD] et révisée trimestriellement par l'équipe sécurité.

---

## Développement externalisé

Le code produit par des sous-traitants externes et des équipes de développement externalisées doit respecter les mêmes normes de codage sécurisé que le code développé en interne.

**Exigences contractuelles** :

- Les contrats doivent exiger le respect des normes de codage sécurisé et de cette politique de l'organisation.
- Les sous-traitants doivent fournir des preuves de formation au codage sécurisé pour leurs développeurs.
- Tout le code produit par les sous-traitants doit faire l'objet de la même revue de code et analyse SAST que le code interne.
- Les sous-traitants doivent remédier aux résultats de sécurité dans les SLA définis par l'organisation.
- L'organisation se réserve le droit d'auditer les pratiques de codage sécurisé des sous-traitants.

**Vérification** :

- Le code des sous-traitants est examiné par un développeur interne avant la fusion.
- Les résultats SAST et SCA pour le code produit par les sous-traitants sont visibles par l'équipe sécurité de l'organisation.
- Le code à risque élevé produit par les sous-traitants (authentification, autorisation, cryptographie, protection des données) fait l'objet d'une revue axée sur la sécurité par un Champion sécurité ou un architecte de sécurité.

**Assurance qualité du développement externalisé** :

En complément de la revue de code et de l'analyse continues, l'organisation réalise des audits périodiques du code produit par les sous-traitants pour vérifier la qualité et la conformité maintenues.

**Audit trimestriel des sous-traitants** (par engagement actif) :
- Taille de l'échantillon : 10 % du code produit par le sous-traitant (minimum 5 PR/MR) du trimestre précédent.
- Périmètre d'audit :
  - Conformité à la sécurité : Le code respecte-t-il les normes de codage sécurisé ? (validation des entrées, encodage des sorties, pas de secrets codés en dur, etc.)
  - Qualité du code : Lisibilité, maintenabilité, couverture des tests.
  - Documentation : Commentaires de code adéquats ? Décisions d'architecture documentées ?
- Auditeur : Développeur senior interne OU membre de l'équipe sécurité (pas la même personne qui a effectué la revue initiale — contrôle indépendant).
- Résultats : Documentés dans le Rapport d'audit du sous-traitant avec sévérité (Critique/Élevé/Moyen/Faible).

**Traitement des résultats d'audit** :
- Critique/Élevé : Escalader immédiatement à la direction du sous-traitant, remédier sous 14 jours, envisager une révision du contrat si un schéma émerge.
- Moyen/Faible : Retours fournis au sous-traitant, remédiation lors du prochain sprint/version.

**Score de performance des sous-traitants** :
- Indicateurs : Taux de résultats SAST/SCA (résultats par KLOC), taux de rejet des revues de code, taux de résultats d'audit, taux d'incidents de sécurité (incidents causés par le code du sous-traitant).
- Tableau de bord trimestriel : Partagé avec la direction du sous-traitant.
- Performance insuffisante : 3 trimestres consécutifs en dessous du seuil déclencheront une révision du contrat et une résiliation potentielle.

**Évaluation annuelle de la sécurité des sous-traitants** (complète) :
- Périmètre : Révision du processus de développement sécurisé, du programme de formation, des outils et de la qualité du code de l'année passée.
- Méthode : Questionnaire + entretien + analyse approfondie d'exemples de code.
- Résultat : Rapport d'évaluation de la sécurité des sous-traitants avec recommandations.
- Action : Les sous-traitants doivent traiter les recommandations Critiques/Élevées dans les 90 jours.

Documentation : Les rapports d'audit des sous-traitants sont conservés pour la durée du contrat + 3 ans.

---

## Cadre du programme de Champions sécurité

Les Champions sécurité sont essentiels à l'intégration de la sécurité au sein des équipes de développement. Le cadre suivant formalise le rôle de Champion sécurité avec une imputabilité claire, une allocation de temps et un soutien.

**Sélection et nomination** :
- Ratio : 1 Champion sécurité par équipe de développement (ou par 8 développeurs si les équipes sont plus grandes).
- Sélection : Volontaire préféré, nommé par le responsable développement en l'absence de volontaire.
- Qualifications : Développeur de niveau intermédiaire ou senior, intérêt pour la sécurité, bon communicant.
- Durée du mandat : 12 mois (renouvelable), avec un mentorat de 6 mois pour les nouveaux Champions.

**Responsabilités** (formelles, documentées dans la description du rôle) :
- Revues de code axées sur la sécurité (tout le code critique pour la sécurité dans l'équipe).
- Mentorat en codage sécurisé (aider les membres de l'équipe à comprendre les problèmes de sécurité).
- Triage SAST/SCA (première ligne de revue des résultats d'analyse, escalade vers l'équipe sécurité si nécessaire).
- Participation à la modélisation des menaces (pour les nouvelles fonctionnalités/changements significatifs).
- Liaison avec l'équipe sécurité (participation aux réunions mensuelles des Champions sécurité, transmission des mises à jour de sécurité à l'équipe).
- Support lors d'incidents de sécurité (assister l'équipe sécurité lors d'incidents affectant le code de l'équipe).

**Allocation de temps** :
- 10 % du temps de travail dédié aux fonctions de Champion sécurité (~4 heures/semaine).
- Le temps de revue de code est comptabilisé dans l'allocation des 10 %.
- Géré par le responsable développement (s'assurer que le Champion dispose du temps nécessaire, sans surcharge de travail fonctionnel).

**Formation et développement** :
- Formation initiale : 8 heures (modélisation des menaces, revue de code sécurisé, approfondissement OWASP Top 10, outils SAST/SCA).
- Mise à jour annuelle : 4 heures (nouvelles vulnérabilités, mises à jour des outils, études de cas).
- Optionnel : Participation à des conférences (OWASP AppSec, conférences axées sur la sécurité), cours en ligne.

**Soutien et ressources** :
- Réunion mensuelle de la communauté des Champions sécurité (apprentissage entre pairs, études de cas, questions-réponses avec l'équipe sécurité).
- Canal de communication dédié (soutien asynchrone, partage des connaissances).
- Accès à l'équipe sécurité pour l'escalade (SLA de réponse dans les 24 heures).
- Reconnaissance : Mention publique (réunions plénières, newsletters), possible prise en compte pour les primes/promotions.

**Indicateurs de performance** (mesurés trimestriellement) :
- Revues de code axées sur la sécurité complétées (cible : 100 % du code critique pour la sécurité).
- Résultats SAST triés dans les SLA (cible : 95 % dans les 48 heures).
- Incidents de sécurité impliquant le code de l'équipe (tendance à la baisse dans le temps).
- Taux de complétion de la formation à la sécurité des développeurs de l'équipe (le Champion encourage la formation de l'équipe).

**Planification de la succession** :
- Programme de doublure : Identifier le successeur 3 mois avant la fin du mandat, observation du Champion en poste.
- Transfert de connaissances : Documenté dans le Manuel du Champion sécurité.

**Gouvernance du programme** :
- Propriétaire du programme : RSSI ou Responsable de l'équipe sécurité.
- Révision trimestrielle du programme : Indicateurs, retours des Champions, améliorations du programme.
- Évaluation annuelle de la maturité du programme : Couverture (toutes les équipes ont-elles des Champions ?), engagement (les Champions sont-ils actifs ?), efficacité (les résultats de sécurité s'améliorent-ils ?).

Documentation : Le registre des Champions sécurité est maintenu dans [Système RH / Wiki] avec les noms, équipes, dates de nomination et complétion de formation.

---

## Gestion des exceptions

Les exceptions à cette politique doivent être demandées par écrit et doivent inclure :

- Les exigences spécifiques nécessitant une exception.
- La justification métier.
- Les contrôles compensatoires.
- La durée demandée pour l'exception (maximum 12 mois).
- L'évaluation et l'acceptation des risques.

Les exceptions doivent être approuvées par le responsable développement et le Responsable de la sécurité de l'information (obligatoire), plus le RSSI pour les exceptions d'applications en production. Toutes les exceptions actives sont révisées trimestriellement.

Lorsqu'il est techniquement impossible de satisfaire une exigence (ex. base de code héritée ne pouvant pas être refactorisée immédiatement), des contrôles compensatoires sont mis en œuvre, documentés, vérifiés par le Responsable de la sécurité de l'information et révisés annuellement.

---

## Définitions

| Terme | Définition |
|-------|------------|
| **CSP** | Politique de sécurité du contenu (Content Security Policy) — en-tête de réponse HTTP qui restreint les ressources qu'un navigateur est autorisé à charger pour une page, atténuant le XSS |
| **CWE** | Énumération des faiblesses communes (Common Weakness Enumeration) — liste développée par la communauté des types de faiblesses logicielles et matérielles |
| **Dépendance** | Une bibliothèque, un framework ou un composant tiers utilisé par le code applicatif |
| **Injection** | Classe de vulnérabilités où des données non fiables sont envoyées à un interpréteur dans le cadre d'une commande ou d'une requête (ex. injection SQL, XSS, injection de commandes) |
| **OWASP** | Open Worldwide Application Security Project — fondation à but non lucratif produisant des normes, outils et conseils pour la sécurité des applications |
| **Requête paramétrée** | Technique de requête de base de données qui sépare la logique SQL des données fournies par l'utilisateur, prévenant l'injection SQL |
| **SAST** | Analyse statique de la sécurité applicative (Static Application Security Testing) — analyse automatisée du code source pour identifier les défauts de sécurité sans exécuter l'application |
| **SBOM** | Catalogue de composants logiciels (Software Bill of Materials) — inventaire lisible par machine de tous les composants, bibliothèques et dépendances d'une application logicielle |
| **SCA** | Analyse de la composition logicielle (Software Composition Analysis) — analyse automatisée des dépendances tierces pour détecter les vulnérabilités connues et les risques de licence |
| **Champion sécurité** | Développeur avec une formation spécialisée en sécurité qui agit en tant que référent sécurité au sein d'une équipe de développement |
| **TLS** | Transport Layer Security — protocole cryptographique pour sécuriser les données en transit |
| **XSS** | Scripts intersites (Cross-Site Scripting) — vulnérabilité permettant aux attaquants d'injecter des scripts malveillants dans des pages web consultées par d'autres utilisateurs |

---

## Rôles et responsabilités

| Rôle | Responsabilités |
|------|----------------|
| **RSSI** | Propriété de la politique ; approbation des exceptions pour les applications en production ; supervision de la conformité au codage sécurisé ; révision annuelle de la politique ; communication à la direction générale ; gouvernance du programme des Champions sécurité |
| **Responsable développement** | Maintenance des normes de codage sécurisé (par langage) ; application des revues de code ; sélection et configuration des outils SAST/SCA ; coordination de la formation des développeurs ; communication de la conformité au RSSI ; garantie de l'allocation de temps des Champions sécurité |
| **Responsable de la sécurité de l'information** | Maintenance de la politique ; revue des exceptions ; surveillance de la sécurité et investigation des incidents ; coordination des audits ; communication trimestrielle de la conformité au RSSI |
| **Champions sécurité** | Revues de code axées sur la sécurité ; mentorat en codage sécurisé au sein des équipes de développement ; promotion des normes de codage sécurisé ; triage des résultats SAST/SCA ; participation à la modélisation des menaces ; escalade des problèmes de sécurité vers l'équipe sécurité |
| **Équipe sécurité** | Gestion des outils SAST/SCA et mises à jour des jeux de règles ; revue de code axée sur la sécurité pour les changements à risque élevé ; coordination des tests de sécurité ; réponse aux incidents pour les vulnérabilités au niveau du code ; approbation des suppressions SAST pour les résultats Critiques/Élevés ; participation aux audits des sous-traitants |
| **Ingénieurs DevOps** | Intégration des outils SAST et SCA dans le pipeline CI/CD ; application des portes de sécurité du pipeline de compilation ; infrastructure de gestion des secrets ; intégration des outils d'analyse des secrets |
| **Développeurs individuels et sous-traitants** | Respect des normes de codage sécurisé ; participation aux revues de code ; remédiation rapide des résultats de sécurité ; complétion de la formation au codage sécurisé ; signalement des défauts de sécurité ; installation du hook pré-commit |

---

## Preuves

Les preuves suivantes démontrent la conformité à cette politique :

| N° | Preuve | Responsable | Fréquence | Conservation |
|----|--------|-------------|-----------|-------------|
| 1 | **Registre des normes de codage sécurisé** (langages, frameworks et références de codage approuvés) | Responsable développement | Maintenu en continu ; révisé annuellement | Version actuelle + 3 ans |
| 2 | **Résultats des analyses SAST** (journaux d'exécution des outils, résultats, justifications des faux positifs) | Responsable développement / DevOps | Par demande de fusion ; examiné mensuellement | 2 ans |
| 3 | **Résultats des analyses SCA des dépendances** (résultats de vulnérabilités, sorties SBOM, enregistrements de remédiation) | Responsable développement / DevOps | Par compilation ; examiné mensuellement | 2 ans |
| 4 | **Enregistrements des revues de code** (revues de PR, listes de contrôle de revue de sécurité, enregistrements d'approbation) | Responsable développement | Par modification de code | 3 ans |
| 5 | **Enregistrements des revues de code axées sur la sécurité** pour les changements à risque élevé (authentification, autorisation, cryptographie) | Champions sécurité / Équipe sécurité | Par changement applicable | 3 ans |
| 6 | **Dossiers de complétion de la formation au codage sécurisé** (fondamentaux, mise à jour, spécifique au langage, Champion sécurité) | Responsable développement / RH | Annuellement ; par intégration | Durée de l'emploi + 3 ans |
| 7 | **Enregistrements de remédiation des vulnérabilités des dépendances** (suivi de résultat à clôture avec conformité aux SLA) | Responsable développement | Par résultat | 3 ans |
| 8 | **Enregistrements de configuration des outils SAST/SCA** (jeux de règles, contrôles activés, justifications de suppression) | Équipe sécurité / DevOps | Révisé annuellement | Version actuelle + 1 an |
| 9 | **Enregistrements de violations de pratiques interdites** (incidents de secrets codés en dur, schémas non sécurisés détectés et remédiés) | Équipe sécurité | Par incident | 3 ans |
| 10 | **Registre des exceptions** (demandes, approbations, contrôles compensatoires, révisions trimestrielles) | Responsable de la sécurité de l'information | Maintenu en continu ; révisé trimestriellement | Durée de l'exception + 3 ans |
| 11 | **Preuves de codage sécurisé du développement externalisé** (dossiers de formation des sous-traitants, enregistrements de revue de code, conformité aux SLA, rapports d'audit trimestriels, évaluations annuelles de sécurité) | Responsable développement / Achats | Par engagement de sous-traitant ; audits trimestriels | Durée du contrat + 3 ans |
| 12 | **Enregistrements de révision annuelle des normes de codage sécurisé** (date de révision, modifications apportées, approbation) | Responsable développement | Annuellement | 3 ans |
| 13 | **Tendances des résultats SAST/SCA** — Rapports mensuels montrant les taux de résultats, les délais de remédiation et les résultats ouverts par sévérité pour l'échantillonnage d'audit SOC 2 | Équipe sécurité | Mensuel | 2 ans |

---

# Conformité à la politique

## Mesure de la conformité

L'équipe de management de la sécurité de l'information vérifie la conformité à cette politique par diverses méthodes, notamment les rapports des outils SAST/SCA, les enregistrements de complétion des revues de code, les enregistrements de complétion de la formation, les résultats des audits de dépendances, les audits internes et externes, et les retours au propriétaire de la politique.

**Indicateurs de conformité** :

| Indicateur | Cible | Fréquence de mesure |
|------------|-------|---------------------|
| Modifications de code avec revue par les pairs complétée avant la fusion | 100 % | Mensuel |
| Analyses SAST exécutées par demande de fusion (applications en production) | >= 95 % | Mensuel |
| Résultats SAST Critiques/Élevés remédiés avant la fusion ou documentés comme faux positifs | >= 95 % | Mensuel |
| Vulnérabilités de dépendances Critiques/Élevées remédiées dans les SLA | >= 90 % | Mensuel |
| Développeurs avec une formation au codage sécurisé à jour | >= 95 % | Trimestriel |
| Secrets codés en dur détectés et remédiés dans les 24 heures | 100 % | Par incident |

**Score de conformité** :

| Composant | Pondération | Calcul |
|-----------|-------------|--------|
| Conformité des revues de code | 30 % | (Modifications de code avec revue complétée) / Total des modifications de code × 100 |
| Couverture SAST | 25 % | (PR avec analyse SAST réussie) / Total des PR × 100 |
| Sécurité des dépendances | 25 % | (Vulnérabilités Critiques/Élevées remédiées dans les SLA) / Total des résultats Critiques/Élevés × 100 |
| Conformité de la formation | 20 % | (Développeurs avec formation à jour) / Total des développeurs × 100 |

**Traitement de la non-conformité** : En dessous de 70 %, escalade immédiate vers le RSSI et plan de remédiation requis. Entre 70 et 89 %, supervision du Responsable de la sécurité de l'information avec revues mensuelles. À 90 % et au-dessus, surveillance trimestrielle standard.

## Exceptions

Toute exception à cette politique doit être approuvée et enregistrée à l'avance par le Responsable de la sécurité de l'information, avec acceptation documentée du risque, contrôles compensatoires et date de révision définie (maximum 12 mois). Les exceptions sont communiquées à l'équipe de revue de direction.

## Non-conformité

Tout employé reconnu coupable d'avoir violé cette politique peut faire l'objet de mesures disciplinaires pouvant aller jusqu'au licenciement. Les violations de la politique sont documentées, investiguées par le Responsable de la sécurité de l'information et communiquées au RSSI.

## Amélioration continue

Cette politique est révisée et mise à jour dans le cadre du processus d'amélioration continue. Les révisions tiennent compte des classes de vulnérabilités émergentes, des évolutions de l'OWASP Top 10 et du CWE/SANS Top 25, des nouveaux langages ou frameworks adoptés par l'organisation, de l'évolution des outils SAST/SCA, des constatations d'audit et des enseignements tirés des incidents de sécurité impliquant des vulnérabilités au niveau applicatif.

---

# Domaines de la norme ISO 27001 couverts

Politique de codage sécurisé — Correspondance avec les contrôles ISO 27001

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership et engagement | 5.1 Politiques de sécurité de l'information |
| Clause 5.2 Politique | 5.4 Responsabilités de la direction |
| Clause 6.2 Objectifs de sécurité de l'information | 5.36 Conformité aux politiques, règles et normes |
| Clause 7.3 Sensibilisation | 6.3 Sensibilisation, formation et éducation à la sécurité de l'information |
| | 6.4 Processus disciplinaire |
| | 8.4 Accès au code source |
| | 8.25 Cycle de développement sécurisé |
| | 8.26 Exigences de sécurité des applications |
| | **8.28 Codage sécurisé** |
| | 8.29 Tests de sécurité dans le développement et l'acceptation |

**Cadre réglementaire et juridique** :

| Cadre | Pertinence |
|-------|-----------|
| nLPD suisse (revDSG) | Art. 7 — Protection des données dès la conception et par défaut ; Art. 8 — Mesures techniques et organisationnelles ; le codage sécurisé en tant que mesure technique préventive |
| OPDo suisse (Ordonnance sur la protection des données) | Art. 1–3 — Exigences minimales en matière de sécurité des données, y compris les contrôles au niveau applicatif |
| RGPD de l'UE (si applicable) | Art. 25 — Protection des données dès la conception et par défaut ; Art. 32 — Sécurité du traitement |
| ISO/IEC 27001:2022 | Contrôle Annexe A 8.28 — Codage sécurisé |
| ISO/IEC 27002:2022 | Section 8.28 — Conseils de mise en œuvre pour le codage sécurisé |
| NIST SP 800-218 (SSDF) v1.1 | PW.4 — Créer du code source adhérant aux pratiques de codage sécurisé ; PW.5 — Configurer le processus de compilation de manière sécurisée ; PW.6 — Examiner et tester le code |
| NIST SP 800-53 Rév. 5 | SA-15 (Processus de développement, normes et outils), SA-16 (Formation fournie par le développeur), SA-17 (Architecture et conception de sécurité fournies par le développeur) |
| CIS Controls v8 | 16.1 (Processus de développement applicatif sécurisé), 16.2 (Gérer l'architecture logicielle), 16.4 (Sécuriser les logiciels développés sur mesure), 16.12 (Mettre en œuvre des contrôles de sécurité au niveau du code) |
| OWASP Top 10 (2021) | A01–A10 — Catégories de risques de sécurité des applications web traitées par les pratiques de codage sécurisé |
| CWE/SANS Top 25 (2025) | Faiblesses logicielles les plus dangereuses traitées par la validation des entrées, l'encodage des sorties et les normes de codage sécurisé |

---

<!-- QA_VERIFIED: 2026-03-29 -->
