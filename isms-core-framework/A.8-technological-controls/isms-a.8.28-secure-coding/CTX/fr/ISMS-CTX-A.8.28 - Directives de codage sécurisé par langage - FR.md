<!-- ISMS-CORE:CTX:ISMS-CTX-A.8.28-FR-language-specific-secure-coding:framework:CTX:a.8.28 -->
**ISMS-CTX-A.8.28 — Directives de codage sécurisé par langage**

**Contrôle du document — ISMS-CTX-A.8.28**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Directives de codage sécurisé par langage |
| **Type de document** | Contexte technique (CTX) |
| **Identifiant du document** | ISMS-CTX-A.8.28 |
| **Créateur du document** | Responsable de la sécurité applicative |
| **Propriétaire du document** | Responsable de la sécurité applicative |
| **Approuvé par** | Responsable de la sécurité applicative |
| **Date de création** | [Date] |
| **Version** | 1.0 |
| **Classification** | Interne |
| **Statut** | Brouillon |

---

## Avertissement

**CRITIQUE** : Il s'agit d'un document de référence informatif et il ne fait **PAS** partie du cadre formel de politique SMSI. Les exigences de politique contraignantes sont définies dans **ISMS-POL-A.8.28 (Politique de codage sécurisé)**.

---

# Objectif et portée

## Objectif du document

Ce document fournit des **modèles de codage sécurisé spécifiques aux langages** qui opérationnalisent les exigences de sécurité génériques d'ISMS-POL-A.8.28. Les vulnérabilités de sécurité se manifestent différemment selon les langages de programmation en raison des choix de conception du langage, des implémentations de la bibliothèque standard, des frameworks courants et des pratiques de la communauté de développement.

**Ce document répond à** : « Comment implémenter les normes de codage sécurisé *dans ce langage spécifique* ? »

## Priorité des langages

Langages couverts selon l'utilisation organisationnelle :

