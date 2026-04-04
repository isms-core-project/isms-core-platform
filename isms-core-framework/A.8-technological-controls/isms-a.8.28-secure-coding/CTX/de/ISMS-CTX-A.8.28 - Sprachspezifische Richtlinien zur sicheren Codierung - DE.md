<!-- ISMS-CORE:CTX:ISMS-CTX-A.8.28-sprachspezifische-richtlinien-sichere-codierung-DE:framework:CTX:a.8.28 -->
**ISMS-CTX-A.8.28 — Sprachspezifische Richtlinien zur sicheren Codierung**

**Dokumentenkontrolle — ISMS-CTX-A.8.28**

| Feld | Wert |
|------|------|
| **Dokumententitel** | Sprachspezifische Richtlinien zur sicheren Codierung |
| **Dokumententyp** | Technischer Kontext (CTX) |
| **Dokument-ID** | ISMS-CTX-A.8.28 |
| **Ersteller** | Application Security Lead |
| **Dokumenteneigentümer** | Application Security Lead |
| **Genehmigt von** | Application Security Lead |
| **Erstellungsdatum** | [Datum] ||
| **Version** | 1.0 |
| **Versionsdatum** | [Date] |
| **Klassifikation** | Intern |
| **Status** | Entwurf |

---

## Haftungsausschluss

**WICHTIG**: Dies ist ein informelles Referenzdokument und ist **NICHT** Bestandteil des formalen ISMS-Richtlinienrahmens.

Die hierin enthaltenen Informationen bieten technischen Kontext, sprachspezifische Muster für sichere Codierung und technologiespezifische Anleitungen, begründen jedoch **KEINE verbindlichen Anforderungen**.

**Verbindliche Richtlinienanforderungen** sind in **ISMS-POL-A.8.28 (Richtlinie zur sicheren Codierung)** definiert.

**Zweck**: Unterstützung fundierter Entscheidungen zur sicheren Codierung durch:

- Sprachspezifische Schwachstellenmuster und Präventionsverfahren
- Informationen zur Technologieentwicklung und zu Sicherheitsfunktionen von Frameworks
- Best-Practice-Anleitungen für von [Organisation] eingesetzte Programmiersprachen
- Codebeispiele zur Veranschaulichung sicherer vs. unsicherer Muster

**Verwendung**: Technische Referenz für Entwickler und Security Champions. Inhalt muss möglicherweise aktualisiert werden, wenn sich Sprachen weiterentwickeln und neue Frameworks entstehen — Veröffentlichungsdatum prüfen.

---

# Zweck und Geltungsbereich

## Dokumentziel

Dieses Dokument stellt **sprachspezifische Muster für sichere Codierung** bereit, die die allgemeinen Sicherheitsanforderungen aus ISMS-POL-A.8.28 operationalisieren. Sicherheitsschwachstellen manifestieren sich in verschiedenen Programmiersprachen unterschiedlich, bedingt durch:

- Sprachdesignentscheidungen (Memory-Safety, Typsysteme)
- Implementierungen der Standardbibliothek
- Gängige Frameworks und Muster
- Praktiken der Entwicklergemeinschaft

*"Für eine erfolgreiche Technologie muss die Realität Vorrang vor Public Relations haben, denn die Natur lässt sich nicht täuschen." — Richard Feynman*

**Dieses Dokument beantwortet**: "Wie implementiere ich Standards für sichere Codierung *in dieser spezifischen Sprache*?"

## Abdeckungsphilosophie

**Fokus auf hochwertige Themen**: Wir behandeln Schwachstellen, die:
1. **Häufig** im organisationseigenen Code auftreten
2. **Hohen Schweregrad** haben (ausnutzbar, hohe Auswirkung)
3. **Sprachspezifisch** sind (sprachspezifische Anleitungen erfordern)

**Nicht behandelt werden**:

