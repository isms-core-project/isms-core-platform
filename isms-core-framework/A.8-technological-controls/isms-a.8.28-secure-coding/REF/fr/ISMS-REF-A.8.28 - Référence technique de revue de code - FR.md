<!-- ISMS-CORE:REF:ISMS-REF-A.8.28-FR-code-review-technical-reference:framework:REF:a.8.28 -->
**ISMS-REF-A.8.28 — Référence technique de revue de code**

**Contrôle du document — ISMS-REF-A.8.28**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Référence technique de revue de code |
| **Type de document** | Référence technique (REF) |
| **Identifiant du document** | ISMS-REF-A.8.28 |
| **Créateur du document** | Responsable de la sécurité applicative |
| **Propriétaire du document** | Responsable de la sécurité applicative |
| **Approuvé par** | Responsable de la sécurité applicative |
| **Date de création** | [Date] |
| **Version** | 1.0 |
| **Date de version** | [Date] |
| **Classification** | Interne |
| **Statut** | Brouillon |

---

## Avertissement

**CRITIQUE** : Il s'agit d'un document de référence informatif qui ne fait **PAS** partie du cadre formel de politique SMSI.

Les informations contenues fournissent des conseils techniques et des détails méthodologiques mais **n'établissent PAS d'exigences obligatoires**.

**Les exigences de politique contraignantes** sont définies dans **ISMS-POL-A.8.28 (Politique de codage sécurisé)**.

**Objectif** : Soutenir l'implémentation de la revue de code en fournissant :

- Des listes de contrôle détaillées de revue de code de sécurité
- Des comparaisons de méthodes et des conseils
- Des approches de revue basées sur les risques
- Des meilleures pratiques d'implémentation

**Utilisation** : Référence technique pour les réviseurs de code, les Champions de la sécurité et les équipes de développement.

---

# Objectif et portée

## Objectif de la référence

Ce document fournit des **critères de sécurité exploitables** pour les réviseurs de code. Il opérationnalise les exigences de revue de code d'ISMS-POL-A.8.28 Section 2.3, traduisant la politique en étapes de revue pratiques.

*« Le premier principe est que vous ne devez pas vous tromper vous-même — et vous êtes la personne la plus facile à tromper. » — Richard Feynman*

**Objectif** : Permettre aux réviseurs de code d'identifier systématiquement les problèmes de sécurité sans nécessiter une expertise approfondie en sécurité pour chaque revue.

## Sujets couverts

- Liste de contrôle de préparation à la revue
- Critères de revue de sécurité de base (authentification, validation des entrées, autorisation, cryptographie, journalisation, gestion des erreurs)
- Approche de revue basée sur les risques
- Patterns courants et anti-patterns
- Procédures d'escalade

## Relation avec la politique

**ISMS-POL-A.8.28 exige** (contraignant) :

- Revue de code par les pairs pour tout le code de production
- Critères de revue axés sur la sécurité
- Participation des Champions de la sécurité dans les revues
- Revue de l'équipe de sécurité applicative pour les changements à risque élevé

**Ce document REF explique** (informatif) :

- COMMENT effectuer des revues de code axées sur la sécurité
- QUELS problèmes de sécurité rechercher
- QUAND escalader aux Champions de la sécurité ou à l'équipe de sécurité applicative
- Application de la liste de contrôle basée sur les risques

---

# Comment utiliser cette liste de contrôle

## Pas chaque élément pour chaque revue

**Approche basée sur les risques** :

**Changements à risque élevé** (utiliser la liste de contrôle complète) :

- Changements d'authentification ou d'autorisation
- Implémentation de cryptographie
- Traitement de paiements ou de transactions financières
- Traitement de DCP ou exposition de données
- Modifications de contrôles de sécurité
- Intégrations tierces avec des données sensibles

**Changements à risque moyen** (se concentrer sur les sections pertinentes) :

- Points de terminaison API → Validation des entrées + Autorisation
- Requêtes de base de données → Prévention de l'injection SQL
- Opérations sur fichiers → Prévention de la traversée de répertoires
- Changements d'interface web → Prévention XSS + CSRF

**Changements à faible risque** (revue de sécurité minimale) :

