<!-- ISMS-CORE:REF:ISMS-REF-A.8.15-FR-logging-standards-reference:framework:REF:a.8.15 -->
**ISMS-REF-A.8.15 — Référence des normes de journalisation**
**Normes de format de journaux et spécifications techniques (Référence technique non-SMSI)**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Référence des normes de journalisation |
| **Type de document** | Interne — Référence technique (non SMSI) |
| **Identifiant du document** | ISMS-REF-A.8.15 |
| **Créateur du document** | Centre des opérations de sécurité (SOC) / Équipe d'architecture de sécurité |
| **Propriétaire du document** | Responsable de la sécurité de l'information |
| **Approuvé par** | RSSI (Référence technique — aucune approbation exécutive requise) |
| **Date de création** | [Date] |
| **Version** | 1.0 |
| **Date de version** | [À déterminer] |
| **Classification** | Interne |
| **Statut** | Brouillon |

**Historique des versions** :

| Version | Date | Auteur | Modifications |
|---------|------|--------|---------------|
| 1.0 | [Date] | SOC / Architecture de sécurité | Référence technique initiale pour la certification ISO 27001:2022 |

**Cycle de révision** : Trimestriel (les normes de format de journaux et les technologies évoluent fréquemment)  
**Prochaine date de révision** : [Date + 3 mois]  
**Approbateurs** : Responsable SOC / Équipe d'architecture de sécurité (référence technique, aucune approbation SMSI requise)

**Distribution** : Équipe SOC, Ingénieurs de sécurité, Administrateurs système, Développeurs d'applications (pour la sensibilisation technique à l'implémentation)

---

⚠️ **IMPORTANT — DOCUMENT DE SUPPORT TECHNIQUE NON-SMSI**

Ce document est fourni à des fins d'information et de sensibilisation uniquement.

- Ce document NE fait PAS partie du Système de management de la sécurité de l'information (SMSI).
- Ce document NE définit PAS de contrôles ou d'exigences de journalisation obligatoires.
- Ce document N'établit PAS d'exigences contraignantes, de délais, d'ICP ou de SLA.
- Ce document N'impose PAS l'utilisation, l'interdiction ou la configuration de formats de journaux, d'outils ou de plateformes spécifiques.
- Ce document NE remplace NI n'étend aucune politique SMSI.

Toutes les exigences de journalisation contraignantes, obligations et décisions de gouvernance sont définies exclusivement dans **ISMS-POL-A.8.15 (Politique de journalisation)** et autres documentations SMSI approuvées.

Ce document sert uniquement de référence technique pour :

- Décrire les formats de journaux et normes couramment utilisés
- Fournir des conventions de nommage des champs et des normes d'encodage
- Soutenir la planification de l'implémentation technique
- Informer la sélection de formats de journaux et le développement d'analyseurs syntaxiques
- **Ce document ne doit pas être utilisé comme preuve d'audit de l'implémentation**

L'utilisation de ce document n'implique pas d'implémentation, de conformité ou de maturité opérationnelle.

---

# Objectif et portée du document

## Objectif

Ce document fournit une référence technique pour les normes de format de journaux, les conventions de nommage des champs et les exigences d'encodage couramment utilisées dans les implémentations de journalisation de sécurité. Il vise à soutenir :

- L'implémentation technique des exigences de journalisation selon ISMS-POL-A.8.15
- La sélection de formats de journaux appropriés selon le type de système et les exigences d'intégration
- Le développement de règles d'analyse syntaxique des journaux et l'intégration SIEM
- La standardisation des noms de champs à travers les sources de journaux organisationnels
- La compréhension des formats de journaux standard du secteur (Syslog, CEF, JSON)

## Ce que ce document N'est PAS

Ce document NE :

- Définit PAS les formats de journaux approuvés ou interdits par [Organisation]
- N'établit PAS d'exigences d'implémentation obligatoires
- Ne crée PAS d'obligations de conformité ou de critères d'audit
- Ne remplace PAS les exigences de la politique ISMS-POL-A.8.15
- N'impose PAS de plateformes SIEM, d'outils de gestion des journaux ou de fournisseurs spécifiques

## Relation avec le SMSI

Ce document est une **référence technique non contraignante**. Toutes les exigences de contrôle de journalisation sont définies exclusivement dans ISMS-POL-A.8.15.

---

# Normes de format Syslog (RFC 5424)

## Vue d'ensemble

**Syslog (RFC 5424)** est le protocole de journalisation standard pour les composants d'infrastructure, les systèmes d'exploitation et les équipements réseau.

