<!-- ISMS-CORE:CTX:ISMS-CTX-A.8.28-IT-language-specific-secure-coding:framework:CTX:a.8.28 -->
**ISMS-CTX-A.8.28 — Linee guida di codifica sicura specifiche per linguaggio**

**Controllo del documento — ISMS-CTX-A.8.28**

| Campo | Valore |
|-------|--------|
| **Titolo del documento** | Linee guida di codifica sicura specifiche per linguaggio |
| **Tipo di documento** | Contesto tecnico (CTX) |
| **Identificativo del documento** | ISMS-CTX-A.8.28 |
| **Autore del documento** | Responsabile della sicurezza applicativa |
| **Proprietario del documento** | Responsabile della sicurezza applicativa |
| **Approvato da** | Responsabile della sicurezza applicativa |
| **Data di creazione** | [Data] |
| **Versione** | 1.0 |
| **Classificazione** | Interno |
| **Stato** | Bozza |

---

## Avvertenza

**CRITICO**: Si tratta di un documento di riferimento informativo e **NON** fa parte del quadro formale delle politiche SGSI. I requisiti di politica vincolanti sono definiti in **ISMS-POL-A.8.28 (Politica di codifica sicura)**.

---

# Scopo e ambito

## Obiettivo del documento

Questo documento fornisce **modelli di codifica sicura specifici per linguaggio** che operazionalizzano i requisiti di sicurezza generici di ISMS-POL-A.8.28. Le vulnerabilità di sicurezza si manifestano in modo diverso tra i linguaggi di programmazione a causa delle scelte di progettazione del linguaggio, delle implementazioni della libreria standard, dei framework comuni e delle pratiche della comunità di sviluppo.

**Questo documento risponde a**: «Come implemento gli standard di codifica sicura *in questo linguaggio specifico*?»

## Priorità dei linguaggi

Linguaggi coperti in base all'utilizzo organizzativo:

1. **Python** (servizi backend, elaborazione dati, automazione)
2. **JavaScript/TypeScript** (frontend, backend Node.js)
3. **Java** (applicazioni enterprise, microservizi)
4. **C#/.NET** (applicazioni Windows, servizi Azure)
5. **Go** (strumenti infrastruttura, microservizi cloud-native)
6. **SQL** (multilingua, accesso ai dati)

## Relazione con la politica

**ISMS-POL-A.8.28 stabilisce** (vincolante):

- Obbligo di seguire standard di codifica sicura
- Obbligo di validazione degli input, codifica degli output, autenticazione sicura
- Obbligo di evitare pratiche vietate (segreti codificati, crittografia debole)

**Questo documento CTX fornisce** (informativo):

- Come implementare tali requisiti in Python, JavaScript, Java, C#, Go, SQL

## Riferimenti esterni

- **OWASP Cheat Sheet Series**: https://cheatsheetseries.owasp.org/
- **SEI CERT Coding Standards**: https://wiki.sei.cmu.edu/confluence/
- **CWE (Common Weakness Enumeration)**: https://cwe.mitre.org/

---

# Linee guida di sicurezza Python

## Pattern di vulnerabilità comuni

**Principali vulnerabilità in Python**:
1. **Iniezione SQL** (CWE-89): Formattazione di stringhe nelle query
2. **Iniezione di comandi** (CWE-78): Uso non sicuro di `os.system()`, `subprocess` con `shell=True`
3. **Deserializzazione** (CWE-502): Uso non sicuro di pickle
4. **Traversata del percorso** (CWE-22): Percorsi dei file non validati
5. **Crittografia debole** (CWE-327): Uso di MD5/SHA1, numero casuale non sicuro

## Prevenzione dell'iniezione SQL

✅ **CORRETTO — Query parametrizzate**:
```python
# sqlite3
cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))

# psycopg2 (PostgreSQL)
cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))

# SQLAlchemy ORM
user = session.query(User).filter(User.id == user_id).first()
```

❌ **PERICOLOSO — Formattazione di stringhe**:
```python
# NON usare MAI f-string per SQL
cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")  # Iniezione SQL!
cursor.execute("SELECT * FROM users WHERE id = {}".format(user_id))  # Iniezione SQL!
```