- Generische Sicherheitsprinzipien (siehe ISMS-POL-A.8.28 Abschnitt 2.2)
- Jede erdenkliche Schwachstelle (Fokus auf OWASP Top 10 + sprachspezifische)
- Ersatz für massgebliche externe Standards (wir verweisen auf OWASP, CERT, Herstellerleitfäden)

## Sprachpriorität

Behandelte Sprachen basierend auf organisatorischer Nutzung (anpassen gemäss Technologie-Stack von [Organisation]):

1. **Python** (Backend-Dienste, Datenverarbeitung, Automatisierung)
2. **JavaScript/TypeScript** (Frontend, Node.js Backend)
3. **Java** (Unternehmensanwendungen, Microservices)
4. **C#/.NET** (Windows-Anwendungen, Azure-Dienste)
5. **Go** (Infrastrukturtools, Cloud-native Microservices)
6. **SQL** (sprachübergreifend, Datenzugriff)

**Hinweis**: Sollte Ihre Sprache nicht abgedeckt sein, konsultieren Sie die OWASP Cheat Sheet Series und SEI CERT Coding Standards für diese Sprache.

## Beziehung zur Richtlinie

**ISMS-POL-A.8.28 legt fest** (verbindlich):

- Anforderung zur Einhaltung von Standards für sichere Codierung
- Anforderung an Eingabevalidierung, Ausgabe-Encoding, sichere Authentifizierung
- Anforderung zur Vermeidung verbotener Praktiken (hartcodierte Geheimnisse, schwache Kryptographie)

**Dieses CTX-Dokument stellt bereit** (informativ):

- Wie diese Anforderungen in Python umzusetzen sind
- Wie diese Anforderungen in JavaScript/TypeScript umzusetzen sind
- Wie diese Anforderungen in Java umzusetzen sind
- Sprachspezifische Muster und Anti-Muster

## Externe Referenzen

**Massgebliche Quellen** (stets auf Aktualität prüfen):

- **OWASP Cheat Sheet Series**: https://cheatsheetseries.owasp.org/
- **SEI CERT Coding Standards**: https://wiki.sei.cmu.edu/confluence/
- **CWE (Common Weakness Enumeration)**: https://cwe.mitre.org/
- **Herstellerspezifisch**: Microsoft SDL, Oracle Secure Coding Standards, Node.js Security Best Practices

---

# Python-Sicherheitsrichtlinien

## Häufige Schwachstellenmuster

**Häufigste Schwachstellen in Python**:
1. **SQL-Injection** (CWE-89): String-Formatierung in Abfragen
2. **Command-Injection** (CWE-78): Unsichere Verwendung von `os.system()`, `subprocess` mit `shell=True`
3. **Deserialisierung** (CWE-502): Unsichere Pickle-Verwendung
4. **Path Traversal** (CWE-22): Nicht validierte Dateipfade
5. **Schwache Kryptographie** (CWE-327): Verwendung von MD5/SHA1, unsicherem Zufallsgenerator

## Verhinderung von SQL-Injection

✅ **KORREKT — Parametrisierte Abfragen**:
```python
# Mit sqlite3
cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))

# Mit psycopg2 (PostgreSQL)
cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))

# Mit SQLAlchemy ORM
user = session.query(User).filter(User.id == user_id).first()
```

❌ **UNSICHER — String-Formatierung**:
```python
# NIEMALS f-Strings oder %-Formatierung für SQL verwenden
cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")  # SQL-Injection!
cursor.execute("SELECT * FROM users WHERE id = %s" % user_id)  # SQL-Injection!
cursor.execute("SELECT * FROM users WHERE id = {}".format(user_id))  # SQL-Injection!
```

## Verhinderung von Command-Injection

✅ **KORREKT — Listenargumente, kein Shell**:
```python
import subprocess

# Argumente als Liste übergeben, shell=False (Standard)
result = subprocess.run(['ls', '-l', directory_name],
                       capture_output=True, check=True)

# Für Dateinamen mit Sonderzeichen shlex verwenden
import shlex
filename = shlex.quote(user_filename)
subprocess.run(['tar', '-czf', 'backup.tar.gz', filename])
```

