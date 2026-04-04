<!-- ISMS-CORE:REF:ISMS-REF-A.8.28-FR-code-review-technical-reference:framework:REF:a.8.28 -->
**ISMS-REF-A.8.28 — Référence technique pour la revue de code**

**Contrôle du document — ISMS-REF-A.8.28**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Référence technique pour la revue de code |
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

**CRITIQUE** : Il s'agit d'un document de référence informatif et il ne fait **PAS** partie du cadre formel de politique SMSI.

Les informations contenues fournissent des conseils techniques et des détails méthodologiques mais **n'établissent PAS d'exigences obligatoires**.

**Les exigences de politique contraignantes** sont définies dans **ISMS-POL-A.8.28 (Politique de codage sécurisé)**.

**Objectif** : Soutenir la mise en œuvre de la revue de code en fournissant :

- Des listes de contrôle détaillées pour la revue de code de sécurité
- Des comparaisons de méthodes et des conseils
- Des approches de revue basées sur les risques
- Les meilleures pratiques d'implémentation

**Utilisation** : Référence technique pour les réviseurs de code, les Champions de sécurité et les équipes de développement. Le contenu peut nécessiter des mises à jour à mesure que les patterns de vulnérabilité évoluent.

---

# Objectif et portée

## Objectif de référence

Ce document fournit des **critères de sécurité actionnables** pour les réviseurs de code. Il opérationnalise les exigences de revue de code de ISMS-POL-A.8.28 Section 2.3, traduisant la politique en étapes de revue pratiques.

*« Le premier principe est de ne pas se leurrer soi-même — et vous êtes la personne la plus facile à tromper. » — Richard Feynman*

**Objectif** : Permettre aux réviseurs de code d'identifier les problèmes de sécurité de manière systématique sans nécessiter une expertise approfondie en sécurité pour chaque revue.

## Sujets couverts

- Liste de contrôle de préparation pré-revue
- Critères de revue de sécurité principaux (authentification, validation des entrées, autorisation, cryptographie, journalisation, gestion des erreurs)
- Approche de revue basée sur les risques
- Patterns courants et anti-patterns
- Procédures d'escalade

## Relation avec la politique

**ISMS-POL-A.8.28 exige** (contraignant) :

- Revue de code par les pairs pour tout code de production
- Critères de revue axés sur la sécurité
- Participation des Champions de sécurité aux revues
- Revue de l'équipe de sécurité applicative pour les changements à risque élevé

**Ce document REF explique** (informatif) :

- COMMENT effectuer des revues de code axées sur la sécurité
- QUELS problèmes de sécurité rechercher
- QUAND escalader vers les Champions de sécurité ou l'équipe de sécurité applicative
- Application de la liste de contrôle basée sur les risques

---

# Comment utiliser cette liste de contrôle

## Pas chaque élément pour chaque revue

**Approche basée sur les risques** :

**Changements à risque élevé** (utiliser la liste de contrôle complète) :

- Authentification ou changements d'autorisation
- Implémentation cryptographique
- Traitement des paiements ou transactions financières
- Traitement des DCP ou exposition de données
- Modifications des contrôles de sécurité
- Intégrations tierces avec données sensibles

**Changements à risque moyen** (se concentrer sur les sections pertinentes) :

- Endpoints API → Validation des entrées + Autorisation
- Requêtes de base de données → Prévention de l'injection SQL
- Opérations sur les fichiers → Prévention de la traversée de chemin
- Changements de l'interface web → Prévention XSS + CSRF

**Changements à risque faible** (revue de sécurité minimale) :

- Refactoring sans changement de fonctionnalité
- Mises à jour de documentation
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

