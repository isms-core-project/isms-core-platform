<!-- ISMS-CORE:CTX:ISMS-CTX-A.8.24-FR-cryptographic-landscape-reference:framework:CTX:a.8.24 -->
**ISMS-CTX-A.8.24 — Référence du paysage cryptographique**
**Vue d'ensemble des algorithmes et des suites de chiffrement du secteur (Référence technique non-SMSI)**

---

**Contrôle du document**

| Champ | Valeur |
|-------|--------|
| **Titre du document** | Référence du paysage cryptographique |
| **Type de document** | Interne — Référence technique (non SMSI) |
| **Identifiant du document** | ISMS-CTX-A.8.24 |
| **Créateur du document** | Responsable de la sécurité des systèmes d'information (RSSI) |
| **Propriétaire du document** | Directeur général (DG) |
| **Approuvé par** | Direction générale |
| **Date de création** | [Date] |
| **Version** | 1.0 |
| **Date de version** | [À déterminer] |
| **Classification** | Interne |
| **Statut** | Brouillon |

**Distribution** : Ingénierie de sécurité, Architectes système, Équipes de développement (pour sensibilisation)

---

⚠️ **IMPORTANT — DOCUMENT DE SUPPORT TECHNIQUE NON-SMSI**

Ce document est fourni à des fins d'information et de sensibilisation uniquement. Il ne fait PAS partie du SMSI et ne remplace PAS ISMS-POL-A.8.24. Les exigences contraignantes sont définies exclusivement dans **ISMS-POL-A.8.24 (Utilisation de la cryptographie)**.

---

# Objectif et portée du document

## Objectif

Ce document fournit une vue d'ensemble technique du paysage des algorithmes cryptographiques couramment rencontrés dans les systèmes d'information modernes. Il vise à soutenir :

- La sensibilisation technique aux options cryptographiques
- La compréhension du cycle de vie et de la maturité des algorithmes
- Le contexte pour la prise de décisions cryptographiques
- La planification de l'implémentation future

## Relation avec le SMSI

Ce document est une **référence technique non contraignante**. Toutes les exigences de contrôle cryptographique sont définies exclusivement dans ISMS-POL-A.8.24.

## Organisation du contenu

Ce référentiel organise les algorithmes cryptographiques par fonction :

- Chiffrement symétrique (confidentialité des données)
- Chiffrement asymétrique (échange de clés, signatures numériques)
- Fonctions de hachage (intégrité des données, authentification)
- Suites de chiffrement TLS/SSL (communications sécurisées)
- Longueurs de clés et statut de maturité des algorithmes

---

# Algorithmes de chiffrement symétrique

## Chiffrement par blocs

Algorithmes de chiffrement par blocs symétriques couramment rencontrés :

| Algorithme | Taille du bloc | Longueurs de clé | Statut | Cas d'utilisation courants |
|-----------|----------------|------------------|--------|---------------------------|
| **AES** (Advanced Encryption Standard) | 128-bit | 128, 192, 256-bit | Moderne, largement déployé | Chiffrement des données, TLS, VPN, chiffrement disque |
| **ChaCha20** | Flux 64 octets | 256-bit | Moderne, optimisé mobile | TLS (appareils mobiles), VPN (WireGuard) |
| **3DES** (Triple DES) | 64-bit | 168-bit (efficace 112-bit) | Héritage, déprécié | Support systèmes héritage uniquement |
| **DES** (Data Encryption Standard) | 64-bit | 56-bit | Obsolète, compromis | Référence historique uniquement |
| **Blowfish** | 64-bit | 32-448 bit | Héritage | Référence historique, remplacé par AES |
| **Twofish** | 128-bit | 128, 192, 256-bit | Moderne mais moins courant | Alternative à AES |

**Observations sectorielles** :

- AES est la norme dominante pour le chiffrement symétrique à l'échelle mondiale
- ChaCha20 gagne en adoption dans les environnements à ressources limitées
- 3DES déprécié par le NIST (interdit après 2023 dans la plupart des contextes)
- DES considéré cryptographiquement compromis depuis la fin des années 1990