❌ **UNSICHER — Shell-Befehlsstrings**:
```python
# NIEMALS shell=True mit Benutzereingaben verwenden
subprocess.run(f'ls -l {directory_name}', shell=True)  # Command-Injection!
os.system(f'rm {filename}')  # Command-Injection!
```

## Verhinderung von Path Traversal

✅ **KORREKT — Pfade validieren und auflösen**:
```python
import os
from pathlib import Path

UPLOAD_DIR = Path('/var/app/uploads')

def safe_file_access(user_filename):
    # In absoluten Pfad auflösen und prüfen, ob er im erlaubten Verzeichnis liegt
    requested_path = (UPLOAD_DIR / user_filename).resolve()

    # Sicherstellen, dass der Pfad innerhalb von UPLOAD_DIR liegt
    if not requested_path.is_relative_to(UPLOAD_DIR):
        raise ValueError("Ungültiger Dateipfad")

    return requested_path

# Verwendung
safe_path = safe_file_access(user_input)
with open(safe_path, 'r') as f:
    content = f.read()
```

❌ **UNSICHER — Direkte Pfadverkettung**:
```python
# Path Traversal: user_input könnte "../../etc/passwd" sein
filepath = f'/var/app/uploads/{user_input}'
with open(filepath, 'r') as f:  # Kann auf beliebige Dateien zugreifen!
    content = f.read()
```

## XSS-Verhinderung in Templates

✅ **KORREKT — Template-Auto-Escaping verwenden**:
```python
# Jinja2 (Flask Standard) — Auto-Escaping standardmässig aktiviert
from flask import render_template

@app.route('/profile')
def profile():
    # user_data['name'] wird automatisch escaped
    return render_template('profile.html', name=user_data['name'])

# Im Template (profile.html):
# <h1>Welcome {{ name }}</h1>  <!-- Automatisch escaped -->
```

❌ **UNSICHER — Manuelle String-Formatierung**:
```python
# NIEMALS HTML mit String-Formatierung erstellen
html = f"<h1>Welcome {user_data['name']}</h1>"  # XSS, wenn name <script> enthält
return html
```

## Sicheres Password-Hashing

✅ **KORREKT — bcrypt oder Argon2**:
```python
import bcrypt

# Passwort hashen
password = b"user_password"
salt = bcrypt.gensalt(rounds=12)  # Kostenfaktor 12
hashed = bcrypt.hashpw(password, salt)

# Passwort verifizieren
if bcrypt.checkpw(password, hashed):
    print("Passwort korrekt")

# Oder Argon2 verwenden (empfohlen für neue Systeme)
from argon2 import PasswordHasher
ph = PasswordHasher()
hash = ph.hash("user_password")
ph.verify(hash, "user_password")
```

❌ **UNSICHER — MD5, SHA1 oder Klartext**:
```python
import hashlib

# NIEMALS MD5 oder SHA1 für Passwörter verwenden
hashed = hashlib.md5(password.encode()).hexdigest()  # Angreifbar!
hashed = hashlib.sha1(password.encode()).hexdigest()  # Angreifbar!

# Auch SHA256 ohne Salt ist schwach
hashed = hashlib.sha256(password.encode()).hexdigest()  # Anfällig für Rainbow Tables
```

## Sichere Zufallszahlengenerierung

✅ **KORREKT — secrets-Modul**:
```python
import secrets

# Sicheres zufälliges Token generieren
token = secrets.token_urlsafe(32)  # 32 Bytes = 256 Bits

# Sichere Zufallszahlen generieren
random_number = secrets.randbelow(100)  # Zufallszahl 0–99
```

❌ **UNSICHER — random-Modul**:
```python
import random

# NIEMALS das random-Modul für Sicherheitszwecke verwenden
token = random.randint(0, 1000000)  # NICHT kryptographisch sicher!
```

## Sicherheit bei der Deserialisierung