- Lier les éléments de la liste de contrôle dans les commentaires de revue (ex. « Échoue 3.2.3 : risque d'injection SQL »)
- Utiliser les étiquettes d'outils de revue (security-review-required, security-approved)

## Quand escalader

**Escalader vers le Champion de sécurité** :

- Élément de liste de contrôle peu clair ou ambigu
- Préoccupation de sécurité dépassant votre expertise
- Plusieurs éléments de liste de contrôle échoués
- Pattern de sécurité complexe nécessitant une validation

**Escalader vers l'équipe de sécurité applicative** :

- Vulnérabilité suspectée nécessitant une validation experte
- Préoccupation de sécurité au niveau de l'architecture
- Besoin d'une session de modélisation des menaces
- Résultat Critique/Élevé provenant des outils automatisés

**Canaux d'escalade** :

- Slack : #security-champions ou #appsec
- Email : security@[organisation].com
- Tagguer dans la PR : @security-champions ou @appsec-team

---

# Liste de contrôle pré-revue

**À compléter AVANT de revoir le code** (gain de temps, assurance qualité) :

- [ ] **Vérifications automatisées réussies** : SAST, SCA, tests unitaires, linters tous au vert ?
  - *Si non* : Revoir d'abord les résultats automatisés, s'assurer qu'ils sont traités ou supprimés avec justification

- [ ] **Description du changement claire** : La description de la PR explique CE QUI a changé et POURQUOI ?
  - *Vérifier* : Descriptions vagues (« bug corrigé », « mises à jour »), contexte manquant
  - *Action* : Demander des clarifications si peu clair

- [ ] **Niveau de risque identifié** : La PR indique-t-elle le niveau de risque (Critique/Élevé/Moyen/Faible) ?
  - *Si non identifié* : Évaluer le risque selon les critères de la Section 2.1

- [ ] **Changements pertinents pour la sécurité signalés** : L'auteur de la PR identifie-t-il les implications de sécurité ?
  - *Vérifier* : Authentification, autorisation, gestion des entrées, cryptographie, accès aux données
  - *Action* : Si pertinent pour la sécurité mais non signalé, appliquer les sections de liste de contrôle appropriées

- [ ] **Portée du changement raisonnable** : La PR est-elle ciblée (pas de modification de 50 fichiers sans rapport) ?
  - *Si trop grande* : Demander une division en PR plus petites et révisables

- [ ] **Tests inclus** : Les changements pertinents pour la sécurité sont-ils couverts par des tests ?
  - *Vérifier* : Tests de validation des entrées, tests d'autorisation, cas de test négatifs
  - *Référence politique* : ISMS-POL-A.8.28 Section 2.3.1

---

# Liste de contrôle principale de revue de sécurité

## Authentification et gestion de session

- [ ] **Vérifications d'authentification présentes** : Tous les endpoints protégés vérifient l'authentification de l'utilisateur
  - *Vérifier* : Authentification manquante sur les endpoints API, pages admin, accès aux données
  - *Test* : L'endpoint peut-il être accédé sans authentification ?
  - *Référence politique* : ISMS-POL-A.8.28 Section 2.2

- [ ] **Jetons de session sécurisés** : Jetons aléatoires, imprévisibles, avec flags HttpOnly/Secure
  - *Vérifier* : IDs de session prévisibles, jetons séquentiels, jetons dans les URLs
  - *Valider* : Les attributs de cookie incluent `HttpOnly`, `Secure`, `SameSite=Strict/Lax`

- [ ] **Gestion des mots de passe sécurisée** : Mots de passe hachés avec bcrypt/Argon2, jamais journalisés
  - *Vérifier* : Mots de passe en clair, hachage faible (MD5, SHA1, SHA256 sans sel)
  - *Valider* : Pas de mots de passe dans les journaux, messages d'erreur ou sortie de débogage
  - *Exemple* : Voir ISMS-CTX-A.8.28 Python Section 2.6

- [ ] **Authentification multi-facteurs (AMF) appliquée** : AMF requise pour les comptes privilégiés
  - *Vérifier* : Comptes admin, opérations financières contournant l'AMF

- [ ] **Délai d'expiration de session approprié** : Les sessions expirent après une période d'inactivité
  - *Vérifier* : Pas de délai d'expiration, délai excessivement long (>30 min pour les apps à risque élevé)

- [ ] **Fonctionnalité de déconnexion sécurisée** : La déconnexion invalide la session côté serveur
  - *Vérifier* : Déconnexion côté client uniquement, session toujours valide après déconnexion
  - *Test* : Jeton de session rejeté après déconnexion

## Validation des entrées

- [ ] **Toutes les entrées validées** : Validation côté serveur présente pour TOUTES les entrées utilisateur
  - *Vérifier* : Validation côté client uniquement, validation manquante sur les endpoints API
  - *Sources* : Formulaires, paramètres URL, en-têtes, cookies, téléchargements de fichiers, requêtes API
  - *Référence politique* : ISMS-POL-A.8.28 Section 2.2

- [ ] **Approche par liste blanche utilisée** : La validation utilise une liste d'autorisation (pas une liste de blocage)
  - *Vérifier* : Patterns de liste noire (« rejeter si contient X »), listes de blocage incomplètes
  - *Correct* : « Accepter uniquement si correspond à Y » (ex. alphanumérique uniquement)

- [ ] **Injection SQL prévenue** : Requêtes paramétrées utilisées, pas de concaténation de chaînes
  - *Vérifier* : Concaténation de chaînes dans SQL (f-strings, +, .format()), construction de requêtes dynamiques
  - *Valider* : Toutes les requêtes de base de données utilisent des instructions paramétrées ou ORM de façon sécurisée
  - *Exemple* : Voir ISMS-CTX-A.8.28 Python Section 2.2, SQL Section 7

- [ ] **Injection de commandes prévenue** : Pas d'appels shell directs avec entrée utilisateur
  - *Vérifier* : `os.system()`, `subprocess` avec `shell=True`, `eval()`, `exec()`
  - *Valider* : Les commandes utilisent des listes d'arguments, pas la concaténation de chaînes
  - *Exemple* : Voir ISMS-CTX-A.8.28 Python Section 2.3

- [ ] **Traversée de chemin prévenue** : Chemins de fichiers validés, pas de traversée de répertoire
  - *Vérifier* : Concaténation directe d'entrée utilisateur aux chemins de fichiers
  - *Valider* : Chemins résolus et validés dans le répertoire autorisé
  - *Exemple* : Voir ISMS-CTX-A.8.28 Python Section 2.4

- [ ] **Entité externe XML (XXE) prévenue** : L'analyse XML désactive les entités externes
  - *Vérifier* : Configuration du parser XML par défaut (souvent vulnérable)
  - *Valider* : Entités externes explicitement désactivées dans la configuration du parser
  - *Exemple* : Voir ISMS-CTX-A.8.28 Java Section 4.3

- [ ] **Validation des téléchargements de fichiers** : Validation du type, de la taille et du contenu présente
  - *Vérifier* : Validation par extension uniquement, pas de validation du contenu, pas de limites de taille
  - *Valider* : Validation des nombres magiques, analyse des logiciels malveillants, limites de taille appliquées

- [ ] **Limites de longueur d'entrée** : Longueur maximale appliquée (prévenir le dépassement de tampon, DoS)
  - *Vérifier* : Longueur d'entrée illimitée, limites excessivement grandes

## Encodage de sortie et prévention XSS

- [ ] **Prévention XSS** : Sortie encodée selon le contexte (HTML, JavaScript, URL, CSS)
  - *Vérifier* : Entrée utilisateur non encodée dans HTML, `innerHTML`, `dangerouslySetInnerHTML`
  - *Valider* : Échappement automatique du framework utilisé ou encodage manuel appliqué
  - *Exemple* : Voir ISMS-CTX-A.8.28 JavaScript Section 3.2

- [ ] **En-têtes Content Security Policy (CSP)** : CSP configuré pour atténuer l'impact XSS
  - *Vérifier* : En-têtes CSP manquants, CSP trop permissif (`unsafe-inline`, `unsafe-eval`)
  - *Valider* : CSP restreint les sources de scripts, désactive les scripts inline si possible

- [ ] **Protection CSRF** : Jetons présents pour les opérations changeant l'état
  - *Vérifier* : Jetons CSRF manquants sur POST/PUT/DELETE/PATCH
  - *Valider* : Jetons validés côté serveur, jetons imprévisibles
  - *Exemple* : Voir ISMS-CTX-A.8.28 JavaScript Section 3.4

- [ ] **En-têtes de sécurité HTTP** : En-têtes de sécurité correctement configurés
  - *Vérifier* : `X-Content-Type-Options`, `X-Frame-Options`, `Strict-Transport-Security` manquants
  - *Valider* : En-têtes présents et correctement configurés

## Autorisation et contrôle d'accès

- [ ] **Autorisation appliquée côté serveur** : Toutes les vérifications de contrôle d'accès côté serveur
  - *Vérifier* : Autorisation côté client uniquement (éléments UI cachés), vérifications serveur manquantes
  - *Valider* : Chaque ressource protégée dispose d'une vérification d'autorisation côté serveur

- [ ] **Prévention IDOR** : Propriété de l'utilisateur vérifiée avant l'accès à la ressource
  - *Vérifier* : Accès direct à l'ID sans vérification de propriété (ex. `/api/orders/123` accessible par n'importe quel utilisateur)
  - *Test* : Un utilisateur peut-il accéder aux ressources d'un autre en changeant l'ID ?