- Refactorisation sans changements de fonctionnalité
- Mises à jour de la documentation
- Changements de configuration (non-sécurité)
- Changements de tests uniquement

## Points d'intégration

**Modèles de Pull Request** :
```markdown
# Liste de contrôle de sécurité (si applicable)

- [ ] Validation des entrées présente et correcte
- [ ] Encodage de sortie approprié au contexte
- [ ] Requêtes SQL paramétrées
- [ ] Pas de secrets codés en dur
- [ ] Vérifications d'autorisation présentes
```

**Outils de revue** :

- Lier les éléments de la liste de contrôle dans les commentaires de revue
- Utiliser les étiquettes de l'outil de revue (security-review-required, security-approved)

## Quand escalader

**Escalader au Champion de la sécurité** :

- Élément de la liste de contrôle ambigu
- Préoccupation de sécurité au-delà de votre expertise
- Plusieurs éléments de la liste de contrôle échoués
- Pattern de sécurité complexe nécessitant une validation

**Escalader à l'équipe de sécurité applicative** :

- Vulnérabilité suspectée nécessitant une validation experte
- Problème de sécurité au niveau de l'architecture
- Besoin d'une session de modélisation des menaces
- Résultat de gravité critique/élevée des outils automatisés

**Canaux d'escalade** :

- Slack : #security-champions ou #appsec
- Email : security@[organisation].com
- Étiquetage dans le PR : @security-champions ou @appsec-team

---

# Liste de contrôle pré-revue

**À compléter AVANT de réviser le code** (économise du temps, assure la qualité) :

- [ ] **Vérifications automatisées réussies** : SAST, SCA, tests unitaires, linters tous verts ?
  - *Si non* : Réviser d'abord les résultats automatisés, s'assurer qu'ils sont traités ou supprimés avec justification

- [ ] **Description du changement claire** : La description du PR explique CE qui a changé et POURQUOI ?
  - *Vérifier* : Descriptions vagues (« bug corrigé », « mises à jour »), contexte manquant
  - *Action* : Demander une clarification si ambigu

- [ ] **Niveau de risque identifié** : Le PR indique-t-il le niveau de risque (Critique/Élevé/Moyen/Faible) ?
  - *Si non identifié* : Évaluer le risque selon les critères de la Section 2.1

- [ ] **Changements pertinents pour la sécurité signalés** : L'auteur du PR identifie-t-il les implications de sécurité ?
  - *Vérifier* : Authentification, autorisation, gestion des entrées, cryptographie, accès aux données

- [ ] **Portée du changement raisonnable** : Le PR est-il ciblé (ne modifiant pas 50 fichiers avec des changements sans rapport) ?
  - *Si trop grand* : Demander la division en PR plus petits et révisables

- [ ] **Tests inclus** : Les changements pertinents pour la sécurité sont-ils couverts par des tests ?
  - *Vérifier* : Tests de validation des entrées, tests d'autorisation, cas de test négatifs
  - *Référence politique* : ISMS-POL-A.8.28 Section 2.3.1

---

# Liste de contrôle de revue de sécurité de base

## Authentification et gestion de session

- [ ] **Vérifications d'authentification présentes** : Tous les points de terminaison protégés vérifient l'authentification de l'utilisateur
  - *Vérifier* : Authentification manquante sur les points de terminaison API, pages d'administration, accès aux données
  - *Test* : Le point de terminaison est-il accessible sans authentification ?
  - *Référence politique* : ISMS-POL-A.8.28 Section 2.2

- [ ] **Jetons de session sécurisés** : Les jetons sont aléatoires, imprévisibles, avec les attributs HttpOnly/Secure
  - *Vérifier* : ID de session prédictibles, jetons séquentiels, jetons dans les URL
  - *Valider* : Les attributs de cookie incluent `HttpOnly`, `Secure`, `SameSite=Strict/Lax`

- [ ] **Gestion des mots de passe sécurisée** : Mots de passe hachés avec bcrypt/Argon2, jamais journalisés
  - *Vérifier* : Mots de passe en clair, hachage faible (MD5, SHA1, SHA256 sans sel)
  - *Valider* : Pas de mots de passe dans les journaux, messages d'erreur ou sortie de débogage