✅ **KORREKT — JSON oder eingeschränkter Unpickler**:
```python
import json

# JSON für die Datenserialisierung bevorzugen
data = json.loads(user_input)  # Sicher

# Wenn Pickle erforderlich, erlaubte Klassen einschränken
import pickle
import io

class RestrictedUnpickler(pickle.Unpickler):
    def find_class(self, module, name):
        # Nur bestimmte sichere Klassen erlauben
        if module == "myapp.models" and name in ["User", "Config"]:
            return super().find_class(module, name)
        raise pickle.UnpicklingError(f"Verbotene Klasse: {module}.{name}")

def safe_unpickle(data):
    return RestrictedUnpickler(io.BytesIO(data)).load()
```

❌ **UNSICHER — Uneingeschränktes pickle.loads()**:
```python
import pickle

# NIEMALS nicht vertrauenswürdige Daten deserialisieren
obj = pickle.loads(user_input)  # Risiko für Remote Code Execution!
```

---

# JavaScript/TypeScript-Sicherheitsrichtlinien

## Häufige Schwachstellenmuster

**Häufigste Schwachstellen in JavaScript**:
1. **XSS** (CWE-79): innerHTML mit Benutzereingaben, eval()-Verwendung
2. **Prototype Pollution** (CWE-1321): Unsicheres Object-Merging
3. **CSRF** (CWE-352): Fehlende CSRF-Tokens in Formularen
4. **Open Redirect** (CWE-601): Nicht validierte Redirect-Ziele
5. **ReDoS** (CWE-1333): Denial-of-Service durch reguläre Ausdrücke

## XSS-Verhinderung

✅ **KORREKT — textContent oder Framework-Auto-Escaping verwenden**:
```javascript
// Vanilla JS — textContent verwenden (nicht innerHTML)
element.textContent = userInput;  // Sicher — escaped automatisch

// React — JSX escaped standardmässig automatisch
function Welcome({ name }) {
  return <h1>Welcome {name}</h1>;  // Automatisch escaped
}

// Vue — Templates escaped standardmässig automatisch
<template>
  <h1>Welcome {{ userName }}</h1>  <!-- Automatisch escaped -->
</template>
```

❌ **UNSICHER — innerHTML mit Benutzereingaben**:
```javascript
// NIEMALS innerHTML mit Benutzereingaben verwenden
element.innerHTML = userInput;  // XSS-Schwachstelle!

// Auch mit Template Literals
element.innerHTML = `<h1>Welcome ${userInput}</h1>`;  // XSS!

// React — dangerouslySetInnerHTML (vermeiden!)
<div dangerouslySetInnerHTML={{__html: userInput}} />  // XSS!
```

## Verhinderung von Prototype Pollution

✅ **KORREKT — Sichere Object-Operationen**:
```javascript
// Object.create(null) für sichere Objekte verwenden
const safeObj = Object.create(null);
safeObj[userKey] = userValue;  // Keine Prototype Pollution

// Oder Schlüssel vor Zuweisung validieren
function safeAssign(obj, key, value) {
  if (key === '__proto__' || key === 'constructor' || key === 'prototype') {
    throw new Error('Verbotener Schlüssel');
  }
  obj[key] = value;
}

// Object.freeze() für unveränderliche Objekte verwenden
const config = Object.freeze({ apiKey: 'secret' });
```

❌ **UNSICHER — Direkte Property-Zuweisung**:
```javascript
// Prototype-Pollution-Schwachstelle
const obj = {};
obj[userControlledKey] = userValue;  // Wenn userControlledKey '__proto__' ist

// Unsichere Merge-Operationen
Object.assign(target, userInput);  // Kann Prototype kontaminieren
```

## CSRF-Schutz