## Prevenzione dell'iniezione di comandi

✅ **CORRETTO — Argomenti in lista, nessuna shell**:
```python
import subprocess

# Passare gli argomenti come lista, shell=False (predefinito)
result = subprocess.run(['ls', '-l', directory_name],
                       capture_output=True, check=True)

# Per nomi file con caratteri speciali
import shlex
filename = shlex.quote(user_filename)
subprocess.run(['tar', '-czf', 'backup.tar.gz', filename])
```

❌ **PERICOLOSO — Stringhe di comandi shell**:
```python
# NON usare MAI shell=True con input utente
subprocess.run(f'ls -l {directory_name}', shell=True)  # Iniezione di comandi!
os.system(f'rm {filename}')  # Iniezione di comandi!
```

## Prevenzione della traversata del percorso

✅ **CORRETTO — Validare e risolvere i percorsi**:
```python
from pathlib import Path

UPLOAD_DIR = Path('/var/app/uploads')

def accesso_file_sicuro(nome_file_utente):
    percorso_richiesto = (UPLOAD_DIR / nome_file_utente).resolve()
    
    if not percorso_richiesto.is_relative_to(UPLOAD_DIR):
        raise ValueError("Percorso file non valido")
    
    return percorso_richiesto
```

❌ **PERICOLOSO — Concatenazione diretta del percorso**:
```python
# Traversata del percorso: user_input potrebbe essere "../../etc/passwd"
filepath = f'/var/app/uploads/{user_input}'
with open(filepath, 'r') as f:  # Può accedere a qualsiasi file!
    content = f.read()
```

## Hashing sicuro delle password

✅ **CORRETTO — bcrypt o Argon2**:
```python
import bcrypt

# Hashing
password = b"password_utente"
salt = bcrypt.gensalt(rounds=12)
hashed = bcrypt.hashpw(password, salt)

# Verifica
if bcrypt.checkpw(password, hashed):
    print("Password corretta")

# O Argon2 (raccomandato per nuovi sistemi)
from argon2 import PasswordHasher
ph = PasswordHasher()
hash = ph.hash("password_utente")
ph.verify(hash, "password_utente")
```

❌ **PERICOLOSO — MD5, SHA1, o testo in chiaro**:
```python
import hashlib
# NON usare MAI MD5 o SHA1 per le password
hashed = hashlib.md5(password.encode()).hexdigest()  # Vulnerabile!
hashed = hashlib.sha1(password.encode()).hexdigest()  # Vulnerabile!
```

## Generazione sicura di numeri casuali

✅ **CORRETTO — Modulo secrets**:
```python
import secrets

token = secrets.token_urlsafe(32)  # 32 byte = 256 bit
random_number = secrets.randbelow(100)
```

❌ **PERICOLOSO — Modulo random**:
```python
import random
# NON usare MAI il modulo random per la sicurezza
token = random.randint(0, 1000000)  # NON crittograficamente sicuro!
```

## Sicurezza della deserializzazione

✅ **CORRETTO — Usare JSON o Unpickler limitato**:
```python
import json
data = json.loads(user_input)  # Sicuro

# Se pickle necessario, limitare le classi consentite
import pickle, io

class UnpicklerLimitato(pickle.Unpickler):
    def find_class(self, module, name):
        if module == "myapp.models" and name in ["User", "Config"]:
            return super().find_class(module, name)
        raise pickle.UnpicklingError(f"Classe vietata: {module}.{name}")

def unpickle_sicuro(data):
    return UnpicklerLimitato(io.BytesIO(data)).load()
```

❌ **PERICOLOSO — pickle.loads() senza restrizioni**:
```python
import pickle
# NON deserializzare MAI dati non attendibili
obj = pickle.loads(user_input)  # Rischio esecuzione di codice remoto!
```

---

# Linee guida di sicurezza JavaScript/TypeScript

## Pattern di vulnerabilità comuni

**Principali vulnerabilità in JavaScript**:
1. **XSS** (CWE-79): innerHTML con input utente, uso di eval()
2. **Inquinamento del prototipo** (CWE-1321): Fusione di oggetti non sicura
3. **CSRF** (CWE-352): Token CSRF mancanti
4. **Reindirizzamento aperto** (CWE-601): Destinazioni di reindirizzamento non validate
5. **ReDoS** (CWE-1333): Denial of service da espressioni regolari