- [ ] **Principe du moindre privilège** : Les opérations utilisent les permissions minimales nécessaires
  - *Vérifier* : Rôles trop permissifs, opérations admin pour les tâches utilisateur
  - *Valider* : Les connexions à la base de données utilisent des privilèges limités, pas root/admin

- [ ] **Contrôle d'accès basé sur les rôles (RBAC)** : Rôles correctement attribués et vérifiés
  - *Vérifier* : ID utilisateurs codés en dur au lieu de rôles, vérifications de rôles manquantes

- [ ] **Élévation de privilèges prévenue** : Aucun moyen d'élever les privilèges de manière incorrecte
  - *Vérifier* : Attributions de rôles contrôlables par l'utilisateur, autorisation manquante sur les changements de privilèges
  - *Test* : Un utilisateur peut-il s'accorder le rôle admin ?

## Cryptographie

- [ ] **Algorithmes approuvés uniquement** : AES-256-GCM, RSA-2048+, ECDSA-256+, SHA-256+
  - *Vérifier* : DES, 3DES, RC4, MD5, SHA1, RSA-1024, mode ECB, crypto personnalisée
  - *Référence politique* : ISMS-POL-A.8.28 Section 2.2, ISMS-POL-A.8.24 (Cryptographie)

- [ ] **Pas de secrets codés en dur** : Identifiants provenant de variables d'environnement ou du gestionnaire de secrets
  - *Vérifier* : Clés API, mots de passe, jetons, clés privées dans le code
  - *Outils* : Utiliser un outil de scan de secrets (Gitleaks, TruffleHog, GitHub Secret Scanning)
  - *Action* : Si trouvés, faire pivoter les identifiants immédiatement