✅ **KORREKT — CSRF-Tokens verwenden**:
```javascript
// Express.js mit csurf-Middleware
const csrf = require('csurf');
const csrfProtection = csrf({ cookie: true });

app.post('/transfer', csrfProtection, (req, res) => {
  // CSRF-Token wird automatisch validiert
  processTransfer(req.body);
});

// Frontend — CSRF-Token in Formulare einbinden
<form method="POST" action="/transfer">
  <input type="hidden" name="_csrf" value="{{csrfToken}}">
  <button type="submit">Übertragen</button>
</form>

// Für AJAX-Requests
fetch('/api/transfer', {
  method: 'POST',
  headers: {
    'CSRF-Token': csrfToken,
    'Content-Type': 'application/json'
  },
  body: JSON.stringify(data)
});
```

## Sicheres Password-Hashing (Node.js)

✅ **KORREKT — bcrypt**:
```javascript
const bcrypt = require('bcrypt');

// Passwort hashen
const saltRounds = 12;
const hash = await bcrypt.hash(password, saltRounds);

// Passwort verifizieren
const match = await bcrypt.compare(password, hash);
if (match) {
  console.log('Passwort korrekt');
}
```

❌ **UNSICHER — crypto.createHash()**:
```javascript
const crypto = require('crypto');

// NIEMALS MD5 oder SHA für Passwörter verwenden
const hash = crypto.createHash('md5').update(password).digest('hex');  // Angreifbar!
const hash = crypto.createHash('sha256').update(password).digest('hex');  // Immer noch schwach!
```

## Sichere Zufallsgenerierung (Node.js)

✅ **KORREKT — crypto.randomBytes()**:
```javascript
const crypto = require('crypto');

// Sicheres zufälliges Token generieren
const token = crypto.randomBytes(32).toString('hex');

// Sichere Zufallszahl generieren
const randomValue = crypto.randomInt(0, 100);
```

❌ **UNSICHER — Math.random()**:
```javascript
// NIEMALS Math.random() für Sicherheitszwecke verwenden
const token = Math.random().toString(36).substring(2);  // NICHT sicher!
```

## eval() und dynamische Code-Ausführung vermeiden

❌ **GEFÄHRLICH — eval() mit Benutzereingaben**:
```javascript
// NIEMALS eval() mit Benutzereingaben verwenden
eval(userInput);  // Remote Code Execution!

// Ebenfalls gefährlich
new Function(userInput)();  // Remote Code Execution!
setTimeout(userInput, 1000);  // Code-Injection!
```

✅ **SICHERER — JSON.parse() oder spezifisches Parsing**:
```javascript
// Für Daten JSON.parse() verwenden
const data = JSON.parse(userInput);  // Sicher, wenn Eingabe JSON ist

// Für Ausdrücke eine Expression-Parser-Bibliothek verwenden
const mathjs = require('mathjs');
const result = mathjs.evaluate(userInput);  // Gesandboxte Auswertung
```

---

# Java-Sicherheitsrichtlinien

## Häufige Schwachstellenmuster

**Häufigste Schwachstellen in Java**:
1. **SQL-Injection** (CWE-89): String-Verkettung in Abfragen
2. **XXE** (CWE-611): XML External Entity-Angriffe
3. **Deserialisierung** (CWE-502): Unsicherer ObjectInputStream
4. **Path Traversal** (CWE-22): Nicht validierte Dateipfade
5. **Schwache Kryptographie** (CWE-327): Verwendung von DES, MD5, schwachem RNG

## Verhinderung von SQL-Injection

✅ **KORREKT — PreparedStatement**:
```java
// JDBC PreparedStatement
String query = "SELECT * FROM users WHERE id = ?";
PreparedStatement stmt = connection.prepareStatement(query);
stmt.setInt(1, userId);
ResultSet rs = stmt.executeQuery();

// JPA/Hibernate (parametrisiert)
String jpql = "SELECT u FROM User u WHERE u.id = :userId";
TypedQuery<User> query = em.createQuery(jpql, User.class);
query.setParameter("userId", userId);
User user = query.getSingleResult();
```