- [ ] **Authentification multi-facteurs (MFA) appliquée** : MFA requis pour les comptes privilégiés
  - *Vérifier* : Comptes administrateur, opérations financières contournant la MFA

- [ ] **Expiration de session appropriée** : Les sessions expirent après une période d'inactivité
  - *Vérifier* : Pas d'expiration, expiration excessivement longue (>30 min pour les applications à risque élevé)

- [ ] **Fonctionnalité de déconnexion sécurisée** : La déconnexion invalide la session côté serveur
  - *Vérifier* : Déconnexion côté client uniquement, session toujours valide après déconnexion

## Validation des entrées

- [ ] **Toutes les entrées validées** : Validation côté serveur présente pour TOUTES les entrées utilisateur
  - *Vérifier* : Validation côté client uniquement, validation manquante sur les points de terminaison API
  - *Sources* : Formulaires, paramètres URL, en-têtes, cookies, téléchargements de fichiers, requêtes API
  - *Référence politique* : ISMS-POL-A.8.28 Section 2.2

- [ ] **Approche par liste blanche utilisée** : La validation utilise une liste d'autorisation (pas de liste de blocage)
  - *Vérifier* : Patterns de liste noire (« rejeter si contient X »), listes de blocage incomplètes
  - *Correct* : « Accepter uniquement si correspond à Y » (ex. alphanumérique uniquement)

- [ ] **Injection SQL prévenue** : Requêtes paramétrées utilisées, pas de concaténation de chaînes
  - *Vérifier* : Concaténation de chaînes dans SQL (f-strings, +, .format()), construction de requêtes dynamiques
  - *Valider* : Toutes les requêtes de base de données utilisent des instructions paramétrées ou ORM de manière sécurisée

- [ ] **Injection de commandes prévenue** : Pas d'appels shell directs avec entrée utilisateur
  - *Vérifier* : `os.system()`, `subprocess` avec `shell=True`, `eval()`, `exec()`
  - *Valider* : Les commandes utilisent des listes d'arguments, pas de concaténation de chaînes

- [ ] **Traversée de chemin prévenue** : Les chemins de fichiers validés, pas de traversée de répertoire
  - *Vérifier* : Concaténation directe de l'entrée utilisateur aux chemins de fichiers
  - *Valider* : Chemins résolus et validés dans le répertoire autorisé

- [ ] **XXE (XML External Entity) prévenu** : L'analyse XML désactive les entités externes
  - *Vérifier* : Configuration par défaut du parseur XML (souvent vulnérable)
  - *Valider* : Entités externes explicitement désactivées dans la configuration du parseur

- [ ] **Validation des téléchargements de fichiers** : Validation du type, de la taille et du contenu présente
  - *Vérifier* : Validation par extension uniquement, pas de validation du contenu, pas de limites de taille
  - *Valider* : Validation du nombre magique, analyse antimalware, limites de taille appliquées

- [ ] **Limites de longueur des entrées** : Longueur maximale appliquée (prévention de débordement de tampon, DoS)
  - *Vérifier* : Longueur d'entrée illimitée, limites excessivement grandes

## Encodage de sortie et prévention XSS

- [ ] **Prévention XSS** : Sortie encodée selon le contexte (HTML, JavaScript, URL, CSS)
  - *Vérifier* : Entrée utilisateur non encodée dans le HTML, `innerHTML`, `dangerouslySetInnerHTML`
  - *Valider* : Échappement automatique du framework utilisé ou encodage manuel appliqué

- [ ] **En-têtes Content Security Policy (CSP)** : CSP configuré pour atténuer l'impact XSS
  - *Vérifier* : En-têtes CSP manquants, CSP trop permissif (`unsafe-inline`, `unsafe-eval`)
  - *Valider* : CSP restreint les sources de scripts, désactive les scripts inline si possible

- [ ] **Protection CSRF** : Jetons présents pour les opérations modifiant l'état
  - *Vérifier* : Jetons CSRF manquants sur POST/PUT/DELETE/PATCH
  - *Valider* : Jetons validés côté serveur, jetons imprévisibles

- [ ] **En-têtes de sécurité HTTP** : En-têtes de sécurité correctement configurés
  - *Vérifier* : `X-Content-Type-Options`, `X-Frame-Options`, `Strict-Transport-Security` manquants
  - *Valider* : En-têtes présents et correctement configurés