## Modes d'opération des chiffres par blocs

Modes courants pour opérer les chiffres par blocs :

| Mode | Authentification | Parallélisable | Statut | Notes |
|------|-----------------|----------------|--------|-------|
| **GCM** (Mode Galois/Compteur) | Oui (AEAD) | Oui | Moderne, recommandé | Chiffrement authentifié, défaut TLS 1.2+ |
| **CCM** (Compteur avec CBC-MAC) | Oui (AEAD) | Partiel | Moderne | Environnements contraints |
| **CTR** (Mode Compteur) | Non | Oui | Moderne | Nécessite authentification séparée (HMAC) |
| **CBC** (Chaîne de blocs en chiffrement) | Non | Partiel | Héritage | Vulnérable aux attaques par oracle de remplissage |
| **ECB** (Dictionnaire électronique de chiffrement) | Non | Oui | Obsolète | Déterministe, non recommandé |
| **XTS** | Non | Oui | Moderne | Chiffrement disque (BitLocker, dm-crypt) |

**Observations sectorielles** :

- Les modes AEAD (GCM, CCM) fortement préférés pour les nouvelles implémentations
- Le mode CBC nécessite une implémentation soigneuse pour éviter les vulnérabilités
- Le mode ECB fournit une sécurité insuffisante pour la plupart des applications

## Chiffres de flux

| Chiffre | Longueur de clé | Statut | Cas d'utilisation courants |
|---------|-----------------|--------|---------------------------|
| **ChaCha20-Poly1305** | 256-bit | Moderne | TLS 1.3, VPN mobile, protocoles modernes |
| **RC4** (Rivest Cipher 4) | 40-2048 bit | Obsolète, compromis | Référence historique uniquement |
| **Salsa20** | 128, 256-bit | Moderne | Prédécesseur de ChaCha20 |

---

# Algorithmes de chiffrement asymétrique

## Algorithmes à clé publique

Algorithmes asymétriques couramment rencontrés :