❌ **UNSICHER — String-Verkettung**:
```java
// NIEMALS Strings für SQL verketten
String query = "SELECT * FROM users WHERE id = " + userId;  // SQL-Injection!
Statement stmt = connection.createStatement();
ResultSet rs = stmt.executeQuery(query);
```

## XXE-Verhinderung

✅ **KORREKT — Externe Entities deaktivieren**:
```java
import javax.xml.parsers.DocumentBuilderFactory;

DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();

// Externe Entities deaktivieren, um XXE zu verhindern
dbf.setFeature("http://apache.org/xml/features/disallow-doctype-decl", true);
dbf.setFeature("http://xml.org/sax/features/external-general-entities", false);
dbf.setFeature("http://xml.org/sax/features/external-parameter-entities", false);
dbf.setXIncludeAware(false);
dbf.setExpandEntityReferences(false);

DocumentBuilder db = dbf.newDocumentBuilder();
Document doc = db.parse(inputStream);
```

## Sichere Deserialisierung

✅ **KORREKT — Look-Ahead Deserialization Filter verwenden (Java 9+)**:
```java
// Erlaubte Klassen für die Deserialisierung festlegen
ObjectInputFilter filter = ObjectInputFilter.Config.createFilter(
    "com.myapp.model.*;!*"  // Nur Klassen aus com.myapp.model erlauben
);

ObjectInputStream ois = new ObjectInputStream(inputStream);
ois.setObjectInputFilter(filter);
Object obj = ois.readObject();
```

❌ **UNSICHER — Uneingeschränktes readObject()**:
```java
// NIEMALS nicht vertrauenswürdige Daten ohne Validierung deserialisieren
ObjectInputStream ois = new ObjectInputStream(inputStream);
Object obj = ois.readObject();  // Deserialisierungs-Schwachstelle!
```

## Sichere Zufallsgenerierung

✅ **KORREKT — SecureRandom**:
```java
import java.security.SecureRandom;

SecureRandom random = new SecureRandom();
byte[] token = new byte[32];
random.nextBytes(token);
```

❌ **UNSICHER — java.util.Random**:
```java
import java.util.Random;

Random random = new Random();
int value = random.nextInt();  // NICHT kryptographisch sicher!
```

---

# C#/.NET-Sicherheitsrichtlinien

## Häufige Schwachstellenmuster

**Häufigste Schwachstellen in C#/.NET**:
1. **SQL-Injection** (CWE-89): String-Interpolation in Abfragen
2. **XSS** (CWE-79): Nicht kodierte Ausgabe in Razor-Views
3. **Path Traversal** (CWE-22): Nicht validierte Dateipfade
4. **XXE** (CWE-611): XML-Parsing-Schwachstellen
5. **Deserialisierung** (CWE-502): BinaryFormatter-Verwendung

## Verhinderung von SQL-Injection

✅ **KORREKT — Parametrisierte Abfragen**:
```csharp
// ADO.NET mit Parametern
string query = "SELECT * FROM Users WHERE Id = @userId";
using (SqlCommand cmd = new SqlCommand(query, connection))
{
    cmd.Parameters.AddWithValue("@userId", userId);
    SqlDataReader reader = cmd.ExecuteReader();
}

// Entity Framework (LINQ — automatisch parametrisiert)
var user = context.Users.FirstOrDefault(u => u.Id == userId);
```

❌ **UNSICHER — String-Interpolation**:
```csharp
// NIEMALS String-Interpolation für SQL verwenden
string query = $"SELECT * FROM Users WHERE Id = {userId}";  // SQL-Injection!
SqlCommand cmd = new SqlCommand(query, connection);
```

## XSS-Verhinderung in Razor

✅ **KORREKT — Razor Auto-Encoding**:
```csharp
@* Razor kodiert standardmässig automatisch als HTML *@
<h1>Welcome @Model.UserName</h1>  @* Automatisch kodiert *@
```

❌ **UNSICHER — Html.Raw()**:
```csharp
@* NIEMALS Html.Raw() mit Benutzereingaben verwenden *@
<div>@Html.Raw(Model.UserInput)</div>  @* XSS-Schwachstelle! *@
```