## Autorisation et contrôle d'accès

- [ ] **Autorisation appliquée côté serveur** : Toutes les vérifications de contrôle d'accès sur le serveur
  - *Vérifier* : Autorisation côté client uniquement (éléments UI masqués), vérifications serveur manquantes
  - *Valider* : Chaque ressource protégée a une vérification d'autorisation côté serveur

- [ ] **Prévention IDOR** : La propriété de l'utilisateur vérifiée avant l'accès aux ressources
  - *Vérifier* : Accès direct par ID sans vérification de propriété (ex. `/api/orders/123` accessible par n'importe quel utilisateur)
  - *Test* : Un utilisateur peut-il accéder aux ressources d'un autre en changeant l'ID ?

- [ ] **Principe du moindre privilège** : Les opérations utilisent les permissions minimales nécessaires
  - *Vérifier* : Rôles trop permissifs, opérations admin-level pour les tâches utilisateur
  - *Valider* : Les connexions de base de données utilisent des privilèges limités, pas root/admin

- [ ] **Contrôle d'accès basé sur les rôles (RBAC)** : Rôles correctement assignés et vérifiés
  - *Vérifier* : ID utilisateur codés en dur à la place des rôles, vérifications de rôle manquantes

- [ ] **Escalade de privilèges prévenue** : Pas de moyen d'élever les privilèges de manière inappropriée
  - *Vérifier* : Affectation de rôles contrôlable par l'utilisateur, autorisation manquante sur les changements de privilèges

## Cryptographie

- [ ] **Algorithmes approuvés uniquement** : AES-256-GCM, RSA-2048+, ECDSA-256+, SHA-256+
  - *Vérifier* : DES, 3DES, RC4, MD5, SHA1, RSA-1024, mode ECB, cryptographie personnalisée
  - *Référence politique* : ISMS-POL-A.8.28 Section 2.2, ISMS-POL-A.8.24 (Cryptographie)

- [ ] **Pas de secrets codés en dur** : Identifiants depuis des variables d'environnement ou un gestionnaire de secrets
  - *Vérifier* : Clés API, mots de passe, jetons, clés privées dans le code
  - *Outils* : Utiliser un outil de scan de secrets (Gitleaks, TruffleHog, GitHub Secret Scanning)
  - *Action* : Si trouvé, faire tourner les identifiants immédiatement

- [ ] **Génération aléatoire sécurisée** : RNG cryptographiquement sécurisé utilisé
  - *Vérifier* : `random.random()`, `Math.random()`, graines basées sur le temps pour les jetons de sécurité
  - *Valider* : Utilisation de `secrets` (Python), `crypto.randomBytes()` (Node.js), `SecureRandom` (Java)

- [ ] **Gestion des clés de chiffrement** : Clés stockées de manière sécurisée, pas dans le code ou la config
  - *Vérifier* : Clés dans des variables d'environnement (mieux mais pas idéal), clés dans le code
  - *Valider* : Clés dans un service de gestion de clés approprié (AWS KMS, Azure Key Vault, HashiCorp Vault)

- [ ] **TLS/HTTPS appliqué** : Toutes les communications sensibles via HTTPS
  - *Vérifier* : HTTP pour l'authentification, transmission de données sensibles
  - *Valider* : En-têtes HSTS présents, pas de contenu mixte

## Gestion des erreurs et journalisation

- [ ] **Messages d'erreur génériques pour les utilisateurs** : Pas de traces de pile, erreurs SQL, chemins de fichiers exposés
  - *Vérifier* : Messages d'erreur détaillés révélant des informations système
  - *Valider* : Les erreurs côté utilisateur sont génériques (« Une erreur s'est produite »), détails journalisés côté serveur

- [ ] **Événements de sécurité journalisés** : Authentification, échecs d'autorisation, échecs de validation des entrées journalisés
  - *Vérifier* : Journalisation des événements de sécurité manquante
  - *Valider* : Détails suffisants pour l'investigation d'incident (utilisateur, action, résultat, horodatage)
  - *Référence politique* : ISMS-POL-A.8.28 Section 2.2

- [ ] **Pas de données sensibles dans les journaux** : Mots de passe, jetons, DCP exclus des journaux
  - *Vérifier* : Journalisation complète requête/réponse, journalisation de mots de passe, numéros de carte de crédit

- [ ] **Exceptions gérées de manière sécurisée** : Les blocs catch n'exposent pas d'informations sensibles
  - *Vérifier* : Blocs catch vides, exceptions propagées à l'interface utilisateur

## Protection des données

- [ ] **Données sensibles chiffrées** : DCP, données financières, identifiants chiffrés au repos et en transit
  - *Vérifier* : Stockage en clair de données sensibles
  - *Référence politique* : ISMS-POL-A.8.24 (Cryptographie)

- [ ] **Minimisation des données** : Seulement les données nécessaires collectées et conservées
  - *Vérifier* : Collecte de données excessive, conservation indéfinie

- [ ] **Suppression sécurisée des données** : Données sensibles supprimées de manière sécurisée lorsque plus nécessaires
  - *Valider* : Pas seulement marqué supprimé mais réellement effacé ou cryptographiquement effacé
  - *Référence politique* : ISMS-POL-A.8.10 (Suppression des informations)

## Dépendances tierces

- [ ] **Dépendances analysées pour les vulnérabilités** : Rapports de l'outil SCA examinés
  - *Vérifier* : Nouvelles dépendances vulnérables introduites
  - *Valider* : Pas de vulnérabilités Critiques/Élevées dans les dépendances

- [ ] **Dépendances de sources fiables** : Dépôts officiels utilisés
  - *Vérifier* : Dépendances de sources inconnues ou non fiables
  - *Valider* : Intégrité des packages (sommes de contrôle, signatures)

- [ ] **Versions des dépendances épinglées** : Fichiers de verrouillage présents et mis à jour
  - *Vérifier* : Versions non épinglées, fichiers de verrouillage manquants
  - *Valider* : `package-lock.json`, `requirements.txt`, `Gemfile.lock` soumis

---

# Lignes directrices de revue basée sur les risques

## Changements à risque critique

**Déclencheurs** :

- Changements du système d'authentification
- Changements du modèle d'autorisation
- Implémentation cryptographique
- Traitement des paiements
- Changements de traitement des DCP

**Approche de revue** :

- Application complète de la liste de contrôle (toutes les sections)
- Revue obligatoire du Champion de la sécurité ou de l'équipe de sécurité applicative
- Session de modélisation des menaces (si changement architectural)
- Tests de pénétration (si changement significatif)

**Approbation** :

- Responsable du développement + Champion de la sécurité + Responsable de la sécurité applicative

## Changements à risque élevé

**Déclencheurs** :

- Nouveaux points de terminaison API avec accès aux données
- Changements de requêtes de base de données
- Fonctionnalité de téléchargement de fichiers
- Intégrations tierces avec partage de données
- Changements d'interface d'administration

**Approche de revue** :

- Sections pertinentes de la liste de contrôle
- Revue du Champion de la sécurité recommandée
- Tests de sécurité (SAST, DAST)

**Approbation** :

- Responsable du développement + Champion de la sécurité

## Changements à risque moyen

**Déclencheurs** :

- Changements d'interface avec entrée utilisateur
- Génération de rapports avec accès aux données
- Changements de configuration affectant la sécurité
- Changements de journalisation ou de surveillance

**Approche de revue** :

- Éléments ciblés de la liste de contrôle (validation des entrées, prévention XSS)
- Revue par les pairs avec sensibilisation à la sécurité
- Analyse de sécurité automatisée

**Approbation** :

- Réviseur par les pairs avec formation en sécurité

## Changements à faible risque

**Déclencheurs** :

- Refactorisation sans changements de fonctionnalité
- Mises à jour de la documentation
- Changements de tests uniquement
- Styles d'interface (CSS) sans changements de logique

**Approche de revue** :

- Revue de code standard
- Vérifier l'absence d'impact de sécurité non intentionnel

**Approbation** :

- Revue par les pairs standard

---

# Patterns courants et anti-patterns

## Patterns sécurisés (à encourager)

**Pattern de validation des entrées** :
```python
# Validation par liste blanche
ALLOWED_FIELDS = {'name', 'email', 'age'}
def validate_input(data):
    if not all(key in ALLOWED_FIELDS for key in data.keys()):
        raise ValidationError("Champ invalide")
    # Validation supplémentaire...
```

**Pattern d'autorisation** :
```python
# Vérification de propriété avant accès à la ressource
def get_order(order_id, current_user):
    order = Order.query.get(order_id)
    if order.user_id != current_user.id:
        raise Forbidden("Accès refusé")
    return order
```

**Pattern de configuration sécurisée** :
```python
# Configuration basée sur l'environnement
API_KEY = os.environ.get('API_KEY')
if not API_KEY:
    raise ConfigError("API_KEY doit être défini")
```

## Anti-patterns (à décourager)

**Concaténation de chaînes pour SQL** :
```python
# ANTI-PATTERN - Vulnérabilité d'injection SQL
query = f"SELECT * FROM users WHERE id = {user_id}"
```

**Autorisation côté client** :
```javascript
// ANTI-PATTERN - L'autorisation doit être côté serveur
if (user.role === 'admin') {
  showAdminPanel();  // Côté client uniquement, facilement contournable
}
```

**Hachage de mot de passe faible** :
```python
# ANTI-PATTERN - Hachage faible
import hashlib
hash = hashlib.md5(password.encode()).hexdigest()
```

---

# Documentation de la revue

## Modèle de commentaire de revue

```
**Problème de sécurité : [Type de problème]**

**Gravité** : [Critique/Élevée/Moyenne/Faible]

**Problème** : [Brève description du problème de sécurité]

**Emplacement** : [Fichier et numéro de ligne]

**Risque** : [Ce qu'un attaquant pourrait faire]

**Recommandation** : [Comment corriger]

**Référence** : ISMS-POL-A.8.28 Section [X.Y] / Élément de liste de contrôle [4.X]
```

## Commentaire d'approbation de sécurité

```
**Revue de sécurité terminée**

Révisé par : [Nom du Champion de la sécurité]
Date : [JJ.MM.AAAA]

Sections de la liste de contrôle appliquées :

- [X] Authentification (4.1)
- [X] Validation des entrées (4.2)
- [X] Autorisation (4.4)

Résultats :

- [Problème 1] : Traité dans le commit [hash]
- [Problème 2] : Risque accepté avec justification [lien]

**Approuvé pour fusion** sans problèmes de sécurité en suspens.
```

---

# Procédures d'escalade

## Quand escalader

**Au Champion de la sécurité** :

- Application de la liste de contrôle ambiguë
- Validation du pattern de sécurité nécessaire
- Plusieurs éléments de la liste de contrôle échoués
- Formation ou conseils nécessaires

**À l'équipe de sécurité applicative** :

- Vulnérabilité Critique/Élevée suspectée
- Problème de sécurité au niveau de l'architecture
- Besoin de modélisation des menaces
- Résultats des outils nécessitant une validation experte

## Canaux d'escalade

| Type de problème | Canal | Délai de réponse |
|-----------------|-------|-----------------|
| **Question pendant la revue** | Slack #security-champions | < 4 heures (heures ouvrables) |
| **Problème de sécurité (non urgent)** | Slack #appsec | < 1 jour ouvrable |
| **Vulnérabilité de sécurité (Élevée)** | Email security@org.com + Slack | < 4 heures |
| **Vulnérabilité de sécurité (Critique)** | Processus de réponse aux incidents | Immédiat |

---

# Maintenance du document

**Fréquence de mise à jour** : Trimestrielle ou lorsque :

- OWASP Top 10 mis à jour
- Nouveaux patterns de vulnérabilité identifiés
- Changements de la pile technologique organisationnelle
- Changements des exigences de politique (mises à jour d'ISMS-POL-A.8.28)

**Propriétaire** : Responsable de la sécurité applicative

**Historique des versions** :

| Version | Date | Auteur | Modifications |
|---------|------|--------|---------------|
| 1.0 | [Date] | Responsable de la sécurité applicative | Référence de revue de code initiale extraite de la politique consolidée |

---

**FIN D'ISMS-REF-A.8.28**

*Cette référence technique soutient l'implémentation d'ISMS-POL-A.8.28. Les exigences contraignantes sont dans la politique, pas dans ce document.*
<!-- QA_VERIFIED: 2026-04-04 -->