## Prevenzione XSS

✅ **CORRETTO — textContent o escape automatico del framework**:
```javascript
// JS vanilla - usare textContent (non innerHTML)
element.textContent = userInput;  // Sicuro - escape automatico

// React - JSX esegue l'escape automatico per impostazione predefinita
function Benvenuto({ name }) {
  return <h1>Benvenuto {name}</h1>;  // Escape automatico
}

// Vue - i template eseguono l'escape automatico per impostazione predefinita
<template>
  <h1>Benvenuto {{ userName }}</h1>  <!-- Escape automatico -->
</template>
```

❌ **PERICOLOSO — innerHTML con input utente**:
```javascript
// NON usare MAI innerHTML con input utente
element.innerHTML = userInput;  // Vulnerabilità XSS!

// React - dangerouslySetInnerHTML (evitare!)
<div dangerouslySetInnerHTML={{__html: userInput}} />  // XSS!
```

## Prevenzione dell'inquinamento del prototipo

✅ **CORRETTO — Operazioni sicure sugli oggetti**:
```javascript
// Usare Object.create(null) per oggetti sicuri
const oggettoSicuro = Object.create(null);
oggettoSicuro[userKey] = userValue;

// O validare le chiavi prima dell'assegnazione
function assegnazioneSicura(obj, chiave, valore) {
  if (['__proto__', 'constructor', 'prototype'].includes(chiave)) {
    throw new Error('Chiave vietata');
  }
  obj[chiave] = valore;
}
```

## Protezione CSRF

✅ **CORRETTO — Usare token CSRF**:
```javascript
// Express.js con csurf
const csrf = require('csurf');
const protezioneCsrf = csrf({ cookie: true });

app.post('/trasferimento', protezioneCsrf, (req, res) => {
  elaboraTrasferimento(req.body);
});

// Frontend - includere il token CSRF
<form method="POST" action="/trasferimento">
  <input type="hidden" name="_csrf" value="{{csrfToken}}">
  <button type="submit">Trasferisci</button>
</form>

// Per richieste AJAX
fetch('/api/trasferimento', {
  method: 'POST',
  headers: {
    'CSRF-Token': csrfToken,
    'Content-Type': 'application/json'
  },
  body: JSON.stringify(data)
});
```

## Hashing sicuro delle password (Node.js)

✅ **CORRETTO — bcrypt**:
```javascript
const bcrypt = require('bcrypt');

const saltRounds = 12;
const hash = await bcrypt.hash(password, saltRounds);

const match = await bcrypt.compare(password, hash);
if (match) { /* Password corretta */ }
```

❌ **PERICOLOSO — crypto.createHash()**:
```javascript
const crypto = require('crypto');
// NON usare MAI MD5 o SHA per le password
const hash = crypto.createHash('md5').update(password).digest('hex');  // Vulnerabile!
```

## Generazione casuale sicura (Node.js)

✅ **CORRETTO — crypto.randomBytes()**:
```javascript
const crypto = require('crypto');
const token = crypto.randomBytes(32).toString('hex');
const randomValue = crypto.randomInt(0, 100);
```

❌ **PERICOLOSO — Math.random()**:
```javascript
// NON usare MAI Math.random() per la sicurezza
const token = Math.random().toString(36).substring(2);  // NON sicuro!
```

## Evitare eval() e l'esecuzione di codice dinamico

❌ **PERICOLOSO — eval() con input utente**:
```javascript
eval(userInput);  // Esecuzione di codice remoto!
new Function(userInput)();  // Esecuzione di codice remoto!
setTimeout(userInput, 1000);  // Iniezione di codice!
```

---

# Linee guida di sicurezza Java

## Pattern di vulnerabilità comuni

**Principali vulnerabilità in Java**:
1. **Iniezione SQL** (CWE-89): Concatenazione di stringhe nelle query
2. **XXE** (CWE-611): Attacchi di entità esterne XML
3. **Deserializzazione** (CWE-502): ObjectInputStream non sicuro
4. **Traversata del percorso** (CWE-22): Percorsi non validati
5. **Crittografia debole** (CWE-327): DES, MD5, RNG debole