## Sicheres Password-Hashing

✅ **KORREKT — ASP.NET Core Identity oder Rfc2898DeriveBytes**:
```csharp
using Microsoft.AspNetCore.Identity;

// ASP.NET Core Identity (empfohlen)
var passwordHasher = new PasswordHasher<User>();
string hash = passwordHasher.HashPassword(user, password);

// Verifizieren
var result = passwordHasher.VerifyHashedPassword(user, hash, password);
if (result == PasswordVerificationResult.Success)
{
    // Passwort korrekt
}

// Manuelles PBKDF2 (wenn Identity nicht verfügbar)
using System.Security.Cryptography;

byte[] salt = new byte[16];
using (var rng = RandomNumberGenerator.Create())
{
    rng.GetBytes(salt);
}

var pbkdf2 = new Rfc2898DeriveBytes(password, salt, 100000, HashAlgorithmName.SHA256);
byte[] hash = pbkdf2.GetBytes(32);
```

## Sichere Deserialisierung

✅ **KORREKT — JSON.NET oder System.Text.Json verwenden**:
```csharp
using System.Text.Json;

// JSON-Serialisierung verwenden (sicher)
string json = JsonSerializer.Serialize(obj);
var obj = JsonSerializer.Deserialize<MyClass>(json);
```

❌ **UNSICHER — BinaryFormatter**:
```csharp
// NIEMALS BinaryFormatter mit nicht vertrauenswürdigen Daten verwenden
BinaryFormatter formatter = new BinaryFormatter();
object obj = formatter.Deserialize(stream);  // Deserialisierungs-Schwachstelle!
```

---

# Go-Sicherheitsrichtlinien

## Häufige Schwachstellenmuster

**Häufigste Schwachstellen in Go**:
1. **SQL-Injection** (CWE-89): String-Formatierung in Abfragen
2. **Command-Injection** (CWE-78): Unsichere exec.Command-Verwendung
3. **Path Traversal** (CWE-22): Nicht validierte Dateipfade
4. **Race Conditions** (CWE-362): Unzureichende Goroutine-Synchronisation
5. **Schwache Kryptographie** (CWE-327): Verwendung von MD5, unsicherem Zufallsgenerator

## Verhinderung von SQL-Injection

✅ **KORREKT — Parametrisierte Abfragen**:
```go
// database/sql mit Parametern
query := "SELECT * FROM users WHERE id = $1"
row := db.QueryRow(query, userId)

// Mit sqlx
var user User
err := db.Get(&user, "SELECT * FROM users WHERE id=$1", userId)
```

❌ **UNSICHER — fmt.Sprintf() für SQL**:
```go
// NIEMALS fmt.Sprintf() für SQL verwenden
query := fmt.Sprintf("SELECT * FROM users WHERE id = %d", userId)  // SQL-Injection!
rows, err := db.Query(query)
```

## Verhinderung von Command-Injection

✅ **KORREKT — exec.Command mit separaten Argumenten**:
```go
import "os/exec"

// Argumente separat übergeben
cmd := exec.Command("ls", "-l", directory)
output, err := cmd.Output()
```

❌ **UNSICHER — exec.Command mit Shell**:
```go
// NIEMALS Shell mit Benutzereingaben verwenden
cmd := exec.Command("sh", "-c", fmt.Sprintf("ls -l %s", directory))  // Command-Injection!
```

## Sicheres Password-Hashing

✅ **KORREKT — golang.org/x/crypto/bcrypt**:
```go
import "golang.org/x/crypto/bcrypt"

// Passwort hashen
hash, err := bcrypt.GenerateFromPassword([]byte(password), bcrypt.DefaultCost)

// Passwort verifizieren
err = bcrypt.CompareHashAndPassword(hash, []byte(password))
if err == nil {
    // Passwort korrekt
}
```

## Sichere Zufallsgenerierung