- [ ] **Génération aléatoire sécurisée** : GNA cryptographiquement sécurisé utilisé
  - *Vérifier* : `random.random()`, `Math.random()`, graines basées sur le temps pour les jetons de sécurité
  - *Valider* : Utilisation de `secrets` (Python), `crypto.randomBytes()` (Node.js), `SecureRandom` (Java)

- [ ] **Gestion des clés de chiffrement** : Clés stockées de façon sécurisée, pas dans le code ou la config
  - *Vérifier* : Clés de chiffrement dans les variables d'environnement (mieux mais pas idéal), clés dans le code
  - *Valider* : Clés dans un service de gestion de clés approprié (AWS KMS, Azure Key Vault, HashiCorp Vault)

- [ ] **TLS/HTTPS appliqué** : Toutes les communications sensibles via HTTPS
  - *Vérifier* : HTTP pour l'authentification, transmission de données sensibles
  - *Valider* : En-têtes HSTS présents, pas de contenu mixte

## Gestion des erreurs et journalisation

- [ ] **Messages d'erreur génériques aux utilisateurs** : Pas de traces de pile, erreurs SQL, chemins de fichiers exposés
  - *Vérifier* : Messages d'erreur détaillés révélant des informations système
  - *Valider* : Les erreurs côté utilisateur sont génériques (« Une erreur s'est produite »), détails journalisés côté serveur

- [ ] **Événements de sécurité journalisés** : Authentification, échecs d'autorisation, échecs de validation des entrées journalisés
  - *Vérifier* : Journalisation d'événements de sécurité manquante
  - *Valider* : Détails suffisants pour l'investigation d'incidents (utilisateur, action, résultat, timestamp)
  - *Référence politique* : ISMS-POL-A.8.28 Section 2.2

- [ ] **Pas de données sensibles dans les journaux** : Mots de passe, jetons, DCP exclus des journaux
  - *Vérifier* : Journalisation complète des requêtes/réponses, journalisation des mots de passe, numéros de carte de crédit
  - *Valider* : Données sensibles expurgées ou exclues

- [ ] **Exceptions gérées de façon sécurisée** : Les blocs catch n'exposent pas d'informations sensibles
  - *Vérifier* : Blocs catch vides, exceptions propagées à l'interface utilisateur

## Protection des données

- [ ] **Données sensibles chiffrées** : DCP, données financières, identifiants chiffrés au repos et en transit
  - *Vérifier* : Stockage en clair de données sensibles
  - *Référence politique* : ISMS-POL-A.8.24 (Cryptographie)

- [ ] **Minimisation des données** : Seules les données nécessaires collectées et conservées
  - *Vérifier* : Collecte excessive de données, conservation indéfinie

- [ ] **Suppression sécurisée des données** : Données sensibles supprimées de façon sécurisée lorsque plus nécessaires
  - *Valider* : Pas seulement marquées supprimées mais réellement effacées ou cryptographiquement supprimées
  - *Référence politique* : ISMS-POL-A.8.10 (Suppression d'informations)

## Dépendances tierces

- [ ] **Dépendances analysées pour les vulnérabilités** : Rapports d'outils SCA examinés
  - *Vérifier* : Nouvelles dépendances vulnérables introduites
  - *Valider* : Pas de vulnérabilités Critiques/Élevées dans les dépendances

- [ ] **Dépendances de sources fiables** : Dépôts officiels utilisés
  - *Vérifier* : Dépendances de sources inconnues ou non fiables
  - *Valider* : Intégrité des paquets (sommes de contrôle, signatures)

- [ ] **Versions des dépendances épinglées** : Fichiers de verrouillage présents et mis à jour
  - *Vérifier* : Versions non épinglées, fichiers de verrouillage manquants
  - *Valider* : `package-lock.json`, `requirements.txt`, `Gemfile.lock` validés

---

# Directives de revue basée sur les risques

## Changements à risque critique

**Déclencheurs** :

- Changements du système d'authentification
- Changements du modèle d'autorisation
- Implémentation cryptographique
- Traitement des paiements
- Changements de gestion des DCP

**Approche de revue** :

- Application complète de la liste de contrôle (toutes les sections)
- Revue obligatoire du Champion de sécurité ou de l'équipe de sécurité applicative
- Session de modélisation des menaces (si changement architectural)
- Tests de pénétration (si changement significatif)
- Tests étendus incluant les cas de test négatifs

**Approbation** :

- Responsable de développement + Champion de sécurité + Responsable de sécurité applicative

## Changements à risque élevé

**Déclencheurs** :

- Nouveaux endpoints API avec accès aux données
- Changements de requêtes de base de données
- Fonctionnalité de téléchargement de fichiers
- Intégrations tierces avec partage de données
- Changements d'interface admin

**Approche de revue** :

- Sections pertinentes de la liste de contrôle (focus sur la validation des entrées, l'autorisation, la protection des données)
- Revue du Champion de sécurité recommandée
- Tests de sécurité (SAST, DAST)
- Cas de test fonctionnels et de sécurité

**Approbation** :

- Responsable de développement + Champion de sécurité

## Changements à risque moyen

**Déclencheurs** :

- Changements UI avec entrée utilisateur
- Génération de rapports avec accès aux données
- Changements de configuration affectant la sécurité
- Changements de journalisation ou de surveillance

**Approche de revue** :

- Éléments ciblés de la liste de contrôle (validation des entrées, prévention XSS)
- Revue par les pairs avec sensibilisation à la sécurité
- Scan de sécurité automatisé

**Approbation** :

- Réviseur par les pairs avec formation à la sécurité

## Changements à risque faible

**Déclencheurs** :

- Refactoring sans changement de fonctionnalité
- Mises à jour de documentation
- Changements de tests uniquement
- Stylisation UI (CSS) sans changements de logique

**Approche de revue** :

- Revue de code standard
- Vérifier qu'il n'y a pas d'impact de sécurité non intentionnel
- Analyse rapide pour les problèmes introduits accidentellement

**Approbation** :

- Revue par les pairs standard

---

# Patterns courants et anti-patterns

## Patterns sécurisés (à encourager)

**Pattern de validation des entrées** :
```python
# Validation par liste blanche
CHAMPS_AUTORISES = {'nom', 'email', 'age'}
def valider_entree(donnees):
    if not all(cle in CHAMPS_AUTORISES for cle in donnees.keys()):
        raise ErreurValidation("Champ invalide")
    # Validation supplémentaire...
```

**Pattern d'autorisation** :
```python
# Vérification de propriété avant l'accès à la ressource
def get_commande(id_commande, utilisateur_courant):
    commande = Commande.query.get(id_commande)
    if commande.id_utilisateur != utilisateur_courant.id:
        raise Interdit("Accès refusé")
    return commande
```

**Pattern de configuration sécurisée** :
```python
# Configuration basée sur les variables d'environnement
CLE_API = os.environ.get('CLE_API')
if not CLE_API:
    raise ErreurConfig("CLE_API doit être définie")
```

## Anti-patterns (à décourager)

**Concaténation de chaînes pour SQL** :
```python
# ANTI-PATTERN - Vulnérabilité d'injection SQL
requete = f"SELECT * FROM utilisateurs WHERE id = {id_utilisateur}"
```

**Autorisation côté client** :
```javascript
// ANTI-PATTERN - L'autorisation doit être côté serveur
if (utilisateur.role === 'admin') {
  afficherPanneauAdmin();  // Côté client uniquement, facilement contournable
}
```

**Hachage de mot de passe faible** :
```python
# ANTI-PATTERN - Hachage faible
import hashlib
hash = hashlib.md5(mot_de_passe.encode()).hexdigest()
```

---

# Documentation de revue

## Modèle de commentaire de revue

```
**Problème de sécurité : [Type de problème]**

**Sévérité** : [Critique/Élevé/Moyen/Faible]

**Problème** : [Brève description du problème de sécurité]

**Emplacement** : [Fichier et numéro de ligne]

**Risque** : [Ce qu'un attaquant pourrait faire]

**Recommandation** : [Comment corriger]

**Référence** : ISMS-POL-A.8.28 Section [X.Y] / Élément de liste de contrôle [4.X]

**Exemple** : [Exemple de code ou lien vers ISMS-CTX-A.8.28]
```

## Commentaire d'approbation de sécurité

```
**Revue de sécurité terminée**

Révisé par : [Nom du Champion de sécurité]
Date : [JJ.MM.AAAA]

Sections de liste de contrôle appliquées :

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

**Vers le Champion de sécurité** :

- Application de la liste de contrôle peu claire
- Validation du pattern de sécurité nécessaire
- Plusieurs éléments de liste de contrôle échoués
- Formation ou conseils nécessaires

**Vers l'équipe de sécurité applicative** :

- Vulnérabilité Critique/Élevée suspectée
- Préoccupation de sécurité au niveau de l'architecture
- Besoin de modélisation des menaces
- Résultats d'outils nécessitant une validation experte
- Recommandation de tests de pénétration

## Canaux d'escalade

| Type de problème | Canal | Délai de réponse |
|-----------------|-------|------------------|
| **Question pendant la revue** | Slack #security-champions | < 4 heures (heures ouvrables) |
| **Préoccupation de sécurité (non urgente)** | Slack #appsec | < 1 jour ouvrable |
| **Vulnérabilité de sécurité (Élevée)** | Email security@org.com + Slack | < 4 heures |
| **Vulnérabilité de sécurité (Critique)** | Processus de réponse aux incidents | Immédiat |

---

# Maintenance du document

**Fréquence de mise à jour** : Trimestrielle ou lorsque :

- OWASP Top 10 mis à jour
- Nouveaux patterns de vulnérabilité identifiés
- Changements de pile technologique de l'organisation
- Changements des exigences de politique (mises à jour d'ISMS-POL-A.8.28)

**Propriétaire** : Responsable de la sécurité applicative

**Déclencheurs de révision** :

- Incidents de sécurité majeurs nécessitant des mises à jour de la liste de contrôle
- Retours des développeurs sur la clarté ou la complétude de la liste de contrôle
- Changements d'intégration des outils de sécurité
- Retours sur l'efficacité de la formation

**Historique des versions** :

| Version | Date | Auteur | Modifications |
|---------|------|--------|---------------|
| 1.0 | [Date] | Responsable de la sécurité applicative | Référence de revue de code initiale extraite de la politique consolidée |

---

**FIN DE ISMS-REF-A.8.28**

*Cette référence technique soutient l'implémentation d'ISMS-POL-A.8.28. Les exigences contraignantes sont dans la politique, pas dans ce document.*
<!-- QA_VERIFIED: 2026-04-04 -->