## Prevenzione dell'iniezione SQL

✅ **CORRETTO — PreparedStatement**:
```java
// JDBC PreparedStatement
String query = "SELECT * FROM users WHERE id = ?";
PreparedStatement stmt = connection.prepareStatement(query);
stmt.setInt(1, userId);
ResultSet rs = stmt.executeQuery();

// JPA/Hibernate (parametrizzato)
TypedQuery<User> query = em.createQuery(
    "SELECT u FROM User u WHERE u.id = :userId", User.class);
query.setParameter("userId", userId);
```

❌ **PERICOLOSO — Concatenazione di stringhe**:
```java
// NON concatenare MAI stringhe per SQL
String query = "SELECT * FROM users WHERE id = " + userId;  // Iniezione SQL!
```

## Prevenzione XXE

✅ **CORRETTO — Disabilitare le entità esterne**:
```java
DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
dbf.setFeature("http://apache.org/xml/features/disallow-doctype-decl", true);
dbf.setFeature("http://xml.org/sax/features/external-general-entities", false);
dbf.setFeature("http://xml.org/sax/features/external-parameter-entities", false);
dbf.setXIncludeAware(false);
dbf.setExpandEntityReferences(false);
DocumentBuilder db = dbf.newDocumentBuilder();
```

## Deserializzazione sicura

✅ **CORRETTO — Filtro di deserializzazione look-ahead (Java 9+)**:
```java
ObjectInputFilter filter = ObjectInputFilter.Config.createFilter(
    "com.myapp.model.*;!*"
);
ObjectInputStream ois = new ObjectInputStream(inputStream);
ois.setObjectInputFilter(filter);
Object obj = ois.readObject();
```

❌ **PERICOLOSO — readObject() senza restrizioni**:
```java
// NON deserializzare MAI dati non attendibili
ObjectInputStream ois = new ObjectInputStream(inputStream);
Object obj = ois.readObject();  // Vulnerabilità di deserializzazione!
```

## Generazione casuale sicura

✅ **CORRETTO — SecureRandom**:
```java
import java.security.SecureRandom;
SecureRandom random = new SecureRandom();
byte[] token = new byte[32];
random.nextBytes(token);
```

❌ **PERICOLOSO — java.util.Random**:
```java
Random random = new Random();
int value = random.nextInt();  // NON crittograficamente sicuro!
```

---

# Linee guida di sicurezza C#/.NET

## Prevenzione dell'iniezione SQL

✅ **CORRETTO — Query parametrizzate**:
```csharp
// ADO.NET con parametri
string query = "SELECT * FROM Users WHERE Id = @userId";
using (SqlCommand cmd = new SqlCommand(query, connection))
{
    cmd.Parameters.AddWithValue("@userId", userId);
    SqlDataReader reader = cmd.ExecuteReader();
}

// Entity Framework (LINQ — parametrizzato automaticamente)
var user = context.Users.FirstOrDefault(u => u.Id == userId);
```

❌ **PERICOLOSO — Interpolazione di stringhe**:
```csharp
string query = $"SELECT * FROM Users WHERE Id = {userId}";  // Iniezione SQL!
```

## Prevenzione XSS in Razor

✅ **CORRETTO — Auto-codifica Razor**:
```csharp
@* Razor codifica automaticamente l'HTML per impostazione predefinita *@
<h1>Benvenuto @Model.UserName</h1>  @* Auto-codificato *@
```

❌ **PERICOLOSO — Html.Raw()**:
```csharp
<div>@Html.Raw(Model.UserInput)</div>  @* Vulnerabilità XSS! *@
```

## Hashing sicuro delle password

✅ **CORRETTO — ASP.NET Core Identity**:
```csharp
using Microsoft.AspNetCore.Identity;

var passwordHasher = new PasswordHasher<User>();
string hash = passwordHasher.HashPassword(user, password);

var result = passwordHasher.VerifyHashedPassword(user, hash, password);
if (result == PasswordVerificationResult.Success)
{ /* Password corretta */ }
```

## Deserializzazione sicura

✅ **CORRETTO — JSON.NET o System.Text.Json**:
```csharp
using System.Text.Json;
var obj = JsonSerializer.Deserialize<MyClass>(json);
```