| Algorithme | Longueurs de clé | Statut | Cas d'utilisation principaux |
|-----------|------------------|--------|------------------------------|
| **RSA** (Rivest-Shamir-Adleman) | 2048, 3072, 4096-bit | Moderne (≥2048-bit) | Certificats TLS, SSH, chiffrement email, signature de code |
| **ECDSA** (DSA sur courbe elliptique) | P-256, P-384, P-521 | Moderne | Certificats TLS, SSH, mobile/IoT, blockchain |
| **EdDSA** (DSA sur courbe d'Edwards) | Ed25519 (équiv. 256-bit) | Moderne | Clés SSH, protocoles modernes, cryptomonnaie |
| **DH** (Diffie-Hellman) | 2048, 3072, 4096-bit | Moderne (≥2048-bit) | Échange de clés (héritage) |
| **ECDH** (DH sur courbe elliptique) | P-256, P-384, P-521, X25519 | Moderne | TLS 1.2+, échange de clés |
| **DSA** (Algorithme de signature numérique) | 2048, 3072-bit | Héritage | Systèmes anciens uniquement, remplacé par RSA/ECDSA |
| **RSA-1024** | 1024-bit | Obsolète, déprécié | Référence historique uniquement |

**Observations sectorielles** :

- RSA-2048 minimum pour les nouveaux déploiements (NIST, CA/Browser Forum)
- RSA-3072 de plus en plus adopté pour les clés à long terme (durée de vie >5 ans)
- ECC (ECDSA, EdDSA) fournit une sécurité équivalente avec des tailles de clés plus petites
- Ed25519 gagne en adoption pour SSH et les protocoles modernes

## Équivalence des longueurs de clés

Équivalence de sécurité approximative entre familles d'algorithmes :

| Symétrique | RSA/DH | ECC | Hachage | Bits de sécurité |
|-----------|--------|-----|---------|-----------------|
| 3DES (2-clés) | 1024 | 160 | SHA-1 | ~80 bits (déprécié) |
| AES-128 | 3072 | 256 (P-256) | SHA-256 | ~128 bits |
| AES-192 | 7680 | 384 (P-384) | SHA-384 | ~192 bits |
| AES-256 | 15360 | 521 (P-521) | SHA-512 | ~256 bits |

**Source** : NIST SP 800-57 Partie 1 Rév. 5

---

# Fonctions de hachage et authentification de messages

## Fonctions de hachage cryptographiques

| Algorithme | Taille de sortie | Statut | Cas d'utilisation courants |
|-----------|------------------|--------|---------------------------|
| **SHA-256** | 256-bit | Moderne | Signatures numériques, certificats, stockage mots de passe (avec KDF), blockchain |
| **SHA-384** | 384-bit | Moderne | Applications haute sécurité, signatures long terme |
| **SHA-512** | 512-bit | Moderne | Applications haute sécurité, hachage mots de passe (avec KDF) |
| **SHA-3** (Keccak) | 224, 256, 384, 512-bit | Moderne | Alternative à SHA-2, blockchain |
| **BLAKE2** | 256, 512-bit | Moderne | Hachage haute performance, stockage mots de passe |
| **SHA-1** | 160-bit | Obsolète, compromis | Référence historique uniquement, déprécié 2017 |
| **MD5** | 128-bit | Obsolète, compromis | Référence historique uniquement, déprécié 2004 |

**Observations sectorielles** :

- SHA-256 minimum pour les nouvelles implémentations (certificats, signatures)
- SHA-1 déprécié pour les certificats (2017), migration git en cours
- MD5 considéré cryptographiquement compromis

## Codes d'authentification de messages (MAC)

| Algorithme | Basé sur | Taille de sortie | Statut |
|-----------|----------|------------------|--------|
| **HMAC-SHA256** | SHA-256 | 256-bit | Moderne |
| **HMAC-SHA384** | SHA-384 | 384-bit | Moderne |
| **HMAC-SHA512** | SHA-512 | 512-bit | Moderne |
| **Poly1305** | ChaCha20 | 128-bit | Moderne (avec ChaCha20) |
| **HMAC-SHA1** | SHA-1 | 160-bit | Héritage, en cours de suppression |
| **HMAC-MD5** | MD5 | 128-bit | Obsolète |

## Fonctions de hachage des mots de passe

Fonctions spécialisées pour le stockage des mots de passe :

| Fonction | Type | Statut | Notes |
|----------|------|--------|-------|
| **Argon2** (Argon2id) | KDF mot de passe | Moderne, recommandé | Vainqueur du Password Hashing Competition 2015 |
| **bcrypt** | KDF mot de passe | Moderne | Largement déployé, facteur de travail automatique |
| **scrypt** | KDF mot de passe | Moderne | Fonction à mémoire intensive |
| **PBKDF2-HMAC-SHA256** | KDF mot de passe | Moderne | Approuvé NIST, facteur de coût plus faible |
| **SHA-256 (brut)** | Hachage général | Inapproprié | Trop rapide pour le stockage des mots de passe |
| **MD5 (brut)** | Hachage général | Obsolète | Inadapté aux mots de passe |

**Observations sectorielles** :

- Le hachage des mots de passe nécessite des fonctions de dérivation de clés (KDF) avec facteur de travail
- Les fonctions de hachage brutes (SHA-256, MD5) inadaptées au stockage des mots de passe
- Argon2id recommandé pour les nouvelles implémentations (OWASP)

---

# Suites de chiffrement TLS/SSL

**Note importante** : Les exemples de suites de chiffrement ci-dessous sont illustratifs et non exhaustifs. Ils sont fournis uniquement pour expliquer les constructions et conventions de nommage courantes du secteur. Ils ne représentent pas des configurations approuvées, requises ou attendues au sein de [Organisation].

## Suites de chiffrement TLS 1.3

TLS 1.3 a simplifié la conception des suites de chiffrement (5 suites standardisées) :

| Suite de chiffrement | Échange de clés | Chiffre en masse | Statut |
|---------------------|-----------------|------------------|--------|
| **TLS_AES_256_GCM_SHA384** | ECDHE | AES-256-GCM | Moderne, recommandé |
| **TLS_AES_128_GCM_SHA256** | ECDHE | AES-128-GCM | Moderne, recommandé |
| **TLS_CHACHA20_POLY1305_SHA256** | ECDHE | ChaCha20-Poly1305 | Moderne, optimisé mobile |
| **TLS_AES_128_CCM_SHA256** | ECDHE | AES-128-CCM | Moderne, IoT/contraint |
| **TLS_AES_128_CCM_8_SHA256** | ECDHE | AES-128-CCM (tag 8 octets) | Moderne, appareils contraints |

**Observations sectorielles** :

- TLS 1.3 supprime la complexité de négociation des suites de chiffrement
- Toutes les suites TLS 1.3 fournissent la confidentialité persistante (ECDHE obligatoire)
- Toutes les suites TLS 1.3 fournissent le chiffrement authentifié (AEAD)

## Suites de chiffrement TLS 1.2 (Exemples courants sélectionnés)

| Suite de chiffrement | Échange de clés | Auth. | Chiffre en masse | MAC | Statut |
|---------------------|-----------------|-------|------------------|-----|--------|
| **TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384** | ECDHE | RSA | AES-256-GCM | (AEAD) | Moderne, largement déployé |
| **TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256** | ECDHE | RSA | AES-128-GCM | (AEAD) | Moderne, largement déployé |
| **TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256** | ECDHE | RSA | ChaCha20-Poly1305 | (AEAD) | Moderne, mobile |
| **TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384** | ECDHE | ECDSA | AES-256-GCM | (AEAD) | Moderne, certificats ECC |
| **TLS_RSA_WITH_AES_256_GCM_SHA384** | RSA | RSA | AES-256-GCM | (AEAD) | Héritage, pas de confidentialité persistante |
| **TLS_RSA_WITH_3DES_EDE_CBC_SHA** | RSA | RSA | 3DES-CBC | SHA-1 | Obsolète, déprécié |
| **TLS_RSA_WITH_RC4_128_SHA** | RSA | RSA | RC4 | SHA-1 | Obsolète, compromis |

**Observations sectorielles** :

- ECDHE fournit la confidentialité persistante (recommandé)
- Les modes AEAD (GCM, Poly1305) préférés à CBC + HMAC
- L'échange de clés RSA (sans ECDHE) manque de confidentialité persistante
- Le mode CBC vulnérable aux attaques par oracle de remplissage

## Protocoles et suites de chiffrement dépréciés/obsolètes

| Protocole/Chiffre | Déprécié | Raison |
|-------------------|----------|--------|
| **SSL v2** | 2011 | Multiples failles cryptographiques |
| **SSL v3** | 2015 | Attaque POODLE, chiffrement faible |
| **TLS 1.0** | 2020 | Cryptographie obsolète, attaque BEAST |
| **TLS 1.1** | 2020 | Cryptographie obsolète |
| **Chiffre RC4** | 2015 | Biais dans le flux de clés, attaques pratiques |
| **Chiffre 3DES** | 2023 | Attaque Sweet32, taille de bloc 64-bit |
| **Chiffres de qualité export** | 1990s-2015 | Intentionnellement affaiblis (40-56 bit) |
| **Chiffrement NULL** | Toujours | Pas de chiffrement |
| **DH anonyme (ADH)** | Toujours | Pas d'authentification, vulnérable MITM |

---

# Longueurs de clés et cycle de vie des algorithmes

## Longueurs de clés couramment référencées dans les recommandations sectorielles

Longueurs de clés couramment référencées (NIST, BSI, ENISA) :

| Famille d'algorithme | Longueur de clé minimum | Valide jusqu'à | Notes |
|---------------------|------------------------|----------------|-------|
| **RSA (signature, échange de clés)** | 2048-bit | ~2030 | 3072-bit pour clés >2030 |
| **RSA (clés long terme)** | 3072-bit | Au-delà de 2030 | AC racines, signature de code |
| **Diffie-Hellman** | 2048-bit | ~2030 | 3072-bit pour usage futur |
| **ECDSA/ECDH** | P-256 (256-bit) | Au-delà de 2030 | P-384 pour haute sécurité |
| **AES** | 128-bit | Au-delà de 2030 | 256-bit pour haute sécurité |
| **Fonctions de hachage** | SHA-256 | Au-delà de 2030 | SHA-384 pour haute sécurité |

**Source** : NIST SP 800-57 Partie 1 Rév. 5, BSI TR-02102-1

## Statut du cycle de vie des algorithmes

Classification de la maturité et du statut d'adoption des algorithmes :

| Statut | Définition | Exemples |
|--------|------------|----------|
| **Moderne** | Bonne pratique actuelle, activement déployé | AES, RSA-2048+, ECDSA P-256+, SHA-256, TLS 1.3 |
| **Largement utilisé** | Mature, stable, large déploiement | TLS 1.2, RSA-2048, SHA-256, ChaCha20 |
| **Héritage** | Vieillissant, en cours de remplacement | 3DES, DSA, SHA-1 (hors certificat), TLS 1.1 |
| **Déprécié** | Plus recommandé, suppression en cours | SSL v3, TLS 1.0, RC4, signatures MD5 |
| **Obsolète** | Cryptographiquement compromis | DES, MD5 (usage sécurité), RC4, SHA-1 (certificats) |
| **Émergent** | Standardisé mais déploiement limité | Algorithmes post-quantiques (ML-KEM, ML-DSA) |

## Statut de la cryptographie post-quantique

Standardisation de la cryptographie post-quantique (PQC) du NIST :

| Algorithme | Type | Statut (2024-2025) | Notes |
|-----------|------|-------------------|-------|
| **ML-KEM** (Kyber) | Encapsulation de clés | FIPS 203 publié 2024 | Échange de clés, mode hybride avec ECDH |
| **ML-DSA** (Dilithium) | Signature numérique | FIPS 204 publié 2024 | Signatures, mode hybride avec ECDSA/RSA |
| **SLH-DSA** (SPHINCS+) | Signature numérique | FIPS 205 publié 2024 | Signatures basées sur le hachage sans état |
| **FN-DSA** (Falcon) | Signature numérique | À l'étude | Basé sur les réseaux, signatures compactes |

**Observations sectorielles** :

- Algorithmes post-quantiques en cours de standardisation mais pas encore largement déployés
- Modes hybrides (PQC + classique) attendus pendant la période de transition
- Échange de clés hybride TLS 1.3 (X25519 + ML-KEM) en développement
- Les autorités de certification commencent les émissions d'essai PQC

---

# Validité et cycle de vie des certificats

## Évolution historique de la validité des certificats

Périodes de validité maximale des certificats TLS publics :

| Période | Validité maximale | Autorité |
|---------|------------------|----------|
| Avant 2011 | Aucune limite définie | Discrétion du fournisseur |
| 2011-2015 | 60 mois (5 ans) | CA/Browser Forum |
| 2015-2017 | 39 mois (~3 ans) | CA/Browser Forum Ballot 193 |
| 2017-2020 | 825 jours (~27 mois) | CA/Browser Forum Ballot 193 |
| 2020-présent | 398 jours (~13 mois) | CA/Browser Forum Ballot SC-31 |

## Validité future des certificats (Ballot SC-081v3)

CA/Browser Forum Ballot SC-081v3 (adopté avril 2025) :

| Date d'entrée en vigueur | Validité maximale | Période de réutilisation DCV |
|--------------------------|-------------------|------------------------------|
| 15 mars 2026 | 200 jours | 200 jours |
| 15 mars 2027 | 100 jours | 100 jours |
| 15 mars 2029 | 47 jours | 10 jours |

**Observations sectorielles** :

- Les durées de vie des certificats se réduisent pour améliorer la sécurité et l'agilité
- Les durées plus courtes augmentent l'importance de la gestion automatisée du cycle de vie
- L'ICP interne/privée n'est pas soumise aux exigences du CA/Browser Forum

**Note sur l'ICP interne** : Les politiques de certificats internes sont déterminées par l'évaluation des risques et le contexte opérationnel. Les organisations peuvent choisir des durées plus courtes ou plus longues selon leur posture de sécurité spécifique.

---

# Normes et sources de référence

## Organismes normatifs faisant autorité

| Organisation | Domaine de compétence | Publications clés |
|-------------|----------------------|------------------|
| **NIST** | Normes cryptographiques (États-Unis) | FIPS 140-2/3, série SP 800 |
| **BSI** | Normes cryptographiques (Allemagne) | TR-02102-1 à TR-02102-4 |
| **ENISA** | Recommandations cryptographiques (UE) | Rapports d'algorithmes, lignes directrices |
| **IETF** | Normes de protocoles | RFC (TLS, SSH, IPsec) |
| **CA/Browser Forum** | Normes des autorités de certification | Exigences de base, ballots |
| **ISO/IEC JTC 1/SC 27** | Normes de sécurité de l'information | ISO/IEC 18033 (algorithmes de chiffrement) |

## Documents de référence clés

**Publications NIST** :

- FIPS 140-2/140-3 : Exigences de sécurité pour les modules cryptographiques
- NIST SP 800-52 Rév. 2 : Directives pour les implémentations TLS
- NIST SP 800-57 Partie 1 Rév. 5 : Recommandations de gestion des clés
- NIST SP 800-131A Rév. 2 : Transition de l'utilisation des algorithmes cryptographiques

**Publications BSI** :

- TR-02102-1 : Mécanismes cryptographiques — Recommandations et longueurs de clés
- TR-02102-2 : Utilisation de TLS
- TR-02102-3 : Algorithmes cryptographiques appropriés
- TR-02102-4 : Utilisation de Secure Shell (SSH)

**RFC IETF** :

- RFC 8446 : Protocole Transport Layer Security (TLS) Version 1.3
- RFC 5246 : Protocole Transport Layer Security (TLS) Version 1.2
- RFC 8032 : Algorithme de signature numérique sur courbe d'Edwards (EdDSA)

## Suivi de la dépréciation des algorithmes

Les organisations surveillent généralement le statut des algorithmes via :

- Programme de validation des algorithmes cryptographiques du NIST (CAVP)
- Liste des algorithmes dépréciés du NIST
- Politiques de sécurité des fournisseurs de navigateurs (Chrome, Firefox, Safari, Edge)
- Suivi des ballots du CA/Browser Forum
- Bulletins de sécurité des fournisseurs (OpenSSL, Microsoft, Apple, etc.)

---

# Maintenance du document

## Déclencheurs de mise à jour

Ce document de référence peut être mis à jour lorsque :

- Une standardisation majeure d'algorithme se produit (NIST, RFC IETF)
- Des dépréciations significatives d'algorithmes sont annoncées
- Des mises à jour du protocole TLS/SSL sont publiées
- Des jalons de déploiement de la cryptographie post-quantique sont atteints
- Les exigences de base du CA/Browser Forum changent

## Responsabilité

**Propriétaire du document** : Architecture de sécurité / Expert en cryptographie  
**Fréquence de révision** : Annuelle ou selon les besoins  
**Autorité de mise à jour** : Mise à jour technique (aucun processus d'approbation SMSI)

---

# Relation avec ISMS-POL-A.8.24

Ce document fournit un **contexte technique** qui peut informer :

- La sensibilisation à l'agilité cryptographique (ISMS-POL-A.8.24 Section 2.6)
- Les discussions sur la sélection des algorithmes lors de la planification de l'implémentation
- L'évaluation des risques des systèmes cryptographiques héritage
- La compréhension de l'évolution des normes sectorielles

---

**FIN DU DOCUMENT**

*Ce document est une référence technique à des fins de sensibilisation uniquement. Il n'établit pas d'exigences SMSI et ne crée pas d'obligations de conformité.*

<!-- QA_VERIFIED: 2026-04-04 -->