✅ **KORREKT — crypto/rand**:
```go
import "crypto/rand"

// Sichere zufällige Bytes generieren
token := make([]byte, 32)
_, err := rand.Read(token)
```

❌ **UNSICHER — math/rand**:
```go
import "math/rand"

// NIEMALS math/rand für Sicherheitszwecke verwenden
value := rand.Intn(100)  // NICHT kryptographisch sicher!
```

---

# SQL-Sicherheitsrichtlinien (sprachübergreifend)

## Parametrisierte Abfragen nach Datenbank

**PostgreSQL**:
```sql
-- Parametrisierte Abfrage (sicher)
SELECT * FROM users WHERE id = $1;  -- Parameter: userId
```

**MySQL**:
```sql
-- Parametrisierte Abfrage (sicher)
SELECT * FROM users WHERE id = ?;  -- Parameter: userId
```

**SQL Server**:
```sql
-- Parametrisierte Abfrage (sicher)
SELECT * FROM users WHERE id = @userId;  -- Parameter: @userId
```

## Datenbankkonten mit minimalen Rechten

✅ **KORREKT — Minimale Berechtigungen**:
```sql
-- Anwendungsspezifischen Benutzer mit minimalen Berechtigungen erstellen
CREATE USER app_user WITH PASSWORD 'secure_password';

-- Nur notwendige Berechtigungen erteilen
GRANT SELECT, INSERT, UPDATE ON users TO app_user;
GRANT SELECT ON products TO app_user;

-- Gefährliche Berechtigungen entziehen
REVOKE DROP, CREATE, ALTER ON DATABASE FROM app_user;
```

## Dynamisches SQL in Stored Procedures vermeiden

❌ **UNSICHER — Dynamisches SQL in Stored Procedure**:
```sql
-- SQL-Injection-Schwachstelle in Stored Procedure
CREATE PROCEDURE GetUserById(@userId VARCHAR(50))
AS
BEGIN
    DECLARE @sql NVARCHAR(MAX);
    SET @sql = 'SELECT * FROM users WHERE id = ' + @userId;  -- SQL-Injection!
    EXEC sp_executesql @sql;
END
```

✅ **KORREKT — Parametrisierte Stored Procedure**:
```sql
-- Sichere parametrisierte Stored Procedure
CREATE PROCEDURE GetUserById(@userId INT)
AS
BEGIN
    SELECT * FROM users WHERE id = @userId;  -- Sicher
END
```

---

# Dokumentenpflege

**Aktualisierungsfrequenz**: Halbjährlich oder wenn:

- Neue Hauptversion einer Sprache erscheint (Python 3.x, Java 17+, Node.js LTS)
- Neue Sicherheitsfunktionen in Frameworks verfügbar
- OWASP Top 10 aktualisiert wird
- Sich die sprachliche Nutzung in der Organisation ändert

**Verantwortlicher**: Application Security Lead

**Überprüfungsauslöser**:

- Neue Schwachstellenmuster entdeckt
- Sicherheitshinweise zu Sprachen/Frameworks veröffentlicht
- Entwickler-Feedback zu unklaren Anleitungen
- Änderungen bei Tool-Integrationen (neue SAST-Regeln)

**Zusammenarbeit**:

- Senior-Entwickler prüfen auf technische Korrektheit
- Security Champions validieren die praktische Anwendbarkeit
- Entwicklungsteams geben Feedback zur Benutzerfreundlichkeit

**Versionshistorie**:

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | [Datum] | Application Security Lead | Erstveröffentlichung — sprachspezifische Leitlinien aus konsolidierter Richtlinie extrahiert |

---

**ENDE VON ISMS-CTX-A.8.28**

*Dieses technische Referenzdokument unterstützt die Umsetzung von ISMS-POL-A.8.28. Verbindliche Anforderungen sind in der Richtlinie, nicht in diesem Dokument, festgelegt.*

**DIESES DOKUMENT IST NICHT BESTANDTEIL DES ISMS.**

<!-- QA_VERIFIED: 2026-03-29 -->