❌ **PERICOLOSO — BinaryFormatter**:
```csharp
BinaryFormatter formatter = new BinaryFormatter();
object obj = formatter.Deserialize(stream);  // Vulnerabilità di deserializzazione!
```

---

# Linee guida di sicurezza Go

## Prevenzione dell'iniezione SQL

✅ **CORRETTO — Query parametrizzate**:
```go
query := "SELECT * FROM users WHERE id = $1"
row := db.QueryRow(query, userId)
```

❌ **PERICOLOSO — fmt.Sprintf() per SQL**:
```go
query := fmt.Sprintf("SELECT * FROM users WHERE id = %d", userId)  // Iniezione SQL!
```

## Prevenzione dell'iniezione di comandi

✅ **CORRETTO — exec.Command con argomenti separati**:
```go
import "os/exec"
cmd := exec.Command("ls", "-l", directory)
output, err := cmd.Output()
```

❌ **PERICOLOSO — exec.Command con shell**:
```go
cmd := exec.Command("sh", "-c", fmt.Sprintf("ls -l %s", directory))  // Iniezione!
```

## Hashing sicuro delle password

✅ **CORRETTO — golang.org/x/crypto/bcrypt**:
```go
import "golang.org/x/crypto/bcrypt"

hash, err := bcrypt.GenerateFromPassword([]byte(password), bcrypt.DefaultCost)

err = bcrypt.CompareHashAndPassword(hash, []byte(password))
if err == nil { /* Password corretta */ }
```

## Generazione casuale sicura

✅ **CORRETTO — crypto/rand**:
```go
import "crypto/rand"
token := make([]byte, 32)
_, err := rand.Read(token)
```

❌ **PERICOLOSO — math/rand**:
```go
import "math/rand"
value := rand.Intn(100)  // NON crittograficamente sicuro!
```

---

# Linee guida di sicurezza SQL (multilingua)

## Query parametrizzate per database

```sql
-- PostgreSQL
SELECT * FROM users WHERE id = $1;

-- MySQL
SELECT * FROM users WHERE id = ?;

-- SQL Server
SELECT * FROM users WHERE id = @userId;
```

## Account database con minimi privilegi

✅ **CORRETTO — Permessi minimi**:
```sql
CREATE USER app_user WITH PASSWORD 'password_sicura';

GRANT SELECT, INSERT, UPDATE ON users TO app_user;
GRANT SELECT ON products TO app_user;

REVOKE DROP, CREATE, ALTER ON DATABASE FROM app_user;
```

## Evitare SQL dinamico nelle stored procedure

❌ **PERICOLOSO — SQL dinamico in una stored procedure**:
```sql
CREATE PROCEDURE GetUserById(@userId VARCHAR(50))
AS BEGIN
    DECLARE @sql NVARCHAR(MAX);
    SET @sql = 'SELECT * FROM users WHERE id = ' + @userId;  -- Iniezione SQL!
    EXEC sp_executesql @sql;
END
```

✅ **CORRETTO — Stored procedure parametrizzata**:
```sql
CREATE PROCEDURE GetUserById(@userId INT)
AS BEGIN
    SELECT * FROM users WHERE id = @userId;  -- Sicuro
END
```

---

# Manutenzione del documento

**Frequenza di aggiornamento**: Semestrale o quando:

- Viene rilasciata una versione principale del linguaggio
- Sono disponibili nuove funzionalità di sicurezza del framework
- OWASP Top 10 viene aggiornato
- Vengono pubblicate avvertenze di sicurezza di linguaggi/framework

**Proprietario**: Responsabile della sicurezza applicativa

**Cronologia delle versioni**:

| Versione | Data | Autore | Modifiche |
|----------|------|--------|-----------|
| 1.0 | [Data] | Responsabile della sicurezza applicativa | Linee guida iniziali estratte dalla politica consolidata |

---

**FINE DI ISMS-CTX-A.8.28**

*Questo riferimento tecnico supporta l'implementazione di ISMS-POL-A.8.28. I requisiti vincolanti sono nella politica, non in questo documento.*
<!-- QA_VERIFIED: 2026-04-04 -->