1. **Python** (services backend, traitement des données, automatisation)
2. **JavaScript/TypeScript** (frontend, backend Node.js)
3. **Java** (applications d'entreprise, microservices)
4. **C#/.NET** (applications Windows, services Azure)
5. **Go** (outils d'infrastructure, microservices cloud-native)
6. **SQL** (multilangage, accès aux données)

## Relation avec la politique

**ISMS-POL-A.8.28 établit** (contraignant) :

- Obligation de suivre des normes de codage sécurisé
- Obligation de validation des entrées, d'encodage des sorties, d'authentification sécurisée
- Obligation d'éviter les pratiques interdites (secrets codés en dur, crypto faible)

**Ce document CTX fournit** (informatif) :

- Comment implémenter ces exigences en Python, JavaScript, Java, C#, Go, SQL

## Références externes

- **OWASP Cheat Sheet Series** : https://cheatsheetseries.owasp.org/
- **SEI CERT Coding Standards** : https://wiki.sei.cmu.edu/confluence/
- **CWE (Common Weakness Enumeration)** : https://cwe.mitre.org/

---

# Directives de sécurité Python

## Patterns de vulnérabilités courants

**Principales vulnérabilités en Python** :
1. **Injection SQL** (CWE-89) : Formatage de chaînes dans les requêtes
2. **Injection de commandes** (CWE-78) : Utilisation non sécurisée de `os.system()`, `subprocess` avec `shell=True`
3. **Désérialisation** (CWE-502) : Utilisation non sécurisée de pickle
4. **Traversée de chemin** (CWE-22) : Chemins de fichiers non validés
5. **Cryptographie faible** (CWE-327) : Utilisation de MD5/SHA1, aléatoire non sécurisé

## Prévention de l'injection SQL

✅ **CORRECT — Requêtes paramétrées** :
```python
# sqlite3
cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))

# psycopg2 (PostgreSQL)
cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))

# SQLAlchemy ORM
user = session.query(User).filter(User.id == user_id).first()
```

❌ **DANGEREUX — Formatage de chaînes** :
```python
# NE JAMAIS utiliser les f-strings pour SQL
cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")  # Injection SQL !
cursor.execute("SELECT * FROM users WHERE id = {}".format(user_id))  # Injection SQL !
```

## Prévention de l'injection de commandes

✅ **CORRECT — Arguments en liste, pas de shell** :
```python
import subprocess

# Passer les arguments en liste, shell=False (défaut)
result = subprocess.run(['ls', '-l', directory_name], 
                       capture_output=True, check=True)

# Pour les noms de fichiers avec des caractères spéciaux
import shlex
filename = shlex.quote(user_filename)
subprocess.run(['tar', '-czf', 'backup.tar.gz', filename])
```

❌ **DANGEREUX — Chaînes de commandes shell** :
```python
# NE JAMAIS utiliser shell=True avec entrée utilisateur
subprocess.run(f'ls -l {directory_name}', shell=True)  # Injection de commandes !
os.system(f'rm {filename}')  # Injection de commandes !
```

## Prévention de la traversée de chemin

✅ **CORRECT — Valider et résoudre les chemins** :
```python
from pathlib import Path

UPLOAD_DIR = Path('/var/app/uploads')

def accès_fichier_sécurisé(nom_fichier_utilisateur):
    chemin_demandé = (UPLOAD_DIR / nom_fichier_utilisateur).resolve()
    
    if not chemin_demandé.is_relative_to(UPLOAD_DIR):
        raise ValueError("Chemin de fichier invalide")
    
    return chemin_demandé
```

❌ **DANGEREUX — Concaténation de chemins directe** :
```python
# Traversée de chemin : user_input pourrait être "../../etc/passwd"
filepath = f'/var/app/uploads/{user_input}'
with open(filepath, 'r') as f:  # Peut accéder à n'importe quel fichier !
    content = f.read()
```

## Hachage sécurisé des mots de passe

✅ **CORRECT — bcrypt ou Argon2** :
```python
import bcrypt

# Hachage
password = b"mot_de_passe_utilisateur"
salt = bcrypt.gensalt(rounds=12)
hashed = bcrypt.hashpw(password, salt)

# Vérification
if bcrypt.checkpw(password, hashed):
    print("Mot de passe correct")

# Ou Argon2 (recommandé pour les nouveaux systèmes)
from argon2 import PasswordHasher
ph = PasswordHasher()
hash = ph.hash("mot_de_passe_utilisateur")
ph.verify(hash, "mot_de_passe_utilisateur")
```

❌ **DANGEREUX — MD5, SHA1, ou texte clair** :
```python
import hashlib
# NE JAMAIS utiliser MD5 ou SHA1 pour les mots de passe
hashed = hashlib.md5(password.encode()).hexdigest()  # Vulnérable !
hashed = hashlib.sha1(password.encode()).hexdigest()  # Vulnérable !
```

## Génération de nombres aléatoires sécurisée

✅ **CORRECT — Module secrets** :
```python
import secrets

# Générer un jeton aléatoire sécurisé
token = secrets.token_urlsafe(32)  # 32 octets = 256 bits

# Nombre aléatoire sécurisé
random_number = secrets.randbelow(100)
```

❌ **DANGEREUX — Module random** :
```python
import random
# NE JAMAIS utiliser le module random pour la sécurité
token = random.randint(0, 1000000)  # PAS cryptographiquement sécurisé !
```

## Sécurité de la désérialisation

✅ **CORRECT — Utiliser JSON ou un Unpickler restreint** :
```python
import json
data = json.loads(user_input)  # Sûr

# Si pickle nécessaire, restreindre les classes autorisées
import pickle, io

class UnpicklerRestreint(pickle.Unpickler):
    def find_class(self, module, name):
        if module == "myapp.models" and name in ["User", "Config"]:
            return super().find_class(module, name)
        raise pickle.UnpicklingError(f"Classe interdite : {module}.{name}")

def unpickle_sécurisé(data):
    return UnpicklerRestreint(io.BytesIO(data)).load()
```

❌ **DANGEREUX — pickle.loads() sans restriction** :
```python
import pickle
# NE JAMAIS désérialiser des données non fiables
obj = pickle.loads(user_input)  # Risque d'exécution de code à distance !
```

---

# Directives de sécurité JavaScript/TypeScript

## Patterns de vulnérabilités courants

**Principales vulnérabilités en JavaScript** :
1. **XSS** (CWE-79) : innerHTML avec entrée utilisateur, utilisation de eval()
2. **Pollution de prototype** (CWE-1321) : Fusion d'objets non sécurisée
3. **CSRF** (CWE-352) : Jetons CSRF manquants
4. **Redirection ouverte** (CWE-601) : Cibles de redirection non validées
5. **ReDoS** (CWE-1333) : Déni de service par expression régulière

## Prévention XSS

✅ **CORRECT — textContent ou auto-échappement du framework** :
```javascript
// JS vanilla - utiliser textContent (pas innerHTML)
element.textContent = userInput;  // Sûr - échappe automatiquement

// React - JSX auto-échappe par défaut
function Bienvenue({ name }) {
  return <h1>Bienvenue {name}</h1>;  // Auto-échappé
}

// Vue - les templates auto-échappent par défaut
<template>
  <h1>Bienvenue {{ userName }}</h1>  <!-- Auto-échappé -->
</template>
```

❌ **DANGEREUX — innerHTML avec entrée utilisateur** :
```javascript
// NE JAMAIS utiliser innerHTML avec entrée utilisateur
element.innerHTML = userInput;  // Vulnérabilité XSS !

// React - dangerouslySetInnerHTML (éviter !)
<div dangerouslySetInnerHTML={{__html: userInput}} />  // XSS !
```

## Prévention de la pollution de prototype

✅ **CORRECT — Opérations sécurisées sur les objets** :
```javascript
// Utiliser Object.create(null) pour des objets sécurisés
const objSécurisé = Object.create(null);
objSécurisé[userKey] = userValue;

// Ou valider les clés avant l'affectation
function affectationSécurisée(obj, clé, valeur) {
  if (['__proto__', 'constructor', 'prototype'].includes(clé)) {
    throw new Error('Clé interdite');
  }
  obj[clé] = valeur;
}
```

## Protection CSRF

✅ **CORRECT — Utiliser des jetons CSRF** :
```javascript
// Express.js avec csurf
const csrf = require('csurf');
const protectionCsrf = csrf({ cookie: true });

app.post('/transfert', protectionCsrf, (req, res) => {
  traiterTransfert(req.body);
});

// Frontend - inclure le jeton CSRF
<form method="POST" action="/transfert">
  <input type="hidden" name="_csrf" value="{{csrfToken}}">
  <button type="submit">Transférer</button>
</form>

// Pour les requêtes AJAX
fetch('/api/transfert', {
  method: 'POST',
  headers: {
    'CSRF-Token': csrfToken,
    'Content-Type': 'application/json'
  },
  body: JSON.stringify(data)
});
```

## Hachage sécurisé des mots de passe (Node.js)

✅ **CORRECT — bcrypt** :
```javascript
const bcrypt = require('bcrypt');

const saltRounds = 12;
const hash = await bcrypt.hash(password, saltRounds);

const match = await bcrypt.compare(password, hash);
if (match) { /* Mot de passe correct */ }
```

❌ **DANGEREUX — crypto.createHash()** :
```javascript
const crypto = require('crypto');
// NE JAMAIS utiliser MD5 ou SHA pour les mots de passe
const hash = crypto.createHash('md5').update(password).digest('hex');  // Vulnérable !
```

## Génération aléatoire sécurisée (Node.js)

✅ **CORRECT — crypto.randomBytes()** :
```javascript
const crypto = require('crypto');
const token = crypto.randomBytes(32).toString('hex');
const randomValue = crypto.randomInt(0, 100);
```

❌ **DANGEREUX — Math.random()** :
```javascript
// NE JAMAIS utiliser Math.random() pour la sécurité
const token = Math.random().toString(36).substring(2);  // PAS sécurisé !
```

## Éviter eval() et l'exécution de code dynamique

❌ **DANGEREUX — eval() avec entrée utilisateur** :
```javascript
eval(userInput);  // Exécution de code à distance !
new Function(userInput)();  // Exécution de code à distance !
setTimeout(userInput, 1000);  // Injection de code !
```

---

# Directives de sécurité Java

## Patterns de vulnérabilités courants

**Principales vulnérabilités en Java** :
1. **Injection SQL** (CWE-89) : Concaténation de chaînes dans les requêtes
2. **XXE** (CWE-611) : Attaques d'entités externes XML
3. **Désérialisation** (CWE-502) : ObjectInputStream non sécurisé
4. **Traversée de chemin** (CWE-22) : Chemins non validés
5. **Cryptographie faible** (CWE-327) : DES, MD5, RNG faible

## Prévention de l'injection SQL

✅ **CORRECT — PreparedStatement** :
```java
// JDBC PreparedStatement
String query = "SELECT * FROM users WHERE id = ?";
PreparedStatement stmt = connection.prepareStatement(query);
stmt.setInt(1, userId);
ResultSet rs = stmt.executeQuery();

// JPA/Hibernate (paramétré)
TypedQuery<User> query = em.createQuery(
    "SELECT u FROM User u WHERE u.id = :userId", User.class);
query.setParameter("userId", userId);
```

❌ **DANGEREUX — Concaténation de chaînes** :
```java
// NE JAMAIS concaténer des chaînes pour SQL
String query = "SELECT * FROM users WHERE id = " + userId;  // Injection SQL !
```

## Prévention XXE

✅ **CORRECT — Désactiver les entités externes** :
```java
DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
dbf.setFeature("http://apache.org/xml/features/disallow-doctype-decl", true);
dbf.setFeature("http://xml.org/sax/features/external-general-entities", false);
dbf.setFeature("http://xml.org/sax/features/external-parameter-entities", false);
dbf.setXIncludeAware(false);
dbf.setExpandEntityReferences(false);
DocumentBuilder db = dbf.newDocumentBuilder();
```

## Désérialisation sécurisée

✅ **CORRECT — Filtre de désérialisation look-ahead (Java 9+)** :
```java
ObjectInputFilter filter = ObjectInputFilter.Config.createFilter(
    "com.myapp.model.*;!*"
);
ObjectInputStream ois = new ObjectInputStream(inputStream);
ois.setObjectInputFilter(filter);
Object obj = ois.readObject();
```

❌ **DANGEREUX — readObject() sans restriction** :
```java
// NE JAMAIS désérialiser des données non fiables
ObjectInputStream ois = new ObjectInputStream(inputStream);
Object obj = ois.readObject();  // Vulnérabilité de désérialisation !
```

## Génération aléatoire sécurisée

✅ **CORRECT — SecureRandom** :
```java
import java.security.SecureRandom;
SecureRandom random = new SecureRandom();
byte[] token = new byte[32];
random.nextBytes(token);
```

❌ **DANGEREUX — java.util.Random** :
```java
Random random = new Random();
int value = random.nextInt();  // PAS cryptographiquement sécurisé !
```

---

# Directives de sécurité C#/.NET

## Prévention de l'injection SQL

✅ **CORRECT — Requêtes paramétrées** :
```csharp
// ADO.NET avec paramètres
string query = "SELECT * FROM Users WHERE Id = @userId";
using (SqlCommand cmd = new SqlCommand(query, connection))
{
    cmd.Parameters.AddWithValue("@userId", userId);
    SqlDataReader reader = cmd.ExecuteReader();
}

// Entity Framework (LINQ — automatiquement paramétré)
var user = context.Users.FirstOrDefault(u => u.Id == userId);
```

❌ **DANGEREUX — Interpolation de chaînes** :
```csharp
string query = $"SELECT * FROM Users WHERE Id = {userId}";  // Injection SQL !
```

## Prévention XSS en Razor

✅ **CORRECT — Auto-encodage Razor** :
```csharp
@* Razor encode automatiquement en HTML par défaut *@
<h1>Bienvenue @Model.UserName</h1>  @* Auto-encodé *@
```

❌ **DANGEREUX — Html.Raw()** :
```csharp
<div>@Html.Raw(Model.UserInput)</div>  @* Vulnérabilité XSS ! *@
```

## Hachage sécurisé des mots de passe

✅ **CORRECT — ASP.NET Core Identity** :
```csharp
using Microsoft.AspNetCore.Identity;

var passwordHasher = new PasswordHasher<User>();
string hash = passwordHasher.HashPassword(user, password);

var result = passwordHasher.VerifyHashedPassword(user, hash, password);
if (result == PasswordVerificationResult.Success)
{ /* Mot de passe correct */ }
```

## Désérialisation sécurisée

✅ **CORRECT — JSON.NET ou System.Text.Json** :
```csharp
using System.Text.Json;
var obj = JsonSerializer.Deserialize<MyClass>(json);
```

❌ **DANGEREUX — BinaryFormatter** :
```csharp
BinaryFormatter formatter = new BinaryFormatter();
object obj = formatter.Deserialize(stream);  // Vulnérabilité de désérialisation !
```

---

# Directives de sécurité Go

## Prévention de l'injection SQL

✅ **CORRECT — Requêtes paramétrées** :
```go
query := "SELECT * FROM users WHERE id = $1"
row := db.QueryRow(query, userId)
```

❌ **DANGEREUX — fmt.Sprintf() pour SQL** :
```go
query := fmt.Sprintf("SELECT * FROM users WHERE id = %d", userId)  // Injection SQL !
```

## Prévention de l'injection de commandes

✅ **CORRECT — exec.Command avec arguments séparés** :
```go
import "os/exec"
cmd := exec.Command("ls", "-l", directory)
output, err := cmd.Output()
```

❌ **DANGEREUX — exec.Command avec shell** :
```go
cmd := exec.Command("sh", "-c", fmt.Sprintf("ls -l %s", directory))  // Injection !
```

## Hachage sécurisé des mots de passe

✅ **CORRECT — golang.org/x/crypto/bcrypt** :
```go
import "golang.org/x/crypto/bcrypt"

hash, err := bcrypt.GenerateFromPassword([]byte(password), bcrypt.DefaultCost)

err = bcrypt.CompareHashAndPassword(hash, []byte(password))
if err == nil { /* Mot de passe correct */ }
```

## Génération aléatoire sécurisée

✅ **CORRECT — crypto/rand** :
```go
import "crypto/rand"
token := make([]byte, 32)
_, err := rand.Read(token)
```

❌ **DANGEREUX — math/rand** :
```go
import "math/rand"
value := rand.Intn(100)  // PAS cryptographiquement sécurisé !
```

---

# Directives de sécurité SQL (multilangage)

## Requêtes paramétrées par base de données

```sql
-- PostgreSQL
SELECT * FROM users WHERE id = $1;

-- MySQL
SELECT * FROM users WHERE id = ?;

-- SQL Server
SELECT * FROM users WHERE id = @userId;
```

## Comptes de base de données à moindres privilèges

✅ **CORRECT — Permissions minimales** :
```sql
CREATE USER app_user WITH PASSWORD 'mot_de_passe_sécurisé';

GRANT SELECT, INSERT, UPDATE ON users TO app_user;
GRANT SELECT ON products TO app_user;

REVOKE DROP, CREATE, ALTER ON DATABASE FROM app_user;
```

## Éviter le SQL dynamique dans les procédures stockées

❌ **DANGEREUX — SQL dynamique dans une procédure stockée** :
```sql
CREATE PROCEDURE GetUserById(@userId VARCHAR(50))
AS BEGIN
    DECLARE @sql NVARCHAR(MAX);
    SET @sql = 'SELECT * FROM users WHERE id = ' + @userId;  -- Injection SQL !
    EXEC sp_executesql @sql;
END
```

✅ **CORRECT — Procédure stockée paramétrée** :
```sql
CREATE PROCEDURE GetUserById(@userId INT)
AS BEGIN
    SELECT * FROM users WHERE id = @userId;  -- Sûr
END
```

---

# Maintenance du document

**Fréquence de mise à jour** : Semestrielle ou lorsque :

- Une version majeure du langage est publiée
- De nouvelles fonctionnalités de sécurité de framework sont disponibles
- OWASP Top 10 est mis à jour
- Les avertissements de sécurité de langage/framework sont publiés

**Propriétaire** : Responsable de la sécurité applicative

**Historique des versions** :

| Version | Date | Auteur | Modifications |
|---------|------|--------|---------------|
| 1.0 | [Date] | Responsable de la sécurité applicative | Directives initiales extraites de la politique consolidée |

---

**FIN DE ISMS-CTX-A.8.28**

*Cette référence technique soutient l'implémentation d'ISMS-POL-A.8.28. Les exigences contraignantes sont dans la politique, pas dans ce document.*
<!-- QA_VERIFIED: 2026-04-04 -->