**Cas d'utilisation courants** :

- Équipements réseau (routeurs, commutateurs, pare-feu)
- Systèmes d'exploitation Unix/Linux
- Services d'infrastructure (DNS, DHCP, NTP)
- Applications legacy

**Protocole** :

- UDP port 514 (traditionnel, non chiffré — NON RECOMMANDÉ pour les journaux de sécurité)
- TCP port 514 ou 6514 (recommandé pour la fiabilité)
- TLS/TCP port 6514 (recommandé pour la transmission chiffrée selon ISMS-POL-A.8.15 Section 2.2.3)

## Format de message Syslog

**Structure de message RFC 5424** :

```
<PRI>VERSION TIMESTAMP HOSTNAME APP-NAME PROCID MSGID STRUCTURED-DATA MSG
```

**Exemple** :
```
<134>1 2026-01-21T14:32:15.003+01:00 server01.example.com sshd 1234 ID47 [exampleSDID@32473 iut="3" eventSource="Application" eventID="1011"] Échec de mot de passe pour utilisateur invalide admin depuis 10.0.1.50 port 22 ssh2
```

## Priorité Syslog (PRI)

**Calcul de la priorité** : `PRI = (Facility × 8) + Severity`

**Codes de facility** (courants) :

| Code | Facility | Utilisation |
|------|----------|-------------|
| 0 | kernel | Messages noyau |
| 1 | user | Messages utilisateur |
| 2 | mail | Système de messagerie |
| 3 | daemon | Démons système |
| 4 | auth | Sécurité / authentification |
| 5 | syslog | Interne Syslog |
| 10 | authpriv | Sécurité / autorisation (privé) |
| 16 | local0-7 | Usage local (applications personnalisées) |

**Niveaux de sévérité** :

| Code | Sévérité | Description | Recommandation d'utilisation |
|------|----------|-------------|------------------------------|
| 0 | Emergency | Système inutilisable | Panique système, crash imminent |
| 1 | Alert | Action immédiate requise | Défaillance de ressource critique, corruption de données |
| 2 | Critical | Conditions critiques | Erreur matérielle, défaillance de service critique |
| 3 | Error | Conditions d'erreur | Erreurs non critiques, défaillances d'application |
| 4 | Warning | Conditions d'avertissement | Erreurs récupérables, avertissements de ressources |
| 5 | Notice | Normal mais significatif | Événements significatifs (élévation de privilèges, changement de config) |
| 6 | Informational | Messages informatifs | Opérations normales, authentifications réussies |
| 7 | Debug | Messages de débogage | Informations détaillées de dépannage |

**Correspondance de sévérité recommandée** :

- **Événements de sécurité** : Notice (5) pour les opérations réussies, Warning (4) pour les violations de politique, Error (3) pour les attaques
- **Authentification** : Info (6) pour le succès, Warning (4) pour les tentatives échouées, Error (3) pour les verrouillages de compte
- **Événements système** : Variable selon le contexte (Critical pour les défaillances de service, Notice pour les changements de configuration)

## Format d'horodatage Syslog

**Format requis** : ISO 8601 avec fuseau horaire

```
AAAA-MM-JJTHH:MM:SS.SSSSSS+TZ
```

**Exemples** :

- `2026-01-21T14:32:15+01:00` (avec décalage de fuseau horaire)
- `2026-01-21T13:32:15Z` (notation UTC)
- `2026-01-21T14:32:15.003+01:00` (avec millisecondes)

**Bonnes pratiques** :

- Toujours inclure les informations de fuseau horaire
- Utiliser la précision en millisecondes pour les systèmes à volume élevé où l'ordonnancement des événements est critique
- Synchroniser les horloges système via NTP selon ISMS-POL-A.8.17
- Utiliser UTC pour les environnements multi-sites pour simplifier la corrélation

## Données structurées Syslog

**Format** : paires clé-valeur entre crochets

```
[SD-ID@PEN clé1="valeur1" clé2="valeur2"]
```

**Exemple** :
```
[secureAuth@123456 user="jdupont" src="10.0.1.50" action="login" result="success"]
```

**Éléments de données structurées recommandés** :

- `user="nom_utilisateur"` — identifiant utilisateur
- `src="adresse_IP"` — IP source
- `dst="adresse_IP"` — IP destination
- `action="verbe"` — action effectuée
- `result="success|failure"` — résultat
- `reason="description"` — motif d'échec ou contexte additionnel

## Exemple de configuration Syslog

**Configuration rsyslog Linux** (TCP avec TLS) :

