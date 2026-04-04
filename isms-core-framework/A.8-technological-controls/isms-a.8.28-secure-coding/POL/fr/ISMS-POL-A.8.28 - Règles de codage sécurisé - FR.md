<!-- ISMS-CORE:POLICY:ISMS-POL-A.8.28-FR:framework:POL:a.8.28 -->
**ISMS-POL-A.8.28 – Règles de codage sécurisé**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Politique de codage sécurisé |
| **Type de document** | Politique |
| **Identifiant du document** | ISMS-POL-A.8.28 |
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
| 1.0 | [Date] | RSSI | Politique initiale pour la première certification ISO 27001:2022 |

**Cycle de révision** : Annuel
**Prochaine date de révision** : [Date d'entrée en vigueur + 12 mois]

**Chaîne d'approbation** :

- Principale : Responsable de la Sécurité des Systèmes d'Information (RSSI)
- Secondaire : Directeur de la Technologie (DT)
- Conformité : Responsable juridique/conformité
- Autorité finale : Direction générale

**Documents connexes** :

- ISMS-POL-00 (Cadre d'applicabilité réglementaire)
- ISMS-IMP-A.8.28.1-UG/TG (Spécification d'évaluation SDLC)
- ISMS-IMP-A.8.28.2-UG/TG (Normes et outils)
- ISMS-IMP-A.8.28.3-UG/TG (Revue de code et tests de sécurité)
- ISMS-IMP-A.8.28.4-UG/TG (Logiciels tiers et open source)
- ISMS-CTX-A.8.28 (Directives de codage sécurisé par langage)
- ISMS-REF-A.8.28 (Référence technique de revue de code)
- ISO/IEC 27001:2022 Contrôle A.8.28

---

## Résumé exécutif

Cette politique établit les exigences de [Organisation] pour le développement logiciel sécurisé, conformément au Contrôle A.8.28 de la norme ISO/IEC 27001:2022 (Codage sécurisé).

**Objet** : Définir QUELS contrôles de codage sécurisé sont requis et QUI en est responsable. Les détails techniques de mise en œuvre (COMMENT) sont documentés dans ISMS-IMP-A.8.28.

**Périmètre** : Toutes les activités de développement logiciel, notamment le développement interne, externalisé et la personnalisation de logiciels acquis. S'applique à tous les types d'applications, toutes les phases de développement et tous les langages de programmation.

**Risque métier traité** : Vulnérabilités logicielles conduisant à des violations de données, des interruptions de service, des pertes financières, des atteintes à la réputation et des sanctions réglementaires.

**Alignement réglementaire** : Conformément à ISMS-POL-00 :

- **Obligatoire** : nLPD suisse, RGPD de l'UE (Art. 32), ISO 27001:2022
- **Informatif** : OWASP Top 10, NIST SP 800-218 SSDF, CWE Top 25

---

# Alignement sur les contrôles et périmètre

## Contrôle A.8.28 de la norme ISO/IEC 27001:2022

**Énoncé du contrôle** :
> *Des principes de codage sécurisé doivent être appliqués au développement logiciel.*

**Objectif du contrôle** : Réduire le nombre de vulnérabilités de sécurité dans les logiciels en appliquant des principes de codage sécurisé tout au long du cycle de vie du développement.

**Ce contrôle traite** :

- La prévention des vulnérabilités pendant le développement (sécurité en amont)
- La prévention des vulnérabilités courantes (injection, XSS, failles d'authentification, etc.)
- Les principes de conception et d'architecture sécurisées
- La formation et la compétence des développeurs
- La revue de code et les tests de sécurité
- La sécurité des composants tiers

## Définition du périmètre

**Dans le périmètre** :

- Tout développement logiciel (nouveaux projets, maintenance, améliorations, correctifs)
- Tous les types de développement (interne, externalisé, contractuel, acquis)
- Tous les types d'applications (web, mobile, API, bureau, embarqué, sans serveur)
- Tous les langages et frameworks utilisés par [Organisation]
- Environnements de développement, de préproduction et de production

**Hors périmètre** :

- Configuration de l'infrastructure (voir A.8.9 Gestion de la configuration)
- Sécurité réseau (voir A.8.20-22 Sécurité des réseaux)
- Gestion des clés cryptographiques (voir A.8.24 Cryptographie)

---

# Exigences de développement sécurisé

## Sécurité en amont du développement

**Définition des exigences de sécurité** :

- Les exigences de sécurité DOIVENT être définies pour tous les projets traitant des données sensibles
- Exigences dérivées de la classification des données, des besoins réglementaires et du paysage des menaces
- Critères d'acceptation de sécurité définis avant le début du développement

**Exigences de modélisation des menaces** :

| Type de projet | Exigence |
|---------------|----------|
| Nouvelles applications traitant des données sensibles | Obligatoire |
| Modifications architecturales majeures | Obligatoire |
| Applications/API exposées au public | Obligatoire |
| Traitement de données financières/DCP | Obligatoire |
| Outils internes (exposition limitée) | Recommandé |

**Documentation du modèle de menaces** :

- Architecture système et flux de données
- Frontières de confiance et surface d'attaque
- Menaces identifiées avec évaluation des risques
- Contrôles d'atténuation mappés aux menaces
- Approche de validation

**Méthodologie de modélisation des menaces** : [Organisation] DOIT utiliser une méthodologie reconnue (STRIDE, PASTA, DREAD ou OWASP Threat Dragon). La sélection de méthodologie est documentée par application ; la cohérence au sein des familles d'applications est encouragée.

**Vérification** : Modèles de menaces révisés par l'Équipe de sécurité applicative ; approbation documentée dans le Classeur 1. Les applications critiques nécessitent la validation du RSSI.

**Revue d'architecture sécurisée** :

- Requise avant le sprint 1 de développement pour les nouvelles applications
- Requise pour les changements architecturaux significatifs
- Approbation de l'Architecte de sécurité ou de l'Équipe de sécurité applicative requise
- Les applications critiques nécessitent l'approbation du RSSI

## Formation à la sécurité des développeurs

**Exigences de formation** :

| Type de formation | Public | Fréquence |
|------------------|--------|-----------|
| Fondamentaux du codage sécurisé | Tous les développeurs | Initial + Annuel |
| Sécurité spécifique au langage | Développeurs utilisant le langage | Initial |
| Formation avancée Champions de la sécurité | Champions de la sécurité | Trimestrielle |
| Mises à jour OWASP Top 10 | Tous les développeurs | À chaque mise à jour |

**Vérification de la formation** :

- Complétion suivie dans le système de gestion de la formation de l'entreprise
- Évaluations des connaissances requises avec note minimale de réussite : 85 % pour les fondamentaux du codage sécurisé et la formation spécifique au langage ; 80 % pour la formation de sensibilisation (mises à jour OWASP Top 10)
- Certificats de complétion conservés comme preuves
- Non-conformité escaladée vers le Responsable du développement après 30 jours ; notification du RSSI après 60 jours

**Vérification** : Rapports de complétion de formation générés trimestriellement depuis le LMS ; taux de complétion suivis comme ICP (cible : 100 %).

## Normes de codage sécurisé

**Exigences universelles** (tous les langages) :

**Validation des entrées** :

- Valider TOUTES les entrées (utilisateur, API, fichier, environnement, base de données)
- Validation par liste d'autorisation préférée à la liste de blocage
- Validation côté serveur obligatoire (la validation côté client est uniquement pour l'expérience utilisateur)
- Rejeter les entrées invalides ; ne pas tenter d'assainissement

**Encodage des sorties** :

- Encodage approprié au contexte (HTML, JavaScript, URL, SQL)
- Utiliser les fonctions d'encodage fournies par le framework
- Prévenir les XSS par un encodage des sorties approprié

**Authentification et gestion des sessions** :

- Hachage robuste des mots de passe (bcrypt, Argon2, scrypt)
- Ne jamais stocker les mots de passe en clair
- Jetons de session cryptographiquement aléatoires
- Délai d'expiration des sessions et invalidation à la déconnexion
- Support AMF pour les applications sensibles

**Autorisation** :

- Application côté serveur pour chaque requête
- Principe du moindre privilège
- Prévention des vulnérabilités IDOR
- Mise en œuvre RBAC ou ABAC

**Cryptographie** :

- Uniquement des algorithmes standard du secteur (AES-256, RSA-2048+)
- Ne jamais implémenter de cryptographie personnalisée
- Gestion appropriée des clés (clés séparées du code)
- TLS 1.2+ pour les données en transit (TLS 1.3 de préférence)

**Gestion des erreurs** :

- Messages d'erreur génériques pour les utilisateurs
- Journalisation détaillée côté serveur (aucune donnée sensible dans les journaux)
- Événements de sécurité journalisés pour la surveillance

**Directives spécifiques aux langages** : Voir ISMS-CTX-A.8.28 pour les patterns Python, JavaScript, Java, C#, Go, SQL.

## Pratiques interdites

Les pratiques suivantes sont **INTERDITES** :

- Secrets codés en dur (clés API, mots de passe, jetons) dans le code source
- Fonctions dépréciées/non sécurisées (gets(), strcpy(), MD5 pour les mots de passe, eval() avec entrée utilisateur)
- Construction de requêtes SQL par concaténation de chaînes
- Contrôles de sécurité désactivés en production
- Poussée de secrets vers les systèmes de contrôle de version (même dans l'historique)
- Ignorer les résultats des outils de sécurité sans exception documentée

## Gestion des secrets

- AUCUN secret codé en dur dans le code source
- Secrets stockés dans des systèmes de gestion des secrets approuvés (par ex. HashiCorp Vault, AWS Secrets Manager, Azure Key Vault)
- Analyse des secrets intégrée dans le pipeline CI/CD (par ex. GitLeaks, TruffleHog, GitHub Secret Scanning)
- Crochets pré-commit configurés pour bloquer les commits contenant des secrets détectés
- Secrets tournés régulièrement et lors du départ d'un employé

**Réponse à la détection de secrets** :

- Blocage pré-commit : le développeur doit supprimer le secret avant que le commit ne se poursuive
- Détection CI/CD : la construction échoue ; le secret doit être supprimé et tourné avant la fusion
- Détection post-commit : rotation immédiate requise ; incident journalisé

## Composants tiers et open source

**Sélection des composants** :

- Évaluer la posture de sécurité avant adoption
- Préférer les bibliothèques bien maintenues et largement utilisées
- Vérifier les vulnérabilités connues avant inclusion
- Vérifier la compatibilité des licences

**Gestion continue** :

- Maintenir un inventaire des composants (Nomenclature des composants logiciels — SBOM)
- Surveiller les vulnérabilités via des outils SCA
- Appliquer les correctifs/mises à jour dans les SLA définis
- Supprimer les dépendances inutilisées

---

# Revue de code et tests de sécurité

## Exigences de revue de code

**Revue par les pairs** :

- Toutes les modifications de code de production nécessitent une revue par les pairs
- Revue axée sur la sécurité pour les modifications touchant l'authentification, l'autorisation, la cryptographie, la gestion des entrées
- Protection des branches empêchant la fusion sans approbation

**Critères de revue de sécurité** : Voir ISMS-REF-A.8.28 pour la liste de contrôle détaillée.

## Exigences de tests de sécurité

**Tests de sécurité des applications statiques (SAST)** :

- Intégrés dans le pipeline CI/CD (par ex. SonarQube, Checkmarx, Snyk Code, Semgrep)
- Exécutés à chaque construction/commit ; la construction échoue sur les résultats Critiques/Élevés
- Résultats triés et remédiés selon les SLA
- Faux positifs documentés et ajustés (cible : taux de faux positifs < 20 %)

**Tests de sécurité des applications dynamiques (DAST)** :

- Exécutés sur les environnements de préproduction/assurance qualité (par ex. OWASP ZAP, Burp Suite, Qualys WAS)
- Requis avant la mise en production pour les applications web
- Tests de sécurité des API pour toutes les API (par ex. tests de sécurité Postman, OWASP API Security)

**Analyse de la composition logicielle (SCA)** :

- Intégrée dans le pipeline CI/CD (par ex. Snyk, Dependabot, OWASP Dependency-Check)
- Surveille toutes les dépendances tierces
- Alertes sur les nouvelles vulnérabilités dans les dépendances ; la construction échoue sur les résultats Critiques/Élevés

**Vérification de l'intégration des outils** :

- Configuration du pipeline CI/CD documentée dans le Classeur 2
- Sélection et statut de déploiement des outils suivis
- Rapports d'analyse des 90 derniers jours disponibles sur demande
- Journaux du pipeline démontrant l'exécution automatisée

**Tests d'intrusion** :

| Type d'application | Fréquence | Périmètre |
|-------------------|-----------|-----------|
| Critique/Haut risque | Annuel minimum | Application complète (toutes les catégories OWASP Top 10) |
| Exposée sur Internet | Annuel minimum | Surface d'attaque externe (authentification, API, gestion des entrées) |
| Après modifications majeures | Selon les besoins | Composants modifiés + points d'intégration |

**Exigences de retests** :

- Les résultats Critiques et Élevés DOIVENT être retestés après remédiation pour vérifier l'efficacité
- Le retest peut être limité aux composants affectés
- Les résultats Moyens et Faibles vérifiés via des tests de sécurité internes (DAST ou tests manuels) sauf exigence client ou réglementaire contraire
- Preuves de retest documentées dans le Classeur 3

## SLA de remédiation des vulnérabilités

| Gravité | Score CVSS | SLA de remédiation |
|---------|------------|-------------------|
| **Critique** | 9,0-10,0 | 7 jours |
| **Élevé** | 7,0-8,9 | 30 jours |
| **Moyen** | 4,0-6,9 | 90 jours |
| **Faible** | 0,1-3,9 | Au mieux / prochaine version |

**Mécanisme de suivi des SLA** :

- Vulnérabilités suivies dans le système de gestion des issues (par ex. Jira, Azure DevOps) avec gravité et date de découverte
- Ancienneté calculée automatiquement ; éléments en retard signalés
- Revue hebdomadaire de la conformité aux SLA par l'Équipe de sécurité applicative
- Rapport mensuel des SLA au Responsable du développement et au RSSI

**Processus d'exception** :

- Justification métier documentée requise
- Évaluation des risques et contrôles compensatoires (par ex. règle WAF, isolation réseau, surveillance renforcée)
- Approbation : Moyen par le Responsable de la sécurité, Élevé/Critique par le RSSI
- Durée maximale de l'exception : 90 jours (renouvelable)
- Exceptions suivies dans le registre central des exceptions (Classeur 3)

**Vérification** : Tableau de bord de l'ancienneté des vulnérabilités révisé hebdomadairement ; taux de conformité aux SLA suivis comme ICP (Critique ≥ 95 %, Élevé ≥ 90 %).

---

# Rôles et responsabilités

## Direction générale

- Approuver la politique de codage sécurisé
- Allouer le budget pour les outils de sécurité et la formation
- Réviser les métriques de sécurité trimestriellement
- Point d'escalade pour les vulnérabilités critiques

## RSSI

- Responsabilité globale du programme de développement sécurisé
- Approuver la sélection des outils de sécurité
- Approuver les exceptions à haut risque
- Réviser les tendances de vulnérabilités et le statut de remédiation

## Équipe de sécurité applicative

- Maintenir les normes de codage sécurisé
- Réaliser les revues des modèles de menaces
- Gérer les outils de tests de sécurité (SAST, DAST, SCA)
- Trier et suivre les vulnérabilités
- Conduire la formation à la sécurité
- Soutenir la réponse aux incidents pour les vulnérabilités du code

## Responsables du développement

- S'assurer que les développeurs complètent la formation à la sécurité
- Allouer du temps aux activités de sécurité dans les sprints
- Appliquer les exigences de revue de code
- Escalader les résultats de sécurité non résolus

## Champions de la sécurité

- Défenseurs de la sécurité intégrés dans les équipes de développement
- Premier point de contact pour les questions de sécurité
- Participer à la modélisation des menaces
- Promouvoir les pratiques de codage sécurisé

**Structure du programme** :

- Cible de couverture : Minimum 1 Champion de la sécurité par équipe de développement (ou par 10 développeurs)
- Sélection : Nommé par le Responsable du développement, approuvé par l'Équipe de sécurité applicative
- Désignation : Rôle formel documenté dans le système RH ; allocation de temps de 10-20 % pour les activités de sécurité
- Formation : Formation avancée trimestrielle en sécurité (au-delà de la formation standard)
- Reconnaissance : Contributions des Champions incluses dans les évaluations de performance

## Développeurs

- Compléter la formation à la sécurité requise
- Respecter les normes de codage sécurisé
- Traiter les résultats de sécurité dans leur code
- Participer aux revues de code
- Signaler les préoccupations de sécurité
- Ne pas pousser de secrets vers les référentiels

## Développeurs tiers

- Se conformer aux normes de codage sécurisé de [Organisation]
- Compléter la formation à la sécurité requise
- Se soumettre aux revues de code et aux tests de sécurité
- Remédier aux vulnérabilités dans les SLA

**Application de la conformité** :

- Obligation contractuelle : Exigences de codage sécurisé incluses dans les accords fournisseurs (conformément à A.5.20)
- Intégration : Les développeurs tiers complètent la formation au codage sécurisé avant l'octroi de l'accès
- Revue de code : Tout le code tiers soumis aux mêmes normes de revue que le code interne
- Tests de sécurité : Livrables tiers analysés avec SAST/SCA avant acceptation
- Attestation : Attestation de conformité annuelle signée par la direction du fournisseur

---

# Gouvernance et conformité

## Surveillance de la conformité à la politique

**Surveillance continue** :

- Résultats SAST/DAST/SCA suivis dans le tableau de bord de sécurité
- Ancienneté des vulnérabilités surveillée
- Complétion de la formation suivie

**Évaluation périodique** :

- Trimestrielle : Métriques de vulnérabilités, conformité à la formation, revue des exceptions
- Annuelle : Évaluation complète du programme de codage sécurisé (ISMS-IMP-A.8.28)

## Gestion de la non-conformité

**Réponse progressive** :

1. Première occurrence : Formation et avertissement documenté
2. Occurrence répétée : Escalade vers le responsable
3. Non-conformité persistante : Privilèges de développement restreints
4. Violation délibérée : Mesure disciplinaire conformément aux politiques RH

## Gestion des exceptions

- Toutes les exceptions nécessitent une justification métier documentée
- Évaluation des risques et contrôles compensatoires obligatoires
- Autorité d'approbation basée sur le niveau de risque
- Exceptions suivies dans le registre central des exceptions (Classeur 3)
- Durée maximale : 90 jours (renouvelable avec ré-approbation)

**Critères d'adéquation des contrôles compensatoires** :

- **Efficacité** : Le contrôle atténue le chemin d'exploitation spécifique
- **Fiabilité** : Le contrôle fonctionne en continu avec alerte en cas de défaillance
- **Vérifiabilité** : L'opération du contrôle peut être testée et surveillée
- **Périmètre** : Le contrôle couvre tous les systèmes/flux de données affectés

## Métriques et reporting

**Indicateurs clés de performance (ICP)** :

| Métrique | Cible | Fréquence | Source des données |
|---------|-------|-----------|-------------------|
| Complétion de la formation des développeurs | 100 % | Trimestrielle | Rapports de complétion LMS |
| Couverture des revues de code | ≥ 95 % | Mensuelle | Statistiques de fusion Git/PR |
| Vulnérabilités critiques dans les SLA | ≥ 95 % | Mensuelle | Rapport d'ancienneté du suivi des vulnérabilités |
| Vulnérabilités élevées dans les SLA | ≥ 90 % | Mensuelle | Rapport d'ancienneté du suivi des vulnérabilités |
| Couverture de modélisation des menaces (apps à haut risque) | ≥ 90 % | Trimestrielle | Classeur 1 — inventaire des applications |

---

# Intégration avec les autres contrôles

## Correspondance réglementaire

| Exigence | nLPD suisse | RGPD UE | ISO 27001 |
|----------|------------|---------|-----------|
| Développement sécurisé | Art. 8 | Art. 32 | A.8.28 |
| Tests de sécurité | Art. 8 | Art. 32 | A.8.29 |
| Gestion des vulnérabilités | Art. 8 | Art. 32 | A.8.8 |

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

*Cette politique établit les exigences pour le développement logiciel sécurisé. Les procédures de mise en œuvre sont documentées dans ISMS-IMP-A.8.28 (UG/TG). Les directives spécifiques aux langages sont dans ISMS-CTX-A.8.28. Les listes de contrôle de revue de code sont dans ISMS-REF-A.8.28.*

<!-- QA_VERIFIED: 2026-04-02 -->