```
# Envoyer les journaux de sécurité au SIEM central
*.* @@(o)siem.example.com:6514
$ActionSendStreamDriverMode 1
$ActionSendStreamDriverAuthMode x509/name
$ActionSendStreamDriverPermittedPeer siem.example.com
```

**Exemple de configuration Syslog équipement réseau** (Cisco) :

```
logging host 10.0.2.100 transport tcp port 6514
logging trap informational
logging origin-id hostname
logging source-interface Loopback0
```

---

# Common Event Format (CEF)

## Vue d'ensemble

**Common Event Format (CEF)** est un format de journaux standardisé pour les événements de sécurité conçu pour l'intégration SIEM.

**Développé par** : ArcSight (désormais Micro Focus), norme de secteur largement adoptée

**Cas d'utilisation courants** :

- Outils de sécurité (pare-feu, IDS/IPS, pare-feu d'application web)
- Plateformes de protection des endpoints
- Systèmes de prévention des pertes de données
- Systèmes d'authentification et de contrôle d'accès
- Intégration SIEM depuis des produits de sécurité divers

## Format de message CEF

**Structure** :

```
CEF:Version|Fournisseur|Produit|Version produit|ID signature|Nom|Sévérité|Extension
```

**Exemple** :
```
CEF:0|Palo Alto Networks|PAN-OS|9.1.0|THREAT|URL Filtering|7|rt=Jan 21 2026 14:32:15 src=10.0.1.50 dst=93.184.216.34 spt=52341 dpt=443 request=https://malicious.example.com act=blocked
```

## Champs d'en-tête CEF

| Champ | Description | Exemple |
|-------|-------------|---------|
| **Version** | Version du format CEF | 0 (norme actuelle) |
| **Fournisseur** | Nom du fournisseur | Palo Alto Networks, Cisco, Check Point |
| **Produit** | Nom du produit | PAN-OS, ASA, FortiGate |
| **Version produit** | Version du produit | 9.1.0 |
| **ID signature** | Identifiant de l'événement | THREAT, AUTH, CONFIG |
| **Nom** | Nom lisible de l'événement | URL Filtering, Login Failed |
| **Sévérité** | Échelle 0-10 | 0=Faible, 5=Moyen, 10=Critique |

**Échelle de sévérité** :

- 0-3 : Faible (informatif, problèmes mineurs)
- 4-6 : Moyen (avertissements, violations de politique)
- 7-8 : Élevé (menaces de sécurité, attaques)
- 9-10 : Critique (menaces sévères, compromissions réussies)

## Champs d'extension CEF

**Clés d'extension standard** (couramment utilisées) :

| Clé | Nom complet | Description | Exemple |
|-----|-------------|-------------|---------|
| **src** | Adresse source | Adresse IP source | 10.0.1.50 |
| **dst** | Adresse destination | Adresse IP destination | 93.184.216.34 |
| **spt** | Port source | Port TCP/UDP source | 52341 |
| **dpt** | Port destination | Port TCP/UDP destination | 443 |
| **suser** | Nom d'utilisateur source | Nom d'utilisateur source | jdupont |
| **duser** | Nom d'utilisateur destination | Nom d'utilisateur destination | admin |
| **act** | Action | Action effectuée | blocked, allowed, alerted |
| **app** | Protocole d'application | Protocole applicatif | HTTP, HTTPS, SSH, FTP |
| **request** | URL de requête | URL ou commande complète | https://example.com/chemin |
| **requestMethod** | Méthode de requête | Méthode HTTP | GET, POST, PUT, DELETE |
| **cn1-cn3** | Numéro personnalisé 1-3 | Champs numériques personnalisés | 1234 (octets transférés) |
| **cs1-cs6** | Chaîne personnalisée 1-6 | Champs de chaîne personnalisés | "User-Agent: Mozilla/5.0" |
| **rt** | Heure de réception | Heure de réception de l'événement | Jan 21 2026 14:32:15 |
| **outcome** | Résultat | Résultat de l'événement | success, failure, unknown |
| **reason** | Motif | Motif de l'action ou de l'échec | Identifiants invalides |
| **fileHash** | Hachage de fichier | Hachage de fichier (MD5, SHA256) | a1b2c3d4e5f6... |
| **filePath** | Chemin de fichier | Chemin complet du fichier | /var/log/suspect.exe |

## Exemples CEF par type d'événement

**Événement d'authentification** (Échec de connexion) :
```
CEF:0|Microsoft|Windows|Server 2019|4625|An account failed to log on|5|rt=Jan 21 2026 14:32:15 suser=admin src=10.0.1.50 outcome=failure reason=Unknown user name or bad password cs1Label=Domain cs1=EXAMPLE
```

**Événement pare-feu** (Connexion bloquée) :
```
CEF:0|Palo Alto Networks|PAN-OS|9.1.0|TRAFFIC|deny|8|rt=Jan 21 2026 14:32:15 src=10.0.1.50 dst=203.0.113.100 spt=52341 dpt=22 proto=TCP act=deny app=SSH
```

**Détection de logiciel malveillant** :
```
CEF:0|CrowdStrike|Falcon|6.42|MALWARE|Malware Detected|9|rt=Jan 21 2026 14:32:15 src=10.0.2.15 filePath=C:\\Users\\jdupont\\Downloads\\malware.exe fileHash=a1b2c3d4e5f6 act=quarantined outcome=success
```

**Pare-feu d'application web** (Injection SQL bloquée) :
```
CEF:0|F5 Networks|BIG-IP ASM|15.1.0|SQL_INJECTION|SQL Injection Attack|9|rt=Jan 21 2026 14:32:15 src=203.0.113.50 request=https://webapp.example.com/login?id=1' OR '1'='1 requestMethod=GET act=blocked
```

## Bonnes pratiques CEF

1. **Utiliser les clés d'extension standard** lorsque applicable (src, dst, suser) pour la compatibilité SIEM
2. **Champs personnalisés pour les données non standard** (cs1-cs6 pour les chaînes, cn1-cn3 pour les nombres)
3. **Toujours inclure l'horodatage** (champ rt) pour la corrélation précise des événements
4. **Échapper les caractères pipe** dans les valeurs d'extension (utiliser antislash : \|)
5. **Échapper les antislashs** dans les valeurs d'extension (utiliser double antislash : \\)
6. **Échapper les signes égal** dans les valeurs de champs personnalisés (utiliser antislash : \=)

---

# Journalisation structurée JSON

## Vue d'ensemble

**JSON (JavaScript Object Notation)** est la norme moderne pour la journalisation des applications et les journaux de services cloud.

**Cas d'utilisation courants** :

- Applications web modernes et microservices
- Environnements de conteneurs et Kubernetes
- Applications cloud-natives (AWS, Azure, GCP)
- Passerelles API et fonctions serverless
- Journaux d'applications SaaS

**Avantages** :

- Lisible par l'homme et analysable par les machines
- Support natif dans les plateformes SIEM modernes et d'agrégation de journaux
- Schéma flexible (peut accueillir toute structure de champs)
- Facile à générer depuis le code applicatif (bibliothèques disponibles pour tous les langages)

## Structure de journal JSON

**Champs minimum requis** :

```json
{
  "timestamp": "2026-01-21T14:32:15.003+01:00",
  "level": "INFO",
  "message": "Connexion utilisateur réussie",
  "logger": "auth.service",
  "context": {
    "user": "jdupont",
    "source_ip": "10.0.1.50",
    "action": "login",
    "outcome": "success"
  }
}
```

## Noms de champs standard

**Convention de nommage JSON recommandée** (snake_case) :

| Nom du champ | Type | Description | Exemple |
|-------------|------|-------------|---------|
| **timestamp** | chaîne (ISO 8601) | Horodatage de l'événement avec fuseau horaire | "2026-01-21T14:32:15+01:00" |
| **level** | chaîne | Niveau de journalisation | "INFO", "WARN", "ERROR", "DEBUG" |
| **message** | chaîne | Message lisible | "Connexion utilisateur réussie" |
| **logger** | chaîne | Nom du logger ou module | "auth.service", "app.controller" |
| **user_id** | chaîne | Identifiant utilisateur | "jdupont", "user@example.com" |
| **session_id** | chaîne | Identifiant de session | "abc123def456" |
| **request_id** | chaîne | ID de trace de requête | "req-7f8a9b0c" |
| **source_ip** | chaîne | Adresse IP source | "10.0.1.50" |
| **destination_ip** | chaîne | Adresse IP destination | "93.184.216.34" |
| **action** | chaîne | Action effectuée | "login", "create", "delete", "read" |
| **resource** | chaîne | Ressource affectée | "/api/users", "fichier.txt" |
| **outcome** | chaîne | Résultat de l'action | "success", "failure", "error" |
| **error_code** | chaîne | Code d'erreur ou type d'exception | "AUTH001", "NullPointerException" |
| **duration_ms** | nombre | Durée en millisecondes | 250 |
| **http_method** | chaîne | Méthode HTTP | "GET", "POST", "PUT", "DELETE" |
| **http_status** | nombre | Code de statut HTTP | 200, 404, 500 |
| **user_agent** | chaîne | Chaîne user agent | "Mozilla/5.0..." |

## Niveaux de journalisation

**Niveaux de journalisation standard** (équivalence RFC 5424) :

| Niveau | Sévérité | Utilisation | Exemple |
|--------|----------|-------------|---------|
| **TRACE** | Débogage | Débogage très détaillé | Valeurs de variables, entrée/sortie de fonctions |
| **DEBUG** | Débogage | Débogage détaillé | Flux logique, résultats intermédiaires |
| **INFO** | Informatif | Opérations normales | Service démarré, utilisateur connecté, transaction terminée |
| **WARN** | Avertissement | Problèmes potentiels | API dépréciée utilisée, tentative de nouvelle connexion |
| **ERROR** | Erreur | Conditions d'erreur | Connexion base de données échouée, erreur de validation |
| **FATAL/CRITICAL** | Critique | Erreurs sévères | Crash de l'application, erreur irrécupérable |

**Recommandation pour la production** :

- **Journaux de sécurité** : INFO et plus (INFO pour le succès, WARN pour les violations, ERROR pour les attaques)
- **Journaux d'application** : WARN et plus (minimiser le bruit tout en capturant les problèmes)
- **DEBUG/TRACE** : Désactivé en production (activer temporairement pour le dépannage)

## Contexte structuré

**Contexte imbriqué pour les champs liés** :

```json
{
  "timestamp": "2026-01-21T14:32:15.003+01:00",
  "level": "ERROR",
  "message": "Échec d'authentification",
  "logger": "auth.service",
  "user": {
    "id": "jdupont",
    "email": "jdupont@example.com",
    "role": "user"
  },
  "request": {
    "id": "req-7f8a9b0c",
    "method": "POST",
    "path": "/api/auth/login",
    "source_ip": "10.0.1.50",
    "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
  },
  "auth": {
    "method": "password",
    "outcome": "failure",
    "reason": "invalid_credentials",
    "attempts": 3
  },
  "error": {
    "code": "AUTH001",
    "type": "AuthenticationException",
    "message": "Nom d'utilisateur ou mot de passe invalide"
  }
}
```

## Exemples JSON par type d'événement

**Authentification réussie** :
```json
{
  "timestamp": "2026-01-21T14:32:15.003+01:00",
  "level": "INFO",
  "message": "Utilisateur authentifié avec succès",
  "logger": "auth.service",
  "user_id": "jdupont",
  "session_id": "sess-abc123",
  "source_ip": "10.0.1.50",
  "action": "login",
  "outcome": "success",
  "auth_method": "password_mfa",
  "duration_ms": 125
}
```

**Journal de requête API** :
```json
{
  "timestamp": "2026-01-21T14:32:16.120+01:00",
  "level": "INFO",
  "message": "Requête API traitée",
  "logger": "api.gateway",
  "request_id": "req-7f8a9b0c",
  "http_method": "GET",
  "http_path": "/api/users/jdupont",
  "http_status": 200,
  "source_ip": "10.0.1.50",
  "user_id": "admin",
  "duration_ms": 45,
  "response_size_bytes": 1024
}
```

**Erreur avec trace de pile** :
```json
{
  "timestamp": "2026-01-21T14:32:18.500+01:00",
  "level": "ERROR",
  "message": "Exception non gérée dans le traitement des paiements",
  "logger": "payment.service",
  "request_id": "req-payment-001",
  "user_id": "customer123",
  "error": {
    "type": "PaymentGatewayException",
    "message": "Délai d'attente de la passerelle de paiement dépassé",
    "code": "GATEWAY_TIMEOUT",
    "stack_trace": "PaymentGatewayException: Gateway timeout\n  at PaymentService.processPayment(PaymentService.java:123)"
  },
  "transaction": {
    "id": "txn-789xyz",
    "amount": 99.99,
    "currency": "CHF"
  }
}
```

## Bonnes pratiques JSON

1. **Toujours inclure l'horodatage** avec fuseau horaire (format ISO 8601)
2. **Utiliser snake_case** pour les noms de champs (convention cohérente)
3. **Minimiser l'imbrication** (1-2 niveaux maximum pour la lisibilité)
4. **Éviter de journaliser les données sensibles** (pas de mots de passe, numéros de carte complets, DCP sauf nécessité)
5. **Inclure les identifiants de contexte** (request_id, session_id, user_id) pour la corrélation
6. **Utiliser les données structurées** plutôt que de concaténer des chaînes dans le champ message
7. **Schéma cohérent** à travers l'application (utiliser une bibliothèque de journalisation avec validation de schéma)
8. **Un événement de journal par ligne** (JSON délimité par des nouvelles lignes pour faciliter l'analyse)

---

# Normes d'horodatage

## Format requis : ISO 8601

**Norme** : ISO 8601 avec informations de fuseau horaire

**Format** : `AAAA-MM-JJTHH:MM:SS.SSSSSS±HH:MM` ou `AAAA-MM-JJTHH:MM:SS.SSSZ`

**Exemples** :

- `2026-01-21T14:32:15+01:00` (Heure d'Europe centrale avec décalage)
- `2026-01-21T13:32:15Z` (UTC, suffixe 'Z' indique UTC)
- `2026-01-21T14:32:15.003+01:00` (avec millisecondes)
- `2026-01-21T14:32:15.123456+01:00` (avec microsecondes)

## Gestion des fuseaux horaires

**Recommandation** : Utiliser UTC pour tout stockage centralisé des journaux

**Justification** :

- Élimine les erreurs de conversion de fuseau horaire
- Simplifie la corrélation sur plusieurs emplacements géographiques
- Évite les complications liées à l'heure d'été
- Référence universelle pour les organisations multi-sites

## Exigences de précision

**Minimum** : Précision à la seconde (`AAAA-MM-JJTHH:MM:SS`)

**Recommandé** : Précision à la milliseconde (`AAAA-MM-JJTHH:MM:SS.SSS`)

- Requise pour les systèmes à volume élevé (centaines d'événements par seconde)
- Permet l'ordonnancement précis des événements dans la même seconde
- Nécessaire pour la corrélation de séquences d'événements rapides

**Optionnel** : Précision à la microseconde (`AAAA-MM-JJTHH:MM:SS.SSSSSS`)

- Utile pour les systèmes très performants
- Journalisation des transactions de base de données avec granularité sous-milliseconde

## Synchronisation de l'heure

**Exigence** : Toutes les sources de journaux DOIVENT synchroniser l'heure avec une source de temps faisant autorité selon ISMS-POL-A.8.17 (Synchronisation des horloges).

**Configuration NTP** :

- Serveur NTP primaire (Stratum 1 ou 2)
- Serveurs NTP secondaires pour la redondance
- Seuil de dérive d'horloge maximum : ±100 ms
- Alerte en cas d'échec de synchronisation NTP

**Importance** : Des horodatages précis sont essentiels pour :

- La corrélation d'événements sur plusieurs systèmes
- La reconstruction de la chronologie des incidents
- L'analyse forensique et les preuves légales
- La vérification de conformité

---

# Conventions de nommage des champs

## Normes de nommage

**Utiliser une convention de nommage cohérente** :

| Convention | Exemple | Cas d'utilisation |
|------------|---------|-------------------|
| **snake_case** | `source_ip`, `user_id`, `event_type` | Journaux JSON, applications Python |
| **camelCase** | `sourceIp`, `userId`, `eventType` | Applications JavaScript, certains SIEM |
| **dot.notation** | `event.type`, `user.id`, `source.ip` | ECS (Elastic Common Schema), champs imbriqués |

**Recommandation** : Choisir UNE convention et l'utiliser de manière cohérente dans toute l'organisation. Le snake_case est de plus en plus courant pour la journalisation de sécurité.

## Noms de champs standard

**Champs d'identité** :

- `user_id` / `user` / `username` — identifiant utilisateur
- `user_email` — adresse e-mail de l'utilisateur
- `service_account` — identifiant de compte de service
- `session_id` — identifiant de session
- `request_id` / `trace_id` — identifiant de trace de requête
- `transaction_id` — identifiant de transaction

**Champs réseau** :

- `source_ip` / `src_ip` — adresse IP source
- `destination_ip` / `dst_ip` — adresse IP destination
- `source_port` / `src_port` — port TCP/UDP source
- `destination_port` / `dst_port` — port TCP/UDP destination
- `protocol` — protocole réseau (TCP, UDP, ICMP)
- `hostname` — nom d'hôte du système

**Champs d'action** :

- `action` / `event_action` — action effectuée (login, create, delete, read, update)
- `event_type` / `event_category` — catégorie d'événement (authentification, autorisation, configuration)
- `outcome` / `result` — résultat (success, failure, error)
- `reason` — motif du résultat ou de l'action
- `severity` / `level` — niveau de sévérité

**Champs de ressource** :

- `resource` / `object` — ressource affectée
- `file_path` — chemin du fichier
- `file_hash` — hachage du fichier (MD5, SHA256)
- `url` / `request_url` — URL ou endpoint
- `api_endpoint` — endpoint API

**Champs temporels** :

- `timestamp` / `event_time` — horodatage de l'événement
- `duration` / `duration_ms` — durée en millisecondes
- `start_time` — horodatage de début
- `end_time` — horodatage de fin

**Champs d'application** :

- `application` / `app_name` — nom de l'application
- `environment` — environnement (production, staging, développement)
- `version` / `app_version` — version de l'application
- `component` / `module` — nom du composant ou du module

**Champs d'erreur** :

- `error_code` — code d'erreur
- `error_type` / `exception_type` — nom de classe d'exception
- `error_message` / `exception_message` — description de l'erreur
- `stack_trace` — trace de pile (pour les erreurs)

## Éviter les noms ambigus

**À NE PAS UTILISER** :

- `data` — trop générique, utiliser un nom spécifique (ex. `user_data`, `request_data`)
- `info` — ambigu, utiliser un nom spécifique (ex. `user_info` → `user_email`)
- `value` — non descriptif, utiliser un nom sémantique
- `temp` — objectif peu clair, utiliser un nom descriptif

**UTILISER** :

- Des noms descriptifs et auto-documentés
- Une terminologie cohérente dans toute l'organisation
- Les noms standard de l'ECS (Elastic Common Schema) lorsque applicable

---

# Encodage des caractères et échappement

## Encodage des caractères

**Norme** : Encodage UTF-8 pour tous les journaux

**Justification** :

- Support universel pour les caractères internationaux
- Efficace pour l'ASCII (1 octet par caractère)
- Compatible avec JSON, XML, les applications modernes

## Échappement des caractères spéciaux

**Syslog (RFC 5424)** :

- Pas d'échappement spécial requis dans le champ MSG
- Utiliser le format de données structurées pour les paires clé-valeur (échappement automatique)

**CEF** :

- Échapper les caractères pipe : `|` → `\|`
- Échapper les antislashs : `\` → `\\`
- Échapper les signes égal dans les valeurs d'extension : `=` → `\=`
- Échapper les nouvelles lignes : `\n` → `\\n`

**JSON** :

- Les bibliothèques JSON échappent automatiquement les caractères spéciaux
- Échappement manuel (si nécessaire) :
  - Guillemets doubles : `"` → `\"`
  - Antislashs : `\` → `\\`
  - Nouvelles lignes : caractère de nouvelle ligne → `\n`
  - Tabulations : caractère de tabulation → `\t`

## Longueurs maximales des champs

**Recommandations** (compatibilité SIEM) :

| Type de champ | Longueur maximale | Justification |
|--------------|-------------------|---------------|
| **Champs de chaîne** | 1024 caractères | Limites de champs de base de données SIEM |
| **Champ message** | 8192 caractères | Le message peut inclure des traces de pile |
| **Champs URL** | 2048 caractères | Support de longueur d'URL moderne |
| **Chemin de fichier** | 4096 caractères | Maximum de chemin Unix/Linux |
| **Identifiant utilisateur** | 256 caractères | Adresses e-mail, DN LDAP |

**Stratégie de troncature** :

- Tronquer depuis la fin pour les champs narratifs (messages, descriptions)
- Tronquer depuis le milieu pour les URL (préserver le domaine et les paramètres)
- Ne jamais tronquer les identifiants (ID utilisateur, ID transaction) — rejeter si trop long

---

# Guide d'implémentation

## Matrice de sélection du format de journaux

**Guide de décision** : Choisir le format de journaux selon le type de système

| Type de système | Format recommandé | Justification |
|----------------|------------------|---------------|
| **Équipements réseau** (Pare-feu, Routeur, Commutateur) | Syslog (RFC 5424) | Support natif, configuration minimale |
| **OS Unix/Linux** | Syslog (RFC 5424) | Support natif, infrastructure standard |
| **OS Windows** | Windows Event Log (natif) | Support natif, convertir en CEF ou JSON pour SIEM |
| **Outils de sécurité** (IDS, Pare-feu, WAF) | CEF | Intégration SIEM, événements de sécurité standardisés |
| **Applications web** | JSON | Facile à générer, schéma flexible |
| **Microservices** | JSON | Cloud-native, compatible conteneurs |
| **Services cloud** (AWS, Azure, GCP) | JSON | Format natif, intégration transparente |
| **Journaux de base de données** | JSON ou Syslog | Spécifique à l'application, JSON préféré |

## Considérations d'intégration SIEM

**Développement d'analyseurs syntaxiques** :

- Syslog : Utiliser les analyseurs intégrés, personnaliser pour l'extraction des données structurées
- CEF : Utiliser les analyseurs CEF intégrés, mapper les champs d'extension vers le schéma SIEM
- JSON : Configurer l'analyseur JSON, définir les mappages de champs

**Mapping de champs** :

- Mapper les champs de la source de journaux vers le schéma commun SIEM (normaliser les noms de champs)
- Créer des champs calculés pour les données dérivées (ex. géolocalisation depuis l'IP)
- Enrichir les événements avec la threat intelligence (recherches d'IP malveillantes)

**Optimisation des performances** :

- Utiliser le filtrage de niveau de journalisation approprié (INFO et plus pour la production)
- Implémenter l'échantillonnage pour les journaux à volume élevé et faible valeur
- Compresser les journaux avant la transmission (gzip, si le SIEM le supporte)
- Transfert de journaux par lot (collect-and-forward vs. temps réel)

## Recommandations de bibliothèques de journalisation

**Par langage de programmation** :

| Langage | Bibliothèque recommandée | Support journalisation structurée |
|---------|--------------------------|-----------------------------------|
| **Python** | `structlog`, `python-json-logger` | Oui (sortie JSON) |
| **Java** | `Logback`, `Log4j2` | Oui (encodeur JSON disponible) |
| **JavaScript/Node.js** | `winston`, `pino` | Oui (JSON natif) |
| **Go** | `zap`, `logrus` | Oui (JSON natif) |
| **C#/.NET** | `Serilog`, `NLog` | Oui (formateur JSON) |
| **Ruby** | `Lograge`, `semantic_logger` | Oui (sortie JSON) |
| **PHP** | `Monolog` | Oui (formateur JSON) |

**Exemple de configuration** (Python structlog) :

```python
import structlog

structlog.configure(
    processors=[
        structlog.stdlib.add_log_level,
        structlog.stdlib.add_logger_name,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.format_exc_info,
        structlog.processors.JSONRenderer()
    ],
    wrapper_class=structlog.stdlib.BoundLogger,
    logger_factory=structlog.stdlib.LoggerFactory(),
)

log = structlog.get_logger()
log.info("user_login", user_id="jdupont", source_ip="10.0.1.50", outcome="success")
```

---

# Maintenance du document

## Déclencheurs de mise à jour

Ce document de référence peut être mis à jour lorsque :

- De nouvelles normes de format de journaux émergent ou les normes existantes sont mises à jour
- Des changements de plateforme SIEM nécessitent un nouveau support de format
- Des problèmes d'analyse syntaxique des journaux sont identifiés nécessitant des clarifications de format
- Les équipes de développement d'applications demandent des conseils sur les nouveaux formats
- Les meilleures pratiques du secteur évoluent (ex. mises à jour du schéma ECS)

## Responsabilité

**Propriétaire du document** : Responsable SOC / Équipe d'architecture de sécurité  
**Fréquence de révision** : Trimestrielle ou selon les besoins  
**Autorité de mise à jour** : Mise à jour technique (aucun processus d'approbation SMSI requis)

---

# Relation avec ISMS-POL-A.8.15

Ce document fournit des **conseils d'implémentation technique** qui peuvent informer :

- La sélection du format de journaux lors de l'intégration de nouveaux systèmes (ISMS-IMP-A.8.15.1)
- Le développement d'analyseurs syntaxiques de journaux pour l'intégration SIEM (ISMS-IMP-A.8.15.2)
- La standardisation des noms de champs à travers les sources de journaux organisationnels
- La formation des développeurs et administrateurs système sur les normes de journalisation

Ce document NE :

- Remplace NI n'étend les exigences d'ISMS-POL-A.8.15
- N'établit PAS de sélections de formats de journaux obligatoires
- Ne crée PAS d'obligations de conformité
- Ne définit PAS de critères d'audit

Toutes les exigences de contrôle de journalisation sont définies exclusivement dans ISMS-POL-A.8.15 et implémentées via les procédures ISMS-IMP-A.8.15.

---

**FIN DU DOCUMENT**

*Il s'agit d'un document de référence technique à des fins de sensibilisation uniquement. Il n'établit pas d'exigences SMSI et ne crée pas d'obligations de conformité.*
<!-- QA_VERIFIED: 2026-04-04 -->
